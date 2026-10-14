# Scientific record review: vegetable oil food product

- Review: 20261014T172904Z-vegetable_oil_food_product
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T17:14:43.008723Z
- Finished UTC: 2026-10-14T17:29:04Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

FOODON:00001087 is plant-derived oil. BacDive Oil-Food distinguishes food oil from fuel, not necessarily plant from animal oil. The ITEM rationale defends only food-product framing, leaving the plant restriction unsupported; no actual animal-oil member is claimed recovered.

## Scope And Provenance

One complete resolved record and its source concepts.

Selection: One of13 remaining Food records after ignored-inclusive census1015/3208; no sampling claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ab46b9d651f5c4212d0b8b26fd420b6cc12efeba.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| FOODON:00001087 | data/habitats/food/vegetable_oil_food_product.yaml | generated | vegetable oil food product |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | FOODON:00001087 | Executed 2026-10-14T17:15:10.871448Z to 2026-10-14T17:15:12.783584Z. No issues found |
| Native validate-strict | passed | True | FOODON:00001087 | Executed 2026-10-14T17:15:14.677937Z to 2026-10-14T17:15:20.563528Z. uv run python scripts/validate_strict.py data/habitats/food/seafood_product.yaml data/habitats/food/seafood_product_eurofir.yaml data/habitats/food/silage_fermentation.yaml data/habitats/food/sodium_chloride_salt.yaml data/habitats/food/solar_salt.yaml data/habitats/food/sourdough.yaml data/habitats/food/soy_sauce.yaml data/habitats/food/soybean_paste.yaml data/habitats/food/spice.yaml data/habitats/food/sweets.yaml data/habitats/food/utensil.yaml data/habitats/food/vegetable_oil_food_product.yaml data/habitats/food/vinegar.yaml<br>Validating 13 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      13<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| Native validate-history | passed | True | FOODON:00001087 | Executed 2026-10-14T17:15:20.564224Z to 2026-10-14T17:15:27.358904Z. No issues found<br>679 history record(s) valid against src/habitatmech/schema/history.yaml |
| Native provenance-check | passed | True | FOODON:00001087 | Executed 2026-10-14T17:15:27.359560Z to 2026-10-14T17:15:27.933220Z. provenance current: 14 committed inventories, 2 GOLD sources |
| Native verify-corpus | passed | True | FOODON:00001087 | Executed 2026-10-14T17:15:27.933784Z to 2026-10-14T17:15:44.440215Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| Native validate-causal-all | passed | True | FOODON:00001087 | Executed 2026-10-14T17:15:44.440896Z to 2026-10-14T17:15:48.106419Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| Native term-requests-check | passed | True | FOODON:00001087 | Executed 2026-10-14T17:15:48.107072Z to 2026-10-14T17:16:03.344493Z. term-request table is current (109 terms) |
| Native validate-products | passed | True | FOODON:00001087 | Executed 2026-10-14T17:16:03.345192Z to 2026-10-14T17:16:52.807179Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1176<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2059<br><br>✅ All id↔label pairs correspond. |
| Exact-base QC | passed | True | FOODON:00001087 | Exact-base hosted success, not final-head validation. |
| Original source joins | unavailable | False | FOODON:00001087 | Original member membership not fully reconstructed. |
| Expression-module applicability | not_applicable | False | FOODON:00001087 | No gene/regulator/transcriptomic mechanism claim requires this adapter. |

## Scientific And Domain Assessments

### Source identity

identity: concern. Targets: FOODON:00001087.

FOODON:00001087 is plant-derived oil. BacDive Oil-Food distinguishes food oil from fuel, not necessarily plant from animal oil. The ITEM rationale defends only food-product framing, leaving the plant restriction unsupported; no actual animal-oil member is claimed recovered.

### Strict genus

grounding: supported. Targets: FOODON:00001087.

FOODON:03310387 edible oil and03460263 vegetable fat or oil are defensible parents of the adopted ontology class. The defect is source-to-class scope, not those internal ontology edges.

### Source assertions and units

provenance: supported. Targets: FOODON:00001087.

BacDive row133 has7 STRAIN assertions and6 taxa; mapping row219 is lexical CLOSE. ITEM REVIEW1721 explains REVIEWED but not plant origin. All6 identifiers/labels resolve in NCBI; bacterium1869227 remains underspecified despite a species-rank taxonomy node.

### Definitions and synonym scope

evidence: supported. Targets: FOODON:00001087.

Present definitions/synonyms retain the inspected owner scope. Missing optional definitions are not automatically a defect.

### Environmental parameters

quantity: not_applicable. Targets: FOODON:00001087.

No environmental-parameter assertion present; neighboring triads and generic literature ranges are not inherited.

### Association versus characteristic presence

evidence: supported. Targets: FOODON:00001087.

Imported taxon identifiers/labels and count/rank/pool retained; these are reported associations, not habitat enrichment. Original joins remain unavailable.

### Mechanism evidence

graph: not_applicable. Targets: FOODON:00001087.

No causal graph or claim-level mechanism asserted; optional absence is not a defect.

### Native status gates

scope: supported. Targets: FOODON:00001087.

ITEM versus CLASS/default resolution explains current native status; this review does not promote it.

### Generated boundaries

ownership: supported. Targets: FOODON:00001087.

Fix maintained decisions/exclusions/definitions and regenerate, never patch generated YAML/pages.

### Member-level limitations

completeness: unknown. Targets: FOODON:00001087.

Frozen aggregates reproduce but missing original joins limit scope certification. No SSSOM/KGX or whole-corpus readiness claim.

## Findings

### F1: Source concept and adopted habitat identity have unresolved scope

major / open / confirmed; issue key: vegetable-oil-food-product-source-identity-scope.

FOODON:00001087 is plant-derived oil. BacDive Oil-Food distinguishes food oil from fuel, not necessarily plant from animal oil. The ITEM rationale defends only food-product framing, leaving the plant restriction unsupported; no actual animal-oil member is claimed recovered. FOODON:03310387 edible oil and03460263 vegetable fat or oil are defensible parents of the adopted ontology class. The defect is source-to-class scope, not those internal ontology edges.

## Recommended Actions And Acceptance Checks

### A1

Recover original source/member context and make an explicit ITEM decision for each contributing concept. Retain a source mint or use a demonstrated exact term; do not force a near match. For silage resolve process versus material first. For a changed identity update guarded parents, path locks and redirects through native generators; no generic predicate swap.

