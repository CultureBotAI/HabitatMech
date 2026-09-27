# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/aquatic/deep_subsurface__f51dcfb9.yaml`
- Started UTC: `2026-09-27T12:36:21Z`
- Finished UTC: `2026-09-27T12:36:21Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/aquatic/deep_subsurface__f51dcfb9.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.3841c9c3af` |
| Label | `Deep subsurface` |
| Category | `AQUATIC` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source provenance | GOLD `Environmental > Aquatic > Marine > Deep subsurface` |
| Generated status | Generated from `data/raw/`, `curation/decisions.tsv`, and `src/habitatmech/seed.py`; `data/habitats/PATHS.tsv` pins `habitatmech:GOLD.3841c9c3af` to `deep_subsurface__f51dcfb9` |

The complete generated record was read before making this judgment. It contains
a minted GOLD identifier, one parent, one GOLD source attestation, and two
curation-history events. It has no definition, synonyms, xrefs, record-level
evidence, environmental parameters, characteristic taxa, causal graphs,
discussion links, external datasets, or quality flags.

Ignored-inclusive exact searches over `data/raw`, `data/habitats`,
`curation`, `history`, `research`, `reports`, and `conf` for
`habitatmech:GOLD.3841c9c3af`, `gold.ecosystem:5368`, `gold.ecosystem:5369`,
and the exact `Environmental > Aquatic > Marine > Deep subsurface` source path
found the expected GOLD raw row, `curation/decisions.tsv` class-level
decision, `PATHS.tsv` pin, generated target, and generated child references
from deeper GOLD paths. The same searches found no term-request row,
causal-graph overlay, history entry, research report, exact-path GOLD
biosample row, exact-path GOLD MIxS triad row, exact-path GOLD study row, or
prior YAML review report for this source concept. Those
`rg --no-ignore --hidden` checks included ignored and hidden files.

Two other generated GOLD records have the same leaf label but are distinct
source concepts: `Environmental > Aquatic > Deep subsurface` is
`habitatmech:GOLD.21222434e2`, and `Environmental > Terrestrial > Deep
subsurface` is `habitatmech:GOLD.151ba43519`. This review covers only
`data/habitats/aquatic/deep_subsurface__f51dcfb9.yaml`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/deep_subsurface__f51dcfb9.yaml` | Passed; LinkML reported no issues. |
| `just validate-all data/habitats/aquatic/deep_subsurface__f51dcfb9.yaml --out /tmp/habitatmech-deep-subsurface-f51dcfb9-validate-all.tsv` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-strict data/habitats/aquatic/deep_subsurface__f51dcfb9.yaml --quiet --out /tmp/habitatmech-deep-subsurface-f51dcfb9-validate-strict.tsv` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs were valid. |
| `just validate-history` | Passed; 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; the corpus has the expected 3206 records and reproduces exactly from `data/raw/`. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist-deep-subsurface-f51dcfb9.tsv` | Passed; wrote 953 ungrounded rows and reported 1810 decisions on file. |
| `just report` | Passed; emitted the corpus diagnostic report for 3206 records, including 468 `AQUATIC` records, 2520 `SEEDED` records, 953 `UNGROUNDED` records, and 830 class-level swept ungrounded records. |
| Focused reference validator | Not checked: an ignored-inclusive exact `rg --no-ignore --hidden` search of `justfile`, `.claude`, `docs`, `scripts`, `src`, and `tests` found no `validate-references` or `validate-refs` recipe, and this record has no evidence references or causal graph edges. |

## Identity and Grounding

The source identity is supported. `data/raw/gold_ecosystem_paths.tsv` has one
canonical path row for `Environmental > Aquatic > Marine > Deep subsurface`,
with leaf label `Deep subsurface`, depth 4, two collapsed GOLD node IDs
`gold.ecosystem:5368|gold.ecosystem:5369`, and 21 `ORGANISM` assertions. The
seeder's `mint` helper returns `habitatmech:GOLD.3841c9c3af` for that exact
source path, matching the generated identifier.

The single source attestation is also supported. The generated
`source_id: gold.ecosystem:5368` is the first of the two collapsed node IDs,
the generated `source_label` and `source_path` match the raw path, the note
correctly reports that two node IDs share the path, and
`assertion_count: 21` with `assertion_unit: ORGANISM` matches the raw
`organism_count`.

The generated `grounding_status: UNGROUNDED` and `mapping_status: SEEDED`
follow from the class-level `CONFIRM_UNGROUNDED` row in
`curation/decisions.tsv`. That row records a lexical no-match sweep, not an
item-level habitat review, so the source concept remains in the worklist and
is correctly not promoted to `REVIEWED`. The worklist still surfaces only an
irrelevant lexical candidate, `UBERON:0010409` `eye surface`, for this target.

The current sole parent is not supported as a strict broader habitat.
`ENVO:00001999` is the record for ENVO `marine water body`, defined in the
vendored slice as a lentic water body composed primarily of marine water. The
target GOLD path is a marine deep-subsurface grouping whose immediate GOLD
children include `Sediment`, `Hydrocarbon`, and `Rock`, and `Hydrocarbon` has
already been reviewed as a non-habitat chemical source concept. The raw path
explains how the edge was generated: `Environmental > Aquatic > Marine` is the
source parent of `Environmental > Aquatic > Marine > Deep subsurface`, and the
`Environmental > Aquatic > Marine` record resolves to `ENVO:00001999`, but a
marine deep-subsurface bin is not itself a kind of lentic marine water body.

## Evidence

The record has no record-level evidence objects, causal graph, references, or
curator-authored mechanism claims. Its only source-level claim is the GOLD path
attestation described above, and that claim traces exactly to
`data/raw/gold_ecosystem_paths.tsv`.

The generated `ENVO:00001999` parent is mechanically traceable but
evidentially over-scoped. `parent_habitats` is an is-a slot for strictly
broader habitats; it is not a place to preserve the fact that GOLD filed this
deep-subsurface bin under its broad `Marine` branch. A future curation row can
define the minted source concept under a true subsurface parent and use
`parent_mode=REPLACE` to drop the inherited `marine water body` edge.

## Completeness

No committed source rows appear to be omitted from this generated record.
Ignored-inclusive exact searches found no exact-path rows for
`Environmental > Aquatic > Marine > Deep subsurface` in
`data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, or
`data/raw/gold_studies.tsv`; no `curation/term_requests.tsv` or
`curation/causal_graphs/` entry for `habitatmech:GOLD.3841c9c3af`; and no
PREGO, Madin, BacDive, environment-table, research, or history input for the
source concept. The empty optional slots are therefore expected in the
generated YAML.

