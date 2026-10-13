# YAML Record Review: ascending colon

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/ascending_colon.yaml`
- Started UTC: 2026-10-04T07:05:38Z
- Finished UTC: 2026-10-04T07:14:02Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord `UBERON:0001156`: HOST_ASSOCIATED,
EXACT, SEEDED. It has an ontology definition, two ontology synonyms, two
parents, one GOLD attestation with skos:exactMatch and one seed event.
No assertion count, taxa, parameters, mechanisms or datasets are emitted.
`data/habitats/PATHS.tsv:1026` pins the filename. The actual `mint` helper
reproduces source key `habitatmech:GOLD.0d9cfc05b6` from the full human path.

## Validation

- `just validate data/habitats/host_associated/ascending_colon.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/ascending_colon.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed; 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
  This gate does not validate ontology synonym scopes or scientific is-a.
- Fresh batch `just qc` passed lint, documentation and raw provenance;
  its tests remain running at report completion. No terminal result is
  claimed. Full-corpus history, reference/invariant, strict schema,
  reproduction, site, redirect and term-request checks are included.
- Exact unchanged base `f154d8e326de08656e89f5908331cf9a851bac9f` passed
  [post-push QC 37184590603](https://github.com/CultureBotAI/HabitatMech/actions/runs/37184590603).
  Its merge-group QC passed 457 tests, with three skips and two warnings.
  These are baseline results, not the new report's final-head CI.
- Current official OLS term JSON, typed graphs and `obo_synonym` scopes
  were inspected directly after browser API retrieval failed. PubMed
  EFetch supplied the human paper's abstract and identifier metadata.
- Read-only comparisons through the actual full-context semantic adapter
  tested parent removal and synonym-type correction separately.

## Identity and Grounding

Current non-obsolete
[UBERON:0001156](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0001156)
agrees with vendored term row 13023 on label and the definition of the colon
segment between caecum and transverse colon. The inherited run-together
`transversecolon` spelling is source-owned, not a different anatomical claim.
The human source names this anatomical site. Its unique leaf path explains
automatic EXACT under `docs/HARMONIZATION.md`; no ITEM decision was found,
so SEEDED must not be described as curator-reviewed equivalence.

The valid ontology parent is
[UBERON:0000168](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0000168),
proximal-distal subdivision of colon. Vendored edge 11175 and the current
typed graph both assert this subclass relation. The superclass's current
[graph](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000168/graph)
separately uses part_of for colon; anatomical containment is not is-a.

The complete `large_intestine__65b4f112.yaml`,
`habitatmech:GOLD.5b0aa7456c`, denotes whole human Large intestine, NARROW
under current
[UBERON:0000059](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0000059).
It has no authored regional-environment definition. A colon segment is not
a type of the whole organ, and the generic UBERON class is not restricted
to humans. `src/habitatmech/seed.py:898-907` promotes this source nesting
to a false superclass, contrary to `docs/CURATION.md:26`.

Current structured synonym metadata explicitly distinguishes exact
`colon ascendens` from related `spiral colon` with taxonomic-disambiguation
type. The generated record instead makes both exact. Current
[UBERON:0010239](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0010239)
separately describes spiral colon as a variant in ruminants and pigs and
contains an editor note considering a merge. That pending consideration
does not change the present related-synonym assertion.

The untyped pipe at `ontology_terms.tsv:13023` cannot prove exactness.
The maintained TSV extractor at `src/habitatmech/extract.py:770-783`
copies such a pipe; the OWL loader at lines 828-837 likewise flattens all
four synonym predicates. `ConceptStore.get` at `seed.py:406-407` then
unconditionally emits exact synonyms. This is a scope-preservation defect,
not an upstream assertion that both names are exact.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:2212` supplies the human depth-five path,
node 6106, one node and zero tree organism/study/biosample counts. The
absence of a generated count follows the nonzero-organism projection rule;
the parent record's 20 organisms are not this record's count.

Complete structured scans covered all 12 non-ontology source tables.
The 1,040-row bulk table has one exact target row at line 1017: one
biosample for path ID 6106. The 4,587-row study table has one matching
membership at line 103: Gs0046453 lists both ascending and descending colon.
The 1,587-row triad table has no target match. Thus a tree zero does not
mean no source activity. These counts remain distinct units and do not
prove that both study paths have identical samples. Direct access to the
[GOLD study](https://gold.jgi.doe.gov/study?id=Gs0046453) returned HTTP 403;
study identity/path support here is bounded to the committed inventory,
not independently verified specimen or study-design details.

The inspected primary
[human mucosal study](https://pubmed.ncbi.nlm.nih.gov/24132077/)
abstract and identifier metadata verify DOI:10.1038/ismej.2013.185 and
PMC3960530. It sampled 77 biopsies from seven intestinal sites, including
ascending colon, in 11 healthy adults and reports spatial heterogeneity.
This supports a bounded microbial sampling site, not uniform communities
or mechanistic proof from co-occurrence.

The inspected primary
[Knight et al. 2019](https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2019.00120/full)
abstract and methods verify DOI:10.3389/fnut.2019.00120 and sampling of pig
ascending-colon contents. This supplies a non-human anatomical example;
the experimental iron treatments, microbial abundances and metabolites
are not universal habitat parameters or evidence for GOLD's one biosample.

## Completeness

Ignored-inclusive identifier/source-key/label/synonym/stem searches covered
curation, history, research, prior reports, PATHS and RETIRED. They found
the pinned path and adjacent caecum/parent references, but no target
decision, term request, causal overlay, session, research report or redirect.
Exact report-metadata traversal including ignored files found no prior
review of this target. Reference reads do not add target coverage.

All eight non-GOLD inventories were scanned completely: 162 BacDive
sources, 3,081 BacDive taxa, 770 parameters, 358 mappings, 58 Madin habitats,
1,378 Madin taxa, 719 PREGO habitats and 8,807 PREGO taxa. None matched the
target key, UBERON ID or searched ascending/spiral/Latin colon wording.
This is not an exhaustive search under every organism or anatomical synonym.
Optional fields need not be filled merely for coverage. iModulonDB is not
applicable: the record makes no gene, regulatory or expression claim.

## Findings

1. **Major - HM-ASCENDING-COLON-001:** the generic colon segment inherits
   whole human Large intestine as a superclass. Maintained owner: the
   GOLD source-parent rule in `src/habitatmech/seed.py` and a scoped
   governed input. Added to existing
   [#1325](https://github.com/CultureBotAI/HabitatMech/issues/1325#issuecomment-5977609051).
2. **Major - HM-ASCENDING-COLON-002:** related UBERON synonym `spiral colon`
   is promoted to exact. Maintained owners: ontology source/extraction
   contract and `ConceptStore.get`. Added to existing
   [#1249](https://github.com/CultureBotAI/HabitatMech/issues/1249#issuecomment-5977610042).

No blocker or minor finding established. The ordinary anatomy identity and
valid UBERON superclass remain supported independently of these defects.

## Recommended Edits

Correct only the false GOLD parent contribution, preserving UBERON identity,
valid parent, source path/node and count-unit semantics. An ITEM review
belongs in `curation/decisions.tsv` under the minted source key; a status
event alone cannot repair the relation. Do not globally discard source
parents or replace part-of with an equivalence xref.

Recover typed ontology assertions reproducibly and emit related `spiral
colon` while retaining exact `colon ascendens`. Preserve spellings and
provenance, including genuinely exact synonyms elsewhere; do not infer
scope from an untyped pipe or hand-patch generated YAML/raw checksums.

The actual parent-removal comparison deletes `broader habitat: Large
intestine` and changes semantic input, requiring the governed rebuild in
[#1217](https://github.com/CultureBotAI/HabitatMech/issues/1217). By contrast,
changing only `synonym_type` leaves actual semantic text byte-identical;
that limited correction is not inherently blocked by map inference.
Draft #1218 remains open and unchanged at
`18c93452a789218f5c653d02723d11388d972055`; its mechanism is not on main.

## Follow-up Checks

Regress this exact source-parent edge and its retained valid parent/source
fields. Add mixed-scope synonym tests, including exact, related, unknown
and multiple-scope cases. Append required curation history and inspect a
guarded canary. Require provenance, ordinary/strict validation, OAK, corpus
reproduction, site/redirect freshness and full QC. Compare complete semantic
inputs before deciding whether a map rebuild is needed; never weaken its
freshness checks or runtime pins.

## Additional Notes

All 504 issue titles, bodies and returned comments were searched for the
target/source/parent IDs, colon names and relevant family wording. Existing
#1325 and #1249 own these findings; #1327 concerns abscesses, not this
anatomical segment. No duplicate issue or scientific edit was created.

An exploratory scan stopped on the unrelated extra-field bulk row 395;
the complete rerun inspected string fields and overflow values explicitly
and compared the named canonical-path and study-membership columns. The
successful full scan, not the interrupted attempt, supports the counts above.

No generated record, maintained input, status, event or history changed.
No paid research ran. This is not independent PR approval. Whole-corpus
review remains ongoing.
