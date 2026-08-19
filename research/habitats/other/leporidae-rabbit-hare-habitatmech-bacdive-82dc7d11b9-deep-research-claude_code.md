---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T17:04:02.040538'
end_time: '2026-08-17T17:11:55.659662'
duration_seconds: 473.62
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Leporidae-Rabbit/Hare
  habitat_identifier: habitatmech:BACDIVE.82dc7d11b9
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Leporidae-Rabbit/Hare'
  assertions: '217'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Host-taxon\
    \ reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon\
    \ is not a habitat'. That reasoning is wrong, and the corpus already contradicted\
    \ it \u2014 the same kind of concept was treated as a habitat for Sponge, Nematoda,\
    \ Reptilia, Mammals, Birds and Fish, which keep their own identity and a term\
    \ request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE\
    \ while its own child Porifera > Sponge was a term request.An organism acting\
    \ as a host IS a habitat: it is where the microbe lives, and ENVO models exactly\
    \ this at plant-associated, animal-associated and fungi-associated environment.\
    \ What is not a habitat is the TAXON TERM \u2014 a phylum is a class of organisms,\
    \ not a place \u2014 so the taxon stays an xref (#99) and the concept keeps its\
    \ own identity as a term-request candidate. NOT_APPLICABLE said the concept is\
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:BACDIVE.82dc7d11b9)"
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
  web_search_requests: 18
  num_turns: 34
  total_cost_usd: 3.7651459999999997
  session_id: 369a21df-effa-440b-bfbb-afa365e15f70
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 41
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Leporidae-Rabbit/Hare
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.82dc7d11b9
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Leporidae-Rabbit/Hare
- **Upstream assertion volume:** 217
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:BACDIVE.82dc7d11b9)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Leporidae-Rabbit/Hare** as a microbial habitat, with citations.

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

# Leporidae-Rabbit/Hare (`habitatmech:BACDIVE.82dc7d11b9`) — definition research

> **A** *animal-associated environment* **which is determined by an individual rabbit or hare — a living or recently dead member of the family Leporidae (NCBITaxon:9979) — and comprises the body surfaces, cavities, contents and tissues of that animal that microorganisms inhabit.**

Genus term: `ENVO:01001002` *animal-associated environment* ("An environmental system determined by an animal") — [OLS](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002).
Recommended xref (not identity): `NCBITaxon:9979` *Leporidae* — [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2alpha/taxonomy/taxon/Leporidae).

A caveat that belongs with the definition rather than inside it: ENVO has **no intermediate class** between *animal-associated environment* and a family-level host term — there is no *vertebrate-associated environment* and no *mammal-associated environment*. The definition above therefore jumps several ranks. Saying so is more useful than padding the sentence (see §2).

---

## 1. What the concept denotes

**Source semantics.** This is a BacDive **isolation-source category term**, verified directly against BacDive's isolation-source browser: the hierarchy is three levels, and the term sits at level 3 as **`#Host > #Mammals > #Leporidae (Rabbit/Hare)`**, alongside siblings `#Bovinae (Cow, Cattle)`, `#Canidae (Dog)`, `#Caprinae (Sheep/Goat)`, `#Equidae (Horse)`, `#Felidae (Cat)`, `#Muridae (Mouse/Rat)` and `#Primates` ([bacdive.dsmz.de/isolation-sources](https://bacdive.dsmz.de/isolation-sources)). The vocabulary is described in the BacDive database paper as "organized in a hierarchical ontology that comprises 387 terms on three levels", assigned manually over free-text isolation-source descriptions (Reimer et al., *Nucleic Acids Res* 2022, [PMC8728306](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728306/); current release: Schober et al., *Nucleic Acids Res* 2025;53:D748, [doi:10.1093/nar/gkae959](https://doi.org/10.1093/nar/gkae959)).

**What a sample under this tag is.** A strain tagged here was isolated **from the body of a rabbit or a hare** — the host organism is the sampled environment. The tag itself is host-level only; the body site lives in BacDive's free-text isolation source (e.g. "Rabbit, nose, healthy animal" for *Neisseria* sp. CCUG 45387, [BacDive 151963](https://bacdive.dsmz.de/strain/151963)). Attested site types across the literature and BacDive free text include caecal contents, soft and hard faeces, nasal cavity and sinuses, tonsils, trachea and lung, blood, liver, uterus, skin, and abscesses.

