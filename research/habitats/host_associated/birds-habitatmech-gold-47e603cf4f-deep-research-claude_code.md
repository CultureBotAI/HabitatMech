---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:50:02.027263'
end_time: '2026-08-17T16:56:56.960699'
duration_seconds: 414.93
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Birds
  habitat_identifier: habitatmech:GOLD.47e603cf4f
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Birds'
  assertions: '1848'
  parent_terms: ENVO:01001000, ENVO:01001002
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Nearest
    broader term ENVO:01001002 ''animal-associated environment'' attached as a parent.
    Birds as host. Parented to animal-associated environment; not grounded there because
    every host clade would merge onto one record. ENVO term request. (source concept
    habitatmech:GOLD.47e603cf4f)'
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
  - claude-opus-5
  web_search_requests: 15
  num_turns: 29
  total_cost_usd: 3.1112905
  session_id: 863cae08-fb96-48c9-b4e6-9315917835ca
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 23
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Birds
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.47e603cf4f
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Birds
- **Upstream assertion volume:** 1848
- **Nearest broader term already on the record:** ENVO:01001000, ENVO:01001002
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:01001002 'animal-associated environment' attached as a parent. Birds as host. Parented to animal-associated environment; not grounded there because every host clade would merge onto one record. ENVO term request. (source concept habitatmech:GOLD.47e603cf4f)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Birds** as a microbial habitat, with citations.

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

# Birds (`habitatmech:GOLD.47e603cf4f`) — novel-term definition research

> **Proposed definition:** An animal-associated environment which is determined by a bird (a member of Aves), comprising the body surfaces, internal organs and cavities, and excreted or shed materials of a living or dead bird as sites colonised by microorganisms.

---

## 1. What the concept denotes

