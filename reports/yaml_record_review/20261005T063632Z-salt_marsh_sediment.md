# YAML Record Review: Salt marsh sediment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/salt_marsh_sediment.yaml`
- Started UTC: 2026-10-05T06:33:38Z
- Finished UTC: 2026-10-05T06:36:32Z
- Verdict: needs curation; 0 blocker, 2 major, 0 minor findings.

## Target

The complete generated HabitatRecord was read. Minted identifier
habitatmech:GOLD.96f7d4c555 denotes sediment from the marine/intertidal
salt-marsh source, not the whole marsh, marsh biome or shore zone. It is
AQUATIC, UNGROUNDED and SEEDED, with one parent, one GOLD attestation
carrying nine ORGANISM assertions and two history events. There is no
definition, synonym, xref, parameter, taxon, evidence item, graph,
discussion or dataset. PATHS.tsv:2407 pins the stem. No scientific input
or generated output was edited.

## Validation

- `just validate data/habitats/aquatic/salt_marsh_sediment.yaml`: pass.
- `just validate-strict data/habitats/aquatic/salt_marsh_sediment.yaml`:
  pass, one file and zero errors.
- Complete build_corpus/build_document dictionary equality: pass; one
  source concept, zero ITEM-reviewed sources, no taxa and two events.
- Fresh batch `just validate-products`: pass, 1179 canonical, one
  synonym, five exceptions and 2054 no-adapter skips. This gate does not
  validate minted definitions or the scientific meaning of a parent edge.
- `just worklist --status all --limit 5`: pass, 953 ungrounded records
  and 1810 decisions; the exact source route was independently executed.
- Fresh `just qc` remains live near the end of tests, after lint,
  documentation and provenance passed. Initial sandbox cache-access
  failures were retried with the required access. Terminal success and
  subsequent gates are not claimed at review close. Log:
  /private/tmp/habitatmech-salt-flat-marsh-qc-20261005.log.
- Actual full-context semantic text changes when the zone parent is
  removed. No record, map, page or export was regenerated.

## Identity and Grounding

Actual minting reproduces GOLD.96f7d4c555. Default gold_unmatched is
UNGROUNDED with no mapping predicate. The CONFIRM_UNGROUNDED row at
curation/decisions.tsv:878 is CLASS-level, explicitly leaving habitat
identity unassessed; curated_confirm_ungrounded_from_gold_unmatched keeps
reviewed=False. SEEDED and both historical events faithfully follow the
inputs. The absence of a mapping predicate is appropriate; this record
is not a #1398 retained-source narrowMatch witness.

