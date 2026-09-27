# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/aquatic/deepwater_brine_lake.yaml`
- Started UTC: `2026-09-27T13:07:39Z`
- Finished UTC: `2026-09-27T13:07:39Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/aquatic/deepwater_brine_lake.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.35b68dbb27` |
| Label | `Deepwater/Brine lake` |
| Category | `AQUATIC` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source provenance | GOLD `Environmental > Aquatic > Marine > Deepwater/Brine lake` |
| Generated status | Generated from `data/raw/`, `curation/decisions.tsv`, and `src/habitatmech/seed.py`; `data/habitats/PATHS.tsv` pins `habitatmech:GOLD.35b68dbb27` to `deepwater_brine_lake` |

The complete generated record was read before making this judgment. It contains
a minted GOLD identifier, one parent, one GOLD source attestation, and two
curation-history events. It has no definition, synonyms, xrefs, record-level
evidence, environmental parameters, characteristic taxa, causal graphs,
discussion links, external datasets, or quality flags.

Ignored-inclusive exact searches over `data/raw`, `data/habitats`,
`curation`, `history`, `research`, `reports`, and `conf` for
`habitatmech:GOLD.35b68dbb27`, `gold.ecosystem:8051`,
`gold.ecosystem:8052`, and the exact
`Environmental > Aquatic > Marine > Deepwater/Brine lake` source path found
the expected GOLD raw row, the `curation/decisions.tsv` class-level decision,
the `PATHS.tsv` pin, the generated target, and the generated child reference
from the deeper Sediment GOLD path. The same searches found no term-request
row, causal-graph overlay, history entry, research report, exact-path GOLD
biosample row, exact-path GOLD MIxS triad row, exact-path GOLD study row, or
prior YAML review report for this source concept. Those
`rg --no-ignore --hidden` checks included ignored and hidden files.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/deepwater_brine_lake.yaml` | Passed; LinkML reported no issues. |
| `just validate-all data/habitats/aquatic/deepwater_brine_lake.yaml --out /tmp/habitatmech-deepwater-brine-lake-validate-all.tsv` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-strict data/habitats/aquatic/deepwater_brine_lake.yaml --quiet --out /tmp/habitatmech-deepwater-brine-lake-validate-strict.tsv` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs were valid. |
| `just validate-history` | Passed; 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; the corpus has the expected 3206 records and reproduces exactly from `data/raw/`. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist-deepwater-brine-lake.tsv` | Passed; wrote 953 ungrounded rows and reported 1810 decisions on file. |
| `just report` | Passed; emitted the corpus diagnostic report for 3206 records, including 468 `AQUATIC` records, 2520 `SEEDED` records, 953 `UNGROUNDED` records, and 830 class-level swept ungrounded records. |
| Focused reference validator | Not checked: an ignored-inclusive exact `rg --no-ignore --hidden` search of `justfile`, `.claude`, `docs`, `scripts`, `src`, and `tests` found no `validate-references` or `validate-refs` recipe, and this record has no evidence references or causal graph edges. |

## Identity and Grounding

The source identity is supported. `data/raw/gold_ecosystem_paths.tsv` has one
canonical path row for `Environmental > Aquatic > Marine > Deepwater/Brine lake`,
with leaf label `Deepwater/Brine lake`, depth 4, two collapsed GOLD node IDs
`gold.ecosystem:8051|gold.ecosystem:8052`, and two `ORGANISM` assertions. The
seeder's `mint` helper returns `habitatmech:GOLD.35b68dbb27` for that exact
source path, matching the generated identifier.

The single source attestation is also supported. The generated
`source_id: gold.ecosystem:8051` is the first of the two collapsed node IDs,
the generated `source_label` and `source_path` match the raw path, the note
correctly reports that two node IDs share the path, and `assertion_count: 2`
with `assertion_unit: ORGANISM` matches the raw `organism_count`.

The generated `grounding_status: UNGROUNDED` and `mapping_status: SEEDED`
follow from the class-level `CONFIRM_UNGROUNDED` row in
`curation/decisions.tsv`. That row records a lexical no-match sweep, not an
item-level habitat review, so the source concept remains in the worklist and
is correctly not promoted to `REVIEWED`.

The worklist has no lexical candidate for this source path, but the vendored
ENVO slice does contain `ENVO:00000369` `brine pool` with exact synonym
`marine brine pool`. That term's definition covers hypersaline brine pools on
the ocean basin and its generated `brine_pool.yaml` record is already present
from PREGO. A future curation pass should compare the GOLD
`Deepwater/Brine lake` source concept against `ENVO:00000369` and decide
whether it is exact to ENVO `brine pool`, narrower than it, or a nearby marine
habitat that still needs a distinct term.

The current sole parent is not supported as a strict broader habitat.
`ENVO:00001999` is the record for ENVO `marine water body`, defined in the
vendored slice as a lentic water body composed primarily of marine water. The
target source path denotes GOLD's marine deepwater or brine-lake bin, and its
only deeper GOLD child is `Environmental > Aquatic > Marine > Deepwater/Brine lake > Sediment`.
`ENVO:00000369` shows the relevant distinction: the marine brine-pool term is
located on the ocean basin, but its vendored parents are `lentic water body`
and `hydroform`, not `marine water body`. Brine on the ocean basin is not
therefore strictly a water body composed primarily of marine water.

## Evidence

The record has no record-level evidence objects, causal graph, references, or
curator-authored mechanism claims. Its only source-level claim is the GOLD path
attestation described above, and that claim traces exactly to
`data/raw/gold_ecosystem_paths.tsv`.

The generated `ENVO:00001999` parent is mechanically traceable but
evidentially over-scoped. `parent_habitats` is an is-a slot for strictly
broader habitats; it is not a place to preserve the fact that GOLD filed this
deepwater or brine-lake bin under its broad `Marine` branch.

## Completeness

No committed source rows appear to be omitted from this generated record.
Ignored-inclusive exact searches found no exact-path rows for
`Environmental > Aquatic > Marine > Deepwater/Brine lake` in
`data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, or
`data/raw/gold_studies.tsv`; no `curation/term_requests.tsv` or
`curation/causal_graphs/` entry for `habitatmech:GOLD.35b68dbb27`; and no
PREGO, Madin, BacDive, environment-table, research, or history input for the
source concept. The empty optional slots are therefore expected in the
generated YAML.

