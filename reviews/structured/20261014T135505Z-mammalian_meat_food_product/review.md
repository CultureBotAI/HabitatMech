# Scientific record review: mammalian meat food product

- Review: 20261014T135505Z-mammalian_meat_food_product
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T13:43:30.833242Z
- Finished UTC: 2026-10-14T13:55:05.702699Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

FOODON:00001006 is explicitly mammalian. The only source is generic GOLD Meat products, whose ITEM decision itself says the chosen ontology term is narrower than the source. A NARROW annotation does not justify using that term as the source identity or making Meat products an exact synonym. The original member composition was not independently recovered.

## Scope And Provenance

Entire resolved record and every contributing source concept; one individual scientific review.

Selection: Next unreviewed Food records by path after an ignored-inclusive census of 999/3208 current records reviewed, Food31/60. This bundle covers one exact target, not a cohort sample or corpus certification.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 72a79e3782e2657aab8507b45ec9b49ac95bcf13.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| FOODON:00001006 | data/habitats/food/mammalian_meat_food_product.yaml | generated | mammalian meat food product |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | FOODON:00001006 | Executed 2026-10-14T13:43:45.116950Z to 2026-10-14T13:43:47.077049Z. No issues found |
| Native validate-strict | passed | True | FOODON:00001006 | Executed 2026-10-14T13:43:50.998179Z to 2026-10-14T13:43:55.575800Z. uv run python scripts/validate_strict.py data/habitats/food/frozen_shrimp.yaml data/habitats/food/fruit_seed.yaml data/habitats/food/heroin.yaml data/habitats/food/ice_cream.yaml data/habitats/food/juice.yaml data/habitats/food/mammalian_meat_food_product.yaml data/habitats/food/meat_trimming.yaml data/habitats/food/morphine.yaml<br>Validating 8 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      8<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| Native validate-history | passed | True | FOODON:00001006 | Executed 2026-10-14T13:43:55.576413Z to 2026-10-14T13:44:01.983391Z. No issues found<br>670 history record(s) valid against src/habitatmech/schema/history.yaml |
| Native provenance-check | passed | True | FOODON:00001006 | Executed 2026-10-14T13:44:01.984106Z to 2026-10-14T13:44:02.463384Z. provenance current: 14 committed inventories, 2 GOLD sources |
| Native verify-corpus | passed | True | FOODON:00001006 | Executed 2026-10-14T13:44:02.463929Z to 2026-10-14T13:44:15.660795Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| Native validate-causal-all | passed | True | FOODON:00001006 | Executed 2026-10-14T13:44:15.661664Z to 2026-10-14T13:44:19.221370Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| Native term-requests-check | passed | True | FOODON:00001006 | Executed 2026-10-14T13:44:19.222000Z to 2026-10-14T13:44:33.161959Z. term-request table is current (109 terms) |
| Native validate-products | passed | True | FOODON:00001006 | Executed 2026-10-14T13:44:33.162696Z to 2026-10-14T13:45:13.853367Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1176<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2059<br><br>✅ All id↔label pairs correspond. |
| Exact-base authoritative QC | passed | True | FOODON:00001006 | Hosted QC on the exact unchanged scientific-input commit passed. New review archive validation is separate. |
| Original source-member reconstruction | unavailable | False | FOODON:00001006 | Bounded ignored-inclusive search did not locate original joins. Nine exact GOLD study page requests across this review set returned HTTP403. |
| Expression-module applicability | not_applicable | False | FOODON:00001006 | No gene, regulator, protein or transcriptomic mechanism is asserted. Occurrence records are not expression-module claims. |

## Scientific And Domain Assessments

### Habitat/source identity and exact scope

identity: concern. Targets: FOODON:00001006.

FOODON:00001006 is explicitly mammalian. The only source is generic GOLD Meat products, whose ITEM decision itself says the chosen ontology term is narrower than the source. A NARROW annotation does not justify using that term as the source identity or making Meat products an exact synonym. The original member composition was not independently recovered.

### Ontology genus versus source context

grounding: concern. Targets: FOODON:00001006.

FOODON:00001092 and FOODON:00005501 are valid named ontology parents of mammalian meat. FOODON:03530206 is instead a process introduced by the GOLD branch. A source remap must audit the two remaining direct record children and two exact expected-parent exclusion guards; no original poultry/fish members are asserted by this review.

