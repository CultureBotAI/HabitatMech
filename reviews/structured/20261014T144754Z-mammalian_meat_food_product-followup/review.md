# Scientific follow-up: mammalian meat food product

- Review: 20261014T144754Z-mammalian_meat_food_product-followup
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T14:09:50.020317Z
- Finished UTC: 2026-10-14T14:47:54.344047Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact GOLD production-process parent is excluded, preserving the two independent FoodOn material genera and 1916 ORGANISM assertions. The generic GOLD Meat products identity remains conflated with mammalian meat in #2078. No original poultry/fish membership has been recovered, and no child or identity migration is implied.

## Scope And Provenance

Complete corrected record and every exact predecessor finding.

Selection: Explicit correction follow-up; one target, not sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0b2b8d8119cf4f4244b1a15a8b5ed6e551ee6700.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| FOODON:00001006 | data/habitats/food/mammalian_meat_food_product.yaml | generated | mammalian meat food product |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate | passed | True | FOODON:00001006 | Executed 2026-10-14T14:26:40.963226Z to 2026-10-14T14:26:42.985309Z. No issues found |
| just validate-strict | passed | True | FOODON:00001006 | Executed 2026-10-14T14:26:42.985836Z to 2026-10-14T14:26:47.005086Z. uv run python scripts/validate_strict.py data/habitats/other/fruit_seed.yaml data/habitats/food/heroin.yaml data/habitats/food/juice.yaml data/habitats/food/mammalian_meat_food_product.yaml<br>Validating 4 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      4<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | FOODON:00001006 | Executed 2026-10-14T14:26:47.005578Z to 2026-10-14T14:26:53.671960Z. No issues found<br>674 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | FOODON:00001006 | Executed 2026-10-14T14:26:53.672443Z to 2026-10-14T14:26:54.189202Z. provenance current: 14 committed inventories, 2 GOLD sources |
| just verify-corpus | passed | True | FOODON:00001006 | Executed 2026-10-14T14:26:54.189792Z to 2026-10-14T14:27:11.391632Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| just validate-causal-all | passed | True | FOODON:00001006 | Executed 2026-10-14T14:27:11.392501Z to 2026-10-14T14:27:15.661509Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| just term-requests-check | passed | True | FOODON:00001006 | Executed 2026-10-14T14:27:15.662003Z to 2026-10-14T14:27:32.982214Z. term-request table is current (109 terms) |
| just validate-products | passed | True | FOODON:00001006 | Executed 2026-10-14T14:27:32.982781Z to 2026-10-14T14:28:18.433805Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1176<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2059<br><br>✅ All id↔label pairs correspond. |
| uv run | passed | True | FOODON:00001006 | Executed 2026-10-14T14:28:18.434497Z to 2026-10-14T14:30:12.582977Z. ........................................................................ [ 80%]<br>.................                                                        [100%]<br>89 passed in 113.20s (0:01:53) |
| uv run | passed | True | FOODON:00001006 | Executed 2026-10-14T14:30:12.583516Z to 2026-10-14T14:30:12.817237Z. All checks passed! |
| Exact corrected-base authoritative QC | passed | True | FOODON:00001006 | Exact corrected base verified; new review archive is separate. |
| Original source member reconstruction | unavailable | False | FOODON:00001006 | Original joins were unavailable in the recorded bounded predecessor search and were not recovered during this correction. Target-specific GOLD access limitations, where applicable, are retained in evidence rather than attributed to every target. |
| Expression-module applicability | not_applicable | False | FOODON:00001006 | No gene, regulator, protein or transcriptomic mechanism is asserted. |
| Broader local regression suite | passed | True | FOODON:00001006 | 1107 passed, 3 skipped in 807.53 seconds. Archive/publication modules were explicitly excluded here and are covered by their separate native/hosted gates; this is not a claim that all tests ran in this command. |

## Scientific And Domain Assessments

### Exact correction and immutable finding lineage

grounding: supported. Targets: FOODON:00001006.

The exact GOLD production-process parent is excluded, preserving the two independent FoodOn material genera and 1916 ORGANISM assertions. The generic GOLD Meat products identity remains conflated with mammalian meat in #2078. No original poultry/fish membership has been recovered, and no child or identity migration is implied.

### Source evidence, native status and optional assertions

provenance: concern. Targets: FOODON:00001006.

Complete record re-read. Source identifiers, paths, counts/units and taxon associations remain unchanged; no characteristic-presence, environmental parameter or causal claim is added. Preserved native REVIEWED/SEEDED status is not a new scientific endorsement. Unresolved predecessor findings remain explicitly open.

### Original membership and identity detail

completeness: unknown. Targets: FOODON:00001006.

