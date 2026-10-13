# YAML Record Review: Simulated rainfall

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/simulated_rainfall.yaml`
- Started UTC: 2026-10-06T01:39:07Z
- Finished UTC: 2026-10-06T01:45:20Z
- Verdict: needs curation; 0 blocker, 1 major, 0 minor findings.

## Target

The entire generated HabitatRecord was read: habitatmech:GOLD.452a98786f,
Simulated rainfall, AQUATIC, UNGROUNDED and SEEDED. It has one parent,
one GOLD attestation and two history events. Definition, synonyms, counts,
units, taxa, parameters, evidence, graphs and discussion are not emitted.
PATHS.tsv:1807 pins simulated_rainfall.

Exact source: Environmental > Aquatic > Freshwater > Simulated rainfall,
GOLD node 8074. Whether that vocabulary grouping denotes an experimental
procedure, supplied/sampled water or an experiment-associated environment
is unresolved. It must not be silently equated with natural rainwater or
the separate, already grounded runoff child.

## Validation

- `just validate data/habitats/aquatic/simulated_rainfall.yaml`: pass,
  no issues; `just validate-strict` for the same path: one file, zero errors.
- Actual build_corpus/build_document whole-document equality: pass;
  one source, zero reviewed sources, zero taxa and two history events.
- Actual source/parent resolution, all 14 raw TSVs with exact path/node
  handling, complete rendered page and full-context semantic probes checked.
- Fresh batch `just verify-corpus`: all 3,206 records reproduce exactly;
  fresh `just validate-history`: all 90 histories valid.
- Unchanged-input full-QC baseline
  [37398300879](https://github.com/CultureBotAI/HabitatMech/actions/runs/37398300879)
  passed 457 tests, three skips and two warnings, plus history, corpus,
  site and term-request gates. Main-push 37399007285 is now SUCCESS.
  These are reused full-CI results, not a new full local suite for this record.
- Required merge-group label validation passed; final-head label report
  37397546821 had zero flagged pairs. Configured no-adapter skips remain
  outside label coverage. Named ontology candidates were checked additionally.
- No standalone reference validator is exposed by justfile; no EvidenceItem
  or causal-edge citation occurs in this target.

## Identity and Grounding

Minting the exact path reproduces GOLD.452a98786f. The default route is
gold_unmatched. CLASS CONFIRM_UNGROUNDED at decisions.tsv:465 produces
curated_confirm_ungrounded_from_gold_unmatched, still UNGROUNDED and
unreviewed. Its note explicitly says habitat validity was not assessed.
The 2026-08-12 class decision and 2026-08-16 seed event are faithful.

Mapping-predicate omission follows the source-to-record contract at
habitatmech.yaml:317-322: this retained record is the source concept.
It is not another #1398 NARROW self-endpoint witness. SEEDED is honest
status disclosure, not a separate status bug.

The sole strict parent, ENVO:00002011 fresh water, is added independently
by seed.py:898-907. Parent source GOLD.ad12f0169a defaults to CLOSE via
gold_leaf_synonym; ITEM REVIEW at decisions.tsv:980 gives
curated_review_of_gold_leaf_synonym, still CLOSE. That parent's ITEM
endorsement does not establish the child's process/material identity.
The parent resolver and source row were checked, not its whole merged
taxon/graph corpus independently reaudited.

Current official [fresh water](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002011)
and the inspected typed snapshot define a low-solute water material,
subclassing liquid water (term 7173, subclass 5272).
No exact-source sample, measurement or definition establishes that node
8074 denotes this material rather than a simulation context. Having an
experimental use for water is not evidence that the procedure itself is
a subtype of water. This is an unsupported-genus finding with unresolved
source identity, not proof that every artificial-rain sample is non-habitat.

Freshly inspected alternatives preserve important distinctions:

| Candidate | Supported meaning and limit |
| --- | --- |
| ENVO:01000600 rainwater | Water originating by atmospheric-vapour condensation/precipitation, not automatically simulator supply water; term 8101, subclass 6354. |
| ENVO:01000830 water-based rainfall | A hydrological precipitation process, not a water-material identity; term 8325, subclass 6602. Typed rainfall/rain fall aliases are BROAD, and rain is RELATED. |
| ENVO:01001565 water-based rain | Falling water-droplet rain participating in rainfall, not an exact match established for this experimental bin; term 9058, subclass 7450. |
| ENVO:06105211 runoff | Water flowing over land without being retained, already the separately generated child; term 10217, subclass 8610. |

All four official term requests succeeded and agreed with the inspected
typed distinctions. Exact current ENVO searches for simulated rainfall
and rainfall simulation returned zero. The artificial rainfall query
returned HTTP 500; no negative result is claimed for that failed query.
No near match is proposed as an automatic exact replacement.

## Evidence

The complete exact-path/node scan across all 14 raw TSVs found only
gold_ecosystem_paths.tsv:1490: one node 8074, depth four, all counters zero.
The positive-organism rule at seed.py:892-895 therefore correctly omits
BOTH assertion_count and assertion_unit. Zero inventory counters do not
prove biological absence or that the source category is non-habitat.

No exact target bulk-biosample, complete-triad, study, parameter, taxon,
BacDive, PREGO or Madin row matched. These are snapshot misses. There is
no target study accession on which to base an original-methods request.
Current GOLD 8074 returned 404, not proof of retirement.

Parent row gold_ecosystem_paths.tsv:23 contains 2,055 organisms and nodes
3488/3786/4159. Current 3488/3786 returned 404; 4159 is active for the exact
Freshwater path, with aquatic-biome broad context and fresh-water medium.
That annotation belongs to the parent, not node 8074; neither its cohort
nor its medium annotation is imported into the target.

The complete current runoff child and its 20261005T022550Z review were read
as context. A hidden/ignored-inclusive corpus search found that child as
the only record listing this minted ID as a parent. Its node 8075 is in
tree row :1491; bulk row gold_path_biosamples.tsv:698 has seven biosamples.
The mixed study Gs0161537 at gold_studies.tsv:4500 covers runoff, liquid
manure and agricultural soil. It is not an exact parent study. Its original
page again returned 403; child GOLD 8075 returned 404. No sample allocation,
soil treatment or measured community is inferred for either parent or child.

The independently accessible USDA-hosted
[National Research Project protocol](https://www.ars.usda.gov/ARSUserFiles/80700000/NationalPprotocolrev.pdf)
was inspected in its source-water, simulation and runoff-collection text
(PDF pages 3-4 and 6-8). It treats input water, the simulation procedure
and collected runoff as distinct objects/activities. This is a bounded
methodological comparison, not provenance for node 8074 or Gs0161537.
No protocol settings, chemical results or microbial mechanism are transferred.
A separate JoVE lead presented a browser challenge and was not bypassed or
used as inspected evidence.

The complete generated page preserves the class-level caveat, count omission,
source path and UNGROUNDED/SEEDED status, but labels fresh water as broader.

## Completeness

Hidden/ignored-inclusive identifier, node, label, stem and exact-path
searches covered curation, history, research, configuration, docs,
source/tests, prior reports, PATHS and RETIRED, in addition to the complete
raw scans. They recovered the CLASS row, path lock and runoff context, but
no target ITEM decision, authored definition, causal overlay, dedicated
research/history, retirement or previous individual target review.

Missing optional taxa/chemistry/graphs are not extra defects. Experimental
process versus material scope is the consequential unresolved gap.
No gene, regulator or expression dataset is asserted, so iModulonDB is
not applicable. Parent/child context is not new whole-record review coverage.

## Findings

| Severity | Finding | Maintained owner / scope |
| --- | --- | --- |
| Major | An unresolved experimental-rainfall grouping is typed as fresh-water material without exact-source evidence establishing that material identity. | ITEM assessment of GOLD.452a98786f in curation/decisions.tsv and its exact source-parent contribution in src/habitatmech/seed.py or governed parent controls. |

No blocker was established because the precise source referent remains
unresolved. No minor was found. This record's own outgoing water edge is
distinct from the runoff child's unsupported incoming context edge in #1441.

## Recommended Edits

1. Resolve the exact source referent at ITEM depth. If it is a simulation
   procedure/non-habitat bin, use justified NOT_APPLICABLE treatment and
   remove unsupported habitat typing through maintained machinery. If it
   denotes supplied or collected water, define that qualified material from
   source evidence and choose a genuinely broader material genus.
2. Do not infer either branch merely from zero counts, the word rainfall,
   or the Freshwater path. Do not exact-ground to natural rainwater, a
   precipitation process, falling rain or the separately grounded runoff
   material without evidence of identity.
3. Preserve original source path/node, count/unit and predicate omission,
   locked stem and old history unless a governed identity correction
   explicitly changes their treatment. New assessment history is additive.
   A leaf-only decision does not itself suppress the source-parent pass.
4. This minted UNGROUNDED record meets the authored-definition status guard,
   but eligibility is not evidence. REPLACE requires a supported definition/
   genus and proof every inherited parent is false; do not manufacture a
   habitat definition for a procedure just to remove its water edge.
5. Coordinate #1441 without dropping the runoff child's valid ENVO identity,
   definition, exact synonyms, liquid-water genus or exact source mapping.
   A parent correction must not recreate an unsupported incoming is-a edge.

## Follow-up Checks

Regress the selected source identity, exact parent disposition, absent count/
unit and predicate, status/history and preserved runoff identity/genus.
Include valid freshwater-material and source-parent positive controls.
Append correction history, dry-seed, inspect exact forced canaries and use
guarded regeneration. Run schema/strict, labels, provenance/floor/history,
full reproduction, site/redirect/term-request and full QC gates.
Never hand-edit generated outputs or prune partial runs.

The actual full-context fresh-water-parent removal changes semantic text;
the already-omitted predicate is text-neutral. Genuine map/site refresh
under #1217 belongs with a correction, including any changed child links.
Preserve protected draft #1218 and runtime pins. These probes do not certify
current kg-microbe SSSOM/KGX compatibility.

## Additional Notes

All 626 open/closed issue titles/bodies were checked for exact source/child
keys, node boundaries and simulated-rainfall wording. Only #1441 matched;
its full body covers runoff's incoming edge and two other source children,
not this target's own outgoing fresh-water claim. Repository-wide comments
were not exhaustively searched.

No scientific edit, GitHub mutation, regeneration, status promotion or
historical-report rewrite occurred during this individual review.
Typed ENVO snapshot SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
