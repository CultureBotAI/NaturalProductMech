# Aureothin Structure Adjudication

Issue: https://github.com/CultureBotAI/NaturalProductMech/issues/676

## Evidence And Decision

MIBiG BGC0000024 version 5 compound 1 and PubChem CID 6436188 encode
`OGUMLESFFBGVOO-VJDLAWOBSA-N`. The 3-star ChEBI default structure for
[CHEBI:80024](https://www.ebi.ac.uk/chebi/CHEBI:80024) is
`GQKXCBCSVYJUMI-WACKOAQBSA-N`. Both have formula C22H23NO6, 29 heavy atoms,
31 bonds and three rings. Pinned RDKit 2026.03.5 finds different connectivity
even after removing stereochemistry and, separately, bond orders in comparison
copies. These are constitutional isomers, not equivalent tautomer/stereo forms.

The primary article [Werneburg et al., DOI:10.1021/ja102751h](https://doi.org/10.1021/ja102751h)
was read through its accessible PMC author manuscript
[PMC2925430](https://pmc.ncbi.nlm.nih.gov/articles/PMC2925430/), main passages
and Figures 1, 6 and 7. Figure 1 compound 1 has the tetrahydrofuran
O-CH2-alkene-bearing-ring-carbon connectivity of ChEBI, rather than oxygen
directly bonded to that alkene-bearing carbon as in the MIBiG/PubChem model.
The correction adopts the pinned ChEBI default structure, including its stated
stereochemistry. This is a cited curator adjudication, not an upstream update.
Neither the article's supplementary information nor additional cited primary
papers were read for this decision.

The original MIBiG inventory is unchanged. Complete parsed rows are pinned in
`curation/mibig_structure_corrections.tsv`; refresh drift must be reviewed.
The correction drops both original database IDs, `pubchem:6436188` and
`chemspider:5029106`, from exact xrefs. Their original values remain in the raw
inventory and the record's correction note. ChemSpider was not independently
validated, so its equivalence is withheld, not claimed disproved.

## Claim Boundaries

- The three old-key LOTUS occurrences are not transferred to the new structure.
  They remain in the committed inventory pending separate source review.
- ChEBI occurrence data and the pinned AntibioticMech SAME_STRUCTURE link are
  recomputed from the new identity, not added by hand.
- The source's unstructured ChEBI bibliography is retained in notes and linked
  through the stable ChEBI entry URL. The newly joined sibling link carries its
  full pinned commit.
- A one-call NPClassifier canary on the actual corrected SMILES returned
  Polyketides / Cyclic polyketides / 4-pyrone derivatives, not a glycoside,
  dated 2026-10-07. The old classification row remains for provenance.
- Existing AurF Q70KH9/CAE02601.1 describes precursor 4-aminobenzoate to
  4-nitrobenzoate, RHEA:58889, citing DOI:10.1021/ja039328t. Its graph and step
  name neither the erroneous mature key nor the old owner ID. They can be
  preserved unchanged with the existing history during explicit migration;
  this does not constitute a new full-text review of that older paper.
- Do not mark the whole record REVIEWED. The identity correction is narrower
  than complete producer, occurrence and mechanism sign-off.
- AurH Q70KH6/CAE02604.1 (406 aa) and AurI Q70KH3/CAE02607.1 (230 aa) were
  verified against complete native AJ575648.1 CDS translations, independent
  GenPept records and reviewed UniProt sequences. These native sequences are
  not proof of experimental construct sequences or mutant phenotypes.
- New AurH/AurI graphs remain separate work. The 2010 article's paragraph
  describing pMZ04 calls it aurF while claiming rescue in a delta-aurFH
  background; this apparent inconsistency must not be silently repaired or
  treated as unqualified complementation evidence.
- The old text-map point is omitted from the rendered map, not relabelled as
  the corrected structure. Its cached embedding remains untouched; a future
  text-embedding refresh can add the new owner. The structure map must instead
  be regenerated because its fingerprints depend on the corrected molecule.

## Retained Audit Pins

Source-audit receipt SHA256:
`195f6f452a42b04c606166762015f4a1391651942abebc47707660b5738b28fe`

| Retained source | SHA256 |
|---|---|
| Primary BioC manuscript JSON | `3e120d567986f153c1d6b3bdd34244a975353ab34eb5b0d1c90f1b6048ea05d3` |
| Figure 1 JPEG | `ee9db3be18b81399beaa77f0fb7e98ab91b57ff473d6ff9676c6d4c84e3e76d1` |
| PubChem CID 6436188 response | `5b08af9467e51c0a9f818579e57f25f98bd75ad77bb65983520004d39c60b352` |
| ChEBI committed inventory | `62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2` |
| Original aureothin owner YAML | `44f2b3b47712629d4672a66623966cb2b22c8dc9e0164121c5801510ae7d7395` |

The source-audit receipt was produced before this correction on commit
`f971ca5d53089ddc16f9c0470cbc7ab54b22c050`; the unchanged original owner has
the same hash on this correction branch's main base
`d2bf485cb2fd502e8761ef232c2a215130aca4d9`.
