# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/marine_fish_farm.yaml
- Started UTC: 2026-09-24T18:48:25Z
- Finished UTC: 2026-09-24T18:52:10Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.3e0abbfef7` |
| Label | `Marine fish farm` |
| Category | `ENGINEERED` |
| Grounding | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Maintained source | generated from `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and the class-level row in `curation/decisions.tsv` |

Reviewed the complete generated record at `data/habitats/engineered/marine_fish_farm.yaml`. The record is a GOLD-only habitat for `Engineered > Artificial ecosystem > Aquaculture > Marine fish farm`, with one displayed `gold.ecosystem:8039` source attestation, two collapsed GOLD ecosystem node IDs in the raw inventory, and one GOLD organism assertion. The file itself is generated output; any future grounding or parent fix belongs in the maintained `curation/decisions.tsv` row for `habitatmech:GOLD.3e0abbfef7`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/engineered/marine_fish_farm.yaml` | Passed |
| `just validate-strict data/habitats/engineered/marine_fish_farm.yaml` | Passed |
| Focused causal overlay validator | Not applicable; exact ignored-inclusive searches in `curation/causal_graphs/` found no `habitatmech:GOLD.3e0abbfef7`, `gold.ecosystem:8039`, `gold.ecosystem:8041`, or exact Marine fish farm source-path overlay |
| `just validate-causal-all` | Passed; 32 files / 32 graphs |
| Reference validator | Not applicable; the generated GOLD-only record has no record-level `evidence` items, no causal graph, and no environmental-parameter references |
| `just term-requests-check` | Passed; 109 terms |
| `just validate-history` | Passed; 77 history records |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected / 3,206 found / 0 missing / 0 extra / 0 differing |
| `just worklist --limit 2000` | Passed; 0 ungrounded concepts remain undecided and 1,810 decisions are present |
| `just report` | Passed; 3,206 habitat records summarized |
| `git diff --check` | Passed |

## Identity and Grounding

The generated identifier, label, category, and source attestation agree with the committed GOLD inventory. `data/raw/gold_ecosystem_paths.tsv` has the collapsed path `Engineered > Artificial ecosystem > Aquaculture > Marine fish farm`, with `depth` 4, `gold_node_count` 2, `organism_count` 1, `study_count` 0, `biosample_count` 0, `total_assertions` 1, and `gold_node_ids` `gold.ecosystem:8039|gold.ecosystem:8041`.

The current `UNGROUNDED` status is under-reviewed. The only maintained decision for `habitatmech:GOLD.3e0abbfef7` is a 2026-08-12 class-level `CONFIRM_UNGROUNDED` row whose note explicitly says the habitat identity was not assessed. An ignored-inclusive exact search of `data/raw/ontology_terms.tsv` found no `marine fish farm` term, but the local slice does contain `ENVO:00000294` `fish farm`, "A facility in which fish are raised commercially in tanks or enclosures, usually for food." Marine fish farms are a narrower subtype of fish farm, so the source concept should be item-reviewed for a `GROUND_AS_PARENT` decision to `ENVO:00000294` unless a curator finds a still narrower term outside the current slice.

The current generated parent, `habitatmech:GOLD.0287e1b2a9`, points to the direct GOLD source-path parent `Engineered > Artificial ecosystem > Aquaculture`. That parent is also still seeded and narrower than `ENVO:03600074` `aquaculture farm`, so it is broader than Marine fish farm but less specific than the available `fish farm` parent. Both `ENVO:00000294` and `ENVO:03600074` are direct subclasses of `ENVO:00000077` `agricultural ecosystem` in the vendored ontology edge table.

## Evidence

- Supported: the source path, source leaf, representative `gold.ecosystem:8039` source ID, two-node collapse, and one-organism assertion count match `data/raw/gold_ecosystem_paths.tsv`.
- Supported: the raw `gold.ecosystem:8041` node is part of the same collapsed Marine fish farm GOLD path, which explains why the generated record displays the first node ID and carries the note that two GOLD ecosystem node IDs share the path.
- Supported: no direct GOLD biosample, MIxS triad, or study side table adds source-path-specific claims for `gold.ecosystem:8039`, `gold.ecosystem:8041`, or the anchored Marine fish farm source path; ignored-inclusive exact searches over the focused GOLD side tables found only the canonical `gold_ecosystem_paths.tsv` row.
- Under-reviewed: the class-level `CONFIRM_UNGROUNDED` decision missed the vendored `ENVO:00000294` `fish farm` broader term because the class sweep did not assess source-path habitat identity.
- No record-level citations, characteristic taxa, environmental parameters, or causal edges are present, so there are no attached snippets or literature references to validate.

## Completeness

The record is structurally sparse but not missing any required generated field. It has the expected GOLD source attestation and source-path parent for a Marine fish farm source concept with one organism assertion and no committed GOLD biosample, triad, or study rows.

Bounded ignored-inclusive searches were run over `curation`, `history`, `research`, `reports/yaml_record_review`, `conf/id_label_targets.yaml`, `data/habitats/PATHS.tsv`, `data/habitats`, and the focused GOLD raw side tables for `habitatmech:GOLD.3e0abbfef7`, `gold.ecosystem:8039`, `gold.ecosystem:8041`, and `Engineered > Artificial ecosystem > Aquaculture > Marine fish farm`. They found the generated target, its generated `Sediment` child, the `data/habitats/PATHS.tsv` row, the class-level `curation/decisions.tsv` row, and the canonical GOLD ecosystem-path row; they found no existing review report for this exact stem before this report was written and no item-level decision, term request, history entry, research report, label-correspondence exception, auxiliary GOLD biosample/triad/study row, or target-specific causal overlay.

The generated child at `data/habitats/engineered/sediment__26a3aecb.yaml` inherits `habitatmech:GOLD.3e0abbfef7` as a parent, so a future item-level decision for Marine fish farm also needs a bounded regeneration of that child to keep the source-path hierarchy synchronized.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `marine_fish_farm.yaml` is still `UNGROUNDED` under a class-level sweep even though the vendored ontology contains a strict broader `ENVO:00000294` `fish farm` parent. | The only maintained decision for `habitatmech:GOLD.3e0abbfef7` has `review_depth` `CLASS` and says the concept's habitat identity was not assessed. Ignored-inclusive exact searches found no exact `marine fish farm` term in `data/raw/ontology_terms.tsv`, but did find `ENVO:00000294` `fish farm`, which is narrower than the current Aquaculture path parent and broader than a marine fish farm. | `curation/decisions.tsv` |

## Recommended Edits

1. Item-review `habitatmech:GOLD.3e0abbfef7` in `curation/decisions.tsv` against the exact `Engineered > Artificial ecosystem > Aquaculture > Marine fish farm` path, `ENVO:00000294` `fish farm`, `ENVO:03600074` `aquaculture farm`, and the existing generated `habitatmech:GOLD.0287e1b2a9` Aquaculture parent.
2. If no exact Marine fish farm ontology term is found, replace the class-level `CONFIRM_UNGROUNDED` row with an item-level `GROUND_AS_PARENT` row to `ENVO:00000294` `fish farm`.
3. Regenerate the Marine fish farm record and its `Sediment` child so the child keeps the reviewed source-path parent and the parent gains the fish-farm ontology parent.

## Follow-up Checks

- `just seed`
- `uv run python scripts/seed_from_sources.py --apply --force --only habitatmech:GOLD.3e0abbfef7 habitatmech:GOLD.d6c97cc5bd`
- Inspect `data/habitats/engineered/marine_fish_farm.yaml` and `data/habitats/engineered/sediment__26a3aecb.yaml`
- `just validate data/habitats/engineered/marine_fish_farm.yaml`
- `just validate-strict data/habitats/engineered/marine_fish_farm.yaml`
- `just validate data/habitats/engineered/sediment__26a3aecb.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`

## Additional Notes

- No blocker finding was found: the current generated YAML validates, its GOLD source attestation is internally consistent, and the record denotes an engineered aquaculture facility rather than a non-habitat.
- No minor findings were found.
