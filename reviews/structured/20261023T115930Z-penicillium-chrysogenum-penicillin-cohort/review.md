# Penicillium chrysogenum penicillin biosynthetic cohort review (BGC0000404 and BGC0000405)

- Review: 20261023T115930Z-penicillium-chrysogenum-penicillin-cohort
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-23T11:43:00.000000Z
- Finished UTC: 2026-10-23T11:59:30.000000Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full 3-record category review of the Penicillium chrysogenum penicillin biosynthetic cohort seeded from MIBiG BGC0000404 (DQ192518.1) and BGC0000405 (EF601124.1): N-[(5S)-5-ammonio-5-carboxylatopentanoyl]-L-cysteinyl-D-valinate (CHEBI:58572, n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml), isopenicillin N (CHEBI:18165, isopenicillin-n.yaml), and benzylpenicillin sodium (CHEBI:51765, benzylpenicillin-sodium.yaml), anchored to a full-corpus deterministic checkpoint of all 3,116 natural product owners (282 with inline causal_graphs and 27 with causal_graph_refs) and 246 standalone causal graph components (3,362 total YAML records). Confirms verified Cycle 2 Stage 2/3 ACVS (P26046) and IPNS (P08703) biosynthetic steps and UniProtKB protein groundings on CHEBI:58572 and CHEBI:18165, while identifying three open findings for Stage 5 grouped remediation: (1) missing producer strain qualifications AS-P-78 on BGC0000404:1 (DQ192518.1, Fierro et al. 2006 DOI:10.1016/j.fgb.2006.03.001) and Wisconsin 54-1255 on BGC0000405:1..3 (EF601124.1, van den Berg et al. 2007 DOI:10.1016/j.fgb.2007.03.008) (F-PEN-001), (2) misrouted claim-level citations attaching Chain et al. 1940 (DOI:10.1016/s0140-6736(00)87452-8) to the 2005/2006 DQ192518.1 locus/producer claims on BGC0000404:1 and Smith et al. 1990 (PMID:1368505) to the 2007 EF601124.1 locus/producer claims on BGC0000405:1..3 (F-PEN-002), and (3) upstream MIBiG salt and protonation-state encoding boundaries on CHEBI:51765 (sodium salt FCPVYOBCFFNJFS-LQDWTQKMSA-M vs neutral benzylpenicillin CHEBI:18208 / CHEBI:17334, blocking PenDE RHEA:19809 pathway curation tracked in #1015) and CHEBI:58572 (monoanion vs neutral ACV CHEBI:28496) (F-PEN-003).

## Scope And Provenance

Coherent 3-record biosynthetic and chemical-identity cohort covering all NaturalProductMech records seeded from the Penicillium chrysogenum penicillin biosynthetic gene clusters MIBiG BGC0000404 (DQ192518.1) and BGC0000405 (EF601124.1), evaluated alongside frozen full-corpus inventory checks (3,116 owner YAML records and 246 standalone causal graph components; 3,362 total YAML records).

Selection: All records derived from the Penicillium chrysogenum penicillin biosynthetic gene cluster deposits BGC0000404:1 and BGC0000405:1..3, selected to audit the newly curated Cycle 2 Stage 2/3 ACVS (P26046) and IPNS (P08703) biosynthetic steps, the blocked PenDE step on benzylpenicillin-sodium.yaml (#1015), and cohort-wide producer strain and claim-reference provenance.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: git_commit at Git base 508e90d99e8e8cb7627eb8c885d535be25873c7f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:58572 | data/natural_products/amino_acids_and_peptides/n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml | generated | N-[(5S)-5-ammonio-5-carboxylatopentanoyl]-L-cysteinyl-D-valinate |
| CHEBI:18165 | data/natural_products/amino_acids_and_peptides/isopenicillin-n.yaml | generated | isopenicillin N |
| CHEBI:51765 | data/natural_products/amino_acids_and_peptides/benzylpenicillin-sodium.yaml | generated | benzylpenicillin sodium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native source inspection (cohort) | passed | True | CHEBI:58572, CHEBI:18165, CHEBI:51765 | Captured exact Git base 508e90d99e8e8cb7627eb8c885d535be25873c7f and verified SHA256 digests for all 3 cohort target YAML files and raw/curation TSV inputs. |
| Strict schema and semantic validation (cohort) | passed | True | CHEBI:58572, CHEBI:18165, CHEBI:51765 | All 3 cohort YAML files passed strict LinkML and semantic validation with 0 ERROR rows. |
| Full-corpus lockfile and filing verification | passed | True | CHEBI:58572, CHEBI:18165, CHEBI:51765 | Verified lockfile integrity across all 3,116 natural product owner records against data/natural_products/PATHS.tsv. |
| Full-corpus ontology ID-label correspondence | passed | True | CHEBI:58572, CHEBI:18165, CHEBI:51765 | Full-corpus ID-label check passed with 0 ERROR rows (13,465 OK_CANONICAL, 655 OK_SYNONYM, 35 OK_EXCEPTION, 0 ID_NOT_FOUND, 499 warn-only taxon_labels mismatches); all ChEBI, NCBITaxon, UniProtKB, GO, and RHEA terms on the 3 cohort records resolve canonically. |
| Exhaustive corpus review-queue checkpoint | passed | True | CHEBI:58572, CHEBI:18165, CHEBI:51765 | Computed exhaustive review-records queue across all 3,116 corpus owners (8,924 rows across 12 queues: producer-evidence 2,292; biosynthesis 1,184; structure-disagreement 5; name-disagreement 67; unnamed-producer 39; shared-structure 207; needs-a-name 18; occurrence-only 12; pathway-ambiguous 620; unresolved-taxa 3,329; stereo-incomplete 1,124; record-review 27). All 3 cohort records appear in producer-evidence; CHEBI:58572 and CHEBI:51765 appear in name-disagreement; CHEBI:51765 additionally appears in biosynthesis and shared-structure. |
| Repository-wide identifier and BGC cross-reference search | passed | True | CHEBI:58572, CHEBI:18165, CHEBI:51765 | Verified all 33 repository file references to BGC0000404, BGC0000405, DQ192518.1, EF601124.1, and cohort identifiers across raw inventories, curation tables, records, and pages. |
| Full-corpus standalone causal graph component validation | passed | True | CHEBI:58572, CHEBI:18165, CHEBI:51765 | Validated all 246 standalone causal graph component YAML files under data/causal_graphs/ (40 passed, 0 failed). |

## Scientific And Domain Assessments

### Chemical structure grounding and Cycle 2 Stage 2/3 ACVS/IPNS biosynthetic pathway verification

identity: supported. Targets: CHEBI:58572, CHEBI:18165, CHEBI:51765.

All three cohort records ground to distinct 3-star ChEBI entries (CHEBI:58572, CHEBI:18165, CHEBI:51765) and file under AMINO_ACIDS_AND_PEPTIDES in exact agreement with data/natural_products/PATHS.tsv. The Cycle 2 Stage 2/3 biosynthetic_pathway steps on CHEBI:58572 (ACVS / pcbAB, UniProtKB:P26046, RHEA:23620, PMID:2125231 / PMID:1849983) and CHEBI:18165 (ACVS P26046 -&gt; IPNS / pcbC, UniProtKB:P08703, RHEA:16689, PMID:3001640) are accurately grounded to Penicillium chrysogenum (NCBITaxon:5076) and pass strict LinkML and ontology ID-label validation.

### Missing AS-P-78 (BGC0000404:1) and Wisconsin 54-1255 (BGC0000405:1..3) producer strain qualifications

completeness: concern. Targets: CHEBI:58572, CHEBI:18165, CHEBI:51765.

All four Penicillium chrysogenum (NCBITaxon:5076) producer_organisms claims across the 3 cohort records omit producer_organisms[*].strain because MIBiG 4.0 exports species-level organism_name='Penicillium chrysogenum'. INSDC DQ192518.1 and Fierro et al. (2006, DOI:10.1016/j.fgb.2006.03.001, PMID:16713314) explicitly identify strain AS-P-78 for BGC0000404:1 (benzylpenicillin-sodium.yaml), and INSDC EF601124.1 and van den Berg et al. (2007, DOI:10.1016/j.fgb.2007.03.008, PMID:17548217) explicitly identify strain Wisconsin 54-1255 for BGC0000405:1..3 (all 3 cohort records).

### Misrouted entry-level citations on BGC0000404:1 (DQ192518.1) and BGC0000405:1..3 (EF601124.1)

provenance: concern. Targets: CHEBI:58572, CHEBI:18165, CHEBI:51765.

On benzylpenicillin-sodium.yaml (BGC0000404:1), producer_organisms[0].evidence[0].reference and biosynthetic_gene_clusters[0].evidence[0].reference (genbank:DQ192518.1) cite Chain et al. (1940, Lancet, DOI:10.1016/s0140-6736(00)87452-8, reference_basis: COMPOUND_BIOACTIVITY), published 65 years before the 2005/2006 DQ192518.1 sequence deposit from strain AS-P-78 (Fierro et al. 2006, DOI:10.1016/j.fgb.2006.03.001). On all three BGC0000405 records (BGC0000405:1..3), producer_organisms and biosynthetic_gene_clusters (genbank:EF601124.1) cite Smith et al. (1990, PMID:1368505), published 17 years before the 2007 EF601124.1 sequence deposit from strain Wisconsin 54-1255 (van den Berg et al. 2007, DOI:10.1016/j.fgb.2007.03.008).

### Upstream MIBiG salt and protonation-state encoding on CHEBI:51765 and CHEBI:58572

representation: concern. Targets: CHEBI:58572, CHEBI:18165, CHEBI:51765.

MIBiG BGC0000404:1 and BGC0000405:3 supply the sodium carboxylate salt SMILES for compound_name='benzylpenicillin' (grounding to CHEBI:51765 benzylpenicillin sodium, FCPVYOBCFFNJFS-LQDWTQKMSA-M, rather than neutral benzylpenicillin CHEBI:18208 / CHEBI:17334 JGSARLDLIJGVTE-MBNYWOFBSA-N or monoanion CHEBI:51354 JGSARLDLIJGVTE-MBNYWOFBSA-M), which triggers OPEN name-disagreement and shared-structure discussions and blocks RHEA:19809 (PenDE / UniProtKB:P15802) pathway curation on benzylpenicillin-sodium.yaml (tracked in open issue #1015). Similarly, BGC0000405:1 encodes monoanionic ACV (CHEBI:58572, BYEIJZFKOAXBBV-ATZCPNFKSA-M) rather than neutral ACV (CHEBI:28496, BYEIJZFKOAXBBV-ATZCPNFKSA-N), triggering an OPEN name-disagreement discussion.

## Findings

### F-PEN-001: Missing AS-P-78 (BGC0000404:1) and Wisconsin 54-1255 (BGC0000405:1..3) producer strain qualifications on Penicillium chrysogenum records

major / open / confirmed; issue key: penicillium-chrysogenum-bgc0000404-bgc0000405-producer-strains-missing.

All four Penicillium chrysogenum (NCBITaxon:5076) producer_organisms claims seeded from BGC0000404:1 (sha256 9460d29fcad2b7ecb913298bc80838656966e219ec0654094d28b71942eaeb19 on benzylpenicillin-sodium.yaml) and BGC0000405:1..3 (sha256s 50cbd967cf8076f7cbfa5a77bbb9b2910e1e37593d10edea50ad6c3a83316de1 on n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml, ae975df0e01f81b73c2e119b776207ca3e0f061375585a06ceef3f099dbbe860 on isopenicillin-n.yaml, and 847cf368dc26e162604ac12681781efc5814bcc31c4e19e94b09578562a1dd42 on benzylpenicillin-sodium.yaml) omit producer_organisms[*].strain. INSDC DQ192518.1 and Fierro et al. (2006, DOI:10.1016/j.fgb.2006.03.001, PMID:16713314) explicitly identify strain AS-P-78 for BGC0000404:1, and INSDC EF601124.1 and van den Berg et al. (2007, DOI:10.1016/j.fgb.2007.03.008, PMID:17548217) explicitly identify strain Wisconsin 54-1255 for BGC0000405:1..3. Notice that on benzylpenicillin-sodium.yaml, qualifying BGC0000404:1 as AS-P-78 and BGC0000405:3 as Wisconsin 54-1255 also resolves the two distinct sequenced industrial/laboratory strains instead of collapsing both clusters onto one unqualified NCBITaxon:5076 producer entry.

### F-PEN-002: Misrouted entry-level citations on BGC0000404:1 (Chain et al. 1940 on DQ192518.1) and BGC0000405:1..3 (Smith et al. 1990 on EF601124.1)

major / open / confirmed; issue key: bgc0000404-bgc0000405-anachronistic-claim-reference-routing.

1) On benzylpenicillin-sodium.yaml (CHEBI:51765), BGC0000404:1 attaches DOI:10.1016/s0140-6736(00)87452-8 (Chain et al., 1940, Lancet, reference_basis: COMPOUND_BIOACTIVITY) to producer_organisms[0].evidence[0].reference and biosynthetic_gene_clusters[0].evidence[0].reference (genbank:DQ192518.1, 17440..28759), even though Chain et al. (1940) pre-date the 2005/2006 DQ192518.1 sequence deposit from Penicillium chrysogenum AS-P-78 (Fierro et al., 2006, DOI:10.1016/j.fgb.2006.03.001, PMID:16713314) by 65 years. 2) Across all three BGC0000405 records (CHEBI:58572, CHEBI:18165, CHEBI:51765), BGC0000405:1..3 attach PMID:1368505 (Smith et al., 1990, Biotechnology 8:39-41, DOI:10.1038/nbt0190-39) to producer_organisms and biosynthetic_gene_clusters (genbank:EF601124.1, 22186..33473), even though Smith et al. (1990) pre-date the 2007 EF601124.1 sequence deposit from Penicillium chrysogenum Wisconsin 54-1255 (van den Berg et al., 2007, DOI:10.1016/j.fgb.2007.03.008, PMID:17548217) by 17 years.

### F-PEN-003: Upstream MIBiG salt and protonation-state encoding on benzylpenicillin sodium (CHEBI:51765) and monoanionic ACV (CHEBI:58572)

minor / open / confirmed; issue key: penicillin-cohort-salt-and-protonation-state-boundary.

1) MIBiG BGC0000404:1 and BGC0000405:3 supply the sodium salt SMILES [H][C@]12SC(C)(C)[C@@H](N1C(=O)[C@H]2NC(=O)Cc1ccccc1)C(=O)[O-].[Na+] (Standard InChIKey FCPVYOBCFFNJFS-LQDWTQKMSA-M, grounding to 3-star CHEBI:51765 benzylpenicillin sodium) for compound_name='benzylpenicillin'. Because the biological product of isopenicillin N acyltransferase (PenDE / UniProtKB:P15802, RHEA:19809) is benzylpenicillin(1-) (CHEBI:51354, JGSARLDLIJGVTE-MBNYWOFBSA-M) / neutral benzylpenicillin (CHEBI:18208 / CHEBI:17334, JGSARLDLIJGVTE-MBNYWOFBSA-N) and validate_strict.py enforces terminal biosynthetic_pathway product grounding against record.identifier (CHEBI:51765), PenDE pathway curation on benzylpenicillin-sodium.yaml remains blocked by open issue #1015, and OPEN name-disagreement and shared-structure discussions remain on the record. 2) MIBiG BGC0000405:1 supplies monoanionic ACV (CHEBI:58572, BYEIJZFKOAXBBV-ATZCPNFKSA-M) under the neutral label 'N-(5-amino-5-carboxypentanoyl)-L-cysteinyl-D-valine' (neutral CHEBI:28496, BYEIJZFKOAXBBV-ATZCPNFKSA-N), leaving an OPEN name-disagreement discussion on n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml.

