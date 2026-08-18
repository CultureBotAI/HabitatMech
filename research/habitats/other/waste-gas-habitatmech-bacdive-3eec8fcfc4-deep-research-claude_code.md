---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T00:21:34.146990'
end_time: '2026-08-18T00:32:12.736136'
duration_seconds: 638.59
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Waste-gas
  habitat_identifier: habitatmech:BACDIVE.3eec8fcfc4
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Waste-gas'
  assertions: '20'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Grounding-cohort
    review (#62): was ENVO:01001155 ''astrogeological gas'', which carries the bare
    synonym ''gas'' and so matches any gas source at all. Waste gas from an industrial
    process is a real habitat and the slice has no term for it. (source concept habitatmech:BACDIVE.3eec8fcfc4)'
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
  web_search_requests: 14
  num_turns: 40
  total_cost_usd: 3.449039
  session_id: 4c87f999-004d-43b1-a021-b8bd6bf14a53
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 38
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Waste-gas
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.3eec8fcfc4
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Waste-gas
- **Upstream assertion volume:** 20
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Grounding-cohort review (#62): was ENVO:01001155 'astrogeological gas', which carries the bare synonym 'gas' and so matches any gas source at all. Waste gas from an industrial process is a real habitat and the slice has no term for it. (source concept habitatmech:BACDIVE.3eec8fcfc4)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Waste-gas** as a microbial habitat, with citations.

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

# Waste-gas — definition research for `habitatmech:BACDIVE.3eec8fcfc4`

## Proposed definition

> A **gaseous environmental material** which is the effluent stream discharged from an industrial, agricultural or waste-handling process to a stack or to abatement equipment, and which carries the pollutant load (volatile organics, reduced sulfur and nitrogen compounds), warmth and near-saturating humidity that support the microbial community sampled from it or from the biological equipment treating it.

If a curator judges the trailing clause too close to a sampling statement, the shorter form

> A gaseous environmental material which is discharged from an anthropogenic process to a stack or to abatement equipment, and which bears a load of volatile organic, nitrogenous or reduced-sulfur pollutants.

is defensible on the same citations, and the microbial-community facts move into `notes`/`comments` rather than the definition. **I recommend the shorter form**, for the reason set out in §1: the microorganisms attributed to this concept are overwhelmingly recovered from the biofilm treating the gas, not suspended in the gas phase, so a definition that says the gas "sustains" a community over-claims slightly.

---

## 1. What the concept denotes

### 1.1 The source path is unambiguous about provenance

"Waste-gas" is a level-3 term in BacDive's **MISO** (Microbial Isolation Source Ontology) controlled vocabulary, a three-level, ~376-term hierarchy used to manually index BacDive isolation sources ([BacDive in 2022, *NAR* 50:D741–D746, doi:10.1093/nar/gkab961](https://academic.oup.com/nar/article/50/D1/D741/6414049); [isolation-source browser](https://bacdive.dsmz.de/isolation-sources)). Its path is:

```
#Engineered  →  #Waste  →  #Waste gas
```

I verified this directly on a tagged strain: ***Aquamicrobium ahrensii* 905/1ᵀ (DSM 19730), [BacDive ID 11867](https://bacdive.dsmz.de/strain/11867)** carries three MISO tag-triples — `#Engineered/#Bioremediation/#Biofilter`, `#Engineered/#Industrial/#Plant (Factory)`, and `#Engineered/#Waste/#Waste gas` — with the free-text source *"experimental biofilter for waste gas treatment of an animal rendering plant"*, Brögbern/Lingen, Lower Saxony, Germany, 1990.

So the concept is firmly **engineered/anthropogenic**, and specifically **waste**, not merely "a gas".

### 1.2 The label is ambiguous between two readings — and the data supports the second

**Reading A — the gaseous material itself.** Waste gas as a substance: the confined, pollutant-bearing effluent stream leaving a process, which carries viable microorganisms as bioaerosols. This reading is real and citable: bioaerosols are measurably present in, and emitted with, the exhaust air of composting plants, livestock housing and wastewater works ([Vélez-Pereira et al., *Microorganisms* 14:963, 2026, doi:10.3390/microorganisms14050963](https://doi.org/10.3390/microorganisms14050963)), and biofilter beds themselves can *add* bacteria and fungi to the gas leaving them, particularly when the incoming waste gas is microbiologically poor ([*Atmosphere* 12:1574, 2021, doi:10.3390/atmos12121574](https://doi.org/10.3390/atmos12121574); [*Atmosphere* 12:673, 2021, doi:10.3390/atmos12060673](https://doi.org/10.3390/atmos12060673)).

**Reading B — the waste-gas stream as the defining feature of an engineered setting**, with the actual biomass residing in the aqueous biofilm on the packing of the biofilter, biotrickling filter or bioscrubber through which that gas passes. Degradation in these systems is carried out by microorganisms *colonising the solid support medium*, aerobically ([VDI 3477:2016-03, *Biological waste gas purification — Biofilters*](https://www.vdi.de/en/home/vdi-standards/details/vdi-3477-biological-waste-gas-purification-biofilters)).

**The BacDive attestations are Reading B.** Every strain I could trace under this label was isolated from the *treatment system*, with "waste gas" naming the stream being treated:

| Strain | BacDive | Free-text isolation source |
|---|---|---|
| *Aquamicrobium ahrensii* 905/1ᵀ | [11867](https://bacdive.dsmz.de/strain/11867) | experimental biofilter for waste gas treatment of an animal rendering plant |
| *Paracoccus alkenifer* 901/1ᵀ | [13717](https://bacdive.dsmz.de/strain/13717) | biofilter for waste gas treatment, Brögbern/Lingen, Germany, 1990 |

Note the tagging inconsistency worth recording: strain 13717 is tagged `#Engineered/#Waste/#Biofilter`, not `#Waste gas`, despite the identical free-text source and the same sampling site. **`#Waste gas` and `#Biofilter` are used near-interchangeably by BacDive curators for this cohort**, and a strain may carry either or both.

**Inference flag.** I confirmed the `#Waste gas` tag on exactly one strain (11867). The characterisation of the full 20-assertion cohort as waste-gas-biofilter isolates is my inference, supported by (a) the two verified BacDive records, (b) the fact that essentially the whole named-taxon literature for German waste-gas biofilters comes from one group and one site, and (c) the near-total absence of taxa described from gas streams *per se*. A curator with BacDive API access should enumerate the 20 strains before relying on it.

That cohort — from A. Lipski and K. Altendorf's group at Universität Osnabrück, sampling experimental and full-scale biofilters at an animal-rendering plant in Brögbern (Lingen), an oil mill in Hamm, and related plants — includes at least:

- *Paracoccus alkenifer* and *P. solventivorans* isolates ([Lipski et al., *IJSB* 48:529–536, 1998, doi:10.1099/00207713-48-2-529](https://doi.org/10.1099/00207713-48-2-529); PMID 9731294)
- *Stenotrophomonas nitritireducens*, *Luteimonas mephitis*, *Pseudoxanthomonas broegbernensis* — N₂O-producing Xanthomonas-like biofilter isolates ([Finkmann et al., *IJSEM* 50:273–282, 2000, doi:10.1099/00207713-50-1-273](https://doi.org/10.1099/00207713-50-1-273))
- *Alkanibacter difficilis*, *Singularimonas variicoloris* — hexane degraders from a hexane-treated biofilter at an oil mill ([Friedrich & Lipski, *IJSEM* 58:2324–2329, 2008, doi:10.1099/ijs.0.65517-0](https://doi.org/10.1099/ijs.0.65517-0))
- *Aquamicrobium ahrensii*, *A. segne* ([Lipski & Kämpfer, *IJSEM* 62:2511–2516, 2012, doi:10.1099/ijs.0.038224-0](https://doi.org/10.1099/ijs.0.038224-0); PMID 22155762)
- earlier Gram-negative non-fermenter isolates (*Alcaligenes*, *Pseudomonas* clusters) from ammonia-supplied biofilters ([Lipski et al., *AEM* 58:2053–2065, 1992, doi:10.1128/aem.58.6.2053-2065.1992](https://doi.org/10.1128/aem.58.6.2053-2065.1992))

### 1.3 The boundary

**Inside the concept:** the confined gaseous effluent of an anthropogenic process, between the point of capture and the point of discharge or abatement — process off-gas, plant exhaust air, animal-house exhaust air, composting hall exhaust, WWTP odour off-gas, biofilter inlet ("crude/raw gas") and outlet ("clean gas").

**Outside the concept (neighbouring):**
- **the abatement device** (biofilter bed, biotrickling filter packing, bioscrubber liquor) — a distinct engineered habitat with its own MISO tags (`#Biofilter`, `#Bioreactor`) and a distinct physical state (wet biofilm on porous solid);
- **ambient/outdoor air** that has received the discharge — once diluted into the atmosphere it is air, or contaminated air, not waste gas;
- **fugitive emissions** — the IED explicitly defines these as emissions *not* in waste gases ([Directive 2010/75/EU Art. 57(3)](https://www.legislation.gov.uk/eudr/2010/75/article/57));
- **liquid and solid waste streams** — wastewater, sludge, compost.

---

## 2. Genus — the broader kind

### Recommended genus: `ENVO:01000797` **gaseous environmental material**

This is the smallest well-established ENVO kind that the concept falls under without over-claiming. Its position in ENVO: `BFO:0000040 material entity → ENVO:00010483 environmental material → ENVO:02000140 fluid environmental material → ENVO:01000797 gaseous environmental material` (verified via the OLS4 ancestor endpoint for `ENVO:03510008`).

Critically, **ENVO already places anthropogenic waste gas streams directly under this class**: `ENVO:03510008` *diesel exhaust* and `ENVO:03510009` *gasoline exhaust* are its direct children. So the proposed term would be a **sibling of diesel and gasoline exhaust** — an existing, populated modelling slot. That is a strong argument that "waste gas" is a well-formed ENVO term request, not an idiosyncratic HabitatMech invention.

### Near-misses and why each fails

| CURIE | Label | Why it fails |
|---|---|---|
| `ENVO:01001155` | astrogeological gas | **The current (wrong) grounding.** Verified definition: *"An astrogeological volatile which is composed primarily of chemical compounds with boiling points around those of hydrogen and helium."* It carries the bare exact synonym **"gas"**, which is why lexical matching landed here. Asserts a planetary-science origin the sources never claim. The curator's note is correct. |
| `ENVO:00002267` | industrial waste material | **Closest existing term, and a genuine near-miss.** Definition explicitly covers gaseous wastes: *"Industrial wastes are liquid, solid and gaseous wastes originating from the manufacture of specific products."* Fails as genus because it asserts a *manufacturing* origin: animal-house exhaust air, composting-hall exhaust and municipal WWTP odour off-gas are waste gas but are not industrial manufacturing waste. It is broader than *industrial* waste gas but **not** broader than waste gas, so per the repo's `parent_habitats` rule it belongs in `relation: xref`, not as a parent. |
| `ENVO:03510008` / `ENVO:03510009` | diesel exhaust / gasoline exhaust | Narrower — fuel-combustion-specific. Correct siblings, not parents. |
| `ENVO:00002264` | waste material | Broader but state-agnostic; loses the gaseous differentia entirely and sits in a branch that is not the gaseous-material branch. Usable as a second parent if the curator wants the waste-role captured in the hierarchy. |
| `ENVO:01000676` | contaminated air | Definition: *"air which has sufficient concentrations of environmental pollutants such that it may adversely affect a given ecosystem."* Asserts ecosystem-level harm and treats the material as *air* (ambient atmosphere). Waste gas is a confined, channelled process stream, and much of it (e.g. clean gas after abatement) is compliant with limits. |
| `ENVO:00002005` | air | The atmosphere/ambient reading; loses both the anthropogenic-origin and the waste-role differentiae. |
| `ENVO:01000556` | biogas | A *product* of anaerobic digestion, valorised as fuel — not a discharge to a stack. See §5. |
| `ENVO:02000131` | flue gas desulfurization material | A solid/slurry sorbent residue, not the gas. Lexically adjacent, semantically unrelated. |
| `ENVO:0010001` | anthropogenic environmental material | *"Anthropogenic material in or on which organisms may live."* Correct in spirit, but far too broad and not gas-specific. |

**Conclusion: no ENVO, UBERON, FOODON, BTO or PO term names this concept.** The `CONFIRM_UNGROUNDED` decision on the record is sound, and a HabitatMech-minted term plus an ENVO term request for *waste gas* under `ENVO:01000797` is the right disposition.

---

## 3. Differentia — what distinguishes it from its siblings

Under *gaseous environmental material*, the properties that separate waste gas from air, atmospheric gas, natural gas, biogas and vehicle exhaust:

1. **Origin — anthropogenic process effluent, captured and channelled.** The regulatory definition is precise and citable: *"'waste gases' means the final gaseous discharge containing volatile organic compounds or other pollutants from a stack or abatement equipment into air"* ([Directive 2010/75/EU, Art. 57(2)](https://www.legislation.gov.uk/eudr/2010/75/article/57)). The complementary "contained conditions" definition in the same article makes the capture-and-channel property explicit. This is the single strongest differentia and it comes from a standard, not from inference.

2. **Waste role.** The stream is destined for discharge or abatement, not for use. This distinguishes it from biogas, natural gas and syngas, which are products.

3. **Characteristic pollutant load.** Odorants, VOCs, reduced sulfur compounds (H₂S, methanethiol, dimethyl sulfide), ammonia and amines, and aldehydes; VDI 3477's scope is *"waste gas/exhaust air streams containing gaseous and aerosol-form air pollutants, in particular odorants."* Documented substrate ranges in the primary literature include hexane (oil mill), styrene, aldehydes and ammonia ([Friedrich & Lipski 2010, *AMB* 85:1189–1199, doi:10.1007/s00253-009-2290-3](https://doi.org/10.1007/s00253-009-2290-3); [Alexandrino, Knief & Lipski 2001, *AEM* 67:4796–4804, doi:10.1128/AEM.67.10.4796-4804.2001](https://doi.org/10.1128/AEM.67.10.4796-4804.2001)).

4. **Characteristic physicochemistry — high flow, low concentration, high humidity, near-ambient temperature.** Biological treatment is the economical option precisely because waste gas is a *high-flow, low-concentration* stream, unlike the low-flow/high-concentration streams that suit adsorption or condensation ([Kennes & Thalasso, *J. Chem. Technol. Biotechnol.* 72:303–319, 1998](https://doi.org/10.1002/(SICI)1097-4660(199808)72:4%3C303::AID-JCTB903%3E3.0.CO;2-Y); [Dobslaw & Ortlinghaus, *Sustainability* 12:8577, 2020, doi:10.3390/su12208577](https://doi.org/10.3390/su12208577)). Treated waste gas leaving a biofilter is essentially water-vapour-saturated — reported means of ~98% relative humidity and ~22.5 °C, not exceeding 33 °C. This near-saturation is what makes the stream biologically tractable at all.

5. **Carries a microbial load as bioaerosol.** Waste gas from composting, livestock and wastewater operations carries bacteria, fungi and endotoxin; biofilters remove fungal bioaerosols efficiently (often >90%) but bacterial removal ranges from negligible to >90%, and unstable, nutrient-rich media can turn the biofilter into a *secondary emission source* (Vélez-Pereira et al. 2026; *Atmosphere* 12:1574).

6. **Selects a characteristic, high-diversity community when biofiltered.** The community treating waste gas is not a random air community. Clone-library and FISH work on a rendering-plant waste-gas biofilter found high bacterial diversity — 60.8% of 444 ARDRA-screened clones showed unique patterns, ~90% of sequenced clones affiliating with *Pseudomonadota* and *Bacteroidota*, with a large share from then-unknown taxa ([Friedrich et al., *Environ. Microbiol.* 4:721–734, 2002, doi:10.1046/j.1462-2920.2002.00349.x](https://doi.org/10.1046/j.1462-2920.2002.00349.x); PMID 12460280), Betaproteobacteria dominating and activity stratified by bed depth ([Friedrich et al., *Environ. Microbiol.* 5:183–201, 2003, doi:10.1046/j.1462-2920.2003.00397.x](https://doi.org/10.1046/j.1462-2920.2003.00397.x); PMID 12588298). Full-scale biotrickling filters on pig-house exhaust air converge on a shared community distinct from their activated-sludge inoculum, rich in heterotrophs including denitrifiers ([*Microb. Biotechnol.*, PMC6559015](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6559015/)).

**Minimal differentia for the definition sentence:** items 1 + 2 + 3 are sufficient and each is directly sourced. Items 4–6 belong in `comments`/`notes`.

---

## 4. Sources

Grouped by what they support. Statements I could not source are flagged inline as inference.

**The source concept and its attestations**
- BacDive strain 11867, *Aquamicrobium ahrensii* 905/1ᵀ — https://bacdive.dsmz.de/strain/11867 *(verified: carries `#Engineered/#Waste/#Waste gas`)*
- BacDive strain 13717, *Paracoccus alkenifer* 901/1ᵀ — https://bacdive.dsmz.de/strain/13717
- BacDive isolation-source browser (MISO tree) — https://bacdive.dsmz.de/isolation-sources
- Reimer LC et al., *BacDive in 2022: the knowledge base for standardized bacterial and archaeal data*, **NAR** 50:D741–D746 (2022), doi:10.1093/nar/gkab961, PMC8728306
- Schober I et al., *BacDive in 2025: the core database for prokaryotic strain data*, **NAR** 53:D748–D756 (2025), doi:10.1093/nar/gkae959

**Regulatory / standards definition of waste gas**
- Directive 2010/75/EU (Industrial Emissions Directive), **Art. 57(2)–(4)** — https://www.legislation.gov.uk/eudr/2010/75/article/57 ; consolidated text https://eur-lex.europa.eu/eli/dir/2010/75/2024-08-04/eng *(note: retitled "on industrial and livestock rearing emissions" by Directive (EU) 2024/1785)*
- JRC, *Best Available Techniques (BAT) Reference Document for Common Waste Gas Management and Treatment Systems in the Chemical Sector* (WGC BREF, 2023), ISSN 1831-9424 — https://bureau-industrial-transformation.jrc.ec.europa.eu/sites/default/files/2023-01/WGC_BREF_2023_for_publishing%20ISSN%201831-9424_final_1_revised.pdf
- **VDI 3477:2016-03**, *Biologische Abgasreinigung — Biofilter / Biological waste gas purification — Biofilters*, VDI/DIN-KRdL — https://www.vdi.de/en/home/vdi-standards/details/vdi-3477-biological-waste-gas-purification-biofilters *(statically referenced by TA Luft 2021, §§5.4.8.5, 5.4.8.6.2; basis for **ISO 23138**, "Biological equipment for treating air and other gases — General requirements")*

**Ontology terms (all verified via the EBI OLS4 API, August 2026)**
- `ENVO:01000797` gaseous environmental material; `ENVO:02000140` fluid environmental material; `ENVO:00010483` environmental material
- `ENVO:03510008` diesel exhaust — *"A gas which results from the incomplete or complete combustion of diesel fuel."*; `ENVO:03510009` gasoline exhaust
- `ENVO:01001155` astrogeological gas — *"An astrogeological volatile which is composed primarily of chemical compounds with boiling points around those of hydrogen and helium."*, exact synonym **"gas"**
- `ENVO:00002267` industrial waste material; `ENVO:00002264` waste material; `ENVO:01000676` contaminated air; `ENVO:00002005` air; `ENVO:01000556` biogas; `ENVO:02000131` flue gas desulfurization material; `ENVO:0010001` anthropogenic environmental material
- OLS4 API: https://www.ebi.ac.uk/ols4/api/search?q=…&ontology=envo

**Taxa described from waste-gas treatment systems**
- Lipski A, Klatte S, Bendinger B, Altendorf K. **AEM** 58:2053–2065 (1992), doi:10.1128/aem.58.6.2053-2065.1992
- Lipski A, Reichert K, Reuter B, Spröer C, Altendorf K. *Identification of bacterial isolates from biofilters as* Paracoccus alkenifer *sp. nov. …* **IJSB** 48:529–536 (1998), doi:10.1099/00207713-48-2-529, PMID 9731294
- Finkmann W, Altendorf K, Stackebrandt E, Lipski A. **IJSEM** 50:273–282 (2000), doi:10.1099/00207713-50-1-273
- Friedrich MM, Lipski A. *Alkanibacter difficilis gen. nov., sp. nov. and Singularimonas variicoloris gen. nov., sp. nov., hexane-degrading bacteria isolated from a hexane-treated biofilter.* **IJSEM** 58:2324–2329 (2008), doi:10.1099/ijs.0.65517-0
- Lipski A, Kämpfer P. *Aquamicrobium ahrensii sp. nov. and Aquamicrobium segne sp. nov., isolated from experimental biofilters.* **IJSEM** 62:2511–2516 (2012), doi:10.1099/ijs.0.038224-0, PMID 22155762

**Microbial ecology of waste gas and its treatment**
- Friedrich U, Naismith MM, Altendorf K, Lipski A. **AEM** 65:3547–3554 (1999), doi:10.1128/aem.65.8.3547-3554.1999
- Friedrich U, Prior K, Altendorf K, Lipski A. **Environ. Microbiol.** 4:721–734 (2002), doi:10.1046/j.1462-2920.2002.00349.x, PMID 12460280
- Friedrich U, Van Langenhove H, Altendorf K, Lipski A. **Environ. Microbiol.** 5:183–201 (2003), doi:10.1046/j.1462-2920.2003.00397.x, PMID 12588298
- Friedrich MM, Lipski A. **Appl. Microbiol. Biotechnol.** 85:1189–1199 (2010), doi:10.1007/s00253-009-2290-3, PMID 19847422
- Alexandrino M, Knief C, Lipski A. **AEM** 67:4796–4804 (2001), doi:10.1128/AEM.67.10.4796-4804.2001
- Long-term microbial community dynamics at two full-scale biotrickling filters treating pig house exhaust air — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6559015/
- Feng et al., biotrickling filters under continuous/discontinuous waste gases — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6320331/
- Metagenomic analysis of microbial community structure and function in an improved biofilter with odorous gases, **Sci. Rep.** 12 (2022), doi:10.1038/s41598-022-05858-9
- Vélez-Pereira AM, Bravo Barra P, Camargo Caicedo Y, O'Connor DJ. *Biofiltration of Bioaerosols Emitted from Organic Waste Management Facilities: A Review.* **Microorganisms** 14:963 (2026), doi:10.3390/microorganisms14050963, PMID 42197349
- *Bioaerosol Emission from Biofilters: Impact of Bed Material Type and Waste Gas Origin.* **Atmosphere** 12:1574 (2021), doi:10.3390/atmos12121574
- *How to Reduce the Emission of Microorganisms from a Biofilter Used to Treat Waste Gas from a Food Industry Plant.* **Atmosphere** 12:673 (2021), doi:10.3390/atmos12060673

**Engineering reviews**
- Kennes C, Thalasso F. *Review: Waste gas biotreatment technology.* **JCTB** 72:303–319 (1998)
- Kennes C, Rene ER, Veiga MC. *Bioprocesses for air pollution control.* **JCTB** 84:1419–1436 (2009), doi:10.1002/jctb.2216
- Dobslaw D, Ortlinghaus O. *Biological Waste Air and Waste Gas Treatment: Overview, Challenges, Operational Efficiency, and Current Trends.* **Sustainability** 12:8577 (2020), doi:10.3390/su12208577
- *Microbiology of Bioreactors for Waste Gas Treatment*, in **Biotechnology for Odor and Air Pollution Control** (Springer, 2005), doi:10.1007/3-540-27007-8_5

---

## 5. Synonyms, and what NOT to conflate

### Synonyms in real use
| Term | Note |
|---|---|
| waste gas | preferred; IED/BREF/VDI usage |
| waste air | VDI/German-English usage |
| exhaust air | common for livestock housing, composting halls, ventilation-borne streams |
| off-gas / offgas | common in process engineering and WWTP odour control |
| process off-gas, vent gas, stack gas | narrower usage contexts |
| Abgas, Abluft | German (VDI 3477 title uses both) |
| raw gas / crude gas (*Rohgas*) | the untreated stream at a biofilter inlet |
| clean gas (*Reingas*) | the treated stream at the outlet — still waste gas under the IED definition, which specifies "final gaseous discharge … from a stack **or abatement equipment**" |
| odorous gas, odour emission | frequent in the biofiltration literature; strictly a subtype |

### Do NOT conflate
- **flue gas / combustion gas.** Combustion-specific, hot, oxygen-depleted, typically not biologically colonisable in the same way. A subtype at best; not a synonym. Note the lexical trap of `ENVO:02000131` *flue gas desulfurization material*, which is a **solid/slurry sorbent residue**, not a gas.
- **`ENVO:01000556` biogas / landfill gas.** A *product* of anaerobic digestion, harvested as fuel. Waste gas is a discharge. (VDI 3477's 2016 revision added a landfill-gas-treatment section, which shows the two are adjacent but distinguished.)
- **`ENVO:03510008` diesel exhaust / `ENVO:03510009` gasoline exhaust.** Vehicular; siblings, not synonyms.
- **`ENVO:00002005` air / `ENVO:01000676` contaminated air / indoor air.** Ambient, unchannelled, no waste role.
- **bioaerosol.** The particulate/biological *fraction carried by* a gas stream, not the stream. Conflating these makes the habitat a particle rather than a medium.
- **the biofilter / biotrickling filter / bioscrubber itself.** A separate engineered habitat (MISO `#Biofilter`, `#Bioreactor`; ENVO has `ENVO:00003968` *air filter* and `ENVO:00002874` *air conditioning unit* nearby). **This is the most likely conflation in practice**, because BacDive curators tag the same strains both ways (§1.2) — worth stating explicitly in the record's `notes`.
- **syngas / steel-mill off-gas as a gas-fermentation feedstock.** In gas fermentation (e.g. *Clostridium autoethanogenum*, *C. ljungdahlii* on CO/CO₂/H₂ streams; see [*Microb. Biotechnol.*, PMC9079231](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9079231/)) the waste gas is a **growth substrate delivered into a bioreactor**, and the organisms were not isolated from it. A strain "grown on waste gas" is not a strain "isolated from waste gas". If any of the 20 attestations turn out to be of this kind, they belong under a bioreactor concept, not here.
- **wastewater (`ENVO:00002001`), industrial wastewater (`ENVO:01000964`), sludge, compost.** Same waste role, different phase.

---

## 6. Should it be a term at all?

**Yes.** It passes the tests the corpus applies:

- **It is a place/material, not a process, quality, disease or taxon.** It is a material entity — a gaseous environmental material — with a defined spatial extent (between capture and discharge) and a legally standardised definition. It is not `NOT_APPLICABLE` material.
- **It is a real microbial habitat.** Waste gas demonstrably carries viable microorganisms as bioaerosols, and the systems built around it host dense, stratified, reproducible, and taxonomically novel communities — at least eight validly published species have been described from waste-gas treatment biofilters alone.
- **No ontology term names it**, and ENVO has an obvious, populated slot for it as a sibling of *diesel exhaust* and *gasoline exhaust* under `ENVO:01000797`.
- **20 upstream assertions** is a real, non-trivial attestation volume for an engineered category.

### Recommended disposition

1. Keep `CONFIRM_UNGROUNDED`; mint the HabitatMech term.
2. `parent_habitats`: `ENVO:01000797` *gaseous environmental material* — genuinely broader, safe.
3. `relation: xref` (not parent): `ENVO:00002267` *industrial waste material* — records the link upstream would want without asserting a manufacturing origin the agricultural and municipal attestations do not have.
4. Record in `notes` the tagging observation from §1.2: **BacDive applies `#Waste gas` and `#Biofilter` near-interchangeably to the same rendering-plant biofilter cohort**, so this record's attestations describe organisms recovered from the *biofilm treating* the gas, not from the gas phase. This is exactly the kind of provenance fact that stops a future curator from over-reading the definition.
5. **Flag as a possible sibling gap:** the corpus may also want a distinct concept for the *biological waste-gas treatment system* (biofilter/biotrickling filter/bioscrubber bed). If BacDive's `#Biofilter` cat-3 term appears in the corpus as its own novel term, these two records should cross-reference each other rather than merge — the gas and the packed bed are different habitats with different water activity, different biomass, and different sampling protocols.

### Suggested ENVO term request text

> **waste gas** — A gaseous environmental material which is discharged from an anthropogenic process to a stack or to abatement equipment, and which bears a load of volatile organic, nitrogenous or reduced-sulfur pollutants. *Parent:* gaseous environmental material (ENVO:01000797). *Siblings:* diesel exhaust (ENVO:03510008), gasoline exhaust (ENVO:03510009). *Synonyms:* waste air, exhaust air, off-gas, process off-gas. *Source:* Directive 2010/75/EU Art. 57(2); VDI 3477:2016-03.

---

**Sources:**

- [BacDive strain 11867 — *Aquamicrobium ahrensii*](https://bacdive.dsmz.de/strain/11867)
- [BacDive strain 13717 — *Paracoccus alkenifer*](https://bacdive.dsmz.de/strain/13717)
- [BacDive isolation-sources browser](https://bacdive.dsmz.de/isolation-sources)
- [BacDive in 2022 (NAR)](https://academic.oup.com/nar/article/50/D1/D741/6414049) · [BacDive in 2025 (NAR)](https://academic.oup.com/nar/article/53/D1/D748/7848838) · [BacDive in 2019 (NAR)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/)
- [Directive 2010/75/EU, Article 57](https://www.legislation.gov.uk/eudr/2010/75/article/57) · [consolidated text (EUR-Lex)](https://eur-lex.europa.eu/eli/dir/2010/75/2024-08-04/eng)
- [JRC Common Waste Gas BREF (2023)](https://bureau-industrial-transformation.jrc.ec.europa.eu/sites/default/files/2023-01/WGC_BREF_2023_for_publishing%20ISSN%201831-9424_final_1_revised.pdf)
- [VDI 3477 — Biological waste gas purification: Biofilters](https://www.vdi.de/en/home/vdi-standards/details/vdi-3477-biological-waste-gas-purification-biofilters)
- [EBI OLS4 (ENVO term lookups)](https://www.ebi.ac.uk/ols4/api/search?q=gas&ontology=envo)
- [Lipski et al. 1998, *Paracoccus alkenifer* sp. nov. (PubMed)](https://pubmed.ncbi.nlm.nih.gov/9731294/)
- [Lipski & Kämpfer 2012, *Aquamicrobium ahrensii* sp. nov.](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.038224-0)
- [Friedrich & Lipski 2008, *Alkanibacter difficilis* gen. nov.](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.65517-0)
- [Friedrich et al. 2002, high bacterial diversity of a waste gas-degrading community](https://pubmed.ncbi.nlm.nih.gov/12460280/?dopt=Abstract)
- [Friedrich et al. 2003, industrial waste gas biofilter community + probes](https://enviromicro-journals.onlinelibrary.wiley.com/doi/abs/10.1046/j.1462-2920.2003.00397.x)
- [Friedrich & Lipski 2010, hexane degraders in a biofilter](https://link.springer.com/article/10.1007/s00253-009-2290-3)
- [Vélez-Pereira et al. 2026, Biofiltration of bioaerosols (Microorganisms)](https://doi.org/10.3390/microorganisms14050963)
- [Bioaerosol emission from biofilters: bed material and waste gas origin (Atmosphere)](https://doi.org/10.3390/atmos12121574) · [Reducing microorganism emission from a food-industry biofilter (Atmosphere)](https://doi.org/10.3390/atmos12060673)
- [Long-term community dynamics at full-scale biotrickling filters, pig house exhaust air](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6559015/) · [Continuous vs. discontinuous waste gases in biotrickling filters](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6320331/) · [Metagenomics of an improved biofilter with odorous gases (Sci. Rep.)](https://www.nature.com/articles/s41598-022-05858-9)
- [Dobslaw & Ortlinghaus 2020, Biological waste air and waste gas treatment (Sustainability)](https://doi.org/10.3390/su12208577) · [Kennes & Thalasso 1998, Waste gas biotreatment technology](https://scijournals.onlinelibrary.wiley.com/doi/10.1002/(SICI)1097-4660(199808)72:4%3C303::AID-JCTB903%3E3.0.CO;2-Y) · [Microbiology of bioreactors for waste gas treatment (Springer)](https://link.springer.com/chapter/10.1007/3-540-27007-8_5)
- [Turning waste gases into valuables (gas fermentation)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9079231/)

## Citations

1. https://academic.oup.com/nar/article/50/D1/D741/6414049
2. https://bacdive.dsmz.de/isolation-sources
3. https://bacdive.dsmz.de/strain/11867
4. https://doi.org/10.3390/microorganisms14050963
5. https://doi.org/10.3390/atmos12121574
6. https://doi.org/10.3390/atmos12060673
7. https://www.vdi.de/en/home/vdi-standards/details/vdi-3477-biological-waste-gas-purification-biofilters
8. https://bacdive.dsmz.de/strain/13717
9. https://doi.org/10.1099/00207713-48-2-529
10. https://doi.org/10.1099/00207713-50-1-273
11. https://doi.org/10.1099/ijs.0.65517-0
12. https://doi.org/10.1099/ijs.0.038224-0
13. https://doi.org/10.1128/aem.58.6.2053-2065.1992
14. https://www.legislation.gov.uk/eudr/2010/75/article/57
15. https://doi.org/10.1007/s00253-009-2290-3
16. https://doi.org/10.1128/AEM.67.10.4796-4804.2001
17. https://doi.org/10.1002/(SICI
18. https://doi.org/10.3390/su12208577
19. https://doi.org/10.1046/j.1462-2920.2002.00349.x
20. https://doi.org/10.1046/j.1462-2920.2003.00397.x
21. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6559015/
22. https://eur-lex.europa.eu/eli/dir/2010/75/2024-08-04/eng
23. https://bureau-industrial-transformation.jrc.ec.europa.eu/sites/default/files/2023-01/WGC_BREF_2023_for_publishing%20ISSN%201831-9424_final_1_revised.pdf
24. https://www.ebi.ac.uk/ols4/api/search?q=…&ontology=envo
25. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6320331/
26. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9079231/
27. https://academic.oup.com/nar/article/53/D1/D748/7848838
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/
29. https://www.ebi.ac.uk/ols4/api/search?q=gas&ontology=envo
30. https://pubmed.ncbi.nlm.nih.gov/9731294/
31. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.038224-0
32. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.65517-0
33. https://pubmed.ncbi.nlm.nih.gov/12460280/?dopt=Abstract
34. https://enviromicro-journals.onlinelibrary.wiley.com/doi/abs/10.1046/j.1462-2920.2003.00397.x
35. https://link.springer.com/article/10.1007/s00253-009-2290-3
36. https://www.nature.com/articles/s41598-022-05858-9
37. https://scijournals.onlinelibrary.wiley.com/doi/10.1002/(SICI
38. https://link.springer.com/chapter/10.1007/3-540-27007-8_5