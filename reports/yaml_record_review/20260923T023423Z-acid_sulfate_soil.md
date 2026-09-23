# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/terrestrial/acid_sulfate_soil.yaml`
- Started UTC: 2026-09-23T02:15:00Z
- Finished UTC: 2026-09-23T02:34:23Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/habitats/terrestrial/acid_sulfate_soil.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.6d518b2c16` |
| Label | `Acid sulfate soil` |
| Habitat category | `TERRESTRIAL` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Record status | Generated from one GOLD source concept and one class-level `CONFIRM_UNGROUNDED` sweep decision |
| GOLD source id | `gold.ecosystem:7792` |
| GOLD source path | `Environmental > Terrestrial > Soil > Coastal area > Acid sulfate soil` |
| Decision row | `curation/decisions.tsv:653` |
| Class-sweep sample row | `curation/samples/class_swept_unscreened-20260814.tsv:18` |
| Locked slug | `data/habitats/PATHS.tsv:2096` maps `habitatmech:GOLD.6d518b2c16` to `acid_sulfate_soil` |

This is the generated record for GOLD's `Environmental > Terrestrial > Soil > Coastal area > Acid sulfate soil` path. The source-concept key is reproducible as `habitatmech:GOLD.6d518b2c16` from `sha1("GOLD:Environmental > Terrestrial > Soil > Coastal area > Acid sulfate soil")[:10]`.

The record is valid and preserves the GOLD path, but it is not yet item-reviewed. Its only maintained decision is the August 12, 2026 class-level sweep row, which explicitly did not assess whether the concept is a real habitat or a term-request candidate. The August 14 sample audit later confirmed that Acid sulfate soil is a habitat, but that sample row is not an item-level curation decision and does not supply a definition, broader parent, or term request.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/habitats/terrestrial/acid_sulfate_soil.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/terrestrial/acid_sulfate_soil.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; validated 32 causal-graph curation files with 32 graphs. |
| `just term-requests-check` | Passed; the term-request table is current at 109 generated terms. |
| `just validate-history` | Passed; 77 history records validated. |
| `just verify-corpus --max-diffs 1` | Passed; all 3,206 expected records reproduced exactly from `data/raw/`, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --limit 2000` | Passed; reported 0 undecided ungrounded records and 1,810 decisions on file. This record is absent because the worklist counts class-level decisions as decided; absence from that report is not evidence of item review. |
| `just report` | Passed; the corpus summary still reports 0 risky groundings not yet reviewed, 0 class-level sweeps contradicted by the current slice, 0 swept concepts whose path names a term the leaf does not, and 0 current organism/process habitat claims. |
| `git diff --check` | Passed before this report was written. |

## Identity and Grounding

The generated source identity is reproducible. `data/raw/gold_ecosystem_paths.tsv:1640` has exactly one node for `Environmental > Terrestrial > Soil > Coastal area > Acid sulfate soil`, with `gold.ecosystem:7792` and 0 upstream organism, study, biosample, or total assertions. `data/habitats/terrestrial/acid_sulfate_soil.yaml:1-25` preserves the minted identifier, GOLD source id, source label, source path, and `UNGROUNDED` status expected for a source concept with no exact vendored ontology term.

The locked slug is correct: `data/habitats/PATHS.tsv:2096` maps `habitatmech:GOLD.6d518b2c16` to `acid_sulfate_soil`. The pre-report exact check `find reports/yaml_record_review -maxdepth 1 -type f -name '*-acid_sulfate_soil.md' -print` returned no previous exact report, and `find` includes ignored files below the checked directory.

The record is still seeded rather than reviewed. `curation/decisions.tsv:653` is a `CONFIRM_UNGROUNDED` decision with `review_depth: CLASS` and no `object_id`, `object_label`, `category`, or `relation`, and the generated history in `data/habitats/terrestrial/acid_sulfate_soil.yaml:13-25` preserves the warning that habitat identity was not assessed. `curation/samples/class_swept_unscreened-20260814.tsv:18` subsequently records Acid sulfate soil as "ok" because it is a place, material, or site an organism can be isolated from; however, that audit sample does not convert the class sweep to `review_depth: ITEM`, does not select a broader genus, and does not define the requested term.

