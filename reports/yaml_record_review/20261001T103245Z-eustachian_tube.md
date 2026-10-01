# YAML Record Review: Eustachian tube

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/eustachian_tube.yaml`
- Started UTC: `2026-10-01T10:32:45Z`
- Finished UTC: `2026-10-01T10:34:54Z`
- Verdict: needs curation

## Target

Reviewed the complete generated `HabitatRecord` for the GOLD Mammals
middle-ear `Eustachian tube` path:

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.1f8a962fa9` |
| Label | `Eustachian tube` |
| Path | `data/habitats/host_associated/eustachian_tube.yaml` |
| Stable slug | `eustachian_tube` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Source | `GOLD` |
| Source ID | `gold.ecosystem:6851` |
| Source path | `Host-associated > Mammals > Auditory/Hearing system > Middle ear > Eustachian tube` |

The record is generated from committed inputs. `data/habitats/PATHS.tsv:1517`
pins `habitatmech:GOLD.1f8a962fa9` to `eustachian_tube`, and future grounding
or hierarchy curation should update maintained inputs and regenerate the YAML
rather than hand-editing this target.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/eustachian_tube.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/eustachian_tube.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, and 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 expected records, 3206 found on disk, 0 missing, 0 extra, and 0 differing. |
| `just worklist --status all --out /tmp/habitatmech-eustachian-tube-worklist.tsv` | Passed; wrote 953 ungrounded rows. The target is `NARROW`, not `UNGROUNDED`, and therefore is not a ranked worklist row. |
| `just report --out /tmp/habitatmech-eustachian-tube-report.tsv` | Passed; the target appears at line 1517 as `NARROW`, `SEEDED`, GOLD-only, one source, zero assertions, two parents, zero environmental parameters, zero characteristic taxa, and zero causal graphs. |

No target-specific causal overlay exists, so there was no narrower
`just validate-causal curation/causal_graphs/<slug>.yaml` command to run.

## Identity and Grounding

The generated source identity is exact. `data/raw/gold_ecosystem_paths.tsv:1986`
has the canonical row
`Host-associated > Mammals > Auditory/Hearing system > Middle ear > Eustachian tube`,
with leaf label `Eustachian tube`, depth 5, one GOLD ecosystem node ID, zero
organism assertions, zero study assertions, zero biosample assertions, zero
total assertions, and source ID `gold.ecosystem:6851`.

The bare `Eustachian tube` label is not unique in GOLD. GOLD also has a
distinct
`Host-associated > Mammals: Human > Auditory/Hearing system > Middle ear > Eustachian tube`
concept at `data/raw/gold_ecosystem_paths.tsv:2151`; that zero-assertion
sibling is generated as `habitatmech:GOLD.2127bae21d` at
`data/habitats/host_associated/eustachian_tube__a8583033.yaml`. The Mammals
target and the Mammals: Human sibling therefore need source-concept-specific
review.

The generated `UBERON:0002393` parent is the seeder's ambiguous-leaf fallback,
not a reviewed final identity decision. The vendored slice labels
`UBERON:0002393` as `pharyngotympanic tube`, defines it as the organ cavity
that connects the middle-ear cavity to the pharynx, and includes
`eustachian tube` as a synonym. Two equal-depth GOLD paths end in
`Eustachian tube`, so `seed.py` leaves no source concept claiming the ontology
term and emits both paths as minted `NARROW` children.

The GOLD source-path parent is supported. `data/habitats/PATHS.tsv:1672` maps
`habitatmech:GOLD.33c4a7e711` to `middle_ear__4109a919`, and the generated
parent record is the exact `Host-associated > Mammals > Auditory/Hearing
system > Middle ear` GOLD path. That parent was reviewed in
`reports/yaml_record_review/20261001T093910Z-middle_ear__4109a919.md`; it
still needs item-level curation, but it is the correct Mammals branch parent
for this Mammals `Eustachian tube` child.

## Evidence

The target has no authored definition, synonyms, xrefs, environmental
parameters, characteristic taxa, record-level evidence, causal graphs,
discussions, or datasets. There are no claim-level citations to audit.

