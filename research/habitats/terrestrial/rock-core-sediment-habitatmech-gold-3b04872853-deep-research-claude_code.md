---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:17:33.961268'
end_time: '2026-08-17T16:28:40.450260'
duration_seconds: 666.49
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Rock core/Sediment
  habitat_identifier: habitatmech:GOLD.3b04872853
  habitat_category: TERRESTRIAL
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Environmental > Terrestrial > Deep subsurface > Rock core/Sediment'
  assertions: '1245'
  parent_terms: ENVO:00002007
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Nearest
    broader term ENVO:00002007 ''sediment'' attached as a parent. Deep subsurface
    rock core and sediment sampled together. GOLD conflates two materials in one node,
    so no single term is honest; parented to sediment as the nearer of the two. (source
    concept habitatmech:GOLD.3b04872853)'
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
  - claude-opus-5
  web_search_requests: 14
  num_turns: 40
  total_cost_usd: 4.360956
  session_id: 93ac9e71-0b96-48d3-9dec-3b88e145ebe7
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 29
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Rock core/Sediment
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.3b04872853
- **Category:** TERRESTRIAL
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Environmental > Terrestrial > Deep subsurface > Rock core/Sediment
- **Upstream assertion volume:** 1245
- **Nearest broader term already on the record:** ENVO:00002007
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:00002007 'sediment' attached as a parent. Deep subsurface rock core and sediment sampled together. GOLD conflates two materials in one node, so no single term is honest; parented to sediment as the nearer of the two. (source concept habitatmech:GOLD.3b04872853)

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

# Rock core/Sediment (`habitatmech:GOLD.3b04872853`) — definition research

> **Proposed definition**
>
> **An environmental material which is the consolidated rock or unconsolidated sediment forming the solid matrix of the continental subsurface below the zone of soil formation, as opposed to the groundwater and other fluids held within it.**

Genus: `ENVO:00010483` *environmental material*. It is deliberately high in the hierarchy — see §2, where I show that `rock` and `sediment` have **no** lower common ancestor in ENVO. The disjunction ("rock or sediment") in the differentia is a symptom of a missing intermediate class; §2 names what that class would be.

---

## 1. What the concept denotes

### 1.1 The concept as GOLD uses it

