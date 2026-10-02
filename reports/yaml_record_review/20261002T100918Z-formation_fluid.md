# YAML Record Review: formation fluid

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/aquatic/formation_fluid.yaml`
- Started UTC: 2026-10-02T10:06:00Z
- Finished UTC: 2026-10-02T10:09:18Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Path | `data/habitats/aquatic/formation_fluid.yaml` |
| Identifier | `ENVO:03600007` |
| Label | `formation fluid` |
| Category | `AQUATIC` |
| Grounding | `EXACT` |
| Mapping | `SEEDED` |
| Generated? | Yes; `just verify-corpus` reproduced this file from `data/raw/` and curation inputs |

This record covers GOLD path `Environmental > Aquatic > Marine > Aquifer > Formation fluid`, source id `gold.ecosystem:5737`, which `data/habitats/PATHS.tsv` maps to stable record stem `formation_fluid`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/formation_fluid.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/aquatic/formation_fluid.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus` | Passed; 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just validate-causal-all` | Passed; 32 curation files with 32 graphs. |
| `just term-requests-check` | Passed; `term-request table is current (109 terms)`. |
| `just validate-history` | Passed; 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just worklist --status all --out /tmp/habitatmech-formation-fluid-worklist.tsv` | Passed; wrote 953 ungrounded rows. The target is not in this minted-term-only worklist because it is an `EXACT` ENVO grounding. |
| `just report --out /tmp/habitatmech-formation-fluid-report.tsv` | Passed; row 928 reports `EXACT`, `SEEDED`, `GOLD`, one source, 0 assertion total, 2 parents, 0 parameters, 0 taxa, and 0 causal graphs. |

## Identity and Grounding

| Claim | Evidence | Verdict |
|---|---|---|
| The generated record denotes ENVO `formation fluid`. | `data/raw/ontology_terms.tsv` labels `ENVO:03600007` as `formation fluid` and defines it as a naturally contained geologic-formation fluid. The generated record uses that same CURIE, label, definition, and `definition_source: ENVO`. | Supported exactly. |
| `EXACT` grounding is appropriate for the GOLD leaf label. | GOLD row `gold.ecosystem:5737` has canonical path `Environmental > Aquatic > Marine > Aquifer > Formation fluid`, leaf `Formation fluid`, depth 5, and no modifier on the terminal label. The ENVO label is the same after case normalization. | Supported exactly. |
| The ontology parent `ENVO:02000140` is strictly broader. | The vendored subclass slice has `ENVO:03600007 rdfs:subClassOf ENVO:02000140`, and `ENVO:02000140` is `fluid environmental material`. | Supported exactly. |
| The generated GOLD source-path parent `habitatmech:GOLD.f8b744283b` is strictly broader. | `src/habitatmech/seed.py` adds every GOLD child path's immediate parent path as a `parent_habitats` edge in a second pass. For this record, that turns `Environmental > Aquatic > Marine > Aquifer` into a parent of ENVO `formation fluid`. The parent record is the minted `Aquifer` source concept, not a fluid-material class. | Unsupported; see `HM-FORMATION-FLUID-001`. |
| `mapping_status: SEEDED` reflects the curation inputs. | Exact ignored/hidden searches over `curation/decisions.tsv`, `curation/term_requests.tsv`, `curation/causal_graphs/`, and `history/` for `ENVO:03600007`, `gold.ecosystem:5737`, `formation_fluid`, and `Formation fluid` found no item-level decision, term request, causal overlay, or curation-history row for this target. | Supported exactly. |

## Evidence

| Claim | Evidence | Verdict |
|---|---|---|
| The sole generated source attestation matches the GOLD path inventory. | `data/raw/gold_ecosystem_paths.tsv` row 1503 records `gold.ecosystem:5737` at `Environmental > Aquatic > Marine > Aquifer > Formation fluid` with leaf `Formation fluid`, and the YAML preserves the same `source_id`, `source_label`, `source_path`, and `skos:exactMatch`. | Supported exactly. |
| No direct assertion count is expected on the source attestation. | The canonical raw GOLD row has `organism_count=0`, `study_count=0`, `biosample_count=0`, and `total_assertions=0`, so the generated attestation correctly omits `assertion_count` and `assertion_unit`. | Supported exactly. |
| Auxiliary GOLD API evidence is sparse and contextual. | `data/raw/gold_path_biosamples.tsv` lists 3 biosamples for path id `5737`, and `data/raw/gold_studies.tsv` lists one study, `Gs0114576`, that combines this exact path with `Environmental > Aquatic > Marine > Oceanic > Abyssal plane`. | Supported; useful provenance, not a reason to add taxa or mechanisms. |
| GOLD MIxS triads should not be promoted into this record. | `data/raw/gold_path_triads.tsv` has one-study triads for broad `ENVO:00000447` `marine biome`, local `ENVO:00012408` `aquifer`, and medium `ENVO:01000950` `water ice formation process`. The broad/local values are context for the submitted biosamples, and the medium value is a process mismatch for a material record. | Correctly omitted. |

