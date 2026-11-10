# Cycle 8 Stage 5 Grouped Remediation Issue Map (`finger`..`free_living_state`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: `8` / `5` / `1` (`resolve_review_findings`)
- **Base Commit (`origin/main`)**: `7c82566b001f676eb0d3c9cc6c905f85a99b8bde`
- **Input Stage 4 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-04/revision-0001/evidence.yaml` (`sha256: d36115934ced616ced1755c2262dea239ddae158d3106b10e3238f187eed3a1e`)
- **Total Intake Findings**: `77` (`17` actionable cohort findings across `13` records + `60` deferred `#1398` findings = `53` carried-forward + `7` new on `foregut__*`, `frass`, and `frass__c029dd2b`)

## Issue Groups

| Group ID | GitHub Issue | Status | Finding Count | Repair Ownership |
| --- | --- | --- | ---: | --- |
| `G-finger-to-free-living-state-identity-grounding-repairs` | [Issue #2334](https://github.com/CultureBotAI/HabitatMech/issues/2334) | `resolved` | 8 | `curation/decisions.tsv`, `curation/term_requests.tsv`, `curation/definition_source_label_exclusions.tsv`, `data/habitats/PATHS.tsv` |
| `G-finger-to-free-living-state-context-parent-repairs` | [Issue #2335](https://github.com/CultureBotAI/HabitatMech/issues/2335) | `resolved` | 8 | `curation/gold_parent_exclusions.tsv` |
| `G-finger-to-free-living-state-synonym-scope-repairs` | [Issue #2336](https://github.com/CultureBotAI/HabitatMech/issues/2336) | `resolved` | 1 | `curation/term_requests.tsv`, `curation/definition_source_label_exclusions.tsv` |
| `G-source-attestation-mapping-endpoint-contract` | [Issue #1398](https://github.com/CultureBotAI/HabitatMech/issues/1398) | `deferred` | 60 | `src/habitatmech/schema/habitatmech.yaml`, `src/habitatmech/seed.py` |
