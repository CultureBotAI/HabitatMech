---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T22:42:57.059644'
end_time: '2026-08-17T22:53:23.908109'
duration_seconds: 626.85
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Cooling-tower
  habitat_identifier: habitatmech:BACDIVE.71d5f01e03
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Cooling-tower'
  assertions: '26'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Cohort
    review: NCIT:C48957 ''Tower'' is a structure of any kind. The slice has cooling
    processes and ENVO:03600002 ''cooling water'' but no cooling tower; the water
    is the medium, not the site. A Legionella habitat worth an ENVO term request.
    (source concept habitatmech:BACDIVE.71d5f01e03)'
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
  web_search_requests: 14
  num_turns: 47
  total_cost_usd: 3.7978005000000006
  session_id: 0c6c7370-d324-4447-bc71-acb1177b1b52
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 33
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Cooling-tower
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.71d5f01e03
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Cooling-tower
- **Upstream assertion volume:** 26
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Cohort review: NCIT:C48957 'Tower' is a structure of any kind. The slice has cooling processes and ENVO:03600002 'cooling water' but no cooling tower; the water is the medium, not the site. A Legionella habitat worth an ENVO term request. (source concept habitatmech:BACDIVE.71d5f01e03)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Cooling-tower** as a microbial habitat, with citations.

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

# Cooling-tower — novel-term definition research

**Target:** `habitatmech:BACDIVE.71d5f01e03` · label *Cooling-tower* · category OTHER · UNGROUNDED · BacDive, 26 strains / 23 taxa

---

## Proposed definition

> A human construction which rejects waste heat from a recirculating water loop by evaporating part of that water into an air stream drawn through the structure, and which retains the remaining water in an open basin between passes.

That single sentence carries the whole load only because the genus available in ENVO (`ENVO:00000070` *human construction*) is very broad. **The intermediate class that ought to sit between them — an *evaporative cooling system* / *evaporative heat rejection device*, the umbrella the HSE and ASHRAE both use to cover cooling towers together with evaporative condensers and evaporative fluid coolers — does not exist in ENVO.** Recommending it alongside the cooling-tower term is more useful than lengthening the sentence (§2 below).

---

## 1. What the concept denotes

**The reading the data means.** BacDive's `Cooling-tower` is a sampling site, not a device catalogue entry. The material a strain is actually recovered from is one of three things inside the structure:

1. **recirculating (basin/bulk) water** — by far the commonest,
2. **biofilm** on the fill, distribution deck, drift eliminators and basin walls,
3. **sediment / sludge / deposits** in the cold-water basin and under-deposit anaerobic microniches.

The record's own characteristic taxa confirm this reading unambiguously. Thirteen of the 23 taxa are *Legionella* or *Fluoribacter* (an obligate freshwater/amoeba-associated genus); three are *Allofrancisella* spp., a genus erected entirely from cooling-system water; *Reyranella massiliensis* was recovered by amoebal co-culture from cooling-tower water; and *Desulfotomaculum* sp. DSM 7440 — the highest-count taxon at 3 strains — is recorded by DSMZ with isolation source **"cooling tower water"**, cultivated anaerobically at 50 °C ([DSMZ DSM 7440](https://www.dsmz.de/collection/catalogue/details/culture/DSM-7440)). That last one is important: it shows the concept's extent includes the anoxic deposit niche, not only the aerated bulk water.

**Boundary — what is inside.** The whole open-recirculating structure and its contained water: distribution deck, fill, air inlets, fan/plenum, drift eliminators, cold-water basin, and the make-up/blow-down connections. Both scale classes are the same concept: rooftop packaged HVAC towers serving chillers, and field-erected industrial/power-station towers (mechanical- or natural-draft hyperboloid). BacDive's 26 strains almost certainly span both — the HVAC/*Legionella* isolates and the thermophilic sulfate-reducer point in different directions.

**Boundary — what is adjacent, not inside.**

