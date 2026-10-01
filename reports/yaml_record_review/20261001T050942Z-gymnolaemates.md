# YAML Record Review: Gymnolaemates

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/host_associated/gymnolaemates.yaml
- Started UTC: 2026-10-01T05:09:42Z
- Finished UTC: 2026-10-01T05:09:42Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/host_associated/gymnolaemates.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.587378d673` |
| Label | `Gymnolaemates` |
| Category | `HOST_ASSOCIATED` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |
| Stable slug | `data/habitats/PATHS.tsv:1937` maps `habitatmech:GOLD.587378d673` to `gymnolaemates` |

I reviewed the complete generated YAML. The target is the GOLD-only record for
`Host-associated > Invertebrates > Bryozoans > Gymnolaemates`, collapsed from
`gold.ecosystem:3642` and `gold.ecosystem:4087`.

The record is generated and reproducible. Its only maintained decision is
`curation/decisions.tsv:551`, a `CLASS`-depth `CONFIRM_UNGROUNDED` row from the
lexical sweep. That row did not assess whether the source concept is a habitat
and therefore does not promote the record to `REVIEWED`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/gymnolaemates.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/host_associated/gymnolaemates.yaml` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 generated terms. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records, 3,206 on disk, no missing, extra, or differing generated records. |
| `just worklist --status all --out /tmp/habitatmech-gymnolaemates-worklist.tsv` | Passed; wrote 953 ungrounded rows. The target appears at row 590 as `habitatmech:GOLD.587378d673` with path `Host-associated > Invertebrates > Bryozoans > Gymnolaemates`. |
| `just report --out /tmp/habitatmech-gymnolaemates-report.tsv` | Passed; the target appears at row 1937 as `UNGROUNDED`, `SEEDED`, GOLD-only, 1 source, 0 total assertions, 1 parent, no taxa, no parameters, and no causal graphs. |
| `git diff --check` | Passed. |

No target-specific causal-graph overlay exists, so there was no narrower
`just validate-causal curation/causal_graphs/<slug>.yaml` command to run.
Exact ignored/hidden-inclusive searches covered `curation/causal_graphs`,
`history`, `research`, `reports`, and generated `pages/habitats` for
`habitatmech:GOLD.587378d673`, `gold.ecosystem:3642`,
`gold.ecosystem:4087`, `Gymnolaemates`, `gymnolaemates`, and the exact source
path; they found the generated page and the earlier Bryozoans parent review,
but no target-specific overlay, append-only history record, research report, or
prior exact YAML review report.

## Identity and Grounding

| Claim | Evidence | Review |
|---|---|---|
| `habitatmech:GOLD.587378d673` is the minted GOLD identifier for this canonical path. | `src/habitatmech/seed.py` mints GOLD IDs from `row["canonical_path"]`; `data/habitats/PATHS.tsv:1937` pins this identifier to `gymnolaemates`; the generated YAML carries the same ID. | Supported exactly. |
| The source identity is the GOLD path `Host-associated > Invertebrates > Bryozoans > Gymnolaemates`. | `data/raw/gold_ecosystem_paths.tsv:1974` has that canonical path, `leaf_label=Gymnolaemates`, depth 4, `gold_node_count=2`, and node IDs `gold.ecosystem:3642|gold.ecosystem:4087`. | Supported exactly. |
| The record is host-associated. | The first GOLD path level is `Host-associated`, and `src/habitatmech/seed.py` uses the GOLD top-level/category tuple to authoritatively set host-associated categories. | Supported. |
| The record is ungrounded because no vendored ontology term fits the label. | `curation/decisions.tsv:551` records the class-level no-match sweep; an exact ignored/hidden-inclusive, case-insensitive search for `Gymnolaemates`, `gymnolaemate`, and `bryozoan` in `data/raw/ontology_terms.tsv`, `curation/term_requests.tsv`, and `curation/external_xrefs.tsv` found no exact vendored term, authored term request, or external xref. | Mechanically supported, but only at class depth. |
| The generated `habitatmech:GOLD.d2ef97a849` parent is the immediate GOLD parent. | `src/habitatmech/seed.py` links each GOLD concept to the resolved identifier of its parent path; the parent path `Host-associated > Invertebrates > Bryozoans` appears at `data/raw/gold_ecosystem_paths.tsv:842`, resolves to `habitatmech:GOLD.d2ef97a849`, and has slug `bryozoans`. | Mechanically supported. The parent record itself remains item-unreviewed and should be checked and defined as a bryozoan-associated environment in the same curation pass. |

The review did not add an external taxon xref. Exact ignored/hidden-inclusive
searches found no Gymnolaemates row in `data/raw/ontology_terms.tsv` or
maintained external xref for this target.

## Evidence

The generated GOLD source attestation is faithful to the rows that
`ingest_gold()` currently consumes:

- `source_id` is `gold.ecosystem:3642`, the first of two node IDs in
  `data/raw/gold_ecosystem_paths.tsv:1974`.
- `source_label` is the leaf label `Gymnolaemates`.
- `source_path` is `Host-associated > Invertebrates > Bryozoans > Gymnolaemates`.
- The collapsed-node note is supported by the two IDs in `gold_node_ids`.
- No `assertion_count` is emitted because `organism_count` is 0 and
  `src/habitatmech/seed.py` currently emits GOLD assertion counts only for
  organism counts.

The committed GOLD side tables add evidence that is not projected into the
generated record:

| Source row | Meaning |
|---|---|
| `data/raw/gold_path_biosamples.tsv:1011` | The same canonical path has one GOLD biosample at ecosystem path ID `4087`. |
| `data/raw/gold_studies.tsv:623` | GOLD study `Gs0111370` is associated only with `Host-associated > Invertebrates > Bryozoans > Gymnolaemates`. |

