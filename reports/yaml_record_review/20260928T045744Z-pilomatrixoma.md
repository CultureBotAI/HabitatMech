# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/pilomatrixoma.yaml`
- Started UTC: 2026-09-28T04:57:44Z
- Finished UTC: 2026-09-28T04:57:44Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.4a9a3f8366` |
| Label | `Pilomatrixoma` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Generated path | `data/habitats/host_associated/pilomatrixoma.yaml` |
| GOLD path | `Host-associated > Mammals: Human > Benign tumor > Pilomatrixoma` |

The target is a generated, GOLD-only host-associated record. It has one GOLD
source attestation, one generated parent, no definition, no xrefs, no
environmental parameters, no characteristic taxa, no record-level evidence, no
causal graphs, no discussions, and no datasets.

This review makes no generated YAML or page edits. The current record is
byte-reproducible from committed inputs, and the remaining defects belong in
the maintained curation layer and in the GOLD source-path parent emitter.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/pilomatrixoma.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/host_associated/pilomatrixoma.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows; wrote `reports/instance_validation_failures.tsv`. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against the vendored history schema. |
| `just verify-corpus` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --status all --out /tmp/habitatmech-pilomatrixoma-worklist.tsv` | Passed; wrote 953 ungrounded rows and kept `habitatmech:GOLD.4a9a3f8366` in the ungrounded worklist. |
| `just report --out /tmp/habitatmech-pilomatrixoma-report.tsv` | Passed; wrote 3206 corpus rows and listed this target with 1 `GOLD` source, 0 source assertions, 1 parent, 0 environmental parameters, 0 characteristic taxa, and 0 causal graphs. |

No required validator was skipped. The target has no causal graph, no
record-local `EvidenceItem`, and no dataset reference for a narrower
record-local reference validator to inspect.

The strict validator left `reports/instance_validation_failures.tsv`
unchanged.

## Identity and Grounding

The generated identifier, label, category, GOLD source ID, class-level curation
history, and duplicate-node note agree with the committed source inventory:

- `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.4a9a3f8366` to
  `pilomatrixoma`.
- `data/raw/gold_ecosystem_paths.tsv` has one exact aggregate row for
  `Host-associated > Mammals: Human > Benign tumor > Pilomatrixoma`.
- The exact aggregate row records two collapsed GOLD node IDs and zero
  organism, study, biosample, and total assertions.
- `curation/decisions.tsv` has one `CLASS`-depth `CONFIRM_UNGROUNDED` row for
  `habitatmech:GOLD.4a9a3f8366`, so the generated `UNGROUNDED` /
  `SEEDED` state is expected.

The exact GOLD ecosystem-path row has:

| Column | Value |
|---|---|
| `canonical_path` | `Host-associated > Mammals: Human > Benign tumor > Pilomatrixoma` |
| `ecosystem` | `Host-associated` |
| `ecosystem_category` | `Mammals: Human` |
| `ecosystem_type` | `Benign tumor` |
| `ecosystem_subtype` | `Pilomatrixoma` |
| `specific_ecosystem` | empty |
| `leaf_label` | `Pilomatrixoma` |
| `depth` | `4` |
| `gold_node_count` | `2` |
| `organism_count` | `0` |
| `study_count` | `0` |
| `biosample_count` | `0` |
| `total_assertions` | `0` |
| `gold_node_ids` | `gold.ecosystem:6995|gold.ecosystem:6996` |

The grounding decision is not item-reviewed. The class-level sweep proves only
that no vendored term matched the leaf label through the configured lexical
routes; its note explicitly says whether the concept is a habitat at all was
not assessed.

That matters here because GOLD places `Pilomatrixoma` directly below
`Benign tumor`, and `curation/decisions.tsv` has already item-reviewed the
parent `habitatmech:GOLD.333c18201f` as `NOT_APPLICABLE`: a non-habitat source
concept. This target needs item-level curation before it can remain a real
`UNGROUNDED` habitat, request an ENVO term, or be reclassified as
`NOT_APPLICABLE`.

## Evidence

| YAML claim | Maintained evidence | Review |
|---|---|---|
| `identifier: habitatmech:GOLD.4a9a3f8366` | `data/habitats/PATHS.tsv` pins the generated minted ID to `pilomatrixoma`; the minted identifier follows from the exact canonical path. | Supported. |
| `label: Pilomatrixoma` | The exact `data/raw/gold_ecosystem_paths.tsv` row has `leaf_label` `Pilomatrixoma`. | Supported as the GOLD source label. |
| `habitat_category: HOST_ASSOCIATED` | The GOLD source path starts with `Host-associated`. | Supported mechanically; item-level curation still needs to decide whether this benign-tumor leaf denotes a habitat rather than a tumor class. |
| `grounding_status: UNGROUNDED` and `mapping_status: SEEDED` | `curation/decisions.tsv` has a `CLASS`-depth `CONFIRM_UNGROUNDED` decision for `habitatmech:GOLD.4a9a3f8366`. | Supported mechanically; not sufficient item-level review. |
| `parent_habitats: habitatmech:GOLD.333c18201f` | GOLD's immediate parent path is `Host-associated > Mammals: Human > Benign tumor`. | Generated reproducibly but semantically unsupported, because `habitatmech:GOLD.333c18201f` is item-reviewed as `NOT_APPLICABLE`. |
| GOLD `source_attestations` fields | The exact `data/raw/gold_ecosystem_paths.tsv` row has `gold.ecosystem:6995|gold.ecosystem:6996`, leaf label `Pilomatrixoma`, and path `Host-associated > Mammals: Human > Benign tumor > Pilomatrixoma`. | Supported. The record correctly emits the first node ID and records a duplicate-node note. |
| Omitted `assertion_count` and `assertion_unit` | The exact `data/raw/gold_ecosystem_paths.tsv` row has 0 total assertions. | Supported. |
| Class-sweep `curation_history` | The only item in `curation/decisions.tsv` for this target is the class-level sweep row. | Supported as generated provenance, not as item-level curator review. |

