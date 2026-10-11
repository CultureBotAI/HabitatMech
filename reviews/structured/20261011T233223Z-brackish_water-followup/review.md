# Bounded correction follow-up: brackish_water

- Review: 20261011T233223Z-brackish_water-followup
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-11T23:22:20.315496Z
- Finished UTC: 2026-10-11T23:32:23.093511Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Retyped three bacterioplankton assemblages as COMMUNITY, separated membrane transport from biosynthesis in two descriptions, and compared bacterial doubling time with water residence time. Conditional estuarine scope and inferred selection/filtering remain open. Exact differential assessment preserved identity, definition, source counts/units or omissions, native lifecycle, stable graph IDs and citations. Append-only history records the correction. Full-corpus regression confines hierarchy changes to 21 records; graph corrections add brackish water as the 22nd changed record.

## Scope And Provenance

Full exact target reassessed for bounded hierarchy or graph representation corrections, retaining predecessor evidence and limitations.

Selection: Successor observation; no additional distinct-record coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0a2f8265263e0aa01dda447ac5988cc7a20c50d3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:00002019 | data/habitats/aquatic/brackish_water.yaml | generated | brackish water |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Post-correction native gate | passed | True | ENVO:00002019 | Actual successful check; started 2026-10-11T23:16:46.030548+00:00; finished 2026-10-11T23:16:48.397384+00:00.  Full-corpus checks do not expand scientific coverage. |
| Post-correction native gate | passed | True | ENVO:00002019 | Actual successful check; started 2026-10-11T23:16:48.398053+00:00; finished 2026-10-11T23:16:56.035195+00:00.  Full-corpus checks do not expand scientific coverage. |
| Post-correction native gate | passed | True | ENVO:00002019 | Actual successful check; started 2026-10-11T23:16:56.035867+00:00; finished 2026-10-11T23:17:09.901828+00:00.  Full-corpus checks do not expand scientific coverage. |
| Post-correction native gate | passed | True | ENVO:00002019 | Actual successful check; started 2026-10-11T23:17:09.902524+00:00; finished 2026-10-11T23:17:54.225131+00:00.  Full-corpus checks do not expand scientific coverage. |
| Post-correction native gate | passed | True | ENVO:00002019 | Actual successful check; started 2026-10-11T23:17:54.225783+00:00; finished 2026-10-11T23:18:02.137511+00:00.  Full-corpus checks do not expand scientific coverage. |
| Post-correction native gate | passed | True | ENVO:00002019 | Actual successful check; started 2026-10-11T23:18:02.138162+00:00; finished 2026-10-11T23:18:06.256002+00:00.  Full-corpus checks do not expand scientific coverage. |
| Post-correction native gate | passed | True | ENVO:00002019 | Actual successful check; started 2026-10-11T23:18:06.256855+00:00; finished 2026-10-11T23:18:22.902626+00:00.  Full-corpus checks do not expand scientific coverage. |
| Post-correction native gate | passed | True | ENVO:00002019 | Actual successful check; started 2026-10-11T23:18:22.903300+00:00; finished 2026-10-11T23:18:29.378516+00:00.  Full-corpus checks do not expand scientific coverage. |
| Post-correction native gate | passed | True | ENVO:00002019 | Actual successful check; started 2026-10-11T23:18:29.379248+00:00; finished 2026-10-11T23:18:29.966477+00:00.  Full-corpus checks do not expand scientific coverage. |
| Post-correction native gate | passed | True | ENVO:00002019 | Actual successful check; started 2026-10-11T23:21:16.473248+00:00; finished 2026-10-11T23:29:39.081880+00:00. Authoritative full QC on exact head 0a2f8265263e0aa01dda447ac5988cc7a20c50d3 passed 827 tests with 3 skipped; all required workflows succeeded. https://github.com/CultureBotAI/HabitatMech/actions/runs/38183960050 Full-corpus checks do not expand scientific coverage. |

## Scientific And Domain Assessments

### Exact corrections and unchanged scientific claims

scope: concern. Targets: ENVO:00002019.

Retyped three bacterioplankton assemblages as COMMUNITY, separated membrane transport from biosynthesis in two descriptions, and compared bacterial doubling time with water residence time. Conditional estuarine scope and inferred selection/filtering remain open. Exact differential assessment preserved identity, definition, source counts/units or omissions, native lifecycle, stable graph IDs and citations. Append-only history records the correction. Full-corpus regression confines hierarchy changes to 21 records; graph corrections add brackish water as the 22nd changed record.

