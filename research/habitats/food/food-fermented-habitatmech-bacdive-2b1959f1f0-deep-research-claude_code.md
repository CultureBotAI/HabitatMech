---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T17:05:01.437160'
end_time: '2026-08-17T17:14:09.387124'
duration_seconds: 547.95
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: food_fermented
  habitat_identifier: habitatmech:BACDIVE.2b1959f1f0
  habitat_category: FOOD
  grounding_status: UNGROUNDED
  attestations: 'MADIN: food_fermented'
  assertions: '173'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Reviewed and endorsed the seeder's own resolution. Category override\
    \ (#57): a minted identifier gives infer_category nothing to read \u2014 no ontology\
    \ term, no GOLD path \u2014 so every Madin habitat named in the BacDive vocabulary\
    \ fell to OTHER. A fermented food is FOOD, the category BacDive and FOODON populate\
    \ heavily and which exists precisely so these are not lumped into ENGINEERED.\
    \ (source concept habitatmech:BACDIVE.2b1959f1f0)"
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
  - claude-opus-5
  web_search_requests: 12
  num_turns: 40
  total_cost_usd: 3.3394234999999997
  session_id: bf8f13af-33af-431f-be47-203750440bba
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 26
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** food_fermented
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.2b1959f1f0
- **Category:** FOOD
- **Grounding status:** UNGROUNDED
- **Source attestations:** MADIN: food_fermented
- **Upstream assertion volume:** 173
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Reviewed and endorsed the seeder's own resolution. Category override (#57): a minted identifier gives infer_category nothing to read — no ontology term, no GOLD path — so every Madin habitat named in the BacDive vocabulary fell to OTHER. A fermented food is FOOD, the category BacDive and FOODON populate heavily and which exists precisely so these are not lumped into ENGINEERED. (source concept habitatmech:BACDIVE.2b1959f1f0)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **food_fermented** as a microbial habitat, with citations.

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

# Definition research: `food_fermented` (habitatmech:BACDIVE.2b1959f1f0)

> **Proposed definition:** A food product which is the output of a food fermentation process, and in which the microbial community driving that process, together with the acids, ethanol and other metabolites it produces, constitutes the habitat.

