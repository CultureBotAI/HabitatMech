# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/thiocyanate_remediating.yaml
- Started UTC: 2026-09-24T15:38:15Z
- Finished UTC: 2026-09-24T15:38:15Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.7a8691bc23` |
| Label | `Thiocyanate-remediating` |
| Category | `ENGINEERED` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |
| Source concept | GOLD `Engineered > Bioreactor > Thiocyanate-remediating` |
| Maintained inputs | `data/raw/gold_ecosystem_paths.tsv`; `curation/decisions.tsv` |
| Generated record | Yes; `just verify-corpus --max-diffs 1` reproduced all 3206 generated records byte-for-byte from maintained inputs. |

The target is the depth-3 GOLD thiocyanate-remediating bioreactor branch, not its `Anaerobic-Aerobic` child and not the sibling `Engineered > Bioremediation > Thiocyanate` branch.

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-thiocyanate_remediating.md' -print` | Pass: no pre-existing report for this stem; `find` included ignored files under the searched directory. |
| `just validate data/habitats/engineered/thiocyanate_remediating.yaml` | Pass: no LinkML issues found. |
| `just validate-strict data/habitats/engineered/thiocyanate_remediating.yaml` | Pass: one file scanned; zero closed-schema errors. |
| `just validate-causal-all` | Pass: 32 causal-graph curation files with 32 graphs validated. |
| `just validate-causal <overlay>` | Not applicable: an ignored-inclusive `rg --no-ignore --hidden` search found no overlay for `habitatmech:GOLD.7a8691bc23` under `curation/causal_graphs/`. |
| Reference validator | Not applicable: this YAML has no `evidence` entries and no causal overlay references. |
| `just term-requests-check` | Pass: `curation/term_requests.tsv` is current. |
| `just validate-history` | Pass: 77 history records valid. |
| `just verify-corpus --max-diffs 1` | Pass: all 3206 generated records on disk match `data/raw/` and curation inputs. |
| `just worklist --limit 2000` | Pass: 0 ungrounded records still undecided; 1810 decisions on file. |
| `just report` | Pass: corpus report completed. |
| `git diff --check` | Pass. |

## Identity and Grounding

`data/raw/gold_ecosystem_paths.tsv:1220` is the maintained GOLD row for `Engineered > Bioreactor > Thiocyanate-remediating`. It has leaf label `Thiocyanate-remediating`, depth `3`, one GOLD node ID, zero direct organism/study/biosample assertions, and node ID `gold.ecosystem:7780`. `data/habitats/PATHS.tsv:2187` maps `habitatmech:GOLD.7a8691bc23` to the reviewed `thiocyanate_remediating` slug.

The generated source attestation mirrors that path and records `gold.ecosystem:7780`. The only generated parent is `ENVO:00002123` `bioreactor`, which is supported by the parent GOLD path `Engineered > Bioreactor`, `data/raw/gold_ecosystem_paths.tsv:60`, and the vendored `bioreactor` ontology row in `data/raw/ontology_terms.tsv:7219`.

The `UNGROUNDED` status traces to `curation/decisions.tsv:725`, but that row has `review_depth=CLASS`. Its note says the class-level sweep found no vendored-slice term by lexical search route and explicitly says whether the concept is a habitat was not assessed.

## Evidence

Supported by maintained inputs:

- The minted identifier, label, category, GOLD source path, and seeded class-level curation history all follow from `data/raw/gold_ecosystem_paths.tsv:1220` and `curation/decisions.tsv:725`.
- The generated `ENVO:00002123` parent is supported as a broader engineered bioreactor context for the source path.
- `data/raw/gold_ecosystem_paths.tsv:1221` supports the child `Engineered > Bioreactor > Thiocyanate-remediating > Anaerobic-Aerobic` path, and the generated child record points back to this target as its source-path parent.

Unsupported or incomplete:

- No item-level curation has inspected whether `Thiocyanate-remediating` denotes a microbial habitat, a reactor objective, a remediation process, or another non-habitat source artifact.
- The target has no direct auxiliary support in `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_studies.tsv`, or `data/raw/gold_path_triads.tsv`; the committed biosample and study support for the thiocyanate-remediating branch is limited to its `Anaerobic-Aerobic` child path.
- No exact ontology grounding, term request, literature `EvidenceItem`, definition, or causal overlay has been reviewed for this thiocyanate-remediating bioreactor bin.

## Completeness

