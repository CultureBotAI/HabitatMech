# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/hadopelagic_zone_ocean_trenches.yaml
- Started UTC: 2026-09-26T09:50:55Z
- Finished UTC: 2026-09-26T09:51:09Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.1f80141d6a` |
| Label | `Hadopelagic zone/Ocean trenches` |
| Class | `HabitatRecord` |
| Category | `AQUATIC` |
| Generated path | `data/habitats/aquatic/hadopelagic_zone_ocean_trenches.yaml` |
| Maintained path lock | `data/habitats/PATHS.tsv:1516` maps `habitatmech:GOLD.1f80141d6a` to `hadopelagic_zone_ocean_trenches` |
| Source concept | GOLD `gold.ecosystem:7901` |
| Source path | `Environmental > Aquatic > Marine > Pelagic zone > Hadopelagic zone/Ocean trenches` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |

The reviewed file is generated from the GOLD source inventory and a
class-level curation decision. It should not be patched directly.

## Validation

| Command | Result |
|---|---|
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist.tsv` | Passed; wrote 953 rows and placed `habitatmech:GOLD.1f80141d6a` immediately after the already reviewed `Ear discharge`. |
| `just validate data/habitats/aquatic/hadopelagic_zone_ocean_trenches.yaml` | Passed with `No issues found`. |
| `just validate-strict data/habitats/aquatic/hadopelagic_zone_ocean_trenches.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 expected records, 3206 found, 0 missing, 0 extra, 0 differing. |
| `just report` | Passed; no stale class-level sweep, contradictory path term, or non-habitat label contradiction was reported for this record. |
| `git diff --check` | Passed before this report was written. |

## Identity and Grounding

The generated identifier, label, category, source attestation, and assertion
count agree with the GOLD source inventory:

| Claim | Evidence | Assessment |
|---|---|---|
| The target is the GOLD `Hadopelagic zone/Ocean trenches` path. | `data/raw/gold_ecosystem_paths.tsv:671` records `Environmental > Aquatic > Marine > Pelagic zone > Hadopelagic zone/Ocean trenches` with leaf label `Hadopelagic zone/Ocean trenches`, depth 5, one GOLD node, four organism assertions, and source ID `gold.ecosystem:7901`. | Supported exactly. |
| The generated `source_attestations` block preserves the raw source ID, path, count, and unit. | The generated YAML carries `source: GOLD`, `source_id: gold.ecosystem:7901`, the same full source path, `assertion_count: 4`, and `assertion_unit: ORGANISM`. | Supported exactly. |
| The generated parent `ENVO:00000208` is inherited from the immediate GOLD `Pelagic zone` path parent. | `data/raw/gold_ecosystem_paths.tsv:14` records `Environmental > Aquatic > Marine > Pelagic zone` and `gold.ecosystem:3771|gold.ecosystem:4021`; the generated parent record `data/habitats/aquatic/marine_pelagic_zone.yaml` grounds that GOLD parent to `ENVO:00000208` `marine pelagic zone`. | Supported as a strict broader parent if this source concept is interpreted as the water column in ocean trenches. |
| The path's exact GOLD label is not a clean ontology label. | A hidden/ignored-inclusive search for `Hadopelagic zone/Ocean trenches` found the exact text only in the GOLD target rows, generated HabitatMech artifacts, and adjacent review reports. The vendored slice instead has `ENVO:00000214` `hadalpelagic zone`, `ENVO:01000039` `oceanic hadal pelagic zone biome`, and `ENVO:00000275` `ocean trench`. | Supported. The one-character `Hadopelagic`/`hadalpelagic` difference and the `/Ocean trenches` suffix evade the lexical class sweep, but exact hadal-pelagic near matches do exist in the slice. |
| `UNGROUNDED` is currently explained only by a class-level no-match sweep. | `curation/decisions.tsv:275` has `CONFIRM_UNGROUNDED` with `review_depth` `CLASS`; the generated curation history repeats that no ontology term fit by any lexical route and that habitat status was not assessed. | Reproducible but incomplete. `CLASS` depth does not establish that the leaf denotes a habitat, that no exact term fits, or whether an exact hadal-pelagic term should be used. |

A bounded hidden/ignored-inclusive search of `data/raw/`, `curation/`,
`history/`, `research/`, `reports/yaml_record_review/`, `data/habitats/`, and
`pages/habitats/` for `habitatmech:GOLD.1f80141d6a`,
`gold.ecosystem:7901`, `hadopelagic_zone_ocean_trenches`,
`Hadopelagic zone/Ocean trenches`, and the exact source path found the expected
generated record, page, path lock, raw GOLD aggregate and biosample rows, and
class-level decision row. It found no target-specific term request, generated
term-request row, causal overlay, append-only history entry, deep-research
report, or prior exact YAML review for this target. The same exhaustive search
also found the exact target label in the Abyssopelagic/Abyssal and
Bathypelagic/Bathyal review reports, where it was noted as part of the same
unresolved slashed GOLD pelagic-depth family; those reports are context, not
item-level review of this record.

## Evidence

| Record claim | Nearest source | Assessment |
|---|---|---|
| `source: GOLD`, `source_id: gold.ecosystem:7901`, `source_label: Hadopelagic zone/Ocean trenches`, and the full source path | `data/raw/gold_ecosystem_paths.tsv:671` | Supported exactly. |
| `assertion_count: 4`, `assertion_unit: ORGANISM` | `data/raw/gold_ecosystem_paths.tsv:671` has `organism_count=4`, `study_count=0`, `biosample_count=0`, and `total_assertions=4`. | Supported; the count is a GOLD `ORGANISM` aggregate and is not study or biosample evidence. |
| Parent `ENVO:00000208` | GOLD places the source concept under `Environmental > Aquatic > Marine > Pelagic zone`; the generated parent record for that path is `ENVO:00000208` `marine pelagic zone`, whose definition is "An open ocean region." | Supported if the slash leaf is treated as the hadal water-column zone. Not established by item review because `Ocean trenches` can also name `ENVO:00000275`, a seafloor topographic depression rather than a pelagic layer. |
| Absence of MIxS triad parameters | An exact hidden/ignored-inclusive search of `data/raw/gold_path_triads.tsv` found no row for the target source path. | Supported. The exact target has GOLD aggregate and biosample rows, but no triad row that could independently distinguish `hadalpelagic zone`, `ocean trench`, or a broader hadal biome as the identity. |
| Absence of characteristic taxa, record evidence, and causal graphs | Exact hidden/ignored-inclusive searches across `data/raw/`, `curation/causal_graphs/`, and the generated YAML found no target-specific taxa or curated overlay, and GOLD path aggregates do not emit inline characteristic-taxon claims. | Supported. |

The vendored ontology slice contains three nearby concepts that need item-level
evaluation against `gold.ecosystem:7901`:

| CURIE | Label | Relationship to the GOLD leaf |
|---|---|---|
| `ENVO:00000214` | `hadalpelagic zone` | Most label-like match for the water-column reading; it is defined as the zone of an ocean in oceanic trenches between 6000 m and 10,000 m and is a subclass of `ENVO:00000210` `marine aphotic zone`. |
| `ENVO:01000039` | `oceanic hadal pelagic zone biome` | Hadal water-column biome; it is a subclass of `ENVO:01000033` `oceanic pelagic zone biome`. |
| `ENVO:00000275` | `ocean trench` | Exact match for the `Ocean trenches` half of the GOLD label, but a trench is a seafloor landform. It should not be made the identity of a pelagic water-column record. |

GOLD also has distinct paths for the adjacent pelagic depth bands:
`Epipelagic/Euphotic zone`, `Mesopelagic/Twilight zone`,
`Bathypelagic/Bathyal zone`, and `Abyssopelagic/Abyssal zone`. `Gs0161492`
co-lists all five of those slashed leaves in `data/raw/gold_studies.tsv`, and
`data/raw/gold_path_biosamples.tsv` reports one blank-node group with 37
biosamples plus one `7901` row with two biosamples for the target path. Those
side rows support that GOLD is using this as part of a water-column depth-band
family, but they do not prove whether the HabitatMech identity should be
`ENVO:00000214`, `ENVO:01000039`, or a minted concept that has `ENVO:00000214`
as a parent.

## Completeness

The generated record preserves the existing raw GOLD aggregate row and
class-level curation decision and correctly avoids unsupported characteristic
taxa, environmental parameters, evidence items, and causal graph claims.

It is incomplete as an item-reviewed habitat. The exact source path has no MIxS
triad row and no committed research report. Its class-level decision only says
the literal leaf label did not match a vendored term by the sweep's lexical
routes; that decision predates item-level inspection of the GOLD node and the
nearby hadal-pelagic ENVO terms. A future curator needs to inspect GOLD
`gold.ecosystem:7901` and the organism assertions behind it, then decide
whether the slash leaf denotes the hadal pelagic zone, the oceanic hadal
pelagic biome, a hadal-pelagic child that only inherits those terms as parents,
or an upstream conflation with the ocean-trench landform.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-HADOPELAGIC-001 | Major | `Hadopelagic zone/Ocean trenches` is still backed only by `review_depth` `CLASS`. The generated `UNGROUNDED` and `SEEDED` statuses are reproducible, but the maintained row explicitly says no one assessed whether the source concept is a habitat, and the vendored slice has close hadal-pelagic candidates that did not match the misspelled/slashed GOLD label. | `curation/decisions.tsv`; possibly `curation/term_requests.tsv` if item review keeps a minted child |
| HM-HADOPELAGIC-002 | Major | The source label conflates a pelagic water-column term with `Ocean trenches`, which can mean the `ENVO:00000275` seafloor landform. The inherited `ENVO:00000208` parent is correct for the water-column reading but would be a false `is_a` parent for the trench-landform reading. An item-level decision must resolve the identity before exact grounding or novel-term definition. | `curation/decisions.tsv`; possibly `curation/term_requests.tsv` |

## Recommended Edits

1. Item-review `habitatmech:GOLD.1f80141d6a` in
   `curation/decisions.tsv`, replacing the class-level row with an item-level
   decision.
2. Inspect GOLD node `gold.ecosystem:7901`, including the four organism
   assertions behind the aggregate row and the 39 biosample contexts visible in
   `data/raw/gold_path_biosamples.tsv`, to confirm whether GOLD is using the
   leaf as a water-column hadal pelagic zone, a trench landform, or a composite
   bucket.
3. Compare the confirmed GOLD meaning against `ENVO:00000214`
   `hadalpelagic zone`, `ENVO:01000039` `oceanic hadal pelagic zone biome`,
   and `ENVO:00000275` `ocean trench`.
4. If `gold.ecosystem:7901` exactly denotes the ocean zone, ground it to the
   exact ENVO term with an item-level `GROUND` row.
5. If GOLD needs to remain minted because its source concept is narrower than
   the available ENVO term or intentionally combines the zone with trenches,
   retain `CONFIRM_UNGROUNDED` at item depth and add a
   `curation/term_requests.tsv` definition whose genus parent is the inspected
   broader hadal-pelagic term. Keep `ENVO:00000208` only if it remains a true
   broader water-column parent.
6. If the source concept is actually the trench landform, remove the inherited
   marine-pelagic parent by defining the minted term with an inspected
   non-pelagic genus and `parent_mode=REPLACE`, or ground it to
   `ENVO:00000275` if it is exact.

Do not hand-edit
`data/habitats/aquatic/hadopelagic_zone_ocean_trenches.yaml`; regenerate it
from maintained TSVs after curation changes.

## Follow-up Checks

After adding item-level curation, rerun:

- `just seed`
- `just seed-canary habitatmech:GOLD.1f80141d6a`
- inspect `data/habitats/aquatic/hadopelagic_zone_ocean_trenches.yaml`
- `just validate-strict data/habitats/aquatic/hadopelagic_zone_ocean_trenches.yaml`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`

If a causal overlay is added later, also run
`just validate-causal curation/causal_graphs/hadopelagic_zone_ocean_trenches.yaml`
and `just validate-causal-all`.

## Additional Notes

None.
