# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/anaerobic_aerobic__b96ead5a.yaml
- Started UTC: 2026-09-24T14:29:36Z
- Finished UTC: 2026-09-24T14:29:36Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.52ffd9fa79` |
| Label | `Anaerobic-Aerobic` |
| Category | `ENGINEERED` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |
| Maintained inputs | `data/raw/gold_ecosystem_paths.tsv`; `curation/decisions.tsv` |
| Generated record | Yes; `just verify-corpus --max-diffs 1` reproduced the committed YAML byte-for-byte |

The record represents the GOLD path `Engineered > Bioreactor > Thiocyanate-remediating > Anaerobic-Aerobic`, not the sibling GOLD paths with the same `Anaerobic-Aerobic` leaf under `EBPR` or `SBR-EBPR`.

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-anaerobic_aerobic__b96ead5a.md' -print` | Pass: no pre-existing report for this stem; `find` included ignored files under the searched directory. |
| `just validate data/habitats/engineered/anaerobic_aerobic__b96ead5a.yaml` | Pass: no LinkML issues found. |
| `just validate-strict data/habitats/engineered/anaerobic_aerobic__b96ead5a.yaml` | Pass: one file scanned; zero closed-schema errors. |
| `just validate-causal-all` | Pass: 32 causal-graph curation files with 32 graphs validated. |
| `just validate-causal <overlay>` | Not applicable: an ignored-inclusive `rg --no-ignore --hidden` search found no `habitatmech:GOLD.52ffd9fa79` overlay under `curation/causal_graphs/`. |
| Reference validator | Not applicable: this YAML has no `evidence` entries and no causal overlay references. |
| `just term-requests-check` | Pass: `curation/term_requests.tsv` is current. |
| `just validate-history` | Pass: 77 history records valid. |
| `just verify-corpus --max-diffs 1` | Pass: all 3206 generated records on disk match `data/raw/` and curation inputs. |
| `just worklist --limit 2000` | Pass: 0 ungrounded records still undecided; 1810 decisions on file. |
| `just report` | Pass: corpus report completed. |
| `git diff --check` | Pass. |

## Identity and Grounding

The generated identity traces to `data/raw/gold_ecosystem_paths.tsv:1221`, whose canonical path is `Engineered > Bioreactor > Thiocyanate-remediating > Anaerobic-Aerobic`, leaf label is `Anaerobic-Aerobic`, level is `4`, GOLD node count is `2`, and GOLD node IDs are `gold.ecosystem:7781|gold.ecosystem:7782`.

`data/habitats/PATHS.tsv:1896` maps `habitatmech:GOLD.52ffd9fa79` to the reviewed `anaerobic_aerobic__b96ead5a` slug. The generated source attestation records only `gold.ecosystem:7781` because `src/habitatmech/seed.py` emits the first node ID when several GOLD node IDs share one canonical path.

The `UNGROUNDED` status traces to `curation/decisions.tsv:526`, but that row has `review_depth=CLASS`. Its text says no vendored-slice term matched the label and explicitly says whether the concept is a habitat was not assessed. That is insufficient for a reviewed item-level habitat decision.

The source-path parent is `habitatmech:GOLD.7a8691bc23`, generated from `Engineered > Bioreactor > Thiocyanate-remediating`; its own generated record also has only a class-level `CONFIRM_UNGROUNDED` decision in `curation/decisions.tsv:725`.

## Evidence

Supported by maintained inputs:

- The minted identifier, label, category, GOLD path, two-node note, and seeded history follow from `data/raw/gold_ecosystem_paths.tsv:1221`.
- The source-path hierarchy from the target to `habitatmech:GOLD.7a8691bc23` is reproducible from the same GOLD path.
- The class-level `CONFIRM_UNGROUNDED` history event follows from `curation/decisions.tsv:526`.
- Auxiliary GOLD biosample support for node `7782` is present in `data/raw/gold_path_biosamples.tsv:586`, and the exact target path is present in `data/raw/gold_studies.tsv:1226`.

Unsupported or incomplete:

- No item-level curation has inspected whether `Anaerobic-Aerobic` under `Thiocyanate-remediating` denotes a microbial habitat, a bioreactor operating condition, a remediation process, or another non-habitat source artifact.
- The generated source attestation omits `assertion_count` and `assertion_unit` because `data/raw/gold_ecosystem_paths.tsv:1221` reports zero `organism_count`. Separate GOLD bulk-export inventories still contain 12 biosamples for node `7782` and one study row for the exact same path, but those auxiliary rows are not surfaced on the generated YAML attestation.
- No literature `EvidenceItem` or causal overlay is attached. That is acceptable for an unreviewed GOLD seed, but it leaves the actual thiocyanate-remediating anaerobic/aerobic niche unsubstantiated by curator-inspected evidence.

## Completeness

