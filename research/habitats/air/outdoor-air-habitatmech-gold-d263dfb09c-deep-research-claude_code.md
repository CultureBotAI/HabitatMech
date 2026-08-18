---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T22:16:57.920074'
end_time: '2026-08-17T22:26:24.573991'
duration_seconds: 566.65
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Outdoor Air
  habitat_identifier: habitatmech:GOLD.d263dfb09c
  habitat_category: AIR
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Environmental > Air > Outdoor Air'
  assertions: '42'
  parent_terms: ENVO:00002005
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Nearest
    broader term ENVO:00002005 ''air'' attached as a parent. Outdoor air. The mapping
    table pointed this at ENVO:01000829, which it labels ''outdoor air'' and ENVO
    labels ''water vapour saturated air''. No outdoor-air term in the slice; parented
    to air. Term request. (source concept habitatmech:GOLD.d263dfb09c)'
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
  web_search_requests: 8
  num_turns: 40
  total_cost_usd: 3.1813759999999998
  session_id: e252dbd0-d1b2-4898-8dd3-459dbd316fe4
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 28
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Outdoor Air
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.d263dfb09c
- **Category:** AIR
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Environmental > Air > Outdoor Air
- **Upstream assertion volume:** 42
- **Nearest broader term already on the record:** ENVO:00002005
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:00002005 'air' attached as a parent. Outdoor air. The mapping table pointed this at ENVO:01000829, which it labels 'outdoor air' and ENVO labels 'water vapour saturated air'. No outdoor-air term in the slice; parented to air. Term request. (source concept habitatmech:GOLD.d263dfb09c)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Outdoor Air** as a microbial habitat, with citations.

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

# Outdoor Air — definition research for `habitatmech:GOLD.d263dfb09c`

## Proposed definition

> **Air which is not enclosed by a building envelope or other construction, and which is therefore in continuous exchange with the planetary atmosphere.**

If the curator wants a strictly single differentia, the first clause alone carries it (`located outside a building envelope`); the second clause states the consequence that makes it a distinct microbial habitat rather than an arbitrary spatial cut, and is the part the ecology literature supports. The genus `air` is `ENVO:00002005`, which the record already carries as `parent_habitats`, and the differentia term `building envelope` exists as `ENVO:01000470`.

---

## 1. What the concept denotes

**The reading the data means.** GOLD's own annotation of this exact path settles the ambiguity. The GOLD ecosystem vocabulary published at w3id.org records:

| GOLD path | `env_broad_scale` | `env_local_scale` | `env_medium` | MIxS extension |
|---|---|---|---|---|
| `Environmental > Air` | biome | — | air | MIXS:Air |
| `Environmental > Air > Indoor Air` | biome | **room** | air | MIXS:Air |
| `Environmental > Air > Outdoor Air` | biome | **atmosphere** | air | MIXS:Air |

