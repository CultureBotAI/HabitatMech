---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T04:50:56.756216'
end_time: '2026-08-18T04:59:01.802464'
duration_seconds: 485.05
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: C2
  habitat_identifier: habitatmech:GOLD.e89f860f72
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Mammals > Digestive system > Stomach > C2'
  assertions: '0'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Disjoint-grounding
    review (#62): was UBERON:0001093 ''vertebral bone 2''. The path is Host-associated
    > Mammals > Digestive system > Stomach > C2, so C2 is the second compartment of
    a camelid stomach, not a neck vertebra. The slice has no term for it. Path: Host-associated
    > Mammals > Digestive system > Stomach > C2 (source concept habitatmech:GOLD.e89f860f72)'
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
  num_turns: 38
  total_cost_usd: 3.3804069999999995
  session_id: caebea3c-b025-4d54-b798-54c79562dbc2
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 19
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** C2
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.e89f860f72
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Mammals > Digestive system > Stomach > C2
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Disjoint-grounding review (#62): was UBERON:0001093 'vertebral bone 2'. The path is Host-associated > Mammals > Digestive system > Stomach > C2, so C2 is the second compartment of a camelid stomach, not a neck vertebra. The slice has no term for it. Path: Host-associated > Mammals > Digestive system > Stomach > C2 (source concept habitatmech:GOLD.e89f860f72)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **C2** as a microbial habitat, with citations.

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

I'll research this now.

# Proposed definition

> A **zone of stomach** (UBERON:0009870) which is the second and smallest compartment of the three-compartmented camelid (Tylopoda) stomach, lying to the right of and partially continuous with C1, lined by a chambered, glandular-sacculated non-papillated mucosa, and holding moist, near-neutral, anaerobically fermenting digesta that it sorts by density between C1 and the tubular C3.

If a curator prefers the environmental-system framing used elsewhere in ENVO, the same content reads:

> A **digestive tract environment** (ENVO:01001033) which is determined by the second compartment (C2) of the camelid stomach — the small, glandular-sacculated chamber between C1 and C3 in which foregut fermentation continues and digesta are sorted by density.

Both are one sentence. I recommend the first: the corpus already grounds this concept's GOLD siblings to anatomical entities (`Rumen` → `BTO:0001194`, `Reticulum` → `BTO:0000347`), so an anatomical genus keeps C2 commensurable with them.

---

## 1. What the concept denotes

**C2 is the second compartment of the compound stomach of a camelid** — dromedary, Bactrian camel, llama, alpaca, guanaco, vicuña. The thing a sample is taken from is the **digesta (fluid + fine particulate) held in the C2 lumen**, or a scraping of its mucosa: an anaerobic, near-neutral, actively fermenting foregut compartment.

**Why this reading and not another.** The GOLD path is `Host-associated > Mammals > Digestive system > Stomach > C2`, and the decisive evidence is the sibling set in the source table itself (`data/raw/gold_ecosystem_paths.tsv`, GOLD ecosystem ids 6699–6701, a consecutive block):

| GOLD id | Specific ecosystem |
|---|---|
| 6699 | `C1/Glandular saccules` |
| 6700 | `C2` |
| 6701 | `C3` |

"Glandular saccules" is camelid-specific terminology — the glandular sacs of C1 are a diagnostic camelid feature with no ruminant counterpart ([Eckerlin & Stevens 1973, PMID 4782561](https://pubmed.ncbi.nlm.nih.gov/4782561/); [Hatt et al. 2021](https://doi.org/10.1007/s42991-021-00142-1)). GOLD *separately* carries `Rumen` (6389/4111), `Reticulum` (6395), `Omasum` (6396) and `Abomasum` (6391) under the same parent, so in the source vocabulary C1/C2/C3 are **not** the ruminant compartments under another name. It also separately carries `Sacciform` (6697) and `Tubiform` (6698), which are the macropod forestomach regions — so the C-series is not those either.

**Boundaries.**
- *Inside the concept:* the C2 lumen and its contents, its chambered glandular-sacculated wall, the C1↔C2 orifice region as far as C2's own mucosa extends.
- *Neighbouring concepts, not inside:* C1 including its glandular saccule rows (GOLD 6699), the tubular C3 and its distal acid-secreting portion (GOLD 6701), the ruminant reticulum (GOLD 6395 / `BTO:0000347`), and the whole camelid forestomach (C1+C2 together).
- *A real fuzziness worth recording:* in the dromedary, C2 is **not completely separated** from C1 — there is a wide opening between them and the two are described as partially continuous, with contents intermixing freely ([Ibrahim 2026, *Vet. Sci.* 13:630](https://doi.org/10.3390/vetsci13070630)). A "C1 vs C2" sample distinction is therefore weaker than a "rumen vs abomasum" one, and any definition should not imply a sealed compartment.

**Ambiguity of the bare label.** "C2" in isolation has at least four readings; only one survives the path.

| Reading | Verdict |
|---|---|
| Second compartment of the camelid stomach | **Adopted** — fits the path and the sibling block |
| Second cervical vertebra / axis (`UBERON:0001093` "vertebral bone 2") | Excluded by the path. This is the exact error #62 corrected on this record, and the parallel one on C1 (`UBERON:0001092`) |
| "C2" in the minority four-compartment dromedary nomenclature (C1–C4, splitting C3) ([Ali 2025, *Open Vet. J.* 15:4569](https://doi.org/10.5455/OVJ.2025.v15.i9.63)) | **Does not change the referent** — C2 is the second compartment under either scheme. Worth a note, not a separate concept |
| Complement component C2; a two-carbon compound | Excluded by the path |

---

## 2. Genus — the broader kind

**The smallest well-established kind is "a compartment/division of a multi-compartmented mammalian stomach."** No ontology term in the vendored slice, or in UBERON or ENVO more broadly, names *that* kind without also asserting Ruminantia.

**Best available genus terms (both in the vendored slice):**

- `UBERON:0009870` **zone of stomach** — "A division of the stomach. The stomach can be divided based on mucosal histology (glandular epithelium and gastric glands) and the relative position and type of gastric gland." Taxon-neutral, broad enough, asserts nothing false. *This is my recommendation as genus.* (That the definition's worked examples are human gastric zones rather than forestomach compartments is my observation; the definition text itself imposes no such restriction — flagging this as inference, not something UBERON states.)
- `ENVO:01001033` **digestive tract environment** — "An environmental system which has its properties and dynamics determined by a digestive tract." Correct if the definition is written in ENVO's environmental-system idiom.

**Near-misses, and why each fails:**

| Candidate | Why it is not a match |
|---|---|
| `UBERON:0007361` **ruminant reticulum** (in slice) | Asserts ruminant-hood. Camelids are Tylopoda, not Ruminantia, and the compound forestomachs of the two groups arose by **parallel, non-homologous evolution** ([UMN Large Animal Anatomy](https://pressbooks.umn.edu/largeanimalanatomy/chapter/abdomen-2/)). C2 is a *functional* equivalent of the reticulum ([Hatt et al. 2021](https://doi.org/10.1007/s42991-021-00142-1); [Al Jassim 2022](https://doi.org/10.1093/af/vfac049)), which is a similarity claim, not an identity claim. Grounding here would also collide with GOLD's own separate `Reticulum` term, already grounded on the record `data/habitats/host_associated/reticulum.yaml` |
| `BTO:0000347` **reticulum** (in slice) | Same problem, stated even more explicitly: "The second compartment of the stomach of a **ruminant**…" |
| `UBERON:0007359` **ruminant forestomach** (in slice) | Wrong taxon, and covers three compartments — broader *and* false, so unusable even as a parent |
| `UBERON:0007366` **ruminant stomach** | Definition asserts four compartments; camelids have three and no omasum ([Al Jassim 2022](https://doi.org/10.1093/af/vfac049)) |
| `UBERON:0008827` **murine forestomach** | Rodent-specific |
| `UBERON:0011953` **stomach glandular region** (in slice) | C2's mucosa is largely glandular, but this term names a *tissue region of any stomach*; it drops the compartment identity, and would equally cover parts of C1 and C3 |
| `UBERON:0000945` **stomach** (in slice) | True but far too broad — a grandparent, not the genus |
| `ENVO` rumen / forestomach / stomach environment | **None exist.** An OLS search of ENVO for "rumen" returns zero hits, and `ENVO:01001033` has exactly one specific child, `ENVO:01001187` holothurian digestive tract |
| Any camelid-specific anatomy term | **None found.** OLS searches of UBERON for "forestomach" and "reticulum" return no term mentioning camelid, Tylopoda, *Camelus*, or llama |

**Consequence for curation:** confirming UNGROUNDED was right. The natural upstream fix is a UBERON term request for a taxon-neutral *stomach compartment* class plus camelid C1/C2/C3 children — the same request would resolve C1 and C3, which sit in exactly this position.

---

## 3. Differentia — what distinguishes C2 from its siblings

Ordered by how observable each property is.

**Position and size**
- Smallest of the three gastric compartments; on the right side of the abdominal cavity, partially continuous with C1 ([Ibrahim 2026](https://doi.org/10.3390/vetsci13070630)).
- C1 + C2 together hold 85–90% of total stomach volume and act as the fermentation vat ([Veterian Key, *Gastrointestinal Surgery in Alpacas and Llamas*](https://veteriankey.com/gastrointestinal-surgery-in-alpacas-and-llamas/), drawing on *Medicine and Surgery of Camelids*). C1 alone is ~80% of forestomach volume ([Al Jassim 2022](https://doi.org/10.1093/af/vfac049)); a figure of ~6% (1–2 L) for C2 circulates in camelid-association and practitioner material — **treat as low-confidence**, I did not find it in primary literature.

**Mucosa and wall — the sharpest anatomical differentia**
- Mucosa forms **chambered / comb-like / honeycomb-patterned zones** supported by prominent longitudinal muscular bands that branch into smaller interconnected bands, producing numerous chambers of variable size ([Ibrahim 2026](https://doi.org/10.3390/vetsci13070630); reticulated structure visible in llama CT, [Hatt et al. 2021](https://doi.org/10.1007/s42991-021-00142-1)).
- Wall is **glandular and sacculated, without papillae** — unlike the papillated rumen of cattle. All three camelid compartments carry glandular epithelium ("columnar surface epithelium and deep tubular glands"); non-glandular portions of C1 and C2 are non-keratinised stratified squamous without papillae ([Al Jassim 2022](https://doi.org/10.1093/af/vfac049); [Veterian Key](https://veteriankey.com/gastrointestinal-surgery-in-alpacas-and-llamas/)).
- Abundant **neutral and acidic mucins** ([Ibrahim 2026](https://doi.org/10.3390/vetsci13070630)).
- Glandular saccules of C1/C2 **secrete bicarbonate directly into the lumen**, buffering the compartment ([Eckerlin & Stevens 1973, *Cornell Vet.* 63(3):436–445, PMID 4782561](https://pubmed.ncbi.nlm.nih.gov/4782561/)).

**Digesta handling — the functional differentia vs C1 and C3**
- C2 is a **sorting compartment operating by density**: dense (typically small) particles pass C2→C3, while lighter (typically large) particles are propelled backwards C2→C1. C2 contents are "particularly moist" ([Hatt et al. 2021](https://doi.org/10.1007/s42991-021-00142-1)).
- The **ventricular (oesophageal) groove** runs from the oesophageal entrance toward C2 and has a *single* lip, versus two in the bovine reticular groove; the tubular C2→C3 passage continues the groove ([UMN Large Animal Anatomy](https://pressbooks.umn.edu/largeanimalanatomy/chapter/abdomen-2/); [Vater et al. 2021, *Anat. Rec.*](https://doi.org/10.1002/ar.24588)).
- Inter-compartment openings are **smaller** than the rumen–reticulum opening in similarly-sized ruminants ([Hatt et al. 2021](https://doi.org/10.1007/s42991-021-00142-1)).
- Motility: contraction cycles begin at the ventricular groove followed by a single rapid C2 contraction; the camelid forestomach contracts 2–3× as often as a ruminant's and in reverse order, emptying and refilling the saccules each cycle ([Vallenas & Stevens 1971a, *Am. J. Physiol.* 220:275–282, PMID 5538663](https://pubmed.ncbi.nlm.nih.gov/5538663/); [Veterian Key](https://veteriankey.com/gastrointestinal-surgery-in-alpacas-and-llamas/)).

**Physicochemistry**
- Fermentative activity with VFA production occurs in **C1 and C2** (and the first two-thirds of C3, caecum and proximal colon): Vallenas & Stevens 1971b, "Volatile fatty acid concentrations and pH of llama and guanaco forestomach digesta," *Cornell Vet.* 61:239–252 — **this is the one paper that reports pH and VFA for C2 specifically**, and I could not obtain its text, so treat the compartment-resolved numbers as unretrieved rather than absent.
- C1 pH values are well documented and near-neutral: 7.28 ± 0.06 (range 6.5–7.7) in llamas ([Zaki et al. 2023, *Trop. Anim. Health Prod.* 55:403](https://doi.org/10.1007/s11250-023-03820-z)); 6.65–6.81 in alpacas across diets ([Carroll et al. 2018, *Front. Microbiol.* 9:3334](https://doi.org/10.3389/fmicb.2018.03334)). **Extending these to C2 is my inference**, supported by the free intermixing of C1 and C2 contents and by C2's own bicarbonate-secreting saccules — but it is an inference, and the definition should say "near-neutral" rather than quote a number.
- Contrast with C3: the distal fifth of C3 is the only HCl-secreting region, at pH ~1.4–2.0 ([Al Jassim 2022](https://doi.org/10.1093/af/vfac049); [Veterian Key](https://veteriankey.com/gastrointestinal-surgery-in-alpacas-and-llamas/)). This is the cleanest physicochemical boundary in the C-series and the reason C2 and C3 are different habitats.
- Long particulate retention — up to ~60 h in camelids vs ~40 h in sheep ([Veterian Key](https://veteriankey.com/gastrointestinal-surgery-in-alpacas-and-llamas/)).

**Microbial community — the evidence that C2 is sampled as a habitat**
- [He et al. 2018, *Sci. Rep.* 8:654](https://doi.org/10.1038/s41598-017-18298-7) profiled nine GI sites in 11 Bactrian camels, **sampling the second forestomach compartment separately** from the first: 1,567 OTUs, Chao1 1,156.33, Shannon 8.19 — essentially matching the first compartment (1,560 OTUs, Chao1 1,144.21, Shannon 8.00) and far exceeding the jejunum (950 OTUs, Shannon 5.82). *Caveat, and it matters:* the paper labels the camel compartments with ruminant terms ("rumen", "reticulum", "abomasum"); reading its "reticulum" as C2 is my inference from the paper's own statement that camels have a three-chambered forestomach lacking an omasum.
- Camelid foregut communities are Bacteroidetes/Firmicutes-dominated, with methanogens, ciliate protozoa and anaerobic fungi ([Al Jassim 2022](https://doi.org/10.1093/af/vfac049); [St-Pierre & Wright 2012, *BMC Microbiol.* 12:1](https://doi.org/10.1186/1471-2180-12-1), where *Methanobrevibacter* was 88.3% of alpaca forestomach archaeal clones).
- **A real gap:** most camelid microbiome work samples C1 only — [Carroll et al. 2018](https://doi.org/10.3389/fmicb.2018.03334) sampled six sites but only C1 among the stomach compartments, and the Peruvian high-altitude study likewise used C1. GOLD records **0 assertions** for C2. So C2-specific community composition is thinly characterised, and the definition should rest on anatomy and physicochemistry, not on a claimed distinctive microbiota.

---

## 4. Synonyms, and what not to conflate

**Names in real use for this concept**
- compartment 2 / C2 / C-2 (the standard camelid convention, after Vallenas, Cummings & Munnell 1971, *J. Morphol.* 134:399–424)
- second compartment of the camelid (or camel / llama / alpaca) stomach
- second stomach chamber of the dromedary (*J. Camel Pract. Res.* usage)
- "reticulum" **as applied to camelids** — widespread in the camel microbiome literature ([He et al. 2018](https://doi.org/10.1038/s41598-017-18298-7)) and defensible as a *functional* label; record it as a related/broad synonym with a taxonomic-disambiguation caveat, never as an exact one

**Do not conflate with**
- **Ruminant reticulum** (`UBERON:0007361`, `BTO:0000347`; GOLD `Reticulum`, gold.ecosystem:6395) — different taxon, convergent not homologous, and a distinct GOLD concept
- **Second cervical vertebra / axis** (`UBERON:0001093` "vertebral bone 2") — the lexical trap this record already fell into
- **C1 / glandular saccules** (GOLD 6699) and **C3** (GOLD 6701)
- **Omasum** (`UBERON:0007362`) — camelids have none; the proximal "gastric tube" of C3 is sometimes called functionally omasum-like, which is a claim about C3, not C2
- **Forestomach** (GOLD 6370; `UBERON:0007359` ruminant forestomach) — C1+C2 collectively, i.e. broader
- **Complement component C2**; **two-carbon (C2) compounds** such as acetate — no relation despite acetate being a principal fermentation product here

---

## 5. Should this be a term at all?

**Yes.** C2 is a place — a bounded anatomical compartment with a lumen that is routinely sampled and sequenced ([He et al. 2018](https://doi.org/10.1038/s41598-017-18298-7)). It is not a process, quality, disease state, taxon, or sampling artefact, so none of the corpus's `NOT_APPLICABLE` dispositions apply. `CONFIRM_UNGROUNDED` is the correct standing disposition and the existing parent (`habitatmech:GOLD.d3869ad37f`, the GOLD Mammals `Stomach` record) is genuinely broader, so it belongs in `parent_habitats`.

Three curation notes:

1. **Low priority, real concept.** Upstream assertion volume is 0. This is a GOLD vocabulary entry with no biosamples behind it yet — worth defining correctly, not worth a term request ahead of high-volume backlog items.
2. **Define C1, C2 and C3 together.** All three fail for the identical reason (no taxon-neutral stomach-compartment term exists), all three have been mis-grounded to cervical vertebrae by lexical matching, and a single UBERON term request covering the camelid compartment series would resolve all three. Splitting them risks three inconsistent genera.
3. **Do not attach `UBERON:0007361` or `BTO:0000347` as a parent** to "keep the link." `parent_habitats` means *broader*, and ruminant reticulum is neither broader than nor identical to camelid C2 — it is a convergent sibling in a different taxon. If the reticulum link is worth preserving at all, `relation: xref` is the honest form, exactly as with the anthropogenic-contamination case in #99.

---

## 6. Sources

**Primary literature**
- Ibrahim, Z.H. (2026). Morphological, Histo-Morphometric and Histochemical Studies on Compartment 2 of Dromedary Camel (*Camelus dromedarius*) Stomach. *Veterinary Sciences* 13(7):630. https://doi.org/10.3390/vetsci13070630 — *the single most on-target source; MDPI blocked full-text retrieval, so detail here comes from the abstract and indexed summaries*
- Hatt, J.-M., Codron, D., Richter, H., Kircher, P.R., Hummel, J., Clauss, M. (2021). Preliminary evidence for a forestomach washing mechanism in llamas (*Lama glama*). *Mammalian Biology* 101(6):941–948. https://doi.org/10.1007/s42991-021-00142-1
- Vater, R., et al. (2021). The topographic and systematic anatomy of the alpaca stomach. *The Anatomical Record*. https://doi.org/10.1002/ar.24588 — *paywalled; detail via indexed summaries*
- Al Jassim, R. (2022). Foregut microbiology of the Arabian camel (*Camelus dromedarius*). *Animal Frontiers* 12(4):46–51. https://doi.org/10.1093/af/vfac049
- He, J., Yi, L., Hai, L., Ming, L., Gao, W., Ji, R. (2018). Characterizing the bacterial microbiota in different gastrointestinal tract segments of the Bactrian camel. *Scientific Reports* 8:654. https://doi.org/10.1038/s41598-017-18298-7
- Carroll, C., et al. (2018). Bacterial Communities in the Alpaca Gastrointestinal Tract Vary With Diet and Body Site. *Frontiers in Microbiology* 9:3334. https://doi.org/10.3389/fmicb.2018.03334
- St-Pierre, B., Wright, A.-D.G. (2012). Molecular analysis of methanogenic archaea in the forestomach of the alpaca (*Vicugna pacos*). *BMC Microbiology* 12:1. https://doi.org/10.1186/1471-2180-12-1
- Zaki, M.G., et al. (2023). Determination of hematobiochemical and fore stomach fluid constituents of llama (*Lama glama*) living in Egypt. *Tropical Animal Health and Production* 55(6):403. https://doi.org/10.1007/s11250-023-03820-z
- Eckerlin, R.H., Stevens, C.E. (1973). Bicarbonate secretion by the glandular saccules of the llama stomach. *Cornell Veterinarian* 63(3):436–445. PMID 4782561. https://pubmed.ncbi.nlm.nih.gov/4782561/
- Vallenas, A.P., Stevens, C.E. (1971a). Motility of the llama and guanaco stomach. *American Journal of Physiology* 220(1):275–282. https://doi.org/10.1152/ajplegacy.1971.220.1.275
- Vallenas, A.P., Stevens, C.E. (1971b). Volatile fatty acid concentrations and pH of llama and guanaco forestomach digesta. *Cornell Veterinarian* 61:239–252 — **not retrieved; the compartment-resolved pH/VFA source to obtain before quoting numbers for C2**
- Vallenas, A.P., Cummings, J.F., Munnell, J.F. (1971). A gross study of the compartmentalized stomach of two New World camelids, the llama and guanaco. *Journal of Morphology* 134:399–424 — *origin of the C1/C2/C3 nomenclature; not retrieved*
- Ali, A.M. (2025). Histological study on the prenatal development of compartment 1 of the stomach of the camel (*Camelus dromedarius*). *Open Veterinary Journal* 15(9):4569–4577. https://doi.org/10.5455/OVJ.2025.v15.i9.63 — *cited only for the C1–C4 nomenclature variant*

**Reference works and vocabularies**
- Ontology Lookup Service (OLS4), EMBL-EBI — UBERON and ENVO queries run 2026-08-18: https://www.ebi.ac.uk/ols4/
- ENVO: `ENVO:01001033` digestive tract environment; `ENVO:01001002` animal-associated environment; `ENVO:01001187` holothurian digestive tract (its only specific child)
- UBERON: `UBERON:0009870`, `UBERON:0000945`, `UBERON:0011953`, `UBERON:0007359`, `UBERON:0007361`, `UBERON:0007366`, `UBERON:0008827`, `UBERON:0001093`
- JGI GOLD Ecosystem Classification: https://gold.jgi.doe.gov/ecosystem_classification and https://gold.jgi.doe.gov/ecosystemtree
- UMN CVM Large Animal Anatomy, *Abdomen 2: Bovine and Camelid*: https://pressbooks.umn.edu/largeanimalanatomy/chapter/abdomen-2/
- WikiVet, *Camelid Stomach – Anatomy & Physiology*: https://en.wikivet.net/Camelid_Stomach_-_Anatomy_%26_Physiology
- Veterian Key, *Gastrointestinal Surgery in Alpacas and Llamas* (derived from *Medicine and Surgery of Camelids*, Wiley): https://veteriankey.com/gastrointestinal-surgery-in-alpacas-and-llamas/
- APHA, *South American Camelids* veterinary information sheet: https://assets.publishing.service.gov.uk/media/678792c73f1182a1e258a235/APHA_Veterinary_Information_Sheet_-_South_American_Camelids.pdf

**Repo-internal evidence** (not external citations, but load-bearing for §1)
- `data/raw/gold_ecosystem_paths.tsv` lines for gold.ecosystem:6699/6700/6701 and 6389–6397
- `data/habitats/host_associated/reticulum.yaml` (GOLD `Reticulum` → `BTO:0000347`), `c1_glandular_saccules.yaml`, `c3.yaml`
- `curation/decisions.tsv` lines 1584 and 1674 (the C2 and C1 disjoint-grounding corrections)

**Explicitly flagged as inference, not sourced**
- That `UBERON:0009870` "zone of stomach" is intended to cover forestomach compartments and not only gastric zones
- That He et al. (2018)'s "reticulum" sample is C2
- That C1's measured pH range (6.5–7.7) applies to C2

**Known gaps a curator should not paper over:** no compartment-resolved pH or VFA numbers for C2 were retrieved (Vallenas & Stevens 1971b is the paper to get); no study I found profiles C2 microbiota under an explicitly camelid nomenclature; and the ~6% volume figure for C2 rests on practitioner material, not primary literature.

## Citations

1. https://pubmed.ncbi.nlm.nih.gov/4782561/
2. https://doi.org/10.1007/s42991-021-00142-1
3. https://doi.org/10.3390/vetsci13070630
4. https://doi.org/10.5455/OVJ.2025.v15.i9.63
5. https://pressbooks.umn.edu/largeanimalanatomy/chapter/abdomen-2/
6. https://doi.org/10.1093/af/vfac049
7. https://veteriankey.com/gastrointestinal-surgery-in-alpacas-and-llamas/
8. https://doi.org/10.1002/ar.24588
9. https://pubmed.ncbi.nlm.nih.gov/5538663/
10. https://doi.org/10.1007/s11250-023-03820-z
11. https://doi.org/10.3389/fmicb.2018.03334
12. https://doi.org/10.1038/s41598-017-18298-7
13. https://doi.org/10.1186/1471-2180-12-1
14. https://doi.org/10.1152/ajplegacy.1971.220.1.275
15. https://www.ebi.ac.uk/ols4/
16. https://gold.jgi.doe.gov/ecosystem_classification
17. https://gold.jgi.doe.gov/ecosystemtree
18. https://en.wikivet.net/Camelid_Stomach_-_Anatomy_%26_Physiology
19. https://assets.publishing.service.gov.uk/media/678792c73f1182a1e258a235/APHA_Veterinary_Information_Sheet_-_South_American_Camelids.pdf