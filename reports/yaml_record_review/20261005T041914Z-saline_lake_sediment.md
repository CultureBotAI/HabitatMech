# YAML Record Review: saline lake sediment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/saline_lake_sediment.yaml`
- Started UTC: 2026-10-05T04:12:32Z
- Finished UTC: 2026-10-05T04:19:14Z
- Verdict: needs curation; 0 blocker, 2 major, 0 minor findings.

## Target

The entire generated HabitatRecord was read. ENVO:00002209 denotes saline
lake sediment, not the lake or its water. The AQUATIC record is EXACT and
REVIEWED, with an ENVO definition, five source-qualified synonym entries,
two parents, GOLD/PREGO attestations, 25 taxa and three history events.
PATHS.tsv:679 fixes its stem. Parameters, external xrefs, evidence, graphs,
discussions and datasets are empty. No scientific input or output was edited.

## Validation

- `just validate data/habitats/aquatic/saline_lake_sediment.yaml`: pass.
- `just validate-strict data/habitats/aquatic/saline_lake_sediment.yaml`:
  pass, one file and zero errors.
- Actual build_corpus/build_document reproduction: complete dictionary
  equality, two source concepts, two reviewed sources, 25 taxa, three events.
- `just validate-products`: pass; 1179 canonical labels, one synonym,
  five configured exceptions and 2054 no-adapter skips. This does not test
  ecological occurrence, synonym scope or parent correctness.
- `just worklist --status all --limit 5`: pass; 953 ungrounded concepts,
  1810 decisions. Exact target resolution was inspected independently.
- Fresh `just qc` remains live during tests at review close; lint,
  documentation and raw provenance passed. Corpus-wide history, schema,
  reproduction, site, redirects and term requests are not claimed complete
  here. Log: /private/tmp/habitatmech-saline-sediment-marsh-qc-20261005.log.
- Previous publication's separate main-push QC 37262175453 reached terminal
  SUCCESS during this review; it is not the fresh local run.
- Actual full-context semantic probes: removing the whole-lake parent changes
  semantic text; correcting only the ENVO synonym scope or omitting only the
  GOLD mapping predicate does not. No map or site was regenerated.

## Identity and Grounding

Current active [ENVO:00002209](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002209)
and ontology_terms.tsv:7291 agree on identity, label and definition. The
source path ends in Saline lake > Sediment, supporting the composed identity
rather than a context-free lexical match to every sediment. Actual minting
gives habitatmech:GOLD.b233d8686d; gold_composed_label resolves EXACT with
skos:exactMatch. ITEM REVIEW at decisions.tsv:1008 endorses that route.
PREGO source key habitatmech:PREGO.0426c15a01 is self-grounded to the ENVO
term and ITEM-reviewed at row 1400. Both 2026-08-13 reviews and the
2026-08-16 seed event explain REVIEWED mechanically.

The GOLD source-to-record endpoints differ; PREGO self-identity has no
predicate. Neither is a new #1398 retained-minted-endpoint witness. GOLD's
Sediment alias is source-qualified by its retained full path, not independent
evidence that generic sediment and saline-lake sediment are identical.

Typed [official ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl)
marks soda lake sediment as hasRelatedSynonym. The untyped inventory pipe
and seed.py:406-407 promote it to EXACT_SYNONYM, a verified #1249 witness.
The three PREGO related entries are faithfully retained and must not be
globally changed to repair that one ENVO assertion.

The true named ontology parent is ENVO:00000546 lake sediment, asserted by
ontology_subclass_edges.tsv:5404. The OWL also has a restriction relating the
sediment to ENVO:00000019, not a named subclass assertion to the whole lake.
The record's whole-lake parent is instead introduced by the GOLD second
parent-path pass at src/habitatmech/seed.py:898-907. Its parent source key
habitatmech:GOLD.6b15f339ac resolves through gold_leaf_label, endorsed by
ITEM REVIEW at decisions.tsv:638. Correct lake identity does not make
material deposited at its bottom a subtype of that water body.

Both entire parent records were read as context only. Preserve the true
lake-sediment genus. Its TERRESTRIAL directory/category is not a rule that
every child must share that category; the reviewed target's explicit GOLD
Aquatic path supplies its own category. Do not transfer parent counts or
taxa, or count those contextual reads as new individual reviews.

