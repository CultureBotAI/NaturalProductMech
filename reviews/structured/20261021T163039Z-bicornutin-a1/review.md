# Bicornutin A1: measured leucine conflicts with the stored stereoisomer

- Review: 20261021T163039Z-bicornutin-a1
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T16:18:25.280834Z
- Finished UTC: 2026-10-21T16:30:39.262240Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The primary supporting data identify L-leucine in compound 1, but the stored graph encodes D-leucine at that unique residue. This confirmed identity blocker requires a guarded correction and explicit handling of unresolved arginine positions. Native and heterologous named-product evidence remain supported.

## Scope And Provenance

One complete generated owner and any referenced components, assessed claim by claim for exact identity, provenance, origin, producer and occurrence scope, biosynthesis, classification, optional content and audit history.

Selection: Campaign record 108, batch 011, selected in path order from the fresh-main authoritative validated catalogue and the separately validated targets in earlier batch commits (publication tracked separately). At selection, 154 of 3116 current records had campaign coverage and 2962 remained. The population search included ignored files. Exactly one target is assessed here.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1c2402097718c138b081e00943de8f04de0541cd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-8904b7e092 | data/natural_products/alkaloids/bicornutin-a1.yaml | generated | bicornutin A1 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | naturalproductmech:mibig-8904b7e092 | The documented target strict validator completed; scientific support is assessed separately. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-8904b7e092 | All 3,116 current record files agree with PATHS.tsv and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-8904b7e092 | All 3,116 current records passed the documented byte-reproduction gate against committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-8904b7e092 | The exhaustive review queue produced 8,928 diagnostic rows across 12 queues; this deterministic output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-8904b7e092 | The configured identifier-label gate passed using the existing ontology caches: 13,449 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,744 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate on the current main baseline | passed | True | naturalproductmech:mibig-8904b7e092 | The full documented just qc recipe passed on the unchanged main baseline during batch004. Test summary: 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). All configured lint, governance, documentation, provenance, source-queue, schema, rendering, reproduction, filing-integrity and reporting stages completed successfully. |
| Complete owner and referenced-component scope | passed | True | naturalproductmech:mibig-8904b7e092 | Full owner, exact matching intake source rows and the empty referenced-component set were read and checked against the actual intake. Fresh target strict validation is retained separately. |
| Exact named product heterologous experiment | passed | True | naturalproductmech:mibig-8904b7e092 | Original Figure S5 explicitly identifies both products and the expression/control conditions; no method withdrawal is warranted. |
| Detailed primary main and chemical assignment context | unavailable | True | naturalproductmech:mibig-8904b7e092 | Required full main remains unavailable. Positive SI scope is retained, while detailed assignment/construct interpretation cannot be represented as a complete paper read. |
| Exact stored graph versus current literal authority graphs | passed | True | naturalproductmech:mibig-8904b7e092 | Standard identity, formula and neutral charge agree; fixed-H tautomer differences are explicitly retained. |
| Exact primary residue-specific stereochemistry | failed | True | naturalproductmech:mibig-8904b7e092 | A1 atom-specific Leu R conflicts with the L-Leu measured from compound1. |
| Detailed full main assignment access | unavailable | True | naturalproductmech:mibig-8904b7e092 | Full main is required to resolve the remaining positional assignment and reporting context; detailed SI is positive but does not remove this limit. |

## Scientific And Domain Assessments

### Native status and retained audit history

provenance: supported. Targets: naturalproductmech:mibig-8904b7e092.

All retained events are dated SEEDED_FROM_SOURCES provenance. The owner remains SEEDED. No native scientific status or history changes result from this review.

### Present optional assertions and enrichment limits

completeness: not_applicable. Targets: naturalproductmech:mibig-8904b7e092.

The complete owner has no optional pathway, mechanism graph, molecular target, bioactivity, application, clinical status, cross-corpus relation or discussion. Optional enrichment is separate from correction of current claims.

### Computed filing and exact-key classification provenance

representation: supported. Targets: naturalproductmech:mibig-8904b7e092.

The current owner reproduces its exact-key NPClassifier result, including npclassifier.gnps2.org@2026-09-07, Alkaloids filing and all returned superclass/class labels. It preserves the false glycoside prediction. These predictions do not independently prove precursor use, natural origin or absolute stereochemistry. Any future identity correction requires classification against the corrected effective key.

### Literal organism-identifier routing

provenance: supported. Targets: naturalproductmech:mibig-8904b7e092.

All literal organism entities have matching scientific names; available P685 values agree. Primary occurrence and producer support are assessed independently.

### Producer and experimental-host transcriptomic applicability

completeness: not_applicable. Targets: naturalproductmech:mibig-8904b7e092.

The complete inspected catalogue has no exact Xenorhabdus budapestensis native-producer dataset. The native DSM16342 producer and engineered Escherichia coli DH10B expression host remain distinct; no exact experimental-host dataset or component membership was established. The catalogue result is not evidence against production.

### Named product, donor, locus and host scope

evidence: supported. Targets: naturalproductmech:mibig-8904b7e092.

The imported heterologous method and corresponding formal grades are supported by original SI. Native culture evidence supports biological origin and occurrence without inventing native genetic necessity. The exact retained stereoisomer is a separate chemical claim.

### Sole LOTUS occurrence and primary reference

evidence: supported. Targets: naturalproductmech:mibig-8904b7e092.

The DOI and PMID identify the same study. Native DSM16342 culture contains named bicornutin A1; positive occurrence should be preserved with strain and chemistry qualification. This does not add a species-wide biosynthesis claim.

### Exact constitution, microstate and stereochemical assignment

identity: concern. Targets: naturalproductmech:mibig-8904b7e092.

A1’s encoded Leu is the opposite stereoisomer to the directly measured single residue; the remaining positional Arg assignments are not independently certified.

### Current authority agreement and eligible identifier

grounding: supported. Targets: naturalproductmech:mibig-8904b7e092.

Current full-key authority matches are two-star ChEBI and exact PubChem. Minting rather than selecting an ineligible ChEBI is consistent with the present priority rules. Authority consensus does not override experimental conflict; Standard identity is distinguished from fixed-H tautomer identity.

## Findings

### S108-F-CONTEXT: Bicornutin A1 omits its supported strain and expression context

minor / open / confirmed; issue key: mibig-bgc0001135-compound1-native-strain-expression-context.

The native donor is specifically DSM16342; the demonstrated experiment uses fed E. coli DH10B with bicA and mtaA. The current generic species and bare method are faithful but omit useful non-blocking context. Preserve the correct method and source-tier producer; do not rename the native donor as the engineered host.

### C108-F-LEU: Bicornutin A1 encodes the opposite leucine stereoisomer

