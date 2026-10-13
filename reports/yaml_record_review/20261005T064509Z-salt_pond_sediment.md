# YAML Record Review: Salt pond sediment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/salt_pond_sediment.yaml`
- Started UTC: 2026-10-05T06:37:31Z
- Finished UTC: 2026-10-05T06:45:09Z
- Verdict: needs curation; 0 blocker, 2 major, 0 minor findings.

## Target

The complete generated HabitatRecord was read. Minted identifier
habitatmech:GOLD.56c9d8587d denotes salt-pond sediment in a marine/intertidal
source path, not a whole pond, zone or biome. It is AQUATIC, UNGROUNDED
and SEEDED, with one parent, one GOLD attestation and two history events.
The attestation omits count/unit because the tree row has zero organisms.
There is no definition, synonym, xref, parameter, taxon, evidence item,
graph, discussion or dataset. PATHS.tsv:1921 pins the stem. No scientific
input or generated output was edited.

## Validation

- `just validate data/habitats/aquatic/salt_pond_sediment.yaml`: pass.
- `just validate-strict data/habitats/aquatic/salt_pond_sediment.yaml`:
  pass, one file and zero errors.
- Complete build_corpus/build_document dictionary equality: pass; one
  source concept, zero ITEM-reviewed sources, no taxa and two events.
- Fresh batch `just validate-products`: pass, 1179 canonical, one
  synonym, five exceptions and 2054 no-adapter skips. Scientific scope,
  minted definitions and parent meaning are not certified by this gate.
- `just worklist --status all --limit 5`: pass, 953 ungrounded records
  and 1810 decisions; the exact source route was independently executed.
- Fresh `just qc`: terminal pass, including 457 passed tests, three
  skips, two warnings, history, strict validation, causal curations,
  curation floor, full reproduction, site, redirect and term-request gates.
  Initial sandbox cache-access failures were retried with required access.
  Log: /private/tmp/habitatmech-salt-flat-marsh-qc-20261005.log.
- Actual full-context semantic text changes when the zone parent is
  removed. No record, map, page or export was regenerated.

## Identity and Grounding

Actual minting reproduces GOLD.56c9d8587d. Default gold_unmatched is
UNGROUNDED without a mapping predicate. The CONFIRM_UNGROUNDED row at
curation/decisions.tsv:539 is CLASS-level and explicitly leaves habitat
identity unassessed. curated_confirm_ungrounded_from_gold_unmatched keeps
reviewed=False. SEEDED and both historical events faithfully follow the
inputs. Predicate omission is appropriate; this is not a #1398 witness.

