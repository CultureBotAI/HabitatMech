# Clarified current finding scope: subglacial_lake

- Review: 20261012T145330Z-subglacial_lake-clarification
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-12T14:53:27.800653Z
- Finished UTC: 2026-10-12T14:53:30.193217Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Re-read the entire unchanged target and corrected ITEM input. The remaining F1 finding concerns only liquid-freshwater ancestry; it no longer alleges that the active deep-source rationale overstates the independent study count. F2 remains resolved: three API samples from one study, distinct from the freshwater seven samples/three studies. The prior successor copied compound predecessor wording into F1 even while resolving F2. This new immutable observation corrects that review wording under #2033 without changing scientific inputs, statuses, findings counts or previous review bytes. Other scientific assessments, inspected authorities, original-occurrence limits and exact-head validation remain as in the predecessor.

## Scope And Provenance

Entire corrected target with explicitly bounded finding dispositions.

Selection: Successor review; no additional distinct-record coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 68259d4da83e48b00e9209c4079432f379aeaaf5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:03000120 | data/habitats/aquatic/subglacial_lake.yaml | generated | subglacial lake |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Post-correction native validation | passed | True | ENVO:03000120 | Actual success 2026-10-12T14:31:42.324003+00:00 to 2026-10-12T14:32:07.734097+00:00. Full-corpus validation does not expand scientific review coverage. |
| Post-correction native validation | passed | True | ENVO:03000120 | Actual success 2026-10-12T14:32:11.201747+00:00 to 2026-10-12T14:32:12.956534+00:00. Full-corpus validation does not expand scientific review coverage. |
| Post-correction native validation | passed | True | ENVO:03000120 | Actual success 2026-10-12T14:32:12.957172+00:00 to 2026-10-12T14:32:16.310312+00:00. Full-corpus validation does not expand scientific review coverage. |
| Post-correction native validation | passed | True | ENVO:03000120 | Actual success 2026-10-12T14:32:16.310938+00:00 to 2026-10-12T14:32:53.190503+00:00. Full-corpus validation does not expand scientific review coverage. |
| Post-correction native validation | passed | True | ENVO:03000120 | Actual success 2026-10-12T14:32:53.191027+00:00 to 2026-10-12T14:32:59.563076+00:00. Full-corpus validation does not expand scientific review coverage. |
| Post-correction native validation | passed | True | ENVO:03000120 | Actual success 2026-10-12T14:32:59.563616+00:00 to 2026-10-12T14:33:00.074493+00:00. Full-corpus validation does not expand scientific review coverage. |
| Post-correction native validation | passed | True | ENVO:03000120 | Actual success 2026-10-12T14:33:00.075047+00:00 to 2026-10-12T14:33:13.427177+00:00. Full-corpus validation does not expand scientific review coverage. |
| Exact corrected-head hosted QC | passed | True | ENVO:03000120 | Exact corrected-head hosted authoritative QC passed: 1057 tests, three skipped, and all native quality gates. Newly saved successor bundles require separate integrity checks. |

## Scientific And Domain Assessments

### Scoped correction and remaining scientific findings

grounding: concern. Targets: ENVO:03000120.

Re-read the entire unchanged target and corrected ITEM input. The remaining F1 finding concerns only liquid-freshwater ancestry; it no longer alleges that the active deep-source rationale overstates the independent study count. F2 remains resolved: three API samples from one study, distinct from the freshwater seven samples/three studies. The prior successor copied compound predecessor wording into F1 even while resolving F2. This new immutable observation corrects that review wording under #2033 without changing scientific inputs, statuses, findings counts or previous review bytes. Other scientific assessments, inspected authorities, original-occurrence limits and exact-head validation remain as in the predecessor. F1 remains open; F2 remains resolved.

## Findings

### F1: GOLD context does not justify a strict habitat superclass

major / open / confirmed; issue key: envo-03000120-gold-context-parent.

The merged subglacial-lake feature retains ENVO:00000198 ice-covered lake as a valid genus, but also inherits liquid fresh water ENVO:00002011 through the GOLD freshwater source context. That material is not a strict superclass of the lake feature. The separately corrected study-count rationale is not part of this remaining finding; undefined deep-subsurface parent scope is not endorsed or newly classified as false.