Current source examples do not reconstruct the unavailable frozen joins. OTHER on Fruit-Seed is a conservative bucket, not a defined new genus. No complete ontology-equivalence search, neighboring-record closure, whole-corpus pass or SSSOM/KGX readiness is claimed.

## Findings

### F1: Acknowledged narrower term is adopted as the source identity

major / open / confirmed; issue key: mammalian-meat-gold-source-identity.

The maintained decision explicitly says mammalian meat is narrower than GOLD Meat products but still uses GROUND. The generator substitutes the mammalian identifier and emits Meat products as an exact synonym. Neither the NARROW annotation nor best-available-term rationale establishes coextensiveness. Original poultry/fish membership has not been independently verified; the confirmed defect is the unsupported identity and internal scope conflict.

Disposition: The bounded correction does not resolve the distinct source-identity/category defect. The exact GOLD production-process parent is excluded, preserving the two independent FoodOn material genera and 1916 ORGANISM assertions. The generic GOLD Meat products identity remains conflated with mammalian meat in #2078. No original poultry/fish membership has been recovered, and no child or identity migration is implied.

### F2: Food production process is not a meat-material genus

major / resolved / confirmed; issue key: mammalian-meat-food-production-process-parent.

The added FOODON:03530206 parent is a planned process, unlike the two independently supported material ontology parents. It is a GOLD classification context contribution, not a strict material superclass.

Disposition: Exact maintained-input correction and regenerated claims verified. The exact GOLD production-process parent is excluded, preserving the two independent FoodOn material genera and 1916 ORGANISM assertions. The generic GOLD Meat products identity remains conflated with mammalian meat in #2078. No original poultry/fish membership has been recovered, and no child or identity migration is implied.

## Recommended Actions And Acceptance Checks

### A1

Reassess mint habitatmech:GOLD.0347e0d978 and retain its native generic scope unless an actual exact identity is verified. A narrower mammalian class cannot be its broader parent. Audit Raw meat and butchery-cut children plus the two expected-parent exclusions for Cooked meat/Fermented meat products. Preserve all original counts and do not assume source-member species from a note.

