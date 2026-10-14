# Scientific follow-up: Raw meat

- Review: 20261014T164047Z-raw_meat-followup
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T16:28:35Z
- Finished UTC: 2026-10-14T16:40:47Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact immediate GOLD parent contribution is excluded through its maintained source-path/expected-parent guard. No replacement genus is invented; the empty optional parent list is omitted. Identity, source nodes/path, counts/units, native status and all other claims are preserved. Parent Meat products identity #2078 and child Meat trimming scope #2080 remain open; neither is repaired here.

## Scope And Provenance

Entire corrected record and all exact predecessor findings.

Selection: Explicit correction follow-up, one target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 249b157d73e8612bb0609a1764e7edd2712ee9bc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.43005e4de2 | data/habitats/food/raw_meat.yaml | generated | Raw meat |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate | passed | True | habitatmech:GOLD.43005e4de2 | Executed 2026-10-14T15:54:45Z to 2026-10-14T15:54:47Z. No issues found |
| just validate-strict | passed | True | habitatmech:GOLD.43005e4de2 | Executed 2026-10-14T15:54:47Z to 2026-10-14T15:54:52Z. uv run python scripts/validate_strict.py data/habitats/food/nut_whole_or_pieces.yaml data/habitats/food/pastry.yaml data/habitats/food/pit_mud.yaml data/habitats/food/plant_products.yaml data/habitats/food/raw_meat.yaml<br>Validating 5 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      5<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m | passed | True | habitatmech:GOLD.43005e4de2 | Executed 2026-10-14T15:54:52Z to 2026-10-14T15:56:13Z. .........................................................                [100%]<br>57 passed in 80.29s (0:01:20) |
| just validate-history | passed | True | habitatmech:GOLD.43005e4de2 | Executed 2026-10-14T15:56:13Z to 2026-10-14T15:56:19Z. No issues found<br>679 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | habitatmech:GOLD.43005e4de2 | Executed 2026-10-14T15:56:19Z to 2026-10-14T15:56:20Z. provenance current: 14 committed inventories, 2 GOLD sources |
| just verify-corpus | passed | True | habitatmech:GOLD.43005e4de2 | Executed 2026-10-14T15:56:20Z to 2026-10-14T15:56:33Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| just validate-causal-all | passed | True | habitatmech:GOLD.43005e4de2 | Executed 2026-10-14T15:56:33Z to 2026-10-14T15:56:36Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| just validate-products | passed | True | habitatmech:GOLD.43005e4de2 | Executed 2026-10-14T15:56:36Z to 2026-10-14T15:57:17Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1176<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2059<br><br>✅ All id↔label pairs correspond. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m | passed | True | habitatmech:GOLD.43005e4de2 | Executed 2026-10-14T16:01:25Z to 2026-10-14T16:01:31Z. .                                                                        [100%]<br>1 passed in 4.56s |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python scripts/render_pages.py | passed | True | habitatmech:GOLD.43005e4de2 | Executed 2026-10-14T16:01:31Z to 2026-10-14T16:02:00Z. rendered 3208 habitat pages, 254 redirect stubs, 8 categories, 117 term requests -&gt; /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmpu4nlmq9a/site<br>pages/ is in step with the corpus |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python scripts/build_term_requests.py | passed | True | habitatmech:GOLD.43005e4de2 | Executed 2026-10-14T16:02:00Z to 2026-10-14T16:02:15Z. term-request table is current (109 terms) |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python scripts/check_docs.py | passed | True | habitatmech:GOLD.43005e4de2 | Executed 2026-10-14T16:02:15Z to 2026-10-14T16:02:29Z. README corpus statistics are current |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python scripts/build_redirects.py | passed | True | habitatmech:GOLD.43005e4de2 | Executed 2026-10-14T16:02:29Z to 2026-10-14T16:04:04Z. RETIRED.tsv is current (254 redirects) |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m | passed | True | habitatmech:GOLD.43005e4de2 | Executed 2026-10-14T16:04:04Z to 2026-10-14T16:04:04Z. All checks passed! |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m | passed | True | habitatmech:GOLD.43005e4de2 | Executed 2026-10-14T16:28:09Z to 2026-10-14T16:28:18Z. .....................                                                    [100%]<br>21 passed in 8.07s |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m | passed | True | habitatmech:GOLD.43005e4de2 | Executed 2026-10-14T16:28:18Z to 2026-10-14T16:28:18Z. All checks passed! |
| Exact corrected-base authoritative QC | passed | True | habitatmech:GOLD.43005e4de2 | Verified success for the captured corrected commit; final archive checks are separate. |
| Original members | unavailable | False | habitatmech:GOLD.43005e4de2 | Predecessor bounded search/access limitations remain; no original joins were recovered by this repair. |
| Expression-module applicability | not_applicable | False | habitatmech:GOLD.43005e4de2 | No transcriptomic mechanism asserted. |

