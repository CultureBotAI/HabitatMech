# Scoped publication follow-up: Sediment [sediment__79de4694]

- Review: 20261010T204528Z-sediment__79de4694-followup
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-10T20:32:20Z
- Finished UTC: 2026-10-10T20:45:28Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The guarded exclusion removes only the context parent habitatmech:GOLD.be4a7c95b6. The independently supported sediment genus, path-qualified identity, source node/path, frozen counts/units and NARROW/SEEDED status remain intact. F1 is resolved. F2 remains open under #1398: the attestation still uses an implicit ontology-parent comparison instead of its declared source-to-record endpoints.

## Scope And Provenance

Reassess this exact hierarchy correction and preservation of the source-qualified material; retain the unresolved mapping finding.

Selection: Scoped successor to one reviewed record; no additional unique-record coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ae4dfb2c7cafd63566b51d2721ba62922b1705ad.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.70845c6a72 | data/habitats/engineered/sediment__79de4694.yaml | generated | Sediment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Authoritative post-fix QC | passed | True | habitatmech:GOLD.70845c6a72 | 678 passed, 3 skipped in 501.82s (0:08:21); exact-commit CI run 38084148060 completed every quality gate. |
| Scoped correction regressions | passed | True | habitatmech:GOLD.70845c6a72 | 66 passed in 140.73s; full-corpus keyset, exact change scope, preserved fields and frozen counts/units asserted. |
| Exact corpus reproduction | passed | True | habitatmech:GOLD.70845c6a72 | 3208 expected/found; zero missing, extra or differing. |
| Ontology label correspondence | passed | True | habitatmech:GOLD.70845c6a72 | 1178 canonical, one synonym, five exceptions; 2057 rows without adapters are not covered. |
| Profile-bound semantic map | passed | True | habitatmech:GOLD.70845c6a72 | Full source-bound map and cache checked; input hash agrees with the reviewed local corpus. |

## Scientific And Domain Assessments

### Material versus context hierarchy

grounding: supported. Targets: habitatmech:GOLD.70845c6a72.

The exact source triad distinguishes sediment medium, pond local scale and aquaculture-farm broad scale. Later BioSample collection sites say shrimp-pond sediment. These mutually scoped annotations support retaining the sediment genus, not making sediment a subtype of the pond. The false context parent is now removed without replacing the material identity.

### Source identity, counts and generated ownership

provenance: supported. Targets: habitatmech:GOLD.70845c6a72.

All non-parent scientific fields are unchanged; the new history is correctly attributed. The corpus and semantic map reproduce from maintained inputs without a source merge or status promotion.

### Unresolved mapping endpoint contract

representation: concern. Targets: habitatmech:GOLD.70845c6a72.

The existing major F2 is still open. No SSSOM/KGX compatibility or whole-record unqualified approval follows from this bounded fix.

## Findings

### F1: Context Crustaceans pond is incorrectly asserted as a sediment genus

major / resolved / confirmed; issue key: gold-70845c6a72-context-parent.

The exact source triad distinguishes sediment medium, pond local scale and aquaculture-farm broad scale. Later BioSample collection sites say shrimp-pond sediment. These mutually scoped annotations support retaining the sediment genus, not making sediment a subtype of the pond. The disputed parent is habitatmech:GOLD.be4a7c95b6; retain ENVO:00002007 and the exact source mint.

Disposition: The guarded exclusion removes only the context parent habitatmech:GOLD.be4a7c95b6. The independently supported sediment genus, path-qualified identity, source node/path, frozen counts/units and NARROW/SEEDED status remain intact. F1 is resolved. F2 remains open under #1398: the attestation still uses an implicit ontology-parent comparison instead of its declared source-to-record endpoints.

### F2: Emitted mapping predicate uses endpoints different from its declared field

major / open / confirmed; issue key: gold-70845c6a72-mapping-endpoint-contract.

The exact source path keeps its own minted identity, yet the source-to-record field emits skos:narrowMatch from the narrower-than-ontology-leaf route. The implicit comparison is to ENVO:00002007, not to the documented generated record target. Reconcile shared #1398 across schema, generator and consumers.

