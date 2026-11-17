# Chaetoglobosin P: local stereochemical conflict and isolate-context review

- Review: 20261021T180400Z-chaetoglobosin-p
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T17:52:16.963980Z
- Finished UTC: 2026-10-21T18:04:00.609309Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The stored C10S graph conflicts with the local C10R depiction in the cited 2020 primary, while the original 1997 natural assignment remains unavailable. This confirmed representation conflict does not establish a complete replacement graph. A minor context finding distinguishes the purified-product isolate TTI-0863 from the deposited-locus isolate TTI-0885, preserving conservative source grades and exact-key biological boundaries.

## Scope And Provenance

One complete generated owner and any referenced components, assessed claim by claim for exact identity, provenance, origin, producer and occurrence scope, biosynthesis, classification, optional content and audit history.

Selection: Campaign record 129, batch 013, selected in path order from the fresh-main authoritative validated catalogue and the separately validated targets in earlier batch commits (publication tracked separately). At selection, 174 of 3116 current records had campaign coverage and 2942 remained. The population search included ignored files. Exactly one target is assessed here.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1c2402097718c138b081e00943de8f04de0541cd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-3456826281 | data/natural_products/alkaloids/chaetoglobosin-p.yaml | generated | Chaetoglobosin P |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | naturalproductmech:mibig-3456826281 | The documented target strict validator completed; scientific support is assessed separately. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-3456826281 | All 3,116 current record files agree with PATHS.tsv and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-3456826281 | All 3,116 current records passed the documented byte-reproduction gate against committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-3456826281 | The exhaustive review queue produced 8,928 diagnostic rows across 12 queues; this deterministic output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-3456826281 | The configured identifier-label gate passed using the existing ontology caches: 13,449 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,744 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate on the current main baseline | passed | True | naturalproductmech:mibig-3456826281 | The full documented just qc recipe passed on the unchanged main baseline during batch004. Test summary: 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). All configured lint, governance, documentation, provenance, source-queue, schema, rendering, reproduction, filing-integrity and reporting stages completed successfully. |
| Complete owner and referenced-component scope | passed | True | naturalproductmech:mibig-3456826281 | The complete owner and all six captured source-row sets were read after successful official intake and agree with the pinned preparation. The external component set is empty. Fresh strict validation is retained separately. |
| Native product and deposited-locus source boundaries | passed | True | naturalproductmech:mibig-3456826281 | Original primary and sequence metadata distinguish both isolates and retain appropriately weak method grades. |
| Original P isolation and absolute-source closure | unavailable | True | naturalproductmech:mibig-3456826281 | The 1997 original body is unavailable and the later depicted stereograph needs separate adjudication. |
| Stored chemical representation and complete source row | passed | True | naturalproductmech:mibig-3456826281 | Fresh intake derivation agrees with the stored graph; the source selector, full row and prepared snapshot were independently rechecked. |
| Literal NPAtlas representation | passed | True | naturalproductmech:mibig-3456826281 | NPA032791 matches the stored full graph; that agreement does not resolve the primary drawing conflict. |
| Stored C10 versus inspected primary depiction | failed | True | naturalproductmech:mibig-3456826281 | Stored C10S disagrees with the original 2020 Figure1 local R depiction and independently checked mapping. |
| Original natural P structure assignment | unavailable | True | naturalproductmech:mibig-3456826281 | The original1997 full structure study is unavailable; no complete P repair or definitive natural hand is selected. |

## Scientific And Domain Assessments

### Native status and complete retained audit history

provenance: supported. Targets: naturalproductmech:mibig-3456826281.

All retained history events record SEEDED_FROM_SOURCES provenance. The native status remains SEEDED; the review changes neither history nor scientific content.

### Present optional assertions and enrichment scope

completeness: not_applicable. Targets: naturalproductmech:mibig-3456826281.

No optional pathway, causal graph, molecular target, activity, application, clinical-status, cross-record relation or discussion is asserted. Potential enrichment is distinct from checking the present producer, occurrence and locus claims.

### Exact-key computed classification provenance

representation: supported. Targets: naturalproductmech:mibig-3456826281.

The owner reproduces its exact-key NPClassifier result and version npclassifier.gnps2.org@2026-09-07, including Alkaloids filing, superclass/class labels and glycoside prediction false. Computed labels are not independent evidence for precursor use or natural origin. Any corrected chemical identity must be reclassified against its corrected effective key.

### Literal organism identifier routing

grounding: supported. Targets: naturalproductmech:mibig-3456826281.

The literal source identifiers and names resolve consistently. Their experimental occurrence and stock claims remain separately assessed.

### Taxonomic synonym and experimental-stock boundaries

provenance: supported. Targets: naturalproductmech:mibig-3456826281.

Discosia 162396 is a genus and D. rubi 2502037 is a species. Neither identifier collapses TTI0863/NRRL66951 and TTI0885/NRRL66952 into one experimental stock. The deposited cluster and isolated sample require their own source bridges.

### Native producer and experimental-host transcriptomic applicability

completeness: not_applicable. Targets: naturalproductmech:mibig-3456826281.

D. rubi TTI0863 and TTI0885 are absent. A C. neoformans susceptibility experiment is a target-organism experiment and does not establish producer transcriptomic applicability.

### biosynthesis_origin and producer_organisms[0]

evidence: supported. Targets: naturalproductmech:mibig-3456826281.

The 2020 native fungal purification supports named-P origin and species production. Exact hand/graph interpretation is separately unresolved, so no product-specific biological claim should be migrated automatically after chemistry correction.

### biosynthetic_gene_clusters[0] and current evidence methods

evidence: supported. Targets: naturalproductmech:mibig-3456826281.

The imported empty methods and CLUSTER_UNSTATED/SOURCE_ASSERTION tiers are conservative and consistent with the putative genome-mining association. MT459796.1 bounds reproduce the deposited region. Do not add producer knockout from Cryptococcus susceptibility or purified final-P enzyme proof from G76/G77 predictions. The broad OTHER class could optionally be enriched to the explicitly depicted hybrid PKS-NRPS through reviewed source curation, without claiming new causal evidence.

### occurrences[0]

evidence: supported. Targets: naturalproductmech:mibig-3456826281.

The genus-level historical Discosia assertion is consistent with the 2020 known-compound comparison, but its original 1997 detailed isolation/absolute source remains unverified. Preserve the source assertion and do not substitute a 2020 strain into the historical occurrence.

### Stored representation and source-concept provenance

identity: supported. Targets: naturalproductmech:mibig-3456826281.

The complete source row BGC0002539:1 and source-concept hash reproduce this stored representation; this does not establish that the upstream compound label is correct. Formula, charge, Standard and fixed-H distinctions are independently recorded. Primary support and any conflicting exact xref are assessed separately.

### Exact authority eligibility and source representation

provenance: supported. Targets: naturalproductmech:mibig-3456826281.

No exact eligible row exists in the committed ChEBI projection for this owner. Current bounded name/key searches do not justify a different congener or a two-star grounding.

### Confirmed local representation conflict and unresolved natural assignment

evidence: concern. Targets: naturalproductmech:mibig-3456826281.

The local C10 disagreement is confirmed at the source-depiction level. It does not establish that the later schematic provides a correct complete P graph, especially given the independent alkene inconsistencies in its A/K examples.

## Findings

### S129-F-STRAIN: The purified-product and deposited-locus isolates need separate context

minor / open / confirmed; issue key: mibig-bgc0002539-cultured-and-deposited-isolate-context.

The species-level assertion is supported, but it omits that purified P is from TTI-0863 whereas the deposited locus is TTI-0885 (literal TTI-00885). The weak grades are source-faithful; this is a provenance qualification, not unsupported production or a grade error.

### C129-F-C10-CONFLICT: Stored P C10 configuration conflicts with the inspected primary drawing

major / open / confirmed; issue key: chaetoglobosin-p-primary-c10-representation-conflict.

