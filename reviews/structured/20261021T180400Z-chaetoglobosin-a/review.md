# Chaetoglobosin A: confirmed constitutional mismatch and guarded repair prerequisites

- Review: 20261021T180400Z-chaetoglobosin-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T17:52:08.497884Z
- Finished UTC: 2026-10-21T18:04:00.470244Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The A-labelled record stores a C34 K-like constitution instead of authentic C32 chaetoglobosin A, a confirmed blocker. Its local stereochemistry also differs from the original K drawing, and the literal NPAtlas A representation is not an exact replacement. A valid three-star ChEBI A MOL provides a candidate, but invalid committed target SMILES and unresolved old-key biological claims require explicit repair prerequisites. Missing original BGC and occurrence bodies keep the review partial.

## Scope And Provenance

One complete generated owner and any referenced components, assessed claim by claim for exact identity, provenance, origin, producer and occurrence scope, biosynthesis, classification, optional content and audit history.

Selection: Campaign record 127, batch 013, selected in path order from the fresh-main authoritative validated catalogue and the separately validated targets in earlier batch commits (publication tracked separately). At selection, 174 of 3116 current records had campaign coverage and 2942 remained. The population search included ignored files. Exactly one target is assessed here.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1c2402097718c138b081e00943de8f04de0541cd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-0c963509fd | data/natural_products/alkaloids/chaetoglobosin-a.yaml | generated | chaetoglobosin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | naturalproductmech:mibig-0c963509fd | The documented target strict validator completed; scientific support is assessed separately. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-0c963509fd | All 3,116 current record files agree with PATHS.tsv and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-0c963509fd | All 3,116 current records passed the documented byte-reproduction gate against committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-0c963509fd | The exhaustive review queue produced 8,928 diagnostic rows across 12 queues; this deterministic output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-0c963509fd | The configured identifier-label gate passed using the existing ontology caches: 13,449 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,744 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate on the current main baseline | passed | True | naturalproductmech:mibig-0c963509fd | The full documented just qc recipe passed on the unchanged main baseline during batch004. Test summary: 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). All configured lint, governance, documentation, provenance, source-queue, schema, rendering, reproduction, filing-integrity and reporting stages completed successfully. |
| Complete owner and referenced-component scope | passed | True | naturalproductmech:mibig-0c963509fd | The complete owner and all six captured source-row sets were read after successful official intake and agree with the pinned preparation. The external component set is empty. Fresh strict validation is retained separately. |
| Exact-congener final-product and occurrence source closure | unavailable | True | naturalproductmech:mibig-0c963509fd | Required 2007 main and two historical occurrence bodies remain unavailable; exact chemistry is independently disputed. |
| Stored chemical representation and complete source row | passed | True | naturalproductmech:mibig-0c963509fd | Fresh intake derivation agrees with the stored graph; the source selector, full row and prepared snapshot were independently rechecked. |
| Named A versus exact stored constitution | failed | True | naturalproductmech:mibig-0c963509fd | The stored C34 K-like constitution is not the original C32 chaetoglobosin A identity. |
| Literal NPAtlas exact structure | failed | True | naturalproductmech:mibig-0c963509fd | NPA013078 encodes a different C32 constitution and additionally differs from the primary-supported complete A graph at C9 precision and all three alkene geometries. |
| Existing eligible-target representation safety | failed | True | naturalproductmech:mibig-0c963509fd | CHEBI:68798 official MOL is valid, but the committed/default SMILES is invalid. The current copy-based replacement must not execute before a maintained target-representation repair and new full target pin. |

## Scientific And Domain Assessments

### Native status and complete retained audit history

provenance: supported. Targets: naturalproductmech:mibig-0c963509fd.

All retained history events record SEEDED_FROM_SOURCES provenance. The native status remains SEEDED; the review changes neither history nor scientific content.

### Present optional assertions and enrichment scope

completeness: not_applicable. Targets: naturalproductmech:mibig-0c963509fd.

No optional pathway, causal graph, molecular target, activity, application, clinical-status, cross-record relation or discussion is asserted. Potential enrichment is distinct from checking the present producer, occurrence and locus claims.

### Exact-key computed classification provenance

representation: supported. Targets: naturalproductmech:mibig-0c963509fd.

The owner reproduces its exact-key NPClassifier result and version npclassifier.gnps2.org@2026-09-07, including Alkaloids filing, superclass/class labels and glycoside prediction false. Computed labels are not independent evidence for precursor use or natural origin. Any corrected chemical identity must be reclassified against its corrected effective key.

### Literal organism identifier routing

grounding: supported. Targets: naturalproductmech:mibig-0c963509fd.

The literal source identifiers and names resolve consistently. Their experimental occurrence and stock claims remain separately assessed.

### Taxonomic synonym and experimental-stock boundaries

provenance: supported. Targets: naturalproductmech:mibig-0c963509fd.

NCBI 371126 S. macrospora includes Diplodia macrospora as a synonym. This is a taxonomic bridge only; it does not turn the primary K/L isolation into support for the named A structure, or identify an unspecified P. expansum stock.

### Native producer and experimental-host transcriptomic applicability

completeness: not_applicable. Targets: naturalproductmech:mibig-0c963509fd.

P. expansum and S. macrospora source stocks are absent. The catalogue gives no exact fungal transcriptomic mapping for the native biosynthesis or isolation claims.

### biosynthesis_origin and producer_organisms[0]

evidence: concern. Targets: naturalproductmech:mibig-0c963509fd.

The family has positive native fungal isolation evidence, but this owner combines an A label with a K-like constitution and disputed stereochemistry. The named-A P. expansum correlation must be adjudicated after exact identity is resolved; it is not evidence that the stored stereograph is natively produced. This biology dependency is part of the separate chemical identity repair, not a duplicate finding.

### biosynthetic_gene_clusters[0] and imported AM779763.1 association

evidence: unknown. Targets: naturalproductmech:mibig-0c963509fd.

The PKS-NRPS CheA and auxiliary-gene SI supports the named cluster architecture and native silencing design. It does not independently verify the precise A-versus-C outcome, the retained K-like graph or full accession boundary. Empty coordinates are not an error. Do not add knockout or final-product enzyme methods from protocol descriptions.

### occurrences[0], occurrences[1], occurrences[2]

evidence: concern. Targets: naturalproductmech:mibig-0c963509fd.

All three LOTUS triples are full-key source assertions for the retained graph. The 1989 study positively isolates named K/L from Diplodia macrospora; the 1980 title is K-specific and the 1988 full body is unavailable. None permits automatic transfer to authentic A after a structural repair. Preserve individual raw rows, their source context and unresolved exact stereo applicability; no wholesale occurrence deletion or taxon substitution is justified here.

### Stored representation and source-concept provenance

identity: supported. Targets: naturalproductmech:mibig-0c963509fd.

The complete source row BGC0000968:1 and source-concept hash reproduce this stored representation; this does not establish that the upstream compound label is correct. Formula, charge, Standard and fixed-H distinctions are independently recorded. Primary support and any conflicting exact xref are assessed separately.

### Exact authority eligibility and source representation

provenance: supported. Targets: naturalproductmech:mibig-0c963509fd.

No exact eligible row exists in the committed ChEBI projection for this owner. Current bounded name/key searches do not justify a different congener or a two-star grounding.

### A, K-like constitution and exact K drawing differences

identity: concern. Targets: naturalproductmech:mibig-0c963509fd.

The wrong named identity is confirmed independently of authority agreement by formula and complete connectivity. Local C10 and alkene checks further prevent treating the raw graph as verified K. The original A hand report is positive, but no absolute K or P assignment is transferred from it.

## Findings

### C127-F-WRONG-IDENTITY: Named chaetoglobosin A contains a different C34 constitution

blocker / open / confirmed; issue key: mibig-bgc0000968-1-chaetoglobosin-a-k-like-identity.

The owner is labelled A but stores a C34 K-like constitution instead of original C32 A. Its C10S/17Z assignments also differ from original K depiction, so a label-only K rename is insufficient. The literal NPA link is a third precision/alkene representation and cannot serve as a replacement template. The eligible A target is available as a valid official MOL, but its committed/default SMILES is invalid and currently unsafe to copy.

## Recommended Actions And Acceptance Checks

### C127-ACTION-IDENTITY