- Change maintained inputs only; dry seed and inspect canary before wider regeneration.
- Preserve source attestations, independent valid parents and honest native status; prove exact corpus delta.
- Validate schema, history, reproduction, site and QC; append immutable successor with exact previous occurrence.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| RECORD | data/habitats/food/vegetable_oil_food_product.yaml | supports | Entire target read, including all source attestations, definitions, synonyms, taxa and generated history. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; src/habitatmech/schema/habitatmech.yaml | supports | Strictly broader parents, exact identity versus broader grounding, distinct source units, FOOD matrix category and all-source ITEM gate applied. |
| ROWS | data/raw/; curation/decisions.tsv; curation/term_requests.tsv | supports | BacDive row133 has7 STRAIN assertions and6 taxa; mapping row219 is lexical CLOSE. ITEM REVIEW1721 explains REVIEWED but not plant origin. All6 identifiers/labels resolve in NCBI; bacterium1869227 remains underspecified despite a species-rank taxonomy node. Parsed matching/comparison row locators: {"curation/decisions.tsv": [1721], "data/raw/bacdive_isolation_sources.tsv": [133], "data/raw/bacdive_source_taxa.tsv": [2014, 2015, 2016, 2017, 2018, 2019], "data/raw/isolation_source_groundings.tsv": [219], "data/raw/ontology_subclass_edges.tsv": [8786, 8787, 8964, 9050], "data/raw/ontology_terms.tsv": [10517, 10650, 10721]} |
| TRANSFORM | src/habitatmech/seed.py | supports | All13 generated documents matched disk in an in-memory build; source resolution traces inspected. FOODON:03310387 edible oil and03460263 vegetable fat or oil are defensible parents of the adopted ontology class. The defect is source-to-class scope, not those internal ontology edges. Trace time: 2026-10-14T17:16:19.351572Z |
| SEARCH | curation/; history/; research/; reviews/structured/; reports/yaml_record_review/; data/raw/; tests/ | supports | Exact labels, slugs, identifiers and source mints searched including ignored files. No prior structured declaration for these13 targets; legacy reports are handled separately. Command: rg --no-ignore --hidden -l -i -F -e FOODON:00001087 -e FOODON:03310387 -e FOODON:03460263 -e Oil-Food -e bacdive.isolation_source:oil-food -e habitatmech:BACDIVE.ab42f44be6 -e vegetable oil food product -e vegetable_oil_food_product curation history research conf reviews/structured reports/yaml_record_review data/raw tests |
| MEMBERS | conf/sources.yaml; data/raw/MANIFEST.yaml; data/raw/GOLD_MANIFEST.yaml | supports | Original member joins not located among 41780 enumerated repository/configured kg-microbe data-root files. Frozen aggregates remain available. Receipt: {"accessed_at": "2026-10-14T17:16:14.759372Z", "command": ["rg", "--no-ignore", "--hidden", "--files", ".", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"], "enumerated_files": 41780, "exit_code": 0, "interpretation": "Ignored/hidden files included within repository and configured kg-microbe data root; not an all-disks search.", "matches": []} |
| GOLD_ACCESS | https://gold.jgi.doe.gov/ | supports | Four study routes returned403 and12 ecosystem routes returned404; unsupported routes/access failures do not invalidate frozen identifiers. No inaccessible page text inferred. {"Gs0150294": {"accessed_at": "2026-10-14T17:16:19.395929Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150294"}, "Gs0150545": {"accessed_at": "2026-10-14T17:16:19.448250Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150545"}, "Gs0154236": {"accessed_at": "2026-10-14T17:16:19.492924Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154236"}, "Gs0154282": {"accessed_at": "2026-10-14T17:16:19.538126Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"}, "gold.ecosystem:3500": {"accessed_at": "2026-10-14T17:16:20.077949Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/3500"}, "gold.ecosystem:5327": {"accessed_at": "2026-10-14T17:16:20.586256Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5327"}, "gold.ecosystem:5531": {"accessed_at": "2026-10-14T17:16:21.754293Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5531"}, "gold.ecosystem:5598": {"accessed_at": "2026-10-14T17:16:20.793466Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5598"}, "gold.ecosystem:5749": {"accessed_at": "2026-10-14T17:16:21.030470Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5749"}, "gold.ecosystem:5895": {"accessed_at": "2026-10-14T17:16:21.188135Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5895"}, "gold.ecosystem:5930": {"accessed_at": "2026-10-14T17:16:19.929021Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5930"}, "gold.ecosystem:5936": {"accessed_at": "2026-10-14T17:16:21.446475Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5936"}, "gold.ecosystem:7230": {"accessed_at": "2026-10-14T17:16:19.696737Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/7230"}, "gold.ecosystem:8057": {"accessed_at": "2026-10-14T17:16:20.239866Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/8057"}, "gold.ecosystem:8058": {"accessed_at": "2026-10-14T17:16:20.406608Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/8058"}, "gold.ecosystem:8314": {"accessed_at": "2026-10-14T17:16:21.617486Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/8314"}} |
| ONTOLOGY | https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl | supports | Pinned full OWL definitions, parents and restrictions inspected, alongside current OLS ENVO/FoodOn identifiers, labels and active status. FOODON:03310387 edible oil and03460263 vegetable fat or oil are defensible parents of the adopted ontology class. The defect is source-to-class scope, not those internal ontology edges. Retrieval receipt: {"accessed_at": "2026-10-14T12:27:42.074174Z", "sha256": "b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf", "url": "https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl"}. |
| OLS | https://www.ebi.ac.uk/ols4/api/ontologies/ | supports | Current term receipts; checking candidates does not import them or refresh the frozen ontology slice. {"ENVO-00003030.json": {"accessed_at": "2026-10-14T17:16:00.856704Z", "sha256": "8568d75af6ec12c7802152ed56ea5111b5cd7c8a8c17c32aa9fee10a2eb96ef9", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00003030"}, "ENVO-01000508.json": {"accessed_at": "2026-10-14T17:16:01.557474Z", "sha256": "9cce974181ae166d71b729c8674d932629b99cd9d813bb646a5a19444aabc628", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000508"}, "ENVO-01000681.json": {"accessed_at": "2026-10-14T17:16:02.265470Z", "sha256": "f74be5e8bf0059667736fabaaae7b1596d629b5f6a653bf139c7e00017f53293", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000681"}, "ENVO-03501263.json": {"accessed_at": "2026-10-14T17:16:02.960918Z", "sha256": "97a307b453b6b6cf1060f13573dceeeed75f1a9de1f58f99eed982d8b9adacf1", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03501263"}, "ENVO-03501327.json": {"accessed_at": "2026-10-14T17:16:03.628104Z", "sha256": "1964b6e5bf8f83111d1824aabbb91ad7b91972ecefd4a99174c81271407eebde", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03501327"}, "ENVO-03600040.json": {"accessed_at": "2026-10-14T17:16:04.322977Z", "sha256": "29f399d45596f0435ee5baf761667c32bb8e83184ec782e7141c97077113f490", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03600040"}, "FOODON-00001046.json": {"accessed_at": "2026-10-14T17:19:30.172322Z", "sha256": "edb13c2554689c15f149f859da114b5bcf00045a54e59ac30c412ff3a4866bcd", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001046"}, "FOODON-00001073.json": {"accessed_at": "2026-10-14T17:16:04.981644Z", "sha256": "07b71752b62fb311191ddb2ddf944c5cea859c3932f29ebe227f9433bd782334", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001073"}, "FOODON-00001078.json": {"accessed_at": "2026-10-14T17:19:28.111825Z", "sha256": "a6709b4a437bf29c657ba98b6dcd8838bb8b4604a58108e2b4c9f4efe8b5bae7", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001078"}, "FOODON-00001087.json": {"accessed_at": "2026-10-14T17:16:05.737513Z", "sha256": "d3278deb470abc548d7ebc211a79b0fcb4ae9613af9d014429ef1a0657da16ae", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001087"}, "FOODON-00001149.json": {"accessed_at": "2026-10-14T17:16:06.476720Z", "sha256": "0b2e8311c42fe85e045b52639da23342f23555c42c4683c4d8de165f81e5be81", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001149"}, "FOODON-00001210.json": {"accessed_at": "2026-10-14T17:19:25.096735Z", "sha256": "dcdd505a2ba7427d6a210337d7c311ef6739c3db0d57d166257aa0e7c60dc11e", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001210"}, "FOODON-00001235.json": {"accessed_at": "2026-10-14T17:19:28.759933Z", "sha256": "6a1218a1a52c4076b26510eb33ae8d93da988bb4ef603aa0520db387065858d8", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001235"}, "FOODON-00001258.json": {"accessed_at": "2026-10-14T17:16:07.054895Z", "sha256": "3a9437d82255b394ac38aebbde2f83013f772b4affdb4e800a7d847f4be59a24", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001258"}, "FOODON-00002266.json": {"accessed_at": "2026-10-14T17:19:26.498681Z", "sha256": "4fd5eed1989b3c3eaafcef84c2a604167d8cd9a909d1022ad042780f487ef8a4", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00002266"}, "FOODON-03301115.json": {"accessed_at": "2026-10-14T17:19:29.430370Z", "sha256": "401aa9bfe630db50ea259b7015b622706e0410c498efb590fda49aa753d1d369", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03301115"}, "FOODON-03301705.json": {"accessed_at": "2026-10-14T17:16:07.785283Z", "sha256": "46d3b3f7ff4459f770cbe4398efc09b87b0ba75107f6c0232440dd127f9dba74", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03301705"}, "FOODON-03302481.json": {"accessed_at": "2026-10-14T17:16:08.467305Z", "sha256": "b2cd9bbb85b36495ea8ecd2145646146f830f50daa3b46eb37f1f946a9e773a2", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03302481"}, "FOODON-03303220.json": {"accessed_at": "2026-10-14T17:16:09.132583Z", "sha256": "9797bca63d1713a1b6538605885b98199bb669beb34ef487e0a35c85a225ce1f", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03303220"}, "FOODON-03303380.json": {"accessed_at": "2026-10-14T17:16:09.882851Z", "sha256": "9b177c23e89117bd634cafca67417ed82cd16a829d62e4035fd9b0e1aa5bae24", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03303380"}, "FOODON-03304099.json": {"accessed_at": "2026-10-14T17:16:11.128136Z", "sha256": "a80d8b9c60b9049d26e9b8a50e44a0f24cceac6cdcc552ec19fb4015ef708ed0", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03304099"}, "FOODON-03304996.json": {"accessed_at": "2026-10-14T17:16:12.669898Z", "sha256": "94bf5dfac4f70de17eb308a56b8c316b6c8feb527dab81a05d222a5d2ce3a434", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03304996"}, "FOODON-03306052.json": {"accessed_at": "2026-10-14T17:16:13.561198Z", "sha256": "13da1f9711d824fb46ab8485c4071005b03afeb0da3a7a5bbb5ae828ed29651c", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03306052"}, "FOODON-03310002.json": {"accessed_at": "2026-10-14T17:16:14.258866Z", "sha256": "333cc7837da5fd72aa4c1f35c346976afd06ce3ee1a50a82d06e2527ab6de2c5", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03310002"}, "FOODON-03310005.json": {"accessed_at": "2026-10-14T17:19:27.341290Z", "sha256": "2a69e4de49c6f5b0265cc9334e6208de07afe3967b40932ed4eb0db80b737b47", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03310005"}, "FOODON-03310387.json": {"accessed_at": "2026-10-14T17:16:14.997310Z", "sha256": "47fb2b0557cbf8357b38529d66dca9babbdf4ae2bd6b19477108ae71462cc779", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03310387"}, "FOODON-03316428.json": {"accessed_at": "2026-10-14T17:16:15.659460Z", "sha256": "96931104d414a1aaa4796d8d18ade9e5119c063650e7390f5a767e081776843d", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03316428"}, "FOODON-03316449.json": {"accessed_at": "2026-10-14T17:19:24.446919Z", "sha256": "5b673a9cabe9392f4c989ffb4571c6d904f470fd7c3b207602e6b5522c08d9b3", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03316449"}, "FOODON-03400801.json": {"accessed_at": "2026-10-14T17:16:16.244341Z", "sha256": "023ca9f5f8e40d2118268da930571a3f0c98feb0b91587a66ccd638b36d49bf1", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03400801"}, "FOODON-03400803.json": {"accessed_at": "2026-10-14T17:16:16.864039Z", "sha256": "c003d98e653d79a8878791cab35bf0f10002d6184ff9bffa1f2e3b6ef91013e0", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03400803"}, "FOODON-03411345.json": {"accessed_at": "2026-10-14T17:19:25.842441Z", "sha256": "a688a4b71fdfb89269ea7b90e1a78be5ff6db5fb412f8c8d4f97db5f47c2138b", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03411345"}, "FOODON-03460263.json": {"accessed_at": "2026-10-14T17:16:17.541063Z", "sha256": "9463e270fb56b69e35e0e8e1c66d621ad3385a5d330165176e10fcf1869ae144", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03460263"}, "FOODON-03530206.json": {"accessed_at": "2026-10-14T17:16:18.276086Z", "sha256": "e209164474c7a06365bce7cdbc1f24ff58a283bc848d26221295686958abaf4e", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03530206"}, "FOODON-03544457.json": {"accessed_at": "2026-10-14T17:16:18.970258Z", "sha256": "8042724409933b9628739f09b41316dea6cb936a51dfc413a62b5762c77d15f8", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03544457"}} |
| PRIMARY | https://bacdive.dsmz.de/isolation-sources | supports | Current BacDive isolation category listing distinguishes Oil (Food) from Oil (Fuel). This supports food context, not plant-only origin or recovery of original7 joins. Retrieval receipt: {"accessed_at": "2026-10-14T17:19:34.727310Z", "sha256": "60f9932f434230027051edf3e35a6e3af4d52d2812eda2e7088ea9228ffef9de", "url": "https://bacdive.dsmz.de/isolation-sources"}. |
| TAXONOMY | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;retmode=xml&amp;id=1077144,1122129,1122211,112331,1123359,1129374,121872,1227498,1238186,1262550,1280,1281,1294022,129985,135826,1423716,1455608,147248,157227,1590,1631871,1690008,179010,1869227,1879320,1881060,261164,282669,43666,47846,69373 | supports | Every imported identifier/label resolves. Mixed strain/species ranks are not equated. Association counts and ranking are not characteristic-enrichment proof. [{"current": {"identifier": "69373", "name": "Curtobacterium pusillum", "names": ["Brevibacterium pusillum", "Curtobacterium sp. IFO12674", "Curtobacterium sp. IFO 12674T", "Curtibacterium pusillum", "Curtibacterium sp. IFO 12674T", "Curtibacterium sp. IFO12674"], "rank": "species"}, "stored": {"association_count": 2, "candidate_pool": 6, "rank": 1, "source": "BACDIVE", "taxon_id": "NCBITaxon:69373", "taxon_label": "Curtobacterium pusillum"}}, {"current": {"identifier": "1280", "name": "Staphylococcus aureus", "names": ["Micrococcus aureus", "Micrococcus pyogenes", "Staphylococcus aureus subsp. anaerobius", "Staphylococcus pyogenes aureus", "Staphylococcus pyogenes citreus", "Staphylococcus aureus subsp. aureus", "Staphylococcus sp. CCUG 17621", "Staphylococcus sp. Fddn_Aq4"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 6, "rank": 2, "source": "BACDIVE", "taxon_id": "NCBITaxon:1280", "taxon_label": "Staphylococcus aureus"}}, {"current": {"identifier": "1869227", "name": "bacterium", "names": ["Bacteria bacterium", "Bacteria sp.", "Bacterial sp.", "Bacterium sp.", "Unknown eubacteria", "Unknown eubacterium", "unclassified bacterium", "unidentified bacteria", "unidentified bacterium", "unidentified eubacterium", "unknown bacteria"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 6, "rank": 3, "source": "BACDIVE", "taxon_id": "NCBITaxon:1869227", "taxon_label": "bacterium"}}, {"current": {"identifier": "1881060", "name": "Clostridium sp. USBA 49", "names": [], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 6, "rank": 4, "source": "BACDIVE", "taxon_id": "NCBITaxon:1881060", "taxon_label": "Clostridium sp. USBA 49"}}, {"current": {"identifier": "43666", "name": "Paeniglutamicibacter sulfureus", "names": ["Arthrobacter sulfureus", "Arthrobacter sp. BZ73"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 6, "rank": 5, "source": "BACDIVE", "taxon_id": "NCBITaxon:43666", "taxon_label": "Paeniglutamicibacter sulfureus"}}, {"current": {"identifier": "47846", "name": "Brachybacterium conglomeratum", "names": ["Micrococcus conglomeratus"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 6, "rank": 6, "source": "BACDIVE", "taxon_id": "NCBITaxon:47846", "taxon_label": "Brachybacterium conglomeratum"}}] Retrieval receipt: {"accessed_at": "2026-10-14T17:16:04.218285Z", "sha256": "c2d205c95a1497fe847855cbea5a30384fa2b305a04c7079820dff71a67c6043", "url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;retmode=xml&amp;id=1077144,1122129,1122211,112331,1123359,1129374,121872,1227498,1238186,1262550,1280,1281,1294022,129985,135826,1423716,1455608,147248,157227,1590,1631871,1690008,179010,1869227,1879320,1881060,261164,282669,43666,47846,69373"}. |
| BASE_QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38602382356 | supports | Exact-base authoritative queue QC succeeded; predates new review files and future fixes. Retrieval receipt: {"accessed_at": "2026-10-14T17:26:22Z"}. |

## Limits And Additional Notes

- Same-agent assessment, not independent approval or native status promotion.
- Original source joins unavailable; counts are frozen aggregates, not independently recovered specimen membership.
- Current ontology checks are bounded candidate verification, not a full snapshot refresh.
- This pre-fix observation does not certify SSSOM/KGX products or all corpus records.
- Legacy reports remain historical; no clean assessment silently closes an older unresolved finding.
- Original input hashes unchanged at extended capture 2026-10-14T17:26:56Z.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T172904Z-vegetable_oil_food_product
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: vegetable oil food product'
started_at: '2026-10-14T17:14:43.008723Z'
finished_at: '2026-10-14T17:29:04Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent maintains and reviews HabitatMech; not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
scientific_review: true
verdict: needs_curation
summary: FOODON:00001087 is plant-derived oil. BacDive Oil-Food distinguishes food
  oil from fuel, not necessarily plant from animal oil. The ITEM rationale defends
  only food-product framing, leaving the plant restriction unsupported; no actual
  animal-oil member is claimed recovered.
source:
  git_revision: ab46b9d651f5c4212d0b8b26fd420b6cc12efeba
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
    sha256: e9ad29df9765530c563a018ac38390e1779da06fadf886e4db422e36558647fa
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
  - path: data/habitats/food/fermentation_starter.yaml
    sha256: 7233bb5a0fdbe4e6e70fac3941d3eb1bb70cb7555658dd95f39e3c1cc1116ef7
    role: context
  - path: data/habitats/food/fermented_food.yaml
    sha256: 7eee668ff9ba018c8a8d8ea6832f18ec8e3efbbd09ead7f850c9f77c115666ef
    role: context
  - path: data/habitats/food/food_fermented.yaml
    sha256: 91efcb97c4ecd67344797aa798d8e6f1cad0434a5ef55d0171dd8a501d95c40a
    role: context
  - path: data/habitats/food/food_production.yaml
    sha256: b0fce7af2cc321a0979ce4d3bfec5e2d4383410ae8e62172b006073afb783ab7
    role: context
  - path: data/habitats/food/seafood_product.yaml
    sha256: 92fe9e0cd56a12671fb144cacdc1a0f1475a0eb8dfb9e3a2a0c1594f95538c84
    role: context
  - path: data/habitats/food/seafood_product_eurofir.yaml
    sha256: 14bb5040ce6aadad131bd13afbea7feabe6695007e1ea1befc20cbf657ad6c22
    role: context
  - path: data/habitats/food/silage_fermentation.yaml
    sha256: d22e9c959cbc581797163d5584738a575c57a9be23bca542f4a4dd16af6d3aba
    role: context
  - path: data/habitats/food/sodium_chloride_salt.yaml
    sha256: 09b804b62b37efef9d9de227b84a64c15797bbb522f4d934fdeb98b23b610842
    role: context
  - path: data/habitats/food/solar_salt.yaml
    sha256: c07dfe07ee688011a64c1d6aef28550e5c204036dd5d8783413c12a411f3a705
    role: context
  - path: data/habitats/food/sourdough.yaml
    sha256: dfe868e7662d6f8d7518006656e4793bc0645a1da6a2b850272bd02a438dc7e9
    role: context
  - path: data/habitats/food/soy_sauce.yaml
    sha256: 74bc4bec93bfbc648a8281e94cd574d4c5da5861486e6e197885953486ed0a87
    role: context
  - path: data/habitats/food/soybean_paste.yaml
    sha256: 14b87d00f2ded098d53c80382e15d7773c98cd780bdc2fee53c4e6c3f383d621
    role: context
  - path: data/habitats/food/spice.yaml
    sha256: df9a2f5826b6478b182766516cfdeef23905fbcaf7e4a8b30118d6b49413efb2
    role: context
  - path: data/habitats/food/sweets.yaml
    sha256: 9d6183c3cad2758d8a21c51f6118133224e289413a85c62b42290eeebb895284
    role: context
  - path: data/habitats/food/utensil.yaml
    sha256: a88185cbda6e62998f4355460f9bd2ffcdb6eb268bed70d3441e377299ef5d6d
    role: context
  - path: data/habitats/food/vegetable_oil_food_product.yaml
    sha256: a2e8e59261b2907bbdd7a7f76a5e99862b651b3995dc1c0926d01ce6589eecf9
    role: target
  - path: data/habitats/food/vinegar.yaml
    sha256: f41ed38ff6fefe105ba9c75fdc3b1e84359574e577c61990b14278a100d94c48
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
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
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
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
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
targets:
- target_id: FOODON:00001087
  path: data/habitats/food/vegetable_oil_food_product.yaml
  label: vegetable oil food product
  kind: generated
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Source identity, relation and native status
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Authored habitat definitions
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact source-path hierarchy exclusions
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Guarded imported annotation corrections
  - repository: CultureBotAI/HabitatMech
    path: data/raw
    role: Manifest-bound inventories; refresh only through governed extraction
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Generated record owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Source transform owner
scope:
  description: One complete resolved record and its source concepts.
  selection: One of13 remaining Food records after ignored-inclusive census1015/3208;
    no sampling claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - FOODON:00001087
checks:
- check_id: C11
  name: Native validate
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/food/vegetable_oil_food_product.yaml
  exit_code: 0
  target_ids:
  - FOODON:00001087
  summary: Executed 2026-10-14T17:15:10.871448Z to 2026-10-14T17:15:12.783584Z. No
    issues found
  scope_note: Schema exact target; strict13 targets; remaining gates full native scope.
    Label skips2059 unsupported-prefix pairs. Deterministic success is not scientific
    approval.
- check_id: C13
  name: Native validate-strict
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/food/seafood_product.yaml data/habitats/food/seafood_product_eurofir.yaml
    data/habitats/food/silage_fermentation.yaml data/habitats/food/sodium_chloride_salt.yaml
    data/habitats/food/solar_salt.yaml data/habitats/food/sourdough.yaml data/habitats/food/soy_sauce.yaml
    data/habitats/food/soybean_paste.yaml data/habitats/food/spice.yaml data/habitats/food/sweets.yaml
    data/habitats/food/utensil.yaml data/habitats/food/vegetable_oil_food_product.yaml
    data/habitats/food/vinegar.yaml
  exit_code: 0
  target_ids:
  - FOODON:00001087
  summary: "Executed 2026-10-14T17:15:14.677937Z to 2026-10-14T17:15:20.563528Z. uv\
    \ run python scripts/validate_strict.py data/habitats/food/seafood_product.yaml\
    \ data/habitats/food/seafood_product_eurofir.yaml data/habitats/food/silage_fermentation.yaml\
    \ data/habitats/food/sodium_chloride_salt.yaml data/habitats/food/solar_salt.yaml\
    \ data/habitats/food/sourdough.yaml data/habitats/food/soy_sauce.yaml data/habitats/food/soybean_paste.yaml\
    \ data/habitats/food/spice.yaml data/habitats/food/sweets.yaml data/habitats/food/utensil.yaml\
    \ data/habitats/food/vegetable_oil_food_product.yaml data/habitats/food/vinegar.yaml\n\
    Validating 13 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      13\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Schema exact target; strict13 targets; remaining gates full native scope.
    Label skips2059 unsupported-prefix pairs. Deterministic success is not scientific
    approval.
- check_id: C14
  name: Native validate-history
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - FOODON:00001087
  summary: 'Executed 2026-10-14T17:15:20.564224Z to 2026-10-14T17:15:27.358904Z. No
    issues found

    679 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Schema exact target; strict13 targets; remaining gates full native scope.
    Label skips2059 unsupported-prefix pairs. Deterministic success is not scientific
    approval.
- check_id: C15
  name: Native provenance-check
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - FOODON:00001087
  summary: 'Executed 2026-10-14T17:15:27.359560Z to 2026-10-14T17:15:27.933220Z. provenance
    current: 14 committed inventories, 2 GOLD sources'
  scope_note: Schema exact target; strict13 targets; remaining gates full native scope.
    Label skips2059 unsupported-prefix pairs. Deterministic success is not scientific
    approval.
- check_id: C16
  name: Native verify-corpus
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - FOODON:00001087
  summary: "Executed 2026-10-14T17:15:27.933784Z to 2026-10-14T17:15:44.440215Z. expected\
    \ 3208 records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing:\
    \ 0\n\ncorpus reproduces exactly from data/raw/"
  scope_note: Schema exact target; strict13 targets; remaining gates full native scope.
    Label skips2059 unsupported-prefix pairs. Deterministic success is not scientific
    approval.
- check_id: C17
  name: Native validate-causal-all
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - FOODON:00001087
  summary: Executed 2026-10-14T17:15:44.440896Z to 2026-10-14T17:15:48.106419Z. validated
    32 causal-graph curation file(s) with 32 graph(s)
  scope_note: Schema exact target; strict13 targets; remaining gates full native scope.
    Label skips2059 unsupported-prefix pairs. Deterministic success is not scientific
    approval.
- check_id: C18
  name: Native term-requests-check
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - FOODON:00001087
  summary: Executed 2026-10-14T17:15:48.107072Z to 2026-10-14T17:16:03.344493Z. term-request
    table is current (109 terms)
  scope_note: Schema exact target; strict13 targets; remaining gates full native scope.
    Label skips2059 unsupported-prefix pairs. Deterministic success is not scientific
    approval.
- check_id: C19
  name: Native validate-products
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - FOODON:00001087
  summary: "Executed 2026-10-14T17:16:03.345192Z to 2026-10-14T17:16:52.807179Z. id↔label\
    \ correspondence summary:\n          OK_CANONICAL: 1176\n            OK_SYNONYM:\
    \ 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2059\n\n✅ All id↔label\
    \ pairs correspond."
  scope_note: Schema exact target; strict13 targets; remaining gates full native scope.
    Label skips2059 unsupported-prefix pairs. Deterministic success is not scientific
    approval.
- check_id: QC
  name: Exact-base QC
  required: true
  status: passed
  command: gh run view 38602382356 --repo CultureBotAI/HabitatMech --json conclusion,headSha,status,url,name
  exit_code: 0
  target_ids:
  - FOODON:00001087
  evidence_ids:
  - BASE_QC
  summary: Exact-base hosted success, not final-head validation.
- check_id: ORIGINAL
  name: Original source joins
  required: false
  status: unavailable
  target_ids:
  - FOODON:00001087
  evidence_ids:
  - MEMBERS
  - GOLD_ACCESS
  summary: Original member membership not fully reconstructed.
- check_id: IMODULON
  name: Expression-module applicability
  required: false
  status: not_applicable
  target_ids:
  - FOODON:00001087
  summary: No gene/regulator/transcriptomic mechanism claim requires this adapter.
evidence:
- evidence_id: RECORD
  kind: record_content
  reference: data/habitats/food/vegetable_oil_food_product.yaml
  summary: Entire target read, including all source attestations, definitions, synonyms,
    taxa and generated history.
  accessed_at: '2026-10-14T17:29:04Z'
  support: supports
- evidence_id: RULES
  kind: authority
  reference: docs/CURATION.md; docs/HARMONIZATION.md; src/habitatmech/schema/habitatmech.yaml
  summary: Strictly broader parents, exact identity versus broader grounding, distinct
    source units, FOOD matrix category and all-source ITEM gate applied.
  accessed_at: '2026-10-14T17:29:04Z'
  support: supports
- evidence_id: ROWS
  kind: record_content
  reference: data/raw/; curation/decisions.tsv; curation/term_requests.tsv
  summary: 'BacDive row133 has7 STRAIN assertions and6 taxa; mapping row219 is lexical
    CLOSE. ITEM REVIEW1721 explains REVIEWED but not plant origin. All6 identifiers/labels
    resolve in NCBI; bacterium1869227 remains underspecified despite a species-rank
    taxonomy node. Parsed matching/comparison row locators: {"curation/decisions.tsv":
    [1721], "data/raw/bacdive_isolation_sources.tsv": [133], "data/raw/bacdive_source_taxa.tsv":
    [2014, 2015, 2016, 2017, 2018, 2019], "data/raw/isolation_source_groundings.tsv":
    [219], "data/raw/ontology_subclass_edges.tsv": [8786, 8787, 8964, 9050], "data/raw/ontology_terms.tsv":
    [10517, 10650, 10721]}'
  accessed_at: '2026-10-14T17:29:04Z'
  support: supports
- evidence_id: TRANSFORM
  kind: record_content
  reference: src/habitatmech/seed.py
  summary: 'All13 generated documents matched disk in an in-memory build; source resolution
    traces inspected. FOODON:03310387 edible oil and03460263 vegetable fat or oil
    are defensible parents of the adopted ontology class. The defect is source-to-class
    scope, not those internal ontology edges. Trace time: 2026-10-14T17:16:19.351572Z'
  accessed_at: '2026-10-14T17:29:04Z'
  support: supports
- evidence_id: SEARCH
  kind: search
  reference: curation/; history/; research/; reviews/structured/; reports/yaml_record_review/;
    data/raw/; tests/
  summary: 'Exact labels, slugs, identifiers and source mints searched including ignored
    files. No prior structured declaration for these13 targets; legacy reports are
    handled separately. Command: rg --no-ignore --hidden -l -i -F -e FOODON:00001087
    -e FOODON:03310387 -e FOODON:03460263 -e Oil-Food -e bacdive.isolation_source:oil-food
    -e habitatmech:BACDIVE.ab42f44be6 -e vegetable oil food product -e vegetable_oil_food_product
    curation history research conf reviews/structured reports/yaml_record_review data/raw
    tests'
  accessed_at: '2026-10-14T17:29:04Z'
  support: supports
  search_scope: Ignored and hidden files included in the named roots; no all-disks
    absence claim.
- evidence_id: MEMBERS
  kind: search
  reference: conf/sources.yaml; data/raw/MANIFEST.yaml; data/raw/GOLD_MANIFEST.yaml
  summary: 'Original member joins not located among 41780 enumerated repository/configured
    kg-microbe data-root files. Frozen aggregates remain available. Receipt: {"accessed_at":
    "2026-10-14T17:16:14.759372Z", "command": ["rg", "--no-ignore", "--hidden", "--files",
    ".", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"],
    "enumerated_files": 41780, "exit_code": 0, "interpretation": "Ignored/hidden files
    included within repository and configured kg-microbe data root; not an all-disks
    search.", "matches": []}'
  accessed_at: '2026-10-14T17:29:04Z'
  support: supports
  search_scope: Ignored and hidden files included in the named roots; no all-disks
    absence claim.
- evidence_id: GOLD_ACCESS
  kind: database
  reference: https://gold.jgi.doe.gov/
  summary: 'Four study routes returned403 and12 ecosystem routes returned404; unsupported
    routes/access failures do not invalidate frozen identifiers. No inaccessible page
    text inferred. {"Gs0150294": {"accessed_at": "2026-10-14T17:16:19.395929Z", "error":
    "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150294"},
    "Gs0150545": {"accessed_at": "2026-10-14T17:16:19.448250Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150545"}, "Gs0154236":
    {"accessed_at": "2026-10-14T17:16:19.492924Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0154236"}, "Gs0154282": {"accessed_at":
    "2026-10-14T17:16:19.538126Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"},
    "gold.ecosystem:3500": {"accessed_at": "2026-10-14T17:16:20.077949Z", "error":
    "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/3500"},
    "gold.ecosystem:5327": {"accessed_at": "2026-10-14T17:16:20.586256Z", "error":
    "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5327"},
    "gold.ecosystem:5531": {"accessed_at": "2026-10-14T17:16:21.754293Z", "error":
    "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5531"},
    "gold.ecosystem:5598": {"accessed_at": "2026-10-14T17:16:20.793466Z", "error":
    "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5598"},
    "gold.ecosystem:5749": {"accessed_at": "2026-10-14T17:16:21.030470Z", "error":
    "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5749"},
    "gold.ecosystem:5895": {"accessed_at": "2026-10-14T17:16:21.188135Z", "error":
    "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5895"},
    "gold.ecosystem:5930": {"accessed_at": "2026-10-14T17:16:19.929021Z", "error":
    "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5930"},
    "gold.ecosystem:5936": {"accessed_at": "2026-10-14T17:16:21.446475Z", "error":
    "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5936"},
    "gold.ecosystem:7230": {"accessed_at": "2026-10-14T17:16:19.696737Z", "error":
    "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/7230"},
    "gold.ecosystem:8057": {"accessed_at": "2026-10-14T17:16:20.239866Z", "error":
    "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/8057"},
    "gold.ecosystem:8058": {"accessed_at": "2026-10-14T17:16:20.406608Z", "error":
    "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/8058"},
    "gold.ecosystem:8314": {"accessed_at": "2026-10-14T17:16:21.617486Z", "error":
    "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/8314"}}'
  accessed_at: '2026-10-14T17:29:04Z'
  support: supports
- evidence_id: ONTOLOGY
  kind: database
  reference: https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl
  summary: 'Pinned full OWL definitions, parents and restrictions inspected, alongside
    current OLS ENVO/FoodOn identifiers, labels and active status. FOODON:03310387
    edible oil and03460263 vegetable fat or oil are defensible parents of the adopted
    ontology class. The defect is source-to-class scope, not those internal ontology
    edges. Retrieval receipt: {"accessed_at": "2026-10-14T12:27:42.074174Z", "sha256":
    "b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf", "url": "https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl"}.'
  accessed_at: '2026-10-14T12:27:42.074174Z'
  support: supports
- evidence_id: OLS
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/
  summary: 'Current term receipts; checking candidates does not import them or refresh
    the frozen ontology slice. {"ENVO-00003030.json": {"accessed_at": "2026-10-14T17:16:00.856704Z",
    "sha256": "8568d75af6ec12c7802152ed56ea5111b5cd7c8a8c17c32aa9fee10a2eb96ef9",
    "url": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00003030"},
    "ENVO-01000508.json": {"accessed_at": "2026-10-14T17:16:01.557474Z", "sha256":
    "9cce974181ae166d71b729c8674d932629b99cd9d813bb646a5a19444aabc628", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000508"},
    "ENVO-01000681.json": {"accessed_at": "2026-10-14T17:16:02.265470Z", "sha256":
    "f74be5e8bf0059667736fabaaae7b1596d629b5f6a653bf139c7e00017f53293", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000681"},
    "ENVO-03501263.json": {"accessed_at": "2026-10-14T17:16:02.960918Z", "sha256":
    "97a307b453b6b6cf1060f13573dceeeed75f1a9de1f58f99eed982d8b9adacf1", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03501263"},
    "ENVO-03501327.json": {"accessed_at": "2026-10-14T17:16:03.628104Z", "sha256":
    "1964b6e5bf8f83111d1824aabbb91ad7b91972ecefd4a99174c81271407eebde", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03501327"},
    "ENVO-03600040.json": {"accessed_at": "2026-10-14T17:16:04.322977Z", "sha256":
    "29f399d45596f0435ee5baf761667c32bb8e83184ec782e7141c97077113f490", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03600040"},
    "FOODON-00001046.json": {"accessed_at": "2026-10-14T17:19:30.172322Z", "sha256":
    "edb13c2554689c15f149f859da114b5bcf00045a54e59ac30c412ff3a4866bcd", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001046"},
    "FOODON-00001073.json": {"accessed_at": "2026-10-14T17:16:04.981644Z", "sha256":
    "07b71752b62fb311191ddb2ddf944c5cea859c3932f29ebe227f9433bd782334", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001073"},
    "FOODON-00001078.json": {"accessed_at": "2026-10-14T17:19:28.111825Z", "sha256":
    "a6709b4a437bf29c657ba98b6dcd8838bb8b4604a58108e2b4c9f4efe8b5bae7", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001078"},
    "FOODON-00001087.json": {"accessed_at": "2026-10-14T17:16:05.737513Z", "sha256":
    "d3278deb470abc548d7ebc211a79b0fcb4ae9613af9d014429ef1a0657da16ae", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001087"},
    "FOODON-00001149.json": {"accessed_at": "2026-10-14T17:16:06.476720Z", "sha256":
    "0b2e8311c42fe85e045b52639da23342f23555c42c4683c4d8de165f81e5be81", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001149"},
    "FOODON-00001210.json": {"accessed_at": "2026-10-14T17:19:25.096735Z", "sha256":
    "dcdd505a2ba7427d6a210337d7c311ef6739c3db0d57d166257aa0e7c60dc11e", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001210"},
    "FOODON-00001235.json": {"accessed_at": "2026-10-14T17:19:28.759933Z", "sha256":
    "6a1218a1a52c4076b26510eb33ae8d93da988bb4ef603aa0520db387065858d8", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001235"},
    "FOODON-00001258.json": {"accessed_at": "2026-10-14T17:16:07.054895Z", "sha256":
    "3a9437d82255b394ac38aebbde2f83013f772b4affdb4e800a7d847f4be59a24", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00001258"},
    "FOODON-00002266.json": {"accessed_at": "2026-10-14T17:19:26.498681Z", "sha256":
    "4fd5eed1989b3c3eaafcef84c2a604167d8cd9a909d1022ad042780f487ef8a4", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A00002266"},
    "FOODON-03301115.json": {"accessed_at": "2026-10-14T17:19:29.430370Z", "sha256":
    "401aa9bfe630db50ea259b7015b622706e0410c498efb590fda49aa753d1d369", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03301115"},
    "FOODON-03301705.json": {"accessed_at": "2026-10-14T17:16:07.785283Z", "sha256":
    "46d3b3f7ff4459f770cbe4398efc09b87b0ba75107f6c0232440dd127f9dba74", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03301705"},
    "FOODON-03302481.json": {"accessed_at": "2026-10-14T17:16:08.467305Z", "sha256":
    "b2cd9bbb85b36495ea8ecd2145646146f830f50daa3b46eb37f1f946a9e773a2", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03302481"},
    "FOODON-03303220.json": {"accessed_at": "2026-10-14T17:16:09.132583Z", "sha256":
    "9797bca63d1713a1b6538605885b98199bb669beb34ef487e0a35c85a225ce1f", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03303220"},
    "FOODON-03303380.json": {"accessed_at": "2026-10-14T17:16:09.882851Z", "sha256":
    "9b177c23e89117bd634cafca67417ed82cd16a829d62e4035fd9b0e1aa5bae24", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03303380"},
    "FOODON-03304099.json": {"accessed_at": "2026-10-14T17:16:11.128136Z", "sha256":
    "a80d8b9c60b9049d26e9b8a50e44a0f24cceac6cdcc552ec19fb4015ef708ed0", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03304099"},
    "FOODON-03304996.json": {"accessed_at": "2026-10-14T17:16:12.669898Z", "sha256":
    "94bf5dfac4f70de17eb308a56b8c316b6c8feb527dab81a05d222a5d2ce3a434", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03304996"},
    "FOODON-03306052.json": {"accessed_at": "2026-10-14T17:16:13.561198Z", "sha256":
    "13da1f9711d824fb46ab8485c4071005b03afeb0da3a7a5bbb5ae828ed29651c", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03306052"},
    "FOODON-03310002.json": {"accessed_at": "2026-10-14T17:16:14.258866Z", "sha256":
    "333cc7837da5fd72aa4c1f35c346976afd06ce3ee1a50a82d06e2527ab6de2c5", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03310002"},
    "FOODON-03310005.json": {"accessed_at": "2026-10-14T17:19:27.341290Z", "sha256":
    "2a69e4de49c6f5b0265cc9334e6208de07afe3967b40932ed4eb0db80b737b47", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03310005"},
    "FOODON-03310387.json": {"accessed_at": "2026-10-14T17:16:14.997310Z", "sha256":
    "47fb2b0557cbf8357b38529d66dca9babbdf4ae2bd6b19477108ae71462cc779", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03310387"},
    "FOODON-03316428.json": {"accessed_at": "2026-10-14T17:16:15.659460Z", "sha256":
    "96931104d414a1aaa4796d8d18ade9e5119c063650e7390f5a767e081776843d", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03316428"},
    "FOODON-03316449.json": {"accessed_at": "2026-10-14T17:19:24.446919Z", "sha256":
    "5b673a9cabe9392f4c989ffb4571c6d904f470fd7c3b207602e6b5522c08d9b3", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03316449"},
    "FOODON-03400801.json": {"accessed_at": "2026-10-14T17:16:16.244341Z", "sha256":
    "023ca9f5f8e40d2118268da930571a3f0c98feb0b91587a66ccd638b36d49bf1", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03400801"},
    "FOODON-03400803.json": {"accessed_at": "2026-10-14T17:16:16.864039Z", "sha256":
    "c003d98e653d79a8878791cab35bf0f10002d6184ff9bffa1f2e3b6ef91013e0", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03400803"},
    "FOODON-03411345.json": {"accessed_at": "2026-10-14T17:19:25.842441Z", "sha256":
    "a688a4b71fdfb89269ea7b90e1a78be5ff6db5fb412f8c8d4f97db5f47c2138b", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03411345"},
    "FOODON-03460263.json": {"accessed_at": "2026-10-14T17:16:17.541063Z", "sha256":
    "9463e270fb56b69e35e0e8e1c66d621ad3385a5d330165176e10fcf1869ae144", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03460263"},
    "FOODON-03530206.json": {"accessed_at": "2026-10-14T17:16:18.276086Z", "sha256":
    "e209164474c7a06365bce7cdbc1f24ff58a283bc848d26221295686958abaf4e", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03530206"},
    "FOODON-03544457.json": {"accessed_at": "2026-10-14T17:16:18.970258Z", "sha256":
    "8042724409933b9628739f09b41316dea6cb936a51dfc413a62b5762c77d15f8", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03544457"}}'
  accessed_at: '2026-10-14T17:29:04Z'
  support: supports
- evidence_id: PRIMARY
  kind: primary_source
  reference: https://bacdive.dsmz.de/isolation-sources
  summary: 'Current BacDive isolation category listing distinguishes Oil (Food) from
    Oil (Fuel). This supports food context, not plant-only origin or recovery of original7
    joins. Retrieval receipt: {"accessed_at": "2026-10-14T17:19:34.727310Z", "sha256":
    "60f9932f434230027051edf3e35a6e3af4d52d2812eda2e7088ea9228ffef9de", "url": "https://bacdive.dsmz.de/isolation-sources"}.'
  accessed_at: '2026-10-14T17:19:34.727310Z'
  support: supports
- evidence_id: TAXONOMY
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&retmode=xml&id=1077144,1122129,1122211,112331,1123359,1129374,121872,1227498,1238186,1262550,1280,1281,1294022,129985,135826,1423716,1455608,147248,157227,1590,1631871,1690008,179010,1869227,1879320,1881060,261164,282669,43666,47846,69373
  summary: 'Every imported identifier/label resolves. Mixed strain/species ranks are
    not equated. Association counts and ranking are not characteristic-enrichment
    proof. [{"current": {"identifier": "69373", "name": "Curtobacterium pusillum",
    "names": ["Brevibacterium pusillum", "Curtobacterium sp. IFO12674", "Curtobacterium
    sp. IFO 12674T", "Curtibacterium pusillum", "Curtibacterium sp. IFO 12674T", "Curtibacterium
    sp. IFO12674"], "rank": "species"}, "stored": {"association_count": 2, "candidate_pool":
    6, "rank": 1, "source": "BACDIVE", "taxon_id": "NCBITaxon:69373", "taxon_label":
    "Curtobacterium pusillum"}}, {"current": {"identifier": "1280", "name": "Staphylococcus
    aureus", "names": ["Micrococcus aureus", "Micrococcus pyogenes", "Staphylococcus
    aureus subsp. anaerobius", "Staphylococcus pyogenes aureus", "Staphylococcus pyogenes
    citreus", "Staphylococcus aureus subsp. aureus", "Staphylococcus sp. CCUG 17621",
    "Staphylococcus sp. Fddn_Aq4"], "rank": "species"}, "stored": {"association_count":
    1, "candidate_pool": 6, "rank": 2, "source": "BACDIVE", "taxon_id": "NCBITaxon:1280",
    "taxon_label": "Staphylococcus aureus"}}, {"current": {"identifier": "1869227",
    "name": "bacterium", "names": ["Bacteria bacterium", "Bacteria sp.", "Bacterial
    sp.", "Bacterium sp.", "Unknown eubacteria", "Unknown eubacterium", "unclassified
    bacterium", "unidentified bacteria", "unidentified bacterium", "unidentified eubacterium",
    "unknown bacteria"], "rank": "species"}, "stored": {"association_count": 1, "candidate_pool":
    6, "rank": 3, "source": "BACDIVE", "taxon_id": "NCBITaxon:1869227", "taxon_label":
    "bacterium"}}, {"current": {"identifier": "1881060", "name": "Clostridium sp.
    USBA 49", "names": [], "rank": "species"}, "stored": {"association_count": 1,
    "candidate_pool": 6, "rank": 4, "source": "BACDIVE", "taxon_id": "NCBITaxon:1881060",
    "taxon_label": "Clostridium sp. USBA 49"}}, {"current": {"identifier": "43666",
    "name": "Paeniglutamicibacter sulfureus", "names": ["Arthrobacter sulfureus",
    "Arthrobacter sp. BZ73"], "rank": "species"}, "stored": {"association_count":
    1, "candidate_pool": 6, "rank": 5, "source": "BACDIVE", "taxon_id": "NCBITaxon:43666",
    "taxon_label": "Paeniglutamicibacter sulfureus"}}, {"current": {"identifier":
    "47846", "name": "Brachybacterium conglomeratum", "names": ["Micrococcus conglomeratus"],
    "rank": "species"}, "stored": {"association_count": 1, "candidate_pool": 6, "rank":
    6, "source": "BACDIVE", "taxon_id": "NCBITaxon:47846", "taxon_label": "Brachybacterium
    conglomeratum"}}] Retrieval receipt: {"accessed_at": "2026-10-14T17:16:04.218285Z",
    "sha256": "c2d205c95a1497fe847855cbea5a30384fa2b305a04c7079820dff71a67c6043",
    "url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&retmode=xml&id=1077144,1122129,1122211,112331,1123359,1129374,121872,1227498,1238186,1262550,1280,1281,1294022,129985,135826,1423716,1455608,147248,157227,1590,1631871,1690008,179010,1869227,1879320,1881060,261164,282669,43666,47846,69373"}.'
  accessed_at: '2026-10-14T17:16:04.218285Z'
  support: supports
- evidence_id: BASE_QC
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38602382356
  summary: 'Exact-base authoritative queue QC succeeded; predates new review files
    and future fixes. Retrieval receipt: {"accessed_at": "2026-10-14T17:26:22Z"}.'
  accessed_at: '2026-10-14T17:26:22Z'
  support: supports
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Source identity
  outcome: concern
  target_ids:
  - FOODON:00001087
  evidence_ids:
  - RECORD
  - ROWS
  - ONTOLOGY
  - PRIMARY
  summary: FOODON:00001087 is plant-derived oil. BacDive Oil-Food distinguishes food
    oil from fuel, not necessarily plant from animal oil. The ITEM rationale defends
    only food-product framing, leaving the plant restriction unsupported; no actual
    animal-oil member is claimed recovered.
- assessment_id: HIERARCHY
  area: grounding
  topic: Strict genus
  outcome: supported
  target_ids:
  - FOODON:00001087
  evidence_ids:
  - RECORD
  - RULES
  - ROWS
  - TRANSFORM
  - ONTOLOGY
  summary: FOODON:03310387 edible oil and03460263 vegetable fat or oil are defensible
    parents of the adopted ontology class. The defect is source-to-class scope, not
    those internal ontology edges.
- assessment_id: PROVENANCE
  area: provenance
  topic: Source assertions and units
  outcome: supported
  target_ids:
  - FOODON:00001087
  evidence_ids:
  - ROWS
  - TRANSFORM
  summary: BacDive row133 has7 STRAIN assertions and6 taxa; mapping row219 is lexical
    CLOSE. ITEM REVIEW1721 explains REVIEWED but not plant origin. All6 identifiers/labels
    resolve in NCBI; bacterium1869227 remains underspecified despite a species-rank
    taxonomy node.
- assessment_id: DEFINITION
  area: evidence
  topic: Definitions and synonym scope
  outcome: supported
  target_ids:
  - FOODON:00001087
  evidence_ids:
  - RECORD
  - ROWS
  - ONTOLOGY
  summary: Present definitions/synonyms retain the inspected owner scope. Missing
    optional definitions are not automatically a defect.
- assessment_id: PARAMETERS
  area: quantity
  topic: Environmental parameters
  outcome: not_applicable
  target_ids:
  - FOODON:00001087
  evidence_ids:
  - RECORD
  - ROWS
  summary: No environmental-parameter assertion present; neighboring triads and generic
    literature ranges are not inherited.
- assessment_id: TAXA
  area: evidence
  topic: Association versus characteristic presence
  outcome: supported
  target_ids:
  - FOODON:00001087
  evidence_ids:
  - RECORD
  - ROWS
  - TAXONOMY
  summary: Imported taxon identifiers/labels and count/rank/pool retained; these are
    reported associations, not habitat enrichment. Original joins remain unavailable.
- assessment_id: CAUSAL
  area: graph
  topic: Mechanism evidence
  outcome: not_applicable
  target_ids:
  - FOODON:00001087
  evidence_ids:
  - RECORD
  - SEARCH
  summary: No causal graph or claim-level mechanism asserted; optional absence is
    not a defect.
- assessment_id: STATUS
  area: scope
  topic: Native status gates
  outcome: supported
  target_ids:
  - FOODON:00001087
  evidence_ids:
  - ROWS
  - TRANSFORM
  summary: ITEM versus CLASS/default resolution explains current native status; this
    review does not promote it.
- assessment_id: OWNERS
  area: ownership
  topic: Generated boundaries
  outcome: supported
  target_ids:
  - FOODON:00001087
  evidence_ids:
  - RULES
  - TRANSFORM
  summary: Fix maintained decisions/exclusions/definitions and regenerate, never patch
    generated YAML/pages.
- assessment_id: LIMITS
  area: completeness
  topic: Member-level limitations
  outcome: unknown
  target_ids:
  - FOODON:00001087
  evidence_ids:
  - MEMBERS
  - GOLD_ACCESS
  summary: Frozen aggregates reproduce but missing original joins limit scope certification.
    No SSSOM/KGX or whole-corpus readiness claim.
findings:
- finding_id: F1
  issue_key: vegetable-oil-food-product-source-identity-scope
  title: Source concept and adopted habitat identity have unresolved scope
  description: FOODON:00001087 is plant-derived oil. BacDive Oil-Food distinguishes
    food oil from fuel, not necessarily plant from animal oil. The ITEM rationale
    defends only food-product framing, leaving the plant restriction unsupported;
    no actual animal-oil member is claimed recovered. FOODON:03310387 edible oil and03460263
    vegetable fat or oil are defensible parents of the adopted ontology class. The
    defect is source-to-class scope, not those internal ontology edges.
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  target_ids:
  - FOODON:00001087
  field_paths:
  - identifier
  - source_attestations.mapping_predicate
  - parent_habitats
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never hand-edit generated records
  - repository: CultureBotAI/HabitatMech
    path: data/raw
    role: Maintained input or generator; never hand-edit generated records
  evidence_ids:
  - RECORD
  - RULES
  - ROWS
  - TRANSFORM
  - ONTOLOGY
  - PRIMARY
  rule_id: Exact source identity and strictly broader habitat parents
  native_severity: major
  normalization_reason: Materially unsupported identity or genus.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - FOODON:00001087
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never hand-edit generated records
  - repository: CultureBotAI/HabitatMech
    path: data/raw
    role: Maintained input or generator; never hand-edit generated records
  description: Recover original source/member context and make an explicit ITEM decision
    for each contributing concept. Retain a source mint or use a demonstrated exact
    term; do not force a near match. For silage resolve process versus material first.
    For a changed identity update guarded parents, path locks and redirects through
    native generators; no generic predicate swap.
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Change maintained inputs only; dry seed and inspect canary before wider regeneration.
  - Preserve source attestations, independent valid parents and honest native status;
    prove exact corpus delta.
  - Validate schema, history, reproduction, site and QC; append immutable successor
    with exact previous occurrence.
limitations:
- Same-agent assessment, not independent approval or native status promotion.
- Original source joins unavailable; counts are frozen aggregates, not independently
  recovered specimen membership.
- Current ontology checks are bounded candidate verification, not a full snapshot
  refresh.
- This pre-fix observation does not certify SSSOM/KGX products or all corpus records.
- Legacy reports remain historical; no clean assessment silently closes an older unresolved
  finding.
notes:
- Original input hashes unchanged at extended capture 2026-10-14T17:26:56Z.
tags:
- habitatmech
- record-review
- food
```
