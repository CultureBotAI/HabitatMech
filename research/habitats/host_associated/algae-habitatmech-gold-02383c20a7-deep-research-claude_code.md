---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:50:24.280399'
end_time: '2026-08-17T16:57:05.493333'
duration_seconds: 401.21
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Algae
  habitat_identifier: habitatmech:GOLD.02383c20a7
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Algae'
  assertions: '394'
  parent_terms: ENVO:01001000
  xrefs: FOODON:03411301
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term FOODON:03411301 'algae' attached as a parent. Non-habitat screen\
    \ (#12): 'Host-associated > Algae' was grounded EXACT to FOODON:03411301 'algae',\
    \ which FOODON defines as 'an informal term for a large, diverse group of photosynthetic\
    \ eukaryotic ORGANISMS'. An organism is not a habitat, and because the seeder\
    \ derives a GOLD child's parent from its path node, that identity also became\
    \ the parent_habitats entry of 14 records under Host-associated > Algae \u2014\
    \ publishing 'is-a algae the organism group' as a broader-habitat claim 14 times\
    \ over. The existing organism-identity screen could not see it: it tests ancestry\
    \ against NCIT and mesh roots, and FOODON files both the organism and the material\
    \ under one 'organism material' root, so there is no structural signal to test.\
    \ The concept itself is real \u2014 algae as host \u2014 and is the same family\
    \ as the sponge, nematode and reptile requests, so it becomes a term request with\
    \ the FOODON term kept as an xref (#99) rather than an identity. (source concept\
    \ habitatmech:GOLD.02383c20a7)"
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
  web_search_requests: 10
  num_turns: 25
  total_cost_usd: 2.3972915
  session_id: ba4e6abd-e58d-4d5c-a1bd-e88ca96f0c72
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 38
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Algae
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.02383c20a7
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Algae
- **Upstream assertion volume:** 394
- **Nearest broader term already on the record:** ENVO:01001000
- **Cross-references upstream suggested:** FOODON:03411301

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term FOODON:03411301 'algae' attached as a parent. Non-habitat screen (#12): 'Host-associated > Algae' was grounded EXACT to FOODON:03411301 'algae', which FOODON defines as 'an informal term for a large, diverse group of photosynthetic eukaryotic ORGANISMS'. An organism is not a habitat, and because the seeder derives a GOLD child's parent from its path node, that identity also became the parent_habitats entry of 14 records under Host-associated > Algae — publishing 'is-a algae the organism group' as a broader-habitat claim 14 times over. The existing organism-identity screen could not see it: it tests ancestry against NCIT and mesh roots, and FOODON files both the organism and the material under one 'organism material' root, so there is no structural signal to test. The concept itself is real — algae as host — and is the same family as the sponge, nematode and reptile requests, so it becomes a term request with the FOODON term kept as an xref (#99) rather than an identity. (source concept habitatmech:GOLD.02383c20a7)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Algae** as a microbial habitat, with citations.

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

# Algae as a microbial habitat — definition research

**Concept:** `habitatmech:GOLD.02383c20a7` · label *Algae* · category HOST_ASSOCIATED · UNGROUNDED
**Attestation:** GOLD `Host-associated > Algae`, 394 assertions
**Nearest broader term on record:** `ENVO:01001000` · upstream xref: `FOODON:03411301`

---

## Proposed definition

> An environmental system determined by an organism which is determined by an alga — a photosynthetic eukaryote of any of the polyphyletic algal lineages — or by a part or surface of one, together with the exudate-enriched layer of the surrounding medium.

Aristotelian reading: **genus** = `ENVO:01001000` *environmental system determined by an organism*; **differentia** = the determining organism is an alga (eukaryotic, photosynthetic, non-embryophyte), and the system extends to the algal surface and its solute-enriched boundary layer.

This deliberately mirrors ENVO's own sibling wording — `ENVO:01001179` *cnidarian-associated environment* is defined as "An environmental system determined by a cnidarian or part of a cnidarian" ([OLS](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179)) — so the term drops into ENVO's existing pattern if it is ever requested upstream.

A minimal, maximally ENVO-idiomatic alternative, if the curator prefers terseness over informativeness:

> An environmental system determined by an alga or part of an alga.

---

## 1. What the concept denotes

### The reading the data supports

GOLD's five-level ecosystem classification puts the **host organism** at Ecosystem Category level for `Host-associated` samples (Ecosystem → Ecosystem Category → Ecosystem Type → Ecosystem Subtype → Specific Ecosystem; [Mukherjee et al., *NAR* 2021, GOLD v.8](https://academic.oup.com/nar/article/49/D1/D723/5957166), doi:10.1093/nar/gkaa983; [GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)). So `Host-associated > Algae` denotes **an alga in its role as the host environment of a microbial community** — the place a sample is taken from is algal biomass, an algal surface, or the water immediately surrounding an algal cell, with the microbes living on or in it.

The children in `data/raw/gold_ecosystem_paths.tsv` confirm this reading and show exactly what the sample is:

| GOLD path under `Host-associated > Algae` | assertions | what is sampled |
|---|---|---|
| Brown Algae | 231 | thallus / whole macroalga |
| Diatoms | 218 | cells + attached bacteria |
| Green algae | 108 | thallus, cells |
| Red algae | 73 | thallus |
| Diatoms > **Phycosphere** | 5 | the water layer around the cell |
| Microalgae | 4 | cells + associated bacteria |
| Dinoflagellates | 3 | cells |
| Brown Algae > Embryo, > Blade, > Whole body; Red algae > Sporeling, > Blade, > Embryo, > Whole body, > Ectosymbionts; Green algae > Ectosymbionts; Haptophytes; Cryptomonads/Cryptophytes; Golden Algae; Yellow-green algae; Biocrust; Mixed algae turf | 0–3 each | parts, life stages, assemblages |

27 GOLD paths sit under this node. The presence of *Phycosphere*, *Blade*, *Whole body* and *Ectosymbionts* as children is the strongest single piece of evidence that the parent means **algal host as habitat**, not "algae the taxonomic group" and not "algal biomass as a commodity".

### The boundary

**Inside the concept**
- The algal cell surface / thallus surface and its attached biofilm (epiphytic or *epibiotic* microbiome).
- The **phycosphere**: the diffusion-dominated region around an algal cell enriched in exuded organic substrates ([Seymour, Amin, Raina & Stocker, *Nature Microbiology* 2:17065, 2017](https://www.nature.com/articles/nmicrobiol201765), doi:10.1038/nmicrobiol.2017.65, PMID [28555622](https://pubmed.ncbi.nlm.nih.gov/28555622/)).
- Algal internal tissues and intercellular space — endophytic and endosymbiotic microbes ([Saha et al., *New Phytologist* 2024](https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.20018), doi:10.1111/nph.20018).
- Algal parts and life stages when sampled as host material (blade, embryo, sporeling).

**Outside the concept (neighbouring concepts)**
- **Algal blooms** as water-column features — `ENVO:2000004` *algal bloom*, `ENVO:01000057` *marine algal bloom*, `ENVO:2000005` *freshwater algal bloom*. These are aquatic environmental features, and the sample is bulk water containing algae, not the alga as host.
- **Engineered algal systems** — GOLD files these separately and so does the corpus: `Engineered > Artificial ecosystem > Aquaculture > Algae raceway pond`, `Engineered > Lab culture > Culture media > Algae`, `Engineered > WWTP > Effluent > Algae cultivation tank`. `ENVO:03600047` *raceway pond* covers the first.
- **Periphyton / biofilm on a non-algal substrate** — `ENVO:03605000` *periphytic biofilm* ("Biofilm consisting of a mixture of algae, cyanobacteria, microbes, and detritus"): here the algae are community members, not the host.
- **Kelp forest** (`ENVO:01000058`) — a landscape-scale ecosystem built by algae; sampling a kelp forest is not sampling a kelp thallus.
- **Cyanobacteria** ("blue-green algae"). GOLD keeps a separate `Host-associated > Microbial` category, and every eukaryotic lineage appears as a child here (Rhodophyta, Chlorophyta, diatoms, dinoflagellates, haptophytes, cryptophytes, chrysophytes, xanthophytes) while cyanobacteria do not. **Curatorial recommendation: exclude cyanobacteria** and say so in the definition or a comment. FOODON's own note that "some tuft-forming bluegreen algae (Cyanobacteria) are sometimes considered seaweed" (`FOODON:03412266`) shows why this needs to be stated rather than assumed.

### Ambiguity to record, not to resolve silently

Two readings of the bare label "Algae" exist and the corpus must not blur them:

1. **Algae-as-host-environment** — the reading GOLD's path and children support, and the one this definition takes.
2. **Algae-as-organism-group** — the FOODON reading: "An informal term for a large, diverse group of photosynthetic eukaryotic organisms that are not necessarily closely related, and is thus polyphyletic" (`FOODON:03411301`). This is a class of organisms, not a place, which is precisely why the existing curator note demoted it from identity to xref (#99).

There is also a **partial-overlap ambiguity worth flagging**: ENVO's `ENVO:01001001` *plant-associated environment* is defined as "An environmental system determined by a green plant" with the exact synonym **"Viridiplantae-associated environment"**. Viridiplantae includes Chlorophyta, so `Host-associated > Algae > Green algae` arguably already has an ENVO home, while brown algae, red algae, diatoms and dinoflagellates do not. Two consequences for curation:
- The proposed *Algae* term overlaps `ENVO:01001001` for the green-algal subset. This is an honest overlap, not a defect, but it should be stated in a comment.
- The `Green algae` child record could reasonably ground to or parent under `ENVO:01001001` independently of what happens to the parent. *(This is my inference from the ENVO synonym plus NCBI Taxonomy's placement of Chlorophyta within Viridiplantae — [NCBI Taxonomy: Viridiplantae, txid33090](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=33090) — not a claim any source makes about this GOLD path.)*

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001000` — *environmental system determined by an organism*** ("An environmental system which is determined by a living organism"; exact synonym *host-associated environment*). This is already the nearest broader term on the record and it is the correct one. Its existing children are exactly the sibling set this term joins:

| CURIE | label | ENVO definition |
|---|---|---|
| `ENVO:01001001` | plant-associated environment | An environmental system determined by a green plant. |
| `ENVO:01001002` | animal-associated environment | An environmental system determined by an animal. |
| `ENVO:01001041` | fungi-associated environment | An environmental system determined by a fungal structure. |
| `ENVO:01001179` | cnidarian-associated environment | An environmental system determined by a cnidarian or part of a cnidarian. |

The gap is conspicuous: ENVO names plant, animal, fungal and even cnidarian host environments, but nothing for the algae. This is the same shape as the sponge, nematode and reptile cases the repo has already worked through, and it is why the answer here is a term request rather than a grounding.

### Near-misses in ENVO and why each fails

Checked by OLS search of ENVO for `alga` and `algal` (13 hits, listed below) plus the `ENVO:01001000` child list.

| CURIE | label | why it is not a match |
|---|---|---|
| `ENVO:01001189` | algal material | "An organic material which is primarily composed of living or dead algae, along with their exudates." **Closest miss.** It is an *environmental material*, not an *environmental system*, and it covers dead/detached biomass (wrack, bloom scum, harvested biomass) that is not a host. In MIxS triad terms it belongs in `env_medium`, not `env_local_scale`. **Recommend keeping it as a `relation: xref`** alongside the FOODON term. |
| `ENVO:2000004` / `ENVO:01000057` / `ENVO:2000005` | algal bloom / marine / freshwater | Features arising from a population increase in an aquatic system. Narrower *and* asserts bloom conditions the GOLD paths never claim — most algal host samples are from non-blooming algae. |
| `ENVO:02500018`, `02500021`–`02500025` | algal bloom process, collapse, algal production, bloom phase, toxin accumulation/degradation | Processes, not places. A process is not a habitat. |
| `ENVO:03605000` | periphytic biofilm | Narrower and mixed-constituent: a biofilm of algae + cyanobacteria + microbes + detritus on a substrate. Algae are inhabitants here, not the host. |
| `ENVO:01000058` | kelp forest | Narrower (kelp only) and at ecosystem scale; asserts a habitat-forming stand, not an individual host. |
| `ENVO:01000411` | infralittoral zone | A depth zone that happens to be algae-dominated. Geographic, not host-associated. |
| `ENVO:03600047` / `ENVO:03600074` | raceway pond / aquaculture farm | Engineered constructions; GOLD files algal cultivation under `Engineered`, so adopting these would cross the category boundary. |
| `ENVO:01000962/3` | diatomite / diatomite particle | Fossil siliceous rock. Dead, mineralised, no host relation. |
| `ENVO:00005739`, `ENVO:01001190` | sea foam, brown sea ice | Materials whose definitions mention algae; neither denotes an algal host. |
| `ENVO:01001001` | plant-associated environment | Covers green algae (Viridiplantae) but **not** Rhodophyta, brown algae, diatoms, dinoflagellates, haptophytes or cryptophytes — i.e. it covers 108 of the 394 assertions at best. Adopting it for the parent would misclassify red and brown algae as green plants. |

### Near-misses outside ENVO

| CURIE | label | why it fails |
|---|---|---|
| `FOODON:03411301` | algae | An organism group, explicitly "informal" and "polyphyletic". Organism ≠ habitat; this is the over-claim #99 removed. Keep as `relation: xref`. |
| `FOODON:00001184` | algae material | Material entity, same failure as `ENVO:01001189`, plus a food-domain framing. |
| `FOODON:03412266` | seaweed | Narrower (macroalgae only, ~304 of 394 assertions), organism-typed, and food-domain. |
| `PO:0030027` | thallus | "A whole plant in the gametophytic phase that has a flat growth form and no distinct organs." Anatomical structure, phase-specific, and PO's scope is green plants — it cannot carry brown or red algal thalli. |
| `BTO:0001366` | thallus | A generic body-plan term spanning algae, fungi and mosses; too broad in taxon and, again, an anatomical entity, not an environment. |
| `BTO:0001064` | phycobiont | The algal partner *in a lichen*. Denotes a symbiotic role, not the free-living algal host. |
| `NCBITaxon:2011160` | phycosphere metagenome | Not a habitat term — it is a metagenome taxonomy placeholder. Worth noting as **independent evidence that "phycosphere" is an established sampling context** with its own NCBI identifier. |

**Conclusion:** no term in ENVO, UBERON, FOODON, BTO or PO expresses "algal host environment". The `UNGROUNDED` + minted-identifier disposition is correct.

---

## 3. Differentia — what distinguishes it from its siblings

Ranked by how observable/measurable they are.

**a. The determining organism is a photosynthetic eukaryote outside the embryophytes.** This is the taxonomic differentia and the one that separates the term from `plant-associated`, `animal-associated`, `fungi-associated`. The lineages attested in GOLD are Rhodophyta, Chlorophyta, Phaeophyceae, Bacillariophyta, Dinophyceae, Haptophyta, Cryptophyta, Chrysophyceae and Xanthophyceae. Algae are polyphyletic — no common ancestor unites them (`FOODON:03411301`; [Egan et al. 2013](https://academic.oup.com/femsre/article/37/3/462/585525) frame seaweeds as three independently multicellular groups).

**b. The host is itself a primary producer, so the habitat's carbon supply is autochthonous and light-driven.** This is the strongest functional differentia and it is what makes an algal host unlike an animal gut. Diatoms alone account for roughly one-fifth of global photosynthesis, and associated bacteria remineralise much of that fixed carbon in situ ([Amin, Parker & Armbrust, *MMBR* 76:667–684, 2012](https://journals.asm.org/doi/10.1128/mmbr.00007-12), doi:10.1128/MMBR.00007-12, PMID [22933565](https://pubmed.ncbi.nlm.nih.gov/22933565/)).

**c. A diffusion-structured chemical microenvironment — the phycosphere.** Solute exchange near an algal cell is diffusion- rather than advection-dominated, producing a steep spherical gradient of exuded organics that chemotactic bacteria track. Phycosphere radius scales with cell radius, leakage rate, molecular diffusivity, bulk concentration and turbulence, and ranges from a few hundred micrometres to a few millimetres ([Seymour et al. 2017](https://www.nature.com/articles/nmicrobiol201765), doi:10.1038/nmicrobiol.2017.65). Seymour et al. explicitly frame it as the aquatic analogue of the rhizosphere — a useful precedent, since ENVO already has `ENVO:01001181` *rhizoplane* and rhizosphere terms.

**d. A host-selected surface biofilm chemically distinct from the surrounding water.** Reported epibacterial densities on seaweed surfaces span 10²–10⁷ cells cm⁻² ([Wahl et al., *Front. Microbiol.* 3:292, 2012](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2012.00292/full), doi:10.3389/fmicb.2012.00292), e.g. 8.3 × 10² to 6.3 × 10⁷ cm⁻² on *Laminaria hyperborea*. Surface communities are compositionally distinct from both planktonic and adjacent rock communities, indicating active host selection, and density and α-diversity increase from apical to basal thallus, giving a within-host maturation gradient ([Othmani et al. / *Front. Microbiol.* 11:494, 2020](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2020.00494/full), doi:10.3389/fmicb.2020.00494; [Lu et al., *Microbiome* 11, 2023](https://microbiomejournal.biomedcentral.com/) on core epiphytic bacteria shared across co-located *Ulva*, *Saccharina*, *Grateloupia* and *Gelidium*). Note the important counter-case: chemically defended hosts can carry *lower* densities than inert substrata, so "enriched relative to seawater" is not universally true (Wahl et al. 2012).

**e. Host chemical defence and host–microbe developmental dependence.** Macroalgae deploy reactive oxygen species and halogenated furanones against colonisers, while simultaneously depending on bacterial morphogens: axenic *Ulva mutabilis* develops a callus-like phenotype and only recovers normal morphogenesis when co-cultured with *Roseovarius* sp. MS2 and *Maribacter* sp. MS6; the *Maribacter*-derived morphogen thallusin induces rhizoid and cell wall formation at 11 pmol l⁻¹ ([Alsufyani et al., *J. Exp. Bot.* 71:3340–3349, 2020](https://academic.oup.com/jxb/article/71/11/3340/5721957), doi:10.1093/jxb/eraa066, PMID [32016363](https://pubmed.ncbi.nlm.nih.gov/32016363/); thallusin originally from [Matsuo et al., *Science* 307:1598, 2005](https://www.science.org/doi/10.1126/science.1105486)). This bidirectional dependence is what justifies "holobiont" framing and is the clearest evidence that the alga is a structured habitat rather than a passive surface ([Egan et al. 2013](https://academic.oup.com/femsre/article/37/3/462/585525), doi:10.1111/1574-6976.12011, PMID [23157386](https://pubmed.ncbi.nlm.nih.gov/23157386/)).

**f. Physical setting is predominantly aquatic** — marine intertidal/subtidal for macroalgae, pelagic for diatoms, dinoflagellates, haptophytes and cryptophytes. *(Inference from the child lineages, not a claim I found stated for the GOLD node. The `Biocrust` child is a terrestrial counter-example — see §6.)*

---

## 4. Sources

**Primary literature — the habitat and its microbial communities**
- Seymour JR, Amin SA, Raina J-B, Stocker R (2017). Zooming in on the phycosphere: the ecological interface for phytoplankton–bacteria relationships. *Nature Microbiology* 2:17065. doi:[10.1038/nmicrobiol.2017.65](https://doi.org/10.1038/nmicrobiol.2017.65) · PMID [28555622](https://pubmed.ncbi.nlm.nih.gov/28555622/) · [full text PDF](https://stockerlab.ethz.ch/wp-content/uploads/2017/05/100._Seymour_atall.pdf)
- Amin SA, Parker MS, Armbrust EV (2012). Interactions between diatoms and bacteria. *Microbiology and Molecular Biology Reviews* 76(3):667–684. doi:[10.1128/MMBR.00007-12](https://doi.org/10.1128/MMBR.00007-12) · PMID [22933565](https://pubmed.ncbi.nlm.nih.gov/22933565/)
- Egan S, Harder T, Burke C, Steinberg P, Kjelleberg S, Thomas T (2013). The seaweed holobiont: understanding seaweed–bacteria interactions. *FEMS Microbiology Reviews* 37(3):462–476. doi:[10.1111/1574-6976.12011](https://doi.org/10.1111/1574-6976.12011) · PMID [23157386](https://pubmed.ncbi.nlm.nih.gov/23157386/)
- Saha M et al. (2024). Progress and future directions for seaweed holobiont research. *New Phytologist*. doi:[10.1111/nph.20018](https://doi.org/10.1111/nph.20018)
- Wahl M, Goecke F, Labes A, Dobretsov S, Weinberger F (2012). The second skin: ecological role of epibiotic biofilms on marine organisms. *Frontiers in Microbiology* 3:292. doi:[10.3389/fmicb.2012.00292](https://doi.org/10.3389/fmicb.2012.00292) — source of the 10²–10⁷ cells cm⁻² range
- Othmani A et al. (2020). A multi-omics analysis suggests links between the differentiated surface metabolome and epiphytic microbiota along the thallus of a Mediterranean seaweed holobiont. *Frontiers in Microbiology* 11:494. doi:[10.3389/fmicb.2020.00494](https://doi.org/10.3389/fmicb.2020.00494) · PMC[7111306](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7111306/)
- Alsufyani T, Califano G, Deicke M, Grueneberg J, Weiss A, Engelen AH, Kwantes M, Mohr JF, Ulrich JF, Wichard T (2020). Macroalgal–bacterial interactions: identification and role of thallusin in morphogenesis of the seaweed *Ulva*. *Journal of Experimental Botany* 71(11):3340–3349. doi:[10.1093/jxb/eraa066](https://doi.org/10.1093/jxb/eraa066) · PMID [32016363](https://pubmed.ncbi.nlm.nih.gov/32016363/)
- Matsuo Y, Imagawa H, Nishizawa M, Shizuri Y (2005). Isolation of an algal morphogenesis inducer from a marine bacterium. *Science* 307:1598. doi:[10.1126/science.1105486](https://doi.org/10.1126/science.1105486)
- Nahor O et al. (2024). Epiphytic microbiome associated with intertidal seaweeds in the Mediterranean Sea. *Scientific Reports* 14. [nature.com/articles/s41598-024-69362-y](https://www.nature.com/articles/s41598-024-69362-y)

**Standards, vocabularies and ontologies**
- Mukherjee S et al. (2021). Genomes OnLine Database (GOLD) v.8. *Nucleic Acids Research* 49(D1):D723–D733. doi:[10.1093/nar/gkaa983](https://doi.org/10.1093/nar/gkaa983) — five-level ecosystem classification, host at Ecosystem Category level
- Mukherjee S et al. (2023). Twenty-five years of GOLD: v.9. *Nucleic Acids Research* 51(D1):D957–D963. doi:[10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974) — Host-Associated environmental package
- [JGI GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)
- Buttigieg PL et al. (2013). The environment ontology: contextualising biological and biomedical entities. *J. Biomed. Semantics* 4:43. doi:[10.1186/2041-1480-4-43](https://doi.org/10.1186/2041-1480-4-43) · PMC[3904460](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3904460/)
- Buttigieg PL et al. (2016). The environment ontology in 2016. *J. Biomed. Semantics* 7:57. doi:[10.1186/s13326-016-0097-6](https://doi.org/10.1186/s13326-016-0097-6) · PMC[5035502](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/)
- ENVO term definitions verified via [EBI OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo) (`ENVO:01001000`, `01001001`, `01001002`, `01001041`, `01001179`, `01001189`, `2000004`, `03605000`) and the repo's vendored slice `data/raw/ontology_terms.tsv`
- ENVO term-request conventions (genus–differentia required, definition citations mandatory): [Creating good definitions](https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions), [Adding classes to ENVO](https://github.com/EnvironmentOntology/envo/wiki/Adding-classes-to-ENVO). Related discussion of the organism-associated pattern: [ENVO issue #1029, "EnvO terms for host-associated samples"](https://github.com/EnvironmentOntology/envo/issues/1029)

**Explicitly flagged as my inference, not sourced**
- That the concept should exclude cyanobacteria (argued from GOLD's child set and the separate `Host-associated > Microbial` category, not stated by GOLD).
- That `ENVO:01001001` partially covers green algae via its *Viridiplantae-associated environment* synonym (argued from the ENVO synonym + NCBI Taxonomy placement).
- That the concept is predominantly aquatic (argued from the attested child lineages).
- That `ENVO:01001189` *algal material* is the best material-side xref candidate.
- That no ENVO new-term request for an algae-associated environment currently exists — searches did not surface one, but I did not exhaustively enumerate the ENVO issue tracker, so treat this as unconfirmed.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- algae-associated environment; algal host environment
- algal microbiome / algal holobiont (community-side naming for the same setting)
- seaweed holobiont, macroalgal holobiont (macroalgal subset — Egan et al. 2013)
- phycosphere (the microscale subset around an individual cell — Seymour et al. 2017; and see `NCBITaxon:2011160` *phycosphere metagenome*)
- algal surface / thallus surface / algal epibiota / epiphytic biofilm (surface subset — Wahl et al. 2012)
- alga-associated (singular form, useful for OBO label style)

**Commonly but wrongly treated as the same thing**

| Confusable | Why it is different |
|---|---|
| **algae** (`FOODON:03411301`) | A polyphyletic group of organisms. Grounding to it publishes "this habitat *is* the organism group" — the exact over-claim retired in #99. |
| **algal material** (`ENVO:01001189`, `FOODON:00001184`) | A material composed of living *or dead* algae plus exudates. Covers wrack and harvested biomass; a `env_medium`, not a host system. |
| **algal bloom** (`ENVO:2000004` and kin) | A water-column feature. Sampling a bloom samples water; asserts bloom conditions absent from most algal-host samples. |
| **periphyton / periphytic biofilm** (`ENVO:03605000`) | Algae are constituents, not host; includes cyanobacteria and detritus on an abiotic substrate. |
| **kelp forest** (`ENVO:01000058`) | Landscape-scale stand, not an individual host. |
| **algal culture / raceway pond** (`ENVO:03600047`, GOLD `Engineered > …`) | Engineered systems, filed under a different top-level category. |
| **cyanobacteria / "blue-green algae"** | Prokaryotes. Included in colloquial "algae" and in some seaweed definitions; GOLD does not place them here. |
| **lichen** (`FOODON:03412345`) / **phycobiont** (`BTO:0001064`) | A fungal–algal composite organism, and the algal partner's *role* within it. A distinct habitat with its own literature. |
| **diatomite** (`ENVO:01000962`) | Fossilised siliceous rock. Dead and mineralised. |
| **plant-associated environment** (`ENVO:01001001`) | Covers green algae only under the Viridiplantae reading; wrong for red and brown algae, diatoms and dinoflagellates. |

---

## 6. Should it be a term at all?

**Yes.** The evidence supports a term request, on all four of the corpus's usual tests:

1. **It is a place, not an organism class.** The GOLD path denotes an alga acting as host — the setting a microbial community occupies — which is exactly what `ENVO:01001000` models. The taxon term `FOODON:03411301` is the organism class and belongs in `relation: xref`. Under the rule the repo settled after #114/#112, this is the sponge/nematode/reptile pattern, not a `NOT_APPLICABLE`.
2. **The genus exists and the sibling slot is empty.** ENVO names plant-, animal-, fungi- and cnidarian-associated environments and nothing for algae.
3. **It is not a process, quality, disease or procedure.** ENVO's algal *processes* (`ENVO:02500018` etc.) exist separately and none of them is this.
4. **It carries real assertion volume** — 394 at the node, 646 across the subtree — and a substantial primary literature treating the alga as a structured microbial habitat.

**Three caveats a curator should carry forward, none of which blocks the term:**

- **`Host-associated > Algae > Biocrust` (0 assertions) is misfiled upstream.** Biological soil crusts are terrestrial, and typically cyanobacteria-dominated rather than eukaryote-algal — so this child sits under an algal-host parent while denoting a terrestrial community-level feature. It should get its own decision rather than inheriting this definition. *(Inference from the GOLD path plus general biocrust literature; I did not verify GOLD's intent.)*
- **`Mixed algae turf` (0 assertions)** denotes an assemblage of many algal individuals — closer to a benthic feature than to a single host. Also worth a separate decision.
- **The part/life-stage children need the part-vs-whole rule applied individually.** `Blade`, `Whole body`, `Embryo`, `Sporeling`, `Ectosymbionts` and `Phycosphere` each fall differently: *Blade* is a part (grounds to an anatomy term if one exists — note neither `PO:0030027` nor `BTO:0001366` *thallus* is a blade term, and PO's green-plant scope will not carry brown or red algal blades); *Whole body*, *Embryo* and *Sporeling* are the whole organism or a life stage, so under the #112 rule they keep minted identities with the organism term as `xref`; *Phycosphere* is a genuine microenvironment and the best candidate in the whole subtree for a term request in its own right, with `NCBITaxon:2011160` *phycosphere metagenome* and Seymour et al. 2017 as supporting evidence.

**Recommended disposition for `habitatmech:GOLD.02383c20a7`:** `CONFIRM_UNGROUNDED` with `parent_habitats: ENVO:01001000` (*environmental system determined by an organism*) as the genus, `FOODON:03411301` demoted to `relation: xref`, and `ENVO:01001189` *algal material* added as a second `xref` for the material-side link.

## Citations

1. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179
2. https://academic.oup.com/nar/article/49/D1/D723/5957166
3. https://gold.jgi.doe.gov/ecosystem_classification
4. https://www.nature.com/articles/nmicrobiol201765
5. https://pubmed.ncbi.nlm.nih.gov/28555622/
6. https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.20018
7. https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=33090
8. https://academic.oup.com/femsre/article/37/3/462/585525
9. https://journals.asm.org/doi/10.1128/mmbr.00007-12
10. https://pubmed.ncbi.nlm.nih.gov/22933565/
11. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2012.00292/full
12. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2020.00494/full
13. https://microbiomejournal.biomedcentral.com/
14. https://academic.oup.com/jxb/article/71/11/3340/5721957
15. https://pubmed.ncbi.nlm.nih.gov/32016363/
16. https://www.science.org/doi/10.1126/science.1105486
17. https://pubmed.ncbi.nlm.nih.gov/23157386/
18. https://doi.org/10.1038/nmicrobiol.2017.65
19. https://stockerlab.ethz.ch/wp-content/uploads/2017/05/100._Seymour_atall.pdf
20. https://doi.org/10.1128/MMBR.00007-12
21. https://doi.org/10.1111/1574-6976.12011
22. https://doi.org/10.1111/nph.20018
23. https://doi.org/10.3389/fmicb.2012.00292
24. https://doi.org/10.3389/fmicb.2020.00494
25. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7111306/
26. https://doi.org/10.1093/jxb/eraa066
27. https://doi.org/10.1126/science.1105486
28. https://www.nature.com/articles/s41598-024-69362-y
29. https://doi.org/10.1093/nar/gkaa983
30. https://doi.org/10.1093/nar/gkac974
31. https://doi.org/10.1186/2041-1480-4-43
32. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3904460/
33. https://doi.org/10.1186/s13326-016-0097-6
34. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/
35. https://www.ebi.ac.uk/ols4/ontologies/envo
36. https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions
37. https://github.com/EnvironmentOntology/envo/wiki/Adding-classes-to-ENVO
38. https://github.com/EnvironmentOntology/envo/issues/1029