Adjudicate source_id=BGC0000968:1, version5, complete source-row SHA256=01a47507c397cb14d2ea4d340739bf8f69f28c6a21930f40f576eafa5755fa70, exact old key=RSYKJHLWNMXRKZ-RVUXUPINSA-N, old SMILES=CC[C@H]1[C@H]2[C@@H](NC(=O)[C@@]23[C@@H](/C=C/C[C@@H](/C=C(\[C@H](C(=O)/C=C/C3=O)O)/C)C)[C@H]4[C@@]1(O4)C)[C@@H](C)C5=CNC6=CC=CC=C65, old database_ids=npatlas:NPA013078, and all taxon/locus/method fields as one source assertion. Preserve those raw bytes. For named A, independently approve the complete primary-numbered C32 graph, all nine tetrahedral centres and 13E/17E/21E against the original A report and valid official CHEBI:68798 MOL (SHA eb0ea40e600c6f7ab63a38109f4f2c8c82e6980b4767a479933f57372bdccfa4); do not use the C10-only diagnostic MOL, current NPA013078, or the later schematic as a full repair. First fix the eligible target representation through a maintained, manifested extraction enhancement or a separately implemented full-row-pinned official-MOL correction contract. Pin the present target SHA78990a5ab6d83b4bb6c5672f5e2476c757c87c656c5fd31b7ecfc4968529af2a and official MOL; require parsed Standard key OUMWCYMRLMEZJH-VOXRAUTJSA-N, exact fixed-H, formula/charge and complete stereochemical agreement before committing a NEW target row/hash. Only then consider existing REPLACE_WITH_CHEBI with that new target hash, freshly derived Standard InChI and tetrahedral flag, stable primary citation and actual attribution. Current raw collision scan finds one old-key owner and no new-key MIBiG owner; repeat ignored-inclusive owner/path and source/target uniqueness checks at application time and fail closed on a collision. Preserve the minted BGC0000968:1 source concept, while reviewing emitted CHEBI identity, label, path and references. Withhold the old literal xref and never transfer old-key LOTUS/classifier/assay data merely because the owner path persists. The three complete old-key LOTUS pins are 10.1002/HLCA.19880710806=0594b4f59a646e2b050062bfd18476f95bb41c72129e35802b49fd2f6de641e6; 10.1021/JF60227A011=4911b2e6dfb2ab1f415a4be4f7e7d66f3ea12a1419339323ca19e3f18b464328; 10.3987/COM-88-S96=987d49e8f5b3aea40ee1367d6660808c5b57879a4606bb18db774d0e3bfed3df; each requires independent exact-congener adjudication, not blanket reassignment to A or K. Named-A Penicillium correlation, methods and source citation must separately support the repaired graph before being carried over. Preserve BGC0000968:2 chaetoglobosin C and all unrelated owners. Any science citation/strain/method action must use an explicitly reviewed and tested composition path because existing consumers reject structure_correction_note. A label-only K rename or unguarded arbitrary-SMILES override is not an implemented or sufficient repair.

