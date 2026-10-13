# Bounded hierarchy correction follow-up: water

- Review: 20261011T202606Z-water-followup
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-11T20:13:00.466493Z
- Finished UTC: 2026-10-11T20:26:06.942143Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Removed only the guarded immediate GOLD context contribution ENVO:00000014. Independent parents, source identity, definition, counts/units or omissions and native grounding/mapping status are unchanged, with one appended exclusion event. The full-corpus differential regression limits direct changes to exactly four records. This does not resolve separate mapping-endpoint or source-membership findings. ENVO canal denotes the contained water body, not the channel; the corrected child is liquid-water material. ENVO:00002006 and all four ORGANISM assertions remain. Shared1398 remains open.

## Scope And Provenance

Full exact target reassessed for the bounded hierarchy correction, retaining predecessor evidence and limitations.

Selection: Successor observation; no additional distinct-record coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 75dde02c5396a39cb7e9e99b66dafbd653a4510c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.0533686915 | data/habitats/engineered/water.yaml | generated | Water |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Post-correction native gate | passed | True | habitatmech:GOLD.0533686915 | Actual successful check; started 2026-10-11T20:06:43.243130+00:00; finished 2026-10-11T20:06:46.457188+00:00.  Full-corpus checks do not expand scientific review coverage. |
| Post-correction native gate | passed | True | habitatmech:GOLD.0533686915 | Actual successful check; started 2026-10-11T20:06:56.016326+00:00; finished 2026-10-11T20:07:02.050786+00:00.  Full-corpus checks do not expand scientific review coverage. |
| Post-correction native gate | passed | True | habitatmech:GOLD.0533686915 | Actual successful check; started 2026-10-11T20:07:02.051536+00:00; finished 2026-10-11T20:07:25.696214+00:00.  Full-corpus checks do not expand scientific review coverage. |
| Post-correction native gate | passed | True | habitatmech:GOLD.0533686915 | Actual successful check; started 2026-10-11T20:07:25.697183+00:00; finished 2026-10-11T20:08:43.205293+00:00.  Full-corpus checks do not expand scientific review coverage. |
| Post-correction native gate | passed | True | habitatmech:GOLD.0533686915 | Actual successful check; started 2026-10-11T20:08:43.206127+00:00; finished 2026-10-11T20:08:53.846625+00:00.  Full-corpus checks do not expand scientific review coverage. |
| Post-correction native gate | passed | True | habitatmech:GOLD.0533686915 | Actual successful check; started 2026-10-11T20:08:53.847437+00:00; finished 2026-10-11T20:09:00.953182+00:00.  Full-corpus checks do not expand scientific review coverage. |
| Post-correction native gate | passed | True | habitatmech:GOLD.0533686915 | Actual successful check; started 2026-10-11T20:09:00.953890+00:00; finished 2026-10-11T20:09:26.060420+00:00.  Full-corpus checks do not expand scientific review coverage. |
| Post-correction native gate | passed | True | habitatmech:GOLD.0533686915 | Actual successful check; started 2026-10-11T20:09:26.061081+00:00; finished 2026-10-11T20:09:34.124559+00:00.  Full-corpus checks do not expand scientific review coverage. |
| Post-correction native gate | passed | True | habitatmech:GOLD.0533686915 | Actual successful check; started 2026-10-11T20:09:34.125407+00:00; finished 2026-10-11T20:09:34.924845+00:00.  Full-corpus checks do not expand scientific review coverage. |
| Post-correction native gate | passed | True | habitatmech:GOLD.0533686915 | Actual successful check; started 2026-10-11T20:13:14.126815+00:00; finished 2026-10-11T20:25:46.436571+00:00. Authoritative full QC on exact head 75dde02c5396a39cb7e9e99b66dafbd653a4510c passed783 tests with3 skipped; all required workflows succeeded. https://github.com/CultureBotAI/HabitatMech/actions/runs/38171265879 Full-corpus checks do not expand scientific review coverage. |

## Scientific And Domain Assessments

### Exact correction and unchanged scientific claims

scope: concern. Targets: habitatmech:GOLD.0533686915.

Removed only the guarded immediate GOLD context contribution ENVO:00000014. Independent parents, source identity, definition, counts/units or omissions and native grounding/mapping status are unchanged, with one appended exclusion event. The full-corpus differential regression limits direct changes to exactly four records. This does not resolve separate mapping-endpoint or source-membership findings. ENVO canal denotes the contained water body, not the channel; the corrected child is liquid-water material. ENVO:00002006 and all four ORGANISM assertions remain. Shared1398 remains open.

