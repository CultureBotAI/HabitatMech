# YAML Record Review: zoological garden

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/other/zoological_garden.yaml
- Started UTC: 2026-09-21T04:13:00Z
- Finished UTC: 2026-09-21T04:16:10Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/other/zoological_garden.yaml` |
| Class | `HabitatRecord` |
| Identifier | `ENVO:00010625` |
| Label | `zoological garden` |
| Category | `OTHER` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Maintained status | generated from `data/raw/` and `data/habitats/PATHS.tsv` |

The generated record is compact:

- ENVO supplies the identifier, canonical label, definition, exact synonyms, and
  `ENVO:00000011` parent.
- PREGO supplies one `biolink:OntologyClass` attestation for
  `ENVO:00010625` and one associated taxon, `NCBITaxon:593135`
  `Orbus hercynius`.
- No curator-owned evidence, environmental parameters, causal graphs,
  discussions, datasets, xrefs, or item-level curation decisions are present.

## Validation

| Check | Result |
|---|---|
| `.venv/bin/python -c "from linkml.validator.cli import cli; cli()" --schema src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/other/zoological_garden.yaml` | Passed; no LinkML issues. |
| `.venv/bin/python scripts/validate_strict.py data/habitats/other/zoological_garden.yaml --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| `.venv/bin/python scripts/build_term_requests.py --check` | Passed; term-request table is current at 109 terms. |
| `.venv/bin/python scripts/verify_corpus.py --max-diffs 1` | Passed; 3,206 expected records, 3,206 found, no missing/extra/differing records. |
| `.venv/bin/python scripts/validate_history.py` | Passed; 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| Reference validator | Not checked: this record has no DOI/PMID/URL `EvidenceItem` or causal-edge evidence, and no matching `research/habitats/` report requiring `scripts/check_report_citations.py` exists. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| The record denotes `ENVO:00010625` `zoological garden`. | `data/raw/ontology_terms.tsv` contains `ENVO:00010625`, ontology `ENVO`, label `zoological garden`, definition "A facility in which animals are confined within enclosures and displayed to the public, and in which they may also be bred.", exact synonyms `zoo\|zoological park`, `directly_referenced=TRUE`, and `label_only=FALSE`. | Supported exactly. |
| The record's broader parent is `ENVO:00000011`. | `data/raw/ontology_subclass_edges.tsv` contains `ENVO:00010625 rdfs:subClassOf ENVO:00000011`; `data/raw/ontology_terms.tsv` labels `ENVO:00000011` as `garden`. | Supported exactly. |
| The stable file stem is `zoological_garden`. | `data/habitats/PATHS.tsv` maps `ENVO:00010625` to `zoological_garden`. | Supported exactly. |
| PREGO directly attests the same ontology class. | `data/raw/prego_habitats.tsv` has `prego_id=ENVO:00010625`, `ontology=ENVO`, `biolink_category=biolink:OntologyClass`, `taxon_count=1`, `direct_assertion_count=1`, `max_prego_score=3`, channel `annotated_genomes_isolates`, and source synonyms including `zoo`, `zoological garden`, `zoological gardens`, `zoological park`, `zoological parkic`, and `zoological parks`. | Supported exactly; the PREGO ID is the same ENVO CURIE as the record ID. |

The `mapping_status: SEEDED` value is correct for a source-derived record with
no item-level row in `curation/decisions.tsv`: the seeder does not promote a
record to `REVIEWED` from a lexical/source match alone.

## Evidence

| Claim | Evidence | Assessment |
|---|---|---|
| `Orbus hercynius` is the top PREGO-associated taxon for the zoological garden habitat. | `data/raw/prego_habitat_taxa.tsv` has row `ENVO:00010625`, rank `1`, `NCBITaxon:593135`, label `Orbus hercynius`, PREGO score `3`, `direct_flag=TRUE`, channel `annotated_genomes_isolates`, and no `corroborated_by` source. | Supported exactly. |
| The `Orbus hercynius` entry is not a curator assertion that this taxon typifies zoological gardens. | The generated YAML omits `is_characteristic` and `reference`. `src/habitatmech/schema/habitatmech.yaml`, `README.md`, and `docs/HARMONIZATION.md` all state that seeded PREGO taxa record observed/reported associations and that `is_characteristic` is the stronger curator-set flag. | Supported; no overclaim found. |

No claim-level literature evidence was present or required. The record has no
causal graph, so there are no causal edges or snippets to audit.

## Completeness

- The record is complete enough for a seeded, exact ENVO/PREGO harmonization
  record.
- Empty `evidence`, `environmental_parameters`, `causal_graphs`, `discussions`,
  and `datasets` are acceptable here. No maintained input supplies those
  fields for this record, and there is no curator-authored overlay to validate.
- Ignored/hidden-inclusive exact searches covered `data`, `curation`,
  `research`, `docs`, `src`, and `.claude`, excluding only generated text-map,
  cache, and build trees, for `ENVO:00010625`, `zoological garden`, and
  `zoological_garden`. They found only the generated record, its `PATHS.tsv`
  row, the ENVO ontology rows, and PREGO raw rows.
- A bounded `find reports -maxdepth 2` search covered ignored files under
  `reports/` and found no prior `reports/yaml_record_review/` report.
- Exact searches for `NCBITaxon:593135` and `Orbus hercynius` found only the
  PREGO raw taxon row and generated record entry.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If this record is curated later, the narrowest proof is:

- add an `ITEM` row to `curation/decisions.tsv`;
- run a single-record seed canary for `ENVO:00010625`;
- rerun strict validation on `data/habitats/other/zoological_garden.yaml`;
- rerun `scripts/verify_corpus.py`.

## Additional Notes

- The PREGO-provided related synonym `zoological parkic` is odd English, but it
  is present verbatim in `data/raw/prego_habitats.tsv`; the generated record
  does not invent it.
- `ENVO:01000923` `petting zoo` appears as a narrower child of
  `ENVO:00010625` in `data/raw/ontology_subclass_edges.tsv`; the zoological
  garden record does not incorrectly absorb that child.
