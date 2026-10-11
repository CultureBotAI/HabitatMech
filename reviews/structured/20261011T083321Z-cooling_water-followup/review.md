# Context-parent correction follow-up: cooling_water

- Review: 20261011T083321Z-cooling_water-followup
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-11T08:31:18.424048Z
- Finished UTC: 2026-10-11T08:33:21.204702Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Resolved F1 only: false strict context parent. F2 source-identity scope remains open in #1917. EXACT/SEEDED metadata is unchanged, not scientifically endorsed by this bounded fix.

## Scope And Provenance

Whole exact current target with changed hierarchy reassessed and unchanged field evidence retained through predecessor.

Selection: Successor for an already-reviewed target; no additional corpus coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8e710b85acdb378be33d8d3bdd58f47a9c1e67a4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:03600002 | data/habitats/engineered/cooling_water.yaml | generated | cooling water |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Post-correction validate | passed | True | ENVO:03600002 | Actual exit0; start 2026-10-11T08:30:26.624109+00:00; finish 2026-10-11T08:30:29.212009+00:00. Native command scope retained. |
| Post-correction validate-strict | passed | True | ENVO:03600002 | Actual exit0; start 2026-10-11T08:30:31.838386+00:00; finish 2026-10-11T08:30:36.189080+00:00. Native command scope retained. |
| Post-correction verify-corpus | passed | True | ENVO:03600002 | Actual exit0; start 2026-10-11T08:30:36.189594+00:00; finish 2026-10-11T08:30:50.205649+00:00. Native command scope retained. |
| Post-correction validate-products | passed | True | ENVO:03600002 | Actual exit0; start 2026-10-11T08:30:50.206397+00:00; finish 2026-10-11T08:31:33.327295+00:00. Native command scope retained. |
| Post-correction validate-history | passed | True | ENVO:03600002 | Actual exit0; start 2026-10-11T08:31:33.328506+00:00; finish 2026-10-11T08:31:40.627525+00:00. Native command scope retained. |
| Post-correction validate-causal-all | passed | True | ENVO:03600002 | Actual exit0; start 2026-10-11T08:31:40.628162+00:00; finish 2026-10-11T08:31:45.256506+00:00. Native command scope retained. |
| Post-correction term-requests-check | passed | True | ENVO:03600002 | Actual exit0; start 2026-10-11T08:31:45.257090+00:00; finish 2026-10-11T08:31:59.035096+00:00. Native command scope retained. |
| Post-correction -m | passed | True | ENVO:03600002 | Actual exit0; start 2026-10-11T08:31:59.035769+00:00; finish 2026-10-11T08:33:10.219444+00:00. Native command scope retained. |
| Final publication QC | skipped | False | ENVO:03600002 | Full final QC and immutable-bundle checks follow saving; no future result is asserted. |

## Scientific And Domain Assessments

### Guarded context-parent exclusion

scope: supported. Targets: ENVO:03600002.

Only the source-context parent and an appended audit event change; independent ontology genus ENVO:00002006 and original source metadata remain intact.

### Original source mapping scope

identity: concern. Targets: ENVO:03600002.

The mapping-scope finding remains provisional and open; this exclusion does not settle it or promote native status.

## Findings

### F1: Containing or source context is emitted as a strict parent

major / resolved / confirmed; issue key: envo-03600002-context-parent.

ENVO supports cooling water as liquid water. All four exact later samples describe water from the secondary cooling system of a nuclear test reactor. A reactor is containing context, not a strict superclass of the water. Whether the source qualifier warrants a distinct narrower mint remains a separate mapping assessment. Unsupported strict parent=ENVO:02000136.

Disposition: Exact source-path/expected-parent exclusion removes only the false immediate context contribution. Inspected current YAML and whole-corpus differential regression confirm all other fields and native status are preserved. The separate source-identity finding F2 remains open.

### F2: Exact source-to-ontology mapping needs original scope reconciliation

major / open / provisional; issue key: envo-03600002-source-identity-scope.

Original source scope and the exact source-to-ontology mapping remain unresolved. The bounded parent correction does not establish whether the original source qualifier is defining or how facility/material context should be represented. See predecessor F2 and the exact later source evidence; this successor does not silently close that finding.

