# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/terrestrial/agricultural_land__3b8e1d48.yaml`
- Started UTC: 2026-09-24T04:58:00Z
- Finished UTC: 2026-09-24T05:06:24Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/terrestrial/agricultural_land__3b8e1d48.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.b43776b642` |
| Label | `Agricultural land` |
| Category | `TERRESTRIAL` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Maintained owners | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, `data/raw/ontology_terms.tsv`, `data/raw/ontology_subclass_edges.tsv`, `data/habitats/PATHS.tsv`, `curation/decisions.tsv`, and `src/habitatmech/seed.py`; `data/habitats/` is generated and remains read-only |

This generated GOLD-only record represents `gold.ecosystem:5729`:

```text
Environmental > Terrestrial > Soil > Pasture > Agricultural land
```

It is one of the collision-pinned GOLD `Agricultural land` leaves. This review covers only the `Pasture`-scoped source concept with stable minted identifier `habitatmech:GOLD.b43776b642`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/terrestrial/agricultural_land__3b8e1d48.yaml` | Passed: LinkML reported no issues |
| `just validate-strict data/habitats/terrestrial/agricultural_land__3b8e1d48.yaml` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| `just validate-causal <overlay>` | Not applicable: the record has no `causal_graphs` slot, and ignored/hidden-inclusive searches of `curation/causal_graphs/` found no overlay for `habitatmech:GOLD.b43776b642` or `agricultural_land__3b8e1d48` |
| `just validate-causal-all` | Passed: 32 causal-graph curation files with 32 graphs |
| `just term-requests-check` | Passed: term-request table is current with 109 terms |
| `just validate-history` | Passed: no issues found; 77 history records valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Passed: expected 3,206 records, found 3,206, 0 missing, 0 extra, 0 differing |
| `just worklist --limit 2000` | Passed: 0 ungrounded records still undecided, 1,810 decisions on file |
| `just report` | Passed: corpus report completed for 3,206 records |
| Reference validator | Not applicable: this record has no DOI, PMID, URL, `EvidenceItem`, or causal-edge evidence that would need citation checking |
| `git diff --check` | Passed |

## Identity and Grounding

The generated identity is internally consistent:

| Claim | Maintained evidence | Assessment |
|---|---|---|
| The output identifier is `habitatmech:GOLD.b43776b642`. | `data/habitats/PATHS.tsv` pins that identifier to `agricultural_land__3b8e1d48`. | Supported. |
| The GOLD source ID is `gold.ecosystem:5729`. | `data/raw/gold_ecosystem_paths.tsv` has one row for `Environmental > Terrestrial > Soil > Pasture > Agricultural land` with one GOLD node ID and one organism assertion. | Supported. |
| The source belongs in the terrestrial category. | `src/habitatmech/seed.py` infers the category from GOLD's `Environmental > Terrestrial` prefix for this raw row. | Supported. |
| `ENVO:00000077` `agricultural ecosystem` is a broader habitat for this source concept. | The reused GOLD leaf `Agricultural land` matches a synonym on the vendored `ENVO:00000077` row; the seeder keeps the exact ontology term as a parent because other GOLD paths reuse the same leaf. | Supported. |
| `ENVO:00000266` `pasture` is a broader habitat for this source concept. | The GOLD parent-path pass links the child path to `Environmental > Terrestrial > Soil > Pasture`, and that collapsed parent source resolves to `ENVO:00000266` `pasture`, defined as a grassland ecosystem used for grazing livestock. | Supported. |
| `mapping_status` is `SEEDED`. | Ignored/hidden-inclusive exact searches found no item-level `curation/decisions.tsv` decision for `habitatmech:GOLD.b43776b642` or `gold.ecosystem:5729`. | Supported. |

The two generated parents also agree with each other in the vendored ontology slice: `data/raw/ontology_subclass_edges.tsv` asserts `ENVO:00000266 rdfs:subClassOf ENVO:00000077`, so the pasture parent is already a subclass of agricultural ecosystem.

## Evidence

The source attestation is an accurate transcription of the committed GOLD row:

- `source: GOLD`
- `source_id: gold.ecosystem:5729`
- `source_label: Agricultural land`
- `source_path: Environmental > Terrestrial > Soil > Pasture > Agricultural land`
- `mapping_predicate: skos:narrowMatch`
- `assertion_count: 1`
- `assertion_unit: ORGANISM`