### F2: Deep-subsurface rationale overstates independent study support

major / resolved / confirmed; issue key: envo-03000120-study-denominator.

The original deep-source rationale overstated three samples from Gs0112339 as three independent studies. The maintained decision and generated active history now state the correct path-specific denominator; the separate freshwater evidence is unchanged.

Disposition: Remains resolved after unchanged-byte and full-record reassessment. Re-read the entire unchanged target and corrected ITEM input. The remaining F1 finding concerns only liquid-freshwater ancestry; it no longer alleges that the active deep-source rationale overstates the independent study count. F2 remains resolved: three API samples from one study, distinct from the freshwater seven samples/three studies. The prior successor copied compound predecessor wording into F1 even while resolving F2. This new immutable observation corrects that review wording under #2033 without changing scientific inputs, statuses, findings counts or previous review bytes. Other scientific assessments, inspected authorities, original-occurrence limits and exact-head validation remain as in the predecessor.

## Recommended Actions And Acceptance Checks

### A1

Assess and exclude only the unsupported exact-source contribution while retaining genuine genera and provenance; do not globally suppress a context class.

- Reassess the exact source and preserve independent valid genera, source IDs, counts/units and omitted counts.
- Change maintained owners with append-only curation history; do not rewrite generated records or saved reviews.
- Add focused regressions; inspect guarded canaries and pass strict schema, labels, history, provenance, reproduction and QC.
- Use a linked successor review for any disposition; this assessment records proposed work, not an executed repair.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| PRIOR | reviews/structured/20261012T142057Z-subglacial_lake/review.yaml | supports | Exact immutable predecessor including inspected authority snapshots and source limitations. |
| CURRENT | data/habitats/aquatic/subglacial_lake.yaml; curation/decisions.tsv; curation/gold_parent_exclusions.tsv; tests/test_spring_lake_review_fixes.py; history/mappings/subglacial_lake | supports | Reassessed the entire corrected target, maintained inputs and immutable predecessor evidence. The deep-source ITEM rationale now states three API samples from one independent study Gs0112339, with unanimous local subglacial-lake annotation. Freshwater evidence remains seven samples from three separate named studies. Current classification, exact-path local annotation and ENVO definition support retaining the exact merged identity with explicitly limited one-study deep-source support. Only generated curation history changes: the superseded active deep-source decision event is replaced, not preserved as an additional active event; the old bytes remain in Git and the immutable predecessor, and a new append-only session history explains the correction. All other source claims and independent freshwater history are unchanged. The freshwater-material parent finding under #1220 remains open. SSSOM/KGX conformance is not established. The separate TSV formatting defect #2032 is corrected with explicit quoted empty category/relation cells, preserving all eleven columns. |
| CHECKS | tests/test_spring_lake_review_fixes.py; justfile; https://github.com/CultureBotAI/HabitatMech/actions/runs/38264229421 | supports | Nine local post-correction gates and exact corrected-head hosted authoritative QC succeeded. Local duplicate full QC is recorded separately, not assumed successful here. Three focused regressions preserve source-parent scope, path-specific sample/study counts and TSV empty-field semantics. Generated-map inputs match the exact local corpus; two changed semantic texts were encoded, repeat reuse verified, all 3208 points displayed. New successor bundles require separate integrity and protected CI checks. |
| CLARIFY | reviews/structured/20261012T145058Z-subglacial_lake-followup/review.yaml | supports | Re-read the entire unchanged target and corrected ITEM input. The remaining F1 finding concerns only liquid-freshwater ancestry; it no longer alleges that the active deep-source rationale overstates the independent study count. F2 remains resolved: three API samples from one study, distinct from the freshwater seven samples/three studies. The prior successor copied compound predecessor wording into F1 even while resolving F2. This new immutable observation corrects that review wording under #2033 without changing scientific inputs, statuses, findings counts or previous review bytes. Other scientific assessments, inspected authorities, original-occurrence limits and exact-head validation remain as in the predecessor. |

## Limits And Additional Notes

