---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T03:55:19.922463'
end_time: '2026-08-18T04:05:10.298509'
duration_seconds: 590.38
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Indoor
  habitat_identifier: habitatmech:GOLD.b4e93f5d66
  habitat_category: ENGINEERED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Engineered > Artificial ecosystem > Water channel system >
    Indoor'
  assertions: '0'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. GOLD''s
    ''Indoor'' node. The mapping table pointed it at ENVO:01000856, which it labels
    ''indoor environment'' and ENVO labels ''temperate marginal sea biome''. No indoor-environment
    term in the vendored slice. Term request. (source concept habitatmech:GOLD.b4e93f5d66)'
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
  web_search_requests: 9
  num_turns: 31
  total_cost_usd: 2.6069264999999997
  session_id: 551d97de-98db-4d65-bea8-0fcdcc5158a4
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 21
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Indoor
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.b4e93f5d66
- **Category:** ENGINEERED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Engineered > Artificial ecosystem > Water channel system > Indoor
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. GOLD's 'Indoor' node. The mapping table pointed it at ENVO:01000856, which it labels 'indoor environment' and ENVO labels 'temperate marginal sea biome'. No indoor-environment term in the vendored slice. Term request. (source concept habitatmech:GOLD.b4e93f5d66)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Indoor** as a microbial habitat, with citations.

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

I'll load the web research tools and start.

# Novel-Term Definition Research: **Indoor** (`habitatmech:GOLD.b4e93f5d66`)

## Proposed definition

> A vivarium which consists of one or more artificial channels through which water is pumped or recirculated over a colonisable substratum, and which is enclosed within a building envelope such that illumination, temperature and water source are set by the operator rather than by ambient conditions.

**Proposed label:** `indoor artificial water channel system` (or `indoor experimental stream channel`). The bare string "Indoor" must not be the term label — see §1 and §6.

**Caveat on the sentence, stated up front:** an intermediate class is missing. The differentia above carries two independent loads — *being an artificial water channel system* (which distinguishes it from aquaria, terraria and soil microcosms) and *being indoors* (which distinguishes it from its GOLD sibling `Outdoor`). The parent record `habitatmech:GOLD.87bf5e5370` "Water channel system" is itself `UNGROUNDED` with only a class-level sweep recorded and no assessment of whether it is a habitat at all. **The cleanest fix is to define the parent first** — `artificial water channel system` = "A vivarium which consists of one or more artificial channels through which water is pumped or recirculated over a colonisable substratum" — after which this term reduces to a genuinely one-differentia definition: *"An artificial water channel system which is enclosed within a building envelope."* I recommend requesting both terms together.

---

## 1. What the concept denotes

### 1.1 The concept is *not* "indoors"; it is *an indoor experimental stream channel*

The label is a bare modifier. Its content comes entirely from its position in the GOLD path, verified against this repository's own extraction (`data/raw/gold_ecosystem_paths.tsv`):

```
Engineered > Artificial ecosystem > Water channel system              gold.ecosystem:8489
Engineered > Artificial ecosystem > Water channel system > Indoor     gold.ecosystem:8490, 8491
Engineered > Artificial ecosystem > Water channel system > Indoor > Biofilm   gold.ecosystem:8494
Engineered > Artificial ecosystem > Water channel system > Outdoor    gold.ecosystem:8492, 8493
```

Three pieces of local evidence fix the reading:

1. **`Indoor` and `Outdoor` are the *only* two children of `Water channel system`.** A two-way indoor/outdoor split under a facility type is the standard classification axis for experimental stream facilities, not a description of a room.
2. **The single child of `Indoor` is `Biofilm`** (`gold.ecosystem:8494`, this repo's `data/habitats/engineered/biofilm__5327749c.yaml`). Benthic biofilm on channel substrata is the canonical sampled material in experimental stream work.
3. **The siblings of `Water channel system` under `Artificial ecosystem` are `Aquaculture`, `Mesocosm` and `Microcosm`** — all deliberately-constructed experimental or cultivation systems, none of them building infrastructure.

**What is sampled:** the microbial biofilm (periphyton, benthic biofilm) growing on tiles, gravel, glass or sediment inside the channel, and secondarily the recirculating water and sediment. In the exemplar facility, "marble tiles (33.6 cm² of surface area)" served as "standard biofilm substrata," colonised for 25 days in a river before transfer to the indoor channels ([Pérez-Calpe et al. 2021, *PLoS ONE* 16(2):e0246719](https://doi.org/10.1371/journal.pone.0246719), PMID 33571231).

### 1.2 The boundary — what is inside and what is a neighbouring concept

**Inside the concept:** laboratory and building-housed artificial stream channels, recirculating flumes, "experimental streams," "artificial streams," "stream mesocosms" and "flume microcosms" operated under a roof. Menczelesz, Szivák & Schmera define experimental streams as "bounded (i.e., having solid impermeable margins) and partially enclosed experimental units that closely simulate specific elements of natural stream ecosystems," and place them on a continuum "ranging from indoor laboratory streams to outdoor artificial channels" ([*Hydrobiologia* 847:1–10, 2019](https://doi.org/10.1007/s10750-019-04093-0)).

**Outside the concept — neighbouring concepts, with the evidence:**

| Neighbour | Why it is *not* this concept |
|---|---|
| **Real-world water conveyance inside/around buildings** (canals, culverts, ditches, town waterways) | GOLD files these under a *different* branch entirely: `Engineered > Built environment > Canal`, `> Canal > Irrigation canal`, `> Canal > Town canal`, `> Canal > Water` (verified in `data/raw/gold_ecosystem_paths.tsv`). This is the decisive local evidence against the "plumbing/waterway inside a building" reading. |
| **Indoor air** | GOLD's *other* `Indoor` nodes are `Environmental > Air > Indoor Air` and its children (`Dust`, `Cattle barn`, `Poultry farm`, `Air scrubber`). Different top-level ecosystem, different medium. Conflating these two `Indoor` labels is the single most likely curation error here. |
| **Building plumbing / drinking-water distribution** | GOLD: `Engineered > Built environment > Drinking water treatment plant > Drinking water`, `> Building > Sink`. Distinct branch. |
| **Outdoor / streamside flume mesocosms** | The explicit sibling `gold.ecosystem:8492/8493`, corresponding to `data/habitats/engineered/outdoor.yaml` (`habitatmech:GOLD.33fb90237d`). |
| **Aquaria and static tanks** | No directed flow; GOLD files aquaculture tanks under `Artificial ecosystem > Aquaculture > Fish tank` etc. ENVO covers this at `ENVO:00002196` *aquarium*. |
| **Bioreactors, lab enrichments** | Separate GOLD categories (`Engineered > Bioreactor`, `> Lab enrichment`). Those are not channel-flow simulations of a lotic system. |

### 1.3 Is the label ambiguous?

Yes, **as a bare string** — "Indoor" in isolation admits at least three readings (indoor air; indoor built environment/surfaces; indoor experimental apparatus). But the path disambiguates completely, and the reading above is the only one consistent with (a) the `Artificial ecosystem` parent category, (b) the `Water channel system` parent, (c) the `Outdoor` sibling, and (d) the `Biofilm` child. *This ranking of the readings is my inference from the path structure; GOLD publishes no textual definition for its ecosystem nodes* ([GOLD v.10, Mukherjee et al. 2025, *NAR* 53:D989–D997](https://doi.org/10.1093/nar/gkae1000); GOLD states its classification "is not a comprehensive list of all possible paths" and is driven by curated samples).

---

## 2. Genus — the broader kind

### 2.1 Recommended genus: `ENVO:00010622` **vivarium** — in the vendored slice ✓

> "A vivarium is an enclosure for keeping and raising organisms for observation or research. Often, a portion of the ecosystem for a particular species is simulated on a smaller scale, with controls for environmental conditions."

This is the smallest well-established ENVO kind that an indoor recirculating stream channel falls under without over-claiming. It is *enclosure for research* + *simulated portion of an ecosystem* + *controlled conditions* — exactly Menczelesz et al.'s "bounded and partially enclosed experimental units." It asserts nothing about landform-hood, nothing about siting in nature, and nothing about scale. `ENVO:00010622` is the parent of `mesocosm`, `microcosm`, `aquarium` and `terrarium` (verified via OLS4 hierarchical-parents for each), so it is genuinely the common genus of the family this concept belongs to.

### 2.2 Near-misses, and why each fails

All of the following **are present in `data/raw/ontology_terms.tsv`**, so none of them is an "absent from the slice" problem — each is a semantic mismatch. (The original curator note's claim that no *indoor-environment* term is in the slice is correct; ENVO's only `indoor*` classes are `ENVO:01000421` *indoor kitchen* and `ENVO:01000425` *indoor toilet*, confirmed by an OLS4 search of ENVO for "indoor".)

| CURIE | Label | Why it is a near-miss, not a match |
|---|---|---|
| `ENVO:01000620` | **mesocosm** | *"…a vivarium that is **embedded within a natural environment**…"* — the definition explicitly excludes indoor siting. This term fits the **`Outdoor` sibling**, not this one. Note the terminological trap: the literature routinely calls indoor facilities "mesocosms" (e.g. the 38-m indoor recirculating stream mesocosms at the German Federal Environment Agency, [Tromboni et al. 2026, *L&O* 71(1)](https://doi.org/10.1002/lno.70285)), so ENVO's definition and common usage disagree. **Do not ground here.** |
| `ENVO:01000621` | **microcosm** | *"…a vivarium within which a simple ecosystem is artificially established and used to simulate and predict the behaviour of natural ecosystems under controlled conditions."* This is a defensible fallback genus — it is silent on siting and matches the literature's "flume microcosms" phrasing ([Reis & Barroso 2025, *L&O Methods* 23:309–325](https://doi.org/10.1002/lom3.10681)). It is *narrower* than vivarium and imports a "simple ecosystem / small scale" claim that a 38-m channel array strains. Acceptable as a second choice; `vivarium` is safer. |
| `ENVO:00000121` | **artificial channel** | *"A channel of a watercource which has been constructed by humans."* Its asserted parents are `ENVO:00000070` *human construction* **and** `ENVO:00000395` *channel of a watercourse* — the latter defined as "a **depressed landform** which physically confines a river, slough or ocean strait, and which consists of a bed and banks." A methacrylate channel on a laboratory bench is not a landform confining a river. Grounding here would publish landform-hood that no source claims. Note it carries "flume" as a synonym, which will attract false lexical matches. |
| `ENVO:00000079` | **flume** | *"An open artificial water channel, that leads water from a diversion dam or weir completely aside a natural flow, often an elevated box structure (typically wood) that follows the natural contours of the land."* Subclass of `ENVO:00000014` *canal*. This is the **civil-engineering homonym** — a mill flume or log flume — not the laboratory hydraulic flume. Pure lexical trap; the highest-risk wrong grounding for this record. |
| `ENVO:00000014` | **canal** | *"Artificial watercourse with no flow or a controlled flow used for navigation, drainage or irrigation."* Purpose clause excludes experimentation; and GOLD already routes real canals to `Built environment > Canal`. |
| `ENVO:00002196` | **aquarium** | A vivarium simulating *submerged portions* of an aquatic environment — a sibling under `vivarium`, not a parent. Lacks directed flow. |
| `ENVO:01001405` | **laboratory environment** | *"An anthropogenic environment which is bounded by the building envelope of a laboratory…"* This captures the **indoor differentia** but is the *room*, not the channel. Useful as a **`relation: xref`** or as the value of a `part_of`-style link; it is not the genus. |
| `ENVO:01001406` | **laboratory facility** | The building/facility, same failure mode as above. |
| `ENVO:01000856` | *temperate marginal sea biome* | The upstream mapping table's target, mislabelled "indoor environment" in that table. Confirmed wrong: OLS4 resolves `ENVO:01000856` to *temperate marginal sea biome*. The existing curator note is correct and this should stay recorded as a mapping-table defect. |

**Conclusion:** no ENVO term names this concept. `vivarium` is the genus; the term itself is a genuine term-request candidate.

---

## 3. Differentia — what distinguishes it

Ordered by how observable/recordable each property is.

### 3.1 Against the sibling `Outdoor` — the primary differentia

**Enclosure within a building envelope, with the consequence that light, temperature and photoperiod are set instrumentally rather than ambiently.**

- The trade-off is the standard framing in the mesocosm methods literature: "outdoor mesocosms are more realistic in terms of representing natural environmental conditions, [while] indoor systems often offer advantages of increased control and monitoring of experimental conditions" ([Macaulay et al. 2025, *Oikos* 2025(5)](https://doi.org/10.1111/oik.11020); see also [Schaum, Comeau & Mullarney 2025, *L&O* 70(S2)](https://doi.org/10.1002/lno.70265)).
- The distinction is built into facilities deliberately: the German Federal Environment Agency constructed a paired modular system of **eight outdoor and eight indoor** ponds and streams precisely so that the indoor/outdoor axis could be varied — the paper's title is "Enhanced experimental flexibility and control in ecotoxicological mesocosm experiments — a new outdoor and indoor pond and stream system" ([Mohr et al. 2005, *Environ Sci Pollut Res Int* 12(1):5–7](https://doi.org/10.1065/espr2004.08.217), PMID 15768734). **This is the strongest single citation that indoor-vs-outdoor is a recognised, designed-for distinction in exactly this class of facility, and not a curatorial invention.**

**Observable correlates of the indoor differentia:**

| Property | Indoor (this concept) | Outdoor (sibling) |
|---|---|---|
| Illumination | Artificial, fixed spectrum and photoperiod. E.g. "LED lights (36 W 6500 k, Aquael, Poland) with a 12/12 light/dark cycle and an intensity of 27.1 ± 1.0 μmol m⁻² s⁻¹" (Pérez-Calpe et al. 2021); indoor flumes "under 12 h light:dark cycles" ([Roche et al. 2017, *WRR* 53:222–236](https://doi.org/10.1002/2016WR019041)) | Natural sunlight; shading imposed as a treatment |
| Temperature | Room-controlled, or a manipulated factor | Ambient, diel- and season-varying |
| Seasonality / weather | Absent | Present (rain, wind, aerial deposition) |
| Natural colonisation | Excluded; inoculation is deliberate (pre-colonised tiles, filtered source water) | Possible via drift, aerial and riparian input — the reason open flow-through outdoor designs are held to be more realistic (Macaulay et al. 2025) |

### 3.2 Against other vivaria (aquaria, terraria, soil microcosms) — the channel differentia

- **Directed, pumped or recirculating flow through an elongate open channel**, with velocity/discharge as a controllable variable. Facility examples: 30 methacrylate channels, 200 × 15 × 20 cm, fed from six 200-L block tanks in a closed pump-driven recirculation, water depth ≈3.4 cm (Pérez-Calpe et al. 2021); 38-m glass-fibre-reinforced-polyester channels with screw pumps for velocity control (Tromboni et al. 2026); 20 recirculating fibreglass channels driven by a stainless-steel paddle wheel (Cary Institute [Artificial Stream Facility](https://www.caryinstitute.org/science/research-projects/artificial-stream-facility)); 16 streams up to 106 m, operable circular or flow-through at 0.02–0.6 m s⁻¹ (Mohr et al. 2005).
- **A colonisable benthic substratum** — aquarium gravel, marble or ceramic tiles, or natural sediment (Pérez-Calpe et al. 2021; [Schmidt et al. 2015, *Environ Sci Eur* 27(1)](https://doi.org/10.1186/s12302-014-0037-y)).
- **Replication for factorial designs** — arrays of nominally identical channels, permitting flow × sediment, flow × temperature, or nutrient × light designs (Pérez-Calpe et al. 2021; Menczelesz et al. 2019).

### 3.3 Characteristic microbiology (supports "habitat", constrains the differentia)

- The dominant sampled assemblage is **benthic biofilm / periphyton**: an autotroph–heterotroph consortium in an EPS matrix on the channel substratum. `ENVO:00002034` *biofilm* — "a complex aggregation of microorganisms marked by the excretion of a protective and adhesive matrix; usually adhering to a substratum" — is already the parent used on the child record `habitatmech:GOLD.905d58ea72`.
- Biofilm in these channels is measured as chlorophyll-*a*, gross primary production, community respiration and net community metabolism (Pérez-Calpe et al. 2021), and as EPS, microbial biomass, community composition and substratum adhesiveness (Schmidt et al. 2015).
- Community assembly in flume-grown biofilms can be dominated by **successional dynamics rather than by the imposed treatments** — in streamside flume mesocosms crossing four flow regimes with ambient vs +2 °C, composition was "largely driven by successional dynamics independent of treatments" ([Ezzat et al. 2025, glacier-fed stream biofilm flume experiment, PMC11705997](https://pmc.ncbi.nlm.nih.gov/articles/PMC11705997/)). *Curator note: this is a property of flume biofilms generally, observed in a streamside (i.e. outdoor) facility; I have no source establishing it specifically for indoor channels.*
- Biofilms in indoor flumes measurably alter their own physical habitat, controlling fine-particle deposition and resuspension (Roche et al. 2017) and stabilising the sediment substratum relative to abiotic controls (Schmidt et al. 2015).

---

## 4. Sources

**Definitional / methodological**
- Menczelesz N, Szivák I, Schmera D. "How do we construct and operate experimental streams? An overview of facilities, protocols, and studied questions." *Hydrobiologia* 847:1–10 (online 19 Oct 2019). https://doi.org/10.1007/s10750-019-04093-0 — *the primary definitional source for the genus and the indoor↔outdoor continuum.*
- Mohr S, Feibicke M, Ottenströer T, Meinecke S, Berghahn R, Schmidt R. "Enhanced experimental flexibility and control in ecotoxicological mesocosm experiments — a new outdoor and indoor pond and stream system." *Environ Sci Pollut Res Int* 12(1):5–7 (2005). https://doi.org/10.1065/espr2004.08.217 — PMID 15768734. *Paired indoor/outdoor stream facility; establishes the differentia as a designed distinction.*
- Macaulay S, Jeppesen E, Riebesell U, Nejstgaard J, Berger S, Lewandowska A, et al. "Addressing grand ecological challenges in aquatic ecosystems: how can mesocosms be used to advance solutions?" *Oikos* 2025(5), 11 Feb 2025. https://doi.org/10.1111/oik.11020
- Schaum C, Comeau S, Mullarney J. "Mesocosms: Bridging the gap between in situ and laboratory studies." *Limnology and Oceanography* 70(S2), 20 Nov 2025. https://doi.org/10.1002/lno.70265
- Lamberti GA, Steinman AD (eds). "Research in Artificial Streams: Applications, Uses, and Abuses." *J. North American Benthological Society* 12(4):313–384 (1993). https://doi.org/10.2307/1467618 — *the foundational synthesis for the whole facility class.*

**Facility descriptions and microbiology (primary literature)**
- Pérez-Calpe AV, Larrañaga A, von Schiller D, Elosegi A. "Interactive effects of discharge reduction and fine sediments on stream biofilm metabolism." *PLoS ONE* 16(2):e0246719 (2021). https://doi.org/10.1371/journal.pone.0246719 — PMID 33571231. *30 indoor methacrylate channels; the clearest single exemplar of the concept.*
- Roche KR, Drummond JD, Boano F, Packman AI, Battin TJ, Hunter WR. "Benthic biofilm controls on fine particle dynamics in streams." *Water Resources Research* 53(1):222–236 (2017). https://doi.org/10.1002/2016WR019041 — *indoor recirculating flumes, 12 h L:D, 0–47 d biofilm growth.*
- Tromboni F, Jativa C, Seitz C, Maasri A, Mohr S, Grossart H-P, et al. "Flow variability and macroinvertebrates jointly regulate stream periphyton and metabolism: Insights from experimental stream mesocosms." *Limnology and Oceanography* 71(1), 13 Dec 2025. https://doi.org/10.1002/lno.70285 — *eight 38-m indoor recirculating stream mesocosms, Berlin.*
- Schmidt H, Thom M, Matthies K, Behrens S, Obst U, Wieprecht S, et al. "A multi-disciplinarily designed mesocosm to address the complex flow–sediment–ecology tripartite relationship on the microscale." *Environmental Sciences Europe* 27(1) (14 Jan 2015). https://doi.org/10.1186/s12302-014-0037-y — *six-flume mesocosm; EPS, biomass, community composition, biostabilisation.*
- Reis L, Barroso G. "Fast responses, rich insights: Optimizing experimental stream studies using periphyton for comprehensive environmental assessment." *Limnology and Oceanography: Methods* 23(5):309–325 (19 Mar 2025). https://doi.org/10.1002/lom3.10681
- Ezzat L et al. "Experimental evidence on the impact of climate-induced hydrological and thermal variations on glacier-fed stream biofilms." https://pmc.ncbi.nlm.nih.gov/articles/PMC11705997/
- Cary Institute of Ecosystem Studies, [Artificial Stream Facility](https://www.caryinstitute.org/science/research-projects/artificial-stream-facility) (accessed 18 Aug 2026).
- Helmholtz Centre for Environmental Research, [BIOFLOW project](https://www.ufz.de/index.php?en=41619) (accessed 18 Aug 2026).

**Vocabularies and standards**
- Mukherjee S, Stamatis D, Li CT, Ovchinnikova G, Kandimalla M, Handke V, et al. "Genomes OnLine Database (GOLD) v.10: new features and updates." *Nucleic Acids Research* 53(D1):D989–D997 (2025). https://doi.org/10.1093/nar/gkae1000
- Mukherjee S, et al. "Twenty-five years of Genomes OnLine Database (GOLD): data updates and new features in v.9." *NAR* 51(D1):D957–D963 (2023). https://doi.org/10.1093/nar/gkac974 (correction: *NAR* 52(6):3483, https://doi.org/10.1093/nar/gkae162)
- GOLD [Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification) (page returns HTTP 403 to automated fetch; the path facts above were verified instead against this repository's own `data/raw/gold_ecosystem_paths.tsv`, which is the extraction of record).
- ENVO term definitions and hierarchy verified 18 Aug 2026 via the EBI OLS4 API (`https://www.ebi.ac.uk/ols4/api/`) and cross-checked against `data/raw/ontology_terms.tsv` in this repository.
- Buttigieg PL, Pafilis E, Lewis SE, Schildhauer MP, Walls RL, Mungall CJ. "The environment ontology in 2016: bridging domains with increased scope, semantic density, and interoperation." *J Biomed Semantics* 7:57 (2016). https://doi.org/10.1186/s13326-016-0097-6
- Glass EM, Dribinsky Y, Yilmaz P, et al. "MIxS-BE: a MIxS extension defining a minimum information standard for sequence data from the built environment." *ISME J* 8:1–3 (2014). https://doi.org/10.1038/ismej.2013.176 — *relevant only as the standard governing the neighbouring* indoor air / built environment *concepts this must not be conflated with.*

**Marked as inference, not sourced**
- The claim that GOLD's `Indoor` node means *indoor water channel system* rather than *indoor space*. GOLD publishes no textual definitions for ecosystem nodes; this is inferred from the path, the `Outdoor` sibling, the `Biofilm` child, the `Artificial ecosystem` category, and GOLD's separate routing of real canals to `Built environment > Canal`. The inference is strong but it is an inference.
- The choice of `vivarium` over `microcosm` as genus. No source ranks these for this concept; the argument is that `microcosm`'s "simple ecosystem" clause is strained by 38-m multi-trophic channel arrays.
- The tabulated indoor/outdoor correlates in §3.1 are assembled from the facility descriptions cited; no single source presents them as a table.

---

## 5. Synonyms, and what NOT to conflate

### Names in real use for this concept
- indoor experimental stream / indoor experimental streams
- indoor artificial stream / indoor artificial stream channel
- laboratory stream / laboratory streams (Menczelesz et al. 2019)
- indoor flume, laboratory flume, recirculating flume (Roche et al. 2017)
- indoor stream mesocosm (Tromboni et al. 2026) — *in-literature usage; see the ENVO conflict noted in §2.2*
- flume microcosm (Reis & Barroso 2025)
- indoor recirculating channel (Pérez-Calpe et al. 2021)
- artificial stream channel (Cary Institute)

Suggested `exact synonym` set for the term request: *indoor experimental stream*, *indoor artificial stream channel*, *laboratory stream channel*, *indoor flume*. Suggested `related synonym`: *indoor stream mesocosm*.

### Commonly but wrongly treated as the same thing

1. **Indoor air / the indoor microbiome of the built environment.** The most dangerous conflation, because GOLD contains a *second, unrelated* `Indoor` at `Environmental > Air > Indoor Air`. That concept is governed by MIxS-BE (Glass et al. 2014); this one is not. Different ecosystem, different medium, different literature.
2. **`ENVO:00000079` *flume* (mill/log flume).** A homonym. ENVO's flume is an outdoor wooden or elevated conveyance leading water aside a natural flow; it is a subclass of *canal*. Nothing to do with a laboratory hydraulic flume.
3. **`ENVO:00000121` *artificial channel*.** Its exact/related synonyms in the slice literally include "flume", so lexical matching will propose it. It is a *channel of a watercourse*, i.e. a landform.
4. **Canals, ditches, irrigation channels, town waterways.** GOLD itself separates these into `Built environment > Canal`.
5. **`ENVO:01000620` *mesocosm*.** Excluded by its own definition ("embedded within a natural environment") despite widespread literature usage of "indoor mesocosm". Belongs to the `Outdoor` sibling.
6. **Aquaria, fish tanks, RAS systems.** No directed channel flow; GOLD routes these to `Artificial ecosystem > Aquaculture`.
7. **Bioreactors and lab enrichment cultures.** Separate GOLD categories; not simulations of a lotic ecosystem.
8. **The room the channels sit in.** `ENVO:01001405` *laboratory environment* names the enclosing space, not the habitat sampled. Link it, don't ground to it.

---

## 6. Should it be a term at all?

**Yes — but not under this label, and preferably not alone.**

**It is a habitat.** It is a physical place that microorganisms colonise and are sampled from; there is a substantial primary literature on the microbial communities that grow there; and the concept's own GOLD child is `Biofilm`. It is not a process, a quality, a disease state, a taxon, or a sampling artefact. It is squarely within HabitatMech's `ENGINEERED` category, which already contains bioreactors and aquaculture systems. `NOT_APPLICABLE` would be wrong.

**Three qualifications the curator should record:**

1. **The label must change.** "Indoor" is a bare adjective and is *not* a term label. Requesting a term labelled "Indoor" would produce an ENVO class indistinguishable from indoor air, indoor kitchens and indoor toilets. Request `indoor artificial water channel system` (or `indoor experimental stream channel`), with `Indoor` recorded only as the GOLD source label.

2. **Request the parent in the same batch.** The intermediate class `artificial water channel system` (this record's parent, `habitatmech:GOLD.87bf5e5370`) is missing and undefined. Requesting the child alone forces the two-clause definition at the top of this report. `curation/term_requests/needs_a_parent_first.tsv` exists in this repo for exactly this situation.

3. **Zero upstream assertion volume.** This record has **0** upstream assertions, and only 2 GOLD node ids (`8490`, `8491`) back it. By the backlog ranking `just report` produces, this sits at the very bottom. The concept is real and definable, but if a term request has a cost, this is a low-yield one — and it may be more efficient to request the parent `artificial water channel system` alone and carry `Indoor`/`Outdoor` as minted HabitatMech children of it until GOLD accumulates samples there.

### Suggested disposition for `curation/decisions.tsv`

| Field | Value |
|---|---|
| key | `habitatmech:GOLD.b4e93f5d66` |
| decision | `CONFIRM_UNGROUNDED` (unchanged) — the existing decision is correct and the ENVO:01000856 mapping-table defect it records is verified |
| optional strengthening | `GROUND_AS_PARENT` → `ENVO:00010622` *vivarium* (in slice; label verified) — makes the record's genus explicit without over-claiming |
| `relation: xref` | `ENVO:01001405` *laboratory environment* (the enclosing space); optionally `ENVO:00000121` *artificial channel* (the shape upstream lexical matching saw, without asserting landform-hood) |
| term request | Yes — but paired with the parent; see qualification 2 |

**Note text the evidence supports (all three checkable claims verified against the repo):**

> Path: `Engineered > Artificial ecosystem > Water channel system > Indoor`. GOLD's `Indoor` here is not an indoor space but an indoor experimental stream channel: its only sibling is `Outdoor`, its only child is `Biofilm`, and GOLD routes real canals to a different branch (`Engineered > Built environment > Canal`). Distinct from `Environmental > Air > Indoor Air`. No ENVO term names it; `ENVO:00000079` *flume* is the civil-engineering homonym and `ENVO:01000620` *mesocosm* is defined as embedded in a natural environment, which excludes indoor siting. Genus is `ENVO:00010622` *vivarium*. Term request, paired with its parent `Water channel system` (`habitatmech:GOLD.87bf5e5370`).

**Sources:**
- [Menczelesz, Szivák & Schmera 2019, *Hydrobiologia*](https://doi.org/10.1007/s10750-019-04093-0)
- [Mohr et al. 2005, *ESPR*](https://doi.org/10.1065/espr2004.08.217)
- [Pérez-Calpe et al. 2021, *PLoS ONE*](https://doi.org/10.1371/journal.pone.0246719)
- [Roche et al. 2017, *Water Resources Research*](https://doi.org/10.1002/2016WR019041)
- [Tromboni et al. 2026, *Limnology and Oceanography*](https://doi.org/10.1002/lno.70285)
- [Schaum, Comeau & Mullarney 2025, *Limnology and Oceanography*](https://doi.org/10.1002/lno.70265)
- [Macaulay et al. 2025, *Oikos*](https://doi.org/10.1111/oik.11020)
- [Reis & Barroso 2025, *L&O Methods*](https://doi.org/10.1002/lom3.10681)
- [Schmidt et al. 2015, *Environmental Sciences Europe*](https://doi.org/10.1186/s12302-014-0037-y)
- [Ezzat et al., glacier-fed stream biofilm flumes (PMC11705997)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11705997/)
- [Lamberti & Steinman 1993, *J-NABS*](https://doi.org/10.2307/1467618)
- [Mukherjee et al. 2025, GOLD v.10, *NAR*](https://doi.org/10.1093/nar/gkae1000)
- [Mukherjee et al. 2023, GOLD v.9, *NAR*](https://doi.org/10.1093/nar/gkac974)
- [JGI GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)
- [Buttigieg et al. 2016, ENVO, *J Biomed Semantics*](https://doi.org/10.1186/s13326-016-0097-6)
- [Glass et al. 2014, MIxS-BE, *ISME J*](https://doi.org/10.1038/ismej.2013.176)
- [Cary Institute Artificial Stream Facility](https://www.caryinstitute.org/science/research-projects/artificial-stream-facility)
- [UFZ BIOFLOW](https://www.ufz.de/index.php?en=41619)
- [EBI OLS4 (ENVO term verification)](https://www.ebi.ac.uk/ols4/ontologies/envo)

## Citations

1. https://doi.org/10.1371/journal.pone.0246719
2. https://doi.org/10.1007/s10750-019-04093-0
3. https://doi.org/10.1093/nar/gkae1000
4. https://doi.org/10.1002/lno.70285
5. https://doi.org/10.1002/lom3.10681
6. https://doi.org/10.1111/oik.11020
7. https://doi.org/10.1002/lno.70265
8. https://doi.org/10.1065/espr2004.08.217
9. https://doi.org/10.1002/2016WR019041
10. https://www.caryinstitute.org/science/research-projects/artificial-stream-facility
11. https://doi.org/10.1186/s12302-014-0037-y
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC11705997/
13. https://doi.org/10.2307/1467618
14. https://www.ufz.de/index.php?en=41619
15. https://doi.org/10.1093/nar/gkac974
16. https://doi.org/10.1093/nar/gkae162
17. https://gold.jgi.doe.gov/ecosystem_classification
18. https://www.ebi.ac.uk/ols4/api/`
19. https://doi.org/10.1186/s13326-016-0097-6
20. https://doi.org/10.1038/ismej.2013.176
21. https://www.ebi.ac.uk/ols4/ontologies/envo