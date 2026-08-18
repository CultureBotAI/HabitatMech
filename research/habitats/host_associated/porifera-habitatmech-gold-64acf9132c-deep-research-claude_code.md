---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T19:53:31.390238'
end_time: '2026-08-17T19:59:56.713914'
duration_seconds: 385.32
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Porifera
  habitat_identifier: habitatmech:GOLD.64acf9132c
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Porifera'
  assertions: '90'
  parent_terms: ENVO:01001000
  xrefs: NCBITaxon:6040
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term NCBITaxon:6040 'Porifera' attached as a parent. Host-taxon reversal\
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
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.64acf9132c)"
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
  web_search_requests: 18
  num_turns: 34
  total_cost_usd: 3.49791
  session_id: b4b58354-6b30-45b8-b234-f73183f5cece
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 19
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Porifera
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.64acf9132c
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Porifera
- **Upstream assertion volume:** 90
- **Nearest broader term already on the record:** ENVO:01001000
- **Cross-references upstream suggested:** NCBITaxon:6040

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term NCBITaxon:6040 'Porifera' attached as a parent. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.64acf9132c)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Porifera** as a microbial habitat, with citations.

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

I'll research this now — starting with the ontology terms and the sponge-microbiome literature in parallel.

# Porifera as a microbial habitat — definition research

**Concept:** `habitatmech:GOLD.64acf9132c` — "Porifera" · HOST_ASSOCIATED · UNGROUNDED
**Source path:** GOLD `Host-associated > Porifera` (90 assertions, unit ORGANISM)

---

## Proposed definition

> An environment associated with an aquatic invertebrate which is determined by a sponge (phylum Porifera), whose water-pumping aquiferous system and collagenous mesohyl matrix house the associated microbial community.

Genus term: **ENVO:01001176** `environment associated with an aquatic invertebrate` — present in the vendored slice (`data/raw/ontology_terms.tsv`) with exactly that label, so it is usable as a `GROUND_AS_PARENT` target today.

---

## 1. What the concept denotes

