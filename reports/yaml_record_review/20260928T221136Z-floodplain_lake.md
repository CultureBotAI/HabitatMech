# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/aquatic/floodplain_lake.yaml`
- Started UTC: 2026-09-28T22:11:36Z
- Finished UTC: 2026-09-28T22:11:36Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| File | `data/habitats/aquatic/floodplain_lake.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.93f4cea4a4` |
| Label | `Floodplain lake` |
| Category | `AQUATIC` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |
| Maintained/generated | Generated from `data/raw/`, `curation/decisions.tsv`, and `data/habitats/PATHS.tsv` |

The complete generated YAML record was read. It is the GOLD-only source
concept for `Environmental > Aquatic > Freshwater > Floodplain lake`, has one
generated GOLD source attestation, inherits `ENVO:00002011` `fresh water` as
its only parent, and has no definition, synonyms, xrefs, characteristic taxa,
environmental parameters, causal graph, discussions, datasets, or
claim-specific literature evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/floodplain_lake.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/floodplain_lake.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| Focused causal overlay check | Not applicable; exact hidden/ignored-inclusive searches found no `curation/causal_graphs` overlay for the Floodplain lake identifier, slug, label, or source path. |
| Reference validator | Not applicable; this generated GOLD-only record has no `evidence` items, environmental-parameter references, causal edges, discussions, or datasets. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus` | Passed; 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just report --out /tmp/habitatmech-floodplain-lake-report.tsv` | Passed; exact row `habitatmech:GOLD.93f4cea4a4` / `Floodplain lake` remains `UNGROUNDED`, `SEEDED`, GOLD-only, and assertion-free in generated source attestations. |

No documented validator was skipped. These checks prove that the YAML is valid,
the causal overlays and history files are valid, the term-request product is
current, and `data/habitats/` reproduces from maintained inputs. They do not
prove that each generated `parent_habitats` edge is semantically strict.

## Identity and Grounding

The record identity is stable and source-supported:

| Raw source | Floodplain lake evidence |
|---|---|
| `data/raw/gold_ecosystem_paths.tsv` | The exact canonical path is `Environmental > Aquatic > Freshwater > Floodplain lake`; its leaf label is `Floodplain lake`; two GOLD ecosystem node IDs collapse to the path: `gold.ecosystem:6980` and `gold.ecosystem:6981`. |
| `data/raw/gold_studies.tsv` | Study `Gs0154659` names the exact Floodplain lake path as its only GOLD path. |
| `data/raw/gold_path_biosamples.tsv` | Ecosystem path id `6981` reports 106 biosamples for the exact Floodplain lake path. |

The current `UNGROUNDED` status follows only from the class-level
`CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.93f4cea4a4` in
`curation/decisions.tsv`. That row proves that the 2026-08-12 lexical sweep
found no term in the vendored slice; it explicitly says the concept itself was
not assessed as a habitat and therefore is not an item-level signoff.

The local ontology slice confirms the closest relationship:

| Candidate | Local evidence | Assessment |
|---|---|---|
| `ENVO:00000021` `freshwater lake` | `data/raw/ontology_terms.tsv` defines it as a lake whose water contains low salt concentrations; the existing reviewed record is `data/habitats/aquatic/freshwater_lake.yaml`. | Broader than a floodplain lake and a better maintained parent than inherited `fresh water`. |
| `ENVO:01000617` `lentic water body` | `data/raw/ontology_terms.tsv` defines it as a low-flow accumulated water body; the existing reviewed record is `data/habitats/aquatic/lentic_water_body.yaml`. | Also broader, but less specific than `freshwater lake`. |
| `ENVO:00002011` `fresh water` | The vendored definition is the water material with low dissolved solute concentration. | Contextual material, not a strict parent of a lake. |
| `ENVO:00000255` `flood plain` | The vendored definition is a periodically flooded land area. | Related setting only; a floodplain lake is not a flood plain. |

The generated Floodplain lake record should remain minted unless a future OBO
term is added for this exact class. An item-level review should instead keep
the source concept `UNGROUNDED`, add an authored definition whose maintained
genus is `ENVO:00000021` `freshwater lake`, and replace the false inherited
`ENVO:00002011` parent.

## Evidence

| Generated claim | Nearest source | Assessment |
|---|---|---|
| `source_id: gold.ecosystem:6980` plus the duplicate-node note | `data/raw/gold_ecosystem_paths.tsv` lists `gold.ecosystem:6980|gold.ecosystem:6981` for the exact canonical path. | Supported; the generated source ID is the first collapsed GOLD ecosystem node. |
| `source_label: Floodplain lake` | `data/raw/gold_ecosystem_paths.tsv` has leaf label `Floodplain lake`. | Supported. |
| `source_path: Environmental > Aquatic > Freshwater > Floodplain lake` | `data/raw/gold_ecosystem_paths.tsv` has this exact canonical path. | Supported. |
| Absence of `assertion_count` | The committed `gold_ecosystem_paths.tsv` aggregate has zero organism, study, biosample, and total assertions for the exact canonical path. | Supported for the generated source-attestation model. |
| `parent_habitats: ENVO:00002011` | This is inherited from GOLD's `Environmental > Aquatic > Freshwater` path segment. | Over-scoped: `ENVO:00002011` is the material `fresh water`, not a water-body class or lake genus. |

