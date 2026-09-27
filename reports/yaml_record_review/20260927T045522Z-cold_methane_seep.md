# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/cold_methane_seep.yaml`
- Started UTC: 2026-09-27T04:51:00Z
- Finished UTC: 2026-09-27T04:55:22Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.dc31418f43` |
| Label | `Cold methane seep` |
| Class | `HabitatRecord` |
| Category | `AQUATIC` |
| Generated or maintained | Generated from `data/raw/`, `curation/decisions.tsv`, and `data/habitats/PATHS.tsv`; do not hand-edit |
| Current grounding | `UNGROUNDED` |
| Current mapping | `SEEDED` |

The target resolves exactly one generated YAML file and one slug:
`data/habitats/aquatic/cold_methane_seep.yaml`. `data/habitats/PATHS.tsv`
pins `habitatmech:GOLD.dc31418f43` to `cold_methane_seep`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/cold_methane_seep.yaml` | Pass: LinkML reported `No issues found`. |
| `just validate-all data/habitats/aquatic/cold_methane_seep.yaml` | Pass: 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-strict data/habitats/aquatic/cold_methane_seep.yaml --quiet` | Pass: 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal-all` | Pass: 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Pass: committed term-request table is current with 109 terms. |
| `just validate-history` | Pass: 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist.tsv` | Pass: regenerated a 953-row ungrounded worklist outside the repository. |
| `just verify-corpus --max-diffs 1` | Pass: 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just report` | Pass: completed the corpus diagnostic report without surfacing a target-specific issue. |

No documented validator was skipped.

## Identity and Grounding

The record identity is consistent with the maintained GOLD inventory. The
GOLD canonical path is
`Environmental > Aquatic > Freshwater > Floodplain > Cold methane seep`, and
`mint("GOLD", canonical_path)` yields `habitatmech:GOLD.dc31418f43`.
`data/raw/gold_ecosystem_paths.tsv` contributes exactly one upstream GOLD node,
`gold.ecosystem:8382`, whose leaf label is `Cold methane seep`.

The `AQUATIC` category is inherited from the first two GOLD levels,
`Environmental > Aquatic`. The sole `parent_habitats` value,
`habitatmech:GOLD.22656a226b`, is the generated identifier for the immediate
GOLD parent path `Environmental > Aquatic > Freshwater > Floodplain`, which
`data/habitats/PATHS.tsv` pins to `floodplain__7ad4b08f`.

The current `UNGROUNDED` status follows from `curation/decisions.tsv`, whose
only row for `habitatmech:GOLD.dc31418f43` is a class-level
`CONFIRM_UNGROUNDED` from the no-match sweep. It is intentionally not an
item-level review: the decision notes state that no vendored-slice term matched
by the sweep routes, but that the source concept itself was not assessed as a
term-request candidate. `mapping_status: SEEDED` is therefore correct because
the seeder promotes a record to `REVIEWED` only when every contributing source
concept has item-level review.

`ENVO:01000263` `cold seep` is already used for the neighboring marine GOLD
path `Environmental > Aquatic > Marine > Cold seeps`. That record has an
item-level `GROUND` decision to `ENVO:01000263`. The current freshwater
floodplain path should remain distinct until a curator reads the path and the
ENVO term definition; adopting the marine cold-seep term automatically would
merge this GOLD path into the marine source concept.

## Evidence

The generated GOLD attestation is faithful to
`data/raw/gold_ecosystem_paths.tsv`:

| Field | Raw value |
|---|---|
| `canonical_path` | `Environmental > Aquatic > Freshwater > Floodplain > Cold methane seep` |
| `leaf_label` | `Cold methane seep` |
| `gold_node_ids` | `gold.ecosystem:8382` |
| `gold_node_count` | `1` |
| `organism_count` | `0` |
| `biosample_count` | `0` |
| `study_count` | `0` |
| `total_assertions` | `0` |

Because the raw row has zero organism assertions, the generated
`source_attestations` entry correctly omits `assertion_count` and
`assertion_unit`; there is no count to expose for this GOLD concept.

Exact raw-inventory searches found no independent GOLD API biosample row, GOLD
study row, GOLD MIxS triad row, environment-parameter row, PREGO row, BacDive
row, or Madin row for the exact source path. The empty
`environmental_parameters` and `characteristic_taxa` slots are therefore
consistent with the committed source inventories.

## Completeness

The record has no curator-authored `evidence`, `causal_graphs`, `discussions`,
or `datasets`; those optional slots are correctly empty for the current
maintained inputs.

Hidden- and ignored-file-inclusive exact searches of `curation`, `history`,
`research`, `reports/yaml_record_review`, `conf`, and
`data/habitats/PATHS.tsv` for `habitatmech:GOLD.dc31418f43`,
`cold_methane_seep`, and `Cold methane seep` found the expected
`curation/decisions.tsv` row and `PATHS.tsv` entry only. A `find` search of
`research`, `curation`, `history`, and `reports/yaml_record_review` for files
named `*cold_methane_seep*` found none, including hidden and ignored files in
those trees.

## Findings

None found.

## Recommended Edits

None required.

Optional future work: replace the class-level
`habitatmech:GOLD.dc31418f43` row in `curation/decisions.tsv` with an
item-level decision once a curator reads the source path and candidate
`ENVO:01000263` `cold seep`. If no exact or broader ontology term fits the
freshwater floodplain source path, keep `CONFIRM_UNGROUNDED`, set
`review_depth` to `ITEM`, explain the rejected marine cold-seep candidate in
`notes`, and add an append-only session record under `history/`. After
regeneration the YAML should remain `UNGROUNDED`, should switch to
`mapping_status: REVIEWED`, and should carry a `CONFIRM_UNGROUNDED`
`curation_history` event whose notes describe an item-level judgment rather
than the class-level no-match sweep.

## Follow-up Checks

For the optional item-level promotion:

- `just seed`
- `just seed-canary habitatmech:GOLD.dc31418f43`
- Inspect `data/habitats/aquatic/cold_methane_seep.yaml`.
- `just seed-apply --force`
- `just validate data/habitats/aquatic/cold_methane_seep.yaml`
- `just validate-all data/habitats/aquatic/cold_methane_seep.yaml`
- `just validate-strict data/habitats/aquatic/cold_methane_seep.yaml --quiet`
- `just validate-history`
- `just verify-corpus --max-diffs 1`

## Additional Notes

`just worklist --limit 0 --status all --out /tmp/habitatmech-worklist.tsv`
lists this source concept with zero assertions and candidate
`ENVO:01000263` via the `methane seep` synonym. That row is a curation queue
lead, not evidence that the candidate is an exact or broad match.
