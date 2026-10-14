# Scientific record review: cereal grain food product

- Review: 20261014T082213Z-cereal_grain_food_product
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T08:06:46.060702Z
- Finished UTC: 2026-10-14T08:22:13.686859Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The cereal-food family is supported by the source path and is not the mineral-particle homonym rejected in prior curation. FoodOn places unprocessed cereal grain under cereal grain under this food-product class, so the label does not itself exclude raw grain. Retain conservative CLOSE and RELATED source scope; reject only the false process parent. Absence of an optional textual ontology definition is not a required-field defect.

## Scope And Provenance

Complete individual record and all contributing source concepts.

Selection: First eight alphabetical food records were selected after ignored-inclusive census: 967/3208 current records reviewed and food 0/61. This bundle judges exactly one target, not the entire cohort or corpus.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b44399980b2f188379de618fda01b46d1b691ef6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| FOODON:00001093 | data/habitats/food/cereal_grain_food_product.yaml | generated | cereal grain food product |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | FOODON:00001093 | Executed 2026-10-14T08:07:15.562280Z to 2026-10-14T08:07:18.187711Z. No issues found |
| Native validate-strict | passed | True | FOODON:00001093 | Executed 2026-10-14T08:07:18.188253Z to 2026-10-14T08:07:23.492140Z. uv run python scripts/validate_strict.py data/habitats/food/baby_formula.yaml data/habitats/food/bean.yaml data/habitats/food/beef_chop.yaml data/habitats/food/beverage.yaml data/habitats/food/bread.yaml data/habitats/food/bread_food_product.yaml data/habitats/food/butchery_cut_of_beef.yaml data/habitats/food/cereal_grain_food_product.yaml<br>Validating 8 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      8<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| Native validate-history | passed | True | FOODON:00001093 | Executed 2026-10-14T08:07:23.492966Z to 2026-10-14T08:07:31.608042Z. No issues found<br>648 history record(s) valid against src/habitatmech/schema/history.yaml |
| Native provenance-check | passed | True | FOODON:00001093 | Executed 2026-10-14T08:07:31.608856Z to 2026-10-14T08:07:32.349189Z. provenance current: 14 committed inventories, 2 GOLD sources |
| Native verify-corpus | passed | True | FOODON:00001093 | Executed 2026-10-14T08:07:32.349950Z to 2026-10-14T08:07:53.711319Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| Native validate-causal-all | passed | True | FOODON:00001093 | Executed 2026-10-14T08:07:53.711917Z to 2026-10-14T08:07:57.768575Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| Native term-requests-check | passed | True | FOODON:00001093 | Executed 2026-10-14T08:07:57.769133Z to 2026-10-14T08:08:13.255286Z. term-request table is current (109 terms) |
| Native validate-products | passed | True | FOODON:00001093 | Executed 2026-10-14T08:08:13.255848Z to 2026-10-14T08:09:35.480899Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1178<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2057<br><br>✅ All id↔label pairs correspond. |
| Exact-base hosted authoritative QC | passed | True | FOODON:00001093 | Confirmed success on the captured base with unchanged scientific inputs; post-save contract and PR checks remain required. |
| Original GOLD member reconstruction | unavailable | False | FOODON:00001093 | Original GOLD node/edge dumps, bulk workbook and API per-sample triads were not found by ignored-inclusive filename search in this repository and configured kg-microbe/data root. Study webpages returned HTTP 403. No original full membership is claimed. |
| Structured expression applicability | not_applicable | False | FOODON:00001093 | No named gene, taxon association, regulator, expression module or transcriptomics dataset is asserted. No taxonomy lookup is needed for these records. |

## Scientific And Domain Assessments

### Entity, grounding and strict hierarchy

identity: concern. Targets: FOODON:00001093.

The cereal-food family is supported by the source path and is not the mineral-particle homonym rejected in prior curation. FoodOn places unprocessed cereal grain under cereal grain under this food-product class, so the label does not itself exclude raw grain. Retain conservative CLOSE and RELATED source scope; reject only the false process parent. Absence of an optional textual ontology definition is not a required-field defect.

### Attestation units, source scope and MIxS evidence

evidence: supported. Targets: FOODON:00001093.

Raw row 1299 collapses nodes 5927/5928/5929 with zero frozen organism assertions and correctly omits count/unit. Bulk row 296 has 71 BIOSAMPLE observations; Gs0154282 has seventeen paths. The September history explains the particle correction, but research prose about storage, water activity and microbial ecology is not adopted as record evidence.

### Native status and optional claims

provenance: supported. Targets: FOODON:00001093.

