# Gentamicin Review and Scoped Remediation

PR #940 reviews two exact owners without merging them or completing missing
stereochemistry. Both remain `SEEDED`; the exact-product findings stay open in
#941. The broader assay cohort and future importer checks remain in #945.

Confirmed corrections address #942 (nonexact CID72396), #943 (one historical
AID1195 dose-data flag) and #944 (two deposited strain qualifiers). The raw
inventories, valid NPAtlas xref, chemistry, taxon IDs and evidence grades remain
unchanged. The other 23 AID1195 rows were not corrected or scientifically
reviewed by this two-owner change.

## Immutable Observations

| Owner | Full-Owner Partial Assessment | Scoped Disposition |
|---|---|---|
| gentamicin-2 | [YAML](../../structured/20261013T221636Z-gentamicin-2/review.yaml), [Markdown](../../structured/20261013T221636Z-gentamicin-2/review.md) | [YAML](../../structured/20261013T222146Z-gentamicin-2-scoped-disposition/review.yaml), [Markdown](../../structured/20261013T222146Z-gentamicin-2-scoped-disposition/review.md) |
| gentamicin | [YAML](../../structured/20261013T221638Z-gentamicin/review.yaml), [Markdown](../../structured/20261013T221638Z-gentamicin/review.md) | [YAML](../../structured/20261013T222153Z-gentamicin-scoped-disposition/review.yaml), [Markdown](../../structured/20261013T222153Z-gentamicin-scoped-disposition/review.md) |

## Evidence and Scope

`manifest.json` maps original capture paths to deterministic gzip artifacts,
with hashes of both stored and decompressed bytes. It binds every review
evidence snapshot and retains exact historical/current inputs, execution
receipts, failed attempts, scoped invariant checks and the campaign checkpoint.
Article text, derivatives and denied responses are reference-only: source URLs
and hashes are retained without assuming redistribution rights. Web-only
authority observations are explicitly distinguished from captured payloads.
Local runtime binaries and ontology caches are not redistributed.

The adversarial pass was performed by the implementing assistant, not an
independent human reviewer. Checks cover complete-row drift, missing/ambiguous
sources, duplicate or malformed decisions, unapplied exclusions, unchanged
other CIDs/AIDs/owners and experimental measurements, and table-owned provenance
that an old YAML answer cannot overwrite.

The checkpoint records 52 observations across 32 owners: 31 partial owners,
one historical completed assessment and 3,083 unassessed owners. It preserves
all 243 graph components and the previous access-stop ledger. The unfinished
bryostatin investigation contributes no saved review or owner coverage here.
The full-corpus review goal is not complete.
