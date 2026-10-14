# Scientific record review: Frozen shrimp

- Review: 20261014T135443Z-frozen_shrimp
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T13:43:20.660771Z
- Finished UTC: 2026-10-14T13:54:43.786275Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The full GOLD path identifies frozen shrimp food material, a defensible subtype of the retained Frozen seafood source concept. The native mint avoids claiming an unverified ontology equivalent. Freezing is a material condition here, not an asserted process identity or a measured storage temperature.

## Scope And Provenance

Entire resolved record and every contributing source concept; one individual scientific review.

Selection: Next unreviewed Food records by path after an ignored-inclusive census of 999/3208 current records reviewed, Food31/60. This bundle covers one exact target, not a cohort sample or corpus certification.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 72a79e3782e2657aab8507b45ec9b49ac95bcf13.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.1a8cb8aae6 | data/habitats/food/frozen_shrimp.yaml | generated | Frozen shrimp |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | habitatmech:GOLD.1a8cb8aae6 | Executed 2026-10-14T13:43:34.224792Z to 2026-10-14T13:43:36.379868Z. No issues found |
| Native validate-strict | passed | True | habitatmech:GOLD.1a8cb8aae6 | Executed 2026-10-14T13:43:50.998179Z to 2026-10-14T13:43:55.575800Z. uv run python scripts/validate_strict.py data/habitats/food/frozen_shrimp.yaml data/habitats/food/fruit_seed.yaml data/habitats/food/heroin.yaml data/habitats/food/ice_cream.yaml data/habitats/food/juice.yaml data/habitats/food/mammalian_meat_food_product.yaml data/habitats/food/meat_trimming.yaml data/habitats/food/morphine.yaml<br>Validating 8 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      8<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| Native validate-history | passed | True | habitatmech:GOLD.1a8cb8aae6 | Executed 2026-10-14T13:43:55.576413Z to 2026-10-14T13:44:01.983391Z. No issues found<br>670 history record(s) valid against src/habitatmech/schema/history.yaml |
| Native provenance-check | passed | True | habitatmech:GOLD.1a8cb8aae6 | Executed 2026-10-14T13:44:01.984106Z to 2026-10-14T13:44:02.463384Z. provenance current: 14 committed inventories, 2 GOLD sources |
| Native verify-corpus | passed | True | habitatmech:GOLD.1a8cb8aae6 | Executed 2026-10-14T13:44:02.463929Z to 2026-10-14T13:44:15.660795Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| Native validate-causal-all | passed | True | habitatmech:GOLD.1a8cb8aae6 | Executed 2026-10-14T13:44:15.661664Z to 2026-10-14T13:44:19.221370Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| Native term-requests-check | passed | True | habitatmech:GOLD.1a8cb8aae6 | Executed 2026-10-14T13:44:19.222000Z to 2026-10-14T13:44:33.161959Z. term-request table is current (109 terms) |
| Native validate-products | passed | True | habitatmech:GOLD.1a8cb8aae6 | Executed 2026-10-14T13:44:33.162696Z to 2026-10-14T13:45:13.853367Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1176<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2059<br><br>✅ All id↔label pairs correspond. |
| Exact-base authoritative QC | passed | True | habitatmech:GOLD.1a8cb8aae6 | Hosted QC on the exact unchanged scientific-input commit passed. New review archive validation is separate. |
| Original source-member reconstruction | unavailable | False | habitatmech:GOLD.1a8cb8aae6 | Bounded ignored-inclusive search did not locate original joins. Nine exact GOLD study page requests across this review set returned HTTP403. |
| Expression-module applicability | not_applicable | False | habitatmech:GOLD.1a8cb8aae6 | No gene, regulator, protein or transcriptomic mechanism is asserted. Occurrence records are not expression-module claims. |

## Scientific And Domain Assessments

### Habitat/source identity and exact scope

identity: supported. Targets: habitatmech:GOLD.1a8cb8aae6.

The full GOLD path identifies frozen shrimp food material, a defensible subtype of the retained Frozen seafood source concept. The native mint avoids claiming an unverified ontology equivalent. Freezing is a material condition here, not an asserted process identity or a measured storage temperature.

### Ontology genus versus source context

grounding: supported. Targets: habitatmech:GOLD.1a8cb8aae6.

The immediate parent habitatmech:GOLD.39a9e4ecb4 is Frozen seafood. That source-level material genus is supported by the full path. No global ontology-equivalence absence, growth-at-freezing claim, or certification of more distant ancestors is made.

### Source assertions, units and native gates

provenance: supported. Targets: habitatmech:GOLD.1a8cb8aae6.

