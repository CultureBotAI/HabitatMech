# YAML Record Review: Estuary: Microbial mat

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/aquatic/estuary_microbial_mat.yaml`
- Started UTC: 2026-10-02T05:30:00Z
- Finished UTC: 2026-10-02T05:36:21Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.57a5257707` |
| Label | `Estuary: Microbial mat` |
| File | `data/habitats/aquatic/estuary_microbial_mat.yaml` |
| Category | `AQUATIC` |
| Grounding | `NARROW` |
| Mapping | `REVIEWED` |
| Source | GOLD `gold.ecosystem:7714` |
| Source path | `Environmental > Aquatic > Marine > Intertidal zone > Estuary: Microbial mat` |
| Generated status | Generated from `data/raw/*` plus `curation/decisions.tsv`; `data/habitats/` is read-only generated output. |

The full generated YAML was read. The record has one GOLD source attestation,
one item-level `GROUND_AS_PARENT` history event, no definition, no synonyms, no
xrefs, no environmental parameters, no characteristic taxa, no claim-level
evidence, no causal graphs, no discussions, and no datasets.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/estuary_microbial_mat.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/estuary_microbial_mat.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus` | Passed; expected 3,206 records, found 3,206 on disk, 0 missing, 0 extra, 0 differing. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just worklist --status all --out /tmp/habitatmech-estuary-microbial-mat-worklist.tsv` | Passed; wrote 953 ungrounded worklist rows. The reviewed target is correctly absent because it has an item-level decision and `mapping_status: REVIEWED`. |
| `just report --out /tmp/habitatmech-estuary-microbial-mat-report.tsv` | Passed; the per-record row for `habitatmech:GOLD.57a5257707` reports `AQUATIC`, `NARROW`, `REVIEWED`, source `GOLD`, 1 source, 12 assertions, `has_definition=False`, 2 parents, 0 parameters, 0 taxa, and 0 causal graphs at `data/habitats/aquatic/estuary_microbial_mat.yaml`. |

`iModulonDB` was not applicable: the record names no gene, locus tag,
regulator, pathway, stress-response trait, or transcriptomics dataset.

## Identity and Grounding

The generated identifier, label, category, source attestation, and reviewed
`NARROW` grounding all trace to maintained inputs:

| Claim | Maintained input |
|---|---|
| Stable slug | `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.57a5257707` to `estuary_microbial_mat`. |
| GOLD source path | `data/raw/gold_ecosystem_paths.tsv` has one canonical path row for `Environmental > Aquatic > Marine > Intertidal zone > Estuary: Microbial mat`, leaf label `Estuary: Microbial mat`, source ID `gold.ecosystem:7714`, 1 GOLD ecosystem node, and 12 `ORGANISM` assertions. |
| Biosample support | `data/raw/gold_path_biosamples.tsv` has the exact path with node `7714` and 13 biosamples. |
| Maintained review | `curation/decisions.tsv` has an `ITEM`-depth `GROUND_AS_PARENT` row for `habitatmech:GOLD.57a5257707`, with `ENVO:00000045` `estuary` attached as a parent even though the row note says the estuary is the microbial mat's setting. |
| ENVO estuary context | `data/raw/ontology_terms.tsv` contains non-obsolete habitat term `ENVO:00000045`, label `estuary`, defined as a semi-enclosed coastal water body freely connected to the open sea. |
| GOLD source-path parent | `src/habitatmech/seed.py` adds a second-pass parent link from each GOLD path to its direct GOLD parent path; here `data/habitats/PATHS.tsv` maps the direct parent path `Environmental > Aquatic > Marine > Intertidal zone` to `habitatmech:GOLD.115edc36f8`. |

The current item-level row correctly avoids grounding an estuarine microbial
mat directly to `ENVO:00000045` `estuary`, and it correctly makes the generated
record `REVIEWED`. Its `GROUND_AS_PARENT` enum is still too strong: estuary is
setting context for this microbial mat, not an is-a parent.

The record is still mis-modeled in two ways:

