# YAML Record Review: Hypersaline spring

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/hypersaline_spring.yaml`
- Started UTC: 2026-10-03T13:32:09Z
- Finished UTC: 2026-10-03T13:33:14Z
- Verdict: pass

## Target

Read the entire generated `HabitatRecord`, `habitatmech:GOLD.36956c8743`,
Hypersaline spring: `AQUATIC`, `UNGROUNDED`, `SEEDED`, one parent, one GOLD
attestation, and two history events. It contains no definition, taxa,
parameters, citations, or causal graph. `PATHS.tsv:1695` locks its stem.
This is not the separate groundwater-path Saline spring or its sediment.

## Validation

- `just validate data/habitats/aquatic/hypersaline_spring.yaml`: pass.
- `just validate-strict data/habitats/aquatic/hypersaline_spring.yaml`:
  one record, zero errors.
- The repository mint function reproduces `habitatmech:GOLD.36956c8743`.
- Current OLS term and search responses were inspected; the primary study's
  title, PMID, DOI, and abstract were retrieved through Europe PMC after
  PubMed/PMC browser pages returned challenges.
- Full corpus/schema/history/site QC is verified at unchanged base
  `ce53c21e8be841478dfdc730cef28ad2ca4bf462`, successful
  [run 37125963812](https://github.com/CultureBotAI/HabitatMech/actions/runs/37125963812).
  This reuses the full baseline rather than claiming a fresh per-record suite.

## Identity and Grounding

The full source path denotes a hypersaline spring, not water quality alone.
Active `ENVO:01001893` salt spring has synonym saline spring and defines a
mineral spring with elevated sodium, calcium, or magnesium salts. It is
broader: elevated salts do not necessarily meet the hypersaline qualifier.
Current ENVO search for hypersaline spring returned no result; that bounded
check is not proof of absence from all ontologies. No exact mapping is
justified by the inspected candidate.
[Salt spring](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001893).

The inherited `habitatmech:GOLD.ce244e62cd` parent is the maintained inland
saline-or-alkaline aquatic environment, not a salinity quality. Its complete
record and definition at `curation/term_requests.tsv:43` were inspected.
The saline spring fits the saline arm without implying alkalinity. This
is the GOLD parent-path relation, not an ENVO-asserted edge.

`curation/decisions.tsv:396` is the CLASS-level no-match decision and
explicitly does not claim ITEM-level habitathood assessment. The current
history and `SEEDED` status represent that distinction correctly.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:1566` contains the exact path
`Environmental > Aquatic > Non-marine Saline and Alkaline > Hypersaline spring`,
nodes `gold.ecosystem:8481|gold.ecosystem:8482`, and zero organism, study,
biosample, and total assertions. The generated record correctly displays
the first node with the two-node note and omits a positive assertion count.
The separate sediment child is not merged or counted into this record.

Complete exact-path scans of the GOLD biosample, triad, and study TSVs found
no target row. This is absence from these committed snapshots, not absence
of microbes or studies in hypersaline springs.

The inspected Perreault et al. study documents microbial communities from
seven cold saline springs and brines saltier than ocean water. It supports
the habitat interpretation but does not link those sites to GOLD nodes 8481
or 8482. Its temperatures, chemistry, taxon abundances, and inferred sulfur
metabolism cannot become universal assertions here.
[PMID:17220254, abstract via Europe PMC](https://europepmc.org/article/MED/17220254),
[DOI:10.1128/AEM.01729-06](https://doi.org/10.1128/AEM.01729-06).

## Completeness

Ignored-inclusive searches covered ID, label, stem, source inventories,
curation, history, research, configuration, path lock, and review reports.
Only the CLASS decision and incidental parent/sibling mentions were found;
no target definition, overlay, session history, PREGO/Madin/parameter
association, or prior exact-target review was found in those locations.

Optional quantitative fields and mechanisms should remain empty rather than
inherit properties of a particular Arctic spring. An ITEM assessment and
definition are useful future curation, not evidence that the present
explicitly seeded assertions are false. iModulonDB is not applicable because
the record names no gene, pathway, regulator, or organism-specific mechanism.

## Findings

None found. Zero blockers, major findings, or minor findings. The review does
not claim that the source inventory's zero counts exhaust real-world evidence.

## Recommended Edits

None required for the current representation. Future curation may evaluate
salt spring as a broader parent and define the hypersaline qualifier through
`curation/decisions.tsv` and `curation/term_requests.tsv`, preserving the
minted identity unless an actual exact match is established.

## Follow-up Checks

Recheck full GOLD paths and current candidate definitions during refresh.
Any curation requires append-only history, a seeder canary, strict validation,
corpus reproduction, applicable ontology-product validation, semantic-map/site
freshness, and full QC. Never hand-edit the generated record or transfer
sample-specific literature values into generic fields.

## Additional Notes

The read-only report changes no curation status, source inventory, corpus,
generated product, or historical artifact. The existing acidic/alkaline
spring reviews concern other source paths and are not this target's review.
