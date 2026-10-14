# Scientific record review: Fruit-Seed

- Review: 20261014T135448Z-fruit_seed
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T13:43:23.101510Z
- Finished UTC: 2026-10-14T13:54:48.313134Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The native Fruit-Seed identity appropriately avoids equating the whole source bin with a seed-only anatomical term. Its plant-food-product genus and pinned FOOD bucket overstate the evidence: source anatomy and environmental plant material need not be a prepared food product.

## Scope And Provenance

Entire resolved record and every contributing source concept; one individual scientific review.

Selection: Next unreviewed Food records by path after an ignored-inclusive census of 999/3208 current records reviewed, Food31/60. This bundle covers one exact target, not a cohort sample or corpus certification.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 72a79e3782e2657aab8507b45ec9b49ac95bcf13.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:BACDIVE.ba016fe448 | data/habitats/food/fruit_seed.yaml | generated | Fruit-Seed |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | habitatmech:BACDIVE.ba016fe448 | Executed 2026-10-14T13:43:36.380539Z to 2026-10-14T13:43:38.847083Z. No issues found |
| Native validate-strict | passed | True | habitatmech:BACDIVE.ba016fe448 | Executed 2026-10-14T13:43:50.998179Z to 2026-10-14T13:43:55.575800Z. uv run python scripts/validate_strict.py data/habitats/food/frozen_shrimp.yaml data/habitats/food/fruit_seed.yaml data/habitats/food/heroin.yaml data/habitats/food/ice_cream.yaml data/habitats/food/juice.yaml data/habitats/food/mammalian_meat_food_product.yaml data/habitats/food/meat_trimming.yaml data/habitats/food/morphine.yaml<br>Validating 8 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      8<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| Native validate-history | passed | True | habitatmech:BACDIVE.ba016fe448 | Executed 2026-10-14T13:43:55.576413Z to 2026-10-14T13:44:01.983391Z. No issues found<br>670 history record(s) valid against src/habitatmech/schema/history.yaml |
| Native provenance-check | passed | True | habitatmech:BACDIVE.ba016fe448 | Executed 2026-10-14T13:44:01.984106Z to 2026-10-14T13:44:02.463384Z. provenance current: 14 committed inventories, 2 GOLD sources |
| Native verify-corpus | passed | True | habitatmech:BACDIVE.ba016fe448 | Executed 2026-10-14T13:44:02.463929Z to 2026-10-14T13:44:15.660795Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| Native validate-causal-all | passed | True | habitatmech:BACDIVE.ba016fe448 | Executed 2026-10-14T13:44:15.661664Z to 2026-10-14T13:44:19.221370Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| Native term-requests-check | passed | True | habitatmech:BACDIVE.ba016fe448 | Executed 2026-10-14T13:44:19.222000Z to 2026-10-14T13:44:33.161959Z. term-request table is current (109 terms) |
| Native validate-products | passed | True | habitatmech:BACDIVE.ba016fe448 | Executed 2026-10-14T13:44:33.162696Z to 2026-10-14T13:45:13.853367Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1176<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2059<br><br>✅ All id↔label pairs correspond. |
| Exact-base authoritative QC | passed | True | habitatmech:BACDIVE.ba016fe448 | Hosted QC on the exact unchanged scientific-input commit passed. New review archive validation is separate. |
| Original source-member reconstruction | unavailable | False | habitatmech:BACDIVE.ba016fe448 | Bounded ignored-inclusive search did not locate original joins. Nine exact GOLD study page requests across this review set returned HTTP403. |
| Expression-module applicability | not_applicable | False | habitatmech:BACDIVE.ba016fe448 | No gene, regulator, protein or transcriptomic mechanism is asserted. Occurrence records are not expression-module claims. |

## Scientific And Domain Assessments

### Habitat/source identity and exact scope

identity: concern. Targets: habitatmech:BACDIVE.ba016fe448.

The native Fruit-Seed identity appropriately avoids equating the whole source bin with a seed-only anatomical term. Its plant-food-product genus and pinned FOOD bucket overstate the evidence: source anatomy and environmental plant material need not be a prepared food product.

### Ontology genus versus source context

grounding: concern. Targets: habitatmech:BACDIVE.ba016fe448.

FOODON:00001015 requires a plant-derived food product. BacDive 21361 places taxid56/So ce1139 in Host Body-Site &gt; Plant &gt; Fruit (Seed), with humus and fruit-peel isolation rather than a demonstrated consumable product. This current example challenges the all-food rationale but does not reconstruct the frozen ten-member taxon join or all 228 source edges.

### Source assertions, units and native gates

provenance: supported. Targets: habitatmech:BACDIVE.ba016fe448.

