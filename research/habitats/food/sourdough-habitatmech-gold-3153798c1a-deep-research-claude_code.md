---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T00:49:38.329854'
end_time: '2026-08-18T00:59:38.614883'
duration_seconds: 600.29
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Sourdough
  habitat_identifier: habitatmech:GOLD.3153798c1a
  habitat_category: FOOD
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Engineered > Food production > Sourdough'
  assertions: '15'
  parent_terms: FOODON:03530206
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Risky-grounding\
    \ review (#12): the seeder grounded 'Engineered > Food production > Sourdough'\
    \ to FOODON:03302481 'sourdough bread'. Sourdough is the leaven \u2014 a flour-and-water\
    \ culture of lactic acid bacteria and yeast \u2014 and it is the habitat the microbes\
    \ live in; the bread is what it is later baked into, and baking ends the habitat.\
    \ The slice has no term for the starter itself, so this is a term-request candidate\
    \ rather than a grounding. (source concept habitatmech:GOLD.3153798c1a)"
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
  web_search_requests: 15
  num_turns: 37
  total_cost_usd: 3.759176
  session_id: 1e818105-2ede-492d-a032-e166c6bd4083
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 20
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Sourdough
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.3153798c1a
- **Category:** FOOD
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Engineered > Food production > Sourdough
- **Upstream assertion volume:** 15
- **Nearest broader term already on the record:** FOODON:03530206
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Risky-grounding review (#12): the seeder grounded 'Engineered > Food production > Sourdough' to FOODON:03302481 'sourdough bread'. Sourdough is the leaven — a flour-and-water culture of lactic acid bacteria and yeast — and it is the habitat the microbes live in; the bread is what it is later baked into, and baking ends the habitat. The slice has no term for the starter itself, so this is a term-request candidate rather than a grounding. (source concept habitatmech:GOLD.3153798c1a)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Sourdough** as a microbial habitat, with citations.

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

# Sourdough — novel-term research for `habitatmech:GOLD.3153798c1a`

> **A fermentation starter which consists of cereal flour and water acidified by the growth of lactic acid bacteria and yeasts, and which is maintained in a metabolically active state by repeated backslopping until baking ends it.**

Genus term: `ENVO:03600040` *fermentation starter* — already in the vendored slice at `data/raw/ontology_terms.tsv` and already a HabitatMech record (`data/habitats/food/fermentation_starter.yaml`, GOLD `Engineered > Food production > Fermentation starter`, 62 assertions).

**One thing changes the recommendation, and the curator should decide it first:** the note on this record says "the slice has no term for the starter itself." That is true of the *slice* but not of *FoodOn upstream*. FoodOn has **`FOODON:03304099` "sourdough starter"** and **`FOODON:03544457` "44570 - sourdough starter (efsa foodex2)"**. Neither is in `data/raw/ontology_terms.tsv`. Per `CLAUDE.md` ("If a target is not in the slice, vendor the ontology (see #10); do not remove the check"), the correct move may be to vendor rather than mint. Section 2 sets out why I still lean toward minting, and what would change my mind.

---

## 1. What the concept denotes

**The material.** Sourdough is a portion of cereal flour mixed with water and fermented by a resident community of lactic acid bacteria (LAB) and yeasts. It is a semi-solid to viscous matter, held between roughly 20 and 30 °C for traditional (type I) propagation, and kept alive indefinitely by *backslopping* — periodically discarding part of the mass and refreshing the remainder with fresh flour and water. A sample taken "from sourdough" is a scoop of this fermenting flour–water matter.

The German *Leitsätze für Brot und Kleingebäck* (the food-code standard that carries anticipatory expert-opinion status under § 15 LFGB), section **1.1.5**, gives what is effectively already a genus-differentia definition, and it is the single most useful source here:

> "Sauerteig ist ein Teig, dessen Mikroorganismen (z. B. Milchsäurebakterien, Hefen) aus Sauerteig oder Sauerteigstartern sich in aktivem Zustand befinden oder reaktivierbar sind. Sie sind nach Zugabe von Getreideerzeugnissen und Wasser zur fortlaufenden Säurebildung befähigt. Teile eines Sauerteiges werden als Anstellgut für neue Sauerteige verwendet. **Die Lebenstätigkeit der Mikroorganismen wird erst durch Backen oder Kochextrudieren beendet.**"
>
> ("Sourdough is a dough whose microorganisms (e.g. lactic acid bacteria, yeasts), derived from sourdough or sourdough starters, are in an active state or are reactivatable. … Portions of a sourdough are used as *Anstellgut* for new sourdoughs. **The living activity of the microorganisms is ended only by baking or cook-extrusion.**")
> — [Leitsätze für Brot und Kleingebäck, Neufassung 01.04.2021 (BAnz AT 06.05.2021 B2), last amended 22.01.2026 (BAnz AT 06.03.2026 B3), § 1.1.5](https://www.bmleh.de/SharedDocs/Downloads/DE/_Ernaehrung/Lebensmittel-Kennzeichnung/LeitsaetzeBrot.pdf?__blob=publicationFile&v=4)

That last clause is an independent standards-body confirmation of exactly the reasoning in the existing curation note: **the habitat ends at the oven.** It is not an inference this repo has to make on its own.

The scientific literature says the same thing with different words. De Vuyst and colleagues define sourdough as "a cereal flour–water mixture fermented to a low pH by the growth and metabolic action of mainly LAB and yeasts," and treat it as "a specific and stressful ecosystem" characterised by variable carbohydrate concentrations, an acid environment, and limited oxygen availability ([De Vuyst, Van Kerrebroeck & Leroy 2017, *Adv Appl Microbiol* 100:49–160](https://doi.org/10.1016/bs.aambs.2017.02.003)).

**Boundary — inside the concept:**

- The maintained perpetual culture (starter / *Anstellgut* / mother dough / levain / chef), whether at home or in a bakery.
- The bulk sourdough built up from it in a bakery's production cycle, before it is mixed into the final bread dough.
- Type I (spontaneous + daily backslopping), type II (starter-culture-initiated, >30 °C, up to ~5 d) and type 0 / sponge predoughs — all are the same material kind, differing in process parameters, not in what they are ([Böcker, Stolz & Hammes 1995](https://www.google.com/search?q=B%C3%B6cker+Stolz+Hammes+1995+%C3%96kosystem+Sauerteig+Getreide+Mehl+und+Brot+49+370); scheme summarised in [De Vuyst, Comasio & Van Kerrebroeck 2023, *Crit Rev Food Sci Nutr* 63(15):2447–2479](https://doi.org/10.1080/10408398.2021.1976100)).
- Non-wheat/rye sourdoughs (rye, barley, gluten-free, Chinese steamed-bread *laomian*), which are the same habitat kind on a different flour substrate.

**Boundary — outside the concept (neighbouring concepts):**

| Neighbour | Why it is outside | Existing HabitatMech / ontology handle |
|---|---|---|
| **Sourdough bread** — the baked loaf | Baking kills the community; the habitat has ended. | `FOODON:03302481` (the seeder's original wrong grounding) |
| **Bread dough / final dough** | Sourdough is one *ingredient* of it, diluted with fresh flour, water, salt and often baker's yeast. A different material with a different microbiota. | `FOODON:03311552` *dough* |
| **Bread** | Baked. | `FOODON:03000288` (already a record) |
| **Type III dried sourdough** | Spray- or drum-dried after fermentation, used as an acidifier and aroma carrier; the community is largely non-viable, so it is a food additive, not a habitat. Edge case worth an explicit exclusion. | — |
| **A commercial freeze-dried "sourdough starter" sachet** | A manufactured inoculum product, not an actively fermenting mass. Covered by `ENVO:03600040`; becomes sourdough only once hydrated and propagated. | `ENVO:03600040` |
| **Poolish, biga, sponge, *Hefevorteig*** | Yeast pre-ferments leavened with baker's yeast. German food law explicitly distinguishes a *Hefevorteig* from a *Sauerteig*. (Note: a *biga* may in practice be sourdough-based, so the label alone does not decide it.) | — |
| **Flour** (the un-inoculated substrate) | The source of most of the inoculum, not the habitat. | — |

**Is the label ambiguous?** Marginally, and in a way that does not fork the definition. English usage collapses three things: (a) the perpetual starter, (b) the fermenting bulk sourdough, and (c) — colloquially — sourdough bread. Reading (c) is what the seeder picked up, because `FOODON:03302481` *sourdough bread* carries **"sourdough" as an exact synonym**; that lexical fact is the direct cause of the mis-grounding recorded in #12.

Readings (a) and (b) are the same material at different points in one propagation cycle — the mature sourdough *is* the *Anstellgut* for the next batch, which is precisely what the Leitsätze sentence describes. **One term covers both**; splitting them would be an intermediate class this corpus does not need.

The GOLD path settles which reading the data means. GOLD's `Engineered > Food production` branch already carries `Bread production` (380 assertions), `Bread` (2), `Fermented food` (221) and — separately — `Fermentation starter` (62). Sourdough sits alongside all of them as its own node with 15 organism assertions. *(Inference, not a stated GOLD policy:* the existence of a sibling `Bread` node makes the baked-loaf reading implausible for this node, and the 15 assertions are far more consistent with isolate/metagenome sampling of a fermenting mass than of baked bread.*)*

---

## 2. Genus — the broader kind

### Recommended: `ENVO:03600040` *fermentation starter*

> "A manufactured product which assists starting a fermentation process which is intended to prepare foods and alcoholic drinks." (synonym: *Daqu*) — in the vendored slice; ENVO parent `ENVO:00003074` *manufactured product*.

This is the smallest well-established kind in the slice that genuinely subsumes sourdough. Sourdough is the archetypal cereal fermentation starter: it is deliberately propagated, and its technological function is to initiate leavening and acidification of bread dough. Gänzle & Zheng frame both uses this way — sourdough as "a leavening agent (type I sourdoughs) or as a baking improver to enhance flavour, texture, and shelf life of bread (type II sourdoughs)" ([Gänzle & Zheng 2019, *Int J Food Microbiol* 302:15–23](https://doi.org/10.1016/j.ijfoodmicro.2018.08.019), PMID 30172443).

The parenting also aligns HabitatMech's two GOLD nodes sensibly: `Fermentation starter` (62 assertions, already grounded EXACT) becomes the parent of `Sourdough` (15), rather than the two sitting as unrelated siblings inherited from GOLD's flat path structure.

**Caveats the curator should weigh.** ENVO's definition says the starter "assists *starting*" a fermentation. Sourdough both starts the bread-dough fermentation *and is itself* an ongoing fermentation — the ENVO gloss under-describes it. That is under-specification, not contradiction, and is a normal reason for a child class to exist. Separately, "manufactured product" is a slightly awkward ancestor for a home starter that arose by spontaneous colonisation, though it is deliberately propagated by a human, so the fit holds.

### Near-misses (all checked, none a match)

| Candidate | In slice? | Why it fails |
|---|---|---|
| `FOODON:03302481` *sourdough bread* | yes | **Narrower and later.** The baked product; the habitat has been destroyed. The exact synonym "sourdough" on this term is the mis-grounding trap. Keep as `relation: xref` at most. |
| `FOODON:03304099` *sourdough starter* | **no** | The nearest thing to a real match anywhere. See below. |
| `FOODON:03544457` *44570 - sourdough starter (efsa foodex2)* | **no** | Definition is good — "Special mixture of yeasts and bacteria (usually Lactobacilli) for the 'natural' fermentation of bakery products" — but this is an **EFSA FoodEx2 food-classification code**, a marketed-commodity category, not a material-entity class. Wrong axis. |
| `FOODON:03544454` *44540 - starter cultures (efsa foodex2)* | yes | Same problem, plus its own text restricts it to *bacterial* preparations ("any type of bacteria used as starter cultures"), excluding the yeast half of the sourdough community. |
| `FOODON:00001258` *food (fermented)* | yes | **Too broad** and asserts the wrong thing: sourdough is an intermediate, not a food consumed as such. Usable as a fallback genus if `ENVO:03600040` is rejected. |
| `FOODON:03311552` *dough* | **no** | The most *literal* genus — the Leitsätze definition itself starts "Sauerteig ist ein **Teig**." But it is absent from the slice and its FoodOn text is a SIREN facet bundle ("Semisolid, not heat-treated plant part with added grain ingredient"), not a usable definition. |
| `FOODON:00001183` *bread food product* / `FOODON:03000288` *bread* | yes | Baked. |
| `FOODON:03530206` *food production* | yes | **A planned process**, not a material — "A planned process involving the rearing, manufacture or distribution of food material." It is currently the sole `parent_habitats` entry on this record (and on `fermentation_starter.yaml`), inherited from the GOLD path. A process is not *broader than* a material, so per the repo's `parent_habitats` rule this is arguably already a mis-parenting; flagging it, since fixing it is a seeder-level question beyond this one record. |
| `ENVO:00003030` *silage* | yes | Sibling, not parent — another backslopped/spontaneous LAB plant-matter ferment, but forage for ruminants. Useful as a modelling precedent: **ENVO already admits a fermented plant-material mass as an environmental material.** |
| `ENVO:00003885` *brewery*, `ENVO:03600039` *fermentation pit*, `ENVO:03501313–17` *food production environmental monitoring zones* | yes | Sites, vessels and facility zones — the container, not the fermenting matter. |
| `BTO:0000316` *culture medium* | yes | Would assert a laboratory cultivation purpose the sources do not claim. |

### On `FOODON:03304099` — the case for vendoring instead of minting

- **Label match is exact** for the starter reading; GOLD's label is bare "Sourdough."
- **Its "definition" is not a definition.** OLS renders it as a SIREN-DB facet bundle: not heat-treated; seed with seed coat and germ removed (endosperm only); lactic acid fermentation; preserved by fermentation. That is a set of processing attributes, and two of them are wrong or over-claiming for the general case — sourdough is not made only from refined endosperm flour (wholemeal rye is the canonical substrate), and it is not "preserved by fermentation" (it is perpetually refreshed, not preserved).
- **Its asserted parent is `FOODON:00002369` *yeast food product*** — i.e. it is classified as a yeast-based food commodity. For a habitat corpus that is a misplacement: it sorts sourdough with baker's yeast products rather than with fermentation starters or environmental materials, and it foregrounds the yeast over the LAB that numerically dominate by two orders of magnitude (§3).

**Recommendation.** Mint, with `FOODON:03304099` recorded as `relation: xref`. The existing `CONFIRM_UNGROUNDED` decision holds, but its *reason* should be amended: not "the slice has no term" (which invites a future re-reading as "so vendor it and ground it"), but "FoodOn's `sourdough starter` is a commodity-classification node under *yeast food product* with a facet-bundle gloss and no habitat definition, so grounding to it would import claims the sources do not make." If the curator disagrees and prefers vendoring, the honest disposition is `GROUND_AS_PARENT` on `ENVO:03600040` with `FOODON:03304099` as xref — *not* a plain `GROUND`, because the FoodOn term's endosperm-only and preservation axioms are narrower than what GOLD's 15 assertions attest.

---

## 3. Differentia — what distinguishes it

Ordered strongest-evidence first. Items 1–4 are the ones I would put in the definition sentence; 5–7 are corroborating detail for the record's notes.

**1. Substrate: cereal flour and water, and nothing essential besides.** The definitional composition across every source. The Leitsätze add a regulatory sharpening that is a clean, checkable differentia against imitations: "Die Säurezunahme des Sauerteigs beruht ausschließlich auf dessen natürlicher Fermentation. Den Säuregehalt (Säuregrad) beeinflussende Zutaten (z. B. organische Säuren, Teigsäuerungsmittel) werden nicht verwendet" — the acidity increase rests **exclusively** on natural fermentation; no added organic acids or dough acidulants ([Leitsätze § 1.1.5](https://www.bmleh.de/SharedDocs/Downloads/DE/_Ernaehrung/Lebensmittel-Kennzeichnung/LeitsaetzeBrot.pdf?__blob=publicationFile&v=4)).

**2. A two-domain community, LAB-dominated by ~1–2 orders of magnitude.** This is the sharpest measurable separator from every yeast pre-ferment (poolish, biga, *Hefevorteig*) on one side and from purely bacterial starter cultures on the other:

- LAB ≥ 10⁸ CFU/g; yeasts ≤ 10⁷ CFU/g; **LAB:yeast ratio ~10:1 to 100:1** ([De Vuyst, Van Kerrebroeck & Leroy 2017](https://doi.org/10.1016/bs.aambs.2017.02.003)).
- Corroborated: "LAB dominate the mature SD, while the yeast content is one/two logarithmic cycles lower" — LAB ~10⁸ CFU/g, yeasts ~10⁶–10⁷ CFU/g ([Pérez-Alvarado et al. 2022, *Front Microbiol* 13:969460](https://doi.org/10.3389/fmicb.2022.969460)).
- And in the largest survey to date: LAB + acetic acid bacteria together made up **over 97 % of bacterial reads**, and *Saccharomyces cerevisiae* exceeded 50 % of fungal ITS reads in **77 %** of 500 starters ([Landis et al. 2021, *eLife* 10:e61644](https://doi.org/10.7554/eLife.61644)).

**3. Acidification is the defining physicochemical state.** Mature sourdough is an acidic, low-oxygen ecosystem; pH 4.0 is reported as the borderline value governing prevalence of the sourdough-specialist LAB ([De Vuyst et al. 2017](https://doi.org/10.1016/bs.aambs.2017.02.003); [De Vuyst et al. 2023](https://doi.org/10.1080/10408398.2021.1976100)). Acidification is delivered by lactic and acetic acid from the LAB. *(I did not find an authoritative source stating a single canonical pH window such as "3.5–4.5"; pH and TTA are always reported as process-dependent. I would not put a numeric pH range in the definition sentence.)*

**4. Perpetuation by backslopping — the process property that makes it a durable habitat.** Backslopping is "cyclic reinoculation of a so-called 'mother dough' using a newly prepared batch of flour and water"; type I sourdough is spontaneous fermentation followed by daily backslopping ([Vrancken et al. 2011, *Appl Environ Microbiol* 77(8):2716–2726](https://doi.org/10.1128/AEM.02470-10), PMID 21335386). Home practice varies from 12-hourly to monthly refreshment, and starters "can be tens or even hundreds of years old" ([Calvert et al. 2021, *PeerJ* 9:e11389](https://doi.org/10.7717/peerj.11389)).

This is not merely a husbandry detail — it is what makes sourdough ecologically distinct from a one-off cereal ferment. Gänzle & Zheng's central argument: "The long-term propagation of sourdoughs eliminates dispersal limitation and consistently leads to sourdough microbiota that are composed of host-adapted lactobacilli," whereas community assembly in spontaneous cereal fermentations is dispersal-limited and dominated by nomadic or environmental LAB ([Gänzle & Zheng 2019](https://doi.org/10.1016/j.ijfoodmicro.2018.08.019)).

**5. Terminated by baking.** Stated by the Leitsätze as quoted, and by [Pérez-Alvarado et al. 2022](https://doi.org/10.3389/fmicb.2022.969460), which describes baking at 200–250 °C as terminating microbial cell viability. This is the differentia that separates the habitat from `FOODON:03302481` *sourdough bread*, and the one the existing curation note turns on.

**6. Characteristic taxa (evidential, not definitional — do not put in the definition).** *Fructilactobacillus sanfranciscensis* (formerly *Lactobacillus sanfranciscensis*, reclassified in [Zheng et al. 2020, *IJSEM* 70(4):2782–2858](https://doi.org/10.1099/ijsem.0.004107), PMID 32293557) is the sourdough specialist, maltose-dependent, and reported as effectively restricted to traditional sourdough. Also prevalent: *Lactiplantibacillus plantarum*, *Levilactobacillus brevis*, *Leuconostoc citreum*, *Companilactobacillus* spp.; yeasts *S. cerevisiae*, *Kazachstania humilis*, *Torulaspora delbrueckii*, *Wickerhamomyces anomalus* ([De Vuyst et al. 2014, *Food Microbiol* 37:11–29](https://doi.org/10.1016/j.fm.2013.06.002), PMID 24230469; [Landis et al. 2021](https://doi.org/10.7554/eLife.61644)). Two new species were described from sourdough as recently as 2025 — *Fructilactobacillus frigidiflavus* and *Levilactobacillus lettrarii* ([*IJSEM*, doi:10.1099/ijsem.0.006726](https://doi.org/10.1099/ijsem.0.006726)) — so the habitat is still yielding novel taxa.

**7. Process parameters that vary within the concept (so: not differentia, but good `environment_parameters` candidates).** Dough yield DY = (flour + water) × 100 / flour; DY ≤ 200 for firm type I, 330–400 for liquid sourdoughs. Type I: 20–30 °C, 5–24 h per cycle; type II: >30 °C, up to ~5 days ([De Vuyst et al. 2023](https://doi.org/10.1080/10408398.2021.1976100); [Van Kerrebroeck, Maes & De Vuyst 2017, *Trends Food Sci Technol* 68:152–159](https://doi.org/10.1016/j.tifs.2017.08.016)). Temperature and backslopping interval strongly restructure the community: 23 °C/24 h → *Leuconostoc citreum*-dominated; 30 and 37 °C/24 h → *Limosilactobacillus fermentum*-dominated ([Vrancken et al. 2011](https://doi.org/10.1128/AEM.02470-10)).

Note that MIxS v6's **food-humanFoods** package provides exactly the slots this habitat needs — `ferm_medium`, `ferm_pH`, `ferm_temp`, `ferm_time`, `ferm_vessel`, `ferm_headspace_oxy`, `ferm_rel_humidity` ([GSC MIxS, Food-humanFoods](https://genomicsstandardsconsortium.github.io/mixs/Food-humanFoods/); [NCBI BioSample MIMS.me.food-human_foods.6.0](https://www.ncbi.nlm.nih.gov/biosample/docs/packages/MIMS.me.food-human_foods.6.0/)). That the GSC built dedicated fermentation-context slots is independent evidence that fermenting food matter is a recognised sampled environment, though the package does not itself name sourdough.

---

## 4. Sources

Ranked by usefulness for writing and defending the definition.

| # | Source | What it supports | Access |
|---|---|---|---|
| 1 | **Leitsätze für Brot und Kleingebäck § 1.1.5**, Deutsches Lebensmittelbuch, Neufassung 01.04.2021 (BAnz AT 06.05.2021 B2, GMBl 29/2021 S. 654–659), last amended 22.01.2026 (BAnz AT 06.03.2026 B3) | The near-verbatim genus-differentia definition; *Anstellgut*/backslopping; **"activity ended only by baking"**; no added acidulants | [PDF](https://www.bmleh.de/SharedDocs/Downloads/DE/_Ernaehrung/Lebensmittel-Kennzeichnung/LeitsaetzeBrot.pdf?__blob=publicationFile&v=4) |
| 2 | De Vuyst L, Van Kerrebroeck S, Leroy F (2017). Microbial Ecology and Process Technology of Sourdough Fermentation. *Adv Appl Microbiol* 100:49–160 | "Cereal flour–water mixture fermented to a low pH"; "specific and stressful ecosystem"; LAB ≥10⁸ / yeast ≤10⁷ CFU/g; 10:1–100:1 | [doi:10.1016/bs.aambs.2017.02.003](https://doi.org/10.1016/bs.aambs.2017.02.003) |
| 3 | De Vuyst L, Comasio A, Van Kerrebroeck S (2023). Sourdough production: fermentation strategies, microbial ecology, and use of non-flour ingredients. *Crit Rev Food Sci Nutr* 63(15):2447–2479 | Type 0/I/II/III scheme; dough yield; temperature regimes; mature-sourdough ecology | [doi:10.1080/10408398.2021.1976100](https://doi.org/10.1080/10408398.2021.1976100) · PMID 34523363 · open access |
| 4 | Gänzle MG, Zheng J (2019). Lifestyles of sourdough lactobacilli — Do they matter for microbial ecology and bread quality? *Int J Food Microbiol* 302:15–23 | Backslopping eliminates dispersal limitation → host-adapted specialist microbiota; the ecological argument that sourdough is a distinct persistent habitat | [doi:10.1016/j.ijfoodmicro.2018.08.019](https://doi.org/10.1016/j.ijfoodmicro.2018.08.019) · PMID 30172443 · [author MS, U. Alberta ERA](https://era.library.ualberta.ca/items/703d6375-52f5-4831-b01e-e44cd3ad7736) |
| 5 | Landis EA, Oliverio AM, McKenney EA, et al. (2021). The diversity and function of sourdough starter microbiomes. *eLife* 10:e61644 | 500 starters, 4 continents; LAB+AAB >97 % of bacterial reads; *S. cerevisiae* >50 % of fungal reads in 77 %; median 7 bacterial / 35 fungal ASVs; **no biogeographic signal**; AAB drive rise rate and aroma | [doi:10.7554/eLife.61644](https://doi.org/10.7554/eLife.61644) · [PMC7837699](https://pmc.ncbi.nlm.nih.gov/articles/PMC7837699/) · open access |
| 6 | Calvert MD, Madden AA, Nichols LM, et al. (2021). A review of sourdough starters: ecology, practices, and sensory quality… *PeerJ* 9:e11389 | Starter as "a culture of unique and complex microorganisms"; backslopping/refreshing terminology and intervals; starters "tens or even hundreds of years old"; >60 common LAB species; ~100:1 bacteria:yeast; explicit framing of starters as distinct microbial ecosystems | [doi:10.7717/peerj.11389](https://doi.org/10.7717/peerj.11389) · [PMC8117929](https://pmc.ncbi.nlm.nih.gov/articles/PMC8117929/) · open access |
| 7 | Vrancken G, Rimaux T, Weckx S, Leroy F, De Vuyst L (2011). Influence of temperature and backslopping time on the microbiota of a type I propagated laboratory wheat sourdough fermentation. *Appl Environ Microbiol* 77(8):2716–2726 | Operational definition of backslopping; temperature/interval → community composition | [doi:10.1128/AEM.02470-10](https://doi.org/10.1128/AEM.02470-10) · PMID 21335386 |
| 8 | De Vuyst L, Van Kerrebroeck S, Harth H, Huys G, Daniel HM, Weckx S (2014). Microbial ecology of sourdough fermentations: diverse or uniform? *Food Microbiol* 37:11–29 | Intrinsic (flour) vs extrinsic (T, pH, DY, backslopping) determinants of the microbiota | [doi:10.1016/j.fm.2013.06.002](https://doi.org/10.1016/j.fm.2013.06.002) · PMID 24230469 |
| 9 | Pérez-Alvarado O, et al. (2022). Role of lactic acid bacteria and yeasts in sourdough fermentation during breadmaking. *Front Microbiol* 13:969460 | Definition; cell counts; >90 LAB species; **baking at 200–250 °C terminates viability** | [doi:10.3389/fmicb.2022.969460](https://doi.org/10.3389/fmicb.2022.969460) · [PMC9524358](https://pmc.ncbi.nlm.nih.gov/articles/PMC9524358/) · open access |
| 10 | Zheng J, Wittouck S, Salvetti E, et al. (2020). A taxonomic note on the genus *Lactobacillus*… *IJSEM* 70(4):2782–2858 | *Lactobacillus sanfranciscensis* → *Fructilactobacillus sanfranciscensis*; use current names in any note | [doi:10.1099/ijsem.0.004107](https://doi.org/10.1099/ijsem.0.004107) · PMID 32293557 · open access |
| 11 | Böcker G, Stolz P, Hammes WP (1995). *Getreide, Mehl und Brot* 49:370–374 | Origin of the type I/II/III scheme | print; scheme restated in #3 |
| 12 | Van Kerrebroeck S, Maes D, De Vuyst L (2017). Sourdoughs as a function of their species diversity and process conditions, a meta-analysis. *Trends Food Sci Technol* 68:152–159 | DY formula and values; type I vs II diversity contrast | [doi:10.1016/j.tifs.2017.08.016](https://doi.org/10.1016/j.tifs.2017.08.016) |
| 13 | GSC MIxS v6 food-humanFoods package / NCBI BioSample MIMS.me.food-human_foods.6.0 | Fermentation metadata slots for a food-matrix sample | [GSC](https://genomicsstandardsconsortium.github.io/mixs/Food-humanFoods/) · [NCBI](https://www.ncbi.nlm.nih.gov/biosample/docs/packages/MIMS.me.food-human_foods.6.0/) |
| 14 | OLS4 / FoodOn term records: `FOODON:03304099`, `FOODON:03544457`, `FOODON:03302481`, `FOODON:03311552`, `FOODON:00002369` | The upstream terms that exist and their actual axioms/parents | [OLS4](https://www.ebi.ac.uk/ols4/ontologies/foodon) |

### Claims that are my inference, not a source statement

Flagging these explicitly, since the report will be read as evidence:

1. **That GOLD's "Sourdough" node means the fermenting material rather than the baked loaf.** Inferred from GOLD's own path structure (sibling `Bread` and `Bread production` nodes) plus the nature of the 15 organism assertions. I found no GOLD documentation defining the node.
2. **That the maintained starter and the bulk production sourdough should share one term.** My judgement, grounded in the Leitsätze's own treatment of *Anstellgut* as a portion of a sourdough rather than a different kind of thing. A curator could reasonably split them; I think that manufactures an intermediate class with no sampling consequence.
3. **That `ENVO:03600040` is genuinely broader than sourdough.** Follows from ENVO's text plus the literature's description of sourdough's technological function, but ENVO has not asserted this subsumption. Type III dried sourdough is the case that most strains it.
4. **That `FOODON:03530206` *food production* is a defective `parent_habitats` value** (process vs. material). My reading of the repo's own `parent_habitats` rule against FoodOn's definition of that term; no source says this.
5. **That FOODON's placement of `sourdough starter` under *yeast food product* is a misclassification for habitat purposes.** My assessment, supported by the LAB-dominance data in #2/#5/#6 but not stated by FoodOn.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept** (candidates for `synonyms`, with a suggested type):

| Term | Type | Note |
|---|---|---|
| sourdough starter | EXACT | commonest English name for the maintained form; the FoodOn label |
| sourdough culture | EXACT | |
| leaven / natural leaven | EXACT | |
| levain | EXACT | French; in US artisan usage sometimes narrowed to "the offshoot built for one bake," which is still the same material |
| levain-chef / chef | EXACT | French, for the perpetual mother |
| mother dough / mother / mother culture | EXACT | |
| Sauerteig | EXACT | German; the Leitsätze term |
| Anstellgut | RELATED | German for the seed portion carried forward — a role, not a distinct material |
| lievito naturale / lievito madre / pasta madre | EXACT | Italian |
| masa madre | EXACT | Spanish |
| desem | EXACT | Dutch/Flemish |
| 老面 *laomian* / "old dough" | EXACT | Chinese, for steamed-bread sourdough |
| type I / type II / type III sourdough | NARROW | process subtypes, not synonyms |
| starter | BROAD | ambiguous alone — covers dairy, meat, brewing starters |

Two more sit at the edge and I would leave them off: **"sponge"** and **"predough"** (= type 0), which in most bakery usage denote yeast-leavened pre-ferments; and **"discard"**, the portion removed at each refreshment — same material, but as a waste/by-product role rather than a habitat name.

**Commonly but wrongly treated as the same thing:**

1. **Sourdough bread** (`FOODON:03302481`) — the highest-risk conflation, because "sourdough" is an *exact synonym* on that FoodOn term, which is what produced the original bad grounding. Baking ends the habitat.
2. **Bread dough / final dough** — sourdough is an ingredient of it, typically 10–30 % of flour weight, and the mixture is a different material with a different (diluted, often baker's-yeast-supplemented) microbiota.
3. **Poolish, biga, sponge, *Hefevorteig*** — yeast pre-ferments. German food law explicitly distinguishes *Hefevorteig* from *Sauerteig*.
4. **Baker's yeast / compressed yeast / "wild yeast"** — an organism or a single-species product, not the habitat. Type II and III sourdoughs *require added baker's yeast* for leavening, which shows the two are separable things.
5. **Commercial dried "sourdough starter" sachets, and type III dried sourdough** — manufactured acidifier/inoculum products, not actively fermenting masses. `ENVO:03600040` already covers them.
6. **A "sourdough starter culture" in the microbiologist's sense** — a defined LAB/yeast strain cocktail, i.e. an inoculum, not the fermenting community in situ.
7. **Flour** — the substrate and principal inoculum source, not the habitat.
8. **Other backslopped ferments** (kefir grains, kombucha SCOBY, *Daqu*, silage `ENVO:00003030`) — ecologically analogous, materially distinct. `Daqu` is already an ENVO synonym on the proposed genus, so guard against sourdough being absorbed into it.
9. **"Sourdough" as a US regional bread style** (e.g. San Francisco sourdough) — a product designation, not this concept.

---

## 6. Should this be a term at all?

**Yes.** It clears every test the corpus applies:

- **It is a place microbes live, not a process, quality, disease or taxon.** It is a bounded portion of material with a resident community, a characteristic physicochemistry (acidic, low-oxygen, maltose-rich), and a defined temporal extent (from first fermentation to the oven). The literature calls it an "ecosystem" and a "habitat" in those words ([De Vuyst et al. 2017](https://doi.org/10.1016/bs.aambs.2017.02.003); [Calvert et al. 2021](https://doi.org/10.7717/peerj.11389)).
- **It is not a sampling artefact.** 500 independently sampled starters across four continents, with 15 GOLD organism assertions on this node alone.
- **It has a resident, adapted biota that other habitats do not.** *Fructilactobacillus sanfranciscensis* is reported as effectively restricted to traditional sourdough, and its maltose dependence is a direct adaptation to this substrate ([Gänzle & Zheng 2019](https://doi.org/10.1016/j.ijfoodmicro.2018.08.019)). Novel species were still being described from it in 2025.
- **It has real curatorial consequence.** Without this term, 15 organism assertions either sit UNGROUNDED or get absorbed into `sourdough bread` — a baked product — and the corpus publishes the claim that microbes were isolated from a loaf.

Not a `NOT_APPLICABLE` candidate on any reading.

### Concrete disposition I would record

- **Decision:** keep `CONFIRM_UNGROUNDED` on `habitatmech:GOLD.3153798c1a`, **but amend the note** — the slice-emptiness argument is weaker than the real one, which is that FoodOn's `sourdough starter` (`FOODON:03304099`) is a food-commodity node under *yeast food product* with a SIREN facet bundle in place of a definition, whose endosperm-only and "preserved by fermentation" axioms over-claim relative to what GOLD attests.
- **`parent_habitats`:** `ENVO:03600040` *fermentation starter* as `relation: parent` (genuinely broader; already a HabitatMech record; keeps the two GOLD food-fermentation nodes in one hierarchy). Retain `FOODON:03530206` only if the seeder requires it — noting it is a process, not a broader material.
- **`relation: xref`** for `FOODON:03304099` *sourdough starter* and `FOODON:03302481` *sourdough bread* — the links upstream saw and the seeder mistook, recorded without this repo asserting identity or is-a.
- **Term-request payload:** label *sourdough*; the definition sentence at the top; sources #1, #2, #4, #5 as the definitional citations; synonyms per §5. The Leitsätze § 1.1.5 sentence is the strongest single citation, because it is a standards-body text that already states the genus, the community, the propagation and the endpoint.
- **Cautions for whoever writes the record:** do not put a numeric pH range in the definition (no source gives a canonical window); do not name taxa in the definition (they vary by flour, temperature and geography, and *L. sanfranciscensis* is now *Fructilactobacillus*); do not write "preserved by fermentation" (FoodOn's phrasing, and wrong — sourdough is perpetuated, not preserved).

---

**Sources:**
- [Leitsätze für Brot und Kleingebäck (BMLEH, 2021/2026)](https://www.bmleh.de/SharedDocs/Downloads/DE/_Ernaehrung/Lebensmittel-Kennzeichnung/LeitsaetzeBrot.pdf?__blob=publicationFile&v=4)
- [De Vuyst, Van Kerrebroeck & Leroy 2017, *Adv Appl Microbiol*](https://doi.org/10.1016/bs.aambs.2017.02.003)
- [De Vuyst, Comasio & Van Kerrebroeck 2023, *Crit Rev Food Sci Nutr*](https://doi.org/10.1080/10408398.2021.1976100)
- [Gänzle & Zheng 2019, *Int J Food Microbiol*](https://doi.org/10.1016/j.ijfoodmicro.2018.08.019)
- [Landis et al. 2021, *eLife*](https://doi.org/10.7554/eLife.61644)
- [Calvert et al. 2021, *PeerJ*](https://doi.org/10.7717/peerj.11389)
- [Vrancken et al. 2011, *Appl Environ Microbiol*](https://doi.org/10.1128/AEM.02470-10)
- [De Vuyst et al. 2014, *Food Microbiol*](https://doi.org/10.1016/j.fm.2013.06.002)
- [Pérez-Alvarado et al. 2022, *Front Microbiol*](https://doi.org/10.3389/fmicb.2022.969460)
- [Zheng et al. 2020, *IJSEM*](https://doi.org/10.1099/ijsem.0.004107)
- [Van Kerrebroeck, Maes & De Vuyst 2017, *Trends Food Sci Technol*](https://doi.org/10.1016/j.tifs.2017.08.016)
- [*Fructilactobacillus frigidiflavus* / *Levilactobacillus lettrarii* sp. nov., *IJSEM* 2025](https://doi.org/10.1099/ijsem.0.006726)
- [GSC MIxS v6 Food-humanFoods package](https://genomicsstandardsconsortium.github.io/mixs/Food-humanFoods/)
- [NCBI BioSample MIMS.me.food-human_foods.6.0](https://www.ncbi.nlm.nih.gov/biosample/docs/packages/MIMS.me.food-human_foods.6.0/)
- [EBI OLS4 — FoodOn](https://www.ebi.ac.uk/ols4/ontologies/foodon)

## Citations

1. https://www.bmleh.de/SharedDocs/Downloads/DE/_Ernaehrung/Lebensmittel-Kennzeichnung/LeitsaetzeBrot.pdf?__blob=publicationFile&v=4
2. https://doi.org/10.1016/bs.aambs.2017.02.003
3. https://www.google.com/search?q=B%C3%B6cker+Stolz+Hammes+1995+%C3%96kosystem+Sauerteig+Getreide+Mehl+und+Brot+49+370
4. https://doi.org/10.1080/10408398.2021.1976100
5. https://doi.org/10.1016/j.ijfoodmicro.2018.08.019
6. https://doi.org/10.3389/fmicb.2022.969460
7. https://doi.org/10.7554/eLife.61644
8. https://doi.org/10.1128/AEM.02470-10
9. https://doi.org/10.7717/peerj.11389
10. https://doi.org/10.1099/ijsem.0.004107
11. https://doi.org/10.1016/j.fm.2013.06.002
12. https://doi.org/10.1099/ijsem.0.006726
13. https://doi.org/10.1016/j.tifs.2017.08.016
14. https://genomicsstandardsconsortium.github.io/mixs/Food-humanFoods/
15. https://www.ncbi.nlm.nih.gov/biosample/docs/packages/MIMS.me.food-human_foods.6.0/
16. https://era.library.ualberta.ca/items/703d6375-52f5-4831-b01e-e44cd3ad7736
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC7837699/
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC8117929/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC9524358/
20. https://www.ebi.ac.uk/ols4/ontologies/foodon