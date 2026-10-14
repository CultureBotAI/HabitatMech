# Scientific record review: food (spoiled)

- Review: 20261014T123817Z-food_spoiled
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T12:23:41.679761Z
- Finished UTC: 2026-10-14T12:38:17.888694Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

FOODON:00003366 denotes food made unsuitable for ingestion by spoilage; FOODON:00002454 is its supported food-material parent. BacDive Spoiled is retained as a related synonym and CLOSE mapping. Independently inspected rotten tofu residue, spoiled canned food and rotting onion examples positively support the displayed taxa as plausible spoiled-food associates, not universal causes of spoilage.

## Scope And Provenance

Entire resolved record and all contributing source concepts; one individual scientific observation.

Selection: Next eight unreviewed Food records after ignored-inclusive census:991/3208 current records,23/60 Food. This bundle declares one target, not a corpus pass.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 07f8ab6c05a1c96de39e2475f306a271ee17243c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| FOODON:00003366 | data/habitats/food/food_spoiled.yaml | generated | food (spoiled) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | FOODON:00003366 | Executed 2026-10-14T12:23:55.373793Z to 2026-10-14T12:23:57.385182Z. No issues found |
| Native validate-strict | passed | True | FOODON:00003366 | Executed 2026-10-14T12:23:59.573723Z to 2026-10-14T12:24:05.058517Z. uv run python scripts/validate_strict.py data/habitats/food/fish_products.yaml data/habitats/food/food_fermented.yaml data/habitats/food/food_preserved.yaml data/habitats/food/food_product.yaml data/habitats/food/food_production.yaml data/habitats/food/food_sample.yaml data/habitats/food/food_spoiled.yaml data/habitats/food/frozen_seafood.yaml<br>Validating 8 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      8<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| Native validate-history | passed | True | FOODON:00003366 | Executed 2026-10-14T12:24:05.059204Z to 2026-10-14T12:24:11.861728Z. No issues found<br>666 history record(s) valid against src/habitatmech/schema/history.yaml |
| Native provenance-check | passed | True | FOODON:00003366 | Executed 2026-10-14T12:24:11.862316Z to 2026-10-14T12:24:12.425647Z. provenance current: 14 committed inventories, 2 GOLD sources |
| Native verify-corpus | passed | True | FOODON:00003366 | Executed 2026-10-14T12:24:12.426275Z to 2026-10-14T12:24:26.823825Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| Native validate-causal-all | passed | True | FOODON:00003366 | Executed 2026-10-14T12:24:26.824468Z to 2026-10-14T12:24:30.461288Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| Native term-requests-check | passed | True | FOODON:00003366 | Executed 2026-10-14T12:24:30.461871Z to 2026-10-14T12:24:44.827612Z. term-request table is current (109 terms) |
| Native validate-products | passed | True | FOODON:00003366 | Executed 2026-10-14T12:24:44.828194Z to 2026-10-14T12:25:27.849380Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1176<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2059<br><br>✅ All id↔label pairs correspond. |
| Exact-base authoritative hosted QC | passed | True | FOODON:00003366 | Exact unchanged scientific-input base passed; new report archive must still be checked. |
| Original membership reconstruction | unavailable | False | FOODON:00003366 | Original source members not located in bounded ignored-inclusive search; 24 GOLD pages HTTP403. |
| Expression-module applicability | not_applicable | False | FOODON:00003366 | No gene/regulator/protein/expression mechanism is asserted. Habitat occurrences are not expression evidence. |

## Scientific And Domain Assessments

### Habitat identity and strict hierarchy

identity: supported. Targets: FOODON:00003366.

FOODON:00003366 denotes food made unsuitable for ingestion by spoilage; FOODON:00002454 is its supported food-material parent. BacDive Spoiled is retained as a related synonym and CLOSE mapping. Independently inspected rotten tofu residue, spoiled canned food and rotting onion examples positively support the displayed taxa as plausible spoiled-food associates, not universal causes of spoilage.

### Field-by-field source interpretation and original units

evidence: supported. Targets: FOODON:00003366.

BacDive isolation row 149 has three STRAIN assertions and three taxa. Mapping row 290 closeMatch is endorsed by ITEM REVIEW decision 1720; CLOSE/REVIEWED is mechanically correct. All three taxon entries have count one, ranks 1-3 and pool three, matching raw inputs and current NCBI labels. Current strain examples are not a reconstruction of the unavailable frozen strain join. No characteristic flags, numerical habitat parameters or causal claims are asserted.

### Native gates and omitted optional claims

provenance: supported. Targets: FOODON:00003366.

Current CLOSE/REVIEWED follows source decisions. All source taxon fields reproduce their frozen rows, without is_characteristic assertions. No unsupported parameter, causal, evidence or discussion fields are invented; optional absence alone is not a defect.

### Missing original membership and broader certification

completeness: unknown. Targets: FOODON:00003366.

