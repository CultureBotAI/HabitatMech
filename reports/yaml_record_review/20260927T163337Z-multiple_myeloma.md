# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/host_associated/multiple_myeloma.yaml
- Started UTC: 2026-09-27T16:33:37Z
- Finished UTC: 2026-09-27T16:33:37Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Record path | `data/habitats/host_associated/multiple_myeloma.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.456120aa2d` |
| Label | `Multiple myeloma` |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and `curation/decisions.tsv`; do not hand-edit this YAML. |

The target is the generated HabitatMech record for the GOLD source path
`Host-associated > Mammals: Human > Malignant tumor > Myeloma > Multiple
myeloma`. `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.456120aa2d` to the
`multiple_myeloma` slug.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/multiple_myeloma.yaml` | Pass. `linkml-validate` found no issues for this record. |
| `just validate-strict data/habitats/host_associated/multiple_myeloma.yaml` | Pass. Strict closed-schema validation scanned 1 file with 0 files in error and 0 error rows. |
| `just validate-causal curation/causal_graphs/<overlay>.yaml` | Not applicable. Ignored-inclusive searches for `habitatmech:GOLD.456120aa2d`, `gold.ecosystem:6210`, the exact GOLD path, the slug, and the label found no causal-graph overlay for this record. |
| `just validate-causal-all` | Pass. All 32 causal-graph curation files and 32 graphs validated. |
| Reference validator | Not applicable. The record has no `evidence`, `datasets`, or `causal_graphs` references to validate. |
| `just term-requests-check` | Pass. The generated term-request table is current at 109 terms. |
| `just validate-history` | Pass. 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus` | Pass. 3,206 expected records were present with 0 missing, 0 extra, and 0 differing generated YAML files. |
| `just worklist --status all --out /tmp/habitatmech-worklist.tsv` | Pass. The worklist completed, wrote 953 ungrounded rows, and included this record as a GOLD-only class-swept row. |
| `just report --out /tmp/habitatmech-report.tsv` | Pass. The corpus report completed and included this record as `UNGROUNDED`, `SEEDED`, and sourced only from GOLD. |
| `git diff --check` | Pass after report creation. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| The generated record denotes GOLD `Multiple myeloma`, not an ontology term. | `data/raw/gold_ecosystem_paths.tsv` has one exact row for `Host-associated > Mammals: Human > Malignant tumor > Myeloma > Multiple myeloma`, leaf label `Multiple myeloma`, depth 5, one GOLD node ID, and `gold.ecosystem:6210`. The generated `source_attestations` entry repeats that source ID, label, and path. | Supported exactly. |
| `grounding_status: UNGROUNDED` reflects the class-level decision, not an item-level habitat judgment. | `curation/decisions.tsv` has a `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.456120aa2d`; its `review_depth` is `CLASS`, and the note explicitly says whether the concept is a habitat at all was not assessed. | Structurally supported, but wrong for a malignant-tumor disease label that has adjacent item-level `NOT_APPLICABLE` decisions. |
| `mapping_status: SEEDED` follows from the maintained curation depth. | HabitatMech class-level decisions do not promote records to `REVIEWED`; no item-level row exists for this exact GOLD source concept. | Supported. |
| The sole `parent_habitats` edge comes from GOLD's disease hierarchy. | `habitatmech:GOLD.e49a44bb6c` is the generated `Myeloma` source concept, itself seeded from `Host-associated > Mammals: Human > Malignant tumor > Myeloma` and still class-swept in `curation/decisions.tsv`. | Supported as GOLD hierarchy, but it is a cancer-type hierarchy rather than a strict hierarchy of microbial habitats. |
| The exact-path MIxS triads point at lab cell culture. | `data/raw/gold_path_triads.tsv` records one exact-path sample in one study using broad `ENVO:01000313` `anthropogenic environment`, local `ENVO:01001406` `laboratory facility`, and medium `ENVO:02000008` `cell culture`. | Supported as submitter-supplied context; the triads make `cell culture` the sampled medium, not `Multiple myeloma` a habitat identity. |

## Evidence

The record has no authored definition, evidence entries, environmental
parameters, characteristic taxa, datasets, or causal graphs.

| Assertion | Evidence | Assessment |
|---|---|---|
| GOLD has a direct multiple-myeloma ecosystem path. | The exact `data/raw/gold_ecosystem_paths.tsv` row stores `gold_node_count=1` and `gold.ecosystem:6210` for the exact path. | Supported exactly. |
| The exact GOLD path is represented in one GOLD study with eight biosamples. | `data/raw/gold_studies.tsv` lists `Gs0150275` across 16 paths including multiple cancer-type labels, blood, colon mucosa, and malignant ascites; `data/raw/gold_path_biosamples.tsv` lists 8 biosamples for path ID `6210`. | Supported exactly. |
| GOLD does not expose organism assertions directly on the grouping row. | The exact raw ecosystem-path row has `organism_count=0`, `study_count=0`, `biosample_count=0`, and `total_assertions=0`; the generated `source_attestations` row therefore has no assertion count. | Supported exactly. |
| The worklist candidates do not provide an exact habitat grounding. | `/tmp/habitatmech-worklist.tsv` lists nearby `BTO:0002101` `multiple myeloma cell` and `BTO:0000727` `multiple myeloma cell line`. `data/raw/ontology_terms.tsv` defines `BTO:0002101` as a malignant proliferation of plasma cells in bone marrow and gives `BTO:0000727` the label `multiple myeloma cell line`. | Supported as a near miss: these are cell or cell-line terms, not a microbial habitat identity. |
| The maintained class-level decision is reproduced in curation history. | The first generated curation event mirrors the `curation/decisions.tsv` row for `habitatmech:GOLD.456120aa2d`, including `CONFIRM_UNGROUNDED`, the `2026-08-12` curator/date, and the class-sweep note. | Supported exactly. |

