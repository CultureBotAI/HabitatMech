# Remediation review: Amniotic fluid

- Review: 20261015T031942Z-amniotic_fluid__ff65cb2e-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T03:09:26Z
- Finished UTC: 2026-10-15T03:19:42Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The specific amniotic-sac source-parent contribution is excluded, retaining the independent fluid genus, human-qualified source mint, node 6329, full path and three ORGANISM assertions. NARROW/SEEDED and the source attestation are unchanged. The mapping-endpoint contract remains unresolved under #1398. Fluid is not treated as a subtype of either an enclosing membrane or cavity; the sac identity ambiguity is not resolved by this edit.

## Scope And Provenance

Complete current target reread and exact finding reassessment after scoped maintained-input remediation; not a new source-member reconstruction.

Selection: Exact successor to 20261015T024348Z-amniotic_fluid__ff65cb2e-record
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base b35a65277f6fa952ffad11b1c642a9655074a40f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.73051a70cb | data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml | generated | Amniotic fluid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Post-remediation just validate data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml | passed | True | habitatmech:GOLD.73051a70cb | Executed 2026-10-15T03:08:14Z to 2026-10-15T03:08:26Z. No issues found |
| Post-remediation just validate-strict data/habitats/host_associated/amniotic_fluid__8d4e7d01.yaml | passed | True | habitatmech:GOLD.73051a70cb | Executed 2026-10-15T03:08:37Z to 2026-10-15T03:08:57Z. files scanned:      3<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| Post-remediation just validate-history | passed | True | habitatmech:GOLD.73051a70cb | Executed 2026-10-15T03:08:57Z to 2026-10-15T03:09:25Z. No issues found<br>730 history record(s) valid against src/habitatmech/schema/history.yaml |
| Post-remediation just provenance-check | passed | True | habitatmech:GOLD.73051a70cb | Executed 2026-10-15T03:09:25Z to 2026-10-15T03:09:26Z. provenance current: 14 committed inventories, 2 GOLD sources |
| Post-remediation just verify-corpus | passed | True | habitatmech:GOLD.73051a70cb | Executed 2026-10-15T03:09:26Z to 2026-10-15T03:10:09Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| Post-remediation just validate-causal-all | passed | True | habitatmech:GOLD.73051a70cb | Executed 2026-10-15T03:10:09Z to 2026-10-15T03:10:20Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| Post-remediation just term-requests-check | passed | True | habitatmech:GOLD.73051a70cb | Executed 2026-10-15T03:10:20Z to 2026-10-15T03:11:11Z. term-request table is current (110 terms) |
| Post-remediation just validate-products | passed | True | habitatmech:GOLD.73051a70cb | Executed 2026-10-15T03:11:11Z to 2026-10-15T03:13:13Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond. |
| Post-remediation /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m pytest | passed | True | habitatmech:GOLD.73051a70cb | Executed 2026-10-15T03:13:13Z to 2026-10-15T03:18:17Z. ........................................................................ [ 80%]<br>..................                                                       [100%]<br>90 passed in 301.90s (0:05:01) |
| Post-remediation /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m ruff | passed | True | habitatmech:GOLD.73051a70cb | Executed 2026-10-15T03:18:17Z to 2026-10-15T03:18:17Z. All checks passed! |
| Post-remediation git diff --check | passed | True | habitatmech:GOLD.73051a70cb | Executed 2026-10-15T03:18:17Z to 2026-10-15T03:18:19Z. |
| Original source-member recovery | unavailable | False | habitatmech:GOLD.73051a70cb | Original GOLD member roles remain uncertified. Hierarchy and synonym correction is not proof of taxon occurrence, healthy prenatal microbiome or original study membership. |
| Final publication gates | unavailable | False | habitatmech:GOLD.73051a70cb | Final retained-archive verification, semantic map/site freshness and protected final-head QC are publication requirements reported separately. They are not predeclared successful here. |
| iModulonDB applicability | not_applicable | False | habitatmech:GOLD.73051a70cb | The record has no gene, regulator or expression claim; no molecular adapter query is needed. |

## Scientific And Domain Assessments

### Supported correction through guarded maintained input

graph: supported. Targets: habitatmech:GOLD.73051a70cb.

