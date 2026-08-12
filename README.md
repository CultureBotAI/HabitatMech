# HabitatMech

Knowledge base of **microbial habitats and environments**, harmonized from the
three source vocabularies that describe where microbes are found and grounded
in ENVO / UBERON / FOODON / BTO.

HabitatMech is the habitat counterpart of
[TraitMech](https://github.com/CultureBotAI/TraitMech) (traits),
[CultureMech](https://github.com/CultureBotAI/CultureMech) (growth media),
[MediaIngredientMech](https://github.com/CultureBotAI/MediaIngredientMech)
(ingredients), and [CommunityMech](https://github.com/CultureBotAI/CommunityMech)
(communities), and follows the curation pattern established by
[dismech](https://github.com/monarch-initiative/dismech): one YAML per entity,
ontology-grounded, evidence-backed, schema-validated, curated incrementally.

## The problem it solves

The same habitat has three different names depending on who is describing it:

| Source | How it names marine sediment |
|---|---|
| JGI GOLD | `Environmental > Aquatic > Marine > Sediment` (5-level ecosystem path) |
| BacDive | `Marine-sediment` (flat isolation-source label) |
| PREGO | `ENVO:00002113` (ontology CURIE) |

Each becomes a *source concept*. Every source concept is resolved to an
identifier — an ontology CURIE where one is defensible, otherwise a minted,
content-hashed `habitatmech:` CURIE — and source concepts resolving to the same
identifier merge into one `HabitatRecord` carrying all their attestations.

That merge is the product. `data/habitats/terrestrial/soil.yaml` is one record
grounded in `ENVO:00001998` that knows GOLD saw 26,399 organisms there, PREGO
associates 8,715 taxa with it, and kg-microbe's environment table says it is
structurally complex, low-pressure, and strongly gradient-forming.

## Current corpus

Seeded from kg-microbe, 2026-08-12. **3,299 habitat records** from 3,443 source
concepts (GOLD 2,562 · BacDive 162 · PREGO 719).

| Category | Records | | Grounding | Records |
|---|---:|---|---|---:|
| HOST_ASSOCIATED | 1,681 | | EXACT | 954 |
| ENGINEERED | 491 | | NARROW | 883 |
| AQUATIC | 462 | | CLOSE | 134 |
| TERRESTRIAL | 321 | | UNGROUNDED | 1,315 |
| OTHER | 251 | | NOT_APPLICABLE | 13 |
| FOOD | 67 | | | |
| CLINICAL | 16 | | | |
| AIR | 10 | | | |

Identifiers: 500 ENVO, 399 BTO, 124 UBERON, 42 FOODON, 23 other, and 2,211
minted. 128 records are attested by more than one source; 21 by all three.

**Everything is `mapping_status: SEEDED` — nothing here has been curator-reviewed
yet.** The lexical grounding routes are unverified by construction. Run
`just report` for the live numbers.

## Quick start

```bash
just install                        # uv sync --extra dev
just report                         # corpus stats: grounding, categories, backlog
just validate-all                   # closed-mode schema validation of every record
just test                           # unit + corpus-integrity tests
```

Re-seeding is only needed when the upstream data changes:

```bash
just extract-inventory-dry          # what extraction would produce (no writes)
just extract-inventory              # refresh data/raw/ from a kg-microbe checkout
just seed                           # dry-run: harmonization report, no writes
just seed-canary ENVO:00001998      # write ONE record and check it, first
just seed-apply --force             # rewrite the corpus
just seed-apply --force --prune     # ...and clean up files left by a category move
```

`just extract-inventory` is the only step that needs a local
[kg-microbe](https://github.com/Knowledge-Graph-Hub/kg-microbe) checkout; point
`KG_MICROBE_ROOT` or `conf/sources.yaml` at it. The derived inventories in
`data/raw/` are committed, so seeding, validation, and tests run without it.

Filenames are pinned by `data/habitats/PATHS.tsv` (identifier → slug), so a
re-seed never renames an existing record just because the corpus grew around
it. **To rename a record, edit its slug there and re-seed** — never rename the
file directly, or the seeder will recreate it under the pinned name and two
files will claim one identifier.

## Schema

`src/habitatmech/schema/habitatmech.yaml` defines **HabitatRecord**, one per
YAML file:

- **Identity** — `identifier`, `label`, `definition`, `definition_source`,
  `synonyms`, `parent_habitats`, `xrefs`, `habitat_category`.
- **`source_attestations`** — the harmonization layer. One entry per upstream
  vocabulary, with `source_id`, `source_label`, GOLD's full `source_path`,
  the `mapping_predicate` relating it to this record, and `assertion_count`
  paired with `assertion_unit` (GOLD counts organisms, BacDive strains, PREGO
  taxa — the numbers are **not summable across sources**).
- **`environmental_parameters`** — physicochemical bands (salinity, pH,
  temperature, pressure, water availability, and their variability).
- **`characteristic_taxa`** — associated taxa with counts and scores.
- **`causal_graphs`** — the "Mech" half: evidence-backed mechanism graphs
  linking a habitat's conditions to the adaptations they select for. Unlike the
  seeded descriptive fields, **every causal edge must carry a citation**.
- **`grounding_status`** and **`mapping_status`**, kept deliberately separate:
  the first is how well the identifier fits, the second is curatorial review.
  A record can be REVIEWED and still honestly UNGROUNDED.
- **`discussions`** / **`datasets`** from the shared `mech_shared` module,
  vendored byte-identical across the Mech repos.

## How grounding works

PREGO concepts are already ENVO/BTO CURIEs and ground to themselves.

BacDive concepts go through kg-microbe's curated
`isolation_source_to_ontology.tsv`, which has a row for all 162 sources. An
empty target is an upstream curator's deliberate refusal to ground, and is
honoured as UNGROUNDED rather than re-guessed. A target in a non-habitat
ontology is kept as an xref and marked NOT_APPLICABLE — "Acidic" maps to
`PATO:0001429`, and a quality is a property of a habitat, not a habitat.

GOLD has no upstream mapping table, so its concepts are matched lexically
against the vendored ontology labels and synonyms, in this order:

1. the **composed label** from the last two path levels ("marine sediment") —
   an exact hit is EXACT, because the path context is included;
2. the **leaf label alone**, when this path is the *shallowest* one ending in
   that leaf. Ten GOLD paths end in "Soil"; the depth-3
   `Environmental > Terrestrial > Soil` is what ENVO means by soil, so it
   claims `ENVO:00001998` and the rest do not;
3. the **leaf label when another path claims it, or when several tie at the
   shallowest depth** — the concept gets a minted identifier, `NARROW`
   grounding, and the matched term as a parent. This is the anti-conflation
   rule: `...Marine > Sediment` and `...Freshwater > Sediment` are different
   habitats, and grounding both to `ENVO:00002007` would merge their
   attestations into one record;
4. the isolation-source mapping table, keyed on the leaf label;
5. nothing — minted identifier, `UNGROUNDED`.

`just report` ranks the ungrounded records by upstream assertion volume; that
list is the ENVO term-request backlog. The current top entries — "Fecal",
"Roots", "Sputum/Phlegm", "Meat products" — are mostly groundable with a little
curation.

## Known limitations

These are real and unfixed; see the issue tracker.

- **Nothing is reviewed.** All 3,299 records are `SEEDED`. Lexical matches are
  plausible, not verified.
- **PREGO scores barely discriminate.** For soil, all 8,715 taxa score between
  4.000 and 4.007, so the "top 25" kept in `characteristic_taxa` is close to
  arbitrary among the ties. Treat seeded taxa as "reported from", not
  "characteristic of" — which is why `is_characteristic` is a separate,
  curator-set flag.
- **BacDive contributes no taxa.** Linking isolation sources to taxa requires a
  join through strain records that the current extraction does not do.
- **Only 29 records carry environmental parameters.** Most rows in the upstream
  table describe compound environments (`sediment_marine_cold` = ENVO sediment
  + PATO cold) that no single term denotes, and are skipped rather than
  misattributed.
- **PO and PCO are not vendored**, so plant-structure habitats like "Roots"
  stay ungrounded even though `PO:0009005` exists.
- **`OTHER` holds 251 records** whose category the ENVO-anchor heuristic could
  not infer.

## Layout

```
HabitatMech/
├── conf/sources.yaml                     # where kg-microbe lives
├── data/
│   ├── raw/                              # committed inventories + MANIFEST.yaml
│   └── habitats/
│       ├── PATHS.tsv                     # identifier -> slug, pins filenames
│       └── <category>/<slug>.yaml        # 3,299 HabitatRecords
├── src/habitatmech/
│   ├── schema/habitatmech.yaml           # LinkML schema
│   ├── schema/mech_shared.yaml           # vendored, sha-pinned shared module
│   ├── validation/write_validated.py     # write-time closed-schema gate
│   └── curate/curation_event.py          # append-only audit trail helper
├── scripts/
│   ├── extract_source_inventory.py       # kg-microbe -> data/raw/
│   ├── seed_from_sources.py              # data/raw/ -> data/habitats/
│   ├── validate_strict.py                # closed-mode corpus validation
│   └── habitat_report.py                 # corpus stats and curation backlog
└── tests/
```

## Sources

- **GOLD** — [JGI Genomes OnLine Database](https://gold.jgi.doe.gov/) ecosystem classification
- **BacDive** — [DSMZ BacDive](https://bacdive.dsmz.de/) isolation sources
- **PREGO** — [PREGO](https://prego.hcmr.gr/) habitat-organism associations
- **ENVO / UBERON / FOODON / BTO** — via
  [kg-microbe](https://github.com/Knowledge-Graph-Hub/kg-microbe), which
  supplies all of the above in harmonized KGX form and contributes the curated
  isolation-source mapping table

## License

CC0-1.0. See [LICENSE](LICENSE).
