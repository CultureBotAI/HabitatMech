# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/delivery_networks.yaml
- Started UTC: 2026-09-24T08:06:40Z
- Finished UTC: 2026-09-24T08:06:40Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Record path | `data/habitats/aquatic/delivery_networks.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.835443324e` |
| Label | `Delivery networks` |
| Habitat category | `AQUATIC` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and `curation/decisions.tsv`; do not hand-edit this YAML. |

The target is a generated GOLD leaf for the source path
`Environmental > Aquatic > Freshwater > Drinking water > Delivery networks`.
`data/habitats/PATHS.tsv` maps `habitatmech:GOLD.835443324e` to the
`delivery_networks` slug.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/delivery_networks.yaml` | Pass. `linkml-validate` found no issues for this record. |
| `just validate-strict data/habitats/aquatic/delivery_networks.yaml` | Pass. Strict closed-schema validation scanned 1 file with 0 files in error and 0 error rows. |
| `just validate-causal curation/causal_graphs/<overlay>.yaml` | Not applicable. An ignored-inclusive search for `habitatmech:GOLD.835443324e`, `gold.ecosystem:4058`, the exact GOLD path, and the label found no causal-graph overlay for this record. |
| `just validate-causal-all` | Pass. All 32 causal-graph curation files and 32 graphs validated. |
| Reference validator | Not applicable. The record has no `evidence`, `datasets`, or `causal_graphs` references to validate. |
| `just term-requests-check` | Pass. The generated term-request table is current at 109 terms. |
| `just validate-history` | Pass. 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Pass. 3,206 expected records were present with 0 missing, 0 extra, and 0 differing generated YAML files. |
| `just worklist --limit 2000` | Pass. The curation worklist command completed and reported 1,810 decisions on file. |
| `just report` | Pass. The corpus report command completed. |
| `git diff --check` | Pass after report creation. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| The generated record denotes the GOLD `Delivery networks` drinking-water leaf. | `data/raw/gold_ecosystem_paths.tsv` has one exact row for `Environmental > Aquatic > Freshwater > Drinking water > Delivery networks` with node `gold.ecosystem:4058`, leaf label `Delivery networks`, depth 5, and 3 organism assertions. The generated `source_attestations` entry repeats that source ID, label, path, count, and `ORGANISM` assertion unit. | Supported. |
| The record is a distinct sibling of other drinking-water leaves, not a duplicate of chlorinated, chloraminated, untreated, unchlorinated, or filtered drinking water. | The committed GOLD path inventory keeps `Delivery networks`, `Unchlorinated`, `Untreated`, `Chlorinated`, `Filtered water`, and `Chloraminated` as separate children of `Environmental > Aquatic > Freshwater > Drinking water`. | Supported. |
| `habitatmech:GOLD.99a88ecb51` is a broader source-path parent for this source concept. | `data/habitats/aquatic/drinking_water__6d6ef579.yaml` is the generated `Drinking water` GOLD parent path, and the delivery-network source path is a child of that path in `data/raw/gold_ecosystem_paths.tsv`. | Supported. |
| `mapping_status: SEEDED` follows from the maintained curation depth. | `curation/decisions.tsv` has a `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.835443324e`, but its `review_depth` is `CLASS`; HabitatMech class-level decisions do not promote records to `REVIEWED`. | Supported. |
| `grounding_status: UNGROUNDED` reflects the class-level decision, but is not an item-level judgment. | The decision note says the class-level sweep found no matching term in the vendored slice and explicitly says whether the concept is a habitat at all was not assessed. | Structurally supported, but incomplete for curation. |
| GOLD MIxS triads provide contextual evidence for this source path. | `data/raw/gold_path_triads.tsv` lists `ENVO:00000873` as broad scale, `ENVO:03600118` as local scale with cached GOLD label `water treatment plant`, and `ENVO:00003064` as medium for the exact path. | Contextual only. `ENVO:00000873` and `ENVO:00003064` are vendored but broader than this leaf; `ENVO:03600118` was found in the raw triads but not in `data/raw/ontology_terms.tsv`. |

## Evidence

The record has no authored definition, evidence entries, environmental
parameters, characteristic taxa, datasets, or causal graphs.

| Assertion | Evidence | Assessment |
|---|---|---|
| GOLD attests this exact source path with 3 organism assertions. | `data/raw/gold_ecosystem_paths.tsv` has assertion count `3` for node `gold.ecosystem:4058`, and the generated attestation preserves the same count and `ORGANISM` unit. | Supported. |
| GOLD has biosample and study context for the exact delivery-network path. | `data/raw/gold_path_biosamples.tsv` has 28 biosamples for node `4058`; `data/raw/gold_studies.tsv` lists `Gs0056616`, `Gs0118587`, `Gs0133054`, `Gs0134339`, and `Gs0150313` on the exact delivery-network path, with `Gs0133054` also attached to its `Drinking water` parent. | Supported as source context not yet surfaced in the YAML. |
| The class-level ungrounded curation event records an exact maintained decision. | The first curation event mirrors the `curation/decisions.tsv` row for `habitatmech:GOLD.835443324e`, including `CONFIRM_UNGROUNDED`, the `2026-08-12` curator/date, and the class-sweep note. | Supported. |

No snippet or citation mismatch was present because this generated placeholder
record carries only source inventory and curation-history facts.

## Completeness

This record is reproducible but not complete enough for reviewed habitat
curation. The exact GOLD path has class-level screening, raw MIxS triads, 28
biosamples, and 5 GOLD studies, but no item-level decision has verified whether
the drinking-water delivery-network leaf is a real habitat, whether any exact
ontology term exists, or whether the minted record should receive a novel-term
definition.

An ignored-inclusive search over `curation/term_requests.tsv`,
`curation/external_xrefs.tsv`, `curation/causal_graphs`, `history`, `research`,
and `reports/yaml_record_review` for the minted ID, GOLD node, exact GOLD path,
label, delivery/distribution-network phrases, and raw triad local term found no
exact term request, external xref, causal overlay, item-level history record, or
prior exact review. It found only the generated record and slug lockfile, the
raw GOLD rows, the class-level decision, one unrelated leaf causal-graph mention
of surface-water distribution, one contextual indoor-habitat research mention
of building plumbing and drinking-water distribution, and sibling chlorinated
and chloraminated review reports that mention `Delivery networks` only as a
separate drinking-water sibling.

The empty optional slots are otherwise unsurprising for a small GOLD-only
record: GOLD does not supply curated causal edges, `is_characteristic` taxa, or
claim-level evidence snippets for this leaf.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `Delivery networks` still needs item-level habitat review and a novel-term decision. | The generated YAML is sourced from a real GOLD drinking-water leaf, and source inventories provide exact node, biosample, study, and MIxS triad rows. The only maintained decision for `habitatmech:GOLD.835443324e` is a class-level `CONFIRM_UNGROUNDED` row whose note explicitly did not assess whether this source concept is a habitat or a term-request candidate. Consequently the generated record has `mapping_status: SEEDED`, no authored definition, and no `curation/term_requests.tsv` row. | `curation/decisions.tsv`; if item review confirms no exact term, `curation/term_requests.tsv`. |

No blockers or minor findings were found.

## Recommended Edits

1. Revisit `habitatmech:GOLD.835443324e` in `curation/decisions.tsv` at
   `ITEM` depth. Verify the exact GOLD path, the sibling drinking-water leaves,
   the MIxS broad/local/medium triads, and nearby ontology candidates before
   deciding whether the source is a drinking-water distribution/delivery-network
   habitat or not a habitat.
2. If no exact vendored or external OBO term denotes this leaf, keep the minted
   identifier with `CONFIRM_UNGROUNDED` or a strictly broader
   `GROUND_AS_PARENT` relation as appropriate. Do not ground directly to
   `ENVO:00003064` `drinking water`; that term is broader medium context rather
   than the delivery-network leaf itself.
3. If item review confirms this is a real habitat with no exact ontology term,
   add a `curation/term_requests.tsv` definition for the minted
   delivery-network habitat, retaining `habitatmech:GOLD.99a88ecb51` as the
   source-derived parent unless item evidence shows the drinking-water parent is
   false.
4. Regenerate the target record from the maintained inputs instead of editing
   `data/habitats/aquatic/delivery_networks.yaml` directly.

## Follow-up Checks

| Check | Purpose |
|---|---|
| Manual GOLD/ontology candidate review | Confirm the ITEM decision does not conflate the delivery-network leaf with the broader `Drinking water` parent or sibling treatment leaves. |
| `just seed` | Preview the regenerated corpus from the edited maintained inputs. |
| `just seed-canary habitatmech:GOLD.835443324e` | Confirm the one generated target carries the new item-depth decision, mapping status, definition, parents, and history expected from the maintained rows. |
| `just seed-apply --force` | Rebuild generated YAML after inspecting the canary output. |
| `just validate data/habitats/aquatic/delivery_networks.yaml` | Check the regenerated target against the LinkML `HabitatRecord` schema. |
| `just validate-strict data/habitats/aquatic/delivery_networks.yaml` | Check the regenerated target under the closed-schema validator. |
| `just term-requests-check` | Confirm generated ENVO term-request products are current if a novel term was added. |
| `just validate-history` | Confirm the append-only history record for the curation session is valid. |
| `just verify-corpus --max-diffs 1` | Prove generated `data/habitats/` still reproduces from `data/raw/` and curation inputs. |
| `just report` | Confirm the record moves out of the class-level sweep bucket after item review. |
| `git diff --check` | Catch whitespace errors in the maintained and generated diffs. |

## Additional Notes

- The absence checks in this review used `rg --no-ignore --hidden` and `find`,
  so ignored and hidden files were included.
- `ENVO:03600118` appears in the raw GOLD triad inventory for this path but was
  not found in `data/raw/ontology_terms.tsv`; it should be treated as cached raw
  context until vendored or otherwise label-verified.
- This record has no maintained causal overlay. `just validate-causal-all`
  covers all existing overlays, and no focused `just validate-causal` target
  applies.
