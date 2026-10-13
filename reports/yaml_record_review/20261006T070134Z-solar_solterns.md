# YAML Record Review: Solar solterns

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/solar_solterns.yaml`
- Started UTC: 2026-10-06T06:53:54Z
- Finished UTC: 2026-10-06T07:01:34Z
- Verdict: pass with minor issues

## Target

Read the complete generated `HabitatRecord`: `habitatmech:GOLD.cb4b2d7af4`,
Solar solterns, AQUATIC, UNGROUNDED, SEEDED. `PATHS.tsv:2782` pins its
stem. Its single source is GOLD node `gold.ecosystem:7928`, representing
nodes 7928 and 7929 on the identical path
`Environmental > Aquatic > Non-marine Saline and Alkaline > Solar solterns`.
The record has one parent, 30 ORGANISM assertions and two history events;
no definition, taxa, parameters, mapping predicate, evidence items or graph.
This is the inland-bin saltern source, not the separately pinned marine
Solar salterns record or either source's sediment child.

## Validation

- Fresh `just validate data/habitats/aquatic/solar_solterns.yaml`: passed.
- Fresh `just validate-strict data/habitats/aquatic/solar_solterns.yaml`:
  one file, zero errors.
- Actual full `build_corpus` / `build_document` equality passed: one source,
  zero reviewed sources, zero taxa and two historical events.
- Actual child and parent routes used the complete normalized mapping table.
  All 14 raw TSVs were parsed for exact source/path membership. The complete
  rendered page and actual semantic text were inspected.
- Current OLS and typed official ENVO verified three candidate classes.
  Correctly formed current GOLD path lookups for both source nodes returned
  404, which does not establish retirement.
- Unchanged-input baseline: the preceding publication's local full QC passed
  463 tests, three skipped, two dependency warnings and all gates. Inspected
  [merge-group QC at base 752bbaafd](https://github.com/CultureBotAI/HabitatMech/actions/runs/37424165465)
  independently passed those counts, all 90 histories, closed validation
  and exact reproduction of 3,206 records, site and redirect checks.
  Required labels/vendor checks passed; labels reported zero flagged pairs
  and 2,054 SKIPPED_NO_ADAPTER entries, not universal ontology coverage.
  This is explicit baseline reuse, not fresh full QC per target.
- No separate reference validator applies without evidence items or causal
  edges. Original GOLD organism membership and input hashes were not recovered.

## Identity and Grounding

The full path reproduces the mint. Default resolution is gold_unmatched
with no predicate or extra parents. CLASS CONFIRM_UNGROUNDED at
`curation/decisions.tsv:1125` changes the route to
`curated_confirm_ungrounded_from_gold_unmatched`, still reviewed=False.
The generated history and page faithfully distinguish the lexical CLASS
sweep from individual assessment. That sweep is not global ontology absence.

The sole parent is `habitatmech:GOLD.ce244e62cd`, inland saline or alkaline
aquatic environment. Its complete record was read: AQUATIC, UNGROUNDED,
REVIEWED, with an authored inland-water-body definition, ENVO:01000317 parent,
121 GOLD ORGANISM assertions from three nodes, 37 BacDive STRAIN assertions,
25 selected taxa and four history entries. None of those counts or taxa
transfers to this target. Its ITEM decision at `curation/decisions.tsv:1597`,
BacDive SAME_AS row at 1600 and REPLACE definition at
`curation/term_requests.tsv:43` reproduce the parent's current state.
Actual parent resolution is curated_confirm_ungrounded_from_gold_unmatched,
reviewed=True, with ENVO:01000317 as an extra parent. The child-to-parent
edge independently comes from `src/habitatmech/seed.py:898-907`.

Current [saline evaporation pond](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000055)
has an explicit seawater-fed salt-production definition. Related saltern
synonymy is not exact equivalence for an unspecified multi-pond complex or
groundwater-fed inland source. [Artificial pond](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03600092)
does not impose that feed-water restriction, but still denotes a pond.
[Aquatic environment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000317)
is a candidate broader genus if ITEM evidence supports an associated
environment or bounded saltern system. None is established here as exact identity.

The source's individual-pond versus multi-pond-system scope is unresolved.
Inland solar salterns exist; seawater-derived salts or thalassohaline
chemistry alone do not prove a coastal location. Thus the inland parent is
not demonstrably false from the recovered source data. Do not turn generic
coastal-saltern descriptions into a finding against these two GOLD nodes.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:353` is the only exact-path row recovered
across all 14 raw TSVs: depth four, nodes 7928|7929, 30 organisms and zero
tree-derived study/biosample counts. The collapse note and count/unit agree.
These are not 30 identified taxa, samples or independent studies. No exact
bulk-biosample, API-triad, aggregate-study, parameter, BacDive, PREGO, Madin
or mapping-table contribution was recovered.