- Edit maintained decisions or exact guarded overlays only; preserve frozen raw inventories and never hand-edit generated records.
- Preserve source identifiers, source paths, count units, taxon metrics and honest native status unless separately evidence-backed.
- Dry seed, inspect target canary and full before/after corpus delta; run schema, strict, history, provenance, corpus, site, label and authoritative QC gates.
- Save a new immutable follow-up with this stable issue key and exact previous occurrence; do not rewrite this report.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| CURRENT | data/habitats/food/mammalian_meat_food_product.yaml | supports | Complete corrected record and predecessor diff read. The exact GOLD production-process parent is excluded, preserving the two independent FoodOn material genera and 1916 ORGANISM assertions. The generic GOLD Meat products identity remains conflated with mammalian meat in #2078. No original poultry/fish membership has been recovered, and no child or identity migration is implied. |
| OWNERS | curation/decisions.tsv; curation/gold_parent_exclusions.tsv; history/mappings/ | supports | Read exact maintained rows and four append-only session histories. Only Fruit-Seed changes its grounding/category; the three parent exclusions preserve all other claims. Raw inventories and manifests are unchanged. Generated curation history is a deterministic current-input projection; immutable historical reviews/session records remain untouched. |
| REGRESSION | tests/test_juice_meat_fruit_review_fixes.py; tests/test_ontology_labels.py | supports | Counterfactual full-corpus build proves exactly four changed identifiers. Three change only parent/history. Fruit-Seed also loses the unsupported narrowMatch and FOOD category, preserving all source IDs/counts/units and taxon metrics. The older label-refresh test was corrected to reject the false juice-to-beverage parent while retaining GOLD context/count/unit. All focused test results are recorded below; this extra test input was inspected at final capture. |
| PREVIOUS | reviews/structured/20261014T135505Z-mammalian_meat_food_product/review.yaml | context_only | Entire immutable predecessor inspected. Old parent/category values and input row numbers are historical, not current values. Evidence limitations are retained. |
| QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38580565321 | supports | Exact corrected-base authoritative hosted QC passed at 0b2b8d8119cf4f4244b1a15a8b5ed6e551ee6700. New successor bundles still require archive/final-head checks. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; src/habitatmech/schema/habitatmech.yaml | supports | Retained inspected source evidence, not a new retrieval or current-record annotation. Native exact identity, strict superclass, source-unit, MIxS-role, optional-field and all-source ITEM rules applied. FOOD is a coarse layout/reporting bucket for food and beverage matrices, not an identity axiom. |
| MEMBERS | conf/sources.yaml; data/raw/MANIFEST.yaml; data/raw/GOLD_MANIFEST.yaml | supports | Retained inspected source evidence, not a new retrieval or current-record annotation. Original GOLD nodes/edges, BacDive and PREGO nodes/edges, goldData.xlsx and gold_biosample_triads.tsv were not located by named-file enumeration of 39439 files under /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data. Ignored/hidden files included; .git internals excluded and symlinks not traversed. Frozen inventories remain available. No global absence or exact frozen member reconstruction is claimed. |
| GOLD_ACCESS | https://gold.jgi.doe.gov/ | context_only | Retained inspected source evidence, not a new retrieval or current-record annotation. Requested exact study pages Gs0111409, Gs0127406, Gs0133016, Gs0150353, Gs0150522, Gs0150710, Gs0154236, Gs0154282; each returned HTTP403. No page text inferred. {"Gs0111409": {"url": "https://gold.jgi.doe.gov/study?id=Gs0111409", "accessed_at": "2026-10-14T13:45:40.887238Z", "error": "HTTP Error 403: Forbidden"}, "Gs0127406": {"url": "https://gold.jgi.doe.gov/study?id=Gs0127406", "accessed_at": "2026-10-14T13:45:41.046759Z", "error": "HTTP Error 403: Forbidden"}, "Gs0133016": {"url": "https://gold.jgi.doe.gov/study?id=Gs0133016", "accessed_at": "2026-10-14T13:45:40.970490Z", "error": "HTTP Error 403: Forbidden"}, "Gs0150353": {"url": "https://gold.jgi.doe.gov/study?id=Gs0150353", "accessed_at": "2026-10-14T13:45:40.808981Z", "error": "HTTP Error 403: Forbidden"}, "Gs0150522": {"url": "https://gold.jgi.doe.gov/study?id=Gs0150522", "accessed_at": "2026-10-14T13:45:40.846257Z", "error": "HTTP Error 403: Forbidden"}, "Gs0150710": {"url": "https://gold.jgi.doe.gov/study?id=Gs0150710", "accessed_at": "2026-10-14T13:45:40.925115Z", "error": "HTTP Error 403: Forbidden"}, "Gs0154236": {"url": "https://gold.jgi.doe.gov/study?id=Gs0154236", "accessed_at": "2026-10-14T13:45:40.727234Z", "error": "HTTP Error 403: Forbidden"}, "Gs0154282": {"url": "https://gold.jgi.doe.gov/study?id=Gs0154282", "accessed_at": "2026-10-14T13:45:41.014612Z", "error": "HTTP Error 403: Forbidden"}} |
| FOODON | https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl | supports | Retained inspected source evidence, not a new retrieval or current-record annotation. Full pinned RDF/XML class definitions, synonym predicates, named parents and restrictions re-inspected at 2026-10-14T13:45:26.271013Z. FOODON:00001092 and FOODON:00005501 are valid named ontology parents of mammalian meat. FOODON:03530206 is instead a process introduced by the GOLD branch. A source remap must audit the two remaining direct record children and two exact expected-parent exclusion guards; no original poultry/fish members are asserted by this review. Retrieved bytes SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf. |

## Limits And Additional Notes

- Same-agent assessment, not independent approval.
- Original joins remain unavailable; positive current examples do not reconstruct frozen membership.
- Issues #2075/#2076/#2078/#2080/#2081 remain open; four bounded repairs do not resolve them.
- Corrected-base QC predates the new successor bundles; final archive and publication checks are separate.
- No native status promotion, full ontology refresh, or SSSOM/KGX certification.
- Initial corrected-input capture 2026-10-14T14:09:50.020317Z; final inspection confirmed all captured input bytes unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T144754Z-mammalian_meat_food_product-followup
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific follow-up: mammalian meat food product'
started_at: '2026-10-14T14:09:50.020317Z'
finished_at: '2026-10-14T14:47:54.344047Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent has participated in HabitatMech curation and publication;
    not independent approval.
skill: .claude/skills/curate-yaml-record/SKILL.md
completion: completed
scientific_review: true
verdict: needs_curation
summary: 'The exact GOLD production-process parent is excluded, preserving the two
  independent FoodOn material genera and 1916 ORGANISM assertions. The generic GOLD
  Meat products identity remains conflated with mammalian meat in #2078. No original
  poultry/fish membership has been recovered, and no child or identity migration is
  implied.'