## Recommended Actions And Acceptance Checks

### A2

Address existing #1398, distinguishing source-to-record identity and record-to-ontology-parent relations. No global predicate swap or invented exact merge.

- Make subject, predicate and object explicit and consistent across the schema, emitting routes and consumers.
- Regression-test retained minted, exact, broader and narrower routes without conflating context-qualified habitats.
- Audit actual SSSOM/KGX triples against current kg-microbe modeling before any product-readiness claim.
- Regenerate through maintained owners, append required history, verify exact reproduction and run full QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R1 | data/habitats/engineered/sediment__79de4694.yaml; Complete regenerated YAML, compared with the pre-curation record | supports | The guarded exclusion removes only the context parent habitatmech:GOLD.be4a7c95b6. The independently supported sediment genus, path-qualified identity, source node/path, frozen counts/units and NARROW/SEEDED status remain intact. F1 is resolved. F2 remains open under #1398: the attestation still uses an implicit ontology-parent comparison instead of its declared source-to-record endpoints. |
| M1 | curation/gold_parent_exclusions.tsv; Exact identifier and source_path row; linked history/mappings/sediment__79de4694 | supports | The maintained row pins the resolved context parent, source path, actor/date, primary-source interpretation and issue. The seeder removes only that GOLD contribution and appends one exclusion event. |
| N1 | docs/CURATION.md; Strictly broader parents, source-parent exclusions and native status rules | supports | Contextual containment is not is-a. A parent exclusion is not an ITEM identity decision, so it does not promote SEEDED to REVIEWED. |
| P1 | reviews/structured/20261010T200656Z-sediment__79de4694/review.yaml; Original complete target assessment and F1/F2, including hashed official OLS and GOLD source evidence | context_only | The exact source triad distinguishes sediment medium, pond local scale and aquaculture-farm broad scale. Later BioSample collection sites say shrimp-pond sediment. These mutually scoped annotations support retaining the sediment genus, not making sediment a subtype of the pond. Original ecological and frozen-member reconstruction limitations remain. This successor assesses the exact correction, not a new source-wide census. |
| G1 | src/habitatmech/seed.py; src/habitatmech/schema/habitatmech.yaml; resolve_gold narrower-than-leaf route; SourceAttestation.mapping_predicate; regenerated attestation | supports | The mint is retained and sediment is a parent, but narrowMatch is still emitted on a field documented as source concept to record identifier. The hierarchy change does not fix this different endpoint contract. |
| I1 | https://github.com/CultureBotAI/HabitatMech/issues/1398; OPEN issue and witness comment for PR #1880 | supports | This shared defect remains tracked without a duplicate issue or a global broad/narrow predicate swap. |
| V1 | https://github.com/CultureBotAI/HabitatMech/actions/runs/38084148060; Authoritative QC on product commit ae4dfb2c7cafd63566b51d2721ba62922b1705ad | supports | 678 passed, 3 skipped in 501.82s (0:08:21); all native quality gates passed. |
| V2 | tests/test_engineered_sediment_review_fixes.py; Full-corpus before/after comparison plus per-target frozen-inventory assertions and existing exclusion tests | supports | 66 focused tests passed in 140.73s. Exactly 15 of 3208 records change only in parent_habitats and one exclusion event; all identities and unrelated fields are preserved. Sediment microcosm is unchanged. |
| V3 | https://github.com/CultureBotAI/HabitatMech/actions/runs/38083767295; Locked Linux map build, repeated canary, full cache check and local/remote input comparison | supports | The 15 changed semantic inputs were re-encoded with the unchanged locked profile. The repeat canary reused 15; the full pass reused 3208. Full inputs match SHA256 c30c03f52fc6cef22ded05fb8fe22b2b47f34511f1bf3561e596807c7f330a68; every plotted ID is unique and coordinates are finite. |

## Limits And Additional Notes