- Reject complete source/target drift, invalid SMILES, formula/key/fixed-H or stereochemical disagreement, duplicate selectors and source/target collisions.
- Verify every primary-numbered atom and all three alkene geometries of the approved complete A target; do not treat a local-C10 diagnostic as a complete molecule.
- Demonstrate old raw rows remain unchanged and old-key xrefs, LOTUS triples, classifier and assays are not copied to the new identity; retain an explicit audit discussion.
- Adjudicate every surviving producer/locus/citation claim for exact A and test overlay composition; keep the distinct C owner unchanged.
- After separately authorized implementation, run maintained extraction/seed canary, reproduction, strict/corpus and full QC; this review does not execute repairs.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R127-OWNER | data/natural_products/alkaloids/chaetoglobosin-a.yaml; Complete owner, all present assertions and complete audit history | supports | Root read the complete chaetoglobosin A owner after official intake. It contains 3 occurrence, 1 producer and 1 locus assertions. Referenced external components are empty. Present optional fields: none. |
| R127-LOCAL | /private/tmp/npm-review-work/127/local-sources.json; Complete resolved owner and all six captured exact matching source-row sets | context_only | Root read every captured MIBiG, LOTUS, ChEBI structures/origins, CyanoMetDB and NPClassifier row, including empty sets. The owner and captured rows match the prepared source snapshot. Separate PubChem raw observations are assessed by the scientific section. Source fidelity alone does not establish experimental support. |
| R127-Q10678663 | https://www.wikidata.org/wiki/Q10678663; Literal P225/P685 fields in retained complete multi-entity response | context_only | Literal Q10678663 scientific names and NCBI identifiers match the imported rows. This verifies identifier routing; it does not validate the occurrence citation, production or stock identity. |
| R127-TAXON-CONTEXT | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;retmode=xml&amp;id=162396,1905,1981977,2062,2502037,27334,292,339670,36816,371126,38033,40623,5149,54571,66425,68195,953739,97398; ScientificName, Rank, ParentTaxId and OtherNames for the exact relevant taxon records | context_only | NCBI 371126 S. macrospora includes Diplodia macrospora as a synonym. This is a taxonomic bridge only; it does not turn the primary K/L isolation into support for the named A structure, or identify an unspecified P. expansum stock. |
| R127-IMODULON | https://imodulondb.org/api/datasets; Complete official 20-organism/28-dataset catalogue | context_only | The retained current catalogue was read and its bytes match the previously inspected catalogue. It establishes membership only, not production or module applicability. |
| S127-E-LOCAL | data/natural_products/alkaloids/chaetoglobosin-a.yaml; Complete actual owner, resolved components and all exact matching local source rows | supports | Exact source selector BGC0000968:1 version 5; complete parsed source row SHA256 01a47507c397cb14d2ea4d340739bf8f69f28c6a21930f40f576eafa5755fa70. Current methods 'Gene expression correlated with compound production'; source grades BGC_CORRELATED/CLUSTER_CORRELATED. Present science claims were compared with the formal intake; source preparation is not treated as another formal target. |
| S127-E-A1982 | DOI:10.1248/cpb.30.1609; Complete isolation article; Chart 1 and PGP/rice culture isolation | supports | Original named A and C are C32H36N2O5 compounds isolated from Chaetomium globosum 68-SA-2. A has indolyl-CH2 and a ring methyl. The current A-labelled row has a different C34 constitution; primary named-A occurrence cannot be silently transferred to that graph. |
| S127-E-KL1989 | DOI:10.3987/COM-88-S96; Complete original 13-page paper, Figure 1 and native isolation/incorporation experiments | supports | Diplodia macrospora ATCC 36896 cultures yielded K (1) and L (2); K contains extra C10/C11 methyl groups. The native isolation and precursor-feeding results are K/L-specific. The independently checked original K drawing differs locally from the retained graph at C10 and C17=C18, so even matching K constitution does not establish its entire retained stereograph. |
| S127-E-SI2007 | DOI:10.1021/ja072884t; Complete S1–S2, CheA silencing and culture/HPLC methods | supports | The SI establishes a native P. expansum antisense/RNA-silencing design: inverted 2.9 kb CheA fragment under alcA, native protoplast transformation, Southern verification and induction/repression culture/HPLC procedures. It supplies no congener-resolved final A/C outcome trace. These methods cannot by themselves establish exact graph-specific correlation or a clean deletion. |
| S127-E-PEER | /private/tmp/npm-review-work/shared-next-batch013/bgc-science/chaeto-peer-check/peer-check.json; Original 1982/1989/2020 drawings and explicit numbered graph maps; actual local read recorded in the peer packet | supports | Primary-to-graph comparison distinguishes authentic A constitution from K constitution and checks local K C10/alkene stereochemistry. Later 2020 depictions are not a complete replacement template or an independent natural absolute determination. |
| S127-E-OCCMETA | PMID:7358926; Exact original 1980 title metadata; no abstract or full body | partial | The 1980 cited DOI 10.1021/jf60227a011 resolves to a paper on chaetoglobosin K from Diplodia macrospora. This is a bibliographic congener lead, not independently inspected isolation/absolute-structure evidence. |
| S127-E-GAP | /private/tmp/npm-review-work/shared-next-batch013/bgc-science/source-notes.json; Bounded original-source routes and retained scopes | unknown | The original 2007 main is blocked; 1980 K and 1988 DOI 10.1002/hlca.19880710806 full bodies remain unavailable. The latter M-named lead is not adjudicated from its title alone. The three LOTUS assertions and exact final-product correlation cannot be reassigned merely by renaming the owner. |
| C127-OWNER | data/natural_products/alkaloids/chaetoglobosin-a.yaml; Complete owner and all local-source rows; no referenced components | supports | The complete owner denotes chaetoglobosin A under naturalproductmech:mibig-0c963509fd. Its exact source selector is BGC0000968:1, version 5, with complete parsed raw-row SHA256 01a47507c397cb14d2ea4d340739bf8f69f28c6a21930f40f576eafa5755fa70. The official intake and prepared owner bytes agree. |
| C127-GRAPH | /private/tmp/npm-review-work/127/chemistry.json; Fresh intake RDKit result and frozen Standard/fixed-H comparison | supports | The stored SMILES recomputes to RSYKJHLWNMXRKZ-RVUXUPINSA-N, formula C34H40N2O5, formal charge 0; stored InChI/key agree. These are representation checks, not experimental identity proof. |
| C127-COMPARISON | /private/tmp/npm-review-work/shared-next-batch013/chemistry-prep/chemical-comparison.json; Record 127; exact source rows and each graph comparison | supports | Exact Standard, fixed-H, formula, charge and stereo comparisons of the retained owner, complete raw rows and current authority responses; primary experimental proof is assessed separately. |
| C127-LOCAL-SEARCH | /private/tmp/npm-review-work/127/chemistry-search-receipt.json; Exact full key, label, slug and source selector in raw/owner/curation trees | supports | Ignored-inclusive bounded search preserves all matching paths; an absent curation decision does not imply a missing scientific source. |
| C127-CHEBI-SEARCH-1 | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=RSYKJHLWNMXRKZ-RVUXUPINSA-N&amp;size=100; Literal key search; chebi-key-chaetoglobosin-a.json | supports | 1 returned name/key results; evaluate exact key and stars, not name similarity. |
| C127-CHEBI-SEARCH-2 | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=chaetoglobosin+A&amp;size=100; Literal name search; chebi-name-chaetoglobosin-a.json | supports | 24 returned name/key results; evaluate exact key and stars, not name similarity. |
| C127-AUTH-1 | https://mibig.secondarymetabolites.org/repository/BGC0000968.5/annotations.json; compounds[].structure; BGC0000968.5.json | supports | current MIBiG BGC0000968:1: parsed key RSYKJHLWNMXRKZ-RVUXUPINSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C127-AUTH-2 | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/RSYKJHLWNMXRKZ-RVUXUPINSA-N/property/MolecularFormula,InChI,InChIKey,CanonicalSMILES,IsomericSMILES,Charge/JSON; PropertyTable.Properties[].SMILES; pubchem-key-chaetoglobosin-a.json | supports | PubChem 6440494: parsed key RSYKJHLWNMXRKZ-RVUXUPINSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C127-AUTH-3 | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/chaetoglobosin%20A/property/MolecularFormula,InChI,InChIKey,CanonicalSMILES,IsomericSMILES,Charge/JSON; PropertyTable.Properties[].SMILES; pubchem-name-chaetoglobosin-a.json | context_only | PubChem 6438437: parsed key OUMWCYMRLMEZJH-VOXRAUTJSA-N; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C127-AUTH-4 | https://www.npatlas.org/api/v1/compound/NPA013078; smiles; retry-NPA013078.json | context_only | NPAtlas literal NPA013078: parsed key OUMWCYMRLMEZJH-YOAIXWIWSA-N; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C127-AUTH-5 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/219830/; default_structure.smiles; CHEBI219830.json | context_only | ChEBI JSON 219830: parsed key None; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C127-AUTH-6 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/219830/; official molfile endpoint; CHEBI219830-official.mol | supports | ChEBI MOL 219830: parsed key RSYKJHLWNMXRKZ-RVUXUPINSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C127-AUTH-7 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/68798/; default_structure.smiles; CHEBI68798.json | context_only | ChEBI JSON 68798: parsed key None; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C127-AUTH-8 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/68798/; official molfile endpoint; CHEBI68798-official.mol | context_only | ChEBI MOL 68798: parsed key OUMWCYMRLMEZJH-VOXRAUTJSA-N; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C127-AUTH-9 | https://www.wikidata.org/wiki/Special:EntityData/Q76386752.json; P2017; Q76386752.json | supports | Wikidata Q76386752: parsed key RSYKJHLWNMXRKZ-RVUXUPINSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C127-AUTH-10 | https://www.wikidata.org/wiki/Special:EntityData/Q76386752.json; P233; Q76386752.json | context_only | Wikidata Q76386752: parsed key RSYKJHLWNMXRKZ-UHFFFAOYSA-N; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. Canonical P233 is not an isomeric stereo assertion; compare P2017 when present. |
| C127-PRIMARY-A | DOI:10.1248/cpb.30.1618; Complete 11-page structure paper; original p1626 Chart7 and configuration discussion | supports | The original A structure is C32H36N2O5, with an indolylmethyl substituent and ring methyl, not the stored C34 graph with additional C10 methyl and ring ethyl. The paper assigns 13E,17E,21E and reports the A monohydrate absolute structure by anomalous oxygen scattering. That reported experiment is distinguished from an independent re-refinement of the cited diffraction data. |
| C127-PRIMARY-K | DOI:10.3987/COM-88-S96; Original 1989 introduction and Figure1 compound1; original pixels and numbered C10/17-18 comparison | supports | Original K has the C34 constitution, but its depicted local C10 is R and its 17 alkene is E. The retained graph has C10S and 17Z. Thus renaming the current owner K would not establish an exact structure match either. No natural K absolute hand is newly selected from this drawing. |
| C127-PEER-MAPPING | /private/tmp/npm-review-work/shared-next-batch013/chemistry-prep/chaeto-peer-addendum-001.json; Independent original-pixel reread, numbered complete graph correspondence and all alkene maps | supports | Two independent numbered comparisons agree: authentic A is C32; stored C34 is K-like constitution with C10S/13E/17Z/21E. Original K depicts C10R/13E/17E/21E. Literal NPA013078 has C32 A constitution but leaves C9 undefined and encodes all three alkenes Z; eligible CHEBI:68798 official MOL has the complete A graph and all E. The later 2020 schematic is not a complete replacement template. |
| C127-CURRENT-ROUTING | /private/tmp/npm-review-work/127/current-chemistry-routing.json; Current complete source/target rows, collision scan and actual MOL parsing | supports | Current source key has exactly one MIBiG compound owner, BGC0000968:1; the proposed A key has no MIBiG owner and exactly one committed ChEBI row. That three-star row has invalid SMILES despite a valid official MOL with its declared A key. Its current row SHA is 78990a5ab6d83b4bb6c5672f5e2476c757c87c656c5fd31b7ecfc4968529af2a; blindly invoking the replacement loader would copy invalid text. |
| C127-STRUCTURE-CONTRACT | src/naturalproductmech/curate/structure_corrections.py; Inspected current maintained contract | supports | REPLACE_WITH_CHEBI pins the complete source and complete eligible target row, requires unique distinct owners and copies target SMILES. It withholds old xrefs and preserves source correction provenance; unrelated inventories join only on the new exact key. |
| C127-SEED-CONTRACT | scripts/seed_from_sources.py; Inspected current maintained contract | supports | Source corrections precede exact-key joins. Current claim-reference, xref-exclusion and strain integrations reject structure_correction_note unless separately reviewed/tested composition is implemented. Minted source concept follows accession plus compound index, not label. |
| C127-REFERENCE-CONTRACT | src/naturalproductmech/curate/claim_references.py; Inspected current maintained contract | supports | The full-row-pinned claim-reference consumer explicitly rejects a structure-corrected row; citation routing cannot be silently stacked with an identity repair. |
| C127-CHEBI-CONTRACT | scripts/extract_chebi.py; Inspected current maintained contract | supports | The committed identity projection admits only three-star default structures. The proposed target representation must be repaired through a maintained, manifested extraction or explicit guarded representation contract, not by editing a generated owner or blindly copying invalid JSON. |

## Limits And Additional Notes

