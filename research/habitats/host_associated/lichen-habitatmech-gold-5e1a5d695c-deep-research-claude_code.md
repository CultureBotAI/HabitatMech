---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T21:49:00.456636'
end_time: '2026-08-17T21:58:54.851117'
duration_seconds: 594.39
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Lichen
  habitat_identifier: habitatmech:GOLD.5e1a5d695c
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Fungi > Lichen'
  assertions: '66'
  parent_terms: (none)
  xrefs: FOODON:03412345
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term FOODON:03412345 'lichen' attached as a parent. Organism-identity\
    \ screen (#109): grounded EXACT to FOODON:03412345 'lichen', which is a composite\
    \ organism arising from algae or cyanobacteria living among fungal filaments \u2014\
    \ an organism, not a place. The screen that exists to catch exactly this reported\
    \ 0 for months because it tested only NCIT and mesh ancestry and only the record's\
    \ identity; widening it to UBERON:0000468 and to parent_habitats surfaced this\
    \ family. The GOLD path says host-associated, so the concept is the environment\
    \ the organism provides, which is the same family as the sponge, nematode and\
    \ reptile term requests. The organism term is kept as an xref (#99) rather than\
    \ an identity. (source concept habitatmech:GOLD.5e1a5d695c)"
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
  num_turns: 35
  total_cost_usd: 3.4302785000000005
  session_id: f1bde2ca-1afd-4303-b148-5c094d3e6712
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 33
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Lichen
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.5e1a5d695c
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Fungi > Lichen
- **Upstream assertion volume:** 66
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** FOODON:03412345

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term FOODON:03412345 'lichen' attached as a parent. Organism-identity screen (#109): grounded EXACT to FOODON:03412345 'lichen', which is a composite organism arising from algae or cyanobacteria living among fungal filaments — an organism, not a place. The screen that exists to catch exactly this reported 0 for months because it tested only NCIT and mesh ancestry and only the record's identity; widening it to UBERON:0000468 and to parent_habitats surfaced this family. The GOLD path says host-associated, so the concept is the environment the organism provides, which is the same family as the sponge, nematode and reptile term requests. The organism term is kept as an xref (#99) rather than an identity. (source concept habitatmech:GOLD.5e1a5d695c)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Lichen** as a microbial habitat, with citations.

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

# Lichen (habitatmech:GOLD.5e1a5d695c) — definition research

> **A fungi-associated environment which is determined by a lichen thallus, the stratified poikilohydric body formed by a lichen-forming fungus in symbiosis with green-algal and/or cyanobacterial photobionts.**

Genus: `ENVO:01001041` *fungi-associated environment* — "An environmental system determined by a fungal structure." It is already in this repo's vendored slice (`data/raw/ontology_terms.tsv`, `directly_referenced TRUE`), and it has no children, so nothing narrower competes.

If a curator judges that calling a lichen thallus "a fungal structure" over-claims (see §2.3), the fallback genus is `ENVO:01001000` *environmental system determined by an organism*, giving: *An environmental system determined by an organism which is a lichen thallus, …*. I recommend the fungi-associated form, because GOLD itself files this concept under Fungi and because the nomenclatural convention treats a lichen's name as the fungus's name (§2.2).

---

## 1. What the concept denotes

**The sampled thing is a lichen thallus** — the whole macroscopic body of a lichen symbiosis, collected from its substrate (bark, rock, soil, wood) and processed as the sample matrix. It is *not* the substrate, and it is *not* the mycobiont as a cultured organism.

The GOLD path is decisive on the reading: `Host-associated > Fungi > Lichen`, 66 organism-level assertions across three GOLD node ids (`gold.ecosystem:4410|4411|4412`). GOLD's top-level `Host-associated` means the sample came from within or on a living host, and the Ecosystem Category `Fungi` names that host ([Mukherjee et al. 2023, *Nucleic Acids Research* 51:D957–D963, doi:10.1093/nar/gkac974](https://academic.oup.com/nar/article/51/D1/D957/6786204); [GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)). So the concept is *the environment a lichen provides to microorganisms*, in the same family as the sponge / nematode / reptile term requests already in this corpus.

**What is inside the boundary.** The thallus is anatomically stratified and each layer is a distinct microbial microhabitat; a sample of "lichen" normally includes all of them:

- **upper cortex** — compacted mycobiont hyphae, UV-filtering, often pigmented; the principal colonised surface, and the layer in which cystobasidiomycete yeasts sit ([Spribille et al. 2016, *Science* 353:488–492, doi:10.1126/science.aaf8287](https://www.science.org/doi/10.1126/science.aaf8287))
- **photobiont layer** — algal or cyanobacterial cells individually ensheathed by hyphae
- **medulla** — loose hyphae, air spaces, water reservoir
- **lower cortex and rhizines** — attachment surface, and the lichen–substrate interface
- **internal cavities** — e.g. the hollow podetia of *Cladonia*, whose inner wall carries the densest biofilm-like bacterial coat ([Cardinale et al. 2008, 2012b, reviewed in Grimm et al. 2021](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2021.623839/full))
- **cephalodia** — gall-like compartments confining a second (usually *Nostoc*) photobiont in tripartite thalli, and the site of thallus N₂ fixation ([Cephalodium overview](https://en.wikipedia.org/wiki/Cephalodium); *Peltigera*/*Nostoc* diazotrophy: [Darnajoux et al. 2014, *European Journal of Phycology* 49:1, doi:10.1080/09670262.2013.873143](https://www.tandfonline.com/doi/full/10.1080/09670262.2013.873143))

**What is a neighbouring concept, not this one:** the rock, bark or soil the thallus grows on; the free-living photobiont; a lichen-dominated landcover unit; and dead/harvested lichen biomass (see §5).

**No material ambiguity in this data.** The English word *lichen* is heavily overloaded in clinical vocabularies (§5), but the GOLD path removes that reading entirely.

---

## 2. Genus — the broader kind

### 2.1 The ENVO terms that exist

| CURIE | Label | ENVO definition | Verdict |
|---|---|---|---|
| `ENVO:01001041` | fungi-associated environment | "An environmental system determined by a fungal structure." Synonyms: *fungus environment*, *fungus-associated environment* | **Best genus.** Parent: `ENVO:01001000`. No children — nothing narrower to lose to. |
| `ENVO:01001000` | environmental system determined by an organism | "An environmental system which is determined by a living organism." Children: plant-, animal-, fungi-associated environment | Correct but one step too broad; use only as a fallback. |
| `ENVO:01001058` | environment associated with a fungal tissue | "An environmental system determined by part of a living or dead fungus." | **Near-miss.** A whole thallus is not a *part* of a fungus. This is the right genus for the GOLD siblings *Mycelium*, *Fruiting body*, *Spore*, not for *Lichen*. |
| `ENVO:03600084` | lichen material | "An organic material which is derived from lichen mats." Parent: `ENVO:01000155` organic material | **Near-miss, and the most tempting wrong answer.** It is an *environmental material*, not an environmental system, and "derived from" describes detached biomass rather than a living thallus that a microbe inhabits. Grounding here would silently reclassify a host-associated environment as a material. |
| `ENVO:01000889` | area of lichen-dominated vegetation | landcover unit, ≥80 % lichen cover (NLCD 2011) | Wrong scale — a landscape polygon, not a thallus. |
| `ENVO:01000949` | lichen woodland | woodland with lichen-mat understory | Wrong scale, and asserts trees. |

Search of ENVO for `lichen`, `thallus`, `fungus`, `associated environment` (OLS4, August 2026) returns nothing closer. There is **no** `lichen-associated environment` in ENVO, which is why this record is UNGROUNDED.

### 2.2 Why "fungi-associated" is defensible for a composite organism

Two independent supports:

1. **Nomenclature.** Article F.1.1 of the *International Code of Nomenclature for algae, fungi, and plants* states: "For nomenclatural purposes, names given to lichens apply to their fungal component." The lichen association as such has no name; the name on a specimen is the lichen-forming fungus's name ([IAPT, Art. F.1](https://www.iapt-taxon.org/nomen/pages/main/art_f1.html); [May et al. 2019, Chapter F, *IMA Fungus* 10:21, doi:10.1186/s43008-019-0019-1](https://imafungus.biomedcentral.com/articles/10.1186/s43008-019-0019-1)).
2. **Construction.** The thallus is built by the mycobiont: cortices, medulla, rhizines and cephalodia are all mycobiont hyphal tissue, which ensheathes the photobiont cells. Even the "lichen as ecosystem" redefinition keeps the fungus as the structuring partner, calling it the *exhabitant fungus* ([Hawksworth & Grube 2020, *New Phytologist* 227:1281–1283, doi:10.1111/nph.16630](https://nph.onlinelibrary.wiley.com/doi/full/10.1111/nph.16630)).

### 2.3 The honest counter-argument, recorded

Hawksworth & Grube's proposed definition is: *"A lichen is a self-sustaining ecosystem formed by the interaction of an exhabitant fungus and an extracellular arrangement of one or more photosynthetic partners and an indeterminate number of other microscopic organisms"* (doi:10.1111/nph.16630). Sanders pushed back — *The disadvantages of current proposals to redefine lichens*, [*New Phytologist* 241:969–971, doi:10.1111/nph.19321](https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.19321) — objecting that "ecosystem" is a level of organisation above the community and includes abiotic components (Tansley 1935); Hawksworth & Grube replied in [*Reflections on lichens as ecosystems*, doi:10.1111/nph.19418](https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.19418). **This debate is live and unresolved as of 2024.** The practical consequence for HabitatMech: do not write "ecosystem" into the definition as though it were settled terminology; "the thallus is a fungal structure that houses photobionts and a microbiome" is the claim all parties accept.

### 2.4 The parent record

`parent_habitats` currently points at `habitatmech:GOLD.a8fc5001d1` (GOLD `Host-associated > Fungi`, 635 assertions), which is itself UNGROUNDED with `FOODON:03411261` as xref. **That parent record looks like an EXACT grounding candidate for `ENVO:01001041` *fungi-associated environment*** — the definitions coincide, and the term is already in the slice. That is a separate curation item, but grounding it would give this record a grounded broader term for free. *(This is my inference from the two definitions, not something a source states.)*

---

## 3. Differentia — what distinguishes it from its siblings

Siblings under `Host-associated > Fungi` in GOLD are *Mycelium* (260), *Fruiting body* (140), *Spore* (135), *Mycorrhiza*, *Sclerotium*, *Stroma*, *Appressorium*, *Germ tube*. Each of those is a **part or growth form of one fungus**; a lichen is **a whole composite organism**, which is exactly why this repo's rule (parts ground to the anatomy term, wholes keep a minted identity) sends *Lichen* down a different path from its siblings.

Beyond that structural difference, the discriminating, observable properties:

**Symbiotic composition.** The thallus contains, obligately, a lichen-forming fungus plus a green-algal and/or cyanobacterial photobiont; frequently also cystobasidiomycete yeasts in the cortex (Spribille et al. 2016 — though a broad follow-up survey detected these in only 2.7 % of taxa and 2.2 % of samples, [Lendemer et al. 2019, *American Journal of Botany*, doi:10.1002/ajb2.1339](https://bsapubs.onlinelibrary.wiley.com/doi/full/10.1002/ajb2.1339)), endolichenic fungi, and lichenicolous fungi.

**Microbial load, distinct from any purely fungal structure.** ~10⁷–10⁸ bacterial cells per gram fresh weight of thallus — the upper figure is stated in the abstract of [Grube et al. 2009, *ISME J* 3:1105–1115, doi:10.1038/ismej.2009.63](https://www.nature.com/articles/ismej200963) ("up to 10⁸ cells per gram fresh weight"), the range in [Grimm et al. 2021, *Front. Microbiol.* 12:623839, doi:10.3389/fmicb.2021.623839](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2021.623839/full). For contrast, vascular-plant leaf surfaces carry ~10⁵ cells cm⁻² (Grimm et al. 2021).

**Biofilm organisation on hyphal surfaces.** Bacteria "form highly structured, biofilm-like assemblages on fungal surfaces" (Grube et al. 2009). FISH–CLSM shows layer-specific patterns: even Alphaproteobacterial colonisation of both cortices in *Lobaria pulmonaria*; Betaproteobacteria restricted to the lower surface; densest colonisation on the *inner* podetium wall in *Cladonia*; bacteria in the cracks between areoles of crustose thalli (Cardinale et al. 2008; Cardinale et al. 2012, *FEMS Microbiol Lett* 329:111–115; [Erlacher et al. 2015, *Front. Microbiol.* 6:53, doi:10.3389/fmicb.2015.00053](https://www.frontiersin.org/articles/10.3389/fmicb.2015.00053/full); reviewed in [Aschenbrenner et al. 2016, *Front. Microbiol.* 7:180, doi:10.3389/fmicb.2016.00180](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2016.00180/full)).

**Poikilohydry — the defining physicochemical regime.** The thallus cannot regulate its water content; it swings between >150 % and <20 % of dry weight, and "recurrent desiccation may prevent persistence of fast growing bacterial opportunists" (Grimm et al. 2021). This, plus UV exposure at the cortex and oligotrophy, is the abiotic filter that makes a thallus a selective habitat rather than a passive surface.

**Extracellular secondary-metabolite crystals.** The mycobiont deposits "lichen substances" as crystals on the outer surface of hyphae — atranorin, parietin, usnic acid and melanins in the cortex; physodic, protocetraric and related acids in the medulla — up to ~20 % of thallus dry weight, >800 compounds described, most of them lichen-exclusive ([Ranković & Kosanić 2019, in *Lichen Secondary Metabolites*, 2nd ed., Springer, doi:10.1007/978-3-030-16814-8_1](https://link.springer.com/chapter/10.1007/978-3-319-13374-4_1)). Several are antibacterial in vitro, notably against Gram-positives ([Lauterwein et al. 1995, *Antimicrob Agents Chemother* 39:2541–2543, doi:10.1128/AAC.39.11.2541](https://journals.asm.org/doi/10.1128/aac.39.11.2541)), and lichens producing abundant acidic metabolites carry significantly different bacterial communities (Grimm et al. 2021). Some lichen-associated bacteria transform usnic acid to less active products ([Noh et al. 2021, *Chemosphere*, doi:10.1016/j.chemosphere.2020.128444](https://www.sciencedirect.com/science/article/abs/pii/S003194222031150X)).

**Community composition, reproducibly distinct from the substrate.** Alphaproteobacteria dominate; Rhizobiales alone make up about a third of the bacteria in *L. pulmonaria*; Rhodospirillales co-dominate in chlorolichens, Sphingomonadales in cyanolichens (Grimm et al. 2021). The largest survey to date — 456 public + 24 new lichen metagenomes reassembled into 1,000 MAGs (674 bacterial, 294 fungal, 32 algal) — found four bacterial families from two phyla (Acetobacteraceae, Beijerinckiaceae, Sphingomonadaceae, Acidobacteriaceae) accounting for as many occurrences as all other 71 families from 16 phyla combined, with *Lichenihabitans* in 99 metagenomes ([Tagirdzhanova et al. 2024, *PLOS Biology* 22:e3002862, doi:10.1371/journal.pbio.3002862](https://journals.plos.org/plosbiology/article?id=10.1371%2Fjournal.pbio.3002862)). "Lichen-associated bacterial communities are not merely a simple extension of the prokaryotic community of the lichen-surrounding environment" (Grimm et al. 2021).

**Within-thallus gradients.** Bacterial diversity increases from apical to basal parts of upright thalli; older central regions are richer than the younger periphery; thallus age, sun exposure and substrate all shape the community (Cardinale et al. 2012b, "Age, sun and substrate"; Grimm et al. 2021).

---

## 4. Recent developments (2023–2025) worth citing

- **Tagirdzhanova et al. 2024** (*PLOS Biology*, doi:10.1371/journal.pbio.3002862) — 1,000 MAGs. Two results that should change how a curator words any mechanism claim: (i) **no `nifH` was recovered in any non-cyanobacterial MAG** (one non-cyanobacterial `nifH` across all assemblies), contradicting the widely repeated claim that the bacterial microbiome contributes N₂ fixation — diazotrophy in lichens is a cyanobiont function; (ii) interdigitated vitamin auxotrophies — most lichen fungi biotin-auxotrophic, most bacteria thiamine-auxotrophic, algae with partial/complete pathways for both — proposed as the cross-feeding basis of the association. The same paper warns that lichen metagenomes contain "bacteria involved in degradation of senescing thalli, by-catch from the surrounding environment and contaminants," which is directly relevant to what a "Lichen" sample actually contains.
- **Schwob et al. 2024** (*Environmental Microbiome* 9, doi:10.1186/s40793-024-00598-x) — four *Peltigera* cyanolichen species across three Chilean Patagonian bioclimatic zones, sampling thalli, substrates and neighbouring soils. Frames thalli explicitly as **island-like habitats**: host phylogeny (especially the cyanobiont) with climate secondary imposes strong ecological filtering; thalli harbour specialised, locally adapted, low-diversity communities with sparse networks relative to soil and substrate, and this fragmentation raises landscape gamma diversity.
- **Sinsuwan et al. 2023** (*Scientific Reports* 13, doi:10.1038/s41598-023-32759-2) — ten tropical lichens, Doi Inthanon, Thailand; *Heterodermia* dominated by Proteobacteria with Planctomycetota, Actinobacteriota, Verrucomicrobiota, Acidobacteriota. Also quantifies how much the isolation method changes what you recover — a caution for comparing GOLD-registered lichen isolates across studies.
- **2025, *npj Biofilms and Microbiomes*** (doi:10.1038/s41522-025-00736-4) — assembly processes for paired soil and lichen microbiomes along an urbanisation gradient.
- **Lichen-associated black fungi genomics, 2024** ([PMC11664114](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11664114/)) — the non-lichenised fungal inhabitants of thalli.
- **Sanders 2024 / Hawksworth & Grube 2024** — the "is a lichen an ecosystem?" exchange (§2.3), still open.

---

## 5. Synonyms, and what NOT to conflate

**Names in real use for this concept**

- lichen thallus
- lichen-associated environment
- lichen holobiont / lichen symbiosis (used for the biological system; acceptable as a related synonym, but see the ecosystem dispute)
- lichen microbiome habitat / lichen microbiota habitat (used for the environment as sampled)
- lichenised fungal thallus

**Do not conflate**

| Confusable | Why it is different |
|---|---|
| **Clinical "lichen" terms** — `SNOMED:88996004` *Lichen*, `mesh:D008010` *Lichen Planus*, `mesh:D018459` *Lichen Sclerosus et Atrophicus*, `MONDO:0007899`, `MONDO:0018879` *lichen planopilaris*, and ~290 more hits on the string | Dermatological lesion morphology, named for a superficial resemblance. Entirely unrelated. A label-only string match in this family is the single most likely wrong grounding for this record. |
| `ENVO:03600084` **lichen material** | An *organic material* derived from lichen mats — detached biomass, e.g. reindeer-lichen litter. Not a living host environment. |
| `ENVO:01000889` **area of lichen-dominated vegetation**, `ENVO:01000949` **lichen woodland** | Landcover units at square-metre-to-hectare scale. A "lichen heath soil" sample is an environmental, not a host-associated, sample. |
| **Biological soil crust** | Lichens are one component alongside cyanobacteria, mosses and free-living algae; a BSC sample is soil, and ENVO has no direct equivalent term surfaced by a `crust` search (hits are all planetary/geological crust). Sampling a BSC is not sampling a thallus. |
| **The mycobiont as an organism** — `BTO:0000892` *mycobiont* | An organism/tissue-role term (BTO glosses it "the fungal component of the lichen partnership"), not a place, and narrower than the thallus. |
| **The photobiont / lichen alga** | Sampling *Trebouxia* or *Nostoc* in culture is not sampling a lichen. GOLD's own `Host-associated > Algae` paths are separate records in this corpus. |
| **The substrate** — bark, rock, `ENVO:03605001` *epilithon* | The lichen–substrate interface is inside the concept; the substrate itself is not. Substrate identity is a documented driver of the thallus community, which only matters if the two are kept apart ([Aschenbrenner et al. 2016](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2016.00180/full); [Leiva et al. 2019, *FEMS Microbiol Ecol* 95:fiz012](https://academic.oup.com/femsec/article/95/3/fiz012/5298863) found substrate rather than photobiont determined the community in an optional lichen symbiosis). |
| **Lichenicolous fungi vs endolichenic fungi** | Not synonyms in the source literature: endolichenic fungi are asymptomatic Ascomycota inside healthy thalli, distinct from mycobiont and from symptom-inducing lichenicolous fungi ([U'Ren et al. 2012, *Am J Bot* 99:898–914, doi:10.3732/ajb.1100459](https://pubmed.ncbi.nlm.nih.gov/22539507/); [Suryanarayanan & Thirunavukkarasu 2017, *Mycology* 8:189–196, doi:10.1080/21501203.2017.1352048](https://www.tandfonline.com/doi/full/10.1080/21501203.2017.1352048)) — though Hafellner (2018) has proposed collapsing the distinction. Both are *inhabitants* of the concept, not the concept. |
| **`FOODON:03412345` *lichen*** | The composite organism itself: "A composite organism that arises from algae or cyanobacteria living among filaments of multiple fungi species in a mutualistic relationship." Correctly kept as `relation: xref` on this record (#99) — it names the organism, not the place. |

---

## 6. Should this be a term at all?

**Yes.** It clears every bar this corpus applies:

1. **It is a place a microbe lives, not a taxon.** The organism-identity screen (#109) fired correctly on `FOODON:03412345`, but the GOLD path is `Host-associated`, so the *concept* is the environment the organism provides. The corpus disposition for that is a minted identity plus the organism term as an xref, which is what the record already has. `NOT_APPLICABLE` would be wrong — it is reserved for diseases, qualities, processes and procedures, and `tests/test_decisions.py` fails on a NOT_APPLICABLE whose target is an organism term.
2. **It is a whole organism, not a part** — so unlike its GOLD siblings *Mycelium*, *Fruiting body* and *Spore*, it does not ground to a fungal-anatomy term, and `ENVO:01001058` *environment associated with a fungal tissue* does not fit.
3. **The habitat is real, bounded and independently characterised.** Distinct community, distinct abundance regime, distinct physicochemistry, layer-resolved microhabitats, and a body of literature spanning 2006–2025 including a 1,000-MAG global survey.
4. **Nothing in ENVO names it.** The gap is genuine, and the family it belongs to (`plant-associated`, `animal-associated`, `fungi-associated`, `cnidarian-associated environment`) has an obvious place for it.

**Recommended disposition:** keep `CONFIRM_UNGROUNDED` with `FOODON:03412345` as `relation: xref`, and treat this as an ENVO term-request candidate for **`lichen-associated environment`** — a sibling of `ENVO:01001179` *cnidarian-associated environment*, sitting under `ENVO:01001041`. Note the standing rule in this repo's memory: an ENVO term request needs explicit per-request permission, not batch approval.

**Optional record improvement:** add `ENVO:01001041` *fungi-associated environment* to `parent_habitats` with `relation: parent`. It is genuinely broader, it is in the vendored slice, and it would give the record a grounded ancestor even while its identity stays minted. *(Recommendation, not a source claim.)*

---

## 7. Claims that are my inference, not a source's

- That `ENVO:01001041` is the *smallest* fitting genus — that is a conclusion from an exhaustive OLS4 search of ENVO (August 2026) returning no closer term, not a statement any publication makes.
- That the parent record `habitatmech:GOLD.a8fc5001d1` (GOLD *Host-associated > Fungi*) is an EXACT grounding candidate for `ENVO:01001041` — inferred from definition comparison.
- The mapping of GOLD's `Fungi` Ecosystem Category onto "the host is a fungus" — GOLD documents the five-level scheme and the `Host-associated` top level, but the v.9 paper's worked example is the plant/leaf-nodule path, not the lichen path.
- That the clinical `lichen*` cluster is the highest-risk false grounding for this record — a judgement about failure modes, not a published finding.

---

## Sources

- [Hawksworth DL, Grube M (2020) Lichens redefined as complex ecosystems. *New Phytologist* 227(5):1281–1283. doi:10.1111/nph.16630](https://nph.onlinelibrary.wiley.com/doi/full/10.1111/nph.16630) · [PMC7497170](https://pmc.ncbi.nlm.nih.gov/articles/PMC7497170/)
- [Sanders WB (2024) The disadvantages of current proposals to redefine lichens. *New Phytologist* 241:969–971. doi:10.1111/nph.19321](https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.19321)
- [Hawksworth DL, Grube M (2024) Reflections on lichens as ecosystems. *New Phytologist*. doi:10.1111/nph.19418](https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.19418)
- [Grube M, Cardinale M, de Castro JV Jr, Müller H, Berg G (2009) Species-specific structural and functional diversity of bacterial communities in lichen symbioses. *ISME J* 3:1105–1115. doi:10.1038/ismej.2009.63](https://www.nature.com/articles/ismej200963) · [PMID 19554038](https://pubmed.ncbi.nlm.nih.gov/19554038/)
- [Grimm M, Grube M, Schiefelbein U, Zühlke D, Bernhardt J, Riedel K (2021) The lichens' microbiota, still a mystery? *Front. Microbiol.* 12:623839. doi:10.3389/fmicb.2021.623839](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2021.623839/full)
- [Aschenbrenner IA, Cernava T, Berg G, Grube M (2016) Understanding microbial multi-species symbioses. *Front. Microbiol.* 7:180. doi:10.3389/fmicb.2016.00180](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2016.00180/full)
- [Erlacher A et al. (2015) Rhizobiales as functional and endosymbiontic members in the lichen symbiosis of *Lobaria pulmonaria*. *Front. Microbiol.* 6:53. doi:10.3389/fmicb.2015.00053](https://www.frontiersin.org/articles/10.3389/fmicb.2015.00053/full)
- [Spribille T et al. (2016) Basidiomycete yeasts in the cortex of ascomycete macrolichens. *Science* 353(6298):488–492. doi:10.1126/science.aaf8287](https://www.science.org/doi/10.1126/science.aaf8287)
- [Lendemer JC et al. (2019) A taxonomically broad metagenomic survey of 339 species … cystobasidiomycete yeasts are not ubiquitous. *American Journal of Botany*. doi:10.1002/ajb2.1339](https://bsapubs.onlinelibrary.wiley.com/doi/full/10.1002/ajb2.1339)
- [Tagirdzhanova G et al. (2024) Microbial occurrence and symbiont detection in a global sample of lichen metagenomes. *PLOS Biology* 22(11):e3002862. doi:10.1371/journal.pbio.3002862](https://journals.plos.org/plosbiology/article?id=10.1371%2Fjournal.pbio.3002862)
- [Schwob G et al. (2024) Host specialization and spatial divergence of bacteria associated with *Peltigera* lichens promote landscape gamma diversity. *Environmental Microbiome* 9. doi:10.1186/s40793-024-00598-x](https://link.springer.com/article/10.1186/s40793-024-00598-x)
- [Sinsuwan W et al. (2023) Bacterial microbiome in tropical lichens and the effect of the isolation method on culturable lichen-derived actinobacteria. *Scientific Reports* 13. doi:10.1038/s41598-023-32759-2](https://www.nature.com/articles/s41598-023-32759-2) · [PMC10073151](https://pmc.ncbi.nlm.nih.gov/articles/PMC10073151/)
- [Ecological processes driving soil and lichen microbiome assembly along an urbanization gradient (2025) *npj Biofilms and Microbiomes*. doi:10.1038/s41522-025-00736-4](https://www.nature.com/articles/s41522-025-00736-4)
- [Bacterial communities associated with an island radiation of lichen-forming fungi (2024) *PLOS ONE*. doi:10.1371/journal.pone.0298599](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0298599)
- [Leiva D et al. (2019) Bacterial communities in an optional lichen symbiosis are determined by substrate, not algal photobionts. *FEMS Microbiol Ecol* 95:fiz012](https://academic.oup.com/femsec/article/95/3/fiz012/5298863)
- [U'Ren JM, Lutzoni F, Miadlikowska J, Laetsch AD, Arnold AE (2012) Host and geographic structure of endophytic and endolichenic fungi at a continental scale. *Am J Bot* 99:898–914. doi:10.3732/ajb.1100459](https://pubmed.ncbi.nlm.nih.gov/22539507/)
- [Suryanarayanan TS, Thirunavukkarasu N (2017) Endolichenic fungi: the lesser known fungal associates of lichens. *Mycology* 8:189–196. doi:10.1080/21501203.2017.1352048](https://www.tandfonline.com/doi/full/10.1080/21501203.2017.1352048)
- [Genomic features of lichen-associated black fungi (2024). PMC11664114](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11664114/)
- [Darnajoux R et al. (2014) Lichen-symbiotic cyanobacteria associated with *Peltigera* have an alternative vanadium-dependent nitrogen fixation system. *European Journal of Phycology* 49:1. doi:10.1080/09670262.2013.873143](https://www.tandfonline.com/doi/full/10.1080/09670262.2013.873143)
- [Ranković B, Kosanić M (2019) Lichens as a potential source of bioactive secondary metabolites. In *Lichen Secondary Metabolites*, 2nd ed. Springer. doi:10.1007/978-3-030-16814-8_1](https://link.springer.com/chapter/10.1007/978-3-319-13374-4_1)
- [Lauterwein M, Oethinger M, Belsner K, Peters T, Marre R (1995) In vitro activities of the lichen secondary metabolites vulpinic acid, (+)-usnic acid, and (−)-usnic acid. *Antimicrob Agents Chemother* 39:2541–2543. doi:10.1128/AAC.39.11.2541](https://journals.asm.org/doi/10.1128/aac.39.11.2541)
- [Noh H-J et al. (2021) Lichen-associated bacteria transform antibacterial usnic acid to products of lower antibiotic activity. *Chemosphere*](https://www.sciencedirect.com/science/article/abs/pii/S003194222031150X)
- [Mukherjee S et al. (2023) Twenty-five years of Genomes OnLine Database (GOLD): data updates and new features in v.9. *Nucleic Acids Research* 51:D957–D963. doi:10.1093/nar/gkac974](https://academic.oup.com/nar/article/51/D1/D957/6786204) · [GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)
- [May TW et al. (2019) Chapter F of the International Code of Nomenclature for algae, fungi, and plants (San Juan). *IMA Fungus* 10:21. doi:10.1186/s43008-019-0019-1](https://imafungus.biomedcentral.com/articles/10.1186/s43008-019-0019-1) · [IAPT Article F.1](https://www.iapt-taxon.org/nomen/pages/main/art_f1.html)
- [Environment Ontology (ENVO)](http://obofoundry.org/ontology/envo.html) — terms `ENVO:01001041`, `ENVO:01001000`, `ENVO:01001058`, `ENVO:03600084`, `ENVO:01000889`, `ENVO:01000949`, `ENVO:03605001` retrieved from [OLS4](https://www.ebi.ac.uk/ols4/), August 2026, and cross-checked against `data/raw/ontology_terms.tsv`
- [Cephalodium (structure and N₂ fixation)](https://en.wikipedia.org/wiki/Cephalodium) and [ANBG, Lichens: form and structure](https://www.anbg.gov.au/lichen/form-structure.html) — tertiary sources used only for standard thallus anatomy; for a citable authority use Büdel B & Scheidegger C, "Thallus morphology and anatomy", in Nash TH III (ed.) *Lichen Biology*, 2nd ed., Cambridge University Press, 2008

## Citations

1. https://academic.oup.com/nar/article/51/D1/D957/6786204
2. https://gold.jgi.doe.gov/ecosystem_classification
3. https://www.science.org/doi/10.1126/science.aaf8287
4. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2021.623839/full
5. https://en.wikipedia.org/wiki/Cephalodium
6. https://www.tandfonline.com/doi/full/10.1080/09670262.2013.873143
7. https://www.iapt-taxon.org/nomen/pages/main/art_f1.html
8. https://imafungus.biomedcentral.com/articles/10.1186/s43008-019-0019-1
9. https://nph.onlinelibrary.wiley.com/doi/full/10.1111/nph.16630
10. https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.19321
11. https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.19418
12. https://bsapubs.onlinelibrary.wiley.com/doi/full/10.1002/ajb2.1339
13. https://www.nature.com/articles/ismej200963
14. https://www.frontiersin.org/articles/10.3389/fmicb.2015.00053/full
15. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2016.00180/full
16. https://link.springer.com/chapter/10.1007/978-3-319-13374-4_1
17. https://journals.asm.org/doi/10.1128/aac.39.11.2541
18. https://www.sciencedirect.com/science/article/abs/pii/S003194222031150X
19. https://journals.plos.org/plosbiology/article?id=10.1371%2Fjournal.pbio.3002862
20. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11664114/
21. https://academic.oup.com/femsec/article/95/3/fiz012/5298863
22. https://pubmed.ncbi.nlm.nih.gov/22539507/
23. https://www.tandfonline.com/doi/full/10.1080/21501203.2017.1352048
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC7497170/
25. https://pubmed.ncbi.nlm.nih.gov/19554038/
26. https://link.springer.com/article/10.1186/s40793-024-00598-x
27. https://www.nature.com/articles/s41598-023-32759-2
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC10073151/
29. https://www.nature.com/articles/s41522-025-00736-4
30. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0298599
31. http://obofoundry.org/ontology/envo.html
32. https://www.ebi.ac.uk/ols4/
33. https://www.anbg.gov.au/lichen/form-structure.html