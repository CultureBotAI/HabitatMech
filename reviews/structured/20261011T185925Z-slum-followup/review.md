# Bounded hierarchy correction follow-up: slum

- Review: 20261011T185925Z-slum-followup
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-11T18:45:00.297902Z
- Finished UTC: 2026-10-11T18:59:25.864213Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Removed only the guarded immediate GOLD context contribution habitatmech:GOLD.d8d3393339. Independent parents, source identity, definition, taxa, counts/units or omissions and native mapping/grounding state are unchanged, with one appended exclusion event. The full-corpus differential regression limits direct changes to eleven records. This does not resolve separate identity, source-membership or endpoint findings.

## Scope And Provenance

Full exact target reassessed for the bounded hierarchy correction, retaining predecessor evidence and limitations.

Selection: Successor observation; no additional distinct-record coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base fd1b23f627d96e0c98f026359f059a08493aa641.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:01000653 | data/habitats/engineered/slum.yaml | generated | slum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Post-correction native gate | passed | True | ENVO:01000653 | Actual successful check; started 2026-10-11T18:38:26.093561+00:00; finished 2026-10-11T18:38:29.512560+00:00.  Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |
| Post-correction native gate | passed | True | ENVO:01000653 | Actual successful check; started 2026-10-11T18:39:02.361224+00:00; finished 2026-10-11T18:39:10.745030+00:00.  Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |
| Post-correction native gate | passed | True | ENVO:01000653 | Actual successful check; started 2026-10-11T18:39:10.747032+00:00; finished 2026-10-11T18:39:40.592528+00:00.  Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |
| Post-correction native gate | passed | True | ENVO:01000653 | Actual successful check; started 2026-10-11T18:39:40.593655+00:00; finished 2026-10-11T18:41:12.774014+00:00.  Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |
| Post-correction native gate | passed | True | ENVO:01000653 | Actual successful check; started 2026-10-11T18:41:12.774972+00:00; finished 2026-10-11T18:41:22.846703+00:00.  Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |
| Post-correction native gate | passed | True | ENVO:01000653 | Actual successful check; started 2026-10-11T18:41:22.847564+00:00; finished 2026-10-11T18:41:29.087829+00:00.  Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |
| Post-correction native gate | passed | True | ENVO:01000653 | Actual successful check; started 2026-10-11T18:41:29.088724+00:00; finished 2026-10-11T18:41:50.726130+00:00.  Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |
| Post-correction native gate | passed | True | ENVO:01000653 | Actual successful check; started 2026-10-11T18:41:50.726789+00:00; finished 2026-10-11T18:41:58.074774+00:00.  Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |
| Post-correction native gate | passed | True | ENVO:01000653 | Actual successful check; started 2026-10-11T18:41:58.075487+00:00; finished 2026-10-11T18:41:58.743974+00:00.  Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |
| Post-correction native gate | passed | True | ENVO:01000653 | Actual successful check; started 2026-10-11T18:45:10.100689+00:00; finished 2026-10-11T18:59:16.288744+00:00. Authoritative full QC on exact head fd1b23f627d96e0c98f026359f059a08493aa641 passed776 tests with3 skipped; all required workflows succeeded. https://github.com/CultureBotAI/HabitatMech/actions/runs/38165120441 Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |

## Scientific And Domain Assessments

### Exact correction and unchanged scientific claims

scope: concern. Targets: ENVO:01000653.

Removed only the guarded immediate GOLD context contribution habitatmech:GOLD.d8d3393339. Independent parents, source identity, definition, taxa, counts/units or omissions and native mapping/grounding state are unchanged, with one appended exclusion event. The full-corpus differential regression limits direct changes to eleven records. This does not resolve separate identity, source-membership or endpoint findings.

## Findings

### F1: Context relation is emitted as a strict superclass

major / resolved / confirmed; issue key: envo-01000653-context-parent.