## Evidence

Physical gold_ecosystem_paths.tsv:313 contains one depth-five node, 7283,
and 43 ORGANISM assertions. No collapsed-node note is needed. Bulk inventory
row 678 separately counts eight biosamples. The one matching study,
Gs0156840 at gold_studies.tsv:4155, includes lake, lake sediment and
lakeshore soil paths. Its original GOLD study page returned 403; it was not
read in full, and all study objects cannot be assigned to this sediment.
The current official GOLD node lookup returned 404, not proof of retirement.

All 14 raw inventories were scanned for the exact GOLD path/node. No exact
complete-triad row, parameter assertion or BacDive/Madin contribution was
found in that bounded scan. The parent lake's ten API triads are not this
child's data. Ontology and PREGO inventories were checked separately.

prego_habitats.tsv:112 records 355 taxa, 355 direct assertions, maximum
score 4 and both annotated_genomes_isolates/environmental_samples channels.
All 25 retained rows at prego_habitat_taxa.tsv:6274-6298 specifically carry
environmental_samples, direct_flag TRUE and score 4, without corroboration.
The habitat-level channel union does not mean each retained taxon has isolate
evidence. extract_prego at extract.py:331-429 retains an untruncated count
and a capped ranked list; ties sort by taxon ID after score/directness.
ingest_prego at seed.py:1012-1107 preserves these observational entries.
The 25/355 difference is not a count error, and rank is not relative abundance.