### Source assertions, units and native gates

provenance: supported. Targets: FOODON:00001006.

GOLD row 24 names nodes 4486/4487/4488 and 1916 ORGANISM assertions. Separate bulk row 79 contains 438 BIOSAMPLE observations and eight study rows include multipath unions. Triad rows 95-97 cover two samples/one study: legume food product as broad, fermented sausage as local, and dried fermented sausage as medium. These roles and small denominators cannot establish a mammal-only identity; the material-valued broad slot is not an ecosystem. ITEM GROUND decision row 118 explains NARROW/REVIEWED but records the scope conflict.

### Parameters, taxa, causal evidence and discussion

completeness: supported. Targets: FOODON:00001006.

No environmental parameter, causal graph, cited mechanism, dataset or discussion claim is present to validate. Optional absence is not itself a defect. Displayed taxa, where present, remain source associations without characteristic flags; counts/ranks are not prevalence or mechanism evidence.

### Independent membership and unavailable source context

evidence: unknown. Targets: FOODON:00001006.

The review assesses every present record claim, but original member-level provenance is unavailable in the bounded roots. Current source examples do not prove original membership, and missing rows or zero counts do not prove environmental absence.

## Findings

### F1: Acknowledged narrower term is adopted as the source identity

major / open / confirmed; issue key: mammalian-meat-gold-source-identity.

The maintained decision explicitly says mammalian meat is narrower than GOLD Meat products but still uses GROUND. The generator substitutes the mammalian identifier and emits Meat products as an exact synonym. Neither the NARROW annotation nor best-available-term rationale establishes coextensiveness. Original poultry/fish membership has not been independently verified; the confirmed defect is the unsupported identity and internal scope conflict.

### F2: Food production process is not a meat-material genus

major / open / confirmed; issue key: mammalian-meat-food-production-process-parent.

The added FOODON:03530206 parent is a planned process, unlike the two independently supported material ontology parents. It is a GOLD classification context contribution, not a strict material superclass.

## Recommended Actions And Acceptance Checks

### A1

Reassess mint habitatmech:GOLD.0347e0d978 and retain its native generic scope unless an actual exact identity is verified. A narrower mammalian class cannot be its broader parent. Audit Raw meat and butchery-cut children plus the two expected-parent exclusions for Cooked meat/Fermented meat products. Preserve all original counts and do not assume source-member species from a note.

- Edit maintained decisions or exact guarded overlays only; preserve frozen raw inventories and never hand-edit generated records.
- Preserve source identifiers, source paths, count units, taxon metrics and honest native status unless separately evidence-backed.
- Dry seed, inspect target canary and full before/after corpus delta; run schema, strict, history, provenance, corpus, site, label and authoritative QC gates.
- Save a new immutable follow-up with this stable issue key and exact previous occurrence; do not rewrite this report.

### A2

Exclude the exact GOLD Meat products path contribution with expected FOODON:03530206, preserving independent material parents on any retained ontology record. Coordinate the guarded row with the separate source-identity correction.

