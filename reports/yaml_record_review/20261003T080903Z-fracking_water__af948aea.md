# YAML Record Review: Fracking water

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/fracking_water__af948aea.yaml`
- Started UTC: 2026-10-03T08:09:03Z
- Finished UTC: 2026-10-03T08:20:23Z
- Verdict: needs curation

## Target

The complete generated `HabitatRecord` was inspected at baseline commit
`1b661b7ae4e6e6123e93af7e0c9638646a7cf18b`. The target is
`habitatmech:GOLD.3426da4c96`, `Fracking water`, category `AQUATIC`, grounding
`NARROW`, mapping status `SEEDED`. Its exact GOLD path is
`Environmental > Aquatic > Non-marine Saline and Alkaline > Fracking water`.
The distinct terrestrial `fracking_water` and engineered `input_fracking_water`
records are not targets of this review. `data/habitats/PATHS.tsv:1676` pins
the collision-resolved filename used here.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/fracking_water__af948aea.yaml` | Pass; no issues found |
| `just validate-strict data/habitats/aquatic/fracking_water__af948aea.yaml` | Pass; one record, zero errors |
| `just qc` | Pass; 451 tests passed, 3 skipped; all 3,206 records validate and reproduce, history/site/redirect/term-request gates pass |
| `git diff --cached --check` | Pass |
| Live `ENVO:01001869` check | OLS returns active `fracking liquid`, synonym `fracking water`, matching the vendored definition |

Full-corpus QC is the documented coverage for history, source provenance,
reproduction, and generated pages. A separate focused reference validator is
not documented in `justfile`; this record has no literature references or
causal edges. Full OAK `just validate-products` was not run locally for a
report-only change; the directly relevant ontology term was inspected live.

## Identity and Grounding

`data/raw/gold_ecosystem_paths.tsv:1560` supports the exact path, leaf label,
depth four, and nodes `gold.ecosystem:4694|gold.ecosystem:4695`. Both nodes
belong to the same collapsed source concept. The record correctly shows the
first and explains the two-node collapse in `source_attestations.notes`.
The row has zero organism/genome/sample/study assertions, so neither an
assertion count nor its unit is emitted.

The seeder's `resolve_gold` leaf-synonym route matches `fracking water` to
`ENVO:01001869`. The same leaf occurs at depth four under terrestrial Deep
subsurface (`gold_ecosystem_paths.tsv:814`), so the tie prevents either path
from claiming the ontology identity. The minted identifier, `NARROW`, and
`skos:narrowMatch` follow the repository's current resolution convention.
This explains the generated values; it is not item-level biological approval.

The first parent is `ENVO:01001869`, `fracking liquid`, whose committed
definition (`ontology_terms.tsv:9360`) and inspected
[OLS response](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001869)
describe a water-based liquid amended with thickening agents and proppants.
The second parent, `habitatmech:GOLD.ce244e62cd`, has the authored definition
of an inland saline or alkaline aquatic environment determined by a water
body (`curation/term_requests.tsv:43`). An environmental liquid and the
environment determined by a water body have different scopes. GOLD path
placement alone does not justify asserting that the same target is a kind
of both.

