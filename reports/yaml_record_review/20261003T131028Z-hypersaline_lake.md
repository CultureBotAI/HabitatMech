# YAML Record Review: hypersaline lake

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/hypersaline_lake.yaml`
- Started UTC: 2026-10-03T13:06:55Z
- Finished UTC: 2026-10-03T13:10:28Z
- Verdict: pass

## Target

The complete generated `HabitatRecord` was read: `ENVO:01001020`, hypersaline
lake, `AQUATIC`, `EXACT`, `SEEDED`. It contains an ENVO definition, two parents,
one GOLD attestation, and one seed-history event. `PATHS.tsv:874` locks the
stem. This target is not the separate Acidic hypersaline lake or GOLD
Hypersaline source bin.

## Validation

- `just validate data/habitats/aquatic/hypersaline_lake.yaml`: pass.
- `just validate-strict data/habitats/aquatic/hypersaline_lake.yaml`:
  one record, zero errors.
- The repository mint function reproduces source key
  `habitatmech:GOLD.ac077b806e`; the resolver reproduces `gold_leaf_label`,
  `EXACT`, and `skos:exactMatch` without an ITEM decision.
- Live OLS API checks verified the identity, saline-lake parent, lake and
  water-body ancestry, and the aquatic-environment genus of the curated parent.
  Browser-tool API retrieval failed; direct structured API retrieval succeeded.
- Full baseline QC is verified at the unchanged corpus commit
  `fd6fb287de9fae9eac672842dde7f82ce3d0b66f`, merge-group run
  [37124645220](https://github.com/CultureBotAI/HabitatMech/actions/runs/37124645220):
  success. Local QC of the identical tree also passed: 453 tests passed,
  three skipped, two dependency warnings, 3,206 reproducible/schema-valid
  records, 82 valid history records, and current site/redirects. This report
  does not claim that a fresh full suite was run for this individual record.
- No record PMID, DOI, taxon, mechanism edge, gene, or transcriptomic dataset
  requires a literature-reference or iModulonDB check.

## Identity and Grounding

The exact label and ENVO definition agree with the source leaf. Current ENVO
defines this as a lake with water saltier than ocean water, with the active
`ENVO:00000019` saline lake as its direct parent. The vendored edge at
`data/raw/ontology_subclass_edges.tsv:6815` agrees. Do not replace this lake
identity with its water constituent or a generic salinity quality.
[Hypersaline lake](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001020),
[saline lake](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000019).

The second parent, `habitatmech:GOLD.ce244e62cd`, resolves to the maintained
inland saline or alkaline aquatic environment. Its definition at
`curation/term_requests.tsv:43` is explicitly disjunctive: saline, alkaline,
or both. The represented non-marine saline lake satisfies its saline arm;
alkalinity is not silently inferred. This is a source-scope compatibility
judgment against the maintained broad environment definition, not an extra
subclass edge claimed to come from ENVO. The parent is not the older rejected
quality-only interpretation described in its historical record.

Current lake ancestry proceeds through lentic water body, water body, water
mass, and body of liquid. The lake definition places the water in a depression
on a landmass; it does not add a measured pH or ionic-composition criterion.
[Lake](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000020),
[aquatic environment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000317).

No ITEM decision exists for source `ac077b806e`; `SEEDED` correctly reports
that state. A read-only review does not promote it to `REVIEWED`.

## Evidence

| Claim | Inspected source and scope |
|---|---|
| Source path and count | `gold_ecosystem_paths.tsv:180` gives `Environmental > Aquatic > Non-marine Saline and Alkaline > Hypersaline lake`, depth four, 115 ORGANISM assertions, and nodes 7892/7893. The displayed first node and two-node note are faithful. |
| Definition | `ontology_terms.tsv:8515` and the live active ENVO term agree. |
| Broader lake | The vendored and current ontology edge both point to saline lake. |
| Curated environment parent | The parent record and maintained definition were read in full; the GOLD parent-path pass in `src/habitatmech/seed.py` supplies this edge. Its saline-or-alkaline wording is relevant here. |
| Separate sample inventories | Structured exact-path scans found no row in `gold_path_biosamples.tsv`, `gold_path_triads.tsv`, or `gold_studies.tsv`. Zero snapshot coverage is not proof that no samples exist. |

Five triad rows use this ENVO ID in other source paths, including the distinct
Hypersaline bin, its mats/sediment, an Athalassic path, and a culture-medium
path. None is evidence for changing this record's organism count, adding
sample statistics, or importing those source contexts as its identity.

## Completeness

No target PREGO, Madin, or environmental-parameter association was found in
the complete parsed inventories. Optional taxa, numeric salinity/pH values,
mechanisms, and generic discussion should remain empty rather than be inferred
from the label, the broader parent's taxa, or neighboring source bins.

Hidden/ignored-inclusive searches of curation, history, research, configuration,
raw inventory files, path lock, and review reports covered the ID, label, stem,
and recomputed source key. They found incidental acidic-lake/parent research
mentions, but no target decision, term request, overlay, or session history.
Exact `Record:` header coverage, including ignored files and both quoted and
unquoted headers, found no prior individual review of this target.

## Findings

None found. Zero blockers, major findings, or minor findings. This bounded pass
covers the represented ontology and source claims, not a fresh validation of
all 115 underlying organism submissions.

## Recommended Edits

None required. Preserve the exact lake identity, saline-lake parent, separately
documented source grouping, 115-ORGANISM unit, and non-promoted mapping status.

## Follow-up Checks

At source refresh, recheck GOLD nodes 7892/7893 and their full path before
transferring any sample crosswalk. Revalidate both parent meanings if the
curated inland-environment definition changes. Any actual curation must use
maintained inputs, append history, canary through the seeder, and pass corpus,
applicable ontology-product, semantic-map/site, and full QC gates.

## Additional Notes

No corpus, source inventory, curation input, generated product, or historical
report was changed. The earlier acidic-hypersaline-lake review is a different
target and is not reused as this record's review.
