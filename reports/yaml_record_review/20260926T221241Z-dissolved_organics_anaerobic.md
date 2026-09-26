# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/dissolved_organics_anaerobic.yaml
- Started UTC: 2026-09-26T22:12:41Z
- Finished UTC: 2026-09-26T22:13:43Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.bb0eb00ccb` |
| Label | `anaerobic wastewater treatment reactor` |
| Category | `ENGINEERED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `REVIEWED` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `curation/decisions.tsv`, `curation/term_requests.tsv`, and the slug lock in `data/habitats/PATHS.tsv`; future edits to the definition or parentage belong in `curation/term_requests.tsv`. |

The target is a generated GOLD-only record for the reviewed GOLD source path
`Engineered > Wastewater > Nutrient removal > Dissolved organics (anaerobic)`.
The corpus keeps a minted HabitatMech identifier because no vendored ontology
term exactly names this anaerobic wastewater-treatment subunit, replaces the
loose GOLD source-path parent with `ENVO:00002124` `anaerobic bioreactor`, and
uses a term request to supply the reviewed label, definition, and source-label
synonym.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/habitats/engineered/dissolved_organics_anaerobic.yaml` | Pass: LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/dissolved_organics_anaerobic.yaml` | Pass: scanned 1 file with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| `just validate-history history/mappings/dissolved_organics_anaerobic/2026-09-09T003601Z-claude-code-869023.yaml` | Pass: the target history record is valid against `src/habitatmech/schema/history.yaml`. |
| `just validate-causal-all` | Pass: validated 32 causal-graph curation files with 32 graphs. |
| `just verify-corpus` | Pass: expected 3,206 records, found 3,206 on disk, and the corpus reproduces exactly from `data/raw/`. |
| `just term-requests-check` | Pass: the term-request table is current with 109 terms. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist.tsv` | Pass: reported 953 ungrounded records, 1,810 decisions on file, and wrote 953 rows. The target follows the previous `Wilt` row in the current worklist. |
| `just report` | Pass: completed the corpus report for 3,206 records and 953 `UNGROUNDED` records. |
| Reference validator | Not applicable: this generated record has no record-level `evidence`, `characteristic_taxa`, `causal_graphs`, `discussions`, or `datasets` with citation-bearing `EvidenceItem` references. |
| `git diff --check` | Pass. |

## Identity and Grounding

The generated identifier, source label, source path, source count, and category
agree with the GOLD inventory. `data/raw/gold_ecosystem_paths.tsv:705` has the
canonical path `Engineered > Wastewater > Nutrient removal > Dissolved organics
(anaerobic)`, `leaf_label` `Dissolved organics (anaerobic)`, depth `4`, two
collapsed GOLD node IDs (`gold.ecosystem:3830|gold.ecosystem:4260`), three
organism assertions, and `total_assertions` `3`. `data/habitats/PATHS.tsv:2660`
locks `habitatmech:GOLD.bb0eb00ccb` to the stable
`dissolved_organics_anaerobic` filename stem.

The item-level grounding decision at `curation/decisions.tsv:1626` correctly
rejects the stale lexical match to `PATO:0001456` `anaerobic` and confirms that
the source concept is a real habitat with no exact vendored term. The later
term request at `curation/term_requests.tsv:68` reviewed the same source path
more specifically, defined the minted class as an `anaerobic wastewater
treatment reactor`, and chose `ENVO:00002124` `anaerobic bioreactor` as a
strict broader parent.

The vendored slice supports that broader parent. `data/raw/ontology_terms.tsv`
labels `ENVO:00002124` as `anaerobic bioreactor`, and
`data/raw/ontology_subclass_edges.tsv` places it directly under
`ENVO:00002123` `bioreactor` with anaerobic dechlorinating, thermophilic
anaerobic methanogenic, and anaerobic sludge blanket reactors as narrower
descendants. The target record is narrower than generic anaerobic bioreactors
because it commits to wastewater treatment and dissolved-organic removal, and
it is broader than `ENVO:00002213` `anaerobic sludge blanket reactor` because
the source path does not select that single reactor geometry.

The generated `REVIEWED` status is supported: the only contributing source
concept has an item-level decision, the generated history carries that decision
and the later definition event, and the emitted `parent_habitats` list follows
the term request's `REPLACE` parent mode rather than inheriting the loose GOLD
`Nutrient removal` context as a strict `is-a` parent.

## Evidence

| Claim | Nearest maintained support | Review |
| --- | --- | --- |
| GOLD contributes `source_id: gold.ecosystem:3830`, source label `Dissolved organics (anaerobic)`, and the exact source path. | `data/raw/gold_ecosystem_paths.tsv:705` | Supported. The raw row has two GOLD node IDs and the seeder emits the first with a duplicate-node note. |
| The source contributes three organism-level assertions. | `data/raw/gold_ecosystem_paths.tsv:705` | Supported. The row has `organism_count=3` and `total_assertions=3`, and the generated record records that as `assertion_count: 3` with `assertion_unit: ORGANISM`. |
| The record should keep a minted identifier instead of grounding exactly to an ontology class. | `curation/decisions.tsv:1626`; `curation/term_requests.tsv:68`; vendored ENVO rows for `ENVO:00002124`, `ENVO:00002211`, and `ENVO:00002213` | Supported. The inspected broader and narrower reactor terms do not exactly name a generic anaerobic wastewater-treatment reactor. |
| `anaerobic wastewater treatment reactor` is a defensible HabitatMech label for the GOLD leaf `Dissolved organics (anaerobic)`. | `research/habitats/engineered/dissolved-organics-anaerobic-habitatmech-gold-bb0eb00ccb-deep-research-claude_code.md`; `curation/term_requests.tsv:68` | Supported. The source path, aerobic sibling, anaerobic activated-sludge child, and surrounding GOLD wastewater branches support reading the terse source label as a secondary-treatment reactor context rather than a dissolved-organic analyte. |
| The definition should say this habitat removes dissolved organic matter from a wastewater stream under anaerobic wastewater-engineering conditions. | `research/habitats/engineered/dissolved-organics-anaerobic-habitatmech-gold-bb0eb00ccb-deep-research-claude_code.md`; `curation/term_requests.tsv:68` | Supported. The generated definition keeps the reactor, wastewater-stream, dissolved-organic removal, and oxygen/nitrate exclusion claims from the report while avoiding its optional methanogenesis language. |
| The GOLD `Nutrient removal` source parent should not be emitted as a strict `parent_habitats` edge. | `curation/term_requests.tsv:68` | Supported. The term-request note documents `parent_mode=REPLACE` because GOLD's bucket groups secondary biological treatment branches loosely, while dissolved organic carbon removal is not nitrogen or phosphorus removal. |

No unsupported, over-scoped, or internally inconsistent target claims were
found. The review did not treat the committed deep-research report as
independent evidence for generated fields; it was used as the documented
curation rationale behind the maintained `curation/term_requests.tsv` row.

## Completeness

The generated record contains the required reviewed fields for the current
maintained inputs: minted identifier, reviewed label and definition, GOLD source
label synonym, strict authored parent, one GOLD source attestation, one
item-level grounding event, one seed event, one definition event, and the slug
lock that preserves the original source-derived filename.

Optional `characteristic_taxa`, `environmental_parameters`, record-level
`evidence`, `causal_graphs`, `discussions`, and `datasets` are correctly absent.
The GOLD source row is an intermediate path with three organism assertions and
no target-specific curator-authored causal overlay. The committed definition
research explicitly warned not to promote reactor-community taxa or performance
details into the habitat definition, and the generated record follows that
constraint.

Exact ignored/hidden-inclusive searches for `habitatmech:GOLD.bb0eb00ccb`,
`Dissolved organics (anaerobic)`, `anaerobic wastewater treatment reactor`,
`Engineered > Wastewater > Nutrient removal > Dissolved organics (anaerobic)`,
`ENVO:00002124`, `ENVO:00002213`, and `dissolved_organics_anaerobic` covered
the maintained and generated roots relevant to this record: `data/raw`,
`data/habitats`, `curation`, `history`, `research`, and `reports`. They found
the cited raw GOLD rows, curation rows, term-request export, history record,
slug lock, generated YAML, research report, and non-target mentions in prior
reviews; they found no target-specific maintained causal overlay that would
need separate edge-level review.

## Findings

None found.

## Recommended Edits

None found.

## Follow-up Checks

No target curation is required. If future work changes the term request or the
decision row, rerun:

- `just seed`
- `just seed-canary habitatmech:GOLD.bb0eb00ccb`
- `just term-requests-check`
- `just validate data/habitats/engineered/dissolved_organics_anaerobic.yaml`
- `just validate-strict data/habitats/engineered/dissolved_organics_anaerobic.yaml`
- `just verify-corpus`
- `just report`

## Additional Notes

- The previously reviewed `data/habitats/engineered/activated_sludge__13f30253.yaml`
  record remains the child-specific problem downstream of this source path:
  activated sludge is material, while this parent is now curated as a reactor.
  That false child edge does not make the reviewed parent record inconsistent.
- The committed deep-research report lists failed provider attempts before a
  successful Claude Code report in `reports/habitat_research_manifest.tsv`.
  Those failed attempts are provenance for the research batch, not source
  support for the generated HabitatRecord.
