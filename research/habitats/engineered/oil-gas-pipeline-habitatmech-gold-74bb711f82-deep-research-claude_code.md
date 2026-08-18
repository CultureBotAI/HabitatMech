---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T02:40:49.797406'
end_time: '2026-08-18T02:49:56.665374'
duration_seconds: 546.87
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Oil/Gas pipeline
  habitat_identifier: habitatmech:GOLD.74bb711f82
  habitat_category: ENGINEERED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Engineered > Built environment > Pipeline > Oil/Gas pipeline'
  assertions: '1'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. The habitat
    is the pipeline interior; the proposal offered ENVO:00002985 oil, the substance.
    No pipeline term in the slice. ENVO term request. Path: Engineered > Built environment
    > Pipeline > Oil/Gas pipeline (source concept habitatmech:GOLD.74bb711f82)'
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
  num_turns: 30
  total_cost_usd: 3.112294
  session_id: 592d2419-53eb-41c6-9e4d-929327a83b78
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 23
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Oil/Gas pipeline
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.74bb711f82
- **Category:** ENGINEERED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Engineered > Built environment > Pipeline > Oil/Gas pipeline
- **Upstream assertion volume:** 1
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. The habitat is the pipeline interior; the proposal offered ENVO:00002985 oil, the substance. No pipeline term in the slice. ENVO term request. Path: Engineered > Built environment > Pipeline > Oil/Gas pipeline (source concept habitatmech:GOLD.74bb711f82)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Oil/Gas pipeline** as a microbial habitat, with citations.

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

# Oil/Gas pipeline (`habitatmech:GOLD.74bb711f82`) — definition research

> **A pipeline network which is used to transport crude oil, natural gas, or the multiphase fluids produced with them, from wells or processing facilities to other such facilities or to consumers.**

---

## ⚠️ Finding that changes the disposition before anything else

**The recorded curation note is factually wrong about the slice.** It says "No pipeline term in the slice." The vendored slice at `data/raw/ontology_terms.tsv` contains three, none deprecated, none `label_only`:

| CURIE | Label | Definition (ENVO's own) |
|---|---|---|
| `ENVO:03600014` | pipeline network | "A human construction which is used to transport a material which is primarily composed of liquid or gas through a system of pipes." |
| `ENVO:03600012` | oil pipeline network | "A pipeline network which is used to transport oil to consumers." (exact synonym: *oil pipeline*) |
| `ENVO:03600003` | drinking water pipeline network | "A pipeline network which is used to transport drinking water to consumers." |

Subclass edges in `data/raw/ontology_subclass_edges.tsv`: `ENVO:03600003 ⊑ ENVO:03600014`, `ENVO:03600012 ⊑ ENVO:03600014`, `ENVO:03600014 ⊑ ENVO:00000070` (*human construction*).

I confirmed the same three, and the absence of any gas-pipeline term, against live ENVO via OLS4 ([`https://www.ebi.ac.uk/ols4/api/search?q=pipeline&ontology=envo`](https://www.ebi.ac.uk/ols4/ontologies/envo)). The only other ENVO hits for "pipeline" are incidental: `ENVO:00000075` bridge, `ENVO:01000968` water intake, `ENVO:02000144` natural gas processing plant, `ENVO:03501367` pneumatic conveyor — all mention pipelines in their definitions without being one.

The likely reason the sweep missed them: ENVO's rdfs:label is "pipeline **network**", so a label-match on "Pipeline" or "Oil/Gas pipeline" fails, while the exact synonym *oil pipeline* only reaches the oil half of the disjunction.

**The corpus already ground the sibling.** `data/habitats/engineered/drinking_water_pipeline_network.yaml` grounds GOLD's `Engineered > Built environment > Pipeline > Drinking water pipeline` to `ENVO:03600003` with `grounding_status: CLOSE`, reviewed 2026-08-16 under the #12 CLOSE-grounding review. `Oil/Gas pipeline` is the immediate sibling of that record under the same GOLD parent. Two sibling concepts from one GOLD parent, one grounded CLOSE and one `CONFIRM_UNGROUNDED` on the grounds that no pipeline term exists, is an internal inconsistency, not two different judgements.

Two consequential asymmetries remain, and they are what the term request is actually for:

1. **`ENVO:03600012` is narrower than the concept.** It covers oil only. GOLD's label is disjunctive — `Oil/Gas` — and natural gas pipelines are a materially different habitat from crude-oil lines (see §3). Grounding the whole concept to *oil pipeline network* would silently drop the gas half.
2. **`ENVO:03600012` and `ENVO:03600003` both assert "to consumers".** No oil or gas pipeline in the GOLD sense necessarily terminates at a consumer: gathering lines run wellhead → central collection point, and under 49 CFR 195.2 / 192.3 that is a distinct regulated class from transmission and distribution ([PHMSA, Gathering Pipelines FAQs](https://www.phmsa.dot.gov/faqs/gathering-pipelines-faqs); [PHMSA Fact Sheet: Gathering Pipelines](https://primis.phmsa.dot.gov/stakeholder-comms/factsheets/fsgatheringpipelines)). Most published pipeline microbiology is on gathering and production lines, i.e. exactly the segments ENVO's "to consumers" excludes. This is an ENVO defect worth raising alongside the request rather than inheriting.

**There is an open ENVO issue that this request belongs on.** [EnvironmentOntology/envo#1111, "Pattern for pipeline network terms"](https://github.com/EnvironmentOntology/envo/issues/1111), opened by kaiiam 2021-05-03, still open, labelled *thoughts*, states verbatim: "there is an opportunity to create a pattern for pipeline network terms where each terms is capable/linked to the transport of some material, e.g. `oil` or `water`. `natural gas` etc." A `natural gas pipeline network` sibling — or a `hydrocarbon pipeline network` parent over both — is the request ENVO has already scoped and not yet executed.

**Recommended disposition (curator's call):** `GROUND_AS_PARENT` to `ENVO:03600014` *pipeline network* — which is genuinely broader, genuinely a habitat, and free of the "to consumers" over-claim — with `ENVO:03600012` recorded as `relation: xref` and a term request filed on #1111. `CONFIRM_UNGROUNDED` with no parent at all, which is the current state, discards a correct broader term that is sitting in the slice.

---

## 1. What the concept denotes

**The reading the source path supports.** GOLD's path is `Engineered > Built environment > Pipeline > Oil/Gas pipeline` (`gold.ecosystem:8072`, `:8073`; 1 ORGANISM assertion). Its one sibling is `Drinking water pipeline`, which in turn has a child `Biofilm` (`gold.ecosystem:5701`). The classification axis under `Pipeline` is therefore **the commodity transported**, and `Oil/Gas pipeline` denotes the pipeline-and-contents system that conveys petroleum and natural gas — steel line pipe plus the fluids, deposits and biofilm inside it.

**Where the microbes actually are, and what a sample is.** The habitat is the **internal, water-wetted surface and the fluids and solids in contact with it**, not the steel as an object. Published sampling is of:

- **Pigging debris / pig returns** — solids and biofilm scraped from the internal wall by a cleaning pig. Bonifay et al. sampled pigging debris from runs #3 and #11 on two adjacent North Sea crude-oil production pipelines, into sterile N₂-filled bottles, frozen at −70 °C (*Front. Microbiol.* 8:99, 2017, [doi:10.3389/fmicb.2017.00099](https://doi.org/10.3389/fmicb.2017.00099)).
- **Sessile biofilm on coupons** exposed in the flowing line.
- **Pipeline-associated solids** upstream and downstream of a chemical injection point ([Lahme et al. / Voordouw group, *AEM*, PMC4729907](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4729907/)).
- **The aqueous phase carried in the line** — produced water, flowback water, condensed water.

The systematic review by Dutra et al. quantifies the sample mix across the field: 368 samples from 69 studies, comprising produced water (155), solid deposits including biofilms and pig residues (119), oil/water mixtures (36), injection water (33) and oil (25), drawn from injection wells, production wells, **pipelines**, valves, membranes, tanks, pumps and separators (*PeerJ* 11:e14642, 2023, [doi:10.7717/peerj.14642](https://doi.org/10.7717/peerj.14642)).

**Boundaries — what is inside and what is a neighbour.**

| Inside the concept | Adjacent concept, not this one |
|---|---|
| Interior wall, biofilm, under-deposit sludge, water condensate film | **External** surface of a buried line under disbonded coating — that habitat is soil |
| Gathering, flowline, transmission and distribution segments carrying oil or gas | The **reservoir** the fluid came from (`ENVO:00002185` oil reservoir) |
| Fluids *while in transit in the line* | The same fluid sampled at the wellhead or in a tank (`ENVO:00002194`, `ENVO:00002183`) |
| Pigging solids, dead-leg and low-point liquid holdup | Vessels inside a plant — separators, refinery units (`ENVO:03600078`) |

*ISO 13623:2017 defines the pipeline system as extending beyond line pipe to pump/compressor stations, block valve stations, metering, pigging facilities and cathodic protection, and covers lines "connecting wells, production plants, process plants, refineries and storage facilities" ([ISO 13623:2017](https://www.iso.org/standard/61251.html)). Whether HabitatMech's habitat should follow that engineering boundary or stop at the line pipe is a curator judgement; the microbiology literature generally treats pigging-accessible line pipe as the unit.*

**One genuine ambiguity, stated rather than resolved.** "Oil/Gas pipeline" can be read two ways:

- **(a) commodity reading** — a pipeline whose contents are oil or natural gas. Supported by the sibling `Drinking water pipeline`, which is also commodity-named.
- **(b) sector reading** — any pipeline in an oil-and-gas operation, which would additionally pull in **water injection lines and produced-water disposal lines**. This reading is common in the MIC literature, where "oil and gas pipelines" routinely includes water-handling lines — and those are among the most microbially active pipes in the field.

The commodity reading (a) is the better fit to the GOLD axis and is what I have written the definition to. This is my inference from the sibling structure, not something GOLD states. If a curator prefers to leave water-handling lines in, the definition needs "…or the water produced or injected with them", and that pushes the term further from anything ENVO currently has.

---

## 2. Genus

**`ENVO:03600014` *pipeline network*** — "A human construction which is used to transport a material which is primarily composed of liquid or gas through a system of pipes." Present in the vendored slice, not deprecated, `⊑ ENVO:00000070` human construction. This is the smallest well-established kind the concept falls under and it is the genus the definition above starts from.

**Near-misses, and why each fails:**

| Candidate | Why it is not a match |
|---|---|
| `ENVO:03600012` **oil pipeline network** | *Narrower* — covers only the oil half of "Oil/Gas". Also asserts "to consumers", which excludes gathering and transmission-to-plant segments. Good `xref`; over-claims as identity. |
| `ENVO:00002985` **oil** (the proposal recorded on the decision) | An environmental **material**, not a place. Correctly rejected in the existing note. Same for `ENVO:00002984` petroleum, `ENVO:00002983` fuel oil. |
| `ENVO:00002185` **oil reservoir** | The geological source formation, upstream of and physicochemically distinct from the line. Communities in pipelines are partly reservoir-derived but shaped by transport conditions (§3). |
| `ENVO:00002194` **oil field production water** | The transported material, not the conduit. A legitimate `xref` for the fluid phase. |
| `ENVO:00002183` **oil tank**, `ENVO:01000003` **oil well**, `ENVO:01001870` **gas well**, `ENVO:03600078` **oil refinery**, `ENVO:02000144` **natural gas processing plant** | Sibling infrastructure at the same or adjacent nodes of the production chain — not pipes. |
| `ENVO:01000864` **mouth of liquid discharge conduit** | An outfall feature; wrong branch and wrong scale. |
| `ENVO:00002060` **oil sludge** | The material class of pipeline deposits, and a defensible `xref` for pig-return solids. Not the habitat concept. |
| `ENVO:03600003` **drinking water pipeline network** | The sibling, not the concept. |
| **No term exists** for gas, natural gas, hydrocarbon, or oil-and-gas pipeline in ENVO. | Verified against the live ontology via OLS4 and against the vendored slice. |

---

## 3. Differentia

What separates this from its siblings under *pipeline network* — chiefly `drinking water pipeline network`, and from the reservoir it drains.

**Transported material and redox state.** Oil and gas lines carry **anoxic, hydrocarbon-bearing multiphase fluid**; drinking-water networks carry oxic, chlorinated or chloraminated potable water. This single difference inverts the community: pipeline microbiology is dominated by anaerobic sulfate reducers, fermenters and methanogens, whereas drinking-water biofilms are oligotrophic aerobes. Dutra et al. (2023, [doi:10.7717/peerj.14642](https://doi.org/10.7717/peerj.14642)) found *Marinobacter* the only genus common to all seven petroliferous regions surveyed, with SRB (*Desulfovibrio*, *Desulfotomaculum*), methanogens (*Methanobacterium*, *Methanosaeta*) and acid-producing bacteria dominant.

**Salinity.** Produced and flowback water is saline to hypersaline, and salinity is the primary community filter. In hydraulically fractured shale gas systems, *Halanaerobium* spp. become the dominant persisting taxon across geographically distinct plays; a 42-well Marcellus survey confirmed the genus's dominance and its potential for acid and sulfide production and biofilm formation (Lipus et al., *AEM* 83:e02659-16, 2017, [doi:10.1128/AEM.02659-16](https://doi.org/10.1128/AEM.02659-16); [Liang et al., *Front. Microbiol.* 7:988, 2016](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4916785/)).

**Temperature.** Field pipelines span mesophilic to thermophilic. Both North Sea production lines in Bonifay et al. ran at ~80 °C or above, and their communities included *Thermoanaerobacter* and methanococcal archaea.

**Sulfur cycling and souring.** The characteristic process is microbial sulfide generation — biogenic H₂S "souring" — and its control by nitrate or bisulfite injection, which itself restructures the community. Bisulfite addition increased *Desulfomicrobium* and *Desulfocapsa* and brought in sulfur-cycling Epsilonproteobacteria (*Sulfuricurvum*, *Sulfurovum*) downstream of the injection point ([*AEM*, PMC4729907](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4729907/)). In shales the sulfide comes from **thiosulfate reduction, not sulfate reduction** — a distinction with practical consequence, since standard wellhead tests target canonical SRB (Lipus et al. 2017).

**Corrosion as the defining functional signature.** Bonifay et al. (2017) contrasted two adjacent North Sea lines: the high-corrosion line was dominated by SRB (*Desulfonatronospira thiodismutans*), fermentative *Thermoanaerobacter*, and methanococcal archaea (21 % of reads in HC11), with minimal denitrification genes; the low-corrosion line was ~72 % Gammaproteobacteria, chiefly *Pseudomonas stutzeri*, with denitrification and aerobic hydrocarbon-degradation potential and <5 % SRB. Sulfate was 980 mg/L (LC) vs 121 mg/L (HC), oil:water 1:3 vs 2:5; both received nitrate-treated seawater injection. MIC is estimated at ~20 % of the total cost of metallic corrosion (Wang et al., *Materials* 17(20):4996, 2024-10-12, [doi:10.3390/ma17204996](https://doi.org/10.3390/ma17204996)).

**Gas lines are a distinct sub-habitat, and this is the strongest argument for not collapsing "Oil/Gas" into `ENVO:03600012`.** In a natural gas transmission line the aqueous phase is a **thin condensate film**, not bulk water. Wei, Xu, Sun & Cheng state it directly: internal MIC in gas pipelines occurs in water condensate rather than bulk solution, and this uniquely affects biofilm formation, sessile growth, local solution chemistry and corrosion-product accumulation — so much so that lab media designed for bulk-solution MIC do not reproduce it (*J. Nat. Gas Sci. Eng.* 102:104581, 2022, [doi:10.1016/j.jngse.2022.104581](https://doi.org/10.1016/j.jngse.2022.104581)). Habitable water in a nominally dry gas line is patchy, concentrated at **low points, river/road crossings, uphill toes and dead legs**; localized corrosion rates in such liquid-accumulating sections run up to 61.4 % higher than in sections without accumulation ([*Processes* 14(8):1320, doi:10.3390/pr14081320](https://doi.org/10.3390/pr14081320)). Direct-assessment practice for such lines is codified in NACE SP0206 (dry natural gas ICDA), with MIC field methods in NACE TM0194 and TM0212.

**Formation process.** Anthropogenic, engineered, and continuously managed — pigged, biocide-dosed, inhibitor-dosed, cathodically protected. Communities are therefore not free-running: the Montney/Kakwa field reported 93 MIC failures and instituted continuous cocodiamine biocide dosing at 50–200 ppm with a film-forming inhibitor ([AMPP Alberta 2026](https://content.ampp.org/alberta/proceedings-abstract/ALBERTA_FEB26/2026/1/107104)). *Inference: this managed-community character is an observable difference from natural hydrocarbon habitats such as oil seeps, and is worth a definition note but probably not a definition clause.*

**Sampling caveat the curator should know.** Pig-return solids integrate over kilometres of line and are strongly heterogeneous, so a "pipeline" sample is not point-localized. A dead-leg leak investigation explicitly criticized prior work for basing assessments on planktonic cells or post-pigging sludge "gathered over a long length of pipeline", as not reflective of conditions at the corrosion site ([*Eng. Fail. Anal.*, ScienceDirect S096483052200066X](https://www.sciencedirect.com/science/article/abs/pii/S096483052200066X)).

---

## 4. Sources

**Primary literature**
- Bonifay V, Wawrik B, Sunner J, et al. (2017) Metabolomic and metagenomic analysis of two crude oil production pipelines experiencing differential rates of corrosion. *Frontiers in Microbiology* 8:99. [doi:10.3389/fmicb.2017.00099](https://doi.org/10.3389/fmicb.2017.00099) — pigging-debris sampling protocol; HC vs LC community contrast; physicochemistry.
- Dutra J, Gomes R, Yupanqui García GJ, et al. (2023) Corrosion-influencing microorganisms in petroliferous regions on a global scale: systematic review, analysis, and scientific synthesis of 16S amplicon metagenomic studies. *PeerJ* 11:e14642. [doi:10.7717/peerj.14642](https://doi.org/10.7717/peerj.14642) — 69 studies, 368 samples, sample-type breakdown, dominant taxa.
- Wei B, Xu J, Sun C, Cheng YF (2022) Internal microbiologically influenced corrosion of natural gas pipelines: a critical review. *Journal of Natural Gas Science and Engineering* 102:104581. [doi:10.1016/j.jngse.2022.104581](https://doi.org/10.1016/j.jngse.2022.104581) — condensate-film habitat in gas lines; CER incident statistics 2008–2021 (568 of 1,554 incidents on gas lines).
- Lipus D, Vikram A, Ross D, et al. (2017) Predominance and metabolic potential of *Halanaerobium* spp. in produced water from hydraulically fractured Marcellus Shale wells. *Applied and Environmental Microbiology* 83:e02659-16. [doi:10.1128/AEM.02659-16](https://doi.org/10.1128/AEM.02659-16)
- Liang R, Davidova IA, Marks CR, et al. (2016) Metabolic capability of a predominant *Halanaerobium* sp. in hydraulically fractured gas wells and its implication in pipeline corrosion. *Frontiers in Microbiology* 7:988. [PMC4916785](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4916785/)
- Booker AE, Hoyt DW, Meulia T, et al. (2019) Deep-subsurface pressure stimulates metabolic plasticity in shale-colonizing *Halanaerobium* spp. *Applied and Environmental Microbiology* 85:e00018-19. [PMC6544827](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6544827/)
- Metagenomic analysis indicates Epsilonproteobacteria as a potential cause of microbial corrosion in pipelines injected with bisulfite. *Applied and Environmental Microbiology*. [PMC4729907](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4729907/)
- Wang D, et al. (2024) The microbiologically influenced corrosion and protection of pipelines: a detailed review. *Materials* 17(20):4996, 2024-10-12. [doi:10.3390/ma17204996](https://doi.org/10.3390/ma17204996)
- Study on corrosion in wet gas pipelines under the influence of gas composition and geometric configuration. *Processes* 14(8):1320. [doi:10.3390/pr14081320](https://doi.org/10.3390/pr14081320)
- Diagnosing microbiologically influenced corrosion at a crude oil pipeline facility leak site — a multiple lines of evidence approach. [ScienceDirect S096483052200066X](https://www.sciencedirect.com/science/article/abs/pii/S096483052200066X)

**Standards and vocabularies**
- ISO 13623:2017, *Petroleum and natural gas industries — Pipeline transportation systems*. [iso.org/standard/61251](https://www.iso.org/standard/61251.html) — system scope and boundary. (Revision in progress as ISO/AWI 13623, retitled "Oil and gas industries including lower carbon energy": [iso.org/standard/90035](https://www.iso.org/standard/90035.html).)
- 49 CFR §192.3, §192.8, §195.2 — US definitions of gathering, transmission and distribution lines. [PHMSA Gathering Pipelines FAQs](https://www.phmsa.dot.gov/faqs/gathering-pipelines-faqs); [PHMSA Fact Sheet](https://primis.phmsa.dot.gov/stakeholder-comms/factsheets/fsgatheringpipelines).
- NACE/AMPP SP0206 (dry gas ICDA); TM0194 (field monitoring of bacterial growth in oil and gas systems); TM0212 (detection and evaluation of MIC on internal pipeline surfaces).
- ENVO: [`ENVO:03600014`](http://purl.obolibrary.org/obo/ENVO_03600014), [`ENVO:03600012`](http://purl.obolibrary.org/obo/ENVO_03600012), [`ENVO:03600003`](http://purl.obolibrary.org/obo/ENVO_03600003); [OLS4 ENVO](https://www.ebi.ac.uk/ols4/ontologies/envo); [ENVO issue #1111](https://github.com/EnvironmentOntology/envo/issues/1111).
- Buttigieg PL, Morrison N, Smith B, Mungall CJ, Lewis SE (2013) The environment ontology: contextualising biological and biomedical entities. *J. Biomed. Semantics* 4:43. [doi:10.1186/2041-1480-4-43](https://doi.org/10.1186/2041-1480-4-43); Buttigieg PL, et al. (2016) The environment ontology in 2016. *J. Biomed. Semantics* 7:57. [PMC5035502](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/)

**Repo-internal evidence (not external citations):** `data/raw/ontology_terms.tsv`, `data/raw/ontology_subclass_edges.tsv`, `data/raw/gold_ecosystem_paths.tsv`, `data/habitats/engineered/{pipeline,drinking_water_pipeline_network,oil_gas_pipeline}.yaml`, `curation/decisions.tsv`.

**Explicitly my inference, not sourced:** the commodity-vs-sector disambiguation in §1; the claim that ENVO's "to consumers" clause is a defect rather than intent; the recommendation of `GROUND_AS_PARENT` over `CONFIRM_UNGROUNDED`; the diagnosis that the label-vs-synonym mismatch is why the class-level sweep missed `pipeline network`.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept:** oil and gas pipeline · oil/gas pipeline · hydrocarbon pipeline · petroleum pipeline · crude oil pipeline · natural gas pipeline · gas transmission pipeline · gathering line · flowline · production pipeline · trunk line · export line · sales gas line · pipeline network (ENVO's genus label; "oil pipeline" is an ENVO exact synonym of `ENVO:03600012`).

*Note that "gathering line", "transmission line" and "distribution line" are regulatory subclasses, not synonyms — see PHMSA above. A term request should list them as narrower, not exact.*

**Commonly but wrongly treated as the same thing:**

| Confused with | Why it is different |
|---|---|
| **Oil reservoir** (`ENVO:00002185`) / **formation fluid** (`ENVO:03600007`) | The subsurface source. Pipeline communities are partly reservoir-derived but reshaped by transport temperature, oxygen ingress, chemical dosing and pigging. Conflating them attributes engineered-system communities to a geological formation. |
| **Produced water / oil field production water** (`ENVO:00002194`) | The transported material. Frequently the *sample matrix*, so studies get filed under either — but material ≠ conduit. Correct as `xref`, wrong as identity. |
| **Oil sludge** (`ENVO:00002060`) | The material class of pig-return deposits, not the habitat. |
| **Oil tank / storage tank** (`ENVO:00002183`) | Static, stratified, different flow regime and different community; often studied in the same paper. |
| **Oil refinery** (`ENVO:03600078`) / **natural gas processing plant** (`ENVO:02000144`) | Downstream process facilities, not conduits. |
| **Drinking water pipeline network** (`ENVO:03600003`) | Same genus, opposite chemistry — oxic, disinfected, oligotrophic. The GOLD sibling; do not let the shared parent blur them. |
| **Sewer pipe / wastewater pipeline** | Also a pipeline network, but an anaerobic–aerobic alternating, high-substrate system with its own concrete/H₂S corrosion literature (Wang et al. 2024). |
| **Oil spill** (`ENVO:00002061`) / **oil seep** (`ENVO:00002063`) / **oil contaminated soil** (`ENVO:00002875`) | Consequences or natural analogues, external to the pipe. Pipeline **external** corrosion under disbonded coating belongs to soil, not here. |
| **Water injection and produced-water disposal lines** | Genuinely disputed — see the §1 ambiguity. Under the commodity reading they are a *different* pipeline type; under the sector reading they are inside. Do not silently include them. |

---

## 6. Should it be a term at all?

**Yes — this is a habitat, and an unusually clear one.** It is a physical, bounded, sampleable place with a resident, well-characterized, spatially structured microbial community (sessile biofilm on the internal wall plus under-deposit and planktonic fractions), a distinctive and measurable physicochemistry (anoxic, saline, hydrocarbon-bearing, 20–80+ °C), and a body of primary literature that treats it as such. It is not a process, a quality, a disease state, a taxon, or a sampling artefact.

Three qualifications for the curator:

1. **Low upstream volume.** `assertion_count: 1`, `assertion_unit: ORGANISM`. This concept is nowhere near the top of `just report`'s backlog on its own merits. Its value is that the grounding is cheap and it repairs a demonstrable inconsistency with an already-REVIEWED sibling.
2. **The parent record has the same problem.** `data/habitats/engineered/pipeline.yaml` (`habitatmech:GOLD.edec297c39`, `Engineered > Built environment > Pipeline`) is `UNGROUNDED` with only `mesh:D000076624` *Built Environment* as a parent — while `ENVO:03600014` *pipeline network* matches it directly and is already used as a parent on the drinking-water sibling. Its curation note records the same "no term in the vendored slice matched this label by any search route" conclusion, from the same label-vs-synonym miss. Whatever is decided here should be decided for the parent in the same pass; separate issues for the two are probably the right record.
3. **The gas half is the only real gap.** If ENVO adds `natural gas pipeline network` (or a `hydrocarbon pipeline network` parent) under issue #1111, this concept grounds cleanly and the minted identifier retires. That makes it a strong term-request candidate — the request is small, ENVO has already scoped the pattern, and the proposed text is one sentence in ENVO's own genus-differentia style:

> **natural gas pipeline network** — A pipeline network which is used to transport natural gas.
> **hydrocarbon pipeline network** — A pipeline network which is used to transport crude oil, natural gas, or the multiphase fluids produced with them.

If a single sentence for `Oil/Gas pipeline` feels strained, that is the disjunction talking: oil lines and gas lines really are two kinds under one commodity-family parent, and the missing intermediate class is `hydrocarbon pipeline network`. Requesting that parent plus a gas sibling is more useful than stretching one definition across both.

## Citations

1. https://www.ebi.ac.uk/ols4/api/search?q=pipeline&ontology=envo`
2. https://www.ebi.ac.uk/ols4/ontologies/envo
3. https://www.phmsa.dot.gov/faqs/gathering-pipelines-faqs
4. https://primis.phmsa.dot.gov/stakeholder-comms/factsheets/fsgatheringpipelines
5. https://github.com/EnvironmentOntology/envo/issues/1111
6. https://doi.org/10.3389/fmicb.2017.00099
7. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4729907/
8. https://doi.org/10.7717/peerj.14642
9. https://www.iso.org/standard/61251.html
10. https://doi.org/10.1128/AEM.02659-16
11. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4916785/
12. https://doi.org/10.3390/ma17204996
13. https://doi.org/10.1016/j.jngse.2022.104581
14. https://doi.org/10.3390/pr14081320
15. https://content.ampp.org/alberta/proceedings-abstract/ALBERTA_FEB26/2026/1/107104
16. https://www.sciencedirect.com/science/article/abs/pii/S096483052200066X
17. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6544827/
18. https://www.iso.org/standard/90035.html
19. http://purl.obolibrary.org/obo/ENVO_03600014
20. http://purl.obolibrary.org/obo/ENVO_03600012
21. http://purl.obolibrary.org/obo/ENVO_03600003
22. https://doi.org/10.1186/2041-1480-4-43
23. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/