Current official [GOLD node 5590](https://www.ebi.ac.uk/ols4/api/ontologies/gold/terms/https%253A%252F%252Fw3id.org%252Fgold.path%252F5590)
is active with the complete source path. Its vocabulary annotations
distinguish broad saline-marsh context, local intertidal zone and sediment
medium, with close-match links to saline marsh and sediment. Those links
are not an exact-identity instruction, nor are they the same dataset as
the historical sample-level API triads.

The sole parent habitatmech:GOLD.115edc36f8 was read in full during this
review sequence. It denotes the marine intertidal zone, carries 77
ORGANISM assertions and has its own ENVO reference and outgoing hierarchy.
The source-parent pass at seed.py:898-907 adds it independently of the
child's CLASS decision. Current typed ENVO and official
[ENVO:00000316 intertidal zone](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000316)
identify a geographic shore/seabed area between tide marks. Sediment
material found there is not a kind of whole zone. The parent's separate
marine-water-body edge is #1253; fixing that outgoing edge alone would
not fix this child's material-to-zone assertion.

The committed ontology inventory and current OLS were searched for
salt marsh sediment, saline marsh sediment and marsh sediment. The
bounded OLS queries returned no candidates for those exact phrases,
and ignored-inclusive inventory searches found no exact marsh-sediment
class. This does not establish absence from every ontology.

Current official ENVO and typed OWL distinguish these alternatives:

| Candidate | Scope / consequence |
| --- | --- |
| ENVO:00002007 sediment | Generic particulate material formed by transport/deposition by flowing liquid. A defensible material-genus candidate, not exact identity for all qualified marsh sediment. Inventory row 7170. |
| ENVO:03000033 marine sediment | Defined by transport through a marine water column and settling on the seafloor; typed under sediment with separate marine-water relations. Assess those conditions before adopting it for every marsh member. Row 9589. |
| ENVO:03000034 shallow marine sediment | Adds shallow ocean-basin/shelf context. A shallow marsh location alone is not proof of this depositional scope. Row 9590. |
| ENVO:01001036 sediment permeated by saline water | Requires saline water filling pore space; do not infer permanent saturation solely from source location. Row 8531. |
| ENVO:01001050 saline sediment environment | Environmental system, not the sampled sediment material. Row 8545. |

[Marine sediment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03000033)
and [shallow marine sediment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03000034)
were checked specifically to avoid treating the word Marine in the source
path as proof of every narrower depositional condition. The generic
[sediment genus](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002007)
does not collapse this source into every sediment habitat.

## Evidence

Physical data/raw/gold_ecosystem_paths.tsv:541 records the depth-five path
Environmental > Aquatic > Marine > Intertidal zone > Salt marsh sediment,
one node 5590, nine organisms and zero tree study/biosample counts. The
generated count/unit and path are faithful; no node-collapse note is needed.

All 14 raw inventories were scanned for exact path/node membership.
gold_path_biosamples.tsv:149 separately records 197 bulk samples. API
triad rows 560-562 cover 55 complete-triad samples in one study, with one
term per slot and share 1.00: broad ENVO:01000022 marine salt marsh biome,
local ENVO:00000316 intertidal zone, and medium ENVO:00002007 sediment.
These role distinctions support material versus context; unanimous
annotations within one cohort are not source-wide exact equivalence.
The API/bulk crosswalk was not recovered. Neither sample count should
replace or be added to nine organism assertions.

Five exact study memberships were inspected:

| Study | Physical gold_studies.tsv row | Path count |
| --- | --- | --- |
| Gs0135152 | 2112 | 1 |
| Gs0154205 | 3901 | 4 |
| Gs0156834 | 4149 | 1 |
| Gs0161450 | 4416 | 1 |
| Gs0164318 | 4544 | 3 |

All five original study-page requests returned 403. Their table membership
is verified; experiment contents, individual samples and the identity of
the one API study remain unrecovered. A shared multi-path study does not
make sediment a woodchip bioreactor or a root compartment. No exact
parameter, PREGO, BacDive or Madin taxon contribution was found. The
whole-marsh sibling's 91 organisms and separate sample cohorts are not
evidence to add here.

The primary [Frates et al. study](https://doi.org/10.3389/fmicb.2023.1235906)
was inspected in the publisher's abstract, methods 2.1-2.5, treatment
table and control comparisons. It collected salt-marsh sediment cores
at Little Sippewissett and used controlled incubations, activity labeling,
cell sorting and 16S sequencing to examine microbial communities.
That establishes a real microbial sediment habitat example, not a whole
shore zone. Carbon-amended experimental responses and local redox/taxon
observations are not universal properties of all marsh sediments.
The paper was not demonstrated to belong to any of the five GOLD studies;
no accession, measured chemistry or mechanism was imported.

The complete rendered page was inspected. It faithfully warns that the
decision is class-level, displays the nine ORGANISM assertions and lists
Intertidal zone as the only broader habitat. This reproduces the same
identity/hierarchy gaps instead of independently validating them.

## Completeness

Ignored/hidden-inclusive ID, node/path, label and stem searches covered
curation, conf, history, research, prior individual reports, inventories,
PATHS, RETIRED, docs, source and tests. The class-level row and path lock
exist; no target-authored definition, causal overlay, dedicated research,
separate history, retirement or prior individual report was found.
Earlier biome/whole-marsh reports mention this sibling only as context.

An ITEM-level identity ruling, source-qualified definition and true
sediment genus are consequential gaps: the sparse record currently
offers only its label and false geographic parent as identity context.
Optional numerical parameters, taxa, datasets and graphs should remain
empty without direct support. iModulonDB is not applicable because the
record has no gene/regulator/expression assertion; literature methods
were not promoted into record mechanisms.

## Findings

| Severity | Finding | Maintained owner / scope |
| --- | --- | --- |
| Major | A real source-qualified sediment habitat has no ITEM-level identity ruling, definition or defensible material genus. | Exact GOLD.96f7d4c555 row in `curation/decisions.tsv` and a keyed authored definition in `curation/term_requests.tsv`. |
| Major | The sole inherited intertidal-zone parent is geographic context, not a strictly broader class of sediment material. | Explicit false-parent ruling with definition parent_mode=REPLACE; source-parent/definition application in `src/habitatmech/seed.py`. |

No blocker or minor finding was established. UNGROUNDED/SEEDED, predicate
omission, count/unit, source path and historical derivation remain faithful.

## Recommended Edits

1. ITEM-confirm the source-qualified habitat as UNGROUNDED and add an
   evidence-backed definition using a justified sediment-material genus.
   Preserve the salt-marsh/intertidal scope without inventing universal
   vegetation, salinity, oxygen, inundation or taxonomic attributes.
2. Use parent_mode=REPLACE only after explicitly ruling the sole zone
   parent false. Assess marine/depositional and pore-water restrictions
   before choosing a narrower genus; do not exact-merge with generic
   sediment, marsh, biome, zone or soil merely to remove an empty field.
3. Retain UNGROUNDED for the authored-definition route. The maintained
   definitions guard rejects NARROW and ontology-owned targets; do not
   combine GROUND_AS_PARENT with an authored term-request definition.
4. Preserve node/path, nine ORGANISM assertions, stable stem, source
   category and old events; append required new history. Recover original
   source membership before enriching taxa, parameters or datasets.

## Follow-up Checks

Regress retained mint, genuine ITEM scope, accepted definition/genus,
removed false zone parent, unchanged source count/provenance and absent
mapping predicate. Dry-seed and inspect a forced GOLD.96f7d4c555 canary
before guarded wider regeneration; never prune a partial run. Require
ordinary/strict schema, labels, provenance/history, full reproduction,
site/redirect, term-request and complete QC gates.

Actual parent removal changes semantic text; compare the new definition
as well. Perform genuine map/site refresh under #1217 without changing
protected #1218 or runtime pins. Actual SSSOM/KGX products and current
kg-microbe contracts still need separate compatibility auditing.

## Additional Notes

All 577 open/closed issue titles and bodies were searched for exact
ID/node and salt-marsh-sediment wording; no target-specific owner was
found. #1253 is the parent's distinct outgoing edge, not this child fix.
Issue comments were not exhaustively searched. No GitHub mutation
occurred during this individual review.

Typed ENVO snapshot SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