The label sits at GOLD's **Ecosystem Subtype** level in the path `Environmental > Terrestrial > Deep subsurface > Rock core/Sediment`. GOLD's five-level scheme is Ecosystem → Ecosystem Category → Ecosystem Type → Ecosystem Subtype → Specific Ecosystem, where "the Ecosystem at the top describes the broader environment, whereas Specific Ecosystem at the bottom refers to a specific feature within that environment" ([Mukherjee et al., *Nucleic Acids Research* 51:D957–D963, Jan 2023, doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974); current release [GOLD v.10, *NAR* 53:D989–D997, Nov 2024, doi:10.1093/nar/gkae1000](https://doi.org/10.1093/nar/gkae1000); the classification originates with [Ivanova et al., *Environmental Microbiology* 12:1803–1805, 2010, doi:10.1111/j.1462-2920.2010.02274.x](https://doi.org/10.1111/j.1462-2920.2010.02274.x)).

**The slash is GOLD's "or".** This is verifiable inside `data/raw/gold_ecosystem_paths.tsv` without appeal to any external source: sibling GOLD nodes use the same construction for genuine disjunctions — `Drilled well/Borehole`, `Produced water/Flow back`, `Shale gas/oil reservoir`. So the label reads **"rock core *or* sediment"**, not "core of rock-sediment". The curator's existing note ("GOLD conflates two materials in one node") is correct.

**The concept is the solid phase, and its contrast class is the fluid phase.** GOLD splits the deep subsurface across two Ecosystem Categories, and the split is by phase, not by geography:

| GOLD path | Organism assertions |
|---|---|
| `Environmental > Terrestrial > Deep subsurface > Rock core/Sediment` | **1245** |
| `Environmental > Terrestrial > Deep subsurface > Rock` | 49 |
| `Environmental > Terrestrial > Deep subsurface > Aquifer` | 40 |
| `Environmental > Aquatic > Deep subsurface > Groundwater` (+ 15 child nodes) | 249 |
| `Environmental > Aquatic > Deep subsurface > Shale gas/oil reservoir > Produced water/Flow back` | 3 |

Every *water* subtype of the deep subsurface — groundwater, saline groundwater, mine water, spring, well water, produced water — is filed under `Aquatic`. Everything solid — rock, sediment, salt mine, cave, coal — is under `Terrestrial`. This is the strongest available evidence for the reading, and it is evidence internal to the source. *(This inference is mine; GOLD publishes no per-node scope note.)*

This one node carries **1245 of the 1447 organism assertions (86%)** under `Environmental > Terrestrial > Deep subsurface` in the vendored inventory — it is, in practice, GOLD's default bucket for continental deep-subsurface solid samples.

### 1.2 The boundary

**Inside the concept:**
- Lithified/consolidated rock at depth: basalt, granite and crystalline basement, sandstone, shale, limestone — recovered by rotary or wireline coring ([Dutta et al., *Scientific Reports* 8:17459, Nov 2018, doi:10.1038/s41598-018-35940-0](https://doi.org/10.1038/s41598-018-35940-0), which cored 500–1250 m of Deccan basalt into Archaean granitic basement to ~1400 m).
- Unconsolidated sediment at depth: deep vadose and saturated sands, silts and clays of sedimentary basins and coastal plains, recovered by wireline or split-spoon coring ([Russell, Phelps, Griffin & Sargent, *Ground Water Monitoring Review* 12:96–104, 1992, doi:10.1111/j.1745-6592.1992.tb00414.x](https://doi.org/10.1111/j.1745-6592.1992.tb00414.x); [Fredrickson & Balkwill, *Geomicrobiology Journal* 23:345–356, 2006, doi:10.1080/01490450600875571](https://doi.org/10.1080/01490450600875571)).
- Weathered rock transitional between the two (saprolite, weathered granite) — Dutta et al. explicitly cored a "transition (weathered granite)" horizon.

**Outside the concept (neighbours):**

| Neighbour | Where it belongs | Why it is not this |
|---|---|---|
| Groundwater, fracture fluid, produced water | `ENVO:01001004` groundwater; GOLD `Aquatic > Deep subsurface` | Fluid phase. Attached and planktonic communities differ by up to five orders of magnitude in density ([Casar et al., *Geobiology* 18:508–522, 2020, doi:10.1111/gbi.12391](https://doi.org/10.1111/gbi.12391)) — sampling one does not sample the other. |
| Soil | `ENVO:00001998` | Surface material within the zone of pedogenesis; the terrestrial subsurface is conventionally taken as below ~8 m *excluding soil* (§3.1). |
| Sub-seafloor / marine sediment | `ENVO:03000033`; GOLD `Aquatic > Marine > Deep subsurface > Sediment` | Different biogeographic realm; a global comparison found a distinct marine–terrestrial divide in subsurface microbiomes ([Ruff et al., *Science Advances* 10:eadq0645, Dec 2024, doi:10.1126/sciadv.adq0645](https://doi.org/10.1126/sciadv.adq0645)). **Note a GOLD defect:** `Environmental > Terrestrial > Deep subsurface > Sub-seafloor > Sediment core` (2 organisms) files a marine node under Terrestrial. Do not let that node's existence widen this definition. |
| Mine wall, tunnel rock face | GOLD `Terrestrial > Deep subsurface > Mine` | Rock exposed by excavation, atmospherically ventilated, not core. |
| Cave floor sediment, speleothem | GOLD `Terrestrial > Deep subsurface > Cave` | Air-exposed subterranean surfaces. |
| Aquifer | `ENVO:00012408` | A water-bearing *geologic unit* (a landform-like entity), not a material. |
| Borehole | `ENVO:00002226` ("A channel which is constructed by removing materials…") | The hole, not the material removed from it. |
| GOLD `Terrestrial > Deep subsurface > Rock` (49 organisms) | already `EXACT` → `ENVO:00001995` in this corpus (`data/habitats/terrestrial/rock.yaml`) | The corpus already keeps these distinct. Whatever is written here must not collapse into `rock`. |

### 1.3 The residual ambiguity you cannot dissolve

There are three readings and the source does not choose between them:

1. **Material reading** — "rock or sediment from the deep subsurface". This is the habitat reading and the only one a habitat ontology can express.
2. **Sample-form reading** — "*core*" names a cylindrical specimen produced by a drilling operation. Under this reading part of the label is a sampling artefact, not a habitat.
3. **Operational-bucket reading** — a grab-bag node for "solid deep-subsurface sample, lithology unspecified", used because the submitter did not distinguish.

I recommend adopting reading 1 and recording readings 2 and 3 in the note. The standards support this: MIxS `env_medium` instructs curators to "identify the material displaced by the entity at time of sampling… rather than what subsequently happened to that material during or after sampling", with the collection method going in `samp_collect_device` and `samp_mat_process` ([GSC MIxS `env_medium`](https://genomicsstandardsconsortium.github.io/mixs/0000014/); [ENVO wiki, *Using ENVO with MIxS*](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS)). "Core" is a `samp_collect_device` fact. Hence the proposed definition drops it and the note should say why.

---

## 2. Genus — and why nothing narrower works

### 2.1 The blocking fact

I traced the superclass chains in the vendored slice (`data/raw/ontology_subclass_edges.tsv`) and re-checked them against live ENVO via the EBI OLS4 API on 2026-08-17:

```
ENVO:00002007 sediment  → ENVO:01000060 particulate environmental material → ENVO:00010483 environmental material
ENVO:00001995 rock      → ENVO:01000814 solid environmental material       → ENVO:00010483 environmental material
```

`sediment` is **not** under `solid environmental material`. The two halves of this concept diverge immediately below `environmental material`, so **`ENVO:00010483` *environmental material* is their least common superclass**, and it is the only honest genus for a class that must cover both. (Verified: [OLS4 hierarchicalAncestors for ENVO:00002007](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_00002007/hierarchicalAncestors) returns `environmental material` and `particulate environmental material` only.)

### 2.2 The missing intermediate class

The genus is uncomfortably broad because ENVO has no class for **"geological/lithologic material"** — the union of rock, sediment, regolith and soil. Searching ENVO via OLS4 for *geological material*, *unconsolidated material* and *earth material* returns no such class. Saying so is more useful than padding the definition: if a term request is ever filed, the higher-value request is the intermediate class, not this leaf.

### 2.3 Near-misses, and why each fails

| Candidate | Definition (ENVO) | Why it fails |
|---|---|---|
| `ENVO:00002007` **sediment** *(current parent)* | "Particulate environmental material which is formed as a result of the transport and deposition of particles by flowing liquid." | **Narrower than the concept** — excludes the rock half entirely. As `parent_habitats` it is a genuine over-claim: the record is `rock ⊔ sediment`, and `rock ⊔ sediment ⊑ sediment` is false. It also asserts *deposition by flowing liquid*, which aeolian and glacial deposits in a core do not satisfy. Recommend demoting to `relation: xref`. |
| `ENVO:00001995` **rock** | "A rock is a naturally occurring solid aggregate of one or more minerals or mineraloids." | Narrower — excludes the sediment half. Also already claimed by the sibling GOLD node `Deep subsurface > Rock` in this corpus. |
| `ENVO:01000814` **solid environmental material** | "An environmental material which is in a solid state." | Does **not** subsume `sediment` in ENVO (§2.1). Tempting and wrong. |
| `ENVO:01000060` **particulate environmental material** | — | Subsumes sediment, not rock. |
| `ENVO:01000751` **bedrock** / `ENVO:03600016` **saprolite** | "A lithified mass of rock that lies under the loose softer material (regolith)…" / "Rock which is derived from bedrock through chemical weathering" | Narrower, and each asserts a specific lithologic history the 1245 assertions do not collectively support. |
| `ENVO:00012408` **aquifer** | "An underground layer of water-bearing permeable rock or unconsolidated materials…" | Asserts water-bearing and extractable — nothing in the source claims it. It is also a geologic unit, not a material. |
| `ENVO:01000942` **continental subsurface zone** | "A region which overlaps parts of one or more planetary structural layers which are located below a continental landmass." | Correct *setting*, wrong *category* — a zone/region, not a material. Good candidate for `relation: xref`, or as parent of the `Deep subsurface` node `habitatmech:GOLD.151ba43519` rather than of this record. |
| `ENVO:01001046` **planetary subsurface environment** / `ENVO:01001047` non-saline variant | "An environmental system which has its properties and dynamics determined by the subsurface zone of a planet." | An environmental *system*, not a material; and not restricted to continental. |
| `ENVO:00002226` **borehole** | "A channel which is constructed by removing materials from land or submerged beds." | The void, not the matrix. |
| `ENVO:01001530` **water ice core** | "An ice mass which has been drilled from an accumulation of snow and ice…" | Not a match, but a **precedent worth recording**: ENVO does model a drilled core as a material entity. If the curator wants to keep "core" in the identity, this is the pattern to point at. |

**No ENVO term for "deep subsurface sediment", "subsurface sediment", "rock core", "drill core" or "core sample" exists.** Confirmed by OLS4 keyword searches across ENVO (and across OBI/NCIT/CHMO/SWEET for "core sample" — only clinical core-biopsy terms and `water ice core` returned). A keyword search of the [ENVO issue tracker](https://github.com/EnvironmentOntology/envo/issues) on 2026-08-17 returned no open or closed request for such a term.

---

## 3. Differentia — what distinguishes it

### 3.1 Depth: below the surface-influenced zone (the load-bearing differentia)

The literature offers a range of thresholds; report the range, do not pick a number silently.

- **≥ 8 m, excluding soil** is the conventional lower bound for "terrestrial subsurface" ([Blamey et al., *Microbial Ecology* 87:126, Oct 2024, doi:10.1007/s00248-024-02434-8](https://doi.org/10.1007/s00248-024-02434-8), which states the terrestrial subsurface "is defined by depths greater than 8 m from the ground surface, excluding soil"; the same 8 m convention is noted in the ISME review below).
- **≥ 100 m** is the threshold most often used for *deep* terrestrial subsurface. [Beaver et al., "Microbial ecology of the deep terrestrial subsurface", *The ISME Journal* 18:wrae091, 2024, doi:10.1093/ismejo/wrae091](https://doi.org/10.1093/ismejo/wrae091) defines it as "rocks and groundwater at least 100 m below the surface of continents" and notes that "previous publications have described the terrestrial subsurface as deeper than 8 m."
- Some authors reserve the term for **> 1 km**.

**Recommendation:** the definition should say "below the zone of soil formation and surface hydrological influence" and let the note record the 8 m / 100 m / 1 km spread. A numeric threshold in the definition would assert precision GOLD's node does not carry.

### 3.2 Phase: solid matrix, not the fluid within it

The concept's most reliable discriminator against its nearest siblings. It matters biologically, not just operationally: at the Deep Mine Microbial Observatory attached cell densities on mineral surfaces exceeded planktonic counts by up to five orders of magnitude ([Casar et al. 2020, doi:10.1111/gbi.12391](https://doi.org/10.1111/gbi.12391)), and active biofilms have been imaged in poorly porous continental subsurface rock ([Escudero et al., *Scientific Reports* 8:1538, 2018, doi:10.1038/s41598-018-19903-z](https://doi.org/10.1038/s41598-018-19903-z)).

### 3.3 Realm: continental, not sub-seafloor

Subsurface microbiomes split along a marine–terrestrial divide ([Ruff et al. 2024, doi:10.1126/sciadv.adq0645](https://doi.org/10.1126/sciadv.adq0645)). The continental subsurface is estimated at **2–6 × 10²⁹ cells**; the same study revised total global prokaryotic biomass to ~23–31 Pg C ([Magnabosco et al., *Nature Geoscience* 11:707–717, 2018, doi:10.1038/s41561-018-0221-6](https://doi.org/10.1038/s41561-018-0221-6)). Subseafloor sediment holds ~2.9 × 10²⁹ cells ([Kallmeyer et al., *PNAS* 109:16213–16216, 2012, doi:10.1073/pnas.1203849109](https://doi.org/10.1073/pnas.1203849109)). For global-biomass framing see [Bar-On, Phillips & Milo, *PNAS* 115:6506–6511, 2018, doi:10.1073/pnas.1711842115](https://doi.org/10.1073/pnas.1711842115) and [Flemming & Wuertz, *Nat Rev Microbiol* 17:247–260, 2019, doi:10.1038/s41579-019-0158-9](https://doi.org/10.1038/s41579-019-0158-9).

### 3.4 Physicochemistry (observable, and citable)

From [Beaver et al. 2024 (ISME J), doi:10.1093/ismejo/wrae091](https://doi.org/10.1093/ismejo/wrae091) unless noted:

- **Anoxic** — "most subsurface microorganisms rely on non-oxygen electron acceptors and inorganic electron donors."
- **Energy-limited, slow** — "average generation time for microbial cells in terrestrial deep subsurface environments has been estimated to be centuries."
- **Thermal gradient ~25 °C km⁻¹**, bounding habitability to roughly the upper ~5 km.
- **Metabolisms** — hydrogen oxidation, methanogenesis, sulfate reduction, chemolithoautotrophic CO₂ fixation via the reductive acetyl-CoA pathway; deep systems are fuelled by H₂, CH₄ and short-chain hydrocarbons from water–rock interaction (serpentinization, radiolysis) rather than photosynthate.
- **Porosity is the habitat control** — "Sedimentary rocks are generally more porous than igneous and metamorphic rocks, providing more space for microorganisms to grow", while in igneous and metamorphic rock "the pore spaces … are usually too small for microbial cells" so "fractures provide the most likely habitats". See also [Templeton & Caro, "The Rock-Hosted Biosphere", *Annu. Rev. Earth Planet. Sci.* 51:493–519, 2023, doi:10.1146/annurev-earth-031920-081957](https://doi.org/10.1146/annurev-earth-031920-081957), on lithology, permeability and fluid mixing as controls.
- **Cell abundance, solid phase** — ~10⁴ cells g⁻¹ in deeply buried oceanic basalt; ~10⁵ cells g⁻¹ in crushed Deccan continental basalt cores ([Dutta et al. 2018, doi:10.1038/s41598-018-35940-0](https://doi.org/10.1038/s41598-018-35940-0)); sediments start far higher and decline log-linearly with depth ([Kallmeyer et al. 2012](https://doi.org/10.1073/pnas.1203849109)).
- **Lithology structures the community** — Magnabosco et al. found community composition correlated with sample lithology while total organic carbon and groundwater cell counts were not predictive. *This is the strongest scientific argument that lumping rock with sediment loses real signal, and it belongs in the note.*
- **Community composition** — [Soares et al., *Microbiology* 169:001172, Jan 2023, doi:10.1099/mic.0.001172](https://doi.org/10.1099/mic.0.001172) report Betaproteobacteria, Gammaproteobacteria and Firmicutes dominance across the terrestrial deep subsurface and note 12–20% of Earth's biomass has been attributed to it (vs ~1.8% deep subseafloor).

### 3.5 Access: drilling, with mandatory contamination control

The one respect in which "core" is doing real work. Because drilling fluid cannot be excluded, tracers are added and the core exterior is pared away; the habitat claim rests on the core *interior*. Perfluorocarbon tracers and ~0.5 µm fluorescent microspheres are the workhorses ([Kallmeyer, "Contamination Control for Scientific Drilling Operations", *Advances in Applied Microbiology* 98:61–91, 2017, doi:10.1016/bs.aambs.2016.09.003](https://doi.org/10.1016/bs.aambs.2016.09.003); [Friese et al., *Limnol. Oceanogr. Methods* 15:200–211, 2017](https://doi.org/10.1002/lom3.10159)). The DOE Subsurface Science Program protocol for *unconsolidated* deep sediment used microspheres, KBr, rhodamine and perfluorocarbons together, with on-site anaerobic processing ([Russell et al. 1992, doi:10.1111/j.1745-6592.1992.tb00414.x](https://doi.org/10.1111/j.1745-6592.1992.tb00414.x)).

**Recommendation:** keep this out of the definition (it is method, not habitat) and put it in the note as the reason "core" appears in the label at all.

---

## 4. Sources

Primary literature and reviews (all DOIs verified against Crossref on 2026-08-17):

| Claim supported | Citation |
|---|---|
| Definition of deep terrestrial subsurface; ≥100 m and ≥8 m thresholds; anoxia, generation times, thermal gradient, metabolisms, porosity/fracture habitats | Beaver CF et al. **Microbial ecology of the deep terrestrial subsurface.** *ISME J* 18:wrae091 (2024). [doi:10.1093/ismejo/wrae091](https://doi.org/10.1093/ismejo/wrae091) · [PMC11170664](https://pmc.ncbi.nlm.nih.gov/articles/PMC11170664/) |
| 8 m threshold, excluding soil; ICDP rock-core contamination procedures | Blamey N et al. **Subsurface microbial colonization at mineral-filled veins in 2-billion-year-old mafic rock, Bushveld Igneous Complex.** *Microb Ecol* 87:126 (Oct 2024). [doi:10.1007/s00248-024-02434-8](https://doi.org/10.1007/s00248-024-02434-8) |
| Continental subsurface 2–6 × 10²⁹ cells; community composition correlates with lithology | Magnabosco C et al. **The biomass and biodiversity of the continental subsurface.** *Nat Geosci* 11:707–717 (2018). [doi:10.1038/s41561-018-0221-6](https://doi.org/10.1038/s41561-018-0221-6) |
| Rock-hosted biosphere; lithology/permeability/fluid mixing as controls | Templeton AS & Caro TA. **The Rock-Hosted Biosphere.** *Annu Rev Earth Planet Sci* 51:493–519 (2023). [doi:10.1146/annurev-earth-031920-081957](https://doi.org/10.1146/annurev-earth-031920-081957) |
| Bacterial diversity, 12–20% of Earth biomass in terrestrial deep subsurface | Soares A et al. **A global perspective on bacterial diversity in the terrestrial deep subsurface.** *Microbiology* 169:001172 (Jan 2023). [doi:10.1099/mic.0.001172](https://doi.org/10.1099/mic.0.001172) |
| Marine–terrestrial subsurface divide | Ruff SE et al. **A global comparison of surface and subsurface microbiomes.** *Sci Adv* 10:eadq0645 (Dec 2024). [doi:10.1126/sciadv.adq0645](https://doi.org/10.1126/sciadv.adq0645) |
| Subseafloor sediment cell abundance | Kallmeyer J et al. *PNAS* 109:16213–16216 (2012). [doi:10.1073/pnas.1203849109](https://doi.org/10.1073/pnas.1203849109) |
| Terrestrial deep-subsurface rock cores, cell counts, TOC | Dutta A et al. *Sci Rep* 8:17459 (Nov 2018). [doi:10.1038/s41598-018-35940-0](https://doi.org/10.1038/s41598-018-35940-0) |
| Attached ≫ planktonic biomass on subsurface mineral surfaces | Casar CP et al. *Geobiology* 18:508–522 (2020). [doi:10.1111/gbi.12391](https://doi.org/10.1111/gbi.12391) |
| Biofilms in poorly porous continental rock | Escudero C et al. *Sci Rep* 8:1538 (2018). [doi:10.1038/s41598-018-19903-z](https://doi.org/10.1038/s41598-018-19903-z) |
| Deep sediment coring for microbiology; tracers; DOE Subsurface Science Program | Russell BF, Phelps TJ, Griffin WT, Sargent KA. *Ground Water Monit Rev* 12:96–104 (1992). [doi:10.1111/j.1745-6592.1992.tb00414.x](https://doi.org/10.1111/j.1745-6592.1992.tb00414.x) |
| Geomicrobiology of deep terrestrial sediments and rock | Fredrickson JK & Balkwill DL. *Geomicrobiol J* 23:345–356 (2006). [doi:10.1080/01490450600875571](https://doi.org/10.1080/01490450600875571) |
| Drill-core contamination control (PFT, microspheres, paring) | Kallmeyer J. *Adv Appl Microbiol* 98:61–91 (2017). [doi:10.1016/bs.aambs.2016.09.003](https://doi.org/10.1016/bs.aambs.2016.09.003) |
| Global biomass framing | Bar-On YM, Phillips R, Milo R. *PNAS* 115:6506–6511 (2018). [doi:10.1073/pnas.1711842115](https://doi.org/10.1073/pnas.1711842115) · Flemming H-C & Wuertz S. *Nat Rev Microbiol* 17:247–260 (2019). [doi:10.1038/s41579-019-0158-9](https://doi.org/10.1038/s41579-019-0158-9) |
| Anthropogenic modification of this habitat | Amundson KK et al. **Anthropogenic impacts on the terrestrial subsurface biosphere.** *Nat Rev Microbiol* 23:147–161 (Oct 2024). [doi:10.1038/s41579-024-01110-5](https://doi.org/10.1038/s41579-024-01110-5) |

Standards and vocabularies:

- GOLD ecosystem classification: [Mukherjee et al. *NAR* 51:D957 (2023), doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974); [v.10, *NAR* 53:D989 (2024), doi:10.1093/nar/gkae1000](https://doi.org/10.1093/nar/gkae1000); origin: [Ivanova et al. *Environ Microbiol* 12:1803 (2010)](https://doi.org/10.1111/j.1462-2920.2010.02274.x). Landing page [gold.jgi.doe.gov/ecosystem_classification](https://gold.jgi.doe.gov/ecosystem_classification) *(returned HTTP 403 to automated fetch on 2026-08-17; level semantics taken from the NAR papers)*.
- MIxS `env_medium` / `env_local_scale` / `env_broad_scale`: [GSC MIxS term pages](https://genomicsstandardsconsortium.github.io/mixs/0000014/); [ENVO wiki, *Using ENVO with MIxS*](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS).
- ENVO: [Buttigieg et al., *J Biomed Semant* 4:43 (2013), doi:10.1186/2041-1480-4-43](https://doi.org/10.1186/2041-1480-4-43); [Buttigieg et al., *J Biomed Semant* 7:57 (2016), doi:10.1186/s13326-016-0097-6](https://doi.org/10.1186/s13326-016-0097-6). Term definitions and hierarchy checked against `data/raw/ontology_terms.tsv` / `ontology_subclass_edges.tsv` and re-verified live via the [EBI OLS4 API](https://www.ebi.ac.uk/ols4/) on 2026-08-17.

**Explicitly flagged as my inference, not source-stated:**
1. That GOLD's Terrestrial/Aquatic split at the deep subsurface is a *solid vs. fluid* split (§1.1) — inferred from the node inventory, not from GOLD documentation.
2. That the slash means "or" (§1.1) — inferred from GOLD's own sibling node labels.
3. That `environmental material` is the correct genus (§2.1) — the ENVO hierarchy fact is verified; the choice to accept a broad genus rather than over-commit is a curatorial judgement.
4. That "core" should be excluded from the definition (§1.3) — supported by MIxS guidance on `env_medium`, but MIxS does not address this GOLD node.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept** (from the literature above):

- deep subsurface rock core · rock core · drill core · borehole core · core sample
- deep subsurface sediment · subsurface sediment core · deep sediment core
- deep continental subsurface rock · crystalline basement core · hard-rock core
- unconsolidated subsurface sediment · deep vadose sediment
- "the solid matrix of the deep continental biosphere"

Only the first two clusters should be recorded as `EXACT_SYNONYM`; the rest are narrower or descriptive.

**Commonly but wrongly treated as the same thing:**

| Not the same | Why |
|---|---|
| **Soil** (`ENVO:00001998`) | Surface material within the zone of pedogenesis; the 8 m convention exists precisely to exclude it. |
| **Groundwater / fracture fluid** (`ENVO:01001004`) | Different phase, different community, ~5 orders of magnitude different cell density (Casar et al. 2020). GOLD files it under a different Ecosystem Category. |
| **Aquifer** (`ENVO:00012408`) | A geologic unit, not a material; asserts water-bearing and extractable. |
| **Borehole / well** (`ENVO:00002226`, `ENVO:00000026`) | The engineered void. |
| **Marine / subseafloor sediment** (`ENVO:03000033`, `ENVO:02000059`) | Different realm (Ruff et al. 2024). GOLD's misfiled `Terrestrial > … > Sub-seafloor > Sediment core` node is a data defect, not a licence to include it. |
| **Sedimentary rock** (`ENVO:00002016`) | A lithology, orthogonal to depth; most sedimentary rock is not deep subsurface and much deep subsurface rock is igneous or metamorphic. |
| **Mine wall / cave sediment** | Air-exposed subterranean surfaces; GOLD keeps them as separate subtypes. |
| **"Core" as a specimen** | A `samp_collect_device` fact, not a habitat. |
| **`ENVO:01000641` planetary core** | Pure lexical trap on "core". |

---

## 6. Should it be a term at all?

**Yes — it is a habitat, and a heavily attested one.** It is not a process, a quality, a disease state, or a taxon. Microorganisms demonstrably live *in* deep subsurface rock and sediment — as attached biofilms on mineral surfaces and fracture walls, not merely as passengers in fluid ([Escudero et al. 2018](https://doi.org/10.1038/s41598-018-19903-z); [Casar et al. 2020](https://doi.org/10.1111/gbi.12391)). It carries 86% of GOLD's terrestrial deep-subsurface organism assertions. `NOT_APPLICABLE` would be wrong.

**But two things about the current record are worth changing, and one is a genuine over-claim:**

1. **`parent_habitats: ENVO:00002007` over-claims.** The record denotes `rock ⊔ sediment`; `sediment` is not broader than that. The existing note is candid about this ("parented to sediment as the nearer of the two"), but per `CLAUDE.md` — "`parent_habitats` means *broader*, so do not attach a term there unless it is" — this is the same shape of error as the ENVO *anthropogenic contamination feature* case in #99. **Recommendation:** move `ENVO:00002007` to `relation: xref`, add `ENVO:00001995` (rock) as a second `xref`, and set the parent to `ENVO:00010483` *environmental material* alongside the existing `habitatmech:GOLD.151ba43519`.
2. **The label's "core" component is a sampling artefact and should not enter the definition** (§1.3), with `ENVO:01001530` *water ice core* recorded in the note as the precedent that was considered and rejected.
3. **The disjunction is real and should be stated, not smoothed over.** Magnabosco et al. found community composition correlates with lithology — so this node genuinely mixes two habitats that differ microbiologically. The definition should say "rock or sediment" out loud rather than pretending to a single material.

**Two housekeeping findings for the curator:**

- `habitatmech:GOLD.20fb5b0162` (`Environmental > Terrestrial > Deep subsurface > Aquifer > Rock core/Sediment`, 1 organism) carries the **identical label** and the same conflation. Whatever definition is adopted here should apply to it verbatim, narrowed by "within an aquifer". Curating them separately will produce two divergent definitions of the same phrase.
- Two GOLD node ids (`gold.ecosystem:7699`, `:7700`) share this path, already noted on the record.

**If a term request is ever filed** (which, per the standing memory, needs explicit per-request permission), the higher-value request is **not** this leaf but the missing intermediate class in ENVO — a "geological material" / "lithologic material" parent of `rock`, `sediment`, `regolith` and `soil`. With that class in place, this concept becomes a clean one-sentence subclass rather than a disjunction, and roughly all of ENVO's rock/sediment cross-cutting queries improve at once.

## Citations

1. https://doi.org/10.1093/nar/gkac974
2. https://doi.org/10.1093/nar/gkae1000
3. https://doi.org/10.1111/j.1462-2920.2010.02274.x
4. https://doi.org/10.1038/s41598-018-35940-0
5. https://doi.org/10.1111/j.1745-6592.1992.tb00414.x
6. https://doi.org/10.1080/01490450600875571
7. https://doi.org/10.1111/gbi.12391
8. https://doi.org/10.1126/sciadv.adq0645
9. https://genomicsstandardsconsortium.github.io/mixs/0000014/
10. https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
11. https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_00002007/hierarchicalAncestors
12. https://github.com/EnvironmentOntology/envo/issues
13. https://doi.org/10.1007/s00248-024-02434-8
14. https://doi.org/10.1093/ismejo/wrae091
15. https://doi.org/10.1038/s41598-018-19903-z
16. https://doi.org/10.1038/s41561-018-0221-6
17. https://doi.org/10.1073/pnas.1203849109
18. https://doi.org/10.1073/pnas.1711842115
19. https://doi.org/10.1038/s41579-019-0158-9
20. https://doi.org/10.1146/annurev-earth-031920-081957
21. https://doi.org/10.1099/mic.0.001172
22. https://doi.org/10.1016/bs.aambs.2016.09.003
23. https://doi.org/10.1002/lom3.10159
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC11170664/
25. https://doi.org/10.1038/s41579-024-01110-5
26. https://gold.jgi.doe.gov/ecosystem_classification
27. https://doi.org/10.1186/2041-1480-4-43
28. https://doi.org/10.1186/s13326-016-0097-6
29. https://www.ebi.ac.uk/ols4/