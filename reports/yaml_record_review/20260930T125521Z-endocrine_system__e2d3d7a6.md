# YAML Record Review: Endocrine system

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/endocrine_system__e2d3d7a6.yaml`
- Started UTC: 2026-09-30T12:55:21Z
- Finished UTC: 2026-09-30T12:55:21Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.d275fc9ccd` |
| Label | Endocrine system |
| Category | `HOST_ASSOCIATED` |
| Grounding | `NARROW` |
| Mapping | `SEEDED` |
| Stable slug | `endocrine_system__e2d3d7a6` |
| Source concept | `GOLD`, `gold.ecosystem:7592`, `Host-associated > Fish > Endocrine system`, `skos:narrowMatch` |
| Maintained owners | `data/raw/gold_ecosystem_paths.tsv`, `data/raw/ontology_terms.tsv`, `data/habitats/PATHS.tsv` |
| Generated products checked | `data/habitats/host_associated/endocrine_system__e2d3d7a6.yaml`, `pages/habitats/endocrine-system-habitatmech-gold-d275fc9ccd.html` |

The target is the generated GOLD record for the Fish-specific
`Endocrine system` path. It is intentionally minted because the GOLD source path
is narrower than generic `UBERON:0000949` `endocrine system`: the path fixes the
host branch to Fish, while the UBERON class names an anatomical system across
animals.

The generated record has one GOLD source attestation, no assertion count, no
authored definition, no synonyms, no environmental parameters, no characteristic
taxa, no record-level evidence block, and no causal graph.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/endocrine_system__e2d3d7a6.yaml` | Pass; `linkml-validate` reported no issues. |
| `just validate-strict data/habitats/host_associated/endocrine_system__e2d3d7a6.yaml` | Pass; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Pass; no issues found and 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Pass; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Pass; 3206 expected records, 3206 on disk, 0 missing, 0 extra, 0 differing. |
| `just worklist --status all --out /tmp/habitat_worklist_fish_endocrine.tsv` | Pass; wrote 953 ungrounded backlog rows. `habitatmech:GOLD.d275fc9ccd` is `NARROW`, not `UNGROUNDED`, so it was correctly absent from that worklist. |
| `just report` | Pass; reported 3206 records and 686 `REVIEWED` records. |
| `just report --out /tmp/habitatmech_fish_endocrine_report.tsv` | Pass; wrote the TSV snapshot and reported this target as a `HOST_ASSOCIATED`, `NARROW`, `SEEDED`, GOLD-only record with 1 source, 0 assertions, 2 parents, no definition, no environmental parameters, no characteristic taxa, and no causal graph. |

## Identity and Grounding

The generated identity is sound. `data/raw/gold_ecosystem_paths.tsv` has the
exact raw row `Host-associated > Fish > Endocrine system`, with leaf label
`Endocrine system`, depth 3, three collapsed GOLD ecosystem node IDs, zero
organism, study, biosample, and total assertion counts, and source IDs
`gold.ecosystem:7592|gold.ecosystem:7593|gold.ecosystem:7594`.

`data/habitats/PATHS.tsv` pins `habitatmech:GOLD.d275fc9ccd` to the stable
`endocrine_system__e2d3d7a6` slug, and the generated target YAML uses that
identifier and slug for exactly this Fish source path.

The `NARROW` grounding against `UBERON:0000949` is appropriate. The vendored
ontology slice labels `UBERON:0000949` as `endocrine system` and defines it as
the anatomical system that consists of glands and gland parts that produce
endocrine secretions. The GOLD source path adds the Fish host context, so the
record should stay a minted habitat narrower than the generic UBERON anatomy
class rather than adopting `UBERON:0000949` as an exact identity.

The two generated parents are traceable to input data:

| Parent | Support |
|---|---|
| `UBERON:0000949` | The source leaf exactly matches the UBERON `endocrine system` anatomy label, and the generic anatomy class is broader than this Fish-specific source concept. |
| `habitatmech:GOLD.3d529a667e` | GOLD has the immediate broader path `Host-associated > Fish`; that generated record is the exact raw parent path. |

The target is distinct from the other minted host-associated `Endocrine system`
source paths that share `UBERON:0000949` as a broader anatomical parent. Those
records preserve their own GOLD host-branch context in separate
`habitatmech:GOLD.*` identifiers instead of merging onto the generic UBERON
term.

## Evidence

The record carries no curator-authored evidence block. Its identity is backed by
the GOLD path inventory and the seeder's lexical narrower-than-ontology route,
not by an item-level curation decision.

The zero assertion total is supported by the raw GOLD inventory. Hidden- and
ignored-inclusive exact searches for the exact Fish Endocrine system source path
found no rows in `data/raw/gold_path_biosamples.tsv`,
`data/raw/gold_path_triads.tsv`, or `data/raw/gold_studies.tsv`; the only exact
raw hit was the `data/raw/gold_ecosystem_paths.tsv` row that reports zero
organisms, zero studies, zero biosamples, and zero total assertions.

The `gold.ecosystem:7592` representative source ID appears only in the generated
record and the raw GOLD row, while the sibling collapsed node IDs
`gold.ecosystem:7593` and `gold.ecosystem:7594` appear only in that raw GOLD row.
That matches the generated attestation note saying that three GOLD ecosystem
node IDs share this path and only the first is shown.

Hidden- and ignored-inclusive exact searches found no maintained causal overlay,
item-level curation decision, term-request row, history record, research report,
or prior exact review report keyed by `habitatmech:GOLD.d275fc9ccd`,
`endocrine_system__e2d3d7a6`, `gold.ecosystem:7592`, `gold.ecosystem:7593`,
`gold.ecosystem:7594`, or the exact Fish Endocrine system source path.

iModulonDB was not applicable: the record names a host anatomical-system
habitat, not a covered microbial gene, regulator, strain, locus tag, protein,
stress response, or transcriptomics dataset.

## Completeness

The rendered page
`pages/habitats/endocrine-system-habitatmech-gold-d275fc9ccd.html` reflects the
same minted identifier, label, category, `NARROW` grounding, `SEEDED` mapping
status, GOLD source path, collapsed-node note, and two broader habitats as the
YAML.

Empty optional slots are appropriate for this seeded zero-assertion parent
record. No raw side-table rows support environmental parameters or
characteristic taxa, and no maintained overlay supplies causal graphs.

## Findings

None found.

## Recommended Edits

None found.

## Follow-up Checks

None required.

## Additional Notes

The hidden-inclusive search for `fish endocrine` in the vendored ontology slice,
curation inputs, history, research reports, and prior review reports found no
Fish-specific exact ontology term that would supersede the generated
`UBERON:0000949` broader parent. This was scoped to the current vendored slice;
it was not a live ontology search.
