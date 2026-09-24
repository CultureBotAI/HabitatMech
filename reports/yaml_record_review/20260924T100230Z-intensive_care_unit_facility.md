# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/intensive_care_unit_facility.yaml
- Started UTC: 2026-09-24T10:02:30Z
- Finished UTC: 2026-09-24T10:02:30Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `HabitatRecord` |
| Identifier | `ENVO:03501152` |
| Label | `intensive care unit facility` |
| Category | `ENGINEERED` |
| Source concept | `habitatmech:GOLD.570ad87007` |
| Source path | `Engineered > Built environment > Hospital > ICU` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv` plus `curation/decisions.tsv`; do not hand-edit `data/habitats/engineered/intensive_care_unit_facility.yaml`. |

The generated record resolves GOLD's `ICU` leaf to ENVO's `intensive care unit facility` through the ENVO synonym `ICU`. The GOLD canonical path row collapses two zero-assertion upstream nodes, `gold.ecosystem:5573` and `gold.ecosystem:8248`, and the record correctly shows the first node with the "2 GOLD ecosystem node ids share this path" note.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/habitats/engineered/intensive_care_unit_facility.yaml` | Pass: LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/intensive_care_unit_facility.yaml` | Pass: scanned 1 file with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| `just validate-causal curation/causal_graphs/<overlay>.yaml` | Not applicable: a gitignore-independent `find curation/causal_graphs -type f -name '*intensive*' -print` search found no candidate overlay, and the target record has no `causal_graphs` block. |
| `just validate-causal-all` | Pass: validated 32 causal-graph curation files with 32 graphs. |
| `just term-requests-check` | Pass: the term-request table is current with 109 terms. |
| `just validate-history` | Pass: 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Pass: expected 3,206 records, found 3,206 on disk, and the corpus reproduces exactly from `data/raw/`. |
| `just worklist --limit 2000` | Pass: reported 0 undecided ungrounded records and 1,810 decisions on file. |
| `just report` | Pass: completed the corpus report for 3,206 records. |
| `git diff --check` | Pass. |
| Reference validator | Not applicable: this record has no record-level `evidence`, `characteristic_taxa`, `causal_graphs`, `discussions`, or `datasets` with citation-bearing `EvidenceItem` references. |

## Identity and Grounding

`ENVO:03501152` is present in `data/raw/ontology_terms.tsv` as `intensive care unit facility`, with the record's ENVO definition and the exact synonyms `ICU`, `ICW`, `ITU`, `critical care unit`, `critical care ward`, `intensive care ward`, `intensive therapy unit`, `intensive treatment unit`, and `intensive treatment ward`.

The sole GOLD source path is `Engineered > Built environment > Hospital > ICU`, and its `ICU` leaf denotes the same hospital unit facility as the ENVO synonym rather than one of ENVO's narrower specialty ICU terms, the ICU room term, or the mobile ICU ambulance term. The item-level `REVIEW` row in `curation/decisions.tsv` correctly endorses the synonym-based generated match for `habitatmech:GOLD.570ad87007`; because this is the only contributing source concept, `mapping_status: REVIEWED` is consistent.

The ontology-derived parent `ENVO:03501137` is supported: `data/raw/ontology_subclass_edges.tsv` asserts `ENVO:03501152 rdfs:subClassOf ENVO:03501137`, and `ENVO:03501137` is the `hospital unit facility` class. The source-derived parent `ENVO:00002173` is not supported as an `is-a` parent; see the major finding below.

## Evidence

No record-level literature evidence is present or required for this seeded ontology/GOLD record. The ENVO-sourced definition, label, and synonyms all trace to `data/raw/ontology_terms.tsv`; the GOLD source attestation traces to the row for `Engineered > Built environment > Hospital > ICU` in `data/raw/gold_ecosystem_paths.tsv`.

The attestation omits `assertion_count` and `assertion_unit` because the raw GOLD path has `organism_count=0`, `study_count=0`, `biosample_count=0`, and `total_assertions=0`; it is preserving a source vocabulary node rather than claiming any associated organism, study, or biosample evidence.

## Completeness

- A gitignore-independent exact search for `ENVO:03501152`, `intensive_care_unit_facility`, `habitatmech:GOLD.570ad87007`, and `gold.ecosystem:5573` across `data/habitats/PATHS.tsv`, `data/raw`, and `curation` found the expected path lockfile row, ontology term and subclass rows, one GOLD path row, and one item-level curation decision.
- A gitignore-independent exact label search for `intensive care unit facility`, `critical care ward`, `intensive care ward`, and `ICU` across non-JSON `data/raw` and `curation` files found ENVO's target term, nearby ICU sibling terms, GOLD's parent and child `ICU` paths, and one GOLD ICU triad on the child floor path. It did not find another maintained input contributing to this exact record.
- `find curation/causal_graphs history research -type f -name '*intensive*' -print` found no causal overlay, session history, or paid research report matching this record stem; `find` covered ignored and hidden files.
- Optional `environmental_parameters`, `characteristic_taxa`, `evidence`, `causal_graphs`, `discussions`, and `datasets` are correctly absent from the generated record. GOLD has no assertions on this path, and no curated overlay adds claim-level mechanism evidence.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | `parent_habitats` contains `ENVO:00002173` `hospital`, but an intensive care unit facility is part of a hospital, not a kind of hospital. | ENVO asserts `ENVO:00002173 hospital` and `ENVO:03501137 hospital unit facility` as sibling children of `ENVO:03501134 healthcare facility`; ENVO separately asserts `ENVO:03501152 intensive care unit facility rdfs:subClassOf ENVO:03501137`. The ICU record therefore should inherit the hospital-unit parent, but promoting the GOLD path parent `Hospital` adds a false `is-a` edge. The analogous `curation/term_requests.tsv` rows that use `parent_mode=REPLACE` already document the same pattern for source parents that are containment or context rather than broader classes, for example subway environments located within cities. | This needs a curator-owned way to suppress or replace false source-path parents for ontology-grounded GOLD records. The current generated value comes from `src/habitatmech/seed.py` applying GOLD path parents; the new maintained input should not be `data/habitats/engineered/intensive_care_unit_facility.yaml`. |

No blocker findings found.

No minor findings found.

## Recommended Edits

1. Add a maintained parent-suppression or parent-override input for ontology-grounded GOLD records and use it to drop `ENVO:00002173` from `ENVO:03501152`. The row should name `habitatmech:GOLD.570ad87007`, the rejected parent `ENVO:00002173`, and a note that GOLD's `Hospital > ICU` edge is locative/contextual while the ENVO definition places ICU facilities under `hospital unit facility`.
2. Update `src/habitatmech/seed.py` to apply that maintained override when promoting a GOLD source path parent into `parent_habitats`, and cover the ICU case with a regression test that rejects `hospital` while preserving `hospital unit facility`.
3. Rerun the GOLD canary for `ENVO:03501152`, inspect the regenerated record, and then apply the full seed so generated record and site artifacts remain reproducible.

## Follow-up Checks

| Edit | Proof |
| --- | --- |
| Drop the false source-path `hospital` parent | `just seed-canary ENVO:03501152`, followed by an inspection of `data/habitats/engineered/intensive_care_unit_facility.yaml` showing `ENVO:03501137` in `parent_habitats` and no `ENVO:00002173`. |
| Preserve corpus reproduction | `just seed-apply --force` and `just verify-corpus --max-diffs 1`. |
| Validate the focused record and curated override | `just validate data/habitats/engineered/intensive_care_unit_facility.yaml`, `just validate-strict data/habitats/engineered/intensive_care_unit_facility.yaml`, and the new parent-override validator or regression test added with the maintained input. |
| Confirm no unrelated history loss or term-request drift | `just term-requests-check`, `just validate-history`, and `git diff --check`. |

## Additional Notes

- The only raw ICU path with assertions is the child `Engineered > Built environment > Hospital > ICU > Floor` row; the reviewed parent ICU path has zero GOLD assertions. The child row is about `building floor` as `env_medium` and does not add an environmental parameter or causal mechanism to the parent ICU facility record.
- No source exact-match conflict was found. The only exact top-level report search before this write, `find reports/yaml_record_review -maxdepth 1 -type f -name '*-intensive_care_unit_facility.md' -print`, returned no existing report and included ignored files.
