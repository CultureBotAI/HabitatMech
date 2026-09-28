# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/testicular_non_seminoma.yaml`
- Started UTC: 2026-09-28T05:35:45Z
- Finished UTC: 2026-09-28T05:35:45Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.4ad87f756c` |
| Label | `Testicular non-seminoma` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Generated path | `data/habitats/host_associated/testicular_non_seminoma.yaml` |
| GOLD path | `Host-associated > Mammals: Human > Malignant tumor > Germ cell tumor > Testicular non-seminoma` |

The target is a generated GOLD-only host-associated record. It has one GOLD
source attestation, one generated parent, no definition, no xrefs, no
environmental parameters, no characteristic taxa, no record-local evidence, no
causal graphs, no discussions, and no datasets.

This review makes no generated YAML or page edits. The current YAML is
byte-reproducible from committed inputs, and the unresolved defects belong in
maintained curation plus the GOLD source-path parent emitter.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/testicular_non_seminoma.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/host_associated/testicular_non_seminoma.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows; wrote `reports/instance_validation_failures.tsv`. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against the vendored history schema. |
| `just verify-corpus` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --status all --out /tmp/habitatmech-testicular-non-seminoma-worklist.tsv` | Passed; wrote 953 ungrounded rows and kept `habitatmech:GOLD.4ad87f756c` in the ungrounded worklist. |
| `just report --out /tmp/habitatmech-testicular-non-seminoma-report.tsv` | Passed; wrote 3206 corpus rows and listed this target with 1 `GOLD` source, 0 source assertions, 1 parent, 0 environmental parameters, 0 characteristic taxa, and 0 causal graphs. |

No required validator was skipped. The target has no causal graph, no
record-local `EvidenceItem`, and no dataset reference for a narrower
record-local reference validator to inspect.

The strict validator left `reports/instance_validation_failures.tsv`
unchanged.

## Identity and Grounding

The generated identifier, label, category, GOLD source ID, class-level curation
history, and `UNGROUNDED` / `SEEDED` state agree with the committed source and
curation inventories:

- `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.4ad87f756c` to
  `testicular_non_seminoma`.
- `data/raw/gold_ecosystem_paths.tsv` has one exact row for
  `Host-associated > Mammals: Human > Malignant tumor > Germ cell tumor > Testicular non-seminoma`.
- That exact source row records one GOLD node ID, `gold.ecosystem:6203`.
- `curation/decisions.tsv` has one `CLASS`-depth `CONFIRM_UNGROUNDED` row for
  `habitatmech:GOLD.4ad87f756c`, so the generated `UNGROUNDED` /
  `SEEDED` state is expected.

The exact GOLD ecosystem-path row has:

| Column | Value |
|---|---|
| `canonical_path` | `Host-associated > Mammals: Human > Malignant tumor > Germ cell tumor > Testicular non-seminoma` |
| `ecosystem` | `Host-associated` |
| `ecosystem_category` | `Mammals: Human` |
| `ecosystem_type` | `Malignant tumor` |
| `ecosystem_subtype` | `Germ cell tumor` |
| `specific_ecosystem` | `Testicular non-seminoma` |
| `leaf_label` | `Testicular non-seminoma` |
| `depth` | `5` |
| `gold_node_count` | `1` |
| `organism_count` | `0` |
| `study_count` | `0` |
| `biosample_count` | `0` |
| `total_assertions` | `0` |
| `gold_node_ids` | `gold.ecosystem:6203` |

The raw GOLD bulk-export inventory separately records 4 biosamples on
`gold.ecosystem:6203`, and `data/raw/gold_studies.tsv` records one study,
`Gs0150275`, whose submitted paths include both `Testicular non-seminoma` and
15 other human tumor or host-associated paths. That is useful source context,
but it is not item-level curation: it does not prove that the bare GOLD leaf
denotes a microbial habitat rather than a tumor diagnosis bucket.

The target's only curation row is still the class-level lexical miss. That
class sweep only proved that no vendored term matched the leaf label through
the configured lexical routes; its note explicitly says whether the concept is
a habitat at all was not assessed.