- Scoped self-review of the authored correction, not independent approval or a new exhaustive ecological review.
- Full QC evidence is from the exact-commit Linux CI run, not a claimed local full-QC completion.
- Original frozen-member reconstruction was unavailable at configured paths and wider searches were permission-limited in the predecessor; it was not repeated or replaced with later source counts.
- The automatic label gate leaves 2057 rows without adapters; skipped tests are not passes.
- The shared mapping endpoint issue #1398 remains open. No SSSOM/KGX readiness or corpus-wide scientific certification is asserted.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T204528Z-sediment__79de4694-followup
kind: record
repository: culturebotai/HabitatMech
title: 'Scoped publication follow-up: Sediment [sediment__79de4694]'
started_at: '2026-10-10T20:32:20Z'
finished_at: '2026-10-10T20:45:28Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same continuing review agent; source and current-model checks
    were performed, but no independent reviewer is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'The guarded exclusion removes only the context parent habitatmech:GOLD.be4a7c95b6.
  The independently supported sediment genus, path-qualified identity, source node/path,
  frozen counts/units and NARROW/SEEDED status remain intact. F1 is resolved. F2 remains
  open under #1398: the attestation still uses an implicit ontology-parent comparison
  instead of its declared source-to-record endpoints.'
source:
  git_revision: ae4dfb2c7cafd63566b51d2721ba62922b1705ad
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
    sha256: 14eb020a26287751c86d1d6eab5c91cf606e0e8ea076832fce82e0646fb85cdd
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
    sha256: f7074c184c97b50d3d8b01c0c51cc813f7cf82a27cbda691fc58b3b854a59eba
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 051623b6783d4fd38b29701ac34c7fea091792b9285880a7eb60401cb6129b2c
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/samples/narrow-20260814.tsv
    sha256: 4d91c76ad5e0a46442075c7b9f882637130bacdfaedb25fbe7922f169d35051c
    role: context
  - path: curation/term_requests.tsv
    sha256: 9977e384b79128d6e89c85f28e35c77d29644d503dea6d53c12628599e33f7f3
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/engineered/crustaceans_pond.yaml
    sha256: e8042877b46366fdf61426376380dfab66447384d535e46778ce805d9e379698
    role: context
  - path: data/habitats/engineered/sediment__79de4694.yaml
    sha256: d25b61135df73a0172e2e9bdccdcfd373d05df996ccafac1c2a402ac30b57e9d
    role: target
  - path: data/habitats/terrestrial/sediment.yaml
    sha256: 850abac7c5b4cd5f033bd07f904cc8a6b4534ce8b38e94f6b99b7a3ac0f73147
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
  - path: data/text_map/current.json
    sha256: 18cd1f71a1b95db8cf62845c1d94bcf11dfc93b22b690ee97f9810a27c07a2c7
    role: context
  - path: data/text_map/d2b69f8f944df7e41e09d49431bda1a3473bd2d2ea5cd2e0bdc4908d87970ba0/index.html
    sha256: bad56d889d08c1dfe1dffdd9b42e151acd993382b77dabd7725753ef942606c9
    role: context
  - path: data/text_map/d2b69f8f944df7e41e09d49431bda1a3473bd2d2ea5cd2e0bdc4908d87970ba0/manifest.json
    sha256: f97840b4ad17902c99fff42539f794525610b044bddd20e1994637f5001975c1
    role: context
  - path: data/text_map/d2b69f8f944df7e41e09d49431bda1a3473bd2d2ea5cd2e0bdc4908d87970ba0/points.json
    sha256: c90bde44538dfa2cef562fc4f9233e96d18fcaa3bf3d55f065913fcea62af738
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
  - path: history/mappings/sediment__79de4694/2026-10-10T202511Z-codex-gpt-5-74b4ea.yaml
    sha256: 5ba6ec59efb73a11ec0f71027bda331f7460908b468fb59b2a52c419cc1e3ce9
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260924T211056Z-sediment__79de4694.md
    sha256: 2f278050421c8d193d27b034837a7e782cdd982272db8f4bf9286df136ceb523
    role: context
  - path: reviews/structured/20261010T200656Z-sediment__79de4694/review.yaml
    sha256: ceacf5fdd8e5a0d2a7cb725b02cb8199fbd200b7eb7a53cfafebfa120e52bc71
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
    role: context
  - path: scripts/extract_source_inventory.py
    sha256: 4bf5391d25ff48a2d81eb3821af6582de063fd0391440973d309dfd93016490c
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 52d2a22309a1f4a10728a663560bb4d918346c292221fd34139b99b4159d3fe5
    role: context
  - path: src/habitatmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/habitatmech/seed.py
    sha256: 92adf631fa099120a497ff7001473e659347d23ac9b418f04cd341ddad5d2a89
    role: context
  - path: tests/test_engineered_sediment_review_fixes.py
    sha256: a60d3fcdb85f9842b7cad31cc0fa262cf41da8490800c36b3e1013701c70ff1d
    role: context
