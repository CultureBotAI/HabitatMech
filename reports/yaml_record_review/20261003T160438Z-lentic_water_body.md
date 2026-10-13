# YAML Record Review: Lentic water body

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/lentic_water_body.yaml`
- Started UTC: 2026-10-03T16:02:37Z
- Finished UTC: 2026-10-03T16:04:38Z
- Verdict: needs curation

## Target

Read the entire generated `HabitatRecord`, `ENVO:01000617`, lentic water body,
`AQUATIC`, `EXACT`, `REVIEWED`: ontology definition, one GOLD exact synonym,
two parents, one attestation, an ITEM grounding event and a seed event.
`PATHS.tsv:849` fixes this target. Its only source is
`Environmental > Aquatic > Freshwater > Lentic`, which mints to
`habitatmech:GOLD.312657c243`.

## Validation

- `just validate data/habitats/aquatic/lentic_water_body.yaml`: pass.
- `just validate-strict data/habitats/aquatic/lentic_water_body.yaml`: pass,
  zero errors.
- Source mint, both node IDs, the 388-ORGANISM count and exact-path bulk,
  triad and study crosswalks were checked.
- Official ENVO OWL XML verifies the identity, both parent meanings, fresh
  water body, lake water and a marine subclass counterexample.
- Exact baseline `d1b6aa47b` passed full QC 37133815658 and labels 37133815698.
  Fresh local full QC is still running, not claimed complete. Green schema
  and correspondence gates do not validate is-a meaning or equivalence scope.

## Identity and Grounding

`curation/decisions.tsv:367` explicitly grounds GOLD's freshwater-qualified
Lentic source exactly to the unrestricted lentic-water-body term. The
ontology defines the latter by very little overall directed flow, not low
salinity. Its current subclass `ENVO:00001999` marine water body is an
explicit counterexample to interpreting all lentic water bodies as freshwater.
The stored definition is faithful, but the source-to-identity equivalence
does not preserve the freshwater restriction. `REVIEWED` truthfully reflects
the existing ITEM row; it does not make that row's scope judgment correct.
[Official ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl).

The direct ontology parent `ENVO:00000063` water body is true. The additional
GOLD parent `ENVO:00002011` fresh water denotes material, not an accumulated
water body. It is neither a valid is-a parent for the unrestricted ontology
class nor a way to encode the source's freshwater composition.

`ENVO:01001320` is fresh water body, with no lentic qualifier. It models
composition using a restriction to fresh water rather than subclassing the
material. It is a useful broader candidate for a freshwater-lentic source,
not an exact substitute that would preserve the low-flow restriction by
itself. Do not confuse its actual label with an invented lentic-freshwater
class. A minted source-specific identity under both verified broader body
concepts is a conservative option if no exact term is established.

## Evidence

`gold_ecosystem_paths.tsv:80` contains nodes 3791/4174, depth four and 388
organism assertions. The first-node note and `ORGANISM` unit match.
`gold_path_biosamples.tsv:301` separately has 68 bulk samples; exact-path
membership was verified for 18 studies in `gold_studies.tsv`. Those accessions
were checked in the committed crosswalk, not through live study metadata.

`gold_path_triads.tsv:341-343` describes 55 complete API triads across 16
studies. Modal broad/local/medium terms are freshwater lake biome
(`ENVO:01000252`), freshwater lake (`ENVO:00000021`) and lake water
(`ENVO:04000007`), with shares 0.82, 0.76 and 0.78, respectively. Their
agreeing-study counts are 13, 11 and 10; distinct-term counts are 3, 6 and 6.
All three term meanings were inspected. These contexts support freshwater
lentic sampling without making every source member exactly a lake, a lake
biome or a water sample. Bulk and API snapshots were not assumed identical,
and neither was summed with organisms.

## Completeness

Ignored-inclusive target/source-ID, label and stem searches covered curation,
history, research, configuration, reports, raw inventories and path locks.
The ITEM row was found; no target authored definition, causal overlay,
session history or prior exact-target report was found. Descendant reviews
are not reviews of this source. Exact source-path scanning identifies five
children: Sediment, Epilimnion, Hypolimnion, Littoral zone and Limnetic zone.
Their source-parent edges need individual containment checks; enumerating
these paths is not five completed reviews. Renaming the parent does not
automatically repair a child's false edge. iModulonDB is not applicable to
this geography-only record. Empty optional taxa and mechanisms are appropriate.

## Findings

1. **Major: the freshwater-qualified source is equated with an unrestricted
   lentic-water-body class.** Owner: the ITEM `GROUND` row for
   `habitatmech:GOLD.312657c243` in `curation/decisions.tsv:367`. A broader
   class is not an exact replacement for the qualified source.
2. **Major: the accumulated water body inherits fresh-water material as an
   is-a parent.** Edge `ENVO:01000617 -> ENVO:00002011`; owner: GOLD source
   parent propagation in `src/habitatmech/seed.py:898-907`, not an ontology
   subclass assertion on lentic water body.

Zero blockers, two major findings, zero minor findings.

## Recommended Edits

Reassess the exact source-specific ITEM row. Use a verified exact term only
if it retains both freshwater composition and lentic scope; otherwise retain
a minted freshwater-lentic identity with appropriate broader body concepts
through decisions and a maintained definition. Remove only the false GOLD
material contribution via governed source-parent controls. Do not ground
exactly to unrestricted fresh water body, and do not use blanket `REPLACE`
to discard a true lentic parent while fixing an unrelated false edge.
Preserve both GOLD nodes, full path and 388-ORGANISM count.

## Follow-up Checks

Add separate regressions for mapping scope and the excluded material edge.
Canary the source, inspect the five children and any retired URL/redirect,
append history, reproduce the corpus, validate ontology labels and rebuild
affected semantic-map/site inputs before full QC. Coordinate #1217/#1218
without bypassing freshness. The layer-specific issue #1245 remains distinct.

## Additional Notes

All 431 returned open/closed issues, including comments, were searched for
this source key and Lentic path. #1245 covers a descendant hypolimnion edge,
not this source's own mapping and material parent. Official OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No curation or generated-product change was made.