The original [PREGO methods paper](https://doi.org/10.3390/microorganisms10020293),
PMID:35208748, was inspected through Europe PMC's structured full-text API,
specifically section 2.4 and Appendix C. Environmental-sample associations
come from taxonomic analyses combined with sample metadata, and their scores
are capped at four. This explains why capped ties need caution; it does not
independently verify any particular target/sample pair. A direct annotation
flag is not proof of culture isolation, viability or characteristic presence.

Current [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi)
EFetch resolved every stored ID to its exact stored label. All 25 compact
responses were inspected, including the following ranks; no merged-ID or
label-mismatch finding was established.

| NCBITaxon ID | Verified label | Current rank |
| --- | --- | --- |
| 100884 | Coprobacillus cateniformis | species |
| 1015 | Bergeyella zoohelcum | species |
| 1026 | Marinoscillum furvescens | species |
| 1027 | Microscilla marina | species |
| 104176 | Oscillochloris trichoides | species |
| 106111 | Pedobacter sp. KP-2 | species |
| 1063 | Cereibacter sphaeroides | species |
| 1087 | Rhodovibrio salinarum | species |
| 111105 | Porphyromonas gulae | species |
| 114628 | Alkaliphilus transvaalensis | species |
| 120962 | Roseiflexus castenholzii | species |
| 1229 | Nitrosococcus oceani | species |
| 1270 | Micrococcus luteus | species |
| 128 | Isosphaera pallida | species |
| 131081 | Corynebacterium capitovis | species |
| 137722 | Azospirillum sp. B510 | species |
| 1462 | Geobacillus kaustophilus | species |
| 147 | Spirochaeta aurantia | species |
| 154 | Winmispira thermophila | species |
| 1562 | Desulfotomaculum | genus |
| 158 | Treponema denticola | species |
| 158847 | Megamonas hypermegale | species |
| 159254 | Parachlamydia acanthamoebae str. Hall's coccus | strain |
| 162209 | Paenibacillus naphthalenovorans | species |
| 165 | Treponema saccharophilum | species |

The original [B510 genome abstract](https://pubmed.ncbi.nlm.nih.gov/20047946/),
DOI:10.1093/dnares/dsp026, was inspected by structured EFetch and identifies
rice-stem isolation. That does not contradict a later environmental-sample
taxonomic assignment by itself. Similarly, familiar host-associated species
names do not prove absence from sediment. Do not manufacture ecological
exclusion findings from taxon names or substitute type-strain origin for the
missing environmental-sample chain. The genus-level row is not evidence that
every Desulfotomaculum member occurs here. None of the 25 entries sets
is_characteristic; schema and rendered-page wording are correctly weaker.

The complete generated page was inspected. It exposes the unsupported
whole-lake broader link and retains all source/rank/pool context. Its
associated/reported-from warning is appropriate, but cannot independently
validate PREGO sample classification or source metadata.

## Completeness

Ignored/hidden-inclusive searches covered the exact identifier, both source
keys, label and stem across curation, conf, history, research, prior reports,
raw inventories and PATHS/RETIRED. No target-owned definition request, causal
overlay, separate history record or earlier individual target review was
located in those surfaces. An exact ENVO-grounded target does not need a new
minted definition request merely to suppress a false source parent.

The ignored-inclusive configured kg-microbe file inventory found no PREGO
path. The original transformed nodes/edges and per-sample annotations were
not available there. PREGO's home and exact target pages were inaccessible
through the web tool. Thus original sample IDs, taxonomic confidence,
metadata spans and source versions behind the 25 environmental associations
remain unrecovered; the full 355-association pool was not independently
audited. This is a bounded evidence limit, not proof all those taxa are wrong.

No reviewed source requires optional chemistry, datasets, discussions or
causal-graph filler. iModulonDB is not applicable: this record contains no
gene/regulator/expression claim. Genes mentioned in a contextual genome
abstract were not imported as habitat mechanism evidence.

## Findings

| Severity | Finding | Maintained owner / scope |
| --- | --- | --- |
| Major | Saline lake sediment inherits the whole saline lake as a strict broader class. The true lake-sediment genus must remain. | Exact-source parent contribution for habitatmech:GOLD.b233d8686d to ENVO:00000019 in `src/habitatmech/seed.py`; governed source-parent control, not generated YAML. |
| Major | ENVO-related soda lake sediment is emitted as an exact synonym. | Typed ontology extraction in `src/habitatmech/extract.py`, `data/raw/ontology_terms.tsv` and `src/habitatmech/seed.py`; shared #1249. |

No blocker or minor finding was established. Unrecovered sample evidence is
not silently converted into either ecological approval or another defect.

## Recommended Edits

1. Suppress only the exact GOLD source-to-whole-lake parent contribution
   through a maintained, regression-tested control. Keep ENVO:00000546,
   exact habitat identity, full GOLD path/node, 43 ORGANISM and 355 TAXON
   units and historical ITEM reviews. A decision endorsement alone does not
   suppress the separate parent-path pass. Do not apply a term-request
   REPLACE flow to this EXACT target or delete both parents.
2. Extend #1249's typed-scope repair with soda lake sediment as a related
   witness. Preserve independently correct PREGO related aliases and the
   context-qualified GOLD leaf. Do not manually patch generated YAML, raw
   checksum metadata or older reports to simulate a source-contract fix.
3. Recover the original PREGO environmental samples for future ecological
   validation. Keep that work separate from definite hierarchy/synonym fixes;
   do not delete all host-associated names or import culture growth limits.

## Follow-up Checks

For later authorized curation, add exact-source parent exclusion and retained
material-genus controls, typed-synonym tests and source/count preservation
tests. Append required new history, dry-seed, then inspect a forced canary
for ENVO:00002209 before guarded wider regeneration. Never prune a partial
run or manually edit generated outputs. Run ordinary/strict validation,
labels, provenance, history, corpus reproduction, site/redirect, term-request
checks and full QC.

Parent removal changes actual full-context semantic input and requires a
genuine map/site refresh under #1217, preserving protected draft #1218 and
runtime pins. Scope-only repair was verified neutral; spelling or additional
content changes need a fresh comparison. No SSSOM/KGX readiness claim follows
without auditing actual products and current kg-microbe consumer contracts.

## Additional Notes

Typed ENVO cache SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
Current OLS succeeded through its structured API; the web tool's OLS fetch
failed. Typed scopes came from inspected OWL, not flattened OLS synonyms.

All-state inventory: 567 GitHub issues searched by exact keys and sediment
hierarchy terms. #1293 concerns marine sediment, #1269 mangrove materials,
and #1444 Sabkha sediment; none names this exact source. #1249 already owns
the shared synonym contract. No GitHub mutation occurred during this
individual review. Publication may file the exact hierarchy follow-up under
the standing user request, without claiming its scientific repair is done.
