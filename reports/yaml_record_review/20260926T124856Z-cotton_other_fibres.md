# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/other/cotton_other_fibres.yaml
- Started UTC: 2026-09-26T12:48:56Z
- Finished UTC: 2026-09-26T12:48:57Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:BACDIVE.009b89b30a` |
| Label | `Cotton-other-fibres` |
| Class | `HabitatRecord` |
| Category | `OTHER` |
| Generated path | `data/habitats/other/cotton_other_fibres.yaml` |
| Maintained path lock | `data/habitats/PATHS.tsv:1157` maps `habitatmech:BACDIVE.009b89b30a` to `cotton_other_fibres` |
| Source concept | BacDive `bacdive.isolation_source:cotton-other-fibres` |
| Source label | `Cotton-other-fibres` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |

The reviewed file is generated from the BacDive source inventory, the local
copy of KG-Microbe's BacDive isolation-source grounding table, and one
class-level curation decision. It should not be patched directly.

## Validation

| Command | Result |
|---|---|
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist.tsv` | Passed; wrote 953 rows. The target appeared as row 235 with three BacDive strain assertions and candidate ontology term `BTO:0000299=cotton fibre`. |
| `just validate data/habitats/other/cotton_other_fibres.yaml` | Passed with `No issues found`. |
| `just validate-strict data/habitats/other/cotton_other_fibres.yaml` | Passed; one file scanned, zero files with `ERROR`, zero total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 expected records, 3206 found, 0 missing, 0 extra, 0 differing. |
| `just report` | Passed. |
| `git diff --check` | Passed before this report was written. |

## Identity and Grounding

The generated identifier, BacDive source identity, BacDive strain count, and
taxon list agree with the raw BacDive inventory:

| Claim | Evidence | Assessment |
|---|---|---|
| The target is the BacDive `Cotton-other-fibres` isolation source. | `data/raw/bacdive_isolation_sources.tsv:144` records `bacdive.isolation_source:cotton-other-fibres`, label `Cotton-other-fibres`, slug `cotton-other-fibres`, three strains, and three taxa. | Supported exactly. |
| The KG-Microbe BacDive grounding row exists but does not carry an ontology target. | `data/raw/isolation_source_groundings.tsv:80` records `Cotton-other-fibres` with normalized label `cotton other fibres`, blank `object_id`, blank `object_label`, and source dataset `bacdive`. | Supported exactly. `src/habitatmech/seed.py` treats this shape as `bacdive_declined_upstream`. |
| The `source_attestations` block preserves the raw source ID, source label, assertion count, and unit. | The generated YAML has `source: BACDIVE`, `source_id: bacdive.isolation_source:cotton-other-fibres`, `source_label: Cotton-other-fibres`, `assertion_count: 3`, and `assertion_unit: STRAIN`. | Supported exactly. |
| The three characteristic taxa preserve the BacDive isolation-source taxa ranking. | `data/raw/bacdive_source_taxa.tsv:697-699` lists `Clostridium sporogenes`, `Acetivibrio thermocellus`, and `Pseudomonas oryzihabitans`, each with one strain at ranks 1 through 3. | Supported exactly. |
| The source concept is still owned by a class-level sweep decision. | `curation/decisions.tsv:2` has `CONFIRM_UNGROUNDED` for `habitatmech:BACDIVE.009b89b30a` with `review_depth` `CLASS`. Its note says habitat status was not assessed. | Reproducible but incomplete. |

`curation/samples/class_swept_unscreened-20260814.tsv:2` sampled this row and
classified it as habitat-like rather than a disease, procedure, quality, or
other non-habitat. That sample is useful coarse evidence, but it is not an
item-level grounding review.

The current vendored ontology slice contains adjacent candidate terms:

| CURIE | Label | Definition | Relationship to the BacDive source |
|---|---|---|---|
| `BTO:0000299` | `cotton fibre` | `Each seed of a cotton plant is surrounded with downy fiber, white or creamy in color and easily spun. The fibers flatten and twist naturally as they dry.` | The worklist's only lexical candidate. It may cover the `Cotton` half of the BacDive label, but the unqualified `other-fibres` half still needs item review. |
| `ENVO:02000108` | `cotton dust` | | Cotton-derived but a dust, not a fibre. This is adjacent rather than an exact match. |
| `ENVO:00000288` | `cotton plantation` | | Cotton-related but an agricultural site, not sampled fibre material. This is adjacent rather than an exact match. |

The record should stay generated until a curator reads the source and decides
whether BacDive's bin is exactly `cotton fibre`, a broader fibre-material bin
that only needs `BTO:0000299` as a related or broader term, or a novel
cotton-and-other-fibre habitat requiring a term request.

## Evidence