- This is a claim-level review of present assertions and bounded source gaps, not an exhaustive search for every later paper or an obligation to add every optional mechanism.
- No identity finding is duplicated here; the chemistry action must preserve and separately adjudicate old-key producer/locus and each LOTUS assertion before graph migration.
- The native method is RNA silencing, not automatically a clean knockout. No collection strain or exact AM779763.1 sequence comparison was independently established in this science packet.
- Original access times are reused. The peer evidence date is a local re-read time, not an external retrieval.
- Authority matches establish the representations actually returned at their retained access times; they are not independent experimental structure or absolute-hand determinations. Root and science sections separately assess organism, locus, classification and history claims.
- The original A paper reports the absolute X-ray determination; underlying diffraction data were not independently re-refined. The K drawing comparison supports exact depicted configurations, not a new absolute-hand determination.
- No complete replacement K/P graph is selected. Old-key biological assertions and authority labels cannot settle congener identity by consensus.
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
review_id: 20261021T180400Z-chaetoglobosin-a
title: 'Chaetoglobosin A: confirmed constitutional mismatch and guarded repair prerequisites'
started_at: '2026-10-21T17:52:08.497884Z'
finished_at: '2026-10-21T18:04:00.470244Z'
completion: partial
verdict: needs_curation
scientific_review: true
summary: The A-labelled record stores a C34 K-like constitution instead of authentic
  C32 chaetoglobosin A, a confirmed blocker. Its local stereochemistry also differs
  from the original K drawing, and the literal NPAtlas A representation is not an
  exact replacement. A valid three-star ChEBI A MOL provides a candidate, but invalid
  committed target SMILES and unresolved old-key biological claims require explicit
  repair prerequisites. Missing original BGC and occurrence bodies keep the review
  partial.
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
  - path: curation/pubchem_bioassay_exclusions.tsv
    sha256: 76f9cbb17e62a270afed637b5058a553cfe85c754c6c9ec406635f12dae572fa
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
    role: context
  - path: data/natural_products/alkaloids/carbazomycin-b.yaml
    sha256: ee2d77b905d7e3158e521dc43ab0e8dc795cad0d6791f1a119b35072c44af4a3
    role: context
  - path: data/natural_products/alkaloids/carquinostatin-a.yaml
    sha256: 363433a8631354f0c1aeecb31592162b13e514a725fa625d825122bf4370b508
    role: context
  - path: data/natural_products/alkaloids/carquinostatin-b.yaml
    sha256: 12699a3ef0bc0b098441f90dd24c3a5323d62d1f8f397d88437984d7d769ee7d
    role: context
  - path: data/natural_products/alkaloids/cc-1065.yaml
    sha256: 18807ddce1f23840d55147cc331acf26c162f174d929473c833712ae1368f3ca
    role: context
  - path: data/natural_products/alkaloids/celesticetin.yaml
    sha256: 350fa68eb60fe724287f9368a7389fb6721b30af53cb69be0a46349530a47a8d
    role: context
  - path: data/natural_products/alkaloids/cepaciachelin.yaml
    sha256: d7f040cf3d0c84a874b4a8a16824b1976a705a981d4689711d749849ec649d8c
    role: context
  - path: data/natural_products/alkaloids/chaetoglobosin-a.yaml
    sha256: ade0d70a3f0c31506cb39562482bf0e09ace40b303ff965e3c6150ff70f5e6c5
    role: target
  - path: data/natural_products/alkaloids/chaetoglobosin-c.yaml
    sha256: 9a1bf49fde80bca26c948c350609bafed6853871a75339aa1301b38aad5fe68a
    role: context
  - path: data/natural_products/alkaloids/chaetoglobosin-p.yaml
    sha256: 0308e9b1b2258370d93d04398111270812a720e2e151bf9fc29a214a7e3cbad1
    role: context
  - path: data/natural_products/alkaloids/chloramphenicol.yaml
    sha256: d1c483e457d58b0306462795af8f027a3ed4dd22d781ed6044b193151a83a793
    role: context
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
  - path: scripts/extract_pubchem_bioassay.py
    sha256: 24f9d794e7cf97c420351cb751f8767f7d81a5f22aed01669b2318d6755e7c00
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
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
    sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
  - path: tests/test_bioassay_exclusions.py
    sha256: 099a0b8f6f51ce93406344440b63d99db7203486ed92797d90990005bdb6bbd0
    role: context
scope:
  description: One complete generated owner and any referenced components, assessed
    claim by claim for exact identity, provenance, origin, producer and occurrence
    scope, biosynthesis, classification, optional content and audit history.
  selection: Campaign record 127, batch 013, selected in path order from the fresh-main
    authoritative validated catalogue and the separately validated targets in earlier
    batch commits (publication tracked separately). At selection, 174 of 3116 current
    records had campaign coverage and 2942 remained. The population search included
    ignored files. Exactly one target is assessed here.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-0c963509fd
targets:
- target_id: naturalproductmech:mibig-0c963509fd
  path: data/natural_products/alkaloids/chaetoglobosin-a.yaml
  label: chaetoglobosin A
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
  - naturalproductmech:mibig-0c963509fd
  command: just validate-strict data/natural_products/alkaloids/chaetoglobosin-a.yaml
    --out /private/tmp/npm-review-work/127/strict.tsv
  exit_code: 0
  scope_note: Actual command finished 2026-10-21T17:52:10.229998Z
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
    for batch013 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch013. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-0c963509fd
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
    Reused for batch013 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch013. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-0c963509fd
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
    for batch013 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch013. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-0c963509fd
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
    for batch013 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch013. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-0c963509fd
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
    transcript: /private/tmp/npm-native-checks/batch-004/qc.log. Reused for batch013
    only after a fresh fetch/clean branch, equal commit/tree and two reads of all
    9,182 tracked byte streams and modes (208,070,649 bytes), including a recheck
    after the fresh authoritative catalogue. This gate was not rerun for batch013.
    Original execution times, scope, warnings, exceptions and skips are retained.'
  target_ids:
  - naturalproductmech:mibig-0c963509fd
- check_id: R127-FULL-OWNER
  name: Complete owner and referenced-component scope
  status: passed
  required: true
  summary: The complete owner and all six captured source-row sets were read after
    successful official intake and agree with the pinned preparation. The external
    component set is empty. Fresh strict validation is retained separately.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  evidence_ids:
  - R127-OWNER
  - R127-LOCAL
- check_id: S127-C-PRIMARY
  name: Exact-congener final-product and occurrence source closure
  status: unavailable
  required: true
  summary: Required 2007 main and two historical occurrence bodies remain unavailable;
    exact chemistry is independently disputed.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  evidence_ids:
  - S127-E-GAP
  - S127-E-SI2007
  - S127-E-PEER
- check_id: C127-C-REPRESENTATION
  name: Stored chemical representation and complete source row
  status: passed
  required: true
  summary: Fresh intake derivation agrees with the stored graph; the source selector,
    full row and prepared snapshot were independently rechecked.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  evidence_ids:
  - C127-OWNER
  - C127-GRAPH
  - C127-COMPARISON
- check_id: C127-C-NAMED-IDENTITY
  name: Named A versus exact stored constitution
  status: failed
  required: true
  summary: The stored C34 K-like constitution is not the original C32 chaetoglobosin
    A identity.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  evidence_ids:
  - C127-OWNER
  - C127-PRIMARY-A
  - C127-PRIMARY-K
  - C127-PEER-MAPPING
  - C127-GRAPH
- check_id: C127-C-LITERAL-NPA
  name: Literal NPAtlas exact structure
  status: failed
  required: true
  summary: NPA013078 encodes a different C32 constitution and additionally differs
    from the primary-supported complete A graph at C9 precision and all three alkene
    geometries.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  evidence_ids:
  - C127-COMPARISON
  - C127-PEER-MAPPING
  - C127-AUTH-1
  - C127-AUTH-2
  - C127-AUTH-3
  - C127-AUTH-4
  - C127-AUTH-5
  - C127-AUTH-6
  - C127-AUTH-7
  - C127-AUTH-8
  - C127-AUTH-9
  - C127-AUTH-10
- check_id: C127-C-REPAIR-READINESS
  name: Existing eligible-target representation safety
  status: failed
  required: true
  summary: CHEBI:68798 official MOL is valid, but the committed/default SMILES is
    invalid. The current copy-based replacement must not execute before a maintained
    target-representation repair and new full target pin.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  evidence_ids:
  - C127-CURRENT-ROUTING
  - C127-STRUCTURE-CONTRACT
  - C127-CHEBI-CONTRACT
evidence:
- evidence_id: R127-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/chaetoglobosin-a.yaml
  locator: Complete owner, all present assertions and complete audit history
  accessed_at: '2026-10-21T17:52:39.707072Z'
  support: supports
  summary: 'Root read the complete chaetoglobosin A owner after official intake. It
    contains 3 occurrence, 1 producer and 1 locus assertions. Referenced external
    components are empty. Present optional fields: none.'
  snapshot_sha256: ade0d70a3f0c31506cb39562482bf0e09ace40b303ff965e3c6150ff70f5e6c5
- evidence_id: R127-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/127/local-sources.json
  locator: Complete resolved owner and all six captured exact matching source-row
    sets
  accessed_at: '2026-10-21T17:52:39.707072Z'
  support: context_only
  summary: Root read every captured MIBiG, LOTUS, ChEBI structures/origins, CyanoMetDB
    and NPClassifier row, including empty sets. The owner and captured rows match
    the prepared source snapshot. Separate PubChem raw observations are assessed by
    the scientific section. Source fidelity alone does not establish experimental
    support.
  snapshot_sha256: 649894b62a0efe3726df31a1df285934704f3a434a674c583f3a7500675f0d45
- evidence_id: R127-Q10678663
  kind: database
  reference: https://www.wikidata.org/wiki/Q10678663
  locator: Literal P225/P685 fields in retained complete multi-entity response
  accessed_at: '2026-10-21T17:25:35.481159Z'
  support: context_only
  summary: Literal Q10678663 scientific names and NCBI identifiers match the imported
    rows. This verifies identifier routing; it does not validate the occurrence citation,
    production or stock identity.
  snapshot_sha256: 026cf7dce61f76ea1be554bf995a269a5531a82c3a0c74c5873851c736a1752b
