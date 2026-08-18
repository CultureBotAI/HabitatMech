---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T01:25:30.433540'
end_time: '2026-08-18T01:34:03.223749'
duration_seconds: 512.79
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Protist
  habitat_identifier: habitatmech:BACDIVE.a7f6b12719
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Protist'
  assertions: '3'
  parent_terms: (none)
  xrefs: NCIT:C77914
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term NCIT:C77914 'Protista' attached as a parent. Host-taxon reversal\
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
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:BACDIVE.a7f6b12719)"
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
  num_turns: 31
  total_cost_usd: 3.0917514999999995
  session_id: f24fd2d8-0374-4975-9164-47d45491d809
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 31
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Protist
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.a7f6b12719
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Protist
- **Upstream assertion volume:** 3
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** NCIT:C77914

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term NCIT:C77914 'Protista' attached as a parent. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:BACDIVE.a7f6b12719)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Protist** as a microbial habitat, with citations.

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

# Novel-term research: **Protist** (`habitatmech:BACDIVE.a7f6b12719`)

> **Proposed definition:** An environmental system determined by an organism which is determined by a protist — any eukaryote that is not an animal, land plant, or fungus — and which comprises the cell surface, cytoplasm, and membrane-bound compartments that its prokaryotic, archaeal, and viral associates inhabit.

ENVO-style short form, if the curator prefers to match the sibling wording exactly (`ENVO:01001001` is *"An environmental system determined by a green plant."*):

> An environmental system determined by a protist.

The longer form is preferred because "protist" alone is a negatively-defined grade, not a clade, and a reader cannot recover its extension from the word (see §5).

---

## 1. What the concept denotes

**The place is a single eukaryotic cell (or a protist colony/thallus), considered as the site a microbial sample is taken from.** The material a sample is drawn from is the protist cell itself — its surface, its cytoplasm, its vacuoles and perinuclear space — not the pond, soil, or gut the protist was collected from.

The evidence in this repo's own raw data settles the reading. All three BacDive strains behind this concept are bacteria/archaea recovered *from inside or from co-culture with* a protist cell:

| Strain (`characteristic_taxa`) | What the protist actually was |
|---|---|
| *Methanobacterium formicicum* DSM 3637 (`NCBITaxon:1204725`) | Endosymbiotic methanogen isolated from the cytoplasm of the giant sapropelic amoeba *Pelomyxa palustris*, by squashing a single specimen onto anaerobic medium ([van Bruggen et al. 1988](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1550-7408.1988.tb04068.x); [DSMZ DSM-3637](https://www.dsmz.de/collection/catalogue/details/culture/DSM-3637), strain designation PP1, "from giant amoeba *Pelomyxa palustris*") |
| *Haematobacter massiliensis* (`NCBITaxon:195105`) | Basonym *Rhodobacter massiliensis*, isolated from a patient's nose **by amoebal co-culture with *Acanthamoeba polyphaga*** ([Greub & Raoult 2003](https://pubmed.ncbi.nlm.nih.gov/14596900/), doi:10.1016/j.resmic.2003.08.002; reclassified by [Helsel et al. 2007](https://journals.asm.org/doi/abs/10.1128/jcm.01188-06)) |
| *Dysgonomonas* sp. (`NCBITaxon:1891233`) | **Not verified.** I could not identify the BacDive strain or its source. NCBI gives only "Dysgonomonas sp." with no strain designation. Bacteroidales ecto- and endosymbionts of termite gut flagellates are well documented ([Hongoh et al. 2008](https://www.science.org/doi/10.1126/science.1165578)), which makes a flagellate-associated *Dysgonomonas* plausible, but that is my conjecture, not a sourced claim — all confirmed *Dysgonomonas* isolates I found came from whole-gut homogenates, not from picked protist cells. |

GOLD corroborates the same reading with a much larger attestation base: `Host-associated > Protists` (40 organisms) with children `Dinoflagellates`, `Oomycetes`, `Amoebozoa`, `Ciliates`, `Breviatea`, `Excavata > Parabasalids > Anaerobic`, `Nanoflagellates`, `Rhizaria > Foraminifera` (`data/raw/gold_ecosystem_paths.tsv`). GOLD explicitly files protists under **Host-associated**, i.e. as hosts.

### Boundary

**Inside the concept:**
- the protist cytoplasm and its intracellular compartments (most endosymbionts are cytoplasmic; some are membrane-bounded, some associate with mitochondria or mitochondrion-derived organelles, some are intranuclear) — [Husnik et al. 2021](https://www.cell.com/current-biology/fulltext/S0960-9822(21)00747-8), doi:10.1016/j.cub.2021.05.049
- the protist cell surface (ectosymbionts, epibionts)
- protists of every trophic mode: free-living amoebae, ciliates, flagellates, foraminifera, dinoflagellates, oomycetes, and unicellular/colonial algae

**Neighbouring, and *not* this concept:**
- the water body, sediment, or soil the protist was collected from — those are ordinary ENVO environmental terms
- the **animal gut lumen** containing a gut flagellate. A symbiont of a termite hindgut protist sits in two nested habitats; the gut is `ENVO:01001033` *digestive tract environment*, the flagellate cell is this concept. Do not collapse them.
- **fungi-associated environment** (`ENVO:01001041`). GOLD places *Oomycetes* under Protists; oomycetes ("water moulds") are stramenopiles, not fungi, despite the hyphal habit. The two concepts do not overlap.
- **algae/seaweed-associated concepts already in the corpus** (`research/habitats/other/alga-…`, the brown-algae and algae host-associated records). Multicellular macroalgae are conventionally called protists in the five-kingdom scheme (see `FOODON:03412266` *seaweed*: "marine algae (kingdom Protista)"), so this concept and the algal ones **overlap by construction**. The curator has to decide whether "Protist" here excludes macroalgae or is a superset of the algal records.

### One genuine ambiguity the curator must resolve

BacDive's "Protist" tag conflates two different things, and the three strains split across both:

1. **Protist as natural habitat** — the microbe lives in/on protists in nature (*M. formicicum*/*Pelomyxa*).
2. **Protist as laboratory isolation vehicle** — amoebal co-culture, where *Acanthamoeba* is a deliberate enrichment tool applied to a clinical or environmental specimen whose *actual* environment was a human nose (*H. massiliensis*). Amoebal co-culture is a standard recovery technique for amoeba-resisting bacteria ([Greub & Raoult 2004](https://pmc.ncbi.nlm.nih.gov/articles/PMC387402/), doi:10.1128/CMR.17.2.413-433.2004, §"Free-Living Amoebae as a Tool for Isolation").

Reading (2) is a **methodological artefact**, not a habitat. I recommend the definition cover reading (1) only, and that the record carry a usage note saying so — otherwise this term will silently absorb the entire amoebal-co-culture literature, in which the protist is apparatus.

---

## 2. Genus — the broader kind

**Genus: `ENVO:01001000` *environmental system determined by an organism*.**

- Definition: *"An environmental system which is determined by a living organism."*
- It carries the **exact synonym "host-associated environment"**, which is precisely the claim being made here.
- Verified via OLS4: <https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000>

This is also already the genus the corpus uses: the GOLD twin record `data/habitats/host_associated/protists.yaml` (`habitatmech:GOLD.eee7408afd`) has `parent_habitats: [ENVO:01001000]`.

**No ontology term expresses the species-level concept.** Checked and confirmed absent:

| Query | Result |
|---|---|
| `protist` in ENVO (OLS4) | **0 hits** |
| `protozoa` in ENVO (OLS4) | **0 hits** |
| `algae`, `amoeba`, `ciliate` in ENVO | only bloom/material/zone terms; nothing organism-associated |
| Full descendant list of `ENVO:01001000` | plant-, animal-, fungi-associated environment and their parts; **no protist branch** |
| Vendored slice `data/raw/ontology_terms.tsv` | only `NCIT:C77914` Protista, `BTO:0002292` flagellum, `FOODON:03412266` seaweed — no ENVO/UBERON/PO/BTO habitat term |

### Near-misses, and why each fails

- **`ENVO:01001041` fungi-associated environment** — *"An environmental system determined by a fungal structure."* Fails: oomycetes and slime moulds are not fungi; would misassert kingdom membership.
- **`ENVO:01001001` plant-associated environment** — *"determined by a green plant."* Fails for the same reason for algae; unicellular green algae are not green plants in ENVO's sense.
- **`ENVO:01001002` animal-associated environment** — fails; protists are not animals, and using it would drag in the metazoan-specific descendants (`digestive tract environment`, `bone element environment`).
- **`ENVO:01001176` environment associated with an aquatic invertebrate** — *narrower and wrong kingdom*; "invertebrate" is a metazoan grade.
- **`NCIT:C77914` Protista** — this is the **taxon term**, a class of organisms, not a place. Per this repo's own rule (#99, #114) it belongs in `relation: xref`, which is exactly where the record already has it. It is not the genus.
- **`ENVO:01001000` itself** — correct but too broad; adopting it as the identity would erase the distinction from plant-, animal-, and fungi-associated environments.

The four sibling terms under `ENVO:01001000` cover plants, animals, fungi and (via `ENVO:01001179`) cnidarians. **The protist branch is a genuine gap in ENVO's organism-associated tree**, which is a clean term-request story: the same design pattern, one more kingdom-grade sibling. The nearest existing ENVO discussion is [issue #1029, "EnvO terms for host-associated samples"](https://github.com/EnvironmentOntology/envo/issues/1029); I found **no** existing ENVO NTR for a protist-associated environment.

---

## 3. Differentia — what distinguishes it from its siblings

Ordered from most to least defensible:

1. **The host is a protist** — a eukaryote outside Metazoa, Embryophyta and Fungi. This is the primary differentia and it is what all the sibling terms differ on. (Caveat in §5: the grouping is paraphyletic.)
2. **The habitat is a single cell, not a tissue or organ.** This is the sharpest observable difference from the animal/plant/fungal siblings and it has structural consequences the literature states directly: in protists, *organelles play the role that tissues play in animal microbiomes* — symbionts are spatially compartmentalised within one cell, in the cytoplasm, inside host-derived membranes, adjacent to mitochondria, or in the nucleus ([Husnik et al. 2021](https://www.cell.com/current-biology/fulltext/S0960-9822(21)00747-8)). It also means the sampling unit is one cell, which is why this literature is dominated by **single-cell** metagenomics rather than bulk sequencing ([Jiang et al., *Microbiome* 2024](https://link.springer.com/article/10.1186/s40168-024-01809-w), doi:10.1186/s40168-024-01809-w).
3. **Community richness is real, not one-host-one-symbiont.** Despite unicellularity, protists commonly host multi-member communities of comparable richness to some animal microbiomes ([Husnik et al. 2021](https://www.cell.com/current-biology/fulltext/S0960-9822(21)00747-8)). Measured: across 246 ciliate samples spanning Ciliophora, **>90% of ciliates coexisted with bacteria**, yielding 883 bacterial species and 116 novel bacterial + 7 novel archaeal genomes ([*Microbiome* 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11127453/)). A 2025 single-cell study of ciliates and testate amoebae recovered 117 genomes of known eukaryotic endosymbiont lineages (Holosporales, Rickettsiales, Legionellales, Chlamydiae, Babelota) plus 258 host-associated Patescibacteriota genomes, and found **ciliate and amoeba microbiomes differ starkly** — i.e. the habitat is internally structured by host lineage ([Ciobanu et al., *Nat Commun* 16:10336, 2025](https://www.nature.com/articles/s41467-025-65263-4); preprint doi:10.1101/2024.12.29.630703).
4. **Characteristic occupants are intracellular-adapted lineages**, showing genome reduction, toxin–antitoxin systems and nucleotide parasitism ([*Nat Commun* 2025](https://www.nature.com/articles/s41467-025-65263-4)); and, in anoxic hosts, **hydrogenotrophic methanogenic archaea** whose activity can be obligate for host survival ([Husnik & colleagues, *microLife* review](https://academic.oup.com/microlife/article/doi/10.1093/femsml/uqag013/8607828)).
5. **Redox/anoxia is a strong secondary axis.** Sapropelic and hindgut protists are anaerobic, hydrogenosome-bearing, and host methanogens; oxic free-living amoebae host a different guild (*Legionella*, *Mycobacterium*, *Parachlamydia*, *Chlamydia*-like organisms) ([Greub & Raoult 2004](https://pmc.ncbi.nlm.nih.gov/articles/PMC387402/); van Bruggen et al. 1988). If the curator wants intermediate classes later, this is the natural first split.

**My inference, not a sourced claim:** that (2) — one-cell scale — is the *definitional* differentia rather than merely a correlate. No source states it as a definition; I am reading it off the shared structure of the ENVO sibling pattern.

---

## 4. Sources

**Primary literature — the habitat and its communities**
- Husnik F, Tashyreva D, Boscaro V, George EE, Lukeš J, Keeling PJ (2021). *Bacterial and archaeal symbioses with protists.* **Current Biology** 31(13):R862–R877. doi:[10.1016/j.cub.2021.05.049](https://doi.org/10.1016/j.cub.2021.05.049) · PMID 34256922 · <https://www.cell.com/current-biology/fulltext/S0960-9822(21)00747-8> — *the single best citation for the definition.*
- Jiang et al. (2024). *Exploring the landscape of symbiotic diversity and distribution in unicellular ciliated protists.* **Microbiome** 12. doi:[10.1186/s40168-024-01809-w](https://doi.org/10.1186/s40168-024-01809-w) · PMID 38790063 · [PMC11127453](https://pmc.ncbi.nlm.nih.gov/articles/PMC11127453/)
- Ciobanu et al. (2025). *Single-cell genomics reveals complex microbial and viral associations in ciliates and testate amoebae.* **Nature Communications** 16:10336, 24 Nov 2025. <https://www.nature.com/articles/s41467-025-65263-4> · PMID 41285752
- *Living together: evolutionary and ecological dimensions of protist endosymbiosis.* **microLife**, doi:[10.1093/femsml/uqag013](https://doi.org/10.1093/femsml/uqag013) · <https://academic.oup.com/microlife/article/doi/10.1093/femsml/uqag013/8607828>
- Greub G, Raoult D (2004). *Microorganisms resistant to free-living amoebae.* **Clin Microbiol Rev** 17(2):413–433. doi:[10.1128/CMR.17.2.413-433.2004](https://doi.org/10.1128/CMR.17.2.413-433.2004) · PMID 15084508 · [PMC387402](https://pmc.ncbi.nlm.nih.gov/articles/PMC387402/)
- Hongoh Y et al. (2008). *Genome of an endosymbiont coupling N₂ fixation to cellulolysis within protist cells in termite gut.* **Science** 322:1108–1109. doi:[10.1126/science.1165578](https://doi.org/10.1126/science.1165578)
- Song, Zhao, Hou & Miao (2023). *Cellular interactions and evolutionary origins of endosymbiotic relationships with ciliates.* **Microbiol Mol Biol Rev** 87.

**Primary literature — the specific strains on this record**
- van Bruggen JJA, Zwart KB, Hermans JGF, van Hove EM, Stumm CK, Vogels GD (1988). *Isolation of a methanogenic endosymbiont of the sapropelic amoeba* Pelomyxa palustris *Greeff.* **J Protozool** 35:20–23. doi:[10.1111/j.1550-7408.1988.tb04068.x](https://doi.org/10.1111/j.1550-7408.1988.tb04068.x)
- DSMZ catalogue, DSM 3637 (*M. formicicum* PP1, "from giant amoeba *Pelomyxa palustris*"): <https://www.dsmz.de/collection/catalogue/details/culture/DSM-3637>
- Draft genome of *M. formicicum* DSM 3637. **J Bacteriol** 194(24):6967. PMID 23209223 · [PMC3510631](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3510631/) — **note the caveat**: the genome shows no endosymbiont reduction and the strain cultures easily, suggesting a free-living lifestyle; a [2017 study](https://www.sciencedirect.com/science/article/abs/pii/S1434461017300536) of *P. palustris* cysts recovered *Methanosaeta*, *Syntrophorhabdus* and *Rhodococcus* and **no** *M. formicicum*. The historic isolation is not in doubt; the symbiotic interpretation is contested.
- Greub G, Raoult D (2003). *Rhodobacter massiliensis sp. nov., a new amoebae-resistant species isolated from the nose of a patient.* **Res Microbiol** 154(9):631–635. doi:[10.1016/j.resmic.2003.08.002](https://doi.org/10.1016/j.resmic.2003.08.002) · PMID 14596900
- Helsel LO et al. (2007). *Identification of "Haematobacter" … reclassification of* Rhodobacter massiliensis. **J Clin Microbiol**. doi:[10.1128/jcm.01188-06](https://doi.org/10.1128/jcm.01188-06) · PMID 17287332

**Standards and reference vocabularies**
- ENVO `ENVO:01001000` *environmental system determined by an organism*, syn. *host-associated environment* — <http://purl.obolibrary.org/obo/ENVO_01001000>; siblings `ENVO:01001001`, `ENVO:01001002`, `ENVO:01001041`, `ENVO:01001179`
- ENVO issue #1029, *EnvO terms for host-associated samples* — <https://github.com/EnvironmentOntology/envo/issues/1029>
- NCIT `NCIT:C77914` *Protista* — "A taxonomic kingdom that includes algae, protozoa, slime molds, and water molds" (via OLS4); `NCIT:C77916` *Protozoa*
- Adl SM et al. (2019). *Revisions to the Classification, Nomenclature, and Diversity of Eukaryotes.* **J Eukaryot Microbiol** 66(1):4–119. doi:[10.1111/jeu.12691](https://doi.org/10.1111/jeu.12691) · PMID 30257078 · [PMC6492006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6492006/) — the current authority; **it does not recognise "Protista" as a taxon.**
- BacDive isolation-source vocabulary (three-level Cat1/Cat2/Cat3 controlled vocabulary), introduced in Reimer LC et al., *BacDive in 2019*, **Nucleic Acids Res** 47:D631–D636, doi:[10.1093/nar/gky879](https://doi.org/10.1093/nar/gky879); current release Schober I et al., *BacDive in 2025*, **NAR** 53(D1):D748–D756, doi:[10.1093/nar/gkae959](https://doi.org/10.1093/nar/gkae959). <https://bacdive.dsmz.de/isolation-sources>

**Explicitly unverified.** I could not retrieve BacDive's exact Cat1/Cat2 parents for the "Protist" tag — the help page documents only the three-level structure with an `#Environmental / #Aquatic / #Marine` example, and the browser is JS-rendered. The claim that BacDive files Protist under a host-type category is my inference from the strain evidence and from GOLD's parallel `Host-associated > Protists` path, **not** something I read in BacDive's documentation. The identity and source of the *Dysgonomonas* sp. strain is likewise unverified.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- protist-associated environment / protist-associated habitat
- protist microbiome; protist-associated microbiota
- protozoan-associated environment *(narrower — see below)*
- host protist cell; symbiont-bearing protist cell
- "Protists" (GOLD, `Host-associated > Protists`); "Protist" (BacDive)

**Do not conflate with:**
- **Protozoa** (`NCIT:C77916`, "unicellular *heterotrophic* eukaryote"). Protozoa is a *proper subset*: it excludes algae, oomycetes and slime moulds, all of which GOLD files under Protists. Treating the two as synonyms silently drops the autotrophs.
- **The taxon *Protista* itself** (`NCIT:C77914`). A kingdom is a class of organisms, not a place. It belongs on this record as `relation: xref`, which is where it already is. This distinction is the entire point of #99/#114.
- **Algae / seaweed / phycosphere.** `FOODON:03412266` *seaweed* explicitly places macroalgae in "kingdom Protista," so the corpus's algal records overlap this concept. Decide the containment explicitly; do not leave it implicit.
- **Fungi-associated environment** (`ENVO:01001041`). Oomycetes and slime moulds look fungal and are not.
- **The gut/rumen/water the protist came from.** Nested habitats, not the same habitat.
- **Amoebal co-culture isolates.** The protist there is laboratory apparatus (§1, ambiguity).
- **"Microbial eukaryote"** used loosely — under most usages it excludes macroalgae and includes microscopic fungi, so it is not a drop-in synonym either.

**The honest caveat that belongs in the record's comment field:** "protist" is a **paraphyletic grade defined by exclusion**, not a clade. The current authoritative classification of eukaryotes ([Adl et al. 2019](https://doi.org/10.1111/jeu.12691)) is rank-free and does not use *Protista*; the only ontology term naming it is NCIT's legacy five-kingdom entry. The concept is nonetheless *operationally* well-defined for habitat purposes — GOLD, BacDive and the symbiosis literature all use it — and negatively-defined genera are already accepted in ENVO's neighbourhood. But the definition should say "not an animal, land plant, or fungus" out loud rather than lean on the word.

---

## 6. Should this be a term at all?

**Yes — it is a habitat, and it is a good term-request candidate.** Four independent lines support this:

1. **ENVO already models exactly this pattern** for plants, animals, fungi and cnidarians under `ENVO:01001000`. A protist sibling is a gap, not a novel modelling proposal.
2. **A protist cell demonstrably *is* where microbes live** — >90% of ciliates carry bacteria; 883 bacterial species and 123 novel genomes recovered from ciliate cells alone ([*Microbiome* 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11127453/)).
3. **Both upstream sources treat it as a habitat**, and GOLD files it under Host-associated with a full sub-tree and 40 organism assertions.
4. The curator's `CONFIRM_UNGROUNDED` reasoning holds up: the host-taxon reversal is correctly applied here.

Two things it is **not**: it is not a process, quality, or disease state; and it is not a `NOT_APPLICABLE` case. The one genuine risk of a **sampling artefact** is the amoebal-co-culture reading (§1), which is a scoping note on the definition rather than a reason to withhold the term.

### Three repo-level issues the curator should handle alongside the definition

- **A duplicate record already exists.** `data/habitats/host_associated/protists.yaml` (`habitatmech:GOLD.eee7408afd`, label "Protists", 40 ORGANISM assertions, `parent_habitats: [ENVO:01001000]`, still `SEEDED`) is the *same concept* with 13× the assertion volume. This BacDive record (3 STRAIN) is currently the only one that has been reasoned about. Given #116/#117 ("a decision can say two novel concepts are the same"), these should almost certainly be merged, or at minimum the BacDive record should take the GOLD record as its parent. Writing a definition for the 3-strain record while the 40-organism record sits undecided is the wrong way round.
- **The category disagrees with the twin.** This record is `habitat_category: OTHER`; the GOLD twin is `HOST_ASSOCIATED`. The curation note itself argues the concept is host-associated. `OTHER` should not survive the merge.
- **The note's prose does not match the record.** The recorded note says "Nearest broader term NCIT:C77914 'Protista' attached as a **parent**," but the record has it under `xrefs` with no `parent_habitats` — which is the *correct* placement per the repo's own rule. The prose is stale relative to what was written. Worth fixing before `tests/test_decisions.py` grows a check for it. The genus to attach as an actual parent is `ENVO:01001000`, matching the GOLD twin.

**Sources:**
- [Bacterial and archaeal symbioses with protists — Current Biology 2021](https://www.cell.com/current-biology/fulltext/S0960-9822(21)00747-8)
- [Exploring the landscape of symbiotic diversity and distribution in unicellular ciliated protists — Microbiome 2024](https://link.springer.com/article/10.1186/s40168-024-01809-w)
- [Single-cell genomics reveals complex microbial and viral associations in ciliates and testate amoebae — Nature Communications 2025](https://www.nature.com/articles/s41467-025-65263-4)
- [Living together: evolutionary and ecological dimensions of protist endosymbiosis — microLife](https://academic.oup.com/microlife/article/doi/10.1093/femsml/uqag013/8607828)
- [Microorganisms Resistant to Free-Living Amoebae — Clin Microbiol Rev 2004](https://pmc.ncbi.nlm.nih.gov/articles/PMC387402/)
- [Genome of an endosymbiont coupling N2 fixation to cellulolysis within protist cells in termite gut — Science 2008](https://www.science.org/doi/10.1126/science.1165578)
- [Isolation of a methanogenic endosymbiont of the sapropelic amoeba Pelomyxa palustris — J Protozool 1988](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1550-7408.1988.tb04068.x)
- [DSMZ catalogue: DSM 3637](https://www.dsmz.de/collection/catalogue/details/culture/DSM-3637)
- [Draft genome sequence of Methanobacterium formicicum DSM 3637 — J Bacteriol 2012](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3510631/)
- [Identification of Pelomyxa palustris endosymbionts — Eur J Protistol 2017](https://www.sciencedirect.com/science/article/abs/pii/S1434461017300536)
- [Rhodobacter massiliensis sp. nov. — Res Microbiol 2003](https://pubmed.ncbi.nlm.nih.gov/14596900/)
- [Reclassification as Haematobacter massiliensis — J Clin Microbiol 2007](https://journals.asm.org/doi/abs/10.1128/jcm.01188-06)
- [Revisions to the Classification, Nomenclature, and Diversity of Eukaryotes — J Eukaryot Microbiol 2019](https://onlinelibrary.wiley.com/doi/10.1111/jeu.12691)
- [ENVO issue #1029 — EnvO terms for host-associated samples](https://github.com/EnvironmentOntology/envo/issues/1029)
- [BacDive isolation sources search](https://bacdive.dsmz.de/isolation-sources) · [BacDive in 2025 — NAR](https://academic.oup.com/nar/article/53/D1/D748/7848838)

## Citations

1. https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1550-7408.1988.tb04068.x
2. https://www.dsmz.de/collection/catalogue/details/culture/DSM-3637
3. https://pubmed.ncbi.nlm.nih.gov/14596900/
4. https://journals.asm.org/doi/abs/10.1128/jcm.01188-06
5. https://www.science.org/doi/10.1126/science.1165578
6. https://www.cell.com/current-biology/fulltext/S0960-9822(21
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC387402/
8. https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000
9. https://github.com/EnvironmentOntology/envo/issues/1029
10. https://link.springer.com/article/10.1186/s40168-024-01809-w
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC11127453/
12. https://www.nature.com/articles/s41467-025-65263-4
13. https://academic.oup.com/microlife/article/doi/10.1093/femsml/uqag013/8607828
14. https://doi.org/10.1016/j.cub.2021.05.049
15. https://doi.org/10.1186/s40168-024-01809-w
16. https://doi.org/10.1093/femsml/uqag013
17. https://doi.org/10.1128/CMR.17.2.413-433.2004
18. https://doi.org/10.1126/science.1165578
19. https://doi.org/10.1111/j.1550-7408.1988.tb04068.x
20. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3510631/
21. https://www.sciencedirect.com/science/article/abs/pii/S1434461017300536
22. https://doi.org/10.1016/j.resmic.2003.08.002
23. https://doi.org/10.1128/jcm.01188-06
24. http://purl.obolibrary.org/obo/ENVO_01001000
25. https://doi.org/10.1111/jeu.12691
26. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6492006/
27. https://doi.org/10.1093/nar/gky879
28. https://doi.org/10.1093/nar/gkae959
29. https://bacdive.dsmz.de/isolation-sources
30. https://onlinelibrary.wiley.com/doi/10.1111/jeu.12691
31. https://academic.oup.com/nar/article/53/D1/D748/7848838