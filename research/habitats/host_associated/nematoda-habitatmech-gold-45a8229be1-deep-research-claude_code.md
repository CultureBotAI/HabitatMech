---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:59:56.064230'
end_time: '2026-08-17T17:08:45.380620'
duration_seconds: 529.32
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Nematoda
  habitat_identifier: habitatmech:GOLD.45a8229be1
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Invertebrates > Nematoda'
  assertions: '300'
  parent_terms: ENVO:01001002
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Nearest
    broader term ENVO:01001002 ''animal-associated environment'' attached as a parent.
    Nematodes as host. Parented to animal-associated environment. ENVO term request.
    (source concept habitatmech:GOLD.45a8229be1)'
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
  web_search_requests: 17
  num_turns: 32
  total_cost_usd: 3.544168999999999
  session_id: af5b546b-dbf3-4ef4-ab10-93da22b418e3
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 28
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Nematoda
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.45a8229be1
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Invertebrates > Nematoda
- **Upstream assertion volume:** 300
- **Nearest broader term already on the record:** ENVO:01001002
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:01001002 'animal-associated environment' attached as a parent. Nematodes as host. Parented to animal-associated environment. ENVO term request. (source concept habitatmech:GOLD.45a8229be1)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Nematoda** as a microbial habitat, with citations.

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

# Nematoda as a microbial habitat — definition research

**Target:** `habitatmech:GOLD.45a8229be1` · label *Nematoda* · category HOST_ASSOCIATED · UNGROUNDED
**Source path:** GOLD `Host-associated > Invertebrates > Nematoda` (300 assertions)

---

## Proposed definition

> An animal-associated environment whose determining animal is a roundworm of the phylum Nematoda, comprising the cuticle surface, intestinal lumen, pseudocoelom and tissues of the worm as the site colonised by its associated microorganisms.

Genus: `ENVO:01001002` *animal-associated environment* ("An environmental system determined by an animal"). Differentia: the determining animal is a nematode, and the habitat is the worm's body — surface and interior — rather than the substrate it was extracted from or the host it parasitises.

**One structural caveat worth recording:** ENVO has no intermediate class between *animal-associated environment* and a specific phylum, except `ENVO:01001176` *environment associated with an aquatic invertebrate*, which is restricted to aquatic taxa and so cannot hold soil, plant-parasitic or vertebrate-parasitic nematodes. The genus therefore has to be the very general `ENVO:01001002`. If HabitatMech wants a tighter parent, the missing class is an *invertebrate-associated environment* not restricted to aquatic settings — that is a second, separate ENVO gap, and saying so is more useful than padding this definition.

---

## 1. What the concept denotes

### The reading the data supports

The GOLD path places *Nematoda* at the Ecosystem Type level under `Host-associated > Invertebrates`. In GOLD's five-level scheme (Ecosystem → Ecosystem Category → Ecosystem Type → Ecosystem Subtype → Specific Ecosystem), the levels below "Host-associated" name **the host organism and then the host body site** — the canonical worked example in the GOLD papers is `Host-associated → mammals → digestive system → foregut → rumen` ([Mukherjee et al. 2023, *NAR* 51:D957–D963, doi:10.1093/nar/gkac974](https://academic.oup.com/nar/article/51/D1/D957/6786204); [Reddy et al. 2015, *NAR* 43:D1099](https://academic.oup.com/nar/article/43/D1/D1099/2439522)). So *Nematoda* here occupies the same slot as *mammals* does: **the host organism whose body is the sampled environment**, not a taxonomic annotation of the sequenced organism and not the soil the worm came from.

Concretely, a sample under this concept is one of:

