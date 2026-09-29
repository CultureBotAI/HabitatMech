# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/terrestrial/floor_sediment.yaml`
- Started UTC: `2026-09-29T00:00:00Z`
- Finished UTC: `2026-09-29T00:12:23Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.5e356e8cab` |
| Label | `Floor sediment` |
| File | `data/habitats/terrestrial/floor_sediment.yaml` |
| Category | `TERRESTRIAL` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source | `GOLD` |
| Source ID | `gold.ecosystem:5971` |
| Source path | `Environmental > Terrestrial > Deep subsurface > Cave > Floor sediment` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `curation/decisions.tsv`, path-derived parentage, and `data/habitats/PATHS.tsv`; do not edit `data/habitats/terrestrial/floor_sediment.yaml` directly. |

`data/habitats/terrestrial/floor_sediment.yaml` is the generated GOLD-only
record for floor sediment under GOLD's deep-subsurface cave path. Future fixes
belong in `curation/decisions.tsv`, and likely `curation/term_requests.tsv`,
followed by regeneration.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/terrestrial/floor_sediment.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/terrestrial/floor_sediment.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus` | Passed; expected 3,206 records, found 3,206 on disk, 0 missing, 0 extra, 0 differing. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just worklist --status all --out /tmp/habitatmech-floor-sediment-worklist.tsv` | Passed; wrote 953 worklist rows and included this target as a decided GOLD record with `ENVO:00002007` `sediment` among its candidates. |
| `just report --out /tmp/habitatmech-corpus.tsv` | Passed; wrote the corpus report TSV and reported current corpus-level summaries. |
| Target causal overlay validator | Not applicable. Exact ignored/hidden-inclusive searches found no overlay keyed to `habitatmech:GOLD.5e356e8cab`, `gold.ecosystem:5971`, `floor_sediment`, or the full source path; ignored-inclusive `find` found no `*floor*` causal overlay and only generic sediment overlays. |
| Reference validator | Not applicable. The record has no record-level `evidence`, no `characteristic_taxa.reference`, and no `causal_graphs` edges requiring claim-level references. |
| `git diff --check` | Passed before this report was written. |

## Identity and Grounding

The generated source identity is internally stable:

| Claim | Review |
|---|---|
| GOLD source path | Supported. `data/raw/gold_ecosystem_paths.tsv` has exactly `Environmental > Terrestrial > Deep subsurface > Cave > Floor sediment`, leaf `Floor sediment`, one GOLD node, 1 `ORGANISM` assertion, and source id `gold.ecosystem:5971`. |
| Generated identifier | Supported by the committed slug map. `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.5e356e8cab` to `floor_sediment`, matching the generated file. |
| Source attestation | Supported. The generated `source_id`, `source_label`, `source_path`, `assertion_count: 1`, and `assertion_unit: ORGANISM` agree with the raw GOLD ecosystem-path row. |
| Habitat category | Supported. `TERRESTRIAL` follows GOLD's `Environmental > Terrestrial` path prefix. |
| `UNGROUNDED` status | Too weak after item review. The vendored slice has no exact `floor sediment`, `cave floor sediment`, or `cave sediment` term, but it does have `ENVO:00002007` `sediment` as a strict broader environmental-material parent. |
| `habitatmech:GOLD.46abb9a153` `Cave` parent | Incorrect as a strict parent. Floor sediment is deposited material on a cave floor, not a kind of cave. |

`curation/decisions.tsv` contains one row for
`habitatmech:GOLD.5e356e8cab`, a class-level `CONFIRM_UNGROUNDED` from the
August lexical sweep. That row explicitly says the sweep did not assess whether
the concept is a habitat or a term-request candidate, so the generated
`mapping_status: SEEDED` is correct and no item-level human curation is being
claimed.

The closest vendored ontology concept is generic `ENVO:00002007` `sediment`,
defined in the slice as particulate environmental material formed by particle
transport and deposition by flowing liquid. `ENVO:01000019` `cave floor` is
also present, but it denotes a solid surface layer forming the lower boundary
of a cave, not deposited particulate material. The GOLD source path supplies
the cave-floor context needed to interpret the leaf, but the exact material
genus for the record is sediment.

## Evidence

The record's generated claims trace back to maintained inputs:

| Claim | Nearest evidence | Review |
|---|---|---|
| The record represents GOLD `Environmental > Terrestrial > Deep subsurface > Cave > Floor sediment`. | `data/raw/gold_ecosystem_paths.tsv` row for `gold.ecosystem:5971` | Supported exactly. |
| The generated file slug is `floor_sediment`. | `data/habitats/PATHS.tsv` row for `habitatmech:GOLD.5e356e8cab` | Supported exactly. |
| The source path contributes one organism assertion. | `organism_count=1`, `study_count=0`, `biosample_count=0`, and `total_assertions=1` in `data/raw/gold_ecosystem_paths.tsv` | Supported exactly for the committed GOLD KGX inventory. |
| The current curation state is only class-level `CONFIRM_UNGROUNDED`. | `curation/decisions.tsv` row for `habitatmech:GOLD.5e356e8cab` | Supported exactly and insufficient after item review because the source concept is a real habitat with a broader vendored ENVO material term. |
| The direct parent is `habitatmech:GOLD.46abb9a153`. | Generated `parent_habitats` plus `data/habitats/PATHS.tsv` row for `cave__4b02055a` | Mechanically supported but ontologically false for an `is_a` parent: `Cave` contains the sampled floor sediment. |