BacDive inventory row 52 contains 228 STRAIN-unit assertions and a 157-taxon pool. Taxon rows 1213-1237 reproduce all 25 displayed IDs, labels, distinct-strain counts and ranks. The aggregate strain_count is computed from outgoing source edges; without original edges this review does not certify 228 distinct specimens. Mapping row 124 originally used FOODON:03420295; ITEM GROUND_AS_PARENT decision row 1751 overrides it with FOODON:00001015 and pins FOOD. All 25 taxon labels agree with current NCBI.

### Parameters, taxa, causal evidence and discussion

completeness: supported. Targets: habitatmech:BACDIVE.ba016fe448.

No environmental parameter, causal graph, cited mechanism, dataset or discussion claim is present to validate. Optional absence is not itself a defect. Displayed taxa, where present, remain source associations without characteristic flags; counts/ranks are not prevalence or mechanism evidence.

### Independent membership and unavailable source context

evidence: unknown. Targets: habitatmech:BACDIVE.ba016fe448.

The review assesses every present record claim, but original member-level provenance is unavailable in the bounded roots. Current source examples do not prove original membership, and missing rows or zero counts do not prove environmental absence.

## Findings

### F1: Plant anatomy is not necessarily a plant food product

major / open / confirmed; issue key: fruit-seed-food-product-parent.

The ITEM rationale says fruit and seed are foods regardless of the source meaning. FOODON:00001015 is a food-product genus, while current BacDive body-site and isolation evidence includes non-consumable environmental context. Native identity retention is sound; the universal food parent and pinned category are not supported. Original member joins remain unavailable.

## Recommended Actions And Acceptance Checks

### A1

Reassess habitatmech:BACDIVE.ba016fe448 with the full source vocabulary and frozen member evidence. Remove the unsupported food genus/category assumption; retain native scope or a verified anatomical/material broader relation. Do not automatically restore the seed-only grounding or delete counts/taxa.