source:
  git_revision: 0b2b8d8119cf4f4244b1a15a8b5ed6e551ee6700
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
    sha256: 927e6d2c66b371c80639059b70665d0069e7a03ac32ed1620b94b36da289a982
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 9106572cbc553bc7da1a40eff8e0d3aa861003feb8ce0b93eb11cf5526dde1c2
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: 5142ff999a3111139f88bca11dab485b18b01773a52f43ae9557239eb2029210
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
    sha256: 3781420be8a7a6de4f44c9be1bc3a0d256824fb44b8dbbb56c6b3c99e21a6014
    role: context
  - path: data/habitats/food/beverage.yaml
    sha256: b5d70ad5849c891fd01efe9f27abe3e6df8a74abc70fc212482dcdc61c842003
    role: context
  - path: data/habitats/food/butchery_cut_of_beef.yaml
    sha256: 837d45cc3f7fb377199b254fffe21a366d1312b13e5fd2232b987c136ffc33bb
    role: context
  - path: data/habitats/food/dairy_food_product.yaml
    sha256: 36c6b5dde12d0d75eca04ac0f91200e839763e14e2ff813ebb85fb7242fb3001
    role: context
  - path: data/habitats/food/food_production.yaml
    sha256: b0fce7af2cc321a0979ce4d3bfec5e2d4383410ae8e62172b006073afb783ab7
    role: context
  - path: data/habitats/food/frozen_seafood.yaml
    sha256: 93677d5139e32554b0263678305c5cf15151268a9374ed5e0332a15241420e8c
    role: context
  - path: data/habitats/food/mammalian_meat_food_product.yaml
    sha256: 5297b7ec6ffa54a867f9b9a4485fb539f15085e0495e1299bbc4145c238fff49
    role: target
  - path: data/habitats/food/morphine.yaml
    sha256: a1f55ea3d879d5f3f83f7433700fe238539e5ac408ac1cd86c79503178d61eee
    role: context
  - path: data/habitats/food/plant_products.yaml
    sha256: 84f11abc0ccc2a67ac560189589126c2ab43fe1d0e9655280f5424fc30d2e018
    role: context
  - path: data/habitats/food/raw_meat.yaml
    sha256: e45e1d71102c32bc410ff08a2175fcd645de883da0d4682f8acfaf0b04b0564d
    role: context
  - path: data/habitats/host_associated/fruit_juice.yaml
    sha256: 1ae7408229392df98be954513b3a820c24d5d39c486f3aae00f59816e2faa439
    role: context
  - path: data/habitats/other/juice_natural.yaml
    sha256: d6dfcee1e355e5673087a1ab439db05b0f655d639c62284a33899ae7aa9db1f5
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
  - path: history/mappings/fruit_seed/2026-10-14T140509Z-codex-gpt-5-e9c6b7.yaml
    sha256: b0c9d43627771cdb1f834a978644481a2ec2541b34c51db167b22e0246430a5e
    role: context
  - path: history/mappings/heroin/2026-10-14T140510Z-codex-gpt-5-4711d8.yaml
    sha256: d456e0f7d8da8e3b651d6b32b6f8edd43676c14c21be2b3cc3ce4d7a7ade1172
    role: context
  - path: history/mappings/juice/2026-10-14T140511Z-codex-gpt-5-a53c87.yaml
    sha256: cf771a4744be8aac62f3900d4b3e0de4bc222bad7cccd8cffcf3768dce186aeb
    role: context
  - path: history/mappings/mammalian_meat_food_product/2026-10-14T140512Z-codex-gpt-5-cbae1f.yaml
    sha256: 084c8dbcf0c467e537d351a13b6f9ab349be7677044a72bd79caeecbdd785a6e
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reviews/structured/20261014T135505Z-mammalian_meat_food_product/review.yaml
    sha256: b769bc19d273313e7430d7ca53085ac93cd86b3c8eed8e539dfe7ab258181d8d
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/aggregate_gold_triads.py
    sha256: 0e25179dbecd7c73cbedd99a0ae44e56e4992afb9e1ec02d2411439f643b8e54
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
    role: context
  - path: src/habitatmech/curate/decisions.py
    sha256: f33d3e9dc95bb428e63e640d48d4074cf15e90ea666603fb16fb651d591e3f02
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
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
  - path: tests/test_food_material_review_fixes.py
    sha256: b9dad3c1c27d037dd40450f4e081381bc3d9860243d661e4e7cdc48b759d64ae
    role: context
  - path: tests/test_juice_meat_fruit_review_fixes.py
    sha256: 5d8a303d069a4426ad1ce49931150ac5bd83ec87c1e208f0ba3052bfb094dd41
    role: context
  - path: tests/test_ontology_labels.py
    sha256: fd2017bfacac10f43c2ef7d4570367d7b7c24ba997bad1b5c36436df7aa4cace
    role: context
targets:
- target_id: FOODON:00001006
  path: data/habitats/food/mammalian_meat_food_product.yaml
  label: mammalian meat food product
  kind: generated
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained owner; generated habitat YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained owner; generated habitat YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained owner; generated habitat YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained owner; generated habitat YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Maintained owner; generated habitat YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_path_biosamples.tsv
    role: Maintained owner; generated habitat YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_path_triads.tsv
    role: Maintained owner; generated habitat YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_studies.tsv
    role: Maintained owner; generated habitat YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Maintained owner; generated habitat YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Maintained owner; generated habitat YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained owner; generated habitat YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained owner; generated habitat YAML is read-only