- Edit maintained decisions or exact guarded overlays only; preserve frozen raw inventories and never hand-edit generated records.
- Preserve source identifiers, source paths, count units, taxon metrics and honest native status unless separately evidence-backed.
- Dry seed, inspect target canary and full before/after corpus delta; run schema, strict, history, provenance, corpus, site, label and authoritative QC gates.
- Save a new immutable follow-up with this stable issue key and exact previous occurrence; do not rewrite this report.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| RECORD | data/habitats/food/mammalian_meat_food_product.yaml | supports | Entire target YAML, all source attestations, optional claims and curation events read before judgment. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; src/habitatmech/schema/habitatmech.yaml | supports | Native exact identity, strict superclass, source-unit, MIxS-role, optional-field and all-source ITEM rules applied. FOOD is a coarse layout/reporting bucket for food and beverage matrices, not an identity axiom. |
| ROWS | data/raw/; curation/decisions.tsv | supports | GOLD row 24 names nodes 4486/4487/4488 and 1916 ORGANISM assertions. Separate bulk row 79 contains 438 BIOSAMPLE observations and eight study rows include multipath unions. Triad rows 95-97 cover two samples/one study: legume food product as broad, fermented sausage as local, and dried fermented sausage as medium. These roles and small denominators cannot establish a mammal-only identity; the material-valued broad slot is not an ecosystem. ITEM GROUND decision row 118 explains NARROW/REVIEWED but records the scope conflict. Parsed row locators, including neighboring comparison rows: {"curation/decisions.tsv": [118], "curation/gold_parent_exclusions.tsv": [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19], "data/raw/gold_ecosystem_paths.tsv": [24, 129, 147, 557, 601, 781, 899, 1300], "data/raw/gold_path_biosamples.tsv": [79], "data/raw/gold_path_triads.tsv": [95, 96, 97], "data/raw/gold_studies.tsv": [646, 1410, 1794, 3174, 3339, 3522, 3931, 3966], "data/raw/ontology_subclass_edges.tsv": [8776, 8777, 8788, 8789, 8811, 8812, 8819, 8901, 8906, 8925, 8982, 8995], "data/raw/ontology_terms.tsv": [10512, 10518, 10602, 10732]} |
| TRANSFORMS | src/habitatmech/seed.py; src/habitatmech/extract.py | supports | Inspected source resolution, immediate GOLD parent contributions, synonym scoping, taxon ranks/units and singleton-term parameter gating. GROUND replaces the identifier even when status is NARROW; status does not undo a merge. Deterministic reproduction does not establish scientific correctness. |
| SEARCH | curation/; history/; research/; reviews/structured/; data/raw/; reports/yaml_record_review/; tests/ | supports | All matching source/decision rows inspected. No earlier structured declaration of these eight targets or collision for the nine issue keys among 1428 bundles. No target-specific causal overlay or authored definition was located within the named roots. Exact target ID, slug, source labels and mints were searched, including ignored files. Command: rg --no-ignore --hidden -l -i -F -e Engineered &gt; Food production &gt; Meat products -e FOODON:00001006 -e FOODON:00001092 -e FOODON:00005501 -e FOODON:03530206 -e Meat products -e gold.ecosystem:4486 -e habitatmech:GOLD.0347e0d978 -e mammalian meat food product -e mammalian_meat_food_product curation history research conf reviews/structured reports/yaml_record_review data/raw tests |
| MEMBERS | conf/sources.yaml; data/raw/MANIFEST.yaml; data/raw/GOLD_MANIFEST.yaml | supports | Original GOLD nodes/edges, BacDive and PREGO nodes/edges, goldData.xlsx and gold_biosample_triads.tsv were not located by named-file enumeration of 39439 files under /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data. Ignored/hidden files included; .git internals excluded and symlinks not traversed. Frozen inventories remain available. No global absence or exact frozen member reconstruction is claimed. |
| GOLD_ACCESS | https://gold.jgi.doe.gov/ | context_only | Requested exact study pages Gs0111409, Gs0127406, Gs0133016, Gs0150353, Gs0150522, Gs0150710, Gs0154236, Gs0154282; each returned HTTP403. No page text inferred. {"Gs0111409": {"url": "https://gold.jgi.doe.gov/study?id=Gs0111409", "accessed_at": "2026-10-14T13:45:40.887238Z", "error": "HTTP Error 403: Forbidden"}, "Gs0127406": {"url": "https://gold.jgi.doe.gov/study?id=Gs0127406", "accessed_at": "2026-10-14T13:45:41.046759Z", "error": "HTTP Error 403: Forbidden"}, "Gs0133016": {"url": "https://gold.jgi.doe.gov/study?id=Gs0133016", "accessed_at": "2026-10-14T13:45:40.970490Z", "error": "HTTP Error 403: Forbidden"}, "Gs0150353": {"url": "https://gold.jgi.doe.gov/study?id=Gs0150353", "accessed_at": "2026-10-14T13:45:40.808981Z", "error": "HTTP Error 403: Forbidden"}, "Gs0150522": {"url": "https://gold.jgi.doe.gov/study?id=Gs0150522", "accessed_at": "2026-10-14T13:45:40.846257Z", "error": "HTTP Error 403: Forbidden"}, "Gs0150710": {"url": "https://gold.jgi.doe.gov/study?id=Gs0150710", "accessed_at": "2026-10-14T13:45:40.925115Z", "error": "HTTP Error 403: Forbidden"}, "Gs0154236": {"url": "https://gold.jgi.doe.gov/study?id=Gs0154236", "accessed_at": "2026-10-14T13:45:40.727234Z", "error": "HTTP Error 403: Forbidden"}, "Gs0154282": {"url": "https://gold.jgi.doe.gov/study?id=Gs0154282", "accessed_at": "2026-10-14T13:45:41.014612Z", "error": "HTTP Error 403: Forbidden"}} |
| FOODON | https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl | supports | Full pinned RDF/XML class definitions, synonym predicates, named parents and restrictions re-inspected at 2026-10-14T13:45:26.271013Z. FOODON:00001092 and FOODON:00005501 are valid named ontology parents of mammalian meat. FOODON:03530206 is instead a process introduced by the GOLD branch. A source remap must audit the two remaining direct record children and two exact expected-parent exclusion guards; no original poultry/fish members are asserted by this review. Retrieved bytes SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf. |
| BASE_QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38570802819 | supports | Exact scientific-input base 72a79e3782e2657aab8507b45ec9b49ac95bcf13: authoritative merge-queue QC passed, with 1112 tests passed and three skipped; four review contract tests passed. This predates the new review bundles and cannot substitute for their post-save validation. |

