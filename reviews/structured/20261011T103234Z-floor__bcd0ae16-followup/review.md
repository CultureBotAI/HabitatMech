# Context-parent correction follow-up: floor__bcd0ae16

- Review: 20261011T103234Z-floor__bcd0ae16-followup
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-11T10:27:34.737261Z
- Finished UTC: 2026-10-11T10:32:34.851083Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Resolved only F1: false strict context parent. Native source identity and SEEDED status remain unchanged.

## Scope And Provenance

Whole exact record, changed hierarchy reassessed and unchanged evidence retained through predecessor.

Selection: Successor to an already reviewed target; no additional corpus coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 28081af81fe6132f018a2bacb6a275245db6542a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.5cc4f65599 | data/habitats/engineered/floor__bcd0ae16.yaml | generated | Floor |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Post-correction native check | passed | True | habitatmech:GOLD.5cc4f65599 | Actual exit0; start 2026-10-11T10:27:25.307546+00:00; finish 2026-10-11T10:27:28.743215+00:00. Full command scope is retained, not additional scientific coverage. |
| Post-correction native check | passed | True | habitatmech:GOLD.5cc4f65599 | Actual exit0; start 2026-10-11T10:27:36.009128+00:00; finish 2026-10-11T10:27:43.418602+00:00. Full command scope is retained, not additional scientific coverage. |
| Post-correction native check | passed | True | habitatmech:GOLD.5cc4f65599 | Actual exit0; start 2026-10-11T10:27:43.419509+00:00; finish 2026-10-11T10:28:07.115074+00:00. Full command scope is retained, not additional scientific coverage. |
| Post-correction native check | passed | True | habitatmech:GOLD.5cc4f65599 | Actual exit0; start 2026-10-11T10:28:07.115904+00:00; finish 2026-10-11T10:29:15.337942+00:00. Full command scope is retained, not additional scientific coverage. |
| Post-correction native check | passed | True | habitatmech:GOLD.5cc4f65599 | Actual exit0; start 2026-10-11T10:29:15.338663+00:00; finish 2026-10-11T10:29:24.233674+00:00. Full command scope is retained, not additional scientific coverage. |
| Post-correction native check | passed | True | habitatmech:GOLD.5cc4f65599 | Actual exit0; start 2026-10-11T10:29:24.234320+00:00; finish 2026-10-11T10:29:29.831185+00:00. Full command scope is retained, not additional scientific coverage. |
| Post-correction native check | passed | True | habitatmech:GOLD.5cc4f65599 | Actual exit0; start 2026-10-11T10:29:29.832029+00:00; finish 2026-10-11T10:29:54.973050+00:00. Full command scope is retained, not additional scientific coverage. |
| Post-correction native check | passed | True | habitatmech:GOLD.5cc4f65599 | Actual exit0; start 2026-10-11T10:29:54.974041+00:00; finish 2026-10-11T10:31:49.627064+00:00. Full command scope is retained, not additional scientific coverage. |
| Final publication QC | skipped | False | habitatmech:GOLD.5cc4f65599 | Final map/site, QC and all-bundle checks follow persistence; no future success is asserted. |

## Scientific And Domain Assessments

### Guarded parent contribution

scope: supported. Targets: habitatmech:GOLD.5cc4f65599.

Floor surface or water material is no longer a subclass of its containing room or experimental enclosure. All unchanged source fields retain predecessor evidence.

### Retained source limitations

identity: supported. Targets: habitatmech:GOLD.5cc4f65599.

Qualified source representation is retained without invented definition, genus or composition. Original source membership is not reconstructed; narrow mapping endpoint issue remains open where applicable.

## Findings

### F1: Containing room or experimental enclosure is emitted as a strict parent

major / resolved / confirmed; issue key: habitatmech-gold.5cc4f65599-context-parent.

The spacecraft-assembly-cleanroom Floor denotes a floor surface, not the containing cleanroom. Inspected later exact organisms explicitly name cleanroom floors. Preserve the 64 frozen ORGANISM observations separately from 65 later matched organisms and remove only the immediate whole-room parent contribution. Unsupported contribution: habitatmech:GOLD.013b99db03.