**Inside the concept:** any leporid host regardless of husbandry status — farmed meat rabbit, laboratory rabbit, pet rabbit, wild European rabbit, wild hare — and any body site of that host.

**Boundary — what is a neighbouring concept, not this one:**

| Neighbouring | Why it is outside |
|---|---|
| Rabbit meat, carcass, offal | A food commodity, covered by FOODON (`FOODON:02021512` rabbit carcass, `FOODON:03411323` rabbit); the habitat is the food material, not the living host |
| Rabbit hutch, cage, bedding, litter, manure heap | Engineered/agricultural environment determined by husbandry, not by the animal body |
| Ectoparasites *of* leporids (ticks, fleas) | The arthropod is the host. **This is a real and attested confusion:** *Spiroplasma mirum* SMCA is tagged in BacDive with **both** `#Host > #Arthropoda > #Tick` **and** `#Host > #Mammals > #Leporidae (Rabbit/Hare)`, while its isolation source reads "rabbit tick *Haemaphysalis leporipalustris*" ([BacDive 14358](https://bacdive.dsmz.de/strain/14358)). Strains like this inflate the 217 count with organisms never sampled from a leporid body |
| Pikas (Ochotonidae) | Lagomorphs but not Leporidae ([Lagomorpha](https://en.wikipedia.org/wiki/Lagomorpha)) |
| Guinea pig, chinchilla, lemur | Also caecotrophic, but rodents/primates — convergent physiology, different clade |

**Ambiguity in the label — two readings, not silently resolved:**

1. *Rabbit only* vs *rabbits and hares.* The label resolves this itself: BacDive names the **family**, and the parenthetical "(Rabbit/Hare)" is a gloss covering both vernacular groups. "Rabbit" conventionally covers every leporid genus except *Lepus*; *Lepus* species are hares ([Leporidae](https://en.wikipedia.org/wiki/Leporidae)). The concept is family-wide. This matters because rabbit and hare caeca are measurably different habitats (§3).
2. *The host as a whole* vs *the gut.* The tag makes no anatomical commitment; nasal, blood and abscess isolates carry the same tag. The definition must be host-level, not gut-level.

**Which species dominate the attestations** is an inference, not a sourced fact: BacDive free text and the isolation literature are overwhelmingly *Oryctolagus cuniculus* (`NCBITaxon:9986`) with a wild-hare minority (*Lepus europaeus*, `NCBITaxon:9983`). I did not enumerate the 217 strains to verify this.

---

## 2. Genus — the broader kind, and every near-miss

**Recommended genus: `ENVO:01001002` *animal-associated environment*.** Definition: "An environmental system determined by an animal"; synonyms "Metazoan-associated environment", "animal environment"; parent `ENVO:01001000` *environmental system determined by an organism*; mapped to EMPO "Animal" via the `envoEmpo` subset.

ENVO already applies exactly this pattern per clade, which is the precedent for a term request here:

- `ENVO:01001001` *plant-associated environment* — "An environmental system determined by a green plant."
- `ENVO:01001041` *fungi-associated environment* — "An environmental system determined by a fungal structure."
- `ENVO:01001179` *cnidarian-associated environment* — "An environmental system determined by a cnidarian or part of a cnidarian."
- `ENVO:01001176` *environment associated with an aquatic invertebrate*

**Near-misses checked and rejected:**

| Candidate | Why it fails |
|---|---|
| `ENVO:01001055` *environment associated with an animal part or small animal* | Covers "part of a living or dead animal, or a whole small animal". Wrong on both arms: this concept is a **whole** animal, and a rabbit is not the "small animal" this term targets (it is the pattern used for invertebrate-scale whole organisms). It is the right genus for *rabbit gut* or *rabbit skin* records, not for the host |
| `ENVO:01001000` *environmental system determined by an organism* | Grandparent; too broad — loses "animal" |
| *mammal-associated environment* / *vertebrate-associated environment* | **Do not exist.** ENVO's `animal-associated environment` has only three hierarchical children — aquatic invertebrate, cnidarian, and *human settlement* (`ENVO:01001829`). There is no vertebrate branch at all. This is a genuine ENVO gap, and the right thing to say in the term request |
| Any ENVO rabbit/hare/leporid term | None exists. An OLS search of ENVO for "rabbit" and for "mammal" returns only tangential material terms (`ENVO:02000025` sweat material, `ENVO:02000028` ear wax material, `ENVO:02000004` nesting material) |
| `NCBITaxon:9979` *Leporidae* | A **taxon** — a class of organisms, not a place. Per the corpus rule (#99/#114) this is `relation: xref`, never identity |
| `FOODON:03411323` *rabbit* ("A rabbit which is dead or alive and has a relatively intact body"); `FOODON:00003176` *European rabbit*; `FOODON:02021511` *rabbit material* | Organism / food-material terms in a food ontology. An organism is not an environmental system, and adopting a FOODON term would import a food-commodity commitment the BacDive strains never make |
| UBERON | No whole-leporid term exists. UBERON supplies host **parts** (`UBERON:0001988` feces, gut, skin, lung), which ground body-site records — the correct pattern for the parts, and per the corpus rule the wrong pattern for the whole organism |
| BTO | Only `BTO:0004495` *SIRC cell* (a rabbit corneal fibroblast cell line) — a cell line, not a habitat |
| PO | Plant ontology; not applicable |

**Standards context.** MIxS handles this case not with an environment term but with `host_taxid` (an NCBI taxon id, required in the host-associated extension, [MIxS 0016002](https://genomicsstandardsconsortium.github.io/mixs/0016002/)), with ENVO's own guidance recommending the *ecosystem* for `env_broad_scale` and an UBERON/PO **anatomical part** for `env_local_scale` ([Using ENVO with MIxS](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS)). In other words: the standards community routes host identity through taxonomy and leaves the host-as-environment class unbuilt below "animal". That is precisely the gap this record occupies — and precisely why a term request is defensible rather than redundant.

---

## 3. Differentia — what distinguishes a leporid from its siblings under *animal-associated environment*

The sibling set is other host-taxon environments (bovine-, murid-, canid-, primate-associated). The differentia below are all observable or measurable properties of leporid hosts.

### 3.1 Host clade (definitional differentia)
Family Leporidae, `NCBITaxon:9979`, rank family; order Lagomorpha `NCBITaxon:9975`; >70 extant species in 11 genera, with *Lepus* (`NCBITaxon:9980`, hares, ~32 spp.) and *Sylvilagus* (`NCBITaxon:9987`, cottontails, ~19 spp.) the largest, and the monotypic *Oryctolagus cuniculus* (`NCBITaxon:9986`) the domesticated and near-globally distributed member ([Leporidae](https://en.wikipedia.org/wiki/Leporidae); NCBI Datasets taxonomy).

### 3.2 A gut habitat with no close analogue among domestic mammals
- **Hindgut fermenter with the proportionally largest caecum of any mammal**: roughly **40–60% of total gastrointestinal volume**, ~10× the capacity of the stomach, terminating in a lymphoid vermiform appendix (Rees Davies & Rees Davies, *Vet Clin North Am Exot Anim Pract* 2003;6(1):139–153, [doi:10.1016/S1094-9194(02)00024-5](https://doi.org/10.1016/S1094-9194(02)00024-5); [full text PDF](https://www.medirabbit.com/EN/GI_diseases/Rees-Davies.pdf)).
- **Colonic separation mechanism + caecotrophy**: fine particles (<0.3 mm) are retained by antiperistalsis and excreted as soft faeces that are re-ingested, recycling microbial protein — a trait shared with hares, lemurs, guinea pigs and chinchillas but not with ruminants, pigs, dogs or primates ([Molecular profiling of bacterial species in the rabbit caecum, *Anaerobe* 2005](https://www.sciencedirect.com/science/article/abs/pii/S037810970500042X)).
- **Characteristic physicochemistry**: caecal pH ≈ 6, varying circadially with the feeding/caecotrophy cycle; VFAs supply **30–50% of maintenance energy**, with an atypical molar order — acetate 60–80%, **butyrate 8–20% exceeding propionate 3–10%**, the reverse of the rumen — attributed to community composition rather than substrate (Gidenne, *Animal* 2015;9(2):227–242, [doi:10.1016/j.animal.2014.11.005](https://doi.org/10.1016/j.animal.2014.11.005)).

### 3.3 Community composition, and two conspicuous absences
- Caecum of meat rabbits (n=21, Illumina MiSeq): **Firmicutes 76.6%, Tenericutes 7.5%, Bacteroidetes 7.5%**; genera *Ruminococcus* 5.1%, *Oscillospira* 2.5%, *Bacteroides* 2.4%, *Blautia* 2.3%. **Neither *Lactobacillus* nor Enterobacteriaceae figure among the abundant taxa** — a departure from most mammalian guts (Velasco-Galilea et al., *Front Microbiol* 2018;9:2144, [doi:10.3389/fmicb.2018.02144](https://doi.org/10.3389/fmicb.2018.02144)).
- Whole-GIT survey: Firmicutes dominant throughout (45.9%), Bacteroidetes 38.9% in the large intestine, **Euryarchaeota 25.9% in the foregut**, with four distinct community clusters along the tract ([*Animals*/PMC7824689](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7824689/)).
- The caecal community is **host-specific and largely undescribed**: Combes et al. report it "composed mostly of species not yet described and very specific to that species" (*Animal* 2013;7(9):1429–1439, [PMID 23769161](https://pubmed.ncbi.nlm.nih.gov/23769161/), [doi:10.1017/S1751731113001079](https://doi.org/10.1017/S1751731113001079)).

### 3.4 The concept is not gut-only — non-digestive sites differ sharply
Whole-body 16S survey of 4 rabbits across 12 sites (skin, lung, uterus, mouth, stomach, duodenum, jejunum, ileum, colon, caecum, caecal appendix, rectum): large intestine Firmicutes 78.6% / Bacteroidota 14.2%; **skin, mouth and lung Proteobacteria 36.3%**; uterus Proteobacteria 43.6% (Hu et al., *BMC Microbiol* 2021;21:312, [doi:10.1186/s12866-021-02377-x](https://doi.org/10.1186/s12866-021-02377-x)).

### 3.5 A host-microbe dependency that is close to diagnostic
Rabbits generate their **preimmune antibody repertoire in gut-associated lymphoid tissue** (appendix, sacculus rotundus, Peyer's patches) rather than in bone marrow, and this requires commensal colonisation: in germfree-appendix rabbits, only the combination of *Bacteroides fragilis* and *Bacillus subtilis* consistently promoted GALT development and VDJ diversification, while *B. fragilis* alone, *Clostridium subterminale*, *E. coli* and *Staphylococcus epidermidis* did not (Rhee et al., *J Immunol* 2004, [PMID 14707086](https://pubmed.ncbi.nlm.nih.gov/14707086/); Hanson & Lanning, *Dev Comp Immunol* 2008, [PMC2408667](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2408667/)). This is the strongest available statement that the leporid body is not merely a container but an environment whose properties are co-determined by its microbiota.

### 3.6 Internal heterogeneity the family-level grouping conceals
- **Hare vs rabbit caecum are different fermentation habitats.** On identical substrate in vitro, brown hare caecal content produced ~**0.2 mmol CH₄/kg vs ~13.5 mmol/kg** in domestic rabbit (~60-fold, P<0.001), with lower total SCFA (28.4 vs 51.8 mmol/kg) and higher propionate and isobutyrate molar proportions (Miśta et al., *PLoS ONE* 2015;10(1):e0117117, [doi:10.1371/journal.pone.0117117](https://doi.org/10.1371/journal.pone.0117117)).
- **Geography can outweigh host identity in the wild.** In the first characterisation of the *Lepus europaeus* gut microbiome (3 populations, MiSeq), Firmicutes and Bacteroidetes dominated (45.5% / 19.3%), intestinal samples were 15.7-fold enriched in Proteobacteria over faecal, and **location mattered more than host factors** (Stalder et al., *Sci Rep* 2019;9:2738, [doi:10.1038/s41598-019-39638-9](https://doi.org/10.1038/s41598-019-39638-9)).
- **Rabbits vary more than hares.** In sympatric invasive Australian populations (9 hares, 12 rabbits), faecal microbiome composition varied significantly more between individual rabbits than between hares ([*PeerJ* 2020;8:e9564](https://peerj.com/articles/9564/)).

### 3.7 Characteristic isolates — the taxa this habitat actually yields
Directly relevant to a 217-strain BacDive tag; several species are named *for* the host:

| Organism | Site / source | Reference |
|---|---|---|
| *Streptococcus cuniculi* sp. nov. | Tonsils and nasal samples of wild rabbits | *IJSEM* 2014, [PMID 24801153](https://pubmed.ncbi.nlm.nih.gov/24801153/) |
| *Campylobacter cuniculorum* sp. nov. | Caecal contents of farmed rabbits, Italy | *IJSEM* 2009, [PMID 19542108](https://pubmed.ncbi.nlm.nih.gov/19542108/) |
| *Gemella cuniculi* sp. nov. | Abscess of a rabbit | *IJSEM* 2000;50:2037–2041, [LPSN](https://lpsn.dsmz.de/species/gemella-cuniculi) |
| *Clostridium cuniculi* sp. nov. | Caecotroph, epizootic rabbit enteropathy | Djukovic et al., *Vet Res* 2018;49:123, [PMID 30572930](https://pubmed.ncbi.nlm.nih.gov/30572930/) |
| *Bartonella alsatica* sp. nov. | Blood of wild rabbits (9/30 positive), Alsace | *IJSEM* 1999, [PMID 10028274](https://pubmed.ncbi.nlm.nih.gov/10028274/) |
| *Neisseria leonii* sp. nov. | Nose, lung and liver of rabbits | [PMC11316581](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11316581/) |
| *Pasteurella multocida*, *Bordetella bronchiseptica* | Upper respiratory tract; commensal carriage and "snuffles" | [MSD Vet Manual](https://www.msdvetmanual.com/exotic-and-laboratory-animals/rabbits/bacterial-and-mycotic-diseases-of-rabbits); [PMID 2298879](https://pubmed.ncbi.nlm.nih.gov/2298879/) |
| *Treponema paraluiscuniculi* | Genital/cutaneous lesions (rabbit syphilis) | MSD Vet Manual (as above) |
| *Clostridium spiroforme* (iota-like toxin) | Caecum; enterotoxaemia | Borriello & Carman, *J Clin Microbiol* 1983;17:414–418 |
| *Francisella tularensis* subsp. *holarctica* | Liver/spleen of hares; **hares are the Central European reservoir**, 1.1% of 2,121 hares PCR/culture-positive in Lower Saxony 2006–2009 | Runge et al., *Eur J Wildl Res* 2011; Müller et al., *BMC Microbiol* 2013;13:61, [PMC3663675](https://pmc.ncbi.nlm.nih.gov/articles/PMC3663675/) |

Dysbiosis states of this habitat are themselves well characterised: in epizootic rabbit enteropathy, *Alistipes* and *Ruminococcus* fall while *Bacteroides*, *Akkermansia muciniphila*, *Rikenella*, *Clostridium* and γ-Proteobacteria rise ([*PLoS ONE* 2014;9:e105707](https://doi.org/10.1371/journal.pone.0105707); [*Sci Rep* 2018;8:12489](https://www.nature.com/articles/s41598-018-30178-2)).

### 3.8 Why 217 strains exist at all (scale)
~**570 million rabbits and hares slaughtered globally in 2021** for ~860,000 t of meat (FAOSTAT, summarised in [Compassion in World Farming, *Rabbit Meat Production – Global Review 2024*](https://www.compassioninfoodbusiness.com/media/7458150/rabbit-production-global-review-2024.pdf)); >**125,000 rabbits used in US laboratories in 2023** ([AAVS analysis of USDA data](https://aavs.org/animals-science/animals-used/rabbits/)). The rabbit is simultaneously a livestock species, a companion animal, a major laboratory model (polyclonal antibodies, pyrogen testing) and a widespread wild/invasive animal — four sampling contexts feeding one tag. That the tag mixes them is a property of the concept, not a defect to define away.

---

## 4. Sources

Ontology / vocabulary:
- ENVO `ENVO:01001002` *animal-associated environment* — https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
- ENVO `ENVO:01001001`, `ENVO:01001041`, `ENVO:01001055`, `ENVO:01001176`, `ENVO:01001179` — queried via OLS4 API, August 2026
- ENVO — Buttigieg et al., *J Biomed Semantics* 2013;4:43, [doi:10.1186/2041-1480-4-43](https://doi.org/10.1186/2041-1480-4-43); [OBO Foundry entry](http://obofoundry.org/ontology/envo.html)
- ENVO issue #1029, "EnvO terms for host-associated samples" — https://github.com/EnvironmentOntology/envo/issues/1029
- MIxS host-associated extension (`host_taxid`) — https://genomicsstandardsconsortium.github.io/mixs/0016002/ ; ENVO/MIxS guidance — https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
- NCBI Taxonomy: Leporidae 9979 (family), Lagomorpha 9975, *Lepus* 9980, *L. europaeus* 9983, *O. cuniculus* 9986, *Sylvilagus* 9987

Source database:
- BacDive isolation-source hierarchy — https://bacdive.dsmz.de/isolation-sources (level-3 term `#Leporidae (Rabbit/Hare)` under `#Host > #Mammals`, verified August 2026)
- BacDive strain 14358 (*Spiroplasma mirum* SMCA) — https://bacdive.dsmz.de/strain/14358
- Reimer et al., *Nucleic Acids Res* 2022 — [PMC8728306](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728306/); Schober et al., *Nucleic Acids Res* 2025;53:D748 — [doi:10.1093/nar/gkae959](https://doi.org/10.1093/nar/gkae959)

Primary literature: as cited inline in §3 (Gidenne 2015; Velasco-Galilea 2018; Hu 2021; Combes 2013; Miśta 2015; Stalder 2019; Rhee 2004; Rees Davies 2003; Djukovic 2018; Müller 2013; and the sp. nov. descriptions).

**Explicitly flagged as my inference, not sourced:**
1. That *O. cuniculus* dominates the 217 BacDive strains (§1) — plausible from the literature's composition, unverified against the strain list.
2. That the tick-derived co-tagging seen on BacDive 14358 recurs across the 217 (§1) — one verified instance, frequency unknown.
3. The mapping of BacDive's `#Leporidae (Rabbit/Hare)` onto NCBITaxon:9979 (§2) — BacDive does not publish a taxon-id crosswalk for its category terms; the family-rank correspondence is read off the term label.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept:**
- rabbit-associated environment; hare-associated environment
- leporid-associated habitat / leporid host
- "rabbit" as an isolation source (the near-universal free-text form in strain records)
- `#Leporidae (Rabbit/Hare)` (BacDive exact form — note BacDive uses parentheses; HabitatMech's label carries a hyphen)
- rabbit-associated microbiota / rabbit gut ecosystem (used for the community, not the place — related but not synonymous)

**Commonly but wrongly treated as the same thing:**

| Confused with | Why it is different |
|---|---|
| **Lagomorpha** (`NCBITaxon:9975`) | One rank broader; adds Ochotonidae (pikas) |
| **Rodent** | Rabbits are not rodents — a persistent lay error; Glires is the shared clade, not the family |
| ***Oryctolagus cuniculus*** (`NCBITaxon:9986`) | One species of ~70; narrower. Do not ground a family-level concept to it |
| **Rabbit meat / carcass / offal** (FOODON) | Food commodity; a distinct habitat with its own spoilage and food-safety literature |
| **Rabbitry, hutch, litter, manure** | Engineered/agricultural environment |
| **Rabbit tick / rabbit flea** (*Haemaphysalis leporispalustris*) | Arthropod host — a *different* level-3 BacDive category that co-occurs on the same records |
| ***Encephalitozoon cuniculi***, *Cryptococcus cuniculi* | Eukaryotic microbes whose epithets name the host; not habitats, and *Cryptococcus cuniculi* came from wild rabbit **faeces**, an environmental material |
| **Rabbit cell lines** (`BTO:0004495` SIRC) | In vitro; not a natural habitat |
| **Rabbit faeces / caecum / skin** (UBERON, ENVO material terms) | Body sites and materials — these are the *parts*, which ground normally to anatomy terms; the whole host does not |

---

## 6. Should this be a term at all?

**Yes — mint it, and file it as an ENVO term request.** The evidence supports the curator's note rather than the earlier NOT_APPLICABLE:

- **It is a place where microbes live.** The rabbit body hosts site-differentiated resident communities across at least twelve anatomical sites (Hu 2021), a caecal community that is host-specific and largely uncultured (Combes 2013), and a host-microbe developmental dependency (Rhee 2004). This is an environmental system determined by an organism in exactly ENVO's sense.
- **ENVO already models the pattern** at plant-, fungi-, animal- and cnidarian-associated environment, and its own guidance directs host-associated samples to host taxonomy plus anatomical local-scale terms — leaving the host-level environmental class genuinely unbuilt below "animal".
- **The taxon term is not the habitat.** `NCBITaxon:9979` denotes a class of organisms. It belongs in `relation: xref`, consistent with #99/#114 and with `tests/test_decisions.py` failing NOT_APPLICABLE decisions whose target is an organism term.
- **Volume justifies it**: 217 upstream assertions, a farmed and laboratory species at 10⁸–10⁹ scale annually, and a named-for-the-host isolate list spanning four genera.

Two things worth recording on the term request rather than hiding in the definition:

1. **The missing intermediate.** Requesting *leporid-associated environment* directly under *animal-associated environment* skips vertebrate and mammal. If ENVO would rather build `mammal-associated environment` first, that is the better shape and this record should sit under it. Saying so is more useful than lengthening the definition sentence.
2. **The family-level grouping merges two measurably different habitats.** Rabbit and hare caeca differ ~60-fold in methanogenesis and diverge in VFA profile (Miśta 2015). The source vocabulary groups them, so the record should define at family level — but a curator adding `causal_graphs` or physicochemical parameters later must not attribute rabbit caecal values to hares, in the same way `assertion_count` cannot be summed across sources.

**Suggested record shape:** identity = minted `habitatmech:BACDIVE.82dc7d11b9`; `parent_habitats`: `ENVO:01001002` *animal-associated environment* (genuinely broader); `relation: xref` → `NCBITaxon:9979` *Leporidae*, and optionally `NCBITaxon:9986` *Oryctolagus cuniculus* as the dominant attested host; term-request candidate label *leporid-associated environment* (synonyms *rabbit-associated environment*, *hare-associated environment*).

## Citations

1. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
2. https://api.ncbi.nlm.nih.gov/datasets/v2alpha/taxonomy/taxon/Leporidae
3. https://bacdive.dsmz.de/isolation-sources
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC8728306/
5. https://doi.org/10.1093/nar/gkae959
6. https://bacdive.dsmz.de/strain/151963
7. https://bacdive.dsmz.de/strain/14358
8. https://en.wikipedia.org/wiki/Lagomorpha
9. https://en.wikipedia.org/wiki/Leporidae
10. https://genomicsstandardsconsortium.github.io/mixs/0016002/
11. https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
12. https://doi.org/10.1016/S1094-9194(02
13. https://www.medirabbit.com/EN/GI_diseases/Rees-Davies.pdf
14. https://www.sciencedirect.com/science/article/abs/pii/S037810970500042X
15. https://doi.org/10.1016/j.animal.2014.11.005
16. https://doi.org/10.3389/fmicb.2018.02144
17. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7824689/
18. https://pubmed.ncbi.nlm.nih.gov/23769161/
19. https://doi.org/10.1017/S1751731113001079
20. https://doi.org/10.1186/s12866-021-02377-x
21. https://pubmed.ncbi.nlm.nih.gov/14707086/
22. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2408667/
23. https://doi.org/10.1371/journal.pone.0117117
24. https://doi.org/10.1038/s41598-019-39638-9
25. https://peerj.com/articles/9564/
26. https://pubmed.ncbi.nlm.nih.gov/24801153/
27. https://pubmed.ncbi.nlm.nih.gov/19542108/
28. https://lpsn.dsmz.de/species/gemella-cuniculi
29. https://pubmed.ncbi.nlm.nih.gov/30572930/
30. https://pubmed.ncbi.nlm.nih.gov/10028274/
31. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11316581/
32. https://www.msdvetmanual.com/exotic-and-laboratory-animals/rabbits/bacterial-and-mycotic-diseases-of-rabbits
33. https://pubmed.ncbi.nlm.nih.gov/2298879/
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC3663675/
35. https://doi.org/10.1371/journal.pone.0105707
36. https://www.nature.com/articles/s41598-018-30178-2
37. https://www.compassioninfoodbusiness.com/media/7458150/rabbit-production-global-review-2024.pdf
38. https://aavs.org/animals-science/animals-used/rabbits/
39. https://doi.org/10.1186/2041-1480-4-43
40. http://obofoundry.org/ontology/envo.html
41. https://github.com/EnvironmentOntology/envo/issues/1029