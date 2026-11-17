# Chloramphenicol: sample identity, cellular assay classes and CmlI review

- Review: 20261021T180457Z-chloramphenicol
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T17:52:21.104850Z
- Finished UTC: 2026-10-21T18:04:57.755983Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The parent graph deliberately leaves both stereocentres undefined, while literal PubChem 5959 and all deposited samples behind the 25 written observations specify RR. One major finding requests exact tested-sample qualification; a second addresses six cellular PhoP assays incorrectly classified as enzyme inhibition. Numeric calls and projection reproduce the source rows. The explicitly qualified CmlI pathway and graph are supported; original 2001 and 1949 bodies remain unavailable.

## Scope And Provenance

One complete generated owner and any referenced components, assessed claim by claim for exact identity, provenance, origin, producer and occurrence scope, biosynthesis, classification, optional content and audit history.

Selection: Campaign record 130, batch 013, selected in path order from the fresh-main authoritative validated catalogue and the separately validated targets in earlier batch commits (publication tracked separately). At selection, 174 of 3116 current records had campaign coverage and 2942 remained. The population search included ignored files. Exactly one target is assessed here.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1c2402097718c138b081e00943de8f04de0541cd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-d9dc3ff908 | data/natural_products/alkaloids/chloramphenicol.yaml | generated | chloramphenicol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | naturalproductmech:mibig-d9dc3ff908 | The documented target strict validator completed; scientific support is assessed separately. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-d9dc3ff908 | All 3,116 current record files agree with PATHS.tsv and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-d9dc3ff908 | All 3,116 current records passed the documented byte-reproduction gate against committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-d9dc3ff908 | The exhaustive review queue produced 8,928 diagnostic rows across 12 queues; this deterministic output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-d9dc3ff908 | The configured identifier-label gate passed using the existing ontology caches: 13,449 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,744 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate on the current main baseline | passed | True | naturalproductmech:mibig-d9dc3ff908 | The full documented just qc recipe passed on the unchanged main baseline during batch004. Test summary: 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). All configured lint, governance, documentation, provenance, source-queue, schema, rendering, reproduction, filing-integrity and reporting stages completed successfully. |
| Complete owner and referenced-component scope | passed | True | naturalproductmech:mibig-d9dc3ff908 | The complete owner and all six captured source-row sets were read after successful official intake and agree with the pinned preparation. The external component set is empty. Fresh strict validation is retained separately. |
| CmlI step/graph primary and native-reference support | passed | True | naturalproductmech:mibig-d9dc3ff908 | Primary biochemistry, appropriate kinetic scope and independent native CDS equality support the existing qualified step and graph. |
| All written assay calls and numeric projection | passed | True | naturalproductmech:mibig-d9dc3ff908 | All 25 current owner observations match the selected raw rows and current bounded source joins; 191 raw and 166 omitted are reproduced. |
| Exact cellular assay activity-class support | failed | True | naturalproductmech:mibig-d9dc3ff908 | Six cellular PhoP reporter/growth observations are falsely labeled ENZYME_INHIBITOR by title regex. |
| Original 2001 detailed method/citation and 1949 occurrence closure | unavailable | True | naturalproductmech:mibig-d9dc3ff908 | Required original bodies remain unavailable; later positive sources do not retroactively certify their exact contents. |
| Independent live Rhea equation endpoint | unavailable | False | naturalproductmech:mibig-d9dc3ff908 | The Rhea TSV request failed. Current UniProt annotation and primary chemistry independently support the represented reaction. |
| Stored chemical representation and complete source row | passed | True | naturalproductmech:mibig-d9dc3ff908 | Fresh intake derivation agrees with the stored graph; the source selector, full row and prepared snapshot were independently rechecked. |
| Literal PubChem exact parent identity | failed | True | naturalproductmech:mibig-d9dc3ff908 | CID5959 has two R centres and is not the exact unspecified owner graph; NPA016373 matches the owner precision. |
| Rendered observation sample identity | failed | True | naturalproductmech:mibig-d9dc3ff908 | All three deposited substances for the25 written observations encode RR, but observations are attached without a tested-stereoisomer qualification to the unspecified owner. Source outcomes and numbers are separate questions. |
| Explicit parent versus RR pathway-endpoint distinction | passed | True | naturalproductmech:mibig-d9dc3ff908 | The owner expressly distinguishes its incomplete parent from CHEBI:17698 in the CmlI pathway and causal graph. Current three-star CHEBI:17698 is RR; CHEBI:47325 is its distinct amino precursor. No accidental pathway-node identity defect is inferred. |

## Scientific And Domain Assessments

### Native status and complete retained audit history

provenance: supported. Targets: naturalproductmech:mibig-d9dc3ff908.

The six retained events comprise four source-seeding events and two 2026-10-01 RECORD_CURATED events adding the CmlI step/graph and correcting citation-title capitalization. The owner still has SEEDED status. These history events are provenance claims, not an earlier structured-review pass; their mechanism content is assessed separately.

### Present optional assertions and enrichment scope

completeness: supported. Targets: naturalproductmech:mibig-d9dc3ff908.

The complete one-step CmlI pathway, one BIOSYNTHESIS graph with three nodes and two edges, all25 written assay observations and ENZYME_INHIBITOR summary are present. Their identity, protein grounding, claim-level primary evidence and assay interpretation require the separate chemical and scientific assessments. The explicit graph/owner stereochemical distinction is preserved. No optional assertion is silently omitted from the audit.

### Exact-key computed classification provenance

representation: supported. Targets: naturalproductmech:mibig-d9dc3ff908.

The owner reproduces its exact-key NPClassifier result and version npclassifier.gnps2.org@2026-09-07, including Alkaloids filing, superclass/class labels and glycoside prediction false. Computed labels are not independent evidence for precursor use or natural origin. Any corrected chemical identity must be reclassified against its corrected effective key.

### Literal organism identifier routing

grounding: supported. Targets: naturalproductmech:mibig-d9dc3ff908.

The literal source identifiers and names resolve consistently. Their experimental occurrence and stock claims remain separately assessed.

### Taxonomic synonym and experimental-stock boundaries

provenance: supported. Targets: naturalproductmech:mibig-d9dc3ff908.

NCBI strain 953739 S. venezuelae ATCC10712 explicitly lists ISP5230 as a synonym; its species parent is 54571. This supports the exact native CmlI stock bridge. It does not equate recombinant E. coli protein production, S. coelicolor whole-cluster expression or Salmonella bioassays with native production.

### Native producer and experimental-host transcriptomic applicability

completeness: not_applicable. Targets: naturalproductmech:mibig-d9dc3ff908.

S. venezuelae ATCC10712/ISP5230 is absent. S. coelicolor, E. coli and S. enterica catalogue entries are not automatic matches to the engineered M1152 cluster host, recombinant BL21 enzyme construct, or specific PhoP reporter strains and conditions. No module assignment is made.

### biosynthesis_origin and producer_organisms[0]

evidence: supported. Targets: naturalproductmech:mibig-d9dc3ff908.

Named chloramphenicol has positive native S. venezuelae biosynthetic evidence, including the native overexpression result and the original abstract reporting mutant genetics. The 2014 WT negative is limited to tested conditions. Preserve the distinction between native ATCC 10712, its engineered M1582 derivative, heterologous M1152 hosts and recombinant E. coli. Exact stereo transfer to the parent is independently adjudicated by chemistry.

### biosynthetic_gene_clusters[0] methods, grades, accession and source citation

evidence: supported. Targets: naturalproductmech:mibig-d9dc3ff908.

The four method categories have support across the original native-genetic abstract, 2014 heterologous deletion/rescue and expression/product study, and 2012/2017 enzyme studies. Retain strong locus support with each experiment correctly routed. The sole imported 2001 citation does not by itself document all later experiments; detailed original 2001 scope remains unavailable. The sequence window contains native CmlI, but its complete outer boundaries are not independently proven by a single CDS match.

### biosynthetic_pathway[0], including all five evidence entries

evidence: supported. Targets: naturalproductmech:mibig-d9dc3ff908.

The terminal CmlI arylamine-to-nitro transformation is directly supported by the 2012 reconstitution and 2017 kinetic study. Both snippets are exact contiguous title text. The step already correctly states that substrate/product CHEBI:47325/17698 are the exact stereochemical reaction and the parent remains incomplete. Native F2RB83 matches the genomic CDS; protein evidence uses a His6 construct, not an untagged native assay. Current UniProt supports the Rhea equation, while the independent live Rhea endpoint is unavailable.

### causal_graphs[0].nodes[0..2] and edges[0..1]

evidence: supported. Targets: naturalproductmech:mibig-d9dc3ff908.

Both edges—NH2-CAM N-oxygenation by CmlI and CmlI formation of chloramphenicol—have direct primary biochemical support. The graph explicitly qualifies exact ChEBI stereo versus the owner. Retention wording is appropriately supported rather than absolute: no zero-exchange or all-constants-directly-measured claim is introduced. The three-node graph need not enumerate every mechanistic intermediate to remain valid.

### occurrences[0]

evidence: unknown. Targets: naturalproductmech:mibig-d9dc3ff908.

The historical 1949 S. venezuelae LOTUS occurrence remains a source assertion. Later native biosynthesis supports the named natural product but does not substitute for the unavailable exact original chemical-studies IV isolation scope. No occurrence deletion is justified solely by that access gap.

### bioactivities[4], [7], [10], [11], [12], [13] and bioactivity_summary

evidence: concern. Targets: naturalproductmech:mibig-d9dc3ff908.

The six Active IC50 calls and values match current original depositions, but their ENZYME_INHIBITOR labels are unsupported. They measure virK-GFP expression or nmpC-GFP culture growth; positive counterscreens limit selective PhoP interpretation. Keep the data and assay context without claiming direct enzyme inhibition, direct binding or demonstrated fluorescence artefact.

### bioactivities[0..3]

evidence: supported. Targets: naturalproductmech:mibig-d9dc3ff908.

Both duplicated source-target variants retain the same HTR2A agonist Inactive and antagonist Inconclusive calls, generic Potency and µM values. These are CHO-cell calcium responses, not direct receptor binding or positive clinical agonism.

### bioactivities[5..6] and target_enzyme O14656

evidence: supported. Targets: naturalproductmech:mibig-d9dc3ff908.

The Inconclusive phenotype call and Potency are faithfully represented. O14656 identifies the deposited torsin target context; the actual screening construct is EGFP-hTOR1A-delE with a WT comparator. It is not evidence of direct purified native torsin inhibition, and no positive activity class is asserted.

### bioactivities[8..9]

evidence: supported. Targets: naturalproductmech:mibig-d9dc3ff908.

MCF10a Inconclusive and SW480 Inactive calls remain distinct, despite small fitted Potency values. Nuclear DNA-content imaging does not prove direct geminin inhibition; leaving the non-UniProt accession ungrounded is faithful.

### bioactivities[14..18]

evidence: supported. Targets: naturalproductmech:mibig-d9dc3ff908.

ADRB2, HepG2 viability and CHRM1 rows retain Inconclusive calls and exact generic Potency values. Their cellular cAMP, viability and calcium readouts are not silently converted to direct receptor binding or a positive caspase mechanism.

### bioactivities[19..24]

evidence: supported. Targets: naturalproductmech:mibig-d9dc3ff908.

CYP2C19 is Active while CYP1A2/CYP2C9 are Inconclusive. The enzyme/proluciferin/NADPH assays differ from the PhoP cellular reporters; general luminescence-interference warnings do not by themselves prove sample interference. Retain exact generic Potency labels/values and refrain from converting them to IC50 or applying the positive call to all CYPs.

### All 25 written assays, the omitted-count note and raw source extent

representation: supported. Targets: naturalproductmech:mibig-d9dc3ff908.

The deterministic first-25 projection and 166 omitted count reproduce all 191 matching raw rows. This audit scientifically scopes every written observation; it does not certify all omitted assay protocols. Exact RR deposited samples require the separate identity action before any old-key migration, regardless of numerical source agreement.

### Stored representation and source-concept provenance

identity: supported. Targets: naturalproductmech:mibig-d9dc3ff908.

The complete source row BGC0000893:1 and source-concept hash reproduce this stored representation; this does not establish that the upstream compound label is correct. Formula, charge, Standard and fixed-H distinctions are independently recorded. Primary support and any conflicting exact xref are assessed separately.

### Exact authority eligibility and source representation

provenance: supported. Targets: naturalproductmech:mibig-d9dc3ff908.

No exact eligible row exists in the committed ChEBI projection for this owner. Current bounded name/key searches do not justify a different congener or a two-star grounding.

### Intentionally unspecified parent and exact pathway endpoint

representation: supported. Targets: naturalproductmech:mibig-d9dc3ff908.

The owner explicitly records the difference between the parent and exact RR pathway endpoint, including its curation history. This truthful boundary must survive any later identity adjudication; it does not qualify unrelated unannotated exact xrefs or assay samples.

### Assayed RR sample versus unresolved parent precision

grounding: concern. Targets: naturalproductmech:mibig-d9dc3ff908.

The literal CID and sample declarations are narrower at both centres. This is a precision mismatch, not a different constitution or proof that other stereoisomers share the reported activities. All25 observations remain deposited measurements/calls with their original outcomes; the separate PhoP classifier finding is owned by science.

## Findings

### S130-F-PHOP: Cellular PhoP reporter results are mislabeled as enzyme inhibition

major / open / confirmed; issue key: pubchem-phop-cellular-reporter-enzyme-class.

All six source protocols measure bacterial reporter fluorescence or culture-growth counterscreens. The generic title regex supplies ENZYME_INHIBITOR without direct enzyme evidence, and those labels supply the current summary. Positive counterscreens also preclude inferring selective PhoP inhibition. Calls/IC50 values remain valid deposited observations, subject to the independent sample-identity adjudication.

### C130-F-SAMPLE-PRECISION: RR PubChem and assay samples are attached as exact identity to an unspecified parent

major / open / confirmed; issue key: chloramphenicol-unspecified-parent-rr-xref-assay-identity.

The literal PubChem5959 and three deposited substances behind all25 written observations specify RR, whereas the owner deliberately leaves both centres undefined. The pathway already explains its separate RR endpoint, so that curated distinction is sound. The unqualified exact xref and assay association still lose the tested-sample precision and cannot establish activity of an unspecified stereochemical population.

## Recommended Actions And Acceptance Checks

### S130-ACT-PHOP

Implement a tested class-withholding/context rule in the actual seeder/curate path for the exact six rows at old key WIIZWVCIJKGZOK-UHFFFAOYSA-N, CID 5959: [{"aid": "2401", "owner_index": 4, "row_sha256": "5dc176943d786873f8a46cbeaf653502b3f481c82455ae6a36d19521481805f0"}, {"aid": "2384", "owner_index": 7, "row_sha256": "106c735adda7b7fbf5ac343138857b221c1db5e05675ada22a8cc80a2127c8fd"}, {"aid": "1985", "owner_index": 10, "row_sha256": "f1cf5fc6a3eacab6a05cc14a851164c2a80d42ba713f2670cbf2f90024f6ddb9"}, {"aid": "1981", "owner_index": 11, "row_sha256": "8c2ef02862f357b0f77c4e5d534241f30e389a0e14adc6760da4b1767e31127a"}, {"aid": "1863", "owner_index": 12, "row_sha256": "16f2a0875255a5087de47f55c572e05efc8e27b373991c06793e748b8a56bc74"}, {"aid": "1850", "owner_index": 13, "row_sha256": "bb20eadc0bb0639914a2b57ae6be990ee75f210f5e82ad71f08b93f34fecf9f8"}]. A new typed rule should consume each complete source-row digest, exact AID/title/protocol snapshot, outcome and endpoint, and remove only the unsupported ENZYME_INHIBITOR assignment while preserving valid Active/IC50/µM observations wherever exact sample identity is accepted. Retain separate virK reporter versus first/modified nmpC growth-counter-screen context. The current classify_activity(title, aid) interface does not enforce those row guards; extend it or add an explicitly consumed guarded overlay. Existing bioassay_exclusions removes whole observations and is not a class-only repair. Coordinate with the separate RR-versus-unspecified identity migration; do not transfer old-key rows automatically.