## Scientific And Domain Assessments

### Exact hierarchy correction

grounding: supported. Targets: habitatmech:GOLD.43005e4de2.

The exact immediate GOLD parent contribution is excluded through its maintained source-path/expected-parent guard. No replacement genus is invented; the empty optional parent list is omitted. Identity, source nodes/path, counts/units, native status and all other claims are preserved. Parent Meat products identity #2078 and child Meat trimming scope #2080 remain open; neither is repaired here.

### Identity and source claims

provenance: supported. Targets: habitatmech:GOLD.43005e4de2.

Complete record re-read. Counts and units are preserved, not summed across organism/biosample snapshots. All optional fields and prior events remain unchanged; no taxon/parameter/causal assertion is introduced.

### Independent category and status

scope: supported. Targets: habitatmech:GOLD.43005e4de2.

Existing category and ITEM/CLASS-derived native status are preserved; this review does not promote them.

### Original source scope

evidence: unknown. Targets: habitatmech:GOLD.43005e4de2.

Unavailable original member joins remain a limitation. Source labels and current examples do not establish every historical member or exact ontology identity. No neighboring-record closure or SSSOM/KGX readiness is implied.

## Findings

### F1: Generic raw meat inherits an unsupported mammalian restriction

major / resolved / confirmed; issue key: raw-meat-mammalian-parent.

FOODON:00001006 is mammalian meat food product. Its restriction is not established for the generic raw-meat source. Current children Beef chop and Meat trimming do not establish universal mammalian scope. Coordinate the exact expected-parent guard with open parent identity issue2078; do not silently change either child.

Disposition: Scoped hierarchy correction verified. The exact immediate GOLD parent contribution is excluded through its maintained source-path/expected-parent guard. No replacement genus is invented; the empty optional parent list is omitted. Identity, source nodes/path, counts/units, native status and all other claims are preserved. Parent Meat products identity #2078 and child Meat trimming scope #2080 remain open; neither is repaired here.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| CURRENT | data/habitats/food/raw_meat.yaml | supports | Complete corrected record and predecessor diff inspected. The exact immediate GOLD parent contribution is excluded through its maintained source-path/expected-parent guard. No replacement genus is invented; the empty optional parent list is omitted. Identity, source nodes/path, counts/units, native status and all other claims are preserved. Parent Meat products identity #2078 and child Meat trimming scope #2080 remain open; neither is repaired here. |
| OWNERS | curation/gold_parent_exclusions.tsv; tests/test_food_context_parent_repairs.py; tests/test_ontology_labels.py | supports | Five guarded rows and five append-only histories read. Counterfactual full-corpus test proves exactly five identifiers change, only parents and generated history. Two older pastry assertions required repair: optional-list indexing and an explicit obsolete production-parent expectation. Initial full QC38594694439 exposed the second after the first focused check passed (1113passed,1failed,3skipped). Both are corrected, with the complete ontology-label module and counterfactual regression rerun. No scientific schema/generator relaxation. |
| PREVIOUS | reviews/structured/20261014T155038Z-raw_meat/review.yaml | supports | Entire predecessor retained unchanged; original rows/parent values are historical. All predecessor findings are reassessed explicitly. |
| QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38598374337 | supports | Authoritative corrected-base QC passed on 249b157d73e8612bb0609a1764e7edd2712ee9bc. This predates these successor bundles; final archive/PR gates remain required. |
| MAP | https://github.com/CultureBotAI/HabitatMech/actions/runs/38593642962 | supports | Pinned locked BGE/PaCMAP pipeline rebuilt five changed inputs, proved repeat reuse and all3208 full-pass reuse. Downloaded full inputs matched local fresh adapter bytes; map/cache/hash validation passed. No freshness bypass or fabricated coordinates. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; src/habitatmech/schema/habitatmech.yaml | supports | Previously inspected evidence, not a new retrieval or current-row annotation. Strictly broader parent_habitats, exact identity versus parent grounding, source-unit semantics, FOOD food/beverage matrix category and all-source ITEM gates applied. |
| MEMBERS | conf/sources.yaml; data/raw/MANIFEST.yaml; data/raw/GOLD_MANIFEST.yaml | supports | Previously inspected evidence, not a new retrieval or current-row annotation. Original GOLD_nodes.tsv, GOLD_edges.tsv, goldData.xlsx and gold_biosample_triads.tsv were not located among 41639 files in the repository and configured kg-microbe data root. Exact command: rg --no-ignore --hidden --files . /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data. Frozen inventories remain available. Counts are frozen aggregate assertions, not independently certified distinct specimens. |
| GOLD_ACCESS | https://gold.jgi.doe.gov/ | context_only | Previously inspected evidence, not a new retrieval or current-row annotation. Four exact study requests returned HTTP403. Eight schema-prefix-expanded ecosystem URL requests returned HTTP404; these browser routes may be unsupported and do not invalidate frozen IDs. No inaccessible page text was inferred. Exact receipt: {"Gs0145265": {"accessed_at": "2026-10-14T15:35:02.815165Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0145265"}, "Gs0153654": {"accessed_at": "2026-10-14T15:35:02.848735Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153654"}, "Gs0154236": {"accessed_at": "2026-10-14T15:35:02.900438Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154236"}, "Gs0154282": {"accessed_at": "2026-10-14T15:35:02.948589Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"}, "gold.ecosystem:5633": {"accessed_at": "2026-10-14T15:35:03.845098Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5633"}, "gold.ecosystem:5892": {"accessed_at": "2026-10-14T15:35:04.088840Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5892"}, "gold.ecosystem:5939": {"accessed_at": "2026-10-14T15:35:03.359272Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5939"}, "gold.ecosystem:5942": {"accessed_at": "2026-10-14T15:35:03.586048Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5942"}, "gold.ecosystem:6419": {"accessed_at": "2026-10-14T15:35:04.251825Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/6419"}, "gold.ecosystem:6424": {"accessed_at": "2026-10-14T15:35:04.621271Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/6424"}, "gold.ecosystem:6971": {"accessed_at": "2026-10-14T15:35:05.075424Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/6971"}, "gold.ecosystem:7384": {"accessed_at": "2026-10-14T15:35:04.879190Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/7384"}} |
| FOODON | https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl | supports | Previously inspected evidence, not a new retrieval or current-row annotation. Pinned full FoodOn class XML re-inspected at 2026-10-14T15:34:45.849036Z: definitions, synonyms, restrictions and parents, not just labels. FOODON:00001006 is mammalian meat food product. Its restriction is not established for the generic raw-meat source. Current children Beef chop and Meat trimming do not establish universal mammalian scope. Coordinate the exact expected-parent guard with open parent identity issue2078; do not silently change either child. Retrieved SHA256: b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf. |