The current official [GOLD node 7710 request](https://www.ebi.ac.uk/ols4/api/ontologies/gold/terms/https%253A%252F%252Fw3id.org%252Fgold.path%252F7710)
returned 404. That does not establish retirement or erase the committed
source attestation. No current GOLD definition was recovered.

The sole parent habitatmech:GOLD.115edc36f8 was read in full during this
review sequence. It denotes the marine intertidal zone and carries its
own 77 ORGANISM assertions, which do not belong to this child. Current
typed ENVO and official [ENVO:00000316](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000316)
describe a geographic shore/seabed area between tide marks. Sediment or
soil located there is not a kind of whole zone. The source-parent pass
at seed.py:898-907 adds that context independently of the CLASS decision.
The parent's distinct marine-water-body edge is already tracked in
#1253; correcting it alone would leave this child's false parent intact.

The committed API medium is predominantly soil, not sediment. Current
official OLS and the typed snapshot distinguish the relevant roles:

| Term | Verified scope / consequence |
| --- | --- |
| ENVO:00001998 soil | Environmental material including mineral and organic components and interstitial fluids; not a geographic area. Inventory row 7163. A cohort annotation, not established source-wide exact identity. |
| ENVO:00000043 wetland area | Vegetated area overlapping a wetland ecosystem. Row 6639. Local context, not the sampled material. |
| ENVO:00000446 terrestrial biome | Biome primarily or entirely situated on land. Row 7030. Broad context does not automatically change this record's source-derived category. |
| ENVO:00002007 sediment | Generic transported/deposited particulate material. Row 7170. A candidate genus for the label-based sediment reading, subject to resolving the actual cohort scope. |
| ENVO:00000055 saline evaporation pond | Shallow, constructed pond designed for seawater salt production. Row 6649. Neither material identity nor a justified universal industrial setting for this source. |

[Soil](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00001998),
[wetland area](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000043),
[terrestrial biome](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000446)
and [saline evaporation pond](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000055)
are active. The last term has salt pond as a RELATED, not exact, synonym
in typed OWL. Do not borrow the whole-pond sibling's industrial definition.
Marine sediment ENVO:03000033 requires marine-water-column transport and
seafloor settling; saline-permeated sediment ENVO:01001036 requires saline
pore water. Those restrictions, inspected in this batch, are not proved
universally by the source path alone.

Bounded current OLS searches for salt pond sediment and pond sediment
returned no candidates; ignored-inclusive inventory searches found no
exact pond-sediment class. This is not an all-ontology absence claim.

## Evidence

Physical data/raw/gold_ecosystem_paths.tsv:1527 records the depth-five path
Environmental > Aquatic > Marine > Intertidal zone > Salt pond sediment,
one node 7710 and zero tree organism/study/biosample counts. Count/unit
omission and the source path are faithful; no node-collapse note is needed.

All 14 raw inventories were scanned for exact path/node membership.
gold_path_biosamples.tsv:502 separately records 22 bulk samples. API
triad rows 563-565 cover 22 complete-triad samples in two studies, with
two terms per slot. Each mode has share 0.91 and one study agreeing:
broad terrestrial biome, local wetland area and medium soil. Equal bulk
and API totals do not prove an accession-level crosswalk or source-wide
consensus. Neither sample total can replace the omitted ORGANISM count.

Two exact study memberships were read in full:

| Study | Physical gold_studies.tsv row | Path count |
| --- | --- | --- |
| Gs0053056 | 189 | 9 |
| Gs0114514 | 827 | 5 |

The first spans marine/coastal/intertidal, oil-contaminated sediment and
non-marine saline contexts. The second also includes marine wetlands and
terrestrial wetland soil. Shared study membership does not make every
sample belong to every listed path. Both original GOLD study requests
returned 403; experiments, sample accessions and the crosswalk to the
two API studies remain unrecovered. No exact parameter, PREGO, BacDive
or Madin taxon contribution was found in the 14-inventory scan.

The primary [Zhou et al. study](https://doi.org/10.1038/s41396-021-01067-w)
was inspected in its abstract and field-sampling, extraction and sequencing
methods. It examines microbial communities in former industrial salt
ponds, a restored pond and a reference marsh in the southern San Francisco
Bay. The same methods use both soil-core and sediment terminology,
illustrating why lexical disagreement alone does not prove disjoint
habitats. It provides a real microbial substrate example, not source-wide
industrial scope. Membership in either GOLD study was not established.
The article points to supplementary accession tables; an accession-level
cohort crosswalk was not completed. No genes, taxa, chemistry, universal
salinity threshold or causal mechanisms were imported.

The complete rendered page faithfully omits counts, warns that the
decision is CLASS-level and displays both history events. Its only
broader link is the same false zone parent; faithful rendering does not
validate the hierarchy.

## Completeness

Ignored/hidden-inclusive ID, node/path, label and stem searches covered
curation, conf, history, research, prior individual reports, inventories,
PATHS, RETIRED, docs, source and tests. The CLASS decision and path lock
exist; no target-authored definition, overlay, dedicated research,
separate history, retirement or prior individual report was found.
The earlier saline-evaporation-pond review only mentions this sediment
cohort as evidence that must not be borrowed for the whole pond.

An ITEM identity assessment, explicit material scope and supported genus
are consequential gaps because the record currently offers only a label
and false area parent. Preserve the soil/sediment uncertainty until
original sample context resolves it; do not force a split or equivalence
from the triad modes alone. Optional taxa, parameters and graphs should
remain empty without direct evidence. iModulonDB is not applicable:
the record makes no gene, regulator or expression-module assertion.

## Findings

| Severity | Finding | Maintained owner / scope |
| --- | --- | --- |
| Major | The CLASS decision leaves material identity, soil/sediment scope, definition and true genus unassessed. | Exact GOLD.56c9d8587d row in `curation/decisions.tsv`; source-qualified authored definition in `curation/term_requests.tsv` after resolving cohort scope. |
| Major | The sole inherited intertidal-zone parent is geographic context, not a strictly broader material class under either soil or sediment reading. | Explicit false-parent ruling and definition parent_mode=REPLACE; source-parent/definition application in `src/habitatmech/seed.py`. |

No blocker or minor finding was established. Count omission, source path,
predicate omission and historical derivation are faithful to the inputs.

## Recommended Edits

1. Recover original cohort metadata before making an ITEM-level scope
   ruling. Preserve the soil/sediment discrepancy explicitly; do not
   exact-ground to soil, pond, biome or zone merely because a triad or
   label suggests one. Do not infer industrial versus natural ponds.
2. Retain the minted UNGROUNDED identity for an evidence-backed authored
   definition, with a justified material genus and source restrictions.
   Use parent_mode=REPLACE only after explicitly ruling the sole zone
   parent false. Authored definitions require UNGROUNDED, not NARROW or
   ontology-owned targets; do not combine this with GROUND_AS_PARENT.
3. Preserve node/path, count omission, stable stem, source category and
   existing events; append required new history when curation occurs.
   Assess narrower marine-depositional and pore-water conditions before
   choosing a restricted genus. Do not import sibling counts or taxa.

## Follow-up Checks

Regress retained mint, real ITEM scope, accepted definition/genus, removed
false zone parent, unchanged provenance/count omission and absent mapping
predicate. Dry-seed and inspect a forced GOLD.56c9d8587d canary before
guarded wider regeneration; never prune a partial run. Require ordinary
and strict schema, labels, provenance/history, corpus reproduction,
site/redirect, term-request and complete QC gates.

Actual parent removal changes semantic text; compare definition changes
as well. Perform genuine map/site refresh under #1217 without changing
protected #1218 or runtime pins. Actual SSSOM/KGX products and current
kg-microbe contracts require a separate compatibility audit.

## Additional Notes

All 577 open/closed issue titles and bodies were searched for exact
ID/node and salt-pond-sediment wording. The hit #1446 owns the different
whole-pond ENVO:00000055 source and explicitly separates sediment cohorts;
it is not a repair owner for this record. #1253 owns a different outgoing
parent edge. Issue comments were not exhaustively searched. No GitHub
mutation occurred during this individual review.

Typed ENVO snapshot SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
