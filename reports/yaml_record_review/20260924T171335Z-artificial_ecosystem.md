# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/engineered/artificial_ecosystem.yaml`
- Started UTC: 2026-09-24T17:11:08Z
- Finished UTC: 2026-09-24T17:13:35Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.0acae9a1a4` |
| Label | `Artificial ecosystem` |
| Category | `ENGINEERED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Generated path | `data/habitats/engineered/artificial_ecosystem.yaml` |
| Source concept | GOLD `Engineered > Artificial ecosystem` |

The target is the depth-2 GOLD `Artificial ecosystem` source path under the top-level `Engineered` branch. It is the source-path parent for children such as `Mesocosm`, `Microcosm`, `Aquaculture`, and `Water channel system`, not one of those narrower child records.

The file is generated. `data/habitats/PATHS.tsv:1357` maps `habitatmech:GOLD.0acae9a1a4` to the stable `artificial_ecosystem` slug, so future fixes belong in `curation/decisions.tsv`, `curation/term_requests.tsv`, or future source-path parent suppression support rather than in this YAML.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/engineered/artificial_ecosystem.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/artificial_ecosystem.yaml` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| Target causal overlay validator | Not applicable; an ignored-inclusive exact search over `curation/causal_graphs` for the target identifier, exact source node IDs, and source path, plus `find curation/causal_graphs -maxdepth 1 -type f -name '*artificial*' -print`, found no target overlay. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files and 32 graphs validated. |
| Reference validator | Not applicable; this generated record has no record-level `evidence` or `causal_graphs`, and HabitatMech has no dedicated per-record reference check. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 records were expected, 3206 were found, and `data/habitats/` reproduced exactly from `data/raw/`. |
| `just worklist --limit 2000` | Passed; 0 ungrounded records remain undecided and 1810 decisions are on file. |
| `just report` | Passed; the corpus report regenerated successfully. |
| `git diff --check` | Passed. |

## Identity and Grounding

`data/raw/gold_ecosystem_paths.tsv:103` is the maintained GOLD row for this exact source concept. It has canonical path `Engineered > Artificial ecosystem`, source leaf `Artificial ecosystem`, depth `2`, four collapsed GOLD node IDs, 261 direct organism assertions, no direct study or biosample assertions in that aggregate row, and `gold.ecosystem:4842|gold.ecosystem:8043|gold.ecosystem:8044|gold.ecosystem:8045` as source node IDs.

The generated source attestation mirrors that row with GOLD `gold.ecosystem:4842`, source label `Artificial ecosystem`, source path `Engineered > Artificial ecosystem`, `assertion_count: 261`, `assertion_unit: ORGANISM`, and a note that four GOLD ecosystem node IDs share this path.

Ignored-inclusive exact raw searches found no exact direct rows for `Engineered > Artificial ecosystem` in `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_studies.tsv`, or `data/raw/gold_path_triads.tsv`.

`curation/decisions.tsv:160` is the only target decision row. It is a class-level `CONFIRM_UNGROUNDED` row from the lexical sweep and explicitly says the sweep did not assess whether the concept is a habitat at all, so `UNGROUNDED` has not been confirmed by item-level review of this source concept.

The record has one generated parent, `habitatmech:GOLD.2acb39dd08`, inherited from the `Engineered` source-path prefix. That parent is the GOLD top-level root reviewed in `reports/yaml_record_review/20260924T165434Z-engineered__900b76ad.md`; it also has only a class-level decision and remains unresolved as a strict habitat parent.

## Evidence

The generated target has no record-level `evidence`, no `definition`, no `environmental_parameters`, no `characteristic_taxa`, and no target-specific `causal_graphs`.

Supported:

- The source-path identity, four-node collapse, and 261 GOLD organism assertions are reproducible from `data/raw/gold_ecosystem_paths.tsv:103`.
- The generated parent edge to `habitatmech:GOLD.2acb39dd08` is reproducible from the `Engineered` source-path prefix.
- Child-level curation exists for exact or narrower concepts under this branch, including sampled `Mesocosm` and `Microcosm` exact groundings and reviewed `Water channel system` term requests.

Unsupported or over-scoped:

- No item-level decision has inspected whether the depth-2 `Artificial ecosystem` branch is a real habitat grouping, an experimental apparatus grouping, or a contextual GOLD source branch.
- No maintained input establishes `Artificial ecosystem` as a strict broader habitat for all of its generated children; children range from exact ontology-grounded `Mesocosm` and `Microcosm` records to aquarium, aquaculture, plant-growth-chamber, and water-channel descendants.
- No maintained term request defines the generic GOLD `Artificial ecosystem` concept if it is retained as a novel habitat.

Related curation:

- `curation/samples/exact-20260814.tsv` confirms exact mesocosm and microcosm matches below this parent, but that sample did not review the `Artificial ecosystem` root itself.
- `curation/term_requests.tsv:107` and `curation/term_requests.tsv:108` define water-channel-system descendants below this parent and interpret those records as vivaria rather than bioreactors, lab-enrichment cultures, building plumbing, or civil-engineering canals.

## Completeness

Consequential gaps:

- The target has no item-level decision or term request.
- The target has no definition, environmental parameters, characteristic taxa, causal graph, or target-specific literature evidence.
- The target's only parent is also class-level reviewed rather than item-reviewed.
- `just report` ranks `Artificial ecosystem` among the high-volume class-level sweep records, so this record is visible as still needing real curation rather than merely a low-assertion branch.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-artificial_ecosystem.md' -print` found no earlier YAML review report for this exact stem. `find` is not gitignore-filtered.
- An ignored-inclusive exact search over `curation`, `history`, `research`, `data/habitats/PATHS.tsv`, `data/habitats/engineered`, `reports/yaml_record_review`, `data/raw`, and `conf/id_label_targets.yaml` for `habitatmech:GOLD.0acae9a1a4` found the path lock, the class-level decision row, generated child records that use this target as a parent, and this target YAML; it found no target-specific term request, term-request exclusion, history record, deep-research report, prior YAML review, id-label residual, or causal overlay.
- Ignored-inclusive exact searches over the same corpus for `gold.ecosystem:4842`, `gold.ecosystem:8043`, `gold.ecosystem:8044`, and `gold.ecosystem:8045` found the raw aggregate row and this generated target, and found no target-specific curation inputs.
- An ignored-inclusive exact raw search found `data/raw/gold_ecosystem_paths.tsv:103` for the exact `Engineered > Artificial ecosystem` path and found no exact rows in `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_studies.tsv`, or `data/raw/gold_path_triads.tsv`.
- Ignored-inclusive `artificial ecosystem`, `mesocosm`, `microcosm`, `aquaculture`, and `vivarium` searches over vendored ontology terms and curation tables found relevant exact or broader child-level terms and curation, but no exact term or item-level curation for this root.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The target has only a class-level `CONFIRM_UNGROUNDED` row, so `UNGROUNDED` has not been item-reviewed against the full `Engineered > Artificial ecosystem` source path. | `curation/decisions.tsv:160` records `review_depth=CLASS` and says habitathood was not assessed. The exact GOLD aggregate row carries 261 direct organism assertions, so this is a high-volume unresolved node in the class-level sweep rather than an empty structural path. | `curation/decisions.tsv`; if item review confirms a real novel habitat, `curation/term_requests.tsv`. |
| Major | The target is serialized as a strict parent for many narrower artificial-ecosystem records even though the parent itself has not been item-reviewed. | Exact ignored-inclusive searches found `habitatmech:GOLD.0acae9a1a4` in generated records for `Mesocosm`, `Microcosm`, `Vivarium`, `Water channel system`, `Aquaculture`, `Plant growth chamber`, and several microcosm/material children. `parent_habitats` means strictly broader, but the current maintained input for this parent is only a class-level lexical sweep. | `curation/decisions.tsv`; if item review rejects a source-derived edge, future parent-suppression support in `src/habitatmech/seed.py` or child-specific `curation/term_requests.tsv` rows with `parent_mode=REPLACE`. |

