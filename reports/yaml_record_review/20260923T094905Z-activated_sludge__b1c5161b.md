# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/activated_sludge__b1c5161b.yaml
- Started UTC: 2026-09-23T09:49:05Z
- Finished UTC: 2026-09-23T09:49:05Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.cc5ac8910b` |
| Label | `Activated sludge` |
| Path | `data/habitats/engineered/activated_sludge__b1c5161b.yaml` |
| Category | `ENGINEERED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Generated or maintained | Generated from `data/raw/gold_ecosystem_paths.tsv`, lexical ENVO grounding, and `data/habitats/PATHS.tsv`; not a maintained curation input |
| Source concept | GOLD `gold.ecosystem:4262` for `Engineered > Wastewater > Nutrient removal > Biological phosphorus removal > Activated sludge` |
| Locked slug | `data/habitats/PATHS.tsv:2788` maps `habitatmech:GOLD.cc5ac8910b` to `activated_sludge__b1c5161b` |

I read the full generated record. It contains generated identity, category,
grounding status, two parents, one GOLD source attestation, and the initial
`SEEDED_FROM_SOURCES` history event. It has no generated definition, synonyms,
environmental parameters, characteristic taxa, evidence items, causal graphs,
discussions, or dataset links.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/engineered/activated_sludge__b1c5161b.yaml` | Pass: `No issues found` |
| `just validate-strict data/habitats/engineered/activated_sludge__b1c5161b.yaml` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate-causal-all` | Pass: 32 causal-graph curation files and 32 graphs validated |
| `just term-requests-check` | Pass: `term-request table is current (109 terms)` |
| `just validate-history` | Pass: `No issues found`; 77 history records valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Pass: expected 3,206 records, found 3,206 on disk, 0 missing, 0 extra, 0 differing |
| `just worklist --limit 2000` | Pass: 0 ungrounded records still undecided; 1,810 decisions on file |
| `just report` | Pass: corpus report completed for 3,206 records |
| `git diff --check` | Pass |
| Reference validator | Not applicable: the target has no `evidence`, `causal_graphs`, or reference-bearing maintained overlay to validate |

## Identity and Grounding

The target is a minted GOLD-path record for `Engineered > Wastewater > Nutrient
removal > Biological phosphorus removal > Activated sludge`.
`data/raw/gold_ecosystem_paths.tsv:916` contains exactly that path, gives it the
label `Activated sludge`, records depth `5`, records one GOLD ecosystem node ID
`gold.ecosystem:4262`, and supports the generated source attestation.

The source path is backed by five GOLD study rows and a biosample row.
`data/raw/gold_studies.tsv` lists this exact path for `Gs0063187`,
`Gs0111422`, `Gs0118584`, `Gs0133135`, and `Gs0133308`, and
`data/raw/gold_path_biosamples.tsv:372` lists node `4262` with 42 biosamples.
The collapsed ecosystem-path row supplies the generated organism-level
`assertion_count: 1` and `assertion_unit: ORGANISM`.

The ontology parent is supported. `data/raw/ontology_terms.tsv:7191` gives
`ENVO:00002046` the canonical label `activated sludge`, and
`data/raw/ontology_subclass_edges.tsv:5293` places it under `ENVO:00002044`;
`data/raw/ontology_terms.tsv:7189` labels `ENVO:00002044` as `sludge`. That
supports keeping the GOLD path minted and carrying the generic activated-sludge
material as a broader parent.

The source-path parent is not supported as an is-a parent. `data/habitats/PATHS.tsv:1286`
maps `habitatmech:GOLD.03345a3f86` to `biological_phosphorus_removal`, and
`data/habitats/engineered/biological_phosphorus_removal.yaml` is the seeded
record for `Engineered > Wastewater > Nutrient removal > Biological phosphorus
removal`. Its GOLD source row is `data/raw/gold_ecosystem_paths.tsv:1410`,
which labels the concept `Biological phosphorus removal` and collapses
`gold.ecosystem:3832|gold.ecosystem:4730`. The only maintained decision for
`habitatmech:GOLD.03345a3f86` is a class-level `CONFIRM_UNGROUNDED` row at
`curation/decisions.tsv:114`; that row explicitly says whether the concept is a
habitat at all was not assessed. Activated sludge is a sludge material inside
some biological phosphorus removal systems, not a subtype of the treatment
process or configuration.

The sibling child corroborates the reading. GOLD also has `Engineered >
Wastewater > Nutrient removal > Biological phosphorus removal > Bioreactor` at
`data/raw/gold_ecosystem_paths.tsv:917`, and the generated
`data/habitats/engineered/bioreactor__9b3c0a8b.yaml` record keeps generic
`ENVO:00002123` `bioreactor` as the ontology parent. The shared path parent
therefore groups an activated-sludge material and a bioreactor device under a
biological phosphorus removal context; it does not establish that either child
is a strict kind of that context.

No item-level curation decision currently reviews
`habitatmech:GOLD.cc5ac8910b`. An exact ignored/hidden-inclusive search for the
child identifier found only the generated record and `PATHS.tsv`; exact
ignored/hidden-inclusive searches for the child source node and full GOLD path
found only the generated record and raw GOLD inventory rows under the searched
repository paths.

## Evidence