targets:
- target_id: habitatmech:GOLD.70845c6a72
  path: data/habitats/engineered/sediment__79de4694.yaml
  label: Sediment
  kind: generated
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: Item-level identity and broader-grounding decisions
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded source-context parent corrections
  - repository: culturebotai/HabitatMech
    path: curation/term_requests.tsv
    role: Authored habitat definition and genus
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen exact source paths, nodes and unit-specific counts
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained harmonization and generated record owner
scope:
  description: Reassess this exact hierarchy correction and preservation of the source-qualified
    material; retain the unresolved mapping finding.
  selection: Scoped successor to one reviewed record; no additional unique-record
    coverage.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.70845c6a72
checks:
- check_id: C1
  name: Authoritative post-fix QC
  command: uv run python scripts/run_qc.py
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.70845c6a72
  summary: 678 passed, 3 skipped in 501.82s (0:08:21); exact-commit CI run 38084148060
    completed every quality gate.
- check_id: C2
  name: Scoped correction regressions
  command: uv run pytest -q tests/test_engineered_sediment_review_fixes.py tests/test_gold_parent_exclusions.py
    tests/test_seawater_and_sediment_review_fixes.py
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.70845c6a72
  summary: 66 passed in 140.73s; full-corpus keyset, exact change scope, preserved
    fields and frozen counts/units asserted.
- check_id: C3
  name: Exact corpus reproduction
  command: just verify-corpus
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.70845c6a72
  summary: 3208 expected/found; zero missing, extra or differing.
- check_id: C4
  name: Ontology label correspondence
  command: just validate-products
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.70845c6a72
  summary: 1178 canonical, one synonym, five exceptions; 2057 rows without adapters
    are not covered.
- check_id: C5
  name: Profile-bound semantic map
  command: .venv/bin/python scripts/embedding_pipeline.py check --output build/pr1880-map-download/data/text_map
    --input build/text-map/pr1880-inputs.jsonl --cache build/pr1880-map-download/build/text-map/vectors.sqlite
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.70845c6a72
  summary: Full source-bound map and cache checked; input hash agrees with the reviewed
    local corpus.
evidence:
- evidence_id: R1
  kind: record_content
  reference: data/habitats/engineered/sediment__79de4694.yaml
  locator: Complete regenerated YAML, compared with the pre-curation record
  accessed_at: '2026-10-10T20:45:28Z'
  summary: 'The guarded exclusion removes only the context parent habitatmech:GOLD.be4a7c95b6.
    The independently supported sediment genus, path-qualified identity, source node/path,
    frozen counts/units and NARROW/SEEDED status remain intact. F1 is resolved. F2
    remains open under #1398: the attestation still uses an implicit ontology-parent
    comparison instead of its declared source-to-record endpoints.'
  support: supports
- evidence_id: M1
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact identifier and source_path row; linked history/mappings/sediment__79de4694
  accessed_at: '2026-10-10T20:45:28Z'
  summary: The maintained row pins the resolved context parent, source path, actor/date,
    primary-source interpretation and issue. The seeder removes only that GOLD contribution
    and appends one exclusion event.
  support: supports
- evidence_id: N1
  kind: authority
  reference: docs/CURATION.md
  locator: Strictly broader parents, source-parent exclusions and native status rules
  accessed_at: '2026-10-10T20:45:28Z'
  summary: Contextual containment is not is-a. A parent exclusion is not an ITEM identity
    decision, so it does not promote SEEDED to REVIEWED.
  support: supports
