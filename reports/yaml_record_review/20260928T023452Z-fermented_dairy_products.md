# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/food/fermented_dairy_products.yaml`
- Started UTC: 2026-09-28T02:34:52Z
- Finished UTC: 2026-09-28T02:34:52Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.4a2834cfef` |
| Label | `Fermented dairy products` |
| Category | `FOOD` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Generated path | `data/habitats/food/fermented_dairy_products.yaml` |
| GOLD path | `Engineered > Food production > Dairy products > Fermented dairy products` |

The target is a generated, GOLD-only food record. It has one GOLD source
attestation, one generated parent, no definition, no synonyms or xrefs, no
environmental parameters, no characteristic taxa, no record-level evidence, no
causal graphs, no discussions, and no datasets.

This record is generated from `data/raw`, `data/habitats/PATHS.tsv`, and
`curation/decisions.tsv`; future item-level grounding or minting decisions
belong in maintained curation inputs followed by regeneration, not in this YAML
file.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/food/fermented_dairy_products.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/food/fermented_dairy_products.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows; wrote `reports/instance_validation_failures.tsv`. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --status all --out /tmp/habitatmech-fermented-dairy-products-worklist.tsv` | Passed; wrote 953 ungrounded rows and listed this target with 178 assertions from `GOLD`. |
| `just report --out /tmp/habitatmech-fermented-dairy-products-report.tsv` | Passed; wrote 3206 corpus rows and listed this target with 1 `GOLD` source, 178 source assertions, 1 parent, 0 environmental parameters, 0 characteristic taxa, and 0 causal graphs. |

No required validator was skipped. The target has no causal graph, no
record-local `EvidenceItem`, and no dataset reference for a narrower
record-local reference validator to inspect.

## Identity and Grounding

The generated identifier, label, category, GOLD source ID, and curation history
agree with the committed source inventory:

- `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.4a2834cfef` to
  `fermented_dairy_products`.
- `data/raw/gold_ecosystem_paths.tsv` has one exact aggregate row for
  `Engineered > Food production > Dairy products > Fermented dairy products`.
- The exact aggregate row records GOLD nodes `gold.ecosystem:5455` and
  `gold.ecosystem:5456` with 178 organism assertions.
- `data/raw/gold_path_biosamples.tsv` has 16 biosamples for the same canonical
  path at node `5456`.
- `data/raw/gold_studies.tsv` references the same canonical path in three
  studies.
- No exact `data/raw/gold_path_triads.tsv` row exists for this path; the only
  `Fermented dairy products` triad rows belong to the narrower child Cheese
  path.

The exact GOLD ecosystem-path row has:

| Column | Value |
|---|---|
| `canonical_path` | `Engineered > Food production > Dairy products > Fermented dairy products` |
| `ecosystem` | `Engineered` |
| `ecosystem_category` | `Food production` |
| `ecosystem_type` | `Dairy products` |
| `ecosystem_subtype` | `Fermented dairy products` |
| `specific_ecosystem` | empty |
| `leaf_label` | `Fermented dairy products` |
| `depth` | `4` |
| `gold_node_count` | `2` |
| `organism_count` | `178` |
| `study_count` | `0` |
| `biosample_count` | `0` |
| `total_assertions` | `178` |
| `gold_node_ids` | `gold.ecosystem:5455\|gold.ecosystem:5456` |

The source node denotes a microbial habitat under GOLD's food-production
hierarchy and is narrower than both `FOODON:00001256` `dairy food product` and
`FOODON:00001258` `food (fermented)`. The current direct parent
`FOODON:00001256` is therefore true but not sufficient to describe the term to
mint.

No exact vendored ontology term for generic fermented dairy products was found.
The hidden/ignored-inclusive lexical and CURIE searches found exact FoodOn
coverage for dairy food products, cheese, fermented food, and fermented meat
products, but not a generic fermented-dairy term. The ungrounded worklist still
offers only two candidate IDs for this record: `FOODON:00001314`, which is the
wrong meat matrix, and `FOODON:00001879`, which is a frozen dairy product rather
than a fermented dairy product.

