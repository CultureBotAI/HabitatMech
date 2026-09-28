# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/multiple_organs__a0ce3dd7.yaml`
- Started UTC: 2026-09-28T13:04:00Z
- Finished UTC: 2026-09-28T13:18:40Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| File | `data/habitats/host_associated/multiple_organs__a0ce3dd7.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.4dbae6ecfe` |
| Label | `Multiple organs` |
| Category | `HOST_ASSOCIATED` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |
| Maintained/generated | Generated from `data/raw/` plus curation inputs |

The record is generated from the GOLD source path `Host-associated > Mammals >
Multiple systems > Multiple organs`, collapsed across `gold.ecosystem:6422`
and `gold.ecosystem:6879`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/multiple_organs__a0ce3dd7.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/multiple_organs__a0ce3dd7.yaml` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated. |
| `just verify-corpus` | Passed; expected and found 3206 records, with 0 missing, 0 extra, and 0 differing records. |
| `just worklist --status all --out /tmp/habitatmech-multiple-organs-worklist.tsv` | Passed; wrote 953 ungrounded rows. Row 336 reports this target with 1 assertion, a `decided` class-level row, and the rejected lexical candidate `UBERON:0001630` `muscle organ`. |
| `just report --out /tmp/habitatmech-multiple-organs-report.tsv` | Passed; row 1863 reports this target as a `HOST_ASSOCIATED` `UNGROUNDED`/`SEEDED` GOLD-only record with one source, one upstream assertion, one parent, no definition, no environmental parameters, no characteristic taxa, and no causal graph. |

## Identity and Grounding

The generated identity is internally consistent but only class-reviewed. The
committed GOLD aggregate has the source row:

| Path | GOLD IDs | Assertions |
|---|---|---:|
| `Host-associated > Mammals > Multiple systems > Multiple organs` | `gold.ecosystem:6422|gold.ecosystem:6879` | 1 organism / 0 studies / 0 biosamples |

The minted identifier denotes the mammalian `Multiple organs` source path, not
the fish sibling that has the same leaf label:

| Record | Source path | Assertions |
|---|---|---:|
| `multiple_organs__a0ce3dd7.yaml` / `habitatmech:GOLD.4dbae6ecfe` | `Host-associated > Mammals > Multiple systems > Multiple organs` | 1 |
| `multiple_organs.yaml` / `habitatmech:GOLD.11ea780433` | `Host-associated > Fish > Multiple systems > Multiple organs` | 0 |

The target's only parent, `habitatmech:GOLD.68a62625da`, is the immediate GOLD
parent path `Host-associated > Mammals > Multiple systems`. That is supported
as a generated source-path parent.

`curation/decisions.tsv` currently has a `CONFIRM_UNGROUNDED` row for
`habitatmech:GOLD.4dbae6ecfe`, but the row is explicitly `review_depth: CLASS`:
the August class-level sweep found no vendored ontology term by lexical search
and did not assess whether the concept itself was a habitat. The only new
worklist candidate, `UBERON:0001630` `muscle organ`, is a false lexical lead for
the plural GOLD aggregate and should not be used as this record's identity or
parent.

## Evidence

| Claim | Evidence checked | Assessment |
|---|---|---|
| This record represents the mammalian GOLD `Multiple organs` path. | `data/raw/gold_ecosystem_paths.tsv` lists exactly `Host-associated > Mammals > Multiple systems > Multiple organs` with GOLD nodes `gold.ecosystem:6422|gold.ecosystem:6879`; the generated source attestation copies the path, the label, and the first node id. | Supported. |
| The source path carries one organism assertion. | The same GOLD aggregate row reports `organism_count` 1, `study_count` 0, `biosample_count` 0, and `total_assertions` 1. The direct path is absent from `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, and `data/raw/gold_studies.tsv`; those files only expose downstream `Pooled tissues` rows under this mammalian branch. | Supported. |
| `parent_habitats: habitatmech:GOLD.68a62625da` reproduces GOLD hierarchy. | `data/raw/gold_ecosystem_paths.tsv` lists `Host-associated > Mammals > Multiple systems` as the immediate prefix of the target path, and `data/habitats/PATHS.tsv` maps that minted id to `multiple_systems`. | Supported. |
| This source concept has been curated at item depth. | `curation/decisions.tsv` has only the class-level sweep row for `habitatmech:GOLD.4dbae6ecfe`; no hidden/ignored-inclusive exact search over maintained curation inputs, history, research outputs, YAML-review reports, curated records, raw inventories, or config found a target-specific term request, causal overlay, deep-research report, or append-only history record. | Unsupported. |

