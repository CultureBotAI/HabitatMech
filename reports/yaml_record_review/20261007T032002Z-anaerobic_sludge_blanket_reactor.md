# YAML Record Review: anaerobic sludge blanket reactor

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/anaerobic_sludge_blanket_reactor.yaml`
- Started UTC: 2026-10-07T03:17:54Z
- Finished UTC: 2026-10-07T03:20:02Z
- Verdict: pass with minor issues (0 blocker, 0 major, 1 minor)

## Target

Read the full generated HabitatRecord and rendered page. Identifier
`ENVO:00002213`, ENGINEERED / EXACT / SEEDED. It has an ENVO definition,
one RELATED plural synonym, parent ENVO:00002124, one PREGO attestation,
six observational taxa and one seed event. No xrefs, environmental parameters,
record-level literature evidence, causal graph, discussion or dataset.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/anaerobic_sludge_blanket_reactor.yaml`: passed.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/anaerobic_sludge_blanket_reactor.yaml`: passed, one file, zero errors.
- Read-only `build_corpus()` / `build_document()` equality check reproduces
  all fields: one source, zero reviewed sources, six taxa and one event.
  This supplemental check is not the documented full-corpus gate.
- Full QC and OAK were not repeated. The scientific tree is unchanged from
  `ec95a7191a9b6c9ddaa404c2062f7be9932623a9`; reuse the successful
  [exact-baseline QC run](https://github.com/CultureBotAI/HabitatMech/actions/runs/37562477062)
  for full-corpus, reference, history and product checks. Its success/SHA
  were verified in the preceding continuation. Official ENVO and all six
  NCBI Taxonomy IDs were freshly checked for this record.
- Original PREGO and taxonomy source re-extraction, including the underlying
  sample-level association evidence, was not available.

## Identity and Grounding

Fresh official ENVO OWL at revision
`a2455d1a77e46bb8a664d65a157166b539269042` confirms active ENVO:00002213,
exact canonical label and verbatim definition, no typed synonyms and sole
named parent ENVO:00002124 anaerobic bioreactor. That active parent denotes
a reactor whose contained material is not oxygenated, with genus bioreactor.
Local rows at `data/raw/ontology_terms.tsv:7295` and
`data/raw/ontology_subclass_edges.tsv:5408` agree. The definition source is
correctly ENVO, not a claim that HabitatMech independently authored it.

PREGO self-grounds on this ontology ID. Its source-concept decision key is
`habitatmech:PREGO.1c620d00b6`, with no decision found in the ignored-inclusive
curation search. Zero reviewed sources and the one original 2026-08-16
event correctly produce SEEDED. PATHS line 680 pins the file. The plural
PREGO synonym is conservatively RELATED; there is no generic exact source
synonym or GOLD-context parent in this record.

## Evidence

The parsed exact-field/pipe-member scan of all 14 raw inventories found target
evidence only in the two ontology and two PREGO files.
`prego_habitats.tsv:382` gives six taxa, six direct source assertions, maximum
score 1.11189, environmental_samples and the singular/plural source synonyms.
`prego_habitat_taxa.tsv:6299` through `:6304` contain all six emitted IDs,
ranks and scores (1.11189 through 1.01893), direct_flag TRUE, the same channel,
and no corroboration. Pool six is the complete retained inventory, not proof
that a reactor community contains only six organisms. Scores are source
association scores, not abundance, oxygen tolerance or methanogenic function.

Fresh NCBI Taxonomy EFetch resolves all six IDs directly, with no aliases:
four species-rank entries and two strains. All five supplied labels match.
The absent sixth name resolves as **Toxopoda sp. 2 RM-2008**, NCBITaxon:517543.
A separate direct taxonomy fetch verifies its lineage under Insecta/Diptera.
That nonmicrobial association is a reason to inspect original environmental
sample evidence, not sufficient evidence to declare the source association
false or silently filter it. The record does not mark any taxon characteristic,
and the rendered page explicitly presents reported associations.

The publisher abstract of [Lettinga et al. 1980](https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/bit.260220402)
was opened and read, and its DOI/title/authors/year were corroborated by the
authors' institutional publication record. It describes experimental and
full-scale upflow anaerobic sludge blanket treatment systems, consistent with
the reactor interpretation. The paper also explores other uses of the broader
USB design: it does not justify broadening this ENVO-defined methanogenic
class to every sludge-blanket process. No operating values, six-taxon presence,
or causal edges are inferred from the abstract. Full experimental text was
not inspected.

## Completeness

Ignored-inclusive searches used the ontology ID, label, slug and source mint
across curation, history, configuration, documentation, tests, PATHS, RETIRED,
research and the research manifest. No target-specific authored definition,
decision, causal overlay, history session or research report was found within
those bounds. Mentions in the separate dissolved-organics research/definition
identify this as a narrower reactor design, not additional target attestations.
No GOLD, BacDive, Madin or parameter contribution was found in the raw scan.

Empty optional mechanisms and datasets need not be filled. The one missing
taxon label is the only established presentation/provenance gap. iModulonDB
is not applicable: no gene, regulator or expression dataset is named.

Case-insensitive, ignored-inclusive filename searches across `build` and the
configured kg-microbe data directory found neither PREGO node/edge files nor
`ncbitaxon_nodes.tsv`. Thus the full source associations and original label
lookup cannot be re-extracted here; this review does not infer why the old
taxonomy slice lacked the name. A prior case-sensitive candidate filename
search was superseded by the case-insensitive search using the actual
extractor filename.

## Findings

1. **Minor: resolvable taxon name missing at rank six.**
   NCBITaxon:517543 has no `taxon_label` in the YAML or the owned input
   `data/raw/prego_habitat_taxa.tsv:6304`; the page consequently displays
   only its CURIE. Fresh NCBI resolves Toxopoda sp. 2 RM-2008. Maintained
   owner: the versioned taxonomy input used by
   `src/habitatmech/extract.py:650` (`_load_taxon_labels`) and governed PREGO
   extraction, not generated YAML or the rendered page.

No blocker or major finding was established. ID validity is not independent
verification of every habitat association, and sparse/nonmicrobial source
observations must not be relabeled as methanogenic or characteristic taxa.

## Recommended Edits

In later authorized source maintenance, recover or refresh the governed
`data/transformed/ontologies/ncbitaxon_nodes.tsv` input with documented
version/provenance, confirm the canonical name, and rerun the supported
inventory extraction so the name reaches the PREGO row. Investigate source
drift before accepting a new manifest. Do not repair only raw bytes and
checksums or fill the generated record by hand.

Preserve the habitat identity/definition/parent, all six IDs and ranks,
scores, pool six, environmental_samples channel, RELATED plural synonym and
SEEDED state. Do not delete the sixth observation solely on lineage or use
the naming repair to assert a new habitat association. Add applicable
append-only session history and regenerate affected scientific/site products
through the normal workflow.

## Follow-up Checks

Test name loading from a known taxonomy input and verify the target's six
associations remain otherwise identical. Run inventory provenance checks,
`just seed`, inspect `just seed-canary ENVO:00002213 --force`, then authorized
full regeneration, strict validation, `just verify-corpus`, site/semantic-map
checks and `just qc`. Name enrichment changes searchable semantic content;
verify actual generated products rather than fabricating a map update.
Inspect original PREGO sample-level support before any separate association
retraction. OAK's environment-label gate does not replace the NCBI check.

## Additional Notes

Only this timestamped review report was written. No curation, extraction,
generated-product edit, paid research, status promotion or GitHub mutation
occurred. The all-record objective remains active.