Disposition: The exact-source/expected-parent exclusion removes only the false room/enclosure contribution. The current record and full-corpus differential regression confirm preserved identity, counts, units, independent parents and lifecycle. No source-definition or mapping-contract resolution is inferred.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| PRIOR | reviews/structured/20261011T102011Z-floor__bcd0ae16/review.yaml; Entire baseline review and its primary evidence | supports | Retains the complete source assessment; only the strict context-parent finding is corrected. |
| CURRENT | data/habitats/engineered/floor__bcd0ae16.yaml; curation/gold_parent_exclusions.tsv; tests/test_gold_parent_exclusions.py; Entire current record; exact guarded row; five-target whole-corpus differential test | supports | The parent list and one appended exclusion event are the only changed fields. Toggling exactly these five exclusions changes no other corpus records. Independent freshwater genus is retained; source identities, units, counts and SEEDED lifecycle are unchanged. |

## Limits And Additional Notes

- Later GOLD members do not reconstruct the original frozen snapshot.
- Same agent authored and assessed the correction; no independent approval.
- Only the demonstrated context edge is resolved. Optional identity/definition gaps and SSSOM/KGX compatibility remain outside this correction.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T103234Z-floor__bcd0ae16-followup
kind: record
repository: culturebotai/HabitatMech
title: 'Context-parent correction follow-up: floor__bcd0ae16'
started_at: '2026-10-11T10:27:34.737261Z'
finished_at: '2026-10-11T10:32:34.851083Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Continuing agent participated in prior reviews and curation;
    adversarial self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Resolved only F1: false strict context parent. Native source identity and
  SEEDED status remain unchanged.'