## Findings

### F1: Containing setting is emitted as a strict superclass

major / resolved / confirmed; issue key: habitatmech-gold.0533686915-context-parent.

The canal-qualified source denotes liquid water material in a canal, not the canal water body itself. The maintained ITEM decision correctly retains a narrower source mint and ENVO:00002006 liquid-water genus, but the extra ENVO:00000014 canal parent is false material-to-water-body subsumption. All three inspected later organism descriptions say canal water. The mapping endpoint contract defect is separate from the false parent and from the legitimate liquid-water scope. False contribution: ENVO:00000014.

Disposition: Removed only the guarded immediate GOLD context contribution ENVO:00000014. Independent parents, source identity, definition, counts/units or omissions and native grounding/mapping status are unchanged, with one appended exclusion event. The full-corpus differential regression limits direct changes to exactly four records. This does not resolve separate mapping-endpoint or source-membership findings. ENVO canal denotes the contained water body, not the channel; the corrected child is liquid-water material. ENVO:00002006 and all four ORGANISM assertions remain. Shared1398 remains open.

### F2: Retained-source mapping has an implicit ontology-parent endpoint

major / open / confirmed; issue key: habitatmech-gold.0533686915-mapping-endpoint-contract.

Executed route curated_ground_as_parent_from_gold_leaf_synonym retains the source mint but emits skos:narrowMatch using implicit ontology target(s) ENVO:00002006. The declared SourceAttestation endpoint is source -&gt; generated record identifier, with omission when that is the source concept. This is an endpoint contract mismatch, not a formal SKOS self-link prohibition.

## Recommended Actions And Acceptance Checks

### A2

Resolve shared1398 with explicit comparison endpoints and consumer regressions. A global broadMatch/narrowMatch swap does not fix an implicit object. Audit actual SSSOM/KGX outputs against current kg-microbe modeling before claiming compatibility.

- Use maintained source/curation owners, exact source keys and inspected claim-level evidence. Do not hand-edit generated records or rewrite immutable reviews.
- Preserve frozen source IDs, paths, count units, valid independent parents and native lifecycle rules; later exports do not replace original membership.
- For an authorized fix, append required native history, add focused regressions, inspect a seed canary, regenerate affected products and pass schema, strict, labels, reproduction and full QC.
- Save a linked successor observation for any disposition; report persistence alone does not resolve this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| PRIOR | reviews/structured/20261011T200007Z-water/review.yaml | supports | Predecessor full assessment, inspected sources and evidence limitations retained; resolves only its named hierarchy finding. |
| CURRENT | data/habitats/engineered/water.yaml; curation/gold_parent_exclusions.tsv; tests/test_final_engineered_review_fixes.py | supports | Removed only the guarded immediate GOLD context contribution ENVO:00000014. Independent parents, source identity, definition, counts/units or omissions and native grounding/mapping status are unchanged, with one appended exclusion event. The full-corpus differential regression limits direct changes to exactly four records. This does not resolve separate mapping-endpoint or source-membership findings. ENVO canal denotes the contained water body, not the channel; the corrected child is liquid-water material. ENVO:00002006 and all four ORGANISM assertions remain. Shared1398 remains open. |

## Limits And Additional Notes

- Original assertion-level source membership remains unreconstructed. Later GOLD examples do not replace frozen counts.
- Same-agent curation and adversarial assessment, not independent approval.
- Shared1398 and other identity/evidence issues remain unresolved. No SSSOM/KGX readiness certification.
- Full QC covers the captured scientific-input commit. Newly saved successor files require final review-integrity and PR checks.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T202606Z-water-followup
kind: record
repository: CultureBotAI/HabitatMech
title: 'Bounded hierarchy correction follow-up: water'
started_at: '2026-10-11T20:13:00.466493Z'
finished_at: '2026-10-11T20:26:06.942143Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Continuing agent has participated in HabitatMech curation and
    earlier reviews; this is not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Removed only the guarded immediate GOLD context contribution ENVO:00000014.
  Independent parents, source identity, definition, counts/units or omissions and
  native grounding/mapping status are unchanged, with one appended exclusion event.
  The full-corpus differential regression limits direct changes to exactly four records.
  This does not resolve separate mapping-endpoint or source-membership findings. ENVO
  canal denotes the contained water body, not the channel; the corrected child is
  liquid-water material. ENVO:00002006 and all four ORGANISM assertions remain. Shared1398
  remains open.
