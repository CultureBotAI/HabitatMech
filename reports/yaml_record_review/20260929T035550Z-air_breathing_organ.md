# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/air_breathing_organ.yaml`
- Started UTC: 2026-09-29T03:49:11Z
- Finished UTC: 2026-09-29T03:55:50Z
- Verdict: needs curation

## Target

`data/habitats/host_associated/air_breathing_organ.yaml` is a generated
`HOST_ASSOCIATED` GOLD record:

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.a7d8777e98` |
| Label | `Air-breathing organ` |
| Grounding | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Parent | `habitatmech:GOLD.c2a1b0b268` |
| Source | `GOLD`, `gold.ecosystem:7536`, `Host-associated > Fish > Digestive system > Intestine: Anterior > Air-breathing organ` |
| Definition | None |
| Evidence, environmental parameters, characteristic taxa, causal graph | None |

The source path is pinned in `data/habitats/PATHS.tsv` as
`habitatmech:GOLD.a7d8777e98 -> air_breathing_organ`; the immediate GOLD
parent is pinned separately as `habitatmech:GOLD.c2a1b0b268 ->
intestine_anterior`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/air_breathing_organ.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/air_breathing_organ.yaml` | Passed; 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the 109-term generated request table is current. |
| `just verify-corpus` | Passed; 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just report --out /tmp/habitatmech-report-air-breathing-organ.tsv` | Passed; wrote `/tmp/habitatmech-report-air-breathing-organ.tsv`. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist-air-breathing-organ.tsv` | Passed; wrote 953 ungrounded rows to `/tmp/habitatmech-worklist-air-breathing-organ.tsv`. |

`/tmp/habitatmech-report-air-breathing-organ.tsv` confirms the generated record
is GOLD-only, `UNGROUNDED`, `SEEDED`, backed by one source attestation, and has
zero generated taxa, parameters, or causal graph. The all-status worklist ranks
the target at row 380 and reports the candidate `UBERON:0000171=breathing
organ`.

## Identity and Grounding

The generated identity is a content-hashed GOLD source concept for the depth-5
path `Host-associated > Fish > Digestive system > Intestine: Anterior >
Air-breathing organ`. In the committed GOLD inventory, that path has one GOLD
node, zero organism assertions, zero studies, zero biosamples, and zero total
assertions:

| Raw row | Path | Depth | GOLD node count | Organism count | Study count | Biosample count | Total assertions | GOLD node IDs |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `data/raw/gold_ecosystem_paths.tsv:1929` | `Host-associated > Fish > Digestive system > Intestine: Anterior > Air-breathing organ` | 5 | 1 | 0 | 0 | 0 | 0 | `gold.ecosystem:7536` |

The current curation row is only a class-level decision:

| Decision row | Decision | Review depth | Note scope |
|---|---|---|---|
| `curation/decisions.tsv:959` | `CONFIRM_UNGROUNDED` | `CLASS` | Lexical no-hit sweep; explicitly did not assess whether the source concept is a habitat. |

That is not enough to endorse the record. `docs/HARMONIZATION.md` states that
`CLASS` decisions do not promote a record to `REVIEWED`, and this target is
still `mapping_status: SEEDED`.

The vendored ontology slice contains `UBERON:0000171` / `respiration organ`,
defined as an organ that functions in gaseous exchange between an organism and
its environment, with exact synonyms including `breathing organ`, `gas exchange
organ`, and `respiratory organ` in `data/raw/ontology_terms.tsv:12920`.
`UBERON:0000171` is broader than this fish-specific GOLD leaf and is therefore
the natural parent candidate to verify in an item-level decision.

The generated GOLD path parent is plausible and separately reviewed. The
parent concept `habitatmech:GOLD.c2a1b0b268`, `Intestine: Anterior`, has an
item-level `GROUND_AS_PARENT` row at `curation/decisions.tsv:1089` that keeps
that minted identity narrow under `UBERON:0000160` / `intestine`.

## Evidence

The committed raw GOLD path is the only source inventory row for
`gold.ecosystem:7536`; an exact hidden/ignored-inclusive search for
`gold.ecosystem:7536`, `habitatmech:GOLD.a7d8777e98`, and `Air-breathing organ`
across `data/raw/*.tsv` and `data/raw/*.yaml` found only
`data/raw/gold_ecosystem_paths.tsv:1929`.

