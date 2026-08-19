---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:09:02.990146'
end_time: '2026-08-17T16:22:33.837662'
duration_seconds: 810.85
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Oral-cavity-and-airways
  habitat_identifier: habitatmech:BACDIVE.3974b3f169
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Oral-cavity-and-airways'
  assertions: '2102'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Cohort\
    \ review (subset/disjoint mapping screen): a composite of two sites. UBERON:0001005\
    \ 'respiratory airway' covers only the airways half and drops the oral cavity,\
    \ and it is also the correct target for the separate 'Airways' source \u2014 adopting\
    \ it here would merge the two. No single term covers mouth plus airway; the respiratory-tract\
    \ terms exclude the oral cavity. (source concept habitatmech:BACDIVE.3974b3f169)"
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
  num_turns: 44
  total_cost_usd: 3.713182000000001
  session_id: 3864f1d3-dfa8-4845-9f82-82553bd8a51e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 25
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Oral-cavity-and-airways
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.3974b3f169
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Oral-cavity-and-airways
- **Upstream assertion volume:** 2102
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Cohort review (subset/disjoint mapping screen): a composite of two sites. UBERON:0001005 'respiratory airway' covers only the airways half and drops the oral cavity, and it is also the correct target for the separate 'Airways' source — adopting it here would merge the two. No single term covers mouth plus airway; the respiratory-tract terms exclude the oral cavity. (source concept habitatmech:BACDIVE.3974b3f169)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Oral-cavity-and-airways** as a microbial habitat, with citations.

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

# Definition research: **Oral-cavity-and-airways** (`habitatmech:BACDIVE.3974b3f169`)

## Proposed definition

> An **anatomical entity environment** (`ENVO:2100000`) which is determined by the contiguous air- and saliva-exposed lumen of a vertebrate host, extending from the oral cavity and its dentition through the pharynx to the trachea, lower airways and lungs.

One caveat that the curator must resolve before writing this into a record, because it changes the extension of the term: **BacDive's MISO vocabulary contains two sibling nodes with this label** — one a body *site*, one a body *product* — and the kg-microbe slug almost certainly collapses them (see §1.3). The sentence above defines the body-site reading only.

---

## 1. What the concept denotes

### 1.1 It is a category-2 node in BacDive's MISO vocabulary, not a free-text sample description

BacDive indexes every strain's isolation source with manually assigned "isolation source tags" drawn from an in-house controlled vocabulary, the **Microbial Isolation Source Ontology (MISO)**, "organized in a hierarchical ontology that comprises 387 terms on three levels" ([Reimer et al., *Nucleic Acids Research* 2022, doi:10.1093/nar/gkab961](https://doi.org/10.1093/nar/gkab961); earlier count of 376 terms in [Reimer et al. 2019, PMC6323973](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/)). Tags are assigned as a full path — a BacDive strain page shows e.g. `#Host Body-Site / #Oral cavity and airways / #Gingiva` ([BacDive ID 2601](https://bacdive.dsmz.de/pdf/2601?doi=10.13145%2Fbacdive2601.20191129.4.1)).

I parsed the live MISO tree from <https://bacdive.dsmz.de/isolation-sources> on 2026-08-17 (317 unique nodes rendered). The exact position of this concept:

- **Cat1:** `#Host Body-Site` (id 5) — one of eight Cat1 classes: `#Engineered`, `#Environmental`, `#Infection`, `#Host`, `#Host Body-Site`, `#Host Body Product`, `#Condition`, `#Climate`
- **Cat2:** `#Oral cavity and airways` (id 41) — siblings under Cat1 are `#Gastrointestinal tract`, `#Limb`, `#Organ`, `#Plant`, `#Urogenital tract`, `#Other`
- **Cat3 children (11, verbatim):** `#Airways`, `#Gingiva`, `#Lung`, `#Mouth`, `#Periodontal pocket`, `#Plaque`, `#Root (Tooth)`, `#Subgingival plaque`, `#Throat`, `#Tooth`, `#Trachea`