GOLD row 782 names node 7232 and two ORGANISM-unit assertions. Separate bulk row 381 records 40 BIOSAMPLE observations; study row 1321 names the single-path Gs0121348. These are different snapshots and units, not 42 interchangeable observations. Own CLASS decision row 248 and parent CLASS decision row 415 explain UNGROUNDED/SEEDED. No target triad or parameter row was found in the parsed inventories.

### Parameters, taxa, causal evidence and discussion

completeness: supported. Targets: habitatmech:GOLD.1a8cb8aae6.

No environmental parameter, causal graph, cited mechanism, dataset or discussion claim is present to validate. Optional absence is not itself a defect. Displayed taxa, where present, remain source associations without characteristic flags; counts/ranks are not prevalence or mechanism evidence.

### Independent membership and unavailable source context

evidence: unknown. Targets: habitatmech:GOLD.1a8cb8aae6.

The review assesses every present record claim, but original member-level provenance is unavailable in the bounded roots. Current source examples do not prove original membership, and missing rows or zero counts do not prove environmental absence.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| RECORD | data/habitats/food/frozen_shrimp.yaml | supports | Entire target YAML, all source attestations, optional claims and curation events read before judgment. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; src/habitatmech/schema/habitatmech.yaml | supports | Native exact identity, strict superclass, source-unit, MIxS-role, optional-field and all-source ITEM rules applied. FOOD is a coarse layout/reporting bucket for food and beverage matrices, not an identity axiom. |
| ROWS | data/raw/; curation/decisions.tsv | supports | GOLD row 782 names node 7232 and two ORGANISM-unit assertions. Separate bulk row 381 records 40 BIOSAMPLE observations; study row 1321 names the single-path Gs0121348. These are different snapshots and units, not 42 interchangeable observations. Own CLASS decision row 248 and parent CLASS decision row 415 explain UNGROUNDED/SEEDED. No target triad or parameter row was found in the parsed inventories. Parsed row locators, including neighboring comparison rows: {"curation/decisions.tsv": [248, 415], "data/raw/gold_ecosystem_paths.tsv": [782], "data/raw/gold_path_biosamples.tsv": [381], "data/raw/gold_studies.tsv": [1321]} |
| TRANSFORMS | src/habitatmech/seed.py; src/habitatmech/extract.py | supports | Inspected source resolution, immediate GOLD parent contributions, synonym scoping, taxon ranks/units and singleton-term parameter gating. GROUND replaces the identifier even when status is NARROW; status does not undo a merge. Deterministic reproduction does not establish scientific correctness. |
| SEARCH | curation/; history/; research/; reviews/structured/; data/raw/; reports/yaml_record_review/; tests/ | supports | All matching source/decision rows inspected. No earlier structured declaration of these eight targets or collision for the nine issue keys among 1428 bundles. No target-specific causal overlay or authored definition was located within the named roots. Exact target ID, slug, source labels and mints were searched, including ignored files. Command: rg --no-ignore --hidden -l -i -F -e Engineered &gt; Food production &gt; Seafood product &gt; Frozen seafood &gt; Frozen shrimp -e Frozen shrimp -e frozen_shrimp -e gold.ecosystem:7232 -e habitatmech:GOLD.1a8cb8aae6 -e habitatmech:GOLD.39a9e4ecb4 curation history research conf reviews/structured reports/yaml_record_review data/raw tests |
| MEMBERS | conf/sources.yaml; data/raw/MANIFEST.yaml; data/raw/GOLD_MANIFEST.yaml | supports | Original GOLD nodes/edges, BacDive and PREGO nodes/edges, goldData.xlsx and gold_biosample_triads.tsv were not located by named-file enumeration of 39439 files under /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data. Ignored/hidden files included; .git internals excluded and symlinks not traversed. Frozen inventories remain available. No global absence or exact frozen member reconstruction is claimed. |
| GOLD_ACCESS | https://gold.jgi.doe.gov/ | context_only | Requested exact study pages Gs0121348; each returned HTTP403. No page text inferred. {"Gs0121348": {"url": "https://gold.jgi.doe.gov/study?id=Gs0121348", "accessed_at": "2026-10-14T13:45:40.764271Z", "error": "HTTP Error 403: Forbidden"}} |
| BASE_QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38570802819 | supports | Exact scientific-input base 72a79e3782e2657aab8507b45ec9b49ac95bcf13: authoritative merge-queue QC passed, with 1112 tests passed and three skipped; four review contract tests passed. This predates the new review bundles and cannot substitute for their post-save validation. |

## Limits And Additional Notes