scope:
  description: Complete corrected record and every exact predecessor finding.
  selection: Explicit correction follow-up; one target, not sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - FOODON:00001006
evidence:
- evidence_id: CURRENT
  kind: record_content
  reference: data/habitats/food/mammalian_meat_food_product.yaml
  summary: 'Complete corrected record and predecessor diff read. The exact GOLD production-process
    parent is excluded, preserving the two independent FoodOn material genera and
    1916 ORGANISM assertions. The generic GOLD Meat products identity remains conflated
    with mammalian meat in #2078. No original poultry/fish membership has been recovered,
    and no child or identity migration is implied.'
  accessed_at: '2026-10-14T14:47:54.343267Z'
  support: supports
- evidence_id: OWNERS
  kind: record_content
  reference: curation/decisions.tsv; curation/gold_parent_exclusions.tsv; history/mappings/
  summary: Read exact maintained rows and four append-only session histories. Only
    Fruit-Seed changes its grounding/category; the three parent exclusions preserve
    all other claims. Raw inventories and manifests are unchanged. Generated curation
    history is a deterministic current-input projection; immutable historical reviews/session
    records remain untouched.
  accessed_at: '2026-10-14T14:47:54.343293Z'
  support: supports
- evidence_id: REGRESSION
  kind: validation
  reference: tests/test_juice_meat_fruit_review_fixes.py; tests/test_ontology_labels.py
  summary: Counterfactual full-corpus build proves exactly four changed identifiers.
    Three change only parent/history. Fruit-Seed also loses the unsupported narrowMatch
    and FOOD category, preserving all source IDs/counts/units and taxon metrics. The
    older label-refresh test was corrected to reject the false juice-to-beverage parent
    while retaining GOLD context/count/unit. All focused test results are recorded
    below; this extra test input was inspected at final capture.
  accessed_at: '2026-10-14T14:47:54.343302Z'
  support: supports
- evidence_id: PREVIOUS
  kind: prior_review
  reference: reviews/structured/20261014T135505Z-mammalian_meat_food_product/review.yaml
  summary: Entire immutable predecessor inspected. Old parent/category values and
    input row numbers are historical, not current values. Evidence limitations are
    retained.
  accessed_at: '2026-10-14T14:47:54.343307Z'
  support: context_only
- evidence_id: QC
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38580565321
  summary: Exact corrected-base authoritative hosted QC passed at 0b2b8d8119cf4f4244b1a15a8b5ed6e551ee6700.
    New successor bundles still require archive/final-head checks.
  accessed_at: '2026-10-14T14:47:54.343310Z'
  support: supports
- evidence_id: RULES
  kind: authority
  reference: docs/CURATION.md; docs/HARMONIZATION.md; src/habitatmech/schema/habitatmech.yaml
  summary: Retained inspected source evidence, not a new retrieval or current-record
    annotation. Native exact identity, strict superclass, source-unit, MIxS-role,
    optional-field and all-source ITEM rules applied. FOOD is a coarse layout/reporting
    bucket for food and beverage matrices, not an identity axiom.
  accessed_at: '2026-10-14T13:55:05.702367Z'
  support: supports
- evidence_id: MEMBERS
  kind: search
  reference: conf/sources.yaml; data/raw/MANIFEST.yaml; data/raw/GOLD_MANIFEST.yaml
  summary: Retained inspected source evidence, not a new retrieval or current-record
    annotation. Original GOLD nodes/edges, BacDive and PREGO nodes/edges, goldData.xlsx
    and gold_biosample_triads.tsv were not located by named-file enumeration of 39439
    files under /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech;
    /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data. Ignored/hidden
    files included; .git internals excluded and symlinks not traversed. Frozen inventories
    remain available. No global absence or exact frozen member reconstruction is claimed.
  accessed_at: '2026-10-14T13:55:05.702501Z'
  support: supports
  search_scope: Ignored/hidden-inclusive structured parsing and rg within the explicitly
    named roots; not an all-disk absence claim.