- evidence_id: R127-TAXON-CONTEXT
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&retmode=xml&id=162396,1905,1981977,2062,2502037,27334,292,339670,36816,371126,38033,40623,5149,54571,66425,68195,953739,97398
  locator: ScientificName, Rank, ParentTaxId and OtherNames for the exact relevant
    taxon records
  accessed_at: '2026-10-21T17:25:35.685538Z'
  support: context_only
  summary: NCBI 371126 S. macrospora includes Diplodia macrospora as a synonym. This
    is a taxonomic bridge only; it does not turn the primary K/L isolation into support
    for the named A structure, or identify an unspecified P. expansum stock.
  snapshot_sha256: 83ff126040853b0ab6de8dbf4dab0b64eaf4b2aea314a68d6caddfcba16f66dd
- evidence_id: R127-IMODULON
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete official 20-organism/28-dataset catalogue
  accessed_at: '2026-10-21T17:25:35.092545Z'
  support: context_only
  summary: The retained current catalogue was read and its bytes match the previously
    inspected catalogue. It establishes membership only, not production or module
    applicability.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: S127-E-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/chaetoglobosin-a.yaml
  locator: Complete actual owner, resolved components and all exact matching local
    source rows
  accessed_at: '2026-10-21T17:57:59.073007Z'
  support: supports
  summary: Exact source selector BGC0000968:1 version 5; complete parsed source row
    SHA256 01a47507c397cb14d2ea4d340739bf8f69f28c6a21930f40f576eafa5755fa70. Current
    methods 'Gene expression correlated with compound production'; source grades BGC_CORRELATED/CLUSTER_CORRELATED.
    Present science claims were compared with the formal intake; source preparation
    is not treated as another formal target.
  snapshot_sha256: ade0d70a3f0c31506cb39562482bf0e09ace40b303ff965e3c6150ff70f5e6c5
- evidence_id: S127-E-A1982
  kind: primary_source
  reference: DOI:10.1248/cpb.30.1609
  locator: Complete isolation article; Chart 1 and PGP/rice culture isolation
  accessed_at: '2026-10-21T17:15:34.597248Z'
  support: supports
  summary: Original named A and C are C32H36N2O5 compounds isolated from Chaetomium
    globosum 68-SA-2. A has indolyl-CH2 and a ring methyl. The current A-labelled
    row has a different C34 constitution; primary named-A occurrence cannot be silently
    transferred to that graph.
  snapshot_sha256: e3f1204a5d49dd61e0a5d6b35a75d1b97258c211720e3e0eab5f9bd6a306b127
- evidence_id: S127-E-KL1989
  kind: primary_source
  reference: DOI:10.3987/COM-88-S96
  locator: Complete original 13-page paper, Figure 1 and native isolation/incorporation
    experiments
  accessed_at: '2026-10-21T17:23:38.715689Z'
  support: supports
  summary: Diplodia macrospora ATCC 36896 cultures yielded K (1) and L (2); K contains
    extra C10/C11 methyl groups. The native isolation and precursor-feeding results
    are K/L-specific. The independently checked original K drawing differs locally
    from the retained graph at C10 and C17=C18, so even matching K constitution does
    not establish its entire retained stereograph.
  snapshot_sha256: 08fcff157ca802ab18f1f1c8c0efdae6c5596538139bd8ba3247e3dbe884a4e3
- evidence_id: S127-E-SI2007
  kind: primary_source
  reference: DOI:10.1021/ja072884t
  locator: Complete S1–S2, CheA silencing and culture/HPLC methods
  accessed_at: '2026-10-21T17:16:45.695657Z'
  support: supports
  summary: 'The SI establishes a native P. expansum antisense/RNA-silencing design:
    inverted 2.9 kb CheA fragment under alcA, native protoplast transformation, Southern
    verification and induction/repression culture/HPLC procedures. It supplies no
    congener-resolved final A/C outcome trace. These methods cannot by themselves
    establish exact graph-specific correlation or a clean deletion.'
  snapshot_sha256: 892944301ee980c5b07b9eb0a103b050820354c85c2dc126bcb14f9579f714ea
- evidence_id: S127-E-PEER
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch013/bgc-science/chaeto-peer-check/peer-check.json
  locator: Original 1982/1989/2020 drawings and explicit numbered graph maps; actual
    local read recorded in the peer packet
  accessed_at: '2026-10-21T17:36:21.431111Z'
  support: supports
  summary: Primary-to-graph comparison distinguishes authentic A constitution from
    K constitution and checks local K C10/alkene stereochemistry. Later 2020 depictions
    are not a complete replacement template or an independent natural absolute determination.
  snapshot_sha256: 54278a05f0e6888a75afaf8ea0e4ec0808a0ffa898ca86dd74af59324a7cf972
- evidence_id: S127-E-OCCMETA
  kind: database
  reference: PMID:7358926
  locator: Exact original 1980 title metadata; no abstract or full body
  accessed_at: '2026-10-21T17:22:27.182465Z'
  support: partial
  summary: The 1980 cited DOI 10.1021/jf60227a011 resolves to a paper on chaetoglobosin
    K from Diplodia macrospora. This is a bibliographic congener lead, not independently
    inspected isolation/absolute-structure evidence.
  snapshot_sha256: df1c7ae15380582b6823ac46739060988d85d4c77aec2f5cd128680b015f5047
- evidence_id: S127-E-GAP
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch013/bgc-science/source-notes.json
  locator: Bounded original-source routes and retained scopes
  accessed_at: '2026-10-21T17:30:25.183480Z'
  support: unknown
  summary: The original 2007 main is blocked; 1980 K and 1988 DOI 10.1002/hlca.19880710806
    full bodies remain unavailable. The latter M-named lead is not adjudicated from
    its title alone. The three LOTUS assertions and exact final-product correlation
    cannot be reassigned merely by renaming the owner.
  snapshot_sha256: 86ba58da529384d774d2e5b81fb4825893bf1fa9beda7e82b7957337b9b18350
  search_scope: Retained official ACS main/SI routes, CLOCKSS original 1989 paper,
    exact PubMed DOI metadata and bounded 1988 publisher searches in the frozen source-preparation
    receipts. Ignored-inclusive local source inventory was used. No renewed blocked
    requests or whole-paper absence claims.
- evidence_id: C127-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/chaetoglobosin-a.yaml
  locator: Complete owner and all local-source rows; no referenced components
  accessed_at: '2026-10-21T18:00:40.368411Z'
  support: supports
  summary: The complete owner denotes chaetoglobosin A under naturalproductmech:mibig-0c963509fd.
    Its exact source selector is BGC0000968:1, version 5, with complete parsed raw-row
    SHA256 01a47507c397cb14d2ea4d340739bf8f69f28c6a21930f40f576eafa5755fa70. The official
    intake and prepared owner bytes agree.
  snapshot_sha256: ade0d70a3f0c31506cb39562482bf0e09ace40b303ff965e3c6150ff70f5e6c5
- evidence_id: C127-GRAPH
  kind: validation
  reference: /private/tmp/npm-review-work/127/chemistry.json
  locator: Fresh intake RDKit result and frozen Standard/fixed-H comparison
  accessed_at: '2026-10-21T17:52:09.193680Z'
  support: supports
  summary: The stored SMILES recomputes to RSYKJHLWNMXRKZ-RVUXUPINSA-N, formula C34H40N2O5,
    formal charge 0; stored InChI/key agree. These are representation checks, not
    experimental identity proof.
  snapshot_sha256: e6b06c43be6aa069ffadd879a547a3a1d06d43b15d2016747c6e7c3ee8923946
- evidence_id: C127-COMPARISON
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch013/chemistry-prep/chemical-comparison.json
  locator: Record 127; exact source rows and each graph comparison
  accessed_at: '2026-10-21T17:23:24.463910Z'
  support: supports
  summary: Exact Standard, fixed-H, formula, charge and stereo comparisons of the
    retained owner, complete raw rows and current authority responses; primary experimental
    proof is assessed separately.
  snapshot_sha256: 503b2ba573d5eef465b41aa483433a9b2b92cce169c7270520b63466b4f5539f
- evidence_id: C127-LOCAL-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/127/chemistry-search-receipt.json
  locator: Exact full key, label, slug and source selector in raw/owner/curation trees
  accessed_at: '2026-10-21T18:00:40.500789Z'
  support: supports
  summary: Ignored-inclusive bounded search preserves all matching paths; an absent
    curation decision does not imply a missing scientific source.
  snapshot_sha256: 6d22cfe1a3336b8f8770afa8a2839756692b8d2ac7e13c0f8c657e302eb33d3b
  search_scope: rg --no-ignore --hidden; data/natural_products, data/raw and curation;
    exact full key, current label, slug and BGC:compound_index. No claim beyond these
    trees.
