# YAML Record Review: Mesopelagic/Twilight zone

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/mesopelagic_twilight_zone.yaml`
- Started UTC: 2026-10-04T14:51:58Z
- Finished UTC: 2026-10-04T14:57:43Z
- Verdict: pass with minor issues

## Target

Entire generated `HabitatRecord`: habitatmech:GOLD.168f298608,
Mesopelagic/Twilight zone, AQUATIC, UNGROUNDED and SEEDED. It has one parent,
one uncounted GOLD attestation, a class-sweep event and a seed event. No
definition, synonyms, taxa, parameters, citations, graphs, datasets,
discussions, xrefs or replacement links are emitted.

The actual mint function reproduces the identifier from
`Environmental > Aquatic > Marine > Pelagic zone > Mesopelagic/Twilight zone`.
The displayed source node is gold.ecosystem:7898; PATHS.tsv:1443 pins the
filename. This is not the already-reviewed Marine > Mesopelagic source
GOLD.76bc4edc73 that feeds ENVO:00000213.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/mesopelagic_twilight_zone.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/mesopelagic_twilight_zone.yaml` | PASS, one file, zero errors. |
| `just validate-products` | PASS: 1,179 canonical pairs, one synonym, five exceptions, 2,054 configured no-adapter skips. This does not validate a hypothetical new grounding. |
| `just worklist --status all --limit 5` | PASS, 953 ungrounded records and 1,810 decisions. |
| `just qc` | First attempt terminated before validation because sandbox access to uv's cache was denied. The authorized rerun is active in tests; lint, documentation and raw provenance passed. No terminal full-QC result yet. |
| Source/reference checks | Full target and candidate record read; structured exact-source scan across all 14 raw TSVs; official OLS/ENVO OWL and NOAA source text inspected. |

Full-corpus-only gates use the documented QC runner. Later terminal results
belong in the publication receipt rather than rewriting this observation time.

## Identity and Grounding

The source denotes a marine water-column habitat, not a sample artifact,
organism or process. Its current parent,
[ENVO:00000208 marine pelagic zone](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000208),
is active and broader than this depth/light band. This is a defensible GOLD
parent contribution; not every source-path edge is a false is-a relation.

`curation/decisions.tsv:222` is CONFIRM_UNGROUNDED at CLASS depth, dated
2026-08-12. Its explanation explicitly leaves habitat identity unassessed.
SEEDED therefore faithfully reflects the maintained decision, and the audit
is not ITEM-level evidence that every possible ontology candidate was rejected.

An existing candidate deserves explicit reconciliation:
[ENVO:00000213 marine mesopelagic zone](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000213).
The committed ontology slice at `ontology_terms.tsv:6803` and current typed
OWL agree on its thermal lower-bound definition and direct marine-aphotic-zone
parent. The entire existing generated record was read: it already combines
the separately keyed GOLD Marine > Mesopelagic path and PREGO under ITEM
decisions. Its four taxa and 34-organism assertion are not this source's data.