- Same-agent review; no independent approval or native status promotion.
- Original source joins were unavailable in bounded searches; exact source counts are preserved without claims of deduplicated biological prevalence.
- Pinned ontology and current NCBI/source pages support bounded interpretations, not an automatic release refresh or whole-population reassessment.
- No scientific input, generated record, history, page, GitHub issue or PR was changed. Actions are proposals only.
- Exact-base QC predates the new review bundles; immutable saver validation and post-save archive checks are separately required.
- No SSSOM/KGX readiness or whole-corpus scientific pass is claimed.
- Original captured input hashes rechecked unchanged before extended inspection at 2026-10-14T13:52:36.920668Z.
- All present identifiers and source references were traced to inspected inventory/ontology/taxonomy evidence; unresolvable live GOLD access is explicitly recorded.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T135443Z-frozen_shrimp
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: Frozen shrimp'
started_at: '2026-10-14T13:43:20.660771Z'
finished_at: '2026-10-14T13:54:43.786275Z'
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
verdict: pass_with_limitations
summary: The full GOLD path identifies frozen shrimp food material, a defensible subtype
  of the retained Frozen seafood source concept. The native mint avoids claiming an
  unverified ontology equivalent. Freezing is a material condition here, not an asserted
  process identity or a measured storage temperature.
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
  - path: data/habitats/food/frozen_shrimp.yaml
    sha256: 5c9e2eed1a3116de5ff1ee0e4bb756ce6985933aada7876f8d3d943db1ccbbf1
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
- target_id: habitatmech:GOLD.1a8cb8aae6
  path: data/habitats/food/frozen_shrimp.yaml
  label: Frozen shrimp
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
    path: data/raw/gold_studies.tsv
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
  - habitatmech:GOLD.1a8cb8aae6
checks:
- check_id: C0
  name: Native validate
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/food/frozen_shrimp.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1a8cb8aae6
  summary: Executed 2026-10-14T13:43:34.224792Z to 2026-10-14T13:43:36.379868Z. No
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
  - habitatmech:GOLD.1a8cb8aae6
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
  - habitatmech:GOLD.1a8cb8aae6
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
  - habitatmech:GOLD.1a8cb8aae6
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
  - habitatmech:GOLD.1a8cb8aae6
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
  - habitatmech:GOLD.1a8cb8aae6
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
  - habitatmech:GOLD.1a8cb8aae6
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
  - habitatmech:GOLD.1a8cb8aae6
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
  - habitatmech:GOLD.1a8cb8aae6
  evidence_ids:
  - BASE_QC
  summary: Hosted QC on the exact unchanged scientific-input commit passed. New review
    archive validation is separate.
- check_id: ORIGINAL
  name: Original source-member reconstruction
  required: false
  status: unavailable
  target_ids:
  - habitatmech:GOLD.1a8cb8aae6
  evidence_ids:
  - MEMBERS
  summary: Bounded ignored-inclusive search did not locate original joins. Nine exact
    GOLD study page requests across this review set returned HTTP403.
- check_id: IMODULON
  name: Expression-module applicability
  required: false
  status: not_applicable
  target_ids:
  - habitatmech:GOLD.1a8cb8aae6
  summary: No gene, regulator, protein or transcriptomic mechanism is asserted. Occurrence
    records are not expression-module claims.
evidence:
- evidence_id: RECORD
  kind: record_content
  reference: data/habitats/food/frozen_shrimp.yaml
  summary: Entire target YAML, all source attestations, optional claims and curation
    events read before judgment.
  accessed_at: '2026-10-14T13:54:43.785818Z'
  support: supports
- evidence_id: RULES
  kind: authority
  reference: docs/CURATION.md; docs/HARMONIZATION.md; src/habitatmech/schema/habitatmech.yaml
  summary: Native exact identity, strict superclass, source-unit, MIxS-role, optional-field
    and all-source ITEM rules applied. FOOD is a coarse layout/reporting bucket for
    food and beverage matrices, not an identity axiom.
  accessed_at: '2026-10-14T13:54:43.786008Z'
  support: supports
- evidence_id: ROWS
  kind: record_content
  reference: data/raw/; curation/decisions.tsv
  summary: 'GOLD row 782 names node 7232 and two ORGANISM-unit assertions. Separate
    bulk row 381 records 40 BIOSAMPLE observations; study row 1321 names the single-path
    Gs0121348. These are different snapshots and units, not 42 interchangeable observations.
    Own CLASS decision row 248 and parent CLASS decision row 415 explain UNGROUNDED/SEEDED.
    No target triad or parameter row was found in the parsed inventories. Parsed row
    locators, including neighboring comparison rows: {"curation/decisions.tsv": [248,
    415], "data/raw/gold_ecosystem_paths.tsv": [782], "data/raw/gold_path_biosamples.tsv":
    [381], "data/raw/gold_studies.tsv": [1321]}'
  accessed_at: '2026-10-14T13:54:43.786097Z'
  support: supports
