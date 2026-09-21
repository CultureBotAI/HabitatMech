# YAML Record Review: Acid-saline drainage

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/acid_saline_drainage.yaml
- Started UTC: 2026-09-21T08:48:15Z
- Finished UTC: 2026-09-21T08:49:29Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/aquatic/acid_saline_drainage.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.4d8430a3ad` |
| Label | `Acid-saline drainage` |
| Category | `AQUATIC` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Maintained/generated status | Generated from `data/raw/` inventories and curator inputs; `just verify-corpus --max-diffs 1` reproduces it byte-for-byte. |

The generated record is a zero-assertion GOLD placeholder:

- GOLD supplies one `Environmental > Aquatic > Deep subsurface > Groundwater >
  Acid-saline drainage` source attestation with source ID
  `gold.ecosystem:8046`.
- The stable filename comes from the lockfile row for
  `habitatmech:GOLD.4d8430a3ad` in `data/habitats/PATHS.tsv`.
- The only curation decision for this source concept is the August 12
  `CLASS`-depth lexical no-match sweep.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/acid_saline_drainage.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/acid_saline_drainage.yaml --quiet` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records, 3,206 records on disk, 0 missing, 0 extra, 0 differing. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| Reference validator | Not checked: this record has no DOI/PMID/URL `EvidenceItem`, no causal-edge evidence, and no dedicated `research/habitats/` report for `habitatmech:GOLD.4d8430a3ad`. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| The record denotes the GOLD `Environmental > Aquatic > Deep subsurface > Groundwater > Acid-saline drainage` source concept. | `data/raw/gold_ecosystem_paths.tsv` has exactly that canonical path, leaf `Acid-saline drainage`, depth `5`, `gold_node_count=1`, `organism_count=0`, `total_assertions=0`, and node ID `gold.ecosystem:8046`. | Supported exactly. |
| The stable file stem is `acid_saline_drainage`. | `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.4d8430a3ad` to `acid_saline_drainage`. | Supported exactly. |
| The `habitatmech:GOLD.22a80cbd14` `Groundwater` parent follows from the GOLD path. | The raw path sits immediately under `Environmental > Aquatic > Deep subsurface > Groundwater`, and `data/habitats/PATHS.tsv` maps that parent source concept to `groundwater`. | Supported as a source-path parent. |
| `grounding_status: UNGROUNDED` follows from curator input. | `curation/decisions.tsv` has a `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.4d8430a3ad`. | Mechanically supported but incomplete for item-level curation because `review_depth=CLASS`. |
| `mapping_status: SEEDED` is correct. | The only decision row for `habitatmech:GOLD.4d8430a3ad` has `review_depth=CLASS`; `docs/CURATION.md` states that class-level decisions do not promote records to `REVIEWED`. | Supported exactly. |

## Evidence

The generated record has no record-level `evidence` entries and no
`causal_graphs`.

| Claim | Evidence | Assessment |
|---|---|---|
| GOLD is the only upstream attestation feeding this record. | Ignored/hidden-inclusive exact searches for `habitatmech:GOLD.4d8430a3ad`, `gold.ecosystem:8046`, `Acid-saline drainage`, and `acid_saline_drainage` found one generated record, one `PATHS.tsv` row, one `curation/decisions.tsv` row, and one `data/raw/gold_ecosystem_paths.tsv` row. No BacDive, PREGO, Madin, term-request, or causal-graph curation rows matched those exact keys. | Supported exactly. |
| The zero assertion count is not hiding committed GOLD biosamples or studies. | The exact canonical path is absent from `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, and `data/raw/gold_studies.tsv`; the only exact path row in `data/raw/` is the zero-assertion `data/raw/gold_ecosystem_paths.tsv` row. | Supported exactly. |
| No vendored ontology term directly names this label. | An ignored/hidden-inclusive search for acid-saline label variants in `data/raw/ontology_terms.tsv`, `curation/term_requests.tsv`, and `curation/term_requests_excluded.tsv` found no exact maintained term, request, or exclusion row. | Supported as a bounded label search, not a full ontology-review substitute. |

## Completeness

- The record is complete enough as a seeded GOLD placeholder, but not as a
  reviewed curation artifact.
- The class-level sweep only proves that no vendored ENVO, UBERON, FOODON, or
  BTO label matched the source label by the configured lexical routes. It does
  not prove that acid-saline drainage is a habitat, that it lacks an exact
  ontology term, or that a HabitatMech term should be requested.
- Ignored/hidden-inclusive exact searches covered `data/habitats`, `data/raw`,
  `curation`, `research/habitats`, `reports/habitat_research_manifest.tsv`, and
  `reports/yaml_record_review` for `habitatmech:GOLD.4d8430a3ad`,
  `gold.ecosystem:8046`, `Acid-saline drainage`, and
  `acid_saline_drainage`. These found the target record, its `PATHS.tsv` row,
  the GOLD ecosystem path row, and the class-level decision row; they found no
  item-level decision, term request, dedicated research report, or prior YAML
  review report.
- Ignored/hidden-inclusive exact searches for the canonical GOLD path in
  `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, and
  `data/raw/gold_studies.tsv` found no biosample, MIxS triad, or study rows.
