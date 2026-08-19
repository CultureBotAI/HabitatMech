---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T21:49:01.700981'
end_time: '2026-08-17T21:58:24.223205'
duration_seconds: 562.52
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Aquatic-plant
  habitat_identifier: habitatmech:BACDIVE.38260eea00
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Aquatic-plant'
  assertions: '66'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Grounding-cohort
    review (#62): was FOODON:03401156 ''50122200 - aquatic plants prepared/processed
    (gs1 gpc)'', a UNSPSC commodity code for prepared food. An aquatic plant as an
    isolation source is a living host, not a prepared foodstuff, and no term in the
    slice names it. (source concept habitatmech:BACDIVE.38260eea00)'
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
  web_search_requests: 19
  num_turns: 41
  total_cost_usd: 4.3884170000000005
  session_id: ca1edd30-7e1b-4d18-9256-19c73ef4eaf8
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 38
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Aquatic-plant
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.38260eea00
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Aquatic-plant
- **Upstream assertion volume:** 66
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Grounding-cohort review (#62): was FOODON:03401156 '50122200 - aquatic plants prepared/processed (gs1 gpc)', a UNSPSC commodity code for prepared food. An aquatic plant as an isolation source is a living host, not a prepared foodstuff, and no term in the slice names it. (source concept habitatmech:BACDIVE.38260eea00)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Aquatic-plant** as a microbial habitat, with citations.

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

# Research: **Aquatic-plant** (`habitatmech:BACDIVE.38260eea00`)

## Proposed definition

> An environmental system determined by an organism which is an aquatic macrophyte — a macroscopic photosynthetic organism that grows permanently or periodically submerged in, floating on, or emergent from a body of water.

ENVO-idiomatic variant, if the curator prefers to mirror the phrasing of `ENVO:01001001`/`ENVO:01001002`:
*"An environmental system determined by an aquatic macrophyte."* — with the macrophyte clause carried in an explanatory comment rather than the definition.

**Recommended disposition:** keep `CONFIRM_UNGROUNDED`, keep the minted identity, add `ENVO:01001000` as the genus/parent (see §2 for why *not* `ENVO:01001001`), and record the source's own targets as `relation: xref`. This is a term-request candidate: **"aquatic macrophyte-associated environment"**, sibling to `ENVO:01001179` *cnidarian-associated environment*, which is the precedent that ENVO does mint taxon-scoped `-associated environment` classes.

---

## 1. What the concept denotes

### 1.1 The source path, verified

The record carries no BacDive category path locally (`data/raw/bacdive_isolation_sources.tsv` holds only the leaf label), so I resolved it against BacDive itself. Three strains in this record's `characteristic_taxa` list carry the tag triplet explicitly:

| Strain (BacDive ID) | Isolation source text | Cat1 · Cat2 · Cat3 |
|---|---|---|
| *Marinirhabdus citrea* MEBiC09412ᵀ ([158685](https://bacdive.dsmz.de/strain/158685)) | "Seaweed collected at Yeonggwang County" | **Host · Plants · Aquatic plant** |
| *Rothia endophytica* DSM 26247 ([24206](https://bacdive.dsmz.de/strain/24206)) | "surface-sterilized healthy root of *Dysophylla stellata* (Lour.) Benth." | **Host · Plants · Aquatic plant** (plus body-site tags Plant, Root/Rhizome, Sterilized plant part) |
| *Erythrobacter longus* DSM 6997 ([5380](https://bacdive.dsmz.de/strain/5380)) | "seaweed, *Enteromorpha linza*" | **Plants · Aquatic plant** |

So the canonical path is **`#Host > #Plants > #Aquatic plant`**, a Cat3 leaf in BacDive's Microbial Isolation Source classification ([Reimer et al., *NAR* 2019, PMC6323973](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/)). Its Cat2 siblings in this corpus are `Herbaceous-plants-Grass,Crops`, `Tree`, `Moss`, `Root-Rhizome`, `Leaf-Phyllosphere`, `Sterilized-plant-part`, `Decomposing-plant`, `Plant-infections`, `Endosphere`. That placement is decisive for the reading: **BacDive files this under `#Host`, not under `#Environmental > #Aquatic`.** The concept is *the plant as a living host*, not the water body it grows in, and not a plantation or a wetland.

### 1.2 What a sample from this concept is

The thing sampled is **a living, macroscopic aquatic plant, or any part or surface of one** — leaf/frond, stem, root, rhizome, thallus — including both the **epiphytic biofilm** on the plant surface and the **endosphere** reached after surface sterilisation. The record's own strains span both routes: *Rothia endophytica* and *Maridesulfovibrio zosterae* were both isolated from **surface-sterilized roots** (endophytic), while *Erythrobacter longus* was recovered from the **surface** of a green seaweed ([Shiba & Simidu 1982](https://doi.org/10.1099/00207713-32-2-211); BacDive 5380).

### 1.3 The extension, read off the 59 attested taxa

The 66 strain assertions are ecologically heterogeneous in a way that matters for the boundary:

- **Marine angiosperms (seagrass).** *Maridesulfovibrio* (*Desulfovibrio*) *zosterae* DSM 11974 — "isolated from surface-sterilized roots of the seagrass *Zostera marina*" ([Nielsen, Liesack & Finster 1999, *IJSB* 49:859–865](https://doi.org/10.1099/00207713-49-2-859), PMID 10319511). *Kordia zosterae* ZO2-23ᵀ, from *Zostera marina* ([Kim et al. 2017, *IJSEM* 67:4790–4795](https://doi.org/10.1099/ijsem.0.002379), PMID 28984217). *Paraglaciecola hydrolytica* S66ᵀ, from eelgrass (*Zostera* sp.), Denmark ([Bech et al. 2017, *IJSEM* 67:2242–2247](https://doi.org/10.1099/ijsem.0.001933), PMID 28671532).
- **Macroalgae / seaweed.** *Marinirhabdus citrea* ([Yang et al. 2018, *IJSEM* 68:547–551](https://doi.org/10.1099/ijsem.0.002539)); *Erythrobacter longus* from the green alga *Enteromorpha linza* (now *Ulva linza*); *Agarivorans* sp. (agarolytic, seaweed-associated).
- **Freshwater / wetland vascular macrophytes and aquatic crops.** *Rothia endophytica* from *Dysophylla stellata*, a wetland herb ([Xiong et al. 2013, *IJSEM* 63:3964–3969](https://doi.org/10.1099/ijs.0.052522-0), PMID 23710050). *Xanthomonas nasturtii* and *X. floridensis* from watercress, *Nasturtium officinale* ([Vicente et al. 2017, *IJSEM* 67:3645–3654](https://doi.org/10.1099/ijsem.0.002189), PMID 28840805). *Peteryoungia* (*Rhizobium*) *ipomoeae* shin9-1ᵀ from a water-convolvulus (*Ipomoea aquatica*) field ([Sheu et al. 2016, *IJSEM* 66:1633–1640](https://doi.org/10.1099/ijsem.0.000875), PMID 26739022).

Two caveats I could not resolve and which the curator should not paper over:

1. **The five *Myxococcus xanthus* / *M. fulvus* / *Corallococcus coralloides* strains (9 of 66 assertions) are unverified by me.** Myxobacteria are typically recovered from decaying plant material, bark and soil; if BacDive tagged decaying reed or litter as "Aquatic plant", part of this bin is *dead* plant material and belongs conceptually with `Decomposing-plant`, not with a living host. This is my inference from the genera, not something a source states.
2. *Peteryoungia ipomoeae* was isolated from **water in a water-spinach field**, not from the plant itself (Sheu et al. 2016) — a sampling-site tag rather than a host tag. At least one assertion is therefore about the surrounding water, not the plant.

### 1.4 Ambiguity in the label

"Aquatic plant" has two readings in general usage, and BacDive's data settles which one is meant:

- **(a) Strict botanical reading** — an aquatic *vascular* plant (angiosperm/fern), excluding algae and bryophytes.
- **(b) Limnological "macrophyte" reading** — any macroscopic aquatic photosynthetic organism: vascular plants, bryophytes, charophytes and macroalgae.

**The data means (b).** Two of the three strains whose tags I verified came from seaweed, and *Erythrobacter longus*'s source is a green macroalga. Reading (a) would exclude them. The canonical limnological definition matches (b) exactly: aquatic macrophytes are *"aquatic photosynthetic organisms, large enough to see with the naked eye, that actively grow permanently or periodically submerged below, floating on, or growing up through the water surface"*, spanning seven divisions including Cyanobacteria, Chlorophyta, Rhodophyta, Xanthophyta, Bryophyta, Pteridophyta and Spermatophyta ([Chambers, Lacoul, Murphy & Thomaz 2008, *Hydrobiologia* 595:9–26](https://doi.org/10.1007/s10750-007-9154-6)).

### 1.5 Boundary — inside vs. neighbouring

**Inside:** living aquatic macrophytes of any growth form (submerged, floating-leaved, free-floating, emergent) in fresh, brackish or marine water; their surfaces and their internal tissues; wild and cultivated (watercress, water spinach) alike.

**Neighbouring concepts, outside:**

| Neighbour | Why it is outside |
|---|---|
| `ENVO:01000059` sea grass bed / `ENVO:01000058` kelp forest | The *place* the plants form — an ecosystem/water-body region. This concept is the plant itself. GOLD attests the bed separately (`Environmental > Aquatic > Marine > Intertidal zone > Seagrass bed`). |
| BacDive `Decomposing-plant` (→ `ENVO:01000628` plant litter) | Dead plant material. `#Host` requires a living host. |
| BacDive `Moss`, `Leaf-Phyllosphere`, `Root-Rhizome` | Cat3 siblings; a moss or a leaf is not by itself aquatic, and the plant-part bins are cross-cutting rather than aquatic. |
| GOLD `Environmental > Aquatic > Marine > Seaweed` (69 assertions) | Filed by GOLD under *Environmental*, not host-associated — the same physical stuff, differently framed. A plausible future co-attestor, but merging it would silently adopt GOLD's environmental framing. |
| `ENVO:03605003` epiphyton | The periphyton growing *on* the plant — the microbial community, not the habitat-determining plant. |
| Aquaculture ponds, paddy fields (`Paddy-Ricefield`), constructed wetlands | Water bodies and facilities that *contain* macrophytes. |

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001000` "environmental system determined by an organism"** — *"An environmental system which is determined by a living organism."* Present in the vendored slice (`data/raw/ontology_terms.tsv`), and the corpus already grounds BacDive's top-level `#Host` bin to it (`habitatmech:BACDIVE.baf38460e6`, `GROUND … EXACT`). It is unambiguously broader than this concept under either reading of §1.4.

### Near-misses, and why each fails

**`ENVO:01001001` plant-associated environment** — *"An environmental system determined by a green plant."* This is the obvious candidate and is the corpus's usual answer for plant hosts (`habitatmech:GOLD.1b21002a97` EXACT; `habitatmech:BACDIVE.d3209b6b2d` BROAD). **It fails here on a logical axiom, not a wording quibble.** OLS shows `ENVO:01001001` is *equivalent* to `environmental system and determined by some Viridiplantae (NCBITaxon:33090)`, with exact synonym "Viridiplantae-associated environment". Viridiplantae covers green algae — so *Ulva/Enteromorpha* and *Chara* are in — but **excludes Rhodophyta and Phaeophyceae**. BacDive's bin demonstrably contains strains whose source is recorded only as "a seaweed" (*Marinirhabdus citrea*), and seaweed is explicitly polyphyletic across red, green and brown algae (`FOODON:03412266`). Asserting `ENVO:01001001` as identity *or* as parent therefore claims Viridiplantae membership the source never asserts, for an unknown fraction of the 66 strains. That is the same over-claim pattern as the *anthropogenic contamination feature* case (#99). If the curator wants it recorded, `relation: xref` is the honest slot; if curation later narrows the concept to vascular macrophytes only, `ENVO:01001001` becomes a legitimate `GROUND_AS_PARENT`.

**`ENVO:01001057` environment associated with a plant part or small plant** — *"An environmental system determined by part of a living or dead plant, or a whole small plant."* Used twice in this corpus for BacDive plant bins (`Root-Rhizome`, `Sterilized-plant-part`). Fails as genus for the same Viridiplantae reason, and additionally on scope: this concept is not restricted to *parts* or to *small* plants (a *Zostera* meadow plant or *Typha* is neither), while it does include duckweed and epiphytic sampling of whole small plants. It is a partial overlap, not a genus.

**`ENVO:03605003` epiphyton** — *"Periphyton colonizing surface of aquatic plants."* In the slice, and the only ENVO term whose text mentions aquatic plants. It denotes the **colonising community**, not the plant that determines the habitat; grounding here would swap the habitat for its inhabitants. Also silently drops the endosphere isolates (*Rothia endophytica*, *M. zosterae*), which are explicitly *not* epiphytic.

**`ENVO:01001032` environment determined by a biofilm on a plant surface** — narrower (biofilm-only, again drops endophytes) and asserts biofilm formation the source does not.

**`FOODON:03401156` "50122200 – aquatic plants prepared/processed (gs1 gpc)"** — the term the seeder originally matched lexically, and correctly rejected: a GS1/UNSPSC commodity code for a processed foodstuff. The whole FOODON `aquatic plants prepared/processed` family (`03401156`–`03401163`) is commodity classification, and asserts human food use of every strain's host, which is false for *Zostera* and *Myriophyllum*.

**`FOODON:03412266` seaweed** — *"A macroscopic, multicellular, marine algae…"*. Covers roughly half the bin and excludes every vascular macrophyte; narrower on one axis and marine-only on another. Worth an xref at most.

**`PO:0000003` whole plant`/ `BTO:0001461` whole plant / `BTO:0001481` plant / `NCIT:C14258` Plant** — these name the *organism*, not a place. This is precisely the line CLAUDE.md draws after #114/#112: a host's *parts* ground to the anatomy term; the *whole host organism* does not. It keeps its own minted identity and carries the organism term as `relation: xref`.

**`ENVO:01001253` freshwater macrophyte farming process / `ENVO:01001252` seaweed farming process** — processes, not habitats; and both assert human cultivation.

**No ENVO term exists for** "aquatic plant", "macrophyte" (as a material or environment), "algae-associated environment", or "phyllosphere" (OLS returns nothing in ENVO for `phyllosphere`; the only hits are GOLD's own path node and NCBITaxon strain names).

---

## 3. Differentia — what distinguishes it

Under the genus `environmental system determined by an organism`, the siblings are animal-, fungi-, plant- and cnidarian-associated environments. Within the plant/algal side, what separates *this* concept from terrestrial plant hosts:

1. **The determining organism is submerged, floating or emergent in a water body.** This is the definitional differentia and is observable: growth form is the standard macrophyte classification axis (emergent, floating-leaved, free-floating, submerged, amphibious) ([Chambers et al. 2008](https://doi.org/10.1007/s10750-007-9154-6)).
2. **The colonisable surface is continuously water-bathed, and the community on it is compositionally distinct from the surrounding water.** Epiphytic bacterial communities on submerged macrophytes differ from the bacterioplankton of the same water, and differ between host species: a metagenomic survey of six submerged macrophytes (*Ceratophyllum demersum*, *Hydrilla verticillata*, *Myriophyllum verticillatum*, *Potamogeton lucens*, *Stuckenia pectinata*, *Najas marina*) recovered 149 phyla / 3,312 genera / 27,336 species, with 94–303 species endemic to each host species ([Wang et al. 2024, *Microbial Ecology* 87:37](https://doi.org/10.1007/s00248-024-02346-7), PMID 38286834). Host identity, plant part and water body each contribute: *"distinct plant species, plant part and habitat specific differences … support the combined impact of substrate (plant) and habitat on epiphytic bacterial community composition"* ([Hempel et al. 2008, *BMC Microbiology* 8:58](https://doi.org/10.1186/1471-2180-8-58), PMID 18402668).
3. **A steep, plant-generated redox gradient at the root/rhizome interface.** Radial oxygen loss from aerenchyma injects O₂ into otherwise anoxic sediment: on *Zostera marina* roots, surface O₂ reaches 19–80 % of air saturation in light within 1–2 mm of the root tip and falls to 0–5 % just 3–6 mm behind the apex ([Jensen et al. 2005, *Mar Ecol Prog Ser* 293:49–58](https://doi.org/10.3354/meps293049)); in *Typha angustifolia*, diffusion is confined to a 1–5 cm band behind the tip, and root sections with active O₂ diffusion carry higher rhizoplane bacterial and archaeal 16S abundance ([Vila-Costa et al. 2020, *Sci Rep* 10:15694](https://doi.org/10.1038/s41598-020-72653-9), PMC7518425). This is what puts strictly anaerobic sulfate reducers (*Maridesulfovibrio zosterae*, *Desulfofaba hansenii*) and iron reducers (*Geobacter*, *Geomobilimonas*) in the same record as aerobic surface flavobacteria.
4. **Carbon supply is host-derived and includes algal/plant structural polysaccharides.** Strains from this bin are characterised by hydrolysis of seaweed polysaccharides — *Paraglaciecola hydrolytica* grows on agar, agarose, porphyran, κ-carrageenan, alginate and laminarin as sole carbon sources (Bech et al. 2017).
5. **Salinity is not a differentia here — it varies within the concept.** The bin spans marine (*Zostera*, seaweed), brackish and freshwater (*Myriophyllum*, watercress) hosts, so any definition that fixes salinity would be wrong.
6. **Convergence with terrestrial phyllosphere is real and limits how "aquatic" the differentia can be pushed.** Duckweed was found to host *"a taxonomically similar bacterial assemblage as the terrestrial leaf microbiome"* ([Acosta et al. 2020, *PLoS ONE* 15(1):e0228560](https://doi.org/10.1371/journal.pone.0228560), PMC7004381). The differentia should therefore rest on the *setting of the host* (in/on water), which is observable, rather than on a claimed distinctive microbiota.

---

## 4. Sources

**Ontology / vocabulary**

- ENVO `ENVO:01001000`, `ENVO:01001001` (with its Viridiplantae equivalence axiom), `ENVO:01001057`, `ENVO:01001179`, `ENVO:03605003`, `ENVO:01000059`, `ENVO:01001032` — https://www.ebi.ac.uk/ols4/ontologies/envo (accessed 17 Aug 2026); all except `ENVO:01001179`/`ENVO:03605003`-adjacent terms are present in `data/raw/ontology_terms.tsv`.
- FOODON `FOODON:03401156`–`03401163` (GS1 GPC aquatic-plant commodity codes), `FOODON:03412266` seaweed — https://www.ebi.ac.uk/ols4/ontologies/foodon
- BacDive isolation-source classification and strain records: Reimer LC et al., "BacDive in 2019", *Nucleic Acids Res* 47:D631–D636, https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/ ; strain pages https://bacdive.dsmz.de/strain/158685, /24206, /5380 (accessed 17 Aug 2026).

**Habitat definition and ecology**

- Chambers PA, Lacoul P, Murphy KJ, Thomaz SM (2008) Global diversity of aquatic macrophytes in freshwater. *Hydrobiologia* 595:9–26. https://doi.org/10.1007/s10750-007-9154-6
- Wetzel RG (1983/2001) *Limnology* — origin of the periphyton/epiphyton substrate-based terminology; secondary summary: Frontiers in Microbiology 11:1275 (2020), https://doi.org/10.3389/fmicb.2020.01275
- Wang X et al. (2024) *Microbial Ecology* 87:37. https://doi.org/10.1007/s00248-024-02346-7
- Hempel M, Blume M, Blindow I, Gross EM (2008) *BMC Microbiology* 8:58. https://doi.org/10.1186/1471-2180-8-58
- Jensen SI, Kühl M, Glud RN, Jørgensen LB, Priemé A (2005) Oxic microzones and radial oxygen loss from roots of *Zostera marina*. *Mar Ecol Prog Ser* 293:49–58. https://doi.org/10.3354/meps293049
- Vila-Costa M et al. (2020) *Scientific Reports* 10:15694. https://doi.org/10.1038/s41598-020-72653-9
- Acosta K et al. (2020) *PLoS ONE* 15(1):e0228560. https://doi.org/10.1371/journal.pone.0228560
- Zhang Y et al. (2024) Rhizosphere and seawater microbiome of *Zostera marina*. *Microbiome* 12:34. https://doi.org/10.1186/s40168-024-01759-3

**Species descriptions used as extension evidence**

- Nielsen JT, Liesack W, Finster K (1999) *IJSB* 49:859–865. https://doi.org/10.1099/00207713-49-2-859 (PMID 10319511)
- Kim DI et al. (2017) *IJSEM* 67:4790–4795. https://doi.org/10.1099/ijsem.0.002379 (PMID 28984217)
- Bech PK et al. (2017) *IJSEM* 67:2242–2247. https://doi.org/10.1099/ijsem.0.001933 (PMID 28671532)
- Yang SH et al. (2018) *IJSEM* 68:547–551. https://doi.org/10.1099/ijsem.0.002539
- Xiong Z et al. (2013) *IJSEM* 63:3964–3969. https://doi.org/10.1099/ijs.0.052522-0 (PMID 23710050)
- Vicente JG, Rothwell S, Holub EB, Studholme DJ (2017) *IJSEM* 67:3645–3654. https://doi.org/10.1099/ijsem.0.002189 (PMID 28840805)
- Sheu SY et al. (2016) *IJSEM* 66:1633–1640. https://doi.org/10.1099/ijsem.0.000875 (PMID 26739022)

**Explicitly my inference, not sourced:** (i) that the *Myxococcus*/*Corallococcus* assertions in this bin may derive from decaying rather than living aquatic plants; (ii) that GOLD's `Environmental > Aquatic > Marine > Seaweed` path is a candidate co-attestor for the same physical material; (iii) the boundary table in §1.5, which is a reading of the source hierarchy rather than a statement any publication makes.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**

- aquatic macrophyte / macrophyte (the dominant term in limnology; the closest thing to a standard name)
- hydrophyte (botanical; strictly the adaptive plant type)
- water plant, aquatic vegetation (informal)
- submerged / floating-leaved / free-floating / emergent macrophyte (growth-form subtypes, all within the concept)
- seagrass, seaweed, duckweed, watercress, water spinach (species-level instances attested in this record)
- helophyte (emergent marsh subtype)

**Commonly but wrongly treated as the same thing**

| Confusable | Why it differs |
|---|---|
| **Epiphyton / periphyton / Aufwuchs** | The microbial-algal film *on* the macrophyte. `ENVO:03605003` is this, not the plant. Epiphyton is the *inhabitant*; the plant is the *habitat*. |
| **Seagrass bed / kelp forest / macrophyte stand** | The ecosystem or water-body region. `ENVO:01000059`, `ENVO:01000058`. |
| **Phytoplankton / microalgae** | Microscopic and suspended; explicitly excluded — "macrophyte" exists to draw exactly this line. |
| **"Aquatic plants (prepared/processed)"** (GS1/FOODON) | A food-commodity class. Already rejected once on this record; do not let a lexical re-match reinstate it. |
| **Wetland / marsh / swamp / paddy field** | Ecosystems *containing* macrophytes (`ENVO:00000035`, BacDive `Wetland-Swamp`, `Paddy-Ricefield`). A sample from a marsh is not a sample from a plant. |
| **Decomposing plant material / plant litter** | `ENVO:01000628`; BacDive keeps `Decomposing-plant` as a separate Cat3 bin. |
| **Aquatic-plant *rhizosphere sediment*** | Sediment, grounded via `ENVO:00005801` rhizosphere / sediment terms. Several published "macrophyte microbiome" studies sample sediment, not plant. |
| **`Aquaculture`, `Plant-Factory`** | Facilities. Note `Plant-Factory` in this corpus is the *industrial* sense of "plant" (`habitatmech:BACDIVE.b938cdfb88`) — an unrelated homonym in the same source vocabulary. |

---

## 6. Should this be a term at all?

**Yes.** It survives every disqualifier the corpus uses:

- It is not a **process** (contrast `ENVO:01001253` freshwater macrophyte farming process), not a **quality**, not a **disease state**, not a **medical procedure**. `NOT_APPLICABLE` is the wrong disposition and would be barred anyway by `tests/test_decisions.py`, since the natural xref target is an organism term.
- It is not a **taxon term**. The concept names *an organism acting as a host* — where the microbe lives — which CLAUDE.md and the #114 reversal establish **is** a habitat. What is not a habitat is the taxonomic class of aquatic plants; that stays in `relation: xref`.
- It is not a **sampling artefact**. 66 strain assertions across 59 taxa, spanning marine seagrass, macroalgae and freshwater vascular macrophytes, with a coherent physical setting and a mechanistically distinct microbiology (§3). The bin is real, and BacDive's own curators tag it as a host.

**Two honest caveats for the term request:**

1. **The name should probably be "aquatic macrophyte-associated environment", not "aquatic plant-associated environment."** The extension includes non-Viridiplantae macroalgae, so "plant" in the ENVO sense (= Viridiplantae, per the `ENVO:01001001` equivalence axiom) would be a misnomer for part of it. "Macrophyte" is the term that actually covers what the data holds, and it has a citable standard definition (Chambers et al. 2008).
2. **If a curator instead narrows the concept to vascular aquatic plants**, the report changes in exactly one way: `ENVO:01001001` becomes a defensible `GROUND_AS_PARENT` (`NARROW`), the definition's genus becomes "A plant-associated environment which …", and the seaweed strains need to be re-homed — but there is no ENVO or FOODON `-associated environment` term for macroalgae either, so that split creates a second unnamed concept rather than resolving one. **I recommend against the split**: keep the macrophyte reading, which is what the source data actually asserts.

**Sources:** [Chambers et al. 2008, *Hydrobiologia*](https://link.springer.com/article/10.1007/s10750-007-9154-6) · [Wang et al. 2024, *Microbial Ecology*](https://pmc.ncbi.nlm.nih.gov/articles/PMC10824801/) · [Hempel et al. 2008, *BMC Microbiology*](https://pmc.ncbi.nlm.nih.gov/articles/PMC2386815/) · [Vila-Costa et al. 2020, *Sci Rep*](https://www.nature.com/articles/s41598-020-72653-9) · [Jensen et al. 2005, *MEPS*](https://www.researchgate.net/publication/230558400_Oxic_microzones_and_radial_oxygen_loss_from_roots_of_Zostera_marina) · [Acosta et al. 2020, *PLoS ONE*](https://pmc.ncbi.nlm.nih.gov/articles/PMC7004381/) · [Zhang et al. 2024, *Microbiome*](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-024-01759-3) · [Nielsen et al. 1999, *IJSB*](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-49-2-859) · [Kim et al. 2017, *IJSEM*](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.002379) · [Bech et al. 2017, *IJSEM*](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.001933) · [Yang et al. 2018, *IJSEM*](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.002539) · [Xiong et al. 2013, *IJSEM*](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.052522-0) · [Vicente et al. 2017, *IJSEM*](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.002189) · [Sheu et al. 2016, *IJSEM*](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.000875) · [Reimer et al. 2019, *NAR*](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/) · [BacDive strain 158685](https://bacdive.dsmz.de/strain/158685) · [BacDive strain 24206](https://bacdive.dsmz.de/strain/24206) · [BacDive strain 5380](https://bacdive.dsmz.de/strain/5380) · [Frontiers in Microbiology 2020, periphyton](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2020.01275/full) · [EBI OLS4](https://www.ebi.ac.uk/ols4/)

## Citations

1. https://bacdive.dsmz.de/strain/158685
2. https://bacdive.dsmz.de/strain/24206
3. https://bacdive.dsmz.de/strain/5380
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/
5. https://doi.org/10.1099/00207713-32-2-211
6. https://doi.org/10.1099/00207713-49-2-859
7. https://doi.org/10.1099/ijsem.0.002379
8. https://doi.org/10.1099/ijsem.0.001933
9. https://doi.org/10.1099/ijsem.0.002539
10. https://doi.org/10.1099/ijs.0.052522-0
11. https://doi.org/10.1099/ijsem.0.002189
12. https://doi.org/10.1099/ijsem.0.000875
13. https://doi.org/10.1007/s10750-007-9154-6
14. https://doi.org/10.1007/s00248-024-02346-7
15. https://doi.org/10.1186/1471-2180-8-58
16. https://doi.org/10.3354/meps293049
17. https://doi.org/10.1038/s41598-020-72653-9
18. https://doi.org/10.1371/journal.pone.0228560
19. https://www.ebi.ac.uk/ols4/ontologies/envo
20. https://www.ebi.ac.uk/ols4/ontologies/foodon
21. https://doi.org/10.3389/fmicb.2020.01275
22. https://doi.org/10.1186/s40168-024-01759-3
23. https://link.springer.com/article/10.1007/s10750-007-9154-6
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC10824801/
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC2386815/
26. https://www.nature.com/articles/s41598-020-72653-9
27. https://www.researchgate.net/publication/230558400_Oxic_microzones_and_radial_oxygen_loss_from_roots_of_Zostera_marina
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC7004381/
29. https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-024-01759-3
30. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-49-2-859
31. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.002379
32. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.001933
33. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.002539
34. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.052522-0
35. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.002189
36. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.000875
37. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2020.01275/full
38. https://www.ebi.ac.uk/ols4/