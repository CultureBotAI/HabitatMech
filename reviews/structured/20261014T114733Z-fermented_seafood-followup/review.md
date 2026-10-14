# Scientific follow-up: Fermented seafood

- Review: 20261014T114733Z-fermented_seafood-followup
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T11:28:16.250939Z
- Finished UTC: 2026-10-14T11:47:33.173582Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact GOLD source-parent contribution is excluded, preserving independent genera, native identity/status and all source IDs, labels, paths, counts and units. No further actionable defect is established in the predecessor scope; source-member limits remain.

## Scope And Provenance

Entire corrected record and exact predecessor findings.

Selection: Explicit correction follow-up, exactly one resolved target; not sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4f280743a3e532cfa8172c433c4de809f7031da3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.4f8bcf2e70 | data/habitats/food/fermented_seafood.yaml | generated | Fermented seafood |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate | passed | True | habitatmech:GOLD.4f8bcf2e70 | Executed 2026-10-14T11:28:16.313560Z to 2026-10-14T11:28:18.878403Z. No issues found |
| just validate-strict | passed | True | habitatmech:GOLD.4f8bcf2e70 | Executed 2026-10-14T11:28:21.336177Z to 2026-10-14T11:28:26.139612Z. uv run python scripts/validate_strict.py data/habitats/food/fermentation_cellar.yaml data/habitats/food/fermentation_starter.yaml data/habitats/food/fermented_food.yaml data/habitats/food/fermented_meat_product.yaml data/habitats/food/fermented_seafood.yaml data/habitats/food/fermented_vegetables.yaml<br>Validating 6 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      6<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.4f8bcf2e70 | Executed 2026-10-14T11:28:26.140234Z to 2026-10-14T11:28:33.740230Z. No issues found<br>666 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | habitatmech:GOLD.4f8bcf2e70 | Executed 2026-10-14T11:28:33.740828Z to 2026-10-14T11:28:34.267083Z. provenance current: 14 committed inventories, 2 GOLD sources |
| just verify-corpus | passed | True | habitatmech:GOLD.4f8bcf2e70 | Executed 2026-10-14T11:28:34.267715Z to 2026-10-14T11:28:48.617510Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| just validate-causal-all | passed | True | habitatmech:GOLD.4f8bcf2e70 | Executed 2026-10-14T11:28:48.618047Z to 2026-10-14T11:28:52.682048Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| just term-requests-check | passed | True | habitatmech:GOLD.4f8bcf2e70 | Executed 2026-10-14T11:28:52.682573Z to 2026-10-14T11:29:08.022018Z. term-request table is current (109 terms) |
| just validate-products | passed | True | habitatmech:GOLD.4f8bcf2e70 | Executed 2026-10-14T11:29:08.022734Z to 2026-10-14T11:29:50.577365Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1176<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2059<br><br>✅ All id↔label pairs correspond. |
| uv run | passed | True | habitatmech:GOLD.4f8bcf2e70 | Executed 2026-10-14T11:29:50.578083Z to 2026-10-14T11:31:52.320775Z. ........................................................................ [ 61%]<br>.............................................                            [100%]<br>117 passed in 120.72s (0:02:00) |
| uv run | passed | True | habitatmech:GOLD.4f8bcf2e70 | Executed 2026-10-14T11:31:52.321572Z to 2026-10-14T11:31:52.598811Z. All checks passed! |
| Exact corrected-base hosted QC | passed | True | habitatmech:GOLD.4f8bcf2e70 | Verified success on exact corrected base; new reports require final archive/PR checks. |
| Original source member reconstruction | unavailable | False | habitatmech:GOLD.4f8bcf2e70 | No recovered original dumps or member crosswalks. Predecessor GOLD study requests returned 403; no new access success is claimed. |
| Expression-source applicability | not_applicable | False | habitatmech:GOLD.4f8bcf2e70 | No gene, regulator, protein or transcriptomics claim is introduced. |

## Scientific And Domain Assessments

### Scoped fixes and finding dispositions

grounding: supported. Targets: habitatmech:GOLD.4f8bcf2e70.

The exact GOLD source-parent contribution is excluded, preserving independent genera, native identity/status and all source IDs, labels, paths, counts and units. No further actionable defect is established in the predecessor scope; source-member limits remain.