The auxiliary GOLD API files add context but no generated record fields:
`data/raw/gold_studies.tsv` has one exact Floodplain lake study, and
`data/raw/gold_path_biosamples.tsv` reports 106 biosamples for ecosystem path
id `6981`. Exact hidden/ignored-inclusive searches found no matching
`data/raw/gold_path_triads.tsv` rows, so there are no MIxS broad/local/medium
terms to audit for this source path.

The generated record has no record-level references, no characteristic-taxon
claims, no environmental-parameter claims, no causal edges, and no discussions
or datasets.

## Completeness

The record is syntactically complete but semantically under-reviewed. The
source concept is a real aquatic habitat, no exact vendored term names a
`Floodplain lake`, and the inherited `fresh water` parent should be replaced
with a curator-authored `freshwater lake` genus before the record can become a
reviewed ENVO term request.

Hidden/ignored-inclusive exact searches covered the repository for
`habitatmech:GOLD.93f4cea4a4`, `Floodplain lake`, and `floodplain_lake`; they
found generated text-map and page products, `data/habitats/PATHS.tsv`, the
generated target, the generated Floodplain lake `Sediment` child, the
class-level row in `curation/decisions.tsv`, and the raw GOLD rows listed
above. They found no existing `reports/yaml_record_review` report, no
item-level decision, no term request, no history record, no research report,
and no causal overlay for this source concept.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `Floodplain lake` remains `SEEDED` after only a class-level `CONFIRM_UNGROUNDED` decision. The local slice lacks an exact term, but `ENVO:00000021` `freshwater lake` is the right broader genus to evaluate and record at item depth. | `curation/decisions.tsv` has only a `CLASS` row for `habitatmech:GOLD.93f4cea4a4`; `data/raw/ontology_terms.tsv` contains `freshwater lake` and no exact `floodplain lake` term. | `curation/decisions.tsv`; `curation/term_requests.tsv` |
| Major | The generated `parent_habitats` edge to `ENVO:00002011` asserts that a floodplain lake is a kind of `fresh water`, but the GOLD concept denotes a lake context. | The GOLD path leaf is `Floodplain lake`; `ENVO:00002011` is defined as a water material; `ENVO:00000021` is the available lake parent. | `curation/term_requests.tsv` |

## Recommended Edits

1. Replace the class-level `curation/decisions.tsv` row for
   `habitatmech:GOLD.93f4cea4a4` with an item-level
   `CONFIRM_UNGROUNDED` decision that records no exact local term exists for
   GOLD's `Environmental > Aquatic > Freshwater > Floodplain lake`.
2. Add `habitatmech:GOLD.93f4cea4a4` to `curation/term_requests.tsv` with a
   Floodplain lake definition, `ENVO:00000021` `freshwater lake` as
   `parent_class`, and `parent_mode=REPLACE` so the generated record drops
   the inherited `ENVO:00002011` material parent.
3. After regeneration, inspect the generated
   `data/habitats/aquatic/sediment__74d34b20.yaml` child because it currently
   uses `habitatmech:GOLD.93f4cea4a4` as its GOLD source-path parent.

## Follow-up Checks

- `just seed`
- `just seed-canary habitatmech:GOLD.93f4cea4a4`
- Inspect `data/habitats/aquatic/floodplain_lake.yaml` and confirm it has an
  authored definition, `grounding_status: UNGROUNDED`,
  `mapping_status: REVIEWED`, `ENVO:00000021` as its parent, and no
  `ENVO:00002011` parent.
- Inspect `data/habitats/aquatic/sediment__74d34b20.yaml` for a retained
  Floodplain lake parent.
- `just seed-apply --force`
- `just term-requests-check`
- `just validate data/habitats/aquatic/floodplain_lake.yaml`
- `just validate-strict data/habitats/aquatic/floodplain_lake.yaml`
- `just validate-causal-all`
- `just validate-history`
- `just verify-corpus`
- `just report`
- `git diff --check`

## Additional Notes

`data/habitats/aquatic/sediment__74d34b20.yaml` is the generated zero-assertion
child for `Environmental > Aquatic > Freshwater > Floodplain lake > Sediment`.

No blocker finding was found: the current generated YAML validates, the source
attestation is faithful to `data/raw/gold_ecosystem_paths.tsv`, and the source
concept denotes a real habitat rather than a disease, quality, process,
procedure, or whole-host taxon.

No minor findings were found.