- Original occurrence membership remains unavailable as bounded in the predecessor.
- Only the named finding is resolved; shared mapping endpoints and other context hierarchy findings remain open.
- The initial canary invocation placed --force before the identifier and failed parsing without changing records; corrected invocations passed. The default CLAW history path was unavailable; the existing parent checkout supplied the scaffold. Optional standalone yamllint was not installed; native QC is the authoritative gate.
- Saved observations are immutable; source-scoped generated decision history is regenerated, while committed session history remains append-only.
- Immutable correction for https://github.com/CultureBotAI/HabitatMech/issues/2033. The superseded F1 wording was historical and misleading as a current-state statement; no saved review was rewritten.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T145330Z-subglacial_lake-clarification
kind: record
repository: CultureBotAI/HabitatMech
title: 'Clarified current finding scope: subglacial_lake'
started_at: '2026-10-12T14:53:27.800653Z'
finished_at: '2026-10-12T14:53:30.193217Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent authored and adversarially reassessed corrections;
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Re-read the entire unchanged target and corrected ITEM input. The remaining
  F1 finding concerns only liquid-freshwater ancestry; it no longer alleges that the
  active deep-source rationale overstates the independent study count. F2 remains
  resolved: three API samples from one study, distinct from the freshwater seven samples/three
  studies. The prior successor copied compound predecessor wording into F1 even while
  resolving F2. This new immutable observation corrects that review wording under
  #2033 without changing scientific inputs, statuses, findings counts or previous
  review bytes. Other scientific assessments, inspected authorities, original-occurrence
  limits and exact-head validation remain as in the predecessor.'
source:
  git_revision: 68259d4da83e48b00e9209c4079432f379aeaaf5
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 4544b5d2c11fbbb3a46cd8a65f7e664363df78c1000c590aab533219f9eec59b
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: d429c8bb74f521df9a77a90b216a44fc6959ee28efb1fa17a93582536caa8bce
    role: context
  - path: CLAUDE.md
    sha256: 98d95f910ff5160bc5b2ff572766785519dacdba487700bebaa6dbf96d071fd9
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
    sha256: 25be865290cf3bbaeecfa2b7582ec7ce3a08d94c0034cfb58edfc73f75cfe31c
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: c7017ce7889ebfce889eb6f2c6a6c12510428be4b8a4370e2e4e165231e1af25
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 331a7d9eb8a8909fc37402c0a776838979a8065644504d5c4f2a1c39bce5c24d
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/aquatic/deep_subsurface__45e0aabf.yaml
    sha256: 83df42364069e6c1fd73c5720c79f0ad14b2147273a9c7e3f3c499c23ad503ea
    role: context
  - path: data/habitats/aquatic/fresh_water.yaml
    sha256: 99bd93c6173c2ccf7b59645a131ae41c88c45246b45265034a8275053b3745b7
    role: context
  - path: data/habitats/aquatic/liquid_water.yaml
    sha256: b91ec338644558b9184fbbb52ace39758ffacaf10f76eb8c52bd854a389c9fd2
    role: context
  - path: data/habitats/aquatic/subglacial_lake.yaml
    sha256: 4026371720d3c7d165320fa357f317891b89bca445b262b49d9d47c82163422f
    role: target
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
    sha256: 36df8306394c06c352b73e0bf7b47a2858784cedac7389a24d0b78f593ece646
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
  - path: history/mappings/subglacial_lake/2026-10-12T142547Z-codex-gpt-5-bd4f4b.yaml
    sha256: 7fe02c0523e6d8c565afe465be18065ff2fab7b1d1845dbdec42db0c82259a40
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20261005T133717Z-sediment__4afb1aae.md
    sha256: 1ddba633fad8520504f665b86e9b4837abf6a09df6ada7727124d567a7a16557
    role: context
  - path: reports/yaml_record_review/20261006T111725Z-subglacial_lake.md
    sha256: cdcda24a092ee01d34862ca721cd0361669b33ad175a688f6e0a7024814b2c5a
    role: context
  - path: reviews/structured/20261012T142057Z-subglacial_lake/review.yaml
    sha256: f8a0d21cf9e25cd716b99997ae1530f1670e6b34b49d8130b490a76567c353d9
    role: context
  - path: reviews/structured/20261012T145058Z-subglacial_lake-followup/review.yaml
    sha256: 32636419f2930b5f368f9eb725805d34a4162a6bd889fe2dff106c4be1d8b999
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
    role: context
  - path: scripts/extract_source_inventory.py
    sha256: 4bf5391d25ff48a2d81eb3821af6582de063fd0391440973d309dfd93016490c
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/habitatmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/habitatmech/seed.py
    sha256: 4adf105e23d75c3563a516a0c160623d1065df7fcb2f31b7a0a0a8303d0401be
    role: context
  - path: tests/test_spring_lake_review_fixes.py
    sha256: 28ba530116989fd91777f19fbb44397a038f38adaa262bbeddd91e065cc809e2
    role: context
