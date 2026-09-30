# YAML Record Review: Multiple systems

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/multiple_systems__74c7f0de.yaml`
- Started UTC: 2026-09-30T14:28:10Z
- Finished UTC: 2026-09-30T14:35:28Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Record | `data/habitats/host_associated/multiple_systems__74c7f0de.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.864a5fdcb7` |
| Label | `Multiple systems` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Maintained/generated | generated from committed source inventories and `curation/decisions.tsv` by `scripts/seed_from_sources.py` |
| Path lock | `data/habitats/PATHS.tsv:2284` pins `habitatmech:GOLD.864a5fdcb7` to `multiple_systems__74c7f0de` |

This is the generated GOLD record for the Fish `Multiple systems` source path.
The source row is an internal GOLD bucket under `Host-associated > Fish` and
above `Multiple organs`; it has no direct GOLD organism, study, or biosample
assertions itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/multiple_systems__74c7f0de.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/habitats/host_associated/multiple_systems__74c7f0de.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 records expected, 3206 found, 0 missing, 0 extra, 0 differing. |
| `just report --out /tmp/habitatmech_multiple_systems_fish_report.tsv` | Passed; the TSV reports this target as `HOST_ASSOCIATED`, `UNGROUNDED`, `SEEDED`, GOLD-attested, definition-free, with 1 parent, 0 parameters, 0 taxa, and 0 causal graphs. |
| `just worklist --status all --out /tmp/habitat_worklist_multiple_systems_fish.tsv` | Passed; wrote 953 ungrounded rows. This target is still listed at row 690 because its only maintained decision is a `CLASS`-depth sweep, not an item-level judgement. |

## Identity and Grounding

The source identity is internally consistent. `data/raw/gold_ecosystem_paths.tsv`
contains the canonical GOLD row `Host-associated > Fish > Multiple systems`
with leaf label `Multiple systems`, depth 3, three GOLD node IDs, zero direct
assertions, and source IDs `gold.ecosystem:6957`, `gold.ecosystem:8466`, and
`gold.ecosystem:8467`. The generated source attestation uses the first node ID
and records that three GOLD ecosystem node IDs share this path.

The `UNGROUNDED` status is supported by the maintained class-level decision at
`curation/decisions.tsv:792`, which records that no vendored term matched this
label by the sweep's lexical search routes. That row deliberately uses
`review_depth: CLASS`, so the record remains `SEEDED` and still appears in
`just worklist` for future item-level curation; it should not be treated as an
ENVO term-request candidate until that review happens.

The single parent is supported:

| Parent | Support | Review |
|---|---|---|
| `habitatmech:GOLD.3d529a667e` | `data/raw/gold_ecosystem_paths.tsv:33` contains the immediate GOLD parent path `Host-associated > Fish`, whose generated, reviewed record is `data/habitats/host_associated/fish.yaml`. | Supported as the source-path parent for fish-associated environments. |

The GOLD hierarchy below this row is also preserved: `data/raw/gold_ecosystem_paths.tsv:1943`
contains the immediate child `Host-associated > Fish > Multiple systems >
Multiple organs`, and the generated `data/habitats/host_associated/multiple_organs.yaml`
uses `habitatmech:GOLD.864a5fdcb7` as its source-path parent.

## Evidence

The record has no curator-authored causal graphs, characteristic taxa,
environmental parameters, authored definition, assertion-bearing source path, or
record-level literature evidence, so there are no claim-level citations to
audit.

| Claim | Nearest maintained support | Review |
|---|---|---|
| GOLD has a Fish `Multiple systems` source path with three upstream node IDs. | `data/raw/gold_ecosystem_paths.tsv:1942` | Supported exactly. |
| The Fish `Multiple systems` path has zero organism, study, biosample, and total assertions. | `data/raw/gold_ecosystem_paths.tsv:1942` | Supported exactly; exact side-table searches found no direct rows for this parent path, and the generated attestation correctly omits `assertion_count` instead of serializing zero. |
| The record reflects a class-level ungrounded sweep, not an item-level review. | `curation/decisions.tsv:792`; generated `curation_history` in the target YAML | Supported exactly. |
| The Fish `Multiple systems` row follows a host-specific GOLD bucket pattern also present under Mammals and Insects. | `data/raw/gold_ecosystem_paths.tsv:272`, `:1825`, and `:1942`; generated `multiple_systems.yaml` and `multiple_systems__6d931d99.yaml` | Supported exactly. |

The rendered page
`pages/habitats/multiple-systems-habitatmech-gold-864a5fdcb7.html` reflects
the same identifier, `HOST_ASSOCIATED` category, `UNGROUNDED` grounding,
`SEEDED` mapping status, single GOLD source attestation, fish-associated parent,
and class-level curation note as the generated YAML.

Unsupported or over-scoped claims: None found.

## Completeness

The generated record is complete for the maintained inputs currently available:

- The minted identifier, GOLD label, representative source ID, multi-node note,
  and source path are present.
- The source-path parent to `fish-associated environment` is present.
- The class-level sweep is reflected as `UNGROUNDED` without promoting
  `mapping_status` to `REVIEWED`.
- The record correctly has no serialized `assertion_count`, definition,
  characteristic taxa, environmental parameters, causal graphs, datasets,
  discussion links, or record-level literature evidence.
- iModulonDB was not applicable because this source bucket names no gene, locus,
  regulator, transcriptomic dataset, or strain-level expression claim.

Exact ignored/hidden-inclusive searches for the Fish source path, all three
GOLD node IDs, `habitatmech:GOLD.864a5fdcb7`, and
`multiple_systems__74c7f0de` covered `data/raw`, `data/habitats/PATHS.tsv`, the
target YAML, `pages/habitats`, `curation`, `history`, `research`, and
`reports/yaml_record_review`. They found the cited raw row, class-level
decision, path lock, generated record, rendered page, and generated Multiple
organs child; they found no maintained term request, causal-graph overlay,
history record, target-specific research report, or prior exact
`multiple_systems__74c7f0de` review report. Exact ignored/hidden-inclusive
searches of `data/raw/gold_path_biosamples.tsv`,
`data/raw/gold_path_triads.tsv`, and `data/raw/gold_studies.tsv` found no
direct Fish `Multiple systems` rows, matching the empty optional slots in the
generated YAML.

## Findings

None found.

No blocker findings.

No major findings.

No minor findings.

## Recommended Edits

None required.

If a future curator wants to promote this seeded record to reviewed status,
replace the existing `CLASS`-depth decision for `habitatmech:GOLD.864a5fdcb7`
with an item-level `CONFIRM_UNGROUNDED` or `NOT_APPLICABLE` decision, rerun
`just seed`, and canary `habitatmech:GOLD.864a5fdcb7`. Keep the Fish
source-path parent unchanged unless the committed GOLD inventory changes.

## Follow-up Checks

None required beyond the validators already run for this report.

For any future item-level review row, run:

- `just seed`
- `just seed-canary habitatmech:GOLD.864a5fdcb7`
- `just validate data/habitats/host_associated/multiple_systems__74c7f0de.yaml`
- `just validate-strict data/habitats/host_associated/multiple_systems__74c7f0de.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`
- `git diff --check`

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -name '*multiple_systems__74c7f0de.md' -print` found no pre-existing exact target report, and `find` included ignored files under the searched directory.
- `just report --out /tmp/habitatmech_multiple_systems_fish_report.tsv` reported this record at TSV row 2284 as `habitatmech:GOLD.864a5fdcb7	Multiple systems	HOST_ASSOCIATED	UNGROUNDED	SEEDED	GOLD	1	0	False	1	0	0	0	data/habitats/host_associated/multiple_systems__74c7f0de.yaml`.
- `just worklist --status all --out /tmp/habitat_worklist_multiple_systems_fish.tsv` reported this record at TSV row 690 as `habitatmech:GOLD.864a5fdcb7	Multiple systems	HOST_ASSOCIATED	0	GOLD	Host-associated > Fish > Multiple systems	TRUE	UBERON:0000383=muscle system`.