Additional GOLD-derived evidence is consistent with a pasture-scoped source:

| Source | Maintained row | Assessment |
|---|---|---|
| Biosamples | `data/raw/gold_path_biosamples.tsv` maps the same exact path and node `5729` to 13 biosamples. | Supported; biosample counts are independent of the `ORGANISM` count in the generated source attestation and are not emitted on this record. |
| MIxS broad scale | `data/raw/gold_path_triads.tsv` summarizes 13 samples from 2 studies and ranks `ENVO:01000177` `grassland biome` as the broad-scale top term. | Supported as contextual evidence; the top broad term covers 85% of the samples and one agreeing study, so it is weaker than the local and medium rows. |
| MIxS local scale | The same triad block ranks `ENVO:00000266` `pasture` as the local-scale top term with 100% sample share and 2 agreeing studies. | Supports the generated pasture parent. |
| MIxS medium | The same triad block ranks `ENVO:00005773` `pasture soil` as the medium top term with 100% sample share and 2 agreeing studies. | Supports pasture soil as the submitted material context; it does not require a separate source identity because the generated record makes no material claim. |

The record has no curator-authored record-level evidence, characteristic taxa, environmental parameters, or causal graph. That is acceptable for this single-source seeded record: the only published claims are the GOLD vocabulary attestation and generated ontology placement above.

## Completeness

The target is complete for the current raw GOLD input.

| Slot | Status |
|---|---|
| Source attestation | Complete for the exact `gold.ecosystem:5729` row and its one organism assertion |
| Definition | Empty because no item-level `curation/term_requests.tsv` row defines `habitatmech:GOLD.b43776b642` |
| Causal graph | Empty; ignored/hidden-inclusive searches found no target overlay |
| Environmental parameters | Empty; no inspected maintained input asserts physicochemical parameters for this source |
| Characteristic taxa | Empty; GOLD source occurrence is not a PREGO, BacDive, or Madin taxon-association table |
| Evidence | Empty; no curator-authored definition, hierarchy edge, characteristic taxon, or causal edge exists that would need claim-level literature |

Bounded absence checks used ignored and hidden files:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-agricultural_land__3b8e1d48.md' -print` found no prior exact-stem review before this report was written.
- Exact searches for `habitatmech:GOLD.b43776b642`, `gold.ecosystem:5729`, and `agricultural_land__3b8e1d48` covered `curation`, `data/raw`, `data/habitats/PATHS.tsv`, `data/habitats/terrestrial`, and `reports/yaml_record_review`.
- Exact searches for `habitatmech:GOLD.b43776b642`, `gold.ecosystem:5729`, `agricultural_land__3b8e1d48`, and `Agricultural land` covered `curation/decisions.tsv`, `curation/term_requests.tsv`, `curation/external_xrefs.tsv`, and `curation/causal_graphs/`; no maintained curation row was found for this source concept.
- Exact searches for `habitatmech:GOLD.b43776b642` and `agricultural_land__3b8e1d48` covered `curation/causal_graphs/`; no target overlay was found.

## Findings

None found.

## Recommended Edits

None.

Keep any future changes out of `data/habitats/terrestrial/agricultural_land__3b8e1d48.yaml`; it is generated and currently reproduces exactly from `data/raw/`.

## Follow-up Checks

No corrective edit is recommended. If the record is changed later, re-run:

| Scope | Command |
|---|---|
| Target schema | `just validate data/habitats/terrestrial/agricultural_land__3b8e1d48.yaml` |
| Closed-schema validation | `just validate-strict data/habitats/terrestrial/agricultural_land__3b8e1d48.yaml` |
| Causal overlays | `just validate-causal-all` |
| Term-request exports | `just term-requests-check` |
| History | `just validate-history` |
| Corpus reproduction | `just verify-corpus --max-diffs 1` |
| Worklist/report sanity | `just worklist --limit 2000` and `just report` |
| Diff hygiene | `git diff --check` |

## Additional Notes

- The sibling `Environmental > Terrestrial > Soil > Loam > Agricultural land` and `Environmental > Terrestrial > Soil > Unclassified > Agricultural land` records have their own review findings; those do not automatically transfer to this pasture-scoped source.
- The exact GOLD path has much lower direct GOLD organism support than several sibling agricultural-land paths, but the asserted count of one organism is faithfully represented and not over-summed with the 13 biosamples or MIxS triad sample totals.