blocker / open / confirmed; issue key: bicornutin-a1-encoded-d-leucine-conflicts-primary-l-leucine.

The unique isobutyl-bearing peptide alpha carbon is R with an explicit N/carbonyl/side-chain/H priority sequence, representing D-Leu. Primary Table S8 directly identifies the single Leu in compound1 as L. This is a concrete stereoisomer conflict, not a general R=L shortcut or an inference from database voting. Other Arg centres remain separately unresolved.

## Recommended Actions And Acceptance Checks

### S108-ACT-CONTEXT

For BGC0001135:1, pin full raw-row SHA256 683877f8e52dc86ee4487134f4cfa53c6a39b98580ff343f4a1ce2d046bc8494, version5, taxon290110, accession JX424818.1, empty locus bounds, key YHRZRWLQHQGLJN-VMAPGKTHSA-N and old Heterologous expression. Use the consumed strain overlay to record DSM16342 with DOI:10.1021/ac300372p. Preserve native SOURCE_ASSERTION and heterologous CLUSTER_DEMONSTRATED. Add the two-plasmid DH10B/fed-amine context through a tested consumed source-context route or an interim explicitly qualified curator discussion. If the identity correction changes this source graph, first implement/test composition: current producer_strains rejects concurrent structure correction. Do not bypass that rejection, change raw rows, or treat partial JX424818.1 as a full expression construct.

- Require exactly one original source row and fail on every field drift, including empty bounds.
- Preserve both positive named-product occurrence and applicable heterologous method; no unsupported native knockout grade.
- Prove explicit composition with any identity correction and no silent loss of context/citations on regeneration.
- Regenerate and run documented strict, grounding, history and scientific review gates only in a separately authorized curation task.

### C108-ACT-LEU

Pin BGC0001135:1, complete raw-row SHA256 683877f8e52dc86ee4487134f4cfa53c6a39b98580ff343f4a1ce2d046bc8494, exact original key YHRZRWLQHQGLJN-VMAPGKTHSA-N, literal SMILES N[C@@H](CCCNC(N)=N)C(N[C@H](CC(C)C)C(N[C@@H](CCCNC(N)=N)C(N[C@@H](CCCNC(N)=N)C(N[C@H](CCCNC(N)=N)C(NCCCCN)=O)=O)=O)=O)=O, and full old chemical payload in exact-owner-claim-guards.json. Adjudicate the remaining positional Arg assignments from detailed primary evidence, then use an eligible exact corrected three-star authority if one becomes available; current CHEBI221898 is two-star and repeats the conflict. Otherwise implement/test an explicit curated-structure correction action that pins original and target MOL/SMILES, atom mapping, Standard and fixed-H identities, charge and supported stereo. At minimum the measured Leu must be S under the demonstrated neighbour ordering; do not invent Arg assignments or silently treat a partially qualified correction as a fully experimentally established graph. Explicitly migrate source-specific positive occurrence/locus/strain context to the corrected owner and audit old-key LOTUS/CheBI/PC associations; current same-key joins and reference/strain loaders do not compose automatically. Preserve A2 separately without copying this repair.