- evidence_id: P1
  kind: prior_review
  reference: reviews/structured/20261010T200656Z-sediment__79de4694/review.yaml
  locator: Original complete target assessment and F1/F2, including hashed official
    OLS and GOLD source evidence
  accessed_at: '2026-10-10T20:45:28Z'
  summary: The exact source triad distinguishes sediment medium, pond local scale
    and aquaculture-farm broad scale. Later BioSample collection sites say shrimp-pond
    sediment. These mutually scoped annotations support retaining the sediment genus,
    not making sediment a subtype of the pond. Original ecological and frozen-member
    reconstruction limitations remain. This successor assesses the exact correction,
    not a new source-wide census.
  support: context_only
- evidence_id: G1
  kind: record_content
  reference: src/habitatmech/seed.py; src/habitatmech/schema/habitatmech.yaml
  locator: resolve_gold narrower-than-leaf route; SourceAttestation.mapping_predicate;
    regenerated attestation
  accessed_at: '2026-10-10T20:45:28Z'
  summary: The mint is retained and sediment is a parent, but narrowMatch is still
    emitted on a field documented as source concept to record identifier. The hierarchy
    change does not fix this different endpoint contract.
  support: supports
- evidence_id: I1
  kind: database
  reference: https://github.com/CultureBotAI/HabitatMech/issues/1398
  locator: 'OPEN issue and witness comment for PR #1880'
  accessed_at: '2026-10-10T20:45:28Z'
  summary: This shared defect remains tracked without a duplicate issue or a global
    broad/narrow predicate swap.
  support: supports
- evidence_id: V1
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38084148060
  locator: Authoritative QC on product commit ae4dfb2c7cafd63566b51d2721ba62922b1705ad
  accessed_at: '2026-10-10T20:45:28Z'
  summary: 678 passed, 3 skipped in 501.82s (0:08:21); all native quality gates passed.
  support: supports
- evidence_id: V2
  kind: validation
  reference: tests/test_engineered_sediment_review_fixes.py
  locator: Full-corpus before/after comparison plus per-target frozen-inventory assertions
    and existing exclusion tests
  accessed_at: '2026-10-10T20:45:28Z'
  summary: 66 focused tests passed in 140.73s. Exactly 15 of 3208 records change only
    in parent_habitats and one exclusion event; all identities and unrelated fields
    are preserved. Sediment microcosm is unchanged.
  support: supports
- evidence_id: V3
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38083767295
  locator: Locked Linux map build, repeated canary, full cache check and local/remote
    input comparison
  accessed_at: '2026-10-10T20:45:28Z'
  summary: The 15 changed semantic inputs were re-encoded with the unchanged locked
    profile. The repeat canary reused 15; the full pass reused 3208. Full inputs match
    SHA256 c30c03f52fc6cef22ded05fb8fe22b2b47f34511f1bf3561e596807c7f330a68; every
    plotted ID is unique and coordinates are finite.
  support: supports
assessments:
- assessment_id: A1
  area: grounding
  topic: Material versus context hierarchy
  outcome: supported
  target_ids:
  - habitatmech:GOLD.70845c6a72
  evidence_ids:
  - R1
  - M1
  - N1
  - P1
  summary: The exact source triad distinguishes sediment medium, pond local scale
    and aquaculture-farm broad scale. Later BioSample collection sites say shrimp-pond
    sediment. These mutually scoped annotations support retaining the sediment genus,
    not making sediment a subtype of the pond. The false context parent is now removed
    without replacing the material identity.
- assessment_id: A2
  area: provenance
  topic: Source identity, counts and generated ownership
  outcome: supported
  target_ids:
  - habitatmech:GOLD.70845c6a72
  evidence_ids:
  - R1
  - M1
  - V1
  - V2
  - V3
  summary: All non-parent scientific fields are unchanged; the new history is correctly
    attributed. The corpus and semantic map reproduce from maintained inputs without
    a source merge or status promotion.
- assessment_id: A3
  area: representation
  topic: Unresolved mapping endpoint contract
  outcome: concern
  target_ids:
  - habitatmech:GOLD.70845c6a72
  evidence_ids:
  - R1
  - G1
  - I1
  - P1
  summary: The existing major F2 is still open. No SSSOM/KGX compatibility or whole-record
    unqualified approval follows from this bounded fix.
