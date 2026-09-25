# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/settled_granule.yaml
- Started UTC: 2026-09-25T16:13:56Z
- Finished UTC: 2026-09-25T16:13:56Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.821fc6dd72` |
| Label | `Settled granule` |
| Category | `ENGINEERED` |
| Source path | `Engineered > Bioreactor > Anaerobic > Settled granule` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`; the current class-level decision lives in `curation/decisions.tsv`. Future item review belongs in `curation/decisions.tsv`, and any retained minted definition or parent replacement belongs in `curation/term_requests.tsv`, not in `data/habitats/engineered/settled_granule.yaml`. |

The generated record is GOLD-only and minted as a novel class because no
vendored ontology term fits the leaf label. It has `grounding_status:
UNGROUNDED`, `mapping_status: SEEDED`, a single generated parent,
`ENVO:00002124` `anaerobic bioreactor`, and one GOLD source attestation for
`gold.ecosystem:5607`.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/habitats/engineered/settled_granule.yaml` | Pass: LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/settled_granule.yaml` | Pass: scanned 1 file with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| `just validate-causal curation/causal_graphs/<overlay>.yaml` | Not applicable: the target has no `causal_graphs` block, and gitignore-independent exact searches for `habitatmech:GOLD.821fc6dd72`, `gold.ecosystem:5607`, `gold.ecosystem:5608`, `settled_granule`, and `Settled granule` under `curation/causal_graphs`, `history`, `research`, `reports/yaml_record_review`, and `conf` found no curated overlay or dedicated history record for this target. |
| `just validate-causal-all` | Pass: validated 32 causal-graph curation files with 32 graphs. |
| `just term-requests-check` | Pass: the term-request table is current with 109 terms. |
| `just validate-history` | Pass: 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Pass: expected 3,206 records, found 3,206 on disk, and the corpus reproduces exactly from `data/raw/`. |
| `just worklist --limit 2000 --status all --out /tmp/habitatmech-settled-granule-worklist.tsv` | Pass: reported 953 ungrounded records, 1,810 decisions on file, and wrote 953 rows to `/tmp/habitatmech-settled-granule-worklist.tsv`. |
| `just report` | Pass: completed the corpus report for 3,206 records. |
| `git diff --check` | Pass. |
| Reference validator | Not applicable: this record has no record-level `evidence`, `characteristic_taxa`, `causal_graphs`, `discussions`, or `datasets` with citation-bearing `EvidenceItem` references. |

## Identity and Grounding

The generated identifier, label, category, slug, source attestation, and
curation history agree with the maintained inputs. `data/raw/gold_ecosystem_paths.tsv`
has the exact `Engineered > Bioreactor > Anaerobic > Settled granule` row with
`gold_node_ids=gold.ecosystem:5607|gold.ecosystem:5608`,
`gold_node_count=2`, and zero direct organism, study, biosample, or total
assertions in the bulk ecosystem-path inventory. `data/habitats/PATHS.tsv` maps
`habitatmech:GOLD.821fc6dd72` to the stable `settled_granule` slug.

The existing `curation/decisions.tsv` row for
`habitatmech:GOLD.821fc6dd72` is a `CLASS`-level
`CONFIRM_UNGROUNDED` decision. That class sweep supports only the lexical claim
that no term in the vendored slice matched this label by any search route; its
own decision note explicitly says whether the concept is a habitat at all was
not assessed. The generated `UNGROUNDED` status is therefore defensible as a
seeded provisional state, but this record still needs an item-level review
before it can become a real term-request candidate.

The generated `ENVO:00002124` `anaerobic bioreactor` parent is strict for the
immediate source parent, `Engineered > Bioreactor > Anaerobic`, which has an
item-level exact `GROUND` decision to `ENVO:00002124`. The raw source path does
not, however, prove that a settled granule is a subtype of the reactor itself;
the leaf likely names a settled granular sludge aggregate or sampled material
within an anaerobic bioreactor context.

## Evidence

The GOLD source attestation traces to `data/raw/gold_ecosystem_paths.tsv`: the
generated `source_id: gold.ecosystem:5607`, `source_label: Settled granule`,
and `source_path: Engineered > Bioreactor > Anaerobic > Settled granule` match
the canonical row. `gold.ecosystem:5608` is the second collapsed GOLD node ID
for the same path.

The GOLD API side tables provide weak but target-specific occurrence context
that is not reflected in the generated `source_attestations` counts:
`data/raw/gold_studies.tsv` has one study, `Gs0151903`, whose only path is
`Engineered > Bioreactor > Anaerobic > Settled granule`, and
`data/raw/gold_path_biosamples.tsv` has two biosamples for numeric GOLD path ID
`5608`. A gitignore-independent exact search for the source path across
`data/raw/gold_path_triads.tsv` and `data/raw/environment_parameters.tsv` found
no MIxS triad or environmental-parameter rows for this concept, so those
biosamples do not settle the best ontology genus or the strictness of the
generated parent edge.

The generated `ENVO:00002124` parent traces to GOLD's source-tree context, not
to any settled-granule-specific decision or evidence overlay. The target has no
record-level evidence, causal graph, environmental parameters, or taxon block
to review.