- Show the exact unique Leu atom mapping and CIP change R to S, unchanged constitution/charge/terminal putrescine, and independent target-graph recomputation.
- Reject every original-row or expected chemical field drift; no hand-edit of raw or generated YAML and no unsupported three-star claim.
- Document retained versus unresolved Arg stereochemistry and do not infer stereowedges from COSY-bold bonds.
- Test migration, old-key cleanup and explicit composition with native-strain/reference/context changes; no lost positive product evidence or accidental A2 edit.
- Regenerate and run all documented gates in separately authorized curation; the present action does not claim that the missing explicit-graph consumer already exists.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R108-OWNER | data/natural_products/alkaloids/bicornutin-a1.yaml; Complete owner, all assertions, inline graph, discussions and history | supports | Root read the entire bicornutin A1 owner following its official intake and rechecked the source-preparation bytes against this base. It has 1 occurrence, 1 producer and 1 cluster assertions. The referenced component set is empty. Present optional fields: none. |
| R108-LOCAL | /private/tmp/npm-review-work/108/local-sources.json; Complete resolved owner and all exact matching local source rows | context_only | Root read the complete resolved owner and every matching MIBiG, LOTUS, ChEBI, CyanoMetDB and NPClassifier row captured by intake. This is a source-fidelity assessment, separate from independent experimental support. |
| R108-Q26307569 | https://www.wikidata.org/wiki/Q26307569; Literal entity and all nondeprecated P225/P685 values | context_only | Literal Q26307569 resolves to P225 Xenorhabdus budapestensis. P685 290110 matches the local taxon identifiers. This checks identifier routing only, not occurrence, native production or experimental-stock identity. |
| R108-IMODULON | https://imodulondb.org/api/datasets; Complete official 20-organism/28-dataset catalogue | context_only | The complete API catalogue retrieved at this timestamp matches the retained catalogue bytes. This evidence concerns catalogue membership only. The earlier adapter catalogue retains its original 2026-10-21T07:21:15.957321Z completion time in the separately pinned source packet. |
| R108-IMODULON-CONTEXT | /private/tmp/npm-review-work/shared-next-batch011/imodulon-context/source-notes.json; Prepared source packet: candidate_context, actual_accesses, metadata and the fully verified 53-input manifest | context_only | The packet records the three official /meta responses and six scoped adapter queries with their individual original 2026-10-21T15:57–15:58Z access times. Its preparation/read-completion timestamp is used here, not presented as a new API retrieval. Exact species, stock, gene-search and component limits remain explicit; no chemical identity, production, native stock equivalence or module membership is inferred. |
| S108-E-LOCAL | /private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/bicornutin-a1.yaml; Entire owner, exact source row and resolved content | supports | Bicornutin A1, BGC0001135:1, full source-row SHA256 683877f8e52dc86ee4487134f4cfa53c6a39b98580ff343f4a1ce2d046bc8494, has Heterologous expression, SOURCE_ASSERTION producer and CLUSTER_DEMONSTRATED locus. Its sole LOTUS occurrence is the same study by DOI; no explicit pathway/protein graph is present. |
| S108-E-SI | https://ndownloader.figshare.com/files/4137001; Tables S2/S4; Figures S2/S3/S5, pages 1–6 and 13–17 | supports | Native X. budapestensis DSM16342 material contains named compound 1. Table S2 exact mass/isotope-feeding and fragmentation distinguish A1 putrescine from A2 phenethylamine. Figure S5 compares E. coli DH10B control with DH10B carrying pCola-tacI-bicA and pCK4-mtaA; both receive putrescine and phenethylamine. The expression condition forms compounds 1 and 2. This is cellular heterologous production, not purified NRPS reconstitution. Exact stereochemical qualification is assessed separately. |
| S108-E-GENBANK | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=JX424818.1&amp;rettype=gb&amp;retmode=text; JX424818.1 header/source/all feature qualifiers | supports | The 16,848 bp sequence is from X. budapestensis DSM16342, taxon290110. nrpS/bicA has partial CDS &lt;1..16848, protein AFP87549.1. A complete-cluster metadata label does not make this submitted CDS or the expression construct complete. Empty owner bounds are retained; the whole accession is not invented as an experimentally minimal BGC. |
| S108-E-MIBIG | https://mibig.secondarymetabolites.org/repository/BGC0001135.5/annotations.json; Exact version 5 compound 1, taxonomy, methods and accession | supports | Current MIBiG retains the exact imported graph, questionable quality, completeness complete, NRPS Type I, heterologous method and JX424818.1. This is corroborated source provenance rather than a new native experiment. |
| S108-E-GAP | https://doi.org/10.1021/ac300372p; ACS main403 and discovered Zenodo410 receipts | unknown | The full main text remains unavailable after bounded distinct public routes. Official detailed SI is positive and inspected; lack of access is not whole-article absence of any experiment. |
| S108-E-ROUTES | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/producer_strains.py; Producer-strain loader and source-pinned composition limits | supports | The current strain overlay can annotate the native producer using a full raw-row guard. It cannot substitute the E. coli host, alter locus context, or compose silently with a structure correction; separate tested context/identity composition is required. |
| S108-E-SEARCH | /private/tmp/npm-review-work/shared-next-batch011/bgc-science/curator-routing/ignored-inclusive-search-receipts.json; Ignored-inclusive curation selectors and inspected consumers | context_only | The retained rg --no-ignore --hidden search covered exact BGC, labels and keys in curation. No existing target-specific correction was found in that scope; the seeder and consumed overlays were inspected statically. |
| C108-E-LOCAL | /private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/bicornutin-a1.yaml; Entire owner chemical_structure, source concept and grounding | supports | Neutral YHRZRWLQHQGLJN-VMAPGKTHSA-N; five assigned peptide alpha centres, including unique Leu alpha atom11R. The current identifier is source-concept-derived. The structure matches the exact frozen raw source row SHA256 683877f8e52dc86ee4487134f4cfa53c6a39b98580ff343f4a1ce2d046bc8494. |
| C108-E-SI | https://ndownloader.figshare.com/files/4137001; Table S8 page6; Figures S6/S7 pages16–17 and Marfey chromatograms page31 | supports | Hydrolyzed compound 1 has one L-Leu: its two derivative retention times are17.2/23.7 minutes, matching L standards. Bulk Arg L:D1:2.4 does not locate four positional configurations. Table S8 is compound1-specific. Figure S7 bold bonds are COSY connectivity, not stereochemical wedges. Therefore it establishes an A1 Leu comparison but cannot automatically repair A2. |
| C108-E-CALC | /private/tmp/npm-review-work/shared-next-batch011/bgc-science/chemical-comparison.json; Explicit graph parse, Standard/fixed-H identities and alpha-carbon neighbours | supports | Raw atom11 is bonded to N10, carbonyl C16 and side-chain CH2 C12. CIP priority N &gt; carbonyl C(O,O,N) &gt; CH2(C,H,H) &gt; H gives R, the D-Leu residue. All five centres and each full Standard key agree with current ChEBI/PubChem, but guanidino proton/double-bond placement differs in fixed-H InChI; no fixed-H identity is asserted. |
| C108-E-CHEBI | https://www.ebi.ac.uk/chebi/backend/api/public/compound/221898/; Exact full-key candidate, rating and chemical fields | supports | CHEBI:221898 is a two-star entry with the same five-centre Standard key. The official MOL agrees with its declared graph. It is not an eligible three-star correction target and copied authority agreement does not resolve the primary stereochemical concern. |
| C108-E-MOL | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/221898/; Complete MOL graph | supports | The neutral authority graph parses and shares Standard identity with raw but differs in fixed-H guanidino tautomer placement. No protonated salt is substituted. |
| C108-E-PC | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/YHRZRWLQHQGLJN-VMAPGKTHSA-N/property/InChI,InChIKey,CanonicalSMILES,IsomericSMILES/JSON; Exact-key returned complete property row | supports | The returned PubChem graph has the exact Standard key and five assigned centres; fixed-H differs from raw in the same guanidino representation. This is an authority comparison, not independent experimental proof. |
| C108-E-QA | /private/tmp/npm-review-work/shared-next-batch011/chemistry-prep/bicornutin-leu-independent-qa.json; Independent atom-neighbour CIP and original Table S8 inspection | context_only | Independent inspection corroborates the unique Leu atom/neighbours, R assignment and A1-specific measured L-Leu. It expressly does not transfer the result to A2 or resolve positional Arg centres. |
| C108-E-GAP | https://doi.org/10.1021/ac300372p; Retained main-paper access gap | unknown | Detailed main is unavailable after bounded ACS403 and discovered repository410. Original SI is available, but no uninspected full-paper absence is inferred. |
| C108-E-ROUTE | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/structure_corrections.py; Complete guarded identity correction consumer and source joins | supports | Existing correction actions accept only guarded unique eligible three-star ChEBI targets. They do not accept an arbitrary curated MOL, and reject duplicate/occupied targets and unsupported composition. Broad reference/strain overlays cannot repair stereo and reject co-application. A tested explicit-graph route is necessary if no eligible corrected target exists. |
| C108-E-SEARCH | /private/tmp/npm-review-work/shared-next-batch011/bgc-science/curator-routing/ignored-inclusive-search-receipts.json; Exact key/BGC/name search over ignored-inclusive curation | context_only | No existing target-specific identity correction was found in the bounded ignored-inclusive curation search. This is not a claim that all external knowledge is absent. |

## Limits And Additional Notes

- This review evaluates present assertions and bounded source gaps; it does not claim exhaustive discovery of every later publication or require all optional mechanisms for coverage.
- Full main unavailable; official SI was inspected at its exact original retrieval time and reread for this target.
- No independent full CDS translation or complete laboratory-construct reconstruction was needed for the absent owner protein claims.
- Chemical precision and unresolved positional stereochemistry are assessed in the companion chemistry packet. Optional extra mechanisms are not required.
- No complete main text; positional Arg configurations are not independently located by a bulk hydrolysate ratio.
- No new chemical experiment is claimed by RDKit or by comparison with copied authority records.
- A2-specific hand is not inferred from A1; current two-star ChEBI entries cannot execute the present identity-replacement contract.
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
review_id: 20261021T163039Z-bicornutin-a1
title: 'Bicornutin A1: measured leucine conflicts with the stored stereoisomer'
started_at: '2026-10-21T16:18:25.280834Z'
finished_at: '2026-10-21T16:30:39.262240Z'
completion: partial
verdict: needs_curation
scientific_review: true
summary: The primary supporting data identify L-leucine in compound 1, but the stored
  graph encodes D-leucine at that unique residue. This confirmed identity blocker
  requires a guarded correction and explicit handling of unresolved arginine positions.
  Native and heterologous named-product evidence remain supported.
