# YAML Record Review: Spring sediment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/spring_sediment.yaml`
- Started UTC: 2026-10-06T08:45:22Z
- Finished UTC: 2026-10-06T08:49:24Z
- Verdict: needs curation

## Target

Read the entire generated `HabitatRecord`: habitatmech:GOLD.883be78511,
Spring sediment, AQUATIC, UNGROUNDED, SEEDED. `PATHS.tsv:2303` pins the
stem. One GOLD source, node 5962, records Environmental > Aquatic > Deep
subsurface > Groundwater > Spring sediment and one ORGANISM assertion.
The sole parent is habitatmech:GOLD.22a80cbd14 Groundwater. There are two
historical events, but no definition, synonyms, xrefs, mapping predicate,
parameters, taxa, evidence or causal graphs. This is sediment associated
with a spring, not the spring landform, its water or the explicitly saline
spring-sediment sibling.

## Validation

- Fresh `just validate data/habitats/aquatic/spring_sediment.yaml`: passed.
- Fresh `just validate-strict data/habitats/aquatic/spring_sediment.yaml`:
  one file, zero errors.
- Actual full `build_corpus` / `build_document` equality passed: one source,
  zero reviewed sources, zero taxa and two history events.
- Actual resolution with the full normalized mapping table returned
  gold_unmatched, UNGROUNDED, own mint, no predicate, parent or xref.
  Applying the real CLASS decision returned
  curated_confirm_ungrounded_from_gold_unmatched, still reviewed=False.
- All 14 raw TSVs were scanned for the exact source path/node. The full
  generated page and actual semantic text were inspected; removing only
  the Groundwater parent changes that text.
- Scientific inputs/code and guidance remain unchanged at baseline
  e9f6174d9. Inspected [main QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37437077343)
  passed 463 tests, three skipped and two dependency warnings, all 90
  histories, zero schema errors and exact reproduction of 3,206 records,
  site, redirects, provenance and term requests. This is unchanged-input
  baseline reuse, not a fresh full QC invocation for this target. The
  preceding label gate passed with zero flagged pairs and 2,054 no-adapter
  skips; it cannot certify a missing minted definition.
- No evidence-reference validator applies without evidence/causal edges.
  Original organism/sample provenance was not recovered.

## Identity and Grounding

Minting from the entire path reproduces GOLD.883be78511. The maintained
`curation/decisions.tsv:803` row is CLASS-level CONFIRM_UNGROUNDED and
explicitly says habitat identity was not assessed. Its dated 2026-08-12
history and the 2026-08-16 seed event reproduce correctly. SEEDED does not
claim an ITEM assessment, despite the existence of a historical decision.

Ignored-inclusive inspection of the vendored ontology inventory and a
structured scan of labels/synonyms in the full typed official ENVO snapshot
found no spring-sediment candidate. Current exact ENVO searches for spring
sediment, sediment from a spring and spring deposits each returned zero
hits. This is a bounded search, not proof that every ontology lacks a term.

Current active [ENVO:00002007 sediment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002007)
defines a particulate environmental material formed by transport and
deposition in flowing liquid. It is a defensible genus, not exact identity
for every spring-qualified deposit. The spring class verified in the
preceding individual review denotes a landform, not its sediment.

The entire contextual parent `data/habitats/aquatic/groundwater.yaml` was
read. It retains GOLD.22a80cbd14 and the water-material genus
[ENVO:01001004 groundwater](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001004),
not a genus for particulate deposits. Its 249 ORGANISM count and two-node
collapse are not child evidence. `src/habitatmech/seed.py:898-907` adds
the parent independently from the source path. The deep-subsurface context
does not make sediment a kind of groundwater or prove an underground
location for every spring deposit.

