# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/drainage_ditch.yaml
- Started UTC: 2026-09-27T15:37:22Z
- Finished UTC: 2026-09-27T15:37:22Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Record path | `data/habitats/aquatic/drainage_ditch.yaml` |
| Class | `HabitatRecord` |
| Identifier | `ENVO:00000140` |
| Label | `drainage ditch` |
| Habitat category | `AQUATIC` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Maintained owner | Generated from `data/raw/ontology_terms.tsv`, `data/raw/ontology_subclass_edges.tsv`, `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/PATHS.tsv`, and source-path parent propagation; do not hand-edit this YAML. |

The target is the generated HabitatMech record for ENVO `ENVO:00000140`
`drainage ditch`, also attested by the GOLD source path `Environmental >
Aquatic > Freshwater > Drainage ditch`. `data/habitats/PATHS.tsv` maps the
ENVO identifier to the stable `drainage_ditch` slug.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/drainage_ditch.yaml` | Pass. `linkml-validate` found no issues for this record. |
| `just validate-strict data/habitats/aquatic/drainage_ditch.yaml` | Pass. Strict closed-schema validation scanned 1 file with 0 files in error and 0 error rows. |
| `just validate-causal curation/causal_graphs/<overlay>.yaml` | Not applicable. Ignored-inclusive searches for `ENVO:00000140`, the `drainage_ditch` slug, and the source label found no causal-graph overlay for this record. |
| `just validate-causal-all` | Pass. All 32 causal-graph curation files and 32 graphs validated. |
| Reference validator | Not applicable. The record has no `evidence`, `datasets`, or `causal_graphs` references to validate. |
| `just term-requests-check` | Pass. The generated term-request table is current at 109 terms. |
| `just validate-history` | Pass. 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus` | Pass. 3,206 expected records were present with 0 missing, 0 extra, and 0 differing generated YAML files. |
| `just worklist --status all --out /tmp/habitatmech-worklist.tsv` | Pass. The worklist completed and wrote 953 ungrounded rows; this exact ENVO record was correctly absent. |
| `just report --out /tmp/habitatmech-report.tsv` | Pass. The corpus report completed and included this record as `EXACT`, `SEEDED`, and sourced only from GOLD. |
| `git diff --check` | Pass after report creation. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| The generated record denotes ENVO's `drainage ditch` class. | `data/raw/ontology_terms.tsv` has `ENVO:00000140`, ontology `ENVO`, label `drainage ditch`, definition `A ditch that collects water from the surrounding land.`, exact synonyms `canal` and `rhyne`, and `obsolete=FALSE`. The generated YAML preserves the identifier, label, definition, `definition_source: ENVO`, and ENVO synonyms. | Supported exactly. |
| GOLD's source path is an exact lexical match for ENVO `drainage ditch`. | `data/raw/gold_ecosystem_paths.tsv` has one row for `Environmental > Aquatic > Freshwater > Drainage ditch` with leaf label `Drainage ditch`, depth 4, two collapsed GOLD node IDs, and no direct GOLD assertions. The generated source attestation records `gold.ecosystem:7922`, the source label, the path, `skos:exactMatch`, and a note that two GOLD ecosystem node IDs share this path. | Supported exactly. |
| `grounding_status: EXACT` is semantically appropriate. | The ENVO label exactly names a ditch that collects water from the surrounding land, and the GOLD path names the same drainage-ditch feature under an aquatic freshwater source prefix. | Supported. |
| The `ENVO:00000037` parent follows ENVO. | `data/raw/ontology_subclass_edges.tsv` asserts `ENVO:00000140 rdfs:subClassOf ENVO:00000037`, and `data/raw/ontology_terms.tsv` labels `ENVO:00000037` as `ditch`. | Supported exactly. |
| The generated `ENVO:00002011` parent does not follow ENVO. | The raw vendored subclass table has no `ENVO:00000140 rdfs:subClassOf ENVO:00002011` edge; that parent is inherited from the GOLD source path segment `Freshwater`, which resolves to `ENVO:00002011` `fresh water`. | Supported as source-path propagation, but not as an `is-a` parent. A drainage ditch is a channel that can collect fresh water, not a subclass of fresh water. |
| `mapping_status: SEEDED` reflects the absence of item-level maintained curation. | Ignored-inclusive searches found no `curation/decisions.tsv`, `curation/term_requests.tsv`, `curation/term_requests_excluded.tsv`, or `curation/external_xrefs.tsv` row keyed by `ENVO:00000140` or the exact GOLD drainage-ditch path. The generated YAML has only the seed curation event. | Supported. |

## Evidence

The record has no curator-authored `evidence`, `environmental_parameters`,
`characteristic_taxa`, `causal_graphs`, `discussions`, or `datasets`.

| Assertion | Evidence | Assessment |
|---|---|---|
| GOLD has a direct drainage-ditch path but no direct sample or organism count for that path. | `data/raw/gold_ecosystem_paths.tsv` stores `gold_node_count=2`, `organism_count=0`, `study_count=0`, `biosample_count=0`, `total_assertions=0`, and node IDs `gold.ecosystem:7922|gold.ecosystem:7923` for `Environmental > Aquatic > Freshwater > Drainage ditch`. The generated source attestation uses the first node ID and explicitly notes the shared path. | Supported exactly. |
| GOLD also has a sampled drainage-ditch sediment child path. | `data/raw/gold_ecosystem_paths.tsv` stores `Environmental > Aquatic > Freshwater > Drainage ditch > Sediment` with `gold.ecosystem:7924` and 8 organism assertions, and the generated `data/habitats/aquatic/sediment__a36658ce.yaml` hangs under both `ENVO:00000140` and `ENVO:00002007`. | Supported; this corroborates drainage ditch as GOLD path context, not `fresh water` as an `is-a` parent of `drainage ditch`. |
| The source-owned ENVO synonyms are copied exactly. | The raw ontology row lists `canal|rhyne`, and the generated YAML carries those as ENVO `EXACT_SYNONYM` entries. | Supported exactly; this review did not re-audit those upstream synonym scopes. |

