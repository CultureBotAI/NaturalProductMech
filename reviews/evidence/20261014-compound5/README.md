# Compound-5 Review Evidence

Two exact owners were assessed at native base
`487536b67c632b474b54bcc2ce32cf5c1097a7bd`. They share a paper-local label,
not a structure. Both assessments remain partial and retain native `SEEDED`.
The main articles were unavailable after access denials; neither exact
compound-5 production nor primary stereochemical assignment was established.

## Adversarial Corrections

- [#958](https://github.com/CultureBotAI/NaturalProductMech/issues/958): the
  original scan incorrectly looked for an InChIKey column in ChEBI origins.
  The corrected scan joins origins through the ChEBI IDs of exact-key
  structure matches and rejects missing join columns. Neither target key has
  a ChEBI structure match, so the corrected origin join remains empty.
- [#959](https://github.com/CultureBotAI/NaturalProductMech/issues/959): the
  original helper depended on unretained temporary inputs and failed lint.
  The current replay uses hash-pinned Git inputs and five retained source
  responses. It ran successfully from outside the research workspace.

`source-inspection.json` and the first two canonical review pairs are immutable
historical observations, including the flawed origin-scan method. Use
`source-inspection-corrected.json` and the linked successor review pairs for
the corrected method. No native record, source inventory, or graph changed.
These are review-method fixes, not confirmation of primary scientific claims.

## Replay

With the repository's locked chemistry environment (RDKit 2026.03.5 and
PyYAML) and Git history containing the reviewed base:

```bash
uv run --extra chemistry python reviews/evidence/20261014-compound5/inspect_sources.py \
  --output /tmp/compound5-replay.json
diff reviews/evidence/20261014-compound5/source-inspection-corrected.json /tmp/compound5-replay.json
uv run pytest -q tests/test_compound5_review_archive.py
```

Use a new output path; the helper refuses to overwrite files. `--repo` accepts
a repository path when the script is invoked elsewhere. All nine Git inputs
and five captured inputs must match `replay-inputs.json`; no network or
temporary research files are needed. Tests cover positive and empty origin
joins, incorrect headers, exact-key matching, hash drift, and unchanged
scientific output. Replay checks encoding and source extraction, not the
truth of biosynthetic claims.

## Sources And Limits

The retained responses are attributed to MIBiG (BGC0002162.3 and
BGC0002165.3) and NCBI (Taxonomy and GenBank). `sources.json` records exact
URLs, retrieval times and payload hashes. The GenBank feature coordinates in
the extracted regions are relative, not the original chromosome coordinates.
Public sequence annotations are not experimental enzyme-role assignments.

The PubMed abstracts and the publisher supplement
`10.1021/jacs.5b08319.s001` are reference-only: full text and PDF are not
redistributed. The supplement was obtained from its public publisher Figshare
record before the main article request returned403. Only the named pages in
the review were inspected, not all50pages. Access denials were not bypassed.
The supplement does not settle the numbered compound5 question or the
NRRL181/JMC1740 strain equivalence.

`checks.json` preserves initial command receipts and their original runtime
paths; `correction-checks.json` preserves correction runs. Temporary paths are
historical execution metadata, not replay prerequisites. Full native QC in the
first observations is explicitly reused from exact-base merge CI; PR and
merge-group gates independently validate this publication.