## Limits And Additional Notes

- Same-agent review, not independent approval.
- Original joins remain unavailable; no exact source-member reconstruction.
- Initial site check correctly failed on the stale semantic map; the governed rebuild and subsequent site checks passed.
- Pit-mud category #2086 and shared endpoint #1398 remain open. Neighboring source-identity issues are not closed by these repairs.
- Corrected-base QC predates these successors; final immutable archive and PR checks remain required.
- No whole-corpus scientific pass, ontology refresh or SSSOM/KGX certification.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T164047Z-raw_meat-followup
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific follow-up: Raw meat'
started_at: '2026-10-14T16:28:35Z'
finished_at: '2026-10-14T16:40:47Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent has maintained and reviewed HabitatMech; no independent
    approval.
skill: .claude/skills/curate-yaml-record/SKILL.md
completion: completed
scientific_review: true
verdict: pass_with_limitations
summary: 'The exact immediate GOLD parent contribution is excluded through its maintained
  source-path/expected-parent guard. No replacement genus is invented; the empty optional
  parent list is omitted. Identity, source nodes/path, counts/units, native status
  and all other claims are preserved. Parent Meat products identity #2078 and child
  Meat trimming scope #2080 remain open; neither is repaired here.'
source:
  git_revision: 249b157d73e8612bb0609a1764e7edd2712ee9bc
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
  - path: conf/ontology_label_refresh.yaml
    sha256: b9960ab7d9b4e210af377db21a35147a5420a937d828da1a11b976a35821bb21
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
  - path: data/habitats/engineered/mud__d8cb1234.yaml
    sha256: 648f5fbe5a2ed08fd224ce4f3b8c2372b44d28f7e93c3be7884d9311126760a0
    role: context
  - path: data/habitats/food/beef_chop.yaml
    sha256: b8254ef3a766d2260f2d65da11284b5ad089c7d7b72d0bf5635b2708abc19e92
    role: context
  - path: data/habitats/food/dairy_food_product.yaml
    sha256: 36c6b5dde12d0d75eca04ac0f91200e839763e14e2ff813ebb85fb7242fb3001
    role: context
  - path: data/habitats/food/fermentation_cellar.yaml
    sha256: ddf0dc98e3046a94be1963662b6226c555ce41cc555cbf8b2fcd17682c9aa2df
    role: context
  - path: data/habitats/food/fish_products.yaml
    sha256: acfda4de9940c1d1debc932bea029f0db5f6b61a171972d94dc18c19f42a6a31
    role: context
  - path: data/habitats/food/food_production.yaml
    sha256: b0fce7af2cc321a0979ce4d3bfec5e2d4383410ae8e62172b006073afb783ab7
    role: context
  - path: data/habitats/food/heroin.yaml
    sha256: aba9a2c57d7b8c0623829ca417045d03dff4cbf903ca217b000b2491c44be5d0
    role: context
  - path: data/habitats/food/mammalian_meat_food_product.yaml
    sha256: 5297b7ec6ffa54a867f9b9a4485fb539f15085e0495e1299bbc4145c238fff49
    role: context
  - path: data/habitats/food/meat_trimming.yaml
    sha256: b3f38c7bb46375d1cc24f455d3df5a89b6e12e99d33693e47ce8ce9f8f94ac73
    role: context
  - path: data/habitats/food/morphine.yaml
    sha256: a1f55ea3d879d5f3f83f7433700fe238539e5ac408ac1cd86c79503178d61eee
    role: context
  - path: data/habitats/food/nut_whole_or_pieces.yaml
    sha256: 693e0d1497df09b012cfc93138073c2eb0f34bd9f2a9ff053db020fbd2e3d510
    role: context
  - path: data/habitats/food/pastry.yaml
    sha256: 3b3c9b328209f936184f03670a5bba6715009793374ad7a660ed7d8401869dd9
    role: context
  - path: data/habitats/food/pit_mud.yaml
    sha256: 804906d88d129b0b7800a670676dc83406f75fd4b59b7b04cffa7118f7c5ae18
    role: context
  - path: data/habitats/food/plant_products.yaml
    sha256: 498662fdda33605304d1d4a515c9a9405276ff82229a546e3dcd705603892455
    role: context
  - path: data/habitats/food/processed_milk.yaml
    sha256: e3b6ea0518b25881230132d9b4244b04b1e2b2644ccd75cb0e18281b1e95aab6
    role: context
  - path: data/habitats/food/raw_meat.yaml
    sha256: e90de1185ecf19c369e05c6315f56eaf03d9ab2ae58e211451877414bcc64276
    role: target
  - path: data/habitats/food/raw_milk.yaml
    sha256: 367e4914f54a5202214c2c6d06a032641885f12de4cf23c94512294caab8e7d1
    role: context
  - path: data/habitats/food/salted_fish.yaml
    sha256: 8c08be6b9aaaabab2c206d0c9c5cf988a446854fbc5d4175383fcb9fcc679362
    role: context
  - path: data/habitats/host_associated/milk.yaml
    sha256: 0d95a2f239a7218eb4152e2efe4bec72c2372507786a9a2ac9e7301f5a0e49c1
    role: context
  - path: data/ontology_label_refresh.json
    sha256: 4be829efda56a39afe47daf83c3a384bab4b9c17f132ebbee799e721a4442c91
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
  - path: history/infrastructure/term_request_site_exclusions/2026-10-08T041045Z-codex-391ff0.yaml
    sha256: 38e02895c141089e84b7af821be985bfb3b36e18fe800e641f047cacfc3bc4ea
    role: context
  - path: history/mappings/foodon_beverage_pastry_scope/2026-10-08T034738Z-codex-4bb239.yaml
    sha256: 3b55dd188863916f4fda7a1813547e08473f124cbb0188aba284e700a1d48ae9
    role: context
  - path: history/mappings/nut_whole_or_pieces/2026-10-14T155324Z-codex-gpt-5-d5c277.yaml
    sha256: 03f597b8d8bdc896bbb61e7810be14076041d14af60f3ac92406c02bfb89fb7d
    role: context
  - path: history/mappings/pastry/2026-10-14T155327Z-codex-gpt-5-e19417.yaml
    sha256: 316dd2fdc5feba7c8425c112b31e33d847978063850797092b4d79947dd0e4ed
    role: context
  - path: history/mappings/pit_mud/2026-10-14T155329Z-codex-gpt-5-f00d87.yaml
    sha256: 72efd5f1749c1bfe6672dd0605abd4fa313a8239f648396a91fc0cd1fce455a3
    role: context
  - path: history/mappings/plant_products/2026-10-14T155331Z-codex-gpt-5-70025f.yaml
    sha256: 5248a36a1bae8bd05643988cd6eeb917ce7126e6b10bfe89bd0ea83d96ddf44d
    role: context
  - path: history/mappings/raw_meat/2026-10-14T155334Z-codex-gpt-5-16ad39.yaml
    sha256: a493ff0af5e868e5cbc0f4718446a15f2bc52e43da446664aef68a750596a163
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260928T183532Z-fermentation-cellar.md
    sha256: e9acb64abd2e1d93fdffc4d0e7d0a144d1c757f527393d4f4644b1b8c4605d1b
    role: context
  - path: reviews/structured/20261009T164402Z-fermentation-pit-mud/review.yaml
    sha256: 908086f6b63f82059f84e8886893462014178845464b1d399cd1ef5f1506da8c
    role: context
  - path: reviews/structured/20261014T144754Z-mammalian_meat_food_product-followup/review.yaml
    sha256: 5d1511a2b4182162458180aa10e79019b1866abf2790db6778709ccf9e352881
    role: context
  - path: reviews/structured/20261014T155038Z-raw_meat/review.yaml
    sha256: 36b2b93b55b0219bfe390df061adb91a440c955870b4ab51255ba757a981235e
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
  - path: tests/test_fermentation_pit_mud_parent.py
    sha256: de24ee1a9be08c82f84bcdfb6a41e6fe9f8c34e7247102cb63df7b019e206aee
    role: context
  - path: tests/test_food_context_parent_repairs.py
    sha256: 331ed0421f5d45a47a0cd338d31d83b9f9caf2977bf540e53ae1606e56aefa57
    role: context
  - path: tests/test_ontology_labels.py
    sha256: 7dd1b5b9153e439f9d6e2e21ec4a4ae4de666c046b6c207feceeb4a178b937d5
    role: context
