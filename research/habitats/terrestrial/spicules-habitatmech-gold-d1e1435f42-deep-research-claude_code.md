---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T03:17:56.000268'
end_time: '2026-08-18T03:26:37.678611'
duration_seconds: 521.68
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Spicules
  habitat_identifier: habitatmech:GOLD.d1e1435f42
  habitat_category: TERRESTRIAL
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Environmental > Terrestrial > Deep subsurface > Cave > Spicules'
  assertions: '0'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Variant-match\
    \ review (#12): the variant route reaches UBERON:3010830 'spicule', which is animal\
    \ anatomy. The path is Terrestrial > Deep subsurface > Cave, where a spicule is\
    \ a mineral speleothem \u2014 a homonym across kingdoms of the kind that put Coral\
    \ on a fish. Path: Environmental > Terrestrial > Deep subsurface > Cave > Spicules\
    \ (source concept habitatmech:GOLD.d1e1435f42)"
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
  web_search_requests: 21
  num_turns: 38
  total_cost_usd: 3.9541364999999993
  session_id: 0627ea5a-17a5-42c0-9f60-9291cd632944
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 21
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Spicules
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.d1e1435f42
- **Category:** TERRESTRIAL
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Environmental > Terrestrial > Deep subsurface > Cave > Spicules
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Variant-match review (#12): the variant route reaches UBERON:3010830 'spicule', which is animal anatomy. The path is Terrestrial > Deep subsurface > Cave, where a spicule is a mineral speleothem — a homonym across kingdoms of the kind that put Coral on a fish. Path: Environmental > Terrestrial > Deep subsurface > Cave > Spicules (source concept habitatmech:GOLD.d1e1435f42)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Spicules** as a microbial habitat, with citations.

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

# Research report — HabitatMech novel term `habitatmech:GOLD.d1e1435f42` "Spicules"

**Source path:** Environmental > Terrestrial > Deep subsurface > Cave > Spicules · **Category:** TERRESTRIAL · **Grounding:** UNGROUNDED

---

## Proposed definition

> A **speleothem** which consists of macroscopic acicular crystals, most commonly of aragonite, precipitated subaerially from evaporating capillary or seepage films on cave wall surfaces and on coralloid nodules.

Genus term: `ENVO:00000327` *speleothem* — recommended as `parent_habitats` (relation `parent`), **not** as a grounding target, because *speleothem* is strictly broader (stalactites, flowstone, moonmilk are also speleothems).

If the curator prefers the habitat framing to be explicit in the sentence rather than inherited from the genus, the alternative is: *"A speleothem which consists of macroscopic acicular aragonite crystals grown by subaerial evaporation on cave surfaces, whose crystal faces and interstices are colonised by oligotrophic cave microbiota."* I recommend the shorter form — habitat-hood is inherited from `speleothem` ⊂ `cave`, and the second clause states something no source verifies *for spicules specifically* (see §4, Verification gaps).

---

## 1. What the concept denotes

**The reading the path supports: a needle-like secondary mineral growth on a cave surface — a speleothem morphotype.** The sample a microbiologist takes is the crystal material itself, scraped or broken from a cave wall, popcorn nodule, or helictite.

This is a documented, named feature in the cave-mineralogy literature, not an invented usage. Carol Hill's monograph on the Guadalupe Mountains caves (Carlsbad Cavern, Lechuguilla, and neighbours) uses "spicule" as a specific morphological stage in an evaporation-driven series:

> "Bushes of coralloidal calcite surround the Lake of the Clouds where the humidity is relatively high. Directly upslope from the Lake, the bushes grade into blunted aragonite spicules and then, higher upslope, delicate acicular-aragonite frostwork occurs."
> — Hill, C.A. (1987), *Geology of Carlsbad Cavern and Other Caves in the Guadalupe Mountains, New Mexico and Texas*, New Mexico Bureau of Mines and Mineral Resources Bulletin 117, Part II (Mineralogy), Carbonates. <https://npshistory.com/publications/geology/state/nm/1987-117/sec1-2.htm>

and again as an overgrowth phase on cave popcorn:

> "…the general sequence of popcorn deposition is rhombohedral calcite surrounded by nodular over-growths of spicular aragonite capped by blebs of hydromagnesite moonmilk on the tips of the aragonite spicules."
> — Hill (1987), same section.

The earliest recorded use is older still: Rowling's review of cave aragonite traces the term to 1887, "describing aragonite spicules depositing in a hollow on a helictite in Luray Cavern (U.S.A.)" (Rowling, J. (2004), *Studies on aragonite and its occurrence in caves, including New South Wales caves*, **Journal and Proceedings of the Royal Society of New South Wales** 137: 123–149, p. 124. <https://www.royalsoc.org.au/wp-content/uploads/2024/09/137_Rowling.pdf>).

### Boundary — what is inside and what is a neighbour

| | Relation to "Spicules" |
|---|---|
| **Inside** | Individual acicular crystal projections, chiefly aragonite; the "blunted aragonite spicules" morphology intermediate between nodular coralloid and delicate frostwork (Hill 1987); "spicular aragonite" overgrowths on popcorn nodules. |
| **Neighbour — the substrate** | *Coralloid / cave popcorn* — "a collective term used for a number of morphological varieties of **nodular** speleothems" (Hill 1987). Spicules grow *on* coralloids; the nodule is not the spicule. |
| **Neighbour — the fully developed form** | *Frostwork* — "the acicular, needle-like variety of aragonite **anthodite** that resembles cactus or thistle plants"; *anthodites* are "speleothems which consist of clusters of colorless to white, needle or quill-like, crystal **sprays**" (Hill 1987). Frostwork is delicate and radiating; spicules are blunter and earlier in the evaporation gradient. Whether a curator wants these as siblings or as a parent/child chain is a judgement call the sources do not settle. |
| **Neighbour — microscopic** | *Needle-fibre calcite (NFC)* in moonmilk: 1–2 µm needles plus sub-µm nanofibers forming a pasty deposit, a distinct thing at a distinct scale (Verrecchia & Verrecchia 1994; Cañaveras et al. 2006). |
| **Outside** | The cave wall or bedrock the spicules sit on (`ENVO:00002144` *cave wall*), and drip water. |

### The label is ambiguous — the readings

1. **Mineral spicule / speleothem morphotype** (recommended). Supported directly by the path, by Hill (1987) for exactly the kind of cave GOLD's "Deep subsurface > Cave" leaf covers, and by Rowling (2004).
2. **Sponge spicule (biogenic silica) in cave sediment.** Siliceous sponge spicules are a standard microfossil proxy in karst and cave-fill sediments, recovered by wet-sieving alongside phytoliths, foraminifera and ostracodes (e.g. van Hengstum et al., sea-level control of sedimentation in coastal caves and sinkholes, <https://www.whoi.edu/science/MCG/groundwater/pubs/PDF/vanHengstum.pdf>; Pantanal doline-sediment study, *Catena*, <https://www.sciencedirect.com/science/article/abs/pii/S0895981122002346>). **Argues against this reading:** GOLD "Specific Ecosystem" leaves name the material sampled for sequencing, and a sponge spicule assemblage is a paleoenvironmental proxy, not a sequencing substrate. It is also normally qualified ("sponge spicules"), whereas GOLD's bare "Spicules" sits directly under Cave.
3. **Lava-cave needle features.** I looked for this and found **no** source using "spicule" for a lava-tube feature; the lava-cave literature uses *coralloid*, *moonmilk*, *ooze*, *reticulated filaments* (Northup et al. 2011, *Astrobiology* 11(7):601–618, PMID 21879833; Hathaway et al. 2024, *Applied Sciences*, <https://doi.org/10.3390/app14156500>). Record this reading as **unsupported**, not merely disfavoured.

The curator note's diagnosis is confirmed and should be preserved: `UBERON:3010830` *spicule* is a homonym, not a match (see §5).

---

## 2. Genus — the broader kind

**Smallest well-established kind: *speleothem*.** An existing ontology term expresses it:

- **`ENVO:00000327` *speleothem*** — "A secondary mineral deposit formed in caves, most commonly calcite." (ENVO via OLS4: <https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00000327>)

This aligns with the discipline's own definition: in Hill & Forti a speleothem is a secondary mineral deposit formed by physico-chemical reaction from a primary mineral within the cave environment, classified **primarily on morphology** and secondarily on origin and crystallography (Hill, C.A. & Forti, P. (1995), *The classification of cave minerals and speleothems*, **International Journal of Speleology** 24: 77–82, <https://digitalcommons.usf.edu/ijs/vol24/iss1/5/>; Hill & Forti (1997), *Cave Minerals of the World*, 2nd ed., National Speleological Society, ISBN 1-879961-07-5).

### Near-misses in ENVO and why each fails

| Term | Why it is not a match |
|---|---|
| `ENVO:00000327` **speleothem** | **Broader**, not equivalent — this is the genus, correct as a parent. Its only ENVO children are `ENVO:00000330` stalagmite and `ENVO:00000331` stalactite, neither of which subsumes an acicular wall growth. |
| `ENVO:00002144` **cave wall** — "A solid surface layer which forms part of the boundary between the cavity of a cave." | Asserts the *bedrock boundary*, not a secondary deposit on it. A spicule is a precipitate that post-dates and sits on the wall. Adjacency, not identity or broader-than. |
| `ENVO:00000067` **cave** | Far too broad; the whole void, not a deposit within it. |
| `ENVO:00000323` **live cave** — "A cave containing a stream or active speleothems." | Asserts a property of the *cave*, and asserts activity. A sampled spicule may be relict. Wrong entity type. |
| `ENVO:00012411` **karst cave**, `ENVO:01000359` **limestone cave**, `ENVO:01000360` **solutional cave** | Assert a host-rock and speleogenetic mechanism the GOLD path does not claim. Also cave-level, not deposit-level. |
| `ENVO:00000331` **stalactite**, `ENVO:00000330` **stalagmite** | Sibling speleothem types with a different formation mode (drip-fed, gravity-oriented). Not broader. |

**No ENVO term exists for the intermediate class.** ENVO has no *coralloid*, *cave popcorn*, *anthodite*, *frostwork*, *moonmilk*, or *flowstone* (OLS4 searches for each returned nothing in ENVO; "moonmilk" returns only `NCBITaxon:1536899` *moonmilk metagenome*). So *speleothem* really is the smallest available genus, and the definition must carry the whole differentia in one step. Worth recording as an ENVO term-request opportunity: a **coralloid / evaporative speleothem** intermediate class would let *spicules*, *frostwork*, *anthodite* and *cave popcorn* share a parent.

---

## 3. Differentia — what distinguishes it from its siblings

Ordered by how directly a source states them.

**(a) Crystal habit: acicular, and macroscopic.** Directly stated — Hill (1987) contrasts "blunted aragonite spicules" against "delicate acicular-aragonite frostwork" and against "nodular" coralloids. This is the primary discriminator and the one the classification system is built on (morphology first — Hill & Forti 1995). *That the crystals are macroscopic (visible without magnification) is my inference from their being field-described and photographed in situ; no source I found gives a size range for spicules specifically.*

**(b) Dominant material: aragonite, not calcite.** Every use I located qualifies spicules as aragonite or "spicular aragonite" (Hill 1987; Rowling 2004; Dolley 1887 via Rowling). Aragonite's needle habit follows from its crystal structure, and its precipitation in preference to calcite is controlled by identifiable inhibitors: Rowling (2004) reports ferroan dolomite, calcite-inhibiting ions (magnesium, manganese, phosphate, sulfate, heavy metals), air movement and low humidity as the controls on aragonite deposition. Gypsum can also form acicular cave deposits, but those carry their own names (cave cotton, angel hair) rather than "spicule" in the sources I found.

**(c) Formation process: subaerial evaporation from capillary/seepage films, not drip-fed.** This is what separates spicules from stalactites and stalagmites, and it is measurable in the field as a **humidity/airflow gradient**. Hill (1987) documents the full transect at Carlsbad: coralloidal calcite bushes at the high-humidity lake margin → blunted aragonite spicules upslope → acicular frostwork higher still. This gradient is the single most useful curatorial fact in this report, because it makes the concept an observable position on a physical gradient rather than a vague morphological impression.

**(d) Substrate: an existing cave surface or nodule, not the cave floor or ceiling drip line.** Hill (1987) has spicular aragonite as "nodular over-growths" on rhombohedral calcite popcorn, itself later capped by hydromagnesite moonmilk — a documented three-mineral paragenetic sequence within a single nodule.

**(e) Characteristic physicochemistry as a habitat: oligotrophic, mineral-dominated, low-biomass.** Caves are "extremely oligotrophic settings with slow-growing microbial communities that rely on limited energy resources," and microorganisms there act as "agents of mineral precipitation and dissolution" (Jones, D.S. & Northup, D.E. (2021), *Cave Decorating with Microbes: Geomicrobiology of Caves*, **Elements** 17(2):107–112, doi:[10.2138/gselements.17.2.107](https://doi.org/10.2138/gselements.17.2.107)). *This is a property of cave speleothem habitats generally; I found no study that sampled objects called "spicules". Treat it as inherited from the genus, not as an attested property of this concept.*

### Why speleothem surfaces are sampled at all — supporting, but for neighbouring morphotypes

- Koning, K. *et al.* (2022), *Biomineralization in Cave Bacteria — Popcorn and Soda Straw Crystal Formations, Morphologies, and Potential Metabolic Pathways*, **Frontiers in Microbiology** 13:933388, doi:[10.3389/fmicb.2022.933388](https://doi.org/10.3389/fmicb.2022.933388). Sampled **popcorn** (coralloid) and soda-straw speleothems from Iron Curtain Cave, BC; 99 bacterial isolates, 11 urease-positive; novel *Sphingobacterium* sp. PCS056 and *Pseudarthrobacter* sp. SSS035; plus *Sporosarcina*, *Arthrobacter*, *Streptomyces*. Mechanism: ureolytic MICP — urease liberates carbonate, effluxed to the cell surface where it binds environmental calcium. **This is the closest published analogue to a spicule sample: popcorn is the substrate spicules grow on.**
- Metagenome analysis of speleothem microbiome, Borra caves, India, **Current Microbiology** (2023), doi:[10.1007/s00284-023-03431-9](https://doi.org/10.1007/s00284-023-03431-9) — core speleothem community dominated by Alpha-/Beta-/Gamma-Proteobacteria, Actinobacteria, Firmicutes, Bacteroidetes.
- Microbial diversity and mineralogical-mechanical properties of calcitic cave speleothems, **Frontiers in Microbiology** (2018), PMC5810276, <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5810276/> — significant phylum-level differences *between speleothem types*, with genus-level structure tracking geochemistry and mineralogy. Direct support for treating a distinct speleothem morphotype as a distinct habitat.
- Boston, P.J. *et al.* (2001), *Cave Biosignature Suites: Microbes, Minerals, and Mars*, **Astrobiology** 1:25–55, doi:[10.1089/153110701750137413](https://doi.org/10.1089/153110701750137413), PMID 12448994 — the framework under which cave mineral morphologies are sampled as candidate biosignatures.

---

## 4. Verification gaps — state these plainly on the record

Three things I could not confirm, and a definition should not silently imply any of them:

1. **The originating GOLD study is unidentified.** `gold.jgi.doe.gov/ecosystemtree` and `/ecosystem_classification` return HTTP 403 to automated fetch. NCBI BioSample `esearch` for `spicule AND cave` returns **0 records**. Combined with the record's **upstream assertion volume of 0**, it is possible this GOLD leaf carries no samples at all and is a curated-but-unpopulated path. That does not make the concept wrong, but it means *no microbial data attaches to it*, and the definition cannot cite community composition.
2. **"Spicule" is not one of Hill & Forti's 38 official speleothem types.** The 38 types run alphabetically from *anthodites* to *tubes*; I could not retrieve the full text of the 1995 classification paper (the USF Digital Commons PDF endpoint returned 403), so I cannot state whether "spicule" appears as a lower-rank *subtype* or *variety*. The honest characterisation from the evidence I do have: **"spicule" is descriptive usage in the primary literature (Hill 1987; Dolley 1887) rather than a formally sanctioned speleothem type name.** Verifying this needs a look at *Cave Minerals of the World* (2nd ed., 1997) glossary and coralloid chapter. Hill & Forti (1995) note that new speleothem types/subtypes/names are meant to be approved by a UIS Commission of cave mineralogists.
3. **No published microbiology of objects called "spicules".** Everything in §3(e) is inherited from speleothem/coralloid studies. Do not write a community composition into the definition.

---

## 5. Synonyms, and what NOT to conflate

### Names in real use for this concept
- **aragonite spicules** (Hill 1987; Rowling 2004 quoting Dolley 1887) — the fullest form
- **spicular aragonite** (Hill 1987) — the adjectival usage for the same material
- **acicular aragonite** (Hill 1987) — used both for spicules and for frostwork; ambiguous on its own
- **cave needles / needle speleothems** — informal; Hill (1987) Part II lists "needles" among less common speleothem shapes

### Related but distinct — do **not** treat as synonyms
| Term | Distinction |
|---|---|
| **frostwork** | The delicate, radiating, fully developed acicular anthodite variety; a *later/drier* stage on the same gradient (Hill 1987). |
| **anthodite** | Needle/quill-like crystal **sprays** in clusters; a formal Hill & Forti type. Spicules are individual projections, not sprays. |
| **coralloid / cave popcorn / knobstone** | The **nodular** substrate spicules grow on. Different morphology, and the collective term for nodular speleothems (Hill 1987). |
| **helictite** | Curving, gravity-defying; the surface Dolley's 1887 spicules grew *in*, not the spicules. |
| **cave cotton, angel hair, gypsum flowers** | Fibrous **sulfate** forms with their own names and their own formation route (sulfide/H₂S oxidation). |
| **needle-fibre calcite (NFC), moonmilk** | Micron-scale (1–2 µm needles, sub-µm nanofibers) within a pasty deposit, with a substantially argued microbial/fungal origin — Cañaveras et al. (2006) *Naturwissenschaften*, doi:[10.1007/s00114-005-0052-3](https://doi.org/10.1007/s00114-005-0052-3); Tomba degli Scudi moonmilk, **Scientific Reports** (2018), <https://www.nature.com/articles/s41598-018-34134-y>; Maciejewska et al. (2017), **Frontiers in Microbiology** 8:1181, <https://doi.org/10.3389/fmicb.2017.01181>. Hill (1987) puts hydromagnesite moonmilk *on the tips of* aragonite spicules — adjacent deposits, different concepts. |

### Homonyms — hard-block these
| | |
|---|---|
| `UBERON:3010830` **spicule** | No definition; imported from **amphibian_anatomy**, flagged in UBERON as needing compatibility checking. Animal anatomy. **This is the variant-match trap the curator note already caught (#12); the note is correct and should stand.** |
| `PORO:0000017` **spicule** | "Siliceous or calcareous entities forming sponge mineral skeleton." Sponge anatomy. Superficially seductive because sponge spicules *are* mineral and *do* occur in cave sediments — but as microfossils, not as a sequencing substrate (see §1, reading 2). |
| `CLAO:0001097`, `TGMA:0001362` **spicule** | Arthropod/crustacean cuticular projections. |
| `NCIT:C82998` **Spicule** | "A tiny, needle-like structure" — generic; also bone spicules, `HP:0007737` bone-spicule retinal pigmentation, `NCIT:C157670` spiculated nodule (radiology). |
| **solar spicules** | Solar physics. Irrelevant but a search-noise source. |

---

## 6. Should it be a term at all?

**Yes — but with a caveat worth recording in the notes.**

It qualifies. A spicule is a material entity with a location, a composition, and a formation process; it is the thing physically removed and extracted from; and it is the same *kind* of thing as popcorn and soda-straw speleothems, which have been sampled and sequenced (Koning et al. 2022). It is **not** a process, a quality, a disease state, an organism, or a sampling artefact, so `NOT_APPLICABLE` is wrong here — this is not a "Contamination"/`PATO:0001429` case.

**Recommended disposition:** term request, with `ENVO:00000327` *speleothem* as `parent_habitats` (`relation: parent` — genuinely broader). Do **not** ground to `ENVO:00000327` (too broad, and grounding would collapse spicules into stalactites and flowstone), and do **not** attach `UBERON:3010830` or `PORO:0000017` in any relation, including `xref` — they are homonyms of a different denotation, so even an xref would publish a false link.

**The caveat.** Two facts should temper enthusiasm: upstream assertion volume is **0**, and "spicule" appears to be descriptive rather than formally sanctioned speleothem nomenclature (§4.2). If the corpus later gains a `coralloid speleothem` or `evaporative speleothem` concept, *Spicules* is a strong candidate to be absorbed into it — the differentia separating spicules from frostwork is a position on a humidity gradient, which is a real distinction but a graded one, and Hill (1987) describes the two as endpoints of a single continuous transect. Flagging that now is cheaper than discovering it after the term is published.

---

## Sources

**Primary — cave mineralogy (the definitional core)**
- Hill, C.A. (1987) *Geology of Carlsbad Cavern and Other Caves in the Guadalupe Mountains, New Mexico and Texas*, New Mexico Bureau of Mines and Mineral Resources Bulletin 117. Part II Mineralogy → Carbonates: <https://npshistory.com/publications/geology/state/nm/1987-117/sec1-2.htm> · contents: <https://npshistory.com/publications/geology/state/nm/1987-117/contents.htm>
- Rowling, J. (2004) *Studies on aragonite and its occurrence in caves, including New South Wales caves*, **J. Proc. R. Soc. NSW** 137:123–149. <https://www.royalsoc.org.au/wp-content/uploads/2024/09/137_Rowling.pdf>
- Rowling, J. *Cave Aragonites of New South Wales* (thesis, Univ. of Sydney). <https://ses.library.usyd.edu.au/handle/2123/694>
- Hill, C.A. & Forti, P. (1995) *The classification of cave minerals and speleothems*, **Int. J. Speleology** 24:77–82. <https://digitalcommons.usf.edu/ijs/vol24/iss1/5/>
- Hill, C.A. & Forti, P. (1997) *Cave Minerals of the World*, 2nd ed., National Speleological Society. ISBN 1-879961-07-5.

**Cave geomicrobiology**
- Jones, D.S. & Northup, D.E. (2021) **Elements** 17(2):107–112. doi:[10.2138/gselements.17.2.107](https://doi.org/10.2138/gselements.17.2.107)
- Koning, K. *et al.* (2022) **Front. Microbiol.** 13:933388. doi:[10.3389/fmicb.2022.933388](https://doi.org/10.3389/fmicb.2022.933388)
- Boston, P.J. *et al.* (2001) **Astrobiology** 1:25–55. doi:[10.1089/153110701750137413](https://doi.org/10.1089/153110701750137413), PMID 12448994
- Northup, D.E. *et al.* (2011) **Astrobiology** 11(7):601–618. PMID 21879833
- Speleothem metagenome, Borra caves (2023) **Curr. Microbiol.** doi:[10.1007/s00284-023-03431-9](https://doi.org/10.1007/s00284-023-03431-9)
- Calcitic cave speleothem microbial diversity (2018) **Front. Microbiol.** <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5810276/>
- Jurado, V., Northup, D.E. & Saiz-Jimenez, C. (2024) Editorial: Microbial roles in caves. **Front. Microbiol.** doi:[10.3389/fmicb.2024.1411535](https://doi.org/10.3389/fmicb.2024.1411535)

**Moonmilk / needle-fibre calcite (the microscopic neighbour)**
- Cañaveras, J.C. *et al.* (2006) **Naturwissenschaften**. doi:[10.1007/s00114-005-0052-3](https://doi.org/10.1007/s00114-005-0052-3)
- Tomba degli Scudi moonmilk (2018) **Sci. Rep.** <https://www.nature.com/articles/s41598-018-34134-y>
- Maciejewska, M. *et al.* (2017) **Front. Microbiol.** 8:1181. <https://doi.org/10.3389/fmicb.2017.01181>

**Sponge-spicule (alternate reading)**
- van Hengstum, P.J. *et al.*, sea-level control of sedimentation in coastal caves and sinkholes. <https://www.whoi.edu/science/MCG/groundwater/pubs/PDF/vanHengstum.pdf>
- Pantanal doline pond sediments, **Catena** (2022). <https://www.sciencedirect.com/science/article/abs/pii/S0895981122002346>

**Ontology lookups (OLS4, EBI, retrieved 2026-08-18)**
- `ENVO:00000327` speleothem, `ENVO:00002144` cave wall, `ENVO:00000067` cave, `ENVO:00000323` live cave, `ENVO:00000330/331` stalagmite/stalactite — <https://www.ebi.ac.uk/ols4/ontologies/envo>
- `UBERON:3010830` spicule (amphibian_anatomy import, no definition), `PORO:0000017` spicule, `CLAO:0001097`, `TGMA:0001362`, `NCIT:C82998` — <https://www.ebi.ac.uk/ols4>
- GOLD ecosystem classification (403 to automated fetch; cited for the 5-level schema): <https://gold.jgi.doe.gov/ecosystem_classification>

## Citations

1. https://npshistory.com/publications/geology/state/nm/1987-117/sec1-2.htm
2. https://www.royalsoc.org.au/wp-content/uploads/2024/09/137_Rowling.pdf
3. https://www.whoi.edu/science/MCG/groundwater/pubs/PDF/vanHengstum.pdf
4. https://www.sciencedirect.com/science/article/abs/pii/S0895981122002346
5. https://doi.org/10.3390/app14156500
6. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00000327
7. https://digitalcommons.usf.edu/ijs/vol24/iss1/5/
8. https://doi.org/10.2138/gselements.17.2.107
9. https://doi.org/10.3389/fmicb.2022.933388
10. https://doi.org/10.1007/s00284-023-03431-9
11. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5810276/
12. https://doi.org/10.1089/153110701750137413
13. https://doi.org/10.1007/s00114-005-0052-3
14. https://www.nature.com/articles/s41598-018-34134-y
15. https://doi.org/10.3389/fmicb.2017.01181
16. https://npshistory.com/publications/geology/state/nm/1987-117/contents.htm
17. https://ses.library.usyd.edu.au/handle/2123/694
18. https://doi.org/10.3389/fmicb.2024.1411535
19. https://www.ebi.ac.uk/ols4/ontologies/envo
20. https://www.ebi.ac.uk/ols4
21. https://gold.jgi.doe.gov/ecosystem_classification