Original joins and GOLD page contents are unavailable. Positive current strain examples do not reconstruct frozen membership. Qualified passes apply to present target claims, not all ancestors, complete curation or whole-corpus science.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| RECORD | data/habitats/food/food_spoiled.yaml | supports | Entire target YAML and history read; all present claims assessed. |
| SOURCE_ROWS | data/raw/; curation/decisions.tsv | supports | BacDive isolation row 149 has three STRAIN assertions and three taxa. Mapping row 290 closeMatch is endorsed by ITEM REVIEW decision 1720; CLOSE/REVIEWED is mechanically correct. All three taxon entries have count one, ranks 1-3 and pool three, matching raw inputs and current NCBI labels. Current strain examples are not a reconstruction of the unavailable frozen strain join. No characteristic flags, numerical habitat parameters or causal claims are asserted. Search-row ledger (includes neighboring comparison rows): {"curation/decisions.tsv": [1720], "data/raw/bacdive_isolation_sources.tsv": [149], "data/raw/bacdive_source_taxa.tsv": [2608, 2609, 2610], "data/raw/isolation_source_groundings.tsv": [290], "data/raw/ontology_subclass_edges.tsv": [8864, 8881, 8942, 8971, 9048], "data/raw/ontology_terms.tsv": [10573, 10585]} |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md | supports | Applied habitat-versus-process identity, strict genus, exact source units, MIxS roles, optional-field and all-source ITEM rules. |
| TRANSFORMS | src/habitatmech/seed.py; src/habitatmech/extract.py; src/habitatmech/curate/record_annotation_corrections.py | supports | Immediate GOLD hierarchy and ontology subclass contributions are distinct. Source inventory labels and rank/count fields are copied. Imported ontology synonyms are flattened to exact; guarded annotation corrections allow local scope repairs. Parameters require exactly one term ID. Reproducibility is not biological evidence. |
| FOODON | https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl | supports | Pinned full RDF/XML inspected for definitions, named parents, restrictions and synonym predicates. FOODON:00003366 denotes food made unsuitable for ingestion by spoilage; FOODON:00002454 is its supported food-material parent. BacDive Spoiled is retained as a related synonym and CLOSE mapping. Independently inspected rotten tofu residue, spoiled canned food and rotting onion examples positively support the displayed taxa as plausible spoiled-food associates, not universal causes of spoilage. Download SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf. |
| ENVO | https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl | supports | Pinned full ENVO inspected: obsolete ENVO:00002002 has replacement FOODON:00001002. Fermentation starter, manufactured product and alcohol fermentation pit are distinct material/context concepts; triad roles must not be collapsed. Download SHA256 a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c. |
| SEARCH | curation/; history/; research/; reviews/structured/; data/raw/; reports/yaml_record_review/; tests/ | supports | Ignored-inclusive searches for exact IDs, mints, slugs and paths; all matching raw/decision TSV rows parsed. Census: 1416 bundles; no prior declarations of these eight exact targets or collisions for seven proposed issue keys. Search command: rg --no-ignore --hidden -l -i -F -e FOODON:00002454 -e FOODON:00003366 -e Spoiled -e bacdive.isolation_source:spoiled -e food (spoiled) -e food_spoiled -e habitatmech:BACDIVE.9f2d319999 curation history research conf reviews/structured reports/yaml_record_review data/raw tests |
| AVAILABILITY | conf/sources.yaml | supports | Ignored-inclusive enumeration covered 41379 files in repository and configured kg-microbe data root. Original GOLD/BacDive/PREGO/MADIN member dumps were not located within these roots. Frozen aggregates are available; no global absence claim. |
| GOLD_ACCESS | https://gold.jgi.doe.gov/ | supports | All 24 requested exact own-path study URLs returned HTTP 403. No original members or page contents inferred. {"Gs0053258": {"accessed_at": "2026-10-14T12:24:46.231486Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0053258"}, "Gs0111475": {"accessed_at": "2026-10-14T12:24:46.356130Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0111475"}, "Gs0114546": {"accessed_at": "2026-10-14T12:24:46.386520Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0114546"}, "Gs0114789": {"accessed_at": "2026-10-14T12:24:46.418493Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0114789"}, "Gs0118570": {"accessed_at": "2026-10-14T12:24:46.467904Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0118570"}, "Gs0132984": {"accessed_at": "2026-10-14T12:24:46.503783Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0132984"}, "Gs0133014": {"accessed_at": "2026-10-14T12:24:46.542534Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0133014"}, "Gs0133290": {"accessed_at": "2026-10-14T12:24:46.572104Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0133290"}, "Gs0133298": {"accessed_at": "2026-10-14T12:24:46.613460Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0133298"}, "Gs0134604": {"accessed_at": "2026-10-14T12:24:46.727244Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0134604"}, "Gs0135060": {"accessed_at": "2026-10-14T12:24:46.849688Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0135060"}, "Gs0141928": {"accessed_at": "2026-10-14T12:24:46.883936Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0141928"}, "Gs0142247": {"accessed_at": "2026-10-14T12:24:46.926691Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0142247"}, "Gs0142315": {"accessed_at": "2026-10-14T12:24:46.971280Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0142315"}, "Gs0150392": {"accessed_at": "2026-10-14T12:24:47.022306Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150392"}, "Gs0150427": {"accessed_at": "2026-10-14T12:24:47.054567Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150427"}, "Gs0150438": {"accessed_at": "2026-10-14T12:24:47.084254Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150438"}, "Gs0150695": {"accessed_at": "2026-10-14T12:24:47.127172Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150695"}, "Gs0150720": {"accessed_at": "2026-10-14T12:24:47.170716Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150720"}, "Gs0153815": {"accessed_at": "2026-10-14T12:24:47.207422Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153815"}, "Gs0153827": {"accessed_at": "2026-10-14T12:24:47.249405Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153827"}, "Gs0153978": {"accessed_at": "2026-10-14T12:24:47.381357Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153978"}, "Gs0154236": {"accessed_at": "2026-10-14T12:24:47.424245Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154236"}, "Gs0154282": {"accessed_at": "2026-10-14T12:24:47.454274Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"}} |
| BASE_QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38561093379 | supports | Exact base 07f8ab6c05a1c96de39e2475f306a271ee17243c completed successfully: 1111 passed, three skipped; four contract tests passed; all authoritative gates passed. New bundles still require archive validation. |
| TAXONOMY | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;retmode=xml&amp;id=1004261,1007676,104097,104099,104101,1045004,1045854,104955,1050107,1051653,1051659,1054041,1074467,1076596,1089442,1091038,1110509,1114972,1121126,1121295,1121312,1121314,1121384,1121941,1122129,1122147,1122148,1122149,1122150,1122151,1122211,1122219,1122618,1123359,1123500,1123687,113557,114090,115541,1167631,120045,1202668,1206774,1220595,1247,1255632,1281,1307912,1405,1408434,1423830,1580,1588,1590,1591,1614,1629,174587,176292,1896336,214326,2338647,261164,2748,28038,282669,291615,292,36987,42895,438,442,457427,47714,51663,53444,545534,549,577,600645,615,61646,647,651,795797,865,86956 | supports | All 87 unique IDs across 88 displayed entries resolve in current NCBI. Historical genus names do not imply different taxa. Food-product 1121384/1408434 merge to the same current strain; 36987 is a termite. All preserved/spoiled labels agree. Full raw-field audit for this target: {"all_displayed_fields_match_raw": true, "by_source": {"BACDIVE": 3}, "displayed": 3, "source_rows": {"BACDIVE": 3}, "taxa": [{"corroborated_by": [], "count": 1, "identifier": "NCBITaxon:2338647", "label": "Ottowia konkukae", "pool": 3, "rank": 1, "score": null, "source": "BACDIVE"}, {"corroborated_by": [], "count": 1, "identifier": "NCBITaxon:291615", "label": "Thermoanaerobacter mathranii subsp. alimentarius", "pool": 3, "rank": 2, "score": null, "source": "BACDIVE"}, {"corroborated_by": [], "count": 1, "identifier": "NCBITaxon:292", "label": "Burkholderia cepacia", "pool": 3, "rank": 3, "score": null, "source": "BACDIVE"}]} Download SHA256 1d7925cd89404cfa893114d28979276fe1b7291cf4f91ea6b7f69f433ab3c04e. |
| BIJI | https://pubmed.ncbi.nlm.nih.gov/30222093/ | supports | PMID 30222093; DOI 10.1099/ijsem.0.003009. Abstract identifies Ottowia konkukae SK3863/DSM105395 isolated from rotten tofu residue. Download SHA256 94818fe6d34848e371784cc161e61d47aa4a50bb81a2235d204e226699d22aa9. |
| CIP | https://catalogue-crbip.pasteur.fr/fiche_catalogue.xhtml?crbip=CIP+108280 | supports | CIP 108280 type strain AIP505-99, Thermoanaerobacter mathranii subsp. alimentarius, has explicit spoiled canned food isolation annotation. Download SHA256 d84da7dabf117290439f2a94e0fb4c1ef8a18c0d6b470ad94e149e54bedf7073. |
| ONION | https://bacdive.dsmz.de/strain/157311 | supports | BacDive 157311 identifies Burkholderia cepacia IMI347462/taxid292 from rotting onion, with Spoiled source classification. Supports a spoiled food example, not unique habitat preference. Download SHA256 32e2b7946a7224afd98a40d1149de383a735583ca11e15eacd33dd04bf260466. |

