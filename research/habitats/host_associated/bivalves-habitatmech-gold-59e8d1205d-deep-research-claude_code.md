---
provider: claude_code
model: claude-opus-5[1m]
cached: false
start_time: '2026-08-17T22:06:57.272192'
end_time: '2026-08-17T22:13:39.788564'
duration_seconds: 402.52
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Bivalves
  habitat_identifier: habitatmech:GOLD.59e8d1205d
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Mollusca > Bivalves'
  assertions: '59'
  parent_terms: ENVO:01001002
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Nearest
    broader term ENVO:01001002 ''animal-associated environment'' attached as a parent.
    Bivalves as host. FOODON:03412113 bivalve is a food product class, not a host
    organism, so it is the wrong kind of term entirely. Parented to animal-associated
    environment like the other host clades. ENVO term request. (source concept habitatmech:GOLD.59e8d1205d)'
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
  - claude-opus-5[1m]
  web_search_requests: 7
  num_turns: 22
  total_cost_usd: 2.1965545
  session_id: f1608876-b919-4753-8344-b45e48a4b4d5
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 27
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Bivalves
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.59e8d1205d
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Mollusca > Bivalves
- **Upstream assertion volume:** 59
- **Nearest broader term already on the record:** ENVO:01001002
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:01001002 'animal-associated environment' attached as a parent. Bivalves as host. FOODON:03412113 bivalve is a food product class, not a host organism, so it is the wrong kind of term entirely. Parented to animal-associated environment like the other host clades. ENVO term request. (source concept habitatmech:GOLD.59e8d1205d)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Bivalves** as a microbial habitat, with citations.

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

# Novel-term research: **Bivalves** (`habitatmech:GOLD.59e8d1205d`)

> **A environment associated with an aquatic invertebrate which is determined by a bivalve mollusc (class Bivalvia) acting as a host, encompassing that animal's tissues, body fluids, mantle cavity and shell surfaces.**

An alternative phrasing that matches ENVO's own existing sibling pattern verbatim (and is therefore the one most likely to be accepted in a term request) is:

> **An environmental system determined by a bivalve mollusc or part of a bivalve mollusc.**

That is the exact template of `ENVO:01001179` *cnidarian-associated environment* ("An environmental system determined by a cnidarian or part of a cnidarian"), fetched from OLS4 on 2026-08-17.

---

## 1. What the concept denotes

**The place a sample is taken from:** the body of a living bivalve mollusc — its gill (ctenidial) tissue, digestive tract and digestive gland, haemolymph, mantle and mantle cavity fluid, gonad, and the inner and outer surfaces of its shell — considered as an environmental system colonised by microorganisms. The sample material in practice is homogenised whole soft tissue, a dissected organ, haemolymph, or a shell swab from an individual bivalve.

**Evidence that the whole-organism reading is what the data means.** GOLD's own tree places the anatomical readings *elsewhere*, as siblings of this node rather than as its children (`data/raw/gold_ecosystem_paths.tsv`):

| GOLD path | assertions |
|---|---|
| `Host-associated > Mollusca > Bivalves` | **59** |
| `Host-associated > Mollusca > Oyster` | 61 |
| `Host-associated > Mollusca > Respiratory system > Gills` | 17 |
| `Host-associated > Mollusca > Digestive system > Gut` | 19 |
| `Host-associated > Mollusca > Integumentary system > Mantle > Mantle fluid` | 0 |
| `Host-associated > Mollusca > Shell` | 5 |
| `Host-associated > Mollusca > Whole body` | 1 |

`Bivalves` is a **leaf with no children in GOLD**. Every part-level concept hangs off `Mollusca` directly. So this node is used when the submitter identified the host clade but not (or not only) an organ — the whole-host reading. This is the same shape the repo has already settled for `Mollusca`, `Porifera`, `Sponge`, `Nematoda`, `Reptilia` and `Oyster` under the #114 rule.