source:
  git_revision: 1c2402097718c138b081e00943de8f04de0541cd
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/SKILL.md
    sha256: 37bab7503a87a7c801f7726f826fdd410588e1536253488c4ca69d451383fa02
    role: context
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
  - path: curation/decisions.tsv
    sha256: 7214a74975fb2cb65521da18dd14ea1c65665f50060106976dc0db9caf887805
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
  - path: data/natural_products/alkaloids/bicornutin-a1.yaml
    sha256: 0928ae4c6ac6fe10091e68ed505d53ed9048f6ab9cecd20ba63217f0d950e4f7
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
  - path: src/naturalproductmech/curate/curation_event.py
    sha256: dd39419502a9a7acf40e134a7642c5e310808cea33708eef300c62ba76dad6a5
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
  - path: src/naturalproductmech/grading.py
    sha256: ece54c4a2c0803f034ac59de51b1006cf79ea8d6b6256d75757d4adb88ea9630
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
  - path: src/naturalproductmech/validation/write_validated.py
    sha256: eb35df21c03c2e6272e665ea4d179f870a1ec6db61d52939058add44a0edde7f
    role: context
  - path: tests/test_claim_references.py
    sha256: 11b2fc60dbe32154df63fb2e8c784c7c8ba6585581c09bba2eebe2c5192d4c06
    role: context
  - path: tests/test_lotus_exclusions.py
    sha256: 3e3aa443714202e1bc41f0fb236e6bf69caabd68a16af23b972323f5f846386c
    role: context
  - path: tests/test_mibig_locus_evidence_overrides.py
    sha256: 9177b5bd24f6e47cc4743857179217d9e0d4add9560b2ce3faefaebe53ba09a0
    role: context
  - path: tests/test_producer_isolates.py
    sha256: 8f96b00fbb66564f2d5e5c2108c991135eec8731b10d9f2d9f2f73830080ccd9
    role: context
  - path: tests/test_producer_strains.py
    sha256: 17002ef1640464777f1925d12d842ed83c9098aad6de724ae0ea236ecccc4ff3
    role: context
  - path: tests/test_seed_skeleton.py
    sha256: 72ec216fb0ed365b09f1cfb64fb06c701c50b5d7c2df409d8dbf613d302803bf
    role: context
  - path: tests/test_structure_corrections.py
    sha256: f0b91c7ed2ffeddb844e6927e4891c1fa3cfd1d11eb70f1c3eda6bf80ae05303
    role: context
scope:
  description: One complete generated owner and any referenced components, assessed
    claim by claim for exact identity, provenance, origin, producer and occurrence
    scope, biosynthesis, classification, optional content and audit history.
  selection: Campaign record 108, batch 011, selected in path order from the fresh-main
    authoritative validated catalogue and the separately validated targets in earlier
    batch commits (publication tracked separately). At selection, 154 of 3116 current
    records had campaign coverage and 2962 remained. The population search included
    ignored files. Exactly one target is assessed here.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-8904b7e092
targets:
- target_id: naturalproductmech:mibig-8904b7e092
  path: data/natural_products/alkaloids/bicornutin-a1.yaml
  label: bicornutin A1
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
  - naturalproductmech:mibig-8904b7e092
  command: just validate-strict data/natural_products/alkaloids/bicornutin-a1.yaml
    --out /private/tmp/npm-review-work/108/strict.tsv
  exit_code: 0
  scope_note: Actual command finished 2026-10-21T16:18:27.302508Z
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
    for batch011 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch011. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-8904b7e092
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
    Reused for batch011 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch011. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-8904b7e092
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
    for batch011 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch011. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-8904b7e092
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
    for batch011 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch011. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-8904b7e092
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
    transcript: /private/tmp/npm-native-checks/batch-004/qc.log. Reused for batch011
    only after a fresh fetch/clean branch, equal commit/tree and two reads of all
    9,182 tracked byte streams and modes (208,070,649 bytes), including a recheck
    after the fresh authoritative catalogue. This gate was not rerun for batch011.
    Original execution times, scope, warnings, exceptions and skips are retained.'
  target_ids:
  - naturalproductmech:mibig-8904b7e092
- check_id: R108-FULL-OWNER
  name: Complete owner and referenced-component scope
  status: passed
  required: true
  summary: Full owner, exact matching intake source rows and the empty referenced-component
    set were read and checked against the actual intake. Fresh target strict validation
    is retained separately.
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  evidence_ids:
  - R108-OWNER
  - R108-LOCAL
- check_id: S108-C-METHOD
  name: Exact named product heterologous experiment
  status: passed
  required: true
  summary: Original Figure S5 explicitly identifies both products and the expression/control
    conditions; no method withdrawal is warranted.
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  evidence_ids:
  - S108-E-SI
  - S108-E-MIBIG
- check_id: S108-C-MAIN
  name: Detailed primary main and chemical assignment context
  status: unavailable
  required: true
  summary: Required full main remains unavailable. Positive SI scope is retained,
    while detailed assignment/construct interpretation cannot be represented as a
    complete paper read.
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  evidence_ids:
  - S108-E-GAP
  - S108-E-SI
- check_id: C108-C-GRAPH
  name: Exact stored graph versus current literal authority graphs
  status: passed
  required: true
  summary: Standard identity, formula and neutral charge agree; fixed-H tautomer differences
    are explicitly retained.
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  evidence_ids:
  - C108-E-LOCAL
  - C108-E-CALC
  - C108-E-CHEBI
  - C108-E-MOL
  - C108-E-PC
- check_id: C108-C-STEREO
  name: Exact primary residue-specific stereochemistry
  status: failed
  required: true
  summary: A1 atom-specific Leu R conflicts with the L-Leu measured from compound1.
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  evidence_ids:
  - C108-E-SI
  - C108-E-CALC
  - C108-E-QA
  - C108-E-GAP
- check_id: C108-C-MAIN
  name: Detailed full main assignment access
  status: unavailable
  required: true
  summary: Full main is required to resolve the remaining positional assignment and
    reporting context; detailed SI is positive but does not remove this limit.
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  evidence_ids:
  - C108-E-SI
  - C108-E-GAP