## Evidence

| YAML claim | Maintained evidence | Review |
|---|---|---|
| `identifier: habitatmech:GOLD.4a2834cfef` | `data/habitats/PATHS.tsv` pins the generated minted ID to `fermented_dairy_products`. | Supported. |
| `label: Fermented dairy products` | The exact `data/raw/gold_ecosystem_paths.tsv` row has `leaf_label` `Fermented dairy products`. | Supported as the GOLD source label. |
| `habitat_category: FOOD` | The GOLD source path starts with `Engineered > Food production`. | Supported. |
| GOLD `source_attestations` fields | The exact `data/raw/gold_ecosystem_paths.tsv` row records the path, the first GOLD node ID `gold.ecosystem:5455`, two node IDs total, and 178 organism assertions. | Supported. |
| `grounding_status: UNGROUNDED` | Hidden/ignored-inclusive searches of the vendored FoodOn slice found no exact generic fermented-dairy term, and `curation/decisions.tsv` carries a class-level `CONFIRM_UNGROUNDED` row for `habitatmech:GOLD.4a2834cfef`. | Supported as a lexical starting point, but incomplete: the row explicitly did not assess whether the concept is a habitat or a term-request candidate. |
| `parent_habitats: FOODON:00001256` | `FOODON:00001256` is the reviewed exact grounding for GOLD `Engineered > Food production > Dairy products`; the ontology labels it `dairy food product`. | Supported as a broader parent. |
| missing `FOODON:00001258` parent | `FOODON:00001258` is the vendored class `food (fermented)`, and the reviewed exact `fermented meat product` record already uses it as the cross-axis parent for a food product subjected to fermentation. | Unsupported omission: fermented dairy products are also fermented foods, so the item-level curated minted term should use `FOODON:00001258` as a parent while preserving the GOLD-inherited `FOODON:00001256` dairy parent. |
| Seeded `curation_history` | The record has the normal `seed_from_sources` event dated `2026-08-16T05:58:02Z`; `curation/decisions.tsv` has the class-level sweep row dated `2026-08-12`. | Supported as generated provenance, not as item-level curator review. |

The generated child `data/habitats/food/cheese.yaml` is consistent with this
target. GOLD's `Cheese` path is an exact child of
`Engineered > Food production > Dairy products > Fermented dairy products`, and
FoodOn asserts both `FOODON:03000287` `cheese` as a subclass of
`FOODON:00001013` `cheese food product` and `FOODON:00001013` as a subclass of
`FOODON:00001256` `dairy food product`.

## Completeness

Exact hidden/ignored-inclusive searches for
`habitatmech:GOLD.4a2834cfef`, `4a2834cfef`,
`fermented_dairy_products`, `Fermented dairy products`,
`gold.ecosystem:5455`, `gold.ecosystem:5456`, and the exact canonical GOLD
path covered `data/habitats`, `data/raw`, `curation`, `history`, `research`,
`reports`, `conf`, `src`, `tests`, `docs`, `.claude`, the `justfile`, and
`README.md`. They found:

- the generated target;
- the generated `data/habitats/PATHS.tsv` row;
- one class-level decision row in `curation/decisions.tsv`;
- exact GOLD rows in `data/raw/gold_ecosystem_paths.tsv`,
  `data/raw/gold_path_biosamples.tsv`, and `data/raw/gold_studies.tsv`;
- the Cheese child and child-only Cheese triad rows;
- the exact reviewed `FOODON:00001256` dairy parent; and
- no item-level decision row, term-request row, causal overlay, history record,
  or prior exact YAML review report for this target.

