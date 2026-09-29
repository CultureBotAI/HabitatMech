# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/food/food_production.yaml`
- Started UTC: 2026-09-29T03:06:51Z
- Finished UTC: 2026-09-29T03:06:51Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `HabitatRecord` |
| Identifier | `FOODON:03530206` |
| Label | `food production` |
| Category | `FOOD` |
| Grounding | `EXACT` |
| Mapping | `SEEDED` |
| Source | `GOLD` |
| Source path | `Engineered > Food production` |
| Hidden source key | `habitatmech:GOLD.c3ec8e02e4` |
| Generated path | `data/habitats/food/food_production.yaml` |
| Maintained owner | The review belongs in `curation/decisions.tsv` under the hidden GOLD source key `habitatmech:GOLD.c3ec8e02e4`; any true novel habitat needs a maintained definition and parent override rather than a direct edit to this generated YAML. |

Reviewed the complete generated record at
`data/habitats/food/food_production.yaml`. The record resolves GOLD's
`Engineered > Food production` branch directly to the ontology identity
`FOODON:03530206`.

`data/habitats/PATHS.tsv` maps `FOODON:03530206` to the stable
`food_production` slug. The unmaterialized source-concept key is
`habitatmech:GOLD.c3ec8e02e4`, the deterministic
`mint("GOLD", "Engineered > Food production")` value that
`src/habitatmech/seed.py` uses for curated GOLD decisions before automatic
resolution to any ontology CURIE.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/habitats/food/food_production.yaml` | Pass: LinkML reported `No issues found`. |
| `just validate-strict data/habitats/food/food_production.yaml` | Pass: scanned 1 file with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| Target causal overlay validator | Not applicable: exact ignored/hidden-inclusive searches found no target-specific curated causal overlay for `FOODON:03530206`, `habitatmech:GOLD.c3ec8e02e4`, `gold.ecosystem:2885`, `gold.ecosystem:3502`, `gold.ecosystem:3823`, `gold.ecosystem:4250`, or `Engineered > Food production`. |
| `just validate-causal-all` | Pass: validated 32 causal-graph curation files with 32 graphs. |
| `just term-requests-check` | Pass: the term-request table is current with 109 terms. |
| `just validate-history` | Pass: 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Pass: expected 3,206 records, found 3,206 on disk, and the corpus reproduces exactly from `data/raw/`. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist-food-production.tsv` | Pass: wrote 953 total `UNGROUNDED` rows across all decision states with 1,810 decisions on file. |
| `just report --out /tmp/habitatmech-report-food-production.tsv` | Pass: completed the corpus report for 3,206 records. |
| `git diff --check` | Pass before writing this report. |
| Reference validator | Not applicable: the target has no record-level `evidence`, `characteristic_taxa`, `causal_graphs`, `discussions`, or `datasets` with citation-bearing `EvidenceItem` references. |

## Identity and Grounding

The GOLD source concept is traceable. `data/raw/gold_ecosystem_paths.tsv:16`
has the exact canonical path `Engineered > Food production`, depth 2, leaf label
`Food production`, four collapsed GOLD node IDs, 4,402 direct organism
assertions, no direct study or biosample assertions in that aggregate row, and
source node IDs `gold.ecosystem:2885`, `gold.ecosystem:3502`,
`gold.ecosystem:3823`, and `gold.ecosystem:4250`.

The generated `source_attestations` entry correctly preserves the exact source
path, the first source ID `gold.ecosystem:2885`, `source_label: Food
production`, `mapping_predicate: skos:exactMatch`, `assertion_count: 4402`, and
`assertion_unit: ORGANISM`.

The automatic identity is not a safe habitat identity. The vendored FoodOn
slice labels `FOODON:03530206` as `food production`, but its definition is `A
planned process involving the rearing, manufacture or distribution of food
material.` A planned process is not a microbial habitat, material, site, or
object aggregate. GOLD uses `Engineered > Food production` as a branch for many
food matrices, equipment records, cellars, facility terms, and product bins;
an exact match to the FoodOn process asserts a narrower and different kind of
thing.

The record has no item-level curated decision. The generated YAML has only a
`seed_from_sources` history event, and the exact ignored/hidden-inclusive search
for `habitatmech:GOLD.c3ec8e02e4` under `curation/`, `history/`,
`reports/yaml_record_review/`, `research/`, `conf/`, `data/habitats/PATHS.tsv`,
and `data/raw/` found no maintained row or report keyed to the source concept.

