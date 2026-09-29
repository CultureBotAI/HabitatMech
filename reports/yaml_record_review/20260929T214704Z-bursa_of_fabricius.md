# YAML Record Review: bursa of Fabricius

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/bursa_of_fabricius.yaml`
- Started UTC: `2026-09-29T21:40:00Z`
- Finished UTC: `2026-09-29T21:47:04Z`
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `UBERON:0003903` |
| Label | `bursa of Fabricius` |
| Stable slug | `bursa_of_fabricius` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Source concept | `habitatmech:GOLD.dfef770cb8` |
| Source attestation | `GOLD`, `gold.ecosystem:7474`, `Host-associated > Birds > Lymphatic system > Bursa of Fabricius`, `skos:exactMatch` |

The record is a generated, seeded, GOLD-only host-associated habitat for the
UBERON anatomical class `bursa of Fabricius`. It has three direct UBERON
parents, one source-path parent for `Host-associated > Birds > Lymphatic system`,
one GOLD source attestation, no source assertion count, no environmental
parameters, no characteristic taxa, no record-level evidence block, and no
causal graphs.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/bursa_of_fabricius.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/habitats/host_associated/bursa_of_fabricius.yaml` | Passed; 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206 on disk, with 0 missing, 0 extra, and 0 differing. |
| `just report --ungrounded-top 0 --out /private/tmp/habitatmech-report-bird-bursa.tsv` | Passed; wrote the TSV snapshot and reported `UBERON:0003903` as `EXACT`, `SEEDED`, 1 source, 0 assertions, definition present, 4 parents, 0 parameters, 0 taxa, and 0 causal graphs. |
| `just worklist --limit 40 --status all --out /private/tmp/habitatmech-worklist-bird-bursa.tsv` | Passed; wrote 953 ungrounded backlog rows. `bursa of Fabricius` is exact-grounded and therefore not a ranked ungrounded item. |

## Identity and Grounding

The identity is internally consistent. `data/raw/ontology_terms.tsv` contains
`UBERON:0003903` with the canonical label `bursa of Fabricius` and an UBERON
definition for the epithelial and lymphoid organ in birds; the generated record
copies the identifier, label, definition, and `definition_source: UBERON`.

The GOLD source identity is exact. `data/raw/gold_ecosystem_paths.tsv` contains
the canonical path `Host-associated > Birds > Lymphatic system > Bursa of
Fabricius` with leaf label `Bursa of Fabricius`, depth 4, two collapsed GOLD
ecosystem node IDs, zero aggregate assertions, and source IDs
`gold.ecosystem:7474|gold.ecosystem:7475`. The generated `source_attestations`
entry stores `gold.ecosystem:7474` as the representative source ID and preserves
the fact that two GOLD node IDs share the path in its note.

The parents are traceable to generated inputs:

| Parent | Support |
|---|---|
| `UBERON:0004177` | `data/raw/ontology_subclass_edges.tsv` asserts `UBERON:0003903 rdfs:subClassOf UBERON:0004177`; `data/raw/ontology_terms.tsv` labels the parent `hemopoietic organ`. |
| `UBERON:0011510` | `data/raw/ontology_subclass_edges.tsv` asserts `UBERON:0003903 rdfs:subClassOf UBERON:0011510`; `data/raw/ontology_terms.tsv` labels the parent `cloacal bursa`. |
| `UBERON:0013765` | `data/raw/ontology_subclass_edges.tsv` asserts `UBERON:0003903 rdfs:subClassOf UBERON:0013765`; `data/raw/ontology_terms.tsv` labels the parent `digestive system element`. |
| `habitatmech:GOLD.f65007e88e` | GOLD has the immediate broader path `Host-associated > Birds > Lymphatic system`; the target source path is its `Bursa of Fabricius` child. |

`mapping_status: SEEDED` is correct. The exact ignored/hidden-inclusive search
for the source concept key, `habitatmech:GOLD.dfef770cb8`, found no
`curation/decisions.tsv` row; the seeder's exact lexical match is therefore not
yet item-reviewed.

