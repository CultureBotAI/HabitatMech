---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T02:04:26.547315'
end_time: '2026-08-18T02:15:39.923151'
duration_seconds: 673.38
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Rot-Root,Stem
  habitat_identifier: habitatmech:BACDIVE.04ddbbeabe
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Rot-Root,Stem'
  assertions: '2'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Cohort\
    \ review: root-or-stem rot. Same PO:0009047 'stem' merge as the leaf-spot source,\
    \ and the same objection \u2014 the dropped alternative is half the concept. (source\
    \ concept habitatmech:BACDIVE.04ddbbeabe)"
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
  web_search_requests: 17
  num_turns: 50
  total_cost_usd: 4.2100925
  session_id: f2d00b65-fc7c-4123-8854-f880c079798a
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 21
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Rot-Root,Stem
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.04ddbbeabe
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Rot-Root,Stem
- **Upstream assertion volume:** 2
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Cohort review: root-or-stem rot. Same PO:0009047 'stem' merge as the leaf-spot source, and the same objection — the dropped alternative is half the concept. (source concept habitatmech:BACDIVE.04ddbbeabe)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Rot-Root,Stem** as a microbial habitat, with citations.

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

# Rot-Root,Stem — definition research

**Concept:** `habitatmech:BACDIVE.04ddbbeabe` · label `Rot-Root,Stem` · category OTHER · UNGROUNDED · 2 BacDive strains

---

## Proposed definition

> **A portion of plant matter which consists of the macerated, softened or necrotic tissue of a root or stem that is being decomposed in place by an invading plant-pathogenic microorganism.**

**A caveat the curator should read before adopting it.** That sentence defines an organ-neutral class ("rotted plant tissue") artificially narrowed by a disjunction ("root or stem"). The disjunction is not a real differentia — nothing about rot in a root differs in kind from rot in a fruit — it is BacDive's tag scoping. **The missing intermediate class is `rotted plant tissue` / `plant rot lesion`**, and saying so is more useful than the sentence above. My recommendation in §6 is to request that intermediate class and let this record be its root/stem instance, rather than to mint "Rot-Root,Stem" as a term in its own right.

---

## 1. What the concept denotes

### The label is a BacDive MISO tag, not free text

`Rot-Root,Stem` is kg-microbe's normalisation of the BacDive isolation-source tag **`#Rot (Root,Stem)`**. Its place in BacDive's Microbial Isolation Source Ontology (MISO) is the single most important fact about it, and it is verifiable directly on a strain page.