| Record claim | Nearest source | Assessment |
|---|---|---|
| `source: BACDIVE`, `source_id: bacdive.isolation_source:cotton-other-fibres`, and `source_label: Cotton-other-fibres` | `data/raw/bacdive_isolation_sources.tsv:144` | Supported exactly. |
| `assertion_count: 3` and `assertion_unit: STRAIN` | `data/raw/bacdive_isolation_sources.tsv:144` | Supported exactly. This is a BacDive strain count and is not comparable with GOLD organism counts or PREGO taxon counts. |
| Note saying KG-Microbe has a blank isolation-source grounding for this source | `data/raw/isolation_source_groundings.tsv:80`; `src/habitatmech/seed.py` emits the note for `bacdive_declined_upstream` rows. | Supported exactly as generated behavior. The upstream blank should be item-reviewed rather than bypassed with a generated-YAML edit. |
| `NCBITaxon:1509`, `NCBITaxon:1515`, and `NCBITaxon:47885` characteristic taxa | `data/raw/bacdive_source_taxa.tsv:697-699` | Supported exactly. No rank, label, count, or candidate-pool mismatch was found. |
| Absence of a curated definition, environmental parameters, evidence objects, causal graph, item-level history event, target-specific research report, and prior exact YAML review | Exact hidden/ignored-inclusive searches for `habitatmech:BACDIVE.009b89b30a`, `bacdive.isolation_source:cotton-other-fibres`, `Cotton-other-fibres`, `cotton-other-fibres`, and `cotton_other_fibres` across `data/raw/`, `curation/`, `history/`, `research/habitats/`, `reports/yaml_record_review/`, `data/habitats/`, and `pages/habitats/` found only the expected raw rows, path lock, class-level decision, sample-screen row, generated record, and generated page. A hidden/ignored-inclusive `find` for `*cotton*` under `data/habitats/` and `research/habitats/` found only the generated target, so there is no target-specific research report. | Supported. The current record is a generated BacDive leaf with no committed item-level curation. |

## Completeness

The generated record completely preserves the current BacDive source aggregate,
blank KG-Microbe grounding, class-level decision, and BacDive characteristic
taxa rows. It also correctly avoids unsupported curated definitions, causal
edges, environmental parameters, and record-level evidence.

The record is incomplete as a grounding and definition decision. The class-level
sweep says no term in the vendored slice matched BacDive's label by its
mechanical routes at the time, and the later sampling row says the source looks
habitat-like rather than obviously out of scope. Neither file makes the
item-level judgment required to keep this as a reviewed minted habitat, merge
it with `BTO:0000299`, or request a cotton-and-other-fibre term with strictly
broader parents.

The lexical `cotton fibre` candidate makes that missing item review material:
`BTO:0000299` may be an exact match if the BacDive label denotes cotton fibre,
but it would be too narrow if the source means cotton plus other fibre
materials. The adjacent ENVO cotton terms make the same point from the opposite
direction: the local ontology slice has cotton-related entities, but not an
obvious exact material habitat for the whole BacDive label.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-COTTON-OTHER-FIBRES-001 | Major | `Cotton-other-fibres` still publishes as `UNGROUNDED` from a blank BacDive grounding row and a `CLASS`-depth `CONFIRM_UNGROUNDED` decision. Its BacDive strain/taxon content is reproducible and a later sample-screen row says the label is habitat-like, but no item-level decision records whether `BTO:0000299` `cotton fibre` is exact, broader, too narrow for the `other-fibres` bin, or only a related term for a novel fibre-material habitat. | `data/raw/isolation_source_groundings.tsv`; `curation/decisions.tsv`; if no exact ontology term exists after item review, `curation/term_requests.tsv` |

## Recommended Edits

1. Item-review `bacdive.isolation_source:cotton-other-fibres` against the
   BacDive strain sources and candidate terms `BTO:0000299` `cotton fibre`,
   `BTO:0000450` `fiber`, `ENVO:02000108` `cotton dust`, and `ENVO:00000288`
   `cotton plantation`.
2. If `BTO:0000299` is exact, update the KG-Microbe BacDive grounding row
   consumed as `data/raw/isolation_source_groundings.tsv` with the chosen
   `object_id`, `object_label`, `predicate_id`, confidence, and mapping
   justification, then remove or replace the class-level decision.
3. If no exact term exists, replace the class-level row in
   `curation/decisions.tsv` with an item-level `CONFIRM_UNGROUNDED` decision
   and add a `curation/term_requests.tsv` row with a definition and strictly
   broader parents for the BacDive source.
4. Regenerate from the maintained inputs and confirm the BacDive attestation,
   grounding status, mapping status, definition, parentage, and generated
   history reflect the item-level decision.

Do not hand-edit `data/habitats/other/cotton_other_fibres.yaml` or generated
HTML pages.

## Follow-up Checks

After item-level curation, rerun:

- `just seed`
- `just seed-canary habitatmech:BACDIVE.009b89b30a`
- inspect `data/habitats/other/cotton_other_fibres.yaml` or the ontology-backed
  target that absorbs `bacdive.isolation_source:cotton-other-fibres`
- `just validate-strict` on the regenerated target
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`

If the item review merges this BacDive source into an ontology-backed record,
also check `data/habitats/PATHS.tsv`, generated pages, and any retired stale
file before committing the curation change.

## Additional Notes

None.
