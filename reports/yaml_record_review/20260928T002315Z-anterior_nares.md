# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/anterior_nares.yaml`
- Started UTC: 2026-09-28T00:23:15Z
- Finished UTC: 2026-09-28T00:23:15Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.48ff047301` |
| Label | `Anterior nares` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Generated path | `data/habitats/host_associated/anterior_nares.yaml` |
| GOLD path | `Host-associated > Mammals > Respiratory system > Nasal cavity > Anterior nares` |

The target is the Mammals-level GOLD `Anterior nares` node. It is distinct from
the Human sibling at
`Host-associated > Mammals: Human > Respiratory system > Nasal cavity > Anterior nares`,
which is generated as `data/habitats/host_associated/anterior_nares__14fc5dcc.yaml`.

This target has one GOLD source attestation, two generated parents, no
definition, no xrefs, no environmental parameters, no characteristic taxa, no
record-level evidence, no causal graphs, no discussions, and no datasets.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/anterior_nares.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/host_associated/anterior_nares.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated against the vendored history schema. |
| `just verify-corpus` | Passed; 3206 records were expected, 3206 were found, and `data/habitats/` reproduced exactly from `data/raw/`. |
| `just worklist --status all --out /tmp/habitatmech-anterior-nares-worklist.tsv` | Passed; wrote 953 ungrounded rows to `/tmp/habitatmech-anterior-nares-worklist.tsv`; this `NARROW` target is not an ungrounded worklist item. |
| `just report --out /tmp/habitatmech-anterior-nares-report.tsv` | Passed; wrote `/tmp/habitatmech-anterior-nares-report.tsv` and listed this target with 1 `GOLD` source, 0 source assertions, 2 parents, and 0 populated optional claim collections. |

No required validator was skipped. The target has no causal graph, no
`EvidenceItem` references, and no dataset references for a narrower
record-local reference validator to inspect.

The strict validator left `reports/instance_validation_failures.tsv`
unchanged.

## Identity and Grounding

The generated identifier, label, host-associated category, source attestation,
path lock, and unreviewed `SEEDED` status agree with the committed source
inventory:

- `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.48ff047301` to
  `anterior_nares`.
- `data/raw/gold_ecosystem_paths.tsv` has an exact row for
  `Host-associated > Mammals > Respiratory system > Nasal cavity > Anterior nares`.
- There is no item-level `curation/decisions.tsv` row for
  `habitatmech:GOLD.48ff047301`, so the generated `SEEDED` mapping status is
  expected.

The exact GOLD ecosystem-path row has:

| Column | Value |
|---|---|
| `canonical_path` | `Host-associated > Mammals > Respiratory system > Nasal cavity > Anterior nares` |
| `ecosystem` | `Host-associated` |
| `ecosystem_category` | `Mammals` |
| `ecosystem_type` | `Respiratory system` |
| `ecosystem_subtype` | `Nasal cavity` |
| `specific_ecosystem` | `Anterior nares` |
| `leaf_label` | `Anterior nares` |
| `depth` | `5` |
| `gold_node_count` | `1` |
| `organism_count` | `0` |
| `study_count` | `0` |
| `biosample_count` | `0` |
| `total_assertions` | `0` |
| `gold_node_ids` | `gold.ecosystem:6827` |

The `NARROW` grounding to `UBERON:0005928` `external naris` is a defensible
automatic fallback. The vendored UBERON row labels `UBERON:0005928` as
`external naris`, defines it as a naris that provides an external head opening
for breathing, and includes `anterior nares` as a synonym. GOLD has two
same-depth `Anterior nares` source paths, so the shallowest-leaf guard minted
both GOLD concepts rather than letting either source row claim the UBERON term
without item-level review.

The source-path parent edge to `habitatmech:GOLD.c9756cb050` is not sound as a
strict broader habitat. That parent is GOLD's Mammals-level
`Host-associated > Mammals > Respiratory system > Nasal cavity` row. An
anterior naris is an external opening into the respiratory tract; it is not a
kind of nasal cavity.

## Evidence

| YAML claim | Maintained evidence | Review |
|---|---|---|
| `identifier: habitatmech:GOLD.48ff047301` | `data/habitats/PATHS.tsv` pins the minted GOLD identifier to `anterior_nares`; the minted identifier follows from the exact canonical path. | Supported. |
| `label: Anterior nares` | The exact `data/raw/gold_ecosystem_paths.tsv` row has `leaf_label` `Anterior nares`. | Supported as the source label. |
| `habitat_category: HOST_ASSOCIATED` | The GOLD source path starts with `Host-associated > Mammals`. | Supported. |
| `grounding_status: NARROW` and `mapping_predicate: skos:narrowMatch` | The vendored ontology has `UBERON:0005928` `external naris` with synonym `anterior nares`; GOLD also has a Human `Anterior nares` sibling at the same depth. | Supported as a generated ambiguous-leaf fallback pending item-level review. |
| `mapping_status: SEEDED` | Hidden/ignored-inclusive searches found no item-level decision for `habitatmech:GOLD.48ff047301`. | Supported. |
| `parent_habitats: UBERON:0005928` | `data/raw/ontology_terms.tsv` labels `UBERON:0005928` as `external naris` and lists `anterior nares` as a synonym. | Supported as a broader anatomical parent. |
| `parent_habitats: habitatmech:GOLD.c9756cb050` | GOLD's immediate parent path resolves to the Mammals-level `Nasal cavity` source concept. | Unsupported as a habitat parent. This is source-path anatomy context, not a strict broader class for the external naris. |
| GOLD `source_attestations` fields | The exact `data/raw/gold_ecosystem_paths.tsv` row has one node, `gold.ecosystem:6827`, and no direct organism, study, biosample, or total assertions. | Supported. The absent `assertion_count` and `assertion_unit` are correct for a zero-assertion GOLD row. |

Unlike the Human `Anterior nares` sibling, the exact
`Host-associated > Mammals > Respiratory system > Nasal cavity > Anterior nares`
path has no `data/raw/gold_path_biosamples.tsv`,
`data/raw/gold_path_triads.tsv`, or `data/raw/gold_studies.tsv` row. The Human
sibling has a GOLD biosample side-table row and two GOLD study side-table rows;
those rows do not feed this Mammals-level target.

## Completeness

Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.48ff047301`,
`48ff047301`, `gold.ecosystem:6827`, `anterior_nares`,
`Anterior nares`, and
`Host-associated > Mammals > Respiratory system > Nasal cavity > Anterior nares`
covered `data/habitats`, `data/raw`, `curation`, `history`, `research`,
`reports`, `conf`, `src`, `tests`, `docs`, the `justfile`, and `README.md`.
They found:

