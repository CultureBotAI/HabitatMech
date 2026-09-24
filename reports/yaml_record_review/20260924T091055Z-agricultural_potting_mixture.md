# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/terrestrial/agricultural_potting_mixture.yaml`
- Started UTC: 2026-09-24T09:00:35Z
- Finished UTC: 2026-09-24T09:10:55Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/terrestrial/agricultural_potting_mixture.yaml` |
| Class | `HabitatRecord` |
| Identifier | `ENVO:03000133` |
| Label | `agricultural potting mixture` |
| Category | `TERRESTRIAL` |
| Grounding status | `CLOSE` |
| Mapping status | `REVIEWED` |
| GOLD source-concept key | `habitatmech:GOLD.02b5e64573` |
| Maintained owners | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/raw/ontology_terms.tsv`, `data/raw/ontology_subclass_edges.tsv`, `curation/decisions.tsv`, `data/habitats/PATHS.tsv`, and `src/habitatmech/seed.py`; `data/habitats/` is generated and remains read-only |

This generated GOLD-only record reviews the path:

```text
Environmental > Terrestrial > Soil > Potting soil
```

That GOLD source path, keyed for curation as `habitatmech:GOLD.02b5e64573`,
is close-grounded to ENVO `agricultural potting mixture`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/terrestrial/agricultural_potting_mixture.yaml` | Passed: LinkML reported no issues |
| `just validate-strict data/habitats/terrestrial/agricultural_potting_mixture.yaml` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| `just validate-causal <overlay>` | Not applicable: the record has no `causal_graphs` slot, and ignored/hidden-inclusive exact searches found no `curation/causal_graphs/` overlay for `ENVO:03000133`, `habitatmech:GOLD.02b5e64573`, `Environmental > Terrestrial > Soil > Potting soil`, or `agricultural_potting_mixture` |
| `just validate-causal-all` | Passed: 32 causal-graph curation files with 32 graphs |
| `just term-requests-check` | Passed: term-request table is current with 109 terms |
| `just validate-history` | Passed: no issues found; 77 history records valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Passed: expected 3,206 records, found 3,206, 0 missing, 0 extra, 0 differing |
| `just worklist --limit 2000` | Passed: 0 ungrounded records still undecided, 1,810 decisions on file |
| `just report` | Passed: corpus report completed for 3,206 records |
| Reference validator | Not applicable: this record has no DOI, PMID, URL, `EvidenceItem`, or causal-edge evidence that would need citation checking |
| `git diff --check` | Passed before and after this report was written |

## Identity and Grounding

| Claim | Maintained evidence | Assessment |
|---|---|---|
| The output identifier is `ENVO:03000133`. | `data/habitats/PATHS.tsv` pins `ENVO:03000133` to `agricultural_potting_mixture`. | Supported. |
| The label, definition, and lowercase `potting soil` synonym are ENVO-derived. | `data/raw/ontology_terms.tsv` has `term_id` `ENVO:03000133`, `ontology` `ENVO`, label `agricultural potting mixture`, the emitted definition, and synonym `potting soil`. | Supported. |
| The GOLD source concept has an item-level `REVIEW` decision. | `curation/decisions.tsv` keys `habitatmech:GOLD.02b5e64573` to `REVIEW`, `review_depth` `ITEM`, and the note says the close grounding was read against the full source path and ENVO term definition. | Supported. |
| The GOLD source path maps to `gold.ecosystem:5778`. | `data/raw/gold_ecosystem_paths.tsv` has one row for `Environmental > Terrestrial > Soil > Potting soil` with two GOLD node IDs, `gold.ecosystem:5778|gold.ecosystem:5779`; the generated attestation uses the first node and records the duplicate-node note. | Supported. |
| `mapping_predicate: skos:closeMatch` and `grounding_status: CLOSE` match the curated decision. | The `curation/decisions.tsv` item-level `REVIEW` row endorses the seeder's close grounding. | Supported. |
| `ENVO:0010003` `agricultural environmental material` is a strict parent. | `data/raw/ontology_subclass_edges.tsv` asserts `ENVO:03000133 rdfs:subClassOf ENVO:0010003`. | Supported. |
| `ENVO:00001998` `soil` is a strict parent. | `src/habitatmech/seed.py` links each GOLD concept to its parent source path; here that turns GOLD's `Environmental > Terrestrial > Soil` source parent into an `ENVO:00001998` `parent_habitats` entry. | Not supported: ENVO places `agricultural potting mixture` under agricultural environmental material, not under soil, and its definition allows mixtures of peat, composted bark, sand, perlite, or compost rather than requiring a soil material. |
| The source attestation has `assertion_count: 1` and `assertion_unit: ORGANISM`. | The exact `data/raw/gold_ecosystem_paths.tsv` row records `organism_count` 1 for the collapsed GOLD path. | Supported. |

The generated identity and close grounding are defensible: GOLD's source label
is `Potting soil`, ENVO lists `potting soil` as a synonym of
`agricultural potting mixture`, and the item-level curation row reviewed the
full source path before endorsing the seeder result. The record inherits one
false parent from GOLD path containment, however. A potting mixture is a growth
medium used like soil, but ENVO does not assert it under `soil`, and its
definition does not require the mineral, humus, interstitial gas, liquid, and
resident-biota composition that ENVO's `soil` class requires.

## Evidence

The source attestation is an accurate transcription of the committed GOLD row:

- `source: GOLD`
- `source_id: gold.ecosystem:5778`
- `source_label: Potting soil`
- `source_path: Environmental > Terrestrial > Soil > Potting soil`
- `mapping_predicate: skos:closeMatch`
- `assertion_count: 1`
- `assertion_unit: ORGANISM`
- `notes: 2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.`

The exact GOLD path has one maintained study row,
`data/raw/gold_studies.tsv` lists `Gs0154305`, and
`data/raw/gold_path_biosamples.tsv` maps the same path through
`gold.ecosystem` node `5779` to 44 biosamples. These support use of the GOLD
path, while leaving the generated source attestation's organism assertion count
unchanged.

Ignored/hidden-inclusive exact searches found no row for
`Environmental > Terrestrial > Soil > Potting soil` in
`data/raw/gold_path_triads.tsv`; no MIxS broad, local, or medium triad is
available for this exact GOLD path.

There is no claim-level evidence, causal graph, or reference-bearing assertion
on this reviewed GOLD record.

## Completeness

- The generated target contains every slot currently emitted from the
  maintained exact GOLD and ENVO rows: ontology identity, ENVO definition,
  GOLD and ENVO synonyms, terrestrial category, close grounding, the GOLD
  source attestation, ontology and source-path parents, and generated curation
  events.
- Empty `environmental_parameters`, `characteristic_taxa`, `evidence`,
  `causal_graphs`, `discussions`, and `datasets` are appropriate for the
  current maintained inputs. No maintained exact MIxS triad row, taxon
  association, claim-level evidence item, causal overlay, discussion item, or
  dataset reference was found for this source concept.
- Ignored/hidden-inclusive exact searches covered `curation/decisions.tsv`,
  `curation/term_requests.tsv`, `curation/external_xrefs.tsv`,
  `curation/causal_graphs/`, `history/`, `reports/yaml_record_review/`,
  `research/`, and the committed `data/raw/` inventories for `ENVO:03000133`,
  `habitatmech:GOLD.02b5e64573`,
  `Environmental > Terrestrial > Soil > Potting soil`, and
  `agricultural_potting_mixture`; they found the cited GOLD, ENVO,
  `PATHS.tsv`, and decision rows, and no maintained target term request,
  external xref, causal overlay, history file, prior exact review, or research
  report.
- A gitignore-independent `find` search covered `reports/yaml_record_review/`
  before report creation; no exact
  `*-agricultural_potting_mixture.md` report was found.

## Findings

### Major

| ID | Finding | Evidence | Maintained owner |
|---|---|---|---|
| `HM-AG-POTTING-001` | `parent_habitats` asserts `ENVO:00001998` `soil` as a strict is-a parent, but the record is grounded to `ENVO:03000133` `agricultural potting mixture`, whose vendored ontology parent is `ENVO:0010003` `agricultural environmental material` rather than soil. | `data/raw/ontology_subclass_edges.tsv` asserts only `ENVO:03000133 rdfs:subClassOf ENVO:0010003`; `data/raw/ontology_terms.tsv` defines `ENVO:03000133` as a mixture of materials such as peat, composted bark, sand, perlite, or compost; the extra `ENVO:00001998` edge is introduced by `src/habitatmech/seed.py` from GOLD's `Environmental > Terrestrial > Soil` path context. | Add a maintained parent-edge override or source-path parent suppression route in `src/habitatmech/seed.py` plus curation input, then apply it so this reviewed close-grounded record keeps `ENVO:0010003` and drops `ENVO:00001998`. |

No blocker or minor findings found.

## Recommended Edits

1. Add a maintained route for demoting or suppressing a GOLD parent-path edge
   when a reviewed ontology-grounded source keeps a correct non-exact identity
   but the source's path parent is contextual rather than strictly broader.

2. Apply that route to `habitatmech:GOLD.02b5e64573` or the exact
   `Environmental > Terrestrial > Soil > Potting soil` path so regenerated
   `data/habitats/terrestrial/agricultural_potting_mixture.yaml` keeps
   `ENVO:0010003` and drops `ENVO:00001998` from `parent_habitats`. Do not
   hand-edit `data/habitats/`.

## Follow-up Checks

| Scope | Command or check |
|---|---|
| Target schema | `just validate data/habitats/terrestrial/agricultural_potting_mixture.yaml` |
| Closed-schema validation | `just validate-strict data/habitats/terrestrial/agricultural_potting_mixture.yaml` |
| Corpus reproduction | `just verify-corpus --max-diffs 1` |
| Worklist/report sanity | `just worklist --limit 2000` and `just report` |
| Causal overlays | `just validate-causal-all` |
| Term-request exports | `just term-requests-check` |
| History | `just validate-history` |
| Manual hierarchy check | Confirm the regenerated record keeps `ENVO:0010003` and drops `ENVO:00001998` from `parent_habitats` |
| Diff hygiene | `git diff --check` |

## Additional Notes

- The item-level `curation/decisions.tsv` row is sufficient to support the
  generated `REVIEWED` mapping status because this record has one source
  concept.
- The duplicate GOLD node note is correct: the collapsed raw row lists
  `gold.ecosystem:5778|gold.ecosystem:5779`, while `seed_from_sources` emits
  only the first node as `source_id` and records the duplicate-node note.