Correctly formed current GOLD lookups for
[7928](https://www.ebi.ac.uk/ols4/api/ontologies/gold/terms/https%253A%252F%252Fw3id.org%252Fgold.path%252F7928)
and [7929](https://www.ebi.ac.uk/ols4/api/ontologies/gold/terms/https%253A%252F%252Fw3id.org%252Fgold.path%252F7929)
returned 404. Ignored-inclusive inventories in this goal turn covered this
repository and the configured kg-microbe checkout: no original GOLD node/edge
TSVs, `goldData.xlsx` or `gold_biosample_triads.tsv` were found. Committed
inventory reproduction is the verified provenance boundary, not a recovered
original organism roster or present-day source replacement.

The inspected publisher full text of [Zafrilla et al. 2010](https://link.springer.com/article/10.1186/1746-1448-6-10),
DOI 10.1186/1746-1448-6-10, describes inland salterns in Alto Vinalopo, Spain,
using multiple shallow artificial ponds and groundwater interacting with
salt deposits. The site description, hydrochemistry and collection methods
support inland salterns as microbial habitats and distinguish inland location
from marine-origin salts. They also illustrate the pond/system boundary.
They do not identify GOLD nodes 7928/7929 or the 30 organisms, establish this
source's exact genus, or authorize transferring site taxa or measurements.
The publisher text was accessible; the separate PMC endpoint returned a
CAPTCHA and was not treated as inspected full text.

Publisher metadata and abstract for [Perez-Davo et al. 2014](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.059121-0),
DOI 10.1099/ijs.0.059121-0, independently describe an isolate from sediment
at an inland solar saltern in La Malaha. This supports the habitat usage
and standard spelling, not the target cohort. Strain growth ranges are not
habitat environmental-parameter bounds.

## Completeness

Ignored-inclusive key/node/label/stem searches covered curation, history,
research, configuration, docs, source, tests, reports, path/retirement
registries and redirect retractions. The CLASS row, registry, parent
research and contextual earlier reviews matched; no target-owned ITEM
decision, definition, causal overlay, session-history record, retirement
entry or prior individual review was found. Current ENVO searches for
solar solterns and solar salterns returned zero results: bounded lexical
results, not a proof that no useful class exists.

Relevant parent research passages suggest all solar salterns are coastal.
That is an untrusted lead, not a node-specific membership crosswalk; the
inspected inland primary evidence prevents using the generalization to
delete this parent. The full earlier review of the sediment child
GOLD.a9d2df6ba5 was read for context, not counted as a new child review.
Its mapping-endpoint finding does not transfer to this predicate-free target.

An ITEM definition could resolve scope, but SEEDED status and empty optional
fields are honest, not separate required-content failures. No gene,
regulator or expression claim makes iModulonDB applicable.

## Findings

1. **Minor: the canonical display label retains the source spelling
   "Solar solterns" instead of "Solar salterns".** Both inspected primary
   publications use saltern. This is a non-blocking wording defect, not a
   wrong biological identity. The raw/source label and source path must stay
   verbatim. The existing maintained authored-label route is
   `curation/term_requests.tsv`, applied by `src/habitatmech/seed.py:422-465`,
   alongside a justified ITEM assessment in `curation/decisions.tsv`.

Zero blockers, zero majors, one minor. Pond/system scope and exact genus
remain unresolved; there is no proven false-inland-parent or mapping-predicate
finding for this record.

## Recommended Edits

During bounded ITEM curation, use canonical display label Solar salterns
while preserving mint, pinned stem, both raw node identities, source path,
source_label, 30 ORGANISM and historical events. A supported minted definition
can use the existing authored-label path. Do not invent a definition or an
exact ontology identity merely to correct spelling, and do not globally
normalize raw GOLD labels or paths.

Resolve source scope before selecting a genus or changing parents. Do not
remove the inland parent based on marine-origin salt alone. Do not borrow
the sediment child's 12 organisms, the other Solar salterns source's 157,
or the parent record's counts/taxa. Generated YAML/pages remain read-only.

## Follow-up Checks

An in-memory label-only counterfactual using the actual full corpus label
context changed semantic text for exactly two records: this target and
`data/habitats/aquatic/sediment__58c2d02d.yaml`, whose broader-habitat text
uses this label. Source attestations stayed identical. The target page URL
changes from `solar-solterns-habitatmech-gold-cb4b2d7af4.html` to
`solar-salterns-habitatmech-gold-cb4b2d7af4.html`; the child page URL is stable.

Regress exact canonical/source-label separation, stable mint/path/stem,
child parent-label resolution and 30 ORGANISM preservation. A real curation
change needs dry seed, an inspected guarded canary, curation history,
schema/strict, labels, provenance, corpus, term-request and full QC gates.
Commit the regenerated correction, then run the history-aware redirect and
render pass so the old published URL is preserved. Refresh genuine #1217
map/site products for both changed semantic inputs while leaving protected
draft #1218 and runtime pins untouched. A predicate-omission probe was a
no-op because the field is absent, not an export test. Actual SSSOM/KGX
products and current kg-microbe consumers were not audited.

## Additional Notes

All-state pagination searched 629 issue bodies/titles. Exact scans found
no cb4b2d7af4, node 7928/7929 or solar-soltern spelling witness. The full
broader CLASS-assessment issue #108 and its comment were checked; they do
not own this exact canonical-label correction. Comments on every other
issue were not exhaustively searched. A bounded label issue is appropriate
after publication-time deduplication; this review makes no GitHub mutation.

Typed official ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
