# YAML Record Review: underground water

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/underground_water.yaml`
- Started UTC: 2026-10-06T18:59:33Z
- Finished UTC: 2026-10-06T19:04:11Z
- Verdict: needs curation

## Target

The complete generated `HabitatRecord` was read at baseline
`afb0e096c62b60499197544166fa96dee800a764`: ENVO:00005792, underground water,
AQUATIC, EXACT/SEEDED. It contains an ENVO definition, seven scoped synonym
entries, one parent, one PREGO attestation, 25 associated taxa and one seed
event. This is the water material, not an underground water body, aquifer,
well, or the narrower groundwater concept.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/aquatic/underground_water.yaml`:
  pass, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/aquatic/underground_water.yaml`:
  one file, zero errors; only the ignored validator diagnostic TSV refreshed.
- Actual `seed.build_corpus()` and `seed.build_document()` execution, with
  entire parsed-document equality: pass; one contributing concept, zero
  ITEM-reviewed sources, all 25 taxa and the one event reproduced.
- Current official ENVO RDF/XML was parsed for the target, liquid water,
  groundwater and underground water body. All are nondeprecated classes.
- NCBI Taxonomy efetch resolved all 25 requested IDs unchanged. A second,
  explicit dictionary-equality assertion verified every current scientific
  name against the YAML: 22 strains and three species, no merged-ID aliases.
- The unchanged baseline's complete local, PR and queue QC passed immediately
  before this report-only continuation: 496 tests, three skips, two dependency
  warnings; 107 histories, 3,206 closed-schema records, 32 causal overlays,
  provenance, corpus reproduction, site, redirects and term-request gates.
  [Current main QC 37515033434](https://github.com/CultureBotAI/HabitatMech/actions/runs/37515033434)
  was freshly checked and is successful at the exact baseline SHA. Full QC and
  OAK were not rerun separately for this individual report; the prior local
  OAK gate passed on this same scientific tree.
- Rendered page text was inspected, including its definition, source count,
  direct parent and weaker associated-taxa wording. No browser visual QA.

## Identity and Grounding

The maintained input and [official ENVO at
a2455d1a77e46bb8a664d65a157166b539269042](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
agree on the target ID, label, definition and ENVO:00002006 liquid-water
superclass. AQUATIC is a reasonable coarse category for this material.
The inspected generated liquid-water parent retains its material superclass.

The executed `apply_decision(Resolution(..., route="prego_self_grounded"), ...)`
returns the original ENVO identifier, EXACT, `reviewed=False`, no decision,
no extra parents/xrefs and no mapping predicate. The addressable source key
is `habitatmech:PREGO.e1f659042a`. SEEDED correctly reflects no item-level
curation; EXACT here is self identity, not independent ecological validation.
`PATHS.tsv:736` pins the target's filename.

Groundwater ENVO:01001004 is a named child whose definition concerns pore
spaces in rock or unconsolidated deposits. Underground water body
ENVO:00000061 is a geographical feature. Neither should replace this broader
material identity merely because its label sounds familiar.

The live ontology types `subterranean water` as `hasRelatedSynonym`, not exact.
Its current EXACT_SYNONYM in the YAML is a pipeline error, not a faithful
translation of the typed source. The separate PREGO related entry is weaker
and must not be promoted merely to harmonize duplicate wording.

The definition's clause `beneath the planetary crust` modifies the processes
determining physicochemical properties; it does not literally locate the
water itself there. Nevertheless, crust and surface are not interchangeable,
and the intended scope is unclear beside the ontology's ordinary pore-water
child. This is an upstream wording problem to clarify, not proof that the
record should become a mantle-water concept or a different ontology identity.

## Evidence

All 14 committed raw TSV inventories were scanned structurally with exact
field and pipe-list membership for the ID, source mint and label/variant.

| Input | Verified contribution |
| --- | --- |
| `prego_habitats.tsv:75` | 1,118 distinct taxa, 1,118 direct-flagged input assertions, maximum score 1.33759, environmental_samples channel, seven source variants including the canonical name |
| `prego_habitat_taxa.tsv:6998-7022` | All 25 emitted IDs, names, descending scores and ranks; every direct flag TRUE, every channel environmental_samples, no corroborating source |
| `ontology_terms.tsv:7477` | Canonical label, definition and flattened synonym text |
| `ontology_subclass_edges.tsv:5606` | Liquid-water superclass |
| `ontology_subclass_edges.tsv:6799` | Groundwater's narrower relationship to this term |

`extract.py:330-425` keeps the best score per habitat/taxon, ranks by score,
direct flag and identifier, and retains the top 25. The YAML's TAXON count is
not a sample, isolate, experiment, or abundance count. The direct count counts
flagged input edges and is not generally interchangeable with a distinct-taxon
count just because these two totals happen to agree here. `ingest_prego`
faithfully emits the attestation and associated taxa without asserting
`is_characteristic` or corroboration. Score 1.33759 is not a probability.

The inspected primary [PREGO paper, DOI:10.3390/microorganisms10020293,
sections 2.4 and Appendix C.3](https://imbbc.hcmr.gr/wp-content/uploads/2022/03/2022-Zafeiropoulos-Micro-12.pdf)
describes environmental-sample associations from metagenomic/taxonomic
profiles co-occurring with tagged sample metadata. Its channel-specific score
uses sample counts and is capped at four; it is not a prevalence estimate.
Figure 3 distinguishes sample evidence links from genome/isolate links.
This supports the channel interpretation, not these 25 individual observations.
Neither a strain-valued taxonomy ID nor an imported direct flag establishes
that the exact named strain was cultured from underground water. Conversely,
an unexpected strain name is not sufficient evidence to delete an association.
Original sample identifiers and annotation resolution are needed to settle it.

Two GOLD medium-triad rows independently use the term as sample context:
`gold_path_triads.tsv:199` covers 17 samples/one study for deep-subsurface
Coalbed methane well water, and row 280 covers 15 samples/four studies for
freshwater Coalbed water, with top share 0.60 and three agreeing studies.
These are not extra attestations for the general class or evidence that all
underground water is coalbed water. Broad/local/medium roles remain distinct.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden` across curation,
history, research, conf, docs, src, tests, PATHS and RETIRED with the ID, mint,
label, slug and subterranean-water wording. Focused searches also covered
term requests, causal overlays, exclusions and the research manifest.
No target-owned decision, authored definition, mechanism overlay or research
report was found in these maintained surfaces. Bytecode was excluded.
The all-TSV scan found no target parameter, BacDive or Madin contribution.

