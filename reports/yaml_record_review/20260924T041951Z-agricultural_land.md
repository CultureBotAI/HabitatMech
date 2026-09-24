# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/terrestrial/agricultural_land.yaml`
- Started UTC: 2026-09-24T04:04:00Z
- Finished UTC: 2026-09-24T04:19:51Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/terrestrial/agricultural_land.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.41a1abb4c2` |
| Label | `Agricultural land` |
| Category | `TERRESTRIAL` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Maintained owners | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/raw/ontology_terms.tsv`, `data/raw/ontology_subclass_edges.tsv`, `data/habitats/PATHS.tsv`, `curation/term_requests.tsv`, and `src/habitatmech/seed.py`; `data/habitats/` is generated and remains read-only |

This generated GOLD-only record represents the path:

```text
Environmental > Terrestrial > Soil > Loam > Agricultural land
```

It is one of seven distinct GOLD `Agricultural land` leaves pinned in `data/habitats/PATHS.tsv`; this review covers only `gold.ecosystem:4242` and its stable minted identifier `habitatmech:GOLD.41a1abb4c2`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/terrestrial/agricultural_land.yaml` | Passed: LinkML reported no issues |
| `just validate-strict data/habitats/terrestrial/agricultural_land.yaml` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| `just validate-causal <overlay>` | Not applicable: the record has no `causal_graphs` slot, and ignored/hidden-inclusive searches of `curation/causal_graphs/` found no overlay for `habitatmech:GOLD.41a1abb4c2` or `agricultural_land` |
| `just validate-causal-all` | Passed: 32 causal-graph curation files with 32 graphs |
| `just term-requests-check` | Passed: term-request table is current with 109 terms |
| `just validate-history` | Passed: no issues found; 77 history records valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Passed: expected 3,206 records, found 3,206, 0 missing, 0 extra, 0 differing |
| `just worklist --limit 2000` | Passed: 0 ungrounded records still undecided, 1,810 decisions on file |
| `just report` | Passed: corpus report completed for 3,206 records |
| Reference validator | Not applicable: this record has no DOI, PMID, URL, `EvidenceItem`, or causal-edge evidence that would need citation checking |
| `git diff --check` | Passed |

## Identity and Grounding

The source identity is internally consistent:

| Claim | Maintained evidence | Assessment |
|---|---|---|
| The output identifier is `habitatmech:GOLD.41a1abb4c2`. | `data/habitats/PATHS.tsv` pins that identifier to `agricultural_land`. | Supported. |
| The GOLD source is `gold.ecosystem:4242`. | `data/raw/gold_ecosystem_paths.tsv` has a row for `Environmental > Terrestrial > Soil > Loam > Agricultural land` with leaf label `Agricultural land`, one GOLD node ID, one organism assertion, and one total assertion. | Supported. |
| The record is narrower than `ENVO:00000077` `agricultural ecosystem`. | The leaf label `Agricultural land` matches a synonym on the vendored `ENVO:00000077` row, while the seeder mints a GOLD identifier because the same leaf is reused under several more specific soil-type paths. | Supported. |
| `ENVO:00002258` `loam` is a broader habitat for this record. | The GOLD second pass in `src/habitatmech/seed.py` adds the concept resolved for parent path `Environmental > Terrestrial > Soil > Loam`; that path resolves to `ENVO:00002258`. | Unsupported as an is-a edge. `loam` is a soil material, while the GOLD source denotes agricultural land in a loam context. |

No item-level curator decision currently exists for this source. Ignored/hidden-inclusive searches of `curation/decisions.tsv`, `curation/term_requests.tsv`, `curation/external_xrefs.tsv`, and `curation/causal_graphs/` found no `habitatmech:GOLD.41a1abb4c2`, no `gold.ecosystem:4242`, and no exact `Agricultural land` row for this concept, so `mapping_status: SEEDED` is expected.

## Evidence

The source attestation is accurately transcribed from `data/raw/gold_ecosystem_paths.tsv`:

- `source: GOLD`
- `source_id: gold.ecosystem:4242`
- `source_label: Agricultural land`
- `source_path: Environmental > Terrestrial > Soil > Loam > Agricultural land`
- `mapping_predicate: skos:narrowMatch`
- `assertion_count: 1`
- `assertion_unit: ORGANISM`

The record has no curator-authored record-level evidence, characteristic taxa, environmental parameters, or causal graph. That is acceptable for this source-seeded record: the current claim is limited to a GOLD vocabulary attestation and generated ontology placement.

The maintained MIxS triad inventory points away from the generated `loam` parent. For the exact source path, `data/raw/gold_path_triads.tsv` records one agreeing study with `ENVO:00000446` `terrestrial biome` at broad scale, `ENVO:00000114` `agricultural field` at local scale, and `ENVO:00005802` `bulk soil` at medium scale. Those triads support interpreting the sample as bulk soil from an agricultural field in a terrestrial setting; they do not support publishing the whole `Agricultural land` source path as a subclass of `ENVO:00002258` `loam`.

## Completeness

The record is complete for the current raw GOLD input, but its generated hierarchy needs curation.

| Slot | Status |
|---|---|
| Source attestation | Complete for the exact `gold.ecosystem:4242` row and its one organism assertion |
| Definition | Empty because no item-level `curation/term_requests.tsv` row defines `habitatmech:GOLD.41a1abb4c2` |
| Causal graph | Empty; ignored/hidden-inclusive searches found no target overlay |
| Environmental parameters | Empty; no inspected maintained input asserts parameters for this GOLD source |
| Characteristic taxa | Empty; GOLD source occurrence is not a taxon association table |
| Evidence | Empty; no curator-authored definition, hierarchy edge, or causal edge exists that would need claim-level literature |

Bounded absence checks used ignored and hidden files:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-agricultural_land.md' -print` found no prior exact-stem review before this report was written.
- Exact searches for `habitatmech:GOLD.41a1abb4c2`, `gold.ecosystem:4242`, and `Environmental > Terrestrial > Soil > Loam > Agricultural land` covered `curation`, `data/raw`, `data/habitats/PATHS.tsv`, and the target YAML, and found the generated target, the path lock, and the GOLD raw rows.
- Exact searches for `habitatmech:GOLD.41a1abb4c2`, `gold.ecosystem:4242`, and `Agricultural land` covered `curation/decisions.tsv`, `curation/term_requests.tsv`, `curation/external_xrefs.tsv`, and `curation/causal_graphs/`; no maintained curation row was found for this source concept.
- Exact searches for `habitatmech:GOLD.41a1abb4c2` and `agricultural_land` covered `curation/causal_graphs/`; no target overlay was found.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-AGLAND-001 | major | `parent_habitats` asserts `habitatmech:GOLD.41a1abb4c2` is a kind of `ENVO:00002258` `loam`. That edge comes from the GOLD path parent `Environmental > Terrestrial > Soil > Loam`, but `loam` is a soil material and the child concept is agricultural land in a loam-soil context. The exact GOLD triad row classifies the source's medium as `ENVO:00005802` `bulk soil`, not `loam`. | Add an item-level definition for `habitatmech:GOLD.41a1abb4c2` in `curation/term_requests.tsv` with `parent_mode: REPLACE`, or add a maintained GOLD path-parent override in `src/habitatmech/seed.py` so this source path keeps `ENVO:00000077` without inheriting the false `ENVO:00002258` parent. |

