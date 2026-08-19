---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T04:13:10.221883'
end_time: '2026-08-18T04:23:16.074013'
duration_seconds: 605.85
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Eutric
  habitat_identifier: habitatmech:GOLD.bfd28de801
  habitat_category: TERRESTRIAL
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Environmental > Terrestrial > Soil > Leptosol > Eutric'
  assertions: '0'
  parent_terms: ENVO:00002241
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Soil-classification\
    \ review: 'Eutric' is a WRB QUALIFIER (base saturation >=50%), not a reference\
    \ soil group, so there is no term for it and there should not be \u2014 the same\
    \ reading already recorded for Acidic, Humid, Arid and the climatic zones. The\
    \ concept the path names is a eutric leptosol, which is a real habitat, and ENVO:00002241\
    \ 'leptosol' is already attached as its parent. Confirmed rather than grounded.\
    \ Path: Environmental > Terrestrial > Soil > Leptosol > Eutric (source concept\
    \ habitatmech:GOLD.bfd28de801)"
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
  num_turns: 48
  total_cost_usd: 4.115479499999999
  session_id: d2a0074a-869a-4adb-b184-b23486801e2b
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 21
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Eutric
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.bfd28de801
- **Category:** TERRESTRIAL
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Environmental > Terrestrial > Soil > Leptosol > Eutric
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** ENVO:00002241
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Soil-classification review: 'Eutric' is a WRB QUALIFIER (base saturation >=50%), not a reference soil group, so there is no term for it and there should not be — the same reading already recorded for Acidic, Humid, Arid and the climatic zones. The concept the path names is a eutric leptosol, which is a real habitat, and ENVO:00002241 'leptosol' is already attached as its parent. Confirmed rather than grounded. Path: Environmental > Terrestrial > Soil > Leptosol > Eutric (source concept habitatmech:GOLD.bfd28de801)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Eutric** as a microbial habitat, with citations.

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

# Eutric — `habitatmech:GOLD.bfd28de801`

> **Proposed definition:** A leptosol whose mineral material below 20 cm has an effective base saturation of 50% or more — that is, in which exchangeable Ca+Mg+K+Na equals or exceeds exchangeable Al.

*(Label recommendation: the record should be labelled `eutric leptosol`, not `Eutric`. See §6.)*

---

## 1. What the concept denotes

**As a habitat, this is a soil — specifically, a shallow, rock-limited soil whose cation exchange complex is dominated by base cations rather than aluminium.** A sample taken from it is a sample of the fine earth of a Leptosol profile, typically only a few centimetres to ~25 cm of solum sitting on continuous rock or on a mass of coarse fragments.

The label as GOLD gives it is *not* the habitat. "Eutric" alone is a **WRB qualifier** — a modifier that attaches to a Reference Soil Group, exactly like "Dystric", "Calcaric" or "Skeletic". The curator's note already records this correctly. The **concept the path denotes** is the composite `Eutric Leptosol`, which is a real, named, mappable soil, and it is that composite the definition should describe.