- evidence_id: C127-CHEBI-SEARCH-1
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=RSYKJHLWNMXRKZ-RVUXUPINSA-N&size=100
  locator: Literal key search; chebi-key-chaetoglobosin-a.json
  accessed_at: '2026-10-21T17:19:09.661961Z'
  support: supports
  summary: 1 returned name/key results; evaluate exact key and stars, not name similarity.
  snapshot_sha256: e1bd08ce3b6154ce273c69be30c414336ebe303d496e0f3f9b636d3e0254a7b2
  search_scope: Official ChEBI es_search bounded key request, size=100, exact URL
    retained. This is not a universal absence claim.
- evidence_id: C127-CHEBI-SEARCH-2
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=chaetoglobosin+A&size=100
  locator: Literal name search; chebi-name-chaetoglobosin-a.json
  accessed_at: '2026-10-21T17:19:10.867592Z'
  support: supports
  summary: 24 returned name/key results; evaluate exact key and stars, not name similarity.
  snapshot_sha256: 90baaf98c97ad2b227e0ba7e86fdfa4ae4975daef310fdff4ae0a9f961ef3fdb
  search_scope: Official ChEBI es_search bounded name request, size=100, exact URL
    retained. This is not a universal absence claim.
- evidence_id: C127-AUTH-1
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000968.5/annotations.json
  locator: compounds[].structure; BGC0000968.5.json
  accessed_at: '2026-10-21T17:19:08.981765Z'
  support: supports
  summary: 'current MIBiG BGC0000968:1: parsed key RSYKJHLWNMXRKZ-RVUXUPINSA-N; exact
    stored Standard key match=True, fixed-H match=True. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: b529db7c3f60db048a59842ff722b6d30a72f31a4efd6c5d7b9fa372d1a81e2c
- evidence_id: C127-AUTH-2
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/RSYKJHLWNMXRKZ-RVUXUPINSA-N/property/MolecularFormula,InChI,InChIKey,CanonicalSMILES,IsomericSMILES,Charge/JSON
  locator: PropertyTable.Properties[].SMILES; pubchem-key-chaetoglobosin-a.json
  accessed_at: '2026-10-21T17:19:10.139658Z'
  support: supports
  summary: 'PubChem 6440494: parsed key RSYKJHLWNMXRKZ-RVUXUPINSA-N; exact stored
    Standard key match=True, fixed-H match=True. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: 6e7173477a529af92019e16d060f915018b76881d8fa56ac04770bc0d932eb2b
- evidence_id: C127-AUTH-3
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/chaetoglobosin%20A/property/MolecularFormula,InChI,InChIKey,CanonicalSMILES,IsomericSMILES,Charge/JSON
  locator: PropertyTable.Properties[].SMILES; pubchem-name-chaetoglobosin-a.json
  accessed_at: '2026-10-21T17:19:11.361578Z'
  support: context_only
  summary: 'PubChem 6438437: parsed key OUMWCYMRLMEZJH-VOXRAUTJSA-N; exact stored
    Standard key match=False, fixed-H match=False. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: 6c8cc2789c33fdb5cb79bf03868c62046394adb6178e570a3a3a17cef4b7141d
- evidence_id: C127-AUTH-4
  kind: authority
  reference: https://www.npatlas.org/api/v1/compound/NPA013078
  locator: smiles; retry-NPA013078.json
  accessed_at: '2026-10-21T17:21:18.600273Z'
  support: context_only
  summary: 'NPAtlas literal NPA013078: parsed key OUMWCYMRLMEZJH-YOAIXWIWSA-N; exact
    stored Standard key match=False, fixed-H match=False. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: 7c6ad9fa09d3d87d2b2ec7fbb5bc25001d76a773faab216d57c91cdc198c2fa4
- evidence_id: C127-AUTH-5
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/219830/
  locator: default_structure.smiles; CHEBI219830.json
  accessed_at: '2026-10-21T17:20:08.939186Z'
  support: context_only
  summary: 'ChEBI JSON 219830: parsed key None; exact stored Standard key match=False,
    fixed-H match=False. This current database representation is not independent primary
    experimental proof.'
  snapshot_sha256: b8733c964995da0845d6d7a9e3fb96fc72a7e37e04e89cee9e810a71b2f9f683
- evidence_id: C127-AUTH-6
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/219830/
  locator: official molfile endpoint; CHEBI219830-official.mol
  accessed_at: '2026-10-21T17:20:34.798312Z'
  support: supports
  summary: 'ChEBI MOL 219830: parsed key RSYKJHLWNMXRKZ-RVUXUPINSA-N; exact stored
    Standard key match=True, fixed-H match=True. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: 39d06a32387be1f3fe549e04a66c02e272c1ffc3fcfe424c5dce40165b22a993
- evidence_id: C127-AUTH-7
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/68798/
  locator: default_structure.smiles; CHEBI68798.json
  accessed_at: '2026-10-21T17:20:10.135012Z'
  support: context_only
  summary: 'ChEBI JSON 68798: parsed key None; exact stored Standard key match=False,
    fixed-H match=False. This current database representation is not independent primary
    experimental proof.'
  snapshot_sha256: fb3b13a107d156d9b6337a1a6f08e4e7ec7f46d47ccc1054dd42c7975cc5dcef
- evidence_id: C127-AUTH-8
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/68798/
  locator: official molfile endpoint; CHEBI68798-official.mol
  accessed_at: '2026-10-21T17:20:35.392726Z'
  support: context_only
  summary: 'ChEBI MOL 68798: parsed key OUMWCYMRLMEZJH-VOXRAUTJSA-N; exact stored
    Standard key match=False, fixed-H match=False. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: eb0ea40e600c6f7ab63a38109f4f2c8c82e6980b4767a479933f57372bdccfa4
- evidence_id: C127-AUTH-9
  kind: authority
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q76386752.json
  locator: P2017; Q76386752.json
  accessed_at: '2026-10-21T17:19:11.496350Z'
  support: supports
  summary: 'Wikidata Q76386752: parsed key RSYKJHLWNMXRKZ-RVUXUPINSA-N; exact stored
    Standard key match=True, fixed-H match=True. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: c8eae7a1fa53c26600482e848f1c49de0523fed4c73c5d16e91c910bc3f1016e
- evidence_id: C127-AUTH-10
  kind: authority
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q76386752.json
  locator: P233; Q76386752.json
  accessed_at: '2026-10-21T17:19:11.496350Z'
  support: context_only
  summary: 'Wikidata Q76386752: parsed key RSYKJHLWNMXRKZ-UHFFFAOYSA-N; exact stored
    Standard key match=False, fixed-H match=False. This current database representation
    is not independent primary experimental proof. Canonical P233 is not an isomeric
    stereo assertion; compare P2017 when present.'
  snapshot_sha256: c8eae7a1fa53c26600482e848f1c49de0523fed4c73c5d16e91c910bc3f1016e
- evidence_id: C127-PRIMARY-A
  kind: primary_source
  reference: DOI:10.1248/cpb.30.1618
  locator: Complete 11-page structure paper; original p1626 Chart7 and configuration
    discussion
  accessed_at: '2026-10-21T17:21:39.426597Z'
  support: supports
  summary: The original A structure is C32H36N2O5, with an indolylmethyl substituent
    and ring methyl, not the stored C34 graph with additional C10 methyl and ring
    ethyl. The paper assigns 13E,17E,21E and reports the A monohydrate absolute structure
    by anomalous oxygen scattering. That reported experiment is distinguished from
    an independent re-refinement of the cited diffraction data.
  snapshot_sha256: 069f60e2357ed2018b51643f5d0bdc7b238f9b2e49a047d36c052a83643dc233
- evidence_id: C127-PRIMARY-K
  kind: primary_source
  reference: DOI:10.3987/COM-88-S96
  locator: Original 1989 introduction and Figure1 compound1; original pixels and numbered
    C10/17-18 comparison
  accessed_at: '2026-10-21T17:23:38.715689Z'
  support: supports
  summary: Original K has the C34 constitution, but its depicted local C10 is R and
    its 17 alkene is E. The retained graph has C10S and 17Z. Thus renaming the current
    owner K would not establish an exact structure match either. No natural K absolute
    hand is newly selected from this drawing.
  snapshot_sha256: 08fcff157ca802ab18f1f1c8c0efdae6c5596538139bd8ba3247e3dbe884a4e3