## Limits And Additional Notes

- Same-agent assessment, not independent approval.
- Original members unavailable; occurrence edges, strain joins, taxa, biosamples and study unions have different denominators and are not summed.
- Pinned full ontology and current taxonomy checks are evidence, not an automatic ontology/taxonomy refresh.
- This observation captures pre-fix inputs; no scientific inputs changed while reviewing. Publication and fixes are separately authorized.
- No SSSOM/KGX certification, native status promotion or historical finding closure follows from validation.
- Exact-base QC predates these new reports; post-save archive validation remains required.
- Additional inputs assessed 2026-10-14T12:30:22.497207Z; all original input hashes rechecked unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T123817Z-food_spoiled
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: food (spoiled)'
started_at: '2026-10-14T12:23:41.679761Z'
finished_at: '2026-10-14T12:38:17.888694Z'
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
verdict: pass_with_limitations
summary: FOODON:00003366 denotes food made unsuitable for ingestion by spoilage; FOODON:00002454
  is its supported food-material parent. BacDive Spoiled is retained as a related
  synonym and CLOSE mapping. Independently inspected rotten tofu residue, spoiled
  canned food and rotting onion examples positively support the displayed taxa as
  plausible spoiled-food associates, not universal causes of spoilage.
source:
  git_revision: 07f8ab6c05a1c96de39e2475f306a271ee17243c
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
    sha256: 0eb5954aae8dc00a1cdf990431a27942e477e028a7d3945c28e3a05d03ce7a30
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: 986b4373d4d75cc5b348689c5eccdae54a3b906be1d885d9bbfc33d8641fe7fa
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
  - path: data/habitats/engineered/engineered__900b76ad.yaml
    sha256: 85154c9542e8e033e17cf631b06a462612229f3bcfdc1cdca0fc6cf73b9b9364
    role: context
  - path: data/habitats/food/fish_products.yaml
    sha256: 5435e216e51f243842916c2e4199123992c81ab166b0746963ffeee71f5253b3
    role: context
  - path: data/habitats/food/food_fermented.yaml
    sha256: 36914b14c9b027073981cfd96d2932852f74f76a597275d6d4e52b9a98da8d70
    role: context
  - path: data/habitats/food/food_preserved.yaml
    sha256: 59b82072dbcf982bdf3c56b832b54a4f4cd870ba0f7b337698632c9434eecd45
    role: context
  - path: data/habitats/food/food_product.yaml
    sha256: 244ae56ce8ff1aa6d066888dd63679f55a604b803758908955c1f3a90d1389de
    role: context
  - path: data/habitats/food/food_production.yaml
    sha256: b0fce7af2cc321a0979ce4d3bfec5e2d4383410ae8e62172b006073afb783ab7
    role: context
  - path: data/habitats/food/food_sample.yaml
    sha256: 33e35e85e3faa88f2e499f6cec84293e04c0946d50eaca180baa930e37fb4ac2
    role: context
  - path: data/habitats/food/food_spoiled.yaml
    sha256: bd94c0154eef2116da13a5a39e74af4f14f5b17ae5a4f68f9fa6d69aa19756f1
    role: target
  - path: data/habitats/food/frozen_seafood.yaml
    sha256: 93677d5139e32554b0263678305c5cf15151268a9374ed5e0332a15241420e8c
    role: context
  - path: data/habitats/food/seafood_product.yaml
    sha256: 92fe9e0cd56a12671fb144cacdc1a0f1475a0eb8dfb9e3a2a0c1594f95538c84
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
  - path: reports/yaml_record_review/20260926T153031Z-food_sample.md
    sha256: 7104d8fc86e95fdd7f54be1ff2b6d8cb43b15d11e3f2e87855797e066bde49b4
    role: context
  - path: reports/yaml_record_review/20260929T023519Z-food_product.md
    sha256: e58254f6987489cd482d9d4a390c1ba8c50c5b2983bef74e506911f505df2d96
    role: context
  - path: reports/yaml_record_review/20260929T030651Z-food_production.md
    sha256: 8e8b30e0bfe4849c96aec02bec10e0ef0970da582375e62f1068e9446a1cae4a
    role: context
  - path: research/habitats/food/food-fermented-habitatmech-bacdive-2b1959f1f0-deep-research-claude_code.md
    sha256: 83872dd2ca3dda125ef5cb8b8820b050e29e95bbd3d20bc3d96511c21381a4df
    role: context
  - path: scripts/aggregate_gold_triads.py
    sha256: 0e25179dbecd7c73cbedd99a0ae44e56e4992afb9e1ec02d2411439f643b8e54
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
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
- target_id: FOODON:00003366
  path: data/habitats/food/food_spoiled.yaml
  label: food (spoiled)
  kind: generated
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or transform; never hand-edit generated record
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or transform; never hand-edit generated record
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or transform; never hand-edit generated record
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or transform; never hand-edit generated record
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Maintained input or transform; never hand-edit generated record
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Maintained input or transform; never hand-edit generated record
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_source_taxa.tsv
    role: Maintained input or transform; never hand-edit generated record
  - repository: CultureBotAI/HabitatMech
    path: data/raw/madin_habitat_taxa.tsv
    role: Maintained input or transform; never hand-edit generated record
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Maintained input or transform; never hand-edit generated record
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or transform; never hand-edit generated record
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or transform; never hand-edit generated record
scope:
  description: Entire resolved record and all contributing source concepts; one individual
    scientific observation.
  selection: Next eight unreviewed Food records after ignored-inclusive census:991/3208
    current records,23/60 Food. This bundle declares one target, not a corpus pass.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - FOODON:00003366
