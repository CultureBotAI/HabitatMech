# YAML Record Review: oceanic abyssopelagic zone biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/oceanic_abyssopelagic_zone_biome.yaml`
- Started UTC: 2026-10-04T21:14:29Z
- Finished UTC: 2026-10-04T21:18:01Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord ENVO:01000038, oceanic abyssopelagic zone
biome, AQUATIC/CLOSE/REVIEWED. One GOLD source contributes 16 ORGANISM
assertions, an exact source-label synonym and two history events. The record
has an ENVO definition and two parents, but no taxa, parameters, xrefs,
record-level evidence, graphs, discussions or datasets.

`PATHS.tsv:765` pins the filename. Actual source minting gives
habitatmech:GOLD.1edff6a744 for Environmental > Aquatic > Marine > Abyssopelagic.
This is not the separately minted Pelagic zone > Abyssopelagic/Abyssal zone
source, an abyssal-plane landform or a trench. Do not merge those records
solely because their labels share a depth-band word.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/oceanic_abyssopelagic_zone_biome.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/oceanic_abyssopelagic_zone_biome.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared batch PASS: 1,179 canonical, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | Shared PASS: 953 ungrounded records and 1,810 decisions. |
| `just qc` | Authorized batch run remains active in tests after an initial pre-run uv cache denial; lint, documentation and 14-inventory provenance passed. No terminal result claimed. |
| Source/reference checks | Full target and maintained decision, actual resolver and full-corpus field equality, all 14 raw tables, current typed ENVO/OLS, both GOLD nodes, original-study attempts, NOAA depth account, entire rendered page and semantic comparison. |

Actual build reproduces every target field, with one source concept, one
reviewed source, no taxa and two history events. That proves faithful input
application, not scientific equivalence of every related depth term. No
SSSOM/KGX compatibility audit is claimed. Later terminal QC belongs in the
publication receipt rather than this timestamped result.

## Identity and Grounding

Current [ENVO:01000038](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000038)
is active and matches physical ontology_terms.tsv line 7548. Its definition
sets an approximate upper boundary around 2,500-2,700 m and a lower boundary
near 6,000 m or the near-seafloor benthopelagic setting. These are inherited
ontology scope statements, not measurements from the 16 GOLD organisms.

The sole named ontology superclass is ENVO:01000033 oceanic pelagic zone
biome, matching subclass row 5678. Its current prose anomalously says
epipelagic although its label and asserted hierarchy are generic pelagic;
that is an upstream clarification question, not justification for deleting
the asserted parent or silently rewriting a generated definition.

The second parent, ENVO:00001999 marine water body, comes from GOLD Marine
nesting through seed.py:898-907. This same source-parent resolution was
executed in the preceding individual trench review: Marine is reviewed CLOSE
to ENVO:00001999. A depth-delimited biome is not a subtype of the whole
marine waterbody. Remove only that source contribution through a maintained
rule, preserving the asserted pelagic-biome parent.

`curation/decisions.tsv:271` is an ITEM GROUND decision dated 2026-08-12,
with target ENVO:01000038 and CLOSE. Actual default resolution is
gold_unmatched/UNGROUNDED; the decision yields curated_ground_from_gold_unmatched,
reviewed=True and skos:closeMatch. The displayed status and GROUND/seed events
are genuine. This symmetric close mapping is not a #1398 narrow-direction
witness, nor permission to upgrade the source to EXACT.

Current GOLD node 5340 annotates this exact path with ENVO:01000038 as
env_broad, but supplies no exact-match or local/medium assertion. This is
positive contextual support for the conservative existing mapping, not
proof that broad context and source identity are interchangeable. Current
ENVO:00000212 marine abyssalpelagic zone also exists, so the old nearest-
available rationale is not an exhaustive modern candidate comparison.