- evidence_id: C127-PEER-MAPPING
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch013/chemistry-prep/chaeto-peer-addendum-001.json
  locator: Independent original-pixel reread, numbered complete graph correspondence
    and all alkene maps
  accessed_at: '2026-10-21T17:36:54.836638Z'
  support: supports
  summary: 'Two independent numbered comparisons agree: authentic A is C32; stored
    C34 is K-like constitution with C10S/13E/17Z/21E. Original K depicts C10R/13E/17E/21E.
    Literal NPA013078 has C32 A constitution but leaves C9 undefined and encodes all
    three alkenes Z; eligible CHEBI:68798 official MOL has the complete A graph and
    all E. The later 2020 schematic is not a complete replacement template.'
  snapshot_sha256: 083ceab73003f538d736164f5f2d5eb47d4c7f915af54280b5ce25699a1e658d
- evidence_id: C127-CURRENT-ROUTING
  kind: validation
  reference: /private/tmp/npm-review-work/127/current-chemistry-routing.json
  locator: Current complete source/target rows, collision scan and actual MOL parsing
  accessed_at: '2026-10-21T17:59:48.020962Z'
  support: supports
  summary: Current source key has exactly one MIBiG compound owner, BGC0000968:1;
    the proposed A key has no MIBiG owner and exactly one committed ChEBI row. That
    three-star row has invalid SMILES despite a valid official MOL with its declared
    A key. Its current row SHA is 78990a5ab6d83b4bb6c5672f5e2476c757c87c656c5fd31b7ecfc4968529af2a;
    blindly invoking the replacement loader would copy invalid text.
  snapshot_sha256: 5e17678cd356e73c43337ad42130fbdfd21dfb09ebe07697f070d4a6cfb7b4d3
- evidence_id: C127-STRUCTURE-CONTRACT
  kind: record_content
  reference: src/naturalproductmech/curate/structure_corrections.py
  locator: Inspected current maintained contract
  accessed_at: '2026-10-21T18:00:40.368411Z'
  support: supports
  summary: REPLACE_WITH_CHEBI pins the complete source and complete eligible target
    row, requires unique distinct owners and copies target SMILES. It withholds old
    xrefs and preserves source correction provenance; unrelated inventories join only
    on the new exact key.
  snapshot_sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
- evidence_id: C127-SEED-CONTRACT
  kind: record_content
  reference: scripts/seed_from_sources.py
  locator: Inspected current maintained contract
  accessed_at: '2026-10-21T18:00:40.368411Z'
  support: supports
  summary: Source corrections precede exact-key joins. Current claim-reference, xref-exclusion
    and strain integrations reject structure_correction_note unless separately reviewed/tested
    composition is implemented. Minted source concept follows accession plus compound
    index, not label.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: C127-REFERENCE-CONTRACT
  kind: record_content
  reference: src/naturalproductmech/curate/claim_references.py
  locator: Inspected current maintained contract
  accessed_at: '2026-10-21T18:00:40.368411Z'
  support: supports
  summary: The full-row-pinned claim-reference consumer explicitly rejects a structure-corrected
    row; citation routing cannot be silently stacked with an identity repair.
  snapshot_sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
- evidence_id: C127-CHEBI-CONTRACT
  kind: record_content
  reference: scripts/extract_chebi.py
  locator: Inspected current maintained contract
  accessed_at: '2026-10-21T18:00:40.368411Z'
  support: supports
  summary: The committed identity projection admits only three-star default structures.
    The proposed target representation must be repaired through a maintained, manifested
    extraction or explicit guarded representation contract, not by editing a generated
    owner or blindly copying invalid JSON.
  snapshot_sha256: 46e1898b88fce16096af34eb9e7c9dea40e4d7c8c157d60d485fa85878088e8f
assessments:
- assessment_id: R127-HISTORY
  area: provenance
  topic: Native status and complete retained audit history
  outcome: supported
  summary: All retained history events record SEEDED_FROM_SOURCES provenance. The
    native status remains SEEDED; the review changes neither history nor scientific
    content.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  evidence_ids:
  - R127-OWNER
- assessment_id: R127-OPTIONAL
  area: completeness
  topic: Present optional assertions and enrichment scope
  outcome: not_applicable
  summary: No optional pathway, causal graph, molecular target, activity, application,
    clinical-status, cross-record relation or discussion is asserted. Potential enrichment
    is distinct from checking the present producer, occurrence and locus claims.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  evidence_ids:
  - R127-OWNER
  - R127-LOCAL
- assessment_id: R127-FILING
  area: representation
  topic: Exact-key computed classification provenance
  outcome: supported
  summary: The owner reproduces its exact-key NPClassifier result and version npclassifier.gnps2.org@2026-09-07,
    including Alkaloids filing, superclass/class labels and glycoside prediction false.
    Computed labels are not independent evidence for precursor use or natural origin.
    Any corrected chemical identity must be reclassified against its corrected effective
    key.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  evidence_ids:
  - R127-OWNER
  - R127-LOCAL
- assessment_id: R127-ORGANISM-IDS
  area: grounding
  topic: Literal organism identifier routing
  outcome: supported
  summary: The literal source identifiers and names resolve consistently. Their experimental
    occurrence and stock claims remain separately assessed.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  evidence_ids:
  - R127-Q10678663
- assessment_id: R127-TAXON-SCOPE
  area: provenance
  topic: Taxonomic synonym and experimental-stock boundaries
  outcome: supported
  summary: NCBI 371126 S. macrospora includes Diplodia macrospora as a synonym. This
    is a taxonomic bridge only; it does not turn the primary K/L isolation into support
    for the named A structure, or identify an unspecified P. expansum stock.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  evidence_ids:
  - R127-TAXON-CONTEXT
  - R127-OWNER
- assessment_id: R127-IMODULON-SCOPE
  area: completeness
  topic: Native producer and experimental-host transcriptomic applicability
  outcome: not_applicable
  summary: P. expansum and S. macrospora source stocks are absent. The catalogue gives
    no exact fungal transcriptomic mapping for the native biosynthesis or isolation
    claims.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  evidence_ids:
  - R127-OWNER
  - R127-IMODULON
- assessment_id: S127-A-ORIGIN
  area: evidence
  topic: biosynthesis_origin and producer_organisms[0]
  outcome: concern
  summary: The family has positive native fungal isolation evidence, but this owner
    combines an A label with a K-like constitution and disputed stereochemistry. The
    named-A P. expansum correlation must be adjudicated after exact identity is resolved;
    it is not evidence that the stored stereograph is natively produced. This biology
    dependency is part of the separate chemical identity repair, not a duplicate finding.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  evidence_ids:
  - S127-E-LOCAL
  - S127-E-A1982
  - S127-E-KL1989
  - S127-E-PEER
  - S127-E-SI2007
  dimensions:
  - name: experimental_strain
    value: P. expansum native transformants; collection strain unresolved
    definition: The SI describes native fungal silencing, distinct from K isolation
      in D. macrospora ATCC 36896.
    evidence_ids:
    - S127-E-SI2007
    - S127-E-KL1989
  - name: evidence_tier
    value: Imported expression/product correlation; exact graph applicability unresolved
    definition: Retain source provenance while resolving congener/graph applicability
      and original final-product outcomes.
    evidence_ids:
    - S127-E-LOCAL
    - S127-E-SI2007
    - S127-E-GAP
- assessment_id: S127-A-LOCUS
  area: evidence
  topic: biosynthetic_gene_clusters[0] and imported AM779763.1 association
  outcome: unknown
  summary: The PKS-NRPS CheA and auxiliary-gene SI supports the named cluster architecture
    and native silencing design. It does not independently verify the precise A-versus-C
    outcome, the retained K-like graph or full accession boundary. Empty coordinates
    are not an error. Do not add knockout or final-product enzyme methods from protocol
    descriptions.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  evidence_ids:
  - S127-E-LOCAL
  - S127-E-SI2007
  - S127-E-GAP
- assessment_id: S127-A-OCCURRENCES
  area: evidence
  topic: occurrences[0], occurrences[1], occurrences[2]
  outcome: concern
  summary: All three LOTUS triples are full-key source assertions for the retained
    graph. The 1989 study positively isolates named K/L from Diplodia macrospora;
    the 1980 title is K-specific and the 1988 full body is unavailable. None permits
    automatic transfer to authentic A after a structural repair. Preserve individual
    raw rows, their source context and unresolved exact stereo applicability; no wholesale
    occurrence deletion or taxon substitution is justified here.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  evidence_ids:
  - S127-E-LOCAL
  - S127-E-KL1989
  - S127-E-OCCMETA
  - S127-E-GAP
  - S127-E-PEER