targets:
- target_id: habitatmech:GOLD.43005e4de2
  path: data/habitats/food/raw_meat.yaml
  label: Raw meat
  kind: generated
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input; regenerate habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input; regenerate habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Maintained input; regenerate habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Maintained input; regenerate habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Maintained input; regenerate habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input; regenerate habitat YAML
scope:
  description: Entire corrected record and all exact predecessor findings.
  selection: Explicit correction follow-up, one target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.43005e4de2
checks:
- check_id: C4
  name: just validate
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.43005e4de2
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/food/raw_meat.yaml
  exit_code: 0
  summary: Executed 2026-10-14T15:54:45Z to 2026-10-14T15:54:47Z. No issues found
- check_id: C5
  name: just validate-strict
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.43005e4de2
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/food/nut_whole_or_pieces.yaml data/habitats/food/pastry.yaml data/habitats/food/pit_mud.yaml
    data/habitats/food/plant_products.yaml data/habitats/food/raw_meat.yaml
  exit_code: 0
  summary: "Executed 2026-10-14T15:54:47Z to 2026-10-14T15:54:52Z. uv run python scripts/validate_strict.py\
    \ data/habitats/food/nut_whole_or_pieces.yaml data/habitats/food/pastry.yaml data/habitats/food/pit_mud.yaml\
    \ data/habitats/food/plant_products.yaml data/habitats/food/raw_meat.yaml\nValidating\
    \ 5 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      5\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