The record denotes the ENVO slum settlement class, not urban wastewater. Its GOLD slash label Slums/Informal settlements is asserted to be exactly equivalent without evidence that informal settlements satisfy the narrower slum definition. Current exact BioSamples describe wastewater from informal settlements: this supports a sampling context, not settlement-to-water subsumption or universal slum identity. Exact false contribution: habitatmech:GOLD.d8d3393339.

Disposition: Removed only the guarded immediate GOLD context contribution habitatmech:GOLD.d8d3393339. Independent parents, source identity, definition, taxa, counts/units or omissions and native mapping/grounding state are unchanged, with one appended exclusion event. The full-corpus differential regression limits direct changes to eleven records. This does not resolve separate identity, source-membership or endpoint findings.

### F2: Slums and informal settlements are asserted to be one exact class

major / open / confirmed; issue key: envo-01000653-slash-label-identity.

The ITEM decision treats a slash alternative as one thing, but official ENVO informal settlement and slum definitions differ. Current exact samples specify wastewater from informal settlements, not the dense-settlement/deprivation constraints of slum. This leaves exact identity and EXACT synonym scope unsupported, independently of the false water parent.

## Recommended Actions And Acceptance Checks

### A2

Recover the original source interpretation and distinguish settlement context from sampled wastewater before retaining exact slum identity. If scope cannot be established, retain the source mint and related ontology references instead of inventing an exact class match.

- Use exact source keys and inspected evidence; preserve path identity, source counts/units and independently valid parents.
- For curation, append native history, add focused regressions, dry seed, inspect a canary, regenerate governed products and pass strict/schema/labels/reproduction/full QC.
- Save a linked successor for any resolved finding; do not rewrite this immutable observation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| PRIOR | reviews/structured/20261011T182912Z-slum/review.yaml | supports | Predecessor full assessment, inspected primary sources and remaining limitations retained; this successor resolves only the named hierarchy finding. |
| CURRENT | data/habitats/engineered/slum.yaml; curation/gold_parent_exclusions.tsv; tests/test_late_engineered_review_fixes.py | supports | Removed only the guarded immediate GOLD context contribution habitatmech:GOLD.d8d3393339. Independent parents, source identity, definition, taxa, counts/units or omissions and native mapping/grounding state are unchanged, with one appended exclusion event. The full-corpus differential regression limits direct changes to eleven records. This does not resolve separate identity, source-membership or endpoint findings. |

## Limits And Additional Notes

- Original assertion-level source membership remains unreconstructed. Current GOLD examples do not replace frozen counts.
- Same-agent curation and adversarial assessment, not independent approval.
- Shared #1398 and separate source/identity/taxonomy issues remain unresolved. No SSSOM/KGX readiness certification.
- Full QC covers the captured scientific-input commit. These newly saved successor files require separate final integrity/PR checks.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T185925Z-slum-followup
kind: record
repository: culturebotai/HabitatMech
title: 'Bounded hierarchy correction follow-up: slum'
started_at: '2026-10-11T18:45:00.297902Z'
finished_at: '2026-10-11T18:59:25.864213Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Continuing agent participated in earlier curation and review;
    same-agent assessment, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Removed only the guarded immediate GOLD context contribution habitatmech:GOLD.d8d3393339.
  Independent parents, source identity, definition, taxa, counts/units or omissions
  and native mapping/grounding state are unchanged, with one appended exclusion event.
  The full-corpus differential regression limits direct changes to eleven records.
  This does not resolve separate identity, source-membership or endpoint findings.
