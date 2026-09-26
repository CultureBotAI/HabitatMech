# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/other/paddy_ricefield.yaml
- Started UTC: 2026-09-26T11:16:05Z
- Finished UTC: 2026-09-26T11:16:28Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:BACDIVE.6e3154acd8` |
| Label | `Paddy-Ricefield` |
| Class | `HabitatRecord` |
| Category | `OTHER` |
| Generated path | `data/habitats/other/paddy_ricefield.yaml` |
| Maintained path lock | `data/habitats/PATHS.tsv:1210` maps `habitatmech:BACDIVE.6e3154acd8` to `paddy_ricefield` |
| Source concept | BACDIVE `bacdive.isolation_source:paddy-ricefield` |
| Source label | `Paddy-Ricefield` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |

The reviewed file is generated from the BacDive source inventory, the local
copy of KG-Microbe's BacDive isolation-source grounding table, and one
class-level curation decision. It should not be patched directly.

## Validation

| Command | Result |
|---|---|
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist.tsv` | Passed; wrote 953 rows. The target appeared as row 232 with four BacDive assertions and candidate ontology terms `ENVO:00000297=paddy field` and `ENVO:00000296=rice field`. |
| `just validate data/habitats/other/paddy_ricefield.yaml` | Passed with `No issues found`. |
| `just validate-strict data/habitats/other/paddy_ricefield.yaml` | Passed; one file scanned, zero files with `ERROR`, zero total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 expected records, 3206 found, 0 missing, 0 extra, 0 differing. |
| `just report` | Passed. |
| `git diff --check` | Passed before this report was written. |

## Identity and Grounding

The target's generated identifier, BacDive source identity, BacDive strain
count, and top-level category agree with the raw BacDive source inventory:

| Claim | Evidence | Assessment |
|---|---|---|
| The target is the BacDive `Paddy-Ricefield` isolation source. | `data/raw/bacdive_isolation_sources.tsv:141` records `bacdive.isolation_source:paddy-ricefield`, label `Paddy-Ricefield`, slug `paddy-ricefield`, four strains, and four taxa. | Supported exactly. |
| The KG-Microbe BacDive grounding row exists but does not carry an ontology target. | `data/raw/isolation_source_groundings.tsv:227` records `Paddy-Ricefield` with normalized label `paddy ricefield`, blank `object_id`, blank `object_label`, and source dataset `bacdive`. | Supported exactly. `src/habitatmech/seed.py` treats this shape as `bacdive_declined_upstream`. |
| The `source_attestations` block preserves the raw source ID, source label, assertion count, and unit. | The generated YAML has `source: BACDIVE`, `source_id: bacdive.isolation_source:paddy-ricefield`, `source_label: Paddy-Ricefield`, `assertion_count: 4`, and `assertion_unit: STRAIN`. | Supported exactly. |
| The four characteristic taxa preserve the BacDive isolation-source taxa ranking. | `data/raw/bacdive_source_taxa.tsv:2095-2098` lists `Novosphingobium arvoryzae`, `Ferrigenium kumadai`, `Alsobacter soli`, and `Rhizobium sp.`, each with one strain at ranks 1 through 4. | Supported exactly. |
| The record is still owned by a class-level sweep decision. | `curation/decisions.tsv:47` has `CONFIRM_UNGROUNDED` for `habitatmech:BACDIVE.6e3154acd8` with `review_depth` `CLASS`. Its note says habitat status was not assessed. | Reproducible but incomplete. A class-level sweep is not enough to settle an apparent paddy/rice-field habitat. |

The current vendored ontology slice contains two close identity candidates:

| CURIE | Label | Definition | Relationship to the BacDive source |
|---|---|---|---|
| `ENVO:00000297` | `paddy field` | `A flooded parcel of arable land used for growing rice and other semiaquatic crops.` | Likely the broadest exact match to the BacDive label's `Paddy` half. |
| `ENVO:00000296` | `rice field` | `A paddy field for the cultivation of rice.` | Likely an exact match if the BacDive label's `Ricefield` half is read as rice-specific rather than a synonym cue. |

An item review still needs to choose the correct ENVO target. Leaving the
record as `UNGROUNDED` is the unsupported part: the source label names the
same paddy/rice-field habitat family that ENVO already represents and the
worklist ranks both ENVO terms as candidates.

## Evidence

