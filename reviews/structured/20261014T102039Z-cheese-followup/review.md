# Scientific follow-up: cheese

- Review: 20261014T102039Z-cheese-followup
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T10:02:02.546430Z
- Finished UTC: 2026-10-14T10:20:39.101718Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The unsupported GOLD parent contribution is excluded for the exact source path. Independent ontology genera, identity, source IDs/labels/paths/counts/units, native status and previous events are preserved; one SOURCE_PARENT_EXCLUDED event is added. Generic cheese no longer becomes necessarily fermented. Whether the GOLD fermentation context narrows its source identity remains unresolved under #2053; the record still needs curation. The parent correction is not a source-member equivalence certification.

## Scope And Provenance

Complete corrected record and exact predecessor finding disposition.

Selection: Explicit source-preserving correction follow-up, not sampling. Exactly one generated record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0e966aec8a12892973dd15c536f89d90ab0c2c70.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| FOODON:03000287 | data/habitats/food/cheese.yaml | generated | cheese |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate | passed | True | FOODON:03000287 | Executed 2026-10-14T10:02:18.115822Z to 2026-10-14T10:02:20.348299Z. No issues found |
| just validate-strict | passed | True | FOODON:03000287 | Executed 2026-10-14T10:02:29.375588Z to 2026-10-14T10:02:34.192584Z. uv run python scripts/validate_strict.py data/habitats/food/cheese.yaml data/habitats/food/cooked_meat.yaml data/habitats/food/dairy_food_product.yaml data/habitats/host_associated/egg.yaml data/habitats/food/egg_products.yaml<br>Validating 5 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      5<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | FOODON:03000287 | Executed 2026-10-14T10:02:34.193195Z to 2026-10-14T10:02:41.329829Z. No issues found<br>659 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | FOODON:03000287 | Executed 2026-10-14T10:02:41.330400Z to 2026-10-14T10:02:41.842199Z. provenance current: 14 committed inventories, 2 GOLD sources |
| just verify-corpus | passed | True | FOODON:03000287 | Executed 2026-10-14T10:02:41.842688Z to 2026-10-14T10:02:57.759857Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| just validate-causal-all | passed | True | FOODON:03000287 | Executed 2026-10-14T10:02:57.760640Z to 2026-10-14T10:03:01.979292Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| just term-requests-check | passed | True | FOODON:03000287 | Executed 2026-10-14T10:03:01.979839Z to 2026-10-14T10:03:17.947037Z. term-request table is current (109 terms) |
| just validate-products | passed | True | FOODON:03000287 | Executed 2026-10-14T10:03:17.947566Z to 2026-10-14T10:04:03.215199Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1176<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2059<br><br>✅ All id↔label pairs correspond. |
| uv run | passed | True | FOODON:03000287 | Executed 2026-10-14T10:04:03.215881Z to 2026-10-14T10:05:25.219804Z. ........................................................................ [ 80%]<br>..................                                                       [100%]<br>90 passed in 81.08s (0:01:21) |
| uv run | passed | True | FOODON:03000287 | Executed 2026-10-14T10:05:25.220422Z to 2026-10-14T10:05:25.351468Z. All checks passed! |
| Exact corrected-base hosted authoritative QC | passed | True | FOODON:03000287 | Verified success on the captured corrected base. Post-save archive and final PR checks remain required. |
| Original source-member reconstruction | unavailable | False | FOODON:03000287 | Original source dumps/member crosswalks remain unavailable; predecessor GOLD access returned 403. No new access success or complete membership claim. |
| Expression-source applicability | not_applicable | False | FOODON:03000287 | No gene, regulator, protein or transcriptomics assertion. Habitat source identity is not expression-module evidence. |

## Scientific And Domain Assessments

### Identity, parent correction and exact finding disposition

grounding: supported. Targets: FOODON:03000287.

The unsupported GOLD parent contribution is excluded for the exact source path. Independent ontology genera, identity, source IDs/labels/paths/counts/units, native status and previous events are preserved; one SOURCE_PARENT_EXCLUDED event is added. Generic cheese no longer becomes necessarily fermented. Whether the GOLD fermentation context narrows its source identity remains unresolved under #2053; the record still needs curation. The parent correction is not a source-member equivalence certification.

### Source scope, counts, rank semantics and optional claims

evidence: supported. Targets: FOODON:03000287.

Re-read the entire current record. Source assertions remain distinct from bulk biosamples and complete-triad samples. No new environmental parameter, causal graph, citation, discussion or dataset assertion is introduced. No taxa are asserted. Hierarchy-only curation does not promote native status; the four records retain their original status. Neighboring source records remain unchanged.

### Unresolved source exactness after parent correction

identity: concern. Targets: FOODON:03000287.

Removing the false generic-cheese fermentation parent does not establish that the GOLD source bin is exactly generic cheese. The fermentation path may narrow source scope or may be organizational context; the original source members and authoritative bin definition are unavailable. The exact match is not proven false, but its scope is not substantiated by the inspected evidence.

## Findings

### F1: Generic cheese inherits an unsupported fermentation restriction

major / resolved / confirmed; issue key: cheese-generic-fermented-parent.