## Completeness

- Gitignore-independent exact searches for `habitatmech:GOLD.821fc6dd72`, `gold.ecosystem:5607`, `gold.ecosystem:5608`, `settled_granule`, and `Settled granule` across `curation`, `history`, `research`, `reports/yaml_record_review`, `data/habitats`, `data/raw`, and `conf` found the generated target, `PATHS.tsv`, the class-level `curation/decisions.tsv` row, the canonical GOLD row, the two GOLD API side-table rows, and no item-level decision, term request, causal overlay, dedicated history record, research report, or prior YAML-record review for this target.
- A gitignore-independent case-insensitive search for `settled|granule` across `data/raw/ontology_terms.tsv`, `curation/term_requests.tsv`, `curation/term_requests_excluded.tsv`, `reports/yaml_record_review`, and `data/habitats/engineered` found no exact ontology term, curated definition, or existing review for `Settled granule`; ontology hits were unrelated sand, silt, snow, plastic, cellular, and anatomical granules.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*settled_granule*' -print` found no prior review report for this record stem; `find` includes ignored files.
- Optional `definition`, `environmental_parameters`, `characteristic_taxa`, `evidence`, `causal_graphs`, `discussions`, and `datasets` are absent. Their absence matches the current class-level-only state, but an item-level review that confirms a real habitat should add an authored definition.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | `habitatmech:GOLD.821fc6dd72` has only a class-level `CONFIRM_UNGROUNDED` decision and still has no item-level habitat assessment. | `curation/decisions.tsv` has `review_depth: CLASS` for this source concept, and the generated record remains `mapping_status: SEEDED`. The class-level decision note says no vendored term matched by any search route and explicitly says whether the concept is a habitat at all was not assessed. Exact ignored/hidden-inclusive searches found no target-specific term request, research report, causal overlay, history record, or prior review report. | `curation/decisions.tsv`; if the minted identity is retained, `curation/term_requests.tsv`. |
| Major | The generated `ENVO:00002124` `anaerobic bioreactor` parent is likely contextual rather than a strict broader habitat for `Settled granule`. | The exact source path says this child is `Settled granule` nested under `Engineered > Bioreactor > Anaerobic`; the existing item-level decision for the immediate parent supports `ENVO:00002124` as that parent path's identity, but neither `curation/decisions.tsv`, `curation/term_requests.tsv`, nor the GOLD side tables show that a settled granule aggregate is itself a kind of anaerobic bioreactor. | `curation/term_requests.tsv`, after an item-level decision confirms the target remains a real minted habitat. |

No blocker findings found.

No minor findings found.

## Recommended Edits

1. Replace the `CLASS` row for `habitatmech:GOLD.821fc6dd72` in `curation/decisions.tsv` with an `ITEM`-level decision that records the inspected `Engineered > Bioreactor > Anaerobic > Settled granule` path and either confirms the concept as ungrounded or marks it not applicable if the source proves to name a sample-processing state rather than a habitat or material.
2. If item review keeps this as a real ungrounded material habitat, add a `curation/term_requests.tsv` definition with a strict material or sludge genus and use `parent_mode: REPLACE` if the review confirms that `ENVO:00002124` is contextual.
3. Regenerate `data/habitats/engineered/settled_granule.yaml` through the seeder and inspect the generated diff rather than editing the generated YAML directly.

## Follow-up Checks

| Edit | Proof |
| --- | --- |
| Record item-level status for `habitatmech:GOLD.821fc6dd72` | `just seed-canary habitatmech:GOLD.821fc6dd72 --force`, followed by inspection of `data/habitats/engineered/settled_granule.yaml` showing an item-level curation-history event and `mapping_status: REVIEWED` if every contributing source concept has item-level review. |
| Replace the contextual `ENVO:00002124` parent if needed | The canary-generated `parent_habitats` list contains the authored material genus and omits `ENVO:00002124` when the term request uses `parent_mode: REPLACE`. |
| Preserve corpus reproduction | `just seed-apply --force` and `just verify-corpus --max-diffs 1`. |
| Validate the focused record and maintained inputs | `just validate data/habitats/engineered/settled_granule.yaml`, `just validate-strict data/habitats/engineered/settled_granule.yaml`, `just term-requests-check`, `just validate-history`, and `git diff --check`. |

## Additional Notes

- The neighboring GOLD child `Engineered > Bioreactor > Anaerobic > Sludge > Granular sludge` remains a separate minted record, `data/habitats/engineered/granular_sludge__16dfa645.yaml`. Its name is suggestive context for the material nature of `Settled granule`, but it does not by itself ground or define this target.
- Nearby reviews for `Biofilm`, `Digestate`, `Inoculum`, `Leachate`, and `Manure` under `Engineered > Bioreactor > Anaerobic` found the same source-tree pattern: the immediate anaerobic-bioreactor context is reviewed, but material or biofilm leaves under it can still inherit `ENVO:00002124` as a false `is-a` parent until they receive item-level definitions.
