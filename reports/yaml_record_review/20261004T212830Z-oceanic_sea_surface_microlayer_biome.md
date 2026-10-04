# YAML Record Review: oceanic sea surface microlayer biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/oceanic_sea_surface_microlayer_biome.yaml`
- Started UTC: 2026-10-04T21:26:28Z
- Finished UTC: 2026-10-04T21:28:30Z
- Verdict: pass

## Target

Entire generated HabitatRecord ENVO:01000034 oceanic sea surface microlayer
biome, AQUATIC/EXACT/SEEDED. It has an ENVO definition, one ontology parent,
two PREGO related synonyms, one four-TAXON attestation, all four retained
taxa and one seed event. Parameters, xrefs, evidence, graphs, discussions
and datasets are absent. `PATHS.tsv:763` pins the stem; actual source-key
minting gives habitatmech:PREGO.3081dd362d.

The target is the offshore sea-surface microlayer biome, not all sea water,
the entire ocean, generic surface water or a nearshore microlayer. Similar
labels elsewhere do not authorize source-count or identity merging.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/oceanic_sea_surface_microlayer_biome.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/oceanic_sea_surface_microlayer_biome.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared batch PASS: 1,179 canonical, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | Shared PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Terminal PASS: 457 tests passed, three skipped, two dependency warnings in 873.11 seconds; all gates passed. |
| Source/reference checks | Complete target, actual PREGO ingestion and complete taxon/attestation equality, 14 raw tables, current typed ENVO/OLS, all four current NCBI taxa, full semantic text and rendered page. |

QC validated 3,206 records, 90 history files and 32 causal overlays; exact
reproduction had zero missing, extra or differing records. Site, 231 redirects
and the 109-term public request table matched. The initial QC invocation
stopped before the runner on a uv cache denial; its authorized retry is the
successful run above. Earlier reports retain their then-pending QC timing.
These results do not establish SSSOM/KGX compatibility or original ecology.

## Identity and Grounding

Current [ENVO:01000034](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000034)
is active and matches physical ontology_terms.tsv line 7544. Its definition
describes the upper 1,000 micrometers of offshore marine surface water and
its atmosphere-ocean interface. That boundary and the described physical,
chemical and biological contrasts are inherited ontology scope statements,
not measurements from these four source associations.

The sole named superclass ENVO:01000033 oceanic pelagic zone biome matches
physical subclass row 5674 and current typed OWL. The parent's current prose
contains epipelagic despite its generic label/hierarchy; preserve that
upstream wording question rather than invent a local generated correction.
No source-only waterbody or landform parent is present in this target.

Actual PREGO ingestion uses prego_self_grounded, with one source concept and
zero reviewed sources. Source and record share the same ontology identifier.
EXACT without a mapping predicate, SEEDED and the single seed event are
faithful; this does not imply an ITEM ecological review or a #1398 witness.

The official term has no synonym assertion. PREGO supplies oceanic sea
surface microlayer and its plural, both correctly related. Canonical-label
deduplication removes the repeated full biome name. No #1249 ontology-scope
inflation is demonstrated, and the shorthand does not exact-equate all
surface-water environments.

## Evidence

`prego_habitats.tsv:421` gives four distinct taxa and four direct assertions,
environmental_samples only and maximum score 1.13534. The emitted TAXON
count and score agree. Four taxa is not four cultures or independent studies.

All raw rows at `prego_habitat_taxa.tsv:7455-7458` were inspected and their
complete generated dictionaries match actual ingestion:

| Taxon | Source score | Rank/pool | Raw direct flag |
| --- | ---: | --- | --- |
| NCBITaxon:172371 Alloalcanivorax venustensis | 1.13534 | 1/4 | TRUE |
| NCBITaxon:285271 uncultured Methylophaga sp. | 1.09698 | 2/4 | TRUE |
| NCBITaxon:31910 Halovibrio variabilis | 1.01834 | 3/4 | TRUE |
| NCBITaxon:550984 Halomonas sp. HAL1 | 1.00788 | 4/4 | TRUE |

Every row is environmental_samples only, with no corroboration or
is_characteristic claim. All four candidates are displayed, but this is
complete only for the source pool, not a complete microlayer community.
Scores are source-provided association values, not calibrated probabilities,
abundances or proof of stronger biological importance. Their lower values
do not negate the explicit TRUE direct flags.

[Current NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=172371,285271,31910,550984&retmode=xml)
resolved every ID directly with matching names and no alias redirects. All
four are species-ranked in NCBI, while uncultured/unclassified sp. names
retain their unresolved biological specificity. No strain-rank claim or
characteristic-presence claim is inferred from the labels.

The complete all-14-table exact-ID/source-key scan found only ontology/PREGO
inputs, with no GOLD, BacDive, MADIN or environmental-parameter contribution.
The batch's fresh ignored-inclusive search found no original PREGO files in
the configured kg-microbe checkout, and its network-authorized portal request
failed verified TLS with an expired certificate. No verification bypass was
used. Original sample contexts and causal literature were not recovered;
faithful projection and current identifiers do not independently certify
the four ecological associations.

## Completeness

Ignored-inclusive ontology-ID, minted-key, label/stem and filename searches
covered curation, history, research, reports, conf, PATHS and RETIRED. Only the
path lock was found: no target-owned decision, definition, overlay, session
history, retirement or previous individual review. All-state GitHub searches
for the ID, source key and label returned no matching issue.

No novel term or mandatory missing field is established. Empty optional
measurements and causal graphs should not be populated from generic
microlayer biology. iModulonDB is inapplicable without gene, regulator or
expression assertions. The full rendered page keeps all four taxa explicitly
source-associated and exposes their ranks against the four-taxon pool.

## Findings

None found within the inspected scope: zero blockers, zero major, zero minor.
This is a bounded identity/projection pass with original ecological evidence
unavailable, not certification of an entire microbial community or mechanism.

## Recommended Edits

None required by the inspected evidence. Preserve the offshore microlayer
identity, asserted parent, related synonym scopes, all four taxon dictionaries,
source scores/channel/count and SEEDED status/history. Any supported future
ecological correction belongs in the maintained source/extraction contract,
not generated YAML or this historical review.

## Follow-up Checks

Recover manifest-matching original PREGO inputs or accessible sample evidence
before upgrading associations to characteristic taxa or direct mechanism
claims. For a governed refresh, dry seed, inspect the ENVO:01000034 canary,
then require provenance, ordinary/strict/product validation, new history,
exact reproduction, site and full QC.

No semantic-map update is needed for a read-only report. Compare actual full
semantic inputs for future corrections and perform genuine rebuilding under
#1217 when changed. Preserve protected #1218/runtime pins and inspect actual
SSSOM/KGX products before compatibility claims.

## Additional Notes

Official typed ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated artifact, old report/history, paid research
or GitHub item was changed by this individual review.