- check_id: C6
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.43005e4de2
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_food_context_parent_repairs.py tests/test_gold_parent_exclusions.py
    tests/test_fermentation_pit_mud_parent.py
  exit_code: 0
  summary: 'Executed 2026-10-14T15:54:52Z to 2026-10-14T15:56:13Z. .........................................................                [100%]

    57 passed in 80.29s (0:01:20)'
- check_id: C7
  name: just validate-history
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.43005e4de2
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  summary: 'Executed 2026-10-14T15:56:13Z to 2026-10-14T15:56:19Z. No issues found

    679 history record(s) valid against src/habitatmech/schema/history.yaml'
- check_id: C8
  name: just provenance-check
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.43005e4de2
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  summary: 'Executed 2026-10-14T15:56:19Z to 2026-10-14T15:56:20Z. provenance current:
    14 committed inventories, 2 GOLD sources'
- check_id: C9
  name: just verify-corpus
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.43005e4de2
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  summary: "Executed 2026-10-14T15:56:20Z to 2026-10-14T15:56:33Z. expected 3208 records,\
    \ found 3208 on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus\
    \ reproduces exactly from data/raw/"
- check_id: C10
  name: just validate-causal-all
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.43005e4de2
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  summary: Executed 2026-10-14T15:56:33Z to 2026-10-14T15:56:36Z. validated 32 causal-graph
    curation file(s) with 32 graph(s)
- check_id: C11
  name: just validate-products
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.43005e4de2
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  summary: "Executed 2026-10-14T15:56:36Z to 2026-10-14T15:57:17Z. id↔label correspondence\
    \ summary:\n          OK_CANONICAL: 1176\n            OK_SYNONYM: 1\n        \
    \  OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2059\n\n✅ All id↔label pairs correspond."
