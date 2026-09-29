# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/terrestrial/flow_back_produced_fluids.yaml`
- Started UTC: `2026-09-29T00:32:00Z`
- Finished UTC: `2026-09-29T00:40:26Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.d96dd38f86` |
| Label | `Flow back/Produced fluids` |
| File | `data/habitats/terrestrial/flow_back_produced_fluids.yaml` |
| Category | `TERRESTRIAL` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source | `GOLD` |
| Source ID | `gold.ecosystem:5876` |
| Source path | `Environmental > Terrestrial > Deep subsurface > Shale gas reservoir > Flow back/Produced fluids` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `curation/decisions.tsv`, path-derived parentage, and `data/habitats/PATHS.tsv`; do not edit `data/habitats/terrestrial/flow_back_produced_fluids.yaml` directly. |

`data/habitats/terrestrial/flow_back_produced_fluids.yaml` is the generated
GOLD-only record for a flowback/produced-fluids leaf under GOLD's
terrestrial, deep-subsurface shale-gas-reservoir path. Future fixes belong in
`curation/decisions.tsv`, possibly `curation/term_requests.tsv`, followed by
regeneration.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/terrestrial/flow_back_produced_fluids.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/terrestrial/flow_back_produced_fluids.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus` | Passed; expected 3,206 records, found 3,206 on disk, 0 missing, 0 extra, 0 differing. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just worklist --status all --out /tmp/habitatmech-flowback-worklist.tsv` | Passed; wrote 953 worklist rows and listed `habitatmech:GOLD.d96dd38f86` as a decided GOLD record with no lexical ontology candidates. |
| `just report --out /tmp/habitatmech-corpus.tsv` | Passed; wrote the corpus report TSV and reported 3,206 generated records. |
| Target causal overlay validator | Not applicable. Ignored-inclusive `find` found no `*flow*`, `*produced*`, or `*shale*` causal overlay under `curation/causal_graphs`. Exact ignored/hidden-inclusive searches found no overlay keyed to `habitatmech:GOLD.d96dd38f86`, `gold.ecosystem:5876`, `flow_back_produced_fluids`, or the exact source path. |
| Reference validator | Not applicable. The record has no record-level `evidence`, no `characteristic_taxa.reference`, and no `causal_graphs` edges requiring claim-level references. |
| `git diff --check` | Passed before this report was written. |

## Identity and Grounding

The generated source identity is internally stable:

| Claim | Review |
|---|---|
| GOLD source path | Supported. `data/raw/gold_ecosystem_paths.tsv` has exactly `Environmental > Terrestrial > Deep subsurface > Shale gas reservoir > Flow back/Produced fluids`, leaf `Flow back/Produced fluids`, one GOLD node, zero older KGX assertions, and source id `gold.ecosystem:5876`. |
| Generated identifier | Supported by the committed slug map. `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.d96dd38f86` to `flow_back_produced_fluids`, matching the generated file. |
| Source attestation | Supported. The generated `source_id`, `source_label`, and `source_path` agree with the raw GOLD ecosystem-path row. The absence of generated `assertion_count` is also supported because the raw row reports `total_assertions=0`. |
| Habitat category | Supported. `TERRESTRIAL` follows GOLD's `Environmental > Terrestrial` path prefix. |
| `UNGROUNDED` status | Plausible but incomplete. Exact vendored-slice searches found no exact `Flow back/Produced fluids`, `flowback`, or `produced fluids` class. The slice does contain broader fluid/material terms, including `ENVO:02000140` `fluid environmental material`, `ENVO:01000815` `liquid environmental material`, `ENVO:00002194` `oil field production water`, `ENVO:01001869` `fracking liquid`, and `ENVO:03600007` `formation fluid`; which is strict enough for this slash label needs item-level review. |
| `habitatmech:GOLD.2e9692d86d` `Shale gas reservoir` parent | Incorrect as a strict parent. Flowback and produced fluids are materials from a shale gas reservoir, not a kind of reservoir. |

`curation/decisions.tsv` contains one row for
`habitatmech:GOLD.d96dd38f86`, a class-level `CONFIRM_UNGROUNDED` from the
August lexical sweep. That row explicitly says the sweep did not assess whether
the concept is a habitat or a term-request candidate, so the generated
`mapping_status: SEEDED` is correct. `curation/samples/class_swept_unscreened-20260814.tsv`
later sampled this source concept and marked it as a real habitat, but the
sample did not add an item-level grounding decision.