- Reject stale, duplicate, missing or ambiguous row decisions; pin all fields rather than only title or AID.
- Preserve six exact Active calls and unqualified IC50 values/units when the corresponding exact chemical identity is retained. Do not invent a direct target, selective PhoP mechanism or proven GFP quenching.
- Recompute top-25 selection, omitted count and summary from accepted emitted observations. Removing these unsupported classes must not force deletion of independently supported enzyme evidence or add a replacement class without evidence.
- Keep inactive/inconclusive generic Potency rows unchanged, preserve distinct target-annotation variants and the raw 191-row inventory.
- Test class-only correction separately and in composition with exact-structure migration/exclusion; reject unreviewed old-key joins. Regenerate through maintained code, with no generated-YAML/raw hand edits or unused curation-table assumptions.

### C130-ACTION-IDENTITY-SCOPE

Keep the explicit unspecified-parent/RR-pathway distinction unless a separate complete natural-product identity adjudication justifies migration. For the retained parent, exclude only literal pubchem:5959 using source_id=BGC0000893:1, version5, expected_source_row_sha256=fcfd701588342825f9921ca6015d064e91d625dbdafed4672efb520dbfc55c78, exact old key=WIIZWVCIJKGZOK-UHFFFAOYSA-N, old SMILES=OCC(NC(=O)C(Cl)Cl)C(O)C1=CC=C(C=C1)N(=O)=O, database_ids=npatlas:NPA016373&#124;pubchem:5959&#124;chemspider:5744, actual curator/date and the stable PubChem reference. Preserve NPA016373 and the raw-only ChemSpider association; ChemSpider is not an emitted supported xref and the existing exclusion table does not accept that namespace. The xref exclusion alone cannot fix already persisted assays. Implement/test a source-identity qualification before assay exact-key joins and the25-item cap: retain tested RR key, CID5959, each actual SID/version and every complete source-row SHA in /130/current-sample-identity.json. Preserve all191 original rows and their191 full-row digests; distinguish the25 verified rendered rows from166 omitted endpoint-unreviewed rows. Either attach explicit tested-RR scope through a new supported schema/consumer contract or withhold nonexact owner associations with retained provenance. Do not silently restamp all rows with RR or allow newly exposed unreviewed rows after a partial exclusion. Current exclusions require one old-key/CID/AID row; AIDs1645839,1671197,1671198,1671199,1963586,1963587,1963588,1963593 each have target-accession variants, so add a reviewed complete-row/target selector or explicit grouped-pin contract rather than claiming the existing selector accepts them. Preserve Active/Inactive/Inconclusive mapping, numeric values, units and target annotations without deduplication by name. Compose the separate six-PhoP class-only repair with the final tested-identity decision. If a later approved natural RR replacement uses CHEBI:17698, pin its current full target row (85bbf640cd55be9647b8b85cfaacb9f009413e11e2ef99bd21576e3dc1e38a4b), independently verify the full graph and collision state, derive chemistry, and explicitly migrate/revalidate the curated CmlI pathway, graph, history and same-key-dependent discussions. The seeder refuses old-owner identity changes and does not carry curator-owned fields across changed keys. Do not move old LOTUS, classifier, sibling or assay claims by path continuity alone.

