# YAML Record Review: Genetically modified

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/genetically_modified.yaml`
- Started UTC: 2026-10-08T16:44:59Z
- Finished UTC: 2026-10-08T16:47:22Z
- Verdict: needs curation

## Target

Generated HabitatRecord `habitatmech:GOLD.2eecc8ad2c`, Genetically modified,
ENGINEERED / NOT_APPLICABLE / REVIEWED. The complete target and immediate
Laboratory developed parent were read. Sole source path:
`Engineered > Laboratory developed > Genetically modified`. Baseline: d3576b026.
This is not the distinct Lab synthesis > Genetic cross concept.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/genetically_modified.yaml`:
  passed, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/genetically_modified.yaml`:
  passed, one file, zero errors.
- Fresh full-corpus construction exactly reproduces the complete parsed target:
  one source, one ITEM-reviewed contributor. Actual target and parent resolution
  ran with full ontology, mapping and claimant indexes; both mints were recomputed.
- Full QC is reused, not rerun for report-only additions. Fresh same-turn tree
  comparison proves baseline d3576b026 equals validated cafc537cd: 594 tests
  passed, three skipped, and all remaining local gates passed, including 191
  histories, 3,207 strict-valid/reproduced records, 32 overlays, provenance,
  curation floor, site, redirects, term requests and report. Head/queue QC,
  labels and vendored checks passed; [PR #1735 receipt](https://github.com/CultureBotAI/HabitatMech/pull/1735#issuecomment-6064561377).
- Original organism joins and SSSOM/KGX compatibility were not verified.
  The target has no literature/graph references or separate session history
  needing an additional focused validator.

## Identity and Grounding

The source mint agrees with `PATHS.tsv:1632`. Automatic resolution is
`gold_unmatched`, UNGROUNDED, with no predicate or extra parents. The ITEM
NOT_APPLICABLE row at `curation/decisions.tsv:359` produces
`curated_not_applicable_from_gold_unmatched`, retains the mint, and correctly
does not assert an ontology mapping. REVIEWED follows from the sole contributor's
ITEM decision; its two events match that decision and source seeding.

The maintained scope judgment is defensible: this path classifies an organism
or sample by genetic modification, not the place in which it lives. Keeping a
citable non-habitat source category is intentional; it should not be forced
into an environment identity, genotype term, host-associated environment or
specific engineering technique.

The sole parent `habitatmech:GOLD.77c5518fff` Laboratory developed comes from
the immediate GOLD path, not the target decision. The parent defaults to
`gold_unmatched` and remains UNGROUNDED under its CLASS CONFIRM_UNGROUNDED row
at `curation/decisions.tsv:713`. It is not ITEM-reviewed. There is no independent
ontology, ambiguous-leaf or authored-definition parent for the target.

The seeder's NOT_APPLICABLE branch supplies no parent, but `ingest_gold` later
adds the source-path parent without a grounding-status restriction. This preserves
a source classification as a positive `parent_habitats` assertion despite the
reviewed non-habitat scope. A development-provenance hierarchy is not a strictly
broader-habitat relation. Keeping the verbatim source path is sufficient to
retain that provenance without claiming a habitat genus.

## Evidence

- `gold_ecosystem_paths.tsv:28` supplies nodes 4386/4725/4726, the exact
  path, 1,704 ORGANISM assertions and zero study/biosample counters. The first
  node, three-node collapse note, count and unit reproduce correctly. These
  are not 1,704 distinct species, genetic modifications or experiments.
- Fresh [GOLD workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths),
  `site data` row 351, confirms node 4726 at this path with two Unclassified
  trailing levels. Worksheet dimensions were reset before complete iteration.
  SHA256 `f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`;
  84,174 bytes. Historical nodes 4386/4725 were not reconstructed.
- Fresh [GOLD organism-tree JSON](https://gold.jgi.doe.gov/download?mode=organismEcosystemsJson),
  discovered through the actual explorer's source in the preceding review,
  confirms the exact classification with a current count of 1,686 and its
  Unclassified descendants. SHA256
  `49ef0a3e654a79f6b7e7140d2cdb2ac0ce0bb1df2ccb8decae68d129eeb7ca11`;
  1,450,415 bytes. The live count differs from the pinned August snapshot;
  do not silently overwrite that historical evidence. The node's linked
  organism-list URL returned HTTP 403, so the membership difference is unresolved.
- Inspected [NHGRI glossary: Genetically Modified Organism](https://www.genome.gov/genetics-glossary/Genetically-Modified-Organism-GMO)
  describes alteration of an organism's genome. This supports the distinction
  between organism qualification and habitat identity. Its examples do not
  establish any particular species, inserted gene, product, purpose or phenotype
  among the GOLD members.
- The same-turn inspected [GOLD classification guide](https://gold.jgi.doe.gov/ecosystem_classification)
  describes source surroundings and sample-driven categories, not a guarantee
  that every parent-child grouping is habitat subsumption.

## Completeness

There are no synonyms, definition, xrefs, environmental parameters, named taxa,
literature evidence objects, causal graphs, discussions or datasets. Optional
empty fields are appropriate: no habitat mechanism or characteristic organism
should be invented for a non-habitat qualifier. iModulonDB is not applicable;
no specific gene, strain, regulator or expression dataset is asserted.

Ignored-inclusive ID, label, stem and source-node searches covered curation,
all raw inventories, PATHS/RETIRED, configuration, docs, tests, history, research,
individual reports and the research manifest. Filename traversal covered
curation/history/research. The ITEM decision exists; no target-owned definition,
exclusion, overlay, separate session history, research file or previous individual
report was found in those bounds.

An exact-field/pipe-member scan of every raw TSV found only the ecosystem row,
not target sample/study/triad/parameter/taxon membership rows. The same-turn
ignored-inclusive find under build, data/raw and configured kg-microbe data found
no original GOLD dumps, bulk workbook or sample/triad intermediates. Current
classification availability is not recovery of the original member evidence.

## Findings

Zero blockers, one major finding, zero minor findings.

1. **Major: non-habitat qualifier retains a habitat-parent assertion.**
   The supported ITEM NOT_APPLICABLE decision says the source is an organism
   property, while `parent_habitats` still asserts a broader habitat in the
   unreviewed Laboratory developed category. The exact owner of this source-only
   contribution is `curation/gold_parent_exclusions.tsv`, applied by
   `src/habitatmech/seed.py:ingest_gold`. The non-habitat decision itself does
   not need reversal merely to accommodate the inherited edge.

## Recommended Edits

Add an evidence-backed exclusion for source `habitatmech:GOLD.2eecc8ad2c`,
its exact full path and expected parent `habitatmech:GOLD.77c5518fff`.
Preserve NOT_APPLICABLE, genuine ITEM-derived REVIEWED status, identity,
attestations, historical counts and verbatim source path. Do not manufacture
a habitat definition or change the parent record's scope in this child-only fix.

If a general seeder policy for non-habitat source hierarchy is proposed, test
it across explicit and inferred parent contributors before changing shared
behavior. This review establishes the bounded child contribution, not a blanket
deletion of all parents or all records classified NOT_APPLICABLE.

## Follow-up Checks

Regress that the exact source-path parent disappears while the source path,
count/unit, mapping omission, identity and review state remain unchanged.
Verify no independent parent or sibling claim is lost. Authorized curation
requires a dry seed, inspected forced canary, append-only history, schema,
provenance, label eligibility, exact reproduction, actual site/map input checks
and full QC. Any count update needs a governed source refresh.

## Additional Notes

Only this new report was written. No scientific/generated input, older report,
history event, lifecycle status or GitHub item changed. The Laboratory developed
record was inspected as context, not counted as independently reviewed here.
