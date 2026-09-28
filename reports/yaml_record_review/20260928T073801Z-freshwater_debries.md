# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/engineered/freshwater_debries.yaml`
- Started UTC: 2026-09-28T07:38:01Z
- Finished UTC: 2026-09-28T07:38:01Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.4b4124c98a` |
| Label | `Freshwater debries` |
| Category | `ENGINEERED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Generated path | `data/habitats/engineered/freshwater_debries.yaml` |
| GOLD path | `Engineered > Solid waste > Debries > Freshwater debries` |
| Locked slug | `data/habitats/PATHS.tsv:1849` maps `habitatmech:GOLD.4b4124c98a` to `freshwater_debries` |

The target is a generated GOLD-only record for GOLD's misspelled freshwater
debris branch under engineered solid waste. It has one GOLD source attestation,
one generated source-path parent, no definition, no synonyms, no xrefs, no
environmental parameters, no characteristic taxa, no record-local evidence, no
causal graphs, no discussions, and no datasets.

The generated YAML is byte-reproducible from committed inputs. Future fixes
belong in maintained curation inputs, not in
`data/habitats/engineered/freshwater_debries.yaml` or `pages/`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/engineered/freshwater_debries.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/freshwater_debries.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows; wrote `reports/instance_validation_failures.tsv`. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against the vendored history schema. |
| `just verify-corpus` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --status all --out /tmp/habitatmech-freshwater-debries-worklist.tsv` | Passed; wrote 953 ungrounded rows and listed `habitatmech:GOLD.4b4124c98a` at row 562. |
| `just report --out /tmp/habitatmech-freshwater-debries-report.tsv` | Passed; wrote the 3206-record corpus TSV and listed `habitatmech:GOLD.4b4124c98a` at row 1849 with `UNGROUNDED`, `SEEDED`, one source, zero assertions, one parent, no parameters, no taxa, and no causal graphs. |
| `git diff --check` | Passed; no whitespace or patch errors. |
| `git diff --cached --check` | Passed; no staged whitespace or patch errors. |

No validator was skipped.

## Identity and Grounding

The minted identity and GOLD source attestation match the raw path inventory:

- `data/raw/gold_ecosystem_paths.tsv:1355` is the exact raw row for
  `Engineered > Solid waste > Debries > Freshwater debries`. It records leaf
  label `Freshwater debries`, depth `4`, two collapsed GOLD ecosystem node ids,
  zero organism assertions, zero study assertions, zero biosample assertions,
  zero total assertions, and node ids `gold.ecosystem:8351|gold.ecosystem:8352`.
- `data/habitats/PATHS.tsv:1849` pins the generated identifier
  `habitatmech:GOLD.4b4124c98a` to slug `freshwater_debries`, matching the
  reviewed YAML path.
- `curation/decisions.tsv:492` has a `CONFIRM_UNGROUNDED` row for this exact
  minted identifier, but its `review_depth` is only `CLASS`.

The generated parent follows the immediate GOLD source path, not an item-level
curator assertion. `data/raw/gold_ecosystem_paths.tsv:1354` has the broader path
`Engineered > Solid waste > Debries`, and `data/habitats/PATHS.tsv:1866` maps
that parent concept to `habitatmech:GOLD.4e8bd5f6aa` / `debries`. That parent
also has only a class-level `CONFIRM_UNGROUNDED` row at
`curation/decisions.tsv:504`.

The existing `UNGROUNDED` status is not item-level signoff. The class-level
sweep only established that no vendored label matched GOLD's misspelled
`Freshwater debries` string through the automated lexical routes documented in
`docs/HARMONIZATION.md#class-level-sweep`; it explicitly did not decide whether
the GOLD source concept is a habitat, a term-request candidate, or narrower
than a vendored term.

The exact source label appears to be an upstream spelling variant of
`freshwater debris`: GOLD stores sibling paths for `Marine debries` and two
`Plastic debries` leaves in the same five-row zero-assertion subtree, all under
`Engineered > Solid waste > Debries`. `data/raw/ontology_terms.tsv:7340`
vendors `ENVO:00002264` `waste material`, and
`data/raw/ontology_terms.tsv:13610` vendors the exact `mesh:D062611`
`Solid Waste` parent already reached through the generated `Debries` source
parent. Neither term names freshwater debris exactly; item review still needs
to decide whether this empty GOLD grouping node should remain minted and, if
so, whether any additional broader term is warranted.

## Evidence

| Claim | Nearest source | Review |
|---|---|---|
| The record denotes the GOLD path `Engineered > Solid waste > Debries > Freshwater debries`. | `data/raw/gold_ecosystem_paths.tsv:1355` lists the same canonical path and leaf label; the generated YAML repeats both. | Supported exactly. |
| The source attestation uses `gold.ecosystem:8351` and notes that two GOLD ecosystem node ids share the path. | The raw aggregate row lists `gold.ecosystem:8351|gold.ecosystem:8352`; the seeder records the first id and a collapsed-node note. | Supported exactly. |
| The source attestation omits `assertion_count` and `assertion_unit`. | The raw aggregate row records `organism_count`, `study_count`, `biosample_count`, and `total_assertions` as `0`. | Supported exactly. |
| `Freshwater debries` is narrower than the `Debries` source-path parent. | `data/raw/gold_ecosystem_paths.tsv:1354` and `:1355` show the exact parent and child paths, and `data/habitats/PATHS.tsv:1866` pins the `Debries` identifier emitted in `parent_habitats`. | Supported as a generated source-path edge. |
| No vendored ontology term fits the `Freshwater debries` concept. | The current decision is a class-level lexical no-match row. It did not inspect the GOLD path, the likely debris spelling variant, or candidate broader material terms such as `ENVO:00002264`. | Unresolved until item review. |