The specific amniotic-sac source-parent contribution is excluded, retaining the independent fluid genus, human-qualified source mint, node 6329, full path and three ORGANISM assertions. NARROW/SEEDED and the source attestation are unchanged. The mapping-endpoint contract remains unresolved under #1398. Fluid is not treated as a subtype of either an enclosing membrane or cavity; the sac identity ambiguity is not resolved by this edit.

### Complete-record identity, source evidence and native status

consistency: supported. Targets: habitatmech:GOLD.73051a70cb.

The complete target was re-read. All fields outside the tested correction and appended history event match the prior record. Exact source identity, raw rows, definition and independently supported parents remain as assessed in the predecessor. No optional parameters, causal edges, characteristic taxa or biological claims are added.

### Separate unresolved predecessor finding

representation: concern. Targets: habitatmech:GOLD.73051a70cb.

The record still has the source-to-record/ontology comparison endpoint mismatch tracked by #1398.

## Findings

### F1: GOLD context parent is not a broader fluid habitat

major / resolved / confirmed; issue key: HM-AMNIOTIC-FLUID-HUMAN-001.

Pre-fix observation: The source path was copied correctly but its immediate context-only parent is an unsupported is-a contribution. Preserve the independent UBERON fluid parent, source path and count unit; missing definitions or zero assertions are not additional defects.

Disposition: The specific amniotic-sac source-parent contribution is excluded, retaining the independent fluid genus, human-qualified source mint, node 6329, full path and three ORGANISM assertions. NARROW/SEEDED and the source attestation are unchanged. The mapping-endpoint contract remains unresolved under #1398. Fluid is not treated as a subtype of either an enclosing membrane or cavity; the sac identity ambiguity is not resolved by this edit.

### F2: Source mapping omits its actual ontology comparison endpoint

major / open / confirmed; issue key: gold-73051a70cb-mapping-endpoint-contract.

Pre-fix observation: The producer compares the path concept to UBERON:0000173 but emits narrowMatch under a field defined as mapping the source to the retained record identifier. A predicate swap cannot supply the missing endpoint or reconcile consumers.

Disposition: The separate confirmed contract or historical provenance defect remains; the scoped parent/synonym correction does not repair it.

## Recommended Actions And Acceptance Checks

### ACT2

Resolve the existing shared mapping-endpoint contract before claiming SSSOM/KGX conformance. Represent source, record and ontology endpoints explicitly and audit actual consumers; do not apply a global narrow/broad predicate replacement.

- Test subject, predicate, object and grounding meaning for retained-mint and exact routes, including this witness; inspect actual exports against current kg-microbe modeling.
- Preserve exact source IDs, paths, counts and units; compare affected descendants and unrelated records, not only the target label.
- Append a new session history for any separately authorized curation; never rewrite saved reviews or previous session records.
- Run schema/strict, history, provenance, exact corpus reproduction, causal, term-request and configured label gates, then just qc.
- Check actual semantic-input changes and regenerate map/site/redirect products through supported tooling when required; save an immutable successor with exact finding lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| PREVIOUS | reviews/structured/20261015T024348Z-amniotic_fluid__ff65cb2e-record/review.yaml | supports | Exact predecessor contains the inspected primary ontology, taxonomy and source evidence, original response hashes and access limitations. Reused scientific context, not independent approval or a claim of fresh external downloads. |
| PATCH | curation/gold_parent_exclusions.tsv; curation/definition_source_label_exclusions.tsv; curation/term_requests.tsv; data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml | supports | The specific amniotic-sac source-parent contribution is excluded, retaining the independent fluid genus, human-qualified source mint, node 6329, full path and three ORGANISM assertions. NARROW/SEEDED and the source attestation are unchanged. The mapping-endpoint contract remains unresolved under #1398. Fluid is not treated as a subtype of either an enclosing membrane or cavity; the sac identity ambiguity is not resolved by this edit. |
| REGRESSION | tests/test_amniotic_amoebozoan_repairs.py | supports | Complete-corpus counterfactual reconstructs former inputs and proves exactly three changed records, no changed IDs, preserved attestations/counts/statuses and prior events. Removing only the authored alias reproduces the automatic fallback. Repeated corpus construction is identical. |
| SOURCE | data/raw/gold_ecosystem_paths.tsv; curation/decisions.tsv; src/habitatmech/schema/habitatmech.yaml | supports | The current complete target still matches its exact frozen source paths, collapsed nodes and ORGANISM count semantics; none of the decisions or source rows changed. Source-to-record mapping endpoint semantics and immutable definition-history concerns remain distinct from the repaired fields. |