The exact source path has no `data/raw/gold_path_biosamples.tsv`,
`data/raw/gold_path_triads.tsv`, or `data/raw/gold_studies.tsv` row. There is
therefore no raw MIxS broad/local/medium evidence or study co-occurrence row
that would reframe the bare pilomatrixoma leaf as a physical tissue or an
anatomical site.

## Completeness

Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.4a9a3f8366`,
`GOLD.4a9a3f8366`, `4a9a3f8366`, `gold.ecosystem:6995`,
`gold.ecosystem:6996`, `pilomatrixoma`, `Pilomatrixoma`, and
`Host-associated > Mammals: Human > Benign tumor > Pilomatrixoma` covered
`data/habitats`, `data/raw`, `curation`, `history`, `research`, `reports`,
`conf`, `src`, `tests`, `docs`, `.claude`, the `justfile`, and `README.md`.
They found:

- the generated target;
- the `data/habitats/PATHS.tsv` row;
- the exact `data/raw/gold_ecosystem_paths.tsv` row; and
- the `CLASS`-depth `curation/decisions.tsv` row.

The same hidden/ignored-inclusive searches found no target-specific item-level
decision row, term request, append-only history record, causal overlay,
habitat research report, prior exact YAML review report, GOLD biosample row,
GOLD triad row, or GOLD study row.

Searches for the immediate parent found:

- the exact `data/raw/gold_ecosystem_paths.tsv` parent row for
  `Host-associated > Mammals: Human > Benign tumor`;
- the generated `data/habitats/host_associated/benign_tumor.yaml` parent
  record, with `grounding_status: NOT_APPLICABLE` and
  `mapping_status: REVIEWED`; and
- the item-level `NOT_APPLICABLE` row for `habitatmech:GOLD.333c18201f` in
  `curation/decisions.tsv`.

No characteristic taxa, environmental parameters, causal graphs, discussions,
or datasets have a maintained target-specific input.

## Findings

### Blocker

None found.

### Major

| ID | Finding | Maintained owner |
|---|---|---|
| M1 | `data/habitats/host_associated/pilomatrixoma.yaml` still has only a class-level `CONFIRM_UNGROUNDED` decision even though its GOLD path places it under `Benign tumor`, an item-reviewed `NOT_APPLICABLE` non-habitat. A class sweep only found no lexical ontology match; it did not decide that the concept is a habitat. The source concept needs item-level curation and should probably be reclassified as `NOT_APPLICABLE` unless a curator verifies that this GOLD node means pilomatrixoma tissue or a pilomatrixoma-associated environment rather than the tumor class itself. | `curation/decisions.tsv` row for `habitatmech:GOLD.4a9a3f8366` |
| M2 | The record's only `parent_habitats` entry is `habitatmech:GOLD.333c18201f`, but that parent record is already item-reviewed as `NOT_APPLICABLE`. The generated YAML is byte-reproducible, but the source-path parent edge is not a valid strictly broader habitat claim. | `src/habitatmech/seed.py` GOLD source-path parent construction |

### Minor

None found.

## Recommended Edits

1. Replace the `CLASS`-depth `CONFIRM_UNGROUNDED` row for
   `habitatmech:GOLD.4a9a3f8366` with an item-level decision in
   `curation/decisions.tsv`. If curator review confirms that `Pilomatrixoma`
   names the benign tumor class rather than a tissue or other habitat, use
   `NOT_APPLICABLE` and record the GOLD source path in the note.
2. Add the required append-only history record for that decision change under
   `history/`.
3. Update `src/habitatmech/seed.py` so GOLD source-path parent emission cannot
   attach a generated record to a parent source concept whose reviewed status
   is `NOT_APPLICABLE`, and add a regression test proving that
   `parent_habitats` does not contain item-reviewed non-habitats.
4. Reseed `habitatmech:GOLD.4a9a3f8366` and inspect
   `data/habitats/host_associated/pilomatrixoma.yaml` to confirm the
   item-level decision is reflected in `grounding_status`, `mapping_status`,
   and `curation_history`, and that `Benign tumor` no longer appears as a
   broader habitat.

## Follow-up Checks

After the future curation and seeder fixes, run:

```bash
just seed
just seed-canary habitatmech:GOLD.4a9a3f8366
just validate data/habitats/host_associated/pilomatrixoma.yaml
just validate-strict data/habitats/host_associated/pilomatrixoma.yaml
just validate-causal-all
just term-requests-check
just validate-history
just verify-corpus
just worklist --status all --out /tmp/habitatmech-pilomatrixoma-worklist.tsv
just report --out /tmp/habitatmech-pilomatrixoma-report.tsv
git diff --check
```

## Additional Notes

This review intentionally leaves `data/habitats/host_associated/pilomatrixoma.yaml`
unchanged. The YAML faithfully records the current seeded result; the remaining
curation task is to decide the exact GOLD source concept and prevent generated
`NOT_APPLICABLE` parents from being emitted as strict habitat parents.