| Claim | Nearest maintained support | Review |
|---|---|---|
| The source attestation preserves the GOLD node ID, leaf label, and full source path. | `data/raw/gold_ecosystem_paths.tsv:1986` | Supported exactly. |
| The `skos:narrowMatch` predicate and `UBERON:0002393` parent explain the current generated fallback. | `data/raw/ontology_terms.tsv:13156` labels `UBERON:0002393` as `pharyngotympanic tube` with `eustachian tube` as a synonym, and `data/raw/gold_ecosystem_paths.tsv` has equal-depth Mammals and Mammals: Human `Eustachian tube` rows. | Major finding: the fallback is unreviewed and should not be endorsed until an item-level decision decides whether the Mammals target claims `UBERON:0002393` exactly. |
| The `habitatmech:GOLD.33c4a7e711` parent is the immediate GOLD source-path parent. | `data/raw/gold_ecosystem_paths.tsv:1984`, `data/raw/gold_ecosystem_paths.tsv:1986`, `data/habitats/PATHS.tsv:1672`, and `data/habitats/host_associated/middle_ear__4109a919.yaml` | Supported. |
| No GOLD `assertion_count` should be emitted. | The exact raw path row reports `organism_count`, `study_count`, `biosample_count`, and `total_assertions` as zero, and exact full-path/source-ID searches found no row in `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, or `data/raw/gold_studies.tsv`. | Supported. |
| The rendered page mirrors the generated YAML. | `pages/habitats/eustachian-tube-habitatmech-gold-1f8a962fa9.html` | Supported; the page shows the same ID, label, `HOST_ASSOCIATED` category, `NARROW` grounding, `SEEDED` mapping, GOLD source path, missing assertion count, and two broader habitats. |

Ignored/hidden-inclusive exact searches found no target-specific
`curation/decisions.tsv` row, authored term request, causal graph overlay,
append-only history record, deep-research report, or prior exact YAML review
for `habitatmech:GOLD.1f8a962fa9`, `gold.ecosystem:6851`, or
`eustachian_tube`.

## Completeness

The generated record is complete for the maintained inputs currently
available, but not for item-level HabitatMech curation.

- It has the expected GOLD source attestation, source path, `skos:narrowMatch`
  predicate, immediate source-path parent, and generic UBERON anatomy parent.
- Empty `definition`, `synonyms`, `environmental_parameters`,
  `characteristic_taxa`, `evidence`, `causal_graphs`, `discussions`, and
  `datasets` fields agree with the absence of maintained target-specific
  curation rows or raw side-table support.
- `mapping_status` correctly remains `SEEDED`: no item-level decision has
  reviewed this source concept.

The substantive gap is the unresolved same-label sibling pair. Existing
`Nails` and `Seminal glands` curation demonstrates that equal GOLD depth does
not settle a Mammals/Mammals: Human anatomy tie on its own; an item-level row
must decide whether this Mammals `Eustachian tube` path should claim
`UBERON:0002393` or should document a reason to stay minted and narrower.

## Findings

| Severity | Finding | Owner |
|---|---|---|
| Major | `habitatmech:GOLD.1f8a962fa9` is still an unreviewed ambiguous-leaf fallback. The live record is `NARROW` because GOLD has equal-depth Mammals and Mammals: Human `Eustachian tube` paths and the seeder deliberately mints tied synonym matches as `NARROW` children instead of choosing a claimant. Existing item-level sibling-path decisions for `Nails` and `Seminal glands` resolved the same Mammals/Mammals: Human anatomy shape by grounding the broader Mammals source to the unqualified UBERON term and keeping the Human sibling as minted/narrower. | Add an item-level row for `habitatmech:GOLD.1f8a962fa9` to `curation/decisions.tsv` that decides whether the Mammals `Eustachian tube` source should `GROUND` to `UBERON:0002393` or stay minted with `UBERON:0002393` as a parent, then regenerate. Review the Mammals: Human sibling separately before changing `habitatmech:GOLD.2127bae21d`. |

## Recommended Edits

1. In `curation/decisions.tsv`, add item-level review for
   `habitatmech:GOLD.1f8a962fa9` that decides whether this broader Mammals
   `Eustachian tube` source should claim `UBERON:0002393` exactly, following
   the reviewed `Nails`/`Seminal glands` pattern, or should stay minted with
   `UBERON:0002393` only as a parent.
2. Independently review `habitatmech:GOLD.2127bae21d`, the Mammals: Human
   `Eustachian tube` sibling. If the Mammals source claims `UBERON:0002393`,
   the likely companion decision is a `GROUND_AS_PARENT` row that keeps the
   Human sibling source-specific and narrower.

## Follow-up Checks

After item-level curation, run:

1. `just seed`
2. `just seed-canary habitatmech:GOLD.1f8a962fa9`
3. `just render`
4. `just validate data/habitats/host_associated/eustachian_tube.yaml`
5. `just validate-strict data/habitats/host_associated/eustachian_tube.yaml`
6. `just validate-causal-all`
7. `just validate-history`
8. `just term-requests-check`
9. `just verify-corpus --max-diffs 1`
10. `just render-check`
11. `git diff --check`

## Additional Notes

- Exact ignored/hidden-inclusive searches covered `curation`, `history`,
  `research`, `reports/yaml_record_review`, `data/raw`,
  `data/habitats/PATHS.tsv`, `data/habitats/host_associated`, and
  `pages/habitats`. No prior exact review report existed before this report
  was added; `find reports/yaml_record_review -maxdepth 1 -type f -iname
  '*eustachian*'` also found no older Eustachian-tube report.
- The exact target source path/source ID search under the GOLD raw tables
  found only the `gold_ecosystem_paths.tsv` row and no direct GOLD biosample,
  study, or triad side-table row.
- iModulonDB structured source checks were not applicable because the record
  names a GOLD anatomical habitat path and no bacterial strain, gene, locus
  tag, regulator, pathway, stress-response term, or transcriptomics dataset.
