# YAML Record Review: Culture Medium

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/culture_medium.yaml`
- Started UTC: 2026-10-08T06:38:31Z
- Finished UTC: 2026-10-08T06:44:50Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord `BTO:0000316` at
`6f0de147db0cfa1c186620880965d227bb20eafd`. It denotes the general culture
medium category, not one formulation, cultured population, filtered liquid,
or cultivation procedure. It is ENGINEERED / EXACT / REVIEWED, with a BTO
definition, one exact GOLD plural synonym, one parent, one GOLD attestation
and two history events. Parameters, named taxa, literature evidence, graphs,
discussions and datasets are absent.

## Validation

Fresh commands used `UV_CACHE_DIR=build/uv-cache`:

- `just validate data/habitats/engineered/culture_medium.yaml`: no issues.
- `just validate-strict data/habitats/engineered/culture_medium.yaml`:
  one file, zero errors.
- `uv run pytest tests/test_bto_extraction.py -q`: six tests passed.

Fresh session-wide checks reused across the three reviews:
`just verify-corpus` reproduced all 3,207 records; `just validate-history`
validated 172 sessions; `just provenance-check` passed 14 inventories and
two GOLD sources; `uv run pytest tests/test_corpus_integrity.py -q -k
'parent or reviewed_records or history or causal_edges_reference'` passed six
parent/status/reference tests, 33 deselected. That selection does not add a
separate generated-history test.

Read-only `build_corpus` / `build_document` comparison reproduced every target
field, one source concept and one item-reviewed source. Executed default and
curated GOLD resolution with complete ontology, normalized mapping and both
claimant indexes. A second in-memory-only build set this ontology row's
`deprecated` value to `true`; the entire EXACT/REVIEWED record still reproduced
unchanged. No inventory or generated artifact was written by this diagnostic.

Full QC and label correspondence were not rerun for report-only additions.
The exact baseline's native queue
[QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37736853501) and
[label gate](https://github.com/CultureBotAI/HabitatMech/actions/runs/37736853478)
passed. The immediately preceding local label gate passed 1,177 canonical
pairs, one synonym and five existing exceptions, with 2,057 no-adapter skips.
These gates do not establish current ontology eligibility. No standalone
literature-reference check applies to this citation-free record. Original
GOLD/BTO re-extraction was unavailable within the searched source bounds.

## Identity and Grounding

The source concept key recomputes to `habitatmech:GOLD.1d91123b55` for
`Engineered > Lab culture > Culture media`. `PATHS.tsv:55` pins the emitted
BTO identity to this filename. The default is `gold_unmatched`, UNGROUNDED.
The ITEM GROUND decision at `curation/decisions.tsv:264` produces
`curated_ground_from_gold_unmatched`, BTO:0000316, EXACT/skos:exactMatch and
reviewed true. The singular canonical label and plural GOLD synonym are
semantically compatible with the historical solid-or-liquid medium definition.
No literal-string-equality rationale is asserted here.

The attestation's predicate compares the source concept to a different,
ontology-grounded record identifier. It is not the retained-mint narrow-match
endpoint defect. REVIEWED correctly reflects the existing ITEM decision, not
a claim that this review has reapproved the obsolete identifier.

The sole parent `habitatmech:GOLD.f8fb18f2a0`, Lab culture, comes from the
independent GOLD parent-path pass. The complete `lab_culture.yaml` was read.
It is an undefined CLASS-screened source category, with decision line 1369;
the source hierarchy proves placement, not a formally assessed material genus.
Its intended meaning could involve a culture, cultivation context or process.
This parent scope remains unresolved; the missing definition alone does not
prove a particular false interpretation or justify NOT_APPLICABLE. Do not
treat the edge as independently validated by schema success.

## Evidence

An exact-field/pipe-member scan of all 14 raw TSVs found these target inputs:

- `gold_ecosystem_paths.tsv:99`: depth three, nodes 5974/7098/7099, 273
  ORGANISM assertions, zero study/biosample tree counters. The count/unit,
  first-node display and three-node note reproduce that inventory.
- `gold_path_biosamples.tsv:354`: 47 BIOSAMPLE observations for node 7099.
  These are not another 47 organisms or an alternative attestation unit.
- `gold_studies.tsv:822`: Gs0114486 links four paths, including this one.
  `gold_studies.tsv:3900`: Gs0154202 links only this path in that inventory.
- `gold_path_triads.tsv:122-124`: each slot has one sample, one study and
  complete agreement within that single observation, not independent replication.

Primary ENVO metadata confirms the triad terms are active and distinct:
[aquatic biome](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002030)
is broad scale,
[hypersaline lake](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001020)
is local scale, and
[microbial mat material](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000157)
is sampled medium. These annotations do not redefine all culture media as a
biome, lake or mat, supply a general salinity value, or identify a strain.
Original sample metadata is needed to distinguish collection context from
the laboratory classification; this observation alone is not proof of a
wrong broad culture-medium identity.

The two [GOLD study](https://gold.jgi.doe.gov/study?id=Gs0114486)
[pages](https://gold.jgi.doe.gov/study?id=Gs0154202) did not provide usable
metadata: one was inaccessible, the other returned an application error.
Exact-accession searches found no usable result. Their existence and path
membership remain inventory-backed, not independently verified online.

The current [GOLD classification workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
confirms node 7099 at `site data` row 343 with two trailing Unclassified
fillers. It does not independently verify historical nodes 5974/7098 or the
source counts. Download: 84,174 bytes; SHA256
`f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.
No exact target named-taxon or environmental-parameter row was found. Child
records' organisms, biosamples and studies were not transferred to the parent.