- evidence_id: GOLD_ACCESS
  kind: database
  reference: https://gold.jgi.doe.gov/
  summary: 'Retained inspected source evidence, not a new retrieval or current-record
    annotation. Requested exact study pages Gs0111409, Gs0127406, Gs0133016, Gs0150353,
    Gs0150522, Gs0150710, Gs0154236, Gs0154282; each returned HTTP403. No page text
    inferred. {"Gs0111409": {"url": "https://gold.jgi.doe.gov/study?id=Gs0111409",
    "accessed_at": "2026-10-14T13:45:40.887238Z", "error": "HTTP Error 403: Forbidden"},
    "Gs0127406": {"url": "https://gold.jgi.doe.gov/study?id=Gs0127406", "accessed_at":
    "2026-10-14T13:45:41.046759Z", "error": "HTTP Error 403: Forbidden"}, "Gs0133016":
    {"url": "https://gold.jgi.doe.gov/study?id=Gs0133016", "accessed_at": "2026-10-14T13:45:40.970490Z",
    "error": "HTTP Error 403: Forbidden"}, "Gs0150353": {"url": "https://gold.jgi.doe.gov/study?id=Gs0150353",
    "accessed_at": "2026-10-14T13:45:40.808981Z", "error": "HTTP Error 403: Forbidden"},
    "Gs0150522": {"url": "https://gold.jgi.doe.gov/study?id=Gs0150522", "accessed_at":
    "2026-10-14T13:45:40.846257Z", "error": "HTTP Error 403: Forbidden"}, "Gs0150710":
    {"url": "https://gold.jgi.doe.gov/study?id=Gs0150710", "accessed_at": "2026-10-14T13:45:40.925115Z",
    "error": "HTTP Error 403: Forbidden"}, "Gs0154236": {"url": "https://gold.jgi.doe.gov/study?id=Gs0154236",
    "accessed_at": "2026-10-14T13:45:40.727234Z", "error": "HTTP Error 403: Forbidden"},
    "Gs0154282": {"url": "https://gold.jgi.doe.gov/study?id=Gs0154282", "accessed_at":
    "2026-10-14T13:45:41.014612Z", "error": "HTTP Error 403: Forbidden"}}'
  accessed_at: '2026-10-14T13:55:05.702581Z'
  support: context_only
- evidence_id: FOODON
  kind: database
  reference: https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl
  summary: Retained inspected source evidence, not a new retrieval or current-record
    annotation. Full pinned RDF/XML class definitions, synonym predicates, named parents
    and restrictions re-inspected at 2026-10-14T13:45:26.271013Z. FOODON:00001092
    and FOODON:00005501 are valid named ontology parents of mammalian meat. FOODON:03530206
    is instead a process introduced by the GOLD branch. A source remap must audit
    the two remaining direct record children and two exact expected-parent exclusion
    guards; no original poultry/fish members are asserted by this review. Retrieved
    bytes SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf.
  accessed_at: '2026-10-14T12:27:42.074174Z'
  support: supports
checks:
- check_id: C3
  name: just validate
  status: passed
  required: true
  target_ids:
  - FOODON:00001006
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/food/mammalian_meat_food_product.yaml
  exit_code: 0
  summary: Executed 2026-10-14T14:26:40.963226Z to 2026-10-14T14:26:42.985309Z. No
    issues found
- check_id: C4
  name: just validate-strict
  status: passed
  required: true
  target_ids:
  - FOODON:00001006
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/other/fruit_seed.yaml data/habitats/food/heroin.yaml data/habitats/food/juice.yaml
    data/habitats/food/mammalian_meat_food_product.yaml
  exit_code: 0
  summary: "Executed 2026-10-14T14:26:42.985836Z to 2026-10-14T14:26:47.005086Z. uv\
    \ run python scripts/validate_strict.py data/habitats/other/fruit_seed.yaml data/habitats/food/heroin.yaml\
    \ data/habitats/food/juice.yaml data/habitats/food/mammalian_meat_food_product.yaml\n\
    Validating 4 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      4\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
- check_id: C5
  name: just validate-history
  status: passed
  required: true
  target_ids:
  - FOODON:00001006
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  summary: 'Executed 2026-10-14T14:26:47.005578Z to 2026-10-14T14:26:53.671960Z. No
    issues found

    674 history record(s) valid against src/habitatmech/schema/history.yaml'
- check_id: C6
  name: just provenance-check
  status: passed
  required: true
  target_ids:
  - FOODON:00001006
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  summary: 'Executed 2026-10-14T14:26:53.672443Z to 2026-10-14T14:26:54.189202Z. provenance
    current: 14 committed inventories, 2 GOLD sources'
- check_id: C7
  name: just verify-corpus
  status: passed
  required: true
  target_ids:
  - FOODON:00001006
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  summary: "Executed 2026-10-14T14:26:54.189792Z to 2026-10-14T14:27:11.391632Z. expected\
    \ 3208 records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing:\
    \ 0\n\ncorpus reproduces exactly from data/raw/"