## Findings

### F1: Transport is described as synthesizing solutes

minor / resolved / confirmed; issue key: envo-00002019-transport-synthesis-wording.

The osmoregulatory transport description conflates import/export with biosynthesis. Compatible-solute production and transport are distinct mechanisms even when both contribute to homeostasis.

Disposition: Retyped three bacterioplankton assemblages as COMMUNITY, separated membrane transport from biosynthesis in two descriptions, and compared bacterial doubling time with water residence time. Conditional estuarine scope and inferred selection/filtering remain open. Exact differential assessment preserved identity, definition, source counts/units or omissions, native lifecycle, stable graph IDs and citations. Append-only history records the correction. Full-corpus regression confines hierarchy changes to 21 records; graph corrections add brackish water as the 22nd changed record.

### F2: Growth rate is compared directly with a residence duration

minor / resolved / confirmed; issue key: envo-00002019-growth-timescale-wording.

The growth-establishment edge says growth is faster than hydrologic residence time. Its source and notes instead compare doubling time with residence time; the intended conditional result is supported but the description mixes dimensions.

Disposition: Retyped three bacterioplankton assemblages as COMMUNITY, separated membrane transport from biosynthesis in two descriptions, and compared bacterial doubling time with water residence time. Conditional estuarine scope and inferred selection/filtering remain open. Exact differential assessment preserved identity, definition, source counts/units or omissions, native lifecycle, stable graph IDs and citations. Append-only history records the correction. Full-corpus regression confines hierarchy changes to 21 records; graph corrections add brackish water as the 22nd changed record.

### F3: Mixed microbial assemblages are typed as taxa

major / resolved / confirmed; issue key: envo-00002019-community-node-type.

freshwater_bacterioplankton, marine_bacterioplankton and estuarine_bacterioplankton do not denote an organism or clade. Native COMMUNITY is available, so a process type or new schema enum is not an appropriate default replacement.

Disposition: Retyped three bacterioplankton assemblages as COMMUNITY, separated membrane transport from biosynthesis in two descriptions, and compared bacterial doubling time with water residence time. Conditional estuarine scope and inferred selection/filtering remain open. Exact differential assessment preserved identity, definition, source counts/units or omissions, native lifecycle, stable graph IDs and citations. Append-only history records the correction. Full-corpus regression confines hierarchy changes to 21 records; graph corrections add brackish water as the 22nd changed record.

### F4: Some causal scope and detailed evidence remain unsupported

major / open / provisional; issue key: envo-00002019-causal-scope-support.

The estuarine example needs explicit conditional scope in its generic description. Temporal stress intensification and osmotic filtering exceed the inspected spatial, proxy or abstract evidence; metagenomic association is not directly measured physiological selection. This does not show that the mechanisms are false.

## Recommended Actions And Acceptance Checks

### A4

Retain supported edges, qualify context and causal strength, retrieve outstanding passages, and replace title-like snippets with short exact evidence and precise locators. Do not equate a resolving reference with claim support.

- Change only maintained inputs with exact source/edge keys; preserve independent parents, identities, source counts/units and native lifecycle.
- Inspect claim-level sources; append required curation history, add focused regressions, inspect a seed canary and regenerate affected products.
- Pass schema, strict, product-label, corpus reproduction, causal/history, review-integrity and full QC; save a linked successor for each finding disposition.
- Compare actual semantic-map inputs and perform genuine regeneration when changed; do not substitute a checksum-only refresh.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| PRIOR | reviews/structured/20261011T225628Z-brackish_water/review.yaml | supports | Predecessor full assessment, inspected primary sources and access limitations retained; resolves only the explicitly corrected findings. |
| CURRENT | data/habitats/aquatic/brackish_water.yaml; curation/gold_parent_exclusions.tsv; src/habitatmech/schema/habitatmech.yaml; tests/test_second_aquatic_review_fixes.py | supports | Retyped three bacterioplankton assemblages as COMMUNITY, separated membrane transport from biosynthesis in two descriptions, and compared bacterial doubling time with water residence time. Conditional estuarine scope and inferred selection/filtering remain open. Exact differential assessment preserved identity, definition, source counts/units or omissions, native lifecycle, stable graph IDs and citations. Append-only history records the correction. Full-corpus regression confines hierarchy changes to 21 records; graph corrections add brackish water as the 22nd changed record. |

