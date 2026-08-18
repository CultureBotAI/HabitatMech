---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T01:25:05.144651'
end_time: '2026-08-18T01:41:13.945368'
duration_seconds: 968.8
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Spot-Leaf,Stem
  habitat_identifier: habitatmech:BACDIVE.31392c69b9
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Spot-Leaf,Stem'
  assertions: '5'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Cohort
    review: a leaf-or-stem lesion. PO:0009047 ''stem'' drops the leaf and is also
    the target of ''Rot-Root,Stem'', so adopting it would merge two different plant
    diseases onto one record. (source concept habitatmech:BACDIVE.31392c69b9)'
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
  num_turns: 62
  total_cost_usd: 4.4172745
  session_id: 7c312bd3-87c0-4efb-94f6-961eab1f01ff
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 18
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Spot-Leaf,Stem
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.31392c69b9
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Spot-Leaf,Stem
- **Upstream assertion volume:** 5
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Cohort review: a leaf-or-stem lesion. PO:0009047 'stem' drops the leaf and is also the target of 'Rot-Root,Stem', so adopting it would merge two different plant diseases onto one record. (source concept habitatmech:BACDIVE.31392c69b9)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Spot-Leaf,Stem** as a microbial habitat, with citations.

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

# Novel-term research: **Spot-Leaf,Stem** (`habitatmech:BACDIVE.31392c69b9`)

> **A plant-part-associated environment (ENVO:01001057) which is a discrete, margin-delimited necrotic or chlorotic lesion in the leaf lamina or stem of a living plant, formed by a localized infection that does not spread systemically through the host.**

**Bottom line:** this *is* a habitat — a physical, sampleable region of plant tissue, not a disease or a process — but no ontology in ENVO, UBERON, FOODON, BTO or PO names it, and no ontology anywhere names a plant lesion as a material entity. The `CONFIRM_UNGROUNDED` decision on the record is correct, and the evidence below strengthens it: the reason PO:0009047 `stem` is wrong is not only the collision the note records, it is that **BacDive itself models the leaf and the stem as separate concepts elsewhere in the same vocabulary**, so this label was never meant to denote an organ. The concept is a term-request candidate, and it needs a shared parent that does not yet exist.

---

## 1. What the concept denotes

### The source path is decisive

