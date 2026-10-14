# Lomaiviticin C/D Review Evidence

Four separate exact owners were assessed at base
`7d6b4d16acc9a28e2b4c9de4244f205beb0da157`. The immutable observations under
`reviews/structured/` remain authoritative; this packet makes bounded database
checks and historical native inputs portable (issue #978).

`manifest.json` binds file hashes, database retrieval receipts and original
owner snapshots to that Git tree. `source-analysis.json` records pinned RDKit
2026.03.5 results, complete parsed MIBiG rows, ring adjacency, taxonomy and
protein/CDS comparisons. `inspect_sources.py` is the original temporary analysis
helper; its original paths and runtime requirements are retained, not represented
as a standalone clean-checkout command. Regression tests verify snapshot hashes
and historical owners independently.

The PR lint pass required one formatting-only line wrap in the archived helper.
`inspect_sources-original.py.txt` and `manifest-before-lint.json` retain the
original bytes, including the manifest hash captured in the immutable follow-up
reviews. The active manifest hashes both archival originals and the formatted
helper. Chemistry/protein results and scientific inputs were not recomputed or
changed by this publication correction.

## Scientific Scope

- C: both stored cores conflict with the 2021 structural revision. The
  BGC0000241 C formula additionally has two extra hydrogens relative to the
  reported 2013 isolation mass. Replacement identities remain unresolved (#975).
- D: the two encodings differ in formula/connectivity, not just stereo
  completeness. Neither is adjudicated as correct; the A-C revision is not
  automatically extended to D (#976).
- KF731828.1 is DPJ-0016; KF515737.1 is DPJ-0019. Knockout and Lom62/Lom63
  enzyme experiments do not establish those experiments on DPJ-0016. C production
  is explicitly reported for DPJ-0016, but D production in that strain is not
  established by the inspected text (#977).
- A4X724 is an exact CNB-440 Strop_2223 sequence match. Bounded UniProt queries
  did not return DPJ-0019 Lom62/Lom63; this is not a global absence claim.

## Inspected Literature

Primary text was read through public NLM XML: DOI:10.1002/cbic.201300147,
DOI:10.1016/j.tet.2014.03.009, DOI:10.1021/ol403714g and
DOI:10.1021/jacs.1c01729. The later F-H paper DOI:10.3390/md23020065 was checked
only for bounded context, not used to transfer its experiments to D.
DOI:10.1021/ja3074984 was inspected at abstract level only.

Full article bodies are not republished in this packet. Their original retrieval
receipts and hashes are retained in the manifest, not claimed as portable full
text. The 2012 ACS article returned 403 and the 2021 PMC HTML page challenged
access. No alternate retrieval was attempted after either denial; previously
retrieved XML was retained. Revision figure pixels and original isolation
spectra were not inspected. These limitations keep all four reviews partial.

Database payloads are original public factual records with their source URLs and
retrieval metadata. Existing repository source attribution remains applicable;
this packet is not a new adopted bulk source or a license grant for article text.

## Changes And Gates

Issues #977, #978 and #979 cover bounded provenance, auditability and conflict
representation corrections. Issues #975 and #976 remain separate scientific
adjudications. Chemistry, identifiers, raw inventories, PATHS.tsv, native status,
protein identities and prior immutable bundles must remain unchanged.

`qc-resumed.log` describes the original unmodified corpus, not the later fixes.
Final correction checks and the separate adversarial pass are recorded alongside
this packet and on the PR. A deterministic pass does not close identity findings.