targets:
- target_id: ENVO:03000120
  path: data/habitats/aquatic/subglacial_lake.yaml
  label: subglacial lake
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Source identity and lifecycle
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Authored definitions and genus
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Source-context parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Frozen ontology
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Ontology hierarchy
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Exact frozen GOLD path
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Generated construction across all contributing source inventories
scope:
  description: Entire corrected target with explicitly bounded finding dispositions.
  selection: Successor review; no additional distinct-record coverage.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:03000120
checks:
- check_id: C0
  name: Post-correction native validation
  required: true
  status: passed
  target_ids:
  - ENVO:03000120
  command: just render
  exit_code: 0
  summary: Actual success 2026-10-12T14:31:42.324003+00:00 to 2026-10-12T14:32:07.734097+00:00.
    Full-corpus validation does not expand scientific review coverage.
  evidence_ids:
  - CHECKS
- check_id: C3
  name: Post-correction native validation
  required: true
  status: passed
  target_ids:
  - ENVO:03000120
  command: just validate data/habitats/aquatic/subglacial_lake.yaml
  exit_code: 0
  summary: Actual success 2026-10-12T14:32:11.201747+00:00 to 2026-10-12T14:32:12.956534+00:00.
    Full-corpus validation does not expand scientific review coverage.
  evidence_ids:
  - CHECKS
- check_id: C4
  name: Post-correction native validation
  required: true
  status: passed
  target_ids:
  - ENVO:03000120
  command: just validate-strict data/habitats/aquatic/spring__6fd75c62.yaml data/habitats/aquatic/spring__76db5e69.yaml
    data/habitats/aquatic/subglacial_lake.yaml
  exit_code: 0
  summary: Actual success 2026-10-12T14:32:12.957172+00:00 to 2026-10-12T14:32:16.310312+00:00.
    Full-corpus validation does not expand scientific review coverage.
  evidence_ids:
  - CHECKS
- check_id: C5
  name: Post-correction native validation
  required: true
  status: passed
  target_ids:
  - ENVO:03000120
  command: just validate-products
  exit_code: 0
  summary: Actual success 2026-10-12T14:32:16.310938+00:00 to 2026-10-12T14:32:53.190503+00:00.
    Full-corpus validation does not expand scientific review coverage.
  evidence_ids:
  - CHECKS
- check_id: C6
  name: Post-correction native validation
  required: true
  status: passed
  target_ids:
  - ENVO:03000120
  command: just validate-history
  exit_code: 0
  summary: Actual success 2026-10-12T14:32:53.191027+00:00 to 2026-10-12T14:32:59.563076+00:00.
    Full-corpus validation does not expand scientific review coverage.
  evidence_ids:
  - CHECKS
- check_id: C7
  name: Post-correction native validation
  required: true
  status: passed
  target_ids:
  - ENVO:03000120
  command: just provenance-check
  exit_code: 0
  summary: Actual success 2026-10-12T14:32:59.563616+00:00 to 2026-10-12T14:33:00.074493+00:00.
    Full-corpus validation does not expand scientific review coverage.
  evidence_ids:
  - CHECKS
- check_id: C8
  name: Post-correction native validation
  required: true
  status: passed
  target_ids:
  - ENVO:03000120
  command: just verify-corpus
  exit_code: 0
  summary: Actual success 2026-10-12T14:33:00.075047+00:00 to 2026-10-12T14:33:13.427177+00:00.
    Full-corpus validation does not expand scientific review coverage.
  evidence_ids:
  - CHECKS