- Edit maintained decisions or exact guarded overlays only; preserve frozen raw inventories and never hand-edit generated records.
- Preserve source identifiers, source paths, count units, taxon metrics and honest native status unless separately evidence-backed.
- Dry seed, inspect target canary and full before/after corpus delta; run schema, strict, history, provenance, corpus, site, label and authoritative QC gates.
- Save a new immutable follow-up with this stable issue key and exact previous occurrence; do not rewrite this report.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| RECORD | data/habitats/food/fruit_seed.yaml | supports | Entire target YAML, all source attestations, optional claims and curation events read before judgment. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; src/habitatmech/schema/habitatmech.yaml | supports | Native exact identity, strict superclass, source-unit, MIxS-role, optional-field and all-source ITEM rules applied. FOOD is a coarse layout/reporting bucket for food and beverage matrices, not an identity axiom. |
| ROWS | data/raw/; curation/decisions.tsv | supports | BacDive inventory row 52 contains 228 STRAIN-unit assertions and a 157-taxon pool. Taxon rows 1213-1237 reproduce all 25 displayed IDs, labels, distinct-strain counts and ranks. The aggregate strain_count is computed from outgoing source edges; without original edges this review does not certify 228 distinct specimens. Mapping row 124 originally used FOODON:03420295; ITEM GROUND_AS_PARENT decision row 1751 overrides it with FOODON:00001015 and pins FOOD. All 25 taxon labels agree with current NCBI. Parsed row locators, including neighboring comparison rows: {"curation/decisions.tsv": [1751], "data/raw/bacdive_isolation_sources.tsv": [52], "data/raw/bacdive_source_taxa.tsv": [1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229, 1230, 1231, 1232, 1233, 1234, 1235, 1236, 1237], "data/raw/isolation_source_groundings.tsv": [124], "data/raw/ontology_subclass_edges.tsv": [8779, 8780, 8802, 8810, 8816, 8817, 9049], "data/raw/ontology_terms.tsv": [10514]} |
| TRANSFORMS | src/habitatmech/seed.py; src/habitatmech/extract.py | supports | Inspected source resolution, immediate GOLD parent contributions, synonym scoping, taxon ranks/units and singleton-term parameter gating. GROUND replaces the identifier even when status is NARROW; status does not undo a merge. Deterministic reproduction does not establish scientific correctness. |
| SEARCH | curation/; history/; research/; reviews/structured/; data/raw/; reports/yaml_record_review/; tests/ | supports | All matching source/decision rows inspected. No earlier structured declaration of these eight targets or collision for the nine issue keys among 1428 bundles. No target-specific causal overlay or authored definition was located within the named roots. Exact target ID, slug, source labels and mints were searched, including ignored files. Command: rg --no-ignore --hidden -l -i -F -e FOODON:00001015 -e Fruit-Seed -e bacdive.isolation_source:fruit-seed -e fruit_seed -e habitatmech:BACDIVE.ba016fe448 curation history research conf reviews/structured reports/yaml_record_review data/raw tests |
| MEMBERS | conf/sources.yaml; data/raw/MANIFEST.yaml; data/raw/GOLD_MANIFEST.yaml | supports | Original GOLD nodes/edges, BacDive and PREGO nodes/edges, goldData.xlsx and gold_biosample_triads.tsv were not located by named-file enumeration of 39439 files under /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data. Ignored/hidden files included; .git internals excluded and symlinks not traversed. Frozen inventories remain available. No global absence or exact frozen member reconstruction is claimed. |
| FOODON | https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl | supports | Full pinned RDF/XML class definitions, synonym predicates, named parents and restrictions re-inspected at 2026-10-14T13:45:26.271013Z. FOODON:00001015 requires a plant-derived food product. BacDive 21361 places taxid56/So ce1139 in Host Body-Site &gt; Plant &gt; Fruit (Seed), with humus and fruit-peel isolation rather than a demonstrated consumable product. This current example challenges the all-food rationale but does not reconstruct the frozen ten-member taxon join or all 228 source edges. Retrieved bytes SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf. |
| BACDIVE | https://bacdive.dsmz.de/strain/21361 | refutes | Strain 21361 is So ce1139/taxid56. Its isolation record describes environmental humus with fruit peels and soil, while its source category is a plant body site. This supports non-food-only scope, not membership of this precise strain in the frozen top-ten count. Cultivation recipes and auto-linked publications were not used as isolation evidence. Retrieved bytes SHA256 cdb89de73a936cac59db663da2978c8a8a6e286ed75c6993f88a15c19f0b29da. |
| TAXONOMY | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;retmode=xml&amp;id=1046596,106592,1247,1327988,1364,1428,1517,152682,153721,1580,1588,176292,184914,1931,2371,28447,298,317,33,339,442,51663,54,556,56,562,71864,83451,84032,935295 | supports | Every displayed ID resolves and its stored label equals current NCBI. Local exact raw-field comparison: {"displayed": 25, "observations": [{"metric": 10, "rank": 1, "raw_row": 1213, "taxon": "NCBITaxon:56"}, {"metric": 9, "rank": 2, "raw_row": 1214, "taxon": "NCBITaxon:184914"}, {"metric": 8, "rank": 3, "raw_row": 1215, "taxon": "NCBITaxon:153721"}, {"metric": 7, "rank": 4, "raw_row": 1216, "taxon": "NCBITaxon:54"}, {"metric": 6, "rank": 5, "raw_row": 1217, "taxon": "NCBITaxon:317"}, {"metric": 4, "rank": 6, "raw_row": 1218, "taxon": "NCBITaxon:442"}, {"metric": 4, "rank": 7, "raw_row": 1219, "taxon": "NCBITaxon:556"}, {"metric": 4, "rank": 8, "raw_row": 1220, "taxon": "NCBITaxon:71864"}, {"metric": 3, "rank": 9, "raw_row": 1221, "taxon": "NCBITaxon:1580"}, {"metric": 3, "rank": 10, "raw_row": 1222, "taxon": "NCBITaxon:176292"}, {"metric": 3, "rank": 11, "raw_row": 1223, "taxon": "NCBITaxon:28447"}, {"metric": 3, "rank": 12, "raw_row": 1224, "taxon": "NCBITaxon:51663"}, {"metric": 3, "rank": 13, "raw_row": 1225, "taxon": "NCBITaxon:83451"}, {"metric": 3, "rank": 14, "raw_row": 1226, "taxon": "NCBITaxon:84032"}, {"metric": 2, "rank": 15, "raw_row": 1227, "taxon": "NCBITaxon:106592"}, {"metric": 2, "rank": 16, "raw_row": 1228, "taxon": "NCBITaxon:1247"}, {"metric": 2, "rank": 17, "raw_row": 1229, "taxon": "NCBITaxon:1428"}, {"metric": 2, "rank": 18, "raw_row": 1230, "taxon": "NCBITaxon:1517"}, {"metric": 2, "rank": 19, "raw_row": 1231, "taxon": "NCBITaxon:152682"}, {"metric": 2, "rank": 20, "raw_row": 1232, "taxon": "NCBITaxon:1588"}, {"metric": 2, "rank": 21, "raw_row": 1233, "taxon": "NCBITaxon:1931"}, {"metric": 2, "rank": 22, "raw_row": 1234, "taxon": "NCBITaxon:2371"}, {"metric": 2, "rank": 23, "raw_row": 1235, "taxon": "NCBITaxon:298"}, {"metric": 2, "rank": 24, "raw_row": 1236, "taxon": "NCBITaxon:33"}, {"metric": 2, "rank": 25, "raw_row": 1237, "taxon": "NCBITaxon:339"}], "pool": 157}. NCBI verifies identity, not habitat specificity. No is_characteristic or corroborated_by assertion is present. Retrieved bytes SHA256 32bb186f9b3a0f4b1eaf0d57090eee36f4679eb3f9ad6a2840cea466f0ba316d. |
| BASE_QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38570802819 | supports | Exact scientific-input base 72a79e3782e2657aab8507b45ec9b49ac95bcf13: authoritative merge-queue QC passed, with 1112 tests passed and three skipped; four review contract tests passed. This predates the new review bundles and cannot substitute for their post-save validation. |

