# YAML Record Review: eutrophic water

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/aquatic/eutrophic_water.yaml`
- Started UTC: 2026-10-02T06:18:00Z
- Finished UTC: 2026-10-02T06:22:35Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `ENVO:00002224` |
| Label | `eutrophic water` |
| File | `data/habitats/aquatic/eutrophic_water.yaml` |
| Category | `AQUATIC` |
| Grounding | `EXACT` |
| Mapping | `SEEDED` |
| Source | PREGO `ENVO:00002224` |
| Generated status | Generated from `data/raw/*`; `data/habitats/` is read-only generated output. |

The full generated YAML was read. The record has one PREGO source attestation,
one ENVO definition, one PREGO synonym, one ontology parent, 25 surfaced PREGO
taxa from a 42-taxon candidate pool, one seed provenance event, no xrefs, no
environmental parameters, no claim-level evidence, no causal graphs, no
discussions, and no datasets.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/eutrophic_water.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/eutrophic_water.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus` | Passed; expected 3,206 records, found 3,206 on disk, 0 missing, 0 extra, 0 differing. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just worklist --status all --out /tmp/habitatmech-eutrophic-water-worklist.tsv` | Passed; wrote 953 ungrounded worklist rows. The target is correctly absent because it is an exact ENVO grounding rather than an ungrounded worklist item. |
| `just report --out /tmp/habitatmech-eutrophic-water-report.tsv` | Passed; the per-record row for `ENVO:00002224` reports `AQUATIC`, `EXACT`, `SEEDED`, source `PREGO`, 1 source, 42 assertions, `has_definition=True`, 1 parent, 0 parameters, 25 taxa, and 0 causal graphs at `data/habitats/aquatic/eutrophic_water.yaml`. |

`iModulonDB` was not applicable: the record names no gene, locus tag,
regulator, pathway, stress-response trait, or transcriptomics dataset.

## Identity and Grounding

The generated identifier, label, category, definition, parent, synonym, and
source attestation all trace to maintained inputs:

| Claim | Maintained input |
|---|---|
| Stable slug | `data/habitats/PATHS.tsv` maps `ENVO:00002224` to `eutrophic_water`. |
| ENVO identity | `data/raw/ontology_terms.tsv` contains non-obsolete habitat term `ENVO:00002224`, label `eutrophic water`, definition `Water with a high nutrient level.`, and provider `ENVO`. |
| PREGO source | `data/raw/prego_habitats.tsv` has the exact same source identifier and label, 42 environmental-sample taxon assertions, score 4, and source synonyms `eutrophic water|eutrophic waters`. |
| ENVO parent | `data/raw/ontology_subclass_edges.tsv` asserts `ENVO:00002224 rdfs:subClassOf ENVO:00002006`, and `data/raw/ontology_terms.tsv` contains non-obsolete `ENVO:00002006` `liquid water`, defined as an environmental material primarily composed of liquid dihydrogen oxide. |
| PREGO taxa | `data/raw/prego_habitat_taxa.tsv` has the source-backed rank 1-25 taxa copied into the generated YAML, all with score 4 and a 42-taxon candidate pool. |

No maintained item-level decision is needed for this record: the PREGO source
identifier is already the exact ENVO class for nutrient-rich liquid water.
The subclass edge to `ENVO:00002006` is an ontology edge, not a generated
source-path containment edge or curation overlay.

The rendered page `pages/habitats/eutrophic-water-envo-00002224.html` mirrors
the YAML: it shows the same ENVO identifier and definition, PREGO source
attestation, `liquid water` broader habitat, 25 PREGO taxa, PREGO synonym, and
no environmental parameters or causal graph.

## Evidence

| Claim | Evidence checked | Assessment |
|---|---|---|
| The record is exactly ENVO `eutrophic water`. | `data/raw/ontology_terms.tsv`, `data/habitats/PATHS.tsv`, and `data/raw/prego_habitats.tsv` all use `ENVO:00002224` for the same label. | Supported. |
| The definition is ontology-backed. | The YAML definition and `definition_source: ENVO` match the committed `ENVO:00002224` ontology row verbatim. | Supported. |
| `ENVO:00002006` is the correct broader habitat. | The committed ontology subclass table links `eutrophic water` directly to `liquid water`, and the parent target is present and non-obsolete in the ontology-term table. | Supported. |
| The PREGO attestation is current for the committed inventory. | `data/raw/prego_habitats.tsv` has 42 `environmental_samples` assertions for `ENVO:00002224`, and `data/raw/prego_habitat_taxa.tsv` supplies the ranked taxa copied into the generated record. | Supported. |
| The plural synonym is source-backed. | The PREGO source row lists both `eutrophic water` and `eutrophic waters`; the generated record keeps the plural as a PREGO `RELATED_SYNONYM`. | Supported. |
| Empty optional sections are current. | Hidden/ignored-inclusive searches over maintained decisions, term requests, causal overlays, `history`, `research`, raw inventories, existing review reports, generated YAML, and the exact rendered page found no target-owned xref, environmental parameter, causal overlay, discussion, dataset, research report, term request, or history record. | Supported for the current maintained inputs. |

## Completeness

Consequential coverage:

- `data/raw/ontology_terms.tsv`, `data/raw/ontology_subclass_edges.tsv`,
  `data/raw/prego_habitats.tsv`, and `data/raw/prego_habitat_taxa.tsv` contain
  the exact `ENVO:00002224` evidence needed to regenerate the record.
- `curation/decisions.tsv` and `curation/term_requests.tsv` have no exact
  `ENVO:00002224` row; the record is therefore intentionally a seeded exact
  match rather than an item-reviewed or authored HabitatMech concept.
- Exact `find` over `reports/yaml_record_review` for `*eutrophic*` found no
  prior review report for this record before this file was added.
- Exact `find` over `curation/causal_graphs`, `history`, and `research` for
  `*eutrophic*` found no target-specific causal overlay, append-only history,
  or research report.
- Exact `rg --no-ignore --hidden` over `research/` found one non-target hit:
  the `eutric` leptosol report mentions `ENVO:00002224` only to warn future
  curators not to conflate eutric soils with eutrophic waters.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If future curation changes the grounding or adds a causal
overlay, rerun:

- `just seed`
- `just seed-canary ENVO:00002224`
- `just validate data/habitats/aquatic/eutrophic_water.yaml`
- `just validate-strict data/habitats/aquatic/eutrophic_water.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus`
- `just render`
- `just report`

## Additional Notes

Ignored files were included in absence searches. Exact `find` and
`rg --no-ignore --hidden` searches covered the target identifier, slug, label,
maintained curation inputs, `history`, `research`, raw PREGO inventory,
existing review reports, generated habitat YAML, the exact rendered page, and
source code. They found the expected `data/habitats/PATHS.tsv`,
`ontology_terms.tsv`, `ontology_subclass_edges.tsv`, `prego_habitats.tsv`,
`prego_habitat_taxa.tsv`, and rendered-page rows, plus one unrelated `eutric`
report that mentions eutrophic water as a non-conflation warning.