## Recommended Actions And Acceptance Checks

### A2

Recover original bin intent and reconcile the exact mapping. Do not infer an industrial-contaminant composition or auto-replace source identity merely from hierarchy. Preserve original membership/count semantics and lifecycle; removing a false parent alone does not resolve this finding.

- Use exact source identifiers and inspected primary evidence; do not invent a replacement or infer ecological absence.
- Preserve counts/units, source provenance and immutable reviews. Append native history for curation.
- Add a focused regression, dry seed, inspect a canary, regenerate affected products and pass strict, history, provenance, label, corpus and full QC gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| PRIOR | reviews/structured/20261011T082507Z-cooling_water/review.yaml; Entire initial exact-target review, including F1/F2 and all source evidence | supports | Retains the prior full-record assessment. Only the demonstrated context-parent contribution is corrected; original mapping intent remains unresolved. |
| CURRENT | data/habitats/engineered/cooling_water.yaml; curation/gold_parent_exclusions.tsv; tests/test_gold_parent_exclusions.py; Entire current YAML, exact guarded row, native history and whole-corpus differential regression | supports | Only parent_habitats and one appended SOURCE_PARENT_EXCLUDED event change. The whole-corpus regression proves no other current records differ when these two exclusions are toggled. Identity, definition, counts, units, paths, EXACT and SEEDED remain unchanged. |
| SCOPE | https://gold.jgi.doe.gov/download?mode=site_excel; Exact tuple members documented in predecessor BULK evidence and current primary ENVO meanings | supports | Four later BioSamples describe secondary cooling-system water; water is not a reactor. Later membership is not original frozen source-intent reconstruction. Independent ontology genus ENVO:00002006 is retained. |

## Limits And Additional Notes

- Original frozen source intent is not reconstructed from later GOLD members.
- Same agent authored and checked the correction; no independent approval is claimed.
- No SSSOM/KGX readiness certification; #1398 and the source-identity finding remain separate.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T083321Z-cooling_water-followup
kind: record
repository: culturebotai/HabitatMech
title: 'Context-parent correction follow-up: cooling_water'
started_at: '2026-10-11T08:31:18.424048Z'
finished_at: '2026-10-11T08:33:21.204702Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Continuing agent participated in prior reviews/curation; adversarial
    self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Resolved F1 only: false strict context parent. F2 source-identity scope
  remains open in #1917. EXACT/SEEDED metadata is unchanged, not scientifically endorsed
  by this bounded fix.'
source:
  git_revision: 8e710b85acdb378be33d8d3bdd58f47a9c1e67a4
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
    sha256: a82d2c6df0a987010b83d2c29c7e65c49e30538d8c3d3a095968e4451dc85d80
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
  - path: data/habitats/aquatic/liquid_water.yaml
    sha256: 03eb8ba51e02bc4c8b65b67ae5d8bb740746f8eff51ed81326685fdc5067b081
    role: context
  - path: data/habitats/engineered/cooling_water.yaml
    sha256: b83bc5a4cf0bf2b7abf773f6af9f5408484a2b3113aeea68b8ac43140f35f4a9
    role: target
  - path: data/habitats/engineered/research_nuclear_reactor.yaml
    sha256: 2efb65b3b767573e97e0f5765c3d09db036377b5eb2d1b0f0eba09b0c03fab71
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
  - path: history/mappings/cooling_water/2026-10-11T082954Z-codex-gpt-5-3c1ef5.yaml
    sha256: e99d99d501bd1a7b1734bdbd280384dc839a54953ccfe84e6915d853ac6b0d33
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260924T121424Z-cooling_water.md
    sha256: 2db98ba79b746e62fcf918b0e7130a599681b328db7e6d63c78ff20c18babaeb
    role: context
  - path: reviews/structured/20261011T082507Z-cooling_water/review.yaml
    sha256: 2e3e49d9ad44b60fa3667d33f4ddbe1345175d62c3ff833311edb85d09e93b75
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
    sha256: 2f360659b91179711764cff4b7c59d79ceebf14c97eaf8e763b3192205d28787
    role: context