The record has no definition, synonyms, xrefs, environmental parameters,
characteristic taxa, record-level evidence, causal graphs, discussions, or
datasets. Those absences agree with exact ignored/hidden-inclusive searches
over maintained curation, history, research, raw, report, and page surfaces
for the target identifier, label, slug, source node IDs, and exact GOLD path.

iModulonDB was not applicable: the record names a GOLD habitat path and no
gene, locus tag, regulator, pathway, stress-response term, or transcriptomics
dataset.

## Completeness

The target is incomplete in two material ways:

- It has only a class-level no-match decision. A curator still needs to decide
  item-level habitat validity, keep the source concept under a minted identity,
  and define the intended gymnolaemate-associated environment.
- It has direct GOLD biosample and study side-table rows that remain outside
  the generated source attestation even though `AssertionUnitEnum` already has
  `STUDY` and `BIOSAMPLE` units.

The inherited Bryozoans parent was already reviewed in
`reports/yaml_record_review/20260922T155553Z-bryozoans.md`; that report found
that `habitatmech:GOLD.d2ef97a849` also needs item-level curation and likely
merge review against the top-level `Host-associated > Bryozoa` source concept.
Any Gymnolaemates curation should happen after, or in the same pass as, that
parent review so the generated child does not get a stable broader edge to a
duplicate bryozoan host record.

No environmental-triad rows exist for the exact Gymnolaemates path. An exact
ignored/hidden-inclusive search covered `data/raw/gold_path_triads.tsv` for
the full source path and both GOLD node IDs and found no matching row.

## Findings

| Severity | Finding | Owner |
|---|---|---|
| Major | `habitatmech:GOLD.587378d673` is still a `SEEDED`, class-reviewed host concept. The GOLD path denotes gymnolaemates acting as hosts, but the record still publishes the bare host-group label `Gymnolaemates` with no definition and with no item-level decision that reviewed whether the source concept is a real habitat. | Add an `ITEM`-depth decision in `curation/decisions.tsv`; add a definition for the minted associated-environment concept in `curation/term_requests.tsv`; regenerate with `just seed` and `just seed-canary habitatmech:GOLD.587378d673`. |
| Major | The generated record hides direct GOLD study and biosample support. `data/raw/gold_path_biosamples.tsv` has one biosample for ecosystem path ID `4087`, and `data/raw/gold_studies.tsv` has one study for the same exact canonical path, but the generated `source_attestations` table has no count because `src/habitatmech/seed.py` only emits GOLD `ORGANISM` counts from `data/raw/gold_ecosystem_paths.tsv`. | Define projection semantics for GOLD study and biosample side tables, then extend `src/habitatmech/seed.py` and its tests to read the committed side tables and emit supported counts without summing unlike units. |

## Recommended Edits

1. In `curation/decisions.tsv`, replace or override the class-depth row for
   `habitatmech:GOLD.587378d673` with an item-level review of
   `Host-associated > Invertebrates > Bryozoans > Gymnolaemates`.
2. In `curation/term_requests.tsv`, add a `gymnolaemate-associated environment`
   definition if the concept remains distinct after reviewing the Bryozoans and
   Bryozoa parent duplication. Use `ADD` unless item review proves every
   inherited parent is false.
3. Curate `habitatmech:GOLD.d2ef97a849` for
   `Host-associated > Invertebrates > Bryozoans` in the same pass, and keep the
   Gymnolaemates parent edge pointed at the surviving bryozoan-associated
   environment if the Bryozoans/Bryozoa records merge.
4. Extend the GOLD seeding path to consume `data/raw/gold_path_biosamples.tsv`
   and `data/raw/gold_studies.tsv`, or add a deliberate report-only decision
   explaining why those committed side tables should stay outside generated
   `source_attestations`.

## Follow-up Checks

After curation:

1. Run `just seed`.
2. Run `just seed-canary habitatmech:GOLD.587378d673`.
3. Inspect `data/habitats/host_associated/gymnolaemates.yaml` or the surviving
   regenerated child if a merge or rename retires this path.
4. Run `just validate data/habitats/host_associated/gymnolaemates.yaml`.
5. Run `just validate-strict data/habitats/host_associated/gymnolaemates.yaml`.
6. Run `just validate-causal-all`.
7. Run `just validate-history`.
8. Run `just term-requests-check`.
9. Run `just verify-corpus --max-diffs 1`.
10. Run `just render` and inspect
    `pages/habitats/gymnolaemates-habitatmech-gold-587378d673.html` or the
    surviving regenerated page.
11. Run `git diff --check`.

If the GOLD side tables are projected into `source_attestations`, add a focused
test that a path with zero organisms but nonzero biosamples or studies no
longer renders as assertion-free.

## Additional Notes

- Exact ignored/hidden-inclusive searches were used before treating maintained
  artifacts as absent. Broad exact searches covered `curation`, `history`,
  `research`, `reports`, `conf`, `src`, `data/raw`, `data/habitats/PATHS.tsv`,
  `data/habitats/host_associated`, `curation/causal_graphs`, and
  `pages/habitats`; generated `data/text_map` was excluded to avoid one-line
  JSON output that is not a maintained source.
- `find` with ignored files included found the rendered page
  `pages/habitats/gymnolaemates-habitatmech-gold-587378d673.html` and no
  `*gymnolaemates*` overlay, history, research, or prior exact review file.
- The rendered page mirrors the generated YAML: it labels the record
  `Gymnolaemates`, shows `UNGROUNDED` and `SEEDED`, links to the seeded
  `Bryozoans` parent, displays no assertion count for GOLD, and shows the
  class-level `CONFIRM_UNGROUNDED` event.
