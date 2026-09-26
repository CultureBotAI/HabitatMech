# YAML Record Review

- Repository: HabitatMech
- Record: `data/habitats/aquatic/produced_water_flow_back.yaml`
- Started UTC: 2026-09-26T18:44:52Z
- Finished UTC: 2026-09-26T18:44:52Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Identifier | `habitatmech:GOLD.9272fc9901` |
| Label | `Produced water/Flow back` |
| Class | `HabitatRecord` |
| Category | `AQUATIC` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source concept | GOLD `Environmental > Aquatic > Deep subsurface > Shale gas/oil reservoir > Produced water/Flow back` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and `curation/decisions.tsv`; the YAML record is read-only |
| Locked slug | `data/habitats/PATHS.tsv:2371` maps `habitatmech:GOLD.9272fc9901` to `produced_water_flow_back` |

The target was selected from the current all-status worklist immediately after
the already-reviewed `Poultry farm` row. `data/raw/gold_ecosystem_paths.tsv`
lists the exact GOLD path at line 708 with leaf label
`Produced water/Flow back`, one collapsed GOLD node, three GOLD organism
assertions, no study or biosample assertions in that count table, and upstream
node `gold.ecosystem:7795`.

The generated YAML preserves that identity with source id
`gold.ecosystem:7795`, assertion count `3`, assertion unit `ORGANISM`,
`mapping_status: SEEDED`, and the single generated parent
`ENVO:00002185` `oil reservoir`.

## Validation

| Command | Result |
| --- | --- |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist.tsv` | Passed; wrote 953 ungrounded rows and listed `habitatmech:GOLD.9272fc9901` as the first unreviewed row after Pooled tissues and the already-reviewed Poultry farm target. |
| `just report` | Passed; reported 3206 generated records, 953 `UNGROUNDED`, 830 class-level sweeps, and ranked `Produced water/Flow back` among GOLD paths with corroborating MIxS triads. |
| `just validate data/habitats/aquatic/produced_water_flow_back.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/aquatic/produced_water_flow_back.yaml` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just validate-causal-all` | Passed; validated 32 causal-graph curation files with 32 graphs. |
| `just term-requests-check` | Passed; the term-request table is current for 109 terms. |
| `just validate-history` | Passed; 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; expected and found 3206 generated records, with 0 missing, 0 extra, and 0 differing files. |
| `git diff --check` | Passed before this report was written. |

No validator was skipped.

## Identity and Grounding

The raw GOLD identity supports the generated source attestation exactly.
`data/raw/gold_ecosystem_paths.tsv:708` has the canonical path
`Environmental > Aquatic > Deep subsurface > Shale gas/oil reservoir >
Produced water/Flow back`, leaf label `Produced water/Flow back`, and source
node `gold.ecosystem:7795`; `data/habitats/PATHS.tsv:2371` pins the generated
identifier to `produced_water_flow_back`.

The side inventories make this a high-priority ungrounded row rather than a
bare lexical miss. `data/raw/gold_path_biosamples.tsv:265` maps the exact path
to 86 biosamples under node `7795`. Three GOLD studies carry the path:
`Gs0114675`, `Gs0118431`, and `Gs0127566`. `data/raw/gold_path_triads.tsv`
summarizes those 86 biosamples as:

| Slot | Top term | Share | Studies |
| --- | --- | ---: | ---: |
| broad | `ENVO:00000446` `terrestrial biome` | 1.00 | 3 |
| local | `ENVO:01000941` `planetary subsurface zone` | 1.00 | 3 |
| medium | `ENVO:00002194` `oil field production water` | 0.57 | 2 |

Those MIxS rows are not automatic identity evidence because broad, local, and
medium slots play different roles, and because the medium slot has three
observed terms. They do show that the class-level no-match sweep missed a
nearby material term for the target's sampled medium.

