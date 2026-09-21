# YAML Record Review: Bathypelagic/Bathyal zone

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/bathypelagic_bathyal_zone.yaml`
- Started UTC: 2026-09-21T19:10:00Z
- Finished UTC: 2026-09-21T19:12:02Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.ebabcbea1e` |
| Label | `Bathypelagic/Bathyal zone` |
| Class | `HabitatRecord` |
| Category | `AQUATIC` |
| Generated or maintained | Generated from `data/raw/gold_ecosystem_paths.tsv`, `curation/decisions.tsv`, and `data/habitats/PATHS.tsv`; do not hand-edit |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source concepts | GOLD `gold.ecosystem:7899` |
| Locked stem | `bathypelagic_bathyal_zone` in `data/habitats/PATHS.tsv` |

The record covers GOLD
`Environmental > Aquatic > Marine > Pelagic zone > Bathypelagic/Bathyal zone`,
a level-5 Pelagic-zone child that GOLD models separately from its shorter
`Environmental > Aquatic > Marine > Bathypelagic` source concept.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/bathypelagic_bathyal_zone.yaml` | Pass: LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/bathypelagic_bathyal_zone.yaml --quiet` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Pass: 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Pass: committed term-request table is current with 109 terms. |
| `just validate-history` | Pass: 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Pass: 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| Reference validator | Not available: `justfile` exposes no reference-specific validator, and this record has no `EvidenceItem`, `EnvironmentalParameter.reference`, `CharacteristicTaxon.reference`, or causal-edge evidence to target. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| The record denotes the GOLD `Bathypelagic/Bathyal zone` path. | `data/raw/gold_ecosystem_paths.tsv` has the exact canonical path, leaf label `Bathypelagic/Bathyal zone`, depth `5`, one GOLD node ID `gold.ecosystem:7899`, and zero organism, study, biosample, or total assertions. | Supported exactly. |
| The generated source attestation preserves that GOLD identity. | The YAML has one `source: GOLD` attestation with `source_id: gold.ecosystem:7899`, `source_label: Bathypelagic/Bathyal zone`, and the exact source path. | Supported exactly. |
| The `ENVO:00000208` `marine pelagic zone` parent is inherited from the source path. | `data/raw/ontology_terms.tsv` labels `ENVO:00000208` as `marine pelagic zone`; `data/habitats/PATHS.tsv` maps `ENVO:00000208` to `marine_pelagic_zone`; the target's immediate GOLD parent is `Environmental > Aquatic > Marine > Pelagic zone`. | Supported as a true broader water-column parent if the slash leaf is interpreted as a pelagic bathypelagic zone. |
| The class-level `UNGROUNDED` decision is not enough to settle identity. | `curation/decisions.tsv` has a `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.ebabcbea1e`, but its `review_depth` is `CLASS`, and the note explicitly says the sweep did not assess whether the concept is a habitat. | Needs item-level curation. |
| Nearby vendored terms make an item-level decision actionable. | The slice contains `ENVO:00000211` `marine bathypelagic zone` and `ENVO:01000026` `marine bathyal zone biome`; the separate GOLD `Environmental > Aquatic > Marine > Bathypelagic` source is already item-grounded exactly to `ENVO:00000211`. | Needs curation; the target's slash label combines a pelagic water-column zone with a bathyal benthic/slope zone, so it should not be blindly grounded to either neighbor. |

## Evidence

The record has no curator-authored `evidence`, `environmental_parameters`,
`characteristic_taxa`, `causal_graphs`, `discussions`, or `datasets`.

| Claim | Evidence | Assessment |
|---|---|---|
| The missing GOLD `assertion_count` is faithful to the collapsed GOLD path row. | `data/raw/gold_ecosystem_paths.tsv` reports `organism_count=0` and `total_assertions=0` for `gold.ecosystem:7899`; the seeder only emits a GOLD assertion count when the organism count is nonzero. | Supported exactly. |
| Later GOLD-derived tables provide sparse context but no generated field for this record. | `data/raw/gold_path_biosamples.tsv` records 5 biosamples for the exact Bathypelagic/Bathyal path, and `data/raw/gold_studies.tsv` lists the path in 3 studies. Hidden/ignored-inclusive exact source-path searches found no `data/raw/gold_path_triads.tsv` or `data/raw/environment_parameters.tsv` row for this path. | Supported exactly; these rows are context for future item review, not enough evidence to choose an ontology identity. |
| The adjacent depth-band family has the same unresolved modeling pattern. | GOLD also emits `Abyssopelagic/Abyssal zone`, `Mesopelagic/Twilight zone`, and `Hadopelagic zone/Ocean trenches` under `Environmental > Aquatic > Marine > Pelagic zone`; the already reviewed Abyssopelagic/Abyssal record found an analogous need for item-level depth-band review. | Contextual only; each slashed GOLD leaf still needs its own item decision. |

