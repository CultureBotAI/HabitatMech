# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/terrestrial/agricultural_field.yaml`
- Started UTC: 2026-09-24T03:49:00Z
- Finished UTC: 2026-09-24T03:53:31Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/terrestrial/agricultural_field.yaml` |
| Class | `HabitatRecord` |
| Identifier | `ENVO:00000114` |
| Label | `agricultural field` |
| Category | `TERRESTRIAL` |
| Grounding | `EXACT` |
| Mapping status | `REVIEWED` |
| Maintained owners | `data/raw/ontology_terms.tsv`, `data/raw/ontology_subclass_edges.tsv`, `data/raw/gold_ecosystem_paths.tsv`, `data/raw/prego_habitats.tsv`, `data/raw/prego_habitat_taxa.tsv`, `curation/decisions.tsv`, `src/habitatmech/seed.py` |

This is the generated exact `ENVO:00000114` record for agricultural fields. It merges the ENVO term, GOLD's `Environmental > Terrestrial > Agricultural field` source path, and PREGO's `ENVO:00000114` habitat.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/terrestrial/agricultural_field.yaml` | pass; LinkML reported no issues |
| `just validate-strict data/habitats/terrestrial/agricultural_field.yaml` | pass; 1 file scanned, 0 error files, 0 total errors |
| `just validate-causal-all` | pass; 32 causal-graph files with 32 graphs |
| `just validate-causal <overlay>` | Not applicable: hidden/ignored-inclusive searches of `curation/causal_graphs/` found no overlay for `agricultural_field`, `ENVO:00000114`, `habitatmech:GOLD.ad99a95e91`, or `habitatmech:PREGO.4f711a5815` |
| `just term-requests-check` | pass; 109 terms current |
| `just validate-history` | pass; 77 history records valid |
| `just verify-corpus --max-diffs 1` | pass; 3206 expected records, 3206 found, 0 missing, 0 extra, 0 differing |
| `just worklist --limit 2000` | pass; 0 ungrounded records still undecided, 1810 decisions |
| `just report` | pass; corpus report completed for 3206 records |
| Reference validator | Not applicable: the record has no DOI, PMID, URL, `EvidenceItem`, or causal-edge evidence that would need a citation checker |
| `git diff --check` | pass |

## Identity and Grounding

The core record identity is supported:

| Claim | Source | Assessment |
|---|---|---|
| The stable output stem is `agricultural_field`. | `data/habitats/PATHS.tsv` pins `ENVO:00000114` to `agricultural_field`. | Supported. |
| The identifier and label are `ENVO:00000114` / `agricultural field`. | `data/raw/ontology_terms.tsv` carries this ENVO row and definition. | Supported. |
| ENVO parents include `ENVO:01000352` `field`. | `data/raw/ontology_subclass_edges.tsv` asserts `ENVO:00000114 rdfs:subClassOf ENVO:01000352`. | Supported. |
| The GOLD attestation is the terrestrial agricultural-field source. | `data/raw/gold_ecosystem_paths.tsv` has `Environmental > Terrestrial > Agricultural field`, leaf label `Agricultural field`, 226 organisms, and node IDs `gold.ecosystem:3494|gold.ecosystem:3806|gold.ecosystem:4199`. | Supported. |
| The PREGO attestation is the same ENVO class. | `data/raw/prego_habitats.tsv` has `ENVO:00000114`, 2315 taxa, max score 4, and channels `annotated_genomes_isolates|environmental_samples`. | Supported. |
| `mapping_status: REVIEWED` follows from source curation. | `curation/decisions.tsv` has item-level `REVIEW` rows for `habitatmech:GOLD.ad99a95e91` and `habitatmech:PREGO.4f711a5815`. | Supported. |
| `ENVO:00000446` `terrestrial biome` is a broader habitat for this record. | The GOLD second pass in `src/habitatmech/seed.py` adds the identifier resolved for parent path `Environmental > Terrestrial`. That parent path resolves to `ENVO:00000446`. | Unsupported as an is-a edge; an agricultural field is a land field, not a terrestrial biome subtype. |
| `grassland` is an exact synonym of `agricultural field`. | The synonym is imported from `data/raw/ontology_terms.tsv` because `ConceptStore.get()` imports every ontology synonym as `EXACT_SYNONYM`. | Unsupported. Local curation already rejects `ENVO:00000114` as the grounding target for five GOLD `Grasslands` paths and says `grassland area` is the right term. |

## Evidence

The source attestations are accurately transcribed from raw inputs:

- `GOLD` keeps first source ID `gold.ecosystem:3494`, path `Environmental > Terrestrial > Agricultural field`, `skos:exactMatch`, `assertion_count: 226`, and the note that three GOLD ecosystem node IDs share the path.
- `PREGO` keeps source ID `ENVO:00000114`, label `agricultural field`, `assertion_count: 2315`, `score: 4.0`, and evidence channels `annotated_genomes_isolates|environmental_samples`.
- The 25 generated PREGO `characteristic_taxa` rows match ranks 1-25 for `ENVO:00000114` in `data/raw/prego_habitat_taxa.tsv`, with rank 24 and rank 25 dropping to score `3`.

