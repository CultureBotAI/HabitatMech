# Bounded hierarchy correction follow-up: soil__5aefc937

- Review: 20261011T185952Z-soil__5aefc937-followup
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-11T18:45:05.373761Z
- Finished UTC: 2026-10-11T18:59:52.554956Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Removed only the guarded immediate GOLD context contribution habitatmech:GOLD.86cf49cefb. Independent parents, source identity, definition, taxa, counts/units or omissions and native mapping/grounding state are unchanged, with one appended exclusion event. The full-corpus differential regression limits direct changes to eleven records. This does not resolve separate identity, source-membership or endpoint findings.

## Scope And Provenance

Full exact target reassessed for the bounded hierarchy correction, retaining predecessor evidence and limitations.

Selection: Successor observation; no additional distinct-record coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base fd1b23f627d96e0c98f026359f059a08493aa641.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.e9844fc187 | data/habitats/engineered/soil__5aefc937.yaml | generated | Soil |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Post-correction native gate | passed | True | habitatmech:GOLD.e9844fc187 | Actual successful check; started 2026-10-11T18:38:32.991399+00:00; finished 2026-10-11T18:38:36.403171+00:00.  Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |
| Post-correction native gate | passed | True | habitatmech:GOLD.e9844fc187 | Actual successful check; started 2026-10-11T18:39:02.361224+00:00; finished 2026-10-11T18:39:10.745030+00:00.  Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |
| Post-correction native gate | passed | True | habitatmech:GOLD.e9844fc187 | Actual successful check; started 2026-10-11T18:39:10.747032+00:00; finished 2026-10-11T18:39:40.592528+00:00.  Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |
| Post-correction native gate | passed | True | habitatmech:GOLD.e9844fc187 | Actual successful check; started 2026-10-11T18:39:40.593655+00:00; finished 2026-10-11T18:41:12.774014+00:00.  Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |
| Post-correction native gate | passed | True | habitatmech:GOLD.e9844fc187 | Actual successful check; started 2026-10-11T18:41:12.774972+00:00; finished 2026-10-11T18:41:22.846703+00:00.  Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |
| Post-correction native gate | passed | True | habitatmech:GOLD.e9844fc187 | Actual successful check; started 2026-10-11T18:41:22.847564+00:00; finished 2026-10-11T18:41:29.087829+00:00.  Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |
| Post-correction native gate | passed | True | habitatmech:GOLD.e9844fc187 | Actual successful check; started 2026-10-11T18:41:29.088724+00:00; finished 2026-10-11T18:41:50.726130+00:00.  Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |
| Post-correction native gate | passed | True | habitatmech:GOLD.e9844fc187 | Actual successful check; started 2026-10-11T18:41:50.726789+00:00; finished 2026-10-11T18:41:58.074774+00:00.  Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |
| Post-correction native gate | passed | True | habitatmech:GOLD.e9844fc187 | Actual successful check; started 2026-10-11T18:41:58.075487+00:00; finished 2026-10-11T18:41:58.743974+00:00.  Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |
| Post-correction native gate | passed | True | habitatmech:GOLD.e9844fc187 | Actual successful check; started 2026-10-11T18:45:10.100689+00:00; finished 2026-10-11T18:59:16.288744+00:00. Authoritative full QC on exact head fd1b23f627d96e0c98f026359f059a08493aa641 passed776 tests with3 skipped; all required workflows succeeded. https://github.com/CultureBotAI/HabitatMech/actions/runs/38165120441 Only applicable per-record checks are attached; full-corpus validation does not expand scientific coverage. |

## Scientific And Domain Assessments

### Exact correction and unchanged scientific claims

scope: concern. Targets: habitatmech:GOLD.e9844fc187.

Removed only the guarded immediate GOLD context contribution habitatmech:GOLD.86cf49cefb. Independent parents, source identity, definition, taxa, counts/units or omissions and native mapping/grounding state are unchanged, with one appended exclusion event. The full-corpus differential regression limits direct changes to eleven records. This does not resolve separate identity, source-membership or endpoint findings.

## Findings

### F1: Context relation is emitted as a strict superclass

major / resolved / confirmed; issue key: habitatmech-gold.e9844fc187-context-parent.

Plant-growth-chamber soil is material, not a chamber. Later exact samples distinguish the soil containing microorganisms and root material from the growth chamber. Retain ENVO:00001998 and the qualified mint; the chamber context is not a strictly broader material. Exact false contribution: habitatmech:GOLD.86cf49cefb.

Disposition: Removed only the guarded immediate GOLD context contribution habitatmech:GOLD.86cf49cefb. Independent parents, source identity, definition, taxa, counts/units or omissions and native mapping/grounding state are unchanged, with one appended exclusion event. The full-corpus differential regression limits direct changes to eleven records. This does not resolve separate identity, source-membership or endpoint findings.

### F2: Retained-source mapping uses an implicit ontology-parent endpoint

major / open / confirmed; issue key: habitatmech-gold.e9844fc187-mapping-endpoint-contract.

