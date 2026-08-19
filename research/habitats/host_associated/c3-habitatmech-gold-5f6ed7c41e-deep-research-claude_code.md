---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T04:50:46.356909'
end_time: '2026-08-18T04:58:36.794345'
duration_seconds: 470.44
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: C3
  habitat_identifier: habitatmech:GOLD.5f6ed7c41e
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Mammals > Digestive system > Stomach > C3'
  assertions: '0'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Disjoint-grounding\
    \ review (#62): was UBERON:0002960 'central oculomotor nucleus', a brainstem structure.\
    \ Same as C2 \u2014 the path is Digestive system > Stomach > C3, a camelid stomach\
    \ compartment. Path: Host-associated > Mammals > Digestive system > Stomach >\
    \ C3 (source concept habitatmech:GOLD.5f6ed7c41e)"
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
  num_turns: 31
  total_cost_usd: 2.8418679999999994
  session_id: 211e429a-2f4f-45da-a23b-35add761f977
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 22
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** C3
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.5f6ed7c41e
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Mammals > Digestive system > Stomach > C3
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Disjoint-grounding review (#62): was UBERON:0002960 'central oculomotor nucleus', a brainstem structure. Same as C2 — the path is Digestive system > Stomach > C3, a camelid stomach compartment. Path: Host-associated > Mammals > Digestive system > Stomach > C3 (source concept habitatmech:GOLD.5f6ed7c41e)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **C3** as a microbial habitat, with citations.

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

# C3 (`habitatmech:GOLD.5f6ed7c41e`) — novel-term definition research

> **A digestive tract environment which is determined by the third and terminal compartment (C3) of the camelid stomach, whose long tubiform proximal region sustains near-neutral (pH ≈ 6.5) forestomach fermentation while its short distal region secretes hydrochloric acid (pH ≈ 2).**

If the curator prefers the anatomy-side framing (the parallel that `gut`, `skin` and `lung` follow in this corpus), the genus changes but the differentia does not:

> *A compartment of the stomach which is the third and terminal compartment of the camelid (Tylopoda) multi-compartmented stomach, comprising a tubiform fermentative proximal region and a short acid-secreting distal region.*

One caveat up front, flagged in §6: **GOLD has assigned nothing to this node** — `organism_count`, `study_count`, `biosample_count` and `total_assertions` are all 0 (`data/raw/gold_ecosystem_paths.tsv:2028`), as they are for its siblings C1 and C2. The concept is real and definable; the evidence that anyone has sampled it *as C3* is thin, and the recommended disposition is a UBERON term request rather than an urgent mint.

---

## 1. What the concept denotes

**Reading taken:** C3 is the third and most distal of the three gastric compartments of camelids (Camelidae — llama, alpaca, guanaco, vicuña, dromedary, Bactrian camel). It is the physical lumen and mucosal surface a sample is drawn from when a study samples "compartment 3" of an alpaca, llama or camel stomach.

**Why this reading and not another.** The GOLD path is `Host-associated > Mammals > Digestive system > Stomach > C3`, and its sibling leaves are `C2` (`gold.ecosystem:6700`) and **`C1/Glandular saccules`** (`gold.ecosystem:6699`). The "glandular saccules" qualifier is decisive: glandular saccules in the first compartment are the diagnostic camelid feature, absent from the ruminant rumen, which is lined entirely with stratified squamous epithelium and papillae ([WikiVet, *Camelid Stomach – Anatomy & Physiology*](https://en.wikivet.net/Camelid_Stomach_-_Anatomy_%26_Physiology)). The C1/C2/C3 numbering itself comes from Vallenas, Cummings & Munnell (1971), who deliberately declined ruminant nomenclature for New World camelids ([*J Morphol* 134(4):399–423; PMID 5093421](https://pubmed.ncbi.nlm.nih.gov/5093421/)).

**Boundary — what is inside:**

- The lumen and digesta of the whole tubiform compartment, from the C2–C3 orifice to the pylorus.
- Both functional zones: the proximal glandular, non-acid-secreting, fermentative region and the distal HCl-secreting region. They are one anatomical compartment in the standard New World camelid nomenclature.
- The mucosal surface and its adherent mucus layer (the compartment is lined throughout by mucigenous tubular glands; Cummings, Munnell & Vallenas, *J Morphol* 137:71–109, 1972).

**Boundary — what is a neighbouring concept:**

- **C1** (`gold.ecosystem:6699`) — the voluminous fermentation vat, ~80% of forestomach volume ([Al Jassim 2022, *Animal Frontiers* 12(4):46–52, doi:10.1093/af/vfac049](https://academic.oup.com/af/article/12/4/46/6663954)).
- **C2** (`gold.ecosystem:6700`) — the small reticulum-analogous compartment with retiform glandular divisions.
- **Duodenum** — begins at the pylorus, distal to C3.
- **Abomasum** — a ruminant structure; see §5, it is the single most common wrong conflation.

**Genuine residual ambiguity (report, do not resolve silently).** Old World camelid literature is not unanimous. Some authors of dromedary and Bactrian camel anatomy split what New World camelid workers call C3 into a cranial tubular **C3** and a caudal dilated **C4** ([Wang et al. 2000, *J Morphol* 245(2):161–175, doi:10.1002/1097-4687(200008)245:2<161::AID-JMOR6>3.0.CO;2-B](https://onlinelibrary.wiley.com/doi/abs/10.1002/1097-4687(200008)245:2%3C161::AID-JMOR6%3E3.0.CO;2-B)). Under GOLD's three-leaf path (C1, C2, C3, with no C4), the Vallenas three-compartment convention is clearly the one in force, and the definition should say "third and terminal" to make that explicit.

**Out-of-domain readings that the path excludes:** cervical vertebra 3 (the pre-#62 mis-grounding for C2 went to `UBERON:0001093` 'vertebral bone 2' by exactly this route), complement component C3, C3 photosynthesis / C3 plants, and the C3 convertase. None survives the `Digestive system > Stomach` context.

---

## 2. Genus — the broader kind

**No ontology term names this concept.** Confirmed against the vendored slice (`data/raw/ontology_terms.tsv`) and against live OLS4 queries of UBERON and ENVO for `C3 stomach`, `camelid`, `forestomach`, and `compartment of stomach`. OLS returns **no camelid stomach term of any kind** in UBERON — the only `camelid` hits are `FOODON:00001106` camelid dairy food product and `NCBITaxon:9835` Camelidae.

**Recommended genus, environment side:** `ENVO:01001033` **digestive tract environment** — "An environmental system which has its properties and dynamics determined by a digestive tract." Present in the vendored slice. This is the smallest well-established environmental kind that covers the concept.

**Recommended genus, anatomy side:** `UBERON:0000945` **stomach** — "An expanded region of the vertebrate alimentary tract that serves as a food storage compartment and digestive organ. A stomach is lined, in whole or in part by a glandular epithelium." Present in the slice. UBERON has no `compartment of stomach` grouping class, which is the structural gap behind this whole cluster of records.

**Near-misses and why each fails:**

| Term | Why it is not a match |
|---|---|
| `UBERON:0007358` **abomasum** | Definition asserts "the fourth stomach of ruminating animals". C3 is the *third* compartment of a *non-ruminant* (Tylopoda, pseudoruminant). It is also functionally unlike: the abomasum is glandular acid-secreting throughout, whereas only the terminal ~1/5–1/4 of C3 secretes acid, the rest being fermentative. Grounding here publishes both a wrong ordinal and a wrong clade. |
| `BTO:0000024` **abomasum** | Same failure ("fourth compartment of the ruminant stomach"). |
| `UBERON:0007359` **ruminant forestomach** | "Any of the first three stomachs of a ruminant" — asserts ruminant status, and is a *sum* of three compartments where C3 is one compartment that is only partly forestomach-like. |
| `BTO:0000480` **forestomach** | Same. |
| `UBERON:0007366` **ruminant stomach** | The whole four-compartment organ; wrong clade and wrong granularity. |
| `UBERON:0007362` **omasum** / `BTO:0000348` | Tempting because the proximal tube of C3 is sometimes called functionally omasum-like, but camelids **lack an omasum entirely**, and the analogy is functional only — the structures are anatomically very different. Adopting it would assert a laminated organ that does not exist in this animal. |
| `UBERON:0007365` **rumen**, `UBERON:0007361` **ruminant reticulum** | These are the C1 and C2 analogues, not C3, and again assert ruminant status. |
| `UBERON:0012270` **forestomach–glandular stomach junction** | Names the boundary, not the compartment; its definition is framed on the rodent limiting ridge. |
| `UBERON:0008827` **murine forestomach** | Rodent-specific. |
| `UBERON:0000945` **stomach** | Correct genus, but the whole organ — *broader*, not equal. Appropriate as `parent_habitats`, not as identity. |
| `ENVO:01001033` **digestive tract environment** | Correct genus on the environment side, but broader by several levels. Appropriate as parent. |
| `ENVO:01001002` **animal-associated environment** | Broader still; the top of the branch. |

**A structural note worth recording:** ENVO's `digestive tract environment` has exactly **one** asserted descendant in the current release — `ENVO:2100002` intestine environment — plus the sibling `ENVO:01001187` holothurian digestive tract. An OLS4 search of ENVO for `rumen` returns **zero results**. ENVO has no rumen environment, no stomach environment, and no forestomach environment. This concept is not unusually neglected; the entire foregut-fermenter branch of ENVO is unbuilt. That is context a term-request should carry.

---

## 3. Differentia — what distinguishes it

Ordered by how observable/measurable each property is.

**a. Position in the compartment series.** Third and terminal compartment; receives digesta from C2 and empties through the pylorus into the duodenum (Vallenas, Cummings & Munnell 1971, PMID 5093421).

**b. Gross form.** Long and tubiform, in contrast to the sacculated C1 and the small comb-like C2. Its motility is peristalsis-like rather than the mixing motility of an abomasum ([Al Jassim 2022, doi:10.1093/af/vfac049](https://academic.oup.com/af/article/12/4/46/6663954); [Veterian Key, *Gastrointestinal Surgery in Alpacas and Llamas*](https://veteriankey.com/gastrointestinal-surgery-in-alpacas-and-llamas/)).

**c. Two-zone mucosa — the single strongest differentia.** The compartment is glandular throughout, but only the terminal portion bears acid-secreting gastric glands; the mucosa of the glandular area is reddish brown, the non-glandular area pink ([WikiVet](https://en.wikivet.net/Camelid_Stomach_-_Anatomy_%26_Physiology)). Sources disagree on the exact split — "proximal 80% non-acid-secreting / distal 20% acid-secreting" ([Veterian Key](https://veteriankey.com/gastrointestinal-surgery-in-alpacas-and-llamas/)), "terminal one-fifth contains gastric glands" ([WikiVet](https://en.wikivet.net/Camelid_Stomach_-_Anatomy_%26_Physiology)), "first two-thirds fermentative" (Cebra, *Disorders of the Digestive System*, ch. 40, via [Veterian Key](https://veteriankey.com/disorders-of-the-digestive-system/)). **Recommendation: write the definition as "a short distal acid-secreting region" and do not commit to a fraction**, or cite the range 1/5–1/3. This is a real disagreement in the literature, not a citation gap.

**d. pH gradient within one compartment.** Proximal/fermentative region ≈ pH 6.5; at the caudal flexure the mucosa thickens to 7–10 mm and pH falls to ≈ 2.0 (Cebra, ch. 40, via [Veterian Key](https://veteriankey.com/disorders-of-the-digestive-system/)). An independent clinical measurement of C3 contents in a displaced alpaca C3 gave pH 2.35 ([Wang et al. 2022, *BMC Vet Res* 18:88, doi:10.1186/s12917-022-03181-z](https://bmcvetres.biomedcentral.com/articles/10.1186/s12917-022-03181-z)). For comparison, whole-forestomach pH in dromedaries averages 6.4 on roughage and ~5.3 with grain (Ghali et al. 2019, cited in [Al Jassim 2022](https://academic.oup.com/af/article/12/4/46/6663954)). *This intra-compartment gradient is the property that most sharply distinguishes C3 from every sibling and from the abomasum.*

**e. Continued microbial fermentation in the proximal region.** Vallenas et al. documented fermentative activity in C1, C2 **and the cranial ~two-thirds of C3** — i.e. C3 is not simply a sterile acid chamber. Consistent with this, von Engelhardt, Ali & Wipper measured that during passage through llama C3, **70% of entering short-chain fatty acids, 60% of sodium and 30% of water are absorbed** ([1979, *J Comp Physiol B* 132:337–341, doi:10.1007/BF00799047](https://link.springer.com/article/10.1007/BF00799047)). SCFAs are microbial products; their presence in C3 digesta at that magnitude is the best quantitative evidence that C3 is a fermentation-associated habitat and not merely a downstream acid trap. *Inference marker: the SCFA figure is measured; reading it as evidence of C3 as a microbial habitat is my inference, since the SCFAs could in principle all be carried in from C1/C2.*

**f. Host clade.** Camelidae (Tylopoda) — llama, alpaca, guanaco, vicuña, dromedary, Bactrian camel. Camelids are foregut fermenters but not ruminants sensu stricto; they are conventionally called pseudoruminants.

**g. Characteristic pathology (useful as a corroborating, not defining, property).** Ulcers concentrate at the junction of the fermentative and acid-secreting zones, especially along the lesser curvature ([Veterian Key](https://veteriankey.com/gastrointestinal-surgery-in-alpacas-and-llamas/); Smith et al., "Third compartment ulcers in the llama", [*Vet Clin North Am Food Anim Pract* 10(2):319–330, 1994; PMID 7953964](https://pubmed.ncbi.nlm.nih.gov/7953964/)). This is the only context in which C3 appears at all frequently in the literature.

---

## 4. Sources

**Anatomy and nomenclature**

- Vallenas A, Cummings JF, Munnell JF. *A gross study of the compartmentalized stomach of two new-world camelids, the llama and guanaco.* J Morphol. 1971 Aug;134(4):399–423. [PMID 5093421](https://pubmed.ncbi.nlm.nih.gov/5093421/). — **The foundational C1/C2/C3 naming source.**
- Cummings JF, Munnell JF, Vallenas A. *The mucigenous glandular mucosa in the complex stomach of two new-world camelids, the llama and guanaco.* J Morphol. 1972;137:71–109. (Not indexed in the PubMed query I ran; cite from the primary literature record.)
- Wang JX et al. *Anatomical subdivisions of the stomach of the Bactrian camel (Camelus bactrianus).* J Morphol. 2000;245(2):161–175. [doi:10.1002/1097-4687(200008)245:2<161::AID-JMOR6>3.0.CO;2-B](https://onlinelibrary.wiley.com/doi/abs/10.1002/1097-4687(200008)245:2%3C161::AID-JMOR6%3E3.0.CO;2-B) — the C3/C4 split disagreement.
- Vater A et al. *The topographic and systematic anatomy of the alpaca stomach.* Anat Rec. 2021. [doi:10.1002/ar.24588](https://anatomypubs.onlinelibrary.wiley.com/doi/10.1002/ar.24588) — **paywalled; I could not read past the landing page (HTTP 402).** Cited as the current authoritative alpaca-stomach anatomy reference; a curator quoting it should read it first.
- WikiVet, *Camelid Stomach – Anatomy & Physiology.* https://en.wikivet.net/Camelid_Stomach_-_Anatomy_%26_Physiology — tertiary but explicit on the glandular/gastric-gland zonation and mucosa colour.

**Physiology, pH, absorption**

- von Engelhardt W, Ali KE, Wipper E. *Absorption and secretion in the tubiform forestomach (compartment 3) of the llama.* J Comp Physiol B. 1979;132:337–341. [doi:10.1007/BF00799047](https://link.springer.com/article/10.1007/BF00799047) — 70% SCFA / 60% Na / 30% water absorbed. **Abstract-level access only.**
- Vallenas A, Stevens CE. *Volatile fatty acid concentrations and pH of llama and guanaco forestomach digesta.* Cornell Vet. 1971 Apr;61(2):239–252. [PMID 5577488](https://pubmed.ncbi.nlm.nih.gov/5577488/).
- Rübsamen K, von Engelhardt W. *Bicarbonate secretion and solute absorption in forestomach of the llama.* Am J Physiol. 1978. [PMID 677305](https://pubmed.ncbi.nlm.nih.gov/677305/).
- *Comparative study of forestomach digestion in llamas and sheep.* Reprod Nutr Dev. 1997;37(6):709–725. [PMID 9477438](https://pubmed.ncbi.nlm.nih.gov/9477438/).
- Cebra C. *Disorders of the Digestive System*, ch. 40 (in *Llama and Alpaca Care*), via [Veterian Key](https://veteriankey.com/disorders-of-the-digestive-system/) — pH ≈ 6.5 proximal, ≈ 2.0 at the caudal flexure, mucosa 7–10 mm. **Accessed through a secondary hosting site; a curator citing the pH figures should verify them against the printed chapter.**
- Anderson DE / Jones ML (GI surgery chapter), via [Veterian Key, *Gastrointestinal Surgery in Alpacas and Llamas*](https://veteriankey.com/gastrointestinal-surgery-in-alpacas-and-llamas/) — 80/20 non-acid/acid split, equine-stomach comparison, ulcer localisation.

**Microbiology**

- Al Jassim R. *Foregut microbiology of the Arabian camel (Camelus dromedarius).* Animal Frontiers. 2022;12(4):46–52. [doi:10.1093/af/vfac049](https://academic.oup.com/af/article/12/4/46/6663954) — C3 as the sole HCl-secreting region; forestomach pH 6.4→5.3 with grain. **Explicitly provides no compartment-resolved microbial data.**
- He J et al. *Characterizing the bacterial microbiota in different gastrointestinal tract segments of the Bactrian camel.* Sci Rep. 2018 Jan 12;8:654. [doi:10.1038/s41598-017-18298-7](https://www.nature.com/articles/s41598-017-18298-7), [PMID 29330494](https://pubmed.ncbi.nlm.nih.gov/29330494/) — **the closest thing to a C3 microbiota dataset**: nine sites including one labelled "abomasum" (i.e. the camel's acid-secreting gastric compartment), with unclassified Bifidobacteriaceae reaching ~9% and notably elevated in abomasum/duodenum/jejunum.
- Pei C-X et al. *Diversity and abundance of the bacterial 16S rRNA gene sequences in forestomach of alpacas (Lama pacos) and sheep (Ovis aries).* Anaerobe. 2010 Aug;16(4):426–432. [PMID 20558310](https://pubmed.ncbi.nlm.nih.gov/20558310/) — alpaca forestomach bacterial density 6.89 vs sheep 7.71 log₁₀ copies/g (P<0.01).
- Carroll C et al. *Bacterial communities in the alpaca gastrointestinal tract vary with diet and body site.* Front Microbiol. 2019. [PMC6345687](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6345687/) — sampled C1, duodenum, jejunum, ileum, caecum, large intestine; **C3 was not sampled**.
- *Molecular analysis of methanogenic archaea in the forestomach of the alpaca (Vicugna pacos).* BMC Microbiol. 2012;12:1. [doi:10.1186/1471-2180-12-1](https://link.springer.com/article/10.1186/1471-2180-12-1).

**Clinical**

- Smith BB et al. *Third compartment ulcers in the llama.* Vet Clin North Am Food Anim Pract. 1994 Jul;10(2):319–330. [PMID 7953964](https://pubmed.ncbi.nlm.nih.gov/7953964/).
- *Left displacement of the third gastric compartment in an alpaca: the first case report in China.* BMC Vet Res. 2022;18:88. [doi:10.1186/s12917-022-03181-z](https://bmcvetres.biomedcentral.com/articles/10.1186/s12917-022-03181-z), [PMC8896222](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8896222/) — measured C3 content pH 2.35.

**Vocabularies (checked, negative results are the finding)**

- ENVO via OLS4: `ENVO:01001033` digestive tract environment; `ENVO:01001002` animal-associated environment; `ENVO:2100002` intestine environment. Query `rumen` against ENVO returns **zero** terms. https://www.ebi.ac.uk/ols4
- UBERON via OLS4: no camelid stomach term; `UBERON:0007358` abomasum, `UBERON:0007359` ruminant forestomach, `UBERON:0007366` ruminant stomach, `UBERON:0000945` stomach are the nearest.
- GOLD ecosystem classification nodes `gold.ecosystem:6699/6700/6701`, as captured in `data/raw/gold_ecosystem_paths.tsv:2026-2028`.

**Explicit inference markers.** Three statements above are mine, not a source's: (i) that the C1 sibling's "Glandular saccules" qualifier proves the camelid reading; (ii) that the C3 SCFA absorption figures constitute evidence of C3 as a microbial habitat; (iii) that "short distal acid-secreting region" is the safe phrasing given the 1/5-vs-1/3-vs-1/5 disagreement across texts. Each is reasoning over cited facts, not a cited fact.

---

## 5. Synonyms, and what NOT to conflate

**Names in real use for this concept**

- compartment 3, C-3, C3
- third compartment (of the camelid stomach); third gastric compartment
- tubiform forestomach — used by von Engelhardt et al. 1979 specifically for C3
- "true stomach" of the camelid (informal, veterinary)
- tercer compartimento (Spanish-language South American camelid literature)
- *In Old World camelid papers only:* "abomasum" is used as a label for the camel's acid-secreting gastric compartment — e.g. He et al. 2018 labels it that way. Treat as an **imported synonym with a caveat**, not as an identity claim.

**Commonly but wrongly treated as the same thing**

- **Abomasum** (`UBERON:0007358`) — the most frequent conflation. C3 is not the abomasum: wrong ordinal (third vs fourth), wrong clade (Tylopoda vs Ruminantia), and wrong physiology (C3 is mostly non-acid-secreting and fermentative; the abomasum is not). Keep as `relation: xref` if a link is wanted; do not ground and do not parent.
- **Omasum** (`UBERON:0007362`) — camelids have no omasum. The proximal C3 tube is *functionally* likened to it in some texts; the structures are unrelated.
- **Rumen / reticulum** — the C1 and C2 analogues, not C3.
- **C4** — a fourth compartment recognised only by some Old World camelid anatomists, carved out of what New World camelid nomenclature calls C3.
- **Cervical vertebra 3 (`UBERON:0002413` and kin)** — the string-match trap that produced the pre-#62 error on the sibling C2.
- **Complement component C3; C3 photosynthesis / C3 plants; C3 convertase** — unrelated homonyms.
- **"Rumen" as a generic label for camelid forestomach content** — several camel microbiome papers title their work "camel rumen" while sampling C1. Not this concept.

---

## 6. Should it be a term at all?

**Yes — it denotes a place, and it is a host *part*, not a host organism.** Under this repo's rule that a host's parts ground to the anatomy term while the whole organism does not, C3 sits squarely on the parts side: it is an anatomical compartment of a stomach, in the same class as `gut`, `lung` and `blood`, not in the class of `Mollusca` or `larva`. It is not a process, a quality, a disease state, a taxon, or a sampling artefact. `NOT_APPLICABLE` would be the wrong disposition.

**But two facts should shape how much effort it gets.**

1. **Zero upstream evidence.** GOLD node `gold.ecosystem:6701` has 0 organisms, 0 studies, 0 biosamples, 0 total assertions — as do C1 and C2. All three are unpopulated leaves of GOLD's classification tree. The concept is real; the *attestation* is a vocabulary entry, nothing more. That places it near the bottom of the assertion-volume-ranked backlog that `just report` prints.
2. **No compartment-resolved microbiota study exists for C3 in New World camelids.** I searched specifically and found none: Carroll et al. 2019 sampled C1 and the intestines but not C3; Pei et al. 2010 sampled "forestomach"; the Peruvian altitude study sampled C1; Al Jassim's 2022 review explicitly treats the camel forestomach as one undifferentiated ecosystem. The only compartment-resolved gastric dataset is He et al. 2018 in the Bactrian camel, under the label "abomasum". A definition can be written entirely from anatomy and physiology, which is sound — but the record will have no microbial-community evidence behind it, and the definition should not imply otherwise.

**Recommended disposition.** Keep `CONFIRM_UNGROUNDED`, and file a **UBERON term request** covering all three siblings at once — `compartment 1 of camelid stomach`, `compartment 2 of camelid stomach`, `compartment 3 of camelid stomach`, ideally under a new `compartment of stomach` grouping class, since UBERON currently has no such grouping and models the ruminant compartments as four unrelated organ terms. Requesting the three together is much stronger than requesting C3 alone: the sibling set is what makes the case that this is a systematic gap and not a one-off.

**Suggested `parent_habitats` and `relation` assignments in the interim:**

- `UBERON:0000945` **stomach** — `relation: parent`. Genuinely broader; C3 is part of a stomach. *(Note: strictly this is a part-of, not an is-a, relation; if `parent_habitats` in this corpus is read as is-a, prefer `xref` and leave the record parented only to its GOLD parent.)*
- `UBERON:0007358` **abomasum** — `relation: xref` only. This is the link every source draws and the one every source qualifies; recording it as a parent would publish the exact over-claim that #99 documents.
- `NCBITaxon:9835` **Camelidae** — `relation: xref`, to record the host clade without asserting that a taxon is a place.
- `ENVO:01001033` **digestive tract environment** — `relation: parent` if the record is framed on the environment side.

**Sources:** [Vallenas et al. 1971 (PMID 5093421)](https://pubmed.ncbi.nlm.nih.gov/5093421/) · [Vallenas & Stevens 1971 (PMID 5577488)](https://pubmed.ncbi.nlm.nih.gov/5577488/) · [von Engelhardt et al. 1979 (doi:10.1007/BF00799047)](https://link.springer.com/article/10.1007/BF00799047) · [Rübsamen & von Engelhardt 1978 (PMID 677305)](https://pubmed.ncbi.nlm.nih.gov/677305/) · [Reprod Nutr Dev 1997 (PMID 9477438)](https://pubmed.ncbi.nlm.nih.gov/9477438/) · [Wang et al. 2000 (J Morphol)](https://onlinelibrary.wiley.com/doi/abs/10.1002/1097-4687(200008)245:2%3C161::AID-JMOR6%3E3.0.CO;2-B) · [Vater et al. 2021 (doi:10.1002/ar.24588)](https://anatomypubs.onlinelibrary.wiley.com/doi/10.1002/ar.24588) · [Al Jassim 2022 (doi:10.1093/af/vfac049)](https://academic.oup.com/af/article/12/4/46/6663954) · [He et al. 2018 (doi:10.1038/s41598-017-18298-7)](https://www.nature.com/articles/s41598-017-18298-7) · [Pei et al. 2010 (PMID 20558310)](https://pubmed.ncbi.nlm.nih.gov/20558310/) · [Carroll et al. 2019 (PMC6345687)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6345687/) · [BMC Microbiol 2012 (doi:10.1186/1471-2180-12-1)](https://link.springer.com/article/10.1186/1471-2180-12-1) · [Smith et al. 1994 (PMID 7953964)](https://pubmed.ncbi.nlm.nih.gov/7953964/) · [BMC Vet Res 2022 (doi:10.1186/s12917-022-03181-z)](https://bmcvetres.biomedcentral.com/articles/10.1186/s12917-022-03181-z) · [WikiVet camelid stomach](https://en.wikivet.net/Camelid_Stomach_-_Anatomy_%26_Physiology) · [Veterian Key GI surgery](https://veteriankey.com/gastrointestinal-surgery-in-alpacas-and-llamas/) · [Veterian Key digestive disorders (Cebra ch. 40)](https://veteriankey.com/disorders-of-the-digestive-system/) · [Merck Veterinary Manual llama stomach](https://www.merckvetmanual.com/multimedia/image/stomach-llama) · [EMBL-EBI OLS4](https://www.ebi.ac.uk/ols4) · [Forestomach washing mechanism in llamas (doi:10.1007/s42991-021-00142-1)](https://link.springer.com/article/10.1007/s42991-021-00142-1)

## Citations

1. https://en.wikivet.net/Camelid_Stomach_-_Anatomy_%26_Physiology
2. https://pubmed.ncbi.nlm.nih.gov/5093421/
3. https://academic.oup.com/af/article/12/4/46/6663954
4. https://onlinelibrary.wiley.com/doi/abs/10.1002/1097-4687(200008
5. https://veteriankey.com/gastrointestinal-surgery-in-alpacas-and-llamas/
6. https://veteriankey.com/disorders-of-the-digestive-system/
7. https://bmcvetres.biomedcentral.com/articles/10.1186/s12917-022-03181-z
8. https://link.springer.com/article/10.1007/BF00799047
9. https://pubmed.ncbi.nlm.nih.gov/7953964/
10. https://anatomypubs.onlinelibrary.wiley.com/doi/10.1002/ar.24588
11. https://pubmed.ncbi.nlm.nih.gov/5577488/
12. https://pubmed.ncbi.nlm.nih.gov/677305/
13. https://pubmed.ncbi.nlm.nih.gov/9477438/
14. https://www.nature.com/articles/s41598-017-18298-7
15. https://pubmed.ncbi.nlm.nih.gov/29330494/
16. https://pubmed.ncbi.nlm.nih.gov/20558310/
17. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6345687/
18. https://link.springer.com/article/10.1186/1471-2180-12-1
19. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8896222/
20. https://www.ebi.ac.uk/ols4
21. https://www.merckvetmanual.com/multimedia/image/stomach-llama
22. https://link.springer.com/article/10.1007/s42991-021-00142-1