evidence:
- evidence_id: R108-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/bicornutin-a1.yaml
  locator: Complete owner, all assertions, inline graph, discussions and history
  accessed_at: '2026-10-21T16:19:22.240896Z'
  support: supports
  summary: 'Root read the entire bicornutin A1 owner following its official intake
    and rechecked the source-preparation bytes against this base. It has 1 occurrence,
    1 producer and 1 cluster assertions. The referenced component set is empty. Present
    optional fields: none.'
  snapshot_sha256: 0928ae4c6ac6fe10091e68ed505d53ed9048f6ab9cecd20ba63217f0d950e4f7
- evidence_id: R108-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/108/local-sources.json
  locator: Complete resolved owner and all exact matching local source rows
  accessed_at: '2026-10-21T16:19:22.240896Z'
  support: context_only
  summary: Root read the complete resolved owner and every matching MIBiG, LOTUS,
    ChEBI, CyanoMetDB and NPClassifier row captured by intake. This is a source-fidelity
    assessment, separate from independent experimental support.
  snapshot_sha256: e97357ee1e875e3b50312d4404d863883e5380ecd9886d3092e8a795a43e2e4c
- evidence_id: R108-Q26307569
  kind: database
  reference: https://www.wikidata.org/wiki/Q26307569
  locator: Literal entity and all nondeprecated P225/P685 values
  accessed_at: '2026-10-21T15:55:34.036365Z'
  support: context_only
  summary: Literal Q26307569 resolves to P225 Xenorhabdus budapestensis. P685 290110
    matches the local taxon identifiers. This checks identifier routing only, not
    occurrence, native production or experimental-stock identity.
  snapshot_sha256: 95bd451541285b30e68b07c85c5d35491ccd5c634271b0d19b50892012ac5e61
- evidence_id: R108-IMODULON
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete official 20-organism/28-dataset catalogue
  accessed_at: '2026-10-21T15:57:37.699699Z'
  support: context_only
  summary: The complete API catalogue retrieved at this timestamp matches the retained
    catalogue bytes. This evidence concerns catalogue membership only. The earlier
    adapter catalogue retains its original 2026-10-21T07:21:15.957321Z completion
    time in the separately pinned source packet.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: R108-IMODULON-CONTEXT
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch011/imodulon-context/source-notes.json
  locator: 'Prepared source packet: candidate_context, actual_accesses, metadata and
    the fully verified 53-input manifest'
  accessed_at: '2026-10-21T16:00:03.119199Z'
  support: context_only
  summary: The packet records the three official /meta responses and six scoped adapter
    queries with their individual original 2026-10-21T15:57–15:58Z access times. Its
    preparation/read-completion timestamp is used here, not presented as a new API
    retrieval. Exact species, stock, gene-search and component limits remain explicit;
    no chemical identity, production, native stock equivalence or module membership
    is inferred.
  snapshot_sha256: bb8dbcfd2ba18338393c3ed0da030ee8f19a9f4c73c2a8e32791240299d50d3d
- evidence_id: S108-E-LOCAL
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/bicornutin-a1.yaml
  locator: Entire owner, exact source row and resolved content
  accessed_at: '2026-10-21T16:26:26.024580Z'
  support: supports
  summary: Bicornutin A1, BGC0001135:1, full source-row SHA256 683877f8e52dc86ee4487134f4cfa53c6a39b98580ff343f4a1ce2d046bc8494,
    has Heterologous expression, SOURCE_ASSERTION producer and CLUSTER_DEMONSTRATED
    locus. Its sole LOTUS occurrence is the same study by DOI; no explicit pathway/protein
    graph is present.
  snapshot_sha256: 0928ae4c6ac6fe10091e68ed505d53ed9048f6ab9cecd20ba63217f0d950e4f7
- evidence_id: S108-E-SI
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/4137001
  locator: Tables S2/S4; Figures S2/S3/S5, pages 1–6 and 13–17
  accessed_at: '2026-10-21T15:41:09.453525Z'
  support: supports
  summary: Native X. budapestensis DSM16342 material contains named compound 1. Table
    S2 exact mass/isotope-feeding and fragmentation distinguish A1 putrescine from
    A2 phenethylamine. Figure S5 compares E. coli DH10B control with DH10B carrying
    pCola-tacI-bicA and pCK4-mtaA; both receive putrescine and phenethylamine. The
    expression condition forms compounds 1 and 2. This is cellular heterologous production,
    not purified NRPS reconstitution. Exact stereochemical qualification is assessed
    separately.
  snapshot_sha256: 2f1c1ceb8da4336c8495bcb2b9b1d22569620dff1230bb50c89a97b822529c0b
- evidence_id: S108-E-GENBANK
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JX424818.1&rettype=gb&retmode=text
  locator: JX424818.1 header/source/all feature qualifiers
  accessed_at: '2026-10-21T15:40:50.637221Z'
  support: supports
  summary: The 16,848 bp sequence is from X. budapestensis DSM16342, taxon290110.
    nrpS/bicA has partial CDS <1..16848, protein AFP87549.1. A complete-cluster metadata
    label does not make this submitted CDS or the expression construct complete. Empty
    owner bounds are retained; the whole accession is not invented as an experimentally
    minimal BGC.
  snapshot_sha256: 5c131ea98c0561142b4a5f956dc4781d4b3cb97f9242e2cad27ed6b35e6c6dff
- evidence_id: S108-E-MIBIG
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0001135.5/annotations.json
  locator: Exact version 5 compound 1, taxonomy, methods and accession
  accessed_at: '2026-10-21T15:35:33.146571Z'
  support: supports
  summary: Current MIBiG retains the exact imported graph, questionable quality, completeness
    complete, NRPS Type I, heterologous method and JX424818.1. This is corroborated
    source provenance rather than a new native experiment.
  snapshot_sha256: e368cf8a365034ced9299d9a89fb26487988f581db7a86522ca24ae946c870f7
- evidence_id: S108-E-GAP
  kind: search
  reference: https://doi.org/10.1021/ac300372p
  locator: ACS main403 and discovered Zenodo410 receipts
  accessed_at: '2026-10-21T16:26:26.024580Z'
  support: unknown
  summary: The full main text remains unavailable after bounded distinct public routes.
    Official detailed SI is positive and inspected; lack of access is not whole-article
    absence of any experiment.
  snapshot_sha256: ab2127b2e17f3e05136124ce54dc9913c374f42ae7050398c6ec5f6cb9bb25e3
  search_scope: Bounded original ACS main DOI10.1021/ac300372p route and discovered
    Zenodo repository route; retained HTTP403/410 responses only. Official accessible
    SI is assessed separately, and no global absence is inferred.
