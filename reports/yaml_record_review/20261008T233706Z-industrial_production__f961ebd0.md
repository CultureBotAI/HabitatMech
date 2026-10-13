# YAML Record Review: Industrial production

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/industrial_production__f961ebd0.yaml`
- Started UTC: 2026-10-08T23:23:18Z
- Finished UTC: 2026-10-08T23:37:06Z
- Verdict: pass with minor issues

## Target

Generated HabitatRecord `habitatmech:GOLD.a744ade0d8`, Industrial production,
ENGINEERED / UNGROUNDED / SEEDED. The entire target, its Engineered parent and
the distinct BacDive Industrial-production record were read. Only the exact
GOLD `Engineered > Industrial production` category is the review target.
Baseline: `e843a50bf15dc16e28f71010508ebba9e98b57ec`.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/industrial_production__f961ebd0.yaml`:
  passed, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/industrial_production__f961ebd0.yaml`:
  passed, one file, zero errors.
- Fresh `just verify-corpus`: 3,208 expected/present, zero missing, extra or
  differing records. Complete in-memory reconstruction with
  `seed.build_corpus()` and `seed.build_document()` also matched the target.
  It has one contributing source, zero ITEM-reviewed sources, zero applied
  definitions and zero target-owned GOLD parent exclusions.
- Fresh `just validate-history`: 205 valid histories. Fresh
  `just provenance-check`: 14 inventories and two GOLD source groups current.
  These manifest checks do not reconstruct the original organism cohort.
- Full QC was not rerun during the read-only record review. The unchanged
  baseline passed native queue [QC run 37857700289](https://github.com/CultureBotAI/HabitatMech/actions/runs/37857700289)
  with 620 tests passed, three skipped and all quality gates passed.
  [Label correspondence run 37857700466](https://github.com/CultureBotAI/HabitatMech/actions/runs/37857700466)
  also passed on that baseline. The label gate does not certify native minted
  identifiers or the semantics of their parent links.
- Original organism-member joins were not reconstructed. No SSSOM/KGX
  compatibility audit was performed.

## Identity and Grounding

The exact GOLD path mint and `data/habitats/PATHS.tsv:2523` agree with the
identifier and filename. The parent `habitatmech:GOLD.2acb39dd08` resolves to
`data/habitats/engineered/engineered__900b76ad.yaml`; its mint and path lock
also agree. The actual resolver, using the full current ontology, mappings,
leaf/composed claimant indexes and decisions, takes `gold_unmatched` for
both, then `curated_confirm_ungrounded_from_gold_unmatched` after their CLASS
decisions (`curation/decisions.tsv:959` and `:332`). Neither route adds an
ontology identity, predicate or ITEM endorsement.

The sole parent is the immediate GOLD Engineered source root. Current GOLD
guidance supports a reading of these categories as sample surroundings, but
neither record has an item-level definition settling its precise extension.
Reproducing the source hierarchy does not independently prove strict habitat
subsumption. Conversely, the word production does not prove that this native
source category denotes an ontology process rather than associated habitats.

The separate `habitatmech:BACDIVE.cb34a860e6` Industrial-production bin has
147 STRAIN assertions and a deliberately empty upstream mapping
(`data/raw/isolation_source_groundings.tsv:158`). It is not merged into this
125-ORGANISM GOLD bin. Its taxa and counts are not evidence for the target;
their individual identifiers were not audited in this review.

## Evidence

- `data/raw/gold_ecosystem_paths.tsv:172` records depth two, four collapsed
  nodes (2892/3522/3859/4293), 125 ORGANISM assertions, and zero study/biosample
  counts. The generated first-node ID, full path, count, unit and four-node
  note agree. The Engineered parent row at `:253` separately records five
  nodes and 68 ORGANISM assertions; these are not a denominator or a census of
  descendants. The target's source-seeding timestamp agrees with
  `data/raw/MANIFEST.yaml`, which pins kg-microbe at
  `7698351a54b48f2e917635fdf51cd0a6b323135d`.
- Exact canonical-path and pipe-member parsing found no target row in
  `gold_path_biosamples.tsv` or `gold_path_triads.tsv`, and no exact target
  membership in `gold_studies.tsv`. These are bounded absences in the
  committed inventories, not proof of no samples or studies anywhere.
  Descendant rows cannot be inherited or summed into this source assertion.
- Primary [GOLD classification guidance](https://gold.jgi.doe.gov/ecosystem_classification)
  describes sample/organism surroundings, three broad ecosystem groups and
  subdivisions based on environmental characteristics. It is sample-driven
  and revised over time, not a declaration that every path step is a formal
  ontology subclass.
- The current [GOLD classification workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
  was parsed in memory, resetting worksheet dimensions before iteration.
  Sheet `site data`, row 331, contains node 4293, Engineered, Industrial
  production, followed by three Unclassified fields. The 84,174-byte download
  has SHA256 `f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.
  It confirms current classification, not historical nodes 2892/3522/3859 or
  the 125 original assertions; this workbook has no organism counts.