- The vendored ENVO slice contains `ENVO:01000008` `microbial mat`, defined as
  a multi-layered sheet of micro-organisms. This record is a path-qualified
  estuarine microbial mat, but it has no `microbial mat` broader parent or
  authored definition under that genus; instead its parents are two settings.
- `habitatmech:GOLD.115edc36f8` is the GOLD `Environmental > Aquatic > Marine >
  Intertidal zone` source path. A microbial mat located in an intertidal
  estuary is not a subclass of an intertidal zone; that upstream containment
  context should not be emitted as a strict `parent_habitats` edge.

The rendered page
`pages/habitats/estuary-microbial-mat-habitatmech-gold-57a5257707.html`
mirrors the YAML: it shows the same GOLD attestation, the same two broader
habitats, no definition, no taxa, no parameters, no causal graph, and the same
single curation event.

## Evidence

| Claim | Evidence checked | Assessment |
|---|---|---|
| The record is the GOLD `Estuary: Microbial mat` concept. | `data/raw/gold_ecosystem_paths.tsv` has the exact canonical path, leaf label, source ID, node count, and 12 organism assertions. | Supported. |
| The 12-assertion source attestation matches the GOLD inventory. | The YAML copies the exact source, source ID, label, path, `assertion_count=12`, and `assertion_unit=ORGANISM` from `data/raw/gold_ecosystem_paths.tsv`. | Supported. |
| The source is estuarine and sampled as sediment in the committed GOLD metadata. | `data/raw/gold_path_triads.tsv` has broad `ENVO:01000020` `estuarine biome`, local `ENVO:00000045` `estuary`, and medium `ENVO:00002007` `sediment` triad rows for the exact path, each with 13 samples, 3 GOLD studies, 3 distinct terms in that slot, 0.54 share, and 1 supporting study. | Supported as weak contextual evidence; one independent study per slot is not enough to promote any triad term to identity. |
| `ENVO:00000045` `estuary` is a strict broader habitat. | `curation/decisions.tsv` item-reviewed the exact source concept as `GROUND_AS_PARENT` to `ENVO:00000045`, and the exact path and local triad also carry estuary context. | Unsupported as `parent_habitats`; an estuary is the setting of an estuarine microbial mat, not its genus. |
| The record should be modeled as a microbial-mat habitat. | The exact GOLD source label and path name `Microbial mat`, and `data/raw/ontology_terms.tsv` has a broader non-obsolete habitat term `ENVO:01000008` `microbial mat`. Existing item-level decisions attach that same parent to other path-qualified GOLD microbial-mat leaves to avoid conflating their settings while retaining the mat genus. | Not represented in the current record. |
| `habitatmech:GOLD.115edc36f8` is a strict broader habitat. | The edge is generated only from the direct GOLD source path `Environmental > Aquatic > Marine > Intertidal zone`; `data/habitats/aquatic/intertidal_zone__2f295854.yaml` is itself an unreviewed `NARROW`, `SEEDED` GOLD record. | Unsupported as `parent_habitats`; it is containment/source-path context rather than an is-a edge. |
| Empty optional sections are current. | Hidden/ignored-inclusive searches over maintained decisions, term requests, causal overlays, `history`, `research`, raw GOLD inventories, existing review reports, generated YAML, and rendered pages found no target-owned definition, xref, environmental parameter, characteristic taxon, causal overlay, discussion, dataset, research report, or history record. | Supported for the current maintained inputs. |

## Completeness

Consequential coverage:

- `data/raw/gold_ecosystem_paths.tsv`, `data/raw/gold_path_biosamples.tsv`,
  and `data/raw/gold_path_triads.tsv` all contain the exact GOLD path.
- The exact source concept has one item-level decision in
  `curation/decisions.tsv`, so the `REVIEWED` mapping status is intentional.
- Exact `find` over `reports/yaml_record_review` for
  `*estuary_microbial_mat*.md` found no prior exact report for this record.
- `find` over `research`, `history`, `curation/term_requests`, and
  `curation/causal_graphs` with `-iname '*estuary*'` found no target-specific
  evidence report, append-only curation history record, term request, or
  causal overlay.