No snippet or citation mismatch was present because this generated seed record
has only source-inventory facts and generated curation history.

## Completeness

This record is partly complete as a generated ENVO/GOLD seed. It preserves the
exact ENVO identity, the ENVO definition and exact synonyms, the exact GOLD
source path, the multi-node GOLD note, and the generated seed curation event.

The generated parentage still needs maintained curation. `ENVO:00000037`
`ditch` is the only direct ENVO parent in the vendored subclass table, while
`ENVO:00002011` `fresh water` is inherited from GOLD's source hierarchy. That
second edge models a sampling-path medium as a strict broader habitat, so
downstream consumers currently see every `drainage ditch` record as both a
`ditch` and a kind of `fresh water`.

Empty optional fields are otherwise expected for the current maintained inputs:

- no `curation/causal_graphs/drainage_ditch.yaml` overlay exists;
- no maintained item-level decision exists for `ENVO:00000140` or the exact
  GOLD drainage-ditch source path;
- no term request, term-request exclusion, or external xref row is keyed by
  `ENVO:00000140`; and
- no target-specific report exists under `research/habitats`.

Ignored- and hidden-file-inclusive searches covered `data/raw`, `curation`,
`research`, `reports/yaml_record_review`, `conf`, and `data/habitats` for
`ENVO:00000140`, `gold.ecosystem:7922`, `gold.ecosystem:7923`,
`gold.ecosystem:7924`, `drainage_ditch`, `Drainage ditch`, `drainage ditch`,
and the exact GOLD drainage-ditch paths. Separate `find` checks covered
`reports/yaml_record_review`, `curation/causal_graphs`, and `research/habitats`
for `drainage`. These checks found the expected raw ontology, raw GOLD,
generated `PATHS.tsv`, generated target YAML, and the generated sediment child
record, with no prior exact drainage-ditch review, causal overlay, or research
report.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `drainage ditch` falsely inherits `fresh water` as a strict parent. The edge is generated from GOLD's `Environmental > Aquatic > Freshwater > Drainage ditch` path prefix, not from ENVO; it asserts that a ditch feature is a kind of water material. The source attestation should remain, but `ENVO:00002011` should be modeled, at most, as source context or possible medium rather than an `is-a` parent. | The generated YAML has `parent_habitats: [ENVO:00000037, ENVO:00002011]`; `data/raw/ontology_subclass_edges.tsv` directly places `ENVO:00000140` only under `ENVO:00000037`; `data/raw/ontology_terms.tsv` labels `ENVO:00000140` as `drainage ditch` and `ENVO:00002011` as `fresh water`; `data/raw/gold_ecosystem_paths.tsv` places the exact GOLD path under `Freshwater`. | `src/habitatmech/seed.py`; future maintained curation input for suppressing false source-path parents on exact ontology records |

No blocker or minor findings were found.

## Recommended Edits

1. Add a maintained way to suppress false source-path parents on exact
   ontology-grounded records.
2. Use that maintained input to remove `ENVO:00002011` from generated
   `data/habitats/aquatic/drainage_ditch.yaml` while preserving the true
   ENVO parent `ENVO:00000037` and the GOLD `Environmental > Aquatic >
   Freshwater > Drainage ditch` source attestation.
3. Regenerate the target record from the maintained inputs instead of editing
   `data/habitats/aquatic/drainage_ditch.yaml` directly.

## Follow-up Checks

| Check | Purpose |
|---|---|
| `just seed` | Preview regenerated corpus-wide outputs after maintained input changes. |
| `just seed-canary ENVO:00000140` | Confirm this one generated target retains the ENVO/GOLD exact identity and drops only the false `fresh water` parent. |
| `just seed-apply --force` | Rebuild generated YAML after inspecting canary output. |
| `just validate data/habitats/aquatic/drainage_ditch.yaml` | Check the regenerated target against the LinkML `HabitatRecord` schema. |
| `just validate-strict data/habitats/aquatic/drainage_ditch.yaml` | Check the regenerated target under the closed-schema validator. |
| `just validate-causal-all` | Check any maintained causal overlays that exist after curation. |
| `just validate-history` | Confirm any append-only history record for a curation session is valid. |
| `just verify-corpus` | Prove generated `data/habitats/` still reproduces from `data/raw/` and curation inputs. |
| `just report` | Confirm the generated corpus report still classifies the record as expected. |
| `git diff --check` | Catch whitespace errors in maintained and generated diffs. |

## Additional Notes

- The absence checks in this review used `rg --no-ignore --hidden` and `find`,
  so ignored and hidden files were included.
- The exact GOLD drainage-ditch grouping path currently carries 0 direct
  organism assertions. Its sampled sediment child, `Environmental > Aquatic >
  Freshwater > Drainage ditch > Sediment`, carries 8 organism assertions and
  uses the exact drainage-ditch record as path context.