## Limits And Additional Notes

- Original assertion-level source membership remains unreconstructed; later GOLD examples do not replace frozen counts.
- All predecessor literature-access and source-support limits remain. A resolving citation or passing schema gate is not proof of a causal mechanism.
- Product-label checks exclude 2057 SKIPPED_NO_ADAPTER targets and retain accepted label exceptions; they do not establish habitat occurrence or ontology correctness.
- Shared mapping-endpoint and typed-synonym issues remain unresolved. No SSSOM/KGX readiness certification.
- Full QC covers the captured scientific-input commit; newly saved successor files still require final review-integrity and PR checks.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T233223Z-brackish_water-followup
kind: record
repository: CultureBotAI/HabitatMech
title: 'Bounded correction follow-up: brackish_water'
started_at: '2026-10-11T23:22:20.315496Z'
finished_at: '2026-10-11T23:32:23.093511Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent authored the curation and adversarial assessment;
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Retyped three bacterioplankton assemblages as COMMUNITY, separated membrane
  transport from biosynthesis in two descriptions, and compared bacterial doubling
  time with water residence time. Conditional estuarine scope and inferred selection/filtering
  remain open. Exact differential assessment preserved identity, definition, source
  counts/units or omissions, native lifecycle, stable graph IDs and citations. Append-only
  history records the correction. Full-corpus regression confines hierarchy changes
  to 21 records; graph corrections add brackish water as the 22nd changed record.
source:
  git_revision: 0a2f8265263e0aa01dda447ac5988cc7a20c50d3
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
  - path: curation/causal_graphs/brackish_water.yaml
    sha256: f1aa7c2da472738a86f75a54e451c56bf588896dd9e65ce0e3cc707b29671ef2
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
    sha256: 89671725df3555b8057c163bbd822d702cdedd9cbd2c2fd3fed619bb041f7adf
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
  - path: data/habitats/aquatic/brackish_water.yaml
    sha256: d9d40b215818bde55a405b40affa8c2642c7f8af766be7660d214139c58cf5e0
    role: target
  - path: data/habitats/aquatic/liquid_water.yaml
    sha256: 03eb8ba51e02bc4c8b65b67ae5d8bb740746f8eff51ed81326685fdc5067b081
    role: context
  - path: data/habitats/aquatic/saline_water.yaml
    sha256: 0114f8f1def88f8f8ce2b675bdd8b96e44ca92248424969288ebaa803fa8c248
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
  - path: history/mappings/brackish_water/2026-10-11T231512Z-codex-gpt-5-745f6b.yaml
    sha256: 88cceaa3bebe874a615fc6f166cfec7a30fe0eeec4d12b874ae17d15c4f0c61e
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260923T140218Z-brackish_water.md
    sha256: 0020d79e17fcbb4578992eb616860c9e2c22bb2af85ea751d1c6082cd3e08b33
    role: context
  - path: reports/yaml_record_review/20260923T142152Z-brackish_water_body.md
    sha256: 408a6c249cac27dba6940eacbd87a92f621a4c3b8aea068f5a671074870a5c01
    role: context
  - path: reports/yaml_record_review/20261002T025158Z-estuarine_biome.md
    sha256: fe6064e80d77aa66261fc02c56d58d48991cddb1e3d5eb002906aca712f0284a
    role: context
  - path: reports/yaml_record_review/20261003T190816Z-marine_lake.md
    sha256: 5b2c24401d3e534c3b85cbc016896750eb8cc311f05029f06ad9f81c5326374a
    role: context
  - path: reviews/structured/20261011T225628Z-brackish_water/review.yaml
    sha256: feae340461ad6ff5b1a17c3e0de221efc4b0ec297dc3e62644ca776f98277ac3
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
  - path: tests/test_second_aquatic_review_fixes.py
    sha256: 2399866a766986d4db0a19fc26f679149b0c3f90e7906f2187fabc1dfeb0a60e
    role: context