source:
  git_revision: 28081af81fe6132f018a2bacb6a275245db6542a
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
  - path: curation/causal_graphs/agricultural_soil.yaml
    sha256: 2f9c73b186d6b79df1d64098f929d8364a1768f732101edaf144dee7723c60f4
    role: context
  - path: curation/causal_graphs/aquatic_biome.yaml
    sha256: 03ba09d10f9a9d8d32060fc0208b511ef0d59e731fd7c63ca6c02296e70da5f5
    role: context
  - path: curation/causal_graphs/biofilm.yaml
    sha256: 37fae9d123c2edfb68376b6b4fe5441f72092d48d81dba6f60510087217c8680
    role: context
  - path: curation/causal_graphs/bioreactor.yaml
    sha256: 170d1134c3de38348844e45dbf6d87663dd4a0d1f33fd9e441a4352b6e277583
    role: context
  - path: curation/causal_graphs/brackish_water.yaml
    sha256: b9d58082a53bef1143a3868918cfed7f6d74ba7e2330648069733d9ea2c76508
    role: context
  - path: curation/causal_graphs/building.yaml
    sha256: 9e9360775fdda554b285d7ecfb9b1729bf389b8241376a410eca60bd672eb235
    role: context
  - path: curation/causal_graphs/compost.yaml
    sha256: e0fd3ae54311115939f07ba1f3f158c5c44353bd0fab1dcdc1a9292ff0ad1de5
    role: context
  - path: curation/causal_graphs/deep_marine_sediment.yaml
    sha256: eb6a68290a58ec157a4c9895e082cbba760c47b5fbe35523d3bb163af3091d0c
    role: context
  - path: curation/causal_graphs/forest_soil.yaml
    sha256: faef7b6c26c25ba33110d362dc7e4351440bc08c1106f270e1e6f2decfb1e3f4
    role: context
  - path: curation/causal_graphs/forested_area.yaml
    sha256: eb96b992e1ee8fef7df2550c765a30f0d446082ce16592b6c1da44a54b34e427
    role: context
  - path: curation/causal_graphs/fresh_water.yaml
    sha256: e95ea96aa1912066d4c98cbff91e34528668d4c453d93dc4203c67e7769c691a
    role: context
  - path: curation/causal_graphs/fungi_associated_environment.yaml
    sha256: 45736893315a37e327c25d401ff8794fee47b1056347e52f4980bc3a58e8e0d8
    role: context
  - path: curation/causal_graphs/grassland_soil.yaml
    sha256: 81b2a9ea6255dfbd4b393102b9903dd3c9e8af12f7d3a9adc7c4649650542ae8
    role: context
  - path: curation/causal_graphs/hot_spring.yaml
    sha256: ee0f6d7f7eff179b44e1e934c1c801524062a7e71f3199e16e9ef35e7bad81ed
    role: context
  - path: curation/causal_graphs/hydrothermal_vent.yaml
    sha256: b5c101a93e724531cb7e50e8031203138230c09599855fe8a03bec945469efb0
    role: context
  - path: curation/causal_graphs/hypersaline_water.yaml
    sha256: e974d5e9cc241ac9daf3542ba11156915cfb7786e683ad5ad212af5b35006158
    role: context
  - path: curation/causal_graphs/intestine_environment.yaml
    sha256: 2ef766692eff55471a3322c0cd1cf82188decf37fd5ecd3535cb0ef612e2b725
    role: context
  - path: curation/causal_graphs/leaf.yaml
    sha256: fadc8027b39884bc16cf98f774804a84fd1b1d805876310a47a095f6019435cc
    role: context
  - path: curation/causal_graphs/liquid_water.yaml
    sha256: 12aac1021b9b51c6becc4ef8509bd63557b306e42c01d9b4443d69252ce29a81
    role: context
  - path: curation/causal_graphs/marine_sediment.yaml
    sha256: 8b230eb079171ab8134b648caa29878dc5015fb36362559a6a8c67fb2b433741
    role: context
  - path: curation/causal_graphs/marine_water_body.yaml
    sha256: b2f81102970e9541bf61978fabdd68b7db8f9459f1ef11b467fecfc2956f238b
    role: context
  - path: curation/causal_graphs/milk.yaml
    sha256: 049daa5b499096c61cb625b7bb9ac0f02ea216c96d6b5f7b77126c8709b2378d
    role: context
  - path: curation/causal_graphs/peat_soil.yaml
    sha256: 0f23fa02718b08e3607478ceaa2294320b320ae841a79e144e48ed3497db09e2
    role: context
  - path: curation/causal_graphs/plant_associated_environment.yaml
    sha256: 300044040f76234e7ed3bf373137ba224e55f48e3f3d6d505086b3830877cfcb
    role: context
  - path: curation/causal_graphs/plant_litter.yaml
    sha256: 25e10d6640992be2aa506490f763d8f9642fde125f599207dae7852b6a13b369
    role: context
  - path: curation/causal_graphs/root_nodule.yaml
    sha256: b363e5d418df93d6e44c9d3f3256c8b0ede7c4518125359ffb880020fc00721c
    role: context
  - path: curation/causal_graphs/sea_water.yaml
    sha256: 240ffc8ad2c0abf6f4cce41e01018679aca726816006c90ce329b8d1910d9cd7
    role: context
  - path: curation/causal_graphs/sediment.yaml
    sha256: 62b97afba9466dc64f8b5b1b3fd5d92f8b4b6bf96fe1c761af579ff7deca0e47
    role: context
  - path: curation/causal_graphs/sludge.yaml
    sha256: 55b9c9a27fd00c7b84a8780f2cedc83eeb31ebdda9a2e1029678d96a7fa4a06c
    role: context
  - path: curation/causal_graphs/soil.yaml
    sha256: 2a2bf4b1099b3bc69015f9530cf6e926c05c33667132234b3c52f06aacc957c2
    role: context
  - path: curation/causal_graphs/terrestrial_biome.yaml
    sha256: 239e6a2b711564ed12084cddd1295547d23858dd329c33c538251d5f53c88834
    role: context
  - path: curation/causal_graphs/waste_water.yaml
    sha256: 299b5128af6cf5f7a61ce53304f1084e6eb045414b47cbcfd8832de095142aef
    role: context
  - path: curation/decisions.tsv
    sha256: c2482c7441b08f593baa8bd59546ac68c6e5c7e4e1cb36c24c12a74592b9ff3c
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 40cbf70d74cf127733b793f3936a54472264bfce9f01afc0c449d53b56802683
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
  - path: data/habitats/engineered/floor__bcd0ae16.yaml
    sha256: 723753e9be769daeff39de300acac86ea95a4d8e1bfdda7bd777007511ddbd7f
    role: target
  - path: data/habitats/engineered/spacecraft_assembly_cleanrooms.yaml
    sha256: b53c74f006e0c73ca41c8f26c75ae0a2e8a1d9c1d25a5ec6235219da274a5758
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
  - path: history/mappings/floor__bcd0ae16/2026-10-11T102524Z-codex-gpt-5-0e8602.yaml
    sha256: c92f9825d1486b8d817a4798f71fd609b2e037379854a2c7832ab3e21f7d39fd
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260928T234003Z-floor__bcd0ae16.md
    sha256: 1cf374fde98bf7f8d3bf989328ca3c44eade2e4f44d5d5d2069cc75ccd213cf4
    role: context
  - path: reviews/structured/20261011T102011Z-floor__bcd0ae16/review.yaml
    sha256: 7b78196183c19d1fd301ecb57d5b94bde2080a12cc6138228f5a3dff43b034b3
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
  - path: src/habitatmech/seed.py
    sha256: 4adf105e23d75c3563a516a0c160623d1065df7fcb2f31b7a0a0a8303d0401be
    role: context
  - path: tests/test_gold_parent_exclusions.py
    sha256: 6e6865c91a287fed1d7cf2018062a5a6de64d433576ce041c54198abef67e052
    role: context
