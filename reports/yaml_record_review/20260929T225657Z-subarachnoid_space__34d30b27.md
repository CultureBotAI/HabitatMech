# YAML Record Review: Subarachnoid space

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/subarachnoid_space__34d30b27.yaml`
- Started UTC: `2026-09-29T22:50:20Z`
- Finished UTC: `2026-09-29T22:56:57Z`
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.ce83e63059` |
| Label | `Subarachnoid space` |
| Stable slug | `subarachnoid_space__34d30b27` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Source concept | `habitatmech:GOLD.ce83e63059` |
| Source attestation | `GOLD`, `gold.ecosystem:7486`, `Host-associated > Birds > Nervous system > Subarachnoid space`, `skos:narrowMatch` |

The record is the generated GOLD concept for the Bird-specific
`Subarachnoid space` path. It is intentionally minted because
`Host-associated > Birds > Nervous system > Subarachnoid space` is narrower
than the generic UBERON `subarachnoid space` anatomy class. The generated
record preserves `UBERON:0000315` as a broader anatomical parent and
`habitatmech:GOLD.bbbdbf55b3` as the immediate GOLD source-path parent for
`Host-associated > Birds > Nervous system`.

The record has one GOLD source attestation, no assertion count, no authored
definition, no synonyms, no environmental parameters, no characteristic taxa,
no record-level evidence block, and no causal graphs.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/subarachnoid_space__34d30b27.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/habitats/host_associated/subarachnoid_space__34d30b27.yaml` | Passed; 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206 on disk, with 0 missing, 0 extra, and 0 differing. |
| `just report --ungrounded-top 0 --out /private/tmp/habitatmech-report-bird-subarachnoid-space.tsv` | Passed; wrote the TSV snapshot and reported `habitatmech:GOLD.ce83e63059` as `NARROW`, `SEEDED`, 1 source, 0 assertions, no definition, 2 parents, 0 parameters, 0 taxa, and 0 causal graphs. |
| `just worklist --limit 40 --status all --out /private/tmp/habitatmech-worklist-bird-subarachnoid-space.tsv` | Passed; wrote 953 ungrounded backlog rows. `habitatmech:GOLD.ce83e63059` is NARROW, not UNGROUNDED, so it is not a ranked ungrounded item. |

## Identity and Grounding

The generated identity is sound. `data/raw/gold_ecosystem_paths.tsv` has the
exact source row `Host-associated > Birds > Nervous system > Subarachnoid
space` with leaf label `Subarachnoid space`, depth 4, two collapsed GOLD
ecosystem node IDs, zero aggregate assertions, and source IDs
`gold.ecosystem:7486|gold.ecosystem:7487`.

`data/habitats/PATHS.tsv` pins `habitatmech:GOLD.ce83e63059` to the stable
`subarachnoid_space__34d30b27` slug, and the generated target YAML uses that
identifier and slug for exactly this Bird source path.

The `NARROW` grounding against `UBERON:0000315` is appropriate. The vendored
ontology slice labels `UBERON:0000315` as `subarachnoid space` and defines it
as the space between the arachnoid and pia mater. The GOLD source path adds
Bird and Nervous system context, so the record should stay a minted habitat
narrower than the generic UBERON anatomy term rather than adopting
`UBERON:0000315` as an exact identity.

The two generated parents are traceable to input data:

| Parent | Support |
|---|---|
| `UBERON:0000315` | The GOLD leaf is a case variant of the generic UBERON `subarachnoid space` anatomy label, and the UBERON term is broader than this Bird-specific source concept. |
| `habitatmech:GOLD.bbbdbf55b3` | GOLD has the immediate broader path `Host-associated > Birds > Nervous system`; that path generates the record's source-path parent. |

The target is distinct from the other minted host-associated Subarachnoid space
source paths for Mammals and Mammals: Human. Those records preserve their own
host-clade context in separate `habitatmech:GOLD.*` identifiers instead of
merging onto `UBERON:0000315`.

## Evidence

The record carries no curator-authored evidence block. Its identity is backed
by the GOLD path inventory and the seeder's lexical narrower-than-ontology
route, not by an item-level curation decision.

The zero assertion total is supported by the raw GOLD inventory. The exact raw
row reports `organism_count = 0`, `study_count = 0`, `biosample_count = 0`,
`mixs_triad_count = 0`, `gold_triad_count = 0`, and `total_assertions = 0` for
this path, and an ignored/hidden-inclusive search for `gold.ecosystem:7486`
and `gold.ecosystem:7487` found no rows in
`data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, or
`data/raw/gold_studies.tsv`.

No causal graph is attached to this record. Ignored/hidden-inclusive searches
found no causal overlay keyed by `habitatmech:GOLD.ce83e63059`, the
`subarachnoid_space__34d30b27` slug, or either exact source GOLD ecosystem ID
under `curation/causal_graphs`.

## Completeness

- The rendered page
  `pages/habitats/subarachnoid-space-habitatmech-gold-ce83e63059.html`
  reflects the same minted identifier, label, category, `NARROW` grounding,
  `SEEDED` mapping status, GOLD source path, and two broader habitats as the
  YAML.
- The exact ignored/hidden-inclusive search for
  `habitatmech:GOLD.ce83e63059`, `subarachnoid_space__34d30b27`,
  `gold.ecosystem:7486`, `gold.ecosystem:7487`, and the full source path
  covered `curation`, `history`, `research`, `conf/`, and prior YAML review
  reports. It found no target-specific maintained curation artifact, research
  report, history record, causal-graph overlay, or prior exact review.
- Empty optional slots are appropriate for this seeded zero-assertion record.
  No raw side-table rows support generated environmental parameters or taxa,
  and no maintained overlay supplies causal graphs.

## Findings

None found.

## Recommended Edits

None found.

## Follow-up Checks

None required.

## Additional Notes

- `Host-associated > Birds > Nervous system > Subarachnoid space >
  Cerebrospinal fluid` is the only generated Bird child found for this path.
  Its parent list correctly includes `habitatmech:GOLD.ce83e63059`.
- iModulonDB structured source checks were not applicable: the record names a
  GOLD anatomical habitat path and no genes, locus tags, regulators, pathways,
  stress-response terms, or transcriptomic datasets.