## Limits And Additional Notes

- Same-agent review; no independent approval or native status promotion.
- Original source joins were unavailable in bounded searches; exact source counts are preserved without claims of deduplicated biological prevalence.
- Pinned ontology and current NCBI/source pages support bounded interpretations, not an automatic release refresh or whole-population reassessment.
- No scientific input, generated record, history, page, GitHub issue or PR was changed. Actions are proposals only.
- Exact-base QC predates the new review bundles; immutable saver validation and post-save archive checks are separately required.
- No SSSOM/KGX readiness or whole-corpus scientific pass is claimed.
- Original captured input hashes rechecked unchanged before extended inspection at 2026-10-14T13:52:38.861660Z.
- All present identifiers and source references were traced to inspected inventory/ontology/taxonomy evidence; unresolvable live GOLD access is explicitly recorded.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T135448Z-fruit_seed
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: Fruit-Seed'
started_at: '2026-10-14T13:43:23.101510Z'
finished_at: '2026-10-14T13:54:48.313134Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent has participated in HabitatMech curation and publication;
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
scientific_review: true
verdict: needs_curation
summary: 'The native Fruit-Seed identity appropriately avoids equating the whole source
  bin with a seed-only anatomical term. Its plant-food-product genus and pinned FOOD
  bucket overstate the evidence: source anatomy and environmental plant material need
  not be a prepared food product.'
source:
  git_revision: 72a79e3782e2657aab8507b45ec9b49ac95bcf13
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
    sha256: 3c84f75cdc8fa1bc5544692938c2408ba36bae96272552ed9007090c60accff1
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
  - path: data/habitats/food/fruit_seed.yaml
    sha256: 7e11faa94dd731c2f0a1ca7f440dbef4e1b80014334d69f3b975a371d84d3f51
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
- target_id: habitatmech:BACDIVE.ba016fe448
  path: data/habitats/food/fruit_seed.yaml
  label: Fruit-Seed
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
    path: data/raw/bacdive_isolation_sources.tsv
    role: Maintained owner; generated habitat YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_source_taxa.tsv
    role: Maintained owner; generated habitat YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/isolation_source_groundings.tsv
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
  description: Entire resolved record and every contributing source concept; one individual
    scientific review.
  selection: Next unreviewed Food records by path after an ignored-inclusive census
    of 999/3208 current records reviewed, Food31/60. This bundle covers one exact
    target, not a cohort sample or corpus certification.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:BACDIVE.ba016fe448
checks:
- check_id: C1
  name: Native validate
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/food/fruit_seed.yaml
  exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.ba016fe448
  summary: Executed 2026-10-14T13:43:36.380539Z to 2026-10-14T13:43:38.847083Z. No
    issues found
  scope_note: Schema targets this record; strict covers these eight; history/provenance/corpus/causal/term/label
    checks use their documented full scope. Label gate intentionally skips 2059 unsupported-prefix
    pairs. Not scientific approval.
- check_id: C8
  name: Native validate-strict
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/food/frozen_shrimp.yaml data/habitats/food/fruit_seed.yaml data/habitats/food/heroin.yaml
    data/habitats/food/ice_cream.yaml data/habitats/food/juice.yaml data/habitats/food/mammalian_meat_food_product.yaml
    data/habitats/food/meat_trimming.yaml data/habitats/food/morphine.yaml
  exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.ba016fe448
  summary: "Executed 2026-10-14T13:43:50.998179Z to 2026-10-14T13:43:55.575800Z. uv\
    \ run python scripts/validate_strict.py data/habitats/food/frozen_shrimp.yaml\
    \ data/habitats/food/fruit_seed.yaml data/habitats/food/heroin.yaml data/habitats/food/ice_cream.yaml\
    \ data/habitats/food/juice.yaml data/habitats/food/mammalian_meat_food_product.yaml\
    \ data/habitats/food/meat_trimming.yaml data/habitats/food/morphine.yaml\nValidating\
    \ 8 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      8\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Schema targets this record; strict covers these eight; history/provenance/corpus/causal/term/label
    checks use their documented full scope. Label gate intentionally skips 2059 unsupported-prefix
    pairs. Not scientific approval.