evidence:
- evidence_id: RECORD
  kind: record_content
  reference: data/habitats/food/food_spoiled.yaml
  summary: Entire target YAML and history read; all present claims assessed.
  accessed_at: '2026-10-14T12:38:17.887142Z'
  support: supports
- evidence_id: SOURCE_ROWS
  kind: record_content
  reference: data/raw/; curation/decisions.tsv
  summary: 'BacDive isolation row 149 has three STRAIN assertions and three taxa.
    Mapping row 290 closeMatch is endorsed by ITEM REVIEW decision 1720; CLOSE/REVIEWED
    is mechanically correct. All three taxon entries have count one, ranks 1-3 and
    pool three, matching raw inputs and current NCBI labels. Current strain examples
    are not a reconstruction of the unavailable frozen strain join. No characteristic
    flags, numerical habitat parameters or causal claims are asserted. Search-row
    ledger (includes neighboring comparison rows): {"curation/decisions.tsv": [1720],
    "data/raw/bacdive_isolation_sources.tsv": [149], "data/raw/bacdive_source_taxa.tsv":
    [2608, 2609, 2610], "data/raw/isolation_source_groundings.tsv": [290], "data/raw/ontology_subclass_edges.tsv":
    [8864, 8881, 8942, 8971, 9048], "data/raw/ontology_terms.tsv": [10573, 10585]}'
  accessed_at: '2026-10-14T12:38:17.887224Z'
  support: supports
