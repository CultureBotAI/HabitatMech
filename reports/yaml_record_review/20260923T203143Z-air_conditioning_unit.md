# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/engineered/air_conditioning_unit.yaml`
- Started UTC: `2026-09-23T20:13:00Z`
- Finished UTC: `2026-09-23T20:31:43Z`
- Verdict: `pass with minor issues`

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/engineered/air_conditioning_unit.yaml` |
| Class | `HabitatRecord` |
| Identifier | `ENVO:00002874` |
| Label | `air conditioning unit` |
| Definition source | `ENVO` |
| Category | `ENGINEERED` |
| Grounding status | `EXACT` |
| Mapping status | `REVIEWED` |

This is a generated record owned by upstream inputs, not by hand edits under
`data/habitats/`. Its path is pinned by `data/habitats/PATHS.tsv`, which maps
`ENVO:00002874` to `air_conditioning_unit`.

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-air_conditioning_unit.md' -print` | Passed; no prior exact report was present. |
| `find curation/causal_graphs -maxdepth 1 -type f -name '*air_conditioning_unit*' -print` | Passed; no candidate causal overlay was present. |
| `rg --no-ignore --hidden -n "ENVO:00002874\|air_conditioning_unit\|air conditioning unit" curation/causal_graphs` | Passed; no causal overlay references the identifier, slug, or label. Ignored and hidden files were included. |
| `just validate data/habitats/engineered/air_conditioning_unit.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/habitats/engineered/air_conditioning_unit.yaml` | Passed; 1 file scanned, 0 files with errors, and 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| Focused causal-graph validation | Not applicable; the record has no maintained overlay under `curation/causal_graphs/`. |
| Reference validator | Not applicable; an ignored- and hidden-inclusive search of `justfile`, `scripts`, `.github`, and `.claude` found no dedicated reference validator in this repository. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; no issues found and 77 history records validated. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records, 3,206 on disk, 0 missing, 0 extra, and 0 differing. |
| `just worklist --limit 2000` | Passed after rerunning outside the managed workspace sandbox; the first run could not read `~/.cache/uv/sdists-v9/.git`. The command reported 0 ungrounded records still undecided and 1,810 decisions on file. |
| `just report` | Passed; the corpus report completed for 3,206 records. |
| `git diff --check` | Passed before report creation. |

## Identity and Grounding

The BacDive source concept is
`bacdive.isolation_source:air-conditioner`, label `Air-conditioner`, slug
`air-conditioner`, with 16 strain assertions and 11 ranked taxa in
`data/raw/bacdive_isolation_sources.tsv`.

The item-level row in `curation/decisions.tsv` grounds
`habitatmech:BACDIVE.802a96c7ec` to `ENVO:00002874` `air conditioning unit` as
`EXACT`. That is defensible: the BacDive label is a hyphenated spelling of
ENVO's `air conditioner` exact synonym. The generated identity, label,
definition, `EXACT` grounding status, `skos:exactMatch` predicate, and
`REVIEWED` mapping status all follow from that decision.

The ENVO slice contains the exact grounding term:

- `ENVO:00002874` `air conditioning unit`, with definition source `ENVO` and
  exact synonyms `A/C`, `A/C unit`, and `air conditioner`.
- A single parent edge from `ENVO:00002874` to `ENVO:00003074`
  `manufactured product`, which accounts for the generated
  `parent_habitats` entry.

## Evidence

The definition, synonyms, and `ENVO:00003074` parent are ontology-derived. The
BacDive source attestation reproduces the row in
`data/raw/bacdive_isolation_sources.tsv` and correctly preserves
`assertion_count: 16` with `assertion_unit: STRAIN`.

All eleven `characteristic_taxa` are the exact rows for
`bacdive.isolation_source:air-conditioner` in `data/raw/bacdive_source_taxa.tsv`.
Their `association_count` values sum to the 16 BacDive strain assertions, and
the generated `rank` values match the raw BacDive ranks 1 through 11.

No causal graph, claim-level evidence block, environmental parameter, discussion
item, or dataset usage is asserted for this record.

## Completeness

The record is complete enough for its current single-source BacDive scope:

- It has one item-level grounding decision for its only source concept.
- Its direct ENVO parent is present.
- It emits every BacDive taxon row for the source concept, not a truncated top
  25 slice.
- It correctly leaves causal graphs, environmental parameters, discussions, and
  datasets empty because no maintained input asserts them.

Bounded, ignored-inclusive searches for `ENVO:00002874`,
`bacdive.isolation_source:air-conditioner`, `BACDIVE.802a96c7ec`,
`Air-conditioner`, and `air-conditioner` across curation inputs, raw inputs,
history, reports, source, tests, and configuration found the single
`curation/decisions.tsv` owner row, the BacDive raw rows, the ENVO slice rows,
the `PATHS.tsv` slug row, and one prior review mention in the unrelated
`air` report. The same search found no maintained causal overlay for this
record.

## Findings

### Minor

| Finding | Evidence | Maintained owner |
|---|---|---|
| The BacDive attestation note is stale after local item curation. | The generated source attestation says kg-microbe's isolation-source mapping row had no ontology target and was "treated as ungrounded rather than re-grounded by lexical match." That describes the raw `data/raw/isolation_source_groundings.tsv` row, but `curation/decisions.tsv` now item-grounds the same BacDive source to `ENVO:00002874`, and the generated record is `EXACT`/`REVIEWED` rather than `UNGROUNDED`. The source concept itself is correct; only this note is misleading. | `src/habitatmech/seed.py`, in the BacDive attestation note generation for `automatic.route == "bacdive_declined_upstream"` |

## Recommended Edits

1. In `src/habitatmech/seed.py`, reword or suppress the
   `bacdive_declined_upstream` attestation note when a HabitatMech curator
   supplies a later `GROUND` or `GROUND_AS_PARENT` decision. For this record the
   generated note should say that the kg-microbe row was empty but HabitatMech
   curated `Air-conditioner` to exact `ENVO:00002874`, or else omit the stale
   upstream note entirely.

## Follow-up Checks

- Add or update a focused seeder regression that covers a BacDive empty-upstream
  row later grounded by `curation/decisions.tsv`.
- Re-seed `ENVO:00002874` with `just seed-canary ENVO:00002874` and inspect
  `data/habitats/engineered/air_conditioning_unit.yaml`.
- Run `just verify-corpus --max-diffs 1` to prove the generated corpus has no
  unexpected drift.
- Run `just validate-strict data/habitats/engineered/air_conditioning_unit.yaml`
  to prove the regenerated record still satisfies the closed LinkML schema.

## Additional Notes

The ENVO definition in the vendored slice spells "manufactured" as
`manufactuered`; the generated record correctly reproduces that ontology text.