## Recommended Actions And Acceptance Checks

### qualify-chrysogenum-producer-strains

Add source-pinned producer strain rows to curation/mibig_producer_strains.tsv for BGC0000404:1 (expected_source_row_sha256 9460d29fcad2b7ecb913298bc80838656966e219ec0654094d28b71942eaeb19, taxon_id NCBITaxon:5076, strain AS-P-78, reference DOI:10.1016/j.fgb.2006.03.001) and BGC0000405:1..3 (expected_source_row_sha256s 50cbd967cf8076f7cbfa5a77bbb9b2910e1e37593d10edea50ad6c3a83316de1, ae975df0e01f81b73c2e119b776207ca3e0f061375585a06ceef3f099dbbe860, and 847cf368dc26e162604ac12681781efc5814bcc31c4e19e94b09578562a1dd42, taxon_id NCBITaxon:5076, strain Wisconsin 54-1255, reference DOI:10.1016/j.fgb.2007.03.008), then re-seed via scripts/seed_from_sources.py.

- Verify exact_source_row_sha256 pins for BGC0000404:1 and BGC0000405:1..3 in curation/mibig_producer_strains.tsv.
- Run scripts/seed_from_sources.py and confirm Wisconsin 54-1255 on CHEBI:58572 and CHEBI:18165, and both AS-P-78 and Wisconsin 54-1255 on CHEBI:51765.
- Verify zero regressions across scripts/validate_strict.py and scripts/verify_corpus.py.