The inspected [NOAA layer account](https://www.noaa.gov/jetstream/ocean/layers-of-ocean)
uses 4,000-6,000 m for its abyssopelagic zone, unlike the biome definition's
shallower upper extent. Preserve this scope difference. Neither general
account establishes the inaccessible GOLD samples' actual depths or licenses
replacing an ontology definition locally. Retain CLOSE pending exact source
evidence rather than force a new identity from a similar label.

The sole synonym Abyssopelagic is GOLD's source label, emitted by the source-
label path, not an ENVO synonym assertion. Its lexical shorthand does not
prove source-to-ontology exact identity or settle zone-versus-biome scope.
No current #1249 ontology-scope witness is present in this record.

## Evidence

`gold_ecosystem_paths.tsv:452` gives depth four, nodes 5339 and 5340, 16
ORGANISM assertions and zero study/biosample counters. The generated first-
node identifier and two-node note agree. Current 5339 returned 404, not proof
of retirement; 5340 is active with the exact path and broad annotation above.

`gold_path_biosamples.tsv:700` separately records seven bulk samples at 5340.
No exact-source complete-triad row exists in the 14-table structured scan.
Study memberships at rows 1989 and 2920 are Gs0133493 (two paths) and
Gs0145237 (four depth-band paths). Both original study-page requests returned
403. The 16 organisms, seven bulk samples and two study memberships are
different units, not a reconciled sample cohort or independent replicates.

The target ontology ID appears as broad context in triad row 605 for
Oceanic > Abyssal plane: 77 samples and six studies. That is a different
source path. Those observations were not borrowed as attestations, measured
parameters or mechanistic support for this record.

The source-path scan covered all 14 raw tables; the additional ignored-
inclusive ontology-ID scan found the ontology term, its subclass row and
that other-path triad reference. No PREGO, BacDive, MADIN, taxon or parameter
contribution feeds the actual target. Lack of a displayed taxon list does
not mean the habitat lacks microorganisms or that the GOLD count is zero.

## Completeness

Ignored-inclusive searches for the ID, minted key, source path, label/stem
and filenames covered curation, history, research, reports, conf, PATHS and
RETIRED. They found the ITEM decision and path lock, but no target-owned
authored definition, causal overlay, session history, retirement or previous
individual review. Broad numeric-node hits in lock hashes were not treated
as source references. Neighboring depth-band reports concern other targets.

No novel-term request or mandatory missing field is established. Keep
optional parameters and graphs empty without target-specific measurements
or mechanism evidence. iModulonDB is inapplicable without gene, regulator
or expression assertions. The main unresolved evidence is exact source
scope and inaccessible study context, not schema completeness.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | GOLD Marine nesting adds a false whole-waterbody parent to a depth-delimited biome. | Scoped GOLD parent contribution in src/habitatmech/seed.py:898-907 and governed curation input. |

Counts: zero blockers, one major, zero minor. Grounding remains conservatively
CLOSE rather than being declared exact or wrong solely from a general depth
convention. Upstream wording and source-scope limitations remain explicit.

## Recommended Edits

1. Suppress only the unsupported ENVO:00001999 source-parent contribution.
   Preserve the asserted ENVO:01000033 parent, current ontology identity,
   source path/count/unit and genuine review history. Do not remove all GOLD
   parent edges or edit the generated record.
2. Add a targeted regression preserving valid parents and evidence. When
   revisiting identity, compare both current zone and biome candidates using
   original source scope; update the existing source decision rather than
   insert a duplicate, and append new history instead of editing old events.
3. Do not use SAME_AS to the already grounded minted source as a shortcut
   for merging the slashed sibling. If future evidence establishes that both
   truly share ENVO:01000038, each source needs its own appropriate direct
   GROUND decision; this report does not make that sibling decision.

## Follow-up Checks

Dry seed and inspect `just seed-canary ENVO:01000038 --force` after an input
correction, then guarded full regeneration without partial prune. Require
parent-retention regressions, ordinary/strict/product checks, new history,
exact corpus reproduction, rendered site/redirect/term-request checks and
full QC. Reassess all affected attestations if any future identity changes.

Actual full-context removal of the waterbody parent changes semantic text,
requiring genuine map/site refresh under #1217. Preserve protected draft
#1218/runtime pins, and do not infer SSSOM/KGX readiness from record validation.

## Additional Notes

All-state source-ID, ontology-ID and abyssopelagic issue searches returned
closed review-correction issues #375, #376 and #377, not an implemented
scientific repair for this target. Full #375 and #377 bodies establish the
SAME_AS and duplicate-decision cautions preserved above. No GitHub mutation,
scientific edit, generated write, old report/history change or paid research
was part of this individual review.

Official typed ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