- Reject full raw-row drift, CID/SID/key mismatch, missing sample identity, ambiguous target selectors and duplicate decisions.
- Demonstrate25 current observations map to17 AIDs and three RR substances; retain191raw/166omitted accounting and all original values/outcomes without claiming unseen endpoint review.
- Verify identity qualification is applied before the rendering cap so withheld rows cannot expose unchecked exact associations.
- Preserve the existing explicit parent/RR pathway caveat and all curated fields; any approved key migration must explicitly prove their new owner and preserve history.
- Run targeted contract tests and documented extraction/seed canary/reproduction/QC after authorized implementation. This review executes none of those mutations or tests.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R130-OWNER | data/natural_products/alkaloids/chloramphenicol.yaml; Complete owner, all present assertions and complete audit history | supports | Root read the complete chloramphenicol owner after official intake. It contains 1 occurrence, 1 producer and 1 locus assertions. Referenced external components are empty. Present optional fields: biosynthetic_pathway, causal_graphs, bioactivities, bioactivity_summary. |
| R130-LOCAL | /private/tmp/npm-review-work/130/local-sources.json; Complete resolved owner and all six captured exact matching source-row sets | context_only | Root read every captured MIBiG, LOTUS, ChEBI structures/origins, CyanoMetDB and NPClassifier row, including empty sets. The owner and captured rows match the prepared source snapshot. Separate PubChem raw observations are assessed by the scientific section. Source fidelity alone does not establish experimental support. |
| R130-Q7623398 | https://www.wikidata.org/wiki/Q7623398; Literal P225/P685 fields in retained complete multi-entity response | context_only | Literal Q7623398 scientific names and NCBI identifiers match the imported rows. This verifies identifier routing; it does not validate the occurrence citation, production or stock identity. |
| R130-TAXON-CONTEXT | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;retmode=xml&amp;id=162396,1905,1981977,2062,2502037,27334,292,339670,36816,371126,38033,40623,5149,54571,66425,68195,953739,97398; ScientificName, Rank, ParentTaxId and OtherNames for the exact relevant taxon records | context_only | NCBI strain 953739 S. venezuelae ATCC10712 explicitly lists ISP5230 as a synonym; its species parent is 54571. This supports the exact native CmlI stock bridge. It does not equate recombinant E. coli protein production, S. coelicolor whole-cluster expression or Salmonella bioassays with native production. |
| R130-IMODULON | https://imodulondb.org/api/datasets; Complete official 20-organism/28-dataset catalogue | context_only | The retained current catalogue was read and its bytes match the previously inspected catalogue. It establishes membership only, not production or module applicability. |
| S130-E-LOCAL | data/natural_products/alkaloids/chloramphenicol.yaml; Complete actual owner, resolved components and all exact matching local source rows | supports | Exact source selector BGC0000893:1 version 5; complete parsed source row SHA256 fcfd701588342825f9921ca6015d064e91d625dbdafed4672efb520dbfc55c78. Current methods 'Knock-out studies&#124;Enzymatic assays&#124;Heterologous expression&#124;Gene expression correlated with compound production'; source grades BGC_CHARACTERIZED/CLUSTER_DEMONSTRATED. Present science claims were compared with the formal intake; source preparation is not treated as another formal target. |
| S130-E-2012 | DOI:10.1016/j.tet.2012.06.036; Complete primary body and methods; original author-PDF Scheme 1/Figure 1 previously inspected and retained | supports | S. venezuelae CmlI is expressed as N-terminal His6 protein in E. coli BL21(DE3). Purified protein converts synthetic (1R,2R) NH2-CAM to chloramphenicol using PMS/NADH and oxygen; representative conditions are 250 µM substrate, 5–20 µM enzyme, 100 µM PMS, 1 mM NADH, HEPES pH 7.5 at 23–25 °C. Fed-substrate E. coli conversion is distinct from whole-cluster heterologous reconstruction. The native enzyme core is 339 residues; complete fusion sequence was not reconstructed. |
| S130-E-2017 | DOI:10.1021/acs.biochem.7b00695; Complete body, kinetic Results/Discussion and stated model; exact title-prefix snippets checked | supports | Transient kinetics and product evidence support the final three-step arylamine oxidation, internal hydroxylamine redox and efficient intermediate retention. This is kinetic preference, not proof of zero intermediate exchange: nitroso exchange under high external substrate is explicitly discussed. Some elementary constants are model-fitted. The principal reduced-diiron stopped-flow conditions at pH 9 and 4 °C differ from the 2012 mediator assay. |
| S130-E-2017SI | DOI:10.1021/acs.biochem.7b00695; Complete five-page official SI; expression and reaction methods, original S2 pixels | supports | The recombinant preparation and kinetic methods support construct/assay context. Printed unusual high expression concentrations are retained as source wording, not silently changed to presumed micro-units. The complete expressed tag/junction is not independently reconstructed. |
| S130-E-2014 | DOI:10.1128/AAC.04272-14; Complete scientific body/tables; original Figures 3–5 and Methods/Results re-read | supports | Native ATCC 10712 cmlR/sven0913 overexpression M1582 yields about 3.5 µg/mL chloramphenicol at 72 h; vector control is undetectable under tested conditions. S. coelicolor M1152/pAH91 M1581 is the heterologous final-product host. Its sven0913 deletion loses production and rescue restores it; sven0914/0915 deletions reduce rather than abolish production. Transcript/product comparisons support association. These are not native ATCC 10712 deletions and do not establish universal WT incapacity. |
| S130-E-2014SI | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4249514/supplementaryFiles; Complete four-page SI and original primary construct tables | supports | PCR/construct details support heterologous deletion/rescue and native overexpression. Internal source gene-label inconsistencies remain explicitly bounded; main Methods/Results identify sven0913, and a copied table label is not used to invent a different genotype. |
| S130-E-NATIVE | https://www.ncbi.nlm.nih.gov/nuccore/FR845719.1?from=1039846&amp;to=1061851; Exact stored-window source/features and complete SVEN_0924 CDS | supports | The native CmlI CDS is complement(1055073..1056092), wholly within the emitted FR845719.1 region. It encodes CCA54211.1, 339 amino acids. This is a native reference sequence, not the exact recombinant tag fusion or the 33–339 crystallographic construct. |
| S130-E-UNIPROT | https://www.uniprot.org/uniprotkb/F2RB83; Complete current entry identity, sequence, catalytic annotation and relevant reference/construct qualifiers | supports | Reviewed F2RB83, entry version 66/sequence version 1, is native SVEN_0924 at taxon 953739. Its reaction annotation links RHEA:58884, CHEBI:47325 and CHEBI:17698 and the net AH2 + 2 O2 chemistry. Later references and crystallographic residue range are not silently substituted for the two cited full-enzyme assays. |
| S130-E-SEQUENCE | /private/tmp/npm-review-work/shared-next-batch013/bgc-science/cmli-native-comparison.json; Independent complete genomic-CDS translation versus deposited translation and current UniProt | supports | All 339 native residues agree; amino-acid SHA256 8d4904a53743323a464a77231d5915d88647c16de7738dda2c6f48b6e1ccb896. The full 1,020 nt CDS includes a terminal stop. This establishes sequence identity, not experimental identity of complete tags or catalytic evidence from equality. |
| S130-E-2001ABSTRACT | PMID:11577160; Complete original abstract, not the unavailable main body | supports | The original abstract reports native ISP5230 mutant complementation and targeted ORF disruptions, supporting a native genetic association at abstract scope. It does not establish all detailed modern locus boundaries or every later assay category. |
| S130-E-GAP | /private/tmp/npm-review-work/shared-next-batch013/bgc-science/source-notes.json; Original 2001/1949 primary routes and failed live Rhea endpoint | unknown | The original PMID 11577160 abstract positively reports native ISP5230 mutant complementation/disruption, but its detailed body is unavailable. The 1949 DOI 10.1021/ja01175a065 occurrence body is also unavailable; its exact occurrence cannot be certified from title alone. The live Rhea TSV returned 500; current UniProt independently supplies its equation annotation. |
| S130-E-PROJECTION | /private/tmp/npm-review-work/130/assay-intake-comparison.json; All 191 parsed source rows; exact selected first 25 compared against current formal owner | supports | The actual current owner reproduces 25 written observations and the 166-omitted note. All 25 literal assay names, calls, values and units match their selected raw rows. Repeated target-blank/target-annotated source rows remain distinct. This verifies projection, not assay mechanism or exact chemical sample identity. |
| S130-E-PHOP2401 | pubchem.aid:2401; Original official assay description/protocol/comments; exact deposited SID 47193729 outcome joined separately | supports | Whole-cell non-Mg2+-responsive nmpC-GFP culture-growth counterscreen; 10 micromolar Mg2+ first counterscreen. The source records Active with IC50 9.59 µM, without a nonempty censoring modifier. This is a cellular reporter/culture-growth endpoint, not a purified-enzyme inhibition assay. |
| S130-E-PHOP2384 | pubchem.aid:2384; Original official assay description/protocol/comments; exact deposited SID 47193729 outcome joined separately | supports | Whole-cell non-Mg2+-responsive nmpC-GFP culture-growth counterscreen; 10 micromolar Mg2+ first counterscreen. The source records Active with IC50 1.57 µM, without a nonempty censoring modifier. This is a cellular reporter/culture-growth endpoint, not a purified-enzyme inhibition assay. |
| S130-E-PHOP1985 | pubchem.aid:1985; Original official assay description/protocol/comments; exact deposited SID 47193729 outcome joined separately | supports | Whole-cell non-Mg2+-responsive nmpC-GFP culture-growth counterscreen; 1 mM Mg2+ modified conditions. The source records Active with IC50 2.713 µM, without a nonempty censoring modifier. This is a cellular reporter/culture-growth endpoint, not a purified-enzyme inhibition assay. |
| S130-E-PHOP1981 | pubchem.aid:1981; Original official assay description/protocol/comments; exact deposited SID 47193729 outcome joined separately | supports | Whole-cell non-Mg2+-responsive nmpC-GFP culture-growth counterscreen; 1 mM Mg2+ modified conditions. The source records Active with IC50 8.46 µM, without a nonempty censoring modifier. This is a cellular reporter/culture-growth endpoint, not a purified-enzyme inhibition assay. |
| S130-E-PHOP1863 | pubchem.aid:1863; Original official assay description/protocol/comments; exact deposited SID 47193729 outcome joined separately | supports | Whole-cell virK-GFP PhoP-responsive reporter, low Mg2+ induction; current version includes primary and confirmatory dose-response results. The source records Active with IC50 9.52 µM, without a nonempty censoring modifier. This is a cellular reporter/culture-growth endpoint, not a purified-enzyme inhibition assay. |
| S130-E-PHOP1850 | pubchem.aid:1850; Original official assay description/protocol/comments; exact deposited SID 47193729 outcome joined separately | supports | Whole-cell virK-GFP PhoP-responsive reporter, low Mg2+ induction; current version includes primary and confirmatory dose-response results. The source records Active with IC50 4.85 µM, without a nonempty censoring modifier. This is a cellular reporter/culture-growth endpoint, not a purified-enzyme inhibition assay. |
| S130-E-PHOPJOIN | /private/tmp/npm-review-work/shared-next-batch013/chemistry-prep/phoP-source-notes.json; All six exact AID/SID/direct endpoint joins and complete-row digests | supports | The compound is active in the virK-GFP screens and both first/modified nmpC-GFP growth counterscreens. These observations do not prove selective PhoP inhibition or direct binding. General fluorescence-interference warnings are not a demonstrated chloramphenicol quenching result. The full source rows and unqualified numeric endpoints are retained. |
| S130-E-AID1963587 | pubchem.aid:1963587; Complete official description/protocol/comments; exact 19-row summary join | supports | HTR2A agonist CHO-cell calcium-flux response; Inactive, 61.6448 µM generic Potency. Generic Potency remains OTHER, and a number is not promoted to an active call or IC50. Raw response curves were not independently refitted. |
| S130-E-AID1963586 | pubchem.aid:1963586; Complete official description/protocol/comments; exact 19-row summary join | supports | HTR2A antagonist CHO-cell calcium-flux response; Inconclusive, 0.0133 µM Potency. Generic Potency remains OTHER, and a number is not promoted to an active call or IC50. Raw response curves were not independently refitted. |
| S130-E-AID1645839 | pubchem.aid:1645839; Complete official description/protocol/comments; exact 19-row summary join | supports | HEK293 EGFP-hTOR1A-delE localization phenotype, with a WT control and cell-count counter-readout; Inconclusive, 39.8107 µM Potency. O14656 is source target annotation, not proof of purified native torsin inhibition. Generic Potency remains OTHER, and a number is not promoted to an active call or IC50. Raw response curves were not independently refitted. |
| S130-E-AID624296 | pubchem.aid:624296; Complete official description/protocol/comments; exact 19-row summary join | supports | MCF10a nuclear Hoechst DNA-content phenotype; Inconclusive, 0.0052 µM Potency. Geminin metadata does not establish a direct target. Generic Potency remains OTHER, and a number is not promoted to an active call or IC50. Raw response curves were not independently refitted. |
| S130-E-AID624297 | pubchem.aid:624297; Complete official description/protocol/comments; exact 19-row summary join | supports | SW480 nuclear Hoechst DNA-content phenotype; Inactive, 0.0058 µM Potency. Generic Potency remains OTHER, and a number is not promoted to an active call or IC50. Raw response curves were not independently refitted. |
| S130-E-AID1963593 | pubchem.aid:1963593; Complete official description/protocol/comments; exact 19-row summary join | supports | CHO-ADRB2 cellular cAMP/HTRF assay; Inconclusive, 13.6854 µM Potency, not a purified receptor-binding assay. Generic Potency remains OTHER, and a number is not promoted to an active call or IC50. Raw response curves were not independently refitted. |
| S130-E-AID1346981 | pubchem.aid:1346981; Complete official description/protocol/comments; exact 19-row summary join | supports | HepG2 CellTiter-Fluor viability counterscreen; Inconclusive, 24.3365 µM Potency, not a positive caspase-induction mechanism. Generic Potency remains OTHER, and a number is not promoted to an active call or IC50. Raw response curves were not independently refitted. |
| S130-E-AID1963588 | pubchem.aid:1963588; Complete official description/protocol/comments; exact 19-row summary join | supports | CHO-CHRM1 cellular calcium-flux antagonist assay; Inconclusive, 3.7501 µM Potency. Generic Potency remains OTHER, and a number is not promoted to an active call or IC50. Raw response curves were not independently refitted. |
| S130-E-AID1671199 | pubchem.aid:1671199; Complete official description/protocol/comments; exact 19-row summary join | supports | CYP1A2 P450-Glo enzyme/proluciferin/NADPH luminescence assay; Inconclusive, 35.5742 µM Potency. Generic Potency remains OTHER, and a number is not promoted to an active call or IC50. Raw response curves were not independently refitted. |
| S130-E-AID1671197 | pubchem.aid:1671197; Complete official description/protocol/comments; exact 19-row summary join | supports | CYP2C19 P450-Glo enzyme/proluciferin/NADPH luminescence assay; Active, 4.4785 µM Potency; source signal-interference caveat retained. Generic Potency remains OTHER, and a number is not promoted to an active call or IC50. Raw response curves were not independently refitted. |
| S130-E-AID1671198 | pubchem.aid:1671198; Complete official description/protocol/comments; exact 19-row summary join | supports | CYP2C9 P450-Glo enzyme/proluciferin/NADPH luminescence assay; Inconclusive, 31.7055 µM Potency. Generic Potency remains OTHER, and a number is not promoted to an active call or IC50. Raw response curves were not independently refitted. |
| S130-E-OTHERJOIN | /private/tmp/npm-review-work/shared-next-batch013/bgc-science/other-assay-current-comparison.json; Exact nineteen non-PhoP AID/CID/SID/target/outcome/endpoint/value joins | supports | All nineteen written non-PhoP entries match one current source-summary row each. Call, endpoint and target-annotation variants remain separately represented; no mechanism is inferred from numeric agreement. |
| S130-E-SAMPLES | /private/tmp/npm-review-work/shared-next-batch013/bgc-science/assay-substance-addendum/source-notes.json; Exact deposited SID 144214022 and 49734345 JSON/SDF comparison, alongside PhoP SID 47193729 | supports | All three deposited assay substances encode neutral RR chloramphenicol; the parent owner is stereo-unspecified. The independent chemistry finding owns that precision/migration issue. This science audit does not treat an unspecified CID join as sample-equivalence proof. |
| S130-E-CONSUMERS | scripts/seed_from_sources.py; classify_activity lines 128–178; assay emission/cap/summary lines 1308–1380; actual exclusion helper | supports | The title pattern inhibitors? of adds ENZYME_INHIBITOR to all six Active PhoP observations. Their classes supply the written summary. The current classifier sees title/AID only; it has no complete-row-guarded class-only override. Existing bioassay exclusions remove entire observations and are not a class correction. |
| S130-E-SEARCH | /private/tmp/npm-review-work/130/curation-search.json; Bounded ignored-inclusive exact-AID and class-override searches | context_only | No exact six-AID curation decision or matched class-withholding/override route was found in the scoped searches; actual consumed classifier/exclusion code was also read. |
| C130-OWNER | data/natural_products/alkaloids/chloramphenicol.yaml; Complete owner and all local-source rows; no referenced components | supports | The complete owner denotes chloramphenicol under naturalproductmech:mibig-d9dc3ff908. Its exact source selector is BGC0000893:1, version 5, with complete parsed raw-row SHA256 fcfd701588342825f9921ca6015d064e91d625dbdafed4672efb520dbfc55c78. The official intake and prepared owner bytes agree. |
| C130-GRAPH | /private/tmp/npm-review-work/130/chemistry.json; Fresh intake RDKit result and frozen Standard/fixed-H comparison | supports | The stored SMILES recomputes to WIIZWVCIJKGZOK-UHFFFAOYSA-N, formula C11H12Cl2N2O5, formal charge 0; stored InChI/key agree. These are representation checks, not experimental identity proof. |
| C130-COMPARISON | /private/tmp/npm-review-work/shared-next-batch013/chemistry-prep/chemical-comparison.json; Record 130; exact source rows and each graph comparison | supports | Exact Standard, fixed-H, formula, charge and stereo comparisons of the retained owner, complete raw rows and current authority responses; primary experimental proof is assessed separately. |
| C130-LOCAL-SEARCH | /private/tmp/npm-review-work/130/chemistry-search-receipt.json; Exact full key, label, slug and source selector in raw/owner/curation trees | supports | Ignored-inclusive bounded search preserves all matching paths; an absent curation decision does not imply a missing scientific source. |
| C130-CHEBI-SEARCH-1 | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=WIIZWVCIJKGZOK-UHFFFAOYSA-N&amp;size=100; Literal key search; chebi-key-chloramphenicol.json | supports | 1 returned name/key results; evaluate exact key and stars, not name similarity. |
| C130-CHEBI-SEARCH-2 | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=chloramphenicol&amp;size=100; Literal name search; chebi-name-chloramphenicol.json | supports | 10 returned name/key results; evaluate exact key and stars, not name similarity. |
| C130-AUTH-1 | https://mibig.secondarymetabolites.org/repository/BGC0000893.5/annotations.json; compounds[].structure; BGC0000893.5.json | supports | current MIBiG BGC0000893:1: parsed key WIIZWVCIJKGZOK-UHFFFAOYSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C130-AUTH-2 | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/WIIZWVCIJKGZOK-UHFFFAOYSA-N/property/MolecularFormula,InChI,InChIKey,CanonicalSMILES,IsomericSMILES,Charge/JSON; PropertyTable.Properties[].SMILES; pubchem-key-chloramphenicol.json | supports | PubChem 298: parsed key WIIZWVCIJKGZOK-UHFFFAOYSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C130-AUTH-3 | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/chloramphenicol/property/MolecularFormula,InChI,InChIKey,CanonicalSMILES,IsomericSMILES,Charge/JSON; PropertyTable.Properties[].SMILES; pubchem-name-chloramphenicol.json | context_only | PubChem 5959: parsed key WIIZWVCIJKGZOK-RKDXNWHRSA-N; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C130-AUTH-4 | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/5959/property/MolecularFormula,InChI,InChIKey,CanonicalSMILES,IsomericSMILES,Charge/JSON; PropertyTable.Properties[].SMILES; pubchem-5959.json | context_only | PubChem 5959: parsed key WIIZWVCIJKGZOK-RKDXNWHRSA-N; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C130-AUTH-5 | https://www.npatlas.org/api/v1/compound/NPA016373; smiles; NPA016373.json | supports | NPAtlas literal NPA016373: parsed key WIIZWVCIJKGZOK-UHFFFAOYSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C130-AUTH-6 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/94390/; default_structure.smiles; CHEBI94390.json | supports | ChEBI JSON 94390: parsed key WIIZWVCIJKGZOK-UHFFFAOYSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C130-AUTH-7 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/94390/; official molfile endpoint; CHEBI94390-official.mol | supports | ChEBI MOL 94390: parsed key WIIZWVCIJKGZOK-UHFFFAOYSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C130-AUTH-8 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/17698/; default_structure.smiles; CHEBI17698.json | context_only | ChEBI JSON 17698: parsed key WIIZWVCIJKGZOK-RKDXNWHRSA-N; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C130-AUTH-9 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/17698/; official molfile endpoint; CHEBI17698-official.mol | context_only | ChEBI MOL 17698: parsed key WIIZWVCIJKGZOK-RKDXNWHRSA-N; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C130-AUTH-10 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/47325/; default_structure.smiles; CHEBI47325.json | context_only | ChEBI JSON 47325: parsed key BFLNGKUCFYKCFZ-RKDXNWHRSA-N; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C130-AUTH-11 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/47325/; official molfile endpoint; CHEBI47325-official.mol | context_only | ChEBI MOL 47325: parsed key BFLNGKUCFYKCFZ-RKDXNWHRSA-N; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C130-AUTH-12 | https://www.wikidata.org/wiki/Special:EntityData/Q27166237.json; P233; Q27166237.json | supports | Wikidata Q27166237: parsed key WIIZWVCIJKGZOK-UHFFFAOYSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. Canonical P233 is not an isomeric stereo assertion; compare P2017 when present. |
| C130-AUTH-13 | https://www.chemspider.com/Chemical-Structure.5744.html; JSON-LD InChI; chemspider5744.html | context_only | ChemSpider raw-only5744: parsed key WIIZWVCIJKGZOK-RKDXNWHRSA-N; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C130-SAMPLE-IDENTITY | /private/tmp/npm-review-work/130/current-sample-identity.json; Independent parsing of three deposited SDFs and exact current raw-row inventory | supports | SID47193729, SID144214022 and SID49734345 each encode neutral RR chloramphenicol, WIIZWVCIJKGZOK-RKDXNWHRSA-N. They cover the 25 written observations across 17 unique AIDs. The owner retains two undefined centres. All191 same-old-key raw rows carry CID5959;166 are omitted from the current rendering and were not all independently endpoint-audited. Eight written AIDs have multiple target-accession rows per old-key/CID/AID. |
| C130-PHOP-SID | https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/47193729/JSON; Literal deposited substance and CID association for the six PhoP rows | supports | The deposited substance is RR and associates with CID5959. Its exact tested-substance identity is narrower than the unresolved parent graph; protocol-specific activity interpretation remains in the science section. |
| C130-SID-144214022 | https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/144214022/JSON; Literal substance identifier, deposited graph and CID5959 association | supports | The official deposited JSON and independently parsed SDF retain RR chloramphenicol, not the stereo-unspecified parent. This is a database sample declaration, not a fresh lot-purity or natural absolute-hand experiment. |
| C130-SID-49734345 | https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/49734345/JSON; Literal substance identifier, deposited graph and CID5959 association | supports | The official deposited JSON and independently parsed SDF retain RR chloramphenicol, not the stereo-unspecified parent. This is a database sample declaration, not a fresh lot-purity or natural absolute-hand experiment. |
| C130-EXTRACTOR | scripts/extract_pubchem_bioassay.py; Inspected maintained identity and projection contract | supports | cid_to_key derives CID mapping from corpus xrefs without independently checking the CID graph; rows_from_summary copies that supplied owner key into each assay row. Thus the current exact-key label is not an independent test-sample identity determination. |
| C130-SEED | scripts/seed_from_sources.py; Inspected maintained identity and projection contract | supports | Assays join on the stored full key and are capped after sorting. Removing a subset can expose previously omitted rows. Curator pathway/graph fields are carried only when the owner full key is unchanged; identity replacement requires explicit migration. |
| C130-EXCLUSIONS | src/naturalproductmech/curate/bioassay_exclusions.py; Inspected maintained identity and projection contract | supports | Existing exclusions require exactly one complete old-key/CID/AID row and withhold entire observations. They cannot qualify a tested stereoisomer, rewrite keys, edit class only or select among duplicate target-accession rows. |
| C130-XREF-CONTRACT | src/naturalproductmech/curate/xref_exclusions.py; Inspected maintained identity and projection contract | supports | The existing seven-field literal-xref exclusion pins the complete original MIBiG row and retains source assertion in a discussion. It cannot repair already persisted assay joins or add a replacement CID. |
| C130-STRUCTURE-CONTRACT | src/naturalproductmech/curate/structure_corrections.py; Inspected maintained identity and projection contract | supports | Structure replacement requires a unique eligible three-star target, full source/target pins, collision checks and separate old-key joins; it is not automatic assay or curator-owned graph migration. |

## Limits And Additional Notes

