# YAML Record Review: Storm water pond

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/storm_water_pond.yaml`
- Started UTC: 2026-10-06T08:56:54Z
- Finished UTC: 2026-10-06T09:04:34Z
- Verdict: needs curation

## Target

Read the complete generated `HabitatRecord`: habitatmech:GOLD.2d1d06f93f,
Storm water pond, AQUATIC, UNGROUNDED, SEEDED. `PATHS.tsv:1618` pins this
stem. Its one GOLD attestation is node 8518, Environmental > Aquatic >
Freshwater > Pond > Storm water pond. The sole parent is ENVO:00000033
pond. Count/unit, definition, synonyms, xrefs, parameters, taxa, evidence
and causal graphs are absent. Two historical events record a CLASS-level
ungrounded decision and subsequent seeding.

## Validation

- Fresh `just validate data/habitats/aquatic/storm_water_pond.yaml`: passed.
- Fresh `just validate-strict data/habitats/aquatic/storm_water_pond.yaml`:
  one file, zero errors.
- Full actual `build_corpus` / `build_document` equality passed: one source,
  zero reviewed sources, zero taxa and two historical events.
- Actual default resolution with the complete normalized mapping table
  returned gold_unmatched, the own mint, UNGROUNDED, no mapping predicate,
  extra parent or xref. Applying the real CLASS row returned
  curated_confirm_ungrounded_from_gold_unmatched, still reviewed=False.
- Structured exact-source inspection covered all 14 raw TSVs. The full
  rendered page and actual semantic text were inspected; adding only an
  in-memory candidate definition changes that text without removing pond.
- Inspected unchanged-input [main QC at e9f6174d9](https://github.com/CultureBotAI/HabitatMech/actions/runs/37437077343)
  passed 463 tests, three skipped and two dependency warnings, all 90
  histories, zero schema errors, exact reproduction of 3,206 records, site,
  redirects, provenance and term requests. This is baseline reuse, not
  completed fresh full QC for this target. A fresh publication QC run was
  still running when this report was finished. The preceding label gate
  had zero flagged pairs and 2,054 SKIPPED_NO_ADAPTER entries.
- No separate evidence-reference check applies without evidence/causal
  edges. Original GOLD sample provenance was not recovered.

## Identity and Grounding

The complete path reproduces the mint. `curation/decisions.tsv:341`
contains CLASS-level CONFIRM_UNGROUNDED, explicitly stating that habitat
identity was not assessed. Neither it nor the seed history claims an
individual identity ruling. SEEDED is therefore faithful to the inputs,
but does not resolve the qualified habitat's definition.

Current active [ENVO:00000033 pond](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000033)
denotes a waterbody, normally smaller than a lake. It is a defensible
genus, not exact identity for every stormwater-qualified pond. The
immediate GOLD parent actually resolves by the ITEM-reviewed direct
pond-label route. Its complete generated record was read for context;
its own extra Freshwater edge, already tracked in #1427, is not a false
direct parent in this child. Preserve the child's valid pond edge.

[ENVO:01001267 stormwater](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001267)
is active and denotes accumulated water material from precipitation or
snow/ice melt, not the receiving pond. Typed OWL distinguishes its formal
definition from the explanatory comment about infiltration and runoff.
Do not replace the pond identity or genus with that material.

Ignored-inclusive local inventory inspection and a typed official ENVO
label/synonym scan found no storm-qualified pond/basin or retention/detention
pond term. Current exact ENVO searches for storm water pond, stormwater
pond, stormwater retention pond, stormwater detention pond and detention
basin returned zero hits. The separate retention basin query returned
[ENVO:00000443 flood control reservoir](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000443).
That active term is also present at `ontology_terms.tsv:7027`; typed OWL
marks retention basin as a RELATED synonym, not an exact synonym. It
describes a reservoir constructed to contain a flood. It is a meaningful
candidate to compare, not established equivalence for this GOLD bin.
These are bounded searches, not proof that every ontology lacks a term.

AQUATIC reflects the source classification. Literature's engineered
stormwater-storage usage should inform a future ITEM scope/category
assessment, but does not by itself prove every item in node 8518 denotes
a deliberately constructed retention pond rather than an incidental
receiving pond. No additional category-error finding is asserted.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:1487` contains the exact depth-five
path, one node 8518 and zero organism, study, biosample and total counts.
The all-14-inventory structured scan found no exact bulk-biosample, study,
API-triad, parameter, other-source or mapping-table contribution. Zero
count/unit omission is correct; one node needs no collapse note. Do not
borrow the generic pond's 729 organisms, 52 PREGO taxa or ranked roster.
The current GOLD path 8518 lookup returned HTTP 404, which does not
establish retirement or falsify the committed source.

