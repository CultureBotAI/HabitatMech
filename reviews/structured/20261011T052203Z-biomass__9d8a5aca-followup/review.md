# Bounded correction follow-up: Biomass

- Review: 20261011T052203Z-biomass__9d8a5aca-followup
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-11T05:21:41.229764Z
- Finished UTC: 2026-10-11T05:22:03.383754Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The guarded exclusion resolves F2 by removing only the anaerobic-zone context parent. Organic-material genus, source identity and observations are unchanged. Mapping-endpoint F1 remains open under #1398.

## Scope And Provenance

Reassess all predecessor findings after a bounded correction; preserve prior scope limits.

Selection: Exact corrected target in PR1906, not a new corpus sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 34085e4cd2153e2c1273e0a5172ba48aae55312c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.497ed1acca | data/habitats/engineered/biomass__9d8a5aca.yaml | generated | Biomass |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Post-correction native check | passed | True | habitatmech:GOLD.497ed1acca | Started 2026-10-11T05:21:47.193471+00:00; completed 2026-10-11T05:21:50.412721+00:00. No issues found |
| Post-correction native check | passed | True | habitatmech:GOLD.497ed1acca | Started 2026-10-11T05:21:50.412808+00:00; completed 2026-10-11T05:21:53.542733+00:00. No issues found |
| Post-correction native check | passed | True | habitatmech:GOLD.497ed1acca | Started 2026-10-11T05:21:53.542814+00:00; completed 2026-10-11T05:21:56.180790+00:00. No issues found |
| Post-correction native check | passed | True | habitatmech:GOLD.497ed1acca | Started 2026-10-11T05:21:56.180852+00:00; completed 2026-10-11T05:22:03.383669+00:00. .................                                                        [100%]<br>17 passed in 6.16s |

## Scientific And Domain Assessments

### Bounded corrected semantics

grounding: supported. Targets: habitatmech:GOLD.497ed1acca.

The guarded exclusion resolves F2 by removing only the anaerobic-zone context parent. Organic-material genus, source identity and observations are unchanged. Mapping-endpoint F1 remains open under #1398.

### Remaining finding

representation: concern. Targets: habitatmech:GOLD.497ed1acca.

One predecessor finding remains open; deterministic gates do not settle it.

## Findings

### F1: Retained source identity carries a narrow mapping to an implicit endpoint

major / open / confirmed; issue key: habitatmech-gold.497ed1acca-mapping-endpoint-contract.

The GOLD path mints habitatmech:GOLD.497ed1acca, which is also the generated record identifier. Its narrowMatch compares implicitly with the broader ontology term, but SourceAttestation.mapping_predicate declares source concept to record identifier and omission when they coincide. This is a local endpoint-contract mismatch, not a claim that SKOS formally prohibits reflexive mappings. Preserve qualified identity and genuine genus; do not merely invert broad/narrow or exact-merge the record.

Disposition: The bounded correction does not resolve this finding; retain the original scope and uncertainty.

### F2: Source context is not an established habitat genus: Anaerobic zone

major / resolved / confirmed; issue key: habitatmech-gold.497ed1acca-context-parent.

The guarded exclusion resolves F2 by removing only the anaerobic-zone context parent. Organic-material genus, source identity and observations are unchanged. Mapping-endpoint F1 remains open under #1398.

Disposition: The guarded exclusion resolves F2 by removing only the anaerobic-zone context parent. Organic-material genus, source identity and observations are unchanged. Mapping-endpoint F1 remains open under #1398.

## Recommended Actions And Acceptance Checks

### A1

Resolve #1398 across actual mapping endpoints, schema, emitters and consumers without merging source-qualified identities or globally swapping predicates.

