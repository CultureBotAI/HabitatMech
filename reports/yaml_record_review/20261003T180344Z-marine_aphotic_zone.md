# YAML Record Review: marine aphotic zone

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_aphotic_zone.yaml`
- Started UTC: 2026-10-03T18:01:56Z
- Finished UTC: 2026-10-03T18:03:44Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord, `ENVO:00000210`, marine aphotic zone,
AQUATIC, EXACT, REVIEWED. It merges GOLD node `gold.ecosystem:4010`, source
key `habitatmech:GOLD.de5b5dffd1`, with PREGO source key
`habitatmech:PREGO.228ab72fbd`. `PATHS.tsv:522` pins the stem.

## Validation

- `just validate data/habitats/aquatic/marine_aphotic_zone.yaml`: pass.
- `just validate-strict data/habitats/aquatic/marine_aphotic_zone.yaml`: one
  file, zero errors.
- Fresh full `just qc` remained active at review finish. Lint, documentation
  and raw provenance passed; tests were running. Later corpus, history and
  site gates are not claimed complete.
- Inspected current official ENVO OWL, retrieved and byte-verified this batch,
  SHA-256 `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- All 13 displayed NCBITaxon IDs resolved directly in fresh NCBI efetch;
  scientific names matched exactly and no alias redirects were returned.
- OAK identity validation is deferred to required CI for this reports-only
  change. Its configured exclusions include taxon labels and synonym scopes.

## Identity and Grounding

Identifier, canonical label, full definition and genuinely exact
`AphoticZone` synonym agree with
[official ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl)
and `ontology_terms.tsv:6800`. Both source decisions are ITEM-level:
`decisions.tsv:1228` grounds GOLD and `:1415` reviews PREGO. REVIEWED follows
from those decisions, not from this report. The freshwater-lake Aphotic zone
is a distinct source, not an additional attestation to import here.

`ENVO:01000295` marine layer is the true ontology parent. Its full definition
and restrictions were inspected; `ontology_terms.tsv:7798` and
`ontology_subclass_edges.tsv:4843` preserve this edge. An ignored-inclusive
root-ID search found no separate generated marine-layer record; a valid
ontology reference does not require one.

The added `ENVO:00000207` oceanic-zone parent comes from GOLD's Oceanic path,
not the target's ontology superclass edge. Its current definition explicitly
excludes water above a continental shelf (`ontology_terms.tsv:6797`). Read the
entire maintained `oceanic_zone.yaml` for that contextual meaning, not as a
second completed review. The generic ENVO/PREGO aphotic class does not impose
the same horizontal restriction.

The [British Antarctic Survey's research account](https://www.bas.ac.uk/news/new-antarctic-seabed-sonar-images-reveal-clues-to-sea-level-rise/)
states that Antarctic continental shelves can reach 1,600 m. Therefore, as an
inference from that observation and the inspected class meanings, depth below
200 m does not entail an off-shelf location. Even a below-1,000-m convention
does not establish that universal implication. A GOLD source's oceanic context
must not become a global is-a constraint on the merged ontology/PREGO class.

There is also a terminology difference to preserve, not silently fix:
[NOAA's light-zone account](https://oceanservice.noaa.gov/facts/light_travel.html)
separates dysphotic 200-1,000 m from aphotic below 1,000 m; ENVO uses the
below-200-m, insufficient-for-photosynthesis convention. The YAML accurately
quotes ENVO. This disagreement is not counted as a separate transcription or
grounding defect, and does not authorize changing an ontology definition
locally or asserting zero light throughout its entire current extent.

## Evidence

`gold_ecosystem_paths.tsv:155` verifies the full Marine > Oceanic > Aphotic
zone path, depth five, one node and 146 ORGANISM assertions.
`gold_path_biosamples.tsv:315` has 64 biosamples. API triads at
`gold_path_triads.tsv:608-610` also cover 64 samples and nine studies: broad-scale marine biome
`ENVO:00000447` leads three terms at 0.95 share with seven agreeing studies;
local marine aphotic zone leads four at 0.92 with five; medium sea water
`ENVO:00002149` leads two at 0.97 with eight. All top-term meanings were
checked in current OWL. Material, local zone and biome roles remain distinct;
three slots do not mean 27 independent studies.

Structured exact-path membership across all 4,587 study rows found nine:
Gs0045617, Gs0046785, Gs0056617, Gs0111355, Gs0111419, Gs0114420,
Gs0121717, Gs0141999 and Gs0145045. Mixed-path studies do not make their
other habitats equivalent. These are verified committed snapshot memberships,
not claims to have independently reviewed each live study page.

`prego_habitats.tsv:322` supplies 13 distinct taxa, 13 direct assertions,
score 4 and the annotated-genomes/isolates channel. All 13 retained rows at
`prego_habitat_taxa.tsv:4290-4302` were checked against the YAML: identifiers,
labels, score, ranks 1-13, pool 13, direct flags and absent corroboration agree.
The full candidate pool is displayed. Current
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/taxonomy) confirmed every name;
none is marked characteristic. These associations remain PREGO's observations,
not independent evidence for the GOLD habitat's exact horizontal extent.

The GOLD exact source label, ENVO exact synonym and three PREGO related
aliases preserve distinct provenance. There is no synonym-scope finding here.

## Completeness

Ignored-inclusive searches covered identifiers, both source keys, labels,
stem and source path in curation, raw inventories, PATHS, history, research
and individual reports. Both ITEM decisions were found; no target authored
definition, overlay, dedicated session history or earlier individual target
review was found. The earlier freshwater-aphotic review and plankton research
mention this source for comparison, not as authoritative target curation.

Do not fill optional measurements or mechanism graphs from triad summaries.
iModulonDB is not applicable to the current observational taxon associations;
there is no gene, regulator or expression-dataset claim.

## Findings

- **Major M1: source-only oceanic restriction imposed on the generic aphotic
  class.** `ENVO:00000207` is not established as strictly broader than the
  entire `ENVO:00000210` class. Owners: GOLD parent-link generation in
  `src/habitatmech/seed.py:898-909` and the source decision in
  `curation/decisions.tsv:1228`. Preserve the valid marine-layer superclass.
- Blockers: 0. Major: 1. Minor: 0.

## Recommended Edits

Reassess the GOLD source's exact-versus-narrow scope and prevent its off-shelf
constraint from leaking into generic ENVO/PREGO ancestry. A scoped exclusion
of the source parent is preferable to blanket parent replacement when keeping
the current identity; if an independently supported narrower GOLD concept is
needed, preserve PREGO identity and all 13 taxa on the generic class. Do not
automatically split identities from this report alone. No REPLACE of both
parents, manual YAML patch, or opportunistic rewrite of ENVO's depth wording.

## Follow-up Checks

Add regression coverage for the invalid source parent and retained marine
layer, with source counts and association ownership unchanged. Canary the
record; append history with the actual future change; check provenance,
schema, labels, corpus reproduction and full QC. A changed parent alters
semantic-map input: rebuild the real map and site rather than weakening their
freshness checks. Keep unrelated blocked draft #1218 separate.

## Additional Notes

All 441 returned open/closed issues and comments were searched for the target,
source key and oceanic-parent failure. #1231 concerns a different hadalpelagic
source; it is not this correction. The ontology, NOAA and BAS source texts
were inspected directly. No scientific input, generated artifact or history
was changed, and no independent reviewer approval is implied.