**Boundary — what is inside:**
- Very shallow soils (continuous rock starting ≤ 25 cm from the soil surface) or soils with < 20% fine earth by volume averaged over 75 cm, *and* with no duric, petrocalcic, petroduric, petrogypsic, pisoplinthic or spodic horizon — this is the WRB 2022 key entry for LEPTOSOLS ([IUSS Working Group WRB 2022, 4th ed., Ch. 4](https://files.isric.org/public/documents/WRB_fourth_edition_2022-12-18.pdf)).
- …in which exchangeable (Ca+Mg+K+Na) ≥ exchangeable Al in the major part of the mineral material between 20 cm and the limiting layer — the WRB 2022 **Eutric** criterion (Ch. 5, qualifier definitions; quoted verbatim in §3).

**Boundary — what is a neighbouring concept, not this one:**
- **Dystric Leptosol** — the mutually exclusive sibling; exchangeable Al > exchangeable bases. WRB lists these as `Dystric/ Eutric`, explicitly "mutually exclusive" (Ch. 2.1, rule on the slash notation).
- **Rendzic / Calcaric Leptosol** — the carbonate-rich shallow soils over limestone (the former Rendzinas). These are base-rich too, but WRB's redundancy rule removes the Eutric name from them: *"Qualifiers conveying redundant information are not added. This is a general rule and applies even if the slash is not used. For example, Eutric is not added if the Calcaric qualifier applies."* (WRB 2022, Ch. 2.1). This is the single most important boundary and the one most often got wrong — see §5.
- **Lithic / Nudilithic Leptosol** — continuous rock starting ≤ 10 cm, or at the surface (WRB 2022 Ch. 5, "in Leptosols only").
- **Coarsic Leptosol** — < 20% fine earth plus dead plant residues over 75 cm; the stone-dominated end of the group (the former Hyperskeletic).
- **Regosol** (`ENVO:00002256`) — weakly developed soils that are explicitly *not* very shallow or very gravelly; ENVO's own definition for regosol names Leptosols as the excluded case.
- **Endolithic environment** (`ENVO:01000303`) — rock interior, not soil. The rock *beneath* a Leptosol is not part of this concept.

**One ambiguity worth recording, and it is a real one.** The 50% threshold has been attached to two different quantities across WRB editions:

| Edition | Criterion for Eutric |
|---|---|
| FAO Revised Legend 1990 / WRB 1998 / WRB 2006 | base saturation (exchangeable bases ÷ CEC by 1 M NH₄OAc at pH 7) ≥ 50%, over specified depth ranges |
| WRB 2014 / 2022 | **effective** base saturation (exchangeable bases ÷ [bases + exchangeable Al]) ≥ 50%, equivalently bases ≥ Al |

These are not interchangeable. In a database of > 290,000 soil horizons, 50% BS corresponds to roughly **75–77% BSe** in mineral soils (85% in Andosols), so keeping the number and changing the denominator materially widened the Eutric class ([Kabała et al. 2025, *Geoderma*](https://www.sciencedirect.com/science/article/pii/S0016706125003064); [preprint copy](https://edepot.wur.nl/699162)). The effect can be extreme: in Japanese Andosols, 80% of samples met Eutric under WRB2014 versus 2% under WRB2006 ([Kubotera & Yamaguchi 2020, *Soil Sci. Plant Nutr.* 66:4, doi:10.1080/00380768.2020.1783699](https://www.tandfonline.com/doi/full/10.1080/00380768.2020.1783699)). A definition should therefore either name the edition or state the criterion in the edition-neutral form "exchangeable bases ≥ exchangeable Al (effective base saturation ≥ 50%)".

**Which reading does the GOLD data mean?** GOLD does not say, and I cannot resolve it from the data. Two observations bear on it, both from this repo's own `data/raw/gold_ecosystem_paths.tsv`:

- GOLD's `Soil` subtype layer uses WRB Reference Soil Group names for exactly **two** subtypes out of ~90 — `Leptosol` and `Solonetz`. Every other subtype is a landform, land use, texture class or biome (`Desert`, `Arable`, `Clay`, `Boreal forest/Taiga`, …). This is not a WRB-derived facet; it is two one-off submitter descriptions.
- Both `Leptosol` (`gold.ecosystem:6001`) and `Leptosol > Eutric` (`gold.ecosystem:6002`) carry `organism_count = 0`, `study_count = 0`, `biosample_count = 0`. The path exists in GOLD's tree with nothing attached to it.

That pattern — a soil-survey-style name entered by one submitter — makes the legacy map-unit reading (FAO-90 `LPe`, base saturation ≥ 50%) at least as likely as strict WRB 2022. *This is my inference from the path structure and counts, not something GOLD states.*

## 2. Genus — the broader kind

**Genus: `leptosol` — `ENVO:00002241`.** This is an existing, exact, well-established ENVO term and it is already attached to the record as the nearest broader term. Its definition:

> "Leptosols are very shallow soils over continuous rock and soils that are extremely gravelly and/or stony. Leptosols are azonal soils and particularly common in mountainous regions." (synonyms: *gravelly soil*, *stony soil*) — [OLS4 / ENVO:00002241](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002241)

ENVO's soil branch mirrors the WRB Reference Soil Groups (`calcisol` ENVO:00002239, `luvisol` ENVO:00002248, `regosol` ENVO:00002256, `umbrisol` ENVO:00002253, …) under `soil` (`ENVO:00001998`) → `environmental material` (`ENVO:00010483`) ([Buttigieg et al. 2013, *J. Biomed. Semantics* 4:43, doi:10.1186/2041-1480-4-43](https://doi.org/10.1186/2041-1480-4-43); [Buttigieg et al. 2016, *J. Biomed. Semantics* 7:57, doi:10.1186/s13326-016-0097-6](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/)).

So the genus is settled. The question is only whether a term for the *species* (eutric leptosol) exists. It does not.

**Near-misses checked and why each fails** (all queried against the EBI OLS4 API, ENVO current release, August 2026):

| Candidate | Result | Why it fails |
|---|---|---|
| `eutric` / `eutric leptosol` in ENVO | **0 hits** | ENVO carries no WRB qualifier terms at all — not Eutric, Dystric, Calcaric, Rendzic, Lithic or Skeletic. There are no subclasses of `leptosol`. |
| `rendzina` in ENVO | **0 hits** | No term for the calcareous shallow-soil sibling either, so there is nothing nearby to hang this off. |
| `basic cation exchange capacity` `ENVO:06105242` | Exists | It is a **characteristic** ("a cation exchange capacity which inheres in an environmental material…"), not a habitat, and it is CEC, not base saturation. Useful as a conceptual pointer; wrong type to ground to and wrong quantity. |
| `lixisol` `ENVO:00002242`, `luvisol` `ENVO:00002248`, `phaeozem` `ENVO:00002249` | Exist | These *do* carry "high base saturation" in their textual definitions — proof that ENVO can express the property — but each is a different Reference Soil Group with an argic horizon or a deep mollic-like profile. All are deep, developed soils; a Leptosol is neither. Not broader, not narrower — disjoint. |
| `ultisol` `ENVO:01001397` | Exists | Defined by "< 35% base saturation" — i.e. ENVO already encodes a base-saturation threshold, but only where USDA Soil Taxonomy supplies it as part of an order. USDA has no Leptosol equivalent at that level (the closest is Lithic subgroups of Entisols). |
| `calcisol` `ENVO:00002239` | Exists | Secondary lime accumulation; asserts a calcic horizon the sources here do not claim, and would be redundant-with-Calcaric in WRB terms. Over-claims. |
| `regosol` `ENVO:00002256` | Exists | ENVO's own definition explicitly excludes soils that are "very shallow or very rich in gravels (Leptosols)". Disjoint. |
| `endolithic environment` `ENVO:01000303` | Exists | Rock interior. Different habitat entirely. |
| AGROVOC `Leptosols` `c_da0af025` | Exists, broader = "World Reference Base soil types" | AGROVOC also stops at the RSG level; **no narrower terms** listed. Confirms the qualifier level is unrepresented in the reference vocabularies, not just in ENVO. ([AGROVOC](https://agrovoc.fao.org/browse/agrovoc/en/page/c_da0af025)) |
| PATO / CHMO "base saturation" | **0 relevant hits** | No quality term for base saturation exists to xref, unlike `PATO:0001429` for "Acidic". |

**Conclusion: the curator's `CONFIRM_UNGROUNDED` is correct, and `ENVO:00002241` is the right and only parent.** Do not ground this record to `ENVO:00002241` itself — that term is the identity of the *sibling* record `Environmental > Terrestrial > Soil > Leptosol` (`gold.ecosystem:6001`), and grounding both would merge the qualified and unqualified concepts.

## 3. Differentia — what distinguishes it

The differentia is **base status of the exchange complex**, and it is measurable by a standard laboratory procedure.

**The authoritative criterion, WRB 2022 (verbatim, Ch. 5):**

> **Eutric (eu)** (from Greek *eu*, good, and *trophae*, food):
> • in Histosols, having a pH<sub>water</sub> of ≥ 5.5 in the major part with organic material, within 100 cm of the soil surface,
> • in other soils, having one or more layers consisting of mineral material,
> ➢ between 20 and 100 cm of the mineral soil surface, or
> ➢ between 20 cm of the mineral soil surface and a limiting layer starting > 25 cm from the mineral soil surface,
> whichever is shallower,
> that have **exchangeable (Ca+Mg+K+Na) ≥ exchangeable Al** in the major part of their combined thickness.

And its exclusive complement:

> **Dystric (dy)**: … having one or more layers consisting of mineral material [same depth ranges] that have **exchangeable Al > exchangeable (Ca+Mg+K+Na)** in half or more of their combined thickness.

**Observable / measurable properties that follow:**

1. **Exchangeable base cations dominate exchangeable aluminium** — determined by 1 M NH₄OAc (pH 7) or unbuffered salt extraction plus KCl-extractable Al. This is the defining measurement.
2. **Near-neutral to alkaline reaction, and low Al toxicity.** Al³⁺ only becomes appreciably exchangeable below roughly pH 5.5, so an Al-subordinate exchange complex implies a soil that is not strongly acid. *This is standard soil-chemical reasoning rather than a sentence I found stated for the Eutric qualifier specifically — treat it as inference.* Base saturation and pH are the two sides of the same measurement, and the WRB itself uses pH ≥ 5.5 as the Eutric criterion in Histosols (above), which makes the equivalence explicit within the standard.
3. **Rock-limited depth and negligible water storage** — from the genus, not the differentia: Leptosols are "unattractive soils for rainfed agriculture because of their inability to hold water" ([FAO/ISRIC, *Leptosols*](https://isric.org/all-about-soil/leptosols/)). For a microbial habitat this is the dominant physical control: shallow rooting volume, strong wet–dry cycling, high coarse-fragment content, close coupling to parent rock.
4. **Not carbonatic.** Under the WRB redundancy rule (Ch. 2.1), a Leptosol that is Calcaric (calcaric material in a ≥ 30 cm layer, or in the major part above a limiting layer starting < 60 cm) is *not* named Eutric. And in the FAO-90 legend the units were keyed in order, with Lithic, Rendzic, Mollic and Umbric preceding Eutric/Dystric, so `LPe` was effectively the residual base-rich unit ([Bureau/Deckers et al., *The classification of Leptosols in the WRB*, 19th WCSS](https://www.old.iuss.org/19th%20WCSS/Symposium/pdf/2302.pdf)). **A eutric leptosol is base-rich because of its silicate mineralogy or base-rich non-carbonate parent rock, not because it sits on limestone.**

**Why the differentia matters for microbiology.** Base status is not an incidental soil-survey label; the pH/base-cation axis is the strongest known single predictor of soil bacterial community composition and diversity:

- Overall bacterial community composition across 88 North and South American soils correlated with soil pH at r = 0.79 (UniFrac), driven by shifts in *Acidobacteria*, *Actinobacteria* and *Bacteroidetes* ([Lauber, Hamady, Knight & Fierer 2009, *Appl. Environ. Microbiol.* 75:5111–5120, doi:10.1128/AEM.00335-09](https://journals.asm.org/doi/10.1128/aem.00335-09); [PMC2725504](https://pmc.ncbi.nlm.nih.gov/articles/PMC2725504)).
- Phylotype diversity vs pH gave R² = 0.70, with mean annual temperature, PET and latitude poor predictors by comparison ([Fierer & Jackson 2006, *PNAS* 103:626–631, doi:10.1073/pnas.0507535103](https://doi.org/10.1073/pnas.0507535103)).
- The relationship is reproducible within a single soil type across an experimental pH gradient ([Rousk et al. 2010, *ISME J.* 4:1340–1351, doi:10.1038/ismej.2010.58](https://www.nature.com/articles/ismej201058)).

So "Dystric vs Eutric" partitions Leptosols along precisely the gradient that most structures their microbiota. That is a defensible reason for the concept to exist as a habitat distinction, and it is worth putting in the record's `notes`.

**One technical caveat the curator should be aware of.** Read literally against WRB 2022, the Eutric depth window ("between 20 cm and a limiting layer starting **> 25 cm**") cannot be satisfied by a Leptosol whose continuous rock starts at ≤ 25 cm — which is the defining case 1a for the RSG. Under the 4th edition, Eutric is therefore applicable chiefly to Leptosols keyed in under criterion 1b (Coarsic: < 20% fine earth) with a limiting layer deeper than 25 cm. **This is my reading of the two definitions side by side, not a statement any source makes**, and it is a further reason to think GOLD's "Eutric Leptosol" reflects legacy FAO-90/WRB-1998 usage, where the criterion was base saturation over the upper 20–50 cm and no such gap arose. It does not affect the definition sentence, which states the chemical criterion rather than a depth window.

## 4. Sources

**Standards and reference vocabularies (primary)**

- IUSS Working Group WRB (2022). *World Reference Base for Soil Resources. International soil classification system for naming soils and creating legends for soil maps.* 4th edition. International Union of Soil Sciences, Vienna. ISBN 979-8-9862451-1-9. PDF (18 December 2022 corrected printing): https://files.isric.org/public/documents/WRB_fourth_edition_2022-12-18.pdf — **Ch. 2.1** (general rules; slash notation; the Calcaric-redundancy rule), **Ch. 4** (Key: LEPTOSOLS entry and its principal/supplementary qualifier lists, which include `Dystric/ Eutric`), **Ch. 5** (verbatim Eutric, Dystric, Calcaric, Lithic, Nudilithic, Coarsic, Skeletic, Rendzic definitions). Open access, CC-BY. All verbatim quotations above are from this document.
- Schad, P. (2023). World Reference Base for Soil Resources — its fourth edition and its history. *J. Plant Nutr. Soil Sci.* 186(2):151–163. doi:10.1002/jpln.202200417 — https://onlinelibrary.wiley.com/doi/10.1002/jpln.202200417
- FAO–UNESCO (1990). *Soil Map of the World: Revised Legend.* World Soil Resources Report 60 — the source of the `LPe` map unit. (I did not retrieve the verbatim LPe text; the unit list and its keying order are reported secondarily by Deckers et al., below. Flagging this as a gap: **the exact 1990 control section and threshold for LPe should be checked against WSRR 60 before being quoted in a definition.**)
- ENVO: `leptosol` `ENVO:00002241`, `soil` `ENVO:00001998`, `regosol` `ENVO:00002256`, `basic cation exchange capacity` `ENVO:06105242` — https://www.ebi.ac.uk/ols4/ontologies/envo ; ontology home https://github.com/EnvironmentOntology/envo
- AGROVOC `Leptosols`, URI http://aims.fao.org/aos/agrovoc/c_da0af025 — https://agrovoc.fao.org/browse/agrovoc/en/page/c_da0af025
- GOLD Ecosystem Classification (path source): https://gold.jgi.doe.gov/ecosystem_classification ; Ivanova et al. (2010), *A call for standardized classification of metagenome projects*, *Environ. Microbiol.* 12:1803–1805, doi:10.1111/j.1462-2920.2010.02170.x

**Soil-classification literature on Leptosols and the Eutric qualifier**

- Deckers, J. et al. *The classification of Leptosols in the World Reference Base for Soil Resources.* 19th World Congress of Soil Science — https://www.old.iuss.org/19th%20WCSS/Symposium/pdf/2302.pdf (FAO unit list: Gelic, Lithic, Rendzic, Umbric, Mollic, Eutric, Dystric; growth from 3 classes in the 1974 Legend to ≥ 36 units in WRB; recommendation to reduce them).
- Kubotera, H. & Yamaguchi, N. (2020). New definition of the qualifiers for Dystric and Eutric should be noted for the classification of Andosols with WRB2014. *Soil Sci. Plant Nutr.* 66(4):604–608. doi:10.1080/00380768.2020.1783699 — https://www.tandfonline.com/doi/full/10.1080/00380768.2020.1783699
- Kabała, C. et al. (2025). Relationships between base saturation, effective base saturation and soil pH as the references for the development and verification of criteria for international soil classification. *Geoderma*. https://www.sciencedirect.com/science/article/pii/S0016706125003064 (50% BS ≈ 75–77% BSe; warns of overestimation of Eutric soils).
- ISRIC / FAO, *Leptosols* fact sheet — https://isric.org/all-about-soil/leptosols/ ; extent ~1.655 billion ha, the most extensive RSG globally, of which ~545 million ha in mountainous environments (ISSS Working Group RB 1998, as reported by Deckers et al.). **Note:** the widely repeated "1.7 billion ha" figure (e.g. [Wikipedia, *Leptosol*](https://en.wikipedia.org/wiki/Leptosol)) is a rounding of this; prefer ~1.6 billion ha with the ISRIC/FAO attribution.

**Microbial ecology — the habitat**

- Lauber, C.L., Hamady, M., Knight, R. & Fierer, N. (2009). Pyrosequencing-based assessment of soil pH as a predictor of soil bacterial community structure at the continental scale. *Appl. Environ. Microbiol.* 75(15):5111–5120. doi:10.1128/AEM.00335-09
- Fierer, N. & Jackson, R.B. (2006). The diversity and biogeography of soil bacterial communities. *PNAS* 103(3):626–631. doi:10.1073/pnas.0507535103
- Rousk, J. et al. (2010). Soil bacterial and fungal communities across a pH gradient in an arable soil. *ISME J.* 4:1340–1351. doi:10.1038/ismej.2010.58
- Kimeklis, A.K. et al. (2021). Microbiomes of different ages in Rendzic Leptosols in the Crimean Peninsula. *PeerJ* 9:e10871. doi:10.7717/peerj.10871 (PMID 33643711) — four Rendzic Leptosol sites, pH 7.6–8.2, CaCO₃ 4.8–45.6%; *Actinobacteria*, *Proteobacteria*, *Acidobacteria*, *Bacteroidetes*, *Thaumarchaeota* dominant; horizon, parent material and litter outweighed soil age. **This is a Rendzic, not Eutric, Leptosol — cite it as evidence about the genus and the neighbouring concept, not about this concept.**
- Aguilar-Rangel, E.J. et al. (2021). Microbial diversity and physicochemical characteristics of tropical karst soils in the northeastern Yucatan peninsula, Mexico. *Appl. Soil Ecol.* doi:10.1016/j.apsoil.2021.104006 — Rendzic Leptosols, pH ~8.4, organic C 17–29%, 2.8 × 10⁷ 16S rDNA copies g⁻¹, 9.3 × 10⁴ ITS copies g⁻¹. Same caveat: Rendzic.
- Carranca, C. et al. (1999). Biological nitrogen fixation estimated by ¹⁵N dilution, natural ¹⁵N abundance, and N difference techniques in a subterranean clover–grass sward under Mediterranean conditions. *Eur. J. Agron.* doi:10.1016/S1161-0301(98)00056-2 — one of the very few papers that measures a microbially mediated process (symbiotic BNF) on a site explicitly described as a Eutric Leptosol.

**A literature-coverage finding worth recording.** A full-text Europe PMC search for the exact phrase `"eutric leptosol"` returns **6 articles** across the entire indexed corpus, and **none of them is a microbiology, microbial-ecology or metagenomics paper** — they are Ethiopian forest inventory and soil-fertility studies, a Mediterranean agronomy paper, and an NIR-spectroscopy methods paper (query: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22eutric%20leptosol%22&format=json). There is, as of this search, **no published study of the microbiome of a soil described as a Eutric Leptosol.** Anything the definition says about the biology of this specific habitat is therefore extrapolation from Leptosols generally and from the pH/base-status literature, and should be worded as such.

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**

| Name | Register |
|---|---|
| Eutric Leptosol | WRB 1998/2006/2014/2022 soil name |
| Eutric Leptosols (LPe) | FAO–UNESCO 1990 Revised Legend map unit; carried into the Harmonized World Soil Database and derived global soil maps |
| base-rich shallow soil / base-saturated shallow soil | descriptive |
| eutric ranker | approximate legacy equivalent — the FAO Rankers (shallow soils over non-calcareous rock) split into Umbric and Dystric/Eutric Leptosols. *Approximate, not synonymous.* |

Etymology, from the WRB itself: **Eutric**, "from Greek *eu*, good, and *trophae*, food"; **Dystric**, "from Greek *dys*, bad, and *trophae*, food" (WRB 2022, Ch. 5).

**Do not conflate with:**

1. **Eutrophic.** This is the big one, and the etymology above is exactly why it happens. `eutrophic water` `ENVO:00002224` ("water with a high nutrient level"), `eutrophic lake` `ENVO:01000548`, `eutrophic pond` `ENVO:03600037`, `hypereutrophic water` `ENVO:01001018` all exist in ENVO and all mean **nutrient-enriched, usually N and P, usually in an aquatic body, usually anthropogenic**. Eutric means **base-cation-saturated exchange complex in soil**. A Eutric Leptosol is typically nutrient-*poor* — shallow, low in total N and water-holding capacity. Grounding this record to any eutrophic-* term would be a straightforward category error and should be explicitly warned against in the record's notes.
2. **Rendzina / Rendzic Leptosol / calcareous shallow soil.** Base-rich, yes — but WRB's redundancy rule means a carbonate-containing Leptosol is named Calcaric or Rendzic, *not* Eutric ("Eutric is not added if the Calcaric qualifier applies", WRB 2022 Ch. 2.1). This matters practically: the only two published Leptosol microbiome studies I found (Crimea, Yucatán) are both **Rendzic** and both moderately alkaline with high carbonate — they are the *neighbouring* concept, and citing them as if they described this one would be exactly the plausible-sounding unsupported claim the corpus guards against.
3. **Calcisol** `ENVO:00002239`. Secondary lime accumulation; a different RSG.
4. **Lithosol / Lithic Leptosol.** A depth criterion (rock ≤ 10 cm), not a chemistry criterion. Orthogonal.
5. **Alfisol / Mollisol** (USDA). Both are base-rich orders (Mollisols have ≥ 50% base saturation in the mollic epipedon), but both are deep, developed profiles. There is no USDA equivalent of "Eutric Leptosol"; the nearest is a Lithic subgroup of an Entisol, which carries no base-status claim.
6. **"Eutric" the qualifier applied to any other RSG.** Eutric Cambisol, Eutric Regosol, Eutric Fluvisol, Eutric Gleysol and Eutric Stagnosol are all real WRB names and all appear in WRB 2022's examples. They are **not** this concept. The genus is what distinguishes them, and this is precisely why the record must be labelled and defined as *eutric leptosol* rather than as bare *Eutric* — the bare label is not unique to any habitat.

## 6. Should it be a term at all?

**Yes — but as `eutric leptosol`, not as `Eutric`, and at low priority.**

**It is a habitat.** The concept the path names is a soil: a physical material a sample is drawn from, with a defined depth, a defined mineralogy and a measurable chemistry. It is not a process, a disease, a quality, an organism or a sampling artefact. This distinguishes it cleanly from `Acidic`, `Humid`, `Arid` and the climatic zones the curator's note compares it to — those are bare qualities with no genus attached, and `PATO:0001429` is the right disposition for them. Here the genus *is* attached, in the path itself, one level up. `Environmental > Terrestrial > Soil > Leptosol > Eutric` is not a naked quality; it is a qualified soil, and the WRB reads it that way too (a qualifier is meaningless except as a modifier of an RSG).

So `CONFIRM_UNGROUNDED` with `ENVO:00002241` as parent is right, and the parent relation is genuinely *broader* — every eutric leptosol is a leptosol — so `relation: parent` is correct here, not `xref`.

**Three things to weigh before requesting an ENVO term:**

1. **Zero attestations.** `data/raw/gold_ecosystem_paths.tsv` records `organism_count = 0`, `study_count = 0`, `biosample_count = 0` for `gold.ecosystem:6002`. No sample in GOLD has ever been assigned this path. By the report's own "ungrounded records ranked by upstream assertion volume" ordering, this sits at the bottom of the backlog.
2. **No microbiological literature exists for it** (§4). A term request that cannot cite a single study of the habitat is weak, and a definition written from Rendzic Leptosol papers would misattribute.
3. **Requesting it opens a very large door.** ENVO currently has *no* WRB qualifier-level subdivisions of any Reference Soil Group — not one, for any of the ~32 RSGs. AGROVOC likewise lists no narrower terms under Leptosols. WRB 2022 defines on the order of 200 qualifiers, most of them combinable with most RSGs; the Leptosol entry alone lists 15 principal and ~35 supplementary qualifiers. Asking ENVO for `eutric leptosol` is asking it to start a combinatorial family it has deliberately not started. **That is an argument to raise with ENVO explicitly rather than to route around** — if ENVO does want WRB qualifier coverage, `eutric leptosol` is a perfectly ordinary member of it; if it does not, this record should simply stay a minted HabitatMech identifier with a good definition and `ENVO:00002241` as parent, which costs nothing and loses nothing.

**Recommended disposition:** keep the minted identity; keep `ENVO:00002241` as `relation: parent`; adopt `eutric leptosol` as the record label with `Eutric` retained as the GOLD source label; write the definition below; record in `notes` the edition ambiguity (§1), the eutrophic/rendzic non-conflations (§5), and the fact that no microbiome study of this soil exists. Defer the ENVO term request pending a policy answer on WRB qualifiers.

---

## The definition, with the alternatives a curator might prefer

**Recommended (edition-neutral, states the criterion in the form both editions agree on for the qualitative case):**

> A leptosol whose mineral material below 20 cm has an effective base saturation of 50% or more — that is, in which exchangeable Ca+Mg+K+Na equals or exceeds exchangeable Al.

**If the definition should track WRB 2022 exactly:**

> A leptosol having one or more layers of mineral material, between 20 cm of the mineral soil surface and the underlying limiting layer, in which exchangeable Ca+Mg+K+Na equals or exceeds exchangeable Al in the major part of their combined thickness.

**If the non-carbonate exclusion should be carried in the definition rather than in the notes** — defensible, since it is what separates this from the rendzic/calcaric siblings in practice, but it is a naming rule rather than a soil property, so I would keep it in `notes`:

> A leptosol which has an effective base saturation of 50% or more below 20 cm and which does not contain calcaric material.

I would not go longer than one of these. If a curator finds the sentence still under-specified, the thing that is actually missing is an intermediate ENVO class along the lines of *base-rich soil* / *high base status soil* — a genus that would let both `eutric leptosol` and `eutric cambisol` be defined against a shared parent instead of restating the chemistry each time. Saying that to ENVO is more useful than a longer sentence here.

## Citations

1. https://files.isric.org/public/documents/WRB_fourth_edition_2022-12-18.pdf
2. https://www.sciencedirect.com/science/article/pii/S0016706125003064
3. https://edepot.wur.nl/699162
4. https://www.tandfonline.com/doi/full/10.1080/00380768.2020.1783699
5. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002241
6. https://doi.org/10.1186/2041-1480-4-43
7. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/
8. https://agrovoc.fao.org/browse/agrovoc/en/page/c_da0af025
9. https://isric.org/all-about-soil/leptosols/
10. https://www.old.iuss.org/19th%20WCSS/Symposium/pdf/2302.pdf
11. https://journals.asm.org/doi/10.1128/aem.00335-09
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC2725504
13. https://doi.org/10.1073/pnas.0507535103
14. https://www.nature.com/articles/ismej201058
15. https://onlinelibrary.wiley.com/doi/10.1002/jpln.202200417
16. https://www.ebi.ac.uk/ols4/ontologies/envo
17. https://github.com/EnvironmentOntology/envo
18. http://aims.fao.org/aos/agrovoc/c_da0af025
19. https://gold.jgi.doe.gov/ecosystem_classification
20. https://en.wikipedia.org/wiki/Leptosol
21. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22eutric%20leptosol%22&format=json