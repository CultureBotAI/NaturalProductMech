# Pre-Merge Campaign Checkpoint

`pre-merge-checkpoint.json.gz` captures the remediated working tree for PR #898.
The manifest pins its compressed and uncompressed bytes and both successor
review pairs. Use `gzip -dc` to read it. It is a pre-merge observation, not a
claim that a later commit or GitHub action had already completed.

Coverage remains 3,115 owners and 243 components: 14 partially reviewed owners,
21 immutable observations, zero completed scientific reviews and 3,101
unassessed owners. Three scoped findings are resolved; the provisional E. coli
occurrence finding remains open in #902. Other campaign findings and all access
restrictions remain unchanged. The next unassessed owners are the two aborycin
records; all partial owners still need their outstanding scientific checks.

The preceding checkpoint and its temporary-path dependencies are durably mapped
by `../20261013-yersiniabactin/manifest.json`. The original checkpoints and
reviews are retained without alteration.