source:
  git_revision: 75dde02c5396a39cb7e9e99b66dafbd653a4510c
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
  - path: curation/causal_graphs/aquatic_biome.yaml
    sha256: 03ba09d10f9a9d8d32060fc0208b511ef0d59e731fd7c63ca6c02296e70da5f5
    role: context
  - path: curation/causal_graphs/fresh_water.yaml
    sha256: e95ea96aa1912066d4c98cbff91e34528668d4c453d93dc4203c67e7769c691a
    role: context
  - path: curation/causal_graphs/liquid_water.yaml
    sha256: 12aac1021b9b51c6becc4ef8509bd63557b306e42c01d9b4443d69252ce29a81
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
    sha256: 53522d2fbe1cfa6c6a350a46170de9b80b1fa138dfcf4e9ddb0b5851f29d1c88
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
  - path: data/habitats/aquatic/aquatic_biome.yaml
    sha256: 27466c1abb6814aa790ecec6987d803850d0237c697c565e6fc21d1baaebfa27
    role: context
  - path: data/habitats/aquatic/fresh_water.yaml
    sha256: fc60c1fc64ceea8fdf8d2d294dc96c855aa3793962f818e9cdd1b9b3cb87d1be
    role: context
  - path: data/habitats/aquatic/liquid_water.yaml
    sha256: 03eb8ba51e02bc4c8b65b67ae5d8bb740746f8eff51ed81326685fdc5067b081
    role: context
  - path: data/habitats/aquatic/lotic_water_body.yaml
    sha256: b9dbba9e27004357037a63cd68bd7115a71587a9bd99d2f9665a2ee25ad7cdfa
    role: context
  - path: data/habitats/aquatic/water_body.yaml
    sha256: 589b017dac949a9705a816afad5094c2ee9ac1655feb1c771358a07472848239
    role: context
  - path: data/habitats/aquatic/watercourse.yaml
    sha256: 842e375ecdecf70ed4749efd2f3bda791ac6616e58d0e16aa708b57cfde9608d
    role: context
  - path: data/habitats/engineered/built_environment.yaml
    sha256: df6de674d7d48a98b7d1d43a0a5c67a696550f00e1fb787ec71a3569acc47021
    role: context
  - path: data/habitats/engineered/canal.yaml
    sha256: 38fc8422059b667863e073b730df50fc53bd69b2d66b4cffc7013fd9cb1e192e
    role: context
  - path: data/habitats/engineered/engineered__900b76ad.yaml
    sha256: 85154c9542e8e033e17cf631b06a462612229f3bcfdc1cdca0fc6cf73b9b9364
    role: context
  - path: data/habitats/engineered/water.yaml
    sha256: 4fc331521b6793b0a5f7d7172b0808088ca6f316bea7ea1538cfdc49e462aa2c
    role: target
  - path: data/habitats/other/biome.yaml
    sha256: 43080ce9bd411ee97a20d97c17bd923405c040feaf9454d44ca22a2955ce1854
    role: context
  - path: data/habitats/other/environmental.yaml
    sha256: b23a64a2d7594f05716dfc8f525d184fe8bb5d885dbb9e755ba8cc844f433659
    role: context
  - path: data/habitats/other/environmental_system.yaml
    sha256: 2c227791ce7b92c16ae9b76ad8295be95efee73cb65ec7050d1de2b00c8eecbc
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
  - path: history/mappings/water/2026-10-11T200543Z-codex-gpt-5-408512.yaml
    sha256: 8fadba9625359d70ef8ce4ad54c8c6d8df0d8661a576fb2bb56606d1deda5e37
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reviews/structured/20261011T200007Z-water/review.yaml
    sha256: 8c51e6386e90209ee7f109b66ed4be6c413f483489764ec78223ee08ffda5640
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
  - path: tests/test_final_engineered_review_fixes.py
    sha256: 96b92ba7777bc51b576334e2794b3c2aa8055b50781e1eaff0b4af2ab4c55d9d
    role: context
targets:
- target_id: habitatmech:GOLD.0533686915
  path: data/habitats/engineered/water.yaml
  label: Water
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
    role: Frozen source paths, nodes and ORGANISM counts
