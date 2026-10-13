# YAML Record Review: Apoeccrine sweat glands

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/apoeccrine_sweat_glands.yaml`
- Started UTC: 2026-10-04T02:55:34Z
- Finished UTC: 2026-10-04T02:57:48Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord `habitatmech:GOLD.d0912b66fe`:
HOST_ASSOCIATED, UNGROUNDED, SEEDED. It has one parent, one uncounted GOLD
attestation and two generated events. The source is Human > Integumentary
system > Apoeccrine sweat glands, not the neighboring Apocrine sweat glands
or its own Sweat child. The actual `mint` helper reproduces the identifier;
`PATHS.tsv:2826` pins the filename.

## Validation

- `just validate data/habitats/host_associated/apoeccrine_sweat_glands.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/apoeccrine_sweat_glands.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed, 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh batch QC remains running in its final corpus-report stage. Earlier
  gates passed: lint, documentation, raw provenance, 457 tests (three skipped,
  two dependency warnings), 85 history records, 3,206 strict-valid records,
  32 overlays, curation floor, exact corpus reproduction with zero missing,
  extra or differing records, current site, 231 redirects and 109 term-request
  table entries. No terminal batch result is claimed yet.
- Official OLS search and primary PubMed EFetch requests succeeded.

## Identity and Grounding

`curation/decisions.tsv:1150` is CLASS CONFIRM_UNGROUNDED and explicitly says
that habitat meaning was not assessed. SEEDED and the August 12/16 events
preserve this limitation. The record does not claim that a lexical screen
resolved the biological status of this proposed gland type.

A current [bounded OLS search](https://www.ebi.ac.uk/ols4/api/search?q=apoeccrine&ontology=bto%2Cuberon%2Cenvo&rows=50)
returned zero named candidates in BTO, UBERON and ENVO. Ignored-inclusive
searching of the complete vendored term table also found no apoeccrine
wording. Neither check proves absence from every ontology. The separately
verified BTO:0001331 sweat-gland class is a possible broader lead for future
ITEM review, not an exact identity or a decision applied by this report.

The complete human `integumentary_system__2442c03e.yaml` was read in this
batch. Its identifier, `habitatmech:GOLD.dc86c8917c`, is NARROW beneath
[UBERON:0002416](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0002416),
independently verified as a non-obsolete connected anatomical system.
There is no authored broader gland-environment definition on the source.
Whatever the eventual classification of the proposed gland, source nesting
does not make it a kind of whole integumentary system.

## Evidence

`gold_ecosystem_paths.tsv:2256` provides the exact four-level path,
nodes 6865/6868 and zero organism, study and biosample assertions. The first
ID, multiplicity note, full path and absent positive count are faithful.
Row 2257 instead denotes the Sweat child, node 6866. Gland, secretion and
two collapsed source nodes must not be treated as interchangeable samples.

Complete scans of 2,562 tree paths, 1,040 bulk rows, 4,587 studies and
1,587 triads find only those two tree rows for apoeccrine wording or the
target key. No target bulk, study or triad association was found. The source
attests a vocabulary category, not a demonstrated gland microbiome.

Four primary abstracts were inspected, with authors, dates and primary
ArticleIdList PMID/DOI pairs verified:

- [Sato, Leidal and Sato 1987](https://pubmed.ncbi.nlm.nih.gov/3812728/),
  DOI:10.1152/ajpregu.1987.252.1.R166, proposed a third gland type from
  axillary morphology and developmental observations.
- [Sato and Sato 1987](https://pubmed.ncbi.nlm.nih.gov/3544873/),
  DOI:10.1152/ajpregu.1987.252.1.R181, reported distinct secretion behavior
  in isolated glands under in-vitro stimulation.
- [Wilke et al. 2006](https://pubmed.ncbi.nlm.nih.gov/16247248/),
  DOI:10.1159/000089142, reported morphological/immunofluorescence evidence
  for apoeccrine glands in axillary skin.
- [Bovell et al. 2007](https://pubmed.ncbi.nlm.nih.gov/17535227/),
  DOI:10.1111/j.1365-2133.2007.07917.x, found none in serial sections from
  ten adult volunteers and found the tested discrimination markers nonspecific.

These observations conflict in identification and method. The negative
study does not prove universal nonexistence, and the positive studies do not
settle universal prevalence or a unique ontology identity. Only abstracts
were inspected. No physiological value, microbial taxon, gene or causal
edge is imported, and evidence for apocrine odor metabolism is not transferred.

## Completeness

Ignored-inclusive identifier, label and filename searches covered curation,
history, research, prior reviews, raw inventories, PATHS and RETIRED. They
found the CLASS row and source paths but no target ITEM decision, definition
request, overlay, session record, research report or earlier exact-target
review. The new apocrine report mentions this distinct sibling; it is not
an apoeccrine target review. Missing later-style history for old curation
is not a retroactive defect.

Full scans of 162 BacDive sources, 3,081 BacDive taxa, 770 parameters,
358 mappings, 58 Madin habitats, 1,378 Madin taxa, 719 PREGO habitats and
8,807 PREGO taxa found no apoeccrine wording or target-key match. This is
bounded inventory absence, not absence of associated microorganisms in
nature. Optional fields are not quotas. iModulonDB is not applicable:
no microbial gene, regulator or expression-module claim is supplied.

## Findings

1. **Major - HM-APOECCRINE-001:** the proposed gland category inherits the
   whole human integumentary system as an is-a parent. Owner:
   `src/habitatmech/seed.py:898-907` or a governed source-specific exclusion.
   Added as a third exact witness to
   [#1337](https://github.com/CultureBotAI/HabitatMech/issues/1337).

No blocker or minor finding established. Anatomical identification remains
unresolved, but the limited CLASS/SEEDED status does not claim otherwise.
The report does not turn uncertainty into a false non-habitat judgment.

## Recommended Edits

Correct or exclude this exact whole-system parent while preserving the
source identity, both nodes and absent positive counts. Keep conflicting
primary evidence explicit in future ITEM curation. Do not automatically
merge with apocrine/eccrine glands, declare non-habitat from one negative
study, or globally delete source parents.

Any future anatomical genus or definition requires a separate supported
ITEM decision and the repository's valid grounding/definition route.
Do not hand-edit generated YAML or encode membership as an equivalence xref.
A read-only real-adapter comparison confirms the parent removal changes
semantic input by dropping Integumentary system. Append required history,
inspect a guarded canary and regenerate map/site with supported tooling;
#1217 remains relevant, and draft #1218 is not assumed merged.

## Follow-up Checks

Regress the exact false edge, preserve source nodes/count semantics and
check intended status. For further identity curation, inspect full studies,
resolve diagnostic criteria and retain their population/method scope.
Run strict schema, OAK, complete ancestry, history, corpus reproduction,
map/site/redirect freshness and QC. Do not use a lexical match to settle
the anatomical disagreement.

## Additional Notes

All 492 existing issue bodies and returned comments were searched for the
target key, apoeccrine wording and whole-system-superclass mechanism.
#1337 already owned the maintained parent rule; the exact witness and the
identity caveat were added there. Parent reference reads do not add review
coverage. No scientific input, generated record or history changed;
no paid research ran.