scope:
  description: Whole exact record, changed hierarchy reassessed and unchanged evidence
    retained through predecessor.
  selection: Successor to an already reviewed target; no additional corpus coverage.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.5cc4f65599
targets:
- target_id: habitatmech:GOLD.5cc4f65599
  path: data/habitats/engineered/floor__bcd0ae16.yaml
  label: Floor
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: Exact source-concept grounding and identity decisions
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded GOLD context-parent contributions
  - repository: culturebotai/HabitatMech
    path: curation/term_requests.tsv
    role: Authored habitat definition and genus
  - repository: culturebotai/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Pinned ontology identities, labels, definitions and parent axioms
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained harmonization and deterministic generation
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen GOLD paths, node IDs and ORGANISM counts
checks:
- check_id: C2
  name: Post-correction native check
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.5cc4f65599
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate
    data/habitats/engineered/floor__bcd0ae16.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual exit0; start 2026-10-11T10:27:25.307546+00:00; finish 2026-10-11T10:27:28.743215+00:00.
    Full command scope is retained, not additional scientific coverage.
- check_id: C5
  name: Post-correction native check
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.5cc4f65599
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-strict
    data/habitats/engineered/floor.yaml data/habitats/engineered/floor__86528402.yaml
    data/habitats/engineered/floor__bcd0ae16.yaml data/habitats/engineered/freshwater__0ce4d27d.yaml
    data/habitats/engineered/freshwater__fec74bd2.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual exit0; start 2026-10-11T10:27:36.009128+00:00; finish 2026-10-11T10:27:43.418602+00:00.
    Full command scope is retained, not additional scientific coverage.
- check_id: C6
  name: Post-correction native check
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.5cc4f65599
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual exit0; start 2026-10-11T10:27:43.419509+00:00; finish 2026-10-11T10:28:07.115074+00:00.
    Full command scope is retained, not additional scientific coverage.
- check_id: C7
  name: Post-correction native check
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.5cc4f65599
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual exit0; start 2026-10-11T10:28:07.115904+00:00; finish 2026-10-11T10:29:15.337942+00:00.
    Full command scope is retained, not additional scientific coverage.
- check_id: C8
  name: Post-correction native check
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.5cc4f65599
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual exit0; start 2026-10-11T10:29:15.338663+00:00; finish 2026-10-11T10:29:24.233674+00:00.
    Full command scope is retained, not additional scientific coverage.
- check_id: C9
  name: Post-correction native check
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.5cc4f65599
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual exit0; start 2026-10-11T10:29:24.234320+00:00; finish 2026-10-11T10:29:29.831185+00:00.
    Full command scope is retained, not additional scientific coverage.
- check_id: C10
  name: Post-correction native check
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.5cc4f65599
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual exit0; start 2026-10-11T10:29:29.832029+00:00; finish 2026-10-11T10:29:54.973050+00:00.
    Full command scope is retained, not additional scientific coverage.