- Save linked successor dispositions with inspected evidence.
- Run relevant native schema, reproduction, graph and export tests before closing findings.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| CURRENT | data/habitats/engineered/biomass__9d8a5aca.yaml; Complete post-correction record and diff against c287909e97d2953317a72ec85ec77dc5a43b7ea3 | supports | The guarded exclusion resolves F2 by removing only the anaerobic-zone context parent. Organic-material genus, source identity and observations are unchanged. Mapping-endpoint F1 remains open under #1398. |
| PRIOR | reviews/structured/20261011T051114Z-biomass__9d8a5aca/review.yaml; All findings; original evidence and limitations | supports | Immutable predecessor; original broad assessment is not relabeled as a fresh full-record review. |
| FIX | curation/gold_parent_exclusions.tsv; Exact target-owned changes | supports | Maintained inputs preserve unrelated source claims. Generated target differs only in graph/parent and appended audit events. |
| RULES | src/habitatmech/schema/habitatmech.yaml; CausalNodeTypeEnum; SourceAttestation.mapping_predicate; docs/CURATION.md strict parent rule | supports | COMMUNITY is an assemblage, TAXON an organism/clade, COMMUNITY_PROCESS an activity; parent_habitats means is-a and source mappings require explicit endpoint semantics. |
| TEST | tests/test_biomass_bioreactor_review_fixes.py; All four tests, plus 13 graph/renderer tests | supports | 17 focused tests pass: full-corpus hierarchy isolation, preserved source fields/status, community renderer/schema acceptance, conditional operating scope and carbon/electron roles. Fresh strict, reproduction, overlay and history checks also passed before saving; final map/site/QC results are reported on the PR. |
| SPETH | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4821891/fullTextXML; Retained XML; introduction, biomass fraction descriptions and sampling methods | supports | Reinspected paper separates granular/flocculent biomass from reactor niches; it is not an original GOLD node-to-study crosswalk. |

## Limits And Additional Notes

- Adversarial self-review, not independent approval.
- Original frozen GOLD membership remains unreconstructed; later snapshots are not a replacement.
- Ontology label checks retain no-adapter skips. No SSSOM/KGX readiness claim.
- Full publication QC and map/site validation are reported separately on PR1906.
- Shared mapping endpoint mismatch remains under #1398.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T052203Z-biomass__9d8a5aca-followup
kind: record
repository: culturebotai/HabitatMech
title: 'Bounded correction follow-up: Biomass'
started_at: '2026-10-11T05:21:41.229764Z'
finished_at: '2026-10-11T05:22:03.383754Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent performed curation; not independent scientific approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'The guarded exclusion resolves F2 by removing only the anaerobic-zone context
  parent. Organic-material genus, source identity and observations are unchanged.
  Mapping-endpoint F1 remains open under #1398.'
source:
  git_revision: 34085e4cd2153e2c1273e0a5172ba48aae55312c
  state: working_tree
  inputs:
  - path: curation/causal_graphs/bioreactor.yaml
    sha256: 170d1134c3de38348844e45dbf6d87663dd4a0d1f33fd9e441a4352b6e277583
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 4a8150d842452267f80310ea3974346c0a01a9c432273d409cc68499a51b30e8
    role: context
  - path: data/habitats/engineered/biomass__9d8a5aca.yaml
    sha256: 3aa7fb4ace4e1b647c408d82fb8209b71286c3e3c496fac0402cb4e642ae62df
    role: target
  - path: docs/CURATION.md
    sha256: 36df8306394c06c352b73e0bf7b47a2858784cedac7389a24d0b78f593ece646
    role: context
  - path: reviews/structured/20261011T051114Z-biomass__9d8a5aca/review.yaml
    sha256: 5964503473537b83be7961221d1d71a648d11593c44b8bb356da75f0f0e0e4ad
    role: context
  - path: scripts/mechanism_graph.py
    sha256: 20684d7982b8e44ca2a64c8c697fde3cac192325b235a4109f60632314846592
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/seed.py
    sha256: 4adf105e23d75c3563a516a0c160623d1065df7fcb2f31b7a0a0a8303d0401be
    role: context
  - path: tests/test_biomass_bioreactor_review_fixes.py
    sha256: bc9421da3893b3440df219f0dd324a5c16bf0dbf758cef74bfa216e42066ada6
    role: context
targets:
- target_id: habitatmech:GOLD.497ed1acca
  path: data/habitats/engineered/biomass__9d8a5aca.yaml
  label: Biomass
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: Exact source-concept identity and grounding decisions
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded immediate GOLD context-parent exclusions
  - repository: culturebotai/HabitatMech
    path: curation/term_requests.tsv
    role: Authored habitat definitions and genus
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained harmonization and generation
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen GOLD concepts and ORGANISM counts
scope:
  description: Reassess all predecessor findings after a bounded correction; preserve
    prior scope limits.
  selection: Exact corrected target in PR1906, not a new corpus sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.497ed1acca
  exclusions:
  - target: Unchanged record biology and other 3207 records
    reason: Compared for preservation; not independently re-certified scientifically.
