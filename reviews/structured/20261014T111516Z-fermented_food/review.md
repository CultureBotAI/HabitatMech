# Scientific record review: Fermented food

- Review: 20261014T111516Z-fermented_food
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T11:03:44.817802Z
- Finished UTC: 2026-10-14T11:15:16.368163Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The native GOLD record denotes fermented food material but inherits a production process as its strict parent. FOODON:00001258 is an existing candidate, not a missing global ontology class. Its current HabitatMech record already merges other source bins with BROAD/CLOSE mappings, so a later grounding requires an explicit source-equivalence and merge audit rather than automatic absorption.

## Scope And Provenance

Entire resolved record and every contributing source concept; one individual scientific observation.

Selection: Next eight unreviewed food paths after the hidden/ignored-inclusive census of 983/3208 current records and 15/60 food records. This bundle declares only one target; neighboring records are bounded comparison evidence.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4757949dc8aa00a5ecf4322c9e0d74064d414730.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.8f5ec46a28 | data/habitats/food/fermented_food.yaml | generated | Fermented food |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | habitatmech:GOLD.8f5ec46a28 | Executed 2026-10-14T11:04:45.287507Z to 2026-10-14T11:05:04.773286Z. No issues found |
| Native validate-strict | passed | True | habitatmech:GOLD.8f5ec46a28 | Executed 2026-10-14T11:05:31.681342Z to 2026-10-14T11:05:41.000056Z. uv run python scripts/validate_strict.py data/habitats/food/fermentation_cellar.yaml data/habitats/food/fermentation_starter.yaml data/habitats/food/fermented_dairy_products.yaml data/habitats/food/fermented_fish.yaml data/habitats/food/fermented_food.yaml data/habitats/food/fermented_meat_product.yaml data/habitats/food/fermented_seafood.yaml data/habitats/food/fermented_vegetables.yaml<br>Validating 8 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      8<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| Native validate-history | passed | True | habitatmech:GOLD.8f5ec46a28 | Executed 2026-10-14T11:05:41.000958Z to 2026-10-14T11:05:55.820604Z. No issues found<br>659 history record(s) valid against src/habitatmech/schema/history.yaml |
| Native provenance-check | passed | True | habitatmech:GOLD.8f5ec46a28 | Executed 2026-10-14T11:05:55.821840Z to 2026-10-14T11:05:56.900787Z. provenance current: 14 committed inventories, 2 GOLD sources |
| Native verify-corpus | passed | True | habitatmech:GOLD.8f5ec46a28 | Executed 2026-10-14T11:05:56.901632Z to 2026-10-14T11:06:28.364947Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| Native validate-causal-all | passed | True | habitatmech:GOLD.8f5ec46a28 | Executed 2026-10-14T11:06:28.367787Z to 2026-10-14T11:06:36.321923Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| Native term-requests-check | passed | True | habitatmech:GOLD.8f5ec46a28 | Executed 2026-10-14T11:06:36.322969Z to 2026-10-14T11:07:04.138036Z. term-request table is current (109 terms) |
| Native validate-products | passed | True | habitatmech:GOLD.8f5ec46a28 | Executed 2026-10-14T11:07:04.139140Z to 2026-10-14T11:08:23.164444Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1176<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2059<br><br>✅ All id↔label pairs correspond. |
| Exact-base authoritative hosted QC | passed | True | habitatmech:GOLD.8f5ec46a28 | Fresh verification 2026-10-14T11:08:46.028200Z: exact unchanged base passed authoritative QC; new review bundles still need archive validation. |
| Original source membership reconstruction | unavailable | False | habitatmech:GOLD.8f5ec46a28 | Bounded hidden/ignored-inclusive search did not locate original dumps/member joins; eighteen GOLD study pages returned HTTP 403. Frozen aggregates remain inspectable. |
| Structured expression applicability | not_applicable | False | habitatmech:GOLD.8f5ec46a28 | No gene, regulator, protein, expression module or transcriptomics claim is asserted; habitat and taxon occurrences are not expression evidence. |

## Scientific And Domain Assessments

### Identity, ontology scope and strict hierarchy

identity: concern. Targets: habitatmech:GOLD.8f5ec46a28.

The native GOLD record denotes fermented food material but inherits a production process as its strict parent. FOODON:00001258 is an existing candidate, not a missing global ontology class. Its current HabitatMech record already merges other source bins with BROAD/CLOSE mappings, so a later grounding requires an explicit source-equivalence and merge audit rather than automatic absorption.

### Every source attestation, unit and contextual observation

evidence: supported. Targets: habitatmech:GOLD.8f5ec46a28.

Exact path row 114 names nodes 5597/5743/5744 with 221 ORGANISM-unit assertions. Separate bulk row 219 has 109 BIOSAMPLE observations. Gs0154231 has this one path; Gs0154282 spans 17 paths and cannot establish membership details for this bin. Soy sauce and Soybean paste children do not contribute additional own counts. CLASS decision row 835 and absent optional definition do not authorize native status promotion.

### Generated history, native status and optional fields

provenance: supported. Targets: habitatmech:GOLD.8f5ec46a28.

