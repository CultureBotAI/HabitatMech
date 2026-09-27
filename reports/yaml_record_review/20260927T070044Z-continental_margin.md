# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/continental_margin.yaml`
- Started UTC: 2026-09-27T07:00:44Z
- Finished UTC: 2026-09-27T07:00:44Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/aquatic/continental_margin.yaml` |
| Identifier | `ENVO:01000298` |
| Label | `continental margin` |
| Class | `HabitatRecord` |
| Category | `AQUATIC` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Generated status | Generated from committed inventories and the vendored ontology slice; `data/habitats/PATHS.tsv` pins `ENVO:01000298` to `continental_margin` |
| Source concept | GOLD `Environmental > Aquatic > Marine > Continental margin` |

The generated record has one GOLD source attestation and the definition for
`ENVO:01000298` `continental margin`. It has no synonyms, xrefs,
environmental parameters, characteristic taxa, evidence items, causal graphs,
discussions, or datasets. No item-level curation decision exists for this GOLD
source concept, so `mapping_status: SEEDED` is expected.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/continental_margin.yaml` | Passed |
| `just validate-all data/habitats/aquatic/continental_margin.yaml` | Passed; delegates to strict validation and scanned 1 file with 0 error rows |
| `just validate-strict data/habitats/aquatic/continental_margin.yaml --quiet` | Passed; scanned 1 file with 0 error rows |
| `just validate-causal-all` | Passed; validated 32 causal-graph curation files with 32 graphs |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml` |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist-continental-margin.tsv` | Passed; wrote 953 ungrounded rows and reported 1,810 decisions on file |
| `just verify-corpus --max-diffs 1` | Passed; all 3,206 records reproduce exactly from `data/raw/` |
| `just report` | Passed; current corpus has 3,206 records, including 468 `AQUATIC`, 1,060 `EXACT`, and 2,520 `SEEDED` records |

No separate `validate-references` recipe is exposed by the HabitatMech
`justfile`; hidden and ignored files were included in the exact search for a
`validate-references:` recipe. This generated record has no `EvidenceItem`,
causal-graph edge, discussion, or dataset references requiring a separate
record-local reference check.

## Identity and Grounding

The record's identifier and definition are supported by the vendored ontology
slice. `data/raw/ontology_terms.tsv` labels `ENVO:01000298` as
`continental margin` and carries the same definition emitted into the generated
record. The generated `ENVO:00002000` `slope` parent is also supported:
`data/raw/ontology_subclass_edges.tsv` has the subclass edge
`ENVO:01000298 rdfs:subClassOf ENVO:00002000`.

The generated GOLD source attestation matches the maintained GOLD inventory:

- `data/raw/gold_ecosystem_paths.tsv` records the exact
  `Environmental > Aquatic > Marine > Continental margin` source path with one
  GOLD ecosystem node, `gold.ecosystem:5386`, and zero organism assertions.
- The generated `source_attestations` entry preserves that node ID, source
  label, source path, and `skos:exactMatch` predicate.
- The generated attestation correctly omits `assertion_count` and
  `assertion_unit`: `src/habitatmech/seed.py` only emits those fields for GOLD
  when `organism_count` is nonzero.

The extra generated `ENVO:00001999` `marine water body` parent is not
supported. It comes from the GOLD parent path
`Environmental > Aquatic > Marine`, which currently resolves to the reviewed
`ENVO:00001999` record. That parent path is valid context for the GOLD source
concept, but it is not a strict genus for `ENVO:01000298`: the ontology defines
`continental margin` as a seafloor slope and places it under `ENVO:00002000`
`slope`, while `ENVO:00001999` denotes a body of marine water.

The related GOLD child
`Environmental > Aquatic > Marine > Continental margin > Sediment` is correctly
kept separate as `habitatmech:GOLD.f3b93cb911`. Its GOLD path denotes sediment
on a continental margin, and its MIxS triad summary uses
`ENVO:01000298` as the local-scale feature and `ENVO:03000033`
`marine sediment` as the sampled medium. That child corroborates continental
margin as the seafloor setting of a sample, not as a marine water body.

## Evidence

The record has no curator-authored definition, causal edge, characteristic
taxon, environmental parameter, or external citation claim.

