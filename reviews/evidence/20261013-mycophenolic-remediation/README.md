# Mycophenolic Acid Assay Remediation

`regeneration-audit.json` compares all 3,115 owners with
`988766b35bae770331e9ec46018158654a88b4b7`, including ignored files and the exact
historical file set. There are 116 changed and 2,999 unchanged owners. The 2,336
retained imported observations carry 1,458 ACTIVE, 212 INACTIVE and 666
NOT_DETERMINED calls. Non-active calls cannot back positive activity summaries.
The latter retain the source outcome label rather than implying intermediate
susceptibility. Unknown endpoint names are retained with OTHER.

The audit confirms unchanged values, units, observation order/caps, evidence
references, identities, scientific status and prior history. Changes are limited
to assay representation, supported activity summaries and appended seeding
events, plus the storage-only exception below. These checks establish faithful
transformation, not independent scientific verification of every assay.

`graph-migration.json` documents the pre-regeneration storage migration required
by issue #196. The final `staurosporine-aglycone-assays` graph moved through
`write_validated_graph_bundle` to an exact-owner component. All 18 resolved graphs,
including evidence and order, and their rendered graph models are unchanged.
The 242 previously external components remain byte-identical; there are now 243.
Neither the 64-KiB limit nor source evidence was weakened.

The first bulk attempt stopped at the size guard; a complete size preflight found
only this owner over the limit. After migration the guarded bulk write completed.
The retry log includes records already updated by the canary/partial first run;
its unchanged count is not the total change count relative to the base commit.

Native QC and regeneration receipts are retained alongside their outputs. Earlier
temporary checks caught two audit-helper assumptions: call-only rows can retain
a raw numeric value without an endpoint name, and renderer test paths must be
repository-absolute. Those helper/test defects were corrected before acceptance.

The earlier partial structured review remains immutable. A separate successor
records scoped dispositions for #877 and #878; #880 tracks the renderer fix.
Primary-paper, identity-equivalence and other scientific review limitations remain.
