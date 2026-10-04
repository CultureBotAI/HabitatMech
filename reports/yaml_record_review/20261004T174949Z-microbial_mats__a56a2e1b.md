# YAML Record Review: Microbial mats

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/microbial_mats__a56a2e1b.yaml`
- Started UTC: 2026-10-04T17:47:51Z
- Finished UTC: 2026-10-04T17:49:49Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.2a0de7e155, Microbial mats,
AQUATIC, NARROW/REVIEWED. It has two lake parents, one GOLD attestation with
seven ORGANISM assertions and skos:narrowMatch, and two history events.
Definition, synonyms, xrefs, parameters, taxa, citations, graphs, discussions,
datasets and replacement links are not emitted. ENVO:01000008 is not a parent.

The exact source is gold.ecosystem:7890,
`Environmental > Aquatic > Non-marine Saline and Alkaline > Soda lake > Microbial mats`.
The actual mint matches; PATHS.tsv:1598 pins the stem. This is the soda-lake
mat, not the whole lake, its sediment or the separate hypersaline-soda-lake mat.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/microbial_mats__a56a2e1b.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/microbial_mats__a56a2e1b.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared fresh run PASS: 1,179 canonical pairs, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Terminal PASS: 457 tests, three skipped, two warnings in 763.06 seconds; 90 history records, 3,206 strict records, 32 graph curations, exact reproduction, site/redirect/term-request gates and all remaining gates passed. |
| Source/reference checks | Full target and parent, exact decisions, all 14 raw tables, actual resolver, official typed OWL/current OLS, full page and isolated semantic comparisons inspected. |

Product validation is the documented identifier-label gate, not a complete
SSSOM/KGX semantic audit. No downstream export run is claimed.

## Identity and Grounding

`curation/decisions.tsv:328` is an ITEM GROUND_AS_PARENT decision dated
2026-08-13 targeting ENVO:00000019 saline lake. Its rationale concerns the
specificity of a soda lake, not the mat leaf. REVIEWED and the two events
are mechanically faithful, but the wrong scoped decision remains wrong.
A mat in a soda lake is neither a kind of saline lake nor a kind of whole
soda lake. The verified generic ENVO:01000008 microbial-mat structure is
the defensible broader candidate for this source leaf. Mat material,
ENVO:01000157, is a separate class and not an automatic identity substitute.

The complete `soda_lake.yaml` parent is habitatmech:GOLD.b11bdfbd7c,
NARROW/REVIEWED, with 52 ORGANISM assertions and two collapsed nodes.
Its maintained row at `curation/decisions.tsv:1001` supplies the same
lake-oriented reasoning. Parent observations and parent identity decisions
cannot be transferred to this mat or repair its mat-to-whole-lake edge.

Current [ENVO:00000019 saline lake](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000019)
denotes a salt-containing lake. [ENVO:00002121 alkaline salt lake](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002121)
is its high-pH subclass. The latter is present in the vendored slice at
`ontology_terms.tsv:7217`, including the soda-lake synonym. Crucially,
current typed OWL marks `soda lake` as **hasRelatedSynonym**, not exact;
the OLS flattened synonym list alone hides that scope. The row's no-soda-
lake-term rationale does not assess this relevant candidate, but neither
the synonym nor a better lake term licenses grounding a microbial mat to it.
No automatic parent-lake identity merge is recommended by this child review.

## Evidence

Physical `gold_ecosystem_paths.tsv:583` contains the exact depth-five path,
one node, seven organisms, zero study/biosample counters and total seven.
The count and unit are faithfully emitted. The complete 14-table scan found
no exact-target bulk sample, API triad, study membership, parameter, PREGO
or BacDive taxon row. These bounded misses do not negate the seven upstream
organism assertions, establish biological absence, or permit borrowing the
parent's observations or the hypersaline-soda-lake sibling's evidence.

Current official GOLD vocabulary lookup for w3id.org/gold.path/7890 returned
404. The committed exact source is verified; current original contents were
not recovered, and no retirement inference is made. No pH or salinity
measurement, characteristic taxon or metabolic mechanism is established for
all members merely by the soda-lake source path.

Actual resolution using the full normalized mapping table gives default
gold_unmatched/UNGROUNDED/no predicate. Applying the ITEM row yields
curated_ground_as_parent_from_gold_unmatched, NARROW, skos:narrowMatch,
extra parent ENVO:00000019 and reviewed=True. The erroneous saline-lake
parent therefore comes from the maintained decision via `seed.py:554-566`
and `:839-843`. The independent source-parent pass at `:898-907` adds
habitatmech:GOLD.b11bdfbd7c. Removing only one contribution leaves the other.

Attestation emission at `seed.py:890-891` also reproduces #1398. Schema
`habitatmech.yaml:317-322` and `:776-790` describe source/record comparisons,
whereas the maintained row compares the retained source identity with an
ontology parent not represented as the attestation's target. Correcting
that ontology target alone will not fix the endpoint contract. A predicate
reversal is insufficient; no formal SKOS inconsistency is claimed.

## Completeness

Ignored-inclusive ID/key, stem, node, exact path and soda-lake label searches
covered curation, history, research, reports, PATHS and RETIRED. A separate
ignored-inclusive filename inventory found only the adjacent hypersaline-
soda-lake report. The ITEM row and lock exist; no target-owned definition,
overlay, dedicated research, session history, retirement or prior individual
target report was found. Broader research and alkaline-lake report snippets
were leads; current typed ontology evidence, not their exact-synonym wording,
supports the distinction above. Optional omissions are not additional defects.
iModulonDB is inapplicable: no gene, regulator or expression dataset is asserted.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | The mat's ITEM decision applies a lake rationale and supplies saline lake instead of a defensible microbial-mat genus. | Exact row GOLD.2a0de7e155 at curation/decisions.tsv:328; group with the separately verified salt-crystallizer mat's wrong-leaf decision. |
| Major | Independent GOLD ancestry makes the mat a kind of whole soda lake. | GOLD parent pass or governed exclusion for GOLD.2a0de7e155 and expected parent GOLD.b11bdfbd7c, #1397. |
| Major | NARROW/skos:narrowMatch use ontology-parent endpoints inconsistent with declared source/record semantics. | Resolver, attestation emitter, schema and mapping consumers, #1398. |

Counts: zero blockers, three major, zero minor. The minted source identity
and mat label remain intact; count/unit and ITEM-derived review/history are
faithfully generated. These are not grounds to relabel the record as a lake.

## Recommended Edits

1. Correct this source's ITEM decision to use the verified microbial-mat genus
   with a complete leaf-specific rationale. Preserve the mint, exact source
   path/node, seven-ORGANISM count and prior events. Do not bulk-change the
   separate Soda lake or Sediment decisions to a mat target.
2. Independently suppress the mat-to-Soda-lake contribution. Changing the
   parent lake's ontology grounding cannot make the whole lake a mat genus.
3. Reconcile mapping endpoints/status meanings across routes; do not assume
   the better genus fixes #1398 or use a global predicate swap.
4. Add exact decision/edge/endpoint and source-preservation regressions,
   append required correction history and regenerate from maintained inputs.

## Follow-up Checks

After correction run `just seed`, then
`just seed-canary habitatmech:GOLD.2a0de7e155 --force`. Inspect the entire
canary, correct mat genus, absence of both lake parents, seven-ORGANISM
count, REVIEWED derivation and prior events plus new correction history
before `just seed-apply --force`. Never prune partial runs. These commands
describe future curation, not actions performed by this review.

Require ordinary/strict validation, ontology labels, source/history and
mapping-consumer tests, `just verify-corpus` and `just qc`. The complete page
shows both lakes as Broader habitats. Isolated in-memory removal of each
parent separately changes actual full-context semantic text. The scientific
repair needs genuine map/site refresh under #1217; predicate-only omission
was separately text-neutral. Preserve draft #1218 and runtime pins. Audit
actual SSSOM/KGX products before claiming compatibility or an export failure.

## Additional Notes

All-state exact-source and soda/mat issue searches returned no results.
Track the wrong-leaf decision with the separately reviewed crystallizer-mat
decision, not as an automatic-source-parent-only repair. Extend #1397 and
#1398 for their distinct contributions; report publication fixes none of them.

The maintained note ends `Microbi`; the event copies that text verbatim
while the full attestation path remains intact. Official typed OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated product, old report/history or paid research changed.
