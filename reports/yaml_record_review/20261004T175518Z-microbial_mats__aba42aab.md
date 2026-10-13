# YAML Record Review: Microbial mats

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/microbial_mats__aba42aab.yaml`
- Started UTC: 2026-10-04T17:53:55Z
- Finished UTC: 2026-10-04T17:55:18Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.17c67a52e1, Microbial mats,
AQUATIC, NARROW/REVIEWED. It has two parents, one GOLD attestation with three
ORGANISM assertions and skos:narrowMatch, and two history events. Definition,
synonyms, xrefs, parameters, taxa, citations, graphs, discussions, datasets
and replacement links are not emitted.

The exact gold.ecosystem:8100 source path is
`Environmental > Aquatic > Marine > Cold seeps > Microbial mats`.
The actual mint matches; PATHS.tsv:1451 pins the stem. This is the marine
cold-seep mat, not the seep feature, seep biome or freshwater-floodplain mat.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/microbial_mats__aba42aab.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/microbial_mats__aba42aab.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared fresh run PASS: 1,179 canonical pairs, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Terminal PASS: 457 tests, three skipped, two warnings in 763.06 seconds; 90 history records, 3,206 strict records, 32 graph curations, exact reproduction, site/redirect/term-request and all remaining gates passed. |
| Source/reference checks | Full target, ITEM row, all 14 raw TSVs, actual resolver, official typed OWL/current OLS, related issue scope and full page/semantic comparisons inspected. |

Identifier-label validation is not complete SSSOM/KGX compatibility testing;
no downstream export execution is claimed.

## Identity and Grounding

The real ITEM GROUND_AS_PARENT row at `curation/decisions.tsv:227`, dated
2026-08-12, retains this source identity beneath ENVO:01000008 microbial mat.
The source-specific identity, true generic mat parent, REVIEWED state and two
history events follow it. ENVO:01000157 denotes material derived from a mat,
not the intact structure; both were verified against official ENVO in this batch.

Current [ENVO:01000263 cold seep](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000263)
is active. Its typed OWL contains a merged definition whose target describes
a seep bringing hydrocarbon-rich fluids to the seafloor and whose source
describes the seafloor area of seepage. Its named parent is seep, ENVO:01000262;
other restrictions describe relationships to contextual entities rather than
microbial-mat identity. A mat occurring there is not itself the seep feature.
The source path preserves the location without justifying the strict broader edge.

The definition's contextual chemistry does not prove methane use, sulfur
oxidation or a characteristic organism for every mat assigned to this GOLD
bin. No such biological inference is needed to identify the false is-a.

## Evidence

Physical `gold_ecosystem_paths.tsv:712` gives the exact depth-five path,
one source node, three organisms, zero study/biosample counters and total
three. The generated count/unit is faithful. The complete 14-table scan
found no exact-target bulk-sample, API-triad, study, parameter, PREGO or
BacDive taxon row. These bounded misses neither contradict the three organism
assertions nor establish biological absence. Parent or adjacent seep cohorts
must not be imported to populate optional fields.

The current official GOLD vocabulary lookup for w3id.org/gold.path/8100
returned 404. The committed source path is verified; current original
contents were not recovered, and no retirement inference is made.

Actual complete normalized-table resolution gives default
gold_unmatched/UNGROUNDED/no predicate. Applying the ITEM row yields
curated_ground_as_parent_from_gold_unmatched, NARROW, skos:narrowMatch,
extra parent ENVO:01000008 and reviewed=True. The route is
`src/habitatmech/seed.py:554-566`, applied at `:839-843`. The independent
GOLD parent-path pass at `:898-907` adds the false seep parent.

Predicate emission at `:890-891` reproduces the separate #1398 contract
defect. SourceAttestation.mapping_predicate at schema `habitatmech.yaml:317-322`
declares source-to-record endpoints with omission when the source identity is
retained; GroundingStatusEnum at `:776-790` also compares source and record.
The decision instead compares the retained identity with an ontology parent,
not the attestation's declared endpoint. Reversing the predicate alone does
not fix that mismatch. No formal SKOS inconsistency or observed export failure
is asserted.

## Completeness

Ignored-inclusive exact ID/key, source-node/path and stem searches covered
curation, history, research, reports, PATHS and RETIRED. Separate cold-seep
label and filename searches found adjacent seep/biome reviews and a broader
host-associated research lead, not a target-owned definition, overlay,
dedicated research, session history, retirement or prior individual target
report. The ITEM row and path lock are present. No scientific claim was
adopted from the broader research. Optional omissions are not defects.
iModulonDB is inapplicable without a gene, regulator or expression dataset.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | The mat inherits the cold-seep feature as a strict broader habitat. | GOLD parent pass or governed exclusion for GOLD.17c67a52e1 and expected parent ENVO:01000263, #1397. |
| Major | Curated NARROW/skos:narrowMatch use ontology-parent comparison endpoints inconsistent with declared source/record fields. | Resolver, attestation emitter, schema and consumers, #1398. |

Counts: zero blockers, two major, zero minor. Mat identity, genuine mat
parent, three-ORGANISM count, ITEM review and event derivation remain sound.

## Recommended Edits

1. Suppress only the false seep context-parent contribution, preserving
   ENVO:01000008, exact source mint/path/node/count and actual review history.
   Do not merge the mat with the seep or populate unsupported mechanisms.
2. Reconcile mapping endpoints and grounding meaning across actual routes,
   preserving distinct source concepts and legitimate imported mappings.
3. Add exact-edge/source-preservation and endpoint-contract regressions,
   append required history and regenerate through maintained inputs.

## Follow-up Checks

After correction run `just seed`, then
`just seed-canary habitatmech:GOLD.17c67a52e1 --force`. Inspect the complete
canary, three-ORGANISM count, true mat parent, REVIEWED derivation and prior
events plus required correction history before `just seed-apply --force`.
Do not prune partial runs. These are future commands, not executed review edits.

Require ordinary/strict schema, labels, source/history and mapping-consumer
checks, `just verify-corpus` and `just qc`. The complete page lists cold seep
as a Broader habitat. Removing only that parent in the full-context semantic
adapter removes `broader habitat: cold seep`; scientific correction requires
the genuine map/site refresh in #1217. Predicate-only omission was separately
text-neutral. Preserve #1218/runtime pins and audit actual SSSOM/KGX output
before asserting compatibility.

## Additional Notes

All-state exact-source issue search found no match. Cold/seep/mat search
found #12 and closed #1161. The full #1161 body/comments concern report
instructions for freshwater-floodplain children, not this marine mat or an
implemented scientific repair. Extend shared #1397/#1398 with this independently
verified witness rather than treating that report closure as resolution.

Official typed ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific record/input, generated product, prior report/history or paid research changed.