- evidence_id: S108-E-ROUTES
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/producer_strains.py
  locator: Producer-strain loader and source-pinned composition limits
  accessed_at: '2026-10-21T16:26:26.024580Z'
  support: supports
  summary: The current strain overlay can annotate the native producer using a full
    raw-row guard. It cannot substitute the E. coli host, alter locus context, or
    compose silently with a structure correction; separate tested context/identity
    composition is required.
  snapshot_sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
- evidence_id: S108-E-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch011/bgc-science/curator-routing/ignored-inclusive-search-receipts.json
  locator: Ignored-inclusive curation selectors and inspected consumers
  accessed_at: '2026-10-21T16:26:26.024580Z'
  support: context_only
  summary: The retained rg --no-ignore --hidden search covered exact BGC, labels and
    keys in curation. No existing target-specific correction was found in that scope;
    the seeder and consumed overlays were inspected statically.
  snapshot_sha256: 5983727d1b68effce0718a6eae1f5c17145ee56c1104d97b255da83806227e60
  search_scope: Ignored-inclusive rg --no-ignore --hidden search within repository
    curation/ for exact BGC0001135, bicornutin names and full target InChIKeys; retained
    command receipt defines the searched surface. No global external-knowledge absence
    claim.
- evidence_id: C108-E-LOCAL
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/bicornutin-a1.yaml
  locator: Entire owner chemical_structure, source concept and grounding
  accessed_at: '2026-10-21T16:26:26.037431Z'
  support: supports
  summary: Neutral YHRZRWLQHQGLJN-VMAPGKTHSA-N; five assigned peptide alpha centres,
    including unique Leu alpha atom11R. The current identifier is source-concept-derived.
    The structure matches the exact frozen raw source row SHA256 683877f8e52dc86ee4487134f4cfa53c6a39b98580ff343f4a1ce2d046bc8494.
  snapshot_sha256: 0928ae4c6ac6fe10091e68ed505d53ed9048f6ab9cecd20ba63217f0d950e4f7
- evidence_id: C108-E-SI
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/4137001
  locator: Table S8 page6; Figures S6/S7 pages16–17 and Marfey chromatograms page31
  accessed_at: '2026-10-21T15:41:09.453525Z'
  support: supports
  summary: 'Hydrolyzed compound 1 has one L-Leu: its two derivative retention times
    are17.2/23.7 minutes, matching L standards. Bulk Arg L:D1:2.4 does not locate
    four positional configurations. Table S8 is compound1-specific. Figure S7 bold
    bonds are COSY connectivity, not stereochemical wedges. Therefore it establishes
    an A1 Leu comparison but cannot automatically repair A2.'
  snapshot_sha256: 2f1c1ceb8da4336c8495bcb2b9b1d22569620dff1230bb50c89a97b822529c0b
- evidence_id: C108-E-CALC
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch011/bgc-science/chemical-comparison.json
  locator: Explicit graph parse, Standard/fixed-H identities and alpha-carbon neighbours
  accessed_at: '2026-10-21T16:26:26.037431Z'
  support: supports
  summary: Raw atom11 is bonded to N10, carbonyl C16 and side-chain CH2 C12. CIP priority
    N > carbonyl C(O,O,N) > CH2(C,H,H) > H gives R, the D-Leu residue. All five centres
    and each full Standard key agree with current ChEBI/PubChem, but guanidino proton/double-bond
    placement differs in fixed-H InChI; no fixed-H identity is asserted.
  snapshot_sha256: 090cb24ec31db5110f7e1b586c87e7b0d480df7fe0f10432d3c843e869909102
- evidence_id: C108-E-CHEBI
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/221898/
  locator: Exact full-key candidate, rating and chemical fields
  accessed_at: '2026-10-21T15:42:37.372274Z'
  support: supports
  summary: CHEBI:221898 is a two-star entry with the same five-centre Standard key.
    The official MOL agrees with its declared graph. It is not an eligible three-star
    correction target and copied authority agreement does not resolve the primary
    stereochemical concern.
  snapshot_sha256: cc99df4e6fc62a562c9fcdf9947aafb73c2135adcd9f8abcde14b8f41bd9bb6e
- evidence_id: C108-E-MOL
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/221898/
  locator: Complete MOL graph
  accessed_at: '2026-10-21T15:42:37.349614Z'
  support: supports
  summary: The neutral authority graph parses and shares Standard identity with raw
    but differs in fixed-H guanidino tautomer placement. No protonated salt is substituted.
  snapshot_sha256: d819e485dd277436f6d039e530e96b13da45f97e2ee5afdd1c788ae3d105a5f2
- evidence_id: C108-E-PC
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/YHRZRWLQHQGLJN-VMAPGKTHSA-N/property/InChI,InChIKey,CanonicalSMILES,IsomericSMILES/JSON
  locator: Exact-key returned complete property row
  accessed_at: '2026-10-21T15:42:03.177222Z'
  support: supports
  summary: The returned PubChem graph has the exact Standard key and five assigned
    centres; fixed-H differs from raw in the same guanidino representation. This is
    an authority comparison, not independent experimental proof.
  snapshot_sha256: 078864b9b9612d8f2aa6041f9c02ec0ddf3c15c1ac5fb036522d35b9b1e6772f
- evidence_id: C108-E-QA
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch011/chemistry-prep/bicornutin-leu-independent-qa.json
  locator: Independent atom-neighbour CIP and original Table S8 inspection
  accessed_at: '2026-10-21T16:26:26.037431Z'
  support: context_only
  summary: Independent inspection corroborates the unique Leu atom/neighbours, R assignment
    and A1-specific measured L-Leu. It expressly does not transfer the result to A2
    or resolve positional Arg centres.
  snapshot_sha256: fd3cc622efaf2e14eca79d8813ff3280e4fda8087d3725e05ecd6b4192384c4b
- evidence_id: C108-E-GAP
  kind: search
  reference: https://doi.org/10.1021/ac300372p
  locator: Retained main-paper access gap
  accessed_at: '2026-10-21T16:26:26.037431Z'
  support: unknown
  summary: Detailed main is unavailable after bounded ACS403 and discovered repository410.
    Original SI is available, but no uninspected full-paper absence is inferred.
  snapshot_sha256: ab2127b2e17f3e05136124ce54dc9913c374f42ae7050398c6ec5f6cb9bb25e3
  search_scope: Bounded original ACS main DOI10.1021/ac300372p route and discovered
    Zenodo repository route; retained HTTP403/410 responses only. Official accessible
    SI is assessed separately, and no global absence is inferred.
