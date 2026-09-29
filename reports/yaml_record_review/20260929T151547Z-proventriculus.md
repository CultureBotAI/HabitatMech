# YAML Record Review: proventriculus

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/proventriculus.yaml`
- Started UTC: 2026-09-29T15:15:47Z
- Finished UTC: 2026-09-29T15:16:43Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| File | `data/habitats/host_associated/proventriculus.yaml` |
| Class | `HabitatRecord` |
| Identifier | `UBERON:0007357` |
| Label | `proventriculus` |
| Definition source | `UBERON` |
| Category | `HOST_ASSOCIATED` |
| Grounding | `EXACT` |
| Mapping | `SEEDED` |
| Maintained/generated | Generated from `data/raw/` plus `curation/decisions.tsv` |

The record currently merges two zero-assertion GOLD leaf paths:

| Source concept | Path | GOLD node |
|---|---|---|
| `habitatmech:GOLD.e83536dc3f` | `Host-associated > Arthropoda: Insects > Digestive system > Foregut > Proventriculus/Gizzard` | `gold.ecosystem:7198` |
| `habitatmech:GOLD.8f147900b1` | `Host-associated > Birds > Digestive system > Stomach > Proventriculus` | `gold.ecosystem:7431` |

`habitatmech:GOLD.e83536dc3f` is item-reviewed in
`curation/decisions.tsv`. `habitatmech:GOLD.8f147900b1` is still seeded.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/proventriculus.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/proventriculus.yaml` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| Standalone reference validator | Not checked: exact hidden/ignored-inclusive searches of `justfile`, `.claude/`, `docs/`, `src/`, and `scripts/` found no standalone habitat-reference validator documented by this repository; this record has no record-level evidence, datasets, or causal graph edges. |
| `just verify-corpus` | Passed; expected 3206 records, found 3206 on disk, with 0 missing, 0 extra, and 0 differing records. |
| `just report --ungrounded-top 0 --out /tmp/habitatmech-report-proventriculus.tsv` | Passed; wrote `/tmp/habitatmech-report-proventriculus.tsv`. Row 1105 reports this target as a GOLD-only `HOST_ASSOCIATED` `EXACT`/`SEEDED` record with zero upstream assertions, a definition, three parents, no environmental parameters, no characteristic taxa, and no causal graph. |
| `just worklist --limit 40 --status all --out /tmp/habitatmech-worklist-proventriculus.tsv` | Passed; wrote `/tmp/habitatmech-worklist-proventriculus.tsv` with 953 ungrounded rows. This target is `EXACT`, so it is intentionally absent from the ungrounded worklist. |
| `git diff --check` | Passed. |

## Identity and Grounding

The Bird GOLD path supports exact `UBERON:0007357` grounding:

| Check | Evidence | Result |
|---|---|---|
| Bird source path | `data/raw/gold_ecosystem_paths.tsv:1879` lists exactly `Host-associated > Birds > Digestive system > Stomach > Proventriculus` with one GOLD node, `gold.ecosystem:7431`, and zero assertions. | Supported. |
| Ontology identity | `data/raw/ontology_terms.tsv:13331` labels `UBERON:0007357` `proventriculus` and defines it as the glandular or true stomach of a bird between the crop and gizzard. | Supported for the Bird path. |
| Ontology parent | `data/raw/ontology_subclass_edges.tsv:11605` asserts `UBERON:0007357` `rdfs:subClassOf` `UBERON:0011953`; `data/raw/ontology_terms.tsv:13435` labels `UBERON:0011953` `stomach glandular region`. | Supported. |
| Bird source-path parent | `data/raw/gold_ecosystem_paths.tsv:1027` has the immediate parent path `Host-associated > Birds > Digestive system > Stomach`, generated as `habitatmech:GOLD.7c20efa06b`. | Supported. |

The Insect GOLD path does **not** support exact `UBERON:0007357` grounding.
`data/raw/gold_ecosystem_paths.tsv:1797` places
`Proventriculus/Gizzard` under `Host-associated > Arthropoda: Insects >
Digestive system > Foregut`, whose immediate parent is generated as
`habitatmech:GOLD.bd1664969c`. The current item-level decision nevertheless
grounds `habitatmech:GOLD.e83536dc3f` to the avian UBERON term exactly:

| Subject | Predicate | Object | Status | Review depth |
|---|---|---|---|---|
| `habitatmech:GOLD.e83536dc3f` | `GROUND` | `UBERON:0007357` / `proventriculus` | `EXACT` | `ITEM` |