- check_id: C9
  name: Native validate-history
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.ba016fe448
  summary: 'Executed 2026-10-14T13:43:55.576413Z to 2026-10-14T13:44:01.983391Z. No
    issues found

    670 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Schema targets this record; strict covers these eight; history/provenance/corpus/causal/term/label
    checks use their documented full scope. Label gate intentionally skips 2059 unsupported-prefix
    pairs. Not scientific approval.
- check_id: C10
  name: Native provenance-check
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.ba016fe448
  summary: 'Executed 2026-10-14T13:44:01.984106Z to 2026-10-14T13:44:02.463384Z. provenance
    current: 14 committed inventories, 2 GOLD sources'
  scope_note: Schema targets this record; strict covers these eight; history/provenance/corpus/causal/term/label
    checks use their documented full scope. Label gate intentionally skips 2059 unsupported-prefix
    pairs. Not scientific approval.
- check_id: C11
  name: Native verify-corpus
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.ba016fe448
  summary: "Executed 2026-10-14T13:44:02.463929Z to 2026-10-14T13:44:15.660795Z. expected\
    \ 3208 records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing:\
    \ 0\n\ncorpus reproduces exactly from data/raw/"
  scope_note: Schema targets this record; strict covers these eight; history/provenance/corpus/causal/term/label
    checks use their documented full scope. Label gate intentionally skips 2059 unsupported-prefix
    pairs. Not scientific approval.
- check_id: C12
  name: Native validate-causal-all
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.ba016fe448
  summary: Executed 2026-10-14T13:44:15.661664Z to 2026-10-14T13:44:19.221370Z. validated
    32 causal-graph curation file(s) with 32 graph(s)
  scope_note: Schema targets this record; strict covers these eight; history/provenance/corpus/causal/term/label
    checks use their documented full scope. Label gate intentionally skips 2059 unsupported-prefix
    pairs. Not scientific approval.
- check_id: C13
  name: Native term-requests-check
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.ba016fe448
  summary: Executed 2026-10-14T13:44:19.222000Z to 2026-10-14T13:44:33.161959Z. term-request
    table is current (109 terms)
  scope_note: Schema targets this record; strict covers these eight; history/provenance/corpus/causal/term/label
    checks use their documented full scope. Label gate intentionally skips 2059 unsupported-prefix
    pairs. Not scientific approval.
- check_id: C14
  name: Native validate-products
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.ba016fe448
  summary: "Executed 2026-10-14T13:44:33.162696Z to 2026-10-14T13:45:13.853367Z. id↔label\
    \ correspondence summary:\n          OK_CANONICAL: 1176\n            OK_SYNONYM:\
    \ 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2059\n\n✅ All id↔label\
    \ pairs correspond."
  scope_note: Schema targets this record; strict covers these eight; history/provenance/corpus/causal/term/label
    checks use their documented full scope. Label gate intentionally skips 2059 unsupported-prefix
    pairs. Not scientific approval.
- check_id: QC
  name: Exact-base authoritative QC
  required: true
  status: passed
  command: gh run view 38570802819 --repo CultureBotAI/HabitatMech --json headSha,status,conclusion,url
  exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.ba016fe448
  evidence_ids:
  - BASE_QC
  summary: Hosted QC on the exact unchanged scientific-input commit passed. New review
    archive validation is separate.
- check_id: ORIGINAL
  name: Original source-member reconstruction
  required: false
  status: unavailable
  target_ids:
  - habitatmech:BACDIVE.ba016fe448
  evidence_ids:
  - MEMBERS
  summary: Bounded ignored-inclusive search did not locate original joins. Nine exact
    GOLD study page requests across this review set returned HTTP403.
- check_id: IMODULON
  name: Expression-module applicability
  required: false
  status: not_applicable
  target_ids:
  - habitatmech:BACDIVE.ba016fe448
  summary: No gene, regulator, protein or transcriptomic mechanism is asserted. Occurrence
    records are not expression-module claims.
evidence:
- evidence_id: RECORD
  kind: record_content
  reference: data/habitats/food/fruit_seed.yaml
  summary: Entire target YAML, all source attestations, optional claims and curation
    events read before judgment.
  accessed_at: '2026-10-14T13:54:48.312529Z'
  support: supports
- evidence_id: RULES
  kind: authority
  reference: docs/CURATION.md; docs/HARMONIZATION.md; src/habitatmech/schema/habitatmech.yaml
  summary: Native exact identity, strict superclass, source-unit, MIxS-role, optional-field
    and all-source ITEM rules applied. FOOD is a coarse layout/reporting bucket for
    food and beverage matrices, not an identity axiom.
  accessed_at: '2026-10-14T13:54:48.312551Z'
  support: supports
