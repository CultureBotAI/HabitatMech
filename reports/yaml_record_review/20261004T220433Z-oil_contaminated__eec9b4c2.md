# YAML Record Review: Oil-contaminated

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/oil_contaminated__eec9b4c2.yaml`
- Started UTC: 2026-10-04T22:02:08Z
- Finished UTC: 2026-10-04T22:04:33Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.d640d7cf58, Oil-contaminated,
AQUATIC/NARROW/REVIEWED, from Environmental > Aquatic > Marine > Oceanic >
Oil-contaminated. It has two parents, one GOLD attestation with 11 ORGANISM
assertions and two history events. Definition, synonyms, taxa, parameters,
xrefs, evidence, graphs, discussions and datasets are absent.
`data/habitats/PATHS.tsv:2872` pins oil_contaminated__eec9b4c2.

This is the Oceanic qualified-water source, not the same-label Intertidal
source or the separately inventoried Oil-contaminated sediment leaf. Shared
words and a shared study do not establish that their source identities merge.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/oil_contaminated__eec9b4c2.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/oil_contaminated__eec9b4c2.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared batch PASS: 1,179 canonical, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | Shared PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Fresh batch run active in tests beyond 62%; lint, documentation and 14-inventory provenance passed. No terminal result claimed. |
| Source/reference checks | Complete target, actual child/parent resolution, full generated-field equality, all 14 raw tables, current typed ENVO/OLS and GOLD, all four original-study attempts, entire page and semantic comparison. |

Full construction reproduces every target field with one source concept and
one reviewed source. Prior PR #1416 main-push QC was observed terminal SUCCESS
during this review; it is not a substitute for the fresh running batch gate.
No SSSOM/KGX compatibility or original ecological verification is claimed.

## Identity and Grounding

Actual source minting reproduces the record identifier. The automatic
gold_unmatched/UNGROUNDED answer is replaced by ITEM GROUND_AS_PARENT at
curation/decisions.tsv:1182, dated 2026-08-13. It retains the minted source,
adds ENVO:00002149 sea water, and yields NARROW/skos:narrowMatch through
curated_ground_as_parent_from_gold_unmatched. The reviewed state and two
history events are faithful; no exact ontology identity was established.

Current [GOLD node 4011](https://www.ebi.ac.uk/ols4/api/ontologies/gold/terms/https%253A%252F%252Fw3id.org%252Fgold.path%252F4011)
is active for the exact path, with broad marine-biome and local oil-spill
annotations, but no exact-match or medium assertion in the inspected live
response. Committed medium summaries predominantly support the curator's
seawater-material reading, while their heterogeneity and inaccessible
original studies limit a universal claim. Do not exact-ground to oil spill,
oil contaminated soil, or generic sea water merely from one matching slot.

The source's old note that ENVO has only the soil term is not a current
exhaustive candidate audit. A structured label/synonym scan of the current
official OWL includes petroleum enriched sediment, oil field production
water, spill and oil terms, among others. None of those inspected labels
establishes exact identity for this qualified open-ocean water. Retain the
path-specific identity pending exact evidence rather than broaden it by fiat.

The oceanic-zone contribution comes from the immediate GOLD Oceanic parent,
habitatmech:GOLD.fc3b904cb2. Actual resolution defaults to gold_unmatched,
then its ITEM GROUND yields EXACT ENVO:00000207. seed.py:898-907 adds that
identifier to this child independently of the seawater-genus decision.

Current [ENVO:00000207 oceanic zone](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000207)
is an off-shelf water mass, a named subclass of ENVO:01000295 marine layer,
with a separate part_of ocean restriction. Marine layer is an aquatic
layer, part of a marine waterbody and composed primarily of sea water;
ENVO:01000325 itself is aquatic layer, not generic water material. These
typed relations distinguish the organized layer from material sampled in it.

The maintained child decision identifies oil-contaminated water material,
not a new whole layer or zone. Source nesting and offshore context alone
do not establish the zone as its strict genus. Under that material reading,
retain sea water and suppress the unsupported zone contribution. This is an
unsupported application hierarchy claim, not proof that water and water
masses are formally disjoint or that no future source evidence could justify
a different, explicitly defined layer interpretation.

The separate #1398 endpoint problem also applies. SourceAttestation at
schema lines 317-322 and GroundingStatusEnum at 776-790 compare source to
record identity. Here that identity is unchanged, while seed.py:554-566
derives NARROW/narrowMatch from the source-to-ontology-parent comparison
and copies it into the attestation at 890-891. The parent is not the field's
declared target. The [W3C mapping reference](https://www.w3.org/TR/skos-reference/#mapping)
does not make hierarchical self-links formally inconsistent; fix the
application contract, not a guessed global predicate direction swap.

## Evidence

`gold_ecosystem_paths.tsv:507` supplies depth five, one node 4011, 11
ORGANISM assertions and zero study/biosample counters in that inventory.
The generated attestation matches. `gold_path_biosamples.tsv:579` separately
supplies 13 bulk samples. These are different units, not contradictory counts.

Triad rows 623-625 cover 13 complete-triad samples and four studies:

| Slot | Distinct terms | Top term | Share | Agreeing studies |
| --- | ---: | --- | ---: | ---: |
| Broad | 2 | ENVO:00000447 marine biome | 0.92 | 3 |
| Local | 3 | ENVO:00002061 oil spill | 0.46 | 1 |
| Medium | 3 | ENVO:00002149 sea water | 0.69 | 2 |

All three current terms were inspected in this batch. The local spill term
is a plurality below one half, not universal context; seawater is a majority
medium, not the sole annotation. The other medium/local terms and individual
sample assignments are not recoverable from these modal summaries. Matching
13/13 bulk/API totals do not prove a sample-level crosswalk or homogeneity.
No contamination concentration, depth range or salinity threshold is supported.

Study rows 158, 340, 669 and 1778 identify Gs0050523, Gs0063184, Gs0111440
and Gs0133000. All four original study pages returned HTTP 403. The first
spans both intertidal and Oceanic oil-contaminated sources; the second spans
generic Marine and this path. Do not borrow entire experiments or collapse
their path memberships into sample-level corroboration.

The complete exact-path/source-ID scan covered all 14 raw tables. No PREGO,
BacDive, MADIN, taxon or parameter contribution feeds this target. Broad
text hits for the separate Oil-contaminated sediment path were explicitly
excluded from the exact-source scan. Eleven organism assertions without
named retained taxa are not evidence of absent microbial life. The rendered
page faithfully shows the path and 11 ORGANISM assertions.

## Completeness

Ignored-inclusive ID, exact path, label/stem and filename searches covered
curation, history, research, conf, reports, raw data, PATHS and RETIRED.
They found the maintained decision/path lock and neighboring environmental
research mentions, but no target-owned authored definition, overlay, session
history, retirement or previous individual report. Those research mentions
are contextual leads, not direct evidence for the original water samples.

A future governed definition could clarify material versus layer scope and
preserve the offshore qualifier; its present optional absence is not alone
a schema defect. Do not fabricate measurements, taxa or mechanisms to fill
empty slots. iModulonDB is inapplicable without gene/regulator/expression
claims. The empty synonym list provides no #1249 witness.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | GOLD Oceanic context supplies a strict zone parent not established for the curator's qualified-water-material identity. | Governed source-specific parent control and src/habitatmech/seed.py:898-907. |
| Major | GROUND_AS_PARENT puts a parent comparison into a source-to-record mapping/status contract. | Schema, decision resolver and consumers under shared #1398. |

Counts: zero blockers, two major, zero minor. Source heterogeneity is a
documented scope limitation, not a proved need to replace the seawater genus.

## Recommended Edits

1. Under the current material interpretation, suppress only the unsupported
   ENVO:00000207 contribution through maintained controls; retain seawater,
   the minted identity, source path/count/unit and history. Reassess original
   material/layer scope before making a different identity decision.
2. Reconcile #1398 with explicit mapping endpoints and regression coverage
   for this ITEM GROUND_AS_PARENT route. Do not globally swap predicates or
   convert the record into generic sea water to silence the mismatch.
3. Recover original studies and nonmodal annotations before universal
   ecological statements or a new definition. Update the existing decision
   if needed and append new history; do not edit generated records.

## Follow-up Checks

Dry seed and inspect `just seed-canary habitatmech:GOLD.d640d7cf58 --force`,
then guarded full regeneration without partial prune. Require source-scope,
parent-retention and endpoint tests, ordinary/strict/products/history checks,
provenance, exact reproduction, site/redirect/term-request checks and full QC.

Actual full-context removal of only the zone parent changes semantic text;
a predicate-only removal does not. Use genuine map/site rebuilding under
#1217 when inputs change, preserve protected draft #1218/runtime pins, and
inspect actual SSSOM/KGX endpoints before downstream compatibility claims.

## Additional Notes

All-state exact-key/node searches found no matching target issue. The earlier
same-label query returned unrelated closed #38. Shared #1398 already owns
the endpoint contract, not the target-specific contextual-parent question.
Official typed ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated artifact, old report/history, paid research
or GitHub item was changed by this individual review.
