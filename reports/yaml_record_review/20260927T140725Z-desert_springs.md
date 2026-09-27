# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/desert_springs.yaml
- Started UTC: 2026-09-27T14:07:25Z
- Finished UTC: 2026-09-27T14:07:25Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Record path | `data/habitats/aquatic/desert_springs.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.3b64b1f98f` |
| Label | `Desert springs` |
| Habitat category | `AQUATIC` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and `curation/decisions.tsv`; do not hand-edit this YAML. |

The target is the generated HabitatMech record for the GOLD source path
`Environmental > Aquatic > Freshwater > Desert springs`. `data/habitats/PATHS.tsv`
maps `habitatmech:GOLD.3b64b1f98f` to the `desert_springs` slug.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/desert_springs.yaml` | Pass. `linkml-validate` found no issues for this record. |
| `just validate-strict data/habitats/aquatic/desert_springs.yaml` | Pass. Strict closed-schema validation scanned 1 file with 0 files in error and 0 error rows. |
| `just validate-causal curation/causal_graphs/<overlay>.yaml` | Not applicable. An ignored-inclusive search for `habitatmech:GOLD.3b64b1f98f`, `gold.ecosystem:5401`, the exact GOLD path, the slug, and the label found no causal-graph overlay for this record. |
| `just validate-causal-all` | Pass. All 32 causal-graph curation files and 32 graphs validated. |
| Reference validator | Not applicable. The record has no `evidence`, `datasets`, or `causal_graphs` references to validate. |
| `just term-requests-check` | Pass. The generated term-request table is current at 109 terms. |
| `just validate-history` | Pass. 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus` | Pass. 3,206 expected records were present with 0 missing, 0 extra, and 0 differing generated YAML files. |
| `just worklist --status all --out /tmp/habitatmech-worklist.tsv` | Pass. The worklist completed, wrote 953 ungrounded rows, and included this record with 0 GOLD assertions and lexical candidates `desert oasis`, `salt spring`, and `desert sand`. |
| `just report --out /tmp/habitatmech-report.tsv` | Pass. The corpus report completed and included this record as `UNGROUNDED`, `SEEDED`, and sourced only from GOLD. |
| `git diff --check` | Pass after report creation. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| The generated record denotes the GOLD `Desert springs` freshwater path. | `data/raw/gold_ecosystem_paths.tsv` has one exact row for `Environmental > Aquatic > Freshwater > Desert springs`, leaf label `Desert springs`, depth 4, one GOLD node ID, and zero total assertions. The generated `source_attestations` entry repeats that source ID, label, and path. | Supported. |
| `ENVO:00002011` is inherited from the GOLD `Freshwater` source-path parent. | The exact source path is a child of `Environmental > Aquatic > Freshwater`; that parent path is generated as `ENVO:00002011`, whose vendored label is `fresh water`. | Supported as generated source-path hierarchy; still needs item-level review to verify that the material term is a strict broader habitat for a desert spring. |
| `mapping_status: SEEDED` follows from the maintained curation depth. | `curation/decisions.tsv` has a `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.3b64b1f98f`, but its `review_depth` is `CLASS`; HabitatMech class-level decisions do not promote records to `REVIEWED`. | Supported. |
| `grounding_status: UNGROUNDED` reflects the class-level decision, but is not an item-level judgment. | The decision note says the class-level sweep found no matching term in the vendored slice by the documented lexical routes and explicitly says whether the concept is a habitat at all was not assessed. | Structurally supported, but incomplete for curation. |
| The source path currently has no GOLD assertion payload to surface. | The exact `data/raw/gold_ecosystem_paths.tsv` row records zero organisms, zero studies, zero biosamples, and zero total assertions; ignored-inclusive exact-path searches found no row in `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, or `data/raw/gold_studies.tsv`. | Supported. |

## Evidence

The record has no authored definition, evidence entries, environmental
parameters, characteristic taxa, datasets, or causal graphs.

| Assertion | Evidence | Assessment |
|---|---|---|
| GOLD attests this collapsed ecosystem path with one source node and no organism assertions. | `data/raw/gold_ecosystem_paths.tsv` stores `gold_node_count` 1, `organism_count` 0, `study_count` 0, `biosample_count` 0, `total_assertions` 0, and `gold.ecosystem:5401` for the exact desert-springs path. The generated record preserves this with a GOLD attestation using `gold.ecosystem:5401`. | Supported. |
| The class-level ungrounded curation event records an exact maintained decision. | The first curation event mirrors the `curation/decisions.tsv` row for `habitatmech:GOLD.3b64b1f98f`, including `CONFIRM_UNGROUNDED`, the `2026-08-12` curator/date, and the class-sweep note. | Supported. |

No snippet or citation mismatch was present because this generated placeholder
record carries only source-inventory and curation-history facts.

## Completeness

This record is reproducible but not complete enough for reviewed habitat
curation. The exact GOLD path has only a class-level lexical screen: no
item-level decision has verified whether GOLD's desert-springs concept is a
microbial habitat, whether an exact ontology term exists, whether `fresh water`
is a true broader parent, or whether the minted record should receive a
novel-term definition.

An ignored-inclusive search over `data/raw`, `curation`, `history`, `research`,
`reports/yaml_record_review`, `conf`, and `data/habitats` for the minted ID,
GOLD node ID, exact GOLD path, slug, and label found only the generated record,
slug lockfile row, raw GOLD rows for the desert-springs parent and `Benthic`
child, the class-level decision, and generated uses of the `Benthic` child
after its separate item-level decision. Separate `find` searches of
`reports/yaml_record_review`, `curation/causal_graphs`, and `research/habitats`
found no exact desert-springs review report, causal overlay, or research
report.

The empty optional slots are otherwise unsurprising for a zero-assertion
GOLD-only source concept. GOLD does not supply claim-level evidence snippets,
curated causal edges, or `is_characteristic` taxa for this path.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `Desert springs` still needs item-level habitat review and a novel-term decision. | The generated YAML is sourced from a real GOLD path, and that path has a separately generated `Benthic` child, but the parent itself has zero organism, study, biosample, or MIxS-triad assertions. The only maintained decision for `habitatmech:GOLD.3b64b1f98f` is a class-level `CONFIRM_UNGROUNDED` row whose note explicitly did not assess whether this source concept is a habitat or a term-request candidate. Consequently the generated record has `mapping_status: SEEDED`, no authored definition, and no `curation/term_requests.tsv` row. | `curation/decisions.tsv`; if item review confirms no exact term, `curation/term_requests.tsv`. |

No blockers or minor findings were found.

## Recommended Edits

1. Revisit `habitatmech:GOLD.3b64b1f98f` in `curation/decisions.tsv` at
   `ITEM` depth. Verify the exact GOLD path, its zero-assertion raw inventory
   state, the generated `Benthic` child, and nearby ontology candidates such as
   `spring`, `desert oasis`, and `salt spring` before deciding whether the
   source path is in scope as a habitat.
2. If no exact vendored or external OBO term denotes this path, keep the minted
   identifier with `CONFIRM_UNGROUNDED` or a strictly broader
   `GROUND_AS_PARENT` relation as appropriate. Do not ground directly to
   `ENVO:00002011` `fresh water`; that term is inherited freshwater context
   rather than the desert-springs identity itself.
3. If item review confirms this is a real habitat with no exact ontology term,
   add a `curation/term_requests.tsv` definition for the minted desert-springs
   habitat, retaining the inherited `ENVO:00002011` parent only if item evidence
   shows that fresh water is a strict broader class rather than medium context.
4. Regenerate the target record from the maintained inputs instead of editing
   `data/habitats/aquatic/desert_springs.yaml` directly.

## Follow-up Checks

| Check | Purpose |
|---|---|
| Manual GOLD/ontology candidate review | Confirm the ITEM decision does not conflate GOLD's desert-springs source with a desert oasis, an arbitrary spring, the freshwater material in the spring, or the separately curated `Benthic` child. |
| `just seed` | Preview the regenerated corpus from the edited maintained inputs. |
| `just seed-canary habitatmech:GOLD.3b64b1f98f` | Confirm the one generated target carries the new item-depth decision, mapping status, definition, parents, and history expected from the maintained rows. |
| `just seed-apply --force` | Rebuild generated YAML after inspecting the canary output. |
| `just validate data/habitats/aquatic/desert_springs.yaml` | Check the regenerated target against the LinkML `HabitatRecord` schema. |
| `just validate-strict data/habitats/aquatic/desert_springs.yaml` | Check the regenerated target under the closed-schema validator. |
| `just term-requests-check` | Confirm generated ENVO term-request products are current if a novel term was added. |
| `just validate-history` | Confirm the append-only history record for the curation session is valid. |
| `just verify-corpus` | Prove generated `data/habitats/` still reproduces from `data/raw/` and curation inputs. |
| `just report` | Confirm the record moves out of the class-level sweep bucket after item review. |
| `git diff --check` | Catch whitespace errors in the maintained and generated diffs. |

## Additional Notes

- The absence checks in this review used `rg --no-ignore --hidden` and `find`,
  so ignored and hidden files were included.
- `just report --out /tmp/habitatmech-report.tsv` put this record in the
  `UNGROUNDED` / `SEEDED` GOLD-only cohort with 0 upstream assertions; the
  `/tmp/habitatmech-worklist.tsv` row listed the record as decided only because
  the class-level decision exists, not because it has an item-level review.
- This record has no maintained causal overlay. `just validate-causal-all`
  covers all existing overlays, and no focused `just validate-causal` target
  applies.