The current generated parent is a false is-a parent for this leaf. `data/habitats/terrestrial/acid_sulfate_soil.yaml:6-7` lists `ENVO:00000303`; `data/habitats/PATHS.tsv:550` maps that CURIE to `sea_coast`; and the vendored ENVO row defines `sea coast` as the general region that extends inland from the sea. Acid sulfate soil may occur in coastal settings, and GOLD nested this source below `Soil > Coastal area`, but a sulfate soil is a soil material, not a kind of coastal region. `ENVO:00001998` `soil` is present in the vendored slice and is a strict broader genus for the requested acid sulfate soil term.

The local MIxS triads reinforce the soil interpretation without supporting exact ontology grounding. `data/raw/gold_path_triads.tsv:968-970` reports nine biosamples from one study for the Acid sulfate soil path; all local triads map to `ENVO:01001785` `land`, all broad triads map to `ENVO:00000446` `terrestrial biome`, and the top medium term is `ENVO:00001998` `soil` across two distinct medium terms. That is enough to show GOLD submitters treated these Acid sulfate soil samples as soil-associated, but the multiple medium terms mean the triads do not identify a narrower exact class.

## Evidence

| Claim | Source | Assessment |
| --- | --- | --- |
| The record represents the GOLD path `Environmental > Terrestrial > Soil > Coastal area > Acid sulfate soil`. | `data/raw/gold_ecosystem_paths.tsv:1640`; `data/habitats/terrestrial/acid_sulfate_soil.yaml:8-12` | Supported exactly. |
| The GOLD ecosystem path has one node id and no raw organism, study, biosample, or total assertions in `gold_ecosystem_paths.tsv`. | `data/raw/gold_ecosystem_paths.tsv:1640` | Supported exactly. |
| The same GOLD path appears in `gold_path_biosamples.tsv`, `gold_studies.tsv`, and `gold_path_triads.tsv` as a path with nine biosamples from one study. | `data/raw/gold_path_biosamples.tsv:653`; `data/raw/gold_studies.tsv:2110`; `data/raw/gold_path_triads.tsv:968-970` | Supported. These derived inventories give local sample context but do not make Acid sulfate soil exact-match any vendored term. |
| No term in the vendored slice exactly fits Acid sulfate soil. | `curation/decisions.tsv:653`; pre-report ignored/hidden-inclusive exact term searches over `data/raw/ontology_terms.tsv`, `curation/term_requests.tsv`, `curation/term_requests_excluded.tsv`, and `curation/external_xrefs.tsv` | Partly supported. The exact searches found no exact acid-sulfate or acid-sulphate soil term in maintained local term tables, but the maintained decision is only a class-level lexical sweep and did not assess the source as a term-request candidate. |
| Acid sulfate soil is a real habitat source concept. | `curation/samples/class_swept_unscreened-20260814.tsv:18`; GOLD source path in `data/raw/gold_ecosystem_paths.tsv:1640` | Supported enough for item-level curation. The record still needs a maintained item-level decision and term request before it can become `REVIEWED`. |
| `ENVO:00000303` `sea coast` is a valid broader parent for Acid sulfate soil. | Generated parent inherited from the GOLD source path in `data/habitats/terrestrial/acid_sulfate_soil.yaml:6-7` | Unsupported. The parent represents the source-path `Coastal area` bucket, but a soil subtype is not a kind of sea coast. |

Unsupported or over-scoped generated claims: the only material unsupported claim is the inherited `sea coast` parent. The generated record has no definition, environmental parameters, characteristic taxa, causal graphs, discussions, or datasets, so this review did not need to assess parameter ranges, taxon typicality, causal edge evidence, or dataset relevance.

## Completeness

The record has the expected source attestation and a locked path, but it lacks the item-level curation inputs needed for a source concept that has already been sampled and judged to be a valid habitat. It still needs an `ITEM` decision in `curation/decisions.tsv` to supersede the class-level sweep, plus a `curation/term_requests.tsv` row that defines an acid sulfate soil class under `ENVO:00001998` and replaces the false inherited `sea_coast` parent.

Exact ignored/hidden-inclusive content searches for `habitatmech:GOLD.6d518b2c16`, `gold.ecosystem:7792`, `Acid sulfate soil`, `acid_sulfate_soil`, and the full GOLD source path covered `curation`, `data/raw`, `data/habitats/PATHS.tsv`, `history`, `research/habitats`, and `reports/yaml_record_review`, excluding only generated `data/text_map/**`, `pages/**`, and `build/**`. They found only the locked slug, raw GOLD rows, derived path-biosample/study/triad rows, the class-level decision, and the August 14 class-swept sample row; they found no target-specific term request, history record, research report, causal graph, or existing review report.

