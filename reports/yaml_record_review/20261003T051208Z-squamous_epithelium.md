# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/squamous_epithelium.yaml`
- Started UTC: 2026-10-03T05:12:08Z
- Finished UTC: 2026-10-03T05:12:08Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `BTO:0002072` |
| Label | `squamous epithelium` |
| Class | `HabitatRecord` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Maintained owner | Generated from the PREGO habitat inventory and committed BTO ontology extract; generated YAML remains read-only |
| Locked slug | `data/habitats/PATHS.tsv:325` maps `BTO:0002072` to `squamous_epithelium` |

This is the seeded PREGO/BTO record for `squamous epithelium`.
PREGO names `BTO:0002072` directly, so the seed path self-grounds the
identifier as `EXACT` unless a curator overrides the addressable PREGO source
key, `habitatmech:PREGO.61e6ec58cc`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/squamous_epithelium.yaml` | Pass; `linkml-validate` reported `No issues found` |
| `just validate-strict data/habitats/host_associated/squamous_epithelium.yaml` | Pass; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just qc` | Pass; all HabitatMech quality gates passed |
| `git diff --check` | Pass; no whitespace or patch errors after this report was staged |

## Identity and Grounding

The BTO identity, generated filename, and broader parent are supported by the
PREGO inventory and BTO extract:

- `data/habitats/PATHS.tsv:325` pins `BTO:0002072` to slug
  `squamous_epithelium`, matching the reviewed YAML path.
- `data/raw/prego_habitats.tsv:620` is the exact PREGO habitat row; it records
  `BTO:0002072`, ontology `BTO`, Biolink type
  `biolink:GrossAnatomicalStructure`, `taxon_count` 1, `max_prego_score` 3,
  evidence channel `annotated_genomes_isolates`, and synonyms
  `squamous epithelia`, `squamous epithelial`, `squamous epithelium`, and
  `squamous epitheliums`.
- `data/raw/ontology_terms.tsv:2072` is the BTO term row for
  `squamous epithelium` and supplies the definition, `Epithelium composed of
  flattened platelike cells.`
- `data/raw/ontology_subclass_edges.tsv:1408` records the direct BTO
  `rdfs:subClassOf` edge from `BTO:0002072` to `BTO:0000416`.
- `data/raw/ontology_terms.tsv:418` labels `BTO:0000416` as `epithelium`,
  matching the rendered broader-habitat link.
- `curation/samples/exact-20260814.tsv:14` independently samples this exact
  PREGO/BTO pair and marks it `ok`.

The rendered page mirrors these generated fields:

- `pages/habitats/squamous-epithelium-bto-0002072.html:24` renders
  `BTO:0002072`.
- `pages/habitats/squamous-epithelium-bto-0002072.html:43` renders the PREGO
  source label `squamous epithelium`.
- `pages/habitats/squamous-epithelium-bto-0002072.html:75` renders the three
  generated PREGO synonyms that differ from the canonical label.
- `pages/category/host-associated-3.html:1799` links the host-associated browse
  table to `squamous-epithelium-bto-0002072.html`.

`grounding_status: EXACT` and `mapping_status: SEEDED` are expected for this
record. The PREGO seeder treats ontology CURIEs as self-grounded by default,
and ignored/hidden-inclusive exact searches found no curation decision for
`habitatmech:PREGO.61e6ec58cc` or `BTO:0002072`.

## Evidence

Every generated scientific claim in this record is source-derived:

| Claim | Nearest source | Review |
|---|---|---|
| BTO identifier, label, definition, definition source, and `HOST_ASSOCIATED` category | `data/raw/prego_habitats.tsv:620`, `data/raw/ontology_terms.tsv:2072`, and the BTO prefix-to-category rule | Supported exactly |
| PREGO `source_attestations` entry with 1 `TAXON` assertion, score 3.0, and `annotated_genomes_isolates` evidence channel | `data/raw/prego_habitats.tsv:620` | Supported exactly |
| PREGO synonyms | `data/raw/prego_habitats.tsv:620` | Supported exactly; the synonym equal to the canonical label is intentionally omitted |
| Broader BTO parent `BTO:0000416` | `data/raw/ontology_subclass_edges.tsv:1408` | Supported exactly |
| Associated taxon `NCBITaxon:1328859`, label `Escherichia coli O157:H7 str. SS17`, score 3.0, rank 1, and pool 1 | `data/raw/prego_habitat_taxa.tsv:2540` and `data/raw/prego_habitats.tsv:620` | Supported exactly |

The record has no xrefs, environmental parameters, curator evidence,
causal graphs, discussion links, or datasets. Those absences are consistent
with a PREGO-only seeded anatomy term with no curation overlay.

## Completeness

No consequential slot is underfilled for the maintained inputs that feed this
record:

- The sole `source_attestations` entry captures the complete PREGO/BTO habitat
  assertion.
- The sole `characteristic_taxa` row captures the complete PREGO taxon row for
  `BTO:0002072`.
- `parent_habitats` records the single direct BTO parent for `BTO:0002072`.
- PREGO synonym propagation preserves all upstream alternates except the
  canonical label itself.

Ignored/hidden-inclusive exact searches covered `curation`, `history`,
`research`, `reports/yaml_record_review`, `conf`, `data/raw`,
`data/habitats/PATHS.tsv`, the generated target page, the generated target YAML,
and the relevant rendered host-associated index page. They found the expected
PREGO rows, BTO rows, slug lock, sample row, and rendered links, with no
item-level override, history record, target-specific research report, causal
overlay, or prior exact `squamous_epithelium` review report.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the same focused validation set if a future curation change redirects
this PREGO term or adds a causal graph:

- `just validate data/habitats/host_associated/squamous_epithelium.yaml`
- `just validate-strict data/habitats/host_associated/squamous_epithelium.yaml`
- `just qc`
- `git diff --check`

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*squamous_epithelium*'`
  found no pre-existing exact review report for this record before this file was
  written.
- `find curation history research reports -name '*squamous_epithelium*'` found
  no maintained target-specific history, research, report, or causal overlay
  artifacts before this file was written.
- `find curation history research reports -name '*61e6ec58cc*'` found no
  maintained item-level curation artifact for the addressable PREGO source key
  before this file was written.
- Exact ignored/hidden-inclusive content searches for `BTO:0002072`,
  `squamous_epithelium`, `squamous-epithelium`, and `61e6ec58cc` found the raw
  rows, path lock, generated YAML, rendered HTML, and sample row cited above.