The current strict parent is not supported as an is-a edge. The only parent in
the YAML is `ENVO:00002185`, inherited from the parent GOLD path
`Shale gas/oil reservoir`. That parent path has an item-level `GROUND`
decision at `curation/decisions.tsv:889`, and the generated
`data/habitats/terrestrial/oil_reservoir.yaml` record carries the
`Shale gas/oil reservoir` source attestation as a close match to
`ENVO:00002185`. The ontology defines `ENVO:00002185` `oil reservoir` as a
subsurface landform, while `ENVO:00002194` `oil field production water` is a
child of `ENVO:00002006` `liquid water`. A water material is contained by or
sampled from a reservoir; it is not a kind of reservoir landform.

The slash in `Produced water/Flow back` also needs item-level interpretation.
The existing `Rock core/Sediment` research report notes that GOLD uses slash
labels as disjunctions in leaves such as `Produced water/Flow back` and
`Shale gas/oil reservoir`; that report is not target-specific evidence, but it
is a useful warning not to silently collapse the slash label onto plain
produced water without reading the GOLD nodes and sample metadata.

## Evidence

| Claim | Evidence | Status |
| --- | --- | --- |
| The record denotes the GOLD path `Environmental > Aquatic > Deep subsurface > Shale gas/oil reservoir > Produced water/Flow back`. | `data/raw/gold_ecosystem_paths.tsv:708` lists the canonical path, leaf, one source node, and node `gold.ecosystem:7795`; the generated YAML repeats the node and the exact source path. | Supported exactly. |
| The source attestation has three GOLD organism assertions. | `data/raw/gold_ecosystem_paths.tsv:708` reports `organism_count` 3 and `total_assertions` 3; the generated YAML records `assertion_count: 3` with `assertion_unit: ORGANISM`. | Supported exactly. |
| The target source path is a child of `ENVO:00002185` `oil reservoir`. | The parent path `Environmental > Aquatic > Deep subsurface > Shale gas/oil reservoir` resolves to `ENVO:00002185`, but ENVO defines that term as a landform and the target denotes a water or flowback-water material under that landform. | Unsupported as a strict parent edge. |
| The class-level ungrounded decision is sufficient. | `curation/decisions.tsv:846` is only a `CLASS` review saying no vendored term lexically matched the label; `data/raw/gold_path_triads.tsv:217` points to `ENVO:00002194` as a medium candidate that must be checked by item review. | Incomplete. |
| `Produced water/Flow back` is separate from every `Produced water` sibling. | `data/habitats/PATHS.tsv` pins five produced-water-like GOLD records, and each still has a class-level `CONFIRM_UNGROUNDED` row. The terrestrial `Produced water` sibling already has a review calling for item review against `ENVO:00002194`. | Incomplete until item review decides whether these are duplicates, narrower contexts, or distinct concepts. |

## Completeness

The record is complete for its current generated input state: it has one GOLD
source attestation, the expected assertion count, the generated source-path
parent, and both generated curation-history events. Its empty definition,
synonyms, xrefs, environmental parameters, characteristic taxa, causal graphs,
discussions, and datasets are expected for a class-swept generated record that
has no target-specific maintained term request or causal overlay.

Ignored/hidden-inclusive exact searches for
`habitatmech:GOLD.9272fc9901`, `GOLD.9272fc9901`,
`Produced water/Flow back`, `produced_water_flow_back`, and the exact GOLD
path covered `data/raw/`, `data/habitats/`, `curation/`, `history/`,
`research/`, and `reports/yaml_record_review/`. They found the target YAML,
the locked slug, the class-level decision row, the raw GOLD ecosystem,
biosample, study, and MIxS-triad rows, and no prior exact YAML review, no
target-specific term request or term-request exclusion, no label-drift
exception, no history record, and no causal overlay. The only research hit for
the exact path was the `Rock core/Sediment` report's generic slash-label
example.

The same ignored/hidden-inclusive search traced the relevant siblings:

