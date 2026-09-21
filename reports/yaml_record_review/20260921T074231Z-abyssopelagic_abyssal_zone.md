# YAML Record Review: Abyssopelagic/Abyssal zone

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/abyssopelagic_abyssal_zone.yaml
- Started UTC: 2026-09-21T07:42:31Z
- Finished UTC: 2026-09-21T07:42:41Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/aquatic/abyssopelagic_abyssal_zone.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.3a1e1f8fd7` |
| Label | `Abyssopelagic/Abyssal zone` |
| Category | `AQUATIC` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Maintained status | generated from `data/raw/`, `curation/decisions.tsv`, and `data/habitats/PATHS.tsv` |

The generated record is a compact GOLD-only placeholder:

- GOLD supplies one `Environmental > Aquatic > Marine > Pelagic zone >
  Abyssopelagic/Abyssal zone` source attestation with 1 `ORGANISM` assertion.
- The parent `ENVO:00000208` `marine pelagic zone` comes from the preceding
  GOLD `Pelagic zone` path step.
- GOLD's MIxS triad inventory separately reports 27 biosamples on this path,
  but only 1 biosample with a triad: broad `ENVO:00000447` `marine biome`,
  local `ENVO:00000209` `marine photic zone`, and medium `ENVO:00002149`
  `sea water`.
- The raw GOLD study inventory lists this path in two studies: once alone and
  once beside all four other `Pelagic zone` depth-band siblings.
- A class-level curation decision rejected automatic lexical grounding but did
  not assess the source concept as an individual habitat.
- No definition, authored term request, item-level grounding decision, taxa,
  environmental parameters, evidence, causal graphs, discussions, datasets,
  synonyms, or xrefs are present.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/abyssopelagic_abyssal_zone.yaml` | Passed; no LinkML issues. |
| `just validate-strict data/habitats/aquatic/abyssopelagic_abyssal_zone.yaml --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just term-requests-check` | Passed; term-request table is current at 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records, 3,206 found, no missing/extra/differing records. |
| `just validate-history` | Passed; 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| Reference validator | Not checked: this record has no DOI/PMID/URL `EvidenceItem` or causal-edge evidence, and no dedicated `research/habitats/aquatic/` report for `habitatmech:GOLD.3a1e1f8fd7` requiring `scripts/check_report_citations.py` exists. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| The record denotes the GOLD `Environmental > Aquatic > Marine > Pelagic zone > Abyssopelagic/Abyssal zone` source concept. | `data/raw/gold_ecosystem_paths.tsv` has exactly that canonical path, leaf `Abyssopelagic/Abyssal zone`, depth `5`, `gold_node_count=1`, `organism_count=1`, `total_assertions=1`, and node ID `gold.ecosystem:7900`. | Supported exactly. |
| The stable file stem is `abyssopelagic_abyssal_zone`. | `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.3a1e1f8fd7` to `abyssopelagic_abyssal_zone`. | Supported exactly. |
| The source path justifies the broad AQUATIC category. | The raw GOLD path is under `Environmental > Aquatic > Marine > Pelagic zone`. Its one triad sample also uses `marine biome` as broad scale and `sea water` as medium. | Supported exactly. |
| The inherited `ENVO:00000208` `marine pelagic zone` parent is strictly broader. | `ENVO:00000208` is the `Pelagic zone` path parent and denotes an open-ocean region. The GOLD child is one depth band under that pelagic-zone node. | Supported exactly. |
| Existing ontology terms are plausible grounding targets. | `data/raw/ontology_terms.tsv` contains `ENVO:01000038` `oceanic abyssopelagic zone biome` and `ENVO:00000212` `marine abyssalpelagic zone`. A separate GOLD source concept, `Environmental > Aquatic > Marine > Abyssopelagic`, is already item-grounded to `ENVO:01000038`. | Needs item-level curation; the slashed GOLD leaf and duplicate-looking GOLD path need curator comparison before choosing identity or SAME_AS handling. |
| The single MIxS triad row is not enough to settle identity. | The path has 27 GOLD biosamples but only 1 biosample with a triad, and that triad places the sample in `marine photic zone` as local scale despite the GOLD abyssopelagic label. | Supported exactly; treat the triad as context only. |
| `grounding_status: UNGROUNDED` is generated from a class-level no-match sweep. | `curation/decisions.tsv` has `habitatmech:GOLD.3a1e1f8fd7` as `CONFIRM_UNGROUNDED` with `review_depth=CLASS` and no object ID. Its note says no vendored-slice term matched the label by any search route and explicitly says whether the concept is a habitat was not assessed. | Mechanically supported but incomplete for item-level curation. |
| `mapping_status: SEEDED` is correct. | The only curation row for `habitatmech:GOLD.3a1e1f8fd7` has `review_depth=CLASS`; `docs/CURATION.md` states that only item-level decisions promote a merged record to `REVIEWED`. | Supported exactly. |

## Evidence

No claim-level literature evidence was present. The record has no
characteristic taxon rows and no causal graph, so there are no taxon
associations, causal edges, or snippets to audit.

The raw GOLD path, two study rows, one-biosample triad, and the nearby
item-reviewed `Environmental > Aquatic > Marine > Abyssopelagic` source concept
are source-context rows, not literature evidence. They make the current
class-level curation too weak, but they do not independently decide whether the
source should merge into the existing `ENVO:01000038` record, ground to another
abyssopelagic-zone term, or remain minted.

## Completeness

- The record is schema-valid and reproducible, but not item-curated.
- Empty `characteristic_taxa`, `evidence`, `environmental_parameters`,
  `causal_graphs`, `discussions`, `datasets`, `synonyms`, and `xrefs` are
  technically acceptable: no maintained input currently supplies them for this
  record.