Current [official BTO metadata](https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms?obo_id=BTO%3A0000316)
marks the identifier obsolete. Fresh primary
[BTO OWL](https://raw.githubusercontent.com/BRENDA-Enzymes/BTO/master/bto.owl)
confirms `owl:deprecated true`; its declared release is 2021-10-26. The
inspected class supplies a comment about culture fluid, not an explicit exact
replacement. BTO:0002233 describes filtered liquid and has culture medium as
a RELATED synonym, so it cannot replace a category that also includes solids.
OWL: 10,645,778 bytes; SHA256
`f89ff8a04b57ffee51cf07b05c70b39b3a6b2026940d5bda851e943a4b1a0f4b`.

The local `ontology_terms.tsv:318` retains an empty deprecated field. The
current `_load_bto` at `src/habitatmech/extract.py:876-881` already preserves
deprecation literals, with six passing regression tests and a recorded prior
infrastructure session. Do not report that loader fix as still missing.
The remaining governed inventory refresh and decision/eligibility work are
distinct: the in-memory probe shows flag recovery alone does not change this
record. An ignored-inclusive search of `seed.py` and `curate/decisions.py`
found no deprecation handling, consistent with the executed result.

## Completeness

Ignored-inclusive searches for the exact ID, minted source key, label, stem,
path and source nodes covered curation, raw inventories, path/retirement
registries, configuration, docs, tests, history, research, its manifest and
prior individual reviews. They found the decision, source rows, infrastructure
history, dependent records and older contextual reviews, but no target-owned
authored definition, parent exclusion, overlay, research report, session
history, retirement or previous individual review. Older recommendations to
add this BTO parent are not fresh evidence that it is active.

There are nine decisions directly targeting BTO:0000316: this GROUND row and
eight GROUND_AS_PARENT rows. Separately, nine emitted records list it as a
parent: the four organism-qualified media and five contaminated categories.
Archaea inherits it through the source hierarchy without a direct BTO-targeting
decision. These are dependency diagnostics, not nine newly completed reviews;
migration must assess both direct decisions and independent source contributions.

The bounded ignored-inclusive source-file search found no original GOLD
node/edge dumps, goldData.xlsx, biosample-sweep intermediate or original
kg-microbe bto.db in `build`, `data/raw` and configured kg-microbe `data`.
It did find the current OAK `build/oak-current-20261008/bto.db` cache and its
compressed copy; these are not the missing extraction snapshot. No global
absence claim is made. The cited sibling CultureMech checkout exists and its
README describes recipe curation; it does not establish this ontology identity
or supply a formulation for the general category.

Empty optional biology is not a defect. With no named organism, gene,
regulator, pathway or transcriptomic assertion, iModulonDB is not applicable.

## Findings

Zero blockers, one major finding, zero minor findings.

1. **Major: obsolete BTO term remains an exact reviewed identity.** Primary
   BTO explicitly deprecates BTO:0000316, while the maintained ITEM decision
   and generated record continue to adopt it. The empty local flag and
   successful in-memory true-flag emission expose separate provenance and
   eligibility surfaces. Owners: governed BTO inventory refresh,
   `curation/decisions.tsv`, and ontology eligibility in
   `src/habitatmech/seed.py` / `src/habitatmech/curate/decisions.py`.

The undefined Lab culture parent and inaccessible original sample context
remain unresolved scope questions, not independently established additional
defects or an endorsement of those assertions.

## Recommended Edits

Complete a reproducible BTO refresh with source receipt, then choose a
supported active identity or an explicitly defined minted medium concept.
Preserve both solid and liquid scope; do not mechanically redirect to culture
fluid or treat an ontology synonym comment as an equivalence axiom. Reassess
the source decision and all dependent direct/source-parent contributions
together, with fail-closed eligibility checks and explicit scope regressions.
Do not hand-patch generated records, inventory checksums or published history.

Independently assess what Lab culture denotes before retaining, replacing or
excluding its strict parent contribution. The owning surfaces are the exact
source decisions and, if supported, `term_requests.tsv` or
`gold_parent_exclusions.tsv`. No definition should be invented just to remove
an edge. Preserve the GOLD path, three nodes, 273 ORGANISM count, separate
47-BIOSAMPLE evidence and the limits of the one-sample triad.

## Follow-up Checks

Regress active versus obsolete ontology eligibility, source-to-record mapping
endpoints, typed non-equivalent replacement handling, all nine incoming parent
records and all nine direct decision rows. Check zero unintended merges,
source counts, plural synonym provenance and lifecycle derivation. Authorized
curation needs append-only session history, dry seed, inspected canary,
provenance/strict/history/label/reproduction gates and full QC. Identity changes
also require committed-history redirect handling, site regeneration and
semantic-map input comparison. A label pass alone cannot prove a safe migration.
No SSSOM/KGX or current kg-microbe modeling readiness is certified here.

## Additional Notes

Only this target's new report was written. Scientific inputs, generated
records/pages, lifecycle/history and GitHub remained unchanged. No paid
research or delegation was used. External OWL, ontology API and workbook
responses were parsed in memory. The primary deprecation check was fresh;
the older infrastructure history was read only to distinguish already-fixed
extraction behavior from outstanding refresh and eligibility work.
