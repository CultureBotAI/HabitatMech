---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T03:36:37.383856'
end_time: '2026-08-18T03:44:47.259816'
duration_seconds: 489.88
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: 'Larva: Zoea'
  habitat_identifier: habitatmech:GOLD.8b6557e4f2
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Arthropoda: Crustaceans > Larva: Zoea'
  assertions: '0'
  parent_terms: (none)
  xrefs: UBERON:0002548
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term UBERON:0002548 'larva' attached as a parent. Life-stage review\
    \ (#112): carried UBERON:0002548 'larva' as a parent, reached by the ambiguous-leaf\
    \ rule rather than the path \u2014 several GOLD paths end in the same leaf, so\
    \ the ones that do not claim the term keep it as a parent. parent_habitats asserts\
    \ the parent is BROADER, and a larva or embryo is a whole organism rather than\
    \ a broader kind of place, so this is the same over-claim the identity cases had\
    \ one level up. Kept as an xref (#99). Per the rule #114 settled: the whole host\
    \ organism gets its own identity and an <X>-associated environment term; parts\
    \ of a host ground to the anatomy term. (source concept habitatmech:GOLD.8b6557e4f2)"
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
  web_search_requests: 6
  num_turns: 38
  total_cost_usd: 2.4518649999999993
  session_id: a77319b8-7ba0-48e8-b182-020c395b5f1e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 20
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Larva: Zoea
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.8b6557e4f2
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Arthropoda: Crustaceans > Larva: Zoea
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** UBERON:0002548

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term UBERON:0002548 'larva' attached as a parent. Life-stage review (#112): carried UBERON:0002548 'larva' as a parent, reached by the ambiguous-leaf rule rather than the path — several GOLD paths end in the same leaf, so the ones that do not claim the term keep it as a parent. parent_habitats asserts the parent is BROADER, and a larva or embryo is a whole organism rather than a broader kind of place, so this is the same over-claim the identity cases had one level up. Kept as an xref (#99). Per the rule #114 settled: the whole host organism gets its own identity and an <X>-associated environment term; parts of a host ground to the anatomy term. (source concept habitatmech:GOLD.8b6557e4f2)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Larva: Zoea** as a microbial habitat, with citations.

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

# Definition research: *Larva: Zoea* (`habitatmech:GOLD.8b6557e4f2`)

> **Proposed definition:** An environment associated with an aquatic invertebrate which is determined by a whole decapod crustacean larva at a zoeal stage — the free-swimming, particle-feeding planktonic stage that swims with its thoracic appendages, after mouth opening and before the post-larval stage.

Genus: **ENVO:01001176** *environment associated with an aquatic invertebrate*. If the curator prefers to stay one level up, **ENVO:01001055** *environment associated with an animal part or small animal* also holds. Both are honest; neither is an identity match, so the record stays `UNGROUNDED` with these as `relation: xref` or as the term-request parent.

**Caveat worth recording before anything else:** the definition above compresses two missing intermediate classes. ENVO has *no* arthropod-, crustacean-, or larva-associated environment term (verified below), so the jump from "aquatic invertebrate" to "zoea" skips at least *crustacean-associated environment* and *larval-crustacean-associated environment*. If this concept is ever submitted to ENVO, the higher-yield request is the intermediate class, not the leaf.

---

## 1. What the concept denotes

**The physical thing sampled:** a pooled mass of whole, live crustacean larvae at a zoeal stage — typically hundreds to thousands of ~1–3 mm animals, netted from a hatchery tank or plankton tow, rinsed, and pelleted for DNA extraction. The habitat is therefore the *whole larval body* as a compound microbial surface-plus-lumen: the chitinous, setose, spiny exoskeleton with its attached epibiotic film; the open digestive tract with ingested microalgae/*Artemia* and their associated bacteria; and the internal tissues and haemocoel that a whole-body homogenate cannot separate from the rest.

This is not a reconstruction of what curators *think* is sampled — it is what the methods sections say. In the reference *Penaeus vannamei* larval time series, larvae were "soaked and washed for 10–15 s with sterilized water to remove the adsorbed rearing water," transferred to sterile tubes, centrifuged, and the whole-larval pellet (~0.8 g per pond) sequenced without gut dissection ([Wang et al. 2020, *Microbiome* 8:106, doi:10.1186/s40168-020-00879-w](https://doi.org/10.1186/s40168-020-00879-w)). Disease-signature studies of hatchery larvae likewise sequence whole larvae ([Reyes et al. 2023, *PeerJ* 11:e15795, doi:10.7717/peerj.15795](https://doi.org/10.7717/peerj.15795)).

**Boundary — what is inside:**
- the larval cuticle and its epibionts (filamentous bacteria, attached rod-formers, diatoms);
- the larval gut lumen and its transient food-borne community, from mouth opening onward;
- larval internal tissues and haemolymph as they occur in a whole-body prep.

**Boundary — what is a neighbouring concept, not this one:**
- **The rearing water.** GOLD models it separately, under `Engineered > Artificial ecosystem > Aquaculture > Crustaceans tank / pond / raceway` (and `> Sediment`). Every study cited here sequences water as a *separate* sample type precisely because it is a different community; the larva is a selective filter on it, not a sample of it (Wang et al. 2020).
- **`Host-associated > Arthropoda: Crustaceans > Larva: Zoea > Whole body`** — GOLD's own child path (gold.ecosystem:7356, 7357). In practice this child and the parent denote the same material; the parent exists because GOLD's path grammar allows a stage node to be terminal. Flag this as a merge candidate rather than a genuinely distinct habitat.
- **Dissected larval organs.** GOLD carries `Larva > Gut` (gold.ecosystem:7811, 7812) as an explicit alternative; a dissected zoeal gut belongs there and grounds to the anatomy term under the repo's part/whole rule.
- **The adult or juvenile crustacean**, and the sibling stages `Larva: Nauplius` and `Post-larva`.

**Ambiguity — two readings, and it matters:**

1. **Whole-organism reading (the one the data means):** the larva itself is the habitat. Supported by the path being under `Host-associated`, by the sibling anatomical branches (`Digestive system`, `Integumentary system`, `Whole body`), and by the `> Whole body` child.
2. **Temporal reading:** "the zoea stage" as a window of time in a production cycle, during which *some* sample (water, feed, biofloc) was taken. This is what UBERON's `zoea stage` class actually denotes, and it is *not* a habitat. GOLD's placement rules this reading out for this record.

**A second, taxonomic ambiguity that is not resolved by the path.** "Zoea" is not used identically across decapods. In brachyuran crabs the sequence is egg → zoea (I–n) → megalopa; in penaeid shrimp it is nauplius → **protozoea** (widely written "zoea") → mysis → postlarva. GOLD's crustacean branch contains `Larva: Nauplius`, `Larva: Zoea`, and `Post-larva` but **no** `Mysis` and **no** `Megalopa` (full path list verified in `data/raw/gold_ecosystem_paths.tsv`). *Inference, not a sourced claim:* submitters working on penaeid shrimp will therefore have filed mysis-stage larvae under either `Larva: Zoea` or `Post-larva`, so the concept's extension in the data is probably "feeding decapod larva between nauplius and postlarva," slightly broader than a strict brachyuran zoea. The definition should not assert a stage count.

---

## 2. Genus — the broader kind

### The recommended genus

| CURIE | Label | ENVO definition | Fit |
|---|---|---|---|
| **ENVO:01001176** | environment associated with an aquatic invertebrate | "An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system." *(typo is ENVO's)* | **Best available.** A zoea is a marine/estuarine metazoan without a vertebral column. Broader than the concept by several levels. |

Its parent is **ENVO:01001002** *animal-associated environment* ("An environmental system determined by an animal."), and its established sibling pattern is **ENVO:01001179** *cnidarian-associated environment* ("An environmental system determined by a cnidarian or part of a cnidarian.") — which is the naming and definition template a future `crustacean-associated environment` request should follow. (Hierarchy verified via OLS4: `https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/…ENVO_01001002/hierarchicalChildren`.)

### Near-misses, and why each fails

| CURIE / term | Why it is not a match |
|---|---|
| **ENVO:01001055** *environment associated with an animal part or small animal* | Genuinely covers the concept — a zoea is a whole small animal — but it deliberately lumps animal *parts* with whole small animals, so adopting it as identity would erase the part/whole distinction this repo spent #112/#114 establishing. Usable as the fallback genus; not an identity. |
| **ENVO:01001002** *animal-associated environment* | Correct but far too broad; every host-associated record in the corpus falls under it. |
| **UBERON:0002548** *larva* | **An organism, not a place.** OLS4 gives its only hierarchical parent as **UBERON:0000468** *multicellular organism*, and its definition is "A distinct juvenile form many animals undergo before metamorphosis into adults." "zoea" is listed among its 16 synonyms as a **narrow** synonym — i.e. UBERON itself records that *larva* is broader than *zoea*, so it is not an identity match even setting the organism/place problem aside. The existing curation note is correct to keep it as an xref. |
| **UBERON:0014857** *zoea stage* | **The closest term in any ontology to this label** — "A crustacean larval stage characterised by the use of the thoracic appendages for swimming." But it is a *life cycle stage*: a temporal region, not a material entity and not an environment. Grounding a habitat to it would assert that a span of time is a place. **Recommendation: add it as a second `relation: xref`** — it names exactly this concept, more precisely than the currently-attached UBERON:0002548, and it supplies the differentia clause of the definition verbatim. |
| **UBERON:0018378** *crustacean larval stage* | "The larval stage of a crustacean, typically proceeding through nauplius-zoea-post-larval phases." Same category problem (a stage), and broader — it is the parent covering the nauplius and post-larva siblings too. Useful as evidence that GOLD's three sibling nodes mirror a recognised developmental series. |
| **ENVO:03600074** *aquaculture farm*, **ENVO:00000294** *fish farm* | Describe the rearing facility, i.e. the neighbouring `Engineered > Aquaculture` branch, not the larva. |
| **ENVO:01001249** *crustacean farming process*, **ENVO:01001254** *animal aquaculture process* | Processes. A process is not a habitat — same disposition as the `PATO:0001429` case in CLAUDE.md. |

### Verified absences

Searches of ENVO via OLS4 returned **no** term for `arthropod`, `crustacean-associated environment`, `insect-associated environment`, `larva`, `larval habitat`, or `zooplankton`. The only ENVO hits for "arthropod" are an NCBITaxon and a UBERON cross-listing; the only ENVO hit for "larva" is UBERON:0000922 *embryo*, matched on incidental definition text. There is no open ENVO new-term request for larva- or invertebrate-associated environments that I could find; the nearest is [ENVO issue #1029, "EnvO terms for host-associated samples"](https://github.com/EnvironmentOntology/envo/issues/1029), which proposes host-/animal-/plant-associated *biome* terms. So the gap is real, not a search artefact.

---

## 3. Differentia — what distinguishes it from its siblings

The siblings under `Host-associated > Arthropoda: Crustaceans` that share the whole-organism reading are `Larva` (unqualified), `Larva: Nauplius`, `Post-larva`, and `Whole body` (the adult). Observable properties that separate the zoea:

**a. The gut is open and loaded — this is the single sharpest differentia against the nauplius.** The nauplius is lecithotrophic and non-feeding; mouth opening occurs at the transition into the zoea, converting a closed animal into one with a through-flowing lumen carrying microalgae, *Artemia*, and their bacteria. Wang et al. (2020) treat mouth opening as the microbial-ecology inflection point of the whole larval cycle and show that Rhodobacteraceae rise sharply *after* it, reaching **72.4 % of the community at the zoea stage** and 84.9 % by mysis ([doi:10.1186/s40168-020-00879-w](https://doi.org/10.1186/s40168-020-00879-w)).

**b. Alpha diversity is at its cycle minimum.** Bacterial diversity follows a U-shaped curve across the larval cycle, dropping sharply at Zoea I relative to the nauplius and staying low through Zoea III — the zoea and mysis stages are the valley (Wang et al. 2020). The same collapse is reported independently in swimming crab *Portunus trituberculatus*: α-diversity decreases through development, with a large Rhodobacteraceae increase at the last zoeal stage ([Lu et al. 2022, *Aquaculture* 548:737600, doi:10.1016/j.aquaculture.2021.737600](https://doi.org/10.1016/j.aquaculture.2021.737600)).

**c. The host actively selects from the surrounding bacterioplankton.** Neutral-model fitting shows rearing water is a major source of the zoeal community, but specific Rhodobacteraceae taxa are positively selected by the host out of that water during the zoea stage (Wang et al. 2020). This is the property that makes the larva a *habitat* rather than a passive sample of the tank: it is a filter with its own selection regime.

**d. Timing and duration are short and measurable.** In *P. vannamei*, the zoeal stages Z-I to Z-III span roughly days 2–8 of a ~15-day larval cycle (Wang et al. 2020). In *P. trituberculatus*, the four zoeal instars run Z1→Z2 in 2–3 d, Z2→Z3 in 2–3 d, Z3→Z4 in 3–4 d, and Z4→megalopa in 4–5 d (Lu et al. 2022). *Inference:* a moult every 2–3 days periodically sheds the cuticle and with it the epibiotic film, so the surface habitat is repeatedly reset on a timescale shorter than the stage itself — a property no adult-crustacean habitat shares to the same degree.

**e. The exterior is a small, spiny, setose chitinous surface held in the plankton.** The zoea is defined morphologically by a prominent cephalothorax, prominent eyes, frequently elaborate carapace and rostral spines, and locomotion by the **thoracic** appendages — the diagnostic that separates it from post-larval stages, which swim with the abdominal appendages ([Britannica, "zoea"](https://www.britannica.com/science/zoea); the swimming criterion is also UBERON:0014857's definition; morphological character sets in e.g. [Di Muzio et al. 2019, *Sci Rep*, PMC6910961](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6910961/) and [Yang et al., PMC8195950](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8195950/)). Chitinous crustacean exteriors are a well-established attachment substrate for marine bacteria including *Vibrio* — demonstrated for planktonic copepods by [Huq et al. 1983, *Appl Environ Microbiol* 45:275–283, doi:10.1128/aem.45.1.275-283.1983](https://doi.org/10.1128/aem.45.1.275-283.1983). *Flag: the Huq work is on copepods, not zoeae; cite it as the general chitin-surface mechanism, not as evidence about zoeae.*

**f. Filamentous epibiont fouling is a characteristic, documented condition of this surface.** *Leucothrix mucor*-like filamentous bacteria (unbranched sheathed filaments 3–5 µm basally, tapering to 1–3 µm, attached by a holdfast, extending up to a millimetre) foul the appendages, gills and eggs of cultured penaeids and lobster larvae, alongside *Thiothrix*, *Flexibacter*, *Cytophaga* and peritrich protozoans; filamentous bacteria are explicitly reported to infest penaeid shrimp *larvae* ([SEAFDEC review of penaeid shrimp diseases](https://repository.seafdec.org.ph/bitstream/handle/10862/877/ficcpps_p079-103.pdf?isAllowed=y&sequence=1); [US Patent 4,418,648, "Process for the reduction of gill disease in shrimp"](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4418648)). Note the organism from penaeids has not been isolated in pure culture, so the *L. mucor* identification is tentative.

**g. It is the stage with a named, stage-specific dysbiosis.** *Zoea 2 syndrome* ("bolitas syndrome") is a vibriosis of early *P. vannamei* larvae attributed to *Vibrio alginolyticus* and *V. harveyi*, with hepatopancreatic cell detachment and vacuolisation, hindgut epithelial damage, and off-white body colour. Affected larvae show ~2-fold Vibrionaceae enrichment and significant enrichment of *Vibrio*, *Spongiimonas*, *Meridianimaribacter* and *Tenacibaculum*, with strong *Vibrio*–*Catenococcus* co-occurrence (Reyes et al. 2023, [doi:10.7717/peerj.15795](https://doi.org/10.7717/peerj.15795)). In crabs, opportunistic *Vibrio* (*V. harveyi*, *V. parahaemolyticus*, *V. alginolyticus*, *V. campbellii*, *V. proteolyticus*, *V. tubiashii*) cause mass zoeal mortality in hatcheries, including vertical transmission via female faeces ([de Souza Valente & Wan 2021, *J Invertebr Pathol* 181:107527, doi:10.1016/j.jip.2020.107527](https://doi.org/10.1016/j.jip.2020.107527)).

**h. Preceded by a distinct embryonic community.** Swimming-crab embryos show γ-Proteobacteria (Oceanospirillaceae, Colwelliaceae) progressively replaced by α-Proteobacteria (Rhodobacteraceae) and Flavobacteriaceae before hatching ([Sun et al. 2025, *Aquaculture* 595:741523, doi:10.1016/j.aquaculture.2024.741523](https://doi.org/10.1016/j.aquaculture.2024.741523)) — useful for the boundary against the embryo record.

**What the differentia should NOT assert:** a fixed number of zoeal instars (2 in *Palicus caronii*, ≥12 over ~120 days in *Plesionika grandis*), a fixed feeding mode (early-stage alvinocaridid vent shrimp zoeae are primarily lecithotrophic — [Hernández-Ávila et al. 2015, *PLOS ONE*, doi:10.1371/journal.pone.0144657](https://doi.org/10.1371/journal.pone.0144657)), or a hatchery setting. Zoeae are overwhelmingly *studied* in aquaculture, but they are a wild planktonic stage; putting "hatchery" in the definition would import a sampling bias as a defining property.

---

## 4. Sources

| Claim | Source |
|---|---|
| Zoea = free-swimming planktonic decapod larval stage; thoracic-appendage swimming; crabs hatch directly as zoea; zoea → megalopa | [Britannica, "zoea"](https://www.britannica.com/science/zoea); UBERON:0014857 definition |
| Zoea stage is a recognised crustacean larval stage in a nauplius–zoea–post-larval series | UBERON:0014857, UBERON:0018378 (OLS4: `https://www.ebi.ac.uk/ols4/api/search?q=zoea`) |
| "larva" is a multicellular organism, with "zoea" as a *narrow* synonym | UBERON:0002548 via [OLS4](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0002548) |
| ENVO genus candidates and their definitions | ENVO:01001176, ENVO:01001055, ENVO:01001002, ENVO:01001179 via OLS4 |
| Whole rinsed larvae are the sample; zoea timing; U-shaped diversity; Rhodobacteraceae 72.4 %; host selection from water; mouth opening as inflection point | Wang Y, Wang K, Huang L, Dong P, Wang S, Chen H, Lu Z, Hou D, Zhang D. *Microbiome* 8:106 (2020). [doi:10.1186/s40168-020-00879-w](https://doi.org/10.1186/s40168-020-00879-w) |
| Crab zoeal succession Z1–Z4, instar durations, Rhodobacteraceae rise, sources and assembly | Lu Z, Ren Z, Lin W, Shi C, Mu C, Wang C, Wu Q, Ye Y. *Aquaculture* 548:737600 (2022). [doi:10.1016/j.aquaculture.2021.737600](https://doi.org/10.1016/j.aquaculture.2021.737600) |
| Zoea 2 syndrome definition, agents, pathology, microbiome signature | Reyes G, et al. *PeerJ* 11:e15795 (2023). [doi:10.7717/peerj.15795](https://doi.org/10.7717/peerj.15795) · [PMC10476614](https://pmc.ncbi.nlm.nih.gov/articles/PMC10476614/) |
| *Vibrio* pathogens of decapod larvae; vertical transmission; hatchery mortality | de Souza Valente C, Wan AHL. *J Invertebr Pathol* 181:107527 (2021). [doi:10.1016/j.jip.2020.107527](https://doi.org/10.1016/j.jip.2020.107527) |
| Embryonic community preceding the zoea | Sun Y, Lin W, Wu Q, Shi C, Wang C, Ye Y. *Aquaculture* 595:741523 (2025). [doi:10.1016/j.aquaculture.2024.741523](https://doi.org/10.1016/j.aquaculture.2024.741523) |
| Filamentous epibiont fouling of larval/penaeid cuticle; morphology; tentative *L. mucor* ID | [SEAFDEC penaeid disease review](https://repository.seafdec.org.ph/bitstream/handle/10862/877/ficcpps_p079-103.pdf?isAllowed=y&sequence=1); [US Patent 4,418,648](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4418648) |
| Chitinous planktonic crustacean surfaces as a *Vibrio* habitat (**analogue, copepods not zoeae**) | Huq A, Small EB, West PA, Huq MI, Rahman R, Colwell RR. *Appl Environ Microbiol* 45:275–283 (1983). [doi:10.1128/aem.45.1.275-283.1983](https://doi.org/10.1128/aem.45.1.275-283.1983) |
| Variation in instar number; lecithotrophy in vent-shrimp zoeae | [Di Muzio et al. 2019, PMC6910961](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6910961/); [Hernández-Ávila et al. 2015, doi:10.1371/journal.pone.0144657](https://doi.org/10.1371/journal.pone.0144657); [Yang et al., PMC5740431](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5740431/) |
| GOLD ecosystem path scheme and node identifiers | Mukherjee S, Stamatis D, Li CT, Ovchinnikova G, Bertsch J, Sundaramurthi JC, Kandimalla M, Nicolopoulos PA, Favognano A, Chen I-MA, Kyrpides NC, Reddy TBK. *Nucleic Acids Res* 51:D957–D963 (2023). [doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974); local `data/raw/gold_ecosystem_paths.tsv` |
| Standard reference work on decapod larval biology (not consulted in full text here — recommended for the curator before finalising) | Anger K. *The Biology of Decapod Crustacean Larvae*. Crustacean Issues 14, Balkema, 2001. [ResearchGate record](https://www.researchgate.net/publication/266673708_The_Biology_of_Decapod_Crustacean_Larvae) |

**Explicitly my inference, not a source's statement:** (i) that GOLD's `Larva: Zoea` probably absorbs penaeid mysis-stage samples given the absence of a `Mysis` node; (ii) that moulting every 2–3 days resets the epibiotic surface (moult intervals are sourced, the reset consequence is not); (iii) that `Larva: Zoea` and its `> Whole body` child denote the same material.

---

## 5. Synonyms, and what not to conflate

**In real use for this concept:**
- zoea, zoëa, zoea larva, zoeal stage, zoeal larva
- plural: zoeae, zoeas
- protozoea / protozoeal stage (penaeid usage for the equivalent post-nauplius feeding stage; commonly written "zoea" in aquaculture practice)
- stage abbreviations: Z1–Zn, ZI–ZIII, Z-I/Z-II/Z-III
- "zoea larvae", "zoea-stage larvae" (whole-organism sample descriptor)
- Historically a nominal genus, *Zoea* Bosc 1802, before it was recognised as a developmental stage of known crabs

**Commonly but wrongly treated as the same thing:**
- **Nauplius** — a *sibling* GOLD node and a genuinely different habitat: non-feeding, closed gut, higher and compositionally different bacterial diversity.
- **Mysis / megalopa / post-larva** — later stages; `Post-larva` is its own GOLD node.
- **"Larva" unqualified** — GOLD's `Host-associated > Arthropoda: Crustaceans > Larva` is a separate, broader node with its own children; do not merge.
- **Larval rearing water / hatchery tank** — the `Engineered > Aquaculture > Crustaceans tank` branch. The most frequent conflation in practice, and the studies cited exist partly to separate them.
- **The zoeal gut** — a part; belongs with `Larva > Gut` and grounds to the anatomy term.
- **The zoea *stage* as a time interval** (UBERON:0014857) — a temporal region, not a place.
- **Zoea 2 syndrome** — a disease state of larvae at this stage. A disease is not a habitat; if it ever appears as a source concept, it is `NOT_APPLICABLE`.
- ***Artemia* nauplii** — the live feed fed *to* zoeae, a separate organism and a separate habitat, and a documented bacterial source into the larval community.
- **"Zoea" in non-decapod contexts** — stomatopods have antizoea/pseudozoea larvae; NCBITaxon also carries unrelated species epithets (*Ducula zoeae*, *Ooencyrtus zoeae*, *Gnathophausia zoea*) that will pollute any lexical match. Do not ground on a string match.

---

## 6. Should this be a term at all?

**Yes — keep it, as its own minted concept, `UNGROUNDED`, exactly as the existing curation note has it.** Three checks:

1. **Is it a habitat?** Yes, under the rule #114 settled and the ENVO precedent: a host organism is where microbes live, and ENVO models exactly this at animal-, plant- and fungi-associated environment. A zoea is a small aquatic animal carrying a distinctive, repeatedly-measured microbial community with its own diversity minimum, its own dominant family, its own selection regime on the surrounding water, and its own named dysbiosis. That is a place, not a process, quality, disease or procedure.
2. **Is it an organism-as-taxon over-claim?** No — but the *terms* are. `Larva: Zoea` names a stage of a host, and both UBERON:0002548 (a `multicellular organism` subclass) and UBERON:0014857 (a life cycle stage) denote things that are not places. Both belong in `xrefs`, not `parent_habitats` and not as grounding targets. **Concrete recommendation: add `UBERON:0014857` 'zoea stage' as a second xref** — it is a far more precise pointer than 'larva', whose relation to zoea UBERON itself records as *narrow synonym*.
3. **Is it a sampling artefact?** Partly, and this is the one honest weakness. Upstream assertion volume is **0**, and GOLD carries a `> Whole body` child (gold.ecosystem:7356/7357) that in practice denotes the same material. The record is a scaffold node in GOLD's path grammar rather than a concept anyone has yet deposited data against. That argues for keeping it and *not* prioritising an ENVO term request for it — but it does not argue for `NOT_APPLICABLE`, which asserts the stronger and false claim that a zoea is not a habitat.

**If a term request is ever made, request the intermediate class first.** ENVO has `cnidarian-associated environment` (ENVO:01001179) as a worked example under `environment associated with an aquatic invertebrate`, and nothing for arthropods or crustaceans at all. A `crustacean-associated environment` request would serve this record, the `Arthropoda: Crustaceans` parent, `Larva: Nauplius`, `Post-larva`, and the whole crustacean anatomical branch at once; a zoea-specific leaf serves one record with zero assertions behind it.

## Citations

1. https://doi.org/10.1186/s40168-020-00879-w
2. https://doi.org/10.7717/peerj.15795
3. https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/…ENVO_01001002/hierarchicalChildren`
4. https://github.com/EnvironmentOntology/envo/issues/1029
5. https://doi.org/10.1016/j.aquaculture.2021.737600
6. https://www.britannica.com/science/zoea
7. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6910961/
8. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8195950/
9. https://doi.org/10.1128/aem.45.1.275-283.1983
10. https://repository.seafdec.org.ph/bitstream/handle/10862/877/ficcpps_p079-103.pdf?isAllowed=y&sequence=1
11. https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4418648
12. https://doi.org/10.1016/j.jip.2020.107527
13. https://doi.org/10.1016/j.aquaculture.2024.741523
14. https://doi.org/10.1371/journal.pone.0144657
15. https://www.ebi.ac.uk/ols4/api/search?q=zoea`
16. https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0002548
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC10476614/
18. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5740431/
19. https://doi.org/10.1093/nar/gkac974
20. https://www.researchgate.net/publication/266673708_The_Biology_of_Decapod_Crustacean_Larvae