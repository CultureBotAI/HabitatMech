# Remediation review: duodenum__00ca3b2c

- Review: 20261025T151004Z-duodenum__00ca3b2c-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-25T15:05:00Z
- Finished UTC: 2026-10-25T15:10:04Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Removed the guarded GOLD context-parent contribution (#2265). Identity, native status, broader ontology parents, and source observations are preserved. The global NARROW source-attestation endpoint finding (#1398) remains explicitly open.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding on data/habitats/host_associated/duodenum__00ca3b2c.yaml after bounded Cycle 2 Stage 5 remediation.

Selection: One of nine repaired targets from the digestive_system__87922027-through-ear_canal__7b012d70 cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a4778d4cff07ec783dd596044d9b00921e3925f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.d1ffda8340 | data/habitats/host_associated/duodenum__00ca3b2c.yaml | generated | Duodenum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.d1ffda8340 | Completed 2026-10-25T10:35:30Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.d1ffda8340 | Completed 2026-10-25T10:35:30Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.d1ffda8340 | Completed 2026-10-25T15:09:00Z. No issues found; 851 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.d1ffda8340 | Completed 2026-10-25T10:35:45Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.d1ffda8340 | Completed 2026-10-25T15:09:10Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.d1ffda8340 | Completed 2026-10-25T10:36:14Z. validated 43 causal-graph curation file(s) with 43 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.d1ffda8340 | Completed 2026-10-25T15:09:15Z. term-request table is current (658 terms). |
| validate-products | passed | True | habitatmech:GOLD.d1ffda8340 | Completed 2026-10-25T10:39:05Z. OK_CANONICAL: 1184, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2063. All id&lt;-&gt;label pairs correspond. |
| Baseline full native QC in CI | passed | True | habitatmech:GOLD.d1ffda8340 | Authoritative Build and test quality gate and label-correspondence succeeded on the exact working-tree base revision 6a4778d4cff07ec783dd596044d9b00921e3925f; verified at 2026-10-25T15:09:20Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/40202979514 |
| pytest counterfactual review repairs | passed | True | habitatmech:GOLD.d1ffda8340 | Completed 2026-10-25T15:09:30Z. 2 passed; exact 9-record counterfactual diff verified. |
| curation-floor | passed | True | habitatmech:GOLD.d1ffda8340 | Completed 2026-10-25T15:09:35Z. Floor satisfied across all 13 metrics. |
| render-check | passed | True | habitatmech:GOLD.d1ffda8340 | Completed 2026-10-25T15:09:45Z. rendered 3209 habitat pages, 739 redirect stubs, 8 categories, 683 term requests; pages/ is in step with the corpus. |

## Scientific And Domain Assessments

### Native validity and reproduction after bounded remediation

schema: supported. Targets: habitatmech:GOLD.d1ffda8340.

Individual schema, strict 24-target validation, 851 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 43 causal overlays, 658 term requests, curation floor, site parity, and counterfactual regression tests passed.

### Identity, definition, hierarchy and aliases

identity: concern. Targets: habitatmech:GOLD.d1ffda8340.

habitatmech:GOLD.d1ffda8340: Duodenum; NARROW/SEEDED; parents ["UBERON:0002114"]. Excluded only the false GOLD context-parent contribution habitatmech:GOLD.f131dcac3d (#2265). Global NARROW mapping-predicate endpoint contract (#1398) remains open.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.d1ffda8340.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": 3, "unit": "ORGANISM"}]. Zero counts are omitted; unrelated parent counts are not combined.

### Predecessor finding reconciliation

representation: concern. Targets: habitatmech:GOLD.d1ffda8340.

Every predecessor finding preserves its stable issue_key and exact lineage. F1 is resolved under #2265; F2 remains open under corpus-wide issue #1398.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.d1ffda8340.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce SEEDED / NARROW; this read-only review does not mutate generated records.

## Findings

### F1: Human duodenum retains whole-organ Small intestine GOLD parent as a superclass

major / resolved / confirmed; issue key: duodenum--00ca3b2c-context-parent.

Add an exclusion row in curation/gold_parent_exclusions.tsv for habitatmech:GOLD.d1ffda8340 on GOLD path 'Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Small intestine &gt; Duodenum' excluding parent_id habitatmech:GOLD.f131dcac3d, preserving ontology parent UBERON:0002114 (duodenum).

Disposition: Excluded only the guarded GOLD source-context contribution habitatmech:GOLD.f131dcac3d in curation/gold_parent_exclusions.tsv (#2265). Independent valid parents, status, and all source observations remain intact.

### F2: Narrow mapping predicate points to a minted source-path record

major / open / confirmed; issue key: duodenum--00ca3b2c-mapping-endpoint-contract.

Resolve the mapping_predicate endpoint contract so skos:narrowMatch expresses the relation between the GOLD source path and the broader ontology parent UBERON:0002114 (duodenum) rather than the minted record identifier habitatmech:GOLD.d1ffda8340.

Disposition: The retained NARROW source/record endpoint mismatch (#1398) is unchanged; a guarded GOLD context-parent exclusion does not alter the global SourceAttestation.mapping_predicate endpoint contract.

## Recommended Actions And Acceptance Checks

### ACT2

Resolve the mapping_predicate endpoint contract so skos:narrowMatch expresses the relation between the GOLD source path and the broader ontology parent UBERON:0002114 (duodenum) rather than the minted record identifier habitatmech:GOLD.d1ffda8340. No repair is performed by this read-only review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/duodenum__00ca3b2c.yaml; Entire YAML | supports | {"identifier": "habitatmech:GOLD.d1ffda8340", "label": "Duodenum", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0002114"], "synonyms": [], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:5023", "source_label": "Duodenum", "source_path": "Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Small intestine &gt; Duodenum", "mapping_predicate": "skos:narrowMatch", "assertion_count": 3, "assertion_unit": "ORGANISM"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}, {"timestamp": "2026-10-25T00:00:00Z", "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.f131dcac3d for habitatmech:GOLD.d1ffda8340 (Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Small intestine &gt; Duodenum). Review https://github.com/CultureBotAI/HabitatMech/issues/2265 : Digestive tract/tube is a tubular subdivision of the digestive system, not the entire digestive system; duodenal ulcer is a mucosal lesion/disease concept, not a subtype of the whole small intestine; duodenum is an intestinal segment, not the entire small intestine; ear is a sense organ, not the entire auditory/hearing system; ear canal is a tubular meatus of the outer ear, not the entire outer ear. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target habitatmech:GOLD.d1ffda8340. Shared mapping endpoints #1398 remain separate."}]} |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, not-applicable disease bins, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.d1ffda8340, grounding_status=NARROW, mapping_status=SEEDED, parent_habitats=["UBERON:0002114"]. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 756 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Small intestine &gt; Duodenum", "depth": "5", "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_subtype": "Small intestine", "ecosystem_type": "Digestive system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:5023", "leaf_label": "Duodenum", "organism_count": "3", "specific_ecosystem": "Duodenum", "study_count": "0", "total_assertions": "3"}, "row": 756}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 13119 | supports | [{"data": {"definition": "The first part of the small intestine. At the junction of the stomach and the duodenum the alimentary canal is inflected. The duodenum first goes anteriorly for a short distance, turns dorsally, and eventually caudally, thus it is a U-shaped structure with two horizontal sections (a ventral and a dorsal one).", "deprecated": "", "directly_referenced": "FALSE", "label": "duodenum", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "proximal intestine&#124;upper intestine", "term_id": "UBERON:0002114"}, "row": 13119}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 11338 | supports | [{"data": {"object": "UBERON:0004921", "predicate": "rdfs:subClassOf", "subject": "UBERON:0002114"}, "row": 11338}] |
| EP2 | data/habitats/host_associated/small_intestine__ce3c8e90.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": null, "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.f131dcac3d", "label": "Small intestine", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0002108", "habitatmech:GOLD.f6720bccf0"], "source_attestations": [{"assertion_count": 1, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:narrowMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:5022", "source_label": "Small intestine", "source_path": "Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Small intestine"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'duodenum__00ca3b2c&#124;habitatmech:GOLD.d1ffda8340' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |
| EPREV | reviews/structured/20261025T104028Z-duodenum__00ca3b2c-record/review.yaml; Every immutable Stage 4 baseline finding | supports | Exact predecessor keys and findings reconciled; original inspected source scope preserved. |
| ETEST | tests/test_digestive_tract_to_ear_canal_review_repairs.py; Complete full-corpus counterfactual regression suite | supports | Exactly nine records differ from the counterfactual baseline: eight guarded GOLD context-parent removals (#2265) and one bare host-clade exact-alias exclusion (#2266). |
| EPARENTS | curation/gold_parent_exclusions.tsv; TSV line 4 | supports | [[4, "habitatmech:GOLD.d1ffda8340\tHost-associated &gt; Mammals: Human &gt; Digestive system &gt; Small intestine &gt; Duodenum\thabitatmech:GOLD.f131dcac3d\tantigravity\t2026-10-25\tReview https://github.com/CultureBotAI/HabitatMech/issues/2265 : Digestive tract/tube is a tubular subdivision of the digestive system, not the entire digestive system; duodenal ulcer is a mucosal lesion/disease concept, not a subtype of the whole small intestine; duodenum is an intestinal segment, not the entire small intestine; ear is a sense organ, not the entire auditory/hearing system; ear canal is a tubular meatus of the outer ear, not the entire outer ear. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target habitatmech:GOLD.d1ffda8340. Shared mapping endpoints #1398 remain separate."]] |
| EHIST | history/other/gold_parent_exclusions/2026-10-25T150000Z-antigravity-226501.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2265 recorded and validated. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,063 no-adapter pairs; this is not whole-corpus identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in this pre-save observation. Baseline full QC is separately identified as CI evidence.
- iModulonDB is not applicable: the target has no gene, regulator or expression-module assertion. No paid research or scientific-status promotion was performed.
- Saved against working-tree repairs atop main commit 6a4778d4cff07ec783dd596044d9b00921e3925f; all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261025T104028Z-duodenum__00ca3b2c-record with exact issue_key and previous_occurrences lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T151004Z-duodenum__00ca3b2c-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: duodenum__00ca3b2c'
started_at: '2026-10-25T15:05:00Z'
finished_at: '2026-10-25T15:10:04Z'
reviewer:
  identity: antigravity
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Same agent inspected the full target and source evidence; not
    independent human or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: Removed the guarded GOLD context-parent contribution (#2265). Identity, native
  status, broader ontology parents, and source observations are preserved. The global
  NARROW source-attestation endpoint finding (#1398) remains explicitly open.
source:
  git_revision: 6a4778d4cff07ec783dd596044d9b00921e3925f
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 4544b5d2c11fbbb3a46cd8a65f7e664363df78c1000c590aab533219f9eec59b
    role: context
  - path: .claude/skills/review-yaml-category/SKILL.md
    sha256: 4a43388a0a8863b06c66cef795db0b9cc12c1507af727f2f672fd97f18309e0e
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: d429c8bb74f521df9a77a90b216a44fc6959ee28efb1fa17a93582536caa8bce
    role: context
  - path: CLAUDE.md
    sha256: bcd9e1c631a4ec7313b7662e2b17fcd9504eed19385577c728440ca78fc55efb
    role: context
  - path: conf/id_label_targets.yaml
    sha256: e100d84aabccaeb00c1a60246142b3cafcec009dbfba58f5cc319c35adddb633
    role: context
  - path: conf/record_review.yaml
    sha256: c2f5d0eb4c5744f5fe354c92184ddab144dc2688dba952b032b4f3d597bc08d6
    role: context
  - path: conf/sources.yaml
    sha256: a8e069f9278068b57fa234f43e03c8d893f857827b83fd10cfa92d6815aed642
    role: context
  - path: curation/decisions.tsv
    sha256: 98268bc72604b7311841d844a0b603421b90098de22ab7f5d29d04ee4ce77308
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 22eb5da5692d90c933aecd0a48c43702b5accbcc7bfa9bc0d47b067e36382ba3
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: d3608f94d77d1709c6fa01e93800e326853b9c027b080692128e80a6039f5c28
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: dd65420687330a236268af6c4e2480be862d19d1c79feb3bea036a7e3c80b56d
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: ee559f7b45b4af2d72a078c45d1a3b676785d34305f286e9738f95771dbaccfd
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: c662d1843091ebe6df1fb05accc52bf78c7e19c6be035450a916397a6cac4f9a
    role: context
  - path: data/habitats/host_associated/duodenum__00ca3b2c.yaml
    sha256: 9fc23470528fec848af6c4595dbbbe0e58680b79585f50f73a8805d98a230ff2
    role: target
  - path: data/habitats/host_associated/small_intestine__ce3c8e90.yaml
    sha256: 882898970e9631588f0933215f65a9743eb9700f68f58bde5c86bea628c24863
    role: context
  - path: data/raw/GOLD_MANIFEST.yaml
    sha256: 99ec487ae02d512cfb75440685f927abe907effe52cb755feb095631e8841489
    role: context
  - path: data/raw/MANIFEST.yaml
    sha256: 4657672d429be35e551ceef4a1204ab0a8120558ce63e2a2b74188eee94b8480
    role: context
  - path: data/raw/bacdive_isolation_sources.tsv
    sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
    role: context
  - path: data/raw/bacdive_source_taxa.tsv
    sha256: 08471c12f887882e2a6af8f078166b1f59ed7e2b24eb7edbe43a7fc77dfbad44
    role: context
  - path: data/raw/environment_parameters.tsv
    sha256: a75d0f565d8ee2498188ff98b17d0ab325ae4f782601bf4414eff6e86c13e0f9
    role: context
  - path: data/raw/gold_ecosystem_paths.tsv
    sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
    role: context
  - path: data/raw/gold_path_biosamples.tsv
    sha256: 97cd7c8d0e731d07a85db6986dbcf9e49096a3c7988bd90a855599f492fe619e
    role: context
  - path: data/raw/gold_path_triads.tsv
    sha256: b1717bd8fc4fdcd6a1a132f4eb32df3638b01ddf7d78f9a5797f110ee2b1e8d6
    role: context
  - path: data/raw/gold_studies.tsv
    sha256: fa7aaa46f288d10c453bb723e6cf486cde646a003559414b5523cc3883a84c8c
    role: context
  - path: data/raw/isolation_source_groundings.tsv
    sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
    role: context
  - path: data/raw/madin_habitat_taxa.tsv
    sha256: d30854cfcffca0405914d04071ac47053938d354d5df250125843131b7c91fd7
    role: context
  - path: data/raw/madin_habitats.tsv
    sha256: 2ae1756f40242600365c49bfbdada4bce5fc8b86630426bb34892f055e5a5c93
    role: context
  - path: data/raw/ontology_subclass_edges.tsv
    sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
    role: context
  - path: data/raw/ontology_terms.tsv
    sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
    role: context
  - path: data/raw/prego_habitat_taxa.tsv
    sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
    role: context
  - path: data/raw/prego_habitats.tsv
    sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
    role: context
  - path: docs/CURATION.md
    sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
    role: context
  - path: docs/HARMONIZATION.md
    sha256: ee39d3cd29115ee14f5e7386169c76c47d471ebdc2502c008c49d30fb44918f1
    role: context
  - path: docs/RESEARCH.md
    sha256: 82c5471890d310bf8fd33141d5596f847bfc1eb6091c2db6f485388435e067af
    role: context
  - path: docs/record-review-profile.md
    sha256: 105b3c8e10f43ce689b05d3089d3a8be1d713a98dd6806e11be37ebd85b10590
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/other/definition_source_label_exclusions/2026-10-25T150010Z-antigravity-226601.yaml
    sha256: 566a6b282191f35c87dc56fc94719bce890e632d2bc1717d788fbc8401bf95dc
    role: context
  - path: history/other/gold_parent_exclusions/2026-10-25T150000Z-antigravity-226501.yaml
    sha256: 2589d74cc90986a45a545b34a42c0d74bf611838320b0ac45b7a3c8f0ae91af9
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reviews/structured/20261025T104028Z-duodenum__00ca3b2c-record/review.yaml
    sha256: d3f4bc5f1825a6585f336eeb01432d168b2149fb6737e98457227ca8153fd004
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/habitatmech/curate/__init__.py
    sha256: d9837c29dc61d8c9245fdb471a68a109cea31b131cdbc0c4d51d23a8d013ce12
    role: context
  - path: src/habitatmech/curate/causal_graphs.py
    sha256: 7e2848e31997195539d5a8b292144e58b85425fc39504c8564ff5912f38ae384
    role: context
  - path: src/habitatmech/curate/curation_event.py
    sha256: 08c774d309fe988c468097518d346f07a653b283cb9b9b51c7fe79fa0af785a9
    role: context
  - path: src/habitatmech/curate/decisions.py
    sha256: f33d3e9dc95bb428e63e640d48d4074cf15e90ea666603fb16fb651d591e3f02
    role: context
  - path: src/habitatmech/curate/definition_source_label_exclusions.py
    sha256: 0c13e83fe17613e8b9f5b346d1259104172f8c1de42f911625579b903707625d
    role: context
  - path: src/habitatmech/curate/definitions.py
    sha256: decd02eea029e884ab1a8bbb51dd870edb5544906b3ddd39598147b27ce572c9
    role: context
  - path: src/habitatmech/curate/external_xrefs.py
    sha256: 8b90ec049887d3aa67e31cce7f7a04d7300421c6fedb833cc66e5d5f5f181694
    role: context
  - path: src/habitatmech/curate/gold_parent_exclusions.py
    sha256: 044d8277509a9b1f6e4f2d7ea1fb82319b41e09ffef7788738a0f4ed0d0b63af
    role: context
  - path: src/habitatmech/curate/record_annotation_corrections.py
    sha256: 15bad3d40fd95e2acc72d3ff3c74289c15fb8a1775adc523b3575c3ea8487033
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/labels.py
    sha256: eb6986c3a9c7d5a3e4651b639351f1f2d3e12d74c4bfaa92899205a1f9df0977
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
    role: context
  - path: src/habitatmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/habitatmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
  - path: tests/test_digestive_tract_to_ear_canal_review_repairs.py
    sha256: 3c1a13f47e091ff3c19f9977f74fcf778ab1db5a0c15557cb437339320b2b984
    role: context
targets:
- target_id: habitatmech:GOLD.d1ffda8340
  path: data/habitats/host_associated/duodenum__00ca3b2c.yaml
  label: Duodenum
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
scope:
  description: Full current target assessment and explicit disposition of every baseline
    finding on data/habitats/host_associated/duodenum__00ca3b2c.yaml after bounded
    Cycle 2 Stage 5 remediation.
  selection: One of nine repaired targets from the digestive_system__87922027-through-ear_canal__7b012d70
    cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.d1ffda8340
  exclusions:
  - target: Other habitat records and SSSOM/KGX products
    reason: Direct parents inform hierarchy interpretation but are not additional
      completed reviews; exports are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: .venv/bin/python -m linkml.validator.cli -s src/habitatmech/schema/habitatmech.yaml
    --target-class HabitatRecord data/habitats/host_associated/duodenum__00ca3b2c.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  summary: Completed 2026-10-25T10:35:30Z. No issues found.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/digestive_system__87922027.yaml
    data/habitats/host_associated/digestive_system__9ec9b5f9.yaml data/habitats/host_associated/digestive_system__ae8329bf.yaml
    data/habitats/host_associated/digestive_system__c5da4fa6.yaml data/habitats/host_associated/digestive_system__d7057103.yaml
    data/habitats/host_associated/digestive_system__e41cfc7b.yaml data/habitats/host_associated/digestive_system__efdbeca1.yaml
    data/habitats/host_associated/digestive_system__f6665a67.yaml data/habitats/host_associated/digestive_system_secreted_substance.yaml
    data/habitats/host_associated/digestive_tract.yaml data/habitats/host_associated/digital_dermatitis.yaml
    data/habitats/host_associated/dinoflagellates__887680eb.yaml data/habitats/host_associated/discharge.yaml
    data/habitats/host_associated/discharge__0e4f2939.yaml data/habitats/host_associated/dorsum.yaml
    data/habitats/host_associated/duodenal_mucosa.yaml data/habitats/host_associated/duodenal_ulcer.yaml
    data/habitats/host_associated/duodenum.yaml data/habitats/host_associated/duodenum__00ca3b2c.yaml
    data/habitats/host_associated/duodenum__5b2d8f0e.yaml data/habitats/host_associated/duodenum__e751f297.yaml
    data/habitats/host_associated/ear.yaml data/habitats/host_associated/ear_canal.yaml
    data/habitats/host_associated/ear_canal__7b012d70.yaml --out /tmp/c2s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  summary: 'Completed 2026-10-25T10:35:30Z. Validated 24 files; files with ERROR:
    0; total ERROR rows: 0.'
  scope_note: Closed-schema strict validation across all 24 cohort target files (and
    3,209 full-corpus files).
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_history.py history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  summary: Completed 2026-10-25T15:09:00Z. No issues found; 851 history record(s)
    valid against src/habitatmech/schema/history.yaml.
  scope_note: Full-corpus curation history validation.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: .venv/bin/python scripts/check_provenance.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  summary: 'Completed 2026-10-25T10:35:45Z. provenance current: 14 committed inventories,
    2 GOLD sources.'
  scope_note: Full-corpus raw inventory provenance verification.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  summary: 'Completed 2026-10-25T15:09:10Z. expected 3209 records, found 3209 on disk;
    missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/.'
  scope_note: Full-corpus deterministic reproduction from raw inventories and curation
    tables.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_causal_graph_curations.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  summary: Completed 2026-10-25T10:36:14Z. validated 43 causal-graph curation file(s)
    with 43 graph(s).
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  summary: Completed 2026-10-25T15:09:15Z. term-request table is current (658 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  summary: 'Completed 2026-10-25T10:39:05Z. OK_CANONICAL: 1184, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2063. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
- check_id: CCI
  name: Baseline full native QC in CI
  status: passed
  required: true
  command: gh run view 40202979514 --json status,conclusion,headSha,url
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  summary: Authoritative Build and test quality gate and label-correspondence succeeded
    on the exact working-tree base revision 6a4778d4cff07ec783dd596044d9b00921e3925f;
    verified at 2026-10-25T15:09:20Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/40202979514
  scope_note: Verified remote baseline execution on exact git revision.
- check_id: C9
  name: pytest counterfactual review repairs
  status: passed
  required: true
  command: .venv/bin/python -m pytest tests/test_digestive_tract_to_ear_canal_review_repairs.py
    -q --no-cov
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  summary: Completed 2026-10-25T15:09:30Z. 2 passed; exact 9-record counterfactual
    diff verified.
  scope_note: 'Full-corpus counterfactual regression test for Issues #2265 and #2266.'
- check_id: C10
  name: curation-floor
  status: passed
  required: true
  command: .venv/bin/python scripts/check_curation_floor.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  summary: Completed 2026-10-25T15:09:35Z. Floor satisfied across all 13 metrics.
  scope_note: Full-corpus curation floor ratchets.
- check_id: C11
  name: render-check
  status: passed
  required: true
  command: .venv/bin/python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  summary: Completed 2026-10-25T15:09:45Z. rendered 3209 habitat pages, 739 redirect
    stubs, 8 categories, 683 term requests; pages/ is in step with the corpus.
  scope_note: Full-corpus static site parity check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/duodenum__00ca3b2c.yaml
  locator: Entire YAML
  accessed_at: '2026-10-25T15:10:04Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.d1ffda8340", "label": "Duodenum", "grounding_status":
    "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0002114"], "synonyms":
    [], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:5023",
    "source_label": "Duodenum", "source_path": "Host-associated > Mammals: Human >
    Digestive system > Small intestine > Duodenum", "mapping_predicate": "skos:narrowMatch",
    "assertion_count": 3, "assertion_unit": "ORGANISM"}], "curation_history": [{"timestamp":
    "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."},
    {"timestamp": "2026-10-25T00:00:00Z", "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED",
    "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.f131dcac3d
    for habitatmech:GOLD.d1ffda8340 (Host-associated > Mammals: Human > Digestive
    system > Small intestine > Duodenum). Review https://github.com/CultureBotAI/HabitatMech/issues/2265
    : Digestive tract/tube is a tubular subdivision of the digestive system, not the
    entire digestive system; duodenal ulcer is a mucosal lesion/disease concept, not
    a subtype of the whole small intestine; duodenum is an intestinal segment, not
    the entire small intestine; ear is a sense organ, not the entire auditory/hearing
    system; ear canal is a tubular meatus of the outer ear, not the entire outer ear.
    Exclude only exact guarded GOLD source-path contributions, preserving independent
    genera and all source observations. Exact target habitatmech:GOLD.d1ffda8340.
    Shared mapping endpoints #1398 remain separate."}]}'
  snapshot_sha256: 9fc23470528fec848af6c4595dbbbe0e58680b79585f50f73a8805d98a230ff2
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, not-applicable disease bins, and
    source ownership
  accessed_at: '2026-10-25T15:10:04Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-10-25T15:10:04Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-10-25T15:10:04Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.d1ffda8340, grounding_status=NARROW,
    mapping_status=SEEDED, parent_habitats=["UBERON:0002114"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 756
  accessed_at: '2026-10-25T15:10:04Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Mammals: Human > Digestive system > Small intestine > Duodenum", "depth": "5",
    "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_subtype":
    "Small intestine", "ecosystem_type": "Digestive system", "gold_node_count": "1",
    "gold_node_ids": "gold.ecosystem:5023", "leaf_label": "Duodenum", "organism_count":
    "3", "specific_ecosystem": "Duodenum", "study_count": "0", "total_assertions":
    "3"}, "row": 756}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 13119
  accessed_at: '2026-10-25T15:10:04Z'
  support: supports
  summary: '[{"data": {"definition": "The first part of the small intestine. At the
    junction of the stomach and the duodenum the alimentary canal is inflected. The
    duodenum first goes anteriorly for a short distance, turns dorsally, and eventually
    caudally, thus it is a U-shaped structure with two horizontal sections (a ventral
    and a dorsal one).", "deprecated": "", "directly_referenced": "FALSE", "label":
    "duodenum", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "proximal
    intestine|upper intestine", "term_id": "UBERON:0002114"}, "row": 13119}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 11338
  accessed_at: '2026-10-25T15:10:04Z'
  support: supports
  summary: '[{"data": {"object": "UBERON:0004921", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:0002114"}, "row": 11338}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EP2
  kind: record_content
  reference: data/habitats/host_associated/small_intestine__ce3c8e90.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-10-25T15:10:04Z'
  support: supports
  summary: '{"definition": null, "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.f131dcac3d",
    "label": "Small intestine", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0002108",
    "habitatmech:GOLD.f6720bccf0"], "source_attestations": [{"assertion_count": 1,
    "assertion_unit": "ORGANISM", "mapping_predicate": "skos:narrowMatch", "notes":
    "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:5022", "source_label": "Small intestine",
    "source_path": "Host-associated > Mammals: Human > Digestive system > Small intestine"}]}'
  snapshot_sha256: 882898970e9631588f0933215f65a9743eb9700f68f58bde5c86bea628c24863
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'duodenum__00ca3b2c|habitatmech:GOLD.d1ffda8340' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-10-25T15:10:04Z'
  support: context_only
  summary: Structured-review traversal verified no prior target review bundle exists
    for this record; curation and history tables were inspected for all matching rows.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 395f4605d8ae0a3d9ed9e381a4108f4a9681865c.
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261025T104028Z-duodenum__00ca3b2c-record/review.yaml
  locator: Every immutable Stage 4 baseline finding
  accessed_at: '2026-10-25T15:10:04Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; original inspected source
    scope preserved.
  snapshot_sha256: d3f4bc5f1825a6585f336eeb01432d168b2149fb6737e98457227ca8153fd004
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_digestive_tract_to_ear_canal_review_repairs.py
  locator: Complete full-corpus counterfactual regression suite
  accessed_at: '2026-10-25T15:10:04Z'
  support: supports
  summary: 'Exactly nine records differ from the counterfactual baseline: eight guarded
    GOLD context-parent removals (#2265) and one bare host-clade exact-alias exclusion
    (#2266).'
  snapshot_sha256: 3c1a13f47e091ff3c19f9977f74fcf778ab1db5a0c15557cb437339320b2b984
- evidence_id: EPARENTS
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: TSV line 4
  accessed_at: '2026-10-25T15:10:04Z'
  support: supports
  summary: '[[4, "habitatmech:GOLD.d1ffda8340\tHost-associated > Mammals: Human >
    Digestive system > Small intestine > Duodenum\thabitatmech:GOLD.f131dcac3d\tantigravity\t2026-10-25\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2265 : Digestive tract/tube
    is a tubular subdivision of the digestive system, not the entire digestive system;
    duodenal ulcer is a mucosal lesion/disease concept, not a subtype of the whole
    small intestine; duodenum is an intestinal segment, not the entire small intestine;
    ear is a sense organ, not the entire auditory/hearing system; ear canal is a tubular
    meatus of the outer ear, not the entire outer ear. Exclude only exact guarded
    GOLD source-path contributions, preserving independent genera and all source observations.
    Exact target habitatmech:GOLD.d1ffda8340. Shared mapping endpoints #1398 remain
    separate."]]'
  snapshot_sha256: d3608f94d77d1709c6fa01e93800e326853b9c027b080692128e80a6039f5c28
- evidence_id: EHIST
  kind: record_content
  reference: history/other/gold_parent_exclusions/2026-10-25T150000Z-antigravity-226501.yaml
  locator: Complete curation session history event
  accessed_at: '2026-10-25T15:10:04Z'
  support: supports
  summary: 'Authorized curation event for Issue #2265 recorded and validated.'
  snapshot_sha256: 2589d74cc90986a45a545b34a42c0d74bf611838320b0ac45b7a3c8f0ae91af9
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction after bounded remediation
  outcome: supported
  summary: Individual schema, strict 24-target validation, 851 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 43 causal
    overlays, 658 term requests, curation floor, site parity, and counterfactual regression
    tests passed.
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: concern
  summary: 'habitatmech:GOLD.d1ffda8340: Duodenum; NARROW/SEEDED; parents ["UBERON:0002114"].
    Excluded only the false GOLD context-parent contribution habitatmech:GOLD.f131dcac3d
    (#2265). Global NARROW mapping-predicate endpoint contract (#1398) remains open.'
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"source": "GOLD", "count": 3, "unit": "ORGANISM"}]. Zero counts are
    omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST
- assessment_id: A4
  area: representation
  topic: Predecessor finding reconciliation
  outcome: concern
  summary: 'Every predecessor finding preserves its stable issue_key and exact lineage.
    F1 is resolved under #2265; F2 remains open under corpus-wide issue #1398.'
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST
- assessment_id: A5
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce SEEDED / NARROW; this read-only review
    does not mutate generated records.
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST
findings:
- finding_id: F1
  issue_key: duodenum--00ca3b2c-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Human duodenum retains whole-organ Small intestine GOLD parent as a superclass
  description: 'Add an exclusion row in curation/gold_parent_exclusions.tsv for habitatmech:GOLD.d1ffda8340
    on GOLD path ''Host-associated > Mammals: Human > Digestive system > Small intestine
    > Duodenum'' excluding parent_id habitatmech:GOLD.f131dcac3d, preserving ontology
    parent UBERON:0002114 (duodenum).'
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2265
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261025T104028Z-duodenum__00ca3b2c-record
    finding_id: F1
  disposition_reason: Excluded only the guarded GOLD source-context contribution habitatmech:GOLD.f131dcac3d
    in curation/gold_parent_exclusions.tsv (#2265). Independent valid parents, status,
    and all source observations remain intact.
- finding_id: F2
  issue_key: duodenum--00ca3b2c-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow mapping predicate points to a minted source-path record
  description: Resolve the mapping_predicate endpoint contract so skos:narrowMatch
    expresses the relation between the GOLD source path and the broader ontology parent
    UBERON:0002114 (duodenum) rather than the minted record identifier habitatmech:GOLD.d1ffda8340.
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  field_paths:
  - source_attestations[0].mapping_predicate
  - identifier
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261025T104028Z-duodenum__00ca3b2c-record
    finding_id: F2
  disposition_reason: The retained NARROW source/record endpoint mismatch (#1398)
    is unchanged; a guarded GOLD context-parent exclusion does not alter the global
    SourceAttestation.mapping_predicate endpoint contract.
actions:
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.d1ffda8340
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  description: Resolve the mapping_predicate endpoint contract so skos:narrowMatch
    expresses the relation between the GOLD source path and the broader ontology parent
    UBERON:0002114 (duodenum) rather than the minted record identifier habitatmech:GOLD.d1ffda8340.
    No repair is performed by this read-only review.
  generator: Controlled source/curation update in Stage 5, then just seed, guarded
    just seed-canary, just seed-apply, and dependent term-request/map/site/redirect
    regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independently valid identifiers,
    source counts/units, raw provenance, native status and history.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
limitations:
- Only the stated primary evidence and current ontology/taxonomy authorities were
  independently inspected; original specimen-level support for every source-bin member
  is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism
  or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,063 no-adapter pairs; this is not whole-corpus
  identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in
  this pre-save observation. Baseline full QC is separately identified as CI evidence.
- 'iModulonDB is not applicable: the target has no gene, regulator or expression-module
  assertion. No paid research or scientific-status promotion was performed.'
notes:
- Saved against working-tree repairs atop main commit 6a4778d4cff07ec783dd596044d9b00921e3925f;
  all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261025T104028Z-duodenum__00ca3b2c-record with exact
  issue_key and previous_occurrences lineage.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261025T104028Z-duodenum__00ca3b2c-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