## Limits And Additional Notes

- Same-agent scientific reassessment, not independent approval.
- Original source-member evidence remains unavailable; no full-corpus, species-occurrence or SSSOM/KGX readiness certification.
- Configured label correspondence skips 2061 no-adapter pairs. Final retained-archive and protected publication gates are pending at this observation.
- The unresolved F2 finding remains open; this is not a clean-record verdict.
- The native inspector captured current inputs after remediation; each hash was verified against exact committed blobs and disk bytes before saving. This is a review of that exact commit. Preserve its off-main base with an annotated remote provenance tag before squash and branch deletion.
- All original review and history files remain immutable. New curation events and four session histories document the bounded changes; no status is promoted by review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T031942Z-amniotic_fluid__ff65cb2e-remediation
kind: record
repository: CultureBotAI/HabitatMech
title: 'Remediation review: Amniotic fluid'
started_at: '2026-10-15T03:09:26Z'
finished_at: '2026-10-15T03:19:42Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Continuing review agent. Complete target and maintained inputs
    were independently reassessed from historical leads, but this is not independent
    human or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'The specific amniotic-sac source-parent contribution is excluded, retaining
  the independent fluid genus, human-qualified source mint, node 6329, full path and
  three ORGANISM assertions. NARROW/SEEDED and the source attestation are unchanged.
  The mapping-endpoint contract remains unresolved under #1398. Fluid is not treated
  as a subtype of either an enclosing membrane or cavity; the sac identity ambiguity
  is not resolved by this edit.'
source:
  git_revision: b35a65277f6fa952ffad11b1c642a9655074a40f
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
  - path: conf/record_review.yaml
    sha256: c2f5d0eb4c5744f5fe354c92184ddab144dc2688dba952b032b4f3d597bc08d6
    role: context
  - path: curation/decisions.tsv
    sha256: d9c76d275d61b7fef860179b6d0472e54e15b2b027022d7a125a19f03881fd8e
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: a3e2880134344406dd3239ee041076df64c76407d311b71a16f2382c4146a177
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: be17ead1dfa258599ee8c31af96143b6415c059a3f0a48ac92ba6afa5c590831
    role: context
  - path: curation/term_requests.tsv
    sha256: 1a03f5fb7ade4232aadf5ad248c87da894a67e90ef3eab513849982429a9155e
    role: context
  - path: data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml
    sha256: 1b826c1011f271b696ab7b906d6556fb038748065a49e2c63e14f336eabfe45a
    role: target
  - path: data/raw/GOLD_MANIFEST.yaml
    sha256: 99ec487ae02d512cfb75440685f927abe907effe52cb755feb095631e8841489
    role: context
  - path: data/raw/MANIFEST.yaml
    sha256: 4657672d429be35e551ceef4a1204ab0a8120558ce63e2a2b74188eee94b8480
    role: context
  - path: data/raw/gold_ecosystem_paths.tsv
    sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
    role: context
  - path: data/raw/ontology_subclass_edges.tsv
    sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
    role: context
  - path: data/raw/ontology_terms.tsv
    sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
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
  - path: history/mappings/amniotic_fluid__ff65cb2e/2026-10-15T030403Z-codex-gpt-5-6dc50b.yaml
    sha256: 07ae3917b04cf4ac9ed131750164402f2fe73d8f8ad6f17a072ab35cfff6e973
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reviews/structured/20261015T024348Z-amniotic_fluid__ff65cb2e-record/review.md
    sha256: f3bfc9756046a741f4896a9bd933f60f1430fdb0a62a41bea833727061a848fc
    role: context
  - path: reviews/structured/20261015T024348Z-amniotic_fluid__ff65cb2e-record/review.yaml
    sha256: c276324cb287f52919c609f9bea2c3557b185123dfbc97dc3f00aab66dc78e4f
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/habitatmech/curate/definition_source_label_exclusions.py
    sha256: 0c13e83fe17613e8b9f5b346d1259104172f8c1de42f911625579b903707625d
    role: context
  - path: src/habitatmech/curate/gold_parent_exclusions.py
    sha256: 044d8277509a9b1f6e4f2d7ea1fb82319b41e09ffef7788738a0f4ed0d0b63af
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
  - path: tests/test_amniotic_amoebozoan_repairs.py
    sha256: 07de38a179f078286a7830c5951c5ad84ca93e6110e33bea6c555663033d2be8
    role: context