- evidence_id: TRANSFORMS
  kind: record_content
  reference: src/habitatmech/seed.py; src/habitatmech/extract.py
  summary: Inspected source resolution, immediate GOLD parent contributions, synonym
    scoping, taxon ranks/units and singleton-term parameter gating. GROUND replaces
    the identifier even when status is NARROW; status does not undo a merge. Deterministic
    reproduction does not establish scientific correctness.
  accessed_at: '2026-10-14T13:54:43.786106Z'
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
    production > Seafood product > Frozen seafood > Frozen shrimp -e Frozen shrimp
    -e frozen_shrimp -e gold.ecosystem:7232 -e habitatmech:GOLD.1a8cb8aae6 -e habitatmech:GOLD.39a9e4ecb4
    curation history research conf reviews/structured reports/yaml_record_review data/raw
    tests'
  accessed_at: '2026-10-14T13:54:43.786117Z'
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
  accessed_at: '2026-10-14T13:54:43.786129Z'
  support: supports
  search_scope: Ignored/hidden-inclusive structured parsing and rg within the explicitly
    named roots; not an all-disk absence claim.
- evidence_id: GOLD_ACCESS
  kind: database
  reference: https://gold.jgi.doe.gov/
  summary: 'Requested exact study pages Gs0121348; each returned HTTP403. No page
    text inferred. {"Gs0121348": {"url": "https://gold.jgi.doe.gov/study?id=Gs0121348",
    "accessed_at": "2026-10-14T13:45:40.764271Z", "error": "HTTP Error 403: Forbidden"}}'
  accessed_at: '2026-10-14T13:54:43.786178Z'
  support: context_only
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
  outcome: supported
  target_ids:
  - habitatmech:GOLD.1a8cb8aae6
  evidence_ids:
  - RECORD
  - RULES
  - ROWS
  - TRANSFORMS
  - SEARCH
  - MEMBERS
  - GOLD_ACCESS
  - BASE_QC
  summary: The full GOLD path identifies frozen shrimp food material, a defensible
    subtype of the retained Frozen seafood source concept. The native mint avoids
    claiming an unverified ontology equivalent. Freezing is a material condition here,
    not an asserted process identity or a measured storage temperature.
- assessment_id: HIERARCHY
  area: grounding
  topic: Ontology genus versus source context
  outcome: supported
  target_ids:
  - habitatmech:GOLD.1a8cb8aae6
  evidence_ids:
  - RECORD
  - RULES
  - ROWS
  - TRANSFORMS
  - SEARCH
  - MEMBERS
  - GOLD_ACCESS
  - BASE_QC
  summary: The immediate parent habitatmech:GOLD.39a9e4ecb4 is Frozen seafood. That
    source-level material genus is supported by the full path. No global ontology-equivalence
    absence, growth-at-freezing claim, or certification of more distant ancestors
    is made.
- assessment_id: PROVENANCE
  area: provenance
  topic: Source assertions, units and native gates
  outcome: supported
  target_ids:
  - habitatmech:GOLD.1a8cb8aae6
  evidence_ids:
  - RECORD
  - ROWS
  - TRANSFORMS
  summary: GOLD row 782 names node 7232 and two ORGANISM-unit assertions. Separate
    bulk row 381 records 40 BIOSAMPLE observations; study row 1321 names the single-path
    Gs0121348. These are different snapshots and units, not 42 interchangeable observations.
    Own CLASS decision row 248 and parent CLASS decision row 415 explain UNGROUNDED/SEEDED.
    No target triad or parameter row was found in the parsed inventories.
- assessment_id: OPTIONAL
  area: completeness
  topic: Parameters, taxa, causal evidence and discussion
  outcome: supported
  target_ids:
  - habitatmech:GOLD.1a8cb8aae6
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
  - habitatmech:GOLD.1a8cb8aae6
  evidence_ids:
  - MEMBERS
  summary: The review assesses every present record claim, but original member-level
    provenance is unavailable in the bounded roots. Current source examples do not
    prove original membership, and missing rows or zero counts do not prove environmental
    absence.
findings: []
actions: []
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
  2026-10-14T13:52:36.920668Z.
- All present identifiers and source references were traced to inspected inventory/ontology/taxonomy
  evidence; unresolvable live GOLD access is explicitly recorded.
tags:
- habitatmech
- record-review
- food
```
