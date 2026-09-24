# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/cyanide_thiocyanate.yaml
- Started UTC: 2026-09-24T15:12:07Z
- Finished UTC: 2026-09-24T15:12:07Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.23007d6432` |
| Label | `Cyanide/thiocyanate` |
| Category | `ENGINEERED` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |
| Source concept | GOLD `Engineered > Bioreactor > Wastewater > Cyanide/thiocyanate` |
| Maintained inputs | `data/raw/gold_ecosystem_paths.tsv`; `curation/decisions.tsv` |
| Generated record | Yes; `just verify-corpus --max-diffs 1` reproduced all 3206 generated records byte-for-byte from maintained inputs. |

The target is the depth-4 GOLD wastewater contaminant path under engineered bioreactors, not the sibling `Engineered > Bioreactor > Thiocyanate-remediating` reactor branch or the `Engineered > Bioremediation > Thiocyanate` branch.

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-cyanide_thiocyanate.md' -print` | Pass: no pre-existing report for this stem; `find` included ignored files under the searched directory. |
| `just validate data/habitats/engineered/cyanide_thiocyanate.yaml` | Pass: no LinkML issues found. |
| `just validate-strict data/habitats/engineered/cyanide_thiocyanate.yaml` | Pass: one file scanned; zero closed-schema errors. |
| `just validate-causal-all` | Pass: 32 causal-graph curation files with 32 graphs validated. |
| `just validate-causal <overlay>` | Not applicable: an ignored-inclusive `rg --no-ignore --hidden` search found no overlay for `habitatmech:GOLD.23007d6432` under `curation/causal_graphs/`. |
| Reference validator | Not applicable: this YAML has no `evidence` entries and no causal overlay references. |
| `just term-requests-check` | Pass: `curation/term_requests.tsv` is current. |
| `just validate-history` | Pass: 77 history records valid. |
| `just verify-corpus --max-diffs 1` | Pass: all 3206 generated records on disk match `data/raw/` and curation inputs. |
| `just worklist --limit 2000` | Pass: 0 ungrounded records still undecided; 1810 decisions on file. |
| `just report` | Pass: corpus report completed. |
| `git diff --check` | Pass. |

## Identity and Grounding

`data/raw/gold_ecosystem_paths.tsv:1224` is the maintained source row for the reviewed target. It records canonical path `Engineered > Bioreactor > Wastewater > Cyanide/thiocyanate`, level `4`, leaf label `Cyanide/thiocyanate`, two collapsed GOLD node IDs, zero direct organism/study/biosample assertions in that inventory, and node IDs `gold.ecosystem:5683|gold.ecosystem:5684`.

The generated attestation mirrors that path and records only `gold.ecosystem:5683`, the first collapsed node ID. The path lock at `data/habitats/PATHS.tsv:1547` maps `habitatmech:GOLD.23007d6432` to the reviewed `cyanide_thiocyanate` slug.

The `UNGROUNDED` status traces to `curation/decisions.tsv:293`, but that row has `review_depth=CLASS`. Its note says the class-level sweep found no vendored-slice lexical match and explicitly says whether the concept is a habitat was not assessed. `curation/samples/class_swept_unscreened-20260814.tsv:10` later sampled this path and marked it "ok", but that sample file is not a seeder input and did not promote the maintained decision to an item-level habitat and term-candidate review.

The sole parent is `habitatmech:GOLD.5e086933bc`, generated from the direct GOLD parent path `Engineered > Bioreactor > Wastewater`. That edge is plausible for a wastewater bin named by cyanide/thiocyanate contamination; unlike nearby sludge or reactor-mode leaves, the target has no contradictory ontology parent or exact vendored identity.

## Evidence

Supported by maintained inputs:

- The minted identifier, label, category, GOLD source path, two-node note, and seeded class-level curation history all follow from `data/raw/gold_ecosystem_paths.tsv:1224` and `curation/decisions.tsv:293`.
- The source-path hierarchy from this target to `habitatmech:GOLD.5e086933bc` follows from the GOLD path prefix `Engineered > Bioreactor > Wastewater`.
- `data/raw/gold_path_biosamples.tsv:941` reports one biosample on `gold.ecosystem:5684`, and `data/raw/gold_studies.tsv:1226` lists the exact target path in GOLD study `Gs0118793`.

Unsupported or incomplete:

- No item-level curation has inspected whether `Cyanide/thiocyanate` denotes cyanide/thiocyanate wastewater, a contaminant class, a remediation process, or another non-habitat source artifact in this GOLD path.
- No exact ontology grounding or term request has been reviewed for the combined cyanide/thiocyanate wastewater habitat.
- No literature `EvidenceItem`, definition, or causal overlay is attached. That is acceptable for an unreviewed GOLD seed, but it leaves the meaning of the novel wastewater subtype unsupported beyond GOLD's path text and auxiliary GOLD biosample/study rows.
- Auxiliary GOLD biosample and study rows are not surfaced in the generated `source_attestations` item because `data/raw/gold_ecosystem_paths.tsv:1224` reports zero KGX-derived organism assertions.

