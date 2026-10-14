# Scientific record review: Egg products

- Review: 20261014T095336Z-egg_products
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T09:39:36.440442Z
- Finished UTC: 2026-10-14T09:53:36.041907Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The GOLD Egg products source names food material and retains its native identity; its only parent FOODON:03530206 is a production process, not a material genus. This GOLD food bin must not be merged automatically with the separate BacDive Egg source. An egg-food candidate requires an ITEM scope assessment before grounding.

## Scope And Provenance

Complete individual record and every contributing source concept.

Selection: Next eight pending food records by path after ignored-inclusive census (975/3208 current targets; food 8/61). This bundle assesses exactly one target, not the whole cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 161bd1b665f9c64e8c8ee6aec86f8fc423901632.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.363486c188 | data/habitats/food/egg_products.yaml | generated | Egg products |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | habitatmech:GOLD.363486c188 | Executed 2026-10-14T09:40:01.804595Z to 2026-10-14T09:40:03.735833Z. No issues found |
| Native validate-strict | passed | True | habitatmech:GOLD.363486c188 | Executed 2026-10-14T09:40:03.736366Z to 2026-10-14T09:40:08.470905Z. uv run python scripts/validate_strict.py data/habitats/food/cheese.yaml data/habitats/food/cold_smoked_fish.yaml data/habitats/food/cooked_blood.yaml data/habitats/food/cooked_fish.yaml data/habitats/food/cooked_meat.yaml data/habitats/food/dairy_food_product.yaml data/habitats/food/egg_food_product.yaml data/habitats/food/egg_products.yaml<br>Validating 8 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      8<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| Native validate-history | passed | True | habitatmech:GOLD.363486c188 | Executed 2026-10-14T09:40:08.471507Z to 2026-10-14T09:40:14.745430Z. No issues found<br>654 history record(s) valid against src/habitatmech/schema/history.yaml |
| Native provenance-check | passed | True | habitatmech:GOLD.363486c188 | Executed 2026-10-14T09:40:14.746048Z to 2026-10-14T09:40:15.227133Z. provenance current: 14 committed inventories, 2 GOLD sources |
| Native verify-corpus | passed | True | habitatmech:GOLD.363486c188 | Executed 2026-10-14T09:40:15.227662Z to 2026-10-14T09:40:28.141881Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| Native validate-causal-all | passed | True | habitatmech:GOLD.363486c188 | Executed 2026-10-14T09:40:28.142448Z to 2026-10-14T09:40:31.707886Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| Native term-requests-check | passed | True | habitatmech:GOLD.363486c188 | Executed 2026-10-14T09:40:31.708412Z to 2026-10-14T09:40:46.178475Z. term-request table is current (109 terms) |
| Native validate-products | passed | True | habitatmech:GOLD.363486c188 | Executed 2026-10-14T09:40:46.179035Z to 2026-10-14T09:41:27.993179Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1177<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2058<br><br>✅ All id↔label pairs correspond. |
| Exact-base authoritative hosted QC | passed | True | habitatmech:GOLD.363486c188 | Freshly verified success at the unchanged captured base; new reports require post-save checks. |
| Original source member reconstruction | unavailable | False | habitatmech:GOLD.363486c188 | Original GOLD and BacDive dumps/member joins unavailable in the ignored-inclusive bounded search; GOLD pages returned 403. Frozen aggregates remain verifiable. |
| Structured expression applicability | not_applicable | False | habitatmech:GOLD.363486c188 | No named gene, regulator, protein or transcriptomics claim; habitat/taxon source identity is not expression-module evidence. |

## Scientific And Domain Assessments

### Habitat identity and strictly broader hierarchy

identity: concern. Targets: habitatmech:GOLD.363486c188.

The GOLD Egg products source names food material and retains its native identity; its only parent FOODON:03530206 is a production process, not a material genus. This GOLD food bin must not be merged automatically with the separate BacDive Egg source. An egg-food candidate requires an ITEM scope assessment before grounding.

### Source claims, units, ranks and triad roles

evidence: supported. Targets: habitatmech:GOLD.363486c188.

Path row 534 collapses nodes 5886/5887/5888 with nine ORGANISM assertions. Bulk row 516 has twenty BIOSAMPLE observations; studies Gs0154236 and Gs0154282 span five and seventeen paths, respectively. No own triad row occurs. CLASS decision row 397 and historical sample row 11 do not establish complete individual review or organism membership.

