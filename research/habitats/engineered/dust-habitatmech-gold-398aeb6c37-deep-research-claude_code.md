---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T21:58:31.042739'
end_time: '2026-08-17T22:06:52.868634'
duration_seconds: 501.83
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Dust
  habitat_identifier: habitatmech:GOLD.398aeb6c37
  habitat_category: ENGINEERED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Environmental > Air > Indoor Air > Dust'
  assertions: '65'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Indoor
    dust is settled particulate matter in a built environment, not air. GOLD''s Air
    branch is about where the sample came from, not what it is. (source concept habitatmech:GOLD.398aeb6c37)'
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
  num_turns: 28
  total_cost_usd: 2.983804499999999
  session_id: dfab4e2b-28b0-4663-84f5-c9661c3581ee
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 35
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Dust
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.398aeb6c37
- **Category:** ENGINEERED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Environmental > Air > Indoor Air > Dust
- **Upstream assertion volume:** 65
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Indoor dust is settled particulate matter in a built environment, not air. GOLD's Air branch is about where the sample came from, not what it is. (source concept habitatmech:GOLD.398aeb6c37)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Dust** as a microbial habitat, with citations.

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

# Dust (`habitatmech:GOLD.398aeb6c37`) — definition research

## Proposed definition

> A **dust** which settles and accumulates on interior surfaces of a built structure, and which is a heterogeneous mixture of particles shed by occupants, pets and furnishings, tracked-in soil, and deposited outdoor-derived particulate matter.

**Genus:** `ENVO:00002008` *dust* — already present in the vendored slice (`data/raw/ontology_terms.tsv`), defined as *"Particulate environmental material with diameters less than 500 micrometers."* ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002008))

**Differentia:** the built-environment setting and the mixed, non-single-source composition that setting produces.

**Recommended disposition:** this is a real habitat and should be a term. But it is **not** a case of "no ontology term fits" — the genus fits precisely; only the setting-specific child is missing. See §6, which also flags a corpus issue that matters more than the definition wording.

---

## 1. What the concept denotes

### The label is ambiguous, and the source path points both ways

GOLD's path is `Environmental > Air > Indoor Air > Dust` (`gold.ecosystem:4619`, `gold.ecosystem:4620`; 65 organism-level assertions). Two readings are live:

**(a) Settled / reservoir dust** — the layer of deposited particulate matter that accumulates on floors, carpets, elevated ledges, furniture and inside vacuum-cleaner bags in an occupied building. This is what "house dust" means in the indoor-microbiome and exposure-science literature, and it is what is sampled by vacuuming or wiping. It is the overwhelmingly dominant sample type in indoor-microbiome studies of the kind GOLD catalogues ([Barberán et al. 2015, *Proc R Soc B* 282:20151139](https://doi.org/10.1098/rspb.2015.1139); [Amend et al. 2010, *PNAS* 107:13748–13753](https://doi.org/10.1073/pnas.1000454107)).

**(b) Airborne indoor particulate matter** — dust captured *while suspended*, on a filter (active sampling) or on a passive collector such as an electrostatic dustfall collector (EDC) or open petri dish. GOLD's parent node, "Indoor Air," literally asserts this reading.

**Which reading the data means.** Three pieces of evidence favour (a):

1. GOLD maintains a *separate* leaf, `Engineered > Built environment > House > Dust` (`gold.ecosystem:5533/5534`, 7 assertions → `habitatmech:GOLD.b1230bf984`), which unambiguously means (a). Two paths for one concept is a routine GOLD artefact, not evidence of two concepts.
2. HabitatMech already assigned this record `habitat_category: ENGINEERED`, not `AIR`, unlike every one of its GOLD siblings under Indoor Air (`Cattle barn`, `Poultry farm`, `Composting facility`, `Poultry litter bioaerosol`, all `AIR`). The seeder's own category assignment already treats this leaf as a material, not an atmosphere.
3. The leaf label is "Dust", not "airborne dust" or "bioaerosol" — and GOLD does use "bioaerosol" explicitly when it means suspended material (`Poultry litter bioaerosol`).

**This is my inference, not a source statement.** I could not read GOLD's underlying study list for `gold.ecosystem:4619/4620`; that list is the only thing that would settle it definitively, and a curator with GOLD API access should check it before finalising. The existing curator note already reached reading (a) independently.

### The boundary

| Inside the concept | Neighbouring concept, outside |
|---|---|
| Floor and carpet dust, vacuum-bag dust | Indoor air itself (`ENVO:00002005`) |
| Settled dust from elevated ledges, door frames, furniture | Suspended bioaerosol / PM sampled on a filter (`ENVO:00010505`, `ENVO:01000405`, `ENVO:01000415`) |
| Mattress and upholstery dust | Building-material surfaces and their biofilms (drywall, HVAC ducting) |
| Passively-deposited dust on EDCs/petri dishes (borderline — see §5) | Outdoor / atmospheric mineral dust (`ENVO:02000100`) |
| Dust from any occupied indoor space (homes, offices, schools, dormitories) | Soil tracked in but still *outside* (`ENVO:00001998`) |

The critical boundary claim — that settled dust is **not** a proxy for indoor air — is empirically supported: EDC-collected airborne dust endotoxin correlated with active airborne sampling at *r* = 0.6–0.8, whereas **vacuumed living-room floor dust correlated poorly with active airborne sampling** ([Noss et al. 2008, *Appl Environ Microbiol* 74:5621–5627](https://doi.org/10.1128/AEM.00619-08); PMID [18676704](https://pubmed.ncbi.nlm.nih.gov/18676704/)). That is the citable evidence for the curator's note that dust "is not air."

---

## 2. Genus — the broader kind

### The genus term exists and is in the slice

`ENVO:00002008` **dust** — *"Particulate environmental material with diameters less than 500 micrometers."*

Its ancestor chain (retrieved from OLS4): `BFO:0000001 entity` → `BFO:0000002 continuant` → `BFO:0000004 independent continuant` → `BFO:0000040 material entity` → `ENVO:00010483 environmental material` → `ENVO:01000060 particulate environmental material` → `ENVO:01000814 solid environmental material` → `ENVO:00002008 dust`.

House dust is comfortably inside the ≤500 µm bound: exposure-science sieving conventions use fractions well below it (e.g. the 63 µm fraction used to predict hidden moisture damage in homes — [Reponen-group study, PMC2724515](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2724515/)), and the most readily resuspended house-dust particles are 5–25 µm ([Oomen et al. 2008, ch. 2](https://www.ncbi.nlm.nih.gov/books/NBK568957/)).

### What is missing

ENVO has **no setting-differentiated dust child**. Every existing child is differentiated by *composition or source material*:

`silica dust` (ENVO:01001282), `aluminium dust` (01001283), `barium dust` (01001284), `talc dust` (01001285), `slate dust` (01001286), `kaolin dust` (01001288), `coal dust` (02000099), `mineral dust` (02000100), `fibrous dust` (02000101), `fibrous glass dust` (02000102), `metallic dust` (02000103), `cement dust` (02000104), `clay dust` (02000105), `asbestos dust` (02000106), `grain dust` (02000107), `cotton dust` (02000108), `dust from plant parts` (02000109), `wood dust` (03510000), `rock dust` (03510036).

A full OLS4 search of ENVO for `dust` returns 41 classes, none labelled "indoor dust", "house dust", "settled dust" or "domestic dust". A search for `indoor` returns only `indoor toilet` (01000425), `indoor kitchen` (01000421), `cupboard` (01000595), `shower fixture` (01000992), `shopping mall` (03501207), `public toilet` (03501265) — all *rooms/fixtures*, no `indoor environment`, `indoor space` or `built environment` class. The 2016-11-20 ENVO release that added the dust batch (coal, cotton, grain, fibrous, mineral, asbestos, clay, cement, metallic…) added **no** setting-based dust class.

**So indoor dust would be the first ENVO dust child differentiated by *where it accumulates* rather than *what it is made of*.** A curator writing the term request should say so explicitly — it is a new differentiating axis under `dust`, not a slot-fill of the existing pattern.

### Near-misses and why each fails

| Candidate | Why it fails |
|---|---|
| `ENVO:00002005` **air** — "the mixture of gases … that surrounds the planet Earth" | A gas mixture. Dust is solid particulate matter. Grounding here would type a solid material as a gas. This is the term the GOLD *parent path* implies, and it is the wrong one. |
| `ENVO:00010505` **aerosol** — "Airborne solid particles … or liquid droplets" | Asserts suspension in a gas. Settled dust is by definition deposited, not airborne. Related-by-process, not identity. |
| `ENVO:01000405` **PM10** / `ENVO:01000415` **PM2.5** / `ENVO:01000416` **ultrafine** | Size-defined *suspended* fractions, far narrower than house dust (which spans sub-µm to hundreds of µm) and again asserting suspension. |
| `ENVO:01000060` **particulate environmental material** | The grandparent of `dust`. Too broad — admits sand, silt, sediment. |
| `ENVO:00002007` **sediment** | Definition asserts "transport and deposition of particles by flowing liquid." Indoor dust deposits from air. Different formation process. |
| `ENVO:02000100` **mineral dust**, `ENVO:03510036` **rock dust**, and all other composition-based children | Each asserts a dominant material. Indoor dust is a mixture that cuts across all of them; picking one over-claims composition. |
| `ENVO:01000417` **house**, `ENVO:01000426` **room**, `ENVO:01000313` **anthropogenic environment**, `ENVO:03600000` **cleanroom** | These are the *setting*, i.e. environmental systems / building parts. Using one as identity types the sample as a place rather than a material. They belong in the definition's differentia and, at most, as `relation: xref`. |
| `ENVO:01000595` **cupboard** | Spurious lexical hit — its *definition* mentions dust ("protect them from dust and dirt"). Not the concept. |
| `ENVO:02000090` **ash** | Relevant only to the separate BacDive "Dust-Ash" concept (§5). |

**Note on `parent_habitats` for the sibling record.** `habitatmech:GOLD.b1230bf984` (`Engineered > Built environment > House > Dust`) currently carries `ENVO:01000417 house` in `parent_habitats`. Per CLAUDE.md's rule that `parent_habitats` means *broader*, a house is not broader than dust — it is the setting. That looks like it should be `relation: xref`. Worth a separate issue.

---

## 3. Differentia — what distinguishes it

Ordered by how observable/measurable each property is.

**3.1 Physical setting (the primary differentia).** Accumulates on interior surfaces — floors, carpets, elevated ledges, door frames, upholstery, mattresses — of an enclosed, occupied, human-built structure. This is the one property that separates it from every existing ENVO dust sibling, all of which are separated by composition.

**3.2 Formation: gravitational settling plus resuspension–redeposition, from many sources at once.** House dust is *"a heterogeneous mixture of substances from numerous sources, including tracked-in or resuspended soil particles, clothing, atmospheric deposition of particulates, hair, fibres (artificial and natural), molds, pollen, allergens, bacteria, viruses, arthropods, ash, soot, animal fur and dander, smoke, skin particles, cooking and heating residues, and building components"* ([Oomen AG, Janssen PJCM, Dusseldorp A, et al. 2008, *Exposure to chemicals via house dust*, RIVM report 609021064, ch. 2 "General information on house dust"](https://www.ncbi.nlm.nih.gov/books/NBK568957/)). MeSH concurs, listing "House Dust" as an entry term of *Dust* (D004391) and defining it as *"a mixture containing fabric fibers, skin particles, animal dander, mites, bacteria, fungal spores, food particles, and cockroach parts"* ([MeSH D004391](https://meshb.nlm.nih.gov/record/ui?ui=D004391)).

**3.3 Biotic content: a reservoir/sink, not a growth substrate under normal conditions.** This is the ecologically load-bearing differentia and the reason dust is a distinct *microbial habitat* rather than a sample of air. Under typical indoor conditions dust functions as a depository integrating deposition from indoor air, occupant and pet shedding, and tracked-in soil. Active growth requires elevated moisture: Dannemiller et al. showed equilibrium relative humidity above ~80 % has a profound effect on fungal growth rates and community structure in floor dust, and that bacterial alpha diversity increased with increasing ERH; the corresponding lower ERH limits for fungal growth at 20–25 °C are 78 % on wood, 86 % on gypsum and >90 % on ceramics ([Dannemiller, Weschler & Peccia 2017, *Indoor Air* 27:354–363, doi:10.1111/ina.12313](https://doi.org/10.1111/ina.12313); PMID [27272645](https://pubmed.ncbi.nlm.nih.gov/27272645/)).

**3.4 Source apportionment differs between domains — a measurable, distinguishing signature.**
- *Fungi are dominated by outdoor air.* Indoor airborne fungal assemblages are strongly determined by dispersal from outdoors, with **no fungal taxa identifiable as indicators of indoor air**, and room and occupant behaviour had no detectable effect ([Adams, Miletto, Taylor & Bruns 2013, *ISME J* 7:1262–1273, doi:10.1038/ismej.2013.28](https://doi.org/10.1038/ismej.2013.28); PMID [23426013](https://pubmed.ncbi.nlm.nih.gov/23426013/)).
- *Bacteria are dominated by occupants and pets.* In settled dust from ~1,200 US homes, fungal communities were predicted by geography and outdoor climate, while bacterial communities were predicted by occupant characteristics — sex ratio and the presence of dogs and cats, with pet-associated taxa shed directly into the home ([Barberán et al. 2015, *Proc R Soc B* 282:20151139, doi:10.1098/rspb.2015.1139](https://doi.org/10.1098/rspb.2015.1139); PMID [26311665](https://pubmed.ncbi.nlm.nih.gov/26311665/); companion continental-scale analysis: [Barberán et al. 2015, *PNAS* 112:5756–5761, doi:10.1073/pnas.1420815112](https://doi.org/10.1073/pnas.1420815112), PMID 25902536).
- *Indoor fungal composition is geographically patterned globally.* Across 72 buildings worldwide, distance from the equator was the best predictor of phylogenetic community similarity, diversity was higher in temperate zones than the tropics, and **building function had no significant effect** ([Amend, Seifert, Samson & Bruns 2010, *PNAS* 107:13748–13753, doi:10.1073/pnas.1000454107](https://doi.org/10.1073/pnas.1000454107); PMID [20616017](https://pubmed.ncbi.nlm.nih.gov/20616017/)).

**3.5 Characteristic physicochemistry.** Room temperature (20–25 °C), low and fluctuating water activity, high organic/fibrous content, and an accumulated burden of semivolatile organics and trace metals from indoor sources — which is why house dust is used as an exposure medium at all ([Oomen et al. 2008](https://www.ncbi.nlm.nih.gov/books/NBK568957/); trace-metal context: [Rasmussen et al. 2021, *Environ Sci Technol*, doi:10.1021/acs.est.1c04494](https://pubs.acs.org/doi/10.1021/acs.est.1c04494)).

**3.6 Particle-size behaviour.** 5–25 µm particles are the most readily resuspended by walking and cleaning; 0.3–1 µm particles are unaffected by either ([Oomen et al. 2008, ch. 2](https://www.ncbi.nlm.nih.gov/books/NBK568957/)).

**3.7 Operational definition (how a sample is obtained).** Vacuum sampling of settled dust or surface wiping, then sieving; the two methods can differ in efficiency by more than a factor of 100, with wiping more reproducible on hard surfaces ([Oomen et al. 2008](https://www.ncbi.nlm.nih.gov/books/NBK568957/)). The National Academies' built-environment report lists vacuum sampling of settled dust alongside air sampling and surface swabbing, and concludes that long-term composite samples are generally the most advantageous paradigm for microbiome characterisation — the property that makes dust attractive as an integrating reservoir ([National Academies 2017, *Microbiomes of the Built Environment: A Research Agenda for Indoor Microbiology, Human Health, and Buildings*, doi:10.17226/23647](https://doi.org/10.17226/23647); [NCBI Bookshelf NBK458827](https://www.ncbi.nlm.nih.gov/books/NBK458827/); PMID 29035489).

**3.8 Illustrative magnitude of the community.** Vacuum-bag dust from Earth homes yielded 465 fungal OTUs and 237 bacterial ASVs, versus 102 and 102 respectively from the ISS — a useful anchor for how much diversity a dust sample holds and how strongly it tracks the enclosing built environment ([*Sci Rep* 2024, 14, doi:10.1038/s41598-024-62191-z](https://doi.org/10.1038/s41598-024-62191-z)).

---

## 4. Sources

**Verified by direct retrieval in this session:**
- ENVO:00002008 label, definition and full ancestor chain — [OLS4 API](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002008)
- ENVO `dust` and `indoor` search result sets (41 and 6 classes respectively) — OLS4 search API
- MeSH D004391 *Dust*, entry terms "House Dust"/"Housedust" — [meshb.nlm.nih.gov](https://meshb.nlm.nih.gov/record/ui?ui=D004391)
- Oomen AG, Janssen PJCM, Dusseldorp A, et al. (2008). *Exposure to chemicals via house dust*, ch. 2. RIVM, Bilthoven — [NCBI Bookshelf NBK568957](https://www.ncbi.nlm.nih.gov/books/NBK568957/)
- Local corpus files: `data/raw/ontology_terms.tsv`, `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/engineered/dust__f81b18c5.yaml`, `data/habitats/air/indoor_air.yaml`, `data/habitats/other/dust_ash.yaml`, `curation/decisions.tsv`

**Primary literature (DOI/PMID given; retrieved via search-result summaries of abstracts, not full-text reads in this session — a curator quoting a specific number should open the paper):**
- Adams RI, Miletto M, Taylor JW, Bruns TD (2013). *ISME J* 7:1262–1273. doi:[10.1038/ismej.2013.28](https://doi.org/10.1038/ismej.2013.28). PMID 23426013. (Erratum: *ISME J* 7:1460, doi:10.1038/ismej.2013.84.)
- Amend AS, Seifert KA, Samson RA, Bruns TD (2010). *PNAS* 107:13748–13753. doi:[10.1073/pnas.1000454107](https://doi.org/10.1073/pnas.1000454107). PMID 20616017.
- Barberán A, Dunn RR, Reich BJ, et al. (2015). *Proc R Soc B* 282:20151139. doi:[10.1098/rspb.2015.1139](https://doi.org/10.1098/rspb.2015.1139). PMID 26311665. PMC4571696.
- Barberán A, Ladau J, Leff JW, et al. (2015). *PNAS* 112:5756–5761. doi:[10.1073/pnas.1420815112](https://doi.org/10.1073/pnas.1420815112). PMID 25902536.
- Dannemiller KC, Weschler CJ, Peccia J (2017). *Indoor Air* 27:354–363. doi:[10.1111/ina.12313](https://doi.org/10.1111/ina.12313). PMID 27272645.
- Noss I, Wouters IM, Visser M, et al. (2008). "Evaluation of a low-cost electrostatic dust fall collector for indoor air endotoxin exposure assessment." *Appl Environ Microbiol* 74:5621–5627. doi:[10.1128/AEM.00619-08](https://doi.org/10.1128/AEM.00619-08). PMID 18676704.
- Adams RI, Tian Y, Taylor JW, et al. (2015). "Passive dust collectors for assessing airborne microbial material." *Microbiome* 3:46. doi:[10.1186/s40168-015-0112-7](https://doi.org/10.1186/s40168-015-0112-7). PMC4593205.
- Nevalainen A, Täubel M, Hyvärinen A (2015). "Indoor fungi: companions and contaminants." *Indoor Air* 25:125–156. doi:[10.1111/ina.12182](https://doi.org/10.1111/ina.12182).
- Fungal diversity, Earth vs ISS dust (2024). *Sci Rep* 14. doi:[10.1038/s41598-024-62191-z](https://doi.org/10.1038/s41598-024-62191-z).
- House dust microbiome review (2019). *Int Microbiol*. doi:[10.1007/s10123-019-00057-5](https://doi.org/10.1007/s10123-019-00057-5).
- "Moving beyond species: fungal function in house dust…" (2024). *Microbiome*. doi:[10.1186/s40168-024-01915-9](https://doi.org/10.1186/s40168-024-01915-9).

**Standards / reference vocabularies:**
- ENVO — [environmentontology.org](http://environmentontology.org/), [OBO Foundry entry](http://obofoundry.org/ontology/envo.html), [GitHub tracker](https://github.com/EnvironmentOntology/envo) (the venue for the term request in §6). Ontology paper: Buttigieg PL et al. (2013). *J Biomed Semantics* 4:43. [PMC3904460](https://pmc.ncbi.nlm.nih.gov/articles/PMC3904460/)
- GOLD five-level ecosystem classification: Mukherjee S, Stamatis D, Li CT, et al. (2023). "Twenty-five years of Genomes OnLine Database (GOLD)." *Nucleic Acids Res* 51(D1):D957–D963. doi:[10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974). PMID 36318257. GOLD's own documentation states the classification is distinct from ENVO, which is exactly why HabitatMech has to do this mapping.
- MeSH D004391 (above).

**Explicitly my inference, not sourced:** the resolution of the (a)/(b) ambiguity in §1; the claim that indoor dust would be ENVO's first setting-differentiated dust child (based on enumerating the 41 returned classes, not on an ENVO curator statement); the `parent_habitats` critique of the sibling record in §2; the merge recommendation in §6.

**Not checked in this session:** SNOMED CT, AGROVOC, and the MIxS built-environment package. If the curator wants cross-references from those, they need a separate lookup — I would rather leave the gap visible than assert a code I did not resolve.

---

## 5. Synonyms, and what not to conflate

### Names in real use for this concept
`indoor dust` · `house dust` · `household dust` · `domestic dust` · `settled dust` · `settled house dust` · `indoor settled dust` · `floor dust` · `carpet dust` · `reservoir dust` · `vacuum dust` · `vacuum-bag dust` · `dust fall` (when passively collected)

MeSH records "House Dust" and "Housedust" as entry terms under *Dust* ([D004391](https://meshb.nlm.nih.gov/record/ui?ui=D004391)).

### Commonly but wrongly treated as the same thing

| Not the same | Why |
|---|---|
| **Indoor air** / bioaerosol (`ENVO:00002005`, `ENVO:00010505`) | Different medium and, empirically, a different signal: floor dust endotoxin correlates poorly with active airborne sampling ([Noss et al. 2008](https://doi.org/10.1128/AEM.00619-08)). This is the exact conflation GOLD's path invites. |
| **PM2.5 / PM10 / ultrafine PM** (`ENVO:01000415`, `01000405`, `01000416`) | Regulatory size fractions of *suspended* matter. House dust spans a much wider size range and is deposited. |
| **Passively-collected dustfall (EDC / petri dish)** | Genuinely borderline: it is settled by gravity, but it is a *surrogate for airborne* material, and EDCs track airborne exposure better than reservoir dust ([Noss et al. 2008](https://doi.org/10.1128/AEM.00619-08); [Adams et al. 2015, *Microbiome* 3:46](https://doi.org/10.1186/s40168-015-0112-7)). Recommend excluding it from the term and noting the exclusion, or the term silently absorbs air samples. |
| **Atmospheric / desert mineral dust** (`ENVO:02000100`, Saharan dust plumes) | Same English word, different concept — outdoor, mineral-dominated, transported. |
| **House dust mite** (*Dermatophagoides* spp.) and its allergens (Der p 1 etc.) | An arthropod and its proteins found *in* dust; not the habitat. A frequent source of confusion because "house dust allergy" usually means mite allergy. |
| **`habitatmech:BACDIVE.4b8650dee7` "Dust-Ash"** (20 BacDive strains) | Already `CONFIRM_UNGROUNDED` in this corpus precisely because dust and ash are different materials. Do not fold it in. |
| **Cleanroom / spacecraft-assembly-facility dust** (`ENVO:03600000` cleanroom) | Indoor, but an oligotrophic, actively controlled setting with a distinct community. Would be a sibling child, not this term. |
| **Soil** (`ENVO:00001998`) and **sediment** (`ENVO:00002007`) | Tracked-in soil is a *component* of indoor dust; the whole is not soil. Sediment asserts deposition by flowing liquid. |
| **Lint, ash, soot** | Components, not the concept. |
| **The vacuum-cleaner bag** | A sample container; the habitat is its contents. |

---

## 6. Should it be a term at all? — yes, but fix two things first

**Yes, this is a habitat.** It is a material environment with a resident (largely deposited, partly growing) microbial community, sampled by a standard protocol, characterised by hundreds of studies including continental- and global-scale surveys, and carrying 65 GOLD assertions here plus 7 on the sibling path. It is not a process, quality, disease state, taxon, or sampling artefact.

**But the curator note's premise is too strong.** The recorded note says *"no ontology term fits this concept."* At the genus level a term fits exactly — `ENVO:00002008 dust`, already in the vendored slice. What is missing is only the setting-specific child. That distinction matters for what happens next:

1. **The record should carry `ENVO:00002008` as `parent_habitats` (relation: parent).** It is genuinely broader — indoor dust *is* dust. Leaving `parent_habitats` empty throws away a correct, checkable is-a link. The setting terms (`ENVO:01000417 house`, `ENVO:01000426 room`) go in `relation: xref` if wanted at all, because a house is not broader than dust. Note the sibling record `habitatmech:GOLD.b1230bf984` currently has `house` in `parent_habitats`, which looks like the same mistake in the other direction and deserves its own issue.

2. **This record and `habitatmech:GOLD.b1230bf984` are almost certainly the same concept** — `Environmental > Air > Indoor Air > Dust` (65) and `Engineered > Built environment > House > Dust` (7) both denote settled indoor dust, differing only in whether GOLD filed them under Air or Built environment. The corpus gained a mechanism for exactly this in #116/#117 ("Let a decision say two novel concepts are the same"). Using it would consolidate 72 assertions onto one concept and remove the duplicate. **Check GOLD's study lists for `gold.ecosystem:4619/4620` and `5533/5534` before merging** — that is the one thing that could falsify this.

3. **Why the record is UNGROUNDED is probably mechanical, not semantic.** Two GOLD paths end in the leaf "Dust" at equal depth (4). Per the documented ambiguity rule, ties at the shallowest depth are left unclaimed on purpose — which is exactly what produced `UNGROUNDED` here and `NARROW` on the sibling. That is the rule working, but it means "UNGROUNDED" here does not carry the evidentiary weight it would if a curator had rejected `ENVO:00002008` on the merits.

**Term-request target:** `indoor dust` in ENVO, as a child of `ENVO:00002008 dust`, with the proposed definition above, synonyms from §5, and an explicit note that it introduces a setting-based differentia under `dust` where all existing children are composition-based. Per the standing memory on external submissions, that request needs its own explicit yes before anything is filed.

**If a curator instead wants an environmental *system* rather than a material** (parallel to how host-associated cases resolve to `<X>-associated environment`), note that ENVO has no `indoor environment` or `built environment` class to hang it on — the closest are `room` (ENVO:01000426), `house` (ENVO:01000417) and `anthropogenic environment` (ENVO:01000313). I recommend against that route: GOLD's node names the sampled *material*, and `dust` gives a clean, already-existing genus.

---

## Sources

- [ENVO:00002008 in OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002008) · [ENVO home](http://environmentontology.org/) · [ENVO on OBO Foundry](http://obofoundry.org/ontology/envo.html) · [ENVO GitHub](https://github.com/EnvironmentOntology/envo) · [ENVO paper, PMC3904460](https://pmc.ncbi.nlm.nih.gov/articles/PMC3904460/)
- [MeSH D004391 "Dust" (entry terms: House Dust, Housedust)](https://meshb.nlm.nih.gov/record/ui?ui=D004391)
- [Oomen et al. 2008, *Exposure to chemicals via house dust*, ch. 2 (RIVM / NCBI Bookshelf NBK568957)](https://www.ncbi.nlm.nih.gov/books/NBK568957/)
- [National Academies 2017, *Microbiomes of the Built Environment* (doi:10.17226/23647)](https://doi.org/10.17226/23647) · [NCBI Bookshelf NBK458827](https://www.ncbi.nlm.nih.gov/books/NBK458827/) · [tools chapter NBK458828](https://www.ncbi.nlm.nih.gov/books/NBK458828/)
- [Barberán et al. 2015, *Proc R Soc B* 282:20151139](https://doi.org/10.1098/rspb.2015.1139) · [PMC4571696](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4571696/) · [PubMed 26311665](https://pubmed.ncbi.nlm.nih.gov/26311665/)
- [Barberán et al. 2015, *PNAS* 112:5756–5761](https://doi.org/10.1073/pnas.1420815112)
- [Amend et al. 2010, *PNAS* 107:13748–13753](https://doi.org/10.1073/pnas.1000454107) · [PubMed 20616017](https://pubmed.ncbi.nlm.nih.gov/20616017/)
- [Adams et al. 2013, *ISME J* 7:1262–1273](https://doi.org/10.1038/ismej.2013.28) · [PubMed 23426013](https://pubmed.ncbi.nlm.nih.gov/23426013/) · [full text](https://academic.oup.com/ismej/article/7/7/1262/7590166)
- [Dannemiller et al. 2017, *Indoor Air* 27:354–363](https://doi.org/10.1111/ina.12313) · [PubMed 27272645](https://pubmed.ncbi.nlm.nih.gov/27272645/)
- [Noss et al. 2008, *Appl Environ Microbiol* 74:5621–5627](https://doi.org/10.1128/AEM.00619-08) · [PubMed 18676704](https://pubmed.ncbi.nlm.nih.gov/18676704/)
- [Adams et al. 2015, "Passive dust collectors for assessing airborne microbial material," *Microbiome* 3:46](https://doi.org/10.1186/s40168-015-0112-7) · [PMC4593205](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4593205/)
- [Nevalainen et al. 2015, "Indoor fungi: companions and contaminants," *Indoor Air*](https://doi.org/10.1111/ina.12182)
- [Earth vs ISS dust fungal diversity, *Sci Rep* 2024](https://doi.org/10.1038/s41598-024-62191-z)
- [House dust microbiome and human health risks, *Int Microbiol* 2019](https://doi.org/10.1007/s10123-019-00057-5)
- ["Moving beyond species: fungal function in house dust," *Microbiome* 2024](https://doi.org/10.1186/s40168-024-01915-9)
- [Fungal and bacterial communities in indoor dust follow different environmental determinants, *PLOS One*](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0154131)
- [Bacterial/fungal microbiome in indoor dust vs outdoor air pilot study, PMC5015483](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5015483/)
- [Aspergillus/Eurotium/Penicillium in the 63-µm house dust fraction, PMC2724515](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2724515/)
- [Trace metal contaminants in residential indoor dust, *Environ Sci Technol* 2021](https://pubs.acs.org/doi/10.1021/acs.est.1c04494)
- [Mukherjee et al. 2023, GOLD v.9, *Nucleic Acids Res* 51:D957–D963](https://doi.org/10.1093/nar/gkac974) · [PMC9825498](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9825498/)

## Citations

1. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002008
2. https://doi.org/10.1098/rspb.2015.1139
3. https://doi.org/10.1073/pnas.1000454107
4. https://doi.org/10.1128/AEM.00619-08
5. https://pubmed.ncbi.nlm.nih.gov/18676704/
6. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2724515/
7. https://www.ncbi.nlm.nih.gov/books/NBK568957/
8. https://meshb.nlm.nih.gov/record/ui?ui=D004391
9. https://doi.org/10.1111/ina.12313
10. https://pubmed.ncbi.nlm.nih.gov/27272645/
11. https://doi.org/10.1038/ismej.2013.28
12. https://pubmed.ncbi.nlm.nih.gov/23426013/
13. https://pubmed.ncbi.nlm.nih.gov/26311665/
14. https://doi.org/10.1073/pnas.1420815112
15. https://pubmed.ncbi.nlm.nih.gov/20616017/
16. https://pubs.acs.org/doi/10.1021/acs.est.1c04494
17. https://doi.org/10.17226/23647
18. https://www.ncbi.nlm.nih.gov/books/NBK458827/
19. https://doi.org/10.1038/s41598-024-62191-z
20. https://doi.org/10.1186/s40168-015-0112-7
21. https://doi.org/10.1111/ina.12182
22. https://doi.org/10.1007/s10123-019-00057-5
23. https://doi.org/10.1186/s40168-024-01915-9
24. http://environmentontology.org/
25. http://obofoundry.org/ontology/envo.html
26. https://github.com/EnvironmentOntology/envo
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC3904460/
28. https://doi.org/10.1093/nar/gkac974
29. https://www.ncbi.nlm.nih.gov/books/NBK458828/
30. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4571696/
31. https://academic.oup.com/ismej/article/7/7/1262/7590166
32. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4593205/
33. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0154131
34. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5015483/
35. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9825498/