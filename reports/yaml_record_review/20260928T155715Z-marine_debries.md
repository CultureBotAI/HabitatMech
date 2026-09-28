# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/engineered/marine_debries.yaml`
- Started UTC: 2026-09-28T15:57:15Z
- Finished UTC: 2026-09-28T15:57:15Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| File | `data/habitats/engineered/marine_debries.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.c9f6be7c10` |
| Label | `Marine debries` |
| Category | `ENGINEERED` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |
| Maintained/generated | Generated from `data/raw/` plus curation inputs |

The record is the generated GOLD node for `Engineered > Solid waste > Debries >
Marine debries`, a zero-assertion branch under GOLD's misspelled Debries
subtree. Its generated child is the marine `Plastic debries` leaf at
`Engineered > Solid waste > Debries > Marine debries > Plastic debries`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/engineered/marine_debries.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/engineered/marine_debries.yaml` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated. |
| `just verify-corpus` | Passed; expected and found 3206 records, with 0 missing, 0 extra, and 0 differing records. |
| `just worklist --status all --out /tmp/habitatmech-marine-debries-worklist.tsv` | Passed; wrote 953 ungrounded rows. Row 655 reports this target as a decided `ENGINEERED` GOLD concept with zero generated assertions and only marine-token lexical candidates such as `ENVO:00000447` `marine biome`, `ENVO:01001378` `marine bed`, `ENVO:01000143` `marine reef`, and `ENVO:06105013` `marine life`. |
| `just report --out /tmp/habitatmech-marine-debries-report.tsv` | Passed; row 2771 reports this target as an `ENGINEERED` `UNGROUNDED`/`SEEDED` GOLD-only record with one source, zero generated assertions, one parent, no definition, no environmental parameters, no characteristic taxa, and no causal graph. |

## Identity and Grounding

The generated identity is reproducible from the raw GOLD path:

| Source | Evidence |
|---|---|
| `data/raw/gold_ecosystem_paths.tsv:1357` | Exact path `Engineered > Solid waste > Debries > Marine debries`, leaf label `Marine debries`, depth `4`, two collapsed GOLD ecosystem node ids, zero organisms, zero studies, zero biosamples, zero total assertions, and node ids `gold.ecosystem:8349|gold.ecosystem:8350`. |
| `data/habitats/PATHS.tsv:2771` | `habitatmech:GOLD.c9f6be7c10` maps to slug `marine_debries`, matching the reviewed YAML path. |
| `curation/decisions.tsv:1122` | `habitatmech:GOLD.c9f6be7c10` has only a class-level `CONFIRM_UNGROUNDED` row. |

The generated parent, `habitatmech:GOLD.4e8bd5f6aa`, is supported only as the
immediate GOLD source-path parent. `data/raw/gold_ecosystem_paths.tsv:1354`
records the broader path `Engineered > Solid waste > Debries`, and
`data/habitats/PATHS.tsv:1866` pins that generated parent to the `debries`
slug.

The generated child, `habitatmech:GOLD.293873d837`, is the separate marine
`Plastic debries` leaf. `data/raw/gold_ecosystem_paths.tsv:1358` records one
zero-assertion GOLD node, `gold.ecosystem:8353`, at `Engineered > Solid waste >
Debries > Marine debries > Plastic debries`, and
`data/habitats/PATHS.tsv:1590` pins it to the simple `plastic_debries` slug.

The current `UNGROUNDED` state is still a lexical no-match placeholder. The
class-level sweep did not read the GOLD path, did not judge whether `Marine
debries` is GOLD's spelling variant for marine debris, and did not compare the
exact marine-debris concept against the generated `Debries` parent or broader
vendored terms such as `ENVO:00002264` `waste material` and `mesh:D062611`
`Solid Waste`.

## Evidence

| Claim | Evidence checked | Assessment |
|---|---|---|
| This record represents the marine `Debries` GOLD node. | The exact source path appears in `data/raw/gold_ecosystem_paths.tsv` only on row 1357, and the generated YAML copies its leaf label, first GOLD node id, full source path, and two-node collapsed-path note. | Supported. |
| The record has no upstream GOLD assertion count. | The raw GOLD row reports zero organism, study, biosample, and total assertions; the exact full source path is absent from the other committed GOLD raw side tables searched here. | Supported. |
| `parent_habitats: habitatmech:GOLD.4e8bd5f6aa` is the source-path parent. | The source path's immediate parent is `Engineered > Solid waste > Debries`, which resolves to `habitatmech:GOLD.4e8bd5f6aa` / `debries`. | Supported as generated source hierarchy. |
| The generated marine plastic child belongs under this target. | `data/raw/gold_ecosystem_paths.tsv:1358` records `Engineered > Solid waste > Debries > Marine debries > Plastic debries`; `data/habitats/engineered/plastic_debries.yaml` uses `habitatmech:GOLD.c9f6be7c10` as its parent. | Supported as generated source hierarchy. |
| The target already has item-level curation. | `curation/decisions.tsv:1122` has `review_depth` `CLASS`; hidden/ignored-inclusive fixed-string searches found no exact target term request, term-request exclusion, external xref, causal overlay, research report, YAML review, or history record. | Unsupported. |
| A corrected `Marine debris` ontology term already exists in maintained inputs. | Corrected-spelling exact searches found other debris definitions, prior Debries-subtree reports, and marine-rubber-waste term-request context, but no exact vendored marine-debris term, target-specific term request, exclusion, or xref. | Unsupported. |

Exact hidden/ignored-inclusive searches for
`habitatmech:GOLD.c9f6be7c10`, `gold.ecosystem:8349`,
`gold.ecosystem:8350`, and `marine_debries` found no maintained term request,
term-request exclusion, external xref, causal overlay, append-only history
record, habitat-research report, or prior YAML review.

An exact hidden/ignored-inclusive fixed-string search for `Engineered > Solid
waste > Debries > Marine debries` across `data/raw`, `data/habitats`,
`curation`, `history`, `research`, `reports`, `docs`, `conf`, `src`, `tests`,
`README.md`, `justfile`, and `Justfile` found only the raw GOLD aggregate row,
the generated target YAML, the raw marine plastic child row, and the generated
marine plastic child YAML.

## Completeness

The YAML is structurally complete for its current input state. It records the
two collapsed GOLD node ids through `gold.ecosystem:8349`, the full GOLD source
path, the generated immediate parent, and curation-history entries for the
class-level `CONFIRM_UNGROUNDED` decision and source seed.

The empty definition, synonyms, xrefs, environmental parameters,
characteristic taxa, evidence, causal graphs, discussions, and datasets are
expected for a zero-assertion GOLD branch with no target-specific research or
item-level curation. They are not enough to prove the modeling is finished:
this node still needs an item-level decision that reads `Marine debries`
through the surrounding solid-waste path and distinguishes the generated
marine `Plastic debries` leaf from the freshwater duplicate.

Before this report was written,
`find reports/yaml_record_review -maxdepth 1 -type f -name '*marine_debries*.md' -print`
returned no prior exact marine `Debries` YAML review. `find` included ignored
files under `reports/yaml_record_review`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | None found | The YAML validates, reproduces from committed inputs, preserves the two collapsed GOLD node ids, and sits under the generated `Engineered > Solid waste > Debries` source-path parent. | Not applicable |
| Major | The exact `Marine debries` source concept is backed only by a class-level `CONFIRM_UNGROUNDED` row, so the generated `UNGROUNDED` state has not been item-reviewed against GOLD's apparent debris spelling variant, the generated marine plastic child, or the vendored waste-material hierarchy. | `curation/decisions.tsv:1122` has `review_depth` `CLASS`; `data/raw/gold_ecosystem_paths.tsv:1357` shows a two-node, zero-assertion branch under `Debries`; `data/raw/gold_ecosystem_paths.tsv:1358` shows its generated `Plastic debries` child; and `data/raw/ontology_terms.tsv` vendors `ENVO:00002264` `waste material` and `mesh:D062611` `Solid Waste` but no exact marine-debris term. | `curation/decisions.tsv`; if the record stays minted and deserves a definition, `curation/term_requests.tsv` |
| Minor | None found | No non-blocking style, provenance, or schema issue was found. | Not applicable |

## Recommended Edits

1. Item-review `habitatmech:GOLD.c9f6be7c10` in
   `curation/decisions.tsv`. Treat `Engineered > Solid waste > Debries >
   Marine debries` as an exact GOLD source concept, not as the generic word
   `marine`.
2. Compare `ENVO:00002264` `waste material`, `mesh:D062611` `Solid Waste`, and
   the generated `Debries` parent against the exact source concept. If one is
   strictly broader and useful as a direct parent, use `GROUND_AS_PARENT`;
   otherwise keep `CONFIRM_UNGROUNDED` at `ITEM` depth and explain why the
   generated `Debries` hierarchy is sufficient.
3. Decide whether the generated marine `Plastic debries` child is enough
   hierarchy for this empty branch, or whether a maintained definition and term
   request should normalize the source label as `marine debris` while
   preserving GOLD's source spelling.

## Follow-up Checks

After item-level curation, rerun:

1. `just seed`
2. `just seed-canary habitatmech:GOLD.c9f6be7c10`
3. `just validate data/habitats/engineered/marine_debries.yaml`
4. `just validate-strict data/habitats/engineered/marine_debries.yaml`
5. `just validate-causal-all`
6. `just term-requests-check`
7. `just validate-history`
8. `just verify-corpus`
9. `just report --out /tmp/habitatmech-marine-debries-report.tsv`
10. `git diff --check`

## Additional Notes

The existing `Debries`, `Freshwater debries`, and freshwater `Plastic debries`
YAML reviews correctly identify this misspelled zero-assertion GOLD subtree as
a curation target. This report narrows that finding to the exact marine branch
represented by `gold.ecosystem:8349` and `gold.ecosystem:8350`.