- An ignored-inclusive exact search over `data/raw/ontology_terms.tsv`, `curation/term_requests.tsv`, and `curation/term_requests_excluded.tsv` for `Anaerobic-Aerobic`, spelling variants, `Thiocyanate-remediating`, and `thiocyanate` found no candidate ontology row, term request, or term-request exclusion.
- An ignored-inclusive exact search under `curation/causal_graphs/` found no causal overlay for `habitatmech:GOLD.52ffd9fa79`.
- An ignored-inclusive exact search under `reports/yaml_record_review/` found only `reports/yaml_record_review/20260924T140857Z-anaerobic_aerobic.md`, which mentions this target as a distinct same-leaf sibling of `Engineered > Bioreactor > SBR-EBPR > Anaerobic-Aerobic`.
- `data/raw/gold_path_biosamples.tsv:586` reports 12 biosamples for `gold.ecosystem:7782` on the exact target path, and `data/raw/gold_studies.tsv:1226` lists the exact target path in GOLD study `Gs0118793`. No matching target row was found in `data/raw/gold_path_triads.tsv` during the ignored-inclusive exact source-path search.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The target has only a class-level `CONFIRM_UNGROUNDED` decision, so its `UNGROUNDED` status has not been item-reviewed against the full `Thiocyanate-remediating > Anaerobic-Aerobic` source path. | `curation/decisions.tsv:526` records `review_depth=CLASS` and says habitathood was not assessed; the exact committed GOLD path also has a 12-biosample row in `gold_path_biosamples.tsv:586` and a GOLD study row in `gold_studies.tsv:1226`, so the source concept is not merely an unattested empty class in all raw tables. | `curation/decisions.tsv`; if the item is a real habitat with no term, `curation/term_requests.tsv`. |
| Major | Auxiliary GOLD biosample and study support for the exact path is invisible in the generated source attestation, so the YAML looks completely unsupported unless a curator separately inspects the GOLD bulk-export inventories. | `data/raw/gold_ecosystem_paths.tsv:1221` aggregates `gold.ecosystem:7781|gold.ecosystem:7782` and reports zero organisms from the KGX-derived table; `data/raw/gold_path_biosamples.tsv:586` separately reports 12 biosamples for node `7782` on the same path, and `data/raw/gold_studies.tsv:1226` lists the same path in study `Gs0118793`. The generated YAML shows `source_id: gold.ecosystem:7781` and no assertion count. | GOLD extraction/raw inventory and source-attestation handling for `data/raw/gold_path_biosamples.tsv` and `data/raw/gold_studies.tsv`. |
| Major | The generated parent `habitatmech:GOLD.7a8691bc23` is also only class-level reviewed, so the target's sole `parent_habitats` edge rests on an unreviewed source-path concept that may be an operation or remediation context rather than a strictly broader habitat. | `data/habitats/engineered/thiocyanate_remediating.yaml` points to `Engineered > Bioreactor > Thiocyanate-remediating`; `curation/decisions.tsv:725` has the same class-level "habitathood was NOT assessed" decision text for that parent. | `curation/decisions.tsv`; possibly `curation/term_requests.tsv` if the parent is confirmed to be a real novel habitat. |

## Recommended Edits

1. Item-review `habitatmech:GOLD.52ffd9fa79` in `curation/decisions.tsv`. Decide whether the exact GOLD path is a microbial habitat, a non-habitat bioreactor operating pattern, or a candidate novel habitat needing `curation/term_requests.tsv`.
2. Reconcile how auxiliary GOLD biosample and study support should appear in generated records. Either add a distinct biosample/study support channel to GOLD source attestations, or document and encode that `assertion_count` is intentionally limited to KGX organism counts while `gold_path_biosamples.tsv` and `gold_studies.tsv` remain review-only inventories.
3. Item-review `habitatmech:GOLD.7a8691bc23` before relying on it as a strict `parent_habitats` value for the anaerobic/aerobic child.

## Follow-up Checks

- After updating `curation/decisions.tsv` or `curation/term_requests.tsv`, run `just seed`, `just seed-canary habitatmech:GOLD.52ffd9fa79`, inspect `data/habitats/engineered/anaerobic_aerobic__b96ead5a.yaml`, then run `just seed-apply --force`.
- After changing GOLD extraction, raw inventory rows, or source-attestation handling, run `just provenance-check`, `just seed`, the target canary, `just seed-apply --force`, and `just verify-corpus --max-diffs 1`.
- Re-run `just validate data/habitats/engineered/anaerobic_aerobic__b96ead5a.yaml`, `just validate-strict data/habitats/engineered/anaerobic_aerobic__b96ead5a.yaml`, `just term-requests-check`, `just validate-causal-all`, `just validate-history`, `just worklist --limit 2000`, `just report`, and `git diff --check`.

## Additional Notes

Exact sibling searches were intentionally path-qualified because three GOLD records share the `Anaerobic-Aerobic` leaf under different engineered bioreactor branches:

- `Engineered > Bioreactor > EBPR > Anaerobic-Aerobic`
- `Engineered > Bioreactor > SBR-EBPR > Anaerobic-Aerobic`
- `Engineered > Bioreactor > Thiocyanate-remediating > Anaerobic-Aerobic`

The prior `20260924T140857Z-anaerobic_aerobic.md` report concerns the EBPR branch and explicitly calls this record an adjacent same-label sibling, not a duplicate target.

`scripts/extract_gold_biosamples.py` documents that `data/raw/gold_path_biosamples.tsv` and `data/raw/gold_studies.tsv` are derived from GOLD's bulk export because `data/raw/gold_ecosystem_paths.tsv` comes from kg-microbe's KGX dump, which does not expose biosamples. The exact-path 12-biosample row is therefore auxiliary support, not proof that `gold_ecosystem_paths.tsv:1221` has a stale `biosample_count`.