[EPA's hydraulic-fracturing water-cycle account](https://www.epa.gov/hfstudy/hydraulic-fracturing-water-cycle)
separates source-water acquisition, preparation and injection of fracturing
fluid, handling of returned water, and disposal/reuse. It supports keeping
these interpretations separate; it does not determine which one GOLD's
zero-assertion source bin denotes. The synonym makes the fluid interpretation
plausible, but no target-specific item decision resolves the full path scope.

## Evidence

| Claim | Nearest inspected support | Assessment |
|---|---|---|
| Source ID/path/label, node-collapse note | GOLD ecosystem row 1560 | Supported exactly |
| Minted ID and pinned slug | Source path; `PATHS.tsv:1676` | Supported |
| `AQUATIC` category | GOLD level-two category | Supported as source classification, not a natural-versus-engineered conclusion |
| Fluid parent and `NARROW` resolution | ENVO synonym plus tied leaf resolution | Mechanically supported; stage-specific meaning remains unreviewed |
| Inland aquatic-environment parent | Immediate GOLD path and maintained parent definition | Context is supported; simultaneous material/environment is-a claims are not established |
| `SEEDED` and single seeding event | No item decision; manifest extraction timestamp | Correctly avoids claiming review |

There are no record-level citations, causal mechanisms, taxa, parameters,
synonyms, xrefs, discussions, datasets, or definition to validate. The seeding
event agrees with `data/raw/MANIFEST.yaml` at `2026-08-16T05:58:02Z`.
The generated page `pages/habitats/fracking-water-habitatmech-gold-3426da4c96.html`
points back to the exact target YAML; it is not an independent evidence source.

## Completeness

The consequential gap is a definition of the fluid versus environmental-setting
scope and, if a fluid is intended, the process stage. The older source row's
zero assertions neither disprove the habitat nor justify adding taxa.
GOLD biosample/triad rows mentioning Fracking water belong to the terrestrial
path; `ENVO:01001869` also occurs as the medium for engineered Input fracking
water. Neither is evidence about this aquatic source bin's counts or identity.

Ignored/hidden-inclusive searches covered `curation`, `history`, `research`,
`conf`, `reports`, `data/raw`, and the slug lock using the target ID, source
node, filename, exact source path, and label. They found no target-specific
decision, authored definition, causal overlay, research report, history
session, or prior target review. The broader parent's research and curation
explicitly discuss fracking-water descendants, but do not adjudicate this
child's liquid-versus-environment identity. Those hits are not independent
evidence for a target definition.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | The record simultaneously asserts a liquid-material parent and a water-body-determined environment parent without a definition or item decision reconciling those scopes. The second edge is generated from GOLD context, not evidence that the liquid is a kind of the surrounding environment. | `curation/decisions.tsv`, `curation/term_requests.tsv`, and the GOLD parent-path insertion in `src/habitatmech/seed.py` |

Counts: zero blockers, one major, zero minor. No exact replacement grounding
is established by this review.
Tracked with the related context-parent findings in
[issue #1215](https://github.com/CultureBotAI/HabitatMech/issues/1215).

## Recommended Edits

1. Item-review the two-node GOLD source bin and record whether it denotes
   fracturing fluid, returned water, or a water-determined setting. Keep the
   aquatic and terrestrial concepts separate unless source equivalence is
   independently established.
2. Make the parents consistent with that interpretation. If a fluid is
   established, preserve supported material is-a parents and keep the
   environmental context in the source path. For the present `NARROW` record,
   introduce a scoped maintained hierarchy suppression/override: term requests
   are accepted only for `UNGROUNDED` records by
   `scripts/build_term_requests.py:196`. Use an ITEM `CONFIRM_UNGROUNDED`
   decision and an authored `REPLACE` definition only if evidence actually
   establishes a novel habitat with no exact term, a supported genus, and a
   false inherited parent. Do not change status merely to remove an edge.
3. Reconsider category only after the source meaning is resolved; the label
   alone does not justify forcing an engineered category or a produced-water
   grounding.

## Follow-up Checks

After an evidence-backed correction, run `just seed` and
`just seed-canary habitatmech:GOLD.3426da4c96 --force`; inspect both retained source
nodes, parents, status, and audit entries. Run focused schema/strict validation,
`just verify-corpus`, `just render`, and `just qc`. Run `just validate-products`
for ontology changes and append a validated history record for actual curation.
Test any hierarchy-rule change against the separate terrestrial source concept
as well as the reviewed target.

## Additional Notes

iModulonDB is not applicable: the record has no gene, regulator, organism, or
expression-dataset claim. Source node verification uses the committed GOLD
inventory, not an authenticated live GOLD query. No generated YAML, page,
status, or curation-history entry was edited by this review.