Inspected the publisher abstract, announcement, sample table and sampling
paragraph of [Moretto et al. 2025](https://journals.asm.org/doi/10.1128/mra.00690-25),
DOI 10.1128/mra.00690-25, published 25 August 2025. The study characterizes
bacterial communities in four South Florida stormwater ponds and describes
the systems as engineered stormwater-storage ecosystems. Its water-column
sampling supplies bounded evidence that these ponds are microbial
habitats. This is not original provenance for GOLD node 8518. Neither
sample/sequence counts, site-specific taxa, location nor experimental
methods can populate the target's empty slots as universal properties.

A second detention/retention study was a search lead, but its publisher
page did not load; it is not affirmative evidence here. The batch's
ignored-inclusive inventory of this repository and the configured
kg-microbe checkout found none of GOLD_nodes.tsv, GOLD_edges.tsv,
goldData.xlsx or gold_biosample_triads.tsv. Original metadata remain
unresolved beyond the committed tree.

## Completeness

Ignored-inclusive exact mint, node, label and stem searches covered
curation, history, research, configuration, docs, source, tests, reports,
raw inputs and path/retirement registries. The CLASS row, raw tree and
stable-path entry matched. No target authored definition, dedicated
research, causal overlay, separate session history, retirement or earlier
individual review was found on those surfaces.

The consequential gap is a scoped individual habitat identity/definition,
not the absence of taxa or a causal graph. No gene/regulator/expression
assertion makes iModulonDB applicable. The full page faithfully shows the
pond parent and the CLASS-not-individually-assessed disclaimer, without
invented count or definition. Rendering fidelity is not ITEM endorsement.

## Findings

Zero blockers, one major, zero minors:

1. **Major: missing ITEM identity assessment and scoped definition.**
   The CLASS sweep leaves a real qualified microbial pond concept without
   an authored definition or a resolved comparison with flood-control
   reservoirs. The maintained owners are the exact source row in
   `curation/decisions.tsv` and, if no exact ontology identity fits, an
   evidence-backed definition in `curation/term_requests.tsv`.

No false direct parent or retained-source predicate finding is present:
pond is broader and no mapping predicate is emitted. Do not duplicate
#1427 or #1398 merely because adjacent records carry those defects.

## Recommended Edits

Individually assess the source and ontology candidates. If the scoped
concept lacks an exact term, record ITEM CONFIRM_UNGROUNDED and author a
pond-genus definition with `parent_mode=ADD`. Preserve the true inherited
pond parent; REPLACE is unjustified. Keep grounding UNGROUNDED for this
authored-definition route rather than using the incompatible
GROUND_AS_PARENT-plus-definition combination.

Define the stormwater relationship with inspected evidence, explicitly
resolving designed storage versus incidental receipt and wet retention
versus detention scope. Do not impose permanence, urban setting, sewer
disconnection, treatment efficacy or universal microbial membership from
one study. Reassess category only consistently with the supported scope.
A generic pond, water material or related retention-basin synonym is not
enough for an exact GROUND decision.

Preserve the mint unless exact identity is proved, source node/path,
correct absence of zero-count fields, stable stem and old historical
events. Never patch generated YAML or HTML.

## Follow-up Checks

Regress the exact source, ITEM status and evidence-backed definition,
retained pond genus, zero-count omission and historical preservation.
Test the chosen candidate/scope against generic ponds, stormwater material
and flood-control reservoirs without conflating them. Recover original
source metadata separately before asserting sample-level ecology.

Any implementation needs append-only history, dry seed, inspected guarded
canary, strict/label/provenance checks, exact reproduction, site/redirect,
term-request and full QC gates. The executed semantic probe added only a
hypothetical definition in memory and retained the pond parent; it changed
the text. It was not an authored or validated final definition. Complete
a genuine #1217 map/site refresh when implementing that change, leaving
#1218/runtime pins isolated. No scientific input changed in this review;
actual SSSOM/KGX products/current kg-microbe compatibility were not audited.

## Additional Notes

All 630 open/closed GitHub issue titles/bodies were searched for the exact
mint, node, stem and stormwater pond/basin wording; no exact follow-up was
found. Comments on every issue were not exhaustively searched. A new
bounded curation issue is appropriate under the separate publication
authorization; publishing this report is not implementation or closure.

Inspected official ENVO OWL snapshot SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