Ignored/hidden-inclusive exact searches of `curation/causal_graphs`,
`curation/term_requests.tsv`, `curation/term_requests_excluded.tsv`,
`curation/external_xrefs.tsv`, `history`, `research`,
`reports/habitat_research_manifest.tsv`, and `reports/yaml_record_review` for
`habitatmech:GOLD.4b4124c98a`, `gold.ecosystem:8351`,
`gold.ecosystem:8352`, `Freshwater debries`, `freshwater_debries`, and
corrected-spelling variants such as `Freshwater debris` found no maintained
overlay, authored definition, term request, exclusion, external xref, history
file, research report, or prior YAML review for this target.

## Completeness

The generated YAML is structurally complete for its current input state: it
records the exact GOLD path, the first collapsed node id, the collapsed-node
note, the immediate GOLD parent, and generated curation-history entries for the
class-level `CONFIRM_UNGROUNDED` row and the source seed.

Its empty definition and definition source are not enough for a reviewed,
minted habitat record. If item-level curation keeps the concept minted, the
decision row should explicitly record whether GOLD's `debries` labels are being
interpreted as debris, and whether the zero-assertion node is a term-request
candidate or just a source grouping kept for hierarchy.

The empty environmental-parameter, characteristic-taxon, evidence,
causal-graph, discussion, and dataset slots are acceptable today. An
ignored/hidden-inclusive fixed-string search for the exact
`Engineered > Solid waste > Debries` prefix across the committed raw GOLD side
tables found only the five `data/raw/gold_ecosystem_paths.tsv` rows for
`Debries`, `Freshwater debries`, `Marine debries`, and their two
`Plastic debries` children. The target has no direct rows in
`data/raw/gold_studies.tsv`, `data/raw/gold_path_biosamples.tsv`, or
`data/raw/gold_path_triads.tsv`.

Ignored/hidden-inclusive exact searches covered `data/habitats`,
`data/raw`, `curation`, `history`, `research`, `reports`, `conf`, `src`,
`tests`, `docs`, `.claude`, `README.md`, and `justfile`. They found the target
YAML, the path lock, the raw GOLD row, the class-level decision, the parent
`Debries` record, and the zero-assertion `Marine debries` and
`Plastic debries` sibling or child records, but no item-level decision, term
request, history record, causal overlay, target-specific research report, or
prior exact YAML review report for `habitatmech:GOLD.4b4124c98a`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The exact `Freshwater debries` source concept is still backed only by a class-level `CONFIRM_UNGROUNDED` row, so the generated `UNGROUNDED` state has not been item-reviewed against GOLD's apparent debris spelling variant or the broader waste-material terms in the vendored slice. | `curation/decisions.tsv:492` has `review_depth` `CLASS`; `data/raw/gold_ecosystem_paths.tsv:1355` shows a GOLD path whose misspelled label is interpretable only from its source context; `data/raw/ontology_terms.tsv:7340` vendors `ENVO:00002264` `waste material` as a plausible broader term that the class sweep did not inspect. | `curation/decisions.tsv`; if the record stays minted and deserves a definition, `curation/term_requests.tsv`. |

No blockers or minor findings.

## Recommended Edits

1. Item-review `habitatmech:GOLD.4b4124c98a` in `curation/decisions.tsv`.
   Treat `Engineered > Solid waste > Debries > Freshwater debries` as a GOLD
   source concept, not as free text; decide whether the apparent upstream
   `debries` spelling variant means debris in freshwater or should remain an
   unresolved spelling-only lead.
2. Compare `ENVO:00002264` `waste material`, `mesh:D062611` `Solid Waste`, and
   the generated `Debries` parent against the exact source concept. If one is
   strictly broader and useful as a direct parent, use `GROUND_AS_PARENT`;
   otherwise keep `CONFIRM_UNGROUNDED` at `ITEM` depth and explain why the
   inherited `Debries` hierarchy is sufficient.
3. If item review promotes the zero-assertion node to a real term-request
   candidate, add a `curation/term_requests.tsv` definition that normalizes the
   English spelling to `freshwater debris` while preserving GOLD's source label
   in `source_attestations`.

## Follow-up Checks

After item-level curation, rerun:

- `just seed`
- `just seed-canary habitatmech:GOLD.4b4124c98a`
- `just validate data/habitats/engineered/freshwater_debries.yaml`
- `just validate-strict data/habitats/engineered/freshwater_debries.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus`
- `just report --out /tmp/habitatmech-freshwater-debries-report.tsv`
- `git diff --check`

If the item-level edit adds a term request, inspect the regenerated target to
confirm the definition, label, parents, status, and history entries follow from
maintained inputs.

## Additional Notes

The `just worklist` near-miss suggestions for this target are all freshwater
water-body terms; the committed GOLD path makes this an engineered solid-waste
branch, not a freshwater water body.
