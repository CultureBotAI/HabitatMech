# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/coastal_water_body.yaml`
- Started UTC: 2026-09-27T04:08:00Z
- Finished UTC: 2026-09-27T04:20:03Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `ENVO:02000049` |
| Label | `coastal water body` |
| Class | `HabitatRecord` |
| Category | `AQUATIC` |
| Generated or maintained | Generated from `data/raw/`, `curation/decisions.tsv`, and `data/habitats/PATHS.tsv`; do not hand-edit |
| Current grounding | `EXACT` |
| Current mapping | `SEEDED` |

The target resolves exactly one generated YAML file and one pinned slug:
`data/habitats/aquatic/coastal_water_body.yaml`. `data/habitats/PATHS.tsv`
maps `ENVO:02000049` to `coastal_water_body`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/coastal_water_body.yaml` | Pass: LinkML reported `No issues found`. |
| `just validate-all data/habitats/aquatic/coastal_water_body.yaml` | Pass: 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-strict data/habitats/aquatic/coastal_water_body.yaml --quiet` | Pass: 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal-all` | Pass: 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Pass: committed term-request table is current with 109 terms. |
| `just validate-history` | Pass: 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist.tsv` | Pass: regenerated a 953-row ungrounded worklist outside the repository. |
| `just verify-corpus --max-diffs 1` | Pass: 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just report` | Pass: completed the corpus diagnostic report without surfacing a global issue for this target. |

No documented validator was skipped.

## Identity and Grounding

The record identity is correct. `data/raw/ontology_terms.tsv` contains
`ENVO:02000049` with label `coastal water body`, the definition copied into the
record, a present-in-ontology flag of `TRUE`, and an obsolete flag of `FALSE`.
`data/raw/ontology_subclass_edges.tsv` makes `ENVO:02000049` a direct subclass
of `ENVO:00001999` `marine water body`, which is the record's only generated
`parent_habitats` entry.

The only upstream source concept is PREGO term `ENVO:02000049`. That source
concept gets the minted curation key `habitatmech:PREGO.761608a2ee`; there is
no item-level decision for it yet, so the generated `mapping_status: SEEDED`
is expected. `src/habitatmech/seed.py` self-grounds PREGO CURIEs before
consulting decisions, stores the PREGO CURIE as the source attestation
`source_id`, and infers this record's `AQUATIC` category from ontology ancestry
rather than from a GOLD path.

## Evidence

The PREGO source attestation is copied from `data/raw/prego_habitats.tsv`: 432
distinct associated taxa, a maximum PREGO score of 3.0, and evidence channels
`annotated_genomes_isolates|environmental_samples`. Its `source_label` comes
from the vendored ENVO label for `ENVO:02000049`.

All three synonyms are source-provided PREGO lexical variants in
`data/raw/prego_habitats.tsv` and are intentionally emitted as
`RELATED_SYNONYM` values, not exact ontology synonyms. The odd-looking
`Coastal Waterses` string is present in the raw PREGO synonym column; the
generated YAML preserves it as weak PREGO provenance rather than treating it as
an ENVO synonym.

The 25 generated taxon rows are the top 25 rows for `ENVO:02000049` in
`data/raw/prego_habitat_taxa.tsv`. Their rank, taxon CURIE, optional taxon
label, PREGO score, and 432-taxon candidate pool agree with the raw source
rows. None of the taxa assert `is_characteristic`, so the record does not
upgrade PREGO's reported-from associations into curator-backed characteristic
taxa.

The lone `SEEDED_FROM_SOURCES` curation-history event accurately records that
the YAML was generated from source inventories and exactly grounded by the
seeder.

## Completeness

The record has no curator-authored `evidence`, `environmental_parameters`,
`causal_graphs`, `discussions`, or `datasets`. Those slots are correctly empty
for the current maintained inputs: this is a PREGO-only, ontology-grounded
record with no row in `curation/decisions.tsv`, no term request, and no
curated causal overlay.

Exact hidden- and ignored-file-inclusive searches of `curation`, `history`,
`research`, `reports`, `conf`, and `data/habitats/PATHS.tsv` found no
maintained decision, target-owned research report, causal overlay, history
entry, term request, term-request exclusion, external xref, id-label target, or
prior YAML review for `data/habitats/aquatic/coastal_water_body.yaml`,
`coastal_water_body`, `ENVO:02000049`, or
`habitatmech:PREGO.761608a2ee`.

Two prior reports mention `ENVO:02000049` only as contextual GOLD MIxS local
evidence for other records. The Coastal lagoon review notes that coastal
lagoons are coastal water bodies but not identical to the target, and the
Brine review notes that the GOLD `Coastal > Brine` path used `ENVO:02000049`
as its local-scale context while using brine as the medium. Neither prior
report changes the PREGO-only provenance of this target record.

## Findings

No blocker findings.

No major findings.

No minor findings.

## Recommended Edits

No required curation edits.

If a curator wants this correct PREGO self-grounding to become `REVIEWED`, add
an item-level `REVIEW` row for `habitatmech:PREGO.761608a2ee` to
`curation/decisions.tsv`, then regenerate `ENVO:02000049`. That would be a
status-promotion edit, not a correction to the current YAML.

## Follow-up Checks

No corrective follow-up is required for the reviewed YAML.

For the optional review-promotion edit above, run:

- `just seed`
- `just seed-canary ENVO:02000049 --force`
- `just validate data/habitats/aquatic/coastal_water_body.yaml`
- `just validate-strict data/habitats/aquatic/coastal_water_body.yaml --quiet`
- `just verify-corpus --max-diffs 1`
- `just report`

After regeneration, re-read `data/habitats/aquatic/coastal_water_body.yaml` and
confirm that it remains `identifier: ENVO:02000049`, keeps
`parent_habitats: [ENVO:00001999]`, keeps the 432-taxon PREGO source
attestation, and changes only from `mapping_status: SEEDED` to `REVIEWED`.

## Additional Notes

This was a read-only YAML review. It did not edit generated habitat YAML,
append curation history, promote review status, create an issue, or run paid
definition research.

The generated HTML page was not used as evidence; all assertions above were
traced to maintained TSV inputs, source inventory rows, the vendored ontology
slice, `src/habitatmech/seed.py`, or the generated target YAML.