- check_id: CI
  name: Exact corrected-head hosted QC
  required: true
  status: passed
  target_ids:
  - ENVO:03000120
  command: gh run view 38264229421 --log
  exit_code: 0
  summary: 'Exact corrected-head hosted authoritative QC passed: 1057 tests, three
    skipped, and all native quality gates. Newly saved successor bundles require separate
    integrity checks.'
  evidence_ids:
  - CHECKS
evidence:
- evidence_id: PRIOR
  kind: prior_review
  reference: reviews/structured/20261012T142057Z-subglacial_lake/review.yaml
  accessed_at: '2026-10-12T14:37:05.604530Z'
  support: supports
  summary: Exact immutable predecessor including inspected authority snapshots and
    source limitations.
- evidence_id: CURRENT
  kind: record_content
  reference: data/habitats/aquatic/subglacial_lake.yaml; curation/decisions.tsv; curation/gold_parent_exclusions.tsv;
    tests/test_spring_lake_review_fixes.py; history/mappings/subglacial_lake
  accessed_at: '2026-10-12T14:50:58.900575Z'
  support: supports
  summary: 'Reassessed the entire corrected target, maintained inputs and immutable
    predecessor evidence. The deep-source ITEM rationale now states three API samples
    from one independent study Gs0112339, with unanimous local subglacial-lake annotation.
    Freshwater evidence remains seven samples from three separate named studies. Current
    classification, exact-path local annotation and ENVO definition support retaining
    the exact merged identity with explicitly limited one-study deep-source support.
    Only generated curation history changes: the superseded active deep-source decision
    event is replaced, not preserved as an additional active event; the old bytes
    remain in Git and the immutable predecessor, and a new append-only session history
    explains the correction. All other source claims and independent freshwater history
    are unchanged. The freshwater-material parent finding under #1220 remains open.
    SSSOM/KGX conformance is not established. The separate TSV formatting defect #2032
    is corrected with explicit quoted empty category/relation cells, preserving all
    eleven columns.'
- evidence_id: CHECKS
  kind: record_content
  reference: tests/test_spring_lake_review_fixes.py; justfile; https://github.com/CultureBotAI/HabitatMech/actions/runs/38264229421
  accessed_at: '2026-10-12T14:50:58.900597Z'
  support: supports
  summary: Nine local post-correction gates and exact corrected-head hosted authoritative
    QC succeeded. Local duplicate full QC is recorded separately, not assumed successful
    here. Three focused regressions preserve source-parent scope, path-specific sample/study
    counts and TSV empty-field semantics. Generated-map inputs match the exact local
    corpus; two changed semantic texts were encoded, repeat reuse verified, all 3208
    points displayed. New successor bundles require separate integrity and protected
    CI checks.
- evidence_id: CLARIFY
  kind: prior_review
  reference: reviews/structured/20261012T145058Z-subglacial_lake-followup/review.yaml
  accessed_at: '2026-10-12T14:53:30.193217Z'
  support: supports
  summary: 'Re-read the entire unchanged target and corrected ITEM input. The remaining
    F1 finding concerns only liquid-freshwater ancestry; it no longer alleges that
    the active deep-source rationale overstates the independent study count. F2 remains
    resolved: three API samples from one study, distinct from the freshwater seven
    samples/three studies. The prior successor copied compound predecessor wording
    into F1 even while resolving F2. This new immutable observation corrects that
    review wording under #2033 without changing scientific inputs, statuses, findings
    counts or previous review bytes. Other scientific assessments, inspected authorities,
    original-occurrence limits and exact-head validation remain as in the predecessor.'
assessments:
- assessment_id: FIX
  area: grounding
  topic: Scoped correction and remaining scientific findings
  outcome: concern
  summary: 'Re-read the entire unchanged target and corrected ITEM input. The remaining
    F1 finding concerns only liquid-freshwater ancestry; it no longer alleges that
    the active deep-source rationale overstates the independent study count. F2 remains
    resolved: three API samples from one study, distinct from the freshwater seven
    samples/three studies. The prior successor copied compound predecessor wording
    into F1 even while resolving F2. This new immutable observation corrects that
    review wording under #2033 without changing scientific inputs, statuses, findings
    counts or previous review bytes. Other scientific assessments, inspected authorities,
    original-occurrence limits and exact-head validation remain as in the predecessor.
    F1 remains open; F2 remains resolved.'
  target_ids:
  - ENVO:03000120
  evidence_ids:
  - CURRENT
  - CHECKS
  - CLARIFY
