# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/activated_sludge__a6d16f1c.yaml
- Started UTC: 2026-09-23T09:08:33Z
- Finished UTC: 2026-09-23T09:08:33Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.43c33f3ecc` |
| Label | `Activated sludge` |
| Path | `data/habitats/engineered/activated_sludge__a6d16f1c.yaml` |
| Category | `ENGINEERED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Generated or maintained | Generated from `data/raw/gold_ecosystem_paths.tsv`, lexical ENVO grounding, and `data/habitats/PATHS.tsv`; not a maintained curation input |
| Source concept | GOLD `gold.ecosystem:5592`, first node for `Engineered > Sewage treatment plant > Wastewater > Activated sludge` |
| Locked slug | `data/habitats/PATHS.tsv:1799` maps `habitatmech:GOLD.43c33f3ecc` to `activated_sludge__a6d16f1c` |

I read the full generated record. It contains only generated identity,
category, grounding status, two parents, one GOLD source attestation, and the
initial `SEEDED_FROM_SOURCES` history event. It has no generated definition,
synonyms, environmental parameters, characteristic taxa, evidence items,
causal graphs, discussions, or dataset links.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/engineered/activated_sludge__a6d16f1c.yaml` | Pass: `No issues found` |
| `just validate-strict data/habitats/engineered/activated_sludge__a6d16f1c.yaml` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate-causal-all` | Pass: 32 causal-graph curation files and 32 graphs validated |
| `just term-requests-check` | Pass: `term-request table is current (109 terms)` |
| `just validate-history` | Pass: `No issues found`; 77 history records valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Pass: expected 3,206 records, found 3,206 on disk, 0 missing, 0 extra, 0 differing |
| `just worklist --limit 2000` | Pass: 0 ungrounded records still undecided; 1,810 decisions on file |
| `just report` | Pass: corpus report completed for 3,206 records |
| `git diff --check` | Pass |
| Reference validator | Not applicable: the target has no `evidence`, `causal_graphs`, or reference-bearing maintained overlay to validate |

## Identity and Grounding

The target is a minted GOLD-path record for `Engineered > Sewage treatment
plant > Wastewater > Activated sludge`. `data/raw/gold_ecosystem_paths.tsv:1348`
contains exactly that path, gives it the label `Activated sludge`, records depth
`4`, records two collapsed GOLD ecosystem node IDs
`gold.ecosystem:5592|gold.ecosystem:5593`, and supports the generated
attestation note that two GOLD ecosystem node IDs share the same path.

The source path is used by GOLD studies and biosamples even though the collapsed
ecosystem-path row itself has zero assertion counts: `data/raw/gold_studies.tsv`
lists the child path for `Gs0114680`, `Gs0150737`, and `Gs0153767`, and
`data/raw/gold_path_biosamples.tsv:761` records five biosamples for node `5593`
on the same path. The generated source attestation intentionally omits
`assertion_count`, so it does not overstate those path-biosample rows as
organism counts.

The ontology parent is supported. `data/raw/ontology_terms.tsv:7191` gives
`ENVO:00002046` the canonical label `activated sludge`, and
`data/raw/ontology_subclass_edges.tsv:5293` places it under `ENVO:00002044`;
`data/raw/ontology_terms.tsv:7189` labels `ENVO:00002044` as `sludge`. That
supports keeping the GOLD path minted and carrying the generic activated-sludge
material as a broader parent.

The source-path parent is unsupported. `data/habitats/PATHS.tsv:1686` maps
`habitatmech:GOLD.353a834cfd` to `wastewater__05daf28f`, and
`data/habitats/engineered/wastewater__05daf28f.yaml` is the seeded record for
`Engineered > Sewage treatment plant > Wastewater`. Its GOLD source row is
`data/raw/gold_ecosystem_paths.tsv:284`, which labels the concept `Wastewater`
and collapses `gold.ecosystem:5521|gold.ecosystem:5522|gold.ecosystem:5523`.
`data/raw/ontology_terms.tsv:7166` labels `ENVO:00002001` as `waste water`.
Activated sludge is a sludge material used in wastewater treatment, not a
subtype of wastewater; the generated `parent_habitats` value currently turns a
source-path containment or process context into a strict broader-habitat claim.

No item-level curation decision currently reviews
`habitatmech:GOLD.43c33f3ecc`. Exact ignored/hidden-inclusive searches for the
child identifier, slug, both GOLD child node IDs, and the full child GOLD path
found only the generated record, `PATHS.tsv`, and raw GOLD inventory rows under
the searched repository paths.

## Evidence

The generated record carries no literature evidence or mechanism evidence, and
none is required for the raw GOLD attestation itself.

