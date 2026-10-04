# YAML Record Review: Microbial mat

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/microbial_mat__eb27cff0.yaml`
- Started UTC: 2026-10-04T15:57:10Z
- Finished UTC: 2026-10-04T15:59:07Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.f962316223, Microbial mat,
AQUATIC, NARROW/SEEDED. Two parents, one uncounted GOLD attestation with
skos:narrowMatch and one seed event are present. Definition, synonyms,
taxa, parameters, citations/graphs, datasets, discussions, xrefs and
replacement links are not emitted.

The exact source is gold.ecosystem:7146,
`Environmental > Aquatic > Freshwater > Floodplain > Microbial mat`.
The actual mint reproduces the identifier; PATHS.tsv:3146 pins the stem.
The parent Floodplain, GOLD.22656a226b, is a different record.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/microbial_mat__eb27cff0.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/microbial_mat__eb27cff0.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared batch run PASS: 1,179 canonical pairs, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | Shared run PASS: 953 ungrounded records and 1,810 decisions. |
| `just qc` | Shared run still active. Its tests passed: 457 passed, three skipped, two warnings in 736.65 seconds. Corpus reproduction has zero missing/extra/differing records; later full-QC gates are not yet claimed terminal. |
| Reference/source checks | Full target, full parent and parent review, complete 14-table source scan, actual mint/resolver, typed official ontology and actual page/semantic checks inspected. |

Shape validation and an earlier report correction do not repair the current
scientific edge. Later full-QC results belong in the publication receipt.

## Identity and Grounding

Current [ENVO:01000008 microbial mat](https://purl.obolibrary.org/obo/ENVO_01000008)
supports the generic mat superclass while retaining a distinct source-path
identity. ENVO:01000157 denotes derived mat material, not an automatic
replacement identity for this intact microbial structure.

The entire `floodplain__7ad4b08f.yaml` parent is Floodplain,
NARROW/SEEDED, without an authored associated-environment definition.
It inherits ENVO:00000255 flood plain and ENVO:00002011 fresh water.
Typed official [ENVO flood-plain evidence](https://purl.obolibrary.org/obo/ENVO_00000255)
denotes an area subject to periodic flooding, with named parent
ENVO:00000086 and exact Floodplain synonyms. A mat situated there does not
thereby become a flood-plain area. Whether the parent should eventually
merge to ENVO is a separate question; either identity still requires removal
of this context-only mat edge.

The target's source mint and SEEDED status are supported. Its NARROW value
matches the executed lexical route, but the source-attestation and grounding
contracts describe different comparison endpoints. That is the distinct
shared issue #1398, not a justification for changing mat identity.

## Evidence

Physical `data/raw/gold_ecosystem_paths.tsv:1462` contains the exact
depth-five path, one source node and zero organism/study/biosample assertions.
The emitted uncounted attestation is faithful to the positive-organism-count
rule. All 14 raw TSVs were scanned structurally: no exact-target bulk sample,
study, triad, parameter, PREGO or BacDive taxon row was found. These bounded
misses are not evidence of biological absence or of a measured flood regime.

Actual `resolve_gold` execution independently returns this mint with
NARROW, skos:narrowMatch and extra parent ENVO:01000008 through
gold_narrower_than_leaf_match. The mapping-table fallback is not reached.
`src/habitatmech/seed.py:784-791` creates the predicate, `:890-891`
copies it into the attestation and the separate `:898-907` pass adds Floodplain.

The declared contracts at
`src/habitatmech/schema/habitatmech.yaml:317-322` and `:776-790`
compare source concept and generated identifier. This mint retains that
source identity; the actual route instead compares it with a generic
ontology parent without emitting that comparison's explicit target in
the attestation. This is the #1398 endpoint-contract mismatch, not a formal
SKOS inconsistency or a sufficient reason to reverse the predicate alone.

Current OLS GOLD lookup for w3id.org/gold.path/7146 returned 404.
The committed source remains verified; current original source content
was not recovered and no retirement inference is made.

## Completeness

Ignored-inclusive exact target/parent keys, node, path, label and filename
searches covered curation, history, research, individual reports, PATHS and
RETIRED. They found path locks and parent-review mentions, but no target-owned
decision, definition, overlay, dedicated research, separate session history,
retirement entry or earlier individual target report. Generic mat-label
leads were also searched this batch, not treated as evidence for this path.

The full `20261002T081248Z-floodplain__7ad4b08f.md` parent report already
recommends excluding this child context edge. It is not evidence that the
implementation changed. #1161's full body and closure comment explicitly
limit its closure to a report-text correction. The generated target and
current source-parent code still demonstrate the scientific defect.

Empty optional fields are not separate defects. iModulonDB is not applicable:
no gene, regulator, expression dataset or mechanism is asserted. No downstream
SSSOM/KGX execution or compatibility audit was performed here.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | The mat inherits the Floodplain area as strict broader identity. Re-grounding the parent alone would preserve or redirect the unsupported edge. | `seed.py:898-907`, or a governed exclusion for GOLD.f962316223 and expected parent GOLD.22656a226b, coordinated with any future parent resolution. |
| Major | Locally generated NARROW/skos:narrowMatch use ontology-parent comparison endpoints inconsistent with source/record field contracts. | Resolver/emitter and schema contracts, #1398. |

Counts: zero blockers, two major, zero minor. The source identity, generic
mat parent, count omission and derived SEEDED state remain supported.

## Recommended Edits

1. Exclude this exact floodplain-context parent while retaining ENVO:01000008
   and the source mint/path/node. If the parent is later merged, verify that
   the exclusion still prevents a mat-is-a-ENVO-flood-plain edge.
2. Resolve #1398 with explicit endpoints and coherent grounding semantics;
   preserve legitimate imported mappings and do not merely swap predicates.
3. Add source-specific parent-resolution, provenance and mapping-contract
   regressions, append required history and inspect guarded regeneration.
   Do not hand-edit YAML/pages or revise committed review history.

## Follow-up Checks

Require schema, labels, source/history validation, exact corpus reproduction,
mapping-consumer tests and full QC. Read the complete generated mat after
any parent merge/exclusion and check both current and redirected parent cases.

The complete page shows Floodplain and microbial mat as Broader habitats.
An actual full-context adapter comparison removing only Floodplain drops
`broader habitat: Floodplain`; this requires a real semantic-map/site refresh
under #1217. A predicate-only omission is text-neutral, so inference is not
automatically needed for every contract correction. Protect draft #1218
and runtime pins.

## Additional Notes

All-state target/parent-key issue search found #1160, #1162 and closed #1161.
The latter was read fully and is report-only; the other titles concern parent
review follow-ups, not a demonstrated scientific implementation. Extend the
mat hierarchy witness set in #1397 and the shared contract set in #1398,
cross-referencing #1161 rather than reopening its completed report correction.

Official typed ENVO OWL inspected this batch has SHA-256
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific edit, status promotion, paid research or history rewrite occurred.
