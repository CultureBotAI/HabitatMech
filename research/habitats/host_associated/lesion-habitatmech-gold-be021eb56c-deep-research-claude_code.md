---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T22:53:49.974183'
end_time: '2026-08-17T23:02:26.936232'
duration_seconds: 516.96
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Lesion
  habitat_identifier: habitatmech:GOLD.be021eb56c
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Fish > Integumentary system > Skin > Lesion'
  assertions: '23'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Stale-sweep\
    \ review (#12): the fish skin-lesion concept, same as the human one \u2014 NCIT's\
    \ 'Lesion' is a finding, not a place. Path: Host-associated > Fish > Integumentary\
    \ system > Skin > Lesion (source concept habitatmech:GOLD.be021eb56c)"
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
  web_search_requests: 12
  num_turns: 29
  total_cost_usd: 3.1213779999999995
  session_id: 82240e05-cc29-4976-9005-793c24c7c09b
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 27
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Lesion
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.be021eb56c
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Fish > Integumentary system > Skin > Lesion
- **Upstream assertion volume:** 23
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Stale-sweep review (#12): the fish skin-lesion concept, same as the human one — NCIT's 'Lesion' is a finding, not a place. Path: Host-associated > Fish > Integumentary system > Skin > Lesion (source concept habitatmech:GOLD.be021eb56c)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Lesion** as a microbial habitat, with citations.

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

# Lesion (fish skin) — HabitatMech novel-term research

**Target:** `habitatmech:GOLD.be021eb56c` · label *Lesion* · HOST_ASSOCIATED · UNGROUNDED
**Source path:** `Host-associated > Fish > Integumentary system > Skin > Lesion` (`gold.ecosystem:6932`, 23 organism assertions)

---

## Proposed definition

> A **skin environment** which is a focal region of teleost skin where the mucus layer and epidermis have been breached or eroded by injury or disease, exposing dermal, scale-pocket or muscle tissue and its exudate directly to the surrounding water.

Genus term: `ENVO:2100003` *skin environment* — "An environment determined by an area or zone of skin tissue" ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:2100003), verified 2026-08-17; present in the vendored slice, `data/raw/ontology_terms.tsv`, and already a corpus record at `data/habitats/other/skin_environment.yaml`).

The one clause that carries the whole differentia is **"directly to the surrounding water."** That is what makes this concept a genuinely different environment from its terrestrial homologue (`habitatmech:GOLD.5caa9dd47f`, human *Lesion*) rather than the same concept with a different host, and it is what an ENVO-style environment definition is built to express.

---

## 1. What the concept denotes