## Limits And Additional Notes

- Same-agent review; no independent approval or native status promotion.
- Original source joins were unavailable in bounded searches; exact source counts are preserved without claims of deduplicated biological prevalence.
- Pinned ontology and current NCBI/source pages support bounded interpretations, not an automatic release refresh or whole-population reassessment.
- No scientific input, generated record, history, page, GitHub issue or PR was changed. Actions are proposals only.
- Exact-base QC predates the new review bundles; immutable saver validation and post-save archive checks are separately required.
- No SSSOM/KGX readiness or whole-corpus scientific pass is claimed.
- Original captured input hashes rechecked unchanged before extended inspection at 2026-10-14T13:52:46.670918Z.
- All present identifiers and source references were traced to inspected inventory/ontology/taxonomy evidence; unresolvable live GOLD access is explicitly recorded.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T135505Z-mammalian_meat_food_product
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: mammalian meat food product'
started_at: '2026-10-14T13:43:30.833242Z'
finished_at: '2026-10-14T13:55:05.702699Z'
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
summary: FOODON:00001006 is explicitly mammalian. The only source is generic GOLD
  Meat products, whose ITEM decision itself says the chosen ontology term is narrower
  than the source. A NARROW annotation does not justify using that term as the source
  identity or making Meat products an exact synonym. The original member composition
  was not independently recovered.
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
  - path: data/habitats/food/mammalian_meat_food_product.yaml
    sha256: fab8fbd8e3352bfe93aefac2761dded407774e918244be3e6b8a87ae45ec27b5
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
  description: Entire resolved record and every contributing source concept; one individual
    scientific review.
  selection: Next unreviewed Food records by path after an ignored-inclusive census
    of 999/3208 current records reviewed, Food31/60. This bundle covers one exact
    target, not a cohort sample or corpus certification.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - FOODON:00001006
checks:
- check_id: C5
  name: Native validate
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/food/mammalian_meat_food_product.yaml
  exit_code: 0
  target_ids:
  - FOODON:00001006
  summary: Executed 2026-10-14T13:43:45.116950Z to 2026-10-14T13:43:47.077049Z. No
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
  - FOODON:00001006
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
  - FOODON:00001006
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
  - FOODON:00001006
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
  - FOODON:00001006
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
  - FOODON:00001006
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
  - FOODON:00001006
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
  - FOODON:00001006
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
  - FOODON:00001006
  evidence_ids:
  - BASE_QC
  summary: Hosted QC on the exact unchanged scientific-input commit passed. New review
    archive validation is separate.
- check_id: ORIGINAL
  name: Original source-member reconstruction
  required: false
  status: unavailable
  target_ids:
  - FOODON:00001006
  evidence_ids:
  - MEMBERS
  summary: Bounded ignored-inclusive search did not locate original joins. Nine exact
    GOLD study page requests across this review set returned HTTP403.
- check_id: IMODULON
  name: Expression-module applicability
  required: false
  status: not_applicable
  target_ids:
  - FOODON:00001006
  summary: No gene, regulator, protein or transcriptomic mechanism is asserted. Occurrence
    records are not expression-module claims.