source:
  git_revision: fd1b23f627d96e0c98f026359f059a08493aa641
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
  - path: curation/causal_graphs/waste_water.yaml
    sha256: 299b5128af6cf5f7a61ce53304f1084e6eb045414b47cbcfd8832de095142aef
    role: context
  - path: curation/decisions.tsv
    sha256: 7cbec6d310b1aac248defdbe657e68c0cc1e848981230d2279e63f474c6f4c96
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 1c75d78798266f625984ddfbc493c0ea9eaacb654925f8d29c8aa337365b1f59
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 3f2ce04805defe5ff65dc20988cc72bc94d4636b3140eb1311017866bdc0ea0a
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/engineered/engineered__900b76ad.yaml
    sha256: 85154c9542e8e033e17cf631b06a462612229f3bcfdc1cdca0fc6cf73b9b9364
    role: context
  - path: data/habitats/engineered/slum.yaml
    sha256: 14058913e4a7f3c98f85b9f892b244543e36d082f0ac0489c4befc4908dce131
    role: target
  - path: data/habitats/engineered/urban_wastewater.yaml
    sha256: e307a41a9453837e4cab7a31f33ea22928920dad0625f3a9198119c8038e6159
    role: context
  - path: data/habitats/engineered/waste_water.yaml
    sha256: 774c88de3169fb8ae95ea05deb748f21e036a35d0b21734c81c228493ec96056
    role: context
  - path: data/habitats/other/environmental_material.yaml
    sha256: f3916c9c17060dbb92c026d8e340be9478c37409361279bbb639642cdae29fe7
    role: context
  - path: data/habitats/other/waste_material.yaml
    sha256: fe8e42f2fe582f7984c8a12d7015ba28a3c417267590b545980d27811a13b757
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
    sha256: 36df8306394c06c352b73e0bf7b47a2858784cedac7389a24d0b78f593ece646
    role: context
  - path: docs/HARMONIZATION.md
    sha256: ee39d3cd29115ee14f5e7386169c76c47d471ebdc2502c008c49d30fb44918f1
    role: context
  - path: docs/RESEARCH.md
    sha256: 82c5471890d310bf8fd33141d5596f847bfc1eb6091c2db6f485388435e067af
    role: context
  - path: docs/record-review-profile.md
    sha256: f7aa39ee762d94f1902d9f08f328cb897bc543e4e226057eb4770d24bfcc6eb5
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/mappings/slum/2026-10-11T183702Z-codex-gpt-5-61ac9d.yaml
    sha256: a9170dc21c0bbac4a212c900f4804d8a74ddf4fc5fb3f70d4ff2f201f41c074c
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reviews/structured/20261011T182912Z-slum/review.yaml
    sha256: 3c0782174c6e86ac808776d77ce4ad1325d033c7d180d6692ec33e2116b2a573
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
  - path: tests/test_late_engineered_review_fixes.py
    sha256: 7a89ce8e09992969c9a75cc01e3198dff2b04f360eab16dd83a277aa4fcc472e
    role: context
targets:
- target_id: ENVO:01000653
  path: data/habitats/engineered/slum.yaml
  label: slum
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Per-source grounding and native review-depth decisions
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact GOLD context-parent contribution decisions
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Curated definition, genus and lexical scope
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Pinned ontology identity, labels, synonyms and definitions
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Pinned ontology hierarchy
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Source harmonization and generated output
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen exact source paths, nodes and ORGANISM counts
scope:
  description: Full exact target reassessed for the bounded hierarchy correction,
    retaining predecessor evidence and limitations.
  selection: Successor observation; no additional distinct-record coverage.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:01000653
checks:
- check_id: C0
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:01000653
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate
    data/habitats/engineered/slum.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T18:38:26.093561+00:00; finished
    2026-10-11T18:38:29.512560+00:00.  Only applicable per-record checks are attached;
    full-corpus validation does not expand scientific coverage.
- check_id: C1
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:01000653
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-strict
    data/habitats/engineered/slum.yaml data/habitats/engineered/soil__5796ed83.yaml
    data/habitats/engineered/soil__5aefc937.yaml data/habitats/engineered/soil__cbcc9126.yaml
    data/habitats/engineered/spacecraft.yaml data/habitats/engineered/stadium.yaml
    data/habitats/engineered/stone.yaml data/habitats/engineered/stone_surface.yaml
    data/habitats/engineered/surface_biofilm.yaml data/habitats/engineered/swine_waste_with_corn.yaml
    data/habitats/engineered/tailings_pond__a57fabd2.yaml data/habitats/engineered/space_station.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T18:39:02.361224+00:00; finished
    2026-10-11T18:39:10.745030+00:00.  Only applicable per-record checks are attached;
    full-corpus validation does not expand scientific coverage.