## Completeness

The record is complete enough as a generated class-swept placeholder. It has the
stable HabitatMech identifier, the GOLD source attestation, the true inherited
Pelagic-zone parent, the generated class-sweep event, and the generated seed
event.

It is not complete enough as a defended ungrounded record:

- the only `curation/decisions.tsv` row has `review_depth=CLASS`;
- no `curation/term_requests.tsv` row defines the slashed source concept if it
  remains minted;
- no `curation/causal_graphs/*.yaml` overlay targets Bathypelagic/Bathyal; and
- no target-specific research report or history record exists.

Hidden- and ignored-file-inclusive searches covered `data/raw`, `data/habitats`,
`data/habitats/PATHS.tsv`, `curation`, `history`, `research/habitats`,
`reports/habitat_research_manifest.tsv`, and `reports/yaml_record_review` for
`habitatmech:GOLD.ebabcbea1e`, `gold.ecosystem:7899`,
`Environmental > Aquatic > Marine > Pelagic zone > Bathypelagic/Bathyal zone`,
`Bathypelagic/Bathyal`, and `bathypelagic_bathyal_zone`. They found the raw GOLD
path row, raw biosample and study context, the locked slug, the target YAML, and
the class-level decision row; they found no item-level decision, term request,
causal overlay, research manifest entry, dedicated research report, history
record, or prior exact YAML review for this target.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| `HM-BATHYPELAGIC-BATHYAL-ZONE-001` | Major | `Bathypelagic/Bathyal zone` is still only class-reviewed. The generated record is left as `UNGROUNDED`, but the class sweep only proved that no vendored label/synonym matched the literal slash label; it did not decide whether this GOLD path should merge into `ENVO:00000211` `marine bathypelagic zone`, remain minted because it combines bathypelagic and bathyal contexts, or use another reviewed relationship to `ENVO:01000026` `marine bathyal zone biome`. | `curation/decisions.tsv` row `habitatmech:GOLD.ebabcbea1e` has `review_depth=CLASS`; `data/raw/ontology_terms.tsv` vendors `ENVO:00000211` and `ENVO:01000026`; `curation/decisions.tsv` already item-grounds the separate GOLD `Bathypelagic` path to `ENVO:00000211`; the target remains `mapping_status: SEEDED`. | `curation/decisions.tsv`, with a possible follow-on `curation/term_requests.tsv` row if item review keeps the source minted. |

No blocker or minor findings found.

## Recommended Edits

1. Replace the class-depth `CONFIRM_UNGROUNDED` row for
   `habitatmech:GOLD.ebabcbea1e` in `curation/decisions.tsv` with an item-depth
   decision after inspecting the three GOLD study contexts for
   `gold.ecosystem:7899` and comparing the slash label against
   `ENVO:00000211` and `ENVO:01000026`.
2. If the GOLD source is the same water-column concept as
   `Environmental > Aquatic > Marine > Bathypelagic`, ground it to
   `ENVO:00000211` so both GOLD source concepts merge. If the slash label is a
   genuine mixed or broader GOLD bucket, keep it minted and add a
   `curation/term_requests.tsv` definition with an explicitly checked broader
   parent.
3. Regenerate with `just seed`, then run the appropriate canary. Use
   `just seed-canary ENVO:00000211 --force` if the record merges into the
   existing ENVO term; otherwise use
   `just seed-canary habitatmech:GOLD.ebabcbea1e --force`.

## Follow-up Checks

- `just seed`
- `just seed-canary <resolved-identifier> --force`
- `just validate <resolved-record-path>`
- `just validate-strict <resolved-record-path> --quiet`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `git diff --check`

After regeneration, re-read the resolved record and confirm the
`grounding_status`, `mapping_status`, source attestation, parent list, and
curation-history events all follow from the maintained item-level decision.

## Additional Notes

This was a read-only YAML review. It did not edit generated habitat YAML, append
curation history, promote the review status, create an issue, or run paid
definition research.

The earlier `Abyssopelagic/Abyssal zone` review is relevant context for the
GOLD depth-band family, but it is not a maintained input for this target.
