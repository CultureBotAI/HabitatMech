# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/photobioreactor.yaml
- Started UTC: 2026-09-25T01:50:00Z
- Finished UTC: 2026-09-25T01:53:21Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `ENVO:03600077` |
| Label | `photobioreactor` |
| Category | `ENGINEERED` |
| Grounding status | `EXACT` |
| Mapping status | `REVIEWED` |
| Generated path | `data/habitats/engineered/photobioreactor.yaml` |
| Path lock | `data/habitats/PATHS.tsv:946` maps `ENVO:03600077` to `photobioreactor` |

The file is generated from the committed source inventories and two item-level `GROUND` decisions in `curation/decisions.tsv`. Future fixes belong in `curation/decisions.tsv` and in future source-path parent suppression support, not in `data/habitats/engineered/photobioreactor.yaml` or the generated rendered page.

The merged record is fed by two GOLD source concepts:

| Source concept | Maintained decision | Source path | GOLD row |
|---|---|---|---|
| `habitatmech:GOLD.e5b2473bf3` | `curation/decisions.tsv:1267` | `Engineered > Bioreactor > Photobioreactor (PBR)` | `data/raw/gold_ecosystem_paths.tsv:884`; 3 GOLD node ids, 1 organism assertion |
| `habitatmech:GOLD.96bbd55dce` | `curation/decisions.tsv:876` | `Engineered > Artificial ecosystem > Aquaculture > Photobioreactor (PBR)` | `data/raw/gold_ecosystem_paths.tsv:1129`; 2 GOLD node ids, 0 assertions |

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/engineered/photobioreactor.yaml` | Pass; `linkml-validate` reported no issues. |
| `just validate-strict data/habitats/engineered/photobioreactor.yaml` | Pass; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Pass; term-request table is current with 109 terms. |
| `just validate-history` | Pass; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Pass; 3,206 expected records, 3,206 on disk, 0 missing, 0 extra, 0 differing. |
| `just worklist --limit 2000` | Pass; 0 undecided ungrounded records and 1,810 decisions on file. |
| `just report` | Pass; corpus report completed and the corpus still contains 3,206 records. |

## Identity and Grounding

- `ENVO:03600077` is present in the vendored ontology table as `photobioreactor`, defined as "A bioreactor which utilizes a light source to cultivate phototrophic microorganisms."
- `data/raw/ontology_subclass_edges.tsv` asserts `ENVO:03600077 rdfs:subClassOf ENVO:00002123`, so the generated ontology parent `ENVO:00002123` `bioreactor` is supported.
- Both GOLD source labels are exactly `Photobioreactor (PBR)`. The `PBR` parenthetical is only an acronym and does not narrow either source path away from ENVO's `photobioreactor`.
- Both contributing source concepts have item-level `GROUND` rows to `ENVO:03600077` with expected label `photobioreactor`. That is enough for the generated merged record to become `mapping_status: REVIEWED`.
- The GOLD synonym `Photobioreactor (PBR)` is a supported exact synonym for the ontology label.
- The second generated parent, `habitatmech:GOLD.0287e1b2a9`, is the minted GOLD parent for `Engineered > Artificial ecosystem > Aquaculture`; it is not an ontology ancestor of `ENVO:03600077`, and it is not a strict broader class of generic photobioreactors.

## Evidence

- The two `source_attestations` agree with `data/raw/gold_ecosystem_paths.tsv`: the Bioreactor path row lists `gold.ecosystem:5844|gold.ecosystem:8184|gold.ecosystem:8185` with one organism assertion, and the generated attestation correctly shows the first source ID and `assertion_count: 1`; the Aquaculture path row lists `gold.ecosystem:7996|gold.ecosystem:7997` with zero assertions, and the generated attestation correctly omits `assertion_count`.
- No record-level literature evidence is present or required. This is a seeded GOLD record with its habitat identity supplied by source attestations and reviewed grounding decisions.
- No causal graph is present. An ignored-inclusive exact search for `ENVO:03600077` over `curation`, `data/habitats`, `data/raw`, `reports`, `history`, `research`, `conf/id_label_targets.yaml`, and `pages` found the target YAML, the generated target page, the path lock, the two source decisions, the two ontology rows, the photobioreactor biofilm child that uses `ENVO:03600077` as a parent, and prior review mentions; it found no `curation/causal_graphs/` overlay targeting this record.

## Completeness

- The record is complete enough for the two GOLD source identities: the ontology ID, label, definition, exact synonym, exact GOLD attestations, `GROUND` decisions, and `REVIEWED` mapping status all agree.
- The generated `ENVO:00002123` parent is supported by the ontology subclass edge and is complete.
- Empty `environmental_parameters`, `characteristic_taxa`, `evidence`, `causal_graphs`, `discussions`, and `datasets` are acceptable for this GOLD-only record. Exact ignored-inclusive searches for `ENVO:03600077`, `Photobioreactor (PBR)`, and the two source paths found no maintained target-specific parameter, taxon, evidence, or causal-overlay inputs beyond the two `curation/decisions.tsv` rows.
- The `Aquaculture` source-path parent is not complete because the current representation has no maintained way to express that the Aquaculture-path source concept should merge into the generic ENVO photobioreactor without making every ENVO photobioreactor a child of the generated Aquaculture record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The exact-grounded merged record has a false inherited `Aquaculture` parent. | `parent_habitats` includes `habitatmech:GOLD.0287e1b2a9` beside the true ontology parent `ENVO:00002123`. The Aquaculture parent comes only from the zero-assertion GOLD path `Engineered > Artificial ecosystem > Aquaculture > Photobioreactor (PBR)`. `ENVO:03600077` denotes any light-driven bioreactor for phototrophic microorganisms, and its vendored ontology parent is `ENVO:00002123` `bioreactor`; it is not a kind of `habitatmech:GOLD.0287e1b2a9` `Aquaculture` or `ENVO:03600074` `aquaculture farm`. `parent_habitats` must mean strictly broader. | Future source-path parent suppression support in `src/habitatmech/seed.py` plus an explicit maintained row keyed to `habitatmech:GOLD.96bbd55dce`, or an equivalent curation-owned input that can drop one inherited GOLD parent without hand-editing generated YAML. |
| Minor | The Aquaculture-path `GROUND` decision has a malformed path literal in its note. | `curation/decisions.tsv:876` says `Path: Engineered > Artificial ecosystem > Aquaculture > Photobioreactor (PBR` without the closing `)`. The generated `curation_history` therefore serializes `Path: Engineered > Artificial ecosystem > Aquaculture > Photobioreactor (PBR (source concept habitatmech:GOLD.96bbd55dce)`, which reads as though the source path itself is malformed. | `curation/decisions.tsv` |

No blocker findings.

## Recommended Edits

1. Add or use maintained support for suppressing a false GOLD source-path parent on an exact-grounded merged ontology record, then apply it to `habitatmech:GOLD.96bbd55dce` so `ENVO:03600077` keeps `ENVO:00002123` and no longer inherits `habitatmech:GOLD.0287e1b2a9`.
2. Correct the note for `habitatmech:GOLD.96bbd55dce` in `curation/decisions.tsv` so the `Path:` clause exactly names `Engineered > Artificial ecosystem > Aquaculture > Photobioreactor (PBR)`.

## Follow-up Checks

- After adding the maintained parent-suppression input, run `just seed`, `just seed-canary ENVO:03600077`, inspect `data/habitats/engineered/photobioreactor.yaml`, then run `just seed-apply --force`.
- Re-run `just validate data/habitats/engineered/photobioreactor.yaml`, `just validate-strict data/habitats/engineered/photobioreactor.yaml`, `just verify-corpus --max-diffs 1`, `just validate-causal-all`, `just validate-history`, `just term-requests-check`, and `just report`.
- Confirm the regenerated photobioreactor record contains `ENVO:00002123` in `parent_habitats`, does not contain `habitatmech:GOLD.0287e1b2a9`, keeps both `GOLD` source attestations, and keeps `mapping_status: REVIEWED`.
- Re-render the site and confirm `pages/habitats/photobioreactor-envo-03600077.html` no longer links `Aquaculture` as a parent and no longer contains the malformed Aquaculture-path curation-history text.

## Additional Notes

- Searches that established absence were run with `rg --no-ignore --hidden` over the maintained curation inputs, generated habitat records, raw source inventories, history, research, prior review reports, rendered pages, and relevant config. The huge `pages/text-map` and `data/text_map` products were deliberately excluded.
- The prior Aquaculture review already called this exact photobioreactor parent out as an example of a contextual source-path parent leaking into an exact-grounded merged ontology record. This record-level review confirms that issue on the generated target itself.