No snippet or citation mismatch was present because this generated placeholder
record carries only source-inventory and curation-history facts.

## Completeness

This record is reproducible but should not remain a minted ungrounded habitat.
The exact GOLD path places `Multiple myeloma` under `Malignant tumor > Myeloma`,
the worklist's closest terms are BTO cell and cell-line classes, and the GOLD
MIxS triad summary says one annotated exact-path sample used a laboratory
facility as local context and cell culture as medium. Together, those inputs
identify a cancer or cell-line type used to organize cultured samples, not an
associated environment that needs a HabitatMech term request.

Item-level curation has already made that distinction for adjacent GOLD cancer
types: `Malignant tumor`, `Basal cell carcinoma`, `Colon cancer`, and
`Malignant tumor tissue` all have `NOT_APPLICABLE` `ITEM` decisions in
`curation/decisions.tsv`. `Multiple myeloma` still has only the class-level
lexical sweep row, so this generated record is in the class-swept ungrounded
worklist rather than the reviewed non-habitat bucket.

Ignored- and hidden-file-inclusive searches covered `data/raw`, `curation`,
`research`, `reports/yaml_record_review`, and `data/habitats` for the minted
identifier, GOLD node ID, exact GOLD path, slug, label, `Myeloma` parent, and
nearby BTO candidates. Before this report was written, a separate `find` check
of `reports/yaml_record_review`, `curation/causal_graphs`, and
`research/habitats` found no prior multiple-myeloma review report, causal
overlay, or research report.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `Multiple myeloma` should be item-reviewed as `NOT_APPLICABLE`, not retained as an `UNGROUNDED` habitat. | GOLD itself places the exact node under `Malignant tumor > Myeloma`; the exact-path MIxS rows describe one sample/study as `laboratory facility` plus `cell culture`; the worklist's BTO hits are multiple-myeloma cell or cell-line classes; and adjacent malignant-tumor disease nodes are already pulled out of the class-level sweep as `NOT_APPLICABLE` item decisions. | `curation/decisions.tsv` |

No blockers or minor findings were found.

## Recommended Edits

1. Replace the `habitatmech:GOLD.456120aa2d` row in
   `curation/decisions.tsv` with an item-depth `NOT_APPLICABLE` decision.
   Keep the reasoning specific to the GOLD path: `Multiple myeloma` is a
   malignant-tumor disease/cell-culture classifier, not the sampled habitat.
2. Do not add a `curation/term_requests.tsv` row for this concept. The exact
   GOLD path does not need a novel habitat term unless item review reframes a
   different maintained source concept as the actual cell-culture habitat.
3. Regenerate the target record from the maintained inputs instead of editing
   `data/habitats/host_associated/multiple_myeloma.yaml` directly.

## Follow-up Checks

| Check | Purpose |
|---|---|
| Manual GOLD/ontology candidate review | Confirm `Multiple myeloma` is not being conflated with its adjacent `cell culture` MIxS medium, with the BTO multiple-myeloma cell/cell-line candidates, or with a tumor-tissue habitat. |
| `just seed` | Preview the regenerated corpus from the edited maintained inputs. |
| `just seed-canary habitatmech:GOLD.456120aa2d` | Confirm the one generated target carries the new item-depth `NOT_APPLICABLE` decision and history expected from `curation/decisions.tsv`. |
| `just seed-apply --force` | Rebuild generated YAML after inspecting the canary output. |
| `just validate data/habitats/host_associated/multiple_myeloma.yaml` | Check the regenerated target against the LinkML `HabitatRecord` schema. |
| `just validate-strict data/habitats/host_associated/multiple_myeloma.yaml` | Check the regenerated target under the closed-schema validator. |
| `just validate-history` | Confirm the append-only history record for the curation session is valid. |
| `just verify-corpus` | Prove generated `data/habitats/` still reproduces from `data/raw/` and curation inputs. |
| `just report` | Confirm the record moves out of the class-level sweep bucket after item review. |
| `git diff --check` | Catch whitespace errors in the maintained and generated diffs. |

## Additional Notes

- The absence checks in this review used `rg --no-ignore --hidden` and `find`,
  so ignored and hidden files were included.
- `ENVO:02000008` `cell culture` is a medium-slot MIxS term for the exact GOLD
  path's one triad-annotated sample. It is not evidence that GOLD's `Multiple
  myeloma` label names an exact cell-culture habitat.
- `BTO:0002101` and `BTO:0000727` are useful near misses for item review
  because they confirm the biomedical sense of the GOLD leaf label, but a BTO
  cell type or cell-line class is not an environment identity.
