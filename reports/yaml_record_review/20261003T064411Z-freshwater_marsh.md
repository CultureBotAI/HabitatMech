# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/terrestrial/freshwater_marsh.yaml`
- Started UTC: 2026-10-03T06:44:11Z
- Finished UTC: 2026-10-03T06:44:11Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `ENVO:00000053` |
| Label | `freshwater marsh` |
| Class | `HabitatRecord` |
| Category | `TERRESTRIAL` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Maintained owner | Generated from the GOLD ecosystem inventory and committed ENVO ontology extract; generated YAML remains read-only |
| Locked slug | `data/habitats/PATHS.tsv:459` maps `ENVO:00000053` to `freshwater_marsh` |

This is the seeded GOLD/ENVO record for `freshwater marsh`. GOLD supplies the
canonical terminal path `Environmental > Terrestrial > Soil > Wetland-upland
transition > Freshwater marsh`, and the seeder resolves that leaf by exact
label to `ENVO:00000053`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/terrestrial/freshwater_marsh.yaml` | Pass; `linkml-validate` reported `No issues found` |
| `just validate-strict data/habitats/terrestrial/freshwater_marsh.yaml` | Pass; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just qc` | Pass; all HabitatMech quality gates passed |
| `git diff --check` | Pass; no whitespace or patch errors after this report was staged |

## Identity and Grounding

The ENVO identity, generated filename, and broader parents are supported by the
GOLD inventory and ENVO extract:

- `data/habitats/PATHS.tsv:459` pins `ENVO:00000053` to slug
  `freshwater_marsh`, matching the reviewed YAML path.
- `data/raw/gold_ecosystem_paths.tsv:1715` is the exact GOLD row; it records
  the canonical path, leaf label `Freshwater marsh`, GOLD node
  `gold.ecosystem:8260`, and zero organism, genome, sample, and study
  assertions.
- `data/raw/ontology_terms.tsv:6647` is the ENVO term row for
  `freshwater marsh` and supplies the definition, `A marsh in which soils are
  saturated with water that contains low concentrations of salts.`
- `data/raw/ontology_subclass_edges.tsv:4681` records the direct ENVO
  `rdfs:subClassOf` edge from `ENVO:00000053` to `ENVO:00000035`; the target is
  labelled `marsh` by `data/raw/ontology_terms.tsv:6631`.
- `data/raw/gold_ecosystem_paths.tsv:1714` records the direct GOLD parent path
  `Environmental > Terrestrial > Soil > Wetland-upland transition`. Its seeded
  identifier is `habitatmech:GOLD.7465227149`, matching the SHA-1-derived
  `mint("GOLD", row["canonical_path"])` fallback in `src/habitatmech/seed.py`.
- `curation/samples/exact-20260814.tsv:17` independently samples this exact
  GOLD/ENVO pair and marks it `ok`.

The rendered page mirrors these generated fields:

- `pages/habitats/freshwater-marsh-envo-00000053.html:24` renders
  `ENVO:00000053`.
- `pages/habitats/freshwater-marsh-envo-00000053.html:64` links to
  `data/habitats/terrestrial/freshwater_marsh.yaml`.
- `pages/category/terrestrial-2.html:287` links the terrestrial browse table to
  `freshwater-marsh-envo-00000053.html`.
- The source attestation table renders the GOLD source path exactly and leaves
  assertions blank, matching the zero-count GOLD source row.
- The broader-habitat list links both `ENVO:00000035` and
  `habitatmech:GOLD.7465227149`, matching `parent_habitats`.

`grounding_status: EXACT` and `mapping_status: SEEDED` are expected for this
record. The GOLD seeder exact-matches the leaf label to ENVO and then adds the
immediate GOLD parent concept in its second pass; ignored/hidden-inclusive
exact searches found no curation decision for `ENVO:00000053`,
`gold.ecosystem:8260`, or the fallback `habitatmech:GOLD.04d1069c2d` source
key.

## Evidence

Every generated scientific claim in this record is source-derived:

| Claim | Nearest source | Review |
|---|---|---|
| ENVO identifier, label, definition, and definition source | `data/raw/ontology_terms.tsv:6647` | Supported exactly |
| `TERRESTRIAL` category | `data/raw/gold_ecosystem_paths.tsv:1715` under `Environmental > Terrestrial > Soil` | Supported exactly |
| GOLD `source_attestations` entry for `gold.ecosystem:8260`, label `Freshwater marsh`, path `Environmental > Terrestrial > Soil > Wetland-upland transition > Freshwater marsh`, and `skos:exactMatch` predicate | `data/raw/gold_ecosystem_paths.tsv:1715` and exact ENVO resolution | Supported exactly |
| Omitted assertion count and unit | `data/raw/gold_ecosystem_paths.tsv:1715` records zero asserted organisms, genomes, samples, and studies | Supported exactly |
| ENVO broader habitat `ENVO:00000035` | `data/raw/ontology_subclass_edges.tsv:4681` | Supported exactly |
| GOLD broader habitat `habitatmech:GOLD.7465227149` | `data/raw/gold_ecosystem_paths.tsv:1714` and GOLD second-pass parent insertion | Supported exactly |

The record has no synonyms, characteristic taxa, xrefs, environmental
parameters, curator evidence, causal graphs, discussion links, or datasets.
Those absences are consistent with a zero-assertion GOLD-only seeded ENVO term
with no curation overlay.

## Completeness

No consequential slot is underfilled for the maintained inputs that feed this
record:

- The sole `source_attestations` entry captures the complete terminal GOLD
  source row.
- `parent_habitats` records the direct ENVO parent and the direct GOLD source
  parent.
- The absent `assertion_count` and `assertion_unit` fields match the zero
  organism count in the GOLD inventory.
- The absence of `characteristic_taxa` rows matches the GOLD source row's zero
  asserted organisms.

Ignored/hidden-inclusive exact searches covered `curation`, `history`,
`research`, `reports/yaml_record_review`, `conf`, `data/raw`,
`data/habitats/PATHS.tsv`, the generated target page, the generated target YAML,
and the relevant rendered terrestrial index page. They found the expected GOLD
row, ENVO rows, slug lock, sample row, generated YAML, rendered page, and
rendered category link, with no item-level override, history record,
target-specific research report, causal overlay, or prior exact
`freshwater_marsh` review report.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the same focused validation set if a future curation change redirects
this GOLD term or adds a causal graph:

- `just validate data/habitats/terrestrial/freshwater_marsh.yaml`
- `just validate-strict data/habitats/terrestrial/freshwater_marsh.yaml`
- `just qc`
- `git diff --check`

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -type f -name
  '*freshwater_marsh*'` found no pre-existing exact review report for this
  record before this file was written.
- `find curation history research reports -name '*freshwater_marsh*'` found no
  maintained target-specific history, research, report, or causal overlay
  artifacts before this file was written.
- Exact ignored/hidden-inclusive content searches for `ENVO:00000053`,
  `freshwater_marsh`, `freshwater-marsh-envo-00000053`,
  `gold.ecosystem:8260`, and `04d1069c2d` found only the raw rows, path lock,
  generated YAML, rendered HTML, and sample row cited above.
