# Local evidence review: KS-505a

- Review: 20261104T050441Z-ks-505a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T04:24:34.141280Z
- Finished UTC: 2026-11-04T05:04:41.481448Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

KS-505a preserves a locally consistent large oxygenated C61 structure, including a separately linked oxygenated C5O ring compatible with glycoside applicability. Ten tetrahedral centres remain unspecified, including the anomeric candidate. Source Meroterpenoid/TERPENE assertions and versioned Friedelane/Triterpenoids predictions remain distinct; no exact sugar stereochemistry, target activity or complete natural identity is newly established.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2345; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-90363bf123 | data/natural_products/terpenoids/ks-505a.yaml | generated | KS-505a |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-90363bf123 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-90363bf123 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-90363bf123 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-90363bf123 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-90363bf123 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-90363bf123 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-90363bf123 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-90363bf123 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and form consistency; exact natural identity unverified

identity: supported. Targets: naturalproductmech:mibig-90363bf123.

The owner naturalproductmech:mibig-90363bf123 retains KS-505a, full key DBIAGVXGCNWASW-JMNNKWMBSA-N, NPatlas:NPA024710 and PubChem:3081782 as source metadata. Its MINTED grounding and historical no-3-star-ChEBI-match note remain limited to the retained source scope and empty exact-key ChEBI join. Both stored forms agree on C61H88O17 and the encoded partial stereochemistry. The exact external cross-references were not fetched or independently structure-matched here, and ten unspecified tetrahedral centres prevent treating the name or full key as proof of one fully assigned natural stereoisomer. No direct companion is admitted.

### Stored molecular representation

representation: supported. Targets: naturalproductmech:mibig-90363bf123.

Both forms represent one neutral C61H88O17 component, 78 heavy atoms and 88 bonds. The saved ring basis has eleven rings: seven saturated carbocycles, one aromatic six-carbon ring and three oxygen heterocycles. Four carbonyls occur in two carboxylic acids (SMILES C14 and C24), a lactone (C60=O61 with intraring O62) and a methyl ester (C66=O67, O68-C69). The separate six-membered oxygenated ring [18,19,20,21,22,23] connects to the larger framework through exocyclic C11-O17-C18; it bears hydroxyls at C20/C21, methoxy at C19 and a carboxyl substituent at C22. This complete topology supports a sugar-like, O-linked substructure rather than relying on the C5O detector alone. Its candidate anomeric centre C18 is unspecified, so alpha/beta configuration or a fully identified sugar residue is not assigned. Fourteen tetrahedral centres are specified and ten remain unresolved (SMILES 3, 7, 11, 18, 33, 35, 39, 47, 51 and 63). Saved ring bases and atom indices are representation descriptors, not biochemical numbering. The maintained stereo_complete field is derived from tetrahedral-centre assignment and is not a universal bond-geometry, optical-sign or natural-identity certificate. All ten original pair-comparison flags and complete atom-count correspondence are true for this record, while full_graph_identity_established remains false. No new molecular parse or alternate structure was introduced.

### Producer and locus evidence

provenance: supported. Targets: naturalproductmech:mibig-90363bf123.

MIBiG row 767 belongs to BGC0000651 version 5 and asserts Streptomyces argenteolus, NCBITaxon:67274, as producer at SOURCE_ASSERTION grade. The AB307968.1 TERPENE locus is CLUSTER_UNSTATED and has no retained experimental method. The source compound class Meroterpenoid is preserved separately from the model prediction. This exact row supports its database provenance, but does not establish the complete pathway, individual glycosyltransferase, sugar donor or exact natural stereochemical product. The cached species stanza is a local taxonomic record, not refreshed production verification.

### Citation scope

evidence: supported. Targets: naturalproductmech:mibig-90363bf123.

The selected MIBiG compound row explicitly carries DOI:10.1271/bbb.70477 at COMPOUND_EVIDENCE level. This source placement is retained without upgrading it to a newly read primary experiment or a complete gene-to-product demonstration. The NPatlas and PubChem identifiers are identity cross-references, not additional independent experiments. No newly accessed publication, assay report or sequence supplies missing stereochemical or pathway assignments.

### Occurrence and assay scope

evidence: supported. Targets: naturalproductmech:mibig-90363bf123.

The owner contains no occurrence, bioactivity or molecular-target object. The exact LOTUS, ChEBI-origin and CyanometDB joins have no occurrence result. PubChem row 953 retains CID3081782 with a blank AID and is a no-assay sentinel; it must not be interpreted as inactivity, a measured endpoint or a target assignment. BindingDB and AntibioticMech joins have no matching target result. The source producer assertion remains distinct from an observed occurrence, and the retained name is not used to infer an unrecorded pharmacological mechanism.

### Computed classification applicability

consistency: supported. Targets: naturalproductmech:mibig-90363bf123.

The source compound class Meroterpenoid and BGC TERPENE class are separately retained from NPClassifier npclassifier.gnps2.org@2026-09-07 Terpenoids/Triterpenoids/Friedelane triterpenoids with is_glycoside:true. The complete graph supplies a bounded structural rationale for glycoside applicability: a separate oxygenated C5O ring is joined by an exocyclic O linkage and carries multiple oxygen substituents. That supports the flag’s applicability without proving a particular residue, anomeric configuration, biosynthetic origin or the finer Friedelane assignment. The C61 total includes substantial substituent structure and cannot alone invalidate or prove the scaffold prediction. No faithful-ingestion or source-identity defect is established by these differing classification scopes.

### Scientific completion

completeness: unknown. Targets: naturalproductmech:mibig-90363bf123.