- evidence_id: C108-E-ROUTE
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/structure_corrections.py
  locator: Complete guarded identity correction consumer and source joins
  accessed_at: '2026-10-21T16:26:26.037431Z'
  support: supports
  summary: Existing correction actions accept only guarded unique eligible three-star
    ChEBI targets. They do not accept an arbitrary curated MOL, and reject duplicate/occupied
    targets and unsupported composition. Broad reference/strain overlays cannot repair
    stereo and reject co-application. A tested explicit-graph route is necessary if
    no eligible corrected target exists.
  snapshot_sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
- evidence_id: C108-E-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch011/bgc-science/curator-routing/ignored-inclusive-search-receipts.json
  locator: Exact key/BGC/name search over ignored-inclusive curation
  accessed_at: '2026-10-21T16:26:26.037431Z'
  support: context_only
  summary: No existing target-specific identity correction was found in the bounded
    ignored-inclusive curation search. This is not a claim that all external knowledge
    is absent.
  snapshot_sha256: 5983727d1b68effce0718a6eae1f5c17145ee56c1104d97b255da83806227e60
  search_scope: Ignored-inclusive rg --no-ignore --hidden search within repository
    curation/ for exact BGC0001135, bicornutin names and full target InChIKeys; retained
    command receipt defines the searched surface. No global external-knowledge absence
    claim.
assessments:
- assessment_id: R108-HISTORY
  area: provenance
  topic: Native status and retained audit history
  outcome: supported
  summary: All retained events are dated SEEDED_FROM_SOURCES provenance. The owner
    remains SEEDED. No native scientific status or history changes result from this
    review.
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  evidence_ids:
  - R108-OWNER
- assessment_id: R108-OPTIONAL
  area: completeness
  topic: Present optional assertions and enrichment limits
  outcome: not_applicable
  summary: The complete owner has no optional pathway, mechanism graph, molecular
    target, bioactivity, application, clinical status, cross-corpus relation or discussion.
    Optional enrichment is separate from correction of current claims.
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  evidence_ids:
  - R108-OWNER
  - R108-LOCAL
- assessment_id: R108-FILING
  area: representation
  topic: Computed filing and exact-key classification provenance
  outcome: supported
  summary: The current owner reproduces its exact-key NPClassifier result, including
    npclassifier.gnps2.org@2026-09-07, Alkaloids filing and all returned superclass/class
    labels. It preserves the false glycoside prediction. These predictions do not
    independently prove precursor use, natural origin or absolute stereochemistry.
    Any future identity correction requires classification against the corrected effective
    key.
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  evidence_ids:
  - R108-OWNER
  - R108-LOCAL
- assessment_id: R108-ORGANISM-IDS
  area: provenance
  topic: Literal organism-identifier routing
  outcome: supported
  summary: All literal organism entities have matching scientific names; available
    P685 values agree. Primary occurrence and producer support are assessed independently.
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  evidence_ids:
  - R108-Q26307569
- assessment_id: R108-IMODULON-SCOPE
  area: completeness
  topic: Producer and experimental-host transcriptomic applicability
  outcome: not_applicable
  summary: The complete inspected catalogue has no exact Xenorhabdus budapestensis
    native-producer dataset. The native DSM16342 producer and engineered Escherichia
    coli DH10B expression host remain distinct; no exact experimental-host dataset
    or component membership was established. The catalogue result is not evidence
    against production.
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  evidence_ids:
  - R108-OWNER
  - R108-IMODULON
  - R108-IMODULON-CONTEXT
- assessment_id: S108-A-BGC
  area: evidence
  topic: Named product, donor, locus and host scope
  outcome: supported
  summary: The imported heterologous method and corresponding formal grades are supported
    by original SI. Native culture evidence supports biological origin and occurrence
    without inventing native genetic necessity. The exact retained stereoisomer is
    a separate chemical claim.
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  evidence_ids:
  - S108-E-LOCAL
  - S108-E-SI
  - S108-E-GENBANK
  - S108-E-MIBIG
  dimensions:
  - name: native_strain
    value: Xenorhabdus budapestensis DSM16342
    definition: Native named-product culture and submitted donor sequence; not the
      heterologous expression host.
    evidence_ids:
    - S108-E-SI
    - S108-E-GENBANK
  - name: experimental_host
    value: E. coli DH10B; pCola-tacI-bicA plus pCK4-mtaA, fed terminal amines
    definition: Positive cellular expression experiment, not a native knockout or
      purified final-product reaction.
    evidence_ids:
    - S108-E-SI
  - name: evidence_tier
    value: Source-tier producer; demonstrated heterologous locus link
    definition: The current method grades are applicable to the named product, subject
      to separate exact-stereochemistry adjudication.
    evidence_ids:
    - S108-E-LOCAL
    - S108-E-SI
    - S108-E-MIBIG
- assessment_id: S108-A-OCC
  area: evidence
  topic: Sole LOTUS occurrence and primary reference
  outcome: supported
  summary: The DOI and PMID identify the same study. Native DSM16342 culture contains
    named bicornutin A1; positive occurrence should be preserved with strain and chemistry
    qualification. This does not add a species-wide biosynthesis claim.
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  evidence_ids:
  - S108-E-LOCAL
  - S108-E-SI
  - S108-E-GENBANK
- assessment_id: C108-A-IDENTITY
  area: identity
  topic: Exact constitution, microstate and stereochemical assignment
  outcome: concern
  summary: A1’s encoded Leu is the opposite stereoisomer to the directly measured
    single residue; the remaining positional Arg assignments are not independently
    certified.
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  evidence_ids:
  - C108-E-LOCAL
  - C108-E-SI
  - C108-E-CALC
  - C108-E-QA
  - C108-E-GAP
  dimensions:
  - name: stereochemical_resolution
    value: Five database-assigned centres; compound1-specific L-Leu experiment
    definition: Atom-neighbour CIP is explicit; bulk hydrolysate Arg ratio and NRPS
      architecture are not equivalent to positional direct determination.
    evidence_ids:
    - C108-E-SI
    - C108-E-CALC
    - C108-E-QA
- assessment_id: C108-A-AUTHORITY
  area: grounding
  topic: Current authority agreement and eligible identifier
  outcome: supported
  summary: Current full-key authority matches are two-star ChEBI and exact PubChem.
    Minting rather than selecting an ineligible ChEBI is consistent with the present
    priority rules. Authority consensus does not override experimental conflict; Standard
    identity is distinguished from fixed-H tautomer identity.
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  evidence_ids:
  - C108-E-LOCAL
  - C108-E-CHEBI
  - C108-E-MOL
  - C108-E-PC
  - C108-E-CALC
