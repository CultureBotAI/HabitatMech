---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T02:24:49.371490'
end_time: '2026-08-18T02:33:16.849555'
duration_seconds: 507.48
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Rock core/Sediment
  habitat_identifier: habitatmech:GOLD.20fb5b0162
  habitat_category: TERRESTRIAL
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Environmental > Terrestrial > Deep subsurface > Aquifer > Rock
    core/Sediment'
  assertions: '1'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. GOLD conflates
    rock core and sediment in one node, so neither term is honest as the identity.
    Pulled out of the class-level sweep, whose note wrongly claimed no term matched.
    Label: ''Rock core/Sediment''. (source concept habitatmech:GOLD.20fb5b0162)'
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
  web_search_requests: 11
  num_turns: 33
  total_cost_usd: 2.992844
  session_id: 8fecd2a4-0a9f-4edc-ae27-909fc6b64d07
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 21
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Rock core/Sediment
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.20fb5b0162
- **Category:** TERRESTRIAL
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Environmental > Terrestrial > Deep subsurface > Aquifer > Rock core/Sediment
- **Upstream assertion volume:** 1
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. GOLD conflates rock core and sediment in one node, so neither term is honest as the identity. Pulled out of the class-level sweep, whose note wrongly claimed no term matched. Label: 'Rock core/Sediment'. (source concept habitatmech:GOLD.20fb5b0162)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Rock core/Sediment** as a microbial habitat, with citations.

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

# Rock core/Sediment (aquifer) — `habitatmech:GOLD.20fb5b0162`

> **Proposed definition:** An environmental material which constitutes the groundwater-saturated solid matrix of an aquifer, being consolidated rock, unconsolidated sediment, or a mixture of both.

If a curator wants a single-material term instead, that is two terms (*aquifer rock* and *aquifer sediment*), not one — and neither alone matches what GOLD attests. The union is deliberate; see §1 and §6.

---

## 1. What the concept denotes

**The reading the data means.** The source path is `Environmental > Terrestrial > Deep subsurface > Aquifer > Rock core/Sediment` — GOLD's *specific ecosystem* level under the *ecosystem subtype* "Aquifer". GOLD's five-level classification places the specific-ecosystem term as a refinement of its parent, so this node names **the solid phase of an aquifer**, as opposed to the aquifer's water ([Mukherjee et al. 2023, *NAR* 51:D957–D963](https://academic.oup.com/nar/article/51/D1/D957/6786204), doi:10.1093/nar/gkac974). That reading is confirmed by the sibling structure in `data/raw/gold_ecosystem_paths.tsv`: the fluid phase of the deep subsurface lives on the *Aquatic* branch (`Environmental > Aquatic > Deep subsurface > Groundwater`, with children *Porewater*, *Drilled well/Borehole*, *Spring*…), while this node sits on the *Terrestrial* branch. GOLD has split the aquifer into a solid habitat and a fluid habitat and put them on opposite branches.