evidence:
- evidence_id: RECORD
  kind: record_content
  reference: data/habitats/food/mammalian_meat_food_product.yaml
  summary: Entire target YAML, all source attestations, optional claims and curation
    events read before judgment.
  accessed_at: '2026-10-14T13:55:05.702344Z'
  support: supports
- evidence_id: RULES
  kind: authority
  reference: docs/CURATION.md; docs/HARMONIZATION.md; src/habitatmech/schema/habitatmech.yaml
  summary: Native exact identity, strict superclass, source-unit, MIxS-role, optional-field
    and all-source ITEM rules applied. FOOD is a coarse layout/reporting bucket for
    food and beverage matrices, not an identity axiom.
  accessed_at: '2026-10-14T13:55:05.702367Z'
  support: supports
- evidence_id: ROWS
  kind: record_content
  reference: data/raw/; curation/decisions.tsv
  summary: 'GOLD row 24 names nodes 4486/4487/4488 and 1916 ORGANISM assertions. Separate
    bulk row 79 contains 438 BIOSAMPLE observations and eight study rows include multipath
    unions. Triad rows 95-97 cover two samples/one study: legume food product as broad,
    fermented sausage as local, and dried fermented sausage as medium. These roles
    and small denominators cannot establish a mammal-only identity; the material-valued
    broad slot is not an ecosystem. ITEM GROUND decision row 118 explains NARROW/REVIEWED
    but records the scope conflict. Parsed row locators, including neighboring comparison
    rows: {"curation/decisions.tsv": [118], "curation/gold_parent_exclusions.tsv":
    [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19], "data/raw/gold_ecosystem_paths.tsv":
    [24, 129, 147, 557, 601, 781, 899, 1300], "data/raw/gold_path_biosamples.tsv":
    [79], "data/raw/gold_path_triads.tsv": [95, 96, 97], "data/raw/gold_studies.tsv":
    [646, 1410, 1794, 3174, 3339, 3522, 3931, 3966], "data/raw/ontology_subclass_edges.tsv":
    [8776, 8777, 8788, 8789, 8811, 8812, 8819, 8901, 8906, 8925, 8982, 8995], "data/raw/ontology_terms.tsv":
    [10512, 10518, 10602, 10732]}'
  accessed_at: '2026-10-14T13:55:05.702464Z'
  support: supports
- evidence_id: TRANSFORMS
  kind: record_content
  reference: src/habitatmech/seed.py; src/habitatmech/extract.py
  summary: Inspected source resolution, immediate GOLD parent contributions, synonym
    scoping, taxon ranks/units and singleton-term parameter gating. GROUND replaces
    the identifier even when status is NARROW; status does not undo a merge. Deterministic
    reproduction does not establish scientific correctness.
  accessed_at: '2026-10-14T13:55:05.702474Z'
  support: supports
- evidence_id: SEARCH
  kind: search
  reference: curation/; history/; research/; reviews/structured/; data/raw/; reports/yaml_record_review/;
    tests/
  summary: 'All matching source/decision rows inspected. No earlier structured declaration
    of these eight targets or collision for the nine issue keys among 1428 bundles.
    No target-specific causal overlay or authored definition was located within the
    named roots. Exact target ID, slug, source labels and mints were searched, including
    ignored files. Command: rg --no-ignore --hidden -l -i -F -e Engineered > Food
    production > Meat products -e FOODON:00001006 -e FOODON:00001092 -e FOODON:00005501
    -e FOODON:03530206 -e Meat products -e gold.ecosystem:4486 -e habitatmech:GOLD.0347e0d978
    -e mammalian meat food product -e mammalian_meat_food_product curation history
    research conf reviews/structured reports/yaml_record_review data/raw tests'
  accessed_at: '2026-10-14T13:55:05.702487Z'
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
  accessed_at: '2026-10-14T13:55:05.702501Z'
  support: supports
  search_scope: Ignored/hidden-inclusive structured parsing and rg within the explicitly
    named roots; not an all-disk absence claim.