The only generated parent is `habitatmech:GOLD.2acb39dd08`, the top-level GOLD
`Engineered` source path. That parent has only a class-level
`CONFIRM_UNGROUNDED` row in `curation/decisions.tsv:330`, and the row
explicitly says the sweep did not assess whether the concept is a habitat at
all. The earlier `engineered__900b76ad` review already found that this GOLD root
is an unresolved strict parent for depth-2 engineered source paths.

## Evidence

Supported:

- The generated source-path identity and four-node collapse are reproducible
  from `data/raw/gold_ecosystem_paths.tsv:16`.
- The exact source path has one side-channel biosample row in
  `data/raw/gold_path_biosamples.tsv:607` for ecosystem path ID `4250` with 11
  biosamples.
- The exact source path has five single-path rows in
  `data/raw/gold_studies.tsv`, each with one study: `Gs0111475`, `Gs0114546`,
  `Gs0114789`, `Gs0153827`, and `Gs0153978`.
- The generated parent edge to `habitatmech:GOLD.2acb39dd08` is reproducible
  from the GOLD source-path prefix `Engineered`.
- `src/habitatmech/seed.py` links GOLD children to the resolved identifier for
  their immediate source-path parent, so food-production children that do not
  replace their inherited parent can acquire `FOODON:03530206` from this
  automatically exact-grounded record.

Unsupported or over-scoped:

- No maintained `curation/decisions.tsv` row item-reviews whether GOLD's
  `Engineered > Food production` branch is a true habitat, a source grouping,
  a facility class, a food-material superclass, or a manufacturing process.
- No maintained input justifies retyping the broad GOLD source branch as the
  FoodOn planned process named `FOODON:03530206`.
- No maintained input establishes the top-level GOLD `Engineered` root as a
  strict broader habitat for this source concept.

Adjacent ontology evidence:

- FoodOn's `FOODON:03530206` definition makes it a planned process rather than
  a food material or food-production site.
- ENVO has `ENVO:03501318` `hygienic food production area`, an environmental
  system that is part of a food production facility. That proves the vendored
  slice distinguishes food-production areas from the abstract FoodOn process,
  but it is narrower than GOLD's broad `Engineered > Food production` branch.

## Completeness

`find reports/yaml_record_review -maxdepth 1 -type f -name
'*food_production.md' -print` found no prior top-level YAML report for this
file stem. `find` is not filtered by `.gitignore`.

Exact ignored/hidden-inclusive searches over `curation/`, `history/`,
`research/`, `conf/`, `reports/yaml_record_review/`, and the committed raw GOLD
support tables found no authored term request, generated term-request row,
curated causal overlay, append-only history record, label-correspondence
residual, research report, or prior top-level review report keyed to
`habitatmech:GOLD.c3ec8e02e4`, `gold.ecosystem:2885`, `gold.ecosystem:3502`,
`gold.ecosystem:3823`, `gold.ecosystem:4250`, or the exact source path.

Existing `sourdough`, `utensil`, and `food_sample` reviews mention
`FOODON:03530206` only as a false process-valued parent inherited by narrower
GOLD children under `Engineered > Food production`. Those reports reinforce the
same modeling defect from the child side and do not review the hidden
`habitatmech:GOLD.c3ec8e02e4` source concept.

Exact ignored/hidden-inclusive searches found no direct row for
`Engineered > Food production` in `data/raw/gold_path_triads.tsv` or
`data/raw/environment_parameters.tsv`. Child paths under
`Engineered > Food production >` do have submitted MIxS environmental triads,
including fermented dairy, fermented beverage, fermented vegetable, and meat
product rows, but those side-channel rows are child evidence and do not resolve
the parent branch identity.