Actual route gold_narrower_than_leaf_match keeps the source mint but emits skos:narrowMatch against implicit ontology parents ENVO:00001998. The declared attestation endpoint is source -&gt; this record identifier, with omission when source identity is retained. A global broad/narrow swap would not fix the implicit target.

## Recommended Actions And Acceptance Checks

### A2

Resolve shared#1398 with explicit endpoints and consumer regressions; audit actual SSSOM/KGX output against current kg-microbe modeling before claiming compatibility.

- Use exact source keys and inspected evidence; preserve path identity, source counts/units and independently valid parents.
- For curation, append native history, add focused regressions, dry seed, inspect a canary, regenerate governed products and pass strict/schema/labels/reproduction/full QC.
- Save a linked successor for any resolved finding; do not rewrite this immutable observation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| PRIOR | reviews/structured/20261011T182920Z-soil__5aefc937/review.yaml | supports | Predecessor full assessment, inspected primary sources and remaining limitations retained; this successor resolves only the named hierarchy finding. |
| CURRENT | data/habitats/engineered/soil__5aefc937.yaml; curation/gold_parent_exclusions.tsv; tests/test_late_engineered_review_fixes.py | supports | Removed only the guarded immediate GOLD context contribution habitatmech:GOLD.86cf49cefb. Independent parents, source identity, definition, taxa, counts/units or omissions and native mapping/grounding state are unchanged, with one appended exclusion event. The full-corpus differential regression limits direct changes to eleven records. This does not resolve separate identity, source-membership or endpoint findings. |

## Limits And Additional Notes

- Original assertion-level source membership remains unreconstructed. Current GOLD examples do not replace frozen counts.
- Same-agent curation and adversarial assessment, not independent approval.
- Shared #1398 and separate source/identity/taxonomy issues remain unresolved. No SSSOM/KGX readiness certification.
- Full QC covers the captured scientific-input commit. These newly saved successor files require separate final integrity/PR checks.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T185952Z-soil__5aefc937-followup
kind: record
repository: culturebotai/HabitatMech
title: 'Bounded hierarchy correction follow-up: soil__5aefc937'
started_at: '2026-10-11T18:45:05.373761Z'
finished_at: '2026-10-11T18:59:52.554956Z'
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
summary: Removed only the guarded immediate GOLD context contribution habitatmech:GOLD.86cf49cefb.
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
  - path: curation/causal_graphs/soil.yaml
    sha256: 2a2bf4b1099b3bc69015f9530cf6e926c05c33667132234b3c52f06aacc957c2
    role: context
  - path: curation/causal_graphs/terrestrial_biome.yaml
    sha256: 239e6a2b711564ed12084cddd1295547d23858dd329c33c538251d5f53c88834
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
  - path: data/habitats/engineered/artificial_ecosystem.yaml
    sha256: 721350810f5b9c5c33a03ce8133bdfee22605458fef414c87390469695964317
    role: context
  - path: data/habitats/engineered/engineered__900b76ad.yaml
    sha256: 85154c9542e8e033e17cf631b06a462612229f3bcfdc1cdca0fc6cf73b9b9364
    role: context
  - path: data/habitats/engineered/plant_growth_chamber.yaml
    sha256: 67a2131813226eb273ee02465d5a098fecff0a22c9159df039fd62a8b8fc25b8
    role: context
  - path: data/habitats/engineered/soil__5aefc937.yaml
    sha256: 015ed5c8b1fcdbf31fd9b3fde782cc41ac3537a67523f27ff60ee7cf56b44960
    role: target
  - path: data/habitats/other/biome.yaml
    sha256: 43080ce9bd411ee97a20d97c17bd923405c040feaf9454d44ca22a2955ce1854
    role: context
  - path: data/habitats/other/environmental.yaml
    sha256: b23a64a2d7594f05716dfc8f525d184fe8bb5d885dbb9e755ba8cc844f433659
    role: context
  - path: data/habitats/other/environmental_material.yaml
    sha256: f3916c9c17060dbb92c026d8e340be9478c37409361279bbb639642cdae29fe7
    role: context
  - path: data/habitats/other/environmental_system.yaml
    sha256: 2c227791ce7b92c16ae9b76ad8295be95efee73cb65ec7050d1de2b00c8eecbc
    role: context
  - path: data/habitats/terrestrial/soil.yaml
    sha256: 7ee242511319844cf9b135a00bd84deba8269179dded67528b573f6071939e86
    role: context
  - path: data/habitats/terrestrial/terrestrial_biome.yaml
    sha256: ae30e45d8631d6a1f7012d92094b816458e440719f7173e4ecf3bd51f8e6c1f4
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
  - path: history/mappings/soil__5aefc937/2026-10-11T183705Z-codex-gpt-5-e6356a.yaml
    sha256: db2cd4f9dffbd9739c6ee827b836a96962a1523dee28f73ad9f30a78c4700cfc
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260925T070724Z-soil__5aefc937.md
    sha256: 52f24b1bc42f436690437638191cf16b7bbe111b86869b941963b0b11691c8a8
    role: context
  - path: reviews/structured/20261011T182920Z-soil__5aefc937/review.yaml
    sha256: 958008c35f4fca397e023662e226a82a7d775e07b9c48ca39ed1e5de2f838b25
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
- target_id: habitatmech:GOLD.e9844fc187
  path: data/habitats/engineered/soil__5aefc937.yaml
  label: Soil
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
  - habitatmech:GOLD.e9844fc187
