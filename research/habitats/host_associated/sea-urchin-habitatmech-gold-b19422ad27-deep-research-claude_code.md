---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T22:13:46.947421'
end_time: '2026-08-17T22:23:19.759793'
duration_seconds: 572.81
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Sea Urchin
  habitat_identifier: habitatmech:GOLD.b19422ad27
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Invertebrates > Echinodermata > Sea Urchin'
  assertions: '53'
  parent_terms: (none)
  xrefs: FOODON:03412107
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term FOODON:03412107 'sea urchin' attached as a parent. Organism-identity\
    \ screen (#109): grounded EXACT to FOODON:03412107 'sea urchin', which is an echinoderm\
    \ \u2014 an organism, not a place. The screen that exists to catch exactly this\
    \ reported 0 for months because it tested only NCIT and mesh ancestry and only\
    \ the record's identity; widening it to UBERON:0000468 and to parent_habitats\
    \ surfaced this family. The GOLD path says host-associated, so the concept is\
    \ the environment the organism provides, which is the same family as the sponge,\
    \ nematode and reptile term requests. The organism term is kept as an xref (#99)\
    \ rather than an identity. (source concept habitatmech:GOLD.b19422ad27)"
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
  num_turns: 48
  total_cost_usd: 3.9888570000000003
  session_id: 58b53163-b8e6-4793-b8ba-1a2521d9aae1
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 27
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Sea Urchin
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.b19422ad27
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Invertebrates > Echinodermata > Sea Urchin
- **Upstream assertion volume:** 53
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** FOODON:03412107

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term FOODON:03412107 'sea urchin' attached as a parent. Organism-identity screen (#109): grounded EXACT to FOODON:03412107 'sea urchin', which is an echinoderm — an organism, not a place. The screen that exists to catch exactly this reported 0 for months because it tested only NCIT and mesh ancestry and only the record's identity; widening it to UBERON:0000468 and to parent_habitats surfaced this family. The GOLD path says host-associated, so the concept is the environment the organism provides, which is the same family as the sponge, nematode and reptile term requests. The organism term is kept as an xref (#99) rather than an identity. (source concept habitatmech:GOLD.b19422ad27)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Sea Urchin** as a microbial habitat, with citations.

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

# Sea Urchin — `habitatmech:GOLD.b19422ad27`

## Proposed definition

> An animal-associated environment which is determined by a living sea urchin (Echinoidea), in which microorganisms inhabit the compartments the host provides — principally the digestive tract and its digesta, the coelomic fluid, and the spine-bearing external surface of the test.

ENVO house-style variant, matching the phrasing of the one existing host-clade sibling `ENVO:01001179` *cnidarian-associated environment* ("An environmental system determined by a cnidarian or part of a cnidarian"), if the term request is written for ENVO rather than for HabitatMech:

> An environmental system determined by a sea urchin or part of a sea urchin.

**Two structural findings up front, because they change what the curator should do:**

1. **This is not the Porifera/Sponge situation.** "Sponge" was a vernacular restatement of its own parent node and the sponge report recommended `SAME_AS`. Here, `Sea Urchin` (53 organisms) is a genuine proper subset of its parent `Echinodermata` (21 organisms), with two attested siblings — `Sea cucumber` (17) and `Sea Star` (16). It warrants its own term, not a merge. (Counts from `data/raw/gold_ecosystem_paths.tsv`; repo data, not literature.)
2. **ENVO already has an echinoderm-specific environment class** — `ENVO:01001187` *holothurian digestive tract* — which is a strong precedent that this family is in ENVO's scope, and which also shows the shape ENVO chose (class-scoped, *organ*-scoped). It is a near-miss, not a match, for reasons in §2.

---

## 1. What the concept denotes

### The reading the data means

GOLD's path is `Ecosystem = Host-associated → Ecosystem Category = Invertebrates → Ecosystem Type = Echinodermata → Ecosystem Subtype = Sea Urchin`. The `Host-associated` root fixes the frame: the place is the host body, not the water or seabed around it. The Ecosystem Type level is the host clade (phylum Echinodermata); the Subtype level narrows it to one of the phylum's classes by vernacular name.

So **"Sea Urchin" denotes the body of a living echinoid animal, sampled as the place a microbial community lives** — a piece of urchin gut, gut content, coelomic fluid, or surface tissue, from which DNA is extracted or from which a strain is isolated. All 53 upstream assertions are `assertion_unit: ORGANISM` — isolate/genome records attributed to this node — with no compartment breakdown recorded upstream.

### The compartments inside the concept

The urchin body is not one habitat but several, and the literature treats them as such:

| Compartment | What it is | Evidence |
|---|---|---|
| **Gut tissue** (epithelium) | The resident, host-associated community; sharply distinct from the lumen contents | Dominated by chemolithoautotrophic Campylobacterota — *Arcobacter* ~20%, *Sulfurimonas* ~12% in *S. purpuratus* ([Hakim et al. 2019, *Microorganisms* 7:35](https://doi.org/10.3390/microorganisms7020035)); Campylobacteraceae 93% in *L. variegatus* ([Hakim et al. 2016, *FEMS Microbiol Ecol* 92:fiw146](https://doi.org/10.1093/femsec/fiw146)) |
| **Gut digesta / fecal pellets** | The lumen contents; more transient, diet-sourced | *Psychromonas* ~40%, *Propionigenium* ~15%, Flavobacteriales ~25% ([Hakim et al. 2019](https://doi.org/10.3390/microorganisms7020035)); a single ASV matching *Psychromonas marina* at 100% identity accounted for 44% of reads in *S. droebachiensis* ([Bengtsson et al. 2025, *FEMS Microbiol Ecol* 101:fiaf006](https://doi.org/10.1093/femsec/fiaf006)) |
| **Pharynx** (inside Aristotle's lantern) | Higher richness, resembles the water community | ([Hakim et al. 2019](https://doi.org/10.3390/microorganisms7020035)) |
| **Coelomic fluid and coelomocytes** | An internal liquid compartment, formerly assumed sterile; it is not | Proteobacteria, Bacteroidetes, Fusobacteria dominate in *P. lividus* ([Faddetta et al. 2020, *Sci Rep* 10:21443](https://doi.org/10.1038/s41598-020-78534-5)); Firmicutes, Izemoplasmatales and Flavobacteriaceae enriched in *P. lividus* and *A. lixula* ([Arranz et al. 2025, *Front Mar Sci* 12:1615711](https://doi.org/10.3389/fmars.2025.1615711)) |
| **External surface — spines, test, tube feet** | An epibiotic community the host actively resists fouling on | Species-specific and trophic-niche-dependent across four Caribbean species ([Rodríguez-Barreras et al. 2023, *Microorganisms* 11:391](https://doi.org/10.3390/microorganisms11020391)); shifts with bald sea urchin disease ([Cavaliere et al. 2023, *Pathog Dis* 81:ftad025](https://doi.org/10.1093/femspd/ftad025)) |
| **Larval stages (pluteus)** | Attested as a distinct microbial habitat within the same host | Gammaproteobacteria/Alphaproteobacteria-dominated, horizontally acquired ([Brocco French et al. 2025, *Biol Bull*](https://german.bio.uci.edu/images/PDF/Brocco%20French%20et%20al.%20(2025)%20Biol%20Bull_online.pdf)) |

**Salinity is safely in the definition here, unlike the sponge case.** Echinoderms are exclusively marine — there are no freshwater or terrestrial echinoids ([Animal Diversity Web, Echinoidea](https://animaldiversity.org/accounts/Echinoidea/)). Writing "marine" into the definition excludes nothing attested. Depth is not restrictive: echinoids range from the intertidal to the abyss.

### The boundary: what is inside, what is next door

**Inside:** urchin gut tissue and lumen contents, coelomic fluid and coelomocytes, the epibiotic surface of spines/test/tube feet, gonads, larvae; regular echinoids (kelp/algal grazers) **and** irregular echinoids (deposit-feeding heart urchins and sand dollars); wild and aquaculture-held animals; healthy and diseased animals.

**Neighbouring concepts, outside it:**

| Neighbour | Why it is outside |
|---|---|
| **Sea urchin barren** | A benthic seafloor state — the alternative stable state of a collapsed kelp ecosystem, characterised by absence of canopy macrophytes and high encrusting-coralline cover ([Filbee-Dexter & Scheibling 2014, *MEPS* 495:1–25](https://doi.org/10.3354/meps10573)). A place *shaped by* urchins, not a place *that is* an urchin. **ENVO has no term for this either** — a separate, real gap. |
| Ambient **seawater** and **sediment** | The routine reference environments, sampled precisely because they are different habitats — and empirically different (§3b). |
| **Sea cucumber** `habitatmech:GOLD.67b0fd9ee7`, **Sea Star** | Sibling GOLD nodes; different echinoderm classes. |
| **Echinodermata** `habitatmech:GOLD.e1f435d44b` | The parent record. Broader, and genuinely so — it has three attested children. |
| **Egested fecal pellets in the sediment** | Once voided into the environment these become marine detritus/sediment; the concept covers pellets *sampled from the intestine*, which is what [Bengtsson et al. 2025](https://doi.org/10.1093/femsec/fiaf006) explicitly did to avoid seawater contamination. |
| `FOODON:03412107` **sea urchin** (the current xref) and **uni / roe** | The food-commodity reading of the string. §5. |
| **Sea urchin embryo as a developmental model system** | A laboratory research subject, not a sampled habitat. |

### Ambiguity in the label

The bare string "sea urchin" has three live readings: (i) the living echinoid as a host organism; (ii) the seafood commodity — gonads sold as *uni*, which is FOODON's reading; (iii) elliptically, "urchin barren", a seabed habitat. **The GOLD path `Host-associated > Invertebrates > Echinodermata > Sea Urchin` settles it unambiguously on (i).**

A fourth, narrower ambiguity is worth an explicit editorial decision: **does "sea urchin" include irregular echinoids?** Vernacular English usually means regular echinoids by "sea urchin" and calls the others "sand dollars" and "heart urchins" — but the microbiome literature does not observe that line. [Schwob et al. 2020](https://doi.org/10.3389/fmicb.2020.00308) title their subject "the Antarctic heart urchin *Abatus agassizii*" and describe it as "an irregular sea urchin". **Recommendation: scope the term to class Echinoidea and say so in the definition text, rather than writing "regular"** — narrowing it to regular echinoids would exclude the deposit-feeder work, which is a distinct and well-characterised part of the attested space.

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001002` *animal-associated environment*** — "An environmental system determined by an animal" (definition verified at [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002); synonyms *Metazoan-associated environment*, *animal environment*). **It is in this repo's vendored slice** with exactly that label (`data/raw/ontology_terms.tsv`), so a `GROUND_AS_PARENT` decision naming it will pass the slice-and-label check.

The modelling precedent is `ENVO:01001179` *cnidarian-associated environment* — "An environmental system determined by a cnidarian or part of a cnidarian" — also in the vendored slice. ENVO already accepts a host clade as an environment class and places it under *animal-associated environment*. **An echinoid-associated environment would be its sibling.**

A second precedent strengthens the case specifically for echinoderms: `ENVO:01001187` *holothurian digestive tract*, "A digestive tract environment which has its properties and dynamics determined by the digestive tract of an echinoderm from the class Holothuroidea", with synonyms *sea cucumber digestive tract* / *sea cucumber gut* ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001187)). ENVO has already minted an echinoderm-class-scoped environment class — for this record's own sibling.

### Near-misses, and why each fails

| Term | Verified content | Verdict |
|---|---|---|
| `ENVO:01001187` **holothurian digestive tract** | "…determined by the digestive tract of an echinoderm from the class Holothuroidea." | **Wrong class and narrower.** Holothuroidea, not Echinoidea; and it is scoped to *one organ*, whereas the 53 GOLD assertions are whole-host and span gut, coelomic fluid and surface. Worth recording as the single most useful precedent. It also suggests a second, narrower ENVO request — *echinoid digestive tract* — but that would not cover this node. |
| `ENVO:01001176` **environment associated with an aquatic invertebrate** | "An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system." | **True of urchins but broader, and structurally awkward.** It has a second parent, `ENVO:01001055` *environment associated with an animal part or small animal* ("An environmental system determined by part of a living or dead animal, or a whole small animal"), which imports a "part or small animal" implication that a 30 cm-diameter *Diadema* does not satisfy. ENVO did not route *cnidarian-associated environment* through it. **Recommend against as genus**; record as near-miss. |
| `ENVO:01001055` **environment associated with an animal part or small animal** | As above. | Same "part or small animal" over-claim; also the whole host, not a part, is what is denoted. |
| `FOODON:03412107` **sea urchin** *(current xref)* | I checked OLS4: **no textual definition, no synonyms, no xrefs** on the term. | **An organism/food-source term, not a place** — exactly what the #109 organism-identity screen exists to catch. Keeping it as `relation: xref` per #99 is correct. The curator note on the record says it was "attached as a parent"; the record itself now correctly carries it under `xrefs`. Note the discrepancy so it isn't re-litigated. |
| `FOODON:03412115` **echinoderm** / `FOODON:00005703` **echinoderm material** | Food-source and food-material classes (both in the vendored slice). | `echinoderm material` denotes *matter derived from* the animal — the meat/roe — which is the food reading, not the habitat. Also phylum-level, so broader. |
| `NCBITaxon:7586` **Echinodermata** *(in slice)* | Taxon. | A class of organisms, not a place. Per repo policy (#99, #114): `relation: xref` only, never grounding, never `parent_habitats`. `NCBITaxon:7626` Echinoidea would be the precise taxon but **is not in the vendored slice**. |
| **UBERON** | No echinoid-specific classes; `UBERON:0001555` *digestive tract* is the generic organ. | A *part*, not the host. Under the repo's host rule it would ground a hypothetical "Sea Urchin > Gut" child record, not this one. |
| **BTO** *(all in slice)* | `BTO:0001923` Aristotles lantern, `BTO:0001919` tube foot, `BTO:0002125` water vascular system, `BTO:0001708` coelomic fluid, `BTO:0002856` coelomocyte, `BTO:0006259` pluteus. | All echinoderm parts or cell types — useful if GOLD ever adds compartment children; **none names this concept**. |
| **ENVO, whole-ontology search for "urchin"** | Zero hits (OLS4 search, ENVO only). | **No existing ENVO term names this concept.** |

**Conclusion: `CONFIRM_UNGROUNDED` is correct.** Recommend adding `ENVO:01001002` *animal-associated environment* as an explicit `GROUND_AS_PARENT`, since the record currently carries no ontology parent at all (only the `Echinodermata` HabitatMech record), and the term request is well founded.

---

## 3. Differentia — what distinguishes it from its siblings

Ordered by how observable and how load-bearing each is. Any one or two of the first three carries the definition sentence; the rest belong in the term-request comment.

**(a) The host is an echinoid — a mobile, benthic, exclusively marine grazer with a complete through-gut.** Echinoids have a rigid calcite test of interlocking plates, movable spines on ball-and-socket joints, pedicellariae, a hydraulic water-vascular system of tube feet, and — in regular forms — a five-jawed masticatory apparatus, Aristotle's lantern ([ADW, Echinoidea](https://animaldiversity.org/accounts/Echinoidea/)). This is the decisive contrast with the two ENVO siblings already modelled or requested: a **sponge** is a sessile filter pump with no gut at all, and a **cnidarian** has a blind gastrovascular cavity. The urchin has a mouth and an anus, so it has a true, directional gut-lumen habitat that neither of those provides.

**(b) The gut is compartmentalised and selective — it is not a bag of seawater.** This is the single best-supported differentia, and it is what makes the concept a habitat rather than a sampling artefact:
- Gut tissue, gut digesta and pharynx carry three different communities in the same animal, and the pharynx is the one that "more closely resembl[es] the water microbiota" ([Hakim et al. 2019](https://doi.org/10.3390/microorganisms7020035)).
- In *L. variegatus*, gut tissue was 93% Campylobacteraceae while the seagrass diet was Cyanobacteria-dominated and surrounding seawater was Alpha-/Betaproteobacteria — the authors describe "a selective attribute for Campylobacteraceae in the gut tissue" ([Hakim et al. 2016](https://doi.org/10.1093/femsec/fiw146)).
- In a **deposit-feeding** heart urchin that eats the sediment it lives in — the hardest possible test of the claim — gut communities "did not cluster with communities from the surrounding environment", and the authors conclude "the conditions within the *Abatus* host impose successional ecological filters sieving the bacterial diversity of the surrounding sediments" ([Schwob et al. 2020, *Front Microbiol* 11:308](https://doi.org/10.3389/fmicb.2020.00308)). Gut tissue was 39–45% *Spirochaeta*; the sediment was Bacteroidia/Gammaproteobacteria.

**(c) Diet-driven, and the diet is nitrogen-poor — the gut hosts diazotrophic symbionts.** Kelp and macroalgae have a high C:N ratio, and N₂ fixation in the echinoid gut has been reported since 1981 across tropical (*Diadema antillarum*, *Echinometra lucunter*, *Tripneustes ventricosus*), temperate (*Strongylocentrotus droebachiensis*) and arctic urchins, with a peak of 11.6 µg N g wet wt⁻¹ d⁻¹ and mean monthly nitrogenase activity *inversely correlated* with the nitrogen content of the food ([Guerinot & Patriquin 1981, *Mar Biol* 62:197–207](https://doi.org/10.1007/BF00388183)). *nifH* sequencing 44 years later recovered diverse fixers related to *Vibrio*, Verrucomicrobia and Bacteroidota, concentrated in the kelp-fed (*Saccharina latissima*) treatment ([Bengtsson et al. 2025](https://doi.org/10.1093/femsec/fiaf006)). Intestinal community composition also tracks the seaweed diet directly, and differs between kelp-bed and barren-ground animals of the same species.

**(d) The gut tissue supports sulfur-based chemolithoautotrophy.** *Arcobacter* and *Sulfurimonas* — marine sulfur-oxidising Campylobacterota — as ~32% of the gut-tissue community, with energy metabolisms (oxidative phosphorylation, carbon fixation, nitrogen, methane, sulfur) predicted to be elevated in gut tissue versus carbohydrate/amino-acid/lipid metabolism in the digesta ([Hakim et al. 2019](https://doi.org/10.3390/microorganisms7020035)). A sulfur-oxidiser-dominated epithelium is unusual among animal guts and is a genuinely diagnostic property.

**(e) An internal liquid compartment — coelomic fluid — that is populated and antimicrobial.** Once assumed sterile, it carries a dynamic microbiota implicated in immunity, with reduced functional diversity and enrichment for animal-symbiont and putative-pathogen traits (Vibrionaceae) relative to the gut, in a fluid that contains abundant antimicrobial compounds ([Faddetta et al. 2020](https://doi.org/10.1038/s41598-020-78534-5); [Arranz et al. 2025](https://doi.org/10.3389/fmars.2025.1615711)). Community structure there also varies with geographic location.

**(f) An epibiotic surface the host actively keeps clean.** Unlike most benthic invertebrates, urchins resist encrustation; the spine microbiota is nonetheless species-specific and trophic-niche-dependent (*Endozoicomonas*-dominated in *Thalassia* seagrass beds versus *Kistimonas*/*Photobacterium* on reefs), and *L. variegatus* carries more species on its spines than in its own gut ([Rodríguez-Barreras et al. 2023](https://doi.org/10.3390/microorganisms11020391)).

---

## 4. Sources — and what is inference rather than sourced

### Primary literature

- Guerinot ML, Patriquin DG (1981). The association of N₂-fixing bacteria with sea urchins. *Marine Biology* 62:197–207. [doi:10.1007/BF00388183](https://doi.org/10.1007/BF00388183)
- Hakim JA, et al. (2016). The gut microbiome of the sea urchin *Lytechinus variegatus*… *FEMS Microbiol Ecol* 92(9):fiw146. [doi:10.1093/femsec/fiw146](https://doi.org/10.1093/femsec/fiw146) · [PMC5975844](https://pmc.ncbi.nlm.nih.gov/articles/PMC5975844/)
- Hakim JA, et al. (2019). The purple sea urchin *Strongylocentrotus purpuratus* demonstrates a compartmentalization of gut bacterial microbiota… *Microorganisms* 7(2):35. [doi:10.3390/microorganisms7020035](https://doi.org/10.3390/microorganisms7020035) · [PMC6406795](https://pmc.ncbi.nlm.nih.gov/articles/PMC6406795/)
- Schwob G, Cabrol L, Poulin E, Orlando J (2020, 28 Feb). Characterization of the gut microbiota of the Antarctic heart urchin (Spatangoida) *Abatus agassizii*. *Front Microbiol* 11:308. [doi:10.3389/fmicb.2020.00308](https://doi.org/10.3389/fmicb.2020.00308) · [PMC7058685](https://pmc.ncbi.nlm.nih.gov/articles/PMC7058685/)
- Faddetta T, et al. (2020, 8 Dec). Composition and geographic variation of the bacterial microbiota associated with the coelomic fluid of the sea urchin *Paracentrotus lividus*. *Sci Rep* 10:21443. [doi:10.1038/s41598-020-78534-5](https://doi.org/10.1038/s41598-020-78534-5) · [PMC7723044](https://pmc.ncbi.nlm.nih.gov/articles/PMC7723044/)
- Rodríguez-Barreras R, et al. (2023, 3 Feb). The epibiotic microbiota of wild Caribbean sea urchin spines is species specific. *Microorganisms* 11(2):391. [doi:10.3390/microorganisms11020391](https://doi.org/10.3390/microorganisms11020391) · [PMC9966300](https://pmc.ncbi.nlm.nih.gov/articles/PMC9966300/)
- Cavaliere V, et al. (2023). Bald sea urchin disease shifts the surface microbiome on purple sea urchins in an aquarium. *Pathogens and Disease* 81:ftad025. [doi:10.1093/femspd/ftad025](https://doi.org/10.1093/femspd/ftad025) · [PMC10550250](https://pmc.ncbi.nlm.nih.gov/articles/PMC10550250/)
- Bengtsson MM, et al. (2025, 14 Jan). Sea urchin intestinal bacterial communities depend on seaweed diet and contain nitrogen-fixing symbionts. *FEMS Microbiol Ecol* 101(2):fiaf006. [doi:10.1093/femsec/fiaf006](https://doi.org/10.1093/femsec/fiaf006) · [PMC11797059](https://pmc.ncbi.nlm.nih.gov/articles/PMC11797059/)
- Arranz V, et al. (2025, 16 Oct). Sea urchin holobionts: microbiome variation across species, compartments and locations in *Paracentrotus lividus* and *Arbacia lixula*. *Front Mar Sci* 12:1615711. [doi:10.3389/fmars.2025.1615711](https://doi.org/10.3389/fmars.2025.1615711)
- Zheng et al. (2024). The multifaceted role of gut microbiota in sea urchin digestion… *Aquaculture Research* 2024:7363987. [doi:10.1155/2024/7363987](https://doi.org/10.1155/2024/7363987) — **paywalled; I could not verify its text directly** (HTTP 402). Cited here only as a pointer to a recent review, not as support for any claim above.
- Hewson I, et al. (2023, 19 Apr). A scuticociliate causes mass mortality of *Diadema antillarum* in the Caribbean Sea. *Sci Adv* 9:eadg3200. [doi:10.1126/sciadv.adg3200](https://doi.org/10.1126/sciadv.adg3200) · [PMC10115408](https://pmc.ncbi.nlm.nih.gov/articles/PMC10115408/)
- Filbee-Dexter K, Scheibling RE (2014). Sea urchin barrens as alternative stable states of collapsed kelp ecosystems. *Mar Ecol Prog Ser* 495:1–25. [doi:10.3354/meps10573](https://doi.org/10.3354/meps10573)

### Ontology sources (all verified live against OLS4)

- `ENVO:01001002` animal-associated environment — [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002)
- `ENVO:01001179` cnidarian-associated environment — [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179)
- `ENVO:01001187` holothurian digestive tract — [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001187)
- `ENVO:01001176`, `ENVO:01001055` — [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo)
- `FOODON:03412107` sea urchin — [OLS4](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03412107) (no definition, no synonyms, no xrefs on the term)

### What is inference, not a sourced claim

- **"No ENVO term names this concept."** This is my conclusion from an OLS4 search of ENVO for "urchin" (zero hits) and for "-associated environment" (four hits: plant, animal, fungi, cnidarian). OLS search is not a formal proof of absence; a curator wanting certainty should grep an ENVO release file.
- **"The four `-associated environment` terms are the complete set."** Same caveat.
- **The 53/21/17/16 assertion counts and the "2 GOLD node ids share this path" note** come from this repo's `data/raw/`, not from GOLD documentation or literature.
- **"Each compartment is distinct from ambient seawater."** Directly demonstrated for the **gut** ([Hakim 2016](https://doi.org/10.1093/femsec/fiw146), [Hakim 2019](https://doi.org/10.3390/microorganisms7020035)) and for the **gut versus sediment** ([Schwob 2020](https://doi.org/10.3389/fmicb.2020.00308)). **Not demonstrated for coelomic fluid** — [Arranz et al. 2025](https://doi.org/10.3389/fmars.2025.1615711) state explicitly: "because seawater was not sampled, we cannot directly evaluate environmental acquisition of these taxa." Do not write a blanket "distinct from surrounding seawater" over all compartments into the definition.
- **The contrast drawn between echinoid, sponge and cnidarian gut architecture** in §3(a) is my synthesis; the individual anatomical facts are sourced, the comparison is not from a single paper.
- **The recommendation to scope to Echinoidea rather than to regular echinoids** is an editorial judgement, argued from usage in [Schwob 2020](https://doi.org/10.3389/fmicb.2020.00308).

---

## 5. Synonyms, and what not to conflate

### Names in real use for this concept

- **sea urchin** (GOLD's label), **urchin**, **echinoid**, **Echinoidea**
- **sea-urchin-associated environment**, **echinoid-associated environment** (the ENVO-pattern names)
- **sea urchin holobiont** — the framing used by [Arranz et al. 2025](https://doi.org/10.3389/fmars.2025.1615711)
- Compartment-qualified names in constant use: *sea urchin gut / intestine microbiome*, *sea urchin coelomic fluid*, *sea urchin spine epibiota*, *fecal pellets*
- Species names that stand in for the concept in practice: *Strongylocentrotus purpuratus*, *S. droebachiensis*, *S. intermedius*, *Mesocentrotus nudus*, *Paracentrotus lividus*, *Arbacia lixula*, *Lytechinus variegatus*, *Diadema antillarum*, *Tripneustes ventricosus*, *Echinometra lucunter*, *Abatus agassizii*, *Sterechinus neumayeri*

### Commonly but wrongly treated as the same thing

| Not this | Why not |
|---|---|
| **Sea urchin barren** | A seabed environmental state produced by urchin grazing — a different entity class entirely (a marine benthic zone, not a host body). [Filbee-Dexter & Scheibling 2014](https://doi.org/10.3354/meps10573). Genuinely unnamed in ENVO too, and worth a separate record/request. |
| **Uni / sea urchin roe / gonad as food** | `FOODON:03412107`'s reading. The commodity is ~55,000 t live weight globally in 2022 (down from ~110,000 t in 1995, FAO capture data); the food is a material derived from the animal, not the place a microbe lives. Keep as `xref`. |
| **`FOODON:00005703` echinoderm material** | Food material derived from echinoderms. Same category error. |
| **`NCBITaxon:7586` Echinodermata / `NCBITaxon:7626` Echinoidea** | Taxa — classes of organisms, not places. Per #99/#114 these are `xref`, and per repo policy `NOT_APPLICABLE` would be the *wrong* disposition here. |
| **Sea cucumber, sea star** | Sibling GOLD nodes, different echinoderm classes with their own records. Note `ENVO:01001187` covers only the sea cucumber gut. |
| **Diseased urchins — BSUD, DaSc** | Disease *states* of the same habitat, not different habitats. *Vibrio splendidus*-clade bacteria (incl. *V. crassostreae*) are recovered from bald-sea-urchin-disease lesions in *P. lividus* but the evidence supports opportunistic, not primary, etiology; injury appears to be a prerequisite in *S. droebachiensis*. The 2022 Caribbean *Diadema* mass mortality (>95% at affected sites) is caused by a **ciliate**, *Philaster apodigitiformis* — a eukaryotic parasite, not a bacterial habitat shift ([Hewson et al. 2023](https://doi.org/10.1126/sciadv.adg3200)). Per repo practice, a lesion is its own concept; disease is a quality, not a new habitat. |
| **Sea urchin embryo/larva as a model system** | The pluteus *is* an attested microbial habitat ([Brocco French et al. 2025](https://german.bio.uci.edu/images/PDF/Brocco%20French%20et%20al.%20(2025)%20Biol%20Bull_online.pdf)) and, per #112, a life stage is a whole organism and therefore a host — but "sea urchin embryo" as a laboratory research subject is not a habitat concept. Keep the distinction. |
| **Fossil/archaeological urchin tests** | Dead calcite skeletons in sediment; a geological material, not a host-associated environment. |
| **`ENVO:01000059` sea grass bed** | Mentions urchins in its definition text as grazers. Pure text collision — an automated-grounding hazard, since it is the only ENVO term whose text contains "sea urchin". |

---

## 6. Should it be a term at all?

**Yes — and it should be its own term, not merged into the parent.**

The `NOT_APPLICABLE` disposition is explicitly the wrong one here, and the repo has already paid for that mistake once. Per CLAUDE.md and #114: an organism acting as a host **is** a habitat; what is not a habitat is the *taxon term*. A sea urchin is where the microbe lives; ENVO models exactly this at plant-, animal-, fungi- and cnidarian-associated environment; and `tests/test_decisions.py` fails on a `NOT_APPLICABLE` whose target is an organism term. `NOT_APPLICABLE` is reserved for diseases, qualities, processes and procedures — none of which this is.

Nor is it a sampling artefact. The strongest evidence against that reading is the deposit-feeder result: an urchin that eats the sediment it lives in still carries a gut community that "did not cluster with communities from the surrounding environment" ([Schwob et al. 2020](https://doi.org/10.3389/fmicb.2020.00308)). If the concept were a mere container for ambient microbes, that is the case where it would show.

**And unlike Sponge/Porifera, this is not a `SAME_AS`.** The parent `Echinodermata` node (21 organisms) has three vernacular children — Sea Urchin (53), Sea cucumber (17), Sea Star (16) — that partition it by class. Sea Urchin is the largest of the three and a proper subset. Merging it upward would lose the class distinction that the sibling records depend on.

### Recommended disposition

- **Decision:** `CONFIRM_UNGROUNDED`, keyed on `habitatmech:GOLD.b19422ad27` (already recorded).
- **Add** `GROUND_AS_PARENT` → `ENVO:01001002` *animal-associated environment*. The record currently carries no ontology parent at all, only the `Echinodermata` HabitatMech record. The term and its exact label are in the vendored slice, so this will pass the seed check.
- **Keep** `FOODON:03412107` as `relation: xref` (#99). Optionally add `NCBITaxon:7586` Echinodermata as a second xref; `NCBITaxon:7626` Echinoidea would be more precise but is not in the slice.
- **Term-request candidate** for ENVO: *echinoid-associated environment* (alt. *sea urchin-associated environment*), a direct sibling of `ENVO:01001179` under `ENVO:01001002`, with `ENVO:01001187` *holothurian digestive tract* cited as the echinoderm precedent. Same family as the standing sponge, nematode and reptile requests, and the request essentially writes itself against the cnidarian template.
- **Do not file anything externally without explicit per-request approval** — the standing rule on ENVO/FoodOn submissions is one explicit yes per individual request, never per batch.
- **Two adjacent gaps this research surfaced**, worth filing as issues rather than folding into this record: (i) ENVO has no *sea urchin barren* term and the corpus has no record for it; (ii) the sibling record `sea_cucumber.yaml` is UNGROUNDED with no ontology parent even though `ENVO:01001187` *holothurian digestive tract* exists — it is narrower than that record's concept, so the answer there is probably the same `ENVO:01001002` parent plus its own term request, but it should be looked at deliberately.

## Citations

1. https://doi.org/10.3390/microorganisms7020035
2. https://doi.org/10.1093/femsec/fiw146
3. https://doi.org/10.1093/femsec/fiaf006
4. https://doi.org/10.1038/s41598-020-78534-5
5. https://doi.org/10.3389/fmars.2025.1615711
6. https://doi.org/10.3390/microorganisms11020391
7. https://doi.org/10.1093/femspd/ftad025
8. https://german.bio.uci.edu/images/PDF/Brocco%20French%20et%20al.%20(2025
9. https://animaldiversity.org/accounts/Echinoidea/
10. https://doi.org/10.3354/meps10573
11. https://doi.org/10.3389/fmicb.2020.00308
12. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
13. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001187
14. https://doi.org/10.1007/BF00388183
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC5975844/
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC6406795/
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC7058685/
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC7723044/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC9966300/
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC10550250/
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC11797059/
22. https://doi.org/10.1155/2024/7363987
23. https://doi.org/10.1126/sciadv.adg3200
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC10115408/
25. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179
26. https://www.ebi.ac.uk/ols4/ontologies/envo
27. https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03412107