| YAML claim | Maintained evidence | Review |
|---|---|---|
| `identifier: ENVO:01000298` | `data/habitats/PATHS.tsv` pins the ontology identifier to `continental_margin`, and `data/raw/ontology_terms.tsv` has a term row for `ENVO:01000298` `continental margin`. | Supported |
| `label: continental margin` | `data/raw/ontology_terms.tsv` gives `ENVO:01000298` this label. | Supported |
| `definition` / `definition_source: ENVO` | The generated definition matches the vendored ENVO definition in `data/raw/ontology_terms.tsv`. | Supported |
| `habitat_category: AQUATIC` | The only source attestation starts with `Environmental > Aquatic`; the ontology term denotes a part of the seafloor. | Supported |
| `grounding_status: EXACT` | GOLD's `Continental margin` source label is the same habitat named by `ENVO:01000298`. | Supported |
| `mapping_status: SEEDED` | Hidden/ignored exact searches found no item-level row for `ENVO:01000298` or `Environmental > Aquatic > Marine > Continental margin` in `curation/decisions.tsv`. | Supported |
| `parent_habitats: ENVO:00002000` | `data/raw/ontology_subclass_edges.tsv` places `ENVO:01000298` directly under `ENVO:00002000` `slope`. | Supported |
| `parent_habitats: ENVO:00001999` | The edge is generated from the GOLD parent path `Environmental > Aquatic > Marine`, whose record resolves to `ENVO:00001999` `marine water body`. | Unsupported: the source path is contextual, and `continental margin` is a seafloor slope rather than a subclass of lentic marine water body. |
| GOLD source attestation | `data/raw/gold_ecosystem_paths.tsv` has the exact source path with `gold.ecosystem:5386`. | Supported |

## Completeness

Hidden and ignored files were included in exact searches for
`ENVO:01000298`, `gold.ecosystem:5386`, `continental_margin`,
`continental margin`, `Continental margin`, and
`Environmental > Aquatic > Marine > Continental margin` across `curation`,
`data/raw`, `history`, `research`, `reports`, `conf`,
`data/habitats/PATHS.tsv`, and `data/habitats`.

Those searches found the generated YAML, the pinned `PATHS.tsv` slug, the
vendored ENVO term row, the ENVO subclass edge to `slope`, the exact GOLD
ecosystem-path row, the zero-assertion GOLD sediment child row, the child
biosample and triad summaries, and the child study path. They found no
`curation/decisions.tsv` row, no `curation/term_requests.tsv` row, no
`curation/causal_graphs/` overlay, no target-specific `history/` entry, no
committed deep-research report, and no prior exact YAML review for this slug or
identifier.

The generated record has no environmental parameters because the kg-microbe
environment table is not keyed to `ENVO:01000298`. It has no characteristic
taxa because the only exact source is a zero-assertion GOLD structural node,
not a PREGO, BacDive, or Madin habitat. It has no causal graph because no
maintained overlay exists for this exact record.

## Findings

### Blocker

None found.

### Major

| ID | Finding | Evidence | Maintained owner |
|---|---|---|---|
| HM-CONTINENTAL-MARGIN-001 | `parent_habitats` incorrectly asserts that `ENVO:01000298` `continental margin` is a subclass of `ENVO:00001999` `marine water body`. | The target lists `ENVO:00001999` as a parent, but `data/raw/ontology_subclass_edges.tsv` only places `ENVO:01000298` under `ENVO:00002000` `slope`. The vendored definitions make the mismatch semantic as well as structural: a continental margin is a seafloor slope, while a marine water body is a lentic water body composed primarily of marine water. | No current data-only curation surface can suppress one generated GOLD parent-path edge while preserving the exact ENVO identity. Add a maintained source-path parent-edge override in `curation/` and teach the second GOLD pass in `src/habitatmech/seed.py` to skip suppressed edges before adding them to `parent_habitats`. |

### Minor

None found.

## Recommended Edits

1. Add a maintained source-path parent-edge override surface under `curation/`
   that can reject one GOLD classification edge without deleting the source
   attestation or weakening exact ontology grounding.
2. Update `src/habitatmech/seed.py` so the second GOLD pass consults that
   maintained table before adding the GOLD parent-path link.
3. Add an override for
   `Environmental > Aquatic > Marine -> Environmental > Aquatic > Marine > Continental margin`
   so the regenerated record keeps `ENVO:00002000` and drops
   `ENVO:00001999`.

## Follow-up Checks

After implementing the source-path override, run:

- `just seed`
- `just seed-canary ENVO:01000298`
- inspect `data/habitats/aquatic/continental_margin.yaml`
- `just validate data/habitats/aquatic/continental_margin.yaml`
- `just validate-all data/habitats/aquatic/continental_margin.yaml`
- `just verify-corpus --max-diffs 1`
- `just render`
- `just qc`

The regenerated target should keep the ontology-derived `ENVO:00002000` parent,
drop only `ENVO:00001999`, retain the GOLD source attestation for
`gold.ecosystem:5386`, and avoid changing the separate
`data/habitats/aquatic/sediment__69d4893f.yaml` continental-margin sediment
record except where the new override explicitly intends to.

## Additional Notes

This defect is another instance of a known generated-parent class: GOLD path
links are classification containment and not always biological subsumption.
`src/habitatmech/seed.py` already treats GOLD path edges as a heuristic when it
breaks parent cycles; this review found a false acyclic edge of the same kind.
