# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/terrestrial/agricultural_land__b27d5e0e.yaml`
- Started UTC: 2026-09-24T06:23:39Z
- Finished UTC: 2026-09-24T06:41:09Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/terrestrial/agricultural_land__b27d5e0e.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.84791b320c` |
| Label | `Agricultural land` |
| Category | `TERRESTRIAL` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| GOLD source-concept key | `habitatmech:GOLD.84791b320c` |
| GOLD parent source-concept key | `habitatmech:GOLD.b102e734ce` |
| Maintained owners | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/raw/ontology_terms.tsv`, `data/raw/ontology_subclass_edges.tsv`, `data/habitats/PATHS.tsv`, and `src/habitatmech/seed.py`; `data/habitats/` is generated and remains read-only |

This generated GOLD-only record represents `gold.ecosystem:5727`:

```text
Environmental > Terrestrial > Soil > Ranch > Agricultural land
```

The source concept is one of the collision-pinned GOLD `Agricultural land`
leaves. This review covers only the `Ranch`-scoped source concept with stable
minted identifier `habitatmech:GOLD.84791b320c`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/terrestrial/agricultural_land__b27d5e0e.yaml` | Passed: LinkML reported no issues |
| `just validate-strict data/habitats/terrestrial/agricultural_land__b27d5e0e.yaml` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| `just validate-causal <overlay>` | Not applicable: the record has no `causal_graphs` slot, and ignored/hidden-inclusive searches of `curation/causal_graphs/` found no overlay for `habitatmech:GOLD.84791b320c`, `gold.ecosystem:5727`, or `agricultural_land__b27d5e0e` |
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
| The output identifier is `habitatmech:GOLD.84791b320c`. | `data/habitats/PATHS.tsv` pins that identifier to `agricultural_land__b27d5e0e`. | Supported. |
| The GOLD source ID is `gold.ecosystem:5727`. | `data/raw/gold_ecosystem_paths.tsv` has one row for `Environmental > Terrestrial > Soil > Ranch > Agricultural land` with one GOLD node ID, depth 5, and zero organism, study, biosample, or total assertions. | Supported. |
| The source belongs in the terrestrial category. | `src/habitatmech/seed.py` infers the category from GOLD's `Environmental > Terrestrial` prefix for this raw row. | Supported. |
| `ENVO:00000077` `agricultural ecosystem` is a broader habitat for this source concept. | The reused GOLD leaf `Agricultural land` matches a synonym on the vendored `ENVO:00000077` row; the seeder keeps the exact ontology term as a parent because other GOLD paths reuse the same leaf. | Supported. |
| `ENVO:01001207` `ranch` is a broader habitat for this source concept. | `src/habitatmech/seed.py` links each GOLD concept to the resolved concept of its parent path; the parent path `Environmental > Terrestrial > Soil > Ranch` currently resolves to `ENVO:01001207`, whose vendored definition is an area of land used for herding and grazing livestock. | Supported. |
| `mapping_status` is `SEEDED`. | Ignored/hidden-inclusive exact searches found no item-level `curation/decisions.tsv` decision for `habitatmech:GOLD.84791b320c`, `gold.ecosystem:5727`, `Environmental > Terrestrial > Soil > Ranch > Agricultural land`, or `agricultural_land__b27d5e0e`. | Supported. |

The generated minted-child identity and both generated parent links are
defensible. GOLD scopes this reused `Agricultural land` leaf under the `Ranch`
path, the exact source concept is narrower than the generic agricultural
ecosystem term, and the parent path resolves to an area-of-land term rather
than to a quality or process.

## Evidence

The source attestation is an accurate transcription of the committed GOLD row:

- `source: GOLD`
- `source_id: gold.ecosystem:5727`
- `source_label: Agricultural land`
- `source_path: Environmental > Terrestrial > Soil > Ranch > Agricultural land`
- `mapping_predicate: skos:narrowMatch`

The attestation correctly omits `assertion_count` and `assertion_unit`: the
maintained GOLD ecosystem-path row for `gold.ecosystem:5727` has
`organism_count`, `study_count`, `biosample_count`, and `total_assertions` all
set to `0`.

Additional GOLD-derived evidence is consistent with a ranch agricultural-land
source:

| Source | Maintained row | Assessment |
|---|---|---|
| Biosamples | `data/raw/gold_path_biosamples.tsv` maps the same exact path and node `5727` to 73 biosamples. | Supported; biosample counts are independent of the `ORGANISM` count in the generated source attestation and are not emitted on this record. |
| GOLD studies | `data/raw/gold_studies.tsv` has two study rows that include `Environmental > Terrestrial > Soil > Ranch > Agricultural land`. | Supports multi-study use of the exact GOLD source path. |
| MIxS broad scale | `data/raw/gold_path_triads.tsv` summarizes 73 samples from 2 studies and ranks `ENVO:00000446` `terrestrial biome` as the broad-scale top term with 100% sample share. | Supports the generated terrestrial category. |
| MIxS local scale | The same triad block ranks `ENVO:01001207` `ranch` as the local-scale top term with 100% sample share from 2 studies. | Supports `ranch` as the parent-path local context for this exact source. |
| MIxS medium | The same triad block ranks `ENVO:00002259` `agricultural soil` as the medium top term with 100% sample share from 2 studies. | Supports the agricultural-soil material context and is compatible with both generated parents. |

There is no claim-level evidence, causal graph, or reference-bearing assertion
on this seeded GOLD record.

## Completeness

- The generated target contains every slot currently emitted from the
  maintained exact GOLD row: minted identity, terrestrial category, seeded
  narrow grounding, the GOLD source attestation, the generated parent set, and
  one generated curation event.
- Empty `synonyms`, `environmental_parameters`, `characteristic_taxa`,
  `evidence`, `causal_graphs`, `discussion`, and `datasets` are appropriate for
  the current maintained inputs. The reviewed GOLD triad rows provide
  contextual evidence for this source path; no maintained input emits them as
  `environmental_parameters`, and no maintained input supplies an output
  synonym, taxon association, claim-level evidence item, causal overlay,
  discussion item, or dataset reference for this source concept.
- Ignored/hidden-inclusive exact searches covered `curation/decisions.tsv`,
  `curation/term_requests.tsv`, `curation/external_xrefs.tsv`,
  `curation/causal_graphs/`, `history/`, `reports/yaml_record_review/`, and
  `research/` for `habitatmech:GOLD.84791b320c`, `gold.ecosystem:5727`,
  `Environmental > Terrestrial > Soil > Ranch > Agricultural land`, and
  `agricultural_land__b27d5e0e`; no maintained curation row, overlay, history
  entry, prior exact report, or research item was found.
- A gitignore-independent `find` search covered `reports/yaml_record_review/`
  before report creation; no exact `*-agricultural_land__b27d5e0e.md` report
  was found.

## Findings

No blocker, major, or minor findings found.

## Recommended Edits

No record edits are recommended.

## Follow-up Checks

| Scope | Command or check |
|---|---|
| Target schema | `just validate data/habitats/terrestrial/agricultural_land__b27d5e0e.yaml` |
| Closed-schema validation | `just validate-strict data/habitats/terrestrial/agricultural_land__b27d5e0e.yaml` |
| Corpus reproduction | `just verify-corpus --max-diffs 1` |
| Worklist/report sanity | `just worklist --limit 2000` and `just report` |
| Causal overlays | `just validate-causal-all` |
| Term-request exports | `just term-requests-check` |
| History | `just validate-history` |
| Manual hierarchy check | Confirm the generated child keeps `ENVO:00000077` and `ENVO:01001207` in `parent_habitats` |
| Diff hygiene | `git diff --check` |

## Additional Notes

This Ranch-scoped GOLD leaf does not share the hierarchy defects found in some
other collision-pinned `Agricultural land` leaves. Its immediate GOLD parent is
an area of land used for livestock, and the exact path's two-study MIxS triad
corroborates `ranch` as the local-scale environmental term and
`agricultural soil` as the material context.