The label names the **sponge animal considered as the place a microbial sample was taken from** — not the clade Porifera as a taxonomic group. Concretely, a sample against this concept is sponge body material: whole sponge or a piece of one, comprising the pinacoderm, the aquiferous canal system and choanocyte chambers through which seawater is pumped, and above all the **mesohyl** — the collagenous extracellular matrix between the epithelia, which is where dense symbiont populations actually sit ([Taylor et al. 2007, *Microbiol Mol Biol Rev* 71:295–347](https://pmc.ncbi.nlm.nih.gov/articles/PMC1899876/); [Hentschel et al. 2012, *Nat Rev Microbiol* 10:641–654, doi:10.1038/nrmicro2839](https://www.nature.com/articles/nrmicro2839)).

**Inside the concept:** any sponge in any of the four extant classes (Demospongiae, Hexactinellida, Calcarea, Homoscleromorpha) acting as host; marine *and* freshwater sponges; sponge tissue, mesohyl, larvae and gemmules as sample material; both HMA and LMA symbiotic phenotypes.

**Outside the concept, adjacent:**
- The **water column immediately around or inside the sponge** as an ambient marine sample — that is a marine-water concept, not a host-associated one.
- **Sponge reefs** as a geographic/biome feature — ENVO:01000161 / ENVO:01000123 (see §2).
- **The taxon Porifera** — NCBITaxon:6040. A phylum is a class of organisms, not a place; it stays an `xref`, per the repo's #99/#114 rule.

**Ambiguity worth flagging, and it is not the label's ambiguity but the corpus's.** GOLD's own tree is `Host-associated > Porifera` → `> Sponge` (323 assertions) → `> Sponge > Tissue` (7). Verified against `data/raw/gold_ecosystem_paths.tsv`: those are the *only* three Porifera paths, and the 90 assertions on this node are attached at the phylum node directly, not inherited. So `Porifera` is a "sponge host, sponge unspecified, body site unspecified" bucket whose single child, `Sponge` (`habitatmech:GOLD.affd2445ea`), denotes the same thing one level down. These two are near-synonymous in denotation and differ only in GOLD path depth. That is a **merge candidate**, not two definitions — see §6.

There are two readings of the label itself, and the source path resolves them: (a) the clade, (b) a sponge acting as host. The `Host-associated` root of the path forces reading (b).

## 2. Genus — the broader kind

**Recommended genus: ENVO:01001176 `environment associated with an aquatic invertebrate`.**
Definition in ENVO: *"An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system."* (sic — "vetebral" is a typo upstream in ENVO). Verified via [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176) and in the repo's vendored slice.

Sponges satisfy it exactly: metazoan, no vertebral column, aquatic (marine or fresh). Its position in ENVO — `subClassOf ENVO:01001002` *and* `subClassOf ENVO:01001055`, per `data/raw/ontology_subclass_edges.tsv` — is the right place in the hierarchy, and it currently has **no children in ENVO**, so nothing narrower pre-empts it.

**Near-misses and why each fails:**

| Term | Label | Why it is not the match |
|---|---|---|
| ENVO:01001000 | environmental system determined by an organism | The record's **current** parent. Far too broad — covers plants, fungi and animals alike. Synonym "host-associated environment" makes it look apt; it is the whole host-associated root. Recommend tightening to ENVO:01001176. |
| ENVO:01001002 | animal-associated environment | Correct but not smallest; ENVO:01001176 sits below it and is still true of every sponge. |
| ENVO:01001055 | environment associated with an animal part or small animal | Asserts *part-of-an-animal* or *small*. A sponge host is a whole animal, and giant barrel sponges (*Xestospongia muta*) exceed a metre — the "small" clause is a claim GOLD does not make. Near-miss, worth recording. |
| ENVO:01001179 | cnidarian-associated environment | Not a match — it is the **precedent**. ENVO already carries a phylum-level host-associated environment class for Cnidaria (*"An environmental system determined by a cnidarian or part of a cnidarian"*), sibling under ENVO:01001002. There is no Porifera counterpart. This is direct evidence that a `sponge-associated environment` NTR is well-formed and structurally identical to something ENVO has already accepted. The corpus already uses ENVO:01001179 this way on `coral.yaml`. |
| ENVO:01000161 / ENVO:01000123 | marine sponge reef / marine sponge reef biome | The only two ENVO classes matching "sponge", and both are geographic features: reefs *built by* hexactinosan sponges, *"found only in glacier-scoured troughs of low-angle continental shelf"* (slice text). They exclude demosponges, exclude freshwater sponges, and denote the seafloor structure rather than the host body. Already correctly rejected on the sibling `sponge.yaml`. |
| NCBITaxon:6040 | Porifera | The taxon. `xref` only. |
| PORO (Porifera Ontology) | — | An active OBO ontology of sponge anatomy (mesohyl, choanocyte chamber, spicule), maintained by Bob Thacker, Stony Brook ([obofoundry.org/ontology/poro.html](https://obofoundry.org/ontology/poro.html)). Serves the MIxS `env_medium` / anatomical slot for sponge *parts*, and would be the right target for a future `Porifera > Sponge > Tissue` record. It supplies no environment class, so it does not serve as genus here. |

**Confirmed:** a targeted search of ENVO's issue tracker surfaced no existing NTR for a sponge-associated environment; the nearest is [envo#1029 "EnvO terms for host-associated samples"](https://github.com/EnvironmentOntology/envo/issues/1029), which established the general host-associated-environment pattern.

## 3. Differentia — what distinguishes it from siblings

Under the genus, the siblings are other aquatic-invertebrate hosts (cnidarians, molluscs, tunicates, echinoderms, annelids). What separates sponge-associated environment, in order of how observable it is:

**Host body plan and sampling compartment.** Sponges lack organs and true tissues; the microbial habitat is not a gut or a mucus layer but the **mesohyl**, a collagenous extracellular matrix perfused by an aquiferous canal system, with additional intracellular symbionts in bacteriocytes ([Taylor et al. 2007](https://pmc.ncbi.nlm.nih.gov/articles/PMC1899876/); [Hentschel et al. 2012](https://www.nature.com/articles/nrmicro2839)). This is the single strongest differentia — no sibling host offers the same compartment.

**Extreme, bimodally distributed symbiont density.** Sponge species partition into two symbiotic phenotypes: **HMA** (high microbial abundance), with 10⁸–10¹⁰ cells g⁻¹ tissue, and **LMA**, at 10⁵–10⁶ cells g⁻¹, i.e. roughly ambient seawater levels ([Gloeckner et al. 2014, *Biol Bull* 227:78–88, doi:10.1086/BBLv227n1p78](https://www.journals.uchicago.edu/doi/full/10.1086/BBLv227n1p78) — TEM survey of 56 species, 28 HMA / 28 LMA; Agelasida and Verongida exclusively HMA, Poecilosclerida exclusively LMA). Microbial biomass reaches **up to ~35% of sponge biomass** ([Hentschel et al. 2012](https://www.nature.com/articles/nrmicro2839)); higher figures (40–60%) circulate in the literature but I did not verify them against a primary measurement.

**HMA/LMA is correlated with measurable host physiology:** HMA sponges have denser mesohyl, narrower canals and smaller choanocyte chambers, and pump 52–94% more slowly per unit volume than LMA sponges ([Weisz, Lindquist & Martens 2008, *Oecologia* 155:367–376, doi:10.1007/s00442-007-0910-0](https://link.springer.com/article/10.1007/s00442-007-0910-0)).

**Continuous high-throughput seawater perfusion.** As sessile filter feeders sponges process very large water volumes — an often-cited upper estimate is ~24,000 L per kg of sponge per day ([Taylor et al. 2007](https://pmc.ncbi.nlm.nih.gov/articles/PMC1899876/)). The habitat is therefore both an enclosed matrix and a high-flux interface with the water column.

**A community demonstrably distinct from the surrounding environment.** The global survey of **804 samples from 81 sponge species** across 20 countries, plus 133 seawater and 36 sediment samples, recovered **41 phyla including candidate phyla**, with every sponge hosting members of ≥13 phyla, and found *"limited overlap in microbiome structure … between sponges and the seawater and sediment samples"*; individual species (*Carteriospongia foliascens*, *Ircinia variabilis*) exceed 12,000 OTUs, approaching the ~15,000 of surrounding seawater ([Thomas et al. 2016, *Nat Commun* 7:11870, doi:10.1038/ncomms11870](https://www.nature.com/articles/ncomms11870)).

**Sponge-enriched lineages.** 27% of 7,546 sponge-derived rRNA sequences fell into monophyletic sponge-specific clusters spanning ≥14 bacterial phyla — 178 SC and 32 sponge/coral SCC clusters, best represented in Chloroflexi, Cyanobacteria, *Poribacteria*, Betaproteobacteria and Acidobacteria ([Simister et al. 2012, *Environ Microbiol* 14:517–524, doi:10.1111/j.1462-2920.2011.02664.x](https://pubmed.ncbi.nlm.nih.gov/22151434/)). Deep sequencing of >12 M pyrotags from 649 non-sponge samples showed many are widespread but rare elsewhere, which is why the field shifted from "sponge-specific" to "sponge-enriched" ([Taylor et al. 2013, *ISME J*, doi:10.1038/ismej.2012.111](https://www.nature.com/articles/ismej2012111)). Note the sponge/coral shared clusters — that is a real overlap with the cnidarian sibling, and a definition should not claim exclusivity.

**Characteristic symbiont metabolism.** Nitrification (ammonia-oxidising archaea and nitrite-oxidising bacteria, some vertically inherited, e.g. *Ca.* Nitrosokoinonia and *Ca.* Nitrosymbion in *Coscinoderma matthewsi*, [PMC11812461](https://pmc.ncbi.nlm.nih.gov/articles/PMC11812461/)), denitrification, sulfur cycling and H₂S detoxification, and carbon/nitrogen/sulfur exchange quantified by genome-scale metabolic modelling of a *Stylissa* holobiont ([Nat Commun 2024, doi:10.1038/s41467-024-55222-w](https://www.nature.com/articles/s41467-024-55222-w)). At ecosystem scale, the **sponge loop** converts reef dissolved organic matter into detritus available to higher trophic levels ([de Goeij et al. 2013, *Science* 342:108–110](https://www.science.org/doi/10.1126/science.1241981)).

**Antiquity and transmission.** Sponge–microbe association is among the oldest metazoan–microbe symbioses; symbionts are transmitted both vertically (via larvae and, in freshwater sponges, gemmules) and horizontally ([Pita et al. 2018, *Microbiome* 6:46, doi:10.1186/s40168-018-0428-1](https://link.springer.com/article/10.1186/s40168-018-0428-1); [Björk et al. / Webster & Thomas 2016, *mBio* 7:e00135-16](https://journals.asm.org/doi/10.1128/mbio.00135-16)).

**Freshwater sponges are inside the concept and behave consistently.** *Ephydatia muelleri* microbiomes are distinct from ambient water and adjacent biofilms and share functional signatures with marine sponge microbiota, though taxonomically divergent ([Sugden et al. 2022, *ISME J* 16:2503–2512, doi:10.1038/s41396-022-01296-7](https://www.nature.com/articles/s41396-022-01296-7); review: [Lo Giudice et al. 2023, *Microorganisms* 12:25, doi:10.3390/microorganisms12010025](https://doi.org/10.3390/microorganisms12010025)). **This matters for the definition:** do not write "marine" into it. GOLD's path says Porifera, not marine Porifera, and freshwater sponge metagenomes exist.

**My inference, not a source claim:** that the mesohyl-plus-aquiferous-system compartment is the *defining* differentia versus other aquatic-invertebrate hosts. The sources establish the compartment and the densities; the judgement that this is the right discriminator for an ontology definition is mine.

## 4. Sources

- Taylor MW, Radax R, Steger D, Wagner M (2007). Sponge-associated microorganisms: evolution, ecology, and biotechnological potential. *Microbiol Mol Biol Rev* 71:295–347. https://pmc.ncbi.nlm.nih.gov/articles/PMC1899876/
- Hentschel U, Piel J, Degnan SM, Taylor MW (2012). Genomic insights into the marine sponge microbiome. *Nat Rev Microbiol* 10:641–654. doi:10.1038/nrmicro2839 · PMID 22842661
- Thomas T, Moitinho-Silva L, Lurgi M, et al. (2016). Diversity, structure and convergent evolution of the global sponge microbiome. *Nat Commun* 7:11870. doi:10.1038/ncomms11870 · PMC4912640 (16 June 2016)
- Moitinho-Silva L, Nielsen S, Amir A, et al. (2017). The sponge microbiome project. *GigaScience* 6:gix077. doi:10.1093/gigascience/gix077 · PMID 29020741 (3,569 sponge specimens, ≥268 species, 1.1 bn reads). Erratum: *GigaScience* 7:giy145.
- Simister RL, Deines P, Botté ES, Webster NS, Taylor MW (2012). Sponge-specific clusters revisited. *Environ Microbiol* 14:517–524. doi:10.1111/j.1462-2920.2011.02664.x · PMID 22151434
- Taylor MW, Tsai P, Simister RL, et al. (2013). 'Sponge-specific' bacteria are widespread (but rare) in diverse marine environments. *ISME J*. doi:10.1038/ismej.2012.111
- Gloeckner V, Wehrl M, Moitinho-Silva L, et al. (2014). The HMA-LMA dichotomy revisited. *Biol Bull* 227:78–88. doi:10.1086/BBLv227n1p78 · PMID 25216505
- Weisz JB, Lindquist N, Martens CS (2008). Do associated microbial abundances impact marine demosponge pumping rates and tissue densities? *Oecologia* 155:367–376. doi:10.1007/s00442-007-0910-0
- Pita L, Rix L, Slaby BM, Franke A, Hentschel U (2018). The sponge holobiont in a changing ocean. *Microbiome* 6:46. doi:10.1186/s40168-018-0428-1 · PMC5845141
- Webster NS, Thomas T (2016). The sponge hologenome. *mBio* 7:e00135-16. https://journals.asm.org/doi/10.1128/mbio.00135-16
- de Goeij JM, van Oevelen D, Vermeij MJA, et al. (2013). Surviving in a marine desert: the sponge loop retains resources within coral reefs. *Science* 342:108–110. doi:10.1126/science.1241981
- Sugden S, Holert J, Cardenas E, et al. (2022). Microbiome of the freshwater sponge *Ephydatia muelleri* shares compositional and functional similarities with those of marine sponges. *ISME J* 16:2503–2512. doi:10.1038/s41396-022-01296-7
- Lo Giudice A, et al. (2023). Freshwater sponges as a neglected reservoir of bacterial biodiversity. *Microorganisms* 12:25. doi:10.3390/microorganisms12010025
- Van Soest RWM, Boury-Esnault N, Vacelet J, et al. (2012). Global diversity of sponges (Porifera). *PLoS ONE* 7:e35105. doi:10.1371/journal.pone.0035105 — 8,553 accepted species as of 31 Aug 2011, 83% Demospongiae; four extant classes.
- ENVO terms: https://www.ebi.ac.uk/ols4/ontologies/envo — ENVO:01001176, ENVO:01001179, ENVO:01001055, ENVO:01001002, ENVO:01001000, ENVO:01000161, ENVO:01000123. Cross-checked against `data/raw/ontology_terms.tsv` and `data/raw/ontology_subclass_edges.tsv` in this repo.
- PORO (Porifera Ontology): https://obofoundry.org/ontology/poro.html
- GOLD ecosystem classification: https://gold.jgi.doe.gov/ecosystem_classification; five-level scheme per Ivanova et al., three top-level branches Environmental / Host-associated / Engineered.

## 5. Synonyms, and what not to conflate

**In real use for this concept:** *sponge-associated environment*; *sponge host*; *sponge holobiont* (strictly the host+microbiota system, not the place — see below); *sponge microbial habitat*; *sponge tissue* (as sample material). GOLD itself uses the bare taxon name `Porifera` and, one level down, `Sponge`.

**Do not conflate:**

- **Porifera the taxon (NCBITaxon:6040).** Same string, different kind of thing. `xref`, never identity.
- **Sponge holobiont.** A holobiont is *"complex ecosystems consisting of the host, the microbiota, and the interactions among them"* ([Pita et al. 2018](https://link.springer.com/article/10.1186/s40168-018-0428-1)) — it includes the microbes, so it is not the habitat *they* live in. Convenient shorthand, wrong as a definition.
- **Marine sponge reef (ENVO:01000161) / marine sponge reef biome (ENVO:01000123).** A geographic seafloor feature built by hexactinosan skeletons; the sponge as host is not a reef, most sponges do not build one, and the ENVO definition restricts these to glacier-scoured continental-shelf troughs.
- **"Sponge" in the domestic/material sense.** ENVO's other "sponge" hits are `foamed plastic` (ENVO:06105016) and `piece of plastic foam` (ENVO:06105006), matched on *sponge-like structure*. A lexical grounding pass will hit these; they are wrong.
- **Sponge-derived seawater / inhalant–exhalant samples.** Water sampled at the osculum measures sponge *function*, not the sponge-associated habitat.
- **Coral / cnidarian-associated environment.** Distinct genus-sibling, despite the 32 shared sponge/coral clusters.
- **Sponge cell culture and sponge-derived isolate media.** Engineered, not host-associated.

## 6. Should it be a term at all?

**Yes — it is a habitat, and it should keep its own minted identity.** It passes every test the repo's #114/#99 rule sets: a sponge acting as host is where the microbe lives; ENVO models the pattern at plant-, animal-, fungi- and cnidarian-associated environment; and the concept has 90 direct organism-level assertions plus 323 on its immediate child. The 2026-08-16 `CONFIRM_UNGROUNDED` note on the record is correct in substance.

**Two concrete recommendations for the curator:**

1. **Tighten the parent.** `parent_habitats: ENVO:01001000` is the host-associated root and under-specifies badly. Replace with **ENVO:01001176 `environment associated with an aquatic invertebrate`** — in the vendored slice, exact label match, and it is where ENVO already puts this kind of thing. Keep `NCBITaxon:6040` as the `xref` it already is. This also fixes an internal inconsistency: the child record `sponge.yaml` currently parents to ENVO:01001002, which is *broader* than the genus available.

2. **Treat `Porifera` and `Sponge` as a probable merge, not two definitions.** `habitatmech:GOLD.64acf9132c` (Porifera, 90) and `habitatmech:GOLD.affd2445ea` (Sponge, 323) denote the same thing at two GOLD depths; the raw paths confirm Porifera has no sibling branch under it other than Sponge. Writing two distinct genus-differentia definitions here would mean inventing a distinction GOLD does not draw. The repo has a decision type for exactly this (two novel concepts are the same, PR #116/#117) — I'd use it rather than duplicating the definition. If they are kept separate, the only honest differentia is path depth, which is a sampling artefact of GOLD's curation, not a property of the habitat.

**One ENVO NTR would serve both**, and its shape is already set by ENVO:01001179: *sponge-associated environment — "An environmental system determined by a sponge or part of a sponge."* Per the standing memory note, that submission needs your explicit per-request go-ahead; I have not filed anything.

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC1899876/
2. https://www.nature.com/articles/nrmicro2839
3. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176
4. https://obofoundry.org/ontology/poro.html
5. https://github.com/EnvironmentOntology/envo/issues/1029
6. https://www.journals.uchicago.edu/doi/full/10.1086/BBLv227n1p78
7. https://link.springer.com/article/10.1007/s00442-007-0910-0
8. https://www.nature.com/articles/ncomms11870
9. https://pubmed.ncbi.nlm.nih.gov/22151434/
10. https://www.nature.com/articles/ismej2012111
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC11812461/
12. https://www.nature.com/articles/s41467-024-55222-w
13. https://www.science.org/doi/10.1126/science.1241981
14. https://link.springer.com/article/10.1186/s40168-018-0428-1
15. https://journals.asm.org/doi/10.1128/mbio.00135-16
16. https://www.nature.com/articles/s41396-022-01296-7
17. https://doi.org/10.3390/microorganisms12010025
18. https://www.ebi.ac.uk/ols4/ontologies/envo
19. https://gold.jgi.doe.gov/ecosystem_classification