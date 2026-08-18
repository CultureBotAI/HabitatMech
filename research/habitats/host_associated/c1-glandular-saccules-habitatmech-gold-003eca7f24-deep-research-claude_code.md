---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T04:58:44.249263'
end_time: '2026-08-18T05:04:53.646453'
duration_seconds: 369.4
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: C1/Glandular saccules
  habitat_identifier: habitatmech:GOLD.003eca7f24
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Mammals > Digestive system > Stomach > C1/Glandular
    saccules'
  assertions: '0'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Variant-match\
    \ review (#12): the variant route reaches UBERON:0001092 'vertebral bone 1'. The\
    \ path is Mammals > Digestive system > Stomach, so C1 is the first compartment\
    \ of a camelid stomach \u2014 the same reading already recorded for C2 and C3.\
    \ The slice has no term for it. Path: Host-associated > Mammals > Digestive system\
    \ > Stomach > C1/Glandular saccules (source concept habitatmech:GOLD.003eca7f24)"
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
  web_search_requests: 10
  num_turns: 25
  total_cost_usd: 2.4129134999999997
  session_id: cdde4596-e658-4e21-ae55-651bb95219e5
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 21
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** C1/Glandular saccules
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.003eca7f24
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Mammals > Digestive system > Stomach > C1/Glandular saccules
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Variant-match review (#12): the variant route reaches UBERON:0001092 'vertebral bone 1'. The path is Mammals > Digestive system > Stomach, so C1 is the first compartment of a camelid stomach — the same reading already recorded for C2 and C3. The slice has no term for it. Path: Host-associated > Mammals > Digestive system > Stomach > C1/Glandular saccules (source concept habitatmech:GOLD.003eca7f24)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **C1/Glandular saccules** as a microbial habitat, with citations.

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

# C1/Glandular saccules — definition research

**Concept:** `habitatmech:GOLD.003eca7f24` · HOST_ASSOCIATED · UNGROUNDED
**Source path:** GOLD `Host-associated > Mammals > Digestive system > Stomach > C1/Glandular saccules`

---

## Proposed definition

> A **digestive tract environment** which is determined by the first compartment (C1) of the compartmentalised stomach of a camelid (*Camelidae*), a large non-papillated foregut fermentation chamber whose ventral wall bears muscularly septate glandular saccules lined by mucigenous tubular glands, and whose near-neutral, anaerobic, continuously mixed digesta supports the microbial fermentation of plant fibre.

That sentence carries a lot; a curator who prefers a tighter one can cut the differentia to the two properties nothing else has — *sacculated glandular ventral wall* + *foregut fermentation chamber of a camelid* — and move pH/anaerobiosis to `environmental_parameters`:

> A digestive tract environment which is determined by the first compartment (C1) of the camelid stomach, the principal foregut fermentation chamber, distinguished from the ruminant rumen by a non-papillated mucosa bearing glandular saccules.

---

## 1. What the concept denotes

**The thing sampled.** The lumen and mucosal surface of **compartment 1 (C1)** of the camelid stomach, together with its contained digesta — the site from which "forestomach content" or "C1 fluid" samples are drawn in camelid microbiome studies. Camelids (dromedary, Bactrian camel, llama, guanaco, alpaca, vicuña) are foregut fermenters with a **three**-compartment stomach, not four; the nomenclature C-1 / C-2 / C-3 was fixed by Vallenas, Cummings & Munnell (1971) precisely because the compartments are *functionally* — not anatomically — equivalent to rumen / reticulum / abomasum, and ruminant terminology was judged misleading ([J Morphol 134:399–424, doi:10.1002/jmor.1051340403](https://doi.org/10.1002/jmor.1051340403); [Vater et al. 2021, Anat Rec, doi:10.1002/ar.24588](https://doi.org/10.1002/ar.24588)).

C1 is the voluminous compartment — **~80% of forestomach volume** — divided by a transverse muscular pillar into a cranial and a caudal sac, with rows of **glandular saccules** along the ventral aspect of both, visible as external bumps on the serosal surface ([Al Jassim 2022, *Animal Frontiers* 12(4):46–52, doi:10.1093/af/vfac049](https://doi.org/10.1093/af/vfac049); [Vallenas et al. 1971](https://doi.org/10.1002/jmor.1051340403)).

**Reading the slash.** The label `C1/Glandular saccules` admits two readings and GOLD gives no gloss:

- **(a) The whole compartment, named by its most distinctive feature** — "C1, the sacculated compartment." I take this as the intended reading. The sibling GOLD nodes under `Stomach` are bare `C2` and `C3` (both also UNGROUNDED in this corpus), alongside `Rumen`, `Reticulum`, `Omasum`, `Abomasum`, and `Sacciform`/`Tubiform` — i.e. GOLD's `Stomach` node enumerates compartment names drawn from several foregut-fermenter groups (true ruminants, camelids, and macropods for sacciform/tubiform). Under that pattern `C1/...` is one compartment node, and the qualifier is descriptive.
- **(b) The saccular sub-region of C1 only** — the glandular-sac area proper, distinct from the dorsal non-glandular wall. This is a real, separately sampled place: the Bactrian camel literature treats the **anterior glandular sac area** and **posterior glandular sac area** of C1 as two named, separately biopsied mucosal regions, distinct from the non-glandular dorsal C1 ([Liu et al. 2024, *PLOS ONE* 19(5):e0300316, doi:10.1371/journal.pone.0300316](https://doi.org/10.1371/journal.pone.0300316)).

*My inference, not a source's:* reading (a) is the safer one for the record, because (b) would make this concept narrower than its own siblings C2 and C3 and would require GOLD to have intended a mucosal sub-region where every neighbouring node is a whole compartment. A definition written to (a) still mentions the saccules as the differentia, so it is not wrong under (b), only broader.

**Boundary — what is *not* inside:**

| Neighbouring concept | Why it is outside |
|---|---|
| **C2** (`habitatmech:GOLD....`, sibling record) | Separate, smaller reniform compartment; its cells are lined by a *papillated* mucosa and, unlike C1's saccules, individual cells are not visible from the serosal surface ([Vallenas et al. 1971](https://doi.org/10.1002/jmor.1051340403)) |
| **C3** (sibling record) | Long tubiform compartment; only its aborad ~1/5 bears true gastric glands and is the sole HCl-secreting region, pH 2–3 ([Al Jassim 2022](https://doi.org/10.1093/af/vfac049)) |
| **Rumen** (`UBERON:0007365`, sibling record, NARROW) | A *ruminant* organ. Homology is disputed; C1 is a functional equivalent only |
| **Dorsal non-glandular C1 wall** | Non-keratinised stratified squamous, no glands — the complement of the saccules within the same compartment |
| **Forestomach digesta / "cud"** | GOLD carries `Cud` and `Chyme` as separate sibling nodes; the material is not the compartment |

**Assertion volume is 0.** No GOLD project is recorded against this node in `data/raw/`, so nothing downstream currently depends on it. That is a prioritisation fact, not an argument against the term.

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001033` 'digestive tract environment'** — *"An environmental system which has its properties and dynamics determined by a digestive tract."* This is the pattern class ENVO already uses for exactly this shape of concept, and its one existing sibling-by-example shows the template verbatim: `ENVO:01001187` 'holothurian digestive tract' = *"A digestive tract environment which has its properties and dynamics determined by the digestive tract of an echinoderm from the class Holothuroidea."* A camelid C1 term is the same construction with a different host clade and a compartment restriction.

**Near-misses checked and rejected:**

| Term | Why it fails |
|---|---|
| `ENVO:2100002` 'intestine environment' | The only asserted child of `ENVO:01001033`; anatomically wrong — C1 is stomach, not intestine |
| `ENVO:01001002` 'animal-associated environment' | Correct but far too broad; it is the grandparent, not the genus |
| `ENVO:01001055` 'environment associated with an animal part or small animal' | Broad; loses "digestive tract" entirely |
| `UBERON:0007365` 'rumen' | **The tempting wrong answer.** Definition is explicitly *"The first compartment of the ruminant stomach"* and its mucosa term (`UBERON:8480046`) specifies *keratinised stratified squamous* epithelium with papillae — the opposite of C1's non-papillated, partly glandular lining. Grounding here asserts ruminant identity the sources deny |
| `UBERON:0007359` 'ruminant forestomach' / `UBERON:0007366` 'ruminant stomach' | Same problem, one level up: *"any of the first three stomachs of a ruminant"*. Camelids lack an omasum entirely |
| `UBERON:0000945` 'stomach' | Already the grounding of this record's *parent* (`GOLD.d3869ad37f`, NARROW). Correct but far too broad for a compartment |
| `UBERON:0006924` 'stomach glandular epithelium' | A tissue, not a place a sample of digesta comes from; also narrower than the compartment |
| `UBERON:0000325` 'gastric gland' / `UBERON:0008859` 'cardiac gastric gland' | The camelid saccular glands are mucigenous tubular glands, not acid-secreting gastric glands — the acid-secreting region is distal C3 ([Al Jassim 2022](https://doi.org/10.1093/af/vfac049)) |
| `UBERON:0001854` 'saccule of membranous labyrinth', `UBERON:0003976` 'saccule duct' | Every UBERON hit on the string "saccule" is inner-ear or lung. A lexical route lands here; it is a false friend, same class of error as the `UBERON:0001092` 'vertebral bone 1' variant match already recorded on this concept |

**No term exists for the concept in UBERON, ENVO, FOODON, BTO or PO.** OLS returns `NCBITaxon:9835` 'Camelidae' as the only hit for "camelid" across UBERON. The existing `CONFIRM_UNGROUNDED` decision is correct.

---

## 3. Differentia — what distinguishes C1 from its siblings

All observable/measurable, all sourced:

**Structural**
- **Glandular saccules on the ventral wall**, divided by muscular septae, present in both the cranial and caudal sac; internally *and* externally visible ([Vallenas et al. 1971](https://doi.org/10.1002/jmor.1051340403); [Hatt et al. 2021, *Mamm Biol* 101:941–948, doi:10.1007/s42991-021-00142-1](https://doi.org/10.1007/s42991-021-00142-1)). In the camel these are formalised as the **cranioventral/anterior** and **caudodorsal/posterior** glandular sac areas ([Liu et al. 2024](https://doi.org/10.1371/journal.pone.0300316)).
- **No papillae anywhere in C1** — the single sharpest contrast with the rumen. Dorsal wall is non-keratinised stratified squamous; the ventral saccules are lined by mucigenous columnar epithelium over deep tubular glands ([Cummings, Munnell & Vallenas 1972, *J Morphol* 137:71–109, doi:10.1002/jmor.1051370106](https://doi.org/10.1002/jmor.1051370106); [Al Jassim 2022](https://doi.org/10.1093/af/vfac049)).
- **~80% of forestomach volume**; partitioned into cranial and caudal sacs by a transverse muscular pillar ([Al Jassim 2022](https://doi.org/10.1093/af/vfac049); [Vallenas et al. 1971](https://doi.org/10.1002/jmor.1051340403)).

**Physicochemical**
- **Near-neutral and anaerobic.** Reported C1 pH is **6.5–7.5** in veterinary surgical reference, **6–7** in alpaca nutrition sources — versus pH 2–3 in distal C3. The primary measurement is Vallenas & Stevens (1971), *Volatile fatty acid concentrations and pH of llama and guanaco forestomach digesta*, Cornell Vet 61:239–252 ([PMID 5577488](https://pubmed.ncbi.nlm.nih.gov/5577488/)). *I could not read that paper's full text; the numeric ranges above come from secondary veterinary sources and should be re-checked against the primary before being written into `environmental_parameters`.*
- **Saccules as an absorptive and buffering surface.** They absorb SCFA, water and electrolytes in place of the papillae camelids lack, and were reported to secrete bicarbonate directly into the C1 lumen — Eckerlin & Stevens (1973), Cornell Vet 63:436–445 ([PMID 4782561](https://pubmed.ncbi.nlm.nih.gov/4782561/)). **Flag:** the bicarbonate finding is contested in secondary sources on the grounds that it was not experimentally repeated; do not state it as settled in a definition. SCFA absorption from C1/C2 is independently confirmed in camels by washed-compartment experiments ([Rübsamen & von Engelhardt–lineage work, *J Comp Physiol B*, doi:10.1007/s00360-007-0161-8](https://doi.org/10.1007/s00360-007-0161-8)).
- **Contents do not stratify into a gas cap** the way rumen contents do; C1 digesta are homogeneous and fibrous, dorsal contents drier and the ventral/saccular contents semifluid to watery, with muscular ridge contraction squeezing nutrient-rich fluid into the relaxing saccules. Camelid motility cycles are near-continuous and more frequent than ruminal contractions. Hatt et al. additionally show density-based sorting: C1 contents are **washed free of ingested sand/silica**, which accumulates downstream in C3 ([Hatt et al. 2021](https://doi.org/10.1007/s42991-021-00142-1)).

**Biotic (what makes it a habitat)**
- Dense anaerobic community of bacteria, methanogenic archaea, ciliate protists and anaerobic fungi fermenting plant fibre to acetate, propionate and butyrate ([Al Jassim 2022](https://doi.org/10.1093/af/vfac049)).
- **Compositionally distinct from the rumen of a true ruminant on the same diet.** Alpaca vs sheep forestomach: 27 vs 21 phylotypes from 60 clones each, alpaca dominated by *Eubacterium* sp. F1 (25% of clones) vs sheep by *Prevotella ruminicola* (40%); alpaca bacterial density significantly *lower* (6.89 vs 7.71 log₁₀ copies/g wet weight, P < 0.01) ([Pei et al. 2010, *Anaerobe* 16:426–432, doi:10.1016/j.anaerobe.2010.06.004](https://doi.org/10.1016/j.anaerobe.2010.06.004)).
- Bactrian camel glandular sac areas are enriched in **Bacteroidetes (59.5%)** and **Fibrobacteria (3.5%)** relative to other ruminants, alongside significantly elevated IgA⁺ plasma cells and acidic mucus secretion versus the fundic and pyloric regions ([Liu et al. 2024](https://doi.org/10.1371/journal.pone.0300316)).
- Alpaca C1 methanogens: 947 sequences → 51 species-level OTUs, **88.3% *Methanobrevibacter***, with *M. millerae*-like clones dominant — an ordering unlike other host species ([St-Pierre & Wright 2012, *BMC Microbiol* 12:1, doi:10.1186/1471-2180-12-1](https://doi.org/10.1186/1471-2180-12-1)).
- C1 community differs by diet and by body site along the alpaca GI tract ([Carroll et al. 2019, *Front Microbiol* 9:3334, doi:10.3389/fmicb.2018.03334](https://doi.org/10.3389/fmicb.2018.03334)); and by altitude/region in Peruvian alpacas, where "first compartment (C1)" is sampled as ~500 g of contents strained to 20 mL and surveyed by 16S/18S metabarcoding ([Flores-Huarco et al. 2026, *Microorganisms* 14(1):138, doi:10.3390/microorganisms14010138](https://doi.org/10.3390/microorganisms14010138)).
- Bactrian camel GI-tract-wide survey confirming compartment-level community structure: [He et al. 2018, *Sci Rep* 8:654, doi:10.1038/s41598-017-18298-7](https://doi.org/10.1038/s41598-017-18298-7).

---

## 4. Synonyms and what NOT to conflate

**Names in real use for the concept**
- C1 · C-1 · compartment 1 · first compartment of the stomach · first forestomach compartment
- glandular saccules (for the ventral sub-region) · glandular sac area · glandular sac region
- anterior/cranioventral glandular sac area; posterior/caudodorsal glandular sac area (camel-specific sub-regions, [Liu et al. 2024](https://doi.org/10.1371/journal.pone.0300316))
- *loose/deprecated:* "camelid rumen", "pseudo-rumen", "rumen-equivalent" — used in camel microbiota papers but expressly discouraged by the anatomy literature

**Do NOT conflate with**
- **Rumen (`UBERON:0007365`)** — functional analogue, not the same organ; different epithelium, different compartment count, different community ([Pei et al. 2010](https://doi.org/10.1016/j.anaerobe.2010.06.004))
- **Reticulum (`UBERON:0007361`) / C2** — separate sibling node, papillated
- **Omasum (`UBERON:0007362`)** — camelids have none
- **Abomasum (`UBERON:0007358`) / C3** — glandular and acidic; a sibling node grounded EXACT in this corpus
- **`UBERON:0001092` 'vertebral bone 1'** — the recorded variant-match false positive; "C1" as cervical vertebra 1
- **Inner-ear `saccule`** (`UBERON:0001854`) and **lung saccule** (`UBERON:0000116`) — lexical false friends
- **Sacciform / tubiform forestomach** — sibling GOLD nodes; those are the **macropod** (kangaroo) forestomach regions, a different host clade, not camelid C1/C3 (*this identification is my inference from the standard macropod anatomical nomenclature, offered as a caution for whoever curates those two sibling records — I did not verify GOLD's intent*)
- **Cud / chyme** — the material, carried as separate GOLD nodes

---

## 5. Should it be a term at all?

**Yes.** This is a bounded anatomical place that microbiologists sample and from which sequence data is generated — not a process, quality, disease, taxon, or sampling artefact. Under this repo's rule that *a host's parts ground to the anatomy term while the whole host organism does not*, C1 is unambiguously a **part**: it would ground routinely if a term existed. None does.

**Recommended disposition:** keep `CONFIRM_UNGROUNDED` and promote to a **term-request candidate**, in two places:

1. **UBERON** — `camelid stomach compartment 1` (with `camelid stomach compartment 2/3` and `glandular saccule of camelid stomach` as the obvious companions, resolving the sibling C2 and C3 records at the same time). UBERON already carries the ruminant compartment series (`UBERON:0007365/0007361/0007362/0007358`) under `ruminant stomach`; the camelid series is the parallel gap. Vallenas et al. 1971 and Cummings et al. 1972 are adequate definitional sources.
2. **ENVO** — `camelid C1 compartment environment` as a child of `ENVO:01001033`, following the `ENVO:01001187` 'holothurian digestive tract' template. ENVO's only child of that class is `intestine environment`; there is no stomach or rumen environment class at all, so this gap is wider than one term and worth saying so in the request.

**Meanwhile, on the record:** attach `NCBITaxon:9835` 'Camelidae' as `relation: xref` (the host clade is not broader than the habitat), and consider `UBERON:0007366` 'ruminant stomach' as an xref **only** if the note is explicit that it is a functional analogue — I'd leave it off, since the existing parent link to the `Stomach` record (`GOLD.d3869ad37f` → `UBERON:0000945`) already carries the correct broader claim without asserting ruminant-hood.

---

## 6. Two things a curator should not take from this report unchecked

- The **pH range 6.5–7.5** reaches me through veterinary secondary sources, not the primary measurement (Vallenas & Stevens 1971, Cornell Vet 61:239–252, no DOI, [PMID 5577488](https://pubmed.ncbi.nlm.nih.gov/5577488/)). Verify before writing it into `environmental_parameters`.
- The **bicarbonate secretion** function of the saccules ([Eckerlin & Stevens 1973](https://pubmed.ncbi.nlm.nih.gov/4782561/)) is reported as unreplicated. It is a good line in a comment, a bad line in a definition. Note also the recurring misspelling "Eckerlein" in downstream reference lists — the correct first author is **Eckerlin**.

---

## Sources

- [Vallenas A, Cummings JF, Munnell JF (1971). A gross study of the compartmentalized stomach of two new-world camelids, the llama and guanaco. *J Morphol* 134:399–424. doi:10.1002/jmor.1051340403](https://doi.org/10.1002/jmor.1051340403)
- [Cummings JF, Munnell JF, Vallenas A (1972). The mucigenous glandular mucosa in the complex stomach of two new-world camelids, the llama and guanaco. *J Morphol* 137:71–109. doi:10.1002/jmor.1051370106](https://doi.org/10.1002/jmor.1051370106)
- [Vallenas A, Stevens CE (1971). Volatile fatty acid concentrations and pH of llama and guanaco forestomach digesta. *Cornell Vet* 61:239–252. PMID 5577488](https://pubmed.ncbi.nlm.nih.gov/5577488/)
- [Eckerlin RH, Stevens CE (1973). Bicarbonate secretion by the glandular saccules of the llama stomach. *Cornell Vet* 63:436–445. PMID 4782561](https://pubmed.ncbi.nlm.nih.gov/4782561/)
- [Vater A et al. (2021). The topographic and systematic anatomy of the alpaca stomach. *Anat Rec*. doi:10.1002/ar.24588](https://doi.org/10.1002/ar.24588)
- [Al Jassim R (2022). Foregut microbiology of the Arabian camel (*Camelus dromedarius*). *Animal Frontiers* 12(4):46–52. doi:10.1093/af/vfac049](https://doi.org/10.1093/af/vfac049)
- [Liu et al. (2024). Distribution characteristics of gastric mucosal colonizing microorganisms in different glandular regions of Bactrian camels… *PLOS ONE* 19(5):e0300316, 30 May 2024. doi:10.1371/journal.pone.0300316](https://doi.org/10.1371/journal.pone.0300316)
- [Hatt J-M et al. (2021). Preliminary evidence for a forestomach washing mechanism in llamas. *Mamm Biol* 101:941–948. doi:10.1007/s42991-021-00142-1](https://doi.org/10.1007/s42991-021-00142-1)
- [Pei C-X et al. (2010). Diversity and abundance of the bacterial 16S rRNA gene sequences in forestomach of alpacas and sheep. *Anaerobe* 16:426–432. doi:10.1016/j.anaerobe.2010.06.004](https://doi.org/10.1016/j.anaerobe.2010.06.004)
- [St-Pierre B, Wright A-DG (2012). Molecular analysis of methanogenic archaea in the forestomach of the alpaca. *BMC Microbiol* 12:1. doi:10.1186/1471-2180-12-1](https://doi.org/10.1186/1471-2180-12-1)
- [Carroll C et al. (2019). Bacterial communities in the alpaca gastrointestinal tract vary with diet and body site. *Front Microbiol* 9:3334. doi:10.3389/fmicb.2018.03334](https://doi.org/10.3389/fmicb.2018.03334)
- [Flores-Huarco NH et al. (2026). Effects of diet and altitude on the microbiota of the first compartment of the stomach in Peruvian alpacas. *Microorganisms* 14(1):138. doi:10.3390/microorganisms14010138](https://doi.org/10.3390/microorganisms14010138)
- [He J et al. (2018). Characterizing the bacterial microbiota in different gastrointestinal tract segments of the Bactrian camel. *Sci Rep* 8:654. doi:10.1038/s41598-017-18298-7](https://doi.org/10.1038/s41598-017-18298-7)
- [Absorption of short-chain fatty acids, sodium and water from the forestomach of camels. *J Comp Physiol B* (2007). doi:10.1007/s00360-007-0161-8](https://doi.org/10.1007/s00360-007-0161-8)
- [WikiVet — Camelid Stomach: Anatomy & Physiology](https://en.wikivet.net/Camelid_Stomach_-_Anatomy_%26_Physiology)
- [UMN CVM Large Animal Anatomy — Abdomen 2: Bovine and Camelid](https://pressbooks.umn.edu/largeanimalanatomy/chapter/abdomen-2/)
- [Veterian Key — Gastrointestinal Surgery in Alpacas and Llamas](https://veteriankey.com/gastrointestinal-surgery-in-alpacas-and-llamas/) (source of the C1 pH 6.5–7.5 figure)
- Ontology terms checked via OLS4: [ENVO:01001033 digestive tract environment](https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001033), [ENVO:01001187 holothurian digestive tract](https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001187), [UBERON:0007365 rumen](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0007365), [UBERON:0007359 ruminant forestomach](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0007359)

## Citations

1. https://doi.org/10.1002/jmor.1051340403
2. https://doi.org/10.1002/ar.24588
3. https://doi.org/10.1093/af/vfac049
4. https://doi.org/10.1371/journal.pone.0300316
5. https://doi.org/10.1007/s42991-021-00142-1
6. https://doi.org/10.1002/jmor.1051370106
7. https://pubmed.ncbi.nlm.nih.gov/5577488/
8. https://pubmed.ncbi.nlm.nih.gov/4782561/
9. https://doi.org/10.1007/s00360-007-0161-8
10. https://doi.org/10.1016/j.anaerobe.2010.06.004
11. https://doi.org/10.1186/1471-2180-12-1
12. https://doi.org/10.3389/fmicb.2018.03334
13. https://doi.org/10.3390/microorganisms14010138
14. https://doi.org/10.1038/s41598-017-18298-7
15. https://en.wikivet.net/Camelid_Stomach_-_Anatomy_%26_Physiology
16. https://pressbooks.umn.edu/largeanimalanatomy/chapter/abdomen-2/
17. https://veteriankey.com/gastrointestinal-surgery-in-alpacas-and-llamas/
18. https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001033
19. https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001187
20. https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0007365
21. https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0007359