- This is a claim-level review of present assertions and bounded source gaps, not an exhaustive search for every later paper or an obligation to add every optional mechanism.
- The 2001 biosynthetic main and 1949 occurrence main remain unavailable; source-faithful assertions are not rewritten from absence of access.
- Full tagged CmlI constructs and exact original protein-stock sequences were not reconstructed. Native CDS identity and assay provenance remain separate.
- The live Rhea endpoint failed; the present reaction has independent primary and current UniProt support.
- All written assay protocols/endpoints were scoped, but no original concentration-response refit, stock-purity test or scientific review of all 166 omitted observations was performed.
- Exact assay-sample stereochemistry and owner identity are handled by the separate chemistry finding; numerical agreement does not resolve that issue.
- Authority matches establish the representations actually returned at their retained access times; they are not independent experimental structure or absolute-hand determinations. Root and science sections separately assess organism, locus, classification and history claims.
- The deposited SDFs establish declared sample structures, not independently measured lot purity or a new natural absolute configuration.
- All25 rendered sample identities were covered; the166 omitted assay endpoints were not all scientifically re-reviewed. Their raw presence must not be treated as an exact-identity or mechanistic endorsement.
- The science packet owns assay endpoint fidelity, PhoP classification and CmlI experimental scope; those findings are not duplicated here.
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
review_id: 20261021T180457Z-chloramphenicol
title: 'Chloramphenicol: sample identity, cellular assay classes and CmlI review'
started_at: '2026-10-21T17:52:21.104850Z'
finished_at: '2026-10-21T18:04:57.755983Z'
completion: partial
verdict: needs_curation
scientific_review: true
summary: The parent graph deliberately leaves both stereocentres undefined, while
  literal PubChem 5959 and all deposited samples behind the 25 written observations
  specify RR. One major finding requests exact tested-sample qualification; a second
  addresses six cellular PhoP assays incorrectly classified as enzyme inhibition.
  Numeric calls and projection reproduce the source rows. The explicitly qualified
  CmlI pathway and graph are supported; original 2001 and 1949 bodies remain unavailable.
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
    role: context
  - path: data/natural_products/alkaloids/chloramphenicol.yaml
    sha256: d1c483e457d58b0306462795af8f027a3ed4dd22d781ed6044b193151a83a793
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
  - path: src/naturalproductmech/curate/xref_exclusions.py
    sha256: 17c3d9e7794bae596b22cf19a2dd5bc2169475d6fea81ea4e6f1781a53af9157
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
  selection: Campaign record 130, batch 013, selected in path order from the fresh-main
    authoritative validated catalogue and the separately validated targets in earlier
    batch commits (publication tracked separately). At selection, 174 of 3116 current
    records had campaign coverage and 2942 remained. The population search included
    ignored files. Exactly one target is assessed here.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-d9dc3ff908
targets:
- target_id: naturalproductmech:mibig-d9dc3ff908
  path: data/natural_products/alkaloids/chloramphenicol.yaml
  label: chloramphenicol
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
    path: data/natural_products/alkaloids/chloramphenicol.yaml
    role: Curator-owned assertions, inline mechanisms, discussions and audit history
checks:
- check_id: C-STRICT
  name: Closed-schema target validation
  status: passed
  required: true
  summary: The documented target strict validator completed; scientific support is
    assessed separately.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  command: just validate-strict data/natural_products/alkaloids/chloramphenicol.yaml
    --out /private/tmp/npm-review-work/130/strict.tsv
  exit_code: 0
  scope_note: Actual command finished 2026-10-21T17:52:22.959318Z
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
  - naturalproductmech:mibig-d9dc3ff908
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
  - naturalproductmech:mibig-d9dc3ff908
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
  - naturalproductmech:mibig-d9dc3ff908
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
  - naturalproductmech:mibig-d9dc3ff908
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
  - naturalproductmech:mibig-d9dc3ff908
- check_id: R130-FULL-OWNER
  name: Complete owner and referenced-component scope
  status: passed
  required: true
  summary: The complete owner and all six captured source-row sets were read after
    successful official intake and agree with the pinned preparation. The external
    component set is empty. Fresh strict validation is retained separately.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - R130-OWNER
  - R130-LOCAL
- check_id: S130-C-MECHANISM
  name: CmlI step/graph primary and native-reference support
  status: passed
  required: true
  summary: Primary biochemistry, appropriate kinetic scope and independent native
    CDS equality support the existing qualified step and graph.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - S130-E-2012
  - S130-E-2017
  - S130-E-UNIPROT
  - S130-E-SEQUENCE
- check_id: S130-C-ASSAY-PROJECTION
  name: All written assay calls and numeric projection
  status: passed
  required: true
  summary: All 25 current owner observations match the selected raw rows and current
    bounded source joins; 191 raw and 166 omitted are reproduced.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - S130-E-PROJECTION
  - S130-E-OTHERJOIN
  - S130-E-PHOPJOIN
- check_id: S130-C-CLASS
  name: Exact cellular assay activity-class support
  status: failed
  required: true
  summary: Six cellular PhoP reporter/growth observations are falsely labeled ENZYME_INHIBITOR
    by title regex.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - S130-E-PHOP2401
  - S130-E-PHOP2384
  - S130-E-PHOP1985
  - S130-E-PHOP1981
  - S130-E-PHOP1863
  - S130-E-PHOP1850
  - S130-E-CONSUMERS
- check_id: S130-C-HISTORICAL
  name: Original 2001 detailed method/citation and 1949 occurrence closure
  status: unavailable
  required: true
  summary: Required original bodies remain unavailable; later positive sources do
    not retroactively certify their exact contents.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - S130-E-GAP
- check_id: S130-C-RHEA
  name: Independent live Rhea equation endpoint
  status: unavailable
  required: false
  summary: The Rhea TSV request failed. Current UniProt annotation and primary chemistry
    independently support the represented reaction.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - S130-E-GAP
  - S130-E-UNIPROT
  - S130-E-2012
  - S130-E-2017
- check_id: C130-C-REPRESENTATION
  name: Stored chemical representation and complete source row
  status: passed
  required: true
  summary: Fresh intake derivation agrees with the stored graph; the source selector,
    full row and prepared snapshot were independently rechecked.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - C130-OWNER
  - C130-GRAPH
  - C130-COMPARISON
- check_id: C130-C-XREF
  name: Literal PubChem exact parent identity
  status: failed
  required: true
  summary: CID5959 has two R centres and is not the exact unspecified owner graph;
    NPA016373 matches the owner precision.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - C130-OWNER
  - C130-COMPARISON
  - C130-AUTH-1
  - C130-AUTH-2
  - C130-AUTH-3
  - C130-AUTH-4
  - C130-AUTH-5
  - C130-AUTH-6
  - C130-AUTH-7
  - C130-AUTH-8
  - C130-AUTH-9
  - C130-AUTH-10
  - C130-AUTH-11
  - C130-AUTH-12
  - C130-AUTH-13
- check_id: C130-C-SAMPLE
  name: Rendered observation sample identity
  status: failed
  required: true
  summary: All three deposited substances for the25 written observations encode RR,
    but observations are attached without a tested-stereoisomer qualification to the
    unspecified owner. Source outcomes and numbers are separate questions.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - C130-SAMPLE-IDENTITY
  - C130-PHOP-SID
  - C130-SID-144214022
  - C130-SID-49734345
  - C130-EXTRACTOR
  - C130-SEED
- check_id: C130-C-PATHWAY-BOUNDARY
  name: Explicit parent versus RR pathway-endpoint distinction
  status: passed
  required: true
  summary: The owner expressly distinguishes its incomplete parent from CHEBI:17698
    in the CmlI pathway and causal graph. Current three-star CHEBI:17698 is RR; CHEBI:47325
    is its distinct amino precursor. No accidental pathway-node identity defect is
    inferred.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - C130-OWNER
  - C130-COMPARISON
  - C130-AUTH-1
  - C130-AUTH-2
  - C130-AUTH-3
  - C130-AUTH-4
  - C130-AUTH-5
  - C130-AUTH-6
  - C130-AUTH-7
  - C130-AUTH-8
  - C130-AUTH-9
  - C130-AUTH-10
  - C130-AUTH-11
  - C130-AUTH-12
  - C130-AUTH-13
evidence:
- evidence_id: R130-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/chloramphenicol.yaml
  locator: Complete owner, all present assertions and complete audit history
  accessed_at: '2026-10-21T17:52:39.707072Z'
  support: supports
  summary: 'Root read the complete chloramphenicol owner after official intake. It
    contains 1 occurrence, 1 producer and 1 locus assertions. Referenced external
    components are empty. Present optional fields: biosynthetic_pathway, causal_graphs,
    bioactivities, bioactivity_summary.'
  snapshot_sha256: d1c483e457d58b0306462795af8f027a3ed4dd22d781ed6044b193151a83a793
- evidence_id: R130-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/130/local-sources.json
  locator: Complete resolved owner and all six captured exact matching source-row
    sets
  accessed_at: '2026-10-21T17:52:39.707072Z'
  support: context_only
  summary: Root read every captured MIBiG, LOTUS, ChEBI structures/origins, CyanoMetDB
    and NPClassifier row, including empty sets. The owner and captured rows match
    the prepared source snapshot. Separate PubChem raw observations are assessed by
    the scientific section. Source fidelity alone does not establish experimental
    support.
  snapshot_sha256: cba5f2b73f7b22feb5f7df36c0ef6c8a5344191cd8b5d1c720fda934b26c2fdd
- evidence_id: R130-Q7623398
  kind: database
  reference: https://www.wikidata.org/wiki/Q7623398
  locator: Literal P225/P685 fields in retained complete multi-entity response
  accessed_at: '2026-10-21T17:25:35.481159Z'
  support: context_only
  summary: Literal Q7623398 scientific names and NCBI identifiers match the imported
    rows. This verifies identifier routing; it does not validate the occurrence citation,
    production or stock identity.
  snapshot_sha256: 026cf7dce61f76ea1be554bf995a269a5531a82c3a0c74c5873851c736a1752b
- evidence_id: R130-TAXON-CONTEXT
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&retmode=xml&id=162396,1905,1981977,2062,2502037,27334,292,339670,36816,371126,38033,40623,5149,54571,66425,68195,953739,97398
  locator: ScientificName, Rank, ParentTaxId and OtherNames for the exact relevant
    taxon records
  accessed_at: '2026-10-21T17:25:35.685538Z'
  support: context_only
  summary: NCBI strain 953739 S. venezuelae ATCC10712 explicitly lists ISP5230 as
    a synonym; its species parent is 54571. This supports the exact native CmlI stock
    bridge. It does not equate recombinant E. coli protein production, S. coelicolor
    whole-cluster expression or Salmonella bioassays with native production.
  snapshot_sha256: 83ff126040853b0ab6de8dbf4dab0b64eaf4b2aea314a68d6caddfcba16f66dd
- evidence_id: R130-IMODULON
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete official 20-organism/28-dataset catalogue
  accessed_at: '2026-10-21T17:25:35.092545Z'
  support: context_only
  summary: The retained current catalogue was read and its bytes match the previously
    inspected catalogue. It establishes membership only, not production or module
    applicability.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: S130-E-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/chloramphenicol.yaml
  locator: Complete actual owner, resolved components and all exact matching local
    source rows
  accessed_at: '2026-10-21T18:02:41.988912Z'
  support: supports
  summary: Exact source selector BGC0000893:1 version 5; complete parsed source row
    SHA256 fcfd701588342825f9921ca6015d064e91d625dbdafed4672efb520dbfc55c78. Current
    methods 'Knock-out studies|Enzymatic assays|Heterologous expression|Gene expression
    correlated with compound production'; source grades BGC_CHARACTERIZED/CLUSTER_DEMONSTRATED.
    Present science claims were compared with the formal intake; source preparation
    is not treated as another formal target.
  snapshot_sha256: d1c483e457d58b0306462795af8f027a3ed4dd22d781ed6044b193151a83a793
- evidence_id: S130-E-2012
  kind: primary_source
  reference: DOI:10.1016/j.tet.2012.06.036
  locator: Complete primary body and methods; original author-PDF Scheme 1/Figure
    1 previously inspected and retained
  accessed_at: '2026-10-21T17:15:32.942179Z'
  support: supports
  summary: S. venezuelae CmlI is expressed as N-terminal His6 protein in E. coli BL21(DE3).
    Purified protein converts synthetic (1R,2R) NH2-CAM to chloramphenicol using PMS/NADH
    and oxygen; representative conditions are 250 µM substrate, 5–20 µM enzyme, 100
    µM PMS, 1 mM NADH, HEPES pH 7.5 at 23–25 °C. Fed-substrate E. coli conversion
    is distinct from whole-cluster heterologous reconstruction. The native enzyme
    core is 339 residues; complete fusion sequence was not reconstructed.
  snapshot_sha256: fdb16ae364e6af742a114d53d1d520f5a70d9c3aed724be7424f821f4cf88868
- evidence_id: S130-E-2017
  kind: primary_source
  reference: DOI:10.1021/acs.biochem.7b00695
  locator: Complete body, kinetic Results/Discussion and stated model; exact title-prefix
    snippets checked
  accessed_at: '2026-10-21T17:15:33.561612Z'
  support: supports
  summary: 'Transient kinetics and product evidence support the final three-step arylamine
    oxidation, internal hydroxylamine redox and efficient intermediate retention.
    This is kinetic preference, not proof of zero intermediate exchange: nitroso exchange
    under high external substrate is explicitly discussed. Some elementary constants
    are model-fitted. The principal reduced-diiron stopped-flow conditions at pH 9
    and 4 °C differ from the 2012 mediator assay.'
  snapshot_sha256: 77c63c508cbcca0998e085a17c17c5eae037a8b5b43fca156aee03b67c492f49
- evidence_id: S130-E-2017SI
  kind: primary_source
  reference: DOI:10.1021/acs.biochem.7b00695
  locator: Complete five-page official SI; expression and reaction methods, original
    S2 pixels
  accessed_at: '2026-10-21T17:20:32.970306Z'
  support: supports
  summary: The recombinant preparation and kinetic methods support construct/assay
    context. Printed unusual high expression concentrations are retained as source
    wording, not silently changed to presumed micro-units. The complete expressed
    tag/junction is not independently reconstructed.
  snapshot_sha256: 259048469feca6ec7d6bdf03bce2a9d5dc13d9f046dcde83a7fa955ea4296dea
- evidence_id: S130-E-2014
  kind: primary_source
  reference: DOI:10.1128/AAC.04272-14
  locator: Complete scientific body/tables; original Figures 3–5 and Methods/Results
    re-read
  accessed_at: '2026-10-21T17:19:47.790100Z'
  support: supports
  summary: Native ATCC 10712 cmlR/sven0913 overexpression M1582 yields about 3.5 µg/mL
    chloramphenicol at 72 h; vector control is undetectable under tested conditions.
    S. coelicolor M1152/pAH91 M1581 is the heterologous final-product host. Its sven0913
    deletion loses production and rescue restores it; sven0914/0915 deletions reduce
    rather than abolish production. Transcript/product comparisons support association.
    These are not native ATCC 10712 deletions and do not establish universal WT incapacity.
  snapshot_sha256: ca54a669f5cd0e564e51168dffef196f20915b95615e389f182dc1855aa516ed
- evidence_id: S130-E-2014SI
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4249514/supplementaryFiles
  locator: Complete four-page SI and original primary construct tables
  accessed_at: '2026-10-21T17:22:53.948602Z'
  support: supports
  summary: PCR/construct details support heterologous deletion/rescue and native overexpression.
    Internal source gene-label inconsistencies remain explicitly bounded; main Methods/Results
    identify sven0913, and a copied table label is not used to invent a different
    genotype.
  snapshot_sha256: 82058e7e3e430c1c89b4a5dad588a63c84190fd226c385ab12b2999cb2c81693
- evidence_id: S130-E-NATIVE
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/nuccore/FR845719.1?from=1039846&to=1061851
  locator: Exact stored-window source/features and complete SVEN_0924 CDS
  accessed_at: '2026-10-21T17:20:32.177903Z'
  support: supports
  summary: The native CmlI CDS is complement(1055073..1056092), wholly within the
    emitted FR845719.1 region. It encodes CCA54211.1, 339 amino acids. This is a native
    reference sequence, not the exact recombinant tag fusion or the 33–339 crystallographic
    construct.
  snapshot_sha256: e8f28248fd55601d614694fc51c9672256490c776c2edf21fe8c48110bf2df2a