targets:
- target_id: habitatmech:GOLD.73051a70cb
  path: data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml
  label: Amniotic fluid
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
scope:
  description: Complete current target reread and exact finding reassessment after
    scoped maintained-input remediation; not a new source-member reconstruction.
  selection: Exact successor to 20261015T024348Z-amniotic_fluid__ff65cb2e-record
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.73051a70cb
checks:
- check_id: FIX1
  name: Post-remediation just validate data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.73051a70cb
  summary: Executed 2026-10-15T03:08:14Z to 2026-10-15T03:08:26Z. No issues found
- check_id: FIX3
  name: Post-remediation just validate-strict data/habitats/host_associated/amniotic_fluid__8d4e7d01.yaml
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/amniotic_fluid__8d4e7d01.yaml data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml
    data/habitats/host_associated/amoebozoa__291e8086.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.73051a70cb
  summary: "Executed 2026-10-15T03:08:37Z to 2026-10-15T03:08:57Z. files scanned:\
    \      3\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:           \
    \     reports/instance_validation_failures.tsv"
- check_id: FIX4
  name: Post-remediation just validate-history
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.73051a70cb
  summary: 'Executed 2026-10-15T03:08:57Z to 2026-10-15T03:09:25Z. No issues found

    730 history record(s) valid against src/habitatmech/schema/history.yaml'
- check_id: FIX5
  name: Post-remediation just provenance-check
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.73051a70cb
  summary: 'Executed 2026-10-15T03:09:25Z to 2026-10-15T03:09:26Z. provenance current:
    14 committed inventories, 2 GOLD sources'
- check_id: FIX6
  name: Post-remediation just verify-corpus
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.73051a70cb
  summary: "Executed 2026-10-15T03:09:26Z to 2026-10-15T03:10:09Z. expected 3208 records,\
    \ found 3208 on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus\
    \ reproduces exactly from data/raw/"
- check_id: FIX7
  name: Post-remediation just validate-causal-all
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.73051a70cb
  summary: Executed 2026-10-15T03:10:09Z to 2026-10-15T03:10:20Z. validated 32 causal-graph
    curation file(s) with 32 graph(s)
- check_id: FIX8
  name: Post-remediation just term-requests-check
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.73051a70cb
  summary: Executed 2026-10-15T03:10:20Z to 2026-10-15T03:11:11Z. term-request table
    is current (110 terms)
- check_id: FIX9
  name: Post-remediation just validate-products
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.73051a70cb
  summary: "Executed 2026-10-15T03:11:11Z to 2026-10-15T03:13:13Z. id↔label correspondence\
    \ summary:\n          OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n        \
    \  OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond."
- check_id: FIX10
  name: Post-remediation /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_amniotic_amoebozoan_repairs.py tests/test_definition_source_label_exclusions.py
    tests/test_gold_parent_exclusions.py tests/test_curated_definitions.py
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.73051a70cb
  summary: 'Executed 2026-10-15T03:13:13Z to 2026-10-15T03:18:17Z. ........................................................................
    [ 80%]

    ..................                                                       [100%]

    90 passed in 301.90s (0:05:01)'
- check_id: FIX11
  name: Post-remediation /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m ruff
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m ruff check .
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.73051a70cb
  summary: Executed 2026-10-15T03:18:17Z to 2026-10-15T03:18:17Z. All checks passed!
- check_id: FIX12
  name: Post-remediation git diff --check
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache git diff --check 45c39c0ae63d7825c13b586b8e99e68a396af394
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.73051a70cb
  summary: Executed 2026-10-15T03:18:17Z to 2026-10-15T03:18:19Z.
- check_id: MEMBERS
  name: Original source-member recovery
  required: false
  status: unavailable
  target_ids:
  - habitatmech:GOLD.73051a70cb
  summary: Original GOLD member roles remain uncertified. Hierarchy and synonym correction
    is not proof of taxon occurrence, healthy prenatal microbiome or original study
    membership.
