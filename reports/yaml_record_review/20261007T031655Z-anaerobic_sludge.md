# YAML Record Review: anaerobic sludge

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/anaerobic_sludge.yaml`
- Started UTC: 2026-10-07T03:15:04Z
- Finished UTC: 2026-10-07T03:16:55Z
- Verdict: needs curation (0 blocker, 2 major, 0 minor)

## Target

Read the entire generated HabitatRecord and rendered page. Identifier
`ENVO:00002129`, category ENGINEERED, grounding EXACT, mapping REVIEWED.
Two sources, two synonyms, two parents, one observational taxon and three
events. No definition, xrefs, environmental parameters, record-level literature
evidence, causal graph, discussion or dataset is asserted.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/anaerobic_sludge.yaml`: passed, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/anaerobic_sludge.yaml`: passed, one file, zero errors.
- Read-only `build_corpus()` / `build_document()` equality check: every field
  reproduced; two source concepts, two reviewed sources, one taxon, three
  events. This supplements, not replaces, full-corpus verification.
- Full QC and OAK were not repeated. A fresh diff confirms guidance, code,
  scientific inputs and products are unchanged from
  `ec95a7191a9b6c9ddaa404c2062f7be9932623a9`. Reuse the successful
  [exact-baseline QC run](https://github.com/CultureBotAI/HabitatMech/actions/runs/37562477062),
  whose completed/success status and SHA were checked during the preceding
  continuation, for full-corpus, reference, history and product gates.
  Official ENVO and the taxon ID/name were checked afresh below.
- Original GOLD/PREGO dump re-extraction and the bulk sample crosswalk were
  not available. No claim of fresh end-to-end source re-extraction is made.

## Identity and Grounding

Fresh official ENVO OWL at revision
`a2455d1a77e46bb8a664d65a157166b539269042` confirms active ENVO:00002129,
canonical label anaerobic sludge, no definition or typed synonyms, and sole
named parent `ENVO:00002044` sludge. The latter denotes residual semi-solid
material. Local term/edge rows agree at `data/raw/ontology_terms.tsv:7225`
and `data/raw/ontology_subclass_edges.tsv:5329`.

The actual GOLD resolver composes Anaerobic and Sludge into the correct
material label. It applies the ITEM REVIEW at `curation/decisions.tsv:1371`
for source mint `habitatmech:GOLD.f96483345a`; PREGO's source mint
`habitatmech:PREGO.8e0c7d0275` has ITEM REVIEW at line 1470. Both source
reviews support the generated REVIEWED state and two 2026-08-13 events,
followed by the original 2026-08-16 seed event. PATHS line 648 pins the file.

This current record has one GOLD path, not the three reactor-specific paths
described in older harmonization prose. The actual corpus and
`tests/test_seed_harmonization.py:129` show that the earlier composed-label
conflation was addressed. Do not diagnose a current three-source merge from
that historical description. The present two defects concern the emitted
parent and synonym semantics, not a demonstrated recurrence of that merge.

## Evidence

Parsed exact-field/pipe-member searches of all 14 raw inventories found
relevant target evidence in eight files: four GOLD inventories, two ontology
inventories and two PREGO inventories. Other Sludge leaf hits belong to
distinct source paths and are not additional sources for this target.

- `gold_ecosystem_paths.tsv:175`: exact path
  `Engineered > Bioreactor > Anaerobic > Sludge`, nodes 5481/5482, 123
  organisms, zero studies/biosamples in that inventory. The first-node note,
  exact predicate and ORGANISM unit are preserved.
- `prego_habitats.tsv:693` and `prego_habitat_taxa.tsv:6106`: one TAXON,
  one direct source assertion, score 3, annotated_genomes_isolates channel,
  NCBITaxon:335543, rank one of one, no corroboration. Neither the source
  score nor the single-candidate ranking proves prevalence or characteristic
  status. The plural PREGO synonym remains conservatively RELATED.
- Fresh NCBI Taxonomy EFetch resolves 335543 directly as the strain
  Syntrophobacter fumaroxidans MPOB, matching the supplied name, with no alias.
  The record and page correctly retain a reported association, not
  `is_characteristic: true` or independent GOLD taxon corroboration.

The inspected publisher abstract of [Harmsen et al. 1998](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-48-4-1383)
explicitly reports MPOB's isolation from an enrichment of anaerobic granular
sludge and identifies it with DSM 10017. The DOI, title, authors and publication
date were verified on that page. [NCBI BioProject PRJNA13013](https://www.ncbi.nlm.nih.gov/bioproject/13013)
independently links taxon 335543 to granular sludge from an anaerobic reactor
treating sugar-beet wastewater. The inspected introduction of
[Plugge et al. 2012](https://link.springer.com/article/10.4056/sigs.2996379)
agrees on the isolation context. These checks support the narrow taxon-origin
claim, not every GOLD organism assertion, all sludge habitats, or universal
growth/mechanism parameters. The original PREGO contributing edge was not
reconstructed; no annotation-channel provenance is invented.

`gold_path_triads.tsv:41` through `:43` separately summarize nine samples
from one study per slot: urban biome ENVO:01000249, anaerobic bioreactor
ENVO:00002124 and anaerobic sludge ENVO:00002129 as broad/local/medium,
respectively. Each has one distinct term and top_share 1.00. Fresh official
ENVO verifies those labels. This is contextual evidence distinguishing the
reactor feature from its sludge medium, not a mandate to make all three
habitat identities or claim all sludge is urban.

## Completeness

`gold_path_biosamples.tsv:76` lists 463 bulk biosamples for path ID 5482;
16 study rows contain this exact path, some with other habitats. These
separately sourced bulk counts must not replace or be summed with 123
ORGANISM and one TAXON. Individual study/sample assignments were not verified.
No target physicochemical parameter row was found in the raw scan.

Ignored-inclusive searches covered curation, history, configuration, tests,
PATHS, RETIRED, research and its manifest using the target and source IDs,
label and slug; filename searches covered curation/history/research. No
target-owned definition, causal overlay, parent exclusion or research report
was found. A mention in another habitat's research prose was not adopted.
The missing definition reflects ENVO's own sparse class and is not a separate
required-field defect. Empty optional evidence, graph and dataset slots do
not require filler. iModulonDB is not applicable: the record names no gene,
regulator or expression dataset, and no mechanism is inferred from the
genome paper consulted for isolation provenance.

An ignored-inclusive filename search of `build` and configured kg-microbe
data found no GOLD or PREGO node/edge dumps. This is a bounded source-access
limit, not proof that any observation is false.

## Findings

1. **Major: material-to-container context becomes an is-a edge.**
   `ENVO:00002124` anaerobic bioreactor is not a broader class of anaerobic
   sludge. Fresh ENVO defines the reactor as a bioreactor with non-oxygenated
   contained material; its genus is the containment unit ENVO:00002123. The
   source parent resolves through `curation/decisions.tsv:1305`, and the
   immediate GOLD path loop at `src/habitatmech/seed.py:910` adds it to this
   sludge record. Preserve the independent material genus ENVO:00002044.
   Maintained owner: `curation/gold_parent_exclusions.tsv`.
2. **Major: generic Sludge is an over-broad exact synonym.** The exact GOLD
   source path denotes anaerobic sludge, but the bare leaf Sludge denotes a
   broader material class. `src/habitatmech/seed.py:878` unconditionally emits
   it as EXACT_SYNONYM. The source label should remain in its contextual
   attestation without claiming context-free lexical equivalence. Maintained
   owner: the GOLD synonym rule in `src/habitatmech/seed.py`, with focused
   regressions in `tests/test_seed_harmonization.py`.

No blocker or minor finding was established.

## Recommended Edits

In later authorized curation, add an exclusion for source mint
`habitatmech:GOLD.f96483345a`, exact path
`Engineered > Bioreactor > Anaerobic > Sludge`, expected parent ENVO:00002124.
Preserve ENVO:00002044, both source attestations, both ITEM decisions,
EXACT/REVIEWED state, 123 ORGANISM, one TAXON and the complete MPOB observation.
Let the seeder append its exclusion event; add append-only session history.

Separately repair the generic leaf synonym's scope: omit it as an exact
synonym or retain it under a defensible non-exact scope, while preserving the
verbatim GOLD attestation and PREGO plural synonym. Evaluate shared-rule
effects across the corpus; do not edit raw source vocabulary or generated
YAML/pages to force this record to look correct. No taxon removal, duplicate
merge, new definition or review-status promotion is needed for these repairs.

## Follow-up Checks

Add a focused parent-exclusion regression proving that only ENVO:00002124
is removed and the exclusion event is added. Add synonym tests for this
qualified Sludge leaf and preserved legitimate exact synonyms. Run the
focused tests, `just seed`, inspect `just seed-canary ENVO:00002129 --force`,
then authorized full regeneration, strict target validation,
`just verify-corpus`, history/site checks and `just qc`. A shared synonym
change requires a corpus-wide diff review; changed grounding requires
`just validate-products`. Source refresh is required for full underlying
association certification, but not to identify the two semantic defects.

## Additional Notes

Only this new report was written. No scientific curation, generated artifact,
history rewrite, status change, paid research or GitHub mutation occurred.
The prior continuation made concrete progress by writing four reports; the
full all-record objective remains active, not complete.