checks:
- check_id: C0
  name: Post-correction native check
  command: just validate data/habitats/engineered/biomass__9d8a5aca.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Started 2026-10-11T05:21:47.193471+00:00; completed 2026-10-11T05:21:50.412721+00:00.
    No issues found
  target_ids:
  - habitatmech:GOLD.497ed1acca
- check_id: C1
  name: Post-correction native check
  command: just validate data/habitats/engineered/bioreactor.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Started 2026-10-11T05:21:50.412808+00:00; completed 2026-10-11T05:21:53.542733+00:00.
    No issues found
  target_ids:
  - habitatmech:GOLD.497ed1acca
- check_id: C2
  name: Post-correction native check
  command: just validate-causal curation/causal_graphs/bioreactor.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Started 2026-10-11T05:21:53.542814+00:00; completed 2026-10-11T05:21:56.180790+00:00.
    No issues found
  target_ids:
  - habitatmech:GOLD.497ed1acca
- check_id: C3
  name: Post-correction native check
  command: .venv/bin/pytest -q tests/test_biomass_bioreactor_review_fixes.py tests/test_causal_graph_curations.py
    tests/test_mechanism_graph.py
  status: passed
  required: true
  exit_code: 0
  summary: 'Started 2026-10-11T05:21:56.180852+00:00; completed 2026-10-11T05:22:03.383669+00:00.
    .................                                                        [100%]

    17 passed in 6.16s'
  target_ids:
  - habitatmech:GOLD.497ed1acca
evidence:
- evidence_id: CURRENT
  kind: record_content
  reference: data/habitats/engineered/biomass__9d8a5aca.yaml
  locator: Complete post-correction record and diff against c287909e97d2953317a72ec85ec77dc5a43b7ea3
  summary: 'The guarded exclusion resolves F2 by removing only the anaerobic-zone
    context parent. Organic-material genus, source identity and observations are unchanged.
    Mapping-endpoint F1 remains open under #1398.'
  accessed_at: '2026-10-11T05:22:03.383754Z'
  support: supports
- evidence_id: PRIOR
  kind: prior_review
  reference: reviews/structured/20261011T051114Z-biomass__9d8a5aca/review.yaml
  locator: All findings; original evidence and limitations
  summary: Immutable predecessor; original broad assessment is not relabeled as a
    fresh full-record review.
  accessed_at: '2026-10-11T05:22:03.383754Z'
  support: supports
- evidence_id: FIX
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact target-owned changes
  summary: Maintained inputs preserve unrelated source claims. Generated target differs
    only in graph/parent and appended audit events.
  accessed_at: '2026-10-11T05:22:03.383754Z'
  support: supports
- evidence_id: RULES
  kind: record_content
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: CausalNodeTypeEnum; SourceAttestation.mapping_predicate; docs/CURATION.md
    strict parent rule
  summary: COMMUNITY is an assemblage, TAXON an organism/clade, COMMUNITY_PROCESS
    an activity; parent_habitats means is-a and source mappings require explicit endpoint
    semantics.
  accessed_at: '2026-10-11T05:22:03.383754Z'
  support: supports
- evidence_id: TEST
  kind: validation
  reference: tests/test_biomass_bioreactor_review_fixes.py
  locator: All four tests, plus 13 graph/renderer tests
  summary: '17 focused tests pass: full-corpus hierarchy isolation, preserved source
    fields/status, community renderer/schema acceptance, conditional operating scope
    and carbon/electron roles. Fresh strict, reproduction, overlay and history checks
    also passed before saving; final map/site/QC results are reported on the PR.'
  accessed_at: '2026-10-11T05:22:03.383754Z'
  support: supports
- evidence_id: SPETH
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4821891/fullTextXML
  locator: Retained XML; introduction, biomass fraction descriptions and sampling
    methods
  summary: Reinspected paper separates granular/flocculent biomass from reactor niches;
    it is not an original GOLD node-to-study crosswalk.
  accessed_at: '2026-10-11T05:22:03.383754Z'
  support: supports