That limitation matters here because GOLD places `Testicular non-seminoma`
directly below `Germ cell tumor`, and `curation/decisions.tsv` has already
item-reviewed the parent `habitatmech:GOLD.fd2b0ef71a` as `NOT_APPLICABLE`: a
non-habitat disease concept. Its parent `Malignant tumor` is likewise
item-reviewed as `NOT_APPLICABLE`. This target needs item-level curation before
it can remain an ungrounded habitat, request an ENVO term, or be reclassified
as non-applicable.

## Evidence

| YAML claim | Maintained evidence | Review |
|---|---|---|
| `identifier: habitatmech:GOLD.4ad87f756c` | `data/habitats/PATHS.tsv` pins this generated minted ID to `testicular_non_seminoma`; the minted ID follows from the exact GOLD path. | Supported. |
| `label: Testicular non-seminoma` | The exact `data/raw/gold_ecosystem_paths.tsv` row has `leaf_label` `Testicular non-seminoma`. | Supported as the GOLD source label. |
| `habitat_category: HOST_ASSOCIATED` | The GOLD source path starts with `Host-associated`. | Supported mechanically; item-level curation still needs to decide whether this malignant-tumor leaf denotes a habitat rather than a cancer subtype. |
| `grounding_status: UNGROUNDED` and `mapping_status: SEEDED` | `curation/decisions.tsv` has a `CLASS`-depth `CONFIRM_UNGROUNDED` decision for `habitatmech:GOLD.4ad87f756c`. | Supported mechanically; not sufficient item-level review. |
| `parent_habitats: habitatmech:GOLD.fd2b0ef71a` | GOLD's immediate parent path is `Host-associated > Mammals: Human > Malignant tumor > Germ cell tumor`. | Generated reproducibly but semantically unsupported, because `habitatmech:GOLD.fd2b0ef71a` is item-reviewed as `NOT_APPLICABLE`. |
| GOLD `source_attestations` fields | The exact `data/raw/gold_ecosystem_paths.tsv` row has node ID `gold.ecosystem:6203`, leaf label `Testicular non-seminoma`, and the same full path. | Supported. |
| Omitted duplicate-node note | The exact `data/raw/gold_ecosystem_paths.tsv` row has `gold_node_count` 1. | Supported. |
| Omitted `assertion_count` and `assertion_unit` | The exact `data/raw/gold_ecosystem_paths.tsv` row still has 0 total assertions, and `just report` lists 0 GOLD source assertions for this record. | Supported mechanically; the auxiliary bulk-export biosample inventory records 4 biosamples for the same path. |
| Class-sweep `curation_history` | The only row in `curation/decisions.tsv` for this target is the class-level sweep row. | Supported as generated provenance, not as item-level curator review. |

The exact target path has no `data/raw/gold_path_triads.tsv` row. The existing
4-biosample inventory and one broad GOLD study co-occurrence row therefore
provide no raw MIxS broad/local/medium evidence that would reframe the
testicular-non-seminoma leaf as a material, anatomical site, cell culture, or
other habitat.

iModulonDB was not applicable to this record: it names a GOLD ecosystem path,
not a gene, regulator, locus, strain, transcriptomic dataset, or iModulon.