The newer GOLD API side rows reinforce that this target denotes a sampled
material rather than a reservoir class. `data/raw/gold_path_biosamples.tsv`
has 12 biosamples for the exact path under node `5876`, and
`data/raw/gold_studies.tsv` has one study spanning this exact target and
`Environmental > Terrestrial > Deep subsurface > Oil well`. The exact-path
`data/raw/gold_path_triads.tsv` rows have one study behind `freshwater
environment`, `well`, and `estuarine open water upper water column` context.
Those GOLD triads are useful source context but should not be promoted to
identity: their `broad`, `local`, and `medium` slots serve different MIxS
roles, and the upper-water-column medium is suspiciously generic for a
shale-gas-reservoir fluid path.

## Evidence

The record's generated claims trace back to maintained inputs:

| Claim | Nearest evidence | Review |
|---|---|---|
| The record represents GOLD `Environmental > Terrestrial > Deep subsurface > Shale gas reservoir > Flow back/Produced fluids`. | `data/raw/gold_ecosystem_paths.tsv` row for `gold.ecosystem:5876` | Supported exactly. |
| The generated file slug is `flow_back_produced_fluids`. | `data/habitats/PATHS.tsv` row for `habitatmech:GOLD.d96dd38f86` | Supported exactly. |
| The generated source attestation omits `assertion_count`. | `organism_count=0`, `study_count=0`, `biosample_count=0`, and `total_assertions=0` in `data/raw/gold_ecosystem_paths.tsv` | Supported exactly for the committed GOLD KGX count inventory. Newer GOLD API side tables have 12 biosamples for the path, but those are not the older KGX count channel used in `source_attestations`. |
| The current curation state is only class-level `CONFIRM_UNGROUNDED`. | `curation/decisions.tsv` row for `habitatmech:GOLD.d96dd38f86` | Supported exactly and insufficient after item review because the source concept is a real fluid habitat with broader vendored fluid/material terms. |
| The direct parent is `habitatmech:GOLD.2e9692d86d`. | Generated `parent_habitats` plus `data/habitats/PATHS.tsv` row for `shale_gas_reservoir` | Mechanically supported but ontologically false for an `is_a` parent: the shale-gas-reservoir path contains the sampled fluid. |

Exact ignored/hidden-inclusive searches for
`habitatmech:GOLD.d96dd38f86`, `gold.ecosystem:5876`,
`flow_back_produced_fluids`, and the full source path found the generated YAML,
the `PATHS.tsv` row, the raw GOLD ecosystem, biosample, study, and MIxS rows,
the class-level curation row, and the class-sweep sample row. They found no
target-specific causal overlay, term request, research artifact, history
record, or prior exact YAML review report.

The record has no authored literature evidence, environmental parameters,
characteristic taxa, causal graphs, discussions, or datasets. That is complete
for a raw GOLD-only generated record: no PREGO, BacDive, Madin, or
curator-authored maintained input attests this exact source concept.

## Completeness

| Area | Assessment |
|---|---|
| Definition | Complete as empty for the current `SEEDED` generated state. If the record remains minted after item-level curation, it needs an authored `curation/term_requests.tsv` definition. |
| Synonyms | Complete as empty. GOLD contributes only the exact leaf label `Flow back/Produced fluids`. |
| Parents | Needs curation. The path-inherited `Shale gas reservoir` parent is contextual, not a strict broader material parent. |
| Source attestation | Complete. The generated GOLD source id, label, and path match `data/raw/gold_ecosystem_paths.tsv`; the missing assertion count is consistent with `total_assertions=0`. |
| Environmental parameters | Complete as empty. No committed maintained parameter table row was found for this exact GOLD path. |
| Characteristic taxa | Complete as empty. The record has no PREGO, BacDive, Madin, or target-specific taxon input. |
| Evidence and graphs | Complete as empty. There are no generated causal edges or curator-authored claims needing claim-level `EvidenceItem` support. |
| Status and audit | Needs curation. The sole decision is class-level and should be replaced by an item-level disposition. |

