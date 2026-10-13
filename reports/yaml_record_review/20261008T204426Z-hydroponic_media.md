# YAML Record Review: Hydroponic media

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/hydroponic_media.yaml`
- Started UTC: 2026-10-08T20:42:08Z
- Finished UTC: 2026-10-08T20:44:26Z
- Verdict: needs curation (0 blocker, 1 major, 0 minor)

## Target

Read the complete generated HabitatRecord `habitatmech:GOLD.7e1e8d505b`
at `0d14407137e4623255d49890dc49ae309080af1f`: ENGINEERED / UNGROUNDED /
SEEDED, one GOLD attestation, one parent and two generated events. No
definition, synonym, xref, taxon, parameter, literature, causal graph,
discussion or dataset is asserted. The complete Plant growth chamber parent
was read as context, not counted as another completed review.

## Validation

Fresh `UV_CACHE_DIR=build/uv-cache just validate` and `just validate-strict`
on the target passed: no open-schema issues, one strict-valid file and zero
errors. Fresh full-index `build_corpus` / `build_document` exactly reproduces
every target field: one source, zero ITEM-reviewed sources, one parent, no
authored definition or applied source-parent exclusion. The source mint and
default/applied GOLD routes were recomputed with complete indexes.

The immediately preceding publication's full local QC completed on the current
scientific baseline: 598 tests passed, three skipped; 203 valid histories;
all 3,208 records strict-valid and exactly reproduced; provenance, curation
floor, graphs, map/site, redirects, term requests and corpus report passed.
The receipt `build/pr1751-qc.log` was inspected again. A fresh tracked diff
confirms no guidance, implementation, scientific input, history or generated
record changes since that head. Those full-corpus gates are reused, not
claimed freshly rerun for this report. Separate label correspondence passed
under its configured adapter policy; it cannot establish a minted source's
meaning or is-a semantics. No target graph or molecular assertion needs a
separate validator. Required CI and SSSOM/KGX compatibility are not certified.

## Identity and Grounding

`PATHS.tsv:2221` agrees with the full-path mint. The exact path is
`Engineered > Artificial ecosystem > Plant growth chamber > Hydroponic media`.
The default `gold_unmatched` route retains the mint and no mapping predicate.
The CLASS CONFIRM_UNGROUNDED at `curation/decisions.tsv:748` yields
`curated_confirm_ungrounded_from_gold_unmatched`, still reviewed=False.
This lexical screen is not an ITEM assessment or proof that no ontology
anywhere contains a suitable term. SEEDED is correct for that provenance.

The sole parent `habitatmech:GOLD.86cf49cefb`, Plant growth chamber, is added
independently by the GOLD parent pass at `src/habitatmech/seed.py:923-946`.
The parent exists, is UNGROUNDED / SEEDED, and has no authored definition.
The path is legitimate source context, but a growth medium is not a kind of
the apparatus or enclosed setting containing it.

The inspected [NASA hydroponics account](https://spinoff.nasa.gov/Spinoff2010/er_1.html)
distinguishes nutrient solutions from a plant growth chamber in which
hydroponic cultivation occurs. The inspected
[University of Minnesota Extension account](https://extension.umn.edu/garden-and-home/yard-and-garden/gardening-in-minnesota/small-scale-hydroponics)
separates nutrient solution, root-supporting substrates, pots and containers.
Together they support the material-versus-enclosure distinction, not a
source-member crosswalk or an exact definition of GOLD's bin. Whether that
bin includes only nutrient liquid, solid supports, or both remains unresolved.
Do not select generic water, soil, a recipe or a chemical identity by guess.

## Evidence

- `gold_ecosystem_paths.tsv:878` gives depth four, two collapsed nodes
  5551 / 6284, one ORGANISM assertion and zero study/biosample counters in
  this extraction. The generated first ID, collapse note, count and unit
  agree. The row does not identify the organism or its nutrient recipe.
- A fresh [public GOLD workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
  retains node 6284 under this path with an Unclassified filler. It supports
  the current classification, not an independent live confirmation of the
  historical node 5551 or the organism count.
- The fresh [GOLD organism tree](https://gold.jgi.doe.gov/download?mode=organismEcosystemsJson)
  shows zero for this branch and its Unclassified child, versus the frozen
  inventory's one. This is an explicit source-version discrepancy; it does
  not prove extraction error, retirement or biological absence. Do not
  replace the historical count or invent a reason without original joins.
- A complete CSV exact-field/pipe-member scan of every raw TSV recovered
  only the target ecosystem-path row for this ID, label, path and both node
  IDs. No direct target study, bulk-biosample, triad, taxon or parameter row
  was found in that scan. The parent's 96 historical organisms are not
  additional target observations.

NASA's crops and nutrient-monitoring examples and Extension's substrates
are not organism, chemistry, growth-condition or performance claims for
this GOLD record. No such assertions should be imported from those examples.

## Completeness

Ignored-inclusive content searches covered the identifier, label, stem and
both source nodes across curation, all raw inventories, PATHS/RETIRED, conf,
docs, tests, history, research and individual reports. Filename traversal
also covered curation/history/research. Only the path lock, CLASS decision
and source row were found; no target-owned definition, overlay, exclusion,
session history, research dossier or previous individual review was found
within those bounds. An ignored-inclusive hydroponic-string search of the
ontology slice, configuration and curation found no candidate spelling;
that bounded lexical miss is not a global ontology absence claim.

Fresh ignored-inclusive `find` under build, data/raw and the configured
kg-microbe data directory found none of the named original GOLD node/edge
dumps, goldData.xlsx, gold_biosample_triads.tsv or biosample JSONL files.
Manifest receipts do not recover their member joins. Optional ecology and
mechanisms remain correctly empty. iModulonDB is not applicable because no
gene, regulator, expression dataset or strain-level mechanism is asserted.

## Findings

1. **Major: medium-to-chamber context is emitted as strict is-a.**
   Hydroponic media are not a subtype of Plant growth chamber. The
   maintained owner of this exact source contribution is
   `curation/gold_parent_exclusions.tsv`, applied by `ingest_gold`.
   This is a semantic relation defect, not a missing parent reference.
   Zero blockers and zero minor findings.

## Recommended Edits

Exclude only the contribution keyed by `habitatmech:GOLD.7e1e8d505b`, the
exact full path above, and expected parent `habitatmech:GOLD.86cf49cefb`.
Preserve mint, source path, both historical nodes, one ORGANISM assertion,
UNGROUNDED/SEEDED state and previous events. Do not invent a definition merely
to remove an edge. A future ITEM identity review belongs in
`curation/decisions.tsv`; any evidence-backed material definition belongs in
`curation/term_requests.tsv` after its liquid/support scope is established.

## Follow-up Checks

Add a full-corpus before/after regression proving only target parent/history
change, with stale path/expected-parent guards. Recover original members to
resolve the count discrepancy and material scope. Authorized curation should
append session history, dry-seed, inspect the target canary, then pass strict,
history, provenance, labels and exact reproduction. Compare full semantic
inputs and genuinely rebuild changed map/site products before full QC.
Do not treat this target review as approval of its parent or other chambers.

## Additional Notes

Only this new report was written; scientific inputs, generated artifacts,
old reports, histories, statuses and GitHub were unchanged. No paid research
or delegation. Fresh public GOLD bytes were parsed in memory:

- Workbook: 84,174 bytes, SHA256
  `f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.
- Organism tree: 1,450,415 bytes, SHA256
  `49ef0a3e654a79f6b7e7140d2cdb2ac0ce0bb1df2ccb8decae68d129eeb7ca11`.

The workbook's missing-default-style warning did not prevent parsing;
worksheet dimensions were reset before complete row traversal.