## Completeness

Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.4ad87f756c`,
`GOLD.4ad87f756c`, `4ad87f756c`, `gold.ecosystem:6203`,
`testicular_non_seminoma`, `Testicular non-seminoma`, and the exact GOLD path
`Host-associated > Mammals: Human > Malignant tumor > Germ cell tumor > Testicular non-seminoma`
covered `data/habitats`, `data/raw`, `curation`, `history`, `research`,
`reports`, `conf`, `src`, `tests`, `docs`, `.claude`, the `justfile`, and
`README.md`.

They found:

- the generated target;
- the `data/habitats/PATHS.tsv` row;
- the `CLASS`-depth `curation/decisions.tsv` row;
- the exact `data/raw/gold_ecosystem_paths.tsv` row;
- the exact `data/raw/gold_path_biosamples.tsv` row; and
- the one `data/raw/gold_studies.tsv` row that mentions the target path.

The same hidden/ignored-inclusive searches found no target-specific item-level
decision, term request, append-only history record, causal overlay, habitat
research report, prior exact YAML review report, or GOLD triad row.

Searches for the immediate GOLD parent found:

- the exact `data/raw/gold_ecosystem_paths.tsv` row for
  `Host-associated > Mammals: Human > Malignant tumor > Germ cell tumor`;
- the generated `data/habitats/host_associated/germ_cell_tumor.yaml` parent
  record, with `grounding_status: NOT_APPLICABLE` and
  `mapping_status: REVIEWED`;
- the `data/habitats/PATHS.tsv` row that pins `habitatmech:GOLD.fd2b0ef71a`
  to `germ_cell_tumor`;
- the item-level `NOT_APPLICABLE` row for `habitatmech:GOLD.fd2b0ef71a` in
  `curation/decisions.tsv`; and
- the generated ovarian and testicular seminoma sibling records that also
  inherit `Germ cell tumor` as their only parent.

No characteristic taxa, environmental parameters, causal graphs, discussions,
or datasets have a maintained target-specific input.

## Findings

### Blocker

None found.

### Major

| ID | Finding | Maintained owner |
|---|---|---|
| M1 | `data/habitats/host_associated/testicular_non_seminoma.yaml` still has only a class-level `CONFIRM_UNGROUNDED` decision even though its GOLD path places it under `Germ cell tumor`, an item-reviewed `NOT_APPLICABLE` disease concept. A class sweep found no lexical ontology match; it did not decide that the source concept is a habitat. The GOLD source concept needs item-level curation and should probably become `NOT_APPLICABLE` unless a curator verifies that `gold.ecosystem:6203` means a testicular non-seminoma sample material or local environment rather than the cancer subtype itself. | `curation/decisions.tsv` row for `habitatmech:GOLD.4ad87f756c` |
| M2 | The record's only `parent_habitats` entry is `habitatmech:GOLD.fd2b0ef71a`, but that parent record is already item-reviewed as `NOT_APPLICABLE`. The generated YAML is byte-reproducible, but the source-path parent edge is not a valid strictly broader habitat claim. | `src/habitatmech/seed.py` GOLD source-path parent construction |

### Minor

None found.

## Recommended Edits

1. Replace the `CLASS`-depth `CONFIRM_UNGROUNDED` row for
   `habitatmech:GOLD.4ad87f756c` with an item-level decision in
   `curation/decisions.tsv`. If curator review confirms that
   `Testicular non-seminoma` names the malignant germ-cell tumor subtype
   rather than a sampled tissue, cell culture, anatomical site, or other
   habitat, use `NOT_APPLICABLE` and include the full GOLD source path in the
   note.
2. Add the required append-only history record for that decision change under
   `history/`.
3. Update `src/habitatmech/seed.py` so GOLD source-path parent emission cannot
   attach a generated record to a parent source concept whose reviewed status
   is `NOT_APPLICABLE`, and add a regression test that rejects item-reviewed
   non-habitats in `parent_habitats`.
4. Reseed `habitatmech:GOLD.4ad87f756c` and inspect
   `data/habitats/host_associated/testicular_non_seminoma.yaml` to confirm the
   item-level decision is reflected in `grounding_status`, `mapping_status`,
   and `curation_history`, and that `Germ cell tumor` no longer appears as a
   broader habitat.

## Follow-up Checks

After the future curation and seeder fixes, run:

```bash
just seed
just seed-canary habitatmech:GOLD.4ad87f756c
just validate data/habitats/host_associated/testicular_non_seminoma.yaml
just validate-strict data/habitats/host_associated/testicular_non_seminoma.yaml
just validate-causal-all
just term-requests-check
just validate-history
just verify-corpus
just worklist --status all --out /tmp/habitatmech-testicular-non-seminoma-worklist.tsv
just report --out /tmp/habitatmech-testicular-non-seminoma-report.tsv
git diff --check
```

## Additional Notes

The auxiliary GOLD bulk-export inventory does see biosamples on
`gold.ecosystem:6203`, but `data/raw/gold_path_biosamples.tsv` records only a
count by path and `data/raw/gold_studies.tsv` records only path co-occurrence.
Those rows are useful for prioritization and for later API triad extraction;
they do not provide a maintained habitat identity, parent, or causal claim for
the generated YAML.