- `data/raw/environment_parameters.tsv` has no row for
  `Environmental > Aquatic > Marine > Pelagic zone > Abyssopelagic/Abyssal
  zone`.
- `curation/term_requests.tsv`,
  `curation/term_requests/envo_robot_template.tsv`, and
  `reports/habitat_research_manifest.tsv` have no row for
  `habitatmech:GOLD.3a1e1f8fd7`.
- Ignored/hidden-inclusive exact searches covered `data/raw`,
  `data/habitats/aquatic`, `data/habitats/PATHS.tsv`, `curation`,
  `research/habitats`, `reports/habitat_research_manifest.tsv`, and
  `reports/yaml_record_review` for `habitatmech:GOLD.3a1e1f8fd7`,
  `gold.ecosystem:7900`, `Environmental > Aquatic > Marine > Pelagic zone >
  Abyssopelagic/Abyssal zone`, `Abyssopelagic/Abyssal zone`, and
  `abyssopelagic_abyssal_zone`. They found the target, the raw GOLD path, raw
  GOLD biosamples and triads, two raw GOLD study rows, the stable path entry,
  and the class-level decision row; they found no item-level decision,
  term-request row, causal overlay, research manifest entry, dedicated research
  report, or prior exact YAML review report for this target.
- A bounded `find curation/causal_graphs -maxdepth 1` search for `*abyss*`,
  `*pelagic*`, `*7900*`, and `*3a1e1f8fd7*` found no candidate causal overlay.
- A bounded `find research/habitats` search for `*abyss*`, `*pelagic*`,
  `*7900*`, and `*3a1e1f8fd7*` found no candidate dedicated research report.
- A bounded `find reports/yaml_record_review -maxdepth 1` search for `*abyss*`,
  `*pelagic*`, `*7900*`, and `*3a1e1f8fd7*` found only the adjacent
  `Abyssal plane` review report, not a report for
  `data/habitats/aquatic/abyssopelagic_abyssal_zone.yaml`.

## Findings

### Major

| ID | Finding | Evidence | Maintained owner |
|---|---|---|---|
| `HM-ABYSSOPELAGIC-ABYSSAL-ZONE-001` | The source concept still needs item-level curation. The generated record treats GOLD `Abyssopelagic/Abyssal zone` as an ungrounded child of `marine pelagic zone`, but its only curation row is a `CLASS`-depth lexical no-match sweep that did not assess the full pelagic-depth path, the already reviewed GOLD `Abyssopelagic` sibling, `ENVO:01000038` `oceanic abyssopelagic zone biome`, or `ENVO:00000212` `marine abyssalpelagic zone`. | `curation/decisions.tsv` row `habitatmech:GOLD.3a1e1f8fd7` has `review_depth=CLASS`; `data/raw/ontology_terms.tsv` contains both candidate ENVO terms; `curation/decisions.tsv` separately grounds `habitatmech:GOLD.1edff6a744`, GOLD `Environmental > Aquatic > Marine > Abyssopelagic`, to `ENVO:01000038` at `review_depth=ITEM`. | `curation/decisions.tsv` |

## Recommended Edits

1. Item-review `habitatmech:GOLD.3a1e1f8fd7` in
   `curation/decisions.tsv`. Resolve whether GOLD's longer
   `Pelagic zone > Abyssopelagic/Abyssal zone` path is the same habitat as the
   already reviewed `Environmental > Aquatic > Marine > Abyssopelagic` source,
   another abyssopelagic water-column term such as `ENVO:00000212`, a mixed
   abyssopelagic/abyssal source artifact, or a real minted habitat with no exact
   ontology term.
2. If the path is another assertion of the existing GOLD `Abyssopelagic`
   identity, replace the existing class-depth `CONFIRM_UNGROUNDED` row for
   `habitatmech:GOLD.3a1e1f8fd7` with an item-depth `GROUND` decision to
   `ENVO:01000038`. Do not use `SAME_AS` for this already grounded sibling: two
   GOLD sources with the same ontology identity merge because they both resolve
   to `ENVO:01000038`.
3. Regenerate a single-record canary for the resolved identifier that follows
   from the item decision. If the source grounds to `ENVO:01000038`, inspect
   `data/habitats/aquatic/oceanic_abyssopelagic_zone_biome.yaml`; if it remains
   minted, inspect `data/habitats/aquatic/abyssopelagic_abyssal_zone.yaml`.
   Confirm that the generated `grounding_status`, `mapping_status`, label,
   parent, source attestation, and curation history all follow from the
   maintained rows.

## Follow-up Checks

- `just seed`
- `just seed-canary <resolved-identifier>`
- `just validate <resolved-record-path>`
- `just validate-strict <resolved-record-path> --quiet`
- `just term-requests-check`
- `just verify-corpus --max-diffs 1`

## Additional Notes

- The GOLD `Pelagic zone > ...` depth-band family appears to need a group
  review. `Epipelagic/Euphotic zone`, `Bathypelagic/Bathyal zone`,
  `Mesopelagic/Twilight zone`, and `Hadopelagic zone/Ocean trenches` are also
  generated as minted, class-level ungrounded children of `ENVO:00000208`.
- The single GOLD study that co-lists all five depth-band siblings reinforces
  the water-column reading of this path, but the sole MIxS triad sample for the
  target has `marine photic zone` as local scale. Item review should inspect the
  two raw GOLD study contexts before deciding whether to ground, merge, or keep
  this source concept minted.
