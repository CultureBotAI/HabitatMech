# YAML Record Review: Geothermal pool/Hot lake

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/geothermal_pool_hot_lake.yaml`
- Started UTC: 2026-10-03T09:25:59Z
- Finished UTC: 2026-10-03T09:27:39Z
- Verdict: needs curation

## Target

Read the complete generated `HabitatRecord`,
`habitatmech:GOLD.d2132d09ae`, category `AQUATIC`, grounding `UNGROUNDED`,
mapping `SEEDED`. Baseline: `52b870a4c7f6fb6a317dffdd6c68e113c33c14e3`.
This is the exact GOLD pool/lake bucket, not its sediment child or the
separate hot-spring record. The pinned slug is at `data/habitats/PATHS.tsv:2838`.

## Validation

- `just validate data/habitats/aquatic/geothermal_pool_hot_lake.yaml`: pass.
- `just validate-strict data/habitats/aquatic/geothermal_pool_hot_lake.yaml`:
  pass, zero errors.
- Recomputed the GOLD minted ID from the exact path: match.
- Live OLS check of `ENVO:00000051`: current, non-obsolete hot-spring term;
  definition agrees with the vendored slice.
- Shared full `just qc`: running at report completion. Its final result belongs
  to the batch PR, not this timestamped review. Full OAK validation was not
  repeated here. No target citation or causal-edge validation applies.

## Identity and Grounding

The source path is
`Environmental > Aquatic > Thermal springs > Geothermal pool/Hot lake`.
The minted identity preserves the unresolved compound source concept rather
than forcing an exact match to either lake or hot spring.
`curation/decisions.tsv:1157` is a `CLASS`-depth `CONFIRM_UNGROUNDED` decision,
not an item-level endorsement of habitat meaning. The record accurately
retains `SEEDED` and includes the class-sweep caveat in its history.

The sole parent, `ENVO:00000051`, comes from GOLD's immediate Thermal springs
path, not from an ontology subclass assertion about this minted target.
That parent resolves through GOLD row 50. Its identity is verified, but the
strict is-a relationship for the entire pool/lake bucket is not established.
No definition in this record limits the bucket to groundwater-emergence
features. The parent record was read for context; this is not a review or
endorsement of all its taxa, mechanisms, or ancestors.

## Evidence

Named-column parsing of `data/raw/gold_ecosystem_paths.tsv:584` gives depth 4,
two nodes (`gold.ecosystem:8064|gold.ecosystem:8066`), `organism_count=7`,
`study_count=0`, `biosample_count=0`, and `total_assertions=7`.
The generated seven `ORGANISM` assertions, representative first node, and
two-node provenance note are correct. This inventory has no genome-count
column. The sediment child at row 807 has its own two organism assertions;
those are not added to this target.

Exact-path parsing of `gold_path_biosamples.tsv`, `gold_path_triads.tsv`, and
the pipe-separated memberships in `gold_studies.tsv` found no matching row.
That is a bounded result for these committed inventories, not proof of no
samples or studies anywhere. No authenticated live GOLD query was made.

The [current ENVO hot-spring definition](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000051)
requires geothermally heated groundwater flowing through a spring.
[NPS's inspected account](https://www.nps.gov/yell/learn/nature/hotsprings.htm)
shows that some named pools are indeed hot springs. Conversely,
[USGS's inspected Yellowstone Lake account](https://www.usgs.gov/observatories/yvo/news/hydrothermal-system-yellowstone-lake)
distinguishes a lake from the hot springs and vents on its floor.
These establish a relevant scope distinction, not the identity of GOLD's
seven underlying organism assertions. They do not prove that every pool is
distinct from a spring, or that this source necessarily contains two classes.

## Completeness

Ignored/hidden-inclusive searches covered `curation`, `history`, `research`,
`reports`, `conf`, `data/raw`, and the slug lock for the identifier, exact
label, slug, source path, and both source nodes. They found the class decision,
source and child rows, and slug, but no target-specific item decision,
definition, research report, causal overlay, or prior target review there.

Optional taxa, parameters, evidence, graphs, discussion, and dataset slots are
empty. Do not fill them from the parent hot-spring record or generic thermal
habitat literature. The consequential gap is the undefined scope supporting
the parent assertion, not optional-field coverage.

## Findings

- **Major M1: the hot-spring parent is not justified for the complete pool/lake
  source bucket.** GOLD placement establishes source context, but without an
  item-level definition it does not establish that every denoted pool or lake
  is a spring feature. The spring-fed pool interpretation is plausible; a
  heated lake containing springs is materially different. This is an
  unsupported generalization requiring scope resolution, not a demonstrated
  assertion that every source member has been misclassified. Owners:
  `curation/decisions.tsv`, any justified definition in
  `curation/term_requests.tsv`, and the source-parent contribution in
  `src/habitatmech/seed.py`.

Zero blockers and zero minor findings.

## Recommended Edits

1. Inspect the underlying GOLD members for nodes 8064 and 8066 and decide whether
   the bucket denotes spring pools, heated lakes, or a deliberately mixed bin.
   Record an item-level decision and evidence-backed definition only after
   resolving that scope; do not automatically merge it with hot spring or lake.
2. If the hot-spring is-a claim is unsupported after that check, exclude only
   the source-context parent using the maintained exclusion mechanism proposed
   in draft PR #1218. Preserve source paths and counts. Do not adopt a narrower
   replacement genus merely to obtain a parent.

## Follow-up Checks

Run `just seed`, then
`just seed-canary habitatmech:GOLD.d2132d09ae --force`. Inspect the complete
record, parent justification, seven-ORGANISM attestation, and sediment-child
boundary. Add curation history only for an actual curation change. Run focused
schema/strict validators, `just validate-products` for grounding changes,
`just verify-corpus`, required semantic-map refresh, `just render`, and
`just qc`. Preserve the historical review report.

## Additional Notes

iModulonDB is not applicable: the target asserts no organism, gene, regulator,
or expression dataset. No paid research was used. This review does not turn
the class-level sweep into an item review or count the parent as reviewed.