Current UNGROUNDED/SEEDED follows the maintained source decisions and seed. No environmental-parameter, causal-graph, record-evidence, discussion or dataset claim is present; optional omission does not authorize invented biology or status promotion. No taxon association is asserted.

### Remaining evidence and ontology coverage limits

completeness: unknown. Targets: habitatmech:GOLD.8f5ec46a28.

Original source members and live GOLD study contents are unavailable. Full-source candidate discovery is not governed import or a completed neighbor review. A qualified pass supports only the present target claims; it does not certify complete curation, global ontology absence, source-bin exactness beyond evidence, or all ancestors.

## Findings

### F1: Production process is asserted as a strict habitat parent

major / open / confirmed; issue key: fermented-food-food-production-process-parent.

Immediate GOLD path contribution FOODON:03530206 is a planned production process in both the frozen definition and inspected full FoodOn. The target denotes a site or food/inoculum material, not a kind of that process. Source hierarchy placement does not establish subclass identity.

## Recommended Actions And Acceptance Checks

### A1

Exclude only the exact immediate GOLD process-parent contribution. Preserve any independent material genus, native identity and status. Do not invent a definition or replacement parent just to suppress this edge.

- Change maintained inputs only after separate curation authorization; do not hand-edit generated records.
- Preserve all source IDs, paths, counts and units, and taxon ranks/associations; no guessed original-member split.
- Inspect a dry seed and exact canary, then focused regression, schema, strict, history, provenance, label, corpus/site and authoritative QC gates.
- Save an immutable successor retaining this issue key and exact previous occurrence for any disposition.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| RECORD | data/habitats/food/fermented_food.yaml | supports | Read all fields and curation history in the entire resolved target YAML. |
| SOURCE_ROWS | data/raw/; curation/decisions.tsv; mint(s) habitatmech:GOLD.8f5ec46a28 | supports | Exact path row 114 names nodes 5597/5743/5744 with 221 ORGANISM-unit assertions. Separate bulk row 219 has 109 BIOSAMPLE observations. Gs0154231 has this one path; Gs0154282 spans 17 paths and cannot establish membership details for this bin. Soy sauce and Soybean paste children do not contribute additional own counts. CLASS decision row 835 and absent optional definition do not authorize native status promotion. Exact own-source row locators: data/raw/gold_ecosystem_paths.tsv:114; data/raw/gold_path_biosamples.tsv:219; data/raw/gold_studies.tsv:3926,3966; curation/decisions.tsv:835 |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md | supports | Applied the local field-by-field checklist: source identity, strict genus, source-unit preservation, MIxS roles, observational taxa, optional fields and all-source ITEM status gates. |
| TRANSFORMS | src/habitatmech/seed.py; src/habitatmech/extract.py; extract_gold; extract_bacdive; _load_taxon_labels; ConceptStore.get; ingest_gold; ingest_bacdive | supports | GOLD occurrence counts increment per Go/Gs/Gb edge and collapse node paths; they do not prove distinct organisms. BacDive aggregate counts source outgoing edges, while taxa use a deduplicated strain-to-taxon join. Seeder adds immediate GOLD parent contributions separately from named ontology subclass parents; it copies inventory taxon labels and assigns imported ontology synonyms exact scope. |
| FOODON | https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl; Relevant target/parent and candidate classes | supports | Inspected the official pinned RDF/XML definitions, active classes, named subclass parents and restriction axioms. SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf. The native GOLD record denotes fermented food material but inherits a production process as its strict parent. FOODON:00001258 is an existing candidate, not a missing global ontology class. Its current HabitatMech record already merges other source bins with BROAD/CLOSE mappings, so a later grounding requires an explicit source-equivalence and merge audit rather than automatic absorption. |
| ENVO | https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl; ENVO:03600039; ENVO:03600040; ENVO:00003074 | supports | Current source revision a2455d1a77e46bb8a664d65a157166b539269042. ENVO:03600040 is a manufactured fermentation inoculum, directly under ENVO:00003074, and explicitly carries hasExactSynonym Daqu. ENVO:03600039 is a pit for alcoholic-spirit fermentation. SHA256 a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c |
| OLS | https://www.ebi.ac.uk/ols4/api/ontologies | supports | Fresh term API queries resolve all seven ontology IDs directly used by this cohort as active. Relevant receipts: {"FOODON:03530206": {"accessed_at": "2026-10-14T11:04:06.208124Z", "sha256": "e209164474c7a06365bce7cdbc1f24ff58a283bc848d26221295686958abaf4e", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03530206"}} |
| SEARCH | curation/; history/; research/; conf/; reviews/structured/; reports/yaml_record_review/; data/raw/; tests/; rg --no-ignore --hidden -l -i -F -e Engineered &gt; Food production &gt; Fermented food -e FOODON:03530206 -e Fermented food -e fermented_food -e gold.ecosystem:5597 -e habitatmech:GOLD.8f5ec46a28 curation history research conf reviews/structured reports/yaml_record_review data/raw tests | supports | Hidden/ignored-inclusive identity, source mint/path, label, slug and parent searches plus structured parsing of every raw/curation TSV. Structured archive census found no earlier declaration of these eight exact targets and no collision for the nine new finding keys. Five inspected full-FoodOn candidates are absent from the parsed committed ontology inventory, not absent globally. {"accessed_at": "2026-10-14T11:10:09.559544Z", "archive_search": "Path.rglob and structured YAML parsing include hidden/ignored files", "bundles": 1402, "candidate_slice_presence": {"FOODON:00001053": false, "FOODON:00001054": false, "FOODON:03310029": false, "FOODON:03310418": false, "FOODON:03310784": false}, "key_search": {"command": ["rg", "--no-ignore", "--hidden", "-l", "-F", "-e", "fermentation-cellar-food-production-process-parent", "-e", "fermentation-starter-food-production-process-parent", "-e", "fermented-food-food-production-process-parent", "-e", "fermented-seafood-food-production-process-parent", "-e", "fermented-vegetables-food-production-process-parent", "-e", "fermentation-starter-daqu-exact-synonym", "-e", "fermentation-starter-ncbitaxon-86957-label", "-e", "fermented-meat-product-mammalian-parent", "-e", "fermented-meat-product-source-exactness", "reviews", "history", "curation", "tests"], "exit_code": 1, "matches": []}, "prior_issue_keys": [], "prior_target_declarations": [], "starter_taxa": {"displayed": 15, "pool": 15, "raw_rows_match": true, "sum_association_counts": 19}} |
| AVAILABILITY | conf/sources.yaml | context_only | {"accessed_at": "2026-10-14T11:04:45.077996Z", "command": ["rg", "--no-ignore", "--hidden", "--files", ".", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"], "enumerated_files": 41210, "exit_code": 0, "interpretation": "Ignored files included. Bounded to this repository and configured kg-microbe data root, not all disks. Inventories do not reconstruct original member joins.", "matches": []} |
| GOLD_ACCESS | https://gold.jgi.doe.gov/ | context_only | All eighteen exact study URLs selected from own-path rows returned HTTP 403. No page contents or original members are inferred. {"Gs0046755": {"accessed_at": "2026-10-14T11:04:49.272093Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0046755"}, "Gs0111426": {"accessed_at": "2026-10-14T11:04:49.628075Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0111426"}, "Gs0117939": {"accessed_at": "2026-10-14T11:04:50.123488Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0117939"}, "Gs0118005": {"accessed_at": "2026-10-14T11:04:50.166468Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0118005"}, "Gs0141280": {"accessed_at": "2026-10-14T11:04:50.206535Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0141280"}, "Gs0150381": {"accessed_at": "2026-10-14T11:04:50.243863Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150381"}, "Gs0150400": {"accessed_at": "2026-10-14T11:04:50.277291Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150400"}, "Gs0150497": {"accessed_at": "2026-10-14T11:04:50.316461Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150497"}, "Gs0150709": {"accessed_at": "2026-10-14T11:04:50.348666Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150709"}, "Gs0150730": {"accessed_at": "2026-10-14T11:04:50.387801Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150730"}, "Gs0150741": {"accessed_at": "2026-10-14T11:04:50.520416Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150741"}, "Gs0153794": {"accessed_at": "2026-10-14T11:04:50.670480Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153794"}, "Gs0154231": {"accessed_at": "2026-10-14T11:04:50.709174Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154231"}, "Gs0154264": {"accessed_at": "2026-10-14T11:04:50.759857Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154264"}, "Gs0154282": {"accessed_at": "2026-10-14T11:04:50.803554Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"}, "Gs0154636": {"accessed_at": "2026-10-14T11:04:50.849346Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154636"}, "Gs0156793": {"accessed_at": "2026-10-14T11:04:50.892628Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0156793"}, "Gs0159152": {"accessed_at": "2026-10-14T11:04:50.949426Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0159152"}} |
| BASE_QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38551394267 | supports | Freshly verified completed/success on exact captured base 4757949dc8aa00a5ecf4322c9e0d74064d414730: 1080 tests passed, 3 skipped; four contract tests passed; all authoritative native quality gates passed. This validates unchanged scientific inputs, not these newly authored reports. |

## Limits And Additional Notes

- Same-agent scientific review, not independent approval or full-corpus certification.
- Original members remain unavailable. Source occurrence edges, distinct-strain joins, bulk biosamples, study path unions and complete triads have different denominators and are not summed.
- Pinned full FoodOn, current pinned ENVO and fresh OLS queries are bounded evidence, not a complete ontology refresh. ENVO-imported FoodOn versions may differ from FoodOn itself; use the defining ontology for FoodOn claims.
- No habitat YAML, maintained curation input, history, ontology inventory, generated page or GitHub state was changed for these reviews.
- No SSSOM/KGX conformance certification, native status promotion or automatic historical-finding closure follows from a valid review.
- Exact-base hosted QC predates the new report files; post-save archive checks remain required.
- Neighbor and legacy inputs added at 2026-10-14T11:07:50.081514Z; all initially captured input hashes were explicitly unchanged.
- HTML inspection used the standard-library parser after optional BeautifulSoup was unavailable; primary downloaded HTML and web views were inspected. No required validator was unavailable.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T111516Z-fermented_food
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: Fermented food'
started_at: '2026-10-14T11:03:44.817802Z'
finished_at: '2026-10-14T11:15:16.368163Z'
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
summary: The native GOLD record denotes fermented food material but inherits a production
  process as its strict parent. FOODON:00001258 is an existing candidate, not a missing
  global ontology class. Its current HabitatMech record already merges other source
  bins with BROAD/CLOSE mappings, so a later grounding requires an explicit source-equivalence
  and merge audit rather than automatic absorption.
source:
  git_revision: 4757949dc8aa00a5ecf4322c9e0d74064d414730
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
  - path: curation/term_requests.tsv
    sha256: 331a7d9eb8a8909fc37402c0a776838979a8065644504d5c4f2a1c39bce5c24d
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: 3781420be8a7a6de4f44c9be1bc3a0d256824fb44b8dbbb56c6b3c99e21a6014
    role: context
  - path: data/habitats/food/fermentation_cellar.yaml
    sha256: 21b09d7d9c985e4c72fbf6746d52c5b1f36a2feb32c1b43cb14fbfd05abd6353
    role: context
  - path: data/habitats/food/fermentation_starter.yaml
    sha256: 8360a18296c54ab67c6a6490943d7a59ed081d4482e4a75bc031f4c026b39b9f
    role: context
  - path: data/habitats/food/fermented_dairy_products.yaml
    sha256: 9ed59912b37facdd56bb980f312ad3f131d13a6a604f8294574f94477e889ae4
    role: context
  - path: data/habitats/food/fermented_fish.yaml
    sha256: 89ff9b5d561742c28425cc8bed2cc18e7a07f7016e3276cc7b77d9dcd3c25ddb
    role: context
  - path: data/habitats/food/fermented_food.yaml
    sha256: 0394875ffa2b3ddcae0d110100627792c732ec0599b5ddc5900d21119ee1386a
    role: target
  - path: data/habitats/food/fermented_meat_product.yaml
    sha256: 3838ea3ee2d541edcde3add4aa0f3658eaac5e3a81b7e8087e395c6852862631
    role: context
  - path: data/habitats/food/fermented_seafood.yaml
    sha256: ff5b2499af4fb58b1b82e3d4f82d9c5f8ad171482234aa3c0aaac9d28812b937
    role: context
  - path: data/habitats/food/fermented_vegetables.yaml
    sha256: e0912ec20a89f06ef264f0a7306499093355f8743ed6a6968553b42ecd01dede
    role: context
  - path: data/habitats/food/fish_products.yaml
    sha256: 5435e216e51f243842916c2e4199123992c81ab166b0746963ffeee71f5253b3
    role: context
  - path: data/habitats/food/food_fermented.yaml
    sha256: 36914b14c9b027073981cfd96d2932852f74f76a597275d6d4e52b9a98da8d70
    role: context
  - path: data/habitats/food/mammalian_meat_food_product.yaml
    sha256: fab8fbd8e3352bfe93aefac2761dded407774e918244be3e6b8a87ae45ec27b5
    role: context
  - path: data/habitats/food/pit_mud.yaml
    sha256: 9aea9d7f49f548dbb29f3a64bed3ed2bd5087559a49665807920fea1db43b2fb
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
  - path: reports/yaml_record_review/20260928T183532Z-fermentation-cellar.md
    sha256: e9acb64abd2e1d93fdffc4d0e7d0a144d1c757f527393d4f4644b1b8c4605d1b
    role: context
  - path: research/habitats/other/starter-culture-habitatmech-bacdive-9eabedc3a1-deep-research-claude_code.md
    sha256: 206cda0d500e847d13ede3fe60fd74d2ec8583391f753fffde77874b8be09f0d
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
- target_id: habitatmech:GOLD.8f5ec46a28
  path: data/habitats/food/fermented_food.yaml
  label: Fermented food
  kind: generated
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained owner; generated record is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained owner; generated record is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained owner; generated record is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Maintained owner; generated record is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_isolation_sources.tsv
    role: Maintained owner; generated record is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_source_taxa.tsv
    role: Maintained owner; generated record is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Maintained owner; generated record is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained owner; generated record is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained owner; generated record is read-only
scope:
  description: Entire resolved record and every contributing source concept; one individual
    scientific observation.
  selection: Next eight unreviewed food paths after the hidden/ignored-inclusive census
    of 983/3208 current records and 15/60 food records. This bundle declares only
    one target; neighboring records are bounded comparison evidence.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.8f5ec46a28
evidence:
- evidence_id: RECORD
  kind: record_content
  reference: data/habitats/food/fermented_food.yaml
  summary: Read all fields and curation history in the entire resolved target YAML.
  accessed_at: '2026-10-14T11:15:16.367240Z'
  support: supports
- evidence_id: SOURCE_ROWS
  kind: record_content
  reference: data/raw/; curation/decisions.tsv
  summary: 'Exact path row 114 names nodes 5597/5743/5744 with 221 ORGANISM-unit assertions.
    Separate bulk row 219 has 109 BIOSAMPLE observations. Gs0154231 has this one path;
    Gs0154282 spans 17 paths and cannot establish membership details for this bin.
    Soy sauce and Soybean paste children do not contribute additional own counts.
    CLASS decision row 835 and absent optional definition do not authorize native
    status promotion. Exact own-source row locators: data/raw/gold_ecosystem_paths.tsv:114;
    data/raw/gold_path_biosamples.tsv:219; data/raw/gold_studies.tsv:3926,3966; curation/decisions.tsv:835'
  accessed_at: '2026-10-14T11:15:16.367240Z'
  support: supports
  locator: mint(s) habitatmech:GOLD.8f5ec46a28
- evidence_id: RULES
  kind: authority
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md
  summary: 'Applied the local field-by-field checklist: source identity, strict genus,
    source-unit preservation, MIxS roles, observational taxa, optional fields and
    all-source ITEM status gates.'
  accessed_at: '2026-10-14T11:15:16.367240Z'
  support: supports
- evidence_id: TRANSFORMS
  kind: record_content
  reference: src/habitatmech/seed.py; src/habitatmech/extract.py
  summary: GOLD occurrence counts increment per Go/Gs/Gb edge and collapse node paths;
    they do not prove distinct organisms. BacDive aggregate counts source outgoing
    edges, while taxa use a deduplicated strain-to-taxon join. Seeder adds immediate
    GOLD parent contributions separately from named ontology subclass parents; it
    copies inventory taxon labels and assigns imported ontology synonyms exact scope.
  accessed_at: '2026-10-14T11:15:16.367240Z'
  support: supports
  locator: extract_gold; extract_bacdive; _load_taxon_labels; ConceptStore.get; ingest_gold;
    ingest_bacdive
- evidence_id: FOODON
  kind: database
  reference: https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl
  summary: Inspected the official pinned RDF/XML definitions, active classes, named
    subclass parents and restriction axioms. SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf.
    The native GOLD record denotes fermented food material but inherits a production
    process as its strict parent. FOODON:00001258 is an existing candidate, not a
    missing global ontology class. Its current HabitatMech record already merges other
    source bins with BROAD/CLOSE mappings, so a later grounding requires an explicit
    source-equivalence and merge audit rather than automatic absorption.
  accessed_at: '2026-10-14T11:07:25.661747Z'
  support: supports
  locator: Relevant target/parent and candidate classes
- evidence_id: ENVO
  kind: database
  reference: https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl
  summary: Current source revision a2455d1a77e46bb8a664d65a157166b539269042. ENVO:03600040
    is a manufactured fermentation inoculum, directly under ENVO:00003074, and explicitly
    carries hasExactSynonym Daqu. ENVO:03600039 is a pit for alcoholic-spirit fermentation.
    SHA256 a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c
  accessed_at: '2026-10-14T11:07:29.497224Z'
  support: supports
  locator: ENVO:03600039; ENVO:03600040; ENVO:00003074
- evidence_id: OLS
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies
  summary: 'Fresh term API queries resolve all seven ontology IDs directly used by
    this cohort as active. Relevant receipts: {"FOODON:03530206": {"accessed_at":
    "2026-10-14T11:04:06.208124Z", "sha256": "e209164474c7a06365bce7cdbc1f24ff58a283bc848d26221295686958abaf4e",
    "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03530206"}}'
  accessed_at: '2026-10-14T11:15:16.367240Z'
  support: supports
- evidence_id: SEARCH
  kind: search
  reference: curation/; history/; research/; conf/; reviews/structured/; reports/yaml_record_review/;
    data/raw/; tests/
  summary: 'Hidden/ignored-inclusive identity, source mint/path, label, slug and parent
    searches plus structured parsing of every raw/curation TSV. Structured archive
    census found no earlier declaration of these eight exact targets and no collision
    for the nine new finding keys. Five inspected full-FoodOn candidates are absent
    from the parsed committed ontology inventory, not absent globally. {"accessed_at":
    "2026-10-14T11:10:09.559544Z", "archive_search": "Path.rglob and structured YAML
    parsing include hidden/ignored files", "bundles": 1402, "candidate_slice_presence":
    {"FOODON:00001053": false, "FOODON:00001054": false, "FOODON:03310029": false,
    "FOODON:03310418": false, "FOODON:03310784": false}, "key_search": {"command":
    ["rg", "--no-ignore", "--hidden", "-l", "-F", "-e", "fermentation-cellar-food-production-process-parent",
    "-e", "fermentation-starter-food-production-process-parent", "-e", "fermented-food-food-production-process-parent",
    "-e", "fermented-seafood-food-production-process-parent", "-e", "fermented-vegetables-food-production-process-parent",
    "-e", "fermentation-starter-daqu-exact-synonym", "-e", "fermentation-starter-ncbitaxon-86957-label",
    "-e", "fermented-meat-product-mammalian-parent", "-e", "fermented-meat-product-source-exactness",
    "reviews", "history", "curation", "tests"], "exit_code": 1, "matches": []}, "prior_issue_keys":
    [], "prior_target_declarations": [], "starter_taxa": {"displayed": 15, "pool":
    15, "raw_rows_match": true, "sum_association_counts": 19}}'
  accessed_at: '2026-10-14T11:03:54.096418Z'
  support: supports
  locator: rg --no-ignore --hidden -l -i -F -e Engineered > Food production > Fermented
    food -e FOODON:03530206 -e Fermented food -e fermented_food -e gold.ecosystem:5597
    -e habitatmech:GOLD.8f5ec46a28 curation history research conf reviews/structured
    reports/yaml_record_review data/raw tests
  search_scope: Target identifiers, minted source IDs, labels, slugs and paths; all
    raw/curation TSV rows and structured review targets/findings; listed repository
    roots only. rg --no-ignore --hidden and Path.rglob include ignored files.
- evidence_id: AVAILABILITY
  kind: search
  reference: conf/sources.yaml
  summary: '{"accessed_at": "2026-10-14T11:04:45.077996Z", "command": ["rg", "--no-ignore",
    "--hidden", "--files", ".", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"],
    "enumerated_files": 41210, "exit_code": 0, "interpretation": "Ignored files included.
    Bounded to this repository and configured kg-microbe data root, not all disks.
    Inventories do not reconstruct original member joins.", "matches": []}'
  accessed_at: '2026-10-14T11:15:16.367240Z'
  support: context_only
  search_scope: Ignored-inclusive file enumeration of this repository and configured
    kg-microbe data directory only, matching original GOLD/BacDive dump filenames;
    not a search of all disks or remote datasets.
- evidence_id: GOLD_ACCESS
  kind: database
  reference: https://gold.jgi.doe.gov/
  summary: 'All eighteen exact study URLs selected from own-path rows returned HTTP
    403. No page contents or original members are inferred. {"Gs0046755": {"accessed_at":
    "2026-10-14T11:04:49.272093Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0046755"},
    "Gs0111426": {"accessed_at": "2026-10-14T11:04:49.628075Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0111426"}, "Gs0117939":
    {"accessed_at": "2026-10-14T11:04:50.123488Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0117939"}, "Gs0118005": {"accessed_at":
    "2026-10-14T11:04:50.166468Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0118005"},
    "Gs0141280": {"accessed_at": "2026-10-14T11:04:50.206535Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0141280"}, "Gs0150381":
    {"accessed_at": "2026-10-14T11:04:50.243863Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0150381"}, "Gs0150400": {"accessed_at":
    "2026-10-14T11:04:50.277291Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150400"},
    "Gs0150497": {"accessed_at": "2026-10-14T11:04:50.316461Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150497"}, "Gs0150709":
    {"accessed_at": "2026-10-14T11:04:50.348666Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0150709"}, "Gs0150730": {"accessed_at":
    "2026-10-14T11:04:50.387801Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150730"},
    "Gs0150741": {"accessed_at": "2026-10-14T11:04:50.520416Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150741"}, "Gs0153794":
    {"accessed_at": "2026-10-14T11:04:50.670480Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0153794"}, "Gs0154231": {"accessed_at":
    "2026-10-14T11:04:50.709174Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154231"},
    "Gs0154264": {"accessed_at": "2026-10-14T11:04:50.759857Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154264"}, "Gs0154282":
    {"accessed_at": "2026-10-14T11:04:50.803554Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"}, "Gs0154636": {"accessed_at":
    "2026-10-14T11:04:50.849346Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154636"},
    "Gs0156793": {"accessed_at": "2026-10-14T11:04:50.892628Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0156793"}, "Gs0159152":
    {"accessed_at": "2026-10-14T11:04:50.949426Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0159152"}}'
  accessed_at: '2026-10-14T11:15:16.367240Z'
  support: context_only
- evidence_id: BASE_QC
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38551394267
  summary: 'Freshly verified completed/success on exact captured base 4757949dc8aa00a5ecf4322c9e0d74064d414730:
    1080 tests passed, 3 skipped; four contract tests passed; all authoritative native
    quality gates passed. This validates unchanged scientific inputs, not these newly
    authored reports.'
  accessed_at: '2026-10-14T11:15:16.367240Z'
  support: supports
checks:
- check_id: C4
  name: Native validate
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.8f5ec46a28
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/food/fermented_food.yaml
  exit_code: 0
  summary: Executed 2026-10-14T11:04:45.287507Z to 2026-10-14T11:05:04.773286Z. No
    issues found
  scope_note: Target schema; eight-target strict check; otherwise full-corpus native
    scope. Label gate has 1176 canonical matches, one synonym, five configured exceptions
    and 2059 no-adapter skips. Not scientific proof.
- check_id: C8
  name: Native validate-strict
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.8f5ec46a28
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/food/fermentation_cellar.yaml data/habitats/food/fermentation_starter.yaml
    data/habitats/food/fermented_dairy_products.yaml data/habitats/food/fermented_fish.yaml
    data/habitats/food/fermented_food.yaml data/habitats/food/fermented_meat_product.yaml
    data/habitats/food/fermented_seafood.yaml data/habitats/food/fermented_vegetables.yaml
  exit_code: 0
  summary: "Executed 2026-10-14T11:05:31.681342Z to 2026-10-14T11:05:41.000056Z. uv\
    \ run python scripts/validate_strict.py data/habitats/food/fermentation_cellar.yaml\
    \ data/habitats/food/fermentation_starter.yaml data/habitats/food/fermented_dairy_products.yaml\
    \ data/habitats/food/fermented_fish.yaml data/habitats/food/fermented_food.yaml\
    \ data/habitats/food/fermented_meat_product.yaml data/habitats/food/fermented_seafood.yaml\
    \ data/habitats/food/fermented_vegetables.yaml\nValidating 8 files with 15 workers;\
    \ schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      8\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Target schema; eight-target strict check; otherwise full-corpus native
    scope. Label gate has 1176 canonical matches, one synonym, five configured exceptions
    and 2059 no-adapter skips. Not scientific proof.
- check_id: C9
  name: Native validate-history
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.8f5ec46a28
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  summary: 'Executed 2026-10-14T11:05:41.000958Z to 2026-10-14T11:05:55.820604Z. No
    issues found

    659 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Target schema; eight-target strict check; otherwise full-corpus native
    scope. Label gate has 1176 canonical matches, one synonym, five configured exceptions
    and 2059 no-adapter skips. Not scientific proof.
- check_id: C10
  name: Native provenance-check
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.8f5ec46a28
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  summary: 'Executed 2026-10-14T11:05:55.821840Z to 2026-10-14T11:05:56.900787Z. provenance
    current: 14 committed inventories, 2 GOLD sources'
  scope_note: Target schema; eight-target strict check; otherwise full-corpus native
    scope. Label gate has 1176 canonical matches, one synonym, five configured exceptions
    and 2059 no-adapter skips. Not scientific proof.
- check_id: C11
  name: Native verify-corpus
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.8f5ec46a28
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  summary: "Executed 2026-10-14T11:05:56.901632Z to 2026-10-14T11:06:28.364947Z. expected\
    \ 3208 records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing:\
    \ 0\n\ncorpus reproduces exactly from data/raw/"
  scope_note: Target schema; eight-target strict check; otherwise full-corpus native
    scope. Label gate has 1176 canonical matches, one synonym, five configured exceptions
    and 2059 no-adapter skips. Not scientific proof.
- check_id: C12
  name: Native validate-causal-all
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.8f5ec46a28
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  summary: Executed 2026-10-14T11:06:28.367787Z to 2026-10-14T11:06:36.321923Z. validated
    32 causal-graph curation file(s) with 32 graph(s)
  scope_note: Target schema; eight-target strict check; otherwise full-corpus native
    scope. Label gate has 1176 canonical matches, one synonym, five configured exceptions
    and 2059 no-adapter skips. Not scientific proof.
- check_id: C13
  name: Native term-requests-check
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.8f5ec46a28
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  summary: Executed 2026-10-14T11:06:36.322969Z to 2026-10-14T11:07:04.138036Z. term-request
    table is current (109 terms)
  scope_note: Target schema; eight-target strict check; otherwise full-corpus native
    scope. Label gate has 1176 canonical matches, one synonym, five configured exceptions
    and 2059 no-adapter skips. Not scientific proof.
- check_id: C14
  name: Native validate-products
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.8f5ec46a28
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  summary: "Executed 2026-10-14T11:07:04.139140Z to 2026-10-14T11:08:23.164444Z. id↔label\
    \ correspondence summary:\n          OK_CANONICAL: 1176\n            OK_SYNONYM:\
    \ 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2059\n\n✅ All id↔label\
    \ pairs correspond."
  scope_note: Target schema; eight-target strict check; otherwise full-corpus native
    scope. Label gate has 1176 canonical matches, one synonym, five configured exceptions
    and 2059 no-adapter skips. Not scientific proof.
- check_id: QC
  name: Exact-base authoritative hosted QC
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.8f5ec46a28
  command: gh run view 38551394267 --json status,conclusion,headSha,url
  exit_code: 0
  summary: 'Fresh verification 2026-10-14T11:08:46.028200Z: exact unchanged base passed
    authoritative QC; new review bundles still need archive validation.'
  evidence_ids:
  - BASE_QC
- check_id: MEMBERS
  name: Original source membership reconstruction
  status: unavailable
  required: false
  target_ids:
  - habitatmech:GOLD.8f5ec46a28
  summary: Bounded hidden/ignored-inclusive search did not locate original dumps/member
    joins; eighteen GOLD study pages returned HTTP 403. Frozen aggregates remain inspectable.
  evidence_ids:
  - AVAILABILITY
  - GOLD_ACCESS
- check_id: IMODULON
  name: Structured expression applicability
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.8f5ec46a28
  summary: No gene, regulator, protein, expression module or transcriptomics claim
    is asserted; habitat and taxon occurrences are not expression evidence.
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Identity, ontology scope and strict hierarchy
  outcome: concern
  target_ids:
  - habitatmech:GOLD.8f5ec46a28
  evidence_ids:
  - RECORD
  - SOURCE_ROWS
  - RULES
  - TRANSFORMS
  - FOODON
  - ENVO
  - SEARCH
  summary: The native GOLD record denotes fermented food material but inherits a production
    process as its strict parent. FOODON:00001258 is an existing candidate, not a
    missing global ontology class. Its current HabitatMech record already merges other
    source bins with BROAD/CLOSE mappings, so a later grounding requires an explicit
    source-equivalence and merge audit rather than automatic absorption.
- assessment_id: SOURCE
  area: evidence
  topic: Every source attestation, unit and contextual observation
  outcome: supported
  target_ids:
  - habitatmech:GOLD.8f5ec46a28
  evidence_ids:
  - RECORD
  - SOURCE_ROWS
  - RULES
  - TRANSFORMS
  - FOODON
  - ENVO
  - SEARCH
  summary: Exact path row 114 names nodes 5597/5743/5744 with 221 ORGANISM-unit assertions.
    Separate bulk row 219 has 109 BIOSAMPLE observations. Gs0154231 has this one path;
    Gs0154282 spans 17 paths and cannot establish membership details for this bin.
    Soy sauce and Soybean paste children do not contribute additional own counts.
    CLASS decision row 835 and absent optional definition do not authorize native
    status promotion.
- assessment_id: STATUS
  area: provenance
  topic: Generated history, native status and optional fields
  outcome: supported
  target_ids:
  - habitatmech:GOLD.8f5ec46a28
  evidence_ids:
  - RECORD
  - SOURCE_ROWS
  - RULES
  - TRANSFORMS
  summary: Current UNGROUNDED/SEEDED follows the maintained source decisions and seed.
    No environmental-parameter, causal-graph, record-evidence, discussion or dataset
    claim is present; optional omission does not authorize invented biology or status
    promotion. No taxon association is asserted.
- assessment_id: LIMITS
  area: completeness
  topic: Remaining evidence and ontology coverage limits
  outcome: unknown
  target_ids:
  - habitatmech:GOLD.8f5ec46a28
  evidence_ids:
  - AVAILABILITY
  - GOLD_ACCESS
  - SEARCH
  - FOODON
  summary: Original source members and live GOLD study contents are unavailable. Full-source
    candidate discovery is not governed import or a completed neighbor review. A qualified
    pass supports only the present target claims; it does not certify complete curation,
    global ontology absence, source-bin exactness beyond evidence, or all ancestors.
findings:
- finding_id: F1
  issue_key: fermented-food-food-production-process-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Production process is asserted as a strict habitat parent
  description: Immediate GOLD path contribution FOODON:03530206 is a planned production
    process in both the frozen definition and inspected full FoodOn. The target denotes
    a site or food/inoculum material, not a kind of that process. Source hierarchy
    placement does not establish subclass identity.
  target_ids:
  - habitatmech:GOLD.8f5ec46a28
  field_paths:
  - parent_habitats
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained owner; generated record is read-only
  evidence_ids:
  - RECORD
  - SOURCE_ROWS
  - RULES
  - FOODON
  - TRANSFORMS
  rule_id: 'docs/CURATION.md and native review checklist: exact identity, strict genus
    and taxon-label scope'
  native_severity: major
  normalization_reason: A materially unsupported identity, lexical equivalence or
    strict genus is a major semantic finding.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.8f5ec46a28
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained owner; generated record is read-only
  description: Exclude only the exact immediate GOLD process-parent contribution.
    Preserve any independent material genus, native identity and status. Do not invent
    a definition or replacement parent just to suppress this edge.
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Change maintained inputs only after separate curation authorization; do not hand-edit
    generated records.
  - Preserve all source IDs, paths, counts and units, and taxon ranks/associations;
    no guessed original-member split.
  - Inspect a dry seed and exact canary, then focused regression, schema, strict,
    history, provenance, label, corpus/site and authoritative QC gates.
  - Save an immutable successor retaining this issue key and exact previous occurrence
    for any disposition.
limitations:
- Same-agent scientific review, not independent approval or full-corpus certification.
- Original members remain unavailable. Source occurrence edges, distinct-strain joins,
  bulk biosamples, study path unions and complete triads have different denominators
  and are not summed.
- Pinned full FoodOn, current pinned ENVO and fresh OLS queries are bounded evidence,
  not a complete ontology refresh. ENVO-imported FoodOn versions may differ from FoodOn
  itself; use the defining ontology for FoodOn claims.
- No habitat YAML, maintained curation input, history, ontology inventory, generated
  page or GitHub state was changed for these reviews.
- No SSSOM/KGX conformance certification, native status promotion or automatic historical-finding
  closure follows from a valid review.
- Exact-base hosted QC predates the new report files; post-save archive checks remain
  required.
notes:
- Neighbor and legacy inputs added at 2026-10-14T11:07:50.081514Z; all initially captured
  input hashes were explicitly unchanged.
- HTML inspection used the standard-library parser after optional BeautifulSoup was
  unavailable; primary downloaded HTML and web views were inspected. No required validator
  was unavailable.
tags:
- habitatmech
- record-review
- food
```