- An ignored-inclusive exact search over `curation`, `history`, `research`, `reports`, `data/habitats/PATHS.tsv`, `data/habitats/engineered`, `data/raw`, and `conf/id_label_targets.yaml` found the target generated record, the path-lock row, the exact class-level decision, the exact GOLD parent and child rows, the generated child that cites this target as parent, and two prior YAML review reports that mention this parent as a neighboring or unreviewed parent concept. The same search found no target-specific term request, term-request exclusion, history record, research report, causal overlay, direct biosample row, direct study row, or direct MIxS triad row; the pre-write `find` check found no existing review report file for the `thiocyanate_remediating` stem.
- An ignored-inclusive search for `thiocyanate`, `cyanide`, `cyanate`, `remediat`, and `SCN` over `data/raw/ontology_terms.tsv`, `curation/term_requests.tsv`, `curation/term_requests_excluded.tsv`, `curation/decisions.tsv`, and `curation/samples` found the related GOLD cyanide/thiocyanate and bioremediation-thiocyanate branches, a few generic bioremediation material term requests, and one unrelated PREGO/BTO `SCN` abbreviation hit. It found no candidate habitat term, existing term request, term-request exclusion, or sample row for the target.
- The `Anaerobic-Aerobic` child path has 12 biosamples in `data/raw/gold_path_biosamples.tsv:586` and appears in `data/raw/gold_studies.tsv:1226`; the same study row also links to `Engineered > Bioremediation > Thiocyanate` and `Engineered > Bioreactor > Wastewater > Cyanide/thiocyanate`, so future curation should review these exact source concepts together without assuming they are equivalent.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The target has only a class-level `CONFIRM_UNGROUNDED` decision, so its `UNGROUNDED` status has not been item-reviewed against the full `Engineered > Bioreactor > Thiocyanate-remediating` source path. | `curation/decisions.tsv:725` records `review_depth=CLASS` and says habitathood was not assessed. The exact GOLD row has zero direct assertions, no direct auxiliary biosample/study/triad rows were found with ignored files included, and the branch's committed auxiliary support sits on the `Anaerobic-Aerobic` child path. | `curation/decisions.tsv`; if the item is a real habitat with no exact term, `curation/term_requests.tsv`. |

## Recommended Edits

1. Item-review `habitatmech:GOLD.7a8691bc23` in `curation/decisions.tsv`. Decide whether the full GOLD path denotes a thiocyanate-remediating bioreactor habitat, a non-habitat remediation objective or process, or a candidate novel habitat needing `curation/term_requests.tsv`.
2. Review the linked child and sibling paths at the same time: `Engineered > Bioreactor > Thiocyanate-remediating > Anaerobic-Aerobic`, `Engineered > Bioreactor > Wastewater > Cyanide/thiocyanate`, and `Engineered > Bioremediation > Thiocyanate`. The shared GOLD study `Gs0118793` makes them related but not automatically equivalent.
3. If the source concept stays `UNGROUNDED`, add a term-request row defining the actual thiocyanate-remediating reactor habitat and its broader parent so the generated record carries a curator-authored definition rather than only the terse GOLD branch label.

## Follow-up Checks

- After updating `curation/decisions.tsv` or `curation/term_requests.tsv`, run `just seed`, `just seed-canary habitatmech:GOLD.7a8691bc23`, inspect `data/habitats/engineered/thiocyanate_remediating.yaml`, then run `just seed-apply --force`.
- Re-run `just validate data/habitats/engineered/thiocyanate_remediating.yaml`, `just validate-strict data/habitats/engineered/thiocyanate_remediating.yaml`, `just term-requests-check`, `just validate-causal-all`, `just validate-history`, `just verify-corpus --max-diffs 1`, `just worklist --limit 2000`, `just report`, and `git diff --check`.

## Additional Notes

The reviewed parent is distinct from its child `data/habitats/engineered/anaerobic_aerobic__b96ead5a.yaml`. That child already has its own YAML review report, `reports/yaml_record_review/20260924T142936Z-anaerobic_aerobic__b96ead5a.md`, which flags this same target as an unreviewed class-level parent that should be resolved before relying on the child's only source-path `parent_habitats` edge.

The generated YAML correctly omits `assertion_count` and `assertion_unit` because the exact parent GOLD row reports zero KGX organism assertions and the auxiliary GOLD bulk-export inventories have no direct row for `gold.ecosystem:7780`.