## Recommended Edits

1. Item-review `habitatmech:GOLD.0acae9a1a4` in `curation/decisions.tsv` against the exact `Engineered > Artificial ecosystem` path and its child records.
2. Decide whether the GOLD root is a real generic artificial ecosystem habitat, an apparatus grouping whose children need narrower vivarium/aquaculture parents, or a contextual GOLD branch that should not be serialized as a strict parent.
3. If the root is retained as a novel habitat, add a definition in `curation/term_requests.tsv`; if the existing source-path parent edges are contextual for any reviewed child, use `parent_mode=REPLACE` or future source-path parent suppression support to remove false inherited parents.

## Follow-up Checks

- After adding a decision or term request, run `just seed`, `just seed-canary habitatmech:GOLD.0acae9a1a4`, inspect `data/habitats/engineered/artificial_ecosystem.yaml`, then run `just seed-apply --force`.
- Run `just validate data/habitats/engineered/artificial_ecosystem.yaml` and `just validate-strict data/habitats/engineered/artificial_ecosystem.yaml`.
- Run `just term-requests-check`, `just validate-history`, `just verify-corpus --max-diffs 1`, `just worklist --limit 2000`, `just report`, and `git diff --check`.
- Run `just validate-causal-all` if any overlay changes.

## Additional Notes

- The exact ignored-inclusive miss searches included hidden and gitignored files.
- The existing child-level reviews under `Artificial ecosystem` are useful leads, but they cannot automatically validate this exact parent or every source-derived parent edge below it.