### route-bgc0000404-bgc0000405-claim-references

Add source-pinned claim-reference overrides to curation/mibig_claim_references.tsv for BGC0000404:1 (expected_source_row_sha256 9460d29fcad2b7ecb913298bc80838656966e219ec0654094d28b71942eaeb19, routing producer_reference to DOI:10.1016/j.fgb.2006.03.001, locus_reference to https://www.ebi.ac.uk/ena/browser/view/DQ192518.1, and preserving source_reference DOI:10.1016/s0140-6736(00)87452-8) and BGC0000405:1..3 (expected_source_row_sha256s 50cbd967cf8076f7cbfa5a77bbb9b2910e1e37593d10edea50ad6c3a83316de1, ae975df0e01f81b73c2e119b776207ca3e0f061375585a06ceef3f099dbbe860, and 847cf368dc26e162604ac12681781efc5814bcc31c4e19e94b09578562a1dd42, routing producer_reference to DOI:10.1016/j.fgb.2007.03.008, locus_reference to https://www.ebi.ac.uk/ena/browser/view/EF601124.1, and preserving source_reference PMID:1368505), then re-seed via scripts/seed_from_sources.py.

- Verify expected_source_row_sha256 pins for BGC0000404:1 and BGC0000405:1..3 in curation/mibig_claim_references.tsv.
- Re-seed the 3 cohort records via scripts/seed_from_sources.py and confirm producer and locus claims cite Fierro et al. 2006 / DQ192518.1 and van den Berg et al. 2007 / EF601124.1 with CURATOR_INFERENCE routing provenance while preserving Chain et al. 1940 and Smith et al. 1990 as additional evidence.
- Verify scripts/validate_strict.py and scripts/verify_corpus.py pass with zero errors.

### preserve-salt-and-protonation-state-boundaries

Retain exact ChEBI 3-star structure identities (CHEBI:58572, CHEBI:18165, CHEBI:51765) and keep OPEN discussions until open issue #1015 (counterion-stripped parent/conjugate-acid matching for terminal biosynthetic_pathway products) or an explicit structure-normalization policy is adopted.

- Do not alter locked PATHS.tsv identifiers CHEBI:58572, CHEBI:18165, or CHEBI:51765 without an explicit structure correction decision.
- Track PenDE (RHEA:19809 / UniProtKB:P15802) terminal-product salt-matching under open issue #1015.

## Category Boundaries

- retain: CHEBI:58572, CHEBI:18165, CHEBI:51765. All three cohort records represent distinct, sequential chemical entities in the Penicillium chrysogenum penicillin biosynthetic pathway with distinct 3-star ChEBI groundings and Standard InChIKeys: linear tripeptide intermediate L-delta-(alpha-aminoadipoyl)-L-cysteinyl-D-valine monoanion (CHEBI:58572, BYEIJZFKOAXBBV-ATZCPNFKSA-M), bicyclic beta-lactam intermediate isopenicillin N (CHEBI:18165, LFKDJXLFVZGSFA-PFFMAATASA-N), and phenylacetylated penicillin G sodium salt (CHEBI:51765, FCPVYOBCFFNJFS-LQDWTQKMSA-M).

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| cohort-owners | data/natural_products/PATHS.tsv; n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml (sha256 369d888b75ac4cbe1c1c95a8fb6a7e15c27cb97d27d69875a1e1b83599e3bbd5), isopenicillin-n.yaml (sha256 02dfa271ed3ca87f0cdcaea0b0e701ec1fab935d3a5f559d6955565193bbdf75), benzylpenicillin-sodium.yaml (sha256 201779de13d90f23e3ec700c3bd7dbaa46cacd9a0f74d87638b35eb5e51a5bf2) at 508e90d99e8e8cb7627eb8c885d535be25873c7f | supports | All 3 cohort YAML files are present at their locked PATHS.tsv locations under AMINO_ACIDS_AND_PEPTIDES with distinct 3-star ChEBI identifiers, valid LinkML structure, and SEEDED curation status. |
| mibig-inventory | data/raw/mibig_compounds.tsv; BGC0000404:1 (sha256 9460d29fcad2b7ecb913298bc80838656966e219ec0654094d28b71942eaeb19), BGC0000405:1 (sha256 50cbd967cf8076f7cbfa5a77bbb9b2910e1e37593d10edea50ad6c3a83316de1), BGC0000405:2 (sha256 ae975df0e01f81b73c2e119b776207ca3e0f061375585a06ceef3f099dbbe860), BGC0000405:3 (sha256 847cf368dc26e162604ac12681781efc5814bcc31c4e19e94b09578562a1dd42) | partial | MIBiG 4.0 exports species-level NCBITaxon:5076 (Penicillium chrysogenum) across BGC0000404:1 (DQ192518.1:17440..28759, entry citation doi:10.1016/s0140-6736(00)87452-8) and BGC0000405:1..3 (EF601124.1:22186..33473, entry citation pubmed:1368505), encoding monoanionic ACV (CHEBI:58572) on BGC0000405:1 and benzylpenicillin sodium (CHEBI:51765) on BGC0000404:1 and BGC0000405:3. |
| chebi-structures | data/raw/chebi_structures.tsv; CHEBI:58572 (sha256 6c786965d739422251e36fdab5d46757c87789d4961c22245f89dd586c09fc15), CHEBI:28496 (sha256 11a3d4328707a9971ba51c36d884ff379d96d74019363828f5899ffc2366c97d), CHEBI:18165 (sha256 587eda2b75e08388e80fd2ffd0f738f11392cbc3275beb64f33901e6a79036c7), CHEBI:58399 (sha256 c92bb361e5670a7925d5ff560dffc4022a1f2a923f7a4cd012152e051e92a686), CHEBI:51765 (sha256 0eec0515d861443a7c6e4eaa372db4618b6ad6a8fa7d00f23f2605806c5cc7d0), CHEBI:18208 (sha256 3a01dd984ebebd9179def226a372014e96b2d318adc4f42ffc7340d9bffbcf71), CHEBI:51354 (sha256 44eeba25b3eecd8f4b84007094a4a2ca92eb78310d1375883613988624172684) | supports | ChEBI 3-star structures confirm exact InChIKey matches for CHEBI:58572 (BYEIJZFKOAXBBV-ATZCPNFKSA-M, monoanionic ACV vs neutral CHEBI:28496 BYEIJZFKOAXBBV-ATZCPNFKSA-N), CHEBI:18165 (LFKDJXLFVZGSFA-PFFMAATASA-N, neutral isopenicillin N vs monoanionic CHEBI:58399 LFKDJXLFVZGSFA-PFFMAATASA-M), and CHEBI:51765 (FCPVYOBCFFNJFS-LQDWTQKMSA-M, benzylpenicillin sodium vs neutral CHEBI:18208 JGSARLDLIJGVTE-MBNYWOFBSA-N and monoanionic CHEBI:51354 JGSARLDLIJGVTE-MBNYWOFBSA-M). |
| ena-dq192518-fgb2006 | DOI:10.1016/j.fgb.2006.03.001; Fierro et al., Fungal Genet. Biol. 2006;43(9):618-629 (PMID:16713314) and INSDC DQ192518.1 source feature (1..56820) | supports | INSDC DQ192518.1 and its primary publication Fierro et al. (2006, PMID:16713314, DOI:10.1016/j.fgb.2006.03.001) characterize the 56.8 kb amplified penicillin cluster region (pcbAB-pcbC-penDE at 17440..28759) in Penicillium chrysogenum industrial strain AS-P-78, whereas MIBiG BGC0000404.4 attaches only Chain et al. (1940, Lancet, DOI:10.1016/s0140-6736(00)87452-8, COMPOUND_BIOACTIVITY). |
| ena-ef601124-fgb2007 | DOI:10.1016/j.fgb.2007.03.008; van den Berg et al., Fungal Genet. Biol. 2007;44(9):830-844 (PMID:17548217) and INSDC EF601124.1 source feature (1..59497) | supports | INSDC EF601124.1 and its primary publication van den Berg et al. (2007, PMID:17548217, DOI:10.1016/j.fgb.2007.03.008) characterize the 59.5 kb penicillin biosynthetic gene cluster region (pcbAB-pcbC-penDE at 22186..33473) in Penicillium chrysogenum strain Wisconsin 54-1255, whereas MIBiG BGC0000405.4 attaches Smith et al. (1990, Biotechnology 8:39-41, PMID:1368505, DOI:10.1038/nbt0190-39). |
| smith-1990-pmid1368505 | PMID:1368505; Smith et al., Biotechnology (N Y). 1990;8(1):39-41 (DOI:10.1038/nbt0190-39) | supports | Smith et al. (1990) demonstrate heterologous expression of a Penicillium chrysogenum cosmid clone containing the penicillin biosynthetic gene cluster in Neurospora crassa and Aspergillus niger (supporting HETEROLOGOUS_EXPRESSION on the pathway), published 17 years prior to the 2007 EF601124.1 sequence submission from strain Wisconsin 54-1255. |
| corpus-worklist | scripts/curation_worklist.py; Full-corpus checkpoint: 3,116 natural product owners (282 with inline causal_graphs, 27 with causal_graph_refs) and 246 standalone causal graph components (3,362 total YAML records) at 508e90d99e8e8cb7627eb8c885d535be25873c7f | supports | Deterministic worklist, lockfile, and graph-component checks confirm 3,116 valid owner records and 246 standalone causal graph components (8,924 worklist items across 12 queues), with all 3 penicillin cohort members in SEEDED status. |

## Limits And Additional Notes

- Stage 4 is strictly read-only with respect to scientific YAML records and curation TSVs; all proposed curation edits are preserved as open findings for Stage 5 grouped remediation.
- Full-corpus deterministic checks (verify_corpus.py, validate_id_label_correspondence.py, curation_worklist.py --review-records, pytest tests/test_graph_components.py) audited all 3,116 owners and 246 standalone causal graph components (3,362 total YAML records), while claim-by-claim primary literature verification in this bundle was scoped to the 3-record Penicillium chrysogenum penicillin cohort.
- Terminal biosynthetic_pathway curation of PenDE (UniProtKB:P15802, RHEA:19809) on benzylpenicillin-sodium.yaml (CHEBI:51765) remains blocked by open issue #1015 because RHEA:19809 produces benzylpenicillin(1-) (CHEBI:51354) rather than the sodium salt (CHEBI:51765).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261023T115930Z-penicillium-chrysogenum-penicillin-cohort
kind: category
repository: CultureBotAI/NaturalProductMech
title: Penicillium chrysogenum penicillin biosynthetic cohort review (BGC0000404 and
  BGC0000405)
started_at: '2026-10-23T11:43:00.000000Z'
finished_at: '2026-10-23T11:59:30.000000Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: self_review
  independence_basis: Same cycle campaign agent auditing the frozen post-Stage-3 corpus
    inventory; not an external human review.
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: SEEDED retained across all 3 cohort records; AS-P-78 and Wisconsin
  54-1255 producer strain qualifications and BGC0000404:1 / BGC0000405:1..3 claim-reference
  routings queued for Stage 5
scientific_review: true
summary: 'Full 3-record category review of the Penicillium chrysogenum penicillin
  biosynthetic cohort seeded from MIBiG BGC0000404 (DQ192518.1) and BGC0000405 (EF601124.1):
  N-[(5S)-5-ammonio-5-carboxylatopentanoyl]-L-cysteinyl-D-valinate (CHEBI:58572, n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml),
  isopenicillin N (CHEBI:18165, isopenicillin-n.yaml), and benzylpenicillin sodium
  (CHEBI:51765, benzylpenicillin-sodium.yaml), anchored to a full-corpus deterministic
  checkpoint of all 3,116 natural product owners (282 with inline causal_graphs and
  27 with causal_graph_refs) and 246 standalone causal graph components (3,362 total
  YAML records). Confirms verified Cycle 2 Stage 2/3 ACVS (P26046) and IPNS (P08703)
  biosynthetic steps and UniProtKB protein groundings on CHEBI:58572 and CHEBI:18165,
  while identifying three open findings for Stage 5 grouped remediation: (1) missing
  producer strain qualifications AS-P-78 on BGC0000404:1 (DQ192518.1, Fierro et al.
  2006 DOI:10.1016/j.fgb.2006.03.001) and Wisconsin 54-1255 on BGC0000405:1..3 (EF601124.1,
  van den Berg et al. 2007 DOI:10.1016/j.fgb.2007.03.008) (F-PEN-001), (2) misrouted
  claim-level citations attaching Chain et al. 1940 (DOI:10.1016/s0140-6736(00)87452-8)
  to the 2005/2006 DQ192518.1 locus/producer claims on BGC0000404:1 and Smith et al.
  1990 (PMID:1368505) to the 2007 EF601124.1 locus/producer claims on BGC0000405:1..3
  (F-PEN-002), and (3) upstream MIBiG salt and protonation-state encoding boundaries
  on CHEBI:51765 (sodium salt FCPVYOBCFFNJFS-LQDWTQKMSA-M vs neutral benzylpenicillin
  CHEBI:18208 / CHEBI:17334, blocking PenDE RHEA:19809 pathway curation tracked in
  #1015) and CHEBI:58572 (monoanion vs neutral ACV CHEBI:28496) (F-PEN-003).'
source:
  git_revision: 508e90d99e8e8cb7627eb8c885d535be25873c7f
  state: git_commit
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9
    role: context
  - path: .claude/skills/review-yaml-category/SKILL.md
    sha256: 645746a86769610457ad445361746d6d5ccccdd29ddf29fc1ff256d419ff70de
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
  - path: conf/sibling_pins.yaml
    sha256: 39a1d007ee65ba546567e8a34b7a309f75270b872809e1f783fe1fcee55866f2
    role: context
  - path: curation/decisions.tsv
    sha256: 7214a74975fb2cb65521da18dd14ea1c65665f50060106976dc0db9caf887805
    role: context
  - path: curation/lotus_occurrence_exclusions.tsv
    sha256: d1778f304b83256e756a3aec99f4fd67b5a5d2aee3ca32f88dd0418592f8a30d
    role: context
  - path: curation/mibig_claim_references.tsv
    sha256: 6a9594c1159fc8038b59f8d421efd15dfb3d748e8e6d508b8f7fb84c43abe09b
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: 7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e
    role: context
  - path: curation/mibig_producer_isolates.tsv
    sha256: 8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: 8879da121435bf96833919d8300031745197ee78a527d602b233dcd1dde23268
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
  - path: data/natural_products/amino_acids_and_peptides/benzylpenicillin-sodium.yaml
    sha256: 201779de13d90f23e3ec700c3bd7dbaa46cacd9a0f74d87638b35eb5e51a5bf2
    role: target
  - path: data/natural_products/amino_acids_and_peptides/isopenicillin-n.yaml
    sha256: 02dfa271ed3ca87f0cdcaea0b0e701ec1fab935d3a5f559d6955565193bbdf75
    role: target
  - path: data/natural_products/amino_acids_and_peptides/n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml
    sha256: 369d888b75ac4cbe1c1c95a8fb6a7e15c27cb97d27d69875a1e1b83599e3bbd5
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
    sha256: ee8f572f191ee2bc92a18ed57b115faca186d56c6f7dab38ef7521c1473de31d
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
  - path: scripts/curation_worklist.py
    sha256: 913508ca8df2eb5c037cd9e4769b14b027869ab78c7306f33b59e1c7e383a1c3
    role: context
  - path: scripts/extract_mibig.py
    sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/seed_from_sources.py
    sha256: b992853ea5e476fa27937bd6641ebe9b266f178215572e45d16ba597115e250d
    role: context
  - path: scripts/validate_id_label_correspondence.py
    sha256: b5ff41bb52d24f5d7819fb12769e216440f75ec3fb3df3e3cb2c5082fffb40e0
    role: context
  - path: scripts/validate_strict.py
    sha256: e9b844d10fb7d2889521677716098da5883c7fd7d3c887a5cb600b87bbca0c21
    role: context
  - path: scripts/verify_corpus.py
    sha256: 3e79d6e18e43010a84e2ef7857625655185796d447ee12979a94cd836d756b60
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
  - path: src/naturalproductmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/naturalproductmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
targets:
- target_id: CHEBI:58572
  path: data/natural_products/amino_acids_and_peptides/n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml
  label: N-[(5S)-5-ammonio-5-carboxylatopentanoyl]-L-cysteinyl-D-valinate
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/amino_acids_and_peptides/n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml
    role: Generated natural product owner record
- target_id: CHEBI:18165
  path: data/natural_products/amino_acids_and_peptides/isopenicillin-n.yaml
  label: isopenicillin N
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/amino_acids_and_peptides/isopenicillin-n.yaml
    role: Generated natural product owner record
- target_id: CHEBI:51765
  path: data/natural_products/amino_acids_and_peptides/benzylpenicillin-sodium.yaml
  label: benzylpenicillin sodium
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/antibioticmech_inchikeys.tsv
    role: Pinned AntibioticMech cross-reference table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/amino_acids_and_peptides/benzylpenicillin-sodium.yaml
    role: Generated natural product owner record
scope:
  description: Coherent 3-record biosynthetic and chemical-identity cohort covering
    all NaturalProductMech records seeded from the Penicillium chrysogenum penicillin
    biosynthetic gene clusters MIBiG BGC0000404 (DQ192518.1) and BGC0000405 (EF601124.1),
    evaluated alongside frozen full-corpus inventory checks (3,116 owner YAML records
    and 246 standalone causal graph components; 3,362 total YAML records).
  selection: All records derived from the Penicillium chrysogenum penicillin biosynthetic
    gene cluster deposits BGC0000404:1 and BGC0000405:1..3, selected to audit the
    newly curated Cycle 2 Stage 2/3 ACVS (P26046) and IPNS (P08703) biosynthetic steps,
    the blocked PenDE step on benzylpenicillin-sodium.yaml (#1015), and cohort-wide
    producer strain and claim-reference provenance.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  exclusions:
  - target: Remaining 3,113 natural product owner records and 246 standalone causal
      graph components in the frozen 3,362-file corpus inventory
    reason: Audited at the corpus-checkpoint level via verify_corpus.py, validate_id_label_correspondence.py,
      curation_worklist.py --review-records, and pytest tests/test_graph_components.py;
      excluded from this 3-record Penicillium chrysogenum penicillin cohort denominator
      to preserve per-target scientific review depth.
checks:
- check_id: inspect-cohort
  name: Native source inspection (cohort)
  status: passed
  required: true
  command: .venv/bin/python scripts/record_review.py inspect --targets /tmp/c2_s4_cohort_targets.yaml
    --input data/raw/mibig_compounds.tsv --input data/raw/chebi_structures.tsv --input
    curation/mibig_producer_strains.tsv --input curation/mibig_claim_references.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  evidence_ids:
  - cohort-owners
  summary: Captured exact Git base 508e90d99e8e8cb7627eb8c885d535be25873c7f and verified
    SHA256 digests for all 3 cohort target YAML files and raw/curation TSV inputs.
  scope_note: 2026-10-23T11:50:37Z..2026-10-23T11:50:39Z; output SHA256 740c4e12dba39dd818e5ce537f9c38189c1ce2561b6d3c29ce4bdc462d188718
- check_id: strict-cohort
  name: Strict schema and semantic validation (cohort)
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py --out /tmp/c2_s4_strict_cohort.tsv
    data/natural_products/amino_acids_and_peptides/n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml
    data/natural_products/amino_acids_and_peptides/isopenicillin-n.yaml data/natural_products/amino_acids_and_peptides/benzylpenicillin-sodium.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  evidence_ids:
  - cohort-owners
  summary: All 3 cohort YAML files passed strict LinkML and semantic validation with
    0 ERROR rows.
  scope_note: 2026-10-23T11:49:17Z..2026-10-23T11:49:21Z; output SHA256 9820169a25fe0b3fae3a4d4ba68f37ed01b707a5998f55db727b8404348c5e0e
- check_id: verify-corpus
  name: Full-corpus lockfile and filing verification
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py --summary
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  evidence_ids:
  - corpus-worklist
  summary: Verified lockfile integrity across all 3,116 natural product owner records
    against data/natural_products/PATHS.tsv.
  scope_note: 2026-10-23T11:43:47Z..2026-10-23T11:45:08Z; output SHA256 c9bcf7add9c5022125581df2e6b486735cd23803e49b73a4a2d6a60b62eebc5e
- check_id: validate-id-labels
  name: Full-corpus ontology ID-label correspondence
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py --report /tmp/c2_s4_id_label.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  evidence_ids:
  - chebi-structures
  - mibig-inventory
  summary: Full-corpus ID-label check passed with 0 ERROR rows (13,465 OK_CANONICAL,
    655 OK_SYNONYM, 35 OK_EXCEPTION, 0 ID_NOT_FOUND, 499 warn-only taxon_labels mismatches);
    all ChEBI, NCBITaxon, UniProtKB, GO, and RHEA terms on the 3 cohort records resolve
    canonically.
  scope_note: 2026-10-23T11:57:04Z..2026-10-23T11:58:58Z; output SHA256 c8bb404d2189463dd173a7ddea6b48893bdba5af63321842dac90984211f41c3
- check_id: review-queue
  name: Exhaustive corpus review-queue checkpoint
  status: passed
  required: true
  command: .venv/bin/python scripts/curation_worklist.py --review-records --limit
    5
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  evidence_ids:
  - corpus-worklist
  summary: 'Computed exhaustive review-records queue across all 3,116 corpus owners
    (8,924 rows across 12 queues: producer-evidence 2,292; biosynthesis 1,184; structure-disagreement
    5; name-disagreement 67; unnamed-producer 39; shared-structure 207; needs-a-name
    18; occurrence-only 12; pathway-ambiguous 620; unresolved-taxa 3,329; stereo-incomplete
    1,124; record-review 27). All 3 cohort records appear in producer-evidence; CHEBI:58572
    and CHEBI:51765 appear in name-disagreement; CHEBI:51765 additionally appears
    in biosynthesis and shared-structure.'
  scope_note: 2026-10-23T11:47:22Z..2026-10-23T11:48:07Z; output SHA256 7edbdc274466a876b3ef923cd3fa7c5a711f1f6aa3119d96c43ef85c7c768c31
- check_id: local-search
  name: Repository-wide identifier and BGC cross-reference search
  status: passed
  required: true
  command: git grep -l -E 'BGC0000404|BGC0000405|CHEBI:58572|CHEBI:18165|CHEBI:51765|DQ192518|EF601124'
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  summary: Verified all 33 repository file references to BGC0000404, BGC0000405, DQ192518.1,
    EF601124.1, and cohort identifiers across raw inventories, curation tables, records,
    and pages.
  scope_note: 2026-10-23T11:59:23Z..2026-10-23T11:59:25Z; output SHA256 0647b3745f650c6146b5a6ce8feba176040639d2102c3a6a4f9d55651f8be290
- check_id: test-graph-components
  name: Full-corpus standalone causal graph component validation
  status: passed
  required: true
  command: .venv/bin/python -m pytest -q tests/test_graph_components.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  evidence_ids:
  - corpus-worklist
  summary: Validated all 246 standalone causal graph component YAML files under data/causal_graphs/
    (40 passed, 0 failed).
  scope_note: 2026-10-23T11:46:26Z..2026-10-23T11:47:22Z; output SHA256 b5a96643be6dd236e181473fa1bbb15fbe22452a95447e99ddc4b6b0a949d7a2
evidence:
- evidence_id: cohort-owners
  kind: record_content
  reference: data/natural_products/PATHS.tsv
  locator: n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml (sha256
    369d888b75ac4cbe1c1c95a8fb6a7e15c27cb97d27d69875a1e1b83599e3bbd5), isopenicillin-n.yaml
    (sha256 02dfa271ed3ca87f0cdcaea0b0e701ec1fab935d3a5f559d6955565193bbdf75), benzylpenicillin-sodium.yaml
    (sha256 201779de13d90f23e3ec700c3bd7dbaa46cacd9a0f74d87638b35eb5e51a5bf2) at 508e90d99e8e8cb7627eb8c885d535be25873c7f
  accessed_at: '2026-10-23T11:50:39.000000Z'
  support: supports
  snapshot_sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
  summary: All 3 cohort YAML files are present at their locked PATHS.tsv locations
    under AMINO_ACIDS_AND_PEPTIDES with distinct 3-star ChEBI identifiers, valid LinkML
    structure, and SEEDED curation status.
- evidence_id: mibig-inventory
  kind: database
  reference: data/raw/mibig_compounds.tsv
  locator: BGC0000404:1 (sha256 9460d29fcad2b7ecb913298bc80838656966e219ec0654094d28b71942eaeb19),
    BGC0000405:1 (sha256 50cbd967cf8076f7cbfa5a77bbb9b2910e1e37593d10edea50ad6c3a83316de1),
    BGC0000405:2 (sha256 ae975df0e01f81b73c2e119b776207ca3e0f061375585a06ceef3f099dbbe860),
    BGC0000405:3 (sha256 847cf368dc26e162604ac12681781efc5814bcc31c4e19e94b09578562a1dd42)
  accessed_at: '2026-10-23T11:50:39.000000Z'
  support: partial
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
  summary: MIBiG 4.0 exports species-level NCBITaxon:5076 (Penicillium chrysogenum)
    across BGC0000404:1 (DQ192518.1:17440..28759, entry citation doi:10.1016/s0140-6736(00)87452-8)
    and BGC0000405:1..3 (EF601124.1:22186..33473, entry citation pubmed:1368505),
    encoding monoanionic ACV (CHEBI:58572) on BGC0000405:1 and benzylpenicillin sodium
    (CHEBI:51765) on BGC0000404:1 and BGC0000405:3.
- evidence_id: chebi-structures
  kind: database
  reference: data/raw/chebi_structures.tsv
  locator: CHEBI:58572 (sha256 6c786965d739422251e36fdab5d46757c87789d4961c22245f89dd586c09fc15),
    CHEBI:28496 (sha256 11a3d4328707a9971ba51c36d884ff379d96d74019363828f5899ffc2366c97d),
    CHEBI:18165 (sha256 587eda2b75e08388e80fd2ffd0f738f11392cbc3275beb64f33901e6a79036c7),
    CHEBI:58399 (sha256 c92bb361e5670a7925d5ff560dffc4022a1f2a923f7a4cd012152e051e92a686),
    CHEBI:51765 (sha256 0eec0515d861443a7c6e4eaa372db4618b6ad6a8fa7d00f23f2605806c5cc7d0),
    CHEBI:18208 (sha256 3a01dd984ebebd9179def226a372014e96b2d318adc4f42ffc7340d9bffbcf71),
    CHEBI:51354 (sha256 44eeba25b3eecd8f4b84007094a4a2ca92eb78310d1375883613988624172684)
  accessed_at: '2026-10-23T11:50:39.000000Z'
  support: supports
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
  summary: ChEBI 3-star structures confirm exact InChIKey matches for CHEBI:58572
    (BYEIJZFKOAXBBV-ATZCPNFKSA-M, monoanionic ACV vs neutral CHEBI:28496 BYEIJZFKOAXBBV-ATZCPNFKSA-N),
    CHEBI:18165 (LFKDJXLFVZGSFA-PFFMAATASA-N, neutral isopenicillin N vs monoanionic
    CHEBI:58399 LFKDJXLFVZGSFA-PFFMAATASA-M), and CHEBI:51765 (FCPVYOBCFFNJFS-LQDWTQKMSA-M,
    benzylpenicillin sodium vs neutral CHEBI:18208 JGSARLDLIJGVTE-MBNYWOFBSA-N and
    monoanionic CHEBI:51354 JGSARLDLIJGVTE-MBNYWOFBSA-M).
- evidence_id: ena-dq192518-fgb2006
  kind: primary_source
  reference: DOI:10.1016/j.fgb.2006.03.001
  locator: Fierro et al., Fungal Genet. Biol. 2006;43(9):618-629 (PMID:16713314) and
    INSDC DQ192518.1 source feature (1..56820)
  accessed_at: '2026-10-23T11:52:48.000000Z'
  support: supports
  summary: INSDC DQ192518.1 and its primary publication Fierro et al. (2006, PMID:16713314,
    DOI:10.1016/j.fgb.2006.03.001) characterize the 56.8 kb amplified penicillin cluster
    region (pcbAB-pcbC-penDE at 17440..28759) in Penicillium chrysogenum industrial
    strain AS-P-78, whereas MIBiG BGC0000404.4 attaches only Chain et al. (1940, Lancet,
    DOI:10.1016/s0140-6736(00)87452-8, COMPOUND_BIOACTIVITY).
- evidence_id: ena-ef601124-fgb2007
  kind: primary_source
  reference: DOI:10.1016/j.fgb.2007.03.008
  locator: van den Berg et al., Fungal Genet. Biol. 2007;44(9):830-844 (PMID:17548217)
    and INSDC EF601124.1 source feature (1..59497)
  accessed_at: '2026-10-23T11:52:48.000000Z'
  support: supports
  summary: INSDC EF601124.1 and its primary publication van den Berg et al. (2007,
    PMID:17548217, DOI:10.1016/j.fgb.2007.03.008) characterize the 59.5 kb penicillin
    biosynthetic gene cluster region (pcbAB-pcbC-penDE at 22186..33473) in Penicillium
    chrysogenum strain Wisconsin 54-1255, whereas MIBiG BGC0000405.4 attaches Smith
    et al. (1990, Biotechnology 8:39-41, PMID:1368505, DOI:10.1038/nbt0190-39).
- evidence_id: smith-1990-pmid1368505
  kind: primary_source
  reference: PMID:1368505
  locator: Smith et al., Biotechnology (N Y). 1990;8(1):39-41 (DOI:10.1038/nbt0190-39)
  accessed_at: '2026-10-23T11:52:48.000000Z'
  support: supports
  summary: Smith et al. (1990) demonstrate heterologous expression of a Penicillium
    chrysogenum cosmid clone containing the penicillin biosynthetic gene cluster in
    Neurospora crassa and Aspergillus niger (supporting HETEROLOGOUS_EXPRESSION on
    the pathway), published 17 years prior to the 2007 EF601124.1 sequence submission
    from strain Wisconsin 54-1255.
- evidence_id: corpus-worklist
  kind: validation
  reference: scripts/curation_worklist.py
  locator: 'Full-corpus checkpoint: 3,116 natural product owners (282 with inline
    causal_graphs, 27 with causal_graph_refs) and 246 standalone causal graph components
    (3,362 total YAML records) at 508e90d99e8e8cb7627eb8c885d535be25873c7f'
  accessed_at: '2026-10-23T11:54:54.000000Z'
  support: supports
  snapshot_sha256: 913508ca8df2eb5c037cd9e4769b14b027869ab78c7306f33b59e1c7e383a1c3
  summary: Deterministic worklist, lockfile, and graph-component checks confirm 3,116
    valid owner records and 246 standalone causal graph components (8,924 worklist
    items across 12 queues), with all 3 penicillin cohort members in SEEDED status.
assessments:
- assessment_id: cohort-identity-and-biosynthesis
  area: identity
  topic: Chemical structure grounding and Cycle 2 Stage 2/3 ACVS/IPNS biosynthetic
    pathway verification
  outcome: supported
  summary: All three cohort records ground to distinct 3-star ChEBI entries (CHEBI:58572,
    CHEBI:18165, CHEBI:51765) and file under AMINO_ACIDS_AND_PEPTIDES in exact agreement
    with data/natural_products/PATHS.tsv. The Cycle 2 Stage 2/3 biosynthetic_pathway
    steps on CHEBI:58572 (ACVS / pcbAB, UniProtKB:P26046, RHEA:23620, PMID:2125231
    / PMID:1849983) and CHEBI:18165 (ACVS P26046 -> IPNS / pcbC, UniProtKB:P08703,
    RHEA:16689, PMID:3001640) are accurately grounded to Penicillium chrysogenum (NCBITaxon:5076)
    and pass strict LinkML and ontology ID-label validation.
  target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  evidence_ids:
  - cohort-owners
  - chebi-structures
  - corpus-worklist
- assessment_id: chrysogenum-producer-strains
  area: completeness
  topic: Missing AS-P-78 (BGC0000404:1) and Wisconsin 54-1255 (BGC0000405:1..3) producer
    strain qualifications
  outcome: concern
  summary: All four Penicillium chrysogenum (NCBITaxon:5076) producer_organisms claims
    across the 3 cohort records omit producer_organisms[*].strain because MIBiG 4.0
    exports species-level organism_name='Penicillium chrysogenum'. INSDC DQ192518.1
    and Fierro et al. (2006, DOI:10.1016/j.fgb.2006.03.001, PMID:16713314) explicitly
    identify strain AS-P-78 for BGC0000404:1 (benzylpenicillin-sodium.yaml), and INSDC
    EF601124.1 and van den Berg et al. (2007, DOI:10.1016/j.fgb.2007.03.008, PMID:17548217)
    explicitly identify strain Wisconsin 54-1255 for BGC0000405:1..3 (all 3 cohort
    records).
  target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - ena-dq192518-fgb2006
  - ena-ef601124-fgb2007
- assessment_id: chrysogenum-claim-reference-routing
  area: provenance
  topic: Misrouted entry-level citations on BGC0000404:1 (DQ192518.1) and BGC0000405:1..3
    (EF601124.1)
  outcome: concern
  summary: 'On benzylpenicillin-sodium.yaml (BGC0000404:1), producer_organisms[0].evidence[0].reference
    and biosynthetic_gene_clusters[0].evidence[0].reference (genbank:DQ192518.1) cite
    Chain et al. (1940, Lancet, DOI:10.1016/s0140-6736(00)87452-8, reference_basis:
    COMPOUND_BIOACTIVITY), published 65 years before the 2005/2006 DQ192518.1 sequence
    deposit from strain AS-P-78 (Fierro et al. 2006, DOI:10.1016/j.fgb.2006.03.001).
    On all three BGC0000405 records (BGC0000405:1..3), producer_organisms and biosynthetic_gene_clusters
    (genbank:EF601124.1) cite Smith et al. (1990, PMID:1368505), published 17 years
    before the 2007 EF601124.1 sequence deposit from strain Wisconsin 54-1255 (van
    den Berg et al. 2007, DOI:10.1016/j.fgb.2007.03.008).'
  target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - ena-dq192518-fgb2006
  - ena-ef601124-fgb2007
  - smith-1990-pmid1368505
- assessment_id: salt-and-protonation-state-boundary
  area: representation
  topic: Upstream MIBiG salt and protonation-state encoding on CHEBI:51765 and CHEBI:58572
  outcome: concern
  summary: 'MIBiG BGC0000404:1 and BGC0000405:3 supply the sodium carboxylate salt
    SMILES for compound_name=''benzylpenicillin'' (grounding to CHEBI:51765 benzylpenicillin
    sodium, FCPVYOBCFFNJFS-LQDWTQKMSA-M, rather than neutral benzylpenicillin CHEBI:18208
    / CHEBI:17334 JGSARLDLIJGVTE-MBNYWOFBSA-N or monoanion CHEBI:51354 JGSARLDLIJGVTE-MBNYWOFBSA-M),
    which triggers OPEN name-disagreement and shared-structure discussions and blocks
    RHEA:19809 (PenDE / UniProtKB:P15802) pathway curation on benzylpenicillin-sodium.yaml
    (tracked in open issue #1015). Similarly, BGC0000405:1 encodes monoanionic ACV
    (CHEBI:58572, BYEIJZFKOAXBBV-ATZCPNFKSA-M) rather than neutral ACV (CHEBI:28496,
    BYEIJZFKOAXBBV-ATZCPNFKSA-N), triggering an OPEN name-disagreement discussion.'
  target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - chebi-structures
findings:
- finding_id: F-PEN-001
  issue_key: penicillium-chrysogenum-bgc0000404-bgc0000405-producer-strains-missing
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Missing AS-P-78 (BGC0000404:1) and Wisconsin 54-1255 (BGC0000405:1..3) producer
    strain qualifications on Penicillium chrysogenum records
  description: All four Penicillium chrysogenum (NCBITaxon:5076) producer_organisms
    claims seeded from BGC0000404:1 (sha256 9460d29fcad2b7ecb913298bc80838656966e219ec0654094d28b71942eaeb19
    on benzylpenicillin-sodium.yaml) and BGC0000405:1..3 (sha256s 50cbd967cf8076f7cbfa5a77bbb9b2910e1e37593d10edea50ad6c3a83316de1
    on n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml, ae975df0e01f81b73c2e119b776207ca3e0f061375585a06ceef3f099dbbe860
    on isopenicillin-n.yaml, and 847cf368dc26e162604ac12681781efc5814bcc31c4e19e94b09578562a1dd42
    on benzylpenicillin-sodium.yaml) omit producer_organisms[*].strain. INSDC DQ192518.1
    and Fierro et al. (2006, DOI:10.1016/j.fgb.2006.03.001, PMID:16713314) explicitly
    identify strain AS-P-78 for BGC0000404:1, and INSDC EF601124.1 and van den Berg
    et al. (2007, DOI:10.1016/j.fgb.2007.03.008, PMID:17548217) explicitly identify
    strain Wisconsin 54-1255 for BGC0000405:1..3. Notice that on benzylpenicillin-sodium.yaml,
    qualifying BGC0000404:1 as AS-P-78 and BGC0000405:3 as Wisconsin 54-1255 also
    resolves the two distinct sequenced industrial/laboratory strains instead of collapsing
    both clusters onto one unqualified NCBITaxon:5076 producer entry.
  target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  field_paths:
  - producer_organisms[0].strain
  - producer_organisms[0].evidence
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - ena-dq192518-fgb2006
  - ena-ef601124-fgb2007
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  rule_id: review-checklist:producer-strain-qualification
  native_severity: major
  normalization_reason: Omission of explicitly published sequenced producer strains
    AS-P-78 and Wisconsin 54-1255 across four BGC compound rows is a material completeness
    gap resolvable via curation/mibig_producer_strains.tsv.
- finding_id: F-PEN-002
  issue_key: bgc0000404-bgc0000405-anachronistic-claim-reference-routing
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Misrouted entry-level citations on BGC0000404:1 (Chain et al. 1940 on DQ192518.1)
    and BGC0000405:1..3 (Smith et al. 1990 on EF601124.1)
  description: '1) On benzylpenicillin-sodium.yaml (CHEBI:51765), BGC0000404:1 attaches
    DOI:10.1016/s0140-6736(00)87452-8 (Chain et al., 1940, Lancet, reference_basis:
    COMPOUND_BIOACTIVITY) to producer_organisms[0].evidence[0].reference and biosynthetic_gene_clusters[0].evidence[0].reference
    (genbank:DQ192518.1, 17440..28759), even though Chain et al. (1940) pre-date the
    2005/2006 DQ192518.1 sequence deposit from Penicillium chrysogenum AS-P-78 (Fierro
    et al., 2006, DOI:10.1016/j.fgb.2006.03.001, PMID:16713314) by 65 years. 2) Across
    all three BGC0000405 records (CHEBI:58572, CHEBI:18165, CHEBI:51765), BGC0000405:1..3
    attach PMID:1368505 (Smith et al., 1990, Biotechnology 8:39-41, DOI:10.1038/nbt0190-39)
    to producer_organisms and biosynthetic_gene_clusters (genbank:EF601124.1, 22186..33473),
    even though Smith et al. (1990) pre-date the 2007 EF601124.1 sequence deposit
    from Penicillium chrysogenum Wisconsin 54-1255 (van den Berg et al., 2007, DOI:10.1016/j.fgb.2007.03.008,
    PMID:17548217) by 17 years.'
  target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  field_paths:
  - producer_organisms[0].evidence[0].reference
  - biosynthetic_gene_clusters[0].evidence[0].reference
  - biosynthetic_gene_clusters[1].evidence[0].reference
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - ena-dq192518-fgb2006
  - ena-ef601124-fgb2007
  - smith-1990-pmid1368505
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  rule_id: review-checklist:claim-specific-citation-routing
  native_severity: major
  normalization_reason: Attaching 1940 bioactivity and 1990 cosmid papers as direct
    evidence for 2006/2007 genome sequence deposits DQ192518.1 and EF601124.1 misstates
    claim provenance and is directly correctable via curation/mibig_claim_references.tsv.
- finding_id: F-PEN-003
  issue_key: penicillin-cohort-salt-and-protonation-state-boundary
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Upstream MIBiG salt and protonation-state encoding on benzylpenicillin sodium
    (CHEBI:51765) and monoanionic ACV (CHEBI:58572)
  description: '1) MIBiG BGC0000404:1 and BGC0000405:3 supply the sodium salt SMILES
    [H][C@]12SC(C)(C)[C@@H](N1C(=O)[C@H]2NC(=O)Cc1ccccc1)C(=O)[O-].[Na+] (Standard
    InChIKey FCPVYOBCFFNJFS-LQDWTQKMSA-M, grounding to 3-star CHEBI:51765 benzylpenicillin
    sodium) for compound_name=''benzylpenicillin''. Because the biological product
    of isopenicillin N acyltransferase (PenDE / UniProtKB:P15802, RHEA:19809) is benzylpenicillin(1-)
    (CHEBI:51354, JGSARLDLIJGVTE-MBNYWOFBSA-M) / neutral benzylpenicillin (CHEBI:18208
    / CHEBI:17334, JGSARLDLIJGVTE-MBNYWOFBSA-N) and validate_strict.py enforces terminal
    biosynthetic_pathway product grounding against record.identifier (CHEBI:51765),
    PenDE pathway curation on benzylpenicillin-sodium.yaml remains blocked by open
    issue #1015, and OPEN name-disagreement and shared-structure discussions remain
    on the record. 2) MIBiG BGC0000405:1 supplies monoanionic ACV (CHEBI:58572, BYEIJZFKOAXBBV-ATZCPNFKSA-M)
    under the neutral label ''N-(5-amino-5-carboxypentanoyl)-L-cysteinyl-D-valine''
    (neutral CHEBI:28496, BYEIJZFKOAXBBV-ATZCPNFKSA-N), leaving an OPEN name-disagreement
    discussion on n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml.'
  target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  field_paths:
  - identifier
  - chemical_structure.standard_inchi_key
  - chemical_structure.smiles
  - discussions
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - chebi-structures
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  rule_id: review-checklist:exact-structure-and-deposit-boundary
  native_severity: minor
  normalization_reason: Faithful reflection of upstream MIBiG 4.0 salt/ion SMILES
    encoding and strict terminal-product validator invariant (#1015); documented as
    a source/representation boundary.
actions:
- action_id: qualify-chrysogenum-producer-strains
  description: Add source-pinned producer strain rows to curation/mibig_producer_strains.tsv
    for BGC0000404:1 (expected_source_row_sha256 9460d29fcad2b7ecb913298bc80838656966e219ec0654094d28b71942eaeb19,
    taxon_id NCBITaxon:5076, strain AS-P-78, reference DOI:10.1016/j.fgb.2006.03.001)
    and BGC0000405:1..3 (expected_source_row_sha256s 50cbd967cf8076f7cbfa5a77bbb9b2910e1e37593d10edea50ad6c3a83316de1,
    ae975df0e01f81b73c2e119b776207ca3e0f061375585a06ceef3f099dbbe860, and 847cf368dc26e162604ac12681781efc5814bcc31c4e19e94b09578562a1dd42,
    taxon_id NCBITaxon:5076, strain Wisconsin 54-1255, reference DOI:10.1016/j.fgb.2007.03.008),
    then re-seed via scripts/seed_from_sources.py.
  finding_ids:
  - F-PEN-001
  target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Verify exact_source_row_sha256 pins for BGC0000404:1 and BGC0000405:1..3 in curation/mibig_producer_strains.tsv.
  - Run scripts/seed_from_sources.py and confirm Wisconsin 54-1255 on CHEBI:58572
    and CHEBI:18165, and both AS-P-78 and Wisconsin 54-1255 on CHEBI:51765.
  - Verify zero regressions across scripts/validate_strict.py and scripts/verify_corpus.py.
- action_id: route-bgc0000404-bgc0000405-claim-references
  description: Add source-pinned claim-reference overrides to curation/mibig_claim_references.tsv
    for BGC0000404:1 (expected_source_row_sha256 9460d29fcad2b7ecb913298bc80838656966e219ec0654094d28b71942eaeb19,
    routing producer_reference to DOI:10.1016/j.fgb.2006.03.001, locus_reference to
    https://www.ebi.ac.uk/ena/browser/view/DQ192518.1, and preserving source_reference
    DOI:10.1016/s0140-6736(00)87452-8) and BGC0000405:1..3 (expected_source_row_sha256s
    50cbd967cf8076f7cbfa5a77bbb9b2910e1e37593d10edea50ad6c3a83316de1, ae975df0e01f81b73c2e119b776207ca3e0f061375585a06ceef3f099dbbe860,
    and 847cf368dc26e162604ac12681781efc5814bcc31c4e19e94b09578562a1dd42, routing
    producer_reference to DOI:10.1016/j.fgb.2007.03.008, locus_reference to https://www.ebi.ac.uk/ena/browser/view/EF601124.1,
    and preserving source_reference PMID:1368505), then re-seed via scripts/seed_from_sources.py.
  finding_ids:
  - F-PEN-002
  target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Verify expected_source_row_sha256 pins for BGC0000404:1 and BGC0000405:1..3 in
    curation/mibig_claim_references.tsv.
  - Re-seed the 3 cohort records via scripts/seed_from_sources.py and confirm producer
    and locus claims cite Fierro et al. 2006 / DQ192518.1 and van den Berg et al.
    2007 / EF601124.1 with CURATOR_INFERENCE routing provenance while preserving Chain
    et al. 1940 and Smith et al. 1990 as additional evidence.
  - Verify scripts/validate_strict.py and scripts/verify_corpus.py pass with zero
    errors.
- action_id: preserve-salt-and-protonation-state-boundaries
  description: 'Retain exact ChEBI 3-star structure identities (CHEBI:58572, CHEBI:18165,
    CHEBI:51765) and keep OPEN discussions until open issue #1015 (counterion-stripped
    parent/conjugate-acid matching for terminal biosynthetic_pathway products) or
    an explicit structure-normalization policy is adopted.'
  finding_ids:
  - F-PEN-003
  target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  acceptance_checks:
  - Do not alter locked PATHS.tsv identifiers CHEBI:58572, CHEBI:18165, or CHEBI:51765
    without an explicit structure correction decision.
  - 'Track PenDE (RHEA:19809 / UniProtKB:P15802) terminal-product salt-matching under
    open issue #1015.'