**Boundary — what is inside:**
- Any member of class Bivalvia as a host: marine, brackish and freshwater; wild, farmed and laboratory-held; clams, mussels, scallops, cockles, arkshells, shipworms, freshwater unionids, chemosymbiotic lucinids and vesicomyids.
- All body compartments of that host, when the sample is attributed only to the animal.

**Boundary — what is a neighbouring concept:**
- **A named organ of a bivalve** (gill, gut, digestive gland, haemolymph, mantle, shell) → the corresponding anatomy term. Under the repo's part/whole rule, `gills`, `gut`, `hemolymph` ground normally to UBERON/BTO; only the whole organism keeps a minted identity.
- **`Oyster`** (`Host-associated > Mollusca > Oyster`, 61 assertions) — taxonomically a bivalve, but GOLD models it as a **sibling**, not a child. Semantically `Oyster` is narrower than `Bivalves`; in the *data*, the two nodes partition the assertions. Flag this for the curator: the term request can legitimately assert `oyster-associated environment` ⊑ `bivalve-associated environment` even though GOLD's path structure does not.
- **`Mollusca`** (`habitatmech:GOLD.6acc0797e9`, 784 assertions) — the parent already on this record; broader, includes gastropods and cephalopods.
- **Bivalve *aggregations* as benthic features** — `ENVO:01001379` *mussel bed*, `ENVO:01001386` *mussel reef*, `ENVO:01001382` *area of attached mussel assemblages*. These are ecosystem-scale marine features whose sample material is sediment, water or shell matrix in and around a bed. A sample from a mussel bed is **not** a sample from a mussel. This is the single most likely conflation and it should be stated in the term request.
- **Bivalve as food** — see §5.

**Ambiguity:** the label "Bivalves" is not genuinely ambiguous as to *which organisms*; class Bivalvia is a stable, monophyletic taxon (WoRMS AphiaID 105, Linnaeus 1758). The only real ambiguity is **organism vs. place**, which the `Host-associated >` prefix in the source path resolves: GOLD asserts the microbial samples came from bivalves as hosts.

---

## 2. Genus — the broader kind

### Recommended genus: `ENVO:01001176` *environment associated with an aquatic invertebrate*

> "An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system." — ENVO, via OLS4, retrieved 2026-08-17

This is a **better fit than the `ENVO:01001002` currently on the record**, and it is a descendant of it (parents of `ENVO:01001176` are `ENVO:01001002` *animal-associated environment* and `ENVO:01001055` *environment associated with an animal part or small animal*). It fits because:

1. Bivalves are invertebrates (Mollusca, no vertebral column) — WoRMS classification, AphiaID 105.
2. **Every** bivalve is aquatic. WoRMS records Bivalvia as `isMarine: 1, isBrackish: 1, isFreshwater: 1, isTerrestrial: 0` ([WoRMS AphiaID 105](https://www.marinespecies.org/aphia.php?p=taxdetails&id=105), accessed 2026-08-17). Britannica's account states the burrowing, filter-feeding mode of life restricts bivalves to aquatic environments ([Britannica, *Bivalve: Ecology and habitats*](https://www.britannica.com/animal/bivalve/Ecology-and-habitats)). This is a *universal* property of the class, so the subsumption is safe with no exceptions — unlike, say, Gastropoda, which has terrestrial members.
3. `ENVO:01001176` currently has **no children in ENVO** (OLS4 children endpoint returns empty). It is an unpopulated intermediate class waiting for exactly this kind of subclass.

**Note the ENVO placement inconsistency, and say so in the term request:** `ENVO:01001179` *cnidarian-associated environment* — the closest existing analogue, and also an aquatic invertebrate — is asserted directly under `ENVO:01001002`, **not** under `ENVO:01001176`. So ENVO has both a suitable intermediate class and a precedent that bypasses it. The curator should pick one and flag the discrepancy rather than silently choose.

### Near-misses, and why each fails

| Candidate | Why it is not the term | Disposition |
|---|---|---|
| `ENVO:01001002` *animal-associated environment* | Correct but far too broad — the whole of Metazoa. It is a legitimate **ancestor**, which is why it works as the current placeholder parent. | Keep as ancestor; supersede with `ENVO:01001176` if the term request goes forward |
| `ENVO:01001176` *environment associated with an aquatic invertebrate* | **Genus, not identity** — covers sponges, cnidarians, annelids, crustaceans, echinoderms and every other aquatic invertebrate host too. | **Use as genus** |
| `ENVO:01001055` *environment associated with an animal part or small animal* | "part or small animal" asserts a size/partonomy restriction the source does not make; bivalves range from ~1 mm to >1 m (*Tridacna*). Also an ancestor of the genus, so already implied. | Reject |
| `ENVO:01001179` *cnidarian-associated environment* | Wrong clade. Value is as a **definitional template**, not a parent. | Pattern source only |
| `ENVO:01001379` *mussel bed* / `ENVO:01001386` *mussel reef* / `ENVO:01001380/81/88/89` | Marine benthic **features** aligned to CMECS — substrate + biota assemblages, not a host organism's environment. Also restricted to *Mytilus*/*Modiolus*. Narrower **and** a different kind. | Reject; note as the key non-conflation |
| `ENVO:01001392` *mussel gill tissue material* | "Gill tissue material which is part of salt-water mussel in the family Mytilidae" — a **material entity** from one **part** of one **family**. Narrower on all three axes. | Reject |
| `NCBITaxon:6544` *Bivalvia* | The taxon: a class of organisms, not a place. Per this repo's #99/#114 rule the taxon goes in `relation: xref`. | **`relation: xref`** |
| `FOODON:03412113` *bivalve* | Food product class. Already correctly rejected in the recorded note. | Reject |
| `UBERON:7770010` *bivalve adductor muscle*, `BTO:0001682` *byssus*, `BTO:0005483` *molluscan catch muscle*, `UBERON:0006612` *shell* | Anatomical parts. | Reject |
| `ENVO:01001251` *mollusc farming process* | A **process**, and a human activity at that. | Reject |
| `ENVO:03600074` *aquaculture farm* | An anthropogenic site; the neighbouring concept for farmed-bivalve samples where the sample is water or gear, not animal. | Reject |

**Confirmed:** an OLS4 search of ENVO, UBERON, FOODON, PO and BTO for `bivalve`, `mollusc`, `mollusk`, `oyster`, `mussel`, `shellfish` and `shell` (2026-08-17, 40 rows each) returned **no** class denoting bivalves-as-host-environment. The recorded `CONFIRM_UNGROUNDED` stands.

---

## 3. Differentia — what distinguishes it from its siblings

Four properties, each observable and each supported. Ranked by how well they separate this concept from other aquatic-invertebrate hosts.

### (a) The host is a bivalve: a headless, radula-less mollusc with a two-valved shell and ctenidia enlarged into filtration organs

This is the definitional differentia and the one a curator should lead with. Bivalves lack a head and a radula; the gills (ctenidia) are enlarged and specialised for suspension feeding rather than respiration alone ([Britannica, *Bivalve*](https://www.britannica.com/animal/bivalve); [Britannica, *Classification*](https://www.britannica.com/animal/bivalve/Classification)). Consequences for microbial habitat: the gill is a very large, highly vascularised, mucus-covered, continuously water-swept surface — structurally unlike the gut-dominated habitats of most other host clades, and it is where most bivalve symbioses are housed.

Scale: roughly 9,200–20,000 extant species depending on source and counting convention (Britannica cites ~8,000 extant in its classification scheme and ">15,000" elsewhere; [Animal Diversity Web](https://animaldiversity.org/accounts/Bivalvia/) gives ~15,000). *Report the range, not a single number* — the sources disagree, and a definition should not pick one silently.

### (b) The habitat is continuously perfused with, and inoculated by, ambient water — yet is compositionally distinct from it

This is the differentia most directly relevant to microbial ecology and the best-supported empirically.

- Bivalves are suspension feeders that pump large volumes of ambient water across the ctenidia, filtering up to ~40 L h⁻¹ ([Britannica, *Ecology and habitats*](https://www.britannica.com/animal/bivalve/Ecology-and-habitats)).
- Despite that, bivalve microbiomes are **not** a passive reflection of the water column. In wild *Crassostrea virginica* sampled along the US East Coast, oyster-associated microbiomes were distinct from surrounding seawater and sediment, were **tissue-specific**, and were more similar within a tissue type across sites than among tissue types at one site — with a persistent core set per tissue (Environmental Microbiology Reports, Oct 2024, [doi:10.1111/1758-2229.70026](https://doi.org/10.1111/1758-2229.70026)).
- Four Mid-Atlantic bivalves (*C. virginica*, *Macoma balthica*, *Ameritella mitchelli*, *Ischadium recurvum*) differed significantly in bacterial ASV composition by species, each with a core ASV present in all individuals; the authors explicitly frame bivalves as having highly plastic, seawater-influenced microbiomes that nonetheless retain a unique core (PeerJ, Oct 2024, [doi:10.7717/peerj.18082](https://doi.org/10.7717/peerj.18082)).
- The same selectivity holds in fresh water: gut microbiota of four co-occurring Unionidae were distinct from water-column seston, with site physicochemistry explaining ~45% of seston community variation but <8% of mussel microbiome variation — i.e. **selective retention** by the host (PLOS ONE 2019, [doi:10.1371/journal.pone.0224796](https://doi.org/10.1371/journal.pone.0224796)).
- Host species and environment jointly structure gut communities in cohabiting marine bivalves (Microbial Ecology, Feb 2023, [doi:10.1007/s00248-023-02192-z](https://doi.org/10.1007/s00248-023-02192-z)).

**"Continuously inoculated but host-selected" is the single most defensible differentia to put in the definition sentence**, because it is measured, replicated, and holds in both marine and freshwater bivalves.

### (c) Strong internal compartmentalisation: gill vs. digestive tract vs. haemolymph vs. shell

Tissue-specific communities are documented (see the 2024 *Environmental Microbiology Reports* study above); gills tend to be Proteobacteria-dominated while digestive tissue differs (Firmicutes/Bacteroidetes-dominated depending on species). GOLD's own tree mirrors this: `Gills`, `Gut`, `Hemolymph`, `Mantle fluid`, `Shell` are all separately attested under `Mollusca`, and gill is further split into `Extracellular` / `Intracellular` (`gold.ecosystem:4325`, `:4326`). That intracellular subdivision at the *gill* is not present anywhere else in GOLD's Mollusca subtree — it exists because of (d).

### (d) The gill bacteriocyte: an intracellular symbiont compartment characteristic of several bivalve lineages

This is the property that most sharply separates bivalve-associated environments from other aquatic-invertebrate host environments.

- Chemosynthetic symbioses — sulfur-oxidising and methanotrophic gammaproteobacteria housed in gill bacteriocytes — have evolved independently in at least six bivalve families: Solemyidae, Nucinellidae, Mytilidae (bathymodiolins), Lucinidae, Thyasiridae and Vesicomyidae (Taylor & Glover, *Chemosymbiotic Bivalves*, in *The Vent and Seep Biota*, Springer 2010, [doi:10.1007/978-90-481-9572-5_5](https://doi.org/10.1007/978-90-481-9572-5_5); Duperron et al., *Biogeosciences* 2013, [doi:10.5194/bg-10-3241-2013](https://doi.org/10.5194/bg-10-3241-2013)).
- Chemosymbiotic bivalves occur from the intertidal to hadal depths, in sulfidic sands and muds, mangrove sediments, seagrass beds, sunken wood, whale falls, cold seeps and hydrothermal vents; symbiosis appears obligate in all studied Lucinidae, Solemyidae and Vesicomyidae (Taylor & Glover 2010, as above). Lucinidae alone comprises >400 described species.
- Symbiont phylogeny is structured: vesicomyid symbionts form one gammaproteobacterial clade sister to the thioautotrophic *Bathymodiolus* symbionts, distinct from the shallow-water lucinid/thyasirid/solemyid group (Dubilier-lineage review, *Appl Microbiol Biotechnol* 2012, [doi:10.1007/s00253-011-3819-9](https://doi.org/10.1007/s00253-011-3819-9)).
- A non-chemosynthetic parallel: wood-boring shipworms (Teredinidae) house cellulolytic gammaproteobacterial symbionts in gill bacteriocytes; these gill communities are distinct from and less diverse than gut communities and are enriched in plant-cell-wall glycoside hydrolases and biosynthetic gene clusters (*mSystems* 2020, [doi:10.1128/mSystems.00261-20](https://doi.org/10.1128/mSystems.00261-20)).
- In non-chemosymbiotic bivalves the gill still hosts a characteristic community — *Endozoicomonas* dominated *Spondylus spinosus* gills, especially at winter temperatures (*Microorganisms* 2024, [doi:10.3390/microorganisms12010197](https://doi.org/10.3390/microorganisms12010197)).

**Caveat to state explicitly:** chemosymbiosis is characteristic of *several* bivalve families, not of Bivalvia as a whole. It must appear in the definition as an *elaboration*, never as a universal claim. Most bivalves — including all the commercially dominant oysters, mussels and clams that supply the bulk of GOLD's 59 assertions — are heterotrophic suspension feeders without chemosynthetic symbionts.

### (e) Supporting, not differentiating

- **Ecosystem function:** the eastern oyster microbiome carries denitrification potential; live symbiont-containing oysters denitrify more than sediment or shell alone (*PLOS ONE* 2017, [doi:10.1371/journal.pone.0185071](https://doi.org/10.1371/journal.pone.0185071)).
- **Applied relevance:** bivalve–microbiota interactions are an active target for disease prevention in aquaculture (*Curr Opin Biotechnol* 2022, [doi:10.1016/j.copbio.2021.07.026](https://doi.org/10.1016/j.copbio.2021.07.026)); warming shifts bivalve microbiomes with disease and mass-mortality consequences (*Front Mar Sci* 2023, [doi:10.3389/fmars.2023.1182438](https://doi.org/10.3389/fmars.2023.1182438)).
- **Rearing history matters:** moving captivity-raised filter-feeding bivalves into natural environments shifts their gut microbiome (*ISME Communications* 2024, [doi:10.1093/ismeco/ycae125](https://doi.org/10.1093/ismeco/ycae125)) — relevant to how samples under this node should be interpreted, not to the definition.

---

## 4. Sources

Verified against Crossref / OLS4 / WoRMS on 2026-08-17.

**Ontology and vocabulary**
- ENVO `ENVO:01001002` *animal-associated environment*; `ENVO:01001176` *environment associated with an aquatic invertebrate*; `ENVO:01001055`; `ENVO:01001179` *cnidarian-associated environment*; `ENVO:01001379` *mussel bed*; `ENVO:01001386` *mussel reef*; `ENVO:01001392` *mussel gill tissue material* — retrieved from OLS4, https://www.ebi.ac.uk/ols4/api/ontologies/envo
- ENVO term-request procedure and MIxS guidance: https://github.com/EnvironmentOntology/envo ; https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS ; related host-association discussion, ENVO issue #1029, https://github.com/EnvironmentOntology/envo/issues/1029
- WoRMS, *Bivalvia* Linnaeus, 1758, AphiaID 105 — https://www.marinespecies.org/aphia.php?p=taxdetails&id=105 (accessed 2026-08-17). Source for the marine/brackish/freshwater/**not**-terrestrial flags.
- NCBITaxon:6544 *Bivalvia*; FOODON:03412113 *bivalve*; UBERON:7770010 *bivalve adductor muscle*

**Host biology / reference works**
- Encyclopædia Britannica, *Bivalve* — https://www.britannica.com/animal/bivalve ; *Classification* — https://www.britannica.com/animal/bivalve/Classification ; *Ecology and habitats* — https://www.britannica.com/animal/bivalve/Ecology-and-habitats
- Animal Diversity Web, *Bivalvia* — https://animaldiversity.org/accounts/Bivalvia/

**Primary literature — microbiome distinctness and structure**
- Persistent tissue-specific resident microbiota in oysters across a broad geographical range. *Environmental Microbiology Reports*, Oct 2024. [doi:10.1111/1758-2229.70026](https://doi.org/10.1111/1758-2229.70026) · [PMC11500617](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11500617/)
- Bivalve microbiomes are shaped by host species, size, parasite infection, and environment. *PeerJ*, 8 Oct 2024. [doi:10.7717/peerj.18082](https://doi.org/10.7717/peerj.18082) · [PMC11468899](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11468899/)
- Host species and environment shape the gut microbiota of cohabiting marine bivalves. *Microbial Ecology*, 22 Feb 2023. [doi:10.1007/s00248-023-02192-z](https://doi.org/10.1007/s00248-023-02192-z)
- Weingarten, Atkinson & Jackson. The gut microbiome of freshwater Unionidae mussels is determined by host species and is selectively retained from filtered seston. *PLOS ONE*, 13 Nov 2019. [doi:10.1371/journal.pone.0224796](https://doi.org/10.1371/journal.pone.0224796)
- Introduction into natural environments shifts the gut microbiome of captivity-raised filter-feeding bivalves. *ISME Communications*, 2024. [doi:10.1093/ismeco/ycae125](https://doi.org/10.1093/ismeco/ycae125)
- Host–microbiome interactions in a changing sea: the gill microbiome of an invasive oyster under drastic temperature changes. *Microorganisms* 12(1):197, 18 Jan 2024. [doi:10.3390/microorganisms12010197](https://doi.org/10.3390/microorganisms12010197)

**Primary literature — symbiosis**
- Taylor & Glover. Chemosymbiotic Bivalves. In *The Vent and Seep Biota*, Topics in Geobiology, Springer, 2010. [doi:10.1007/978-90-481-9572-5_5](https://doi.org/10.1007/978-90-481-9572-5_5)
- Duperron et al. An overview of chemosynthetic symbioses in bivalves from the North Atlantic and Mediterranean Sea. *Biogeosciences* 10:3241, 14 May 2013. [doi:10.5194/bg-10-3241-2013](https://doi.org/10.5194/bg-10-3241-2013) (open access)
- On the evolutionary ecology of symbioses between chemosynthetic bacteria and bivalves. *Applied Microbiology and Biotechnology*, 2012. [doi:10.1007/s00253-011-3819-9](https://doi.org/10.1007/s00253-011-3819-9) · [PMC3304057](https://pmc.ncbi.nlm.nih.gov/articles/PMC3304057/)
- Secondary metabolism in the gill microbiota of shipworms (Teredinidae). *mSystems*, 30 Jun 2020. [doi:10.1128/mSystems.00261-20](https://doi.org/10.1128/mSystems.00261-20)

**Function and applied context**
- Denitrification potential of the eastern oyster microbiome. *PLOS ONE*, 21 Sep 2017. [doi:10.1371/journal.pone.0185071](https://doi.org/10.1371/journal.pone.0185071)
- Recent advances in bivalve-microbiota interactions for disease prevention in aquaculture. *Current Opinion in Biotechnology*, Feb 2022. [doi:10.1016/j.copbio.2021.07.026](https://doi.org/10.1016/j.copbio.2021.07.026)
- Bivalves and microbes: a mini-review… in a rapidly warming ocean. *Frontiers in Marine Science*, 2 Jun 2023. [doi:10.3389/fmars.2023.1182438](https://doi.org/10.3389/fmars.2023.1182438)

**Explicitly marked as inference, not sourced**
1. *That GOLD's `Bivalves` node denotes the whole-host reading rather than a part.* Inferred from the structure of `data/raw/gold_ecosystem_paths.tsv` (it is a leaf; all part nodes hang off `Mollusca`). GOLD publishes no prose definition of the node.
2. *That `Oyster` should be a subclass of `bivalve-associated environment` in the requested term.* This is taxonomic reasoning (oysters are Ostreidae ⊂ Bivalvia), not a claim GOLD makes — GOLD models them as siblings.
3. *That `ENVO:01001176` is the better genus than `ENVO:01001002`.* My judgement from the two definitions plus the WoRMS aquatic flags; ENVO itself put the analogous cnidarian term under `ENVO:01001002` instead.
4. *That the gill bacteriocyte compartment is the sharpest separator from other aquatic-invertebrate host environments.* Comparative judgement across the cited symbiosis literature; no single source ranks differentiae this way.

---

## 5. Synonyms and what not to conflate

**Synonyms / names in real use (safe to record):**
- bivalve mollusc-associated environment
- Bivalvia-associated environment
- bivalve-associated environment *(recommended primary label for the term request, matching ENVO's `<X>-associated environment` pattern)*
- bivalve host environment / bivalve-associated habitat
- lamellibranch-associated environment *(archaic; Lamellibranchia is a superseded name for the class)*
- pelecypod-associated environment *(archaic; Pelecypoda, likewise superseded)*

Both archaic forms appear in older literature; record them as `RELATED`/deprecated synonyms rather than exact, since neither is exactly coextensive with modern Bivalvia in every historical usage.

**Not synonyms — do not conflate:**

| Wrongly treated as the same | What it actually is |
|---|---|
| **`FOODON:03412113` bivalve**, and the whole FOODON EFSA FoodEx2 block (`25290`–`25520`: oysters, mussels, scallops, clams, cockles, arkshells) | Food product classes. A shucked oyster on a plate is a food material, not a host environment. Already correctly rejected in the recorded curation note. |
| **`NCBITaxon:6544` Bivalvia** | A taxon — a class of organisms, not a place. Per this repo's #99/#114 rule it belongs in `relation: xref`, not as identity and not as `parent_habitats`. |
| **"Shellfish"** | Conflates bivalves with gastropods, crustaceans (shrimp, crab, lobster) and sometimes echinoderms. A culinary/regulatory grouping, not a clade. Never use as a synonym. |
| **`ENVO:01001379` mussel bed / `ENVO:01001386` mussel reef** and kin | Marine benthic features (CMECS-aligned): substrate-plus-biota assemblages. Sample material is sediment, water or conglomerated shell. **The most likely wrong grounding for this concept.** |
| **`ENVO:01001392` mussel gill tissue material** | A material entity from one organ of one family (Mytilidae). Narrower on three axes. |
| **`ENVO:03600074` aquaculture farm / `ENVO:01001251` mollusc farming process** | A site and a process respectively. Farmed-bivalve samples where the material is water, sediment or gear belong here, not under the host concept. |
| **Mollusca** (`habitatmech:GOLD.6acc0797e9`) | Broader — includes gastropods and cephalopods. Correctly the parent, not the same concept. |
| **Bivalves as pathogen vectors** | Filter feeding concentrates human norovirus in gills and digestive gland within 4–24 h, and standard depuration removes bacteria but not norovirus (McLeod et al., *Compr Rev Food Sci Food Saf* 2017, [doi:10.1111/1541-4337.12271](https://doi.org/10.1111/1541-4337.12271); [PMC10969863](https://pmc.ncbi.nlm.nih.gov/articles/PMC10969863/)). This is real and relevant to *why* people sample bivalves — but a transiently filtered virus particle is not a resident of the habitat. Do not let food-safety framing pull the definition toward a food or a contamination concept. |

---

## 6. Should it be a term at all?

**Yes.** This is a host organism acting as a habitat, which is the case the repo settled in #114 and #112: an organism that hosts microbes *is* a place; the *taxon term* is not.

Supporting points:
1. **ENVO already models this exact pattern for a sibling clade.** `ENVO:01001179` *cnidarian-associated environment* is a whole-clade-as-host environment class under `animal-associated environment`. There is no principled reason cnidarians get one and bivalves do not.
2. **The genus class is empty and waiting.** `ENVO:01001176` *environment associated with an aquatic invertebrate* has zero children. A bivalve subclass is the natural first occupant.
3. **59 GOLD assertions** at this node, plus 61 at the sibling `Oyster` node and 784 at the parent `Mollusca` — a real and non-trivial sampling category, not a stray leaf.
4. **The concept is empirically coherent as a habitat**, not just as a taxon: bivalve-associated microbial communities are reproducibly distinct from ambient water and sediment, tissue-structured, and host-species-selected, in both marine and freshwater bivalves (2024 *Env Microbiol Rep*; 2024 *PeerJ*; 2019 *PLOS ONE*). That is exactly the evidence a habitat term needs.
5. It is **not** a process, a quality, a disease state, or a sampling artefact. `NOT_APPLICABLE` would be the wrong disposition and would repeat the #114 error.

**Recommended actions for the curator:**
- Keep `CONFIRM_UNGROUNDED`. The existing decision is correct.
- Add `NCBITaxon:6544` *Bivalvia* with `relation: xref` (the record currently has no xref; the recorded note discusses only the FOODON rejection).
- Consider replacing the placeholder parent `ENVO:01001002` with `ENVO:01001176`, which is a tighter and still fully safe superclass — but note in the decision that ENVO's own cnidarian term bypasses `ENVO:01001176`, so the placement is not unambiguous.
- File the ENVO term request for `bivalve-associated environment` using the `ENVO:01001179` phrasing, with `ENVO:01001176` (or `ENVO:01001002`, matching the cnidarian precedent) as parent. **Per the standing rule, that request needs an explicit go-ahead from you before it is submitted.**

## Citations

1. https://www.marinespecies.org/aphia.php?p=taxdetails&id=105
2. https://www.britannica.com/animal/bivalve/Ecology-and-habitats
3. https://www.britannica.com/animal/bivalve
4. https://www.britannica.com/animal/bivalve/Classification
5. https://animaldiversity.org/accounts/Bivalvia/
6. https://doi.org/10.1111/1758-2229.70026
7. https://doi.org/10.7717/peerj.18082
8. https://doi.org/10.1371/journal.pone.0224796
9. https://doi.org/10.1007/s00248-023-02192-z
10. https://doi.org/10.1007/978-90-481-9572-5_5
11. https://doi.org/10.5194/bg-10-3241-2013
12. https://doi.org/10.1007/s00253-011-3819-9
13. https://doi.org/10.1128/mSystems.00261-20
14. https://doi.org/10.3390/microorganisms12010197
15. https://doi.org/10.1371/journal.pone.0185071
16. https://doi.org/10.1016/j.copbio.2021.07.026
17. https://doi.org/10.3389/fmars.2023.1182438
18. https://doi.org/10.1093/ismeco/ycae125
19. https://www.ebi.ac.uk/ols4/api/ontologies/envo
20. https://github.com/EnvironmentOntology/envo
21. https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
22. https://github.com/EnvironmentOntology/envo/issues/1029
23. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11500617/
24. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11468899/
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC3304057/
26. https://doi.org/10.1111/1541-4337.12271
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC10969863/