An ignored-inclusive filename/path search under the configured kg-microbe
`data/` tree found no PREGO dump under either case variant/source-directory
pattern. The original full graph, sample evidence keys and complete pool were
therefore not independently reconstructed. PREGO's public site failed to load.
The MDPI page returned 429 and PMC a browser challenge; the author institution's
PDF was inspected instead. USGS pages and a direct read-only retry returned
403/timeouts; their search excerpts were not used as inspected scientific
evidence. A BGS page was also unavailable. Access failures are not negative
evidence about the habitat or its microbes.

Empty parameter, literature-evidence, graph, discussion and dataset slots are
not defects by themselves. No universal salinity, depth, oxygen state,
hydrochemistry, microbial function or characteristic community is justified by
the vocabulary source alone. iModulonDB is not applicable: this target has no
gene, regulator, protein, pathway or expression-module assertion.

## Findings

1. **Major: a related ontology synonym is published as exact.** Official
   `hasRelatedSynonym` for subterranean water is promoted to EXACT_SYNONYM.
   Owner: `extract.py:_load_tsv_ontology`, the governed ontology inventory
   representation, and `seed.py:ConceptStore.get` (unconditional exact
   promotion at lines 413-414). Existing [#1249](https://github.com/CultureBotAI/HabitatMech/issues/1249)
   was inspected read-only and remains open. The imported PREGO entry must
   retain its independent weaker provenance.
2. **Minor: upstream definition has an unresolved spatial wording ambiguity.**
   The process-location clause says beneath the crust, not beneath the
   surface/within the crust. Its relationship to the ordinary pore-water
   child is unclear. Owner: the ENVO definition and subsequent governed
   `data/raw/ontology_terms.tsv` refresh, not generated habitat YAML. This is
   not classified as a proven wrong-identity or mantle-location assertion.

Totals: zero blockers, one major finding, one minor finding. Individual PREGO
sample evidence remains unresolved; no false-association finding is asserted.

## Recommended Edits

1. Preserve typed ontology synonyms reproducibly at extraction and emission,
   then regenerate. Do not hand-correct the YAML or relabel the PREGO synonym
   as exact. Include this term in the shared scope-preservation regression.
2. Seek an upstream definition clarification distinguishing process location
   from water location, surface from crust, and underground water from its
   groundwater child. Do not silently substitute a narrower identity or
   overwrite the governed inventory without provenance.
3. Trace the environmental-sample evidence keys for the retained taxa before
   any characteristic-presence, isolation or strain-resolution claim. Preserve
   uncertainty when the original annotations cannot resolve those questions.

## Follow-up Checks

For a later curation change, compare typed synonyms against a pinned ontology,
inspect a dry seed and forced canary, then run strict/open schema, labels,
history, provenance, exact corpus reproduction, term requests and full QC.
Rebuild the semantic map/site if corrected selected text changes their inputs.
Verify all original sample keys and score-channel semantics before changing
taxon assertions. Review both child and material/container boundaries if an
upstream definition changes; a lexical near-match is not an identity decision.

## Additional Notes

This timestamped report is the only authored target change. No scientific
input, record, page, history, old report or GitHub item was modified. The
earlier unfinished Underground water attempt was not counted as a completed
review; the complete current target and relevant checks were repeated here.
The ignored-inclusive census before this report found 1,059 reviewed current
records of 3,206. SSSOM/KGX compatibility and full-corpus completion are not
claimed. The overall record-review goal remains active.