The child GOLD paths are intentionally represented by their own generated
records. The exact child rows for
`Environmental > Aquatic > Marine > Deep subsurface > Sediment`,
`Environmental > Aquatic > Marine > Deep subsurface > Hydrocarbon`, and
`Environmental > Aquatic > Marine > Deep subsurface > Rock` each point back to
`habitatmech:GOLD.3841c9c3af`; they are not missing evidence rows from this
parent record.

The consequential gap is item-level review. The class-level sweep has only
established that no vendored term matched the label by its automated lexical
routes; it explicitly did not decide whether this source path is a habitat or
whether a novel ENVO request is warranted. Until a curator performs that
item-level review, the record should stay `SEEDED`.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| HM-DEEP-SUBSURFACE-F51DCFB9-001 | Major | `parent_habitats` asserts a false or at least unsupported is-a edge from GOLD `Environmental > Aquatic > Marine > Deep subsurface` to `ENVO:00001999` `marine water body`. | The raw GOLD row places this source under `Environmental > Aquatic > Marine`, and `data/habitats/PATHS.tsv` maps that parent source record to `ENVO:00001999`. The vendored ENVO row defines `marine water body` as a kind of lentic water body, while the target record denotes the GOLD marine deep-subsurface bin that has deeper Sediment, Hydrocarbon, and Rock source paths. | Perform item-level curation in `curation/decisions.tsv`, add a definition and true genus for `habitatmech:GOLD.3841c9c3af` in `curation/term_requests.tsv`, and use `parent_mode=REPLACE` so regeneration drops the inherited `ENVO:00001999` parent. |

## Recommended Edits

1. Re-read GOLD `Environmental > Aquatic > Marine > Deep subsurface`, its two
   collapsed node IDs, and the immediate Sediment, Hydrocarbon, and Rock child
   bins; then update the existing `curation/decisions.tsv` row for
   `habitatmech:GOLD.3841c9c3af` from a class-level `CONFIRM_UNGROUNDED` row
   to an item-level decision that records the path interpretation.
2. Add a `curation/term_requests.tsv` row for
   `habitatmech:GOLD.3841c9c3af` with a label that carries the missing marine
   deep-subsurface context, a strict subsurface environmental genus such as
   `ENVO:01001045` or `ENVO:01001046` if item review confirms it, and
   `parent_mode=REPLACE` to remove `ENVO:00001999`.
3. Include a curation-history record for the item-level review and term-request
   addition before regenerating this record.
4. Regenerate with `just seed`, canary
   `just seed-canary habitatmech:GOLD.3841c9c3af`, inspect
   `data/habitats/aquatic/deep_subsurface__f51dcfb9.yaml`, and then apply the
   generated change with `just seed-apply --force` once the canary has the
   expected parent set.

## Follow-up Checks

1. Run `just validate data/habitats/aquatic/deep_subsurface__f51dcfb9.yaml`.
2. Run `just validate-all data/habitats/aquatic/deep_subsurface__f51dcfb9.yaml`.
3. Run `just validate-history`.
4. Run `just term-requests-check`.
5. Run `just verify-corpus --max-diffs 1`.
6. Run `just render`.
7. Run `just qc`.
8. Re-read the regenerated target and confirm that it keeps the GOLD
   attestation, has the curated label and definition, no longer lists
   `ENVO:00001999`, and remains the only file pinned to
   `habitatmech:GOLD.3841c9c3af`.

## Additional Notes

The same exact leaf label appears at three GOLD paths with different scope:
aquatic deep subsurface, aquatic marine deep subsurface, and terrestrial deep
subsurface. The source path, not the leaf label alone, is the identity-bearing
field for this generated record.