- evidence_id: RULES
  kind: authority
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md
  summary: Applied habitat-versus-process identity, strict genus, exact source units,
    MIxS roles, optional-field and all-source ITEM rules.
  accessed_at: '2026-10-14T12:38:17.887235Z'
  support: supports
- evidence_id: TRANSFORMS
  kind: record_content
  reference: src/habitatmech/seed.py; src/habitatmech/extract.py; src/habitatmech/curate/record_annotation_corrections.py
  summary: Immediate GOLD hierarchy and ontology subclass contributions are distinct.
    Source inventory labels and rank/count fields are copied. Imported ontology synonyms
    are flattened to exact; guarded annotation corrections allow local scope repairs.
    Parameters require exactly one term ID. Reproducibility is not biological evidence.
  accessed_at: '2026-10-14T12:38:17.887240Z'
  support: supports
- evidence_id: FOODON
  kind: database
  reference: https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl
  summary: Pinned full RDF/XML inspected for definitions, named parents, restrictions
    and synonym predicates. FOODON:00003366 denotes food made unsuitable for ingestion
    by spoilage; FOODON:00002454 is its supported food-material parent. BacDive Spoiled
    is retained as a related synonym and CLOSE mapping. Independently inspected rotten
    tofu residue, spoiled canned food and rotting onion examples positively support
    the displayed taxa as plausible spoiled-food associates, not universal causes
    of spoilage. Download SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf.
  accessed_at: '2026-10-14T12:27:42.074174Z'
  support: supports
- evidence_id: ENVO
  kind: database
  reference: https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl
  summary: 'Pinned full ENVO inspected: obsolete ENVO:00002002 has replacement FOODON:00001002.
    Fermentation starter, manufactured product and alcohol fermentation pit are distinct
    material/context concepts; triad roles must not be collapsed. Download SHA256
    a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c.'
  accessed_at: '2026-10-14T12:27:44.541645Z'
  support: supports
- evidence_id: SEARCH
  kind: search
  reference: curation/; history/; research/; reviews/structured/; data/raw/; reports/yaml_record_review/;
    tests/
  summary: 'Ignored-inclusive searches for exact IDs, mints, slugs and paths; all
    matching raw/decision TSV rows parsed. Census: 1416 bundles; no prior declarations
    of these eight exact targets or collisions for seven proposed issue keys. Search
    command: rg --no-ignore --hidden -l -i -F -e FOODON:00002454 -e FOODON:00003366
    -e Spoiled -e bacdive.isolation_source:spoiled -e food (spoiled) -e food_spoiled
    -e habitatmech:BACDIVE.9f2d319999 curation history research conf reviews/structured
    reports/yaml_record_review data/raw tests'
  accessed_at: '2026-10-14T12:38:17.887263Z'
  support: supports
  search_scope: Ignored/hidden-inclusive rg and structured TSV/review parsing of the
    named repository roots; original source search limited to repository and configured
    kg-microbe data root, not all disks.
- evidence_id: AVAILABILITY
  kind: search
  reference: conf/sources.yaml
  summary: Ignored-inclusive enumeration covered 41379 files in repository and configured
    kg-microbe data root. Original GOLD/BacDive/PREGO/MADIN member dumps were not
    located within these roots. Frozen aggregates are available; no global absence
    claim.
  accessed_at: '2026-10-14T12:38:17.887272Z'
  support: supports
  search_scope: Ignored/hidden-inclusive rg and structured TSV/review parsing of the
    named repository roots; original source search limited to repository and configured
    kg-microbe data root, not all disks.