The owner and literal NPAtlas graph encode C10S, whereas original 2020 Figure1 depicts local C10R. The exact original1997 natural assignment remains uninspected, and the later schematic is not a complete reliable stereo template. Preserve the conflict instead of silently choosing either authority or flipping the whole graph.

## Recommended Actions And Acceptance Checks

### S129-ACT-STRAIN

After and in tested composition with the independent exact-identity adjudication, qualify BGC0002539:1, complete raw-row SHA256 1ba514b8ab881c14ba612e09cc5d6695e1795534f9cb2ca0b9910d95dc1dca15, expected context {"entry_version": "3", "genome_accession": "MT459796.1", "locus_evidence_methods": "", "locus_from": "1", "locus_to": "37406", "primary_reference": "DOI:10.3389/fmicb.2020.01766", "reference_basis": "COMPOUND_EVIDENCE", "standard_inchi_key": "YLBJYVFDYOTYHW-PCKGUDBLSA-N", "taxon_id": "NCBITaxon:2502037"}. Use the consumed producer-strain row for cultured TTI-0863 (NRRL 66951), and a separately attributed deposited-isolate qualifier preserving literal TTI-00885 while explaining paper TTI-0885 (NRRL 66952). Do not rename MT459796.1 as the purified-product isolate. If BGC-local wording is required, implement an explicit typed context consumer rather than misusing a producer-only table. Preserve conservative grades and the historical genus occurrence.

- Require exactly one unchanged complete source row and reject source/version/key/taxon/accession/bounds/method drift.
- Preserve distinct cultured and deposited isolates and the literal spelling discrepancy. No targeted producer knockout or final-product enzyme claim may be added.
- Reject untested concurrent structure correction; explicitly decide which product/isolate assertions survive any changed key rather than carrying old-key claims automatically.
- Regeneration must preserve current accession/bounds and weak grades while emitting separate attributed context; no raw or generated YAML hand edits.

### C129-ACTION-ADJUDICATE

Resolve original DOI10.1080/10575639708043695 and any structure revision before choosing natural P hand. Pin source_id=BGC0002539:1, version3, complete source-row SHA256=1ba514b8ab881c14ba612e09cc5d6695e1795534f9cb2ca0b9910d95dc1dca15, old key=YLBJYVFDYOTYHW-PCKGUDBLSA-N, exact old SMILES=C/C1=C/[C@@H](C)C/C=C/[C@H]2[C@@H]3O[C@]3(C)[C@@H](C)[C@H]3[C@H]([C@@H](C)C4=C[NH]C5=CC=CC=C45)NC(=O)[C@@]23C(=O)/C=C/C(=O)[C@@H]1O, literal NPA032791 and all producer/locus/reference fields. Preserve the local C10R depiction, current C10S source and independent alkene caveat in a source-pinned maintained conflict discussion; if no existing consumer supports that qualification, implement and test an explicit guarded discussion contract rather than editing generated YAML or an unsupported override column. A future structure repair needs an independently approved complete atom/stereo map, including all alkene geometries, plus formula/charge/Standard/fixed-H checks. Current CHEBI:172345 is two-star with invalid default JSON SMILES, so existing REPLACE_WITH_CHEBI cannot be used for it; a non-ChEBI route would require a separately implemented, full-row-pinned source-graph contract and collision tests. The local diagnostic MOL is not a candidate full molecule. Reconcile any exact-key xref, LOTUS, classifier and assay joins without carrying old-key data to an unverified new key. Compose any separately justified cultured-strain/deposit-isolate qualification through an explicitly tested path, since current integration rejects structure_correction_note. Do not conflate this question with the distinct A/K identities.