Hidden/ignored-inclusive searches for `FOODON:00001256`, `FOODON:00001258`,
`FOODON:00001314`, `FOODON:00001879`, `fermented dairy`, `yogurt`, and
`yoghurt` found no exact generic fermented-dairy term in the vendored
`data/raw/ontology_terms.tsv` slice. They did find the broader
`FOODON:00001256` `dairy food product` and `FOODON:00001258`
`food (fermented)` terms, the exact `FOODON:00001314`
`fermented meat product` sibling, narrower cheese terms, and frozen-dairy
near misses.

The target's empty characteristic-taxon, environmental-parameter,
causal-graph, discussion, and dataset slots are expected for a generated
one-source GOLD leaf. The consequential gaps are the lack of an item-level
grounding decision, a definition, curated synonyms, and a maintained request
that would mint the missing class under the right food-product parents.

## Findings

### Blocker

None found.

### Major

| ID | Finding | Maintained owner |
|---|---|---|
| M1 | `data/habitats/food/fermented_dairy_products.yaml` is still only class-swept: it records `UNGROUNDED` from a 2026-08-12 lexical sweep whose history text explicitly says nobody assessed whether the GOLD concept is a habitat or term-request candidate. The source is a real GOLD food-production node with 178 organism assertions and a true child, Cheese; no vendored exact term was found; and the item-level record needs to be promoted to a reviewed HabitatMech concept under `FOODON:00001258` `food (fermented)` while preserving the existing `FOODON:00001256` `dairy food product` ancestry. | `curation/decisions.tsv`; `curation/term_requests.tsv` |

### Minor

None found.

## Recommended Edits

1. Add item-level curation for `habitatmech:GOLD.4a2834cfef` that keeps the
   record minted and `UNGROUNDED`, confirms that the exact GOLD source concept
   is a valid habitat, and authors a definition for the missing class.
2. Model the minted class as a fermented food under
   `FOODON:00001258` `food (fermented)`. Leave
   `FOODON:00001256` `dairy food product` in `parent_habitats` because GOLD's
   source hierarchy already supplies the dairy-product axis.
3. Keep `Fermented dairy products` as the source-attested exact synonym from
   GOLD and avoid grounding to near misses: `FOODON:00001314` is fermented meat,
   and the frozen-dairy FoodOn terms do not imply fermentation.
4. Regenerate and inspect the canary:

```bash
just seed
just seed-canary habitatmech:GOLD.4a2834cfef
just seed-apply --force --prune
```

5. Confirm `data/habitats/food/fermented_dairy_products.yaml` is `REVIEWED`,
   has a `HabitatMech` definition, keeps the GOLD source attestation, and has
   both `FOODON:00001256` and `FOODON:00001258` as parents.

## Follow-up Checks

After the item-level decision and generated outputs are updated:

```bash
just validate data/habitats/food/fermented_dairy_products.yaml
just validate-strict data/habitats/food/fermented_dairy_products.yaml
just verify-corpus
just validate-causal-all
just validate-history
just term-requests-check
just report --out /tmp/habitatmech-fermented-dairy-products-report.tsv
git diff --check
```

Manually check the regenerated record for:

- `mapping_status: REVIEWED`;
- `grounding_status: UNGROUNDED` with a `HabitatMech` definition rather than
  only a class-level lexical sweep;
- `parent_habitats` containing both `FOODON:00001256` and
  `FOODON:00001258`;
- a retained `GOLD` attestation with `source_id: gold.ecosystem:5455` and
  `source_path: Engineered > Food production > Dairy products > Fermented dairy products`;
- a `just report` row for `habitatmech:GOLD.4a2834cfef` that is still one
  `GOLD` source with 178 upstream assertions.

## Additional Notes

The committed deep-research report for the broader BacDive/Madin fermented-food
record mentions unvendored FoodOn fermented-milk terms as narrower concepts with
regulatory-classification baggage. I treated that as a lead, not as target
evidence: this review stayed inside vendored local data and did not perform new
paid research or inspect unvendored FoodOn.