The record is not complete enough to pass because the current curation models
estuary and intertidal-zone settings as parents while omitting the
microbial-mat genus that the GOLD label requires.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| HM-ESTUARY-MICROBIAL-MAT-001 | Major | The reviewed GOLD source concept lacks its microbial-mat genus and instead uses estuary as a false parent. | GOLD labels the exact source path `Estuary: Microbial mat`, and the vendored ENVO slice has `ENVO:01000008` `microbial mat`; however the generated record has no definition and attaches contextual `ENVO:00000045` `estuary` as a parent. An estuary is the setting of the mat, not a superclass of it. | Replace the `curation/decisions.tsv` row with an item-level `CONFIRM_UNGROUNDED` decision, then define `habitatmech:GOLD.57a5257707` under `ENVO:01000008` in `curation/term_requests.tsv`. |
| HM-ESTUARY-MICROBIAL-MAT-002 | Major | The inherited `Intertidal zone` parent is source-path containment, not a supported strict broader habitat. | `src/habitatmech/seed.py` links this record to the concept for GOLD's direct parent path `Environmental > Aquatic > Marine > Intertidal zone`; a microbial mat located in an intertidal estuary is not a kind of intertidal zone. | `curation/term_requests.tsv` can set `parent_mode=REPLACE` for the authored microbial-mat definition so the generated record keeps only the true `ENVO:01000008` genus. |
| HM-ESTUARY-MICROBIAL-MAT-003 | Minor | The curation note records a truncated GOLD path. | `curation/decisions.tsv` and the generated curation history end the source path with `Estuary: Microbia` instead of the exact `Estuary: Microbial mat`. The row still keys the right identifier and decision, so this is a provenance typo rather than a grounding error. | `curation/decisions.tsv`. |

No blockers were found.

## Recommended Edits

| Priority | Edit | Owner | Follow-up validator |
|---:|---|---|---|
| 1 | Replace the `GROUND_AS_PARENT` row for `habitatmech:GOLD.57a5257707` with `CONFIRM_UNGROUNDED`, because no vendored ontology term exactly names an estuary microbial mat and `ENVO:00000045` is contextual rather than broader. | `curation/decisions.tsv` | `just seed`, `just seed-canary habitatmech:GOLD.57a5257707`, and `just verify-corpus`. |
| 2 | Add an authored `estuary microbial mat` definition for `habitatmech:GOLD.57a5257707`, with `ENVO:01000008` `microbial mat` as the genus and `parent_mode=REPLACE` so generated source-path and setting parents are dropped. | `curation/term_requests.tsv` | `just seed`, `just seed-canary habitatmech:GOLD.57a5257707`, and `just term-requests-check`. |
| 3 | Correct the truncated source path in the replacement `habitatmech:GOLD.57a5257707` decision note and add append-only history for the future curation session. | `curation/decisions.tsv` and `history/` | `just validate-history`. |

## Follow-up Checks

After the future `CONFIRM_UNGROUNDED` decision and microbial-mat definition,
rerun:

- `just seed`
- `just seed-canary habitatmech:GOLD.57a5257707`
- `just validate data/habitats/aquatic/estuary_microbial_mat.yaml`
- `just validate-strict data/habitats/aquatic/estuary_microbial_mat.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus`
- `just render`
- `just report`

The repaired generated record should keep identifier
`habitatmech:GOLD.57a5257707`, become `UNGROUNDED` and `REVIEWED`, gain a
definition whose parent is `ENVO:01000008`, and drop both contextual parents:
`ENVO:00000045` estuary and the generated GOLD `Intertidal zone` record.

## Additional Notes

Ignored files were included in absence searches. Exact `find` and
`rg --no-ignore --hidden` searches covered the target identifier, slug, source
ID, and label across maintained curation inputs, `history`, `research`, raw GOLD
inventories, existing review reports, generated habitat YAML, rendered pages,
and source code. They found the expected `data/habitats/PATHS.tsv` row, the
exact `curation/decisions.tsv` row, exact GOLD inventory rows, a rendered page,
and one prior broad-estuary review that mentions this GOLD row only as a
narrower source concept.
