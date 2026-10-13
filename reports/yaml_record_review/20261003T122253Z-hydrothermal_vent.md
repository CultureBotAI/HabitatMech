# YAML Record Review: hydrothermal vent

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/hydrothermal_vent.yaml`
- Started UTC: 2026-10-03T12:16:11Z
- Finished UTC: 2026-10-03T12:22:53Z
- Verdict: needs curation

## Target

The entire 568-line generated `HabitatRecord` and its maintained overlay were
read. The record is `ENVO:00000215`, hydrothermal vent, `AQUATIC`, `EXACT`,
`SEEDED`. It contains five source-qualified synonyms, two parents, four source
attestations, 12 parameter bands, 30 taxon entries, a 16-node/16-edge graph,
and four history events. `PATHS.tsv:525` locks the stem; the overlay is
`curation/causal_graphs/hydrothermal_vent.yaml`.

## Validation

- `just validate data/habitats/aquatic/hydrothermal_vent.yaml`: pass.
- `just validate-strict data/habitats/aquatic/hydrothermal_vent.yaml`:
  one file, zero errors.
- `just validate-causal curation/causal_graphs/hydrothermal_vent.yaml`: pass.
- Structured comparisons: all 12 complete parameter dictionaries and all 30
  taxon dictionaries match their raw inputs; graph and event match the overlay.
- Live OLS verified the identity, both parents, and marine vent/biome/fluid
  context. NCBI EFetch resolved all 30 taxa unchanged and all six cited PMIDs.
- Baseline `just qc`: all gates passed; 451 tests passed, three skipped,
  two dependency warnings; 3,206 schema-valid, reproducible records, 32 valid
  causal overlays, 78 valid history records, current site and redirects.
  OAK label correspondence is a separate network-backed CI gate.

## Identity and Grounding

The ENVO identity denotes a fissure discharging geothermally heated water;
its direct parent is `ENVO:00000027` spring. The second generated parent,
`ENVO:00001999` marine water body, instead denotes a lentic marine water body.
A fissure in that setting is not a subtype of the enclosing water body.
[Vent](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000215),
[spring](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000027),
[marine water body](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00001999).

The mint function reproduces GOLD `77ae835059`, PREGO `90a1d4d39e`, MADIN
`0dfc6681c9`, and ENVIRONMENTS_TABLE `7d9df340d1`. The first two have ITEM
decisions at `curation/decisions.tsv:710` and `:1473`; the latter two do not.
Thus `SEEDED` is correct. The ontology definition's typographical error and
PREGO's unusual related synonyms originate upstream, not in a local rewrite.

The marine GOLD path merits a future scope check against the active child
`ENVO:01000122` marine hydrothermal vent. The triad's local slot favors that
term, but this alone does not authorize changing the generic PREGO/Madin
identity or splitting the merged record. Preserve these source boundaries.
[Marine vent candidate](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000122).

## Evidence

### Source inventories

| Claim | Inspected support and limits |
|---|---|
| GOLD count/path | `gold_ecosystem_paths.tsv:64` has `Environmental > Aquatic > Marine > Hydrothermal vents`, two nodes 3776/4027, and 581 ORGANISM assertions. Showing the first node with a two-node note is correct. |
| Sample/study context | `gold_path_biosamples.tsv:93` separately has 348 samples; 42 `gold_studies.tsv` rows include the exact path. `gold_path_triads.tsv:497-499` covers 140 samples/31 studies, with marine vent biome, marine vent, and hydrothermal fluid in distinct broad/local/medium roles. These are not interchangeable identity or count claims. |
| PREGO and Madin | `prego_habitats.tsv:202` supplies 78 taxa, a separate 101-direct-assertion count, score 4, and two evidence channels. `madin_habitats.tsv:26` supplies 229 taxa. Generated units and counters agree. |
| Twelve parameters | `environment_parameters.tsv:306-317`, `water_marine_hydrothermal`, source context `therm`, supplies all emitted values. The multi-term marine-sediment rows at 147-158 are correctly excluded. |
| Thirty taxon entries | Twenty-five selected PREGO and 25 Madin entries overlap at 20 IDs. All generated labels, scores, ranks, pools, and corroboration match the raw columns; 25 entries are corroborated. None asserts `is_characteristic`. |

All 30 source taxon names match current NCBI names or aliases after
case/underscore normalization. Association is not measured abundance or a
claim that every listed organism performs the graph's metabolisms. In
particular, a hydrogen oxidizer need not be an autotroph.

The source's qualitative low-gradients/high-pH bands are not measured bounds
for every microenvironment. The graph's steep local mixing gradients are a
different evidence layer. Without an operational definition for the source's
gradient axis, their contrast is a scope question, not a proven numerical
contradiction. The dropped raw context relates to the existing parameter-
provenance work in #1229.

### Causal evidence

| Edge group | Verified support and limits |
|---|---|
| Geothermal heating, redox and thermal gradients, carbon fixation to primary production | Dick 2019, PMID:30867583, DOI:10.1038/s41579-019-0160-2: the inspected abstract supports deep-sea vent geochemistry, local variation, and chemosynthetic production. This is review evidence, not a new experiment. |
| Discharge, seawater mixing, reaction zone | Dick et al. 2013, PMID:23720658, DOI:10.3389/fmicb.2013.00124: full-text introduction explicitly describes reduced vent fluids mixing with oxidizing seawater. The mixing snippet occurs in the body, not the PubMed abstract. |
| Hydrogen supply, hydrogen-oxidizing organisms and metabolism | Adam and Perner 2018, PMID:30532749, DOI:10.3389/fmicb.2018.02873: full text describes geological variation, hydrogen use, and multiple evidence types. It also includes heterotrophic hydrogen oxidizers, so hydrogen use alone must not imply carbon fixation. |
| Sulfide supply, sulfur oxidation/carbon fixation, surface assemblages | Nakagawa and Takai 2008, PMID:18503548, DOI:10.1111/j.1574-6941.2008.00502.x: inspected introduction and distribution sections support reduced donors, chemoautotrophy, and free-living/episymbiotic contexts. The graph's surface-biofilm edge needs a more precise locator and bounded wording, not the two-word title fragment. |
| Sulfur-oxidizer distribution and metabolism | Meier et al. 2017, PMID:28375213, DOI:10.1038/ismej.2017.37: abstract describes sampled Manus Basin niches and inferred oxygen/sulfide controls. It does not establish sulfide alone as a universal sufficient cause of community selection. |
| Hydrogen oxidation and carbon fixation | McNichol et al. 2018, PMID:29891698, DOI:10.1073/pnas.1804351115: inspected PDF Results and Discussion and methods describe Crab Spa isotope-incorporation incubations, including hydrogen/nitrate amendments. Carbon fixation increased with the combined amendment; donor electron totals were inferred, not independently measured hydrogen-specific production fluxes. The paper supports a bounded example, not an abstract-only missing-evidence finding. |

Sources: [Dick 2019 abstract](https://pubmed.ncbi.nlm.nih.gov/30867583/),
[Dick 2013 full text](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2013.00124/full),
[Adam and Perner full text](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2018.02873/full),
[Nakagawa and Takai publisher text](https://academic.oup.com/femsec/article/65/1/1/619918),
[Meier abstract](https://pubmed.ncbi.nlm.nih.gov/28375213/),
[McNichol PDF](https://oceaniron.org/wp-content/uploads/sites/16/2019/11/McNichol-et-al-2018.pdf).
All 16 snippets were found in the corresponding title, abstract, or inspected
body text. Real references and exact title fragments do not themselves provide
claim-level localization. The attempted PDF screenshot timed out; the parsed
paper text, not unseen figure pixels, supports the assessment above.

The shared iModulonDB adapter's inspected 28 dataset rows contain no matching
named strain in this record. Mycobacterium sp. 141 is not interchangeable with
M. tuberculosis. No module evidence was transferred; this bounded lack of
coverage is not negative ecological evidence.

## Completeness

No generic gene list, numeric parameters, or characteristic-taxon status is
required. Hidden/ignored-inclusive searches covered curation, history,
research, configuration, raw inventories, path lock, and review reports using
ID, label, stem, full path, and source keys. They found the two decisions and
overlay, but no target term-request/session-history entry. Exact `Record:`
header coverage found no prior individual report, including ignored files.

## Findings

1. **Major: unsupported marine-water-body parent.** GOLD's marine context is
   emitted as a strictly broader parent of a vent fissure. Owner: GOLD parent
   linking in `src/habitatmech/seed.py`, or the maintained source exclusion
   mechanism proposed in draft #1218. Preserve the independent spring parent.
2. **Minor: graph types conflate guilds and places with taxa and cell states.**
   Sulfur- and hydrogen-oxidizing guilds are not organisms/clades as required
   by `TAXON`. A vent-seawater mixing zone and vent biofilms are not the
   bioenergetic/molecular cell states defined by `STATE`. Owner:
   `curation/causal_graphs/hydrothermal_vent.yaml`. Use supported capacities,
   bounded taxa, habitat contexts, or community processes and adjust endpoints
   and predicates accordingly; merely changing enum values is insufficient.
3. **Minor: claim localization and inference scope need tightening.** Title
   fragments obscure the actual supporting results. Explicitly bound the
   marine mixing scenario, condition-dependent niche selection, and Crab Spa
   amendment evidence. Do not remove the verified hydrogen/carbon-fixation
   support simply because it was absent from the abstract. Owner: same overlay.

Blockers: none. Total: one major, two minor.

## Recommended Edits

1. Exclude only GOLD `habitatmech:GOLD.77ae835059`'s unsupported water-body
   contribution, retaining its path/count and independent ontology parents.
2. Correct graph endpoint semantics and attach short exact supporting passages
   with locators and conditional notes. Keep guild membership distinct from
   autotrophy and avoid universalizing the marine mechanism.
3. Assess the marine GOLD grounding separately if better source scope is
   obtained; the triad is contextual evidence, not an automatic exact mapping.
4. Append session history for any actual curation and regenerate via the seeder.

## Follow-up Checks

Run focused schema/strict/overlay validation, `just validate-causal-all`,
`just validate-history`, and `just verify-corpus`. Compare non-graph and
non-hierarchy fields before/after their respective fixes. Graph-only changes
do not alter semantic-map input, but prove that with `just text-map-inputs`
and render the site. Hierarchy/identity changes require the pinned complete
map rebuild tracked in #1217 and, for grounding, OAK label correspondence.
Pass full QC and blocking CI before merge.

## Additional Notes

The review itself edits neither the generated record nor its mapping status.
An initial ad hoc study counter used an incorrect column name; rerunning with
the actual `paths` field produced the 42 exact-path rows above. This was not a
record defect or a failed project validator.
