---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T03:55:20.071112'
end_time: '2026-08-18T04:04:28.224966'
duration_seconds: 548.15
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Grains/Grain products
  habitat_identifier: habitatmech:GOLD.c25f588dad
  habitat_category: FOOD
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Engineered > Food production > Grains/Grain products'
  assertions: '0'
  parent_terms: FOODON:03530206
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. The proposal
    offered ENVO:01003002 particle via the synonym grain, which is a different sense
    of the word. No cereal-grain habitat term in the slice. Term request. Path: Engineered
    > Food production > Grains/Grain products (source concept habitatmech:GOLD.c25f588dad)'
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 11
  num_turns: 31
  total_cost_usd: 2.970324
  session_id: b4435ee7-355d-402e-bcf5-9feedea8d19b
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 25
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Grains/Grain products
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.c25f588dad
- **Category:** FOOD
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Engineered > Food production > Grains/Grain products
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** FOODON:03530206
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. The proposal offered ENVO:01003002 particle via the synonym grain, which is a different sense of the word. No cereal-grain habitat term in the slice. Term request. Path: Engineered > Food production > Grains/Grain products (source concept habitatmech:GOLD.c25f588dad)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Grains/Grain products** as a microbial habitat, with citations.

This is a definition for an ontology term, not a literature review. The output is judged
on whether a curator can write one defensible sentence from it and cite the sources.

## Required findings

### 1. What the concept denotes

State what physical place, material or setting the label refers to **as a habitat for
microorganisms** — the thing a sample is taken from. Be explicit about the boundary: what
is inside the concept and what is a neighbouring concept.

If the label is ambiguous, say so and give the readings. Do not pick one silently. The
source path above is the strongest evidence of which reading the data means.

### 2. Genus — the broader kind

Name the smallest well-established kind this concept falls under, and say whether an
existing ontology term expresses it (give the CURIE if so). The genus is what the
definition will start from: "A ⟨genus⟩ which ...".

Check ENVO in particular before concluding nothing fits. Report the near-misses and why
each fails — a term that is *narrower* than the concept, or that asserts something the
sources do not, is a near-miss worth recording, not a match.

### 3. Differentia — what distinguishes it

What separates this concept from its siblings under that genus. Prefer properties that
are observable or measurable: physical setting, dominant material, host, formation
process, characteristic physicochemistry.

### 4. Sources

Every claim above needs a citation — a DOI, PubMed ID, or a resolvable URL. Prefer:

- primary literature describing the habitat and its microbial communities
- standards and reference vocabularies (MIxS, GSC, ENVO, SNOMED, AGROVOC)
- authoritative reference works

Say plainly when a claim is your inference rather than something a source states. An
unsupported sentence in a definition is worse than a missing one, because it is
indistinguishable from a supported one once it is in the ontology.

### 5. Synonyms and what NOT to conflate

List names in real use for this concept, and separately list terms that are commonly but
wrongly treated as the same thing.

### 6. Whether it should be a term at all

Say so if the evidence suggests this is not a habitat — a process, a quality, a disease
state, an organism as a taxonomic grouping, or a sampling artefact. That is a useful
answer and the corpus has an established disposition for it. Do not manufacture a
definition for something that should not have one.

## Output format

Plain markdown. Lead with a single proposed definition sentence of the form

> A ⟨genus⟩ which ⟨differentia⟩.

then the supporting sections. Keep the proposed definition to one sentence; if it needs
more, that usually means an intermediate class is missing, and saying so is more useful
than a longer sentence.


## Output

# Definition research: **Grains/Grain products** (`habitatmech:GOLD.c25f588dad`)

> **A cereal grain food product which consists of the whole harvested caryopses of cereal or pseudocereal plants, or of the milling, dehulling and rolling fractions derived from them, held as a bulk commodity between harvest and consumption.**

---

## ⚠️ Read this before writing the definition: the "no term in the slice" premise is wrong

The recorded curation note says:

> "No cereal-grain habitat term in the slice."

**That is not correct.** `FOODON:00001093` **cereal grain food product** is present in the vendored slice:

```
data/raw/ontology_terms.tsv
FOODON:00001093	FOODON	cereal grain food product	(no definition)	(no synonyms)	FALSE	FALSE
```

It is non-deprecated, not `label_only`, and it carries hierarchy in the vendored edge table:

