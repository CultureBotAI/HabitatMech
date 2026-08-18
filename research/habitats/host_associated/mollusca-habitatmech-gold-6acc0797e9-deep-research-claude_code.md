---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:22:45.092091'
end_time: '2026-08-17T16:32:43.129459'
duration_seconds: 598.04
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Mollusca
  habitat_identifier: habitatmech:GOLD.6acc0797e9
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Mollusca'
  assertions: '784'
  parent_terms: ENVO:01001000
  xrefs: FOODON:03412112
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term FOODON:03412112 'mollusc' attached as a parent. Host-taxon reversal\
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
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.6acc0797e9)"
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
  web_search_requests: 16
  num_turns: 40
  total_cost_usd: 3.655047999999999
  session_id: ed43a543-6ef1-4619-9822-d8a4e04be7a8
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 35
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Mollusca
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.6acc0797e9
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Mollusca
- **Upstream assertion volume:** 784
- **Nearest broader term already on the record:** ENVO:01001000
- **Cross-references upstream suggested:** FOODON:03412112

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term FOODON:03412112 'mollusc' attached as a parent. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.6acc0797e9)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Mollusca** as a microbial habitat, with citations.

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

# Novel-term research: **Mollusca** (`habitatmech:GOLD.6acc0797e9`)

> **An animal-associated environment which is determined by a mollusc (phylum Mollusca) or by a part of one.**

Genus: `ENVO:01001002` *animal-associated environment*. Differentia: the determining organism is a mollusc. This deliberately mirrors, word-for-word in structure, ENVO's own already-minted sibling `ENVO:01001179` *cnidarian-associated environment* — "An environmental system determined by a cnidarian or part of a cnidarian" ([OLS4/ENVO](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179)). If the curator wants the ENVO house style verbatim rather than a strict genus-differentia form, the sentence is *"An environmental system determined by a mollusc or part of a mollusc."*

---

## 1. What the concept denotes

**It denotes a mollusc host organism, or any part of one, considered as the place a microbial sample was taken from** — not the phylum, and not the animal as a specimen or a commodity.

The strongest evidence for the intended reading is the GOLD subtree itself. From this repo's own `data/raw/gold_ecosystem_paths.tsv`, `Host-associated > Mollusca` sits at depth 2 (ecosystem category), carries **784 GOLD organisms** across 4 GOLD ecosystem node ids, and has 43 descendant paths. The descendants enumerate the body sites curators actually sample:

| GOLD path (below `Host-associated > Mollusca`) | organisms |
|---|---|
| `> Oyster` | 61 |
| `> Bivalves` | 59 |
| `> Larvae` (and `> Larvae > Spat`) | 22 |
| `> Digestive system > Gut` | 19 |
| `> Digestive system` | 17 |
| `> Respiratory system > Gills` | 17 |
| `> Shell` | 5 |
| `> Tissue` | 5 |
| `> Digestive system > Glands` | 2 |
| `> Reproductive system` (incl. `> Accessory nidamental gland (ANG)`) | 2 |
| `> Circulatory system > Hemolymph` | 1 |
| `> Respiratory system > Gills > Intracellular` / `> Extracellular` | 1 / 1 |
| `> Sensory organs > Light organ` | 1 |
| `> Whole body` | 1 |
| also present with 0 organisms: `> Integumentary system > Mantle > Mantle fluid`, `> Siphon`, `> Integumentary system > Shell > Surface`, `> Digestive system > Midgut > Hepatopancreas/Digestive gland/Hepatic cecum`, `> Hindgut > Intestine: Digesta`, `> Ceca` | 0 |

