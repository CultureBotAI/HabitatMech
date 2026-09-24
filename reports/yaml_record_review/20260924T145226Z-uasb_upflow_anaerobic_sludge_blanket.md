# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/uasb_upflow_anaerobic_sludge_blanket.yaml
- Started UTC: 2026-09-24T14:52:26Z
- Finished UTC: 2026-09-24T14:52:26Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.0d77d00b06` |
| Label | `UASB (Upflow anaerobic sludge blanket)` |
| Category | `ENGINEERED` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |
| Source concept | GOLD `Engineered > Bioreactor > UASB (Upflow anaerobic sludge blanket)` |
| Maintained inputs | `data/raw/gold_ecosystem_paths.tsv`; `curation/decisions.tsv` |
| Generated record | Yes; `just verify-corpus --max-diffs 1` reproduced all 3206 generated records byte-for-byte from maintained inputs. |

This is the depth-3 GOLD UASB bioreactor path that groups three GOLD node IDs, not the child `Sludge` or `Granular sludge` material paths below UASB.

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-uasb_upflow_anaerobic_sludge_blanket.md' -print` | Pass: no pre-existing report for this stem; `find` included ignored files under the searched directory. |
| `just validate data/habitats/engineered/uasb_upflow_anaerobic_sludge_blanket.yaml` | Pass: no LinkML issues found. |
| `just validate-strict data/habitats/engineered/uasb_upflow_anaerobic_sludge_blanket.yaml` | Pass: one file scanned; zero closed-schema errors. |
| `just validate-causal-all` | Pass: 32 causal-graph curation files with 32 graphs validated. |
| `just validate-causal <overlay>` | Not applicable: an ignored-inclusive `rg --no-ignore --hidden` search found no overlay for `habitatmech:GOLD.0d77d00b06` under `curation/causal_graphs/`. |
| Reference validator | Not applicable: this YAML has no `evidence` entries and no causal overlay references. |
| `just term-requests-check` | Pass: `curation/term_requests.tsv` is current. |
| `just validate-history` | Pass: 77 history records valid. |
| `just verify-corpus --max-diffs 1` | Pass: all 3206 generated records on disk match `data/raw/` and curation inputs. |
| `just worklist --limit 2000` | Pass: 0 ungrounded records still undecided; 1810 decisions on file. |
| `just report` | Pass: corpus report completed. |
| `git diff --check` | Pass. |

## Identity and Grounding

`data/raw/gold_ecosystem_paths.tsv:1222` is the maintained GOLD row for `Engineered > Bioreactor > UASB (Upflow anaerobic sludge blanket)`. It has leaf label `UASB (Upflow anaerobic sludge blanket)`, depth `3`, `gold_node_count` `3`, zero direct organism/study/biosample assertions, and node IDs `gold.ecosystem:8145|gold.ecosystem:8146|gold.ecosystem:8147`. `data/habitats/PATHS.tsv:1377` maps `habitatmech:GOLD.0d77d00b06` to the reviewed slug.

The generated `source_attestations` entry mirrors the GOLD path and records `gold.ecosystem:8145`, the first of the three collapsed node IDs. The record has only the source-path parent `ENVO:00002123`, because `Engineered > Bioreactor` is grounded to ENVO's `bioreactor`.

The `UNGROUNDED` status traces to `curation/decisions.tsv:172`, but that row is only a class-level `CONFIRM_UNGROUNDED`; its note says no term in the vendored slice matched by the sweep routes and explicitly says habitathood was not assessed.

That grounding is stale or incomplete. The vendored slice already contains `ENVO:00002213` `anaerobic sludge blanket reactor`, defined as an anaerobic bioreactor that treats wastewater through methanogenic microbes forming a sludge blanket due to upward flow. The GOLD label spells out `Upflow anaerobic sludge blanket`, so the source concept should be item-reviewed against `ENVO:00002213` as an exact identity rather than retained as an ungrounded minted term.

## Evidence

Supported by maintained inputs:

- `data/raw/gold_ecosystem_paths.tsv:1222` supports the GOLD UASB source identity, the three-node note, and the absence of direct GOLD organism assertions.
- `data/raw/ontology_terms.tsv:7295` supports `ENVO:00002213` as a non-obsolete, direct ENVO class in the vendored slice with label `anaerobic sludge blanket reactor`.
- `data/raw/ontology_subclass_edges.tsv:5408` places `ENVO:00002213` under `ENVO:00002124` `anaerobic bioreactor`, which is more precise than the current generated `ENVO:00002123` `bioreactor` parent.
- `data/raw/prego_habitats.tsv:382` and the generated `data/habitats/engineered/anaerobic_sludge_blanket_reactor.yaml` show that HabitatMech already has a PREGO-attested exact `ENVO:00002213` record with 6 PREGO taxon assertions.
- `data/raw/gold_ecosystem_paths.tsv:696` and `:1223` support distinct child GOLD paths for UASB sludge and granular sludge; the reviewed record is their UASB bioreactor parent, not the sludge material itself.

Unsupported or incomplete:

