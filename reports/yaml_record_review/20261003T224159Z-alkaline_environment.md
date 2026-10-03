# YAML Record Review: alkaline environment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/other/alkaline_environment.yaml`
- Started UTC: 2026-10-03T22:38:49Z
- Finished UTC: 2026-10-03T22:41:59Z
- Verdict: pass

## Target

Read the complete generated HabitatRecord: `ENVO:01000316`, alkaline
environment, OTHER, EXACT, SEEDED. It contains the ENVO definition, one
PREGO related synonym, one parent, one source attestation, ten observational
taxa and one seed event. `data/habitats/PATHS.tsv:835` pins the stem.

## Validation

- `just validate data/habitats/other/alkaline_environment.yaml`: passed.
- `just validate-strict data/habitats/other/alkaline_environment.yaml`:
  one file, zero errors.
- Structured comparison verified all ten IDs, optional labels, scores,
  ranks and candidate-pool values against the committed PREGO inventory.
- Current NCBI Taxonomy EFetch resolved all ten IDs directly; current OLS
  verified the identity and parent as non-obsolete.
- Unchanged baseline `e12b8ca4b` passed local `just qc`, ontology
  correspondence and required head/queue checks in #1308: 457 tests passed,
  three skipped, two dependency warnings; 85 valid history records, 3,206
  strict-valid records, 32 overlays, exact corpus reproduction and current
  generated products. OAK: 1,179 canonical pairs, one synonym, five configured
  exceptions and 2,054 no-adapter skips. These are baseline receipts, not
  final-head checks for this new report branch.

## Identity and Grounding

The current [ENVO identity](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01000316)
agrees with `data/raw/ontology_terms.tsv:7819`: an environment exposing
entities to high pH, typically above nine. This is an environmental system,
not the pH quality itself. The word "typically" is not a strict measured
minimum, and no numerical environmental-parameter assertion is warranted.

The parent `ENVO:01000997`, environmental system determined by a quality,
is a strictly broader organisational class. Current OLS and
`ontology_terms.tsv:8492` agree; `ontology_subclass_edges.tsv:6036` supplies
the actual is-a edge. Its organisational/not-for-annotation note does not
invalidate use as a superclass. OTHER is appropriate for a class not limited
to aquatic, terrestrial, host-associated or engineered settings.

The PREGO plural alias is conservatively RELATED_SYNONYM. The source concept
decision key is `habitatmech:PREGO.06ab19a46f`. An ignored-inclusive search
found no decision for it in the maintained inputs; `ingest_prego` therefore
uses its ordinary self-grounding route. SEEDED and the sole
2026-08-16T05:58:02Z event correctly describe that state. This review does
not promote it to REVIEWED.

## Evidence

`data/raw/prego_habitats.tsv:339` supplies ten taxa, ten direct assertions,
maximum score four, environmental_samples and the two lexical forms. The
record faithfully emits the taxon unit, maximum score and channel.
`prego_habitat_taxa.tsv:8649-8658` supplies the entire ten-entry pool:
eight scores of four, then 1.10314 and 1.08264. All ten direct flags are TRUE
in the inventory; no corroborating source is recorded. No `is_characteristic`
or causal claim is added by the generated record.

The [PREGO methods paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC8879827/),
sections 2.1 and 2.4, describes ontology-normalized associations inferred
from environmental sample profiles and metadata. Scores order source
associations; they are not prevalence, growth limits or habitat specificity.
The paper's microbial scope makes the two nonmicrobial IDs below worth
tracing, but does not establish the source of those particular rows.

Current NCBI resolves the eight supplied labels exactly: Elizabethkingia
meningoseptica (238), Capnocytophaga canimorsus (28188), Gemmatimonas
aurantiaca T-27 (379066), Tritonibacter mobilis (379347), Rhizobium
leguminosarum (384), Flavobacterium columnare (996), Halanaerobium
congolense (54121) and Desulfonatronovibrio hydrogenovorans (53245).
The two unlabeled entries resolve to Coptotermes formosanus (36987) and
Sorghum bicolor (4558), not unidentified bacteria. NCBI references:
[36987](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=36987),
[4558](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=4558).

The local schema defines `CharacteristicTaxon` as a general observational
taxon association and makes its label optional. It does not assert that every
listed taxon is microbial or characteristic. The two names alone therefore
do not justify deleting their source associations or declaring them impossible.
Their ecological roles and original sample-level support remain unverified.

The pinned [kg-microbe PREGO transform](https://github.com/Knowledge-Graph-Hub/kg-microbe/blob/7698351a54b48f2e917635fdf51cd0a6b323135d/kg_microbe/transform_utils/prego/prego.py)
maps ENVO-to-taxon rows into location_of associations; its `utils.py` derives
channel names from archives and preserves NCBITaxon IDs without a microbial
lineage filter. HabitatMech `extract_prego` preserves those IDs and channels,
deduplicates pairs and ranks by score with deterministic tie-breaking.
`ingest_prego` copies the maintained entries. This is provenance tracing,
not independent validation of each ecological association.

## Completeness

Ignored-inclusive identifier, label, stem and decision-key searches covered
curation, history, research, prior reports, the path map and ontology
inventories. No exact-target curation decision, authored definition, causal
overlay, session history or earlier exact-target review was found there.
Related saline/alkaline reports are not substitutes for this record's evidence.

Structured full-table scans found no exact identity/label match among 770
parameter rows, 358 isolation-source grounding rows or 58 Madin habitat rows.
Empty optional parameters, graphs, citations and discussions are not defects.
iModulonDB is not applicable: the record contains no gene, regulator or
expression-module claim.

An ignored-inclusive `find` of the configured kg-microbe checkout's `data/`
and `kg_microbe/` trees returned no PREGO-named files. Original pair evidence
could not be checked there; the live PREGO page also failed to load. This is
a bounded availability limit, not proof the source data do not exist elsewhere.

## Findings

None established: zero blockers, zero major and zero minor findings in the
checked identity, source-copying, taxonomy and schema scope. The verdict is
not experimental confirmation of all ten ecological associations. The
nonmicrobial pair provenance is an explicit unresolved check, not a proven
mapping error or an invented negative ecological claim.

## Recommended Edits

No mandatory record edit is supported. Before interpreting the two
nonmicrobial entries as microbial residents, recover their original PREGO
rows and evidence URLs from the pinned KGX source and resolve the associated
sample roles. Any correction belongs in the upstream source transform or
maintained extraction inputs, not generated YAML. A label refresh would also
belong in the maintained taxon-label extraction, not a hand edit.

## Follow-up Checks

Check the original pair-level evidence against `data/raw/MANIFEST.yaml`:
the PREGO edges input is SHA-256
`8863ee3197a36915865fa4833df39d10c3f8f69b64bafbb746b9cd731308a0aa`,
from kg-microbe `7698351a54b48f2e917635fdf51cd0a6b323135d`. If source
curation becomes justified, add focused association tests, regenerate through
the normal extractor/seeder, inspect a canary, and run strict validation,
corpus reproduction, product correspondence and `just qc`. Do not infer a
new pH measurement, characteristic status or mechanism from source scores.

## Additional Notes

The original 2022 PREGO paper does not prove the exact contents of the 2026
snapshot. Likewise, a score of four alone does not identify an evidence
channel; the pinned transform and recorded channel are the relevant checks.
No curation input, generated record, prior report or history was changed.
No paid research ran. The institutional PDF fetch failed; the inspected PMC
methods text supplied the source-method context.