Exact ignored/hidden-inclusive searches for
`habitatmech:GOLD.5e356e8cab`, `gold.ecosystem:5971`,
`floor_sediment`, and the full source path found the generated YAML, the
`PATHS.tsv` row, the raw GOLD ecosystem row, and the class-level curation row.
They found no target-specific causal overlay, term request, research artifact,
history record, or prior exact YAML review report.

The record has no authored literature evidence, environmental parameters,
characteristic taxa, causal graphs, discussions, or datasets. That is complete
for a raw GOLD-only generated record: exact searches found no target row in
`data/raw/gold_path_biosamples.tsv`, `data/raw/gold_studies.tsv`, or
`data/raw/gold_path_triads.tsv`, and no maintained overlay exists.

## Completeness

| Area | Assessment |
|---|---|
| Definition | Complete as empty for the current `SEEDED` generated state. If the record remains minted after item-level curation, it needs an authored `curation/term_requests.tsv` definition. |
| Synonyms | Complete as empty. GOLD contributes only the exact leaf label `Floor sediment`. |
| Parents | Needs curation. The path-inherited `Cave` parent is contextual, not a strict broader material parent. |
| Source attestation | Complete. The generated GOLD source id, label, path, count, and unit match `data/raw/gold_ecosystem_paths.tsv`. |
| Environmental parameters | Complete as empty. No committed side table has a target row for this exact GOLD path. |
| Characteristic taxa | Complete as empty. No PREGO, BacDive, Madin, or target-specific taxon input attests this exact record. |
| Evidence and graphs | Complete as empty. There are no generated causal edges or curator-authored claims needing claim-level `EvidenceItem` support. |
| Status and audit | Needs curation. The sole decision is class-level and should be replaced by an item-level disposition. |

An ignored-file-inclusive pre-report `find` over
`reports/yaml_record_review` for names containing `floor` or `sediment` found
other floor and sediment reports but no `floor_sediment` report. Exact
ignored/hidden-inclusive searches for `ENVO:01000019` and `cave floor` found
the vendored ontology row but no generated HabitatMech `cave_floor` record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | None found. | The YAML validates, its source attestation agrees with `data/raw/gold_ecosystem_paths.tsv`, and the generated status truthfully remains `SEEDED`. | Not applicable |
| Major | **`Cave` is not a strict broader parent for Floor sediment, and the class-level decision missed `ENVO:00002007` `sediment`.** The target denotes sediment from a cave floor, not a kind of cave. The vendored `sediment` record is the correct broader material parent; `cave floor` is the site whose deposited material the GOLD leaf names. | `data/raw/ontology_terms.tsv` contains `ENVO:00002007` `sediment`, and `/tmp/habitatmech-floor-sediment-worklist.tsv` ranks that term among the target's candidates. Exact target-path searches found no MIxS triad or study row that would justify a more specific ontology grounding. | `curation/decisions.tsv`; probably `curation/term_requests.tsv` if the source stays minted |
| Minor | None found. | Empty optional slots are consistent with the absence of target-specific side-table rows, causal overlays, and source taxa. | Not applicable |

## Recommended Edits

| Priority | Edit | Maintained path |
|---|---|---|
| Major | Replace the class-level row for `habitatmech:GOLD.5e356e8cab` with an item-level `GROUND_AS_PARENT` decision to `ENVO:00002007` `sediment`, yielding `grounding_status: NARROW`. | `curation/decisions.tsv` |
| Major | If Floor sediment stays distinct from generic `ENVO:00002007`, add a `floor sediment` term request with genus parent `ENVO:00002007` and `parent_mode=REPLACE` so regeneration drops the inherited `habitatmech:GOLD.46abb9a153` `Cave` parent. | `curation/term_requests.tsv` |

Do not hand-edit `data/habitats/terrestrial/floor_sediment.yaml`; regenerate it
from the maintained inputs after item-level curation changes.

## Follow-up Checks

After item-level curation, run:

- `just seed`
- `just seed-canary habitatmech:GOLD.5e356e8cab`
- `just seed-apply --force`
- `just validate data/habitats/terrestrial/floor_sediment.yaml`
- `just validate-strict data/habitats/terrestrial/floor_sediment.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus`
- `just worklist --status all --out /tmp/habitatmech-floor-sediment-worklist.tsv`
- `just report`
- `git diff --check`

Before marking the fix done, re-read the regenerated YAML and verify that
`parent_habitats` contains `ENVO:00002007`, no longer contains
`habitatmech:GOLD.46abb9a153`, `grounding_status` is `NARROW`, and the curation
history records an item-level decision rather than the old class-level sweep.

## Additional Notes

- Searches used to establish absence included ignored and hidden files. Broad
  exact content searches covered `data/habitats`, `curation`, `data/raw`,
  `research`, `history`, and `reports/yaml_record_review`; high-volume rendered
  `pages/`, minified text-map JSON, `build/`, and `.git/` outputs were excluded
  from the final absence checks because generated pages are not authoritative
  inputs.
- The already reviewed `habitatmech:GOLD.46abb9a153` parent record documents
  that the deep-subsurface `Cave` path is itself only seeded and still needs
  item-level disposition. That separate cave cleanup does not remove this
  record's own need for a sediment parent.
- The aquatic `Cave pool sediment` and `Cave stream sediment` sibling reviews
  reported the same class of issue: GOLD places sediment leaves under useful
  source contexts, but those path prefixes are not automatically strict
  material parents for the sediment.