- **whole worms**, washed or surface-sterilised, homogenised for 16S/metagenomics — the standard preparation in wild-*Caenorhabditis* microbiome work ([Dirksen et al. 2016, *BMC Biology* 14:38, doi:10.1186/s12915-016-0258-1](https://link.springer.com/article/10.1186/s12915-016-0258-1));
- **the worm intestine / gut contents**, dissected or recovered by grinding after removal of transient surface colonisers ([Portal-Celhay et al. 2012, *BMC Microbiology* 12:49, doi:10.1186/1471-2180-12-49](https://bmcmicrobiol.biomedcentral.com/articles/10.1186/1471-2180-12-49); [Formenti et al. 2022, *Microbiome* 10:222, doi:10.1186/s40168-022-01399-5](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-022-01399-5));
- **the worm cuticle surface**, sampled by micro-swab or wash ([Haghani et al. 2024, *Microbiology Spectrum* 12(8), doi:10.1128/spectrum.00169-24](https://journals.asm.org/doi/10.1128/spectrum.00169-24); [McQueen et al. 2023, *Journal of Nematology* 55:20230004, doi:10.2478/jofnem-2023-0004](https://pmc.ncbi.nlm.nih.gov/articles/PMC10035304/));
- **specialised symbiont-bearing compartments**: the anterior-gut *receptacle* of *Steinernema* infective juveniles carrying *Xenorhabdus*, or the reproductive and hypodermal tissues of filarial nematodes carrying *Wolbachia* ([Machado et al. 2024, *Zoological Letters* 10:14, doi:10.1186/s40851-024-00235-y](https://zoologicalletters.biomedcentral.com/articles/10.1186/s40851-024-00235-y); [Lefoulon et al. 2021, *Parasites & Vectors*, doi:10.1186/s13071-021-04742-1](https://link.springer.com/article/10.1186/s13071-021-04742-1)).

### The boundary

**Inside the concept:** any nematode body — free-living bacterivore, marine meiofaunal, entomopathogenic, plant-parasitic, or animal-parasitic — and any of its compartments (cuticle, gut lumen, tissues, gonad, egg/cyst).

**Neighbouring concepts, explicitly outside:**

| Neighbour | Why it is not this concept |
|---|---|
| Soil / sediment / rotting plant matter the worm was extracted from | This is the *substrate*, a distinct environment. Empirically distinct too: wild *C. elegans* communities differ significantly from the substrate they were isolated from ([Dirksen et al. 2016](https://link.springer.com/article/10.1186/s12915-016-0258-1)), and Antarctic nematode internal and external communities are distinct from the surrounding microbial mats ([McQueen et al. 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10035304/)). |
| The vertebrate or insect gut in which a parasitic nematode lives | "Guts within guts": the *Ascaris suum* intestinal microbiome is derived from, but significantly distinct from, the pig jejunal microbiome, and is less diverse ([Formenti et al. 2022](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-022-01399-5)); the same holds for *A. lumbricoides* vs. its human host ([Sahimin et al. 2024, *Curr. Res. Parasitol. Vector Borne Dis.*](https://pmc.ncbi.nlm.nih.gov/articles/PMC10844936/)). The mammalian gut belongs under `Host-associated > Mammals > Digestive system`. |
| Root knots and galls induced by plant-parasitic nematodes | Plant tissue, hence plant-associated (`ENVO:01001001` and descendants), even though a nematode caused it. |
| The taxon *Nematoda* (`NCBITaxon:6231`) | A class of organisms, not a place. See §6. |
| Nematode-trapping fungi, nematophagous interactions, biocontrol formulations | Processes, interactions, or products. |

**Ambiguity assessment:** the label "Nematoda" is ambiguous in isolation between (a) the worm body as habitat, (b) nematode-containing substrate, and (c) the taxon as a classification of an organism. The GOLD path resolves it to (a) — that is what "Host-associated >" asserts. This is my reading of the path semantics, supported by the GOLD documentation cited above, not a statement any source makes about this specific path.

**Heterogeneity warning for the curator:** 300 assertions under one label will pool at least four ecologically incomparable systems — laboratory and wild *Caenorhabditis*, entomopathogenic *Steinernema*/*Heterorhabditis*, plant-parasitic cyst and dagger nematodes, and vertebrate-parasitic filariae and ascarids. The definition must be broad enough to cover all four; it should not smuggle in any of *soil-dwelling*, *bacterivorous*, or *parasitic*. Sub-concepts (nematode gut environment, nematode cuticle environment) are the natural children if the corpus ever needs them.

---

## 2. Genus — the broader kind

**Recommended genus:** `ENVO:01001002` *animal-associated environment* — "An environmental system determined by an animal." This is already the parent on the record and it is correct.

I queried the current ENVO release via OLS4 for every class whose label contains "-associated environment". There are exactly eight, and none names nematodes:

| CURIE | Label | Verdict |
|---|---|---|
| `ENVO:01001002` | animal-associated environment | **Genus.** Correct but very general — the concept is far narrower. |
| `ENVO:01001176` | environment associated with an aquatic invertebrate | **Near miss.** Definition: "An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system." Asserts an *aquatic* habitat that the GOLD concept does not — most nematode microbiome sampling is soil, plant, insect or vertebrate-parasitic. Grounding here would misclassify the majority of the 300 assertions. It has no child classes. |
| `ENVO:01001055` | environment associated with an animal part or small animal | **Near miss, and the most tempting one.** Definition: "An environmental system determined by part of a living or dead animal, or a whole small animal." A nematode *is* a small animal, so the concept is a subclass of this. But it is not a match — it is far broader (any animal part, any small animal, live or dead), and its placement is odd: OLS4 reports its direct parents as `BFO:0000040` *material entity* and `ENVO:01001110` *ecosystem*, not `ENVO:01001002`. Using it as genus would put the term outside the animal-associated branch the rest of the corpus's host concepts sit in. |
| `ENVO:01001179` | cnidarian-associated environment | Sibling, not parent — this is the pattern the requested term should follow. |
| `ENVO:01001001`, `ENVO:01001041`, `ENVO:01001057`, `ENVO:01001058` | plant-, fungi-, plant-part-, fungal-tissue-associated | Wrong kingdom. |

A search of ENVO for "nematode" returns nothing relevant (only `ENVO:01000059` *sea grass bed*, a text match on associated fauna). A GitHub API search of `EnvironmentOntology/envo` for issues mentioning "nematode" returns zero results — no one has requested this term, so there is no in-flight request to wait on.

**Conclusion: nothing in ENVO expresses the concept.** UBERON, PO and BTO are not candidates: UBERON holds nematode *anatomy* (intestine, cuticle), which is a body part, not the whole-organism-as-habitat concept the GOLD path denotes; PO is plants; BTO is tissue/cell-line. The nematode-specific anatomy ontology WBbt likewise names parts, not habitats. This matches the repo's standing rule — a host's *parts* ground to the anatomy term, the *whole host organism* keeps its own minted identity.

---

## 3. Differentia — what distinguishes it from its siblings

Under *animal-associated environment*, the siblings are other host phyla (Cnidaria, Mollusca, Arthropoda, Porifera, Annelida, and vertebrate classes). Observable properties that separate the nematode case:

**Body plan and physical scale.** The habitat is a microscopic to macroscopic unsegmented pseudocoelomate tube. Free-living forms such as *C. elegans* are ~1 mm long as adults; parasitic *Ascaris* reach tens of centimetres. The determining animal's whole body, not an organ within a large animal, constitutes the environment.

**A collagenous cuticle that is itself a distinct microbial habitat.** Unlike the chitinous exoskeleton of arthropod hosts or the mucus-coated epithelium of vertebrates, the nematode cuticle is a moulted collagen sheath, and recent work establishes it as a habitat compartment separate from the gut:
- Antarctic *Plectus murrayi* and *Eudorylaimus antarcticus* carry external bacterial communities that are **more diverse than their internal communities but less diverse than the surrounding mats**, are compositionally distinct from the internal communities, yet more similar to them than to the environment; host identity is the main driver of both, with stream location influencing external communities more ([McQueen et al. 2023, doi:10.2478/jofnem-2023-0004](https://pmc.ncbi.nlm.nih.gov/articles/PMC10035304/)).
- In *C. elegans*, micro-swabbing of a modified CeMbio consortium showed *Enterobacter* sp. JUb101 localises primarily to the cuticle, while *Stenotrophomonas indicatrix* JUb19 and *Ochrobactrum vermis* MYb71 are predominantly in the gut; the cuticle community promotes cuticle integrity under environmental stress ([Haghani et al. 2024, doi:10.1128/spectrum.00169-24](https://journals.asm.org/doi/10.1128/spectrum.00169-24)).
- The most extreme case: Stilbonematinae (*Laxus*, *Stilbonema*, *Robbea*, *Leptonemella*, *Paralaxus*) are marine nematodes **entirely ensheathed in a monospecific coat of chemoautotrophic sulfur-oxidising Gammaproteobacteria, "*Candidatus* Thiosymbion"**, which the worm farms as its principal diet while migrating between oxic and sulfidic sand layers ([Paredes et al. 2021, *mSystems* 6:e01186-20, doi:10.1128/mSystems.01186-20](https://journals.asm.org/doi/10.1128/msystems.01186-20); [Zimmermann et al. on *Paralaxus*, bioRxiv 728105](https://www.biorxiv.org/content/10.1101/728105v1.full)). This is a cuticle habitat with a defined redox regime (H₂S/thiosulfate as electron donor, O₂ as acceptor) and no close analogue among the sibling phyla.

**A through-gut with a mechanical filter at the entrance.** The *C. elegans* intestine is a tube of exactly **20 non-renewable cells** with microvilli and apical junctions; the pharyngeal grinder crushes ingested bacteria before they enter, so colonisation requires either surviving mechanical lysis or a grinder-defective host ([Portal-Celhay et al. 2012](https://bmcmicrobiol.biomedcentral.com/articles/10.1186/1471-2180-12-49); review: [Zhang et al. 2024, PMC11104810](https://pmc.ncbi.nlm.nih.gov/articles/PMC11104810/)). This bottleneck is a defining physicochemical property of the habitat and has no vertebrate-gut counterpart.

**Small, measurable standing microbial load.** Viable counts in *phm-2* grinder mutants rise from ~10² CFU/worm at L4 to ~10⁴ CFU/worm by day 4, roughly tenfold above wild-type N2, then plateau; across eleven monocolonising species, loads range from ~200 cells/worm (*Bacillus cereus*) to tens of thousands (*Serratia marcescens*) ([Portal-Celhay et al. 2012](https://bmcmicrobiol.biomedcentral.com/articles/10.1186/1471-2180-12-49)). *Flagged as unverified:* secondary summaries also report an acidic anterior-to-posterior gut pH gradient (≈5.96 in the anterior pharynx to ≈3.59 in the posterior intestine) from pH-nanosensor work; I did not reach the primary paper, so do not cite this figure without checking it.

**Host filtering against a substrate-derived pool.** Wild-caught *C. elegans*, *C. briggsae* and *C. remanei* carry species-rich communities dominated by Proteobacteria — Enterobacteriaceae plus *Pseudomonas*, *Stenotrophomonas*, *Ochrobactrum*, *Sphingomonas* — that are distinct from both the substrate and from congeneric species; worm communities from different geographic sites resemble each other more than they resemble their own local environments ([Dirksen et al. 2016](https://link.springer.com/article/10.1186/s12915-016-0258-1); commentary [Clark & Hodgkin 2016, *BMC Biol* 14:37, doi:10.1186/s12915-016-0260-7](https://link.springer.com/article/10.1186/s12915-016-0260-7); companion studies [Berg et al. 2016, *ISME J* 10:1998](https://pubmed.ncbi.nlm.nih.gov/26800234/) and [Samuel et al. 2016, *PNAS* 113:E3941](https://www.pnas.org/doi/10.1073/pnas.1607183113)). The natural substrate for *Caenorhabditis* is rotting plant stems, fruits, flowers and mushrooms ([Schulenburg & Félix 2017, *Genetics* 206:55–86, doi:10.1534/genetics.116.195511](https://academic.oup.com/genetics/article/206/1/55/6067227)).

**Obligate and organ-localised symbioses that define whole nematode clades:**
- *Wolbachia pipientis* is an obligate, maternally transmitted intracellular mutualist of Onchocercidae (*Brugia malayi*, *Wuchereria bancrofti*, *Onchocerca volvulus*, *Dirofilaria immitis*), required for worm fertility and survival — which is why doxycycline is macrofilaricidal ([Lefoulon et al. 2021, doi:10.1186/s13071-021-04742-1](https://link.springer.com/article/10.1186/s13071-021-04742-1); [Hoerauf et al. 2000, *Lancet* 355:1242, doi:10.1016/S0140-6736(00)02095-X](https://www.sciencedirect.com/science/article/abs/pii/S0140673600045815)).
- Entomopathogenic *Steinernema* infective juveniles carry *Xenorhabdus* in a dedicated **receptacle in the anterior gut**; *Heterorhabditis* carries *Photorhabdus* in the intestine. Fewer than five CFU delivered into an insect suffice for the symbiont to kill it ([Machado et al. 2024, doi:10.1186/s40851-024-00235-y](https://zoologicalletters.biomedcentral.com/articles/10.1186/s40851-024-00235-y); [Kajol et al. 2024, PMC10926393](https://pmc.ncbi.nlm.nih.gov/articles/PMC10926393/); [Tailliez et al. 2019, *Symbiosis*, doi:10.1007/s13199-019-00660-0](https://link.springer.com/article/10.1007/s13199-019-00660-0)).
- Plant-parasitic nematodes host vertically transmitted intracellular symbionts: "*Ca.* Cardinium hertigii" in *Heterodera*, *Globodera* and *Pratylenchus*; "*Ca.* Xiphinematobacter" (Verrucomicrobiota) and "*Ca.* Xiphinematincola pachtaicus" in *Xiphinema*, implicated in inducing thelytokous parthenogenesis ([Brown 2018, *Annu. Rev. Phytopathol.*, doi:10.1146/annurev-phyto-080417-045824](https://www.annualreviews.org/content/journals/10.1146/annurev-phyto-080417-045824); [Showmaker et al. 2018, PMC6025951](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6025951/); [Palomares-Rius et al. 2021, *IJSEM*, doi:10.1099/ijsem.0.004888](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.004888)).

**Ubiquity and scale** (context for why this deserves a term, not part of the differentia): an estimated **4.4 ± 0.64 × 10²⁰ nematodes, ~0.3 Gt biomass, inhabit global topsoil**, making them the most abundant animals on Earth ([van den Hoogen et al. 2019, *Nature* 572:194–198, doi:10.1038/s41586-019-1418-6](https://www.nature.com/articles/s41586-019-1418-6)).

---

## 4. Sources — what is cited vs. inferred

Every factual claim above carries a DOI or resolvable URL inline. Three statements are **my inference, not any source's assertion**, and should not be written into the definition as fact:

1. **That the GOLD Ecosystem Type slot under `Host-associated` denotes the host body as the sampled environment.** Supported by GOLD's own worked example (`Host-associated → mammals → digestive system → foregut → rumen`) but not stated for the *Nematoda* path specifically.
2. **That the 300 assertions pool free-living, entomopathogenic, plant-parasitic and vertebrate-parasitic studies.** Inferred from the literature's composition; I did not inspect the underlying GOLD biosamples.
3. **That `ENVO:01001055` is a superclass of the concept.** Follows from its definition ("a whole small animal") but ENVO does not assert it.

The ENVO class inventory in §2 was obtained by direct query of the EBI OLS4 API against the current ENVO release (label search for "-associated environment", plus `hierarchicalChildren`/`hierarchicalParents` for `ENVO:01001002`, `ENVO:01001055`, `ENVO:01001176`), not from a paper. The direct children of `ENVO:01001002` are, in the current release, exactly: `ENVO:01001176`, `ENVO:01001179` and `ENVO:01001829` *human settlement*.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept:**
- nematode-associated environment / nematode-associated habitat
- roundworm-associated environment
- nematode host (in the microbiome literature: "the nematode as host")
- nematode holobiont / nematode metaorganism — related but *not* synonymous: these denote worm-plus-microbes as a unit, whereas the habitat term denotes the worm-as-place
- "worm microbiome" (informal, and in *C. elegans* circles often means specifically *Caenorhabditis*)
- *eelworm* — plant-pathology vernacular for plant-parasitic nematodes only

**Commonly but wrongly treated as the same thing:**

| Not this | Why |
|---|---|
| `NCBITaxon:6231` *Nematoda* | The taxon: a class of organisms, not a place. Belongs in `relation: xref`, per the repo's standing rule. |
| **Helminth-associated environment** | *Helminth* is polyphyletic — it lumps nematodes with cestodes and trematodes (Platyhelminthes). Broader, not equivalent. |
| **Nematomorpha** (horsehair worms), **Annelida**, **Nemertea** | Different phyla. Nematomorpha in particular is regularly confused with Nematoda in text. |
| **The parasitised host's gut** | A distinct habitat; "guts within guts" ([Formenti et al. 2022](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-022-01399-5)). |
| **Soil / rhizosphere / sediment containing nematodes** | The substrate, empirically distinct from the worm community. |
| **Nematode-induced root knots and galls** | Plant tissue, plant-associated. |
| **Monoxenic laboratory *C. elegans* on *E. coli* OP50** | An experimental artefact of the standard N2 husbandry — worms are propagated from a bleached, essentially axenic starting point on a single food strain, so lab worms are not an instance of the natural habitat ([Dirksen et al. 2016](https://link.springer.com/article/10.1186/s12915-016-0258-1)). This matters if GOLD samples include OP50-fed lab cultures. |
| **Entomopathogenic nematode biopesticide formulations** | A product/material. |
| **Nematophagy, nematode trapping** | Processes. |

---

## 6. Should this be a term at all? — Yes

This is a habitat and should get a term. The concept denotes a **place where microorganisms live** — a body with a lumen, a surface, tissues and a redox regime — not a taxonomic grouping, disease, quality or process. It is exactly the case the repo's rule covers: *an organism acting as a host IS a habitat; the taxon term is not*. ENVO itself models this pattern at *plant-associated environment*, *animal-associated environment*, *fungi-associated environment* and *cnidarian-associated environment*.

`NOT_APPLICABLE` would be the wrong disposition here, and would repeat the #114/#112 error: it asserts the concept is not a habitat, which is false for a phylum whose members are among the best-characterised host systems in microbiology (*C. elegans* as a model metaorganism; *Wolbachia*–filaria as an active drug target; *Xenorhabdus*/*Photorhabdus* as commercial biocontrol).

Recommended disposition, in the repo's vocabulary:

- **`CONFIRM_UNGROUNDED`** (the existing note is right) with `ENVO:01001002` *animal-associated environment* as `parent`, and `NCBITaxon:6231` *Nematoda* as `relation: xref` — never as a parent, since the taxon is not broader than a habitat.
- **ENVO term-request candidate:** `nematode-associated environment`, sibling of `ENVO:01001179` *cnidarian-associated environment*, using the proposed definition above. Per the standing rule recorded in memory, **do not submit this to ENVO without explicit per-request permission** — it is a candidate here, nothing more.
- Do **not** ground to `ENVO:01001176` *environment associated with an aquatic invertebrate*: it asserts an aquatic setting the sources do not support for most of the attestations. If a link is wanted, `relation: xref` is the honest one.

Two standards-level notes that support keeping the taxon and the habitat separate: MIxS records host identity in dedicated host fields (`host_taxid`, `host_common_name`) while `env_broad_scale` / `env_local_scale` / `env_medium` take ENVO classes, and ENVO's own MIxS guidance is to fill the NCBI TaxID for host-associated samples rather than encode the host taxon as the environment ([ENVO wiki, *Using ENVO with MIxS*](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS); [MIxS `env_broad_scale`, MIXS:0000012](https://genomicsstandardsconsortium.github.io/mixs/0000012/)). The GSC has since added a symbiont-associated extension, MIxS-SA, precisely because nested host→symbiont→microbe systems — of which nematodes are the archetype — could not be expressed in the host-associated package alone ([Jorge et al. 2022, *ISME Communications* 2:9, doi:10.1038/s43705-022-00092-w](https://pmc.ncbi.nlm.nih.gov/articles/PMC9723553/)).

---

## Sources

- [Dirksen et al. 2016, *BMC Biology* 14:38 — native microbiome of *C. elegans*](https://link.springer.com/article/10.1186/s12915-016-0258-1)
- [Clark & Hodgkin 2016, *BMC Biology* 14:37 — commentary](https://link.springer.com/article/10.1186/s12915-016-0260-7)
- [Schulenburg & Félix 2017, *Genetics* 206:55–86 — natural biotic environment of *C. elegans*](https://academic.oup.com/genetics/article/206/1/55/6067227)
- [Haghani et al. 2024, *Microbiology Spectrum* 12(8) — *C. elegans* skin/cuticle microbiome](https://journals.asm.org/doi/10.1128/spectrum.00169-24)
- [McQueen et al. 2023, *Journal of Nematology* 55:20230004 — external vs internal microbiomes of Antarctic nematodes](https://pmc.ncbi.nlm.nih.gov/articles/PMC10035304/)
- [Portal-Celhay et al. 2012, *BMC Microbiology* 12:49 — intestinal bacterial load in *C. elegans*](https://bmcmicrobiol.biomedcentral.com/articles/10.1186/1471-2180-12-49)
- [Zhang et al. 2024 — *C. elegans* as a model for host–microbe interactions (PMC11104810)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11104810/)
- [Formenti et al. 2022, *Microbiome* 10:222 — "guts within guts", *Ascaris suum*](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-022-01399-5)
- [Sahimin et al. 2024 — *Ascaris lumbricoides* gut microbiota distinct from human host (PMC10844936)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10844936/)
- [Machado et al. 2024, *Zoological Letters* 10:14 — Steinernema–Xenorhabdus / Heterorhabditis–Photorhabdus systematics](https://zoologicalletters.biomedcentral.com/articles/10.1186/s40851-024-00235-y)
- [Tailliez et al. 2019, *Symbiosis* — *Xenorhabdus*/*Photorhabdus* overview, receptacle](https://link.springer.com/article/10.1007/s13199-019-00660-0)
- [Kajol et al. — entomopathogenic nematodes and their symbiotic bacteria (PMC10926393)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10926393/)
- [Lefoulon et al. 2021, *Parasites & Vectors* — *Wolbachia* in onchocercid nematodes](https://link.springer.com/article/10.1186/s13071-021-04742-1)
- [Hoerauf et al. 2000, *Lancet* 355:1242 — doxycycline depletion of *Wolbachia* in *O. volvulus*](https://www.sciencedirect.com/science/article/abs/pii/S0140673600045815)
- [Brown 2018, *Annual Review of Phytopathology* — endosymbionts of plant-parasitic nematodes](https://www.annualreviews.org/content/journals/10.1146/annurev-phyto-080417-045824)
- [Showmaker et al. 2018 — *Ca.* Cardinium hertigii cHgTN10 genome from *Heterodera glycines*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6025951/)
- [Palomares-Rius et al. 2021, *IJSEM* — *Ca.* Xiphinematincola pachtaicus](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.004888)
- [Paredes et al. 2021, *mSystems* 6:e01186-20 — *Ca.* Thiosymbion oneisti anaerobic sulfur oxidation](https://journals.asm.org/doi/10.1128/msystems.01186-20)
- [Zimmermann et al., bioRxiv 728105 — *Paralaxus* gen. nov., stilbonematine ectosymbiont morphology](https://www.biorxiv.org/content/10.1101/728105v1.full)
- [van den Hoogen et al. 2019, *Nature* 572:194–198 — global soil nematode abundance](https://www.nature.com/articles/s41586-019-1418-6)
- [Mukherjee et al. 2023, *NAR* 51:D957 — GOLD v.9 and the five-level ecosystem classification](https://academic.oup.com/nar/article/51/D1/D957/6786204)
- [Reddy et al. 2015, *NAR* 43:D1099 — GOLD v.5, host-associated path example](https://academic.oup.com/nar/article/43/D1/D1099/2439522)
- [Jorge et al. 2022, *ISME Communications* 2:9 — MIxS-SA symbiont-associated extension](https://pmc.ncbi.nlm.nih.gov/articles/PMC9723553/)
- [MIxS `env_broad_scale` (MIXS:0000012)](https://genomicsstandardsconsortium.github.io/mixs/0000012/)
- [ENVO wiki — Using ENVO with MIxS](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS)
- [EBI OLS4 — ENVO class queries (ENVO:01001002, :01001055, :01001176, :01001179)](https://www.ebi.ac.uk/ols4/ontologies/envo)

## Citations

1. https://academic.oup.com/nar/article/51/D1/D957/6786204
2. https://academic.oup.com/nar/article/43/D1/D1099/2439522
3. https://link.springer.com/article/10.1186/s12915-016-0258-1
4. https://bmcmicrobiol.biomedcentral.com/articles/10.1186/1471-2180-12-49
5. https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-022-01399-5
6. https://journals.asm.org/doi/10.1128/spectrum.00169-24
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC10035304/
8. https://zoologicalletters.biomedcentral.com/articles/10.1186/s40851-024-00235-y
9. https://link.springer.com/article/10.1186/s13071-021-04742-1
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC10844936/
11. https://journals.asm.org/doi/10.1128/msystems.01186-20
12. https://www.biorxiv.org/content/10.1101/728105v1.full
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC11104810/
14. https://link.springer.com/article/10.1186/s12915-016-0260-7
15. https://pubmed.ncbi.nlm.nih.gov/26800234/
16. https://www.pnas.org/doi/10.1073/pnas.1607183113
17. https://academic.oup.com/genetics/article/206/1/55/6067227
18. https://www.sciencedirect.com/science/article/abs/pii/S0140673600045815
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC10926393/
20. https://link.springer.com/article/10.1007/s13199-019-00660-0
21. https://www.annualreviews.org/content/journals/10.1146/annurev-phyto-080417-045824
22. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6025951/
23. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.004888
24. https://www.nature.com/articles/s41586-019-1418-6
25. https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
26. https://genomicsstandardsconsortium.github.io/mixs/0000012/
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC9723553/
28. https://www.ebi.ac.uk/ols4/ontologies/envo