# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/coastal_lagoon.yaml`
- Started UTC: 2026-09-27T02:50:00Z
- Finished UTC: 2026-09-27T03:18:17Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.c9a99e0db8` |
| Label | `Coastal lagoon` |
| Class | `HabitatRecord` |
| Category | `AQUATIC` |
| Generated or maintained | Generated from `data/raw/gold_ecosystem_paths.tsv`, `curation/decisions.tsv`, and `data/habitats/PATHS.tsv`; do not hand-edit |
| Current grounding | `UNGROUNDED` |
| Current mapping | `SEEDED` |

The target resolves exactly one YAML file and one GOLD source path:
`Environmental > Aquatic > Marine > Coastal lagoon`. `data/habitats/PATHS.tsv`
maps `habitatmech:GOLD.c9a99e0db8` to the stable corpus slug
`coastal_lagoon`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/coastal_lagoon.yaml` | Pass: LinkML reported `No issues found`. |
| `just validate-all data/habitats/aquatic/coastal_lagoon.yaml` | Pass: 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-strict data/habitats/aquatic/coastal_lagoon.yaml --quiet` | Pass: 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal-all` | Pass: 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Pass: committed term-request table is current with 109 terms. |
| `just validate-history` | Pass: 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist.tsv` | Pass: regenerated a 953-row ungrounded worklist outside the repository. |
| `just verify-corpus --max-diffs 1` | Pass: 3,206 expected records, 3,206 found, 0 missing, 0 extra, 0 differing. |
| `just report` | Pass: completed the corpus diagnostic report without modifying tracked files. |

No documented validator was skipped.

## Identity and Grounding

The generated record faithfully copies the unreviewed GOLD concept:

- `data/raw/gold_ecosystem_paths.tsv` has the exact collapsed path on line 579,
  with leaf label `Coastal lagoon`, depth 4, two node IDs
  (`gold.ecosystem:7873|gold.ecosystem:7874`), seven organism assertions, and
  seven total bulk assertions.
- `source_attestations[0]` carries `source: GOLD`,
  `source_id: gold.ecosystem:7873`, `source_label: Coastal lagoon`, the exact
  path, `assertion_count: 7`, `assertion_unit: ORGANISM`, and the generated
  note that two GOLD ecosystem node IDs share the path.
- The raw GOLD API inventory has 76 biosamples for the same path on
  `gold.ecosystem:7874`, and `data/raw/gold_studies.tsv` lists the exact path
  in studies `Gs0159305`, `Gs0159327`, and `Gs0160759`.
- Two exact GOLD child paths are already minted with
  `habitatmech:GOLD.c9a99e0db8` as their source-path parent:
  `Environmental > Aquatic > Marine > Coastal lagoon > Sediment` and
  `Environmental > Aquatic > Marine > Coastal lagoon > Microbial mat`.

The current inherited parent is true but coarse. The immediate GOLD source
parent, `Environmental > Aquatic > Marine`, resolves to `ENVO:00001999`
`marine water body`, so `parent_habitats: [ENVO:00001999]` records only the
generated path context and not a curator-reviewed coastal-lagoon identity.

The 2026-08-12 `curation/decisions.tsv` row is only a class-level
`CONFIRM_UNGROUNDED` sweep. That row states that no vendored term matched this
label by a label/synonym search route and that the concept's habitathood was not
assessed.

The vendored ontology slice contains two relevant nearby habitat terms:

- `ENVO:00000038` `lagoon` is broader than `Coastal lagoon` and is an exact
  match candidate to evaluate during item review.
- `ENVO:02000049` `coastal water body` is a subclass of `ENVO:00001999`, but
  HabitatMech only sees it in GOLD MIxS triads for the sibling
  `Environmental > Aquatic > Marine > Coastal` path, not for the exact
  `Coastal lagoon` path.

## Evidence

The record has no curator-authored `definition`, record-level `evidence`,
`environmental_parameters`, `characteristic_taxa`, `causal_graphs`,
`discussions`, or `datasets`.

The GOLD source attestation is supported by the collapsed GOLD inventory row.
It is not a definition or ontology-grounding decision by itself. The additional
GOLD API biosample and study rows show that the exact path is used in submitted
GOLD records, and the exact child paths show GOLD treats `Coastal lagoon` as an
interior source-path node, but none of those rows decide whether HabitatMech
should ground the record exactly to `ENVO:00000038`, keep a minted narrower
record under `ENVO:00000038`, or request a new coastal-lagoon term.

Hidden- and ignored-file-inclusive exact searches found no row for the exact
`Environmental > Aquatic > Marine > Coastal lagoon` path in
`data/raw/gold_path_triads.tsv`. No MIxS triad has been dropped from the
generated YAML for this exact path.

## Completeness

The empty optional slots are correct for the current maintained inputs. Exact
hidden- and ignored-file-inclusive searches of `reports/yaml_record_review`,
`research/habitats`, `curation/causal_graphs`, `history`,
`curation/term_requests.tsv`, `curation/term_requests_excluded.tsv`,
`curation/external_xrefs.tsv`, `conf/id_label_targets.yaml`, and
`reports/habitat_research_manifest.tsv` found no prior target-specific review,
research report, causal overlay, curation history entry, term request,
term-request exclusion, external xref, or label target for
`habitatmech:GOLD.c9a99e0db8`, `GOLD.c9a99e0db8`, `gold.ecosystem:7873`,
`gold.ecosystem:7874`, `gold.ecosystem:7875`, `gold.ecosystem:7945`,
`coastal_lagoon`, `Coastal lagoon`, or the exact GOLD source path.

The record is not complete as a reviewed HabitatMech habitat because it still
depends on a class-depth absence sweep. Item-level curation needs to decide the
relationship to vendored `ENVO:00000038` `lagoon`, choose whether
`Coastal lagoon` needs a HabitatMech-native definition or an upstream term
request, and record any retained near misses so the generated record moves from
`SEEDED` to `REVIEWED`.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-COASTAL-LAGOON-001 | Major | `Coastal lagoon` is still represented by a class-sweep `CONFIRM_UNGROUNDED` decision even though the exact GOLD path has two source node IDs, seven organism assertions, 76 GOLD API biosamples, three GOLD studies, and two exact GOLD child paths. The generated `ENVO:00001999` parent is a true but coarse source-path parent; no item-level row records whether the GOLD concept should be treated as exactly `ENVO:00000038` `lagoon`, narrower than `ENVO:00000038`, or unsupported pending a new term request. | `curation/decisions.tsv` |

No blocker findings.

No minor findings.

## Recommended Edits

1. Replace the `CLASS`-depth row for `habitatmech:GOLD.c9a99e0db8` in
   `curation/decisions.tsv` with an `ITEM`-depth decision after inspecting the
   exact GOLD concept, `ENVO:00000038` `lagoon`, `ENVO:02000049`
   `coastal water body`, the exact GOLD biosample and study inventory, and the
   two child paths under `Coastal lagoon`.
2. If item review confirms GOLD's concept is a narrower kind of lagoon, add a
   maintained `curation/term_requests.tsv` row for
   `habitatmech:GOLD.c9a99e0db8` with parent `ENVO:00000038`, a definition that
   differentiates coastal lagoons from generic lagoons, and `parent_mode=ADD`
   so the generated record can keep the true source-derived
   `ENVO:00001999` parent while gaining the tighter lagoon genus.
3. Run the dry-run `just seed`, regenerate the target with
   `just seed-canary habitatmech:GOLD.c9a99e0db8 --force`, and inspect the
   generated target before any wider `just seed-apply --force` run.

## Follow-up Checks

- `just validate data/habitats/aquatic/coastal_lagoon.yaml`
- `just seed-canary habitatmech:GOLD.c9a99e0db8 --force`
- `just validate-strict data/habitats/aquatic/coastal_lagoon.yaml --quiet`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `git diff --check`

After regeneration, re-read `data/habitats/aquatic/coastal_lagoon.yaml` and
confirm that the record is item-reviewed, preserves `ENVO:00001999`, has an
explicit reviewed relationship to `ENVO:00000038`, and records curation-history
events for the item-level decision and any term request.

## Additional Notes

This was a read-only YAML review. It did not edit generated habitat YAML, append
curation history, promote review status, create an issue, or run paid
definition research.

The generated HTML page was not used as evidence; all assertions above were
traced to maintained TSV inputs, the vendored ontology slice, or the generated
target YAML.