- evidence_id: ROWS
  kind: record_content
  reference: data/raw/; curation/decisions.tsv
  summary: 'BacDive inventory row 52 contains 228 STRAIN-unit assertions and a 157-taxon
    pool. Taxon rows 1213-1237 reproduce all 25 displayed IDs, labels, distinct-strain
    counts and ranks. The aggregate strain_count is computed from outgoing source
    edges; without original edges this review does not certify 228 distinct specimens.
    Mapping row 124 originally used FOODON:03420295; ITEM GROUND_AS_PARENT decision
    row 1751 overrides it with FOODON:00001015 and pins FOOD. All 25 taxon labels
    agree with current NCBI. Parsed row locators, including neighboring comparison
    rows: {"curation/decisions.tsv": [1751], "data/raw/bacdive_isolation_sources.tsv":
    [52], "data/raw/bacdive_source_taxa.tsv": [1213, 1214, 1215, 1216, 1217, 1218,
    1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229, 1230, 1231,
    1232, 1233, 1234, 1235, 1236, 1237], "data/raw/isolation_source_groundings.tsv":
    [124], "data/raw/ontology_subclass_edges.tsv": [8779, 8780, 8802, 8810, 8816,
    8817, 9049], "data/raw/ontology_terms.tsv": [10514]}'
  accessed_at: '2026-10-14T13:54:48.312642Z'
  support: supports
- evidence_id: TRANSFORMS
  kind: record_content
  reference: src/habitatmech/seed.py; src/habitatmech/extract.py
  summary: Inspected source resolution, immediate GOLD parent contributions, synonym
    scoping, taxon ranks/units and singleton-term parameter gating. GROUND replaces
    the identifier even when status is NARROW; status does not undo a merge. Deterministic
    reproduction does not establish scientific correctness.
  accessed_at: '2026-10-14T13:54:48.312650Z'
  support: supports
- evidence_id: SEARCH
  kind: search
  reference: curation/; history/; research/; reviews/structured/; data/raw/; reports/yaml_record_review/;
    tests/
  summary: 'All matching source/decision rows inspected. No earlier structured declaration
    of these eight targets or collision for the nine issue keys among 1428 bundles.
    No target-specific causal overlay or authored definition was located within the
    named roots. Exact target ID, slug, source labels and mints were searched, including
    ignored files. Command: rg --no-ignore --hidden -l -i -F -e FOODON:00001015 -e
    Fruit-Seed -e bacdive.isolation_source:fruit-seed -e fruit_seed -e habitatmech:BACDIVE.ba016fe448
    curation history research conf reviews/structured reports/yaml_record_review data/raw
    tests'
  accessed_at: '2026-10-14T13:54:48.312658Z'
  support: supports
  search_scope: Ignored/hidden-inclusive structured parsing and rg within the explicitly
    named roots; not an all-disk absence claim.
- evidence_id: MEMBERS
  kind: search
  reference: conf/sources.yaml; data/raw/MANIFEST.yaml; data/raw/GOLD_MANIFEST.yaml
  summary: Original GOLD nodes/edges, BacDive and PREGO nodes/edges, goldData.xlsx
    and gold_biosample_triads.tsv were not located by named-file enumeration of 39439
    files under /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech;
    /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data. Ignored/hidden
    files included; .git internals excluded and symlinks not traversed. Frozen inventories
    remain available. No global absence or exact frozen member reconstruction is claimed.
  accessed_at: '2026-10-14T13:54:48.312673Z'
  support: supports
  search_scope: Ignored/hidden-inclusive structured parsing and rg within the explicitly
    named roots; not an all-disk absence claim.
- evidence_id: FOODON
  kind: database
  reference: https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl
  summary: Full pinned RDF/XML class definitions, synonym predicates, named parents
    and restrictions re-inspected at 2026-10-14T13:45:26.271013Z. FOODON:00001015
    requires a plant-derived food product. BacDive 21361 places taxid56/So ce1139
    in Host Body-Site > Plant > Fruit (Seed), with humus and fruit-peel isolation
    rather than a demonstrated consumable product. This current example challenges
    the all-food rationale but does not reconstruct the frozen ten-member taxon join
    or all 228 source edges. Retrieved bytes SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf.
  accessed_at: '2026-10-14T12:27:42.074174Z'
  support: supports
- evidence_id: BACDIVE
  kind: database
  reference: https://bacdive.dsmz.de/strain/21361
  summary: Strain 21361 is So ce1139/taxid56. Its isolation record describes environmental
    humus with fruit peels and soil, while its source category is a plant body site.
    This supports non-food-only scope, not membership of this precise strain in the
    frozen top-ten count. Cultivation recipes and auto-linked publications were not
    used as isolation evidence. Retrieved bytes SHA256 cdb89de73a936cac59db663da2978c8a8a6e286ed75c6993f88a15c19f0b29da.
  accessed_at: '2026-10-14T13:45:38.818075Z'
  support: refutes
