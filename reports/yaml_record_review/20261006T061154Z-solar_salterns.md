# YAML Record Review: Marine Solar Salterns

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/solar_salterns.yaml`
- Started UTC: 2026-10-06T06:07:45Z
- Finished UTC: 2026-10-06T06:11:54Z
- Verdict: needs curation

## Target

Read the complete generated `HabitatRecord`: `habitatmech:GOLD.67571e7dc1`,
Solar salterns, AQUATIC, UNGROUNDED, SEEDED; pinned at `PATHS.tsv:2036`.
The exact source is `Environmental > Aquatic > Marine > Intertidal zone > Solar salterns`,
node `gold.ecosystem:8054`. There is one parent, one 157-ORGANISM
attestation and two history events. No definition, taxa, parameters,
mapping predicate, evidence items or causal graph is asserted.
The target is the whole source concept, not salt-pond sediment, a single
crystallizer pond, its brine, or the separately pinned Solar solterns source.

## Validation

- Fresh `just validate data/habitats/aquatic/solar_salterns.yaml`: passed.
- Fresh `just validate-strict data/habitats/aquatic/solar_salterns.yaml`:
  one file, zero errors.
- Actual full `build_corpus` / `build_document` equality passed: one source,
  zero reviewed sources, zero taxa, two history events.
- Complete normalized mapping-table execution verified default/applied
  child and parent routes. All 14 raw TSVs were parsed for exact source/path
  membership. The complete rendered page and actual semantic text were read.
- Current OLS and typed official ENVO verified saline evaporation pond,
  intertidal zone and aquatic environment. The correctly formed current GOLD
  path-IRI lookup returned 404; source retirement is not established.
- Unchanged-input baseline: preceding full local QC passed 463 tests,
  three skipped, two dependency warnings and all gates. Actual inspected
  [merge-group QC at base 5cfb086a6](https://github.com/CultureBotAI/HabitatMech/actions/runs/37418137551)
  passed the same test counts, all 90 histories, exact reproduction of all
  3,206 records and a consistent site. Required labels and vendored checks
  passed. This is baseline reuse, not another local full-QC run for this
  individual record. No separate reference validator applies without
  evidence items or causal edges.

## Identity and Grounding

The exact path reproduces the retained mint. Actual default resolution is
gold_unmatched, UNGROUNDED, no predicate or extra parent. The CLASS
CONFIRM_UNGROUNDED row at `curation/decisions.tsv:615` returns
`curated_confirm_ungrounded_from_gold_unmatched`, still reviewed=False.
SEEDED and the CLASS decision plus seed event are faithful; the rendered
page explicitly says this was not an individual judgement. A lexical
negative is not a reviewed global proof that no ontology concept fits.

The sole parent is independently added by `seed.py:898-907`.
`Environmental > Aquatic > Marine > Intertidal zone` mints
`habitatmech:GOLD.115edc36f8`; actual default and applied parent resolution
take gold_narrower_than_leaf_match with ENVO:00000316 as the extra parent
and no ITEM override. The entire parent record was read: it is
NARROW/SEEDED with 77 ORGANISM assertions, two collapsed nodes and one
event. Neither its counts nor its mapping predicate belong to this child.

Current typed [intertidal zone](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000316)
denotes the shore/seabed area between tide marks. A managed salt-production
pond or connected pond system is not a subtype of that geographic zone
merely because GOLD groups it there. Location, seawater origin and
managed evaporative flow do not establish tidal exposure as its genus.
The parent's own outgoing waterbody edge is a separate defect; repairing
that ancestor would not justify this child-to-zone edge.

[Saline evaporation pond](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000055)
is a shallow artificial pond designed to produce salt from seawater.
Typed OWL makes saltern a RELATED synonym, not EXACT. Salt evaporation
pond is EXACT; lake is BROAD. Do not flatten those scopes or merge this
whole source automatically into ENVO:00000055. A saltern can encompass
multiple ponds, and the committed source lacks a sample-level scope ruling.
The current ENVO query for solar saltern returned zero results, while the
local candidate search recovered ENVO:00000055; the query miss is not a
global ontology-absence claim. [Aquatic environment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000317)
is a defensible broad candidate for a future explicitly bounded multi-pond
environment definition, not an automatic exact identity.

AQUATIC follows the source context and is not itself a finding. The fact
that the system is operated does not authorize a file move, category change,
or a claim that it denotes the salt-manufacturing procedure rather than a
microbial habitat.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:145` is the only exact-path contribution
recovered across all 14 raw TSVs. It supplies depth five, one node 8054,
157 organisms and zero tree-derived study/biosample counts. No exact bulk
biosample, sample triad, study membership, parameter, BacDive, PREGO, Madin
or mapping row was found. The attestation faithfully says 157 ORGANISM;
these are not 157 identified taxa or water samples. Do not borrow cohorts
from Salt pond, Salt pond sediment, or non-marine crystallizer sources.