- check_id: C11
  name: Post-correction native check
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.5cc4f65599
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache .venv/bin/python
    -m pytest tests/test_gold_parent_exclusions.py -q
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
  summary: Actual exit0; start 2026-10-11T10:29:54.974041+00:00; finish 2026-10-11T10:31:49.627064+00:00.
    Full command scope is retained, not additional scientific coverage.
- check_id: QC
  name: Final publication QC
  required: false
  status: skipped
  target_ids:
  - habitatmech:GOLD.5cc4f65599
  summary: Final map/site, QC and all-bundle checks follow persistence; no future
    success is asserted.
evidence:
- evidence_id: PRIOR
  kind: prior_review
  reference: reviews/structured/20261011T102011Z-floor__bcd0ae16/review.yaml
  locator: Entire baseline review and its primary evidence
  accessed_at: '2026-10-11T10:27:34.737261Z'
  support: supports
  summary: Retains the complete source assessment; only the strict context-parent
    finding is corrected.
- evidence_id: CURRENT
  kind: record_content
  reference: data/habitats/engineered/floor__bcd0ae16.yaml; curation/gold_parent_exclusions.tsv;
    tests/test_gold_parent_exclusions.py
  locator: Entire current record; exact guarded row; five-target whole-corpus differential
    test
  accessed_at: '2026-10-11T10:32:34.851083Z'
  support: supports
  summary: The parent list and one appended exclusion event are the only changed fields.
    Toggling exactly these five exclusions changes no other corpus records. Independent
    freshwater genus is retained; source identities, units, counts and SEEDED lifecycle
    are unchanged.
assessments:
- assessment_id: CORRECTION
  area: scope
  topic: Guarded parent contribution
  outcome: supported
  target_ids:
  - habitatmech:GOLD.5cc4f65599
  evidence_ids:
  - PRIOR
  - CURRENT
  summary: Floor surface or water material is no longer a subclass of its containing
    room or experimental enclosure. All unchanged source fields retain predecessor
    evidence.
- assessment_id: SCOPE
  area: identity
  topic: Retained source limitations
  outcome: supported
  target_ids:
  - habitatmech:GOLD.5cc4f65599
  evidence_ids:
  - PRIOR
  - CURRENT
  summary: Qualified source representation is retained without invented definition,
    genus or composition. Original source membership is not reconstructed; narrow
    mapping endpoint issue remains open where applicable.
findings:
- finding_id: F1
  issue_key: habitatmech-gold.5cc4f65599-context-parent
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: Containing room or experimental enclosure is emitted as a strict parent
  description: 'The spacecraft-assembly-cleanroom Floor denotes a floor surface, not
    the containing cleanroom. Inspected later exact organisms explicitly name cleanroom
    floors. Preserve the 64 frozen ORGANISM observations separately from 65 later
    matched organisms and remove only the immediate whole-room parent contribution.
    Unsupported contribution: habitatmech:GOLD.013b99db03.'
  target_ids:
  - habitatmech:GOLD.5cc4f65599
  field_paths:
  - parent_habitats
  evidence_ids:
  - PRIOR
  - CURRENT
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: Material identity, hierarchy, grounding scope or application
    contract requires maintained-input adjudication.
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact-source guarded context-parent exclusion
  previous_occurrences:
  - repository: culturebotai/HabitatMech
    review_id: 20261011T102011Z-floor__bcd0ae16
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1925
  disposition_reason: The exact-source/expected-parent exclusion removes only the
    false room/enclosure contribution. The current record and full-corpus differential
    regression confirm preserved identity, counts, units, independent parents and
    lifecycle. No source-definition or mapping-contract resolution is inferred.
actions: []
limitations:
- Later GOLD members do not reconstruct the original frozen snapshot.
- Same agent authored and assessed the correction; no independent approval.
- Only the demonstrated context edge is resolved. Optional identity/definition gaps
  and SSSOM/KGX compatibility remain outside this correction.
related_reviews:
- repository: culturebotai/HabitatMech
  review_id: 20261011T102011Z-floor__bcd0ae16
  relationship: Resolves F1 only and retains all other predecessor findings
tags:
- habitatmech
- engineered
- record-review
- followup
```