findings:
- finding_id: F1
  issue_key: gold-70845c6a72-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Context Crustaceans pond is incorrectly asserted as a sediment genus
  description: The exact source triad distinguishes sediment medium, pond local scale
    and aquaculture-farm broad scale. Later BioSample collection sites say shrimp-pond
    sediment. These mutually scoped annotations support retaining the sediment genus,
    not making sediment a subtype of the pond. The disputed parent is habitatmech:GOLD.be4a7c95b6;
    retain ENVO:00002007 and the exact source mint.
  target_ids:
  - habitatmech:GOLD.70845c6a72
  field_paths:
  - parent_habitats
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded exclusion of this immediate GOLD context-parent contribution
  evidence_ids:
  - R1
  - M1
  - N1
  - P1
  - V1
  - V2
  rule_id: HabitatMech:strictly-broader-parents
  native_severity: major
  normalization_reason: A context-only edge asserts the wrong material-versus-setting
    hierarchy, not merely incomplete optional curation.
  previous_occurrences:
  - repository: culturebotai/HabitatMech
    review_id: 20261010T200656Z-sediment__79de4694
    finding_id: F1
  disposition_reason: 'The guarded exclusion removes only the context parent habitatmech:GOLD.be4a7c95b6.
    The independently supported sediment genus, path-qualified identity, source node/path,
    frozen counts/units and NARROW/SEEDED status remain intact. F1 is resolved. F2
    remains open under #1398: the attestation still uses an implicit ontology-parent
    comparison instead of its declared source-to-record endpoints.'
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1877
- finding_id: F2
  issue_key: gold-70845c6a72-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Emitted mapping predicate uses endpoints different from its declared field
  description: 'The exact source path keeps its own minted identity, yet the source-to-record
    field emits skos:narrowMatch from the narrower-than-ontology-leaf route. The implicit
    comparison is to ENVO:00002007, not to the documented generated record target.
    Reconcile shared #1398 across schema, generator and consumers.'
  target_ids:
  - habitatmech:GOLD.70845c6a72
  field_paths:
  - source_attestations[0].mapping_predicate
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Shared endpoint contract and emitting-route owner
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Shared endpoint contract and emitting-route owner
  evidence_ids:
  - R1
  - G1
  - I1
  - P1
  rule_id: HabitatMech:source-attestation-mapping-endpoints
  native_severity: major
  normalization_reason: The shared generator emits a semantic relation with the wrong
    declared endpoints.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
  previous_occurrences:
  - repository: culturebotai/HabitatMech
    review_id: 20261010T200656Z-sediment__79de4694
    finding_id: F2
actions:
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.70845c6a72
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Shared endpoint contract and emitting-route owner
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Shared endpoint contract and emitting-route owner
  description: 'Address existing #1398, distinguishing source-to-record identity and
    record-to-ontology-parent relations. No global predicate swap or invented exact
    merge.'
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Make subject, predicate and object explicit and consistent across the schema,
    emitting routes and consumers.
  - Regression-test retained minted, exact, broader and narrower routes without conflating
    context-qualified habitats.
  - Audit actual SSSOM/KGX triples against current kg-microbe modeling before any
    product-readiness claim.
  - Regenerate through maintained owners, append required history, verify exact reproduction
    and run full QC.
limitations:
- Scoped self-review of the authored correction, not independent approval or a new
  exhaustive ecological review.
- Full QC evidence is from the exact-commit Linux CI run, not a claimed local full-QC
  completion.
- Original frozen-member reconstruction was unavailable at configured paths and wider
  searches were permission-limited in the predecessor; it was not repeated or replaced
  with later source counts.
- The automatic label gate leaves 2057 rows without adapters; skipped tests are not
  passes.
- 'The shared mapping endpoint issue #1398 remains open. No SSSOM/KGX readiness or
  corpus-wide scientific certification is asserted.'
related_reviews:
- repository: culturebotai/HabitatMech
  review_id: 20261010T200656Z-sediment__79de4694
  relationship: Scoped successor preserving exact finding lineage and original evidence
    limitations.
```
