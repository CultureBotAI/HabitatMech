# YAML Record Review

- Repository: HabitatMech
- Record: `data/habitats/engineered/pulp_and_paper_wastewater.yaml`
- Started UTC: 2026-09-25T22:24:48Z
- Finished UTC: 2026-09-25T22:24:48Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Identifier | `habitatmech:GOLD.0ef022fc47` |
| Label | `Pulp and paper wastewater` |
| Class | `HabitatRecord` |
| Category | `ENGINEERED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source concept | GOLD `Engineered > Wastewater > Industrial wastewater > Pulp and paper wastewater` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and `curation/decisions.tsv`; the YAML record is read-only |
| Locked slug | `data/habitats/PATHS.tsv:1391` maps `habitatmech:GOLD.0ef022fc47` to `pulp_and_paper_wastewater` |

The generated record denotes the collapsed GOLD depth-4 path
`Engineered > Wastewater > Industrial wastewater > Pulp and paper wastewater`.
`data/raw/gold_ecosystem_paths.tsv:632` lists leaf label
`Pulp and paper wastewater`, depth `4`, two GOLD node ids, five organism
assertions, no study or biosample assertions in that source-count table, and
node ids `gold.ecosystem:3835|gold.ecosystem:4266`.

`data/habitats/engineered/pulp_and_paper_wastewater.yaml:1-15` preserves that
source identity with the minted identifier, the source label, the exact source
path, the first collapsed source id `gold.ecosystem:3835`, the `ORGANISM`
assertion unit, and a note that the other GOLD node id shares this path.

## Validation

| Command | Result |
| --- | --- |
| `just validate data/habitats/engineered/pulp_and_paper_wastewater.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/engineered/pulp_and_paper_wastewater.yaml` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; `curation/term_requests.tsv` is current for 109 generated terms. |
| `just validate-history` | Passed; 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; expected and found 3206 records, with 0 missing, 0 extra, and 0 differing files. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist.tsv` | Passed; wrote 953 ungrounded rows and listed `habitatmech:GOLD.0ef022fc47` at output line 221 with no lexical candidates. |
| `just report` | Passed; the corpus report completed and did not list `habitatmech:GOLD.0ef022fc47` in a target-specific contradiction or GOLD-triad ranking. |
| `git diff --check` | Passed before the report was written. |

No validator was skipped.

## Identity and Grounding

`data/raw/gold_ecosystem_paths.tsv:632` supports the generated GOLD identity
exactly. The raw row is for
`Engineered > Wastewater > Industrial wastewater > Pulp and paper wastewater`,
has leaf label `Pulp and paper wastewater`, reports five organism-level
assertions for the collapsed path, and collapses two source nodes:
`gold.ecosystem:3835` and `gold.ecosystem:4266`. The generated source
attestation at
`data/habitats/engineered/pulp_and_paper_wastewater.yaml:8-15` repeats the
first source node, the exact path, the expected assertion count, the assertion
unit, and the collapsed-node note.

The current generated parent is defensible as a strict broader habitat.
`data/habitats/engineered/pulp_and_paper_wastewater.yaml:6-7` attaches
`ENVO:01000964`, and the GOLD path itself places the `Pulp and paper
wastewater` leaf under `Industrial wastewater`. The vendored slice labels
`ENVO:01000964` as `industrial wastewater`, defines it as wastewater produced
by industrial activity, and makes it a subclass of `ENVO:00002001` `waste
water` at `data/raw/ontology_terms.tsv:8459` and
`data/raw/ontology_subclass_edges.tsv:6759`.

The slice contains a related narrower term, `ENVO:00002193` `pulp-bleaching
waste water`, at `data/raw/ontology_terms.tsv:7276`, and places it directly
under `ENVO:00002001` `waste water` at
`data/raw/ontology_subclass_edges.tsv:5388`. The GOLD source path does not
restrict the concept to pulp-bleaching effluent, so `ENVO:00002193` is not a
safe exact identity or strict parent for the broader pulp-and-paper wastewater
concept.

The only maintained grounding decision is still a lexical class sweep.
`curation/decisions.tsv:181` records `CONFIRM_UNGROUNDED` with no object term,
no object label, no relation, and `review_depth` `CLASS`. The note says no term
in the vendored ontology slice matched by the class-level search routes, and
it explicitly says the sweep did not assess whether the source concept is a
habitat.

## Evidence