- check_id: C2
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:01000653
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T18:39:10.747032+00:00; finished
    2026-10-11T18:39:40.592528+00:00.  Only applicable per-record checks are attached;
    full-corpus validation does not expand scientific coverage.
- check_id: C3
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:01000653
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T18:39:40.593655+00:00; finished
    2026-10-11T18:41:12.774014+00:00.  Only applicable per-record checks are attached;
    full-corpus validation does not expand scientific coverage.
- check_id: C4
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:01000653
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T18:41:12.774972+00:00; finished
    2026-10-11T18:41:22.846703+00:00.  Only applicable per-record checks are attached;
    full-corpus validation does not expand scientific coverage.
- check_id: C5
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:01000653
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T18:41:22.847564+00:00; finished
    2026-10-11T18:41:29.087829+00:00.  Only applicable per-record checks are attached;
    full-corpus validation does not expand scientific coverage.
- check_id: C6
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:01000653
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T18:41:29.088724+00:00; finished
    2026-10-11T18:41:50.726130+00:00.  Only applicable per-record checks are attached;
    full-corpus validation does not expand scientific coverage.
- check_id: C7
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:01000653
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache .venv/bin/python
    -m pytest tests/test_late_engineered_review_fixes.py -q
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T18:41:50.726789+00:00; finished
    2026-10-11T18:41:58.074774+00:00.  Only applicable per-record checks are attached;
    full-corpus validation does not expand scientific coverage.
- check_id: C8
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:01000653
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just provenance-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T18:41:58.075487+00:00; finished
    2026-10-11T18:41:58.743974+00:00.  Only applicable per-record checks are attached;
    full-corpus validation does not expand scientific coverage.
- check_id: C9
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:01000653
  command: gh pr checks codex/record-reviews-20261011o --watch --interval 30
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T18:45:10.100689+00:00; finished
    2026-10-11T18:59:16.288744+00:00. Authoritative full QC on exact head fd1b23f627d96e0c98f026359f059a08493aa641
    passed776 tests with3 skipped; all required workflows succeeded. https://github.com/CultureBotAI/HabitatMech/actions/runs/38165120441
    Only applicable per-record checks are attached; full-corpus validation does not
    expand scientific coverage.
evidence:
- evidence_id: PRIOR
  kind: prior_review
  reference: reviews/structured/20261011T182912Z-slum/review.yaml
  accessed_at: '2026-10-11T18:45:00.297902Z'
  support: supports
  summary: Predecessor full assessment, inspected primary sources and remaining limitations
    retained; this successor resolves only the named hierarchy finding.
- evidence_id: CURRENT
  kind: record_content
  reference: data/habitats/engineered/slum.yaml; curation/gold_parent_exclusions.tsv;
    tests/test_late_engineered_review_fixes.py
  accessed_at: '2026-10-11T18:59:25.864213Z'
  support: supports
  summary: Removed only the guarded immediate GOLD context contribution habitatmech:GOLD.d8d3393339.
    Independent parents, source identity, definition, taxa, counts/units or omissions
    and native mapping/grounding state are unchanged, with one appended exclusion
    event. The full-corpus differential regression limits direct changes to eleven
    records. This does not resolve separate identity, source-membership or endpoint
    findings.
assessments:
- assessment_id: CORRECTION
  area: scope
  topic: Exact correction and unchanged scientific claims
  outcome: concern
  target_ids:
  - ENVO:01000653
  evidence_ids:
  - PRIOR
  - CURRENT
  summary: Removed only the guarded immediate GOLD context contribution habitatmech:GOLD.d8d3393339.
    Independent parents, source identity, definition, taxa, counts/units or omissions
    and native mapping/grounding state are unchanged, with one appended exclusion
    event. The full-corpus differential regression limits direct changes to eleven
    records. This does not resolve separate identity, source-membership or endpoint
    findings.
