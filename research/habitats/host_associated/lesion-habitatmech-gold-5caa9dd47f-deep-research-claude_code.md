---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T21:08:48.548964'
end_time: '2026-08-17T21:17:38.542420'
duration_seconds: 529.99
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Lesion
  habitat_identifier: habitatmech:GOLD.5caa9dd47f
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Mammals: Human > Integumentary system > Skin
    > Lesion'
  assertions: '81'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Stale-sweep
    review (#12): NCIT:C3824 ''Lesion'' matches the label now, but it is a pathological
    finding rather than a place, and the habitat here is the skin the lesion is on.
    The sweep''s answer was right and its stated reason has stopped being true, so
    it is re-recorded with the reason that holds. Path: Host-associated > Mammals:
    Human > Integumentary system > Skin > Lesion (source concept habitatmech:GOLD.5caa9dd47f)'
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
  web_search_requests: 5
  num_turns: 28
  total_cost_usd: 2.4285805
  session_id: 5b386a7d-4924-4896-9de7-d1dfe59c08b1
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 21
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Lesion
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.5caa9dd47f
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Mammals: Human > Integumentary system > Skin > Lesion
- **Upstream assertion volume:** 81
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Stale-sweep review (#12): NCIT:C3824 'Lesion' matches the label now, but it is a pathological finding rather than a place, and the habitat here is the skin the lesion is on. The sweep's answer was right and its stated reason has stopped being true, so it is re-recorded with the reason that holds. Path: Host-associated > Mammals: Human > Integumentary system > Skin > Lesion (source concept habitatmech:GOLD.5caa9dd47f)

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

# Lesion — HabitatMech novel-term research

**Concept:** `habitatmech:GOLD.5caa9dd47f` · label *Lesion* · HOST_ASSOCIATED · UNGROUNDED
**Source path:** `Host-associated > Mammals: Human > Integumentary system > Skin > Lesion` (`gold.ecosystem:6236`, 81 ORGANISM assertions)

---

## Proposed definition

> A skin environment which is determined by a zone of skin whose structure has been locally altered by disease or injury, and which is thereby demarcated from the adjacent unaffected skin of the same host.

Genus: `ENVO:2100003` *skin environment*. Differentia: local pathological or traumatic structural alteration, plus demarcation from surrounding intact skin.

**Read section 6 before adopting this.** The definition is writable and defensible, but there is a real case that the right disposition is to keep `CONFIRM_UNGROUNDED` and request nothing, and there is a live internal inconsistency with the sibling records that has to be settled either way.

---

## 1. What the concept denotes

**The physical thing sampled.** A delimited patch of a human's skin whose normal structure has been locally changed by disease or injury, together with the material occupying or covering that patch — exudate, crust, scale, pus, necrotic debris, or the exposed living epidermis/dermis where the stratum corneum is gone. This is the locus a swab or biopsy is taken from, and the microbiological literature routinely samples it as a unit, paired against non-lesional skin on the same subject as an internal control ([Alekseyenko et al. 2013, *Microbiome* 1:31, doi:10.1186/2049-2618-1-31](https://doi.org/10.1186/2049-2618-1-31); [Kong et al. 2012, *Genome Res* 22:850, doi:10.1101/gr.131029.111](https://doi.org/10.1101/gr.131029.111)).

**The boundary — what is inside.** The affected zone of skin and its surface material. Whether the "lesion" extends to the immediately surrounding periwound/perilesional skin is genuinely contested in the wound literature: the standard Levine swab samples the centre, and bacteria are also present in quantity at wound edges ([wound-swab technique and spatial-sampling limitations, medRxiv 2024.04.18.24305961](https://www.medrxiv.org/content/10.1101/2024.04.18.24305961)). Treat the perilesional margin as inside the concept only if a curator wants to, and say so; sources do not settle it.

**What is a neighbouring concept, per GOLD's own hierarchy.** This is the strongest single piece of evidence about what GOLD means, and it is in `data/raw/gold_ecosystem_paths.tsv`. Under `... > Integumentary system > Skin`, GOLD's children are: **Lesion** (81), Skin tissue (54), **Abscess** (17), Perineum (13), Umbilicus (5), Axilla/Armpit (4), **Ulcer** (4), Epidermis (2). Abscess and Ulcer are *siblings* of Lesion, not children of it. So in this data, "Lesion" does not mean "any skin lesion"; it means **skin lesion not otherwise specified** — the residual bin left after the named lesion types were pulled out. Anything a submitter called an abscess or an ulcer went elsewhere.

**Ambiguity in the bare label.** Three readings, and the path disambiguates decisively:

1. *Skin lesion* — the reading the path forces (`... > Skin > Lesion`). Adopt this.
2. *Plant lesion* — a leaf or stem lesion. The corpus already has a separate concept for this at `habitatmech:BACDIVE.31392c69b9`, decided `CONFIRM_UNGROUNDED`.
3. *Neurological lesion* — a focal brain/nerve injury, the dominant sense in neuroscience. Not in play here and not a microbial habitat.

A fourth, near-identical concept exists in the corpus and must be decided the same way: `habitatmech:GOLD.be021eb56c`, `Host-associated > Fish > Integumentary system > Skin > Lesion` (23 assertions). Whatever is done here should be done there. If the genus below is adopted, one new term can serve both records, with host specificity carried by each record's own parent chain rather than by the term.

---

## 2. Genus — the broader kind

**Smallest well-established kind: a skin environment. `ENVO:2100003` *skin environment* — "An environment determined by an area or zone of skin tissue."** ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:2100003)) A lesion is a zone of skin, so the genus fits without strain, and ENVO's term is defined off `UBERON:0000014` *zone of skin* — the same construction the definition above needs.

The corpus already carries `ENVO:2100003` as a record (`data/habitats/other/skin_environment.yaml`, EXACT, REVIEWED — note it is filed under OTHER, not HOST_ASSOCIATED, which is a separate small inconsistency).

### Near-misses in ENVO, and why each fails

I enumerated the full descendant set of `ENVO:2100000` *anatomical entity environment* via the OLS4 API. It has **thirteen** terms: mushroom environment, environment determined by a metazoan secretion, digestive tract environment, fungi-associated environment, environment associated with a fungal tissue, bone element environment, axilla skin environment, mouth environment, intestine environment, skin environment, integumental system environment, face skin environment, feather environment. **None is pathological.** ENVO has no wound environment, no lesion environment, no diseased-tissue environment anywhere in this branch.

| Term | Why it is not a match |
|---|---|
| `ENVO:2100003` *skin environment* | **Broader.** Grounding here merges lesional and intact skin into one record, erasing exactly the distinction GOLD's leaf is drawing — and the distinction the microbiome literature reports as significant (§3). This is the genus, not the match. |
| `ENVO:08000001` *axilla skin environment*, `ENVO:2100005` *face skin environment* | **Siblings on the wrong axis.** ENVO's only existing subdivision of skin environment is by body region. Nothing subdivides it by pathological state. Informative: the axis this concept needs does not exist in ENVO yet. |
| `ENVO:2100004` *integumental system environment* | Broader still — the parent of skin environment. |
| `ENVO:01001000` *environmental system determined by an organism* | Far too broad; two levels up. |
| `UBERON:0000014` *zone of skin*, `UBERON:0002097` *skin of body* | The unqualified anatomical site. `UBERON:0002097` is already used in the corpus for BacDive's skin bin (`habitatmech:BACDIVE.c94bf36c57`). UBERON has no lesion class. |
| `BTO:0003114` *wound fluid* | **Narrower and a different entity type** — the exudate, a portion of material, not the site; and it asserts a wound, which most skin lesions are not. |
| `BTO:0003257` *granulation tissue* | **Narrower and over-asserting** — a specific tissue of the proliferative healing phase, present in some lesions at some times. |
| `NCIT:C3824` *Lesion* — "A localized pathological or traumatic structural change, damage, deformity, or discontinuity of tissue, organ, or body part." | **Not in HabitatMech's five vocabularies** (ENVO/UBERON/FOODON/BTO/PO), so it cannot be a `GROUND` target regardless. Also organ-agnostic: it covers bone, brain and breast lesions equally, so it is broader than the skin concept, not equal to it. The existing note's characterisation is right. |
| `HP:0011355` *Localized skin lesion* | A **phenotypic abnormality** — a quality of an organism, in HabitatMech's terms the same category as `PATO:0001429` *acidic*, which the corpus already treats as `NOT_APPLICABLE`-with-xref. |
| `SNOMED:52988006` *Lesion* | See below — informative but not adoptable. |
| `OGMS:0000045` *disorder* — "A material entity which is clinically abnormal and part of an extended organism." | **Not a habitat vocabulary**, but the most useful upper-level evidence available: BFO-aligned OBO modelling treats a disorder as a *material entity*, i.e. a thing, not a process or quality. This is the single best support for the "a lesion is a place" reading. |

### The SNOMED evidence, which cuts both ways

SNOMED CT models `52988006 |Lesion|` with the semantic tag **(morphologic abnormality)**, which places it in the **Body structure** hierarchy — a descendant of `49755003 |Morphologically abnormal structure|` — *not* in Clinical finding ([SNOMED CT Editorial Guide, "Structure of Domain Coverage"](https://docs.snomed.org/snomed-ct-specifications/snomed-ct-editorial-guide/readme/snomed-ct-introduction/structure-of-domain-coverage)). So the most widely deployed clinical terminology in the world says a lesion **is a structure**, contra the "it is a finding, not a place" framing in the current curation note.

But SNOMED also says it is not a *self-sufficient* place: `52988006` is a value for the `116676008 |Associated morphology|` attribute, and a disorder concept is built by pairing that morphology with a `363698007 |Finding site|`. A lesion needs a site supplied separately to denote anywhere. In the September 2022 release, SNOMED remodelled many Lesion-morphology concepts that had been Clinical findings into Disorders ([SNOMED CT September 2022 International Edition release notes](https://confluence.ihtsdotools.org/display/RMT/SNOMED+CT+September+2022+International+Edition+-+SNOMED+International+Release+notes)).

**This is the crux for the definition.** "Lesion" alone is a morphology, not a place. `Skin` + `Lesion` — which is exactly what the GOLD path supplies — *is* a place. Hence the proposed definition builds the site into the genus (`skin environment`) rather than trying to define "lesion" simpliciter.

The same decomposition appears in the GSC's own standard: MIxS puts the anatomical site in **`host_body_site`** (values from UBERON or FMA, e.g. `gill [UBERON:0002535]`) and the pathological state in a separate slot, **`host_disease_stat`** (`MIXS:0000031`, values from the Disease Ontology) ([MIxS host-associated extension, genomicsstandardsconsortium.github.io/mixs/0016002](https://genomicsstandardsconsortium.github.io/mixs/0016002/)). Under MIxS, a human skin lesion sample is annotated as *skin* + *disease state*, not as a distinct body site. **That is a standards-body precedent directly against minting a site term for this.** It is also the strongest argument in section 6.

---

## 3. Differentia — what distinguishes it from intact skin

All of these are observable or measurable, and each is a candidate differentia clause. They are also the material for `environmental_parameters` if a record is written.

**Surface pH — the acid mantle is lost.** Intact skin surface pH is on average below 5 ([Lambers et al. 2006, *Int J Cosmet Sci* 28:359, doi:10.1111/j.1467-2494.2006.00344.x](https://doi.org/10.1111/j.1467-2494.2006.00344.x)). Where a lesion breaches the stratum corneum, the wound bed and edge show markedly higher pH than adjacent intact skin, reflecting exposure of subepidermal tissue at ~7.4. The classic cited range for chronic wounds is 7.15–8.9 ([Gethin, "The significance of surface pH in chronic wounds", *Wounds UK*](https://wounds-uk.com/wp-content/uploads/2023/02/content_9150.pdf)); a recent prospective multicentre cohort narrows this to an observed 5.1–8.6 clustering near 7.0, with alkaline values associated with chronicity and microbial burden ([*Sci Rep* 2026, doi:10.1038/s41598-026-45000-7](https://www.nature.com/articles/s41598-026-45000-7)). Note: the classic range covers *open* lesions; a scaly plaque or a closed comedo is not covered by it, and quoting 7.15–8.9 as a property of "lesion" generally would over-claim.

**Substrate chemistry — plasma-derived rather than sebaceous.** Intact skin surface offers sebum lipids and a desiccated, protein-poor stratum corneum. A breached lesion presents serum exudate: plasma proteins, host adhesion substrates, and haem iron. Concretely, fibronectin and fibrinogen exposed in the disrupted barrier mediate the enhanced adherence of *S. aureus* to atopic skin ([Cho et al. 2001, *J Allergy Clin Immunol* 108:269, doi:10.1067/mai.2001.117455](https://doi.org/10.1067/mai.2001.117455)).

**Community composition differs from adjacent unaffected skin of the same individual.** This is the strongest empirical case that a lesion is a distinguishable habitat rather than a label on skin. In 51 matched triplets (psoriatic lesion / unaffected contralateral skin of the same patient / matched healthy control), PCoA separated lesion samples from both unaffected and control along the first axis, with intragroup UniFrac β-diversity increasing control → unaffected → lesion ([Alekseyenko et al. 2013, doi:10.1186/2049-2618-1-31](https://doi.org/10.1186/2049-2618-1-31)). Note the same study's caveat: unaffected skin of psoriasis patients is itself shifted away from healthy control skin, so the lesion/non-lesion boundary is a gradient, not a step.

**Bloom of a single taxon under disease activity.** In children with atopic dermatitis, the proportion of *Staphylococcus* — particularly *S. aureus* — was greater during flares than at baseline or post-treatment and correlated with worsened severity; community structure at sites of disease predilection was dramatically different from controls ([Kong et al. 2012, doi:10.1101/gr.131029.111](https://doi.org/10.1101/gr.131029.111)). Strain-level resolution shows AD-associated *S. aureus* and *S. epidermidis* lineages ([Byrd et al. 2017, *Sci Transl Med* 9:eaal4651, doi:10.1126/scitranslmed.aal4651](https://doi.org/10.1126/scitranslmed.aal4651)). Metagenomics adds a functional signature and a "dry and alkaline phenotype primed for pathogen growth" ([Chng et al. 2016, *Nat Microbiol* 1:16106, doi:10.1038/nmicrobiol.2016.106](https://doi.org/10.1038/nmicrobiol.2016.106)).

**The lesion community is not confined to the lesion.** In cutaneous leishmaniasis, dysbiosis was transmissible to normal skin distant from the infection site and to co-housed naive mice ([Gimblet et al. 2017, *Cell Host Microbe* 22:13, doi:10.1016/j.chom.2017.06.006](https://doi.org/10.1016/j.chom.2017.06.006)). **This weakens the "spatially bounded habitat" claim** and is worth recording honestly rather than omitting.

**General reference for the intact-skin baseline the differentia is drawn against:** [Grice & Segre 2011, *Nat Rev Microbiol* 9:244, doi:10.1038/nrmicro2537](https://doi.org/10.1038/nrmicro2537); [Byrd, Belkaid & Segre 2018, *Nat Rev Microbiol* 16:143, doi:10.1038/nrmicro.2017.157](https://doi.org/10.1038/nrmicro.2017.157).

### The heterogeneity problem — my inference, stated as such

*This paragraph is my analysis, not a claim any cited source makes.* The differentia above are drawn from **open, exudative** lesions (wounds, ulcers, eczematous lesions). NCIT's definition of *Lesion*, which the current note already invokes, spans macules, papules, plaques, vesicles, pustules, nodules, comedones and ulcers. Their microenvironments are not one environment: a closed comedo is a lipid-rich, low-oxygen follicular compartment dominated by *Cutibacterium acnes* strain populations ([Fitz-Gibbon et al. 2013, *J Invest Dermatol* 133:2152, doi:10.1038/jid.2013.21](https://doi.org/10.1038/jid.2013.21)); a neuropathic diabetic foot ulcer is an open, protein-rich, near-neutral bed with biofilm-forming *S. aureus* and Corynebacteria ([Kalan et al. 2019, *Cell Host Microbe* 25:641, doi:10.1016/j.chom.2019.03.006](https://doi.org/10.1016/j.chom.2019.03.006)) and prevalent fungal communities ([Kalan et al. 2016, *mBio* 7:e01058-16, doi:10.1128/mBio.01058-16](https://doi.org/10.1128/mbio.01058-16)); a psoriatic plaque is a hyperkeratotic, closed, scaling surface. **The only property they all share is "structurally abnormal".** Any differentia stronger than that will be false of some member of the class. That constraint is what the one-sentence definition above is built to respect — and it is why the definition is thin.

---

## 4. Sources

Primary literature on the habitat and its communities:

- Kong HH et al. Temporal shifts in the skin microbiome associated with disease flares and treatment in children with atopic dermatitis. *Genome Research* 22:850–859, 2012-02-06. PMID 22310478. [doi:10.1101/gr.131029.111](https://doi.org/10.1101/gr.131029.111)
- Alekseyenko AV et al. Community differentiation of the cutaneous microbiota in psoriasis. *Microbiome* 1:31, 2013-12-23. PMID 24451201. [doi:10.1186/2049-2618-1-31](https://doi.org/10.1186/2049-2618-1-31)
- Chng KR et al. Whole metagenome profiling reveals skin microbiome-dependent susceptibility to atopic dermatitis flare. *Nature Microbiology* 1:16106, 2016-07-11. PMID 27562258. [doi:10.1038/nmicrobiol.2016.106](https://doi.org/10.1038/nmicrobiol.2016.106)
- Byrd AL et al. *Staphylococcus aureus* and *Staphylococcus epidermidis* strain diversity underlying pediatric atopic dermatitis. *Science Translational Medicine* 9:eaal4651, 2017-07-01. PMID 28679656. [doi:10.1126/scitranslmed.aal4651](https://doi.org/10.1126/scitranslmed.aal4651)
- Kalan LR et al. Strain- and species-level variation in the microbiome of diabetic wounds is associated with clinical outcomes and therapeutic efficacy. *Cell Host & Microbe* 25:641–655, 2019-04-18. PMID 31006638. [doi:10.1016/j.chom.2019.03.006](https://doi.org/10.1016/j.chom.2019.03.006)
- Kalan L et al. Redefining the chronic-wound microbiome: fungal communities are prevalent, dynamic, and associated with delayed healing. *mBio* 7:e01058-16, 2016-09-06. PMID 27601572. [doi:10.1128/mBio.01058-16](https://doi.org/10.1128/mbio.01058-16)
- Loesche M et al. Temporal stability in chronic wound microbiota is associated with poor healing. *J Invest Dermatol* 137:237–244, 2016-08-24. PMID 27566400. [doi:10.1016/j.jid.2016.08.009](https://doi.org/10.1016/j.jid.2016.08.009)
- Gimblet C et al. Cutaneous leishmaniasis induces a transmissible dysbiotic skin microbiota that promotes skin inflammation. *Cell Host & Microbe* 22:13–24, 2017-06-29. PMID 28669672. [doi:10.1016/j.chom.2017.06.006](https://doi.org/10.1016/j.chom.2017.06.006)
- Fitz-Gibbon S et al. *Propionibacterium acnes* strain populations in the human skin microbiome associated with acne. *J Invest Dermatol* 133:2152–2160, 2013-01-21. PMID 23337890. [doi:10.1038/jid.2013.21](https://doi.org/10.1038/jid.2013.21)
- Cho SH et al. Fibronectin and fibrinogen contribute to the enhanced binding of *Staphylococcus aureus* to atopic skin. *J Allergy Clin Immunol* 108:269–274, 2001-08-01. PMID 11496245. [doi:10.1067/mai.2001.117455](https://doi.org/10.1067/mai.2001.117455)
- Verbanic S et al. Improved single-swab sample preparation for recovering bacterial and phage DNA from human skin and wound microbiomes. *BMC Microbiology*, 2019. [PMC6729076](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6729076/) — methods context: skin and wound samples are low-biomass, and only one-quarter of wound samples yielded sufficient DNA by traditional preparation.

Reviews and baselines:

- Grice EA & Segre JA. The skin microbiome. *Nature Reviews Microbiology* 9:244–253, 2011-04-01. PMID 21407241. [doi:10.1038/nrmicro2537](https://doi.org/10.1038/nrmicro2537)
- Byrd AL, Belkaid Y & Segre JA. The human skin microbiome. *Nature Reviews Microbiology* 16:143–155, 2018-01-15. PMID 29332945. [doi:10.1038/nrmicro.2017.157](https://doi.org/10.1038/nrmicro.2017.157)
- Lambers H et al. Natural skin surface pH is on average below 5, which is beneficial for its resident flora. *Int J Cosmet Sci* 28:359–370, 2006-10-01. PMID 18489300. [doi:10.1111/j.1467-2494.2006.00344.x](https://doi.org/10.1111/j.1467-2494.2006.00344.x)
- Gethin G. The significance of surface pH in chronic wounds. *Wounds UK*. [PDF](https://wounds-uk.com/wp-content/uploads/2023/02/content_9150.pdf)
- pH profiling reveals progressive wound acidification during healing and higher pH in chronic non-healing wounds: a prospective, multicenter cohort study. *Scientific Reports*, 2026. [doi:10.1038/s41598-026-45000-7](https://www.nature.com/articles/s41598-026-45000-7)

Standards and reference vocabularies:

- GSC MIxS host-associated extension — `host_body_site` (UBERON/FMA) and `host_disease_stat` (`MIXS:0000031`, Disease Ontology) are separate slots. [genomicsstandardsconsortium.github.io/mixs/0016002](https://genomicsstandardsconsortium.github.io/mixs/0016002/)
- ENVO `ENVO:2100003` *skin environment*, and the full 13-term descendant set of `ENVO:2100000` *anatomical entity environment*, retrieved from the EBI OLS4 API on 2026-08-17. [OLS4 ENVO:2100003](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:2100003)
- NCIT `NCIT:C3824` *Lesion*, definition as quoted, via OLS4.
- SNOMED CT `52988006 |Lesion (morphologic abnormality)|` — Body structure hierarchy, used as `116676008 |Associated morphology|` paired with `363698007 |Finding site|`. [SNOMED CT Editorial Guide](https://docs.snomed.org/snomed-ct-specifications/snomed-ct-editorial-guide/readme/snomed-ct-introduction/structure-of-domain-coverage); [September 2022 release notes](https://confluence.ihtsdotools.org/display/RMT/SNOMED+CT+September+2022+International+Edition+-+SNOMED+International+Release+notes)
- OGMS `OGMS:0000045` *disorder* — "A material entity which is clinically abnormal and part of an extended organism", via OLS4.
- In-repo evidence: `data/raw/gold_ecosystem_paths.tsv` (sibling structure and assertion counts), `curation/decisions.tsv` (sibling dispositions), `data/habitats/other/skin_environment.yaml`.

**Stated as inference, not sourced:** the sibling-structure interpretation in §1 (that GOLD's "Lesion" means *lesion NOS*) is my reading of the path table, not something GOLD documents. The heterogeneity argument in §3 is my synthesis across the acne, wound and psoriasis literature; no single source makes it.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept:** *skin lesion*; *lesional skin*; *lesional site*; *cutaneous lesion*; *affected skin*; *involved skin*; *skin lesion NOS*. GOLD's own string is bare *Lesion*.

**Do not conflate — these are commonly but wrongly treated as the same thing:**

- **Ulcer** and **abscess** — in GOLD these are explicitly *siblings*, not this concept (`... > Skin > Ulcer`, 4 assertions; `... > Skin > Abscess`, 17). Merging them here would double-count and would contradict the source hierarchy. Both already have separate HabitatMech records.
- **Wound** — implies traumatic breach of the epithelium. Many lesions (macules, plaques, comedones, nodules) are not wounds. `BTO:0003114` *wound fluid* is the exudate, not the site.
- **Infection / infected site** — a lesion need not be infected, and characterising a lesion's microbiota is not the same claim as infection. Colonisation ≠ infection.
- **Dysbiosis** — a property of a community, not a place.
- **The skin disease itself** (MONDO/DOID *psoriasis*, *atopic dermatitis*, *acne*) — the disease is the process; the lesion is the locus. This is the distinction MIxS encodes as `host_disease_stat` vs `host_body_site`.
- **`HP:0011355` *Localized skin lesion*** — a phenotypic abnormality of an organism, i.e. a quality, in the same category the corpus already handles as `NOT_APPLICABLE`-with-xref for `PATO:0001429`.
- **`BTO:0003257` *granulation tissue*** — a healing-phase tissue found inside some lesions.
- **`UBERON:0000014` *zone of skin* / `UBERON:0002097` *skin of body*** — the site without the pathological alteration; the genus's ingredient, not the concept.
- **Plant lesion** (`habitatmech:BACDIVE.31392c69b9`) and **brain lesion** — homonyms in other domains.
- **`PREGO.c312b0d6fc` *tubercle*** — already decided `CONFIRM_UNGROUNDED` on the reasoning that a tubercle-as-isolation-source is a tuberculous lesion. That is a *specific* lesion type and should not be folded into this concept, but it is the closest existing precedent in the corpus for the "the slice has no term for the lesion" finding.

---

## 6. Whether it should be a term at all

**There is a genuine case on both sides, and the corpus is currently inconsistent about it. That inconsistency should be resolved before either answer is committed.**

### The case for a term (supports the proposed definition)

- A lesion is a **material entity**, not a process or quality — OGMS models disorders that way explicitly, and SNOMED files *Lesion* under Body structure, not Clinical finding. The current curation note's premise ("a pathological finding rather than a place") is contradicted by SNOMED's own semantic tag.
- It is what is actually sampled, and the sampling literature treats it as a locus with its own methods problems (low biomass, centre-vs-edge, Levine technique).
- Lesional and non-lesional skin **on the same person** carry measurably different communities (Alekseyenko 2013's matched triplets are the cleanest demonstration).
- ENVO has no term, and the whole `anatomical entity environment` branch has no pathological axis, so nothing can be grounded to and the record cannot be resolved by grounding.

### The case against — keep `CONFIRM_UNGROUNDED`, request nothing

- **The GSC already decided this.** MIxS encodes the diseased-vs-healthy dimension in `host_disease_stat`, orthogonal to `host_body_site`. Minting a site term for "diseased skin" would put in the site axis what the field's own minimum-information standard puts in the disease axis. If that pattern were extended consistently, ENVO would need a lesional variant of every anatomical environment term.
- **SNOMED requires a site to be supplied separately** — a morphology is not a place until it is paired with a finding site. The concept only denotes a place because the GOLD *path* supplies "Skin"; the leaf label does not.
- **The bin is a residual.** GOLD's "Lesion" is what was left after Abscess and Ulcer were named separately. A residual bin is close to a sampling artefact, and it is the reason no differentia stronger than "structurally abnormal" survives contact with the class's members (§3).
- **81 assertions, one source, no cross-references.** Low evidential weight for a new ENVO term request.

### The internal inconsistency that has to be settled

`curation/decisions.tsv` currently records, from the same 2026-08-12 sweep:

- `habitatmech:GOLD.8eb824daf3` **Ulcer** → `NOT_APPLICABLE`, "names a disease, an intervention, a sampling artefact or a no-value filler rather than a place"
- `habitatmech:GOLD.ef667faebd` **Abscess: Furuncle/Boil**, `GOLD.0e7950bba4` **Breast abscess**, `GOLD.1219b1a720` **Diabetic foot ulcer (DFU)**, `GOLD.431c971c17` **Venous ulcer**, and ~15 more → all `NOT_APPLICABLE`, same reason
- `habitatmech:GOLD.5caa9dd47f` **Lesion** → `CONFIRM_UNGROUNDED`
- `habitatmech:GOLD.be021eb56c` **Lesion (fish)** → `CONFIRM_UNGROUNDED`

Ulcer, abscess and lesion are the same shape — a skin site altered by pathology. They currently have two different dispositions. Worse, DFU and venous ulcer are `NOT_APPLICABLE` despite being among the **best-characterised microbial habitats in the whole clinical literature** (Kalan 2019, Kalan 2016, Loesche 2016 above), which is hard to reconcile with `NOT_APPLICABLE`'s meaning under CLAUDE.md — "the concept is not a habitat", reserved for diseases, qualities, processes and procedures. A diabetic foot ulcer is a place with a measured pH, a measured community, and a debridement-responsive succession.

### Recommendation

**Adopt the definition above, but do it as a family decision, not for Lesion alone.** Specifically:

1. Request one ENVO term, `lesional skin environment` (or `skin lesion environment`), parent `ENVO:2100003`, with the definition sentence at the top of this report. One term serves both `GOLD.5caa9dd47f` (human) and `GOLD.be021eb56c` (fish); host specificity stays in each record's parent chain, as it already does.
2. **Reopen the sibling `NOT_APPLICABLE` decisions** on Ulcer, Abscess, DFU and venous ulcer as part of the same pass, or explicitly justify why Lesion differs from them. File this as an issue regardless of which way it goes — under CLAUDE.md's rule, every review finding becomes an issue.
3. Record in the note that the differentia is deliberately thin because the source concept is a *lesion NOS* residual bin, and that the pH/exudate properties in §3 hold only of open lesions and must **not** be written into the definition or into `environmental_parameters` for this record.

**If the curator prefers the conservative call, keep `CONFIRM_UNGROUNDED` and request nothing** — and then rewrite the existing note, because its stated reason (SNOMED and OGMS both model a lesion as a structure) does not hold. The defensible conservative reason is the MIxS one: *the pathological state belongs to the disease axis, not the site axis, and the site here is already captured by the parent record `habitatmech:GOLD.4b37ab4b76` (Skin).* That is a reason that survives checking; the current one does not.

## Citations

1. https://doi.org/10.1186/2049-2618-1-31
2. https://doi.org/10.1101/gr.131029.111
3. https://www.medrxiv.org/content/10.1101/2024.04.18.24305961
4. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:2100003
5. https://docs.snomed.org/snomed-ct-specifications/snomed-ct-editorial-guide/readme/snomed-ct-introduction/structure-of-domain-coverage
6. https://confluence.ihtsdotools.org/display/RMT/SNOMED+CT+September+2022+International+Edition+-+SNOMED+International+Release+notes
7. https://genomicsstandardsconsortium.github.io/mixs/0016002/
8. https://doi.org/10.1111/j.1467-2494.2006.00344.x
9. https://wounds-uk.com/wp-content/uploads/2023/02/content_9150.pdf
10. https://www.nature.com/articles/s41598-026-45000-7
11. https://doi.org/10.1067/mai.2001.117455
12. https://doi.org/10.1126/scitranslmed.aal4651
13. https://doi.org/10.1038/nmicrobiol.2016.106
14. https://doi.org/10.1016/j.chom.2017.06.006
15. https://doi.org/10.1038/nrmicro2537
16. https://doi.org/10.1038/nrmicro.2017.157
17. https://doi.org/10.1038/jid.2013.21
18. https://doi.org/10.1016/j.chom.2019.03.006
19. https://doi.org/10.1128/mbio.01058-16
20. https://doi.org/10.1016/j.jid.2016.08.009
21. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6729076/