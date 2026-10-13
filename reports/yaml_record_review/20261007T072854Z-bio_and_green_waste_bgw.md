# YAML Record Review: Bio- and green waste (BGW)

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/bio_and_green_waste_bgw.yaml`
- Started UTC: 2026-10-07T07:27:02Z
- Finished UTC: 2026-10-07T07:28:54Z
- Verdict: pass (0 blocker, 0 major, 0 minor)

## Target

Read the complete generated HabitatRecord, direct Solid Waste parent and target
page. The target is `habitatmech:GOLD.d6cebb0aa0`, ENGINEERED / UNGROUNDED /
SEEDED, with one parent, one GOLD attestation and two history events. It asserts
no definition, synonyms, xrefs, count/unit, environmental parameters, taxa,
literature evidence, causal graph, discussion or dataset. An earlier partial
inspection was interrupted by publication; the record and checks were freshly
read at the new baseline before this report was completed.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/bio_and_green_waste_bgw.yaml`: passed.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/bio_and_green_waste_bgw.yaml`: passed, one file and zero errors.
- Fresh `build_corpus()` / `build_document()` comparison reproduced the entire
  parsed record, with one source concept, zero reviewed sources, zero taxa and
  two events. Actual target and parent GOLD resolution routes were inspected.
- Full QC and OAK were not repeated per target. Reuse unchanged scientific
  baseline `92c7c270dbbece1ce5d7db810f41f429822d3704` and its
  [full QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37585578115)
  and [label gate](https://github.com/CultureBotAI/HabitatMech/actions/runs/37585578170).
  Their exact SHA and terminal success were rechecked this continuation. These
  cover corpus, references, history and generated products, not scientific
  identity; the minted target and MeSH parent are outside active OAK adapters.
- An ignored-inclusive filename search in `build` and configured kg-microbe
  `data` found no original GOLD node/edge dumps. Original-source re-extraction
  was not run; the exact source-node trace remains inventory-backed.

## Identity and Grounding

`data/raw/gold_ecosystem_paths.tsv:1351` records the exact depth-three path
`Engineered > Solid waste > Bio- and green waste (BGW)`, node
`gold.ecosystem:7755`, one source node and zero counted assertions. Its mint
agrees with PATHS line 2879. The zero counts explain omitted count/unit, not
biological absence. The Composting descendant at line 1352 has its own two
nodes, 7756 and 7757, and is not merged into this target.

CLASS CONFIRM_UNGROUNDED at `curation/decisions.tsv:1188` preserves the automatic
unmatched route without extra parents or xrefs. Its explicit habitat-hood
caveat and SEEDED status correctly avoid an ITEM-review claim.

The sole parent, `mesh:D062611`, comes from the immediate GOLD parent path.
Parent mint `habitatmech:GOLD.4233e9003d` resolves by `gold_mapping_table` using
the Solid-waste row at `data/raw/isolation_source_groundings.tsv:286`; the slice
label is at `data/raw/ontology_terms.tsv:13610`. No target exactMatch is thereby
asserted. Unlike a generic retained crop residue, the target explicitly denotes
waste; its source path supports membership in the broader solid-waste class.
The parent's 81 ORGANISM assertions and own ancestors are not target assertions.

## Evidence

Structured exact-field/pipe-member scans covered all 14 raw TSVs. Only the
ecosystem inventory matched target keys, including its named descendant.
No target study, bulk biosample, triad, parameter or taxon contribution was
found in those committed inventories.

Fresh primary NLM JSON identifies [D062611](https://id.nlm.nih.gov/mesh/D062611.json)
as active Solid Waste. Its preferred concept
[M0568791](https://id.nlm.nih.gov/mesh/M0568791.json) covers garbage, refuse and
discarded solid or related contained materials, distinguishing dissolved waste.
The JavaScript HTML shell did not expose this scope, so the primary JSON was
read directly. This supports the broad material distinction, not an exact BGW
definition or a claim that BGW comes from one specified facility type.

The JGI-submitted [BioSample SAMN06268781](https://www.ncbi.nlm.nih.gov/biosample/SAMN06268781)
contains the GOLD classification through BGW and then Composting. It concerns
an adapted compost community. This independently confirms use of the source
category in compost-associated microbial sampling, not a crosswalk from that
sample to node 7755 or universal properties of the parent class. Its project,
location, community and experimental conditions are not transferred.

[EPA's composting definitions](https://www.epa.gov/sustainable-management-food/composting)
distinguish organic feedstocks, managed microbial decomposition and the stable
compost product. Inference: the BGW source label is compatible with organic
waste material but does not establish finished compost, a fixed recipe, a
particular processing stage or universally thermophilic conditions.

## Completeness

Ignored-inclusive identifier, label and filename searches covered curation,
history, configuration, docs, tests, research, the research manifest, PATHS,
RETIRED and the ontology/mapping inventories. Only the CLASS row and PATHS
entry matched; no target-owned definition, overlay, parent exclusion, session
history or research file was found within those bounds.

The bounded ontology search for biowaste, biodegradable/green/yard/garden waste
returned the generic MeSH parent and chicken breeding waste material
ENVO:00002266, not an exact BGW identity. The chicken-specific term must not be
substituted merely because it includes a yard-waste synonym. This is not a
global claim that no suitable term exists. Missing optional fields are not
defects by themselves. iModulonDB is not applicable without a named organism,
gene, regulator or expression dataset; non-use is not negative evidence.

## Findings

None found. The source hierarchy, preserved mint, conservative grounding and
limited review status are coherent at the asserted scope. The page faithfully
renders them. This pass does not certify exact feedstock composition or every
descendant's modeling.

## Recommended Edits

No correction is justified. Any later definition belongs in
`curation/term_requests.tsv`, with a separately evidenced ITEM decision in
`curation/decisions.tsv` where warranted. Resolve source scope first; do not
borrow the descendant experiment's properties or equate BGW with compost.

## Follow-up Checks

For future enrichment, recover original GOLD metadata and distinguish incoming
waste, processing material and stable product before choosing an ontology
identity or genus. Then inspect dry seed and a canary, run strict and full QC,
and refresh affected products; a new ontology identity also needs OAK checks.
No such enrichment or regeneration was performed here.

## Additional Notes

The direct parent was inspected as a reference, not counted as another complete
record review. Only this timestamped report was written. No curation, status
promotion, scientific artifact regeneration, paid research or GitHub mutation
occurred in this review continuation.