- evidence_id: S130-E-UNIPROT
  kind: authority
  reference: https://www.uniprot.org/uniprotkb/F2RB83
  locator: Complete current entry identity, sequence, catalytic annotation and relevant
    reference/construct qualifiers
  accessed_at: '2026-10-21T17:20:31.602222Z'
  support: supports
  summary: Reviewed F2RB83, entry version 66/sequence version 1, is native SVEN_0924
    at taxon 953739. Its reaction annotation links RHEA:58884, CHEBI:47325 and CHEBI:17698
    and the net AH2 + 2 O2 chemistry. Later references and crystallographic residue
    range are not silently substituted for the two cited full-enzyme assays.
  snapshot_sha256: 11c80884b65f5ef74ebbf654d514708d7e6bcb0f24d5bed5b03c1349aacd1f45
- evidence_id: S130-E-SEQUENCE
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch013/bgc-science/cmli-native-comparison.json
  locator: Independent complete genomic-CDS translation versus deposited translation
    and current UniProt
  accessed_at: '2026-10-21T17:22:00.515307Z'
  support: supports
  summary: All 339 native residues agree; amino-acid SHA256 8d4904a53743323a464a77231d5915d88647c16de7738dda2c6f48b6e1ccb896.
    The full 1,020 nt CDS includes a terminal stop. This establishes sequence identity,
    not experimental identity of complete tags or catalytic evidence from equality.
  snapshot_sha256: 1b9c758d7d15ae80e3dbdc0a904ebad75f7db11d58e18a6e3d813d553f094712
- evidence_id: S130-E-2001ABSTRACT
  kind: primary_source
  reference: PMID:11577160
  locator: Complete original abstract, not the unavailable main body
  accessed_at: '2026-10-21T16:52:42.775983Z'
  support: supports
  summary: The original abstract reports native ISP5230 mutant complementation and
    targeted ORF disruptions, supporting a native genetic association at abstract
    scope. It does not establish all detailed modern locus boundaries or every later
    assay category.
  snapshot_sha256: 4ba2c57107d7635fc9d6505b1d8808259b4a435231e9fb4126ea268fdd812904
- evidence_id: S130-E-GAP
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch013/bgc-science/source-notes.json
  locator: Original 2001/1949 primary routes and failed live Rhea endpoint
  accessed_at: '2026-10-21T17:30:25.183480Z'
  support: unknown
  summary: The original PMID 11577160 abstract positively reports native ISP5230 mutant
    complementation/disruption, but its detailed body is unavailable. The 1949 DOI
    10.1021/ja01175a065 occurrence body is also unavailable; its exact occurrence
    cannot be certified from title alone. The live Rhea TSV returned 500; current
    UniProt independently supplies its equation annotation.
  snapshot_sha256: 86ba58da529384d774d2e5b81fb4825893bf1fa9beda7e82b7957337b9b18350
  search_scope: Retained exact official publisher PDF/HTML/body endpoints for 2001
    and 1949, original PubMed metadata and one Rhea TSV request, with failed responses
    preserved. No renewed blocked requests or inference of absence from access failures.
- evidence_id: S130-E-PROJECTION
  kind: record_content
  reference: /private/tmp/npm-review-work/130/assay-intake-comparison.json
  locator: All 191 parsed source rows; exact selected first 25 compared against current
    formal owner
  accessed_at: '2026-10-21T18:00:15.306074Z'
  support: supports
  summary: The actual current owner reproduces 25 written observations and the 166-omitted
    note. All 25 literal assay names, calls, values and units match their selected
    raw rows. Repeated target-blank/target-annotated source rows remain distinct.
    This verifies projection, not assay mechanism or exact chemical sample identity.
  snapshot_sha256: 82f7bfb70c6c1923d35b72837a37d7f0196301a68bb5e69cdb9d6c5721e77c49
- evidence_id: S130-E-PHOP2401
  kind: database
  reference: pubchem.aid:2401
  locator: Original official assay description/protocol/comments; exact deposited
    SID 47193729 outcome joined separately
  accessed_at: '2026-10-21T17:23:55.169147Z'
  support: supports
  summary: Whole-cell non-Mg2+-responsive nmpC-GFP culture-growth counterscreen; 10
    micromolar Mg2+ first counterscreen. The source records Active with IC50 9.59
    µM, without a nonempty censoring modifier. This is a cellular reporter/culture-growth
    endpoint, not a purified-enzyme inhibition assay.
  snapshot_sha256: b2431b9671f600a8094a5f2f2f74eccdf26c3312b7a751520462c80ca9277116
- evidence_id: S130-E-PHOP2384
  kind: database
  reference: pubchem.aid:2384
  locator: Original official assay description/protocol/comments; exact deposited
    SID 47193729 outcome joined separately
  accessed_at: '2026-10-21T17:23:55.162543Z'
  support: supports
  summary: Whole-cell non-Mg2+-responsive nmpC-GFP culture-growth counterscreen; 10
    micromolar Mg2+ first counterscreen. The source records Active with IC50 1.57
    µM, without a nonempty censoring modifier. This is a cellular reporter/culture-growth
    endpoint, not a purified-enzyme inhibition assay.
  snapshot_sha256: 53fbe6fcfe9e1031226ca134accecfc9dd7543c749a31567b30d29dd90e13192
- evidence_id: S130-E-PHOP1985
  kind: database
  reference: pubchem.aid:1985
  locator: Original official assay description/protocol/comments; exact deposited
    SID 47193729 outcome joined separately
  accessed_at: '2026-10-21T17:23:55.152290Z'
  support: supports
  summary: Whole-cell non-Mg2+-responsive nmpC-GFP culture-growth counterscreen; 1
    mM Mg2+ modified conditions. The source records Active with IC50 2.713 µM, without
    a nonempty censoring modifier. This is a cellular reporter/culture-growth endpoint,
    not a purified-enzyme inhibition assay.
  snapshot_sha256: 0c974a5b7265e2a355898581d24c2d71847f2643f5f51291619627644c3a752b
- evidence_id: S130-E-PHOP1981
  kind: database
  reference: pubchem.aid:1981
  locator: Original official assay description/protocol/comments; exact deposited
    SID 47193729 outcome joined separately
  accessed_at: '2026-10-21T17:23:55.155632Z'
  support: supports
  summary: Whole-cell non-Mg2+-responsive nmpC-GFP culture-growth counterscreen; 1
    mM Mg2+ modified conditions. The source records Active with IC50 8.46 µM, without
    a nonempty censoring modifier. This is a cellular reporter/culture-growth endpoint,
    not a purified-enzyme inhibition assay.
  snapshot_sha256: 427d082293a0479290cfa4d4166ebfb2e0f6ad0613d8fc12a5cd17120a8551de
- evidence_id: S130-E-PHOP1863
  kind: database
  reference: pubchem.aid:1863
  locator: Original official assay description/protocol/comments; exact deposited
    SID 47193729 outcome joined separately
  accessed_at: '2026-10-21T17:23:55.165872Z'
  support: supports
  summary: Whole-cell virK-GFP PhoP-responsive reporter, low Mg2+ induction; current
    version includes primary and confirmatory dose-response results. The source records
    Active with IC50 9.52 µM, without a nonempty censoring modifier. This is a cellular
    reporter/culture-growth endpoint, not a purified-enzyme inhibition assay.
  snapshot_sha256: 48a22b94e4bf88e8d0e5ffb54d88cadf5d2fa0b9ec81720f8e311d9f44acfb19
- evidence_id: S130-E-PHOP1850
  kind: database
  reference: pubchem.aid:1850
  locator: Original official assay description/protocol/comments; exact deposited
    SID 47193729 outcome joined separately
  accessed_at: '2026-10-21T17:23:55.533031Z'
  support: supports
  summary: Whole-cell virK-GFP PhoP-responsive reporter, low Mg2+ induction; current
    version includes primary and confirmatory dose-response results. The source records
    Active with IC50 4.85 µM, without a nonempty censoring modifier. This is a cellular
    reporter/culture-growth endpoint, not a purified-enzyme inhibition assay.
  snapshot_sha256: 18191801d27375562d4a8ce9d0c3c8fcfa5deade8004e535282081268a67f802
- evidence_id: S130-E-PHOPJOIN
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch013/chemistry-prep/phoP-source-notes.json
  locator: All six exact AID/SID/direct endpoint joins and complete-row digests
  accessed_at: '2026-10-21T17:28:28.911491Z'
  support: supports
  summary: The compound is active in the virK-GFP screens and both first/modified
    nmpC-GFP growth counterscreens. These observations do not prove selective PhoP
    inhibition or direct binding. General fluorescence-interference warnings are not
    a demonstrated chloramphenicol quenching result. The full source rows and unqualified
    numeric endpoints are retained.
  snapshot_sha256: 78c59a9847fac543c1ac3f292b24b994cffe4d933ac64010a1476093333fbd6c
- evidence_id: S130-E-AID1963587
  kind: database
  reference: pubchem.aid:1963587
  locator: Complete official description/protocol/comments; exact 19-row summary join
  accessed_at: '2026-10-21T17:23:22.376657Z'
  support: supports
  summary: HTR2A agonist CHO-cell calcium-flux response; Inactive, 61.6448 µM generic
    Potency. Generic Potency remains OTHER, and a number is not promoted to an active
    call or IC50. Raw response curves were not independently refitted.
  snapshot_sha256: 1a5a2bac18d8b75939863dd42f33232129b848c9091ebfa464398751ede35f90
- evidence_id: S130-E-AID1963586
  kind: database
  reference: pubchem.aid:1963586
  locator: Complete official description/protocol/comments; exact 19-row summary join
  accessed_at: '2026-10-21T17:23:22.686920Z'
  support: supports
  summary: HTR2A antagonist CHO-cell calcium-flux response; Inconclusive, 0.0133 µM
    Potency. Generic Potency remains OTHER, and a number is not promoted to an active
    call or IC50. Raw response curves were not independently refitted.
  snapshot_sha256: f8b6fd85162ce80e64513c8a8de590c7fe923e2d4453e3d9147161894f452109
- evidence_id: S130-E-AID1645839
  kind: database
  reference: pubchem.aid:1645839
  locator: Complete official description/protocol/comments; exact 19-row summary join
  accessed_at: '2026-10-21T17:23:22.265453Z'
  support: supports
  summary: HEK293 EGFP-hTOR1A-delE localization phenotype, with a WT control and cell-count
    counter-readout; Inconclusive, 39.8107 µM Potency. O14656 is source target annotation,
    not proof of purified native torsin inhibition. Generic Potency remains OTHER,
    and a number is not promoted to an active call or IC50. Raw response curves were
    not independently refitted.
  snapshot_sha256: 57272ebf9e3fcbb57b7fb914252a8a7fb1ff6b1d44889f153af2779f94d2694f
- evidence_id: S130-E-AID624296
  kind: database
  reference: pubchem.aid:624296
  locator: Complete official description/protocol/comments; exact 19-row summary join
  accessed_at: '2026-10-21T17:23:22.322754Z'
  support: supports
  summary: MCF10a nuclear Hoechst DNA-content phenotype; Inconclusive, 0.0052 µM Potency.
    Geminin metadata does not establish a direct target. Generic Potency remains OTHER,
    and a number is not promoted to an active call or IC50. Raw response curves were
    not independently refitted.
  snapshot_sha256: 970f728b1c2e48d344d0a16976dc03b6f85699a416f0d5a6fd233db2c179ae56
- evidence_id: S130-E-AID624297
  kind: database
  reference: pubchem.aid:624297
  locator: Complete official description/protocol/comments; exact 19-row summary join
  accessed_at: '2026-10-21T17:23:22.560395Z'
  support: supports
  summary: SW480 nuclear Hoechst DNA-content phenotype; Inactive, 0.0058 µM Potency.
    Generic Potency remains OTHER, and a number is not promoted to an active call
    or IC50. Raw response curves were not independently refitted.
  snapshot_sha256: ecfb8c016075176a45303cdde22a638acbb0542ebf6e51cd7dc5e2411a435241
- evidence_id: S130-E-AID1963593
  kind: database
  reference: pubchem.aid:1963593
  locator: Complete official description/protocol/comments; exact 19-row summary join
  accessed_at: '2026-10-21T17:23:23.303596Z'
  support: supports
  summary: CHO-ADRB2 cellular cAMP/HTRF assay; Inconclusive, 13.6854 µM Potency, not
    a purified receptor-binding assay. Generic Potency remains OTHER, and a number
    is not promoted to an active call or IC50. Raw response curves were not independently
    refitted.
  snapshot_sha256: 555444c0d658dbeb651c69b7996d2e8b808afeb456eadcd2cd5244ffefdf3bd6
- evidence_id: S130-E-AID1346981
  kind: database
  reference: pubchem.aid:1346981
  locator: Complete official description/protocol/comments; exact 19-row summary join
  accessed_at: '2026-10-21T17:23:22.996319Z'
  support: supports
  summary: HepG2 CellTiter-Fluor viability counterscreen; Inconclusive, 24.3365 µM
    Potency, not a positive caspase-induction mechanism. Generic Potency remains OTHER,
    and a number is not promoted to an active call or IC50. Raw response curves were
    not independently refitted.
  snapshot_sha256: feee5aaacdf31b802a1bbd1f7e5fa34f0a806adb9700dae5325b7ce2e98995fd
- evidence_id: S130-E-AID1963588
  kind: database
  reference: pubchem.aid:1963588
  locator: Complete official description/protocol/comments; exact 19-row summary join
  accessed_at: '2026-10-21T17:23:23.125684Z'
  support: supports
  summary: CHO-CHRM1 cellular calcium-flux antagonist assay; Inconclusive, 3.7501
    µM Potency. Generic Potency remains OTHER, and a number is not promoted to an
    active call or IC50. Raw response curves were not independently refitted.
  snapshot_sha256: 2846206d562bbcc5332ced83cb48856daf32ce8f8b70c76ec450b32e46bc7363
- evidence_id: S130-E-AID1671199
  kind: database
  reference: pubchem.aid:1671199
  locator: Complete official description/protocol/comments; exact 19-row summary join
  accessed_at: '2026-10-21T17:28:09.671430Z'
  support: supports
  summary: CYP1A2 P450-Glo enzyme/proluciferin/NADPH luminescence assay; Inconclusive,
    35.5742 µM Potency. Generic Potency remains OTHER, and a number is not promoted
    to an active call or IC50. Raw response curves were not independently refitted.
  snapshot_sha256: e8d0505e1c889f7a4384be8894058ac66df3829fee36c6fb84145802bcf4d458
- evidence_id: S130-E-AID1671197
  kind: database
  reference: pubchem.aid:1671197
  locator: Complete official description/protocol/comments; exact 19-row summary join
  accessed_at: '2026-10-21T17:23:23.605158Z'
  support: supports
  summary: CYP2C19 P450-Glo enzyme/proluciferin/NADPH luminescence assay; Active,
    4.4785 µM Potency; source signal-interference caveat retained. Generic Potency
    remains OTHER, and a number is not promoted to an active call or IC50. Raw response
    curves were not independently refitted.
  snapshot_sha256: 7a9a5c613c48115f6ed5f30d9a22553f5bd3f73369b80da317c894db953828bd
