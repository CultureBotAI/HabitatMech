# YAML Record Review: mangrove swamp

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/mangrove_swamp.yaml`
- Started UTC: 2026-10-03T17:27:45Z
- Finished UTC: 2026-10-03T17:29:58Z
- Verdict: needs curation

## Target

Read the entire generated `HabitatRecord`, `ENVO:00000057`, mangrove swamp,
AQUATIC, EXACT, REVIEWED. It merges GOLD node 4018 at Environmental > Aquatic
> Marine > Intertidal zone > Mangrove swamp with PREGO's same ontology ID.
`PATHS.tsv:462` pins the stem. ITEM REVIEW rows exist for both contributing
source concepts: `habitatmech:GOLD.79cfdb171a` at decisions row 723 and
`habitatmech:PREGO.5b0f9775b2` at row 1451. The two review events plus seed
event explain REVIEWED mechanically; that status does not settle parent or
synonym semantics.

## Validation

- `just validate data/habitats/aquatic/mangrove_swamp.yaml`: pass.
- `just validate-strict data/habitats/aquatic/mangrove_swamp.yaml`: one file,
  zero errors.
- Fresh full `just qc` was near the end of its test stage at review finish;
  lint, documentation and provenance had passed. Later corpus/history/site
  gates are not claimed complete here.
- Inspected the current official ENVO definition, all three ontology synonym
  predicates, direct parent and every API modal term. The full OWL was fetched
  and byte-verified this batch: SHA-256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- Fresh structured NCBI efetch returned taxon 405436 directly, species
  Micromonospora pattaloongensis, with no aliases and the same label as the
  record. No attached DOI/PMID or causal reference is present. Study
  memberships below are checked in the committed inventory, not live pages.
- Full OAK network validation is deferred to required CI for this reports-only
  change; its configuration does not check taxon labels or synonym scopes.

## Identity and Grounding

The identifier, canonical label and definition match
[official ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl).
The true direct parent is `ENVO:00000230` coastal wetland ecosystem, not a
class currently labelled simply swamp. It is present in
`ontology_terms.tsv:6819`. An ignored-inclusive record-ID search found no
standalone generated parent record; the valid ontology reference remains
usable. The complete maintained GOLD Intertidal zone parent was read.

The extra `habitatmech:GOLD.115edc36f8` parent comes from one source's path,
not the ontology. Importing it makes the entire merged mangrove-swamp class,
including PREGO, a subtype of that marine intertidal zone. Coastal ecosystem
identity is not the same assertion as occupying precisely the shore region
between tidal marks. The inspected
[NOAA estuarine-habitat account](https://oceanservice.noaa.gov/education/tutorial_estuaries/est06_habitats.html)
describes mangal zones with markedly different flooding regimes, including
upper portions rarely reached by tides. It does not justify constraining
every complete mangrove swamp to the strict intertidal extent. This is a
scope/context finding, not merely an absent ontology subclass edge.

Current ENVO types `MangroveForest` as related and `woodland` as broad; both
are emitted exact. `mangal` is genuinely exact and must stay so. PREGO's
independent related spellings must retain their source attribution.

## Evidence

`gold_ecosystem_paths.tsv:714` has one depth-five node and three ORGANISM
assertions. `prego_habitats.tsv:660` independently has one TAXON, one direct
assertion, maximum score 4 and the annotated-genomes/isolates channel. Both
generated attestations preserve their units. They do not sum to four taxa,
four isolates, or four characteristic organisms.

The sole PREGO association at `prego_habitat_taxa.tsv:3574` matches the record:
NCBITaxon:405436, current name, score 4, direct TRUE, rank 1 and pool 1.
No corroboration or `is_characteristic` is claimed. A one-member ranked pool
does not independently establish ecological preference or the species' full
distribution. The source channel is not a new strain-isolation claim.

Bulk biosample row 127 records 232 samples. API rows 548-550 describe 176
samples and two studies: broad mangrove biome (`ENVO:01000181`) has one term,
share 1.00 and two agreeing studies; local mangrove swamp has three terms,
share 0.98 and one agreeing study; medium sea water (`ENVO:00002149`) has
three terms, share 0.98 and one agreeing study. All current term meanings were
checked. Sea water is a sample material, not the ecosystem's identity, and
the dominant local term does not make every sample identical in scope.

Exact membership scans over all 4,587 study rows found seven accessions:
Gs0128957, Gs0144828, Gs0150243, Gs0150248, Gs0150263, Gs0150408 and
Gs0161797. The first spans 13 paths; shared study membership does not merge
the other habitats. Bulk/API/study inventories are distinct snapshots, not
quantities to add or force into agreement.

## Completeness

Ignored-inclusive ontology/source IDs, node, label, full path and stem searches
covered curation, raw inventories, PATHS, history, research and prior reports.
The two ITEM rows exist; no target authored definition, causal overlay,
dedicated session history or prior completed individual report was found.
The current ontology already provides a definition. New neighboring reports
mentioning the swamp are not previous individual reviews.

There is no requirement to add mechanisms, measured parameter bands or a
larger taxon list without evidence. iModulonDB is not applicable to this
observational species association without a molecular or expression claim.

## Findings

1. **Major M1: non-exact ontology synonyms emitted exact.** `MangroveForest`
   is related and `woodland` broad, while `mangal` is exact. Owners: governed
   ontology source/extraction contract and `seed.py:406-407`. Extend #1249's
   mixed-scope regression rather than globally changing all synonym types.
2. **Major M2: one source's geographic context constrains a merged ecosystem
   class.** The inherited marine Intertidal zone parent is not supported as
   a universal genus of mangrove swamp. Owner: exact-source parent controls
   consumed by `seed.py:898`, with reassessment of GOLD's scope in its ITEM
   decision if a source split is warranted. Preserve the independently
   supported coastal-wetland-ecosystem ontology parent and PREGO identity.

Blockers: 0. Major: 2. Minor: 0.

## Recommended Edits

Restore the actual related/broad synonym scopes while keeping exact `mangal`
and PREGO provenance. Remove the unjustified global source-parent contribution;
do not blanket-REPLACE true ontology ancestry. Reassess the GOLD path's degree
of narrowing before changing its exact mapping, and do not move PREGO's taxon
to a newly minted source without evidence. Retain all original source counts,
units, paths and audit provenance. Append a new history event only for actual
curation, never rewrite committed review events.

## Follow-up Checks

Canary the target, inspect every synonym scope and both parent contributions,
and test a mixed-source record so the GOLD path cannot rewrite PREGO's
ontology-wide identity. Run strict/OAK/history/provenance checks, exact corpus
reproduction, supported map/site regeneration and full QC. #1217/#1218 remain
independent regeneration dependencies and must not be bypassed.

## Additional Notes

The fresh all-state query covered 439 issues and comments and found no
mangrove-swamp hierarchy issue. #1249 already owns the synonym mechanism;
#1269 concerns the distinct sediment and soil records. The source habitat and
its material components are not interchangeable. No scientific input,
generated record, page or history was changed by this review.
