# Aborycin Review Evidence

This archive makes the two immutable partial reviews in PR #904 auditable
without their temporary workspaces. `manifest.json` maps original paths and
evidence IDs to checksum-pinned gzip files, retaining both stored and original
byte hashes. Helpers, failed attempts and check logs are historical evidence,
not commands to replay.

The `owner` evidence snapshot hashes the resolved JSON view, not the raw YAML.
The `inventories` snapshot hashes the extracted source-row set, not the complete
MIBiG TSV. The raw file hashes are retained separately in each review's
`source.inputs`. The manifest's `evidence_snapshots` makes these representations
explicit without rewriting either saved observation.

The historical checkpoint retains all 3,115 owners, 243 graph components,
23 observations, 16 partially reviewed owners, zero complete scientific
reviews, 3,099 unassessed owners and all 182 inherited/current source-access
restrictions. Its corpus revision is `9191a148`; publication is not new
scientific coverage. Later work must reassess changed inputs.

Public structured sequence/chemistry snapshots and local computations are
archived. Publisher abstract payloads and the NPAtlas response remain
reference-only, with source URLs, retrieval times and digests. No new network
retrieval or bypass of an existing source barrier was needed for publication.

Adversarial review found the temporary-only evidence gap (#905), addressed by
this archive and its tests. The confirmed identity blocker (#906) and provisional
contig-attribution finding (#907) remain open pending primary-source and
source-owner adjudication. No structure merger, accession substitution,
generated-record edit or native REVIEWED promotion accompanies this archive.