The generic FoodOn cheese definition and cheese-food-product genus are supported, but the GOLD-derived Fermented dairy products parent is not a genus of all cheese. FAO describes an industrial paneer route using heat and citric-acid coagulation without a fermentation step. Unripened alone is not evidence of nonfermentation. The exact scope of the GOLD bin remains less certain than the invalid universal parent claim.

Disposition: The unsupported GOLD parent contribution is excluded for the exact source path. Independent ontology genera, identity, source IDs/labels/paths/counts/units, native status and previous events are preserved; one SOURCE_PARENT_EXCLUDED event is added. Generic cheese no longer becomes necessarily fermented. Whether the GOLD fermentation context narrows its source identity remains unresolved under #2053; the record still needs curation. The parent correction is not a source-member equivalence certification.

### F2: Fermentation-qualified source still lacks substantiated generic exact identity

major / open / provisional; issue key: cheese-fermentation-context-exact-identity.

Removing the false generic-cheese fermentation parent does not establish that the GOLD source bin is exactly generic cheese. The fermentation path may narrow source scope or may be organizational context; the original source members and authoritative bin definition are unavailable. The exact match is not proven false, but its scope is not substantiated by the inspected evidence.

## Recommended Actions And Acceptance Checks

### A2

Recover an authoritative source-bin definition or member crosswalk to decide whether fermentation narrows this source. Substantiate exact generic identity or adopt only a defensible source-preserving mapping; do not guess an exact replacement.

