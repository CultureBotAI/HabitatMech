# YAML Record Review: anaerobic digester sludge

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/anaerobic_digester_sludge.yaml`
- Started UTC: 2026-10-07T03:05:49Z
- Finished UTC: 2026-10-07T03:08:23Z
- Verdict: needs curation (0 blocker, 2 major, 0 minor)

## Target

Read the complete generated HabitatRecord and rendered page. Identifier
`ENVO:00003965`, category ENGINEERED, grounding EXACT, mapping REVIEWED.
Two source attestations, two synonyms, two parents, 25 observational PREGO
taxa, and three history events. No definition, xrefs, environmental parameters,
literature evidence, causal graph, discussion or dataset is asserted.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/anaerobic_digester_sludge.yaml`: passed.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/anaerobic_digester_sludge.yaml`: passed, one file, zero errors.
- Read-only Python `build_corpus()` / `build_document()` equality check:
  all fields reproduced, two source concepts, two reviewed sources, 25 taxa,
  three events. This supplemental target check is not the full-corpus gate.
- Full QC and OAK were not repeated per target. The scientific and governed
  input tree is unchanged from `ec95a7191a9b6c9ddaa404c2062f7be9932623a9`.
  The [exact-baseline QC run](https://github.com/CultureBotAI/HabitatMech/actions/runs/37562477062)
  was freshly queried in this review session and is completed/success at that
  SHA; its full-corpus, reference, history and generated-site gates are reused.
  Official typed ENVO and all 25 NCBI Taxonomy IDs were checked afresh below.
- Original GOLD/PREGO source re-extraction and the full 1,026-taxon association
  crosswalk were not available. Public GOLD study pages did not provide usable
  record detail. These limits do not invalidate faithful inventory reproduction.

## Identity and Grounding

Fresh official ENVO OWL at revision
`a2455d1a77e46bb8a664d65a157166b539269042` confirms an active class with exactly
this label, no definition, no typed synonyms, and sole named parent
`ENVO:00002129` anaerobic sludge. That active parent has sole named parent
`ENVO:00002044` sludge, whose definition describes residual semi-solid material
from domestic, industrial or wastewater-treatment processes. The local slice
agrees at `data/raw/ontology_terms.tsv:7423` and
`data/raw/ontology_subclass_edges.tsv:5540`.

The actual resolver uses `gold_composed_label` for
`Engineered > WWTP > Anaerobic digester > Sludge`, yielding the material term
`ENVO:00003965`, not the vessel. PREGO self-grounds on the same identifier.
The ITEM REVIEW decisions at `curation/decisions.tsv:854` and `:1467` apply
to `habitatmech:GOLD.93b148cc23` and `habitatmech:PREGO.8091443436`; both
sources are reviewed, so the generated REVIEWED state and three events agree.
`data/habitats/PATHS.tsv:724` pins the file. The source path is compatible with
the named material; this review does not claim that every possible source
qualification is irrelevant to a future finer-grained model.

Two assertions nevertheless overstep that identity: the material is given
its digester container as a broader class, and its contextual GOLD leaf Sludge
is elevated to an unqualified exact synonym. The plural PREGO synonym is
conservatively RELATED and does not have the same scope problem.

## Evidence

All 14 raw TSVs were parsed and searched by exact field/pipe member for the
target ID, both source mints, labels, GOLD source ID and full path. Seven files
contain relevant target evidence: GOLD ecosystem paths, biosample counts and
studies; ontology terms and subclass edges; PREGO habitats and habitat taxa.
Other Sludge path hits are distinct concepts, not extra attestations here.

- `gold_ecosystem_paths.tsv:474`: nodes 5477/5478, depth four, 14 organisms,
  zero studies/biosamples in that inventory. The first-ID note and 14 ORGANISM
  count are correct; two vocabulary nodes are not two samples.
- `prego_habitats.tsv:79`: 1,026 taxa, 1,026 direct source assertions,
  maximum score 2.34854 and environmental_samples channel. TAXON and ORGANISM
  counts must not be summed. The score is an association score, not abundance
  or the proportion of sludge communities containing the top-ranked taxon.
- `prego_habitat_taxa.tsv:6796` through `:6820`: all 25 IDs, supplied names,
  ranks 1-25 and scores 2.34854 to 1.66219 match. Every retained row has
  direct_flag TRUE, the environmental_samples channel and no corroboration.
  The pool of 1,026 makes the top-25 truncation explicit.
- Fresh official NCBI Taxonomy EFetch resolves all 25 requested IDs directly:
  15 species, ten strains, no aliases and no name mismatches. This verifies
  taxonomy, not the original sample-level occurrence of every association.
  No entry is marked characteristic or independently corroborated; the
  rendered page correctly presents associated taxa rather than exemplars.

The extractor `src/habitatmech/extract.py:331` retains the best association
score per habitat/taxon across channels and ranks the retained subset.
The seeder's PREGO path preserves that observational meaning. Fresh official
PubMed XML for [Zafeiropoulos et al. 2022](https://pubmed.ncbi.nlm.nih.gov/35208748/)
verified PMID 35208748, DOI 10.3390/microorganisms10020293, authors and full
abstract. It describes text and omics-derived co-occurrence associations;
it does not certify these 25 particular pairs. Browser full-text access was
blocked, so no detailed scoring formula is claimed to have been inspected.

[EPA's reactor account](https://www.epa.gov/agstar/how-does-anaerobic-digestion-work),
opened and read in this session, distinguishes the microbial containment unit
from the residual material. Combined with ENVO's material hierarchy, this
supports removing the material-to-container is-a claim, not any universal
sludge composition or reactor operating parameter.

## Completeness

An exact-path GOLD bulk row at `gold_path_biosamples.tsv:439` lists 29
biosamples for ecosystem path ID 5478. `gold_studies.tsv:4088` associates
Gs0156633 with both aerobic activated-sludge and this anaerobic-digester-sludge
path; `:4519` associates Gs0161792 with this path. These separately sourced
bulk counts are not replacements for the 14 ORGANISM count. Neither study's
public GOLD page yielded usable details. A search lead linking Gs0156633 to
DOI 10.1128/msystems.01188-23 could not be opened as primary full text and was
not used to identify any of the 29 biosamples or to add a causal claim.
No target triad or physicochemical parameter row was found.

Ignored-inclusive content searches covered curation, history, configuration,
documentation, tests, PATHS, RETIRED, research and the research manifest;
filename searches also covered research/curation/history. No target-owned
definition, parent exclusion, causal overlay or research report was found.
Mentions in another habitat's research prose were not adopted as evidence.
The absent definition mirrors the ontology release and is not independently
a required-field defect. Empty optional evidence, graph and dataset fields
do not require boilerplate. iModulonDB is not applicable without a named
gene, regulator or expression dataset.

Ignored-inclusive filename searches across `build` and configured kg-microbe
data found no GOLD node/edge or PREGO node/edge dumps. Original association
re-extraction and source-to-sample verification remain bounded limitations.

## Findings

1. **Major: sludge is not a type of its digester container.** The second
   parent, `habitatmech:GOLD.3f58fb59be`, comes from the immediate GOLD path
   and denotes Anaerobic digester. The full parent record was read in the
   immediately preceding individual review. Material in that unit is not a
   subtype of the unit. Preserve the independent ontology parent
   `ENVO:00002129`. Maintained owner: `curation/gold_parent_exclusions.tsv`.
2. **Major: the generic word Sludge is asserted as an exact synonym of the
   narrower anaerobic digester sludge class.** ENVO distinguishes generic
   sludge from this nested subtype. The full GOLD path supplies the missing
   qualifications, but `src/habitatmech/seed.py:878` unconditionally copies
   its leaf as EXACT_SYNONYM. Source provenance does not make that stand-alone
   lexical equivalence true. Maintained owner: the GOLD synonym-emission rule
   in `src/habitatmech/seed.py`, with regressions in
   `tests/test_seed_harmonization.py` and any deliberately introduced scoped
   curation input. No generated-file or raw-label patch is appropriate.

No blocker or minor finding was established. In particular, unusual-looking
ranked taxa are not grounds to discard source observations or call them false
without their underlying association evidence.

## Recommended Edits

1. In a later authorized curation, exclude only the GOLD parent contribution
   keyed by `habitatmech:GOLD.93b148cc23`, exact path
   `Engineered > WWTP > Anaerobic digester > Sludge`, and expected parent
   `habitatmech:GOLD.3f58fb59be`. Preserve the ontology genus, source path,
   both source nodes, both ITEM decisions, EXACT/REVIEWED status, both count
   units, all 25 taxa/ranks/scores, pool and PREGO synonym.
2. Correct the source-leaf synonym scope without deleting the verbatim source
   label from its attestation. For this target, omit the bare Sludge exact
   synonym or retain it under a defensible non-exact scope. Do not manufacture
   a source synonym by silently rewriting raw vocabulary text. Evaluate shared
   rule effects beyond this target before regenerating the corpus.

Both changes require append-only session history and generator-produced
records/pages. Neither requires changing the valid ENVO identity, borrowing
operating temperatures or promoting associated taxa to characteristic taxa.

## Follow-up Checks

Add a parent-exclusion regression proving the independent `ENVO:00002129`
edge remains and only the container edge/event changes. Add a synonym
regression proving Sludge is no longer exact while the source attestation,
PREGO plural synonym and correctly exact source synonyms remain intact.
Run the focused tests, `just seed`, inspect
`just seed-canary ENVO:00003965 --force`, then authorized full regeneration,
`just validate-strict` on the target, `just verify-corpus`, history validation,
site/semantic-product checks and `just qc`; run `just validate-products` for
any grounding change. Shared synonym behavior needs corpus-wide diff review.

## Additional Notes

Read-only review; only this timestamped report was written. No GitHub mutation,
paid research, scientific edit, status promotion or history rewrite occurred.
Some initially guessed test filenames did not exist; ignored-inclusive filename
discovery located `tests/test_seed_harmonization.py`. No missing-infrastructure
finding relies on those failed guesses. The all-record review remains active.
