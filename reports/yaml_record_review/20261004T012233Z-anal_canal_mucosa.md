# YAML Record Review: Anal canal mucosa

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/anal_canal_mucosa.yaml`
- Started UTC: 2026-10-04T01:19:37Z
- Finished UTC: 2026-10-04T01:22:33Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord for `habitatmech:GOLD.1d3e238d30`:
HOST_ASSOCIATED, NARROW, SEEDED. It contains two parents, one GOLD attestation
with one ORGANISM assertion and one seed event. The source is Mammals >
Digestive system > Large intestine > Anal canal mucosa, not the human
mucosa or either whole-canal source. The actual `mint` helper reproduces
the identifier; `data/habitats/PATHS.tsv:1498` pins its filename.

## Validation

- `just validate data/habitats/host_associated/anal_canal_mucosa.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/anal_canal_mucosa.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed, 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh `just qc` is running. Lint, documentation and raw provenance passed;
  tests are underway. Baseline `e4e479e0a7` passed head/queue QC in #1326,
  including 457 tests and exact corpus/site reproduction. Those earlier
  receipts do not replace this batch's unfinished QC.
- Browser OLS API retrieval failed; direct official API requests succeeded.
  The successful responses, not the browser failures, support the checks below.

## Identity and Grounding

Current [UBERON:0003342](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0003342)
denotes mucosa of anal canal, is non-obsolete and explicitly lists anal canal
mucosa as a synonym. Vendored `ontology_terms.tsv:13199` agrees. Mammalian
scope is compatible with this anatomical identity; the mucosa is not the
whole canal or whole host. Both GOLD mucosa leaves tie at depth five, so
the conservative `resolve_gold` leaf route retains separate minted sources
with the term as a parent. NARROW and SEEDED are not defects by themselves.

`curation/samples/narrow-20260814.tsv:6` marks this exact mammal source
correct in a narrow-grounding sample audit. It is neither an ITEM decision
nor relation-level evidence for the extra GOLD parent.

The complete referenced `large_intestine__834e53c8.yaml` identifies
`habitatmech:GOLD.6bda0871e2` as NARROW under UBERON:0000059 and a digestive-
system source. It has no authored broader environmental definition. Current
[large intestine](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0000059)
denotes the digestive-tract subdivision, not a genus encompassing its tissues.

The current [typed mucosa graph](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0003342/graph)
gives `rdfs:subClassOf` UBERON:0001207, mucosa of large intestine, and
`BFO:0000050` part_of UBERON:0000159, anal canal. Both terms' current
definitions and non-obsolete status were checked separately. Vendored term
lines 13030/12910 and subclass edge 11438 agree. This positive typed evidence
distinguishes mucosa ancestry from whole-organ containment; the finding does
not rely solely on an absent subclass edge.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:1043` supplies the exact five-level path,
node 6464, one source node, one organism and zero study/biosample assertions.
The generated source ID, label, path, predicate and count/unit are faithful.
One organism assertion does not identify a specimen, microbe or sampling method.
The referenced parent's 37 ORGANISM assertions are not this mucosa's count.

Complete scans of 2,562 tree paths, 1,040 bulk-count rows, 4,587 studies and
1,587 triads found the mammal and human anal-canal-mucosa tree rows but no
anal-canal-mucosa match in the other three inventories. Other mucosal sites
are not target attestations. No live study membership or microbial taxon
is invented. The human source at tree line 1069 remains a distinct source,
not an extra attestation automatically merged into this target.

The additional whole-intestine edge is contributed by the GOLD parent-path
pass at `src/habitatmech/seed.py:898-907`. The schema's `parent_habitats`
contract and `docs/CURATION.md` require strictly broader/is-a semantics.
The template presents those links as Broader habitats, not merely untyped
source-path navigation. Reproducibility does not establish semantic validity.

## Completeness

Ignored-inclusive ID, source-label and stem searches covered curation,
history, research, prior reviews, PATHS, RETIRED and ontology inventories.
They located the sample audit but no target ITEM decision, term request,
overlay, session record or earlier exact-target review. The older sample
audit's lack of later-style session history is not a retroactive defect.

Full structured scans of 719 PREGO habitats, 8,807 PREGO taxa, 162 BacDive
sources, 3,081 BacDive taxa, 770 parameters, 358 mappings, 58 Madin habitats
and 1,378 Madin taxa found no anal-canal-mucosa or UBERON:0003342 match.
No whole-canal, rectal or generic intestinal evidence is imported merely
because it is nearby. Empty optional taxa, parameters and mechanism fields
are not findings. iModulonDB is not applicable: no gene, regulator or
expression-module claim is supplied.

## Findings

1. **Major - HM-ANAL-MUCOSA-MAMMAL-001:** the mucosa inherits a whole-large-
   intestine superclass from source nesting. Its supported broader mucosa
   term does not justify that separate whole-organ edge. Maintained owner:
   `src/habitatmech/seed.py:898-907` or a governed source-specific exclusion.
   Added as an independently verified witness to existing
   [#1325](https://github.com/CultureBotAI/HabitatMech/issues/1325).

No blocker or minor finding established. Source copying, anatomy-as-habitat
and conservative host-qualified grounding remain supported.

## Recommended Edits

Exclude or evidence-correct this exact source-parent contribution while
retaining the valid UBERON:0003342 parent and complete source provenance.
Do not replace mucosa with whole anal canal, encode part-of as an equivalent
xref, drop every GOLD parent or hand-edit generated YAML. Compare host-
qualified identities at ITEM depth before changing NARROW or merging sources.

Use governed inputs, append required history, inspect a guarded canary and
compare actual semantic inputs before supported map/site regeneration.
The runtime limitation remains tracked in #1217; draft #1218's exclusion
mechanism is not on main. Neither is claimed fixed by this report.

## Follow-up Checks

Regress this mucosa edge independently of the two canal witnesses; retain
the correct mucosa parent, source ID, one-ORGANISM count and intended status.
Check full ancestry, strict validation, OAK, history, corpus reproduction,
semantic/site freshness, redirects if identities change, and full QC.

## Additional Notes

All 483 existing issues and returned comments were searched for both mucosa
keys, anal-canal wording and UBERON:0003342. #1325 was the sole matching
repair, so no duplicate issue was opened. The parent was read as a reference,
not counted as a completed target. No scientific input, generated record or
history was changed, and no paid research ran.