- Retain both actual source representations and the original-body gap without claiming new natural absolute proof.
- Reject partial/local graph replacements, two-star ChEBI targets, invalid SMILES, source drift and collisions.
- If a full target is justified, verify every numbered centre and all alkene geometries, plus Standard/fixed-H identity and all dependent exact-key joins.
- Test any required discussion/strain/structure composition and preserve raw rows and unrelated owners.
- After authorized curation, run documented reproduction and QC; no repair is executed by this review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R129-OWNER | data/natural_products/alkaloids/chaetoglobosin-p.yaml; Complete owner, all present assertions and complete audit history | supports | Root read the complete Chaetoglobosin P owner after official intake. It contains 1 occurrence, 1 producer and 1 locus assertions. Referenced external components are empty. Present optional fields: none. |
| R129-LOCAL | /private/tmp/npm-review-work/129/local-sources.json; Complete resolved owner and all six captured exact matching source-row sets | context_only | Root read every captured MIBiG, LOTUS, ChEBI structures/origins, CyanoMetDB and NPClassifier row, including empty sets. The owner and captured rows match the prepared source snapshot. Separate PubChem raw observations are assessed by the scientific section. Source fidelity alone does not establish experimental support. |
| R129-Q10474164 | https://www.wikidata.org/wiki/Q10474164; Literal P225/P685 fields in retained complete multi-entity response | context_only | Literal Q10474164 scientific names and NCBI identifiers match the imported rows. This verifies identifier routing; it does not validate the occurrence citation, production or stock identity. |
| R129-TAXON-CONTEXT | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;retmode=xml&amp;id=162396,1905,1981977,2062,2502037,27334,292,339670,36816,371126,38033,40623,5149,54571,66425,68195,953739,97398; ScientificName, Rank, ParentTaxId and OtherNames for the exact relevant taxon records | context_only | Discosia 162396 is a genus and D. rubi 2502037 is a species. Neither identifier collapses TTI0863/NRRL66951 and TTI0885/NRRL66952 into one experimental stock. The deposited cluster and isolated sample require their own source bridges. |
| R129-IMODULON | https://imodulondb.org/api/datasets; Complete official 20-organism/28-dataset catalogue | context_only | The retained current catalogue was read and its bytes match the previously inspected catalogue. It establishes membership only, not production or module applicability. |
| S129-E-LOCAL | data/natural_products/alkaloids/chaetoglobosin-p.yaml; Complete actual owner, resolved components and all exact matching local source rows | supports | Exact source selector BGC0002539:1 version 3; complete parsed source row SHA256 1ba514b8ab881c14ba612e09cc5d6695e1795534f9cb2ca0b9910d95dc1dca15. Current methods ''; source grades SOURCE_ASSERTION/CLUSTER_UNSTATED. Present science claims were compared with the formal intake; source preparation is not treated as another formal target. |
| S129-E-PRIMARY | DOI:10.3389/fmicb.2020.01766; Complete scientific body, strain/chemical/genomic methods, Tables 1–2 and Figures 1/4 | supports | Exact named P was purified (12.1 mg) from TTI-0863 / NRRL 66951 grown in MMK2; NMR/LC-MS matched known-compound data. The distinct TTI-0885 / NRRL 66952 supplies the tabulated putative BGC. Genome mining and homology support association, not an exact final-product enzyme or producer-locus knockout. The Cryptococcus twf1 experiment is drug susceptibility. |
| S129-E-SI | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7399079/supplementaryFiles; All supplementary DOCX text/captions/tables; S4–S8 sample context, without exhaustive spectral reassignment | supports | Supplementary characterization concerns the purified TTI-0863 product; comparative morphology and sequences support both isolates as D. rubi. Shared species does not identify the same physical culture or establish locus function. |
| S129-E-LOCUS | https://www.ncbi.nlm.nih.gov/nuccore/MT459796.1; Header/source and feature qualifiers; literal accession and isolate | supports | MT459796.1 is 37,406 bp, taxon 2502037, with deposited isolate TTI-00885 and the 2020 primary reference. The extra-zero literal deposit spelling is retained; the paper uses TTI-0885. This supports accession provenance, not exact final-product function or independent equality of two isolates. |
| S129-E-PEER | /private/tmp/npm-review-work/shared-next-batch013/bgc-science/chaeto-peer-check/peer-check.json; Local C10 and all three macrocycle-alkene comparisons, bounded to original pixels | supports | The 2020 drawing differs at C10 from the retained P graph; its common A/K/P alkene layout also conflicts with older A/K depictions. This does not establish a complete corrected P stereograph or natural absolute hand. Chemistry owns the exact identity finding. |
| S129-E-GAP | /private/tmp/npm-review-work/shared-next-batch013/bgc-science/source-notes.json; Original 1997 DOI access boundary | unknown | The original Discosia isolation DOI 10.1080/10575639708043695 full body remains unavailable. The 2020 paper positively compares its P with those known-compound data; no original absolute experiment or complete 1997 strain details are reconstructed. |
| S129-E-CONSUMERS | src/naturalproductmech/curate/producer_strains.py; Complete producer strain and deposit-isolate loaders; actual seeder application | supports | Existing producer-strain and isolate tables enforce exact complete raw-row SHA and qualify producer context only. They cannot separately annotate a BGC or silently rewrite genome identity, and the seeder rejects unreviewed composition after structure correction. |
| S129-E-SEARCH | /private/tmp/npm-review-work/129/curation-search.json; Exact accession/source selectors in curation | context_only | No existing exact BGC0002539/MT459796 decision was returned by the bounded current curation search. |
| C129-OWNER | data/natural_products/alkaloids/chaetoglobosin-p.yaml; Complete owner and all local-source rows; no referenced components | supports | The complete owner denotes Chaetoglobosin P under naturalproductmech:mibig-3456826281. Its exact source selector is BGC0002539:1, version 3, with complete parsed raw-row SHA256 1ba514b8ab881c14ba612e09cc5d6695e1795534f9cb2ca0b9910d95dc1dca15. The official intake and prepared owner bytes agree. |
| C129-GRAPH | /private/tmp/npm-review-work/129/chemistry.json; Fresh intake RDKit result and frozen Standard/fixed-H comparison | supports | The stored SMILES recomputes to YLBJYVFDYOTYHW-PCKGUDBLSA-N, formula C33H38N2O5, formal charge 0; stored InChI/key agree. These are representation checks, not experimental identity proof. |
| C129-COMPARISON | /private/tmp/npm-review-work/shared-next-batch013/chemistry-prep/chemical-comparison.json; Record 129; exact source rows and each graph comparison | supports | Exact Standard, fixed-H, formula, charge and stereo comparisons of the retained owner, complete raw rows and current authority responses; primary experimental proof is assessed separately. |
| C129-LOCAL-SEARCH | /private/tmp/npm-review-work/129/chemistry-search-receipt.json; Exact full key, label, slug and source selector in raw/owner/curation trees | supports | Ignored-inclusive bounded search preserves all matching paths; an absent curation decision does not imply a missing scientific source. |
| C129-CHEBI-SEARCH-1 | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=YLBJYVFDYOTYHW-PCKGUDBLSA-N&amp;size=100; Literal key search; chebi-key-chaetoglobosin-p.json | supports | No compound matches the provided term: 'YLBJYVFDYOTYHW-PCKGUDBLSA-N' |
| C129-CHEBI-SEARCH-2 | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=Chaetoglobosin+P&amp;size=100; Literal name search; chebi-name-chaetoglobosin-p.json | supports | 1 returned name/key results; evaluate exact key and stars, not name similarity. |
| C129-AUTH-1 | https://mibig.secondarymetabolites.org/repository/BGC0002539.3/annotations.json; compounds[].structure; BGC0002539.3.json | supports | current MIBiG BGC0002539:1: parsed key YLBJYVFDYOTYHW-PCKGUDBLSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C129-AUTH-2 | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/YLBJYVFDYOTYHW-PCKGUDBLSA-N/property/MolecularFormula,InChI,InChIKey,CanonicalSMILES,IsomericSMILES,Charge/JSON; PropertyTable.Properties[].SMILES; pubchem-key-chaetoglobosin-p.json | supports | PubChem 170988176: parsed key YLBJYVFDYOTYHW-PCKGUDBLSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C129-AUTH-3 | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/Chaetoglobosin%20P/property/MolecularFormula,InChI,InChIKey,CanonicalSMILES,IsomericSMILES,Charge/JSON; PropertyTable.Properties[].SMILES; pubchem-name-chaetoglobosin-p.json | supports | PubChem 170988176: parsed key YLBJYVFDYOTYHW-PCKGUDBLSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C129-AUTH-4 | https://www.npatlas.org/api/v1/compound/NPA032791; smiles; NPA032791.json | supports | NPAtlas literal NPA032791: parsed key YLBJYVFDYOTYHW-PCKGUDBLSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C129-AUTH-5 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/172345/; default_structure.smiles; CHEBI172345.json | context_only | ChEBI JSON 172345: parsed key None; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C129-AUTH-6 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/172345/; official molfile endpoint; CHEBI172345-official.mol | context_only | ChEBI MOL 172345: parsed key YLBJYVFDYOTYHW-QLDXQYSGSA-N; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C129-AUTH-7 | https://www.wikidata.org/wiki/Special:EntityData/Q115948637.json; P2017; Q115948637.json | supports | Wikidata Q115948637: parsed key YLBJYVFDYOTYHW-PCKGUDBLSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C129-AUTH-8 | https://www.wikidata.org/wiki/Special:EntityData/Q115948637.json; P233; Q115948637.json | context_only | Wikidata Q115948637: parsed key YLBJYVFDYOTYHW-UHFFFAOYSA-N; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. Canonical P233 is not an isomeric stereo assertion; compare P2017 when present. |
| C129-PRIMARY-P | DOI:10.3389/fmicb.2020.01766; Original Figure1 P/K/A; exact local C10 red methyl wedge and backbone branches | supports | At P C10, the ring branch is above, indolyl carbon lower-left and methyl dashed lower-right. Priorities C3(N,C,H) &gt; indolyl(C,C,C) &gt; methyl &gt; H give depicted R, whereas the stored graph encodes S. This is an independently checked local drawing discrepancy, not a complete natural-P absolute assignment. |
| C129-LOCAL-MAP | /private/tmp/npm-review-work/shared-next-batch013/chemistry-prep/local-C10-comparison.json; Stereo-erased local C10 reconstruction and independently checked pixel orientation | supports | The diagnostic reconstructs only the explicitly inspected C10 arrangement. It agrees with the independent manual check and current two-star CHEBI:172345 MOL at that centre. It is not a complete P replacement structure. |
| C129-PEER | /private/tmp/npm-review-work/shared-next-batch013/chemistry-prep/chaeto-peer-addendum-001.json; Complete heavy-atom/bond crosswalk and all alkene maps | supports | Owner, literal NPA032791 and PubChem170988176 agree at C10S with 13E/17Z/21E. The ChEBI MOL differs locally at C10R. Later Figure1 schematics use 17Z even for A/K, conflicting with their original E evidence; therefore this later schematic is not a safe complete stereochemical replacement template. |
| C129-ORIGINAL-ACCESS | /private/tmp/npm-review-work/shared-next-batch013/bgc-science/source-notes.json; Original 1997 P isolation/structure body | unknown | The original DOI10.1080/10575639708043695 full body was unavailable in the retained bounded route. The exact original natural P stereochemical assignment and any revision remain required unresolved evidence. |
| C129-STRUCTURE-CONTRACT | src/naturalproductmech/curate/structure_corrections.py; Inspected maintained consumer | supports | Current replacement requires a unique structured three-star ChEBI target and copies its representation; it cannot apply an arbitrary local stereo flip or a two-star target. |
| C129-SEED-CONTRACT | scripts/seed_from_sources.py; Inspected maintained consumer | supports | Structure-corrected rows join other inventories only at the corrected exact key; current claim-reference, strain and xref consumers require reviewed composition. |
| C129-STRAIN-CONTRACT | src/naturalproductmech/curate/producer_strains.py; Inspected maintained consumer | supports | Strain and isolate context is complete-source-row pinned and distinct from chemical identity; no strain qualification establishes the disputed stereocentre. |

## Limits And Additional Notes