scope:
  description: Full exact target reassessed for the bounded hierarchy correction,
    retaining predecessor evidence and limitations.
  selection: Successor observation; no additional distinct-record coverage.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.0533686915
checks:
- check_id: C0
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.0533686915
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate
    data/habitats/engineered/water.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T20:06:43.243130+00:00; finished
    2026-10-11T20:06:46.457188+00:00.  Full-corpus checks do not expand scientific
    review coverage.
- check_id: C1
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.0533686915
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-strict
    data/habitats/engineered/water.yaml data/habitats/engineered/wetland_sediment.yaml
    data/habitats/engineered/woodchip_biofilm.yaml data/habitats/engineered/wooden_surface.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T20:06:56.016326+00:00; finished
    2026-10-11T20:07:02.050786+00:00.  Full-corpus checks do not expand scientific
    review coverage.
- check_id: C2
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.0533686915
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T20:07:02.051536+00:00; finished
    2026-10-11T20:07:25.696214+00:00.  Full-corpus checks do not expand scientific
    review coverage.
- check_id: C3
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.0533686915
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T20:07:25.697183+00:00; finished
    2026-10-11T20:08:43.205293+00:00.  Full-corpus checks do not expand scientific
    review coverage.
- check_id: C4
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.0533686915
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T20:08:43.206127+00:00; finished
    2026-10-11T20:08:53.846625+00:00.  Full-corpus checks do not expand scientific
    review coverage.
- check_id: C5
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.0533686915
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T20:08:53.847437+00:00; finished
    2026-10-11T20:09:00.953182+00:00.  Full-corpus checks do not expand scientific
    review coverage.
- check_id: C6
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.0533686915
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T20:09:00.953890+00:00; finished
    2026-10-11T20:09:26.060420+00:00.  Full-corpus checks do not expand scientific
    review coverage.
- check_id: C7
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.0533686915
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache .venv/bin/python
    -m pytest tests/test_final_engineered_review_fixes.py -q
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T20:09:26.061081+00:00; finished
    2026-10-11T20:09:34.124559+00:00.  Full-corpus checks do not expand scientific
    review coverage.
- check_id: C8
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.0533686915
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just provenance-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T20:09:34.125407+00:00; finished
    2026-10-11T20:09:34.924845+00:00.  Full-corpus checks do not expand scientific
    review coverage.
- check_id: C9
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.0533686915
  command: gh pr checks codex/record-reviews-20261011p --watch --interval 30
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T20:13:14.126815+00:00; finished
    2026-10-11T20:25:46.436571+00:00. Authoritative full QC on exact head 75dde02c5396a39cb7e9e99b66dafbd653a4510c
    passed783 tests with3 skipped; all required workflows succeeded. https://github.com/CultureBotAI/HabitatMech/actions/runs/38171265879
    Full-corpus checks do not expand scientific review coverage.
evidence:
- evidence_id: PRIOR
  kind: prior_review
  reference: reviews/structured/20261011T200007Z-water/review.yaml
  accessed_at: '2026-10-11T20:13:00.466493Z'
  support: supports
  summary: Predecessor full assessment, inspected sources and evidence limitations
    retained; resolves only its named hierarchy finding.
- evidence_id: CURRENT
  kind: record_content
  reference: data/habitats/engineered/water.yaml; curation/gold_parent_exclusions.tsv;
    tests/test_final_engineered_review_fixes.py
  accessed_at: '2026-10-11T20:26:06.942143Z'
  support: supports
  summary: Removed only the guarded immediate GOLD context contribution ENVO:00000014.
    Independent parents, source identity, definition, counts/units or omissions and
    native grounding/mapping status are unchanged, with one appended exclusion event.
    The full-corpus differential regression limits direct changes to exactly four
    records. This does not resolve separate mapping-endpoint or source-membership
    findings. ENVO canal denotes the contained water body, not the channel; the corrected
    child is liquid-water material. ENVO:00002006 and all four ORGANISM assertions
    remain. Shared1398 remains open.