- the generated target;
- the `data/habitats/PATHS.tsv` row;
- the exact `data/raw/gold_ecosystem_paths.tsv` row;
- the immediate GOLD parent row for
  `Host-associated > Mammals > Respiratory system > Nasal cavity`;
- the Human `Anterior nares` sibling;
- the generated Mammals `nasal_cavity__05a49906` source-path parent;
- the vendored `UBERON:0005928` `external naris` row and its ontology
  subclass edges.

The same search found no target-specific decision row, term request, history
record, causal overlay, habitat research report, prior exact YAML review
report, raw GOLD biosample row, raw GOLD triad row, or raw GOLD study row for
this exact Mammals target path.

No characteristic taxa, environmental parameters, causal graphs, discussions,
or datasets are expected on this zero-assertion generated GOLD leaf.

## Findings

### Blocker

None found.

### Major

| ID | Finding | Maintained owner |
|---|---|---|
| M1 | `parent_habitats` keeps the GOLD source-path locality as an `is_a` edge: `data/habitats/host_associated/anterior_nares.yaml` says mammalian anterior nares are a kind of `habitatmech:GOLD.c9756cb050` Mammals `Nasal cavity`. The external naris is anatomically adjacent to the nasal cavity, not a subclass of nasal cavity. | Maintained GOLD path-parent suppression consumed by `src/habitatmech/seed.py`; if curation instead keeps this source concept under a minted identifier, a curated definition in `curation/term_requests.tsv` would also need `parent_mode: REPLACE`. |

### Minor

None found.

## Recommended Edits

1. Add an item-level decision in `curation/decisions.tsv` for
   `habitatmech:GOLD.48ff047301`. The expected grounding target is
   `UBERON:0005928` `external naris`; inspect the Mammals and Human GOLD
   `Anterior nares` rows together before deciding whether both are exact
   anatomical attestations.
2. Suppress `habitatmech:GOLD.c9756cb050` as an inherited source-path parent
   for this anterior-nares source row. If a future exact `GROUND` decision
   merges the source into `UBERON:0005928`, confirm the false nasal-cavity edge
   does not move onto the generated `external naris` record.
3. Regenerate with:

```bash
just seed
just seed-canary habitatmech:GOLD.48ff047301
just seed-apply --force
```

No hand edit is recommended for `data/habitats/host_associated/anterior_nares.yaml`.

## Follow-up Checks

After the future curation edit:

1. Re-read the regenerated anterior-nares record and confirm it no longer lists
   `habitatmech:GOLD.c9756cb050` as a parent.
2. Confirm the GOLD source attestation for `gold.ecosystem:6827` is preserved.
3. Inspect `data/habitats/host_associated/anterior_nares__14fc5dcc.yaml` or its
   regenerated replacement so the Human sibling keeps a valid broader
   external-naris parent and does not inherit an invalid nasal-cavity `is_a`
   edge.
4. Run:

```bash
just validate-causal-all
just validate-strict <regenerated-record-path>
just verify-corpus
just term-requests-check
just validate-history
```

## Additional Notes

This review intentionally makes no generated YAML, page, decision, or term
request edits. The YAML faithfully records the current seeded result; the
remaining curation task is to maintain the correct item-level grounding and
source-path hierarchy for a sparse GOLD anatomical leaf.