- evidence_id: TAXONOMY
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&retmode=xml&id=1046596,106592,1247,1327988,1364,1428,1517,152682,153721,1580,1588,176292,184914,1931,2371,28447,298,317,33,339,442,51663,54,556,56,562,71864,83451,84032,935295
  summary: 'Every displayed ID resolves and its stored label equals current NCBI.
    Local exact raw-field comparison: {"displayed": 25, "observations": [{"metric":
    10, "rank": 1, "raw_row": 1213, "taxon": "NCBITaxon:56"}, {"metric": 9, "rank":
    2, "raw_row": 1214, "taxon": "NCBITaxon:184914"}, {"metric": 8, "rank": 3, "raw_row":
    1215, "taxon": "NCBITaxon:153721"}, {"metric": 7, "rank": 4, "raw_row": 1216,
    "taxon": "NCBITaxon:54"}, {"metric": 6, "rank": 5, "raw_row": 1217, "taxon": "NCBITaxon:317"},
    {"metric": 4, "rank": 6, "raw_row": 1218, "taxon": "NCBITaxon:442"}, {"metric":
    4, "rank": 7, "raw_row": 1219, "taxon": "NCBITaxon:556"}, {"metric": 4, "rank":
    8, "raw_row": 1220, "taxon": "NCBITaxon:71864"}, {"metric": 3, "rank": 9, "raw_row":
    1221, "taxon": "NCBITaxon:1580"}, {"metric": 3, "rank": 10, "raw_row": 1222, "taxon":
    "NCBITaxon:176292"}, {"metric": 3, "rank": 11, "raw_row": 1223, "taxon": "NCBITaxon:28447"},
    {"metric": 3, "rank": 12, "raw_row": 1224, "taxon": "NCBITaxon:51663"}, {"metric":
    3, "rank": 13, "raw_row": 1225, "taxon": "NCBITaxon:83451"}, {"metric": 3, "rank":
    14, "raw_row": 1226, "taxon": "NCBITaxon:84032"}, {"metric": 2, "rank": 15, "raw_row":
    1227, "taxon": "NCBITaxon:106592"}, {"metric": 2, "rank": 16, "raw_row": 1228,
    "taxon": "NCBITaxon:1247"}, {"metric": 2, "rank": 17, "raw_row": 1229, "taxon":
    "NCBITaxon:1428"}, {"metric": 2, "rank": 18, "raw_row": 1230, "taxon": "NCBITaxon:1517"},
    {"metric": 2, "rank": 19, "raw_row": 1231, "taxon": "NCBITaxon:152682"}, {"metric":
    2, "rank": 20, "raw_row": 1232, "taxon": "NCBITaxon:1588"}, {"metric": 2, "rank":
    21, "raw_row": 1233, "taxon": "NCBITaxon:1931"}, {"metric": 2, "rank": 22, "raw_row":
    1234, "taxon": "NCBITaxon:2371"}, {"metric": 2, "rank": 23, "raw_row": 1235, "taxon":
    "NCBITaxon:298"}, {"metric": 2, "rank": 24, "raw_row": 1236, "taxon": "NCBITaxon:33"},
    {"metric": 2, "rank": 25, "raw_row": 1237, "taxon": "NCBITaxon:339"}], "pool":
    157}. NCBI verifies identity, not habitat specificity. No is_characteristic or
    corroborated_by assertion is present. Retrieved bytes SHA256 32bb186f9b3a0f4b1eaf0d57090eee36f4679eb3f9ad6a2840cea466f0ba316d.'
  accessed_at: '2026-10-14T13:43:40.739429Z'
  support: supports
- evidence_id: BASE_QC
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38570802819
  summary: 'Exact scientific-input base 72a79e3782e2657aab8507b45ec9b49ac95bcf13:
    authoritative merge-queue QC passed, with 1112 tests passed and three skipped;
    four review contract tests passed. This predates the new review bundles and cannot
    substitute for their post-save validation.'
  accessed_at: '2026-10-14T13:48:45.905464Z'
  support: supports
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Habitat/source identity and exact scope
  outcome: concern
  target_ids:
  - habitatmech:BACDIVE.ba016fe448
  evidence_ids:
  - RECORD
  - RULES
  - ROWS
  - TRANSFORMS
  - SEARCH
  - MEMBERS
  - FOODON
  - BACDIVE
  - TAXONOMY
  - BASE_QC
  summary: 'The native Fruit-Seed identity appropriately avoids equating the whole
    source bin with a seed-only anatomical term. Its plant-food-product genus and
    pinned FOOD bucket overstate the evidence: source anatomy and environmental plant
    material need not be a prepared food product.'