The same hierarchy exists independently at EBI MGnify, whose biome lineage `root:Host-associated:Mollusca` has children *Digestive system* (819 samples), *Digestive system:Ceca*, *Digestive system:Glands*, *Respiratory system*, *Respiratory system:Gills:Intracellular*, *Respiratory system:Gills:Extracellular*, and *Shell* ([MGnify API](https://www.ebi.ac.uk/metagenomics/api/v1/biomes/root:Host-associated:Mollusca/children)). Studies pathed there include the *Bathymodiolus brooksi* (deep-sea mussel) metagenome assembly from the Aquatic Symbiosis Genomics Project, and snail-microbiome biosamples under `…:Mollusca:Digestive system`.

**Boundary — inside the concept:**

- Any molluscan organ, tissue, fluid or surface as a microbial habitat: gill and gill bacteriocytes, gut/digestive gland/hepatopancreas, hemolymph, mantle and mantle fluid, shell surface, light organ, accessory nidamental gland, larvae and spat, whole body.
- Marine, freshwater **and terrestrial** molluscs. MolluscaBase's own figures give roughly 50,000–55,000 marine, 25,000–30,000 terrestrial and 6,000–7,000 freshwater valid Recent species, with ~86,600 valid extant species as of February 2024 ([MolluscaBase](https://www.molluscabase.org/about.php)). Snail-gut microbiome work spans land, freshwater and marine gastropods ([Li et al. 2023](https://doi.org/10.1186/s40249-023-01159-z)). **Any definition that says "aquatic" is wrong for ~1/3 of the phylum.**
- Both the resident, host-selected community and the transient community the host filters from its surroundings — GOLD's category makes no such distinction.

**Boundary — outside the concept (neighbouring concepts, all attested as separate GOLD nodes or ENVO terms):**

- The **aquaculture facility** the molluscs are grown in: GOLD has `Engineered > Artificial ecosystem > Aquaculture > Molluscs farm / Molluscs pond / Molluscs tank` (± `> Sediment`) as separate paths, and ENVO has `ENVO:01001251` *mollusc farming process* — a process, not a place.
- The **shell-built geographic feature**: ENVO `mussel reef` (`ENVO:01001386`), `neritic mussel reef` (`ENVO:01001380`), `oceanic mussel reef` (`ENVO:01001381`), `Bathymodiolus-dominated oceanic mussel reef` (`ENVO:01001385`), and shell-derived sediments (`marl`, `ENVO:01000853`). These are determined by shells *as material*, not by a living host.
- The **mollusc as food**: FOODON `mollusc` (`FOODON:03412112`), `bivalve` (`FOODON:03412113`), `oyster` (`FOODON:03411224`), `shellfish species` (`FOODON:03411433`).
- The **taxon**: `NCBITaxon:6447` *Mollusca*.
- The surrounding **seawater / sediment** the host filters from; empirically distinguishable, see §3.

**Ambiguity:** the label *Mollusca* is a taxon name being used as an environment name, so on its face it has three readings — (a) the clade, (b) an individual mollusc as a habitat, (c) mollusc-derived material such as shell or tissue as a substrate. The GOLD path `Host-associated > Mollusca` with organ-system children forces reading (b), extended to parts of the host. Reading (a) is the category error this repo already ruled on (#99/#114); reading (c) is ENVO's mussel-reef/marl branch.

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001002` *animal-associated environment*** — "An environmental system determined by an animal", synonyms *Metazoan-associated environment*, *animal environment* ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002)). Molluscs are animals, so this is a safe, non-over-claiming is-a. It is also the term MIxS/NCBI submitters actually use for host-associated `env_broad_scale`/`env_local_scale`.

**No ENVO term names the concept itself.** An OLS4 search of ENVO for *mollusc* returns only `ENVO:01001251` *mollusc farming process* and `ENVO:01000906` *aquaculture process*. A search for *"associated environment"* across ENVO returns the complete host-associated branch: `ENVO:01001000`, `ENVO:01001001`, `ENVO:01001002`, `ENVO:01001041`, `ENVO:01001055`, `ENVO:01001057`, `ENVO:01001058`, `ENVO:01001176`, `ENVO:01001179`. There is no mollusc member. A search of the ENVO issue tracker for `mollusc` (all states) returns only #1018 (a robot report) and #621 (*mussel bed* / *gill tissue*, closed) — so **no new-term request for this concept is pending**.

Near-misses, and why each fails:

| Candidate | Why it is not a match |
|---|---|
| `ENVO:01001176` *environment associated with an aquatic invertebrate* — "An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system" | Wrong on both axes. **Too broad** taxonomically (all aquatic invertebrates: annelids, echinoderms, arthropods…), and **too narrow** ecologically — it asserts an aquatic host habitat, which excludes the ~25,000–30,000 terrestrial molluscs. Grounding here would both merge Mollusca with Annelida/Arthropoda and silently assert aquatic of land snails. |
| `ENVO:01001179` *cnidarian-associated environment* | A **sibling**, not a parent. Its existence is the modelling precedent: ENVO already accepts phylum-level host-associated environment terms, and places this one directly under `ENVO:01001002` (verified via the OLS4 parents call — its only parent is *animal-associated environment*, not the aquatic-invertebrate term). |
| `ENVO:01001055` *environment associated with an animal part or small animal* — "An environmental system determined by part of a living or dead animal, or a whole small animal" (alt. label *animal corpus*) | Narrower and differently scoped: it commits to *part*, *small*, or *dead*. Mollusca includes *Architeuthis* and whole living adult hosts; the concept covers whole hosts of any size, so this asserts something the sources do not. Useful as a parent for the organ-level children (`> Shell`, `> Gills`), not for the phylum node. |
| `ENVO:01001000` *environmental system determined by an organism* (syn. *host-associated environment*) — **the record's current parent** | Correct but not the *smallest* well-established kind. It is two levels up: it admits plant- and fungus-associated environments. Recommend tightening the parent to `ENVO:01001002`. |
| `FOODON:03412112` *mollusc* — **the note claims this is attached as a parent** | An organism/food-source class, not an environment. Parenting a habitat to it asserts the habitat *is a kind of mollusc* — the exact category error #99 was filed about. The record itself correctly has it under `xrefs:`, so the note's prose ("attached as a parent") contradicts the record's structure; worth reconciling, since `tests/test_decisions.py` checks note claims. |
| `NCBITaxon:6447` *Mollusca* | The taxon. Not a place. Keep as `relation: xref`. |
| UBERON | Holds molluscan **parts** only (e.g. `UBERON:0010264` *hepatopancreas*, `UBERON:0006612` *shell*), not a whole-mollusc-as-host term. BTO likewise holds parts (`BTO:0003509` *headfoot*, `BTO:0004995` *osphradium*, `BTO:0005483` *molluscan catch muscle*). |

Standards context: MIxS's host-associated environmental package is the checklist that expects exactly this kind of value paired with `host_taxid`/`host_body_site` ([Yilmaz et al. 2011, *Nat Biotechnol* 29:415–420, doi:10.1038/nbt.1823](https://doi.org/10.1038/nbt.1823)); ENVO issue [#1029](https://github.com/EnvironmentOntology/envo/issues/1029) is the community discussion of host-as-biome terms, and GSC MIxS issue [#196](https://github.com/GenomicsStandardsConsortium/mixs/issues/196) covers symbiont-host sampling — both directly relevant if this becomes an ENVO NTR.

---

## 3. Differentia — what distinguishes it from its siblings

The differentia in the one-sentence definition is just *the host is a mollusc*. What justifies the term being worth minting — the observable, measurable properties that make a molluscan host a distinct habitat from a cnidarian, arthropod, fish or mammalian one — is the following. Each is sourced; none of it belongs in the definition sentence, but it is what a curator would put in a comment or use to defend the NTR.

**a) Host selection is demonstrable and tissue-specific — the host, not the water, defines the community.** In wild *Crassostrea virginica* sampled at six sites across the US East Coast, gill, mantle and stomach communities were significantly different from seawater and sediment at the same site, and communities were **more similar to the same tissue 2,000 km away than to a different tissue at the same site** ([Unzueta-Martínez & Bowen 2024, *Environ Microbiol Rep* 16(5):e70026, doi:10.1111/1758-2229.70026](https://doi.org/10.1111/1758-2229.70026)). Across four Chesapeake bivalves (*C. virginica*, *Ischadium recurvum*, *Macoma balthica*, *Ameritella mitchelli*), each species held a unique core set of microbes including species-specific spirochaete strains, with host species, size, *Perkinsus marinus*/*Zaops ostreum* infection and environment all contributing ([Gignoux-Wolfsohn et al. 2024, *PeerJ* 12:e18082, doi:10.7717/peerj.18082](https://doi.org/10.7717/peerj.18082)). In cephalopods and other molluscs, host phylogeny, habitat and diet are the main drivers, and cephalopod cecal communities (dominated by *Mycoplasma* and *Photobacterium*) cluster apart from other molluscs and from fish ([Kang et al. 2022, *Anim Microbiome* 4:30, doi:10.1186/s42523-022-00184-x](https://doi.org/10.1186/s42523-022-00184-x)).

**b) Suspension feeding makes the habitat a concentrator of the surrounding water column.** This is the property that most sharply separates a bivalve host from a vertebrate host: microbial input is continuous and bulk, so resident-vs-transient membership is a live methodological problem rather than a detail — bivalve studies routinely co-sample marine aggregates and aggregate-free seawater because both plausibly seed the gut ([Arfken et al. 2019, *mSphere* 4(6):e00730-19, doi:10.1128/mSphere.00730-19](https://journals.asm.org/doi/10.1128/msphere.00730-19)). Farmed *C. gigas* communities diverge from their surroundings as the animals grow, and the biomarker taxa shared with the environment decline over the grow-out ([Yang et al. 2023, *Microorganisms*, Laoshan Bay marine ranching](https://pmc.ncbi.nlm.nih.gov/articles/PMC10222713/)).

**c) An open circulatory system means the internal fluid is itself a colonisable habitat.** Oyster hemolymph hosts a complex, dynamic community of bacteria, protists and viruses despite circulating phagocytic hemocytes ([Dupont et al. 2020, *Anim Microbiome* 2:12, doi:10.1186/s42523-020-00032-w](https://doi.org/10.1186/s42523-020-00032-w)); *Mytilus galloprovincialis* hemolymph carries a candidate core of eight genera (*Vibrio*, *Pseudoalteromonas*, *Tenacibaculum*, *Colwellia*, *Shewanella*, *Amphritea*, *Halarcobacter*, an *Arcobacter*-like genus) across a February–November series ([Aquaculture 2023](https://www.sciencedirect.com/science/article/pii/S0044848623008025)); in *Perna viridis*, hemolymph is the one tissue whose phylum-level profile departs from all others, dominated by Spirochaetae ([Front Microbiol 2024;15:1366305](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2024.1366305/full)). GOLD's `> Circulatory system > Hemolymph` node records this directly.

**d) The gill is a chemosynthetic intracellular habitat found in no other molluscan organ and in few other phyla.** Vent and seep bivalves house sulfur- and/or methane-oxidising symbionts intracellularly in gill **bacteriocytes**; in *Solemya velum* the bacteriocytes give symbionts simultaneous access to sulfide, CO₂ and oxygen ([Cavanaugh et al.; review: Roeselers & Newton 2012, *Appl Microbiol Biotechnol*, PMC3304057](https://pmc.ncbi.nlm.nih.gov/articles/PMC3304057/)). Transmission mode differs by lineage — vertical in *Solemya velum* ([Krueger et al. 1996, *Biol Bull* 190(2):195–202, doi:10.2307/1542539](https://www.journals.uchicago.edu/doi/10.2307/1542539)) and vesicomyids, horizontal from seawater in bathymodiolins, with newly formed gill filaments colonised de novo in both ([Wentrup et al. 2014, *Environ Microbiol* 16:3699–3713, PMID 25142549](https://pubmed.ncbi.nlm.nih.gov/25142549/); [Russell et al. 2018, *Proc R Soc B* 285:20182157, PMID 30381385](https://pubmed.ncbi.nlm.nih.gov/30381385/)). GOLD's `> Gills > Intracellular` / `> Extracellular` distinction is exactly this. In shipworms (Teredinidae) the homologous habitat is the **gland of Deshayes**, where *Teredinibacter turnerae* grows in gill bacteriocytes and supplies lignocellulolytic enzymes to a nearly microbe-free cecum ([Waterbury et al. 1983; transport via ducts of Deshayes: *Proc R Soc B* 2022, doi:10.1098/rspb.2022.1478](https://royalsocietypublishing.org/doi/10.1098/rspb.2022.1478); [Gasser et al. 2024, *Microb Biotechnol*, PMC11632262](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11632262/)).

**e) Molluscs supply specialised, spatially bounded organs found in no other host phylum.** The cephalopod **light organ** — crypts colonised exclusively by *Vibrio fischeri*, in a host that hatches uncolonised and whose crypts stay in contact with seawater ([Ruby 1996, *Annu Rev Microbiol* 50:591–624, PMID 8905092](https://pubmed.ncbi.nlm.nih.gov/8905092/); [Nyholm & Ruby ecological review, PMC106330](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC106330/); [Donnelly et al. 2023, *PLOS ONE* 18(7):e0287519, doi:10.1371/journal.pone.0287519](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0287519)). The **accessory nidamental gland** — a female reproductive organ of pigmented, epithelium-lined tubules holding a dense Alphaproteobacteria/Gammaproteobacteria/Verrucomicrobia consortium that is transferred into the egg jelly coat and protects embryos from *Fusarium keratoplasticum* fouling ([Kerwin et al. 2019, *mBio* 10:e02376-19, doi:10.1128/mBio.02376-19](https://journals.asm.org/doi/10.1128/mbio.02376-19); [Collins et al. 2012, *Appl Environ Microbiol*, PMC3370523](https://ncbi.nlm.nih.gov/pmc/articles/PMC3370523)). Both are GOLD nodes (`> Sensory organs > Light organ`, `> Reproductive system > Accessory nidamental gland (ANG)`).

**f) Terrestrial and freshwater gastropods are cellulolytic gut habitats, not marine ones.** *Achatina fulica* crop and intestinal communities are dominated by novel, herbivore-gut-related taxa and shift with a sugarcane diet ([Cardoso et al. 2012, *PLOS ONE* 7(3):e33440, doi:10.1371/journal.pone.0033440](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0033440)); across 73 gastropod species, land and freshwater snails are Proteobacteria/Firmicutes/Bacteroidetes-dominated while marine gastropods are Tenericutes/Proteobacteria/Fusobacteria-dominated, sampled from buccal mass, stomach and intestine ([Li et al. 2023, *Infect Dis Poverty* 12:105, doi:10.1186/s40249-023-01159-z](https://doi.org/10.1186/s40249-023-01159-z)).

**g) Absence of adaptive immunity.** Bivalves rely on innate defence — hemocyte phagocytosis, antimicrobial peptides, fibrinogen-related pattern-recognition proteins in *C. gigas* — which is the mechanistic basis offered for host-mediated selection and for the ease with which resident taxa turn pathobiotic under stress ([Dupont et al. 2020](https://doi.org/10.1186/s42523-020-00032-w); [Gignoux-Wolfsohn et al. 2024](https://doi.org/10.7717/peerj.18082)).

---

## 4. Sources

All primary and standards citations are inline above with DOIs/PMIDs. Ontology and vocabulary facts were checked live against OLS4 (`api/ontologies/envo/terms`, `api/search`) on 2026-08-17, the EBI MGnify biomes API, and this repo's `data/raw/gold_ecosystem_paths.tsv`.

**What is my inference rather than a source statement — flagged explicitly:**

1. That `Host-associated > Mollusca` at depth 2 means *mollusc host, body site unspecified* is inferred from the table's structure (empty `ecosystem_type`/`subtype`/`specific_ecosystem` columns for that row, with organ systems appearing as separate deeper rows). GOLD's own documentation describes the level semantics but does not annotate this particular node.
2. That `ENVO:01001179` *cnidarian-associated environment* constitutes a **precedent** for a phylum-level mollusc term is my reading. What is verifiable is the term's existence, its definition, and that its only asserted parent is `ENVO:01001002`.
3. That the 784 organisms at the phylum node are predominantly bivalve-derived is **not** verified — I did not enumerate the GOLD organism list, and the label distribution is unknown. Do not put a taxonomic composition claim in the definition.
4. The differentia in §3 is a synthesis across independent studies of different molluscan classes; **no single source asserts "molluscan hosts constitute a distinct habitat class"**. The definition sentence therefore rests only on the taxonomic differentia (host is a mollusc), which needs no such claim.
5. Species counts differ by source: MolluscaBase gives ~86,600 valid extant species (Feb 2024) while the FOODON/Wikipedia-derived text on `FOODON:03412112` says ~85,000. Cite MolluscaBase, not the FOODON definition, if a number is used at all.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**

- *mollusc-associated environment* / *mollusk-associated environment* (the ENVO-pattern name a term request would use)
- *molluscan host* / *mollusc host* / *molluscan holobiont*
- *mollusc microbiome* / *molluscan microbiota* (community-shaped phrasing, not habitat phrasing — usable as a related synonym at most)
- *shellfish-associated* (only ever a partial synonym: regulatory usage narrows "shellfish" to filter-feeding bivalves and sometimes extends it to crustaceans — see `FOODON:03411433`)
- `Mollusca` as used in the GOLD ecosystem path and the MGnify biome lineage `root:Host-associated:Mollusca`

**Commonly but wrongly treated as the same thing**

| Do not conflate with | Why |
|---|---|
| `NCBITaxon:6447` *Mollusca* (the taxon) | A class of organisms, not a place. This is the #114/#99 error; keep as `relation: xref`. |
| `FOODON:03412112` *mollusc*, `FOODON:03412113` *bivalve*, `FOODON:03411224` *oyster*, `FOODON:03411433` *shellfish species* | Food-source organism classes. An oyster on a plate is a food product; the same oyster in the water is a habitat. Xref, never parent. |
| `ENVO:01001176` *environment associated with an aquatic invertebrate* | Broader taxonomically, narrower ecologically; asserts *aquatic*, which is false for terrestrial gastropods. |
| `ENVO:01001386` *mussel reef* and kin (`ENVO:01001380`, `01001381`, `01001385`) | Marine reef features made of shell material — determined by shells as substrate, not by a living host. A biofilm on a reef is not a host-associated sample. |
| `ENVO:01000853` *marl*, `ENVO:02000046` *calcareous ooze*, `ENVO:01000082` *biogenous sediment* | Mollusc- and plankton-derived **sediment**. Same shell carbonate, different concept. |
| `ENVO:01001251` *mollusc farming process*, and GOLD `Engineered > … > Aquaculture > Molluscs farm/pond/tank` | A process and a built environment. The oyster is the habitat; the tank is not. |
| The surrounding seawater, sediment or marine aggregates | Empirically distinct communities ([Unzueta-Martínez & Bowen 2024](https://doi.org/10.1111/1758-2229.70026); [Arfken et al. 2019](https://journals.asm.org/doi/10.1128/msphere.00730-19)) — and the whole point of the filter-feeding caveat. |
| Molluscs as **parasite** intermediate hosts (e.g. *Biomphalaria* for schistosomes) | A different relation, and BTO holds the parasite life stages (`BTO:0005513` *cercaria*, `BTO:0005891` *sporocyst*). The snail is still a microbial habitat, but the vector role is not the definition. |
| Molluscan **parts** with their own anatomy terms — `UBERON:0006612` *shell*, `UBERON:0010264` *hepatopancreas*, `BTO:0003509` *headfoot* | Per this repo's rule, a host's parts ground to the anatomy term; the whole host does not. The child records (`> Shell`, `> Gills`, `> Digestive system`) are where those terms belong. |

---

## 6. Should this be a term at all? — Yes

The evidence supports keeping the concept with its own identity and treating it as an ENVO new-term-request candidate. Three independent reasons:

1. **ENVO already accepts this exact pattern at exactly this taxonomic rank.** `ENVO:01001179` *cnidarian-associated environment* is a phylum-level host-associated environment term sitting directly under *animal-associated environment*. A mollusc term is the same construction, one phylum over, and there is no competing term and no pending NTR (issue-tracker search returns nothing).
2. **Two independent large repositories path samples here.** GOLD (784 organisms at the node, 43 descendant paths) and MGnify (`root:Host-associated:Mollusca`, 819 samples under *Digestive system* alone) both need a resolvable term for this node.
3. **The concept is a place, not one of the dispositions `NOT_APPLICABLE` is for.** It is not a disease, quality, process or procedure. The prior `NOT_APPLICABLE` decision was the host-taxon conflation the curation note correctly reverses.

**Two concrete follow-ups for the curator, neither of them the definition:**

- **Tighten the parent from `ENVO:01001000` to `ENVO:01001002`** (*animal-associated environment*). The current parent is correct but two levels too general, and it is the level that also admits plants and fungi; molluscs are animals, so the tighter is-a costs nothing and asserts nothing new. Sibling records for Fish, Mammals, Birds, Reptilia and Sponge should presumably take the same parent, so this is a corpus-wide consistency point, not a one-record tweak.
- **Reconcile the note with the record.** The note says `FOODON:03412112` was "attached as a parent"; the record has it under `xrefs:` (which is right — it is an organism class). Since `tests/test_decisions.py` checks note claims against the repo, the prose should say *xref*.

I have **not** filed anything with ENVO. Per the standing rule, an ENVO term request needs an explicit yes for this specific request; say the word and I will draft the NTR text (ENVO requires definition citations in the issue body, which §3 and §4 already supply) without submitting it.

**Sources:**

- [OLS4 — ENVO:01001002 animal-associated environment](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002)
- [OLS4 — ENVO:01001179 cnidarian-associated environment](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179)
- [OLS4 — ENVO:01001176 environment associated with an aquatic invertebrate](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176)
- [OLS4 — ENVO:01001055 environment associated with an animal part or small animal](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001055)
- [OLS4 — ENVO:01001000 environmental system determined by an organism](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000)
- [ENVO issue #1029 — EnvO terms for host-associated samples](https://github.com/EnvironmentOntology/envo/issues/1029)
- [ENVO wiki — Creating good definitions](https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions)
- [GSC MIxS issue #196 — symbiont hosts and environmental medium](https://github.com/GenomicsStandardsConsortium/mixs/issues/196)
- [Yilmaz et al. 2011, MIMARKS/MIxS, Nat Biotechnol 29:415–420](https://doi.org/10.1038/nbt.1823)
- [JGI GOLD — Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)
- [Mukherjee et al., GOLD v.6, Nucleic Acids Res](https://pmc.ncbi.nlm.nih.gov/articles/PMC5210664/)
- [MGnify API — root:Host-associated:Mollusca children](https://www.ebi.ac.uk/metagenomics/api/v1/biomes/root:Host-associated:Mollusca/children)
- [MolluscaBase — about / species counts](https://www.molluscabase.org/about.php)
- [Unzueta-Martínez & Bowen 2024, Environ Microbiol Rep 16(5):e70026](https://doi.org/10.1111/1758-2229.70026)
- [Gignoux-Wolfsohn et al. 2024, PeerJ 12:e18082](https://doi.org/10.7717/peerj.18082)
- [Kang et al. 2022, Animal Microbiome 4:30](https://doi.org/10.1186/s42523-022-00184-x)
- [Arfken et al. 2019, mSphere 4(6):e00730-19](https://journals.asm.org/doi/10.1128/msphere.00730-19)
- [Yang et al. 2023, farmed C. gigas, Laoshan Bay](https://pmc.ncbi.nlm.nih.gov/articles/PMC10222713/)
- [Dupont et al. 2020, Animal Microbiome 2:12 — oyster hemolymph](https://doi.org/10.1186/s42523-020-00032-w)
- [Mytilus galloprovincialis hemolymph microbiota, Aquaculture 2023](https://www.sciencedirect.com/science/article/pii/S0044848623008025)
- [Perna viridis tissue-scale microbiota, Front Microbiol 2024;15:1366305](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2024.1366305/full)
- [Roeselers & Newton 2012 — chemosynthetic bivalve symbioses review](https://pmc.ncbi.nlm.nih.gov/articles/PMC3304057/)
- [Krueger et al. 1996, Biol Bull 190:195 — Solemya velum vertical transmission](https://www.journals.uchicago.edu/doi/10.2307/1542539)
- [Wentrup et al. 2014, Environ Microbiol — "Forever competent"](https://pubmed.ncbi.nlm.nih.gov/25142549/)
- [Russell et al. 2018, Proc R Soc B 285:20182157 — transmission strategies](https://pubmed.ncbi.nlm.nih.gov/30381385/)
- [Ducts of Deshayes, Proc R Soc B 2022](https://royalsocietypublishing.org/doi/10.1098/rspb.2022.1478)
- [Gasser et al. 2024 — Teredinibacter turnerae membrane vesicles](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11632262/)
- [Ruby 1996, Annu Rev Microbiol 50:591 — V. fischeri/E. scolopes](https://pubmed.ncbi.nlm.nih.gov/8905092/)
- [Nyholm & Ruby — light organ ecological paradigms](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC106330/)
- [Donnelly et al. 2023, PLOS ONE 18(7):e0287519](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0287519)
- [Kerwin et al. 2019, mBio 10:e02376-19 — ANG protects eggs](https://journals.asm.org/doi/10.1128/mbio.02376-19)
- [Collins et al. 2012 — ANG bacterial populations in E. scolopes](https://ncbi.nlm.nih.gov/pmc/articles/PMC3370523)
- [Cardoso et al. 2012, PLOS ONE 7(3):e33440 — Achatina fulica gut](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0033440)
- [Li et al. 2023, Infect Dis Poverty 12:105 — gastropod gut microbiota](https://doi.org/10.1186/s40249-023-01159-z)
- [Bacterial Diversity Associated with Terrestrial and Aquatic Snails, Microorganisms 2024](https://www.mdpi.com/2076-2607/13/1/8)

## Citations

1. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179
2. https://www.ebi.ac.uk/metagenomics/api/v1/biomes/root:Host-associated:Mollusca/children
3. https://www.molluscabase.org/about.php
4. https://doi.org/10.1186/s40249-023-01159-z
5. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
6. https://doi.org/10.1038/nbt.1823
7. https://github.com/EnvironmentOntology/envo/issues/1029
8. https://github.com/GenomicsStandardsConsortium/mixs/issues/196
9. https://doi.org/10.1111/1758-2229.70026
10. https://doi.org/10.7717/peerj.18082
11. https://doi.org/10.1186/s42523-022-00184-x
12. https://journals.asm.org/doi/10.1128/msphere.00730-19
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC10222713/
14. https://doi.org/10.1186/s42523-020-00032-w
15. https://www.sciencedirect.com/science/article/pii/S0044848623008025
16. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2024.1366305/full
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC3304057/
18. https://www.journals.uchicago.edu/doi/10.2307/1542539
19. https://pubmed.ncbi.nlm.nih.gov/25142549/
20. https://pubmed.ncbi.nlm.nih.gov/30381385/
21. https://royalsocietypublishing.org/doi/10.1098/rspb.2022.1478
22. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11632262/
23. https://pubmed.ncbi.nlm.nih.gov/8905092/
24. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC106330/
25. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0287519
26. https://journals.asm.org/doi/10.1128/mbio.02376-19
27. https://ncbi.nlm.nih.gov/pmc/articles/PMC3370523
28. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0033440
29. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176
30. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001055
31. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000
32. https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions
33. https://gold.jgi.doe.gov/ecosystem_classification
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC5210664/
35. https://www.mdpi.com/2076-2607/13/1/8