The generated record carries no literature evidence or mechanism evidence, and
none is required for the raw GOLD attestation itself.

| Claim | Checked evidence | Assessment |
|---|---|---|
| GOLD attests `Engineered > Wastewater > Nutrient removal > Biological phosphorus removal > Activated sludge`. | `data/raw/gold_ecosystem_paths.tsv:916` | Supported. The path, label, depth, one-node identity, and organism count agree with the generated `source_attestations` item. |
| The target path can use generic activated sludge as a broader parent. | `data/raw/ontology_terms.tsv:7191`; `data/raw/ontology_subclass_edges.tsv:5293` | Supported. `ENVO:00002046` is `activated sludge` and is a subclass of sludge. |
| The target path is a kind of `Engineered > Wastewater > Nutrient removal > Biological phosphorus removal`. | Generated from the GOLD parent path alone; the parent has only a class-level decision that did not assess habitat identity. | Unsupported. Biological phosphorus removal is a wastewater treatment context; activated sludge is a material within some such systems, not a subtype of the context itself. |
| The parent `Biological phosphorus removal` record is raw-source backed. | `data/raw/gold_ecosystem_paths.tsv:1410`; `data/habitats/engineered/biological_phosphorus_removal.yaml:9-15` | Supported as a source concept, not as a reviewed broader parent of this activated-sludge child. |

## Completeness

- No generated definition, curator-authored term request, environmental
  parameter, characteristic taxon, discussion, dataset, or causal graph is
  expected for a purely seeded GOLD record that has not yet received item-level
  review.
- Exact ignored/hidden-inclusive searches for `habitatmech:GOLD.cc5ac8910b`,
  `activated_sludge__b1c5161b`, `gold.ecosystem:4262`, `Engineered >
  Wastewater > Nutrient removal > Biological phosphorus removal > Activated
  sludge`, `habitatmech:GOLD.03345a3f86`, `gold.ecosystem:3832`,
  `gold.ecosystem:4730`, `Engineered > Wastewater > Nutrient removal >
  Biological phosphorus removal`, `ENVO:00002046`, and `ENVO:00002044` found
  the cited raw, path-lock, maintained parent curation, ontology-slice,
  generated-record, prior-review, and research-report rows outside `build/`,
  `pages/`, and `data/text_map/`.
- The target identifier had no hits in `curation/`, `research/`, `history/`, or
  pre-existing `reports/yaml_record_review/`, with ignored and hidden files
  included.
- No exact prior report existed for `activated_sludge__b1c5161b` before this
  report was written: `find reports/yaml_record_review -maxdepth 1 -type f
  -name '*-activated_sludge__b1c5161b.md' -print` returned no paths.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-ACTSLUDGE-B1C5161B-001 | major | `parent_habitats` asserts `habitatmech:GOLD.cc5ac8910b` is a kind of `habitatmech:GOLD.03345a3f86` `Biological phosphorus removal`, but the child is `Activated sludge` and the supported ontology parent is `ENVO:00002046` `activated sludge` under `ENVO:00002044` `sludge`. `parent_habitats` is an is-a relation, and this path edge turns GOLD's biological-phosphorus-removal context into the false claim that activated sludge is the treatment context itself. | Add an item-level decision for `habitatmech:GOLD.cc5ac8910b` in `curation/decisions.tsv`; if the concept stays minted, add a `curation/term_requests.tsv` definition with `parent_mode=REPLACE` so the generated record keeps `ENVO:00002046` and drops the inherited `Biological phosphorus removal` parent. |

## Recommended Edits

1. Resolve `habitatmech:GOLD.cc5ac8910b` at item depth in
   `curation/decisions.tsv`.
2. If `Engineered > Wastewater > Nutrient removal > Biological phosphorus
   removal > Activated sludge` denotes generic activated sludge rather than an
   enhanced-biological-phosphorus-removal-specific subtype, ground it directly
   to `ENVO:00002046` so the GOLD attestation merges into the existing
   activated-sludge identity.
3. If the biological-phosphorus-removal context is materially narrower than
   generic activated sludge, keep the source concept minted, use a
   `GROUND_AS_PARENT` decision to `ENVO:00002046`, and add a definition in
   `curation/term_requests.tsv` with `parent_mode=REPLACE` so the next seed no
   longer inherits the false `Biological phosphorus removal` source-path
   parent.
4. Regenerate through the seeder rather than editing
   `data/habitats/engineered/activated_sludge__b1c5161b.yaml` directly.

## Follow-up Checks

- `just seed`
- `just seed-canary habitatmech:GOLD.cc5ac8910b`
- Inspect `data/habitats/engineered/activated_sludge__b1c5161b.yaml` or
  confirm the record intentionally merged away after an exact `GROUND`.
- `just seed-apply --force`
- `just validate-strict data/habitats/engineered/activated_sludge__b1c5161b.yaml`
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
- The parent decision at `curation/decisions.tsv:114` explains only that no
  vendored term matched `Biological phosphorus removal` by the class-level
  search routes. It does not review the parent as a habitat, does not validate
  source-path child edges, and does not promote the child target to
  `REVIEWED`.
- A reference validator was recorded as not applicable because this record has
  no references or causal-graph overlay; the edge that needs curation is a
  generated hierarchy edge, not a reference-backed mechanism claim.