scope:
  description: Whole exact current target with changed hierarchy reassessed and unchanged
    field evidence retained through predecessor.
  selection: Successor for an already-reviewed target; no additional corpus coverage.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:03600002
targets:
- target_id: ENVO:03600002
  path: data/habitats/engineered/cooling_water.yaml
  label: cooling water
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
- check_id: C0
  name: Post-correction validate
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T08:30:26.624109+00:00; finish 2026-10-11T08:30:29.212009+00:00.
    Native command scope retained.
  target_ids:
  - ENVO:03600002
  command: just validate data/habitats/engineered/cooling_water.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
- check_id: C2
  name: Post-correction validate-strict
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T08:30:31.838386+00:00; finish 2026-10-11T08:30:36.189080+00:00.
    Native command scope retained.
  target_ids:
  - ENVO:03600002
  command: just validate-strict data/habitats/engineered/cooling_water.yaml data/habitats/engineered/dairy_farm.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
- check_id: C3
  name: Post-correction verify-corpus
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T08:30:36.189594+00:00; finish 2026-10-11T08:30:50.205649+00:00.
    Native command scope retained.
  target_ids:
  - ENVO:03600002
  command: just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
- check_id: C4
  name: Post-correction validate-products
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T08:30:50.206397+00:00; finish 2026-10-11T08:31:33.327295+00:00.
    Native command scope retained.
  target_ids:
  - ENVO:03600002
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
- check_id: C5
  name: Post-correction validate-history
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T08:31:33.328506+00:00; finish 2026-10-11T08:31:40.627525+00:00.
    Native command scope retained.
  target_ids:
  - ENVO:03600002
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
- check_id: C6
  name: Post-correction validate-causal-all
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T08:31:40.628162+00:00; finish 2026-10-11T08:31:45.256506+00:00.
    Native command scope retained.
  target_ids:
  - ENVO:03600002
  command: just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
- check_id: C7
  name: Post-correction term-requests-check
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T08:31:45.257090+00:00; finish 2026-10-11T08:31:59.035096+00:00.
    Native command scope retained.
  target_ids:
  - ENVO:03600002
  command: just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
- check_id: C8
  name: Post-correction -m
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T08:31:59.035769+00:00; finish 2026-10-11T08:33:10.219444+00:00.
    Native command scope retained.
  target_ids:
  - ENVO:03600002
  command: .venv/bin/python -m pytest tests/test_gold_parent_exclusions.py -q
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - CURRENT
- check_id: QC
  name: Final publication QC
  status: skipped
  required: false
  summary: Full final QC and immutable-bundle checks follow saving; no future result
    is asserted.
  target_ids:
  - ENVO:03600002
evidence:
- evidence_id: PRIOR
  kind: prior_review
  reference: reviews/structured/20261011T082507Z-cooling_water/review.yaml
  locator: Entire initial exact-target review, including F1/F2 and all source evidence
  accessed_at: '2026-10-11T08:31:18.424048Z'
  support: supports
  summary: Retains the prior full-record assessment. Only the demonstrated context-parent
    contribution is corrected; original mapping intent remains unresolved.
- evidence_id: CURRENT
  kind: record_content
  reference: data/habitats/engineered/cooling_water.yaml; curation/gold_parent_exclusions.tsv;
    tests/test_gold_parent_exclusions.py
  locator: Entire current YAML, exact guarded row, native history and whole-corpus
    differential regression
  accessed_at: '2026-10-11T08:33:21.204196Z'
  support: supports
  summary: Only parent_habitats and one appended SOURCE_PARENT_EXCLUDED event change.
    The whole-corpus regression proves no other current records differ when these
    two exclusions are toggled. Identity, definition, counts, units, paths, EXACT
    and SEEDED remain unchanged.
- evidence_id: SCOPE
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  locator: Exact tuple members documented in predecessor BULK evidence and current
    primary ENVO meanings
  accessed_at: '2026-10-11T08:31:18.424048Z'
  support: supports
  snapshot_sha256: 5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439
  summary: Four later BioSamples describe secondary cooling-system water; water is
    not a reactor. Later membership is not original frozen source-intent reconstruction.
    Independent ontology genus ENVO:00002006 is retained.
