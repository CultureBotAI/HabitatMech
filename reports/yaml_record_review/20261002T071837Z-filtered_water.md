# YAML Record Review: Filtered water

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/aquatic/filtered_water.yaml`
- Started UTC: 2026-10-02T07:18:37Z
- Finished UTC: 2026-10-02T07:26:50Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Path | `data/habitats/aquatic/filtered_water.yaml` |
| Identifier | `habitatmech:GOLD.5f9ddabb4f` |
| Label | `Filtered water` |
| Category | `AQUATIC` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source concept | `GOLD:Environmental > Aquatic > Freshwater > Drinking water > Filtered water` |
| Locked slug | `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.5f9ddabb4f` to `filtered_water` |
| Generated status | Generated from `data/raw/` inventories plus the class-level lexical sweep row in `curation/decisions.tsv` |
| Rendered page | `pages/habitats/filtered-water-habitatmech-gold-5f9ddabb4f.html` |

The full generated record is a 27-line GOLD-derived `UNGROUNDED` record with
one source attestation, one GOLD parent-path parent, no definition, no
environmental parameters, no characteristic taxa, no causal graph, and two
curation-history entries.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/aquatic/filtered_water.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/filtered_water.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus` | Passed; expected 3,206 records, found 3,206 on disk, with 0 missing, 0 extra, and 0 differing records. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the committed term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just worklist --status all --out /tmp/habitatmech-filtered-water-worklist.tsv` | Passed; the target remains in the exported worklist as row 321 with lexical candidate parents `ENVO:00005791` `sterile water`, `ENVO:01000940` `fissure water`, `ENVO:01000599` `river water`, and `ENVO:00002011` `fresh water`. |
| `just report --out /tmp/habitatmech-filtered-water-report.tsv` | Passed; row 1,991 reports this target as `AQUATIC`, `UNGROUNDED`, `SEEDED`, source `GOLD`, 1 source, 1 assertion, `has_definition=False`, 1 parent, 0 parameters, 0 taxa, and 0 causal graphs at `data/habitats/aquatic/filtered_water.yaml`. |

## Identity and Grounding

The generated identity and source attestation trace to maintained inputs:

| Claim | Maintained input |
|---|---|
| Stable slug | `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.5f9ddabb4f` to `filtered_water`. |
| Class-level sweep | `curation/decisions.tsv` has a `CLASS`-depth `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.5f9ddabb4f`, recording that no ontology term matched the leaf label by lexical routes and that habitathood was not assessed. |
| GOLD source path | `data/raw/gold_ecosystem_paths.tsv` has one canonical path row for `Environmental > Aquatic > Freshwater > Drinking water > Filtered water`, leaf label `Filtered water`, source ID `gold.ecosystem:5122`, 1 GOLD ecosystem node, and 1 `ORGANISM` assertion. |
| GOLD parent path | `data/raw/gold_ecosystem_paths.tsv` records the direct parent path `Environmental > Aquatic > Freshwater > Drinking water`; the generated parent record is `data/habitats/aquatic/drinking_water__6d6ef579.yaml`, pinned by `data/habitats/PATHS.tsv` to `habitatmech:GOLD.99a88ecb51`. |
| Sibling separation | The committed GOLD inventory keeps `Unchlorinated`, `Untreated`, `Delivery networks`, `Chlorinated`, `Filtered water`, and `Chloraminated` as separate children of `Environmental > Aquatic > Freshwater > Drinking water`. |

`Filtered water` is a specific drinking-water treatment state, not a synonym of
generic drinking water and not a duplicate of the sibling chlorinated,
chloraminated, unchlorinated, untreated, or delivery-network leaves. Exact and
near-term ignored/hidden-inclusive searches for `filtrat`, `filtered`,
`filter(ed|ing)? water`, `drinking water`, and `potable` over
`data/raw/ontology_terms.tsv`, `curation/decisions.tsv`, and
`curation/term_requests.tsv` found `ENVO:00003064` `drinking water`, several
drinking-water infrastructure terms, and unrelated filtration/process matches,
but no exact ontology identity or authored term-request row for a
filtered-drinking-water habitat.

The target also lacks GOLD MIxS triad support: exact ignored/hidden-inclusive
searches of `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`,
and `data/raw/gold_studies.tsv` found no row for
`Environmental > Aquatic > Freshwater > Drinking water > Filtered water` or
`gold.ecosystem:5122`. That absence is consistent with the raw ecosystem-path row
reporting one organism assertion but zero study or biosample counts.

## Completeness

The generated YAML is complete for the current maintained inputs. It includes
the GOLD source path, node ID, organism assertion count, generated category,
class-depth lexical decision, seed provenance, and generated broader source-path
parent. The rendered page repeats the same public claims and still links this
record under `Drinking water`.

Empty optional slots are expected at this stage:

| Empty slot | Assessment |
|---|---|
| `definition` / `definition_source` | No `curation/term_requests.tsv` row defines `habitatmech:GOLD.5f9ddabb4f`; the current `CLASS` decision is not enough to mark this as a reviewed novel term. |
| `synonyms` / `xrefs` | No maintained row supplies a synonym or external xref for the source-scoped filtered-drinking-water concept. |
| `environmental_parameters` | No raw GOLD MIxS triad rows exist for the exact `Filtered water` source path. |
| `characteristic_taxa` | The target is GOLD-only, and GOLD contributes only source assertion counts. |
| `causal_graphs` / claim-level `evidence` | Exact ignored/hidden-inclusive searches found no target overlay under `curation/causal_graphs`. |

Ignored/hidden-inclusive exact searches covered `curation`, `data/raw`,
`data/habitats`, `history`, `research`, `reports/yaml_record_review`, and
`pages/habitats` for `habitatmech:GOLD.5f9ddabb4f`, `5f9ddabb4f`,
`filtered_water`, `gold.ecosystem:5122`, and the exact GOLD source path. They
found the locked slug, the generated record, the rendered page, the class-level
sweep row, sibling-review mentions, and the exact raw GOLD path. They found no
item-level decision, term request, causal overlay, history event, research
report, prior exact YAML review report, biosample row, triad row, or study row
for this source concept.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| HM-FILTERED-WATER-001 | Major | The `Filtered water` source concept still needs item-level curation and a definition if retained as minted. | `curation/decisions.tsv` records only a `CLASS`-depth `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.5f9ddabb4f`, and that row explicitly did not assess whether the concept is a habitat. The full GOLD path places `Filtered water` under `Environmental > Aquatic > Freshwater > Drinking water` beside other treatment-state leaves, but exact ignored/hidden-inclusive searches found no exact filtered-drinking-water ontology term, no `curation/term_requests.tsv` row, and no item-level decision. | Replace the class-level `curation/decisions.tsv` row with an item-level decision. If final review confirms no exact ontology identity exists, keep the source concept `CONFIRM_UNGROUNDED` and add a `curation/term_requests.tsv` definition under `ENVO:00003064` `drinking water`. |

No blocker or minor findings were found.

## Recommended Edits

1. Replace the existing `CLASS`-depth `curation/decisions.tsv` row for
   `habitatmech:GOLD.5f9ddabb4f` with an `ITEM`-depth decision. If final item
   review confirms no exact ontology term exists, keep the minted identifier
   with `CONFIRM_UNGROUNDED`.

2. Add a `curation/term_requests.tsv` row defining filtered drinking water as a
   novel child of `ENVO:00003064` `drinking water`. Preserve the generated GOLD
   parent-path edge to `habitatmech:GOLD.99a88ecb51` unless item review finds
   that the source hierarchy itself is too broad.

3. Regenerate the corpus from maintained inputs and confirm
   `data/habitats/aquatic/filtered_water.yaml` is still minted, has the same GOLD
   source attestation for `gold.ecosystem:5122`, has the generated `Drinking
   water` parent, receives the authored definition, and becomes
   `mapping_status: REVIEWED`.

## Follow-up Checks

After the future item-level decision and term request, rerun:

- `just seed`
- `just seed-canary habitatmech:GOLD.5f9ddabb4f`
- `just validate data/habitats/aquatic/filtered_water.yaml`
- `just validate-strict data/habitats/aquatic/filtered_water.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus`
- `just render`
- `just report`

Also manually confirm the replacement decision is keyed to
`habitatmech:GOLD.5f9ddabb4f`, uses `review_depth: ITEM`, keeps the source
separate from the sibling drinking-water leaves, and does not ground this source
to a generic water or filtration-process term.

## Additional Notes

The sibling chlorinated and chloraminated reviews found the same curation-depth
gap for their own treatment-state leaves. `Filtered water` has less GOLD
evidence than `Chlorinated` because it has no committed MIxS triads or study
rows, but its current issue is identical: the generated record is structurally
consistent and still needs item-level curation to decide and define the novel
filtered-drinking-water concept.