| Neighbouring concept | Why it is outside |
|---|---|
| **Evaporative condenser** | Refrigerant condenser coils sit *directly in the wet air stream*; the water sprayed over them is not the process fluid ([OSHA](https://www.osha.gov/legionnaires-disease/control-prevention)). Sister concept under the same missing genus, not the same thing. |
| **Closed-circuit fluid cooler** | Process fluid stays inside a coil; a separate spray-water circuit evaporates over it. Same sister relation. |
| **Dry cooler / air-cooled condenser / radiator** | No evaporation, no open water, approaches dry-bulb rather than wet-bulb temperature. **Not a microbial habitat of this kind at all.** |
| **Air conditioner** (BacDive's own sibling source, `bacdive.isolation_source:air-conditioner`, 16 strains) | Denotes the air-handling side — condensate pans, coils, filters, ducts. Distinct sampled material. |
| **Cooling water** as a *material* (`ENVO:03600002`) | The medium, not the site — and broader, since it also covers once-through and closed-loop coolant that never enters a tower. This is exactly the distinction the curator's existing note already drew, and it holds. |
| **Cooling pond / spray pond** | Evaporative, but a water body rather than a construction with forced or induced draught through fill. |
| **Humidifier, air washer, misting/atomizing system, decorative fountain** | Also aerosol-generating recirculating water, also *Legionella* risk, also outside — grouped separately even in the regulations that lump them for risk-management purposes (HSE HSG274 Part 3 vs Part 1). |

**Residual ambiguity, stated rather than resolved:** the label alone does not distinguish HVAC-scale from power-plant-scale towers, and does not say whether the sample was water, biofilm or deposit. I recommend the term cover both scales (they are the same functional structure and the literature treats them as one class), and that the site/material distinction be handled the way ENVO already handles it elsewhere — one site term, with material recorded separately.

---

## 2. Genus — the broader kind

### Nothing in the target ontologies names this concept

Confirmed by direct query, not by assumption:

- **ENVO**: OLS search for `tower` in ENVO returns exactly one hit, `ENVO:01000754` *fumarole-derived ice tower*. Search for `cooling` in ENVO returns 40 hits, all processes (`ENVO:03000146` *water cooling*, `ENVO:01001615` *material cooling process*, `ENVO:01001735–8` cooling of a gas/liquid/solid/fluid), one material (`ENVO:03600002` *cooling water*), one katabatic wind, one *cold room*. No device, no site.
- **UBERON, FOODON, BTO, PO, OBI, MeSH, EFO**: no `tower` hit of any kind.
- **NCIT**: only `NCIT:C48957` *Tower* — "a structure of any kind", which is what the upstream mapping table already recorded as a `skos:closeMatch` at medium confidence via lexical matching. That is a lexical accident, not a semantic match.
- **ENVO GitHub issue tracker**: zero open or closed issues matching `cooling tower`, `cooling` in title, or `legionella`. **No new-term request exists yet.**

### The genus to use

**`ENVO:00000070` *human construction*** — "A construction that has been assembled by deliberate human effort", itself a child of `ENVO:01001813` *construction* and part of `ENVO:01000983` *technosphere*. This is the smallest well-established ENVO kind the concept falls under.

Honest tension worth recording: a packaged rooftop tower arrives as a factory-assembled unit and reads equally as `ENVO:00003074` *manufactured product*; a field-erected hyperboloid tower is unambiguously a construction. *Human construction* covers both without strain ("assembled by deliberate human effort" does not specify where), and it keeps the term in the environmental/site branch rather than the artefact branch, which is what a habitat term needs. This is my judgement call, not something a source states.

### Near-misses and why each fails

| Candidate | Why it is not a match |
|---|---|
| `ENVO:03600002` **cooling water** | Material, not site; and broader — includes coolant that never enters a tower. |
| `ENVO:03000146` **water cooling** | A process. A habitat is not a process. |
| `ENVO:00002874` **air conditioning unit** | Asserts a function the concept does not have — a tower serving refinery process cooling or a power-station condenser conditions no air. Also narrower in another direction (device-scale). |
| `ENVO:00000025` **reservoir** | "An artificial body of water… constructed for the purpose of water storage." Storage is not the function; and a reservoir is a water body, not a heat-rejection structure. |
| `ENVO:00002214` **power plant**, `ENVO:00003861` **industrial building**, `ENVO:01000536` **factory** | Whole facilities containing towers. Grounding here would inflate the sampled site by orders of magnitude. |
| `ENVO:01000989` **plumbing fixture** (and `ENVO:01000924` *plumbing drain*, `ENVO:01000992` *shower fixture*) | Wrong branch — potable/domestic water. **But precedential:** ENVO does already model built water infrastructure at this granularity, which is the strongest argument that a cooling-tower term belongs in ENVO too. |
| `ENVO:00002043` **wastewater treatment plant**, `ENVO:03600004` **drinking water treatment plant** | Same design pattern (built water facility as environmental site), different water. Good templates for the request. |
| `NCIT:C48957` **Tower** | Genus-only and the wrong genus — any tall structure. Keep as `relation: xref` at most; it should not be a grounding. |

### The missing intermediate

Both ASHRAE TC 8.6 and HSE HSG274 Part 1 treat *cooling towers* and *evaporative condensers* (plus adiabatic/evaporative fluid coolers, spray ponds) as one family of **contact-type liquid-to-air heat rejection equipment** / **evaporative cooling systems**, governed together precisely because they share the aerosol-generating open-water hazard. Requesting that parent alongside the child would let ENVO place the evaporative condenser and fluid cooler terms — which BacDive and other isolation-source vocabularies will hit next — without re-litigating the genus each time.

---

## 3. Differentia

Observable/measurable properties that separate a cooling tower from other human constructions, in decreasing order of definitional weight:

**a. Function and mechanism — evaporative heat rejection.** "Cooling towers use evaporation to cool condenser water from a chiller. Warm process water is pumped to the top where the water moves down flow plates to the cooling tower basin. As the water flows down the plates, air is pulled through the plates and heat is removed through evaporation" ([OSHA](https://www.osha.gov/legionnaires-disease/control-prevention)). DOE FEMP: "Cooling towers dissipate heat from recirculating water used to cool chillers, air conditioners, or other process equipment to the ambient air" ([DOE FEMP BMP #10](https://www.energy.gov/cmei/femp/best-management-practice-10-cooling-tower-management)). This is the single most discriminating property — it is what excludes dry coolers and radiators.

**b. Open to the atmosphere with a recirculating loop.** The water is in *direct contact* with a large volume of ambient air on every pass and is then retained rather than discharged. This is the property that makes it a habitat rather than a pipe: it supplies continuous inoculation, organic carbon and dust scavenged from the air, and oxygenation. Water leaves only by evaporation, drift, blow-down and leakage — DOE FEMP's mass balance is `Make-Up = Evaporation + Blowdown + Drift`.

**c. Water chemistry set by cycles of concentration.** Because evaporation removes pure water and leaves solutes behind, dissolved solids concentrate to a controlled multiple of the make-up water — most systems run at **2–4 cycles, with 6 or more achievable** (DOE FEMP). The consequence is elevated conductivity/TDS relative to source water, alkalinity and pH drifting upward, and continuous dosing of scale inhibitors, corrosion inhibitors and oxidising or non-oxidising biocides. This chemically distinguishes tower water from any natural freshwater of similar temperature.

**d. Temperature.** OSHA: cooling tower water is "likely to have ideal temperature ranges for *Legionella* growth: **20°–50 °C (68°–122 °F)**". Measured over a year in three Vienna towers: **10.6–32.3 °C**, seasonally modulated but with "large semi-open water volumes at a rather constant temperature" (Tsao et al. 2019). Industrial cooling water systems generally: **25–35 °C, pH close to neutrality, sunlight exposure and continuous aeration** (Di Pippo et al. 2018).

**e. Two-phase internal structure — bulk water vs. attached biofilm.** These are distinct niches with distinct communities, which matters because a habitat term will be used to annotate samples drawn from either. In a pilot tower, *Legionella* reached up to 11% relative abundance in the water phase but ≤0.5% in the biofilm, while its protozoan host cells were mainly in the biofilm (Paranjape/Séguin-type pilot-tower work, *Sci Total Environ* 2020). Anaerobic microniches under deposits support sulfate reducers — Delta-proteobacterial SRB are detected in biofilms colonising carbon-steel cooling pipework, and they drive microbially influenced corrosion by generating H₂S (Di Pippo et al. 2018). DSM 7440's anaerobic, 50 °C cultivation confirms this niche is real in the BacDive attestations themselves.

**f. Characteristic microbiota.** Not part of a genus-differentia definition proper, but the strongest external evidence that the concept is a coherent habitat:
- *Legionella* DNA in **84%** of US cooling tower samples across 7 of 8 climate regions, culturable in **47%** of PCR-positives, *L. pneumophila* sg1 in **24%** of all samples (Llewellyn et al. 2017).
- Community dominated by Proteobacteria (**79.5%**), then Bacteroidetes (8.1%), Cyanobacteria (2.2%); commonest families Comamonadaceae (22.2%) and Pseudomonadaceae (19.0%) (Llewellyn et al. 2017). Vienna towers: *Flavobacterium*, *Pseudomonas*, *Hyphomicrobium*, *Methyloversatilis*, Rhizobiales, Sphingomonadales (Tsao et al. 2019).
- An obligate protist component — ciliates (*Vorticella*, *Ancistrum*) and amoebae (*Vexillifera*, *Cochliopodium*, *Vannella*) — serving as intracellular hosts. Two of the record's own taxa (*Reyranella massiliensis*, and the *Legionella* spp. generally) are amoeba-associated and were recovered by amoebal co-culture.
- Bacterial diversity "broadly comparable to other freshwater systems but less diverse than natural environments", with strong site-specific signatures and a shared core of biofilm-forming taxa (Tsao et al. 2019).

**g. Aerosol emission.** Every open tower emits drift — "a small quantity of water may be carried from the tower as mist or small droplets", controlled by drift eliminators (DOE FEMP; OSHA). Atmospheric dispersion modelling of an industrial tower in the Pas-de-Calais outbreak showed viable dispersal **over at least 6 km** (Nguyen et al. 2006). This is the epidemiological significance rather than the definitional core, and I would keep it out of the definition sentence — it is a consequence of (b), and it also holds for evaporative condensers and misters.

---

## 4. Sources

**Definitional / standards and regulatory**

| Source | What it supports | Verification status |
|---|---|---|
| OSHA, *Legionellosis: Control and Prevention* — https://www.osha.gov/legionnaires-disease/control-prevention | Mechanism of operation; 20–50 °C range; explicit separation of cooling towers from evaporative condensers, fluid coolers, humidifiers, whirlpool spas | **Fetched and verified directly** |
| US DOE FEMP, *Best Management Practice #10: Cooling Tower Management* — https://www.energy.gov/cmei/femp/best-management-practice-10-cooling-tower-management | "Cooling towers dissipate heat from recirculating water…"; evaporation/drift/blow-down/make-up mass balance; 2–4 (up to 6+) cycles of concentration | **Fetched and verified directly** |
| HSE, *HSG274 Part 1: The control of legionella bacteria in evaporative cooling systems*, 2nd edn 2024, ISBN 978 0 7176 6753 6 — https://www.hse.gov.uk/pUbns/priced/hsg274part1.pdf | "Evaporative cooling systems" as the umbrella genus over cooling towers + evaporative condensers; regulatory grouping under the Notification of Cooling Towers and Evaporative Condensers Regulations 1992 | Located; **not fetched in full** — cited from search-result summary and title/subtitle. A curator quoting it should open the PDF. |
| ANSI/ASHRAE Standard 188 (Legionellosis: Risk Management for Building Water Systems), incl. Addendum h (2018) — https://www.ashrae.org/file%20library/technical%20resources/standards%20and%20guidelines/standards%20addenda/188_2015_h_20180628.pdf ; ASHRAE TC 8.6 scope — https://tpc.ashrae.org/?cmtKey=f712e1df-9d46-49c7-8370-09a62ffefd4d | Equipment taxonomy: open-circuit cooling towers / closed-circuit cooling towers / evaporative condensers as distinct categories; TC 8.6's "contact-type liquid-to-air heat rejection equipment" family | Addendum h §7.2.1 wording confirmed via search; **the Section 3 defined term in Standard 188 itself is paywalled and I did not read it.** Do not quote 188's definition verbatim without buying the standard. |
| 10 NYCRR Subpart 4-1 § 4-1.2(c) (NY State Sanitary Code); 24 RCNY Ch. 8 + NYC Admin. Code § 28-317 (Local Law 77 of 2015) — https://regulations.justia.com/states/new-york/title-10/chapter-i/part-4/subpart-4-1/section-4-1-2 ; https://www.nyc.gov/assets/buildings/pdf/ll77of2015.pdf | A crisp legal definition: "a cooling tower, evaporative condenser, fluid cooler or other wet cooling device capable of aerosolizing water that is part of, or contains, a recirculated water system incorporated into a building's cooling process, an industrial process, a refrigeration system, or an energy production system" | ⚠️ **Not verified against primary text — all three hosts returned HTTP 403.** The wording above is as reported by search retrieval. Useful as a model, but **do not cite it in the definition without independently opening the regulation.** |
| WHO, *Legionella and the prevention of legionellosis*, 2007, ISBN 92 4 156297 8 — https://www.who.int/publications/i/item/9241562978 | Devotes a risk-management chapter to "cooling towers and evaporative condensers" — corroborates the same grouping | Existence and chapter structure confirmed via the EID review (PMC2600316); **full text not fetched** |

**Primary literature — microbial ecology**

- **Llewellyn AC, Lucas CE, Roberts SE, et al.** Distribution of *Legionella* and bacterial community composition among regionally diverse US cooling towers. *PLoS ONE* 2017;12(12):e0189937. doi:[10.1371/journal.pone.0189937](https://doi.org/10.1371/journal.pone.0189937) · [PMC5738086](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5738086/) — **fetched and verified**
- **Tsao H-F, Scheikl U, Herbold C, Indra A, Walochnik J, Horn M.** The cooling tower water microbiota: seasonal dynamics and co-occurrence of bacterial and protist phylotypes. *Water Research* 2019;159:464–479. doi:[10.1016/j.watres.2019.04.028](https://doi.org/10.1016/j.watres.2019.04.028) · [PMC6554697](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6554697/) — **fetched and verified** (temperatures 10.6–32.3 °C; biocide 1–3 g/m³; taxa)
- **Di Pippo F, Di Gregorio L, Congestri R, Tandoi V, Rossetti S.** Biofilm growth and control in cooling water industrial systems. *FEMS Microbiology Ecology* 2018;94(5):fiy044. doi:[10.1093/femsec/fiy044](https://doi.org/10.1093/femsec/fiy044) — **fetched and verified** (25–35 °C, near-neutral pH, aeration; Proteobacteria/Cyanobacteria/Acidobacteria; SRB and MIC on carbon steel)
- **Paranjape K, Bédard É, Whyte LG, et al.** Presence of *Legionella* spp. in cooling towers: the role of microbial diversity, *Pseudomonas*, and continuous chlorine application. *Water Research* 2020;169:115252. doi:[10.1016/j.watres.2019.115252](https://doi.org/10.1016/j.watres.2019.115252) · preprint [bioRxiv 540302](https://www.biorxiv.org/content/10.1101/540302.full.pdf) — located via search; **abstract-level only**
- **Paranjape K, et al.** Impact of temperature on *Legionella pneumophila*, its protozoan host cells, and the microbial diversity of the biofilm community of a pilot cooling tower. *Science of the Total Environment* 2020;712:136131. doi:[10.1016/j.scitotenv.2019.136131](https://doi.org/10.1016/j.scitotenv.2019.136131) · preprint [bioRxiv 2019.12.12.874149](https://www.biorxiv.org/content/10.1101/2019.12.12.874149.full.pdf) — **water-vs-biofilm partitioning figures (11% vs ≤0.5%) are from the search summary of this work, not read in the paper.** Verify before quoting.
- **Nguyen TMN, Ilef D, Jarraud S, et al.** A community-wide outbreak of Legionnaires disease linked to industrial cooling towers — how far can contaminated aerosols spread? *J Infect Dis* 2006;193(1):102–111. doi:[10.1086/498575](https://doi.org/10.1086/498575) · PMID [16323138](https://pubmed.ncbi.nlm.nih.gov/16323138/) — ≥6 km dispersal

**Primary literature — the record's own characteristic taxa**

- **Qu P-H, Li Y, Salam N, et al.** *Allofrancisella inopinata* gen. nov., sp. nov. and *Allofrancisella frigidaquae* sp. nov., isolated from water-cooling systems, and transfer of *Francisella guangzhouensis* to the new genus. *Int J Syst Evol Microbiol* 2016;66:4832–4838. PMID [27543089](https://pubmed.ncbi.nlm.nih.gov/27543089/) — the entire genus is a cooling-system genus; strains from "water reservoirs of cooling systems", Guangzhou. Genomes: *Microbiol Resour Announc* 2020, doi:[10.1128/MRA.00554-20](https://journals.asm.org/doi/10.1128/mra.00554-20)
- **Pagnier I, Raoult D, La Scola B.** Isolation and characterization of *Reyranella massiliensis* gen. nov., sp. nov. from freshwater samples by using an amoeba co-culture procedure. *Int J Syst Evol Microbiol* 2011;61:2151–2154. doi:[10.1099/ijs.0.025775-0](https://doi.org/10.1099/ijs.0.025775-0) · PMID [20889765](https://pubmed.ncbi.nlm.nih.gov/20889765/) — three strains from **two cooling towers and one river**, recovered by *Acanthamoeba polyphaga* co-culture
- **DSMZ catalogue, DSM 7440** (*Desulforamulus* sp., ex-*Desulfotomaculum*) — https://www.dsmz.de/collection/catalogue/details/culture/DSM-7440 — isolation source **"cooling tower water"**, anaerobic, 50 °C. **Fetched and verified**

**Repo-internal evidence (not external citations)**

- `data/habitats/other/…` record `habitatmech:BACDIVE.71d5f01e03` — 26 strains, 23 taxa, 13 of them *Legionella*/*Fluoribacter*.
- `data/raw/isolation_source_groundings.tsv` — the upstream `NCIT:C48957` link is `skos:closeMatch`, medium confidence, justification `semapv:LexicalMatching`, curator `ols4_search_synonym`. Machine lexical output, not a curated judgement.
- `data/raw/bacdive_isolation_sources.tsv` — sibling `Air-conditioner` (16 strains, 11 taxa) with an **empty** upstream mapping.

**Explicitly my inference, not any source's claim:** the choice of `ENVO:00000070` over `ENVO:00003074`; the recommendation that HVAC-scale and power-station-scale towers be one term; the claim that the sampled material for these 26 BacDive strains spans water, biofilm and deposit (supported by DSM 7440's anaerobic 50 °C cultivation but not stated in any single source); and the judgement that aerosol emission belongs outside the definition sentence.

---

## 5. Synonyms and what NOT to conflate

**Names in real use for this concept**

- cooling tower *(preferred)*
- wet cooling tower
- open-circuit cooling tower · direct cooling tower · open recirculating cooling tower
- evaporative cooling tower
- water cooling tower
- induced-draft / forced-draft / mechanical-draft cooling tower *(fan configurations — same concept)*
- natural-draft cooling tower · hyperbolic / hyperboloid cooling tower *(power-station configuration — same concept)*
- counterflow cooling tower · crossflow cooling tower *(airflow geometry — same concept)*
- cooling tower basin · cold-water basin *(a part, frequently the actual sampled locus)*
- **French** tour aéroréfrigérante / tour de refroidissement; **German** Kühlturm / Verdunstungskühlanlage — worth carrying if the term goes to ENVO

**Commonly but wrongly treated as the same thing**

| Not a synonym | Relation |
|---|---|
| **evaporative condenser** | Sibling. Refrigerant coils in the wet air stream. Grouped with towers by HSE/ASHRAE/NY regulation for *risk management*, which is exactly why the conflation happens. |
| **closed-circuit cooling tower / evaporative fluid cooler** | Sibling. Process fluid never contacts the spray water. |
| **dry cooling tower / air-cooled condenser / dry cooler** | Not evaporative, no open water. Approaches dry-bulb, not wet-bulb. Should not inherit anything from this term. |
| **cooling water** (`ENVO:03600002`) | Material vs. site — and broader. |
| **water cooling** (`ENVO:03000146`) | Process vs. site. |
| **air conditioner / air-conditioning unit** (`ENVO:00002874`, and BacDive's own `Air-conditioner`) | Different equipment and a different sampled material (condensate pan, coil, filter, duct). A tower is often *part of* an air-conditioning installation, which is why they get merged — but many towers serve process cooling or power generation with no air conditioning involved. |
| **chiller / condenser / heat exchanger** | Components of the loop the tower serves, upstream of it. |
| **cooling pond, spray pond** | Evaporative, but water bodies rather than draught-through-fill constructions. |
| **humidifier, air washer, mister, atomizer, decorative fountain, spa pool** | Other aerosol-generating recirculating water systems. Same hazard class, different habitats. |
| **potable hot-water system / shower / plumbing** | The other major *Legionella* reservoir, and the most frequent conflation in the epidemiological literature. Entirely different water, chemistry and community. |
| **`NCIT:C48957` Tower** | Lexical accident. Any tall structure. |

---

## 6. Should it be a term at all?

**Yes.** This is a place with a boundary, contained material, a characteristic physicochemistry and a reproducible, well-described microbial community — not a process, quality, disease state, taxon or sampling artefact. It fits ENVO's existing built-environment design pattern (*plumbing fixture*, *wastewater treatment plant*, *drinking water treatment plant*, *constructed swimming pool*) exactly. It has 26 strain attestations here, an entire bacterial genus described from it (*Allofrancisella*), and a public-health literature large enough that the absence of an ENVO class is a genuine annotation gap rather than a long-tail curiosity. The curator's existing note ("A *Legionella* habitat worth an ENVO term request") is correct and this research supports it.

**Recommended disposition:** keep the minted identifier `habitatmech:BACDIVE.71d5f01e03`; keep `grounding_status: UNGROUNDED`; add `NCIT:C48957` as `relation: xref` only, never as a grounding or parent — "Tower" asserts nothing beyond tall-structure-hood and would publish an over-claim of exactly the kind #99 documented.

**Recommended ENVO new-term request (two terms, not one).** Note per the standing rule that I have **not** filed anything and am not proposing to without an explicit per-request yes:

1. **`evaporative cooling system`** *(new intermediate)* — "A human construction which rejects heat from a fluid to the atmosphere by evaporating water into an air stream in direct contact with that water." Parent: `ENVO:00000070`. This is the class HSE and ASHRAE both already use, and it gives *evaporative condenser* and *evaporative fluid cooler* a home when they surface next.
2. **`cooling tower`** — parent: the above; definition as proposed at the top, with the differentia narrowed to "…in which the water being cooled is itself the fluid distributed over the air-contact surface, and is collected in an open basin and recirculated."

Optionally a third, **`cooling tower water`**, as a child of `ENVO:03600002` *cooling water* — but only if HabitatMech later needs to distinguish the material from the site. It is not needed for this record.

**One flag outside the definition question:** this record sits in `data/habitats/other/` with `habitat_category: OTHER`. A built industrial water system looks like it belongs under `ENGINEERED` alongside the repo's other engineered habitats. That is a seeder-mapping question, not a curation decision, and I have not touched it.

---

### Sources

[FEMS Microbiol Ecol — biofilm in cooling water systems](https://academic.oup.com/femsec/article/94/5/fiy044/4935158) · [PLoS ONE — US cooling tower survey](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5738086/) · [Water Research — cooling tower water microbiota](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6554697/) · [Sci Total Environ / bioRxiv — pilot cooling tower temperature study](https://www.biorxiv.org/content/10.1101/2019.12.12.874149.full.pdf) · [Water Research / bioRxiv — Legionella, Pseudomonas, chlorination](https://www.biorxiv.org/content/10.1101/540302.full.pdf) · [J Infect Dis — 6 km aerosol dispersal](https://academic.oup.com/jid/article/193/1/102/863674) · [PubMed 16323138](https://pubmed.ncbi.nlm.nih.gov/16323138/) · [IJSEM — Allofrancisella](https://pubmed.ncbi.nlm.nih.gov/27543089/) · [LPSN — Allofrancisella](https://lpsn.dsmz.de/genus/allofrancisella) · [MRA — Allofrancisella genomes](https://journals.asm.org/doi/10.1128/mra.00554-20) · [IJSEM — Reyranella massiliensis](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.025775-0) · [PubMed 20889765](https://pubmed.ncbi.nlm.nih.gov/20889765/) · [DSMZ DSM 7440](https://www.dsmz.de/collection/catalogue/details/culture/DSM-7440) · [OSHA — Legionellosis control and prevention](https://www.osha.gov/legionnaires-disease/control-prevention) · [DOE FEMP BMP #10](https://www.energy.gov/cmei/femp/best-management-practice-10-cooling-tower-management) · [HSE HSG274 Part 1](https://www.hse.gov.uk/pUbns/priced/hsg274part1.pdf) · [ASHRAE 188 Addendum h](https://www.ashrae.org/file%20library/technical%20resources/standards%20and%20guidelines/standards%20addenda/188_2015_h_20180628.pdf) · [ASHRAE TC 8.6](https://tpc.ashrae.org/?cmtKey=f712e1df-9d46-49c7-8370-09a62ffefd4d) · [WHO — Legionella and the prevention of legionellosis](https://www.who.int/publications/i/item/9241562978) · [EID review of the WHO volume](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2600316/) · [10 NYCRR Subpart 4-1 §4-1.2](https://regulations.justia.com/states/new-york/title-10/chapter-i/part-4/subpart-4-1/section-4-1-2) · [NYC Local Law 77 of 2015](https://www.nyc.gov/assets/buildings/pdf/ll77of2015.pdf) · [NYS cooling tower registry guide](https://www.health.ny.gov/environmental/water/drinking/legionella/cooling_tower_guide.htm) · [Environment Ontology](http://environmentontology.org/) · [ENVO on GitHub](https://github.com/EnvironmentOntology/envo) · [EBI OLS4](https://www.ebi.ac.uk/ols4/)

## Citations

1. https://www.dsmz.de/collection/catalogue/details/culture/DSM-7440
2. https://www.osha.gov/legionnaires-disease/control-prevention
3. https://www.energy.gov/cmei/femp/best-management-practice-10-cooling-tower-management
4. https://www.hse.gov.uk/pUbns/priced/hsg274part1.pdf
5. https://www.ashrae.org/file%20library/technical%20resources/standards%20and%20guidelines/standards%20addenda/188_2015_h_20180628.pdf
6. https://tpc.ashrae.org/?cmtKey=f712e1df-9d46-49c7-8370-09a62ffefd4d
7. https://regulations.justia.com/states/new-york/title-10/chapter-i/part-4/subpart-4-1/section-4-1-2
8. https://www.nyc.gov/assets/buildings/pdf/ll77of2015.pdf
9. https://www.who.int/publications/i/item/9241562978
10. https://doi.org/10.1371/journal.pone.0189937
11. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5738086/
12. https://doi.org/10.1016/j.watres.2019.04.028
13. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6554697/
14. https://doi.org/10.1093/femsec/fiy044
15. https://doi.org/10.1016/j.watres.2019.115252
16. https://www.biorxiv.org/content/10.1101/540302.full.pdf
17. https://doi.org/10.1016/j.scitotenv.2019.136131
18. https://www.biorxiv.org/content/10.1101/2019.12.12.874149.full.pdf
19. https://doi.org/10.1086/498575
20. https://pubmed.ncbi.nlm.nih.gov/16323138/
21. https://pubmed.ncbi.nlm.nih.gov/27543089/
22. https://journals.asm.org/doi/10.1128/mra.00554-20
23. https://doi.org/10.1099/ijs.0.025775-0
24. https://pubmed.ncbi.nlm.nih.gov/20889765/
25. https://academic.oup.com/femsec/article/94/5/fiy044/4935158
26. https://academic.oup.com/jid/article/193/1/102/863674
27. https://lpsn.dsmz.de/genus/allofrancisella
28. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.025775-0
29. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2600316/
30. https://www.health.ny.gov/environmental/water/drinking/legionella/cooling_tower_guide.htm
31. http://environmentontology.org/
32. https://github.com/EnvironmentOntology/envo
33. https://www.ebi.ac.uk/ols4/