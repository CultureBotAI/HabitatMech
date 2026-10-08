# YAML Record Review: Concrete surface

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/concrete_surface.yaml`
- Started UTC: 2026-10-08T03:16:02Z
- Finished UTC: 2026-10-08T03:18:53Z
- Verdict: needs curation

## Target

Read the full generated HabitatRecord `habitatmech:GOLD.d4694eed69` at
`6ef2563f667a7af527721a1a29ff6f0189e6d1da`. It denotes the exact GOLD path
`Engineered > Built environment > City > Subway > Concrete surface`.
It is ENGINEERED / UNGROUNDED / SEEDED, with one parent, one attestation and
two history events. No definition, synonyms, xrefs, count/unit, mapping
predicate, parameters, taxa, literature evidence, graph, discussion or dataset
is asserted. It is not the whole subway or a specific floor, wall or biofilm.

## Validation

- Fresh `UV_CACHE_DIR=build/uv-cache just validate` passed on this file.
- Fresh strict validation: one file, zero errors.
- Actual full-index resolution is `gold_unmatched`; applying the real CLASS
  decision gives `curated_confirm_ungrounded_from_gold_unmatched`, retained
  mint, UNGROUNDED, no predicate/extra parent, reviewed=False.
- Full read-only `build_corpus` / `build_document` equality passed: one source,
  zero reviewed sources, the expected CLASS decision and matching source mint.
  `PATHS.tsv:2863` agrees.
- Exact-field/pipe-member scans of all 14 raw TSVs found three target rows.
- Current OLS confirms active ENVO:01000458 concrete; exact ENVO-index search
  for concrete surface returned zero hits. This is a bounded candidate search,
  not proof that no suitable term exists anywhere.

Reused current-head PR #1683 offline QC passed, including 552 tests with three
skips and exact reproduction of all 3,207 records; vendored sync passed.
Its required label-correspondence job failed on unchanged beverage/pastry
FOODON identities (#1690), not on this minted record. No full all-green or
merge-queue baseline is claimed. Full history/reference/corpus gates were not
rerun per target. Structural success does not validate the hierarchy.

## Identity and Grounding

The mint, source ID/path, surface label and category agree. CLASS
CONFIRM_UNGROUNDED at `curation/decisions.tsv:1174` explicitly says habitat
meaning was not assessed. SEEDED and the two events faithfully preserve that
limit; the record is not falsely presented as ITEM-reviewed. Its absent
mapping predicate is consistent with retained identity, so it is not another
#1398 witness.

Read the whole `data/habitats/engineered/subway.yaml` parent and its maintained
definition at `curation/term_requests.tsv:75`. That definition covers the
environment bounded by stations, tunnels, trains and enclosed transit
structures. A local concrete surface in that setting is not a subtype of the
whole environment. The parent comes from the independent GOLD path pass,
not a target ITEM decision or an ontology superclass.

[ENVO concrete](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000458)
is a composite material, not an exact surface identity. Vendored
ENVO:00010504 surface layer is a possible genus to assess, not an adopted
grounding. Concrete masonry unit, concrete building floor, exterior wall,
road, cement and cement dust introduce unsupported object or material scope.
The source does not establish a floor/wall, coating, pore depth or biofilm.

## Evidence

`gold_ecosystem_paths.tsv:1255` records depth five, one node (5465) and zero
tree counters. Omitted count/unit and lack of a collapsed-node note are
correct. `gold_path_biosamples.tsv:666` separately records eight BIOSAMPLE
observations, not eight organisms or named taxa.

`gold_studies.tsv:1093` lists Gs0118444 across 12 paths, including the target,
other subway surfaces, City, Park, Canal, Lab synthesis and fish intestine.
This is a study membership, not 12 experiments or evidence that those other
habitats characterize concrete. No exact target triad was recovered.

Fresh [node 5465](https://gold.jgi.doe.gov/ecosystem/5465) retrieval failed;
[Gs0118444](https://gold.jgi.doe.gov/study?id=Gs0118444) returned an error shell,
not usable study metadata. Bounded exact-study, category and BioSample searches
yielded no verified original sample crosswalk. No city or publication was
assigned to the eight observations solely from a broad subway topic match.

The existing Subway deep-research report was read as contextual leads, not
independent evidence or an instruction to import its taxa and broad claims.
Freshly inspected [Gohli et al. 2019](https://link.springer.com/article/10.1186/s40168-019-0772-9)
abstract and sampling sections distinguish subway air from specific kiosk,
railing and bench surfaces. They support the bounded surface-versus-enclosing-
environment distinction, not concrete composition or a Gs0118444 crosswalk.
No organism, seasonality, risk or abundance claim is imported. An EPA concrete
experiment was also inspected as a material-surface lead, but its manipulated
coupons are not evidence of natural target taxa or of these GOLD samples.

## Completeness

Ignored-inclusive ID, source node/path, stem, concrete-surface spelling
variants, parent and study searches covered curation, history, conf, tests,
docs, research, prior reports, raw inventories and registries. No target-owned
definition, exclusion, overlay, research entry, retirement or prior individual
report was found. The CLASS decision is present, not absent.
Structured label/synonym searches of the entire vendored ontology table found
concrete-related near-misses but no exact concrete-surface label.

[Issue #282](https://github.com/CultureBotAI/HabitatMech/issues/282) was freshly
read and is OPEN. Its comment and current exclusion table show that only
Bench surface has been corrected. The guarded row at
`curation/gold_parent_exclusions.tsv:27` and regression beginning at
`tests/test_gold_parent_exclusions.py:503` do not include this target.
That sibling correction is not target curation or a completed target review.
Optional empty biology is not a defect; iModulonDB is inapplicable because no
named gene, strain, regulator, pathway or expression dataset is asserted.

## Findings

Zero blockers, one major finding, zero minor findings.

1. **Major: location context is emitted as a strict superclass.**
   `parent_habitats: habitatmech:GOLD.961229841c` classifies a concrete surface
   as the whole defined subway environment. This contradicts the maintained
   parent definition and surface/environment distinction. Existing #282 owns
   this exact target. The supported repair owner is
   `curation/gold_parent_exclusions.tsv`, consumed by the seeder's GOLD
   parent-path pass; do not patch generated YAML or redefine the parent to
   accommodate its surface children.

## Recommended Edits

For authorized curation, add one exclusion guarded by GOLD.d4694eed69, the
exact full source path and expected parent GOLD.961229841c. Preserve source
5465, path, mint, count omissions and existing history. Removal need not wait
for an invented replacement definition or a speculative ontology identity.

Separately assess the material-layer versus interface boundary and the exact
source samples before adding ITEM identity curation or a definition in
`curation/term_requests.tsv`. Verify any proposed genus against current
ontology semantics; bulk concrete, a specific structural object and the
whole environment are not interchangeable. Do not promote lifecycle status
merely because a hierarchy contribution was corrected, or freeze SEEDED if
later genuine ITEM decisions justify a change.

## Follow-up Checks

Add a differential regression proving only this target's parent contribution
and appended exclusion audit event change across the full corpus. Retain
source/path/count omissions and all sibling records, including the already
corrected bench. Append history, dry-seed, inspect a forced canary, regenerate
through maintained inputs and check actual semantic map/site refresh needs.
Run strict schema, labels, provenance, full reproduction and QC. Resolve
#1690 before claiming all required gates pass. No SSSOM/KGX execution or
current kg-microbe modeling certification was performed in this review.

## Additional Notes

Only this report was written. No scientific input, generated record/page,
history, lifecycle status or GitHub item was changed. No paid research or
delegation was used. Reading the parent and sibling correction as context does
not add individual record reviews to the coverage count.
