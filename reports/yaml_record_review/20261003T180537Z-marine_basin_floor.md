# YAML Record Review: Marine basin floor

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_basin_floor.yaml`
- Started UTC: 2026-10-03T18:04:47Z
- Finished UTC: 2026-10-03T18:05:37Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord, `habitatmech:GOLD.5a296e32d2`,
Marine basin floor, AQUATIC, UNGROUNDED, SEEDED. Its sole source is
`gold.ecosystem:5352`, Environmental > Aquatic > Marine > Marine basin floor.
`PATHS.tsv:1944` pins the stem. The CLASS decision and deterministic seed
events are not evidence of ITEM curation.

## Validation

- `just validate data/habitats/aquatic/marine_basin_floor.yaml`: pass.
- `just validate-strict data/habitats/aquatic/marine_basin_floor.yaml`: one
  file, zero errors.
- Fresh full `just qc` remained active at review finish; lint, documentation
  and raw provenance passed, tests were running. Later full-corpus gates are
  not claimed complete from these focused checks.
- Inspected candidate and parent classes in the current official ENVO OWL,
  fetched and byte-verified this batch: SHA-256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- Network OAK validation is deferred to required CI. The minted identity is
  an explicitly configured no-adapter skip, not proof of correct biology.
  No taxon, DOI/PMID, causal graph or literature reference is attached.

## Identity and Grounding

The source path denotes a marine bottom habitat. `decisions.tsv:557` only
records a CLASS lexical miss; it does not establish exact identity or rule out
all ontology candidates. Keeping a minted identity pending ITEM work is
appropriate, but its current sole parent is not.

`ENVO:00001999` marine water body denotes a whole body of marine water, as
confirmed in [current official ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl)
and the maintained parent record's identity/definition block. A basin floor
underlies that water; it is not a kind of water body. GOLD parent-path
generation introduces this false is-a assertion.

Current candidate meanings were inspected, not selected by label alone:

- `ENVO:01001378` marine bed is a submerged bed beneath a marine water body;
  it is a defensible broader candidate (`ontology_terms.tsv:8872`).
- `ENVO:00000426` ocean floor and `ENVO:00000482` sea floor distinguish the
  bed beneath an ocean versus a sea. Do not resolve the source's intended
  extent merely from overlapping synonyms.
- `ENVO:00002450` ocean basin is the structural basin, not its floor.
- `ENVO:00000244` abyssal plain adds deep-water and flat/gently sloping
  constraints not stated by this source label/path.

Thus a true broader bed placement is available for item-level assessment;
exact identity with a named floor or abyssal plain is not established by the
inspected source evidence. Do not automatically mint another habitat or merge
the current one with a near-match ontology class.

## Evidence

`gold_ecosystem_paths.tsv:1535` records depth four, one GOLD node and zero
organism assertions. The absent generated count is faithful to zero-source-
count emission; it is not a claim that the floor has no microbes.
The child Sediment path at `:951` has its own node, 5353, and one ORGANISM
assertion; that count must not be copied onto this parent source.

Structured exact-path membership searches scanned every committed row in
`gold_path_biosamples.tsv` (1,040), `gold_path_triads.tsv` (1,587) and
`gold_studies.tsv` (4,587). None matched this source path. This bounded
snapshot result does not establish that live GOLD has no relevant samples or
studies. No sample depth, substrate composition or microbial specialization
can be inferred from missing rows.

## Completeness

Ignored-inclusive searches of the minted ID, source node, label, stem and
full path covered curation, raw inventories, PATHS, history, research and
individual reports. The CLASS row was found; no target ITEM decision, authored
definition, causal overlay, dedicated history or prior individual review was
found. Unrelated macroalgal-bed curation uses marine bed as a genus but is not
independent evidence for this target's exact identity.

An ITEM decision and supported genus/definition would resolve the present
hierarchy problem. Empty optional taxa, measurements, graphs, discussions and
datasets are otherwise appropriate. iModulonDB is not applicable: no organism,
gene, regulator, expression dataset or molecular mechanism is claimed.

## Findings

- **Major M1: floor asserted to be a marine water body.** The sole
  `parent_habitats` value is a contextual water-body link, not a broader bed
  class. Owners: the source decision in `curation/decisions.tsv:557`, a
  supported definition in `curation/term_requests.tsv`, and GOLD parent-link
  generation in `src/habitatmech/seed.py:898-909`.
- Blockers: 0. Major: 1. Minor: 0.

## Recommended Edits

Individually assess the source, preserving its minted identity until a true
exact mapping is supported. Place it under a verified bed genus and remove the
false water-body parent through maintained inputs. If using an authored
definition, REPLACE is defensible only after recording that this sole inherited
parent is false; otherwise use a scoped source-parent exclusion. Do not apply
that replacement rule blindly to other records with true inherited parents.

## Follow-up Checks

Regenerate a canary and verify source identity, absent zero count, new true
genus and removal of only the false parent. Inspect descendants without
transferring their counts or assuming their material-to-place edges are valid.
Append history for the actual curation change; run provenance, schema, applicable
OAK, corpus, semantic-map/site rebuild and full QC. Do not bypass the separate
map-runtime blocker tracked in #1217 or merge draft #1218 prematurely.

## Additional Notes

All 442 returned open/closed issues and comments were searched for this source
and Marine basin floor; no corresponding correction issue was found. The
marine-water-body parent was inspected for meaning only, not counted as another
completed review. No scientific input, generated record, page or history
changed.