- Four active candidate classes were inspected in the primary
  [pinned ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
  and compared with the vendored slice: ENVO:00003074 manufactured product,
  ENVO:01000536 factory, ENVO:01000993 manufacturing process, and ENVO:01001450
  usage of an environment for industry. They denote respectively a processed
  material, an industrial site/building, a manufacturing process, and an
  environmental-use process. None is demonstrated to equal this GOLD bin.
  The fresh 9,614,229-byte upstream fetch matched the inspected local OWL:
  SHA256 `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`,
  version IRI dated 2026-06-26.

## Completeness

Definition, synonyms, xrefs, environmental parameters, named taxa, evidence
objects, causal graphs, discussions and datasets are empty. None should be
invented from a broad source label or a descendant. iModulonDB is not
applicable to this unnamed-organism source-category record. Missing optional
fields and CLASS/SEEDED lifecycle status are not major defects by themselves.

Ignored-inclusive identifier, label/stem and source-path searches covered
curation, raw inventories, PATHS, history, research, configuration and individual
review reports. Within those bounds there is no target-owned definition,
causal overlay, session history, deep-research report or earlier individual
target review. Child reviews and parent-exclusion histories are contextual
material, not independent evidence defining this record.

The configured original kg-microbe GOLD node dump could not be opened.
Ignored-inclusive filename traversal under `data/raw`, `build` and
`/private/tmp` found none of the searched GOLD node/edge dumps, goldData.xlsx,
gold_biosample_triads.tsv or biosample JSONL intermediates. The original
125-organism membership and source-description crosswalk therefore remain
unverified within those local bounds, not disproved or globally absent.

## Findings

1. **Minor: source scope and strict parent meaning remain unresolved.** A
   production-associated habitat grouping, production activity and wider
   source context are not interchangeable. The source path and current GOLD
   guidance support the grouping, but no item-level definition or original
   member inspection settles its exact meaning and strict relationship to
   Engineered. This is a bounded scope ambiguity, not a demonstrated wrong
   identity or false parent. Owner: exact-source assessments in
   `curation/decisions.tsv`, supported definitions in
   `curation/term_requests.tsv`, and a guarded
   `curation/gold_parent_exclusions.tsv` row only if contextual scope is
   established.

No blocker or major finding. Child-specific context exclusions for Chemical
products and Biochar do not decide this category's identity or its own parent.

The earlier [Engineered-root review](20260924T165434Z-engineered__900b76ad.md)
returned needs curation with major root-level identity/hierarchy findings.
That review concerns the root and its wider membership; this report does not
supersede it or adjudicate every outgoing parent edge. Here, current primary
GOLD guidance supports a plausible environment grouping, and no inspected
evidence establishes a false identity or false parent for this exact target.
The narrower finding is therefore minor: uncertainty and CLASS lifecycle alone
do not prove a major defect. The root's broader follow-up remains unresolved;
publication of this report is not an ITEM decision for either record.

## Recommended Edits

The exact target/Engineered-parent question is tracked in
[issue #1758](https://github.com/CultureBotAI/HabitatMech/issues/1758).
[Issue #1724](https://github.com/CultureBotAI/HabitatMech/issues/1724) separately
concerns the Engineered product child and its Industrial production parent;
neither issue is resolved by publishing this report.

Recover the original source-member descriptions before choosing a process,
product, factory or associated-environment interpretation. Assess the exact
target and Engineered root at ITEM depth only when the evidence warrants it.
Preserve the parent if genuinely broader; exclude only its exact GOLD
contribution if shown to be context-only. Do not use a fabricated definition
to suppress the edge, infer NOT_APPLICABLE from the label, merge the BacDive
bin, or promote mapping status merely because this report was published.

## Follow-up Checks

Reconstruct the four-node, 125-ORGANISM crosswalk against the original pinned
source before interpreting current descendant samples as evidence. Any later
authorized curation must preserve unrelated fields and records, append
session history, dry-run seed and inspect a target canary before regeneration.
Run strict validation, corpus reproduction, history/provenance validation,
rendered-site checks and full QC; run label correspondence for grounding
changes. Verify the independent contributions before altering a parent edge.

## Additional Notes

Only this new report is authored; scientific inputs, generated records,
historical reviews and mapping status are unchanged. The separate explicit
publication request authorizes the subsequent PR/review/issue workflow.
The publication adversarial pass identified the missing comparison with the
older root verdict ([#1757](https://github.com/CultureBotAI/HabitatMech/issues/1757));
the Findings section now preserves that distinction without rewriting the
historical report or changing the scientific verdict.
Failed GOLD project-page and explorer retrievals, search snippets and a
minimal PubMed response were not used as organism or paper evidence. The
current workbook is not the original organism cohort. This is one record
review, not completion of the all-record goal or export-readiness certification.
