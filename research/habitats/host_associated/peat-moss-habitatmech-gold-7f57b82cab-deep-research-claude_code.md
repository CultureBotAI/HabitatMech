---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T01:16:41.530179'
end_time: '2026-08-18T01:24:53.797665'
duration_seconds: 492.27
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Peat moss
  habitat_identifier: habitatmech:GOLD.7f57b82cab
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Plants > Peat moss'
  assertions: '11'
  parent_terms: ENVO:01001001
  xrefs: mesh:D044003
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term mesh:D044003 'Sphagnopsida' attached as a parent. Host-taxon reversal\
    \ (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a\
    \ habitat'. That reasoning is wrong, and the corpus already contradicted it \u2014\
    \ the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia,\
    \ Mammals, Birds and Fish, which keep their own identity and a term request for\
    \ an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE\
    \ while its own child Porifera > Sponge was a term request.An organism acting\
    \ as a host IS a habitat: it is where the microbe lives, and ENVO models exactly\
    \ this at plant-associated, animal-associated and fungi-associated environment.\
    \ What is not a habitat is the TAXON TERM \u2014 a phylum is a class of organisms,\
    \ not a place \u2014 so the taxon stays an xref (#99) and the concept keeps its\
    \ own identity as a term-request candidate. NOT_APPLICABLE said the concept is\
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.7f57b82cab)"
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
  web_search_requests: 10
  num_turns: 18
  total_cost_usd: 2.3208485000000003
  session_id: dffaba9f-5939-42e7-ae70-37179ca65400
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 26
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Peat moss
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.7f57b82cab
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Plants > Peat moss
- **Upstream assertion volume:** 11
- **Nearest broader term already on the record:** ENVO:01001001
- **Cross-references upstream suggested:** mesh:D044003

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term mesh:D044003 'Sphagnopsida' attached as a parent. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.7f57b82cab)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Peat moss** as a microbial habitat, with citations.

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

I'll research this now.

# Peat moss (`habitatmech:GOLD.7f57b82cab`) — novel-term definition research

> **Proposed definition**
>
> **A plant-associated environment which is determined by a living peat moss (*Sphagnum*) gametophore, comprising the surfaces of its stem and phyllids together with the water-filled lumina of its hyaline cells and the capillary spaces between them.**

If the curator wants the characteristic physicochemistry inside the definition rather than in a comment, the minimal extension is `… and characterised by acidic (pH ≈ 3–4.5), nutrient-poor, water-saturated conditions.` I would keep that in `comments`/`environmental_context` instead — it is a property of the typical bog setting, not a necessary condition of the host association (Section 3.5 explains why).

---

## 1. What the concept denotes

**Reading the source path.** `Host-associated > Plants > Peat moss` places this under GOLD's *Host-associated* ecosystem category, whose defining property is that the sample is taken **from an organism**, not from a soil, sediment or water body. The parent node is `Plants`. So the data means: *a sample of microbial life taken from a peat-moss plant* — surface-attached and internal microbiota of *Sphagnum* shoots — not a sample of the bog around them. Eleven assertions are consistent with the small published literature that isolates or sequences directly from washed or surface-sterilised *Sphagnum* tissue.

