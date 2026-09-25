# YAML Record Review

- Repository: HabitatMech
- Record: `data/habitats/terrestrial/produced_water.yaml`
- Started UTC: 2026-09-25T21:55:05Z
- Finished UTC: 2026-09-25T21:55:17Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Identifier | `habitatmech:GOLD.72719ea056` |
| Label | `Produced water` |
| Class | `HabitatRecord` |
| Category | `TERRESTRIAL` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source concept | GOLD `Environmental > Terrestrial > Oil reservoir > Produced water` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and `curation/decisions.tsv`; the YAML record is read-only |
| Locked slug | `data/habitats/PATHS.tsv:2130` maps `habitatmech:GOLD.72719ea056` to `produced_water` |

The generated record denotes the collapsed GOLD depth-4 path
`Environmental > Terrestrial > Oil reservoir > Produced water`.
`data/raw/gold_ecosystem_paths.tsv:643` lists leaf label `Produced water`,
depth `4`, two GOLD node ids, five organism assertions, no study or biosample
assertions in that source-count table, and node ids
`gold.ecosystem:5427|gold.ecosystem:5428`.

`data/habitats/terrestrial/produced_water.yaml:1-15` preserves that source
identity with the minted identifier, the source label, the exact source path,
the first collapsed source id `gold.ecosystem:5427`, the `ORGANISM` assertion
unit, and a note that the other GOLD node id shares this path.

## Validation