iModulonDB was not applicable: this record names a host anatomical aggregate,
not a covered organism, gene, regulator, locus, iModulon, or transcriptomics
dataset.

## Completeness

The generated record is intentionally sparse: it has no definition, synonyms,
xrefs, environmental parameters, characteristic taxa, record-level evidence,
causal graphs, discussions, or datasets. That sparseness follows from the
maintained inputs checked here, rather than from a missing generated field.

Exact hidden/ignored-inclusive searches over `curation/term_requests.tsv`,
`curation/term_requests_excluded.tsv`, `curation/external_xrefs.tsv`,
`curation/causal_graphs/`, `history/`, `research/`,
`reports/habitat_research_manifest.tsv`, `reports/yaml_record_review/`,
`conf/`, `data/habitats/`, and `data/raw/` found no maintained row or overlay
for `habitatmech:GOLD.4dbae6ecfe`, `gold.ecosystem:6422`,
`gold.ecosystem:6879`, or the record slug beyond the current class-level
decision, generated target, generated descendants, raw GOLD aggregate, and
source-path index rows. `find reports/yaml_record_review -maxdepth 1 -type f
-name '*multiple_organs__a0ce3dd7*' -print` also found no prior exact YAML
review before this report was written; `find` included ignored files under
`reports/yaml_record_review`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | None found | The YAML validates, the generated file reproduces exactly from source inputs, and its GOLD identity, assertion count, source attestation, and source-path parent agree with the committed raw inventories. | Not applicable |
| Major | The mammalian `Multiple organs` GOLD node lacks an item-level curation decision. | The record is still `mapping_status: SEEDED`; its curation history says the `CONFIRM_UNGROUNDED` decision came from a `[CLASS-level]` sweep where "Whether the concept is a habitat at all was NOT assessed"; and hidden/ignored-inclusive exact searches found no term request, target-specific research report, causal overlay, or history record for `habitatmech:GOLD.4dbae6ecfe`, the two GOLD node ids, or the target slug. | `curation/decisions.tsv` |
| Minor | None found | No non-blocking style, provenance, or schema issue was found. | Not applicable |

## Recommended Edits

1. Replace the class-level row for `habitatmech:GOLD.4dbae6ecfe` in
   `curation/decisions.tsv` with an item-level decision after checking whether
   GOLD's mammalian multi-organ bin denotes a real host habitat or only a
   sample-aggregation bucket. Do not adopt `UBERON:0001630`; `muscle organ` is
   a specific organ type, not the `Multiple organs` aggregate in the GOLD path.
2. If item-level review confirms this is a real multi-organ host habitat with
   no fitting ontology term, add a maintained definition and ENVO request in
   `curation/term_requests.tsv`. If item-level review instead finds the source
   concept is not a habitat, record `NOT_APPLICABLE` in `curation/decisions.tsv`
   and leave no term-request row.

## Follow-up Checks

After the future item-level curation input is added:

1. Run `just seed`.
2. Run `just seed-canary habitatmech:GOLD.4dbae6ecfe`.
3. Confirm `data/habitats/host_associated/multiple_organs__a0ce3dd7.yaml`
   changes from the class-sweep `SEEDED` state to the item-level result while
   preserving the `gold.ecosystem:6422` source attestation.
4. Run `just validate-strict data/habitats/host_associated/multiple_organs__a0ce3dd7.yaml`.
5. Run `just term-requests-check` if a term request is added.
6. Run `just verify-corpus`.
7. Run `just validate-history` if the curation session adds the required
   append-only history record.
8. Run `just render` if the generated record changes.

## Additional Notes

`Pooled tissues` and `Viscera` currently reproduce GOLD's hierarchy by listing
`habitatmech:GOLD.4dbae6ecfe` as their immediate source-path parent. This
review only checks that the parent record itself reproduces the mammalian
`Multiple organs` path; any narrower claim about whether the `Pooled tissues`
sample category is truly a kind of multi-organ host habitat belongs to that
child record's item-level curation.
