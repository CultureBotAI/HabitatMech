# YAML Record Review: Reproductive system

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/reproductive_system__e62e83f1.yaml`
- Finished UTC: `2026-09-30T01:46:52Z`
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.acf7b9c74c` |
| Label | `Reproductive system` |
| Stable slug | `reproductive_system__e62e83f1` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Source concept | `habitatmech:GOLD.acf7b9c74c` |
| Source attestation | `GOLD`, `gold.ecosystem:8192`, `Host-associated > Bryozoa > Reproductive system`, `skos:narrowMatch` |

The record is the generated GOLD concept for the Bryozoa-specific
`Reproductive system` path. It is intentionally minted because
`Host-associated > Bryozoa > Reproductive system` is narrower than the generic
UBERON `reproductive system` anatomy class. The generated record preserves
`UBERON:0000990` as a broader anatomical parent and
`habitatmech:GOLD.dfaedfff09` as the immediate GOLD source-path parent for
`Host-associated > Bryozoa`.

The record has one GOLD source attestation, no assertion count, no authored
definition, no synonyms, no environmental parameters, no characteristic taxa,
no record-level evidence block, and no causal graphs.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/reproductive_system__e62e83f1.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/habitats/host_associated/reproductive_system__e62e83f1.yaml` | Passed; 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206 on disk, with 0 missing, 0 extra, and 0 differing. |
| `just report --out /private/tmp/habitatmech-report-bryozoa-reproductive-system.tsv` | Passed; wrote the TSV snapshot and reported `habitatmech:GOLD.acf7b9c74c` as `NARROW`, `SEEDED`, 1 source, 0 assertions, no definition, 2 parents, 0 parameters, 0 taxa, and 0 causal graphs. |
| `just worklist --limit 40 --status all --out /private/tmp/habitatmech-worklist-bryozoa-reproductive-system.tsv` | Passed; wrote 953 ungrounded backlog rows. `habitatmech:GOLD.acf7b9c74c` is `NARROW`, not `UNGROUNDED`, so it is not a ranked ungrounded item. |
| `git diff --check` | Passed. |

## Identity and Grounding

The generated identity is sound. `data/raw/gold_ecosystem_paths.tsv` has the
exact source row `Host-associated > Bryozoa > Reproductive system` with leaf
label `Reproductive system`, depth 3, three collapsed GOLD ecosystem node IDs,
zero aggregate assertions, and source IDs
`gold.ecosystem:8192|gold.ecosystem:8193|gold.ecosystem:8194`.

`data/habitats/PATHS.tsv` pins `habitatmech:GOLD.acf7b9c74c` to the stable
`reproductive_system__e62e83f1` slug, and the generated target YAML uses that
identifier and slug for exactly this Bryozoa source path.

The `NARROW` grounding against `UBERON:0000990` is appropriate. The vendored
ontology slice labels `UBERON:0000990` as `reproductive system` and defines it
as the anatomical system whose parts are organs concerned with reproduction.
The GOLD source path adds the Bryozoa host-phylum context, so the record should
stay a minted habitat narrower than the generic UBERON anatomy term rather
than adopting `UBERON:0000990` as an exact identity.

The two generated parents are traceable to input data:

| Parent | Support |
|---|---|
| `UBERON:0000990` | The source leaf exactly matches the UBERON `reproductive system` anatomy label, and the generic anatomy class is broader than this Bryozoa-specific source concept. |
| `habitatmech:GOLD.dfaedfff09` | GOLD has the immediate broader path `Host-associated > Bryozoa`; that generated record is the exact raw parent path. |

The target is also distinct from the other minted host-associated
`Reproductive system` source paths that share `UBERON:0000990` as a broader
anatomical parent. Those records preserve their own GOLD host-branch context
in separate `habitatmech:GOLD.*` identifiers instead of merging onto the
generic UBERON term.

## Evidence

The record carries no curator-authored evidence block. Its identity is backed
by the GOLD path inventory and the seeder's lexical narrower-than-ontology
route, not by an item-level curation decision.

The zero assertion total is supported by the raw GOLD inventory. The exact raw
row reports `organism_count = 0`, `study_count = 0`, `biosample_count = 0`,
`mixs_triad_count = 0`, `gold_triad_count = 0`, and `total_assertions = 0` for
this path, and ignored/hidden-inclusive exact searches for
`gold.ecosystem:8192`, `gold.ecosystem:8193`, `gold.ecosystem:8194`, and the
exact Bryozoa Reproductive system source path found no rows in
`data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, or
`data/raw/gold_studies.tsv`.

The single GOLD biosample and study side-table rows under
`Host-associated > Bryozoa > Reproductive system > Ovicells` are correctly
absent from this parent record. They belong to the generated Ovicells
descendant unless curation later decides to merge or retire that leaf.

No causal graph is attached to this record. Ignored/hidden-inclusive exact
searches found no maintained causal overlay, item-level curation decision,
history record, research report, or configuration row keyed by
`habitatmech:GOLD.acf7b9c74c`, `reproductive_system__e62e83f1`,
`gold.ecosystem:8192`, `gold.ecosystem:8193`, `gold.ecosystem:8194`, or the
exact Bryozoa Reproductive system source path.

## Completeness

- The rendered page
  `pages/habitats/reproductive-system-habitatmech-gold-acf7b9c74c.html`
  reflects the same minted identifier, label, category, `NARROW` grounding,
  `SEEDED` mapping status, GOLD source path, collapsed-node note, and two
  broader habitats as the YAML.
- Before this report was added, exact ignored/hidden-inclusive searches found
  no prior exact review report for
  `data/habitats/host_associated/reproductive_system__e62e83f1.yaml`. The
  existing `reports/yaml_record_review/20260922T153519Z-bryozoa.md` parent
  review references this record only as a generated child of the reviewed
  `Host-associated > Bryozoa` path.
- Empty optional slots are appropriate for this seeded zero-assertion parent
  record. No raw side-table rows support generated environmental parameters or
  taxa, and no maintained overlay supplies causal graphs.

## Findings

None found.

## Recommended Edits

None found.

## Follow-up Checks

None required.

## Additional Notes

- The prior Bryozoa parent review already records the item-level curation need
  for `habitatmech:GOLD.dfaedfff09`. This child report does not add a new
  defect: it confirms the generated child keeps the expected raw parent until
  that future parent curation rewrites the Bryozoa branch.
- `Host-associated > Bryozoa > Reproductive system > Ovicells` remains a
  separate child record whose generated parentage points back to this Bryozoa
  Reproductive system record.
- The ignored/hidden-inclusive exact searches covered `curation`, `history`,
  `research`, `conf`, `data/raw`, `data/habitats`, the generated target page,
  and `reports/yaml_record_review`.
- iModulonDB structured source checks were not applicable: the record names a
  GOLD anatomical habitat path and no genes, locus tags, regulators, pathways,
  stress-response terms, or transcriptomic datasets.
