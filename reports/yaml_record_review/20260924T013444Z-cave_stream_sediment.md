# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/cave_stream_sediment.yaml
- Started UTC: 2026-09-24T01:18:00Z
- Finished UTC: 2026-09-24T01:34:44Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.5c3db359b7` |
| Label | `Cave stream sediment` |
| Habitat category | `AQUATIC` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Generated path | `data/habitats/aquatic/cave_stream_sediment.yaml` |
| Maintained owner | `curation/decisions.tsv`, `curation/term_requests.tsv`, and GOLD source inventories under `data/raw/` |

`data/habitats/aquatic/cave_stream_sediment.yaml` is generated. Future fixes
must change maintained inputs and regenerate the YAML rather than patching the
record directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/cave_stream_sediment.yaml` | Pass - LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/cave_stream_sediment.yaml` | Pass - 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Target causal overlay validator | Not applicable - ignored-independent `find` searches found no `*cave*` or `*stream*` overlay under `curation/causal_graphs`; `*sediment*` only found generic `deep_marine_sediment.yaml`, `sediment.yaml`, and `marine_sediment.yaml`. |
| `just validate-causal-all` | Pass - 32 causal-graph curation files with 32 graphs validated. |
| Reference validator | Not applicable - this seeded record has no `evidence`, `causal_graphs`, `discussions`, or `datasets` reference block to validate with a focused record-level reference checker. |
| `just term-requests-check` | Pass - committed term-request table is current with 109 terms. |
| `just validate-history` | Pass - 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Pass - expected and found 3,206 records; the corpus reproduces exactly from `data/raw/`. |
| `just worklist --limit 2000` | Pass - worklist generation completed and reported 0 ungrounded records still undecided, with 1,810 decisions on file. |
| `just report` | Pass - corpus report completed for 3,206 records. |
| `git diff --check` | Pass - no whitespace errors. |

## Identity and Grounding

The record identity matches the GOLD source concept:

| Claim | Review |
|---|---|
| Minted ID | Supported. `habitatmech:GOLD.5c3db359b7` is the minted identifier for `Environmental > Aquatic > Deep subsurface > Groundwater > Cave stream sediment`; `data/habitats/PATHS.tsv` maps that ID to `cave_stream_sediment`. |
| GOLD source path | Supported. `gold.ecosystem:7786` has the exact path `Environmental > Aquatic > Deep subsurface > Groundwater > Cave stream sediment` in `data/raw/gold_ecosystem_paths.tsv`. |
| Habitat meaning | Supported. The leaf denotes cave-stream sediment, and the class-sweep sample row explicitly screened this concept as a habitat. |
| Current `UNGROUNDED` status | Too weak. The exact leaf should stay minted because `stream sediment` is broader than cave stream sediment, but vendored `ENVO:00002127` `stream sediment` is a strict broader material term. |
| Current `Groundwater` parent | Incorrect. `habitatmech:GOLD.22a80cbd14` inherits from GOLD's path prefix, but sediment deposited in a cave stream is not a kind of groundwater. |

`ENVO:00002127` is present in `data/raw/ontology_terms.tsv` as `stream
sediment`, exists as `data/habitats/terrestrial/stream_sediment.yaml`, and is a
subclass of `ENVO:00002007` `sediment` in
`data/raw/ontology_subclass_edges.tsv`. GOLD's MIxS triad inventory for this path
independently reports local `ENVO:00000067` `cave` and medium `ENVO:00002007`
`sediment` for all 3 biosamples from one study. That triad is contextual
evidence, not an exact identity decision, but it corroborates that the target is
a cave sediment material rather than groundwater itself.

## Evidence

| Claim | Nearest evidence | Review |
|---|---|---|
| Source attestation uses `gold.ecosystem:7786` and the Cave stream sediment path | `data/raw/gold_ecosystem_paths.tsv` row for `gold.ecosystem:7786` | Supported. The generated `source_id`, `source_label`, and `source_path` agree with the raw GOLD ecosystem-path row. |
| No GOLD assertion count is emitted | `data/raw/gold_ecosystem_paths.tsv` reports 0 KGX organism, sample, and study assertions for this ecosystem node | Supported for the committed GOLD KGX inventory. |
| Cave stream sediment has newer GOLD biosample/triad context | `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_studies.tsv`, and `data/raw/gold_path_triads.tsv` | Present but not yet a generated attestation. Those rows show 3 biosamples from `Gs0149395` and all 3 map to `cave` plus `sediment`; they should be treated as supporting context for curation, not as characteristic taxa or causal evidence. |
| Class-level `CONFIRM_UNGROUNDED` curation history | `curation/decisions.tsv` row for `habitatmech:GOLD.5c3db359b7` | Mechanically reproduced, but the row is insufficient after item review because the source concept is a real habitat with a broader vendored ENVO term. |

The target record has no record-level `evidence`, no environmental parameters, no
characteristic taxa, no causal graph, no discussions, and no datasets. That is
not a schema defect: GOLD is its only generated source, and this exact minted
GOLD concept has no PREGO, BacDive, Madin, or environment-table rows in the
generated record.

## Completeness

- A future item-level curation row is needed in `curation/decisions.tsv`; the
  existing `CLASS` decision deliberately did not assess whether the concept was
  a habitat and cannot promote this source concept to `REVIEWED`.
- A future definition/term request is needed in `curation/term_requests.tsv` if
  the record remains minted. Its authored parent should be `ENVO:00002127`, and
  `parent_mode` should be `REPLACE` because the inherited `Groundwater` parent is
  false for the sediment material.
- Exact, ignored-inclusive searches found no prior
  `*-cave_stream_sediment.md` report, no target-specific causal overlay, no
  research/history filename for `5c3db359b7`, and no research/history filename
  matching a cave-stream slug.

## Findings

| Severity | Finding |
|---|---|
| Major | **`Groundwater` is not a strict broader parent for Cave stream sediment.** `parent_habitats` currently contains `habitatmech:GOLD.22a80cbd14` solely because GOLD nests the leaf under the path prefix `Groundwater`. The reviewed concept denotes deposited material in a cave stream, and vendored `ENVO:00002127` `stream sediment` is already available as a strict broader parent. Owner: replace the class-level row for `habitatmech:GOLD.5c3db359b7` in `curation/decisions.tsv` with item-level `GROUND_AS_PARENT` to `ENVO:00002127`, and add a minted-term definition in `curation/term_requests.tsv` with `parent=ENVO:00002127` and `parent_mode=REPLACE` to prevent the false GOLD parent from regenerating. |

No blocker findings.

No minor findings.

## Recommended Edits

1. In `curation/decisions.tsv`, replace the `habitatmech:GOLD.5c3db359b7`
   class-level `CONFIRM_UNGROUNDED` row with an item-level `GROUND_AS_PARENT`
   row pointing to `ENVO:00002127` `stream sediment`.
2. In `curation/term_requests.tsv`, add a Cave stream sediment definition whose
   genus parent is `ENVO:00002127`, and set `parent_mode` to `REPLACE` so the
   generated record drops `habitatmech:GOLD.22a80cbd14` `Groundwater`.
3. Regenerate the record through `just seed`, `just seed-canary
   habitatmech:GOLD.5c3db359b7`, and `just seed-apply --force`; then verify that
   `data/habitats/aquatic/cave_stream_sediment.yaml` has `grounding_status:
   NARROW`, `mapping_status: REVIEWED`, `parent_habitats: [ENVO:00002127]`, the
   authored definition, and regenerated item-level curation history.

## Follow-up Checks

- `just validate data/habitats/aquatic/cave_stream_sediment.yaml`
- `just validate-strict data/habitats/aquatic/cave_stream_sediment.yaml`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`

## Additional Notes

- Searches establishing absence included ignored files: exact `find` checks
  covered `reports/yaml_record_review`, `curation/causal_graphs`, `research`,
  `reports`, and `history`; exact `rg --no-ignore --hidden` checks covered
  source identifiers, labels, ontology CURIEs, and the GOLD source path while
  excluding high-volume generated `pages/`, `build/`, `data/text_map/`, and
  `.git/` data where appropriate.
- Exact `ENVO:00002127` searches also find the PREGO-sourced generated
  `stream_sediment.yaml` record and PREGO taxon rows for generic stream
  sediment. Those rows confirm that ENVO `stream sediment` is already part of
  the corpus; they are not evidence for Cave stream sediment's characteristic
  taxa.
- The GOLD triad rows for Cave stream sediment are all from one study. They
  corroborate the material/site interpretation but are not independent
  multi-study evidence for exact grounding.
