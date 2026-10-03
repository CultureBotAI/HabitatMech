# YAML Record Review: freshwater lake biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/freshwater_lake_biome.yaml`
- Started UTC: 2026-10-03T08:53:37Z
- Finished UTC: 2026-10-03T08:54:49Z
- Verdict: pass

## Target

The complete generated `HabitatRecord` denotes `ENVO:01000252`, freshwater
lake biome, category `AQUATIC`, grounding `EXACT`, mapping `SEEDED`.
The sole source concept is `habitatmech:PREGO.834a337ad8`; the slug is fixed
at `data/habitats/PATHS.tsv:818`. This is the biome determined by a freshwater
lake, not the lake body or its water. Baseline:
`3cfdfff350ad925214be41e08836ad2783d0ef80`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/freshwater_lake_biome.yaml` | Pass; no issues found |
| `just validate-strict data/habitats/aquatic/freshwater_lake_biome.yaml` | Pass; one record, zero errors |
| Live OLS identity and hierarchy | Target definition and sole direct parent match; both terms active |
| NCBI reference | Taxon 148219 checked live in the immediately preceding lake review; exact ID/name match |
| Full `just qc` | Running on this unchanged report-only corpus at review completion; final result belongs to the batch PR |

Full local OAK validation was not rerun for this report; the relevant ontology
terms were checked directly. There are no literature citations or causal edges
requiring citation/graph validation.

## Identity and Grounding

`data/raw/ontology_terms.tsv:7757` agrees with the
[current ENVO definition](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000252).
The only parent, `ENVO:00000873` freshwater biome, matches the live OLS direct
parent response and `ontology_subclass_edges.tsv:5964`. A biome determined
by a freshwater lake specializes a freshwater biome; no water material or
lake-body superclass is introduced.

PREGO uses this ENVO identifier directly, supporting the current exact
resolution. Its spellings freshwater lake and freshwater lakes are correctly
marked RELATED_SYNONYM, not exact identities. They do not justify merging this
record with `ENVO:00000021` freshwater lake. No item decision was found for
the PREGO source concept, so `SEEDED` and the lone seeding event are accurate.

## Evidence

`data/raw/prego_habitats.tsv:719` supplies one taxon, one source edge, maximum
score 3, the annotated-genomes/isolate channel, and the synonym list. All
generated attestation values match. There is no GOLD attestation to add simply
because GOLD environmental triads use this biome term.

`prego_habitat_taxa.tsv:8474` supplies `NCBITaxon:148219`, uncultured Crater
Lake bacterium CL500-11, rank 1, score 3, direct flag TRUE, and no corroborating
source. The candidate pool is one. Its
[NCBI Taxonomy entry](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=148219&retmode=xml)
resolves unchanged with the recorded name. This same taxon also appears in the
distinct freshwater-lake source concept; that does not make the two habitat
classes identical, and their counts must not be added as independent organisms.

The record leaves `is_characteristic` unset. PREGO's reported association and
the taxon's resolvable identity do not establish characteristic presence across
all freshwater lake biomes.

## Completeness

Ignored/hidden-inclusive searches across `curation`, `history`, `research`,
`conf`, `data/raw`, `reports/yaml_record_review`, and the slug lock used the
target ID, minted PREGO source ID, label, and slug. No item decision, term
request, causal overlay, target-specific research report, environmental-
parameter row, or prior review of this target was found in those locations.
References in other reviews and GOLD broad-scale triads concern contextual use
of the term rather than new source concepts for this generated record.

The optional parameter, evidence, graph, discussion, and dataset slots are
appropriately empty. A single retained source association is not an exhaustive
list of organisms occupying the biome, and no extra taxa are inferred.

## Findings

None found: zero blockers, zero major, zero minor. Source reproduction and
identifier/hierarchy support were checked; the underlying PREGO ecological
assertion was not independently re-extracted or generalized.

## Recommended Edits

None required. A future item review can endorse the source resolution, but
must preserve the biome/body/material distinction and the weaker synonym scope.
This report does not itself promote mapping status.

## Follow-up Checks

For future curation, run `just seed` and
`just seed-canary ENVO:01000252 --force`; inspect the sole biome parent, one
TAXON attestation, and unchanged observed-taxon fields. Repeat focused schema
and strict validation, `just validate-products` for changed grounding,
`just verify-corpus`, semantic-map refresh if needed, `just render`, and
`just qc`. Add session history only for actual curation changes.

## Additional Notes

iModulonDB is not applicable: no gene, regulator, mechanism, or expression
dataset claim occurs here. No paid research or live PREGO re-extraction was
used. Generated data and curation status remain unchanged.
