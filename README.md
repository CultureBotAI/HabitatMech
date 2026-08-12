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

Seeded from kg-microbe, 2026-08-12. **3,284 habitat records** from 3,443 source
concepts (GOLD 2,562 · BacDive 162 · PREGO 719).

| Category | Records | | Grounding | Records |
|---|---:|---|---|---:|
| HOST_ASSOCIATED | 1,675 | | EXACT | 962 |
| ENGINEERED | 490 | | NARROW | 884 |
| AQUATIC | 461 | | CLOSE | 134 |
| TERRESTRIAL | 321 | | UNGROUNDED | 1,278 |
| OTHER | 244 | | NOT_APPLICABLE | 23 |
| FOOD | 67 | | BROAD | 3 |
| CLINICAL | 16 | | | |
| AIR | 10 | | | |

135 records are attested by more than one source; 26 by all three.

**55 records (1.7%) are `REVIEWED`; the other 3,229 are `SEEDED`** — machine-generated
and unverified. Of the 1,278 still ungrounded, 23 have been curator-confirmed as
real habitats with no term that fits (the ENVO term-request list) and the rest
are undecided backlog. Run `just report` for the live numbers and both lists.

## Quick start

```bash
just install                        # uv sync --extra dev
just report                         # corpus stats: grounding, categories, backlog
just validate-all                   # closed-mode schema validation of every record
just verify-corpus                  # check data/habitats/ is what data/raw/ produces
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

`just report` ranks the ungrounded records by upstream assertion volume and
splits them into curator-confirmed term requests and undecided backlog. The
first curation pass cleared the whole head of that distribution — "Fecal",
"Sputum/Phlegm", "Roots", "Meat products" and the rest of the top 60 are now
decided — so the largest undecided entry is down from 40,432 upstream
assertions to 261.

## Curation

Records are generated, and `just verify-corpus` gates that they reproduce
exactly from `data/raw/` — so **curation is never a hand-edit to a record**, which
the next re-seed would silently revert. Decisions live in
[`curation/decisions.tsv`](curation/decisions.tsv), which the seeder reads as an
input. A curation pass is therefore a small reviewable diff in one file, every
decision carries its curator, date and reason, and the corpus stays reproducible.

Four decisions are available, each keyed on the **minted identifier of one
source concept** (a content hash of the GOLD path or BacDive id, so it survives
an upstream refresh):

| Decision | Meaning |
|---|---|
| `GROUND` | Redirect this source concept onto an ontology term. It merges with anything else resolving there. |
| `NOT_APPLICABLE` | Not a habitat at all — a host taxon, a disease process, a temperature band. Keeps its minted id so it stays citable. |
| `CONFIRM_UNGROUNDED` | A real habitat with no term that fits. May name a nearest-*broader* term, attached as a parent rather than adopted as identity. This is the ENVO term-request list. |
| `REVIEW` | The curator checked the seeder's own answer and endorsed it. |

**Every target is verified at seed time.** A `GROUND` must name both the CURIE
and the label it expects, and the seed fails unless the term exists in the
vendored ontology slice *and* its label matches. An invented term ID cannot
pass, and neither can a real ID paired with the wrong concept — which is the
failure mode that matters when a curation pass is LLM-assisted.

A merged record is `REVIEWED` only when **every** source concept feeding it has
been decided. A record aggregating GOLD, BacDive and PREGO is not checked until
all three have been looked at.

```bash
just worklist                 # the backlog, ranked, with candidate terms
just report                   # term requests vs undecided, and the numbers below
```

## Known limitations

These are real and unfixed; see the issue tracker.

- **Almost nothing is reviewed.** 55 of 3,284 records are `REVIEWED`; the rest
  are `SEEDED`, meaning their lexical matches are plausible but unverified.
- **ENVO has no host-clade environment terms.** "Mammals: Human" (40,432 GOLD
  organisms, the single largest ungrounded concept), "Birds", "Fish", "Insects"
  and the rest are real habitats with only `ENVO:01001002 animal-associated
  environment` above them. They are deliberately *not* grounded there: every
  host clade would merge onto one record and the host distinction is the entire
  content. They are the highest-value term requests.
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
