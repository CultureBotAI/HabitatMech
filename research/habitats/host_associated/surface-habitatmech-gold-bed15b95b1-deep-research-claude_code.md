---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T02:22:45.359694'
end_time: '2026-08-18T02:32:16.336656'
duration_seconds: 570.98
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Surface
  habitat_identifier: habitatmech:GOLD.bed15b95b1
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Plants > Phyllosphere > Surface'
  assertions: '1'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Disjoint-grounding\
    \ review (#62): was UBERON:0002416 'integumental system', an ANIMAL organ system,\
    \ for a plant leaf surface \u2014 matched across kingdoms on a synonym. The slice\
    \ has no plain plant-surface or phyllosphere term; the nearest, ENVO:01001032,\
    \ is specifically a biofilm on one. Path: Host-associated > Plants > Phyllosphere\
    \ > Surface (source concept habitatmech:GOLD.bed15b95b1)"
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
  web_search_requests: 17
  num_turns: 47
  total_cost_usd: 4.154815999999999
  session_id: 74dec358-c7b4-495d-aafd-57511c619acc
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 29
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Surface
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.bed15b95b1
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Plants > Phyllosphere > Surface
- **Upstream assertion volume:** 1
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Disjoint-grounding review (#62): was UBERON:0002416 'integumental system', an ANIMAL organ system, for a plant leaf surface — matched across kingdoms on a synonym. The slice has no plain plant-surface or phyllosphere term; the nearest, ENVO:01001032, is specifically a biofilm on one. Path: Host-associated > Plants > Phyllosphere > Surface (source concept habitatmech:GOLD.bed15b95b1)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Surface** as a microbial habitat, with citations.

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

# Definition research: **Surface** (`habitatmech:GOLD.bed15b95b1`)

> **Proposed definition:** A plant-associated environment which is determined by the exterior surface of a living plant's above-ground organs — the cuticle and the thin film of epicuticular wax, leachates and intermittent water overlying it — and which is colonised by epiphytic microorganisms rather than by the endophytes of the interior tissues.

Genus term available in the vendored slice: **`ENVO:01001001` 'plant-associated environment'** ("An environmental system determined by a green plant") — broader than the concept, so it is a legitimate `parent_habitats` / `GROUND_AS_PARENT` target, not an identity. No ENVO, PO, UBERON, FOODON or BTO term names the concept itself. See §6 for a caveat: the missing class is really one level up (*phyllosphere* / aerial plant surface environment), and this record and its parent `habitatmech:GOLD.7406232b7e` 'Phyllosphere' should probably be one term request, not two.

---

## 1. What the concept denotes

**The reading the data supports.** The attestation is GOLD path `Host-associated > Plants > Phyllosphere > Surface` — an *Ecosystem Subtype* sitting directly under the Ecosystem Type **Phyllosphere**, which GOLD itself glosses as "above-ground surfaces of plant" ([GOLD ontology class `Phyllosphere`, via OLS4](https://www.ebi.ac.uk/ols4/api/v2/ontologies/gold/classes?search=phyllosphere); GOLD's five-level scheme is described in [Mukherjee et al. 2023, *Nucleic Acids Research* 51:D957–D963, doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974)). Its siblings at that same level in the local extract (`data/raw/gold_ecosystem_paths.tsv`) are `Caulosphere` (stem), `Anthosphere` (flower), `Carposphere` (fruit), `Phylloplane/Leaf`, `Phylloplane/Leaf surface`, `Stem`, `Petiole` and `Seeds`. In the GOLD ontology snapshot in OLS, `Caulosphere`, `Anthosphere` and `Carposphere` each carry an `anatomical_site` annotation (stem, flower, fruit); the *Phylloplane/Leaf surface* node carries none, and the node behind this record carries none either.

So the concept the sample provenance means is: **the outer face of a plant's aerial organs, taken as the place a microbial sample was washed or scraped from, with the organ left unspecified.** It is the epiphytic compartment of the phyllosphere — what Ruinen called "the external leaf surface … as an environment for micro-organisms" when the term was established in the 1950s ([Last 1955; Ruinen 1956, *Nature* 177:220–221, doi:10.1038/177220a0](https://doi.org/10.1038/177220a0); history reviewed in [Leveau 2006, *Microbial communities in the phyllosphere*](https://leveau.ucdavis.edu/wp-content/uploads/sites/220/2019/07/Leveau2006a.pdf)).

**Boundary — inside the concept:**
- the cuticle's outer face and its epicuticular wax crystals, on leaves, stems, petioles, flowers, fruits and other aerial organs;
- the solid topography microbes colonise — veins, anticlinal-wall grooves, trichome bases, stomatal complexes ([Lindow & Brandl 2003, *Appl Environ Microbiol* 69:1875–1883, doi:10.1128/AEM.69.4.1875-1883.2003](https://doi.org/10.1128/AEM.69.4.1875-1883.2003));
- the transient water film and droplets on that surface — the "phyllotelma" or leaf-surface waterscape, distinguished from the solid "phylloplane" landscape by [Doan & Leveau 2015, *Phytopathology* 105:1036–1042, doi:10.1094/PHYTO-02-15-0050-RVW](https://doi.org/10.1094/PHYTO-02-15-0050-RVW);
- leachates, exudates and guttation fluid deposited on that surface — the nutrient base of the habitat ([Lindow & Brandl 2003](https://doi.org/10.1128/AEM.69.4.1875-1883.2003)).

**Boundary — neighbouring concepts, outside:**
- the **leaf/organ interior** (endosphere, apoplast, xylem, leaf nodules): GOLD holds these as separate paths (`Phylloplane/Leaf > Endosphere`, `Phylloplane/Leaf > Leaf nodule`), and the split is operationally the difference between washing/sonicating a leaf and surface-sterilising it before extraction (methods and their failure modes: [Sahu et al. 2022, *J Basic Microbiol* 62:57–70, doi:10.1002/jobm.202100462](https://doi.org/10.1002/jobm.202100462); [Saldierna Guzmán et al. 2020, "Simple methods to remove microbes from leaf surfaces"](https://escholarship.org/content/qt05n539tv/qt05n539tv.pdf));
- **below-ground surfaces** — rhizoplane and rhizosphere — which are the explicit contrast class in every definition of the phyllosphere ([Vorholt 2012, *Nat Rev Microbiol* 10:828–840, doi:10.1038/nrmicro2910](https://doi.org/10.1038/nrmicro2910));
- **leaf litter / dead plant matter** (`ENVO:01000628` 'plant litter'), which is no longer a living plant's surface;
- an established **biofilm** on that surface, which GOLD itself separates (`Phyllosphere > Phylloplane/Leaf surface > Biofilm`) and which is what `ENVO:01001032` actually names.

**Residual ambiguity, stated rather than resolved.** "Surface" is a bare relational noun and two readings survive:
- **(a) organ-unspecified aerial plant surface** — supported by its position directly under *Phyllosphere*, by GOLD's own gloss of the parent, and by the absence of an `anatomical_site` annotation. This is the reading the proposed definition takes.
- **(b) leaf surface specifically** — the reading the earlier HabitatMech curation note assumed. It is weaker: GOLD already has `Phylloplane/Leaf surface` (843 assertions) and `Phylloplane/Leaf > Leaf surface` (128) as distinct nodes, so an annotator who meant "leaf" had two better nodes to pick. The record carries 1 organism assertion across 2 GOLD node ids (`gold.ecosystem:7642|7643`), i.e. this is a thinly-populated node whose intent cannot be recovered from usage volume.

If the curator wants reading (b), the definition should say "leaf" and the record should probably be merged into the leaf-surface family instead — see §6.

## 2. Genus — the broader kind

The smallest well-established kind is *an environment determined by a plant, restricted to its exterior*. **No ontology term expresses that.** Best available genus in the vendored slice, one step too broad:

| CURIE | Label | Verdict |
|---|---|---|
| `ENVO:01001001` | plant-associated environment — "An environmental system determined by a green plant." | **Use as genus / `parent_habitats`.** Correctly broader; says nothing about surface vs interior, aerial vs root. |

Near-misses, and why each fails:

| CURIE | Label | Why it is not a match |
|---|---|---|
| `ENVO:01001032` | environment determined by a biofilm on a plant surface | **Narrower — asserts a biofilm.** Its definition is "An environmental system which has its properties and dynamics determined by a biofilm on the surface of a plant" and it is subclassed under *environmental system determined by a material* with a restriction on biofilm material adjacent to a plant surface layer ([OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001032)). Grounding here publishes a biofilm claim the single GOLD assertion never makes; much phyllosphere colonisation is solitary cells and small aggregates, not biofilm. **This term is also the origin of the confusion**: its alternative label in ENVO is literally "Plant surface", because it is the mapping target for EMPO's level-3 class *Plant surface* ([Thompson et al. 2017, *Nature* 551:457–463, doi:10.1038/nature24621](https://doi.org/10.1038/nature24621); [EMPO](https://earthmicrobiome.org/protocols-and-standards/empo/)). The EMPO label is a habitat bucket; the ENVO class it points at is a biofilm environment. Record it as `relation: xref`, not as identity or parent. |
| `ENVO:01001057` | environment associated with a plant part or small plant | Sibling, not parent: alt label "Plant corpus" (EMPO), i.e. the plant *body/material* — which in EMPO is explicitly contrasted with *Plant surface*. Grounding here would place a surface sample inside the plant-material bucket. |
| `ENVO:01001031` | environment determined by a plant substance | About plant substances (sap, exudate as material), not the organ exterior. |
| `ENVO:00010504` | surface layer — "A layer of some material entity which is adjacent to one or more of its external boundaries and directly interacts with its immediate surroundings." | Right shape, wrong kind: it is a generic layer, not an environment, and carries nothing plant-specific. ENVO's populated children of this branch are all abiotic (soil, sea, ice, glacial); there is **no plant surface layer** class. Usable only as a genus for a *new* term, not as a grounding target on its own. |
| `PO:0005679` / `PO:0006016` | plant epidermis / leaf epidermis | A **tissue**, not a surface: "A portion of plant tissue composed of plant epidermal cells … that covers the surface of a plant structure". It includes cell interiors and inner periclinal walls that no epiphyte ever occupies, and `PO:0006016` is leaf-specific where this concept is organ-unspecified. Note that upstream kg-microbe already maps BacDive's *Phylloplane* to `PO:0006016` with `skos:exactMatch` (`data/raw/isolation_source_groundings.tsv:236`) — that is an over-claim of the same shape, worth flagging rather than copying. |
| `PO:0000022`, `PO:0025388` | plant cuticle, epicuticular wax | Materials *on* the surface — components of the habitat, narrower than it, and grounding to them names a substance where the source names a place. Good `xref`s. |
| `PO:0025034` | leaf | What the corpus already uses for GOLD's `Phylloplane/Leaf` and `Phylloplane/Leaf surface` (EXACT, via GOLD-supplied synonyms). Wrong here for two reasons: it is an organ, not that organ's exterior, and this node is not leaf-restricted. |
| `UBERON:0002416` | integumental system | The previous, retired grounding. An **animal** organ system; the match came across kingdoms through GOLD's generic `Surface` node whose synonym is "anatomical surface". Correctly rejected under #62. |
| — | *phyllosphere* | **No class with this label exists in ENVO** (searches of ENVO via OLS4 return nothing; the only "Phyllosphere" hit in OLS is GOLD's own ecosystem class). The nearest ENVO tracker discussion of how to type host-derived samples is [envo#1029](https://github.com/EnvironmentOntology/envo/issues/1029), which is still open-ended. ENVO's MIxS guidance for plant samples reaches for canopy/litter-layer terms plus `ENVO:01001121` 'plant matter' as `env_medium` ([ENVO wiki, *Using ENVO with MIxS*](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS)) — i.e. it routes around the gap rather than filling it. |

*My inference, not a source claim:* that the absence of a plant-surface environment class in ENVO is a genuine gap rather than a deliberate exclusion. The parallel animal branch is equally thin (EMPO's *Animal surface* maps to the corresponding biofilm class), which is consistent with a gap.

## 3. Differentia — what distinguishes it from its siblings

Under *plant-associated environment*, the properties that separate this concept, all observable or measurable:

- **Exterior, not interior.** Its inhabitants are removable by washing, agitation or sonication and killable by non-penetrating agents such as peroxide or UV — the operational test Lindow & Brandl use to define epiphytes ([doi:10.1128/AEM.69.4.1875-1883.2003](https://doi.org/10.1128/AEM.69.4.1875-1883.2003)).
- **Above ground, not root-associated.** The phyllosphere is defined by contrast to the rhizosphere ([Vorholt 2012](https://doi.org/10.1038/nrmicro2910)).
- **Dominant material: cuticle + epicuticular wax.** A hydrophobic layer that limits passive diffusion of nutrients and water vapour from the plant interior and sets the surface's wettability ([Lindow & Brandl 2003](https://doi.org/10.1128/AEM.69.4.1875-1883.2003); cuticle biology: [Yeats & Rose 2013, *Plant Physiol* 163:5–20, doi:10.1104/pp.113.222737](https://doi.org/10.1104/pp.113.222737)).
- **Oligotrophic and spatially heterogeneous.** Carbon is the limiting factor and is patchy; simple sugars (glucose, fructose, sucrose) dominate; cells aggregate at nutrient-rich sites near veins and trichome bases, with aggregates accounting for 30–80% of the total bacterial population ([Lindow & Brandl 2003](https://doi.org/10.1128/AEM.69.4.1875-1883.2003); [Thomas, Kay & Fones 2024, *BMC Biology* 22:168, doi:10.1186/s12915-024-01967-1](https://doi.org/10.1186/s12915-024-01967-1)).
- **Stress regime:** high UV flux, desiccation, and rapidly fluctuating temperature and relative humidity — "a harsh environment for microorganisms" ([Rangel & Leveau 2024, *Appl Microbiol Biotechnol* 108:211, doi:10.1007/s00253-024-13042-4](https://doi.org/10.1007/s00253-024-13042-4)).
- **Two coupled compartments:** solid landscape (phylloplane) and intermittent waterscape (phyllotelma), the latter formed by rain, fog, dew, guttation and re-condensation and required for microbial motility, nutrient acquisition and signalling ([Doan & Leveau 2015](https://doi.org/10.1094/PHYTO-02-15-0050-RVW)).
- **Characteristic population density:** 10⁶–10⁸ bacterial cells cm⁻² of leaf ([Rangel & Leveau 2024](https://doi.org/10.1007/s00253-024-13042-4); 10⁶–10⁷ cm⁻², up to 10⁸ g⁻¹ in [Lindow & Brandl 2003](https://doi.org/10.1128/AEM.69.4.1875-1883.2003)).
- **Scale:** ~6.4 × 10⁸ km² of terrestrial leaf surface, roughly twice global land area, carrying on the order of 10²⁶ bacterial cells (Morris & Kinkel 2002, in *Phyllosphere Microbiology*, APS Press, pp. 365–375, as cited by [Lindow & Brandl 2003](https://doi.org/10.1128/AEM.69.4.1875-1883.2003) and [Vorholt 2012](https://doi.org/10.1038/nrmicro2910); ~10⁹ km² / 10²⁶ cells in [Remus-Emsermann & Schlechter 2018, *New Phytologist* 218:1327–1333, doi:10.1111/nph.15054](https://doi.org/10.1111/nph.15054)).
- **Internally structured at the sub-organ scale** — enough that a definition should not over-specify: adaxial and abaxial faces of the same leaf carry compositionally and functionally distinct communities (upper surfaces enriched in degradation pathways and saprotrophic fungi, lower surfaces in biosynthetic/energy pathways and plant pathogens) ([Sugimoto et al. 2026, *J Exp Bot*, doi:10.1093/jxb/erag255](https://doi.org/10.1093/jxb/erag255)).

## 4. Sources

Primary and review literature
- Ruinen J. 1956. Occurrence of *Beijerinckia* species in the "phyllosphere". *Nature* 177:220–221. doi:[10.1038/177220a0](https://doi.org/10.1038/177220a0) — coinage (with Last 1955); phyllosphere as the external leaf surface as a microbial environment.
- Lindow SE, Brandl MT. 2003. Microbiology of the phyllosphere. *Appl Environ Microbiol* 69:1875–1883. doi:[10.1128/AEM.69.4.1875-1883.2003](https://doi.org/10.1128/AEM.69.4.1875-1883.2003) — the canonical habitat description; densities, cuticle, oligotrophy, aggregates, epiphyte definition.
- Vorholt JA. 2012. Microbial life in the phyllosphere. *Nat Rev Microbiol* 10:828–840. doi:[10.1038/nrmicro2910](https://doi.org/10.1038/nrmicro2910) — phyllosphere surface area ≈ 2× land surface; surface vs interior; community composition.
- Doan HK, Leveau JHJ. 2015. Artificial surfaces in phyllosphere microbiology. *Phytopathology* 105:1036–1042. doi:[10.1094/PHYTO-02-15-0050-RVW](https://doi.org/10.1094/PHYTO-02-15-0050-RVW) — phylloplane (landscape) vs phyllotelma (waterscape).
- Remus-Emsermann MNP, Schlechter RO. 2018. Phyllosphere microbiology: at the interface between microbial individuals and the plant host. *New Phytologist* 218:1327–1333. doi:[10.1111/nph.15054](https://doi.org/10.1111/nph.15054) — ~10⁹ km², ~10²⁶ cells; leaf as island; micro-scale heterogeneity.
- Rangel LI, Leveau JHJ. 2024. Applied microbiology of the phyllosphere. *Appl Microbiol Biotechnol* 108:211. doi:[10.1007/s00253-024-13042-4](https://doi.org/10.1007/s00253-024-13042-4) — 10⁶–10⁸ cells cm⁻²; residual vs transient epiphytes; stress regime.
- Thomas G, Kay WT, Fones HN. 2024. Life on a leaf: the epiphyte to pathogen continuum and interplay in the phyllosphere. *BMC Biology* 22:168 (7 Aug 2024). doi:[10.1186/s12915-024-01967-1](https://doi.org/10.1186/s12915-024-01967-1) — epiphyte definition; topography, carbon as limiting factor; epiphyte–pathogen continuum.
- Bringel F, Couée I. 2015. Pivotal roles of phyllosphere microorganisms at the interface between plant functioning and atmospheric trace gas dynamics. *Front Microbiol* 6:486. doi:[10.3389/fmicb.2015.00486](https://doi.org/10.3389/fmicb.2015.00486) — phyllosphere compartment vocabulary (phylloplane, caulosphere, anthosphere, carposphere).
- Sugimoto H, et al. 2026. Adaxial–abaxial leaf surface asymmetry is a key ecological driver of the phyllosphere microbiome. *J Exp Bot*. doi:[10.1093/jxb/erag255](https://doi.org/10.1093/jxb/erag255) — sub-organ structuring of the surface habitat.
- Sahu PK, et al. 2022. Surface sterilization for isolation of endophytes: ensuring what (not) to grow. *J Basic Microbiol* 62:57–70. doi:[10.1002/jobm.202100462](https://doi.org/10.1002/jobm.202100462) — the surface/interior split is operational, defined by method.
- Yeats TH, Rose JKC. 2013. The formation and function of plant cuticles. *Plant Physiol* 163:5–20. doi:[10.1104/pp.113.222737](https://doi.org/10.1104/pp.113.222737).

Standards and vocabularies
- GOLD Ecosystem Classification, five-level scheme and plant branch: Mukherjee S, et al. 2023. *Nucleic Acids Research* 51:D957–D963. doi:[10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974); classification pages at [gold.jgi.doe.gov/ecosystem_classification](https://gold.jgi.doe.gov/ecosystem_classification) (JS-rendered; the machine-readable tree is mirrored as the `gold` ontology in [OLS4](https://www.ebi.ac.uk/ols4/api/v2/ontologies/gold/classes?search=phyllosphere)). GOLD annotates this whole branch `mixs_extension: MIXS:PlantAssociated`, i.e. it expects the [MIxS plant-associated environmental package](https://www.ncbi.nlm.nih.gov/biosample/docs/packages/MIMS.me.plant-associated.6.0/).
- EMPO: Thompson LR, et al. 2017. A communal catalogue reveals Earth's multiscale microbial diversity. *Nature* 551:457–463. doi:[10.1038/nature24621](https://doi.org/10.1038/nature24621); [EMPO page](https://earthmicrobiome.org/protocols-and-standards/empo/) — *Plant surface* as an empo_3 class (empo_4 in EMPO v2, [Shaffer et al. 2022, *Nat Microbiol*, doi:10.1038/s41564-022-01266-x](https://doi.org/10.1038/s41564-022-01266-x)).
- ENVO term records via OLS4: [`ENVO:01001001`](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001001), [`ENVO:01001032`](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001032), [`ENVO:01001057`](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001057), [`ENVO:00010504`](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00010504); ENVO/MIxS guidance in the [ENVO wiki](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS) and open discussion [envo#1029](https://github.com/EnvironmentOntology/envo/issues/1029).

Repo evidence (checked locally, not literature): `data/raw/gold_ecosystem_paths.tsv` — the target path carries 1 organism assertion across `gold.ecosystem:7642|7643`, while sibling `Phylloplane/Leaf surface` carries 843 and `Phylloplane/Leaf` 1,448; `data/raw/isolation_source_groundings.tsv:236` — upstream maps BacDive *Phylloplane* to `PO:0006016` as an exact match; `data/raw/ontology_terms.tsv` — `ENVO:01001001`, `ENVO:01001032`, `ENVO:01001057`, `ENVO:00010504`, `PO:0005679`, `PO:0006016`, `PO:0000022`, `PO:0025388` are all present in the slice, `UBERON:0006984` is not.

**Explicitly my inference, not sourced:** (i) that GOLD's `Surface` node under *Phyllosphere* means organ-unspecified aerial surface — argued from path position and the absence of an `anatomical_site` annotation, not stated by GOLD; (ii) that EMPO's *Plant surface* → `ENVO:01001032` mapping is the proximate cause of "plant surface" being read as a biofilm class; (iii) the recommendation in §6 about merging.

## 5. Synonyms and what NOT to conflate

**Names in real use for this concept**
- *plant surface* / *aerial plant surface* / *above-ground plant surface* (EMPO's *Plant surface*)
- *phylloplane* — strictly the leaf-surface landscape; the standard term when the organ is a leaf ([Last & Deighton 1965](https://doi.org/10.1016/S0007-1536(65)80100-1); [Doan & Leveau 2015](https://doi.org/10.1094/PHYTO-02-15-0050-RVW))
- *leaf surface*, *epiphytic compartment*, *epiphytic habitat*, *phyllosphere sensu stricto* (usage where "phyllosphere" is restricted to surface-dwelling communities — [Bringel & Couée 2015](https://doi.org/10.3389/fmicb.2015.00486))
- organ-specific covers of the same idea: *caulosphere* (stem), *anthosphere* (flower), *carposphere* (fruit) surfaces

**Do not conflate with**
- **`ENVO:01001032` 'environment determined by a biofilm on a plant surface'** — despite its ENVO alternative label "Plant surface". A biofilm claim, narrower.
- **Phyllosphere *sensu lato*** — many authors include the interior of aerial organs and the leaf boundary layer; that broader sense is the parent record `habitatmech:GOLD.7406232b7e`, not this one ([Vorholt 2012](https://doi.org/10.1038/nrmicro2910)).
- **Endosphere / endophytes** — the interior; a distinct GOLD path and a distinct sampling protocol.
- **`PO:0005679` / `PO:0006016` epidermis** — a tissue of the plant, not the exterior surface; and leaf-specific in the latter case.
- **`PO:0025034` 'leaf'** — the whole organ.
- **Plant litter (`ENVO:01000628`)** — dead, detached plant material.
- **Rhizoplane / rhizosphere** — below-ground surfaces.
- **`UBERON:0002416` 'integumental system'** and the generic GOLD `Surface` node ("anatomical surface") — animal anatomy; the cross-kingdom match that #62 retired.
- **"Epiphyte" in the botanical sense** — a plant growing on another plant (orchids, bromeliads). GOLD's `Epiphytes` nodes under this branch mean epiphytic *microorganisms*; the homonymy is a live risk for anyone grounding those sibling records.

## 6. Should it be a term at all?

**Yes — it is a place, not a process, quality, disease or taxon.** A microbial sample is physically taken from it, and the literature treats it as a habitat with its own physicochemistry, colonists and dynamics. Nothing here supports `NOT_APPLICABLE`.

Three things a curator should weigh before writing the definition, though:

1. **The gap is one level up.** ENVO has no *phyllosphere* / *aerial plant surface environment* class at all, and this record's own parent — `habitatmech:GOLD.7406232b7e` 'Phyllosphere', 149 assertions — is likewise UNGROUNDED. The highest-yield unit of work is a single ENVO term request for the aerial-plant-surface environment (genus `ENVO:01001001`, differentia "restricted to the exterior of above-ground organs"), after which this record is either that term or a trivially-defined child of it. Writing a standalone definition for the 1-assertion child while the 149-assertion parent stays undefined inverts the priority. This is the "intermediate class is missing" case the brief asks to be named rather than papered over.

2. **The label is not self-standing and the node is nearly empty.** "Surface" carries 1 organism assertion, against 843 for the sibling `Phylloplane/Leaf surface` and 1,448 for `Phylloplane/Leaf` — both of which the corpus already resolves to `PO:0025034` 'leaf' via GOLD-supplied exact synonyms. It is a reasonable reading that GOLD's `Phyllosphere > Surface` is a legacy/redundant node superseded by `Phylloplane/Leaf surface`; note that the current GOLD tree exposed through OLS lists `Caulosphere`, `Anthosphere`, `Carposphere` and `Phylloplane/Leaf surface` under *Phyllosphere* but no bare `Surface`, while the vendored `data/raw/` extract still carries it. If the curator concludes it is the same concept as `Phylloplane/Leaf surface`, the established disposition is a same-concept merge decision rather than a new definition.

3. **If it is kept as its own concept, the safe record shape is:**
   - `parent_habitats: ENVO:01001001` (plant-associated environment) — the genus, `GROUND_AS_PARENT`; broader, and asserts only what the source asserts;
   - `relation: xref` to `ENVO:01001032` (the EMPO "Plant surface" mapping target — link preserved without adopting the biofilm claim), and to `PO:0000022` 'plant cuticle' / `PO:0025388` 'epicuticular wax' as the dominant surface materials;
   - **no** grounding to `PO:0006016`/`PO:0005679` (tissue, and leaf-specific), **no** re-use of `UBERON:0002416`;
   - term-request candidate label: *aerial plant surface environment* (or *phyllosphere*, if filed jointly with the parent record).

**Sources:** [Ruinen 1956](https://doi.org/10.1038/177220a0) · [Lindow & Brandl 2003](https://doi.org/10.1128/AEM.69.4.1875-1883.2003) · [Vorholt 2012](https://doi.org/10.1038/nrmicro2910) · [Doan & Leveau 2015](https://doi.org/10.1094/PHYTO-02-15-0050-RVW) · [Bringel & Couée 2015](https://doi.org/10.3389/fmicb.2015.00486) · [Thompson et al. 2017](https://doi.org/10.1038/nature24621) · [Remus-Emsermann & Schlechter 2018](https://doi.org/10.1111/nph.15054) · [Sahu et al. 2022](https://doi.org/10.1002/jobm.202100462) · [Mukherjee et al. 2023](https://doi.org/10.1093/nar/gkac974) · [Rangel & Leveau 2024](https://doi.org/10.1007/s00253-024-13042-4) · [Thomas et al. 2024](https://doi.org/10.1186/s12915-024-01967-1) · [Sugimoto et al. 2026](https://doi.org/10.1093/jxb/erag255) · [Yeats & Rose 2013](https://doi.org/10.1104/pp.113.222737) · [EMPO](https://earthmicrobiome.org/protocols-and-standards/empo/) · [MIxS plant-associated package](https://www.ncbi.nlm.nih.gov/biosample/docs/packages/MIMS.me.plant-associated.6.0/) · [ENVO on OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo) · [ENVO/MIxS wiki](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS) · [envo#1029](https://github.com/EnvironmentOntology/envo/issues/1029) · [GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)

## Citations

1. https://www.ebi.ac.uk/ols4/api/v2/ontologies/gold/classes?search=phyllosphere
2. https://doi.org/10.1093/nar/gkac974
3. https://doi.org/10.1038/177220a0
4. https://leveau.ucdavis.edu/wp-content/uploads/sites/220/2019/07/Leveau2006a.pdf
5. https://doi.org/10.1128/AEM.69.4.1875-1883.2003
6. https://doi.org/10.1094/PHYTO-02-15-0050-RVW
7. https://doi.org/10.1002/jobm.202100462
8. https://escholarship.org/content/qt05n539tv/qt05n539tv.pdf
9. https://doi.org/10.1038/nrmicro2910
10. https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001032
11. https://doi.org/10.1038/nature24621
12. https://earthmicrobiome.org/protocols-and-standards/empo/
13. https://github.com/EnvironmentOntology/envo/issues/1029
14. https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
15. https://doi.org/10.1104/pp.113.222737
16. https://doi.org/10.1186/s12915-024-01967-1
17. https://doi.org/10.1007/s00253-024-13042-4
18. https://doi.org/10.1111/nph.15054
19. https://doi.org/10.1093/jxb/erag255
20. https://doi.org/10.3389/fmicb.2015.00486
21. https://gold.jgi.doe.gov/ecosystem_classification
22. https://www.ncbi.nlm.nih.gov/biosample/docs/packages/MIMS.me.plant-associated.6.0/
23. https://doi.org/10.1038/s41564-022-01266-x
24. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001001
25. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001032
26. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001057
27. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00010504
28. https://doi.org/10.1016/S0007-1536(65
29. https://www.ebi.ac.uk/ols4/ontologies/envo