- check_id: PUBLICATION
  name: Final publication gates
  required: false
  status: unavailable
  target_ids:
  - habitatmech:GOLD.73051a70cb
  summary: Final retained-archive verification, semantic map/site freshness and protected
    final-head QC are publication requirements reported separately. They are not predeclared
    successful here.
- check_id: MOLECULAR
  name: iModulonDB applicability
  required: false
  status: not_applicable
  target_ids:
  - habitatmech:GOLD.73051a70cb
  summary: The record has no gene, regulator or expression claim; no molecular adapter
    query is needed.
evidence:
- evidence_id: PREVIOUS
  kind: prior_review
  reference: reviews/structured/20261015T024348Z-amniotic_fluid__ff65cb2e-record/review.yaml
  accessed_at: '2026-10-15T03:19:42Z'
  support: supports
  summary: Exact predecessor contains the inspected primary ontology, taxonomy and
    source evidence, original response hashes and access limitations. Reused scientific
    context, not independent approval or a claim of fresh external downloads.
- evidence_id: PATCH
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv; curation/definition_source_label_exclusions.tsv;
    curation/term_requests.tsv; data/habitats/host_associated/amniotic_fluid__ff65cb2e.yaml
  accessed_at: '2026-10-15T03:19:42Z'
  support: supports
  summary: 'The specific amniotic-sac source-parent contribution is excluded, retaining
    the independent fluid genus, human-qualified source mint, node 6329, full path
    and three ORGANISM assertions. NARROW/SEEDED and the source attestation are unchanged.
    The mapping-endpoint contract remains unresolved under #1398. Fluid is not treated
    as a subtype of either an enclosing membrane or cavity; the sac identity ambiguity
    is not resolved by this edit.'
- evidence_id: REGRESSION
  kind: validation
  reference: tests/test_amniotic_amoebozoan_repairs.py
  accessed_at: '2026-10-15T03:19:42Z'
  support: supports
  summary: Complete-corpus counterfactual reconstructs former inputs and proves exactly
    three changed records, no changed IDs, preserved attestations/counts/statuses
    and prior events. Removing only the authored alias reproduces the automatic fallback.
    Repeated corpus construction is identical.
- evidence_id: SOURCE
  kind: record_content
  reference: data/raw/gold_ecosystem_paths.tsv; curation/decisions.tsv; src/habitatmech/schema/habitatmech.yaml
  accessed_at: '2026-10-15T03:19:42Z'
  support: supports
  summary: The current complete target still matches its exact frozen source paths,
    collapsed nodes and ORGANISM count semantics; none of the decisions or source
    rows changed. Source-to-record mapping endpoint semantics and immutable definition-history
    concerns remain distinct from the repaired fields.
assessments:
- assessment_id: REPAIR
  area: graph
  topic: Supported correction through guarded maintained input
  outcome: supported
  target_ids:
  - habitatmech:GOLD.73051a70cb
  evidence_ids:
  - PREVIOUS
  - PATCH
  - REGRESSION
  summary: 'The specific amniotic-sac source-parent contribution is excluded, retaining
    the independent fluid genus, human-qualified source mint, node 6329, full path
    and three ORGANISM assertions. NARROW/SEEDED and the source attestation are unchanged.
    The mapping-endpoint contract remains unresolved under #1398. Fluid is not treated
    as a subtype of either an enclosing membrane or cavity; the sac identity ambiguity
    is not resolved by this edit.'
- assessment_id: PRESERVATION
  area: consistency
  topic: Complete-record identity, source evidence and native status
  outcome: supported
  target_ids:
  - habitatmech:GOLD.73051a70cb
  evidence_ids:
  - PREVIOUS
  - REGRESSION
  - SOURCE
  summary: The complete target was re-read. All fields outside the tested correction
    and appended history event match the prior record. Exact source identity, raw
    rows, definition and independently supported parents remain as assessed in the
    predecessor. No optional parameters, causal edges, characteristic taxa or biological
    claims are added.
- assessment_id: OPEN
  area: representation
  topic: Separate unresolved predecessor finding
  outcome: concern
  target_ids:
  - habitatmech:GOLD.73051a70cb
  evidence_ids:
  - PREVIOUS
  - PATCH
  - SOURCE
  summary: 'The record still has the source-to-record/ontology comparison endpoint
    mismatch tracked by #1398.'
