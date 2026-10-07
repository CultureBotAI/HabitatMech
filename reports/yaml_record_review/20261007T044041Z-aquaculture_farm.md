# YAML Record Review: aquaculture farm

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/aquaculture_farm.yaml`
- Started UTC: 2026-10-07T04:38:04Z
- Finished UTC: 2026-10-07T04:40:41Z
- Verdict: needs curation (0 blocker, 2 major, 0 minor)

## Target

Read the complete generated HabitatRecord and rendered page. Identifier
`ENVO:03600074`, ENGINEERED / EXACT / REVIEWED. The record denotes an
aquatic cultivation ecosystem, with two contributing sources, an ENVO
definition, three synonym entries, two parents, 25 BacDive taxon associations
and three history events. No xref, parameter, literature-evidence object,
causal graph, discussion or dataset is asserted. This exact target is not
either separately minted GOLD Aquaculture record.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/aquaculture_farm.yaml`: passed.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/aquaculture_farm.yaml`: passed, one file, zero errors.
- Read-only `build_corpus()` / `build_document()` comparison reproduced every
  field: two source concepts, two reviewed sources, 25 taxa and three events.
  Actual source resolution routes were checked separately for both inputs.
- Full QC/OAK were not rerun per target. Scientific inputs/products remain
  at `43e6c5d0fb508bcbf7341b8ca5be0141a495f2ed`; reuse successful
  [exact-baseline QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37569153392),
  whose SHA and completed/success state were freshly checked in this
  continuation, for corpus, reference, history and generated-product gates.
  Primary ontology/taxonomy checks below do not certify original associations.
- Original GOLD/BacDive dump re-extraction was unavailable: this continuation's
  ignored-inclusive filename search of `build` and configured kg-microbe
  `data` found no corresponding node/edge TSVs or NCBI label dump. Full
  source counts are inventory-verified, not independently recomputed from
  all 109 strains or all 96 source taxa.

## Identity and Grounding

Fresh primary [ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
at master SHA `a2455d1a77e46bb8a664d65a157166b539269042` confirms the target
is active, with the same canonical label, complete cultivation-ecosystem
definition and direct named parent ENVO:00000077, agricultural ecosystem.
The local rows are `ontology_terms.tsv:10110` and
`ontology_subclass_edges.tsv:8508`; PATHS line 944 agrees.

BacDive source key `habitatmech:BACDIVE.6b8777930d` is ITEM REVIEW at
`curation/decisions.tsv:45`, preserving a CLOSE/skos:closeMatch route through
`isolation_source_groundings.tsv:24`. That source mapping is medium-confidence
lexical matching, not proof that its bare Aquaculture label is an exact synonym.
GOLD key `habitatmech:GOLD.add1edcd6d` is ITEM REVIEW at decision line 986,
preserving EXACT/skos:exactMatch through `gold_leaf_label`. Two reviewed
sources explain REVIEWED; the strongest source explains aggregate EXACT.
Neither status makes the BacDive source mapping exact.

Read both full local parent records. ENVO directly supports agricultural
ecosystem as a superclass. The other parent, ENVO:01000964 industrial
wastewater, is active and defined as a wastewater material with specified
industrial origin/contamination. It comes only from the GOLD prefix path,
whose automatic resolution is exact. A cultivation ecosystem is not a kind
of that water material. The parent record's additional content is not being
independently curated in this target review.

## Evidence

Structured scans covered all 14 raw TSVs. A broad source-label scan also
matched unrelated Aquaculture paths and exceeded output limits; a fresh
exact-ID/source-key/full-path scan recovered all target rows without relying
on truncated output.

- `bacdive_isolation_sources.tsv:68` records 109 strains and 96 taxa.
  All 25 retained rows at `bacdive_source_taxa.tsv:114-138` reproduce with
  counts 3, 3, nine 2s and fourteen 1s, totaling 38 retained strain
  associations. Each pool is 96; the top-25 sum is not the full source count.
  No corroboration or characteristic-taxon claim is asserted.
- `gold_ecosystem_paths.tsv:1393` records the exact path
  `Engineered > Wastewater > Industrial wastewater > Aquaculture farm`,
  nodes `gold.ecosystem:7856|gold.ecosystem:7857`, and zero organism/study/
  biosample counts. The first-ID note and omitted positive count/unit are
  correct, not evidence of biological absence.
- `gold_path_biosamples.tsv:788` independently reports four bulk biosamples.
  `gold_studies.tsv:4304` links Gs0159290 to this and two other paths,
  WWTP effluent and river. The specific
  [GOLD study page](https://gold.jgi.doe.gov/study?id=Gs0159290) was
  inaccessible through web retrieval. Its live contents, facility-versus-
  effluent sample scope and crosswalk to counted organisms remain unverified.
- The triad hit at `gold_path_triads.tsv:5` uses this ENVO class as broad
  context for a different Crustaceans pond > Sediment path. It is not an
  aquaculture-farm parameter, identity assertion or additional target source.

Fresh NCBI Taxonomy efetch verified all 25 retained IDs and every scientific
name, with no alias or mismatch: 21 species, one subspecies and three
strains. Counts/ranks are BacDive association statistics, not microbial
abundance or taxonomic rank. These identity checks do not independently
reconstruct the original ecological observations.

Primary ENVO explicitly marks both `aquaculture` and `aquafarming` as
BROAD synonyms, with no exact synonyms for this class. The generated record
instead calls both exact. Its capitalized BacDive Aquaculture alias is also
exact despite the retained closeMatch and lack of separate exact lexical
evidence. An activity or practice label should not automatically collapse
to its associated physical cultivation ecosystem.

## Completeness

Ignored-inclusive ID, label, slug and both source-key searches covered
curation, history, configuration, docs, tests, research, the research
manifest, PATHS and RETIRED; filename searches covered curation/history/
research. No target-owned authored definition, causal overlay, parent
exclusion, separate history session or research file was found in those
bounds. Related host/algal research mentions are not independent evidence
for the target source merge. Existing ITEM decision rows are present.

No target environmental-parameter or PREGO/Madin contribution appeared in
the raw scans. Empty mechanism and parameter slots are not defects by
themselves. iModulonDB is not applicable to these habitat association claims:
no gene, regulator, expression dataset or mechanism is supplied to test.

The source-name ambiguity must remain visible. If GOLD means wastewater
from an aquaculture facility, its exact farm identity may need separate
curation; the unavailable study does not establish that conclusion. If it
means the farm setting, the water ancestor is context only. Either way,
the current global farm-is-wastewater assertion is unsupported.

## Findings

1. **Major: an ecosystem is asserted to be a wastewater subtype.** The
   ENVO definitions distinguish farm ecosystem from industrial wastewater
   material, but the immediate GOLD path contributes ENVO:01000964 to the
   merged farm's `parent_habitats`. The schema requires strictly broader
   habitats, not source, output or sampling context. Maintained owner:
   `curation/gold_parent_exclusions.tsv`; any later source-identity revision
   belongs separately in `curation/decisions.tsv`.
2. **Major: ontology and source synonym scopes are inflated.** Both ENVO
   broad synonyms are emitted exact, and BacDive's close-mapped Aquaculture
   label is independently promoted to exact. Maintained owners: governed
   typed ontology extraction and source-synonym handling in
   `src/habitatmech/seed.py`, corresponding to the existing #1249 and #1459
   contracts. Counted as one record-level lexical-scope finding, not three
   independent scientific defects.

No blocker or minor finding was established. The ontology identity itself,
definition, supported agricultural superclass and retained taxon labels agree.

## Recommended Edits

In separately authorized curation, exclude the unsupported immediate GOLD
parent using key `habitatmech:GOLD.add1edcd6d`, its exact wastewater/farm
path and expected parent ENVO:01000964. Retain the independently supported
ENVO:00000077 parent. Preserve original source paths, separate count units,
taxa and existing review accounting; append attributed session history.
Resolve the exact GOLD sample meaning before deciding whether to retain
the farm identity or create a distinct farm-wastewater concept.

Recover the verified broad ENVO synonym scopes through governed inputs.
Give the close-mapped BacDive alias justified weaker scope or retain it only
as source provenance; do not globally downgrade verified exact aliases or
change closeMatch to exactMatch to silence the inconsistency. The recent
GOLD strict-ancestor synonym guard does not fix either mechanism here.
No invented definition or causal graph is needed for these repairs.

## Follow-up Checks

Regress the guarded parent exclusion while retaining the ontology parent,
all 25 taxon rows, the 109-strain count and each source predicate. Regress
the two typed broad synonyms and the close-mapped source label independently
of genuinely exact synonyms. Run `just seed`, inspect
`just seed-canary ENVO:03600074 --force`, then authorized regeneration,
provenance, strict validation, `just verify-corpus`, `just validate-products`,
history/site checks and `just qc`. Compare semantic-map inputs and rebuild
if parent removal or identity changes alter them. Verify source scope before
any future split, not merely the lexical farm match.

## Additional Notes

Only this new report was authored for the target. No scientific edits,
review-status changes, history writes, paid research or GitHub mutation
occurred. The all-record goal remains active.