targets:
- target_id: ENVO:00002019
  path: data/habitats/aquatic/brackish_water.yaml
  label: brackish water
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
    path: data/raw/madin_habitats.tsv
    role: Frozen Madin source habitat
  - repository: CultureBotAI/HabitatMech
    path: data/raw/madin_habitat_taxa.tsv
    role: Frozen Madin taxa
  - repository: CultureBotAI/HabitatMech
    path: data/raw/environment_parameters.tsv
    role: Frozen source-specific qualitative environmental parameter bands
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitats.tsv
    role: Frozen PREGO habitat identity and count
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Frozen top-ranked taxon associations
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/brackish_water.yaml
    role: Authored causal graph nodes, directed edges and claim-level evidence
scope:
  description: Full exact target reassessed for bounded hierarchy or graph representation
    corrections, retaining predecessor evidence and limitations.
  selection: Successor observation; no additional distinct-record coverage.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:00002019
checks:
- check_id: C0
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:00002019
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate
    data/habitats/aquatic/brackish_water.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T23:16:46.030548+00:00; finished
    2026-10-11T23:16:48.397384+00:00.  Full-corpus checks do not expand scientific
    coverage.
- check_id: C1
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:00002019
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-strict
    data/habitats/aquatic/beach.yaml data/habitats/aquatic/benthic_zone.yaml data/habitats/aquatic/biofilm__599a99de.yaml
    data/habitats/aquatic/biofilm__5f164a0f.yaml data/habitats/aquatic/biofilm__cc6fe05a.yaml
    data/habitats/aquatic/biofilm__e72e4f05.yaml data/habitats/aquatic/biofouling.yaml
    data/habitats/aquatic/biofouling__438bcaa2.yaml data/habitats/aquatic/biofouling__50243100.yaml
    data/habitats/aquatic/biofouling__fa010eab.yaml data/habitats/aquatic/bog_lake.yaml
    data/habitats/aquatic/borehole.yaml data/habitats/aquatic/brine__2299825d.yaml
    data/habitats/aquatic/canal__c42831a4.yaml data/habitats/aquatic/cave_lake.yaml
    data/habitats/aquatic/cave_microbial_mat.yaml data/habitats/aquatic/cave_pool.yaml
    data/habitats/aquatic/cave_pool_sediment.yaml data/habitats/aquatic/cave_stream.yaml
    data/habitats/aquatic/cave_stream_sediment.yaml data/habitats/aquatic/chemocline.yaml
    data/habitats/aquatic/brackish_water.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T23:16:48.398053+00:00; finished
    2026-10-11T23:16:56.035195+00:00.  Full-corpus checks do not expand scientific
    coverage.
- check_id: C2
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:00002019
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T23:16:56.035867+00:00; finished
    2026-10-11T23:17:09.901828+00:00.  Full-corpus checks do not expand scientific
    coverage.
- check_id: C3
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:00002019
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T23:17:09.902524+00:00; finished
    2026-10-11T23:17:54.225131+00:00.  Full-corpus checks do not expand scientific
    coverage.
- check_id: C4
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:00002019
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T23:17:54.225783+00:00; finished
    2026-10-11T23:18:02.137511+00:00.  Full-corpus checks do not expand scientific
    coverage.
- check_id: C5
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:00002019
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T23:18:02.138162+00:00; finished
    2026-10-11T23:18:06.256002+00:00.  Full-corpus checks do not expand scientific
    coverage.
- check_id: C6
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:00002019
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T23:18:06.256855+00:00; finished
    2026-10-11T23:18:22.902626+00:00.  Full-corpus checks do not expand scientific
    coverage.
- check_id: C7
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:00002019
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache .venv/bin/python
    -m pytest tests/test_second_aquatic_review_fixes.py -q
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T23:18:22.903300+00:00; finished
    2026-10-11T23:18:29.378516+00:00.  Full-corpus checks do not expand scientific
    coverage.
- check_id: C8
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:00002019
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just provenance-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T23:18:29.379248+00:00; finished
    2026-10-11T23:18:29.966477+00:00.  Full-corpus checks do not expand scientific
    coverage.