findings:
- finding_id: S108-F-CONTEXT
  issue_key: mibig-bgc0001135-compound1-native-strain-expression-context
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Bicornutin A1 omits its supported strain and expression context
  description: The native donor is specifically DSM16342; the demonstrated experiment
    uses fed E. coli DH10B with bicA and mtaA. The current generic species and bare
    method are faithful but omit useful non-blocking context. Preserve the correct
    method and source-tier producer; do not rename the native donor as the engineered
    host.
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  field_paths:
  - producer_organisms[0].strain
  - producer_organisms[0].notes
  - biosynthetic_gene_clusters[0].notes
  evidence_ids:
  - S108-E-LOCAL
  - S108-E-SI
  - S108-E-GENBANK
  - S108-E-ROUTES
  - S108-E-SEARCH
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Full-row guarded native-strain annotation
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Consumed strain overlay and composition contract
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Locus experiment-context emission if implemented
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Untouched exact source row
- finding_id: C108-F-LEU
  issue_key: bicornutin-a1-encoded-d-leucine-conflicts-primary-l-leucine
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Bicornutin A1 encodes the opposite leucine stereoisomer
  description: The unique isobutyl-bearing peptide alpha carbon is R with an explicit
    N/carbonyl/side-chain/H priority sequence, representing D-Leu. Primary Table S8
    directly identifies the single Leu in compound1 as L. This is a concrete stereoisomer
    conflict, not a general R=L shortcut or an inference from database voting. Other
    Arg centres remain separately unresolved.
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  - chemical_structure.stereo_complete
  evidence_ids:
  - C108-E-LOCAL
  - C108-E-SI
  - C108-E-CALC
  - C108-E-QA
  - C108-E-CHEBI
  - C108-E-ROUTE
  - C108-E-SEARCH
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Future guarded source-concept identity decision
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Explicit-graph correction route requires implementation
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Identity regrouping and claim migration
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Original full source-row pin
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: Composition boundary
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Composition boundary
actions:
- action_id: S108-ACT-CONTEXT
  finding_ids:
  - S108-F-CONTEXT
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Full-row guarded native-strain annotation
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Consumed strain overlay and composition contract
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Locus experiment-context emission if implemented
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Untouched exact source row
  generator: scripts/seed_from_sources.py
  description: 'For BGC0001135:1, pin full raw-row SHA256 683877f8e52dc86ee4487134f4cfa53c6a39b98580ff343f4a1ce2d046bc8494,
    version5, taxon290110, accession JX424818.1, empty locus bounds, key YHRZRWLQHQGLJN-VMAPGKTHSA-N
    and old Heterologous expression. Use the consumed strain overlay to record DSM16342
    with DOI:10.1021/ac300372p. Preserve native SOURCE_ASSERTION and heterologous
    CLUSTER_DEMONSTRATED. Add the two-plasmid DH10B/fed-amine context through a tested
    consumed source-context route or an interim explicitly qualified curator discussion.
    If the identity correction changes this source graph, first implement/test composition:
    current producer_strains rejects concurrent structure correction. Do not bypass
    that rejection, change raw rows, or treat partial JX424818.1 as a full expression
    construct.'
  acceptance_checks:
  - Require exactly one original source row and fail on every field drift, including
    empty bounds.
  - Preserve both positive named-product occurrence and applicable heterologous method;
    no unsupported native knockout grade.
  - Prove explicit composition with any identity correction and no silent loss of
    context/citations on regeneration.
  - Regenerate and run documented strict, grounding, history and scientific review
    gates only in a separately authorized curation task.
- action_id: C108-ACT-LEU
  finding_ids:
  - C108-F-LEU
  target_ids:
  - naturalproductmech:mibig-8904b7e092
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Future guarded source-concept identity decision
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Explicit-graph correction route requires implementation
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Identity regrouping and claim migration
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Original full source-row pin
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: Composition boundary
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Composition boundary
  generator: scripts/seed_from_sources.py
  description: Pin BGC0001135:1, complete raw-row SHA256 683877f8e52dc86ee4487134f4cfa53c6a39b98580ff343f4a1ce2d046bc8494,
    exact original key YHRZRWLQHQGLJN-VMAPGKTHSA-N, literal SMILES N[C@@H](CCCNC(N)=N)C(N[C@H](CC(C)C)C(N[C@@H](CCCNC(N)=N)C(N[C@@H](CCCNC(N)=N)C(N[C@H](CCCNC(N)=N)C(NCCCCN)=O)=O)=O)=O)=O,
    and full old chemical payload in exact-owner-claim-guards.json. Adjudicate the
    remaining positional Arg assignments from detailed primary evidence, then use
    an eligible exact corrected three-star authority if one becomes available; current
    CHEBI221898 is two-star and repeats the conflict. Otherwise implement/test an
    explicit curated-structure correction action that pins original and target MOL/SMILES,
    atom mapping, Standard and fixed-H identities, charge and supported stereo. At
    minimum the measured Leu must be S under the demonstrated neighbour ordering;
    do not invent Arg assignments or silently treat a partially qualified correction
    as a fully experimentally established graph. Explicitly migrate source-specific
    positive occurrence/locus/strain context to the corrected owner and audit old-key
    LOTUS/CheBI/PC associations; current same-key joins and reference/strain loaders
    do not compose automatically. Preserve A2 separately without copying this repair.
  acceptance_checks:
  - Show the exact unique Leu atom mapping and CIP change R to S, unchanged constitution/charge/terminal
    putrescine, and independent target-graph recomputation.
  - Reject every original-row or expected chemical field drift; no hand-edit of raw
    or generated YAML and no unsupported three-star claim.
  - Document retained versus unresolved Arg stereochemistry and do not infer stereowedges
    from COSY-bold bonds.
  - Test migration, old-key cleanup and explicit composition with native-strain/reference/context
    changes; no lost positive product evidence or accidental A2 edit.
  - Regenerate and run all documented gates in separately authorized curation; the
    present action does not claim that the missing explicit-graph consumer already
    exists.
limitations:
- This review evaluates present assertions and bounded source gaps; it does not claim
  exhaustive discovery of every later publication or require all optional mechanisms
  for coverage.
- Full main unavailable; official SI was inspected at its exact original retrieval
  time and reread for this target.
- No independent full CDS translation or complete laboratory-construct reconstruction
  was needed for the absent owner protein claims.
- Chemical precision and unresolved positional stereochemistry are assessed in the
  companion chemistry packet. Optional extra mechanisms are not required.
- No complete main text; positional Arg configurations are not independently located
  by a bulk hydrolysate ratio.
- No new chemical experiment is claimed by RDKit or by comparison with copied authority
  records.
- A2-specific hand is not inferred from A1; current two-star ChEBI entries cannot
  execute the present identity-replacement contract.
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
- batch-011
```
