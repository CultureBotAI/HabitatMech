# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/aquatic/deep_marine_sediment.yaml`
- Started UTC: `2026-09-27T11:38:01Z`
- Finished UTC: `2026-09-27T11:38:01Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/aquatic/deep_marine_sediment.yaml` |
| Class | `HabitatRecord` |
| Identifier | `ENVO:00002113` |
| Label | `deep marine sediment` |
| Category | `AQUATIC` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Source provenance | `ENVIRONMENTS_TABLE` `sediment_marine_deep`, `MADIN` `ENVO:00002113`, and `PREGO` `ENVO:00002113` |
| Generated status | Generated from `data/raw/`, the vendored ontology slice, `curation/causal_graphs/deep_marine_sediment.yaml`, and `src/habitatmech/seed.py`; `data/habitats/PATHS.tsv` pins `ENVO:00002113` to `deep_marine_sediment` |

The complete generated record was read before making this judgment. It contains
the ENVO identifier, definition, exact and related synonyms, one ontology
parent, three source attestations, ten environment-table physicochemical
parameters, 44 observational taxon associations from PREGO and Madin, one
curator-authored causal graph with 12 nodes and 15 edges, and two curation
history events. It has no xrefs, record-level evidence, discussions, external
datasets, or quality flags.

Ignored-inclusive exact searches over `data/raw`, `data/habitats`,
`curation`, `history`, `research`, `reports`, and `conf` for `ENVO:00002113`,
`sediment_marine_deep`, `deep marine sediment`, `deep_marine_sediment`,
`PMID:15618510`, `PMID:35308366`, `PMID:30194429`, and `PMID:11034209` found
the expected ontology rows, PREGO rows, Madin rows, environment-table rows,
`PATHS.tsv` pin, generated target, causal-graph overlay, graph references, and
incidental mentions from adjacent overlays or non-target research. A second
exact search for the three addressable source-concept keys
`habitatmech:PREGO.f1db205755`, `habitatmech:MADIN.5001c198b6`, and
`habitatmech:ENVIRONMENTS_TABLE.dbd62c80d0` found no decision, term-request,
research, history, config, or generated-record occurrence. Those
`rg --no-ignore --hidden` checks included ignored and hidden files. `find`
under `curation/causal_graphs` and `research/habitats` found the maintained
`deep_marine_sediment.yaml` overlay and no exact target-specific research
report.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/deep_marine_sediment.yaml` | Passed; LinkML reported no issues. |
| `just validate-all data/habitats/aquatic/deep_marine_sediment.yaml --out /tmp/habitatmech-deep-marine-sediment-validate-all.tsv` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-strict data/habitats/aquatic/deep_marine_sediment.yaml --quiet --out /tmp/habitatmech-deep-marine-sediment-validate-strict.tsv` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal curation/causal_graphs/deep_marine_sediment.yaml` | Passed; LinkML reported no issues. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs were valid. |
| `just validate-history` | Passed; 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; the corpus has the expected 3206 records and reproduces exactly from `data/raw/`. |
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist-deep-marine-sediment.tsv` | Passed; wrote 953 ungrounded rows and reported 1810 decisions on file. |
| `just report` | Passed; emitted the corpus diagnostic report for 3206 records, including 468 `AQUATIC` records, 2520 `SEEDED` records, 1060 `EXACT` records, and 953 `UNGROUNDED` records. |
| Focused reference validator | Not checked: an ignored-inclusive exact `rg` search of `justfile`, `.claude`, `docs`, `scripts`, `src`, and `tests` found no `validate-references` command. The four graph PMIDs were checked through PubMed E-utilities metadata and abstracts. |

## Identity and Grounding

The ontology identity is supported. `data/raw/ontology_terms.tsv:7209`
contains `ENVO:00002113` with canonical label `deep marine sediment`, the exact
generated definition, and ENVO exact synonyms `deep marine sediments` and
`pelagic sediment {alternative name}`. `data/raw/ontology_subclass_edges.tsv:5311`
contains the direct `ENVO:00002113 rdfs:subClassOf ENVO:03000033` edge, so the
sole generated parent `ENVO:03000033` `marine sediment` is supported.

The three source identities are supported:

| Source | Raw support | Assessment |
|---|---|---|
| `ENVIRONMENTS_TABLE` `sediment_marine_deep` | `data/raw/environment_parameters.tsv:117-126` has ten rows keyed by `sediment_marine_deep`, each with the single term `ENVO:00002113` and label `deep marine sediment`. | Exact self-grounding is supported, and the ten generated qualitative parameters match the raw rows. |
| `MADIN` `ENVO:00002113` | `data/raw/madin_habitats.tsv:55` has `ENVO:00002113`, vocabulary `ENVO`, label `deep marine sediment`, and `taxon_count` 19; `data/raw/madin_habitat_taxa.tsv:436-454` lists exactly 19 taxa. | Exact self-grounding and `assertion_count: 19` / `assertion_unit: TAXON` are supported. The three Madin rows whose `corroborated_by` cell is `PREGO` are the three generated taxa surfaced first. |
| `PREGO` `ENVO:00002113` | `data/raw/prego_habitats.tsv:36` has `taxon_count` 2065, `direct_assertion_count` 2155, max score 4, both generated evidence channels, and the three PREGO synonyms; `data/raw/prego_habitat_taxa.tsv:5962-5986` has the emitted top-25 taxa. | Exact self-grounding is supported. The generated attestation correctly uses `taxon_count` as `assertion_count` with `TAXON` units, and the generated top-25 taxa preserve rank, score, source, labels, and the blank label for `NCBITaxon:158080`. |

The generated `mapping_status: SEEDED` is also supported. PREGO, Madin, and
the environment table all point directly at the ENVO CURIE, but the exact
addressable keys for those source concepts are absent from `curation/decisions.tsv`,
so no item-level `REVIEW` or override has promoted the merged record to
`REVIEWED`.

## Evidence

The record has no record-level `evidence` objects. Its source-attestation,
definition, hierarchy, environmental-parameter, and observational-taxon claims
trace to source inventories and ontology rows as described above.

The curated `deep_marine_sediment_sulfate_methane_transition` graph is
maintained in `curation/causal_graphs/deep_marine_sediment.yaml` and is
attached to the generated record by the seeder. Its 15 edges all have
syntactically valid PMID evidence, and the snippets are exact short substrings
from the cited metadata or abstracts for PMID:15618510, PMID:35308366,
PMID:30194429, and PMID:11034209. Several edge descriptions, however, go beyond
those snippets' scope:

| Edge | Cited support checked | Assessment |
|---|---|---|
| `deep_sediment_buries_marine_organic_matter` | PMID:15618510 is D'Hondt et al. on microbial-activity distributions in deep subseafloor sediments and reports that major activity rates principally rely on electron donors and acceptors from the photosynthetic surface world. | Partly supported, but the evidence does not specifically support the subject/object edge that deep marine sediment accumulates buried marine organic matter. |
| `organic_burial_creates_anoxic_porewater` | PMID:35308366 states that sulfate reduction is quantitatively important for organic-matter degradation in anoxic marine sediment. | Over-scoped: the cited abstract supports sulfate reduction in anoxic marine sediment, not the causal claim that buried organic matter degradation leaves deep marine porewaters anoxic. |
| `depleted_sulfate_permits_methanogenic_sediment` | PMID:15618510 compares microbial activities in deep subseafloor sediments. | Under-supported: the cited abstract does not state that sulfate depletion at depth permits methanogenic sediment zones below sulfate-reducing marine sediment. |
| `smtz_hosts_sulfate_reducers` | PMID:11034209 is Boetius et al. on a gas-hydrate-rich sediment consortium mediating anaerobic methane oxidation. | Over-scoped: the source supports sulfate-reducing bacterial partners in an archaeal-bacterial methane-oxidizing consortium, but not that marine sulfate-methane transition zones generally host those partners. |

The Beulig et al. sulfate-methane transition source, PMID:30194429, supports
the SMTZ, ANME-1, and methane-oxidation edges more directly: its abstract
describes methane oxidation with sulfate before methane reaches the water
column, defines the sulfate-methane transition as the sediment horizon where
downward sulfate and upward methane fluxes meet, reports ANME-1 archaeal gene
pools within and beneath that transition, and reports enzymatic potential for
methane production and consumption.

## Completeness

The ENVO definition, ENVO parent, three source attestations, ten environment
parameters, and 44 generated observational taxon associations are complete for
the committed raw rows that feed this record.

The causal graph is structurally complete but not evidentially complete:
`scripts/validate_causal_graph_curations.py` checks overlay schema, duplicate
graph IDs, node and edge presence, dangling edge endpoints, duplicate edge IDs,
empty predicates, missing evidence lists, and missing evidence references. It
does not inspect PubMed content or prove that a snippet supports an edge
description. Manual PMID checks found the over-scoped graph claims described
in `HM-DEEP-MARINE-SEDIMENT-001`.