```
data/raw/ontology_subclass_edges.tsv
FOODON:00001093  rdfs:subClassOf  FOODON:00001173   # plant seed food product
FOODON:00001917  rdfs:subClassOf  FOODON:00001093   # grain based bakery food product
FOODON:00001173  rdfs:subClassOf  FOODON:03460177   # plant seed or nut food product
```

What the automated proposal actually did was offer `ENVO:01003002` **particle** via its synonym *grain* — the mineralogical sense. The curator correctly rejected that, but then generalised from one bad proposal to "nothing in the slice fits", without checking. The FoodOn `<X> food product` grouping classes were never inspected.

**The corpus already has the exact structural precedent.** GOLD's sibling node `Engineered > Food production > Dairy products` is grounded `EXACT` to `FOODON:00001256` *dairy food product* (`data/habitats/food/dairy_food_product.yaml:1`). GOLD `<X> products` → FoodOn `<X> food product` is an established, reviewed pattern in this repo, applied to Meat products, Dairy products, Egg products, Spices and Nuts.

**Recommendation: this is a `GROUND` decision, not a term request.** See §6 for the exact decision row and the one caveat (FoodOn supplies no textual definition for `FOODON:00001093`).

Sources for the slice claims are the repo files themselves; the FoodOn term is independently confirmed at [OLS4 / FOODON_00001093](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:00001093) and in the [FoodOn food-product hierarchy](https://foodon.org/food-facets/food-product/) (FoodOn: [Dooley et al. 2018, *npj Science of Food* 2:23, doi:10.1038/s41538-018-0032-6](https://doi.org/10.1038/s41538-018-0032-6)).

---

## 1. What the concept denotes

**The thing a sample is taken from:** a quantity of harvested cereal grain, or of material milled or otherwise derived from it, in the post-harvest food/feed chain — the contents of a grain bin, a silo drawdown sample, a truck lot at intake, a sack of flour, a bag of rolled oats, a bran or semolina milling fraction. A sample is a scoop of kernels or a scoop of powder; the assay recovers the community living on the kernel surface (epiphytic) and inside the pericarp, aleurone and endosperm (endophytic) ([Solanki et al. 2021, *J Fungi* 7:781, doi:10.3390/jof7090781](https://doi.org/10.3390/jof7090781)).

**The source path is decisive about the reading.** `Engineered > Food production > Grains/Grain products` sits under GOLD's *Engineered* top-level ecosystem, which classifies human-built and human-managed systems, not the field. GOLD's five-level ecosystem classification and the placement of `Engineered` are described in [Mukherjee et al. 2023, *Nucleic Acids Research* 51:D957–D963, doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974) (and v.10, [doi:10.1093/nar/gkae1000](https://doi.org/10.1093/nar/gkae1000)). So this is **grain as a stored/processed commodity**, not grain on the plant.

### Inside the concept
- Whole harvested kernels of wheat, rice (paddy and milled), maize, barley, oat, rye, sorghum, millet, triticale
- Pseudocereal grains conventionally counted as grain — buckwheat, amaranth, quinoa (FoodOn's CCPR-derived `020 cereal grains` explicitly includes buckwheat and *Chenopodium*: [FOODON:03400683](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03400683))
- Milling and processing fractions that are still recognisably grain material: flour, meal, semolina, bran, germ, polished/husked rice, rolled flakes
- Grain lots destined for feed as well as for human food (FoodOn's `food product`, `FOODON:00001002`, is defined as "Food material for **humans and animals**")

### Outside the concept — neighbouring GOLD nodes with their own records
| Neighbour | Why it is separate |
|---|---|
| `Engineered > Food production > Bread production` / `> Bread` | Baked; a distinct fermented/thermally-processed substrate (`FOODON:03000288`, `data/habitats/food/bread.yaml`) |
| `Engineered > Food production > Sourdough` | An actively fermenting flour–water community, not the flour |
| `Engineered > Food production > Fermented beverages` | Malt/mash/wort; ENVO models the site as `ENVO:00003885` brewery |
| `Engineered > Food production > Silage fermentation` | Deliberately rehydrated and anaerobically fermented; rehydrated corn/sorghum grain silage is the genuine boundary case ([Carvalho et al. 2022, PMC9546842](https://pmc.ncbi.nlm.nih.gov/articles/PMC9546842/)) |
| `Engineered > Food production > Nuts`, `> Plant products`, `> Bean` | Sibling plant commodities; not caryopses |
| Environmental > Terrestrial > agricultural field; plant-associated seed | The grain *on the plant*, pre-harvest — a plant-associated habitat, not an engineered one |
| `ENVO:02000107` grain dust | The aerosolised fraction generated by handling grain, not the grain |
| `ENVO:00003869` straw | The stalk *after the grain has been removed* — the complement |
| Silos, bins, elevators, mills (`ENVO:00003863` food processing building) | The containing structure, a site not a material |

### Ambiguity in the label
Three readings exist; only one is live here.
1. **Cereal caryopsis / grain commodity** — the intended reading, fixed by the `Food production` path. ✅
2. **Granular particle** (mineral grain, sand grain, grain of snow) — `ENVO:01003002` *particle* carries `grain` as a synonym; this is the sense that produced the bad proposal. ❌
3. **Grain as a unit of mass** (64.79 mg) — irrelevant. ❌

The `/` in "Grains/Grain products" bundles the raw commodity with its derived products in one node. That is a real breadth the definition has to carry; it is not two concepts, because GOLD gives it one identifier and (as of this extraction) no children.

---

## 2. Genus — the broader kind

**Recommended genus: `FOODON:00001093` *cereal grain food product*** — present in the slice, correct level of generality, and its own parent chain (`plant seed food product` → `plant seed or nut food product` → ... → `food product`) is coherent.

If a lower-risk, definition-bearing genus is preferred for a minted term, the next one up with a real definition is **`FOODON:00001015` *plant food product*** — *"A food product which has as a defining ingredient some plant material."* (in slice, with definition). This is the genus already used as `parent_habitats` on `data/habitats/food/fruit_seed.yaml`.

### ENVO: checked, nothing fits

I searched ENVO exhaustively for `grain` via [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo) and grepped the vendored slice. ENVO has **no food-commodity branch at all** — its food-adjacent terms are either *sites* (bakery, brewery, grocery store, food processing building, the `ENVO:035013xx` food-production monitoring zones) or *feed/waste* materials. Near-misses and why each fails:

| Term | Why it fails |
|---|---|
| `ENVO:01003002` **particle** — "A mass of solid material which is either 1) a minute fragment of a larger mass or 2) one of a collection of small masses composing an aggregate." | Different sense of *grain* entirely; its sibling terms are `particle of sand`, `particle of silt`, `grain of desert sand`. The curator was right to reject it. |
| `ENVO:02000107` **grain dust** — "Dust that comes from grain and all the other substances associated with its cultivation & harvesting." | *Narrower and derived*: the airborne fraction, not the commodity. Good `xref` candidate; not a genus, not a parent. |
| `ENVO:02000047` **animal feed** — "Food material which can be used to meet nutritional requirements of animals, particularly livestock..." | Asserts a **use role** GOLD does not claim, and excludes human-food grain. Covers only part of the concept. `xref` at most. |
| `ENVO:02000055` **plant feed** — "Food material which can be used to meet nutritional requirements of **plants**." | Label collision only; this is plant nutrition. Not relevant. |
| `ENVO:00003869` **straw** — "the dry stalk of a cereal plant, **after the nutrient grain or seed has been removed**" | The explicit complement of this concept. |
| `ENVO:00003863` food processing building; `ENVO:03864` bakery; `ENVO:00003885` brewery; `ENVO:03501313` food production environmental monitoring zone | Sites/facilities, not material entities. A wrong genus category, not a near-miss on breadth. |
| `BTO:0000668` **kernel** — "The inner softer part of a seed, fruit stone, or nut"; `BTO:0003365` germinated grain (green malt); `BTO:0000057` aleurone layer | Plant-anatomy terms, each narrower than a grain lot and none denoting a commodity. |
| `FOODON:03301941` **cereal grain**, `FOODON:03301760` **cereal grain (unprocessed)** | Genuinely good terms — *"whole, natural shape, not heat-treated, seed (anatomical part)"* — but **not in the vendored slice**, and both are **narrower**: they exclude the "/Grain products" half (flour, bran, rolled flakes). Vendoring one of these would *not* solve the node. |

**Note on the repo's parts-vs-whole rule (CLAUDE.md).** It does not bite here. A cereal grain is a plant part, not a whole host organism, and the concept as GOLD means it is a detached commodity rather than an organ in a living plant — so grounding to a food-product class is the right move, and no `<X>-associated environment` term is wanted.

---

## 3. Differentia — what distinguishes it

The differentia that separate this from its siblings under *plant food product* / *food product*, in decreasing order of definitional weight.

**(a) Dominant material — a caryopsis, a dry dormant seed.** This is the compositional differentia and the one that belongs in the sentence. It separates grain from `Meat products`, `Dairy products`, `Fish products`, `Nuts`, `Fermented vegetables` and the other GOLD food siblings.

**(b) Two structurally distinct compartments.** Unlike a homogenised food, a grain lot presents an epiphytic (kernel surface) and an endophytic (pericarp/aleurone/endosperm) niche that differ significantly in composition. In 27 stored Israeli wheat samples (63,108 bacterial + 114,849 fungal OTUs), α-diversity was higher epiphytically for both bacteria and fungi (p = 0.001); endophytic bacteria were led by *Pantoea* (7.5%), *Bacillus* (4.9%), *Burkholderia* (4.0%), epiphytic by *Pantoea* (20.3%), *Sphingomonas* (10.2%), *Massilia* (8.5%), *Pseudomonas* (8.1%); endophytic fungi by *Alternaria* (76.8%) and *Stemphylium* (11.8%), epiphytic by *Alternaria* (50.3%), *Cladosporium* (10.5%), *Sporobolomyces* (9.5%) ([Solanki et al. 2021, doi:10.3390/jof7090781](https://doi.org/10.3390/jof7090781)). Milling collapses this distinction — a real internal heterogeneity of the concept.

**(c) Characteristic physicochemistry — low water activity is the master variable.** Growth is governed by a_w rather than total moisture, because water bound to starch and protein is unavailable to microbes. The overall microbial growth limit is ≈ 0.65 a_w; most field fungi and bacteria need > 0.95 a_w; storage fungi grow from ≈ 0.70 a_w and accelerate toward 0.90 ([Magan & Aldred 2007, *J Stored Prod Res*, doi:10.1016/j.jspr.2006.08.006](https://doi.org/10.1016/j.jspr.2006.08.006); [Mannaa & Kim 2017, *Mycobiology* 45:240–254, PMC5780356](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5780356/); [K-State, *Molds and Mycotoxins in Stored Products*](https://entomology.k-state.edu/doc/finished-chapters/s156-6.pdf)). Corresponding safe moisture contents at 25 °C are ≈ 13.0% for rice grain, 10.7% for wheat flour and 10.5% for corn flour ([Abdullah et al. 2000, *J Stored Prod Res* 36:47–54, doi:10.1016/S0022-474X(99)00026-0](https://doi.org/10.1016/S0022-474X(99)00026-0)). This differentia distinguishes grain sharply from the wet food siblings (raw milk, raw meat, fermented vegetables) and explains why grain is a *survival* rather than a *growth* habitat for most bacteria.

**(d) Formation process — a managed post-harvest succession.** The classic field-fungi/storage-fungi dichotomy (Christensen and colleagues) holds: *Alternaria*, *Cladosporium*, *Fusarium* and *Helminthosporium* colonise in the field and die back or go quiescent on drying; *Aspergillus*, *Eurotium* and *Penicillium* are scarce at harvest and dominate the dried bulk, particularly at hot spots created by moisture migration within a bin ([Magan & Aldred 2007](https://doi.org/10.1016/j.jspr.2006.08.006); [Hanson et al. 2005, *J Agric Food Chem*, doi:10.1021/jf050821t](https://doi.org/10.1021/jf050821t); [Mannaa & Kim 2017](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5780356/)). Both groups co-occur in surveys — a Tunisian wheat survey recovered *Alternaria* 70.8%, *Eurotium* 62.5%, *Aspergillus* 54.2%, *Penicillium* 41.7% ([Lahouar et al. 2018, PMC6088110](https://pmc.ncbi.nlm.nih.gov/articles/PMC6088110/)).

**(e) Partly inherited community.** A restricted subset of grain-associated taxa is vertically transmitted seed-to-seed; in rice, vertical transmission accounted for 25.5% of seed bacteria versus 10.7% acquired from the rhizosphere ([Kim & Lee 2023, "The seed microbiomes of staple food crops", PMC10686132](https://pmc.ncbi.nlm.nih.gov/articles/PMC10686132/); [Abdelfattah et al. 2023, *Trends Microbiol*, doi:10.1016/j.tim.2022.12.006](https://doi.org/10.1016/j.tim.2022.12.006)). This is what makes grain distinct from a purely environmentally-inoculated food matrix.

**(f) Consequential outputs — mycotoxins and desiccation-tolerant pathogens.** Grain is the principal food-chain source of aflatoxins, ochratoxin A, deoxynivalenol, zearalenone and fumonisins; post-harvest losses from mould spoilage and mycotoxin contamination run at 5–10% even in developed countries ([Magan & Aldred 2007](https://doi.org/10.1016/j.jspr.2006.08.006)). On the products side, enteric pathogens cannot grow at flour's a_w but persist for extraordinary periods: STEC O121 in naturally contaminated flour showed no significant viability decline between 6 months and 2 years, at outbreak-relevant levels of 0.15–0.44 MPN/100 g ([Forghani et al. 2019, *J Food Prot* 82:1289–1296, PMID 31310172](https://pubmed.ncbi.nlm.nih.gov/31310172/); [Crowe et al. 2017, *NEJM* 377:2036–2043, doi:10.1056/NEJMoa1615910](https://doi.org/10.1056/NEJMoa1615910) — 63 patients, 24 states, 2016 US flour outbreak).

**Recent primary data (2024):** 99 rice-grain samples from three Chinese producing regions yielded 6,019,722 ITS reads and 2,014 effective fungal ASVs, with community assembly dominated by deterministic processes and significant regional differentiation ([Zhang et al. 2024, *Agronomy* 14:1681, doi:10.3390/agronomy14081681](https://doi.org/10.3390/agronomy14081681)).

**Standards support that this is a recognised sampling context:** the GSC's MIxS food extensions include **`food-human foods`** and **`food-animal feed`** alongside `food-farm environment` and `food-food production facility` (MIxS ≥ 6.1, LinkML-based; [MIxS documentation](https://genomicsstandardsconsortium.github.io/mixs/), [FoodFoodProductionFacility MIXS:0016021](https://genomicsstandardsconsortium.github.io/mixs/0016021/), [v6.3.0 on Zenodo](https://zenodo.org/records/18511302)). A stored grain lot is sampled under `food-human foods` / `food-animal feed`, not under a farm or facility package — which is independent confirmation that the *material*, not the *site*, is the habitat here.

---

## 4. Sources

Grouped, with what each supports.

**Ontology / vocabulary**
- FoodOn: [Dooley et al. 2018, *npj Science of Food* 2:23, doi:10.1038/s41538-018-0032-6](https://doi.org/10.1038/s41538-018-0032-6); [food-product hierarchy](https://foodon.org/food-facets/food-product/); terms via OLS4 — [FOODON:00001093](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:00001093), [FOODON:03301941](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03301941), [FOODON:03400683](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03400683)
- GOLD ecosystem classification: [Mukherjee et al. 2023, *NAR* 51:D957, doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974); v.10 [doi:10.1093/nar/gkae1000](https://doi.org/10.1093/nar/gkae1000)
- MIxS food extensions: [GSC MIxS](https://genomicsstandardsconsortium.github.io/mixs/), [MIXS:0016021](https://genomicsstandardsconsortium.github.io/mixs/0016021/), [MIxS 6.3.0, Zenodo, Feb 2026](https://zenodo.org/records/18511302)
- ENVO terms as quoted from the vendored slice `data/raw/ontology_terms.tsv` and cross-checked at [OLS4/ENVO](https://www.ebi.ac.uk/ols4/ontologies/envo)

**Grain microbiome (primary)**
- [Solanki et al. 2021, *J Fungi* 7:781, doi:10.3390/jof7090781, PMID 34575819](https://doi.org/10.3390/jof7090781) — stored wheat, epiphyte/endophyte, all OTU and taxon percentages in §3(b)
- [Zhang et al. 2024, *Agronomy* 14:1681, doi:10.3390/agronomy14081681](https://doi.org/10.3390/agronomy14081681) — rice grain fungal survey
- [Kim & Lee 2023, "The seed microbiomes of staple food crops", PMC10686132](https://pmc.ncbi.nlm.nih.gov/articles/PMC10686132/) — wheat/rice/maize seed microbiome review, 25.5% vs 10.7% figure
- [Abdelfattah et al. 2023, *Trends Microbiol* 31:346–355, doi:10.1016/j.tim.2022.12.006](https://doi.org/10.1016/j.tim.2022.12.006) — seed-to-seed inheritance
- [Carvalho et al. 2022, PMC9546842](https://pmc.ncbi.nlm.nih.gov/articles/PMC9546842/) — rehydrated corn/sorghum grain silage (the boundary case)

**Storage ecology, spoilage, mycotoxins**
- [Magan & Aldred 2007, *J Stored Prod Res* 43:341, doi:10.1016/j.jspr.2006.08.006](https://doi.org/10.1016/j.jspr.2006.08.006) — a_w thresholds, hot spots, 5–10% loss figure
- [Mannaa & Kim 2017, *Mycobiology* 45:240–254, PMC5780356](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5780356/) — temperature × a_w and mycotoxin production
- [Abdullah et al. 2000, *J Stored Prod Res* 36:47, doi:10.1016/S0022-474X(99)00026-0](https://doi.org/10.1016/S0022-474X(99)00026-0) — safe moisture contents
- [Hanson et al. 2005, *J Agric Food Chem*, doi:10.1021/jf050821t](https://doi.org/10.1021/jf050821t) — field vs storage fungi, functional consequences
- [Lahouar et al. 2018, PMC6088110](https://pmc.ncbi.nlm.nih.gov/articles/PMC6088110/) — Tunisian wheat mycoflora frequencies
- [K-State S156 ch.6, *Molds and Mycotoxins in Stored Products*](https://entomology.k-state.edu/doc/finished-chapters/s156-6.pdf) — reference chapter. **Caution:** its a_w values are printed as "65 aw", "70 aw", "95 aw"; read as 0.65/0.70/0.95. Prefer the peer-reviewed sources above for any number you cite.

**Grain products / low-a_w pathogens**
- [Crowe et al. 2017, *NEJM* 377:2036, doi:10.1056/NEJMoa1615910](https://doi.org/10.1056/NEJMoa1615910)
- [Forghani et al. 2019, *J Food Prot* 82:1289, PMID 31310172](https://pubmed.ncbi.nlm.nih.gov/31310172/)

### Flagged as my inference, not sourced
- **That GOLD's "Grains" excludes pulses/legumes.** No GOLD scope note states this; I infer it from the presence of separate `Bean` and `Nuts` nodes in the same extraction. If a curator wants the definition to commit either way, this needs checking against GOLD directly.
- **That milling fractions belong inside the node.** GOLD gives no scope note; the label's "/Grain products" and the absence of any flour/milling sibling node are the whole basis.
- **That `FOODON:00001093` semantically covers unprocessed grain sold as feed.** Inferred from `FOODON:00001002`'s "for humans **and animals**" wording plus FoodOn's `cereal grain (unprocessed)` sitting in the same branch. FoodOn supplies no textual definition for `00001093` to check against — this is the main residual risk in the grounding.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- cereal grain; cereals; food grain; grain commodity; stored grain; grain lot; small grains (wheat/barley/oat/rye, US usage)
- cereal grain food product (FoodOn); cereal grains and cereal-like grains (EFSA FoodEx2 `00030`); `020 cereal grains (GC)` (Codex CCPR); `058 milled cereal products` and `065 cereal grain milling fractions` (CCPR) — these last two are the "Grain products" half
- AGROVOC: *cereals* (c_1666), *grain* (c_3323) — [AGROVOC](https://agrovoc.fao.org/browse/agrovoc/en/)
- kernels; caryopses (botanical); groats, meal, flour, bran, semolina, middlings (fraction names)

**Commonly but wrongly treated as the same thing**
| Not the same | Why |
|---|---|
| **Mineral/sedimentary grain, particle** (`ENVO:01003002` and its `grain of …sand` children) | Homonym. This is the trap that produced the original bad proposal. |
| **Grain dust** (`ENVO:02000107`) | The bioaerosol generated *by handling* grain — a different sample type with a different (occupational-exposure) literature. |
| **Straw / stover / chaff** (`ENVO:00003869`) | Explicitly the residue *after grain removal*. |
| **Seed as a plant organ** (`PO` seed; `BTO:0000668` kernel; `BTO:0000057` aleurone layer) | Anatomical entities. Relevant to the endophytic compartment, but the habitat here is a bulk commodity, not an organ. |
| **The growing cereal crop / agricultural field** | An *Environmental > Terrestrial* habitat in GOLD, and where field fungi are acquired — but a different node. |
| **Bread, sourdough, malt, beer wort, silage** | Downstream fermented or baked substrates, each with its own GOLD node and its own community. Green malt even has its own BTO term (`BTO:0003365` germinated grain). |
| **Grain storage structures** (silo, bin, elevator, mill) | Sites. If the sample is a swab of a silo wall or a mill surface, the right habitat is a food-production facility/monitoring-zone term (`ENVO:035013xx`), not this one. |
| **Animal feed** (`ENVO:02000047`) | Overlapping *use*, not identity: feed includes non-grain material, and most grain is not feed. `xref` only. |
| **Breakfast cereal, pasta, baked goods** | Composite manufactured foods; FoodOn puts them under `grain based bakery food product` (`FOODON:00001917`), a child of the proposed genus. |

---

## 6. Should this be a term at all? — Yes, and it should be grounded, not minted

This is a **material entity that microorganisms demonstrably inhabit**, with a large primary literature, a distinctive and measurable physicochemistry, and a characteristic succession. It is not a process, a quality, a disease, a taxon, or a sampling artefact. `NOT_APPLICABLE` would be wrong.

It *is* a heterogeneous commodity class rather than a single homogeneous substrate — flour and a whole wheat kernel are quite different habitats. But the corpus already keeps exactly this shape of class (`Meat products`, `Dairy products`, `Fish products`, `Egg products`, `Plant products`), so that is not a reason to withhold a term.

**Recommended disposition — `GROUND`, keyed on `habitatmech:GOLD.c25f588dad`:**

- **Target:** `FOODON:00001093`, label **`cereal grain food product`** (label verified against `data/raw/ontology_terms.tsv`; will pass the seeder's label check)
- **Predicate:** `skos:closeMatch` / `CLOSE`, not `EXACT`. GOLD's label bundles the raw commodity with derived products, while FoodOn's class is a *food product* class — a silo lot destined for feed or for seed stock is a boundary case FoodOn's wording does not clearly cover. `EXACT` is defensible on the `Dairy products` → `dairy food product` precedent if a curator prefers consistency over caution; I would take `CLOSE`.
- **`parent_habitats`:** keep `FOODON:03530206` *food production*; optionally add `FOODON:00001173` *plant seed food product* as the taxonomic parent (mirrors `spice.yaml`, which carries both a FoodOn taxonomic parent and `FOODON:03530206`).
- **`relation: xref`** for `ENVO:02000107` *grain dust* and `ENVO:02000047` *animal feed* — related, neither broader nor identity.

**Two things a curator must weigh before committing.**

1. **FoodOn gives `FOODON:00001093` no textual definition.** Every currently-grounded FOOD record in the corpus (`bread`, `spice`, `dairy_food_product`, `nut (whole or pieces)`) carries a `definition` copied from the source ontology; grounding here would produce the first grounded FOOD record with a label and no definition. The clean fix is to **submit the sentence at the top of this report to FoodOn as a textual definition for `FOODON:00001093`** and cite the issue in the decision note. That converts a repo-local gap into an upstream contribution.

2. **The upstream assertion volume is 0.** `data/raw/gold_ecosystem_paths.tsv` records this path with `0` organisms across all three GOLD ecosystem ids (`gold.ecosystem:5927|5928|5929`) — an empty GOLD node. By `just report`'s backlog ranking this is the lowest-yield record in the FOOD category, so it is not urgent; it is worth doing because it is cheap and because the existing note asserts something false.

**Suggested note text** (every claim in it is checkable against the repo, per `tests/test_decisions.py`):

> GROUND to FOODON:00001093 'cereal grain food product' (CLOSE). Supersedes the 2026-08-12 CONFIRM_UNGROUNDED, whose note claimed no cereal-grain term was in the slice; FOODON:00001093 is in data/raw/ontology_terms.tsv and has children there (FOODON:00001917). Mirrors the reviewed GOLD 'Dairy products' -> FOODON:00001256 'dairy food product' grounding. CLOSE rather than EXACT because the GOLD label bundles raw grain with derived products while the FoodOn class is a food-product class. FoodOn supplies no textual definition for this term; definition contributed upstream. Path: Engineered > Food production > Grains/Grain products (source concept habitatmech:GOLD.c25f588dad)

**If the grounding is rejected and a HabitatMech term is minted instead**, the definition at the top of this report stands with `FOODON:00001015` *plant food product* as the genus — but that would be minting a term FoodOn already has a label for, which the repo's own minting rule ("only when no term in ENVO, UBERON, FOODON, BTO or PO names the concept") does not permit.

**Sources:**
- [Solanki et al. 2021, *J Fungi* — stored wheat grain microbiota](https://doi.org/10.3390/jof7090781)
- [Zhang et al. 2024, *Agronomy* — rice grain fungal communities](https://doi.org/10.3390/agronomy14081681)
- [Kim & Lee 2023 — seed microbiomes of staple food crops](https://pmc.ncbi.nlm.nih.gov/articles/PMC10686132/)
- [Abdelfattah et al. 2023, *Trends in Microbiology* — microbial inheritance seed to seed](https://doi.org/10.1016/j.tim.2022.12.006)
- [Magan & Aldred 2007, *J Stored Prod Res* — integrated management of stored grain spoilage](https://doi.org/10.1016/j.jspr.2006.08.006)
- [Mannaa & Kim 2017, *Mycobiology* — temperature and water activity in grain storage](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5780356/)
- [Abdullah et al. 2000, *J Stored Prod Res* — fungal spoilage of starch-based foods vs a_w](https://doi.org/10.1016/S0022-474X(99)00026-0)
- [Hanson et al. 2005, *J Agric Food Chem* — field vs storage fungi on wheat gluten](https://doi.org/10.1021/jf050821t)
- [Lahouar et al. 2018 — mycoflora of Tunisian cereals](https://pmc.ncbi.nlm.nih.gov/articles/PMC6088110/)
- [Carvalho et al. 2022 — rehydrated corn and sorghum grain silage microbiome](https://pmc.ncbi.nlm.nih.gov/articles/PMC9546842/)
- [K-State S156 ch.6 — molds and mycotoxins in stored products](https://entomology.k-state.edu/doc/finished-chapters/s156-6.pdf)
- [Crowe et al. 2017, *NEJM* — STEC infections associated with flour](https://doi.org/10.1056/NEJMoa1615910)
- [Forghani et al. 2019, *J Food Prot* — desiccation and thermal resistance of E. coli O121 in wheat flour](https://pubmed.ncbi.nlm.nih.gov/31310172/)
- [Mukherjee et al. 2023, *Nucleic Acids Research* — GOLD v.9](https://doi.org/10.1093/nar/gkac974)
- [Dooley et al. 2018, *npj Science of Food* — FoodOn](https://doi.org/10.1038/s41538-018-0032-6)
- [FoodOn food-product hierarchy](https://foodon.org/food-facets/food-product/)
- [OLS4 — FOODON:00001093 cereal grain food product](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:00001093)
- [GSC MIxS documentation](https://genomicsstandardsconsortium.github.io/mixs/) and [MIxS food-food production facility extension](https://genomicsstandardsconsortium.github.io/mixs/0016021/)
- [MIxS v6.3.0, Zenodo](https://zenodo.org/records/18511302)
- [AGROVOC](https://agrovoc.fao.org/browse/agrovoc/en/)

## Citations

1. https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:00001093
2. https://foodon.org/food-facets/food-product/
3. https://doi.org/10.1038/s41538-018-0032-6
4. https://doi.org/10.3390/jof7090781
5. https://doi.org/10.1093/nar/gkac974
6. https://doi.org/10.1093/nar/gkae1000
7. https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03400683
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC9546842/
9. https://www.ebi.ac.uk/ols4/ontologies/envo
10. https://doi.org/10.1016/j.jspr.2006.08.006
11. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5780356/
12. https://entomology.k-state.edu/doc/finished-chapters/s156-6.pdf
13. https://doi.org/10.1016/S0022-474X(99
14. https://doi.org/10.1021/jf050821t
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC6088110/
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC10686132/
17. https://doi.org/10.1016/j.tim.2022.12.006
18. https://pubmed.ncbi.nlm.nih.gov/31310172/
19. https://doi.org/10.1056/NEJMoa1615910
20. https://doi.org/10.3390/agronomy14081681
21. https://genomicsstandardsconsortium.github.io/mixs/
22. https://genomicsstandardsconsortium.github.io/mixs/0016021/
23. https://zenodo.org/records/18511302
24. https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03301941
25. https://agrovoc.fao.org/browse/agrovoc/en/