- check_id: C13
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.43005e4de2
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_ontology_labels.py::test_foodon_refresh_changes_only_the_two_intended_records
  exit_code: 0
  summary: 'Executed 2026-10-14T16:01:25Z to 2026-10-14T16:01:31Z. .                                                                        [100%]

    1 passed in 4.56s'
- check_id: C14
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    scripts/render_pages.py
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.43005e4de2
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    scripts/render_pages.py --check
  exit_code: 0
  summary: 'Executed 2026-10-14T16:01:31Z to 2026-10-14T16:02:00Z. rendered 3208 habitat
    pages, 254 redirect stubs, 8 categories, 117 term requests -> /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmpu4nlmq9a/site

    pages/ is in step with the corpus'
- check_id: C15
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    scripts/build_term_requests.py
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.43005e4de2
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    scripts/build_term_requests.py --check
  exit_code: 0
  summary: Executed 2026-10-14T16:02:00Z to 2026-10-14T16:02:15Z. term-request table
    is current (109 terms)
- check_id: C16
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    scripts/check_docs.py
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.43005e4de2
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    scripts/check_docs.py --check
  exit_code: 0
  summary: Executed 2026-10-14T16:02:15Z to 2026-10-14T16:02:29Z. README corpus statistics
    are current
- check_id: C17
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    scripts/build_redirects.py
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.43005e4de2
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    scripts/build_redirects.py --check
  exit_code: 0
  summary: Executed 2026-10-14T16:02:29Z to 2026-10-14T16:04:04Z. RETIRED.tsv is current
    (254 redirects)
- check_id: C18
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.43005e4de2
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m ruff check .
  exit_code: 0
  summary: Executed 2026-10-14T16:04:04Z to 2026-10-14T16:04:04Z. All checks passed!
- check_id: C19
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.43005e4de2
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_ontology_labels.py tests/test_food_context_parent_repairs.py
  exit_code: 0
  summary: 'Executed 2026-10-14T16:28:09Z to 2026-10-14T16:28:18Z. .....................                                                    [100%]

    21 passed in 8.07s'
- check_id: C20
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.43005e4de2
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m ruff check .
  exit_code: 0
  summary: Executed 2026-10-14T16:28:18Z to 2026-10-14T16:28:18Z. All checks passed!
- check_id: QC
  name: Exact corrected-base authoritative QC
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.43005e4de2
  command: gh run view 38598374337 --repo CultureBotAI/HabitatMech --json databaseId,status,conclusion,headSha,url
  exit_code: 0
  evidence_ids:
  - QC
  summary: Verified success for the captured corrected commit; final archive checks
    are separate.
- check_id: ORIGINAL
  name: Original members
  status: unavailable
  required: false
  target_ids:
  - habitatmech:GOLD.43005e4de2
  evidence_ids:
  - MEMBERS
  - GOLD_ACCESS
  summary: Predecessor bounded search/access limitations remain; no original joins
    were recovered by this repair.
- check_id: IMODULON
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.43005e4de2
  summary: No transcriptomic mechanism asserted.
evidence:
- evidence_id: CURRENT
  kind: record_content
  reference: data/habitats/food/raw_meat.yaml
  summary: 'Complete corrected record and predecessor diff inspected. The exact immediate
    GOLD parent contribution is excluded through its maintained source-path/expected-parent
    guard. No replacement genus is invented; the empty optional parent list is omitted.
    Identity, source nodes/path, counts/units, native status and all other claims
    are preserved. Parent Meat products identity #2078 and child Meat trimming scope
    #2080 remain open; neither is repaired here.'
  accessed_at: '2026-10-14T16:40:47Z'
  support: supports
- evidence_id: OWNERS
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv; tests/test_food_context_parent_repairs.py;
    tests/test_ontology_labels.py
  summary: 'Five guarded rows and five append-only histories read. Counterfactual
    full-corpus test proves exactly five identifiers change, only parents and generated
    history. Two older pastry assertions required repair: optional-list indexing and
    an explicit obsolete production-parent expectation. Initial full QC38594694439
    exposed the second after the first focused check passed (1113passed,1failed,3skipped).
    Both are corrected, with the complete ontology-label module and counterfactual
    regression rerun. No scientific schema/generator relaxation.'
  accessed_at: '2026-10-14T16:40:47Z'
  support: supports
- evidence_id: PREVIOUS
  kind: prior_review
  reference: reviews/structured/20261014T155038Z-raw_meat/review.yaml
  summary: Entire predecessor retained unchanged; original rows/parent values are
    historical. All predecessor findings are reassessed explicitly.
  accessed_at: '2026-10-14T16:40:47Z'
  support: supports