- This is a claim-level review of present assertions and bounded source gaps, not an exhaustive search for every later paper or an obligation to add every optional mechanism.
- Original 1997 isolation/absolute-assignment body remains unavailable.
- The 2020 known-compound depiction is not a complete absolute-configuration experiment; chemistry adjudication precedes any claim migration.
- A putative cluster class or early precursor-function prediction does not establish final-P enzymology.
- Authority matches establish the representations actually returned at their retained access times; they are not independent experimental structure or absolute-hand determinations. Root and science sections separately assess organism, locus, classification and history claims.
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
review_id: 20261021T180400Z-chaetoglobosin-p
title: 'Chaetoglobosin P: local stereochemical conflict and isolate-context review'
started_at: '2026-10-21T17:52:16.963980Z'
finished_at: '2026-10-21T18:04:00.609309Z'
completion: partial
verdict: needs_curation
scientific_review: true
summary: The stored C10S graph conflicts with the local C10R depiction in the cited
  2020 primary, while the original 1997 natural assignment remains unavailable. This
  confirmed representation conflict does not establish a complete replacement graph.
  A minor context finding distinguishes the purified-product isolate TTI-0863 from
  the deposited-locus isolate TTI-0885, preserving conservative source grades and
  exact-key biological boundaries.
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
    role: context
  - path: data/natural_products/alkaloids/chaetoglobosin-c.yaml
    sha256: 9a1bf49fde80bca26c948c350609bafed6853871a75339aa1301b38aad5fe68a
    role: context
  - path: data/natural_products/alkaloids/chaetoglobosin-p.yaml
    sha256: 0308e9b1b2258370d93d04398111270812a720e2e151bf9fc29a214a7e3cbad1
    role: target
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
  selection: Campaign record 129, batch 013, selected in path order from the fresh-main
    authoritative validated catalogue and the separately validated targets in earlier
    batch commits (publication tracked separately). At selection, 174 of 3116 current
    records had campaign coverage and 2942 remained. The population search included
    ignored files. Exactly one target is assessed here.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-3456826281
targets:
- target_id: naturalproductmech:mibig-3456826281
  path: data/natural_products/alkaloids/chaetoglobosin-p.yaml
  label: Chaetoglobosin P
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
  - naturalproductmech:mibig-3456826281
  command: just validate-strict data/natural_products/alkaloids/chaetoglobosin-p.yaml
    --out /private/tmp/npm-review-work/129/strict.tsv
  exit_code: 0
  scope_note: Actual command finished 2026-10-21T17:52:19.798368Z
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
  - naturalproductmech:mibig-3456826281
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
  - naturalproductmech:mibig-3456826281
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
  - naturalproductmech:mibig-3456826281
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
  - naturalproductmech:mibig-3456826281
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
  - naturalproductmech:mibig-3456826281
- check_id: R129-FULL-OWNER
  name: Complete owner and referenced-component scope
  status: passed
  required: true
  summary: The complete owner and all six captured source-row sets were read after
    successful official intake and agree with the pinned preparation. The external
    component set is empty. Fresh strict validation is retained separately.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - R129-OWNER
  - R129-LOCAL
- check_id: S129-C-SCOPE
  name: Native product and deposited-locus source boundaries
  status: passed
  required: true
  summary: Original primary and sequence metadata distinguish both isolates and retain
    appropriately weak method grades.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - S129-E-PRIMARY
  - S129-E-SI
  - S129-E-LOCUS
- check_id: S129-C-PRIMARY
  name: Original P isolation and absolute-source closure
  status: unavailable
  required: true
  summary: The 1997 original body is unavailable and the later depicted stereograph
    needs separate adjudication.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - S129-E-GAP
  - S129-E-PEER
- check_id: C129-C-REPRESENTATION
  name: Stored chemical representation and complete source row
  status: passed
  required: true
  summary: Fresh intake derivation agrees with the stored graph; the source selector,
    full row and prepared snapshot were independently rechecked.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - C129-OWNER
  - C129-GRAPH
  - C129-COMPARISON
- check_id: C129-C-LITERAL-XREF
  name: Literal NPAtlas representation
  status: passed
  required: true
  summary: NPA032791 matches the stored full graph; that agreement does not resolve
    the primary drawing conflict.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - C129-COMPARISON
  - C129-AUTH-1
  - C129-AUTH-2
  - C129-AUTH-3
  - C129-AUTH-4
  - C129-AUTH-5
  - C129-AUTH-6
  - C129-AUTH-7
  - C129-AUTH-8
- check_id: C129-C-PRIMARY-C10
  name: Stored C10 versus inspected primary depiction
  status: failed
  required: true
  summary: Stored C10S disagrees with the original 2020 Figure1 local R depiction
    and independently checked mapping.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - C129-PRIMARY-P
  - C129-LOCAL-MAP
  - C129-PEER
  - C129-GRAPH
- check_id: C129-C-ORIGINAL-STEREO
  name: Original natural P structure assignment
  status: unavailable
  required: true
  summary: The original1997 full structure study is unavailable; no complete P repair
    or definitive natural hand is selected.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - C129-ORIGINAL-ACCESS
  - C129-PEER
evidence:
- evidence_id: R129-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/chaetoglobosin-p.yaml
  locator: Complete owner, all present assertions and complete audit history
  accessed_at: '2026-10-21T17:52:39.707072Z'
  support: supports
  summary: 'Root read the complete Chaetoglobosin P owner after official intake. It
    contains 1 occurrence, 1 producer and 1 locus assertions. Referenced external
    components are empty. Present optional fields: none.'
  snapshot_sha256: 0308e9b1b2258370d93d04398111270812a720e2e151bf9fc29a214a7e3cbad1
- evidence_id: R129-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/129/local-sources.json
  locator: Complete resolved owner and all six captured exact matching source-row
    sets
  accessed_at: '2026-10-21T17:52:39.707072Z'
  support: context_only
  summary: Root read every captured MIBiG, LOTUS, ChEBI structures/origins, CyanoMetDB
    and NPClassifier row, including empty sets. The owner and captured rows match
    the prepared source snapshot. Separate PubChem raw observations are assessed by
    the scientific section. Source fidelity alone does not establish experimental
    support.
  snapshot_sha256: 5a40e7f3e4dbbb296c25120fed235cf267f4920aeefaab58732f8ff7a1332809
- evidence_id: R129-Q10474164
  kind: database
  reference: https://www.wikidata.org/wiki/Q10474164
  locator: Literal P225/P685 fields in retained complete multi-entity response
  accessed_at: '2026-10-21T17:25:35.481159Z'
  support: context_only
  summary: Literal Q10474164 scientific names and NCBI identifiers match the imported
    rows. This verifies identifier routing; it does not validate the occurrence citation,
    production or stock identity.
  snapshot_sha256: 026cf7dce61f76ea1be554bf995a269a5531a82c3a0c74c5873851c736a1752b
- evidence_id: R129-TAXON-CONTEXT
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&retmode=xml&id=162396,1905,1981977,2062,2502037,27334,292,339670,36816,371126,38033,40623,5149,54571,66425,68195,953739,97398
  locator: ScientificName, Rank, ParentTaxId and OtherNames for the exact relevant
    taxon records
  accessed_at: '2026-10-21T17:25:35.685538Z'
  support: context_only
  summary: Discosia 162396 is a genus and D. rubi 2502037 is a species. Neither identifier
    collapses TTI0863/NRRL66951 and TTI0885/NRRL66952 into one experimental stock.
    The deposited cluster and isolated sample require their own source bridges.
  snapshot_sha256: 83ff126040853b0ab6de8dbf4dab0b64eaf4b2aea314a68d6caddfcba16f66dd
- evidence_id: R129-IMODULON
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete official 20-organism/28-dataset catalogue
  accessed_at: '2026-10-21T17:25:35.092545Z'
  support: context_only
  summary: The retained current catalogue was read and its bytes match the previously
    inspected catalogue. It establishes membership only, not production or module
    applicability.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: S129-E-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/chaetoglobosin-p.yaml
  locator: Complete actual owner, resolved components and all exact matching local
    source rows
  accessed_at: '2026-10-21T17:58:44.849326Z'
  support: supports
  summary: Exact source selector BGC0002539:1 version 3; complete parsed source row
    SHA256 1ba514b8ab881c14ba612e09cc5d6695e1795534f9cb2ca0b9910d95dc1dca15. Current
    methods ''; source grades SOURCE_ASSERTION/CLUSTER_UNSTATED. Present science claims
    were compared with the formal intake; source preparation is not treated as another
    formal target.
  snapshot_sha256: 0308e9b1b2258370d93d04398111270812a720e2e151bf9fc29a214a7e3cbad1
