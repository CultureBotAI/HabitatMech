---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:57:51.166942'
end_time: '2026-08-17T17:08:54.150767'
duration_seconds: 662.98
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: host_animal_endotherm_intratissue
  habitat_identifier: habitatmech:BACDIVE.319ac5f8f8
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'MADIN: host_animal_endotherm_intratissue'
  assertions: '341'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Reviewed and endorsed the seeder's own resolution. Category override\
    \ (#57): a minted identifier gives infer_category nothing to read \u2014 no ontology\
    \ term, no GOLD path \u2014 so every Madin habitat named in the BacDive vocabulary\
    \ fell to OTHER. Inside the tissue of a warm-blooded animal host \u2014 more specific\
    \ than the endotherm source, and host-associated for the same reason. (source\
    \ concept habitatmech:BACDIVE.319ac5f8f8)"
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
  web_search_requests: 15
  num_turns: 43
  total_cost_usd: 3.998705
  session_id: 5d5ad67e-57d9-4ddb-ac1c-f73982bfd6ee
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 44
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** host_animal_endotherm_intratissue
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.319ac5f8f8
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** MADIN: host_animal_endotherm_intratissue
- **Upstream assertion volume:** 341
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Reviewed and endorsed the seeder's own resolution. Category override (#57): a minted identifier gives infer_category nothing to read — no ontology term, no GOLD path — so every Madin habitat named in the BacDive vocabulary fell to OTHER. Inside the tissue of a warm-blooded animal host — more specific than the endotherm source, and host-associated for the same reason. (source concept habitatmech:BACDIVE.319ac5f8f8)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **host_animal_endotherm_intratissue** as a microbial habitat, with citations.

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

# host_animal_endotherm_intratissue — definition research

**HabitatMech identifier:** `habitatmech:BACDIVE.319ac5f8f8` · **Category:** HOST_ASSOCIATED · **Status:** UNGROUNDED · **Upstream volume:** 341 taxa (MADIN, `assertion_unit: TAXON`)

---

## Proposed definition

> An **anatomical entity environment** which is determined by an internal organ, solid tissue or enclosed fluid compartment of an endothermic animal host, lying beneath the host's epithelial surfaces and outside the lumina of its digestive, respiratory and urogenital tracts.

Genus: `ENVO:2100000` *anatomical entity environment* (present in the vendored slice; label verified). Recommended second parent: `ENVO:01001002` *animal-associated environment* (also in slice).

If a curator prefers a single-parent record, `ENVO:01001002` alone is defensible, and the sentence becomes "An animal-associated environment which is determined by an internal organ, solid tissue or enclosed fluid compartment of an endothermic host…". I flag below (§6) that this concept is closer to a **sampling stratum over many anatomical sites** than to one natural habitat, which is the honest reason the sentence needs three disjuncts ("organ, tissue or fluid compartment") — an intermediate class *internal body site environment* is what is actually missing from ENVO.

---

## 1. What the concept denotes

### 1.1 Provenance of the label

The label is not free text. It is a level-4 term in the four-level isolation-source vocabulary of the Madin et al. (2020) bacteria–archaea traits synthesis, which the KG-Microbe `bacdive.isolation_source` vocabulary reuses. The paper states the scheme explicitly:

