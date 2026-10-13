# YAML Record Review: periphytic biofilm

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/periphytic_biofilm.yaml`
- Started UTC: 2026-10-04T22:48:42Z
- Finished UTC: 2026-10-04T22:51:04Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord ENVO:03605000, periphytic biofilm,
AQUATIC/CLOSE/REVIEWED. It contains an ENVO definition/source, one ENVO
synonym, two parents, one GOLD attestation with one ORGANISM assertion,
and two history events. Taxa, parameters, xrefs, evidence, graphs, discussions
and datasets are absent. PATHS.tsv:950 pins the stem.

The exact source is Environmental > Aquatic > Freshwater > River > Periphyton,
minted as habitatmech:GOLD.9b43111989. The film is not the river itself,
an individual alga, drifting plankton or an arbitrarily chosen substrate.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/periphytic_biofilm.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/periphytic_biofilm.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared batch PASS: 1,179 canonical, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | Shared PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Active in final corpus reporting; tests passed, 457 passed/three skipped/two warnings in 526.74 seconds. No terminal whole-run result claimed. |
| Source/reference checks | Entire target, actual child/parent routes and full-field reproduction, all 14 raw tables, current typed ENVO/OLS and GOLD, original study attempt, institutional source text, whole page and full semantic comparisons. |

Full construction reproduces all fields with one source and one reviewed
source. History, strict corpus, overlays, floor, exact reproduction, site,
redirect and term-request stages have passed in the shared run; its final
completion belongs in a later receipt, not a backdated report observation.

## Identity and Grounding

Actual default resolution uses gold_leaf_synonym, adopting ENVO:03605000
with CLOSE/skos:closeMatch. ITEM REVIEW at curation/decisions.tsv:1695,
dated 2026-08-16, endorses that result without upgrading the relation;
the actual route is curated_review_of_gold_leaf_synonym. REVIEWED and the
two events faithfully reflect one reviewed source. Conservatively retaining
CLOSE is not a separate defect or a reason to force exactness in this audit.

Current [GOLD node 5345](https://www.ebi.ac.uk/ols4/api/ontologies/gold/terms/https%253A%252F%252Fw3id.org%252Fgold.path%252F5345)
is active for the exact path. It supplies aquatic-biome broad, river local
and periphytic-biofilm medium annotations, marked complete, plus an explicit
exact match to ENVO:03605000. This supports the selected biofilm meaning;
it does not turn the river setting into a strict genus or create missing
historical triad sample rows.

Current [ENVO:03605000](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03605000)
is active and agrees with the inherited label/definition. Its named superclass
is ENVO:01000156 biofilm material, and its comment locates the film on
submerged surfaces. The committed term and subclass are at physical
ontology_terms.tsv:10131 and ontology_subclass_edges.tsv:8530. Preserve
that supported genus rather than substitute the waterbody or a whole taxon.

Typed official OWL marks Periphyton as hasRelatedSynonym, not hasExactSynonym.
The generated synonym claims EXACT_SYNONYM with source ENVO. This is the
shared #1249 scope-inflation defect: the untyped pipe at ontology_terms.tsv
loses relation scope, and ConceptStore.get at seed.py:406-407 labels each
imported spelling exact. OLS's flattened synonym list alone cannot settle scope.

There is an important provenance distinction. GOLD independently uses
Periphyton as its source label; seed.py:870 adds a GOLD exact-label synonym,
but add_synonym's (text,type) setdefault currently retains the earlier ENVO
attribution. Correcting the ENVO scope must not erase the source spelling
or imply that no independent GOLD lexical assertion exists. Preserve typed
source assertions separately rather than globally downgrading every spelling.

The second parent, ENVO:01000297 freshwater river, comes independently from
the GOLD parent-path pass at seed.py:898-907. Actual immediate River source
resolution mints habitatmech:GOLD.b9a8cb85e1, then gold_composed_label maps
EXACT to freshwater river without a decision. Current ENVO defines a river
containing flowing fresh water, not a periphytic film. Source nesting states
where this film occurs, not that a film is a kind of river.

## Evidence

Physical gold_ecosystem_paths.tsv:939 gives depth five, one node 5345,
one organism and zero study/biosample counters in that tree inventory.
The attestation is faithful. gold_path_biosamples.tsv:648 separately gives
nine bulk samples; these must not replace the one ORGANISM count.

gold_studies.tsv:2229 names Gs0140997 with this exact path only. Its original
study page returned 403. The complete exact-path/source-ID scan of all 14 raw
tables found no committed triad row, other source, named taxon or environmental-
parameter contribution for this target. Current GOLD's annotation roles are
not evidence of nine complete API triads or an invented one-study sample crosswalk.

The inspected [EPA account](https://www.epa.gov/national-aquatic-resource-surveys/indicators-sediment-diatoms)
describes periphyton as mixed material attached to submerged surfaces.
The [USGS sampling protocol](https://water.usgs.gov/nawqa/protocols/OFR-93-409/algp7.html)
distinguishes attached or associated periphyton on rocks, wood, plants and
sediment within stream habitats. These support the film-versus-river distinction,
not a particular substrate, community member or experiment for GOLD 5345.

The full rendered page faithfully reproduces both the false river parent
and incorrectly ENVO-exact synonym. Its display is propagation, not additional
scientific evidence. The single organism assertion does not identify a
characteristic taxon, and the record makes no causal or numerical claims to fill.

## Completeness

Ignored-inclusive ontology ID, minted key, path, label/stem and filename
searches covered curation, conf, history, research, reports, raw inventories,
PATHS and RETIRED. They found the decision and expected source/ontology rows,
plus contextual mentions in unrelated plant, plankton and engineered-film
research. No target-owned definition request, overlay, dedicated research,
session history, retirement or previous individual review was located.

Those neighboring reports are leads, not evidence to import their taxa or
mechanisms here. The ENVO definition already supplies identity text; a novel
term request is unnecessary for these two repairs. Empty optional fields
remain appropriate. iModulonDB is inapplicable without gene/regulator/
expression assertions.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | GOLD context promotes freshwater river to a strict parent of periphytic biofilm. | Governed exact-source parent control and src/habitatmech/seed.py:898-907. |
| Major | The ENVO-related Periphyton synonym is emitted with ENVO exact scope. | Governed ontology extraction/synonym representation and seed.py:406-407 under #1249. |

Counts: zero blockers, two major, zero minor. Neither finding requires
discarding the supported biofilm identity or forcing the current CLOSE mapping
to exact. No retained-minted endpoint-contract witness is diagnosed here.

## Recommended Edits

1. Suppress only the exact source's ENVO:01000297 parent contribution, keeping
   ENVO:01000156, the full river source path, one ORGANISM assertion and history.
2. Extend #1249's typed-synonym repair to this ENVO hasRelatedSynonym witness.
   Preserve independent GOLD label provenance, known exact scopes and the
   spelling itself; do not manually patch generated synonyms or raw checksums.
3. Add source-parent-retention and typed-synonym/provenance regressions, append
   required new history, and regenerate through maintained inputs and guarded
   writers. Original-study evidence is needed for any stronger ecological claim.

## Follow-up Checks

Dry seed, inspect `just seed-canary ENVO:03605000 --force`, then guarded full
regeneration without partial prune. Run ordinary/strict/products/history/
provenance checks, exact reproduction and all site/redirect/term-request/QC gates.

Actual full-context removal of the river parent changes semantic text and
requires genuine map/site rebuilding under #1217. Changing only ENVO synonym
scope is neutral; an illustrative typed ENVO-related entry plus independent
GOLD-exact entry is also neutral because the spelling is unchanged. Those
in-memory probes made no corpus changes. Preserve protected #1218/runtime
pins and inspect actual SSSOM/KGX before compatibility claims.

## Additional Notes

All-state exact-ID/key/periphyton searches returned no target issue; the full
existing #1249 body owns the shared synonym mechanism. The false river-parent
edge is a separate scientific finding. Official typed ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated output, old report/history, paid research or
GitHub item changed during this individual review.
