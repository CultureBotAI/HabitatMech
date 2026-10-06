# YAML Record Review: Subterranean estuary

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/subterranean_estuary.yaml`
- Started UTC: 2026-10-06T11:41:39Z
- Finished UTC: 2026-10-06T11:45:36Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord habitatmech:GOLD.58415258eb,
Subterranean estuary, AQUATIC, UNGROUNDED, SEEDED. Its sole source is
GOLD8255, Environmental > Aquatic > Marine > Intertidal zone >
Subterranean estuary. The actual mint agrees and `PATHS.tsv:1934`
pins the stem. One parent and two generated events are present; there
is no definition, synonym, xref, count, taxon, parameter, evidence or graph.

## Validation

- `just validate data/habitats/aquatic/subterranean_estuary.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/aquatic/subterranean_estuary.yaml`:
  one file, zero errors.
- Actual full `build_corpus` / `build_document` equality passed for all
  fields: one source, zero item-reviewed sources, zero taxa, two events.
- Executed target and immediate-parent default/applied routes; scanned
  all 14 raw inventories for exact path/node membership; read the full
  rendered page and full-context semantic text.
- [Main QC at exact base 51b57a85c](https://github.com/CultureBotAI/HabitatMech/actions/runs/37457680179)
  passed every gate: 463 tests passed, three skipped, two dependency
  warnings, 90 valid histories, 3,206 strict-valid and exactly reproduced
  records, current site, 231 redirects and term-request table. Scientific
  inputs, guidance, code and tests are unchanged from the prior reviews;
  this is baseline reuse, not a new full QC per target.
- Required merge-candidate labels passed with zero flagged pairs and
  2,054 no-adapter skips. No emitted taxon/evidence/graph references
  require a separate target audit.

## Identity and Grounding

`curation/decisions.tsv:549` is CLASS CONFIRM_UNGROUNDED. The actual
gold_unmatched route becomes curated_confirm_ungrounded_from_gold_unmatched,
retaining the minted identity, no predicate and reviewed=False. The
SEEDED status and explicit CLASS-level warning are faithful, not defects.

Current structured ENVO searches for subterranean estuary, subterranean
estuaries, coastal aquifer and subsurface estuary returned no term.
Ignored-inclusive searches of the committed slice likewise recovered
only broader or adjacent concepts. These are bounded searches, not a
claim that no external vocabulary can name this habitat.

Verified current OLS and typed official OWL candidates include:

- [Estuary, ENVO:00000045](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000045):
  a coastal waterbody with river/stream input and an open-sea connection.
  Lexical containment of estuary does not equate a coastal subsurface
  groundwater-mixing environment with that surface-waterbody identity.
- [Aquifer, ENVO:00012408](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00012408):
  a water-bearing permeable geological layer with an extraction criterion.
  It is not automatically identical to the reaction/mixing zone within it.
- [Planetary subsurface environment, ENVO:01001046](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001046):
  a potential broader environmental-system genus, not an exact match.

The entire immediate parent habitatmech:GOLD.115edc36f8 and its earlier
individual review were read. Its actual gold_narrower_than_leaf_match
route is NARROW/SEEDED without an ITEM override, with the ontology
reference [intertidal zone, ENVO:00000316](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000316).
That term denotes the foreshore/seabed area alternately exposed to air
and submerged between tide marks. A groundwater-seawater mixing zone
in the subsurface is not a type of that exposed surface merely because
it occurs beneath an intertidal location. GOLD source placement is
context, not evidence of a strict genus.

The parent also has the already-documented false marine-waterbody
edge to ENVO:00001999, independently verified as a lentic marine body.
[#1253](https://github.com/CultureBotAI/HabitatMech/issues/1253) owns
that parent correction. Correcting it alone would leave this child's
unsupported direct intertidal edge. These are distinct contributions;
the inherited consequence is not counted as a second child finding.

## Evidence

`gold_ecosystem_paths.tsv:1530` gives the exact depth-five path,
one node and zero organism/study/biosample/total counters. Omitting
count and unit is correct, not proof of ecological emptiness. No exact
path/node contribution appears in the other 13 raw inventories,
including bulk biosamples, triads, studies, taxa or parameters.
The current official GOLD8255 projection returned HTTP 404, which
alone neither proves retirement nor invalidates historical provenance.

[Hong et al. 2019](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2018.03343/full),
DOI 10.3389/fmicb.2018.03343, [PMID 30687299](https://pubmed.ncbi.nlm.nih.gov/30687299/),
provides direct microbial evidence from a Gloucester Point subterranean
estuary. The inspected primary abstract/introduction describe the
groundwater-saline-porewater interface and bacterial/archaeal 16S
analyses of a metre-long permeable sediment core. This supports habitat
plausibility and the distinction between a subsurface habitat and its
surface setting. Functional assignments use prediction, not direct proof
of every process. The study does not identify GOLD8255 or establish
universal taxa, chemistry, vertical limits or mechanisms for this bin.

Do not transfer the broader intertidal parent's 77 ORGANISM assertions,
276 bulk samples or 273 API samples/13 studies from its prior review.
They are not this exact path's observations. No characteristic presence,
quantitative parameter or causal edge is justified by those aggregates.

## Completeness

Ignored-inclusive ID, label/stem, node and source-key searches covered
curation, history, research, configuration, documentation, source,
scripts, tests, reports and path/retirement registries. The CLASS decision
and path lock exist; no target-owned definition, causal overlay, session
history, retirement or previous individual review was found. Adjacent
estuary, sediment, intertidal and microbialite reports are not this record.

An ITEM scope assessment should distinguish the subsurface environment,
the containing aquifer, groundwater material and any sampled sediment.
Optional fields must not be filled for coverage; the absence of taxa,
parameters or mechanisms is not independently a defect. iModulonDB is
not applicable without a gene, regulator or expression claim.

## Findings

Zero blockers, one major, zero minors:

1. **Major: source context becomes an unsupported intertidal genus.**
   The sole direct edge is GOLD.58415258eb -> GOLD.115edc36f8, added
   by the independent GOLD parent-path pass at `src/habitatmech/seed.py:898-907`.
   The subsurface mixing environment is not established as a type of
   exposed intertidal surface. Maintained owners: the target's
   `curation/decisions.tsv` and `curation/term_requests.tsv` inputs,
   or governed source-specific parent controls with regression coverage.

## Recommended Edits

Perform an ITEM habitat/scope assessment and author an evidence-backed
definition if no exact term fits. A subsurface-environment genus is a
candidate, not a lexical auto-grounding. For a justified minted
UNGROUNDED definition, REPLACE can remove this sole unsupported inherited
parent; use it only after confirming the entire inherited set is false.
Alternatively suppress the exact source contribution through validated
maintained controls, without inventing a replacement identity.

Preserve GOLD8255, the full source path, pinned stem, AQUATIC category,
zero-count omission and old events. Do not exact-merge with generic
estuary, classify a real habitat NOT_APPLICABLE, treat sampled water as
the whole environment or borrow other intertidal-source evidence.

## Follow-up Checks

The actual in-memory direct-parent removal changes full-context semantic
text. A real hierarchy/definition correction therefore requires genuine
#1217 map/site handling and a fresh input comparison, while keeping
draft #1218/runtime pins isolated. Predicate omission was text-neutral
because this target has no predicate; it is not an export validation.

Regress the exact source/parent contribution and supported intertidal
controls, append corrective history, dry seed, inspect a guarded canary,
and run applicable schema, labels, provenance, history, reproduction,
site, redirect, term-request and full-QC checks. Verify #1253 separately
rather than claiming a child correction solves its parent. No scientific
input, history, generated record, page or SSSOM/KGX artifact was changed
or certified by this report.

## Additional Notes

All 636 open/closed issue titles and bodies were searched for the exact
source key, subterranean-estuary wording and parent key. #1253's full
body has no comments and owns only the parent's outgoing edge. No
exact child-specific owner was found on these surfaces; every repository
issue comment was not exhaustively searched.

The Moore 1999 and Euler 2024 publisher requests were blocked, and PMC
served a browser challenge. The accessible Hong publisher text supplies
the bounded evidence used above; a later attempt to fetch its methods
section timed out, so no full-methods audit is claimed.

Typed official ENVO snapshot SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