assessments:
- assessment_id: CORRECTION
  area: scope
  topic: Guarded context-parent exclusion
  outcome: supported
  summary: Only the source-context parent and an appended audit event change; independent
    ontology genus ENVO:00002006 and original source metadata remain intact.
  target_ids:
  - ENVO:03600002
  evidence_ids:
  - PRIOR
  - CURRENT
  - SCOPE
- assessment_id: IDENTITY
  area: identity
  topic: Original source mapping scope
  outcome: concern
  summary: The mapping-scope finding remains provisional and open; this exclusion
    does not settle it or promote native status.
  target_ids:
  - ENVO:03600002
  evidence_ids:
  - PRIOR
  - CURRENT
  - SCOPE
findings:
- finding_id: F1
  issue_key: envo-03600002-context-parent
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: Containing or source context is emitted as a strict parent
  description: ENVO supports cooling water as liquid water. All four exact later samples
    describe water from the secondary cooling system of a nuclear test reactor. A
    reactor is containing context, not a strict superclass of the water. Whether the
    source qualifier warrants a distinct narrower mint remains a separate mapping
    assessment. Unsupported strict parent=ENVO:02000136.
  target_ids:
  - ENVO:03600002
  field_paths:
  - parent_habitats
  evidence_ids:
  - PRIOR
  - CURRENT
  - SCOPE
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: Material identity, hierarchy or synonym scope needs supported
    maintained-input curation.
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact source-path and expected-parent guard
  previous_occurrences:
  - repository: culturebotai/HabitatMech
    review_id: 20261011T082507Z-cooling_water
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1916
  disposition_reason: Exact source-path/expected-parent exclusion removes only the
    false immediate context contribution. Inspected current YAML and whole-corpus
    differential regression confirm all other fields and native status are preserved.
    The separate source-identity finding F2 remains open.
- finding_id: F2
  issue_key: envo-03600002-source-identity-scope
  category: scope
  severity: major
  status: open
  certainty: provisional
  title: Exact source-to-ontology mapping needs original scope reconciliation
  description: Original source scope and the exact source-to-ontology mapping remain
    unresolved. The bounded parent correction does not establish whether the original
    source qualifier is defining or how facility/material context should be represented.
    See predecessor F2 and the exact later source evidence; this successor does not
    silently close that finding.
  target_ids:
  - ENVO:03600002
  field_paths:
  - grounding_status
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - PRIOR
  - CURRENT
  - SCOPE
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: Material identity, hierarchy or synonym scope needs supported
    maintained-input curation.
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: ITEM assessment of exact GOLD source concept
  - repository: culturebotai/HabitatMech
    path: curation/term_requests.tsv
    role: Only evidence-supported identity and genus
  previous_occurrences:
  - repository: culturebotai/HabitatMech
    review_id: 20261011T082507Z-cooling_water
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1917
actions:
- action_id: A2
  description: Recover original bin intent and reconcile the exact mapping. Do not
    infer an industrial-contaminant composition or auto-replace source identity merely
    from hierarchy. Preserve original membership/count semantics and lifecycle; removing
    a false parent alone does not resolve this finding.
  finding_ids:
  - F2
  target_ids:
  - ENVO:03600002
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: ITEM assessment of exact GOLD source concept
  - repository: culturebotai/HabitatMech
    path: curation/term_requests.tsv
    role: Only evidence-supported identity and genus
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Use exact source identifiers and inspected primary evidence; do not invent a replacement
    or infer ecological absence.
  - Preserve counts/units, source provenance and immutable reviews. Append native
    history for curation.
  - Add a focused regression, dry seed, inspect a canary, regenerate affected products
    and pass strict, history, provenance, label, corpus and full QC gates.
limitations:
- Original frozen source intent is not reconstructed from later GOLD members.
- Same agent authored and checked the correction; no independent approval is claimed.
- 'No SSSOM/KGX readiness certification; #1398 and the source-identity finding remain
  separate.'
related_reviews:
- repository: culturebotai/HabitatMech
  review_id: 20261011T082507Z-cooling_water
  relationship: Resolves only F1 and retains F2 as open after bounded correction
tags:
- habitatmech
- engineered
- record-review
- followup
```