- assessment_id: HIERARCHY
  area: grounding
  topic: Ontology genus versus source context
  outcome: concern
  target_ids:
  - habitatmech:BACDIVE.ba016fe448
  evidence_ids:
  - RECORD
  - RULES
  - ROWS
  - TRANSFORMS
  - SEARCH
  - MEMBERS
  - FOODON
  - BACDIVE
  - TAXONOMY
  - BASE_QC
  summary: FOODON:00001015 requires a plant-derived food product. BacDive 21361 places
    taxid56/So ce1139 in Host Body-Site > Plant > Fruit (Seed), with humus and fruit-peel
    isolation rather than a demonstrated consumable product. This current example
    challenges the all-food rationale but does not reconstruct the frozen ten-member
    taxon join or all 228 source edges.
- assessment_id: PROVENANCE
  area: provenance
  topic: Source assertions, units and native gates
  outcome: supported
  target_ids:
  - habitatmech:BACDIVE.ba016fe448
  evidence_ids:
  - RECORD
  - ROWS
  - TRANSFORMS
  summary: BacDive inventory row 52 contains 228 STRAIN-unit assertions and a 157-taxon
    pool. Taxon rows 1213-1237 reproduce all 25 displayed IDs, labels, distinct-strain
    counts and ranks. The aggregate strain_count is computed from outgoing source
    edges; without original edges this review does not certify 228 distinct specimens.
    Mapping row 124 originally used FOODON:03420295; ITEM GROUND_AS_PARENT decision
    row 1751 overrides it with FOODON:00001015 and pins FOOD. All 25 taxon labels
    agree with current NCBI.
- assessment_id: OPTIONAL
  area: completeness
  topic: Parameters, taxa, causal evidence and discussion
  outcome: supported
  target_ids:
  - habitatmech:BACDIVE.ba016fe448
  evidence_ids:
  - RECORD
  - ROWS
  - SEARCH
  - RULES
  summary: No environmental parameter, causal graph, cited mechanism, dataset or discussion
    claim is present to validate. Optional absence is not itself a defect. Displayed
    taxa, where present, remain source associations without characteristic flags;
    counts/ranks are not prevalence or mechanism evidence.
- assessment_id: LIMITS
  area: evidence
  topic: Independent membership and unavailable source context
  outcome: unknown
  target_ids:
  - habitatmech:BACDIVE.ba016fe448
  evidence_ids:
  - MEMBERS
  summary: The review assesses every present record claim, but original member-level
    provenance is unavailable in the bounded roots. Current source examples do not
    prove original membership, and missing rows or zero counts do not prove environmental
    absence.
findings:
- finding_id: F1
  issue_key: fruit-seed-food-product-parent
  title: Plant anatomy is not necessarily a plant food product
  description: The ITEM rationale says fruit and seed are foods regardless of the
    source meaning. FOODON:00001015 is a food-product genus, while current BacDive
    body-site and isolation evidence includes non-consumable environmental context.
    Native identity retention is sound; the universal food parent and pinned category
    are not supported. Original member joins remain unavailable.
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  target_ids:
  - habitatmech:BACDIVE.ba016fe448
  field_paths:
  - parent_habitats
  - habitat_category
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained owner; generated habitat YAML is read-only
  evidence_ids:
  - ROWS
  - FOODON
  - BACDIVE
  - RULES
  rule_id: Habitat identity, strict genus and source-specific scope
  native_severity: major
  normalization_reason: Unsupported identity equivalence or strict superclass materially
    changes the source meaning.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - habitatmech:BACDIVE.ba016fe448
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained owner; generated habitat YAML is read-only
  description: Reassess habitatmech:BACDIVE.ba016fe448 with the full source vocabulary
    and frozen member evidence. Remove the unsupported food genus/category assumption;
    retain native scope or a verified anatomical/material broader relation. Do not
    automatically restore the seed-only grounding or delete counts/taxa.
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
- Same-agent review; no independent approval or native status promotion.
- Original source joins were unavailable in bounded searches; exact source counts
  are preserved without claims of deduplicated biological prevalence.
- Pinned ontology and current NCBI/source pages support bounded interpretations, not
  an automatic release refresh or whole-population reassessment.
- No scientific input, generated record, history, page, GitHub issue or PR was changed.
  Actions are proposals only.
- Exact-base QC predates the new review bundles; immutable saver validation and post-save
  archive checks are separately required.
- No SSSOM/KGX readiness or whole-corpus scientific pass is claimed.
notes:
- Original captured input hashes rechecked unchanged before extended inspection at
  2026-10-14T13:52:38.861660Z.
- All present identifiers and source references were traced to inspected inventory/ontology/taxonomy
  evidence; unresolvable live GOLD access is explicitly recorded.
tags:
- habitatmech
- record-review
- food
```
