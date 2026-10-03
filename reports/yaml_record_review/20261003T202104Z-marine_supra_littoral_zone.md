# YAML Record Review: marine supra-littoral zone

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_supra_littoral_zone.yaml`
- Started UTC: 2026-10-03T20:19:31Z
- Finished UTC: 2026-10-03T20:21:04Z
- Verdict: needs curation

## Target

Read the full generated HabitatRecord for `ENVO:01000124`, marine
supra-littoral zone: AQUATIC, CLOSE, REVIEWED, sole GOLD attestation and two
generated history events. `data/habitats/PATHS.tsv:777` pins the current stem.

## Validation

- `just validate data/habitats/aquatic/marine_supra_littoral_zone.yaml`: passed.
- `just validate-strict data/habitats/aquatic/marine_supra_littoral_zone.yaml`:
  one file, zero errors.
- Fresh `just qc` passed 455 tests (three skipped, two warnings), history,
  3,206-record strict validation, 32 overlays, curation floor, exact corpus
  reproduction and generated-site freshness. Its retired-URL/later stages
  are not yet confirmed complete at report finish.
- Current official ENVO class, definition, named parent and typed synonyms
  were inspected directly. No NCBI taxon, DOI or PMID occurs in the record.
- OAK identity checks remain required in CI; they do not validate the meaning
  of every parent or preserve typed synonym scopes automatically.

## Identity and Grounding

`ontology_terms.tsv:7624` and current ENVO agree on the identity and
definition: an elevated coastal area normally reached by spray or splash,
with exceptional seawater penetration under storm/high-tide conditions.
This is neither the intertidal zone nor an entire water body. AQUATIC is a
coarse source-derived grouping, not a claim of permanent submergence.

`curation/decisions.tsv:1734` is an ITEM REVIEW of
`habitatmech:GOLD.600724f138`, explicitly endorsing a CLOSE relationship for
`Environmental > Aquatic > Marine > Supratidal zone`. The record preserves
`skos:closeMatch` and the review event. The existence of similar spellings is
not permission to silently promote the reviewed source mapping to exact.

`ontology_subclass_edges.tsv:5774` and current OWL support the true parent
`ENVO:01001201` marine environmental zone. The generated additional
`ENVO:00001999` marine water body comes from the GOLD Marine path context,
not a valid is-a relationship. The whole-waterbody definition conflicts with
the target's coastal-zone meaning. Part-of and adjacency restrictions in
the OWL must not be converted to named superclasses.

## Evidence

`gold_ecosystem_paths.tsv:1554` has two nodes, 8047/8048, and zero organism,
study, biosample and total assertions. The record correctly uses the first
node, includes the two-node note, and omits a positive assertion count/unit.
An attested vocabulary concept with no counted observations is not itself a
broken reference or a reason to invent a taxon.

Structured exact-path scans included all 1,040 bulk biosample rows, 1,587 API
triad rows and 4,587 study rows and found no target match. A complete scan of
770 environment-parameter rows found no target term. No ecological sample
evidence is borrowed from adjacent intertidal or marine-water concepts.

The current ontology's synonym scopes do not match the generated scopes:

| ENVO synonym | Current OWL scope | Generated scope |
|---|---|---|
| marine supralittoral zone | exact | exact |
| supralittoral zone | broad | exact |
| splash zone | related | exact |
| spray zone | related | exact |
| supratidal zone | related | exact |

The separate capitalized GOLD source-label synonym retains source provenance;
it is not an ENVO assertion. `extract.py:_load_tsv_ontology` reads an untyped
synonym pipe; `seed.py:406-407` emits every ontology string as exact. This
explains one broad and three related scope inflations, not an error in the
genuinely exact spelling.

## Completeness

Ignored-inclusive searches by identifier, label, stem and source key covered
curation, history, research, prior reports and PATHS. They found the ITEM
decision, but no target-specific term request, causal overlay, research report,
authored session history or previous exact-target review. Empty optional
parameters, taxa, evidence, graphs, discussions and datasets are not automatic
defects. The existing decision and seeding history explain REVIEWED without
claiming that the present scientific findings were previously checked.

## Findings

1. **Major - HM-SUPRALITTORAL-001:** unsupported whole-waterbody parent.
   Owner: source-specific curation control and the second GOLD parent pass in
   `src/habitatmech/seed.py`. Tracked in
   [#1297](https://github.com/CultureBotAI/HabitatMech/issues/1297).
2. **Major - HM-SUPRALITTORAL-002:** one broad and three related ENVO
   synonyms are promoted to exact. Owner: governed typed ontology inputs,
   `src/habitatmech/extract.py` and `src/habitatmech/seed.py`. Added as a
   verified witness to [#1249](https://github.com/CultureBotAI/HabitatMech/issues/1249).

No blocker or minor finding was established.

## Recommended Edits

1. Suppress only the false GOLD parent contribution, retaining the marine
   environmental-zone parent, source path, zero-count semantics, CLOSE mapping
   and reviewed provenance.
2. Preserve typed ontology synonym assertions through extraction and emission.
   Keep the true exact synonym and separately sourced GOLD spelling; do not
   globally downgrade every synonym as a substitute for recovering scope.
3. Append actual session provenance when those maintained inputs/rules change;
   do not rewrite the old review event or generated YAML by hand.

## Follow-up Checks

Add exact-source parent and mixed-synonym-scope regressions, canary the
record, inspect preserved status/count fields, validate schema/OAK/provenance,
and verify corpus reproduction. Compare semantic-map inputs and rebuild any
changed map/site products in the supported runtime tracked by #1217; run full
QC before merging a curation fix. Draft #1218 remains unchanged. Neither issue
is fixed or closed by publishing this report.

## Additional Notes

Current [official ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl)
SHA256: `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
All 461 existing open/closed issues and returned comments were searched for
this target and source key before filing #1297. iModulonDB was not applicable:
no gene, regulator, strain-specific pathway or expression-module assertion is
present. No paid research or scientific input/product mutation was performed.