## Completeness

- An ignored-inclusive exact search over `curation`, `history`, `research`, `reports`, `data/habitats/PATHS.tsv`, `data/habitats/engineered`, `data/raw`, and `conf/id_label_targets.yaml` found the target generated record, the path-lock row, the class-level decision, the sample row, the exact GOLD ecosystem row, the exact auxiliary GOLD biosample and study rows, and no target-specific term request, term-request exclusion, history record, research report, causal overlay, MIxS triad row, or prior YAML review report.
- An ignored-inclusive search for `cyanide`, `thiocyanate`, and `SCN` over `data/raw` and `curation` found the related GOLD thiocyanate branches and one unrelated PREGO/BTO abbreviation hit for `SCN`; it found no candidate habitat term, no existing term request, and no existing term-request exclusion for cyanide/thiocyanate wastewater.
- The exact study row links this target to `Engineered > Bioreactor > Thiocyanate-remediating > Anaerobic-Aerobic` and `Engineered > Bioremediation > Thiocyanate`, so future curation should review the three GOLD concepts together without assuming they are equivalent.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The target has only a class-level `CONFIRM_UNGROUNDED` decision, so its `UNGROUNDED` status has not been item-reviewed against the full `Engineered > Bioreactor > Wastewater > Cyanide/thiocyanate` path. | `curation/decisions.tsv:293` records `review_depth=CLASS` and says habitathood was not assessed. The exact committed GOLD path also has one biosample in `gold_path_biosamples.tsv:941`, appears in `gold_studies.tsv:1226`, and was sampled as an ok habitat in `curation/samples/class_swept_unscreened-20260814.tsv:10`, so the source concept warrants a maintained item-level decision rather than remaining a bare sweep result. | `curation/decisions.tsv`; if the item is a real habitat with no term, `curation/term_requests.tsv`. |
| Major | Auxiliary GOLD biosample and study support for the exact path is invisible in the generated source attestation, so the YAML looks completely unattested unless a curator separately inspects the GOLD bulk-export inventories. | `data/raw/gold_ecosystem_paths.tsv:1224` aggregates `gold.ecosystem:5683|gold.ecosystem:5684` and reports zero organism assertions from the KGX-derived table; `data/raw/gold_path_biosamples.tsv:941` separately reports one biosample for node `5684`, and `data/raw/gold_studies.tsv:1226` lists the same path in study `Gs0118793`. The generated YAML shows `source_id: gold.ecosystem:5683` and no assertion count. | GOLD extraction/raw inventory and source-attestation handling for `data/raw/gold_path_biosamples.tsv` and `data/raw/gold_studies.tsv`. |

## Recommended Edits

1. Item-review `habitatmech:GOLD.23007d6432` in `curation/decisions.tsv`. Decide whether the full GOLD path denotes cyanide/thiocyanate wastewater, a non-habitat contaminant/process label, or a candidate novel habitat needing `curation/term_requests.tsv`.
2. If the source concept stays `UNGROUNDED`, add a term-request row defining the actual wastewater habitat and its broader parent so the generated record carries a curator-authored definition rather than only the terse GOLD leaf label.
3. Reconcile how auxiliary GOLD biosample and study support should appear in generated records. Either add a distinct biosample/study support channel to GOLD source attestations, or document and encode that `assertion_count` is intentionally limited to KGX organism counts while `gold_path_biosamples.tsv` and `gold_studies.tsv` remain review-only inventories.

## Follow-up Checks

- After updating `curation/decisions.tsv` or `curation/term_requests.tsv`, run `just seed`, `just seed-canary habitatmech:GOLD.23007d6432`, inspect `data/habitats/engineered/cyanide_thiocyanate.yaml`, then run `just seed-apply --force`.
- After changing GOLD extraction, raw inventory rows, or source-attestation handling, run `just provenance-check`, `just seed`, the target canary, `just seed-apply --force`, and `just verify-corpus --max-diffs 1`.
- Re-run `just validate data/habitats/engineered/cyanide_thiocyanate.yaml`, `just validate-strict data/habitats/engineered/cyanide_thiocyanate.yaml`, `just term-requests-check`, `just validate-causal-all`, `just validate-history`, `just worklist --limit 2000`, `just report`, and `git diff --check`.

## Additional Notes

`scripts/extract_gold_biosamples.py` documents that `data/raw/gold_path_biosamples.tsv` and `data/raw/gold_studies.tsv` are derived from GOLD's bulk export because `data/raw/gold_ecosystem_paths.tsv` comes from kg-microbe's KGX dump, which does not expose biosamples. The exact-path one-biosample row is therefore auxiliary support, not proof that `gold_ecosystem_paths.tsv:1224` has a stale `biosample_count`.
