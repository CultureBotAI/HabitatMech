---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T04:20:19.940159'
end_time: '2026-08-18T04:27:32.281531'
duration_seconds: 432.34
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Embryo
  habitat_identifier: habitatmech:GOLD.b648ad12d6
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Algae > Red algae > Embryo'
  assertions: '0'
  parent_terms: (none)
  xrefs: UBERON:0000922
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term UBERON:0000922 'embryo' attached as a parent. Life-stage review\
    \ (#112): carried UBERON:0000922 'embryo' as a parent, reached by the ambiguous-leaf\
    \ rule rather than the path \u2014 several GOLD paths end in the same leaf, so\
    \ the ones that do not claim the term keep it as a parent. parent_habitats asserts\
    \ the parent is BROADER, and a larva or embryo is a whole organism rather than\
    \ a broader kind of place, so this is the same over-claim the identity cases had\
    \ one level up. Kept as an xref (#99). Per the rule #114 settled: the whole host\
    \ organism gets its own identity and an <X>-associated environment term; parts\
    \ of a host ground to the anatomy term. (source concept habitatmech:GOLD.b648ad12d6)"
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
  num_turns: 23
  total_cost_usd: 2.4630304999999995
  session_id: c909dff1-e71c-4e41-9a18-4e418997543e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 25
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Embryo
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.b648ad12d6
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Algae > Red algae > Embryo
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** UBERON:0000922

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term UBERON:0000922 'embryo' attached as a parent. Life-stage review (#112): carried UBERON:0000922 'embryo' as a parent, reached by the ambiguous-leaf rule rather than the path — several GOLD paths end in the same leaf, so the ones that do not claim the term keep it as a parent. parent_habitats asserts the parent is BROADER, and a larva or embryo is a whole organism rather than a broader kind of place, so this is the same over-claim the identity cases had one level up. Kept as an xref (#99). Per the rule #114 settled: the whole host organism gets its own identity and an <X>-associated environment term; parts of a host ground to the anatomy term. (source concept habitatmech:GOLD.b648ad12d6)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Embryo** as a microbial habitat, with citations.

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

# Research report — GOLD "Embryo" under *Host-associated > Algae > Red algae*

**Concept:** `habitatmech:GOLD.b648ad12d6` · label **Embryo** · category HOST_ASSOCIATED · UNGROUNDED
**Source path:** `Host-associated > Algae > Red algae > Embryo` (GOLD nodes `gold.ecosystem:7225`, `gold.ecosystem:7226`)
**Upstream assertion volume: 0** — no GOLD organism, study or biosample has ever been filed under this path.

---

## Proposed definition

> An **environmental system determined by an organism** ([ENVO:01001000](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000)) which is determined by a red alga (Rhodophyta) at its earliest post-fertilisation multicellular stage — the diploid carposporophyte retained on and nourished by the female gametophyte — and which comprises that structure's surfaces, mucilage and enclosing gametophytic tissue.

**Read the next section before using this sentence.** I can write it, but I do not recommend adopting it. The evidence points to this node being a vocabulary placeholder rather than an attested habitat, and the disposition I recommend is at §6.

---

## 1. What the concept denotes

### 1a. The label does not denote anything red algae have

"Embryo" is not a term of art in red algal biology. Red algae are not embryophytes: the zygote is *not* released and does not develop into an independent young sporophyte. Instead the fertilised carpogonium develops *in situ* into a third generation, the **carposporophyte** (gonimoblast filaments + carposporangia), which remains attached to and nutritionally dependent on the female gametophyte, enclosed by a gametophyte-derived **pericarp** — the whole assembly being a **cystocarp** ([Searles 1980, *Am. Nat.* 115:113–120, doi:10.1086/283548](https://www.journals.uchicago.edu/doi/abs/10.1086/283548); [Gonimoblast, Wikipedia](https://en.wikipedia.org/wiki/Gonimoblast); [Carpogonium, Wikipedia](https://en.wikipedia.org/wiki/Carpogonium)).

The canonical criterion for calling something an embryo — a zygote developing into a young sporophyte *protected by the multicellular archegonium* and nourished through placental transfer tissue — is exactly what defines Embryophyta and excludes all algae ([Embryophyte, Wikipedia](https://en.wikipedia.org/wiki/Embryophyte)). Red algae satisfy the *retention* and *matrotrophy* halves of that criterion (nutrient transfer runs through a multinucleate fusion cell / "placental tissue" formed from carpogonial, auxiliary and surrounding gametophyte cells) but not the archegonium half, which is why phycology withholds the word. The recognised algal precedent for matrotrophy is *Coleochaete* in the green algae, not Rhodophyta ([Matrotrophy, Wikipedia](https://en.wikipedia.org/wiki/Matrotrophy)).

The standard terminological chain in Rhodophyta is: carpogonium → zygote → **carposporophyte / cystocarp** → carpospore → **germling / sporeling** → tetrasporophyte ([Biology LibreTexts, Phylum Rhodophyta](https://bio.libretexts.org/Bookshelves/Botany/Botany_Lab_Manual_(Morrow)/18:_Red_and_Green_Algae/18.3:_Phylum_Rhodophyta_-_The_Red_Algae)). There is no slot in it for "embryo."

### 1b. The two readings, and why the source path cannot choose between them

If a sample really were filed here, it would be one of:

- **(A) The carposporophyte/cystocarp** — the post-zygotic, gametophyte-retained diploid body. This is the structural analogue of an embryo (retained, matrotrophic) and is the reading my proposed sentence takes. It is a *part of* an adult female thallus, not a free organism.
- **(B) The germling/sporeling** — the young thallus arising from a germinating carpospore or tetraspore. This is the developmental-stage analogue (a young whole organism). **GOLD already has a separate sibling node for this**: `Host-associated > Algae > Red algae > Sporeling` (2 organisms). A curator adopting reading (B) would be duplicating an existing, actually-populated record.

These are not the same place: (A) is enclosed maternal tissue on a mature alga; (B) is a free-living juvenile thallus on a substratum. **The source path does not disambiguate them, and the assertion count is zero, so there is no sample metadata to appeal to.** This is my inference from the path structure, not a claim any source makes.

### 1c. Strongest evidence for what GOLD meant: symmetry with the brown algae

The subtype set under Red algae — *Whole body, Blade, Embryo, Sporeling, Ectosymbionts* — mirrors the set under Brown Algae — *Whole body, Blade, Embryo*. Only the brown algae "Embryo" node carries samples (3 organisms); the red algae node carries none. GOLD's own documentation states the classification "is not a comprehensive list of all possible paths… it is primarily driven by the samples curated" ([GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification); [Mukherjee et al. 2023, *NAR* 51:D957–D963, doi:10.1093/nar/gkac974](https://academic.oup.com/nar/article/51/D1/D957/6786204)) — an empty node is therefore anomalous within GOLD's own stated method.

"Embryo" *is* legitimate for brown algae: *Fucus* embryogenesis (polar axis fixation, rhizoid determination) is a classic developmental system, and Fucales genuinely produce a zygote that develops into an embryo. My reading — stated as inference — is that the red algae subtype list was replicated from the brown algae list and the biologically inapplicable member came along with it.

**Boundary summary.** Inside: nothing attested. Neighbouring concepts that *are* attested and *do* have records: `Red algae > Sporeling` (young thallus), `Red algae > Blade`, `Red algae > Whole body`, `Brown Algae > Embryo` (`habitatmech:GOLD.32330da5da`, a separate record with 3 organisms).

---

## 2. Genus — the broader kind

**No ontology term expresses this concept.** The relevant genus, if the record is kept, is the top of ENVO's host-associated branch.

| Candidate | Verdict | Why |
|---|---|---|
| **ENVO:01001000** *environmental system determined by an organism* (syn. "host-associated environment") | **Best available genus** — but broad | Its only children are `ENVO:01001001` plant-associated, `ENVO:01001002` animal-associated, `ENVO:01001041` fungi-associated, and `ENVO:2100000` anatomical entity environment (verified against [OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000/hierarchicalChildren)). **There is no algae-associated environment term.** Algae are neither Viridiplantae *sensu* ENVO:01001001 (which is glossed "determined by a green plant") nor Metazoa nor Fungi, so the concept has no intermediate class. |
| **ENVO:01001001** *plant-associated environment* | Near-miss, fails | Defined as "determined by a green plant"; synonym "Viridiplantae-associated environment". Rhodophyta are Archaeplastida but not Viridiplantae. Adopting it would assert a clade membership the source does not claim. |
| **UBERON:0000922** *embryo* (the upstream suggestion, currently the record's xref) | Near-miss, fails twice | Its definition — "anatomical entity that comprises the organism in the early stages of growth and differentiation that are characterized by **cleavage**, the laying down of fundamental tissues, and the formation of **primitive organs and organ systems**", exemplified for mammals, insects and plants ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0000922)) — asserts organogenesis that a thallose alga does not undergo. Its definition xref is `BTO:0000379`, whose text in the vendored slice is explicitly "**An animal** in the early stages of growth…". Second failure: it is a whole-organism life stage, not a place — the same over-claim #112 settled. Keeping it as `relation: xref` is correct; do not promote it. |
| **PO:0009009** *plant embryo* | Fails | "A whole plant (PO:0000003) that participates in the plant embryo stage (PO:0007631)" ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/po/classes?obo_id=PO:0009009)). PO's scope is green plants; red algae are out of scope, and again this is a whole organism, not a habitat. |
| **FOODON:03411743** *red algae* | Fails, and already handled | The taxon, not a place — already carried as `relation: xref` on the parent record `habitatmech:GOLD.e789c273d0`. |
| **FOODON:03412266** *seaweed* / **FOODON:00001184** *algae material* | Fail | Food-material framing; `seaweed` is defined as the polyphyletic macroalgal group, i.e. an organism class. `algae material` is a material entity (harvested biomass), not a host environment. |
| **BTO:0001290** *sporocarp* ("a structure (as in **red algae**, fungi, or mosses) in or on which spores are produced") | Interesting near-miss, fails | This is the closest existing term to reading (A) — BTO explicitly extends it to red algae, where "sporocarp" is a legacy synonym for cystocarp. But it is an anatomical-structure term with a fungal/bryophyte centre of gravity, it is not the *embryo* concept, and grounding an empty node to it would invent an identity the source never asserted. Worth recording; not worth adopting. |

**No ENVO term names a red alga as a host environment, and no ontology in the vendored slice names an algal embryo.** That is the finding.

---

## 3. Differentia — what would distinguish it

If the record survives, the differentiae available under reading (A) are, in decreasing order of defensibility:

1. **Host clade and host part.** Determined by a rhodophyte, and specifically by the gametophyte-retained diploid generation rather than by vegetative thallus (blade, holdfast) or by a free-living juvenile — the property that separates it from its GOLD siblings *Blade*, *Whole body* and *Sporeling*.
2. **Enclosure.** The habitat surface is largely *internal to maternal tissue*: gonimoblast filaments and carposporangia sit inside a gametophyte-derived pericarp, functionally analogous to a seed coat ([Carposporophyte development literature summarised above](https://link.springer.com/article/10.1007/BF02114685)). This is a materially different microbial niche from an exposed thallus surface, where macroalgal–bacterial interaction is normally sited ([Egan et al. framing, reviewed in *Mar. Drugs* 18:641, doi:10.3390/md18120641](https://www.mdpi.com/1660-3397/18/12/641)).
3. **Matrotrophic chemistry.** Nutrient transfer runs through a multinucleate fusion cell / "placental tissue"; storage gonimoblast cells are loaded with floridean starch ([Cryptopleura ultrastructure, *Eur. J. Phycol.*-adjacent, doi:10.1016/S0248-4900(03)00085-6](https://www.sciencedirect.com/science/article/abs/pii/S0248490003000856)). A carbon-rich, enclosed, low-flow compartment is a plausible distinct niche — **this is my inference; I found no study that sampled it.**

**Physicochemistry, community composition, and characteristic taxa are all unavailable.** I could not find a single study of the microbiota of a red algal carposporophyte, cystocarp, or carpospore. The nearest published work is life-stage sampling in *Porphyra dioica* (conchocelis, conchosporangia, young blade, adult blade — the yeast fraction), which does not include the carposporophyte ([*Front. Microbiol.* 2026, doi:10.3389/fmicb.2026.1918765](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2026.1918765/full)). A review notes only that cross-kingdom quorum-sensing signalling around *carpospore liberation* is poorly known ([*Mar. Drugs* 18:641](https://www.mdpi.com/1660-3397/18/12/641)). The one demonstrated early-life-stage colonisation result in macroalgae is from **brown** algae: "the egg-containing oogonia of *F. vesiculosus* appear to be colonized from the parental thallus surface as they are released into the sea" ([Quigley et al. 2020, *Front. Microbiol.* 11:563118, doi:10.3389/fmicb.2020.563118](https://pmc.ncbi.nlm.nih.gov/articles/PMC7541829/), 24 Sep 2020) — that supports the *brown* algae Embryo record, not this one.

**A differentia written from this evidence would be structural only.** There is no measured physicochemistry or characteristic community to cite.

---

## 4. Sources

Verified in this session unless marked otherwise.

- JGI GOLD, Ecosystem Classification — https://gold.jgi.doe.gov/ecosystem_classification ; path tree — https://gold.jgi.doe.gov/ecosystemtree
- Mukherjee S. *et al.* (2023) Twenty-five years of Genomes OnLine Database (GOLD): data updates and new features in v.9. *Nucleic Acids Research* 51(D1):D957–D963. doi:[10.1093/nar/gkac974](https://academic.oup.com/nar/article/51/D1/D957/6786204) · PMID 36318257 · [PMC9825498](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9825498/). *(Note: a 2024 corrigendum, doi:10.1093/nar/gkae162, adds two authors; GOLD v.10 is doi:10.1093/nar/gkae1000. Not fetched.)*
- Searles R.B. (1980) The Strategy of the Red Algal Life History. *The American Naturalist* 115(1):113–120. doi:[10.1086/283548](https://www.journals.uchicago.edu/doi/abs/10.1086/283548). Zygote retention, nurture and amplification by the gametophyte; explicit contrast drawn with Embryophyta. *(Metadata and argument verified via search; full text not fetched.)*
- Quigley C.T.C., Capistrant-Fossa K.A., Morrison H.G., Johnson L.E., Morozov A., Hertzberg V.S., Brawley S.H. (2020) Bacterial communities show algal host (*Fucus* spp.)/zone differentiation across the stress gradient of the intertidal zone. *Front. Microbiol.* 11:563118. doi:[10.3389/fmicb.2020.563118](https://pmc.ncbi.nlm.nih.gov/articles/PMC7541829/) — oogonial colonisation from parental thallus; **fetched and quote confirmed**.
- Culturable yeasts associated with different life stages of the farmed red seaweed *Porphyra dioica* (2026) *Front. Microbiol.* doi:[10.3389/fmicb.2026.1918765](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2026.1918765/full) — life-stage sampling in a red alga; carposporophyte not sampled.
- Ecological and Industrial Implications of Dynamic Seaweed-Associated Microbiota Interactions (2020) *Marine Drugs* 18:641. doi:[10.3390/md18120641](https://www.mdpi.com/1660-3397/18/12/641) — carpospore-liberation quorum sensing flagged as a knowledge gap.
- Metabolic relationships between marine red algae and algae-associated bacteria (2024) — [PMC11136935](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11136935/) · PMID [38827136](https://pubmed.ncbi.nlm.nih.gov/38827136/) — adult red algal microbiome baseline.
- Environmental factors shape the epiphytic bacterial communities of *Gracilariopsis lemaneiformis* (2021) *Sci. Rep.* doi:[10.1038/s41598-021-87977-3](https://www.nature.com/articles/s41598-021-87977-3) — adult thallus only.
- Metagenomic Insights… Microbial Diversity on the Surface of Red Algae among Remote Regions — [PMC10342065](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10342065/).
- Carposporophyte ultrastructure and nutritive/placental tissue: [*Cryptopleura ruprechtiana*, doi:10.1016/S0248-4900(03)00085-6](https://www.sciencedirect.com/science/article/abs/pii/S0248490003000856); [*Caulacanthus ustulatus*, *Mar. Biol.*, doi:10.1007/BF02114685](https://link.springer.com/article/10.1007/BF02114685).
- Ontology terms: [UBERON:0000922](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0000922), [PO:0009009](https://www.ebi.ac.uk/ols4/ontologies/po/classes?obo_id=PO:0009009), ENVO:01001000 and its four children via [OLS4](https://www.ebi.ac.uk/ols4/); BTO:0000379, BTO:0001290, FOODON:03411743, FOODON:03412266, FOODON:00001184, ENVO:01001001/01001002/01001041 read from this repo's `data/raw/ontology_terms.tsv`.
- Reference/tertiary, used only for standard terminology: [Biology LibreTexts — Phylum Rhodophyta](https://bio.libretexts.org/Bookshelves/Botany/Botany_Lab_Manual_(Morrow)/18:_Red_and_Green_Algae/18.3:_Phylum_Rhodophyta_-_The_Red_Algae); Wikipedia [Gonimoblast](https://en.wikipedia.org/wiki/Gonimoblast), [Carpogonium](https://en.wikipedia.org/wiki/Carpogonium), [Matrotrophy](https://en.wikipedia.org/wiki/Matrotrophy), [Embryophyte](https://en.wikipedia.org/wiki/Embryophyte). These are not adequate support for a definition on their own; the Searles and ultrastructure papers are.
- ENVO new-term-request procedure and the nearest precedent, [EnvironmentOntology/envo issue #1029 "EnvO terms for host-associated samples"](https://github.com/EnvironmentOntology/envo/issues/1029). I found **no** existing ENVO issue requesting an algae-associated environment term.

**Explicitly unsupported / inference, flagged:** that GOLD replicated the brown-algae subtype list onto red algae; that the cystocarp interior is a distinct microbial niche; that a sample filed here would more likely be a sporeling than a carposporophyte.

---

## 5. Synonyms, and what not to conflate

**Names in real use for the thing reading (A) denotes:** carposporophyte; gonimoblast (the filament system); cystocarp (carposporophyte + enclosing pericarp); sporocarp (legacy, cf. BTO:0001290); "the diploid generation retained on the female gametophyte".

**Names for reading (B):** germling; sporeling (GOLD's own sibling label); juvenile thallus.

**"Embryo" itself is not a synonym for either** in the phycological literature — that is the core finding of §1.

**Do not conflate with:**

| Not the same as | Why |
|---|---|
| **Brown algae embryo** (`habitatmech:GOLD.32330da5da`, `Host-associated > Algae > Brown Algae > Embryo`, 3 organisms) | Fucales *do* form a true embryo from a released zygote. That record is biologically sound; this one is not. They must not be merged. |
| **Fish embryo** (`Host-associated > Fish > Embryo`) | Same label, unrelated concept; distinct record. |
| **Red algae > Sporeling** (2 organisms) | The attested young-thallus habitat. If reading (B) is ever adopted here, these two records collide. |
| **Carpospore / tetraspore** | Single cells released from the carposporophyte, not the structure itself. |
| **Conchocelis** | The filamentous sporophyte phase of Bangiales — an independent generation, not an embryo. |
| **Plant embryo / seed** (PO:0009009) | Different clade, different structure, different ontology scope. |
| **Phycosphere** | The diffusive boundary layer around (chiefly micro-) algal cells; GOLD sites it under Diatoms. Not an embryo and not a red algal concept here. |

---

## 6. Should this be a term at all? — recommendation

**My recommendation: no new definition, and no term request. Keep `CONFIRM_UNGROUNDED`, and add to the note that the concept is unattested and biologically inapplicable.**

Three independent reasons, each sufficient on its own:

1. **Zero attestation.** No GOLD organism, study or biosample uses this path, in a classification GOLD itself describes as sample-driven. Nothing upstream vouches for this concept's existence as a sampled place.
2. **The label denotes something the host clade does not have.** Red algae do not form embryos; the word is reserved, by definition, for Embryophyta. A definition written for "red algal embryo" would be asserting a developmental stage no rhodophyte passes through.
3. **Both salvage readings are bad.** Reading (A) requires inventing a carposporophyte-habitat concept with **no** published microbiological characterisation whatsoever. Reading (B) duplicates the sibling `Sporeling` record, which has actual samples.

This is the shape of a **vocabulary placeholder / sampling artefact**, not a habitat — the category §6 of the brief invites. It is not a disease, a quality or a process, and it is *not* the "host taxon is not a habitat" case that #114 settled: a red alga acting as a host genuinely is a place. The defect is at the leaf, not at the host.

**Concretely:**
- Leave `grounding_status: UNGROUNDED`, `parent_habitats: [habitatmech:GOLD.e789c273d0]` (Red algae), `xrefs: [UBERON:0000922]` with `relation: xref` — all three are already right, and the existing note's reasoning about #99/#112/#114 holds.
- Extend the note with the substantive finding: *zero upstream assertions; "embryo" is not a developmental stage of Rhodophyta (the post-zygotic structure is the gametophyte-retained carposporophyte/cystocarp, cf. Searles 1980 doi:10.1086/283548); the node appears to mirror the Brown Algae subtype list, where the term is biologically correct; no microbiome study of any red algal carposporophyte was found.*
- **Do not** file an ENVO new-term request for this. If an NTR is ever filed out of this branch, the defensible one is a general **algae-associated environment** under `ENVO:01001000` — a real gap (ENVO has plant-, animal- and fungi-associated but nothing for algae) that would serve the 394 GOLD organisms under `Host-associated > Algae`, the 73 under `Red algae`, and the attested `Blade` / `Sporeling` / `Whole body` records. That is a far better use of a term request than this empty leaf.
- Worth a separate issue: `Brown Algae > Embryo` (`habitatmech:GOLD.32330da5da`) currently carries the **identical** boilerplate note, but its case is materially different — brown algae do form embryos, the node has 3 organisms, and there is direct evidence for parental bacterial transmission at the oogonium ([Quigley et al. 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7541829/)). One note should not stand for both records.

## Citations

1. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000
2. https://www.journals.uchicago.edu/doi/abs/10.1086/283548
3. https://en.wikipedia.org/wiki/Gonimoblast
4. https://en.wikipedia.org/wiki/Carpogonium
5. https://en.wikipedia.org/wiki/Embryophyte
6. https://en.wikipedia.org/wiki/Matrotrophy
7. https://bio.libretexts.org/Bookshelves/Botany/Botany_Lab_Manual_(Morrow
8. https://gold.jgi.doe.gov/ecosystem_classification
9. https://academic.oup.com/nar/article/51/D1/D957/6786204
10. https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000/hierarchicalChildren
11. https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0000922
12. https://www.ebi.ac.uk/ols4/ontologies/po/classes?obo_id=PO:0009009
13. https://link.springer.com/article/10.1007/BF02114685
14. https://www.mdpi.com/1660-3397/18/12/641
15. https://www.sciencedirect.com/science/article/abs/pii/S0248490003000856
16. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2026.1918765/full
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC7541829/
18. https://gold.jgi.doe.gov/ecosystemtree
19. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9825498/
20. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11136935/
21. https://pubmed.ncbi.nlm.nih.gov/38827136/
22. https://www.nature.com/articles/s41598-021-87977-3
23. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10342065/
24. https://www.ebi.ac.uk/ols4/
25. https://github.com/EnvironmentOntology/envo/issues/1029