# YAML Record Review: alkaline spring

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/alkaline_spring.yaml
- Started UTC: 2026-09-21T14:09:12Z
- Finished UTC: 2026-09-21T14:09:12Z
- Verdict: needs curation

## Target

The target is the generated `HabitatRecord` at `data/habitats/aquatic/alkaline_spring.yaml`.

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `ENVO:01001894` |
| Label | `alkaline spring` |
| Category | `AQUATIC` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| GOLD source concept | `habitatmech:GOLD.784eaddd71` |
| GOLD source node | `gold.ecosystem:7946` |
| Source path | `Environmental > Aquatic > Deep subsurface > Groundwater > Alkaline spring` |
| Locked stem | `alkaline_spring` in `data/habitats/PATHS.tsv` |

This review covers the single GOLD source concept that has been lexically grounded to `ENVO:01001894`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/alkaline_spring.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/alkaline_spring.yaml --quiet` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records, 3,206 records on disk, 0 missing, 0 extra, 0 differing. |
| Reference validator | Not checked: this record has no DOI/PMID/URL `EvidenceItem`, no causal-edge evidence, and no target-specific `curation/causal_graphs/` overlay. |

## Identity and Grounding

The record currently merges GOLD `Environmental > Aquatic > Deep subsurface > Groundwater > Alkaline spring` onto `ENVO:01001894`. The vendored ENVO term row for `ENVO:01001894` has label `alkaline spring` and definition `A mineral spring through which water with a high pH flows.` The ontology subclass table makes `ENVO:01001894` a direct child of `ENVO:00000125` `mineral spring`, itself a child of `ENVO:00000027` `spring`. The GOLD lexical identity is therefore plausible and the record's own label, definition, `ENVO:00000125` parent, and `skos:exactMatch` source attestation all agree.

This exact GOLD path is sparse. `data/raw/gold_ecosystem_paths.tsv` has one row for `Environmental > Aquatic > Deep subsurface > Groundwater > Alkaline spring` with leaf `Alkaline spring`, depth 5, one GOLD node, and zero organism, study, biosample, and total assertions. Exact ignored/hidden-inclusive searches before this report was created covered the maintained `curation/`, `history/`, and `data/raw/` surfaces plus `data/habitats/PATHS.tsv` and prior `reports/yaml_record_review/` reports; they found the source path in `data/raw/gold_ecosystem_paths.tsv`, the locked stem in `data/habitats/PATHS.tsv`, and one contextual sibling-review mention, but no `curation/decisions.tsv`, `curation/term_requests.tsv`, or `curation/causal_graphs/` row for `ENVO:01001894`, `alkaline_spring`, `habitatmech:GOLD.784eaddd71`, or `gold.ecosystem:7946`.

`mapping_status: SEEDED` is correct because the GOLD source concept has no item-level row in `curation/decisions.tsv`. The seeder documentation explicitly treats GOLD lexical matches as unreviewed.

The generated GOLD path parent is not safe. `parent_habitats` contains `habitatmech:GOLD.22a80cbd14`, the minted `Groundwater` record for `Environmental > Aquatic > Deep subsurface > Groundwater`; that edge is inherited mechanically from the parent path. ENVO defines `spring` as a surface landform that provides an egress for groundwater or steam, so `Groundwater` is related context rather than a strictly broader class for `alkaline spring`.

## Evidence

| Claim | Evidence | Assessment |
|---|---|---|
| The generated identifier, label, and definition match the vendored ENVO identity. | `data/raw/ontology_terms.tsv` contains `ENVO:01001894` with label `alkaline spring` and the same definition. | Supported. |
| The record's ontology parent `ENVO:00000125` is a direct superclass of alkaline spring. | `data/raw/ontology_subclass_edges.tsv` contains `ENVO:01001894 rdfs:subClassOf ENVO:00000125`; `data/raw/ontology_terms.tsv` labels `ENVO:00000125` as `mineral spring`. | Supported. |
| `data/habitats/aquatic/alkaline_spring.yaml` is the stable file path for this record. | `data/habitats/PATHS.tsv` maps `ENVO:01001894` to `alkaline_spring`. | Supported. |
| The GOLD attestation preserves the sole upstream ecosystem node for the exact source path. | `data/raw/gold_ecosystem_paths.tsv` lists exactly `gold.ecosystem:7946` for `Environmental > Aquatic > Deep subsurface > Groundwater > Alkaline spring`, and the target YAML names that node with `source_label: Alkaline spring`. | Supported. |
| The GOLD source has zero current organism assertions. | The raw ecosystem-path row has `organism_count=0`, `study_count=0`, `biosample_count=0`, and `total_assertions=0`, and the YAML omits `assertion_count` and `assertion_unit`. | Supported. |
| The inherited `habitatmech:GOLD.22a80cbd14` parent is a strict broader habitat for `ENVO:01001894`. | The raw GOLD row sits under `Environmental > Aquatic > Deep subsurface > Groundwater`, and `data/habitats/PATHS.tsv` maps that parent source concept to `groundwater`, but ENVO places alkaline spring under the surface-landform class `spring`, via `mineral spring`, not under a groundwater material class. | Not supported as an `is-a` edge. |
| Existing target-specific causal evidence belongs on this record. | Exact ignored/hidden-inclusive searches of `curation/causal_graphs`, `curation/term_requests.tsv`, `history`, and prior `reports/yaml_record_review` found no row or file for `alkaline_spring`, `ENVO:01001894`, `habitatmech:GOLD.784eaddd71`, or `gold.ecosystem:7946` before this report was created. | Not supported by current maintained inputs. |

## Completeness

The generated record preserves the current source-owned facts for the GOLD path: node ID, label, full path, the exact-match predicate, and zero assertion count. No `assertion_count` is expected because the raw row has no organism assertions.

The record is still incomplete as a reviewed model:

- The exact GOLD match has no item-level decision for `habitatmech:GOLD.784eaddd71`; `mapping_status: SEEDED` should remain until a curator verifies the source path and ENVO identity together.
- The inherited `Groundwater` parent should not be exported as a strict broader habitat unless item review finds evidence that GOLD used `Alkaline spring` for a groundwater material rather than for the ENVO spring landform.
- Exact ignored/hidden-inclusive searches of the maintained curation and history surfaces found no target-specific causal overlay, term request, or prior review report before this report was created.

Empty `environmental_parameters`, `characteristic_taxa`, `evidence`, `causal_graphs`, `discussions`, and `datasets` are otherwise appropriate for this zero-assertion GOLD-only record. No maintained input currently supplies those fields.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| `HM-ALKALINE-SPRING-001` | Major | The generated `Groundwater` parent is a GOLD path context, not a demonstrated broader habitat. `parent_habitats` is an `is-a` field, but ENVO defines `alkaline spring` as a kind of `mineral spring`, and `mineral spring` is a kind of surface-landform `spring`. That makes `Groundwater` related to the spring rather than strictly broader than it. | `data/habitats/aquatic/alkaline_spring.yaml` lists `habitatmech:GOLD.22a80cbd14`; the exact GOLD source path is nested below `Groundwater`; `data/raw/ontology_terms.tsv` defines `ENVO:00000027` `spring`; `data/raw/ontology_subclass_edges.tsv` places `ENVO:01001894` below `ENVO:00000125`, not below a groundwater material term. | `src/habitatmech/seed.py`, or a maintained parent-edge override consumed by the seeder. |

## Recommended Edits

1. Item-review GOLD source concept `habitatmech:GOLD.784eaddd71` in `curation/decisions.tsv`. If the exact identity is retained, add an item-depth `GROUND` row for `ENVO:01001894` `alkaline spring` so the lexical match can become reviewed.
2. Add generator support or a maintained curation override that can suppress the false GOLD path edge from `ENVO:01001894` to `habitatmech:GOLD.22a80cbd14` while preserving the true ontology parent `ENVO:00000125`.
3. Recheck sibling spring rows under the same GOLD parent, especially `data/habitats/aquatic/salt_spring.yaml`, because an existing item-depth review on that record does not suppress the inherited `Groundwater` parent.

No direct edit should be made to `data/habitats/aquatic/alkaline_spring.yaml`.

## Follow-up Checks

| Edit | Narrowest proving check |
|---|---|
| Add the item-level `GROUND` decision for `habitatmech:GOLD.784eaddd71`. | Re-read the exact `curation/decisions.tsv` row and confirm `decision=GROUND`, `object_id=ENVO:01001894`, `object_label=alkaline spring`, and `review_depth=ITEM`. |
| Suppress the false GOLD path parent. | Run `just seed-canary ENVO:01001894 --force` and inspect `data/habitats/aquatic/alkaline_spring.yaml` to confirm `ENVO:00000125` remains in `parent_habitats` and `habitatmech:GOLD.22a80cbd14` is absent. |
| Preserve the sparse GOLD attestation. | Inspect the regenerated `source_attestations` entry and confirm it still carries `gold.ecosystem:7946`, the exact source path, and no nonzero `assertion_count`. |
| Validate the regenerated corpus. | Run `just validate data/habitats/aquatic/alkaline_spring.yaml`, `just validate-strict data/habitats/aquatic/alkaline_spring.yaml --quiet`, `just term-requests-check`, `just validate-history`, and `just verify-corpus --max-diffs 1`. |
| Verify exported hierarchy products. | Rebuild KGX and SSSOM products and confirm they no longer publish `ENVO:01001894` as a child of `habitatmech:GOLD.22a80cbd14`. |

## Additional Notes

This review follows up on the `acidic_spring` report's recommendation to recheck sibling spring rows under the same GOLD parent. `curation/decisions.tsv` already contains an item-depth `REVIEW` row for the sibling GOLD `Environmental > Aquatic > Deep subsurface > Groundwater > Saline spring` source. That record still inherits `habitatmech:GOLD.22a80cbd14`, which confirms that direct item review alone cannot currently remove a false source-path parent.

This report intentionally leaves generated YAML unchanged. The record is schema-valid and reproducible; the defect is in how a reproducible GOLD classification parent is being interpreted as an exported subclass edge.
