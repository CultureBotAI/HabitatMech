# YAML Record Review: Sub-saline lake

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/sub_saline_lake.yaml`
- Started UTC: 2026-10-06T11:06:51Z
- Finished UTC: 2026-10-06T11:12:54Z
- Verdict: pass

## Target

Read the entire generated HabitatRecord habitatmech:GOLD.6dec91dddc,
Sub-saline lake, AQUATIC, UNGROUNDED, SEEDED. Its sole attestation is
Environmental > Aquatic > Non-marine Saline and Alkaline > Sub-saline lake,
represented by GOLD7919 with a two-node aggregation note. The actual mint
matches and `data/habitats/PATHS.tsv:2100` fixes its stem. One parent and
two generated events are present. This review does not promote its status.

## Validation

- `just validate data/habitats/aquatic/sub_saline_lake.yaml`: passed.
- `just validate-strict data/habitats/aquatic/sub_saline_lake.yaml`:
  one file, zero errors.
- Actual full `build_corpus` / `build_document` equality passed for every
  field: one source, zero item-reviewed sources, zero taxa, two events.
- Executed default/applied target and immediate-parent routes; scanned
  all 14 raw inventories for exact source path/node membership; read
  the complete rendered page and full-context semantic text.
- [Main QC on base 7c8d28437](https://github.com/CultureBotAI/HabitatMech/actions/runs/37452730923)
  completed successfully: 463 tests passed, three skipped, two dependency
  warnings, 90 valid histories, 3,206 strict-valid and exactly reproduced
  records, and current site, redirects and term requests. This is reuse
  of an unchanged scientific/code baseline, not a fresh per-report full QC.
- Required merge-candidate label correspondence passed with zero flagged
  pairs and 2,054 no-adapter skips. This record emits no taxon, evidence
  or causal-graph identifiers requiring a separate reference audit.

A resumed `uv run` parent probe was blocked by access to the external uv
cache; the same probe completed with the existing `.venv/bin/python`.

## Identity and Grounding

`curation/decisions.tsv:658` is CLASS CONFIRM_UNGROUNDED. The actual
gold_unmatched route becomes curated_confirm_ungrounded_from_gold_unmatched,
preserving the minted ID, no mapping predicate and reviewed=False. The
SEEDED status and original CLASS-level warning are accurate.

Current ENVO searches for subsaline and hyposaline lake returned no
term. The sub-saline lake query returned saline evaporation pond, an
irrelevant lexical candidate, not an identity. The brackish lake query
returned [ENVO:00000540](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000540),
an active class with no synonym equating it to this GOLD label. Its
definition describes a lake between freshwater and marine salinity;
its typed OWL parents are saline lake and brackish water body. That
does not establish GOLD's operational meaning of sub-saline.

The local ontology row at `ontology_terms.tsv:7123` includes brackish
lake, and `ontology_subclass_edges.tsv:5212-5213` includes both parents.
The FALSE flags are directly_referenced and label_only, not exclusion
from a habitat class. There is no demonstrated missing-ontology defect.

[Lake, ENVO:00000020](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000020),
and [saline lake, ENVO:00000019](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000019),
were also verified in current OLS and typed OWL. Lake is a potential
broader genus, not an exact identity. Saline lake needs an explicit
assessment of how the source uses the salinity qualifier. Searches were
bounded to ENVO and the committed slice, not all external vocabularies.

The entire immediate parent habitatmech:GOLD.ce244e62cd was read. It is
the authored inland saline or alkaline aquatic environment, with a
disjunctive definition and the verified broader aquatic environment
ENVO:01000317. Its ITEM decision and REPLACE definition intentionally
removed an earlier aquatic-biome edge. It is neither a water material
nor a whole-lake class. No evidence here establishes that this source's
lake falls outside that environmental grouping. Do not remove a
defensible parent just because other GOLD paths have false parents.

## Evidence

`gold_ecosystem_paths.tsv:1576` provides the exact depth-four path,
nodes 7919 and 7921, and zero organism, study, biosample and total
counters. Count/unit omission is faithful. No exact target membership
occurs in the other 13 raw inventories, including samples, triads,
studies, parameters and taxon feeds. This does not prove no upstream
sampling exists. Both current official GOLD node projections returned
HTTP 404; neither result alone establishes retirement.

[Veres, Pienitz and Smol (1995), Arctic 48:63-70](https://pubs.aina.ucalgary.ca/arctic/Arctic48-1-63.pdf),
reports periphytic diatom succession in three Yukon lakes. The inspected
abstract, study area and methods distinguish a subsaline lake at
0.5-3.0 g/L and sample diatoms colonizing submerged glass slides in its
littoral zone. This supports the plausibility of a microbial habitat
and one explicit usage of subsaline. It is not GOLD7919/7921 provenance
or authority to impose that numerical range, closed-basin morphology,
species composition or seasonal mechanism on this source concept.

The broader parent's GOLD and BacDive counts and taxa are not child
evidence. Its research report was used only as a lead, not independent
primary support. A located 2025 article could not be inspected beyond
access barriers and is not used to support the verdict.

## Completeness

Ignored-inclusive searches covered the exact ID, label, spelling
variants, stem and node keys across curation, history, research,
configuration, documentation, source, scripts, tests, reports and
path/retirement registries. The target decision and path lock exist;
no target-owned definition, overlay, session history or retirement was
found. An existing sediment-child review mentions this parent but is
not a previous individual review of this lake.

An ITEM scope assessment and evidence-backed definition would improve
interpretability. Their absence is not a defect in this honestly
declared seed. Empty optional parameters, taxa, citations and graphs
must not be filled for coverage. iModulonDB is not applicable because
there is no gene, regulator or expression claim.

## Findings

None found: zero blockers, zero majors, zero minors. This pass means
no substantiated defect in the emitted claims, not completed curation
or certified exact grounding. Source-specific salinity semantics remain
unresolved.

The parent's saline-only synonym problem is owned by
[#1415](https://github.com/CultureBotAI/HabitatMech/issues/1415). Those
aliases are not emitted as child synonyms and are not a new finding here.

## Recommended Edits

None required by this review. A later source-specific ITEM assessment
may retain CONFIRM_UNGROUNDED and author a definition in
`curation/term_requests.tsv`, using a verified genus and ADD to preserve
supported inherited parents. Do not exact-merge into brackish lake on
lexical proximity, infer an uncited salinity threshold, import ancestor
observations, or mark a real habitat NOT_APPLICABLE.

## Follow-up Checks

Obtain original GOLD node/sample documentation to settle qualifier
scope before proposing grounding or quantitative conditions. Future
curation must use authoritative inputs, append-only history, dry seed,
an inspected guarded canary, reproduction, labels and full QC.

An exploratory direct-parent removal changes full-context semantic
text; it is not a recommended edit. Predicate omission is text-neutral
because no predicate exists. This is not an export test. Genuine future
label/definition/hierarchy changes need #1217 map/site handling while
isolating #1218 and runtime pins. No SSSOM/KGX artifact is changed or
certified by this report.

## Additional Notes

All 634 open/closed issue titles and bodies were searched for the exact
ID, sub-saline variants and candidate/parent keys. No target-owned
implementation issue was found on those surfaces. Related parent and
sediment issues are not evidence that this lake has the same defect;
all repository issue comments were not exhaustively searched.

Typed official ENVO snapshot SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
