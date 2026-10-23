# Stage 5 Finding Group & GitHub Issue Map (`mech-goal-sequence-20261019`, Cycle 2)

## Consumed Stage 4 Review Artifacts

| Kind | Path | SHA-256 |
| --- | --- | --- |
| `category` | `reviews/structured/20261023T115930Z-penicillium-chrysogenum-penicillin-cohort/review.yaml` | `9eba2af62ddda72739387be4483a87a7fb075673542e01df9e97047fed10f0c9` |
| `record` | `reviews/structured/20261023T115935Z-benzylpenicillin-sodium-record-review/review.yaml` | `561aaed5b6954f981f3ad0a4f8de22a8449ffbc99611eeb1baa61cd132da0d61` |
| `workflow_manifest` | `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/evidence.yaml` | `5d5cca19b7d71a2699c63b8ac23d7122eac3340568b22b24d875e4cf3bb38334` |

## Grouped Findings, Repair Ownership, and GitHub Issue Mapping

| Group ID | Finding IDs | Issue Key | Severity | Status | Repair Owner | GitHub Issue | Target IDs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `G-PEN-001` | `F-PEN-001`, `F-BPEN-001` | `penicillium-chrysogenum-bgc0000404-bgc0000405-producer-strains-missing` | `major` | `resolved` | `curation/mibig_producer_strains.tsv` (+ `scripts/seed_from_sources.py`) | [#1022](https://github.com/CultureBotAI/NaturalProductMech/issues/1022) (`created`, closes with Stage 5 PR) | `CHEBI:58572`, `CHEBI:18165`, `CHEBI:51765` |
| `G-PEN-002` | `F-PEN-002`, `F-BPEN-002` | `bgc0000404-bgc0000405-anachronistic-claim-reference-routing` | `major` | `resolved` | `curation/mibig_claim_references.tsv` (+ `scripts/seed_from_sources.py`) | [#1023](https://github.com/CultureBotAI/NaturalProductMech/issues/1023) (`created`, closes with Stage 5 PR) | `CHEBI:58572`, `CHEBI:18165`, `CHEBI:51765` |
| `G-PEN-003` | `F-PEN-003`, `F-BPEN-003` | `penicillin-cohort-salt-and-protonation-state-boundary` | `minor` | `deferred` | `curation/mibig_structure_corrections.tsv` (+ `src/naturalproductmech/curate/structure_corrections.py`) | [#1015](https://github.com/CultureBotAI/NaturalProductMech/issues/1015) (`reused`, remains `open`) | `CHEBI:58572`, `CHEBI:18165`, `CHEBI:51765` |
| `G-PIK-DES-003` | `F-PIK-DES-003` | `desosamine-cyclic-open-chain-and-bgc0000898-locus-split` | `minor` | `deferred` | `curation/mibig_structure_corrections.tsv` | [#1012](https://github.com/CultureBotAI/NaturalProductMech/issues/1012) (`reused`, remains `open`) | `CHEBI:32540`, `naturalproductmech:mibig-bc0da8b0f6`, `CHEBI:29630`, `CHEBI:29665`, `CHEBI:29656`, `CHEBI:29649` |

## Group Details

### `G-PEN-001` — Missing `AS-P-78` (`BGC0000404:1`) and `Wisconsin 54-1255` (`BGC0000405:1..3`) producer strain qualifications on *Penicillium chrysogenum* records
- **Cause**: MIBiG 4.0 exports species-level `NCBITaxon:5076` (*Penicillium chrysogenum*) without strain metadata for `BGC0000404:1` (`DQ192518.1`) and `BGC0000405:1..3` (`EF601124.1`), even though Fierro et al., *Fungal Genet. Biol.* 2006 (`PMID:16713314`, `DOI:10.1016/j.fgb.2006.03.001`) and GenBank `DQ192518.1` explicitly identify strain `AS-P-78` for `BGC0000404:1` and van den Berg et al., *Fungal Genet. Biol.* 2007 (`PMID:17548217`, `DOI:10.1016/j.fgb.2007.03.008`) and GenBank `EF601124.1` explicitly identify strain `Wisconsin 54-1255` for `BGC0000405:1..3`.
- **Remediation**:
  1. Added four source-pinned rows (`BGC0000404:1` -> `AS-P-78`, `BGC0000405:1..3` -> `Wisconsin 54-1255`) to `curation/mibig_producer_strains.tsv`.
  2. Added unit and regression tests in `tests/test_producer_strains.py`.
  3. Re-ran `scripts/seed_from_sources.py` to regenerate `n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml` (`CHEBI:58572`), `isopenicillin-n.yaml` (`CHEBI:18165`), and `benzylpenicillin-sodium.yaml` (`CHEBI:51765`).

### `G-PEN-002` — Misrouted entry-level citations on `BGC0000404:1` (Chain et al. 1940 on `DQ192518.1`) and `BGC0000405:1..3` (Smith et al. 1990 on `EF601124.1`)
- **Cause**: MIBiG `BGC0000404:1` attaches `DOI:10.1016/s0140-6736(00)87452-8` (Chain et al., *Lancet* 1940, `COMPOUND_BIOACTIVITY`) to the 2005/2006 `genbank:DQ192518.1` (`17440..28759`) producer and locus claims, and `BGC0000405:1..3` attach `PMID:1368505` (Smith et al., *Bio/Technology* 1990, heterologous cosmid expression in *Neurospora crassa* and *Aspergillus niger*) to the 2007 `genbank:EF601124.1` (`22186..33473`) producer and locus claims.
- **Remediation**:
  1. Added four source-pinned rows to `curation/mibig_claim_references.tsv`, routing `BGC0000404:1` `producer_reference` and `locus_reference` to `DOI:10.1016/j.fgb.2006.03.001` (Fierro et al. 2006, preserving `source_reference=DOI:10.1016/s0140-6736(00)87452-8`) and routing `BGC0000405:1..3` `producer_reference` and `locus_reference` to `DOI:10.1016/j.fgb.2007.03.008` (van den Berg et al. 2007, preserving `source_reference=PMID:1368505`).
  2. Added regression tests in `tests/test_claim_references.py`.
  3. Re-seeded `CHEBI:58572`, `CHEBI:18165`, and `CHEBI:51765` via `scripts/seed_from_sources.py`.

### `G-PEN-003` — Upstream MIBiG salt and protonation-state encoding on benzylpenicillin sodium (`CHEBI:51765`) and monoanionic ACV (`CHEBI:58572`)
- **Cause**: MIBiG `BGC0000404:1` and `BGC0000405:3` supply the sodium carboxylate salt SMILES (`CHEBI:51765`, `FCPVYOBCFFNJFS-LQDWTQKMSA-M`) rather than neutral benzylpenicillin (`CHEBI:18208` / `CHEBI:17334`, `JGSARLDLIJGVTE-MBNYWOFBSA-N`) or biological monoanion (`CHEBI:51354`, `JGSARLDLIJGVTE-MBNYWOFBSA-M`), and `BGC0000405:1` supplies monoanionic ACV (`CHEBI:58572`, `BYEIJZFKOAXBBV-ATZCPNFKSA-M`) under the neutral label (`CHEBI:28496`, `BYEIJZFKOAXBBV-ATZCPNFKSA-N`). Replacing both `BGC0000404:1` and `BGC0000405:3` atomically or allowing counterion-stripped terminal-product validation for PenDE (`UniProtKB:P15802`, `RHEA:19809`) requires the writer enhancement tracked in open issue [#1015](https://github.com/CultureBotAI/NaturalProductMech/issues/1015).
- **Disposition**: `deferred` in open GitHub issue [#1015](https://github.com/CultureBotAI/NaturalProductMech/issues/1015).

### `G-PIK-DES-003` — Carried-forward upstream tautomeric/stereochemical separation of desosamine records and `BGC0000898`/`BGC0000094` deposit split
- **Cause**: `desosamine.yaml` (`naturalproductmech:mibig-bc0da8b0f6`, `BGC0000899:1`) encodes flat cyclic hexopyranose `ZOYWWAGVGBSJDL-UHFFFAOYSA-N` (`stereo_complete: false`) whereas `desosamine-2.yaml` (`CHEBI:32540`, `BGC0000898:1`) encodes 3-star ChEBI open-chain D-desosamine aldehyde `VTJCSBJRQLZNHE-CSMHCCOUSA-N` (`stereo_complete: true`), and 3-star ChEBI lacks a stereochemically complete cyclic D-desosamine entry. Separately, MIBiG splits the *S. venezuelae* `ATCC 15439` `pik`/`des` cluster across `BGC0000094` (`AF079138.1`, `CLUSTER_DEMONSTRATED`) and `BGC0000898` (`AF079762.1`, `CLUSTER_UNSTATED` with blank coordinates).
- **Disposition**: `deferred` in open GitHub issue [#1012](https://github.com/CultureBotAI/NaturalProductMech/issues/1012).
