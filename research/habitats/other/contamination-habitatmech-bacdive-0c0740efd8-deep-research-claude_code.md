---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:50:15.979976'
end_time: '2026-08-17T16:59:46.154638'
duration_seconds: 570.17
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Contamination
  habitat_identifier: habitatmech:BACDIVE.0c0740efd8
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Contamination'
  assertions: '474'
  parent_terms: (none)
  xrefs: ENVO:00002204
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term ENVO:00002204 'anthropogenic contamination feature' attached as\
    \ a parent. Risky-grounding review (#12): the seeder made ENVO:00002204 'anthropogenic\
    \ contamination feature' the identity of BacDive's 'Contamination' category \u2014\
    \ the highest-volume risky grounding at 474 strains. The term asserts two things\
    \ BacDive does not: that the contamination is anthropogenic, and that the thing\
    \ is a geographic feature with elevated contaminants in its materials. BacDive's\
    \ category says only that a strain was isolated as a contaminant, which is as\
    \ often of a product, a culture or a cleanroom as of a place. These are different\
    \ concepts rather than a broader and a narrower one, so the term is not a parent\
    \ either \u2014 parent_habitats asserts the parent is BROADER. Kept as an xref\
    \ (#99), which records that upstream saw a connection without this repo asserting\
    \ one. (source concept habitatmech:BACDIVE.0c0740efd8)"
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
  web_search_requests: 13
  num_turns: 40
  total_cost_usd: 3.7939309999999993
  session_id: ae2831ad-9536-4962-9d6e-0a26f277f939
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 23
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Contamination
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.0c0740efd8
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Contamination
- **Upstream assertion volume:** 474
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** ENVO:00002204

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:00002204 'anthropogenic contamination feature' attached as a parent. Risky-grounding review (#12): the seeder made ENVO:00002204 'anthropogenic contamination feature' the identity of BacDive's 'Contamination' category — the highest-volume risky grounding at 474 strains. The term asserts two things BacDive does not: that the contamination is anthropogenic, and that the thing is a geographic feature with elevated contaminants in its materials. BacDive's category says only that a strain was isolated as a contaminant, which is as often of a product, a culture or a cleanroom as of a place. These are different concepts rather than a broader and a narrower one, so the term is not a parent either — parent_habitats asserts the parent is BROADER. Kept as an xref (#99), which records that upstream saw a connection without this repo asserting one. (source concept habitatmech:BACDIVE.0c0740efd8)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Contamination** as a microbial habitat, with citations.

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

# Definition research: **Contamination** (`habitatmech:BACDIVE.0c0740efd8`)

> **Proposed definition:** An environmental material which has elevated levels of one or more contaminants introduced by human activity, relative to comparable material of the same kind.

---

## ⚠️ Read this first: the recorded curation note rests on a factual error about which BacDive tag this is

The note on the record says:

> "BacDive's category says only that a strain was isolated as a contaminant, which is as often of a product, a culture or a cleanroom as of a place."

That is the wrong BacDive tag. BacDive has **two distinct isolation-source tags**, and HabitatMech already has **two distinct records** for them:

| BacDive tag path | Free-text examples | HabitatMech record | Strains |
|---|---|---|---|
| `#Engineered` → `#Contamination` | "soil contaminated with crude oil"; "pesticide (imidacloprid)-contaminated soil"; "sediment cores taken from an uranium-contaminated environment" | `habitatmech:BACDIVE.0c0740efd8` **Contamination** (this record) | 474 |
| `#Engineered` → `#Laboratory` → `#Contaminant` | "contaminant of biopharmaceutical process" | `habitatmech:BACDIVE.4d06ff4bb5` **Contaminant** (`data/habitats/other/contaminant.yaml`) | 61 |

Evidence, from BacDive strain records (the Cat1/Cat2/Cat3 fields are displayed verbatim on each strain page):

- ***Janibacter terrae* DPO 360**, BacDive ID 6251 — isolation source *"soil contaminated with crude oil"*; **Cat1: Engineered · Cat2: Contamination · Cat3: Oil (Fuel)**. <https://bacdive.dsmz.de/strain/6251> *(this is the #1 characteristic taxon on the record, 6 strains)*
- ***Afipia* sp. SG-6C**, BacDive ID 130219 — *"pesticide (imidacloprid)-contaminated soil"*, Canberra, Australia; **Cat1: Engineered · Cat2: Contamination**. <https://bacdive.dsmz.de/strain/130219>
- ***Anaeromyxobacter dehalogenans* FRC-W**, BacDive ID 3758 — *"sediment cores taken from an uranium-contaminated environment"*, Oak Ridge, Tennessee; carries **Engineered/Contamination** alongside **Environmental/Terrestrial/Sediment**. <https://bacdive.dsmz.de/strain/3758> *(#2 characteristic taxon, 6 strains)*
- ***Herminiimonas contaminans*** (DSM 28178), BacDive ID 24261 — *"contaminant of biopharmaceutical process"*; **Cat1: Engineered · Cat2: Laboratory · Cat3: Contaminant** (plus Engineered/Industrial/Engineered product). <https://bacdive.dsmz.de/strain/24261>. Species description: Ala Aldeen *et al.* (2012) *IJSEM*, doi:[10.1099/ijs.0.039073-0](https://doi.org/10.1099/ijs.0.039073-0), PMID [22447701](https://pubmed.ncbi.nlm.nih.gov/22447701/)

The BacDive isolation-source browser confirms the placement structurally: the Category-2 list under Category-1 **Engineered** is *Agriculture, Biodegradation, Biofilm, Bioreactor, Bioremediation, Built environment, **Contamination**, Food production, Industrial, Laboratory, Medical device, Medical environment, Medical product, Treatment, Waste* (<https://bacdive.dsmz.de/isolation-sources>, fetched 2026-08-17).

**Consequence for curation.** The 474 attestations are dominated by *contaminated environmental materials* — polluted soils, sediments, groundwater — not by strains recovered as contaminants of cultures or products. The "as often of a product, a culture or a cleanroom" claim describes the *sibling* record `BACDIVE.4d06ff4bb5` (61 strains). The `NOT_APPLICABLE`-adjacent disposition recorded in `curation/term_requests_excluded.tsv` ("Not a place… a circumstance of sampling rather than an environment ENVO models") should be revisited on that basis.

*Caveat, stated plainly:* one fetch of the isolation-source browser's dropdown returned "Contaminant" and "Sterilized (Desinfected)" as Category-3 options in the same page render as Contamination. The dropdown dump is unreliable (the same render listed "Human", "Patient" and "Oral cavity" as Engineered siblings). The strain-record evidence above is the stronger signal and places Contaminant under Laboratory. If the curator wants certainty on the exact Cat3 child set of Contamination, that requires the BacDive API (registration-gated) rather than the public pages.

---

## 1. What the concept denotes

**As a habitat: a portion of environmental material — soil, sediment, groundwater, sludge, or land — carrying elevated levels of a chemical or radiological contaminant introduced by human activity, from which the strain was isolated.** The contaminant classes attested in the sampled records are petroleum hydrocarbons and coal tar, agricultural pesticides, and radionuclides/metals.

**Inside the concept:** crude-oil-contaminated soil; coal-tar-contaminated soil at former gasworks; PAH-contaminated soil; pesticide-contaminated soil; uranium-contaminated subsurface sediment and groundwater; creosote-, chromate-, solvent-contaminated material.

**Outside the concept (neighbouring concepts, each with its own BacDive tag and, mostly, its own HabitatMech record):**

- `#Engineered > #Laboratory > #Contaminant` — a strain isolated *as* a contaminant of a culture, reagent or product → `habitatmech:BACDIVE.4d06ff4bb5`
- `#Engineered > #Waste` — wastewater, sewage, landfill: material that *is* waste, rather than clean material into which a contaminant has entered
- `#Engineered > #Bioremediation` / `#Biodegradation` — the *treatment process* applied to contaminated material, not the material
- `#Environmental > #Terrestrial > #Soil` — the uncontaminated material identity

**An important structural qualification.** BacDive's category assignments are **multi-valued and cross-cutting**, not a partition. *Anaeromyxobacter dehalogenans* FRC-W carries both `Engineered/Contamination` and `Environmental/Terrestrial/Sediment`. Conversely *Sphingopyxis bauzanensis* BZ30 (BacDive ID 14287), whose free text is literally *"hydrocarbon-contaminated soil"*, carries only `Environmental/Terrestrial/Soil` (<https://bacdive.dsmz.de/strain/14287>). So:

1. `Contamination` functions in BacDive as a **modifier applied alongside a material tag**, naming the contaminated *condition* of the sample rather than its material identity; and
2. the 474 count is a **floor, not a census** — contaminated-material isolations exist in BacDive that were never given this tag.

Both facts belong in the record's notes. Neither prevents the concept from being a habitat class; ENVO itself models `contaminated soil` as a subclass of soil, i.e. as a material bearing a condition.

**Ambiguity that remains.** The label "Contamination" in isolation is genuinely ambiguous across three readings — (a) contaminated environmental material, (b) an organism that is a contaminant, (c) the process of contaminating. Reading (a) is the one this tag means, on the evidence above. Readings (b) and (c) have separate homes: (b) is `BACDIVE.4d06ff4bb5`; (c) is `ENVO:02500036` *environmental pollution*, "An environmental system process that results in the introduction of contaminants into an environment" — a process, and therefore not a habitat.

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:00010483` *environmental material*** — "A material entity which other material entities in an environmental system are primarily or partially composed of." Present in the vendored slice (`data/raw/ontology_terms.tsv`).

**There is no ENVO term for the concept itself.** ENVO has a well-populated set of *contaminated-\<material\>* classes but **no umbrella class over them**:

| CURIE | Label | Why it is not the genus |
|---|---|---|
| `ENVO:00002116` | contaminated soil | **Narrower** — soil only. Concept also covers sediment, groundwater, sludge. Ancestor chain: environmental material → soil → enriched soil → contaminated soil. Already grounded EXACT in the corpus at `terrestrial/contaminated_soil.yaml` (GOLD `contaminated soil`). |
| `ENVO:00003600073` → `ENVO:03600073` | contaminated land | **Narrower** — land only; also carries a hazard-to-health clause the sources do not assert. |
| `ENVO:00002186` / `ENVO:03600001` / `ENVO:01000676` | contaminated water / chemically contaminated sediment / contaminated air | **Narrower** — each fixes one material. |
| `ENVO:00003082` | enriched soil | Soil-specific, and "elevated levels of some material entity" drops the *contaminant* / harm framing entirely. |
| `ENVO:02500036` | environmental pollution | **Wrong kind** — a process, not a material. Cannot be the genus of a habitat. Same for `ENVO:02500038` soil pollution, `ENVO:02500039` water pollution. |
| `ENVO:0010001` | anthropogenic environmental material | "Anthropogenic material in or on which organisms may live." Plausible-looking, but **ENVO itself does not put contaminated soil under it** — contaminated soil descends from soil, not from this class. Adopting it would assert the material *is* anthropogenic in origin; uranium-contaminated sediment is natural sediment that received an anthropogenic input. |
| `ENVO:00002204` | anthropogenic contamination feature | The current xref. **Wrong branch and over-claims** — see below. |

**On `ENVO:00002204` specifically.** Definition: *"An anthropogenic geographic feature which has increased levels of contaminants in its consituent materials."* Its only hierarchical descendant in ENVO is `ENVO:00002061` *oil spill* (checked via OLS4, 2026-08-17). It sits in ENVO's **geographic-feature** branch, structurally separate from the material branch where every *contaminated-\<material\>* class lives. So the existing curation decision — **keep it as `relation: xref`, not as identity and not as parent** — is correct, and correct for a sharper reason than the note gives: ENVO already splits *contaminated site* (feature) from *contaminated material*, and BacDive's tag is applied to materials.

**Recommendation:** this is a real, well-shaped gap in ENVO — a missing intermediate class **"contaminated environmental material"** that would parent `contaminated soil`, `contaminated water`, `contaminated air`, `chemically contaminated sediment`, `contaminated sludge` and `contaminated land`. It is worth recording as a term-request candidate. *(Per the standing rule, no request should be submitted to ENVO without your explicit per-request yes; this is a recommendation only.)* Until such a term exists, `ENVO:00010483` is the honest genus, with the differentia carrying the work.

---

## 3. Differentia — what distinguishes it

Observable, and each traceable to a source:

1. **Elevated concentration of an introduced contaminant** relative to comparable material of the same kind. This is exactly ENVO's own differentia pattern across the family — "Soil which has elevated concentrations of oil" (`ENVO:00002875`), "Land which has elevated levels of some contaminants" (`ENVO:03600073`), "Sediment which contains some chemical contaminant" (`ENVO:03600001`). Measurable directly: e.g. chronically polluted Ogoniland soils at TPH 36,775 ppm (surface) and 14,087 ppm (subsurface) versus 479 ppm in unpolluted control soil, and TOC 5.64%/5.06% versus 1.97% — doi:[10.1007/s11356-024-33326-6](https://doi.org/10.1007/s11356-024-33326-6) (Environ Sci Pollut Res, 2024).
2. **Anthropogenic origin of the contaminant** (not of the material). Supported by BacDive's placement of the tag under Cat1 `#Engineered` and by every sampled free text (crude oil, coal tar, pesticide, uranium mill/processing residue). *This is an inference from tag placement plus attested instances; BacDive publishes no prose definition of the tag.* If you prefer not to make the claim, drop "introduced by human activity" — "elevated levels of one or more contaminants" alone is fully supported.
3. **The contaminant, not the material, is the ecological selector.** Contaminated materials support communities enriched in catabolically specialised taxa: in nine oil-contaminated oilfield soils, *Alkanindiges, Arthrobacter, Pseudomonas, Mycobacterium* and *Rhodococcus* were detected across all samples, most dominant genera being phylogenetically related to known oil degraders — PMID [26025169](https://pubmed.ncbi.nlm.nih.gov/26025169/). Redox-stratified degrader guilds in crude-oil-contaminated saline soil: PMID [34890619](https://pubmed.ncbi.nlm.nih.gov/34890619/).
4. **The material identity is inherited, not fixed by this class** — soil, sediment, groundwater and sludge all occur. This is what distinguishes the concept from each of the `contaminated <material>` ENVO terms and is why it needs its own identity rather than grounding to any of them.
5. **Co-selection via altered nutrient stoichiometry**, not only direct catabolism: high TPH loading depletes bioavailable nitrogen and enriches nitrogen-transforming taxa (*Solirubrobacter*, Ca. *Udaeobacter*, *Bradyrhizobium*, *Sphingomonas*, *Mycobacterium*) — PMID [34890619](https://pubmed.ncbi.nlm.nih.gov/34890619/). Useful as a differentia only if the record later carries mechanism claims; it is not needed in the definition sentence.

**A caution on this record's `characteristic_taxa`, which the curator should not treat as community evidence.** Eight of the record's top genera — *Janibacter, Afipia, Aquabacterium, Acidovorax, Sphingomonas, Rhodococcus, Corynebacterium* and *Propionibacterium*/*Cutibacterium* — appear in Salter *et al.*'s Table 1 of contaminant genera detected in sequenced negative controls (BMC Biology 12:87, 12 Nov 2014, doi:[10.1186/s12915-014-0087-z](https://doi.org/10.1186/s12915-014-0087-z), PMID [25387460](https://pubmed.ncbi.nlm.nih.gov/25387460/)). The kitome mechanism does **not** explain these particular attestations — BacDive holds deposited cultured strains with curator-recorded isolation sources, not amplicon survey reads, and I verified *Afipia* sp. SG-6C's source individually. The overlap instead reflects that these are ubiquitous oligotrophic genera. But it does mean the top-taxa list is a weak discriminator and should not be cited as showing a contamination-specific community.

---

## 4. Sources

**Concept / source vocabulary**
- BacDive isolation-source search and Cat1–Cat3 hierarchy: <https://bacdive.dsmz.de/isolation-sources> (fetched 2026-08-17)
- Reimer *et al.*, "BacDive in 2019: bacterial phenotypic data for High-throughput biodiversity analysis", *Nucleic Acids Res* 47(D1):D631–D636, doi:[10.1093/nar/gky879](https://doi.org/10.1093/nar/gky879), PMID [30256983](https://pubmed.ncbi.nlm.nih.gov/30256983/) — describes the three-level isolation-source classification (Category 1–3)
- Schober *et al.*, "BacDive in 2025: the core database for prokaryotic strain data", *Nucleic Acids Res* 53(D1):D748–D756, 6 Jan 2025, doi:[10.1093/nar/gkae959](https://doi.org/10.1093/nar/gkae959), PMID [39470737](https://pubmed.ncbi.nlm.nih.gov/39470737/) — current release, >100,000 strains
- Strain records cited individually above: BacDive [6251](https://bacdive.dsmz.de/strain/6251), [130219](https://bacdive.dsmz.de/strain/130219), [3758](https://bacdive.dsmz.de/strain/3758), [24261](https://bacdive.dsmz.de/strain/24261), [14287](https://bacdive.dsmz.de/strain/14287), [8499](https://bacdive.dsmz.de/strain/8499)

**Ontology**
- Buttigieg *et al.*, "The environment ontology in 2016", *J Biomed Semantics* 7:57, 23 Sep 2016, doi:[10.1186/s13326-016-0097-6](https://doi.org/10.1186/s13326-016-0097-6), PMID [27664130](https://pubmed.ncbi.nlm.nih.gov/27664130/)
- Term definitions and hierarchy checked via OLS4, 2026-08-17: `ENVO:00002204`, `ENVO:00002116`, `ENVO:00003082`, `ENVO:00010483`, `ENVO:0010001`, `ENVO:01000254`, `ENVO:03600073`, `ENVO:02500036` — <https://www.ebi.ac.uk/ols4/ontologies/envo>. All of these are present in `data/raw/ontology_terms.tsv` with the labels quoted.

**Habitat microbiology**
- Ogoniland chronically polluted soils, culture-dependent + independent: *Environ Sci Pollut Res* (2024), doi:[10.1007/s11356-024-33326-6](https://doi.org/10.1007/s11356-024-33326-6)
- Oil-contaminated oilfield soils, Daqing/Changqing: PMID [26025169](https://pubmed.ncbi.nlm.nih.gov/26025169/)
- Crude-oil-contaminated saline soil, Yellow River Delta: PMID [34890619](https://pubmed.ncbi.nlm.nih.gov/34890619/)
- *Mycolicibacterium frederiksbergense* LB501T from PAH-contaminated soil: *Microbiol Resour Announc* (2020), doi:[10.1128/MRA.00671-20](https://doi.org/10.1128/MRA.00671-20), PMC [PMC7585852](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7585852/)
- Reagent/laboratory contaminant genera: Salter *et al.*, doi:[10.1186/s12915-014-0087-z](https://doi.org/10.1186/s12915-014-0087-z)

**Explicitly my inference, not stated by any source:** (i) that BacDive's Cat1 `#Engineered` placement licenses the "introduced by human activity" clause; (ii) that the tag functions as a cross-cutting modifier rather than a partition class (this is read off the multi-valued assignments on strains 3758 and 14287, not from BacDive documentation); (iii) that the 474 count under-counts contaminated-material isolations in BacDive.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- contaminated environmental material · polluted environmental material
- contaminated site material · impacted media · impacted soil (US regulatory/remediation usage)
- polluted soil / sediment / groundwater (medium-specific instances)
- "contaminated matrix" (analytical-chemistry usage)

**Do NOT conflate with:**

| Confusable | Why it is different |
|---|---|
| **Contaminant** (`habitatmech:BACDIVE.4d06ff4bb5`; BacDive `#Engineered > #Laboratory > #Contaminant`) | An organism recovered *as* an unwanted intruder in a culture, reagent or product. Different tag, different record, different concept. This is the confusion presently recorded in the note. |
| **`ENVO:02500036` environmental pollution** (and soil/water/air pollution) | A *process*. A process is not a habitat. |
| **`ENVO:00002204` anthropogenic contamination feature** | A *geographic feature* (a site), not a material, and asserts anthropogenic feature-hood. Correctly retained as `xref`. |
| **Waste / wastewater / sewage** (`ENVO:00002018`, `ENVO:01000964`) | Material that *is* the waste stream, versus clean material that has received a contaminant. Separate BacDive Cat2 (`#Waste`). |
| **Bioremediation / biodegradation** (`#Engineered > #Bioremediation`, `#Biodegradation`; corpus records `other/bioremediation.yaml`, `other/biodegradation.yaml`) | The intervention applied to contaminated material, not the material. |
| **Reagent/kit contamination, the "kitome"** (Salter *et al.* 2014) | A sequencing artefact. Not a habitat under any reading, and not what BacDive's cultured-strain records capture. |
| **`ENVO:00003082` enriched soil** | Elevated levels of *any* material entity, including nutrients deliberately added. No contaminant or harm claim. |
| **Contaminated *food* / food-production contamination areas** (`ENVO:02000048`, `ENVO:03501320–22`) | Product hygiene, a different domain with its own ENVO branch. |

---

## 6. Should this be a term at all?

**Yes — and the corpus already treats the same idea as a habitat elsewhere, which makes the current disposition inconsistent.**

`terrestrial/contaminated_soil.yaml` is grounded **EXACT** to `ENVO:00002116` from GOLD's `contaminated soil`. `terrestrial/oil_contaminated_soil.yaml` is grounded EXACT to `ENVO:00002875`. If contaminated soil is a habitat, contaminated environmental material is a habitat; it is simply the class one level up, and ENVO has not minted it.

So the recommended disposition is: **keep the minted identity, keep `ENVO:00002204` as `relation: xref`, and record it as a term-request candidate for ENVO with the definition above.** The entry in `curation/term_requests_excluded.tsv` ("Not a place… a circumstance of sampling") should be removed or rewritten, because its stated reason describes `BACDIVE.4d06ff4bb5` rather than this record. The blocker recorded in `curation/term_requests/needs_a_parent_first.tsv` ("no ontology parent on the record, so there is no genus to write a definition from") is resolved by using `ENVO:00010483` *environmental material* as the genus.

Three secondary items the curator should decide alongside this one, all surfaced by the same finding:

1. **`habitat_category: OTHER`.** If the concept is now read as a contaminated material rather than a sampling circumstance, OTHER may no longer be the right bucket. It is genuinely cross-cutting (terrestrial soil, aquatic sediment, engineered sludge), so OTHER is defensible — but it should be an explicit choice, not a leftover.
2. **`other/oil_fuel.yaml`** (`habitatmech:BACDIVE.9f31ab2d87`, "Oil-Fuel", 130 strains) is currently `NOT_APPLICABLE`. BacDive strain 6251 shows *Oil (Fuel)* is the Cat3 **child of Contamination** — i.e. the contaminant type, and for many strains the isolated-from material itself. Worth re-reviewing under the same light.
3. **The `Contaminant` record** (`BACDIVE.4d06ff4bb5`, 61 strains, currently `SEEDED` with a class-level sweep note that explicitly did not assess habitat-hood) is where the "not a place, a circumstance of sampling" argument actually belongs. It is a strong `NOT_APPLICABLE` candidate on that reasoning — a strain being *a contaminant* is a role of the organism, not an environment.

---

### Definition, restated with the optional clause marked

> **A** ***environmental material (`ENVO:00010483`)*** **which** *has elevated levels of one or more contaminants* [*introduced by human activity*] *, relative to comparable material of the same kind.*

The bracketed clause is supported by BacDive's placement of the tag under `#Engineered` and by all sampled instances, but is an inference from tag placement rather than a published BacDive definition. Dropping it costs nothing that the sources vouch for; keeping it should be footnoted in `notes` as resting on the Cat1 placement.

## Citations

1. https://bacdive.dsmz.de/strain/6251
2. https://bacdive.dsmz.de/strain/130219
3. https://bacdive.dsmz.de/strain/3758
4. https://bacdive.dsmz.de/strain/24261
5. https://doi.org/10.1099/ijs.0.039073-0
6. https://pubmed.ncbi.nlm.nih.gov/22447701/
7. https://bacdive.dsmz.de/isolation-sources
8. https://bacdive.dsmz.de/strain/14287
9. https://doi.org/10.1007/s11356-024-33326-6
10. https://pubmed.ncbi.nlm.nih.gov/26025169/
11. https://pubmed.ncbi.nlm.nih.gov/34890619/
12. https://doi.org/10.1186/s12915-014-0087-z
13. https://pubmed.ncbi.nlm.nih.gov/25387460/
14. https://doi.org/10.1093/nar/gky879
15. https://pubmed.ncbi.nlm.nih.gov/30256983/
16. https://doi.org/10.1093/nar/gkae959
17. https://pubmed.ncbi.nlm.nih.gov/39470737/
18. https://bacdive.dsmz.de/strain/8499
19. https://doi.org/10.1186/s13326-016-0097-6
20. https://pubmed.ncbi.nlm.nih.gov/27664130/
21. https://www.ebi.ac.uk/ols4/ontologies/envo
22. https://doi.org/10.1128/MRA.00671-20
23. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7585852/