| Identifier | Generated record | GOLD path |
| --- | --- | --- |
| `habitatmech:GOLD.72719ea056` | `data/habitats/terrestrial/produced_water.yaml` | `Environmental > Terrestrial > Oil reservoir > Produced water` |
| `habitatmech:GOLD.bfd6bfa0f1` | `data/habitats/engineered/produced_water__58649b5f.yaml` | `Engineered > Wastewater > Industrial wastewater > Petroleum reservoir > Produced water` |
| `habitatmech:GOLD.df1d688f27` | `data/habitats/engineered/produced_water__123adb7f.yaml` | `Engineered > Bioreactor > MBR (Membrane bioreactor) > Produced water` |
| `habitatmech:GOLD.e860ad4c9d` | `data/habitats/engineered/produced_water__4b7c7f10.yaml` | `Engineered > Wastewater > Industrial wastewater > Mine water > Produced water` |

All four siblings are also still `review_depth: CLASS`. The terrestrial
`Produced water` review already documents the same `ENVO:00002194` medium
candidate for the oil-reservoir path, so a future curation pass should review
the produced-water cluster rather than deciding this slash-labeled target in
isolation.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | `Produced water/Flow back` inherits `ENVO:00002185` `oil reservoir` as a strict parent even though the target denotes water or flowback water from a reservoir, not a reservoir landform. | `data/habitats/aquatic/produced_water_flow_back.yaml` lists `ENVO:00002185` under `parent_habitats`; `data/raw/ontology_terms.tsv` defines `ENVO:00002185` as a subsurface landform; `ENVO:00002194` is instead a child of `ENVO:00002006` `liquid water`. | `curation/decisions.tsv`; if exact grounding or merging keeps a false source-path parent, add maintained source-parent suppression or edge retyping in the seeder's authoritative inputs. |
| Major | The source concept still has only class-level curation despite local MIxS evidence and same-label siblings that could change its identity. | `curation/decisions.tsv:846` has `review_depth` `CLASS`; `data/raw/gold_path_triads.tsv:217` offers `ENVO:00002194` `oil field production water` as a medium candidate across two studies; four other `Produced water` siblings are still independently minted. | `curation/decisions.tsv`; if the concept stays minted, `curation/term_requests.tsv`; if it merges or grounds to an ontology term, `data/habitats/RETIRED.tsv` and `pages/` after regeneration. |

No blockers or minor findings.

## Recommended Edits

1. Item-review `habitatmech:GOLD.9272fc9901` in
   `curation/decisions.tsv`. Inspect GOLD node `7795`, the 86 biosamples, the
   three exact-path studies, and the GOLD medium terms behind
   `data/raw/gold_path_triads.tsv:217`.
2. Test whether `ENVO:00002194` `oil field production water` exactly denotes
   the slash label `Produced water/Flow back`. If the slash only widens the
   label to two water types, keep the target minted instead of grounding it to
   a narrower material term.
3. Compare the four same-label `Produced water` siblings before choosing the
   final identity. If two source concepts denote the same water material, use a
   `SAME_AS` decision so their GOLD source attestations land on one record.
4. Remove the generated strict `ENVO:00002185` parent from the final produced
   water or flowback-water record. If the record stays minted, define it in
   `curation/term_requests.tsv` with a strict water-material parent and
   `parent_mode=REPLACE`. If it grounds exactly to `ENVO:00002194`, add a
   maintained way to suppress or retype the inherited shale-gas/oil-reservoir
   source-path parent.

## Follow-up Checks

After the item-level decision:

- Run `just seed`.
- If the target stays at `habitatmech:GOLD.9272fc9901`, regenerate it with
  `just seed-apply --force --only habitatmech:GOLD.9272fc9901`.
- If the target grounds to `ENVO:00002194` or merges with a sibling, run
  `just seed-apply --force --prune`, `just redirects`, and `just render`; then
  confirm the old `Produced water/Flow back` URL appears in
  `data/habitats/RETIRED.tsv`.
- Inspect the regenerated record to confirm that `parent_habitats` no longer
  asserts `ENVO:00002185` as an is-a parent for a water material.
- Run `just validate` on the regenerated target path.
- Run `just validate-strict` on the regenerated target path.
- Run `just validate-causal-all`.
- Run `just term-requests-check`.
- Run `just validate-history`.
- Run `just verify-corpus --max-diffs 1`.
- If the identity changed or a stale YAML was pruned, run
  `just redirects-check` and `just render-check`.
- Run `git diff --check`.

## Additional Notes

None found.
