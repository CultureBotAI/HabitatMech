# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/engineered/plastic_debries.yaml`
- Started UTC: 2026-09-28T16:34:58Z
- Finished UTC: 2026-09-28T16:34:59Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| File | `data/habitats/engineered/plastic_debries.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.293873d837` |
| Label | `Plastic debries` |
| Category | `ENGINEERED` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |
| Maintained/generated | Generated from `data/raw/` plus curation inputs |

The record is the generated GOLD leaf for `Engineered > Solid waste > Debries >
Marine debries > Plastic debries`, a zero-assertion branch under the marine
half of GOLD's misspelled Debries subtree. It has the simple `plastic_debries`
slug because its same-label freshwater sibling is disambiguated as
`plastic_debries__693ff27d`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/engineered/plastic_debries.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/engineered/plastic_debries.yaml` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated. |
| `just verify-corpus` | Passed; expected and found 3206 records, with 0 missing, 0 extra, and 0 differing records. |
| `just worklist --status all --out /tmp/habitatmech-plastic-debries-marine-worklist.tsv` | Passed; wrote 953 ungrounded rows. Row 763 reports this target as a decided `ENGINEERED` GOLD concept with zero generated assertions and only weak lexical candidates such as `ENVO:06105009` `plastic line`, its `plastic fibre` synonym, `ENVO:06105007` `plastic membrane`, and `ENVO:01000732` `clastic dike`. |
| `just report --out /tmp/habitatmech-plastic-debries-marine-report.tsv` | Passed; row 1590 reports this target as an `ENGINEERED` `UNGROUNDED`/`SEEDED` GOLD-only record with one source, zero generated assertions, one parent, no definition, no environmental parameters, no characteristic taxa, and no causal graph. |

## Identity and Grounding

The generated identity is reproducible and is locked to the simple
`plastic_debries` slug:

| Source | Evidence |
|---|---|
| `data/raw/gold_ecosystem_paths.tsv:1358` | Exact path `Engineered > Solid waste > Debries > Marine debries > Plastic debries`, leaf label `Plastic debries`, depth `5`, one GOLD ecosystem node, zero organisms, zero studies, zero biosamples, zero total assertions, and node id `gold.ecosystem:8353`. |
| `data/habitats/PATHS.tsv:1590` | `habitatmech:GOLD.293873d837` maps to `plastic_debries`, matching the reviewed YAML path. |
| `curation/decisions.tsv:322` | `habitatmech:GOLD.293873d837` has only a class-level `CONFIRM_UNGROUNDED` row. |

The generated parent, `habitatmech:GOLD.c9f6be7c10`, is supported only as the
immediate GOLD source-path parent. `data/raw/gold_ecosystem_paths.tsv:1357`
records the parent path `Engineered > Solid waste > Debries > Marine debries`,
and `data/habitats/PATHS.tsv:2771` pins that parent to slug
`marine_debries`.

The identical generated sibling label is not an accidental duplicate. The
sibling `data/habitats/engineered/plastic_debries__693ff27d.yaml` is
`habitatmech:GOLD.b39df834b2` from `Engineered > Solid waste > Debries >
Freshwater debries > Plastic debries`; this target is the `gold.ecosystem:8353`
leaf under `Marine debries`.

The current `UNGROUNDED` state is still a lexical no-match placeholder. The
class-level sweep did not read the GOLD path, did not judge whether `Plastic
debries` is GOLD's spelling variant for plastic debris, and did not compare
the exact marine plastic-debris concept against vendored broader terms such
as `ENVO:00002264` `waste material` and `mesh:D062611` `Solid Waste`.

## Evidence

| Claim | Evidence checked | Assessment |
|---|---|---|
| This record represents the marine `Plastic debries` GOLD leaf. | The exact source path appears in `data/raw/gold_ecosystem_paths.tsv` only on row 1358, and the generated YAML copies its leaf label, `gold.ecosystem:8353`, and full source path. | Supported. |
| The record has no upstream GOLD assertion count. | The raw GOLD row reports zero organism, study, biosample, and total assertions; the exact full source path is absent from the other committed GOLD raw side tables searched here. | Supported. |
| `parent_habitats: habitatmech:GOLD.c9f6be7c10` is the source-path parent. | The source path's immediate parent is `Engineered > Solid waste > Debries > Marine debries`, which resolves to `habitatmech:GOLD.c9f6be7c10` / `marine_debries`. | Supported as generated source hierarchy. |
| The target already has item-level curation. | `curation/decisions.tsv:322` has `review_depth` `CLASS`; hidden/ignored-inclusive fixed-string searches found no exact target term request, term-request exclusion, external xref, causal overlay, habitat-research report, or history record. | Unsupported. |
| A corrected `marine plastic debris` concept already exists in maintained inputs. | Corrected-spelling searches found `plastic debris` only in an ontology definition for `ENVO:01000946` `secondary microplastic particle` and in the freshwater duplicate review, but no exact vendored marine-plastic-debris term, target-specific term request, exclusion, or xref. | Unsupported. |
| Existing Debries-subtree reviews solve this leaf. | The `Debries`, `Marine debries`, and freshwater `Plastic debries` reviews all flag this small subtree for future item-level review, but none is a maintained curation input for `habitatmech:GOLD.293873d837`. | Unsupported. |

Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.293873d837`,
`gold.ecosystem:8353`, and `plastic_debries` found no maintained term request,
term-request exclusion, external xref, causal overlay, append-only history
record, or habitat-research report.

