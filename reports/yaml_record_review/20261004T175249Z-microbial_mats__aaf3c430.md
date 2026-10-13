# YAML Record Review: Microbial mats

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/microbial_mats__aaf3c430.yaml`
- Started UTC: 2026-10-04T17:50:49Z
- Finished UTC: 2026-10-04T17:52:49Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.b3e7b4ce80, Microbial mats,
AQUATIC, NARROW/REVIEWED. It has two parents, one GOLD attestation with nine
ORGANISM assertions and skos:narrowMatch, and two history events. Definition,
synonyms, xrefs, parameters, taxa, citations, graphs, discussions, datasets
and replacement links are not emitted.

The exact gold.ecosystem:4028 path is
`Environmental > Aquatic > Marine > Hydrothermal vents > Microbial mats`.
The actual mint matches; PATHS.tsv:2607 pins this stem. The target is the
microbial structure, not the hydrothermal vent, its biome, fluid or sediment.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/microbial_mats__aaf3c430.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/microbial_mats__aaf3c430.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared fresh run PASS: 1,179 canonical pairs, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Terminal PASS: 457 tests, three skipped, two warnings in 763.06 seconds; 90 history records, 3,206 strict records, 32 graph curations, exact reproduction and all site/redirect/term-request and remaining gates passed. |
| Source/reference checks | Full target, ITEM row, structured scan of all 14 raw TSVs, actual resolver, typed OWL/current OLS, all ten study retrieval attempts and full page/semantic comparisons inspected. |

Identifier-label validation does not certify downstream SSSOM/KGX modeling;
no export execution or observed export failure is claimed.

## Identity and Grounding

`curation/decisions.tsv:1018` is a genuine ITEM GROUND_AS_PARENT decision
dated 2026-08-12, using ENVO:01000008 microbial mat. The retained identity,
true generic mat parent, REVIEWED state and two events follow it. The
separate ENVO:01000157 denotes mat-derived material, not intact mat identity;
both were verified against official typed ENVO/current OLS in this batch.

Current [ENVO:00000215 hydrothermal vent](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000215)
is a fissure releasing geothermally heated water, with named parent spring.
A mat at the vent is not a kind of fissure or spring. The source path supports
that setting, not the currently asserted strict broader identity.
Substituting the more specific marine vent would not resolve the type error.

Current [ENVO:01000122 marine hydrothermal vent](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000122)
is a vent feature located in the marine realm; ENVO:01000030 is the
marine hydrothermal vent biome. The local feature, broad biome, microbial
structure and sampled material remain distinct entities and roles.

## Evidence

Physical `gold_ecosystem_paths.tsv:540` gives this depth-five path, one
node, nine organisms, zero study/biosample counters and total nine. The
emitted count/unit is faithful. `gold_path_biosamples.tsv:284` independently
gives 75 bulk samples. Triad rows 506-508 cover 74 complete-triad samples
across nine studies:

| Role | Top term | Share | Distinct terms | Agreeing studies |
| --- | --- | ---: | ---: | ---: |
| Broad | ENVO:01000030 marine hydrothermal vent biome | 1.00 | 1 | 9 |
| Local | ENVO:01000122 marine hydrothermal vent | 0.62 | 3 | 8 |
| Medium | ENVO:01000157 microbial mat material | 0.97 | 3 | 7 |

Local and medium annotations are heterogeneous. Agreement counts refer to
studies containing the top term, not proved experimental independence or
unanimous annotation within each study. No inspected exact-sample crosswalk
establishes the 74 API samples as a particular subset of the 75 bulk samples.

Ten exact study memberships were inspected:

| Physical row in gold_studies.tsv | Accession | Path count |
| --- | --- | ---: |
| 407 | Gs0072209 | 2 |
| 1218 | Gs0118692 | 1 |
| 1370 | Gs0121629 | 1 |
| 1407 | Gs0127394 | 2 |
| 1451 | Gs0127575 | 1 |
| 1499 | Gs0128946 | 2 |
| 1566 | Gs0129088 | 7 |
| 1574 | Gs0129113 | 3 |
| 1997 | Gs0133538 | 1 |
| 3576 | Gs0151908 | 2 |

All ten original GOLD study-page requests returned 403. The committed
memberships are verified, not the current experimental contents. Ten
memberships are not the nine-study API cohort, and path counts are not
organisms or samples. Mixed freshwater paths in Gs0129088, Diffuse flow in
Gs0128946 and Black smokers in Gs0151908 do not characterize every mat.
The complete 14-table scan found no exact-target parameter, PREGO or BacDive
taxon row. No universal thermophily, sulfur metabolism or deep-sea location
is inferred from the branch label or generic vent knowledge.

Current official GOLD node 4028 is active and matches the full source path.
Its complete vocabulary annotations are marine biome, hydrothermal vent and
ENVO:01000008 microbial mat. Those vocabulary roles differ from the samples'
more specific vent-biome/marine-vent/mat-material roles and are not a new
sample cohort or proof of class identity.

The actual complete normalized-table resolver gives default
gold_unmatched/UNGROUNDED/no predicate. Applying the ITEM row gives
curated_ground_as_parent_from_gold_unmatched, NARROW, skos:narrowMatch,
extra parent ENVO:01000008 and reviewed=True. The route is `seed.py:554-566`,
applied at `:839-843`; the separate GOLD parent pass at `:898-907` adds
the false vent parent. `:890-891` emits the predicate.

Schema `habitatmech.yaml:317-322` and `:776-790` declare source/record
comparisons, while this route compares the retained identity with an ontology
parent. The latter is not the attestation's declared target. This reproduces
#1398's endpoint contract defect, not a formal SKOS inconsistency. Reversing
the predicate alone is insufficient.

## Completeness

Ignored-inclusive exact ID/key, node/path and stem searches covered curation,
history, research, reports, PATHS and RETIRED. Separate hydrothermal-label
and filename searches found parent/adjacent artifacts, not a target-owned
definition, overlay, dedicated research, session history, retirement or prior
individual target report. The ITEM row and path lock exist.

The inspected overlay header `curation/causal_graphs/hydrothermal_vent.yaml`
targets ENVO:00000215 and explicitly scopes its mechanism to a marine setting;
it is not attached to this mat and must not be copied as universal evidence.
No claim to a full new review of that parent graph is made. Optional missing
fields are not defects; iModulonDB is inapplicable without a gene, regulator
or expression dataset claim.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | The vent-associated mat inherits the vent fissure as a strictly broader habitat. | GOLD parent pass or governed exclusion for GOLD.b3e7b4ce80 and expected parent ENVO:00000215, #1397. |
| Major | Curated NARROW/skos:narrowMatch use ontology-parent endpoints inconsistent with declared source/record semantics. | Resolver, attestation emitter, schema and consumers, #1398. |

Counts: zero blockers, two major, zero minor. Mat identity, genuine generic
parent, nine-ORGANISM count, ITEM review and event derivation remain sound.

## Recommended Edits

1. Exclude only the false vent context-parent contribution. Preserve
   ENVO:01000008, source mint/path/node/count and actual review history;
   do not replace it with a marine-vent feature or import the parent graph.
2. Reconcile mapping endpoints and grounding meaning across actual routes,
   preserving distinct source mats and legitimate imported mappings.
3. Add exact-edge/source-preservation and mapping-contract regressions,
   append required correction history and regenerate through maintained inputs.

## Follow-up Checks

After correction run `just seed`, then
`just seed-canary habitatmech:GOLD.b3e7b4ce80 --force`. Inspect the complete
canary, nine-ORGANISM count, true mat parent, REVIEWED derivation and prior
events plus required correction history before `just seed-apply --force`.
Never prune partial runs. These are future commands, not executed review edits.

Require ordinary/strict validation, labels, source/history and consumer tests,
`just verify-corpus` and `just qc`. The actual page lists hydrothermal vent
as a Broader habitat. Removing only that parent in the full-context semantic
adapter removes `broader habitat: hydrothermal vent`; a scientific repair
needs genuine map/site refresh under #1217. Predicate-only omission was
separately text-neutral. Preserve #1218 and runtime pins; audit actual
SSSOM/KGX products before claiming compatibility.

## Additional Notes

All-state exact-key and hydrothermal/mat issue searches returned no matches.
Extend the separately inspected shared #1397/#1398 contracts with this
independent witness; do not duplicate issues or close them after publication.

Official typed ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific record/input, generated product, prior report/history or paid research changed.