- Preserve all source observations and distinguish 582 ORGANISM-unit assertions, 65 bulk biosamples and the single complete triad.
- Edit maintained decisions only, inspect a canary, regenerate affected records/redirects/map/site and pass full native gates.
- Save a successor retaining this exact issue key and occurrence; the parent-only correction does not close this identity finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| CURRENT | data/habitats/food/cheese.yaml; Complete corrected YAML, all source and taxon assertions and history | supports | The unsupported GOLD parent contribution is excluded for the exact source path. Independent ontology genera, identity, source IDs/labels/paths/counts/units, native status and previous events are preserved; one SOURCE_PARENT_EXCLUDED event is added. Generic cheese no longer becomes necessarily fermented. Whether the GOLD fermentation context narrows its source identity remains unresolved under #2053; the record still needs curation. The parent correction is not a source-member equivalence certification. |
| OWNERS | curation/decisions.tsv; curation/gold_parent_exclusions.tsv; tests/test_food_egg_scope.py; curation/gold_parent_exclusions.tsv:2 identifier=habitatmech:GOLD.58a308b569 | supports | Read the complete maintained rows, five append-only histories and counterfactual regression. Full corpus comparison changes only four common records (parent/history) and replaces the former food-egg identity with the BacDive source mint. Raw observations are unchanged. |
| PREVIOUS | reviews/structured/20261014T095250Z-cheese/review.yaml | context_only | Read the immutable predecessor, exact finding, evidence receipts and limitations. Its baseline decision rows are historical, not current line references. |
| QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38547107819 | supports | Verified full hosted QC success on exact corrected commit 0e966aec8a12892973dd15c536f89d90ab0c2c70. Initial corrected scientific inputs were rehashed without change after map/site publication. New successor bundles still require post-save and final PR checks. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md | supports | Applied strict-superclass, source identity, count-unit, MIxS role, optional-field and ITEM status rules from the local record checklist. |
| TRANSFORM | src/habitatmech/seed.py; src/habitatmech/extract.py; extract_gold; extract_bacdive; ingest_gold; ingest_bacdive; build_document; scripts/extract_gold_biosamples.py; scripts/aggregate_gold_triads.py | supports | GOLD counts outgoing occurrence edges by subject prefix, not proven distinct organisms. Bulk biosamples and study path unions are different inventories. BacDive aggregate strain_count counts source outgoing edges; taxon associations deduplicate strain joins and retain top-25 ranks/candidate_pool. Neither ranking implies characteristic presence. |
| FOODON | https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl; FOODON:03000287; relevant FoodOn parents and candidate context | supports | Historical external evidence retained from the predecessor, not a description of the corrected record. Read definitions, typed synonyms, active status and direct named parents in the pinned official RDF/XML. SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf. The generic FoodOn cheese definition and cheese-food-product genus are supported, but the GOLD-derived Fermented dairy products parent is not a genus of all cheese. FAO describes an industrial paneer route using heat and citric-acid coagulation without a fermentation step. Unripened alone is not evidence of nonfermentation. The exact scope of the GOLD bin remains less certain than the invalid universal parent claim. |
| AVAILABILITY | conf/sources.yaml | context_only | {"accessed_at": "2026-10-14T09:44:16.995506Z", "command": ["rg", "--no-ignore", "--hidden", "--files", ".", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"], "enumerated_files": 41045, "exit_code": 0, "interpretation": "Ignored files included. Bounded to this repository and the configured kg-microbe data root, not all disks. No exact original member crosswalk is inferred from inventory presence.", "matches": []} |
| GOLD_ACCESS | https://gold.jgi.doe.gov/ | context_only | All 25 retrieved study URLs for this cohort returned HTTP 403; no page contents inferred. {"Gs0111397": {"accessed_at": "2026-10-14T09:41:44.844987Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0111397"}, "Gs0117939": {"accessed_at": "2026-10-14T09:41:44.917192Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0117939"}, "Gs0121311": {"accessed_at": "2026-10-14T09:41:44.946799Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0121311"}, "Gs0127428": {"accessed_at": "2026-10-14T09:41:44.984453Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0127428"}, "Gs0132999": {"accessed_at": "2026-10-14T09:41:45.015413Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0132999"}, "Gs0133059": {"accessed_at": "2026-10-14T09:41:45.135671Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0133059"}, "Gs0133061": {"accessed_at": "2026-10-14T09:41:45.168420Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0133061"}, "Gs0133297": {"accessed_at": "2026-10-14T09:41:45.211877Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0133297"}, "Gs0135057": {"accessed_at": "2026-10-14T09:41:45.248222Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0135057"}, "Gs0144921": {"accessed_at": "2026-10-14T09:41:45.279258Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0144921"}, "Gs0144994": {"accessed_at": "2026-10-14T09:41:45.325246Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0144994"}, "Gs0145069": {"accessed_at": "2026-10-14T09:41:45.359515Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0145069"}, "Gs0150357": {"accessed_at": "2026-10-14T09:41:45.403531Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150357"}, "Gs0150359": {"accessed_at": "2026-10-14T09:41:45.534775Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150359"}, "Gs0150613": {"accessed_at": "2026-10-14T09:41:45.657223Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150613"}, "Gs0150615": {"accessed_at": "2026-10-14T09:41:45.694287Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150615"}, "Gs0153752": {"accessed_at": "2026-10-14T09:41:45.728601Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153752"}, "Gs0153769": {"accessed_at": "2026-10-14T09:41:45.759538Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153769"}, "Gs0153860": {"accessed_at": "2026-10-14T09:41:45.793390Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153860"}, "Gs0153898": {"accessed_at": "2026-10-14T09:41:45.825210Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153898"}, "Gs0154236": {"accessed_at": "2026-10-14T09:41:45.874324Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154236"}, "Gs0154282": {"accessed_at": "2026-10-14T09:41:45.906640Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"}, "Gs0156793": {"accessed_at": "2026-10-14T09:41:45.940030Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0156793"}, "Gs0159152": {"accessed_at": "2026-10-14T09:41:45.985158Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0159152"}, "Gs0161780": {"accessed_at": "2026-10-14T09:41:46.016628Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0161780"}} |
| FAO | https://www.fao.org/4/t0251e/T0251E12.htm; I. Cheeses; 2.5 Paneer; India Industrial Technology | supports | Inspected the India industrial paneer preparation: heated milk, citric-acid coagulation, settling, pressing and chilling. Inference: cheese production need not include fermentation. Do not generalize this to every paneer route or infer nonfermentation from unripened alone. SHA256 05f97764061e20fbe01cd46eb655dff096aafb2e9e37fb2fb032cfdb8a03d537 |
| LEGACY | reports/yaml_record_review/20260928T023452Z-fermented_dairy_products.md | supports | Read full neighbor report. Its cheese-child consistency statement does not establish universal fermentation; the present counterexample limits that earlier inference. The frozen-slice term absence is not a claim about full FoodOn. |
| RAW | reviews/structured/20261014T095250Z-cheese/review.yaml; evidence_id=RAW; assessments SCIENCE | context_only | Frozen source tables are byte-unchanged; baseline curation rows are superseded by OWNERS. Path row 63 names node 5509 and 582 ORGANISM assertions. Bulk row 307 has 65 BIOSAMPLE observations, separately. Eight study rows include both single-path and multi-path studies. Triad rows 86-88 describe one complete sample/study: broad-scale production area, obsolete local-scale food-product annotation and medium cheese food product. These roles and the obsolete upstream annotation are not promoted to identity or habitat-wide parameters. The legacy fermented-dairy report checks dairy ancestry but does not establish that generic cheese is necessarily fermented. |

## Limits And Additional Notes

- Same-agent review and adversarial pass, not independent approval.
- Original source membership remains unavailable. Cheese source identity versus fermentation context and fuller egg-source scope are not resolved by bounded corrections.
- No latest-ontology refresh or SSSOM/KGX conformance certification. Native label checks retain configured exceptions and unsupported-prefix skips.
- Only exact predecessor findings receive the shown dispositions; adjacent Fish products, Meat products and Fermented dairy products records are not silently curated.
- Corrected-base full QC predates new successor bundles; post-save archive and final publication gates remain required.
- Initial corrected capture at 09bb13f857d3e634f4a8cb295d7b847b10612a4b; reinspection after map/site publication proved every scientific input hash unchanged before recording the final corrected base. The explicit empty-target relation default is semantically inactive and was captured before this review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T102039Z-cheese-followup
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific follow-up: cheese'
started_at: '2026-10-14T10:02:02.546430Z'
finished_at: '2026-10-14T10:20:39.101718Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent participated in repository work; not independent
    approval.
skill: .claude/skills/curate-yaml-record/SKILL.md
completion: completed
scientific_review: true
verdict: needs_curation
summary: 'The unsupported GOLD parent contribution is excluded for the exact source
  path. Independent ontology genera, identity, source IDs/labels/paths/counts/units,
  native status and previous events are preserved; one SOURCE_PARENT_EXCLUDED event
  is added. Generic cheese no longer becomes necessarily fermented. Whether the GOLD
  fermentation context narrows its source identity remains unresolved under #2053;
  the record still needs curation. The parent correction is not a source-member equivalence
  certification.'
source:
  git_revision: 0e966aec8a12892973dd15c536f89d90ab0c2c70
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
    sha256: 05aee2989e186bba8ae0ecb5eca6c1f2ad3c1e6977c3aaf0aea6977bccd6f900
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: ffde12786b35a791272a202f26d3baa0a36879c63a97dbdc2d11d38683d7fe0f
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/samples/class_swept_unscreened-20260814.tsv
    sha256: 27fce2849781b21f8fdb434aaaffac0f55e51bef84f1c1ea7d7feecd11d8471e
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
  - path: data/habitats/food/cheese.yaml
    sha256: 16174620ee9ed816c5edce647beda782cbe1709a576d4222e3718990342cc3d5
    role: target
  - path: data/habitats/food/cold_smoked_fish.yaml
    sha256: ea4db4c6c2d849efc11464ef0373492ccb6e3b0aac284415ce87140a22223939
    role: context
  - path: data/habitats/food/cooked_blood.yaml
    sha256: e0a358f58f554a0e652187d63d5399a8f3c36516b0c96d791adbcbe59ae8aa28
    role: context
  - path: data/habitats/food/cooked_fish.yaml
    sha256: 7a1a29ec27659c2d48296a6b09e9d29a48d6c86f4ca48ea2ab2c0bd06c81a4a8
    role: context
  - path: data/habitats/food/cooked_meat.yaml
    sha256: 80e2f39391b2d20f587b21dfc95c1e9fb9b3217c75c7adcfec1758d9389be0bc
    role: context
  - path: data/habitats/food/dairy_food_product.yaml
    sha256: 36c6b5dde12d0d75eca04ac0f91200e839763e14e2ff813ebb85fb7242fb3001
    role: context
  - path: data/habitats/food/egg_products.yaml
    sha256: bb5fcdf9504b49c4163294fbb90685165a091798bf66da0a633bc4419de77a74
    role: context
  - path: data/habitats/food/fermented_dairy_products.yaml
    sha256: 9ed59912b37facdd56bb980f312ad3f131d13a6a604f8294574f94477e889ae4
    role: context
  - path: data/habitats/food/fish_products.yaml
    sha256: 5435e216e51f243842916c2e4199123992c81ab166b0746963ffeee71f5253b3
    role: context
  - path: data/habitats/food/mammalian_meat_food_product.yaml
    sha256: fab8fbd8e3352bfe93aefac2761dded407774e918244be3e6b8a87ae45ec27b5
    role: context
  - path: data/habitats/host_associated/egg.yaml
    sha256: 4442ae82f9df6071c9c46f1f0ce6db9210ed6b836e497ccfbb22525c11ee2781
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
    sha256: 105b3c8e10f43ce689b05d3089d3a8be1d713a98dd6806e11be37ebd85b10590
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/mappings/cheese/2026-10-14T095757Z-codex-gpt-5-78213b.yaml
    sha256: 6b4153ee37290c15aca5f066f991c4a9f87c75fe8c31f92d9142c40e66e28996
    role: context
  - path: history/mappings/cooked_meat/2026-10-14T095758Z-codex-gpt-5-a6b320.yaml
    sha256: 5a6022050f294ca92d740f5bf2fb356aae1712cea5a05b7b400e56fe1ee04719
    role: context
  - path: history/mappings/dairy_food_product/2026-10-14T095759Z-codex-gpt-5-857556.yaml
    sha256: 713d9f40c7aeddef2a7030b6c4d1569a6691aa63fa721ad06ebb61920977121c
    role: context
  - path: history/mappings/egg_food_product/2026-10-14T095800Z-codex-gpt-5-f76776.yaml
    sha256: 5fa3a42ef9295f98e2c07bc1aa4e7ac1f1da6a0ed93a2789422c7631dd9dac32
    role: context
  - path: history/mappings/egg_products/2026-10-14T095801Z-codex-gpt-5-1e0c57.yaml
    sha256: 7d1d265ed407ab60770b12884a8e7c64eb8493b9bd85c662842d9f0ea06a2ac4
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260928T023452Z-fermented_dairy_products.md
    sha256: 97780165ab7bf28e671769c7f4b43d60edb3d5e0d2b96fb7a1143c3a42d5c561
    role: context
  - path: reviews/structured/20261014T095250Z-cheese/review.yaml
    sha256: 9a89fd3caad3cf35ce6104d1207f0961c537cb41356684cc7a3c08f66b95ae93
    role: context
  - path: scripts/aggregate_gold_triads.py
    sha256: 0e25179dbecd7c73cbedd99a0ae44e56e4992afb9e1ec02d2411439f643b8e54
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/seed.py
    sha256: 4adf105e23d75c3563a516a0c160623d1065df7fcb2f31b7a0a0a8303d0401be
    role: context
  - path: tests/test_food_egg_scope.py
    sha256: 9f6fbc43fef08aa610cecf31d956f83e30d9aeb9b74eebda525b890924ad1ab8
    role: context
  - path: tests/test_food_review_fixes.py
    sha256: bc798ddc7027b09b4300ef507ae62eea8037d25ce0b7a623ef605ec86ef1e94f
    role: context
targets:
- target_id: FOODON:03000287
  path: data/habitats/food/cheese.yaml
  label: cheese
  kind: generated
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_isolation_sources.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_source_taxa.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input owner; generated records are read-only
scope:
  description: Complete corrected record and exact predecessor finding disposition.
  selection: Explicit source-preserving correction follow-up, not sampling. Exactly
    one generated record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - FOODON:03000287
evidence:
- evidence_id: CURRENT
  kind: record_content
  reference: data/habitats/food/cheese.yaml
  accessed_at: '2026-10-14T10:20:39.085994Z'
  support: supports
  locator: Complete corrected YAML, all source and taxon assertions and history
  summary: 'The unsupported GOLD parent contribution is excluded for the exact source
    path. Independent ontology genera, identity, source IDs/labels/paths/counts/units,
    native status and previous events are preserved; one SOURCE_PARENT_EXCLUDED event
    is added. Generic cheese no longer becomes necessarily fermented. Whether the
    GOLD fermentation context narrows its source identity remains unresolved under
    #2053; the record still needs curation. The parent correction is not a source-member
    equivalence certification.'
- evidence_id: OWNERS
  kind: record_content
  reference: curation/decisions.tsv; curation/gold_parent_exclusions.tsv; tests/test_food_egg_scope.py
  accessed_at: '2026-10-14T10:20:39.085994Z'
  support: supports
  summary: Read the complete maintained rows, five append-only histories and counterfactual
    regression. Full corpus comparison changes only four common records (parent/history)
    and replaces the former food-egg identity with the BacDive source mint. Raw observations
    are unchanged.
  locator: curation/gold_parent_exclusions.tsv:2 identifier=habitatmech:GOLD.58a308b569
- evidence_id: PREVIOUS
  kind: prior_review
  reference: reviews/structured/20261014T095250Z-cheese/review.yaml
  accessed_at: '2026-10-14T10:20:39.085994Z'
  support: context_only
  summary: Read the immutable predecessor, exact finding, evidence receipts and limitations.
    Its baseline decision rows are historical, not current line references.
- evidence_id: QC
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38547107819
  accessed_at: '2026-10-14T10:20:39.085994Z'
  support: supports
  summary: Verified full hosted QC success on exact corrected commit 0e966aec8a12892973dd15c536f89d90ab0c2c70.
    Initial corrected scientific inputs were rehashed without change after map/site
    publication. New successor bundles still require post-save and final PR checks.
- evidence_id: RULES
  kind: authority
  reference: docs/CURATION.md; docs/HARMONIZATION.md
  summary: Applied strict-superclass, source identity, count-unit, MIxS role, optional-field
    and ITEM status rules from the local record checklist.
  accessed_at: '2026-10-14T09:52:50.376328Z'
  support: supports
- evidence_id: TRANSFORM
  kind: record_content
  reference: src/habitatmech/seed.py; src/habitatmech/extract.py
  summary: GOLD counts outgoing occurrence edges by subject prefix, not proven distinct
    organisms. Bulk biosamples and study path unions are different inventories. BacDive
    aggregate strain_count counts source outgoing edges; taxon associations deduplicate
    strain joins and retain top-25 ranks/candidate_pool. Neither ranking implies characteristic
    presence.
  accessed_at: '2026-10-14T09:52:50.376328Z'
  support: supports
  locator: extract_gold; extract_bacdive; ingest_gold; ingest_bacdive; build_document;
    scripts/extract_gold_biosamples.py; scripts/aggregate_gold_triads.py
- evidence_id: FOODON
  kind: database
  reference: https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl
  summary: Historical external evidence retained from the predecessor, not a description
    of the corrected record. Read definitions, typed synonyms, active status and direct
    named parents in the pinned official RDF/XML. SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf.
    The generic FoodOn cheese definition and cheese-food-product genus are supported,
    but the GOLD-derived Fermented dairy products parent is not a genus of all cheese.
    FAO describes an industrial paneer route using heat and citric-acid coagulation
    without a fermentation step. Unripened alone is not evidence of nonfermentation.
    The exact scope of the GOLD bin remains less certain than the invalid universal
    parent claim.
  accessed_at: '2026-10-14T09:41:41.574451Z'
  support: supports
  locator: FOODON:03000287; relevant FoodOn parents and candidate context
- evidence_id: AVAILABILITY
  kind: record_content
  reference: conf/sources.yaml
  summary: '{"accessed_at": "2026-10-14T09:44:16.995506Z", "command": ["rg", "--no-ignore",
    "--hidden", "--files", ".", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"],
    "enumerated_files": 41045, "exit_code": 0, "interpretation": "Ignored files included.
    Bounded to this repository and the configured kg-microbe data root, not all disks.
    No exact original member crosswalk is inferred from inventory presence.", "matches":
    []}'
  accessed_at: '2026-10-14T09:52:50.376328Z'
  support: context_only
- evidence_id: GOLD_ACCESS
  kind: database
  reference: https://gold.jgi.doe.gov/
  summary: 'All 25 retrieved study URLs for this cohort returned HTTP 403; no page
    contents inferred. {"Gs0111397": {"accessed_at": "2026-10-14T09:41:44.844987Z",
    "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0111397"},
    "Gs0117939": {"accessed_at": "2026-10-14T09:41:44.917192Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0117939"}, "Gs0121311":
    {"accessed_at": "2026-10-14T09:41:44.946799Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0121311"}, "Gs0127428": {"accessed_at":
    "2026-10-14T09:41:44.984453Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0127428"},
    "Gs0132999": {"accessed_at": "2026-10-14T09:41:45.015413Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0132999"}, "Gs0133059":
    {"accessed_at": "2026-10-14T09:41:45.135671Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0133059"}, "Gs0133061": {"accessed_at":
    "2026-10-14T09:41:45.168420Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0133061"},
    "Gs0133297": {"accessed_at": "2026-10-14T09:41:45.211877Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0133297"}, "Gs0135057":
    {"accessed_at": "2026-10-14T09:41:45.248222Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0135057"}, "Gs0144921": {"accessed_at":
    "2026-10-14T09:41:45.279258Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0144921"},
    "Gs0144994": {"accessed_at": "2026-10-14T09:41:45.325246Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0144994"}, "Gs0145069":
    {"accessed_at": "2026-10-14T09:41:45.359515Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0145069"}, "Gs0150357": {"accessed_at":
    "2026-10-14T09:41:45.403531Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150357"},
    "Gs0150359": {"accessed_at": "2026-10-14T09:41:45.534775Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150359"}, "Gs0150613":
    {"accessed_at": "2026-10-14T09:41:45.657223Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0150613"}, "Gs0150615": {"accessed_at":
    "2026-10-14T09:41:45.694287Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150615"},
    "Gs0153752": {"accessed_at": "2026-10-14T09:41:45.728601Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153752"}, "Gs0153769":
    {"accessed_at": "2026-10-14T09:41:45.759538Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0153769"}, "Gs0153860": {"accessed_at":
    "2026-10-14T09:41:45.793390Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153860"},
    "Gs0153898": {"accessed_at": "2026-10-14T09:41:45.825210Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153898"}, "Gs0154236":
    {"accessed_at": "2026-10-14T09:41:45.874324Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0154236"}, "Gs0154282": {"accessed_at":
    "2026-10-14T09:41:45.906640Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"},
    "Gs0156793": {"accessed_at": "2026-10-14T09:41:45.940030Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0156793"}, "Gs0159152":
    {"accessed_at": "2026-10-14T09:41:45.985158Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0159152"}, "Gs0161780": {"accessed_at":
    "2026-10-14T09:41:46.016628Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0161780"}}'
  accessed_at: '2026-10-14T09:52:50.376328Z'
  support: context_only
- evidence_id: FAO
  kind: authority
  reference: https://www.fao.org/4/t0251e/T0251E12.htm
  summary: 'Inspected the India industrial paneer preparation: heated milk, citric-acid
    coagulation, settling, pressing and chilling. Inference: cheese production need
    not include fermentation. Do not generalize this to every paneer route or infer
    nonfermentation from unripened alone. SHA256 05f97764061e20fbe01cd46eb655dff096aafb2e9e37fb2fb032cfdb8a03d537'
  accessed_at: '2026-10-14T09:44:22.790813Z'
  support: supports
  locator: I. Cheeses; 2.5 Paneer; India Industrial Technology
- evidence_id: LEGACY
  kind: prior_review
  reference: reports/yaml_record_review/20260928T023452Z-fermented_dairy_products.md
  summary: Read full neighbor report. Its cheese-child consistency statement does
    not establish universal fermentation; the present counterexample limits that earlier
    inference. The frozen-slice term absence is not a claim about full FoodOn.
  accessed_at: '2026-10-14T09:52:50.376328Z'
  support: supports
- evidence_id: RAW
  kind: prior_review
  reference: reviews/structured/20261014T095250Z-cheese/review.yaml
  locator: evidence_id=RAW; assessments SCIENCE
  accessed_at: '2026-10-14T10:20:39.085994Z'
  support: context_only
  summary: 'Frozen source tables are byte-unchanged; baseline curation rows are superseded
    by OWNERS. Path row 63 names node 5509 and 582 ORGANISM assertions. Bulk row 307
    has 65 BIOSAMPLE observations, separately. Eight study rows include both single-path
    and multi-path studies. Triad rows 86-88 describe one complete sample/study: broad-scale
    production area, obsolete local-scale food-product annotation and medium cheese
    food product. These roles and the obsolete upstream annotation are not promoted
    to identity or habitat-wide parameters. The legacy fermented-dairy report checks
    dairy ancestry but does not establish that generic cheese is necessarily fermented.'
checks:
- check_id: C0
  name: just validate
  status: passed
  required: true
  target_ids:
  - FOODON:03000287
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/food/cheese.yaml
  exit_code: 0
  summary: Executed 2026-10-14T10:02:18.115822Z to 2026-10-14T10:02:20.348299Z. No
    issues found
- check_id: C5
  name: just validate-strict
  status: passed
  required: true
  target_ids:
  - FOODON:03000287
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/food/cheese.yaml data/habitats/food/cooked_meat.yaml data/habitats/food/dairy_food_product.yaml
    data/habitats/host_associated/egg.yaml data/habitats/food/egg_products.yaml
  exit_code: 0
  summary: "Executed 2026-10-14T10:02:29.375588Z to 2026-10-14T10:02:34.192584Z. uv\
    \ run python scripts/validate_strict.py data/habitats/food/cheese.yaml data/habitats/food/cooked_meat.yaml\
    \ data/habitats/food/dairy_food_product.yaml data/habitats/host_associated/egg.yaml\
    \ data/habitats/food/egg_products.yaml\nValidating 5 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      5\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
- check_id: C6
  name: just validate-history
  status: passed
  required: true
  target_ids:
  - FOODON:03000287
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  summary: 'Executed 2026-10-14T10:02:34.193195Z to 2026-10-14T10:02:41.329829Z. No
    issues found

    659 history record(s) valid against src/habitatmech/schema/history.yaml'
- check_id: C7
  name: just provenance-check
  status: passed
  required: true
  target_ids:
  - FOODON:03000287
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  summary: 'Executed 2026-10-14T10:02:41.330400Z to 2026-10-14T10:02:41.842199Z. provenance
    current: 14 committed inventories, 2 GOLD sources'
- check_id: C8
  name: just verify-corpus
  status: passed
  required: true
  target_ids:
  - FOODON:03000287
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  summary: "Executed 2026-10-14T10:02:41.842688Z to 2026-10-14T10:02:57.759857Z. expected\
    \ 3208 records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing:\
    \ 0\n\ncorpus reproduces exactly from data/raw/"
- check_id: C9
  name: just validate-causal-all
  status: passed
  required: true
  target_ids:
  - FOODON:03000287
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  summary: Executed 2026-10-14T10:02:57.760640Z to 2026-10-14T10:03:01.979292Z. validated
    32 causal-graph curation file(s) with 32 graph(s)
- check_id: C10
  name: just term-requests-check
  status: passed
  required: true
  target_ids:
  - FOODON:03000287
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  summary: Executed 2026-10-14T10:03:01.979839Z to 2026-10-14T10:03:17.947037Z. term-request
    table is current (109 terms)
- check_id: C11
  name: just validate-products
  status: passed
  required: true
  target_ids:
  - FOODON:03000287
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  summary: "Executed 2026-10-14T10:03:17.947566Z to 2026-10-14T10:04:03.215199Z. id↔label\
    \ correspondence summary:\n          OK_CANONICAL: 1176\n            OK_SYNONYM:\
    \ 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2059\n\n✅ All id↔label\
    \ pairs correspond."
- check_id: C12
  name: uv run
  status: passed
  required: true
  target_ids:
  - FOODON:03000287
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache uv run pytest -q tests/test_food_egg_scope.py
    tests/test_food_review_fixes.py tests/test_gold_parent_exclusions.py tests/test_ontology_labels.py
  exit_code: 0
  summary: 'Executed 2026-10-14T10:04:03.215881Z to 2026-10-14T10:05:25.219804Z. ........................................................................
    [ 80%]

    ..................                                                       [100%]

    90 passed in 81.08s (0:01:21)'
- check_id: C13
  name: uv run
  status: passed
  required: true
  target_ids:
  - FOODON:03000287
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache uv run ruff check .
  exit_code: 0
  summary: Executed 2026-10-14T10:05:25.220422Z to 2026-10-14T10:05:25.351468Z. All
    checks passed!
- check_id: QC
  name: Exact corrected-base hosted authoritative QC
  status: passed
  required: true
  target_ids:
  - FOODON:03000287
  command: gh run view 38547107819 --json headSha,status,conclusion,url
  exit_code: 0
  summary: Verified success on the captured corrected base. Post-save archive and
    final PR checks remain required.
  evidence_ids:
  - QC
- check_id: MEMBERS
  name: Original source-member reconstruction
  status: unavailable
  required: false
  target_ids:
  - FOODON:03000287
  summary: Original source dumps/member crosswalks remain unavailable; predecessor
    GOLD access returned 403. No new access success or complete membership claim.
  evidence_ids:
  - AVAILABILITY
  - GOLD_ACCESS
- check_id: IMODULON
  name: Expression-source applicability
  status: not_applicable
  required: false
  target_ids:
  - FOODON:03000287
  summary: No gene, regulator, protein or transcriptomics assertion. Habitat source
    identity is not expression-module evidence.
assessments:
- assessment_id: FIX
  area: grounding
  topic: Identity, parent correction and exact finding disposition
  outcome: supported
  target_ids:
  - FOODON:03000287
  evidence_ids:
  - CURRENT
  - OWNERS
  - PREVIOUS
  - QC
  - RULES
  - FOODON
  - FAO
  summary: 'The unsupported GOLD parent contribution is excluded for the exact source
    path. Independent ontology genera, identity, source IDs/labels/paths/counts/units,
    native status and previous events are preserved; one SOURCE_PARENT_EXCLUDED event
    is added. Generic cheese no longer becomes necessarily fermented. Whether the
    GOLD fermentation context narrows its source identity remains unresolved under
    #2053; the record still needs curation. The parent correction is not a source-member
    equivalence certification.'
- assessment_id: SCIENCE
  area: evidence
  topic: Source scope, counts, rank semantics and optional claims
  outcome: supported
  target_ids:
  - FOODON:03000287
  evidence_ids:
  - CURRENT
  - RAW
  - TRANSFORM
  - OWNERS
  - FAO
  summary: Re-read the entire current record. Source assertions remain distinct from
    bulk biosamples and complete-triad samples. No new environmental parameter, causal
    graph, citation, discussion or dataset assertion is introduced. No taxa are asserted.
    Hierarchy-only curation does not promote native status; the four records retain
    their original status. Neighboring source records remain unchanged.
- assessment_id: SCOPE
  area: identity
  topic: Unresolved source exactness after parent correction
  outcome: concern
  target_ids:
  - FOODON:03000287
  evidence_ids:
  - CURRENT
  - RAW
  - PREVIOUS
  - FOODON
  - FAO
  - GOLD_ACCESS
  summary: Removing the false generic-cheese fermentation parent does not establish
    that the GOLD source bin is exactly generic cheese. The fermentation path may
    narrow source scope or may be organizational context; the original source members
    and authoritative bin definition are unavailable. The exact match is not proven
    false, but its scope is not substantiated by the inspected evidence.
findings:
- finding_id: F1
  issue_key: cheese-generic-fermented-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Generic cheese inherits an unsupported fermentation restriction
  description: The generic FoodOn cheese definition and cheese-food-product genus
    are supported, but the GOLD-derived Fermented dairy products parent is not a genus
    of all cheese. FAO describes an industrial paneer route using heat and citric-acid
    coagulation without a fermentation step. Unripened alone is not evidence of nonfermentation.
    The exact scope of the GOLD bin remains less certain than the invalid universal
    parent claim.
  target_ids:
  - FOODON:03000287
  field_paths:
  - parent_habitats
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input owner; generated records are read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input owner; generated records are read-only
  evidence_ids:
  - CURRENT
  - OWNERS
  - PREVIOUS
  - QC
  - RULES
  - FOODON
  - FAO
  rule_id: 'docs/CURATION.md: identity and strict parent rules'
  native_severity: major
  normalization_reason: A materially unsupported strict superclass is a major semantic
    defect, not style.
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261014T095250Z-cheese
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2048
  disposition_reason: 'The unsupported GOLD parent contribution is excluded for the
    exact source path. Independent ontology genera, identity, source IDs/labels/paths/counts/units,
    native status and previous events are preserved; one SOURCE_PARENT_EXCLUDED event
    is added. Generic cheese no longer becomes necessarily fermented. Whether the
    GOLD fermentation context narrows its source identity remains unresolved under
    #2053; the record still needs curation. The parent correction is not a source-member
    equivalence certification.'
- finding_id: F2
  issue_key: cheese-fermentation-context-exact-identity
  category: grounding
  severity: major
  status: open
  certainty: provisional
  title: Fermentation-qualified source still lacks substantiated generic exact identity
  description: Removing the false generic-cheese fermentation parent does not establish
    that the GOLD source bin is exactly generic cheese. The fermentation path may
    narrow source scope or may be organizational context; the original source members
    and authoritative bin definition are unavailable. The exact match is not proven
    false, but its scope is not substantiated by the inspected evidence.
  target_ids:
  - FOODON:03000287
  field_paths:
  - identifier
  - grounding_status
  - source_attestations[0].mapping_predicate
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Source identity decision owner
  evidence_ids:
  - CURRENT
  - RAW
  - PREVIOUS
  - FOODON
  - FAO
  - RULES
  - GOLD_ACCESS
  rule_id: 'docs/CURATION.md: exact identity versus contextual source hierarchy'
  native_severity: major
  normalization_reason: Unsubstantiated exact source equivalence is a material evidence
    gap, distinct from the resolved false parent; uncertainty is retained rather than
    claiming a proven wrong identity.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2053
actions:
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - FOODON:03000287
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Source identity decision owner
  generator: src/habitatmech/seed.py
  description: Recover an authoritative source-bin definition or member crosswalk
    to decide whether fermentation narrows this source. Substantiate exact generic
    identity or adopt only a defensible source-preserving mapping; do not guess an
    exact replacement.
  acceptance_checks:
  - Preserve all source observations and distinguish 582 ORGANISM-unit assertions,
    65 bulk biosamples and the single complete triad.
  - Edit maintained decisions only, inspect a canary, regenerate affected records/redirects/map/site
    and pass full native gates.
  - Save a successor retaining this exact issue key and occurrence; the parent-only
    correction does not close this identity finding.
limitations:
- Same-agent review and adversarial pass, not independent approval.
- Original source membership remains unavailable. Cheese source identity versus fermentation
  context and fuller egg-source scope are not resolved by bounded corrections.
- No latest-ontology refresh or SSSOM/KGX conformance certification. Native label
  checks retain configured exceptions and unsupported-prefix skips.
- Only exact predecessor findings receive the shown dispositions; adjacent Fish products,
  Meat products and Fermented dairy products records are not silently curated.
- Corrected-base full QC predates new successor bundles; post-save archive and final
  publication gates remain required.
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261014T095250Z-cheese
  relationship: Exact immutable predecessor finding reassessed without rewriting its
    report.
notes:
- Initial corrected capture at 09bb13f857d3e634f4a8cb295d7b847b10612a4b; reinspection
  after map/site publication proved every scientific input hash unchanged before recording
  the final corrected base. The explicit empty-target relation default is semantically
  inactive and was captured before this review.
tags:
- habitatmech
- record-review
- food
- followup
```