- check_id: C8
  name: just validate-causal-all
  status: passed
  required: true
  target_ids:
  - FOODON:00001006
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  summary: Executed 2026-10-14T14:27:11.392501Z to 2026-10-14T14:27:15.661509Z. validated
    32 causal-graph curation file(s) with 32 graph(s)
- check_id: C9
  name: just term-requests-check
  status: passed
  required: true
  target_ids:
  - FOODON:00001006
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  summary: Executed 2026-10-14T14:27:15.662003Z to 2026-10-14T14:27:32.982214Z. term-request
    table is current (109 terms)
- check_id: C10
  name: just validate-products
  status: passed
  required: true
  target_ids:
  - FOODON:00001006
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  summary: "Executed 2026-10-14T14:27:32.982781Z to 2026-10-14T14:28:18.433805Z. id↔label\
    \ correspondence summary:\n          OK_CANONICAL: 1176\n            OK_SYNONYM:\
    \ 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2059\n\n✅ All id↔label\
    \ pairs correspond."
- check_id: C11
  name: uv run
  status: passed
  required: true
  target_ids:
  - FOODON:00001006
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache uv run pytest -q tests/test_juice_meat_fruit_review_fixes.py
    tests/test_food_material_review_fixes.py tests/test_gold_parent_exclusions.py
    tests/test_curation_floor.py tests/test_ontology_labels.py
  exit_code: 0
  summary: 'Executed 2026-10-14T14:28:18.434497Z to 2026-10-14T14:30:12.582977Z. ........................................................................
    [ 80%]

    .................                                                        [100%]

    89 passed in 113.20s (0:01:53)'
- check_id: C12
  name: uv run
  status: passed
  required: true
  target_ids:
  - FOODON:00001006
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache uv run ruff check .
  exit_code: 0
  summary: Executed 2026-10-14T14:30:12.583516Z to 2026-10-14T14:30:12.817237Z. All
    checks passed!
- check_id: QC
  name: Exact corrected-base authoritative QC
  status: passed
  required: true
  target_ids:
  - FOODON:00001006
  command: gh run view 38580565321 --repo CultureBotAI/HabitatMech --json status,conclusion,headSha,url
  exit_code: 0
  summary: Exact corrected base verified; new review archive is separate.
  evidence_ids:
  - QC
- check_id: MEMBERS
  name: Original source member reconstruction
  status: unavailable
  required: false
  target_ids:
  - FOODON:00001006
  summary: Original joins were unavailable in the recorded bounded predecessor search
    and were not recovered during this correction. Target-specific GOLD access limitations,
    where applicable, are retained in evidence rather than attributed to every target.
  evidence_ids:
  - MEMBERS
- check_id: IMODULON
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - FOODON:00001006
  summary: No gene, regulator, protein or transcriptomic mechanism is asserted.
- check_id: BROAD_LOCAL
  name: Broader local regression suite
  status: passed
  required: true
  target_ids:
  - FOODON:00001006
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache uv run pytest -q --ignore=tests/test_record_review_contract.py
    --ignore=tests/test_record_review_publication.py
  exit_code: 0
  summary: 1107 passed, 3 skipped in 807.53 seconds. Archive/publication modules were
    explicitly excluded here and are covered by their separate native/hosted gates;
    this is not a claim that all tests ran in this command.
assessments:
- assessment_id: FIX
  area: grounding
  topic: Exact correction and immutable finding lineage
  outcome: supported
  target_ids:
  - FOODON:00001006
  evidence_ids:
  - CURRENT
  - OWNERS
  - REGRESSION
  - PREVIOUS
  - QC
  - RULES
  - MEMBERS
  - GOLD_ACCESS
  - FOODON
  summary: 'The exact GOLD production-process parent is excluded, preserving the two
    independent FoodOn material genera and 1916 ORGANISM assertions. The generic GOLD
    Meat products identity remains conflated with mammalian meat in #2078. No original
    poultry/fish membership has been recovered, and no child or identity migration
    is implied.'
- assessment_id: SOURCE
  area: provenance
  topic: Source evidence, native status and optional assertions
  outcome: concern
  target_ids:
  - FOODON:00001006
  evidence_ids:
  - CURRENT
  - OWNERS
  - REGRESSION
  - PREVIOUS
  - QC
  - RULES
  - MEMBERS
  - GOLD_ACCESS
  - FOODON
  summary: Complete record re-read. Source identifiers, paths, counts/units and taxon
    associations remain unchanged; no characteristic-presence, environmental parameter
    or causal claim is added. Preserved native REVIEWED/SEEDED status is not a new
    scientific endorsement. Unresolved predecessor findings remain explicitly open.