### Native status, history and optional fields

provenance: supported. Targets: habitatmech:GOLD.363486c188.

Reproduces as UNGROUNDED/SEEDED. Native status follows source ITEM decisions, not this review. No causal graph, environmental parameter, citation, discussion or dataset claim is present; optional omissions do not justify invented biology. No taxon association is asserted.

## Findings

### F1: Food material inherits a production process as strict parent

major / open / confirmed; issue key: egg-products-food-production-process-parent.

The source path contributes FOODON:03530206, whose frozen and pinned definitions describe a process rather than a material genus.

## Recommended Actions And Acceptance Checks

### A1

Add an exact-path exclusion for the immediate GOLD process contribution only. Preserve independent ontology genera, source mint or ontology identity, native status and source attestations.

- Change only the maintained source input; dry seed and inspect an exact canary before full application.
- Preserve source IDs, labels, paths, units, counts and all taxon observations; do not infer original population membership.
- Pass focused regressions, schema, strict, history, labels, provenance, reproduction, site/products and authoritative QC.
- Use a new immutable successor with this issue key and exact previous occurrence for any disposition.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| RECORD | data/habitats/food/egg_products.yaml | supports | Read the entire generated YAML, all assertions and history. |
| RAW | data/raw/; curation/decisions.tsv; data/raw/gold_ecosystem_paths.tsv:534; data/raw/gold_path_biosamples.tsv:516; data/raw/gold_studies.tsv:3931,3966; data/raw/ontology_terms.tsv:10732; curation/decisions.tsv:397 | supports | Structured exact-key rows, with own-source versus parent/child distinction. {"curation/decisions.tsv": [{"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-12", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.363486c188", "notes": "Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched this label by any search route. Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate.", "object_id": "", "object_label": "", "relation": "", "review_depth": "CLASS"}, "row": 397}], "data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0", "canonical_path": "Engineered &gt; Food production &gt; Egg products", "depth": "3", "ecosystem": "Engineered", "ecosystem_category": "Food production", "ecosystem_subtype": "", "ecosystem_type": "Egg products", "gold_node_count": "3", "gold_node_ids": "gold.ecosystem:5886&#124;gold.ecosystem:5887&#124;gold.ecosystem:5888", "leaf_label": "Egg products", "organism_count": "9", "specific_ecosystem": "", "study_count": "0", "total_assertions": "9"}, "row": 534}], "data/raw/gold_path_biosamples.tsv": [{"data": {"biosample_count": "20", "canonical_path": "Engineered &gt; Food production &gt; Egg products", "ecosystem_path_id": "5888"}, "row": 516}], "data/raw/gold_studies.tsv": [{"data": {"path_count": "5", "paths": "Engineered &gt; Food production &gt; Egg products&#124;Engineered &gt; Food production &gt; Fish products&#124;Engineered &gt; Food production &gt; Meat products&#124;Engineered &gt; Food production &gt; Plant products&#124;Engineered &gt; Food production &gt; Spices", "study_gold_id": "Gs0154236"}, "row": 3931}, {"data": {"path_count": "17", "paths": "Engineered &gt; Food production &gt; Baby formula&#124;Engineered &gt; Food production &gt; Beans&#124;Engineered &gt; Food production &gt; Beverages&#124;Engineered &gt; Food production &gt; Bread production&#124;Engineered &gt; Food production &gt; Dairy products&#124;Engineered &gt; Food production &gt; Egg products&#124;Engineered &gt; Food production &gt; Fermented beverages&#124;Engineered &gt; Food production &gt; Fermented food&#124;Engineered &gt; Food production &gt; Food sample&#124;Engineered &gt; Food production &gt; Grains/Grain products&#124;Engineered &gt; Food production &gt; Meat products&#124;Engineered &gt; Food production &gt; Nuts&#124;Engineered &gt; Food production &gt; Pastry&#124;Engineered &gt; Food production &gt; Plant products&#124;Engineered &gt; Food production &gt; Seafood&#124;Engineered &gt; Food production &gt; Spices&#124;Engineered &gt; Food production &gt; Sweets", "study_gold_id": "Gs0154282"}, "row": 3966}], "data/raw/ontology_terms.tsv": [{"data": {"definition": "A planned process involving the rearing, manufacture or distribution of food material.", "deprecated": "", "directly_referenced": "FALSE", "label": "food production", "label_only": "FALSE", "ontology": "FOODON", "synonyms": "production area", "term_id": "FOODON:03530206"}, "row": 10732}]} |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md | supports | Applied strict-superclass, source identity, count-unit, MIxS role, optional-field and ITEM status rules from the local record checklist. |
| TRANSFORM | src/habitatmech/seed.py; src/habitatmech/extract.py; extract_gold; extract_bacdive; ingest_gold; ingest_bacdive; build_document; scripts/extract_gold_biosamples.py; scripts/aggregate_gold_triads.py | supports | GOLD counts outgoing occurrence edges by subject prefix, not proven distinct organisms. Bulk biosamples and study path unions are different inventories. BacDive aggregate strain_count counts source outgoing edges; taxon associations deduplicate strain joins and retain top-25 ranks/candidate_pool. Neither ranking implies characteristic presence. |
| FOODON | https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl; habitatmech:GOLD.363486c188; relevant FoodOn parents and candidate context | supports | Read definitions, typed synonyms, active status and direct named parents in the pinned official RDF/XML. SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf. The GOLD Egg products source names food material and retains its native identity; its only parent FOODON:03530206 is a production process, not a material genus. This GOLD food bin must not be merged automatically with the separate BacDive Egg source. An egg-food candidate requires an ITEM scope assessment before grounding. |
| OLS | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms | supports | Fresh queries resolve all eight ontology IDs used by this cohort as active. Relevant receipts: {"FOODON:03530206": {"accessed_at": "2026-10-14T09:40:23.382263Z", "sha256": "e209164474c7a06365bce7cdbc1f24ff58a283bc848d26221295686958abaf4e", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03530206"}} |
| SEARCH | curation/; history/; research/; conf/; reviews/structured/; reports/yaml_record_review/; data/raw/; tests/; rg --no-ignore --hidden -l -i -F -e Egg products -e Engineered &gt; Food production &gt; Egg products -e FOODON:03530206 -e egg_products -e gold.ecosystem:5886 -e habitatmech:GOLD.363486c188 curation history research conf reviews/structured reports/yaml_record_review data/raw tests | supports | Ignored/hidden-inclusive target ID, label, slug, source mint/path and parent searches plus structured parsing of every raw/curation TSV. No prior individual structured target declaration was found for these eight records; contextual mentions are not absent. Candidate IDs FOODON:03310979, FOODON:03305103 and FOODON:00001053 were separately searched in data/raw, curation, conf, tests and history, including ignored files, with no matches. This is a bounded slice absence, not global ontology absence. |
| AVAILABILITY | conf/sources.yaml | context_only | {"accessed_at": "2026-10-14T09:44:16.995506Z", "command": ["rg", "--no-ignore", "--hidden", "--files", ".", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"], "enumerated_files": 41045, "exit_code": 0, "interpretation": "Ignored files included. Bounded to this repository and the configured kg-microbe data root, not all disks. No exact original member crosswalk is inferred from inventory presence.", "matches": []} |
| GOLD_ACCESS | https://gold.jgi.doe.gov/ | context_only | All 25 retrieved study URLs for this cohort returned HTTP 403; no page contents inferred. {"Gs0111397": {"accessed_at": "2026-10-14T09:41:44.844987Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0111397"}, "Gs0117939": {"accessed_at": "2026-10-14T09:41:44.917192Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0117939"}, "Gs0121311": {"accessed_at": "2026-10-14T09:41:44.946799Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0121311"}, "Gs0127428": {"accessed_at": "2026-10-14T09:41:44.984453Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0127428"}, "Gs0132999": {"accessed_at": "2026-10-14T09:41:45.015413Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0132999"}, "Gs0133059": {"accessed_at": "2026-10-14T09:41:45.135671Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0133059"}, "Gs0133061": {"accessed_at": "2026-10-14T09:41:45.168420Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0133061"}, "Gs0133297": {"accessed_at": "2026-10-14T09:41:45.211877Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0133297"}, "Gs0135057": {"accessed_at": "2026-10-14T09:41:45.248222Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0135057"}, "Gs0144921": {"accessed_at": "2026-10-14T09:41:45.279258Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0144921"}, "Gs0144994": {"accessed_at": "2026-10-14T09:41:45.325246Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0144994"}, "Gs0145069": {"accessed_at": "2026-10-14T09:41:45.359515Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0145069"}, "Gs0150357": {"accessed_at": "2026-10-14T09:41:45.403531Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150357"}, "Gs0150359": {"accessed_at": "2026-10-14T09:41:45.534775Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150359"}, "Gs0150613": {"accessed_at": "2026-10-14T09:41:45.657223Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150613"}, "Gs0150615": {"accessed_at": "2026-10-14T09:41:45.694287Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150615"}, "Gs0153752": {"accessed_at": "2026-10-14T09:41:45.728601Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153752"}, "Gs0153769": {"accessed_at": "2026-10-14T09:41:45.759538Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153769"}, "Gs0153860": {"accessed_at": "2026-10-14T09:41:45.793390Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153860"}, "Gs0153898": {"accessed_at": "2026-10-14T09:41:45.825210Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153898"}, "Gs0154236": {"accessed_at": "2026-10-14T09:41:45.874324Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154236"}, "Gs0154282": {"accessed_at": "2026-10-14T09:41:45.906640Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"}, "Gs0156793": {"accessed_at": "2026-10-14T09:41:45.940030Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0156793"}, "Gs0159152": {"accessed_at": "2026-10-14T09:41:45.985158Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0159152"}, "Gs0161780": {"accessed_at": "2026-10-14T09:41:46.016628Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0161780"}} |
| BASE_QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38541126605 | supports | Fresh gh query verified completed/success at exact captured base 161bd1b665f9c64e8c8ee6aec86f8fc423901632. This merge-candidate run predates new review files; post-save and final PR checks remain required. |

## Limits And Additional Notes

- Same-agent scientific review, not independent approval or corpus-wide certification.
- Original source-member joins remain unavailable; source edges, distinct-strain taxon joins, bulk biosamples and complete-triad samples are distinct observations, never additive or prevalence.
- Pinned FoodOn axioms plus fresh OLS identities do not certify a complete latest ontology refresh.
- No SSSOM/KGX conformance certification or native status promotion follows from this report.
- Exact-base hosted QC predates these review files; post-save archive and publication gates remain required.
- Additional neighboring records, legacy report and sampling table captured at 2026-10-14T09:44:31.623463Z; every originally captured hash was explicitly unchanged. No scientific input was edited for this observation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T095336Z-egg_products
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: Egg products'
started_at: '2026-10-14T09:39:36.440442Z'
finished_at: '2026-10-14T09:53:36.041907Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent participated in repository work; not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
scientific_review: true
verdict: needs_curation
summary: The GOLD Egg products source names food material and retains its native identity;
  its only parent FOODON:03530206 is a production process, not a material genus. This
  GOLD food bin must not be merged automatically with the separate BacDive Egg source.
  An egg-food candidate requires an ITEM scope assessment before grounding.
source:
  git_revision: 161bd1b665f9c64e8c8ee6aec86f8fc423901632
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
    sha256: 45321d0e994aa54fa4b80a943c9ce28e174d9334e59a5bde2a8a02826055106f
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: e31f574d4a1e65f5ff97a7a1b675c4d1179b3e2fe048dc0de9c3e34b9388cf0f
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
    sha256: a28af6ce3b1406cf8fe7d05c66c0a2e1378ea21910c742a281cc9bf81e9ccd86
    role: context
  - path: data/habitats/food/cheese.yaml
    sha256: f86640d44ea126e2890978d8b58042bdae84f0659f6af44f70d0729fb583ce41
    role: context
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
    sha256: af8dd5b264df77bde90811142a57439abb0ca20f2faf0283407b43dd4a179937
    role: context
  - path: data/habitats/food/dairy_food_product.yaml
    sha256: 1010e322454d36e7b64ec217a00dd5d644e881894fdbe49225ce1a30cc1d7171
    role: context
  - path: data/habitats/food/egg_food_product.yaml
    sha256: 456ac28652a419b92c38c7811b43d36e9e3952c278d16f2e0f82f8b1f8892d26
    role: context
  - path: data/habitats/food/egg_products.yaml
    sha256: 615c739f22cf166f0fa9b778f194588df19acc4ae9f38ad880bff664f0f174bb
    role: target
  - path: data/habitats/food/fermented_dairy_products.yaml
    sha256: 9ed59912b37facdd56bb980f312ad3f131d13a6a604f8294574f94477e889ae4
    role: context
  - path: data/habitats/food/fish_products.yaml
    sha256: 5435e216e51f243842916c2e4199123992c81ab166b0746963ffeee71f5253b3
    role: context
  - path: data/habitats/food/mammalian_meat_food_product.yaml
    sha256: fab8fbd8e3352bfe93aefac2761dded407774e918244be3e6b8a87ae45ec27b5
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
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260928T023452Z-fermented_dairy_products.md
    sha256: 97780165ab7bf28e671769c7f4b43d60edb3d5e0d2b96fb7a1143c3a42d5c561
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
targets:
- target_id: habitatmech:GOLD.363486c188
  path: data/habitats/food/egg_products.yaml
  label: Egg products
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
  description: Complete individual record and every contributing source concept.
  selection: Next eight pending food records by path after ignored-inclusive census
    (975/3208 current targets; food 8/61). This bundle assesses exactly one target,
    not the whole cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.363486c188
evidence:
- evidence_id: RECORD
  kind: record_content
  reference: data/habitats/food/egg_products.yaml
  summary: Read the entire generated YAML, all assertions and history.
  accessed_at: '2026-10-14T09:53:36.034169Z'
  support: supports
- evidence_id: RAW
  kind: record_content
  reference: data/raw/; curation/decisions.tsv
  summary: 'Structured exact-key rows, with own-source versus parent/child distinction.
    {"curation/decisions.tsv": [{"data": {"category": "", "curator": "claude-opus-5",
    "date": "2026-08-12", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "",
    "identifier": "habitatmech:GOLD.363486c188", "notes": "Class-level sweep (see
    docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched
    this label by any search route. Whether the concept is a habitat at all was NOT
    assessed, so this is not yet a term-request candidate.", "object_id": "", "object_label":
    "", "relation": "", "review_depth": "CLASS"}, "row": 397}], "data/raw/gold_ecosystem_paths.tsv":
    [{"data": {"biosample_count": "0", "canonical_path": "Engineered > Food production
    > Egg products", "depth": "3", "ecosystem": "Engineered", "ecosystem_category":
    "Food production", "ecosystem_subtype": "", "ecosystem_type": "Egg products",
    "gold_node_count": "3", "gold_node_ids": "gold.ecosystem:5886|gold.ecosystem:5887|gold.ecosystem:5888",
    "leaf_label": "Egg products", "organism_count": "9", "specific_ecosystem": "",
    "study_count": "0", "total_assertions": "9"}, "row": 534}], "data/raw/gold_path_biosamples.tsv":
    [{"data": {"biosample_count": "20", "canonical_path": "Engineered > Food production
    > Egg products", "ecosystem_path_id": "5888"}, "row": 516}], "data/raw/gold_studies.tsv":
    [{"data": {"path_count": "5", "paths": "Engineered > Food production > Egg products|Engineered
    > Food production > Fish products|Engineered > Food production > Meat products|Engineered
    > Food production > Plant products|Engineered > Food production > Spices", "study_gold_id":
    "Gs0154236"}, "row": 3931}, {"data": {"path_count": "17", "paths": "Engineered
    > Food production > Baby formula|Engineered > Food production > Beans|Engineered
    > Food production > Beverages|Engineered > Food production > Bread production|Engineered
    > Food production > Dairy products|Engineered > Food production > Egg products|Engineered
    > Food production > Fermented beverages|Engineered > Food production > Fermented
    food|Engineered > Food production > Food sample|Engineered > Food production >
    Grains/Grain products|Engineered > Food production > Meat products|Engineered
    > Food production > Nuts|Engineered > Food production > Pastry|Engineered > Food
    production > Plant products|Engineered > Food production > Seafood|Engineered
    > Food production > Spices|Engineered > Food production > Sweets", "study_gold_id":
    "Gs0154282"}, "row": 3966}], "data/raw/ontology_terms.tsv": [{"data": {"definition":
    "A planned process involving the rearing, manufacture or distribution of food
    material.", "deprecated": "", "directly_referenced": "FALSE", "label": "food production",
    "label_only": "FALSE", "ontology": "FOODON", "synonyms": "production area", "term_id":
    "FOODON:03530206"}, "row": 10732}]}'
  accessed_at: '2026-10-14T09:53:36.034169Z'
  support: supports
  locator: data/raw/gold_ecosystem_paths.tsv:534; data/raw/gold_path_biosamples.tsv:516;
    data/raw/gold_studies.tsv:3931,3966; data/raw/ontology_terms.tsv:10732; curation/decisions.tsv:397
- evidence_id: RULES
  kind: authority
  reference: docs/CURATION.md; docs/HARMONIZATION.md
  summary: Applied strict-superclass, source identity, count-unit, MIxS role, optional-field
    and ITEM status rules from the local record checklist.
  accessed_at: '2026-10-14T09:53:36.034169Z'
  support: supports
- evidence_id: TRANSFORM
  kind: record_content
  reference: src/habitatmech/seed.py; src/habitatmech/extract.py
  summary: GOLD counts outgoing occurrence edges by subject prefix, not proven distinct
    organisms. Bulk biosamples and study path unions are different inventories. BacDive
    aggregate strain_count counts source outgoing edges; taxon associations deduplicate
    strain joins and retain top-25 ranks/candidate_pool. Neither ranking implies characteristic
    presence.
  accessed_at: '2026-10-14T09:53:36.034169Z'
  support: supports
  locator: extract_gold; extract_bacdive; ingest_gold; ingest_bacdive; build_document;
    scripts/extract_gold_biosamples.py; scripts/aggregate_gold_triads.py
- evidence_id: FOODON
  kind: database
  reference: https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl
  summary: Read definitions, typed synonyms, active status and direct named parents
    in the pinned official RDF/XML. SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf.
    The GOLD Egg products source names food material and retains its native identity;
    its only parent FOODON:03530206 is a production process, not a material genus.
    This GOLD food bin must not be merged automatically with the separate BacDive
    Egg source. An egg-food candidate requires an ITEM scope assessment before grounding.
  accessed_at: '2026-10-14T09:41:41.574451Z'
  support: supports
  locator: habitatmech:GOLD.363486c188; relevant FoodOn parents and candidate context
- evidence_id: OLS
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms
  summary: 'Fresh queries resolve all eight ontology IDs used by this cohort as active.
    Relevant receipts: {"FOODON:03530206": {"accessed_at": "2026-10-14T09:40:23.382263Z",
    "sha256": "e209164474c7a06365bce7cdbc1f24ff58a283bc848d26221295686958abaf4e",
    "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03530206"}}'
  accessed_at: '2026-10-14T09:53:36.034169Z'
  support: supports
- evidence_id: SEARCH
  kind: record_content
  reference: curation/; history/; research/; conf/; reviews/structured/; reports/yaml_record_review/;
    data/raw/; tests/
  summary: Ignored/hidden-inclusive target ID, label, slug, source mint/path and parent
    searches plus structured parsing of every raw/curation TSV. No prior individual
    structured target declaration was found for these eight records; contextual mentions
    are not absent. Candidate IDs FOODON:03310979, FOODON:03305103 and FOODON:00001053
    were separately searched in data/raw, curation, conf, tests and history, including
    ignored files, with no matches. This is a bounded slice absence, not global ontology
    absence.
  accessed_at: '2026-10-14T09:39:50.508181Z'
  support: supports
  locator: rg --no-ignore --hidden -l -i -F -e Egg products -e Engineered > Food production
    > Egg products -e FOODON:03530206 -e egg_products -e gold.ecosystem:5886 -e habitatmech:GOLD.363486c188
    curation history research conf reviews/structured reports/yaml_record_review data/raw
    tests
- evidence_id: AVAILABILITY
  kind: record_content
  reference: conf/sources.yaml
  summary: '{"accessed_at": "2026-10-14T09:44:16.995506Z", "command": ["rg", "--no-ignore",
    "--hidden", "--files", ".", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"],
    "enumerated_files": 41045, "exit_code": 0, "interpretation": "Ignored files included.
    Bounded to this repository and the configured kg-microbe data root, not all disks.
    No exact original member crosswalk is inferred from inventory presence.", "matches":
    []}'
  accessed_at: '2026-10-14T09:53:36.034169Z'
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
  accessed_at: '2026-10-14T09:53:36.034169Z'
  support: context_only
- evidence_id: BASE_QC
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38541126605
  summary: Fresh gh query verified completed/success at exact captured base 161bd1b665f9c64e8c8ee6aec86f8fc423901632.
    This merge-candidate run predates new review files; post-save and final PR checks
    remain required.
  accessed_at: '2026-10-14T09:53:36.034169Z'
  support: supports
checks:
- check_id: C7
  name: Native validate
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.363486c188
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/food/egg_products.yaml
  exit_code: 0
  summary: Executed 2026-10-14T09:40:01.804595Z to 2026-10-14T09:40:03.735833Z. No
    issues found
  scope_note: Target schema, eight-record strict, otherwise full-corpus native checks.
    Label gate retains five configured exceptions and 2058 unsupported-prefix skips;
    not scientific proof.
- check_id: C8
  name: Native validate-strict
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.363486c188
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/food/cheese.yaml data/habitats/food/cold_smoked_fish.yaml data/habitats/food/cooked_blood.yaml
    data/habitats/food/cooked_fish.yaml data/habitats/food/cooked_meat.yaml data/habitats/food/dairy_food_product.yaml
    data/habitats/food/egg_food_product.yaml data/habitats/food/egg_products.yaml
  exit_code: 0
  summary: "Executed 2026-10-14T09:40:03.736366Z to 2026-10-14T09:40:08.470905Z. uv\
    \ run python scripts/validate_strict.py data/habitats/food/cheese.yaml data/habitats/food/cold_smoked_fish.yaml\
    \ data/habitats/food/cooked_blood.yaml data/habitats/food/cooked_fish.yaml data/habitats/food/cooked_meat.yaml\
    \ data/habitats/food/dairy_food_product.yaml data/habitats/food/egg_food_product.yaml\
    \ data/habitats/food/egg_products.yaml\nValidating 8 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      8\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Target schema, eight-record strict, otherwise full-corpus native checks.
    Label gate retains five configured exceptions and 2058 unsupported-prefix skips;
    not scientific proof.
- check_id: C9
  name: Native validate-history
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.363486c188
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  summary: 'Executed 2026-10-14T09:40:08.471507Z to 2026-10-14T09:40:14.745430Z. No
    issues found

    654 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Target schema, eight-record strict, otherwise full-corpus native checks.
    Label gate retains five configured exceptions and 2058 unsupported-prefix skips;
    not scientific proof.
- check_id: C10
  name: Native provenance-check
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.363486c188
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  summary: 'Executed 2026-10-14T09:40:14.746048Z to 2026-10-14T09:40:15.227133Z. provenance
    current: 14 committed inventories, 2 GOLD sources'
  scope_note: Target schema, eight-record strict, otherwise full-corpus native checks.
    Label gate retains five configured exceptions and 2058 unsupported-prefix skips;
    not scientific proof.
- check_id: C11
  name: Native verify-corpus
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.363486c188
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  summary: "Executed 2026-10-14T09:40:15.227662Z to 2026-10-14T09:40:28.141881Z. expected\
    \ 3208 records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing:\
    \ 0\n\ncorpus reproduces exactly from data/raw/"
  scope_note: Target schema, eight-record strict, otherwise full-corpus native checks.
    Label gate retains five configured exceptions and 2058 unsupported-prefix skips;
    not scientific proof.
- check_id: C12
  name: Native validate-causal-all
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.363486c188
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  summary: Executed 2026-10-14T09:40:28.142448Z to 2026-10-14T09:40:31.707886Z. validated
    32 causal-graph curation file(s) with 32 graph(s)
  scope_note: Target schema, eight-record strict, otherwise full-corpus native checks.
    Label gate retains five configured exceptions and 2058 unsupported-prefix skips;
    not scientific proof.
- check_id: C13
  name: Native term-requests-check
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.363486c188
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  summary: Executed 2026-10-14T09:40:31.708412Z to 2026-10-14T09:40:46.178475Z. term-request
    table is current (109 terms)
  scope_note: Target schema, eight-record strict, otherwise full-corpus native checks.
    Label gate retains five configured exceptions and 2058 unsupported-prefix skips;
    not scientific proof.
- check_id: C14
  name: Native validate-products
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.363486c188
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  summary: "Executed 2026-10-14T09:40:46.179035Z to 2026-10-14T09:41:27.993179Z. id↔label\
    \ correspondence summary:\n          OK_CANONICAL: 1177\n            OK_SYNONYM:\
    \ 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2058\n\n✅ All id↔label\
    \ pairs correspond."
  scope_note: Target schema, eight-record strict, otherwise full-corpus native checks.
    Label gate retains five configured exceptions and 2058 unsupported-prefix skips;
    not scientific proof.
- check_id: QC
  name: Exact-base authoritative hosted QC
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.363486c188
  command: gh run view 38541126605 --json status,conclusion,headSha,url
  exit_code: 0
  summary: Freshly verified success at the unchanged captured base; new reports require
    post-save checks.
  evidence_ids:
  - BASE_QC
- check_id: MEMBERS
  name: Original source member reconstruction
  status: unavailable
  required: false
  target_ids:
  - habitatmech:GOLD.363486c188
  summary: Original GOLD and BacDive dumps/member joins unavailable in the ignored-inclusive
    bounded search; GOLD pages returned 403. Frozen aggregates remain verifiable.
  evidence_ids:
  - AVAILABILITY
  - GOLD_ACCESS
- check_id: IMODULON
  name: Structured expression applicability
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.363486c188
  summary: No named gene, regulator, protein or transcriptomics claim; habitat/taxon
    source identity is not expression-module evidence.
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Habitat identity and strictly broader hierarchy
  outcome: concern
  target_ids:
  - habitatmech:GOLD.363486c188
  evidence_ids:
  - RECORD
  - RAW
  - RULES
  - FOODON
  - TRANSFORM
  - SEARCH
  summary: The GOLD Egg products source names food material and retains its native
    identity; its only parent FOODON:03530206 is a production process, not a material
    genus. This GOLD food bin must not be merged automatically with the separate BacDive
    Egg source. An egg-food candidate requires an ITEM scope assessment before grounding.
- assessment_id: SCIENCE
  area: evidence
  topic: Source claims, units, ranks and triad roles
  outcome: supported
  target_ids:
  - habitatmech:GOLD.363486c188
  evidence_ids:
  - RECORD
  - RAW
  - RULES
  - FOODON
  - TRANSFORM
  - SEARCH
  summary: Path row 534 collapses nodes 5886/5887/5888 with nine ORGANISM assertions.
    Bulk row 516 has twenty BIOSAMPLE observations; studies Gs0154236 and Gs0154282
    span five and seventeen paths, respectively. No own triad row occurs. CLASS decision
    row 397 and historical sample row 11 do not establish complete individual review
    or organism membership.
- assessment_id: STATUS
  area: provenance
  topic: Native status, history and optional fields
  outcome: supported
  target_ids:
  - habitatmech:GOLD.363486c188
  evidence_ids:
  - RECORD
  - RAW
  - RULES
  - FOODON
  - TRANSFORM
  - SEARCH
  summary: Reproduces as UNGROUNDED/SEEDED. Native status follows source ITEM decisions,
    not this review. No causal graph, environmental parameter, citation, discussion
    or dataset claim is present; optional omissions do not justify invented biology.
    No taxon association is asserted.
findings:
- finding_id: F1
  issue_key: egg-products-food-production-process-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Food material inherits a production process as strict parent
  description: The source path contributes FOODON:03530206, whose frozen and pinned
    definitions describe a process rather than a material genus.
  target_ids:
  - habitatmech:GOLD.363486c188
  field_paths:
  - parent_habitats
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input owner; generated records are read-only
  evidence_ids:
  - RECORD
  - RAW
  - RULES
  - FOODON
  rule_id: 'docs/CURATION.md: identity and strict parent rules'
  native_severity: major
  normalization_reason: A materially unsupported strict superclass is a major semantic
    defect, not style.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.363486c188
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input owner; generated records are read-only
  description: Add an exact-path exclusion for the immediate GOLD process contribution
    only. Preserve independent ontology genera, source mint or ontology identity,
    native status and source attestations.
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Change only the maintained source input; dry seed and inspect an exact canary
    before full application.
  - Preserve source IDs, labels, paths, units, counts and all taxon observations;
    do not infer original population membership.
  - Pass focused regressions, schema, strict, history, labels, provenance, reproduction,
    site/products and authoritative QC.
  - Use a new immutable successor with this issue key and exact previous occurrence
    for any disposition.
limitations:
- Same-agent scientific review, not independent approval or corpus-wide certification.
- Original source-member joins remain unavailable; source edges, distinct-strain taxon
  joins, bulk biosamples and complete-triad samples are distinct observations, never
  additive or prevalence.
- Pinned FoodOn axioms plus fresh OLS identities do not certify a complete latest
  ontology refresh.
- No SSSOM/KGX conformance certification or native status promotion follows from this
  report.
- Exact-base hosted QC predates these review files; post-save archive and publication
  gates remain required.
notes:
- Additional neighboring records, legacy report and sampling table captured at 2026-10-14T09:44:31.623463Z;
  every originally captured hash was explicitly unchanged. No scientific input was
  edited for this observation.
tags:
- habitatmech
- record-review
- food
```