| Claim | Evidence | Status |
| --- | --- | --- |
| The record denotes the GOLD path `Engineered > Wastewater > Industrial wastewater > Pulp and paper wastewater`. | `data/raw/gold_ecosystem_paths.tsv:632` lists that canonical path, leaf label `Pulp and paper wastewater`, and node ids `gold.ecosystem:3835|gold.ecosystem:4266`; `data/habitats/engineered/pulp_and_paper_wastewater.yaml:8-15` repeats the first source node, the path, and the collapsed-node note. | Supported exactly. |
| The source attestation's assertion count is five GOLD organism assertions. | `data/raw/gold_ecosystem_paths.tsv:632` reports `organism_count` 5 and `total_assertions` 5 for the collapsed path, and `data/habitats/engineered/pulp_and_paper_wastewater.yaml:13-14` records `assertion_count: 5` with `assertion_unit: ORGANISM`. | Supported exactly. |
| `Pulp and paper wastewater` is narrower than `ENVO:01000964` `industrial wastewater`. | The GOLD path places the leaf below `Industrial wastewater`, and `data/raw/ontology_terms.tsv:8459` defines `ENVO:01000964` as wastewater from industrial activity. | Supported exactly. |
| No committed GOLD side table adds direct study, biosample, or MIxS-triad context for this exact path. | An ignored/hidden-inclusive exact search for `Engineered > Wastewater > Industrial wastewater > Pulp and paper wastewater`, `gold.ecosystem:3835`, and `gold.ecosystem:4266` across `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, `data/raw/gold_studies.tsv`, and `data/raw/gold_ecosystem_paths.tsv` found only the source inventory row. | Supported for the current raw tables. |
| No item-level curation input or causal overlay is attached to this record. | Ignored/hidden-inclusive exact searches for `habitatmech:GOLD.0ef022fc47`, the exact GOLD path, `gold.ecosystem:3835`, `gold.ecosystem:4266`, and the slug found no target-specific row in `curation/term_requests.tsv`, `curation/term_requests_excluded.tsv`, `history/`, `research/`, or `curation/causal_graphs/`, and `find curation/causal_graphs -maxdepth 1 -type f -name 'pulp_and_paper_wastewater.yaml' -print` returned no files. | Supported exactly. |

## Completeness

The record is complete for the currently generated source state but incomplete
as curation. It has the exact GOLD source path, a locked slug, one
source-derived parent, one class-level `CONFIRM_UNGROUNDED` decision, no
definition, no synonyms, no xrefs, no side-table study or biosample support,
no environmental parameters, no characteristic taxa, no causal graph, no
discussion, and no dataset.

Ignored/hidden-inclusive exact searches covered `curation/decisions.tsv`,
`curation/term_requests.tsv`, `curation/term_requests_excluded.tsv`,
`curation/term_requests/`, `curation/causal_graphs/`, `history/`,
`research/`, `reports/habitat_research_manifest.tsv`,
`conf/id_label_targets.yaml`, `data/habitats/PATHS.tsv`,
`data/habitats/engineered/pulp_and_paper_wastewater.yaml`,
`data/raw/gold_ecosystem_paths.tsv`, `data/raw/gold_path_biosamples.tsv`,
`data/raw/gold_studies.tsv`, `data/raw/gold_path_triads.tsv`,
`data/raw/ontology_terms.tsv`, and `data/raw/ontology_subclass_edges.tsv`.
They found the generated target, the locked slug, the source inventory row, the
`curation/decisions.tsv` class-level row, the strict broader
`ENVO:01000964` parent, the narrower `ENVO:00002193` near miss, and no
target-specific term request, excluded term-request row, history record,
committed research report, causal overlay, direct GOLD side-table row,
label-drift target entry, or pre-existing `*-pulp_and_paper_wastewater.md`
review report.

The exact path has five direct GOLD organism assertions but no committed study,
biosample, or MIxS-triad side-table rows. That is enough context to keep the
source under the current `industrial wastewater` parent, but not enough to
write an evidence-backed definition or decide whether any relation to
`pulp-bleaching waste water` should be retained.

## Findings

| ID | Severity | Finding | Maintained owner |
| --- | --- | --- | --- |
| HM-PULP-PAPER-WASTEWATER-001 | Major | `Pulp and paper wastewater` remains at `review_depth` `CLASS`. The only maintained decision at `curation/decisions.tsv:181` explicitly did not assess habitathood, and no item-level row has confirmed that this GOLD concept is a real wastewater habitat, that `ENVO:01000964` is only a parent, or that the narrower `ENVO:00002193` `pulp-bleaching waste water` is not an exact identity. | `curation/decisions.tsv`; if the concept stays minted, add its definition in `curation/term_requests.tsv`. |

## Recommended Edits

1. Reopen `habitatmech:GOLD.0ef022fc47` in `curation/decisions.tsv` with
   `review_depth` `ITEM`; inspect GOLD nodes `3835` and `4266` and the five
   organism assertions for the exact
   `Engineered > Wastewater > Industrial wastewater > Pulp and paper
   wastewater` path.
2. If the source concept is a real engineered wastewater habitat with no exact
   ontology identity, keep it minted with `CONFIRM_UNGROUNDED`, add an
   evidence-backed `curation/term_requests.tsv` definition, and retain
   `ENVO:01000964` `industrial wastewater` as its strict parent.
3. If the source concept is only a process, facility, or metadata bucket rather
   than a sampled habitat, mark it `NOT_APPLICABLE` and rerun seeding so the
   generated record is retired instead of promoted as a term-request candidate.

## Follow-up Checks

- `rg --no-ignore --hidden -n 'habitatmech:GOLD\.0ef022fc47|Engineered > Wastewater > Industrial wastewater > Pulp and paper wastewater|gold\.ecosystem:(3835|4266)|ENVO:00002193' curation history research data/habitats data/raw`
- `just seed`
- `just seed-canary habitatmech:GOLD.0ef022fc47`
- `just seed-apply --force`
- `just validate data/habitats/engineered/pulp_and_paper_wastewater.yaml`
- `just validate-strict data/habitats/engineered/pulp_and_paper_wastewater.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -type f -iname '*pulp*paper*wastewater*.md' -print` found no pre-existing Pulp and paper wastewater review report before this file was written; `find` included ignored files under the searched directory.
- `find curation/causal_graphs -maxdepth 1 -type f -name 'pulp_and_paper_wastewater.yaml' -print` found no slug-matched causal overlay before this report was written; `find` included ignored files under the searched directory.
- `find research history curation/term_requests -iname '*pulp*paper*wastewater*' -print` found no target-specific maintained research, history, or term-request files before this report was written; `find` included ignored files under the searched directories.
- `find . -name AGENTS.md -print` found no local `AGENTS.md` files before this report was written; `find` included ignored files under the searched tree.
