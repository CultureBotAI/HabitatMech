# YAML Record Review: Biological phosphorus removal

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/biological_phosphorus_removal.yaml`
- Started UTC: 2026-10-07T10:43:17Z
- Finished UTC: 2026-10-07T10:45:03Z
- Verdict: needs curation (0 blocker, 1 major, 0 minor)

## Target

Read the entire generated HabitatRecord `habitatmech:GOLD.03345a3f86`, Biological
phosphorus removal, ENGINEERED, UNGROUNDED/SEEDED. One GOLD path at depth four,
`Engineered > Wastewater > Nutrient removal > Biological phosphorus removal`,
has two collapsed source nodes3832/4730. Its parent is the separately minted
Nutrient removal record. There is no authored definition clarifying a habitat.

## Validation

- Focused `just validate` and `just validate-strict` for this complete target
  passed; strict validation scanned one file with zero errors.
- Complete parsed reproduction through `seed.build_corpus()` and
  `seed.build_document()` passed: one source, zero reviewed sources, no taxa,
  two history events. All fields match, not just the identity projection.
- Structured exact-key inspection covered all 14 raw TSVs and both source nodes.
  Actual automatic/applied GOLD routes were inspected for target and parent.
- Read the full target page, full Nutrient removal parent, and both immediate
  Activated sludge/Bioreactor child records to check what the source hierarchy
  distinguishes. This does not complete independent reviews of those records.
- Reuse the immediately preceding complete local QC at unchanged tracked head
  `66f2dc3d13ac1000ea5cb7199f271dc1df4a1a08`: 523 tests passed, 3 skipped,
  146 valid histories, 3,207 strict-valid/reproducible records, 32 overlays and
  current site, redirects, term requests, provenance, lint, docs and floor.
  Governing-file diff is empty. Session-wide OAK passed with documented adapter
  skips; the target relies on minted habitat IDs, not a new ontology/taxon match.
- PMID, DOI and inspected primary-paper sections agree. The GOLD study page
  could not be retrieved. Required PR #1630 checks remain queued, not passed.

## Identity and Grounding

The source path deterministically produces the record mint. Automatic resolution
is `gold_unmatched`; the applied route is
`curated_confirm_ungrounded_from_gold_unmatched`, reviewed false. The target's
decision at `curation/decisions.tsv:115` and parent's at row937 are CLASS-only
CONFIRM_UNGROUNDED decisions. They explicitly leave habitat applicability
unassessed, rather than endorsing a treatment-system or material identity.

The generated history and page accurately retain that limitation. No unsupported
ontology exact match or false REVIEWED status is present. However, the literal
label names a biological treatment process, while the record and page present it
as a microbial habitat. The sole parent Nutrient removal is also process-named.
Without an item-level habitat interpretation, neither supplies a defensible
habitat genus. This is more consequential than a missing optional description.

The source hierarchy separately names Activated sludge (`habitatmech:GOLD.cc5ac8910b`,
node4262) and Bioreactor (`habitatmech:GOLD.778799e140`, node4263) below this node.
That is evidence of classification context, not proof that the target equals
either child or that both are subclasses of a single material. Do not silently
collapse the parent into sludge, a reactor, an anaerobic zone or a process ontology
term. PATHS row1286 and the parent link resolve correctly.

## Evidence

`gold_ecosystem_paths.tsv:1410` supplies the exact path, two nodes3832/4730 and
zero organism/study/biosample/total assertions. The missing count/unit pair and
collapsed-node note are faithful. The separate bulk-export row
`gold_path_biosamples.tsv:447` reports 27 biosamples for path ID4730; these must
not be relabeled as organism assertions. `gold_studies.tsv:2397` names one
single-path study, Gs0142311. Its [GOLD page](https://gold.jgi.doe.gov/study?id=Gs0142311)
failed retrieval, and an exact-ID search found no original metadata.
No source-to-paper or sample-phase crosswalk was established. The other eleven
raw inventories had no exact target-key hit, including no triad, parameter or taxon.

Inspected [Crocetti et al. 2000](https://pmc.ncbi.nlm.nih.gov/articles/PMC91959/),
PMID:10698788, DOI:10.1128/AEM.66.3.1175-1182.2000: abstract, introductory
process description and Materials and Methods / EBPR reactors distinguish
biological phosphorus removal from the SBR vessels, sampled sludges and treated
wastewater. The experiment used alternating anaerobic/aerobic operation, so an
entire EBPR system cannot be equated with just its anaerobic phase from this
example. The study supports the process/system/material distinction, not a
GOLD sample identification. Organisms, probes, percentages and operating values
were not transferred to the habitat, and no universal EBPR mechanism is asserted.

## Completeness

An ITEM-level decision about habitat applicability and scope is consequentially
missing. A CLASS-level absence of a lexical ontology match does not answer that
question. Optional taxa, parameters, evidence objects, graph, discussions and
datasets are not required merely because the process is well studied. Neighboring
dissolved-organics research calls an EBPR zone anaerobic, but that passage is not
evidence that this whole source node denotes that single zone.

Ignored-inclusive searches covered curation tables/overlays, histories, conf,
docs, tests, research, manifest, PATHS and RETIRED using exact source/minted IDs,
label and slug. Apart from the two CLASS decisions and neighboring context,
no target authored definition, ITEM decision, overlay, session history,
research-manifest row or retired URL was found in this bounded scope. No original
study metadata was successfully inspected. iModulonDB does not resolve this
habitat-identity question without an organism/dataset/gene-level target; no
absence of relevant organisms from that resource is inferred.

## Findings

**Major: a treatment process has no established habitat interpretation.**
The record exposes Biological phosphorus removal under the equally process-named
Nutrient removal as a habitat hierarchy, while its only decision explicitly
leaves applicability unassessed. The inspected primary study distinguishes the
process, device and microbial material. Original GOLD evidence is needed to
decide whether the source means a treatment environment or is non-habitat context.
This is one scope/identity finding, not duplicate findings for every missing field.

Maintained owners: `curation/decisions.tsv` for the exact source mint and ITEM
applicability decision; `curation/term_requests.tsv` for an evidence-backed habitat
label/definition and true genus if needed. Source assertions belong to their
extractor/inventory. Generated YAML and pages are not edit surfaces.

## Recommended Edits

1. Obtain the original node4730/3832 and Gs0142311 sample descriptions. Explicitly
   distinguish process-only indexing from treatment environment, vessel, wastewater
   and sludge; preserve any mixed source scope instead of choosing a convenient child.
2. If a habitat meaning is established, replace the CLASS-only decision with an
   ITEM decision and a bounded definition/label with a defensible habitat genus.
   If the source is genuinely only a process, use NOT_APPLICABLE with evidence.
   Do not select a phosphorus chemical or GO process as a habitat identity.
3. Reassess the Nutrient removal parent and incoming child contributions under
   the selected meaning. Preserve all source IDs, full paths and count omissions;
   do not infer a new mapping status or biological mechanism from this review.

## Follow-up Checks

Test the exact source decision and any hierarchy replacement, including both
child references and effects on other records. Dry seed, inspect the target
canary, run focused open/strict validation, full reproduction, history and OAK
checks. Regenerate affected paths/redirects, semantic map and site before full
QC. Every new taxon or causal edge would need its own inspected evidence.

## Additional Notes

Only this timestamped report was written. No habitat, curation input, status,
history, paid research or GitHub item changed for this target. The report remains
outside PR #1630. The full all-record goal remains active and incomplete.
