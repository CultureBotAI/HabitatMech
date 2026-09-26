# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/engineered/granular_sludge.yaml`
- Started UTC: `2026-09-26T16:07:39Z`
- Finished UTC: `2026-09-26T16:07:51Z`
- Verdict: needs curation

## Target

Reviewed the complete generated record at
`data/habitats/engineered/granular_sludge.yaml`.

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.c79068da29` |
| Label | `Granular sludge` |
| Category | `ENGINEERED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source concept | `gold.ecosystem:8150` |
| Source path | `Engineered > Bioreactor > UASB (Upflow anaerobic sludge blanket) > Sludge > Granular sludge` |
| Stable slug | `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.c79068da29` to `granular_sludge` |
| Maintained owner | The item-level review decision belongs in `curation/decisions.tsv`; a confirmed novel term definition and parent override would belong in `curation/term_requests.tsv`. |

This is the UASB-specific GOLD `Granular sludge` child of
`Engineered > Bioreactor > UASB (Upflow anaerobic sludge blanket) > Sludge`.
It is not the already reviewed same-label anaerobic child at
`data/habitats/engineered/granular_sludge__16dfa645.yaml`, and it is not the
GOLD `AGS (Aerobic granular sludge)` leaf reviewed in
`data/habitats/engineered/ags_aerobic_granular_sludge.yaml`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/engineered/granular_sludge.yaml` | Pass: LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/granular_sludge.yaml` | Pass: scanned 1 file with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| `just validate-causal curation/causal_graphs/granular_sludge.yaml` | Not applicable: exact ignored/hidden-inclusive searches found no target-specific causal-graph overlay. |
| `just validate-causal-all` | Pass: validated 32 causal-graph curation files with 32 graphs. |
| `just term-requests-check` | Pass: the generated term-request table is current with 109 terms. |
| `just validate-history` | Pass: 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Pass: expected and found 3,206 records, with 0 missing, 0 extra, and 0 differing files. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist.tsv` | Pass: wrote 953 total `UNGROUNDED` rows. This target is the next all-status row after the newly merged `Food sample` review. |
| `just report` | Pass: reported 3,206 records, 953 `UNGROUNDED`, 123 individually examined ENVO term-request records, and 830 class-level sweep rows. |
| `git diff --check` | Pass. |

## Identity and Grounding

The record's minted identifier, label, category, source identity, and stable
slug agree with the committed source inventory:

- `data/raw/gold_ecosystem_paths.tsv` has the exact path
  `Engineered > Bioreactor > UASB (Upflow anaerobic sludge blanket) > Sludge > Granular sludge`,
  leaf label `Granular sludge`, depth 5, one GOLD node, three organism
  assertions, no study assertions, no biosample assertions, no total
  side-table assertions, and node ID `gold.ecosystem:8150`.
- The generated `source_attestations` block preserves that source ID, source
  label, source path, `assertion_count: 3`, and `assertion_unit: ORGANISM`.
- `data/habitats/PATHS.tsv` pins `habitatmech:GOLD.c79068da29` to
  `granular_sludge`, matching the file under `data/habitats/engineered/`.

Grounding remains unresolved. `curation/decisions.tsv` has exactly one row for
`habitatmech:GOLD.c79068da29`, and it is the August 12 class-level
`CONFIRM_UNGROUNDED` sweep whose note explicitly says that whether the concept
is a habitat at all was not assessed. The vendored slice contains
`ENVO:00002212` `thermophilic granular sludge`, but that term over-specifies a
temperature condition not present in this GOLD UASB granular-sludge path.

The generated parent `habitatmech:GOLD.84c231bfef` is the immediate GOLD source
parent `Engineered > Bioreactor > UASB (Upflow anaerobic sludge blanket) >
Sludge`. That is strictly broader than the target leaf. The parent is itself a
seeded `NARROW` record whose own UASB parent has a pending review
recommendation to merge with `ENVO:00002213` `anaerobic sludge blanket reactor`,
but that does not make the direct edge from UASB granular sludge to UASB sludge
false.

## Evidence

| Claim | Evidence | Assessment |
|---|---|---|
| The target is the GOLD UASB granular-sludge leaf. | `data/raw/gold_ecosystem_paths.tsv` has the exact UASB path ending in `Granular sludge` at node `gold.ecosystem:8150`. | Supported. |
| The generated `assertion_count: 3` is a GOLD organism count. | The exact GOLD ecosystem-path row reports `organism_count=3` and no side-table `study`, `biosample`, or `total` assertions. | Supported. |
| The direct parent is source-path broader. | The target path's immediate prefix is `Engineered > Bioreactor > UASB (Upflow anaerobic sludge blanket) > Sludge`, generated as `habitatmech:GOLD.84c231bfef`. | Supported for this target. |
| `ENVO:00002212` is not an exact grounding target. | `data/raw/ontology_terms.tsv` labels `ENVO:00002212` as `thermophilic granular sludge`. The target path says only `Granular sludge` under a UASB sludge parent and does not claim a thermophilic temperature range. | Supported as a near miss to avoid. |
| Empty environmental parameters, characteristic taxa, record-level evidence, and causal graphs are generated correctly. | Exact ignored/hidden-inclusive searches found the target path only in `data/raw/gold_ecosystem_paths.tsv`, not in the GOLD biosample, study, or triad side tables, and no target-specific curated causal overlay exists. GOLD organism aggregates are source-volume counts, not characteristic-taxon evidence. | Supported. |

No literature-derived mechanism claim is present in the target record.

## Completeness

The record is structurally complete for a seeded, one-source GOLD leaf, but it
is not complete as a curated habitat. Its only curation decision is the
class-level sweep, it has no authored definition, and no ENVO term-request row
establishes the intended genus, parent mode, or reason this UASB granular sludge
should stay distinct from the same-label granular-sludge record under
`Engineered > Bioreactor > Anaerobic > Sludge`.

Exact ignored/hidden-inclusive searches covered `curation`, `data/raw`,
`data/habitats`, `history`, `research`, and
`reports/yaml_record_review`, excluding generated JSON semantic-map files and
the research manifest. They found the target-generated YAML, the path-lock row,
the class-level decision row, the exact GOLD inventory row, and prior mentions
in neighboring reviews. They found no target-specific term request, curated
causal overlay, history record, research report, or prior top-level
`*-granular_sludge.md` review report.

The target path has no generated child path in the committed GOLD side tables:
an ignored/hidden-inclusive exact search for
`Engineered > Bioreactor > UASB (Upflow anaerobic sludge blanket) > Sludge > Granular sludge >`
across `data/raw/gold_ecosystem_paths.tsv`,
`data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`,
`data/raw/gold_studies.tsv`, and `data/raw/environment_parameters.tsv` found no
rows.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | `Granular sludge` remains only class-swept, so HabitatMech has not item-reviewed whether this UASB child is a real reactor-sludge habitat, the same concept as another anaerobic granular-sludge source path, or a narrower novel term that needs an authored definition. | The only decision for `habitatmech:GOLD.c79068da29` has `review_depth: CLASS` and explicitly did not assess habitathood. `ENVO:00002212` names `thermophilic granular sludge`, which is not exact unless thermophily is part of the reviewed identity. The same-label `Engineered > Bioreactor > Anaerobic > Sludge > Granular sludge` record is a separate minted source concept and is not evidence that these two leaves are already interchangeable. | Add an item-level row for `habitatmech:GOLD.c79068da29` in `curation/decisions.tsv`; if the concept remains minted, add a supported definition in `curation/term_requests.tsv`. |

No blockers found.

No minor findings.

## Recommended Edits

1. Item-review `habitatmech:GOLD.c79068da29` in `curation/decisions.tsv`, using
   the full GOLD path
   `Engineered > Bioreactor > UASB (Upflow anaerobic sludge blanket) > Sludge > Granular sludge`
   rather than the leaf label alone.

2. During the item review, decide explicitly whether the concept denotes
   UASB-specific granular sludge, anaerobic granular sludge independent of
   reactor type, or a duplicate of another maintained granular-sludge concept.
   Do not ground it directly to `ENVO:00002212` unless inspected evidence shows
   that thermophily is part of the source concept.

3. If no exact external term fits, keep `habitatmech:GOLD.c79068da29` as the
   identity, add a `curation/term_requests.tsv` definition with a true broader
   material parent such as `ENVO:00002044` `sludge`, and select the parent mode
   that preserves only strictly broader generated parents.

## Follow-up Checks

| Follow-up | Proof |
|---|---|
| Verify the item-level decision | `rg --no-ignore --hidden -n '^habitatmech:GOLD\\.c79068da29\\b' curation/decisions.tsv` should show an `ITEM` row whose `decision` and target, if any, match the reviewed identity. |
| Verify any novel definition | `rg --no-ignore --hidden -n '^habitatmech:GOLD\\.c79068da29\\b' curation/term_requests.tsv` should show an evidence-backed definition only if the concept remains minted. |
| Regenerate the target | Run `just seed`, then `just seed-canary habitatmech:GOLD.c79068da29`, and inspect `data/habitats/engineered/granular_sludge.yaml` for the expected `grounding_status`, `mapping_status`, source attestation, parents, and curation history. |
| Keep the corpus reproducible | Run `just verify-corpus --max-diffs 1`, `just validate data/habitats/engineered/granular_sludge.yaml`, `just validate-strict data/habitats/engineered/granular_sludge.yaml`, `just validate-causal-all`, `just term-requests-check`, `just validate-history`, `just worklist --limit 0 --status all`, `just report`, and `git diff --check`. |

## Additional Notes

- Ignored files were included in all absence checks via `rg --no-ignore
  --hidden` or `find`.
- `reports/yaml_record_review/20260925T162902Z-granular_sludge__16dfa645.md`
  reviewed the same-label anaerobic child at
  `data/habitats/engineered/granular_sludge__16dfa645.yaml` and called the
  current UASB leaf a distinct future target. This report reviews that UASB
  leaf.
- `reports/yaml_record_review/20260924T145226Z-uasb_upflow_anaerobic_sludge_blanket.md`
  already separated the UASB reactor source path from this material child: the
  child's three organism assertions belong to granular sludge, not to the UASB
  bioreactor parent.
