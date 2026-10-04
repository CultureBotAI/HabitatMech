# YAML Record Review: Oil sands pit lake

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/oil_sands_pit_lake.yaml`
- Started UTC: 2026-10-04T22:38:19Z
- Finished UTC: 2026-10-04T22:41:13Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.e13608a63a, Oil sands pit
lake, AQUATIC/UNGROUNDED/SEEDED. One source parent, one GOLD attestation
without count/unit or mapping predicate, a two-node note and two history
events are present. Definition, synonyms, xrefs, parameters, taxa, evidence,
graphs, discussions and datasets are absent. PATHS.tsv:2960 pins the stem.

The exact source is Environmental > Aquatic > Pit lake > Oil sands pit lake.
It denotes the qualified lake, not oil sands material, lake water, sediment,
the sibling Mine pit lake source or a particular named demonstration lake.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/oil_sands_pit_lake.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/oil_sands_pit_lake.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Fresh batch PASS: 1,179 canonical, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Fresh local batch run active in tests; lint, documentation and 14-inventory provenance passed. No terminal result claimed. |
| Source/reference checks | Whole target and contextual parent, actual resolution/full-field construction, all 14 raw tables, current typed ENVO/OLS, both GOLD node attempts, primary research and institutional source text, full rendered page and semantic comparisons. |

Actual construction reproduces all fields with one source concept and zero
reviewed sources. The previous PR #1419 main-push run was polled on its
existing handle and remains active; neither it nor this fresh run is counted
as terminal success. No SSSOM/KGX compatibility audit was performed.

## Identity and Grounding

Actual minting reproduces the record ID. The automatic gold_unmatched answer
is UNGROUNDED; CLASS CONFIRM_UNGROUNDED at curation/decisions.tsv:1246,
dated 2026-08-12, preserves it through
curated_confirm_ungrounded_from_gold_unmatched, reviewed=False. The note
explicitly says habitat meaning was not assessed. SEEDED, count omission,
absent predicate and class-level history are faithful, not false endorsement.

Current [ENVO:00000020 lake](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000020)
is active and supplies a broader waterbody genus for the explicit lake source.
No whole-label lexical match is not evidence that no supported ontology
relation exists. Preserve the oil-sands and pit qualifications rather than
adopting generic lake as exact identity.

Current ENVO:00000377 artificial lake requires purposeful construction, while
ENVO:00000025 reservoir adds water-storage purpose. The inspected research
describes a deliberately engineered oil-sands lake, making artificial lake
a meaningful candidate to compare. That one example does not establish the
unavailable GOLD nodes' full scope or justify automatically treating every
source member as a reservoir. The verified generic lake genus is already usable.

ENVO:03600013 bituminous sand is a material, not the lake. ENVO:03600021
tailings pond is a tailings-storage construction; current typed ENVO does
not place it under pond because its contents need not be primarily water.
Neither a matching oil-sands synonym nor shared reclamation context makes
either term an exact whole-lake identity. Coal mine lake sediment is also
a material near miss with an unsupported coal restriction.

Ignored-inclusive committed-slice searches and a structured current official
OWL label/synonym scan for pit/quarry/mining/mine lake, oil sands and tailings
pond found these near misses, not an exact qualified-lake class. This is not
an exhaustive claim about all ontologies or every possible lexical variant.

The full parent pit_lake.yaml is habitatmech:GOLD.5b56a06a4c, also
UNGROUNDED/SEEDED. Actual parent resolution retains that identity and CLASS
decision. The child's narrower oil-sands lake meaning is consistent with
the source's Pit lake grouping; no false direct parent is diagnosed here.
Do not remove that valid grouping merely to add an ontology genus. The
parent's own broader edge is outside this child's finding.

## Evidence

Physical gold_ecosystem_paths.tsv:1578 gives depth four, two nodes
gold.ecosystem:7958 and 7959, with zero organism/study/biosample counters
and zero total assertions. Displaying the first node with a two-node note
is faithful. Zero organism assertions explain the absent count/unit; two
vocabulary nodes are not two samples or organisms.

Both current GOLD OLS node requests returned 404. The committed source
provenance is verified, but original contents were not recovered and retirement
is not established. The full exact-path scan of all 14 raw tables found no
target sample, triad, study, taxon, parameter or other-source contribution.
The parent's one organism and the separate sediment descendant are not
evidence to copy into this target.

The inspected [Mori et al. primary study](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2019.02435/full)
describes Base Mine Lake as an engineered oil-sands pit lake and samples its
water cap and underlying tailings separately. It supports a real microbial
lake habitat and the distinction between a lake and its sampled materials.
It does not identify GOLD 7958/7959 in the inspected passages or establish
that its taxa, depths, chemistry or proposed metabolisms characterize every
oil-sands pit lake. No such claims were transferred to the record.

The [Alberta Energy Regulator account](https://www.aer.ca/understanding-resource-development/resource-development-topics/tailings)
describes tailings ponds as engineered storage structures for tailings and
process-affected water. That supplies contextual contrast, not an identity
crosswalk. A second journal search result could not be opened and was not
used as claim support. The entire rendered page faithfully exposes the
class-level caveat, absent counts and source parent.

## Completeness

Ignored-inclusive identifier, exact path, label/stem and filename searches
covered curation, conf, history, research, reports, raw inventories, PATHS and
RETIRED. Only the maintained decision/path lock and raw source were located
for this target; a previous Mine pit lake review mentions it contextually,
not as its own reviewed target. No target definition, overlay, dedicated
research, session history, retirement or earlier individual review was found.

The consequential gap is an ITEM ontology-genus assessment. Optional empty
measurements, taxa and mechanisms are appropriate without exact source
evidence. A future authored definition belongs in curation/term_requests.tsv
after exact-term deduplication. iModulonDB is inapplicable to the current
record's absent gene/regulator/expression assertions.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | A real oil-sands-qualified lake remains CLASS/UNGROUNDED with no assessed ontology genus although lake is supported. | Existing ITEM follow-up at curation/decisions.tsv:1246; a supported novel definition, if needed, belongs in curation/term_requests.tsv. |

Counts: zero blockers, one major, zero minor. The source identity, parent,
count omission and honest unreviewed status are not additional defects.

## Recommended Edits

1. Replace the existing CLASS row with evidence-backed ITEM curation.
   Retain the qualified minted identity under verified lake unless a current
   exact term is established; compare artificial lake against actual source
   scope rather than force a reservoir or tailings-pond identity.
2. Keep the valid Pit lake parent, both node IDs, full path, absent count/unit
   and old history. A supported authored definition should use ADD for an
   additional true genus; no unsupported REPLACE or sibling merge is justified.
3. Resolve #1398's endpoint contract before adding a GROUND_AS_PARENT mapping,
   then append new history and regenerate through maintained inputs. The
   current predicate-free record is not itself a #1398 witness.

## Follow-up Checks

Dry seed and inspect `just seed-canary habitatmech:GOLD.e13608a63a --force`
before guarded full regeneration without partial prune. Require exact-source,
node/count, parent-retention and endpoint regressions; ordinary/strict,
products/history/provenance validation; exact reproduction and full QC.

Actual full-context addition of ENVO:00000020 adds a lake-genus line to
semantic text. Genuine map/site refresh under #1217 is needed for that
repair. The separate exploratory source-parent-removal probe is not a
recommendation to remove the valid parent. Preserve protected #1218/runtime
pins and inspect actual SSSOM/KGX before downstream compatibility claims.

## Additional Notes

All-state exact-key/label issue search returned related #1409. Its full body
covers Mine pit lake and Mine pit pond, not this oil-sands source; coordinate
the common genus-curation work without treating this source as already fixed.
Official typed ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated output, old report/history, paid research or
GitHub item changed during this individual review.