- evidence_id: S130-E-AID1671198
  kind: database
  reference: pubchem.aid:1671198
  locator: Complete official description/protocol/comments; exact 19-row summary join
  accessed_at: '2026-10-21T17:23:23.682065Z'
  support: supports
  summary: CYP2C9 P450-Glo enzyme/proluciferin/NADPH luminescence assay; Inconclusive,
    31.7055 µM Potency. Generic Potency remains OTHER, and a number is not promoted
    to an active call or IC50. Raw response curves were not independently refitted.
  snapshot_sha256: 07d75e3d1f68c8c019dd18a721621f566b26e6524e12b9b083a7c7aaa3c86773
- evidence_id: S130-E-OTHERJOIN
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch013/bgc-science/other-assay-current-comparison.json
  locator: Exact nineteen non-PhoP AID/CID/SID/target/outcome/endpoint/value joins
  accessed_at: '2026-10-21T17:27:23.285504Z'
  support: supports
  summary: All nineteen written non-PhoP entries match one current source-summary
    row each. Call, endpoint and target-annotation variants remain separately represented;
    no mechanism is inferred from numeric agreement.
  snapshot_sha256: 6bc2debb5443d43e060472cdc34be5a03c16005ec58f6bfe1c2f945b1626f643
- evidence_id: S130-E-SAMPLES
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch013/bgc-science/assay-substance-addendum/source-notes.json
  locator: Exact deposited SID 144214022 and 49734345 JSON/SDF comparison, alongside
    PhoP SID 47193729
  accessed_at: '2026-10-21T17:31:51.892062Z'
  support: supports
  summary: All three deposited assay substances encode neutral RR chloramphenicol;
    the parent owner is stereo-unspecified. The independent chemistry finding owns
    that precision/migration issue. This science audit does not treat an unspecified
    CID join as sample-equivalence proof.
  snapshot_sha256: a4ebe10e71400d7bef2c6c36bc8e5058356e85628bd48dba7fbc505e826428a1
- evidence_id: S130-E-CONSUMERS
  kind: record_content
  reference: scripts/seed_from_sources.py
  locator: classify_activity lines 128–178; assay emission/cap/summary lines 1308–1380;
    actual exclusion helper
  accessed_at: '2026-10-21T18:02:41.988912Z'
  support: supports
  summary: The title pattern inhibitors? of adds ENZYME_INHIBITOR to all six Active
    PhoP observations. Their classes supply the written summary. The current classifier
    sees title/AID only; it has no complete-row-guarded class-only override. Existing
    bioassay exclusions remove entire observations and are not a class correction.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: S130-E-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/130/curation-search.json
  locator: Bounded ignored-inclusive exact-AID and class-override searches
  accessed_at: '2026-10-21T18:00:39.101502Z'
  support: context_only
  summary: No exact six-AID curation decision or matched class-withholding/override
    route was found in the scoped searches; actual consumed classifier/exclusion code
    was also read.
  snapshot_sha256: f848e4eef731861ace956d14dee7e6c3b8e1b5d8311c2672571f0c42a0d54ff4
  search_scope: rg --no-ignore --hidden exact six AIDs under curation; activity-class
    override/withholding patterns under src/scripts/curation/tests. Both searches
    exit 1; ignored files included. This is a bounded implementation observation,
    not an exhaustive semantic proof about every file.
- evidence_id: C130-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/chloramphenicol.yaml
  locator: Complete owner and all local-source rows; no referenced components
  accessed_at: '2026-10-21T18:04:04.111969Z'
  support: supports
  summary: The complete owner denotes chloramphenicol under naturalproductmech:mibig-d9dc3ff908.
    Its exact source selector is BGC0000893:1, version 5, with complete parsed raw-row
    SHA256 fcfd701588342825f9921ca6015d064e91d625dbdafed4672efb520dbfc55c78. The official
    intake and prepared owner bytes agree.
  snapshot_sha256: d1c483e457d58b0306462795af8f027a3ed4dd22d781ed6044b193151a83a793
- evidence_id: C130-GRAPH
  kind: validation
  reference: /private/tmp/npm-review-work/130/chemistry.json
  locator: Fresh intake RDKit result and frozen Standard/fixed-H comparison
  accessed_at: '2026-10-21T17:52:21.829037Z'
  support: supports
  summary: The stored SMILES recomputes to WIIZWVCIJKGZOK-UHFFFAOYSA-N, formula C11H12Cl2N2O5,
    formal charge 0; stored InChI/key agree. These are representation checks, not
    experimental identity proof.
  snapshot_sha256: 36fb4c719e98bffc1af54240ab421ddd3f5e8ccdc1430f9df598325c7288b5a0
- evidence_id: C130-COMPARISON
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch013/chemistry-prep/chemical-comparison.json
  locator: Record 130; exact source rows and each graph comparison
  accessed_at: '2026-10-21T17:23:24.463910Z'
  support: supports
  summary: Exact Standard, fixed-H, formula, charge and stereo comparisons of the
    retained owner, complete raw rows and current authority responses; primary experimental
    proof is assessed separately.
  snapshot_sha256: 503b2ba573d5eef465b41aa483433a9b2b92cce169c7270520b63466b4f5539f
- evidence_id: C130-LOCAL-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/130/chemistry-search-receipt.json
  locator: Exact full key, label, slug and source selector in raw/owner/curation trees
  accessed_at: '2026-10-21T18:04:04.200352Z'
  support: supports
  summary: Ignored-inclusive bounded search preserves all matching paths; an absent
    curation decision does not imply a missing scientific source.
  snapshot_sha256: 34dfaba92b23daf1e5f623a1f5a561f007d53e0a3cf68f7401f3bac1d8be945c
  search_scope: rg --no-ignore --hidden; data/natural_products, data/raw and curation;
    exact full key, current label, slug and BGC:compound_index. No claim beyond these
    trees.
- evidence_id: C130-CHEBI-SEARCH-1
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=WIIZWVCIJKGZOK-UHFFFAOYSA-N&size=100
  locator: Literal key search; chebi-key-chloramphenicol.json
  accessed_at: '2026-10-21T17:19:52.335758Z'
  support: supports
  summary: 1 returned name/key results; evaluate exact key and stars, not name similarity.
  snapshot_sha256: 860252728a7041aed4c50382de0c5f16f7da12cd529928378e8e19821dbb7e57
  search_scope: Official ChEBI es_search bounded key request, size=100, exact URL
    retained. This is not a universal absence claim.
- evidence_id: C130-CHEBI-SEARCH-2
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=chloramphenicol&size=100
  locator: Literal name search; chebi-name-chloramphenicol.json
  accessed_at: '2026-10-21T17:19:53.005610Z'
  support: supports
  summary: 10 returned name/key results; evaluate exact key and stars, not name similarity.
  snapshot_sha256: 1f944b96423aeb2fa8d7af6b8193bdf0b520ad2cf01e345f4e45e1e96dd687ea
  search_scope: Official ChEBI es_search bounded name request, size=100, exact URL
    retained. This is not a universal absence claim.
- evidence_id: C130-AUTH-1
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000893.5/annotations.json
  locator: compounds[].structure; BGC0000893.5.json
  accessed_at: '2026-10-21T17:19:51.676012Z'
  support: supports
  summary: 'current MIBiG BGC0000893:1: parsed key WIIZWVCIJKGZOK-UHFFFAOYSA-N; exact
    stored Standard key match=True, fixed-H match=True. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: 600fe16513b2333af6b07391492a0c50e872dba0a11e78c8a520387461c7448f
- evidence_id: C130-AUTH-2
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/WIIZWVCIJKGZOK-UHFFFAOYSA-N/property/MolecularFormula,InChI,InChIKey,CanonicalSMILES,IsomericSMILES,Charge/JSON
  locator: PropertyTable.Properties[].SMILES; pubchem-key-chloramphenicol.json
  accessed_at: '2026-10-21T17:19:52.520575Z'
  support: supports
  summary: 'PubChem 298: parsed key WIIZWVCIJKGZOK-UHFFFAOYSA-N; exact stored Standard
    key match=True, fixed-H match=True. This current database representation is not
    independent primary experimental proof.'
  snapshot_sha256: 35e84c0b282878d2550f37c5e3cd2a25430ea86bbff9c09b6e67e4f2c30215f1
- evidence_id: C130-AUTH-3
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/chloramphenicol/property/MolecularFormula,InChI,InChIKey,CanonicalSMILES,IsomericSMILES,Charge/JSON
  locator: PropertyTable.Properties[].SMILES; pubchem-name-chloramphenicol.json
  accessed_at: '2026-10-21T17:19:52.871346Z'
  support: context_only
  summary: 'PubChem 5959: parsed key WIIZWVCIJKGZOK-RKDXNWHRSA-N; exact stored Standard
    key match=False, fixed-H match=False. This current database representation is
    not independent primary experimental proof.'
  snapshot_sha256: ff2595ca48c874fbb6eb706757adcaac8ad313054b8f7f7f824b47096b8f5d4e
- evidence_id: C130-AUTH-4
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/5959/property/MolecularFormula,InChI,InChIKey,CanonicalSMILES,IsomericSMILES,Charge/JSON
  locator: PropertyTable.Properties[].SMILES; pubchem-5959.json
  accessed_at: '2026-10-21T17:19:52.026688Z'
  support: context_only
  summary: 'PubChem 5959: parsed key WIIZWVCIJKGZOK-RKDXNWHRSA-N; exact stored Standard
    key match=False, fixed-H match=False. This current database representation is
    not independent primary experimental proof.'
  snapshot_sha256: ff2595ca48c874fbb6eb706757adcaac8ad313054b8f7f7f824b47096b8f5d4e
- evidence_id: C130-AUTH-5
  kind: authority
  reference: https://www.npatlas.org/api/v1/compound/NPA016373
  locator: smiles; NPA016373.json
  accessed_at: '2026-10-21T17:20:25.809647Z'
  support: supports
  summary: 'NPAtlas literal NPA016373: parsed key WIIZWVCIJKGZOK-UHFFFAOYSA-N; exact
    stored Standard key match=True, fixed-H match=True. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: 61562eee081fd42113cda23e1f4a2b581c0d4fdd746cd6793ad66a5b650da862
- evidence_id: C130-AUTH-6
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/94390/
  locator: default_structure.smiles; CHEBI94390.json
  accessed_at: '2026-10-21T17:20:10.196661Z'
  support: supports
  summary: 'ChEBI JSON 94390: parsed key WIIZWVCIJKGZOK-UHFFFAOYSA-N; exact stored
    Standard key match=True, fixed-H match=True. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: 7dc5314f653bcf559b6bbc5ee3f42a79355d01841b533a9f090bda894df4c1d0
- evidence_id: C130-AUTH-7
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/94390/
  locator: official molfile endpoint; CHEBI94390-official.mol
  accessed_at: '2026-10-21T17:20:35.381544Z'
  support: supports
  summary: 'ChEBI MOL 94390: parsed key WIIZWVCIJKGZOK-UHFFFAOYSA-N; exact stored
    Standard key match=True, fixed-H match=True. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: 3ffdd9df502bbb92d2bc32bd6920fac85f16bcaeb1032021b60e176a820e4ff1
- evidence_id: C130-AUTH-8
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/17698/
  locator: default_structure.smiles; CHEBI17698.json
  accessed_at: '2026-10-21T17:20:08.929239Z'
  support: context_only
  summary: 'ChEBI JSON 17698: parsed key WIIZWVCIJKGZOK-RKDXNWHRSA-N; exact stored
    Standard key match=False, fixed-H match=False. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: d88f4415ca57051bf135248e1ecea5c5e9b43ec53a872429e0614ca12fc6a4b5
- evidence_id: C130-AUTH-9
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/17698/
  locator: official molfile endpoint; CHEBI17698-official.mol
  accessed_at: '2026-10-21T17:20:34.162268Z'
  support: context_only
  summary: 'ChEBI MOL 17698: parsed key WIIZWVCIJKGZOK-RKDXNWHRSA-N; exact stored
    Standard key match=False, fixed-H match=False. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: 0f79c2787c4764e3caa62ed5e263938e3fe2fc50778498a4796d8b1de0281c83
- evidence_id: C130-AUTH-10
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/47325/
  locator: default_structure.smiles; CHEBI47325.json
  accessed_at: '2026-10-21T17:20:09.625092Z'
  support: context_only
  summary: 'ChEBI JSON 47325: parsed key BFLNGKUCFYKCFZ-RKDXNWHRSA-N; exact stored
    Standard key match=False, fixed-H match=False. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: 357337f8b8a4a52584899d1dfc0fb2760df7db2c80864048e36724c3b8a87db6
- evidence_id: C130-AUTH-11
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/47325/
  locator: official molfile endpoint; CHEBI47325-official.mol
  accessed_at: '2026-10-21T17:20:34.788260Z'
  support: context_only
  summary: 'ChEBI MOL 47325: parsed key BFLNGKUCFYKCFZ-RKDXNWHRSA-N; exact stored
    Standard key match=False, fixed-H match=False. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: 75251928f9deb985ca70091ae804d5c317dbfc81fc66fa9cd26f6a4f7a42f7aa
- evidence_id: C130-AUTH-12
  kind: authority
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q27166237.json
  locator: P233; Q27166237.json
  accessed_at: '2026-10-21T17:19:53.053746Z'
  support: supports
  summary: 'Wikidata Q27166237: parsed key WIIZWVCIJKGZOK-UHFFFAOYSA-N; exact stored
    Standard key match=True, fixed-H match=True. This current database representation
    is not independent primary experimental proof. Canonical P233 is not an isomeric
    stereo assertion; compare P2017 when present.'
  snapshot_sha256: 5bcb8511656d331f19db9d8935e4d41d03ead5a07ff668bc5cdec00b2d8ab05f
- evidence_id: C130-AUTH-13
  kind: authority
  reference: https://www.chemspider.com/Chemical-Structure.5744.html
  locator: JSON-LD InChI; chemspider5744.html
  accessed_at: '2026-10-21T17:19:54.295795Z'
  support: context_only
  summary: 'ChemSpider raw-only5744: parsed key WIIZWVCIJKGZOK-RKDXNWHRSA-N; exact
    stored Standard key match=False, fixed-H match=False. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: 593efed88edf90f64411b64793adedc871e432a5569ecffc58624076e85629ce
- evidence_id: C130-SAMPLE-IDENTITY
  kind: validation
  reference: /private/tmp/npm-review-work/130/current-sample-identity.json
  locator: Independent parsing of three deposited SDFs and exact current raw-row inventory
  accessed_at: '2026-10-21T18:03:01.626204Z'
  support: supports
  summary: SID47193729, SID144214022 and SID49734345 each encode neutral RR chloramphenicol,
    WIIZWVCIJKGZOK-RKDXNWHRSA-N. They cover the 25 written observations across 17
    unique AIDs. The owner retains two undefined centres. All191 same-old-key raw
    rows carry CID5959;166 are omitted from the current rendering and were not all
    independently endpoint-audited. Eight written AIDs have multiple target-accession
    rows per old-key/CID/AID.
  snapshot_sha256: a6902a78f242451e198c4f71a59253a6a6d2b86b99441834205554981a3e4d94
