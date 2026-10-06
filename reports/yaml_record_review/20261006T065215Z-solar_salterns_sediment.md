# YAML Record Review: Solar Salterns Sediment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/solar_salterns_sediment.yaml`
- Started UTC: 2026-10-06T06:47:38Z
- Finished UTC: 2026-10-06T06:52:15Z
- Verdict: needs curation

## Target

Read the complete generated `HabitatRecord`: `habitatmech:GOLD.d9d8c58a7b`,
Solar salterns sediment, AQUATIC, UNGROUNDED, SEEDED. `PATHS.tsv:2901`
pins its stem. Its single source is GOLD node `gold.ecosystem:8055`,
`Environmental > Aquatic > Marine > Intertidal zone > Solar salterns sediment`.
It has one parent, 42 ORGANISM assertions and two history events; no
definition, taxa, parameters, mapping predicate, evidence items or graph.
This is sediment material, not the whole saltern, its brine, salt crystals,
salt-marsh sediment or the separately pinned Salt pond sediment source.

## Validation

- Fresh `just validate data/habitats/aquatic/solar_salterns_sediment.yaml`:
  passed.
- Fresh `just validate-strict data/habitats/aquatic/solar_salterns_sediment.yaml`:
  one file, zero errors.
- Actual full `build_corpus` / `build_document` equality passed: one source,
  zero reviewed sources, zero taxa and two historical events.
- Actual child and parent routes used the complete normalized mapping table.
  All 14 raw TSVs were parsed for exact source/path membership. The full
  rendered page and actual semantic text were inspected.
- Current OLS and typed official ENVO verified five relevant classes,
  including their material/system distinction and formal restrictions.
  The correctly formed current GOLD path lookup returned 404.
