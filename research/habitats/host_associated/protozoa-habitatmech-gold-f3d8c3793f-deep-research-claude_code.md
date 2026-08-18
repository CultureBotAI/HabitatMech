---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T22:26:31.256274'
end_time: '2026-08-17T22:35:44.065049'
duration_seconds: 552.81
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Protozoa
  habitat_identifier: habitatmech:GOLD.f3d8c3793f
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Protozoa'
  assertions: '32'
  parent_terms: ENVO:01001000
  xrefs: NCIT:C77916
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term NCIT:C77916 'Protozoa' attached as a parent. Host-taxon reversal\
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
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.f3d8c3793f)"
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
  num_turns: 43
  total_cost_usd: 3.364178
  session_id: 7e4d29c7-dd81-4834-847f-61d1b89a0442
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 31
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Protozoa
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.f3d8c3793f
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Protozoa
- **Upstream assertion volume:** 32
- **Nearest broader term already on the record:** ENVO:01001000
- **Cross-references upstream suggested:** NCIT:C77916

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term NCIT:C77916 'Protozoa' attached as a parent. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.f3d8c3793f)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Protozoa** as a microbial habitat, with citations.

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

# Protozoa (`habitatmech:GOLD.f3d8c3793f`) — novel-term definition research

> **An environmental system determined by a protozoan — a unicellular heterotrophic eukaryote — whose cell surface, cytoplasm, food vacuoles and nuclei are the space inhabited by the microorganisms sampled from it.**

If the curator wants the minimal ENVO-pattern form, drop everything after the em dash: *"An environmental system determined by a protozoan."* That matches `ENVO:01001001` / `ENVO:01001002` / `ENVO:01001041` word-for-word in shape, but it inherits the taxon's ambiguity (§1) rather than resolving it, so I recommend the longer form above.

---

## 1. What the concept denotes

**The place is a single protozoan cell.** In GOLD's five-level scheme (Ecosystem → Ecosystem Category → Ecosystem Type → Ecosystem Subtype → Specific Ecosystem), level 2 under `Host-associated` is *the host organism* — the slot occupied by "Human", "Plants", "Mammals" ([Mukherjee et al. 2019, *NAR* 47:D649–D659, doi:10.1093/nar/gky977](https://doi.org/10.1093/nar/gky977); [PMC6323969](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323969/)). `Host-associated > Protozoa` therefore denotes *a protozoan acting as host*: the microorganisms in the record were isolated **from** protozoan cells.

The repository's own raw inventory (`data/raw/gold_ecosystem_paths.tsv`) fixes the reading and its neighbourhood:

| GOLD path | depth | organism assertions |
|---|---|---|
| `Host-associated > Protozoa` | 2 (category) | **32** |
| `Host-associated > Protozoa > Myzozoa` | 3 | 0 |
| `Host-associated > Protozoa > Oxymonads` | 3 | 0 |
| `Host-associated > Protozoa > Sporozoa` | 3 | 0 |
| `Host-associated > Protists` (sibling category) | 2 | 40 |
| `Host-associated > Amoebozoa` (sibling category) | 2 | 13 |
| `Host-associated > Ciliophora` (sibling category) | 2 | 0 |
| `Host-associated > Protists > {Dinoflagellates, Ciliates, Amoebozoa, Excavata, Rhizaria, Nanoflagellates, Oomycetes, Breviatea}` | 3–5 | 18 total |

The three children are **host taxa**, not sample materials — which is what a host slot predicts, and is the strongest evidence for the reading. All three are empty, so the 32 assertions sit on the bare category: submissions that recorded "the host is a protozoan" without saying which.

**Inside the concept** — the protozoan cell considered as living space, in all the positions the literature documents for its occupants:

- the **cell surface** (ectosymbionts/epibionts),
- the **cytoplasm**, free or inside host-derived membranes,
- the **food vacuole / phagosome**, which is also the entry route,
- the **nuclear apparatus** — *Holospora* spp. grow exclusively inside the macronucleus of *Paramecium caudatum* and are expelled if injected there without passing through the digestive vacuole first ([Fokin & Görtz 2009, *Endosymbionts in Paramecium*, Microbiology Monographs 12:161–201, doi:10.1007/978-3-540-92677-1_7](https://doi.org/10.1007/978-3-540-92677-1_7); [Fokin 2022, *J Eukaryot Microbiol* 69:e12886, doi:10.1111/jeu.12886](https://doi.org/10.1111/jeu.12886)),
- association with **hydrogen-producing organelles** (hydrogenosome; and the newly described hydrogenobody of rumen ciliates — [Xie et al. 2026, *Science*, doi:10.1126/science.adv4244](https://doi.org/10.1126/science.adv4244), PMID 42060748, published 30 April 2026).

Husnik et al. describe exactly this range for prokaryotic symbionts of protists: most in the cytoplasm, "some are surrounded by host-derived membranes, some associate with mitochondria…, some colonize the outer surface in orderly arrangements, and some have invaded the host nuclear apparatus" ([Husnik et al. 2021, *Curr Biol* 31:R862–R877, doi:10.1016/j.cub.2021.05.049](https://doi.org/10.1016/j.cub.2021.05.049)).

**Outside the concept (neighbouring concepts):**

- **The rumen, the termite hindgut, the human vagina.** These are the *animal's* habitat, and GOLD files them under its animal categories. A methanogen inside a rumen ciliate is in a protozoan habitat nested inside an animal habitat; a methanogen free in rumen fluid is not.
- **Algae / phototrophic protists.** GOLD keeps `Host-associated > Algae` (394 assertions) as a separate category, and `Protists > Nanoflagellates > Autotrophic (ANF)` as a separate branch. The traditional protozoa/algae split is heterotrophy vs. phototrophy.
- **Fungi.** Separate GOLD category and an existing ENVO term (`ENVO:01001041`).
- **Protozoal disease** (malaria, amoebiasis, trichomoniasis). A disease is not a place — `NOT_APPLICABLE` territory in this corpus.
- **The protozoan as prey/grazer.** Protozoan predation structuring a soil or water community is a *process*; the sample there is soil or water.

### The label is ambiguous — three readings, none of them silently picked

1. **Traditional broad reading: "unicellular eukaryotes that are not plants, algae or fungi"** — i.e. heterotrophic protists. This is the NCIt definition attached to the record's own xref: NCIT:C77916 *Protozoa*, "Unicellular heterotrophic eukaryote in the kingdom protista" (verified via [OLS4](https://www.ebi.ac.uk/ols4/ontologies/ncit/classes?obo_id=NCIT:C77916)).
2. **Formal kingdom Protozoa** *sensu* Cavalier-Smith, retained in the seven-kingdom consensus classification used by Catalogue of Life: "unicellular eukaryotes, usually called protists, [that] comprise a polyphyletic group of eukaryotes that do not undergo tissue formation" — the authors explicitly concede it is paraphyletic and defend it as a practical grouping ([Ruggiero et al. 2015, *PLoS ONE* 10:e0119248, doi:10.1371/journal.pone.0119248](https://doi.org/10.1371/journal.pone.0119248); [PMC4418965](https://pmc.ncbi.nlm.nih.gov/articles/PMC4418965/)). This kingdom includes euglenids (photosynthetic) and excludes Chromista, so it does **not** coincide with reading 1.
3. **Medical/parasitological reading: parasitic protozoa** — *Plasmodium*, *Entamoeba*, *Giardia*, *Trichomonas*, *Leishmania*.

**GOLD's own children span readings 1 and 3 and cannot be reduced to either:** `Sporozoa` is the parasitological group (apicomplexans), `Oxymonads` are free-living-in-gut termite flagellates, `Myzozoa` is dinoflagellates + apicomplexans and contains photosynthetic members. That mixture is only coherent under the broad reading (1), so **reading 1 is what the data means** — with the caveat that GOLD's own usage leaks into phototrophs via Myzozoa.

Modern eukaryote systematics has dropped the name entirely: the ISP classification "no longer includes formal terms such as protozoa, animals, and plants, although these continue to be used by the public" ([Adl et al. 2019, *J Eukaryot Microbiol* 66:4–119, doi:10.1111/jeu.12691](https://doi.org/10.1111/jeu.12691); [PMC6492006](https://pmc.ncbi.nlm.nih.gov/articles/PMC6492006/)). **This does not disqualify a habitat term** — a habitat class defined by what the host organism *is like* (one heterotrophic eukaryotic cell) does not need the host group to be monophyletic — but the definition should say "unicellular heterotrophic eukaryote" rather than imply a clade. *(That last sentence is my judgement, not a claim from a source.)*

**Corroboration that this is a known modelling gap, not a local one:** ENVO issue [#781 "organismal groupings for EBI/JGI GOLD microbiome terms"](https://github.com/EnvironmentOntology/envo/issues/781) (open, filed 2019-05-27) names exactly this problem, listing "Reptilia, **Protists, Protozoa**, Spiralia, fish and green algae" as GOLD host groupings with no usable NCBITaxon semantics. A term request from this repo joins that thread rather than duplicating it.

---

## 2. Genus — the broader kind

**Genus: `ENVO:01001000` *environmental system determined by an organism*** — "An environmental system which is determined by a living organism" (verified live via [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000)). This is already the record's `parent_habitats` value and it is correct: a protozoan is a living organism, and this branch is the pattern ENVO uses for hosts.

**Its direct children, fetched from OLS4 today — there are exactly three:**

| CURIE | Label | Definition |
|---|---|---|
| ENVO:01001001 | plant-associated environment | An environmental system determined by a green plant. |
| ENVO:01001002 | animal-associated environment | An environmental system determined by an animal. |
| ENVO:01001041 | fungi-associated environment | An environmental system determined by a fungal structure. |

**There is no protist, protozoan, ciliate, amoeba or microorganism sibling.** Two independent OLS4 queries confirm the gap: a search of ENVO for `protozoa` returns zero classes; a search for `protist` returns zero classes; a search for `"associated environment"` returns only the plant/animal/fungi families plus the animal sub-branch (`ENVO:01001176` *environment associated with an aquatic invertebrate*, `ENVO:01001179` *cnidarian-associated environment*) and the part-variants (`ENVO:01001055`, `01001057`, `01001058`). The curator's note is correct as of this check.

**Near-misses and why each fails:**

| Candidate | Why it is not a match |
|---|---|
| `ENVO:01001002` *animal-associated environment* | The historical trap: "Protozoa" literally means "first animals" and 19th-century zoology filed them there. ENVO's definition says *an animal*; protozoa are not Metazoa under any current classification (Adl et al. 2019; Ruggiero et al. 2015). Parenting here asserts animal-hood the sources deny. |
| `ENVO:01001041` *fungi-associated environment* | Asserts fungal identity. Genuinely adjacent for GOLD's `Protists > Oomycetes` child (oomycetes are fungus-like but stramenopiles, not fungi) — which is an argument for keeping them apart, not merging. |
| `ENVO:01001001` *plant-associated environment* | Asserts green-plant identity; would misfile the phototrophic members (Myzozoa, euglenids) that a taxonomist might reach for. |
| `ENVO:2100000` *anatomical entity environment* | A single cell has no anatomical entity in the UBERON sense. Misapplies the anatomy axis; also no longer a direct child of `ENVO:01001000` in the current release. |
| `NCIT:C77916` *Protozoa* | An **organism** class, not an environment, and its own definition ("kingdom protista") conflates protozoa with protists. Correctly held as `relation: xref` on the record already (#99). |
| `BTO:0002503` *protozoan form* — "Any individual of the Protozoa" (in the vendored slice, `data/raw/ontology_terms.tsv:2503`) | An organism/cell term. Same objection; also the parent of `BTO:0005312` *amoeba*. |
| `BTO:0005312` *amoeba* | The nearest **in-slice** term to any part of this concept, and what PREGO uses (7 taxa, `data/raw/prego_habitats.tsv:361`). Still an organism term, and narrower than the concept. |
| NCBITaxon | **There is no NCBITaxon class with the exact label "Protozoa"** (verified via OLS4 exact search; only `Protozoa sp.` strain entries at NCBITaxon:1891099/1891100). So even the taxon-xref route has no clean target — precisely the complaint in ENVO #781. NCIT:C77916 is the only exact-label option, which is why it is the xref. |
| `habitatmech:GOLD.184623c963` *microbe-associated environment* (requested, `curation/term_requests.tsv:14`) | **Not a failure — the natural parent.** If minted, this concept becomes its child. It does not exist yet, so `ENVO:01001000` remains the genus in the meantime. |

---

## 3. Differentia — what distinguishes it from its siblings

The host is **one heterotrophic eukaryotic cell**, and the observable consequences separate it from all three existing siblings:

1. **Micrometre scale; organelles play the role of organs.** The whole habitat is a single cell; compartments are the food vacuole, symbiosome, hydrogenosome and macronucleus. Husnik et al. describe protist hosts carrying communities "whose richness and functional complexity are not very different from some model animal 'microbiomes'", compartmentalised "with organelles playing the role of tissues" ([doi:10.1016/j.cub.2021.05.049](https://doi.org/10.1016/j.cub.2021.05.049)).

2. **The habitat is formed by predation.** Protozoa are phagotrophs; the entry route into the habitat is the food vacuole, and colonisation is failed digestion. This is the "Trojan horse" and "training ground" literature: protozoa as vectors and environmental reservoirs for bacterial pathogens ([Barker & Brown 1994, *Microbiology* 140:1253–1259, doi:10.1099/00221287-140-6-1253](https://doi.org/10.1099/00221287-140-6-1253), PMID 8081490; [Molmeret et al. 2005, *Appl Environ Microbiol* 71:20–28, "Amoebae as training grounds for intracellular bacterial pathogens"](https://journals.asm.org/doi/10.1128/AEM.71.1.20-28.2005)). Free-living amoebae host *Legionella*, *Mycobacterium avium*, *Parachlamydia* and others, with encysted amoebae shielding internalised bacteria from chlorine and biocides ([Greub & Raoult 2004, *Clin Microbiol Rev* 17:413–433, doi:10.1128/CMR.17.2.413-433.2004](https://doi.org/10.1128/CMR.17.2.413-433.2004)). No plant-, animal- or fungi-associated environment is *constituted* by phagocytosis in this way.

3. **A measurable selective regime.** In a polluted estuary, 46% of *Acanthamoeba*-associated bacterial isolates were resistant to ≥4 antibiotics versus 0.6% of sediment-associated isolates; 22% were resistant to ≥6 ([Mooney et al. 2025, *Environ Microbiol* 27:e70193, doi:10.1111/1462-2920.70193](https://doi.org/10.1111/1462-2920.70193); [PMC12572456](https://pmc.ncbi.nlm.nih.gov/articles/PMC12572456/), 29 Oct 2025). The protozoan interior is a different chemical and selective environment from the sediment 1 mm away.

4. **Intranuclear occupancy — a compartment with no sibling counterpart.** *Holospora obtusa* enters *P. caudatum* via a food vacuole and grows **exclusively inside the macronucleus**, binding host chromatin so that reproductive forms are partitioned into each daughter nucleus at host division (Fokin & Görtz 2009, [doi:10.1007/978-3-540-92677-1_7](https://doi.org/10.1007/978-3-540-92677-1_7); Fokin 2022, [doi:10.1111/jeu.12886](https://doi.org/10.1111/jeu.12886)).

5. **Host-generated anoxia and H₂ — the habitat's characteristic physicochemistry.** Hydrogenosome- and hydrogenobody-bearing protozoa supply H₂ to intracellular methanogens. Rumen ciliates carry intracellular methanogens ([Finlay et al. 1994, *FEMS Microbiol Lett* 117:157–161, "Some rumen ciliates have endosymbiotic methanogens"](https://www.sciencedirect.com/science/article/abs/pii/0378109794901880)); methanogens associated with rumen ciliates were "responsible for between 9 and 25% of methanogenesis in rumen fluid" ([Newbold, Lassalas & Jouany 1995, *Lett Appl Microbiol* 21:230–234, doi:10.1111/j.1472-765x.1995.tb01048.x](https://doi.org/10.1111/j.1472-765x.1995.tb01048.x), PMID 7576513). The 2026 *Science* catalogue of 450 rumen ciliate genomes attributes the effect to a single-membrane H₂-producing organelle, the hydrogenobody, and reports ciliates at up to ~25% of rumen microbial biomass ([doi:10.1126/science.adv4244](https://doi.org/10.1126/science.adv4244)).

6. **Function localised to the protozoan cell, not the surrounding gut.** In the termite *Hodotermopsis sjoestedti*, nearly 60% of reductive acetogenesis and **almost all** nitrogen fixation in the hindgut are attributable to *Treponema* endosymbionts **inside** the protist *Eucomonympha* ([Ohkuma et al. 2015, *PNAS* 112:10224–10230, doi:10.1073/pnas.1423979112](https://doi.org/10.1073/pnas.1423979112), PMID 25979941). The Bacteroidales endosymbiont of *Pseudotrichonympha grassii* — 70% of all bacterial cells in the gut of *Coptotermes formosanus* — fixes N₂ and recycles host nitrogen waste, coupling N₂ fixation to cellulolysis within the protist cell ([Hongoh et al. 2008, *Science* 322:1108–1109, doi:10.1126/science.1165578](https://doi.org/10.1126/science.1165578), PMID 19008447). This is the clearest evidence that the protozoan cell, not the insect gut, is the unit of habitat — and it matches GOLD's `Oxymonads` child directly.

7. **A structured, host-specific microbiome that single-cell methods can resolve.** Single-cell isolation plus genome-resolved metagenomics on >100 uncultivated ciliates and amoebae recovered 117 endosymbiont genomes (Holosporales, Rickettsiales, Legionellales, Chlamydiae, Babelota), 258 host-associated Patescibacteriota genomes, and >80 giant viruses, with microbiome structure differing sharply between ciliates and amoebae ([Schulz et al. 2025, *Nat Commun* 16, doi:10.1038/s41467-025-65263-4](https://doi.org/10.1038/s41467-025-65263-4), PMID 41285752, PMCID PMC12644861). "Protists as significant microbial and viral association centres" is the paper's framing.

8. **A parasitic protozoan can be a habitat too.** >85% of *Trichomonas vaginalis* clinical isolates in some regions harbour *Mycoplasma hominis* — described as the only known endosymbiosis between two true human pathogens, with the trichomonad acting as both niche and transmission vector ([Margarita et al. 2022, *mBio* 13:e00918-22, doi:10.1128/mbio.00918-22](https://doi.org/10.1128/mbio.00918-22); [PMC9239101](https://pmc.ncbi.nlm.nih.gov/articles/PMC9239101/); review: [Fiori et al. 2023, *Pathogens* 12:1083](https://www.mdpi.com/2076-0817/12/9/1083)). This covers GOLD's `Sporozoa`/parasitological reading.

9. **Endosymbiosis is the norm here, not the exception.** "Endosymbiosis seems to represent a general evolutionary strategy of protists" for acquiring novel biochemical functions — photosynthesis, N₂ fixation, methanogenesis ([Nowack & Melkonian 2010, *Phil Trans R Soc B* 365:699–712, doi:10.1098/rstb.2009.0188](https://doi.org/10.1098/rstb.2009.0188), PMID 20124339).

*Flagged as inference, not source claim:* items 1–9 are each cited, but the choice of **"one heterotrophic eukaryotic cell"** as *the* differentia — rather than, say, "phagotrophy" alone or "non-monophyletic unicellular eukaryote" — is my synthesis. I chose it because (a) it is what separates the concept from all three existing ENVO siblings, (b) heterotrophy is what separates it from GOLD's own `Algae` category, and (c) it survives the fact that Protozoa is not a clade.

---

## 4. Sources

**Source scheme and standards**
- Mukherjee S. et al. Genomes OnLine Database (GOLD) v.7. *Nucleic Acids Research* 47(D1):D649–D659, 2019. doi:[10.1093/nar/gky977](https://doi.org/10.1093/nar/gky977) · [PMC6323969](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323969/) — the five-level scheme and host-as-Ecosystem-Category pattern. **`gold.jgi.doe.gov/ecosystem_classification` returns HTTP 403 to automated fetch and was not read directly**; the scheme is cited from the paper.
- Yilmaz P. et al. MIMARKS/MIxS specifications. *Nature Biotechnology* 29:415–420, 2011. doi:[10.1038/nbt.1823](https://doi.org/10.1038/nbt.1823) — the host-associated environmental package, which records a `host taxid` but supplies no controlled habitat class for a protozoan host. *Cited from metadata; landing page not fetched.*
- ENVO issue [#781](https://github.com/EnvironmentOntology/envo/issues/781), open since 2019-05-27, labels `mapping` / `GOLD-EBI-MGNIFY` — names "Protists, Protozoa" among GOLD groupings lacking NCBITaxon semantics. *Fetched via GitHub API.*
- ENVO classes verified live via OLS4: `ENVO:01001000` and its three direct children; zero hits for `protozoa` and for `protist` in ENVO. NCIT:C77916 label + definition verified via OLS4. Absence of an exact-label `Protozoa` in NCBITaxon verified via OLS4 exact search.

**Classification / nomenclature**
- Adl S.M. et al. Revisions to the Classification, Nomenclature, and Diversity of Eukaryotes. *J Eukaryot Microbiol* 66:4–119, 2019. doi:[10.1111/jeu.12691](https://doi.org/10.1111/jeu.12691) · [PMC6492006](https://pmc.ncbi.nlm.nih.gov/articles/PMC6492006/) — "protozoa" is not a formal group. *The "no longer includes formal terms such as protozoa" wording is quoted from the [International Society of Protistologists' announcement](https://protistologists.org/revised-classification-of-eukaryotes-published/) of the paper, not from the paper's own text, which I did not read in full.*
- Ruggiero M.A. et al. A Higher Level Classification of All Living Organisms. *PLoS ONE* 10:e0119248, 2015. doi:[10.1371/journal.pone.0119248](https://doi.org/10.1371/journal.pone.0119248) · [PMC4418965](https://pmc.ncbi.nlm.nih.gov/articles/PMC4418965/) — retains kingdom Protozoa while conceding it is paraphyletic. *Fetched.*

**Primary literature and reviews**
- Husnik F. et al. Bacterial and archaeal symbioses with protists. *Curr Biol* 31:R862–R877, 2021. doi:[10.1016/j.cub.2021.05.049](https://doi.org/10.1016/j.cub.2021.05.049)
- Nowack E.C.M. & Melkonian M. Endosymbiotic associations within protists. *Phil Trans R Soc B* 365:699–712, 2010. doi:[10.1098/rstb.2009.0188](https://doi.org/10.1098/rstb.2009.0188)
- Schulz F. et al. Single-cell genomics reveals complex microbial and viral associations in ciliates and testate amoebae. *Nat Commun* 16, 2025. doi:[10.1038/s41467-025-65263-4](https://doi.org/10.1038/s41467-025-65263-4)
- Song Q. et al. Cellular interactions and evolutionary origins of endosymbiotic relationships with ciliates. *ISME J* 18(1):wrae117, 2024. [oup link](https://academic.oup.com/ismej/article/18/1/wrae117/7698271) · [PMC11253213](https://pmc.ncbi.nlm.nih.gov/articles/PMC11253213/)
- Barker J. & Brown M.R.W. Trojan horses of the microbial world. *Microbiology* 140:1253–1259, 1994. doi:[10.1099/00221287-140-6-1253](https://doi.org/10.1099/00221287-140-6-1253)
- Molmeret M. et al. Amoebae as training grounds for intracellular bacterial pathogens. *Appl Environ Microbiol* 71:20–28, 2005. [journal link](https://journals.asm.org/doi/10.1128/AEM.71.1.20-28.2005) *— cited from search metadata; DOI not independently confirmed.*
- Greub G. & Raoult D. Microorganisms resistant to free-living amoebae. *Clin Microbiol Rev* 17:413–433, 2004. doi:[10.1128/CMR.17.2.413-433.2004](https://doi.org/10.1128/CMR.17.2.413-433.2004)
- Mooney et al. The Microbial Trojan Horse and Antimicrobial Resistance. *Environ Microbiol*, 2025. doi:[10.1111/1462-2920.70193](https://doi.org/10.1111/1462-2920.70193)
- Fokin S.I. & Görtz H.-D. Diversity of *Holospora* bacteria in *Paramecium*. In *Endosymbionts in Paramecium*, Microbiology Monographs 12:161–201, 2009. doi:[10.1007/978-3-540-92677-1_7](https://doi.org/10.1007/978-3-540-92677-1_7)
- Fokin S.I. Bacterial symbiosis in ciliates. *J Eukaryot Microbiol* 69:e12886, 2022. doi:[10.1111/jeu.12886](https://doi.org/10.1111/jeu.12886)
- Finlay B.J. et al. Some rumen ciliates have endosymbiotic methanogens. *FEMS Microbiol Lett* 117:157–161, 1994. [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/0378109794901880)
- Newbold C.J., Lassalas B. & Jouany J.P. *Lett Appl Microbiol* 21:230–234, 1995. doi:[10.1111/j.1472-765x.1995.tb01048.x](https://doi.org/10.1111/j.1472-765x.1995.tb01048.x)
- Xie F. et al. Rumen ciliates modulate methane emissions in ruminants. *Science*, 30 Apr 2026. doi:[10.1126/science.adv4244](https://doi.org/10.1126/science.adv4244) *— publisher page returns 403; metadata and abstract claims taken from Europe PMC (PMID 42060748).*
- Hongoh Y. et al. *Science* 322:1108–1109, 2008. doi:[10.1126/science.1165578](https://doi.org/10.1126/science.1165578)
- Ohkuma M. et al. *PNAS* 112:10224–10230, 2015. doi:[10.1073/pnas.1423979112](https://doi.org/10.1073/pnas.1423979112)
- Margarita V. et al. Two different species of *Mycoplasma* endosymbionts can influence *T. vaginalis* pathophysiology. *mBio* 13:e00918-22, 2022. doi:[10.1128/mbio.00918-22](https://doi.org/10.1128/mbio.00918-22)
- Fiori P.L. et al. *Pathogens* 12:1083, 2023. [MDPI](https://www.mdpi.com/2076-0817/12/9/1083)

**Repository evidence (internal, but decisive for the reading)**
- `data/raw/gold_ecosystem_paths.tsv` lines 322, 344, 461, 490, 868, 1734, 1913–1914, 2533–2548 — the Protozoa/Protists/Amoebozoa/Ciliophora paths and counts.
- `data/raw/ontology_terms.tsv:2503` (BTO:0002503), `:5311` (BTO:0005312), `:10831` (NCIT:C77916 — **no definition in the vendored slice**).
- `data/raw/bacdive_isolation_sources.tsv:148` (BacDive `Protist`, 3 strains); `data/raw/prego_habitats.tsv:361` (PREGO `amoeba`, 7 taxa); `curation/decisions.tsv:1550` (the parallel BacDive Protista decision), `:1587` (this decision), `:921`.
- `curation/term_requests.tsv:13–15` (reptile-, microbe-, bacterium-associated environment — the established request pattern).

---

## 5. Synonyms, and what NOT to conflate

**Names in real use for this concept**
- protozoan host; protozoan as host cell
- protozoa-associated environment / protozoan-associated environment (the ENVO-pattern name)
- protist host (broader — includes algae)
- amoebal host; "amoeba-resisting microorganisms" (Greub & Raoult 2004)
- "protozoan microbiome" / "the microbiome of a protist" (Schulz et al. 2025; Husnik et al. 2021)
- basibiont (the larger partner in an epibiotic pair)
- GOLD's own string: `Host-associated > Protozoa`

**Commonly but wrongly treated as the same thing**
- **The taxon / the organism.** `NCIT:C77916` *Protozoa*, `BTO:0002503` *protozoan form*, `BTO:0005312` *amoeba*. These are classes of organisms, not places — `relation: xref`, per #99. **Consistency flag for the curator:** `data/habitats/host_associated/amoeba.yaml` is currently grounded `EXACT` to `BTO:0005312`, an organism term, with `BTO:0002503` as `parent_habitats`. That is the same over-claim this record's decision was reversed to avoid, and it will look inconsistent alongside a `protozoan-associated environment` request. Worth a separate issue rather than a change here.
- **"Protists" (GOLD's sibling category, 40 assertions, `habitatmech:GOLD.eee7408afd`) and BacDive's "Protist" (`habitatmech:BACDIVE.a7f6b12719`).** Under the standard reading these are **broader**, not synonymous: protists include algae, protozoa are the heterotrophic ones. GOLD carries both as level-2 siblings, which is a source artefact.
- **Algae / phototrophic protists** — separate GOLD category, separate metabolism, and the whole point of the "heterotrophic" clause.
- **Oomycetes** — fungus-like but stramenopiles; GOLD files them under `Protists`, and they belong nowhere near `ENVO:01001041`.
- **The animal or plant the protozoan lives in** — rumen, termite hindgut, human urogenital tract. Nested habitat, different concept, different record.
- **Protozoal diseases** — malaria, amoebiasis, giardiasis, trichomoniasis. Disease states, not places; `NOT_APPLICABLE` is right for those.
- **Protozoa as grazers / wastewater indicator organisms** — an ecological role and a process, not a habitat.
- **Plastid / mitochondrion / apicoplast** — organelles of endosymbiotic origin. Evolutionary history, not a sampled habitat.
- **`Host-associated > Endosymbionts`** — names the *occupant's* role, not the host. Occupant ≠ habitat.

---

## 6. Should it be a term at all — yes

This is a place: it is what a sample is taken from (a *Paramecium* macronucleus, an *Acanthamoeba* trophozoite, an *Entodinium* cell, a *Trichomonas* cytoplasm, a *Pseudotrichonympha* cell), it has a physical boundary, a characteristic chemistry (anoxic, H₂-rich in the hydrogenosome-bearing lineages), a documented entry process (phagocytosis), and a distinctive selective regime. It is not a process, quality, disease state or sampling artefact. And it is **not** a taxon term dressed as a habitat — the taxon stays in `relation: xref`, exactly as the reversed decision records, and the concept keeps its minted identity, the same shape ENVO already publishes at plant-, animal- and fungi-associated environment.

The gap is independently confirmed: ENVO's organism-determined branch has exactly three children and none of them covers a protozoan host, and ENVO's own tracker has had this open as issue #781 since 2019.

**Three things the curator must decide, because the sources do not decide them:**

1. **The relationship to GOLD's `Protists` record (40 assertions) is unresolved and this record cannot be finished without settling it.** They are near-duplicates in GOLD but not synonyms in the literature. My recommendation: request **`protist-associated environment`** ("An environmental system determined by a protist — a unicellular eukaryote that is not a plant, animal or fungus") and **`protozoan-associated environment`** as its child restricted to heterotrophic protists; then `Amoebozoa` (`GOLD.1341e74d35`), `Ciliophora` (`GOLD.797c5e7dbb`), `Myzozoa`, `Oxymonads` and `Sporozoa` all have somewhere principled to hang. Requesting only one of the pair leaves the other record with the same problem next month.
2. **Parenting, given the pending `microbe-associated environment` request (`term_requests.tsv:14`).** That term does not exist yet, so `ENVO:01001000` stays the genus, with the same "editors should re-parent if both are minted" note already used for `bacterium-associated environment` (`term_requests.tsv:15`).
3. **Whether the definition should mention non-monophyly explicitly.** Protozoa is paraphyletic at best (Ruggiero et al. 2015) and formally abandoned at worst (Adl et al. 2019). I would put that in a `comment`, not in the definition — the definition should carry the observable properties (one cell, eukaryotic, heterotrophic), and the comment should say the grouping is traditional and non-monophyletic, so a future editor does not read the term as a clade claim.

**One thing I could not verify:** what the 32 assertions on the bare `Host-associated > Protozoa` path actually are — which protozoan hosts, and whether any are in fact algal or fungal hosts misfiled by submitters. `gold.jgi.doe.gov` blocks automated fetch and `data/raw/` carries only node ids and counts. It does not change the genus or the differentia, but it is the one check that would confirm the broad reading against GOLD's actual records rather than against its path structure.

**Sources:** [GOLD v.7 *NAR* 2019](https://doi.org/10.1093/nar/gky977) · [Adl et al. 2019](https://doi.org/10.1111/jeu.12691) · [Ruggiero et al. 2015](https://doi.org/10.1371/journal.pone.0119248) · [Husnik et al. 2021](https://doi.org/10.1016/j.cub.2021.05.049) · [Nowack & Melkonian 2010](https://doi.org/10.1098/rstb.2009.0188) · [Schulz et al. 2025](https://doi.org/10.1038/s41467-025-65263-4) · [Song et al. 2024](https://academic.oup.com/ismej/article/18/1/wrae117/7698271) · [Barker & Brown 1994](https://doi.org/10.1099/00221287-140-6-1253) · [Molmeret et al. 2005](https://journals.asm.org/doi/10.1128/AEM.71.1.20-28.2005) · [Greub & Raoult 2004](https://doi.org/10.1128/CMR.17.2.413-433.2004) · [Mooney et al. 2025](https://doi.org/10.1111/1462-2920.70193) · [Fokin & Görtz 2009](https://doi.org/10.1007/978-3-540-92677-1_7) · [Fokin 2022](https://doi.org/10.1111/jeu.12886) · [Newbold et al. 1995](https://doi.org/10.1111/j.1472-765x.1995.tb01048.x) · [Xie et al. 2026](https://doi.org/10.1126/science.adv4244) · [Hongoh et al. 2008](https://doi.org/10.1126/science.1165578) · [Ohkuma et al. 2015](https://doi.org/10.1073/pnas.1423979112) · [Margarita et al. 2022](https://doi.org/10.1128/mbio.00918-22) · [Fiori et al. 2023](https://www.mdpi.com/2076-0817/12/9/1083) · [ENVO issue #781](https://github.com/EnvironmentOntology/envo/issues/781) · [OLS4 ENVO:01001000](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000) · [OLS4 NCIT:C77916](https://www.ebi.ac.uk/ols4/ontologies/ncit/classes?obo_id=NCIT:C77916)

## Citations

1. https://doi.org/10.1093/nar/gky977
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC6323969/
3. https://doi.org/10.1007/978-3-540-92677-1_7
4. https://doi.org/10.1111/jeu.12886
5. https://doi.org/10.1126/science.adv4244
6. https://doi.org/10.1016/j.cub.2021.05.049
7. https://www.ebi.ac.uk/ols4/ontologies/ncit/classes?obo_id=NCIT:C77916
8. https://doi.org/10.1371/journal.pone.0119248
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC4418965/
10. https://doi.org/10.1111/jeu.12691
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC6492006/
12. https://github.com/EnvironmentOntology/envo/issues/781
13. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000
14. https://doi.org/10.1099/00221287-140-6-1253
15. https://journals.asm.org/doi/10.1128/AEM.71.1.20-28.2005
16. https://doi.org/10.1128/CMR.17.2.413-433.2004
17. https://doi.org/10.1111/1462-2920.70193
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC12572456/
19. https://www.sciencedirect.com/science/article/abs/pii/0378109794901880
20. https://doi.org/10.1111/j.1472-765x.1995.tb01048.x
21. https://doi.org/10.1073/pnas.1423979112
22. https://doi.org/10.1126/science.1165578
23. https://doi.org/10.1038/s41467-025-65263-4
24. https://doi.org/10.1128/mbio.00918-22
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC9239101/
26. https://www.mdpi.com/2076-0817/12/9/1083
27. https://doi.org/10.1098/rstb.2009.0188
28. https://doi.org/10.1038/nbt.1823
29. https://protistologists.org/revised-classification-of-eukaryotes-published/
30. https://academic.oup.com/ismej/article/18/1/wrae117/7698271
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC11253213/