boundary_decisions:
- action: retain
  target_ids:
  - CHEBI:58572
  - CHEBI:18165
  - CHEBI:51765
  rationale: 'All three cohort records represent distinct, sequential chemical entities
    in the Penicillium chrysogenum penicillin biosynthetic pathway with distinct 3-star
    ChEBI groundings and Standard InChIKeys: linear tripeptide intermediate L-delta-(alpha-aminoadipoyl)-L-cysteinyl-D-valine
    monoanion (CHEBI:58572, BYEIJZFKOAXBBV-ATZCPNFKSA-M), bicyclic beta-lactam intermediate
    isopenicillin N (CHEBI:18165, LFKDJXLFVZGSFA-PFFMAATASA-N), and phenylacetylated
    penicillin G sodium salt (CHEBI:51765, FCPVYOBCFFNJFS-LQDWTQKMSA-M).'
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - chebi-structures
limitations:
- Stage 4 is strictly read-only with respect to scientific YAML records and curation
  TSVs; all proposed curation edits are preserved as open findings for Stage 5 grouped
  remediation.
- Full-corpus deterministic checks (verify_corpus.py, validate_id_label_correspondence.py,
  curation_worklist.py --review-records, pytest tests/test_graph_components.py) audited
  all 3,116 owners and 246 standalone causal graph components (3,362 total YAML records),
  while claim-by-claim primary literature verification in this bundle was scoped to
  the 3-record Penicillium chrysogenum penicillin cohort.
- 'Terminal biosynthetic_pathway curation of PenDE (UniProtKB:P15802, RHEA:19809)
  on benzylpenicillin-sodium.yaml (CHEBI:51765) remains blocked by open issue #1015
  because RHEA:19809 produces benzylpenicillin(1-) (CHEBI:51354) rather than the sodium
  salt (CHEBI:51765).'
```
