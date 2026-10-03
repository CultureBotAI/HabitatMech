# YAML Record Review: freshwater lake

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/freshwater_lake.yaml`
- Started UTC: 2026-10-03T08:50:40Z
- Finished UTC: 2026-10-03T08:51:37Z
- Verdict: needs curation

## Target

The complete generated `HabitatRecord` is `ENVO:00000021`, freshwater lake,
category `AQUATIC`, grounding `EXACT`, mapping `REVIEWED`.
`data/habitats/PATHS.tsv:438` fixes its slug. The target denotes a freshwater
water body, not its water material or its associated biome. Baseline:
`3cfdfff350ad925214be41e08836ad2783d0ef80`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/freshwater_lake.yaml` | Pass; no issues found |
| `just validate-strict data/habitats/aquatic/freshwater_lake.yaml` | Pass; one record, zero errors |
| Live term/reference checks | Target and direct ontology parents match OLS; the single NCBI taxon resolves with the exact recorded name |
| Full `just qc` | Running for this report-only branch when this review finished; final result belongs to the batch PR |

No literature references or causal edges are present. Full OAK validation was
not rerun for this report; relevant terms were inspected directly. Passing
schema checks does not validate the scientific meaning of a source-path edge.

## Identity and Grounding

The target definition and ENVO synonym match `ontology_terms.tsv:6618` and
the [current ENVO freshwater-lake term](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000021).
The composed GOLD label is freshwater lake; PREGO uses the exact ENVO ID.
Both contributing source concepts have item-level `REVIEW` decisions:
`habitatmech:GOLD.d14ddff103` at `curation/decisions.tsv:1155` and
`habitatmech:PREGO.d988e3979f` at row 1507. The generated status and two
review events are therefore reproducible, but do not excuse an erroneous
automatically inherited parent.

The two supported direct parents are `ENVO:00000020` lake and
`ENVO:01001320` fresh water body, matching live OLS and
`ontology_subclass_edges.tsv:4650-4651`. Their definitions describe water
bodies. `ENVO:00002011` fresh water instead denotes low-solute water
material and is generated only from the immediate GOLD path. A lake containing
fresh water is not an instance of its contents.

## Evidence

| Claim | Inspected source | Assessment |
|---|---|---|
| GOLD source label/path, two nodes, 1,002 ORGANISM assertions | `gold_ecosystem_paths.tsv:42`, nodes 3792 and 4179 | Exact match; first-node display and explanatory note are accurate |
| PREGO source ID, one TAXON, score 3, isolate channel | `prego_habitats.tsv:658` | Exact match; not summed with the organism count |
| One retained observed taxon | `prego_habitat_taxa.tsv:3266`, rank 1, pool 1, score 3 | Exact source reproduction; no corroboration or characteristic flag |
| Taxon identity | [NCBI Taxonomy 148219](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=148219&retmode=xml) | Current ID/name: uncultured Crater Lake bacterium CL500-11 |
| Source-specific aliases | GOLD Lake, PREGO freshwater lakes, ENVO FreshwaterLake | Provenance retained; the generic GOLD spelling is interpreted with its source path |
| Separate sample counts | `gold_path_biosamples.tsv:5`, node 4179, 6,675 samples | Different inventory from the organism assertions and triad cohort |
| Broad/local/medium roles | `gold_path_triads.tsv:314-316` | Freshwater lake biome / freshwater lake / lake water, respectively |

The triad cohort has 7,045 samples across 155 studies. Broad-scale biome has
share 0.99 with 151 agreeing studies; local lake has share 0.97 with 144;
medium lake water has share 0.97 with 143. The study crosswalk has 161 exact
path memberships. These inventories have different coverage and must not be
forced into a single count. Their distinct environmental roles reinforce the
lake-versus-water distinction, but do not constitute mechanism evidence.

The NCBI entry establishes identifier resolution, not independent evidence that
the organism characterizes all freshwater lakes. The record correctly leaves
`is_characteristic` unset.

## Completeness

Ignored/hidden-inclusive searches covered `curation`, `history`, `research`,
`conf`, `data/raw`, `reports/yaml_record_review`, and the slug lock, using the
record ID, both source-concept IDs, label/slug, and exact GOLD path. They found
the two item decisions and relevant source/triad/taxon rows, but no target
definition request, mechanism overlay, environmental-parameter row, or prior
target review. Numerous other reports mention this lake as context; those do
not substitute for reviewing this record. General lake discussions in research
reports concern other targets.

Empty evidence, causal graph, parameter, discussion, and dataset slots are not
defects on the available inputs. No missing taxa are inferred from GOLD's
aggregate count, and the one PREGO association is not described as an exhaustive
ecological inventory.

## Findings

One major; zero blockers; zero minor.

**HM-FRESHWATER-LAKE-001 (major): fresh-water material is not a lake parent.**
The GOLD second pass in `src/habitatmech/seed.py:ingest_gold` adds
`ENVO:00002011` because Lake is nested under Freshwater. The
[fresh-water-body definition](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001320)
distinguishes the body from its material, while the existing correct lake/body
parents already classify this target. Future curation should suppress only the
source contribution keyed by `habitatmech:GOLD.d14ddff103`, preserving all
independent ontology parents and source assertions. The new exclusion interface
is proposed in draft PR #1218, not yet part of this baseline.

## Recommended Edits

1. Record the exact GOLD parent exclusion in the maintained interface once
   available; retain the source path and both ontology parents.
2. Keep the two supported identity endorsements. Do not move PREGO's observed
   taxon to water material or lake biome just to remove the bad parent.
3. Preserve the ontology-owned definition verbatim, including its grammatical
   awkwardness; text correction belongs upstream, not in generated YAML.

## Follow-up Checks

Run `just seed` and `just seed-canary ENVO:00000021 --force`, then inspect
the two true parents, both attestations, and the one unchanged observed taxon.
Repeat focused schema/strict validation, `just validate-products`, and
`just verify-corpus`. Record actual curation history; refresh semantic-map
artifacts for changed parent text before `just render` and `just qc`.

## Additional Notes

iModulonDB is not applicable: no gene, regulator, stress response, or expression
dataset is asserted. Source verification is against the committed GOLD/PREGO
inventories, with live ontology/taxonomy identity checks. No generated record,
curation decision, or review status changed in this review.
