# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/aquatic/cyanobacterial_bloom.yaml`
- Started UTC: `2026-09-27T11:06:11Z`
- Finished UTC: `2026-09-27T11:06:11Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/aquatic/cyanobacterial_bloom.yaml` |
| Class | `HabitatRecord` |
| Identifier | `ENVO:03600071` |
| Label | `cyanobacterial bloom` |
| Category | `AQUATIC` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Source provenance | One GOLD source concept, `gold.ecosystem:5356` |
| Generated status | Generated from `data/raw/`, the vendored ontology slice, and `src/habitatmech/seed.py`; `data/habitats/PATHS.tsv` pins `ENVO:03600071` to `cyanobacterial_bloom` |

The complete generated record was read before making this judgment. It
contains the ENVO identifier and definition, the ontology parent
`ENVO:00000012`, one generated GOLD source-path `parent_habitats` edge, one
GOLD source attestation, and the seeder history event. It has no synonyms,
xrefs, environmental parameters, characteristic taxa, evidence, causal graphs,
discussions, external datasets, or quality flags.

Before this report was written, ignored-inclusive exact searches over
`data/raw`, `data/habitats`, `curation`, `history`, `research`, `reports`, and
`conf` for `ENVO:03600071`, the source-concept key
`habitatmech:GOLD.95bd6f3756`, `gold.ecosystem:5356`, the exact GOLD path,
`cyanobacterial_bloom`, and related cyanobacterial-bloom labels found the path
lock, the expected raw GOLD rows, the expected vendored ontology rows, the
generated target record, and incidental mentions in the already-reviewed
`cyanobacterial_aggregates` report. A `find` under `curation/causal_graphs`
found no `*cyanobacter*`, `*cyanobacterial*`, or `*bloom*` causal overlay, a
`find` under `research/habitats` found no target-specific research report, and
a `find` under `reports/yaml_record_review` found no pre-existing
`*cyanobacterial_bloom*` YAML-record review report. Those
`rg --no-ignore --hidden` and `find` checks included ignored files.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/cyanobacterial_bloom.yaml` | Passed; LinkML reported no issues. |
| `just validate-all data/habitats/aquatic/cyanobacterial_bloom.yaml --out /tmp/habitatmech-cyanobacterial-bloom-validate-all.tsv` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-strict data/habitats/aquatic/cyanobacterial_bloom.yaml --quiet --out /tmp/habitatmech-cyanobacterial-bloom-validate-strict.tsv` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs were valid. |
| `just validate-history` | Passed; 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; the corpus has the expected 3206 records and reproduces exactly from `data/raw/`. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist-cyanobacterial-bloom.tsv` | Passed; wrote 953 ungrounded rows and reported 1810 decisions on file. |
| `just report` | Passed; emitted the corpus diagnostic report for 3206 records, including 468 `AQUATIC` records, 2520 `SEEDED` records, 1060 `EXACT` records, and 953 `UNGROUNDED` records. |
| Focused reference validator | Not checked: an ignored-inclusive exact `rg` search of `justfile`, `.claude`, `docs`, `scripts`, `src`, and `tests` found no `validate-references` command, and this target has no `evidence` entries to dereference. |

## Identity and Grounding

The GOLD source identity is supported. `data/raw/gold_ecosystem_paths.tsv`
contains exactly
`Environmental > Aquatic > Freshwater > Lake > Cyanobacterial bloom` with leaf
label `Cyanobacterial bloom`, depth 5, one GOLD node, one organism assertion,
and `gold.ecosystem:5356`. The generated source attestation preserves that
GOLD node, label, path, assertion count, exact mapping predicate, and
`ORGANISM` unit.

The committed GOLD API side tables add 115 biosamples and seven GOLD studies
for the exact path. Their MIxS triad summary preserves the same lake context:
`ENVO:01000252` `freshwater lake biome` is the broad scale for all seven
studies, `ENVO:04000007` `lake water` is the medium for all seven studies, and
`ENVO:03600071` `cyanobacterial bloom` is the dominant local-scale term,
spanning five of seven studies.

The ENVO lexical match is supported, but the generated exact identity is too
broad for the source path. `data/raw/ontology_terms.tsv` contains
`ENVO:03600071` with canonical label `cyanobacterial bloom` and the generated
definition text. However, GOLD does not assert a bare cyanobacterial-bloom
concept: this source is a child of `Environmental > Aquatic > Freshwater >
Lake`, and both the broad-scale and medium-scale MIxS rows keep that
freshwater-lake context. The deterministic minted key for the source concept
is `habitatmech:GOLD.95bd6f3756`, which is currently absent from
`curation/decisions.tsv`, `curation/term_requests.tsv`, `data/habitats`, and
`data/habitats/PATHS.tsv`.

The generated ontology parent is supported. `data/raw/ontology_subclass_edges.tsv`
records `ENVO:03600071 rdfs:subClassOf ENVO:00000012`, and
`data/raw/ontology_terms.tsv` defines `ENVO:00000012` `hydrographic feature` as
a geographical feature associated with water.

The generated GOLD source-path parent is not supported. `ENVO:00000021`
denotes `freshwater lake`, and the target's GOLD source path only says that
the cyanobacterial-bloom source concept sits under GOLD's `Lake` path. A
cyanobacterial bloom may occur in a freshwater lake, but it is not a freshwater
lake. `src/habitatmech/seed.py` adds this edge unconditionally in its second
GOLD pass by resolving every child path to the concept of its parent path and
then calling `store.concepts[child_id].parents.add(parent_id)`.

## Evidence

The record has no claim-level `evidence` objects or curator-authored mechanism
claims. Its generated source-attestation, grounding, and hierarchy claims trace
to maintained raw and ontology inputs:

| Claim | Nearest support | Assessment |
|---|---|---|
| The source concept is GOLD `gold.ecosystem:5356` `Cyanobacterial bloom` under `Environmental > Aquatic > Freshwater > Lake`. | `data/raw/gold_ecosystem_paths.tsv:935` carries that exact collapsed GOLD path and node. | Supported exactly. |
| The record has one GOLD organism assertion. | `data/raw/gold_ecosystem_paths.tsv:935` reports one organism assertion, zero study assertions, zero biosample assertions, and one total assertion for the exact path. | Supported exactly. |
| The exact path has additional biosample, study, and MIxS context. | `data/raw/gold_path_biosamples.tsv:211`, the seven `data/raw/gold_studies.tsv` rows at lines 969, 970, 975, 1496, 1497, 3775, and 4574, and `data/raw/gold_path_triads.tsv:323-325` carry 115 biosamples, seven study rows, and the freshwater-lake/cyanobacterial-bloom/lake-water triad summary. | Supported exactly. |
| `ENVO:03600071` is the exact identity. | Generated from a same-label ontology hit for a lake-specific GOLD path. The dominant local-scale MIxS term also names `ENVO:03600071`. | Unsupported as an exact identity; the term is broader than the source path. |
| `ENVO:00000012` is a broader parent. | `data/raw/ontology_subclass_edges.tsv:8505` records the direct ENVO subclass edge. | Supported exactly. |
| `ENVO:00000021` is a broader parent. | Generated by `src/habitatmech/seed.py` from the GOLD parent path `Environmental > Aquatic > Freshwater > Lake`. | Unsupported as an is-a parent; see `HM-CYANOBACTERIAL-BLOOM-001`. |

## Completeness

The GOLD source attestation is complete for the currently committed aggregate
GOLD source inventory. The separate biosample, study, and triad inventories
provide useful context but are not fields on this generated
`SourceAttestation`.

The target lacks the item-level decision needed to keep the source path minted
as a lake-specific cyanobacterial bloom. That future decision should be keyed
by `habitatmech:GOLD.95bd6f3756`, the seeder's deterministic mint for
`GOLD:Environmental > Aquatic > Freshwater > Lake > Cyanobacterial bloom`.

The hierarchy is incomplete because GOLD path context is being emitted as an
`is-a` edge even where the source tree has modeled location rather than
subtyping. A future minted record should keep `ENVO:03600071` as its true
bloom parent and stop claiming that the bloom is a kind of `freshwater lake`.

No causal graph, evidence, environmental-parameter, characteristic-taxon,
discussion, or external-dataset input is currently maintained for this exact
record. Those empty optional fields are acceptable on this seeded GOLD-only
record.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| HM-CYANOBACTERIAL-BLOOM-001 | Major | GOLD's freshwater-lake-specific `Cyanobacterial bloom` source concept is grounded exactly to generic `ENVO:03600071` and inherits false parent `ENVO:00000021` `freshwater lake`. | The target's GOLD source path is `Environmental > Aquatic > Freshwater > Lake > Cyanobacterial bloom`; exact-path MIxS rows report `freshwater lake biome` at broad scale and `lake water` as medium; the generated record uses the generic ENVO cyanobacterial-bloom term as its identity; the parent path resolves to the reviewed `ENVO:00000021` `freshwater lake` record; and `src/habitatmech/seed.py` unconditionally adds resolved GOLD parent paths as `parent_habitats`. A cyanobacterial bloom in a lake is a narrower bloom feature, not a freshwater-lake subtype. | Add an item-level `GROUND_AS_PARENT` decision for `habitatmech:GOLD.95bd6f3756` in `curation/decisions.tsv`, preserve the `cyanobacterial_bloom` slug for that minted source concept in `data/habitats/PATHS.tsv`, and add a minted definition under `ENVO:03600071` in `curation/term_requests.tsv` with `parent_mode=REPLACE` so the inherited lake parent is dropped. |

## Recommended Edits

1. Add an item-level `GROUND_AS_PARENT` decision for
   `habitatmech:GOLD.95bd6f3756` in `curation/decisions.tsv`, grounding the
   GOLD source concept as narrower than `ENVO:03600071` `cyanobacterial bloom`
   and recording the exact GOLD path plus the MIxS broad/local/medium rows.
2. Replace the existing `data/habitats/PATHS.tsv` pin for `ENVO:03600071` with
   a pin from `habitatmech:GOLD.95bd6f3756` to `cyanobacterial_bloom`, so the
   corrected minted record keeps the current filename instead of creating a
   new collision-resolved slug.
3. Add a `curation/term_requests.tsv` definition for a minted freshwater-lake
   cyanobacterial-bloom class under `ENVO:03600071`, using
   `parent_mode=REPLACE` because `ENVO:00000021` is contextual rather than a
   strict broader parent.
4. Regenerate only through the seeder with `just seed`, then
   `just seed-canary habitatmech:GOLD.95bd6f3756 --force`, and inspect
   `data/habitats/aquatic/cyanobacterial_bloom.yaml` to confirm that the
   minted identifier replaced `ENVO:03600071`, `ENVO:03600071` is a parent, and
   `ENVO:00000021` was removed.

## Follow-up Checks

1. Run `just validate data/habitats/aquatic/cyanobacterial_bloom.yaml`.
2. Run `just validate-all data/habitats/aquatic/cyanobacterial_bloom.yaml`.
3. Run `just term-requests`.
4. Run `just validate-causal-all`.
5. Run `just validate-history`.
6. Run `just verify-corpus --max-diffs 1`.
7. Repeat ignored-inclusive searches for `habitatmech:GOLD.95bd6f3756`,
   `ENVO:03600071`, `gold.ecosystem:5356`,
   `Environmental > Aquatic > Freshwater > Lake > Cyanobacterial bloom`, and
   `cyanobacterial_bloom` over maintained raw, curation, generated record,
   research, history, report, and config paths to ensure no other maintained
   owner needs a parallel update.

## Additional Notes

The adjacent `Environmental > Aquatic > Freshwater > Lake > Cyanobacterial aggregates`
GOLD source concept is separate and should remain separate. It has no exact
vendored ontology identity, whereas this target's source concept is narrower
than an exact vendored `cyanobacterial bloom` parent.