findings:
- finding_id: F1
  issue_key: envo-01000653-context-parent
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: Context relation is emitted as a strict superclass
  description: 'The record denotes the ENVO slum settlement class, not urban wastewater.
    Its GOLD slash label Slums/Informal settlements is asserted to be exactly equivalent
    without evidence that informal settlements satisfy the narrower slum definition.
    Current exact BioSamples describe wastewater from informal settlements: this supports
    a sampling context, not settlement-to-water subsumption or universal slum identity.
    Exact false contribution: habitatmech:GOLD.d8d3393339.'
  target_ids:
  - ENVO:01000653
  field_paths:
  - parent_habitats
  evidence_ids:
  - PRIOR
  - CURRENT
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded exact source-path contribution
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Independent-parent preservation
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: False or unsupported identity, strict hierarchy or declared
    mapping endpoint.
  previous_occurrences:
  - repository: culturebotai/HabitatMech
    review_id: 20261011T182912Z-slum
    finding_id: F1
  disposition_reason: Removed only the guarded immediate GOLD context contribution
    habitatmech:GOLD.d8d3393339. Independent parents, source identity, definition,
    taxa, counts/units or omissions and native mapping/grounding state are unchanged,
    with one appended exclusion event. The full-corpus differential regression limits
    direct changes to eleven records. This does not resolve separate identity, source-membership
    or endpoint findings.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1955
- finding_id: F2
  issue_key: envo-01000653-slash-label-identity
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Slums and informal settlements are asserted to be one exact class
  description: The ITEM decision treats a slash alternative as one thing, but official
    ENVO informal settlement and slum definitions differ. Current exact samples specify
    wastewater from informal settlements, not the dense-settlement/deprivation constraints
    of slum. This leaves exact identity and EXACT synonym scope unsupported, independently
    of the false water parent.
  target_ids:
  - ENVO:01000653
  field_paths:
  - identifier
  - grounding_status
  - synonyms
  - source_attestations
  evidence_ids:
  - PRIOR
  - CURRENT
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: ITEM decision GOLD.765d4bdada
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: False or unsupported identity, strict hierarchy or declared
    mapping endpoint.
  previous_occurrences:
  - repository: culturebotai/HabitatMech
    review_id: 20261011T182912Z-slum
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1956
actions:
- action_id: A2
  description: Recover the original source interpretation and distinguish settlement
    context from sampled wastewater before retaining exact slum identity. If scope
    cannot be established, retain the source mint and related ontology references
    instead of inventing an exact class match.
  finding_ids:
  - F2
  target_ids:
  - ENVO:01000653
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: ITEM decision GOLD.765d4bdada
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Use exact source keys and inspected evidence; preserve path identity, source counts/units
    and independently valid parents.
  - For curation, append native history, add focused regressions, dry seed, inspect
    a canary, regenerate governed products and pass strict/schema/labels/reproduction/full
    QC.
  - Save a linked successor for any resolved finding; do not rewrite this immutable
    observation.
limitations:
- Original assertion-level source membership remains unreconstructed. Current GOLD
  examples do not replace frozen counts.
- Same-agent curation and adversarial assessment, not independent approval.
- 'Shared #1398 and separate source/identity/taxonomy issues remain unresolved. No
  SSSOM/KGX readiness certification.'
- Full QC covers the captured scientific-input commit. These newly saved successor
  files require separate final integrity/PR checks.
related_reviews:
- repository: culturebotai/HabitatMech
  review_id: 20261011T182912Z-slum
  relationship: Resolves only the named hierarchy finding and carries all other findings
    forward
tags:
- habitatmech
- record-review
- followup
```