The single child GOLD path is intentionally represented by its own generated
record. The exact child row for
`Environmental > Aquatic > Marine > Deepwater/Brine lake > Sediment` points
back to `habitatmech:GOLD.35b68dbb27`; it is not a missing evidence row from
this parent record.

The consequential gap is item-level review. The class-level sweep has only
established that no vendored term matched the label by its automated lexical
routes; it explicitly did not decide whether this source path is a habitat or
whether a novel ENVO request is warranted. Until a curator compares the source
path to `ENVO:00000369`, the record should stay `SEEDED`.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| HM-DEEPWATER-BRINE-LAKE-001 | Major | `parent_habitats` asserts a false or at least unsupported is-a edge from GOLD `Environmental > Aquatic > Marine > Deepwater/Brine lake` to `ENVO:00001999` `marine water body`. | The raw GOLD row places this source under `Environmental > Aquatic > Marine`, and that generated parent record is grounded to `ENVO:00001999`. The vendored ENVO row defines `marine water body` as a kind of lentic water body composed primarily of marine water, while the target denotes GOLD's marine deepwater or brine-lake bin and the relevant ENVO `brine pool` candidate has parents `lentic water body` and `hydroform`, not `marine water body`. | Perform item-level curation in `curation/decisions.tsv`; either ground `habitatmech:GOLD.35b68dbb27` to `ENVO:00000369`, ground it as narrower than `ENVO:00000369`, or add a true definition/genus in `curation/term_requests.tsv` with `parent_mode=REPLACE` so regeneration drops the inherited `ENVO:00001999` parent. |

## Recommended Edits

1. Re-read GOLD `Environmental > Aquatic > Marine > Deepwater/Brine lake`, its
   two collapsed node IDs, and the immediate Sediment child bin; then update
   the existing `curation/decisions.tsv` row for
   `habitatmech:GOLD.35b68dbb27` from a class-level
   `CONFIRM_UNGROUNDED` row to an item-level decision that records the path
   interpretation.
2. Compare the source concept to `ENVO:00000369` `brine pool`. If the GOLD
   bin is an exact marine-brine-pool use, add a `GROUND` decision; if it is a
   stricter subtype, add a `GROUND_AS_PARENT` decision or a
   `curation/term_requests.tsv` row with `parent_mode=REPLACE`; if it is a
   real nearby habitat absent from ENVO, add a term-request row with a strict
   genus that item review confirms.
3. Include a curation-history record for the item-level review and any
   decision or term-request addition before regenerating this record.
4. Regenerate with `just seed`, canary
   `just seed-canary habitatmech:GOLD.35b68dbb27`, inspect
   `data/habitats/aquatic/deepwater_brine_lake.yaml`, and then apply the
   generated change with `just seed-apply --force` once the canary has the
   expected identity and parent set.

## Follow-up Checks

1. Run `just validate data/habitats/aquatic/deepwater_brine_lake.yaml`.
2. Run `just validate-all data/habitats/aquatic/deepwater_brine_lake.yaml`.
3. Run `just validate-history`.
4. Run `just term-requests-check`.
5. Run `just verify-corpus --max-diffs 1`.
6. Run `just render`.
7. Run `just qc`.
8. Re-read the regenerated target and confirm that it keeps the GOLD
   attestation, no longer lists `ENVO:00001999`, and either resolves to
   `ENVO:00000369` or carries an item-reviewed minted identity with only
   strict parents.

## Additional Notes

This record is adjacent to, but distinct from, the existing generated
`ENVO:00000369` `brine pool` record. `brine_pool.yaml` is attested by PREGO,
whereas this review covers only GOLD
`Environmental > Aquatic > Marine > Deepwater/Brine lake`.