Filename searches for `*acid_sulfate*`, `*acid-sulfate*`, `*6d518b2c16*`, and `*7792*` under `curation/causal_graphs`, `history`, `research/habitats`, and `reports/yaml_record_review` also returned no target-specific maintained artifact. Those `find` searches include ignored files under the checked directories.

The missing causal overlay is not a correctness gap. This seeded record asserts no causal mechanism, and HabitatMech does not require a causal graph for every valid habitat term-request candidate.

## Findings

No blocker findings.

Major findings:

1. `curation/decisions.tsv:653` is only a class-level ungrounded sweep for a source concept that is already known to be a habitat.

   The row's note says the sweep did not assess whether `habitatmech:GOLD.6d518b2c16` is a habitat or a term-request candidate. `curation/samples/class_swept_unscreened-20260814.tsv:18` later sampled this exact source concept and marked it "ok"; however, because no maintained `ITEM` decision or term request exists, `data/habitats/terrestrial/acid_sulfate_soil.yaml:4-25` is still `UNGROUNDED`, `SEEDED`, and generated from the original class-level warning. The maintained owner is `curation/decisions.tsv`, with the actual acid-sulfate-soil definition and genus owned by `curation/term_requests.tsv`.

2. `data/habitats/terrestrial/acid_sulfate_soil.yaml:6-7` inherits `ENVO:00000303` `sea coast` as a false broader parent.

   `sea coast` is a coastal region, while acid sulfate soil is a kind of soil. The raw GOLD path explains how the bad is-a edge was introduced: the source path places Acid sulfate soil below a `Coastal area` grouping between `Soil` and the leaf. The future term-request row should therefore use `ENVO:00001998` `soil` as the broader parent and `parent_mode=REPLACE` so regeneration drops `sea_coast` instead of keeping it beside the correct soil parent. The maintained owner is `curation/term_requests.tsv`.

No minor findings.

## Recommended Edits

1. Update the existing `habitatmech:GOLD.6d518b2c16` row in `curation/decisions.tsv` from a class-level sweep to an item-level `CONFIRM_UNGROUNDED` decision after a focused term search confirms that the current vendored slice still lacks an exact Acid sulfate soil class.

2. Add a `curation/term_requests.tsv` row for Acid sulfate soil with `parent_class` `ENVO:00001998`, a soil-specific definition from a durable authority or the primary literature, useful exact synonyms such as the sulphate spelling if supported, a note explaining that GOLD's `Coastal area` bucket is locational context, and `parent_mode=REPLACE`.

3. Regenerate from the maintained inputs so `data/habitats/terrestrial/acid_sulfate_soil.yaml` becomes an ungrounded but `REVIEWED` term-request record with `soil` as its broader parent and no inherited `sea_coast` parent.

4. Add a short history record for the item-level curation pass so later reviewers can distinguish the August 12 class sweep, the August 14 sample audit, and the future exact curation decision.

## Follow-up Checks

After applying the maintained curation edits, rerun:

- `just seed`
- `just seed-canary habitatmech:GOLD.6d518b2c16`
- `just validate data/habitats/terrestrial/acid_sulfate_soil.yaml`
- `just validate-strict data/habitats/terrestrial/acid_sulfate_soil.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`

Manually confirm after regeneration that:

- `data/habitats/terrestrial/acid_sulfate_soil.yaml` has `mapping_status: REVIEWED`.
- The generated `parent_habitats` list contains `ENVO:00001998` and does not contain `ENVO:00000303`.
- The generated curation history contains an item-level decision for `habitatmech:GOLD.6d518b2c16`.

## Additional Notes

- The pre-report exact record check found exactly one generated target at `data/habitats/terrestrial/acid_sulfate_soil.yaml`.
- The pre-report exact report check `find reports/yaml_record_review -maxdepth 1 -type f -name '*-acid_sulfate_soil.md' -print` returned no previous exact report; `find` includes ignored files.
- Exact ignored/hidden-inclusive local searches found no exact Acid sulfate soil class in `data/raw/ontology_terms.tsv`, `curation/term_requests.tsv`, `curation/term_requests_excluded.tsv`, or `curation/external_xrefs.tsv`.
- The `just report` output lists 830 class-swept ungrounded records. Acid sulfate soil remains part of that backlog rather than the smaller risky-grounding or organism/process correction sets.