Complete owner/history, actual intake and source ownership, all retained rows/no-match frames and relevant cache, and both full 78-atom/88-bond molecular forms were read. The source stereo_complete:false agrees with ten unresolved centres. No mechanism reader applies because no mechanism roots or components are declared. Accepted diagnostics and local gates retain their limited scope; Full QC, complete OAK and fresh primary/identity/sequence checks remain unavailable. This is a partial scientific review with explicit sugar and stereochemical limits and no supported curation finding.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2345-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/ks-505a.yaml; Whole current owner plaintext and complete curation_history | supports | Complete current owner and all 2 history entries; native curation_status remains SEEDED. |
| bgc-2345-capture | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/4 | supports | Complete captured owner preserves every written field/history; selected maintained-reader applicability is false and no component reference is declared. |
| bgc-2345-intake | /private/tmp/npm-review-work/shared-next-batch235/intakes/2345-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical intake for naturalproductmech:mibig-90363bf123; 37 pinned input placements and explicit maintained source/curator ownership. |
| bgc-2345-grounding-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/4/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"chemical_structure":{"smiles":"C[C@@H]1CC2[C@@](CCC3[C@@]2([C@@H](CC([C@]3(C)C(=O)O)OC4[C@@H]([C@H]([C@@H]([C@H](O4)C(=O)O)O)O)OC)C)C)(C5[C@]1(C6CC[C@]7(C([C@@]6(CC5)C)CC[C@@]8(C7CC[C@]9(C8CC1=C(O9)C=CC2=C1C(=O)OC2(CCC(=O)OC)O)CO)C)CO)C)C","standard_inchi":"InChI=1S/C61H88O17/c1-30-25-40-54(4,21-15-39-57(40,7)31(2)26-42(58(39,8)52(70)71)75-51-48(74-10)46(66)45(65)47(76-51)49(67)68)35-13-19-53(3)36(56(30,35)6)16-22-59(28-62)37(53)14-20-55(5)38(59)17-23-60(29-63)41(55)27-32-34(77-60)12-11-33-44(32)50(69)78-61(33,72)24-18-43(64)73-9/h11-12,30-31,35-42,45-48,51,62-63,65-66,72H,13-29H2,1-10H3,(H,67,68)(H,70,71)/t30-,31-,35?,36?,37?,38?,39?,40?,41?,42?,45+,46+,47+,48-,51?,53-,54+,55-,56+,57+,58-,59-,60-,61?/m1/s1","standard_inchi_key":"DBIAGVXGCNWASW-JMNNKWMBSA-N","stereo_complete":false,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0000651"},"grounding_notes":"No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.","grounding_status":"MINTED","identifier":"naturalproductmech:mibig-90363bf123","label":"KS-505a","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-90363bf123","source":"MIBIG","source_id":"BGC0000651","source_label":"KS-505a","source_version":"5"}],"xrefs":["npatlas:NPA024710","pubchem:3081782"]} |
| bgc-2345-origin-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/4/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0000651","bgc_class":["TERPENE"],"entry_status":"active","entry_version":"5","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0000651 entry version 5; citation taken from the compound evidence level","reference":"DOI:10.1271/bbb.70477"}],"genome_accession":"genbank:AB307968.1","link_evidence_basis":"CLUSTER_UNSTATED","organism_label":"Streptomyces argenteolus","organism_taxon_id":"NCBITaxon:67274"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0000651","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0000651 entry version 5; citation taken from the compound evidence level","reference":"DOI:10.1271/bbb.70477"}],"evidence_basis":"SOURCE_ASSERTION","notes":"Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"5","taxon_id":"NCBITaxon:67274","taxon_label":"Streptomyces argenteolus"}],"producer_taxon_groups":["ACTINOBACTERIAL"],"source_concepts":[{"minted_identifier":"naturalproductmech:mibig-90363bf123","source":"MIBIG","source_id":"BGC0000651","source_label":"KS-505a","source_version":"5"}]} |
| bgc-2345-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/4/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"grounding_notes":"No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier."} |
| bgc-2345-assay-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/4/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {} |
| bgc-2345-classification-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/4/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"bgc_class":["TERPENE"],"biosynthesis_origin":"NATURAL_PRODUCT","compound_classes":["Meroterpenoid"],"np_classification":{"class_results":["Friedelane triterpenoids"],"is_glycoside":true,"pathway_results":["Terpenoids"],"superclass_results":["Triterpenoids"],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"} |
| bgc-2345-chemistry | /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-DATA-001.json; /records/4/declared_structure; /records/4/smiles/status; /records/4/inchi/status; /records/4/smiles/computed; /records/4/inchi/computed; /records/4/comparisons; /records/4/atom_correspondence | supports | Both stored forms parsed. Exact original comparison/correspondence and stereo values: {"atom_correspondence":{"complete_atom_count_match":true,"full_graph_identity_established":false,"scope":"One chirality-aware substructure match; no independent full graph or natural identity claim.","smiles_to_inchi_atom_indices":[0,29,24,39,53,20,14,38,56,30,25,41,57,7,51,69,70,74,50,47,45,44,46,75,48,66,67,64,65,73,9,1,6,34,55,35,15,21,58,36,52,18,12,2,13,19,54,37,16,22,59,40,26,31,33,76,11,10,32,43,49,68,77,60,23,17,42,63,72,8,71,28,62,4,27,61,5,3]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true},"declared_structure":{"smiles":"C[C@@H]1CC2[C@@](CCC3[C@@]2([C@@H](CC([C@]3(C)C(=O)O)OC4[C@@H]([C@H]([C@@H]([C@H](O4)C(=O)O)O)O)OC)C)C)(C5[C@]1(C6CC[C@]7(C([C@@]6(CC5)C)CC[C@@]8(C7CC[C@]9(C8CC1=C(O9)C=CC2=C1C(=O)OC2(CCC(=O)OC)O)CO)C)CO)C)C","standard_inchi":"InChI=1S/C61H88O17/c1-30-25-40-54(4,21-15-39-57(40,7)31(2)26-42(58(39,8)52(70)71)75-51-48(74-10)46(66)45(65)47(76-51)49(67)68)35-13-19-53(3)36(56(30,35)6)16-22-59(28-62)37(53)14-20-55(5)38(59)17-23-60(29-63)41(55)27-32-34(77-60)12-11-33-44(32)50(69)78-61(33,72)24-18-43(64)73-9/h11-12,30-31,35-42,45-48,51,62-63,65-66,72H,13-29H2,1-10H3,(H,67,68)(H,70,71)/t30-,31-,35?,36?,37?,38?,39?,40?,41?,42?,45+,46+,47+,48-,51?,53-,54+,55-,56+,57+,58-,59-,60-,61?/m1/s1","standard_inchi_key":"DBIAGVXGCNWASW-JMNNKWMBSA-N","stereo_complete":false,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0000651"},"saved_stereo":{"inchi":{"Atom_Tetrahedral:Specified":14,"Atom_Tetrahedral:Unspecified":10},"smiles":{"Atom_Tetrahedral:Specified":14,"Atom_Tetrahedral:Unspecified":10}}} |
| bgc-2345-topology | /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-DATA-001.json; /records/4/smiles/computed; /records/4/inchi/computed; /records/4/declared_structure; /records/4/literal_InChI_layers; /records/4/comparisons; /records/4/atom_correspondence | supports | Complete saved topology interpretation: Both forms represent one neutral C61H88O17 component, 78 heavy atoms and 88 bonds. The saved ring basis has eleven rings: seven saturated carbocycles, one aromatic six-carbon ring and three oxygen heterocycles. Four carbonyls occur in two carboxylic acids (SMILES C14 and C24), a lactone (C60=O61 with intraring O62) and a methyl ester (C66=O67, O68-C69). The separate six-membered oxygenated ring [18,19,20,21,22,23] connects to the larger framework through exocyclic C11-O17-C18; it bears hydroxyls at C20/C21, methoxy at C19 and a carboxyl substituent at C22. This complete topology supports a sugar-like, O-linked substructure rather than relying on the C5O detector alone. Its candidate anomeric centre C18 is unspecified, so alpha/beta configuration or a fully identified sugar residue is not assigned. Fourteen tetrahedral centres are specified and ten remain unresolved (SMILES 3, 7, 11, 18, 33, 35, 39, 47, 51 and 63). Saved ring bases and atom indices are representation descriptors, not biochemical numbering. |
| bgc-2345-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-execution-001.json; Whole current diagnostic-execution | supports | ROOT operated one original stored-form diagnostic, exit 0, one attempt, preserved original streams and closed environment. This execution receipt is not independent scientific verification. |
| bgc-2345-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/root-diagnostic-acceptance-001.json; /status; /accepted; /DATA; /execution; /verification; /warning_scope; /limits | supports | ROOT accepts the original 20 stored parses and exact original comparisons/key/capture joins. Two original undefined-stereo and two charge-rearrangement warnings remain global and unassigned. Acceptance establishes local execution integrity, not natural identity or full graph proof. |
| bgc-2345-native-acceptance | /private/tmp/npm-review-work/shared-next-batch235/root-native-five-gates-acceptance-001.json; Whole current native-acceptance | supports | Five original local gates passed. Full QC and complete OAK coverage remain unavailable, so these results do not establish all required validation or a scientific verdict. |
| bgc-2345-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch235/root-intake-native-acceptance-001.json; Whole current intake-acceptance | supports | ROOT accepts ten actual canonical intakes and exact current source ownership/input plans; scientific assessment is separate. |
| bgc-2345-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch235/root-source-inventory-acceptance-001.json; Whole current inventory-acceptance | supports | ROOT accepts the original saved inventory and current input/raw/query/row joins. Complete meaning reading is separately attributed in source notes. |
| bgc-2345-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch235/root-source-plan-acceptance-001.json; Whole current plan-acceptance | supports | ROOT accepts the actual input plan and preserved source contexts, without a scientific verdict. |
| bgc-2345-plan | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-target-input-plan-001.json; /records/4 | supports | Current one-record input plan with exact direct companions, predicates and input roles. |
| bgc-2345-source-notes | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-scope-notes-001.json; /reading; /cautions; /scientific_limits | supports | Complete disjoint source/raw-history reading and exact carries, with compound-specific cautions; source planning did not adjudicate pre-intake science. |
| bgc-2345-curation-scope | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-scope-notes-001.json; /curation | supports | ROOT explicitly opened eight implemented curation tables, including ignored files, over 1233 casefolded literal tokens. One taxon-only rationale hit at unrelated BGC0001648:1 does not support any present compound/locus strain transfer; there was no current key, identifier, owned-BGC, label or slug hit. Reserved decisions.tsv, queue and unresolved-taxon routes were not consumed. This is bounded coverage, not universal absence. |
| bgc-2345-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/mibig_compounds | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[{"last_physical_line":767,"physical_line":767,"raw_tsv_record":"BGC0000651\t5\tactive\tquestionable\tunknown\tKS-505a\t1\tC[C@@H]1CC2[C@@](CCC3[C@@]2([C@@H](CC([C@]3(C)C(=O)O)OC4[C@@H]([C@H]([C@@H]([C@H](O4)C(=O)O)O)O)OC)C)C)(C5[C@]1(C6CC[C@]7(C([C@@]6(CC5)C)CC[C@@]8(C7CC[C@]9(C8CC1=C(O9)C=CC2=C1C(=O)OC2(CCC(=O)OC)O)CO)C)CO)C)C\tInChI=1S/C61H88O17/c1-30-25-40-54(4,21-15-39-57(40,7)31(2)26-42(58(39,8)52(70)71)75-51-48(74-10)46(66)45(65)47(76-51)49(67)68)35-13-19-53(3)36(56(30,35)6)16-22-59(28-62)37(53)14-20-55(5)38(59)17-23-60(29-63)41(55)27-32-34(77-60)12-11-33-44(32)50(69)78-61(33,72)24-18-43(64)73-9/h11-12,30-31,35-42,45-48,51,62-63,65-66,72H,13-29H2,1-10H3,(H,67,68)(H,70,71)/t30-,31-,35?,36?,37?,38?,39?,40?,41?,42?,45+,46+,47+,48-,51?,53-,54+,55-,56+,57+,58-,59-,60-,61?/m1/s1\tDBIAGVXGCNWASW-JMNNKWMBSA-N\tfalse\tMeroterpenoid\tnpatlas:NPA024710&#124;pubchem:3081782\tNCBITaxon:67274\tStreptomyces argenteolus\tterpene\tUnknown\tAB307968.1\t\t\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tDOI:10.1271/bbb.70477\tCOMPOUND_EVIDENCE\n","row":{"bgc_classes":"terpene","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"Meroterpenoid","compound_index":"1","compound_name":"KS-505a","database_ids":"npatlas:NPA024710&#124;pubchem:3081782","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"5","genome_accession":"AB307968.1","locus_evidence_methods":"","locus_from":"","locus_to":"","mibig_accession":"BGC0000651","primary_reference":"DOI:10.1271/bbb.70477","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"COMPOUND_EVIDENCE","smiles":"C[C@@H]1CC2[C@@](CCC3[C@@]2([C@@H](CC([C@]3(C)C(=O)O)OC4[C@@H]([C@H]([C@@H]([C@H](O4)C(=O)O)O)O)OC)C)C)(C5[C@]1(C6CC[C@]7(C([C@@]6(CC5)C)CC[C@@]8(C7CC[C@]9(C8CC1=C(O9)C=CC2=C1C(=O)OC2(CCC(=O)OC)O)CO)C)CO)C)C","standard_inchi":"InChI=1S/C61H88O17/c1-30-25-40-54(4,21-15-39-57(40,7)31(2)26-42(58(39,8)52(70)71)75-51-48(74-10)46(66)45(65)47(76-51)49(67)68)35-13-19-53(3)36(56(30,35)6)16-22-59(28-62)37(53)14-20-55(5)38(59)17-23-60(29-63)41(55)27-32-34(77-60)12-11-33-44(32)50(69)78-61(33,72)24-18-43(64)73-9/h11-12,30-31,35-42,45-48,51,62-63,65-66,72H,13-29H2,1-10H3,(H,67,68)(H,70,71)/t30-,31-,35?,36?,37?,38?,39?,40?,41?,42?,45+,46+,47+,48-,51?,53-,54+,55-,56+,57+,58-,59-,60-,61?/m1/s1","standard_inchi_key":"DBIAGVXGCNWASW-JMNNKWMBSA-N","stereo_complete":"false","taxon_id":"NCBITaxon:67274","taxon_label":"Streptomyces argenteolus"},"row_sha256":"758e652cd11ffe7cd62aaf4e8f99392609be93cc509f47233658e974a341c185"}],"predicate":"exact complete standard_inchi_key equality","query":"DBIAGVXGCNWASW-JMNNKWMBSA-N"} |
| bgc-2345-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 767–767, row_sha256 758e652cd11ffe7cd62aaf4e8f99392609be93cc509f47233658e974a341c185 | supports | Complete retained physical row payloads, every field: [{"bgc_classes":"terpene","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"Meroterpenoid","compound_index":"1","compound_name":"KS-505a","database_ids":"npatlas:NPA024710&#124;pubchem:3081782","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"5","genome_accession":"AB307968.1","locus_evidence_methods":"","locus_from":"","locus_to":"","mibig_accession":"BGC0000651","primary_reference":"DOI:10.1271/bbb.70477","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"COMPOUND_EVIDENCE","smiles":"C[C@@H]1CC2[C@@](CCC3[C@@]2([C@@H](CC([C@]3(C)C(=O)O)OC4[C@@H]([C@H]([C@@H]([C@H](O4)C(=O)O)O)O)OC)C)C)(C5[C@]1(C6CC[C@]7(C([C@@]6(CC5)C)CC[C@@]8(C7CC[C@]9(C8CC1=C(O9)C=CC2=C1C(=O)OC2(CCC(=O)OC)O)CO)C)CO)C)C","standard_inchi":"InChI=1S/C61H88O17/c1-30-25-40-54(4,21-15-39-57(40,7)31(2)26-42(58(39,8)52(70)71)75-51-48(74-10)46(66)45(65)47(76-51)49(67)68)35-13-19-53(3)36(56(30,35)6)16-22-59(28-62)37(53)14-20-55(5)38(59)17-23-60(29-63)41(55)27-32-34(77-60)12-11-33-44(32)50(69)78-61(33,72)24-18-43(64)73-9/h11-12,30-31,35-42,45-48,51,62-63,65-66,72H,13-29H2,1-10H3,(H,67,68)(H,70,71)/t30-,31-,35?,36?,37?,38?,39?,40?,41?,42?,45+,46+,47+,48-,51?,53-,54+,55-,56+,57+,58-,59-,60-,61?/m1/s1","standard_inchi_key":"DBIAGVXGCNWASW-JMNNKWMBSA-N","stereo_complete":"false","taxon_id":"NCBITaxon:67274","taxon_label":"Streptomyces argenteolus"}] |
| bgc-2345-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/chebi_structures | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"DBIAGVXGCNWASW-JMNNKWMBSA-N"} |
| bgc-2345-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"DBIAGVXGCNWASW-JMNNKWMBSA-N"} |
| bgc-2345-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"DBIAGVXGCNWASW-JMNNKWMBSA-N"} |
| bgc-2345-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/npclassifier | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[{"last_physical_line":378,"physical_line":378,"raw_tsv_record":"DBIAGVXGCNWASW-JMNNKWMBSA-N\tC[C@@H]1CC2[C@@](CCC3[C@@]2([C@@H](CC([C@]3(C)C(=O)O)OC4[C@@H]([C@H]([C@@H]([C@H](O4)C(=O)O)O)O)OC)C)C)(C5[C@]1(C6CC[C@]7(C([C@@]6(CC5)C)CC[C@@]8(C7CC[C@]9(C8CC1=C(O9)C=CC2=C1C(=O)OC2(CCC(=O)OC)O)CO)C)CO)C)C\tTerpenoids\tTriterpenoids\tFriedelane triterpenoids\ttrue\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"Friedelane triterpenoids","is_glycoside":"true","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@@H]1CC2[C@@](CCC3[C@@]2([C@@H](CC([C@]3(C)C(=O)O)OC4[C@@H]([C@H]([C@@H]([C@H](O4)C(=O)O)O)O)OC)C)C)(C5[C@]1(C6CC[C@]7(C([C@@]6(CC5)C)CC[C@@]8(C7CC[C@]9(C8CC1=C(O9)C=CC2=C1C(=O)OC2(CCC(=O)OC)O)CO)C)CO)C)C","standard_inchi_key":"DBIAGVXGCNWASW-JMNNKWMBSA-N","superclass_results":"Triterpenoids"},"row_sha256":"c7881ec6b7284c0c44cfb7fe74a5f06276af88160b0522013a41ce3e5d7317f5"}],"predicate":"exact complete standard_inchi_key equality","query":"DBIAGVXGCNWASW-JMNNKWMBSA-N"} |
| bgc-2345-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 378–378, row_sha256 c7881ec6b7284c0c44cfb7fe74a5f06276af88160b0522013a41ce3e5d7317f5 | supports | Complete retained physical row payloads, every field: [{"class_results":"Friedelane triterpenoids","is_glycoside":"true","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@@H]1CC2[C@@](CCC3[C@@]2([C@@H](CC([C@]3(C)C(=O)O)OC4[C@@H]([C@H]([C@@H]([C@H](O4)C(=O)O)O)O)OC)C)C)(C5[C@]1(C6CC[C@]7(C([C@@]6(CC5)C)CC[C@@]8(C7CC[C@]9(C8CC1=C(O9)C=CC2=C1C(=O)OC2(CCC(=O)OC)O)CO)C)CO)C)C","standard_inchi_key":"DBIAGVXGCNWASW-JMNNKWMBSA-N","superclass_results":"Triterpenoids"}] |
| bgc-2345-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[{"last_physical_line":953,"physical_line":953,"raw_tsv_record":"DBIAGVXGCNWASW-JMNNKWMBSA-N\t3081782\t\t(no assay data)\t\t\t\t\t\t\t\n","row":{"activity_name":"","activity_outcome":"","activity_value_um":"","aid":"","assay_name":"(no assay data)","assay_type":"","cid":"3081782","depositor":"","reference":"","standard_inchi_key":"DBIAGVXGCNWASW-JMNNKWMBSA-N","target_accession":""},"row_sha256":"f3b85aa5c8d437d5d19ba54519ccbd29d26e8779642b1dd727576da6b500f2bf"}],"predicate":"exact complete standard_inchi_key equality","query":"DBIAGVXGCNWASW-JMNNKWMBSA-N"} |
| bgc-2345-source-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Header line 1; physical lines 953–953, row_sha256 f3b85aa5c8d437d5d19ba54519ccbd29d26e8779642b1dd727576da6b500f2bf | supports | Complete retained physical row payloads, every field: [{"activity_name":"","activity_outcome":"","activity_value_um":"","aid":"","assay_name":"(no assay data)","assay_type":"","cid":"3081782","depositor":"","reference":"","standard_inchi_key":"DBIAGVXGCNWASW-JMNNKWMBSA-N","target_accession":""}] |
| bgc-2345-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"DBIAGVXGCNWASW-JMNNKWMBSA-N"} |
| bgc-2345-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"DBIAGVXGCNWASW-JMNNKWMBSA-N"} |
| bgc-2345-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/chebi_origins | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact chebi_id from exact full-key structure rows","query":[]} |
| bgc-2345-source-routes | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/source_taxa; /contexts/8/source_scope_inventory/forward_taxon_merge_matches; /contexts/8/source_scope_inventory/nonorganism_matches; /contexts/8/source_scope_inventory/actual_assay_rows; /contexts/8/source_scope_inventory/blank_AID_sentinels; /contexts/8/source_scope_inventory/related_corpus_rows | supports | Exact source taxa and route lists; source_taxa is distinct from the empty forward/nonorganism and actual-assay/related routes; a blank-AID sentinel is separate: {"actual_assay_rows":[],"blank_AID_sentinels":[{"last_physical_line":953,"physical_line":953,"raw_tsv_record":"DBIAGVXGCNWASW-JMNNKWMBSA-N\t3081782\t\t(no assay data)\t\t\t\t\t\t\t\n","row":{"activity_name":"","activity_outcome":"","activity_value_um":"","aid":"","assay_name":"(no assay data)","assay_type":"","cid":"3081782","depositor":"","reference":"","standard_inchi_key":"DBIAGVXGCNWASW-JMNNKWMBSA-N","target_accession":""},"row_sha256":"f3b85aa5c8d437d5d19ba54519ccbd29d26e8779642b1dd727576da6b500f2bf"}],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:67274"]} |
| bgc-2345-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/232 | supports | Complete relevant cached stanzas, with no fresh taxonomy verification: [{"complete_stanza":"[Term]\nid: NCBITaxon:67274\nname: Streptomyces argenteolus\n\n","id":"NCBITaxon:67274","physical_line":29950}] |
| bgc-2345-direct-contexts | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /records/4/direct_companion_paths; /records/4/direct_companion_predicates | supports | Exact one-hop scope, with no claim transfer: {"direct_companion_paths":[],"direct_companion_predicates":[]} |
| bgc-2345-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 392–433 | supports | The structure flag describes undefined stereocentres. ComputedClassification is explicitly a named/versioned prediction from structure, never a source assertion or an admission criterion. |
| bgc-2345-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 142–173 | supports | Maintained stereo_complete derives from FindMolChiralCenters and absence of question-mark centre tags. It is not blanket all-bond-geometry or natural-identity proof. |
| bgc-2345-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 972–1020 | supports | Maintained seeding preserves lead source structures and named/versioned computed predictions separately; the computed pathway can control filing without becoming a source assertion. |
| bgc-2345-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole current profile | supports | One-record claim-level scientific review requires twelve dimensions and truthful partial completion/unavailable-check limits. |
| bgc-2345-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole current skill | supports | The review does not edit source records; the overriding absolute no-request instruction limits evidence access to retained local files. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-235/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-235/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-235/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-235/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-235/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- All evidence is retained locally. No external identifier, taxonomy, primary publication, protein sequence or natural stereochemical assignment was refreshed under the absolute no-request instruction.
- Full QC and complete OAK authority coverage remain unavailable. Local gate and parse success establish only their explicit mechanical scope. No maintained reader applies to this owner.
- Exact no-match joins are bounded by saved predicates/snapshots. Shared names, loci, taxa, citations or companions do not transfer compound-specific production, activity, mechanism or independent-study status.
- Two original undefined-stereo and two charge-rearrangement warnings are global and unassigned. No additional molecular/YAML parse, source query or target invocation occurred during this scientific authoring.
- No source record, native status or history is edited. Any supported future correction belongs to the maintained source/curator owners listed in the actual canonical intake.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Complete owner/history and actual intake were read. Full source payload meanings and direct-companion/raw-history carries remain explicitly attributed in pinned source notes.
- BGC personally read all ten first-five molecular forms: 302 atom rows / 334 bond rows plus complete scalars, ring/stereo/motif tables and original comparisons/maps. Diagnostic indices are zero-based, not biochemical locants.
- ROOT operated original activation/capture, collector/composer, canonical intakes and chemistry; Native operated original gates and the one applicable Juniperol maintained reader. BGC authored source planning and these scientific assessments without invoking any target during scientific authoring.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T050441Z-ks-505a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: KS-505a'
started_at: '2026-11-04T04:24:34.141280Z'
finished_at: '2026-11-04T05:04:41.481448Z'
reviewer:
  identity: Codex root with native_checks, bgc_science and review_support peer agents
  kind: agent
  independence: independent
  independence_basis: This review team inspected existing owner and retained source
    bytes without editing them; scientific fragments were cross-checked separately
    from their author. Local validation is not treated as scientific proof.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: KS-505a preserves a locally consistent large oxygenated C61 structure, including
  a separately linked oxygenated C5O ring compatible with glycoside applicability.
  Ten tetrahedral centres remain unspecified, including the anomeric candidate. Source
  Meroterpenoid/TERPENE assertions and versioned Friedelane/Triterpenoids predictions
  remain distinct; no exact sugar stereochemistry, target activity or complete natural
  identity is newly established.
source:
  git_revision: ce6a5498df5be51116bd5e0c119023ee62bb5464
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
    role: context
  - path: AGENTS.md
    sha256: 69e4037f8dc97d4b00bb7bb83b41ceca025f6ef578d5c0bf8086f3400becde0b
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
  - path: curation/lotus_occurrence_exclusions.tsv
    sha256: d1778f304b83256e756a3aec99f4fd67b5a5d2aee3ca32f88dd0418592f8a30d
    role: context
  - path: curation/mibig_claim_references.tsv
    sha256: bee1d64051b9b934be99ed1320ef33ecef7644c94bbdd11e7c1a040accd02029
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: 7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e
    role: context
  - path: curation/mibig_producer_isolates.tsv
    sha256: 8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: bab55d1e354d6196096511d7fdb25f25e4c98cfbe041e02a91d707419987f7ae
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: c48f7467343ec2679f404d2fbd8b178e5f62afc7545b785ecb75f99d8617f4f0
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: cc27be3b8e741164b50f154f8fc82df884066006b5343c295541ee671868bc9c
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
    role: context
  - path: data/natural_products/terpenoids/ks-505a.yaml
    sha256: 119d20166daaa1be65caf23ab7c2b6ca79b5530c6046a14487afe8c5b76b561d
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
  - path: data/raw/cyanometdb_occurrences.tsv
    sha256: f81900edaaaceb1472c0d8100a17b6ca51ccd0c913e4f0aebf24b010b7bb92b8
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
    sha256: c3ebdac3952c23894df0d58843322b1082357098642762b834eca137358d1eaa
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/extract_chebi.py
    sha256: 46e1898b88fce16096af34eb9e7c9dea40e4d7c8c157d60d485fa85878088e8f
    role: context
  - path: scripts/extract_mibig.py
    sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2345; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-90363bf123
targets:
- target_id: naturalproductmech:mibig-90363bf123
  path: data/natural_products/terpenoids/ks-505a.yaml
  label: KS-505a
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained harmonization generator; seeded fields are corrected through
      maintained inputs and validated regeneration.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Retained MIBiG structure, producer and compound-specific locus assertions.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned computed classification and filing assertions.
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Maintained extraction of MIBiG compound names, structures, stereochemistry
      flags and source provenance.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/pubchem_bioassay.tsv
    role: Retained assay rows or empty-assay sentinels; source outcome and title alone
      do not establish mechanism.
  ownership_note: This review proposes no record edit. Source corrections belong in
    maintained inventories, implemented curation tables, extractors or the seeder;
    generated pages are not owners.
checks:
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-90363bf123
  command: just validate-strict data/natural_products/terpenoids/jerangolid-d.yaml
    data/natural_products/terpenoids/juniperol-longiborneol.yaml data/natural_products/terpenoids/kainic-acid-lactone.yaml
    data/natural_products/terpenoids/koraiol.yaml data/natural_products/terpenoids/ks-505a.yaml
    data/natural_products/terpenoids/lankacidin-c.yaml data/natural_products/terpenoids/lupeol.yaml
    data/natural_products/terpenoids/lycosantalonol.yaml data/natural_products/terpenoids/mangicol-a.yaml
    data/natural_products/terpenoids/marinoterpin-a.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-235/validate-strict-selected10-001.tsv
  exit_code: 0
  evidence_ids:
  - root-native-strict_ten
  scope_note: Batch-local execution also covers this individual target; full-corpus
    checks retain their full scope.
- check_id: root-native-strict_full
  name: strict_full
  status: passed
  required: true
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  target_ids:
  - naturalproductmech:mibig-90363bf123
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-235/validate-all-001.tsv
  exit_code: 0
  evidence_ids:
  - root-native-strict_full
  scope_note: Batch-local execution also covers this individual target; full-corpus
    checks retain their full scope.
- check_id: root-native-lockfile
  name: lockfile
  status: passed
  required: true
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  target_ids:
  - naturalproductmech:mibig-90363bf123
  command: just verify-corpus --summary
  exit_code: 0
  evidence_ids:
  - root-native-lockfile
  scope_note: Batch-local execution also covers this individual target; full-corpus
    checks retain their full scope.
- check_id: root-native-reproduction
  name: reproduction
  status: passed
  required: true
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  target_ids:
  - naturalproductmech:mibig-90363bf123
  command: just verify-reproduction
  exit_code: 0
  evidence_ids:
  - root-native-reproduction
  scope_note: Batch-local execution also covers this individual target; full-corpus
    checks retain their full scope.
- check_id: root-native-queue
  name: queue
  status: passed
  required: true
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  target_ids:
  - naturalproductmech:mibig-90363bf123
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-235/review-queue-001.tsv
  exit_code: 0
  evidence_ids:
  - root-native-queue
  scope_note: Batch-local execution also covers this individual target; full-corpus
    checks retain their full scope.
- check_id: root-full-qc
  name: Full just qc
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-90363bf123
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-90363bf123
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-90363bf123
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2345-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/ks-505a.yaml
  locator: Whole current owner plaintext and complete curation_history
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Complete current owner and all 2 history entries; native curation_status
    remains SEEDED.
  snapshot_sha256: 119d20166daaa1be65caf23ab7c2b6ca79b5530c6046a14487afe8c5b76b561d
- evidence_id: bgc-2345-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/4
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Complete captured owner preserves every written field/history; selected
    maintained-reader applicability is false and no component reference is declared.
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: bgc-2345-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/intakes/2345-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Actual canonical intake for naturalproductmech:mibig-90363bf123; 37 pinned
    input placements and explicit maintained source/curator ownership.
  snapshot_sha256: 852370777d7094099006dc2b3999b91262b2ec52a0df2e495e7e097991d7878f
- evidence_id: bgc-2345-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/4/owner_document
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"chemical_structure":{"smiles":"C[C@@H]1CC2[C@@](CCC3[C@@]2([C@@H](CC([C@]3(C)C(=O)O)OC4[C@@H]([C@H]([C@@H]([C@H](O4)C(=O)O)O)O)OC)C)C)(C5[C@]1(C6CC[C@]7(C([C@@]6(CC5)C)CC[C@@]8(C7CC[C@]9(C8CC1=C(O9)C=CC2=C1C(=O)OC2(CCC(=O)OC)O)CO)C)CO)C)C","standard_inchi":"InChI=1S/C61H88O17/c1-30-25-40-54(4,21-15-39-57(40,7)31(2)26-42(58(39,8)52(70)71)75-51-48(74-10)46(66)45(65)47(76-51)49(67)68)35-13-19-53(3)36(56(30,35)6)16-22-59(28-62)37(53)14-20-55(5)38(59)17-23-60(29-63)41(55)27-32-34(77-60)12-11-33-44(32)50(69)78-61(33,72)24-18-43(64)73-9/h11-12,30-31,35-42,45-48,51,62-63,65-66,72H,13-29H2,1-10H3,(H,67,68)(H,70,71)/t30-,31-,35?,36?,37?,38?,39?,40?,41?,42?,45+,46+,47+,48-,51?,53-,54+,55-,56+,57+,58-,59-,60-,61?/m1/s1","standard_inchi_key":"DBIAGVXGCNWASW-JMNNKWMBSA-N","stereo_complete":false,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0000651"},"grounding_notes":"No
    3-star ChEBI entry shares this structure, so the record keeps a content-hashed
    identifier.","grounding_status":"MINTED","identifier":"naturalproductmech:mibig-90363bf123","label":"KS-505a","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-90363bf123","source":"MIBIG","source_id":"BGC0000651","source_label":"KS-505a","source_version":"5"}],"xrefs":["npatlas:NPA024710","pubchem:3081782"]}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: bgc-2345-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/4/owner_document
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0000651","bgc_class":["TERPENE"],"entry_status":"active","entry_version":"5","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0000651 entry version 5; citation taken from the compound evidence level","reference":"DOI:10.1271/bbb.70477"}],"genome_accession":"genbank:AB307968.1","link_evidence_basis":"CLUSTER_UNSTATED","organism_label":"Streptomyces
    argenteolus","organism_taxon_id":"NCBITaxon:67274"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0000651","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0000651 entry version 5; citation taken from the compound evidence level","reference":"DOI:10.1271/bbb.70477"}],"evidence_basis":"SOURCE_ASSERTION","notes":"Locus
    evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this
    field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"5","taxon_id":"NCBITaxon:67274","taxon_label":"Streptomyces
    argenteolus"}],"producer_taxon_groups":["ACTINOBACTERIAL"],"source_concepts":[{"minted_identifier":"naturalproductmech:mibig-90363bf123","source":"MIBIG","source_id":"BGC0000651","source_label":"KS-505a","source_version":"5"}]}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: bgc-2345-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/4/owner_document
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"grounding_notes":"No 3-star ChEBI entry shares this structure,
    so the record keeps a content-hashed identifier."}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: bgc-2345-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/4/owner_document
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: bgc-2345-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/4/owner_document
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"bgc_class":["TERPENE"],"biosynthesis_origin":"NATURAL_PRODUCT","compound_classes":["Meroterpenoid"],"np_classification":{"class_results":["Friedelane
    triterpenoids"],"is_glycoside":true,"pathway_results":["Terpenoids"],"superclass_results":["Triterpenoids"],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: bgc-2345-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-DATA-001.json
  locator: /records/4/declared_structure; /records/4/smiles/status; /records/4/inchi/status;
    /records/4/smiles/computed; /records/4/inchi/computed; /records/4/comparisons;
    /records/4/atom_correspondence
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Both stored forms parsed. Exact original comparison/correspondence and
    stereo values: {"atom_correspondence":{"complete_atom_count_match":true,"full_graph_identity_established":false,"scope":"One
    chirality-aware substructure match; no independent full graph or natural identity
    claim.","smiles_to_inchi_atom_indices":[0,29,24,39,53,20,14,38,56,30,25,41,57,7,51,69,70,74,50,47,45,44,46,75,48,66,67,64,65,73,9,1,6,34,55,35,15,21,58,36,52,18,12,2,13,19,54,37,16,22,59,40,26,31,33,76,11,10,32,43,49,68,77,60,23,17,42,63,72,8,71,28,62,4,27,61,5,3]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true},"declared_structure":{"smiles":"C[C@@H]1CC2[C@@](CCC3[C@@]2([C@@H](CC([C@]3(C)C(=O)O)OC4[C@@H]([C@H]([C@@H]([C@H](O4)C(=O)O)O)O)OC)C)C)(C5[C@]1(C6CC[C@]7(C([C@@]6(CC5)C)CC[C@@]8(C7CC[C@]9(C8CC1=C(O9)C=CC2=C1C(=O)OC2(CCC(=O)OC)O)CO)C)CO)C)C","standard_inchi":"InChI=1S/C61H88O17/c1-30-25-40-54(4,21-15-39-57(40,7)31(2)26-42(58(39,8)52(70)71)75-51-48(74-10)46(66)45(65)47(76-51)49(67)68)35-13-19-53(3)36(56(30,35)6)16-22-59(28-62)37(53)14-20-55(5)38(59)17-23-60(29-63)41(55)27-32-34(77-60)12-11-33-44(32)50(69)78-61(33,72)24-18-43(64)73-9/h11-12,30-31,35-42,45-48,51,62-63,65-66,72H,13-29H2,1-10H3,(H,67,68)(H,70,71)/t30-,31-,35?,36?,37?,38?,39?,40?,41?,42?,45+,46+,47+,48-,51?,53-,54+,55-,56+,57+,58-,59-,60-,61?/m1/s1","standard_inchi_key":"DBIAGVXGCNWASW-JMNNKWMBSA-N","stereo_complete":false,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0000651"},"saved_stereo":{"inchi":{"Atom_Tetrahedral:Specified":14,"Atom_Tetrahedral:Unspecified":10},"smiles":{"Atom_Tetrahedral:Specified":14,"Atom_Tetrahedral:Unspecified":10}}}'
  snapshot_sha256: aeff6d2db3c52b75fa7cd85438a014925445302087c33263b7522f3f556e0d4c
- evidence_id: bgc-2345-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-DATA-001.json
  locator: /records/4/smiles/computed; /records/4/inchi/computed; /records/4/declared_structure;
    /records/4/literal_InChI_layers; /records/4/comparisons; /records/4/atom_correspondence
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete saved topology interpretation: Both forms represent one neutral
    C61H88O17 component, 78 heavy atoms and 88 bonds. The saved ring basis has eleven
    rings: seven saturated carbocycles, one aromatic six-carbon ring and three oxygen
    heterocycles. Four carbonyls occur in two carboxylic acids (SMILES C14 and C24),
    a lactone (C60=O61 with intraring O62) and a methyl ester (C66=O67, O68-C69).
    The separate six-membered oxygenated ring [18,19,20,21,22,23] connects to the
    larger framework through exocyclic C11-O17-C18; it bears hydroxyls at C20/C21,
    methoxy at C19 and a carboxyl substituent at C22. This complete topology supports
    a sugar-like, O-linked substructure rather than relying on the C5O detector alone.
    Its candidate anomeric centre C18 is unspecified, so alpha/beta configuration
    or a fully identified sugar residue is not assigned. Fourteen tetrahedral centres
    are specified and ten remain unresolved (SMILES 3, 7, 11, 18, 33, 35, 39, 47,
    51 and 63). Saved ring bases and atom indices are representation descriptors,
    not biochemical numbering.'
  snapshot_sha256: aeff6d2db3c52b75fa7cd85438a014925445302087c33263b7522f3f556e0d4c
- evidence_id: bgc-2345-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-execution-001.json
  locator: Whole current diagnostic-execution
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: ROOT operated one original stored-form diagnostic, exit 0, one attempt,
    preserved original streams and closed environment. This execution receipt is not
    independent scientific verification.
  snapshot_sha256: c6f0da32c1be702c997e92c5892ea02e38a069abc6c0b720fa4e1338b674661c
- evidence_id: bgc-2345-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /accepted; /DATA; /execution; /verification; /warning_scope; /limits
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: ROOT accepts the original 20 stored parses and exact original comparisons/key/capture
    joins. Two original undefined-stereo and two charge-rearrangement warnings remain
    global and unassigned. Acceptance establishes local execution integrity, not natural
    identity or full graph proof.
  snapshot_sha256: 5c7d1831ae5c8d9ffdafa16a84aaf306a7641eec7b63ed29999a7182721156f6
- evidence_id: bgc-2345-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/root-native-five-gates-acceptance-001.json
  locator: Whole current native-acceptance
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Five original local gates passed. Full QC and complete OAK coverage remain
    unavailable, so these results do not establish all required validation or a scientific
    verdict.
  snapshot_sha256: 713d96670fed493630776183217dec028aa27c64ca70142c925e14679e8064bc
- evidence_id: bgc-2345-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/root-intake-native-acceptance-001.json
  locator: Whole current intake-acceptance
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: ROOT accepts ten actual canonical intakes and exact current source ownership/input
    plans; scientific assessment is separate.
  snapshot_sha256: 97b8f40e4ce5c08c4508e916b5951f267a4aba333bf78abf8275d7c8c865e7f0
- evidence_id: bgc-2345-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/root-source-inventory-acceptance-001.json
  locator: Whole current inventory-acceptance
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: ROOT accepts the original saved inventory and current input/raw/query/row
    joins. Complete meaning reading is separately attributed in source notes.
  snapshot_sha256: efe55c8fc90acc75742e2e133be3d52885ba31a8027a7ef4736e7bc020950af9
- evidence_id: bgc-2345-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/root-source-plan-acceptance-001.json
  locator: Whole current plan-acceptance
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: ROOT accepts the actual input plan and preserved source contexts, without
    a scientific verdict.
  snapshot_sha256: ebd812deb22f4b63b07c62f2cfb77b5ccaefd41fa85e5da34e9ad033ab96431c
- evidence_id: bgc-2345-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-target-input-plan-001.json
  locator: /records/4
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Current one-record input plan with exact direct companions, predicates
    and input roles.
  snapshot_sha256: 4534eaf8666f0c106f388a2d17af4dc6b1edc20f665e7aef9a03813706c19ddb
- evidence_id: bgc-2345-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-scope-notes-001.json
  locator: /reading; /cautions; /scientific_limits
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Complete disjoint source/raw-history reading and exact carries, with compound-specific
    cautions; source planning did not adjudicate pre-intake science.
  snapshot_sha256: 8c85f257f59a062eabc086ac4dd94acabd196bf072e6d66aa20f1215dd31aaa7
- evidence_id: bgc-2345-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-scope-notes-001.json
  locator: /curation
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: ROOT explicitly opened eight implemented curation tables, including ignored
    files, over 1233 casefolded literal tokens. One taxon-only rationale hit at unrelated
    BGC0001648:1 does not support any present compound/locus strain transfer; there
    was no current key, identifier, owned-BGC, label or slug hit. Reserved decisions.tsv,
    queue and unresolved-taxon routes were not consumed. This is bounded coverage,
    not universal absence.
  snapshot_sha256: 8c85f257f59a062eabc086ac4dd94acabd196bf072e6d66aa20f1215dd31aaa7
- evidence_id: bgc-2345-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[{"last_physical_line":767,"physical_line":767,"raw_tsv_record":"BGC0000651\t5\tactive\tquestionable\tunknown\tKS-505a\t1\tC[C@@H]1CC2[C@@](CCC3[C@@]2([C@@H](CC([C@]3(C)C(=O)O)OC4[C@@H]([C@H]([C@@H]([C@H](O4)C(=O)O)O)O)OC)C)C)(C5[C@]1(C6CC[C@]7(C([C@@]6(CC5)C)CC[C@@]8(C7CC[C@]9(C8CC1=C(O9)C=CC2=C1C(=O)OC2(CCC(=O)OC)O)CO)C)CO)C)C\tInChI=1S/C61H88O17/c1-30-25-40-54(4,21-15-39-57(40,7)31(2)26-42(58(39,8)52(70)71)75-51-48(74-10)46(66)45(65)47(76-51)49(67)68)35-13-19-53(3)36(56(30,35)6)16-22-59(28-62)37(53)14-20-55(5)38(59)17-23-60(29-63)41(55)27-32-34(77-60)12-11-33-44(32)50(69)78-61(33,72)24-18-43(64)73-9/h11-12,30-31,35-42,45-48,51,62-63,65-66,72H,13-29H2,1-10H3,(H,67,68)(H,70,71)/t30-,31-,35?,36?,37?,38?,39?,40?,41?,42?,45+,46+,47+,48-,51?,53-,54+,55-,56+,57+,58-,59-,60-,61?/m1/s1\tDBIAGVXGCNWASW-JMNNKWMBSA-N\tfalse\tMeroterpenoid\tnpatlas:NPA024710|pubchem:3081782\tNCBITaxon:67274\tStreptomyces
    argenteolus\tterpene\tUnknown\tAB307968.1\t\t\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tDOI:10.1271/bbb.70477\tCOMPOUND_EVIDENCE\n","row":{"bgc_classes":"terpene","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"Meroterpenoid","compound_index":"1","compound_name":"KS-505a","database_ids":"npatlas:NPA024710|pubchem:3081782","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"5","genome_accession":"AB307968.1","locus_evidence_methods":"","locus_from":"","locus_to":"","mibig_accession":"BGC0000651","primary_reference":"DOI:10.1271/bbb.70477","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"COMPOUND_EVIDENCE","smiles":"C[C@@H]1CC2[C@@](CCC3[C@@]2([C@@H](CC([C@]3(C)C(=O)O)OC4[C@@H]([C@H]([C@@H]([C@H](O4)C(=O)O)O)O)OC)C)C)(C5[C@]1(C6CC[C@]7(C([C@@]6(CC5)C)CC[C@@]8(C7CC[C@]9(C8CC1=C(O9)C=CC2=C1C(=O)OC2(CCC(=O)OC)O)CO)C)CO)C)C","standard_inchi":"InChI=1S/C61H88O17/c1-30-25-40-54(4,21-15-39-57(40,7)31(2)26-42(58(39,8)52(70)71)75-51-48(74-10)46(66)45(65)47(76-51)49(67)68)35-13-19-53(3)36(56(30,35)6)16-22-59(28-62)37(53)14-20-55(5)38(59)17-23-60(29-63)41(55)27-32-34(77-60)12-11-33-44(32)50(69)78-61(33,72)24-18-43(64)73-9/h11-12,30-31,35-42,45-48,51,62-63,65-66,72H,13-29H2,1-10H3,(H,67,68)(H,70,71)/t30-,31-,35?,36?,37?,38?,39?,40?,41?,42?,45+,46+,47+,48-,51?,53-,54+,55-,56+,57+,58-,59-,60-,61?/m1/s1","standard_inchi_key":"DBIAGVXGCNWASW-JMNNKWMBSA-N","stereo_complete":"false","taxon_id":"NCBITaxon:67274","taxon_label":"Streptomyces
    argenteolus"},"row_sha256":"758e652cd11ffe7cd62aaf4e8f99392609be93cc509f47233658e974a341c185"}],"predicate":"exact
    complete standard_inchi_key equality","query":"DBIAGVXGCNWASW-JMNNKWMBSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2345-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 767–767, row_sha256 758e652cd11ffe7cd62aaf4e8f99392609be93cc509f47233658e974a341c185
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"bgc_classes":"terpene","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"Meroterpenoid","compound_index":"1","compound_name":"KS-505a","database_ids":"npatlas:NPA024710|pubchem:3081782","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"5","genome_accession":"AB307968.1","locus_evidence_methods":"","locus_from":"","locus_to":"","mibig_accession":"BGC0000651","primary_reference":"DOI:10.1271/bbb.70477","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"COMPOUND_EVIDENCE","smiles":"C[C@@H]1CC2[C@@](CCC3[C@@]2([C@@H](CC([C@]3(C)C(=O)O)OC4[C@@H]([C@H]([C@@H]([C@H](O4)C(=O)O)O)O)OC)C)C)(C5[C@]1(C6CC[C@]7(C([C@@]6(CC5)C)CC[C@@]8(C7CC[C@]9(C8CC1=C(O9)C=CC2=C1C(=O)OC2(CCC(=O)OC)O)CO)C)CO)C)C","standard_inchi":"InChI=1S/C61H88O17/c1-30-25-40-54(4,21-15-39-57(40,7)31(2)26-42(58(39,8)52(70)71)75-51-48(74-10)46(66)45(65)47(76-51)49(67)68)35-13-19-53(3)36(56(30,35)6)16-22-59(28-62)37(53)14-20-55(5)38(59)17-23-60(29-63)41(55)27-32-34(77-60)12-11-33-44(32)50(69)78-61(33,72)24-18-43(64)73-9/h11-12,30-31,35-42,45-48,51,62-63,65-66,72H,13-29H2,1-10H3,(H,67,68)(H,70,71)/t30-,31-,35?,36?,37?,38?,39?,40?,41?,42?,45+,46+,47+,48-,51?,53-,54+,55-,56+,57+,58-,59-,60-,61?/m1/s1","standard_inchi_key":"DBIAGVXGCNWASW-JMNNKWMBSA-N","stereo_complete":"false","taxon_id":"NCBITaxon:67274","taxon_label":"Streptomyces
    argenteolus"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2345-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"DBIAGVXGCNWASW-JMNNKWMBSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2345-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"DBIAGVXGCNWASW-JMNNKWMBSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2345-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"DBIAGVXGCNWASW-JMNNKWMBSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2345-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[{"last_physical_line":378,"physical_line":378,"raw_tsv_record":"DBIAGVXGCNWASW-JMNNKWMBSA-N\tC[C@@H]1CC2[C@@](CCC3[C@@]2([C@@H](CC([C@]3(C)C(=O)O)OC4[C@@H]([C@H]([C@@H]([C@H](O4)C(=O)O)O)O)OC)C)C)(C5[C@]1(C6CC[C@]7(C([C@@]6(CC5)C)CC[C@@]8(C7CC[C@]9(C8CC1=C(O9)C=CC2=C1C(=O)OC2(CCC(=O)OC)O)CO)C)CO)C)C\tTerpenoids\tTriterpenoids\tFriedelane
    triterpenoids\ttrue\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"Friedelane
    triterpenoids","is_glycoside":"true","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@@H]1CC2[C@@](CCC3[C@@]2([C@@H](CC([C@]3(C)C(=O)O)OC4[C@@H]([C@H]([C@@H]([C@H](O4)C(=O)O)O)O)OC)C)C)(C5[C@]1(C6CC[C@]7(C([C@@]6(CC5)C)CC[C@@]8(C7CC[C@]9(C8CC1=C(O9)C=CC2=C1C(=O)OC2(CCC(=O)OC)O)CO)C)CO)C)C","standard_inchi_key":"DBIAGVXGCNWASW-JMNNKWMBSA-N","superclass_results":"Triterpenoids"},"row_sha256":"c7881ec6b7284c0c44cfb7fe74a5f06276af88160b0522013a41ce3e5d7317f5"}],"predicate":"exact
    complete standard_inchi_key equality","query":"DBIAGVXGCNWASW-JMNNKWMBSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2345-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 378–378, row_sha256 c7881ec6b7284c0c44cfb7fe74a5f06276af88160b0522013a41ce3e5d7317f5
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"class_results":"Friedelane
    triterpenoids","is_glycoside":"true","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@@H]1CC2[C@@](CCC3[C@@]2([C@@H](CC([C@]3(C)C(=O)O)OC4[C@@H]([C@H]([C@@H]([C@H](O4)C(=O)O)O)O)OC)C)C)(C5[C@]1(C6CC[C@]7(C([C@@]6(CC5)C)CC[C@@]8(C7CC[C@]9(C8CC1=C(O9)C=CC2=C1C(=O)OC2(CCC(=O)OC)O)CO)C)CO)C)C","standard_inchi_key":"DBIAGVXGCNWASW-JMNNKWMBSA-N","superclass_results":"Triterpenoids"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2345-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[{"last_physical_line":953,"physical_line":953,"raw_tsv_record":"DBIAGVXGCNWASW-JMNNKWMBSA-N\t3081782\t\t(no
    assay data)\t\t\t\t\t\t\t\n","row":{"activity_name":"","activity_outcome":"","activity_value_um":"","aid":"","assay_name":"(no
    assay data)","assay_type":"","cid":"3081782","depositor":"","reference":"","standard_inchi_key":"DBIAGVXGCNWASW-JMNNKWMBSA-N","target_accession":""},"row_sha256":"f3b85aa5c8d437d5d19ba54519ccbd29d26e8779642b1dd727576da6b500f2bf"}],"predicate":"exact
    complete standard_inchi_key equality","query":"DBIAGVXGCNWASW-JMNNKWMBSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2345-source-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Header line 1; physical lines 953–953, row_sha256 f3b85aa5c8d437d5d19ba54519ccbd29d26e8779642b1dd727576da6b500f2bf
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"activity_name":"","activity_outcome":"","activity_value_um":"","aid":"","assay_name":"(no
    assay data)","assay_type":"","cid":"3081782","depositor":"","reference":"","standard_inchi_key":"DBIAGVXGCNWASW-JMNNKWMBSA-N","target_accession":""}]'
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2345-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"DBIAGVXGCNWASW-JMNNKWMBSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2345-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"DBIAGVXGCNWASW-JMNNKWMBSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2345-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact chebi_id from exact full-key structure
    rows","query":[]}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2345-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/source_taxa; /contexts/8/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/8/source_scope_inventory/nonorganism_matches; /contexts/8/source_scope_inventory/actual_assay_rows;
    /contexts/8/source_scope_inventory/blank_AID_sentinels; /contexts/8/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Exact source taxa and route lists; source_taxa is distinct from the empty
    forward/nonorganism and actual-assay/related routes; a blank-AID sentinel is separate:
    {"actual_assay_rows":[],"blank_AID_sentinels":[{"last_physical_line":953,"physical_line":953,"raw_tsv_record":"DBIAGVXGCNWASW-JMNNKWMBSA-N\t3081782\t\t(no
    assay data)\t\t\t\t\t\t\t\n","row":{"activity_name":"","activity_outcome":"","activity_value_um":"","aid":"","assay_name":"(no
    assay data)","assay_type":"","cid":"3081782","depositor":"","reference":"","standard_inchi_key":"DBIAGVXGCNWASW-JMNNKWMBSA-N","target_accession":""},"row_sha256":"f3b85aa5c8d437d5d19ba54519ccbd29d26e8779642b1dd727576da6b500f2bf"}],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:67274"]}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2345-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/232
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete relevant cached stanzas, with no fresh taxonomy verification:
    [{"complete_stanza":"[Term]\nid: NCBITaxon:67274\nname: Streptomyces argenteolus\n\n","id":"NCBITaxon:67274","physical_line":29950}]'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2345-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /records/4/direct_companion_paths; /records/4/direct_companion_predicates
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Exact one-hop scope, with no claim transfer: {"direct_companion_paths":[],"direct_companion_predicates":[]}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2345-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 392–433
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: The structure flag describes undefined stereocentres. ComputedClassification
    is explicitly a named/versioned prediction from structure, never a source assertion
    or an admission criterion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2345-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 142–173
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Maintained stereo_complete derives from FindMolChiralCenters and absence
    of question-mark centre tags. It is not blanket all-bond-geometry or natural-identity
    proof.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2345-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 972–1020
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Maintained seeding preserves lead source structures and named/versioned
    computed predictions separately; the computed pathway can control filing without
    becoming a source assertion.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2345-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole current profile
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: One-record claim-level scientific review requires twelve dimensions and
    truthful partial completion/unavailable-check limits.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2345-review-skill
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Whole current skill
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: The review does not edit source records; the overriding absolute no-request
    instruction limits evidence access to retained local files.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-235/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json
  accessed_at: '2026-11-04T04:28:50.246712Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 451bdae3fced338f9cab6a0065481c50af073167c8f08ea2278221cdc9bd3b9f
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-235/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json
  accessed_at: '2026-11-04T04:29:16.400882Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 855c8f91f20c1843d397c7f6cc176f7bc5b008882a65cac37c9d332069c3fa14
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-235/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json
  accessed_at: '2026-11-04T04:29:36.734590Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-235/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json
  accessed_at: '2026-11-04T04:30:13.718045Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-235/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json
  accessed_at: '2026-11-04T04:30:25.980598Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: f0f15dd29bebbfeaee4046ecb5069d24cf4a36fdd1c6d046bf9208c3c24d4d57
assessments:
- assessment_id: bgc-2345-identity
  area: identity
  topic: Retained identity and form consistency; exact natural identity unverified
  outcome: supported
  summary: The owner naturalproductmech:mibig-90363bf123 retains KS-505a, full key
    DBIAGVXGCNWASW-JMNNKWMBSA-N, NPatlas:NPA024710 and PubChem:3081782 as source metadata.
    Its MINTED grounding and historical no-3-star-ChEBI-match note remain limited
    to the retained source scope and empty exact-key ChEBI join. Both stored forms
    agree on C61H88O17 and the encoded partial stereochemistry. The exact external
    cross-references were not fetched or independently structure-matched here, and
    ten unspecified tetrahedral centres prevent treating the name or full key as proof
    of one fully assigned natural stereoisomer. No direct companion is admitted.
  target_ids:
  - naturalproductmech:mibig-90363bf123
  evidence_ids:
  - bgc-2345-grounding-owner
  - bgc-2345-source-mibig_compounds
  - bgc-2345-query-chebi_structures
  - bgc-2345-chemistry
  - bgc-2345-direct-contexts
  dimensions:
  - name: standard_inchi_key
    value: DBIAGVXGCNWASW-JMNNKWMBSA-N; exact full retained key, not a name or connectivity-block
      substitute.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2345-grounding-owner
    - bgc-2345-source-mibig_compounds
    - bgc-2345-query-chebi_structures
    - bgc-2345-chemistry
    - bgc-2345-direct-contexts
  - name: grounding_scope
    value: The owner naturalproductmech:mibig-90363bf123 retains KS-505a, full key
      DBIAGVXGCNWASW-JMNNKWMBSA-N, NPatlas:NPA024710 and PubChem:3081782 as source
      metadata. Its MINTED grounding and historical no-3-star-ChEBI-match note remain
      limited to the retained source scope and empty exact-key ChEBI join. Both stored
      forms agree on C61H88O17 and the encoded partial stereochemistry. The exact
      external cross-references were not fetched or independently structure-matched
      here, and ten unspecified tetrahedral centres prevent treating the name or full
      key as proof of one fully assigned natural stereoisomer. No direct companion
      is admitted.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2345-grounding-owner
    - bgc-2345-source-mibig_compounds
    - bgc-2345-query-chebi_structures
    - bgc-2345-chemistry
    - bgc-2345-direct-contexts
- assessment_id: bgc-2345-representation
  area: representation
  topic: Stored molecular representation
  outcome: supported
  summary: 'Both forms represent one neutral C61H88O17 component, 78 heavy atoms and
    88 bonds. The saved ring basis has eleven rings: seven saturated carbocycles,
    one aromatic six-carbon ring and three oxygen heterocycles. Four carbonyls occur
    in two carboxylic acids (SMILES C14 and C24), a lactone (C60=O61 with intraring
    O62) and a methyl ester (C66=O67, O68-C69). The separate six-membered oxygenated
    ring [18,19,20,21,22,23] connects to the larger framework through exocyclic C11-O17-C18;
    it bears hydroxyls at C20/C21, methoxy at C19 and a carboxyl substituent at C22.
    This complete topology supports a sugar-like, O-linked substructure rather than
    relying on the C5O detector alone. Its candidate anomeric centre C18 is unspecified,
    so alpha/beta configuration or a fully identified sugar residue is not assigned.
    Fourteen tetrahedral centres are specified and ten remain unresolved (SMILES 3,
    7, 11, 18, 33, 35, 39, 47, 51 and 63). Saved ring bases and atom indices are representation
    descriptors, not biochemical numbering. The maintained stereo_complete field is
    derived from tetrahedral-centre assignment and is not a universal bond-geometry,
    optical-sign or natural-identity certificate. All ten original pair-comparison
    flags and complete atom-count correspondence are true for this record, while full_graph_identity_established
    remains false. No new molecular parse or alternate structure was introduced.'
  target_ids:
  - naturalproductmech:mibig-90363bf123
  evidence_ids:
  - bgc-2345-chemistry
  - bgc-2345-topology
  - bgc-2345-grounding-owner
  - bgc-2345-stereo-method
  - bgc-2345-structure-schema
  dimensions:
  - name: stereochemistry_scope
    value: 'Both forms represent one neutral C61H88O17 component, 78 heavy atoms and
      88 bonds. The saved ring basis has eleven rings: seven saturated carbocycles,
      one aromatic six-carbon ring and three oxygen heterocycles. Four carbonyls occur
      in two carboxylic acids (SMILES C14 and C24), a lactone (C60=O61 with intraring
      O62) and a methyl ester (C66=O67, O68-C69). The separate six-membered oxygenated
      ring [18,19,20,21,22,23] connects to the larger framework through exocyclic
      C11-O17-C18; it bears hydroxyls at C20/C21, methoxy at C19 and a carboxyl substituent
      at C22. This complete topology supports a sugar-like, O-linked substructure
      rather than relying on the C5O detector alone. Its candidate anomeric centre
      C18 is unspecified, so alpha/beta configuration or a fully identified sugar
      residue is not assigned. Fourteen tetrahedral centres are specified and ten
      remain unresolved (SMILES 3, 7, 11, 18, 33, 35, 39, 47, 51 and 63). Saved ring
      bases and atom indices are representation descriptors, not biochemical numbering.
      The maintained stereo_complete field is derived from tetrahedral-centre assignment
      and is not a universal bond-geometry, optical-sign or natural-identity certificate.
      All ten original pair-comparison flags and complete atom-count correspondence
      are true for this record, while full_graph_identity_established remains false.
      No new molecular parse or alternate structure was introduced.'
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2345-chemistry
    - bgc-2345-topology
    - bgc-2345-grounding-owner
    - bgc-2345-stereo-method
    - bgc-2345-structure-schema
  - name: representation_correspondence
    value: All ten saved comparisons and complete atom-count correspondence are true;
      original full_graph_identity_established remains false. Stored normalization
      is not independent exact natural-graph identity.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2345-chemistry
    - bgc-2345-topology
    - bgc-2345-grounding-owner
    - bgc-2345-stereo-method
    - bgc-2345-structure-schema
- assessment_id: bgc-2345-provenance
  area: provenance
  topic: Producer and locus evidence
  outcome: supported
  summary: MIBiG row 767 belongs to BGC0000651 version 5 and asserts Streptomyces
    argenteolus, NCBITaxon:67274, as producer at SOURCE_ASSERTION grade. The AB307968.1
    TERPENE locus is CLUSTER_UNSTATED and has no retained experimental method. The
    source compound class Meroterpenoid is preserved separately from the model prediction.
    This exact row supports its database provenance, but does not establish the complete
    pathway, individual glycosyltransferase, sugar donor or exact natural stereochemical
    product. The cached species stanza is a local taxonomic record, not refreshed
    production verification.
  target_ids:
  - naturalproductmech:mibig-90363bf123
  evidence_ids:
  - bgc-2345-origin-owner
  - bgc-2345-source-mibig_compounds
  - bgc-2345-cached-taxonomy
  - bgc-2345-source-routes
  dimensions:
  - name: taxon_scope
    value: MIBiG row 767 belongs to BGC0000651 version 5 and asserts Streptomyces
      argenteolus, NCBITaxon:67274, as producer at SOURCE_ASSERTION grade. The AB307968.1
      TERPENE locus is CLUSTER_UNSTATED and has no retained experimental method. The
      source compound class Meroterpenoid is preserved separately from the model prediction.
      This exact row supports its database provenance, but does not establish the
      complete pathway, individual glycosyltransferase, sugar donor or exact natural
      stereochemical product. The cached species stanza is a local taxonomic record,
      not refreshed production verification.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2345-origin-owner
    - bgc-2345-source-mibig_compounds
    - bgc-2345-cached-taxonomy
    - bgc-2345-source-routes
  - name: producer_evidence
    value: MIBiG row 767 belongs to BGC0000651 version 5 and asserts Streptomyces
      argenteolus, NCBITaxon:67274, as producer at SOURCE_ASSERTION grade. The AB307968.1
      TERPENE locus is CLUSTER_UNSTATED and has no retained experimental method. The
      source compound class Meroterpenoid is preserved separately from the model prediction.
      This exact row supports its database provenance, but does not establish the
      complete pathway, individual glycosyltransferase, sugar donor or exact natural
      stereochemical product. The cached species stanza is a local taxonomic record,
      not refreshed production verification.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2345-origin-owner
    - bgc-2345-source-mibig_compounds
    - bgc-2345-cached-taxonomy
    - bgc-2345-source-routes
  - name: locus_evidence
    value: MIBiG row 767 belongs to BGC0000651 version 5 and asserts Streptomyces
      argenteolus, NCBITaxon:67274, as producer at SOURCE_ASSERTION grade. The AB307968.1
      TERPENE locus is CLUSTER_UNSTATED and has no retained experimental method. The
      source compound class Meroterpenoid is preserved separately from the model prediction.
      This exact row supports its database provenance, but does not establish the
      complete pathway, individual glycosyltransferase, sugar donor or exact natural
      stereochemical product. The cached species stanza is a local taxonomic record,
      not refreshed production verification.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2345-origin-owner
    - bgc-2345-source-mibig_compounds
    - bgc-2345-cached-taxonomy
    - bgc-2345-source-routes
- assessment_id: bgc-2345-citations
  area: evidence
  topic: Citation scope
  outcome: supported
  summary: The selected MIBiG compound row explicitly carries DOI:10.1271/bbb.70477
    at COMPOUND_EVIDENCE level. This source placement is retained without upgrading
    it to a newly read primary experiment or a complete gene-to-product demonstration.
    The NPatlas and PubChem identifiers are identity cross-references, not additional
    independent experiments. No newly accessed publication, assay report or sequence
    supplies missing stereochemical or pathway assignments.
  target_ids:
  - naturalproductmech:mibig-90363bf123
  evidence_ids:
  - bgc-2345-grounding-owner
  - bgc-2345-origin-owner
  - bgc-2345-source-mibig_compounds
  - bgc-2345-source-notes
  - bgc-2345-direct-contexts
  dimensions:
  - name: citation_scope
    value: The selected MIBiG compound row explicitly carries DOI:10.1271/bbb.70477
      at COMPOUND_EVIDENCE level. This source placement is retained without upgrading
      it to a newly read primary experiment or a complete gene-to-product demonstration.
      The NPatlas and PubChem identifiers are identity cross-references, not additional
      independent experiments. No newly accessed publication, assay report or sequence
      supplies missing stereochemical or pathway assignments.
    definition: Database provenance, retained historical primary-experiment support
      and occurrence citations have distinct scopes; repeated placements do not establish
      independent studies, and no fresh external access is claimed.
    evidence_ids:
    - bgc-2345-grounding-owner
    - bgc-2345-origin-owner
    - bgc-2345-source-mibig_compounds
    - bgc-2345-source-notes
    - bgc-2345-direct-contexts
- assessment_id: bgc-2345-occurrence
  area: evidence
  topic: Occurrence and assay scope
  outcome: supported
  summary: The owner contains no occurrence, bioactivity or molecular-target object.
    The exact LOTUS, ChEBI-origin and CyanometDB joins have no occurrence result.
    PubChem row 953 retains CID3081782 with a blank AID and is a no-assay sentinel;
    it must not be interpreted as inactivity, a measured endpoint or a target assignment.
    BindingDB and AntibioticMech joins have no matching target result. The source
    producer assertion remains distinct from an observed occurrence, and the retained
    name is not used to infer an unrecorded pharmacological mechanism.
  target_ids:
  - naturalproductmech:mibig-90363bf123
  evidence_ids:
  - bgc-2345-occurrence-owner
  - bgc-2345-assay-owner
  - bgc-2345-query-lotus_occurrences
  - bgc-2345-query-chebi_origins
  - bgc-2345-query-cyanometdb_occurrences
  - bgc-2345-query-pubchem_bioassay
  - bgc-2345-source-pubchem_bioassay
  - bgc-2345-query-bindingdb_targets
  - bgc-2345-query-antibioticmech_inchikeys
  - bgc-2345-source-routes
  - bgc-2345-cached-taxonomy
  - bgc-2345-source-notes
  dimensions:
  - name: occurrence_scope
    value: The owner contains no occurrence, bioactivity or molecular-target object.
      The exact LOTUS, ChEBI-origin and CyanometDB joins have no occurrence result.
      PubChem row 953 retains CID3081782 with a blank AID and is a no-assay sentinel;
      it must not be interpreted as inactivity, a measured endpoint or a target assignment.
      BindingDB and AntibioticMech joins have no matching target result. The source
      producer assertion remains distinct from an observed occurrence, and the retained
      name is not used to infer an unrecorded pharmacological mechanism.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2345-occurrence-owner
    - bgc-2345-assay-owner
    - bgc-2345-query-lotus_occurrences
    - bgc-2345-query-chebi_origins
    - bgc-2345-query-cyanometdb_occurrences
    - bgc-2345-query-pubchem_bioassay
    - bgc-2345-source-pubchem_bioassay
    - bgc-2345-query-bindingdb_targets
    - bgc-2345-query-antibioticmech_inchikeys
    - bgc-2345-source-routes
    - bgc-2345-cached-taxonomy
    - bgc-2345-source-notes
  - name: assay_target_scope
    value: No written bioactivity or molecular target and no actual assay/target result
      in the exact retained PubChem/BindingDB/AntibioticMech joins. A blank-AID sentinel,
      where present, is not an activity result. This is a bounded source result, not
      global inactivity or absence.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2345-occurrence-owner
    - bgc-2345-assay-owner
    - bgc-2345-query-lotus_occurrences
    - bgc-2345-query-chebi_origins
    - bgc-2345-query-cyanometdb_occurrences
    - bgc-2345-query-pubchem_bioassay
    - bgc-2345-source-pubchem_bioassay
    - bgc-2345-query-bindingdb_targets
    - bgc-2345-query-antibioticmech_inchikeys
    - bgc-2345-source-routes
    - bgc-2345-cached-taxonomy
    - bgc-2345-source-notes
- assessment_id: bgc-2345-classification
  area: consistency
  topic: Computed classification applicability
  outcome: supported
  summary: 'The source compound class Meroterpenoid and BGC TERPENE class are separately
    retained from NPClassifier npclassifier.gnps2.org@2026-09-07 Terpenoids/Triterpenoids/Friedelane
    triterpenoids with is_glycoside:true. The complete graph supplies a bounded structural
    rationale for glycoside applicability: a separate oxygenated C5O ring is joined
    by an exocyclic O linkage and carries multiple oxygen substituents. That supports
    the flag’s applicability without proving a particular residue, anomeric configuration,
    biosynthetic origin or the finer Friedelane assignment. The C61 total includes
    substantial substituent structure and cannot alone invalidate or prove the scaffold
    prediction. No faithful-ingestion or source-identity defect is established by
    these differing classification scopes.'
  target_ids:
  - naturalproductmech:mibig-90363bf123
  evidence_ids:
  - bgc-2345-classification-owner
  - bgc-2345-source-npclassifier
  - bgc-2345-source-mibig_compounds
  - bgc-2345-chemistry
  - bgc-2345-topology
  - bgc-2345-structure-schema
  - bgc-2345-classification-seeder
  dimensions:
  - name: classification_applicability
    value: 'The source compound class Meroterpenoid and BGC TERPENE class are separately
      retained from NPClassifier npclassifier.gnps2.org@2026-09-07 Terpenoids/Triterpenoids/Friedelane
      triterpenoids with is_glycoside:true. The complete graph supplies a bounded
      structural rationale for glycoside applicability: a separate oxygenated C5O
      ring is joined by an exocyclic O linkage and carries multiple oxygen substituents.
      That supports the flag’s applicability without proving a particular residue,
      anomeric configuration, biosynthetic origin or the finer Friedelane assignment.
      The C61 total includes substantial substituent structure and cannot alone invalidate
      or prove the scaffold prediction. No faithful-ingestion or source-identity defect
      is established by these differing classification scopes.'
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2345-classification-owner
    - bgc-2345-source-npclassifier
    - bgc-2345-source-mibig_compounds
    - bgc-2345-chemistry
    - bgc-2345-topology
    - bgc-2345-structure-schema
    - bgc-2345-classification-seeder
- assessment_id: bgc-2345-completion
  area: completeness
  topic: Scientific completion
  outcome: unknown
  summary: Complete owner/history, actual intake and source ownership, all retained
    rows/no-match frames and relevant cache, and both full 78-atom/88-bond molecular
    forms were read. The source stereo_complete:false agrees with ten unresolved centres.
    No mechanism reader applies because no mechanism roots or components are declared.
    Accepted diagnostics and local gates retain their limited scope; Full QC, complete
    OAK and fresh primary/identity/sequence checks remain unavailable. This is a partial
    scientific review with explicit sugar and stereochemical limits and no supported
    curation finding.
  target_ids:
  - naturalproductmech:mibig-90363bf123
  evidence_ids:
  - bgc-2345-owner
  - bgc-2345-capture
  - bgc-2345-intake
  - bgc-2345-plan
  - bgc-2345-intake-acceptance
  - bgc-2345-inventory-acceptance
  - bgc-2345-plan-acceptance
  - bgc-2345-source-notes
  - bgc-2345-curation-scope
  - bgc-2345-diagnostic-execution
  - bgc-2345-diagnostic-acceptance
  - bgc-2345-native-acceptance
  - bgc-2345-review-profile
  - bgc-2345-review-skill
  dimensions:
  - name: review_completion
    value: 'Partial: complete actual evidence and saved forms assessed; no maintained
      mechanism reader applies. Full QC/OAK and fresh primary/identity authority remain
      unavailable.'
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2345-owner
    - bgc-2345-capture
    - bgc-2345-intake
    - bgc-2345-plan
    - bgc-2345-intake-acceptance
    - bgc-2345-inventory-acceptance
    - bgc-2345-plan-acceptance
    - bgc-2345-source-notes
    - bgc-2345-curation-scope
    - bgc-2345-diagnostic-execution
    - bgc-2345-diagnostic-acceptance
    - bgc-2345-native-acceptance
    - bgc-2345-review-profile
    - bgc-2345-review-skill
findings: []
actions: []
limitations:
- All evidence is retained locally. No external identifier, taxonomy, primary publication,
  protein sequence or natural stereochemical assignment was refreshed under the absolute
  no-request instruction.
- Full QC and complete OAK authority coverage remain unavailable. Local gate and parse
  success establish only their explicit mechanical scope. No maintained reader applies
  to this owner.
- Exact no-match joins are bounded by saved predicates/snapshots. Shared names, loci,
  taxa, citations or companions do not transfer compound-specific production, activity,
  mechanism or independent-study status.
- Two original undefined-stereo and two charge-rearrangement warnings are global and
  unassigned. No additional molecular/YAML parse, source query or target invocation
  occurred during this scientific authoring.
- No source record, native status or history is edited. Any supported future correction
  belongs to the maintained source/curator owners listed in the actual canonical intake.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Complete owner/history and actual intake were read. Full source payload meanings
  and direct-companion/raw-history carries remain explicitly attributed in pinned
  source notes.
- 'BGC personally read all ten first-five molecular forms: 302 atom rows / 334 bond
  rows plus complete scalars, ring/stereo/motif tables and original comparisons/maps.
  Diagnostic indices are zero-based, not biochemical locants.'
- ROOT operated original activation/capture, collector/composer, canonical intakes
  and chemistry; Native operated original gates and the one applicable Juniperol maintained
  reader. BGC authored source planning and these scientific assessments without invoking
  any target during scientific authoring.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-235
```