The empty optional `environmental_parameters`, `characteristic_taxa`,
`evidence`, `causal_graphs`, `discussions`, and `datasets` blocks are not
schema defects. They correctly stay empty until a maintained input supplies
claim-level evidence.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | `FOODON:03530206` is a FoodOn planned process, so it should not be the exact HabitatRecord identity for GOLD's `Engineered > Food production` branch. | The generated record carries `grounding_status: EXACT` and `mapping_predicate: skos:exactMatch` solely from the automatic leaf-label route. The vendored `FOODON:03530206` row defines `food production` as a planned process, while GOLD's branch contains food matrices, equipment, cellars, facility areas, and product bins. A planned process is not a habitat, material, site, or strict broader class for those children. | Add an item-level `curation/decisions.tsv` row for `habitatmech:GOLD.c3ec8e02e4`. Depending on item review, confirm a minted branch, map it to a true site or material parent with `GROUND_AS_PARENT`, merge it with another minted concept using `SAME_AS`, or mark it `NOT_APPLICABLE`; do not keep the process term as exact identity. |
| Major | The generated `parent_habitats` edge points at the unreviewed GOLD `Engineered` root. | `src/habitatmech/seed.py` derives the edge from the `Engineered` source-path prefix. The parent identifier `habitatmech:GOLD.2acb39dd08` has only a class-level `CONFIRM_UNGROUNDED` row whose note says habitathood was not assessed, and no item-level decision establishes it as a strict broader habitat for food production. | Item-review `habitatmech:GOLD.2acb39dd08` in `curation/decisions.tsv`; if the inherited edge is rejected, add maintained support for suppressing or replacing false GOLD source-path parents before seeding serializes `parent_habitats`. |

No minor findings found.

## Recommended Edits

1. Add an item-level `curation/decisions.tsv` row for
   `habitatmech:GOLD.c3ec8e02e4`, the minted key for
   `Engineered > Food production`.
2. Review whether the GOLD branch denotes a broad food-production source
   grouping, a food-production facility or facility area, a food-material
   superclass, or a non-habitat process.
3. Reject the exact identity to `FOODON:03530206` unless review can prove the
   source branch itself means only the planned process rather than the food
   habitats under that process.
4. If the branch stays as a real minted habitat, define it in
   `curation/term_requests.tsv` under a true broader class or add a
   non-identity xref to the nearest broader site or material term.
5. Item-review `habitatmech:GOLD.2acb39dd08` before preserving `Engineered` as
   the strict parent, or add a maintained parent-suppression path if that
   source root is only a structural GOLD grouping.
6. Record the decision and term-request edits in an append-only mapping history
   file with `just new-history`, then re-seed with `just seed`,
   `just seed-canary habitatmech:GOLD.c3ec8e02e4`, and
   `just seed-apply --force`.

## Follow-up Checks

| Edit | Proof |
| --- | --- |
| Item-review the GOLD source branch | `rg --no-ignore --hidden -n '^habitatmech:GOLD\\.c3ec8e02e4\\b' curation/decisions.tsv` should show one `ITEM` row. |
| Remove the process identity | A forced canary for `habitatmech:GOLD.c3ec8e02e4` should show either a minted `habitatmech:GOLD.c3ec8e02e4` record, a curated `SAME_AS` merge into another minted branch, or `NOT_APPLICABLE`; it should not emit `identifier: FOODON:03530206`. |
| Preserve the GOLD attestation if the concept stays applicable | The seeded record should still carry `source_id: gold.ecosystem:2885`, `source_path: Engineered > Food production`, `assertion_count: 4402`, and `assertion_unit: ORGANISM`. |
| Avoid propagating a planned-process parent to children | After the relevant canaries or a full seed, child records under `Engineered > Food production >` should not inherit `FOODON:03530206` as a strict `parent_habitats` edge. |
| Keep the generated corpus reproducible | Run `just verify-corpus --max-diffs 1`, `just validate data/habitats/food/food_production.yaml`, `just validate-strict data/habitats/food/food_production.yaml`, `just validate-causal-all`, `just term-requests-check`, `just validate-history`, `just report`, `just worklist --status all`, and `git diff --check`. |

## Additional Notes

The exact absence searches above included ignored and hidden files. They were
bounded to the committed raw GOLD tables and the maintained curation surfaces
that could plausibly own this target; no search inspected uncommitted external
GOLD API exports.

The false `FOODON:03530206` identity is a systemic food-branch risk. For
narrower children, the second GOLD ingest pass uses the resolved identifier of
the immediate source-path parent as a generated `parent_habitats` edge. Until
`Engineered > Food production` stops resolving exactly to a planned process,
children under that branch can inherit the same process as an `is-a` parent.