No blocker or minor findings were found.

## Recommended Edits

1. Keep future corrections out of `data/habitats/terrestrial/agricultural_land.yaml`; it reproduces exactly from `data/raw/`.
2. Curate `habitatmech:GOLD.41a1abb4c2` at item depth.
3. Either add a real HabitatMech term request for the loam agricultural-land concept with the correct broader class and `parent_mode: REPLACE`, or introduce a small maintained override table that lets the GOLD parent-path pass drop the `ENVO:00002258` edge for `Environmental > Terrestrial > Soil > Loam > Agricultural land`.
4. Regenerate the corpus and confirm the record keeps the `ENVO:00000077` parent while dropping `ENVO:00002258`.

## Follow-up Checks

| Scope | Command |
|---|---|
| Dry-run regeneration | `just seed` |
| Target canary | `just seed-canary habitatmech:GOLD.41a1abb4c2` |
| Causal overlays | `just validate-causal-all` |
| Target schema | `just validate data/habitats/terrestrial/agricultural_land.yaml` |
| Closed-schema validation | `just validate-strict data/habitats/terrestrial/agricultural_land.yaml` |
| Term-request exports | `just term-requests-check` |
| History | `just validate-history` |
| Corpus reproduction | `just verify-corpus --max-diffs 1` |
| Worklist/report sanity | `just worklist --limit 2000` and `just report` |
| Diff hygiene | `git diff --check` |

Manual follow-up should verify that:

- `identifier` remains `habitatmech:GOLD.41a1abb4c2`.
- `grounding_status` remains `NARROW` unless a curator chooses a different explicit grounding decision.
- `source_attestations` still has exactly one GOLD entry for `gold.ecosystem:4242`.
- `parent_habitats` no longer contains `ENVO:00002258`.

## Additional Notes

- The generated `ENVO:00000077` parent is not the issue in this target. It is the matched parent for GOLD's reused `Agricultural land` leaf and is broader than this loam-scoped source path.
- Several sibling `Agricultural land` leaves have the same mechanical pattern under `Clay`, `Unclassified`, `Greenhouse`, `Pasture`, `Ranch`, and `Arable`. Each has a distinct minted identifier and should be reviewed against its own source path and inherited GOLD parent.
- The one local MIxS triad row for this exact path names `ENVO:00000114` `agricultural field`, while the top-level ontology parent is `ENVO:00000077` `agricultural ecosystem`. That is a near miss to check during future curation, but it does not by itself prove either term is an exact identity for the loam-scoped GOLD concept.