Source: [`https://w3id.org/gold.path/3962`](https://w3id.org/gold.path/3962) and [`https://w3id.org/gold.path/3961`](https://w3id.org/gold.path/3961), as loaded in the EBI OLS `gold` vocabulary. GOLD's `Air` branch has exactly two children — `Indoor Air` and `Outdoor Air` — and it partitions them on *enclosure*: `env_local_scale` is `room` for one and `atmosphere` for the other. Both keep `env_medium: air`.

So the concept denotes **a volume of ambient atmospheric air, sampled outside of any enclosing built structure** — the thing an impinger, cyclone or high-volume filter sampler draws through when it is standing on a rooftop, in a field, on a ship deck, or at a street-level monitoring station. It is a *material* (a mass noun), not a place or a system: a sample of it is a quantity of air plus everything suspended in it.

**Boundary — what is inside:** near-surface and free-tropospheric air outside buildings; urban, rural, marine, montane, polar and desert ambient air; air sampled in open or partially-open structures with no complete envelope. Regulatory carve-outs in the air-quality standards below (workplaces, places without public access) are **not** part of the habitat concept and should not be imported.

**Boundary — what is a neighbouring concept:**
- `Indoor Air` (`habitatmech:GOLD.40979f5751`, 72 GOLD organism assertions) — the direct sibling, and the complement.
- `Dust`, `Air scrubber`, `Air scrubber > Biofilm` — GOLD places all three under *Indoor* Air, not under Air generally ([gold.path/4620](https://w3id.org/gold.path/4620), [gold.path/5806](https://w3id.org/gold.path/5806)). They are not children of this concept.
- Cloud water, precipitation, snow — liquid environmental materials formed in the atmosphere, not air.
- The particulate phase alone (bioaerosol, `atmospheric aerosol` ENVO:01001652) — a *part* of outdoor air, not the same entity.

**Residual ambiguity worth recording, not resolving here:** the label does not fix an *altitude ceiling*. GOLD's `env_local_scale: atmosphere` reads as unbounded, and the atmospheric microbiology literature treats the atmospheric boundary layer, the free troposphere and the lower stratosphere as ecologically distinct strata ([Šantl-Temkiv et al. 2022](https://doi.org/10.1093/femsre/fuac009)). In practice essentially every GOLD attestation under this node will be near-surface. My recommendation is to leave the ceiling unstated in the definition — the differentia is enclosure, not altitude — and note that if altitude-stratified air terms are ever needed they are additional siblings, not readings of this one. *(This paragraph is my inference from the GOLD annotation plus the review, not a claim either source makes.)*

---

## 2. Genus — the broader kind

**Genus: `air` (`ENVO:00002005`)** — "The mixture of gases (roughly (by molar content/volume: 78% nitrogen, 20.95% oxygen, 0.93% argon, 0.038% carbon dioxide, trace amounts of other gases, and a variable amount (average around 1%) of water vapor) that surrounds the planet Earth." Its own parent is `gaseous environmental material` (`ENVO:01000797`). Verified via OLS4 on 2026-08-17: <https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002005>.

This is the right genus and it is already on the record. `air` has exactly three asserted children in ENVO — `contaminated air` (ENVO:01000676), `humid air` (ENVO:01000828), `water vapour saturated air` (ENVO:01000829) — none of which is location-differentiated, so there is a clean, empty slot for an enclosure-based subdivision.

### Confirmation that no term exists — and that ENVO already knows it

This is not a case where the term might be hiding under an unexpected label. **ENVO has three open issues requesting exactly this term**, one of which proposes the same differentia this report recommends:

- [**ENVO #1179, "NTRs: Indoor and outdoor air"** (opened 2021-06-15, still open)](https://github.com/EnvironmentOntology/envo/issues/1179) — "I propose an alternate way to subdivide air. We currently have: […] I can add two classes, indoor and outdoor air, using **contained-in some building as differentia**."
- [**ENVO #980, "Request for new ENVO term labels"** (2020-06-23, open)](https://github.com/EnvironmentOntology/envo/issues/980) — requests, among others, "**Outdoor air / ambient air**" and "Indoor air" as ENVO material term labels, plus an "Air biome".
- [**ENVO #858, "GOLD/EBI Air terms"** (2019-08-16, open)](https://github.com/EnvironmentOntology/envo/issues/858) — a request to create terms for precisely the four GOLD paths `Environmental > Air`, `… > Indoor Air`, `… > Indoor Air > Dust`, `… > Outdoor Air`. The thread contains a worked modelling proposal in which *indoor* air is `air-associated ecosystem and 'located in' some 'building envelope'` — making outdoor air its complement. The thread stalled on a pre- vs post-composition question, not on whether the concept is real.

An OLS4 search across all loaded ontologies for `"outdoor air"` returns no material or environment class in ENVO, UBERON, FOODON, BTO or PO. The only near-label hits are `FOODON:03530209` *conventional outdoor/open-air cultivation* (a cultivation practice), `LFID:0001141` *exposure to outdoor air pollution* (an exposure), and `OMIT:0001823` *Air Pollution* (a chemical driver) — none of which is air.

### Near-misses, and why each fails

| Term | Why it is not a match |
|---|---|
| `ENVO:01000829` **water vapour saturated air** | The target kg-microbe's mapping table pointed at. ENVO defines it as "Air which has a partial pressure of water vapour equal or near equal to its equilibrium vapor pressure at a given temperature", synonyms "wet air", "water-vapour-saturated air". A completely different concept; the curator's existing note is correct. |
| `ENVO:03501101` **outdoor environment** | "An environmental system which is not sheltered." Captures the *outdoor-ness* exactly, but it is an `environmental system` (subclass of ENVO:01000254), not an environmental material, and it is not air-specific — an unsheltered soil plot or pond satisfies it equally. It is broader on the material axis and wrong on the category axis. **Best available xref**, not a grounding target. |
| `ENVO:01000267` **atmosphere** / `ENVO:01000543` **atmospheric layer** | An atmosphere is "a layer of gases surrounding a material body … held in place by the gravity of the body" — a planetary-scale part, not a sampled material, and it does not exclude the air inside a building. Asserts astronomical-body-part structure the sources never claim. |
| `ENVO:01000323` **atmospheric boundary layer**, `ENVO:01001712` **free atmosphere**, `ENVO:01001711` **upper air**, `ENVO:03520000-2` **low/middle/high atmospheric level** | All altitude-stratified atmospheric layers. Each is *narrower* than outdoor air on the wrong axis (altitude, not enclosure), and none excludes indoor air by definition. Useful for future stratified terms; not this one. |
| `ENVO:01001652` **atmospheric aerosol**, `ENVO:00010505` **aerosol**, `ENVO:01001052` **aerosol environment** | The suspended particulate/droplet phase and the system it determines — a *part* of outdoor air. Grounding here would silently narrow the concept to the particles and lose the gas phase that the `env_medium: air` annotation asserts. |
| `ENVO:01000676` **contaminated air** | A sibling under `air`. Asserts pollutant loading; GOLD's `Outdoor Air` makes no such claim. |
| `ENVO:01000470` **building envelope** | Not a habitat — it is the differentia term the definition should reference. |

**Alternative genus considered and rejected:** ENVO #858 proposed an *ecosystem*-typed genus (`air-associated ecosystem`, `construction-enclosed air-associated ecosystem`). That class was never created, and HabitatMech's record already sits under the material `air`. Following the material line keeps this record consistent with `data/habitats/air/air.yaml` and with GOLD's own `env_medium: air`.

---

## 3. Differentia — what distinguishes it

### 3a. The primary, definitional differentia: absence of a built enclosure

This is the criterion the whole air branch is partitioned on, and four independent authorities converge on it:

- **US EPA, 40 CFR §50.1(e)**: "*ambient air* means that portion of the atmosphere, **external to buildings**, to which the general public has access." (<https://www.law.cornell.edu/cfr/text/40/50.1>)
- **EU Ambient Air Quality Directive 2008/50/EC of 21 May 2008, Art. 2(1)**: "'ambient air' shall mean **outdoor air in the troposphere**, excluding workplaces as defined by Directive 89/654/EEC where provisions concerning health and safety at work apply and to which members of the public do not have regular access." (<https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32008L0050>)
- **ENVO #1179** proposes "contained-in some building as differentia" for the indoor/outdoor split.
- **GOLD** itself: `env_local_scale = room` for Indoor Air vs `atmosphere` for Outdoor Air.

Two caveats a curator should carry over:
1. The EPA and EU clauses append a *public-access / non-workplace* qualifier. That is regulatory scoping for enforcement, not part of the natural kind. Air over a fenced industrial yard is outdoor air as a habitat. Do not import it.
2. **ISO 4225:2020** *Air quality — General aspects — Vocabulary* (Edition 3, 2020-05, reconfirmed 2025) is the standards-body vocabulary that formally distinguishes *ambient air*, *indoor air* and *workplace air* (<https://www.iso.org/standard/72525.html>). I could not retrieve its clause text — the standard is paywalled and the ISO OBP is behind a bot challenge — so I am citing it as evidence that the tripartite distinction is standardised, **not** quoting a definition from it.

### 3b. Observable ecological differentia (what makes the split microbiologically real)

- **Community source composition.** In a global survey of 370 air particulate samples from 63 sites, surface microbiomes contribute on average **46.3%** of the airborne bacterial community, with the remainder shaped by meteorology and air quality; in urban areas human impact "weaken[s] the relative importance of plant sources … and elevate[s] the occurrence of potential pathogens from anthropogenic sources." (Zhao J, Jin L, Wu D, et al. *Global airborne bacterial community—interactions with Earth's microbiomes and anthropogenic activities.* **PNAS** 2022;119(42):e2204465119. [doi:10.1073/pnas.2204465119](https://doi.org/10.1073/pnas.2204465119), PMID 36215495, published 2022-10-18.)
- **Dominant emission sources are outdoor-only.** Terrestrial emissions "predominantly from crops, grasslands and shrubs", marine emission via bubble bursting at breaking waves, and phyllosphere-derived diversity — plus anthropogenic biomass burning, fossil-fuel combustion and land-use soil destabilisation. (Šantl-Temkiv T, Amato P, Casamayor EO, Lee PKH, Pointing SB. *Microbial ecology of the atmosphere.* **FEMS Microbiology Reviews** 2022;46(4):fuac009. [doi:10.1093/femsre/fuac009](https://doi.org/10.1093/femsre/fuac009), PMID 35137064.)
- **Contrast with the sibling is measured, not assumed.** Human-associated bacterial genera are **more than twice as abundant** in indoor air as in outdoor air, and indoor communities track outdoor communities with a ventilation-dependent time lag. (Meadow JF, Altrichter AE, Kembel SW, et al. *Indoor airborne bacterial communities are influenced by ventilation, occupancy, and outdoor air source.* **Indoor Air** 2014;24(1):41–48. [doi:10.1111/ina.12047](https://doi.org/10.1111/ina.12047), PMID 23621155, [PMC4285785](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4285785/).) Indoor airborne fungi are dominated by outdoor air (Adams RI, Miletto M, Taylor JW, Bruns TD. *Dispersal in microbes: fungi in indoor air are dominated by outdoor air and show dispersal limitation at short distances.* **ISME J** 2013;7(7):1262–1273. [doi:10.1038/ismej.2013.28](https://doi.org/10.1038/ismej.2013.28).) **Outdoor air is the source pool for indoor air** — the asymmetry is itself a differentia.
- **Characteristic physicochemistry: extreme oligotrophy and low biomass.** Modelled global concentrations of 10²–10⁵ bacteria and fungi per m³; cloud-water-derived estimates of 4×10²–4×10³ bacterial cells m⁻³ and 4×10⁰–4×10² eukaryotic cells m⁻³; aerosolised desert dust up to 10⁷ cells m⁻³. Total global tropospheric airborne bacterial abundance is 1.72×10²⁴ cells — 1 to 3 orders of magnitude below other habitats — while taxon richness (4.71×10⁸–3.08×10⁹) is comparable to the hydrosphere. (Šantl-Temkiv 2022; Zhao 2022, both above.)
- **Transport-medium character.** Modelled airborne residence times of ~3–8 days depending on particle characteristics; "most cells in the atmosphere are metabolically inactive during transport", with active heterotrophic metabolism apparent under favourable cloud conditions (putative generation times 3.6–19.5 days). (Šantl-Temkiv 2022.)
- **Community composition is dominated by bacteria and fungi**, archaea and protists minor; pronounced seasonal structure near the ground and above the boundary layer, and diel variation in the equatorial tropics. (Šantl-Temkiv 2022; see also the dedicated review: Ruiz-Gil T, Acuña JJ, Fujiyoshi S, Tanaka D, Noda J, Maruyama F, et al. *Airborne bacterial communities of outdoor environments and their associated influencing factors.* **Environment International** 2020;145:106156. [doi:10.1016/j.envint.2020.106156](https://doi.org/10.1016/j.envint.2020.106156), PMID 33039877.)

**Sampling-side differentia (relevant to what a record means operationally):** GOLD assigns this node the **MIxS Air extension, `MIXS:0016000`** — "A collection of terms appropriate when collecting and sequencing samples obtained from a gaseous environment" (<https://genomicsstandardsconsortium.github.io/mixs/>). MIxS `env_medium` (`MIXS:0000014`) for such samples is `air [ENVO:00002005]`; the filter or impinger fluid is *not* the `env_medium`.

---

## 4. Sources

Every substantive claim above is cited inline. Consolidated, with what each supports:

| Claim | Source |
|---|---|
| GOLD's own env-triad for this path and its sibling | [w3id.org/gold.path/3962](https://w3id.org/gold.path/3962), [/3961](https://w3id.org/gold.path/3961), [/4620](https://w3id.org/gold.path/4620), [/5806](https://w3id.org/gold.path/5806) (via OLS4 `gold`) |
| ENVO `air`, its children and parent; absence of an outdoor-air term | OLS4, queried 2026-08-17: <https://www.ebi.ac.uk/ols4/ontologies/envo> |
| ENVO knows the gap and proposes the enclosure differentia | ENVO issues [#1179](https://github.com/EnvironmentOntology/envo/issues/1179), [#980](https://github.com/EnvironmentOntology/envo/issues/980), [#858](https://github.com/EnvironmentOntology/envo/issues/858) |
| "external to buildings" | 40 CFR §50.1(e), <https://www.law.cornell.edu/cfr/text/40/50.1> |
| "outdoor air in the troposphere" | Directive 2008/50/EC, 21 May 2008, Art. 2(1) |
| Standardised ambient/indoor/workplace air vocabulary *(cited for existence only — text not retrieved)* | ISO 4225:2020, <https://www.iso.org/standard/72525.html> |
| ASHRAE's conflicting HVAC sense of "outdoor air" | ANSI/ASHRAE Standard 62.1-2022, terminology section |
| Abundance, residence time, activity, sources, stratification | Šantl-Temkiv et al. 2022, FEMS Microbiol Rev 46(4):fuac009 |
| Global biogeography, source apportionment, total abundance/richness | Zhao et al. 2022, PNAS 119(42):e2204465119 |
| Indoor/outdoor asymmetry | Meadow et al. 2014, Indoor Air 24(1):41–48; Adams et al. 2013, ISME J 7(7):1262–1273 |
| Dedicated review of outdoor airborne bacterial communities | Ruiz-Gil et al. 2020, Environ Int 145:106156 |
| MIxS Air extension identifier and description | <https://genomicsstandardsconsortium.github.io/mixs/> |
| Public-health weight of the ambient-air concept | WHO fact sheet, *Ambient (outdoor) air quality and health*, updated 24 Oct 2024 — 4.2 M premature deaths (2019); 99% of the global population in areas exceeding WHO guidelines |

**Explicitly flagged as my inference, not sourced:** (a) that the definition should leave the altitude ceiling unstated; (b) that the regulatory public-access/workplace carve-outs are not part of the habitat concept; (c) that `ENVO:03501101` is the best available `xref` target. Each is a curatorial judgement, defensible from the cited material but not asserted by any source.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- **ambient air** — the dominant term of art in air-quality science, regulation and standards (EPA, EU, ISO, WHO). ENVO #980 requested the pair as one label: "Outdoor air / ambient air".
- outdoor air *(GOLD, ASHRAE, indoor-air-quality literature)*
- open air, outside air, external air, outdoor ambient air
- atmospheric air *(common in aerosol/atmospheric chemistry; slightly broader in practice)*

**Commonly but wrongly treated as the same thing**
1. **`atmosphere` (ENVO:01000267)** — the whole gravitationally bound gas envelope, including air inside buildings and air far above the sampled layer. Broader and category-shifted.
2. **`outdoor environment` (ENVO:03501101)** — an unsheltered environmental *system*; includes outdoor soil, water and surfaces. Broader on material.
3. **Bioaerosol / `atmospheric aerosol` (ENVO:01001652) / airborne particulate matter** — the suspended phase only. A part-of relation, not identity. PM₂.₅/PM₁₀ are size-fractionated measurements, not the habitat.
4. **Ambient air *pollution*** — an exposure or quality (`OMIT:0001823` *Air Pollution*, `LFID:0001141` *exposure to outdoor air pollution*, MeSH D000393). `ENVO:01000676` *contaminated air* is a sibling under `air`, not a synonym.
5. **ASHRAE's "outdoor air"** — a genuine and dangerous homonym. ANSI/ASHRAE 62.1-2022 defines *outdoor air* as "ambient air **and** ambient air that enters a building through a ventilation system, through intentional openings for natural ventilation, or by infiltration." That is an HVAC *airstream*, partly indoors. HabitatMech's concept is the ambient reservoir only. This matters here because GOLD's `Air scrubber` node sits under *Indoor* Air.
6. **Cloud water, fog, rain, snow** — liquid or solid environmental materials formed in outdoor air; distinct habitats with distinct ENVO terms.
7. **`Dust`** — GOLD scopes its `Dust` node to *Indoor* Air (`env_medium: dust`), and dust is a solid material regardless.
8. **Urban air / rural air / marine air / desert dust plume** — potential *children*, not synonyms.
9. **Air biome** — ENVO #980 requested this separately; a biome is a different ENVO category from an environmental material. Do not collapse the two.

---

## 6. Should it be a term at all?

**Yes.** It is a habitat, not a process, quality, disease state, taxon or sampling artefact. Specifically:

- It is a **material** (a mass noun, `env_medium: air`), which is the category ENVO's `environmental material` branch requires, and it sits cleanly under an existing genus with an empty enclosure-differentiated slot.
- The distinction is **not a HabitatMech invention**: it is the primary partition of GOLD's entire `Air` branch, it is the tripartite split ISO 4225 standardises, and it is the boundary EPA and the EU write into law.
- **ENVO has three open, unresolved requests for it** (#858 2019, #980 2020, #1179 2021), one of which proposes the same differentia. This is as strong a signal as this corpus gets that a term request is warranted rather than a grounding failure.
- The distinction is **empirically load-bearing** for microbial ecology, not just administrative: indoor and outdoor air differ measurably in community composition, and the direction of influence runs outdoor→indoor (Meadow 2014; Adams 2013).

**Two honest caveats to record on the term request:**

1. **Pre- vs post-composition.** ENVO #858 stalled on precisely this: whether to mint `outdoor air` as a named class or to post-compose it as `air` + an outdoor location at annotation time. HabitatMech mints an identifier because a single-IRI annotation is what GOLD supplies, and the sibling `Indoor Air` is minted on the same grounds — but the ENVO submission should acknowledge the alternative rather than pretend it does not exist. **Request the indoor/outdoor pair together**, as #1179 frames them; requesting one alone is the weaker ask.
2. **Habitat vs conduit.** Šantl-Temkiv et al. 2022 conclude that "most cells in the atmosphere are metabolically inactive during transport", which invites the objection that outdoor air is a dispersal medium rather than a habitat. This does **not** defeat the term. HabitatMech's `AIR` category and GOLD's `env_medium: air` record where a sample was taken, and outdoor air satisfies that unambiguously; the same review documents active heterotrophic metabolism under favourable cloud conditions and estimated in-air generation times of 3.6–19.5 days. If the definition is to stay one sentence, do not attempt to adjudicate this in it — the enclosure differentia is the defensible one, and "is a habitat where cells actively grow" is not a claim the sources uniformly support.

**Volume note for triage:** 42 GOLD organism assertions across 3 GOLD ecosystem node ids (`gold.ecosystem:3478|3747|3962`), versus 72 for the `Indoor Air` sibling and 397 + 2,424 PREGO taxa for the parent `air`. Modest, but the concept's justification rests on the source vocabularies' structure and the standards, not on assertion count.

---

**Sources:**
[GOLD path 3962 (OLS4)](https://w3id.org/gold.path/3962) · [GOLD path 3961](https://w3id.org/gold.path/3961) · [EBI OLS4 — ENVO](https://www.ebi.ac.uk/ols4/ontologies/envo) · [ENVO issue #1179](https://github.com/EnvironmentOntology/envo/issues/1179) · [ENVO issue #980](https://github.com/EnvironmentOntology/envo/issues/980) · [ENVO issue #858](https://github.com/EnvironmentOntology/envo/issues/858) · [40 CFR §50.1](https://www.law.cornell.edu/cfr/text/40/50.1) · [Directive 2008/50/EC](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32008L0050) · [ISO 4225:2020](https://www.iso.org/standard/72525.html) · [ANSI/ASHRAE 62.1-2022](https://static1.squarespace.com/static/6320b844c3820725e4d5688f/t/6372af076022e56f815dc7f5/1668460297956/ASHRAE+62.1-2022+(1).pdf) · [Šantl-Temkiv et al. 2022, FEMS Microbiol Rev](https://academic.oup.com/femsre/article/46/4/fuac009/6524182) · [Zhao et al. 2022, PNAS](https://www.pnas.org/doi/10.1073/pnas.2204465119) · [Meadow et al. 2014, Indoor Air](https://onlinelibrary.wiley.com/doi/full/10.1111/ina.12047) · [Adams et al. 2013, ISME J](https://academic.oup.com/ismej/article/7/7/1262/7590166) · [Ruiz-Gil et al. 2020, Environ Int](https://www.sciencedirect.com/science/article/pii/S0160412020321115) · [GSC MIxS extensions](https://genomicsstandardsconsortium.github.io/mixs/) · [WHO ambient (outdoor) air quality and health, 24 Oct 2024](https://www.who.int/news-room/fact-sheets/detail/ambient-(outdoor)-air-quality-and-health)

## Citations

1. https://w3id.org/gold.path/3962`
2. https://w3id.org/gold.path/3962
3. https://w3id.org/gold.path/3961`
4. https://w3id.org/gold.path/3961
5. https://w3id.org/gold.path/4620
6. https://w3id.org/gold.path/5806
7. https://doi.org/10.1093/femsre/fuac009
8. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002005
9. https://github.com/EnvironmentOntology/envo/issues/1179
10. https://github.com/EnvironmentOntology/envo/issues/980
11. https://github.com/EnvironmentOntology/envo/issues/858
12. https://www.law.cornell.edu/cfr/text/40/50.1
13. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32008L0050
14. https://www.iso.org/standard/72525.html
15. https://doi.org/10.1073/pnas.2204465119
16. https://doi.org/10.1111/ina.12047
17. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4285785/
18. https://doi.org/10.1038/ismej.2013.28
19. https://doi.org/10.1016/j.envint.2020.106156
20. https://genomicsstandardsconsortium.github.io/mixs/
21. https://www.ebi.ac.uk/ols4/ontologies/envo
22. https://static1.squarespace.com/static/6320b844c3820725e4d5688f/t/6372af076022e56f815dc7f5/1668460297956/ASHRAE+62.1-2022+(1
23. https://academic.oup.com/femsre/article/46/4/fuac009/6524182
24. https://www.pnas.org/doi/10.1073/pnas.2204465119
25. https://onlinelibrary.wiley.com/doi/full/10.1111/ina.12047
26. https://academic.oup.com/ismej/article/7/7/1262/7590166
27. https://www.sciencedirect.com/science/article/pii/S0160412020321115
28. https://www.who.int/news-room/fact-sheets/detail/ambient-(outdoor