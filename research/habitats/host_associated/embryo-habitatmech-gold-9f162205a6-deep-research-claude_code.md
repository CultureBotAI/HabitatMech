---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T04:41:26.409532'
end_time: '2026-08-18T04:50:40.889813'
duration_seconds: 554.48
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Embryo
  habitat_identifier: habitatmech:GOLD.9f162205a6
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Fish > Embryo'
  assertions: '0'
  parent_terms: (none)
  xrefs: UBERON:0000922
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term UBERON:0000922 'embryo' attached as a parent. Life-stage review\
    \ (#112), applying the rule #114 settled: the whole host ORGANISM gets its own\
    \ identity plus an <X>-associated environment term, while PARTS of a host ground\
    \ to the anatomy term as gut, skin and lung already do. A larva, pupa, prepupa\
    \ or embryo is the whole organism at a stage, not a part of one, so UBERON:0000922\
    \ 'embryo' is the organism rather than the place \u2014 the same shape as Mollusca,\
    \ Porifera and the host clades. Kept as an xref (#99); the concept keeps its own\
    \ identity as a term-request candidate.This is the line that makes both calls\
    \ fall out of one rule, rather than an exception for terms that happen to live\
    \ in UBERON: a cocoon is a STRUCTURE an insect builds and stays grounded, because\
    \ it is not the organism. (source concept habitatmech:GOLD.9f162205a6)"
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
  web_search_requests: 15
  num_turns: 34
  total_cost_usd: 3.3140989999999992
  session_id: f90e3a08-ba48-4380-a08c-bfbf1364c3e1
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 21
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Embryo
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.9f162205a6
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Fish > Embryo
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** UBERON:0000922

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term UBERON:0000922 'embryo' attached as a parent. Life-stage review (#112), applying the rule #114 settled: the whole host ORGANISM gets its own identity plus an <X>-associated environment term, while PARTS of a host ground to the anatomy term as gut, skin and lung already do. A larva, pupa, prepupa or embryo is the whole organism at a stage, not a part of one, so UBERON:0000922 'embryo' is the organism rather than the place — the same shape as Mollusca, Porifera and the host clades. Kept as an xref (#99); the concept keeps its own identity as a term-request candidate.This is the line that makes both calls fall out of one rule, rather than an exception for terms that happen to live in UBERON: a cocoon is a STRUCTURE an insect builds and stays grounded, because it is not the organism. (source concept habitatmech:GOLD.9f162205a6)

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

# Research report — GOLD "Embryo" under *Host-associated > Fish*

**Concept:** `habitatmech:GOLD.9f162205a6` · label **Embryo** · category HOST_ASSOCIATED · UNGROUNDED
**Source path:** `Host-associated > Fish > Embryo` (GOLD ecosystem ids 7578, 7579, 7581; upstream assertion volume **0**)

---

## Proposed definition

> An animal-associated environment which is determined by a fish between fertilization and hatching, bounded by the chorion and comprising the chorion surface, the enclosed perivitelline fluid, and the embryo's own tissues.

If a curator judges that one sentence over-reaches by naming three compartments, the honest reading is that an intermediate class is missing: the corpus has no *"organism at a developmental stage as an environment"* class, and the same gap is visible in the sibling `larva`, `pupa`, `prepupa` and algal `Embryo` records. Saying so is more useful than lengthening the sentence.

---

## 1. What the concept denotes

**As a habitat, this is the fertilized fish egg during development — a discrete, chorion-bounded, millimetre-scale object that is picked out of the water or the incubation tray and extracted whole.** Nearly every study in this literature homogenises or swabs the *whole egg*, not a dissected embryo: Nikouli et al. sampled "whole-body microbiota from fertilized eggs at day 0 … due to the small size of the larvae" ([*Genes* 2019, 10:483](https://doi.org/10.3390/genes10070483)); Wilkins et al. pooled eight whole late-eyed brown trout embryos per site ([*Sci Rep* 2015, 5:17084](https://doi.org/10.1038/srep17084)); Lokesh et al. sequenced "eyed egg, embryo, and hatchling" stages as whole units ([*MicrobiologyOpen* 2019, 8:e672](https://doi.org/10.1002/mbo3.672)).

**Internal structure the definition has to respect.** The object has three nested compartments, and the microbes are not evenly distributed across them:

1. **The chorion (outer egg envelope, UBERON:0000920 'egg chorion')** — where essentially all of the detected community sits. It is an acellular, three-layered envelope pierced by pore canals reported at ~0.2 µm in unfertilized eggs and ~0.5–0.7 µm in fertilized eggs, dimensions at or below the diameter of most bacteria (Rawson et al. 2000, *Aquaculture Research* 31:325–336; reviewed in [*Aquaculture and Fisheries*/Elsevier chorion review, 2023](https://www.sciencedirect.com/science/article/pii/S2352513423001291)).
2. **The perivitelline space and its fluid** — formed at egg activation by the cortical reaction; not a passive buffer but a maternally-loaded innate-immune compartment carrying lectins, α-2-macroglobulin protease inhibitors, transferrin and chitinases, with demonstrated agglutinating activity against *E. coli* and *S. typhimurium* and protective activity against *Edwardsiella tarda* ([De la Paz et al., *Biomolecules* 2020, 10:1274](https://doi.org/10.3390/biom10091274)).
3. **The embryo proper** — normally microbe-free, but *demonstrably colonizable*. *Flavobacterium psychrophilum* enters through the micropyle during water hardening and multiplies in the perivitelline space from <10 CFU/egg to >10⁷ CFU/egg by the eyed stage, without killing the egg (Kumagai & Nawata 2010, *Fish Pathology* 45:31–36; [Kohara, Kasai & Yoshimizu 2012, *Fish Pathology* 47:49–55](https://www.jstage.jst.go.jp/article/jsfp/47/2/47_49/_article)). This is why the "sterile interior" framing must not be written into the definition as a claim.

**The label is mildly ambiguous and the ambiguity should be recorded, not resolved silently.** Two readings:

- **(a) The whole developing egg** — chorion + perivitelline fluid + embryo. This is what the sampling practice in the literature delivers, and it is the reading I recommend.
- **(b) The embryo body only**, strictly excluding its envelopes (the UBERON:0000922 reading).

The GOLD path is weak evidence between the two — it says only "Fish > Embryo" — but the **sibling paths are strong evidence about the outer boundary**. GOLD separately carries `Host-associated > Fish > Reproductive system > Ovaries > Eggs` (habitatmech `GOLD.1f110436d1`, also UNGROUNDED). That path is the *unfertilized* egg inside the mother; "Embryo" is therefore the post-fertilization, externally incubated object. Adopting reading (a) does not collide with any other GOLD path.

**Neighbouring concepts, explicitly outside:**

| Outside the concept | Why |
|---|---|
| `Host-associated > Fish > Reproductive system > Ovaries > Eggs` | Pre-fertilization, intra-maternal; a separate GOLD path and a separate HabitatMech record |
| Larvae / fry after hatching | Different life stage; the chorion barrier is gone and the gut opens to the environment ([Llewellyn et al., *Front. Microbiol.* 2014, 5:207](https://doi.org/10.3389/fmicb.2014.00207)) |
| Incubation / hatchery water | An aquatic environment; ENVO:00000295 'fish hatchery' names the *facility*, not the egg |
| Ovarian fluid and milt | Maternal/paternal fluids that act as an inoculum source ([Long et al., *J. Aquat. Anim. Health* 2014, 26:66](https://doi.org/10.1080/08997659.2014.886632)) |
| Roe / caviar | Food-role concept (FOODON:00001250 'fish egg food product') |
| GOLD `Algae > Brown/Red algae > Embryo` (`GOLD.32330da5da`, `GOLD.b648ad12d6`) | Same label, non-metazoan; not the same concept |

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001002` 'animal-associated environment'** — "An environmental system determined by an animal." A fish embryo is an animal; the class fits without asserting anything the sources do not support. *(Term text verified 2026-08-18 via the OLS4 API against the current ENVO release.)*

**There is no ENVO term for this concept.** I queried ENVO through OLS4 for `egg`, `embryo`, `larva`, `fish`, `fish-associated`, `vertebrate-associated` and `host-associated environment` over labels and synonyms. ENVO's fish-related terms are all built environments or gear (`ENVO:00000295` fish hatchery, `ENVO:00000294` fish farm, `ENVO:00000056` fishpond, the fishing-gear branch); there is **no** egg-, embryo-, larva- or fish-associated *environment* class. The children of ENVO:01001002 are only `ENVO:01001176` (aquatic invertebrate), `ENVO:01001179` (cnidarian-associated) and `ENVO:01001829` (human settlement). This confirms the UNGROUNDED status independently of the vendored slice.

**Near-misses, and why each fails:**

| Candidate | Verdict |
|---|---|
| `ENVO:01001002` animal-associated environment | **Genus, not identity.** Correct kind, far broader — covers any animal at any stage |
| `ENVO:01001055` environment associated with an animal part or small animal | Plausible parent, but the label disjoins "part of an animal" from "whole small animal"; grounding here risks publishing the part-hood reading that #114 and #112 were about. Its actual children (aquatic invertebrate, human settlement) show the class is not being used as an embryo-scale bucket |
| `ENVO:01001034` environment determined by a biofilm on an animal surface | **Narrower** and asserts more than the sources do. Egg-surface communities are usually characterised as microbiota, not demonstrated biofilms; and this excludes the perivitelline compartment |
| `UBERON:0000922` embryo | **The organism, not the place** — "Anatomical entity that comprises the organism in the early stages of growth and differentiation." Exactly the case the curator's note settles: keep as `relation: xref` |
| `UBERON:0000920` egg chorion | **Narrower** — one membrane of the object, even though it carries most of the community. Grounding the whole to the envelope loses the perivitelline and embryonic compartments |
| `UBERON:0000323` late embryo | Narrower still, and a stage subdivision GOLD does not make |
| `ENVO:00000295` fish hatchery | Asserts an **artificial facility**; wild-spawned eggs are a major part of this literature (Wilkins et al. sampled nine natural spawning sites) |
| `FOODON:00001250` fish egg food product | Asserts a **food role** the source path never claims |

---

## 3. Differentia — what distinguishes it from siblings under 'animal-associated environment'

Ranked by how observable each is:

1. **Life-stage bound, with hard temporal endpoints.** Begins at fertilization/water hardening, ends at hatching — days to months depending on species and temperature. Both endpoints are visible events, unlike most host-associated habitats.
2. **A size-selective physical envelope.** Chorion pore canals ~0.5–0.7 µm at gastrula stage (Rawson et al. 2000) partition the habitat into a densely colonised exterior and a normally uncolonised interior — the single most distinctive physical property, and one no other fish body-site habitat has.
3. **A chemically defended interior.** Perivitelline fluid carries ~85 constitutive maternal proteins including lectins, protease inhibitors, transferrin and chitinases, active at 10% dilution in agglutination assays ([De la Paz et al. 2020](https://doi.org/10.3390/biom10091274)). Rainbow trout embryos also express lysozyme autologously within the first days post-fertilization ([Auclert, Chhanda & Derome, *PeerJ* 2024, 12:e17051](https://doi.org/10.7717/peerj.17051)).
4. **A characteristic and reproducible community.** Pseudomonadota/Proteobacteria dominate everywhere; the sub-dominant signal splits by salinity —
 - *Freshwater/salmonid:* Pseudomonadota 83%, Bacteroidota 14%; top genera *Acinetobacter*, *Janthinobacterium*, *Pseudomonas*, *Flavobacterium*, Comamonadaceae, *Undibacterium*; mean Shannon 4.52, mean 102 observed ASVs ([Pavić et al., *Microorganisms* 2024, 12:1733](https://doi.org/10.3390/microorganisms12081733)). Brown trout embryos: Flavobacteriaceae, Comamonadaceae, Moraxellaceae, Enterobacteriaceae, Oxalobacteraceae ([Wilkins et al. 2015](https://doi.org/10.1038/srep17084)).
 - *Marine hatchery:* Proteobacteria 49.7% mean, *Vibrio* 7.1%, then *Glaciecola*, *Pseudoalteromonas*, *Colwellia* ([Najafpour et al., *Microorganisms* 2021, 9:2275](https://doi.org/10.3390/microorganisms9112275)); gilthead seabream eggs 59.2% Proteobacteria / 13.7% Bacteroidetes ([Nikouli et al. 2019](https://doi.org/10.3390/genes10070483)).
5. **Partly autochthonous, not merely a water film.** 34.5% of egg-associated bacterial representatives were not shared with the rearing water ([Nikouli et al. 2019](https://doi.org/10.3390/genes10070483)) — the authors themselves flag this as needing confirmation, since rare seawater taxa could account for part of it.
6. **A directional successional trajectory.** Egg-stage richness is the highest of the early stages in seabream (217 ± 87.5 observed OTUs, Chao1 260 ± 104.4, Shannon 3.46 ± 0.71) and declines thereafter ([Nikouli et al. 2019](https://doi.org/10.3390/genes10070483)); diversity declines across development in naturally spawned whitefish ([Wilkins et al., *Aquatic Sciences* 2015](https://doi.org/10.1007/s00027-015-0392-9)). Atlantic salmon embryos show *lower* richness than hatchlings, so the direction is not universal ([Lokesh et al. 2019](https://doi.org/10.1002/mbo3.672)) — do not write a monotonic trend into the definition.
7. **Cold, oxygenated, temperature-responsive.** Brown trout embryos incubate at ~2.0–5.8 °C mean, and bacterial alpha diversity rises significantly with incubation temperature across all three diversity measures, independent of geographic distance and host genetics ([Wilkins et al. 2015](https://doi.org/10.1038/srep17084)).
8. **A distinctive antagonist set.** Oomycete pathogenesis (*Saprolegnia parasitica*) is a defining pressure on this habitat and restructures the surface community, lowering evenness and Shannon diversity ([Pavić et al. 2024](https://doi.org/10.3390/microorganisms12081733)); the fungal/eukaryotic dimension is separately profiled in Atlantic salmon eggs ([*Sci Rep* 2024, 14:1543](https://doi.org/10.1038/s41598-023-50883-x)).

**Inference flags.** The three-compartment framing in §1, and the claim that this compartmentalisation is the *primary* differentia, are my synthesis across the sources cited — no single source states it that way. The pore-diameter-versus-cell-diameter comparison is likewise my inference from the two measured quantities.

---

## 4. Sources

Primary literature:

- Nikouli E. et al. (2019) Host-Associated Bacterial Succession during the Early Embryonic Stages and First Feeding in Farmed Gilthead Sea Bream. *Genes* 10(7):483. https://doi.org/10.3390/genes10070483
- Wilkins L.G.E., Rogivue A., Schütz F., Fumagalli L., Wedekind C. (2015) Increased diversity of egg-associated bacteria on brown trout at elevated temperatures. *Sci Rep* 5:17084. https://doi.org/10.1038/srep17084
- Wilkins L.G.E. et al. (2015) Declining diversity of egg-associated bacteria during development of naturally spawned whitefish embryos (*Coregonus* spp.). *Aquatic Sciences*. https://doi.org/10.1007/s00027-015-0392-9
- Pavić D., Geček S., Miljanović A., Grbin D., Bielen A. (2024) Characterization of Bacterial Communities on Trout Skin and Eggs in Relation to *Saprolegnia parasitica* Infection Status. *Microorganisms* 12(8):1733. https://doi.org/10.3390/microorganisms12081733
- Najafpour B. et al. (2021) Factors Driving Bacterial Microbiota of Eggs from Commercial Hatcheries of European Seabass and Gilthead Seabream. *Microorganisms* 9(11):2275. https://doi.org/10.3390/microorganisms9112275
- Lokesh J., Kiron V., Sipkema D., Fernandes J.M.O., Moum T. (2019) Succession of embryonic and the intestinal bacterial communities of Atlantic salmon reveals stage-specific microbial signatures. *MicrobiologyOpen* 8:e672. https://doi.org/10.1002/mbo3.672
- De la Paz J.F., Anguita-Salinas C., Díaz-Celis C., Chávez F.P., Allende M.L. (2020) The Zebrafish Perivitelline Fluid Provides Maternally-Inherited Defensive Immunity. *Biomolecules* 10(9):1274. https://doi.org/10.3390/biom10091274
- Kumagai A., Nawata A. (2010) Mode of the intra-ovum infection of *Flavobacterium psychrophilum* in salmonid eggs. *Fish Pathology* 45:31–36. https://www.jstage.jst.go.jp/article/jsfp/45/1/45_1_31/_article
- Kohara M., Kasai H., Yoshimizu M. (2012) Intra-ovum Infection in Salmonid Eggs Artificially Contaminated with Fish Pathogenic Bacteria. *Fish Pathology* 47(2):49–55. https://www.jstage.jst.go.jp/article/jsfp/47/2/47_49/_article
- Long A. et al. (2014) Investigation of the Link between Broodstock Infection, Vertical Transmission, and Prevalence of *F. psychrophilum*. *J. Aquat. Anim. Health* 26(2):66. https://doi.org/10.1080/08997659.2014.886632
- Vestrum R./Rud I. et al. (2024) Unravelling the temporal and spatial variation of fungal phylotypes from embryo to adult stages in Atlantic salmon. *Sci Rep* 14:1543. https://doi.org/10.1038/s41598-023-50883-x

Reviews and syntheses:

- Auclert L.Z., Chhanda M.S., Derome N. (2024) Interwoven processes in fish development: microbial community succession and immune maturation. *PeerJ* 12:e17051. https://doi.org/10.7717/peerj.17051
- Llewellyn M.S. et al. (2014) Teleost microbiomes: the state of the art. *Front. Microbiol.* 5:207. https://doi.org/10.3389/fmicb.2014.00207
- Mueller R.S. et al. (2021) Developing Inside a Layer of Germs — A Potential Role for Multiciliated Surface Cells in Vertebrate Embryos. *Diversity* 13(11):527. https://doi.org/10.3390/d13110527
- Chorion in fish: synthesis, functions and factors associated with its malformations (2023), *Aquaculture and Fisheries*. https://www.sciencedirect.com/science/article/pii/S2352513423001291

Standards and vocabularies:

- GOLD Ecosystem Classification (five-level scheme; sample-driven, not exhaustive). https://gold.jgi.doe.gov/ecosystem_classification
- GSC MIxS host-associated extension (0016002) — `host_life_stage` and `host_body_site` are **separate slots**; `host_body_site` is the UBERON/FMA-typed one. https://genomicsstandardsconsortium.github.io/mixs/0016002/
- ENVO via OLS4 (queried 2026-08-18): ENVO:01001002, ENVO:01001055, ENVO:01001034; UBERON:0000922, UBERON:0000920. https://www.ebi.ac.uk/ols4

**Not read, listed for the curator:** Liu Y. et al. (2014) *Deciphering microbial landscapes of fish eggs to mitigate emerging diseases*, *ISME J* — https://doi.org/10.1038/ismej.2014.44 (paywalled at fetch time). The bioRxiv preprint *The External Microbiome Communicates with the Developing Zebrafish Embryo Through the Chorion* (https://doi.org/10.1101/2024.05.28.596134) is **not peer-reviewed**; its claim that the external microbiome influences embryos across an intact chorion is interesting but should not be cited in a definition.

---

## 5. Synonyms and what not to conflate

**Names in real use for this concept:** fish egg microbiota / fish egg microbiome; egg-associated microbial community; egg-surface microbiota; chorion-associated microbiota; fertilized fish egg; developing fish egg; eyed egg / eyed-stage egg (a developmental substage, salmonid usage); embryonated egg; *in ovo* (as a location qualifier); "embryonic stage" whole-body sample.

**Commonly conflated but distinct:**

- **Unfertilized / ovarian eggs** — pre-fertilization, inside the female; GOLD gives these their own path. The community source there is ovarian fluid, not incubation water.
- **Roe, caviar, fish egg food product** (FOODON:00001250) — food role; a different concept even though the physical material overlaps.
- **Larva, fry, yolk-sac larva** — post-hatch; the barrier and the successional regime both change at hatching.
- **The chorion alone** (UBERON:0000920) — where the microbes are, but not the whole habitat.
- **Incubation/hatchery water and the tray or hatchery** (ENVO:00000295) — the surrounding environment; the main horizontal inoculum source, and precisely what the 34.5%-unshared figure is contrasted against.
- **Ovarian fluid / milt** — the vertical inoculum vehicle, not the habitat.
- **UBERON:0000922 'embryo'** — the organism. Also note UBERON's definition is cross-kingdom (it explicitly covers plant zygotic and vegetative embryos), so it is not even specific to the animal reading.
- **Amniote embryo / avian egg** — the "sterile egg" debate in birds is a *parallel*, not the same habitat ([Nearly (?) sterile avian egg in a passerine bird, *FEMS Microbiol Ecol* 2024](https://academic.oup.com/femsec/article/100/1/fiad164/7480268)).
- **Algal "Embryo"** (`GOLD.32330da5da`, `GOLD.b648ad12d6`) — homonym under a different kingdom.
- **Germ-free / gnotobiotic zebrafish embryos** — a laboratory-derived state (gentamicin + hypochlorite protocols), not this habitat. Any sample so labelled is an experimental artefact relative to this concept.

---

## 6. Should this be a term at all?

**Yes — this is a genuine habitat, and it is a good term-request candidate.** It names a physical, bounded, sampleable place that microorganisms demonstrably occupy, with a decade of primary literature characterising its community, its physicochemistry, its succession and its pathogens. It is not a process, quality, disease state, or bare taxonomic grouping, so `NOT_APPLICABLE` would be the wrong disposition.

The curator's existing note is right on the ontology question and I found no evidence against it: UBERON:0000922 is the *organism at a stage*, ENVO has no egg-, embryo- or fish-associated environment class, and the correct shape is HabitatMech's own identity plus an `<X>-associated environment` term request. The MIxS extension corroborates the split independently — `host_life_stage` and `host_body_site` are separate slots, and only the latter takes a UBERON anatomy term ([GSC MIxS 0016002](https://genomicsstandardsconsortium.github.io/mixs/0016002/)). "Embryo" is a `host_life_stage` value, not a `host_body_site` value.

**Suggested term request to ENVO:** *fish embryo-associated environment*, `is_a` ENVO:01001002 'animal-associated environment'. A general *embryo-associated environment* parent would let the algal `Embryo` records, `larva`, `pupa` and `prepupa` all hang from one place, but ENVO's animal-associated branch is currently thin (three children) and the general parent would cross kingdoms, so I would request the specific term and mention the general one in the issue rather than betting the request on it.

**Two caveats the curator should weigh before filing:**

1. **Assertion volume is 0.** GOLD carries the path (three ecosystem ids) but no organisms or biosamples reach it in `data/raw/`. This is a vocabulary-level concept with no data behind it *in this corpus* — the justification for a term rests on the external literature, not on attestation volume. That is a legitimate basis, but it should be stated in the request rather than implied.
2. **The reading must be fixed before the definition is written.** Whole egg (recommended) versus embryo body only changes what the differentia can say. If a future curator prefers the narrow reading, the chorion and perivitelline clauses have to come out, and the concept becomes almost unsampleable in practice — which is itself the argument for the whole-egg reading.

Recommended xrefs on the record: `UBERON:0000922` (embryo — the organism, already present) and optionally `UBERON:0000920` (egg chorion — the compartment carrying the community). Neither is a parent.

Sources: [Genes 2019](https://doi.org/10.3390/genes10070483) · [Sci Rep 2015](https://doi.org/10.1038/srep17084) · [Aquatic Sciences 2015](https://doi.org/10.1007/s00027-015-0392-9) · [Microorganisms 2024](https://doi.org/10.3390/microorganisms12081733) · [Microorganisms 2021](https://doi.org/10.3390/microorganisms9112275) · [MicrobiologyOpen 2019](https://doi.org/10.1002/mbo3.672) · [Biomolecules 2020](https://doi.org/10.3390/biom10091274) · [Fish Pathology 45:31](https://www.jstage.jst.go.jp/article/jsfp/45/1/45_1_31/_article) · [Fish Pathology 47:49](https://www.jstage.jst.go.jp/article/jsfp/47/2/47_49/_article) · [J Aquat Anim Health 2014](https://doi.org/10.1080/08997659.2014.886632) · [Sci Rep 2024 mycobiome](https://doi.org/10.1038/s41598-023-50883-x) · [PeerJ 2024](https://doi.org/10.7717/peerj.17051) · [Front Microbiol 2014](https://doi.org/10.3389/fmicb.2014.00207) · [Diversity 2021](https://doi.org/10.3390/d13110527) · [Chorion review 2023](https://www.sciencedirect.com/science/article/pii/S2352513423001291) · [FEMS Microbiol Ecol 2024](https://academic.oup.com/femsec/article/100/1/fiad164/7480268) · [ISME J 2014](https://doi.org/10.1038/ismej.2014.44) · [bioRxiv 2024 preprint](https://doi.org/10.1101/2024.05.28.596134) · [GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification) · [MIxS host-associated extension](https://genomicsstandardsconsortium.github.io/mixs/0016002/) · [OLS4](https://www.ebi.ac.uk/ols4)

## Citations

1. https://doi.org/10.3390/genes10070483
2. https://doi.org/10.1038/srep17084
3. https://doi.org/10.1002/mbo3.672
4. https://www.sciencedirect.com/science/article/pii/S2352513423001291
5. https://doi.org/10.3390/biom10091274
6. https://www.jstage.jst.go.jp/article/jsfp/47/2/47_49/_article
7. https://doi.org/10.3389/fmicb.2014.00207
8. https://doi.org/10.1080/08997659.2014.886632
9. https://doi.org/10.7717/peerj.17051
10. https://doi.org/10.3390/microorganisms12081733
11. https://doi.org/10.3390/microorganisms9112275
12. https://doi.org/10.1007/s00027-015-0392-9
13. https://doi.org/10.1038/s41598-023-50883-x
14. https://www.jstage.jst.go.jp/article/jsfp/45/1/45_1_31/_article
15. https://doi.org/10.3390/d13110527
16. https://gold.jgi.doe.gov/ecosystem_classification
17. https://genomicsstandardsconsortium.github.io/mixs/0016002/
18. https://www.ebi.ac.uk/ols4
19. https://doi.org/10.1038/ismej.2014.44
20. https://doi.org/10.1101/2024.05.28.596134
21. https://academic.oup.com/femsec/article/100/1/fiad164/7480268