- check_id: C9
  name: Post-correction native gate
  required: true
  status: passed
  target_ids:
  - ENVO:00002019
  command: gh pr checks codex/record-reviews-20261011r --watch --interval 30
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual successful check; started 2026-10-11T23:21:16.473248+00:00; finished
    2026-10-11T23:29:39.081880+00:00. Authoritative full QC on exact head 0a2f8265263e0aa01dda447ac5988cc7a20c50d3
    passed 827 tests with 3 skipped; all required workflows succeeded. https://github.com/CultureBotAI/HabitatMech/actions/runs/38183960050
    Full-corpus checks do not expand scientific coverage.
evidence:
- evidence_id: PRIOR
  kind: prior_review
  reference: reviews/structured/20261011T225628Z-brackish_water/review.yaml
  accessed_at: '2026-10-11T23:22:20.315496Z'
  support: supports
  summary: Predecessor full assessment, inspected primary sources and access limitations
    retained; resolves only the explicitly corrected findings.
- evidence_id: CURRENT
  kind: record_content
  reference: data/habitats/aquatic/brackish_water.yaml; curation/gold_parent_exclusions.tsv;
    src/habitatmech/schema/habitatmech.yaml; tests/test_second_aquatic_review_fixes.py
  accessed_at: '2026-10-11T23:32:23.093511Z'
  support: supports
  summary: Retyped three bacterioplankton assemblages as COMMUNITY, separated membrane
    transport from biosynthesis in two descriptions, and compared bacterial doubling
    time with water residence time. Conditional estuarine scope and inferred selection/filtering
    remain open. Exact differential assessment preserved identity, definition, source
    counts/units or omissions, native lifecycle, stable graph IDs and citations. Append-only
    history records the correction. Full-corpus regression confines hierarchy changes
    to 21 records; graph corrections add brackish water as the 22nd changed record.
assessments:
- assessment_id: CORRECTION
  area: scope
  topic: Exact corrections and unchanged scientific claims
  outcome: concern
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - PRIOR
  - CURRENT
  summary: Retyped three bacterioplankton assemblages as COMMUNITY, separated membrane
    transport from biosynthesis in two descriptions, and compared bacterial doubling
    time with water residence time. Conditional estuarine scope and inferred selection/filtering
    remain open. Exact differential assessment preserved identity, definition, source
    counts/units or omissions, native lifecycle, stable graph IDs and citations. Append-only
    history records the correction. Full-corpus regression confines hierarchy changes
    to 21 records; graph corrections add brackish water as the 22nd changed record.
findings:
- finding_id: F1
  issue_key: envo-00002019-transport-synthesis-wording
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Transport is described as synthesizing solutes
  description: The osmoregulatory transport description conflates import/export with
    biosynthesis. Compatible-solute production and transport are distinct mechanisms
    even when both contribute to homeostasis.
  target_ids:
  - ENVO:00002019
  field_paths:
  - causal_graphs[0].edges
  evidence_ids:
  - PRIOR
  - CURRENT
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/brackish_water.yaml
    role: Transport and synthesis descriptions
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: minor
  normalization_reason: Bounded wording or provenance limitation; identity is not
    disproved.
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261011T225628Z-brackish_water
    finding_id: F1
  disposition_reason: Retyped three bacterioplankton assemblages as COMMUNITY, separated
    membrane transport from biosynthesis in two descriptions, and compared bacterial
    doubling time with water residence time. Conditional estuarine scope and inferred
    selection/filtering remain open. Exact differential assessment preserved identity,
    definition, source counts/units or omissions, native lifecycle, stable graph IDs
    and citations. Append-only history records the correction. Full-corpus regression
    confines hierarchy changes to 21 records; graph corrections add brackish water
    as the 22nd changed record.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1980
- finding_id: F2
  issue_key: envo-00002019-growth-timescale-wording
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Growth rate is compared directly with a residence duration
  description: The growth-establishment edge says growth is faster than hydrologic
    residence time. Its source and notes instead compare doubling time with residence
    time; the intended conditional result is supported but the description mixes dimensions.
  target_ids:
  - ENVO:00002019
  field_paths:
  - causal_graphs[0].edges
  evidence_ids:
  - PRIOR
  - CURRENT
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/brackish_water.yaml
    role: Growth/residence description
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: minor
  normalization_reason: Bounded wording or provenance limitation; identity is not
    disproved.
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261011T225628Z-brackish_water
    finding_id: F2
  disposition_reason: Retyped three bacterioplankton assemblages as COMMUNITY, separated
    membrane transport from biosynthesis in two descriptions, and compared bacterial
    doubling time with water residence time. Conditional estuarine scope and inferred
    selection/filtering remain open. Exact differential assessment preserved identity,
    definition, source counts/units or omissions, native lifecycle, stable graph IDs
    and citations. Append-only history records the correction. Full-corpus regression
    confines hierarchy changes to 21 records; graph corrections add brackish water
    as the 22nd changed record.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1980