## Evidence

The record carries no curator-authored evidence block and needs none for a
seeded, source-attested ontology match. Its only scientific content beyond the
ontology definition is the GOLD attestation and parentage described above.

The zero assertion total is supported by the raw GOLD inventory. The exact raw
row reports `organism_count = 0`, `study_count = 0`, `biosample_count = 0`,
`mixs_triad_count = 0`, `gold_triad_count = 0`, and `total_assertions = 0` for
this path, and an ignored/hidden-inclusive search for `gold.ecosystem:7474` and
`gold.ecosystem:7475` found no rows in `data/raw/gold_path_biosamples.tsv`,
`data/raw/gold_path_triads.tsv`, or `data/raw/gold_studies.tsv`.

No causal graph is attached to this record. Ignored/hidden-inclusive searches
found no causal overlay keyed by `UBERON:0003903`,
`habitatmech:GOLD.dfef770cb8`, either exact GOLD ecosystem ID, or `bursa` under
`curation/causal_graphs`.

## Completeness

- The exact path is represented once in the generated corpus:
  `data/habitats/PATHS.tsv` pins `UBERON:0003903` to `bursa_of_fabricius`,
  and `data/habitats/host_associated/bursa_of_fabricius.yaml` is the generated
  target for that slug.
- Empty optional slots are appropriate. No raw side-table rows support seeded
  environmental parameters or taxa, and no maintained causal overlay supplies
  causal graphs.
- The rendered page `pages/habitats/bursa-of-fabricius-uberon-0003903.html`
  reflects the same identifier, label, category, grounding status, mapping
  status, UBERON definition, GOLD source path, and four broader habitats as the
  generated YAML.
- Ignored/hidden-inclusive searches found no preexisting Bursa of
  Fabricius-specific review report, research report, curation history record,
  or causal-graph artifact under `reports/yaml_record_review`,
  `research/habitats`, `history`, or `curation/causal_graphs`.

## Findings

None found.

## Recommended Edits

None found.

## Follow-up Checks

- If an item-level decision is added for `habitatmech:GOLD.dfef770cb8`, rerun
  `just seed`, `just seed-canary UBERON:0003903`, and
  `just validate data/habitats/host_associated/bursa_of_fabricius.yaml` before
  any full `just seed-apply --force`.
- If a causal overlay is added for `UBERON:0003903`, run
  `just validate-causal curation/causal_graphs/<file>.yaml`,
  `just validate-causal-all`, and
  `just validate-strict data/habitats/host_associated/bursa_of_fabricius.yaml`.
- Rerun `just verify-corpus --max-diffs 1` after any maintained input edit to
  prove the generated record still reproduces from `data/raw/` plus curation
  overlays.

## Additional Notes

- The source-concept key `habitatmech:GOLD.dfef770cb8` is
  `mint("GOLD", "Host-associated > Birds > Lymphatic system > Bursa of Fabricius")`
  from `src/habitatmech/seed.py`.
- `research/habitats/host_associated/birds-habitatmech-gold-47e603cf4f-deep-research-claude_code.md`
  mentions `bursa of Fabricius` only while distinguishing bird anatomical
  parts from the parent host-clade concept. It is a parent-context lead, not a
  maintained input for this record.
- The exact ignored/hidden-inclusive search for `Bursa of Fabricius`,
  `bursa_of_fabricius`, `bursa-of-fabricius`, `habitatmech:GOLD.dfef770cb8`,
  `UBERON:0003903`, `gold.ecosystem:7474`, `gold.ecosystem:7475`, and the full
  source path covered maintained curation inputs, history, research, review
  reports, `conf/`, `data/raw/`, and `data/habitats/`; no target-specific
  maintained artifact was found beyond the raw GOLD row, raw ontology rows,
  locked slug row, and generated YAML described above.
