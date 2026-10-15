# Remediation review: air sac

- Review: 20261015T013700Z-air_sac-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T01:32:16Z
- Finished UTC: 2026-10-15T01:37:00Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact GOLD respiratory-system container contribution is excluded while UBERON:0010000 remains the avian air-sac genus. Only the ontology-related psotcranial air sac alias changes to RELATED_SYNONYM; its spelling and both independently exact aliases are retained. Identity, original source nodes/path, zero-count omission and EXACT/REVIEWED status are unchanged.

## Scope And Provenance

Focused scientific reassessment of the complete current record and exact prior findings after maintained-input remediation.

Selection: Exact successor to 20261015T005253Z-air_sac-record
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 81f9c9ead99cc14954df0c59bf752ed7284dd4b3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| UBERON:0009060 | data/habitats/host_associated/air_sac.yaml | generated | air sac |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | UBERON:0009060 | Executed 2026-10-15T01:16:17Z to 2026-10-15T01:16:23Z. No issues found |
| Native validate-strict | passed | True | UBERON:0009060 | Executed 2026-10-15T01:16:49Z to 2026-10-15T01:17:00Z. files scanned:      6<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| Native validate-history | passed | True | UBERON:0009060 | Executed 2026-10-15T01:17:00Z to 2026-10-15T01:17:19Z. No issues found<br>725 history record(s) valid against src/habitatmech/schema/history.yaml |
| Native provenance-check | passed | True | UBERON:0009060 | Executed 2026-10-15T01:17:19Z to 2026-10-15T01:17:20Z. provenance current: 14 committed inventories, 2 GOLD sources |
| Native verify-corpus | passed | True | UBERON:0009060 | Executed 2026-10-15T01:17:20Z to 2026-10-15T01:18:03Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| Native validate-causal-all | passed | True | UBERON:0009060 | Executed 2026-10-15T01:18:03Z to 2026-10-15T01:18:11Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| Native term-requests-check | passed | True | UBERON:0009060 | Executed 2026-10-15T01:18:11Z to 2026-10-15T01:18:46Z. term-request table is current (110 terms) |
| Native validate-products | passed | True | UBERON:0009060 | Executed 2026-10-15T01:18:46Z to 2026-10-15T01:20:48Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond. |
| Focused regressions | passed | True | UBERON:0009060 | Executed 2026-10-15T01:20:48Z to 2026-10-15T01:28:37Z. ........................................................................ [ 74%]<br>.........................                                                [100%]<br>97 passed in 467.28s (0:07:47) |
| Repository lint | passed | True | UBERON:0009060 | Executed 2026-10-15T01:28:37Z to 2026-10-15T01:28:37Z. All checks passed! |
| Whitespace | passed | True | UBERON:0009060 | Executed 2026-10-15T01:28:37Z to 2026-10-15T01:28:40Z. |
| Native render | passed | True | UBERON:0009060 | Executed 2026-10-15T01:29:55Z to 2026-10-15T01:31:02Z. rendered 3208 habitat pages, 258 redirect stubs, 8 categories, 121 term requests -&gt; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/pages |
| Native validate | passed | True | UBERON:0009060 | Executed 2026-10-15T01:31:02Z to 2026-10-15T01:31:08Z. No issues found |
| Native validate-strict | passed | True | UBERON:0009060 | Executed 2026-10-15T01:31:08Z to 2026-10-15T01:31:18Z. files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| Native validate-history | passed | True | UBERON:0009060 | Executed 2026-10-15T01:31:18Z to 2026-10-15T01:31:36Z. No issues found<br>726 history record(s) valid against src/habitatmech/schema/history.yaml |
| Native verify-corpus | passed | True | UBERON:0009060 | Executed 2026-10-15T01:31:36Z to 2026-10-15T01:32:14Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| Focused regressions | passed | True | UBERON:0009060 | Executed 2026-10-15T01:32:14Z to 2026-10-15T01:32:24Z. ..                                                                       [100%]<br>2 passed in 7.95s |
| Repository lint | passed | True | UBERON:0009060 | Executed 2026-10-15T01:32:24Z to 2026-10-15T01:32:24Z. All checks passed! |
| Semantic input export | passed | True | UBERON:0009060 | Executed 2026-10-15T01:32:24Z to 2026-10-15T01:32:39Z. {"adapter_version": "habitatmech-semantic-v1", "jsonl_sha256": "0558587d4f64acbaf076ce3c3b3031db377da3cc4900486a1ee4c271692d88f8", "mode": "export", "output": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/build/pr2145-linkfix-text-map-inputs.jsonl", "records": 3208, "scope": "full"} |
| Semantic input preservation | passed | True | UBERON:0009060 | Executed 2026-10-15T01:32:39Z to 2026-10-15T01:32:39Z. All 3208 semantic input rows byte-identical after punctuation-only correction |
| Whitespace | passed | True | UBERON:0009060 | Executed 2026-10-15T01:32:39Z to 2026-10-15T01:32:39Z. |
| Original source-member recovery | unavailable | False | UBERON:0009060 | Original GOLD member joins and PREGO pair-level citations remain unavailable. Anatomy and synonym corrections are not occurrence certification. |
| Final publication gates | unavailable | False | UBERON:0009060 | Final retained-archive verification and protected final-head QC remain required before merge. Local map verification and site regeneration passed; final publication freshness is reported separately. No final merge-gate success is predeclared. |

## Scientific And Domain Assessments

### Exact maintained-input repairs and remaining findings

grounding: supported. Targets: UBERON:0009060.

The exact GOLD respiratory-system container contribution is excluded while UBERON:0010000 remains the avian air-sac genus. Only the ontology-related psotcranial air sac alias changes to RELATED_SYNONYM; its spelling and both independently exact aliases are retained. Identity, original source nodes/path, zero-count omission and EXACT/REVIEWED status are unchanged.

### Identity, source evidence and native status preservation

consistency: supported. Targets: UBERON:0009060.

All original fields outside the explicit tested corrections are preserved. The entire current target was re-read. Native status is REVIEWED/EXACT; a saved review does not promote status or certify species occurrence.

## Findings

### F1: Respiratory-system container is emitted as a superclass

major / resolved / confirmed; issue key: uberon-0009060-respiratory-container-parent.

Pre-fix observation: Current typed UBERON relations make an avian air sac part of a respiratory system, not a kind of respiratory system. The source-derived system parent violates strict broader semantics.

Disposition: The exact GOLD respiratory-system container contribution is excluded while UBERON:0010000 remains the avian air-sac genus. Only the ontology-related psotcranial air sac alias changes to RELATED_SYNONYM; its spelling and both independently exact aliases are retained. Identity, original source nodes/path, zero-count omission and EXACT/REVIEWED status are unchanged.

### F2: Ontology-related synonym is inflated to exact equivalence

major / resolved / confirmed; issue key: uberon-0009060-related-synonym-promoted.

Pre-fix observation: The emitted psotcranial air sac synonym is EXACT_SYNONYM, while current UBERON explicitly types it hasRelatedSynonym. The retained flat ontology inventory loses scope; do not silently correct the source spelling or change unrelated exact synonyms.

Disposition: The exact GOLD respiratory-system container contribution is excluded while UBERON:0010000 remains the avian air-sac genus. Only the ontology-related psotcranial air sac alias changes to RELATED_SYNONYM; its spelling and both independently exact aliases are retained. Identity, original source nodes/path, zero-count omission and EXACT/REVIEWED status are unchanged.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| PREVIOUS | reviews/structured/20261015T005253Z-air_sac-record/review.yaml | supports | Exact same-agent predecessor retains inspected primary ontology/literature evidence, hashes, source rows and bounded access limitations. Not independent approval. |
| PATCH | curation/decisions.tsv; curation/gold_parent_exclusions.tsv; curation/record_annotation_corrections.tsv; curation/term_requests.tsv; data/habitats/host_associated/air_sac.yaml | supports | The exact GOLD respiratory-system container contribution is excluded while UBERON:0010000 remains the avian air-sac genus. Only the ontology-related psotcranial air sac alias changes to RELATED_SYNONYM; its spelling and both independently exact aliases are retained. Identity, original source nodes/path, zero-count omission and EXACT/REVIEWED status are unchanged. |
| REGRESSION | tests/test_airway_and_alga_repairs.py | supports | A full-corpus counterfactual reconstructs the former input rows and proves exactly five changed records, no identity changes, preserved counts/taxa/attestations and prior events, exact remaining parents and unchanged child insect-air-sac bytes. Only the insect Trachea parent gains ITEM-derived REVIEWED status. |

## Limits And Additional Notes

- Same-agent scientific reassessment, not independent approval.
- Original source-member evidence remains unavailable; no full-corpus, species-occurrence or SSSOM/KGX readiness certification.
- Configured label correspondence retains unsupported-prefix skips. Final retained-archive and protected publication gates are pending at this immutable observation.
- Source inputs were freshly captured with the native inspector and checked against exact committed blobs and current disk bytes. Retain this off-main input commit with an annotated provenance tag before squash and branch deletion.
- The original definition date, author and generated definition history of Algae were deliberately preserved; the new session history records the synonym-only correction. No historic review/history file was rewritten.
- Adversarial rendered-page inspection found a semicolon incorrectly included in the new issue 2148 href. The new publication regression reproduced the defect (one expected failure). Issue 2152 corrects the maintained note and regenerates the record/page, followed by fresh passing checks. Earlier temporary captures were superseded by a fresh native inspection and reassessment, not silently rehashed. Scientific fields and all 3208 semantic input rows remain unchanged by this punctuation-only follow-up.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T013700Z-air_sac-remediation
kind: record
repository: CultureBotAI/HabitatMech
title: 'Remediation review: air sac'
started_at: '2026-10-15T01:32:16Z'
finished_at: '2026-10-15T01:37:00Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Continuing review agent; current claims and historical leads
    were reassessed against primary evidence. No independent approval is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact GOLD respiratory-system container contribution is excluded while
  UBERON:0010000 remains the avian air-sac genus. Only the ontology-related psotcranial
  air sac alias changes to RELATED_SYNONYM; its spelling and both independently exact
  aliases are retained. Identity, original source nodes/path, zero-count omission
  and EXACT/REVIEWED status are unchanged.
source:
  git_revision: 81f9c9ead99cc14954df0c59bf752ed7284dd4b3
  state: git_commit
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
    sha256: d9c76d275d61b7fef860179b6d0472e54e15b2b027022d7a125a19f03881fd8e
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 505e6efc536392c9f6ce77fd4a70284392166269713189ff53e40367256d2899
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 41d223485ac848fcb5a724dc308caba88e922ae89c972ca9f92565ff3b753f32
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: 144e48a101aa072a96cd08f88a9a66ecd14122d788c54b95ac8ad7d934f720bc
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 034aee0bcf71e9c813d20450bc93d7f3f6070cab0ddebfe6f3f39911e7c6b0e1
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b0135af0aa4deed0f3824a2f491d5a742c1b7de4775c533f283761d22e805821
    role: context
  - path: data/habitats/host_associated/air_sac.yaml
    sha256: 786f0ffcea004d114d2ddb672ea9dcd9694215ea7846e1b3cf2ad99883b5b061
    role: target
  - path: data/habitats/host_associated/respiratory_system__431eac8d.yaml
    sha256: 700815817315ed32613134e3b2ba05700a2600c1c0935a53173134b967d0e617
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
  - path: history/mappings/air_sac/2026-10-15T011325Z-codex-gpt-5-69f5dd.yaml
    sha256: 13a5cf8d28124aedefd71533ee4f027996cfd49eb31f107fb380cad2d17575a2
    role: context
  - path: history/mappings/air_sac/2026-10-15T011333Z-codex-gpt-5-0d02ca.yaml
    sha256: f368c5a1c69c0947c90ccf718c09176dbc8c4e8d552707ff287046e099285d4f
    role: context
  - path: history/mappings/air_sac/2026-10-15T012856Z-codex-gpt-5-9cd9fc.yaml
    sha256: 26445221603d04ca66c25776093ca39bee3744975a74a94e36071fa9bc2aec23
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260929T042341Z-air_sac.md
    sha256: 014c1760c4d351c523a4e1d5328da58b83115006a4087aa720e2be89c0c4f430
    role: context
  - path: reviews/structured/20261015T005253Z-air_sac-record/review.md
    sha256: d74a53890a0c60971bf6e91b4040da3b70b6b662e33648017ecafd4d973ad8b2
    role: context
  - path: reviews/structured/20261015T005253Z-air_sac-record/review.yaml
    sha256: 2fc8746ceaea79eb8f587291913ae53c97ecd2a3a8a90d55847773504e9c706c
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/habitatmech/curate/decisions.py
    sha256: f33d3e9dc95bb428e63e640d48d4074cf15e90ea666603fb16fb651d591e3f02
    role: context
  - path: src/habitatmech/curate/definitions.py
    sha256: decd02eea029e884ab1a8bbb51dd870edb5544906b3ddd39598147b27ce572c9
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
  - path: tests/test_airway_and_alga_repairs.py
    sha256: 8593a60916200c099b6ec7d30cfc542a71acf55dafe09c22deadece1e0080f6e
    role: context
  - path: tests/test_airway_publication.py
    sha256: 0cc3a47fdabc09abdc12c5758b7fa4f05931720c3a01c33353bdfe1c8c3039ef
    role: context
targets:
- target_id: UBERON:0009060
  path: data/habitats/host_associated/air_sac.yaml
  label: air sac
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained source, curation input, or generator; target YAML is read-only
scope:
  description: Focused scientific reassessment of the complete current record and
    exact prior findings after maintained-input remediation.
  selection: Exact successor to 20261015T005253Z-air_sac-record
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - UBERON:0009060
checks:
- check_id: FIX0
  name: Native validate
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/air_sac.yaml
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: Executed 2026-10-15T01:16:17Z to 2026-10-15T01:16:23Z. No issues found
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX6
  name: Native validate-strict
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/air_sac.yaml data/habitats/host_associated/air_sacs__d20658f1.yaml
    data/habitats/host_associated/algae.yaml data/habitats/host_associated/alveoli.yaml
    data/habitats/host_associated/alveoli__5d35ddee.yaml data/habitats/host_associated/trachea__4ac9ebc1.yaml
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: "Executed 2026-10-15T01:16:49Z to 2026-10-15T01:17:00Z. files scanned:\
    \      6\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:           \
    \     reports/instance_validation_failures.tsv"
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX7
  name: Native validate-history
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: 'Executed 2026-10-15T01:17:00Z to 2026-10-15T01:17:19Z. No issues found

    725 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX8
  name: Native provenance-check
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: 'Executed 2026-10-15T01:17:19Z to 2026-10-15T01:17:20Z. provenance current:
    14 committed inventories, 2 GOLD sources'
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX9
  name: Native verify-corpus
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: "Executed 2026-10-15T01:17:20Z to 2026-10-15T01:18:03Z. expected 3208 records,\
    \ found 3208 on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus\
    \ reproduces exactly from data/raw/"
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX10
  name: Native validate-causal-all
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: Executed 2026-10-15T01:18:03Z to 2026-10-15T01:18:11Z. validated 32 causal-graph
    curation file(s) with 32 graph(s)
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX11
  name: Native term-requests-check
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: Executed 2026-10-15T01:18:11Z to 2026-10-15T01:18:46Z. term-request table
    is current (110 terms)
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX12
  name: Native validate-products
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: "Executed 2026-10-15T01:18:46Z to 2026-10-15T01:20:48Z. id↔label correspondence\
    \ summary:\n          OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n        \
    \  OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond."
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX13
  name: Focused regressions
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_airway_and_alga_repairs.py tests/test_gold_parent_exclusions.py
    tests/test_record_annotation_corrections.py tests/test_curated_definitions.py
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: 'Executed 2026-10-15T01:20:48Z to 2026-10-15T01:28:37Z. ........................................................................
    [ 74%]

    .........................                                                [100%]

    97 passed in 467.28s (0:07:47)'
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX14
  name: Repository lint
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m ruff check .
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: Executed 2026-10-15T01:28:37Z to 2026-10-15T01:28:37Z. All checks passed!
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX15
  name: Whitespace
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache git diff --check
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: Executed 2026-10-15T01:28:37Z to 2026-10-15T01:28:40Z.
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX16
  name: Native render
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just render
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: Executed 2026-10-15T01:29:55Z to 2026-10-15T01:31:02Z. rendered 3208 habitat
    pages, 258 redirect stubs, 8 categories, 121 term requests -> /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/pages
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX17
  name: Native validate
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/air_sac.yaml
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: Executed 2026-10-15T01:31:02Z to 2026-10-15T01:31:08Z. No issues found
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX18
  name: Native validate-strict
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/air_sac.yaml
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: "Executed 2026-10-15T01:31:08Z to 2026-10-15T01:31:18Z. files scanned:\
    \      1\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:           \
    \     reports/instance_validation_failures.tsv"
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX19
  name: Native validate-history
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: 'Executed 2026-10-15T01:31:18Z to 2026-10-15T01:31:36Z. No issues found

    726 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX20
  name: Native verify-corpus
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: "Executed 2026-10-15T01:31:36Z to 2026-10-15T01:32:14Z. expected 3208 records,\
    \ found 3208 on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus\
    \ reproduces exactly from data/raw/"
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX21
  name: Focused regressions
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_airway_and_alga_repairs.py tests/test_airway_publication.py
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: 'Executed 2026-10-15T01:32:14Z to 2026-10-15T01:32:24Z. ..                                                                       [100%]

    2 passed in 7.95s'
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX22
  name: Repository lint
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m ruff check .
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: Executed 2026-10-15T01:32:24Z to 2026-10-15T01:32:24Z. All checks passed!
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX23
  name: Semantic input export
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    scripts/text_map_inputs.py --output build/pr2145-linkfix-text-map-inputs.jsonl
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: 'Executed 2026-10-15T01:32:24Z to 2026-10-15T01:32:39Z. {"adapter_version":
    "habitatmech-semantic-v1", "jsonl_sha256": "0558587d4f64acbaf076ce3c3b3031db377da3cc4900486a1ee4c271692d88f8",
    "mode": "export", "output": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/build/pr2145-linkfix-text-map-inputs.jsonl",
    "records": 3208, "scope": "full"}'
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX24
  name: Semantic input preservation
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -c from pathlib import Path; assert Path("build/pr2145-linkfix-text-map-inputs.jsonl").read_bytes()
    == Path("build/pr2145-text-map-inputs.jsonl").read_bytes(); print("All 3208 semantic
    input rows byte-identical after punctuation-only correction")
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: Executed 2026-10-15T01:32:39Z to 2026-10-15T01:32:39Z. All 3208 semantic
    input rows byte-identical after punctuation-only correction
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX25
  name: Whitespace
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache git diff --check b09f0b8718528ce9b5853f3a809d2e1846499f99
  exit_code: 0
  target_ids:
  - UBERON:0009060
  summary: Executed 2026-10-15T01:32:39Z to 2026-10-15T01:32:39Z.
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: MEMBERS
  name: Original source-member recovery
  required: false
  status: unavailable
  target_ids:
  - UBERON:0009060
  summary: Original GOLD member joins and PREGO pair-level citations remain unavailable.
    Anatomy and synonym corrections are not occurrence certification.
- check_id: PUBLICATION
  name: Final publication gates
  required: false
  status: unavailable
  target_ids:
  - UBERON:0009060
  summary: Final retained-archive verification and protected final-head QC remain
    required before merge. Local map verification and site regeneration passed; final
    publication freshness is reported separately. No final merge-gate success is predeclared.
evidence:
- evidence_id: PREVIOUS
  kind: prior_review
  reference: reviews/structured/20261015T005253Z-air_sac-record/review.yaml
  accessed_at: '2026-10-15T01:37:00Z'
  support: supports
  summary: Exact same-agent predecessor retains inspected primary ontology/literature
    evidence, hashes, source rows and bounded access limitations. Not independent
    approval.
- evidence_id: PATCH
  kind: record_content
  reference: curation/decisions.tsv; curation/gold_parent_exclusions.tsv; curation/record_annotation_corrections.tsv;
    curation/term_requests.tsv; data/habitats/host_associated/air_sac.yaml
  accessed_at: '2026-10-15T01:37:00Z'
  support: supports
  summary: The exact GOLD respiratory-system container contribution is excluded while
    UBERON:0010000 remains the avian air-sac genus. Only the ontology-related psotcranial
    air sac alias changes to RELATED_SYNONYM; its spelling and both independently
    exact aliases are retained. Identity, original source nodes/path, zero-count omission
    and EXACT/REVIEWED status are unchanged.
- evidence_id: REGRESSION
  kind: validation
  reference: tests/test_airway_and_alga_repairs.py
  accessed_at: '2026-10-15T01:37:00Z'
  support: supports
  summary: A full-corpus counterfactual reconstructs the former input rows and proves
    exactly five changed records, no identity changes, preserved counts/taxa/attestations
    and prior events, exact remaining parents and unchanged child insect-air-sac bytes.
    Only the insect Trachea parent gains ITEM-derived REVIEWED status.
assessments:
- assessment_id: REPAIR
  area: grounding
  topic: Exact maintained-input repairs and remaining findings
  outcome: supported
  target_ids:
  - UBERON:0009060
  evidence_ids:
  - PREVIOUS
  - PATCH
  - REGRESSION
  summary: The exact GOLD respiratory-system container contribution is excluded while
    UBERON:0010000 remains the avian air-sac genus. Only the ontology-related psotcranial
    air sac alias changes to RELATED_SYNONYM; its spelling and both independently
    exact aliases are retained. Identity, original source nodes/path, zero-count omission
    and EXACT/REVIEWED status are unchanged.
- assessment_id: PRESERVATION
  area: consistency
  topic: Identity, source evidence and native status preservation
  outcome: supported
  target_ids:
  - UBERON:0009060
  evidence_ids:
  - PREVIOUS
  - REGRESSION
  summary: All original fields outside the explicit tested corrections are preserved.
    The entire current target was re-read. Native status is REVIEWED/EXACT; a saved
    review does not promote status or certify species occurrence.
  dimensions:
  - name: mapping_status
    value: REVIEWED
    definition: Native generated status, separate from scientific-review verdict
    evidence_ids:
    - PATCH
  - name: grounding_status
    value: EXACT
    definition: Native generated status, separate from scientific-review verdict
    evidence_ids:
    - PATCH
findings:
- issue_key: uberon-0009060-respiratory-container-parent
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: Respiratory-system container is emitted as a superclass
  description: 'Pre-fix observation: Current typed UBERON relations make an avian
    air sac part of a respiratory system, not a kind of respiratory system. The source-derived
    system parent violates strict broader semantics.'
  field_paths:
  - parent_habitats
  evidence_ids:
  - PREVIOUS
  - PATCH
  - REGRESSION
  rule_id: HabitatMech:claim-scope-and-strict-broader-identity
  native_severity: major
  normalization_reason: The finding changes the scientific interpretation of an anatomical
    relation, identity or occurrence claim, rather than style. Provisional findings
    require original source evidence before correction.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  finding_id: F1
  target_ids:
  - UBERON:0009060
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T005253Z-air_sac-record
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2147
  disposition_reason: The exact GOLD respiratory-system container contribution is
    excluded while UBERON:0010000 remains the avian air-sac genus. Only the ontology-related
    psotcranial air sac alias changes to RELATED_SYNONYM; its spelling and both independently
    exact aliases are retained. Identity, original source nodes/path, zero-count omission
    and EXACT/REVIEWED status are unchanged.
- issue_key: uberon-0009060-related-synonym-promoted
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: Ontology-related synonym is inflated to exact equivalence
  description: 'Pre-fix observation: The emitted psotcranial air sac synonym is EXACT_SYNONYM,
    while current UBERON explicitly types it hasRelatedSynonym. The retained flat
    ontology inventory loses scope; do not silently correct the source spelling or
    change unrelated exact synonyms.'
  field_paths:
  - synonyms
  evidence_ids:
  - PREVIOUS
  - PATCH
  - REGRESSION
  rule_id: HabitatMech:claim-scope-and-strict-broader-identity
  native_severity: major
  normalization_reason: The finding changes the scientific interpretation of an anatomical
    relation, identity or occurrence claim, rather than style. Provisional findings
    require original source evidence before correction.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained source, curation input, or generator; target YAML is read-only
  finding_id: F2
  target_ids:
  - UBERON:0009060
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T005253Z-air_sac-record
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2148
  disposition_reason: The exact GOLD respiratory-system container contribution is
    excluded while UBERON:0010000 remains the avian air-sac genus. Only the ontology-related
    psotcranial air sac alias changes to RELATED_SYNONYM; its spelling and both independently
    exact aliases are retained. Identity, original source nodes/path, zero-count omission
    and EXACT/REVIEWED status are unchanged.
actions: []
limitations:
- Same-agent scientific reassessment, not independent approval.
- Original source-member evidence remains unavailable; no full-corpus, species-occurrence
  or SSSOM/KGX readiness certification.
- Configured label correspondence retains unsupported-prefix skips. Final retained-archive
  and protected publication gates are pending at this immutable observation.
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261015T005253Z-air_sac-record
  relationship: Exact finding remediation successor retaining every affected predecessor
    target
notes:
- Source inputs were freshly captured with the native inspector and checked against
  exact committed blobs and current disk bytes. Retain this off-main input commit
  with an annotated provenance tag before squash and branch deletion.
- The original definition date, author and generated definition history of Algae were
  deliberately preserved; the new session history records the synonym-only correction.
  No historic review/history file was rewritten.
- Adversarial rendered-page inspection found a semicolon incorrectly included in the
  new issue 2148 href. The new publication regression reproduced the defect (one expected
  failure). Issue 2152 corrects the maintained note and regenerates the record/page,
  followed by fresh passing checks. Earlier temporary captures were superseded by
  a fresh native inspection and reassessment, not silently rehashed. Scientific fields
  and all 3208 semantic input rows remain unchanged by this punctuation-only follow-up.
```