No mapping predicate is emitted here. The retained-source narrow-match
endpoint finding in #1398 does not apply to this UNGROUNDED child merely
because it applies to its parent or to neighboring spring records.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:926` contains the exact depth-five path,
one node 5962, one organism and zero tree study/biosample counts. The full
14-inventory scan found no exact bulk-biosample, study, API-triad, parameter,
BacDive, PREGO, Madin or mapping-table contribution. Neither parent counts
nor independent literature samples may be added to that one organism.
The current GOLD path 5962 endpoint returned 404, not evidence that the
identifier is retired or the source assertion false.

The fresh structured PubMed abstract and metadata for
[Perreault et al. 2008](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=18805995&retmode=xml)
verify PMID 18805995 and DOI 10.1128/AEM.00359-08. The study reports
microbial isolates from spring waters and sediments at Gypsum Hill and
activity measurements in sediment slurries. This supports a real microbial
spring-sediment habitat and separates the material from water. Its saline,
cold Arctic setting is one example, not the definition of this unqualified
source. It does not identify the organism behind node 5962. Taxa, genes,
chemistry and metabolic observations must not become target-wide claims.
Fresh full-text inspection is not claimed.

A newer Baiyi Basin article was located as a lead, but its publisher page
returned HTTP 403; its search excerpt is not affirmative evidence in this
review. The batch's ignored-inclusive inventory of this repository and
the configured kg-microbe checkout found none of GOLD_nodes.tsv,
GOLD_edges.tsv, goldData.xlsx or gold_biosample_triads.tsv. Original
accession-level provenance remains unresolved beyond committed inputs.

## Completeness

Ignored-inclusive identifier, source node, label and stem searches covered
curation, history, research, configuration, docs, source, tests, reports,
raw inventories and path/retirement registries. The CLASS row, source row
and stable-path entry matched. No target authored definition, causal
overlay, dedicated research report, separate session-history entry,
retirement or earlier individual review was found. Other research reports'
mentions of spring sediment and the saline sibling review are context,
not target-specific curation.

A scoped definition and true material genus are consequential gaps: the
label is the only scientific description and the only parent is false.
Other empty optional fields are not defects. No gene/regulator/expression
claim makes iModulonDB applicable, and contextual paper genes are not
evidence for a habitat-wide causal graph.

## Findings

Zero blockers, two majors, zero minors:

1. **Major: missing ITEM identity ruling, material genus and definition.**
   The CLASS sweep did not assess this real habitat individually. The
   maintained owners are the exact row in `curation/decisions.tsv` and a
   keyed authored definition in `curation/term_requests.tsv`.
2. **Major: false groundwater-material superclass.** The only inherited
   parent is source context, not a strictly broader class. The maintained
   definition's explicit parent mode can correct this after an ITEM ruling;
   `src/habitatmech/seed.py` owns generation and definition application.

Extend [#1454](https://github.com/CultureBotAI/HabitatMech/issues/1454) with
this distinct, not-explicitly-saline source witness and bounded acceptance
criteria. Do not import the original issue's salinity qualifier or organism
provenance, or conflate this material defect with the outlet finding #1467.

## Recommended Edits

Replace the CLASS-only ruling with evidence-backed ITEM
CONFIRM_UNGROUNDED, preserving the mint. For the authored-definition route,
leave the decision's optional placement empty and define the spring-
qualified material with ENVO:00002007 sediment as genus in
`curation/term_requests.tsv`. Document why the sole inherited Groundwater
parent is false and use `parent_mode=REPLACE` to replace it with the genus.
Do not first add a true parent and then claim every inherited parent was
false. The actual REPLACE implementation resets the entire parent set.

Keep grounding UNGROUNDED: `src/habitatmech/curate/definitions.py` rejects
NARROW or ontology-owned definition targets. GROUND_AS_PARENT plus a novel
definition is not a valid combination. Do not ground exactly to sediment,
spring or groundwater. Scope the definition to the spring-associated
deposit, without invented salinity, temperature, depth or pore-water rules.

Preserve AQUATIC category, exact node/path, one ORGANISM count/unit, stable
stem and old historical events. Recover original sample metadata separately
before point-level ecology. Never repair generated YAML/pages directly.

## Follow-up Checks

Add exact-source controls for preserved identity/count/unit/history,
ITEM-reviewed status, accepted scoped definition, true sediment genus and
removed Groundwater parent. Check the saline sibling separately and retain
valid groundwater-material children as controls. Append required new
history, dry-seed and inspect the guarded canary before wider regeneration;
do not prune a partial run. Run schema/strict, labels, provenance, history,
exact reproduction, site/redirect, term-request and full QC gates.

The actual semantic builder loses broader habitat: Groundwater when the
false parent is removed. Adding a definition/genus also requires a genuine
map/site refresh under #1217; keep #1218/runtime pins isolated. The page's
class-level disclaimer is correct, but it faithfully exposes the same
unsupported broader-habitat link. No scientific input or page changed in
this review. Actual SSSOM/KGX products/current kg-microbe compatibility
were not audited.

## Additional Notes

All 630 open/closed issue titles/bodies were searched for the exact key,
node and record path: no exact witness matched. Related titles included
#1454, #1489 and #1491; #1454's complete body and comments (none) directly
own the linked definition/groundwater mechanism. Comments on every issue
were not exhaustively searched. Report publication is not implementation
or closure of the scientific findings.

Inspected official ENVO OWL snapshot SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
