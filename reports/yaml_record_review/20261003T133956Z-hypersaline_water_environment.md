# YAML Record Review: hypersaline water environment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/hypersaline_water_environment.yaml`
- Started UTC: 2026-10-03T13:38:23Z
- Finished UTC: 2026-10-03T13:39:56Z
- Verdict: needs curation

## Target

Read the complete generated `HabitatRecord`, `ENVO:01001043`, hypersaline water
environment: `AQUATIC`, `CLOSE`, `REVIEWED`, with an ENVO definition, one GOLD
synonym, two parents, one attestation, and two history events. No taxa,
parameters, citations, or graph are present. `PATHS.tsv:878` locks the stem.
This environment is not the material `ENVO:00002012` or lake `ENVO:01001020`.

## Validation

- `just validate data/habitats/aquatic/hypersaline_water_environment.yaml`: pass.
- `just validate-strict data/habitats/aquatic/hypersaline_water_environment.yaml`:
  one record, zero errors.
- The mint function reproduces GOLD source key `habitatmech:GOLD.4398c0543d`.
- Live OLS responses verified the active identity and saline-water-environment
  parent. Structured source TSVs were parsed, including pipe-separated study
  paths rather than substring approximations.
- Full QC is verified successful on unchanged base
  `ce53c21e8be841478dfdc730cef28ad2ca4bf462`,
  [run 37125963812](https://github.com/CultureBotAI/HabitatMech/actions/runs/37125963812).
  This reuses the baseline corpus/schema/history/site gates; semantic validity
  of an inherited source-path edge is not established by schema success.

## Identity and Grounding

The ID and ENVO definition agree: this is a system determined by hypersaline
water. Its current direct parent is `ENVO:01000307` saline water environment,
matching `ontology_subclass_edges.tsv:6843`. Neither definition restricts the
system to inland water.
[Hypersaline water environment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001043),
[saline water environment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000307).

`curation/decisions.tsv:459` explicitly maps the non-marine GOLD Hypersaline
bin to that identity with `CLOSE` and ITEM depth. The emitted predicate,
status, and history faithfully record the decision; `REVIEWED` is not a
guarantee that the decision's hierarchy is scientifically sound.

The extra parent `habitatmech:GOLD.ce244e62cd` is explicitly **inland** saline
or alkaline aquatic environment (`curation/term_requests.tsv:43`). The full
parent record was read. It is compatible with the GOLD bin's context, but not
strictly broader than the global ENVO identity. Transferring the source-path
context onto that identity makes all marine hypersaline-water environments
inland, which is false. The material's salinity does not determine geography.

## Evidence

`gold_ecosystem_paths.tsv:115` has the exact path
`Environmental > Aquatic > Non-marine Saline and Alkaline > Hypersaline`,
219 ORGANISM assertions and nodes `3754|3978`; the display names the first
with an accurate two-node note. This is not the separate Hypersaline lake
path with 115 organisms.

The exact-path biosample crosswalk has 179 biosamples under path ID 3978.
The independently derived API triad inventory covers 143 complete-triad
samples from 33 studies: broad scale
is aquatic biome, local-scale plurality is hypersaline lake (0.48 share),
and medium plurality is hypersaline water (0.48 share). The study inventory
contains this path in 42 studies. These different units and coverage levels
must not be summed or substituted for the 219-organism attestation. The
triad roles do not establish an exact lake or material identity for the bin.
`GOLD_MANIFEST.yaml` identifies the bulk-export versus API origins; the API
rows have not been proved to be a strict subset of the bulk-export samples.

Primary work on Atlantis II and Discovery in the Red Sea describes marine
hypersaline water columns and salinity-related environmental structuring.
These are concrete counterexamples to an inland-only superclass for the
global environment. This is a semantic inference from the inspected ENVO
definition and study, not an asserted ENVO subclass edge or a claim that those
sites are among this record's GOLD organisms.
[PMID:23542623, structured abstract inspected](https://europepmc.org/article/MED/23542623).

The parent research report itself contains conflicting shorthand: one table
calls the hypersaline environment narrower, while its later comparison
recognizes overlap and marine examples. That generated research prose is a
lead, not authority that overrides the definitions or inspected primary study.

## Completeness

Ignored-inclusive searches of ID, source key, label, and stem covered curation,
history, research, configuration, source inventories, path lock, and review
reports. They found the ITEM decision and parent research, but no target
term request, graph overlay, standalone session history, PREGO/Madin/parameter
association, or prior exact-target review. Optional mechanisms and taxa must
not be copied from the adjacent hypersaline-water record. iModulonDB is not
applicable: there is no gene, pathway, regulator, or organism-specific claim.

## Findings

1. **Major: inherited inland context is not a superclass of the ENVO identity.**
   The source-path pass in `src/habitatmech/seed.py` contributes
   `habitatmech:GOLD.ce244e62cd` after `curation/decisions.tsv:459` assigns the
   general ENVO identity. The two scopes must be reconciled without weakening
   `parent_habitats` into a contextual relation. Owner: maintained source
   decision and source-parent controls, not generated YAML.

Zero blockers, one major finding, zero minor findings.

## Recommended Edits

Assess whether the source bin should retain a minted inland identity with the
general hypersaline-water environment as a broader parent, or whether the
current ontology identity should remain with the unsupported inland edge
excluded. Preserve `source_path`, all source IDs/counts, and the bounded
mapping rationale. Reassess the exact-synonym treatment as part of that scope
decision; do not relabel the source as universally identical merely because
it is water-associated.

The maintained source-parent-exclusion work in draft #1218 is relevant to the
second option; it is not merged and is not a completed fix for this record.
Any change needs append-only history and a complete regenerated product chain.

## Follow-up Checks

Recheck the full GOLD bin and triad roles before choosing an identity model.
Add a regression rejecting the false inland parent on the global ENVO class,
canary the seeder, inspect all affected descendants, and validate corpus,
ontology correspondence, semantic-map/site freshness, history, and full QC.
The map-rebuild dependency recorded in #1217 must not be bypassed by shipping
stale generated products.

## Additional Notes

No corpus, input, history, or generated artifact was changed. All 416 returned
open/closed issues were searched for the exact ID, source key, and label; no
existing issue for this particular hierarchy finding was found.