assessments:
- assessment_id: CORRECTION
  area: scope
  topic: Exact correction and unchanged scientific claims
  outcome: concern
  target_ids:
  - habitatmech:GOLD.0533686915
  evidence_ids:
  - PRIOR
  - CURRENT
  summary: Removed only the guarded immediate GOLD context contribution ENVO:00000014.
    Independent parents, source identity, definition, counts/units or omissions and
    native grounding/mapping status are unchanged, with one appended exclusion event.
    The full-corpus differential regression limits direct changes to exactly four
    records. This does not resolve separate mapping-endpoint or source-membership
    findings. ENVO canal denotes the contained water body, not the channel; the corrected
    child is liquid-water material. ENVO:00002006 and all four ORGANISM assertions
    remain. Shared1398 remains open.
findings:
- finding_id: F1
  issue_key: habitatmech-gold.0533686915-context-parent
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: Containing setting is emitted as a strict superclass
  description: 'The canal-qualified source denotes liquid water material in a canal,
    not the canal water body itself. The maintained ITEM decision correctly retains
    a narrower source mint and ENVO:00002006 liquid-water genus, but the extra ENVO:00000014
    canal parent is false material-to-water-body subsumption. All three inspected
    later organism descriptions say canal water. The mapping endpoint contract defect
    is separate from the false parent and from the legitimate liquid-water scope.
    False contribution: ENVO:00000014.'
  target_ids:
  - habitatmech:GOLD.0533686915
  field_paths:
  - parent_habitats
  evidence_ids:
  - PRIOR
  - CURRENT
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact source-path and expected-parent guard
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Preserve independent parents
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: An asserted identity, strict relation, source-evidence scope
    or mapping endpoint is materially unsupported.
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261011T200007Z-water
    finding_id: F1
  disposition_reason: Removed only the guarded immediate GOLD context contribution
    ENVO:00000014. Independent parents, source identity, definition, counts/units
    or omissions and native grounding/mapping status are unchanged, with one appended
    exclusion event. The full-corpus differential regression limits direct changes
    to exactly four records. This does not resolve separate mapping-endpoint or source-membership
    findings. ENVO canal denotes the contained water body, not the channel; the corrected
    child is liquid-water material. ENVO:00002006 and all four ORGANISM assertions
    remain. Shared1398 remains open.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1962
- finding_id: F2
  issue_key: habitatmech-gold.0533686915-mapping-endpoint-contract
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Retained-source mapping has an implicit ontology-parent endpoint
  description: Executed route curated_ground_as_parent_from_gold_leaf_synonym retains
    the source mint but emits skos:narrowMatch using implicit ontology target(s) ENVO:00002006.
    The declared SourceAttestation endpoint is source -> generated record identifier,
    with omission when that is the source concept. This is an endpoint contract mismatch,
    not a formal SKOS self-link prohibition.
  target_ids:
  - habitatmech:GOLD.0533686915
  field_paths:
  - source_attestations.mapping_predicate
  - grounding_status
  evidence_ids:
  - PRIOR
  - CURRENT
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Declared comparison endpoints
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Resolver and emitted attestation endpoints
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: An asserted identity, strict relation, source-evidence scope
    or mapping endpoint is materially unsupported.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261011T200007Z-water
    finding_id: F2
actions:
- action_id: A2
  description: Resolve shared1398 with explicit comparison endpoints and consumer
    regressions. A global broadMatch/narrowMatch swap does not fix an implicit object.
    Audit actual SSSOM/KGX outputs against current kg-microbe modeling before claiming
    compatibility.
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.0533686915
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Declared comparison endpoints
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Resolver and emitted attestation endpoints
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Use maintained source/curation owners, exact source keys and inspected claim-level
    evidence. Do not hand-edit generated records or rewrite immutable reviews.
  - Preserve frozen source IDs, paths, count units, valid independent parents and
    native lifecycle rules; later exports do not replace original membership.
  - For an authorized fix, append required native history, add focused regressions,
    inspect a seed canary, regenerate affected products and pass schema, strict, labels,
    reproduction and full QC.
  - Save a linked successor observation for any disposition; report persistence alone
    does not resolve this finding.
limitations:
- Original assertion-level source membership remains unreconstructed. Later GOLD examples
  do not replace frozen counts.
- Same-agent curation and adversarial assessment, not independent approval.
- Shared1398 and other identity/evidence issues remain unresolved. No SSSOM/KGX readiness
  certification.
- Full QC covers the captured scientific-input commit. Newly saved successor files
  require final review-integrity and PR checks.
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261011T200007Z-water
  relationship: Resolves only the named hierarchy finding and carries other findings
    forward
tags:
- habitatmech
- record-review
- followup
```
