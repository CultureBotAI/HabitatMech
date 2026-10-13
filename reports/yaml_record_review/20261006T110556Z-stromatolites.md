# YAML Record Review: Stromatolites

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/stromatolites.yaml`
- Started UTC: 2026-10-06T11:01:40Z
- Finished UTC: 2026-10-06T11:05:56Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord habitatmech:GOLD.ae0d773157,
Stromatolites, AQUATIC, UNGROUNDED, SEEDED. Its sole source is
Environmental > Aquatic > Freshwater > Microbialites > Stromatolites,
GOLD7925. The actual mint matches and `PATHS.tsv:2566` pins the stem.
One minted parent and two history events are present; definition,
synonyms, xrefs, parameters, taxa, evidence and graphs are absent.

This is the freshwater GOLD whole-structure bin, not the separate
PREGO-backed ENVO:00002157 stromatolite mat record. Both the full
immediate parent and full mat comparator were read; their observations
are not imported as evidence for this source.

## Validation

- `just validate data/habitats/aquatic/stromatolites.yaml`: passed.
- `just validate-strict data/habitats/aquatic/stromatolites.yaml`:
  one file, zero errors.
- Full actual `build_corpus` / `build_document` equality passed:
  one source concept, zero reviewed sources, zero taxa, two events,
  every emitted field equal to the committed record.
- Executed default/applied target and parent routes, scanned all 14 raw
  inventories for exact path/node membership, and read the full page
  and full-context semantic text.
- [Main QC on exact base 7c8d28437](https://github.com/CultureBotAI/HabitatMech/actions/runs/37452730923)
  is now terminal SUCCESS. Its log verifies every gate: 463 tests passed,
  three skips, two dependency warnings, 90 valid histories, 3,206 records
  with zero strict errors and exact reproduction, current site/redirects/
  term requests. Scientific inputs and code are unchanged; this is baseline
  reuse, not a fresh full QC for each report.
- Required label correspondence passed on the merge candidate with zero
  flagged pairs and 2,054 no-adapter skips. No taxon identifiers or
  evidence/graph references are emitted for this target.

## Identity and Grounding

`curation/decisions.tsv:986` is CLASS CONFIRM_UNGROUNDED, not an item
review. Actual gold_unmatched becomes
curated_confirm_ungrounded_from_gold_unmatched, retaining the minted
identity, UNGROUNDED, no predicate and reviewed=False. The SEEDED status
and history accurately disclose the limitation. This review does not
promote them or add an event.

Current ENVO searches for stromatolite/stromatolites return only
[stromatolite mat, ENVO:00002157](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002157);
laminated microbialite returns no term. The mat has no definition and
subclasses [microbial mat, ENVO:01000008](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000008),
a layered sheet of microorganisms. Neither its near-matching name nor its
six PREGO associations proves equivalence to a lithified stromatolite.
These are bounded ENVO searches, not a claim that no external vocabulary
can name the structure.

[Microbialite, ENVO:03600064](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03600064),
has a carbonate-mud, benthic microbial-formation definition and the named
parent ENVO:00002016 sedimentary rock. Both current OLS and the typed
official OWL snapshot were checked. This is not a mat identity and
should not become an exact merge of every setting-specific microbialite.
Source-specific mineralogy remains unverified for GOLD7925.

The immediate parent habitatmech:GOLD.e53e2c6e8e is the separately
minted freshwater Microbialites bin. Its actual ITEM GROUND_AS_PARENT
route at `decisions.tsv:1265` preserves the source identity and adds
ENVO:03600064. A freshwater stromatolite is a form of freshwater
microbialite, so the child's direct source-parent relation is defensible.

However, the parent's independent GOLD path-parent pass also adds
ENVO:00002011 fresh water. The exact emitted ancestry is:

`GOLD.ae0d773157 -> GOLD.e53e2c6e8e -> ENVO:00002011`.

Fresh water is low-solute liquid-water material, not the superclass of
a lithified microbialite growing in it. The false second edge therefore
affects this descendant. Its owner is the parent contribution already
tracked by [#1406](https://github.com/CultureBotAI/HabitatMech/issues/1406),
not the supported Stromatolites-to-Microbialites edge.

## Evidence

`gold_ecosystem_paths.tsv:1485` supplies the exact depth-five path,
one node (7925), and zero organism/study/biosample/total counters.
Omitting assertion_count and assertion_unit is faithful; zero counters
do not prove the habitat lacks organisms.

No exact target path/node match occurs in the committed bulk-biosample,
triad or study tables, nor any parameter or taxon feed. This is an
exact-match inventory result, not proof that upstream sampling never
occurred. The current official GOLD7925 projection returned HTTP 404;
that alone does not prove retirement or invalidate the historical node.
Original sample evidence remains unrecovered.

Do not borrow the immediate parent's 14 bulk samples, nine API samples
or four study memberships from its earlier review. Those concern the
broader Microbialites path, not GOLD7925. Likewise, the comparator
stromatolite-mat record's six taxa and scores are not this child's taxa.

[Proemse et al. 2017](https://www.nature.com/articles/s41598-017-15507-1),
DOI 10.1038/s41598-017-15507-1, [PMID 29133809](https://pubmed.ncbi.nlm.nih.gov/29133809/),
directly reports living freshwater stromatolites in Tasmanian karstic
wetlands and bacterial community analysis. The inspected primary
abstract, introduction and figure captions identify laminated microbial
mineral accretions and sectioned calcite laminations. This supports
the freshwater habitat interpretation and the distinction between a
mineral structure and its microorganisms. It does not identify GOLD7925,
establish the composition of every source sample, or justify copying
the study's chemistry, taxa or mechanisms into this generic source bin.

The separately located Rivularia freshwater-stromatolite paper could
not be opened at its publisher; no claim here depends on its search
snippet. Primary evidence above is sufficient for the bounded distinction,
not a complete review of stromatolite formation mechanisms.

## Completeness

Ignored-inclusive ID/node/path, singular/plural label and stem searches
covered curation, history, research, configuration, documentation, source,
tests, reports, raw inventories and path/retirement registries. The
decision and path lock exist; no target-owned definition, causal overlay,
session history, retirement or prior individual Stromatolites report
was found. Existing microbialite reports are parent context.

An ITEM scope assessment and a distinguishing definition would improve
the source's interpretability, particularly whole structure versus
associated mat and freshwater versus global scope. Missing optional
fields and honestly declared SEEDED status are not independently counted
as defects. No justified quantitative condition or characteristic taxon
was recovered. iModulonDB is not applicable without a gene, regulator or
expression claim.

## Findings

Zero blockers, one major, zero minors:

1. **Major: inherited false water-material ancestry.** The emitted child
   reaches ENVO:00002011 through freshwater Microbialites. The invalid
   edge is at the parent, already owned by #1406. Maintained owner:
   the exact GOLD.e53e2c6e8e source-parent contribution in
   `src/habitatmech/seed.py:898-907`, governed controls and regressions.
   This is a descendant-impact witness for an existing defect, not a
   new false direct edge or a duplicate implementation issue.

The current child has no mapping predicate; the parent's separate #1398
endpoint/status issue is not claimed as an emitted child predicate defect.

## Recommended Edits

Repair the parent's false water edge while retaining the child-to-parent
relationship and the parent's supported microbialite reference.
Preserve GOLD7925, exact source path, minted identity, pinned stem,
AQUATIC category, zero-count omission and original events. Do not use
blanket REPLACE on the child, classify the habitat NOT_APPLICABLE or
exact-merge it with stromatolite mat.

A later ITEM assessment can clarify the source scope and, if justified,
author a qualified label/definition in `curation/term_requests.tsv`
with an appropriate verified genus. Preserve supported inherited parents
with ADD rather than deleting them for preference. Do not invent sample
mineralogy or assume all uses of stromatolite match ENVO's carbonate-specific
microbialite definition. The current definition interface is for minted
UNGROUNDED terms; do not switch to NARROW and assume it still accepts an
authored definition without checking the maintained contract.

## Follow-up Checks

An actual in-memory corpus probe removed only ENVO:00002011 from the
parent concept. The child's complete `build_document` output remained
unchanged, and the parent retained ENVO:03600064. Add that preservation
case to #1406's regression coverage alongside valid source-parent controls.

Full-context semantic text changes for the corrected parent but not
for this otherwise unchanged child: the adapter reads direct parent
labels, not transitive ancestry. An exploratory direct-child-parent
removal also changed text, but it is not a scientifically justified fix.
A qualified child label changes its own text and must be assessed
separately. Do genuine #1217 map/site regeneration wherever actual inputs
change; isolate #1218 and runtime pins.

Future scientific curation requires append-only history, dry seed,
inspected guarded canaries for the changed parent and preserved child,
labels/provenance/schema checks, full reproduction and site/redirect/
term-request/QC gates. No scientific inputs, histories, generated products
or SSSOM/KGX artifacts were changed or certified here.

## Additional Notes

All 634 open/closed issue titles/bodies were searched for exact source
keys, stromatolite/microbialite labels and candidate IDs. #1406's full
body and its one comment were inspected; it owns the parent correction.
#1404 is a closed report-label correction, not the scientific fix.
No exact child-specific issue was found on those bounded surfaces;
every repository issue comment was not exhaustively searched.

Typed official ENVO snapshot SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