**What a sample is.** A cylindrical section of rock or sediment recovered by drilling and coring into a water-bearing formation below the land surface, then subsampled — conventionally the core interior, after the periphery is discarded or flamed, because drilling fluid infiltrates the outside ([Kallmeyer 2017, *Contamination Control for Scientific Drilling Operations*, Adv. Appl. Microbiol.](https://pubmed.ncbi.nlm.nih.gov/28189155/); [Twing et al. 2025, *Front. Microbiol.* 16:1504241](https://doi.org/10.3389/fmicb.2025.1504241)).

**Boundary — what is inside:**
- consolidated aquifer rock (sandstone, carbonate, fractured basalt, fractured crystalline basement) recovered by coring;
- unconsolidated aquifer sediment (basin-fill, glacial, alluvial sand and gravel) recovered by coring;
- both saturated, i.e. below the water table, within a body that transmits water.

**Boundary — what is a neighbouring concept:**
- **Groundwater** (`ENVO:01001004`) — the fluid filling the same pore space. Distinct habitat, distinct community (§3).
- **Vadose-zone material** — above the water table; ENVO's *vadose zone* (`ENVO:00000328`) is explicitly the unsaturated interval separating land surface and phreatic zone. An unsaturated core is not aquifer matrix.
- **Sibling GOLD node `habitatmech:GOLD.3b04872853`** — `Environmental > Terrestrial > Deep subsurface > Rock core/Sediment`, the depth-4 node with 1,245 organism assertions. Same label, *no aquifer commitment*: it covers deep subsurface solids generally, saturated or not. This record (depth 5, 1 assertion) is the aquifer-restricted narrower concept. **These two records must not be merged, and their definitions must differ by exactly the aquifer clause.**
- **Marine sub-seafloor sediment** — GOLD keeps `Aquatic > Marine > Deep subsurface > Sediment` separate; `ENVO:00002113 deep marine sediment` is the wrong domain.
- **Borehole** (`ENVO:00002226`) — the constructed channel, not the material.

**Residual ambiguity worth recording:** "Rock core" names a *sample form* (a cylinder of recovered material), not a place. The definition above deliberately reads the concept as the *in situ* material, because a habitat term for the cylinder-as-artefact would be uninstantiable. This is an inference on my part, supported by the fact that GOLD's peer specific-ecosystem terms under Groundwater (*Porewater*, *Well sediment*, *Spring sediment*) are likewise material names.

## 2. Genus — the broader kind

**Recommended genus: `ENVO:00010483` environmental material** — "A material entity which other material entities in an environmental system are primarily or partially composed of" (ENVO, via [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00010483)). It is the nearest ENVO class that subsumes *both* rock and sediment: `ENVO:00001995 rock` sits under *solid environmental material* (`ENVO:01000814`) and `ENVO:00002007 sediment` under *particulate environmental material* (`ENVO:01000060`), and `ENVO:00010483` is the immediate parent of both branches (verified against the OLS4 hierarchicalParents endpoint, 2026-08-18).

`ENVO:01000814 solid environmental material` would be tighter, but ENVO annotates it as a *defined* class whose "subclasses will not be asserted, but filled by inference" — so a term request should not assert under it.

**Near-misses, and why each fails:**

| Term | Why it is not the identity |
|---|---|
| `ENVO:00002007` **sediment** | *Narrower* — excludes consolidated rock, which is half of what the node names. Also asserts a depositional origin: "formed as a result of the transport and deposition of particles by flowing liquid." A basalt or serpentinite core has no such origin. **Note:** the sibling record `rock_core_sediment__d94b06e9.yaml` currently carries `ENVO:00002007` in `parent_habitats`. Under this repo's rule that `parent_habitats` means *broader*, that is an over-claim — sediment is not broader than "rock or sediment" — and is worth filing as its own issue. |
| `ENVO:00001995` **rock** | *Narrower* in the other direction — excludes unconsolidated sediment, which is the dominant matrix of basin-fill, glacial and stream-valley aquifers ([USGS](https://www.usgs.gov/mission-areas/water-resources/science/unconsolidated-and-semiconsolidated-sand-and-gravel-aquifers)). |
| `ENVO:00012408` **aquifer** | Wrong kind, and broader. ENVO models it as a `solid layer` (`ENVO:01001275`) — a geological body, "an underground layer of water-bearing permeable rock or unconsolidated materials … from which groundwater can be usefully extracted". The concept here is the *material composing* that layer, which is a part-of relation, not an is-a. Correct disposition: `relation: xref`, **not** a parent. |
| `ENVO:01000942` **continental subsurface zone** / `ENVO:01001776` **subsurface zone of an astronomical body** | Regions/zones, not materials. Broader in setting but of a different category. |
| `ENVO:01000747` **regolith** | "A solid layer which is composed primarily of loose, heterogeneous, superficial material covering solid rock." Both a *layer* and *superficial* — it asserts near-surface position, which the deep-subsurface path contradicts. |
| `ENVO:01000751` **bedrock**, `ENVO:00002016` **sedimentary rock**, `ENVO:03600016` **saprolite** | Lithology-specific; each is narrower and asserts a formation history GOLD does not. |
| `ENVO:01001004` **groundwater** | The complementary phase — explicitly what this term is *not* (§5). |
| `ENVO:00000328` **vadose zone** | Explicitly unsaturated; the aquifer matrix is saturated. |

No ENVO term for "aquifer sediment", "aquifer rock", "subsurface sediment" or "core sample" exists — searched OLS4 for `subsurface sediment`, `aquifer sediment`, `core sample`, `unconsolidated`, and full label/synonym sweeps on `rock` and `subsurface` (2026-08-18). The only `core`-labelled classes are `ENVO:01000641 planetary core` and `ENVO:01001530 water ice core`, neither relevant. **The CONFIRM_UNGROUNDED decision is correct.**

## 3. Differentia — what distinguishes it

**(a) It is the solid, not the fluid, phase of an aquifer.** This is the primary differentia and it is biologically load-bearing, not merely a sampling distinction:

- Attachment preference explained the **largest share of community variance (18.5 %, R²=0.185, F=15.4)** in a carbonate aquifer — more than oxygen presence (16.7 %) — and **attached cells outnumber planktonic ones by at least three orders of magnitude** ([Sharma, Küsel, Wegner, Pérez-Carrascal & Taubert 2026, *Microbiome* 14:73](https://doi.org/10.1186/s40168-025-02325-1)).
- In a serpentinizing aquifer, **rock-core community composition was distinct from groundwater**, and source tracking showed groundwater is not a significant source of OTUs into the rock ([Twing et al. 2025, *Front. Microbiol.* 16:1504241](https://doi.org/10.3389/fmicb.2025.1504241)).
- Attached and suspended communities in the Mahomet aquifer separate clearly, with iron reducers far more abundant in the attached fraction (Flynn et al., Mahomet aquifer; summarised in the deep-subsurface literature above).
- Attached genomes are larger and more metabolically versatile (mean Proteobacteria genome 4.48 Mb attached vs. 1.80 Mb planktonic; Sharma et al. 2026).

**(b) It is saturated and within a water-transmitting body** — this is what separates it from the depth-4 sibling `Deep subsurface > Rock core/Sediment` and from vadose material.

**(c) Dominant material varies with aquifer type, and both consolidated and unconsolidated are in scope.** USGS classifies principal aquifers by matrix: unconsolidated sand and gravel; semiconsolidated sand; sandstone; carbonate rock; sandstone-and-carbonate; basaltic and other volcanic rock; igneous and metamorphic rock ([USGS Water Resources](https://www.usgs.gov/mission-areas/water-resources/science/unconsolidated-and-semiconsolidated-sand-and-gravel-aquifers), [carbonate-rock aquifers](https://www.usgs.gov/mission-areas/water-resources/science/carbonate-rock-aquifers)).

**(d) Characteristic physicochemistry (observable/measurable):**
- Pore space ranges "from pore spaces smaller than the size of a microbial cell to larger fractures and faults"; sedimentary rocks are more hospitable than igneous or metamorphic ([Beaver & Neufeld 2024, *ISME J* 18:wrae091](https://doi.org/10.1093/ismejo/wrae091)).
- Oligotrophic and typically anoxic below shallow depth; H₂, CH₄ and CO₂ are the principal geogenic energy and carbon sources; **average generation times estimated in centuries** (Beaver & Neufeld 2024).
- Very low biomass — DNA yields from most rock core samples fell **below 0.25 ng DNA per g of core material** (Twing et al. 2025).
- Community structure is vertically stratified by geological formation and redox: bacterial Chao1 richness fell from >700 in the oxic Hanford formation to <50 in the deeper reduced Ringold strata across a 9–52 m borehole ([Lin, Kennedy, Fredrickson, Bjornstad & Konopka 2012, *Environ. Microbiol.* 14:414–425](https://pubmed.ncbi.nlm.nih.gov/22122741/), doi:10.1111/j.1462-2920.2011.02659.x).

**(e) Not a low-value habitat despite the 1-assertion count here.** Aquifer sediments plus groundwater at Rifle, CO yielded **2,540 draft-quality genomes including 47 new phylum-level lineages** ([Anantharaman et al. 2016, *Nat. Commun.* 7:13219](https://www.nature.com/articles/ncomms13219), doi:10.1038/ncomms13219, PMID 27774985).

**(f) Depth is *not* a reliable differentia.** GOLD's "Deep subsurface" branch does not define a depth cutoff, and the literature threshold varies from 8 m to >100 m; Beaver & Neufeld adopt ≥100 m, while most aquifers sit in the top 100 m (Beaver & Neufeld 2024). Do not put a metre value in the definition.

## 4. Sources

| Claim | Source |
|---|---|
| GOLD five-level classification; specific ecosystem refines subtype | Mukherjee S. et al. (2023) *Nucleic Acids Res.* 51(D1):D957–D963. doi:[10.1093/nar/gkac974](https://academic.oup.com/nar/article/51/D1/D957/6786204). PMID 36318257. Correction: *NAR* 52(6):3483, doi:10.1093/nar/gkae162 |
| ENVO term labels, definitions, parents (all verified 2026-08-18 via OLS4 API) | [EBI OLS4 — ENVO](https://www.ebi.ac.uk/ols4/ontologies/envo) |
| Aquifer = water-bearing permeable rock **or unconsolidated materials** | ENVO:00012408; AGROVOC ("freshwater-bearing stratum of permeable rock, sand or gravel"); [USGS Aquifers and Groundwater](https://www.usgs.gov/special-topics/water-science-school/science/aquifers-and-groundwater) |
| Aquifer matrix types (unconsolidated → crystalline) | [USGS, Unconsolidated and semiconsolidated sand and gravel aquifers](https://www.usgs.gov/mission-areas/water-resources/science/unconsolidated-and-semiconsolidated-sand-and-gravel-aquifers); [USGS, Carbonate-rock aquifers](https://www.usgs.gov/mission-areas/water-resources/science/carbonate-rock-aquifers) |
| Attached ≫ planktonic; attachment is the top variance driver; genome-size contrast | Sharma A., Küsel K., Wegner C.-E., Pérez-Carrascal O.M., Taubert M. (2026) *Microbiome* 14:73. doi:[10.1186/s40168-025-02325-1](https://doi.org/10.1186/s40168-025-02325-1). [PMC12930757](https://pmc.ncbi.nlm.nih.gov/articles/PMC12930757/) |
| Rock core community ≠ groundwater; coring depths 31/45 m; DNA <0.25 ng g⁻¹ | Twing K.I., Brazelton W.J., McCollom T.M. et al. (2025) *Front. Microbiol.* 16:1504241. doi:[10.3389/fmicb.2025.1504241](https://doi.org/10.3389/fmicb.2025.1504241). [PMC11926711](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11926711/) |
| Deep terrestrial subsurface: depth thresholds, rock-matrix vs groundwater habitat, oligotrophy/anoxia, century generation times | Beaver R.C. & Neufeld J.D. (2024) *ISME J* 18(1):wrae091. doi:[10.1093/ismejo/wrae091](https://academic.oup.com/ismej/article/18/1/wrae091/7680289) |
| Vertical stratification by formation and redox; richness decline with depth | Lin X., Kennedy D.W., Fredrickson J.K., Bjornstad B.N., Konopka A. (2012) *Environ. Microbiol.* 14(2):414–425. doi:10.1111/j.1462-2920.2011.02659.x. [PMID 22122741](https://pubmed.ncbi.nlm.nih.gov/22122741/). Companion: Lin et al. (2012) *Appl. Environ. Microbiol.* 78:759–767, [PMC3264105](https://pmc.ncbi.nlm.nih.gov/articles/PMC3264105/) |
| 2,540 genomes, 47 new phylum-level lineages from aquifer sediment + groundwater | Anantharaman K. et al. (2016) *Nat. Commun.* 7:13219. doi:[10.1038/ncomms13219](https://www.nature.com/articles/ncomms13219). PMID 27774985, [PMC5079060](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5079060/) |
| Groundwater cell densities 10²–10⁶ cells mL⁻¹; terrestrial subsurface holds a large share of Earth's microbial biomass | Griebler C. & Lueders T. (2009) *Freshwater Biology* 54(4):649–677. doi:[10.1111/j.1365-2427.2008.02013.x](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1365-2427.2008.02013.x) |
| Coring contamination is unavoidable and must be traced; core-interior subsampling | Kallmeyer J. (2017) *Contamination Control for Scientific Drilling Operations*, Adv. Appl. Microbiol. [PMID 28189155](https://pubmed.ncbi.nlm.nih.gov/28189155/); Kieft T.L. et al. (2007) "Drilling, Coring, and Sampling Subsurface Environments", *Manual of Environmental Microbiology*; [Frontiers, Trends and Future Challenges in Sampling the Deep Terrestrial Biosphere](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2014.00481/full) |
| "core" as a standardised **sample type**, distinct from an environment | MIxS `samp_type` (MIXS:0000998) in the hydrocarbon resources-cores package, [GSC MIxS](https://genomicsstandardsconsortium.github.io/mixs/0016015/); Tsesmetzis N. et al. (2016) *Environ. Microbiome* 11:18, doi:[10.1186/s40793-016-0203-5](https://link.springer.com/article/10.1186/s40793-016-0203-5) |

**Explicitly my inference, not stated by any source:** (i) that the GOLD node should be read as the in-situ material rather than the recovered cylinder (§1); (ii) that `ENVO:00010483` is the correct genus given ENVO's current material hierarchy (§2) — ENVO does not say this, it follows from the parentage I verified; (iii) that `ENVO:00002007` on the sibling record is an over-claim under this repo's `parent_habitats` semantics (§2).

## 5. Synonyms and what NOT to conflate

**Names in real use** (for the concept, not necessarily as ontology synonyms):
- aquifer sediment; aquifer matrix; aquifer solids
- subsurface sediment; saturated-zone sediment
- rock-hosted subsurface habitat; rock-attached subsurface biosphere (Sharma et al. 2026)
- aquifer host rock; formation rock
- *sample-form names, distinct register:* rock core, sediment core, core sample, drill core, whole-round core, core interior

Suggested annotation: keep `Rock core/Sediment` as the label (it is GOLD's), add *aquifer sediment* and *aquifer rock* as related synonyms, and `rock core` as a **sample-form** synonym rather than an exact one.

**Do NOT conflate with:**
- **Groundwater** (`ENVO:01001004`) / GOLD `Aquatic > Deep subsurface > Groundwater` — different phase, different community, ≥3 orders of magnitude difference in cell counts (Sharma et al. 2026; Twing et al. 2025).
- **Porewater** — the fluid *in* the matrix; GOLD gives it its own node under Groundwater.
- **Borehole / well** (`ENVO:00002226`) — the constructed channel. Well biofilms and well sediment are their own GOLD nodes and are partly artefacts of well construction.
- **Drilling mud / drilling fluid** — the introduced contaminant the tracer work exists to exclude (Kallmeyer 2017).
- **Soil** (`ENVO:00001998`) — surface, unsaturated, biologically distinct.
- **Vadose-zone material** (`ENVO:00000328`) — unsaturated.
- **Deep marine sediment** (`ENVO:00002113`) / sub-seafloor cores — GOLD keeps these on the Aquatic-Marine branch.
- **The depth-4 GOLD sibling `habitatmech:GOLD.3b04872853`** — identical label, broader concept, 1,245 assertions.
- **Oil reservoir** (`ENVO:00002185`) and shale/fracking nodes — hydrocarbon-bearing formations, separate GOLD subtypes with their own MIxS package.

## 6. Should this be a term at all?

**Yes — keep it, as UNGROUNDED with its own minted identity.** It is a place-and-material where microorganisms live, not a process, quality, disease or taxon. The evidence that it is a genuine habitat rather than a mere sampling convenience is direct: its community is reproducibly distinct from the groundwater in the same formation, and attachment is the single strongest structuring variable measured (Sharma et al. 2026; Twing et al. 2025; Lin et al. 2012).

Two honest caveats to record on the term, both of which argue for keeping HabitatMech's own identifier rather than grounding:

1. **The label is written in sampling terms.** "Rock core" is a MIxS `samp_type` value, not an environment (Tsesmetzis et al. 2016; [GSC MIxS](https://genomicsstandardsconsortium.github.io/mixs/0016015/)). The definition above deliberately reads through it to the material. A curator who disagrees with that reading would have to call the node a sampling artefact — but that would leave GOLD with no term at all for the solid phase of an aquifer, which the literature clearly treats as a habitat.
2. **The node conflates two materials.** The original curator's note is right that neither `rock` nor `sediment` is honest as the identity. The proposed definition handles this by naming the union explicitly and giving the aquifer-matrix role as the unifying differentia — that role is what both materials share and is what the sampling actually targets. This is why the genus has to be as high as `ENVO:00010483`; anything lower picks a side.

**Recommended dispositions for the record:**
- `grounding_status: UNGROUNDED` — unchanged, correct.
- `ENVO:00012408` *aquifer* → `relation: xref` (part-of, not is-a; do not put it in `parent_habitats`).
- Keep `habitatmech:GOLD.193fc3b328` (GOLD *Aquifer*) as the parent — that is the genuine broader concept in this hierarchy.
- Do **not** add `ENVO:00002007` as a parent here, and consider filing an issue to remove it from the depth-4 sibling for the same reason.
- Term-request candidate for ENVO: an *aquifer rock or sediment* / *aquifer matrix* material class under `ENVO:00010483`, with `ENVO:00012408` as a `part of` axiom. This would also give the depth-4 sibling a proper parent.

## Citations

1. https://academic.oup.com/nar/article/51/D1/D957/6786204
2. https://pubmed.ncbi.nlm.nih.gov/28189155/
3. https://doi.org/10.3389/fmicb.2025.1504241
4. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00010483
5. https://www.usgs.gov/mission-areas/water-resources/science/unconsolidated-and-semiconsolidated-sand-and-gravel-aquifers
6. https://doi.org/10.1186/s40168-025-02325-1
7. https://www.usgs.gov/mission-areas/water-resources/science/carbonate-rock-aquifers
8. https://doi.org/10.1093/ismejo/wrae091
9. https://pubmed.ncbi.nlm.nih.gov/22122741/
10. https://www.nature.com/articles/ncomms13219
11. https://www.ebi.ac.uk/ols4/ontologies/envo
12. https://www.usgs.gov/special-topics/water-science-school/science/aquifers-and-groundwater
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC12930757/
14. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11926711/
15. https://academic.oup.com/ismej/article/18/1/wrae091/7680289
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC3264105/
17. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5079060/
18. https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1365-2427.2008.02013.x
19. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2014.00481/full
20. https://genomicsstandardsconsortium.github.io/mixs/0016015/
21. https://link.springer.com/article/10.1186/s40793-016-0203-5