checks:
- check_id: C0
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.e9844fc187
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate
    data/habitats/engineered/soil__5aefc937.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T18:38:32.991399+00:00; finished
    2026-10-11T18:38:36.403171+00:00.  Only applicable per-record checks are attached;
    full-corpus validation does not expand scientific coverage.
- check_id: C1
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.e9844fc187
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
  - habitatmech:GOLD.e9844fc187
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
  - habitatmech:GOLD.e9844fc187
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
  - habitatmech:GOLD.e9844fc187
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
  - habitatmech:GOLD.e9844fc187
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
  - habitatmech:GOLD.e9844fc187
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
  - habitatmech:GOLD.e9844fc187
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
  - habitatmech:GOLD.e9844fc187
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
  - habitatmech:GOLD.e9844fc187
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
  reference: reviews/structured/20261011T182920Z-soil__5aefc937/review.yaml
  accessed_at: '2026-10-11T18:45:05.373761Z'
  support: supports
  summary: Predecessor full assessment, inspected primary sources and remaining limitations
    retained; this successor resolves only the named hierarchy finding.
- evidence_id: CURRENT
  kind: record_content
  reference: data/habitats/engineered/soil__5aefc937.yaml; curation/gold_parent_exclusions.tsv;
    tests/test_late_engineered_review_fixes.py
  accessed_at: '2026-10-11T18:59:52.554956Z'
  support: supports
  summary: Removed only the guarded immediate GOLD context contribution habitatmech:GOLD.86cf49cefb.
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
  - habitatmech:GOLD.e9844fc187
  evidence_ids:
  - PRIOR
  - CURRENT
  summary: Removed only the guarded immediate GOLD context contribution habitatmech:GOLD.86cf49cefb.
    Independent parents, source identity, definition, taxa, counts/units or omissions
    and native mapping/grounding state are unchanged, with one appended exclusion
    event. The full-corpus differential regression limits direct changes to eleven
    records. This does not resolve separate identity, source-membership or endpoint
    findings.
findings:
- finding_id: F1
  issue_key: habitatmech-gold.e9844fc187-context-parent
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: Context relation is emitted as a strict superclass
  description: 'Plant-growth-chamber soil is material, not a chamber. Later exact
    samples distinguish the soil containing microorganisms and root material from
    the growth chamber. Retain ENVO:00001998 and the qualified mint; the chamber context
    is not a strictly broader material. Exact false contribution: habitatmech:GOLD.86cf49cefb.'
  target_ids:
  - habitatmech:GOLD.e9844fc187
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
    review_id: 20261011T182920Z-soil__5aefc937
    finding_id: F1
  disposition_reason: Removed only the guarded immediate GOLD context contribution
    habitatmech:GOLD.86cf49cefb. Independent parents, source identity, definition,
    taxa, counts/units or omissions and native mapping/grounding state are unchanged,
    with one appended exclusion event. The full-corpus differential regression limits
    direct changes to eleven records. This does not resolve separate identity, source-membership
    or endpoint findings.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1955
- finding_id: F2
  issue_key: habitatmech-gold.e9844fc187-mapping-endpoint-contract
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Retained-source mapping uses an implicit ontology-parent endpoint
  description: Actual route gold_narrower_than_leaf_match keeps the source mint but
    emits skos:narrowMatch against implicit ontology parents ENVO:00001998. The declared
    attestation endpoint is source -> this record identifier, with omission when source
    identity is retained. A global broad/narrow swap would not fix the implicit target.
  target_ids:
  - habitatmech:GOLD.e9844fc187
  field_paths:
  - source_attestations[0].mapping_predicate
  - grounding_status
  evidence_ids:
  - PRIOR
  - CURRENT
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Declared source/record endpoint
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Resolution and attestation emission
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: False or unsupported identity, strict hierarchy or declared
    mapping endpoint.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
  previous_occurrences:
  - repository: culturebotai/HabitatMech
    review_id: 20261011T182920Z-soil__5aefc937
    finding_id: F2
actions:
- action_id: A2
  description: Resolve shared#1398 with explicit endpoints and consumer regressions;
    audit actual SSSOM/KGX output against current kg-microbe modeling before claiming
    compatibility.
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.e9844fc187
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Declared source/record endpoint
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Resolution and attestation emission
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
  review_id: 20261011T182920Z-soil__5aefc937
  relationship: Resolves only the named hierarchy finding and carries all other findings
    forward
tags:
- habitatmech
- record-review
- followup
```
