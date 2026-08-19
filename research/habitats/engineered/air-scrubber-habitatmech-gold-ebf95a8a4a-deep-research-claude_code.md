---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T05:13:09.236961'
end_time: '2026-08-18T05:23:13.087437'
duration_seconds: 603.85
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Air scrubber
  habitat_identifier: habitatmech:GOLD.ebf95a8a4a
  habitat_category: ENGINEERED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Environmental > Air > Indoor Air > Air scrubber'
  assertions: '0'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. An air
    scrubber is a piece of equipment. GOLD files it under Air because the sample is
    scrubber air, but the habitat named by this leaf is the device, which belongs
    with the other built and managed environments. (source concept habitatmech:GOLD.ebf95a8a4a)'
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
  num_turns: 36
  total_cost_usd: 3.5413420000000007
  session_id: 5661089b-0552-401f-84ac-4cff1fe0abc3
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 27
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Air scrubber
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.ebf95a8a4a
- **Category:** ENGINEERED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Environmental > Air > Indoor Air > Air scrubber
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. An air scrubber is a piece of equipment. GOLD files it under Air because the sample is scrubber air, but the habitat named by this leaf is the device, which belongs with the other built and managed environments. (source concept habitatmech:GOLD.ebf95a8a4a)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Air scrubber** as a microbial habitat, with citations.

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

# Air scrubber — definition research for `habitatmech:GOLD.ebf95a8a4a`

## Proposed definition

> A manufactured product which removes gaseous and particulate contaminants from a ventilation exhaust or waste-gas stream by passing that stream through a packing wetted by a continuously recirculating aqueous liquid, and which thereby sustains a colonising microbial biofilm on the packing and a suspended community in the recirculation water.

**One sentence, but it is carrying two jobs**, and that is worth saying rather than hiding. The first clause defines the *device*; the trailing clause is what makes it a *habitat*. ENVO has no class between `manufactured product` and this concept — no "air pollution control device", no "waste gas treatment installation" — so the genus is forced up to `ENVO:00003074 manufactured product`, and the differentia has to do all the work. **The missing intermediate class is the real finding here** (§2). If HabitatMech would rather define the sampled *place* than the device, the alternative is:

> An anthropogenic environment which consists of the wetted packing, biofilm and recirculating scrubbing liquid within a device that removes contaminants from a ventilation exhaust air stream by gas–liquid contact.

I recommend the first. It matches ENVO's own drafting pattern for equipment (`hot tub`, `animal trap`, `air conditioning unit`, `biofilter` are all "A ⟨manufactured product / bioreactor⟩ which …"), and the second form invents an intermediate ("anthropogenic environment bounded by a device housing") that only `ENVO:01001405 laboratory environment` currently instantiates, and only for buildings.

---

## 1. What the concept denotes

### The reading the data means

**An exhaust-air scrubber fitted to the ventilation outlet of an animal house, composting facility or similar enclosed operation** — a packed vessel through which the building's exhaust air is forced while scrubbing liquid is sprayed counter-current over the packing. The habitat sampled is the **wetted packing surface, the biofilm growing on it, and the recirculating wash water in the sump**, together with the dust and ammonia load the air deposits there.

Four pieces of evidence converge on this reading, and I want to be explicit that this is an inference from the source structure, not a statement any single source makes:

1. **The child leaf.** GOLD does not stop at the scrubber: `Environmental > Air > Indoor Air > Air scrubber > Biofilm` (`gold.ecosystem:5806`, already in the corpus as `habitatmech:GOLD.7f436f8aff`). A dry HEPA cartridge does not get a "Biofilm" sub-leaf. A wetted packed bed does. This is the single strongest signal.
2. **The siblings.** Under the same `Indoor Air` parent GOLD lists **Cattle barn**, **Poultry farm**, **Composting facility**, **Poultry litter bioaerosol**, and **Dust** (verified in `data/raw/gold_ecosystem_paths.tsv`). GOLD's "Indoor Air" here is livestock- and waste-facility air, not office air. An "Air scrubber" alongside those is the abatement unit on their ventilation, which is exactly the technology reviewed by [Van der Heyden et al. 2015](https://doi.org/10.1016/j.biosystemseng.2015.04.002) and [Melse & Ogink 2005](https://doi.org/10.13031/2013.20094).
3. **The category the curator already assigned.** The record sits in `ENGINEERED` with the note that "the habitat named by this leaf is the device". That is consistent with (1) and (2).
4. **The term of art.** In Dutch/Flemish/German livestock regulation "air scrubber" (*luchtwasser*, *Abluftwäscher*) is the standard name for exactly this unit, and the literature subdivides it into **acid scrubbers**, **bioscrubbers** and **biotrickling filters** ([Melse & Ogink 2005](https://edepot.wur.nl/31455)).

### The boundary

| Inside the concept | Outside it |
|---|---|
| Packing material and its biofilm | The untreated barn air upstream (`Cattle barn`, `Poultry farm` leaves) |
| Recirculating scrubbing / wash water and the sump | The treated air discharged downstream (outdoor air) |
| Dust and mist captured on the wetted surfaces | Discharge water once bled off the unit (that is wastewater) |
| Both dry-dust and bio- stages of a multi-stage unit | A composting **biofilter** bed (see §5) |

### Where the label is genuinely ambiguous

The label alone supports at least four readings, and only the first is what the GOLD path means:

- **(A) Industrial / agricultural wet scrubber** — the reading above.
- **(B) Portable HEPA "air scrubber" / negative-air machine** used in mould and water-damage remediation and hospital construction containment. This is a *dry* filtration box; trade sources are clear that scrubber and negative-air machine are often the same chassis differing only in whether the exhaust is ducted out of containment ([Setra](https://www.setra.com/blog/whats-the-difference-between-an-air-scrubber-a-negative-air-machine), [Herc Rentals](https://blog.hercrentals.com/climate-control/whats-the-difference-between-an-air-scrubber-a-negative-air-machine/)). Its microbial habitat is the loaded filter medium, which is a **different** habitat — analogous to the HEPA-filter niche studied by [Wang et al. 2020, *Sci Rep* 10:6684](https://doi.org/10.1038/s41598-020-63543-1).
- **(C) CO₂/trace-contaminant scrubber in closed life support** (spacecraft, submarine) — a sorbent or amine bed, not a gas–liquid contactor.
- **(D) Residential HVAC-mounted "Air Scrubber" products** (e.g. the Aerus brand) — photocatalytic/ionising devices sold under the trademarked name.

**Do not silently fold B–D into this record.** If B ever needs a record it should be minted separately; the two share a name and nothing else physically.

---

## 2. Genus — the broader kind

**No ontology term in ENVO, UBERON, FOODON, BTO or PO names this concept.** I searched OLS4 across all ontologies for `scrubber`: the only hits are `NCBITaxon:2983206 gas scrubber metagenome` and GOLD's own path entries. ENVO has **zero** terms containing "scrubber" in label or synonym, and the ENVO issue tracker has **zero** issues mentioning it (GitHub search, `repo:EnvironmentOntology/envo scrubber`, total_count 0). **The UNGROUNDED status is correct.**

### Near-misses, and why each fails

| CURIE | Label | In the vendored slice? | Why it is not a match |
|---|---|---|---|
| `ENVO:00002152` | **biofilter** — "A bioreactor which captures and, through the biological processes maintained in the medium it contains, degrades pollutants." | Yes, `directly_referenced TRUE` | **Narrower and cross-cutting.** In the ag-engineering literature "air scrubbers **and** biofilters" are contrasted technologies, not genus/species ([Van der Heyden et al. 2015](https://doi.org/10.1016/j.biosystemseng.2015.04.002); VDI 3477 covers biofilters, VDI 3478 covers bioscrubbers/trickle-bed reactors — [VDI](https://www.vdi.de/en/home/vdi-standards/details/vdi-3478-blatt-1-biological-waste-gas-purification-bioscrubbers)). It also asserts *biological degradation of pollutants*, which an **acid scrubber** — a large fraction of the installed base — does not do; it strips NH₃ into sulphuric acid abiotically. Grounding here would publish a mechanism claim the sources do not support for the whole class. Use `relation: xref`. |
| `ENVO:00002123` | **bioreactor** — "maintaining conditions which are conducive to one or more metabolic activities of the organisms it contains" | Yes | Fits a **bioscrubber/biotrickling filter** and only that. An acid scrubber is operated at pH 2–4 explicitly to *suppress* biology. Asserting "conditions conducive to metabolism" over the whole class over-claims. |
| `ENVO:00003968` | **air filter** — "An air filter is a device that removes some substance from air." | Yes (`label_only FALSE`) | The **definition** is broad enough, but the **placement is wrong**: ENVO asserts `air filter is_a ENVO:00002874 air conditioning unit`, and that term is "capable of removing heat and controlling the humidity of the air within a site." An exhaust scrubber does neither. Parenting here inherits an HVAC over-claim — the same failure mode as *anthropogenic contamination feature* in #99. This ENVO placement looks like a defect worth reporting upstream regardless of what HabitatMech does. |
| `ENVO:00003074` | **manufactured product** | Yes | True but uninformative — it is the genus of the definition sentence, not a useful `parent_habitats` assertion. |
| `ENVO:01000676` | **contaminated air** | Yes | Names the *input stream*, not the device or the sampled surface. Would relocate the concept back to a portion of air, which is the framing curation already rejected. |

### Non-OBO vocabularies that *do* have it

- **AGROVOC `c_43e1595d` "scrubbers"** (alt. "gas scrubbers"), created 2022-09-22, last modified 2024-09-17. Definition, sourced by AGROVOC to EMIS/VITO: *"A scrubber is a waste gas treatment installation in which a gas stream is brought into intensive contact with a liquid, with the aim of allowing certain gaseous components to pass from the gas to the liquid. Scrubbers can be employed as an emission-limiting technique for many gaseous emissions."* Broader: `c_2631 equipment`. Narrower: `c_5c3aef22 bioscrubbers`. — <https://agrovoc.fao.org/browse/en/agrovoc/c_43e1595d>
  **This is the best available prior definition and I recommend the HabitatMech definition track its wording.**
- **NCBITaxon:2983206 "gas scrubber metagenome"**, rank species, lineage `unclassified entries; unclassified sequences; metagenomes; ecological metagenomes`. **Caveat, verified directly against NCBI E-utilities:** the *only* public BioSample carrying this organism is `SAMN43181758`, which is a **tomato soil** sample from Shouguang, China (`env_broad_scale: "tomato soil bacteria"`, `env_medium: "soil77"`, MIMARKS.survey.soil package). The taxon node is real; its usage is a single mis-annotation. Cite it as evidence that the environment is *recognised*, not that it is *sampled*.

---

## 3. Differentia — what distinguishes it

Ordered most to least diagnostic. Each is observable or measurable.

**a. Gas–liquid contact over a packing, with liquid recirculation.** This is the defining physical operation and separates it from every dry air-cleaning device. EPA's packed-bed/packed-tower fact sheet (EPA-452/F-03-015): the gas stream "is forced to follow a circuitous path through the packing material", liquid on the packing collects the contaminants and drains to the sump, a mist eliminator returns entrained droplets, and "the effluent from the column may be recycled into the system and used again" ([FRTR copy](https://frtr.gov/matrix/documents/Vapor-Treatment/Packed-Bed-Packed-Tower-Fact-Sheet.pdf)).

**b. Continuously wetted, nutrient-loaded inert surface.** VDI 3478 Part 2 describes biotrickling reactors as inert carriers (synthetic foam, lava, structured plastic packing) whose surface must allow biomass to bond, kept constantly covered with sprayed water, with nutrients dosed and excess sludge carried away ([EMIS/VITO BAT factsheet](https://emis.vito.be/en/bat/tools-overview/sheets/biotrickling-filter)). This is what makes the device a habitat rather than a duct.

**c. Extreme, actively controlled pH — bimodal across the class.** Acid scrubbers hold pH **2–4** with sulphuric acid dosing; biotrickling filters run near-neutral, measured at **pH 7.1–7.5** in two full-scale Flemish pig-house units ([Van der Heyden et al. 2019](https://doi.org/10.1111/1751-7915.13417), PMID 31106964; [Melse & Ogink 2005](https://edepot.wur.nl/31455)). This bimodality is the single most useful physicochemical discriminator and is why a definition must not assert an active biological community for the whole class.

**d. Nitrogen chemistry dominated by ammonia absorption and nitrification.** Ammonia absorption dominates the first stages; nitrification proceeds through later sections; recirculation liquid is bled off to keep N below inhibitory levels ([Van der Heyden et al. 2019](https://doi.org/10.1111/1751-7915.13417)). Nitrite accumulates where nitrite-oxidising bacteria are absent — the non-inoculated filter showed incomplete nitrification and high nitrite; the activated-sludge-inoculated one retained *Nitrospira*, achieved higher NH₃ removal and produced less N₂O.

**e. Very short air residence time and high volumetric loading.** Minimum empty-bed residence times of **0.4–1.1 s** in on-farm Dutch units ([Melse & Ogink 2005](https://doi.org/10.13031/2013.20094)).

**f. Selected, convergent, non-inoculum community.** Both full-scale filters converged on a similar community distinct from the activated-sludge inoculum; **Proteobacteria, Bacteroidetes and Actinobacteria together exceeded 80%**, with *Comamonadaceae* and *Xanthomonadaceae* as principal heterotrophs and a large denitrifier population ([Van der Heyden et al. 2019](https://doi.org/10.1111/1751-7915.13417)). In VOC-treating biotrickling filters, community composition tracked performance: the filter with 19.2% *Pseudomonas* removed 90% of isopropanol versus 79% at 8% ([PMID 24527643](https://pubmed.ncbi.nlm.nih.gov/24527643/)).

**g. It is a source as well as a sink of bioaerosols.** *Legionella* spp. were surveyed in the recirculating water of **36 farm bioscrubbers** in the southern/eastern Netherlands (34 pig, 2 poultry, three samples each), by culture and amoebal coculture, on the reasoning that scrubber water pH and temperature may favour *Legionella* growth and spraying nozzles make aerosol release probable ([Schets et al., *J Water Technol Treat Methods*, 2019-12-28](https://www.boffinaccess.com/journal-water-technology-treatment-methods/prevalence-of-legionella-2-124/JWT-2-124.pdf)). At wastewater plants, odour-control systems (biofiltration, activated carbon, chemical scrubbing) cut total airborne bacteria up to **25-fold** and non-tuberculous mycobacteria up to **13-fold**, yet *Legionella* spp. reached **up to 27% relative abundance in treated winter air** at 26–1140 GC/m³ ([Ouradou et al. 2023, *Sci Total Environ* 874:162419](https://doi.org/10.1016/j.scitotenv.2023.162419)).

**Differentia to avoid.** Do not put "removes ammonia and odour" in the definition as the essential property. Removal efficiency is highly variable and is a *performance* claim, not a defining one: acid scrubbers 40–100% NH₃ (mean 96%), biotrickling filters −8% to +100% (mean 70%), odour averaging only ~31% with large variation ([Melse & Ogink 2005](https://doi.org/10.13031/2013.20094)). A negative removal efficiency does not stop a unit being an air scrubber.

---

## 4. Sources

Primary literature, standards and reference vocabularies, with what each supports.

| Source | Supports |
|---|---|
| Van der Heyden C, De Mulder T, Volcke EIP, Demeyer P, Heyndrickx M, Rasschaert G. **Long-term microbial community dynamics at two full-scale biotrickling filters treating pig house exhaust air.** *Microbial Biotechnology* 12(4):775–786, 2019. [doi:10.1111/1751-7915.13417](https://doi.org/10.1111/1751-7915.13417) · PMID 31106964 · [PMC6559015](https://pmc.ncbi.nlm.nih.gov/articles/PMC6559015/) | pH 7.1–7.5; counter-current water flow; multi-stage (dust / bio / odour) design; inert packing; biofilm and washing water as the sampled matrices; >80% Proteobacteria+Bacteroidetes+Actinobacteria; *Comamonadaceae*, *Xanthomonadaceae*, *Nitrospira*; nitrite accumulation without NOB |
| Van der Heyden C, Demeyer P, Volcke EIP. **Mitigating emissions from pig and poultry housing facilities through air scrubbers and biofilters: state-of-the-art and perspectives.** *Biosystems Engineering* 134:74–93, 2015. [doi:10.1016/j.biosystemseng.2015.04.002](https://doi.org/10.1016/j.biosystemseng.2015.04.002) | Air scrubbers and biofilters as **distinct** technologies; packing size/material and air–liquid configuration as design variables; water flow, discharge and acid dosage as control variables |
| Melse RW, Ogink NWM. **Air scrubbing techniques for ammonia and odor reduction at livestock operations: review of on-farm research in the Netherlands.** *Transactions of the ASAE* 48(6):2303–2313, 2005. [doi:10.13031/2013.20094](https://doi.org/10.13031/2013.20094) · [full text](https://edepot.wur.nl/31455) | The acid-scrubber / biotrickling-filter split; pH 2–4 with H₂SO₄; NH₃ removal 40–100% (mean 96%) vs −8–100% (mean 70%); odour ~31%; EBRT 0.4–1.1 s |
| Schets FM, Melse RW, et al. **Prevalence of *Legionella* spp. in bioscrubbers at 36 livestock farms.** *J Water Technol Treat Methods*, 2019-12-28. [PDF](https://www.boffinaccess.com/journal-water-technology-treatment-methods/prevalence-of-legionella-2-124/JWT-2-124.pdf) | 36 farm bioscrubbers (34 pig, 2 poultry, NL); recirculating water as sampled matrix; pH/temperature favourable to *Legionella*; aerosol release via spray nozzles |
| Ouradou A, Veillette M, Bélanger Cayouette A, et al. **Effect of odor treatment systems on bioaerosol microbial concentration and diversity from wastewater treatment plants.** *Sci Total Environ* 874:162419, 2023. [doi:10.1016/j.scitotenv.2023.162419](https://doi.org/10.1016/j.scitotenv.2023.162419) · [open access](https://publications.polymtl.ca/53104/) | Chemical scrubbing / biofiltration / activated carbon as parallel odour-control technologies; up to 25× bacterial reduction; *Legionella* up to 27% of treated winter air; NTM up to 2500 GC/m³ reduced 13-fold; biofiltration as an "active process that adapts over time" |
| **Microbial community analysis in biotrickling filters treating isopropanol air emissions.** [PMID 24527643](https://pubmed.ncbi.nlm.nih.gov/24527643/) | Gammaproteobacteria enrichment; *Pseudomonas putida* persistence; community composition tracking removal efficiency (19.2% vs 8% *Pseudomonas* → 90% vs 79% removal) |
| **US EPA, Air Pollution Control Technology Fact Sheet: Packed-Bed/Packed-Tower Wet Scrubber**, EPA-452/F-03-015. [PDF](https://frtr.gov/matrix/documents/Vapor-Treatment/Packed-Bed-Packed-Tower-Fact-Sheet.pdf) · [EPA index](https://www.epa.gov/air-emissions-monitoring-knowledge-base/monitoring-control-technique-wet-scrubber-gaseous-control) | Authoritative physical description: packing, circuitous gas path, liquid drain to sump, mist eliminator, effluent recycle; clogging limits at high dust loading |
| **VDI 3478 Part 1** (bioscrubbers) and **Part 2:2008-04** (trickle-bed reactors); **VDI 3477** (biofilters). [VDI 3478-1](https://www.vdi.de/en/home/vdi-standards/details/vdi-3478-blatt-1-biological-waste-gas-purification-bioscrubbers) · [VDI 3477](https://www.vdi.de/en/home/vdi-standards/details/vdi-3477-biological-waste-gas-purification-biofilters) | The standards-level distinction between bioscrubber, trickle-bed reactor and biofilter; inert vs biological carrier; pH/nutrient/salt monitoring of circulating liquor |
| **EMIS/VITO BAT factsheets**, [biotrickling filter](https://emis.vito.be/en/bat/tools-overview/sheets/biotrickling-filter) and [gas scrubbing, general](https://emis.vito.be/en/bat/tools-overview/sheets/gas-scrubbing-general) | Working principle and packing materials; **the source AGROVOC cites for its own definition** |
| **AGROVOC `c_43e1595d` "scrubbers"** — <https://agrovoc.fao.org/browse/en/agrovoc/c_43e1595d> | The best existing controlled-vocabulary definition; `broader: equipment`, `narrower: bioscrubbers` |
| **NCBITaxon:2983206 "gas scrubber metagenome"** — <http://purl.obolibrary.org/obo/NCBITaxon_2983206> | Recognition of the environment as a metagenome source. **Verified caveat:** its sole BioSample `SAMN43181758` is a mislabelled tomato-soil sample |
| **JGI GOLD ecosystem classification** — Mukherjee S, et al. *Nucleic Acids Res* 51(D1):D957, 2023, [doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974); Ivanova N, et al., *Stand Genomic Sci*, "A call for standardized classification of metagenome projects"; [gold.jgi.doe.gov/ecosystem_classification](https://gold.jgi.doe.gov/ecosystem_classification) | Provenance of the five-level path and of `gold.ecosystem:5805` / `:5806` |
| Wang H, et al. **Bacterial community analysis of floor dust and HEPA filters in air purifiers used in office rooms in ILAS, Beijing.** *Sci Rep* 10:6684, 2020. [doi:10.1038/s41598-020-63543-1](https://doi.org/10.1038/s41598-020-63543-1) | The **contrast** case: the dry HEPA-filter niche of reading (B), explicitly framed as possibly "a new indoor ecological niche" |

**Explicitly flagged as my inference, not sourced:** (i) that the GOLD leaf means reading (A) rather than (B) — this is deduced from the `Biofilm` child, the livestock siblings and the ENGINEERED categorisation, not stated by GOLD; (ii) that `ENVO:00003968 air filter`'s placement under `air conditioning unit` is a defect; (iii) the inside/outside boundary table, which is a curation proposal.

**Gap I could not close:** I found no published metagenomic or ARG survey targeting livestock **air-scrubber wash water or packing** specifically. The adjacent literature covers barn air and dust ([Hein et al. 2024, *Front Vet Sci* 11:1362011](https://doi.org/10.3389/fvets.2024.1362011); [Bai et al. 2023, *Environ Int*](https://www.sciencedirect.com/science/article/pii/S0160412023000247)) and WWTP odour-control units ([Ouradou 2023](https://doi.org/10.1016/j.scitotenv.2023.162419)), not scrubber interiors as a resistome reservoir. The definition should not imply that evidence exists.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept** (recommend as `synonyms` / `exact_synonym` where the schema allows):

- air scrubber · air washer · gas scrubber · wet scrubber · packed-bed scrubber · packed-tower scrubber · scrubbing tower
- **bioscrubber** · **biotrickling filter** · trickle-bed reactor · *Rieselbettreaktor* · *Biowäscher* — narrower: the biologically-active subset
- **acid scrubber** · chemical scrubber · *chemische luchtwasser* — narrower: the acid-dosed subset
- **multi-stage scrubber** / combined air scrubber — a dust stage plus a chemical and/or bio stage in series
- *luchtwasser* (nl), *Abluftwäscher* (de) — the regulatory terms in the two countries where the technology is most deployed

**Commonly but wrongly treated as the same thing:**

| Not this | Why it differs |
|---|---|
| **Biofilter** (`ENVO:00002152`) — compost, wood-chip or bark bed | Biological support medium, no free-flowing recirculating liquid, much longer residence time. Standards separate them (VDI 3477 vs 3478); the ag literature contrasts "air scrubbers **and** biofilters". GOLD itself has a separate `Composting facility` leaf. |
| **HEPA air scrubber / negative-air machine** (reading B) | Dry filtration, portable, indoor, no liquid phase, no biofilm. Same English name, different device. |
| **Air filter** (`ENVO:00003968`) / **air conditioning unit** (`ENVO:00002874`) | Filtration and thermal/humidity conditioning; a scrubber does mass transfer into a liquid. |
| **Flue-gas desulphurisation unit** | Overlapping technology, but the FGD case is a combustion-stack context with a very different chemistry and temperature; do not merge. |
| **CO₂ scrubber** in closed life-support | Solid sorbent bed, no aqueous phase. |
| **Cooling tower** | Also a recirculating-water gas–liquid contactor and also a *Legionella* habitat — the closest true physical analogue — but its purpose is heat rejection, not contaminant capture. Related, not identical. |
| **Scrubber discharge water / scrubbing wastewater** | The bleed stream once it leaves the unit is a wastewater habitat, not this one. |
| **"scrubbers (brush)"** (AGROVOC `c_25684`) | Homonym; cleaning brushes. A real lexical-matching hazard. |

---

## 6. Should this be a term at all?

**Yes. Keep it, and keep it UNGROUNDED.** It is a place, not a process, quality, disease or taxon: a bounded engineered volume with a characteristic material (wetted inert packing), a characteristic physicochemistry (pH 2–4 or ~7.3; high ammonium/nitrite; continuous liquid film), and a selected, reproducible, well-characterised resident community. The existing `CONFIRM_UNGROUNDED` note is right on every point.

Three things a curator should weigh before writing the record:

1. **Upstream assertion volume is zero.** `gold.ecosystem:5805` carries 0 organisms and 0 genomes in `data/raw/gold_ecosystem_paths.tsv`, as does its `Biofilm` child. GOLD has *declared* the path but nothing is filed under it in our extract, and the one NCBI BioSample nominally from a gas scrubber is a mislabelled soil sample. So this is a well-motivated, well-documented habitat with **no attested samples behind it here**. That does not argue against defining it — the literature is ample and the concept is stable — but it should temper how much weight the record's definition claims.

2. **The device/interior split should be decided once, for this record and its `Biofilm` child together.** `habitatmech:GOLD.7f436f8aff` (`Air scrubber > Biofilm`) is already UNGROUNDED with the note "a biofilm is not air; it is a community on engineered equipment". If this record is defined as the *device*, the child reads naturally as "the biofilm within an air scrubber" and the pair is coherent. If this record is instead defined as the *interior environment*, the child becomes near-redundant with it. **Defining the device is the cleaner of the two**, and it is the option that keeps the parent/child distinction meaningful.

3. **Suggested `relation: xref` links** (none of these are broader, so none belongs in `parent_habitats`): `ENVO:00002152` biofilter, `ENVO:00003968` air filter, `NCBITaxon:2983206` gas scrubber metagenome, AGROVOC `c_43e1595d`. Per the `parent_habitats` rule and the #99 precedent, an xref records what the neighbouring vocabularies saw without HabitatMech asserting an is-a it cannot defend.

**Recommended follow-on action:** an ENVO new-term request. The gap is not one term but a small branch — an `air pollution control device` (or `waste gas treatment installation`, following AGROVOC's wording) genus under `manufactured product`, with `wet scrubber` / `bioscrubber` / `biotrickling filter` beneath it and `biofilter` re-parented alongside. The tracker has no existing issue for it, and the ENVO placement of `air filter` under `air conditioning unit` is worth raising in the same request.

**Sources:** [Van der Heyden 2019](https://doi.org/10.1111/1751-7915.13417) · [Van der Heyden 2015](https://doi.org/10.1016/j.biosystemseng.2015.04.002) · [Melse & Ogink 2005](https://doi.org/10.13031/2013.20094) ([full text](https://edepot.wur.nl/31455)) · [Schets et al. 2019](https://www.boffinaccess.com/journal-water-technology-treatment-methods/prevalence-of-legionella-2-124/JWT-2-124.pdf) · [Ouradou et al. 2023](https://doi.org/10.1016/j.scitotenv.2023.162419) · [PMID 24527643](https://pubmed.ncbi.nlm.nih.gov/24527643/) · [EPA-452/F-03-015](https://frtr.gov/matrix/documents/Vapor-Treatment/Packed-Bed-Packed-Tower-Fact-Sheet.pdf) · [EPA wet scrubber knowledge base](https://www.epa.gov/air-emissions-monitoring-knowledge-base/monitoring-control-technique-wet-scrubber-gaseous-control) · [VDI 3478-1](https://www.vdi.de/en/home/vdi-standards/details/vdi-3478-blatt-1-biological-waste-gas-purification-bioscrubbers) · [VDI 3477](https://www.vdi.de/en/home/vdi-standards/details/vdi-3477-biological-waste-gas-purification-biofilters) · [EMIS biotrickling filter](https://emis.vito.be/en/bat/tools-overview/sheets/biotrickling-filter) · [EMIS bioscrubber](https://emis.vito.be/en/bat/tools-overview/sheets/bioscrubber) · [AGROVOC scrubbers](https://agrovoc.fao.org/browse/en/agrovoc/c_43e1595d) · [GOLD ecosystem classification](https://gold.jgi.doe.gov/ecosystem_classification) · [GOLD v.9, NAR 2023](https://doi.org/10.1093/nar/gkac974) · [Wang et al. 2020, Sci Rep](https://doi.org/10.1038/s41598-020-63543-1) · [Hein et al. 2024, Front Vet Sci](https://doi.org/10.3389/fvets.2024.1362011) · [Bélanger Cayouette et al. 2022, Atmosphere](https://www.mdpi.com/2073-4433/13/10/1723) · [EnvironmentOntology/envo](https://github.com/EnvironmentOntology/envo)

## Citations

1. https://doi.org/10.1016/j.biosystemseng.2015.04.002
2. https://doi.org/10.13031/2013.20094
3. https://edepot.wur.nl/31455
4. https://www.setra.com/blog/whats-the-difference-between-an-air-scrubber-a-negative-air-machine
5. https://blog.hercrentals.com/climate-control/whats-the-difference-between-an-air-scrubber-a-negative-air-machine/
6. https://doi.org/10.1038/s41598-020-63543-1
7. https://www.vdi.de/en/home/vdi-standards/details/vdi-3478-blatt-1-biological-waste-gas-purification-bioscrubbers
8. https://agrovoc.fao.org/browse/en/agrovoc/c_43e1595d
9. https://frtr.gov/matrix/documents/Vapor-Treatment/Packed-Bed-Packed-Tower-Fact-Sheet.pdf
10. https://emis.vito.be/en/bat/tools-overview/sheets/biotrickling-filter
11. https://doi.org/10.1111/1751-7915.13417
12. https://pubmed.ncbi.nlm.nih.gov/24527643/
13. https://www.boffinaccess.com/journal-water-technology-treatment-methods/prevalence-of-legionella-2-124/JWT-2-124.pdf
14. https://doi.org/10.1016/j.scitotenv.2023.162419
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC6559015/
16. https://publications.polymtl.ca/53104/
17. https://www.epa.gov/air-emissions-monitoring-knowledge-base/monitoring-control-technique-wet-scrubber-gaseous-control
18. https://www.vdi.de/en/home/vdi-standards/details/vdi-3477-biological-waste-gas-purification-biofilters
19. https://emis.vito.be/en/bat/tools-overview/sheets/gas-scrubbing-general
20. http://purl.obolibrary.org/obo/NCBITaxon_2983206
21. https://doi.org/10.1093/nar/gkac974
22. https://gold.jgi.doe.gov/ecosystem_classification
23. https://doi.org/10.3389/fvets.2024.1362011
24. https://www.sciencedirect.com/science/article/pii/S0160412023000247
25. https://emis.vito.be/en/bat/tools-overview/sheets/bioscrubber
26. https://www.mdpi.com/2073-4433/13/10/1723
27. https://github.com/EnvironmentOntology/envo