- evidence_id: C130-PHOP-SID
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/47193729/JSON
  locator: Literal deposited substance and CID association for the six PhoP rows
  accessed_at: '2026-10-21T17:24:35.690058Z'
  support: supports
  summary: The deposited substance is RR and associates with CID5959. Its exact tested-substance
    identity is narrower than the unresolved parent graph; protocol-specific activity
    interpretation remains in the science section.
  snapshot_sha256: 63e7cb7b4609f6f3f7e5e44910c5d8bd0bdcd9a1ab60dcaba85066b336428158
- evidence_id: C130-SID-144214022
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/144214022/JSON
  locator: Literal substance identifier, deposited graph and CID5959 association
  accessed_at: '2026-10-21T17:30:58.112573Z'
  support: supports
  summary: The official deposited JSON and independently parsed SDF retain RR chloramphenicol,
    not the stereo-unspecified parent. This is a database sample declaration, not
    a fresh lot-purity or natural absolute-hand experiment.
  snapshot_sha256: 7fb4604208b295c588c291d017c9546987a6cd44a879de51e1d9ac5699769b56
- evidence_id: C130-SID-49734345
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/49734345/JSON
  locator: Literal substance identifier, deposited graph and CID5959 association
  accessed_at: '2026-10-21T17:30:58.118239Z'
  support: supports
  summary: The official deposited JSON and independently parsed SDF retain RR chloramphenicol,
    not the stereo-unspecified parent. This is a database sample declaration, not
    a fresh lot-purity or natural absolute-hand experiment.
  snapshot_sha256: 56c5b5929976afbaa9a680116000766cdb5e843a6ca89b6dbad9ce5230d40caa
- evidence_id: C130-EXTRACTOR
  kind: record_content
  reference: scripts/extract_pubchem_bioassay.py
  locator: Inspected maintained identity and projection contract
  accessed_at: '2026-10-21T18:04:04.111969Z'
  support: supports
  summary: cid_to_key derives CID mapping from corpus xrefs without independently
    checking the CID graph; rows_from_summary copies that supplied owner key into
    each assay row. Thus the current exact-key label is not an independent test-sample
    identity determination.
  snapshot_sha256: 24f9d794e7cf97c420351cb751f8767f7d81a5f22aed01669b2318d6755e7c00
- evidence_id: C130-SEED
  kind: record_content
  reference: scripts/seed_from_sources.py
  locator: Inspected maintained identity and projection contract
  accessed_at: '2026-10-21T18:04:04.111969Z'
  support: supports
  summary: Assays join on the stored full key and are capped after sorting. Removing
    a subset can expose previously omitted rows. Curator pathway/graph fields are
    carried only when the owner full key is unchanged; identity replacement requires
    explicit migration.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: C130-EXCLUSIONS
  kind: record_content
  reference: src/naturalproductmech/curate/bioassay_exclusions.py
  locator: Inspected maintained identity and projection contract
  accessed_at: '2026-10-21T18:04:04.111969Z'
  support: supports
  summary: Existing exclusions require exactly one complete old-key/CID/AID row and
    withhold entire observations. They cannot qualify a tested stereoisomer, rewrite
    keys, edit class only or select among duplicate target-accession rows.
  snapshot_sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
- evidence_id: C130-XREF-CONTRACT
  kind: record_content
  reference: src/naturalproductmech/curate/xref_exclusions.py
  locator: Inspected maintained identity and projection contract
  accessed_at: '2026-10-21T18:04:04.111969Z'
  support: supports
  summary: The existing seven-field literal-xref exclusion pins the complete original
    MIBiG row and retains source assertion in a discussion. It cannot repair already
    persisted assay joins or add a replacement CID.
  snapshot_sha256: 17c3d9e7794bae596b22cf19a2dd5bc2169475d6fea81ea4e6f1781a53af9157
- evidence_id: C130-STRUCTURE-CONTRACT
  kind: record_content
  reference: src/naturalproductmech/curate/structure_corrections.py
  locator: Inspected maintained identity and projection contract
  accessed_at: '2026-10-21T18:04:04.111969Z'
  support: supports
  summary: Structure replacement requires a unique eligible three-star target, full
    source/target pins, collision checks and separate old-key joins; it is not automatic
    assay or curator-owned graph migration.
  snapshot_sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
assessments:
- assessment_id: R130-HISTORY
  area: provenance
  topic: Native status and complete retained audit history
  outcome: supported
  summary: The six retained events comprise four source-seeding events and two 2026-10-01
    RECORD_CURATED events adding the CmlI step/graph and correcting citation-title
    capitalization. The owner still has SEEDED status. These history events are provenance
    claims, not an earlier structured-review pass; their mechanism content is assessed
    separately.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - R130-OWNER
- assessment_id: R130-OPTIONAL
  area: completeness
  topic: Present optional assertions and enrichment scope
  outcome: supported
  summary: The complete one-step CmlI pathway, one BIOSYNTHESIS graph with three nodes
    and two edges, all25 written assay observations and ENZYME_INHIBITOR summary are
    present. Their identity, protein grounding, claim-level primary evidence and assay
    interpretation require the separate chemical and scientific assessments. The explicit
    graph/owner stereochemical distinction is preserved. No optional assertion is
    silently omitted from the audit.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - R130-OWNER
  - R130-LOCAL
- assessment_id: R130-FILING
  area: representation
  topic: Exact-key computed classification provenance
  outcome: supported
  summary: The owner reproduces its exact-key NPClassifier result and version npclassifier.gnps2.org@2026-09-07,
    including Alkaloids filing, superclass/class labels and glycoside prediction false.
    Computed labels are not independent evidence for precursor use or natural origin.
    Any corrected chemical identity must be reclassified against its corrected effective
    key.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - R130-OWNER
  - R130-LOCAL
- assessment_id: R130-ORGANISM-IDS
  area: grounding
  topic: Literal organism identifier routing
  outcome: supported
  summary: The literal source identifiers and names resolve consistently. Their experimental
    occurrence and stock claims remain separately assessed.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - R130-Q7623398
- assessment_id: R130-TAXON-SCOPE
  area: provenance
  topic: Taxonomic synonym and experimental-stock boundaries
  outcome: supported
  summary: NCBI strain 953739 S. venezuelae ATCC10712 explicitly lists ISP5230 as
    a synonym; its species parent is 54571. This supports the exact native CmlI stock
    bridge. It does not equate recombinant E. coli protein production, S. coelicolor
    whole-cluster expression or Salmonella bioassays with native production.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - R130-TAXON-CONTEXT
  - R130-OWNER
- assessment_id: R130-IMODULON-SCOPE
  area: completeness
  topic: Native producer and experimental-host transcriptomic applicability
  outcome: not_applicable
  summary: S. venezuelae ATCC10712/ISP5230 is absent. S. coelicolor, E. coli and S.
    enterica catalogue entries are not automatic matches to the engineered M1152 cluster
    host, recombinant BL21 enzyme construct, or specific PhoP reporter strains and
    conditions. No module assignment is made.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - R130-OWNER
  - R130-IMODULON
- assessment_id: S130-A-PRODUCER
  area: evidence
  topic: biosynthesis_origin and producer_organisms[0]
  outcome: supported
  summary: Named chloramphenicol has positive native S. venezuelae biosynthetic evidence,
    including the native overexpression result and the original abstract reporting
    mutant genetics. The 2014 WT negative is limited to tested conditions. Preserve
    the distinction between native ATCC 10712, its engineered M1582 derivative, heterologous
    M1152 hosts and recombinant E. coli. Exact stereo transfer to the parent is independently
    adjudicated by chemistry.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - S130-E-LOCAL
  - S130-E-2014
  - S130-E-2012
  - S130-E-GAP
  - S130-E-2001ABSTRACT
  dimensions:
  - name: native_experiment
    value: ATCC 10712 M1582, cmlR/sven0913 overexpression
    definition: Native background engineered for detectable product; conditional WT
      silence is not general incapacity.
    evidence_ids:
    - S130-E-2014
  - name: heterologous_experiment
    value: S. coelicolor M1152/pAH91 and deletion/rescue derivatives
    definition: These are whole-cluster host experiments, not native ATCC 10712 deletions.
    evidence_ids:
    - S130-E-2014
    - S130-E-2014SI
- assessment_id: S130-A-LOCUS
  area: evidence
  topic: biosynthetic_gene_clusters[0] methods, grades, accession and source citation
  outcome: supported
  summary: The four method categories have support across the original native-genetic
    abstract, 2014 heterologous deletion/rescue and expression/product study, and
    2012/2017 enzyme studies. Retain strong locus support with each experiment correctly
    routed. The sole imported 2001 citation does not by itself document all later
    experiments; detailed original 2001 scope remains unavailable. The sequence window
    contains native CmlI, but its complete outer boundaries are not independently
    proven by a single CDS match.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - S130-E-LOCAL
  - S130-E-GAP
  - S130-E-2014
  - S130-E-2014SI
  - S130-E-2012
  - S130-E-2017
  - S130-E-NATIVE
  - S130-E-2001ABSTRACT
  dimensions:
  - name: evidence_tier
    value: Strong locus support with experiment-specific host scope
    definition: Do not equate a heterologous knockout with a native knockout or a
      fed single enzyme with whole-cluster sufficiency.
    evidence_ids:
    - S130-E-2014
    - S130-E-2012
    - S130-E-GAP
- assessment_id: S130-A-PATHWAY
  area: evidence
  topic: biosynthetic_pathway[0], including all five evidence entries
  outcome: supported
  summary: The terminal CmlI arylamine-to-nitro transformation is directly supported
    by the 2012 reconstitution and 2017 kinetic study. Both snippets are exact contiguous
    title text. The step already correctly states that substrate/product CHEBI:47325/17698
    are the exact stereochemical reaction and the parent remains incomplete. Native
    F2RB83 matches the genomic CDS; protein evidence uses a His6 construct, not an
    untagged native assay. Current UniProt supports the Rhea equation, while the independent
    live Rhea endpoint is unavailable.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - S130-E-2012
  - S130-E-2017
  - S130-E-2017SI
  - S130-E-UNIPROT
  - S130-E-NATIVE
  - S130-E-SEQUENCE
  - S130-E-GAP
  dimensions:
  - name: native_reference
    value: F2RB83 / CCA54211.1, full 339 residues
    definition: Exact native sequence agreement does not reconstruct the full tagged
      construct.
    evidence_ids:
    - S130-E-UNIPROT
    - S130-E-SEQUENCE
  - name: assay_construct
    value: N-terminal His6-CmlI expressed in BL21(DE3)
    definition: Complete tag/junction equality was not established.
    evidence_ids:
    - S130-E-2012
    - S130-E-2017SI
- assessment_id: S130-A-GRAPH
  area: evidence
  topic: causal_graphs[0].nodes[0..2] and edges[0..1]
  outcome: supported
  summary: 'Both edges—NH2-CAM N-oxygenation by CmlI and CmlI formation of chloramphenicol—have
    direct primary biochemical support. The graph explicitly qualifies exact ChEBI
    stereo versus the owner. Retention wording is appropriately supported rather than
    absolute: no zero-exchange or all-constants-directly-measured claim is introduced.
    The three-node graph need not enumerate every mechanistic intermediate to remain
    valid.'
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - S130-E-2012
  - S130-E-2017
  - S130-E-UNIPROT
  - S130-E-SEQUENCE
- assessment_id: S130-A-OCCURRENCE
  area: evidence
  topic: occurrences[0]
  outcome: unknown
  summary: The historical 1949 S. venezuelae LOTUS occurrence remains a source assertion.
    Later native biosynthesis supports the named natural product but does not substitute
    for the unavailable exact original chemical-studies IV isolation scope. No occurrence
    deletion is justified solely by that access gap.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - S130-E-LOCAL
  - S130-E-GAP
  - S130-E-2014
- assessment_id: S130-A-PHOP
  area: evidence
  topic: bioactivities[4], [7], [10], [11], [12], [13] and bioactivity_summary
  outcome: concern
  summary: The six Active IC50 calls and values match current original depositions,
    but their ENZYME_INHIBITOR labels are unsupported. They measure virK-GFP expression
    or nmpC-GFP culture growth; positive counterscreens limit selective PhoP interpretation.
    Keep the data and assay context without claiming direct enzyme inhibition, direct
    binding or demonstrated fluorescence artefact.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - S130-E-PROJECTION
  - S130-E-PHOP2401
  - S130-E-PHOP2384
  - S130-E-PHOP1985
  - S130-E-PHOP1981
  - S130-E-PHOP1863
  - S130-E-PHOP1850
  - S130-E-PHOPJOIN
  - S130-E-CONSUMERS
  dimensions:
  - name: assay_scope
    value: Cellular reporter and culture-growth responses
    definition: Not purified PhoP/PhoQ activity or a validated selective molecular
      target.
    evidence_ids:
    - S130-E-PHOP2401
    - S130-E-PHOP1985
    - S130-E-PHOP1863
- assessment_id: S130-A-HTR
  area: evidence
  topic: bioactivities[0..3]
  outcome: supported
  summary: Both duplicated source-target variants retain the same HTR2A agonist Inactive
    and antagonist Inconclusive calls, generic Potency and µM values. These are CHO-cell
    calcium responses, not direct receptor binding or positive clinical agonism.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - S130-E-AID1963587
  - S130-E-AID1963586
  - S130-E-OTHERJOIN
  - S130-E-PROJECTION
- assessment_id: S130-A-DYT
  area: evidence
  topic: bioactivities[5..6] and target_enzyme O14656
  outcome: supported
  summary: The Inconclusive phenotype call and Potency are faithfully represented.
    O14656 identifies the deposited torsin target context; the actual screening construct
    is EGFP-hTOR1A-delE with a WT comparator. It is not evidence of direct purified
    native torsin inhibition, and no positive activity class is asserted.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - S130-E-AID1645839
  - S130-E-OTHERJOIN
- assessment_id: S130-A-DNA
  area: evidence
  topic: bioactivities[8..9]
  outcome: supported
  summary: MCF10a Inconclusive and SW480 Inactive calls remain distinct, despite small
    fitted Potency values. Nuclear DNA-content imaging does not prove direct geminin
    inhibition; leaving the non-UniProt accession ungrounded is faithful.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - S130-E-AID624296
  - S130-E-AID624297
  - S130-E-OTHERJOIN
- assessment_id: S130-A-OTHER-CELLS
  area: evidence
  topic: bioactivities[14..18]
  outcome: supported
  summary: ADRB2, HepG2 viability and CHRM1 rows retain Inconclusive calls and exact
    generic Potency values. Their cellular cAMP, viability and calcium readouts are
    not silently converted to direct receptor binding or a positive caspase mechanism.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - S130-E-AID1963593
  - S130-E-AID1346981
  - S130-E-AID1963588
  - S130-E-OTHERJOIN
- assessment_id: S130-A-CYP
  area: evidence
  topic: bioactivities[19..24]
  outcome: supported
  summary: CYP2C19 is Active while CYP1A2/CYP2C9 are Inconclusive. The enzyme/proluciferin/NADPH
    assays differ from the PhoP cellular reporters; general luminescence-interference
    warnings do not by themselves prove sample interference. Retain exact generic
    Potency labels/values and refrain from converting them to IC50 or applying the
    positive call to all CYPs.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - S130-E-AID1671199
  - S130-E-AID1671197
  - S130-E-AID1671198
  - S130-E-OTHERJOIN
