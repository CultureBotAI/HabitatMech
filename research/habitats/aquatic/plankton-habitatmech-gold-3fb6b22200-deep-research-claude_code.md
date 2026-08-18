---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T01:07:21.048550'
end_time: '2026-08-18T01:16:43.834276'
duration_seconds: 562.79
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Plankton
  habitat_identifier: habitatmech:GOLD.3fb6b22200
  habitat_category: AQUATIC
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Environmental > Aquatic > Marine > Oceanic > Plankton'
  assertions: '14'
  parent_terms: ENVO:00000207
  xrefs: mesh:D010933
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term mesh:D010933 'Plankton' attached as a parent. Host-taxon reversal\
    \ (#114): NOT_APPLICABLE on the reasoning that plankton is 'an assemblage of organisms\
    \ rather than a place'. Organisms can be habitats \u2014 plankton hosts epibiotic\
    \ and particle-attached microbial communities, which is a well-described habitat\
    \ distinct from the free-living water column. What is not a place is the TAXON\
    \ TERM, so mesh:D010933 stays an xref (#99) and the concept keeps its own identity.\
    \ NOT_APPLICABLE asserted the concept is not a habitat, which is stronger than\
    \ the evidence and stronger than what was meant. (source concept habitatmech:GOLD.3fb6b22200)"
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
  num_turns: 27
  total_cost_usd: 2.9315715000000004
  session_id: 0113386f-5152-4d55-a6fa-45436116ff6b
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 23
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Plankton
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.3fb6b22200
- **Category:** AQUATIC
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Environmental > Aquatic > Marine > Oceanic > Plankton
- **Upstream assertion volume:** 14
- **Nearest broader term already on the record:** ENVO:00000207
- **Cross-references upstream suggested:** mesh:D010933

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term mesh:D010933 'Plankton' attached as a parent. Host-taxon reversal (#114): NOT_APPLICABLE on the reasoning that plankton is 'an assemblage of organisms rather than a place'. Organisms can be habitats — plankton hosts epibiotic and particle-attached microbial communities, which is a well-described habitat distinct from the free-living water column. What is not a place is the TAXON TERM, so mesh:D010933 stays an xref (#99) and the concept keeps its own identity. NOT_APPLICABLE asserted the concept is not a habitat, which is stronger than the evidence and stronger than what was meant. (source concept habitatmech:GOLD.3fb6b22200)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Plankton** as a microbial habitat, with citations.

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

# Plankton (`habitatmech:GOLD.3fb6b22200`) — definition research

> **A portion of planktonic material which is suspended in the water column of an ocean beyond the continental shelf, and whose constituent drifting organisms and organic aggregates are colonised by microbial communities compositionally distinct from the free-living microbiota of the surrounding seawater.**

If the second clause is judged to be a fact *about* the habitat rather than a differentia, the minimal form is: *A portion of planktonic material which is suspended in the water column of an ocean beyond the continental shelf.* The genus alone (`ENVO:01000063` "planktonic material") carries the biotic composition; the marine-oceanic setting is what separates this record from its two GOLD siblings.

---

## 0. Finding that should be settled before the definition is written

**The premise of the recorded note — "no ontology term fits this concept" — is not supported.** ENVO has **`ENVO:01000063` "planktonic material"**, defined as *"A portion of planktonic material is a portion of environmental material primarily composed of plankton"*, an `ENVO:00010483` environmental material under `ENVO:01000155` organic material ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01000063)). It is present in this repo's vendored slice at `data/raw/ontology_terms.tsv:7570`, so nothing needs vendoring to use it.

The likelier explanation for the UNGROUNDED status is the repo's own deliberate ambiguous-leaf rule rather than an ontology gap: **three** GOLD paths end in "Plankton", all at depth 5 —

| GOLD path | record | assertions |
|---|---|---|
| Environmental > Aquatic > Marine > Oceanic > Plankton | `GOLD.3fb6b22200` (this one) | 14 |
| Environmental > Aquatic > Freshwater > River > Plankton | `GOLD.23cd8889db` | 2 |
| Environmental > Aquatic > Marine > River plume > Plankton | `GOLD.aeb3ec93d9` | 0 |