- evidence_id: GOLD_ACCESS
  kind: database
  reference: https://gold.jgi.doe.gov/
  summary: 'Requested exact study pages Gs0111409, Gs0127406, Gs0133016, Gs0150353,
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
  summary: Full pinned RDF/XML class definitions, synonym predicates, named parents
    and restrictions re-inspected at 2026-10-14T13:45:26.271013Z. FOODON:00001092
    and FOODON:00005501 are valid named ontology parents of mammalian meat. FOODON:03530206
    is instead a process introduced by the GOLD branch. A source remap must audit
    the two remaining direct record children and two exact expected-parent exclusion
    guards; no original poultry/fish members are asserted by this review. Retrieved
    bytes SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf.
  accessed_at: '2026-10-14T12:27:42.074174Z'
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
  - FOODON:00001006
  evidence_ids:
  - RECORD
  - RULES
  - ROWS
  - TRANSFORMS
  - SEARCH
  - MEMBERS
  - GOLD_ACCESS
  - FOODON
  - BASE_QC
  summary: FOODON:00001006 is explicitly mammalian. The only source is generic GOLD
    Meat products, whose ITEM decision itself says the chosen ontology term is narrower
    than the source. A NARROW annotation does not justify using that term as the source
    identity or making Meat products an exact synonym. The original member composition
    was not independently recovered.
- assessment_id: HIERARCHY
  area: grounding
  topic: Ontology genus versus source context
  outcome: concern
  target_ids:
  - FOODON:00001006
  evidence_ids:
  - RECORD
  - RULES
  - ROWS
  - TRANSFORMS
  - SEARCH
  - MEMBERS
  - GOLD_ACCESS
  - FOODON
  - BASE_QC
  summary: FOODON:00001092 and FOODON:00005501 are valid named ontology parents of
    mammalian meat. FOODON:03530206 is instead a process introduced by the GOLD branch.
    A source remap must audit the two remaining direct record children and two exact
    expected-parent exclusion guards; no original poultry/fish members are asserted
    by this review.
- assessment_id: PROVENANCE
  area: provenance
  topic: Source assertions, units and native gates
  outcome: supported
  target_ids:
  - FOODON:00001006
  evidence_ids:
  - RECORD
  - ROWS
  - TRANSFORMS
  summary: 'GOLD row 24 names nodes 4486/4487/4488 and 1916 ORGANISM assertions. Separate
    bulk row 79 contains 438 BIOSAMPLE observations and eight study rows include multipath
    unions. Triad rows 95-97 cover two samples/one study: legume food product as broad,
    fermented sausage as local, and dried fermented sausage as medium. These roles
    and small denominators cannot establish a mammal-only identity; the material-valued
    broad slot is not an ecosystem. ITEM GROUND decision row 118 explains NARROW/REVIEWED
    but records the scope conflict.'
- assessment_id: OPTIONAL
  area: completeness
  topic: Parameters, taxa, causal evidence and discussion
  outcome: supported
  target_ids:
  - FOODON:00001006
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
  - FOODON:00001006
  evidence_ids:
  - MEMBERS
  summary: The review assesses every present record claim, but original member-level
    provenance is unavailable in the bounded roots. Current source examples do not
    prove original membership, and missing rows or zero counts do not prove environmental
    absence.
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
  - ROWS
  - FOODON
  - TRANSFORMS
  - RULES
  rule_id: Habitat identity, strict genus and source-specific scope
  native_severity: major
  normalization_reason: Unsupported identity equivalence or strict superclass materially
    changes the source meaning.
- finding_id: F2
  issue_key: mammalian-meat-food-production-process-parent
  title: Food production process is not a meat-material genus
  description: The added FOODON:03530206 parent is a planned process, unlike the two
    independently supported material ontology parents. It is a GOLD classification
    context contribution, not a strict material superclass.
  category: grounding
  severity: major
  status: open
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
  - ROWS
  - FOODON
  - TRANSFORMS
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
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - FOODON:00001006
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained owner; generated habitat YAML is read-only
  description: Exclude the exact GOLD Meat products path contribution with expected
    FOODON:03530206, preserving independent material parents on any retained ontology
    record. Coordinate the guarded row with the separate source-identity correction.
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
  2026-10-14T13:52:46.670918Z.
- All present identifiers and source references were traced to inspected inventory/ontology/taxonomy
  evidence; unresolvable live GOLD access is explicitly recorded.
tags:
- habitatmech
- record-review
- food
```