**The reading the data means.** GOLD's `Host-associated > Birds` is an Ecosystem Category — the second of five levels in GOLD's classification, sitting directly under the `Host-associated` Ecosystem and parallel to `Mammals`, `Fish`, `Arthropoda`, `Plants` and so on ([Mukherjee et al. 2023, *NAR* 51:D957–D963, doi:10.1093/nar/gkac974](https://dx.doi.org/10.1093/nar/gkac974)). At this level the node names **the host clade whose body constitutes the environment**, and the levels below it name where on or in that body the sample came from. The corpus's own extraction shows exactly this: `data/raw/gold_ecosystem_paths.tsv` carries 39 descendant paths under `Host-associated > Birds`, all of them anatomical or body-product —

| child path (abbreviated) | assertions |
|---|---|
| Digestive system > Large intestine > Fecal | 1229 |
| Digestive system > Large intestine > Ceca | 407 |
| Digestive system > Ceca | 315 |
| Digestive system > Large intestine > Cloaca | 309 |
| Digestive system (unspecified) | 186 |
| Remains | 60 |
| Respiratory system | 53 |
| Integumentary system > Skin | 37 |
| Circulatory system > Blood | 30 |
| Respiratory system > Trachea > Syrinx | 21 |
| Integumentary system > Uropygial/Preen gland | 3 |

…plus crop, gizzard-adjacent stomach, ileum, jejunum, liver, biliary tract, spleen, kidney, brain, heart, skeletal muscle, infraorbital sinus, nasal cavity and oral/buccal cavity. **What a sample from this concept is, is a swab, gut content, tissue, blood or dropping taken from a bird.**

**The boundary.**

- *Inside:* the internal compartments and luminal contents of a bird's gut, respiratory tract, urogenital tract and circulatory system; its skin, plumage and glandular surfaces; its droppings while still host-associated material; and the carcass (`Birds > Remains`, 60 assertions).
- *Outside (neighbouring concepts):* the **nest** (`ENVO:00005805 nest of bird` — an animal habitation the bird builds, not the bird), **guano-derived soils** (`ENVO:00005782 ornithogenic soil` — an environmental material formed *from* avian faeces after deposition), **poultry houses, litter and processing surfaces** (engineered environments in GOLD's scheme), and **bird-derived foods** (`FOODON:00001105 avian egg food product`, `FOODON:00001251 avian food product`, `FOODON:00001131 poultry meat food product`).
- *Also outside:* **Aves the taxon** (`NCBITaxon:8782`). A clade is a class of organisms, not a place. Per this repo's standing rule, the taxon is recorded as `relation: xref`, and the habitat concept keeps its own minted identity.

**Ambiguities that must not be resolved silently.**

1. **Host organism vs. bird-influenced external environment.** "Birds" as a habitat label is used in the literature both for the bird's body (this concept) and for environments a bird *creates* (nests, guano fields, seabird-colony soils, moss banks). The GOLD path and all 39 of its children fix the first reading. The second is real and well studied — penguin guano deposition restructures Antarctic soil microbiomes and the taxa it introduces include bird-gut organisms such as *Gottschalkia* ([Zhu et al. 2018, *Front. Microbiol.* 9:552](https://pmc.ncbi.nlm.nih.gov/articles/PMC5891643/); [Almela et al. 2024, *Front. Microbiol.* 15:1362975](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2024.1362975/full)) — but it belongs to `ornithogenic soil` and to a possible future *bird-influenced environment*, not here.
2. **Wild vs. domestic.** GOLD does not split the node. The assertion profile is heavily weighted toward gut compartments that dominate poultry research (fecal 1229, ceca 407+315), and poultry is the most extensively studied avian group ([Falchi et al. 2024, *Reprod. Fertil.* 5:e230076](https://pmc.ncbi.nlm.nih.gov/articles/PMC11301535/)). *That the volume is therefore mostly chicken is my inference from the path profile, not a statement GOLD makes* — the node itself is clade-wide and the definition must stay clade-wide.
3. **Living vs. dead.** `Birds > Remains` places carcass material inside the concept. The proposed definition says "living or dead" for that reason, following ENVO's own wording in `ENVO:01001055` ("part of a living or dead animal").

---

## 2. Genus — the broader kind

**Genus: `ENVO:01001002` animal-associated environment** — *"An environmental system determined by an animal."* This is already on the record as a parent and is the correct genus: a bird is an animal, and the concept is an environmental system determined by it. Its own parent `ENVO:01001000 environmental system determined by an organism` (synonym: *host-associated environment*) is the grandparent.

**No ENVO term names the concept.** I checked the descendant closure of `ENVO:01001002` in OLS4: it has only 23 hierarchical descendants, of which the sole organism-scoped ones are `ENVO:01001176 environment associated with an aquatic invertebrate` and `ENVO:01001179 cnidarian-associated environment` (the rest are the human-settlement branch). Text search of ENVO for "bird" and for "avian" returns only `nest of bird`, `nesting material`, `ornithogenic soil` and `feather environment` — no host-clade class. A search of the ENVO issue tracker for open bird/avian new-term requests returns nothing relevant (issues #157, #159, #161, #177, #178, #191 are all closed and about foods, excrement cleanup and nesting material).

**Near-misses, and why each fails:**

| Term | Why it is not a match |
|---|---|
| `ENVO:01001002` animal-associated environment | **Too broad** — covers all Metazoa. Grounding here merges every host clade (Birds, Fish, Mammals, Insects…) onto one record, which is precisely what the existing curation note refuses. Correct as *parent*. |
| `ENVO:01001000` environmental system determined by an organism | Broader still (plants, fungi, animals). Correct as ancestor. |
| `ENVO:01001055` environment associated with an animal part or small animal | **Near-miss with an added assertion.** It asserts either part-hood or small body size; the GOLD concept is the whole host at any size, from hummingbird to ostrich. Its sibling framing makes it useful as a parent for the *child* body-site records, not for this one. |
| `ENVO:01001179` cnidarian-associated environment | Not a match, but the **decisive precedent**: ENVO already admits clade-specific host environments under `animal-associated environment`, with the pattern *"An environmental system determined by a ⟨clade⟩ or part of a ⟨clade⟩."* A bird-associated environment is the same pattern one clade over. |
| `ENVO:01001176` environment associated with an aquatic invertebrate | Precedent for scoping a host environment by clade + ecology; disjoint from Aves. |
| `ENVO:2100006` feather environment | **Narrower** — one body surface of a bird, and it carries no textual definition in the vendored slice. A candidate child, not the concept. |
| `ENVO:00005805` nest of bird | **Narrower and a different kind** — an animal habitation the bird constructs. Under this repo's rule (a cocoon grounds normally because it is a structure, not the insect), a nest is a legitimate habitat term, but it is not the bird. |
| `ENVO:00005782` ornithogenic soil | **Narrower and downstream** — *"Soil which is formed from avian fecal matter."* An environmental material produced by birds, not an environment determined by a bird's body. |
| `NCBITaxon:8782` Aves | **Not a habitat.** The taxon term names a class of organisms. `relation: xref`. |
| `UBERON:0000022` feather, `UBERON:0012464` cloacal vent, `BTO:0001420` uropygial gland | Anatomical parts. These are the right targets for the *child* records (and the corpus already grounds several of them), not for the host-clade concept. |
| FOODON avian/poultry product terms | Food commodities. |

**Conclusion:** the genus exists (`ENVO:01001002`); the species does not. HabitatMech must supply the definition, and the natural ENVO new-term request is **`bird-associated environment`**, minted as a child of `ENVO:01001002` alongside `cnidarian-associated environment`. (Per the standing rule in this workspace, actually submitting that NTR needs explicit per-request human authorisation; this report only identifies it.)

---

## 3. Differentia — what distinguishes it from its siblings

The siblings under `animal-associated environment` are the other GOLD host clades (Mammals, Fish, Reptilia, Amphibia, Arthropoda, Mollusca, Porifera…). What separates a bird from them, in observable terms:

**a. Host identity and scope.** Determined by a member of Aves — ~11,032 extant species in 44 orders and 253 families (IOC World Bird List v14.1, 2024). Aves is the only extant clade of feathered, endothermic, oviparous archosaurs, so host identity alone is diagnostic and testable by host metadata (MIxS host-associated package records `host taxid` / `host scientific name`; [Yilmaz et al. 2011, *Nat. Biotechnol.* 29:415–420, doi:10.1038/nbt.1823](https://www.nature.com/articles/nbt.1823)).

**b. Thermal regime — measurable, and the highest of any endotherm.** Mean avian body temperature is 38.5 ± 1.0 °C at rest, 41.0 ± 1.3 °C in the active phase and 43.9 ± 0.9 °C at high activity; birds exceed mammals by ~1.9 °C at rest and ~2.4 °C when active ([Prinzinger, Preßmar & Schleucher 1991, *Comp. Biochem. Physiol. A* 99:499–506, doi:10.1016/0300-9629(91)90122-S](https://www.sciencedirect.com/science/article/abs/pii/030096299190122S)). The interior of this habitat is therefore a thermophilic-leaning, near-constant 40 °C environment — a real physicochemical differentiator from fish, reptile and amphibian hosts, and a measurable one from mammals.

**c. Gut architecture and residence time.** The avian digestive tract is compartmentalised into crop (lactic-acid-bacteria dominated), gizzard (low pH, mechanical, low fermentation), short small intestine, and **paired ceca** as the principal anaerobic fermentation chambers, discharging through a **cloaca** shared with the urinary and reproductive tracts. Cecal microbial density reaches ~10¹¹ cells g⁻¹ in chickens and over half the phylotypes recovered in deep 16S surveys were previously undescribed ([Sergeant et al. 2014, *PLoS ONE* 9:e91941](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0091941)). Overall gut transit is rapid and the tract shortened relative to mammals of comparable mass, an adaptation associated with flight ([Grond et al. 2018, *J. Avian Biol.* 49:e01788, doi:10.1111/jav.01788](https://nsojournals.onlinelibrary.wiley.com/doi/10.1111/jav.01788); [Bodawatta et al. 2022, *Trends Microbiol.* 30:268–280, doi:10.1016/j.tim.2021.07.003](https://pubmed.ncbi.nlm.nih.gov/34393028/)).

**d. Community signature and weak phylosymbiosis.** The wild-bird core gut community is dominated by Firmicutes, Proteobacteria, Bacteroidetes and Actinobacteria, but varies strongly within and between species and among gut sections (Grond et al. 2018). In the largest comparative survey to date — ~900 vertebrate species including **491 birds** and 315 mammals — bird gut microbiomes did **not** show the diet- and phylogeny-structured pattern typical of mammals, and bats clustered with birds rather than with other mammals, implicating flight-associated physiology as the shared cause ([Song et al. 2020, *mBio* 11:e02901-19, doi:10.1128/mBio.02901-19](https://journals.asm.org/doi/10.1128/mbio.02901-19); commentary: [Hird 2020, *mBio* 11:e00153-20](https://journals.asm.org/doi/10.1128/mbio.00153-20)). **This "weak phylosymbiosis" is the strongest published differentiator between a bird-associated and a mammal-associated environment**, and is stated by the sources, not inferred here.

**e. Integument.** A keratinous, feathered body surface supporting a distinctive keratinolytic guild (*Bacillus licheniformis* and relatives) that degrades feathers, together with the **uropygial (preen) gland** whose secretions and resident bacteria antagonise those degraders — e.g. *Enterococcus faecalis* bacteriocin-mediated inhibition in hoopoes ([Martín-Vivaldi et al. 2010, *J. Exp. Biol.* 213:3621–3626, doi:10.1242/jeb.031336](https://dx.doi.org/10.1242/jeb.031336)), and inhibition assays on great-tit gland isolates ([Diaz-Lora et al. 2020, *Front. Microbiol.* 11:1735](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7401573/)); [Møller et al. 2009, *Funct. Ecol.* 23:1097–1105](https://besjournals.onlinelibrary.wiley.com/doi/10.1111/j.1365-2435.2009.01594.x). No non-avian host clade offers this niche. GOLD's own `Integumentary system > Uropygial/Preen gland` path (3 assertions) confirms it is sampled as such.

**f. Excretory chemistry.** Birds excrete nitrogen principally as uric acid in semi-solid urine voided with faeces through the cloaca, rather than as urea in liquid urine (BTO:0001419 *urine*, definition: "…forms a clear amber and usually slightly acid fluid in mammals but is semisolid in birds and reptiles"). This is why the downstream deposit is chemically distinctive enough to have its own ENVO material class (`ornithogenic soil`, formed from avian faecal matter) and why guano is nitrogen-rich in urea, protein and ammonium (Zhu et al. 2018).

**Which of these to put in the definition:** only (a). The rest belong in the term's comment/elucidation. An Aristotelian differentia should be the one property that individuates within the genus — here, *determined by a bird* — with the physiology cited as supporting characterisation. Loading (b)–(f) into the definition sentence would make it a description, and would over-claim for the many bird hosts whose ceca are vestigial or whose plumage guild is unstudied.

---

## 4. Sources

Full citations for every claim above, in order of use:

1. Mukherjee S. et al. (2023) "Twenty-five years of Genomes OnLine Database (GOLD): data updates and new features in v.9." *Nucleic Acids Research* 51(D1):D957–D963. doi:[10.1093/nar/gkac974](https://dx.doi.org/10.1093/nar/gkac974). — GOLD's five-level Ecosystem→Category→Type→Subtype→Specific Ecosystem scheme; host-associated exemplar path.
2. `data/raw/gold_ecosystem_paths.tsv` (this repo, extracted from kg-microbe) — the 39 child paths and their assertion counts, quoted above.
3. ENVO term records, retrieved 2026-08-17 from the vendored slice `data/raw/ontology_terms.tsv` and cross-checked in OLS4: `ENVO:01001000`, `ENVO:01001001`, `ENVO:01001002`, `ENVO:01001041`, `ENVO:01001055`, `ENVO:01001176`, `ENVO:01001179`, `ENVO:00005782`, `ENVO:00005805`, `ENVO:02000004`, `ENVO:2100006`. Ontology home: [environmentontology.org](http://environmentontology.org/); Buttigieg P.L. et al. (2016) "The environment ontology in 2016." *J. Biomed. Semantics* 7:57, [PMC5035502](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/); Buttigieg P.L. et al. (2013) *J. Biomed. Semantics* 4:43, doi:[10.1186/2041-1480-4-43](https://link.springer.com/article/10.1186/2041-1480-4-43).
4. Yilmaz P. et al. (2011) "Minimum information about a marker gene sequence (MIMARKS) and minimum information about any (x) sequence (MIxS) specifications." *Nat. Biotechnol.* 29:415–420. doi:[10.1038/nbt.1823](https://www.nature.com/articles/nbt.1823). — host-associated environmental package; host taxonomy as sample metadata.
5. Song S.J. et al. (2020) "Comparative analyses of vertebrate gut microbiomes reveal convergence between birds and bats." *mBio* 11(1):e02901-19. doi:[10.1128/mBio.02901-19](https://journals.asm.org/doi/10.1128/mbio.02901-19); PMID 31911491.
6. Hird S.M. (2020) "Context is key: comparative biology illuminates the vertebrate microbiome." *mBio* 11:e00153-20. doi:[10.1128/mBio.00153-20](https://journals.asm.org/doi/10.1128/mbio.00153-20).
7. Bodawatta K.H., Hird S.M., Grond K., Poulsen M., Jønsson K.A. (2022) "Avian gut microbiomes taking flight." *Trends in Microbiology* 30(3):268–280. doi:[10.1016/j.tim.2021.07.003](https://pubmed.ncbi.nlm.nih.gov/34393028/). — >100 non-poultry gut-microbiome studies 2017–2020; flight-related physiological constraints.
8. Grond K., Sandercock B.K., Jumpponen A., Zeglin L.H. (2018) "The avian gut microbiota: community, physiology and function in wild birds." *J. Avian Biol.* 49:e01788. doi:[10.1111/jav.01788](https://nsojournals.onlinelibrary.wiley.com/doi/10.1111/jav.01788).
9. Bodawatta K.H., Kogut M., Taylor M.W. (2023) "Editorial: Evolution and diversity of avian gut microbiomes." *Front. Microbiol.* [PMC10773680](https://pmc.ncbi.nlm.nih.gov/articles/PMC10773680/).
10. Falchi E. et al. (2024) "Microbiomes in birds: a review of links to health and reproduction." *Reproduction and Fertility* 5(3):e230076. [PMC11301535](https://pmc.ncbi.nlm.nih.gov/articles/PMC11301535/). — site-specific avian microbiomes (gut, skin, cloacal, preen gland, feather); poultry as the best-studied group.
11. Zhang Y. et al. (2022) "The avian gut microbiota: diversity, influencing factors, and future directions." *Front. Microbiol.* 13:934272. [PMC9389168](https://pmc.ncbi.nlm.nih.gov/articles/PMC9389168/).
12. Prinzinger R., Preßmar A., Schleucher E. (1991) "Body temperature in birds." *Comp. Biochem. Physiol. A* 99:499–506. doi:[10.1016/0300-9629(91)90122-S](https://www.sciencedirect.com/science/article/abs/pii/030096299190122S).
13. Sergeant M.J. et al. (2014) "Extensive microbial and functional diversity within the chicken cecal microbiome." *PLoS ONE* 9(3):e91941. doi:[10.1371/journal.pone.0091941](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0091941).
14. Liu L. et al. (2022) "Microbial short-chain fatty acids: a bridge between dietary fibers and poultry gut health — a review." *Animal Bioscience*. [PMC9449382](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9449382/). — hindgut/cecal fermentation, SCFA profile.
15. Videvall E., Strandh M., Engelbrecht A., Cloete S., Cornwallis C.K. (2018) "Measuring the gut microbiome in birds: comparison of faecal and cloacal sampling." *Mol. Ecol. Resour.* 18(3):424–434. doi:[10.1111/1755-0998.12744](https://www.biorxiv.org/content/10.1101/160564.full.pdf).
16. Martín-Vivaldi M. et al. (2010) "Symbiotic bacteria living in the hoopoe's uropygial gland prevent feather degradation." *J. Exp. Biol.* 213:3621–3626. doi:[10.1242/jeb.031336](https://dx.doi.org/10.1242/jeb.031336).
17. Diaz-Lora S. et al. (2020) "Great tit (*Parus major*) uropygial gland microbiomes and their potential defensive roles." *Front. Microbiol.* 11:1735. [PMC7401573](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7401573/).
18. Møller A.P. et al. (2009) "Feather micro-organisms and uropygial antimicrobial defences in a colonial passerine bird." *Funct. Ecol.* 23:1097–1105. doi:[10.1111/j.1365-2435.2009.01594.x](https://besjournals.onlinelibrary.wiley.com/doi/10.1111/j.1365-2435.2009.01594.x).
19. Gunderson A.R. et al. (2016) "Feather-degrading bacilli in the plumage of wild birds: prevalence and relation to feather wear." *The Auk* 133(4):583–592. [Oxford Academic](https://academic.oup.com/auk/article/133/4/583/5149256).
20. Zhu R. et al. (2018) "Direct and indirect effects of penguin feces on microbiomes in Antarctic ornithogenic soils." *Front. Microbiol.* 9:552. [PMC5891643](https://pmc.ncbi.nlm.nih.gov/articles/PMC5891643/).
21. Almela P. et al. (2024) "From acidophilic to ornithogenic: microbial community dynamics in moss banks altered by gentoo penguins." *Front. Microbiol.* 15:1362975. [Frontiers](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2024.1362975/full).
22. Gill F., Donsker D., Rasmussen P. (eds.) *IOC World Bird List* v14.1 (2024): 11,032 extant species, 44 orders, 253 families. [worldbirdnames.org/new/updates](https://www.worldbirdnames.org/new/updates/).

**Explicitly flagged as my inference, not sourced:** (i) that the bulk of the 1848 assertions under this node are poultry rather than wild birds — the path profile is suggestive, GOLD does not record the split; (ii) that `bird-associated environment` is the right ENVO label and placement — that is a proposal patterned on `cnidarian-associated environment`, not an ENVO decision; (iii) that the near-40 °C interior functions as a selective filter on colonisers — the temperature is measured, the microbial consequence is a reasonable but here-unsupported extrapolation.

---

## 5. Synonyms, and what NOT to conflate

**Names in real use for this concept** (candidate exact/related synonyms):

- bird-associated environment
- avian-associated environment
- avian host environment
- bird host environment
- Aves-associated environment
- bird-associated habitat / avian habitat *(caution: in ornithology "avian habitat" almost always means the landscape a bird lives in — forest, wetland — which is the opposite of this concept; do not adopt it as a synonym)*
- avian microbiome / bird microbiome *(a community, not an environment — see below)*

**Commonly but wrongly treated as the same thing:**

| Confusable | Why it is different |
|---|---|
| **Aves (`NCBITaxon:8782`)** | A taxon, a class of organisms. The habitat is the environment the organism constitutes. Record as `relation: xref`; do not ground. |
| **Avian/bird microbiome** | The microbial community that occupies the habitat, not the habitat. |
| **Bird nest (`ENVO:00005805`), nesting material (`ENVO:02000004`)** | Constructed habitations. Adjacent, well-populated microbial habitats in their own right, and already named by ENVO. |
| **Ornithogenic soil (`ENVO:00005782`), guano** | Environmental material formed from deposited avian faeces; a bird-*influenced* terrestrial environment, downstream of the host. |
| **Poultry house, litter, hatchery, processing plant** | Engineered environments under GOLD's own top-level split; the bird is an occupant, not the determining system. |
| **Avian food products (`FOODON:00001105`, `FOODON:00001251`, `FOODON:00001131`)** | Commodities derived from birds. |
| **Avian influenza / salmonellosis / any avian disease** | Disease states are not habitats. If such a concept ever arrives from a source, `NOT_APPLICABLE` is the correct disposition — but it is not this concept's. |
| **`ENVO:2100006` feather environment; `UBERON:0000022` feather; `UBERON:0012464` cloacal vent; `BTO:0001420` uropygial gland; `BTO:0000301` crop; `BTO:0000520` gizzard; `BTO:0001699` bursa of Fabricius** | Bird *parts*. Correct grounding targets for the child records under this node, and by this repo's part/whole rule they ground routinely; they are narrower than the host-clade concept. |
| **Cloacal swab ≠ gut** | A sampling caveat worth recording on the child records: cloacal samples do not faithfully represent colon, ileum or cecum communities, and faecal samples represent colon but not ileum/ceca (Videvall et al. 2018). This is a measurement boundary, not a term boundary. |

---

## 6. Should this be a term at all?

**Yes.** Three checks, all passed:

1. **It is a place, not a process, quality or disease.** An organism acting as host is where microbes live — the position ENVO itself takes by minting `plant-associated environment`, `animal-associated environment`, `fungi-associated environment` and `cnidarian-associated environment`. The concept is exactly one clade-step below an existing ENVO class.
2. **It is not merely the taxon.** The distinction this repo has already paid for twice (#112, #114) applies cleanly here: `NOT_APPLICABLE` would be wrong, because it asserts the concept is not a habitat. The correct shape is what is already on the record — minted identity, `ENVO:01001002` as parent, `NCBITaxon:8782 Aves` as `relation: xref`, and an ENVO new-term request for `bird-associated environment`.
3. **It is not a sampling artefact.** 1848 organism-level assertions across 39 distinct anatomical sub-paths, from a curated classification maintained since 1997, is a well-populated and independently reproduced concept, not a stray bin.

**Consistency check against the corpus:** the sibling record `habitatmech:GOLD.3d529a667e` (Fish) carries the identical `CONFIRM_UNGROUNDED` + `ENVO:01001002` parent + ENVO-term-request disposition, with the same rationale ("not grounded there because every host clade would merge onto one record"). Keeping Birds on that footing is the consistent outcome; the only change this research supports is supplying the definition text and the `NCBITaxon:8782` xref.

**One caution on the definition sentence.** If a curator wants the nest, the guano soil and the carcass all under one bird-related umbrella, that is a *different and broader* concept (something like *bird-influenced environment*), and it would need an intermediate class rather than a longer sentence. The GOLD path does not attest that broader concept — its children are all body sites plus `Remains` — so the recommendation is to define the narrow, host-determined concept above and leave nest and ornithogenic soil where ENVO already puts them.

## Citations

1. https://dx.doi.org/10.1093/nar/gkac974
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC5891643/
3. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2024.1362975/full
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC11301535/
5. https://www.nature.com/articles/nbt.1823
6. https://www.sciencedirect.com/science/article/abs/pii/030096299190122S
7. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0091941
8. https://nsojournals.onlinelibrary.wiley.com/doi/10.1111/jav.01788
9. https://pubmed.ncbi.nlm.nih.gov/34393028/
10. https://journals.asm.org/doi/10.1128/mbio.02901-19
11. https://journals.asm.org/doi/10.1128/mbio.00153-20
12. https://dx.doi.org/10.1242/jeb.031336
13. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7401573/
14. https://besjournals.onlinelibrary.wiley.com/doi/10.1111/j.1365-2435.2009.01594.x
15. http://environmentontology.org/
16. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/
17. https://link.springer.com/article/10.1186/2041-1480-4-43
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC10773680/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC9389168/
20. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9449382/
21. https://www.biorxiv.org/content/10.1101/160564.full.pdf
22. https://academic.oup.com/auk/article/133/4/583/5149256
23. https://www.worldbirdnames.org/new/updates/