- Bounded `find` checks for `*acid*` and `*saline*` under
  `curation/causal_graphs`, `research/habitats`, and
  `reports/yaml_record_review` found no target-specific causal overlay or
  research report.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| `HM-ACID-SALINE-DRAINAGE-001` | Major | The source concept still needs item-level curation. The generated record publishes a real minted habitat identity under deep-subsurface groundwater, but the only curator input is a `CLASS`-depth no-match sweep that explicitly did not assess whether the concept is a habitat. The source is also a zero-assertion GOLD leaf, so no committed biosample, triad, study, taxon, or environmental-parameter row independently explains GOLD's intended meaning. | `curation/decisions.tsv` row `habitatmech:GOLD.4d8430a3ad` has `review_depth=CLASS` and says, "Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate." `data/raw/gold_ecosystem_paths.tsv` has `organism_count=0` and `total_assertions=0` for `gold.ecosystem:8046`, and exact ignored/hidden-inclusive searches found no committed biosample, triad, study, or research evidence for this path. | `curation/decisions.tsv`, with a possible follow-on `curation/term_requests.tsv` row if item review confirms acid-saline drainage is a real habitat lacking an ontology term. |

No blocker or minor findings found.

## Recommended Edits

1. Item-review `habitatmech:GOLD.4d8430a3ad` in
   `curation/decisions.tsv`. Resolve whether this zero-assertion GOLD leaf
   denotes a sampled deep-subsurface acidic saline drainage habitat, a synonym
   or near-synonym of a different GOLD drainage concept, or an unused
   placeholder that should be excluded from HabitatMech term requests.
2. If the concept is a real habitat with no fitting ontology identity, keep it
   `CONFIRM_UNGROUNDED` at `review_depth=ITEM` and consider adding a precise
   definition to `curation/term_requests.tsv`.
3. If it is the same source meaning as an existing drainage, acid-mine-drainage,
   or mine-water record, use a `SAME_AS` or exact `GROUND` decision as
   appropriate rather than preserving a duplicate minted identity.
4. If the source leaf is not a habitat, replace the class-level row with an
   item-level `NOT_APPLICABLE` or add a term-request exclusion, then regenerate
   the record or remove the term-request candidate by the existing pipeline.

## Follow-up Checks

| Edit | Narrowest proving check |
|---|---|
| Add an item-level decision for `habitatmech:GOLD.4d8430a3ad`. | Re-read the edited `curation/decisions.tsv` row, run `just seed`, and confirm the dry-run resolution for the source concept. |
| Add a term request if a novel habitat definition is warranted. | `just term-requests-check`, followed by inspection of `curation/term_requests/envo_robot_template.tsv` to confirm the requested label, definition, parent, and page URL. |
| Regenerate a canary for the target. | `just seed-canary habitatmech:GOLD.4d8430a3ad`, or the replacement identifier if the item-level decision merges the source elsewhere, then inspect the generated YAML. |
| Validate the regenerated corpus. | `just validate <generated-record>`, `just validate-strict <generated-record> --quiet`, `just verify-corpus --max-diffs 1`, and `just validate-history`. |

## Additional Notes

- `research/habitats/aquatic/non-marine-saline-and-alkaline-habitatmech-gold-ce244e62cd-deep-research-claude_code.md`
  discusses GOLD's inland saline-or-alkaline grouping, not this deep-subsurface
  zero-assertion Acid-saline drainage leaf.
- The exact acid-saline label search found incidental mentions of acid and
  saline physiology in unrelated oil/gas-pipeline and free-living-environment
  reports; those are not evidence for this source concept.
