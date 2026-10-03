# YAML Record Review: Glacier meltwater

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/glacier_meltwater.yaml`
- Started UTC: 2026-10-03T09:35:57Z
- Finished UTC: 2026-10-03T09:36:51Z
- Verdict: needs curation

## Target

Read the complete generated `HabitatRecord`, `habitatmech:GOLD.f3dc60ff11`,
category `AQUATIC`, grounding `UNGROUNDED`, mapping `SEEDED`. Baseline:
`be5b91732f2f75e7135a9cba05b385a361798847`. This is the Glacier meltwater
leaf beneath Ice, not the differently keyed Meltwater leaf beneath Glacier.
Its slug is pinned at `data/habitats/PATHS.tsv:3101`.

## Validation

- `just validate data/habitats/aquatic/glacier_meltwater.yaml`: pass.
- `just validate-strict data/habitats/aquatic/glacier_meltwater.yaml`: pass,
  zero errors.
- Exact source counters, biosample/triad rows, and study memberships parsed
  by named columns.
- Current OLS meltwater and liquid-water definitions and direct parents checked.
  Freshwater ice and the contextual lake/biome terms were checked earlier in
  this same batch.
- Shared full `just qc`: running at completion. Final outcome belongs to the
  PR. Full OAK validation was not repeated; the target has no literature
  references, taxa, or causal edges requiring separate evidence validation.

## Identity and Grounding

The exact path is
`Environmental > Aquatic > Freshwater > Ice > Glacier meltwater`.
The minted identity preserves glacier-origin specificity; no exact merge with
generic meltwater is warranted merely from the name.
`curation/decisions.tsv:1347` is a `CLASS`-depth `CONFIRM_UNGROUNDED` decision.
The separate sample-screen row at `curation/samples/class_swept_unscreened-20260814.tsv:40`
recognizes a real habitat but is not an item-level grounding decision.
The generated `SEEDED` status and class-history wording faithfully reflect
the maintained inputs.

The sole parent, `ENVO:01001511` freshwater ice, is wrong for liquid
meltwater. The [current meltwater term](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000722)
explicitly includes water released by melting glacial ice and has
`ENVO:00002006` liquid water as its direct parent. This agrees with
`data/raw/ontology_terms.tsv:8223` and `ontology_subclass_edges.tsv:6492`.
The verified [ice term](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001511)
denotes frozen water, not the liquid produced by melting it. Source origin
is not an is-a relationship to the original solid phase.

## Evidence

Named-column parsing of `data/raw/gold_ecosystem_paths.tsv:1472` gives depth 5,
one node (`gold.ecosystem:7784`), and zero organism, study, biosample, and
total assertion counters. The generated attestation correctly preserves the
source without inventing a positive count or a mapping predicate. The path
inventory has no genome-count column.

The separate `gold_path_biosamples.tsv:728` has six biosamples. Triad rows
305-307 cover six samples from one study, each with one distinct term and
sample share 1.00: broad = `ENVO:01000252` freshwater lake biome;
local = `ENVO:00000488` glacial lake; medium = `ENVO:01000722` meltwater.
The sole exact-path study membership is `Gs0118069` at
`gold_studies.tsv:1057`, which also names a different Liftoff microbial mat
path. That second path is not an additional study for this target.

The medium annotation corroborates the liquid-meltwater interpretation but
does not establish equivalence to all meltwater from snow, sea ice, and other
sources. The lake and biome slots remain context, not material identities.
Six biosamples do not contradict zero organism assertions: these inventories
measure different source cohorts. No authenticated live GOLD query was used.

## Completeness

Ignored/hidden-inclusive searches covered `curation`, `history`, `research`,
`conf`, `reports/yaml_record_review`, `data/raw`, and the slug lock using the
identifier, source node, exact path, slug, and glacier/glacial meltwater names.
They found the class decision and sample-screen row, but no item-level
decision, authored definition, target research report, causal overlay, or
prior individual target review there.

Empty optional taxa, parameter, graph, evidence, discussion, and dataset slots
are not defects to fill from generic cryosphere literature. The existing
broader meltwater concept can support a narrow grounding without inventing
an exact ontology identity or attaching lake-biome traits to the material.

## Findings

- **Major M1: meltwater is classified as its frozen precursor.** The
  `ENVO:01001511` parent contradicts the liquid-material meaning corroborated
  by the source label and medium annotation. A verified broader meltwater
  genus is available. Owners: the item row in `curation/decisions.tsv` and
  the maintained source-parent exclusion input proposed in draft PR #1218.

Zero blockers and zero minor findings.

## Recommended Edits

Make an evidence-backed item-level `GROUND_AS_PARENT` decision to
`ENVO:01000722` meltwater, retaining the minted glacier-specific identity.
Also exclude the immediate GOLD `ENVO:01001511` parent for this exact source:
adding the correct genus alone would leave the false solid-phase edge.
Preserve the raw path and distinct source counters. Let the seeder derive
grounding and review status from the maintained decision rather than setting
them in generated YAML.

## Follow-up Checks

Run `just seed` and
`just seed-canary habitatmech:GOLD.f3dc60ff11 --force`; inspect the whole
record and verify the meltwater parent, loss of only the false source parent,
unchanged minted identity, and decision-derived status/history. Add append-only
session history for curation. Run schema/strict validation, `just
validate-products`, `just verify-corpus`, required map refresh, `just render`,
and `just qc`. Do not merge the separate Meltwater source as a side effect.

## Additional Notes

iModulonDB is not applicable: there is no taxon, gene, regulator, or expression
dataset in this record. No paid research, generated-record edits, or status
promotion was performed by this review.
