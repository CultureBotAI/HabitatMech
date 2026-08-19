---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T04:59:05.957430'
end_time: '2026-08-18T05:06:06.723431'
duration_seconds: 420.77
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Biofilm
  habitat_identifier: habitatmech:GOLD.7f436f8aff
  habitat_category: ENGINEERED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Environmental > Air > Indoor Air > Air scrubber > Biofilm'
  assertions: '0'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. A biofilm
    growing inside an air scrubber. Whatever GOLD''s branch, a biofilm is not air;
    it is a community on engineered equipment. (source concept habitatmech:GOLD.7f436f8aff)'
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
  num_turns: 25
  total_cost_usd: 2.714008
  session_id: 69284ec7-ac82-4fa1-af81-b2d3e5cc4a49
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 20
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Biofilm
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.7f436f8aff
- **Category:** ENGINEERED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Environmental > Air > Indoor Air > Air scrubber > Biofilm
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. A biofilm growing inside an air scrubber. Whatever GOLD's branch, a biofilm is not air; it is a community on engineered equipment. (source concept habitatmech:GOLD.7f436f8aff)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Biofilm** as a microbial habitat, with citations.

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

# Novel-term research: **Biofilm** (`habitatmech:GOLD.7f436f8aff`)

> **Proposed definition:** A biofilm which grows on the wetted packing, walls and sump surfaces inside an air scrubber, sustained by pollutants transferred out of the gas stream the device treats into the liquid film that irrigates it.

---

## ⚠️ Read this before writing the definition: a genus already exists

The curation note on this record says *"no ontology term fits this concept."* That is too strong, and it is the reason the record landed in `curation/term_requests/needs_a_parent_first.tsv` with the complaint *"no ontology parent on the record, so there is no genus to write a definition from."*

**`ENVO:00002034` "biofilm" exists, is in the vendored slice, and is already the asserted parent of at least ten sibling GOLD "Biofilm" leaves in this corpus.** Verified directly:

- `data/raw/ontology_terms.tsv` line for `ENVO:00002034` — *"A complex aggregation of microorganisms marked by the excretion of a protective and adhesive matrix; usually adhering to a substratum."*
- `data/habitats/engineered/biofilm__c8931a26.yaml` (`Engineered > Artificial ecosystem > Vivarium > Seawater aquarium > Biofilm`) — `grounding_status: NARROW`, `parent_habitats: [ENVO:00002034, …]`
- `data/habitats/aquatic/biofilm__599a99de.yaml` (`Environmental > Aquatic > Freshwater > Creek > Biofilm`) — same shape.

This record differs from those siblings only in that a `CONFIRM_UNGROUNDED` decision was recorded against it on 2026-08-13, which removed the parent the seeder would otherwise have attached. There are five GOLD "Biofilm" leaves tied at depth 4 (`Engineered > Bioreactor > Aerobic|Anaerobic|Photobioreactor (PBR) > Biofilm`, `Engineered > Bioremediation > Thiocyanate > Biofilm`, `Environmental > Terrestrial > Soil > Biofilm`), so under the documented ambiguous-leaf rule nothing claims `ENVO:00002034` outright and every deeper leaf gets `NARROW` + the term as parent. This leaf is at depth 5.

**Recommended disposition: `GROUND_AS_PARENT` → `ENVO:00002034` "biofilm", `relation: parent`** — restoring consistency with the siblings and supplying the genus. `CONFIRM_UNGROUNDED` was the wrong instrument here; the concept *is* narrower than plain biofilm, but plain biofilm is a perfectly good genus for it. What has no ENVO term is the **parent** record, `Air scrubber` (`habitatmech:GOLD.ebf95a8a4a`) — an OLS4 search of ENVO for "scrubber" returns `numFound: 0`, so that record's `CONFIRM_UNGROUNDED` is correct and this one inherited a verdict that belongs to it.

---

## 1. What the concept denotes