The record has no curator-authored record-level evidence and no causal graph. That is acceptable for a source-seeded ontology record: the habitat existence claim is currently backed by ENVO plus the GOLD/PREGO source attestations, not by a causal mechanism overlay.

Two generated claims exceed the inspected evidence:

- The `ENVO:00000446` parent edge converts GOLD's `Environmental > Terrestrial` filing context into a strict `parent_habitats` assertion. `data/raw/ontology_subclass_edges.tsv` has no `ENVO:00000114 rdfs:subClassOf ENVO:00000446` edge; the only true ENVO parent in the record is `ENVO:01000352` `field`.
- The `grassland` exact synonym comes from ENVO's raw synonym field, but HabitatMech curation rows for GOLD `Grasslands` sources consistently reject that synonym route as the wrong agricultural-field target and ground those rows to `ENVO:00000106` `grassland area` instead.

## Completeness

The target is complete for a generated source record except for the two over-broad generated fields above.

- Hidden/ignored-inclusive search across `curation`, `history`, `research`, `reports`, `data/raw`, and the generated path locks found the expected GOLD row, PREGO rows, ontology rows, item-level decision rows, generated target, sibling `agricultural_field__c2942601` review, and `agricultural_ecosystem` review.
- Hidden/ignored-inclusive search found no `curation/causal_graphs` overlay for `agricultural_field`, `ENVO:00000114`, `habitatmech:GOLD.ad99a95e91`, or `habitatmech:PREGO.4f711a5815`.
- Hidden/ignored-inclusive search found no BacDive, Madin, environment-parameter, external-xref, redirect, or term-request row for `ENVO:00000114` / `agricultural_field`.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-agricultural_field.md' -print` found no prior exact-stem review before this report was written.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-AGFIELD-001 | major | `parent_habitats` asserts `agricultural field` is a kind of `ENVO:00000446` `terrestrial biome`. The edge is generated from the GOLD parent path `Environmental > Terrestrial`, but the ontology only asserts `ENVO:00000114` under `ENVO:01000352` `field`; a field located on land is not a biome subtype. | Add a maintained suppression/edge-typing rule for this GOLD path-parent edge, or change `src/habitatmech/seed.py` so the second-pass GOLD parent linker does not turn broad source categories such as `Environmental > Terrestrial` into false ontology is-a parents on merged exact records. |
| HM-AGFIELD-002 | major | `grassland` is published as an `EXACT_SYNONYM` of `agricultural field`, which can make plain grassland inputs resolve to the agricultural-field class. This is a known false synonym route in this corpus: five `curation/decisions.tsv` rows reject `ENVO:00000114` for GOLD `Grasslands` concepts and choose `ENVO:00000106` `grassland area` instead. | Fix upstream ENVO and re-extract `data/raw/ontology_terms.tsv`, or add a maintained ontology-synonym suppression input consumed by `src/habitatmech/seed.py` so `ENVO:00000114` no longer emits `grassland` as an exact synonym. |

## Recommended Edits

1. Suppress or retype the generated `ENVO:00000446` parent on `ENVO:00000114`.
   - The exact maintained surface is missing today; add a small curation input for GOLD path-parent edge overrides or update `src/habitatmech/seed.py` to skip broad GOLD category parents when a child is already exactly grounded to a more precise ontology class.
   - Regenerate `ENVO:00000114` and confirm `parent_habitats` keeps `ENVO:01000352` but drops `ENVO:00000446`.

2. Remove `grassland` as an exact synonym of `ENVO:00000114` in generated HabitatMech records.
   - Prefer an upstream ENVO fix if possible.
   - If the upstream slice will continue to carry the synonym, add a maintained local synonym-suppression table and make `ConceptStore.get()` filter `ontology.synonyms(identifier)` through it before emitting `EXACT_SYNONYM`.

## Follow-up Checks

- `just seed`
- `just seed-canary ENVO:00000114`
- Inspect `data/habitats/terrestrial/agricultural_field.yaml` and confirm:
  - `identifier` remains `ENVO:00000114`
  - `grounding_status` remains `EXACT`
  - `mapping_status` remains `REVIEWED`
  - `parent_habitats` no longer contains `ENVO:00000446`
  - `synonyms` no longer contains `grassland`
- `just seed-apply --force`
- `just validate data/habitats/terrestrial/agricultural_field.yaml`
- `just validate-strict data/habitats/terrestrial/agricultural_field.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`
- `git diff --check`

## Additional Notes

- The sibling aquatic source `data/habitats/aquatic/agricultural_field__c2942601.yaml` has the opposite shape: it is a fresh-water GOLD concept where `ENVO:00000114` is only local-scale context, and its existing review correctly keeps that issue separate from this exact terrestrial record.
- `data/raw/gold_path_triads.tsv` has no exact triad row for `Environmental > Terrestrial > Agricultural field`. That absence is not itself a defect; the GOLD path and organism count still attest the source category.
- The PREGO taxa are reported-from associations. None of the 25 generated taxon rows sets `is_characteristic` or adds a curator reference, so the record does not overclaim that the taxa typify agricultural fields.