- evidence_id: QC
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38598374337
  summary: Authoritative corrected-base QC passed on 249b157d73e8612bb0609a1764e7edd2712ee9bc.
    This predates these successor bundles; final archive/PR gates remain required.
  accessed_at: '2026-10-14T16:40:47Z'
  support: supports
- evidence_id: MAP
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38593642962
  summary: Pinned locked BGE/PaCMAP pipeline rebuilt five changed inputs, proved repeat
    reuse and all3208 full-pass reuse. Downloaded full inputs matched local fresh
    adapter bytes; map/cache/hash validation passed. No freshness bypass or fabricated
    coordinates.
  accessed_at: '2026-10-14T16:40:47Z'
  support: supports
- evidence_id: RULES
  kind: authority
  reference: docs/CURATION.md; docs/HARMONIZATION.md; src/habitatmech/schema/habitatmech.yaml
  summary: Previously inspected evidence, not a new retrieval or current-row annotation.
    Strictly broader parent_habitats, exact identity versus parent grounding, source-unit
    semantics, FOOD food/beverage matrix category and all-source ITEM gates applied.
  accessed_at: '2026-10-14T15:50:38Z'
  support: supports
- evidence_id: MEMBERS
  kind: search
  reference: conf/sources.yaml; data/raw/MANIFEST.yaml; data/raw/GOLD_MANIFEST.yaml
  summary: 'Previously inspected evidence, not a new retrieval or current-row annotation.
    Original GOLD_nodes.tsv, GOLD_edges.tsv, goldData.xlsx and gold_biosample_triads.tsv
    were not located among 41639 files in the repository and configured kg-microbe
    data root. Exact command: rg --no-ignore --hidden --files . /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data.
    Frozen inventories remain available. Counts are frozen aggregate assertions, not
    independently certified distinct specimens.'
  accessed_at: '2026-10-14T15:50:38Z'
  support: supports
  search_scope: Ignored and hidden files included within the named roots; no all-disks
    absence claim.
- evidence_id: GOLD_ACCESS
  kind: database
  reference: https://gold.jgi.doe.gov/
  summary: 'Previously inspected evidence, not a new retrieval or current-row annotation.
    Four exact study requests returned HTTP403. Eight schema-prefix-expanded ecosystem
    URL requests returned HTTP404; these browser routes may be unsupported and do
    not invalidate frozen IDs. No inaccessible page text was inferred. Exact receipt:
    {"Gs0145265": {"accessed_at": "2026-10-14T15:35:02.815165Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0145265"}, "Gs0153654":
    {"accessed_at": "2026-10-14T15:35:02.848735Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0153654"}, "Gs0154236": {"accessed_at":
    "2026-10-14T15:35:02.900438Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154236"},
    "Gs0154282": {"accessed_at": "2026-10-14T15:35:02.948589Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"}, "gold.ecosystem:5633":
    {"accessed_at": "2026-10-14T15:35:03.845098Z", "error": "HTTP Error 404: Not Found",
    "url": "https://gold.jgi.doe.gov/ecosystem/5633"}, "gold.ecosystem:5892": {"accessed_at":
    "2026-10-14T15:35:04.088840Z", "error": "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5892"},
    "gold.ecosystem:5939": {"accessed_at": "2026-10-14T15:35:03.359272Z", "error":
    "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5939"},
    "gold.ecosystem:5942": {"accessed_at": "2026-10-14T15:35:03.586048Z", "error":
    "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/5942"},
    "gold.ecosystem:6419": {"accessed_at": "2026-10-14T15:35:04.251825Z", "error":
    "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/6419"},
    "gold.ecosystem:6424": {"accessed_at": "2026-10-14T15:35:04.621271Z", "error":
    "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/6424"},
    "gold.ecosystem:6971": {"accessed_at": "2026-10-14T15:35:05.075424Z", "error":
    "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/6971"},
    "gold.ecosystem:7384": {"accessed_at": "2026-10-14T15:35:04.879190Z", "error":
    "HTTP Error 404: Not Found", "url": "https://gold.jgi.doe.gov/ecosystem/7384"}}'
  accessed_at: '2026-10-14T15:50:38Z'
  support: context_only
- evidence_id: FOODON
  kind: database
  reference: https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl
  summary: 'Previously inspected evidence, not a new retrieval or current-row annotation.
    Pinned full FoodOn class XML re-inspected at 2026-10-14T15:34:45.849036Z: definitions,
    synonyms, restrictions and parents, not just labels. FOODON:00001006 is mammalian
    meat food product. Its restriction is not established for the generic raw-meat
    source. Current children Beef chop and Meat trimming do not establish universal
    mammalian scope. Coordinate the exact expected-parent guard with open parent identity
    issue2078; do not silently change either child. Retrieved SHA256: b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf.'
  accessed_at: '2026-10-14T12:27:42.074174Z'
  support: supports