findings:
- finding_id: F1
  issue_key: envo-03000120-gold-context-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: GOLD context does not justify a strict habitat superclass
  description: The merged subglacial-lake feature retains ENVO:00000198 ice-covered
    lake as a valid genus, but also inherits liquid fresh water ENVO:00002011 through
    the GOLD freshwater source context. That material is not a strict superclass of
    the lake feature. The separately corrected study-count rationale is not part of
    this remaining finding; undefined deep-subsurface parent scope is not endorsed
    or newly classified as false.
  target_ids:
  - ENVO:03000120
  field_paths:
  - parent_habitats
  evidence_ids:
  - CURRENT
  - CHECKS
  - CLARIFY
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained owner of the exact finding; never patch generated YAML
  rule_id: docs/CURATION.md; docs/record-review-profile.md
  native_severity: major
  normalization_reason: Material claim or representation mismatch.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1220
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261012T145058Z-subglacial_lake-followup
    finding_id: F1
- finding_id: F2
  issue_key: envo-03000120-study-denominator
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Deep-subsurface rationale overstates independent study support
  description: The original deep-source rationale overstated three samples from Gs0112339
    as three independent studies. The maintained decision and generated active history
    now state the correct path-specific denominator; the separate freshwater evidence
    is unchanged.
  target_ids:
  - ENVO:03000120
  field_paths:
  - curation_history
  evidence_ids:
  - CURRENT
  - CHECKS
  - CLARIFY
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained owner of the exact finding; never patch generated YAML
  rule_id: docs/CURATION.md; docs/record-review-profile.md
  native_severity: major
  normalization_reason: Material claim or representation mismatch.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1557
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261012T145058Z-subglacial_lake-followup
    finding_id: F2
  disposition_reason: 'Remains resolved after unchanged-byte and full-record reassessment.
    Re-read the entire unchanged target and corrected ITEM input. The remaining F1
    finding concerns only liquid-freshwater ancestry; it no longer alleges that the
    active deep-source rationale overstates the independent study count. F2 remains
    resolved: three API samples from one study, distinct from the freshwater seven
    samples/three studies. The prior successor copied compound predecessor wording
    into F1 even while resolving F2. This new immutable observation corrects that
    review wording under #2033 without changing scientific inputs, statuses, findings
    counts or previous review bytes. Other scientific assessments, inspected authorities,
    original-occurrence limits and exact-head validation remain as in the predecessor.'
actions:
- action_id: A1
  description: Assess and exclude only the unsupported exact-source contribution while
    retaining genuine genera and provenance; do not globally suppress a context class.
  finding_ids:
  - F1
  target_ids:
  - ENVO:03000120
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained owner of the exact finding; never patch generated YAML
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Reassess the exact source and preserve independent valid genera, source IDs, counts/units
    and omitted counts.
  - Change maintained owners with append-only curation history; do not rewrite generated
    records or saved reviews.
  - Add focused regressions; inspect guarded canaries and pass strict schema, labels,
    history, provenance, reproduction and QC.
  - Use a linked successor review for any disposition; this assessment records proposed
    work, not an executed repair.
limitations:
- Original occurrence membership remains unavailable as bounded in the predecessor.
- Only the named finding is resolved; shared mapping endpoints and other context hierarchy
  findings remain open.
- The initial canary invocation placed --force before the identifier and failed parsing
  without changing records; corrected invocations passed. The default CLAW history
  path was unavailable; the existing parent checkout supplied the scaffold. Optional
  standalone yamllint was not installed; native QC is the authoritative gate.
- Saved observations are immutable; source-scoped generated decision history is regenerated,
  while committed session history remains append-only.
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261012T145058Z-subglacial_lake-followup
  relationship: Clarifies current open-finding wording and preserves the resolved
    denominator disposition
tags:
- habitatmech
- record-review
- followup
notes:
- Immutable correction for https://github.com/CultureBotAI/HabitatMech/issues/2033.
  The superseded F1 wording was historical and misleading as a current-state statement;
  no saved review was rewritten.
```