- evidence_id: GOLD_ACCESS
  kind: database
  reference: https://gold.jgi.doe.gov/
  summary: 'All 24 requested exact own-path study URLs returned HTTP 403. No original
    members or page contents inferred. {"Gs0053258": {"accessed_at": "2026-10-14T12:24:46.231486Z",
    "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0053258"},
    "Gs0111475": {"accessed_at": "2026-10-14T12:24:46.356130Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0111475"}, "Gs0114546":
    {"accessed_at": "2026-10-14T12:24:46.386520Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0114546"}, "Gs0114789": {"accessed_at":
    "2026-10-14T12:24:46.418493Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0114789"},
    "Gs0118570": {"accessed_at": "2026-10-14T12:24:46.467904Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0118570"}, "Gs0132984":
    {"accessed_at": "2026-10-14T12:24:46.503783Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0132984"}, "Gs0133014": {"accessed_at":
    "2026-10-14T12:24:46.542534Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0133014"},
    "Gs0133290": {"accessed_at": "2026-10-14T12:24:46.572104Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0133290"}, "Gs0133298":
    {"accessed_at": "2026-10-14T12:24:46.613460Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0133298"}, "Gs0134604": {"accessed_at":
    "2026-10-14T12:24:46.727244Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0134604"},
    "Gs0135060": {"accessed_at": "2026-10-14T12:24:46.849688Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0135060"}, "Gs0141928":
    {"accessed_at": "2026-10-14T12:24:46.883936Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0141928"}, "Gs0142247": {"accessed_at":
    "2026-10-14T12:24:46.926691Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0142247"},
    "Gs0142315": {"accessed_at": "2026-10-14T12:24:46.971280Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0142315"}, "Gs0150392":
    {"accessed_at": "2026-10-14T12:24:47.022306Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0150392"}, "Gs0150427": {"accessed_at":
    "2026-10-14T12:24:47.054567Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150427"},
    "Gs0150438": {"accessed_at": "2026-10-14T12:24:47.084254Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150438"}, "Gs0150695":
    {"accessed_at": "2026-10-14T12:24:47.127172Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0150695"}, "Gs0150720": {"accessed_at":
    "2026-10-14T12:24:47.170716Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150720"},
    "Gs0153815": {"accessed_at": "2026-10-14T12:24:47.207422Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153815"}, "Gs0153827":
    {"accessed_at": "2026-10-14T12:24:47.249405Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0153827"}, "Gs0153978": {"accessed_at":
    "2026-10-14T12:24:47.381357Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153978"},
    "Gs0154236": {"accessed_at": "2026-10-14T12:24:47.424245Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154236"}, "Gs0154282":
    {"accessed_at": "2026-10-14T12:24:47.454274Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"}}'
  accessed_at: '2026-10-14T12:38:17.887528Z'
  support: supports
- evidence_id: BASE_QC
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38561093379
  summary: 'Exact base 07f8ab6c05a1c96de39e2475f306a271ee17243c completed successfully:
    1111 passed, three skipped; four contract tests passed; all authoritative gates
    passed. New bundles still require archive validation.'
  accessed_at: '2026-10-14T12:38:17.887541Z'
  support: supports
- evidence_id: TAXONOMY
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&retmode=xml&id=1004261,1007676,104097,104099,104101,1045004,1045854,104955,1050107,1051653,1051659,1054041,1074467,1076596,1089442,1091038,1110509,1114972,1121126,1121295,1121312,1121314,1121384,1121941,1122129,1122147,1122148,1122149,1122150,1122151,1122211,1122219,1122618,1123359,1123500,1123687,113557,114090,115541,1167631,120045,1202668,1206774,1220595,1247,1255632,1281,1307912,1405,1408434,1423830,1580,1588,1590,1591,1614,1629,174587,176292,1896336,214326,2338647,261164,2748,28038,282669,291615,292,36987,42895,438,442,457427,47714,51663,53444,545534,549,577,600645,615,61646,647,651,795797,865,86956
  summary: 'All 87 unique IDs across 88 displayed entries resolve in current NCBI.
    Historical genus names do not imply different taxa. Food-product 1121384/1408434
    merge to the same current strain; 36987 is a termite. All preserved/spoiled labels
    agree. Full raw-field audit for this target: {"all_displayed_fields_match_raw":
    true, "by_source": {"BACDIVE": 3}, "displayed": 3, "source_rows": {"BACDIVE":
    3}, "taxa": [{"corroborated_by": [], "count": 1, "identifier": "NCBITaxon:2338647",
    "label": "Ottowia konkukae", "pool": 3, "rank": 1, "score": null, "source": "BACDIVE"},
    {"corroborated_by": [], "count": 1, "identifier": "NCBITaxon:291615", "label":
    "Thermoanaerobacter mathranii subsp. alimentarius", "pool": 3, "rank": 2, "score":
    null, "source": "BACDIVE"}, {"corroborated_by": [], "count": 1, "identifier":
    "NCBITaxon:292", "label": "Burkholderia cepacia", "pool": 3, "rank": 3, "score":
    null, "source": "BACDIVE"}]} Download SHA256 1d7925cd89404cfa893114d28979276fe1b7291cf4f91ea6b7f69f433ab3c04e.'
  accessed_at: '2026-10-14T12:24:15.991594Z'
  support: supports
- evidence_id: BIJI
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/30222093/
  summary: PMID 30222093; DOI 10.1099/ijsem.0.003009. Abstract identifies Ottowia
    konkukae SK3863/DSM105395 isolated from rotten tofu residue. Download SHA256 94818fe6d34848e371784cc161e61d47aa4a50bb81a2235d204e226699d22aa9.
  accessed_at: '2026-10-14T12:27:45.266611Z'
  support: supports