- assessment_id: C127-A-IDENTITY
  area: identity
  topic: Stored representation and source-concept provenance
  outcome: supported
  summary: The complete source row BGC0000968:1 and source-concept hash reproduce
    this stored representation; this does not establish that the upstream compound
    label is correct. Formula, charge, Standard and fixed-H distinctions are independently
    recorded. Primary support and any conflicting exact xref are assessed separately.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  evidence_ids:
  - C127-OWNER
  - C127-GRAPH
  - C127-COMPARISON
  dimensions:
  - name: mibig_source_selector
    value: BGC0000968:1
    definition: Accession plus compound_index, distinct from the entry-level accession.
    evidence_ids:
    - C127-OWNER
  - name: complete_raw_row_sha256
    value: 01a47507c397cb14d2ea4d340739bf8f69f28c6a21930f40f576eafa5755fa70
    definition: Sorted compact ASCII JSON of every parsed TSV field, including empty
      values.
    evidence_ids:
    - C127-OWNER
- assessment_id: C127-A-GROUNDING
  area: provenance
  topic: Exact authority eligibility and source representation
  outcome: supported
  summary: No exact eligible row exists in the committed ChEBI projection for this
    owner. Current bounded name/key searches do not justify a different congener or
    a two-star grounding.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  evidence_ids:
  - C127-OWNER
  - C127-COMPARISON
  - C127-LOCAL-SEARCH
  - C127-CHEBI-SEARCH-1
  - C127-CHEBI-SEARCH-2
- assessment_id: C127-A-NAMED-IDENTITY
  area: identity
  topic: A, K-like constitution and exact K drawing differences
  outcome: concern
  summary: The wrong named identity is confirmed independently of authority agreement
    by formula and complete connectivity. Local C10 and alkene checks further prevent
    treating the raw graph as verified K. The original A hand report is positive,
    but no absolute K or P assignment is transferred from it.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  evidence_ids:
  - C127-PRIMARY-A
  - C127-PRIMARY-K
  - C127-PEER-MAPPING
  - C127-GRAPH
findings:
- finding_id: C127-F-WRONG-IDENTITY
  issue_key: mibig-bgc0000968-1-chaetoglobosin-a-k-like-identity
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Named chaetoglobosin A contains a different C34 constitution
  description: The owner is labelled A but stores a C34 K-like constitution instead
    of original C32 A. Its C10S/17Z assignments also differ from original K depiction,
    so a label-only K rename is insufficient. The literal NPA link is a third precision/alkene
    representation and cannot serve as a replacement template. The eligible A target
    is available as a valid official MOL, but its committed/default SMILES is invalid
    and currently unsafe to copy.
  normalization_reason: The confirmed constitutional mismatch makes the record denote
    the wrong named product, meeting the native blocker identity rubric. The separate
    K/P drawing and absolute-hand limits are not promoted into new absolute assignments.
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  field_paths:
  - label
  - chemical_structure
  - xrefs
  - grounding_status
  - grounding_notes
  - source_concepts
  evidence_ids:
  - C127-OWNER
  - C127-PRIMARY-A
  - C127-PRIMARY-K
  - C127-PEER-MAPPING
  - C127-CURRENT-ROUTING
  - C127-STRUCTURE-CONTRACT
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Pin the exact source and valid eligible A target only after representation
      prerequisites
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Retain full guards, collision rejection and old-key separation
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_chebi.py
    role: Implement or obtain a manifested, verified official-MOL representation repair
      without lowering eligibility
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Regenerated target representation with new full-row SHA; no ad hoc raw patch
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Regenerate exact-key identity/joins and explicitly adjudicated biological
      composition
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Preserve original source assertion and complete row
actions:
- action_id: C127-ACTION-IDENTITY
  finding_ids:
  - C127-F-WRONG-IDENTITY
  target_ids:
  - naturalproductmech:mibig-0c963509fd
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Pin the exact source and valid eligible A target only after representation
      prerequisites
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Retain full guards, collision rejection and old-key separation
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_chebi.py
    role: Implement or obtain a manifested, verified official-MOL representation repair
      without lowering eligibility
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Regenerated target representation with new full-row SHA; no ad hoc raw patch
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Regenerate exact-key identity/joins and explicitly adjudicated biological
      composition
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Preserve original source assertion and complete row
  description: Adjudicate source_id=BGC0000968:1, version5, complete source-row SHA256=01a47507c397cb14d2ea4d340739bf8f69f28c6a21930f40f576eafa5755fa70,
    exact old key=RSYKJHLWNMXRKZ-RVUXUPINSA-N, old SMILES=CC[C@H]1[C@H]2[C@@H](NC(=O)[C@@]23[C@@H](/C=C/C[C@@H](/C=C(\[C@H](C(=O)/C=C/C3=O)O)/C)C)[C@H]4[C@@]1(O4)C)[C@@H](C)C5=CNC6=CC=CC=C65,
    old database_ids=npatlas:NPA013078, and all taxon/locus/method fields as one source
    assertion. Preserve those raw bytes. For named A, independently approve the complete
    primary-numbered C32 graph, all nine tetrahedral centres and 13E/17E/21E against
    the original A report and valid official CHEBI:68798 MOL (SHA eb0ea40e600c6f7ab63a38109f4f2c8c82e6980b4767a479933f57372bdccfa4);
    do not use the C10-only diagnostic MOL, current NPA013078, or the later schematic
    as a full repair. First fix the eligible target representation through a maintained,
    manifested extraction enhancement or a separately implemented full-row-pinned
    official-MOL correction contract. Pin the present target SHA78990a5ab6d83b4bb6c5672f5e2476c757c87c656c5fd31b7ecfc4968529af2a
    and official MOL; require parsed Standard key OUMWCYMRLMEZJH-VOXRAUTJSA-N, exact
    fixed-H, formula/charge and complete stereochemical agreement before committing
    a NEW target row/hash. Only then consider existing REPLACE_WITH_CHEBI with that
    new target hash, freshly derived Standard InChI and tetrahedral flag, stable primary
    citation and actual attribution. Current raw collision scan finds one old-key
    owner and no new-key MIBiG owner; repeat ignored-inclusive owner/path and source/target
    uniqueness checks at application time and fail closed on a collision. Preserve
    the minted BGC0000968:1 source concept, while reviewing emitted CHEBI identity,
    label, path and references. Withhold the old literal xref and never transfer old-key
    LOTUS/classifier/assay data merely because the owner path persists. The three
    complete old-key LOTUS pins are 10.1002/HLCA.19880710806=0594b4f59a646e2b050062bfd18476f95bb41c72129e35802b49fd2f6de641e6;
    10.1021/JF60227A011=4911b2e6dfb2ab1f415a4be4f7e7d66f3ea12a1419339323ca19e3f18b464328;
    10.3987/COM-88-S96=987d49e8f5b3aea40ee1367d6660808c5b57879a4606bb18db774d0e3bfed3df;
    each requires independent exact-congener adjudication, not blanket reassignment
    to A or K. Named-A Penicillium correlation, methods and source citation must separately
    support the repaired graph before being carried over. Preserve BGC0000968:2 chaetoglobosin
    C and all unrelated owners. Any science citation/strain/method action must use
    an explicitly reviewed and tested composition path because existing consumers
    reject structure_correction_note. A label-only K rename or unguarded arbitrary-SMILES
    override is not an implemented or sufficient repair.
  generator: Maintained ChEBI representation prerequisite, then guarded exact-source
    structure correction and seed reproduction.
  acceptance_checks:
  - Reject complete source/target drift, invalid SMILES, formula/key/fixed-H or stereochemical
    disagreement, duplicate selectors and source/target collisions.
  - Verify every primary-numbered atom and all three alkene geometries of the approved
    complete A target; do not treat a local-C10 diagnostic as a complete molecule.
  - Demonstrate old raw rows remain unchanged and old-key xrefs, LOTUS triples, classifier
    and assays are not copied to the new identity; retain an explicit audit discussion.
  - Adjudicate every surviving producer/locus/citation claim for exact A and test
    overlay composition; keep the distinct C owner unchanged.
  - After separately authorized implementation, run maintained extraction/seed canary,
    reproduction, strict/corpus and full QC; this review does not execute repairs.
limitations:
- This is a claim-level review of present assertions and bounded source gaps, not
  an exhaustive search for every later paper or an obligation to add every optional
  mechanism.
- No identity finding is duplicated here; the chemistry action must preserve and separately
  adjudicate old-key producer/locus and each LOTUS assertion before graph migration.
- The native method is RNA silencing, not automatically a clean knockout. No collection
  strain or exact AM779763.1 sequence comparison was independently established in
  this science packet.
- Original access times are reused. The peer evidence date is a local re-read time,
  not an external retrieval.
- Authority matches establish the representations actually returned at their retained
  access times; they are not independent experimental structure or absolute-hand determinations.
  Root and science sections separately assess organism, locus, classification and
  history claims.
- The original A paper reports the absolute X-ray determination; underlying diffraction
  data were not independently re-refined. The K drawing comparison supports exact
  depicted configurations, not a new absolute-hand determination.
- No complete replacement K/P graph is selected. Old-key biological assertions and
  authority labels cannot settle congener identity by consensus.
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
- batch-013
```
