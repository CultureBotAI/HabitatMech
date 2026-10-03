# YAML Record Review: freshwater river

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/freshwater_river.yaml`
- Started UTC: 2026-10-03T08:55:26Z
- Finished UTC: 2026-10-03T08:56:14Z
- Verdict: needs curation

## Target

The complete generated `HabitatRecord` denotes `ENVO:01000297`, freshwater
river, with category `AQUATIC`, grounding `EXACT`, and mapping `SEEDED`.
Its GOLD source concept is `habitatmech:GOLD.b9a8cb85e1`, derived from
`Environmental > Aquatic > Freshwater > River`. The slug is pinned at
`data/habitats/PATHS.tsv:827`. Baseline:
`3cfdfff350ad925214be41e08836ad2783d0ef80`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/freshwater_river.yaml` | Pass; no issues found |
| `just validate-strict data/habitats/aquatic/freshwater_river.yaml` | Pass; one record, zero errors |
| Live OLS checks | Target label/definition and two ontology parents match; all relevant terms active |
| Full `just qc` | Running for this report-only branch at individual-review completion; final result belongs to the batch PR |

Full OAK label validation was not repeated for this report; relevant terms were
checked directly. No taxon, literature citation, or causal graph occurs here.
Schema validation does not establish that every source hierarchy is is-a.

## Identity and Grounding

The composed source label freshwater river matches the ENVO identity. Its
definition in `ontology_terms.tsv:7800` agrees with the
[current term](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000297),
whose annotation calls it preliminary. This target is a freshwater watercourse,
not river water or river biome. The source-qualified alias River is retained
with GOLD provenance and should not erase that qualification in a merge.

`ENVO:00000022` river and `ENVO:03605007` freshwater stream are the two
direct ontology parents in both live OLS and
`ontology_subclass_edges.tsv:6014-6015`. The
[river definition](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000022)
describes a stream flowing along a channel, and the
[freshwater-stream definition](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03605007)
adds the low-solute water composition. Both are supported broader classes.

The third parent, `ENVO:00002011` fresh water, is instead water material.
It is added from GOLD's immediate Freshwater context, not by ENVO. A river's
water composition does not make the river itself a kind of liquid water.

## Evidence

| Claim | Inspected support | Assessment |
|---|---|---|
| Path, leaf, depth four, two source nodes | `gold_ecosystem_paths.tsv:69`, nodes 4511 and 4512 | Exact match; first-node display and note are correct |
| 521 ORGANISM assertions | Row 69's named `organism_count` | Correct; `study_count=0`, `biosample_count=0`, `total_assertions=521` are separate columns |
| Exact automatic grounding | Composed-label route in `resolve_gold` | Supported lexical identity, not an item review |
| 2,783 biosamples in a separate inventory | `gold_path_biosamples.tsv:16`, node 4512 | Different source coverage; not added to the organism count |
| Environmental roles | `gold_path_triads.tsv:380-382` | Broad freshwater river biome, local river, medium river water |
| `SEEDED` and single seeding event | No item decision; source-manifest timestamp | Accurate representation of review depth |

The triad cohort has 2,760 samples across 78 studies. Broad-scale river biome
has rounded share 1.00 but 77 agreeing studies and three distinct terms;
it must not be described as unanimous evidence. Local river has share 0.94
with 75 agreeing studies; medium river water has share 0.80 with 70.
The source study crosswalk contains 84 exact path memberships. These counts
have different coverage and are not interchangeable.

The triads independently distinguish the water body from its sampled material.
They supply no taxa or mechanistic edges. The path inventory has no genome
count column, and none is inferred.

## Completeness

Ignored/hidden-inclusive searches across `curation`, `history`, `research`,
`conf`, `data/raw`, `reports/yaml_record_review`, and the slug lock used the
record ID, minted source ID, label/slug, and exact GOLD path. No target item
decision, definition request, causal overlay, environmental-parameter row,
target-specific research report, or prior target review was found in those
locations. River-plankton decisions/research mention this river as context;
they concern a different source concept and do not endorse this target's
water-material parent.

The record has no taxa, environmental parameters, authored evidence, graphs,
discussions, or datasets. These optional omissions are appropriate to the
maintained inputs; 521 aggregate organism assertions do not supply taxon names.

## Findings

One major; zero blockers; zero minor.

**HM-FRESHWATER-RIVER-001 (major): fresh-water material is not a river parent.**
`src/habitatmech/seed.py:ingest_gold` promotes the parent source path into
an is-a claim to `ENVO:00002011`. The lake/river distinction from water material
is explicit in the inspected ontology definitions and the source triad roles.
Future curation should exclude only this contribution for
`habitatmech:GOLD.b9a8cb85e1`, preserving the river and freshwater-stream
parents. The maintained exclusion interface is proposed in draft PR #1218
and is not in this report baseline.

## Recommended Edits

1. Add the source-specific parent exclusion once its maintained interface is
   available. Do not alter the raw GOLD path or independent ontology parents.
2. An item-level decision may endorse the exact freshwater-river identity after
   review. It must not imply that every descendant's source-parent edge is is-a.
3. Preserve source-specific organism counts, source-node note, and status until
   actual curation is applied; do not invent organism or mechanism assertions.

## Follow-up Checks

Run `just seed` and `just seed-canary ENVO:01000297 --force`, then inspect
the two supported parents and unchanged 521-ORGANISM attestation. Run focused
schema/strict validation, `just validate-products`, and `just verify-corpus`.
Record the curation session, refresh the full semantic map for changed parent
text, then run `just render` and `just qc`. Inspect descendants separately
rather than transferring this target's verdict to them.

## Additional Notes

iModulonDB is not applicable: there are no gene, regulator, taxon, stress-
response, or expression-dataset claims. GOLD source facts were checked against
the committed inventories rather than an authenticated live query. No paid
research or generated-data edit was performed.