- assessment_id: LIMITS
  area: completeness
  topic: Original membership and identity detail
  outcome: unknown
  target_ids:
  - FOODON:00001006
  evidence_ids:
  - PREVIOUS
  - MEMBERS
  summary: Current source examples do not reconstruct the unavailable frozen joins.
    OTHER on Fruit-Seed is a conservative bucket, not a defined new genus. No complete
    ontology-equivalence search, neighboring-record closure, whole-corpus pass or
    SSSOM/KGX readiness is claimed.
findings:
- finding_id: F1
  issue_key: mammalian-meat-gold-source-identity
  title: Acknowledged narrower term is adopted as the source identity
  description: The maintained decision explicitly says mammalian meat is narrower
    than GOLD Meat products but still uses GROUND. The generator substitutes the mammalian
    identifier and emits Meat products as an exact synonym. Neither the NARROW annotation
    nor best-available-term rationale establishes coextensiveness. Original poultry/fish
    membership has not been independently verified; the confirmed defect is the unsupported
    identity and internal scope conflict.
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  target_ids:
  - FOODON:00001006
  field_paths:
  - identifier
  - definition
  - synonyms
  - source_attestations
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained owner; generated habitat YAML is read-only
  evidence_ids:
  - CURRENT
  - OWNERS
  - REGRESSION
  - PREVIOUS
  - QC
  - RULES
  - MEMBERS
  - GOLD_ACCESS
  - FOODON
  rule_id: Habitat identity, strict genus and source-specific scope
  native_severity: major
  normalization_reason: Unsupported identity equivalence or strict superclass materially
    changes the source meaning.
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261014T135505Z-mammalian_meat_food_product
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2078
  disposition_reason: 'The bounded correction does not resolve the distinct source-identity/category
    defect. The exact GOLD production-process parent is excluded, preserving the two
    independent FoodOn material genera and 1916 ORGANISM assertions. The generic GOLD
    Meat products identity remains conflated with mammalian meat in #2078. No original
    poultry/fish membership has been recovered, and no child or identity migration
    is implied.'
- finding_id: F2
  issue_key: mammalian-meat-food-production-process-parent
  title: Food production process is not a meat-material genus
  description: The added FOODON:03530206 parent is a planned process, unlike the two
    independently supported material ontology parents. It is a GOLD classification
    context contribution, not a strict material superclass.
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  target_ids:
  - FOODON:00001006
  field_paths:
  - parent_habitats
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained owner; generated habitat YAML is read-only
  evidence_ids:
  - CURRENT
  - OWNERS
  - REGRESSION
  - PREVIOUS
  - QC
  - RULES
  - MEMBERS
  - GOLD_ACCESS
  - FOODON
  rule_id: Habitat identity, strict genus and source-specific scope
  native_severity: major
  normalization_reason: Unsupported identity equivalence or strict superclass materially
    changes the source meaning.
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261014T135505Z-mammalian_meat_food_product
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2079
  disposition_reason: 'Exact maintained-input correction and regenerated claims verified.
    The exact GOLD production-process parent is excluded, preserving the two independent
    FoodOn material genera and 1916 ORGANISM assertions. The generic GOLD Meat products
    identity remains conflated with mammalian meat in #2078. No original poultry/fish
    membership has been recovered, and no child or identity migration is implied.'
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - FOODON:00001006
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained owner; generated habitat YAML is read-only
  description: Reassess mint habitatmech:GOLD.0347e0d978 and retain its native generic
    scope unless an actual exact identity is verified. A narrower mammalian class
    cannot be its broader parent. Audit Raw meat and butchery-cut children plus the
    two expected-parent exclusions for Cooked meat/Fermented meat products. Preserve
    all original counts and do not assume source-member species from a note.
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Edit maintained decisions or exact guarded overlays only; preserve frozen raw
    inventories and never hand-edit generated records.
  - Preserve source identifiers, source paths, count units, taxon metrics and honest
    native status unless separately evidence-backed.
  - Dry seed, inspect target canary and full before/after corpus delta; run schema,
    strict, history, provenance, corpus, site, label and authoritative QC gates.
  - Save a new immutable follow-up with this stable issue key and exact previous occurrence;
    do not rewrite this report.
limitations:
- Same-agent assessment, not independent approval.
- Original joins remain unavailable; positive current examples do not reconstruct
  frozen membership.
- 'Issues #2075/#2076/#2078/#2080/#2081 remain open; four bounded repairs do not resolve
  them.'
- Corrected-base QC predates the new successor bundles; final archive and publication
  checks are separate.
- No native status promotion, full ontology refresh, or SSSOM/KGX certification.
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261014T135505Z-mammalian_meat_food_product
  relationship: Exact predecessor findings reassessed; original report unchanged.
notes:
- Initial corrected-input capture 2026-10-14T14:09:50.020317Z; final inspection confirmed
  all captured input bytes unchanged.
tags:
- habitatmech
- record-review
- food
- followup
```