> "approximately 100 environment labels. The scheme is hierarchical using up to four levels of specificity, for example a one-term label is 'host', a two-term is 'host_animal', a three-term is 'host_animal_endotherm', and a four-term is 'host_animal_endotherm_intestinal'"
> — Madin JS *et al.*, *Sci Data* 7:170 (2020), [doi:10.1038/s41597-020-0497-4](https://doi.org/10.1038/s41597-020-0497-4) ([PMC7275036](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275036/))

So the label parses as **host / animal / endotherm / intratissue**: level 1 the sample is host-associated, level 2 the host is an animal, level 3 the animal is an endotherm, level 4 the sample came from within its tissue.

### 1.2 What it actually denotes, from the upstream mapping table

The strongest evidence of the intended reading is the extensional definition in the project's own conversion table, [`data/conversion_tables/renaming_isolation_source.csv`](https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/blob/master/data/conversion_tables/renaming_isolation_source.csv). 65 free-text isolation-source strings map to `host_animal_endotherm_intratissue`. Grouped:

| Kind of site | Attested source strings (verbatim) |
|---|---|
| Solid organ / parenchyma | `host-associated, mammals, tissue`; `other, human kidney`; `other, liver of vole`; `other, liver of a stranded beaked whale`; `other, spleen of seal`; `spleen of wild mouse`; `spleen tissue from parrot (polytelis)`; `necropsy lung, liver and kidney tissue`; `other, human - heart`; `other, tissue extract`; `appendix tissue` |
| Nervous system / CNS | `brain`; `host-associated, human, nervous system, brain`; `other, brain of pig with meningitis`; `other, human brain abscess` |
| Lymphoid / haematopoietic | `host-associated, human, lymphatic system, lymph nodes`; `other, human cervical lymph node`; `other, lymph node of a pig`; `bone marrow` |
| Enclosed sterile fluids | `csf`; `other, cerebrospinal fluid`; `other, human csf`; `other, human amniotic fluid`; `amniotic fluid` |
| Joint / bone | `other, human osteo-articular sample`; `other, human ankle aspirate`; `knee aspirate of human`; `other, arthritic joint of a calf`; `the wound exudate of bone fracture` |
| Reproductive / gestational | `uterus`; `uterus of a maiden mare`; `ovary from adult female`; `other, equine placenta(s)`; `other, placental tissue of cow`; `other, sow's placenta`; `other, kidney and liver of aborted pig fetus` |
| Focal infection / lesion | `abscess`; `liver abcess material`; `caseous lymphadenitis abscess`; `subcutaneous granuloma`; `wound`; `surgical wound`; `other, breast implant infection`; `other, endocarditis in chicken`; `other, liposarcoma infection` |

Hosts named in these rows span **mammals (human, pig, cow, horse, seal, whale, vole, mouse, calf) and birds (chicken, parrot)** — confirming that "endotherm" here means the Mammalia + Aves reading in practice, not merely "human".

**Reading of the boundary.** The category is *not* strictly "solid tissue". As used, it is **the set of normally microbe-free, internally enclosed body sites of a warm-blooded host** — which is essentially the clinical-microbiology notion of a *normally sterile site*. Public-health surveillance definitions enumerate almost exactly this list: blood; CSF; pleural, peritoneal, pericardial and joint fluid; bone and bone marrow; and "internal body sites — specimens obtained from surgery or aspirate from lymph node, brain, heart, liver, spleen, vitreous fluid, kidney, pancreas, or ovary, and vascular tissue" ([Minnesota DOH, *Normally Sterile Sites: Invasive Bacterial Diseases*](https://www.health.state.mn.us/diseases/invbacterial/sterile.html); [NJ DOH, rev. 02/2024](https://www.nj.gov/health/cd/documents/sterile_sites.pdf); [NZMN Position Statement on Microbiological Specimen Sterility, Sept 2024](https://www.nzmn.org.nz/assets/NZMN/Position-Statements/Current/2024.09-NZMN-Position-Statement-on-Microbiological-Specimen-Sterility-FINAL.pdf)).

*That the Madin extension coincides with the clinical "sterile site" list is my inference from comparing the two lists; neither source states the equivalence.*

### 1.3 Ambiguity — two readings, and which the data means

**Reading A (strict, anatomical):** microorganisms residing *within solid tissue* — interstitium, stroma, parenchyma — as opposed to on mucosal or epithelial surfaces. This is how the word is used in the primary literature that employs it: Wu *et al.* contrasted "intratissue bacterial communities" from oral-lichen-planus **biopsies** against communities swabbed from the **mucosal surface** of the same patients, finding intratissue communities had lower α-diversity and higher β-diversity ([*Sci Rep* 10:3495, 2020](https://www.nature.com/articles/s41598-020-60449-w), [PMC7044275](https://pmc.ncbi.nlm.nih.gov/articles/PMC7044275/)).

**Reading B (as-used, compartmental):** any deep/internal body site normally free of microbes, including enclosed fluids (CSF, amniotic, synovial), abscess and granuloma contents, and surgical wounds.

**The source data means Reading B.** `csf`, `amniotic fluid`, `human ankle aspirate` and `abscess` are not tissue in any anatomical sense, yet all three map here. A definition written to Reading A would exclude a substantial fraction of the 341 attesting taxa.

### 1.4 Known noise in the upstream extension

Four of the 65 mapped strings are mapping artefacts rather than habitat statements and should temper any strong claim about the 341 taxa:

- `culture contaminant` → intratissue
- `other, human clinical specimens` → intratissue (site unspecified)
- `Most frequently encountered serovar. Causes leptospirosis and tubulointerstitial nephritis in Taiwan.` → intratissue (a free-text strain description, matched on "tubulointerstitial")
- `Isolated from a fatal human nocardiosis case at Washington, DC, in the 1970s.` → intratissue

There is also a genuine **upstream inconsistency with `_blood`**: `host-associated, human, circulatory system, blood` → `host_animal_endotherm_blood`, but `host-associated, human, circulatory system, blood, free living` → `host_animal_endotherm_intratissue`; likewise `host-associated, mammals, circulatory system` → `_blood` while `host-associated, animal, circulatory system` → `_intratissue`. So a small number of blood isolates are counted in this record's 341. *This is my direct reading of the conversion table, not a documented caveat.*

---

## 2. Genus — the broader kind

### 2.1 The upstream source itself declares no ENVO term fits

This is the single most useful piece of evidence for keeping the record UNGROUNDED. Madin *et al.* annotated their habitat labels with ENVO and then **withheld the annotations**:

> "These environmental labels were annotated with terms from the Environmental Ontology (ENVO)… however, ENVO annotations do not currently appear in the data products because most environmental terms required the union of multiple ENVO terms"
> — [Madin *et al.* 2020, PMC7275036](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275036/)

And in their [`environments.csv`](https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/blob/master/data/conversion_tables/environments.csv), where sibling rows carry ENVO/UBERON ids, the intratissue row's `ENVO_terms` and `ENVO_ids` columns are **empty**:

```
host_animal_endotherm_oral          → mouth environment        ENVO:08000002
host_animal_endotherm_intestinal    → intestine environment    ENVO:2100002
host_animal_endotherm_surface       → skin environment         ENVO:2100003
host_animal_endotherm_blood         → blood                    UBERON:0000178
host_animal_endotherm_vagina        → vagina                   UBERON:0000996
host_animal_endotherm_nasopharyngeal→ respiratory tract        UBERON:0000065
host_animal_endotherm_intratissue   → (empty)                  (empty)
host_animal_endotherm_rumen         → (empty)                  (empty)
host_animal_endotherm_intracellullar→ (empty)                  (empty)
```

Three of ten endotherm sub-labels were left unmapped by the upstream curators, and this is one of them.

### 2.2 Recommended genus

**`ENVO:2100000` — *anatomical entity environment*** — "An environment which is determined by an anatomical entity." ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:2100000))

This is the established ENVO pattern for exactly this family of concepts. Its existing children are the sibling habitats of this one: *intestine environment* (`ENVO:2100002`), *mouth environment* (`ENVO:08000002`), *skin environment* (`ENVO:2100003`), *digestive tract environment* (`ENVO:01001033`), *bone element environment* (`ENVO:01001306`), *integumental system environment* (`ENVO:2100004`), *feather environment* (`ENVO:2100006`). HabitatMech has already grounded two of this concept's siblings to members of this branch (curation decisions on `host_animal_endotherm_intestinal` → `ENVO:2100002` and `host_animal_endotherm_oral` → `ENVO:08000002`), so using its parent as the genus keeps the sibling set structurally consistent.

**Second parent: `ENVO:01001002` — *animal-associated environment*** — "An environmental system determined by an animal." This carries the host-associatedness that `ENVO:2100000` does not (the latter also subsumes *mushroom environment* and fungal-tissue environments). Note this is an *environment* term, not a taxon term, so attaching it as `parent` does not run into the CLAUDE.md prohibition on parenting to organism classes.

### 2.3 Near-misses and why each fails

| Candidate | Label / definition | Why it is not a match |
|---|---|---|
| `ENVO:01001055` | *environment associated with an animal part or small animal* — "An environmental system determined by part of a living or dead animal, or a whole small animal." | Definitionally the closest thing ENVO has. But it is **too broad** (covers external parts, whole small animals, dead animals) and its asserted subclass tree is a modelling artefact: its descendants via `human settlement` are *city*, *slum*, *village biome*, *business park* (verified on OLS4). Parenting a tissue habitat under a class whose descendants include *city* publishes a structure no source supports. Record as a **related term, not a parent**. |
| `UBERON:0000479` | *tissue* — "Multicellular anatomical structure that consists of many cells of one or a few types…" | It is an anatomical part, so the CLAUDE.md parts rule would permit grounding in principle. It fails on three counts: (a) it is taxon-neutral, so it drops the endotherm restriction entirely, admitting insect and plant tissue; (b) it is an anatomical structure, not an environment — grounding here would make the record's identity a body part rather than a place; (c) the concept's extension includes CSF, amniotic fluid and abscess pus, which are not tissue. Best as `relation: xref`. |
| `ENVO:01001058` | *environment associated with a fungal tissue* | The exact analogue this concept needs — and its existence for **fungi** but not for animals is direct evidence of a gap in ENVO. Wrong kingdom; not a match. |
| `ENVO:01001391` | *gill tissue material* | A narrow ENVO term for one animal tissue, and an aquatic ectotherm one. Illustrates that ENVO handles animal tissue only in one-off special cases. |
| `UBERON:0000178` (blood), `ENVO:2100002` (intestine environment), `ENVO:2100003` (skin environment) | — | All **narrower** than, or **disjoint** from, this concept; each is already the grounding target of a distinct sibling record in this same vocabulary. |
| `ENVO:01001033` | *digestive tract environment* | Narrower and explicitly a lumen; this concept excludes it. |
| ENVO *abscess environment*, *wound environment*, *internal organ environment* | — | **Do not exist.** OLS4 searches of ENVO for "abscess", "wound", "organ environment", "body site" and "host-associated environment" return no relevant class. |

**Conclusion on grounding:** no ENVO, UBERON, FOODON, BTO or PO term names this concept. UNGROUNDED is correct; this is a legitimate term-request candidate, with `ENVO:2100000` and `ENVO:01001002` attached as `parent` and `UBERON:0000479` as `xref`.

---

## 3. Differentia — what distinguishes it from its siblings

Its siblings under the genus are the other nine level-4 splits of `host_animal_endotherm`, plus the ENVO anatomical-entity environments. Four properties separate it, in decreasing order of how well the sources support them.

### 3.1 Location: internal, beneath the epithelium, outside every lumen open to the exterior

This is the load-bearing differentia and the only one that is fully determined by the source data. The nine sibling categories partition the endotherm host as follows (counts = distinct source strings mapping to each, from `renaming_isolation_source.csv`):

| Sibling | n | Compartment |
|---|---|---|
| `_intestinal` | 110 | gut lumen |
| `_feces` | 78 | excreted material |
| `_oral` | 73 | oral cavity |
| `_nasopharyngeal` | 69 | upper respiratory lumen |
| **`_intratissue`** | **65** | **internal / normally sterile** |
| `_blood` | 57 | circulating blood |
| `_surface` | 39 | skin, ear, eye, udder — external surfaces |
| `_rumen` | 25 | forestomach lumen |
| `_vagina` | 17 | vaginal lumen |
| `_intracellullar` | 0 | (declared but unpopulated in the current table) |

Madin's own `environments.csv` groups `_intratissue` under the adjusted habitat class **`host_internal`** (with `_blood`, `_vagina`, `_intracellullar`), as against `gut` (`_intestinal`, `_rumen`), `oral`, and unassigned (`_surface`, `_feces`). This is the upstream curator's own statement that internality is the distinguishing axis.

### 3.2 Host thermal class: the habitat is thermally buffered near the host's regulated core temperature

The level-3 term `endotherm` restricts the host to warm-blooded animals — in the attested data, mammals and birds. Terrestrial vertebrate thermoregulators converge on a core temperature near **37 °C**, and this convergence is treated as a general feature ([Mota-Rojas *et al.* / thermal-physiology review, *Biol Rev*, 2025, PMC12120395](https://pmc.ncbi.nlm.nih.gov/articles/PMC12120395/)). Birds run higher and tolerate more: red-billed quelea sustained body temperatures of 48.0 ± 0.7 °C (individual maxima 49.1 °C) without apparent harm ([O'Connor *et al.*, *R Soc Open Sci*, 2020, PMC7403380](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7403380/)). Note the caution that *endotherm* and *homeotherm* are not synonyms and that heterothermic mammals and birds vary more widely than the term implies (same review).

Madin's parameter row assigns this habitat `Temperature = low`, `temp variability = low` — the "low" is on the scale that reserves "high" for hydrothermal habitats; the informative value is the **low variability**, which is precisely what endothermy supplies.

### 3.3 Physicochemistry

Madin's `environments.csv` row for this label, verbatim:

```
Water=high | water variability=permanently wet | Nutrients=high | Gradients=NA
Organic=high | Structural=medium | Pressure=low | Temperature=low | temp variability=low
Salinity=medium | salinity variability=small | pH=medium | Cobo-Simon habitat=host | CSadj=host_internal
```

The habitat-parameter scheme these bands come from derives from Cobo-Simón M & Tamames J, "Relating genomic characteristics to environmental preferences and ubiquity in different microbial taxa," *BMC Genomics* 18:499 (2017), [doi:10.1186/s12864-017-3888-y](https://doi.org/10.1186/s12864-017-3888-y) ([PMC5492924](https://pmc.ncbi.nlm.nih.gov/articles/PMC5492924/)) — the column is literally named `Cobo-Simon habitat`.

Two properties that the parameter table does *not* capture but that the primary literature does, and that are the most discriminating physicochemical features of this habitat:

- **Physioxia, not air.** Tissue oxygen tensions are far below atmospheric: roughly 3–11 % O₂ across organs, with reported mean tissue values of brain 4.4 %, liver 5.4 %, kidney 9.5 %, muscle 3.8 %, bone marrow 6.4 % (Keeley TP & Mann GE, "Defining Physiological Normoxia for Improved Translation of Cell Physiology to Animal Models and Humans," *Physiol Rev* 99:161–234, 2019, [doi:10.1152/physrev.00041.2017](https://journals.physiology.org/doi/full/10.1152/physrev.00041.2017)). At infection foci and in wounds, O₂ falls below 1 %, and the resulting hypoxia is itself created by microbial and immune-cell respiration and modulates virulence ([Lopes Fischer *et al.* / "The battle for oxygen during bacterial and fungal infections," *Trends Microbiol* 30, 2022](https://www.sciencedirect.com/science/article/abs/pii/S0966842X22000026); [Taylor & Colgan, *Nat Rev Immunol*, PMC5799081](https://pmc.ncbi.nlm.nih.gov/articles/PMC5799081/)).
- **Transition-metal restriction (nutritional immunity).** Host tissue actively withholds Fe, Mn and Zn from invading microbes; calprotectin-mediated metal chelation in **tissue abscesses** is the canonical demonstration (Corbin BD *et al.*, "Metal chelation and inhibition of bacterial growth in tissue abscesses," *Science* 319:962–965, 2008). Reviews: Hood MI & Skaar EP, *Nat Rev Microbiol* 10:525–537 (2012), [doi:10.1038/nrmicro2836](https://www.nature.com/articles/nrmicro2836); Murdoch CC & Skaar EP, "Nutritional immunity: the battle for nutrient metals at the host–pathogen interface," *Nat Rev Microbiol* (2022), [doi:10.1038/s41579-022-00745-6](https://www.nature.com/articles/s41579-022-00745-6); Zygiel EM & Nolan EM, *Annu Rev Biochem* 87:621–643 (2018), [doi:10.1146/annurev-biochem-062917-012312](https://www.annualreviews.org/doi/10.1146/annurev-biochem-062917-012312). This is arguably the sharpest physiological contrast with the *nutrient-replete* gut and oral siblings, which Madin's own table also scores `Nutrients = high` — the parameter table cannot distinguish them, but nutritional immunity does.

### 3.4 Colonisation mode: invasion, not residency

Because these sites are normally microbe-free, recovering an organism from one is generally read as evidence of infection rather than commensalism, whereas recovery from non-sterile sites may represent colonisation or contamination — which is why laboratories reserve full identification and susceptibility workup for sterile-site isolates ([NZMN 2024](https://www.nzmn.org.nz/assets/NZMN/Position-Statements/Current/2024.09-NZMN-Position-Statement-on-Microbiological-Specimen-Sterility-FINAL.pdf); [UCSF Clinical Laboratories microbiology guide](https://clinlab.ucsf.edu/microbiology-guide)). The same framework distinguishes invasive infection — dissemination to deep internal body sites, fluid compartments and deep tissues, usually haematogenously — from superficial infection of surfaces.

The taxa attesting this record are consistent with that: *Neisseria meningitidis* (16 of the first 25 strains), *Streptococcus pneumoniae*, *Haemophilus haemolyticus*, *Escherichia coli* O7:K1 (a neonatal-meningitis K1 strain), *Legionella cardiaca*, *Corynebacterium uterequi*, *Camelimonas abortus*, *Arcobacter cryaerophilus* — invasive and abortifacient organisms, not gut commensals. *That the taxon profile matches the "invasion" reading is my observation from the record, not a source claim.*

---

## 4. Synonyms and what NOT to conflate

### In real use for this concept

- **normally sterile site** / **sterile-site specimen** — the clinical-microbiology and public-health-surveillance term; the closest thing to a standard name ([MN DOH](https://www.health.state.mn.us/diseases/invbacterial/sterile.html), [NC DPH](https://epi.dph.ncdhhs.gov/cd/lhds/manuals/cd/strep/NormallySterileSites.pdf), [PA DOH, Mar 2025](https://www.pa.gov/content/dam/copapwp-pagov/en/health/documents/topics/documents/programs/haip-as/Normally%20Sterile%20Sites.pdf))
- **deep tissue** / **internal body site** / **deep body site**
- **invasive isolate** (of the strain, not the site)
- **tissue microbiome** / **tissue-resident microbiota** — the sequencing-era name
- **intratissue microbiome** — used, but see the caveat below
- GOLD's nearest paths, all already in `data/raw/gold_ecosystem_paths.tsv`: `Host-associated > Mammals > Unspecified system > Unspecified organ > Unspecified tissue`; `Host-associated > Mammals > Multiple systems > Soft tissue`; `Host-associated > Mammals > Lymphatic system > Lymph nodes | Spleen`; `Host-associated > Mammals > Fetus > Fetal tissue > Placenta`; `Host-associated > Mammals: Human > Nervous system > Spinal cord > Abscess`

**Caution on the label itself:** *intratissue* is **not a MeSH term and has no formal definition in microbiology**. It is a descriptive compound used ad hoc, and readers routinely misread it as *intracellular*. It should be defined on first use. Literature search for this habitat is better done under "tissue microbiome", "tissue-resident bacteria" or "intratumoral microbiota" ([Wu *et al.* 2020](https://www.nature.com/articles/s41598-020-60449-w) is the clearest published use of the exact word).

### Commonly but wrongly treated as the same thing

| Do not conflate with | Why not |
|---|---|
| **intracellular** (`host_animal_endotherm_intracellullar`) | A *localisation mechanism* (inside host cells), not a compartment. Madin declares it as a separate level-4 sibling. Most intratissue organisms are extracellular or facultatively intracellular. |
| **blood** (`host_animal_endotherm_blood`) | A separate sibling with 57 mapped strings and its own grounding (`UBERON:0000178`). Circulating blood is a transit compartment, not a tissue. (Upstream mapping leaks a few blood rows into intratissue — §1.4.) |
| **wound swab / skin lesion** | Surface-swab material maps to `_surface` upstream (`human - skin, thumb wound`), while *deep* wound and abscess material maps here. The differentia is depth, not the word "wound". Note the sterile-site definitions that qualify joint fluid as sterile "only when the joint surface is intact (no abscess or break in skin)". |
| **UBERON:0000479 *tissue*** | An anatomical structure class, taxon-neutral; not a place and not endotherm-restricted. |
| **`ENVO:01001055` *environment associated with an animal part or small animal*** | Broader; its ENVO subclass tree descends into *city* and *human settlement*. |
| **host-associated in general (`ENVO:01001001`/`ENVO:01001002` used loosely)** | Gut, skin, oral and vaginal habitats are all host-associated and all explicitly *excluded* here. |
| **intratumoral microbiota** | A proper subset at best, and the subset with the worst contamination record (below). |
| **the host taxon** (Mammalia, Aves) | Per HabitatMech convention, the taxon is not the habitat. No taxon term belongs on this record even as a parent. |

---

## 5. Should it be a term at all?

**Yes — it denotes places, so `NOT_APPLICABLE` would be wrong.** Brains, spleens, lymph nodes, joints and abscess cavities are physical settings that microorganisms occupy and that samples are taken from. This is not a disease, a quality, a process, a procedure, or a taxonomic grouping. It should keep its minted identity with ontology parents attached.

Three caveats a curator should carry into the definition, in descending order of importance:

**(a) It is a coarse stratum, not one natural habitat.** Brain parenchyma, bone marrow, synovial fluid, placenta and a caseous granuloma differ from each other far more than the gut differs from the mouth. The concept coheres as *"the residual internal compartment, once gut, mouth, nose, vagina, skin, faeces and blood have been split off"* — a partition boundary, not a shared physicochemistry. This is also why the definition sentence needs three disjuncts, and it is the argument for saying an **intermediate ENVO class (*internal body site environment* / *sterile body site environment*) is what is actually missing**, rather than lengthening the sentence. MIxS guidance points the same way: for host-associated samples the environmental triad is populated with **UBERON anatomical terms plus a separate host taxon field**, i.e. the community's answer to this problem is two fields, not one coarse habitat label ([ENVO wiki, *Using ENVO with MIxS*](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS); [MIxS `env_local_scale`](https://genomicsstandardsconsortium.github.io/mixs/0000013/); [ENVO issue #1029, *EnvO terms for host-associated samples*](https://github.com/EnvironmentOntology/envo/issues/1029)).

**(b) Part of the attestation is a sampling artefact, and this habitat is the one where that risk is highest.** Four of 65 mapped strings are noise (§1.4), and beyond the mapping, this is the compartment where the microbiome literature has most often mistaken reagent contamination for biology. De Goffau *et al.*, "Human placenta has no microbiome but can contain potential pathogens," *Nature* 572:329–334 (2019), [doi:10.1038/s41586-019-1451-5](https://www.nature.com/articles/s41586-019-1451-5), found signals in 537 placental biopsies traced almost entirely to intrapartum acquisition or reagent contamination — and `other, equine placenta`, `other, sow's placenta`, `placental tissue of cow` all map to this record. See also Kennedy *et al.*, "Questioning the fetal microbiome illustrates pitfalls of low-biomass microbial studies," *Nature* 613:639–649 (2023), [doi:10.1038/s41586-022-05546-8](https://www.nature.com/articles/s41586-022-05546-8); Gihawi *et al.*, "Major data analysis errors invalidate cancer microbiome findings," *mBio* (2023), [doi:10.1128/mbio.01607-23](https://journals.asm.org/doi/10.1128/mbio.01607-23); and the 2025 consensus guidance, "Guidelines for preventing and reporting contamination in low-biomass microbiome studies," *Nat Microbiol* (2025), [doi:10.1038/s41564-025-02035-2](https://www.nature.com/articles/s41564-025-02035-2). **Nothing in this caveat undermines the 341 records here**, which are BacDive *cultured-strain isolation sources* rather than amplicon surveys — but a definition should not assert a resident tissue microbiota, only that microorganisms are recovered from these sites.

**(c) Do not write "sterile" into the definition.** "Normally sterile site" is the right synonym and the right pointer to the literature, but a habitat defined as sterile is self-contradictory. The definition should say *internal / beneath the epithelium / outside the tracts*; the sterility framing belongs in a comment.

### Suggested curation disposition

- **Decision:** `CONFIRM_UNGROUNDED` on `habitatmech:BACDIVE.319ac5f8f8`, with parents attached — `ENVO:2100000` *anatomical entity environment* (`relation: parent`), `ENVO:01001002` *animal-associated environment* (`relation: parent`), `UBERON:0000479` *tissue* (`relation: xref`).
- **Term request:** an ENVO *internal body site environment* (or *animal internal body site environment*), sibling to `ENVO:01001058` *environment associated with a fungal tissue* — noting the pointed asymmetry that ENVO has a fungal-tissue environment class and no animal-tissue one. Per standing memory, an ENVO submission needs explicit per-request permission and is **not** authorised by this research.
- **Note claims that `tests/test_decisions.py` will check:** all four CURIEs above are present in `data/raw/ontology_terms.tsv` with the labels quoted here (verified: `ENVO:2100000` "anatomical entity environment", `ENVO:01001002` "animal-associated environment", `ENVO:01001055` "environment associated with an animal part or small animal", `UBERON:0000479` "tissue").

---

## Sources

**Primary source vocabulary**
- Madin JS, Nielsen DA, Brbic M, Corkrey R, Danko D, Edwards K, *et al.* "A synthesis of bacterial and archaeal phenotypic trait data." *Sci Data* 7:170 (2020). https://doi.org/10.1038/s41597-020-0497-4 · [PMC7275036](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275036/) · [Nature](https://www.nature.com/articles/s41597-020-0497-4)
- bacteria-archaea-traits repository, conversion tables `renaming_isolation_source.csv` and `environments.csv` (v1.0.0). https://github.com/bacteria-archaea-traits/bacteria-archaea-traits · [release v1.0.0](https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/releases/tag/v1.0.0) · [Open Traits Network entry](https://opentraits.org/datasets/madin-2020.html)
- Cobo-Simón M & Tamames J. "Relating genomic characteristics to environmental preferences and ubiquity in different microbial taxa." *BMC Genomics* 18:499 (2017). https://doi.org/10.1186/s12864-017-3888-y · [PMC5492924](https://pmc.ncbi.nlm.nih.gov/articles/PMC5492924/) · [Springer](https://link.springer.com/article/10.1186/s12864-017-3888-y)

**Ontology / standards**
- ENVO via OLS4 — `ENVO:2100000`, `ENVO:01001002`, `ENVO:01001055`, `ENVO:01001058`, `UBERON:0000479`. https://www.ebi.ac.uk/ols4/ontologies/envo
- ENVO wiki, "Using ENVO with MIxS." https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
- ENVO issue #1029, "EnvO terms for host-associated samples." https://github.com/EnvironmentOntology/envo/issues/1029
- GSC MIxS schema, slot `env_local_scale`. https://genomicsstandardsconsortium.github.io/mixs/0000013/ · https://genomicsstandardsconsortium.github.io/mixs/
- Holmes I, *et al.* "MIxS-SA: a MIxS extension … for symbiont-associated micro-organisms." *ISME Commun* (2022). https://www.nature.com/articles/s43705-022-00092-w · [PMC9723553](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9723553/)

**Normally sterile sites**
- Minnesota Department of Health, "Normally Sterile Sites: Invasive Bacterial Diseases." https://www.health.state.mn.us/diseases/invbacterial/sterile.html
- North Carolina DPH. https://epi.dph.ncdhhs.gov/cd/lhds/manuals/cd/strep/NormallySterileSites.pdf
- Pennsylvania DOH, March 2025. https://www.pa.gov/content/dam/copapwp-pagov/en/health/documents/topics/documents/programs/haip-as/Normally%20Sterile%20Sites.pdf
- New Jersey DOH, rev. 02/2024. https://www.nj.gov/health/cd/documents/sterile_sites.pdf
- NZ Microbiology Network, "Position Statement on Microbiological Specimen Sterility," Sept 2024. https://www.nzmn.org.nz/assets/NZMN/Position-Statements/Current/2024.09-NZMN-Position-Statement-on-Microbiological-Specimen-Sterility-FINAL.pdf
- UCSF Clinical Laboratories microbiology guide. https://clinlab.ucsf.edu/microbiology-guide

**Habitat physicochemistry**
- Keeley TP & Mann GE. "Defining Physiological Normoxia for Improved Translation of Cell Physiology to Animal Models and Humans." *Physiol Rev* 99:161–234 (2019). https://doi.org/10.1152/physrev.00041.2017
- "The battle for oxygen during bacterial and fungal infections." *Trends Microbiol* 30 (2022). https://www.sciencedirect.com/science/article/abs/pii/S0966842X22000026
- Taylor CT & Colgan SP. "Regulation of immunity and inflammation by hypoxia in immunological niches." [PMC5799081](https://pmc.ncbi.nlm.nih.gov/articles/PMC5799081/)
- Corbin BD *et al.* "Metal chelation and inhibition of bacterial growth in tissue abscesses." *Science* 319:962–965 (2008).
- Hood MI & Skaar EP. "Nutritional immunity: transition metals at the pathogen–host interface." *Nat Rev Microbiol* 10:525–537 (2012). https://www.nature.com/articles/nrmicro2836
- Murdoch CC & Skaar EP. "Nutritional immunity: the battle for nutrient metals at the host–pathogen interface." *Nat Rev Microbiol* (2022). https://www.nature.com/articles/s41579-022-00745-6
- Zygiel EM & Nolan EM. "Transition metal sequestration by the host-defense protein calprotectin." *Annu Rev Biochem* 87:621–643 (2018). https://www.annualreviews.org/doi/10.1146/annurev-biochem-062917-012312

**Endothermy**
- Thermal-physiology review, "Revisiting concepts of thermal physiology…" *Biol Rev* (2025). [PMC12120395](https://pmc.ncbi.nlm.nih.gov/articles/PMC12120395/)
- "Extreme hyperthermia tolerance in the world's most abundant wild bird." [PMC7403380](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7403380/)
- "The Physiology of Heat Tolerance in Small Endotherms." *Physiology* (2019). https://journals.physiology.org/doi/full/10.1152/physiol.00011.2019

**Use of the term "intratissue" and low-biomass caveats**
- Wu H, *et al.* "Characterization of intratissue bacterial communities and isolation of *Escherichia coli* from oral lichen planus lesions." *Sci Rep* 10:3495 (2020). https://www.nature.com/articles/s41598-020-60449-w · [PMC7044275](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7044275/)
- de Goffau MC, *et al.* "Human placenta has no microbiome but can contain potential pathogens." *Nature* 572:329–334 (2019). https://www.nature.com/articles/s41586-019-1451-5 (author correction: https://www.nature.com/articles/s41586-019-1628-y)
- Kennedy KM, *et al.* "Questioning the fetal microbiome illustrates pitfalls of low-biomass microbial studies." *Nature* 613:639–649 (2023). https://www.nature.com/articles/s41586-022-05546-8
- Gihawi A, *et al.* "Major data analysis errors invalidate cancer microbiome findings." *mBio* (2023). https://journals.asm.org/doi/10.1128/mbio.01607-23
- "Guidelines for preventing and reporting contamination in low-biomass microbiome studies." *Nat Microbiol* (2025). https://www.nature.com/articles/s41564-025-02035-2
- "Evidence for contamination as the origin for bacteria found in human placenta rather than a microbiota." *PLOS ONE* (2020). https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0237232

## Citations

1. https://doi.org/10.1038/s41597-020-0497-4
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC7275036/
3. https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/blob/master/data/conversion_tables/renaming_isolation_source.csv
4. https://www.health.state.mn.us/diseases/invbacterial/sterile.html
5. https://www.nj.gov/health/cd/documents/sterile_sites.pdf
6. https://www.nzmn.org.nz/assets/NZMN/Position-Statements/Current/2024.09-NZMN-Position-Statement-on-Microbiological-Specimen-Sterility-FINAL.pdf
7. https://www.nature.com/articles/s41598-020-60449-w
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC7044275/
9. https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/blob/master/data/conversion_tables/environments.csv
10. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:2100000
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC12120395/
12. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7403380/
13. https://doi.org/10.1186/s12864-017-3888-y
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC5492924/
15. https://journals.physiology.org/doi/full/10.1152/physrev.00041.2017
16. https://www.sciencedirect.com/science/article/abs/pii/S0966842X22000026
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC5799081/
18. https://www.nature.com/articles/nrmicro2836
19. https://www.nature.com/articles/s41579-022-00745-6
20. https://www.annualreviews.org/doi/10.1146/annurev-biochem-062917-012312
21. https://clinlab.ucsf.edu/microbiology-guide
22. https://epi.dph.ncdhhs.gov/cd/lhds/manuals/cd/strep/NormallySterileSites.pdf
23. https://www.pa.gov/content/dam/copapwp-pagov/en/health/documents/topics/documents/programs/haip-as/Normally%20Sterile%20Sites.pdf
24. https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
25. https://genomicsstandardsconsortium.github.io/mixs/0000013/
26. https://github.com/EnvironmentOntology/envo/issues/1029
27. https://www.nature.com/articles/s41586-019-1451-5
28. https://www.nature.com/articles/s41586-022-05546-8
29. https://journals.asm.org/doi/10.1128/mbio.01607-23
30. https://www.nature.com/articles/s41564-025-02035-2
31. https://www.nature.com/articles/s41597-020-0497-4
32. https://github.com/bacteria-archaea-traits/bacteria-archaea-traits
33. https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/releases/tag/v1.0.0
34. https://opentraits.org/datasets/madin-2020.html
35. https://link.springer.com/article/10.1186/s12864-017-3888-y
36. https://www.ebi.ac.uk/ols4/ontologies/envo
37. https://genomicsstandardsconsortium.github.io/mixs/
38. https://www.nature.com/articles/s43705-022-00092-w
39. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9723553/
40. https://doi.org/10.1152/physrev.00041.2017
41. https://journals.physiology.org/doi/full/10.1152/physiol.00011.2019
42. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7044275/
43. https://www.nature.com/articles/s41586-019-1628-y
44. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0237232