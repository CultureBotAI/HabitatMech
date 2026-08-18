---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T15:50:34.085676'
end_time: '2026-08-17T16:00:30.935921'
duration_seconds: 596.85
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Environmental
  habitat_identifier: habitatmech:BACDIVE.0f1e92a02c
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Environmental'
  assertions: '18454'
  parent_terms: (none)
  xrefs: ENVO:01000951
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Nearest
    broader term ENVO:01000951 ''natural environment'' attached as a parent. Term-request
    re-check (#12), after ENVO:01001000 showed these claims were never machine-rechecked:
    ''Environmental'' is the counterpart of BacDive''s Host and Engineered bins, so
    ENVO:01000951 ''natural environment'' looks like the answer and is not. Its definition
    requires ''minimal to no anthropisation'', and this bin holds BacDive''s Paddy-Ricefield,
    Grove-Orchard and Herbaceous-plants-Grass,Crops, which are farmed. The term is
    narrower than the concept, so it is neither an identity nor a parent; kept as
    an xref (#99) to record the near-miss so the next curator does not re-derive it.
    Still a term request. (source concept habitatmech:BACDIVE.0f1e92a02c)'
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
  web_search_requests: 5
  num_turns: 41
  total_cost_usd: 3.324677
  session_id: 0900dc04-23fa-4e93-a1e3-3e918a494e52
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 23
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Environmental
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.0f1e92a02c
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Environmental
- **Upstream assertion volume:** 18454
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** ENVO:01000951

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:01000951 'natural environment' attached as a parent. Term-request re-check (#12), after ENVO:01001000 showed these claims were never machine-rechecked: 'Environmental' is the counterpart of BacDive's Host and Engineered bins, so ENVO:01000951 'natural environment' looks like the answer and is not. Its definition requires 'minimal to no anthropisation', and this bin holds BacDive's Paddy-Ricefield, Grove-Orchard and Herbaceous-plants-Grass,Crops, which are farmed. The term is narrower than the concept, so it is neither an identity nor a parent; kept as an xref (#99) to record the near-miss so the next curator does not re-derive it. Still a term request. (source concept habitatmech:BACDIVE.0f1e92a02c)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Environmental** as a microbial habitat, with citations.

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

# Definition research — `habitatmech:BACDIVE.0f1e92a02c` "Environmental"

> **A** *environmental system* (ENVO:01000254) **which** comprises a portion of the atmosphere, a body of water, or a land surface of an astronomical body together with the environmental materials composing it, and which is neither determined by a host organism nor a product of human construction or operation.

A shorter variant that keeps the same boundary but drops the material clause:

> An environmental system which is a portion of the atmosphere, hydrosphere, or land surface of an astronomical body and is neither host-determined nor anthropogenic.

Both sentences need two negative clauses, and that is diagnostic: **the missing intermediate class is a grouping term for "free-living / non-host-associated environment."** ENVO has positive classes for the two things this concept excludes — `ENVO:01001000` *environmental system determined by an organism* and `ENVO:01000313` *anthropogenic environment* — but no class for their complement other than `ENVO:01000951` *natural environment*, which adds an anthropisation restriction the source data does not honour. Saying that plainly is more useful to ENVO than a longer sentence.

---

## 0. Two corrections to the record before anything else

These affect the curation note already on the record, so they come first.

### 0.1 The evidence cited in the note is attached to the wrong source

The note on `habitatmech:BACDIVE.0f1e92a02c` says:

> "…this bin holds BacDive's Paddy-Ricefield, Grove-Orchard and Herbaceous-plants-Grass,Crops, which are farmed."

**That is not what BacDive's MISO says.** I parsed the live BacDive isolation-source browser (<https://bacdive.dsmz.de/isolation-sources>, fetched 2026-08-17) directly from its `data-parent-id` / `data-cat1-ids` attributes. In the current MISO:

- `#Paddy (Ricefield)`, `#Grove (Orchard)`, `#Field`, `#Meadow`, `#Garden`, `#Plantation`, `#Vineyard`, `#Greenhouse` are all **level‑3 tags of `#Engineered`** (via level‑2 `#Agriculture`), not of `#Environmental`.
- `#Herbaceous plants (Grass,Crops)` is a **level‑3 tag of `#Host`** (via level‑2 `#Plants`).

The level‑2 children of `#Environmental` are exactly five: **`#Air`, `#Aquatic`, `#Biofilm`, `#Microbial community`, `#Terrestrial`.**

The 44 level‑3 tags reachable under `#Environmental` are: `#Bacteriome, #Brackish, #Cave water, #Co-culture, #Coast, #Coral reef, #Core sample, #Decomposing algae, #Decomposing fungi, #Desert, #Dust, #Estuary, #Foam, #Forest, #Freshwater, #Geologic, #Glacier, #Grassland, #Groundwater, #Hydrothermal vent, #Ice, #Indoor Air, #Iron mat, #Lake (large), #Mangrove, #Marine, #Microbial mat, #Mud (Sludge), #Non-marine Saline and Alkaline, #Outdoor Air, #Permafrost, #Pond (small), #River (Creek), #Salt marsh, #Sandy, #Sediment, #Soil, #Spring, #Surface water, #Thermal spring, #Tidal flat, #Tundra, #Volcanic, #Wetland (Swamp)`.

**The conclusion still holds — reject `ENVO:01000951` — but on different evidence** (see §2.2). The farmed-land argument is valid for the *GOLD* record, `habitatmech:GOLD.c3fa7fc4c2`, whose own note already cites `Tree plantation` correctly. I confirmed in `data/raw/gold_ecosystem_paths.tsv` that GOLD's `Environmental` subtree contains `Environmental > Terrestrial > Agricultural field`, `… > Soil > Paddy field/soil`, `… > Soil > Orchard`, `… > Soil > Garden`, `… > Soil > City park`, `… > Soil > Contaminated > Pesticide`, and `Environmental > Air > Indoor Air > Poultry farm`.

### 0.2 There are two records for what is very likely one concept

`data/habitats/other/environmental.yaml` (`habitatmech:BACDIVE.0f1e92a02c`, 18,454 BacDive strains) and `data/habitats/other/environmental__a27d7186.yaml` (`habitatmech:GOLD.c3fa7fc4c2`, 1,285 GOLD organisms) are both `label: Environmental`, both `OTHER`, both `UNGROUNDED`, both xref `ENVO:01000951`, and both carry near-identical notes. They are the level‑1 bin of two different source vocabularies that partition sample provenance the same way (§1.2). This is exactly the case #116/#117 added machinery for ("let a decision say two novel concepts are the same"). Whatever definition is written should be written once and cover both, or the corpus publishes two terms for one concept.

### 0.3 The 18,454 is a subtree rollup, not level‑1-only annotation

`scripts/extract_source_inventory.py` counts one edge per (strain, isolation-source-node) pair from kg-microbe's BacDive transform. Since MISO assigns a strain a tag at *each* of the three levels, a strain tagged `#Environmental / #Terrestrial / #Soil` contributes to all three counts. Consistent with that, `Terrestrial` (13,182) + `Aquatic` (6,002) = 19,184 > `Environmental` (18,454), the excess being strains carrying both. **So 18,454 is "strains whose source was binned as Environmental at all," not "strains whose most specific annotation is Environmental."** This is my inference from the extractor code plus the arithmetic, not a statement any source makes — but it matters, because `just report` ranks the backlog by this number and it therefore overstates how much annotation this one term would actually carry on its own.

---

## 1. What the concept denotes

### 1.1 The reading the data means

`#Environmental` is **the level‑1 (category 1) class of BacDive's Microbial Isolation Source Ontology (MISO)** — a binning label for the provenance of a cultured strain, not a place anyone samples directly. It denotes, collectively, the settings a strain can be isolated from that are (a) *outside the body of any host organism* and (b) *not a human-built, human-operated, or laboratory construction*: the air, the water bodies, the land surfaces and subsurface, their sediments, soils and rocks, plus free-living microbial aggregations (biofilms, mats, communities) growing in those settings.

The MISO is described in the BacDive papers:

> "The isolation sources are classified according to the controlled vocabulary *Microbial Isolation Source Ontology* (MISO). This ontology is hierarchically ordered into three levels of tags (category 1–3). At the top level the eight major classes #Environmental, #Engineered, #Host, #Host body-site, #Host body-product, #Medical, #Condition and #Climate are listed."
> — Reimer LC, Vetcininova A, Sardà Carbasse J, Söhngen C, et al. *BacDive in 2019: bacterial phenotypic data for High-throughput biodiversity analysis.* **Nucleic Acids Research** 47(D1):D631–D636, 2019. doi:[10.1093/nar/gky879](https://doi.org/10.1093/nar/gky879), PMID 30256983, [PMC6323973](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/)

(The live browser now shows `#Infection` in place of `#Medical`; the eight-class structure is otherwise unchanged.)

Worked example given by the same paper: `#Environmental` (cat 1) → `#Aquatic` (cat 2) → `#Marine` (cat 3) retrieves marine isolates.

### 1.2 The same concept in the sibling source HabitatMech already ingests

GOLD's top level is a three-way version of the same partition:

> "Environmental features of a Biosample or an Organism is described in a five-level ecosystem classification… Ecosystem, Ecosystem Category, Ecosystem Type, Ecosystem Subtype and Specific Ecosystem." … "Ecosystem, which consists of Engineered, Environmental and Host-associated terms to describe the broader environment."
> — Mukherjee S, Stamatis D, Bertsch J, Ovchinnikova G, et al. *Genomes OnLine database (GOLD) v.7: updates and new features.* **Nucleic Acids Research** 47(D1):D649–D659, 2019. doi:[10.1093/nar/gky977](https://doi.org/10.1093/nar/gky977), [PMC6323969](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323969/)

GOLD's Ecosystem Categories under `Environmental` are **Air, Aquatic, Terrestrial** — the same three axes as MISO's, minus MISO's `#Biofilm` and `#Microbial community`. See also Mukherjee S, Stamatis D, Li CT, Ovchinnikova G, et al., *Twenty-five years of Genomes OnLine Database (GOLD): data updates and new features in v.9*, **NAR** 51(D1):D957–D963, 2023, doi:[10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974); and the GOLD documentation page <https://gold.jgi.doe.gov/ecosystem_classification> (returns HTTP 403 to automated fetch; content above is from the NAR papers).

### 1.3 The boundary — what is inside and what is a neighbour

**Inside** (per the tag list in §0.1): outdoor air; all natural waters (marine, freshwater, brackish, groundwater, springs, hydrothermal vents); land surfaces and subsurface (soil, sediment, sand, rock/geologic, permafrost, ice, glacier, cave, desert, forest, grassland, tundra, wetland, salt marsh, tidal flat, mangrove, volcanic); and free-living microbial structures in those settings (biofilms, microbial mats, iron mats, foam, microbial communities).

**Neighbouring concepts, explicitly outside:**

| Neighbour | Where the sources put it |
|---|---|
| Bioreactors, wastewater, activated sludge, landfill, mines, oil reservoirs, cooling towers, clean rooms, cities, roads, buildings | BacDive `#Engineered`; GOLD `Engineered` |
| Farmed land — fields, paddies, orchards, vineyards, plantations, gardens, greenhouses, meadows, parks | BacDive `#Engineered / #Agriculture`; **but GOLD `Environmental / Terrestrial`** (see §0.1) |
| Food, fermentation, dairy, starter cultures | BacDive `#Engineered`; GOLD `Engineered / Food production` |
| Any animal, plant, fungal or protist host, whole or part; rhizosphere, phyllosphere, gut, skin, blood | BacDive `#Host` / `#Host Body-Site` / `#Host Body Product`; GOLD `Host-associated` |
| Clinical/infection provenance | BacDive `#Infection` |
| Physicochemical qualifiers (acidic, saline, thermophilic, anoxic) and climate bands | BacDive `#Condition` and `#Climate` — orthogonal axes, not places |

**The one boundary the two sources genuinely disagree on is agriculture.** BacDive puts farmed land in `#Engineered`; GOLD puts it in `Environmental`. A definition that is to cover both source bins therefore cannot assert "no agricultural land," and this is the strongest single reason `ENVO:01000951` cannot be the identity of the *merged* concept. If the two records are **not** merged, the BacDive record alone is compatible with excluding farmland — but it still fails for the reasons in §2.2.

### 1.4 Ambiguity in the label

"Environmental" is ambiguous outside this context and the readings should be recorded:

1. **The provenance bin** (what the data means here): non-host, non-engineered sample origin.
2. **"Environmental" as opposed to "clinical"** — the usage in most isolation-source free text and in culture-collection catalogues, where "environmental isolate" simply means "not from a patient." Under this reading, sewage and bioreactors *are* environmental.
3. **"The environment" as a mass concept** — the totality of surroundings; ENVO's `environmental system` root.
4. **"Environmental" as a qualifier on a method** — "environmental sequencing," "environmental DNA." This is a *process/technique* sense and is not a habitat at all.

The source path (`bacdive.isolation_source:environmental`, level 1 of MISO, sibling to `#Host` and `#Engineered`) settles it on reading 1. Reading 2 must be explicitly excluded in a comment, because it is the reading a reader will default to.

---

## 2. Genus

### 2.1 Recommended genus

**`ENVO:01000254` — *environmental system***
Definition: *"A system which has the disposition to environ one or more material entities."* (as vendored in `data/raw/ontology_terms.tsv`; ENVO's public `rdfs:comment` adds the BFO-alignment caveat). Exact synonym: *environment*.

This is the correct genus because it is the immediate parent of all three of the partition's members — `natural environment` (ENVO:01000951), `anthropogenic environment` (ENVO:01000313), and `environmental system determined by an organism` (ENVO:01001000) are all direct `rdfs:subClassOf` children of it (verified via OLS4, <https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/…/hierarchicalParents>, retrieved 2026-08-17). Placing "Environmental" as a fourth sibling puts it at exactly the level where the source vocabularies place it.

**Caveat:** `ENVO:01000254`'s children are *not* a disjoint partition — it has ~25 direct children including `marine environment`, `cold environment`, `outdoor environment`, `ecosystem`, `environmental zone`. So "sibling of anthropogenic environment" is a weaker structural claim than it looks. This is an observation about ENVO's current axiomatisation, not a sourced statement.

### 2.2 Near-misses — every one checked, and why each fails

| CURIE | Label | Why it is not the answer |
|---|---|---|
| **ENVO:01000951** | **natural environment** | Definition (`IAO:0000115`, verified via OLS4): *"An environmental system in which minimal to no anthropisation has occurred and non-human agents are the primary determinants of the system's dynamics and composition."* **Fails on four counts.** (i) BacDive's bin contains `#Indoor Air` — air inside a built structure is by construction anthropised. (ii) It contains `#Dust`, `#Core sample`, `#Foam`, `#Mud (Sludge)`. (iii) It contains `#Co-culture` and `#Bacteriome`, which are laboratory/analytical constructs, not environments at all. (iv) GOLD's bin contains farmed land, contaminated soil, and `Indoor Air > Poultry farm` (§0.1). Additionally, `natural environment` has only three children — `terrestrial natural environment` (ENVO:01001226), `aquatic natural environment` (ENVO:01001227), `natural monument` — and **no air child**, so it does not even span MISO's three axes. **Verdict: strictly narrower than the concept. Keep as `relation: xref`, exactly as the record already does.** |
| ENVO:01000313 | anthropogenic environment | *"An environmental system which is the product of human activity."* This is the **complement**, corresponding to `#Engineered` / GOLD `Engineered`. Recording it here would be an outright inversion. Useful as the sibling to cite in the definition's comment. |
| ENVO:01001000 | environmental system determined by an organism (syn. *host-associated environment*) | The other complement — `#Host` / GOLD `Host-associated`. |
| ENVO:01000739 | habitat | *"An environmental system which can sustain and allow the growth of an ecological population."* Not wrong, but **non-discriminating**: every record in HabitatMech is a habitat, so using it as the genus contributes nothing to the differentia. It is also oddly placed in ENVO (parents include `population of organisms` and `astronomical body part`). |
| ENVO:01001110 | ecosystem | *"An environmental system which includes both living and non-living components."* True of the concept, but also true of `#Host` and much of `#Engineered`; does not discriminate. Its child `anthropised ecosystem` (ENVO:01001828) is again the complement. |
| ENVO:03501101 | outdoor environment | *"An environmental system which is not sheltered."* The closest **positive** near-miss and worth recording. Fails because MISO's `#Environmental` includes `#Indoor Air`, `#Cave water`, subsurface `#Geologic` and `#Groundwater`, and `#Core sample` — none of which are "not sheltered" in the ordinary sense — while it would wrongly admit city streets, which BacDive files under `#Engineered`. |
| ENVO:00010483 | environmental material | *"A material entity which other material entities in an environmental system are primarily or partially composed of."* A **material**, not a system. Grounding a place to a material is the same category error the repo's `NOT_APPLICABLE` rule guards against for qualities. Relevant only because MIxS `env_medium` draws from it. |
| ENVO:00000428 | biome | The MIxS `env_broad_scale` vocabulary. Biomes are climatically/biotically defined regions; the concept here is a provenance partition, not a biome. |
| ENVO:01001226 / ENVO:01001227 | terrestrial / aquatic natural environment | These are the children of `natural environment` that map onto MISO `#Terrestrial` / `#Aquatic`. They inherit the anthropisation restriction and there is no air counterpart. Worth flagging to ENVO as evidence that the `natural environment` branch is where a non-anthropisation-committed sibling is missing. |

**Nothing in UBERON, FOODON, BTO or PO is a candidate** — the concept is not an anatomical structure, food, culture-collection tissue source, or plant structure.

**Non-OBO vocabularies checked and rejected:** SNOMED CT has no place-kind term at this level of generality (its environment hierarchy is built around healthcare and occupational settings). AGROVOC's `environment` (c_2600) is a topical descriptor for a subject area, not a sampled place, and AGROVOC descriptors are not appropriate grounding targets for a habitat record.

---

## 3. Differentia

The observable properties that separate this concept from its siblings under `environmental system`:

1. **The sample is taken *in situ* from a bulk environmental matrix.** The material displaced at sampling (the MIxS `env_medium` sense) is air, water, soil, sediment, rock, ice, or a microbial mat/biofilm — not tissue, not a body fluid, not a manufactured product or process stream. This is the single most operational differentia and is directly checkable from the sampling record.
   *Source for the framing:* MIxS `env_medium` (MIXS:0000016) recommends subclasses of `environmental material` (ENVO:00010483); `env_broad_scale` (MIXS:0000012) recommends subclasses of `biome` (ENVO:00000428); `env_local_scale` (MIXS:0000013) admits UBERON anatomical sites *specifically for host-associated samples*. GSC MIxS: <https://genomicsstandardsconsortium.github.io/mixs/>; ENVO/MIxS usage guide: <https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS>. Original specification: Yilmaz P, Kottmann R, Field D, et al., *Minimum information about a marker gene sequence (MIMARKS) and minimum information about any (x) sequence (MIxS) specifications*, **Nature Biotechnology** 29:415–420, 2011, doi:[10.1038/nbt.1823](https://doi.org/10.1038/nbt.1823).

2. **No host organism bounds the system.** The microorganisms present are free-living rather than resident in or on a plant, animal, fungus or protist. This is the primary axis of every major microbial-habitat classification (§4), and it is the differentia that separates the concept from `ENVO:01001000`.

3. **The system is not constructed, contained, or operated for a human purpose.** No engineered vessel, built envelope, treatment process, cultivation regime, or laboratory manipulation determines its dynamics. This separates it from `ENVO:01000313`. **Note the disagreement of §1.3**: BacDive draws this line to exclude farmed land, GOLD does not.

4. **It does *not* require the absence of human influence.** Anthropogenic *contamination* of an otherwise unengineered setting stays inside: GOLD has `Environmental > Terrestrial > Soil > Contaminated > Pesticide`, `… > Oil-contaminated`, `… > Uranium contaminated`, and `Environmental > Aquatic > Marine > Oceanic > Oil-contaminated`. This is the property that makes the concept **broader than `natural environment`** and is the crux of the whole grounding decision.

5. **Physicochemistry and climate are orthogonal, not differentiating.** BacDive models these on separate axes — `#Condition` (`#Acidic`, `#Alkaline`, `#Anoxic`, `#Saline`, `#Sulfuric`, `#Thermophilic`, `#Xerophilic`, `#Humid`) and `#Climate` (`#Cold`, `#Hot`, `#Temperate`, and level‑3 `#Polar`, `#Boreal`, `#Alpine`, `#Arid`, `#Tropical`…). A strain from an acidic hot spring carries `#Environmental` *and* `#Acidic` *and* `#Hot`. This matches the repo's existing `NOT_APPLICABLE` rule for qualities (`"Acidic" maps to PATO:0001429`) — do not fold any of these into the differentia.

**Characteristic taxa (weak, and I flag it as such):** the record's top BacDive taxa are dominated by myxobacteria (*Sorangium cellulosum* 1,535; *Corallococcus coralloides* 1,301; *Nannocystis exedens* 1,008; *Myxococcus* spp.). That is a **collection-bias artefact**, not an ecological signature — it reflects large historical soil-myxobacteria isolation campaigns deposited in DSMZ, not anything true of environmental habitats as a class. It should not enter the definition. *(This is my inference from the taxon profile, not a claim any cited source makes.)*

---

## 4. Sources

**Primary — the source vocabularies themselves**

- Reimer LC, Vetcininova A, Sardà Carbasse J, Söhngen C, Gleim D, Ebeling C, Overmann J. *BacDive in 2019: bacterial phenotypic data for High-throughput biodiversity analysis.* **Nucleic Acids Research** 47(D1):D631–D636 (26 Sep 2018). doi:[10.1093/nar/gky879](https://doi.org/10.1093/nar/gky879) · PMID [30256983](https://pubmed.ncbi.nlm.nih.gov/30256983/) · [PMC6323973](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/) — **introduces MISO, the three levels, and the eight top-level classes; source of the verbatim quote in §1.1.**
- Reimer LC, Sardà Carbasse J, Koblitz J, Ebeling C, Podstawka A, Overmann J. *BacDive in 2022: the knowledge base for standardized bacterial and archaeal data.* **NAR** 50(D1):D741–D746 (29 Oct 2021). doi:[10.1093/nar/gkab961](https://doi.org/10.1093/nar/gkab961)
- Schober I, Koblitz J, Sardà Carbasse J, Ebeling C, et al. *BacDive in 2025: the core database for prokaryotic strain data.* **NAR** 53(D1):D748–D756 (29 Oct 2024). doi:[10.1093/nar/gkae959](https://doi.org/10.1093/nar/gkae959) — current release; describes the BacDive knowledge graph and SPARQL endpoint, which is the machine-readable route to MISO if the hierarchy is to be ingested properly rather than as a flat tag list.
- BacDive isolation-source browser, <https://bacdive.dsmz.de/isolation-sources> — **the authoritative current MISO hierarchy; source of the tag lists in §0.1, extracted from `data-parent-id` / `data-cat1-ids` attributes, retrieved 2026-08-17.**
- Mukherjee S, Stamatis D, Bertsch J, Ovchinnikova G, Katta HY, Mojica A, Chen I-MA, Kyrpides NC, Reddy TBK. *Genomes OnLine database (GOLD) v.7: updates and new features.* **NAR** 47(D1):D649–D659 (24 Oct 2018). doi:[10.1093/nar/gky977](https://doi.org/10.1093/nar/gky977) · [PMC6323969](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323969/) — **source of the verbatim GOLD quotes in §1.2.**
- Mukherjee S, Stamatis D, Li CT, Ovchinnikova G, et al. *Twenty-five years of Genomes OnLine Database (GOLD): data updates and new features in v.9.* **NAR** 51(D1):D957–D963 (1 Nov 2022). doi:[10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974)
- GOLD ecosystem classification: <https://gold.jgi.doe.gov/ecosystem_classification>

**Independent corroboration that the host/non-host split is the primary axis**

- Thompson LR, Sanders JG, McDonald D, et al. (Earth Microbiome Project Consortium). *A communal catalogue reveals Earth's multiscale microbial diversity.* **Nature** 551:457–463 (1 Nov 2017). doi:[10.1038/nature24621](https://doi.org/10.1038/nature24621) — EMPO level 1 is **free-living vs host-associated**; level 2 splits free-living by salinity (saline / non-saline). This is the strongest external evidence that the concept is a real, independently rediscovered partition and not a BacDive idiosyncrasy.
- Shaffer JP, Nothias L-F, Thompson LR, et al. *Standardized multi-omics of Earth's microbiomes reveals microbial and metabolite diversity.* **Nature Microbiology** 7:2128–2150 (28 Nov 2022). doi:[10.1038/s41564-022-01266-x](https://doi.org/10.1038/s41564-022-01266-x) · PMID [36443458](https://pubmed.ncbi.nlm.nih.gov/36443458/) — EMPO v2; retains host-association as level 1 while moving salinity to level 2 for *both* branches.
- EMPO documentation: <https://earthmicrobiome.org/protocols-and-standards/empo/> — fields `empo_1` ∈ {Free-living, Host-associated, Control, Unknown}.

**Standards**

- Yilmaz P, Kottmann R, Field D, et al. *Minimum information about a marker gene sequence (MIMARKS) and minimum information about any (x) sequence (MIxS) specifications.* **Nature Biotechnology** 29:415–420 (2011). doi:[10.1038/nbt.1823](https://doi.org/10.1038/nbt.1823)
- GSC MIxS term registry: `env_broad_scale` <https://genomicsstandardsconsortium.github.io/mixs/0000012/>, `env_local_scale` <https://genomicsstandardsconsortium.github.io/mixs/0000013/>
- ENVO/MIxS usage guide: <https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS>

**Ontology**

- Buttigieg PL, Morrison N, Smith B, Mungall CJ, Lewis SE, ENVO Consortium. *The environment ontology: contextualising biological and biomedical entities.* **Journal of Biomedical Semantics** 4:43 (2013). doi:[10.1186/2041-1480-4-43](https://doi.org/10.1186/2041-1480-4-43)
- Buttigieg PL, Pafilis E, Lewis SE, Schildhauer MP, Walls RL, Mungall CJ. *The environment ontology in 2016: bridging domains with increased scope, semantic density, and interoperation.* **J Biomed Semantics** 7:57 (2016). doi:[10.1186/s13326-016-0097-6](https://doi.org/10.1186/s13326-016-0097-6)
- ENVO term definitions and hierarchy retrieved from OLS4 (<https://www.ebi.ac.uk/ols4/api/>) on 2026-08-17: `ENVO:01000254`, `ENVO:01000951`, `ENVO:01000313`, `ENVO:01001000`, `ENVO:01000739`, `ENVO:01001110`, `ENVO:03501101`, `ENVO:01001226`, `ENVO:01001227`, `ENVO:01001828`, `ENVO:01000952`.

**Marked as inference, not sourced:** §0.3 (that 18,454 is a rollup); §2.1's caveat about ENVO's children not being a partition; §3's reading of the myxobacterial taxon profile as collection bias; and the overall judgement in §6.

---

## 5. Synonyms, and what not to conflate

### Names in real use for this concept

| Name | Where used |
|---|---|
| **free-living environment** / **free-living** | EMPO `empo_1`; the best positive-polarity name in the literature |
| **non-host-associated environment** | common in comparative microbiome work |
| **environmental (as a sample-provenance bin)** | BacDive MISO cat 1; GOLD Ecosystem level 1 |
| **environmental sample source** / **environmental isolate source** | culture-collection catalogues |
| **natural and semi-natural environment** | used where anthropogenic disturbance must be admitted without implying engineering |
| **in-situ environment** (contrast: *ex situ*, which BacDive files under `#Engineered`) | BacDive tag semantics |

### Commonly but wrongly treated as the same thing — do NOT conflate

- **`ENVO:01000951` *natural environment*.** The single most likely error, and the one already correctly caught. It asserts minimal anthropisation; this concept does not. Keep as `relation: xref`.
- **"Environmental" = "non-clinical."** Very widespread in isolation-source free text. Under that reading sewage, bioreactors and food are environmental; under MISO/GOLD they are `#Engineered`.
- **`ENVO:00010483` *environmental material*.** A material, not a system. The MIxS `env_medium` slot, not a habitat.
- **`ENVO:00000428` *biome*.** The MIxS `env_broad_scale` slot. A climatic/biotic region, not a provenance partition.
- **`ENVO:01000313` *anthropogenic environment*** and **`ENVO:01001000` *environmental system determined by an organism*.** Both are complements. Attaching either as parent or identity inverts the meaning.
- **`ENVO:03501101` *outdoor environment*.** Overlaps heavily but cross-cuts: excludes indoor air, caves and subsurface (which are in), includes streets and buildings' exteriors (which are out).
- **"Environmental sequencing / environmental DNA."** A method, not a place.
- **`ENVO:01000952` *anthropisation*.** A process. Cf. the repo's rule that processes are `NOT_APPLICABLE`.
- **BacDive `#Condition` and `#Climate` tags.** Orthogonal axes. A strain is `#Environmental` *and* `#Saline` *and* `#Cold`; folding those in is the mistake the repo's environment-parameter skip rule (`sediment_marine_cold`) already guards against.

---

## 6. Should it be a term at all?

**Yes — as an explicitly-labelled grouping class, not as a sampleable habitat.** It is not a process, a quality, a disease state, a taxon, or a sampling artefact, so none of the corpus's existing disposals apply. It denotes a kind of place, and two independent, widely-used source vocabularies (BacDive MISO, GOLD) plus a third independent scheme (EMPO) all draw the same top-level cut, which is about as strong an argument for term-hood as a high-level bin can have.

Three qualifications the curator should weigh:

1. **Its differentia is partly negative, and that is a real defect in an Aristotelian definition.** OBO practice discourages definition by negation. The honest framing to send upstream is not "please add *Environmental*" but **"ENVO has positive classes for host-determined and anthropogenic environments but no sibling for their complement; `natural environment` is not that sibling because it requires minimal anthropisation, and every large microbial-provenance vocabulary needs the complement class."** That is a defensible, specific ENVO request. *(Per standing rule: no ENVO submission without a separate, explicit yes for that individual request.)*

2. **Its real annotation yield is much lower than 18,454** (§0.3). The number that would land on a term used *only* where no finer bin applies is far smaller. Rank the backlog accordingly.

3. **Merge the BacDive and GOLD records first** (§0.2). Writing one definition for two identifiers that denote the same concept publishes a duplicate. The one substantive difference between the two bins — agriculture, in for GOLD, out for BacDive — belongs in the merged record's notes, not in the definition, since it is a disagreement between sources rather than a property of the concept.

**Suggested record shape** (for `curation/decisions.tsv`, subject to the merge decision):

- `parent_habitats`: `ENVO:01000254` *environmental system*, `relation: parent` — genuinely broader, asserts nothing the sources do not.
- `xrefs`: `ENVO:01000951` *natural environment*, `relation: xref` — **keep as-is**; it records the near-miss so it is not re-derived, exactly as #99 intends. Consider adding `ENVO:03501101` *outdoor environment* as a second xref for the same reason.
- Grounding: `CONFIRM_UNGROUNDED`, term-request candidate.
- Note: replace the Paddy/Grove/Herbaceous evidence with the `#Indoor Air` / `#Dust` / `#Co-culture` / `#Bacteriome` evidence for the BacDive record, and keep the `Tree plantation` evidence on the GOLD side — `tests/test_decisions.py` checks the claims a note makes, and the current BacDive note asserts a source path that the source does not have.

## Citations

1. https://bacdive.dsmz.de/isolation-sources
2. https://doi.org/10.1093/nar/gky879
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/
4. https://doi.org/10.1093/nar/gky977
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC6323969/
6. https://doi.org/10.1093/nar/gkac974
7. https://gold.jgi.doe.gov/ecosystem_classification
8. https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/…/hierarchicalParents
9. https://genomicsstandardsconsortium.github.io/mixs/
10. https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
11. https://doi.org/10.1038/nbt.1823
12. https://pubmed.ncbi.nlm.nih.gov/30256983/
13. https://doi.org/10.1093/nar/gkab961
14. https://doi.org/10.1093/nar/gkae959
15. https://doi.org/10.1038/nature24621
16. https://doi.org/10.1038/s41564-022-01266-x
17. https://pubmed.ncbi.nlm.nih.gov/36443458/
18. https://earthmicrobiome.org/protocols-and-standards/empo/
19. https://genomicsstandardsconsortium.github.io/mixs/0000012/
20. https://genomicsstandardsconsortium.github.io/mixs/0000013/
21. https://doi.org/10.1186/2041-1480-4-43
22. https://doi.org/10.1186/s13326-016-0097-6
23. https://www.ebi.ac.uk/ols4/api/