---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T00:42:23.650685'
end_time: '2026-08-18T00:51:44.573584'
duration_seconds: 560.92
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Gall
  habitat_identifier: habitatmech:BACDIVE.f4971616a5
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Gall'
  assertions: '16'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. GOLD''s
    plant context means a plant gall; the proposal offered bile material, which is
    a different thing entirely. No plant-gall term in the vendored slice. ENVO term
    request. Path: Gall (source concept habitatmech:BACDIVE.f4971616a5)'
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
  web_search_requests: 16
  num_turns: 28
  total_cost_usd: 3.1495580000000007
  session_id: 926697fb-29fd-44c6-bbd8-0401cb26dc14
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 32
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Gall
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.f4971616a5
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Gall
- **Upstream assertion volume:** 16
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. GOLD's plant context means a plant gall; the proposal offered bile material, which is a different thing entirely. No plant-gall term in the vendored slice. ENVO term request. Path: Gall (source concept habitatmech:BACDIVE.f4971616a5)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Gall** as a microbial habitat, with citations.

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

> **A multi-tissue plant structure which develops in response to a biotic stress — a localized outgrowth of hypertrophied and hyperplastic host tissue induced and inhabited by another organism (bacterium, fungus, nematode, insect or mite), enclosing nutritive tissue that the inducer and its associated microbiota feed on.**

That sentence is a paraphrase of an existing ontology term, and that is the main finding: **this concept does not need a new term.** `PO:0025626 'plant gall'` exists, is in this repo's vendored slice, and is already used by another HabitatMech record. See §0 before reading further.

---

## 0. Disposition first: the recorded note is wrong on its central fact

The `CONFIRM_UNGROUNDED` note on `habitatmech:BACDIVE.f4971616a5` says "No plant-gall term in the vendored slice. ENVO term request." Checking the slice:

```
data/raw/ontology_terms.tsv:
PO:0025626   PO   plant gall   A multi-tissue plant structure (PO:0025496) that
                               develops in response to a biotic stress (PSO:0000011).
BTO:0005833  BTO  plant gall   An abnormal growth of plant tissue caused by an organism,
                               such as an insect, mite, or bacterium, or by a wound.
```

Both are present. Four days after this note was written (2026-08-12 → 2026-08-16), a different curator pass grounded GOLD's `Host-associated > Plants > Roots > Galls` to `PO:0025626` as **EXACT**, producing `data/habitats/host_associated/plant_gall.yaml`, and that note explicitly says "`PO:0025626 'plant gall'` is the term, and it is already in the slice." The two decisions contradict each other on a checkable fact, and the GOLD one is the correct one.

**Recommended decision:** `GROUND` → `PO:0025626` / `plant gall` (EXACT), which merges the 16 BacDive strains into the existing `plant_gall` record as a second attestation. Three caveats a curator must handle, detailed in §7:

1. the upstream kg-microbe cell is deliberately empty (`family_mismatch_fix`), so this must be an explicit `decisions.tsv` override, not a lexical re-grounding;
2. the existing record carries `parent_habitats: [PO:0009005 root, PO:0025496]`, and `root` is over-narrow for the BacDive strains (stem, crown, bud and leaf galls);
3. one of the 12 BacDive taxa (`Schaalia odontolytica`) is probably a bile/gallbladder mis-file, not a plant gall.

Everything below is the supporting evidence, written so it also serves as the definition material if the curator instead wants an `<X>-associated environment`-style habitat term (§2.3).

---

## 1. What the concept denotes

### 1.1 The reading the data means

A **plant gall**: a discrete, abnormal swelling or outgrowth of plant tissue whose development is induced by a parasitic or pathogenic organism, and which encloses or is colonized by that inducer. It is a *place a sample is taken from* — a curator excises the gall (or its interior tissue and larval chamber) and plates or sequences it.

The label alone is ambiguous, but the attestation is not. All 16 BacDive strains sit under `bacdive.isolation_source:gall`, spread over 12 taxa, and the plant-gall signal is overwhelming:

| Taxon (as BacDive names it) | Strains | What "gall" means for it |
|---|---|---|
| *Agrobacterium radiobacter* (NCBITaxon:362) | 5 | crown gall — the canonical Ti-plasmid tumour |
| *Rhizobium nepotum* (→ *Agrobacterium nepotum*) | 1 | described from plant tumours, Poland/Hungary ([Puławska et al. 2012](https://doi.org/10.1016/j.syapm.2012.03.001)) |
| *Rhizobium skierniewicense* (→ *A. skierniewicense*) | 1 | described from tumours on chrysanthemum and cherry plum ([Puławska et al. 2012](https://doi.org/10.1099/ijs.0.032532-0)) |
| *Martinezella rhizogenes* (NCBITaxon:359, = *A./R. rhizogenes*) | 1 | Ri-plasmid hairy-root / cane-gall agent |
| *Leifsonia poae* (NCBITaxon:110933) | 1 | root galls induced by the nematode *Subanguina radicicola* on *Poa annua* ([PMID 10826825](https://pubmed.ncbi.nlm.nih.gov/10826825/)) |
| *Agreia bicolorata* + *Agreia* sp. VKM Ac-1783 | 2 | leaf galls induced by *Heteroanguina graminophila* on *Calamagrostis neglecta* ([PMID 11760949](https://pubmed.ncbi.nlm.nih.gov/11760949/)) |
| *Rathayibacter festucae* DSM 15932 | 1 | nematode-vectored seed/leaf galls of grasses |
| *Nocardia vaccinii* NBRC 15922 | 1 | stem/bud-proliferating galls of blueberry (Demaree & Smith, *Phytopathology* 42:249–252, 1952) |
| *Pseudomonas* sp., *P. mandelii* | 2 | unresolved; *Pseudomonas* is a routine gall co-inhabitant (§3.4) |
| *Schaalia odontolytica* (NCBITaxon:1660) | 1 | **doubtful** — an oral/dental organism; see §1.3 |

Eleven of twelve taxa are plant-gall organisms and nine of them were *described from* gall material. Source: `data/raw/bacdive_source_taxa.tsv`, cross-checked against LPSN and the original species descriptions.

### 1.2 Boundary — what is inside and what is next door

**Inside the concept:** crown galls and cane galls (Rhizobiaceae, Ti/Ri plasmid); olive knots (*Pseudomonas savastanoi* pv. *savastanoi*); bacterial bud/stem galls (*Nocardia vaccinii*); nematode-induced root knots (*Meloidogyne*), root galls (*Subanguina*), leaf and seed galls (*Anguina*, *Heteroanguina*, *Mesoanguina*); insect and mite galls (Cynipidae, Cecidomyiidae, Eriophyidae) including their larval chamber, nutritive tissue and gall cortex; fungal galls (e.g. *Exobasidium*). Galls on any organ — root, crown, stem, bud, leaf, flower, seed.

**Neighbouring, not inside:**

- **Root nodule** (`BTO:0001190`, whose own gloss calls nodules "gall-like structures") — a mutualistic, plant-genetically-programmed organ, not a stress response to a parasite. Not a gall.
- **Callus / wound tissue** — abiotic or purely mechanical injury. Note that `BTO:0005833`'s definition explicitly admits growths caused "by a wound," making BTO's term *broader* than PO's biotic-stress-only reading. PO is the tighter fit to the data.
- **Hairy root disease** (*R. rhizogenes*/Ri plasmid) — adventitious root proliferation rather than an undifferentiated swelling; usually lumped with galls in isolation-source records, and one BacDive strain here is *M. rhizogenes*. Inference, flagged.
- **The disease, not the place** — `BTO:0000303 'crown gall'` is defined as *a disease*. Grounding a habitat to it would be a category error of exactly the kind `tests/test_decisions.py` guards against.
- **The inducer** — a gall wasp larva or a nematode is an organism, not the habitat; galls hosting them are still plant tissue.

### 1.3 The other reading, and why it loses

"Gall" is an archaic English synonym for **bile**, and this is a live trap in this corpus: `ENVO:02000023 'bile material'` carries `gall` as a synonym in the vendored slice, `BTO:0000493 'gall bladder'` exists, and GOLD has `Host-associated > Fish > Digestive system > Biliary tract > Gall bladder`. The GOLD grounding note records that the automated variant-match route reached `UBERON:0001970 'BILE'` for exactly this reason, and the kg-microbe mapping row for this BacDive source was blanked with the justification `family_mismatch_fix` — consistent with an upstream curator deleting a wrong bile/gallbladder mapping rather than judging the concept unnameable.

The single BacDive taxon that fits the bile reading is *Schaalia odontolytica* (formerly *Actinomyces odontolyticus*), an oral/dental organism. It has been recovered from bile in sporadic clinical cases ([Yamamoto et al., *BMC Infect Dis* 22:499, 2022](https://doi.org/10.1186/s12879-022-07491-3)), but I found **no** deposited BacDive strain of it with a bile or gallbladder isolation source — the deposited strains are from caries, blood, urine, pus, synovial fluid and wounds. So this attestation is unexplained either way; treat it as one likely-mislabelled strain out of 16 (1 assertion of 16), not as evidence for a second sense. My inference, not a source's claim.

---

## 2. Genus — the broader kind

### 2.1 The match (in the slice, already used)

| CURIE | Label | Definition | Verdict |
|---|---|---|---|
| **`PO:0025626`** | **plant gall** | *A multi-tissue plant structure (PO:0025496) that develops in response to a biotic stress (PSO:0000011).* | **Exact match.** In the slice; added to PO 2024-02-14 via `PO_GIT:641`; its only asserted parent is `PO:0025496`. |
| `PO:0025496` | multi-tissue plant structure | a plant structure with ≥2 tissue types forming one unit demarcated by bona-fide boundaries | The **genus** the definition starts from. In slice. |
| `BTO:0005833` | plant gall | *An abnormal growth of plant tissue caused by an organism, such as an insect, mite, or bacterium, or by a wound.* | Near-match, slightly **broader** (admits wound callus). In slice. Use as `xref`, not identity. |
| `GALLONT:0000025` | plant gall | *A multi-tissue plant structure (PO:0025496) that develops in response to a biotic stress (PSO:0000004).* | Same definition, from the dedicated gall ontology ([Deans et al. 2024](https://doi.org/10.3897/BDJ.12.e128585)). **Not in the slice**; GallOnt also supplies `plant gall cavity` (`GALLONT:0000003`), `nutritive tissue` (`GALLONT:0000040`) and `zoocecidium` (`GALLONT:0000050`) if finer habitat granularity is ever wanted. |

Under this repo's rule that **a host's parts ground to the anatomy term while the whole organism does not**, a gall is unambiguously a part — plant tissue on a plant, like `cocoon` is a structure rather than the insect. Grounding to PO is right and routine here.

### 2.2 ENVO near-misses (checked; none fit)

A full-text OLS search of ENVO for "gall" returns exactly one class — `ENVO:02000023 'bile material'`, matched on its `gall` synonym. **ENVO has no plant-gall term.** The nearest candidates, and why each fails:

- `ENVO:01001057 'environment associated with a plant part or small plant'` — *broader*, not a match; this is the correct ENVO **parent** if a habitat-flavoured term is ever requested.
- `ENVO:01001001 'plant-associated environment'` — broader still (any environment determined by a green plant).
- `ENVO:01001032 'environment determined by a biofilm on a plant surface'` — asserts a surface biofilm; gall microbiota are largely endophytic in the gall's internal tissue. Asserts something the sources do not.
- `ENVO:01001121 'plant matter'` — a material, not a structure, and does not carry the induced-abnormality claim.
- `ENVO:02000023 'bile material'` — the lexical trap of §1.3. Not applicable.

### 2.3 If a habitat-flavoured term is nonetheless wanted

An ENVO request would read: *plant gall environment* — "An environment associated with a plant part (`ENVO:01001057`) which is determined by a plant gall (`PO:0025626`)." Filing that is optional; grounding to PO discharges the concept today, and the GOLD-derived sibling record already sets the corpus precedent.

---

## 3. Differentia — what separates a gall from its siblings under "multi-tissue plant structure"

Each property below is observable or measurable, and each is cited.

### 3.1 Induced by another organism, not by the plant's own developmental programme
Galls are induced by viruses, phytoplasmas, bacteria, fungi, nematodes, insects, mites and parasitic plants; the inducer secretes effectors or growth regulators that hijack host developmental programmes, producing ectopic cell proliferation and expansion ([Britannica, "gall (botany)"](https://www.britannica.com/science/gall-botany); [Recent Progress Regarding the Molecular Aspects of Insect Gall Formation, PMC8430891](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8430891/)). This is the differentia PO encodes as "develops in response to a biotic stress." It is what excludes root nodules and wound callus.

### 3.2 The inducer creates a nutrient sink with dedicated nutritive tissue
The gall is a physiological sink: assimilates are imported and stored, principally as starch, which — being non-transportable — must be synthesized in situ. Typical nutritive tissue lining the larval chamber has dense cytoplasm, hypertrophied nuclei, dedifferentiated plastids and modified walls, and supplies reducing sugars from starch hydrolysis by invertase/sucrose synthase; storage and defence compounds are spatially compartmentalized, with condensed tannins concentrated in cortex and epidermis away from the feeding zone (Shorthouse & Rohfritsch, *Biology of Insect-Induced Galls*, OUP 1992; [Ferreira et al., *J Insect Physiol*, PMID 26620152](https://pubmed.ncbi.nlm.nih.gov/26620152/); [Allison & Schultz, *J Chem Ecol* 31:151–166, 2005](https://doi.org/10.1007/s10886-005-0981-5); [Formiga et al. on metabolite gradients, PMC4568204](https://ncbi.nlm.nih.gov/pmc/articles/PMC4568204)). **For a microbiologist this is the point:** the gall interior is a nutrient-enriched, water-rich, physically enclosed compartment with chemistry unlike the surrounding organ.

### 3.3 In bacterial galls, a chemically private nutrient supply — opines
Ti-plasmid T-DNA transferred into host cells makes the gall synthesize and secrete opines, which few other organisms can catabolize, so the pathogen builds a semi-exclusive niche for itself; opines nonetheless leak to other gall colonizers ([Kuzmanović et al., "Insights into the Gallobiome," *Phytobiomes J.*](https://apsjournals.apsnet.org/doi/10.1094/PBIOMES-09-23-0090-R); [Gelvin, ASM review 2023, PMC10127608](https://pmc.ncbi.nlm.nih.gov/articles/PMC10127608/); ChEBI `CHEBI:82803 'opine'`). This differentiates gall interiors from any other plant tissue.

### 3.4 The gall carries a community distinct from adjacent healthy tissue — it is a habitat, empirically
- **Crown gall / "gallobiome":** rhododendron aerial galls host a reproducible bacterial pathobiome beyond the tumorigenic agrobacteria ([Phytobiomes J., 2024](https://apsjournals.apsnet.org/doi/10.1094/PBIOMES-09-23-0090-R)).
- **Nematode galls:** in tomato, gall communities are structurally distinct from healthy and from diseased-but-ungalled root, dominated by Proteobacteria + Bacteroidetes (~92.7%), and functionally enriched for plant-polysaccharide degradation and N fixation ([Tian et al., *Sci Rep* 5:17087, 2015](https://www.nature.com/articles/srep17087)); in eggplant, gall communities diverge from adjacent non-gall root segments and follow their own succession ([Toju/Cabos-style longitudinal study, *mSphere* 5:e00306-20](https://journals.asm.org/doi/10.1128/msphere.00306-20)); rice galls harbour genera absent from uninfected root (*Chryseobacterium*, *Rhizobium*, *Gemmata*, *Pseudomonas*) ([*Ann Microbiol* 74, 2024](https://link.springer.com/article/10.1186/s13213-024-01789-0)); endophytic N-fixer composition tracks gall vs non-gall tissue ([*Microbiome* 11, 2023](https://link.springer.com/article/10.1186/s40168-023-01484-3)).
- **Olive knot:** the knot is an established model multispecies niche, with *Erwinia toletana*, *E. oleae* and *Pantoea* cohabiting with and aggravating *P. savastanoi* via shared AHL quorum signalling ([Buonaurio et al., *Front Plant Sci* 6:434, 2015](https://doi.org/10.3389/fpls.2015.00434); [*Microorganisms* 10:1529, 2022](https://doi.org/10.3390/microorganisms10081529)).
- **Nematode-vectored grass galls:** *Rathayibacter toxicus* is carried on the cuticle of *Anguina* J2 juveniles into developing seed galls, where it multiplies on gall and adjoining tissue and produces tunicamycin — the mechanism behind annual ryegrass toxicity, and the reason APHIS lists it as a select agent ([Murray et al., *Phytopathology* 107:804–815, 2017](https://apsjournals.apsnet.org/doi/full/10.1094/PHYTO-02-17-0047-RVW); [*Annu Rev Phytopathol*, seed gall nematodes and toxigenic bacteria](https://www.annualreviews.org/content/journals/10.1146/annurev-phyto-121823-033153)).
- **Fungal exception worth knowing:** "ambrosia" galls of some Cecidomyiidae have no nutritive tissue at all; a fungal mycelium lines the chamber and feeds the larva — a gall that is *constitutively* a microbial habitat (Bronner 1992, in Shorthouse & Rohfritsch).

### 3.5 Scale and observability
Galls occur on leaves, stems, buds, flowers, fruits and roots, range from leaf blisters to large woody warts, and are usually species-specific in form, so the inducer can often be identified from gall morphology alone; >2,000 insect- and mite-induced gall types are described in North America, with oaks the richest hosts ([Britannica](https://www.britannica.com/science/gall-botany); [Morton Arboretum](https://mortonarb.org/plant-and-protect/tree-plant-care/plant-care-resources/plant-galls/); [Clemson HGIC](https://hgic.clemson.edu/factsheet/galls-outgrowths/)). Cecidology is the established discipline name, and MIDG v0.1 is the proposed minimum-information standard for gall records ([Deans et al. 2024](https://doi.org/10.3897/BDJ.12.e128585)).

---

## 4. Sources

**Ontologies and vocabularies**
- Plant Ontology `PO:0025626 plant gall`, `PO:0025496 multi-tissue plant structure` — http://purl.obolibrary.org/obo/PO_0025626 (created 2024-02-14, `PO_GIT:641`); also in this repo at `data/raw/ontology_terms.tsv`.
- BRENDA Tissue Ontology `BTO:0005833 plant gall`; `BTO:0000303 crown gall` (a *disease*); `BTO:0001190 root nodule`; `BTO:0000493 gall bladder`.
- ENVO `ENVO:01001057`, `ENVO:01001001`, `ENVO:01001032`, `ENVO:02000023 bile material` (synonym "gall"). No gall class in ENVO as of this check (OLS4, 2026-08-18).
- Deans A.R., Nastasi L.F., Davis C. (2024) *GallOnt: An ontology for plant gall phenotypes.* Biodiversity Data Journal 12:e128585. https://doi.org/10.3897/BDJ.12.e128585 — PMC11369494; repo https://github.com/adeans/gallont
- MeSH `D010941 Plant Tumors`; ChEBI `CHEBI:82803 opine`.

**Concept and biology**
- Encyclopaedia Britannica, "gall | botany." https://www.britannica.com/science/gall-botany
- Shorthouse J.D. & Rohfritsch O. (eds.) *Biology of Insect-Induced Galls.* Oxford University Press, 1992 (Bronner's nutritive-cell chapter).
- Ferreira B.G. et al. *Manipulation of host plant cells and tissues by gall-inducing insects…* J Insect Physiol, PMID 26620152.
- Allison S.D. & Schultz J.C. (2005) *Biochemical responses of chestnut oak to a galling cynipid.* J Chem Ecol 31:151–166. https://doi.org/10.1007/s10886-005-0981-5
- *Recent Progress Regarding the Molecular Aspects of Insect Gall Formation.* PMC8430891.
- *Microbiome and plant cell transformation trigger insect gall induction in cassava.* Front Plant Sci 14:1237966 (2023). https://doi.org/10.3389/fpls.2023.1237966
- Anatomy/ultrastructure of *Neuroterus quercusbaccarum* galls, *Insects* 12:850 (2021). https://doi.org/10.3390/insects12100850

**Gall microbiology**
- Kuzmanović N. et al. *Deciphering the key players of the bacterial microbiota associated with aerial crown gall tumors on rhododendron: insights into the gallobiome.* Phytobiomes J. https://doi.org/10.1094/PBIOMES-09-23-0090-R
- Gelvin S.B. (2023) *Agrobacterium tumefaciens: a transformative agent…* PMC10127608.
- Tian B. et al. (2015) *Metagenomic insights into… root-knot nematode… in tomato roots.* Sci Rep 5:17087.
- *Bacterial community structure dynamics in* Meloidogyne incognita*-infected roots.* mSphere 5:e00306-20. PMC7364209.
- *Alteration of rice root endophytic bacterial community by* Meloidogyne graminicola. Ann Microbiol 74 (2024). https://doi.org/10.1186/s13213-024-01789-0
- *Microbiota and functional analyses of nitrogen-fixing bacteria in root-knot nematode parasitism.* Microbiome 11 (2023). https://doi.org/10.1186/s40168-023-01484-3
- Buonaurio R. et al. (2015) *The olive knot disease as a model to study the role of interspecies bacterial communities in plant disease.* Front Plant Sci 6:434.
- *Pseudomonas ST1 and Pantoea Paga strains cohabit in olive knots.* Microorganisms 10:1529 (2022).
- Murray T.D. et al. (2017) *Rathayibacter toxicus… and the potential for livestock poisonings.* Phytopathology 107:804–815.
- *Seed gall nematodes and their association with toxigenic bacteria.* Annu Rev Phytopathol. https://doi.org/10.1146/annurev-phyto-121823-033153

**Taxa in the attestation**
- Evtushenko L.I. et al. (2000) *Leifsonia* gen. nov. … *L. poae* from nematode galls on *Poa annua*. IJSEM 50:371–380. PMID 10826825.
- Evtushenko L.I. et al. (2001) *Agreia bicolorata* gen. nov., sp. nov., from reed grass infected by *Heteroanguina graminophila*. IJSEM 51:2073–2079. PMID 11760949.
- Puławska J. et al. (2012) *Rhizobium nepotum* sp. nov. Syst Appl Microbiol 35:215–220. https://doi.org/10.1016/j.syapm.2012.03.001 (now *Agrobacterium nepotum*).
- Puławska J., Willems A., Sobiczewski P. (2012) *Rhizobium skierniewicense* sp. nov., from tumours on chrysanthemum and cherry plum. IJSEM 62:895–899. https://doi.org/10.1099/ijs.0.032532-0 (now *A. skierniewicense*).
- Demaree J.B. & Smith N.R. (1952) *Nocardia vaccinii* n. sp. causing galls on blueberry plants. Phytopathology 42:249–252. (CABI datasheet 36413, "bud-proliferating gall of blueberry," EPPO code NOCRVA.)
- Yamamoto et al. (2022) *Recurrent acute cholecystitis caused by Actinomyces odontolyticus.* BMC Infect Dis 22:499. https://doi.org/10.1186/s12879-022-07491-3 (cited only for §1.3.)

**Explicitly my inference, not a source's claim:** that the empty kg-microbe mapping cell for this source reflects deletion of a bile/gallbladder mapping; that the *Schaalia odontolytica* strain is mis-filed; that hairy-root disease should sit outside the gall concept boundary; and the summary table's per-taxon "what gall means for it" column, which combines each species description with the isolation-source label.

---

## 5. Synonyms, and what not to conflate

**In real use for this concept:** gall; plant gall; cecidium / cecidia (pl.); zoocecidium (animal-induced), phytocecidium (plant/fungus-induced); plant tumour (MeSH "Plant Tumors"); knot (olive knot); knot gall / cane gall / crown gall / bud gall / seed gall / root knot / erineum / blister gall (all narrower, morphology- or organ-specific); tumour, gall tumour (phytopathology usage).

**Commonly but wrongly treated as the same thing:**
- **Bile / gall / gall bladder** — a different sense of the English word entirely (`ENVO:02000023`, `BTO:0000493`, `UBERON:0001970`). This is the live failure mode in this corpus.
- **Root nodule** — mutualistic and plant-programmed, despite BTO calling nodules "gall-like."
- **Crown gall *disease*** (`BTO:0000303`) — the disease process, not the tissue.
- **Callus / wound periderm** — abiotic or mechanical origin; BTO's gall definition wrongly admits it.
- **Burl / witches' broom** — proliferations of different developmental character (witches' broom is a shoot-proliferation phenotype, usually phytoplasma-induced).
- **The inducer** — *Agrobacterium*, a cynipid wasp, or *Meloidogyne* are organisms; "gall wasp" is not a habitat.
- **Gall as a taxonomic sample of the insect** — 16S surveys of *gall-inducing insects* sample the insect's microbiome, not the gall tissue's ([Hammer et al., Arthropod-Plant Interactions](https://link.springer.com/article/10.1007/s11829-020-09800-6)). Keep the two apart when reading the literature into a habitat definition.

---

## 6. Should it be a term at all?

**Yes — and it already is one.** A gall is a physical, samplable plant structure with a distinct internal microbiota, not a process, quality, disease state or taxon. It passes this repo's part-versus-whole test cleanly (plant tissue, not the plant), so `NOT_APPLICABLE` would be wrong. The correct disposition is `GROUND` to `PO:0025626`, not a term request — the only reason it stands `UNGROUNDED` is a factual error in the note that recorded the decision.

---

## 7. Three things the curator must handle when regrounding

1. **The empty upstream cell is deliberate.** `data/raw/isolation_source_groundings.tsv` has `Gall / gall` with a blank target and justification `family_mismatch_fix` (bacdive, verified 2026-05-02). CLAUDE.md's rule — "BacDive sources with an empty upstream mapping stay UNGROUNDED… do not re-ground by weaker lexical match" — is about not defeating a curator's decision with lexical matching. Grounding here is not lexical: it rests on 11 of 12 attesting taxa being described from plant galls, and on the corpus's own GOLD precedent. Record that reasoning in the `notes` column, since the note is what `tests/test_decisions.py` will check.

2. **`plant_gall.yaml`'s `parent_habitats` will be wrong after the merge.** It currently lists `PO:0009005 root` (inherited from GOLD's `Plants > Roots > Galls` path) alongside `PO:0025496`. The BacDive strains come from crown, stem, bud, leaf and seed galls — `root` is over-narrow and, once merged, would be an over-claim on 16 strains. Drop it, or keep only `PO:0025496`.

3. **One attestation is probably not a plant gall.** *Schaalia odontolytica* (1 strain) is an oral organism with no deposited bile-source strain; it is unexplained under either reading of "gall." That is 1 of 16 assertions and does not change the disposition, but it belongs in the note so the next reader does not re-litigate it.

## Citations

1. https://doi.org/10.1016/j.syapm.2012.03.001
2. https://doi.org/10.1099/ijs.0.032532-0
3. https://pubmed.ncbi.nlm.nih.gov/10826825/
4. https://pubmed.ncbi.nlm.nih.gov/11760949/
5. https://doi.org/10.1186/s12879-022-07491-3
6. https://doi.org/10.3897/BDJ.12.e128585
7. https://www.britannica.com/science/gall-botany
8. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8430891/
9. https://pubmed.ncbi.nlm.nih.gov/26620152/
10. https://doi.org/10.1007/s10886-005-0981-5
11. https://ncbi.nlm.nih.gov/pmc/articles/PMC4568204
12. https://apsjournals.apsnet.org/doi/10.1094/PBIOMES-09-23-0090-R
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC10127608/
14. https://www.nature.com/articles/srep17087
15. https://journals.asm.org/doi/10.1128/msphere.00306-20
16. https://link.springer.com/article/10.1186/s13213-024-01789-0
17. https://link.springer.com/article/10.1186/s40168-023-01484-3
18. https://doi.org/10.3389/fpls.2015.00434
19. https://doi.org/10.3390/microorganisms10081529
20. https://apsjournals.apsnet.org/doi/full/10.1094/PHYTO-02-17-0047-RVW
21. https://www.annualreviews.org/content/journals/10.1146/annurev-phyto-121823-033153
22. https://mortonarb.org/plant-and-protect/tree-plant-care/plant-care-resources/plant-galls/
23. https://hgic.clemson.edu/factsheet/galls-outgrowths/
24. http://purl.obolibrary.org/obo/PO_0025626
25. https://github.com/adeans/gallont
26. https://doi.org/10.3389/fpls.2023.1237966
27. https://doi.org/10.3390/insects12100850
28. https://doi.org/10.1094/PBIOMES-09-23-0090-R
29. https://doi.org/10.1186/s13213-024-01789-0
30. https://doi.org/10.1186/s40168-023-01484-3
31. https://doi.org/10.1146/annurev-phyto-121823-033153
32. https://link.springer.com/article/10.1007/s11829-020-09800-6