| Command | Result |
| --- | --- |
| `just validate data/habitats/terrestrial/produced_water.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/terrestrial/produced_water.yaml` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; `curation/term_requests.tsv` is current for 109 generated terms. |
| `just validate-history` | Passed; 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; expected and found 3206 records, with 0 missing, 0 extra, and 0 differing files. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-produced-water-worklist.tsv` | Passed; wrote 953 ungrounded rows and listed `habitatmech:GOLD.72719ea056` at output line 220 with only generic water lexical candidates. |
| `just report` | Passed; the corpus report completed and ranked `habitatmech:GOLD.72719ea056` among GOLD paths whose full broad/local/medium triads were corroborated by two studies. |
| `git diff --check` | Passed before the report was written. |

No validator was skipped.

## Identity and Grounding

`data/raw/gold_ecosystem_paths.tsv:643` supports the generated GOLD identity
exactly. The raw row is for
`Environmental > Terrestrial > Oil reservoir > Produced water`, has leaf label
`Produced water`, reports five organism-level assertions for the collapsed
path, and collapses two source nodes: `gold.ecosystem:5427` and
`gold.ecosystem:5428`. The generated source attestation at
`data/habitats/terrestrial/produced_water.yaml:8-15` repeats the first source
node, the exact path, the expected assertion count, the assertion unit, and the
collapsed-node note.

The side inventories add stronger item-level leads than the class-level sweep
read. `data/raw/gold_path_biosamples.tsv:737` maps the exact path to
`gold.ecosystem:5428` with six biosamples. `data/raw/gold_studies.tsv:730`,
`:907`, and `:1086` list the exact path in studies `Gs0112330`, `Gs0116204`,
and `Gs0118423`. `data/raw/gold_path_triads.tsv:908-910` shows that submitter
MIxS triads for the exact path unanimously chose `ENVO:00000446` `terrestrial
biome` as the broad scale, `ENVO:00002185` `oil reservoir` as the local scale,
and `ENVO:00002194` `oil field production water` as the medium.

The only maintained grounding decision is still a lexical class sweep.
`curation/decisions.tsv:679` records `CONFIRM_UNGROUNDED` with no object term,
no object label, no relation, and `review_depth` `CLASS`. The note says no term
in the vendored ontology slice matched by the class-level search routes, and
it explicitly says the sweep did not assess whether the source concept is a
habitat.

The generated parent is also not a defensible is-a parent. The YAML says
`parent_habitats: ENVO:00002185`, but `data/raw/ontology_terms.tsv:7272`
defines `ENVO:00002185` `oil reservoir` as a subsurface landform that contains
fluid hydrocarbons. `data/raw/gold_path_triads.tsv:909` uses that term as the
`local` slot for this path, so the MIxS evidence treats the reservoir as
context around the sampled medium. `data/raw/ontology_terms.tsv:7277` lists the
potential exact medium term `ENVO:00002194` `oil field production water`, and
`data/raw/ontology_subclass_edges.tsv:5389` places that candidate under
`ENVO:00002006` `water`, not under the oil-reservoir landform branch.

## Evidence

| Claim | Evidence | Status |
| --- | --- | --- |
| The record denotes the GOLD path `Environmental > Terrestrial > Oil reservoir > Produced water`. | `data/raw/gold_ecosystem_paths.tsv:643` lists that canonical path, leaf label `Produced water`, and node ids `gold.ecosystem:5427|gold.ecosystem:5428`; `data/habitats/terrestrial/produced_water.yaml:8-15` repeats the first source node, the path, and the collapsed-node note. | Supported exactly. |
| The source attestation's assertion count is five GOLD organism assertions. | `data/raw/gold_ecosystem_paths.tsv:643` reports `organism_count` 5 and `total_assertions` 5 for the collapsed path, and `data/habitats/terrestrial/produced_water.yaml:13-14` records `assertion_count: 5` with `assertion_unit: ORGANISM`. | Supported exactly. |
| `Produced water` is narrower than `ENVO:00002185` `oil reservoir`. | `data/habitats/terrestrial/produced_water.yaml:6-7` asserts `ENVO:00002185` as a parent, but the ontology row at `data/raw/ontology_terms.tsv:7272` defines that term as a subsurface landform, and the exact-path GOLD triad at `data/raw/gold_path_triads.tsv:909` uses it as `local` context rather than the `medium`. | Unsupported. |
| The class-level ungrounded decision had no exact ontology candidate to read. | `curation/decisions.tsv:679` records only a lexical `CLASS` sweep; `data/raw/gold_path_triads.tsv:910` independently records `ENVO:00002194` `oil field production water` for the `medium` slot of the exact path, so an item review must test that candidate before concluding the GOLD concept is ungrounded. | Incomplete. |
| No item-level curation input or causal overlay is attached to this record. | Ignored/hidden-inclusive exact searches for `habitatmech:GOLD.72719ea056`, `gold.ecosystem:5427`, `gold.ecosystem:5428`, and the exact GOLD path found no target-specific row in `curation/term_requests.tsv`, `curation/term_requests_excluded.tsv`, `history/`, `research/`, or `curation/causal_graphs/`, and `find curation/causal_graphs -maxdepth 1 -type f -name 'produced_water.yaml' -print` returned no files. | Supported exactly. |

## Completeness

The record is complete for the currently generated source state but incomplete
as curation. It has the exact GOLD source path, a locked slug, one generated
source-path parent, one class-level `CONFIRM_UNGROUNDED` decision, no
definition, no synonyms, no xrefs, no characteristic taxa, no environmental
parameters, no causal graph, no discussion, and no dataset.

Ignored/hidden-inclusive exact searches covered `curation/decisions.tsv`,
`curation/term_requests.tsv`, `curation/term_requests_excluded.tsv`,
`curation/term_requests/`, `curation/causal_graphs/`, `history/`,
`research/`, `reports/habitat_research_manifest.tsv`,
`conf/id_label_targets.yaml`, `data/habitats/PATHS.tsv`,
`data/habitats/terrestrial/produced_water.yaml`,
`data/raw/gold_ecosystem_paths.tsv`, `data/raw/gold_path_biosamples.tsv`,
`data/raw/gold_studies.tsv`, `data/raw/gold_path_triads.tsv`,
`data/raw/ontology_terms.tsv`, and `data/raw/ontology_subclass_edges.tsv`.
They found the generated target, the locked slug, the source inventory row, the
`curation/decisions.tsv` class-level row, exact-path biosample, study, and
MIxS-triad side evidence, ontology rows for `ENVO:00002185` and
`ENVO:00002194`, and no target-specific term request, excluded term-request
row, history record, committed research report, causal overlay,
label-drift target entry, or pre-existing `*-produced_water.md` review report.

The exact path has five direct GOLD organism assertions, one committed
biosample side-table row for node `5428`, three study side-table rows, and a
three-slot MIxS triad backed by two studies. That is enough local evidence to
reopen the record for item-level curation against `ENVO:00002194`; it is not
enough to assert exact identity without reading the underlying GOLD nodes and
sample metadata, because the candidate term has no definition or synonyms in
the vendored slice.

## Findings

| ID | Severity | Finding | Maintained owner |
| --- | --- | --- | --- |
| HM-PRODUCED-WATER-001 | Major | The generated hierarchy claims `Produced water` is-a `ENVO:00002185` `oil reservoir`. ENVO defines `oil reservoir` as a subsurface landform, while GOLD's exact-path MIxS triad uses `oil reservoir` as `local` context and `ENVO:00002194` `oil field production water` as the `medium`; a produced-water material is not a strict subtype of the landform that contains it. | `curation/decisions.tsv`; if the concept stays minted, add the corrected strict parent in `curation/term_requests.tsv`. |
| HM-PRODUCED-WATER-002 | Major | `Produced water` remains at `review_depth` `CLASS`. The only maintained decision at `curation/decisions.tsv:679` explicitly did not assess habitathood, and its lexical sweep could not see the submitter MIxS medium candidate `ENVO:00002194` `oil field production water` at `data/raw/gold_path_triads.tsv:910`. | `curation/decisions.tsv`; if `ENVO:00002194` is not exact, define the minted record and strict parent in `curation/term_requests.tsv`. |

## Recommended Edits

1. Reopen `habitatmech:GOLD.72719ea056` in `curation/decisions.tsv` with
   `review_depth` `ITEM`; inspect GOLD nodes `5427` and `5428`, the five
   organism assertions, the six node-5428 biosamples, studies `Gs0112330`,
   `Gs0116204`, and `Gs0118423`, and the exact-path MIxS triad.
2. Test whether `ENVO:00002194` `oil field production water` is an exact
   identity for `Environmental > Terrestrial > Oil reservoir > Produced water`.
   If it is exact, replace the class-level `CONFIRM_UNGROUNDED` row with an
   `ITEM`-level `GROUND` decision to `ENVO:00002194`.
3. If `ENVO:00002194` is only a related material or is too underspecified in
   the vendored slice, keep the GOLD concept minted, preserve the relation as a
   narrow/broad/xref decision as appropriate, add an evidence-backed
   `curation/term_requests.tsv` definition, and replace the generated
   `ENVO:00002185` parent with a strict broader water or produced-water parent.

## Follow-up Checks

- `rg --no-ignore --hidden -n 'habitatmech:GOLD\.72719ea056|Environmental > Terrestrial > Oil reservoir > Produced water|gold\.ecosystem:(5427|5428)|ENVO:00002194' curation history research data/habitats data/raw`
- `just seed`
- `just seed-canary habitatmech:GOLD.72719ea056`
- `just seed-apply --force`
- `just validate data/habitats/terrestrial/produced_water.yaml`
- `just validate-strict data/habitats/terrestrial/produced_water.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*produced_water.md' -print` found no pre-existing Produced water review report before this file was written; `find` included ignored files under the searched directory.
- `find curation/causal_graphs -maxdepth 1 -type f -name 'produced_water.yaml' -print` found no slug-matched causal overlay before this report was written; `find` included ignored files under the searched directory.
- `find research history curation/term_requests -iname '*produced*water*' -print` found no target-specific maintained research, history, or term-request files before this report was written; `find` included ignored files under the searched directories.
- `find . -name AGENTS.md -print` found no local `AGENTS.md` files before this report was written; `find` included ignored files under the searched tree.