findings:
- finding_id: F1
  issue_key: HM-AMNIOTIC-FLUID-HUMAN-001
  category: graph
  severity: major
  status: resolved
  certainty: confirmed
  title: GOLD context parent is not a broader fluid habitat
  description: 'Pre-fix observation: The source path was copied correctly but its
    immediate context-only parent is an unsupported is-a contribution. Preserve the
    independent UBERON fluid parent, source path and count unit; missing definitions
    or zero assertions are not additional defects.'
  target_ids:
  - habitatmech:GOLD.73051a70cb
  field_paths:
  - parent_habitats
  evidence_ids:
  - PREVIOUS
  - PATCH
  - REGRESSION
  - SOURCE
  rule_id: 'docs/CURATION.md: semantic habitat and strictly-broader hierarchy rules'
  native_severity: major
  normalization_reason: Native severity agrees with the shared record-review rubric.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1318
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T024348Z-amniotic_fluid__ff65cb2e-record
    finding_id: F1
  disposition_reason: 'The specific amniotic-sac source-parent contribution is excluded,
    retaining the independent fluid genus, human-qualified source mint, node 6329,
    full path and three ORGANISM assertions. NARROW/SEEDED and the source attestation
    are unchanged. The mapping-endpoint contract remains unresolved under #1398. Fluid
    is not treated as a subtype of either an enclosing membrane or cavity; the sac
    identity ambiguity is not resolved by this edit.'
- finding_id: F2
  issue_key: gold-73051a70cb-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Source mapping omits its actual ontology comparison endpoint
  description: 'Pre-fix observation: The producer compares the path concept to UBERON:0000173
    but emits narrowMatch under a field defined as mapping the source to the retained
    record identifier. A predicate swap cannot supply the missing endpoint or reconcile
    consumers.'
  target_ids:
  - habitatmech:GOLD.73051a70cb
  field_paths:
  - source_attestations[0].mapping_predicate
  - grounding_status
  evidence_ids:
  - PREVIOUS
  - PATCH
  - REGRESSION
  - SOURCE
  rule_id: SourceAttestation.mapping_predicate endpoint contract
  native_severity: major
  normalization_reason: Native severity agrees with the shared record-review rubric.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T024348Z-amniotic_fluid__ff65cb2e-record
    finding_id: F2
  disposition_reason: The separate confirmed contract or historical provenance defect
    remains; the scoped parent/synonym correction does not repair it.
actions:
- action_id: ACT2
  description: Resolve the existing shared mapping-endpoint contract before claiming
    SSSOM/KGX conformance. Represent source, record and ontology endpoints explicitly
    and audit actual consumers; do not apply a global narrow/broad predicate replacement.
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.73051a70cb
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained curation input or implementation; never patch generated habitat
      YAML
  acceptance_checks:
  - Test subject, predicate, object and grounding meaning for retained-mint and exact
    routes, including this witness; inspect actual exports against current kg-microbe
    modeling.
  - Preserve exact source IDs, paths, counts and units; compare affected descendants
    and unrelated records, not only the target label.
  - Append a new session history for any separately authorized curation; never rewrite
    saved reviews or previous session records.
  - Run schema/strict, history, provenance, exact corpus reproduction, causal, term-request
    and configured label gates, then just qc.
  - Check actual semantic-input changes and regenerate map/site/redirect products
    through supported tooling when required; save an immutable successor with exact
    finding lineage.
  generator: just seed; inspect the affected just seed-canary output before authorized
    regeneration
limitations:
- Same-agent scientific reassessment, not independent approval.
- Original source-member evidence remains unavailable; no full-corpus, species-occurrence
  or SSSOM/KGX readiness certification.
- Configured label correspondence skips 2061 no-adapter pairs. Final retained-archive
  and protected publication gates are pending at this observation.
- The unresolved F2 finding remains open; this is not a clean-record verdict.
notes:
- The native inspector captured current inputs after remediation; each hash was verified
  against exact committed blobs and disk bytes before saving. This is a review of
  that exact commit. Preserve its off-main base with an annotated remote provenance
  tag before squash and branch deletion.
- All original review and history files remain immutable. New curation events and
  four session histories document the bounded changes; no status is promoted by review.
tags:
- individual-scientific-review
- host-associated
- read-only
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261015T024348Z-amniotic_fluid__ff65cb2e-record
  relationship: Exact finding remediation successor retaining every affected predecessor
    target
```
