# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/terrestrial/agricultural_land__529ac6cb.yaml`
- Started UTC: 2026-09-24T06:15:20Z
- Finished UTC: 2026-09-24T06:18:16Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/terrestrial/agricultural_land__529ac6cb.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.854d6d1a1c` |
| Label | `Agricultural land` |
| Category | `TERRESTRIAL` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| GOLD source-concept key | `habitatmech:GOLD.854d6d1a1c` |
| GOLD parent source-concept key | `habitatmech:GOLD.7ea9c48727` |
| Maintained owners | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/raw/ontology_terms.tsv`, `data/raw/ontology_subclass_edges.tsv`, `data/habitats/PATHS.tsv`, and `src/habitatmech/seed.py`; `data/habitats/` is generated and remains read-only |

This generated GOLD-only record represents `gold.ecosystem:5768`:

```text
Environmental > Terrestrial > Soil > Arable > Agricultural land
```

The source concept is one of the collision-pinned GOLD `Agricultural land`
leaves. This review covers only the `Arable`-scoped source concept with stable
minted identifier `habitatmech:GOLD.854d6d1a1c`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/terrestrial/agricultural_land__529ac6cb.yaml` | Passed: LinkML reported no issues |
| `just validate-strict data/habitats/terrestrial/agricultural_land__529ac6cb.yaml` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| `just validate-causal <overlay>` | Not applicable: the record has no `causal_graphs` slot, and ignored/hidden-inclusive searches of `curation/causal_graphs/` found no overlay for `habitatmech:GOLD.854d6d1a1c`, `gold.ecosystem:5768`, or `agricultural_land__529ac6cb` |
| `just validate-causal-all` | Passed: 32 causal-graph curation files with 32 graphs |
| `just term-requests-check` | Passed: term-request table is current with 109 terms |
| `just validate-history` | Passed: no issues found; 77 history records valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Passed: expected 3,206 records, found 3,206, 0 missing, 0 extra, 0 differing |
| `just worklist --limit 2000` | Passed: 0 ungrounded records still undecided, 1,810 decisions on file |
| `just report` | Passed: corpus report completed for 3,206 records |
| Reference validator | Not applicable: this record has no DOI, PMID, URL, `EvidenceItem`, or causal-edge evidence that would need citation checking |
| `git diff --check` | Passed before this report was written |

## Identity and Grounding

| Claim | Maintained evidence | Assessment |
|---|---|---|
| The output identifier is `habitatmech:GOLD.854d6d1a1c`. | `data/habitats/PATHS.tsv` pins that identifier to `agricultural_land__529ac6cb`. | Supported. |
| The GOLD source ID is `gold.ecosystem:5768`. | `data/raw/gold_ecosystem_paths.tsv` has one row for `Environmental > Terrestrial > Soil > Arable > Agricultural land` with one GOLD node ID, depth 5, `organism_count` 1, `study_count` 0, `biosample_count` 0, and `total_assertions` 1. | Supported. |
| The source belongs in the terrestrial category. | `src/habitatmech/seed.py` infers the category from GOLD's `Environmental > Terrestrial` prefix for this raw row. | Supported. |
| `ENVO:00000077` `agricultural ecosystem` is a broader habitat for this source concept. | The reused GOLD leaf `Agricultural land` matches a synonym on the vendored `ENVO:00000077` row; the seeder keeps the exact ontology term as a parent because other GOLD paths reuse the same leaf. | Supported. |
| `ENVO:01001184` `arable` is a broader habitat for this source concept. | `src/habitatmech/seed.py` links each GOLD concept to the resolved concept of its parent path; the parent path `Environmental > Terrestrial > Soil > Arable` currently resolves to `ENVO:01001184`. | Not supported: the vendored ontology labels `ENVO:01001184` as `arable`, defines it as a quality, and subclasses it to `ENVO:01000203` `environmental condition`. It is not a broader habitat. |
| The source attestation has `assertion_count: 1` and `assertion_unit: ORGANISM`. | The same `data/raw/gold_ecosystem_paths.tsv` row records `organism_count` 1 for `gold.ecosystem:5768`. | Supported. |
| `mapping_status` is `SEEDED`. | Ignored/hidden-inclusive exact searches found no item-level `curation/decisions.tsv` decision for `habitatmech:GOLD.854d6d1a1c`, `gold.ecosystem:5768`, `Environmental > Terrestrial > Soil > Arable > Agricultural land`, or `agricultural_land__529ac6cb`. | Supported. |

The generated minted child identity is internally consistent, but one generated
hierarchy edge is too strong. The source path places `Agricultural land` under
GOLD's `Arable` bin, yet `parent_habitats` is an is-a assertion and
`ENVO:01001184` is a quality rather than a habitat superclass.

## Evidence

The source attestation is an accurate transcription of the committed GOLD row:

- `source: GOLD`
- `source_id: gold.ecosystem:5768`
- `source_label: Agricultural land`
- `source_path: Environmental > Terrestrial > Soil > Arable > Agricultural land`
- `mapping_predicate: skos:narrowMatch`
- `assertion_count: 1`
- `assertion_unit: ORGANISM`

Ignored/hidden-inclusive exact searches found no row for
`Environmental > Terrestrial > Soil > Arable > Agricultural land`,
`gold.ecosystem:5768`, or `habitatmech:GOLD.854d6d1a1c` in these GOLD evidence
tables:

| Source | Search result | Assessment |
|---|---|---|
| `data/raw/gold_path_biosamples.tsv` | No exact path or node row. | No biosample count should be emitted. |
| `data/raw/gold_path_triads.tsv` | No exact path row. | No MIxS triad evidence should be emitted as `environmental_parameters`. |
| `data/raw/gold_studies.tsv` | No exact path row. | No study-level context is available from the maintained GOLD study table. |

There is no claim-level evidence, causal graph, or reference-bearing assertion
on this seeded GOLD record.

## Completeness

- The generated target contains every slot currently emitted from the
  maintained exact GOLD row: minted identity, terrestrial category, seeded
  narrow grounding, the GOLD source attestation, the generated parent set, and
  one generated curation event.
- Empty `synonyms`, `environmental_parameters`, `characteristic_taxa`,
  `evidence`, `causal_graphs`, `discussion`, and `datasets` are appropriate
  for the current maintained inputs. No maintained exact GOLD biosample, triad,
  or study row exists for this source path, and no maintained curation input
  supplies an output synonym, taxon association, claim-level evidence item,
  causal overlay, discussion item, or dataset reference for this source
  concept.
- Ignored/hidden-inclusive exact searches covered `curation/decisions.tsv`,
  `curation/term_requests.tsv`, `curation/external_xrefs.tsv`,
  `curation/causal_graphs/`, and `history/` for
  `habitatmech:GOLD.854d6d1a1c`, `gold.ecosystem:5768`,
  `Environmental > Terrestrial > Soil > Arable > Agricultural land`, and
  `agricultural_land__529ac6cb`; no maintained curation row, overlay, or
  history entry was found.
- A gitignore-independent `find` search covered `reports/yaml_record_review/`
  before report creation; no exact `*-agricultural_land__529ac6cb.md` report
  was found.

## Findings

### Major

| ID | Finding | Evidence | Maintained owner |
|---|---|---|---|
| `HM-AGR-LAND-529AC6CB-001` | `parent_habitats` asserts `ENVO:01001184` `arable` as an is-a parent, but `ENVO:01001184` is an environmental quality, not a habitat superclass. | The raw GOLD row places the child at `Environmental > Terrestrial > Soil > Arable > Agricultural land`; the GOLD parent-path pass in `src/habitatmech/seed.py` links that child to the resolved `Environmental > Terrestrial > Soil > Arable` concept; the parent currently resolves by label to `ENVO:01001184`, whose ontology row labels it `arable` and whose subclass edge places it under `ENVO:01000203` `environmental condition`. | Add an item-level row for the parent source concept `habitatmech:GOLD.7ea9c48727` in `curation/decisions.tsv` so GOLD's `Arable` soil path no longer exact-grounds to the `ENVO:01001184` quality, then regenerate the corpus. |

No blocker or minor findings found.

## Recommended Edits

1. Add an item-level `curation/decisions.tsv` row for
   `habitatmech:GOLD.7ea9c48727`, the minted source concept for
   `Environmental > Terrestrial > Soil > Arable`, that prevents this GOLD path
   from adopting `ENVO:01001184` as an exact habitat identity. If the arable
   quality remains useful context, keep `ENVO:01001184` as an xref rather than
   as an identifier or parent.

2. Re-seed from the maintained input and confirm
   `data/habitats/terrestrial/agricultural_land__529ac6cb.yaml` no longer
   lists `ENVO:01001184` under `parent_habitats`. Do not hand-edit
   `data/habitats/`.

## Follow-up Checks

| Scope | Command or check |
|---|---|
| Target schema | `just validate data/habitats/terrestrial/agricultural_land__529ac6cb.yaml` |
| Closed-schema validation | `just validate-strict data/habitats/terrestrial/agricultural_land__529ac6cb.yaml` |
| Corpus reproduction | `just verify-corpus --max-diffs 1` |
| Worklist/report sanity | `just worklist --limit 2000` and `just report` |
| Causal overlays | `just validate-causal-all` |
| Term-request exports | `just term-requests-check` |
| History | `just validate-history` |
| Manual hierarchy check | Confirm the regenerated child keeps a strictly broader agricultural parent and no longer has `ENVO:01001184` in `parent_habitats` |
| Diff hygiene | `git diff --check` |

## Additional Notes

- `ENVO:00000077` is not the hierarchy defect in this target. It is a broader
  agricultural-ecosystem term for GOLD's reused `Agricultural land` leaf and
  belongs as a `NARROW` parent unless a future item-level review chooses a more
  specific source identity.
- The arable-path defect is the same general failure mode as other reviewed
  GOLD parent-path issues: an upstream source path can provide useful context
  without being a strict habitat superclass suitable for `parent_habitats`.