The complete record reproduces as CLOSE/REVIEWED. Reviewed status follows contributing ITEM decisions, not this review. No taxa, causal graph, environmental parameters, citations, discussions or datasets are asserted; these optional omissions do not justify invented biology. Food category is a coarse bucket, not a mechanism claim.

## Findings

### F1: Food material inherits a food-production process as a strict parent

major / open / confirmed; issue key: cereal-grain-food-product-food-production-process-parent.

The record emits FOODON:03530206 from the GOLD path. Both frozen and pinned definitions make it a planned process, not a broader food material. The source hierarchy supplies production context, not is-a evidence.

## Recommended Actions And Acceptance Checks

### A1

Exclude only the exact GOLD path contribution with its expected parent ID, retaining independent ontology parents and every source observation. For Bread production, reassess after its identity correction. Update the beverage regression that currently expects the invalid edge.

- Inspect an exact canary; preserve raw counts/units, IDs, paths and existing history. No manual generated-file edits.
- Pass schema, labels, provenance, reproduction, regression tests, history, generated site and full QC; regenerate affected semantic products.
- A disposition requires a new immutable observation retaining this issue key and exact previous occurrence.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| RECORD | data/habitats/food/cereal_grain_food_product.yaml | supports | Read the complete YAML, all fields and history; no projection substitutes for the record. |
| RAW | data/raw/; curation/decisions.tsv; data/raw/gold_ecosystem_paths.tsv:1299; data/raw/gold_path_biosamples.tsv:296; data/raw/gold_studies.tsv:3966; curation/decisions.tsv:1089 | supports | Inspected exact-key structured rows, distinguishing parent and child matches from the own source path. {"curation/decisions.tsv": [{"data": {"category": null, "curator": "codex-gpt-5", "date": "2026-09-08", "decision": "GROUND", "grounding_status": "CLOSE", "identifier": "habitatmech:GOLD.c25f588dad", "notes": "Definition research for Grains/Grain products found FOODON:00001093 'cereal grain food product' in the vendored slice and confirmed it mirrors the reviewed GOLD Dairy products -&gt; FOODON:00001256 'dairy food product' pattern. The prior CONFIRM_UNGROUNDED decision had only rejected ENVO:01003002 'particle' via a mineralogical grain synonym; CLOSE is used because the GOLD label bundles raw grain with derived products while FOODON:00001093 is food-product scoped and has no textual definition.", "object_id": "FOODON:00001093", "object_label": "cereal grain food product", "relation": null, "review_depth": "ITEM"}, "row": 1089}], "data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0", "canonical_path": "Engineered &gt; Food production &gt; Grains/Grain products", "depth": "3", "ecosystem": "Engineered", "ecosystem_category": "Food production", "ecosystem_subtype": "", "ecosystem_type": "Grains/Grain products", "gold_node_count": "3", "gold_node_ids": "gold.ecosystem:5927&#124;gold.ecosystem:5928&#124;gold.ecosystem:5929", "leaf_label": "Grains/Grain products", "organism_count": "0", "specific_ecosystem": "", "study_count": "0", "total_assertions": "0"}, "row": 1299}], "data/raw/gold_path_biosamples.tsv": [{"data": {"biosample_count": "71", "canonical_path": "Engineered &gt; Food production &gt; Grains/Grain products", "ecosystem_path_id": "5929"}, "row": 296}], "data/raw/gold_studies.tsv": [{"data": {"path_count": "17", "paths": "Engineered &gt; Food production &gt; Baby formula&#124;Engineered &gt; Food production &gt; Beans&#124;Engineered &gt; Food production &gt; Beverages&#124;Engineered &gt; Food production &gt; Bread production&#124;Engineered &gt; Food production &gt; Dairy products&#124;Engineered &gt; Food production &gt; Egg products&#124;Engineered &gt; Food production &gt; Fermented beverages&#124;Engineered &gt; Food production &gt; Fermented food&#124;Engineered &gt; Food production &gt; Food sample&#124;Engineered &gt; Food production &gt; Grains/Grain products&#124;Engineered &gt; Food production &gt; Meat products&#124;Engineered &gt; Food production &gt; Nuts&#124;Engineered &gt; Food production &gt; Pastry&#124;Engineered &gt; Food production &gt; Plant products&#124;Engineered &gt; Food production &gt; Seafood&#124;Engineered &gt; Food production &gt; Spices&#124;Engineered &gt; Food production &gt; Sweets", "study_gold_id": "Gs0154282"}, "row": 3966}]} |
| RULES | docs/CURATION.md | supports | Applied identity, strict-superclass, MIxS roles, source units, optional-field and ITEM status rules with the local checklist. |
| TRANSFORM | src/habitatmech/seed.py; extract.py:extract_gold; seed.py:ingest_gold; scripts/extract_gold_biosamples.py:extract; scripts/aggregate_gold_triads.py:aggregate | supports | extract_gold counts occurs_in edges by subject prefix and collapses path nodes, not proven unique organisms. ingest_gold emits a positive ORGANISM count only and resolves immediate source-path parents separately. Bulk biosample rows and study path unions use a separate export; triads aggregate complete annotations only. |
| FOODON | https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl; FOODON:00001093 and all FoodOn parents; raw-chop, formula and grain candidate context | supports | Inspected typed synonyms, definitions and named parents in pinned official RDF/XML; SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf. This is a pinned ontology check, not an unbounded latest-release refresh. The cereal-food family is supported by the source path and is not the mineral-particle homonym rejected in prior curation. FoodOn places unprocessed cereal grain under cereal grain under this food-product class, so the label does not itself exclude raw grain. Retain conservative CLOSE and RELATED source scope; reject only the false process parent. Absence of an optional textual ontology definition is not a required-field defect. |
| OLS | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms | supports | Fresh OLS requests resolved all eighteen FoodOn identifiers used by the eight targets and their parents as active. Typed synonym scope is taken from OWL, not the flat OLS synonym list. Target-relevant receipts: {"FOODON:00001093": {"accessed_at": "2026-10-14T08:07:14.559422Z", "sha256": "1c7d93ad233daef9159063f78a26dc155da5e1059388ca9edeab12297aa9bbbc", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001093"}, "FOODON:00001173": {"accessed_at": "2026-10-14T08:07:15.532479Z", "sha256": "7a1b3ca9d711e211bbcb566979dc075b078c4a6473a4945f922d73a0791a874a", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001173"}, "FOODON:03530206": {"accessed_at": "2026-10-14T08:07:28.251120Z", "sha256": "e209164474c7a06365bce7cdbc1f24ff58a283bc848d26221295686958abaf4e", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03530206"}} |
| SEARCH | curation/; history/; research/; conf/; reviews/structured/; reports/yaml_record_review/; data/raw/; tests/; rg --no-ignore --hidden -l -i -F -e Engineered &gt; Food production &gt; Grains/Grain products -e FOODON:00001093 -e FOODON:00001173 -e FOODON:03530206 -e Grains/Grain products -e cereal grain food product -e cereal_grain_food_product -e gold.ecosystem:5927 -e habitatmech:GOLD.c25f588dad curation history research conf reviews/structured reports/yaml_record_review data/raw tests | supports | Ignored/hidden-inclusive rg searched target ID, label, slug, source path, source mint and parents; structured parsing covered every raw and curation TSV. No existing structured target declaration for these eight targets was found. Candidate infant-formula/raw-chop IDs and labels were also searched in data/raw, curation, conf, tests and history with no match; no global ontology absence is claimed. |
| GOLD_ACCESS | https://gold.jgi.doe.gov/ | context_only | Direct retrieval of the six relevant study pages returned HTTP 403; no study contents were inferred. Receipts: {"Gs0142293": {"accessed_at": "2026-10-14T08:11:39.570835Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0142293"}, "Gs0150300": {"accessed_at": "2026-10-14T08:11:39.785085Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150300"}, "Gs0150660": {"accessed_at": "2026-10-14T08:11:39.830086Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150660"}, "Gs0153740": {"accessed_at": "2026-10-14T08:11:39.869363Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153740"}, "Gs0153816": {"accessed_at": "2026-10-14T08:11:39.925031Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153816"}, "Gs0154282": {"accessed_at": "2026-10-14T08:11:39.962586Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"}} |
| BASE_QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38530055451 | supports | Queried headSha/status/conclusion: success on exact unchanged scientific-input base b44399980b2f188379de618fda01b46d1b691ef6. This hosted QC predates the new review files. |

## Limits And Additional Notes

- Same-agent review, not independent approval or a full-corpus scientific pass.
- Original GOLD membership and sample-study joins were unavailable. Frozen edge counts, later bulk biosamples and complete-triad sample counts are distinct observations, never summed or interpreted as prevalence.
- FoodOn OWL was pinned, with fresh OLS identity checks; this does not certify latest-release hierarchy equivalence or an ontology refresh.
- No SSSOM/KGX conformance certification, curation edit or native status promotion is performed by this observation. Original review bundles remain immutable.
- Exact-base hosted QC does not validate subsequently saved review files; post-save archive and publication checks remain required.
- Additional context inputs were captured before finalization; every original input hash and Git base was explicitly proved unchanged. Candidate searches included ignored files. Neighbor-record defects were not transferred to valid child ontology edges.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T082213Z-cereal_grain_food_product
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: cereal grain food product'
started_at: '2026-10-14T08:06:46.060702Z'
finished_at: '2026-10-14T08:22:13.686859Z'
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
summary: The cereal-food family is supported by the source path and is not the mineral-particle
  homonym rejected in prior curation. FoodOn places unprocessed cereal grain under
  cereal grain under this food-product class, so the label does not itself exclude
  raw grain. Retain conservative CLOSE and RELATED source scope; reject only the false
  process parent. Absence of an optional textual ontology definition is not a required-field
  defect.
source:
  git_revision: b44399980b2f188379de618fda01b46d1b691ef6
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
    sha256: eb82cec48508912622b452ae78bb1ad199c93cb0591ce534bb8f25273da4e220
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 27ba9a5fe34ef636e764af44c6a43f025e86d59fc25634e24d9c179a18322808
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
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/food/baby_formula.yaml
    sha256: f9a12748f7eab347ab0ceea90b580f43ec397c312295c4627405b68c679802ba
    role: context
  - path: data/habitats/food/bean.yaml
    sha256: 68b91f8ce044adf57e13bc286b8e69c4519a7d077cf5e74e2975b5b6dd90a63e
    role: context
  - path: data/habitats/food/beef_chop.yaml
    sha256: f7d6eaf604e279b96430fd8213205c5733c52a381876140b744c7c863974e834
    role: context
  - path: data/habitats/food/beverage.yaml
    sha256: 85b0e4a6ad366a1b725f617e2ec99d188efc552b6493cd75a9ec3aae4160fa12
    role: context
  - path: data/habitats/food/bread.yaml
    sha256: 109e90fe77a77741c93ff5c4fc9c753dcd16c987c3cc527c36f544944ce719bf
    role: context
  - path: data/habitats/food/bread_food_product.yaml
    sha256: 246d9e3628f616feda38d840905daaa948ad8745cad69df343ff3266b4690520
    role: context
  - path: data/habitats/food/butchery_cut_of_beef.yaml
    sha256: 837d45cc3f7fb377199b254fffe21a366d1312b13e5fd2232b987c136ffc33bb
    role: context
  - path: data/habitats/food/cereal_grain_food_product.yaml
    sha256: f59dc568143d6f5458a65824c0633456a21af78f25e0ed0c1288f2e3ae91a4d9
    role: target
  - path: data/habitats/food/food_production.yaml
    sha256: b0fce7af2cc321a0979ce4d3bfec5e2d4383410ae8e62172b006073afb783ab7
    role: context
  - path: data/habitats/food/mammalian_meat_food_product.yaml
    sha256: fab8fbd8e3352bfe93aefac2761dded407774e918244be3e6b8a87ae45ec27b5
    role: context
  - path: data/habitats/food/raw_meat.yaml
    sha256: e45e1d71102c32bc410ff08a2175fcd645de883da0d4682f8acfaf0b04b0564d
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
  - path: history/mappings/foodon_beverage_pastry_scope/2026-10-08T034738Z-codex-4bb239.yaml
    sha256: 3b55dd188863916f4fda7a1813547e08473f124cbb0188aba284e700a1d48ae9
    role: context
  - path: history/mappings/grains_grain_products/2026-09-09T030500Z-claude-code-1b8d5a.yaml
    sha256: fd799709156f489929dfdb3d7cc3cc4dc779a51aa91665b7e85432941391b2c5
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260929T030651Z-food_production.md
    sha256: 8e8b30e0bfe4849c96aec02bec10e0ef0970da582375e62f1068e9446a1cae4a
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
  - path: tests/test_ontology_labels.py
    sha256: 8411f5256681f96aaa8faa469db5063fb6fe6f2706228c8f8c7c378d5c6d1512
    role: context
targets:
- target_id: FOODON:00001093
  path: data/habitats/food/cereal_grain_food_product.yaml
  label: cereal grain food product
  kind: generated
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_path_biosamples.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_path_triads.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_studies.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained curation or source owner; never hand-edit generated YAML
  record_class: HabitatRecord
scope:
  description: Complete individual record and all contributing source concepts.
  selection: 'First eight alphabetical food records were selected after ignored-inclusive
    census: 967/3208 current records reviewed and food 0/61. This bundle judges exactly
    one target, not the entire cohort or corpus.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - FOODON:00001093
checks:
- check_id: C7
  name: Native validate
  status: passed
  required: true
  target_ids:
  - FOODON:00001093
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/food/cereal_grain_food_product.yaml
  exit_code: 0
  summary: Executed 2026-10-14T08:07:15.562280Z to 2026-10-14T08:07:18.187711Z. No
    issues found
  scope_note: Target-specific schema, eight-record strict, otherwise full-corpus native
    gates. Label correspondence retains five accepted exceptions and 2057 unsupported-prefix
    skips; deterministic success is not semantic proof.
- check_id: C8
  name: Native validate-strict
  status: passed
  required: true
  target_ids:
  - FOODON:00001093
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/food/baby_formula.yaml data/habitats/food/bean.yaml data/habitats/food/beef_chop.yaml
    data/habitats/food/beverage.yaml data/habitats/food/bread.yaml data/habitats/food/bread_food_product.yaml
    data/habitats/food/butchery_cut_of_beef.yaml data/habitats/food/cereal_grain_food_product.yaml
  exit_code: 0
  summary: "Executed 2026-10-14T08:07:18.188253Z to 2026-10-14T08:07:23.492140Z. uv\
    \ run python scripts/validate_strict.py data/habitats/food/baby_formula.yaml data/habitats/food/bean.yaml\
    \ data/habitats/food/beef_chop.yaml data/habitats/food/beverage.yaml data/habitats/food/bread.yaml\
    \ data/habitats/food/bread_food_product.yaml data/habitats/food/butchery_cut_of_beef.yaml\
    \ data/habitats/food/cereal_grain_food_product.yaml\nValidating 8 files with 15\
    \ workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      8\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Target-specific schema, eight-record strict, otherwise full-corpus native
    gates. Label correspondence retains five accepted exceptions and 2057 unsupported-prefix
    skips; deterministic success is not semantic proof.
- check_id: C9
  name: Native validate-history
  status: passed
  required: true
  target_ids:
  - FOODON:00001093
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  summary: 'Executed 2026-10-14T08:07:23.492966Z to 2026-10-14T08:07:31.608042Z. No
    issues found

    648 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Target-specific schema, eight-record strict, otherwise full-corpus native
    gates. Label correspondence retains five accepted exceptions and 2057 unsupported-prefix
    skips; deterministic success is not semantic proof.
- check_id: C10
  name: Native provenance-check
  status: passed
  required: true
  target_ids:
  - FOODON:00001093
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  summary: 'Executed 2026-10-14T08:07:31.608856Z to 2026-10-14T08:07:32.349189Z. provenance
    current: 14 committed inventories, 2 GOLD sources'
  scope_note: Target-specific schema, eight-record strict, otherwise full-corpus native
    gates. Label correspondence retains five accepted exceptions and 2057 unsupported-prefix
    skips; deterministic success is not semantic proof.
- check_id: C11
  name: Native verify-corpus
  status: passed
  required: true
  target_ids:
  - FOODON:00001093
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  summary: "Executed 2026-10-14T08:07:32.349950Z to 2026-10-14T08:07:53.711319Z. expected\
    \ 3208 records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing:\
    \ 0\n\ncorpus reproduces exactly from data/raw/"
  scope_note: Target-specific schema, eight-record strict, otherwise full-corpus native
    gates. Label correspondence retains five accepted exceptions and 2057 unsupported-prefix
    skips; deterministic success is not semantic proof.
- check_id: C12
  name: Native validate-causal-all
  status: passed
  required: true
  target_ids:
  - FOODON:00001093
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  summary: Executed 2026-10-14T08:07:53.711917Z to 2026-10-14T08:07:57.768575Z. validated
    32 causal-graph curation file(s) with 32 graph(s)
  scope_note: Target-specific schema, eight-record strict, otherwise full-corpus native
    gates. Label correspondence retains five accepted exceptions and 2057 unsupported-prefix
    skips; deterministic success is not semantic proof.
- check_id: C13
  name: Native term-requests-check
  status: passed
  required: true
  target_ids:
  - FOODON:00001093
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  summary: Executed 2026-10-14T08:07:57.769133Z to 2026-10-14T08:08:13.255286Z. term-request
    table is current (109 terms)
  scope_note: Target-specific schema, eight-record strict, otherwise full-corpus native
    gates. Label correspondence retains five accepted exceptions and 2057 unsupported-prefix
    skips; deterministic success is not semantic proof.
- check_id: C14
  name: Native validate-products
  status: passed
  required: true
  target_ids:
  - FOODON:00001093
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  summary: "Executed 2026-10-14T08:08:13.255848Z to 2026-10-14T08:09:35.480899Z. id↔label\
    \ correspondence summary:\n          OK_CANONICAL: 1178\n            OK_SYNONYM:\
    \ 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2057\n\n✅ All id↔label\
    \ pairs correspond."
  scope_note: Target-specific schema, eight-record strict, otherwise full-corpus native
    gates. Label correspondence retains five accepted exceptions and 2057 unsupported-prefix
    skips; deterministic success is not semantic proof.
- check_id: QC
  name: Exact-base hosted authoritative QC
  status: passed
  required: true
  target_ids:
  - FOODON:00001093
  command: gh run view 38530055451 --json headSha,status,conclusion,url
  exit_code: 0
  summary: Confirmed success on the captured base with unchanged scientific inputs;
    post-save contract and PR checks remain required.
  evidence_ids:
  - BASE_QC
- check_id: MEMBERS
  name: Original GOLD member reconstruction
  status: unavailable
  required: false
  target_ids:
  - FOODON:00001093
  summary: Original GOLD node/edge dumps, bulk workbook and API per-sample triads
    were not found by ignored-inclusive filename search in this repository and configured
    kg-microbe/data root. Study webpages returned HTTP 403. No original full membership
    is claimed.
  evidence_ids:
  - GOLD_ACCESS
- check_id: IMODULON
  name: Structured expression applicability
  status: not_applicable
  required: false
  target_ids:
  - FOODON:00001093
  summary: No named gene, taxon association, regulator, expression module or transcriptomics
    dataset is asserted. No taxonomy lookup is needed for these records.
evidence:
- evidence_id: RECORD
  kind: record_content
  reference: data/habitats/food/cereal_grain_food_product.yaml
  summary: Read the complete YAML, all fields and history; no projection substitutes
    for the record.
  accessed_at: '2026-10-14T08:22:13.686117Z'
  support: supports
- evidence_id: RAW
  kind: record_content
  reference: data/raw/; curation/decisions.tsv
  summary: 'Inspected exact-key structured rows, distinguishing parent and child matches
    from the own source path. {"curation/decisions.tsv": [{"data": {"category": null,
    "curator": "codex-gpt-5", "date": "2026-09-08", "decision": "GROUND", "grounding_status":
    "CLOSE", "identifier": "habitatmech:GOLD.c25f588dad", "notes": "Definition research
    for Grains/Grain products found FOODON:00001093 ''cereal grain food product''
    in the vendored slice and confirmed it mirrors the reviewed GOLD Dairy products
    -> FOODON:00001256 ''dairy food product'' pattern. The prior CONFIRM_UNGROUNDED
    decision had only rejected ENVO:01003002 ''particle'' via a mineralogical grain
    synonym; CLOSE is used because the GOLD label bundles raw grain with derived products
    while FOODON:00001093 is food-product scoped and has no textual definition.",
    "object_id": "FOODON:00001093", "object_label": "cereal grain food product", "relation":
    null, "review_depth": "ITEM"}, "row": 1089}], "data/raw/gold_ecosystem_paths.tsv":
    [{"data": {"biosample_count": "0", "canonical_path": "Engineered > Food production
    > Grains/Grain products", "depth": "3", "ecosystem": "Engineered", "ecosystem_category":
    "Food production", "ecosystem_subtype": "", "ecosystem_type": "Grains/Grain products",
    "gold_node_count": "3", "gold_node_ids": "gold.ecosystem:5927|gold.ecosystem:5928|gold.ecosystem:5929",
    "leaf_label": "Grains/Grain products", "organism_count": "0", "specific_ecosystem":
    "", "study_count": "0", "total_assertions": "0"}, "row": 1299}], "data/raw/gold_path_biosamples.tsv":
    [{"data": {"biosample_count": "71", "canonical_path": "Engineered > Food production
    > Grains/Grain products", "ecosystem_path_id": "5929"}, "row": 296}], "data/raw/gold_studies.tsv":
    [{"data": {"path_count": "17", "paths": "Engineered > Food production > Baby formula|Engineered
    > Food production > Beans|Engineered > Food production > Beverages|Engineered
    > Food production > Bread production|Engineered > Food production > Dairy products|Engineered
    > Food production > Egg products|Engineered > Food production > Fermented beverages|Engineered
    > Food production > Fermented food|Engineered > Food production > Food sample|Engineered
    > Food production > Grains/Grain products|Engineered > Food production > Meat
    products|Engineered > Food production > Nuts|Engineered > Food production > Pastry|Engineered
    > Food production > Plant products|Engineered > Food production > Seafood|Engineered
    > Food production > Spices|Engineered > Food production > Sweets", "study_gold_id":
    "Gs0154282"}, "row": 3966}]}'
  accessed_at: '2026-10-14T08:22:13.686117Z'
  support: supports
  locator: data/raw/gold_ecosystem_paths.tsv:1299; data/raw/gold_path_biosamples.tsv:296;
    data/raw/gold_studies.tsv:3966; curation/decisions.tsv:1089
- evidence_id: RULES
  kind: authority
  reference: docs/CURATION.md
  summary: Applied identity, strict-superclass, MIxS roles, source units, optional-field
    and ITEM status rules with the local checklist.
  accessed_at: '2026-10-14T08:22:13.686117Z'
  support: supports
- evidence_id: TRANSFORM
  kind: record_content
  reference: src/habitatmech/seed.py
  summary: extract_gold counts occurs_in edges by subject prefix and collapses path
    nodes, not proven unique organisms. ingest_gold emits a positive ORGANISM count
    only and resolves immediate source-path parents separately. Bulk biosample rows
    and study path unions use a separate export; triads aggregate complete annotations
    only.
  accessed_at: '2026-10-14T08:22:13.686117Z'
  support: supports
  locator: extract.py:extract_gold; seed.py:ingest_gold; scripts/extract_gold_biosamples.py:extract;
    scripts/aggregate_gold_triads.py:aggregate
- evidence_id: FOODON
  kind: database
  reference: https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl
  summary: Inspected typed synonyms, definitions and named parents in pinned official
    RDF/XML; SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf.
    This is a pinned ontology check, not an unbounded latest-release refresh. The
    cereal-food family is supported by the source path and is not the mineral-particle
    homonym rejected in prior curation. FoodOn places unprocessed cereal grain under
    cereal grain under this food-product class, so the label does not itself exclude
    raw grain. Retain conservative CLOSE and RELATED source scope; reject only the
    false process parent. Absence of an optional textual ontology definition is not
    a required-field defect.
  accessed_at: '2026-10-14T08:11:36.247630Z'
  support: supports
  locator: FOODON:00001093 and all FoodOn parents; raw-chop, formula and grain candidate
    context
- evidence_id: OLS
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms
  summary: 'Fresh OLS requests resolved all eighteen FoodOn identifiers used by the
    eight targets and their parents as active. Typed synonym scope is taken from OWL,
    not the flat OLS synonym list. Target-relevant receipts: {"FOODON:00001093": {"accessed_at":
    "2026-10-14T08:07:14.559422Z", "sha256": "1c7d93ad233daef9159063f78a26dc155da5e1059388ca9edeab12297aa9bbbc",
    "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001093"},
    "FOODON:00001173": {"accessed_at": "2026-10-14T08:07:15.532479Z", "sha256": "7a1b3ca9d711e211bbcb566979dc075b078c4a6473a4945f922d73a0791a874a",
    "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001173"},
    "FOODON:03530206": {"accessed_at": "2026-10-14T08:07:28.251120Z", "sha256": "e209164474c7a06365bce7cdbc1f24ff58a283bc848d26221295686958abaf4e",
    "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03530206"}}'
  accessed_at: '2026-10-14T08:22:13.686117Z'
  support: supports
- evidence_id: SEARCH
  kind: record_content
  reference: curation/; history/; research/; conf/; reviews/structured/; reports/yaml_record_review/;
    data/raw/; tests/
  summary: Ignored/hidden-inclusive rg searched target ID, label, slug, source path,
    source mint and parents; structured parsing covered every raw and curation TSV.
    No existing structured target declaration for these eight targets was found. Candidate
    infant-formula/raw-chop IDs and labels were also searched in data/raw, curation,
    conf, tests and history with no match; no global ontology absence is claimed.
  accessed_at: '2026-10-14T08:07:01.304534Z'
  support: supports
  locator: rg --no-ignore --hidden -l -i -F -e Engineered > Food production > Grains/Grain
    products -e FOODON:00001093 -e FOODON:00001173 -e FOODON:03530206 -e Grains/Grain
    products -e cereal grain food product -e cereal_grain_food_product -e gold.ecosystem:5927
    -e habitatmech:GOLD.c25f588dad curation history research conf reviews/structured
    reports/yaml_record_review data/raw tests
- evidence_id: GOLD_ACCESS
  kind: database
  reference: https://gold.jgi.doe.gov/
  summary: 'Direct retrieval of the six relevant study pages returned HTTP 403; no
    study contents were inferred. Receipts: {"Gs0142293": {"accessed_at": "2026-10-14T08:11:39.570835Z",
    "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0142293"},
    "Gs0150300": {"accessed_at": "2026-10-14T08:11:39.785085Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150300"}, "Gs0150660":
    {"accessed_at": "2026-10-14T08:11:39.830086Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0150660"}, "Gs0153740": {"accessed_at":
    "2026-10-14T08:11:39.869363Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153740"},
    "Gs0153816": {"accessed_at": "2026-10-14T08:11:39.925031Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153816"}, "Gs0154282":
    {"accessed_at": "2026-10-14T08:11:39.962586Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"}}'
  accessed_at: '2026-10-14T08:22:13.686117Z'
  support: context_only
- evidence_id: BASE_QC
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38530055451
  summary: 'Queried headSha/status/conclusion: success on exact unchanged scientific-input
    base b44399980b2f188379de618fda01b46d1b691ef6. This hosted QC predates the new
    review files.'
  accessed_at: '2026-10-14T08:22:13.686117Z'
  support: supports
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Entity, grounding and strict hierarchy
  outcome: concern
  target_ids:
  - FOODON:00001093
  evidence_ids:
  - RECORD
  - RAW
  - FOODON
  - RULES
  - TRANSFORM
  - SEARCH
  summary: The cereal-food family is supported by the source path and is not the mineral-particle
    homonym rejected in prior curation. FoodOn places unprocessed cereal grain under
    cereal grain under this food-product class, so the label does not itself exclude
    raw grain. Retain conservative CLOSE and RELATED source scope; reject only the
    false process parent. Absence of an optional textual ontology definition is not
    a required-field defect.
- assessment_id: SCIENCE
  area: evidence
  topic: Attestation units, source scope and MIxS evidence
  outcome: supported
  target_ids:
  - FOODON:00001093
  evidence_ids:
  - RECORD
  - RAW
  - FOODON
  - RULES
  - TRANSFORM
  - SEARCH
  summary: Raw row 1299 collapses nodes 5927/5928/5929 with zero frozen organism assertions
    and correctly omits count/unit. Bulk row 296 has 71 BIOSAMPLE observations; Gs0154282
    has seventeen paths. The September history explains the particle correction, but
    research prose about storage, water activity and microbial ecology is not adopted
    as record evidence.
- assessment_id: STATUS
  area: provenance
  topic: Native status and optional claims
  outcome: supported
  target_ids:
  - FOODON:00001093
  evidence_ids:
  - RECORD
  - RAW
  - FOODON
  - RULES
  - TRANSFORM
  - SEARCH
  summary: The complete record reproduces as CLOSE/REVIEWED. Reviewed status follows
    contributing ITEM decisions, not this review. No taxa, causal graph, environmental
    parameters, citations, discussions or datasets are asserted; these optional omissions
    do not justify invented biology. Food category is a coarse bucket, not a mechanism
    claim.
findings:
- finding_id: F1
  issue_key: cereal-grain-food-product-food-production-process-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Food material inherits a food-production process as a strict parent
  description: The record emits FOODON:03530206 from the GOLD path. Both frozen and
    pinned definitions make it a planned process, not a broader food material. The
    source hierarchy supplies production context, not is-a evidence.
  target_ids:
  - FOODON:00001093
  field_paths:
  - parent_habitats
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  evidence_ids:
  - RECORD
  - RAW
  - FOODON
  - RULES
  - TRANSFORM
  rule_id: docs/CURATION.md; local record checklist
  native_severity: major
  normalization_reason: Unsupported identity scope or false strict superclass is a
    material semantic defect, not style; no original member-level population is asserted.
actions:
- action_id: A1
  description: Exclude only the exact GOLD path contribution with its expected parent
    ID, retaining independent ontology parents and every source observation. For Bread
    production, reassess after its identity correction. Update the beverage regression
    that currently expects the invalid edge.
  finding_ids:
  - F1
  target_ids:
  - FOODON:00001093
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Inspect an exact canary; preserve raw counts/units, IDs, paths and existing history.
    No manual generated-file edits.
  - Pass schema, labels, provenance, reproduction, regression tests, history, generated
    site and full QC; regenerate affected semantic products.
  - A disposition requires a new immutable observation retaining this issue key and
    exact previous occurrence.
limitations:
- Same-agent review, not independent approval or a full-corpus scientific pass.
- Original GOLD membership and sample-study joins were unavailable. Frozen edge counts,
  later bulk biosamples and complete-triad sample counts are distinct observations,
  never summed or interpreted as prevalence.
- FoodOn OWL was pinned, with fresh OLS identity checks; this does not certify latest-release
  hierarchy equivalence or an ontology refresh.
- No SSSOM/KGX conformance certification, curation edit or native status promotion
  is performed by this observation. Original review bundles remain immutable.
- Exact-base hosted QC does not validate subsequently saved review files; post-save
  archive and publication checks remain required.
notes:
- Additional context inputs were captured before finalization; every original input
  hash and Git base was explicitly proved unchanged. Candidate searches included ignored
  files. Neighbor-record defects were not transferred to valid child ontology edges.
tags:
- habitatmech
- record-review
- food
```
