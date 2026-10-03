# YAML Record Review: alkaline hot spring

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/terrestrial/alkaline_hot_spring.yaml`
- Started UTC: 2026-10-03T22:45:59Z
- Finished UTC: 2026-10-03T22:47:46Z
- Verdict: pass

## Target

Read the complete generated HabitatRecord: `ENVO:00002119`, alkaline hot
spring, TERRESTRIAL, EXACT, SEEDED. It has the ENVO definition, one PREGO
related plural synonym, two parents, one PREGO attestation, one observational
strain association and one seed event. The stem is pinned at
`data/habitats/PATHS.tsv:641`.

## Validation

- `just validate data/habitats/terrestrial/alkaline_hot_spring.yaml`: passed.
- `just validate-strict data/habitats/terrestrial/alkaline_hot_spring.yaml`:
  one file, zero errors.
- Structured comparison verified the sole PREGO taxon's ID, label, score,
  rank and candidate pool. Current NCBI resolves the strain ID/name directly.
- Current OLS verified the identity and both parent terms as non-obsolete.
- Fresh `just validate-products`: passed, 1,179 canonical pairs, one synonym,
  five configured exceptions, 2,054 no-adapter skips.
- Full branch `just qc` is running, not yet a completed receipt. Baseline
  `e12b8ca4b` has completed local and required head/queue QC from #1308:
  457 tests passed, three skipped, two dependency warnings; 85 valid history
  records, 3,206 strict-valid records, 32 overlays, exact corpus reproduction
  and current generated products. Final publication needs its own checks.

## Identity and Grounding

Current [ENVO identity](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_00002119)
matches `data/raw/ontology_terms.tsv:7215`: a spring with alkaline water
and geothermal heating. The record denotes the spring feature, not sampled
water, a temperature quality or the general alkaline environment.

Both parents are strictly broader: `ENVO:00000051`, hot spring
(`ontology_terms.tsv:6645`), and `ENVO:01001894`, alkaline spring
(`ontology_terms.tsv:9384`). The asserted edges are at
`ontology_subclass_edges.tsv:5317-5318`. The current definitions retain the
thermal and alkaline restrictions respectively, supporting both parents.
TERRESTRIAL follows the repository's ENVO ancestry-based categorisation;
it does not turn this spring feature into a water-material class.

The plural source synonym is correctly RELATED_SYNONYM. The decision key
is `habitatmech:PREGO.c4f27e48fe`; no target decision or authored definition
was found in the ignored-inclusive maintained-input search. Ordinary PREGO
self-grounding explains EXACT/SEEDED and the sole
2026-08-16T05:58:02Z source seed event. The definition's grammatical opening
is copied from current ENVO, not introduced by this record's generator.

## Evidence

`data/raw/prego_habitats.tsv:692` supplies one taxon, one direct assertion,
maximum score three, annotated_genomes_isolates and canonical/plural lexical
forms. `prego_habitat_taxa.tsv:6005` supplies the entire retained pool:
`NCBITaxon:480224`, Chloroflexus aurantiacus Y-400-fl, rank one, score
three, direct TRUE and no source corroboration. The record matches exactly.
Rank one out of one is source ordering, not abundance or habitat specificity.
No `is_characteristic` assertion is present.

Current [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=480224)
resolves the supplied strain ID/name directly and retains DSM 637 as a
synonym. The strain was not replaced with the related J-10-fl type-strain
record merely because a genome-paper search also returned that strain.

The inspected primary [DSMZ DSM 637 catalogue](https://www.dsmz.de/collection/catalogue/details/culture/DSM-637)
identifies Y-400-fl, cross-references ATCC 29364 and records alkaline-hot-spring
isolation in Yellowstone, Wyoming. Its stated cultivation conditions are
laboratory instructions, not habitat-wide temperature, oxygen or light values.

The inspected [BioProject PRJNA21119](https://www.ncbi.nlm.nih.gov/bioproject/21119)
description identifies the same Y-400-fl/DSM 637/ATCC 29364 isolate and
explicitly gives an alkaline-hot-spring origin. The current project organism
field uses species ID 1108; the description remains strain-specific and does
not invalidate the separately resolved strain ID 480224. These resources
describe the same isolate, not two independent isolation events. They support
the bounded occurrence without establishing prevalence, exclusivity or a
causal mechanism across alkaline hot springs.

The exact PREGO pair-level evidence URL is not retained in the local inventory
and was not recovered. The registry/catalogue checks corroborate the stated
isolate context; they are not proof of which particular upstream document
produced the PREGO row. Score three remains a source score, not a measured
probability or experimentally established habitat-wide effect.

## Completeness

Ignored-inclusive identifier, label, stem and minted-key searches covered
curation, history, research and prior reviews. No target decision, authored
term request, causal overlay, session-history record or earlier exact-target
review was found. A previous GOLD alkaline-leaf review mentions this adjacent
ontology concept but does not review this record or justify merging them.

Structured full-table scans found no exact-target match in 770 parameter
rows, 358 isolation-source grounding rows or 58 Madin habitat rows. Missing
optional parameters, graphs, discussions and record-level references are not
defects. The definition does not authorize inventing universal numerical
pH/temperature bounds from the isolate's cultivation data.

iModulonDB is not applicable: no gene, regulator, pathway or expression-module
claim is asserted by the record. Genome-resource links alone do not create
such a claim.

## Findings

None established: zero blockers, zero major and zero minor findings. Identity,
both parents, source-copying and the bounded strain occurrence are supported.
The unresolved exact PREGO evidence-row provenance limits the review; no
characteristic-taxon or habitat-mechanism claim has been certified.

## Recommended Edits

No required record edit is supported. Preserve the two parents and the
source-specific strain observation. Optional future enrichment must cite
specific field observations and use maintained curation inputs; do not
hand-edit generated YAML or substitute laboratory conditions for environmental
measurements. Any grammatical definition correction belongs upstream in ENVO
and a governed ontology refresh, not an isolated generated-file patch.

## Follow-up Checks

For any future change, verify the exact source pair and sample/strain scope,
run an affected seed canary and inspect the emitted record. Then run strict
validation, ontology correspondence, corpus reproduction, required history
validation, current-product checks and full QC. Keep the GOLD context-specific
alkaline leaf separate unless its full identity is independently established.

## Additional Notes

Synonym assertions on the broader hot-spring class are not inherited into
this record. The broader generated record was not reviewed here and requires
its own record-level assessment; no defect in it is established by this review.
Adversarial self-review correction on 2026-10-03T22:58:21Z
([#1311](https://github.com/CultureBotAI/HabitatMech/issues/1311)) removed
an unsupported assertion about that adjacent record. The target verdict and
single PREGO related synonym are unchanged.
No source input, generated habitat, prior report or history record changed.
No paid research or unsupported biological mechanism inference was used.
