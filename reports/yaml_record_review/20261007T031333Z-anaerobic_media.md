# YAML Record Review: Anaerobic media

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/anaerobic_media.yaml`
- Started UTC: 2026-10-07T03:12:00Z
- Finished UTC: 2026-10-07T03:13:33Z
- Verdict: pass (0 blocker, 0 major, 0 minor)

## Target

Read the entire generated HabitatRecord and rendered page. Identifier
`habitatmech:GOLD.bab80a1f4c`, label Anaerobic media, category ENGINEERED,
grounding UNGROUNDED, mapping SEEDED. The exact target is the material class
under `Engineered > Lab enrichment > Defined media > Anaerobic media`.
One source attestation, one parent, eight ORGANISM assertions and two history
events. No definition, synonyms, xrefs, environmental parameters, taxa,
record-level literature evidence, causal graph, discussion or dataset.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/anaerobic_media.yaml`: passed, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/anaerobic_media.yaml`: passed, one file, zero errors.
- Read-only Python full `build_corpus()` / `build_document()` comparison:
  all fields match, one source concept, zero reviewed sources, zero taxa,
  two history events. This is a supplemental target comparison, not a
  replacement for documented full-corpus verification.
- Full QC and OAK were not repeated per record. A fresh scientific/product
  diff is empty against baseline `ec95a7191a9b6c9ddaa404c2062f7be9932623a9`.
  The [exact-baseline QC run](https://github.com/CultureBotAI/HabitatMech/actions/runs/37562477062)
  was freshly queried in this session and is completed/success at that SHA.
  Its reference, history, full-corpus and generated-product gates are reused.
  The target and its immediate parent have minted IDs, not ontology identities
  whose labels can be independently certified by OAK.
- Original GOLD source-node/organism re-extraction and individual bulk
  biosample crosswalks were not available; their counts are verified against
  the committed inventories only.

## Identity and Grounding

`data/raw/gold_ecosystem_paths.tsv:558` contains the exact depth-four path,
nodes `gold.ecosystem:3856|gold.ecosystem:4289`, two vocabulary nodes, eight
organisms, zero studies and zero biosamples in that inventory. The full-path
mint recomputes to `habitatmech:GOLD.bab80a1f4c` and the filename agrees with
`data/habitats/PATHS.tsv:2658`. The first-ID attestation, duplicate-node note
and ORGANISM unit are faithful. Two source nodes are not two samples.

Actual GOLD resolution is `gold_unmatched`, preserved by the CLASS
CONFIRM_UNGROUNDED decision at `curation/decisions.tsv:1049`. No ontology
mapping predicate is emitted for the minted source concept. The CLASS event
and original 2026-08-16 seed event agree with SEEDED, not REVIEWED.

Read the complete immediate parent record
`data/habitats/engineered/defined_media__b53817a1.yaml`. It denotes Defined
media on the exact prefix path, ID `habitatmech:GOLD.a60b6f216d`, independently
recomputed by the resolver and pinned at PATHS line 2517. Its source inventory
row is line 602 and its CLASS decision is line 954. Anaerobic media within
this defined-media path are a specialization of that material class, not a
material-to-vessel or material-to-procedure edge. This does not claim that
every anaerobic growth medium outside this path is chemically defined, nor
does it adjudicate the parent's own Lab enrichment parent.

## Evidence

The all-14-inventory exact-field/pipe-member scan found relevant rows in only
the GOLD ecosystem, biosample and study tables. Source identity and eight
ORGANISM assertions are supported by the ecosystem row; no taxa can be
reconstructed from that count alone.

`gold_path_biosamples.tsv:308` separately lists 65 biosamples for path ID 4289.
Sixteen rows in `gold_studies.tsv` contain the target path, sometimes alongside
other habitats; for example Gs0047444 spans 14 paths. These bulk-export
associations are contextual leads, not recipes, not 65 taxa and not a
replacement for the organism inventory. Their distinct provenance is recorded
in `data/raw/GOLD_MANIFEST.yaml`. No exact-path triad or physicochemical
parameter row was found. The individual study/sample assignments were not
verified from live source pages and are not promoted to record claims.

Fresh publisher abstract and official PubMed XML inspection verified
[Karasawa et al. 1995, A defined growth medium for Clostridium difficile](https://www.microbiologyresearch.org/content/journal/micro/10.1099/13500872-141-2-371),
PMID 7704267, DOI 10.1099/13500872-141-2-371, authors, date and full abstract.
Its experiment demonstrates that defined medium is an actual microbial growth
substrate, not merely a laboratory procedure. It is only an illustrative
material-class check: none of the tested organisms, recipe components or
experimental results is inferred to belong to the eight GOLD assertions.
The methods/full experimental text was not inspected, so no particular
anaerobic preparation, incubation or performance claim is adopted from it.

The historical sample screen at
`curation/samples/class_swept_unscreened-20260814.tsv:27` also calls this
source concept a habitat material. That row is prior curatorial judgment,
not independent primary evidence and not an ITEM decision consumed by the
seeder. It does not authorize changing the generated review status or
rewriting the earlier CLASS-event wording.

## Completeness

Ignored-inclusive searches for ID, label, slug and exact path covered
curation, history, configuration, documentation, tests, research, research
manifest, PATHS and RETIRED. Filename searches also covered
research/curation/history. Beyond the CLASS decision, path pin and historical
sample row, no target-owned definition, causal overlay or research report was
found within those bounds.

A bounded search of the local ontology slice found a generic culture-medium
candidate but no exact anaerobic-defined-media term; the actual resolver is
also unmatched. A broad culture-medium class would not establish exact
identity. This is not a global absence claim about all ontologies.

The record is complete enough for its modest seeded provenance claim. Empty
optional fields need not be filled with a guessed formula, oxygen threshold,
gas mixture, temperature, organism or mechanism. iModulonDB is not applicable
without a named gene, regulator or expression dataset. The session's
ignored-inclusive search across `build` and configured kg-microbe data found
no GOLD node/edge dumps, so original source-edge verification remains a
bounded limit, not a scientific finding.

## Findings

None found: zero blocker, major or minor findings. This pass validates the
record's current scoped assertions; it does not certify all underlying
sample annotations or imply human review.

## Recommended Edits

None required by this review. Optional future ITEM curation could define this
qualified material class in `curation/term_requests.tsv` and document a
verified broader term through the maintained decision/definition surfaces.
That would require source-scoped evidence and append-only session history.
Do not ground it exactly to a generic culture-medium class, expand it to all
anaerobic media, hand-edit generated files or promote SEEDED from this report.

## Follow-up Checks

For any authorized curation, run `just seed`, inspect
`just seed-canary habitatmech:GOLD.bab80a1f4c --force`, then regenerate through
the documented workflow and run target strict validation, `just verify-corpus`,
history/site checks and `just qc`; use `just validate-products` for new
ontology grounding. Source-count certification would additionally require
the governed GOLD dumps and a scoped sample/organism crosswalk. Recipe-level
claims would require separate recipe evidence, not a class-level label.

## Additional Notes

Read-only review. Only this new timestamped report was written; no scientific
input, record, rendered page, mapping status, curation event or GitHub item
changed. No paid research or SSSOM/KGX readiness certification occurred.
The all-record review goal remains active.