BacDive classifies isolation sources with the Microbial Isolation Source Ontology (MISO), "hierarchically ordered into three levels of tags (category 1–3)" ([Reimer et al., *Nucleic Acids Research* 47:D631, 2019, doi:10.1093/nar/gky879](https://doi.org/10.1093/nar/gky879)). I resolved the live hierarchy from <https://bacdive.dsmz.de/isolation-sources> (fetched 2026-08-18); the term carries `data-id="347"`, `data-parent-ids=",67,"`, `data-cat1-ids=",3,"`, which resolves to:

> **`#Infection` → `#Plant infections` → `#Spot (Leaf,Stem)`**

Its seven siblings under `#Plant infections` are `#Canker`, `#Coloration/Discoloration`, `#Deformation (Broom)`, `#Gall`, `#Lesion (incl. Necrosis)`, `#Rot (Root,Stem)`, `#Wilt`.

Critically, the *organs* live on a different branch of the same vocabulary — `#Host Body-Site` → `#Plant` → `#Leaf (Phyllosphere)` (id 239), `#Stem (Branch)` (id 245), `#Root (Rhizome)` (id 243), `#Sterilized plant part` (id 302). BacDive already had a way to say "leaf" and "stem"; when a curator chose `#Spot (Leaf,Stem)` they were saying **"the lesion", not "the organ"**. The label's parenthetical "(Leaf,Stem)" restricts *where the lesion is*, it does not name the sampled organ.

### The reading

The sample is a **discrete diseased patch of aerial plant tissue** — the necrotic/chlorotic spot itself plus the immediately surrounding water-soaked or chlorotic halo — excised from a leaf blade or a green stem and used to isolate the resident bacteria. In practice this is the standard phytobacteriology isolation procedure: cut lesion margin tissue, macerate, plate.

**Inside the concept:** individual bounded spots on leaves; the same lesion type when it occurs on a herbaceous stem or petiole; the water-soaked halo and lesion margin, which is where viable bacteria are concentrated.

**Neighbouring concepts, explicitly outside:**

| Neighbour | BacDive term | Why it is not this |
|---|---|---|
| Healthy leaf surface / interior | `#Leaf (Phyllosphere)` (500 strains in the HabitatMech extract) | No disease; different community and nutrient regime |
| Healthy stem | `#Stem (Branch)` — pinned to `PO:0009047` by the upstream mapping table | The organ, not a lesion in it |
| Soft/dry decay of fleshy tissue | `#Rot (Root,Stem)` | Maceration of the whole organ, not a bounded spot |
| Sunken necrosis of woody stem/bark | `#Canker` | Perennial, woody, sunken; spots are superficial and self-limiting |
| Hyperplastic outgrowth | `#Gall` | Tissue proliferation, not necrosis |
| Systemic vascular disease | `#Wilt` | Occupies xylem throughout the plant; spots are non-systemic |
| Coalesced spots covering large foliage areas | `#Lesion (incl. Necrosis)` — and, in the literature, "blight" | Once spots merge the bounded-spot geometry is gone |

That last boundary is the one the plant-pathology literature draws explicitly: leaf spots are "discrete diseased sections of leaves that initially appear water-soaked, but later turn yellow, brown, or black… usually angular in shape and bordered by the veins in the leaf," and "merging of numerous leaf spots results in infection of large portions of the foliage — symptoms called **blights**" ([UC IPM Pest Management Guidelines: Floriculture and Ornamental Nurseries, UC ANR Publication 3392, "Bacterial Leaf Spots, Blights, Cankers, and Rots," Koike, Tjosvold & Mathews, text updated 11/2020](https://ipm.ucanr.edu/agriculture/floriculture-and-ornamental-nurseries/bacterial-leaf-spots-blights-cankers-and-rots/)).

### Ambiguity — one real one

The label is **not** ambiguous as to symptom type; "spot" is a well-defined symptom class. It *is* under-specified in two ways a definition should acknowledge rather than resolve:

1. **Causal agent is not fixed.** BacDive's parent is `#Infection`, so the vocabulary asserts an infection, but bacterial, fungal and oomycete leaf spots are all spots. The record's own taxa are bacterial, but the concept as defined by the source is agent-agnostic. *Do not* write "bacterial" into the definition — that would over-claim relative to the source.
2. **"Leaf,Stem" is a disjunction, not a conjunction.** A given sample is a spot on a leaf *or* on a stem. This is exactly why `PO:0009047 stem` is not a defensible grounding: it silently drops the leaf disjunct.

---

## 2. Genus — the broader kind

### Recommended genus: `ENVO:01001057` — *environment associated with a plant part or small plant*

Definition: "An environmental system determined by part of a living or dead plant, or a whole small plant." (retrieved from OLS4, <https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001057>)

This is the smallest well-established kind that fits. A spot lesion is a *part of a part* of a living plant, and the environmental system it determines is exactly what is sampled. It is also already in use in this corpus — `data/habitats/other/part_of_plant.yaml`, `root_rhizome.yaml` and `sterilized_plant_part.yaml` all carry it as `parent_habitats` — so adopting it as genus is consistent rather than novel.

The next term up, `ENVO:01001001` *plant-associated environment* ("An environmental system determined by a green plant"), is also true but is a weaker genus: it would put the lesion at the same level as the whole rhizosphere.

### Near-misses, and why each fails

**`PO:0009047` *stem*** — the upstream lexical mapping (`data/raw/isolation_source_groundings.tsv`, method `ols4_search_synonym`, confidence *medium*). It fails three ways, one more than the record's note captures:
- it drops the leaf disjunct;
- the *same* PO term is the lexical target for `Rot-Root,Stem`, so adopting it merges two distinct plant diseases (as the note says);
- and it is additionally the **`skos:exactMatch`, high-confidence, manually curated** target for `Stem-Branch` in the same mapping table. Grounding here would collide the lesion with the healthy organ that BacDive deliberately models separately.

**`PO:0025034` *leaf*** — same failure, mirrored: drops the stem disjunct, and denotes the healthy organ.

**`ENVO:01000170` *indeterminate root nodule infection zone*** — the closest structural precedent anywhere in ENVO, and worth recording: ENVO *does* model a plant infection zone as an environment ("A part of an indeterminate root nodule permeated with infection threads full of bacteria…"). But it is a *symbiotic*, organogenic structure on a root, far narrower than and disjoint from a foliar necrotic lesion. It is a template for the term request, not a match.

**`ENVO:01001121` *plant matter*** / **`ENVO:01000628` *plant litter*** — plant matter is "Organic material which is primarily composed of plant structures, living or dead," and litter is detached dead material. A spot is attached to and metabolically continuous with a living host; the litter reading loses the host.

**`ENVO:01001032` *environment determined by a biofilm on a plant surface*** — asserts a surface biofilm. Spot-forming bacteria are predominantly *apoplastic* (intercellular), not epiphytic; see §3. Over-claims.

**No ENVO term for lesion, wound, or diseased tissue exists.** OLS4 searches of ENVO for `lesion`, `wound`, `diseased` and `infected plant tissue` return nothing relevant (queries run 2026-08-18 against <https://www.ebi.ac.uk/ols4/api/search>).

**Outside the five ontologies HabitatMech grounds to** — all of these are the *wrong kind of entity* and none should be adopted, but they are worth recording as xref candidates:

- **`PSO:0000034` *maize bacterial leaf spot disease*** and ~20 sibling `PSO:*` leaf-spot terms (Plant Stress Ontology, "describes biotic and abiotic stresses that a plant may encounter"). These are **diseases**, host-specific, not sites.
- **`TO:0002702` *Cercospora leaf spot response*, `TO:0000422` *rice narrow brown leaf spot disease response*** etc. (Plant Trait Ontology). These are **plant traits/responses** — qualities of the host, not places.
- **`PECO:0007060` *Sphaerulina oryzina exposure*** (Plant Experimental Conditions Ontology). An **experimental treatment**, not a habitat.
- **`SYMP:0019178` *necrotic lesion*, `NCIT:C36123` *Necrotic Lesion*** — human/animal clinical symptom terms; wrong kingdom and, in SYMP's case, a symptom rather than a material entity.
- **AGROVOC `c_12119` *leaf spots*** — the only controlled vocabulary that names the concept at all. Its broader chain is `leaf spots` → `spots` (`c_7329`) → `plant diseases` (`c_5962`) (resolved via <https://agrovoc.fao.org/browse/rest/v1/agrovoc/data?uri=http://aims.fao.org/aos/agrovoc/c_12119>). So AGROVOC classes it as a **disease**, not a place — which is a good xref and a bad parent.

---

## 3. Differentia — what distinguishes it

Ordered by how observable each property is. Sibling contrasts in brackets.

**a. Geometry: bounded, margin-delimited, self-limiting.** Circular to angular necrotic lesions with a yellow halo and water-soaking, angular because spread is restricted by the leaf's major veins in net-veined dicots; discrete rather than confluent. Once they coalesce they are called blights ([UC IPM UC ANR 3392](https://ipm.ucanr.edu/agriculture/floriculture-and-ornamental-nurseries/bacterial-leaf-spots-blights-cankers-and-rots/); [Zhao et al., "Bacterial Leaf Spot Diseases of Leafy Crucifers in Oklahoma Caused by Pathovars of *Xanthomonas campestris*," *Plant Disease* 84:1008, 2000, doi:10.1094/PDIS.2000.84.9.1008](https://doi.org/10.1094/PDIS.2000.84.9.1008)). [vs. `#Lesion (incl. Necrosis)`, blight]

**b. Non-systemic.** This is the sharpest separator from `#Wilt` and from vascular disease generally, and it is documented at pathovar resolution in the same host: *X. campestris* pv. *raphani* (syn. pv. *armoraciae*) strains "enter through stomata and cause infection of the parenchyma" and **always produce leaf spots**, whereas pv. *campestris* invades hydathodes and wounds and moves systemically through the vascular system to cause black rot ([Vicente & Holub, "*Xanthomonas campestris* pv. *campestris* … in the genomic era is still a worldwide threat to brassica crops," *Molecular Plant Pathology* 14:2–18, 2013, doi:10.1111/j.1364-3703.2012.00833.x](https://doi.org/10.1111/j.1364-3703.2012.00833.x); [Zhao et al. 2000](https://doi.org/10.1094/PDIS.2000.84.9.1008)). Note this also means the *taxon* alone does not tell you the habitat — pathovar does.

**c. Dominant material: intercellular space (apoplast) of parenchyma, not the leaf surface.** This is the property that makes the lesion a genuinely different microbial habitat rather than "a leaf that looks bad." Foliar pathogens actively remodel the apoplast: *Xanthomonas hortorum* pv. *gardneri* "can deploy its type III secretion system to manipulate the host into leaking cellular constituents into this space, creating an aqueous environment," via the effector AvrHah1, which upregulates a host pectate lyase and degrades the pectin cement between cells ([Dixon et al., "*Xanthomonas* Infection Transforms the Apoplast into an Accessible and Habitable Niche for *Salmonella enterica*," *Applied and Environmental Microbiology* 88:e01330-22, 2022, doi:10.1128/aem.01330-22](https://doi.org/10.1128/aem.01330-22), PMID 36314834).

**d. Characteristic physicochemistry: free water and liberated nutrients.** The same paper shows the transformation is habitat-forming in the strongest sense — a non-phytopathogen, *S. enterica*, achieves "near 4-log population growth within 3 days of arrival on *X. hortorum* pv. *gardneri*-infected leaves," because infection "aids in overcoming the host immune response and/or liberates nutrients inaccessible to *S. enterica*" ([Dixon et al. 2022](https://doi.org/10.1128/aem.01330-22)). Water-soaking as an engineered apoplast condition is independently quantified for *P. syringae* ([Aung et al. / Beattie group, "A method for quantitation of apoplast hydration in Arabidopsis leaves reveals water-soaking activity of effectors of *Pseudomonas syringae* during biotrophy," *Scientific Reports* 12, 2022, doi:10.1038/s41598-022-22472-x](https://doi.org/10.1038/s41598-022-22472-x)).

**e. A community distinct from adjacent healthy tissue — and spatially zoned.** Three independent studies, three pathosystems:
- **Maize white spot:** the leaf microbiome was compared at the *infection site*, the *area in proximity to the spot*, and *healthy area*; late-stage disease and proximity to the spot raised bacterial alpha diversity relative to healthy tissue while fungal alpha diversity fell ([Jibril et al., *Biomolecules* 15:252, 2025, doi:10.3390/biom15020252](https://doi.org/10.3390/biom15020252)).
- **Angular leaf spot of cucumber:** samples binned by lesion coverage (mild/moderate/severe) differ significantly in α-diversity and community structure, with the lowest biodiversity at the intermediate stage; communities dominated by Proteobacteria, Actinobacteria and Firmicutes ([Luo et al., *AMB Express* 9:76, 2019, doi:10.1186/s13568-019-0800-y](https://doi.org/10.1186/s13568-019-0800-y), PMID 31134393).
- **Leaf spot of *Leymus chinensis*:** significant compositional differences between healthy and diseased leaves ([Qian et al., *Plants* 13:2128, 2024, doi:10.3390/plants13152128](https://doi.org/10.3390/plants13152128)).

Note the maize and cucumber results point in opposite directions on diversity in some comparisons, and the maize paper itself flags conflicting results across pathosystems. **The defensible claim is "distinct from healthy tissue," not "more diverse than healthy tissue."** Do not put a direction into the definition.

**f. Type-strain provenance confirms the sampling practice.** *Pseudomonas floridensis* GEV388ᵀ — one of the four taxa on this record — was described from "tomato exhibiting leaf spot symptoms similar to bacterial speck" ([Timilsina et al., *Int J Syst Evol Microbiol* 68:64–70, 2018, doi:10.1099/ijsem.0.002445](https://doi.org/10.1099/ijsem.0.002445), PMID 29148362). The same isolation practice underlies e.g. *Pseudomonas fragariae*, described from strawberry leaf spots (PMID 39141420).

---

## 4. Sources

Grouped by what they support. Everything below is either a resolvable primary/standards source or an inspection of the repo/source data I performed directly.

**BacDive vocabulary and the source path**
- Reimer LC, Vetcininova A, Sardà Carbasse J, et al. BacDive in 2019: bacterial phenotypic data for high-throughput biodiversity analysis. *Nucleic Acids Research* 47(D1):D631–D636 (2019). doi:[10.1093/nar/gky879](https://doi.org/10.1093/nar/gky879) — establishes the MISO three-level tag system and the eight category-1 classes.
- Live hierarchy: <https://bacdive.dsmz.de/isolation-sources> (fetched 2026-08-18). The parent-id resolution (`347` → `67` `#Plant infections` → cat1 `3` `#Infection`; and `#Leaf (Phyllosphere)` 239 / `#Stem (Branch)` 245 under cat1 `5` `#Host Body-Site` → `#Plant` 42) is **my parse of that page's DOM**, not something BacDive states in prose. It is reproducible but the curator should be aware it is a derivation.
- Schober I, Koblitz J, Sardà Carbasse J, et al. BacDive in 2025: the core database for prokaryotic strain data. *Nucleic Acids Research* 53(D1):D748 (2025). <https://academic.oup.com/nar/article/53/D1/D748/7848838>

**Symptom definition and sibling boundaries**
- Koike ST, Tjosvold SA, Mathews DM. Bacterial Leaf Spots, Blights, Cankers, and Rots. *UC IPM Pest Management Guidelines: Floriculture and Ornamental Nurseries*, UC ANR Publication 3392, text updated 11/2020. <https://ipm.ucanr.edu/agriculture/floriculture-and-ornamental-nurseries/bacterial-leaf-spots-blights-cankers-and-rots/>
- Zhao Y, Damicone JP, Demezas DH, Rangaswamy V, Bender CL. Bacterial leaf spot diseases of leafy crucifers in Oklahoma caused by pathovars of *Xanthomonas campestris*. *Plant Disease* 84:1008–1014 (2000). doi:[10.1094/PDIS.2000.84.9.1008](https://doi.org/10.1094/PDIS.2000.84.9.1008)
- Vicente JG, Holub EB. *Xanthomonas campestris* pv. *campestris* (cause of black rot of crucifers) in the genomic era is still a worldwide threat to brassica crops. *Molecular Plant Pathology* 14:2–18 (2013). doi:[10.1111/j.1364-3703.2012.00833.x](https://doi.org/10.1111/j.1364-3703.2012.00833.x)
- *Not retrieved:* the APS *Illustrated Glossary of Plant Pathology* (apsnet.org returns 403) and Agrios, *Plant Pathology*, 5th ed. (2005). If the curator wants a canonical one-line glossary definition in the term's `notes`, one of these is the source to check by hand; I did **not** verify their exact wording and no wording from them appears above.

**The lesion as a microbial habitat**
- Dixon MH, Cowles KN, Zaacks SC, Marciniak IN, Barak JD. *Xanthomonas* infection transforms the apoplast into an accessible and habitable niche for *Salmonella enterica*. *Applied and Environmental Microbiology* 88(22):e01330-22 (2022). doi:[10.1128/aem.01330-22](https://doi.org/10.1128/aem.01330-22), PMID 36314834.
- Beattie GA group. A method for quantitation of apoplast hydration in *Arabidopsis* leaves reveals water-soaking activity of effectors of *Pseudomonas syringae* during biotrophy. *Scientific Reports* 12 (2022). doi:[10.1038/s41598-022-22472-x](https://doi.org/10.1038/s41598-022-22472-x)
- Jibril SM, et al. Microbiome analysis of area in proximity to white spot lesions reveals more harmful plant pathogens in maize. *Biomolecules* 15(2):252 (2025). doi:[10.3390/biom15020252](https://doi.org/10.3390/biom15020252)
- Luo J, et al. Variations in phyllosphere microbial community along with the development of angular leaf-spot of cucumber. *AMB Express* 9:76 (2019). doi:[10.1186/s13568-019-0800-y](https://doi.org/10.1186/s13568-019-0800-y), PMID 31134393.
- Qian D, et al. Effects of grazing and leaf spot disease on the structure and diversity of phyllosphere microbiome communities in *Leymus chinensis*. *Plants* 13(15):2128 (2024). doi:[10.3390/plants13152128](https://doi.org/10.3390/plants13152128)
- Timilsina S, Minsavage GV, Preston J, et al. *Pseudomonas floridensis* sp. nov., a bacterial pathogen isolated from tomato. *Int J Syst Evol Microbiol* 68:64–70 (2018). doi:[10.1099/ijsem.0.002445](https://doi.org/10.1099/ijsem.0.002445), PMID 29148362.

**Ontology / standards checks (all run 2026-08-18)**
- ENVO term records via OLS4: `ENVO:01001057`, `ENVO:01001001`, `ENVO:01000170`, `ENVO:01001121`, `ENVO:01001031`, `ENVO:01001032` — <https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/>
- Negative searches (no hits): ENVO for `lesion`, `wound`, `diseased`, `infected plant tissue`; all-of-OLS for `plant lesion` and `diseased plant tissue`.
- AGROVOC `c_12119` *leaf spots* and its broader chain — <https://agrovoc.fao.org/browse/rest/v1/agrovoc/c_12119>
- GSC MIxS / NCBI BioSample MIMS plant-associated package v6.0 — <https://www.ncbi.nlm.nih.gov/biosample/docs/packages/MIMS.me.plant-associated.6.0/> — `plant structure (plant_struc)`: "Name of plant structure the sample was obtained from; for Plant Ontology (PO) … terms"; `host disease (host_disease)`: "Name of relevant disease."

**Repo inspection (my own, stated as such)**
- `data/raw/isolation_source_groundings.tsv`: `Spot-Leaf,Stem` → `PO:0009047` (`skos:closeMatch`, medium, `ols4_search_synonym`); `Rot-Root,Stem` → same target, same method; **`Stem-Branch` → `PO:0009047`, `skos:exactMatch`, high, `semapv:ManualMappingCuration`, `kg_review_promote`**. The third of these is the collision the existing curation note does not mention.
- `data/habitats/other/{part_of_plant,root_rhizome,sterilized_plant_part}.yaml` already carry `ENVO:01001057` in `parent_habitats`.
- Sibling records `gall.yaml`, `canker.yaml`, `wilt.yaml` all carry the note "kg-microbe's isolation-source mapping table has a row for this source with no ontology target" and are UNGROUNDED; `rot_root_stem.yaml` is UNGROUNDED/REVIEWED. So the whole `#Plant infections` cohort is ungrounded, consistently.

**Explicit inferences, not sourced claims** — flagged because §4 asks for it:
- That the parenthetical "(Leaf,Stem)" is a *disjunction over lesion location* rather than a compound organ name. This follows from BacDive housing leaf and stem separately under `#Host Body-Site`, but BacDive does not say it.
- That the apoplast is the dominant material of the habitat. Well supported for the bacterial spot pathogens cited, but the source concept is agent-agnostic; a fungal leaf spot's dominant microbial compartment is not the same.
- That *Klebsiella aerogenes* (one of the four taxa on the record) reached a spot lesion as a secondary or opportunistic colonizer rather than as the spot-forming agent. This is a reasonable reading given Dixon et al.'s demonstration that lesions are colonizable by non-phytopathogenic enterobacteria, but **no source ties that specific strain record to that mechanism.** Do not put it in the definition.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- leaf spot; leaf spot lesion; leaf lesion (UC IPM uses "leaf spots (leaf lesions)" as a gloss)
- bacterial leaf spot lesion; bacterial spot lesion
- angular leaf spot lesion (when vein-delimited)
- stem spot; stem lesion (herbaceous)
- spot lesion tissue; lesion margin tissue (the isolation-practice phrasing)
- AGROVOC: *leaf spots* (`c_12119`)
- BacDive/MISO surface form: `#Spot (Leaf,Stem)`

**Commonly conflated, and wrong**

| Not this | Why |
|---|---|
| `PO:0009047` **stem** / `PO:0025034` **leaf** | The healthy organ. Also already the exact-match target of `Stem-Branch` upstream. |
| **Phyllosphere / phylloplane** (`#Leaf (Phyllosphere)`; `PO:0006016` *leaf epidermis*) | Surface habitat of healthy leaves; separate BacDive concept with 500 strains vs. this one's 5. |
| **Blight / blotch** | Coalesced spots; the bounded geometry that defines "spot" is gone. |
| **Canker** | Sunken necrosis of woody stem/bark, typically perennial. Separate BacDive sibling. |
| **Rot** (`#Rot (Root,Stem)`) | Maceration of fleshy tissue — "a soft, watery decay" (UC IPM). Separate sibling; and the reason PO:0009047 must not be adopted here. |
| **Wilt** | Systemic vascular occupation. Separate sibling, opposite on the non-systemic differentia. |
| **The disease** (`PSO:0000034` and kin; AGROVOC's own placement under *plant diseases*) | A disease is not a place. The lesion is the place the disease produces. |
| **The plant trait / resistance response** (`TO:*` "…disease response") | A quality of the host organism. |
| **The pathogen taxon** (*Xanthomonas campestris*, *Pseudomonas syringae*) | The organism, not its habitat — and pathovar, not species, determines whether the habitat is a spot or a vascular system. |
| **Abiotic leaf spot** (herbicide, ozone, nutrient burn) | Visually similar, no infection. BacDive's cat1 is `#Infection`, so these are outside the concept. |
| **Necrotic lesion** in the clinical sense (`SYMP:0019178`, `NCIT:C36123`) | Human/animal; and a symptom, not a material entity. |

---

## 6. Should this be a term at all?

**Yes — but it needs a parent that does not exist yet, and the record carries two caveats.**

### Why it is a habitat, not a disposition of one

The corpus has an established disposition for concepts that are diseases, qualities, processes or procedures: `NOT_APPLICABLE`. This is *not* one of them, for the same reason `gut` is a habitat while `Mollusca` is not. A spot lesion is a bounded region of material that a sample is physically taken from; it has a dominant material (apoplast and collapsed parenchyma), a characteristic physicochemistry (free water, liberated nutrients, breached pectin cement), and a demonstrably distinct microbial community. [Dixon et al. 2022](https://doi.org/10.1128/aem.01330-22) is the strongest single piece of evidence: it treats the infected apoplast as a *niche* that a bacterium unrelated to the disease can colonize and grow 4 logs in. That is a habitat by any definition this repo uses.

The distinction to hold on to: **the disease is not the habitat; the lesion the disease produces is.** AGROVOC gets this wrong for our purposes by classing "leaf spots" under "plant diseases" — which is exactly why it is an xref and not a parent.

The `parts vs. whole` rule in CLAUDE.md points the same way. A lesion is a *part of a part* of a plant, not a whole organism at a life stage. `Larva` keeps its own identity because it is the whole organism; a spot lesion is not, so the part-of-a-plant genus applies cleanly.

### The missing intermediate class — say this rather than lengthening the sentence

All eight of BacDive's `#Plant infections` children (`Spot`, `Rot`, `Canker`, `Gall`, `Wilt`, `Lesion`, `Deformation`, `Coloration/Discoloration`) are UNGROUNDED in this corpus, all for the same reason: **ENVO has no class for "a site of plant infection as an environment."** ENVO's only instance of the pattern is `ENVO:01000170` *indeterminate root nodule infection zone*, which is symbiotic and root-specific.

The higher-yield term request is therefore **a shared parent** — something like *plant infection site environment* or *diseased plant tissue environment*, subclass of `ENVO:01001057` — with `Spot-Leaf,Stem`, `Rot-Root,Stem`, `Canker`, `Gall` and `Wilt` as siblings under it. Requesting the parent once serves 8 concepts and ~27 strain assertions; requesting five leaf terms with no parent serves five. Recommend filing the parent request first and holding `Spot-Leaf,Stem` as a child of it.

If the curator wants a definition **today**, the one-sentence form at the top works with `ENVO:01001057` as an immediate `parent_habitats` entry and `AGROVOC:c_12119` plus `PO:0009047` as `relation: xref` — capturing what upstream saw without asserting that a lesion *is* a stem.

### Caveats to record on the record

1. **Volume is very low.** 5 strains, 4 taxa. The taxa are `X. campestris` (×2), `P. floridensis`, `P. syringae`, `K. aerogenes`. Three of four are consistent with the reading; the fourth is not a spot-forming phytopathogen and is most plausibly a co-isolate. Do not build the differentia on the taxon list.
2. **The taxon is not the habitat.** `X. campestris` at species rank spans both a leaf-spot pathovar (`raphani`/`armoraciae`) and a vascular black-rot pathovar (`campestris`) ([Vicente & Holub 2013](https://doi.org/10.1111/j.1364-3703.2012.00833.x)). A BacDive strain recorded as `X. campestris` under `#Spot (Leaf,Stem)` tells you the sample was a spot; it does not tell you the pathovar, and the reverse inference does not hold.
3. **Standards model this as two orthogonal fields, not one class.** MIxS/MIMS plant-associated records `plant_struc` (which PO part) and `host_disease` (which disease) separately. A curator could reasonably argue that a habitat class combining organ + disease state is a modelling shortcut. My position is that it is still the right class here — the lesion is a real, distinct, sampleable environment whose properties are not the sum of "leaf" and "has a disease" — but the tension is worth a line in the term request, because it is the objection an ENVO reviewer is most likely to raise.

## Citations

1. https://doi.org/10.1093/nar/gky879
2. https://bacdive.dsmz.de/isolation-sources
3. https://ipm.ucanr.edu/agriculture/floriculture-and-ornamental-nurseries/bacterial-leaf-spots-blights-cankers-and-rots/
4. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001057
5. https://www.ebi.ac.uk/ols4/api/search
6. https://agrovoc.fao.org/browse/rest/v1/agrovoc/data?uri=http://aims.fao.org/aos/agrovoc/c_12119
7. https://doi.org/10.1094/PDIS.2000.84.9.1008
8. https://doi.org/10.1111/j.1364-3703.2012.00833.x
9. https://doi.org/10.1128/aem.01330-22
10. https://doi.org/10.1038/s41598-022-22472-x
11. https://doi.org/10.3390/biom15020252
12. https://doi.org/10.1186/s13568-019-0800-y
13. https://doi.org/10.3390/plants13152128
14. https://doi.org/10.1099/ijsem.0.002445
15. https://academic.oup.com/nar/article/53/D1/D748/7848838
16. https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/
17. https://agrovoc.fao.org/browse/rest/v1/agrovoc/c_12119
18. https://www.ncbi.nlm.nih.gov/biosample/docs/packages/MIMS.me.plant-associated.6.0/