- evidence_id: S129-E-PRIMARY
  kind: primary_source
  reference: DOI:10.3389/fmicb.2020.01766
  locator: Complete scientific body, strain/chemical/genomic methods, Tables 1–2 and
    Figures 1/4
  accessed_at: '2026-10-21T17:15:33.703420Z'
  support: supports
  summary: Exact named P was purified (12.1 mg) from TTI-0863 / NRRL 66951 grown in
    MMK2; NMR/LC-MS matched known-compound data. The distinct TTI-0885 / NRRL 66952
    supplies the tabulated putative BGC. Genome mining and homology support association,
    not an exact final-product enzyme or producer-locus knockout. The Cryptococcus
    twf1 experiment is drug susceptibility.
  snapshot_sha256: be1fef7745d9609b88999d003ab5567108269e9018533ea26097c5983202646c
- evidence_id: S129-E-SI
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7399079/supplementaryFiles
  locator: All supplementary DOCX text/captions/tables; S4–S8 sample context, without
    exhaustive spectral reassignment
  accessed_at: '2026-10-21T17:19:56.583105Z'
  support: supports
  summary: Supplementary characterization concerns the purified TTI-0863 product;
    comparative morphology and sequences support both isolates as D. rubi. Shared
    species does not identify the same physical culture or establish locus function.
  snapshot_sha256: 6559828a59d5b6fe63c6d3c98c2d87a5a7053b31b5bbc59bd8a1b0be34e3de9e
- evidence_id: S129-E-LOCUS
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/nuccore/MT459796.1
  locator: Header/source and feature qualifiers; literal accession and isolate
  accessed_at: '2026-10-21T17:20:31.971678Z'
  support: supports
  summary: MT459796.1 is 37,406 bp, taxon 2502037, with deposited isolate TTI-00885
    and the 2020 primary reference. The extra-zero literal deposit spelling is retained;
    the paper uses TTI-0885. This supports accession provenance, not exact final-product
    function or independent equality of two isolates.
  snapshot_sha256: e51ccbd3cb936db78a69e43abca6c130c0774bf26831fca8ab46a785170fa526
- evidence_id: S129-E-PEER
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch013/bgc-science/chaeto-peer-check/peer-check.json
  locator: Local C10 and all three macrocycle-alkene comparisons, bounded to original
    pixels
  accessed_at: '2026-10-21T17:36:21.431111Z'
  support: supports
  summary: The 2020 drawing differs at C10 from the retained P graph; its common A/K/P
    alkene layout also conflicts with older A/K depictions. This does not establish
    a complete corrected P stereograph or natural absolute hand. Chemistry owns the
    exact identity finding.
  snapshot_sha256: 54278a05f0e6888a75afaf8ea0e4ec0808a0ffa898ca86dd74af59324a7cf972
- evidence_id: S129-E-GAP
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch013/bgc-science/source-notes.json
  locator: Original 1997 DOI access boundary
  accessed_at: '2026-10-21T17:30:25.183480Z'
  support: unknown
  summary: The original Discosia isolation DOI 10.1080/10575639708043695 full body
    remains unavailable. The 2020 paper positively compares its P with those known-compound
    data; no original absolute experiment or complete 1997 strain details are reconstructed.
  snapshot_sha256: 86ba58da529384d774d2e5b81fb4825893bf1fa9beda7e82b7957337b9b18350
  search_scope: Bounded original 1997 publisher/DOI route retained alongside complete
    2020 main and SI; ignored-inclusive local source search. No broad or repeated
    blocked retrieval and no claim that the unavailable body lacks evidence.
- evidence_id: S129-E-CONSUMERS
  kind: record_content
  reference: src/naturalproductmech/curate/producer_strains.py
  locator: Complete producer strain and deposit-isolate loaders; actual seeder application
  accessed_at: '2026-10-21T17:58:44.849326Z'
  support: supports
  summary: Existing producer-strain and isolate tables enforce exact complete raw-row
    SHA and qualify producer context only. They cannot separately annotate a BGC or
    silently rewrite genome identity, and the seeder rejects unreviewed composition
    after structure correction.
  snapshot_sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
- evidence_id: S129-E-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/129/curation-search.json
  locator: Exact accession/source selectors in curation
  accessed_at: '2026-10-21T17:58:06.619306Z'
  support: context_only
  summary: No existing exact BGC0002539/MT459796 decision was returned by the bounded
    current curation search.
  snapshot_sha256: 4d9d8aa857e5dfdde6ebf2de1935aa9def3536e5af661a2efc9089f083008936
  search_scope: rg --no-ignore --hidden -n BGC0002539|MT459796 under current curation;
    exit 1 with empty stdout/stderr. Ignored files included; this is not an assertion
    about all implementation routes or literature.
- evidence_id: C129-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/chaetoglobosin-p.yaml
  locator: Complete owner and all local-source rows; no referenced components
  accessed_at: '2026-10-21T18:02:03.015819Z'
  support: supports
  summary: The complete owner denotes Chaetoglobosin P under naturalproductmech:mibig-3456826281.
    Its exact source selector is BGC0002539:1, version 3, with complete parsed raw-row
    SHA256 1ba514b8ab881c14ba612e09cc5d6695e1795534f9cb2ca0b9910d95dc1dca15. The official
    intake and prepared owner bytes agree.
  snapshot_sha256: 0308e9b1b2258370d93d04398111270812a720e2e151bf9fc29a214a7e3cbad1
- evidence_id: C129-GRAPH
  kind: validation
  reference: /private/tmp/npm-review-work/129/chemistry.json
  locator: Fresh intake RDKit result and frozen Standard/fixed-H comparison
  accessed_at: '2026-10-21T17:52:18.485192Z'
  support: supports
  summary: The stored SMILES recomputes to YLBJYVFDYOTYHW-PCKGUDBLSA-N, formula C33H38N2O5,
    formal charge 0; stored InChI/key agree. These are representation checks, not
    experimental identity proof.
  snapshot_sha256: 286319718e97338547838b26df76dfa9d9227c7a908fb4e6fb09667c8f3799db
- evidence_id: C129-COMPARISON
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch013/chemistry-prep/chemical-comparison.json
  locator: Record 129; exact source rows and each graph comparison
  accessed_at: '2026-10-21T17:23:24.463910Z'
  support: supports
  summary: Exact Standard, fixed-H, formula, charge and stereo comparisons of the
    retained owner, complete raw rows and current authority responses; primary experimental
    proof is assessed separately.
  snapshot_sha256: 503b2ba573d5eef465b41aa483433a9b2b92cce169c7270520b63466b4f5539f
- evidence_id: C129-LOCAL-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/129/chemistry-search-receipt.json
  locator: Exact full key, label, slug and source selector in raw/owner/curation trees
  accessed_at: '2026-10-21T18:02:03.060711Z'
  support: supports
  summary: Ignored-inclusive bounded search preserves all matching paths; an absent
    curation decision does not imply a missing scientific source.
  snapshot_sha256: f1d916a9e21c2e91ea2c5f326d54b940a2fa63f08157c18d458d2b0f0b9d540f
  search_scope: rg --no-ignore --hidden; data/natural_products, data/raw and curation;
    exact full key, current label, slug and BGC:compound_index. No claim beyond these
    trees.
- evidence_id: C129-CHEBI-SEARCH-1
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=YLBJYVFDYOTYHW-PCKGUDBLSA-N&size=100
  locator: Literal key search; chebi-key-chaetoglobosin-p.json
  accessed_at: '2026-10-21T17:19:51.559241Z'
  support: supports
  summary: 'No compound matches the provided term: ''YLBJYVFDYOTYHW-PCKGUDBLSA-N'''
  snapshot_sha256: c744144db36f2d8d46b31a2e38a7f0c4ffdc0b8d73e2c5d970092a624ec5e60d
  search_scope: Official ChEBI es_search bounded key request, size=100, exact URL
    retained. This is not a universal absence claim.
