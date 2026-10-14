# Geldanamycin Review Evidence

Two exact owners were assessed at base
`06fe27d721baac64909b12adc272528735c5a30a`, before native corrections.
`manifest.json` retains retrieval URLs, UTC times, byte hashes and executed
checks. `source-inspection.json` contains exact-key inventory scans and pinned
RDKit results. Taxonomy and registry agreement are not primary scientific closure.

The inspected public article PMC3993908 is not redistributed. Its retrieval
receipt identifies the XML bytes; the reviews name the inspected isolation and
assay sections. It reports radicicol/pochonin isolation, while geldanamycin is an
assay comparator. This rejects this particular occurrence citation, not every
possible fungal occurrence. No supplement or figure-image adjudication is claimed.

The original executed source script is preserved byte-for-byte as
`inspect_sources.original.py.txt`, matching the original manifest and initial
reviews' script hash. The `.py` copy differs only by removing an unused import
for repository lint. `replay_sources.py` explicitly verifies and executes the
archival script in a fresh temporary directory, reads the seven source TSVs from
the exact historical Git base, and checks the entire derived result for equality.
It requires the project's pinned RDKit 2026.03.5 runtime:

```bash
python reviews/evidence/20261014-geldanamycin/replay_sources.py --output /tmp/geldanamycin-replay.json
```

The requested output must not already exist. Retained resolved-owner snapshots
are the pre-curation views; successor reviews assess the corrected native owners.
Issue #131 covers the nonexact CID/assay/graph withdrawal, #966 the unsupported
fungal triple, and #967 the construct mapping. #968 remains primary identity and
migration follow-up. No assays are automatically moved between the two owners.