BacDive tags each strain with up to four independent `Cat1/Cat2/Cat3` triplets ([Reimer et al., *NAR* 2019, D631–D636](https://academic.oup.com/nar/article/47/D1/D631/5106998); [BacDive isolation-source browser](https://bacdive.dsmz.de/isolation-sources)). For *Pectobacterium polaris* NIBIO1006ᵀ ([BacDive ID 158290](https://bacdive.dsmz.de/strain/158290)) the triplets are:

| Cat1 | Cat2 | Cat3 |
|---|---|---|
| Host | Plants | Herbaceous plants (Grass, Crops) |
| Host Body-Site | Plant | Root (Rhizome) |
| **Infection** | **Plant infections** | **Rot (Root, Stem)** |

Free-text isolation source: *"potato tuber of cv. Polaris with severe symptoms of soft rot"* ([DSMZ catalogue DSM-105255](https://www.dsmz.de/catalogues/details/culture/DSM-105255.html)).

Three things follow, and they constrain everything below:

1. **In BacDive's own model this string is the *infection* facet, not the *place* facet.** The place was recorded separately, by the `Host Body-Site → Plant → Root (Rhizome)` triplet. `#Rot (Root,Stem)` answers "what was wrong with it", not "what was it".
2. **The organ scope in the label is unreliable.** The attesting strain came from a *tuber* — a stem-derived storage organ (PO has `PO:0004543` *shoot axis tuber* and `PO:0004547` *subterranean shoot axis tuber* for exactly this; [Plant Ontology, Cooper et al.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2447502/)) — yet was tagged both `Root (Rhizome)` and `Rot (Root, Stem)`. The tag is used for below-ground and stem-axis rots broadly, not for a botanically clean root ∪ stem set.
3. **The attestations are bacterial soft rot specifically.** Both characteristic taxa on the record are soft-rot Pectobacteriaceae: *Pectobacterium polaris* (`NCBITaxon:2042057`) and *Pectobacterium carotovorum* (`NCBITaxon:554`). I could confirm the isolation source of the *P. polaris* strain but **not** of the *P. carotovorum* strain — that one I could not pin to a BacDive record, so its tissue of origin is unverified.

### The habitat reading

Read as a place — which is what an *isolation source* operationally is — the concept denotes:

> the region of a plant root or stem whose tissue has been enzymatically macerated and killed in situ by a microbial pathogen: wet, softened or necrotic parenchyma still attached to (or lately part of) the living plant, together with the exudate and slime in it.

That is a genuine, samplable material. Standard bench practice treats it as one: pathogen isolation targets *the advancing margin of the lesion* — a 5–10 mm block spanning rotted and adjacent healthy tissue — precisely because the rotted centre and the healthy tissue are microbiologically different places ([Schaad et al., *Laboratory Guide for Identification of Plant Pathogenic Bacteria*, APS Press; teaching protocol summarised at SU LMS](https://lms.su.edu.pk/lesson/1074/practical-isolation-of-plant-pathogenic-bacteria)).

### Boundary — inside and outside

**Inside:** macerated/necrotic root, stem, crown, collar, basal-stem, rhizome and stem-tuber tissue of a living or freshly killed plant; the lesion and its advancing margin; the liquid and slime within it.

**Outside — neighbouring concepts:**

- **Rhizosphere** (`ENVO:00005801`) and **rhizoplane** (`ENVO:01001181`) — soil and root-surface compartments *around* a root, healthy or not. Both are in the vendored slice.
- **Healthy root endosphere** — BacDive has a separate `Endosphere` source (2 strains) in this corpus.
- **Plant litter** (`ENVO:01000628`) — dead plant material *that has fallen to the ground* and detached. Rot tissue is still part of the plant.
- **Soil** — the pathogen reservoir for most root rots, not the rot.
- **Wood decay** — BacDive keeps a distinct `#Rot fungi` Cat3 tag; white-/brown-rot of lignified wood is a different substrate and a different concept.
- **Postharvest / storage rot of produce** — bleeds into the FOOD category (BacDive also has a separate `Spoiled` source, 3 strains). The *P. polaris* case sits exactly on this line: a rotting stored tuber is both.

### Ambiguity — the readings, not silently resolved

| Reading | What it makes the term | Support |
|---|---|---|
| **(a) The rotted tissue** — a material region of a diseased root/stem | a habitat (material class) | Isolation-source semantics; lesion-margin sampling practice; distinctive physicochemistry (§3) |
| **(b) The disease syndrome** — "root rot" / "stem rot", a named disease | not a habitat; NOT_APPLICABLE-shaped | BacDive's own Cat1 = `#Infection`; the plain-language meaning of "root rot"; the separate Body-Site triplet already carries the place |
| **(c) The organ, tagged by disease** — i.e. just root and stem | already covered by `PO:0009005` + `PO:0009047` | The lexical match the seeder proposed, and what curation rejected |

Reading (c) is the one already rejected and it should stay rejected: `PO:0009047` *stem* is the seeder's `skos:closeMatch` (`data/raw/isolation_source_groundings.tsv:266`) and it is *also* the proposed target for `Spot-Leaf,Stem` (line 291), so adopting it merges two different diseases onto one record — the objection already recorded. Readings (a) and (b) are both live; §6 weighs them.

---

## 2. Genus — the broader kind

### Nothing in ENVO, PO, UBERON, FOODON or BTO names rotted plant tissue

I checked the vendored slice (`data/raw/ontology_terms.tsv`) for ENVO and PO terms whose label or definition contains *rot*, *necro*, *diseas*, *lesion*, *macerat*, *infect* or *decay*. **No hit denotes diseased or decomposing plant tissue.** An OLS4 search of ENVO for `diseased necrotic lesion` returns zero results, and for `rotting decaying wood` zero results.

### Recommended genus

**`ENVO:01001121` — *plant matter*** — "Organic material which is primarily composed of plant structures, living or dead." In the slice. It is a material class, matches what a sample of rot actually is, and its definition already spans living and dead, which is the state rot tissue is in.

If the corpus prefers an *environment* class over a *material* class, the genus is instead **`ENVO:01001057` — *environment associated with a plant part or small plant*** ("An environmental system determined by part of a living or dead plant, or a whole small plant"; EMPO-aligned, alt-label "Plant corpus"; in the slice, and currently **childless** in ENVO — I confirmed 0 children via OLS4, so a new subclass would be the first). The definition would then read *"An environment associated with a plant part which is determined by the macerated or necrotic tissue of a root or stem undergoing microbial rot."*

### Near-misses and why each fails

| CURIE | Label | Why it is not a match |
|---|---|---|
| `PO:0009047` | stem | **Narrower and wrong facet.** Drops the root half; asserts nothing about rot; already the proposed target of the leaf-spot sibling. The seeder's own match. |
| `PO:0009005` | root | Same, mirrored. Drops the stem half. |
| `PO:0009007` | portion of plant tissue | Correct *kind* but silent on rot — no differentia at all, and PO models healthy anatomy. |
| `PO:0025626` | plant gall | **The precedent, not the match.** "A multi-tissue plant structure that develops in response to a biotic stress (`PSO:0000011`)." PO does model a disease-induced structure — but only this one. There is no PO analogue for a rot lesion. (GOLD's `Galls` was GROUNDed here; `curation/decisions.tsv:1661`.) |
| `ENVO:01000349` | root matter | **Narrower and asserts health-neutrality.** "An organic material primarily composed of a portion of plant root." Drops the stem; says nothing about rot. Closest ENVO material term. |
| `ENVO:01000628` | plant litter | **Asserts detachment.** "…dead plant material…that has fallen to the ground." Rot tissue is in situ. |
| `ENVO:01001395` | necromass | **Over-asserts death.** "Biomass composed primarily of dead organisms, their parts, or their organic derivatives." A rot lesion is on a living plant and its advancing margin is living tissue. |
| `ENVO:00005801` / `ENVO:01001181` | rhizosphere / rhizoplane | Wrong compartment — soil and root surface, not root interior. |
| `ENVO:01001001` | plant-associated environment | **Too broad** — the whole plant-associated class; would lose the concept entirely. |
| `ENVO:03600036` | pathogen-suppressive soil | Soil, and the opposite polarity. Surfaced by ENVO search for "plant disease"; the only ENVO term that does. |
| `PSO:0000196`, `PSO:0002047`, `PSO:0000738`, … | *cassava Armillaria root rot fungal disease* etc. | **Diseases, not places**, and host-and-pathogen-specific — the Planteome stress ontology has dozens of these ("A cassava disease caused by *Armillaria mellea* affecting a root"). Grounding here would assert a disease and a host the sources never claim. |
| `TO:0020058`, `TO:0020059` | barley/wheat common root rot response | **Traits**, not places. |

**Conclusion: no existing term expresses the genus-plus-differentia. HabitatMech must supply the definition, or dispose of the concept as non-habitat.**

---

## 3. Differentia — what distinguishes it from siblings under *plant matter*

Each property below is observable or measurable, and each is cited. All refer to bacterial soft rot unless noted, because that is what the two attesting strains are.

**(a) Enzymatic maceration is the defining process.** Soft-rot Pectobacteriaceae secrete plant-cell-wall-degrading enzymes — chiefly pectate and pectin lyases, plus polygalacturonases, pectin esterases, cellulases and proteases — which dissolve the middle lamella and release protoplast contents; tissue loses coherence and becomes watery ([Charkowski, *Annu. Rev. Phytopathol.* 56:269–288, 2018, doi:10.1146/annurev-phyto-080417-045906](https://www.annualreviews.org/content/journals/10.1146/annurev-phyto-080417-045906), PMID 29958075; [Davidsson et al., *Front. Plant Sci.* 2013, PMC3678301](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3678301/)). This is what separates rot from every other kind of plant matter: the material is *plant tissue being taken apart in place*.

**(b) The interior is hypoxic to anoxic.** A surface water film blocks oxygen replenishment; tissue respiration then depletes it, and anaerobiosis both disables oxygen-dependent host defences (phytoalexins, lignification, suberisation) and permits bacterial multiplication ([Pérombelon, *Plant Pathology* 51:1–12, 2002, doi:10.1046/j.0032-0862.2001.Shorttitle.doc.x](https://bsppjournals.onlinelibrary.wiley.com/doi/full/10.1046/j.0032-0862.2001.Shorttitle.doc.x); [Pérombelon & Kelman, *Annu. Rev. Phytopathol.* 18:361–387, 1980](https://www.annualreviews.org/doi/10.1146/annurev.py.18.090180.002045)). Hypoxia is reinforced as the rot proceeds because bacterial slime further reduces diffusion ([Kõiv et al. 2015, below](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4484245/)). "The limited oxygen environment on the rotting site of the tubers allows *P. atrosepticum* for nitrate respiration, enhancing its growth rate and invasion" ([Maciag et al., *Int. J. Mol. Sci.* 25(7):3757, 2024, doi:10.3390/ijms25073757](https://pmc.ncbi.nlm.nih.gov/articles/PMC11011919/), PMID 38612570). Direct measurement of tuber oxygen status during maceration goes back to [Phytopathology 73:536, 1983](https://www.apsnet.org/publications/phytopathology/backissues/Documents/1983Abstracts/Phyto73_536.htm).

**(c) It is a nutrient flush, and it drives a reproducible succession.** This is the strongest single habitat-level citation, and the one I would build the differentia on. Kõiv et al. tracked 16S communities through *P. atrosepticum* maceration of potato tubers: the inoculating pathogen is *always taken over by endophytes* during maceration; Gammaproteobacteria (*Enterobacter*, *Pseudomonas*) dominate by day 2 on released sugars; organic-acid users (*Comamonas*, *Delftia*) then displace them; and by day 8 anaerobic pectolytic *Clostridia* rise, attributed to oxygen depletion ([Kõiv et al., *Sci. Rep.* 5:11606, 2015, doi:10.1038/srep11606](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4484245/), PMID 26118792). A rot lesion is therefore not merely "plant tissue with a pathogen in it" — it is a distinct successional community, which is what makes the habitat reading defensible at all.

**(d) The community is depleted and pathogen-skewed relative to healthy tissue of the same organ.** Across recent root-rot microbiome studies the endosphere signal is stronger than the rhizosphere signal: bacterial diversity falls as rot progresses and Proteobacteria are enriched in diseased tissue ([*Zanthoxylum bungeanum*, PeerJ 10:e13808, 2022](https://peerj.com/articles/13808/); [*Angelica sinensis*, *Microorganisms* 13(2):417, 2025, doi:10.3390/microorganisms13020417](https://doi.org/10.3390/microorganisms13020417); [*Paris polyphylla*, *Genes* 15(1):21, 2024, doi:10.3390/genes15010021](https://doi.org/10.3390/genes15010021)). The *Ligusticum chuanxiong* study is the most directly relevant sampling design, because it separated *the rotten layer* of a diseased rhizome from *the still-healthy layer of the same rhizome* — i.e. it treated the rot as its own compartment ([PeerJ 13:e20369, 2025](https://peerj.com/articles/20369/)).

**(e) The physical presentation varies with pathogen, and this is a real sibling boundary, not noise.** Wet rots (*Pythium*, *Pectobacterium*) soften and disintegrate the tissue; dry rots (*Rhizoctonia*) leave brown/tan firm tissue ([Cornell Greenhouse Horticulture, Root Rot Diseases](https://greenhouse.cornell.edu/pests-diseases/disease-factsheets/root-rot-diseases/)). *Sclerotinia* stem rot lesions begin water-soaked and end dry and bleached-white with cottony mycelium ([NDSU, *Canola Diseases: Sclerotinia Stem Rot*](https://www.ndsu.edu/agriculture/extension/publications/canola-diseases-sclerotinia-stem-rot); [Ohio State PLPATH-SOY-3](https://ohioline.osu.edu/factsheet/plpath-soy-3)). A definition should therefore say *macerated **or** necrotic* rather than committing to "soft".

**(f) Causal agents span oomycetes, fungi and bacteria.** Root rot is defined as "a plant disease caused by various soil-borne pathogens, primarily characterized by the necrosis and decay of plant roots", predominantly *Fusarium solani* / *F. oxysporum* but also *Pseudomonas* spp. ([Han et al., *Front. Plant Sci.* 15:1504370, 2025, doi:10.3389/fpls.2024.1504370](https://pmc.ncbi.nlm.nih.gov/articles/PMC11830675/), PMID 39963361). The definition must not name a pathogen group.

### Explicitly flagged as **not** supported by a source I read

- **pH.** Alkalinisation of macerating tissue via ammonia release and organic-acid consumption is widely repeated, but I did not find a primary source for it in this search. **Do not put pH in the definition.**
- **Whether the *P. carotovorum* attestation came from a root or a stem.** Unverified.
- **My inference, not a source's claim:** that the isolation-source semantics of a BacDive `#Infection` tag license reading it as a place. Sources establish that rot tissue *is* a distinct microbial compartment (c, d); the inferential step is that BacDive's tag *denotes* that compartment rather than the disease. §6 is where that matters.

---

## 4. Sources

Consolidated, with what each supports.

**Concept identity / source vocabulary**
- BacDive strain 158290, *Pectobacterium polaris* NIBIO1006ᵀ — the tag triplets and free-text source. https://bacdive.dsmz.de/strain/158290
- DSMZ catalogue DSM-105255 — isolation source and locality. https://www.dsmz.de/catalogues/details/culture/DSM-105255.html
- BacDive isolation-source browser — the MISO tag tree, incl. `#Rot (Root,Stem)`, `#Spot (Leaf,Stem)`, `#Gall`, `#Canker`, `#Wilt`, `#Lesion (incl. Necrosis)`, `#Rot fungi`. https://bacdive.dsmz.de/isolation-sources
- Reimer LC et al. *BacDive in 2019.* Nucleic Acids Res 47:D631–D636. doi:10.1093/nar/gky879 — the three-level Cat1/2/3 model and multi-triplet annotation. https://academic.oup.com/nar/article/47/D1/D631/5106998
- Dees MW et al. (2017) *Pectobacterium polaris* sp. nov. IJSEM 67:5222–5229. doi:10.1099/ijsem.0.002448

**Habitat biology**
- Charkowski AO (2018) *The Changing Face of Bacterial Soft-Rot Diseases.* Annu Rev Phytopathol 56:269–288. doi:10.1146/annurev-phyto-080417-045906. PMID 29958075
- Pérombelon MCM (2002) *Potato diseases caused by soft rot erwinias: an overview of pathogenesis.* Plant Pathol 51:1–12. doi:10.1046/j.0032-0862.2001.Shorttitle.doc.x
- Pérombelon MCM & Kelman A (1980) *Ecology of the soft rot Erwinias.* Annu Rev Phytopathol 18:361–387
- Kõiv V et al. (2015) *Microbial population dynamics in response to* Pectobacterium atrosepticum *infection in potato tubers.* Sci Rep 5:11606. doi:10.1038/srep11606. PMID 26118792 — **the succession evidence**
- Maciag T et al. (2024) *Looking for Resistance to Soft Rot Disease of Potatoes Facing Environmental Hypoxia.* Int J Mol Sci 25:3757. doi:10.3390/ijms25073757. PMID 38612570
- Davidsson PR et al. (2013) *Pathogenicity of and plant immunity to soft rot pectobacteria.* Front Plant Sci. PMC3678301
- Han Y et al. (2025) *Root rot in medicinal plants: a review of extensive research progress.* Front Plant Sci 15:1504370. doi:10.3389/fpls.2024.1504370. PMID 39963361
- Zhang et al. (2022) *Zanthoxylum bungeanum root-rot associated shifts in microbiomes.* PeerJ 10:e13808. https://peerj.com/articles/13808/
- (2025) *Microbial community structure … healthy and diseased roots of* Angelica sinensis. Microorganisms 13(2):417. doi:10.3390/microorganisms13020417
- (2024) *Multiomics … resistance to root rot disease of* Paris polyphylla. Genes 15(1):21. doi:10.3390/genes15010021
- (2025) *Microbiome shifts during* Fusarium*-induced* Ligusticum chuanxiong *root rot.* PeerJ 13:e20369 — rotten-layer vs healthy-layer sampling

**Reference / extension**
- Cornell Greenhouse Horticulture, *Root Rot Diseases.* https://greenhouse.cornell.edu/pests-diseases/disease-factsheets/root-rot-diseases/
- NDSU Extension, *Canola Diseases: Sclerotinia Stem Rot.* https://www.ndsu.edu/agriculture/extension/publications/canola-diseases-sclerotinia-stem-rot
- Ohio State Ohioline PLPATH-SOY-3, *Sclerotinia Stem Rot (White Mold) of Soybean.* https://ohioline.osu.edu/factsheet/plpath-soy-3
- Schaad NW et al., *Laboratory Guide for Identification of Plant Pathogenic Bacteria*, 3rd ed., APS Press — lesion-margin isolation; secondary protocol summary at https://lms.su.edu.pk/lesson/1074/practical-isolation-of-plant-pathogenic-bacteria
- Cooper L et al., *The Plant Ontology.* PMC2447502 — PO scope
- EBI OLS4 (queried 2026-08-18) for ENVO/PO/PSO/TO term checks; term membership in the vendored slice checked against `data/raw/ontology_terms.tsv`

---

## 5. Synonyms, and what not to conflate

### Names in real use for the concept (rotted root/stem tissue)

root rot · stem rot · basal rot · basal stem rot · crown rot · collar rot · foot rot · blackleg (of potato — stem rot caused by *Pectobacterium*/*Dickeya*) · soft rot · wet rot · dry rot · bacterial soft rot · rot lesion · macerated tissue · rotted root tissue · decayed root · white mould (for *Sclerotinia* stem rot) · butt rot (woody stems) · damping-off (seedling stage, root/hypocotyl rot)

Note these are mostly **disease names**; the material is usually referred to periphrastically ("rotted stem tissue", "the macerated zone", "the lesion margin"). That absence of a settled noun for the material is itself evidence that the ontologies have no term for it.

### Commonly but wrongly treated as the same thing

| Confused with | Why it is different |
|---|---|
| **root rot** (the disease) | A syndrome, with an aetiology and a host. The habitat is the tissue the syndrome leaves behind. Conflating them is exactly what BacDive's `Cat1 = #Infection` placement invites. |
| **rhizosphere** / **rhizoplane** | Soil and root-surface compartments. `ENVO:00005801`, `ENVO:01001181`. |
| **root endosphere** (healthy) | The compartment rot tissue *was*, before maceration. BacDive tracks `Endosphere` separately. |
| **plant litter** (`ENVO:01000628`) | Detached and fallen. Rot is in situ. |
| **necromass** (`ENVO:01001395`) | Asserts wholesale death; the advancing rot margin is living tissue. |
| **wood decay / white-rot / brown-rot** | Lignocellulose decay of dead woody substrate. BacDive keeps `#Rot fungi` as its own tag. |
| **compost / decomposing plant material** | Detached, aggregated, thermophilic, and not host-associated. |
| **spoiled produce** (`Spoiled`) | Postharvest food matrix. Overlaps for storage rots — the *P. polaris* tuber is precisely this edge case. |
| **wilt** (`habitatmech:BACDIVE.4c48b5114d`) | A whole-plant vascular symptom with **no localised material**; a stronger NOT_APPLICABLE candidate than rot. |
| **canker** (`habitatmech:BACDIVE.0f078d72a7`), **leaf spot** (`habitatmech:BACDIVE.31392c69b9`) | Sibling localised lesions on other organs, same open question. |
| **plant gall** (`PO:0025626`) | A *proliferative* disease structure — the plant builds new tissue. Rot is destructive. Opposite processes; the corpus already grounds gall here. |
| **root nodule** | Symbiotic, host-built, functional. Not a lesion. |

---

## 6. Should this be a term at all?

**Both dispositions are defensible and the choice is a policy call, not an evidence call. I recommend CONFIRM_UNGROUNDED plus a term request — for the intermediate class, not for this label.**

### The case for NOT_APPLICABLE

BacDive itself files this string under `Cat1 = #Infection`, alongside `Tuberculosis` (7 strains) and `Mycosis` (2) in the same corpus. "Root rot" and "stem rot" are, in ordinary phytopathological use, **disease names** — Han et al. define root rot as "a plant disease caused by various soil-borne pathogens". CLAUDE.md reserves NOT_APPLICABLE for "diseases, qualities, processes and procedures", and a disease name is the paradigm case. Decisively, BacDive already recorded the place separately: the *P. polaris* strain carries a `Host Body-Site → Plant → Root (Rhizome)` triplet. On this reading `#Rot (Root,Stem)` adds no locational information at all, and minting a habitat term for it duplicates the body-site facet.

### The case for a habitat term (what I recommend)

Rot tissue is not merely a disease label attached to an organ — it is a compartment with its own community, and the literature treats it as one. Kõiv et al. show a reproducible successional community in macerated tissue in which the pathogen is a *minority* by day 8; the *L. chuanxiong* design separates the rotten layer from the healthy layer of the same rhizome; lesion-margin sampling exists precisely because rotted and healthy tissue are different places. Sampling "root" and sampling "rotted root" do not return the same microbiota. And the corpus has already taken this route once: `Gall` — another Cat3 tag under `#Plant infections` — was disposed as an ENVO term request, and GOLD's `Galls` was grounded to `PO:0025626` *plant gall*, a disease-induced *structure*. Rot is the destructive counterpart of that proliferative structure.

The line I would draw across this whole BacDive cohort: **tags naming a localised material region are habitats (`Rot`, `Canker`, `Spot`, `Lesion`, `Gall`); tags naming a whole-plant physiological state are not (`Wilt`).**

### What to request

Not "Rot-Root,Stem". Request the organ-neutral intermediate class:

- **`rotted plant tissue`** (or `plant rot lesion`), genus `ENVO:01001121` *plant matter* — *"Plant matter which consists of the macerated, softened or necrotic tissue of a plant organ that is being decomposed in place by an invading plant-pathogenic microorganism."*
- Optionally an environment counterpart under `ENVO:01001057` *environment associated with a plant part or small plant*, which is currently childless.

Then this record is that class **restricted to root and stem** — expressible as the definition at the top, or, better, as the general class with `PO:0009005` and `PO:0009047` carried as `relation: xref` to record the organ scope BacDive asserted without HabitatMech asserting the disjunction is a natural kind. That xref treatment is also what keeps the leaf-spot sibling (`habitatmech:BACDIVE.31392c69b9`) from colliding on `PO:0009047` again — the two records would share a stem xref but sit under different lesion classes, which is the correct outcome and the one the original objection was reaching for.

### Two facts the curator should carry into whichever note they write

1. The concept's two attestations are both *Pectobacterium* — bacterial soft rot — so any note that generalises to fungal and oomycete root rots is generalising beyond the record's own evidence, even though the tag's scope plainly covers them.
2. The verified attesting strain came from a **potato tuber**, not a root or a stem. Do not write a note asserting the record's samples came from roots or stems.

## Citations

1. https://academic.oup.com/nar/article/47/D1/D631/5106998
2. https://bacdive.dsmz.de/isolation-sources
3. https://bacdive.dsmz.de/strain/158290
4. https://www.dsmz.de/catalogues/details/culture/DSM-105255.html
5. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2447502/
6. https://lms.su.edu.pk/lesson/1074/practical-isolation-of-plant-pathogenic-bacteria
7. https://www.annualreviews.org/content/journals/10.1146/annurev-phyto-080417-045906
8. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3678301/
9. https://bsppjournals.onlinelibrary.wiley.com/doi/full/10.1046/j.0032-0862.2001.Shorttitle.doc.x
10. https://www.annualreviews.org/doi/10.1146/annurev.py.18.090180.002045
11. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4484245/
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC11011919/
13. https://www.apsnet.org/publications/phytopathology/backissues/Documents/1983Abstracts/Phyto73_536.htm
14. https://peerj.com/articles/13808/
15. https://doi.org/10.3390/microorganisms13020417
16. https://doi.org/10.3390/genes15010021
17. https://peerj.com/articles/20369/
18. https://greenhouse.cornell.edu/pests-diseases/disease-factsheets/root-rot-diseases/
19. https://www.ndsu.edu/agriculture/extension/publications/canola-diseases-sclerotinia-stem-rot
20. https://ohioline.osu.edu/factsheet/plpath-soy-3
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC11830675/