- evidence_id: C129-CHEBI-SEARCH-2
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=Chaetoglobosin+P&size=100
  locator: Literal name search; chebi-name-chaetoglobosin-p.json
  accessed_at: '2026-10-21T17:19:50.798698Z'
  support: supports
  summary: 1 returned name/key results; evaluate exact key and stars, not name similarity.
  snapshot_sha256: 1873f0b102755069d1f5b489f3ad5508ced8a6b9f8b60286d2677af31b89feec
  search_scope: Official ChEBI es_search bounded name request, size=100, exact URL
    retained. This is not a universal absence claim.
- evidence_id: C129-AUTH-1
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002539.3/annotations.json
  locator: compounds[].structure; BGC0002539.3.json
  accessed_at: '2026-10-21T17:19:49.799562Z'
  support: supports
  summary: 'current MIBiG BGC0002539:1: parsed key YLBJYVFDYOTYHW-PCKGUDBLSA-N; exact
    stored Standard key match=True, fixed-H match=True. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: e35ad8672d034adf8033e37ac76a36f69163d933152f0b38d6dede75a43e36b5
- evidence_id: C129-AUTH-2
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/YLBJYVFDYOTYHW-PCKGUDBLSA-N/property/MolecularFormula,InChI,InChIKey,CanonicalSMILES,IsomericSMILES,Charge/JSON
  locator: PropertyTable.Properties[].SMILES; pubchem-key-chaetoglobosin-p.json
  accessed_at: '2026-10-21T17:19:50.146828Z'
  support: supports
  summary: 'PubChem 170988176: parsed key YLBJYVFDYOTYHW-PCKGUDBLSA-N; exact stored
    Standard key match=True, fixed-H match=True. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: 2b82331ba1a2f44acf4315fccf62ab0c14141943039c8f123ceae194d876bc42
- evidence_id: C129-AUTH-3
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/Chaetoglobosin%20P/property/MolecularFormula,InChI,InChIKey,CanonicalSMILES,IsomericSMILES,Charge/JSON
  locator: PropertyTable.Properties[].SMILES; pubchem-name-chaetoglobosin-p.json
  accessed_at: '2026-10-21T17:19:51.172557Z'
  support: supports
  summary: 'PubChem 170988176: parsed key YLBJYVFDYOTYHW-PCKGUDBLSA-N; exact stored
    Standard key match=True, fixed-H match=True. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: 2b82331ba1a2f44acf4315fccf62ab0c14141943039c8f123ceae194d876bc42
- evidence_id: C129-AUTH-4
  kind: authority
  reference: https://www.npatlas.org/api/v1/compound/NPA032791
  locator: smiles; NPA032791.json
  accessed_at: '2026-10-21T17:20:25.811567Z'
  support: supports
  summary: 'NPAtlas literal NPA032791: parsed key YLBJYVFDYOTYHW-PCKGUDBLSA-N; exact
    stored Standard key match=True, fixed-H match=True. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: 3d78e17bf992a8d9ea3bee8ecdcd0a5e4d3a9fd3ed2e17a7abc0faa2f02b8f73
- evidence_id: C129-AUTH-5
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/172345/
  locator: default_structure.smiles; CHEBI172345.json
  accessed_at: '2026-10-21T17:20:07.708226Z'
  support: context_only
  summary: 'ChEBI JSON 172345: parsed key None; exact stored Standard key match=False,
    fixed-H match=False. This current database representation is not independent primary
    experimental proof.'
  snapshot_sha256: 0213f4cfe1e40f5cc54da27fcef76e1319ba1e3191ea1710fea61583c9288eb5
- evidence_id: C129-AUTH-6
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/172345/
  locator: official molfile endpoint; CHEBI172345-official.mol
  accessed_at: '2026-10-21T17:20:34.124157Z'
  support: context_only
  summary: 'ChEBI MOL 172345: parsed key YLBJYVFDYOTYHW-QLDXQYSGSA-N; exact stored
    Standard key match=False, fixed-H match=False. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: c56452cb68a3f2faabe78a13fc4457fc35f776e2f65650c813e4a491f2c99717
- evidence_id: C129-AUTH-7
  kind: authority
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q115948637.json
  locator: P2017; Q115948637.json
  accessed_at: '2026-10-21T17:19:51.194489Z'
  support: supports
  summary: 'Wikidata Q115948637: parsed key YLBJYVFDYOTYHW-PCKGUDBLSA-N; exact stored
    Standard key match=True, fixed-H match=True. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: 0e4b989a4ca612dd953972091bbe4a4de2e28d4b04cd48d53d3296c85c3f1f65
- evidence_id: C129-AUTH-8
  kind: authority
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q115948637.json
  locator: P233; Q115948637.json
  accessed_at: '2026-10-21T17:19:51.194489Z'
  support: context_only
  summary: 'Wikidata Q115948637: parsed key YLBJYVFDYOTYHW-UHFFFAOYSA-N; exact stored
    Standard key match=False, fixed-H match=False. This current database representation
    is not independent primary experimental proof. Canonical P233 is not an isomeric
    stereo assertion; compare P2017 when present.'
  snapshot_sha256: 0e4b989a4ca612dd953972091bbe4a4de2e28d4b04cd48d53d3296c85c3f1f65
- evidence_id: C129-PRIMARY-P
  kind: primary_source
  reference: DOI:10.3389/fmicb.2020.01766
  locator: Original Figure1 P/K/A; exact local C10 red methyl wedge and backbone branches
  accessed_at: '2026-10-21T17:19:56.583105Z'
  support: supports
  summary: At P C10, the ring branch is above, indolyl carbon lower-left and methyl
    dashed lower-right. Priorities C3(N,C,H) > indolyl(C,C,C) > methyl > H give depicted
    R, whereas the stored graph encodes S. This is an independently checked local
    drawing discrepancy, not a complete natural-P absolute assignment.
  snapshot_sha256: 4b57bc42cef7c1a9a52167e0f71ae1c72db7d409d3194ec469dde0ba33998efb
- evidence_id: C129-LOCAL-MAP
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch013/chemistry-prep/local-C10-comparison.json
  locator: Stereo-erased local C10 reconstruction and independently checked pixel
    orientation
  accessed_at: '2026-10-21T17:31:18.196804Z'
  support: supports
  summary: The diagnostic reconstructs only the explicitly inspected C10 arrangement.
    It agrees with the independent manual check and current two-star CHEBI:172345
    MOL at that centre. It is not a complete P replacement structure.
  snapshot_sha256: ea912e0864d0ea184ca9717de4a9cbb086da0ff4ed2e00cfdadf66c040730f9d
- evidence_id: C129-PEER
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch013/chemistry-prep/chaeto-peer-addendum-001.json
  locator: Complete heavy-atom/bond crosswalk and all alkene maps
  accessed_at: '2026-10-21T17:36:54.836638Z'
  support: supports
  summary: Owner, literal NPA032791 and PubChem170988176 agree at C10S with 13E/17Z/21E.
    The ChEBI MOL differs locally at C10R. Later Figure1 schematics use 17Z even for
    A/K, conflicting with their original E evidence; therefore this later schematic
    is not a safe complete stereochemical replacement template.
  snapshot_sha256: 083ceab73003f538d736164f5f2d5eb47d4c7f915af54280b5ce25699a1e658d
- evidence_id: C129-ORIGINAL-ACCESS
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch013/bgc-science/source-notes.json
  locator: Original 1997 P isolation/structure body
  accessed_at: '2026-10-21T17:30:25.183480Z'
  support: unknown
  summary: The original DOI10.1080/10575639708043695 full body was unavailable in
    the retained bounded route. The exact original natural P stereochemical assignment
    and any revision remain required unresolved evidence.
  snapshot_sha256: 86ba58da529384d774d2e5b81fb4825893bf1fa9beda7e82b7957337b9b18350
  search_scope: Retained exact original1997 DOI publisher route and source-preparation
    access ledger; no global absence claim and no repeat of failed access.