assessments:
- assessment_id: A1
  area: grounding
  topic: Bounded corrected semantics
  outcome: supported
  summary: 'The guarded exclusion resolves F2 by removing only the anaerobic-zone
    context parent. Organic-material genus, source identity and observations are unchanged.
    Mapping-endpoint F1 remains open under #1398.'
  target_ids:
  - habitatmech:GOLD.497ed1acca
  evidence_ids:
  - CURRENT
  - PRIOR
  - FIX
  - RULES
  - TEST
  - SPETH
- assessment_id: A2
  area: representation
  topic: Remaining finding
  outcome: concern
  summary: One predecessor finding remains open; deterministic gates do not settle
    it.
  target_ids:
  - habitatmech:GOLD.497ed1acca
  evidence_ids:
  - PRIOR
  - CURRENT
  - RULES
findings:
- finding_id: F1
  issue_key: habitatmech-gold.497ed1acca-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Retained source identity carries a narrow mapping to an implicit endpoint
  description: The GOLD path mints habitatmech:GOLD.497ed1acca, which is also the
    generated record identifier. Its narrowMatch compares implicitly with the broader
    ontology term, but SourceAttestation.mapping_predicate declares source concept
    to record identifier and omission when they coincide. This is a local endpoint-contract
    mismatch, not a claim that SKOS formally prohibits reflexive mappings. Preserve
    qualified identity and genuine genus; do not merely invert broad/narrow or exact-merge
    the record.
  target_ids:
  - habitatmech:GOLD.497ed1acca
  field_paths:
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - CURRENT
  - PRIOR
  - FIX
  - RULES
  - TEST
  - SPETH
  rule_id: docs/CURATION.md; docs/record-review-profile.md
  native_severity: major
  normalization_reason: Material semantic or evidence defect requiring maintained-input
    correction.
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Mapping emission and source resolution
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Declared mapping endpoints
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
  previous_occurrences:
  - repository: culturebotai/HabitatMech
    review_id: 20261011T051114Z-biomass__9d8a5aca
    finding_id: F1
  disposition_reason: The bounded correction does not resolve this finding; retain
    the original scope and uncertainty.
- finding_id: F2
  issue_key: habitatmech-gold.497ed1acca-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: 'Source context is not an established habitat genus: Anaerobic zone'
  description: 'The guarded exclusion resolves F2 by removing only the anaerobic-zone
    context parent. Organic-material genus, source identity and observations are unchanged.
    Mapping-endpoint F1 remains open under #1398.'
  target_ids:
  - habitatmech:GOLD.497ed1acca
  field_paths:
  - parent_habitats[habitatmech:GOLD.9f519b94cc]
  evidence_ids:
  - CURRENT
  - PRIOR
  - FIX
  - RULES
  - TEST
  - SPETH
  rule_id: docs/CURATION.md; docs/record-review-profile.md
  native_severity: major
  normalization_reason: Material semantic or evidence defect requiring maintained-input
    correction.
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact path and expected-parent guard
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: Source-scope adjudication
  previous_occurrences:
  - repository: culturebotai/HabitatMech
    review_id: 20261011T051114Z-biomass__9d8a5aca
    finding_id: F2
  disposition_reason: 'The guarded exclusion resolves F2 by removing only the anaerobic-zone
    context parent. Organic-material genus, source identity and observations are unchanged.
    Mapping-endpoint F1 remains open under #1398.'
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1907
actions:
- action_id: A1
  description: 'Resolve #1398 across actual mapping endpoints, schema, emitters and
    consumers without merging source-qualified identities or globally swapping predicates.'
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.497ed1acca
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Mapping emission and source resolution
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Declared mapping endpoints
  acceptance_checks:
  - Save linked successor dispositions with inspected evidence.
  - Run relevant native schema, reproduction, graph and export tests before closing
    findings.
limitations:
- Adversarial self-review, not independent approval.
- Original frozen GOLD membership remains unreconstructed; later snapshots are not
  a replacement.
- Ontology label checks retain no-adapter skips. No SSSOM/KGX readiness claim.
- Full publication QC and map/site validation are reported separately on PR1906.
- 'Shared mapping endpoint mismatch remains under #1398.'
related_reviews:
- repository: culturebotai/HabitatMech
  review_id: 20261011T051114Z-biomass__9d8a5aca
  relationship: Reassesses all findings and resolves only the explicitly corrected
    subset
links:
- https://github.com/CultureBotAI/HabitatMech/pull/1906
tags:
- followup
- scientific-review
- engineered
```
