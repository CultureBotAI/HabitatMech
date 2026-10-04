# YAML Record Review: Microbial mat

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/microbial_mat__fc2dbb7f.yaml`
- Started UTC: 2026-10-04T16:00:02Z
- Finished UTC: 2026-10-04T16:02:01Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.f128d45ecf, Microbial mat,
AQUATIC, NARROW/SEEDED. Two parents, one uncounted GOLD attestation with
skos:narrowMatch and one seed event are present. Definition, synonyms,
taxa, parameters, citations/graphs, datasets, discussions, xrefs and
replacement links are not emitted.

The source is gold.ecosystem:7979,
`Environmental > Aquatic > Acidic > Acidic lake > Microbial mat`.
The actual mint reproduces the identifier; PATHS.tsv:3080 pins the stem.
This target is distinct from its Acidic lake parent, GOLD.41f771c2b4,
and from habitats under the separate Thermal springs source branch.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/microbial_mat__fc2dbb7f.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/microbial_mat__fc2dbb7f.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared batch run PASS: 1,179 canonical pairs, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | Shared run PASS: 953 ungrounded records and 1,810 decisions. |
| `just qc` | Shared invocation is active in its final corpus report. Tests passed: 457 passed, three skipped, two warnings; exact corpus reproduction, generated site, redirects and term-request checks have passed. No terminal whole-run result claimed yet. |
| Reference/source checks | Complete target, parent and parent review; all 14 raw tables; actual mint/resolver; official typed mat evidence; actual rendered page and semantic comparisons inspected. |

Schema and deterministic output checks do not validate is-a or mapping
endpoint semantics. Later terminal QC belongs in the publication receipt.

## Identity and Grounding

Current [ENVO:01000008 microbial mat](https://purl.obolibrary.org/obo/ENVO_01000008)
supports the broader microbial structure while preserving the source-specific
identity. Official OWL distinguishes ENVO:01000157 as derived mat material;
it is not an automatic identity replacement.

The entire `acidic_lake.yaml` parent is Acidic lake, UNGROUNDED/SEEDED,
without an authored associated-environment definition. Its CLASS
CONFIRM_UNGROUNDED decision is at `curation/decisions.tsv:452`.
The mat's location in that lake does not make it a kind of whole lake.
Correcting the parent's pH-band ancestry or choosing a lake genus would
not by itself repair this child edge.

The target mint and SEEDED state remain supported. NARROW is faithful to
the actual route but not to the schema's declared source/identifier comparison;
the latter is the separate endpoint-contract issue #1398.

## Evidence

Physical `data/raw/gold_ecosystem_paths.tsv:1422` contains the exact
depth-five path, one node and zero organism/study/biosample assertions.
Omitting a count follows the positive-organism-only rule. The parent lake's
48 ORGANISM assertions and collapsed-node note must not be transferred to
this zero-count child path.

The full structured scan of all 14 raw TSVs found no exact-target bulk
biosample, study, triad, parameter, PREGO or BacDive taxon row beyond the
tree source itself. This bounded absence does not establish that organisms
are absent, and the label does not provide measured pH, temperature or
community membership. No thermal-spring biology is inferred for this branch.

Actual resolver execution independently returns this mint through
gold_narrower_than_leaf_match, with NARROW, skos:narrowMatch and extra
parent ENVO:01000008. The mapping-table fallback is not reached.
`src/habitatmech/seed.py:784-791` creates the predicate; `:890-891`
copies it to the attestation; the separate pass at `:898-907` adds Acidic lake.

The contracts at `src/habitatmech/schema/habitatmech.yaml:317-322`
and `:776-790` describe source concept versus generated identifier.
This mint preserves the exact path identity, while the resolver compares
it with a generic ontology match whose endpoint is not explicit in the
attestation. This reproduces #1398 for this target. A predicate reversal
alone would still leave the wrong implicit target; no formal SKOS
inconsistency or downstream export failure is claimed.

Current OLS GOLD lookup for w3id.org/gold.path/7979 returned 404.
The committed node/path remain verified, but current original contents
were not recovered. No source retirement is inferred.

## Completeness

Ignored-inclusive target/parent IDs, node, full path, label and filename
searches covered curation, history, research, individual reports, PATHS and
RETIRED. They found both path locks, the parent's CLASS row and parent-review
mentions. No target-owned decision, definition, overlay, dedicated research,
separate history, retirement entry or earlier individual target report was
found. Generic microbial-mat label leads were searched this batch but not
promoted into evidence for this source.

The full `20260921T103849Z-acidic_lake.md` parent review was read as context.
It recommends revisiting this child after parent repair but is not an
individual mat review or evidence that its is-a edge has been corrected.
Optional empty fields are not separate defects. iModulonDB is not applicable:
no gene, regulator, expression dataset or mechanism is asserted.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | The acidic-lake mat inherits the whole Acidic lake as a superclass; source occurrence is not strict broader identity. | `seed.py:898-907`, or governed exclusion for GOLD.f128d45ecf and expected parent GOLD.41f771c2b4. |
| Major | NARROW/skos:narrowMatch use ontology-parent comparison endpoints on source/record contract fields. | Resolver/emitter and schema contracts, #1398. |

Counts: zero blockers, two major, zero minor. Source identity, generic mat
parent, count omission and derived SEEDED status remain supported.

## Recommended Edits

1. Exclude only this lake context-parent contribution. Retain ENVO:01000008,
   the exact mint/path/node and honest count omission. Do not borrow parent
   assertions, merge thermal-source identities or infer numeric pH from a label.
2. Reconcile #1398 with explicit mapping endpoints and coherent status meaning;
   avoid blanket imported-mapping changes or a predicate-only reversal.
3. Add exact-edge/source-preservation and endpoint regressions, append required
   history and inspect guarded regeneration. Authored definitions, if later
   supported, belong in maintained term requests after ITEM review.

## Follow-up Checks

Require schema, labels, provenance/history, exact corpus reproduction,
mapping-consumer tests and full QC. No SSSOM/KGX execution or compatibility
verdict is claimed. The complete rendered page currently lists Acidic lake
and microbial mat as Broader habitats and correctly omits an assertion count.

An actual full-context semantic-adapter comparison removing only the lake
drops `broader habitat: Acidic lake`. This hierarchy change requires a real
map/site rebuild under #1217. A separate predicate-only omission is
text-neutral, so not every contract fix needs new inference. Preserve
protected draft #1218 and runtime pins.

## Additional Notes

All-state exact-key issue search returned #389. Its full body/empty comments
were inspected: it concerns --force in the parent report's canary commands,
not either scientific mechanism found here. Extend #1397 and #1398 with
this separately verified mat witness rather than treating the command issue
as a scientific fix. Existing committed reports were not edited.

Official typed ENVO OWL inspected this batch has SHA-256
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific edit, status promotion, paid research or history rewrite occurred.