[NOAA's mesopelagic description](https://oceantoday.noaa.gov/fullmoon-mysteriesofthemesopelagic/)
explicitly uses mesopelagic and twilight for the roughly 200-1,000 m zone.
However, [NOAA's light-zone account](https://oceanservice.noaa.gov/facts/light_travel.html)
uses dysphotic for that interval and reserves aphotic for deeper water,
whereas ENVO:00000210 uses a photosynthesis-based threshold below 200 m.
These naming/boundary conventions are not interchangeable numeric limits.
The GOLD source's exact boundary convention has not been recovered, so the
review does not assert a proven exact merge or force a NARROW relation.

Current ENVO:01000036 oceanic mesopelagic zone biome and ENVO:01000043 neritic
mesopelagic zone biome have explicit offshore/shelf scopes and denote biomes.
Neither is an automatic replacement identity for a generic pelagic zone.

## Evidence

Physical CSV line locators account for multiline cells. The exact tree row,
`data/raw/gold_ecosystem_paths.tsv:1545`, has depth five, one node and zero
organism/study/biosample counts. The uncounted emitted GOLD attestation is
faithful to that tree snapshot, not evidence of an uninhabited zone.

The separately versioned bulk inventory at `gold_path_biosamples.tsv:625`
contains ten biosamples. Exact memberships in `gold_studies.tsv` are:

| Physical line | Study | Total source paths in that study |
| --- | --- | --- |
| 4429 | Gs0161463 | 2 |
| 4434 | Gs0161468 | 3 |
| 4456 | Gs0161492 | 5 |

These are cross-zone studies, not ten additional organism assertions or
three exclusively mesopelagic studies. The structured raw scan found no
exact-target triad, environmental-parameter or taxon row. A current OLS
lookup for w3id.org/gold.path/7898 returned 404; bounded GOLD-filtered
full-path and leaf searches returned zero hits. Accession web searches did
not recover relevant original GOLD study content; an unrelated accession-like
search hit was not treated as biological evidence. Snapshot provenance is
verified, but current original sample contents remain uninspected.

The already-reviewed marine mesopelagic report and #1285 were read as
context. That issue concerns its different source's whole-waterbody parent.
This target does not currently assert that parent, so it does not inherit
that finding merely because an eventual merge is being considered.

## Completeness

Ignored-inclusive ID, node, source-key, label and filename searches covered
curation, history, research, individual reports, PATHS and RETIRED. They
found the class decision, path lock, candidate decision and contextual
mentions, but no target ITEM decision, authored definition, causal overlay,
dedicated research, separate session history, retirement entry or earlier
individual target review. Nearby research and sibling depth-band reviews
are not independent evidence for this source's boundaries.

The unresolved candidate is a useful curation follow-up. Empty optional
mechanisms, measurements and taxa are not independent defects, and general
NOAA depth descriptions must not become universal measured parameters here.
iModulonDB is not applicable: no gene, regulator, pathway, expression dataset
or mechanism is asserted.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Minor | Grounding remains at a lexical class-sweep conclusion despite an existing marine mesopelagic candidate and independently supported twilight alias. An ITEM-level boundary/identity reconciliation is missing; exact equivalence is not yet established. | `curation/decisions.tsv:222`, keyed to GOLD.168f298608; source definitions/member evidence for the boundary decision. |

Counts: zero blockers, zero major, one minor. UNGROUNDED is conservative,
not a demonstrated wrong identity. The current pelagic parent, source
projection and SEEDED status are supported.

## Recommended Edits

1. Inspect original source definitions/member contexts and explicitly compare
   ENVO:00000213 before proposing a novel term. If equivalence is supported,
   use an ITEM GROUND decision and merge through the normal generator while
   preserving both GOLD paths and PREGO provenance. Otherwise document the
   bounded distinction in an ITEM decision and, if needed, an authored minted
   definition in `curation/term_requests.tsv`.
2. Preserve this source's zero tree-organism count and separate ten-biosample
   bulk cohort. Do not copy taxa or sum unlike units from the candidate record.
3. For actual curation, append history and inspect guarded regeneration. Do not
   edit YAML/pages or change every slashed depth-band label through one rule.

## Follow-up Checks

Require current candidate/source verification, ordinary and strict schema,
identifier-label correspondence, history/provenance, full corpus reproduction
and QC. If a merge is justified, inspect all merged attestations, statuses,
parent contributions and the old URL's generated retirement/redirect handling.
Coordinate the candidate record's separately tracked #1285 parent correction.

The rendered target page and actual semantic text currently contain the source
label, aquatic category and marine-pelagic parent but no definition. A merge
would retire a map identity and change semantic inputs; use the real governed
map/site rebuild and coordinate #1217. A status-only ITEM endorsement is not
itself a semantic-text change. Protected draft #1218 remains untouched.

## Additional Notes

GitHub all-state searches for mesopelagic and the exact source key found only
the other record's #1285 issue, not a target-specific grounding issue. Its
full body and empty comments were inspected. This report does not claim that
the current missing exact mapping is a broken reference or that every unknown
grounding is scientifically wrong.

Current official ENVO OWL was downloaded to a temporary evidence cache and
parsed by predicate; SHA-256
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No paid research, scientific edit, status promotion, curation event or
committed-history rewrite was performed.