- evidence_id: C129-STRUCTURE-CONTRACT
  kind: record_content
  reference: src/naturalproductmech/curate/structure_corrections.py
  locator: Inspected maintained consumer
  accessed_at: '2026-10-21T18:02:03.015819Z'
  support: supports
  summary: Current replacement requires a unique structured three-star ChEBI target
    and copies its representation; it cannot apply an arbitrary local stereo flip
    or a two-star target.
  snapshot_sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
- evidence_id: C129-SEED-CONTRACT
  kind: record_content
  reference: scripts/seed_from_sources.py
  locator: Inspected maintained consumer
  accessed_at: '2026-10-21T18:02:03.015819Z'
  support: supports
  summary: Structure-corrected rows join other inventories only at the corrected exact
    key; current claim-reference, strain and xref consumers require reviewed composition.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: C129-STRAIN-CONTRACT
  kind: record_content
  reference: src/naturalproductmech/curate/producer_strains.py
  locator: Inspected maintained consumer
  accessed_at: '2026-10-21T18:02:03.015819Z'
  support: supports
  summary: Strain and isolate context is complete-source-row pinned and distinct from
    chemical identity; no strain qualification establishes the disputed stereocentre.
  snapshot_sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
assessments:
- assessment_id: R129-HISTORY
  area: provenance
  topic: Native status and complete retained audit history
  outcome: supported
  summary: All retained history events record SEEDED_FROM_SOURCES provenance. The
    native status remains SEEDED; the review changes neither history nor scientific
    content.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - R129-OWNER
- assessment_id: R129-OPTIONAL
  area: completeness
  topic: Present optional assertions and enrichment scope
  outcome: not_applicable
  summary: No optional pathway, causal graph, molecular target, activity, application,
    clinical-status, cross-record relation or discussion is asserted. Potential enrichment
    is distinct from checking the present producer, occurrence and locus claims.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - R129-OWNER
  - R129-LOCAL
- assessment_id: R129-FILING
  area: representation
  topic: Exact-key computed classification provenance
  outcome: supported
  summary: The owner reproduces its exact-key NPClassifier result and version npclassifier.gnps2.org@2026-09-07,
    including Alkaloids filing, superclass/class labels and glycoside prediction false.
    Computed labels are not independent evidence for precursor use or natural origin.
    Any corrected chemical identity must be reclassified against its corrected effective
    key.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - R129-OWNER
  - R129-LOCAL
- assessment_id: R129-ORGANISM-IDS
  area: grounding
  topic: Literal organism identifier routing
  outcome: supported
  summary: The literal source identifiers and names resolve consistently. Their experimental
    occurrence and stock claims remain separately assessed.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - R129-Q10474164
- assessment_id: R129-TAXON-SCOPE
  area: provenance
  topic: Taxonomic synonym and experimental-stock boundaries
  outcome: supported
  summary: Discosia 162396 is a genus and D. rubi 2502037 is a species. Neither identifier
    collapses TTI0863/NRRL66951 and TTI0885/NRRL66952 into one experimental stock.
    The deposited cluster and isolated sample require their own source bridges.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - R129-TAXON-CONTEXT
  - R129-OWNER
- assessment_id: R129-IMODULON-SCOPE
  area: completeness
  topic: Native producer and experimental-host transcriptomic applicability
  outcome: not_applicable
  summary: D. rubi TTI0863 and TTI0885 are absent. A C. neoformans susceptibility
    experiment is a target-organism experiment and does not establish producer transcriptomic
    applicability.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - R129-OWNER
  - R129-IMODULON
- assessment_id: S129-A-NATIVE
  area: evidence
  topic: biosynthesis_origin and producer_organisms[0]
  outcome: supported
  summary: The 2020 native fungal purification supports named-P origin and species
    production. Exact hand/graph interpretation is separately unresolved, so no product-specific
    biological claim should be migrated automatically after chemistry correction.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - S129-E-LOCAL
  - S129-E-PRIMARY
  - S129-E-SI
  - S129-E-PEER
  dimensions:
  - name: isolated_product_strain
    value: TTI-0863 / NRRL 66951
    definition: The culture from which purified P and its NMR data were obtained.
    evidence_ids:
    - S129-E-PRIMARY
    - S129-E-SI
  - name: deposited_locus_isolate
    value: TTI-0885 / NRRL 66952; deposited TTI-00885
    definition: A distinct isolate used for the referenced locus; shared species is
      not same-stock proof.
    evidence_ids:
    - S129-E-PRIMARY
    - S129-E-LOCUS
- assessment_id: S129-A-BGC
  area: evidence
  topic: biosynthetic_gene_clusters[0] and current evidence methods
  outcome: supported
  summary: The imported empty methods and CLUSTER_UNSTATED/SOURCE_ASSERTION tiers
    are conservative and consistent with the putative genome-mining association. MT459796.1
    bounds reproduce the deposited region. Do not add producer knockout from Cryptococcus
    susceptibility or purified final-P enzyme proof from G76/G77 predictions. The
    broad OTHER class could optionally be enriched to the explicitly depicted hybrid
    PKS-NRPS through reviewed source curation, without claiming new causal evidence.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - S129-E-LOCAL
  - S129-E-PRIMARY
  - S129-E-LOCUS
  dimensions:
  - name: evidence_tier
    value: Putative genomic association
    definition: No targeted native producer-locus intervention or exact-P reconstitution
      is established by the inspected study.
    evidence_ids:
    - S129-E-PRIMARY
    - S129-E-LOCAL
- assessment_id: S129-A-OCCURRENCE
  area: evidence
  topic: occurrences[0]
  outcome: supported
  summary: The genus-level historical Discosia assertion is consistent with the 2020
    known-compound comparison, but its original 1997 detailed isolation/absolute source
    remains unverified. Preserve the source assertion and do not substitute a 2020
    strain into the historical occurrence.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - S129-E-LOCAL
  - S129-E-PRIMARY
  - S129-E-GAP
- assessment_id: C129-A-IDENTITY
  area: identity
  topic: Stored representation and source-concept provenance
  outcome: supported
  summary: The complete source row BGC0002539:1 and source-concept hash reproduce
    this stored representation; this does not establish that the upstream compound
    label is correct. Formula, charge, Standard and fixed-H distinctions are independently
    recorded. Primary support and any conflicting exact xref are assessed separately.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - C129-OWNER
  - C129-GRAPH
  - C129-COMPARISON
  dimensions:
  - name: mibig_source_selector
    value: BGC0002539:1
    definition: Accession plus compound_index, distinct from the entry-level accession.
    evidence_ids:
    - C129-OWNER
  - name: complete_raw_row_sha256
    value: 1ba514b8ab881c14ba612e09cc5d6695e1795534f9cb2ca0b9910d95dc1dca15
    definition: Sorted compact ASCII JSON of every parsed TSV field, including empty
      values.
    evidence_ids:
    - C129-OWNER
- assessment_id: C129-A-GROUNDING
  area: provenance
  topic: Exact authority eligibility and source representation
  outcome: supported
  summary: No exact eligible row exists in the committed ChEBI projection for this
    owner. Current bounded name/key searches do not justify a different congener or
    a two-star grounding.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - C129-OWNER
  - C129-COMPARISON
  - C129-LOCAL-SEARCH
  - C129-CHEBI-SEARCH-1
  - C129-CHEBI-SEARCH-2
- assessment_id: C129-A-CONFLICT
  area: evidence
  topic: Confirmed local representation conflict and unresolved natural assignment
  outcome: concern
  summary: The local C10 disagreement is confirmed at the source-depiction level.
    It does not establish that the later schematic provides a correct complete P graph,
    especially given the independent alkene inconsistencies in its A/K examples.
  target_ids:
  - naturalproductmech:mibig-3456826281
  evidence_ids:
  - C129-PRIMARY-P
  - C129-LOCAL-MAP
  - C129-PEER
  - C129-ORIGINAL-ACCESS