## Completeness

- The `definition` and `definition_source` slots are complete because ENVO already supplies the exact class definition.
- `environmental_parameters`, `characteristic_taxa`, `evidence`, `causal_graphs`, `discussions`, and `datasets` are correctly empty for now. The raw GOLD ecosystem row has no direct organism assertions, the auxiliary biosample and triad rows provide only three biosamples from one study, and no inspected causal mechanism evidence is attached.
- A `REVIEW` decision is still needed in `curation/decisions.tsv` after the false path parent is suppressed. That decision should be keyed to the GOLD source concept that currently resolves to `ENVO:03600007`; `REVIEW` is the decision enum that endorses a seeded exact answer.
- Exact ignored/hidden searches over maintained inputs, `history/`, `research/habitats/`, `conf/`, and `reports/yaml_record_review/` found prior mentions of Formation fluid only in advisory research/review prose for neighboring oil/gas and Aquifer records. They found no existing Formation fluid YAML-review report and no maintained curation row for `ENVO:03600007` or `gold.ecosystem:5737`.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| `HM-FORMATION-FLUID-001` | Major | `parent_habitats` includes false source-path parent `habitatmech:GOLD.f8b744283b`. Formation fluid is a fluid environmental material contained in geologic formations, not a kind of aquifer. | The vendored ENVO slice gives `ENVO:03600007` exactly one direct parent, `ENVO:02000140` `fluid environmental material`. The GOLD parent row `gold.ecosystem:5736` denotes the path bucket `Environmental > Aquatic > Marine > Aquifer`; `src/habitatmech/seed.py` currently adds that path bucket as a parent solely because it is the immediate source path prefix. `docs/CURATION.md` states that `parent_habitats` is an is-a claim and must not retain merely related upstream links. | Add a maintained GOLD parent-path suppression or override in `curation/`, then teach the second GOLD pass in `src/habitatmech/seed.py` to consult it before adding `parent_habitats`. |

## Recommended Edits

1. Add a maintained `curation/` input that suppresses the generated GOLD edge from child path `Environmental > Aquatic > Marine > Aquifer > Formation fluid` to parent path `Environmental > Aquatic > Marine > Aquifer`.
2. Update the second GOLD parent-path pass in `src/habitatmech/seed.py` so it skips curated suppressions before calling `store.concepts[child_id].parents.add(parent_id)`.
3. Regenerate the corpus and confirm `data/habitats/aquatic/formation_fluid.yaml` keeps ENVO parent `ENVO:02000140` and drops `habitatmech:GOLD.f8b744283b`.
4. Add an item-level `REVIEW` row in `curation/decisions.tsv` for the GOLD source concept after the generated hierarchy is correct, preserving the `EXACT` `ENVO:03600007` grounding.

## Follow-up Checks

| Edit | Check |
|---|---|
| GOLD parent-path suppression | Run `just seed` and `just seed-canary ENVO:03600007`; re-read `data/habitats/aquatic/formation_fluid.yaml` and verify only `ENVO:02000140` remains in `parent_habitats`. |
| Seeder suppression support | Add a regression test that proves a suppressed GOLD parent path is not added during the second GOLD pass. |
| Item-level review | Run `just validate data/habitats/aquatic/formation_fluid.yaml`, `just validate-strict data/habitats/aquatic/formation_fluid.yaml`, `just verify-corpus`, and `just report --out /tmp/habitatmech-formation-fluid-after.tsv`; the report row should become `REVIEWED` for the same exact ENVO identifier once every contributing source concept is item-reviewed. |

## Additional Notes

- This finding is the same generated-parent class as the earlier Crustal fluid review: a GOLD path context can be related evidence without being an is-a parent.
- The earlier `Aquifer` review correctly flagged its inherited `marine water body` parent as false. Its suggestion to preserve Formation fluid's `Aquifer` parent should be superseded by this item-level Formation fluid review because ENVO's exact Formation fluid class is a material, not an aquifer.
- Exact absence checks used `rg --no-ignore --hidden` and `find`, so ignored and hidden files were included in the bounded paths searched for prior maintained rows, causal overlays, research notes, and YAML review reports.