| Claim | Checked evidence | Assessment |
|---|---|---|
| GOLD attests `Engineered > Sewage treatment plant > Wastewater > Activated sludge`. | `data/raw/gold_ecosystem_paths.tsv:1348` | Supported. The path, label, depth, and two-node note agree with the generated `source_attestations` item. |
| The target path can use generic activated sludge as a broader parent. | `data/raw/ontology_terms.tsv:7191`; `data/raw/ontology_subclass_edges.tsv:5293` | Supported. `ENVO:00002046` is `activated sludge` and is a subclass of sludge. |
| The target path is a kind of `Engineered > Sewage treatment plant > Wastewater`. | Generated from the parent path alone; no item-level decision exists for `habitatmech:GOLD.43c33f3ecc` or `habitatmech:GOLD.353a834cfd`. | Unsupported. The GOLD tree places the child below the wastewater segment, but `parent_habitats` is a strict broader-habitat relation; activated sludge is not waste water. |
| The parent `Wastewater` record is itself raw-source backed. | `data/raw/gold_ecosystem_paths.tsv:284`; `data/habitats/engineered/wastewater__05daf28f.yaml:11-17` | Supported as a source concept, not as a reviewed broader parent of this activated-sludge child. |

## Completeness

- No generated definition, curator-authored term request, environmental
  parameter, characteristic taxon, discussion, dataset, or causal graph is
  expected for a purely seeded GOLD record that has not yet received item-level
  review.
- Exact ignored/hidden-inclusive searches for `habitatmech:GOLD.43c33f3ecc`,
  `activated_sludge__a6d16f1c`, `gold.ecosystem:5592`,
  `gold.ecosystem:5593`,
  `Engineered > Sewage treatment plant > Wastewater > Activated sludge`,
  `habitatmech:GOLD.353a834cfd`,
  `Engineered > Sewage treatment plant > Wastewater`, `ENVO:00002046`,
  `ENVO:00002044`, and `ENVO:00002001` found the cited raw, path-lock,
  ontology-slice, generated-record, prior-review, and research-report rows
  outside `build/`, `pages/`, and `data/text_map/`.
- The target identifier, the child GOLD node IDs, and the child GOLD path had no
  hits in `curation/`, `research/`, `history/`, or pre-existing
  `reports/yaml_record_review/`, with ignored and hidden files included.
- No exact prior report existed for `activated_sludge__a6d16f1c` before this
  report was written: `find reports/yaml_record_review -maxdepth 1 -type f
  -name '*-activated_sludge__a6d16f1c.md' -print` returned no paths.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-ACTSLUDGE-A6D16F1C-001 | major | `parent_habitats` asserts `habitatmech:GOLD.43c33f3ecc` is a kind of `habitatmech:GOLD.353a834cfd` `Wastewater`, but the child is `Activated sludge` and the supported ontology parent is `ENVO:00002046` `activated sludge` under `ENVO:00002044` `sludge`. `parent_habitats` is an is-a relation, and this path edge turns GOLD's wastewater-treatment context into the false claim that activated sludge is wastewater. | Add an item-level decision for `habitatmech:GOLD.43c33f3ecc` in `curation/decisions.tsv`; if the concept stays minted, add a `curation/term_requests.tsv` definition with `parent_mode=REPLACE` so the generated record keeps `ENVO:00002046` and drops the inherited `Wastewater` parent. |

## Recommended Edits

1. Resolve `habitatmech:GOLD.43c33f3ecc` at item depth in
   `curation/decisions.tsv`.
2. If `Engineered > Sewage treatment plant > Wastewater > Activated sludge`
   denotes generic activated sludge rather than a path-specific subtype, ground
   it directly to `ENVO:00002046` so the GOLD attestation merges into the
   existing activated-sludge identity.
3. If the sewage-treatment-plant wastewater context is materially narrower than
   generic activated sludge, keep the source concept minted, use a
   `GROUND_AS_PARENT` decision to `ENVO:00002046`, and add a definition in
   `curation/term_requests.tsv` with `parent_mode=REPLACE` so the next seed no
   longer inherits the false `Wastewater` source-path parent.
4. Regenerate through the seeder rather than editing
   `data/habitats/engineered/activated_sludge__a6d16f1c.yaml` directly.

## Follow-up Checks

- `just seed`
- `just seed-canary habitatmech:GOLD.43c33f3ecc`
- Inspect `data/habitats/engineered/activated_sludge__a6d16f1c.yaml` or confirm
  the record intentionally merged away after an exact `GROUND`.
- `just seed-apply --force`
- `just validate-strict data/habitats/engineered/activated_sludge__a6d16f1c.yaml`
  if the record stays minted; otherwise validate the record that absorbed its
  source attestation.
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`

## Additional Notes

- The false parent is not caused by a hand edit: `just verify-corpus --max-diffs
  1` reproduced the generated YAML exactly from committed raw inputs.
- `data/raw/gold_ecosystem_paths.tsv:430` and
  `data/habitats/engineered/activated_sludge__e45bf91b.yaml` describe the
  sibling GOLD path `Engineered > Sewage treatment plant > Activated sludge`.
  That confirms GOLD has multiple sewage-treatment activated-sludge source
  concepts and does not validate this target's intervening `Wastewater`
  path-parent edge.
- A reference validator was recorded as not applicable because this record has
  no references or causal-graph overlay; the edge that needs curation is a
  generated hierarchy edge, not a reference-backed mechanism claim.
