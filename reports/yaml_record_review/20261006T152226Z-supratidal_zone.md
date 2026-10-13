# YAML Record Review: Supratidal zone (littoral GOLD path)

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/supratidal_zone.yaml`
- Started UTC: 2026-10-06T15:19:57Z
- Finished UTC: 2026-10-06T15:22:26Z
- Verdict: needs curation; 0 blocker, 2 major, 0 minor findings.

## Target

The whole generated HabitatRecord was read: habitatmech:GOLD.2ef6207bd1,
Supratidal zone, AQUATIC/NARROW/SEEDED. The exact source is Environmental >
Aquatic > Marine > Littoral zone > Supratidal zone, node gold.ecosystem:7910.
It has two parents, one uncounted attestation and one seed event.
PATHS.tsv:1633 pins this target, distinct from the shallower Supratidal zone
source currently resolved to ENVO:01000124. Baseline:
4157ac2b3935aa8a5ab6d018df5acc15fd5214b6.

## Validation

- `just validate data/habitats/aquatic/supratidal_zone.yaml`: pass.
- `just validate-strict data/habitats/aquatic/supratidal_zone.yaml`: pass,
  one file and zero errors.
- Full actual build_corpus/build_document equality: pass, one contributing
  source, zero reviewed sources, zero taxa, one history event.
- Actual child/parent resolution, leaf claimant and full-context semantic
  comparison were executed; outcomes are detailed below.
- Fresh shared baseline gates all passed: `just verify-corpus --max-diffs 1`
  (3,206 exact records), `just validate-history` (95),
  `just validate-causal-all` (32 graphs), `just term-requests-check` (109),
  `just provenance-check` (14 inventories/two GOLD sources),
  `just worklist --limit 3`, and `just report` (688 REVIEWED/2,518 SEEDED).
- Shared `just validate-products`: 1,179 canonical, one synonym, five accepted
  exceptions, 2,054 configured no-adapter skips; pass, not semantic approval.
- `git diff --quiet -- curation data/raw src scripts data/habitats pages history README.md`
  confirmed those scientific inputs/products remain at the tested baseline.
- Full tests/QC and browser visual QA were not rerun for report-only changes.
  No standalone reference validator is documented for this citation-free
  record; it contains no parameter/taxon/edge reference to resolve.

## Identity and Grounding

seed.mint reproduces the full-path identity. The automatic and applied
routes both take gold_narrower_than_leaf_match, with no target decision:
retained source mint, NARROW/skos:narrowMatch, ENVO:01000124 as extra parent.
The shallowest claimant is Environmental > Aquatic > Marine > Supratidal zone.
Path depth explains the algorithm, not an ITEM judgement of biological
specificity. The child does not inherit that shallower source's review.

The immediate Littoral zone source GOLD.2a3e25f443 resolves through
gold_composed_label to ENVO:01000125, EXACT and unreviewed. The independent
GOLD parent pass at seed.py:908-929 adds that second parent to the child.
The complete marine_supra_littoral_zone.yaml and marine_littoral_zone.yaml
were read as context, not counted as new reviews.

Current typed official
[ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
and vendored ontology_terms.tsv:7630-7631 distinguish the upper, normally
spray-exposed supra-littoral area from the whole marine littoral region
extending approximately from the spray region to the continental shelf.
The child's source does not denote that whole region.

The structured OWL explicitly places ENVO:01000124 under ENVO:01001201 marine
environmental zone, with a BFO:0000050 part-of restriction to ENVO:01000125.
The latter's named parent is ENVO:01000407 littoral zone. These active classes,
definitions and named parents were checked; blank-node restrictions were
decoded as predicates and fillers, not mistaken for named superclasses.
Containment is therefore supported, not the emitted child-is-a-whole-zone.

ENVO types supratidal zone as a related synonym of marine supra-littoral
zone, not exact. The source's marine context makes that term relevant, but
the flattened synonym hit and extra GOLD level alone cannot settle exact
identity versus genuinely narrower scope. Preserve this uncertainty for ITEM
assessment. No synonym entries are emitted on this child, so the separate
parent record's synonym-scope inflation is not a third child finding.

SourceAttestation.mapping_predicate (schema lines 317-322) describes
source-to-record comparison and omission when the record is the source.
GroundingStatusEnum (lines 776-790) also compares record with source. Here
the record remains precisely the source's minted identity, while the
NARROW/predicate computation compares it with the implicit ontology parent.
Those are different endpoints. This is an application-contract mismatch,
not a claim that SKOS formally forbids hierarchical self-links.

## Evidence

Exact full-path, minted-ID and node membership searches covered all 14 raw
TSV inventories. gold_ecosystem_paths.tsv:1534 gives depth five, one node and
zero organism/study/biosample/total KGX counters. The emitted attestation
preserves label, path and node; omission of count/unit is correct. Its
mapping predicate is locally computed, not an imported GOLD assertion.

No exact target row was found in the committed bulk biosample, API triad or
study membership inventories, nor a source-key contribution elsewhere in
that scan. This bounded snapshot result is not absence of microbial life.
The enclosing littoral source has three organisms and nodes 7907/7909; the
shallower supratidal source has nodes 8047/8048. None is a child count or ID.

The directly inspected S section of the
[NOAA estuary glossary](https://coast.noaa.gov/estuaries/estuary-resources/glossary.html)
describes supratidal flooding as occasional under unusually high/storm tides.
It supports an intermittently wetted shore setting, not permanent submergence,
a water body, fixed chemistry or any taxon/causal assertion. AQUATIC is the
coarse source-derived category, not a contradictory submergence measurement.

The complete generated HTML preserves source scope and the NARROW/SEEDED
warning but presents both parents as broader habitats. Actual semantic_text
contains both labels; an in-memory removal of only ENVO:01000125 changes the
text. No generated record, page or map was edited.

## Completeness

Ignored/hidden-inclusive searches by ID, label, stem and exact path covered
curation, history, research, reports/research manifest, conf, docs, src,
tests, PATHS and RETIRED, plus the full raw scan. No target-owned decision,
definition, causal overlay, exclusion or prior exact-target report was found.
The related intertidal and supra-littoral reports were inspected only as leads;
fresh source/code/ontology checks establish this target's findings.

Empty definition, measurements, taxa, evidence, datasets and mechanisms are
not independent defects. iModulonDB is not applicable: no organism, gene,
regulator or expression dataset is asserted. No sample-level evidence was
invented to fill the blanks.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | The component supratidal zone inherits the whole marine littoral zone ENVO:01000125 as a strict superclass, converting source containment into is-a. | Exact GOLD.2ef6207bd1 contribution in curation/gold_parent_exclusions.tsv and the independent seed.py parent pass. |
| Major | Retained-source NARROW/skos:narrowMatch uses an implicit ontology-parent endpoint, contrary to the declared source-to-record field contract. | Shared schema/resolver/attestation-consumer contract in src/habitatmech/schema/habitatmech.yaml and src/habitatmech/seed.py; existing issue #1398. |

No blocker or minor finding was established. Exact-versus-narrow candidate
scope remains unresolved; it is not counted again as a separate defect.

## Recommended Edits

1. ITEM-assess and exclude only the exact path's ENVO:01000125 context parent
   with the guarded maintained table. Preserve the source mint, node/path,
   omitted count, stable stem and independent ontology-candidate contribution
   while that candidate is separately assessed. Do not bulk-delete parents.
2. Resolve the actual source/record/ontology-parent comparison contract under
   #1398, representing endpoints explicitly and aligning all consumers.
   Swapping broadMatch/narrowMatch or merging same-labelled source bins is
   not a fix for an implicit target. Add this source as an automatic-route
   regression witness when that authorized work is performed.
3. Assess whether the extra littoral path level adds real specificity before
   choosing exact identity, broader placement or a justified same-as merge.
   A related synonym alone is not proof. Record any curation in maintained
   decisions and append session history; do not promote status from this report.

## Follow-up Checks

Regress guarded parent exclusion and preservation of independent placement,
source identity, zero-count omission and history. Test actual subject,
predicate, object and grounding-status meaning across source and ontology
routes. Dry-seed and inspect an exact canary before broader regeneration;
then run schema/strict, labels, provenance, curation-floor, history, exact
reproduction and full QC. A changed parent changes semantic text and needs
genuine map/site regeneration. Audit SSSOM/KGX exports against current
kg-microbe separately before claiming product compatibility.

## Additional Notes

[Issue #1398](https://github.com/CultureBotAI/HabitatMech/issues/1398) was read
directly and remains OPEN; its body describes this same endpoint contract and
requires downstream export verification. It was not edited or closed, and no
new issue was created. No exhaustive issue/comment deduplication is claimed.
The typed ontology retrieval parsed 106,817 triples at the pinned commit.
No paid research, scientific edits, curation event or review-status mutation
was performed.