No GOLD biosample, MIxS triad, or study row is committed for this one-node,
zero-assertion leaf, so there is no auxiliary source metadata to audit. There
are also no generated taxa, environmental parameters, evidence objects, or
causal edges on the record.

iModulonDB was not applicable: the target is a GOLD habitat leaf, not a named
gene, locus, UniProt accession, regulator, iModulon, pathway, stress-response
record, or transcriptomics dataset.

## Completeness

The record is structurally complete for a generated zero-assertion GOLD leaf:
it preserves its upstream source path and its source-path parent, and it does
not invent taxa, physicochemical parameters, definition text, or mechanism
evidence.

Exact hidden/ignored-inclusive searches found no target-specific append-only
history record, research report, causal overlay, authored term request, label
correspondence residual, or prior exact YAML-record review for
`habitatmech:GOLD.a7d8777e98`, `gold.ecosystem:7536`,
`Air-breathing organ`, or `air_breathing_organ` under `curation/`,
`history/`, `research/habitats/`, `reports/yaml_record_review/`, `conf/`, and
the committed raw inventories. A broader ignored-inclusive filename search for
`*air*` under `curation/causal_graphs`, `history`, `research/habitats`, and
`reports/yaml_record_review` found only different reviewed or researched
records: indoor air, outdoor air, air sacs, air scrubber, and
oral-cavity/airways artifacts.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `habitatmech:GOLD.a7d8777e98` has not received item-level grounding review and is missing the evident broader UBERON parent. | The only curation row is a `CLASS` `CONFIRM_UNGROUNDED` at `curation/decisions.tsv:959`, so the record remains `mapping_status: SEEDED`. `just worklist` proposes `UBERON:0000171=breathing organ`, and the vendored slice defines `UBERON:0000171` as `respiration organ` with exact synonyms including `breathing organ` and `respiratory organ`, making it a stronger broader parent candidate than the current no-parent class-level decision expresses. | `curation/decisions.tsv` |

## Recommended Edits

1. Replace the class-level row for `habitatmech:GOLD.a7d8777e98` in
   `curation/decisions.tsv` with an item-level decision after verifying the
   exact GOLD path and ontology target. The expected shape is
   `GROUND_AS_PARENT`, `object_id: UBERON:0000171`, `object_label:
   respiration organ`, `grounding_status: NARROW`, `review_depth: ITEM`, with
   notes explaining that an air-breathing organ is a fish-specific respiratory
   organ under GOLD's anterior-intestine branch.
2. Rerun `just seed`, canary `habitatmech:GOLD.a7d8777e98`, and apply the
   generated corpus update. The regenerated record should stay minted, become
   `NARROW`, gain `UBERON:0000171` in `parent_habitats`, and become
   `REVIEWED`.
3. If the curator wants a natural-language definition for the fish-specific
   concept, add a curated `term_requests.tsv` row instead of hand-editing
   `data/habitats/host_associated/air_breathing_organ.yaml`.

## Follow-up Checks

| Follow-up | Purpose |
|---|---|
| `just validate data/habitats/host_associated/air_breathing_organ.yaml` | Validate the regenerated target shape. |
| `just validate-strict data/habitats/host_associated/air_breathing_organ.yaml` | Confirm the regenerated target is still closed-schema valid. |
| `just verify-corpus` | Prove the maintained `curation/decisions.tsv` row reproduces the generated habitat record. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist-after-air-breathing-organ.tsv` | Confirm `habitatmech:GOLD.a7d8777e98` no longer appears in the ungrounded worklist once the item-level decision lands. |
| `just report --out /tmp/habitatmech-report-after-air-breathing-organ.tsv` | Confirm corpus summaries move this record out of the class-level sweep and count it as individually reviewed. |
| `just term-requests-check` | Run only if a definition term request is added. |

## Additional Notes

This review found no blocker identity problem. The current generated record is
a faithful, reproducible projection of one raw GOLD path row. The issue is that
the existing `CLASS` decision is deliberately shallow and has not captured an
available broader UBERON parent.

The GOLD row has no committed study, biosample, triad, or organism evidence,
so this review did not launch paid deep research or inspect external
literature. A later curation pass can decide whether this zero-assertion GOLD
leaf is worth a full definition and term request.
