# YAML Record Review: freshwater biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/freshwater_biome.yaml`
- Started UTC: 2026-10-03T08:25:04Z
- Finished UTC: 2026-10-03T08:28:55Z
- Verdict: pass

## Target

The complete generated `HabitatRecord` denotes `ENVO:00000873`, freshwater
biome, with category `AQUATIC`, grounding `EXACT`, and mapping `REVIEWED`.
`data/habitats/PATHS.tsv:600` fixes this slug. It is distinct from the water
material `ENVO:00002011` and the source-qualified groundwater Freshwater
record. Review baseline: `fd6af4035db0b6cb2a2553fc6b048a27ed333939`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/freshwater_biome.yaml` | Pass; no issues found |
| `just validate-strict data/habitats/aquatic/freshwater_biome.yaml` | Pass; one record, zero errors |
| Shared `just qc` baseline | Passed earlier in this session: 451 tests passed, 3 skipped; 3,206 records valid and reproduced; history/site/redirect/term-request gates passed |
| Live ontology checks | Identity, definition, synonym, both parents, and active status checked through OLS |
| Live taxonomy checks | All 50 requested IDs returned unchanged by NCBI Taxonomy EFetch |
| Structured source comparison | All retained taxon labels, ranks, scores/counts, and corroboration flags match the two committed source slices |

Only reports changed after the shared QC baseline. Full local OAK
`just validate-products` was not rerun for this report-only review; relevant
ontology terms were checked directly. No literature citations or causal edges
require a citation/graph check on this target.

## Identity and Grounding

The definition and exact ENVO synonym `freshwater realm` agree with
`data/raw/ontology_terms.tsv:7152` and the
[live OLS term](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000873).
Both direct parents, `ENVO:00002030` aquatic biome and `ENVO:01001789`
freshwater ecosystem, agree with the live OLS parent response and
`data/raw/ontology_subclass_edges.tsv:5247-5248`. Unlike the fresh-water
material record, this biome legitimately specializes those classes.

PREGO uses the ENVO identity directly. BacDive's source label `Freshwater`
is mapped by the upstream table to this biome with `skos:closeMatch`, not
`skos:exactMatch` (`data/raw/isolation_source_groundings.tsv:123`). That
weaker source relation is preserved in the attestation. Overall `EXACT`
grounding is supported by PREGO's direct identity and does not strengthen
the BacDive mapping. The source-labelled BacDive synonym follows the
repository convention and should not be used to merge all records named
Freshwater. Item decisions at `curation/decisions.tsv:67` and `:1443`
endorse both contributing resolutions, explaining `REVIEWED` and the two
review events. This review found no evidence requiring reversal of those
decisions; source-label ambiguity is not independent evidence of equivalence.

## Evidence

| Claim | Inspected support | Assessment |
|---|---|---|
| BacDive attestation | `bacdive_isolation_sources.tsv:33`; ID `bacdive.isolation_source:freshwater`, 469 strains, 438 taxa | Count 469 has unit STRAIN; 438 is the candidate taxon pool |
| PREGO attestation | `prego_habitats.tsv:5`; 5,856 taxa, maximum score 4, two channels | Correct TAXON count and score; source edge count 6,338 is not substituted for taxa |
| Seven synonym entries | ENVO term, BacDive source label, PREGO synonym list | Source and scope retained; duplicate text has distinct provenance/scope |
| 50 retained taxa | 25 rows in each source slice; PREGO rows 5163-5187 | Disjoint retained ID sets; ranks 1-25 in each source, not one global prevalence ranking |
| Five corroborated entries | Four BacDive rows marked PREGO; one PREGO row marked BACDIVE | Flags match source inventories, including corroboration outside the retained slices |
| Optional missing taxon label | PREGO row 5167 has no label for `NCBITaxon:102822` | Faithfully omitted, not a broken reference; NCBI currently resolves it to Staurastrum punctulatum |

All 49 populated labels match the current scientific names returned by
[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=102822&retmode=xml)
in a bulk query of all 50 IDs. The linked single-ID request documents the
unlabelled entry. Neither database association nor cross-source corroboration
proves a taxon is characteristic of freshwater biomes. No entry sets
`is_characteristic: true`; surprising ecological associations remain reported
source assertions, not independently verified ecological generalizations.
STRAIN and TAXON counts must not be added together.

## Completeness

Ignored/hidden-inclusive searches covered `curation`, `history`, `research`,
`conf`, `data/raw`, `reports/yaml_record_review`, and the slug lock, using the
ontology ID, both source-concept IDs, biome label/realm synonym, and slug.
They found the two item decisions and source inputs, but no target-specific
term request, causal overlay, research report, or prior target review. Other
reviews and GOLD triads mention this term as broad environmental context;
they are not reviews or new source concepts for this target. No raw
environmental-parameter row names this identity.

Empty evidence, graph, discussion, dataset, and parameter slots are appropriate
for the available maintained inputs. A future provenance-preserving source
refresh can supply the missing optional taxon label; direct generated-file
patching is not justified.

## Findings

None found: zero blockers, zero major, zero minor. This verdict concerns
correct identity and scoped representation of the inspected source assertions,
not proof of every underlying ecological association.

## Recommended Edits

None required. Retain the BacDive `closeMatch` and both valid biome parents.
Keep freshwater material, biome, and qualified source concepts distinct.

## Follow-up Checks

For a future source/curation change, run `just seed` and
`just seed-canary ENVO:00000873 --force`, then inspect both attestations,
parents, source-specific counts, and the retained taxon slices. Repeat focused
validation, `just verify-corpus`, `just render`, and `just qc`; use
`just validate-products` for changed grounding and record actual curation in
session history.

## Additional Notes

iModulonDB is not applicable: no gene, regulator, mechanism, or expression
dataset claim occurs here. Taxonomy checks establish identifier resolution,
not habitat membership. No paid research or live strain-level BacDive/PREGO
re-extraction was performed. The generated record and mapping status were not
changed by this review.