So the concept denotes **the whole oral-plus-respiratory sampling region of a host body**: teeth and their supporting tissues, the mouth and throat, and everything from the trachea down to the lung. It is not restricted to a mucosal surface — dental sites (four of the eleven children) are non-shedding hard surfaces.

### 1.2 The count is a roll-up, not 2,102 samples labelled "oral cavity and airways"

Because MISO tags are assigned as complete Cat1/Cat2/Cat3 paths, a strain tagged `#Mouth` also carries `#Oral cavity and airways`. The record's `assertion_count: 2102` (STRAIN, 881 taxa) is therefore **the union over the eleven children plus strains whose source text was too vague to place at Cat3** — not evidence of a distinct sampling site. This is an inference from the observed path format on BacDive strain pages, but a strongly supported one; the corroborating internal evidence is that `data/raw/bacdive_isolation_sources.tsv` holds only 163 of MISO's ~317 nodes and omits `#Mouth`, `#Lung`, `#Throat`, `#Tooth`, `#Gingiva`, `#Nose`, `#Trachea`, `#Saliva` and `#Sputum` entirely, while retaining `Airways` (73), `Plaque` (106), `Subgingival-plaque` (33), `Root-Tooth` (28), `Bronchial-wash` (18) and `Tracheal-aspirate` (3). The Cat2 tag is carrying the traffic its children would otherwise carry.

**This is the single most important boundary fact for the definition:** whatever is written must be true of a *region*, because the extension is a region-level roll-up, not a site.

### 1.3 The label is ambiguous in the source, and the ambiguity is structural

MISO contains a **second node with the same label**, differing only in capitalisation:

- id 41: `#Host Body-Site` → **`#Oral cavity and airways`**
- id 47: `#Host Body Product` → **`#Oral cavity and Airways`**, whose Cat3 children are `#Bronchial wash`, `#Dental plaque`, `#Mucus`, `#Nasopharyngeal aspirate`, `#Phlegm`, `#Pleural fluid`, `#Saliva`, `#Tracheal aspirate`

Any slugging that lowercases and hyphenates maps both to `oral-cavity-and-airways`. The repo's inventory has exactly one such row (2,102 strains) and separately holds `Bronchial-wash` and `Tracheal-aspirate`, which are **children of node 47**, alongside `Plaque`/`Subgingival-plaque`/`Root-Tooth`, which are children of node 41. That the inventory draws from both branches is consistent with a collapse.

**Two readings, stated rather than chosen:**

- **(A) Site reading** — the anatomical region: mouth, dentition, pharynx, trachea, airways, lung. This is what the label most naturally means and what the definition above covers.
- **(B) Site ∪ product reading** — the region *plus* materials voided or aspirated from it (saliva, sputum-adjacent phlegm, mucus, dental plaque, bronchial and tracheal aspirates, pleural fluid). Pleural fluid is the tell: it is not in the oral-airway lumen at all, so reading (B) is genuinely broader than any single anatomical region.

**Concrete check the curator can run:** in the kg-microbe extraction, look at whether BacDive Cat2 labels are case-normalised before slugging, and whether the 2,102 figure equals BacDive's count for node 41 alone or for 41+47. If it is 41+47, the record is a merge of a site and a product class and should either be split upstream or defined as reading (B) with the pleural-fluid anomaly recorded. **My inference is that the collapse occurred; I could not verify it against BacDive's per-node counts, which the isolation-sources page does not expose.**

### 1.4 The host is not human

The record's `characteristic_taxa` settle a question the label leaves open. Alongside human oral commensals (*Actinomyces viscosus* 74, *Schaalia odontolytica* 33, *Actinomyces naeslundii* 29, *Streptococcus anginosus/sanguinis/oralis/gordonii*) and human respiratory pathogens (*Bordetella pertussis* 60, *B. parapertussis* 17, *Haemophilus influenzae* 28, *Streptococcus pneumoniae* 25, *Corynebacterium diphtheriae* 23) sit two strictly non-human respiratory organisms:

- ***Ornithobacterium rhinotracheale*** (18 strains) — a poultry respiratory-tract pathogen of chickens and turkeys, first isolated in 1981 from the respiratory tract of turkeys ([Barbosa et al., *Veterinary Sciences* 2019, doi:10.3390/vetsci7010003](https://doi.org/10.3390/vetsci7010003))
- ***Histophilus somni*** (14 strains) — a commensal of the bovine **upper respiratory tract** and one of the four principal bacterial agents of bovine respiratory disease ([Zeineldin et al., *Trends in Microbiology* 2019, doi:10.1016/j.tim.2019.04.005](https://doi.org/10.1016/j.tim.2019.04.005))

The definition must therefore say *vertebrate host*, not *human*. MISO's Cat1 is `#Host Body-Site`, host-agnostic by construction, with host taxon carried on the separate `#Host` branch (`#Mammals`, `#Chicken`, `#Bovinae`, …).

**Neighbouring concepts, explicitly outside:** `#Gastrointestinal tract` (Cat2 sibling; oesophagus and below), `#Nose` — which sits under `#Organ` (id 40), **not** under this node, despite the anatomical continuity — `#Sputum` and `#Rumen fluid`, which sit under `#Host Body Product / #Fluids` (id 45), and the `#Infection` branch (`#Tuberculosis`, `#Cystic fibrosis`), which encodes disease state rather than place.

---

## 2. Genus

### 2.1 Recommended: `ENVO:2100000` **anatomical entity environment**

> "An environment which is determined by an anatomical entity."

This is the correct and only clean genus. It is an ENVO class, it is **already in the vendored slice** (`data/raw/ontology_terms.tsv`) and **already used as a parent in this corpus** — `data/habitats/other/mouth_environment.yaml` carries `parent_habitats: [ENVO:2100000]`. Its existing children establish exactly the naming and definition pattern a new term would follow (retrieved from OLS4, 2026-08-17):

| CURIE | Label | ENVO definition |
|---|---|---|
| `ENVO:08000002` | mouth environment | An environment that is determined by a mouth. |
| `ENVO:2100002` | intestine environment | An environmental system determined by an intestine. |
| `ENVO:2100003` | skin environment | An environment determined by an area or zone of skin tissue. |
| `ENVO:01001033` | digestive tract environment | An environmental system which has its properties and dynamics determined by a digestive tract. |
| `ENVO:01001306` | bone element environment | An environment which is determined by a bone element. |
| `ENVO:08000001` | axilla skin environment | An environment that is determined by an axilla skin. |
| `ENVO:2100004/5/6` | integumental system / face skin / feather environment | — |

The full descendant list is 13 terms. **There is no respiratory, airway, lung, trachea or nasal environment class anywhere in ENVO** — I searched ENVO on OLS4 for `lung`, `nasal`, `airway`, `respiratory`, `trachea`, `nose`, `oral`, `saliva`, `sputum` and `pharyn` and got no environment-branch hits. ENVO covers the oral half of this concept and nothing of the airway half.

### 2.2 Near-misses, and why each fails

| Candidate | Verdict | Why |
|---|---|---|
| `UBERON:0001005` **respiratory airway** ("An airway through which respiratory air passes in organisms.") | **Do not use** | Drops the entire oral/dental half. It is also already the identity of `data/habitats/host_associated/respiratory_airway.yaml`, which carries BacDive `Airways` (73 strains) as an EXACT synonym — and `#Airways` is a *child* of this node in MISO. Grounding here would collapse a parent into its own child. The existing curation note is correct. |
| `UBERON:0001557` **upper respiratory tract** ("starts proximally with the nose and ends distally with the cricoid cartilage, before continuing to the trachea") | Near-miss both ends | Excludes the oral cavity *and* stops before the trachea; MISO's node includes `#Trachea` and `#Lung`. |
| `UBERON:0000065` respiratory tract / `UBERON:0001004` respiratory system | Narrower | No oral cavity. Same failure as above. |
| `UBERON:0000165` mouth / `UBERON:0000167` oral cavity | Narrower | Oral half only. |
| **`BTO:0006487` aerodigestive tract** ("The mixed airway and gastrointestinal tract that includes the oral cavity, pharynx, paranasal sinuses, sinonasal tract, larynx, pyriform sinus, pharynx, and upper oesophagus.") | **Best single-term near-miss — in the vendored slice** | Overlapping, not broader: it *adds* the upper oesophagus and paranasal sinuses (which MISO assigns to `#Gastrointestinal tract` and `#Organ` respectively) and *omits* the trachea, lower airways and lung, which MISO includes. Neither subsumes the other → `relation: xref`, never `parent`. |
| `NCIT:C82347` Aerodigestive Tract ("Anatomic structures forming the upper respiratory tract and upper part of the digestive tract… oral cavity, sinonasal tract, pharynx, pyriform sinus, larynx, trachea, and esophagus") | Closest wording anywhere | Includes trachea *and* oral cavity — the nearest match in any vocabulary. Still over-claims the oesophagus and under-claims the lung. NCIT is outside HabitatMech's five source ontologies, so it is citable evidence rather than a grounding target. |
| `ENVO:08000002` mouth environment | Narrower | The oral half only; it is a proper part of the proposed concept and is already a separate record (`data/habitats/other/mouth_environment.yaml`, 608 MADIN taxa). |
| `ENVO:01001002` animal-associated environment | Too broad, and wrong axis | Determined by *an animal*, not by an anatomical part of one. Using it as genus would lose everything the label says. |

**UBERON has no `aerodigestive tract` term at all** (OLS4 search over UBERON: 0 results). That absence is itself the finding: the composite region is named in clinical vocabularies (NCIT, BTO) and in the microbiome literature, but not in the anatomy ontology HabitatMech grounds body sites to.

---

## 3. Differentia

What separates this concept from its Cat2 siblings (`#Gastrointestinal tract`, `#Urogenital tract`, `#Limb`, `#Organ`) and from the two halves it spans. All four properties below are observable and sourced.

**(a) Physical continuity and a single dominant immigration route.** The oral cavity and the lower airways are one connected lumen, and the connection is the defining ecological fact, not an anatomical coincidence. The healthy lung microbiota resembles that of the oropharynx more than that of the nasopharynx or the lower GI tract, and this overlap is attributed to microaspiration and mucosal dispersion ([Bassis et al., *mBio* 2015, doi:10.1128/mBio.00037-15](https://doi.org/10.1128/mBio.00037-15); [Dickson et al., *mBio* 2017, doi:10.1128/mBio.02287-16](https://doi.org/10.1128/mBio.02287-16)). Lung community composition is governed by an immigration/elimination balance in which immigration is dominated by microaspiration — largely during sleep, as oral and pharyngeal muscle tone falls — inhalation, and mucosal dispersion, with elimination by cough, mucociliary clearance and host defence ([Dickson et al., *PLoS Pathogens* 2015, doi:10.1371/journal.ppat.1004923](https://doi.org/10.1371/journal.ppat.1004923); [Garmendia et al., *Microbial Biotechnology* 2024, doi:10.1111/1751-7915.14506](https://doi.org/10.1111/1751-7915.14506)). The oral-lung axis is now a standing framework in the review literature ([*Clinical Microbiology Reviews* 2025, doi:10.1128/cmr.00150-24](https://doi.org/10.1128/cmr.00150-24)).

**(b) Shared species pool.** The composite is treated as one reference space by the field's own infrastructure: eHOMD is explicitly "a resource for the microbiome of the human aerodigestive tract", curating 16S references for nasal passages, sinuses, throat, oesophagus and mouth in a single database ([Escapa et al., *mSystems* 2018, doi:10.1128/mSystems.00187-18](https://doi.org/10.1128/mSystems.00187-18)). The lung community is dominated by taxa of oral provenance — *Prevotella*, *Streptococcus*, *Veillonella*, *Fusobacterium*, *Porphyromonas*, *Neisseria* ([Garmendia et al. 2024](https://doi.org/10.1111/1751-7915.14506)); enrichment of the lung microbiome with oral taxa is associated with Th17 lung inflammation ([Segal et al., *Nature Microbiology* 2016, doi:10.1038/nmicrobiol.2016.31](https://doi.org/10.1038/nmicrobiol.2016.31)). HabitatMech's own top taxa for this record show the same mixture within one bucket: *Actinomyces*, *Schaalia* and oral streptococci beside *Bordetella*, *Haemophilus* and *Streptococcus pneumoniae*.

**(c) Two surface types under one region, unlike any sibling.** This region uniquely combines shedding mucosal epithelium with **non-shedding mineralised tooth surfaces** that support thick, structured biofilms. Four of the eleven Cat3 children (`#Tooth`, `#Root (Tooth)`, `#Plaque`, `#Subgingival plaque`, plus `#Periodontal pocket` and `#Gingiva`) are dental. Dental plaque is spatially organised at micron scale into reproducible taxon consortia ([Mark Welch et al., *PNAS* 2016, doi:10.1073/pnas.1522149113](https://doi.org/10.1073/pnas.1522149113)), and oral biogeography is site-specific and well characterised ([Baker et al., *Nature Reviews Microbiology* 2023, doi:10.1038/s41579-023-00963-6](https://doi.org/10.1038/s41579-023-00963-6)). No other MISO Cat2 body-site node contains a mineralised habitat.

**(d) Physicochemistry: aerobic-to-microaerophilic, near-neutral, saliva- and mucus-wetted, ~host body temperature, with a steep oxygen and nutrient gradient along its length.** The airway surface is a low-biomass, nutrient-poor, mucociliary-cleared environment with a gradient of oxygen tension, pH, temperature and inhaled-particle deposition from nares to alveolus ([Man, de Steenhuijsen Piters & Bogaert, *Nature Reviews Microbiology* 2017, doi:10.1038/nrmicro.2017.14](https://doi.org/10.1038/nrmicro.2017.14)); the mouth is by contrast high-biomass and saliva-bathed, with anaerobic microniches in the gingival crevice ([Baker et al. 2023](https://doi.org/10.1038/s41579-023-00963-6)). **The claim that this gradient is the differentia rather than merely a property is my synthesis; the individual gradient facts are sourced.**

---

## 4. Sources

All DOIs verified against Crossref on 2026-08-17; ontology terms verified against the EBI OLS4 API and against `data/raw/ontology_terms.tsv` on the same date.

**Source vocabulary (MISO / BacDive)**
- Reimer LC, Sardà Carbasse J, Koblitz J, Ebeling C, Podstawka A, Overmann J. BacDive in 2022: the knowledge base for standardized bacterial and archaeal data. *Nucleic Acids Research* 2022;50(D1):D741–D746. [doi:10.1093/nar/gkab961](https://doi.org/10.1093/nar/gkab961) — PMID 34718743, [PMC8728306](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728306). *387 MISO terms on three levels; tags are hierarchical paths.*
- Reimer LC, et al. BacDive in 2019. *Nucleic Acids Research* 2019;47(D1):D631–D636. [PMC6323973](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/). *MISO named as a 376-term three-level controlled vocabulary; introduction of the Microbial Isolation Source Search.*
- Schober I, et al. BacDive in 2025: the core database for prokaryotic strain data. *Nucleic Acids Research* 2025;53(D1):D748–D756. [doi:10.1093/nar/gkae959](https://doi.org/10.1093/nar/gkae959).
- BacDive isolation sources browser: <https://bacdive.dsmz.de/isolation-sources> (live tree parsed 2026-08-17 — source of the Cat1/Cat2/Cat3 structure and both duplicate nodes). Example tagged strain record: [BacDive ID 2601](https://bacdive.dsmz.de/pdf/2601?doi=10.13145%2Fbacdive2601.20191129.4.1).
- Note on MISO's status: it is characterised in the literature as a non-aligned in-house classification, alongside GOLD's — [Dérozier et al., *PLoS ONE* 2023, Omnicrobe, doi:10.1371/journal.pone.0272473](https://doi.org/10.1371/journal.pone.0272473).

**Ontologies / standards**
- Buttigieg PL, et al. The environment ontology in 2016. *Journal of Biomedical Semantics* 2016;7:57. [doi:10.1186/s13326-016-0097-6](https://doi.org/10.1186/s13326-016-0097-6).
- `ENVO:2100000`, `ENVO:08000002`, `ENVO:2100002`, `ENVO:2100003`, `ENVO:01001033` — <https://www.ebi.ac.uk/ols4/ontologies/envo>.
- `UBERON:0001005`, `UBERON:0001557`, `UBERON:0000065`, `UBERON:0000165`, `UBERON:0000167`; `BTO:0006487`; `NCIT:C82347` — <https://www.ebi.ac.uk/ols4>.
- Yilmaz P, et al. MIMARKS and MIxS specifications. *Nature Biotechnology* 2011;29:415–420. [doi:10.1038/nbt.1823](https://doi.org/10.1038/nbt.1823). *MIxS environmental packages; the human-associated family is `human-associated`, `human-gut`, `human-oral`, `human-skin`, `human-vaginal` — note there is **no** `human-airway` or combined oral+airway package. Current package list: <https://genomicsstandardsconsortium.github.io/mixs/>.*
- Human Microbiome Project Consortium. Structure, function and diversity of the healthy human microbiome. *Nature* 2012;486:207–214. [doi:10.1038/nature11234](https://doi.org/10.1038/nature11234). *HMP sampled the oral cavity (9 sites) and the anterior nares as **separate** body-site groups — precedent against merging.*

**Primary and review literature on the habitat**
- Baker JL, Mark Welch JL, Kauffman KM, McLean JS, He X. The oral microbiome: diversity, biogeography and human health. *Nature Reviews Microbiology* 2023;21:89–104. [doi:10.1038/s41579-023-00963-6](https://doi.org/10.1038/s41579-023-00963-6).
- Man WH, de Steenhuijsen Piters WAA, Bogaert D. The microbiota of the respiratory tract: gatekeeper to respiratory health. *Nature Reviews Microbiology* 2017;15:259–270. [doi:10.1038/nrmicro.2017.14](https://doi.org/10.1038/nrmicro.2017.14).
- Bassis CM, et al. Analysis of the upper respiratory tract microbiotas as the source of the lung and gastric microbiotas in healthy individuals. *mBio* 2015;6(2):e00037-15. [doi:10.1128/mBio.00037-15](https://doi.org/10.1128/mBio.00037-15).
- Dickson RP, et al. Bacterial topography of the healthy human lower respiratory tract. *mBio* 2017;8(1):e02287-16. [doi:10.1128/mBio.02287-16](https://doi.org/10.1128/mBio.02287-16).
- Dickson RP, Erb-Downward JR, Huffnagle GB. The lung microbiome: new principles for respiratory bacteriology in health and disease. *PLoS Pathogens* 2015;11(7):e1004923. [doi:10.1371/journal.ppat.1004923](https://doi.org/10.1371/journal.ppat.1004923).
- Segal LN, et al. Enrichment of the lung microbiome with oral taxa is associated with lung inflammation of a Th17 phenotype. *Nature Microbiology* 2016;1:16031. [doi:10.1038/nmicrobiol.2016.31](https://doi.org/10.1038/nmicrobiol.2016.31).
- Escapa IF, Chen T, Huang Y, Gajare P, Dewhirst FE, Lemon KP. New insights into human nostril microbiome from the expanded Human Oral Microbiome Database (eHOMD): a resource for the microbiome of the human aerodigestive tract. *mSystems* 2018;3(6):e00187-18. [doi:10.1128/mSystems.00187-18](https://doi.org/10.1128/mSystems.00187-18) — PMID 30534599.
- Mark Welch JL, Rossetti BJ, Rieken CW, Dewhirst FE, Borisy GG. Biogeography of a human oral microbiome at the micron scale. *PNAS* 2016;113(6):E791–E800. [doi:10.1073/pnas.1522149113](https://doi.org/10.1073/pnas.1522149113).
- Garmendia J, et al. Environmental exposures, the oral–lung axis and respiratory health. *Microbial Biotechnology* 2024;17(6):e14506. [doi:10.1111/1751-7915.14506](https://doi.org/10.1111/1751-7915.14506).
- Oral microbiota and respiratory diseases: advances and perspectives. *Clinical Microbiology Reviews* 2025. [doi:10.1128/cmr.00150-24](https://doi.org/10.1128/cmr.00150-24) — PMID 40172191.

**Non-human hosts**
- Zeineldin M, Lowe J, Aldridge B. Contribution of the mucosal microbiota to bovine respiratory health. *Trends in Microbiology* 2019;27(9):753–770. [doi:10.1016/j.tim.2019.04.005](https://doi.org/10.1016/j.tim.2019.04.005).
- Barbosa EV, et al. *Ornithobacterium rhinotracheale*: an update review about an emerging poultry pathogen. *Veterinary Sciences* 2020;7(1):3. [doi:10.3390/vetsci7010003](https://doi.org/10.3390/vetsci7010003).

**Repo-internal evidence (not external claims):** `data/habitats/other/oral_cavity_and_airways.yaml` (2,102 strains / 881 taxa; characteristic taxa), `data/raw/bacdive_isolation_sources.tsv` (163 of ~317 MISO nodes present), `data/habitats/host_associated/respiratory_airway.yaml`, `data/habitats/other/mouth_environment.yaml`, `data/habitats/host_associated/bronchus.yaml`, `data/habitats/clinical/tracheal_aspirate.yaml`.

---

## 5. Synonyms, and what not to conflate

**Names in real use for approximately this concept**
- *aerodigestive tract* / *upper aerodigestive tract* — the closest established name (`NCIT:C82347`, `BTO:0006487`; [Escapa et al. 2018](https://doi.org/10.1128/mSystems.00187-18) uses it for exactly this microbiome scope). Caveat: it conventionally includes the oesophagus and stops at the larynx or trachea.
- *oral–respiratory tract*, *oral–lung axis* (the last names the *relationship*, not the place — see below)
- *upper respiratory tract* in loose clinical usage, which often silently includes the mouth; the ontology definitions do not (`UBERON:0001557` starts at the nose; `NCIT:C33839` "Upper Respiratory System" lists nares, nasopharynx, oropharynx, larynx, vocal cords, glottis, upper trachea — no oral cavity)
- BacDive/MISO surface forms: `#Oral cavity and airways`, `#Oral cavity and Airways`

**Commonly but wrongly treated as the same thing**
- **`UBERON:0001005` respiratory airway** — a *child* here (MISO `#Airways`) and the identity of an existing HabitatMech record. Adopting it merges parent and child.
- **`ENVO:08000002` mouth environment** — the oral half only; a separate existing record.
- **`#Nose` / nasal cavity / nasopharynx** — anatomically continuous and microbiologically linked, but MISO files `#Nose` under `#Organ`, *not* under this node. Do not fold the nares in.
- **oesophagus / `#Gastrointestinal tract`** — included by the *aerodigestive tract* concept, excluded by MISO's node. This is the single largest reason `BTO:0006487` cannot be a parent.
- **`#Sputum`, `#Saliva`, `#Phlegm`, `#Mucus`, `#Bronchial wash`, `#Tracheal aspirate`, `#Pleural fluid`** — MISO body *products*, under Cat1 `#Host Body Product`. These are materials, not the site; conflating them is precisely the risk created by the duplicate-label collision in §1.3.
- **`#Cystic fibrosis`, `#Tuberculosis`, `#Pneumonia`** — MISO `#Infection` branch. Disease state, not place; `NOT_APPLICABLE` territory per this repo's rules.
- **the oral–lung axis** — a *process* (microaspiration-driven immigration), not a habitat. It is the best evidence for the differentia and must not become the definition.

---

## 6. Should it be a term at all?

**Yes — but as an explicitly region-level, roll-up habitat, and the record should say so.** It is not a process, a quality, a disease state, or an organism-as-taxon, so none of the corpus's standard non-habitat dispositions apply. It is a place: a connected region of a host body from which microbial samples are taken, whose treatment as a single ecological unit is independently supported by eHOMD's aerodigestive-tract scope and by the microaspiration literature. Per this repo's own rule, these are host *parts*, so anatomy-style grounding is the right instinct here — the obstacle is only that no ontology has minted the composite.

Three honest qualifications a curator should carry into the record, in descending order of importance:

1. **Resolve the duplicate-label collision first (§1.3).** If the 2,102 strains merge MISO node 41 (site) with node 47 (body product), the record is a merge of two source concepts and no single definition is true of it — `#Pleural fluid` is not in the oral-airway lumen. The cleanest outcome is a split upstream in the extraction; failing that, define reading (A) and record the contamination in the note. This is the one finding that could change the disposition from "term request" to "fix the extraction".
2. **It is a roll-up, and its assertion volume is an aggregate (§1.2).** Ranking it #1 in a curation backlog by 2,102 strains overstates it relative to a genuine leaf site — the count double-counts strains already attributable to `#Mouth`, `#Plaque`, `#Airways` etc. Worth a line in the note so the number is not later read as 2,102 distinct region-level samples.
3. **Host scope is vertebrate, not human (§1.4).** A definition that says "human" is contradicted by the record's own top-25 taxa.

**Recommended record shape** (all targets verified present in the vendored slice, with labels as quoted):

- `grounding_status: UNGROUNDED` — unchanged; the existing curation note is correct and should be extended with the node-41/47 finding rather than replaced
- `parent_habitats: [ENVO:2100000]` with `relation: parent` — "anatomical entity environment"; genuinely broader, already the parent of `mouth_environment.yaml`
- `BTO:0006487` "aerodigestive tract" with `relation: xref` — overlapping, not broader; the closest named concept
- `ENVO:08000002` "mouth environment" with `relation: xref` — a proper part, so not a parent under this repo's *broader-only* rule
- **Do not attach `UBERON:0001005`** in any role; the merge risk with `respiratory_airway.yaml` is exactly what the original note flagged
- The record's `habitat_category: OTHER` tracks the grounding ontology rather than the biology (`mouth_environment` is OTHER, `respiratory_airway` is HOST_ASSOCIATED). Worth a curator decision, but it is a corpus-wide convention question, not specific to this term.

If this is taken forward as an ENVO term request — `oral cavity and airways environment`, following the `mouth environment` / `skin environment` pattern under `ENVO:2100000` — note that submitting anything externally needs your explicit per-request go-ahead; nothing here has been sent anywhere.

## Citations

1. https://doi.org/10.1093/nar/gkab961
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/
3. https://bacdive.dsmz.de/pdf/2601?doi=10.13145%2Fbacdive2601.20191129.4.1
4. https://bacdive.dsmz.de/isolation-sources
5. https://doi.org/10.3390/vetsci7010003
6. https://doi.org/10.1016/j.tim.2019.04.005
7. https://doi.org/10.1128/mBio.00037-15
8. https://doi.org/10.1128/mBio.02287-16
9. https://doi.org/10.1371/journal.ppat.1004923
10. https://doi.org/10.1111/1751-7915.14506
11. https://doi.org/10.1128/cmr.00150-24
12. https://doi.org/10.1128/mSystems.00187-18
13. https://doi.org/10.1038/nmicrobiol.2016.31
14. https://doi.org/10.1073/pnas.1522149113
15. https://doi.org/10.1038/s41579-023-00963-6
16. https://doi.org/10.1038/nrmicro.2017.14
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC8728306
18. https://doi.org/10.1093/nar/gkae959
19. https://doi.org/10.1371/journal.pone.0272473
20. https://doi.org/10.1186/s13326-016-0097-6
21. https://www.ebi.ac.uk/ols4/ontologies/envo
22. https://www.ebi.ac.uk/ols4
23. https://doi.org/10.1038/nbt.1823
24. https://genomicsstandardsconsortium.github.io/mixs/
25. https://doi.org/10.1038/nature11234