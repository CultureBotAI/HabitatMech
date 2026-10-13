# YAML Record Review: Salt crystallizer ponds

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/salt_crystallizer_ponds.yaml`
- Started UTC: 2026-10-05T05:46:49Z
- Finished UTC: 2026-10-05T05:50:49Z
- Verdict: needs curation; 0 blocker, 2 major, 0 minor findings.

## Target

The entire generated HabitatRecord was reread as an individual target,
not merely as its previously reviewed children's context. Minted identifier
habitatmech:GOLD.277843111f denotes salt-crystallizer ponds. It is AQUATIC,
NARROW and REVIEWED, with two parents, one GOLD attestation carrying 103
ORGANISM assertions and a two-node collapse note, and two history events.
Definition, synonyms, xrefs, parameters, taxa, evidence, graphs, discussions
and datasets are absent. PATHS.tsv:1577 pins the stem. No scientific input,
generated output or prior report/history was edited.

## Validation

- `just validate data/habitats/aquatic/salt_crystallizer_ponds.yaml`: pass.
- `just validate-strict data/habitats/aquatic/salt_crystallizer_ponds.yaml`:
  pass, one file and zero errors.
- Complete build_corpus/build_document dictionary equality: pass, one
  contributing source, one ITEM-reviewed source, no taxa and two events.
- Fresh `just validate-products`: pass, 1179 canonical, one synonym, five
  exceptions and 2054 no-adapter skips. It does not validate the meaning of
  a parent edge or a minted source's mapping endpoints.
- `just worklist --status all --limit 5`: pass, 953 ungrounded records and
  1810 decisions; exact source minting and resolution were separately run.
- Fresh `just qc` is still live in the final corpus report. Lint, docs,
  provenance, tests (457 passed, 3 skipped, 2 warnings), history, strict
  schema, causal overlays, curation floor, exact reproduction, site, retired
  URLs and term-request checks passed. No terminal success is claimed here.
  Log: /private/tmp/habitatmech-waterbody-crust-qc-20261005.log.
- Actual full-context semantic text changes when the false water-material
  parent is removed. Isolated predicate omission is text-neutral. No map,
  site or SSSOM/KGX product was regenerated.

## Identity and Grounding

Actual minting reproduces GOLD.277843111f. Automatic gold_unmatched gives
UNGROUNDED with no predicate. The ITEM GROUND_AS_PARENT row at
curation/decisions.tsv:313 changes this to
curated_ground_as_parent_from_gold_unmatched, NARROW, skos:narrowMatch
and extra parent ENVO:00002012 hypersaline water. REVIEWED and the
2026-08-13 event follow that decision correctly, but the scientific judgment
confuses a pond with its water contents. Its pond-specific rationale does
not establish that the whole pond is a kind of water material.

Current official OLS and typed ENVO OWL confirm active
[hypersaline water ENVO:00002012](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002012)
and [brine ENVO:00003044](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00003044)
as water materials. Neither is a pond genus. The current definition of brine
is composition-specific, not an instruction to replace a feature with its
sampled medium.

Verified broader candidates are
[ENVO:03600092 artificial pond](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03600092),
inventory row 10126, and its parent ENVO:00000033 pond, row 6629. The former
expresses a human-constructed pond without imposing a seawater feedstock.
ENVO:00000055 saline evaporation pond, row 6649, is a tighter candidate
only after the source's scope is explicitly assessed: its definition requires
a shallow artificial pond designed to obtain salt from seawater. The
crystallizer stage is still narrower than evaporation ponds generally. Current
exact OLS searches for salt crystallizer pond and crystallizer pond returned
zero hits; ignored-inclusive inventory searches found no such exact term.
This bounded result is not proof of absence from every ontology.

The entire inland saline or alkaline environment parent,
habitatmech:GOLD.ce244e62cd, was read in this review sequence. The independent
GOLD parent pass contributes that source context. Its authored definition
and notes require an inland setting while acknowledging separately curated
out-of-scope descendants. Whether this minted source-qualified pond class
is intended to be geographically inland needs original source/cohort evidence.
Seawater feedstock alone does not prove geographic non-inlandness. This
review neither certifies that second edge nor orders its blanket removal;
it is a scoped follow-up uncertainty, unlike the demonstrated water-material
genus error. Generic ENVO water-body findings cannot simply be copied here.

## Evidence

Physical data/raw/gold_ecosystem_paths.tsv:189 contains the depth-four path
Environmental > Aquatic > Non-marine Saline and Alkaline > Salt crystallizer
ponds, nodes 3755 and 3981, 103 organisms and zero tree study/biosample
counts. The generated count/unit and first-node collapse note are faithful.
Current official [GOLD 3981](https://www.ebi.ac.uk/ols4/api/ontologies/gold/terms/https%253A%252F%252Fw3id.org%252Fgold.path%252F3981)
is active with the exact path and a partial broad aquatic-biome annotation;
3755 returned 404, not proven retirement.

All 14 raw inventories were scanned for exact path/node membership. Bulk
gold_path_biosamples.tsv:279 separately records 77 samples. API triad rows
740-742 cover 63 complete-triad samples in 14 studies: broad aquatic biome
and local saline evaporation pond each have share 1.00 and all 14 studies
agreeing; medium has three terms, with brine at share 0.67 and three studies
agreeing. The local feature and sampled medium are not interchangeable
identities. A unanimous local annotation is useful support for pond context,
not automatic exact equivalence or proof of every source member's feedstock.

Fourteen exact study memberships were inspected at these physical rows:

| Study | gold_studies.tsv row |
| --- | --- |
| Gs0050867 | 161 |
| Gs0069917 | 394 |
| Gs0072276 | 408 |
| Gs0075597 | 422 |
| Gs0114367 | 797 |
| Gs0128970 | 1515 |
| Gs0128972 | 1516 |
| Gs0130336 | 1607 |
| Gs0130342 | 1609 |
| Gs0131380 | 1649 |
| Gs0135215 | 2122 |
| Gs0141883 | 2260 |
| Gs0150277 | 3101 |
| Gs0150713 | 3525 |

All 14 original study-page requests returned 403. Equal study counts do not
prove these are the same 14 studies underlying the API aggregate; the
necessary crosswalk was not recovered. Do not sum the 77 bulk samples, 63
API samples or 103 organisms, or borrow the child water/mat cohorts. The
Gs0045085 membership found for the two children is not an exact membership
of this parent. No exact parameter, PREGO, BacDive or Madin taxon evidence
was found in the 14-table scan.

Inspected primary publisher methods for
[Plominsky et al., PMID:25395641](https://doi.org/10.1128/genomeA.01172-14)
and [Garcia-Roldan et al., PMID:37014230](https://doi.org/10.1128/mra.00039-23)
describe constructed solar-saltern systems, their final crystallizer ponds
and separately collected brine/water fractions. They support the distinction
between pond and contents and the constructed-pond candidate. PubMed article
identifiers were verified during this sequence. Neither study was connected
to one of the unavailable GOLD experiments; site chemistry and taxa are
not universal attributes to add to this record.

The retained-source NARROW/skos:narrowMatch output independently reproduces
#1398. Schema mapping_predicate at lines 317-322 and grounding status at
776-790 describe source/record comparisons; the actual decision compares
the minted source with an ontology parent, and seed.py:890-891 emits that
predicate without an explicit parent endpoint. A corrected pond genus alone
cannot reconcile the contract. No formal SKOS inconsistency or actual
downstream export failure is claimed.

The complete rendered page was inspected. It reproduces the wrong
hypersaline-water Broader habitats link, correct count/collapse note and
ITEM event. Faithful rendering is not scientific validation.

## Completeness

Ignored/hidden-inclusive ID, label, node/path and stem searches covered
curation, conf, history, research, prior individual reports, inventories,
PATHS and RETIRED. The decision and path lock exist. No target-owned authored
definition, causal overlay, dedicated research, separate history, retirement
or earlier individual pond report was found. Broader research and earlier
child reports are contextual leads, not an individual review of this pond.

Optional quantitative parameters, taxa, datasets and causal graphs should
remain empty without exact evidence. iModulonDB is not applicable because
the record has no gene/regulator/expression assertions. Original-study and
inland-scope uncertainties remain explicit rather than being filled by a
generic definition or guessed sample identity.

## Findings

| Severity | Finding | Maintained owner / scope |
| --- | --- | --- |
| Major | The maintained ITEM decision makes a whole salt-crystallizer pond a kind of hypersaline water material and omits a defensible pond genus. | Exact GOLD.277843111f row in `curation/decisions.tsv`, applied by `src/habitatmech/seed.py`. |
| Major | NARROW/skos:narrowMatch uses an ontology-parent comparison inconsistent with declared source/record endpoints. | Shared resolver, schema, emitter and consumers under #1398. |

No blocker or minor finding was established. Minted identity, source count,
unit, collapse provenance and mechanical review/history derivation remain.
The unresolved inland edge is not represented as independently validated.

## Recommended Edits

1. Correct this exact ITEM decision to a defensible pond genus, with a full
   source-specific rationale. Artificial pond is the scope-safe candidate;
   use saline evaporation pond only after documenting the seawater restriction.
   Preserve the crystallizer-specific minted identity rather than exact-merging
   it with all artificial/evaporation ponds or any water material.
2. Resolve #1398 separately with explicit mapping endpoints and consumer
   regressions. Do not use a global predicate swap or assume the new genus
   fixes source-to-record semantics.
3. Assess the inland source-parent scope independently from the wrong water
   genus. Do not remove it through a blanket REPLACE merely to leave one
   parent. An optional authored definition also requires a compatible
   UNGROUNDED decision; definitions.py rejects the current NARROW state.
4. Preserve nodes/path, 103 ORGANISM assertions, stable stem and prior events;
   append required correction history. Do not bulk-copy the pond repair into
   the microbial-mat or water children, whose appropriate genera differ.

## Follow-up Checks

Regress the exact decision, false-water-parent removal, retained minted
identity, source counts and endpoint semantics. Check the independent inland
edge and both child edges explicitly; repairing this parent's genus does
not fix a child material-to-whole-pond edge. Dry-seed and inspect a forced
GOLD.277843111f canary before guarded wider regeneration, never pruning a
partial run. Require ordinary/strict schema, labels, provenance/history,
mapping-consumer tests, full reproduction, site/redirect and full QC gates.

Actual water-parent removal changes semantic text, requiring genuine
map/site refresh under #1217. Preserve #1218/runtime pins and audit actual
SSSOM/KGX products before claiming current kg-microbe compatibility.

## Additional Notes

All 572 open/closed issue titles and bodies were searched. #1403's body
explicitly scopes its decision repairs to mats, not this pond; #1446 concerns
the generic evaporation pond's separate intertidal edge. Neither implements
this target correction. #1398 is the existing shared endpoint owner. Issue
comments were not exhaustively searched. No GitHub mutation occurred in the
individual review.

Typed ENVO snapshot SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