### Source scope, observations and native status

evidence: supported. Targets: habitatmech:GOLD.4f8bcf2e70.

Re-read every field of the corrected record. Source occurrence, strain, bulk-sample and triad denominators remain separate. No environmental parameter, mechanism, citation, discussion or dataset claim is invented. No taxon association is asserted. Hierarchy and annotation repair do not promote native status. Neighbors remain unchanged.

### Evidence and source identity limits

completeness: unknown. Targets: habitatmech:GOLD.4f8bcf2e70.

Original source members remain unavailable. This qualified pass does not establish complete curation, exact original membership, new ontology mappings or a whole-corpus scientific pass.

## Findings

### F1: Production process is asserted as a strict habitat parent

major / resolved / confirmed; issue key: fermented-seafood-food-production-process-parent.

Immediate GOLD path contribution FOODON:03530206 is a planned production process in both the frozen definition and inspected full FoodOn. The target denotes a site or food/inoculum material, not a kind of that process. Source hierarchy placement does not establish subclass identity.

Disposition: Confirmed the exact correction in maintained inputs, fully regenerated record and counterfactual preservation checks. The exact GOLD source-parent contribution is excluded, preserving independent genera, native identity/status and all source IDs, labels, paths, counts and units. No further actionable defect is established in the predecessor scope; source-member limits remain.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| CURRENT | data/habitats/food/fermented_seafood.yaml; Entire current YAML and exact predecessor diff | supports | The exact GOLD source-parent contribution is excluded, preserving independent genera, native identity/status and all source IDs, labels, paths, counts and units. No further actionable defect is established in the predecessor scope; source-member limits remain. |
| OWNERS | curation/gold_parent_exclusions.tsv; curation/record_annotation_corrections.tsv; curation/gold_parent_exclusions.tsv:6 habitatmech:GOLD.4f8bcf2e70 | supports | Read exact maintained rows and seven append-only session histories. Source mints and expected parents are guarded. The annotation table validates record/source/old value and rejects stale, conflicting, duplicate or malformed rows before mutation. Raw inventories and manifests are unchanged; no ontology lexical index refresh is claimed. |
| REGRESSION | tests/test_fermented_food_review_fixes.py; tests/test_record_annotation_corrections.py; tests/test_curation_floor.py | supports | Counterfactual full-corpus build changes exactly six records. Five change only parent/history; starter changes parent, two annotations and history. Identity, source attestations and native status are byte-semantically preserved; starter taxon metrics/ranks remain exact. The expected old value, origin, malformed/duplicate/conflicting/stale cases, no partial mutation, deterministic history and correction-ID loss are covered. |
| PREVIOUS | reviews/structured/20261014T111526Z-fermented_seafood/review.yaml | context_only | Inspected immutable predecessor and its complete source/evidence assessment. Baseline curation-row numbers and old parent/annotation values are historical, not current locators. |
| QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38557567712 | supports | Verified full authoritative hosted QC success on exact corrected base 4f280743a3e532cfa8172c433c4de809f7031da3. Scientific input hashes were unchanged between initial corrected inspection and final map/site publication. New follow-up reports still require post-save archive and final PR checks. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md | supports | Retained inspected predecessor evidence, not a fresh retrieval or statement of corrected values. Applied the local field-by-field checklist: source identity, strict genus, source-unit preservation, MIxS roles, observational taxa, optional fields and all-source ITEM status gates. |
| FOODON | https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl; Relevant target/parent and candidate classes | supports | Retained inspected predecessor evidence, not a fresh retrieval or statement of corrected values. Inspected the official pinned RDF/XML definitions, active classes, named subclass parents and restriction axioms. SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf. The native seafood food-material identity is retained, but its sole FOODON:03530206 parent denotes a process rather than a material genus. Full FoodOn offers FOODON:00001054 fermented fish or seafood food product, whose sea-water-fish parent makes its scope unsuitable for unexamined exact equivalence with generic seafood. Fish, seafood, saline origin and shellfish coverage must not be conflated by label alone. |
| ENVO | https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl; ENVO:03600039; ENVO:03600040; ENVO:00003074 | supports | Retained inspected predecessor evidence, not a fresh retrieval or statement of corrected values. Current source revision a2455d1a77e46bb8a664d65a157166b539269042. ENVO:03600040 is a manufactured fermentation inoculum, directly under ENVO:00003074, and explicitly carries hasExactSynonym Daqu. ENVO:03600039 is a pit for alcoholic-spirit fermentation. SHA256 a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c |
| AVAILABILITY | conf/sources.yaml | context_only | Retained inspected predecessor evidence, not a fresh retrieval or statement of corrected values. {"accessed_at": "2026-10-14T11:04:45.077996Z", "command": ["rg", "--no-ignore", "--hidden", "--files", ".", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"], "enumerated_files": 41210, "exit_code": 0, "interpretation": "Ignored files included. Bounded to this repository and configured kg-microbe data root, not all disks. Inventories do not reconstruct original member joins.", "matches": []} |
| GOLD_ACCESS | https://gold.jgi.doe.gov/ | context_only | Retained inspected predecessor evidence, not a fresh retrieval or statement of corrected values. All eighteen exact study URLs selected from own-path rows returned HTTP 403. No page contents or original members are inferred. {"Gs0046755": {"accessed_at": "2026-10-14T11:04:49.272093Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0046755"}, "Gs0111426": {"accessed_at": "2026-10-14T11:04:49.628075Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0111426"}, "Gs0117939": {"accessed_at": "2026-10-14T11:04:50.123488Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0117939"}, "Gs0118005": {"accessed_at": "2026-10-14T11:04:50.166468Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0118005"}, "Gs0141280": {"accessed_at": "2026-10-14T11:04:50.206535Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0141280"}, "Gs0150381": {"accessed_at": "2026-10-14T11:04:50.243863Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150381"}, "Gs0150400": {"accessed_at": "2026-10-14T11:04:50.277291Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150400"}, "Gs0150497": {"accessed_at": "2026-10-14T11:04:50.316461Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150497"}, "Gs0150709": {"accessed_at": "2026-10-14T11:04:50.348666Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150709"}, "Gs0150730": {"accessed_at": "2026-10-14T11:04:50.387801Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150730"}, "Gs0150741": {"accessed_at": "2026-10-14T11:04:50.520416Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150741"}, "Gs0153794": {"accessed_at": "2026-10-14T11:04:50.670480Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153794"}, "Gs0154231": {"accessed_at": "2026-10-14T11:04:50.709174Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154231"}, "Gs0154264": {"accessed_at": "2026-10-14T11:04:50.759857Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154264"}, "Gs0154282": {"accessed_at": "2026-10-14T11:04:50.803554Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"}, "Gs0154636": {"accessed_at": "2026-10-14T11:04:50.849346Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154636"}, "Gs0156793": {"accessed_at": "2026-10-14T11:04:50.892628Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0156793"}, "Gs0159152": {"accessed_at": "2026-10-14T11:04:50.949426Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0159152"}} |

## Limits And Additional Notes

- Same-agent review, not independent approval.
- Original source members remain unavailable; separate fermented-meat exact-source issue #2061 remains open.
- No global ontology refresh or SSSOM/KGX conformance certification. Label validation retains configured exceptions and unsupported-prefix skips.
- Only the exact predecessor findings receive these dispositions; no neighboring record is silently curated.
- The synonym correction is a reviewed output-level disagreement with upstream ENVO, not a change to its raw lexical index. Current source labels do not ground through Daqu.
- Corrected-base QC predates these reports; post-save archive and final publication gates remain required.
- Initial corrected capture at cec2394f25502176882c7fa44f3117ea55cc5ae5; final reinspection proves every captured scientific input hash unchanged after map/site publication.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T114733Z-fermented_seafood-followup
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific follow-up: Fermented seafood'
started_at: '2026-10-14T11:28:16.250939Z'
finished_at: '2026-10-14T11:47:33.173582Z'
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
verdict: pass_with_limitations
summary: The exact GOLD source-parent contribution is excluded, preserving independent
  genera, native identity/status and all source IDs, labels, paths, counts and units.
  No further actionable defect is established in the predecessor scope; source-member
  limits remain.
source:
  git_revision: 4f280743a3e532cfa8172c433c4de809f7031da3
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
  - path: data/habitats/food/fermentation_cellar.yaml
    sha256: ddf0dc98e3046a94be1963662b6226c555ce41cc555cbf8b2fcd17682c9aa2df
    role: context
  - path: data/habitats/food/fermentation_starter.yaml
    sha256: 7233bb5a0fdbe4e6e70fac3941d3eb1bb70cb7555658dd95f39e3c1cc1116ef7
    role: context
  - path: data/habitats/food/fermented_dairy_products.yaml
    sha256: 9ed59912b37facdd56bb980f312ad3f131d13a6a604f8294574f94477e889ae4
    role: context
  - path: data/habitats/food/fermented_fish.yaml
    sha256: 89ff9b5d561742c28425cc8bed2cc18e7a07f7016e3276cc7b77d9dcd3c25ddb
    role: context
  - path: data/habitats/food/fermented_food.yaml
    sha256: 7eee668ff9ba018c8a8d8ea6832f18ec8e3efbbd09ead7f850c9f77c115666ef
    role: context
  - path: data/habitats/food/fermented_meat_product.yaml
    sha256: 5da67dcf566c8ffdd1083792ddeb7a1dac517c5ec08c1dc3cceeef60df7d4697
    role: context
  - path: data/habitats/food/fermented_seafood.yaml
    sha256: e30a66ee7d5a7fd6d971df246dc11826a753be4f6584e1991478389a021659f2
    role: target
  - path: data/habitats/food/fermented_vegetables.yaml
    sha256: cbb5ef98ac42fb5a85918b459d5a2788cef0ee0ee42979107ef157f327ff2143
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
  - path: history/mappings/fermentation_cellar/2026-10-14T112503Z-codex-gpt-5-7f8b67.yaml
    sha256: 7fd86414bbe4d0f3f27a6cf99ff21979f1fe3fd2db70e0133d125eb3ddeaaca5
    role: context
  - path: history/mappings/fermentation_starter/2026-10-14T112506Z-codex-gpt-5-9b5a0a.yaml
    sha256: a75727074c4829042836ef26d54c57cb8181f06b24656f8d40889f44887b8c45
    role: context
  - path: history/mappings/fermentation_starter/2026-10-14T112517Z-codex-gpt-5-07fb1b.yaml
    sha256: 0f49e8c62f47d7f661a60d4365424a8cdc147cf3c7e17e3b17de60b1fa67e248
    role: context
  - path: history/mappings/fermented_food/2026-10-14T112508Z-codex-gpt-5-146d1d.yaml
    sha256: 9ebf9d990e532b6cb2d4e4c91c7d9554bbe4330c97befc930bee6970a886ab7a
    role: context
  - path: history/mappings/fermented_meat_product/2026-10-14T112511Z-codex-gpt-5-bb8f29.yaml
    sha256: 0f68cc4ef174136e1e1529a51dfcbc81d842fa7feeb37c95bdc13c445ad6e85d
    role: context
  - path: history/mappings/fermented_seafood/2026-10-14T112513Z-codex-gpt-5-b9ba07.yaml
    sha256: e09680423d2a22ecd9d547e8ede4084858582451b47851fb117b598642390e1f
    role: context
  - path: history/mappings/fermented_vegetables/2026-10-14T112515Z-codex-gpt-5-d965f7.yaml
    sha256: 2b18d36f94ea15334bb1d1ebd3cfcf02448098ff4a4491d04553f36a875839d6
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
  - path: reviews/structured/20261014T111526Z-fermented_seafood/review.yaml
    sha256: 6699615723530e2ceecd4b5a281b03c704b4c8a403fe9dd716dda48230e07625
    role: context
  - path: scripts/aggregate_gold_triads.py
    sha256: 0e25179dbecd7c73cbedd99a0ae44e56e4992afb9e1ec02d2411439f643b8e54
    role: context
  - path: scripts/check_curation_floor.py
    sha256: 54bf01c1d101e66f27a50eccacb54ddb8f7856694ed2ad16dde54981c996b973
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
  - path: tests/test_curation_floor.py
    sha256: a07e4b4282ffd482e2b2bbf637e6e57f0fd727aaadea8f0c3b296454e43d7840
    role: context
  - path: tests/test_fermented_food_review_fixes.py
    sha256: 43fb2b3dde440904b6691f9d80610fb886024d40d20534edf9da886de23aa58b
    role: context
  - path: tests/test_record_annotation_corrections.py
    sha256: af02b2a45e608f8dd816bcb9b659490385fbf3d78405e188342be56433f18425
    role: context
targets:
- target_id: habitatmech:GOLD.4f8bcf2e70
  path: data/habitats/food/fermented_seafood.yaml
  label: Fermented seafood
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
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Guarded imported annotation corrections
scope:
  description: Entire corrected record and exact predecessor findings.
  selection: Explicit correction follow-up, exactly one resolved target; not sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.4f8bcf2e70
evidence:
- evidence_id: CURRENT
  kind: record_content
  reference: data/habitats/food/fermented_seafood.yaml
  locator: Entire current YAML and exact predecessor diff
  accessed_at: '2026-10-14T11:47:33.168941Z'
  support: supports
  summary: The exact GOLD source-parent contribution is excluded, preserving independent
    genera, native identity/status and all source IDs, labels, paths, counts and units.
    No further actionable defect is established in the predecessor scope; source-member
    limits remain.
- evidence_id: OWNERS
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv; curation/record_annotation_corrections.tsv
  accessed_at: '2026-10-14T11:47:33.168941Z'
  support: supports
  summary: Read exact maintained rows and seven append-only session histories. Source
    mints and expected parents are guarded. The annotation table validates record/source/old
    value and rejects stale, conflicting, duplicate or malformed rows before mutation.
    Raw inventories and manifests are unchanged; no ontology lexical index refresh
    is claimed.
  locator: curation/gold_parent_exclusions.tsv:6 habitatmech:GOLD.4f8bcf2e70
- evidence_id: REGRESSION
  kind: validation
  reference: tests/test_fermented_food_review_fixes.py; tests/test_record_annotation_corrections.py;
    tests/test_curation_floor.py
  accessed_at: '2026-10-14T11:47:33.168941Z'
  support: supports
  summary: Counterfactual full-corpus build changes exactly six records. Five change
    only parent/history; starter changes parent, two annotations and history. Identity,
    source attestations and native status are byte-semantically preserved; starter
    taxon metrics/ranks remain exact. The expected old value, origin, malformed/duplicate/conflicting/stale
    cases, no partial mutation, deterministic history and correction-ID loss are covered.
- evidence_id: PREVIOUS
  kind: prior_review
  reference: reviews/structured/20261014T111526Z-fermented_seafood/review.yaml
  accessed_at: '2026-10-14T11:47:33.168941Z'
  support: context_only
  summary: Inspected immutable predecessor and its complete source/evidence assessment.
    Baseline curation-row numbers and old parent/annotation values are historical,
    not current locators.
- evidence_id: QC
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38557567712
  accessed_at: '2026-10-14T11:47:33.168941Z'
  support: supports
  summary: Verified full authoritative hosted QC success on exact corrected base 4f280743a3e532cfa8172c433c4de809f7031da3.
    Scientific input hashes were unchanged between initial corrected inspection and
    final map/site publication. New follow-up reports still require post-save archive
    and final PR checks.
- evidence_id: RULES
  kind: authority
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md
  summary: 'Retained inspected predecessor evidence, not a fresh retrieval or statement
    of corrected values. Applied the local field-by-field checklist: source identity,
    strict genus, source-unit preservation, MIxS roles, observational taxa, optional
    fields and all-source ITEM status gates.'
  accessed_at: '2026-10-14T11:15:26.881330Z'
  support: supports
- evidence_id: FOODON
  kind: database
  reference: https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl
  summary: Retained inspected predecessor evidence, not a fresh retrieval or statement
    of corrected values. Inspected the official pinned RDF/XML definitions, active
    classes, named subclass parents and restriction axioms. SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf.
    The native seafood food-material identity is retained, but its sole FOODON:03530206
    parent denotes a process rather than a material genus. Full FoodOn offers FOODON:00001054
    fermented fish or seafood food product, whose sea-water-fish parent makes its
    scope unsuitable for unexamined exact equivalence with generic seafood. Fish,
    seafood, saline origin and shellfish coverage must not be conflated by label alone.
  accessed_at: '2026-10-14T11:07:25.661747Z'
  support: supports
  locator: Relevant target/parent and candidate classes
- evidence_id: ENVO
  kind: database
  reference: https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl
  summary: Retained inspected predecessor evidence, not a fresh retrieval or statement
    of corrected values. Current source revision a2455d1a77e46bb8a664d65a157166b539269042.
    ENVO:03600040 is a manufactured fermentation inoculum, directly under ENVO:00003074,
    and explicitly carries hasExactSynonym Daqu. ENVO:03600039 is a pit for alcoholic-spirit
    fermentation. SHA256 a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c
  accessed_at: '2026-10-14T11:07:29.497224Z'
  support: supports
  locator: ENVO:03600039; ENVO:03600040; ENVO:00003074
- evidence_id: AVAILABILITY
  kind: search
  reference: conf/sources.yaml
  summary: 'Retained inspected predecessor evidence, not a fresh retrieval or statement
    of corrected values. {"accessed_at": "2026-10-14T11:04:45.077996Z", "command":
    ["rg", "--no-ignore", "--hidden", "--files", ".", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"],
    "enumerated_files": 41210, "exit_code": 0, "interpretation": "Ignored files included.
    Bounded to this repository and configured kg-microbe data root, not all disks.
    Inventories do not reconstruct original member joins.", "matches": []}'
  accessed_at: '2026-10-14T11:15:26.881330Z'
  support: context_only
  search_scope: Ignored-inclusive file enumeration of this repository and configured
    kg-microbe data directory only, matching original GOLD/BacDive dump filenames;
    not a search of all disks or remote datasets.
- evidence_id: GOLD_ACCESS
  kind: database
  reference: https://gold.jgi.doe.gov/
  summary: 'Retained inspected predecessor evidence, not a fresh retrieval or statement
    of corrected values. All eighteen exact study URLs selected from own-path rows
    returned HTTP 403. No page contents or original members are inferred. {"Gs0046755":
    {"accessed_at": "2026-10-14T11:04:49.272093Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0046755"}, "Gs0111426": {"accessed_at":
    "2026-10-14T11:04:49.628075Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0111426"},
    "Gs0117939": {"accessed_at": "2026-10-14T11:04:50.123488Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0117939"}, "Gs0118005":
    {"accessed_at": "2026-10-14T11:04:50.166468Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0118005"}, "Gs0141280": {"accessed_at":
    "2026-10-14T11:04:50.206535Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0141280"},
    "Gs0150381": {"accessed_at": "2026-10-14T11:04:50.243863Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150381"}, "Gs0150400":
    {"accessed_at": "2026-10-14T11:04:50.277291Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0150400"}, "Gs0150497": {"accessed_at":
    "2026-10-14T11:04:50.316461Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150497"},
    "Gs0150709": {"accessed_at": "2026-10-14T11:04:50.348666Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150709"}, "Gs0150730":
    {"accessed_at": "2026-10-14T11:04:50.387801Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0150730"}, "Gs0150741": {"accessed_at":
    "2026-10-14T11:04:50.520416Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150741"},
    "Gs0153794": {"accessed_at": "2026-10-14T11:04:50.670480Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153794"}, "Gs0154231":
    {"accessed_at": "2026-10-14T11:04:50.709174Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0154231"}, "Gs0154264": {"accessed_at":
    "2026-10-14T11:04:50.759857Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154264"},
    "Gs0154282": {"accessed_at": "2026-10-14T11:04:50.803554Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"}, "Gs0154636":
    {"accessed_at": "2026-10-14T11:04:50.849346Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0154636"}, "Gs0156793": {"accessed_at":
    "2026-10-14T11:04:50.892628Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0156793"},
    "Gs0159152": {"accessed_at": "2026-10-14T11:04:50.949426Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0159152"}}'
  accessed_at: '2026-10-14T11:15:26.881330Z'
  support: context_only
checks:
- check_id: C4
  name: just validate
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.4f8bcf2e70
  exit_code: 0
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/food/fermented_seafood.yaml
  summary: Executed 2026-10-14T11:28:16.313560Z to 2026-10-14T11:28:18.878403Z. No
    issues found
- check_id: C6
  name: just validate-strict
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.4f8bcf2e70
  exit_code: 0
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/food/fermentation_cellar.yaml data/habitats/food/fermentation_starter.yaml
    data/habitats/food/fermented_food.yaml data/habitats/food/fermented_meat_product.yaml
    data/habitats/food/fermented_seafood.yaml data/habitats/food/fermented_vegetables.yaml
  summary: "Executed 2026-10-14T11:28:21.336177Z to 2026-10-14T11:28:26.139612Z. uv\
    \ run python scripts/validate_strict.py data/habitats/food/fermentation_cellar.yaml\
    \ data/habitats/food/fermentation_starter.yaml data/habitats/food/fermented_food.yaml\
    \ data/habitats/food/fermented_meat_product.yaml data/habitats/food/fermented_seafood.yaml\
    \ data/habitats/food/fermented_vegetables.yaml\nValidating 6 files with 15 workers;\
    \ schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      6\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
- check_id: C7
  name: just validate-history
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.4f8bcf2e70
  exit_code: 0
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  summary: 'Executed 2026-10-14T11:28:26.140234Z to 2026-10-14T11:28:33.740230Z. No
    issues found

    666 history record(s) valid against src/habitatmech/schema/history.yaml'
- check_id: C8
  name: just provenance-check
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.4f8bcf2e70
  exit_code: 0
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  summary: 'Executed 2026-10-14T11:28:33.740828Z to 2026-10-14T11:28:34.267083Z. provenance
    current: 14 committed inventories, 2 GOLD sources'
- check_id: C9
  name: just verify-corpus
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.4f8bcf2e70
  exit_code: 0
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  summary: "Executed 2026-10-14T11:28:34.267715Z to 2026-10-14T11:28:48.617510Z. expected\
    \ 3208 records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing:\
    \ 0\n\ncorpus reproduces exactly from data/raw/"
- check_id: C10
  name: just validate-causal-all
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.4f8bcf2e70
  exit_code: 0
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  summary: Executed 2026-10-14T11:28:48.618047Z to 2026-10-14T11:28:52.682048Z. validated
    32 causal-graph curation file(s) with 32 graph(s)
- check_id: C11
  name: just term-requests-check
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.4f8bcf2e70
  exit_code: 0
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  summary: Executed 2026-10-14T11:28:52.682573Z to 2026-10-14T11:29:08.022018Z. term-request
    table is current (109 terms)
- check_id: C12
  name: just validate-products
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.4f8bcf2e70
  exit_code: 0
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  summary: "Executed 2026-10-14T11:29:08.022734Z to 2026-10-14T11:29:50.577365Z. id↔label\
    \ correspondence summary:\n          OK_CANONICAL: 1176\n            OK_SYNONYM:\
    \ 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2059\n\n✅ All id↔label\
    \ pairs correspond."
- check_id: C13
  name: uv run
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.4f8bcf2e70
  exit_code: 0
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache uv run pytest -q tests/test_record_annotation_corrections.py
    tests/test_fermented_food_review_fixes.py tests/test_curation_floor.py tests/test_gold_parent_exclusions.py
    tests/test_ontology_labels.py
  summary: 'Executed 2026-10-14T11:29:50.578083Z to 2026-10-14T11:31:52.320775Z. ........................................................................
    [ 61%]

    .............................................                            [100%]

    117 passed in 120.72s (0:02:00)'
- check_id: C14
  name: uv run
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.4f8bcf2e70
  exit_code: 0
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache uv run ruff check .
  summary: Executed 2026-10-14T11:31:52.321572Z to 2026-10-14T11:31:52.598811Z. All
    checks passed!
- check_id: QC
  name: Exact corrected-base hosted QC
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.4f8bcf2e70
  command: gh run view 38557567712 --json headSha,status,conclusion,url
  exit_code: 0
  summary: Verified success on exact corrected base; new reports require final archive/PR
    checks.
  evidence_ids:
  - QC
- check_id: MEMBERS
  name: Original source member reconstruction
  status: unavailable
  required: false
  target_ids:
  - habitatmech:GOLD.4f8bcf2e70
  summary: No recovered original dumps or member crosswalks. Predecessor GOLD study
    requests returned 403; no new access success is claimed.
  evidence_ids:
  - AVAILABILITY
  - GOLD_ACCESS
- check_id: IMODULON
  name: Expression-source applicability
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.4f8bcf2e70
  summary: No gene, regulator, protein or transcriptomics claim is introduced.
assessments:
- assessment_id: FIX
  area: grounding
  topic: Scoped fixes and finding dispositions
  outcome: supported
  target_ids:
  - habitatmech:GOLD.4f8bcf2e70
  evidence_ids:
  - CURRENT
  - OWNERS
  - REGRESSION
  - PREVIOUS
  - QC
  summary: The exact GOLD source-parent contribution is excluded, preserving independent
    genera, native identity/status and all source IDs, labels, paths, counts and units.
    No further actionable defect is established in the predecessor scope; source-member
    limits remain.
- assessment_id: SCIENCE
  area: evidence
  topic: Source scope, observations and native status
  outcome: supported
  target_ids:
  - habitatmech:GOLD.4f8bcf2e70
  evidence_ids:
  - CURRENT
  - PREVIOUS
  - REGRESSION
  - RULES
  summary: Re-read every field of the corrected record. Source occurrence, strain,
    bulk-sample and triad denominators remain separate. No environmental parameter,
    mechanism, citation, discussion or dataset claim is invented. No taxon association
    is asserted. Hierarchy and annotation repair do not promote native status. Neighbors
    remain unchanged.
- assessment_id: LIMITS
  area: completeness
  topic: Evidence and source identity limits
  outcome: unknown
  target_ids:
  - habitatmech:GOLD.4f8bcf2e70
  evidence_ids:
  - PREVIOUS
  - AVAILABILITY
  - GOLD_ACCESS
  - FOODON
  summary: Original source members remain unavailable. This qualified pass does not
    establish complete curation, exact original membership, new ontology mappings
    or a whole-corpus scientific pass.
findings:
- finding_id: F1
  issue_key: fermented-seafood-food-production-process-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Production process is asserted as a strict habitat parent
  description: Immediate GOLD path contribution FOODON:03530206 is a planned production
    process in both the frozen definition and inspected full FoodOn. The target denotes
    a site or food/inoculum material, not a kind of that process. Source hierarchy
    placement does not establish subclass identity.
  target_ids:
  - habitatmech:GOLD.4f8bcf2e70
  field_paths:
  - parent_habitats
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained owner; generated record is read-only
  evidence_ids:
  - CURRENT
  - OWNERS
  - REGRESSION
  - PREVIOUS
  - RULES
  - FOODON
  - QC
  rule_id: 'docs/CURATION.md and native review checklist: exact identity, strict genus
    and taxon-label scope'
  native_severity: major
  normalization_reason: A materially unsupported identity, lexical equivalence or
    strict genus is a major semantic finding.
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261014T111526Z-fermented_seafood
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2062
  disposition_reason: Confirmed the exact correction in maintained inputs, fully regenerated
    record and counterfactual preservation checks. The exact GOLD source-parent contribution
    is excluded, preserving independent genera, native identity/status and all source
    IDs, labels, paths, counts and units. No further actionable defect is established
    in the predecessor scope; source-member limits remain.
actions: []
limitations:
- Same-agent review, not independent approval.
- 'Original source members remain unavailable; separate fermented-meat exact-source
  issue #2061 remains open.'
- No global ontology refresh or SSSOM/KGX conformance certification. Label validation
  retains configured exceptions and unsupported-prefix skips.
- Only the exact predecessor findings receive these dispositions; no neighboring record
  is silently curated.
- The synonym correction is a reviewed output-level disagreement with upstream ENVO,
  not a change to its raw lexical index. Current source labels do not ground through
  Daqu.
- Corrected-base QC predates these reports; post-save archive and final publication
  gates remain required.
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261014T111526Z-fermented_seafood
  relationship: Exact predecessor findings reassessed without changing immutable reports.
notes:
- Initial corrected capture at cec2394f25502176882c7fa44f3117ea55cc5ae5; final reinspection
  proves every captured scientific input hash unchanged after map/site publication.
tags:
- habitatmech
- record-review
- food
- followup
```