assessments:
- assessment_id: FIX
  area: grounding
  topic: Exact hierarchy correction
  outcome: supported
  target_ids:
  - habitatmech:GOLD.43005e4de2
  evidence_ids:
  - CURRENT
  - OWNERS
  - PREVIOUS
  - QC
  - MAP
  - RULES
  - MEMBERS
  - GOLD_ACCESS
  - FOODON
  summary: 'The exact immediate GOLD parent contribution is excluded through its maintained
    source-path/expected-parent guard. No replacement genus is invented; the empty
    optional parent list is omitted. Identity, source nodes/path, counts/units, native
    status and all other claims are preserved. Parent Meat products identity #2078
    and child Meat trimming scope #2080 remain open; neither is repaired here.'
- assessment_id: SOURCE
  area: provenance
  topic: Identity and source claims
  outcome: supported
  target_ids:
  - habitatmech:GOLD.43005e4de2
  evidence_ids:
  - CURRENT
  - OWNERS
  - PREVIOUS
  - QC
  - MAP
  - RULES
  - MEMBERS
  - GOLD_ACCESS
  - FOODON
  summary: Complete record re-read. Counts and units are preserved, not summed across
    organism/biosample snapshots. All optional fields and prior events remain unchanged;
    no taxon/parameter/causal assertion is introduced.
- assessment_id: CATEGORY
  area: scope
  topic: Independent category and status
  outcome: supported
  target_ids:
  - habitatmech:GOLD.43005e4de2
  evidence_ids:
  - CURRENT
  - OWNERS
  - PREVIOUS
  - QC
  - MAP
  - RULES
  - MEMBERS
  - GOLD_ACCESS
  - FOODON
  summary: Existing category and ITEM/CLASS-derived native status are preserved; this
    review does not promote them.
- assessment_id: LIMITS
  area: evidence
  topic: Original source scope
  outcome: unknown
  target_ids:
  - habitatmech:GOLD.43005e4de2
  evidence_ids:
  - CURRENT
  - OWNERS
  - PREVIOUS
  - QC
  - MAP
  - RULES
  - MEMBERS
  - GOLD_ACCESS
  - FOODON
  summary: Unavailable original member joins remain a limitation. Source labels and
    current examples do not establish every historical member or exact ontology identity.
    No neighboring-record closure or SSSOM/KGX readiness is implied.
findings:
- finding_id: F1
  issue_key: raw-meat-mammalian-parent
  title: Generic raw meat inherits an unsupported mammalian restriction
  description: FOODON:00001006 is mammalian meat food product. Its restriction is
    not established for the generic raw-meat source. Current children Beef chop and
    Meat trimming do not establish universal mammalian scope. Coordinate the exact
    expected-parent guard with open parent identity issue2078; do not silently change
    either child.
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  target_ids:
  - habitatmech:GOLD.43005e4de2
  field_paths:
  - parent_habitats
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input; regenerate habitat YAML
  evidence_ids:
  - CURRENT
  - OWNERS
  - PREVIOUS
  - QC
  - MAP
  - RULES
  - MEMBERS
  - GOLD_ACCESS
  - FOODON
  rule_id: Strict genus, habitat category and explicit mapping endpoints
  native_severity: major
  normalization_reason: Materially unsupported genus or incompatible source mapping
    contract.
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261014T155038Z-raw_meat
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2088
  disposition_reason: 'Scoped hierarchy correction verified. The exact immediate GOLD
    parent contribution is excluded through its maintained source-path/expected-parent
    guard. No replacement genus is invented; the empty optional parent list is omitted.
    Identity, source nodes/path, counts/units, native status and all other claims
    are preserved. Parent Meat products identity #2078 and child Meat trimming scope
    #2080 remain open; neither is repaired here.'
actions: []
limitations:
- Same-agent review, not independent approval.
- Original joins remain unavailable; no exact source-member reconstruction.
- Initial site check correctly failed on the stale semantic map; the governed rebuild
  and subsequent site checks passed.
- 'Pit-mud category #2086 and shared endpoint #1398 remain open. Neighboring source-identity
  issues are not closed by these repairs.'
- Corrected-base QC predates these successors; final immutable archive and PR checks
  remain required.
- No whole-corpus scientific pass, ontology refresh or SSSOM/KGX certification.
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261014T155038Z-raw_meat
  relationship: Exact predecessor findings reassessed without rewriting history.
tags:
- habitatmech
- record-review
- food
- followup
```
