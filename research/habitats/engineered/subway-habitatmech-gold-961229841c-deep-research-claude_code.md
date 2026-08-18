---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T02:59:13.097663'
end_time: '2026-08-18T03:08:22.468071'
duration_seconds: 549.37
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Subway
  habitat_identifier: habitatmech:GOLD.961229841c
  habitat_category: ENGINEERED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Engineered > Built environment > City > Subway'
  assertions: '0'
  parent_terms: ENVO:00000856
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Narrowed-grounding
    review (#67): was ENVO:03501109 ''subway train''. GOLD''s path is Engineered >
    Built environment > City > Subway, which is the system or the station rather than
    the rolling stock; the slice has train terms but nothing for the subway environment
    itself. (source concept habitatmech:GOLD.961229841c)'
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
  web_search_requests: 13
  num_turns: 44
  total_cost_usd: 3.136275999999999
  session_id: fb5140c9-5c0f-4b4a-bd10-84e1ea93074a
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 27
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Subway
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.961229841c
- **Category:** ENGINEERED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Engineered > Built environment > City > Subway
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** ENVO:00000856
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Narrowed-grounding review (#67): was ENVO:03501109 'subway train'. GOLD's path is Engineered > Built environment > City > Subway, which is the system or the station rather than the rolling stock; the slice has train terms but nothing for the subway environment itself. (source concept habitatmech:GOLD.961229841c)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Subway** as a microbial habitat, with citations.

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

# Definition research: **Subway** — `habitatmech:GOLD.961229841c` (ENGINEERED, UNGROUNDED)

## Proposed definition

> An anthropogenic environment which is bounded by the underground stations, tunnels and trains of an urban rapid transit system, whose surfaces and enclosed air receive continuous microbial input from large numbers of human passengers and from ventilated outdoor air, and whose particulate matter is dominated by iron-rich wear debris from wheel–rail–brake abrasion.

That is one sentence but it is a long one. If the curator wants it shorter, the honest reason is that **an intermediate class is missing**: ENVO has no "public transport environment" / "transit-associated environment" class between `anthropogenic environment` and this concept, and no `subway station` or `railway station` term at all (§2). With such a parent in place the sentence collapses to:

> A public transport environment which is bounded by the underground stations, tunnels and trains of an urban rapid transit system.

An alternative, artifact-flavoured reading is given in §2.3 — it grounds differently and a curator should choose deliberately, not by accident.

---

## 1. What the concept denotes

**The reading the data means.** The GOLD path is `Engineered > Built environment > City > Subway`. In GOLD's five-level schema (`Ecosystem → Ecosystem Category → Ecosystem Type → Ecosystem Subtype → Specific Ecosystem`), `City` is the subtype and `Subway` the *specific ecosystem* — i.e. a specific built feature **within a city**, sampled as built environment ([JGI GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification); schema origin: Ivanova et al., "A call for standardized classification of metagenome projects," described on the same page). This supports the curator's existing note: the concept is the *place* — the system and its stations — not the rolling stock alone.

**What a sample is actually taken from.** Across the primary literature, "subway" samples are one of two material classes, both inside the same physical envelope:

- **Touch surfaces** in stations and inside trains: railings/handrails, benches and seats, ticket kiosks, turnstiles, poles, platform floors, escalator handrails. The MetaSUB standard operating procedure directs teams to "at least three common surfaces in each mass transit system (railings, benches, and ticket kiosks), with additional optional surfaces" ([Danko et al. 2021, *Cell* 184:3376–3393, 24 Jun 2021, doi:10.1016/j.cell.2021.05.002](https://www.cell.com/cell/fulltext/S0092-8674(21)00585-7)). Mexico City sampled 47 sites across stations *and* trains on all 12 lines ([Hernández et al. 2020, *Sci Rep* 10:8798, 29 May 2020, doi:10.1038/s41598-020-65643-4](https://www.nature.com/articles/s41598-020-65643-4)); the companion study resolves surfaces individually — platform floor most diverse, stair handrail and pole least ([Vargas-Robles et al. 2020, *PLoS ONE* 15:e0237272, PMID 32813719, doi:10.1371/journal.pone.0237272](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0237272)). Boston profiled multiple surface types across lines and stations ([Hsu et al. 2016, *mSystems* 1:e00018-16, doi:10.1128/mSystems.00018-16](https://journals.asm.org/doi/10.1128/msystems.00018-16), PMC5069760).
- **Enclosed air / bioaerosol and settled PM** on platforms, in concourses and inside train cars ([Robertson et al. 2013, *Appl Environ Microbiol* 79:3485–3493, doi:10.1128/AEM.00331-13](https://pmc.ncbi.nlm.nih.gov/articles/PMC3648054/); [Triadó-Margarit et al. 2017, *Indoor Air* 27:564–575, doi:10.1111/ina.12343](https://onlinelibrary.wiley.com/doi/10.1111/ina.12343); [Grydaki et al. 2021, *Environ Int* 146:106186, doi:10.1016/j.envint.2020.106186, PMID 33126062](https://www.sciencedirect.com/science/article/pii/S0160412020321413)).

**Boundary — inside the concept:** station structures and their interior air (platforms, concourses, ticket halls, turnstiles, escalators), running tunnels, and the interior surfaces and air of the trains while in that system.

**Boundary — neighbouring concepts, outside:** the *train as an object* (that is `ENVO:03501109 subway train`); surface tram, light-rail, bus and commuter-rail environments (MetaSUB explicitly substituted "the most common form of public transit" where a city had no subway — so MetaSUB's corpus is a **superset** of this concept, Danko et al. 2021); road and utility tunnels; a British pedestrian underpass (§5); the general indoor built environment of buildings.

**Ambiguity — three readings, stated rather than silently resolved:**

1. **The system/environment** (US/Canadian English): an underground urban rapid transit system and the environment it encloses. *This is the reading the GOLD path supports* and the one all the microbiome literature uses.
2. **The rolling stock only:** already covered by `ENVO:03501109`; the previous narrowed grounding, and the reason #67 removed it.
3. **British English "subway" = a pedestrian underpass**, a footway beneath a road or railway ([Wikipedia, *Rapid transit*, terminology section](https://en.wikipedia.org/wiki/Rapid_transit)). No evidence in the GOLD path or any cited study supports this reading; it matters only as a conflation risk (§5).

---

## 2. Genus — the broader kind

### 2.1 Recommended genus: `ENVO:01000313` *anthropogenic environment*

"An environmental system which is the product of human activity." ENVO already uses this class as the genus for exactly this shape of concept — a human-made setting that people occupy and that gets sampled:

| CURIE | Label | ENVO definition |
|---|---|---|
| `ENVO:01000313` | anthropogenic environment | "An environmental system which is the product of human activity." |
| `ENVO:03501339` | household environment | "An anthropogenic environment which is bounded by a human dwelling." |
| `ENVO:03501331` | healthcare environment | bounded by a healthcare facility providing specialized services |
| `ENVO:03501323` | residential environment | "An anthropogenic environment which provides long-term shelter for its inhabitants." |
| `ENVO:03501332` | occupational environment | "An anthropogenic environment which is the product of a particular human occupational activity." |

(All retrieved from [OLS4/ENVO](https://www.ebi.ac.uk/ols4/ontologies/envo), August 2026.) The `<X> environment` … *"which is bounded by <artifact>"* pattern is the idiomatic ENVO construction and is what the proposed definition above follows. **This is my recommendation** because it makes the concept an environment (a place microbes live), not a piece of infrastructure.

### 2.2 The closest existing term — a real near-miss the curator must see: `ENVO:03501116` *rapid transit system*

ENVO **does** have a metro term, and the note on this record ("the slice has train terms but nothing for the subway environment itself") is right only if this term is absent from the vendored slice or is judged not to be an environment. Its record:

- **`ENVO:03501116` rapid transit system** — definition: *"A public transit system which is owned by a government or other form of public representation."* Synonyms: **MRT, Heavy rail, Light rail, Mass rapid transit, Medium-capacity rail, Metro**. Created 2021-03-15; xref: Wikipedia.

Why it is a near-miss rather than a match:

- **Its definition is defective.** It is a verbatim copy of its parent `ENVO:03501111 public transit system` ("A constructed transport system which is owned by a government or other form of public representation") — it carries *no differentia at all* for rapid transit. Grounding to it therefore grounds to a class whose asserted content is "publicly owned transit system", nothing more.
- **It over-claims ownership.** The asserted differentia that survives is public ownership. GOLD's `Subway` claims nothing about ownership, and the claim is not universally true (e.g. Hong Kong's MTR Corporation is a publicly listed company). *This is the same failure mode as the `anthropogenic contamination feature` case recorded in CLAUDE.md/#99.*
- **Its synonym set conflates modes.** It lists both "Heavy rail"/"Metro" and "Light rail", which the transit literature treats as distinct: light rail often shares street right-of-way, metro is fully grade-separated ([Britannica, *Rapid transit*](https://www.britannica.com/technology/rapid-transit); [ITDP Rapid Transit Database](https://itdp.org/rapid-transit-database/)).
- **It is a system, not a place.** A "constructed transport system" is infrastructure; a habitat record is about the environment sampled. An is-a from "subway environment" to "rapid transit system" is a category error, though an is-a from "subway *system*" to it would be correct.

**Disposition I would suggest:** keep the record UNGROUNDED with `ENVO:03501116` recorded as `relation: xref` (upstream saw the same concept; this repo does not assert identity), exactly as the `parent_habitats` rule in CLAUDE.md prescribes for related-but-not-broader terms. If the curator instead adopts the artifact reading (§2.3), `ENVO:03501116` becomes a defensible `GROUND_AS_PARENT` target — but the ownership over-claim should be flagged to ENVO as a term-definition bug either way.

### 2.3 Alternative reading (artifact), if the curator prefers it

> A rapid transit system which runs predominantly in tunnels beneath an urban area.

Genus `ENVO:03501116`; differentia = predominant underground/tunnel alignment. This matches the transit-industry definition of the subway/underground/tube subtype: "a system that primarily runs below the surface may be called a subway, tube, or underground," within rapid transit defined by exclusive, grade-separated right-of-way, electric traction, high platforms and high frequency ([Britannica](https://www.britannica.com/technology/rapid-transit); [UITP's definition of metros as urban guided transport "operated on their own right of way and segregated from general road and pedestrian traffic"](https://www.gtkp.com/wp-content/uploads/from-gtkp/documents/17/20100214-204543-5022-UMTIS%20MRT.pdf); [Wikipedia, *Rapid transit*](https://en.wikipedia.org/wiki/Rapid_transit)). **Cost of this reading:** it defines the infrastructure, so it says nothing about the habitat, and it makes the many partially-above-ground systems (≈40% of the NYC subway runs above ground, per the same source) awkward members.

### 2.4 Other ENVO near-misses checked and rejected

| CURIE | Label | Why it fails |
|---|---|---|
| `ENVO:03501109` | subway train | **Narrower** — the rolling stock only; excludes stations, tunnels, platform air. This is the grounding #67 removed. |
| `ENVO:03501115` | public subway train | Narrower still; adds an ownership claim. |
| `ENVO:03501111` | public transit system | Broader *and* asserts public ownership; covers buses, ferries, trams. |
| `ENVO:03501110` | constructed transport system | Broader; covers roads, airports, canals. |
| `ENVO:03501351` | ground transport | Broader; any land transport system. |
| `ENVO:03501117` / `ENVO:03501118` | transport hub / public transport hub | "A place where passengers and cargo are exchanged between vehicles or/and between transport modes" — covers a *station* reading but not tunnels or trains, and covers airports and bus terminals; also asserts intermodal exchange that a plain station need not have. |
| `ENVO:00000010` | transport feature | Far too broad ("a construction which enables the movement of humans, their animals or their vehicles"). |
| `ENVO:00000065` | railway | "A permanent way having one or more rails which provides a track for cars" — the track, not the environment; covers freight and mainline rail. |
| `ENVO:00000068` / `ENVO:00000066` | tunnel / man-made tunnel | Covers the running tunnels only, not stations or trains; covers road, canal and utility tunnels. |
| `ENVO:00000856` | city | The current nearest-broader on this record; correct as a broader term but far too coarse to define from. |
| `ENVO:01000249` | urban biome | Broader; the whole urbanized biome. |

**ENVO gaps confirmed by search (OLS4, August 2026):** no `subway station`, no `railway station`, no `metro station`, no `station platform`, no `public transport environment`, no `built environment` class as such. Searches for `station`, `railway`, `underground`, `tunnel`, `transit`, `transportation` and `built environment` in ENVO returned nothing covering these. *That absence is the substantive finding of §2.*

---

## 3. Differentia — what distinguishes it from siblings

Ordered most- to least-diagnostic. Each is observable or measurable.

**3.1 Enclosed, largely subterranean, mechanically ventilated envelope.** Rapid transit is defined by exclusive, grade-separated right-of-way, typically in tunnels or elevated; the "subway" subtype is the predominantly-below-surface case ([Britannica](https://www.britannica.com/technology/rapid-transit); [UITP](https://www.gtkp.com/wp-content/uploads/from-gtkp/documents/17/20100214-204543-5022-UMTIS%20MRT.pdf)). One study's authors describe it as "an almost enclosed, human-made biome built of steel and concrete" ([Liang et al. 2025, *Microbiology Spectrum*, doi:10.1128/spectrum.01626-25, 25 Sep 2025](https://journals.asm.org/doi/10.1128/spectrum.01626-25); quoted in the [ASM press release](https://asm.org/press-releases/2025/september/new-study-reveals-subway-station-fungal-communitie)).

**3.2 Extreme, sustained human throughput with high-touch surfaces.** Boston's MBTA carries ~238 million trips/year (Hsu et al. 2016); Mexico City's metro >4 million users/day, ~1.65 billion/year (Hernández et al. 2020); subway systems worldwide move >100 million people daily (Triadó-Margarit et al. 2017). 99% of passengers touch a surface during a trip, mostly with hands (Vargas-Robles et al. 2020).

**3.3 Touch surfaces dominated by human skin commensals.** Mexico City: Actinobacteria-dominated, *Cutibacterium* 15% (*C. acnes* 13%), *Corynebacterium* 13%, *Streptococcus* 9%, *Staphylococcus* 5% (*S. epidermidis* 4%); source-tracking gave dust ~34%, skin ~32%, saliva ~13%, soil ~4%, vaginal ~0.1%, **no faecal contribution**; trains carried more skin signal, stations more dust and soil (Hernández et al. 2020). Boston: Staphylococcaceae and Corynebacteriaceae highest mean relative abundance; gut/oral commensals (Lachnospiraceae, *Veillonella*, *Prevotella*) at low proportions (Hsu et al. 2016). NYC: taxa enriched for harmless skin-associated genera such as *Acinetobacter* (Afshinnekoo et al. 2015 — see §4 caveat).

**3.4 Air communities that differ from surface communities and track outdoor air, not commuters.** Oslo, 16 stations × 4 seasons: "significant differences between the air and surface bacterial communities, and across seasons"; diversity higher in spring/summer; temperature a strong driver ([Gohli et al. 2019, *Microbiome* 7:160, doi:10.1186/s40168-019-0772-9, PMID 31856911](https://link.springer.com/article/10.1186/s40168-019-0772-9)). NYC platform bioaerosols were compositionally simple (26 families ≈75% of sequences), similar system-wide and over 1.5 years, and "most closely resembled outdoor air," at 1×10⁴–4×10⁴ cells/m³ (mean 2.2×10⁴) (Robertson et al. 2013). Barcelona: ~10⁴ bacteria/m³, communities overlapping across trains, platforms and lobbies, dominated by *Methylobacterium*, human-associated and potentially pathogenic taxa <2% of reads — "commuters were found not to be the main source of bioaerosols" (Triadó-Margarit et al. 2017). Athens, naturally ventilated station: mean 2.82×10⁵ 16S rRNA gene copies/m³ of PM₁₀, higher on weekdays and daytime, dominated by environmental taxa (*Paracoccus*, *Sphingomonas*, *Cladosporium*, *Mycosphaerella*) with lower *Corynebacterium*/*Staphylococcus* (Grydaki et al. 2021). Seoul PM₁₀: mainly soil/environmental taxa (*Acinetobacter*, *Brevundimonas*, *Lysinibacillus*) ([*Sci Rep* 2023, s41598-023-49848-x](https://www.nature.com/articles/s41598-023-49848-x); seasonal companion: [*Sci Rep* 2022, s41598-022-21120-8](https://www.nature.com/articles/s41598-022-21120-8)).

**3.5 A distinctive abiotic matrix: iron-rich non-exhaust wear particles.** The defining physicochemical signature of the underground subway environment and the one that separates it from other indoor built environments. Fe-rich particles from brake–wheel–rail abrasion dominate subway PM₂.₅; in NYC, iron was ~43% of platform PM₂.₅ mass, ~126× outdoor ambient, with Si, S, Cu, Ni, Al, Ca, Ba and Mn as trace constituents ([*Atmospheric Pollution Research* 2023](https://www.sciencedirect.com/science/article/abs/pii/S1309104223001216); see also [Beijing Fe in PM₂.₅, *Atmos Environ* 2022](https://www.sciencedirect.com/science/article/abs/pii/S1352231022002400), and [Moreno et al., aerosol sources in subway environments, *Environ Res* 2018](https://www.sciencedirect.com/science/article/pii/S0013935118304158)). Barcelona: subway-specific sources up to 91% of platform PM₂.₅ in old stations vs 21–52% in newer stations with platform screen doors — i.e. **station design is a measurable modifier** (same source). Resuspension of settled tunnel dust by train piston effect and foot traffic is a major particle source (Seoul PM₁₀ study, above).

**3.6 A globally reproducible core community distinct from human commensals.** 4,728 samples, 60 cities, 32 countries, three years: **31 species present in 97% of samples and distinct from human commensal organisms**; 4,246 known species catalogued; 10,928 previously unobserved viral species (94.1% of 11,614 predicted); 748 novel bacterial genomes; 838,532 CRISPR arrays. Transit surfaces were shown to be a "distinct ecological niche," more dissimilar from soil than from human skin — an "ecologically distinct" ecosystem (Danko et al. 2021). *This is the strongest single piece of evidence that the concept names a real habitat rather than a sampling convenience.*

**3.7 Seasonal and diel structure despite the enclosure.** Beijing, 15 stations, monthly air filters Oct 2021–Sep 2022: 270 fungal genera, a persistent core, lower summer diversity, *Fusarium*/*Alternaria* in spring–summer vs *Aspergillus*/*Chaetomium*/*Cladosporium*/*Meyerozyma* in autumn–winter, varying by station type (interchange, airport, urban hub, suburban) (Liang et al. 2025). Hong Kong MTR: line-specific palm communities at morning rush hour converge into one network-wide community by evening ([Kang et al. 2018, *Cell Reports* 24:1190–1202, PMID 30067975, doi:10.1016/j.celrep.2018.07.006](https://www.cell.com/cell-reports/fulltext/S2211-1247(18)31051-9)). Hong Kong aerosols: [Leung et al. 2014, *Appl Environ Microbiol* 80:6760–6770, doi:10.1128/AEM.02244-14, PMID 25172855](https://pubmed.ncbi.nlm.nih.gov/25172855/). Cleaning perturbs and the community re-establishes with altered composition within hours on poles (Vargas-Robles et al. 2020).

**My inference, not a source claim:** (a) that "dry, oligotrophic, frequently cleaned, non-porous surfaces select for deposition-and-persistence rather than active growth" is a reasonable reading of 3.3+3.7 but I found **no** subway study that directly demonstrates in-situ growth versus deposition — do not put it in the definition; (b) that stations, tunnels and trains form one habitat rather than three is an ontological choice consistent with how the studies sample, not something any source asserts.

---

## 4. Source-quality caveats a curator must carry forward

- **Afshinnekoo et al. 2015** ([*Cell Systems* 1:72–87, doi:10.1016/j.cels.2015.01.001](https://www.cell.com/cell-systems/fulltext/S2405-4712(15)00002-2)) is the founding NYC study, but its anthrax and *Yersinia pestis* claims were rebutted and the paper amended — see "Lack of Evidence for Plague or Anthrax on the New York City Subway," *Cell Syst* 1:4–5, and "Modern Methods for Delineating Metagenomic Complexity," *Cell Syst* 1:6–7. **Cite the amended version; do not repeat the pathogen claims.** Hsu et al. 2016 explicitly position their work against that study's non-standardized surface metadata.
- Danko et al. 2021 uses "mass transit system," not "subway" — its corpus includes bus systems in cities without a metro. Do not silently equate the MetaSUB corpus with this concept.
- Data availability for Danko et al. 2021: https://pngb.io/metasub-2021; raw reads SRA `PRJNA732392`.

---

## 5. Synonyms, and what NOT to conflate

**Names in real use for this concept (safe as synonyms):** subway; subway system; metro; metro system; underground; the Underground; the Tube; MRT; mass rapid transit; metropolitan railway; rapid transit system (underground sense); U-Bahn; métro; metropolitana. (Sources: [Wikipedia, *Rapid transit*](https://en.wikipedia.org/wiki/Rapid_transit); [Britannica](https://www.britannica.com/technology/rapid-transit); ENVO:03501116 synonym set; and the titles of Hernández et al. 2020, "metro (subway/underground)".)

**Wrongly treated as the same thing — keep out:**

| Not this | Why |
|---|---|
| `ENVO:03501109` **subway train** / `ENVO:03501115` public subway train | Rolling stock only. The exact over-narrow grounding #67 removed. |
| **Pedestrian subway / underpass** (British English) | A footway under a road or railway; unrelated to rail transit. A real homograph, documented in the *Rapid transit* terminology section. |
| **Light rail, tram, streetcar** | Often street-running, not grade-separated; conflated by ENVO:03501116's own synonym list, which is a bug in that term. |
| **Commuter/suburban rail, mainline railway station** | Longer routes, shared track, lower frequency, above ground; e.g. the Seoul PM₁₀ study deliberately contrasts subway with KTX stations. |
| **Bus, bus terminal, "urban transit system" broadly** | The MetaSUB superset; not the GOLD concept. |
| **Road tunnels, subsea tunnels, utility/sewer tunnels** | Share the "underground concrete" physics but have no passenger flux; e.g. the Oslofjord subsea road tunnel nitrifier-biofilm work ([PMID 40156577](https://pubmed.ncbi.nlm.nih.gov/40156577/)) is *not* subway literature. |
| **"Subway" the sandwich franchise** | A trademark; a genuine text-mining conflation risk for a corpus that also has a FOOD category. Worth noting in the record. |
| **Passenger skin/palm samples taken after riding** | Kang et al. 2018 and Vargas-Robles et al. 2020 sample *hands*; those are host-associated samples, not subway-environment samples. |

---

## 6. Should this be a term at all?

**Yes.** It is a place, not a process, quality, disease or taxon, and it is one of the most heavily sampled built environments in microbiology: 4,728 samples across 60 cities in a single coordinated study, plus independent city-scale studies in New York, Boston, Hong Kong, Barcelona, Oslo, Athens, Seoul, Moscow, Mexico City and Beijing. Danko et al. 2021 demonstrate it is an "ecologically distinct" niche with a 31-species core distinct from human commensals, which is the substantive test for "is there a there there."

**Two honest caveats for the curator:**

1. **Upstream assertion volume on this record is 0.** The concept is attested as a GOLD path but carries no assertions in this corpus. The definition below is therefore justified by the external literature, not by sample volume here — worth saying in the note, since `just report` ranks the backlog by assertion volume and this record will never surface there.
2. **The concept is arguably two habitats with different physics** — *subway surface* (skin-commensal dominated, human-sourced: Hsu 2016, Hernández 2020) and *subway air* (outdoor/soil-sourced, ventilation-driven: Robertson 2013, Triadó-Margarit 2017, Grydaki 2021), which Gohli et al. 2019 showed differ significantly within the same 16 stations. That is an argument for one term with two children, not for splitting or for declining the term. If HabitatMech ever needs sample-type resolution, `subway surface` and `subway air` are the natural children and both would be well-evidenced.

---

## Sources

- [Danko D, et al. A global metagenomic map of urban microbiomes and antimicrobial resistance. *Cell* 184:3376–3393.e17, 24 Jun 2021. doi:10.1016/j.cell.2021.05.002 (PMID 34043940)](https://www.cell.com/cell/fulltext/S0092-8674(21)00585-7)
- [Afshinnekoo E, et al. Geospatial resolution of human and bacterial diversity with city-scale metagenomics. *Cell Systems* 1:72–87, 2015. doi:10.1016/j.cels.2015.01.001 — **use the amended version**](https://www.cell.com/cell-systems/fulltext/S2405-4712(15)00002-2)
- [Hsu T, et al. Urban transit system microbial communities differ by surface type and interaction with humans and the environment. *mSystems* 1(3):e00018-16, 2016. doi:10.1128/mSystems.00018-16 (PMC5069760)](https://journals.asm.org/doi/10.1128/msystems.00018-16)
- [Hernández AM, Vargas-Robles D, Alcaraz LD, Peimbert M. Station and train surface microbiomes of Mexico City's metro (subway/underground). *Sci Rep* 10:8798, 29 May 2020. doi:10.1038/s41598-020-65643-4 (PMC7260218)](https://www.nature.com/articles/s41598-020-65643-4)
- [Vargas-Robles D, et al. Passenger-surface microbiome interactions in the subway of Mexico City. *PLoS ONE* 15:e0237272, 2020. doi:10.1371/journal.pone.0237272 (PMID 32813719)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0237272)
- [Robertson CE, et al. Culture-independent analysis of aerosol microbiology in a metropolitan subway system. *Appl Environ Microbiol* 79:3485–3493, 2013. doi:10.1128/AEM.00331-13 (PMC3648054)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3648054/)
- [Triadó-Margarit X, et al. Bioaerosols in the Barcelona subway system. *Indoor Air* 27:564–575, 2017. doi:10.1111/ina.12343 (PMID 27687789)](https://onlinelibrary.wiley.com/doi/10.1111/ina.12343)
- [Gohli J, Bøifot KO, Moen LV, Pastuszek P, Skogan G, Udekwu KI, Dybwad M. The subway microbiome: seasonal dynamics and direct comparison of air and surface bacterial communities. *Microbiome* 7:160, 2019. doi:10.1186/s40168-019-0772-9 (PMID 31856911)](https://link.springer.com/article/10.1186/s40168-019-0772-9)
- [Grydaki N, Colbeck I, Mendes L, Eleftheriadis K, Whitby C. Bioaerosols in the Athens Metro: metagenetic insights into the PM₁₀ microbiome in a naturally ventilated subway station. *Environ Int* 146:106186, 2021. doi:10.1016/j.envint.2020.106186 (PMID 33126062)](https://www.sciencedirect.com/science/article/pii/S0160412020321413)
- [Leung MHY, Wilkins D, Li EKT, Kong FKF, Lee PKH. Indoor-air microbiome in an urban subway network: diversity and dynamics. *Appl Environ Microbiol* 80:6760–6770, 2014. doi:10.1128/AEM.02244-14 (PMID 25172855)](https://pubmed.ncbi.nlm.nih.gov/25172855/)
- [Kang K, et al. The environmental exposures and inner- and intercity traffic flows of the metro system may contribute to the skin microbiome and resistome. *Cell Reports* 24:1190–1202, 2018. doi:10.1016/j.celrep.2018.07.006 (PMID 30067975)](https://www.cell.com/cell-reports/fulltext/S2211-1247(18)31051-9)
- [Liang et al. Fungal communities in Beijing subway station air. *Microbiology Spectrum*, 25 Sep 2025. doi:10.1128/spectrum.01626-25](https://journals.asm.org/doi/10.1128/spectrum.01626-25) · [ASM press release](https://asm.org/press-releases/2025/september/new-study-reveals-subway-station-fungal-communitie)
- [Bacterial communities in PM₁₀ from Seoul subway and railway stations. *Sci Rep*, 2023. doi:10.1038/s41598-023-49848-x (PMC10948816)](https://www.nature.com/articles/s41598-023-49848-x) · [Seasonal variation companion, *Sci Rep* 2022, doi:10.1038/s41598-022-21120-8](https://www.nature.com/articles/s41598-022-21120-8)
- [Particulate matter concentration and composition in the New York City subway system. *Atmospheric Pollution Research*, 2023](https://www.sciencedirect.com/science/article/abs/pii/S1309104223001216) · [Aerosol sources in subway environments, *Environ Res*, 2018](https://www.sciencedirect.com/science/article/pii/S0013935118304158) · [Atmospheric iron particles in PM₂.₅ from a Beijing subway station, *Atmos Environ*, 2022](https://www.sciencedirect.com/science/article/abs/pii/S1352231022002400)
- [Association between subway iron particulate matter exposure and respiratory disease in New York City (PMC12779137)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12779137/)
- [ENVO via EMBL-EBI OLS4 — terms ENVO:03501116, ENVO:03501111, ENVO:03501110, ENVO:03501109, ENVO:03501115, ENVO:03501117, ENVO:03501118, ENVO:01000313, ENVO:03501339, ENVO:00000856, ENVO:00000065, ENVO:00000068 (retrieved August 2026)](https://www.ebi.ac.uk/ols4/ontologies/envo)
- [JGI GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)
- [Britannica, *Rapid transit*](https://www.britannica.com/technology/rapid-transit) · [Wikipedia, *Rapid transit*](https://en.wikipedia.org/wiki/Rapid_transit) · [UITP/GTKP, Mass Rapid Transit definitions](https://www.gtkp.com/wp-content/uploads/from-gtkp/documents/17/20100214-204543-5022-UMTIS%20MRT.pdf) · [ITDP Rapid Transit Database](https://itdp.org/rapid-transit-database/)
- [Nitrifier biofilms on concrete in the Oslofjord subsea tunnel (PMID 40156577)](https://pubmed.ncbi.nlm.nih.gov/40156577/) — cited only as a *contrast* case, not subway literature

## Citations

1. https://gold.jgi.doe.gov/ecosystem_classification
2. https://www.cell.com/cell/fulltext/S0092-8674(21
3. https://www.nature.com/articles/s41598-020-65643-4
4. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0237272
5. https://journals.asm.org/doi/10.1128/msystems.00018-16
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC3648054/
7. https://onlinelibrary.wiley.com/doi/10.1111/ina.12343
8. https://www.sciencedirect.com/science/article/pii/S0160412020321413
9. https://en.wikipedia.org/wiki/Rapid_transit
10. https://www.ebi.ac.uk/ols4/ontologies/envo
11. https://www.britannica.com/technology/rapid-transit
12. https://itdp.org/rapid-transit-database/
13. https://www.gtkp.com/wp-content/uploads/from-gtkp/documents/17/20100214-204543-5022-UMTIS%20MRT.pdf
14. https://journals.asm.org/doi/10.1128/spectrum.01626-25
15. https://asm.org/press-releases/2025/september/new-study-reveals-subway-station-fungal-communitie
16. https://link.springer.com/article/10.1186/s40168-019-0772-9
17. https://www.nature.com/articles/s41598-023-49848-x
18. https://www.nature.com/articles/s41598-022-21120-8
19. https://www.sciencedirect.com/science/article/abs/pii/S1309104223001216
20. https://www.sciencedirect.com/science/article/abs/pii/S1352231022002400
21. https://www.sciencedirect.com/science/article/pii/S0013935118304158
22. https://www.cell.com/cell-reports/fulltext/S2211-1247(18
23. https://pubmed.ncbi.nlm.nih.gov/25172855/
24. https://www.cell.com/cell-systems/fulltext/S2405-4712(15
25. https://pngb.io/metasub-2021
26. https://pubmed.ncbi.nlm.nih.gov/40156577/
27. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12779137/