- evidence_id: CIP
  kind: database
  reference: https://catalogue-crbip.pasteur.fr/fiche_catalogue.xhtml?crbip=CIP+108280
  summary: CIP 108280 type strain AIP505-99, Thermoanaerobacter mathranii subsp. alimentarius,
    has explicit spoiled canned food isolation annotation. Download SHA256 d84da7dabf117290439f2a94e0fb4c1ef8a18c0d6b470ad94e149e54bedf7073.
  accessed_at: '2026-10-14T12:27:55.616880Z'
  support: supports
- evidence_id: ONION
  kind: database
  reference: https://bacdive.dsmz.de/strain/157311
  summary: BacDive 157311 identifies Burkholderia cepacia IMI347462/taxid292 from
    rotting onion, with Spoiled source classification. Supports a spoiled food example,
    not unique habitat preference. Download SHA256 32e2b7946a7224afd98a40d1149de383a735583ca11e15eacd33dd04bf260466.
  accessed_at: '2026-10-14T12:27:54.402875Z'
  support: supports
checks:
- check_id: C6
  name: Native validate
  status: passed
  required: true
  target_ids:
  - FOODON:00003366
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/food/food_spoiled.yaml
  exit_code: 0
  summary: Executed 2026-10-14T12:23:55.373793Z to 2026-10-14T12:23:57.385182Z. No
    issues found
  scope_note: Target schema, eight-target strict, otherwise full-corpus native scope.
    Label gate:1176 canonical, one synonym, five exceptions,2059 unsupported-prefix
    skips; not scientific proof.
- check_id: C8
  name: Native validate-strict
  status: passed
  required: true
  target_ids:
  - FOODON:00003366
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/food/fish_products.yaml data/habitats/food/food_fermented.yaml data/habitats/food/food_preserved.yaml
    data/habitats/food/food_product.yaml data/habitats/food/food_production.yaml data/habitats/food/food_sample.yaml
    data/habitats/food/food_spoiled.yaml data/habitats/food/frozen_seafood.yaml
  exit_code: 0
  summary: "Executed 2026-10-14T12:23:59.573723Z to 2026-10-14T12:24:05.058517Z. uv\
    \ run python scripts/validate_strict.py data/habitats/food/fish_products.yaml\
    \ data/habitats/food/food_fermented.yaml data/habitats/food/food_preserved.yaml\
    \ data/habitats/food/food_product.yaml data/habitats/food/food_production.yaml\
    \ data/habitats/food/food_sample.yaml data/habitats/food/food_spoiled.yaml data/habitats/food/frozen_seafood.yaml\n\
    Validating 8 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      8\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Target schema, eight-target strict, otherwise full-corpus native scope.
    Label gate:1176 canonical, one synonym, five exceptions,2059 unsupported-prefix
    skips; not scientific proof.
- check_id: C9
  name: Native validate-history
  status: passed
  required: true
  target_ids:
  - FOODON:00003366
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  summary: 'Executed 2026-10-14T12:24:05.059204Z to 2026-10-14T12:24:11.861728Z. No
    issues found

    666 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Target schema, eight-target strict, otherwise full-corpus native scope.
    Label gate:1176 canonical, one synonym, five exceptions,2059 unsupported-prefix
    skips; not scientific proof.
- check_id: C10
  name: Native provenance-check
  status: passed
  required: true
  target_ids:
  - FOODON:00003366
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  summary: 'Executed 2026-10-14T12:24:11.862316Z to 2026-10-14T12:24:12.425647Z. provenance
    current: 14 committed inventories, 2 GOLD sources'
  scope_note: Target schema, eight-target strict, otherwise full-corpus native scope.
    Label gate:1176 canonical, one synonym, five exceptions,2059 unsupported-prefix
    skips; not scientific proof.
- check_id: C11
  name: Native verify-corpus
  status: passed
  required: true
  target_ids:
  - FOODON:00003366
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  summary: "Executed 2026-10-14T12:24:12.426275Z to 2026-10-14T12:24:26.823825Z. expected\
    \ 3208 records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing:\
    \ 0\n\ncorpus reproduces exactly from data/raw/"
  scope_note: Target schema, eight-target strict, otherwise full-corpus native scope.
    Label gate:1176 canonical, one synonym, five exceptions,2059 unsupported-prefix
    skips; not scientific proof.
- check_id: C12
  name: Native validate-causal-all
  status: passed
  required: true
  target_ids:
  - FOODON:00003366
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  summary: Executed 2026-10-14T12:24:26.824468Z to 2026-10-14T12:24:30.461288Z. validated
    32 causal-graph curation file(s) with 32 graph(s)
  scope_note: Target schema, eight-target strict, otherwise full-corpus native scope.
    Label gate:1176 canonical, one synonym, five exceptions,2059 unsupported-prefix
    skips; not scientific proof.
- check_id: C13
  name: Native term-requests-check
  status: passed
  required: true
  target_ids:
  - FOODON:00003366
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  summary: Executed 2026-10-14T12:24:30.461871Z to 2026-10-14T12:24:44.827612Z. term-request
    table is current (109 terms)
  scope_note: Target schema, eight-target strict, otherwise full-corpus native scope.
    Label gate:1176 canonical, one synonym, five exceptions,2059 unsupported-prefix
    skips; not scientific proof.