**The thing sampled** is the lesion site on a live or freshly dead fish: the ulcer bed, its necrotic margin, adherent exudate and any biofilm on it — swabbed or excised. The clearest published example of the sampling act is Godoy et al. 2023, who swabbed "ulcerated areas, non-ulcerated skin regions, and first-gill arches" of the same *Salmo salar* population into RNAlater ([*Animals* 14:97, doi:10.3390/ani14010097](https://doi.org/10.3390/ani14010097); [PMC10778177](https://pmc.ncbi.nlm.nih.gov/articles/PMC10778177/)).

**The label is genuinely ambiguous, and GOLD's is the broadest reading.** The readings in the fish-health literature are:

1. **Deep ulcer** — full-thickness loss of epidermis and dermis, often exposing musculature. Winter ulcer (*Moritella viscosa*) and advanced epizootic ulcerative syndrome (EUS) lesions are of this kind ([WOAH Aquatic Manual, *Infection with Aphanomyces invadans*](https://www.woah.org/fileadmin/Home/eng/Health_standards/aahm/current/chapitre_aphanomyces_invadans.pdf)).
2. **Superficial erosion / red spot** — scale loss, blanching, haemorrhagic focus, no deep tissue exposure. EUS lesion scoring runs explicitly from score 1 (skin blanching, loss of scales and epithelial cells) to score 4 (deep ulcers involving underlying muscle) — the same disease produces both readings in sequence (WOAH, ibid.; [Reviews in Fisheries Science & Aquaculture 28:3, doi:10.1080/23308249.2020.1753167](https://doi.org/10.1080/23308249.2020.1753167)).
3. **Any focal skin abnormality**, including non-ulcerative nodules, granulomas or masses.

**The source path settles which reading the data means, and it is the broadest one.** In `data/raw/gold_ecosystem_paths.tsv` the complete child set of `Host-associated > Fish > Integumentary system > Skin` is:

| child node | assertions |
|---|---|
| **Lesion** | **23** |
| Epidermal mucus | 7 |
| Fin | 0 |

There is **no *Ulcer*, no *Abscess*, no *Erosion* sibling** anywhere in GOLD's fish branch. *This is the single most important structural difference from the human `Lesion` record*, where *Ulcer* (`GOLD.8eb824daf3`) and *Abscess* (`GOLD.ef667faebd` and others) are named siblings and *Lesion* is what was left over. **Here, "Lesion" is not a residual bin — it is the only node GOLD offers for any pathologically altered fish skin, and it must therefore absorb winter ulcers, tenacibaculosis erosions, EUS ulcers, red-spot lesions and non-specific ulcers alike.** *(The table is data; the conclusion drawn from it is my inference, not something GOLD documents.)*

For scale: 23 of the 82 organism assertions in the whole `Fish > Integumentary system` subtree sit on this node — more than the parent *Skin* node's own 52 would suggest is marginal. *(My arithmetic from the path table.)*

### Boundary — what is inside and what is a neighbouring concept

**Inside:** the ulcer bed and its margin; necrotic tissue and exudate in the lesion; the biofilm on the lesion surface; the scale pocket and dermis where these are exposed.

**Outside, and each already has its own GOLD node and HabitatMech record:**

- **Intact skin of the same fish** — the parent record `habitatmech:GOLD.92e3c832eb` (*Skin*, 52 assertions). Godoy et al. sampled non-ulcerated skin of infected fish as a *separate* sample type, and it was intermediate between healthy control skin and ulcer, not equivalent to either (doi:10.3390/ani14010097).
- **Epidermal mucus** — sibling, grounded `UBERON:0010152` *skin mucus* at `data/habitats/host_associated/skin_mucus.yaml`. In a deep lesion the mucus layer is precisely what is *absent*, so these two concepts are complementary, not nested.
- **Gill** (`Host-associated > Fish > Respiratory system > Gills`) — a separate mucosal surface with its own lesion syndromes.
- **Internal organs of an ulcerated fish** — GOLD has *Kidneys*, *Spleen*, *Blood*, *Liver* nodes under Fish. Winter ulcer and tenacibaculosis both progress to septicaemia, with *M. viscosa* recovered from head kidney, spleen, liver and blood ([Olsen et al. 2011, *Dis Aquat Organ* 94:189, doi:10.3354/dao02324](https://doi.org/10.3354/dao02324), PMID 21790066). **A systemic isolate from head kidney of an ulcerated fish belongs to the kidney node, not this one.** This is a real and likely source of mis-binning in the 23 assertions and should be stated in the record's notes.
- **The pond, tank or sea-cage water bathing the lesion** — an aquatic-biome concept. It is continuous with the lesion (that is the differentia) but it is not the lesion.

---

## 2. Genus — the broader kind

**`ENVO:2100003` *skin environment*** is the correct genus and is in the vendored slice. It is host-agnostic ("an area or zone of skin tissue"), so it covers teleost skin without over-claiming; host specificity comes from the parent chain, which for this record runs *Skin* → *Fish* (`GOLD.3d529a667e`, itself parented to `ENVO:01001002` *animal-associated environment* with a fish-associated-environment term request pending).

### Near-misses, and why each fails

| Term | Why it is not the genus |
|---|---|
| `ENVO:2100004` *integumental system environment* | In slice, **but carries no definition text at all** (empty definition column in `data/raw/ontology_terms.tsv`; confirmed empty in ENVO). Broader than needed and undefined — a poor thing to hang a new definition off. |
| `BTO:0001253` *skin* | **This is what the parent record `GOLD.92e3c832eb` is currently NARROW-grounded to**, and it is a bad anchor: BTO defines it as "the integument of an animal (as a fur-bearing mammal or a bird) separated from the body usually with its hair or feathers" — a **pelt**, not a place, and mammal/bird-framed. Flagging this as a separate finding (§6). |
| `UBERON:0002097` *skin of body*, `UBERON:0001003` *skin epidermis* | Anatomy terms for the intact organ. They name the site without the pathological alteration — the genus's ingredient, not the concept. Under the CLAUDE.md parts-vs-whole rule these are legitimate *part* terms, but grounding here would erase the only thing the concept adds. |
| `UBERON:0010152` *skin mucus* | The sibling concept, and in a deep lesion the layer that has been lost. |
| `BTO:0003114` *wound fluid* | The exudate — a material, not a site. Useful as an xref for the substrate, not as a genus. |
| `ENVO:02000040` *mucus material* | Material, not place. |
| `NCIT:C3824` *Lesion* | Label match only. NCIT is a cancer-domain terminology; the class is an abnormality/finding, has no environment semantics and no aquatic scope. The existing curation note's use of it is right in outcome. |
| `MeSH:D014947` *Wounds and Injuries* | A disease/injury class, not a place; also excludes non-traumatic lesions. |

**ENVO has no pathological axis anywhere under `ENVO:2100000` *anatomical entity environment*.** An OLS4 search of ENVO for "wound" returns **zero ENVO classes** (queried 2026-08-17; the only hits are PATO shape qualities matching "wound" as in *coiled*). There is no *wound environment*, no *lesion environment*, no *diseased tissue environment*. **Nothing in ENVO can be grounded to, so this record cannot be resolved by grounding — only by a term request or by confirming it ungrounded.**

---

## 3. Differentia — what distinguishes a fish skin lesion

Each of these is observable or measurable, and each is candidate differentia or `environmental_parameters` material.

### (a) The breach opens directly onto the water column — the primary differentia

Fish skin is a *living, non-keratinised, mucus-covered* epithelium that serves simultaneously as an osmotic barrier and as the mucosal immune interface with the water; unlike the highly keratinised skin of mammals it is part of the mucosal immune system ([Esteban 2012, *ISRN Immunology*, doi:10.5402/2012/853470](https://doi.org/10.5402/2012/853470)). When it is breached, two things happen at once that have no terrestrial equivalent: severe **osmotic stress from acute skin loss**, and **direct access for waterborne microbes** — *Aeromonas* spp., *Pseudomonas* spp., *Saprolegnia* spp. and parasites invade far more readily ([Sveen et al. 2020, "Mechanical induced wounds in fish – a review on models and healing mechanisms", *Reviews in Aquaculture* 12:2446–2465, doi:10.1111/raq.12443](https://doi.org/10.1111/raq.12443)).

Because the lesion is continuously bathed, the **ambient water community is itself an input to the lesion community**: a largemouth bass wound model found healing rates differed with pond-water microbiota, via effects on skin and wound microbiota ([*Aquaculture* 2025, doi:10.1016/j.aquaculture.2025.742180](https://doi.org/10.1016/j.aquaculture.2025.742180) — see [ScienceDirect S0044848625001504](https://www.sciencedirect.com/science/article/abs/pii/S0044848625001504)). *This is the strongest reason the fish concept is not a copy of the human one, and it is the clause I would keep if only one differentia survives.*

### (b) Depth of breach determines colonisation — a dose-response, not a binary

In Atlantic salmon, removing the mucus layer by swabbing alone raised mortality with *Vibrio anguillarum*, whereas raised mortality with *Aeromonas salmonicida* required deep wounding; partial or deep scarification increased infection and ulcer development by *Moritella viscosa* and *Tenacibaculum* spp. (Sveen et al. 2020, doi:10.1111/raq.12443). This supports treating "breached or eroded" as the differentia while acknowledging the class spans erosion to full-thickness ulcer.

### (c) The lesion community is measurably distinct from intact skin on the same infected fish

This is the empirical case that a lesion is a distinguishable habitat rather than a label on skin. Godoy et al. 2023 compared healthy control skin, non-ulcerated skin of infected fish, and ulcers: NMDS on Bray–Curtis with PERMANOVA (`adonis2`) separated groups at *p* = 0.001; healthy versus ulcerated skin diverged at *p* = 0.00014, while infected-but-non-ulcerated skin differed less (*p* = 0.042) — i.e. **a gradient with the ulcer at the extreme** (doi:10.3390/ani14010097). Note the counter-example the same authors cite: Kashinskaya et al. 2021 found no beta-diversity difference in intact skin mucosa of Prussian carp bearing ectoparasites, so the effect is not universal across insult types.

### (d) Characteristic taxa — a recurrent polymicrobial "pathobiome", not one agent

- Ulcerated salmon skin is colonised by *Piscirickettsia salmonis*, *Tenacibaculum dicentrarchi* and *Aliivibrio wodanis*, with Vibrionaceae, Flavobacteriaceae and Pseudomonadaceae over-represented; the authors describe a previously undescribed **core pathobiome** (doi:10.3390/ani14010097).
- Winter ulcer is conventionally *M. viscosa* disease, but *Aliivibrio wodanis* and *Tenacibaculum* spp. are recurrently co-isolated and their role is unresolved (doi:10.3354/dao02324).
- **Culture badly under-reports the community.** Olsen et al. saw *Tenacibaculum*-like long slender rods histologically in **70%** (1996) and **62.5%** (2004–05) of ulcers, while marine-agar culture recovered them from only **3%** and **13%** (doi:10.3354/dao02324). This is a direct argument that lesion samples should be characterised culture-independently, and a caution about what the 23 GOLD organism assertions represent.
- In EUS, the primary agent is the oomycete *Aphanomyces invadans*, with *Aeromonas hydrophila* and *A. sobria* implicated as opportunists; a post-flood Kerala epizootic recovered *Aeromonas veronii*, *Shewanella putrefaciens*, *Vibrio vulnificus* and *V. parahaemolyticus* from affected tissue (WOAH chapter; [*J Fish Dis* 2020, PMID 32270765](https://pubmed.ncbi.nlm.nih.gov/32270765/)). **The lesion habitat is therefore not exclusively bacterial** — an oomycete is the defining resident in the largest ulcerative syndrome by species range (~94 fish species histologically confirmed).
- A pathogen can also actively prevent the lesion from closing: *M. viscosa* affects or inhibits keratocyte-mediated epidermal regeneration (Sveen et al. 2020, doi:10.1111/raq.12443), which is what makes the lesion a *persistent* habitat rather than a transient one.

### (e) The intact-skin baseline this is measured against

Across 1,922 fish skin microbiomes from 36 studies and 98 species, Gammaproteobacteria were present in every marine and freshwater fish skin microbiome; *Acinetobacter*, *Aeromonas*, *Ralstonia*, *Sphingomonas* and *Flavobacterium* dominated freshwater fish skin, and *Alteromonas*, *Photobacterium*, *Pseudoalteromonas*, *Psychrobacter* and *Vibrio* dominated saltwater fish ([Kelly et al. 2024, *FEMS Microbiol Ecol* 100:fiae021, doi:10.1093/femsec/fiae021](https://doi.org/10.1093/femsec/fiae021)). Water temperature, pH, dissolved oxygen and salinity all correlated with beta-diversity — **so the water's physicochemistry is already a determinant of intact fish skin communities, and an open lesion can only increase that coupling.** *(The inference in that last clause is mine.)*

### (f) Physicochemistry — what I could NOT source, stated plainly

**I found no measured pH, redox or osmolality value for a fish skin lesion bed.** The human-lesion report could cite a chronic-wound pH range; the fish literature has no equivalent I could locate, and fish skin mucus pH itself is reported only qualitatively and varies with species, ambient water and stress ([Frontiers in Marine Science 2020, doi:10.3389/fmars.2020.541853](https://doi.org/10.3389/fmars.2020.541853)). **Do not transfer the human chronic-wound values (7.15–8.9) onto this record** — no source supports them for a submerged fish lesion, where the wound bed is in exchange with the ambient water rather than with air. Leave `environmental_parameters` empty rather than borrow.

---

## 4. Sources

**Primary literature — the habitat and its communities**

- Godoy M, Coca Y, Suárez R, et al. *Salmo salar* skin and gill microbiome during *Piscirickettsia salmonis* infection. *Animals* 14(1):97, 2023-12-27. [doi:10.3390/ani14010097](https://doi.org/10.3390/ani14010097) · [PMC10778177](https://pmc.ncbi.nlm.nih.gov/articles/PMC10778177/) — *the key citation: paired ulcer / non-ulcerated-skin / gill sampling, PERMANOVA, "core pathobiome".*
- Olsen AB, Nilsen H, Sandlund N, Mikkelsen H, Sørum H, Colquhoun DJ. *Tenacibaculum* sp. associated with winter ulcers in sea-reared Atlantic salmon *Salmo salar*. *Diseases of Aquatic Organisms* 94(3):189–199, 2011-05-09. PMID 21790066. [doi:10.3354/dao02324](https://doi.org/10.3354/dao02324) — *histology 70% / 62.5% vs culture 3% / 13%; co-infection established within 1 h on existing M. viscosa ulcers.*
- Sveen L, Karlsen C, Ytteborg E, et al. Mechanical induced wounds in fish — a review on models and healing mechanisms. *Reviews in Aquaculture* 12(4):2446–2465, 2020-04-27. [doi:10.1111/raq.12443](https://doi.org/10.1111/raq.12443) — *barrier breach, osmotic stress, wound-depth/pathogen dose-response.*
- Kelly C, Salinas I, et al. Influence of host phylogeny and water physicochemistry on microbial assemblages of the fish skin microbiome. *FEMS Microbiology Ecology* 100(3):fiae021, 2024-02-21. [doi:10.1093/femsec/fiae021](https://doi.org/10.1093/femsec/fiae021) · [PMC10903987](https://pmc.ncbi.nlm.nih.gov/articles/PMC10903987/) — *intact-skin baseline, 1,922 samples / 36 studies / 98 species.*
- Esteban MÁ. An overview of the immunological defenses in fish skin. *ISRN Immunology* 2012:853470. [doi:10.5402/2012/853470](https://doi.org/10.5402/2012/853470) — *fish skin as non-keratinised mucosal barrier.*
- Sequeira V, et al. Influence of aquaculture pond water microbiota on wound healing in largemouth bass (*Micropterus salmoides*) via modulation of skin and wound microbiota. *Aquaculture*, 2025. [ScienceDirect S0044848625001504](https://www.sciencedirect.com/science/article/abs/pii/S0044848625001504) — *ambient water microbiota as an input to the wound community.*
- Sveen L, et al. Global gene expression responses of Atlantic salmon skin to *Moritella viscosa*. *Scientific Reports* 12:4224, 2022-03-11. [doi:10.1038/s41598-022-08341-7](https://doi.org/10.1038/s41598-022-08341-7) · [PMC8931016](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8931016/)
- Munday BL, et al. The acute ulceration response (AUR): a potentially widespread and serious cause of skin infection in fish. *Aquaculture* 246:1–4, 2005. [ScienceDirect S0044848605000293](https://www.sciencedirect.com/science/article/abs/pii/S0044848605000293) — *aetiologies of barrier breach: infectious, toxic, physical, immunologic, nutritional.*
- Molecular evidence for stress, inflammation and structural changes in **non-specific ulcers** in skin of farmed Chinook salmon (*Oncorhynchus tshawytscha*). *Fish & Shellfish Immunology*, 2023. PMID 37061071. [PubMed](https://pubmed.ncbi.nlm.nih.gov/37061071/) — *"non-specific ulcer" is the field's own name for exactly what GOLD's bare "Lesion" denotes.*
- Ledesma-Amaro R, et al. Community structure and functional annotations of the skin microbiome in healthy and diseased catfish, *Heteropneustes fossilis*. [PMC8918984](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8918984/) — *freshwater, non-salmonid counterexample.*
- Salmonid alphavirus infection causes skin dysbiosis in Atlantic salmon post-smolts. *PLOS ONE* 12(3):e0172856, 2017. [doi:10.1371/journal.pone.0172856](https://doi.org/10.1371/journal.pone.0172856) — *a viral insult produces skin dysbiosis without a classic ulcer; boundary case.*

**Standards, reference works and vocabularies**

- WOAH (OIE) Aquatic Animal Health Code / Manual, *Infection with Aphanomyces invadans* (EUS). [PDF](https://www.woah.org/fileadmin/Home/eng/Health_standards/aahm/current/chapitre_aphanomyces_invadans.pdf) — *lesion progression scoring, ~94 confirmed host species, opportunist Aeromonas involvement.*
- Reviews in Fisheries Science & Aquaculture 28(3), EUS pathobiology review. [doi:10.1080/23308249.2020.1753167](https://doi.org/10.1080/23308249.2020.1753167)
- GSC MIxS host-associated extension — `host_body_site` (UBERON/FMA) and `host_disease_stat` (`MIXS:0000031`, DO) are **separate slots**. [genomicsstandardsconsortium.github.io/mixs/0016002](https://genomicsstandardsconsortium.github.io/mixs/0016002/) — *the standards-body precedent against minting a site term for a diseased site; see §6.*
- ENVO `ENVO:2100003` *skin environment*, `ENVO:2100004` *integumental system environment* (no definition), `ENVO:01001002` *animal-associated environment*; ENVO search for "wound" returns no ENVO class. Retrieved from EBI OLS4, 2026-08-17. [OLS4 ENVO:2100003](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:2100003)
- In-repo evidence: `data/raw/gold_ecosystem_paths.tsv` (sibling structure, assertion counts); `data/raw/ontology_terms.tsv` (vendored slice contents); `data/habitats/host_associated/skin__9a5d285e.yaml`, `skin_mucus.yaml`, `data/habitats/other/skin_environment.yaml`; `curation/decisions.tsv` (`GOLD.3d529a667e` Fish, `GOLD.5caa9dd47f` human Lesion).

**Explicitly my inference, not any source's claim:**
(i) that GOLD's fish *Lesion* is a catch-all rather than a residual, argued from the absence of Ulcer/Abscess siblings in the fish branch; (ii) the assertion arithmetic in §1; (iii) that systemic isolates from ulcerated fish may be mis-binned here versus the kidney/spleen nodes; (iv) that open lesions increase the water–community coupling that Kelly et al. demonstrate for intact skin; (v) the whole recommendation in §6.

---

## 5. Synonyms, and what NOT to conflate

**Names in real use for this concept:** *skin lesion*; *skin ulcer*; *ulcerative lesion*; *non-specific ulcer*; *dermal ulcer*; *cutaneous lesion*; *ulcerated skin*; *lesion site*; *red spot* (early-stage, EUS/RSD); *winter ulcer* and *winter wound* (the *M. viscosa* syndrome specifically). GOLD's own string is bare *Lesion*.

**Commonly but wrongly treated as the same thing:**

- **Winter ulcer disease / tenacibaculosis / EUS / ulcerative mycosis / mycotic granulomatosis / red spot disease** — these are *diseases* (processes with an aetiological agent); the lesion is the *locus*. EUS alone carries four of those aliases (WOAH chapter). Under CLAUDE.md this is exactly the disease-versus-place line, and it is what MIxS encodes as `host_disease_stat` versus `host_body_site`.
- **Epidermal mucus (`UBERON:0010152`)** — the *sibling* GOLD node with its own record. In a full-thickness lesion the mucus layer is absent. Merging them would double-count and contradict the source hierarchy.
- **Intact skin (`habitatmech:GOLD.92e3c832eb`, `UBERON:0002097`)** — the parent. Godoy et al. show non-ulcerated skin of an infected fish is its own intermediate state, distinct from both.
- **Gill lesion / mouth erosion / fin rot** — tenacibaculosis presents as skin lesions *and* mouth erosion, frayed fins and tail rot. Only the skin ones are in scope; GOLD has separate *Gills* and (zero-assertion) *Fin* nodes.
- **Systemic infection sites** — head kidney, spleen, liver, blood of an ulcerated fish. Different GOLD nodes; different habitat.
- **`BTO:0003114` *wound fluid*** — the exudate material, not the site. Good xref, wrong genus.
- **`NCIT:C3824` *Lesion*** — a human-clinical abnormality class; the label matches and nothing else does.
- **`MeSH:D014947` *Wounds and Injuries*** — injury as event/condition, and it excludes the non-traumatic lesions (EUS, winter ulcer) that dominate this concept.
- **Human skin lesion (`habitatmech:GOLD.5caa9dd47f`)** — the homologous concept in the human branch, and the reason a shared parent term is attractive; but the two are *not* interchangeable, because only one of them is submerged.
- **Plant lesion (`habitatmech:BACDIVE.31392c69b9`)** — a homonym in another domain.
- **Sea-lice attachment sites, net-pen abrasion, delousing damage** — mechanical wounds are within the concept when the barrier is breached (Sveen et al. treat them together), but the *causes* are not the habitat.

---

## 6. Whether it should be a term at all

**Yes — and the fish case is stronger than the human one.** But it should be settled as a family with the human record, not alone.

### The case for

- **It is a place, not a finding.** A breach exposing dermis and muscle to water is a material configuration with a boundary, not a quality of an organism. `NOT_APPLICABLE` — which CLAUDE.md reserves for diseases, qualities, processes and procedures — would be the wrong disposition here.
- **The community is measurably distinct** from both intact skin of the same infected fish and healthy control skin, in the same study, by the same method (doi:10.3390/ani14010097).
- **It is not a residual bin.** Unlike the human record, this node has no Ulcer or Abscess siblings; it is GOLD's *only* handle for pathologically altered fish skin, carrying 23 assertions, and there is nowhere else for that data to go.
- **The differentia is environmental, not merely pathological.** "Open to the water column" is the kind of claim ENVO's environment classes exist to make. That is not true of the human lesion, whose differentia are all about the host tissue.
- **ENVO has nothing to ground to**, so the record cannot be resolved any other way (§2).

### The case against

- **MIxS puts this on the disease axis.** The GSC's own minimum-information standard annotates a diseased site as *body site* + `host_disease_stat`, not as a distinct site ([mixs/0016002](https://genomicsstandardsconsortium.github.io/mixs/0016002/)). Extended consistently, every anatomical environment term would need a lesional variant. **This is the strongest single argument against, and it applies identically to the human record.**
- **The class is heterogeneous.** Score-1 blanching and score-4 muscle-exposing ulcer are both in it, and an oomycete-driven EUS granuloma and a *Tenacibaculum* erosion are not one microenvironment. This is why the proposed differentia is "breached or eroded" rather than anything quantitative, and why no `environmental_parameters` should be attached (§3f).
- **23 assertions, one source, no cross-references** — modest evidential weight for a term request.
- **Likely contamination of the bin** by systemic isolates from ulcerated fish (my inference, §1).

### Recommendation

1. **Request one ENVO term serving both records:** *skin lesion environment*, parent `ENVO:2100003`, defined generically ("a skin environment in which the epidermal barrier has been breached or disrupted by injury or disease"), with the aquatic clause carried as this record's own narrower differentia via the *Fish* parent chain. This is the same recommendation the human-lesion report reached, and consistency between the two is worth more than either answer alone. **Per the standing memory rule, that request must not be filed without an explicit per-request yes from the curator.**
2. **If the conservative call is preferred, keep `CONFIRM_UNGROUNDED` — but rewrite the note.** The current note's reason ("NCIT's 'Lesion' is a finding, not a place") is a claim about NCIT, not about the concept, and it will not survive scrutiny: SNOMED CT models `52988006 |Lesion|` under **Body structure** as a morphologic abnormality, not under Clinical finding ([SNOMED CT Editorial Guide](https://docs.snomed.org/snomed-ct-specifications/snomed-ct-editorial-guide/readme/snomed-ct-introduction/structure-of-domain-coverage)). The defensible conservative reason is the MIxS one: **the pathological state belongs to the disease axis, and the site is already captured by the parent record `habitatmech:GOLD.92e3c832eb` (Skin).**
3. **File two issues regardless of which way the decision goes** (CLAUDE.md: every review finding becomes an issue):
   - **The fish *Skin* parent is grounded NARROW to `BTO:0001253`**, whose definition is a *pelt* — "the integument of an animal (as a fur-bearing mammal or a bird) separated from the body usually with its hair or feathers." That is wrong for a live teleost and it is the genus anchor this record inherits. `ENVO:2100003` or a UBERON zone-of-skin term is the better target. The record is still `SEEDED`, so this has not been reviewed.
   - **Human *Lesion* (`GOLD.5caa9dd47f`) and fish *Lesion* (`GOLD.be021eb56c`) are `CONFIRM_UNGROUNDED` while their human siblings *Ulcer*, *Abscess*, *DFU* and *venous ulcer* are `NOT_APPLICABLE`.** Same shape, two dispositions. Whatever is decided here should be applied across that family.
4. **Record in the note** that the concept is a *lesion NOS* catch-all spanning erosion to full-thickness ulcer, that no physicochemical parameters are sourceable for it, and that culture-based attestations under-report the community by roughly an order of magnitude for *Tenacibaculum* (doi:10.3354/dao02324).

---

Sources:

- [Godoy et al. 2023, *Animals* 14:97 — doi:10.3390/ani14010097](https://doi.org/10.3390/ani14010097)
- [Godoy et al. 2023, PMC10778177](https://pmc.ncbi.nlm.nih.gov/articles/PMC10778177/)
- [Olsen et al. 2011, *Dis Aquat Organ* 94:189 — doi:10.3354/dao02324](https://doi.org/10.3354/dao02324)
- [Olsen et al. 2011, PubMed PMID 21790066](https://pubmed.ncbi.nlm.nih.gov/21790066/)
- [Sveen et al. 2020, *Rev Aquacult* — doi:10.1111/raq.12443](https://doi.org/10.1111/raq.12443)
- [Kelly et al. 2024, *FEMS Microbiol Ecol* — doi:10.1093/femsec/fiae021](https://doi.org/10.1093/femsec/fiae021)
- [Kelly et al. 2024, PMC10903987](https://pmc.ncbi.nlm.nih.gov/articles/PMC10903987/)
- [Esteban 2012, *ISRN Immunology* — doi:10.5402/2012/853470](https://doi.org/10.5402/2012/853470)
- [Sveen et al. 2022, *Sci Rep* 12:4224 — doi:10.1038/s41598-022-08341-7](https://doi.org/10.1038/s41598-022-08341-7)
- [Largemouth bass pond-microbiota wound healing, *Aquaculture* 2025](https://www.sciencedirect.com/science/article/abs/pii/S0044848625001504)
- [Acute ulceration response, *Aquaculture* 2005](https://www.sciencedirect.com/science/article/abs/pii/S0044848605000293)
- [Non-specific ulcers in farmed Chinook salmon, PMID 37061071](https://pubmed.ncbi.nlm.nih.gov/37061071/)
- [Catfish healthy vs diseased skin microbiome, PMC8918984](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8918984/)
- [Salmonid alphavirus skin dysbiosis, PLOS ONE — doi:10.1371/journal.pone.0172856](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0172856)
- [WOAH Aquatic Manual — Infection with *Aphanomyces invadans*](https://www.woah.org/fileadmin/Home/eng/Health_standards/aahm/current/chapitre_aphanomyces_invadans.pdf)
- [EUS pathobiology review — doi:10.1080/23308249.2020.1753167](https://www.tandfonline.com/doi/full/10.1080/23308249.2020.1753167)
- [Kerala EUS epizootic, PMID 32270765](https://pubmed.ncbi.nlm.nih.gov/32270765/)
- [Skin mucus antimicrobials review — doi:10.3389/fmars.2020.541853](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2020.541853/full)
- [MIxS host-associated extension (GSC)](https://genomicsstandardsconsortium.github.io/mixs/0016002/)
- [ENVO:2100003 *skin environment* (OLS4)](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:2100003)
- [SNOMED CT Editorial Guide — structure of domain coverage](https://docs.snomed.org/snomed-ct-specifications/snomed-ct-editorial-guide/readme/snomed-ct-introduction/structure-of-domain-coverage)
- [Fish skin and gill microbiome ecology review — doi:10.1093/femsre/fuaf027](https://academic.oup.com/femsre/article/doi/10.1093/femsre/fuaf027/8169310)

## Citations

1. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:2100003
2. https://doi.org/10.3390/ani14010097
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC10778177/
4. https://www.woah.org/fileadmin/Home/eng/Health_standards/aahm/current/chapitre_aphanomyces_invadans.pdf
5. https://doi.org/10.1080/23308249.2020.1753167
6. https://doi.org/10.3354/dao02324
7. https://doi.org/10.5402/2012/853470
8. https://doi.org/10.1111/raq.12443
9. https://doi.org/10.1016/j.aquaculture.2025.742180
10. https://www.sciencedirect.com/science/article/abs/pii/S0044848625001504
11. https://pubmed.ncbi.nlm.nih.gov/32270765/
12. https://doi.org/10.1093/femsec/fiae021
13. https://doi.org/10.3389/fmars.2020.541853
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC10903987/
15. https://doi.org/10.1038/s41598-022-08341-7
16. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8931016/
17. https://www.sciencedirect.com/science/article/abs/pii/S0044848605000293
18. https://pubmed.ncbi.nlm.nih.gov/37061071/
19. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8918984/
20. https://doi.org/10.1371/journal.pone.0172856
21. https://genomicsstandardsconsortium.github.io/mixs/0016002/
22. https://docs.snomed.org/snomed-ct-specifications/snomed-ct-editorial-guide/readme/snomed-ct-introduction/structure-of-domain-coverage
23. https://pubmed.ncbi.nlm.nih.gov/21790066/
24. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0172856
25. https://www.tandfonline.com/doi/full/10.1080/23308249.2020.1753167
26. https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2020.541853/full
27. https://academic.oup.com/femsre/article/doi/10.1093/femsre/fuaf027/8169310