(`data/raw/gold_ecosystem_paths.tsv`, lines 476, 797, 1547.) A tie at the shallowest depth is left unclaimed on purpose, per `CLAUDE.md`. That is a statement about *which* record may claim the term, not that no term exists.

The disposition the evidence supports is therefore **`GROUND_AS_PARENT` on `ENVO:01000063` 'planktonic material'** for all three, each keeping its minted identity — which is also correct on the merits, since "marine oceanic plankton" is genuinely narrower than generic planktonic material. `mesh:D010933` stays an `xref` for the reason already recorded (#99), and `ENVO:00000207` "oceanic zone" should stay as a second parent expressing the setting.

*This paragraph is my reading of repo state plus the ENVO record, not something a source states.*

---

## 1. What the concept denotes

**As a habitat, the thing sampled is the plankton biomass itself** — the drifting organisms and organism-derived aggregates retained from offshore ocean water by a net tow or a size-fractionating filter — *as substrate*, together with the microbiota living on, in and immediately around them. It is a **material**, not a place: the sample is what stays on the mesh, not a volume of water defined by coordinates and depth.

The GOLD sibling structure is the strongest evidence for this reading. Under `Marine > Oceanic`, the other specific ecosystems are places and bulk materials — *Photic zone* (25), *Aphotic zone* (146), *Sediment* (929), *Benthic* (15), *Abyssal plane* (15), *Microbial mats* (3), *Oceanic crust* (3), *Rock*, *Crustal Fluids*, *Oil-contaminated* (11) (`data/raw/gold_ecosystem_paths.tsv`). The water column is already fully covered by the depth-zone siblings, so "Plankton" is not doing the work of naming a water mass; it names the biotic fraction the sampler collected. GOLD's five-level scheme (Ecosystem → Category → Type → Subtype → Specific ecosystem) is described in [Mukherjee et al. 2023, *NAR* 51:D957–D963, doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974). The 14 assertions here are `ORGANISM`-unit — i.e. cultured isolates whose recorded isolation source was plankton.

### Readings the label admits

The label **is** ambiguous, and the ambiguity is worth recording rather than resolving silently:

1. **Plankton biomass as substrate/host** (epibiotic and particle-attached microbiota of phyto- and zooplankton and their aggregates). Supported by the sibling structure above and by the isolate-source semantics. *This is the reading the proposed definition takes.*
2. **Bacterioplankton itself** — i.e. the free-living microbial fraction of seawater, in which case "plankton" collapses onto the oceanic water column and the record largely duplicates `Photic zone` / `Aphotic zone`. This reading cannot be excluded sample-by-sample: microorganisms are themselves plankton, and the free-living/particle-attached split is an *operational* one imposed by filtration ([Grossart 2010, *Environ Microbiol Rep* 2:706–714, doi:10.1111/j.1758-2229.2010.00179.x](https://doi.org/10.1111/j.1758-2229.2010.00179.x)). The field that would disambiguate is MIxS `size_frac` ([MIXS:0000017](https://genomicsstandardsconsortium.github.io/mixs/0000017/)), which GOLD's ecosystem path does not carry.
3. **Plankton as an organism grouping** (the MeSH sense — see §5). Not a place; this is the reading #114 correctly rejected as an identity.

Reading 1 and reading 2 both terminate at *the collected planktonic material*, which is exactly what `ENVO:01000063` denotes; the genus survives the ambiguity even though a per-sample interpretation does not.

### Boundary

**Inside:** living phyto- and zooplankton and their attached/endobiotic microbiota; colonial and aggregate-forming plankton (e.g. *Trichodesmium* colonies); marine snow and detrital aggregates co-retained with the plankton; the immediate solute plume around them (the phycosphere).

**Neighbouring, and outside:** the seawater the plankton drifts in (`ENVO:00002010` saline water; `ENVO:00000207` oceanic zone; `ENVO:00000208` marine pelagic zone); marine snow taken on its own as a detrital aggregate class (`ENVO:01000158`); sinking export once it reaches the seafloor (marine sediment); the GOLD sibling *Marine > Coastal > Phytoplankton bloom*, which names a transient event/water state rather than collected biomass; and any host-associated record keyed on a named plankton taxon (e.g. a copepod or diatom host), which belongs under the organism-as-host pattern, not here.

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01000063` "planktonic material"** — an environmental material primarily composed of plankton. It is the smallest well-established kind that fits, and it has the property the curation history needed: it is a **material entity composed of organisms**, so adopting it makes no taxonomic claim and does not repeat the taxon-as-place error. It sits under `ENVO:00010483` environmental material via `ENVO:01000155` organic material, the same branch that holds sediment and soil — the branch this corpus routinely grounds habitats to.

Caveat on the term's maturity: `ENVO:01000063` has **no children, no synonyms, and no logical definition**, and carries the editor note *"See Issue #251. Awaiting class creation in PCO to attempt logical definitions."* [ENVO issue #251](https://github.com/EnvironmentOntology/envo/issues/251) (open since 12 Sep 2015) is precisely a debate about whether plankton is best modelled as a mass noun, as a PCO community, or as water with an elevated planktonic-community content. So the term is a stub — but a stub with the right genus and the right ontological category, and it is textually defined.

### Near-misses (all checked; all present in the vendored slice)

| Term | Why it is not the match |
|---|---|
| `ENVO:00000207` **oceanic zone** (current parent) | *"The water mass of an ocean that is not above a continental shelf."* A water mass, not the biotic material. Correct as a **setting** parent; wrong as genus — it would make plankton a kind of water body. |
| `ENVO:00000208` marine pelagic zone / `ENVO:01000033` oceanic pelagic zone biome / `ENVO:01000035` oceanic epipelagic zone biome | Zones and biomes: spatial/ecosystem-scale entities. Same category error as above, and the epipelagic terms additionally assert a depth stratum GOLD's path does not. |
| `ENVO:00002010` saline water | The medium, not the material collected. Would erase the sampling distinction that motivates the GOLD leaf. |
| `ENVO:01000158` **marine snow** | *Narrower and different*: detrital aggregates raining from the photic zone. Excludes living plankton; plankton samples contain aggregates but are not reducible to them. |
| `ENVO:04000012` particulate organic matter / `ENVO:01001103` detritus | POM is compositional (organic particulates generally, including non-planktonic and terrigenous material); detritus asserts *dead* matter. Both over- or under-claim relative to "primarily composed of plankton". |
| `ENVO:01001000` environmental system determined by an organism, and its children `ENVO:01001001` plant-associated, `ENVO:01001002` animal-associated, `ENVO:01001041` fungi-associated, `ENVO:01001176` environment associated with an aquatic invertebrate | ENVO's organism-determined environments are keyed on **taxa**. Plankton is a functional/ecological grouping spanning bacteria, archaea, protists, algae and metazoans, so no single one applies and their union is not a class. There is no "plankton-associated environment" term. Usable only if the concept were narrowed to one host lineage — which would lose the record. |
| `mesh:D010933` Plankton | An organism grouping, not an environment — see §5. Correctly held as `xref`. |
| `BTO:0003281` planktonic cell | A cell type, present in the slice; not a habitat. |

---

## 3. Differentia

### 3.1 Against its siblings under the genus — physical setting

Marine, offshore, beyond the continental shelf (`ENVO:00000207`), salinity of open-ocean seawater, and — for the 14 assertions here — no depth stratum specified. This is what separates it from `GOLD.23cd8889db` (freshwater river plankton, parent `ENVO:01000297`) and `GOLD.aeb3ec93d9` (river-plume plankton, parent `ENVO:03600070`, an oceanic front where river discharge mixes with seawater). Setting is not cosmetic here: particle-attached and free-living communities diverge most at low salinity and converge at oceanic salinities ([Liu et al. 2022, *Sci Rep* 12:13882](https://www.nature.com/articles/s41598-022-18274-w)), and coastal/riverine particles are dominated by terrigenous input whereas oceanic particles are biotic in origin.

### 3.2 Operational — how the material is delimited, and therefore measurable

Plankton is delimited by **size-selective capture**, and the cutoff is recordable: MIxS `size_frac` ("size fraction selected", pattern `{float}-{float} {unit}`, [MIXS:0000017](https://genomicsstandardsconsortium.github.io/mixs/0000017/)). The reference implementation is *Tara* Oceans, which fractionated plankton into a virus-enriched (<0.22 µm), a prokaryote-enriched (0.22–1.6 or 0.22–3 µm) and four eukaryote-enriched fractions — pico-nano 0.8–5 µm, nano 5–20 µm, micro 20–180 µm, meso 180–2000 µm — using peristaltic pumps for the small fractions and towed nets for the large ones ([Pesant et al. 2015, *Sci Data* 2:150023, doi:10.1038/sdata.2015.23](https://doi.org/10.1038/sdata.2015.23); [de Vargas et al. 2015, *Science* 348:1261605, doi:10.1126/science.1261605](https://doi.org/10.1126/science.1261605)). Fractions are operational, not taxonomically clean — ~12% of reads in the prokaryote-enriched fraction are eukaryotic — which is the honest caveat to attach to any definition that leans on size.

### 3.3 Biological — why this is a habitat and not just a sample

The microbiota carried on plankton is **compositionally and functionally distinct from the surrounding free-living seawater community**, which is the substantive claim underwriting habitat-hood:

- **General particle-attached vs free-living contrast.** Across the oligotrophic open-ocean water column, sinking-particle-associated microbes are enriched in two-component environmental-sensing systems, extracellular secretion systems for cell–cell interaction, and higher predicted maximal growth efficiencies than free-living bacterioplankton at all depths ([Leu et al. 2022, *mBio* 13:e01569-22, doi:10.1128/mbio.01569-22](https://doi.org/10.1128/mbio.01569-22)). Aggregates function as microbial hot spots with steep internal chemical gradients and elevated hydrolytic activity ([Alldredge & Silver 1988, *Prog Oceanogr* 20:41–82, doi:10.1016/0079-6611(88)90053-5](https://doi.org/10.1016/0079-6611(88)90053-5); [Simon et al. 2002, *Aquat Microb Ecol* 28:175–211, doi:10.3354/ame028175](https://doi.org/10.3354/ame028175)). Colonisation of model marine particles proceeds through rapid, reproducible successions ([Datta et al. 2016, *Nat Commun* 7:11965, doi:10.1038/ncomms11965](https://doi.org/10.1038/ncomms11965)).
- **Phytoplankton surfaces — the phycosphere.** The diffusive microzone around individual phytoplankton cells is the planktonic analogue of the rhizosphere and hosts relationships spanning mutualism to parasitism ([Seymour, Amin, Raina & Stocker 2017, *Nat Microbiol* 2:17065, doi:10.1038/nmicrobiol.2017.65](https://doi.org/10.1038/nmicrobiol.2017.65)). Hosts actively curate it: *Asterionellopsis glacialis* secretes rosmarinic acid that promotes attachment of beneficial bacteria while suppressing opportunists ([Shibl et al. 2020, *PNAS* 117:27445–27455, doi:10.1073/pnas.2012088117](https://doi.org/10.1073/pnas.2012088117)).
- **Colonial plankton as a discrete habitat.** *Trichodesmium* colonies carry epibionts taxonomically distinct from surrounding oligotrophic surface water — 25–76% of colony 16S amplicons are non-*Trichodesmium*, dominated by Bacteroidetes and Alpha-/Gammaproteobacteria, depleted in the streamlined picocyanobacteria that dominate ambient water, and enriched in motility, phosphate/iron acquisition and denitrification genes ([Gradoville et al. 2017, *Front Microbiol* 8:1122, doi:10.3389/fmicb.2017.01122](https://doi.org/10.3389/fmicb.2017.01122); [Frischkorn et al. 2017, *ISME J* 11:2090–2101, doi:10.1038/ismej.2017.74](https://doi.org/10.1038/ismej.2017.74)).
- **Zooplankton as a discrete habitat.** Zooplankton-associated bacteria colonise internal and external surfaces via a large adhesion gene repertoire and metabolise host-derived chitin and taurine, with iron- and phosphorus-metabolism genes underrepresented in ambient water ([De Corte et al. 2018, *Environ Microbiol* 20:492–505, doi:10.1111/1462-2920.13944](https://doi.org/10.1111/1462-2920.13944)). Chitin degradation is a general trait of the copepod-associated community, with copepod-specific phylotypes in Rhodobacteraceae and *Polaribacter* ([Gerdts et al. 2013, *Helgol Mar Res* 67:757–773, doi:10.1007/s10152-013-0361-4](https://doi.org/10.1007/s10152-013-0361-4)). The best-characterised case is *Vibrio cholerae* on copepod chitin, a reservoir association with epidemiological consequences ([Lutz et al. 2013 / Vibrio–zooplankton review, *Microbiol Spectr*, doi:10.1128/microbiolspec.VE-0003-2014](https://doi.org/10.1128/microbiolspec.VE-0003-2014)).

**Suggested measurable annotations for the record** (all observable, none asserted by the definition): `size_frac` cutoff; salinity ≈ 33–37 PSU; offshore/beyond-shelf setting; sampling gear (net mesh vs filter pore); and — if the curator wants one discriminating physicochemical fact — particles are nutrient-enriched relative to the surrounding oligotrophic seawater, which is the mechanism behind the copiotroph enrichment reported above.

---

## 4. Sources

Ontology / standards
- ENVO `ENVO:01000063` planktonic material — https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01000063
- ENVO `ENVO:00000207` oceanic zone — https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_00000207
- ENVO issue #251, "Plankton" (open, 2015-09-12) — https://github.com/EnvironmentOntology/envo/issues/251
- GSC MIxS `size_frac` (MIXS:0000017) — https://genomicsstandardsconsortium.github.io/mixs/0000017/
- MeSH Plankton D010933, scope note and tree number B05.080.500 — https://meshb.nlm.nih.gov/record/ui?ui=D010933 ; parent D059001 "Aquatic Organisms", grandparent D056891 "Organism Forms" (verified via https://id.nlm.nih.gov/mesh/D010933.json)
- Mukherjee S et al. 2023. Twenty-five years of GOLD: v.9. *Nucleic Acids Res* 51:D957–D963. doi:[10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974)

Primary literature
- Alldredge AL & Silver MW 1988. *Prog Oceanogr* 20:41–82. doi:[10.1016/0079-6611(88)90053-5](https://doi.org/10.1016/0079-6611(88)90053-5)
- Simon M, Grossart H-P, Schweitzer B, Ploug H 2002. *Aquat Microb Ecol* 28:175–211. doi:[10.3354/ame028175](https://doi.org/10.3354/ame028175)
- Grossart H-P 2010. Ecological consequences of bacterioplankton lifestyles. *Environ Microbiol Rep* 2:706–714. PMID 23766274. doi:[10.1111/j.1758-2229.2010.00179.x](https://doi.org/10.1111/j.1758-2229.2010.00179.x)
- Gerdts G et al. 2013. The microbiome of North Sea copepods. *Helgol Mar Res* 67:757–773. doi:[10.1007/s10152-013-0361-4](https://doi.org/10.1007/s10152-013-0361-4)
- Pesant S et al. 2015. *Sci Data* 2:150023. PMID 26029378. doi:[10.1038/sdata.2015.23](https://doi.org/10.1038/sdata.2015.23)
- de Vargas C et al. 2015. *Science* 348:1261605. PMID 25999516. doi:[10.1126/science.1261605](https://doi.org/10.1126/science.1261605)
- Sunagawa S et al. 2015. Structure and function of the global ocean microbiome. *Science* 348:1261359. doi:[10.1126/science.1261359](https://doi.org/10.1126/science.1261359)
- Datta MS et al. 2016. *Nat Commun* 7:11965. PMID 27311813. doi:[10.1038/ncomms11965](https://doi.org/10.1038/ncomms11965)
- Seymour JR et al. 2017. *Nat Microbiol* 2:17065. doi:[10.1038/nmicrobiol.2017.65](https://doi.org/10.1038/nmicrobiol.2017.65)
- Gradoville MR et al. 2017. *Front Microbiol* 8:1122. doi:[10.3389/fmicb.2017.01122](https://doi.org/10.3389/fmicb.2017.01122)
- Frischkorn KR et al. 2017. *ISME J* 11:2090–2101. PMID 28534879. doi:[10.1038/ismej.2017.74](https://doi.org/10.1038/ismej.2017.74)
- De Corte D et al. 2018. *Environ Microbiol* 20:492–505. PMID 28967193. doi:[10.1111/1462-2920.13944](https://doi.org/10.1111/1462-2920.13944)
- Shibl AA et al. 2020. *PNAS* 117:27445–27455. doi:[10.1073/pnas.2012088117](https://doi.org/10.1073/pnas.2012088117)
- Leu AO et al. 2022. *mBio* 13:e01569-22. PMID 35862780. doi:[10.1128/mbio.01569-22](https://doi.org/10.1128/mbio.01569-22)
- Liu et al. 2022, free-living and particle-attached communities in a macrotidal estuary. *Sci Rep* 12:13882. https://www.nature.com/articles/s41598-022-18274-w

**Explicitly my inference, not a source's claim:** (a) that GOLD's "Plankton" leaf denotes collected biomass rather than a water mass — inferred from the sibling structure of the path, not from GOLD documentation; (b) that the record's UNGROUNDED status follows from the three-way depth-5 tie rather than an ontology gap; (c) that `ENVO:01000063` is the best available genus. Claims (a) and (c) are judgements a curator should be willing to defend; the underlying facts (sibling list, term existence, slice membership) are verifiable in this repo and OLS.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept:** plankton; planktonic material; plankton biomass; net-tow plankton / net plankton; size-fractionated plankton; plankton-associated microbiome / plankton microbiome; plankton-associated community. Fraction-specific names that fall inside it: picoplankton, nanoplankton, microplankton, mesoplankton; phytoplankton, zooplankton; holoplankton, meroplankton.

**Commonly but wrongly treated as the same thing:**

- **Bacterioplankton.** These are the microbes being surveyed, not the habitat. Using "plankton" for the free-living bacterial fraction makes the habitat identical to seawater and dissolves the concept.
- **Seawater / the water column.** The medium plankton drifts in. Covered by `ENVO:00002010`, `ENVO:00000207`, `ENVO:00000208`. A plankton sample and a water sample from the same station are different materials with demonstrably different communities (§3.3).
- **Marine snow / detritus / POM** (`ENVO:01000158`, `ENVO:01001103`, `ENVO:04000012`). Detrital aggregates; overlapping but not identical, and "detritus" asserts dead matter, which plankton is not.
- **Seston.** All suspended particulate matter, living plus non-living, including mineral particles — broader, and not composed *primarily* of plankton.
- **Phytoplankton bloom** (GOLD `Marine > Coastal > Phytoplankton bloom`). A transient high-biomass state of a water body — an event/condition, not the collected material.
- **The MeSH concept Plankton (D010933).** Scope note: *"Community of tiny aquatic PLANTS and ANIMALS, and photosynthetic BACTERIA, that are either free-floating or suspended in the water, with little or no power of locomotion"*; tree number **B05.080.500**, i.e. under *Aquatic Organisms* → *Organism Forms*. This is an organism grouping in MeSH's own classification and is exactly the thing #99/#114 say must stay an `xref` rather than become an identity or an `is_a` parent.
- **Neuston, nekton, benthos.** Sibling ecological groupings distinguished by locomotion and position; not plankton.
- **A named plankton host taxon** (a copepod species, *Trichodesmium*, a diatom genus). Those are organism-as-host habitats with their own records under the host-associated pattern; "Plankton" is the mixed assemblage, not any one of them.

---

## 6. Should it be a term at all?

**Yes — it is a habitat, and the existing `CONFIRM_UNGROUNDED` reasoning is right that `NOT_APPLICABLE` would over-claim.** Plankton names a physical material that is sampled, that supports resident microbial communities, and whose communities are measurably different from the surrounding water (§3.3). It is not a process, a quality, a disease state or a sampling artefact.

Two qualifications a curator should weigh:

1. **It is partly operational.** The free-living/particle-attached boundary is imposed by filter and mesh cutoffs, and the fractions are not clean ([Pesant 2015](https://doi.org/10.1038/sdata.2015.23); [Grossart 2010](https://doi.org/10.1111/j.1758-2229.2010.00179.x)). That is a reason to record `size_frac` where known and to avoid writing a hard size boundary into the definition — not a reason to withhold the term. Sediment and soil are also operationally delimited at the sampling step.
2. **It is not, strictly, a *novel* concept.** `ENVO:01000063` names the general kind; what is unnamed is only the marine-oceanic specialisation. So the honest disposition is `GROUND_AS_PARENT`, and the ENVO term request (if one is filed) is for a subclass such as *marine planktonic material*, best raised on the already-open [ENVO #251](https://github.com/EnvironmentOntology/envo/issues/251) rather than as a fresh request. A `plankton-associated environment` request under `ENVO:01001000` is the wrong shape: that branch is taxon-keyed, and plankton is a functional grouping spanning three domains.

**Suggested decision row** (one per source concept; the note's `Path:` must match each record's own canonical path):

- `habitatmech:GOLD.3fb6b22200` → `GROUND_AS_PARENT` `ENVO:01000063` "planktonic material", `relation: parent`; retain `ENVO:00000207` "oceanic zone" as setting parent; retain `mesh:D010933` as `xref`.
- Apply the same genus to `GOLD.23cd8889db` (keeping `ENVO:01000297` freshwater river) and `GOLD.aeb3ec93d9` (keeping `ENVO:03600070` river plume); leaving them with only a MeSH parent while this one is grounded would put three identically-argued records in three different states.

## Citations

1. https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01000063
2. https://doi.org/10.1093/nar/gkac974
3. https://doi.org/10.1111/j.1758-2229.2010.00179.x
4. https://genomicsstandardsconsortium.github.io/mixs/0000017/
5. https://github.com/EnvironmentOntology/envo/issues/251
6. https://www.nature.com/articles/s41598-022-18274-w
7. https://doi.org/10.1038/sdata.2015.23
8. https://doi.org/10.1126/science.1261605
9. https://doi.org/10.1128/mbio.01569-22
10. https://doi.org/10.1016/0079-6611(88
11. https://doi.org/10.3354/ame028175
12. https://doi.org/10.1038/ncomms11965
13. https://doi.org/10.1038/nmicrobiol.2017.65
14. https://doi.org/10.1073/pnas.2012088117
15. https://doi.org/10.3389/fmicb.2017.01122
16. https://doi.org/10.1038/ismej.2017.74
17. https://doi.org/10.1111/1462-2920.13944
18. https://doi.org/10.1007/s10152-013-0361-4
19. https://doi.org/10.1128/microbiolspec.VE-0003-2014
20. https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_00000207
21. https://meshb.nlm.nih.gov/record/ui?ui=D010933
22. https://id.nlm.nih.gov/mesh/D010933.json
23. https://doi.org/10.1126/science.1261359