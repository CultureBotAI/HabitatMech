---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T00:32:26.919576'
end_time: '2026-08-18T00:41:20.715795'
duration_seconds: 533.8
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Starter-culture
  habitat_identifier: habitatmech:BACDIVE.9eabedc3a1
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Starter-culture'
  assertions: '19'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Grounding-cohort
    review (#62): was FOODON:03544454 ''44540 - starter cultures (efsa foodex2)'',
    a food-classification code rather than a place. A starter culture is a real habitat
    for the organisms in it; the slice has no term that is one. (source concept habitatmech:BACDIVE.9eabedc3a1)'
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
  web_search_requests: 12
  num_turns: 37
  total_cost_usd: 3.118863499999999
  session_id: 1d4cba55-2933-4b64-83a1-acb68443a220
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 19
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Starter-culture
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.9eabedc3a1
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Starter-culture
- **Upstream assertion volume:** 19
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Grounding-cohort review (#62): was FOODON:03544454 '44540 - starter cultures (efsa foodex2)', a food-classification code rather than a place. A starter culture is a real habitat for the organisms in it; the slice has no term that is one. (source concept habitatmech:BACDIVE.9eabedc3a1)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Starter-culture** as a microbial habitat, with citations.

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

# Starter-culture (`habitatmech:BACDIVE.9eabedc3a1`) — definition research

> **A manufactured microbial preparation which is deliberately propagated and held as a viable inoculum for transfer into a fermentable substrate, and in which the resident microbial community grows and is maintained prior to that transfer.**

**Recommended disposition, before anything else:** this concept most likely should not stay `CONFIRM_UNGROUNDED`. **`ENVO:03600040` 'fermentation starter'** is present in this repo's vendored slice today (`data/raw/ontology_terms.tsv`), and the corpus **already uses it** — `data/habitats/food/fermentation_starter.yaml` grounds GOLD's `Engineered > Food production > Fermentation starter` to it at `EXACT` with 62 organism assertions. The curator note on this decision ("the slice has no term that is one") is contradicted by the corpus as it now stands. Details and the caveats in §2.

---

## 1. What the concept denotes

### 1a. The label as BacDive uses it

Critically, **`Starter-culture` here is a BacDive isolation-source *category node*, not a free-text sample description.** I verified this directly against a strain in this record's own `characteristic_taxa`: *Selenomonas lacticifex* VB4b (`NCBITaxon:86957`, listed here under the newer name *Schleiferibacter lactififex*) is [BacDive strain 17160](https://bacdive.dsmz.de/strain/17160), whose recorded isolation source is the free text **"pitching yeast"**, classified as **Cat1 `Engineered` / Cat2 `Food production` / Cat3 `Starter culture`**.

That makes the BacDive concept structurally parallel to GOLD's `Engineered > Food production > Fermentation starter` — the same slot in the same three-level engineered/food-production classification. This is the strongest single piece of evidence for how to dispose of the record.

### 1b. The physical thing sampled

As a habitat, a starter culture is **a physical, viable microbial preparation held separately from the food it will ferment** — the thing a pipette or spatula goes into. Concretely it is one of:

| Format | Physical description | Example organisms in this record |
|---|---|---|
| Bulk / mother starter | Milk or wort inoculated and propagated in a starter tank, cell densities ~10⁸–10⁹ CFU/mL | *Lactococcus lactis*, *Leuconostoc pseudomesenteroides* |
| DVS concentrate | Frozen pellets or freeze-dried powder, ~10¹⁰–10¹¹ CFU/g | *Lacticaseibacillus* spp., *Bifidobacterium bifidum* |
| Backslopped / traditional starter | Sourdough starter, kefir grain, daqu/qu brick, koji — a continuously refreshed matrix | (evidenced by GOLD's `Sourdough` sibling, not by this BacDive bucket) |
| Pitching yeast / yeast slurry | Cropped brewing yeast slurry, ~1–2 × 10⁹ cells/mL, ~90% viability, held cold in a brink between fermentations | *Propionispira paucivorans*, *P. raffinosivorans*, *Schleiferibacter/Selenomonas lacticifex* |

The last row matters: **at least 6 of the 19 strains in this record are brewery pitching-yeast organisms.** *Propionispira raffinosivorans* DSM 20765's [DSMZ catalogue entry](https://www.dsmz.de/collection/catalogue/details/culture/DSM-20765) gives isolation source verbatim as **"pitching yeast"**, and the founding taxonomic paper describes 47 strains "isolated mainly from spoiled beer and pitching yeast" ([Schleifer et al. 1990, *Int J Syst Bacteriol* 40:19–27, doi:10.1099/00207713-40-1-19](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-40-1-19); reclassified into *Propionispira* by [Ueki et al. 2014, *IJSEM* 64:3571–3577, PMID 25061065](https://pubmed.ncbi.nlm.nih.gov/25061065/)).

**Boundary — inside the concept:** the starter preparation itself, in any of the four formats above, including the maintained mother culture and the harvested yeast slurry.

**Boundary — neighbouring concepts, outside:**

- **The fermented product** the starter is added to — cheese, sourdough bread, beer, salami. GOLD keeps `Fermented food`, `Cheese`, `Sourdough` and `Fermented beverages` as separate siblings of `Fermentation starter` under `Engineered > Food production` (`data/raw/gold_ecosystem_paths.tsv`), so the sources themselves draw this line.
- **The fermentation vessel or facility** — `ENVO:00003885` brewery, `ENVO:03600039` fermentation pit, `ENVO:03600091` clay fermentation pit. These are constructions; the starter is the material in them.
- **The growth medium as such** — `BTO:0000316` culture medium ("a substance … used for the cultivation, isolation, identification, or storage of microorganisms"). A starter is medium *plus* an established community, defined by its inoculating role.
- **A laboratory pure culture** — `ENVO:01001060` single strain cell culture, `ENVO:02000008` cell culture ("growth of cells in vitro in an artificial medium for experimental research"). A starter is propagated for production, not experiment, and is typically multi-strain.
- **The fermentation process** — a process, not a place.

### 1c. Ambiguity: three readings, only one of which is a habitat

1. **The preparation (material).** ✅ This is what the data means, confirmed by the BacDive category tree and the pitching-yeast free text.
2. **A role attributed to a strain** ("this isolate is a starter culture organism"). A role borne by an organism, not a place. This is what `FOODON:03544454` encodes — see §2.
3. **The commercial product line / regulatory commodity class** (an EFSA FoodEx2 code, a supplier SKU). A classification, not a place.

Readings 2 and 3 are why the earlier `FOODON:03544454` grounding was rightly rejected in #62. They do not undermine reading 1.

---

## 2. Genus — the broader kind

### The match: `ENVO:03600040` 'fermentation starter'

- Label (verified in `data/raw/ontology_terms.tsv`, exact): **`fermentation starter`**
- ENVO definition: *"A manufactured product which assists starting a fermentation process which is intended to prepare foods and alcoholic drinks."*
- Exact synonym recorded: **Daqu**
- Direct parent: `ENVO:00003074` 'manufactured product' — *"A material entity that has been processed by humans or their technology in any way, including intermediate products as well as final products."*
- Provenance ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:03600040)): created 2021-06-24, creator ORCID `0000-0002-6670-9157`, xref `https://en.wikipedia.org/wiki/Fermentation_starter`.

It is a **material entity**, which is what a habitat record needs, and its definition explicitly covers **alcoholic drinks** — so pitching yeast, the awkward third of this record's strains, falls inside rather than outside it.

Two caveats a curator should weigh, both mine to flag rather than blockers:

- ENVO places it under *manufactured product*, not under *environmental material*. Whether a backslopped home sourdough starter is a "manufactured product" is arguable; ENVO's own definition of the parent ("processed by humans … in any way, including intermediate products") is broad enough that I read it as covered, but that is my inference, not an ENVO assertion.
- "foods and alcoholic drinks" would exclude non-food fermentation starters (silage inoculants, industrial biogas seed sludge). **No evidence of those in this record** — all 15 taxa are food/beverage-associated — so the exclusion costs nothing here. GOLD keeps `Silage fermentation` as a separate sibling anyway.

### Near-misses and why each fails

| Term | Why it is not the genus |
|---|---|
| `FOODON:03544454` '44540 - starter cultures (efsa foodex2)' | A **food-classification code**, not a material entity — "the part consumed/analysed is by default the whole marketed unit". Already rejected in #62; that rejection was correct. |
| `FOODON:00001018` 'cheese starter culture' | **Narrower** — dairy only, which would drop the pitching-yeast and *Pediococcus* strains. Also **not in the vendored slice** (the FOODON slice is 226 terms; I checked and it is absent). Its parent is `FOODON:00001145` 'microbial food material' — *"microbial material derived from one or more microorganisms including bacteria, mold, and yeast"* — a plausible upper genus, also not vendored. |
| `FOODON:03302365` 'sour dough starter culture' | Narrower; not vendored. |
| `FOODON:00001144` 'yeast material' (*is* vendored) | Narrower on organism (fungi only) and silent on the inoculating role. |
| `ENVO:02000008` 'cell culture' | Asserts *"in vitro in an artificial medium for experimental research"* — a starter is production, not research, and a bulk starter in milk is not obviously "artificial medium". |
| `ENVO:01001060` 'single strain cell culture' / `ENVO:01001059` 'mock community culture' | Assert composition (single strain / known composition) that undefined mixed starters explicitly lack. |
| `BTO:0000316` 'culture medium' | The substrate, not the substrate-plus-community. |
| `ENVO:03600039` 'fermentation pit' | A construction; sibling context, not genus. |

---

## 3. Differentia — what distinguishes it from siblings

Observable properties that separate a starter from the other things under *manufactured product* / *microbial food material*:

1. **Function as inoculum.** It exists to be transferred into a larger fermentable substrate; the fermented product is downstream and distinct. "A preparation of living microorganisms deliberately used to assist the beginning of fermentation, producing specific changes in the chemical composition and sensory properties of the substrate" — the standard framing in [Leroy & De Vuyst 2004, *Trends Food Sci Technol* 15:67–78, doi:10.1016/j.tifs.2003.09.004](https://www.sciencedirect.com/science/article/abs/pii/S0924224403002085).
2. **High, deliberately maintained cell density.** Orders of magnitude above the substrate it inoculates: ~10⁹–10¹¹ CFU/g for concentrated DVS cultures; 1–2 × 10⁹ cells/mL at ~90% viability for brewery slurry ([Craft Beer & Brewing, harvesting/re-pitching guide](https://www.beerandbrewing.com/the-giga-guide-to-harvesting-and-re-pitching-yeast)).
3. **Serial propagation as the defining maintenance regime**, which is what makes it a *persistent* habitat rather than a transient one. Backslopping — refreshing a fermenting mixture with fresh substrate — sustains a community across hundreds of generations. Documented ranges: 29 daily transfers ≈ 186 generations for a Gouda starter ([Erkus et al. 2013, *ISME J* 7:2126–2136, doi:10.1038/ismej.2013.108](https://www.nature.com/articles/ismej2013108)); **82 years of continuous propagation** for a Swiss cheese starter, still dominated by a few coexisting *Streptococcus thermophilus* and *Lactobacillus delbrueckii* subsp. *lactis* strains ([Somerville et al. 2022, *ISME J* 16:388–399, doi:10.1038/s41396-021-01071-0](https://www.nature.com/articles/s41396-021-01071-0)). Brewing repitching runs ~12 generations before strain drift forces re-culturing from lab stock.
4. **Community structure that is a property of the starter, not of the food.** Undefined mesophilic starter "Ur" carries seven distinguishable *L. lactis* genetic lineages plus a *Leuconostoc* component (Erkus et al. 2013). Across 500 sourdough starters from four continents, the median starter held one yeast type but 70 yeast types were found overall, and *Lactobacillus plantarum*/*L. brevis* co-occurred in 177 of 500 ([Landis et al. 2021, *eLife* 10:e61644, doi:10.7554/eLife.61644](https://elifesciences.org/articles/61644)).
5. **Spatial structure distinct from the fermenting substrate.** In kefir, the grain (a kefiran polysaccharide matrix) and the milk are separate niches: the grain grows in mass but stays compositionally unchanged while the milk is colonised sequentially, and the grain-dominant *Lactobacillus kefiranofaciens* cannot survive in milk alone ([Blasche et al. 2021, *Nat Microbiol* 6:196–208, doi:10.1038/s41564-020-00816-5](https://www.nature.com/articles/s41564-020-00816-5)). This is the clearest published demonstration that a starter is a habitat in its own right and not merely a sample of the food.
6. **Characteristic physicochemistry.** Low pH from lactic acidification (sourdough starters typically pH 3.5–4.5), largely anoxic, high in fermentable carbohydrate. The organisms in *this* record are consistent with it: anaerobic lactic acid bacteria plus obligately anaerobic, Gram-negative *Propionispira*/*Selenomonas* rods.
7. **Solid-state variants are structurally distinct habitats.** Daqu is a solid brick supporting filamentous fungi (*Rhizopus*, *Rhizomucor*, *Aspergillus*), yeasts and bacteria simultaneously ([Zheng et al. 2011, *J Inst Brew* 117:82–90, doi:10.1002/j.2050-0416.2011.tb00447.x](https://onlinelibrary.wiley.com/doi/10.1002/j.2050-0416.2011.tb00447.x); [Xia et al. 2023, *Appl Microbiol Biotechnol* 107:25–41](https://link.springer.com/article/10.1007/s00253-022-12312-3)).

A **useful secondary axis** if a curator ever needs to split this: **defined/commercial vs. undefined/backslopped**. De Vuyst and colleagues formalise it for sourdough as type 1 (spontaneous + successive refreshment), type 2 (started from a starter culture), type 3 (starter culture then backslopped) ([De Vuyst, Van Kerrebroeck & Leroy 2017, *Adv Appl Microbiol* 100:49–160, doi:10.1016/bs.aambs.2017.02.003](https://www.sciencedirect.com/science/article/abs/pii/S0065216417300175)). I would **not** encode this in the definition — the sources do not distinguish it, and the two would be near-impossible to separate for a given BacDive strain.

---

## 4. Sources

**Primary literature**

- Schleifer KH, Leuteritz M, Weiss N, Ludwig W, Kirchhof G, Seidel-Rüfer H. 1990. Taxonomic study of anaerobic, Gram-negative, rod-shaped bacteria from breweries. *Int J Syst Bacteriol* 40:19–27. doi:10.1099/00207713-40-1-19 — https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-40-1-19
- Ueki A, et al. 2014. *Propionispira arcuata* sp. nov. … reclassification of *Zymophilus*. *IJSEM* 64:3571–3577. PMID 25061065 — https://pubmed.ncbi.nlm.nih.gov/25061065/
- Erkus O, et al. 2013. Multifactorial diversity sustains microbial community stability. *ISME J* 7:2126–2136. doi:10.1038/ismej.2013.108
- Somerville V, et al. 2022. Functional strain redundancy and persistent phage infection in Swiss hard cheese starter cultures. *ISME J* 16:388–399. doi:10.1038/s41396-021-01071-0
- Landis EA, et al. 2021. The diversity and function of sourdough starter microbiomes. *eLife* 10:e61644. doi:10.7554/eLife.61644 — PMC7837699
- Blasche S, et al. 2021. Metabolic cooperation and spatiotemporal niche partitioning in a kefir microbial community. *Nat Microbiol* 6:196–208. doi:10.1038/s41564-020-00816-5
- Smid EJ, et al. 2014. Functional implications of the microbial community structure of undefined mesophilic starter cultures. *Microb Cell Fact* 13(Suppl 1):S2. doi:10.1186/1475-2859-13-S1-S2 — PMC4155819

**Reviews and reference works**

- Leroy F, De Vuyst L. 2004. Lactic acid bacteria as functional starter cultures for the food fermentation industry. *Trends Food Sci Technol* 15:67–78. doi:10.1016/j.tifs.2003.09.004
- De Vuyst L, Van Kerrebroeck S, Leroy F. 2017. Microbial ecology and process technology of sourdough fermentation. *Adv Appl Microbiol* 100:49–160. doi:10.1016/bs.aambs.2017.02.003
- Zheng X-W, Tabrizi MR, Nout MJR, Han B-Z. 2011. Daqu — a traditional Chinese liquor fermentation starter. *J Inst Brew* 117:82–90. doi:10.1002/j.2050-0416.2011.tb00447.x
- Xia Y, Luo H, Wu Z, Zhang W. 2023. Microbial diversity in jiuqu and its fermentation features. *Appl Microbiol Biotechnol* 107:25–41. doi:10.1007/s00253-022-12312-3
- Oxford Companion to Beer, s.v. "pitching" — https://www.beerandbrewing.com/dictionary/V04NmdFJJA

**Vocabularies and databases**

- ENVO `ENVO:03600040` 'fermentation starter' — https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:03600040
- FoodOn `FOODON:00001018`, `FOODON:00001145`, `FOODON:03544454` — https://www.ebi.ac.uk/ols4/ontologies/foodon
- Dooley DM, et al. 2018. FoodOn: a harmonized food ontology. *npj Sci Food* 2:23. doi:10.1038/s41538-018-0032-6
- BacDive strain 17160, *Selenomonas lacticifex* VB4b — https://bacdive.dsmz.de/strain/17160 (isolation source "pitching yeast"; Cat3 "Starter culture")
- DSMZ catalogue, DSM 20765 — https://www.dsmz.de/collection/catalogue/details/culture/DSM-20765 (isolation source "pitching yeast")
- GSC MIxS food extensions (`FoodHumanFoods` 0016022, `FoodFoodProductionFacility` 0016021, `FoodFarmEnvironment` 0016020, `FoodAnimalAndAnimalFeed` 0016019) — https://genomicsstandardsconsortium.github.io/mixs/0016022/

**Explicitly my inference, not sourced:** that a backslopped domestic starter satisfies ENVO's 'manufactured product'; that the BacDive `Starter-culture` bucket and GOLD's `Fermentation starter` denote the same concept (strongly supported by the parallel Cat1/Cat2/Cat3 tree, but no source asserts the equivalence); the CFU/g range for DVS concentrates, which is textbook-level but which I did not pin to a specific citation. **A caution on nomenclature:** BacDive renders `NCBITaxon:86957` as *Schleiferibacter lactififex*; the basonym is *Selenomonas lacticifex* (Schleifer et al. 1990), and the genus transfer comes from a 2026 Selenomonadaceae reclassification ([doi:10.1099/ijsem.0.007178](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.007178), PMID 42207170). The `-fifex` spelling in the corpus looks like an upstream typo — worth a separate issue, not a blocker here.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**

- fermentation starter (ENVO's label; GOLD's leaf label)
- starter, starter culture, mother culture, bulk starter, mother dough
- DVS culture / direct-vat-set culture / direct vat inoculation culture
- inoculum, seed culture
- levain, chef, sourdough starter, *Sauerteig*
- kefir grains, SCOBY, kombucha mother
- daqu / xiaoqu / fuqu / jiuqu (ENVO records **Daqu** as an exact synonym), koji, ragi, bubod, nuruk
- backslop / back-slopping inoculum
- pitching yeast, yeast slurry, barm, repitched yeast (**brewing register — evidenced in this record's own data**)

**Commonly conflated but distinct — do not treat as the same thing**

| Not the same | Why |
|---|---|
| The fermented food or beverage | Separate GOLD siblings; separate ENVO/FoodOn terms. Grounding a cheese sample here would misattribute it. |
| Probiotic preparation / dietary supplement | Overlapping organisms, different function — consumed as-is, not used to ferment a substrate. |
| Culture collection deposit / lab pure culture | `ENVO:01001060`; a strain in a cryovial is not a starter. |
| Culture medium (`BTO:0000316`) | The substrate alone. |
| Fermentation vessel / brewery / fermentation pit (`ENVO:00003885`, `ENVO:03600039`) | Constructions. |
| "Starter culture" as an EFSA FoodEx2 commodity code (`FOODON:03544454`) | A classification of a marketed unit. |
| "Starter culture" as a *role* of an organism | A role borne by a taxon, not a place. |
| Rumen fluid / silage inoculant | Also inocula, but outside ENVO's "foods and alcoholic drinks" scope and outside this record's evidence. |

---

## 6. Should it be a term at all?

**Yes — it denotes a habitat, and it already has one.** A starter culture is a physical material harbouring a reproducing, structured, serially maintained microbial community; Blasche et al. 2021 and Somerville et al. 2022 demonstrate niche partitioning and 82-year community persistence *within the starter*, which is exactly what distinguishes a habitat from a sampling artefact. The `#62` reviewer's own reasoning ("a starter culture is a real habitat for the organisms in it") was right; only the "no term exists" half was wrong.

**What I would put to the curator, in order:**

1. **`GROUND` to `ENVO:03600040` 'fermentation starter'.** Label matches the vendored slice exactly, so the seed's label check passes. This merges the BacDive attestation (19 strains) into the existing `data/habitats/food/fermentation_starter.yaml` alongside GOLD's 62 organisms, and moves the concept out of `OTHER` into `FOOD` — where the source path (`Engineered > Food production > Starter culture`) says it belongs. Remember `assertion_count` is not summable across `STRAIN` and `ORGANISM` units.
2. If the fit is judged too loose because ENVO asserts *manufactured product* while a third of the strains come from cropped pitching yeast, the fallback is **`GROUND_AS_PARENT` on `ENVO:03600040`** with the minted identity retained — but I do not think the evidence supports that: ENVO's definition names alcoholic drinks explicitly, and pitching yeast is a manufactured, deliberately propagated inoculum by any reading.
3. **`NOT_APPLICABLE` is wrong here** — that disposition is for diseases, qualities, processes and procedures, and a starter is a material.
4. **A term request is not needed.** The gap the `#62` note described has a term in it.

**Two things worth filing separately, not resolved here:**

- **Whether the corpus should carry the same concept twice.** Right now `data/habitats/other/starter_culture.yaml` (`REVIEWED`, `UNGROUNDED`, BacDive, category `OTHER`) and `data/habitats/food/fermentation_starter.yaml` (`SEEDED`, `EXACT`, GOLD, category `FOOD`) split one concept across two records and two categories. Grounding this decision fixes it; leaving it as-is publishes a contradiction.
- **The heterogeneity of the BacDive bucket itself.** "Pitching yeast" as a habitat — a cold-stored, high-density, repeatedly reused brewing yeast slurry — is a defensible narrower concept with its own physicochemistry, and 6 of the 19 strains here are from it. Nothing in ENVO, FoodOn or the vendored slice names it. That is a genuine term-request candidate; **this** record is not.

## Citations

1. https://bacdive.dsmz.de/strain/17160
2. https://www.dsmz.de/collection/catalogue/details/culture/DSM-20765
3. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-40-1-19
4. https://pubmed.ncbi.nlm.nih.gov/25061065/
5. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:03600040
6. https://en.wikipedia.org/wiki/Fermentation_starter`
7. https://www.sciencedirect.com/science/article/abs/pii/S0924224403002085
8. https://www.beerandbrewing.com/the-giga-guide-to-harvesting-and-re-pitching-yeast
9. https://www.nature.com/articles/ismej2013108
10. https://www.nature.com/articles/s41396-021-01071-0
11. https://elifesciences.org/articles/61644
12. https://www.nature.com/articles/s41564-020-00816-5
13. https://onlinelibrary.wiley.com/doi/10.1002/j.2050-0416.2011.tb00447.x
14. https://link.springer.com/article/10.1007/s00253-022-12312-3
15. https://www.sciencedirect.com/science/article/abs/pii/S0065216417300175
16. https://www.beerandbrewing.com/dictionary/V04NmdFJJA
17. https://www.ebi.ac.uk/ols4/ontologies/foodon
18. https://genomicsstandardsconsortium.github.io/mixs/0016022/
19. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.007178