**The physical thing sampled.** A *Sphagnum* gametophore (the leafy shoot; there is no root and the sporophyte generation is ephemeral). Its distinguishing anatomy is what makes it a habitat rather than merely a surface: *Sphagnum* phyllids are a single cell layer built of two alternating cell types — narrow living photosynthetic **chlorophyllose cells** and large, dead, pore-bearing **hyaline cells (hyalocysts)** that fill with water and hold it by capillarity. Microbes colonise both the external surface (phyllosphere) and, endophytically, the hyalocyst lumina. Kostka et al. describe the microbiome as intimately associated "both within tissues and on plant surfaces" ([Kostka et al. 2016, *New Phytologist* 211:57–64, doi:10.1111/nph.13993](https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.13993); [PMID 27173909](https://pubmed.ncbi.nlm.nih.gov/27173909/)); confocal microscopy of *S. magellanicum* and *S. fallax* leaves showed dense bacterial colonisation of the internal gametophyte space, with Alphaproteobacteria up to ~50% of detected colonies ([Bragina et al. 2012, *ISME J* 6:802–813, doi:10.1038/ismej.2011.151](https://www.nature.com/articles/ismej2011151); [PMC3309359](https://pmc.ncbi.nlm.nih.gov/articles/PMC3309359)).

**Boundary — what is inside the concept.**

| Inside | Outside (neighbouring concept) |
|---|---|
| Living *Sphagnum* shoot surfaces (phyllosphere) | Bog porewater and surface peat around the shoot |
| Hyaline-cell lumina and internal shoot spaces (endosphere) | Decomposed *Sphagnum* peat / horticultural "peat moss" → `ENVO:00005774` peat soil |
| Capillary water held between phyllids and branches | The *Sphagnum* bog as an ecosystem → `ENVO:00002268` sphagnum bog |
| Green capitulum and the still-recognisable moss shoot below it | The taxon *Sphagnum* / Sphagnopsida as a class of organisms → xref only |

The boundary that is genuinely fuzzy is the **bottom of the shoot**: a *Sphagnum* stem grades continuously from living capitulum into senescing tissue into peat, and published sampling protocols cut this arbitrarily — the 2025 phyllosphere study sampled "the top green portions (0–3 cm from the shoot tip)" ([Yin et al. 2025, *ISME Communications* 5:ycaf221, doi:10.1093/ismeco/ycaf221](https://academic.oup.com/ismecommun/article/5/1/ycaf221/8342222)). *This is my inference from the sampling protocols, not a statement any source makes about the concept's extension:* the defensible line is "living/recognisable moss shoot", and everything below it belongs to peat.

**Ambiguity.** The label "peat moss" has two readings in wide use, and they are not the same material:

1. **The living plant** — *Sphagnum* moss growing on the bog surface. This is what the GOLD path means.
2. **The horticultural commodity** — dead, partially decomposed, milled *Sphagnum* peat, sold as "sphagnum peat moss" and used as a growing medium and soil amendment ([Gardening Know How, "Sphagnum Moss vs. Sphagnum Peat Moss"](https://www.gardeningknowhow.com/garden-how-to/soil-fertilizers/sphagnum-moss-vs-sphagnum-peat-moss.htm)).

The two differ in biological state (living fibrous plant vs. soil-like decayed deposit), harvest depth, and pH. **Do not pick reading 2**: it is a material/soil, would sit under peat soil rather than a host-associated environment, and would contradict the `Host-associated > Plants` path that is the strongest evidence available. Flag reading 2 in the record's comments so a future curator does not merge a horticultural-substrate record into this one.

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001001` plant-associated environment** — *"An environmental system determined by a green plant."* This is exactly the claim being made: a *Sphagnum* gametophore is a green plant (Viridiplantae, Bryophyta), and the habitat is the environmental system it determines. It is already the record's nearest broader term, and it is the same genus the corpus uses for the animal- and fungus-side cases (`ENVO:01001002`, `ENVO:01001041`). Verified against ENVO via OLS on 2026-08-18.

**Competing genus worth recording: `ENVO:01001057` "environment associated with a plant part or small plant"** — *"An environmental system determined by part of a living or dead plant, or a whole small plant."* A *Sphagnum* shoot is literally a whole small plant, so this reads as a tighter fit. Two reasons I do **not** recommend it as the genus: it is asserted in ENVO as a child of `ENVO:01001110` ecosystem rather than of `ENVO:01001001` (checked via OLS), so using it would place the record in a different branch from the animal/fungal host-associated records; and its "or dead plant" clause covers the peat reading this definition is trying to exclude. Record it as a **related near-miss**, not the parent.

### Near-misses in ENVO and why each fails

| Term | Why it is not a match |
|---|---|
| `ENVO:00002268` **sphagnum bog** — "A peatland dominated by species of the Bryophyte Sphagnum" | Wrong entity type and wrong scale: a peatland ecosystem, not the plant. Grounding here would place samples of moss tissue in the same class as samples of bog water. This is the term most likely to be grabbed by lexical matching, and it is the single most important thing to *not* ground to. |
| `ENVO:00005774` **peat soil** ("A histosol which is formed by the decomposition of vegetation or organic matter"; syn. *turf*) | The dead decomposed product — reading 2 above. Asserts decomposition, which the living-moss reading denies. |
| `ENVO:00000044` **peatland** (syns. include *bog*, *peat bog*, *mire*, *muskeg*) | A wetland ecosystem. Far broader and again the wrong entity type. |
| `ENVO:01000890` **area of moss-dominated vegetation** | A vegetated area defined by NLCD 2011 cover thresholds (≥80% moss) with an "Alaska only" intent noted in its definition. Asserts landscape-scale cover and a geographic scope the sources do not; also not moss-specific to *Sphagnum*. |
| `ENVO:00002243` **histosol**, `ENVO:00000511` blanket bog, `ENVO:00000185` raised mire, `ENVO:00000187` tundra mire | All soil or ecosystem classes; same category error. |
| `PO:0030018` **gametophore** (the leafy gametophyte); `PO:0025075` **non-vascular leaf** (syns. *phyllid*, *gametophyll*) | Anatomical entities, not environments — PO models the plant, not the place. `PO:0025075` is also narrower (one phyllid, not the shoot). Useful as anatomical *xrefs* if the record wants to pin what is being colonised. |
| `mesh:D044003` **Sphagnopsida** (entry terms: *Peat Moss*, *Mosses, Peat*, *Moss, Sphagnum*, *Sphagnum*) — verified at [id.nlm.nih.gov/mesh/D044003](https://id.nlm.nih.gov/mesh/D044003) | A taxonomic class of organisms, not a place — the exact case CLAUDE.md's #99/#114 rule covers. Keep as `relation: xref`. Note it is also *slightly broader* than "peat moss" strictly construed: Sphagnopsida contains *Sphagnum* (`NCBITaxon:13804`) plus the small segregate genera. |
| `PO` hyaline-cell / hyalocyst / chlorophyllose-cell terms | **Do not exist** — searched PO via OLS, no hits. There is no ontology term for the specific cell type that makes this a habitat. |

**Conclusion: nothing in ENVO, UBERON, FOODON, BTO or PO names this concept.** The UNGROUNDED disposition and the term request are correct.

---

## 3. Differentia — what separates it from siblings under *plant-associated environment*

### 3.1 The host is a bryophyte with no roots and no vasculature
Unlike every vascular-plant sibling (rhizosphere, phyllosphere of a tracheophyte, root endosphere), there is no root/shoot compartmentalisation to sample. *Sphagnum* is a genus of c. 350 species found on every continent except Antarctica ([Keane et al. 2025, *New Phytologist*, doi:10.1111/nph.70361](https://pmc.ncbi.nlm.nih.gov/articles/PMC12329207/); [Turetsky et al. 2025, *New Phytologist* 247:1608–1621, doi:10.1111/nph.70233](https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.70233)). The photosynthetic gametophyte, not the sporophyte, is the persistent generation — Bragina et al. make this contrast with higher plants explicitly.

### 3.2 The hyaline cell is the defining habitat structure — an internal, water-filled, dead-cell compartment
This is the strongest differentia and the one no sibling shares. Most of the leaf volume is empty, pore-bearing hyaline cells, giving microorganisms expanded surface area, stable hydration and a protected interior; the hyalocysts have been described as a "hot spot of plant–microbe interaction" functioning as a rhizosphere analogue in a plant with no roots ([Kostka et al. 2016](https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.13993); [Kolton et al. 2022, *mBio* 13:e03714-21, doi:10.1128/mbio.03714-21](https://journals.asm.org/doi/10.1128/mbio.03714-21), [PMC8863050](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8863050/)). Methanotrophs, phototrophs and diazotrophs have all been localised *inside* the non-photosynthetic hyaline cells. Kolton et al. also report that arabinosylated β-galactans are enriched in hyaline cell walls relative to chlorophyllose cells, matching the arabinose-degrading capacity of *Sphagnum*-isolated heterotrophs (*Granulicella*, *Bryobacter*, *Acidisoma*) — i.e. the compartment supplies a distinctive carbon substrate.

### 3.3 A distinct, deterministically-assembled community, not a sample of the surrounding bog
This is what makes it a habitat in its own right rather than a sampling artefact of bog peat. *Sphagnum* communities are "significantly distinct from [the] surrounding environment", with assembly primarily driven by deterministic processes, in contrast to the stochastic assembly of adjacent litter and soil layers; the host-specific core accounted for 57.5% of ASVs and 72.2% of total abundance ([Yin et al. 2025](https://academic.oup.com/ismecommun/article/5/1/ycaf221/8342222)). Raghoebarsing et al. established the same point functionally two decades earlier: bog-water controls showed no methane oxidation, so the methanotrophy was plant-associated, not a property of the water ([Raghoebarsing et al. 2005, *Nature* 436:1153–1156, doi:10.1038/nature03802](https://www.nature.com/articles/nature03802); [PMID 16121180](https://pubmed.ncbi.nlm.nih.gov/16121180/)).

### 3.4 A characteristic functional signature: coupled methanotrophy and diazotrophy
- Partly endophytic methanotrophs oxidise CH₄ to CO₂ that *Sphagnum* re-fixes photosynthetically ([Raghoebarsing et al. 2005](https://www.nature.com/articles/nature03802)); the association is globally prevalent, not a Dutch peculiarity ([Kip et al. 2010, *Nature Geoscience* 3:617–621, doi:10.1038/ngeo939](https://www.nature.com/articles/ngeo939)).
- Acidophilic methanotrophs have been isolated directly from *Sphagnum* mosses ([Kip et al. 2011, *Appl Environ Microbiol* 77:5643–5654, doi:10.1128/AEM.05017-11](https://journals.asm.org/doi/10.1128/aem.05017-11)).
- Continental-scale core: 12 bacterial genera; N₂-fixing populations ≈15% of prokaryotic communities, dominated by Nostocales cyanobacteria and Rhizobiales methanotrophs, with obligate methanotrophic *Methyloferula* accounting for one quarter of transcribed *nifH*; dual ¹³CH₄/¹⁵N₂ tracing confirmed coupled incorporation ([Kolton et al. 2022](https://journals.asm.org/doi/10.1128/mbio.03714-21)).
- Contribution to host budget: methanotrophic and N₂-fixing bacteria may supply up to 20–30% of *Sphagnum* carbon and nitrogen respectively ([Kostka et al. 2016](https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.13993)).

### 3.5 Physicochemistry: acidic, oligotrophic, water-saturated — a typical, not a necessary, condition
*Sphagnum* is an ecosystem engineer that acidifies its own surroundings: unesterified polyuronic (galacturonic) acid residues of the cell-wall polysaccharide **sphagnan** exchange bound H⁺ for base cations, and *Sphagnum* additionally releases organic acids; bog pH typically runs ~3.0–4.5. Note a real dispute here — Hájek et al. found substantial and broadly similar cation-exchange capacity across bryophytes including brown mosses, refuting living-*Sphagnum* CEC as *the* cause of peatland acidification, while still finding *Sphagnum*'s acidification capacity several times higher ([Hájek et al. 2011, *New Phytologist*, PMID 20957965](https://www.ncbi.nlm.nih.gov/pubmed/20957965); see also [Ellis & Rochefort / cation-exchange and anoxic peat decay, doi:10.1016/S0038-0717(03)00286-4](https://www.sciencedirect.com/science/article/abs/pii/S0038071703002864)). **Because the mechanism is contested, keep the pH claim out of the necessary-and-sufficient definition and put it in a comment.** Note also that community structure tracks pH and nutrient status rather than geography, and differs sharply between congeners — *S. magellanicum* (ombrotrophic, strongly acidic) was dominated by Gammaproteobacteria while *S. fallax* (mesotrophic, weakly acidic) by Verrucomicrobia and Planctomycetes ([Bragina et al. 2012](https://www.nature.com/articles/ismej2011151); [Bragina et al. 2014, *Mol Ecol* 23:4498–4510](https://www.nature.com/articles/ismej2011151)).

### 3.6 Ecosystem stakes (context, not differentia)
Peatlands cover roughly 3–4% of land surface but hold up to about one third of the world's soil carbon — twice that of the world's forests ([UNEP, *Global Peatlands Assessment*, 2022](https://www.unep.org/resources/global-peatlands-assessment-2022)). Boreal/northern-only estimates are lower (~25–30%); cite the range, not the headline number alone.

---

## 4. Sources

Primary and review literature (all verified this session):

| Claim | Source |
|---|---|
| Microbiome present both within tissues and on surfaces; up to 20–30% of C and N from symbionts; most of microbiome uncultivated | Kostka JE, Weston DJ, Glass JB, Lilleskov EA, Shaw AJ, Turetsky MR (2016) *New Phytologist* 211(1):57–64. [doi:10.1111/nph.13993](https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.13993) · PMID 27173909 |
| Endophytic methanotrophs oxidise CH₄ → CO₂ used in host photosynthesis; bog-water controls negative | Raghoebarsing AA et al. (2005) *Nature* 436(7054):1153–1156. [doi:10.1038/nature03802](https://www.nature.com/articles/nature03802) · PMID 16121180 |
| Global prevalence of symbiotic methane oxidation in peat-moss ecosystems | Kip N et al. (2010) *Nature Geoscience* 3:617–621. [doi:10.1038/ngeo939](https://www.nature.com/articles/ngeo939) |
| Acidophilic methanotrophs isolated from *Sphagnum* | Kip N et al. (2011) *Appl Environ Microbiol* 77(16):5643–5654. [doi:10.1128/AEM.05017-11](https://journals.asm.org/doi/10.1128/aem.05017-11) |
| Host-species-specific communities; internal colonisation imaged; 12 core genera / diazotrophic methanotrophy | Bragina A et al. (2012) *ISME J* 6(4):802–813, [doi:10.1038/ismej.2011.151](https://www.nature.com/articles/ismej2011151) · [PMC3309359](https://pmc.ncbi.nlm.nih.gov/articles/PMC3309359) — and Kolton M et al. (2022) *mBio* 13(1):e03714-21, [doi:10.1128/mbio.03714-21](https://journals.asm.org/doi/10.1128/mbio.03714-21) · [PMC8863050](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8863050/) |
| *Sphagnum* community distinct from surrounding litter/soil; deterministic assembly; host-specific core = 72.2% of abundance; 0–3 cm capitulum sampling | Yin X, Ang LP, Zhu R-L et al. (2025) *ISME Communications* 5(1):ycaf221. [doi:10.1093/ismeco/ycaf221](https://academic.oup.com/ismecommun/article/5/1/ycaf221/8342222) |
| c. 350 species; hummock vs. hollow decomposition contrast; genus as eco-evolutionary system | Turetsky MR et al. (2025) *New Phytologist* 247(4):1608–1621, [doi:10.1111/nph.70233](https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.70233) · PMID 40452151; Keane JB et al. (2025) *New Phytologist*, [doi:10.1111/nph.70361](https://pmc.ncbi.nlm.nih.gov/articles/PMC12329207/) |
| Cation exchange / sphagnan acidification, and the challenge to it | Hájek T et al. (2011) *New Phytologist*, [PMID 20957965](https://www.ncbi.nlm.nih.gov/pubmed/20957965); [doi:10.1016/S0038-0717(03)00286-4](https://www.sciencedirect.com/science/article/abs/pii/S0038071703002864) |
| Endophyte structure varies by *Sphagnum* species and nutrient type; water-holding capacity a driver | [*Microbial Ecology* (2024), doi:10.1007/s00248-024-02355-6](https://link.springer.com/article/10.1007/s00248-024-02355-6) |
| Warming alters *Sphagnum* microbiome / habitat-adapted communities mediate resilience | [PMC9310625](https://pmc.ncbi.nlm.nih.gov/articles/PMC9310625/) |
| Peatland carbon share (~3–4% of land, up to ⅓ of soil carbon) | [UNEP Global Peatlands Assessment 2022](https://www.unep.org/resources/global-peatlands-assessment-2022) |
| MeSH D044003 = Sphagnopsida, entry terms incl. "Peat Moss" | [id.nlm.nih.gov/mesh/D044003](https://id.nlm.nih.gov/mesh/D044003) (NLM lookup API, retrieved 2026-08-18) |
| ENVO/PO/NCBITaxon term labels, definitions, and hierarchy | EBI OLS4 API, retrieved 2026-08-18: [ENVO:01001001](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001001), [ENVO:01001057](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001057), [ENVO:00002268](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002268), [PO:0030018](https://www.ebi.ac.uk/ols4/ontologies/po/classes?obo_id=PO:0030018), [NCBITaxon:13804](https://www.ebi.ac.uk/ols4/ontologies/ncbitaxon/classes?obo_id=NCBITaxon:13804) |
| Living *Sphagnum* vs. horticultural sphagnum peat distinction | [Gardening Know How](https://www.gardeningknowhow.com/garden-how-to/soil-fertilizers/sphagnum-moss-vs-sphagnum-peat-moss.htm) — trade/horticultural usage, **not** a scientific source; cite only for the existence of the naming ambiguity, not for any biological claim |

**Explicitly my inference, not sourced:** (a) that the concept's lower boundary should be drawn at "living/recognisable moss shoot" rather than at any measured depth — sampling protocols vary and no source defines the term's extension; (b) that `ENVO:01001001` rather than `ENVO:01001057` is the right genus — that is a modelling judgement about branch consistency, not an ENVO assertion; (c) the mapping of individual near-misses to specific failure reasons in the Section 2 table.

---

## 5. Synonyms and what NOT to conflate

**Names in real use for this concept**
- peat moss (the living plant)
- *Sphagnum*, *Sphagnum* moss, sphagnum
- bog moss
- *Sphagnum* gametophore / *Sphagnum* shoot (technical)
- *Sphagnum* phyllosphere (narrower — surface compartment only)
- *Sphagnum* endosphere / hyaline-cell habitat (narrower — internal compartment only)
- MeSH entry terms mapping to the same string: *Peat Moss*, *Mosses, Peat*, *Moss, Sphagnum*, *Sphagnum* → all under Sphagnopsida

**Commonly but wrongly treated as the same thing**
1. **Horticultural "sphagnum peat moss" / peat** — dead, decomposed bog deposit sold as growing medium. Different material, different pH, different entity type → `ENVO:00005774` peat soil.
2. **Sphagnum bog / peat bog / peatland** — the ecosystem the moss builds, not the moss. `ENVO:00002268`, `ENVO:00000044`. Note `ENVO:00000044` carries *bog*, *peat bog*, *mire*, *muskeg* as synonyms, so lexical matching on "peat" will pull it in wrongly.
3. **Peat porewater / surface peat / acrotelm** — the surrounding medium. Functionally distinguished from the moss by both Raghoebarsing (2005) and Yin (2025).
4. **Sphagnopsida / *Sphagnum* the taxon** (`mesh:D044003`, `NCBITaxon:13804`) — a class of organisms, not a place. Per the repo's #99/#114 rule, this stays `relation: xref`; it is also marginally broader than *Sphagnum* alone.
5. **Brown mosses** (Amblystegiaceae, fen-dwelling) and other bryophytes — a genuinely different host with a different associated community; "moss-associated" is broader than "peat-moss-associated".
6. **Area of moss-dominated vegetation** (`ENVO:01000890`) — a landcover class, not a host.
7. **The plant anatomy terms** `PO:0030018` gametophore and `PO:0025075` non-vascular leaf — what is colonised, not the environment. Fine as anatomical xrefs; wrong as identity.

---

## 6. Should it be a term at all?

**Yes — request the term.** This is a bona fide host-associated microbial habitat and the strongest possible case for the #114 reversal, not a marginal one:

- It is a **place where microbes live**, with a physically delimited internal compartment (hyaline-cell lumina) that has been imaged and sampled, not merely a taxonomic label.
- Its community is **demonstrably distinct from the surrounding environment** and deterministically assembled ([Yin et al. 2025](https://academic.oup.com/ismecommun/article/5/1/ycaf221/8342222)) — so it is not a sampling artefact of bog peat.
- It has a **reproducible core microbiome** defined at continental scale across 17 sites and 18 *Sphagnum* species ([Kolton et al. 2022](https://journals.asm.org/doi/10.1128/mbio.03714-21)) — so it is not a one-lab curiosity.
- It has **host-specific functional traits** (in-plant CH₄ oxidation feeding host photosynthesis, coupled N₂ fixation) that no surrounding-environment term would capture.

It is not a process, a quality, a disease state or a procedure. `NOT_APPLICABLE` would be wrong for exactly the reason the curator's note gives. The correct disposition is the one on the record: **`CONFIRM_UNGROUNDED`, taxon (`mesh:D044003` / optionally `NCBITaxon:13804`) as `relation: xref`, `ENVO:01001001` as parent, term request for a *Sphagnum*-associated (peat-moss-associated) environment.**

Two things worth adding to the record while it is open:
- an **anatomical xref** to `PO:0030018` gametophore, which pins the colonised structure without asserting it *is* the habitat;
- a **comment recording the horticultural-peat ambiguity**, so a later merge does not silently absorb a peat-substrate record into this one.

Sources: [Kostka 2016](https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.13993) · [Raghoebarsing 2005](https://www.nature.com/articles/nature03802) · [Kip 2010](https://www.nature.com/articles/ngeo939) · [Kip 2011](https://journals.asm.org/doi/10.1128/aem.05017-11) · [Bragina 2012](https://www.nature.com/articles/ismej2011151) · [Kolton 2022](https://journals.asm.org/doi/10.1128/mbio.03714-21) · [Yin 2025](https://academic.oup.com/ismecommun/article/5/1/ycaf221/8342222) · [Turetsky 2025](https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.70233) · [Keane 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12329207/) · [Hájek 2011](https://www.ncbi.nlm.nih.gov/pubmed/20957965) · [Microbial Ecology 2024](https://link.springer.com/article/10.1007/s00248-024-02355-6) · [Warming/resilience, PMC9310625](https://pmc.ncbi.nlm.nih.gov/articles/PMC9310625/) · [UNEP 2022](https://www.unep.org/resources/global-peatlands-assessment-2022) · [MeSH D044003](https://id.nlm.nih.gov/mesh/D044003) · [EBI OLS4](https://www.ebi.ac.uk/ols4/) · [Gardening Know How (usage only)](https://www.gardeningknowhow.com/garden-how-to/soil-fertilizers/sphagnum-moss-vs-sphagnum-peat-moss.htm)

## Citations

1. https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.13993
2. https://pubmed.ncbi.nlm.nih.gov/27173909/
3. https://www.nature.com/articles/ismej2011151
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC3309359
5. https://academic.oup.com/ismecommun/article/5/1/ycaf221/8342222
6. https://www.gardeningknowhow.com/garden-how-to/soil-fertilizers/sphagnum-moss-vs-sphagnum-peat-moss.htm
7. https://id.nlm.nih.gov/mesh/D044003
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC12329207/
9. https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.70233
10. https://journals.asm.org/doi/10.1128/mbio.03714-21
11. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8863050/
12. https://www.nature.com/articles/nature03802
13. https://pubmed.ncbi.nlm.nih.gov/16121180/
14. https://www.nature.com/articles/ngeo939
15. https://journals.asm.org/doi/10.1128/aem.05017-11
16. https://www.ncbi.nlm.nih.gov/pubmed/20957965
17. https://www.sciencedirect.com/science/article/abs/pii/S0038071703002864
18. https://www.unep.org/resources/global-peatlands-assessment-2022
19. https://link.springer.com/article/10.1007/s00248-024-02355-6
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC9310625/
21. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001001
22. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001057
23. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002268
24. https://www.ebi.ac.uk/ols4/ontologies/po/classes?obo_id=PO:0030018
25. https://www.ebi.ac.uk/ols4/ontologies/ncbitaxon/classes?obo_id=NCBITaxon:13804
26. https://www.ebi.ac.uk/ols4/