# YAML Record Review: Oil-contaminated sediment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/oil_contaminated_sediment__6a7b1764.yaml`
- Started UTC: 2026-10-04T22:08:30Z
- Finished UTC: 2026-10-04T22:10:58Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.77996bd8e6, Oil-contaminated
sediment, AQUATIC/UNGROUNDED/SEEDED. Its source is Environmental > Aquatic >
Marine > Neritic zone/Coastal water > Oil-contaminated sediment. It has one
parent, one one-ORGANISM GOLD attestation and two history events. Definition,
synonyms, taxa, parameters, xrefs, evidence, graphs, discussions and datasets
are absent. `data/habitats/PATHS.tsv:2168` pins the stem.

The target is the qualified neritic/coastal sediment source, not coastal
seawater itself, the Oceanic sediment source, or a generic petroleum material.
The exact source path and minted identity preserve those distinctions.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/oil_contaminated_sediment__6a7b1764.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/oil_contaminated_sediment__6a7b1764.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared batch PASS: 1,179 canonical, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | Shared PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Still active in the corpus-report stage; tests passed, 457 passed/three skipped/two warnings in 530.76 seconds. No terminal whole-run result claimed. |
| Source/reference checks | Entire target, actual child/parent resolution and full field reproduction, all 14 raw tables, current typed ENVO/OLS and GOLD, whole rendered page and full semantic comparison. |

Actual construction counts one source and zero reviewed sources, reproducing
all target fields. The lack of an ITEM decision is visible, not incorrectly
reported as REVIEWED. Validation does not establish the parent's scientific
meaning. No actual SSSOM/KGX compatibility audit was performed.

## Identity and Grounding

Actual minting reproduces habitatmech:GOLD.77996bd8e6. Its default route is
gold_unmatched/UNGROUNDED. CLASS CONFIRM_UNGROUNDED at decisions.tsv:708,
dated 2026-08-12, retains that result through
curated_confirm_ungrounded_from_gold_unmatched, reviewed=False. The note
explicitly limits itself to lexical no-match and says habitat status was
not assessed. Thus SEEDED, the class-level history caveat and absent mapping
predicate are faithful. This record is not a #1398 predicate witness.

The material head noun sediment in a marine path supplies a real candidate
habitat meaning. An ITEM assessment should compare current ENVO:03000033
marine sediment and ENVO:00002115 petroleum enriched sediment, independently
verified in this batch. They are not automatic exact identities: coastal
scope and oil composition still require source evidence. Retaining a minted
qualified identity with a defensible sediment genus is preferable to forcing
an exact match from a short leaf or declaring a novel term prematurely.

The sole generated parent [ENVO:00002150 coastal sea water](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002150)
is active and denotes sea water adjacent to a coast. Its named superclass
is ENVO:00002149 sea water, with a separate adjacency restriction to coast.
It is water material, not coastal sediment. The ontology intentionally leaves
the adjacency distance imprecise; no numerical coastal boundary is supported.

Actual immediate-parent resolution mints habitatmech:GOLD.89754b31f3 for
Neritic zone/Coastal water, defaults to gold_unmatched, then ITEM GROUND at
decisions.tsv:810 maps CLOSE to ENVO:00002150. The GOLD second pass at
seed.py:898-907 contributes that resolved identifier to the child. Even a
reviewed parent mapping does not make the sediment child a kind of water.
Correct this scoped edge rather than change the whole source parent globally.

Current [GOLD node 4033](https://www.ebi.ac.uk/ols4/api/ontologies/gold/terms/https%253A%252F%252Fw3id.org%252Fgold.path%252F4033)
is active but now labels its parent path Neritic zone, without the committed
/Coastal water suffix. It gives broad ENVO:00000447 marine biome and local
ENVO:00000206 marine neritic zone, marked partial, without a medium or exact
match in the inspected response. Current ENVO:00000206 is the ocean water
mass above a continental shelf, not sediment. Preserve this source-version
difference; neither renaming the pinned path nor replacing the bad parent
with another water-mass setting is a justified repair.

## Evidence

`gold_ecosystem_paths.tsv:954` gives depth five, one node 4033 and one
ORGANISM assertion, with zero study/biosample counters in that inventory.
All emitted attestation fields agree. The full structured scan of all 14
raw tables found no exact-source biosample, triad or study row. An additional
ignored-inclusive search for the current alternative Neritic zone path
found no matching committed source row, so its modern label was not used
to borrow counts from a different source.

No original organism accession, study accession, sample context or paper
was supplied by these aggregate inputs. Original organism-level ecology
was therefore not checked; there is no study ID to fabricate for a page
request. This is a bounded input limitation, not evidence that no studies
or organisms exist outside the inventories.

No PREGO, BacDive, MADIN, named taxon or environmental-parameter contribution
feeds the actual target. Do not import Oceanic or Intertidal sediment study
counts, offshore triads, taxa or oil chemistry simply because their leaf
labels match. The generated page faithfully shows one ORGANISM assertion,
the incorrect coastal-water parent, and the unreviewed/class-sweep caveat.

## Completeness

Ignored-inclusive ID, exact path, label/stem, current alternative path and
filename searches covered curation, history, research, conf, reports, raw
inventories, PATHS and RETIRED. The CLASS decision and path lock were found;
there was no target-owned definition, overlay, session history, retirement
or previous individual report. Same-label records in other settings are
not duplicates established by those searches.

The consequential next step is an ITEM material-scope assessment, not a
silent status promotion. Existing sediment candidates should be assessed
before a new term request. Optional taxa, parameters and causal mechanisms
must remain empty without evidence. iModulonDB is inapplicable without
gene/regulator/expression assertions. Empty synonyms provide no #1249 witness.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | GOLD source nesting adds coastal seawater as the sole strict parent of a sediment concept. | Governed source-specific parent control and src/habitatmech/seed.py:898-907; ITEM sediment-genus assessment belongs in the existing curation/decisions.tsv:708 row. |

Counts: zero blockers, one major, zero minor. The current unreviewed status
honestly records the class-level curation gap; it is not a separate false
endorsement or proof that the source has no fitting broader sediment concept.

## Recommended Edits

1. Suppress only the unsupported ENVO:00002150 source-parent contribution.
   Assess a real sediment genus through an ITEM update of the existing row,
   preserving the neritic/coastal qualified identity and one-organism evidence.
2. Compare marine and petroleum-enriched sediment against original source
   scope; do not automatically adopt an exact identity, merge same-label
   records, or substitute marine neritic zone as a new sediment genus.
3. Append new curation history for the actual correction. Preserve the old
   class-sweep event and pinned source path; refresh source versions only
   through governed extraction/provenance, not generated YAML edits.

## Follow-up Checks

Dry seed and inspect `just seed-canary habitatmech:GOLD.77996bd8e6 --force`,
then guarded full regeneration without partial prune. Require parent and
source-retention tests, candidate/status checks, ordinary/strict/products/
history/provenance validation, exact reproduction, site/redirect/term-request
gates and full QC. Ensure any added mapping satisfies the resolved #1398
endpoint contract rather than introducing the defect while adding a genus.

Actual full-context removal of the coastal-water parent changes semantic
text, requiring genuine map/site refresh under #1217. No record field was
changed by the in-memory probe. Preserve protected #1218/runtime pins and
inspect actual SSSOM/KGX products before compatibility claims.

## Additional Notes

All-state exact-key/node and the preceding same-label sediment searches
returned no matching issue. Official typed ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated artifact, old report/history, paid research
or GitHub item was changed by this individual review.