- Unchanged-input baseline: the preceding publication's full local QC
  passed 463 tests, three skipped, two dependency warnings and all gates.
  The inspected [merge-group QC at base 752bbaafd](https://github.com/CultureBotAI/HabitatMech/actions/runs/37424165465)
  independently passed those counts, all 90 histories, closed validation
  and exact reproduction of 3,206 records, site and redirect checks.
  Required labels/vendor checks passed; labels reported zero flagged pairs
  and 2,054 SKIPPED_NO_ADAPTER entries, not universal ontology coverage.
  This is explicit baseline reuse, not a fresh full-QC run per target.
- No separate reference validator applies without evidence items or causal
  edges. Original GOLD organism membership and input hashes were not recovered.

## Identity and Grounding

The full source path reproduces the mint. Default resolution is
gold_unmatched with no predicate or extra parent. CLASS CONFIRM_UNGROUNDED
at `curation/decisions.tsv:1203` changes the route to
`curated_confirm_ungrounded_from_gold_unmatched`, still reviewed=False.
The record and page faithfully distinguish this sweep from ITEM review.
The class-level lexical miss is not a global proof of ontology absence.

The sole parent comes from the independent source-parent pass at
`src/habitatmech/seed.py:898-907`. Its path is
`Environmental > Aquatic > Marine > Intertidal zone`, mint
`habitatmech:GOLD.115edc36f8`. Fresh default/applied resolution takes
gold_narrower_than_leaf_match, with ENVO:00000316 as an extra parent and
no ITEM override. The complete parent record has 77 organisms, two collapsed
nodes (3770 and 4013), NARROW/SEEDED and one event. None of those counts,
mapping predicates or historical states transfers to the sediment child.

Typed [sediment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002007)
is particulate material formed by transport and deposition in flowing
liquid. Typed [intertidal zone](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000316)
is a geographic area between tide marks. Sediment located there is not a
kind of that area. Repairing the parent's own outgoing waterbody edge
would not repair this child-to-area claim.

Generic sediment is a defensible candidate genus for an ITEM definition,
not an exact equivalent of every saltern-qualified sediment.
[Marine sediment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03000033)
has explicit marine-water-column/seafloor deposition scope; seawater supply
or the GOLD Marine bin alone does not establish it for an operated pond.
[Sediment permeated by saline water](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001036)
requires saline pore water and specifies no numeric threshold. Verify that
scope before selecting it as a narrower genus. In contrast,
[saline sediment environment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001050)
denotes an environmental system, not the sediment material itself.

AQUATIC is faithful source context and is not a separate defect or authority
to move the pinned file. There is no material/soil conflict in this target's
recovered feeds; do not import the Salt pond sediment record's conflict.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:315` is the only exact-path row recovered
across all 14 raw TSVs: depth five, one node 8055, 42 organisms and zero
tree-derived study/biosample counts. The attestation preserves 42 ORGANISM;
these are not 42 taxonomically identified taxa, samples or independent studies.
No exact bulk-biosample, API-triad, aggregate-study, parameter, BacDive,
PREGO, Madin or mapping-table contribution was recovered.

The proper [current GOLD path lookup](https://www.ebi.ac.uk/ols4/api/ontologies/gold/terms/https%253A%252F%252Fw3id.org%252Fgold.path%252F8055)
returned 404; retirement and source replacement are not established.
Ignored-inclusive inventories of this repository and the configured
kg-microbe checkout found no original GOLD node/edge TSVs, `goldData.xlsx`
or `gold_biosample_triads.tsv`. Committed inventory reproduction is the
verified provenance boundary, not a reconstructed original organism roster.

The inspected primary [Mani et al. 2020 study](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2020.01891/full),
DOI 10.3389/fmicb.2020.01891, separately collected surface sediment and
brine from reservoir, evaporator and crystallizer pans at Siridao, Goa,
in February and May 2014. Its abstract and sampling methods support a
real microbial sediment habitat distinct from the liquid and operated
system. They do not identify GOLD's 42 organisms or justify transferring
the site's taxa, salinity, microbial abundances or mechanisms to this
whole source concept. No original GOLD study accession links this record
to that paper in the committed inventories.

## Completeness

Ignored-inclusive key/node/label/stem searches covered curation, history,
research, configuration, docs, source, tests, reports and the path registry.
Only the CLASS row and pinned path matched: no exact definition, causal
overlay, session-history record or earlier individual review was found.
These are bounded local absences, not proof that published research is absent.

Current structured ENVO search for solar saltern sediment returned zero
results; saline sediment returned seven candidates, including the distinct
material and environmental-system classes examined above. Search ranking
does not decide exact identity. An ITEM scope/definition would improve this
record, but honest SEEDED status and empty optional fields are not additional
required-content failures. The target asserts no gene, regulator or
expression claim; iModulonDB is not applicable, not negative evidence.

## Findings

1. **Major: sediment inherits geographic intertidal context as its sole
   strict superclass.** The source-parent pass in `src/habitatmech/seed.py:898-907`
   adds GOLD.115edc36f8 independently of the child CLASS row. The material
   needs a defensible material genus, not an is-a link to its setting.
   Extend the false-zone portion of [#1465](https://github.com/CultureBotAI/HabitatMech/issues/1465)
   with this distinct solar-saltern sediment witness. Maintained source-specific
   hierarchy handling, `curation/decisions.tsv` and, for an authored minted
   definition, `curation/term_requests.tsv` own the correction.

Zero blockers, one major, zero minors. The child has no mapping predicate;
its parent's NARROW/narrowMatch is not another #1398 witness for this child.

## Recommended Edits

ITEM-assess this exact source, retaining its saltern-specific material scope.
For a justified minted UNGROUNDED definition, explicitly document why the
sole inherited zone parent is false before choosing parent_mode=REPLACE
with a supported sediment genus. Do not use REPLACE as a general hierarchy
bypass, merge the material into a pond/system, or combine authored-definition
semantics with an incompatible ontology-owned/NARROW route.

Alternatively, a chosen grounding route needs maintained source-specific
controls to suppress the independently inferred false zone edge; a leaf
decision alone does not remove it. Preserve mint/path/node, category/stem,
42 ORGANISM, absent predicate and historical events. Do not borrow the
whole saltern's 157 organisms or the different salt-pond sediment cohorts.
Generated YAML/pages remain read-only in this review.

## Follow-up Checks

Regress exact parent-contribution suppression, material-versus-area/system
boundaries, genuine-genus retention, source count/unit and faithful ITEM
status/history derivation. Run dry seed, inspect a guarded forced canary,
append required curation history, and pass schema/strict, labels, provenance,
corpus, term-request, site/redirect and full QC for a scientific correction.

The complete rendered page publishes Intertidal zone as Broader habitats.
Removing the sole parent in actual full-context semantic input changes its
text, so a real hierarchy/definition correction needs genuine #1217 map/site
refresh while preserving protected draft #1218 and runtime pins. Predicate
omission was a no-op because the field is absent, not a mapping/export test.
Actual SSSOM/KGX products and current kg-microbe consumers were not audited.

## Additional Notes

All-state pagination searched 629 issue bodies/titles; no exact key, node,
stem or label witness matched. Full #1465 and #1446 bodies/comments were
read. #1465 owns the closest sediment-to-zone mechanism but its 22-sample,
two-study soil/sediment uncertainty does not belong to this source. #1446
and its new whole-saltern comment concern whole pond/system records, not
this material. Comments on every other issue were not exhaustively searched.
Scientific implementation remains open after report publication.

Typed official ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
