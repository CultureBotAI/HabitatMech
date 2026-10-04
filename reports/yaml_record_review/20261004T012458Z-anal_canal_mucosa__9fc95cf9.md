# YAML Record Review: Anal canal mucosa

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/anal_canal_mucosa__9fc95cf9.yaml`
- Started UTC: 2026-10-04T01:23:15Z
- Finished UTC: 2026-10-04T01:24:58Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord for `habitatmech:GOLD.e45d906034`:
HOST_ASSOCIATED, NARROW, SEEDED. It has two parents, one GOLD attestation
with one ORGANISM assertion and one seed event. This target is the human
Anal canal mucosa beneath Large intestine, not the mammal mucosa or either
whole-canal record. The actual `mint` helper reproduces its identifier;
`data/habitats/PATHS.tsv:2989` pins its distinct filename.

## Validation

- `just validate data/habitats/host_associated/anal_canal_mucosa__9fc95cf9.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/anal_canal_mucosa__9fc95cf9.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed, 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh batch QC remains running; lint, documentation and raw provenance
  passed. Baseline `e4e479e0a7` passed head/queue QC in #1326, but that does
  not constitute a completed QC result for this review batch.
- Current official OLS term definitions and typed graph were inspected in
  this batch using successful direct API requests after browser retrieval
  failed. Target, source, parent and curation searches were checked separately.

## Identity and Grounding

Current [UBERON:0003342, mucosa of anal canal](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0003342)
is non-obsolete and includes Anal canal mucosa as a synonym. Vendored
`ontology_terms.tsv:13199` agrees. Its anatomical tissue scope is compatible
with the human source. The tied depth-five GOLD leaves explain the conservative
minted NARROW route in `resolve_gold`; this is not wrong identity merely
because an ITEM decision is absent.

The complete `large_intestine__65b4f112.yaml` identifies the second parent,
`habitatmech:GOLD.5b0aa7456c`, as a whole-intestine source NARROW beneath
[UBERON:0000059](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0000059).
It has no authored associated-environment definition broadening that scope.
Current OLS and vendored line 12893 agree on the digestive-tract subdivision.

The [current mucosa graph](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0003342/graph)
explicitly distinguishes subclass UBERON:0001207, mucosa of large intestine,
from part_of UBERON:0000159, anal canal. Both referenced definitions and
non-obsolete statuses were verified; vendored lines 13030/12910 and subclass
edge 11438 agree. Mucosa is a tissue of the canal, not a subtype of the
whole large intestine. This rests on definitions and typed relations, not
merely a missing ancestor. No whole-host taxon is used as habitat identity.

## Evidence

An independent exact-path structured check of `gold_ecosystem_paths.tsv:1069`
verifies node 6311, one source node, depth five, one organism and zero study/
biosample assertions. Generated label, full human path, source ID, predicate,
count and ORGANISM unit match. The parent's 20 organism assertions are not
assigned to the child. Human and mammal sources need not denote disjoint
populations, so their counts are not added.

Full batch scans cover 2,562 tree paths, 1,040 bulk-count rows, 4,587 studies
and 1,587 triads. Only the two mucosa tree rows match the specific phrase;
the other three tables have no anal-canal-mucosa match. Other mucosal sites
are not target attestations. No study membership, specimen,
taxon or collection method is inferred from the one source assertion.

`src/habitatmech/seed.py:898-907` adds the source-parent edge. The schema,
CLAUDE.md and `docs/CURATION.md` require every such contribution to be
strictly broader/is-a. The rendered Broader habitats relation cannot be
defended as merely preserving an untyped GOLD breadcrumb.

## Completeness

Ignored-inclusive exact target/parent IDs, stem and source-label searches
covered curation, history, research, prior reports, PATHS and RETIRED. They
found no target ITEM decision, authored definition, overlay, session record
or earlier exact-target review. The narrow sample row at
`curation/samples/narrow-20260814.tsv:6` concerns mammal mucosa, not this
human target. It cannot serve as this record's review or justify its parent.

Full structured batch scans of 719 PREGO habitats, 8,807 PREGO taxa, 162
BacDive sources, 3,081 BacDive taxa, 770 parameters, 358 mappings, 58 Madin
habitats and 1,378 Madin taxa found no anal-canal-mucosa or UBERON:0003342
match. The inspected whole-canal and mucosa ontology terms are not silently
interchanged. Empty optional taxa, parameters and causal graphs are not
findings. iModulonDB is not applicable: no gene, regulator or expression
claim occurs in this record.

## Findings

1. **Major - HM-ANAL-MUCOSA-HUMAN-001:** the human mucosa inherits a whole-
   large-intestine superclass from GOLD source nesting, despite the supported
   tissue-versus-organ distinction. Maintained owner:
   `src/habitatmech/seed.py:898-907` or a governed source-specific exclusion.
   Added independently to [#1325](https://github.com/CultureBotAI/HabitatMech/issues/1325).

No blocker or minor finding established. The valid mucosa parent, human
source scope, count unit and conservative grounding remain supported.

## Recommended Edits

Exclude or evidence-correct this exact source contribution while retaining
UBERON:0003342, full source provenance and the intended identity/status.
Do not hand-edit generated YAML, replace mucosa with whole canal, encode
part-of as an equivalence xref or globally delete GOLD parents. Compare
host-qualified source identities at ITEM depth before any exact merge.

A read-only copy processed through the real `semantic_text` adapter confirms
that removing this parent drops the Large intestine broader-habitat line
and changes the semantic input. This is an actual adapter check, not an
assumption that every curation change needs inference. Use governed inputs,
required history, a guarded canary and supported map/site regeneration;
#1217 remains relevant, and draft #1218 is not assumed merged.

## Follow-up Checks

Regress this human mucosa edge independently of the three established canal/
mammal-mucosa witnesses. Verify the correct mucosa ancestry, source ID,
one-ORGANISM assertion, status and unchanged URLs. Require strict schema,
OAK, history, corpus reproduction, semantic/site freshness and full QC.

## Additional Notes

The complete 483-issue body/comment scan in this batch matched #1325 only
for the exact mucosa keys, anal-canal wording and UBERON:0003342. A separate
human witness was added rather than a duplicate issue. The parent was a
reference read, not a second completed target. No scientific input,
generated record or history was changed; no paid research ran.