That maintained row conflates the insect foregut `Proventriculus/Gizzard`
source concept with the avian glandular stomach term. As a result, the
generated UBERON record now carries an insect source attestation and an insect
Foregut parent that are not strictly broader than the record's avian identity.

The exact same-label habitat search is otherwise narrow. A hidden/
ignored-inclusive search of `data/habitats/` for `label: proventriculus`,
`source_label: Proventriculus`, and `source_label: Proventriculus/Gizzard`
found only this generated target. `BTO:0001136`, the only additional vendored
`proventriculus` label, has a polysemous definition covering bird, insect, and
earthworm senses; hidden/ignored-inclusive searches found no generated record
or maintained decision using it.

## Evidence

| Claim | Evidence checked | Assessment |
|---|---|---|
| `gold.ecosystem:7431` attests the Bird Proventriculus path. | `data/raw/gold_ecosystem_paths.tsv:1879` lists the exact Bird path, the leaf label `Proventriculus`, one GOLD node, zero organism assertions, zero study assertions, zero biosample assertions, and zero total assertions. | Supported. |
| `gold.ecosystem:7198` attests the Insect `Proventriculus/Gizzard` path. | `data/raw/gold_ecosystem_paths.tsv:1797` lists the exact Insect Foregut path, the leaf label `Proventriculus/Gizzard`, one GOLD node, zero organism assertions, zero study assertions, zero biosample assertions, and zero total assertions. | Supported. |
| The Bird source path and the Insect source path have no generated MIxS environmental parameters, characteristic taxa, biosample rows, or study rows. | Exact hidden/ignored-inclusive searches of `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, `data/raw/gold_studies.tsv`, and `data/raw/gold_ecosystem_paths.tsv` for both full GOLD paths and both GOLD node ids found only the aggregate `gold_ecosystem_paths.tsv` rows. | Supported. |
| `parent_habitats: UBERON:0011953` is the ontology parent of `UBERON:0007357`. | The vendored subclass slice asserts `UBERON:0007357` `rdfs:subClassOf` `UBERON:0011953`. | Supported. |
| `parent_habitats: habitatmech:GOLD.7c20efa06b` is the Bird source-path parent. | The Bird path's immediate parent string is `Host-associated > Birds > Digestive system > Stomach`, whose generated record has identifier `habitatmech:GOLD.7c20efa06b`. | Supported. |
| `parent_habitats: habitatmech:GOLD.bd1664969c` is a broader parent of this UBERON record. | `habitatmech:GOLD.bd1664969c` is the Insect Foregut path parent, not a broader term for avian proventriculus. It appears only because the Insect `Proventriculus/Gizzard` source concept was merged into this UBERON record. | Unsupported. |
| `source_attestations[gold.ecosystem:7198]` is an exact match to avian `UBERON:0007357`. | The raw path is explicitly under `Arthropoda: Insects`; the UBERON definition is explicitly the glandular/true stomach of a bird. | Unsupported. |

The record has no generated characteristic taxa, environmental parameters,
curator evidence objects, datasets, or causal edges. That is appropriate here:
both GOLD aggregate rows are zero-assertion source paths with no committed GOLD
side-table rows.

iModulonDB was not applicable: the target is a GOLD anatomical habitat, not a
gene, locus tag, UniProt accession, regulator, iModulon, pathway,
stress-response record, or transcriptomics dataset.

## Completeness

The record is schema-valid and reproducible from maintained inputs, but those
inputs currently over-merge an insect source concept into an avian UBERON
identity. The Bird `Stomach > Proventriculus` source path is exact enough for
`UBERON:0007357`; the Insect `Foregut > Proventriculus/Gizzard` source path
needs to be split back out to a minted record or regrounded to a verified
insect-compatible term.

Before this report was written, exact hidden/ignored-inclusive searches for
`UBERON:0007357`, `BTO:0001136`, `habitatmech:GOLD.e83536dc3f`,
`habitatmech:GOLD.8f147900b1`, `gold.ecosystem:7198`,
`gold.ecosystem:7431`, `proventriculus`, `Proventriculus/Gizzard`, and both
full GOLD source paths across `data/habitats`, `data/raw`, `curation`,
`history`, `research`, `reports`, and `conf` found:

- the generated `proventriculus.yaml` target;
- the path lock for `UBERON:0007357`;
- both aggregate GOLD source rows;
- the item-level insect decision in `curation/decisions.tsv`;
- the Gizzard review's cross-reference to that insect decision;
- the background `proventriculus` mentions in the Gaster research report; and
- no item-level Bird Proventriculus decision, append-only history record,
  causal overlay, target-specific research report, or prior exact
  Proventriculus YAML review.

An ignored-inclusive `find` over `reports/yaml_record_review`,
`research/habitats`, `history`, and `curation/causal_graphs` found no
Proventriculus-named review, history, research, or causal overlay artifact
before this report was created.

## Findings

No blocker findings.

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The item-level Insect `Proventriculus/Gizzard` decision incorrectly merges an insect foregut concept into the avian `UBERON:0007357` proventriculus record. | `curation/decisions.tsv` grounds `habitatmech:GOLD.e83536dc3f` exactly to `UBERON:0007357`, but `data/raw/gold_ecosystem_paths.tsv:1797` places that GOLD source under `Host-associated > Arthropoda: Insects > Digestive system > Foregut > Proventriculus/Gizzard`, while `data/raw/ontology_terms.tsv:13331` defines `UBERON:0007357` as the glandular or true stomach of a bird. This wrong merge also adds the insect Foregut parent `habitatmech:GOLD.bd1664969c` to the avian UBERON record. | `curation/decisions.tsv` row for `habitatmech:GOLD.e83536dc3f` |
| Minor | The Bird GOLD Proventriculus source concept has not received item-level grounding review. | Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.8f147900b1`, `gold.ecosystem:7431`, and the full Bird Proventriculus source path found no maintained decision or history record for this source concept, and the generated record remains `mapping_status: SEEDED`. The current exact `UBERON:0007357` grounding for the Bird path itself is supported by the full GOLD path and the vendored UBERON row. | `curation/decisions.tsv` |