The thing sampled is **microbial biomass scraped, swabbed or cut from surfaces inside an air-scrubbing device** — overwhelmingly from the *packing material* (the inert carrier bed: polypropylene rings, lava rock, clay pellets, wood chips) over which recirculating water is sprayed while a fan forces the air stream through. In a full-scale unit, sampling is described as "composite samples collected from multiple positions across the packing surface," and the biofilm is characterised as "a consortium of bacteria" developing on that inert packing ([Van der Heyden et al. 2019, *Microb Biotechnol* 12(4):775–786, doi:10.1111/1751-7915.13417](https://doi.org/10.1111/1751-7915.13417)).

**Source path evidence.** `Environmental > Air > Indoor Air > Air scrubber > Biofilm`, GOLD ecosystem 5806, one leaf of a five-level GOLD ecosystem classification path ([Mukherjee et al. 2023, *NAR* 51(D1):D957–D963, doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974)). The parent leaf 5805 is `Air scrubber` itself. **The record carries zero upstream assertions** — no GOLD study is filed under it — so there is no taxon evidence from the source; everything below is literature about scrubber biofilms generally, and I say so where it matters.

**Boundary — inside the concept:** biomass attached to packing/carrier media, scrubber housing walls, spray nozzles, demister/mist eliminator surfaces, and sump walls.

**Boundary — neighbouring concepts, outside:**
- the **device** itself (`Air scrubber`, `habitatmech:GOLD.ebf95a8a4a`, the parent record);
- the **recirculating washing water / sump liquor** — a distinct liquid habitat, and the matrix actually sampled in the *Legionella* survey below;
- the **treated air / bioaerosol** leaving the unit — a real and separate habitat, because sheared biofilm becomes airborne (see §3);
- the **activated-sludge inoculum** some operators add;
- the **dry filter media and dust** of a non-wetted air cleaner (see the third reading in §1a).

### 1a. The label is ambiguous — three readings

I have not picked one silently. Ranked by fit to the source path:

**(A) Biological air scrubber / bioscrubber / biotrickling filter — strongly preferred.** Here the biofilm *is the working part of the machine*: pollutants are absorbed from gas into the trickling liquid and oxidised by the attached consortium. This is the only reading under which "Biofilm" is a natural child leaf of "Air scrubber" — it is what an operator would sample and sequence. In livestock housing these are standard ammonia-abatement equipment ([Melse & Ogink 2005, *Transactions of the ASAE* 48(6):2303–2313](https://edepot.wur.nl/31455); [INMS measure A12, biological air scrubbers in pig housing](https://measures.inms.international/measures/a12-use-of-biological-air-scrubbers-in-pig-housing)).

**(B) Chemical (acid) or particulate wet scrubber, biofilm as fouling.** Same physical location, same genus; differs in that the biofilm is unwanted rather than cultivated, and acid scrubbers run at pH 2–4, which suppresses it. Melse & Ogink report acid scrubbers averaging 96% NH₃ removal vs 70% for biotrickling filters, i.e. the two device classes are routinely contrasted and both are called "air scrubbers."

**(C) "Air scrubber" as an HVAC or portable indoor air-cleaning appliance.** Common trade usage. Weakest reading for a *biofilm* child: dry media and UV/PCO devices do not support biofilms; where microbial growth does occur in HVAC it is on wet surfaces — cooling coils, drain pans, humidifiers ([Simmons & Crow-style HVAC heat-exchanger community work, PMC3378845](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3378845/); [filter-dust communities, *Sci Rep* 10:6486](https://www.nature.com/articles/s41598-020-63543-1)). Note also that conventional biofilters/biotrickling filters are considered **unsuitable** for treating indoor air directly, precisely because of bioaerosol and humidity release ([Rybarczyk et al. / Gabaldón-group work, *Environ Sci Technol* 2019, doi:10.1021/acs.est.8b05209](https://pubs.acs.org/doi/abs/10.1021/acs.est.8b05209)) — which further undercuts reading (C) and supports (A) with the "Indoor Air" placement being GOLD's filing artefact.

**My recommendation:** write the definition to cover (A) and (B) — i.e. *a wet air-scrubbing device*, without asserting that the biofilm is deliberately cultivated. This is my inference from the source path, not a claim any source makes about GOLD ecosystem 5806. HabitatMech has already, correctly, moved both this record and its parent out of GOLD's `Air` branch into `ENGINEERED`.

---

## 2. Genus

**`ENVO:00002034` "biofilm"** — *"A complex aggregation of microorganisms marked by the excretion of a protective and adhesive matrix; usually adhering to a substratum."* Its direct ENVO parent is `ENVO:01000549` "mass of biological material" (verified via OLS4 `hierarchicalParents`), which is also in the vendored slice.

The genus is uncontroversial in the primary literature: biofilms are communities embedded in a self-produced matrix of extracellular polymeric substances, whose emergent properties derive from that matrix ([Flemming et al. 2016, *Nat Rev Microbiol* 14(9):563–575, doi:10.1038/nrmicro.2016.94, PMID 27510863](https://pubmed.ncbi.nlm.nih.gov/27510863/)). The current conceptual model is aggregation → growth → disaggregation, deliberately *independent of surface attachment* ([Sauer et al. 2022, *Nat Rev Microbiol* 20(10):608–620, doi:10.1038/s41579-022-00767-0](https://www.nature.com/articles/s41579-022-00767-0)) — relevant here only as a caution that "surface-attached" should be phrased as characteristic rather than definitional, which is exactly how ENVO's "usually adhering" hedges it.

The Genomic Standards Consortium treats this as a first-class habitat class too: **`microbial mat/biofilm` is one of the ~15 MIxS environmental packages** ([MIxS schema](https://cmungall.github.io/mixs-source/); [EMP metadata guide](https://earthmicrobiome.ucsd.edu/protocols-and-standards/metadata-guide/)).

### Near-misses, and why each fails

| Term | Why it is not the genus |
|---|---|
| `ENVO:01000156` **biofilm material** | Names the *stuff derived from* a biofilm, not the biofilm entity. Already an independent EXACT-grounded record in this corpus (`data/habitats/other/biofilm_material.yaml`, 2,205 PREGO taxa). Using it here would collide with that record. |
| `ENVO:03605000` **periphytic biofilm** | *Narrower* — asserts "a mixture of algae, cyanobacteria, microbes, and detritus." Scrubber packing beds are dark and chemotrophic; the term would import a phototroph claim no source supports. |
| `ENVO:01000008` **microbial mat** | "A multi-layered sheet… mostly on submerged or moist surfaces." Overlapping but a different structural kind; no source describes scrubber packing biomass as a mat. |
| `ENVO:01001051` **environment determined by a biofilm on a non-saline surface** | Wrong upper kind (an *environmental system*, not a mass of material), and "non-saline" is contradicted by measured EC of 18.7–20.6 mS cm⁻¹ in the recirculating liquor (Van der Heyden 2019). Its saline counterpart `ENVO:01001056` would over-claim in the other direction. *The salinity reasoning here is my inference from the reported EC, not a statement in the paper.* |
| `ENVO:00002152` **biofilter** / `ENVO:00002123` **bioreactor** / `ENVO:00003968` **air filter** | All *devices*. These are candidate relatives for the **parent** record `Air scrubber`, not for this one — and even there they over-claim, since not every air scrubber is a biofilter. |
| `ENVO:0010001` **anthropogenic environmental material** | Too broad, and asserts anthropogenic origin of the material; the biofilm is biogenic even though its substratum is manufactured. |
| **No ENVO "scrubber" class at all** | OLS4 search of ENVO for "scrubber": `numFound: 0`. AGROVOC does carry a "scrubbers" equipment concept, but that is a device term and belongs on the parent record as an xref at most. |

---

## 3. Differentia — observable and measured

All figures below are from full-scale or pilot systems; none are from GOLD 5806, which has no data.

**Physical setting.** Attached growth on an inert packing bed inside a housed unit; forced air passes through the bed at empty-bed residence times of ~0.4–1.1 s (Melse & Ogink 2005); water is sprayed from above over the packing and recirculated, with fresh water entering at the final stage and washing water discharged when EC reaches 10–20 mS cm⁻¹ (Van der Heyden et al. 2019). Buffer-tank hydraulic retention times of ~7.3–7.7 days.

**Characteristic physicochemistry** (two full-scale pig-house biotrickling filters, Van der Heyden et al. 2019):

| Parameter | BTF 1 | BTF 2 |
|---|---|---|
| pH | 7.5 ± 0.6 | 7.1 ± 0.6 |
| EC | 18.7 ± 13.0 mS cm⁻¹ | 20.6 ± 11.3 mS cm⁻¹ |
| NH₄⁺ | 2.5 ± 1.9 gN L⁻¹ | 2.8 ± 1.8 gN L⁻¹ |
| NO₂⁻ | 2.1 ± 1.5 gN L⁻¹ | 0.6 ± 0.8 gN L⁻¹ |
| NO₃⁻ | 0.5 ± 0.3 gN L⁻¹ | 1.8 ± 1.3 gN L⁻¹ |

Contrast: acid scrubbers of reading (B) operate at pH 2–4, a regime in which the biofilm is suppressed rather than cultivated (Melse & Ogink 2005).

**Energy and carbon source — the sharpest differentia.** The community lives on what the gas phase delivers: ammonia, volatile organic compounds, H₂S, mercaptans and odorants, driven from gas into liquid by intense air/water contact over the packing, then oxidised. This is what separates a scrubber biofilm from a creek biofilm, a drinking-water-pipeline biofilm, or a leaf-surface biofilm sharing the same genus.

**Community composition** (Van der Heyden et al. 2019, 16S metabarcoding): Proteobacteria 24.7–57.7%, Bacteroidetes 21.6–45.0%, Actinobacteria 4.9–22.8%; dominant families *Comamonadaceae*, *Flavobacteriaceae*, *Cytophagaceae*, *Xanthomonadaceae*. Ammonia-oxidisers (*Nitrosomonas*) <5%; *Nitrospira* largely absent from the non-inoculated unit. A broader review reports AOB and NOB frequently <1% of reads despite driving the target function, alongside AOA, heterotrophic nitrifiers and denitrifiers ([Tandfonline 2025, doi:10.1080/00380768.2025.2498470](https://www.tandfonline.com/doi/full/10.1080/00380768.2025.2498470)). Two independently operated full-scale filters converged on similar communities, distinct from the activated-sludge inoculum — evidence that this is a reproducible habitat type and not one system's idiosyncrasy.

**Formation process.** Colonisation from the incoming air, from the recirculating water, and optionally from deliberate inoculation with activated sludge from a domestic wastewater plant; the inoculated unit reached 70.0% NH₃ removal vs 50.5% uninoculated (Van der Heyden et al. 2019). Biofilm thickness is actively managed — intermittent loading with dry air during nights and weekends is used as a control strategy, and carbon starvation during idle periods disturbs biofilm formation ([*Processes* 10(12):2531, 2022](https://www.mdpi.com/2227-9717/10/12/2531)).

**Escape into the treated stream.** Organisms in the biofilm shear off under inlet flow and leave with the treated air ([Chen et al., *Sci Total Environ* 2021, S0048969720334185](https://www.sciencedirect.com/science/article/abs/pii/S0048969720334185)). Screening of the *recirculating water* at 36 farm bioscrubbers detected neither *Legionella* spp. nor *L. pneumophila*, though below-detection presence could not be excluded (Melse et al., *J Water Technol Treat Methods*, 2020 — **caveat: this is a Boffin Access title of uncertain editorial standing; treat as suggestive, not authoritative**; [PDF](https://www.boffinaccess.com/journal-water-technology-treatment-methods/prevalence-of-legionella-2-124/JWT-2-124.pdf)). Do **not** put this in the definition — it is context for a curator, and it concerns the water phase, not the biofilm.

---

## 4. Sources

- Van der Heyden, C., Volcke, E.I.P., Brusselman, E., Demeyer, P. (2019). Long-term microbial community dynamics at two full-scale biotrickling filters treating pig house exhaust air. *Microbial Biotechnology* 12(4):775–786. doi:[10.1111/1751-7915.13417](https://doi.org/10.1111/1751-7915.13417) — **the load-bearing citation** for what the biofilm is, where it sits, its physicochemistry and its taxa.
- Flemming, H.-C., Wingender, J., Szewzyk, U., Steinberg, P., Rice, S.A., Kjelleberg, S. (2016). Biofilms: an emergent form of bacterial life. *Nat Rev Microbiol* 14(9):563–575. doi:[10.1038/nrmicro.2016.94](https://www.nature.com/articles/nrmicro.2016.94), PMID [27510863](https://pubmed.ncbi.nlm.nih.gov/27510863/) — genus, matrix/EPS.
- Sauer, K., Stoodley, P., Goeres, D.M., Hall-Stoodley, L., Burmølle, M., Stewart, P.S., Bjarnsholt, T. (2022). The biofilm life cycle. *Nat Rev Microbiol* 20(10):608–620. doi:[10.1038/s41579-022-00767-0](https://www.nature.com/articles/s41579-022-00767-0) — why "surface-attached" should stay a hedge.
- Melse, R.W., Ogink, N.W.M. (2005). Air scrubbing techniques for ammonia and odour reduction at livestock operations. *Transactions of the ASAE* 48(6):2303–2313. [Full text](https://edepot.wur.nl/31455) — device typology, acid vs biological scrubber, EBRT, removal efficiencies.
- Review (2025). Insights into microbial removal of ammonia and nitrous oxide from biological air purification reactors used for livestock farming. doi:[10.1080/00380768.2025.2498470](https://www.tandfonline.com/doi/full/10.1080/00380768.2025.2498470) — functional guilds, AOB/NOB rarity.
- Rybarczyk et al. / Gabaldón group (2019). Miniaturized biotrickling filters and capillary microbioreactors… with intended application to indoor air. *Environ Sci Technol*. doi:[10.1021/acs.est.8b05209](https://pubs.acs.org/doi/abs/10.1021/acs.est.8b05209) — why conventional BTFs are considered unsuitable for direct indoor-air treatment.
- *Processes* 10(12):2531 (2022). Removal of VOCs from air: focus on biotrickling filtration and process modeling. [Open access](https://www.mdpi.com/2227-9717/10/12/2531) — packing/carrier effects, biofilm-thickness control.
- Chen et al. (2021). Dynamics of airborne bacterial community during biofiltration of gases from a swine house. *Sci Total Environ*. [Link](https://www.sciencedirect.com/science/article/abs/pii/S0048969720334185) — biofilm shear/escape.
- Mukherjee, S. et al. (2023). Twenty-five years of GOLD: v.9. *NAR* 51(D1):D957–D963. doi:[10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974) — the five-level path this leaf comes from.
- ENVO: [`ENVO:00002034`](http://purl.obolibrary.org/obo/ENVO_00002034) via [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo); Buttigieg, P.L. et al. (2013). The environment ontology. *J Biomed Semantics* 4:43. doi:[10.1186/2041-1480-4-43](https://doi.org/10.1186/2041-1480-4-43).
- GSC MIxS `microbial mat/biofilm` environmental package: [MIxS schema](https://cmungall.github.io/mixs-source/); [EMP metadata guide](https://earthmicrobiome.ucsd.edu/protocols-and-standards/metadata-guide/).
- AGROVOC "scrubbers" (waste-gas treatment installation where a gas stream contacts a liquid): [c_43e1595d](https://agrovoc.fao.org/browse/agrovoc/es/page/c_43e1595d?clang=fi) — relevant to the **parent** record, not this one.

**Explicitly flagged as my inference, not sourced:** (a) that GOLD ecosystem 5806 means reading (A); (b) that the reported EC makes `…non-saline surface` an over-claim; (c) that the definition should span readings (A) and (B). No source addresses GOLD 5806 specifically, because nothing is filed under it.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept:** scrubber biofilm; bioscrubber biofilm; biotrickling filter biofilm; packing biofilm; carrier biofilm; packed-bed biofilm; attached biomass; "bio section" biofilm (the stage-specific name in multi-stage units). GOLD's own label is the bare `Biofilm`, disambiguated only by its parent path — which is why the record's label alone is insufficient and the definition must carry the scrubber context.

**Commonly but wrongly treated as the same thing:**
- **The air scrubber itself** — a device. Already a separate record (`habitatmech:GOLD.ebf95a8a4a`).
- **The recirculating washing water / sump liquor** — a distinct liquid habitat with its own sampling protocols; the *Legionella* survey sampled water, not biofilm.
- **Treated air and scrubber bioaerosol** — downstream, and the whole reason biofilm shear is a concern.
- **Activated sludge** — an inoculum source, a different habitat (and `ENVO:00002044` sludge is a different term).
- **`ENVO:01000156` biofilm material** — the material, already its own record here.
- **`ENVO:01000008` microbial mat** — a different structural kind.
- **A dry biofilter's compost bed** (`ENVO:00002153` compost biofilter) — packed medium of a *dry* biofilter, not a trickled scrubber packing.
- **HVAC filter dust, cooling-coil and drain-pan growth** — reading (C) territory; different device, different formation.
- **The other ~30 GOLD "Biofilm" leaves** — soil, creek, lake, aquifer, cave wall, drinking-water pipeline, MFC anode/cathode, woodchip bioreactor, leaf surface, etc. Each is a separate HabitatMech record sharing this genus and differing exactly in the differentia.

---

## 6. Should it be a term at all?

**Yes.** It is a place with a physical extent, a dominant material, a characteristic physicochemistry, and a reproducible community — a thing you take a sample from. It is not a process, quality, disease state, taxonomic grouping, or sampling artefact.

Two honest caveats a curator should weigh:

1. **Zero assertions.** No GOLD study is filed under ecosystem 5806. The term's justification is the source vocabulary's structure plus external literature, not observed data. That is a legitimate basis in this corpus, but it is thinner than for, say, the creek or drinking-water-pipeline siblings.

2. **A bespoke definition may be more than this record needs.** The cheapest correct action, and the one consistent with its ten sibling leaves, is `GROUND_AS_PARENT → ENVO:00002034` with `relation: parent`, yielding `NARROW` grounding and no hand-written definition at all. If you want a definition anyway, the sentence at the top is defensible from Van der Heyden et al. 2019 plus Melse & Ogink 2005. What is *not* defensible is the current state — `UNGROUNDED` with no parent, on the strength of a note claiming no ontology term fits, when `ENVO:00002034` is in the slice and is doing exactly this job elsewhere in the corpus.

**If the definition sentence needs to be narrower than the one proposed** — e.g. asserting that the biofilm is the device's deliberately cultivated working element — then reading (A) has been chosen over (B), and the honest move is to say so in `notes` rather than to lengthen the sentence. The alternative reading of the intermediate class is "*wet air-scrubbing device*", which ENVO does not have; that gap belongs to the parent record and is already recorded there.

## Citations

1. https://doi.org/10.1111/1751-7915.13417
2. https://doi.org/10.1093/nar/gkac974
3. https://edepot.wur.nl/31455
4. https://measures.inms.international/measures/a12-use-of-biological-air-scrubbers-in-pig-housing
5. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3378845/
6. https://www.nature.com/articles/s41598-020-63543-1
7. https://pubs.acs.org/doi/abs/10.1021/acs.est.8b05209
8. https://pubmed.ncbi.nlm.nih.gov/27510863/
9. https://www.nature.com/articles/s41579-022-00767-0
10. https://cmungall.github.io/mixs-source/
11. https://earthmicrobiome.ucsd.edu/protocols-and-standards/metadata-guide/
12. https://www.tandfonline.com/doi/full/10.1080/00380768.2025.2498470
13. https://www.mdpi.com/2227-9717/10/12/2531
14. https://www.sciencedirect.com/science/article/abs/pii/S0048969720334185
15. https://www.boffinaccess.com/journal-water-technology-treatment-methods/prevalence-of-legionella-2-124/JWT-2-124.pdf
16. https://www.nature.com/articles/nrmicro.2016.94
17. http://purl.obolibrary.org/obo/ENVO_00002034
18. https://www.ebi.ac.uk/ols4/ontologies/envo
19. https://doi.org/10.1186/2041-1480-4-43
20. https://agrovoc.fao.org/browse/agrovoc/es/page/c_43e1595d?clang=fi