- `CONFIRM_UNGROUNDED` is not supported for the UASB source concept while `ENVO:00002213` is present in the vendored slice and matches the expanded GOLD acronym.
- The generated minted `habitatmech:GOLD.0d77d00b06` record duplicates the existing ENVO-grounded anaerobic sludge blanket reactor habitat instead of merging GOLD and PREGO attestations onto `ENVO:00002213`.
- There is no item-level decision establishing whether the three collapsed GOLD node IDs `8145`, `8146`, and `8147` are exact UASB reactor aliases. They share the same canonical GOLD path, so the current three-node note is reproducible, but the class-level sweep did not inspect the individual nodes.

## Completeness

- An ignored-inclusive exact search over `curation`, `history`, `research`, `reports`, `data/habitats/PATHS.tsv`, `data/habitats/engineered`, `data/raw`, and `conf/id_label_targets.yaml` found the target generated record, its path-lock row, the exact class-level decision row, the maintained GOLD parent and child UASB rows, one prior AGS review that mentions the neighboring UASB granular-sludge child, and no target-specific term request, history record, research report, causal overlay, biosample row, study row, or MIxS triad row.
- An ignored-inclusive exact search for `upflow`, `UASB`, `anaerobic sludge blanket`, `anaerobic-sludge-blanket`, and `sludge blanket` over `data/raw/ontology_terms.tsv`, `curation/term_requests.tsv`, `curation/term_requests_excluded.tsv`, and `curation/decisions.tsv` found `ENVO:00002213` and one existing term-request note that discusses `ENVO:00002213`; it found no target-specific term request or exclusion.
- An ignored-inclusive exact `rg --no-ignore --hidden` search under `curation/causal_graphs/` found no overlay for `habitatmech:GOLD.0d77d00b06`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record is minted and `UNGROUNDED` even though a fitting exact ENVO identity, `ENVO:00002213` `anaerobic sludge blanket reactor`, is already vendored. | GOLD expands the `UASB` acronym to `Upflow anaerobic sludge blanket`; `data/raw/ontology_terms.tsv:7295` defines `ENVO:00002213` as an anaerobic bioreactor with an upward-flow sludge blanket; `curation/decisions.tsv:172` is only a class-level negative sweep. | `curation/decisions.tsv`: change `habitatmech:GOLD.0d77d00b06` from `CONFIRM_UNGROUNDED` to an item-level `GROUND` decision targeting `ENVO:00002213` with expected label `anaerobic sludge blanket reactor`. |
| Major | Missing exact grounding leaves the same habitat split into two records instead of merging the GOLD UASB source with the existing PREGO `ENVO:00002213` record. | `data/habitats/engineered/uasb_upflow_anaerobic_sludge_blanket.yaml` carries the GOLD UASB attestation under a minted ID; `data/habitats/engineered/anaerobic_sludge_blanket_reactor.yaml` is the existing `ENVO:00002213` record with PREGO support. The seeder only merges source concepts when they share the same ontology identity. | `curation/decisions.tsv`; after re-grounding, the generated `ENVO:00002213` record should carry both GOLD and PREGO source attestations and the minted UASB YAML should disappear. |

## Recommended Edits

1. Update `curation/decisions.tsv` row `habitatmech:GOLD.0d77d00b06` to `GROUND`, object `ENVO:00002213`, object label `anaerobic sludge blanket reactor`, relation `EXACT`, `review_depth=ITEM`, with a note recording that `UASB` expands to `Upflow anaerobic sludge blanket` and denotes ENVO's upward-flow anaerobic sludge blanket reactor.
2. Regenerate the corpus so the GOLD source attestation merges onto `data/habitats/engineered/anaerobic_sludge_blanket_reactor.yaml`; canary the merged `ENVO:00002213` record, then run the full seed with `--prune` so `data/habitats/engineered/uasb_upflow_anaerobic_sludge_blanket.yaml` is removed and `data/habitats/PATHS.tsv` drops the stale minted identifier.
3. Rebuild redirects and pages after the deletion commit so the former UASB page URL points at the merged anaerobic-sludge-blanket-reactor page.

## Follow-up Checks

- Run `just validate-products` or the CI `label-correspondence` workflow to verify `ENVO:00002213` still resolves to `anaerobic sludge blanket reactor`.
- Run `just seed`, `just seed-canary ENVO:00002213`, inspect the merged `ENVO:00002213` YAML, then run `just seed-apply --force --prune`.
- Commit the seed/prune diff, then run `just redirects` and `just render` so the retired generated UASB page redirects correctly.
- Re-run `just validate data/habitats/engineered/anaerobic_sludge_blanket_reactor.yaml`, `just validate-strict`, `just verify-corpus --max-diffs 1`, `just render-check`, `just redirects-check`, `just term-requests-check`, `just validate-causal-all`, `just validate-history`, `just worklist --limit 2000`, `just report`, and `git diff --check`.

## Additional Notes

The exact UASB source-path search was path-qualified to keep this parent bioreactor distinct from its two GOLD descendants:

- `Engineered > Bioreactor > UASB (Upflow anaerobic sludge blanket) > Sludge`
- `Engineered > Bioreactor > UASB (Upflow anaerobic sludge blanket) > Sludge > Granular sludge`

The child `Granular sludge` row at `data/raw/gold_ecosystem_paths.tsv:696` has three direct GOLD organism assertions, but those assertions belong to the granular sludge material and do not prove a direct assertion count for the UASB bioreactor parent.