## Recommended Edits

1. Replace the `curation/decisions.tsv` row for
   `habitatmech:GOLD.e83536dc3f` so the Insect `Proventriculus/Gizzard`
   source concept no longer exact-merges into `UBERON:0007357`. If a strict
   insect-compatible broader term is verified in the vendored slice, use
   `GROUND_AS_PARENT`; otherwise use item-level `CONFIRM_UNGROUNDED` so the
   insect source concept stays minted, and add a term request for an insect
   proventriculus/gizzard habitat only if a local HabitatMech definition is
   needed.

2. Add an item-level `GROUND` row for
   `habitatmech:GOLD.8f147900b1` in `curation/decisions.tsv`, preserving
   `UBERON:0007357`, `proventriculus`, `grounding_status: EXACT`, and
   `review_depth: ITEM` for the Bird source path.

3. Add the corresponding append-only curation history record under `history/`,
   then rerun the seeding pipeline. The regenerated avian
   `data/habitats/host_associated/proventriculus.yaml` should retain only the
   Bird source attestation and should drop `habitatmech:GOLD.bd1664969c`;
   the insect source concept should survive as a separate minted record under
   the Insect Foregut source-path parent.

## Follow-up Checks

After fixing the maintained decisions, run:

1. `just seed`
2. `just seed-canary UBERON:0007357`
3. `just seed-canary habitatmech:GOLD.e83536dc3f`
4. `just seed-apply --force`
5. `just validate data/habitats/host_associated/proventriculus.yaml`
6. `just validate-strict data/habitats/host_associated/proventriculus.yaml`
7. `just validate-causal-all`
8. `just validate-history`
9. `just term-requests-check`
10. `just verify-corpus`
11. `just report --ungrounded-top 0 --out /tmp/habitatmech-report-after-proventriculus.tsv`
12. `git diff --check`

Manually inspect the regenerated insect `Proventriculus/Gizzard` record and
confirm that the Insect Foregut source-path parent stays with that record
rather than with `UBERON:0007357`.

## Additional Notes

This report does not review the broader generated Insect `Foregut` record.
`data/habitats/host_associated/foregut__ce63e8ab.yaml` is a separate seeded
`NARROW` GOLD record that should receive its own item-level grounding review.

The existing `BTO:0001136` `proventriculus` row is not an automatic replacement
grounding. Its vendored definition combines bird, insect, and earthworm senses,
so adopting it for the Insect `Proventriculus/Gizzard` source concept still
requires an item-level curator decision that it is exact or strictly broader
for this specific GOLD path.