Append-only curation history is missing for the maintained overlay. Exact
ignored-inclusive searches of `history/` for `deep_marine_sediment`,
`sulfate-methane`, `PMID:15618510`, `PMID:35308366`, `PMID:30194429`, and
`PMID:11034209` found no session record documenting the 2026-09-04 graph
addition, even though the generated record has an inline
`ADD_CAUSAL_GRAPH` curation event copied from the overlay.

The three source concepts have no item-level decisions yet. Because they are
direct self-grounded source concepts and the record remains `SEEDED`, this is
a review-depth gap rather than a generated-YAML defect.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| HM-DEEP-MARINE-SEDIMENT-001 | Major | Four causal-graph edges overrun the exact scope of their cited evidence. | PubMed E-utilities metadata and abstracts confirm that the D'Hondt PMID supports deep-subseafloor microbial-activity distributions, the Nagakura PMID supports sulfate reduction in anoxic Guaymas Basin sediment, and the Boetius PMID supports gas-hydrate-rich methane-oxidizing consortia. Those sources do not exactly support the current `deep_sediment_buries_marine_organic_matter`, `organic_burial_creates_anoxic_porewater`, `depleted_sulfate_permits_methanogenic_sediment`, or `smtz_hosts_sulfate_reducers` edge descriptions. | Rewrite or re-evidence the affected edges in `curation/causal_graphs/deep_marine_sediment.yaml`, then regenerate the target record through the seeder. |
| HM-DEEP-MARINE-SEDIMENT-002 | Minor | The maintained causal-graph overlay has no append-only `history/` session record. | The overlay adds a 2026-09-04 `ADD_CAUSAL_GRAPH` event, but ignored-inclusive exact searches of `history/` for the graph slug, mechanism phrase, and four PMIDs found no provenance record. `history/README.md` states that curation-history presence is advisory, not blocking, so the valid overlay can still seed and pass CI. | Add a corrective history record beside the next edit to `curation/causal_graphs/deep_marine_sediment.yaml`. |

## Recommended Edits

1. Update `curation/causal_graphs/deep_marine_sediment.yaml` so
   `deep_sediment_buries_marine_organic_matter`,
   `organic_burial_creates_anoxic_porewater`,
   `depleted_sulfate_permits_methanogenic_sediment`, and
   `smtz_hosts_sulfate_reducers` either carry evidence that directly supports
   their current subject-predicate-object and description text or are narrowed
   to the claims their cited papers actually make.
2. Prefer deep-marine or deep-subseafloor sediment sources for edges that are
   specific to this habitat. If an edge is intentionally about a broader
   marine-sediment methane-cycle pattern, either move it to the broader
   `marine_sediment` graph or word its description so the broader scope is
   explicit.
3. When editing the overlay, scaffold an append-only session record with
   `just new-history --kind other --path curation/causal_graphs/deep_marine_sediment.yaml --slug deep_marine_sediment ...`
   and describe which graph edges were rewritten, which PMIDs were retained or
   replaced, and which validators were rerun.
4. Add item-level `REVIEW` rows for `habitatmech:PREGO.f1db205755`,
   `habitatmech:MADIN.5001c198b6`, and
   `habitatmech:ENVIRONMENTS_TABLE.dbd62c80d0` only after a curator is ready
   to promote the exact self-grounded sources to `REVIEWED`.

## Follow-up Checks

1. Run `just validate-causal curation/causal_graphs/deep_marine_sediment.yaml`.
2. Run `just seed` and `just seed-canary ENVO:00002113`.
3. Inspect `data/habitats/aquatic/deep_marine_sediment.yaml` and confirm that
   the causal graph was regenerated from the overlay and not edited directly.
4. Run `just validate data/habitats/aquatic/deep_marine_sediment.yaml`.
5. Run `just validate-all data/habitats/aquatic/deep_marine_sediment.yaml`.
6. Run `just validate-causal-all`.
7. Run `just validate-history`.
8. Run `just term-requests-check`.
9. Run `just verify-corpus --max-diffs 1`.
10. Manually recheck every retained PMID snippet against the cited paper, not
    just PubMed metadata, because edge descriptions carry mechanism claims.

## Additional Notes

The only GOLD evidence touching `ENVO:00002113` in the current report inputs is
contextual MIxS-triad evidence from other minted records: for example, the
GOLD `Environmental > Aquatic > Marine > Ocean trench > Sediment` path has
`ENVO:00002113` as its `medium` term across two studies. That does not make
GOLD an attestation source for this ontology-grounded PREGO/Madin/environment
table record.