An exact hidden/ignored-inclusive fixed-string search for `Engineered > Solid
waste > Debries > Marine debries > Plastic debries` across `data/raw`,
`data/habitats`, `curation`, `history`, `research`, `reports`, `docs`, `conf`,
`src`, `tests`, `README.md`, `justfile`, and `Justfile` found only the raw GOLD
aggregate row, the generated target YAML, and contextual mentions in the
freshwater `Plastic debries` and `Marine debries` YAML reviews.

## Completeness

The YAML is structurally complete for its current input state. It records the
single GOLD node id, the full GOLD source path, the generated immediate parent,
and curation-history entries for the class-level `CONFIRM_UNGROUNDED` decision
and source seed.

The empty definition, synonyms, xrefs, environmental parameters,
characteristic taxa, evidence, causal graphs, discussions, and datasets are
expected for a zero-assertion GOLD leaf with no target-specific research or
item-level curation. They are not enough to prove the biological scope is
finished: this leaf still needs an item-level decision that reads `Plastic
debries` through the surrounding marine debris path and the duplicate
freshwater plastic-debris sibling.

Before this report was written,
`find reports/yaml_record_review -maxdepth 1 -type f -name '*-plastic_debries.md' -print`
returned no prior exact marine `Plastic debries` YAML review. `find` included
ignored files under `reports/yaml_record_review`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | None found | The YAML validates, reproduces from committed inputs, preserves the exact `gold.ecosystem:8353` source node, and disambiguates the duplicate `Plastic debries` labels through its `PATHS.tsv` slug. | Not applicable |
| Major | The marine `Plastic debries` leaf is backed only by a class-level `CONFIRM_UNGROUNDED` row, so the generated `UNGROUNDED` state has not been item-reviewed against GOLD's apparent debris spelling variant, its duplicate freshwater sibling, or the vendored waste-material hierarchy. | `curation/decisions.tsv:322` has `review_depth` `CLASS`; `data/raw/gold_ecosystem_paths.tsv:1358` shows a one-node, zero-assertion leaf under `Marine debries`; `data/raw/gold_ecosystem_paths.tsv:1356` shows the duplicate `Plastic debries` leaf under `Freshwater debries`; and `data/raw/ontology_terms.tsv` vendors `ENVO:00002264` `waste material` and `mesh:D062611` `Solid Waste` but no exact marine-plastic-debris term. | `curation/decisions.tsv`; if the record stays minted and deserves a definition, `curation/term_requests.tsv` |
| Minor | None found | No non-blocking style, provenance, or schema issue was found. | Not applicable |

## Recommended Edits

1. Item-review `habitatmech:GOLD.293873d837` in
   `curation/decisions.tsv`. Treat `Engineered > Solid waste > Debries >
   Marine debries > Plastic debries` as an exact GOLD source concept, not as a
   bare duplicate `Plastic debries` label.
2. Decide whether the freshwater and marine `Plastic debries` leaves should
   stay as two minted records or be merged. Their labels match, but their
   source-path parents encode distinct freshwater and marine contexts.
3. Compare `ENVO:00002264` `waste material`, `mesh:D062611` `Solid Waste`, and
   the generated `Marine debries` parent against the exact leaf. If the leaf
   remains minted, decide whether an `ENVO:00002264` direct parent or a
   term-request definition for `marine plastic debris` is warranted.

## Follow-up Checks

After item-level curation, rerun:

1. `just seed`
2. `just seed-canary habitatmech:GOLD.293873d837`
3. `just validate data/habitats/engineered/plastic_debries.yaml`
4. `just validate-strict data/habitats/engineered/plastic_debries.yaml`
5. `just validate-causal-all`
6. `just term-requests-check`
7. `just validate-history`
8. `just verify-corpus`
9. `just report --out /tmp/habitatmech-plastic-debries-marine-report.tsv`
10. `git diff --check`

## Additional Notes

The existing `Debries`, `Marine debries`, and freshwater `Plastic debries`
YAML reviews correctly identify this misspelled zero-assertion GOLD subtree as
a curation target. This report narrows that finding to the exact marine
plastic leaf represented by `gold.ecosystem:8353`.
