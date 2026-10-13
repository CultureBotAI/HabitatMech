# YAML Record Review: Cellulose associated waste

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/cellulose_associated_waste.yaml`
- Started UTC: 2026-10-07T16:43:53Z
- Finished UTC: 2026-10-07T16:47:33Z
- Verdict: pass

## Target

Generated `HabitatRecord` `habitatmech:GOLD.a1c99dadfc`, label
`Cellulose associated waste`, category `ENGINEERED`, grounding `UNGROUNDED`,
mapping `SEEDED`. Baseline: `3222c6ac408b97facf09851d54a920441651c93e`.

The entire target was read. It has one parent, one source attestation and two
generated history events. It has no definition, synonyms, xrefs, environmental
parameters, associated taxa, causal graph, discussion or dataset reference.
This is a judgement of that bounded seeded representation, not an ITEM
curation decision or certification of a chemically uniform waste stream.

## Validation

Commands use `UV_CACHE_DIR=build/uv-cache`:

| Check | Result and scope |
|---|---|
| `just validate data/habitats/engineered/cellulose_associated_waste.yaml` | No issues found. |
| `just validate-strict data/habitats/engineered/cellulose_associated_waste.yaml` | One file, zero errors. |
| Read-only `build_corpus` / `build_document` comparison | Every target field is exactly reproduced; one identity source, zero ITEM-reviewed sources. |
| Identifier/source checks | Mint recomputed from the exact path; GOLD4928 and the parent ID verified against the maintained inventories and current NLM descriptor. |

The full gates from the preceding publication session apply to the unchanged
scientific tree: `just qc` passed 529 tests with three skips, strict validation
and exact reproduction of all 3,207 records, 32 overlays, 151 histories, curation
floor, site/map freshness, redirects and term requests. Independent OAK results
were 1,178 canonical labels, one synonym, five accepted exceptions and 2,056
no-adapter skips; vendored-sync verified 18 artifacts. These are reused results,
not a new full-QC run for this record. MeSH parent semantics were inspected
directly because OAK adapter coverage does not certify them.

## Identity and Grounding

The source identity is exactly `Engineered > Solid waste > Cellulose associated
waste`. The source mint, category and displayed wording agree. The path supplies
the solid-waste scope that the short label alone would not fully explain. It
does not claim that every cellulose-containing object, usable residue or pure
cellulose preparation is waste.

`curation/decisions.tsv` contains the 2026-08-12 CLASS-level
`CONFIRM_UNGROUNDED` for this source. Its explicit note says that the lexical
screen did not assess habitat meaning individually. `SEEDED`, rather than
`REVIEWED`, therefore accurately describes the decision depth. The August 16
seed event follows that decision without adding an ITEM endorsement.

The parent `mesh:D062611` is current [NLM Solid Waste](https://meshb.nlm.nih.gov/record/ui?ui=D062611).
NLM's scope covers discarded refuse and related solid, semisolid or contained
materials, while distinguishing dissolved material in specified liquid flows.
The [structured descriptor](https://id.nlm.nih.gov/mesh/D062611.json) confirms
the identifier, active status and label. Its preferred concept is M0568791.
That scope is compatible with this expressly waste-qualified GOLD concept;
no contrary source evidence establishes a false direct parent.

This differs from the already corrected generic bagasse record: a generic
material can also be retained as useful feedstock, whereas this target has not
been merged into an unqualified cellulose material identity. The bagasse parent
exclusion must not be mechanically copied here.

An ignored-inclusive structured label/synonym search of the local ontology slice
examined cellulose, pulp and solid-waste matches. They include a cellulose-grown
cell culture condition, pulp-bleaching wastewater, formulated methyl-cellulose
paste, biological pulp terms and the broad Solid Waste descriptor. None of
those local matches establishes exact equivalence to this source-defined solid
waste bin. This is not an exhaustive claim about all current ontologies.

## Evidence

**Direct attestation.** The exact committed GOLD inventory row has depth three,
one source node, `gold.ecosystem:4928`, and zero organism, study, biosample and
total-assertion counts. The record correctly omits a collapse note because
there is only one node. Its count and unit omissions follow `ingest_gold`, which
emits the ORGANISM count only when nonzero. Its mapping predicate is also
appropriately absent because the record retains the GOLD source identity.

Exact-path structured scans found no row in the separately governed
`gold_path_biosamples.tsv`, `gold_studies.tsv` or `gold_path_triads.tsv`.
This does not prove absence of biological occurrence, samples in other source
releases, or incomplete-triad observations. No organism prevalence or microbial
mechanism is asserted by the target.

**Parent contribution.** The parent resolves to
`data/habitats/engineered/solid_waste.yaml`. `src/habitatmech/seed.py::ingest_gold`
adds it from the immediate source-path level, not from a cellulose chemical
identity. The parent's own 81 ORGANISM assertions are not this child's count.
This review assesses the direct parent meaning; it does not certify every
MeSH thesaurus-to-subclass conversion in the parent's imported ancestry.

**Descendant observations are separate.** The child at
`data/habitats/engineered/composting__59a6ebe1.yaml` retains
`habitatmech:GOLD.90c526cac3`, two source nodes, GOLD4929 and GOLD4930, and 11
ORGANISM assertions under the longer composting path. Those counts, its NARROW
mapping to compost, and any compost mechanism must not be aggregated into this
target. The child was read only to distinguish provenance; its own identity and
parent relations require a separate individual review.

No DOI, PMID, taxon, gene, mechanism edge, quantitative parameter or claimed
experimental result occurs in the target, so no corresponding literature or
taxon-label validator is applicable. Broad cellulose-decomposition literature
would not identify this exact waste stream or establish an asserted organism.

## Completeness

Ignored-inclusive searches covered the exact identifier, label and slug in
curation tables, graph overlays, history, configuration, raw inventories,
PATHS/RETIRED maps, research reports and the research manifest. The maintained
CLASS decision and GOLD row were found. No target term request, graph overlay,
parent exclusion, external-xref entry, retirement or target-specific session
history was found in those surfaces. Generic cellulose mentions in plant,
forest, compost and host research concern different records and were not
treated as evidence for this target.

A definition, feedstock composition, cellulose fraction, processing state,
temperature, moisture, characteristic taxon or degradation pathway cannot be
filled merely from the label or the composting child. The empty optional fields
are appropriate until original source evidence supports a narrower claim.
No required field or broken internal reference was found.

iModulonDB is not applicable. Cellulose in a source habitat label is not itself
a gene, regulator, strain-specific pathway or transcriptomic-module assertion.
An expression-module search would not establish this source bin's identity.

## Findings

None found: zero blockers, zero major findings and zero minor findings.

The pass is limited to the current source-qualified, unreviewed representation.
It does not transform CLASS screening into biological validation, prove the
availability of a matching ontology term, or endorse inherited mechanisms.

## Recommended Edits

None required for the present bounded representation.

For a future ITEM curation, first recover the source description and establish
which discarded materials the bin includes. Any resulting decision belongs in
`curation/decisions.tsv`; an evidence-backed minted definition belongs in
`curation/term_requests.tsv`. Preserve the source identity unless exact
equivalence is demonstrated. Do not map to pure cellulose, wastewater or compost
solely because each is chemically or operationally related.

## Follow-up Checks

- A future definition or grounding should be checked against both the exact
  GOLD source scope and the candidate ontology definition, not label similarity.
- Preserve GOLD4928, direct count/unit omissions and separation from the two
  composting nodes. Do not sum parent and child observations.
- After authorized curation, dry-seed and inspect
  `just seed-canary habitatmech:GOLD.a1c99dadfc --force`, then run strict target
  validation, history validation, full corpus reproduction and `just qc`.
  Refresh governed map/site products if selected semantic fields change.

## Additional Notes

NLM browser text was accessible. The browser could not open the JSON endpoint,
but direct structured retrieval succeeded and confirmed the same descriptor.
Live GOLD node contents were not independently retrieved; source fidelity is
verified against the committed inventories, not a newly downloaded source dump.

No curation event, history entry, generated product or GitHub item was changed.
The parent and composting child are contextual reads, not extra completed
reviews toward the all-record objective.
