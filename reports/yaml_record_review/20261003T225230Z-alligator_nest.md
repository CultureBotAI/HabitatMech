# YAML Record Review: Alligator nest

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/terrestrial/alligator_nest.yaml`
- Started UTC: 2026-10-03T22:48:32Z
- Finished UTC: 2026-10-03T22:52:30Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord for `habitatmech:GOLD.0cd2784356`,
Alligator nest: TERRESTRIAL, UNGROUNDED, SEEDED. It has no definition,
one parent, one GOLD source attestation without a positive assertion count,
and two history events. `data/habitats/PATHS.tsv:1371` pins its stem.

## Validation

- `just validate data/habitats/terrestrial/alligator_nest.yaml`: passed.
- `just validate-strict data/habitats/terrestrial/alligator_nest.yaml`:
  one file, zero errors.
- Current OLS verified the existing superclass and the specific candidate
  `ENVO:03600069`; both are non-obsolete and already in the vendored slice.
- Fresh batch `just validate-products` passed: 1,179 canonical pairs,
  one synonym, five configured exceptions, 2,054 no-adapter skips. This gate
  does not find every missed exact grounding for a minted identifier.
- Full branch QC remains running. Baseline `e12b8ca4b` passed local and
  required head/queue QC in #1308: 457 tests passed, three skipped, two
  dependency warnings; 85 valid history records, 3,206 strict-valid records,
  32 overlays, exact corpus reproduction and current generated products.
- A read-only semantic-adapter probe confirmed that applying the expected
  canonical label and definition changes semantic text. This was not a
  seeded candidate, scientific edit or completed product rebuild.

## Identity and Grounding

The source path unambiguously denotes the constructed nest, not the alligator
taxon, an anatomical site or merely a surrounding wetland. The current parent
`ENVO:00005803` is animal habitation, not a taxon; its label/definition at
`data/raw/ontology_terms.tsv:7494` and current OLS support that broader link.
The GOLD source places this structure under Terrestrial > Nest, consistently
with the emitted category.

The missed exact term is [ENVO:03600069, nest of alligator](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_03600069).
Current OLS and physical `ontology_terms.tsv:10105` describe the plant and
decomposing-vegetation habitation built by alligators for their eggs.
`ontology_subclass_edges.tsv:8503` places it under the same animal-habitation
parent. It is neither a merely broader lexical match nor a new term requiring
an ontology release update: the exact candidate is already committed here.

`curation/decisions.tsv:170` still records CLASS-level CONFIRM_UNGROUNDED,
dated 2026-08-12, because the lexical sweep found no label match and did not
assess habitat status. That explains SEEDED and both generated events, but
does not justify retaining an ungrounded identity after item-level inspection
finds this existing term. A new authored definition for the minted concept
would duplicate an available ontology identity rather than solve the gap.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:1616` supplies the exact canonical path
and nodes 4840/4841. Its organism, study, biosample and total-assertion
columns are zero. The record correctly emits the first node, two-node note,
full path and no positive count; zero here is not evidence of an empty or
nonmicrobial habitat.

Separate bulk inventories report 35 biosamples for path 4841 at
`gold_path_biosamples.tsv:406`, and study Gs0145185 with this sole path at
`gold_studies.tsv:2874`. Structured scans covered all 2,562 path rows,
1,040 biosample rows, 4,587 study rows and 1,587 triad rows. No exact-target
triad was found. These different snapshots and units do not justify summing
35 samples and one study into an organism assertion count. The live GOLD
study page failed to load, so its current sample-level contents are not claimed
as independently inspected evidence.

The inspected [Texas Parks and Wildlife nest description](https://tpwd.texas.gov/huntwild/wild/species/alligator/nest/index.phtml)
describes a constructed accumulation of decaying vegetation and mud for
eggs. This supports the specific ontology meaning; it does not make the
nest identical to the animal or to all water and soil around the nest.

The publisher abstract of [Grajal-Puche et al., DOI:10.1007/s00248-020-01522-9; PMID:32424717](https://link.springer.com/article/10.1007/s00248-020-01522-9)
was inspected. The published study compares bacterial assemblages across
eight compartments within and near American-alligator nests, 18 nests and
four sites. It supports microbial habitat status, but not a universal taxon
list or a direct causal mechanism for every alligator nest. Nearby water and
other sampled compartments must not be silently equated with the nest itself.
Only the abstract was accessible; no full-text methods/results inspection is
claimed. Counts from an earlier thesis/search lead were not substituted for
the published study's counts.

## Completeness

Ignored-inclusive identifier, label, stem and candidate-term searches covered
the ontology slice, source inventories, maintained curation, history, path and
retirement maps, research and prior reviews. They found the exact ontology
candidate but no target term request, causal overlay, session-history record,
prior exact-target report or separately emitted `ENVO:03600069` habitat.
The August CLASS decision predates the September history-layer adoption;
no retroactive session-history violation is asserted.

Missing taxa, parameters, graphs and record-level references are optional and
not automatic defects. The consequential gap is the missed specific grounding,
with the missing canonical definition as one consequence. iModulonDB is not
applicable because no gene, regulator or expression-module claim is asserted.

## Findings

1. **Major - HM-ALLIGATOR-NEST-001:** an existing, fitting ontology identity
   is missed while the record remains class-swept and ungrounded. Owner:
   the source-specific decision at `curation/decisions.tsv:170`, followed by
   guarded regeneration, not direct edits to this generated record.
   [#1310](https://github.com/CultureBotAI/HabitatMech/issues/1310).

No blocker or minor finding established. The existing animal-habitation
parent and GOLD source provenance are sound and should be retained.

## Recommended Edits

1. Replace the source decision with evidence-backed ITEM-level GROUND to
   `ENVO:03600069`, verified label `nest of alligator`. Preserve the source
   path/node provenance and true broader parent. Do not create a redundant
   novel-term request or ground the habitat to an alligator organism term.
2. Append session provenance and run a guarded canary; inspect the emitted
   identity, definition, status, hierarchy and affected source relationships.
   Preserve published URLs through the normal retirement/redirect workflow.
3. Rebuild affected semantic and site products using the governed runtime.
   The expected label/definition update changes adapter text; #1217 remains
   relevant to obtaining a supported inference environment. Do not bypass
   freshness checks, fabricate map values or leave stale pages.

## Follow-up Checks

Add a regression for this missed lexical-order variant and its item-level
grounding. Run `just seed`, an affected `just seed-canary`, strict validation,
`just validate-history`, `just validate-products`, corpus reproduction,
semantic-product validation, normal rendering, redirect checks and full QC.
Inspect the complete identity/URL diff and preserve distinct source units.
No inference that the 35 samples represent 35 independent taxa is warranted.

## Additional Notes

All 470 GitHub issues in all states and their returned comments were searched
for the source key, exact term and nest label before filing #1310. Generic
backlog #108 covers class-swept habitat assessment but not this concrete exact
grounding. No curation or generated-file correction is claimed by this review.
The semantic probe modified only an in-memory copy; no map was rebuilt.
No paid research ran. The PubMed browser view returned a challenge page;
the inspected publisher abstract supplied the bounded study evidence.