The correct [current GOLD path lookup](https://www.ebi.ac.uk/ols4/api/ontologies/gold/terms/https%253A%252F%252Fw3id.org%252Fgold.path%252F8054)
returned 404. This does not prove retirement or erase the committed path.
The ignored-inclusive original-dump inventory under the configured
kg-microbe checkout found no GOLD node/edge TSVs; original membership and
input hashes were not reconstructed. Committed inventory reproduction is
the verified provenance boundary.

The inspected primary [Dillon et al. 2013 study](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2013.00399/full),
DOI 10.3389/fmicb.2013.00399, describes pumped flow through interconnected
ponds at the ESSA saltworks and samples three individual ponds, including
a crystallizer, in February 2006. Its abstract, introduction and sampling
methods support the system/pond distinction and real microbial habitat
status. They do not identify the 157 GOLD organisms or justify importing
study-specific taxa, salinity values or mechanisms into this entire source.

[Oren 2009, DOI 10.3354/ame01297](https://cris.huji.ac.il/en/publications/saltern-evaporation-ponds-as-model-systems-for-the-study-of-prima/)
was verified in the author's institutional publication record and abstract.
It likewise explicitly concerns multi-pond solar salterns and a salinity
sequence. The direct publisher PDF fetch failed; full-paper inspection is
not claimed. Neither paper is a recovered GOLD source crosswalk.

## Completeness

Ignored-inclusive identifier, source-path, node, label and stem searches
covered curation, history, research, configuration, docs, source, tests,
registries and prior reports. The CLASS row exists; no exact target
definition, causal overlay, session-history record or earlier individual
review was recovered. Parent research and related pond reviews are leads,
not inherited evidence or authority for merging distinct records.

Habitat-hood is positively supported, but source-specific pond-versus-complex
scope still needs an ITEM decision. The existing class-sweep backlog #108
already names Solar salterns. Honest SEEDED status and optional empty fields
are not counted as additional defects solely for lacking curation.
No gene, regulator or expression dataset is asserted; iModulonDB is not
applicable and its absence is not biological evidence.

## Findings

1. **Major: source-path intertidal context is emitted as the only strict
   superclass of the saltern.** `src/habitatmech/seed.py:898-907` promotes
   the exact source-to-parent-path edge to habitatmech:GOLD.115edc36f8.
   Neither an operated pond nor the multi-pond system is made a type of
   geographic intertidal zone by this classification context. Maintained
   source-specific hierarchy controls and the source's future ITEM scope
   decision own the repair. Extend
   [#1446](https://github.com/CultureBotAI/HabitatMech/issues/1446)
   with this distinct source witness, without merging it into that issue's
   existing ENVO:00000055 pond record.

Zero blockers, one major, zero minors. There is no current mapping-predicate
endpoint finding for this child: its predicate is absent. Do not transfer
the parent's NARROW/narrowMatch defect or count this as another #1398 case.

## Recommended Edits

Resolve the exact source's pond-versus-complex scope from original metadata
before selecting an ITEM grounding or authored definition. Preserve the mint
unless exact equivalence is established; a related synonym is insufficient.
For a justified minted multi-pond definition, use maintained
`curation/decisions.tsv` and `curation/term_requests.tsv` with a defensible
environment genus. Do not equate the whole system with its hypersaline
water, sediment, microbial mat or one crystallizer.

Suppress only the unsupported source-zone parent through maintained controls.
If retaining UNGROUNDED for an authored definition, explicitly record why
the sole inherited parent is false before using parent_mode=REPLACE; do not
use it as a blanket bypass. Exact/NARROW ontology grounding is a separate
decision route, not permission to attach an incompatible authored definition.
Preserve path/node, category/stem, 157 ORGANISM, absent predicate, and old
history; derive REVIEWED only from a genuine ITEM decision.

## Follow-up Checks

Regress the exact source-parent contribution, pond-versus-complex boundary,
true-genus retention and source/count/history preservation. Run dry seed,
guarded forced canary, append-only curation history, schema/strict, labels,
provenance, corpus, term-request, site/redirect and full QC gates for a fix.

The full rendered page publishes the unsupported Broader habitats entry.
Actual full-context removal of the sole zone parent changes semantic text,
so a real hierarchy/definition correction needs the genuine #1217 map/site
refresh. A predicate-removal probe is merely a no-op here because no
predicate exists; it is not an export or mapping-contract test. Preserve
protected draft #1218 and runtime pins. SSSOM/KGX products and current
kg-microbe consumers were not executed or certified by this review.

## Additional Notes

All-state pagination searched 629 issue bodies/titles. Full #1446 and #1465
bodies and their empty comment lists were read, plus #108's body. #1446
owns the same intertidal-parent mechanism for a different whole pond;
#1465 concerns soil/sediment uncertainty and is not this source's identity
repair. No exact key/node witness was present. #108's historical cohort
counts were not reused as current corpus statistics. Scientific issues
remain open after report publication. Typed official ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