- check_id: C14
  name: Native validate-products
  status: passed
  required: true
  target_ids:
  - FOODON:00003366
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  summary: "Executed 2026-10-14T12:24:44.828194Z to 2026-10-14T12:25:27.849380Z. id↔label\
    \ correspondence summary:\n          OK_CANONICAL: 1176\n            OK_SYNONYM:\
    \ 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2059\n\n✅ All id↔label\
    \ pairs correspond."
  scope_note: Target schema, eight-target strict, otherwise full-corpus native scope.
    Label gate:1176 canonical, one synonym, five exceptions,2059 unsupported-prefix
    skips; not scientific proof.
- check_id: QC
  name: Exact-base authoritative hosted QC
  status: passed
  required: true
  target_ids:
  - FOODON:00003366
  command: gh run view 38561093379 --repo CultureBotAI/HabitatMech --json status,conclusion,headSha,url
  exit_code: 0
  summary: Exact unchanged scientific-input base passed; new report archive must still
    be checked.
  evidence_ids:
  - BASE_QC
- check_id: MEMBERS
  name: Original membership reconstruction
  status: unavailable
  required: false
  summary: Original source members not located in bounded ignored-inclusive search;
    24 GOLD pages HTTP403.
  evidence_ids:
  - AVAILABILITY
  - GOLD_ACCESS
  target_ids:
  - FOODON:00003366
- check_id: IMODULON
  name: Expression-module applicability
  status: not_applicable
  required: false
  summary: No gene/regulator/protein/expression mechanism is asserted. Habitat occurrences
    are not expression evidence.
  target_ids:
  - FOODON:00003366
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Habitat identity and strict hierarchy
  outcome: supported
  target_ids:
  - FOODON:00003366
  evidence_ids:
  - RECORD
  - SOURCE_ROWS
  - RULES
  - TRANSFORMS
  - FOODON
  - ENVO
  - SEARCH
  - AVAILABILITY
  - GOLD_ACCESS
  - BASE_QC
  - TAXONOMY
  - BIJI
  - CIP
  - ONION
  summary: FOODON:00003366 denotes food made unsuitable for ingestion by spoilage;
    FOODON:00002454 is its supported food-material parent. BacDive Spoiled is retained
    as a related synonym and CLOSE mapping. Independently inspected rotten tofu residue,
    spoiled canned food and rotting onion examples positively support the displayed
    taxa as plausible spoiled-food associates, not universal causes of spoilage.
- assessment_id: SOURCE
  area: evidence
  topic: Field-by-field source interpretation and original units
  outcome: supported
  target_ids:
  - FOODON:00003366
  evidence_ids:
  - RECORD
  - SOURCE_ROWS
  - RULES
  - TRANSFORMS
  - FOODON
  - ENVO
  - SEARCH
  - AVAILABILITY
  - GOLD_ACCESS
  - BASE_QC
  - TAXONOMY
  - BIJI
  - CIP
  - ONION
  summary: BacDive isolation row 149 has three STRAIN assertions and three taxa. Mapping
    row 290 closeMatch is endorsed by ITEM REVIEW decision 1720; CLOSE/REVIEWED is
    mechanically correct. All three taxon entries have count one, ranks 1-3 and pool
    three, matching raw inputs and current NCBI labels. Current strain examples are
    not a reconstruction of the unavailable frozen strain join. No characteristic
    flags, numerical habitat parameters or causal claims are asserted.
- assessment_id: STATUS
  area: provenance
  topic: Native gates and omitted optional claims
  outcome: supported
  target_ids:
  - FOODON:00003366
  evidence_ids:
  - RECORD
  - RULES
  - SOURCE_ROWS
  - TRANSFORMS
  summary: Current CLOSE/REVIEWED follows source decisions. All source taxon fields
    reproduce their frozen rows, without is_characteristic assertions. No unsupported
    parameter, causal, evidence or discussion fields are invented; optional absence
    alone is not a defect.
- assessment_id: LIMITS
  area: completeness
  topic: Missing original membership and broader certification
  outcome: unknown
  target_ids:
  - FOODON:00003366
  evidence_ids:
  - AVAILABILITY
  - GOLD_ACCESS
  summary: Original joins and GOLD page contents are unavailable. Positive current
    strain examples do not reconstruct frozen membership. Qualified passes apply to
    present target claims, not all ancestors, complete curation or whole-corpus science.
findings: []
actions: []
limitations:
- Same-agent assessment, not independent approval.
- Original members unavailable; occurrence edges, strain joins, taxa, biosamples and
  study unions have different denominators and are not summed.
- Pinned full ontology and current taxonomy checks are evidence, not an automatic
  ontology/taxonomy refresh.
- This observation captures pre-fix inputs; no scientific inputs changed while reviewing.
  Publication and fixes are separately authorized.
- No SSSOM/KGX certification, native status promotion or historical finding closure
  follows from validation.
- Exact-base QC predates these new reports; post-save archive validation remains required.
notes:
- Additional inputs assessed 2026-10-14T12:30:22.497207Z; all original input hashes
  rechecked unchanged.
tags:
- habitatmech
- record-review
- food
```