- finding_id: F3
  issue_key: envo-00002019-community-node-type
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: Mixed microbial assemblages are typed as taxa
  description: freshwater_bacterioplankton, marine_bacterioplankton and estuarine_bacterioplankton
    do not denote an organism or clade. Native COMMUNITY is available, so a process
    type or new schema enum is not an appropriate default replacement.
  target_ids:
  - ENVO:00002019
  field_paths:
  - causal_graphs[0].nodes
  evidence_ids:
  - PRIOR
  - CURRENT
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/brackish_water.yaml
    role: Exact node typing
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: Material hierarchy, scope, entity typing or comparison-contract
    defect.
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261011T225628Z-brackish_water
    finding_id: F3
  disposition_reason: Retyped three bacterioplankton assemblages as COMMUNITY, separated
    membrane transport from biosynthesis in two descriptions, and compared bacterial
    doubling time with water residence time. Conditional estuarine scope and inferred
    selection/filtering remain open. Exact differential assessment preserved identity,
    definition, source counts/units or omissions, native lifecycle, stable graph IDs
    and citations. Append-only history records the correction. Full-corpus regression
    confines hierarchy changes to 21 records; graph corrections add brackish water
    as the 22nd changed record.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1980
- finding_id: F4
  issue_key: envo-00002019-causal-scope-support
  category: scope
  severity: major
  status: open
  certainty: provisional
  title: Some causal scope and detailed evidence remain unsupported
  description: The estuarine example needs explicit conditional scope in its generic
    description. Temporal stress intensification and osmotic filtering exceed the
    inspected spatial, proxy or abstract evidence; metagenomic association is not
    directly measured physiological selection. This does not show that the mechanisms
    are false.
  target_ids:
  - ENVO:00002019
  field_paths:
  - causal_graphs[0].description
  - causal_graphs[0].edges
  evidence_ids:
  - PRIOR
  - CURRENT
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/brackish_water.yaml
    role: Conditional scope and claim-level evidence
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: Material hierarchy, scope, entity typing or comparison-contract
    defect.
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261011T225628Z-brackish_water
    finding_id: F4
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1981
actions:
- action_id: A4
  description: Retain supported edges, qualify context and causal strength, retrieve
    outstanding passages, and replace title-like snippets with short exact evidence
    and precise locators. Do not equate a resolving reference with claim support.
  finding_ids:
  - F4
  target_ids:
  - ENVO:00002019
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/brackish_water.yaml
    role: Conditional scope and claim-level evidence
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Change only maintained inputs with exact source/edge keys; preserve independent
    parents, identities, source counts/units and native lifecycle.
  - Inspect claim-level sources; append required curation history, add focused regressions,
    inspect a seed canary and regenerate affected products.
  - Pass schema, strict, product-label, corpus reproduction, causal/history, review-integrity
    and full QC; save a linked successor for each finding disposition.
  - Compare actual semantic-map inputs and perform genuine regeneration when changed;
    do not substitute a checksum-only refresh.
limitations:
- Original assertion-level source membership remains unreconstructed; later GOLD examples
  do not replace frozen counts.
- All predecessor literature-access and source-support limits remain. A resolving
  citation or passing schema gate is not proof of a causal mechanism.
- Product-label checks exclude 2057 SKIPPED_NO_ADAPTER targets and retain accepted
  label exceptions; they do not establish habitat occurrence or ontology correctness.
- Shared mapping-endpoint and typed-synonym issues remain unresolved. No SSSOM/KGX
  readiness certification.
- Full QC covers the captured scientific-input commit; newly saved successor files
  still require final review-integrity and PR checks.
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261011T225628Z-brackish_water
  relationship: Resolves only the named corrected findings and carries all other findings
    forward
tags:
- habitatmech
- record-review
- followup
```