| Record claim | Nearest source | Assessment |
|---|---|---|
| `source: BACDIVE`, `source_id: bacdive.isolation_source:paddy-ricefield`, and `source_label: Paddy-Ricefield` | `data/raw/bacdive_isolation_sources.tsv:141` | Supported exactly. |
| `assertion_count: 4` and `assertion_unit: STRAIN` | `data/raw/bacdive_isolation_sources.tsv:141` | Supported exactly. This is a BacDive strain count and is not comparable with PREGO taxon counts. |
| Note saying KG-Microbe has a blank isolation-source grounding for this source | `data/raw/isolation_source_groundings.tsv:227`; `src/habitatmech/seed.py` emits the note for `bacdive_declined_upstream` rows. | Supported exactly as generated behavior. The upstream blank should be re-reviewed, not hidden by a direct YAML patch. |
| `NCBITaxon:1256514` through `NCBITaxon:391` characteristic taxa | `data/raw/bacdive_source_taxa.tsv:2095-2098` | Supported exactly. No rank, label, count, or candidate-pool mismatch was found. |
| Absence of a curated definition, source-derived parents, environmental parameters, evidence objects, and causal graphs | Exact hidden/ignored-inclusive searches for `habitatmech:BACDIVE.6e3154acd8`, `bacdive.isolation_source:paddy-ricefield`, `Paddy-Ricefield`, and `paddy_ricefield` across `curation/`, `history/`, `research/habitats/`, and generated record/page paths found no target-specific maintained overlay or history. | Supported. The current record is a generated BacDive leaf with no committed item-level curation. |

## Completeness

The generated record completely preserves the current BacDive source aggregate,
blank KG-Microbe grounding, class-level decision, and BacDive characteristic
taxa rows. It also correctly avoids unsupported curated definitions, causal
edges, environmental parameters, and record-level evidence.

The record is incomplete as a grounding decision. An exact hidden/ignored-
inclusive search of `data/raw/`, `curation/`, `history/`,
`reports/yaml_record_review/`, `data/habitats/`, and `pages/habitats/` for the
record identifier, BacDive source ID, filename stem, source label, normalized
label, and title-case label found the expected raw rows, generated record,
generated page, path lock, and class-level decision. It found no prior exact
YAML review, no item-level decision, no term request, no history event, and no
causal overlay for this target. An exact search of `research/habitats/` for
`Paddy-Ricefield` found only contextual mentions in the Aquatic-Plant and
Environmental reports, not a target-specific paddy/rice-field review.

`data/habitats/other/paddy_field.yaml` and
`data/habitats/other/rice_field.yaml` already represent the two ENVO
candidates as PREGO-attested records. If item review confirms either as an
exact match, the BacDive attestation should merge into one of those records
instead of continuing as a separate minted HabitatMech leaf.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-PADDY-RICEFIELD-001 | Major | `Paddy-Ricefield` still publishes as `UNGROUNDED` from a blank BacDive grounding row plus a `CLASS`-depth `CONFIRM_UNGROUNDED` decision, even though the source label is a concrete paddy/rice-field habitat and the current ontology slice has direct `paddy field` and `rice field` candidates. The class-level decision explicitly did not assess whether the source is a habitat, and the KG-Microbe blank target leaves this BacDive source split away from the existing ENVO `paddy field` and `rice field` records. | `data/raw/isolation_source_groundings.tsv`; `curation/decisions.tsv` |

## Recommended Edits

1. Item-review `bacdive.isolation_source:paddy-ricefield` against
   `ENVO:00000297` `paddy field` and `ENVO:00000296` `rice field`.
2. If either ENVO term is exact, update the KG-Microbe BacDive grounding row
   consumed as `data/raw/isolation_source_groundings.tsv` with the chosen
   `object_id`, `object_label`, `predicate_id`, confidence, and mapping
   justification.
3. Remove or replace the class-level `CONFIRM_UNGROUNDED` row for
   `habitatmech:BACDIVE.6e3154acd8` in `curation/decisions.tsv`; otherwise it
   will continue overriding any fixed BacDive default grounding.
4. Regenerate the corpus from maintained inputs and confirm the BacDive
   attestation appears on the chosen ENVO record rather than on
   `data/habitats/other/paddy_ricefield.yaml`.

Do not hand-edit `data/habitats/other/paddy_ricefield.yaml` or generated HTML
pages.

## Follow-up Checks

After the BacDive grounding is item-reviewed and updated, rerun:

- `just seed`
- `just validate-strict data/habitats/other/paddy_field.yaml` or
  `just validate-strict data/habitats/other/rice_field.yaml`, depending on the
  chosen target
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`

If the minted `paddy_ricefield` record disappears after the exact merge, also
check `data/habitats/PATHS.tsv`, generated pages, and any removed stale file in
the corpus diff before committing the curation change.

## Additional Notes

None.
