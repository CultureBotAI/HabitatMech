# YAML Record Review: Commercial compost

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/commercial_compost.yaml`
- Started UTC: 2026-10-07T21:43:18Z
- Finished UTC: 2026-10-07T21:46:52Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord `habitatmech:GOLD.f9bc260cd7`,
Commercial compost, ENGINEERED / UNGROUNDED / SEEDED, at baseline
`c9d26980ff653a546bdd8f39133c1ef869b8711d`.

It has one parent, one GOLD attestation and two events. There is no definition,
synonym, xref, count/unit, taxon, parameter, literature evidence, causal graph,
discussion or dataset assertion. The source is the specific commercial-compost
path, not the generic ENVO compost record or a named commercial formulation.

## Validation

Commands used `UV_CACHE_DIR=build/uv-cache`.

- `just validate data/habitats/engineered/commercial_compost.yaml`: no issues.
- `just validate-strict data/habitats/engineered/commercial_compost.yaml`:
  one file, zero errors.
- Fresh read-only `build_corpus` / `build_document`: all-field equality,
  one contributing source and zero ITEM-reviewed sources; recomputed mint,
  PATHS entry and source path agree.
- Fresh official structured ENVO responses verified the compost candidate,
  manure genus and the two top contextual triad terms, including active status.

Full gates are reused, not rerun for this target. Fresh tree comparison with
tested head `7387b7a490b036f84fdb53f3125392c998902ba9` passed. Local QC,
final-head CI and native-queue CI passed on this exact tree: 533 tests,
three skips, 159 histories, 3,207 strict-valid/exact records, 32 overlays,
curation floor, provenance and generated-product checks. OAK reported 1,178
canonical labels, one synonym, five accepted exceptions and 2,056 no-adapter
skips. These results do not establish the source parent's intended meaning.

## Identity and Grounding

The full path is
`Engineered > Solid waste > Mixed feedstock > Composting > Commercial compost`.
The mint preserves this qualified source identity. Its 2026-08-12
CONFIRM_UNGROUNDED decision is CLASS depth and explicitly leaves habitat
meaning unassessed; SEEDED accurately reflects that limitation.

Active [ENVO:00002170 compost](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002170)
is a decomposed organic material, with the local subclass genus
[ENVO:03501300 manure](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03501300).
The latter includes plant-derived fertilizer material; it is not restricted to
animal feces. Generic compost is a plausible broader material candidate, not
an automatically exact identity for this qualified source.

The [EPA definitions](https://www.epa.gov/sustainable-management-food/composting)
distinguish the managed aerobic process from its stable compost product and
from still-active, incompletely decomposed material. Commercial products
typically undergo a high-temperature phase, but that statement supplies neither
a universal temperature nor a condition to attach to this record. Production
scale, feedstock, process environment and finished product must remain distinct.

## Evidence

**Source fidelity and units.** A completed exact-field/pipe-member scan of all
14 raw TSVs found six target rows in four inventories:

- The ecosystem row is depth five with one node, `gold.ecosystem:7698`, and
  zero organism/study/biosample/total counters in that particular snapshot.
- The later bulk inventory separately has 32 BIOSAMPLE observations.
- `gold_studies.tsv` has one study, `Gs0127392`, spanning two paths: this
  commercial-compost path and the separate terrestrial Soil path.
- API triads cover 31 samples from that one study. All medium annotations
  are compost. Broad scale has terrestrial biome as its top term, and local
  scale anthropogenic environment; both top shares are 0.97, with two distinct
  terms per slot and one agreeing study. The aggregate does not identify the
  minority terms or crosswalk all 31 API samples to the 32 bulk biosamples.

Current official [terrestrial biome](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000446)
and [anthropogenic environment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000313)
responses agree with those IDs and labels. They remain contextual slots, not
habitat identities. Do not count the three slots as independent studies, sum
31 and 32, or turn biosamples into organisms. Count/unit omission in the
generated organism-based attestation is appropriate; no microbial absence is
asserted. One node needs no collapse note, and UNGROUNDED needs no self-mapping
predicate.

**Parent route and uncertainty.** The full parent record,
`habitatmech:GOLD.753da37dcf` (`composting__614642ae.yaml`), is automatically
NARROW under ENVO compost and the minted Mixed feedstock source. It has no
ITEM scope decision or authored definition. Its material placement traces to
the upstream lexical mapping `Composting -> compost` in
`data/raw/isolation_source_groundings.tsv:72` and the ambiguous-leaf route,
not an independently established definition of this GOLD bin.

This is not enough to declare the edge definitely false: if the parent means
mixed-feedstock compost material, the commercial product may genuinely be
narrower. If it means a composting process or the environment of an active
operation, product-to-process/environment subsumption is not established.
The complete Mixed feedstock ancestor was read for this distinction; its own
CLASS decision does not settle the immediate parent's scope. The unanimous
sample-medium term supports compost material context, not the identity of
every source ancestor or a strict parent relationship.

**Study recovery limits.** Direct GOLD study/project and IMG pages were
inaccessible. Exact-accession searches surfaced NMPFamsDB metadata leads for
enriched commercial-compost communities, including IMG 3300017652 and
3300013048, but attempts to open their pages failed or timed out. Search
results were not accepted as inspected study evidence. No enrichment
temperature, passage, formulation, organism or expression result was imported,
and no original sample-to-path crosswalk was established.

## Completeness

Ignored-inclusive identifier, label and slug searches covered curation,
history, conf, docs, tests, research, its manifest, raw inventories, PATHS,
RETIRED and prior review reports. They found only the CLASS decision and
inventory/path references, not a target-owned definition, xref, overlay,
parent exclusion, retirement, history entry or research-manifest item. No
earlier target report was found in those report searches.

An ignored-inclusive filename search in `build` and configured kg-microbe
`data` found neither `GOLD_nodes.tsv` nor `GOLD_edges.tsv`. This bounded result
does not establish that no alternate archive exists elsewhere.

Missing optional biology is not a defect. This record makes no named organism,
gene, regulator, pathway, stress-response or transcriptomics assertion;
iModulonDB is not applicable. A search lead mentioning RNA does not make an
expression-module lookup evidence for commercial-compost identity.

## Findings

Zero blockers, one major finding, zero minor findings established.

1. **Major: unresolved material/process scope in the asserted parent.**
   `parent_habitats` asserts strict subsumption, but the parent's automatic
   process-label-to-material route and the sample triads do not establish
   which referent the GOLD parent denotes. This is a consequential unresolved
   hierarchy claim, not a finding that every process-named parent is wrong
   or that an optional definition is mandatory. Scope assessment belongs in
   `curation/decisions.tsv` for the relevant source concepts; a justified
   authored definition belongs in `curation/term_requests.tsv`.

## Recommended Edits

1. Recover original GOLD scope and sample metadata for `Gs0127392`, retaining
   the distinction between the two study paths, sample material and laboratory
   enrichment context. Resolve the immediate parent before endorsing its
   strict relationship to this target.
2. Retain the edge if the parent is supported as broader mixed-feedstock
   compost material. If the actual relation is only process or production
   context, any guarded suppression belongs in
   `curation/gold_parent_exclusions.tsv`, keyed to source
   `habitatmech:GOLD.f9bc260cd7`, the full path and expected parent
   `habitatmech:GOLD.753da37dcf`. Do not remove it from the label alone.
3. Assess generic compost as a possible broader material genus, not an exact
   commercial-source merge. Do not force NOT_APPLICABLE, a product formulation,
   an arbitrary definition or ITEM review merely to close this report.

## Follow-up Checks

For separately authorized curation, test the exact whole-corpus scope and
preserve the mint, GOLD node, path, count omissions, original events and honest
review status. Dry seed, inspect a forced target canary, and run strict,
history, provenance, corpus, ontology-scope/label, map/site and full QC gates.
Check parent and sibling records independently; a generic compost graph or
taxon list must not be transferred to this leaf.

## Additional Notes

Official structured ENVO and EPA content were accessible. GOLD, IMG and the
NMPFamsDB page opens were not; their search results remain leads only. The
initial generic TSV diagnostic encountered an unrelated overflow column at
`gold_path_biosamples.tsv:395`; the completed scan retained overflow values
and found the six well-formed target rows. No source inventory was changed.

Only this new review report was written. Contextual parent reads are not
additional completed reviews. No scientific curation, regeneration, history
or status change, paid research, or GitHub mutation occurred in this pass.