An ignored-file-inclusive pre-report `find` over
`reports/yaml_record_review` found no `*flow_back_produced_fluids*` report.
A broader ignored-file-inclusive `find` for `*flow*` found only
`diffuse_flow`, `produced_water_flow_back`, and
`uasb_upflow_anaerobic_sludge_blanket` reports. Exact ignored/hidden-inclusive
content searches for the target identifier and source id under
`reports/yaml_record_review` also found no prior report.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | None found. | The YAML validates, its source attestation agrees with `data/raw/gold_ecosystem_paths.tsv`, and the generated status truthfully remains `SEEDED`. | Not applicable |
| Major | **`Shale gas reservoir` is not a strict broader parent for Flow back/Produced fluids.** The source path parent is the reservoir containing or yielding the fluids, while the leaf names a fluid material. Keeping this edge as `parent_habitats` makes the record claim that produced or flowback fluids are a kind of shale gas reservoir. | `data/habitats/terrestrial/flow_back_produced_fluids.yaml` lists `habitatmech:GOLD.2e9692d86d` under `parent_habitats`; `data/habitats/terrestrial/shale_gas_reservoir.yaml` shows that identifier is the reservoir parent path; the target GOLD leaf is `Flow back/Produced fluids`. | `curation/decisions.tsv`; probably `curation/term_requests.tsv` if the source stays minted |
| Major | **The source concept still has only class-level curation despite being an individually sampled real habitat.** The class sweep only showed that no exact vendored term matched the label; it did not choose among broader fluid/material terms or decide whether `Flow back/Produced fluids` should merge with any `Produced water` or `Produced water/Flow back` sibling. | `curation/samples/class_swept_unscreened-20260814.tsv` screened the source as a habitat; `data/raw/gold_path_biosamples.tsv` has 12 biosamples for the exact GOLD path; the vendored slice has broader fluid terms but exact worklist output offers no lexical candidate for this slash label. | `curation/decisions.tsv`; sibling comparison may need additional `SAME_AS` or grounding decisions |
| Minor | None found. | Empty optional slots are consistent with the absence of maintained target-specific parameter, taxon, evidence, and causal overlay rows. | Not applicable |

## Recommended Edits

| Priority | Edit | Maintained path |
|---|---|---|
| Major | Replace the class-level row for `habitatmech:GOLD.d96dd38f86` with an item-level curation decision. If no exact ontology term covers both sides of the slash label, keep the record minted with `GROUND_AS_PARENT` to a strict broader fluid/material term. | `curation/decisions.tsv` |
| Major | If this source concept stays minted, add a `Flow back/Produced fluids` term request with a supported fluid/material genus and `parent_mode=REPLACE` so regeneration drops the inherited `habitatmech:GOLD.2e9692d86d` `Shale gas reservoir` parent. | `curation/term_requests.tsv` |
| Major | Compare `Flow back/Produced fluids` to the aquatic `Produced water/Flow back` source and other `Produced water` siblings before choosing the final identity. Use an exact grounding or merge only if item-level evidence shows the source concepts denote the same material; do not collapse the flowback slash label onto `ENVO:00002194` `oil field production water` without evidence that the flowback side is in scope. | `curation/decisions.tsv`; possibly redirects and rendered pages after regeneration if records merge |

Do not hand-edit `data/habitats/terrestrial/flow_back_produced_fluids.yaml`;
regenerate it from maintained inputs after item-level curation changes.

## Follow-up Checks

After item-level curation, run:

- `just seed`
- `just seed-canary habitatmech:GOLD.d96dd38f86` if the record stays minted
- `just seed-apply --force`
- `just redirects` and `just render` if a merge deletes an old generated YAML
- `just validate data/habitats/terrestrial/flow_back_produced_fluids.yaml` if the record stays minted
- `just validate-strict data/habitats/terrestrial/flow_back_produced_fluids.yaml` if the record stays minted
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus`
- `just worklist --status all --out /tmp/habitatmech-flowback-worklist.tsv`
- `just report`
- `just redirects-check` and `just render-check` if any record merged or a URL moved
- `git diff --check`

Before marking the fix done, re-read the regenerated YAML or merged target and
verify that no strict parent asserts a produced or flowback fluid is a kind of
shale gas reservoir.

## Additional Notes

- Searches used to establish absence included ignored and hidden files. Broad
  exact content searches covered `data/habitats`, `curation`, `data/raw`,
  `research`, `history`, and `reports/yaml_record_review`; high-volume rendered
  `pages/`, minified text-map JSON, `build/`, and `.git/` outputs were excluded
  from the final absence checks because generated pages are not authoritative
  inputs.
- Ignored-inclusive `find` checks also covered
  `curation/causal_graphs`; no likely `*flow*`, `*produced*`, or `*shale*`
  overlay filename exists.
- The already reviewed aquatic `Produced water/Flow back` record documents the
  same broader identity question around shale-reservoir fluids and
  `ENVO:00002194` `oil field production water`, but it is a separate GOLD
  path under `Environmental > Aquatic > Deep subsurface > Shale gas/oil reservoir`.