findings:
- finding_id: S129-F-STRAIN
  issue_key: mibig-bgc0002539-cultured-and-deposited-isolate-context
  category: evidence
  severity: minor
  certainty: confirmed
  status: open
  title: The purified-product and deposited-locus isolates need separate context
  description: The species-level assertion is supported, but it omits that purified
    P is from TTI-0863 whereas the deposited locus is TTI-0885 (literal TTI-00885).
    The weak grades are source-faithful; this is a provenance qualification, not unsupported
    production or a grade error.
  target_ids:
  - naturalproductmech:mibig-3456826281
  field_paths:
  - producer_organisms[0].strain
  - producer_organisms[0].notes
  - producer_organisms[0].evidence
  - biosynthetic_gene_clusters[0].organism_label
  evidence_ids:
  - S129-E-LOCAL
  - S129-E-PRIMARY
  - S129-E-LOCUS
  - S129-E-CONSUMERS
  - S129-E-SEARCH
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Consumed raw-row-pinned cultured-strain qualifier
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_isolates.tsv
    role: Consumed literal deposited-isolate qualifier
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Exact guarded context consumer
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Producer/BGC emission and composition handling
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Unchanged source context
- finding_id: C129-F-C10-CONFLICT
  issue_key: chaetoglobosin-p-primary-c10-representation-conflict
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Stored P C10 configuration conflicts with the inspected primary drawing
  description: The owner and literal NPAtlas graph encode C10S, whereas original 2020
    Figure1 depicts local C10R. The exact original1997 natural assignment remains
    uninspected, and the later schematic is not a complete reliable stereo template.
    Preserve the conflict instead of silently choosing either authority or flipping
    the whole graph.
  normalization_reason: Major reflects a confirmed source-to-representation conflict
    requiring adjudication. It is not normalized as a proven wrong natural-product
    identity because the original absolute protocol and a complete corrected P graph
    remain unresolved.
  target_ids:
  - naturalproductmech:mibig-3456826281
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  evidence_ids:
  - C129-OWNER
  - C129-PRIMARY-P
  - C129-LOCAL-MAP
  - C129-PEER
  - C129-ORIGINAL-ACCESS
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Use only after a complete independently approved eligible graph is available
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Preserve complete pins and implement any separately justified non-ChEBI
      route explicitly
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Project any approved repair and reviewed context without old-key transfers
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Preserve the original complete source assertion
actions:
- action_id: S129-ACT-STRAIN
  finding_ids:
  - S129-F-STRAIN
  target_ids:
  - naturalproductmech:mibig-3456826281
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Consumed raw-row-pinned cultured-strain qualifier
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_isolates.tsv
    role: Consumed literal deposited-isolate qualifier
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Exact guarded context consumer
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Producer/BGC emission and composition handling
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Unchanged source context
  generator: scripts/seed_from_sources.py
  description: 'After and in tested composition with the independent exact-identity
    adjudication, qualify BGC0002539:1, complete raw-row SHA256 1ba514b8ab881c14ba612e09cc5d6695e1795534f9cb2ca0b9910d95dc1dca15,
    expected context {"entry_version": "3", "genome_accession": "MT459796.1", "locus_evidence_methods":
    "", "locus_from": "1", "locus_to": "37406", "primary_reference": "DOI:10.3389/fmicb.2020.01766",
    "reference_basis": "COMPOUND_EVIDENCE", "standard_inchi_key": "YLBJYVFDYOTYHW-PCKGUDBLSA-N",
    "taxon_id": "NCBITaxon:2502037"}. Use the consumed producer-strain row for cultured
    TTI-0863 (NRRL 66951), and a separately attributed deposited-isolate qualifier
    preserving literal TTI-00885 while explaining paper TTI-0885 (NRRL 66952). Do
    not rename MT459796.1 as the purified-product isolate. If BGC-local wording is
    required, implement an explicit typed context consumer rather than misusing a
    producer-only table. Preserve conservative grades and the historical genus occurrence.'
  acceptance_checks:
  - Require exactly one unchanged complete source row and reject source/version/key/taxon/accession/bounds/method
    drift.
  - Preserve distinct cultured and deposited isolates and the literal spelling discrepancy.
    No targeted producer knockout or final-product enzyme claim may be added.
  - Reject untested concurrent structure correction; explicitly decide which product/isolate
    assertions survive any changed key rather than carrying old-key claims automatically.
  - Regeneration must preserve current accession/bounds and weak grades while emitting
    separate attributed context; no raw or generated YAML hand edits.
- action_id: C129-ACTION-ADJUDICATE
  finding_ids:
  - C129-F-C10-CONFLICT
  target_ids:
  - naturalproductmech:mibig-3456826281
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Use only after a complete independently approved eligible graph is available
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Preserve complete pins and implement any separately justified non-ChEBI
      route explicitly
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Project any approved repair and reviewed context without old-key transfers
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Preserve the original complete source assertion
  description: Resolve original DOI10.1080/10575639708043695 and any structure revision
    before choosing natural P hand. Pin source_id=BGC0002539:1, version3, complete
    source-row SHA256=1ba514b8ab881c14ba612e09cc5d6695e1795534f9cb2ca0b9910d95dc1dca15,
    old key=YLBJYVFDYOTYHW-PCKGUDBLSA-N, exact old SMILES=C/C1=C/[C@@H](C)C/C=C/[C@H]2[C@@H]3O[C@]3(C)[C@@H](C)[C@H]3[C@H]([C@@H](C)C4=C[NH]C5=CC=CC=C45)NC(=O)[C@@]23C(=O)/C=C/C(=O)[C@@H]1O,
    literal NPA032791 and all producer/locus/reference fields. Preserve the local
    C10R depiction, current C10S source and independent alkene caveat in a source-pinned
    maintained conflict discussion; if no existing consumer supports that qualification,
    implement and test an explicit guarded discussion contract rather than editing
    generated YAML or an unsupported override column. A future structure repair needs
    an independently approved complete atom/stereo map, including all alkene geometries,
    plus formula/charge/Standard/fixed-H checks. Current CHEBI:172345 is two-star
    with invalid default JSON SMILES, so existing REPLACE_WITH_CHEBI cannot be used
    for it; a non-ChEBI route would require a separately implemented, full-row-pinned
    source-graph contract and collision tests. The local diagnostic MOL is not a candidate
    full molecule. Reconcile any exact-key xref, LOTUS, classifier and assay joins
    without carrying old-key data to an unverified new key. Compose any separately
    justified cultured-strain/deposit-isolate qualification through an explicitly
    tested path, since current integration rejects structure_correction_note. Do not
    conflate this question with the distinct A/K identities.
  generator: Primary adjudication followed by an explicitly guarded maintained qualification
    or full-graph correction; no automatic flip.
  acceptance_checks:
  - Retain both actual source representations and the original-body gap without claiming
    new natural absolute proof.
  - Reject partial/local graph replacements, two-star ChEBI targets, invalid SMILES,
    source drift and collisions.
  - If a full target is justified, verify every numbered centre and all alkene geometries,
    plus Standard/fixed-H identity and all dependent exact-key joins.
  - Test any required discussion/strain/structure composition and preserve raw rows
    and unrelated owners.
  - After authorized curation, run documented reproduction and QC; no repair is executed
    by this review.
limitations:
- This is a claim-level review of present assertions and bounded source gaps, not
  an exhaustive search for every later paper or an obligation to add every optional
  mechanism.
- Original 1997 isolation/absolute-assignment body remains unavailable.
- The 2020 known-compound depiction is not a complete absolute-configuration experiment;
  chemistry adjudication precedes any claim migration.
- A putative cluster class or early precursor-function prediction does not establish
  final-P enzymology.
- Authority matches establish the representations actually returned at their retained
  access times; they are not independent experimental structure or absolute-hand determinations.
  Root and science sections separately assess organism, locus, classification and
  history claims.
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