- assessment_id: S130-A-INVENTORY
  area: representation
  topic: All 25 written assays, the omitted-count note and raw source extent
  outcome: supported
  summary: The deterministic first-25 projection and 166 omitted count reproduce all
    191 matching raw rows. This audit scientifically scopes every written observation;
    it does not certify all omitted assay protocols. Exact RR deposited samples require
    the separate identity action before any old-key migration, regardless of numerical
    source agreement.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - S130-E-PROJECTION
  - S130-E-OTHERJOIN
  - S130-E-PHOPJOIN
  - S130-E-SAMPLES
- assessment_id: C130-A-IDENTITY
  area: identity
  topic: Stored representation and source-concept provenance
  outcome: supported
  summary: The complete source row BGC0000893:1 and source-concept hash reproduce
    this stored representation; this does not establish that the upstream compound
    label is correct. Formula, charge, Standard and fixed-H distinctions are independently
    recorded. Primary support and any conflicting exact xref are assessed separately.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - C130-OWNER
  - C130-GRAPH
  - C130-COMPARISON
  dimensions:
  - name: mibig_source_selector
    value: BGC0000893:1
    definition: Accession plus compound_index, distinct from the entry-level accession.
    evidence_ids:
    - C130-OWNER
  - name: complete_raw_row_sha256
    value: fcfd701588342825f9921ca6015d064e91d625dbdafed4672efb520dbfc55c78
    definition: Sorted compact ASCII JSON of every parsed TSV field, including empty
      values.
    evidence_ids:
    - C130-OWNER
- assessment_id: C130-A-GROUNDING
  area: provenance
  topic: Exact authority eligibility and source representation
  outcome: supported
  summary: No exact eligible row exists in the committed ChEBI projection for this
    owner. Current bounded name/key searches do not justify a different congener or
    a two-star grounding.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - C130-OWNER
  - C130-COMPARISON
  - C130-LOCAL-SEARCH
  - C130-CHEBI-SEARCH-1
  - C130-CHEBI-SEARCH-2
- assessment_id: C130-A-PARENT
  area: representation
  topic: Intentionally unspecified parent and exact pathway endpoint
  outcome: supported
  summary: The owner explicitly records the difference between the parent and exact
    RR pathway endpoint, including its curation history. This truthful boundary must
    survive any later identity adjudication; it does not qualify unrelated unannotated
    exact xrefs or assay samples.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - C130-OWNER
  - C130-COMPARISON
- assessment_id: C130-A-SAMPLE
  area: grounding
  topic: Assayed RR sample versus unresolved parent precision
  outcome: concern
  summary: The literal CID and sample declarations are narrower at both centres. This
    is a precision mismatch, not a different constitution or proof that other stereoisomers
    share the reported activities. All25 observations remain deposited measurements/calls
    with their original outcomes; the separate PhoP classifier finding is owned by
    science.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  evidence_ids:
  - C130-SAMPLE-IDENTITY
  - C130-PHOP-SID
  - C130-SID-144214022
  - C130-SID-49734345
  - C130-COMPARISON
findings:
- finding_id: S130-F-PHOP
  issue_key: pubchem-phop-cellular-reporter-enzyme-class
  category: evidence
  severity: major
  certainty: confirmed
  status: open
  title: Cellular PhoP reporter results are mislabeled as enzyme inhibition
  description: All six source protocols measure bacterial reporter fluorescence or
    culture-growth counterscreens. The generic title regex supplies ENZYME_INHIBITOR
    without direct enzyme evidence, and those labels supply the current summary. Positive
    counterscreens also preclude inferring selective PhoP inhibition. Calls/IC50 values
    remain valid deposited observations, subject to the independent sample-identity
    adjudication.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  field_paths:
  - bioactivities[4].activity_class
  - bioactivities[7].activity_class
  - bioactivities[10].activity_class
  - bioactivities[11].activity_class
  - bioactivities[12].activity_class
  - bioactivities[13].activity_class
  - bioactivity_summary
  evidence_ids:
  - S130-E-LOCAL
  - S130-E-PHOP2401
  - S130-E-PHOP2384
  - S130-E-PHOP1985
  - S130-E-PHOP1981
  - S130-E-PHOP1863
  - S130-E-PHOP1850
  - S130-E-PHOPJOIN
  - S130-E-CONSUMERS
  - S130-E-SEARCH
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Consumed title classifier, assay projection and summary computation
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/bioassay_exclusions.py
    role: Existing guarded whole-observation exclusion; not a class override
  - repository: CultureBotAI/NaturalProductMech
    path: curation/pubchem_bioassay_exclusions.tsv
    role: Existing exclusion contract only after separate identity adjudication
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/pubchem_bioassay.tsv
    role: Unchanged exact raw assay rows
  - repository: CultureBotAI/NaturalProductMech
    path: tests/test_bioassay_exclusions.py
    role: Existing guard tests; new class-only contract needs meaningful tests
- finding_id: C130-F-SAMPLE-PRECISION
  issue_key: chloramphenicol-unspecified-parent-rr-xref-assay-identity
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: RR PubChem and assay samples are attached as exact identity to an unspecified
    parent
  description: The literal PubChem5959 and three deposited substances behind all25
    written observations specify RR, whereas the owner deliberately leaves both centres
    undefined. The pathway already explains its separate RR endpoint, so that curated
    distinction is sound. The unqualified exact xref and assay association still lose
    the tested-sample precision and cannot establish activity of an unspecified stereochemical
    population.
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  field_paths:
  - xrefs
  - bioactivities
  - chemical_structure
  evidence_ids:
  - C130-OWNER
  - C130-COMPARISON
  - C130-SAMPLE-IDENTITY
  - C130-PHOP-SID
  - C130-SID-144214022
  - C130-SID-49734345
  - C130-EXTRACTOR
  - C130-EXCLUSIONS
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_xref_exclusions.tsv
    role: Withhold the literal PubChem exact-equivalence claim under a full raw guard
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_pubchem_bioassay.py
    role: Verify CID/sample structure before assigning a corpus full key and preserve
      source-specific identity
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/bioassay_exclusions.py
    role: Extend or add a separately guarded identity-qualification consumer where
      current selectors are nonunique
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Project tested-structure scope before the cap and preserve curated pathway
      ownership
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/pubchem_bioassay.tsv
    role: Retain historical rows and full-row audit pins; only manifested regeneration
      or guarded migration
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Use only if a separate complete RR owner migration is explicitly adjudicated
actions:
- action_id: S130-ACT-PHOP
  finding_ids:
  - S130-F-PHOP
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Consumed title classifier, assay projection and summary computation
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/bioassay_exclusions.py
    role: Existing guarded whole-observation exclusion; not a class override
  - repository: CultureBotAI/NaturalProductMech
    path: curation/pubchem_bioassay_exclusions.tsv
    role: Existing exclusion contract only after separate identity adjudication
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/pubchem_bioassay.tsv
    role: Unchanged exact raw assay rows
  - repository: CultureBotAI/NaturalProductMech
    path: tests/test_bioassay_exclusions.py
    role: Existing guard tests; new class-only contract needs meaningful tests
  generator: scripts/seed_from_sources.py
  description: 'Implement a tested class-withholding/context rule in the actual seeder/curate
    path for the exact six rows at old key WIIZWVCIJKGZOK-UHFFFAOYSA-N, CID 5959:
    [{"aid": "2401", "owner_index": 4, "row_sha256": "5dc176943d786873f8a46cbeaf653502b3f481c82455ae6a36d19521481805f0"},
    {"aid": "2384", "owner_index": 7, "row_sha256": "106c735adda7b7fbf5ac343138857b221c1db5e05675ada22a8cc80a2127c8fd"},
    {"aid": "1985", "owner_index": 10, "row_sha256": "f1cf5fc6a3eacab6a05cc14a851164c2a80d42ba713f2670cbf2f90024f6ddb9"},
    {"aid": "1981", "owner_index": 11, "row_sha256": "8c2ef02862f357b0f77c4e5d534241f30e389a0e14adc6760da4b1767e31127a"},
    {"aid": "1863", "owner_index": 12, "row_sha256": "16f2a0875255a5087de47f55c572e05efc8e27b373991c06793e748b8a56bc74"},
    {"aid": "1850", "owner_index": 13, "row_sha256": "bb20eadc0bb0639914a2b57ae6be990ee75f210f5e82ad71f08b93f34fecf9f8"}].
    A new typed rule should consume each complete source-row digest, exact AID/title/protocol
    snapshot, outcome and endpoint, and remove only the unsupported ENZYME_INHIBITOR
    assignment while preserving valid Active/IC50/µM observations wherever exact sample
    identity is accepted. Retain separate virK reporter versus first/modified nmpC
    growth-counter-screen context. The current classify_activity(title, aid) interface
    does not enforce those row guards; extend it or add an explicitly consumed guarded
    overlay. Existing bioassay_exclusions removes whole observations and is not a
    class-only repair. Coordinate with the separate RR-versus-unspecified identity
    migration; do not transfer old-key rows automatically.'
  acceptance_checks:
  - Reject stale, duplicate, missing or ambiguous row decisions; pin all fields rather
    than only title or AID.
  - Preserve six exact Active calls and unqualified IC50 values/units when the corresponding
    exact chemical identity is retained. Do not invent a direct target, selective
    PhoP mechanism or proven GFP quenching.
  - Recompute top-25 selection, omitted count and summary from accepted emitted observations.
    Removing these unsupported classes must not force deletion of independently supported
    enzyme evidence or add a replacement class without evidence.
  - Keep inactive/inconclusive generic Potency rows unchanged, preserve distinct target-annotation
    variants and the raw 191-row inventory.
  - Test class-only correction separately and in composition with exact-structure
    migration/exclusion; reject unreviewed old-key joins. Regenerate through maintained
    code, with no generated-YAML/raw hand edits or unused curation-table assumptions.
- action_id: C130-ACTION-IDENTITY-SCOPE
  finding_ids:
  - C130-F-SAMPLE-PRECISION
  target_ids:
  - naturalproductmech:mibig-d9dc3ff908
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_xref_exclusions.tsv
    role: Withhold the literal PubChem exact-equivalence claim under a full raw guard
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_pubchem_bioassay.py
    role: Verify CID/sample structure before assigning a corpus full key and preserve
      source-specific identity
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/bioassay_exclusions.py
    role: Extend or add a separately guarded identity-qualification consumer where
      current selectors are nonunique
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Project tested-structure scope before the cap and preserve curated pathway
      ownership
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/pubchem_bioassay.tsv
    role: Retain historical rows and full-row audit pins; only manifested regeneration
      or guarded migration
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Use only if a separate complete RR owner migration is explicitly adjudicated
  description: 'Keep the explicit unspecified-parent/RR-pathway distinction unless
    a separate complete natural-product identity adjudication justifies migration.
    For the retained parent, exclude only literal pubchem:5959 using source_id=BGC0000893:1,
    version5, expected_source_row_sha256=fcfd701588342825f9921ca6015d064e91d625dbdafed4672efb520dbfc55c78,
    exact old key=WIIZWVCIJKGZOK-UHFFFAOYSA-N, old SMILES=OCC(NC(=O)C(Cl)Cl)C(O)C1=CC=C(C=C1)N(=O)=O,
    database_ids=npatlas:NPA016373|pubchem:5959|chemspider:5744, actual curator/date
    and the stable PubChem reference. Preserve NPA016373 and the raw-only ChemSpider
    association; ChemSpider is not an emitted supported xref and the existing exclusion
    table does not accept that namespace. The xref exclusion alone cannot fix already
    persisted assays. Implement/test a source-identity qualification before assay
    exact-key joins and the25-item cap: retain tested RR key, CID5959, each actual
    SID/version and every complete source-row SHA in /130/current-sample-identity.json.
    Preserve all191 original rows and their191 full-row digests; distinguish the25
    verified rendered rows from166 omitted endpoint-unreviewed rows. Either attach
    explicit tested-RR scope through a new supported schema/consumer contract or withhold
    nonexact owner associations with retained provenance. Do not silently restamp
    all rows with RR or allow newly exposed unreviewed rows after a partial exclusion.
    Current exclusions require one old-key/CID/AID row; AIDs1645839,1671197,1671198,1671199,1963586,1963587,1963588,1963593
    each have target-accession variants, so add a reviewed complete-row/target selector
    or explicit grouped-pin contract rather than claiming the existing selector accepts
    them. Preserve Active/Inactive/Inconclusive mapping, numeric values, units and
    target annotations without deduplication by name. Compose the separate six-PhoP
    class-only repair with the final tested-identity decision. If a later approved
    natural RR replacement uses CHEBI:17698, pin its current full target row (85bbf640cd55be9647b8b85cfaacb9f009413e11e2ef99bd21576e3dc1e38a4b),
    independently verify the full graph and collision state, derive chemistry, and
    explicitly migrate/revalidate the curated CmlI pathway, graph, history and same-key-dependent
    discussions. The seeder refuses old-owner identity changes and does not carry
    curator-owned fields across changed keys. Do not move old LOTUS, classifier, sibling
    or assay claims by path continuity alone.'
  generator: Guarded literal-xref exclusion plus explicit CID/sample-identity ingestion
    and projection contract; optional whole-owner migration is separate.
  acceptance_checks:
  - Reject full raw-row drift, CID/SID/key mismatch, missing sample identity, ambiguous
    target selectors and duplicate decisions.
  - Demonstrate25 current observations map to17 AIDs and three RR substances; retain191raw/166omitted
    accounting and all original values/outcomes without claiming unseen endpoint review.
  - Verify identity qualification is applied before the rendering cap so withheld
    rows cannot expose unchecked exact associations.
  - Preserve the existing explicit parent/RR pathway caveat and all curated fields;
    any approved key migration must explicitly prove their new owner and preserve
    history.
  - Run targeted contract tests and documented extraction/seed canary/reproduction/QC
    after authorized implementation. This review executes none of those mutations
    or tests.
limitations:
- This is a claim-level review of present assertions and bounded source gaps, not
  an exhaustive search for every later paper or an obligation to add every optional
  mechanism.
- The 2001 biosynthetic main and 1949 occurrence main remain unavailable; source-faithful
  assertions are not rewritten from absence of access.
- Full tagged CmlI constructs and exact original protein-stock sequences were not
  reconstructed. Native CDS identity and assay provenance remain separate.
- The live Rhea endpoint failed; the present reaction has independent primary and
  current UniProt support.
- All written assay protocols/endpoints were scoped, but no original concentration-response
  refit, stock-purity test or scientific review of all 166 omitted observations was
  performed.
- Exact assay-sample stereochemistry and owner identity are handled by the separate
  chemistry finding; numerical agreement does not resolve that issue.
- Authority matches establish the representations actually returned at their retained
  access times; they are not independent experimental structure or absolute-hand determinations.
  Root and science sections separately assess organism, locus, classification and
  history claims.
- The deposited SDFs establish declared sample structures, not independently measured
  lot purity or a new natural absolute configuration.
- All25 rendered sample identities were covered; the166 omitted assay endpoints were
  not all scientifically re-reviewed. Their raw presence must not be treated as an
  exact-identity or mechanistic endorsement.
- The science packet owns assay endpoint fidelity, PhoP classification and CmlI experimental
  scope; those findings are not duplicated here.
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
