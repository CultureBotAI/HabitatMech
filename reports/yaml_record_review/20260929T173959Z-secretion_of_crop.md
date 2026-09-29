# YAML Record Review: secretion of crop

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/host_associated/secretion_of_crop.yaml
- Started UTC: 2026-09-29T17:35:00Z
- Finished UTC: 2026-09-29T17:39:59Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/host_associated/secretion_of_crop.yaml` |
| Identifier | `UBERON:0012422` |
| Label | `secretion of crop` |
| Category | `HOST_ASSOCIATED` |
| Grounding | `CLOSE` |
| Mapping status | `REVIEWED` |
| Maintained inputs | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/raw/ontology_terms.tsv`, `data/raw/ontology_subclass_edges.tsv`, and the item-level decision in `curation/decisions.tsv` |

The record is generated, not hand-maintained. Its durable slug is pinned in
`data/habitats/PATHS.tsv`:

```text
UBERON:0012422	secretion_of_crop
```

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/secretion_of_crop.yaml` | Pass: no issues found. |
| `just validate-strict data/habitats/host_associated/secretion_of_crop.yaml` | Pass: 1 file scanned, 0 `ERROR` rows. |
| `just validate-causal-all` | Pass: 32 causal-graph curation files with 32 graphs. |
| `just validate-history` | Pass: 77 history records valid. |
| `just term-requests-check` | Pass: term-request table is current with 109 terms. |
| `just verify-corpus` | Pass: 3,206 expected records, 3,206 records on disk, 0 missing, 0 extra, 0 differing. |
| `just report --ungrounded-top 0 --out /private/var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/habitatmech-report-secretion-of-crop.tsv` | Pass; the generated row reports `CLOSE`, `REVIEWED`, one GOLD source, two parents, zero taxa, zero parameters, and zero causal graphs. |
| `just worklist --limit 40 --status all --out /private/var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/habitatmech-worklist-secretion-of-crop.tsv` | Pass; the worklist wrote 953 ungrounded rows and does not include `UBERON:0012422`. |
| Focused reference validation | No standalone `validate-references` target exists; a hidden/ignored-inclusive search for `validate-references` across `justfile`, `.claude`, `docs`, `src`, and `scripts` found no target. |

The generated report indexes the reviewed row as:

```text
UBERON:0012422	secretion of crop	HOST_ASSOCIATED	CLOSE	REVIEWED	GOLD	1	0	True	2	0	0	0	data/habitats/host_associated/secretion_of_crop.yaml
```

## Identity and Grounding

| Claim | Check | Verdict |
|---|---|---|
| The record represents GOLD Bird `Crop milk`. | `data/raw/gold_ecosystem_paths.tsv:1870` has exactly `Host-associated > Birds > Digestive system > Esophagus > Crop milk` with leaf label `Crop milk`, depth 5, one GOLD node, zero organism/study/biosample/total assertions, and `gold.ecosystem:7427`. | Supported. |
| GOLD `Crop milk` is reviewed against `UBERON:0012422`. | `curation/decisions.tsv:1767` records an item-level `REVIEW` for source concept `habitatmech:GOLD.85ca0baf23`; the generated history preserves that the close grounding was read against the full GOLD path and the term definition. | Supported. |
| `UBERON:0012422` is the vendored `secretion of crop` term with `crop milk` as a synonym. | `data/raw/ontology_terms.tsv:13450` has identifier `UBERON:0012422`, label `secretion of crop`, the crop-secretion definition, and synonym `crop milk`. | Supported. |
| `CLOSE`, not `EXACT`, matches the committed curation. | The source leaf names `Crop milk`; the ontology identity names the species-neutral nutritional fluid secreted by the crop and carries `crop milk` as a synonym; the item-level curation decision explicitly kept `CLOSE` after comparing the source path with the definition. | Supported. |
| `UBERON:0000463` is an ontology superclass. | `data/raw/ontology_subclass_edges.tsv:11755` has `UBERON:0012422 rdfs:subClassOf UBERON:0000463`; `data/raw/ontology_terms.tsv:12940` labels that parent `organism substance`. | Supported. |
| The generated source-path parent is Bird `Esophagus`. | The full GOLD path puts `Crop milk` under `Host-associated > Birds > Digestive system > Esophagus`, and the generated parent `habitatmech:GOLD.b2fc8fb1e4` is the reviewed Bird `Esophagus` record for that source path. | Supported. |
| The record is distinct from GOLD `Crop content`. | Hidden/ignored-inclusive exact searches for `UBERON:0012422`, `gold.ecosystem:7427`, and `Crop milk` found this YAML, the raw GOLD row, the reviewed decision row, and sibling mentions in prior Bird reports; the adjacent `Crop content` record has a different source id, `gold.ecosystem:7426`, and a different minted identifier, `habitatmech:GOLD.57a0497838`. | Supported. |

## Evidence

This record carries a GOLD source attestation, ontology-derived definition and
synonym, ontology-derived parent, source-path parent, and generated curation
history. It has no characteristic taxa, environmental parameters, causal graph
edges, `discussions`, or `quality_flags`.

| Evidence-bearing claim | Source support | Verdict |
|---|---|---|
| GOLD has one node for `Host-associated > Birds > Digestive system > Esophagus > Crop milk`. | `data/raw/gold_ecosystem_paths.tsv:1870` lists `gold.ecosystem:7427` and `gold_node_count` 1. | Supported. |
| The raw GOLD path contributes no organism, study, biosample, or total assertions. | The same raw row has `organism_count`, `study_count`, `biosample_count`, and `total_assertions` all set to 0. | Supported; no missing characteristic taxa follow from this source. |
| The definition comes from UBERON. | `data/raw/ontology_terms.tsv:13450` supplies the exact generated definition text for `UBERON:0012422`, and the YAML marks `definition_source: UBERON`. | Supported. |

No PubMed, DOI, PMID, GOLD biosample, environmental-triad, or causal evidence
objects are cited by the record, so there were no external article or MIxS
claims to verify. iModulonDB was not applicable because the record names no
gene, locus tag, regulator, pathway, stress response, trait, or transcriptomics
dataset.

## Completeness

- The record has all expected ontology-derived content for `UBERON:0012422`:
  label, definition, definition source, `crop milk` synonym, and the
  `organism substance` superclass.
- The single GOLD source concept feeding the record has an item-level
  `REVIEW` decision, so the generated `mapping_status: REVIEWED` is justified.
- The raw GOLD row has zero assertions, so leaving `characteristic_taxa`,
  `environmental_parameters`, and `causal_graphs` empty does not contradict the
  inspected maintained input.
- Hidden/ignored-inclusive exact searches for `UBERON:0012422`,
  `habitatmech:GOLD.85ca0baf23`, `gold.ecosystem:7427`, and the full GOLD
  source path across `data/habitats`, `data/raw`, `curation`, `history`,
  `research`, `reports`, and `conf` found no unaccounted second source concept,
  history record, research report, or causal overlay for this reviewed source.
- A hidden/ignored-inclusive `find` under `reports/yaml_record_review`,
  `research/habitats`, `history`, and `curation/causal_graphs` found no
  existing `secretion_of_crop`, `secretion-of-crop`, `crop_milk`, or
  `crop-milk` sidecar.

## Findings

None found. No blocker, major, or minor findings were found.

## Recommended Edits

None.

## Follow-up Checks

None required for the current record. If GOLD source paths, UBERON term data,
or the item-level `curation/decisions.tsv` row for
`habitatmech:GOLD.85ca0baf23` change later, rerun:

1. `just validate data/habitats/host_associated/secretion_of_crop.yaml`
2. `just validate-strict data/habitats/host_associated/secretion_of_crop.yaml`
3. `just verify-corpus`
4. `just report --ungrounded-top 0 --out <writable-temp>/habitatmech-report-secretion-of-crop.tsv`

## Additional Notes

- The hidden/ignored-inclusive searches required to establish absence included
  ignored files and hidden files via `rg --no-ignore --hidden` or `find`.
- The exact start time of this review was not captured before the first
  evidence commands. `Started UTC` is rounded to the nearest observed review
  window.
- The reviewed source path has zero GOLD assertions. That is not a data
  integrity defect, but it means this GOLD leaf supplies no organism evidence
  beyond the source inventory row itself.