**Headline finding, before anything else: this concept already has a term, and the corpus already uses it.** `FOODON:00001258` "food (fermented)" — *"Food material which has been fermented."* — is present in the vendored slice (`data/raw/ontology_terms.tsv`, `directly_referenced=TRUE`) and is the `identifier` of the existing record `data/habitats/food/food_fermented.yaml`. That record was reached by an earlier curation decision on the near-identical BacDive bin (`habitatmech:BACDIVE.556e1e04f8` → `GROUND FOODON:00001258 food (fermented)`, `BROAD`, 2026-08-12). The Madin bin under research is the *same concept arriving from a third source*; it is UNGROUNDED only because Madin habitat rows carry no ontology target for `infer_category` or the grounder to read (the same mechanism the #57 category override was written to work around). The evidence below supports **`GROUND` to `FOODON:00001258`**, not minting a new term. See §6.

---

## 1. What the concept denotes

### 1.1 Provenance of the label

`food_fermented` is not a BacDive isolation source despite the `bacdive.isolation_source:` prefix on its identifier. It is a term in the **Madin et al. (2020) condensed-traits `isolation_source` vocabulary**, a nested up-to-4-level controlled hierarchy in which level 1 is a broad habitat class and each subsequent level refines it ([Madin et al. 2020, *Sci Data* 7:170, doi:10.1038/s41597-020-0497-4](https://doi.org/10.1038/s41597-020-0497-4)). `food_fermented` is therefore *level 1 = food, level 2 = fermented*. Its sibling under level 1 is plain `food`; there are exactly two `food*` targets in the whole vocabulary — 127 source strings map to `food` and 86 map to `food_fermented` ([conversion table `renaming_isolation_source.csv`](https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/blob/master/data/conversion_tables/renaming_isolation_source.csv)).

This matters for grounding: `food_fermented` is not one of Madin's *coarse* habitat classes. It is a specific, deliberately-named bin, and its name is a straight transliteration of the FoodOn label pattern `food (fermented)`.

### 1.2 What is inside the bin — the authoritative evidence

The 86 free-text isolation-source strings that Madin's table maps to `food_fermented` are the strongest available evidence of the concept's extension. They fall into six coherent groups:

| Group | Example source strings |
|---|---|
| Fermented vegetables / brines | `kimchi`, `cabbage kimchi`, `chinese pickle`, `japanese pickles`, `sunki`, `senmaizuke`, `fermented white radish`, `fermenting olives`, `fermented mustard`, `engineered, food production, fermented vegetables` |
| Fermented dairy | `traditional dairy fermented product (dahi type)`, `other, fermented mare's milk`, `kefir grain`, `kefir grains`, `multiple, fermented dairy product` |
| Fermented cereal / legume / soy | `sourdough`, `rye sourdough`, `rye-bran sourdough`, `rice sourdough`, `artisanal wheat sourdough`, `fermented rice grain`, `fermented soybean`, `doenjang, fermented soybeans`, `fermented brine used for stinky tofu production` |
| Fermented meat, fish, seafood | `nem chua (fermented meat)`, `fermented raw meat`, `fermented meat product`, `fermented anchovy (engraulis japonica)`, `shrimp jeotgal`, `saeu-jeotgal`, `other, salt-fermented seafood`, `other, fermented shrimp paste` |
| Alcoholic and acetic beverages and their mashes | `engineered, food production, fermented beverages`, `spanish natural cider`, `partially fermented wine`, `dolo wort`, `malt whiskey fermentation`, `shochu mash`, `sour grain mash`, `fermenting agave juice`, `fermented vinegar broth`, `yeast storage tank containing lager beer`, `spoiled sake` |
| Fermented feed and non-food agro-fermentations | `silage`, `grass silage`, `maize silage`, `orchardgrass silage`, `sudangrass silage sample`, `silage cattle feed`, `cattle waste-corn fermentation`, `swine waste-corn fermentation`, `cocoa bean heap fermentation`, `cassava sour starch fermentation`, `fermented cane molasses of alcohol plants`, `malted barley` |

**The reading the data means.** The bin denotes **the fermenting or fermented edible matrix itself** — the sauerkraut brine, the cheese curd, the sourdough, the mash, the silage clamp contents — as the material a strain was isolated from. It is a *material entity a sample is taken from*, not a facility, not a process, and not a quality. The characteristic taxa on the record confirm this reading unambiguously: `Lactobacillus` (many species), `Weissella koreensis` (kimchi), `Oenococcus oeni` and `O. kitaharae` (wine/sake), `Pediococcus damnosus` (beer spoilage), `Acetobacter persici`/`A. mesoxydans` (vinegar), `Zymomonas mobilis` (agave/palm sap), `Megasphaera cerevisiae` (beer).

### 1.3 The boundary — what is inside, what is a neighbour

**Inside (well-supported):** solid and liquid edible matrices undergoing or having undergone desired microbial conversion, including their brines, mashes and worts, and the fermented feed (silage) case. FoodOn's own `food product` root (`FOODON:00001002`) is defined as *"Food material for humans **and animals** which is processed with the intention that it be consumable…"* ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?short_form=FOODON_00001002)), so silage is inside FoodOn's "food", which is why `FOODON:00001258` subsumes the silage strings rather than being violated by them. **This is my inference from FoodOn's definition text, not a statement any source makes about `food_fermented`.**

**Neighbouring concepts already in the corpus that this is *not*:**
- `data/habitats/food/food_production.yaml` and `fermentation_cellar.yaml`, `pit_mud.yaml` — the **facility or built setting**, not the matrix. ENVO models this side (`ENVO:00003885` brewery, `ENVO:03600039` fermentation pit); the earlier decision `habitatmech:BACDIVE.b415adf879` explicitly separated "'Food-production' as a setting rather than a product."
- `fermentation_starter.yaml` (`ENVO:03600040`) — the **inoculum**, a manufactured product that starts a fermentation. Note Madin puts `kefir grain`/`kefir grains` in `food_fermented`; a kefir grain is a starter, so the bin does slightly overlap this neighbour.
- `food_spoiled.yaml` (`FOODON:00003366`) — the **undesired** microbial conversion. The distinguishing property is intent, not chemistry (§3).
- `food_preserved.yaml` (`FOODON:00002158`) — overlapping but not identical: fermentation is one preservation route among many (canning, freezing, irradiation are preservation without fermentation).
- `silage_fermentation.yaml` (`ENVO:00003030`) — a **child**, already present as its own record.
- `food_fermented.yaml` (`FOODON:00001258`) — **the same concept**, already grounded. This is the merge target.

### 1.4 Known contamination in the bin (must be recorded, not hidden)

Three defects are demonstrable from the mapping table and should be noted on the record rather than defined away:

1. **`malted barley`** is in the bin, but malting is grain germination driven by *endogenous plant* enzymes. The ISAPP consensus is explicit that "microorganisms must drive the process; endogenous enzymes alone are insufficient" ([Marco et al. 2021](https://doi.org/10.1038/s41575-020-00390-5)). Malted barley is therefore mis-binned under any principled definition of fermented food.
2. **`pickle` / `pickles` / `japanese pickles`** are ambiguous: vinegar-pickled products are acidified, not fermented. Madin's flat text mapping cannot separate the two.
3. **An outright wrong-habitat isolate is present in the characteristic taxa.** `NCBITaxon:1110509` *Methanosaeta harundinacea* 6Ac was isolated from an **upflow anaerobic sludge blanket bioreactor treating beer-manufacture wastewater**, not from a food ([Ma, Liu & Dong 2006, *IJSEM* 56:127–131, doi:10.1099/ijs.0.63887-0](https://doi.org/10.1099/ijs.0.63887-0); [BacDive strain 131756](https://bacdive.dsmz.de/strain/131756)). An acetoclastic methanogen is not a fermented-food organism. This is a text-matching artefact of the Madin bin (a source string mentioning beer), and it is direct evidence that `assertion_count: 173` is an upper bound.

---

## 2. Genus — the broader kind

### 2.1 Recommended genus

**`FOODON:00001002` "food product"** — *"Food material for humans and animals which is processed with the intention that it be consumable as a whole or added to other food products."* ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?short_form=FOODON_00001002))

This is the smallest well-established kind that covers the whole bin (human food, beverages, and animal feed), and it is the term ENVO itself points at: **`ENVO:00002002` "obsolete food product" is deprecated with `IAO:0100001 term_replaced_by → FOODON:00001002`**.

If a tighter genus is wanted, **`FOODON:00002645` "food material by process"** (*"Food material organized by the process which it results from."*) is the immediate parent that `FOODON:00001258` actually asserts, alongside `FOODON:00002501` "multi-component food" (`data/raw/ontology_subclass_edges.tsv`).

### 2.2 ENVO — checked, and it deliberately has nothing

ENVO **has no term for fermented food, by design**. Its entire food-product branch is obsoleted and redirected to FoodOn. Terms retrieved as obsolete from [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo):

| ENVO id | Label | Status |
|---|---|---|
| `ENVO:00002002` | obsolete food product | obsolete → `FOODON:00001002` |
| `ENVO:00003882` | obsolete **fermented millet food product** | obsolete |
| `ENVO:00003928` | obsolete **pickled food product** | obsolete |
| `ENVO:00002165`, `ENVO:00002216`, `ENVO:0010000`, `ENVO:0010002`, `ENVO:0010049`, `ENVO:0010057` | obsolete meat / plant / animal / cereal / soya / microbial food product | obsolete |

That `ENVO:00003882` *fermented millet food product* was obsoleted rather than generalised is the decisive signal: ENVO retired this space rather than mint a parent for it. **Do not file an ENVO term request for this concept.**

### 2.3 ENVO near-misses and why each fails

| CURIE | Label | Why it is not a match |
|---|---|---|
| `ENVO:00003030` | silage | **Narrower** — one fermented feed among ~20 groups in the bin. Already its own record (`silage_fermentation.yaml`). |
| `ENVO:03600040` | fermentation starter | **Different entity** — the inoculum that initiates fermentation, not the fermented matrix. Already its own record. |
| `ENVO:03600039` / `ENVO:03600090` / `ENVO:03600091` | fermentation pit / alcohol fermentation pit / clay fermentation pit | **Container, not contents.** Also asserts a constructed pit, which 84 of the 86 source strings never claim. |
| `ENVO:00003885` / `ENVO:00003911` | brewery / sake brewery | **Buildings.** Asserts a facility the sources do not claim; also narrower (alcoholic beverages only). |
| `ENVO:01000313` | anthropogenic environment | **Far too broad**; would lose the FOOD/ENGINEERED distinction the FOOD category exists to preserve. |

### 2.4 FoodOn near-misses within the food branch

| CURIE | Label | Why it is not the match |
|---|---|---|
| **`FOODON:00001258`** | **food (fermented)** | **This is the match.** |
| `FOODON:00001304` | food fermentation | **A process, not a material.** *"A fermentation process in which either carbohydrates, proteins or fats are modified."* Grounding a habitat to this would be a category error of exactly the kind the corpus's NOT_APPLICABLE rule guards against. |
| `FOODON:00001314` | fermented meat product | **Narrower** — a child of `FOODON:00001258`; covers one of six groups. |
| `FOODON:00001073` | vinegar food product | **Narrower** — also a child of `FOODON:00001258`. |
| `FOODON:00002158` | food (preserved) | **Overlapping sibling**, not a parent: preservation ≠ fermentation. Already a separate record. |
| `FOODON:03544454` | 44540 - starter cultures (efsa foodex2) | A **food-classification commodity code**, and the inoculum rather than the product. The corpus already rejected it once for exactly this reason (`habitatmech:BACDIVE.9eabedc3a1`). |
| `FOODON:03540941`, `FOODON:03542692`, `FOODON:03400783` | fermented vegetables (efsa) / fermented milk products (efsa) / fermented milk product (eurofir) | **Narrower**, and they carry regulatory-classification baggage the isolation sources never assert. |

---

## 3. Differentia — what distinguishes it from siblings under `food product`

Four differentiae are available, ordered by how well-sourced and how observable they are.

### 3.1 Formation process — desired, microbially driven conversion (the primary differentia)

The ISAPP expert consensus definition, the authoritative reference for this concept, is:

> **"foods made through desired microbial growth and enzymatic conversions of food components"**
> — [Marco ML, Sanders ME, Gänzle M, et al. *Nat Rev Gastroenterol Hepatol* 18:196–208 (2021), doi:10.1038/s41575-020-00390-5](https://doi.org/10.1038/s41575-020-00390-5); [PMID 33398112](https://pubmed.ncbi.nlm.nih.gov/33398112/); [free full text PMC7925329](https://pmc.ncbi.nlm.nih.gov/articles/PMC7925329/)

The panel's explicit inclusion and exclusion criteria give the boundary directly:
- Microorganisms must drive the process; **endogenous enzymes alone are insufficient** (this is what excludes `malted barley`).
- **Live microorganisms need not be present at consumption** — baked bread and pasteurised beer are fermented foods. *This is important for a habitat definition:* the habitat claim is about the fermenting matrix during and shortly after fermentation, which is where isolation actually happens.
- **Excluded:** foods merely *containing* a fermented ingredient (salad dressing made with vinegar), non-fermented foods with microbes added afterwards, and chemically-derived analogues (chemical leavening, synthetic vinegar, non-brewed soy sauce).

### 3.2 Distinguishing from spoiled food — intent, not chemistry

ISAPP is unusually direct here, and this settles the `food (fermented)` vs `food (spoiled)` (`FOODON:00003366`) boundary in HabitatMech's own corpus:

> "both processes occur via microbial growth and enzymatic activity on food constituents" — but spoilage is unintentional, while fermentation is deliberate and controlled to generate desirable attributes ([Marco et al. 2021](https://doi.org/10.1038/s41575-020-00390-5)).

**This differentia is intentional, not physical.** A definition writer should be honest that no measurement of the matrix distinguishes the two; the discriminator is the producer's intent. Note that Madin's own bin contains `spoiled sake`, which straddles the line.

### 3.3 Characteristic physicochemistry — a selective, self-imposed regime

ISAPP gives concrete, citable numbers for the microbiological regime of fermented foods:

> "appreciable levels of fermentation-produced organic acids (>100 mM), combined with low water activity, salt, nitrite and other antimicrobials"; beverages with "4% or more alcohol and pH values less than 4.5 are also considered microbiologically safe" ([Marco et al. 2021](https://doi.org/10.1038/s41575-020-00390-5)).

The key ecological point — and the strongest habitat-specific differentia — is that **the community creates the selective regime it then lives in**. Progressive acidification, oxygen depletion, and accumulation of organic acids and ethanol select for acid- and ethanol-tolerant taxa and drive a reproducible succession ([Auchtung TA, Hallen-Adams HE, Hutkins RW, "Microbial interactions and ecology in fermented food ecosystems," *Nat Rev Microbiol* (2025), doi:10.1038/s41579-025-01191-w](https://doi.org/10.1038/s41579-025-01191-w); [Xu et al., *Compr Rev Food Sci Food Saf* (2024), doi:10.1111/1541-4337.13362](https://doi.org/10.1111/1541-4337.13362)).

### 3.4 Substrate — the strongest empirical structuring variable

If a curator wants a differentia that is measurable and that predicts community composition, substrate is it. Shotgun metagenomics of 58 fermented foods from 8 countries found **food substrate to be the primary factor driving microbial composition**, with samples clustering by dairy / brined-vegetable / sugar-based substrate rather than by geography or producer ([Leech J, Cabrera-Rubio R, Walsh AM, et al., *mSystems* 5(6):e00522-20 (2020), doi:10.1128/mSystems.00522-20](https://doi.org/10.1128/mSystems.00522-20); [PMID 33172966](https://pubmed.ncbi.nlm.nih.gov/33172966/)). This is also the natural basis for any future child terms.

### 3.5 Habitat status is empirically established at scale

Fermented foods are a recognised, distinct microbial habitat with substantial uncultivated diversity:

- **10,899 MAGs** from 2,533 food metagenomes yielded **1,036 prokaryotic and 108 eukaryotic species-level genome bins, 320 of them previously undescribed**; food SGBs account on average for ~3% of the adult and ~56% of the infant gut microbiome ([Carlino N, Blanco-Míguez A, Punčochář M, et al., "Unexplored microbial diversity from 2,500 food metagenomes and links with the human microbiome," *Cell* 187(20):5775–5795.e15 (3 Oct 2024), doi:10.1016/j.cell.2024.07.039](https://doi.org/10.1016/j.cell.2024.07.039); resource: [cFMD](https://github.com/SegataLab/cFMD), [Zenodo](https://zenodo.org/doi/10.5281/zenodo.10891046)).
- Fermented foods are treated in the field as *bona fide* microbial ecosystems — "simple, reproducible, accessible, culturable, and easy-to-manipulate" model communities that are, notably, **not host-associated** ([Wolfe BE & Dutton RJ, "Fermented Foods as Experimentally Tractable Microbial Ecosystems," *Cell* 161(1):49–55 (2015), doi:10.1016/j.cell.2015.02.034](https://doi.org/10.1016/j.cell.2015.02.034); [PMID 25815984](https://pubmed.ncbi.nlm.nih.gov/25815984/)).
- Scale of the concept: **>5,000 varieties** of fermented foods and alcoholic beverages are estimated to be consumed worldwide ([Tamang JP, Watanabe K, Holzapfel WH, *Front Microbiol* 7:377 (2016), doi:10.3389/fmicb.2016.00377](https://doi.org/10.3389/fmicb.2016.00377); [Tamang JP et al., *Compr Rev Food Sci Food Saf* 19(1):184–217 (2020), doi:10.1111/1541-4337.12520](https://doi.org/10.1111/1541-4337.12520)).

### 3.6 Standards recognition

The GSC's MIxS provides four dedicated food environmental extensions — **food-human foods** ([`MIxS:0016022`](https://genomicsstandardsconsortium.github.io/mixs/0016022/)), **food-animal and animal feed** ([`0016019`](https://genomicsstandardsconsortium.github.io/mixs/0016019/)), **food-farm environment** ([`0016020`](https://genomicsstandardsconsortium.github.io/mixs/0016020/)), and **food-food production facility** ([`0016021`](https://genomicsstandardsconsortium.github.io/mixs/0016021/)) — whose slot ranges are drawn from FoodOn (e.g. `food_product_type` → `FOODON:03400361`; `food_product_qual` → `FOODON:00002454`; `microb_start_taxID` for starter cultures). **MIxS's own answer to "which vocabulary names a fermented food sample?" is FoodOn**, which independently corroborates the grounding recommendation. Note also that MIxS's four-way split mirrors the corpus's own matrix / facility / feed distinction in §1.3.

---

## 4. Sources

| # | Claim it supports | Citation |
|---|---|---|
| 1 | Madin isolation_source is a nested ≤4-level vocabulary; provenance of `food_fermented` | Madin JS, Nielsen DA, Brbić M, et al. "A synthesis of bacterial and archaeal phenotypic trait data." *Sci Data* 7:170 (2020). [doi:10.1038/s41597-020-0497-4](https://doi.org/10.1038/s41597-020-0497-4) · data: [figshare 10.6084/m9.figshare.c.4843290](https://doi.org/10.6084/m9.figshare.c.4843290) |
| 2 | The 86 source strings in the bin (§1.2) and the two-way `food` / `food_fermented` split | [`data/conversion_tables/renaming_isolation_source.csv`](https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/blob/master/data/conversion_tables/renaming_isolation_source.csv), bacteria-archaea-traits repo |
| 3 | Consensus definition; inclusion/exclusion criteria; fermentation vs spoilage; live-microbe question; >100 mM organic acids, 4% ethanol, pH <4.5 | Marco ML, Sanders ME, Gänzle M, et al. *Nat Rev Gastroenterol Hepatol* 18:196–208 (2021). [doi:10.1038/s41575-020-00390-5](https://doi.org/10.1038/s41575-020-00390-5) · [PMID 33398112](https://pubmed.ncbi.nlm.nih.gov/33398112/) · [PMC7925329](https://pmc.ncbi.nlm.nih.gov/articles/PMC7925329/) |
| 4 | `FOODON:00001258` label, definition, parents | FoodOn via [OLS4](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?short_form=FOODON_00001258); locally `data/raw/ontology_terms.tsv`, `data/raw/ontology_subclass_edges.tsv` |
| 5 | `FOODON:00001002` genus definition | [OLS4 FOODON:00001002](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?short_form=FOODON_00001002) |
| 6 | ENVO food branch obsoleted, `ENVO:00002002` replaced_by `FOODON:00001002`; `ENVO:00003882`/`ENVO:00003928` obsolete | [OLS4 ENVO](https://www.ebi.ac.uk/ols4/ontologies/envo) |
| 7 | Substrate is the primary driver of fermented-food community composition (58 foods, 8 countries, 127 MAGs) | Leech J, Cabrera-Rubio R, Walsh AM, et al. *mSystems* 5(6):e00522-20 (2020). [doi:10.1128/mSystems.00522-20](https://doi.org/10.1128/mSystems.00522-20) · [PMID 33172966](https://pubmed.ncbi.nlm.nih.gov/33172966/) |
| 8 | 2,533 food metagenomes; 1,036 + 108 SGBs; 320 undescribed; 3% adult / 56% infant gut | Carlino N, Blanco-Míguez A, Punčochář M, et al. *Cell* 187(20):5775–5795.e15 (2024). [doi:10.1016/j.cell.2024.07.039](https://doi.org/10.1016/j.cell.2024.07.039) |
| 9 | Fermented foods as tractable, non-host-associated microbial ecosystems | Wolfe BE, Dutton RJ. *Cell* 161(1):49–55 (2015). [doi:10.1016/j.cell.2015.02.034](https://doi.org/10.1016/j.cell.2015.02.034) |
| 10 | Succession, acidification, cross-kingdom interactions in fermented-food ecosystems | Auchtung TA, Hallen-Adams HE, Hutkins RW. *Nat Rev Microbiol* (2025). [doi:10.1038/s41579-025-01191-w](https://doi.org/10.1038/s41579-025-01191-w) |
| 11 | Vegetable-fermentation succession, salt/oxygen/pH selection | Xu et al. *Compr Rev Food Sci Food Saf* (2024). [doi:10.1111/1541-4337.13362](https://doi.org/10.1111/1541-4337.13362) |
| 12 | >5,000 varieties worldwide; global diversity | Tamang JP, Watanabe K, Holzapfel WH. *Front Microbiol* 7:377 (2016). [doi:10.3389/fmicb.2016.00377](https://doi.org/10.3389/fmicb.2016.00377) · Tamang JP et al. *Compr Rev Food Sci Food Saf* 19(1):184–217 (2020). [doi:10.1111/1541-4337.12520](https://doi.org/10.1111/1541-4337.12520) |
| 13 | MIxS food packages; FoodOn as the range vocabulary | GSC MIxS: [food-human foods 0016022](https://genomicsstandardsconsortium.github.io/mixs/0016022/), [food-animal and animal feed 0016019](https://genomicsstandardsconsortium.github.io/mixs/0016019/), [food-farm environment 0016020](https://genomicsstandardsconsortium.github.io/mixs/0016020/), [food-food production facility 0016021](https://genomicsstandardsconsortium.github.io/mixs/0016021/) |
| 14 | *Methanosaeta harundinacea* 6Ac isolated from a UASB reactor on beer-manufacture wastewater (mis-binning evidence) | Ma K, Liu X, Dong X. *Int J Syst Evol Microbiol* 56:127–131 (2006). [doi:10.1099/ijs.0.63887-0](https://doi.org/10.1099/ijs.0.63887-0) · [BacDive 131756](https://bacdive.dsmz.de/strain/131756) |

### Claims that are my inference, not a source statement

Flagged explicitly so they are not mistaken for cited facts:

- That **silage and animal feed fall inside `FOODON:00001258`** — inferred from FoodOn's `food product` definition covering "humans and animals". No source states this about `FOODON:00001258` directly.
- That **the Madin bin is co-extensive with `FOODON:00001258`** — inferred by inspecting all 86 source strings against ISAPP's criteria. Madin's authors made no ontology mapping.
- That **`malted barley` and `pickle` are mis-binned** — inferred by applying ISAPP's stated criteria to Madin's strings.
- That **the *Methanosaeta* isolate entered the bin via a beer-related string** — the isolation source (bioreactor, not food) is cited; the routing is inference.
- The **habitat-relevant scope note** in §3.1 (that the habitat claim concerns the matrix during/shortly after fermentation, since ISAPP's definition permits dead microbes at consumption) is my reasoning, not ISAPP's.

---

## 5. Synonyms, and what not to conflate

### Names in real use for this concept

- fermented food *(most common)*
- fermented food product
- fermented foods and beverages *(the ISAPP scope phrasing)*
- food (fermented) *(FoodOn / LanguaL parenthetical style)*
- fermented food matrix
- fermented food ecosystem / fermented food microbiome *(used when the community, not the material, is the referent)*
- Existing corpus synonyms already recorded on `food_fermented.yaml`: **"Fermented"** (BacDive), **"Fermented beverages"** (GOLD)
- Additional GOLD path label available for merging: **"Fermented food"** (`Engineered > Food production > Fermented food`, `gold.ecosystem:5597`, 221 organisms — currently the separate UNGROUNDED record `habitatmech:GOLD.8f5ec46a28`)

### Commonly but wrongly treated as the same thing

| Confusable | Why it is different |
|---|---|
| **`FOODON:00001304` food fermentation** | The **process**. A process is not a place. Grounding here would be the same category error as grounding to a PATO quality. |
| **Spoiled food** (`FOODON:00003366`) | Same mechanism, opposite intent ([Marco et al. 2021](https://doi.org/10.1038/s41575-020-00390-5)). Madin's own `spoiled sake` string sits on this line. |
| **Preserved food** (`FOODON:00002158`) | Fermentation is one preservation route; canning, drying and irradiation are preservation without fermentation. |
| **Acidified / pickled-in-vinegar food** | Chemically acidified, no microbial growth. ISAPP explicitly excludes synthetic vinegar and non-brewed soy sauce. |
| **Probiotic food / food with added cultures** | ISAPP explicitly excludes non-fermented foods supplemented with microorganisms. |
| **Starter culture / kefir grain / SCOBY** (`ENVO:03600040`, `FOODON:03544454`) | The **inoculum**, not the fermented product. Already a separate record; already rejected once as a grounding target (`habitatmech:BACDIVE.9eabedc3a1`). |
| **Fermentation vessel, cellar, pit, brewery** (`ENVO:03600039`, `ENVO:00003885`) | Container and built setting. Distinct habitat with distinct biofilm communities (`pit_mud.yaml`, `fermentation_cellar.yaml`). |
| **Industrial bioreactor / anaerobic digester** | Not food. This is exactly what the *Methanosaeta* isolate is, and it is currently inside the bin. |
| **Malted grain** | Endogenous plant enzymes, not microbial conversion. |
| **"Fermentative metabolism"** as an organism trait | A physiological trait of a strain, not a habitat. The lexical collision with "fermented" is a real risk for automated grounding. |

---

## 6. Should this be a term at all?

**Yes — `food_fermented` is unambiguously a habitat.** It is a material entity that microbes inhabit, with a resident community, a characteristic physicochemistry, a reproducible succession, and thousands of sequenced metagenomes (§3.5). It is not a process, a quality, a disease state, a taxon, or a sampling artefact. It should **not** be `NOT_APPLICABLE`.

**But it should not keep a minted HabitatMech identifier, and no ENVO term request should be filed.**

**Recommended decision:**

| Field | Value |
|---|---|
| `identifier` | `habitatmech:BACDIVE.2b1959f1f0` |
| `decision` | `GROUND` |
| `object_id` | `FOODON:00001258` |
| `object_label` | `food (fermented)` |
| `grounding_status` | `CLOSE` |
| `category` | `FOOD` (keep the #57 override; correct and already endorsed) |

**Why `GROUND` rather than `CONFIRM_UNGROUNDED` + term request.** The premise in the research brief — "no term in ENVO, UBERON, FOODON, BTO or PO names the concept" — is not borne out. `FOODON:00001258` names it, is in the vendored slice, is `directly_referenced`, and the corpus **already grounds the identical BacDive bin to it** (`habitatmech:BACDIVE.556e1e04f8`, 2026-08-12). Leaving this record minted publishes two HabitatMech identifiers for one concept and splits 173 Madin taxa away from 242 BacDive strains that belong on the same record. Filing an ENVO request would be worse still: ENVO obsoleted its whole food branch and redirects to FoodOn (§2.2).

**Why `CLOSE` and not `EXACT` or `BROAD`.** The Madin label is a transliteration of the FoodOn label, so this is far tighter than the `BROAD` recorded for BacDive's bare "Fermented". It falls short of `EXACT` in both directions: the bin **under-covers** FoodOn (post-fermentation-killed products like baked bread are `FOODON:00001258` but are never a Madin `food_fermented` isolation source) and **over-covers** it (`malted barley`, vinegar-pickles, and at least one bioreactor isolate — §1.4). `CLOSE` states both honestly; `BROAD` would be defensible if a curator weights the under-coverage more heavily, but `EXACT` would over-claim.

**Follow-on work this exposes** — worth filing regardless of how the above is decided:

1. **`habitatmech:GOLD.8f5ec46a28` "Fermented food"** (`data/habitats/food/fermented_food.yaml`, 221 organisms) is the *same concept from a third source*, still `CONFIRM_UNGROUNDED` from a class-level sweep whose own note says "Whether the concept is a habitat at all was NOT assessed." This research assesses it: it is a habitat, and it grounds to `FOODON:00001258` on identical reasoning. Three records for one concept is the current state.
2. **Record the *Methanosaeta* mis-binning** (§1.4) somewhere durable, so `assertion_count: 173` is read as an upper bound.
3. **If a curator does want HabitatMech's own definition text** rather than FoodOn's thin *"Food material which has been fermented"* — which is arguably circular — the sentence at the top of this report is the one the sources support. FoodOn's definition does not say *desired*, does not say *microbially driven*, and therefore does not, on its own text, exclude spoiled food. That is a genuine defect worth reporting upstream to FoodOn, though **not without your explicit go-ahead for that specific submission.**

## Citations

1. https://doi.org/10.1038/s41597-020-0497-4
2. https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/blob/master/data/conversion_tables/renaming_isolation_source.csv
3. https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?short_form=FOODON_00001002
4. https://doi.org/10.1038/s41575-020-00390-5
5. https://doi.org/10.1099/ijs.0.63887-0
6. https://bacdive.dsmz.de/strain/131756
7. https://www.ebi.ac.uk/ols4/ontologies/envo
8. https://pubmed.ncbi.nlm.nih.gov/33398112/
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC7925329/
10. https://doi.org/10.1038/s41579-025-01191-w
11. https://doi.org/10.1111/1541-4337.13362
12. https://doi.org/10.1128/mSystems.00522-20
13. https://pubmed.ncbi.nlm.nih.gov/33172966/
14. https://doi.org/10.1016/j.cell.2024.07.039
15. https://github.com/SegataLab/cFMD
16. https://zenodo.org/doi/10.5281/zenodo.10891046
17. https://doi.org/10.1016/j.cell.2015.02.034
18. https://pubmed.ncbi.nlm.nih.gov/25815984/
19. https://doi.org/10.3389/fmicb.2016.00377
20. https://doi.org/10.1111/1541-4337.12520
21. https://genomicsstandardsconsortium.github.io/mixs/0016022/
22. https://genomicsstandardsconsortium.github.io/mixs/0016019/
23. https://genomicsstandardsconsortium.github.io/mixs/0016020/
24. https://genomicsstandardsconsortium.github.io/mixs/0016021/
25. https://doi.org/10.6084/m9.figshare.c.4843290
26. https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?short_form=FOODON_00001258