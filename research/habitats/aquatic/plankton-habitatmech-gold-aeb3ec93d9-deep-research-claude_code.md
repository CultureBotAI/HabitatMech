---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T03:26:10.355277'
end_time: '2026-08-18T03:36:32.495326'
duration_seconds: 622.14
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Plankton
  habitat_identifier: habitatmech:GOLD.aeb3ec93d9
  habitat_category: AQUATIC
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Environmental > Aquatic > Marine > River plume > Plankton'
  assertions: '0'
  parent_terms: ENVO:03600070
  xrefs: mesh:D010933
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term mesh:D010933 'Plankton' attached as a parent. Host-taxon reversal\
    \ (#114): NOT_APPLICABLE on the reasoning that plankton is 'an assemblage of organisms\
    \ rather than a place'. Organisms can be habitats \u2014 plankton hosts epibiotic\
    \ and particle-attached microbial communities, which is a well-described habitat\
    \ distinct from the free-living water column. What is not a place is the TAXON\
    \ TERM, so mesh:D010933 stays an xref (#99) and the concept keeps its own identity.\
    \ NOT_APPLICABLE asserted the concept is not a habitat, which is stronger than\
    \ the evidence and stronger than what was meant. (source concept habitatmech:GOLD.aeb3ec93d9)"
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
  web_search_requests: 10
  num_turns: 25
  total_cost_usd: 2.592488000000001
  session_id: 8378d525-ad99-494d-aa78-dad137da1f90
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 21
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Plankton
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.aeb3ec93d9
- **Category:** AQUATIC
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Environmental > Aquatic > Marine > River plume > Plankton
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** ENVO:03600070
- **Cross-references upstream suggested:** mesh:D010933

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term mesh:D010933 'Plankton' attached as a parent. Host-taxon reversal (#114): NOT_APPLICABLE on the reasoning that plankton is 'an assemblage of organisms rather than a place'. Organisms can be habitats — plankton hosts epibiotic and particle-attached microbial communities, which is a well-described habitat distinct from the free-living water column. What is not a place is the TAXON TERM, so mesh:D010933 stays an xref (#99) and the concept keeps its own identity. NOT_APPLICABLE asserted the concept is not a habitat, which is stronger than the evidence and stronger than what was meant. (source concept habitatmech:GOLD.aeb3ec93d9)

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

# Plankton (habitatmech:GOLD.aeb3ec93d9) — definition research

> **Proposed definition:** A portion of planktonic material which is suspended in the brackish mixing water of a river plume.

If the curator prefers to keep the habitat-hood explicit in the text rather than inherited from the genus, the alternative one-sentence form is:

> A portion of planktonic material which is suspended in the brackish mixing water of a river plume and which is colonised by epibiotic, endobiotic and particle-attached microorganisms.

I recommend the first. The second's second clause is true of *all* planktonic material (§3), so it is not a differentia — it belongs in a comment, not in the definition.

**Recommended disposition: `GROUND_AS_PARENT` on `ENVO:01000063` 'planktonic material', not `CONFIRM_UNGROUNDED`.** ENVO does have a term for the generic concept, it is already in the vendored slice (`data/raw/ontology_terms.tsv:7570`), and the reason to mint rather than ground outright is the three-way GOLD leaf ambiguity documented in §2.4 — not the absence of a term. The current record's note ("no ontology term fits this concept") is too strong; see §6.

---

## 1. What the concept denotes

### 1.1 The GOLD reading is a sample fraction, not a place

The source path is `Environmental > Aquatic > Marine > River plume > Plankton`. In GOLD's five-level scheme (Ecosystem → Ecosystem Category → Ecosystem Type → Ecosystem Subtype → Specific Ecosystem), the fifth level "refers to a specific feature within that environment" ([GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification); [Mukherjee et al. 2023, *Nucleic Acids Res* 51:D957](https://academic.oup.com/nar/article/51/D1/D957/6786204)). So the Ecosystem Subtype `River plume` carries the *place*, and `Plankton` at the Specific Ecosystem slot names **what was collected from that place** — the suspended living biomass, as recovered by a net tow or by size-fractionated filtration.

This matters for the definition: the concept is not "the water of a river plume" and not "the river plume". It is the **plankton itself, treated as the sampled medium**, in the same way `Sediment` at the same slot denotes sediment rather than the lake it came from.

Concretely, a sample under this concept is a plankton tow, a >3 µm or >5 µm particle-associated filter fraction, or a net-concentrated biomass pellet, taken from the salinity-gradient water mass where river discharge mixes with seawater.

### 1.2 What is inside and what is a neighbouring concept

**Inside:** living drifting organisms of a river plume (phytoplankton, protists, metazoan zooplankton, and the microbiota attached to, inside, and immediately surrounding them), collected together as a portion of material.

**Neighbouring, and explicitly outside:**

| Neighbour | Why it is outside |
|---|---|
| The plume water column itself / free-living bacterioplankton fraction (<0.2–3 µm) | This is the surrounding *medium*, operationally separated from plankton by size filtration. The two fractions are compositionally and functionally distinct — see §3. |
| `ENVO:03600070` river plume | The *place* (an oceanic front), one level up in the source path. |
| Marine snow / detritus (`ENVO:01000158`, `ENVO:01001103`) | Non-living aggregated detritus. Overlaps in practice with a net tow but is defined by being dead particulate matter. |
| Seston / particulate organic matter (`ENVO:04000012`) | Living **plus** non-living suspended particulates; strictly broader. |
| Phytoplankton bloom | A distinct GOLD Specific Ecosystem in this same corpus (`gold.ecosystem:5825`, path `Environmental > Aquatic > Marine > Coastal > Phytoplankton bloom`) — an event/state, not a steady-state material. |

### 1.3 Ambiguity of the label

"Plankton" has one relevant reading here, but the word is a **hard homonym** in a microbiology corpus. See §5.2 — the `planktonic cell` / `planktonic growth` sense (free-floating rather than biofilm-associated) is a completely different concept and appears in the vendored slice as `BTO:0003281`.

---

## 2. Genus — the broader kind

### 2.1 The match: `ENVO:01000063` 'planktonic material'

> "A portion of planktonic material is a portion of environmental material primarily composed of plankton."

This is the correct genus and it exists. Its asserted parent is `ENVO:01000155` 'organic material', under `ENVO:00010483` 'environmental material'. It has **no children** in ENVO, so there is no existing narrower marine/estuarine/plume subclass to prefer.

Confirmed present in the vendored slice at `data/raw/ontology_terms.tsv:7570` with label `planktonic material`, so a `GROUND` or `GROUND_AS_PARENT` naming it will pass the label check.

Environmental materials are legitimate habitat groundings in the ENVO/MIxS design — the MIxS `env_medium` slot is explicitly populated from ENVO's environmental-material branch ([Yilmaz et al. 2011, *Nat Biotechnol* 29:415–420, doi:10.1038/nbt.1823](https://doi.org/10.1038/nbt.1823); [Buttigieg et al. 2016, *J Biomed Semantics* 7:57, doi:10.1186/s13326-016-0097-6](https://doi.org/10.1186/s13326-016-0097-6)). So grounding a habitat to a material class is not a category error here; it is the intended usage.

### 2.2 Near-misses in ENVO, and why each fails

| CURIE | Label | Why it is not the match |
|---|---|---|
| `ENVO:03600070` | river plume | The setting, not the concept. Its parent is `ENVO:01000071` 'oceanic front' — a front is a *region*, and planktonic material is not a kind of region. **This has consequences for `parent_habitats` — see §2.3.** |
| `ENVO:01000023` / `ENVO:00000208` | marine pelagic biome / marine pelagic zone | The water column, i.e. the neighbouring free-living concept, and asserts oceanic-basin scale that a river plume does not have. |
| `ENVO:04000012` | particulate organic matter | Broader — includes non-living detritus. |
| `ENVO:01001103` | detritus | "primarily composed of dead particulate matter" — asserts *dead*, which plankton is not. |
| `ENVO:01000158` | marine snow | Narrower and different: detrital aggregate, "continuous shower of mostly organic detritus". |
| `ENVO:01001176` | environment associated with an aquatic invertebrate | Narrower on two counts: only metazoan invertebrates (excludes phytoplankton and protists), and asserts a single determining organism. |
| `ENVO:01000057` | marine algal bloom | An event/accumulation, and asserts one-or-few-species dominance. |
| `ENVO:00002034` | biofilm | Attached to a substratum by definition — the opposite of drifting. |
| `ENVO:01000301` | estuarine water | The right physicochemistry, wrong material — this is water, not plankton. Also a plume is not an estuary. |

**Outside the vendored slice**, for completeness: `MICRO:0001451` 'planktonic environment' exists but carries **no definition** in OLS, and MICRO is not among ENVO/UBERON/FOODON/BTO/PO, so it is not a grounding candidate. `NCBITaxon:1874687` 'marine plankton metagenome' is a metagenome, not a habitat.

### 2.3 A note on the record's current parent

`ENVO:03600070` river plume is currently on the record as the nearest broader term. Under this repo's rule that **`parent_habitats` means *broader***, that is questionable: planktonic material is not a subclass of an oceanic front — it is material *located in* one. The defensible arrangement is:

- `parent_habitats`: `ENVO:01000063` planktonic material (`relation: parent`, genuinely broader)
- `ENVO:03600070` river plume — as `relation: xref`, or retained as a parent only if the corpus deliberately uses setting-as-parent for material records (as it does for `lake sediment` → `lake`). This is a corpus-convention question, not an evidence question, and I flag it rather than resolve it.
- `mesh:D010933` — `relation: xref` only. Confirmed below.

### 2.4 Why mint rather than ground outright

`Plankton` appears as a GOLD Specific Ecosystem under **three** different subtypes in this repo's own extract (`data/raw/gold_ecosystem_paths.tsv`):

| line | path | GOLD id | organisms |
|---|---|---|---|
| 476 | `Environmental > Aquatic > Marine > Oceanic > Plankton` | `gold.ecosystem:5378` | 14 |
| 797 | `Environmental > Aquatic > Freshwater > River > Plankton` | `gold.ecosystem:5346` | 2 |
| 1547 | `Environmental > Aquatic > Marine > River plume > Plankton` | `gold.ecosystem:5367` | 0 |

This is exactly the ambiguous-leaf case in `CLAUDE.md`: grounding all three to `ENVO:01000063` would merge oceanic, riverine and plume plankton into one record with mixed attestations. The shallowest-depth tiebreak does not resolve it either — all three sit at depth 5. So minting with `NARROW` grounding and `planktonic material` as parent is the consistent treatment, and the river-plume instance (0 assertions) is the one with the least independent evidence behind it.

---

## 3. Differentia — what distinguishes it

The genus `planktonic material` is differentiated here by **location in a river plume**, which is not a bare geographic fact: a river plume is a defined physicochemical regime with measurable, characteristic properties.

### 3.1 The plume as a physicochemical regime (observable, measurable)

ENVO's own definition: "An oceanic front in which mixing of river discharge and saline seawater occurs" (`ENVO:03600070`). The measurable differentiae:

- **A steep salinity gradient**, typically 0 → >35 PSU across the plume, which is the primary structuring variable for the resident microbiota. Salinity and depth were the primary drivers of bacterioplankton community structure across the Columbia River coastal margin ([Fortunato et al. 2012, *ISME J* 6:554–563](https://www.nature.com/articles/ismej2011135); [Fortunato & Crump 2015, *PLOS ONE* 10:e0140578, doi:10.1371/journal.pone.0140578](https://doi.org/10.1371/journal.pone.0140578)).
- **Riverine nutrient and turbidity loading**, which produces a characteristic successional sequence along the mixing gradient — coastal diatoms at low salinity once turbidity drops, diatom–diazotroph assemblages at 30–35 PSU where N is depleted but Si, P and Fe persist, and *Trichodesmium* beyond 35 PSU ([Subramaniam et al. 2008, *PNAS* 105:10460–10465, doi:10.1073/pnas.0710279105](https://doi.org/10.1073/pnas.0710279105)).
- **Elevated particle load**, which is what makes the particle-attached fraction — this concept — a large and distinct compartment rather than a marginal one.

### 3.2 Why plankton is a habitat distinct from the surrounding water

This is the claim that justifies the record existing at all, and it is well supported:

- **Particle-attached and free-living fractions are genomically and functionally distinct.** Particle-associated prokaryotes are enriched in extracellular peptidases, carbohydrate-active enzymes, substrate-specific transporters, two-component regulatory systems and secretion systems ([Smith et al. 2013, *Front Microbiol* 4:120, doi:10.3389/fmicb.2013.00120](https://doi.org/10.3389/fmicb.2013.00120)). This was first shown in a river-plume system specifically: [Crump, Armbrust & Baross 1999, *Appl Environ Microbiol* 65(7):3192–3204](https://pubmed.ncbi.nlm.nih.gov/10388719/) partitioned particle-attached from free-living communities across the Columbia River, its estuary and the adjacent coastal ocean.
- **Individual phytoplankton cells carry their own microenvironment.** The phycosphere — the diffusive boundary layer immediately around a phytoplankton cell, described as "the planktonic analogue of the plant rhizosphere" — supports mutualistic, commensal, antagonistic and parasitic bacterial associations governed by exuded metabolites and infochemicals ([Seymour et al. 2017, *Nat Microbiol* 2:17065, doi:10.1038/nmicrobiol.2017.65](https://doi.org/10.1038/nmicrobiol.2017.65)).
- **Zooplankton are discrete microbial habitats**, not just carriers. A copepod and its fecal pellets constitute a "microbial hotspot": starved *Acartia tonsa* carry 10³–10⁴ bacteria per animal, gut-associated bacteria grow at ~0.89 d⁻¹ (faster than average free-living pelagic bacteria), and fecal-pellet bacterial abundance reaches 6.5 × 10⁸ ml⁻¹ ([Tang 2005, *Aquat Microb Ecol* 38:31–40](https://www.int-res.com/abstracts/ame/v38/ame038031)). Copepod guts are additionally **anoxic microenvironments** in an oxygenated water column (Tang et al. 2011, *Limnol Oceanogr* 56:666–672) — a physicochemistry the surrounding water does not have.
- **Plankton surfaces host taxa absent from the free-living fraction**, including human pathogens: *Vibrio cholerae* O1 attaches to the zooplankton and phytoplankton of Bangladesh waters ([Tamplin, Gauzens, Huq, Sack & Colwell 1990, *Appl Environ Microbiol* 56(6):1977–1980](https://pubmed.ncbi.nlm.nih.gov/2383016/)), and zooplankton act as a dispersal vector for hitchhiking bacteria (Grossart et al. 2010, *PNAS* 107:11959–11964).
- **Endosymbiosis makes some plankton an intracellular habitat.** In the Amazon plume, *Richelia intracellularis* lives within the frustule/periplasm of *Hemiaulus* and *Rhizosolenia*; 80–100% of *Hemiaulus* cells carry the symbiont ([Subramaniam et al. 2008](https://doi.org/10.1073/pnas.0710279105); [Hilton et al. 2015, *ISME J* 9:1557–1569](https://academic.oup.com/ismej/article/9/7/1557/7558109)).
- **Aggregate-associated microbial ecology is a standing subdiscipline**: [Simon, Grossart, Schweitzer & Ploug 2002, *Aquat Microb Ecol* 28:175–211, doi:10.3354/ame028175](https://doi.org/10.3354/ame028175); [Alldredge & Silver 1988, *Prog Oceanogr* 20:41–82, doi:10.1016/0079-6611(88)90053-5](https://doi.org/10.1016/0079-6611%2888%2990053-5).

**Inference flag:** the sources above establish (a) that plankton hosts distinct attached/internal microbiota generally, and (b) that river plumes structure microbial communities and that particle-attached/free-living partitioning has been measured in plumes specifically. What I did **not** find is a study framed as "the microbiome of river-plume plankton as such". The differentia "in a river plume" is therefore supported as a *physicochemical* differentia (§3.1, well-cited) rather than as a demonstrated distinct-microbiome differentia. A curator should not write a definition asserting a plume-specific plankton microbiome.

### 3.3 Operational boundary — how the fraction is delimited

Plankton is operationally size-fractionated. The standard scheme is picoplankton 0.2–2 µm, nanoplankton 2–20 µm, microplankton 20–200 µm, mesoplankton 0.2–20 mm ([Sieburth, Smetacek & Lenz 1978, *Limnol Oceanogr* 23(6):1256–1263, doi:10.4319/lo.1978.23.6.1256](https://doi.org/10.4319/lo.1978.23.6.1256)). In practice most "particle-attached vs free-living" studies split at 3 µm or 5 µm. This is worth a comment on the record, because it means **the concept's boundary against the free-living water-column concept is a filter pore size, not a natural kind** — and the split is known to be imperfect, since size-selective filtration misses free-living chemotactic cells that are functionally particle-associated.

---

## 4. Sources

Primary literature and standards, with identifiers verified against PubMed/Crossref/OLS at the time of writing:

| Claim | Source |
|---|---|
| Plankton = drifting organisms not able to swim against currents; term coined by Hensen 1887 | Hensen V. (1887) *Ueber die Bestimmung des Plankton's…*; [Pioneers of plankton research: Victor Hensen, *J Plankton Res* 43(4):507](https://academic.oup.com/plankt/article/43/4/507/6318684) |
| Plankton size classes | [Sieburth, Smetacek & Lenz 1978, *Limnol Oceanogr* 23(6):1256–1263](https://doi.org/10.4319/lo.1978.23.6.1256) |
| Phycosphere as microbial habitat | [Seymour, Amin, Raina & Stocker 2017, *Nat Microbiol* 2:17065](https://doi.org/10.1038/nmicrobiol.2017.65) (PMID 28555622) |
| Copepods/fecal pellets as microbial hotspots | [Tang 2005, *Aquat Microb Ecol* 38:31–40](https://www.int-res.com/abstracts/ame/v38/ame038031) |
| *V. cholerae* attachment to plankton | [Tamplin et al. 1990, *Appl Environ Microbiol* 56(6):1977–1980](https://pubmed.ncbi.nlm.nih.gov/2383016/) |
| Particle-attached vs free-living genomic distinction | [Smith et al. 2013, *Front Microbiol* 4:120](https://doi.org/10.3389/fmicb.2013.00120) (PMID 23750156) |
| Particle-attached vs free-living in a river/estuary/plume system | [Crump, Armbrust & Baross 1999, *Appl Environ Microbiol* 65(7):3192–3204](https://pubmed.ncbi.nlm.nih.gov/10388719/) |
| Salinity/depth structure plume bacterioplankton | [Fortunato et al. 2012, *ISME J* 6:554–563](https://www.nature.com/articles/ismej2011135); [Fortunato et al. 2013, *ISME J* 7:1899–1911, doi:10.1038/ismej.2013.79](https://doi.org/10.1038/ismej.2013.79); [Fortunato & Crump 2015, *PLOS ONE* 10:e0140578](https://doi.org/10.1371/journal.pone.0140578) |
| Plume succession, DDAs, plume physicochemistry | [Subramaniam et al. 2008, *PNAS* 105:10460–10465](https://doi.org/10.1073/pnas.0710279105); [Hilton et al. 2015, *ISME J* 9:1557–1569](https://academic.oup.com/ismej/article/9/7/1557/7558109) |
| Organic aggregates as microbial habitat | [Simon et al. 2002, *Aquat Microb Ecol* 28:175–211](https://doi.org/10.3354/ame028175); [Alldredge & Silver 1988, *Prog Oceanogr* 20:41–82](https://doi.org/10.1016/0079-6611%2888%2990053-5) |
| ENVO term definitions and hierarchy | [OLS4 / ENVO](https://www.ebi.ac.uk/ols4/ontologies/envo); [Buttigieg et al. 2016, *J Biomed Semantics* 7:57](https://doi.org/10.1186/s13326-016-0097-6) |
| `env_medium` is populated from ENVO environmental materials | [Yilmaz et al. 2011, *Nat Biotechnol* 29:415–420](https://doi.org/10.1038/nbt.1823) |
| GOLD five-level path semantics | [GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification); [Mukherjee et al. 2023, *Nucleic Acids Res* 51:D957](https://academic.oup.com/nar/article/51/D1/D957/6786204) |
| MeSH D010933 is a class of organisms, no scope note | [id.nlm.nih.gov/mesh/D010933.json](https://id.nlm.nih.gov/mesh/D010933.json) — tree `B05.080.500`, broader `D059001` 'Aquatic Organisms', introduced 1966, annotation only |

**Explicitly my inference, not a source's claim:**
- That GOLD's Specific-Ecosystem `Plankton` denotes a sampled fraction rather than a place. This follows from GOLD's documented level semantics plus the sibling paths, but no GOLD document says it in those words.
- That "in a river plume" is a sufficient differentia against the other two `Plankton` leaves. It distinguishes them, but as noted in §3.2 no source demonstrates a plume-specific plankton microbiome.

---

## 5. Synonyms and what NOT to conflate

### 5.1 Names in real use for this concept

- plankton; plankton sample; plankton tow; net plankton; bulk plankton
- particle-attached fraction; particle-associated fraction (the microbiological framing of the same material)
- planktonic material (ENVO's label)
- plume plankton; river-plume plankton (context-specific)
- Narrower, do not use as synonyms: phytoplankton, zooplankton, bacterioplankton, picoplankton, nanoplankton, microplankton, mesoplankton

### 5.2 Commonly but wrongly treated as the same thing

1. **`planktonic` in the microbiological sense.** In microbiology, "planktonic" means *free-floating single cells as opposed to biofilm* — a growth mode, not membership in the plankton. `BTO:0003281` 'planktonic cell' and `MCO:0000085` 'planktonic growth' carry this sense. **This is the single most dangerous conflation for this record**, because a keyword match on "plankton" in a microbiology corpus will pull in the wrong sense. Note that BTO's own definition of `planktonic cell` ("A plankton-like cell…") straddles both senses, which makes the trap worse, not better.
2. **Seston / suspended particulate matter / POM** (`ENVO:04000012`). Includes non-living material; broader.
3. **Marine snow / detritus** (`ENVO:01000158`, `ENVO:01001103`). Dead aggregated matter; overlaps a net tow but is a different concept.
4. **The water column / free-living bacterioplankton.** The complementary fraction, not the same one.
5. **Phytoplankton bloom** (`gold.ecosystem:5825` in this corpus). A state/event.
6. **Periphyton, biofilm, epiphyton.** Surface-attached, definitionally not drifting.
7. **Nekton.** Actively swimming; the term Hensen contrasted plankton against.
8. **`mesh:D010933` 'Plankton'.** A MeSH descriptor under 'Aquatic Organisms' — an organism grouping with no scope note. Correctly held as `relation: xref` and **not** as a parent, per the #99 precedent.
9. **`NCBITaxon:1874687` 'marine plankton metagenome' / `NCBITaxon:632957` 'marine plankton environmental sample'.** Sequence-provenance labels, not habitats.

---

## 6. Whether it should be a term at all

**Yes — but the current curator note is wrong in one specific way, and it matters for the decision that gets recorded.**

The note reads "Confirmed UNGROUNDED: no ontology term fits this concept." That is not accurate. `ENVO:01000063` 'planktonic material' fits the generic concept precisely, is already in the vendored slice, and has no children. The correct reason to mint an identifier here is the **three-way GOLD leaf ambiguity** (§2.4), not the absence of a term. Recording it as `CONFIRM_UNGROUNDED` with "no term fits" publishes a claim the ontology contradicts, and it would also lose the `planktonic material` genus link that a `GROUND_AS_PARENT` preserves.

Everything else in the note is right, and I'd endorse it explicitly:

- The host-taxon reversal is correct. Plankton hosts epibiotic, endobiotic and particle-attached microbial communities that are demonstrably distinct from the free-living water column (§3.2, six independent citations). `NOT_APPLICABLE` — reserved for diseases, qualities, processes and procedures — would be the wrong disposition, and `tests/test_decisions.py` would flag a `NOT_APPLICABLE` pointing at an organism term anyway.
- `mesh:D010933` as `xref` rather than `parent` is right, and now has a hard confirmation: MeSH classifies it under `B05.080` 'Aquatic Organisms' with no scope note, i.e. it is a taxonomic/organism grouping, exactly the thing #99 says not to parent to.

**Two honest caveats a curator should weigh before writing the record:**

1. **Zero upstream assertions.** `gold.ecosystem:5367` has 0 organisms, 0 of everything, in this repo's own extract. This is a GOLD path that exists but has never been used. Its two siblings (`5378`, 14 organisms; `5346`, 2) carry all the evidence. If the corpus ever prunes never-attested paths, this is a candidate; if it does not, the record should still exist for path completeness, but its definition should not be written as though it summarises observed data.
2. **The concept is partly a sampling convention.** The boundary between "plankton" and "the water it drifts in" is a filter pore size or a net mesh (§3.3), and that convention is known to misclassify chemotactic free-living cells. This does not make the concept a sampling *artefact* — ENVO already accepts `planktonic material` as a real environmental material, and MIxS `env_medium` is designed for exactly this kind of entity — but the record deserves a comment saying that its extension is operationally delimited, so that a downstream user does not read a sharper boundary into it than exists.

**Sources:**
- [ENVO via OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo) · [Buttigieg et al. 2016, *J Biomed Semantics* 7:57](https://doi.org/10.1186/s13326-016-0097-6)
- [MeSH D010933](https://id.nlm.nih.gov/mesh/D010933.json) · [MeSH D059001 'Aquatic Organisms'](https://id.nlm.nih.gov/mesh/D059001.json)
- [GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification) · [Mukherjee et al. 2023, *Nucleic Acids Res* 51:D957](https://academic.oup.com/nar/article/51/D1/D957/6786204)
- [Sieburth, Smetacek & Lenz 1978](https://doi.org/10.4319/lo.1978.23.6.1256) · [Alldredge & Silver 1988](https://doi.org/10.1016/0079-6611%2888%2990053-5) · [Simon et al. 2002](https://doi.org/10.3354/ame028175)
- [Seymour et al. 2017](https://doi.org/10.1038/nmicrobiol.2017.65) · [Tang 2005](https://www.int-res.com/abstracts/ame/v38/ame038031) · [Tamplin et al. 1990](https://pubmed.ncbi.nlm.nih.gov/2383016/)
- [Crump, Armbrust & Baross 1999](https://pubmed.ncbi.nlm.nih.gov/10388719/) · [Smith et al. 2013](https://doi.org/10.3389/fmicb.2013.00120) · [Fortunato et al. 2013](https://doi.org/10.1038/ismej.2013.79) · [Fortunato & Crump 2015](https://doi.org/10.1371/journal.pone.0140578)
- [Subramaniam et al. 2008](https://doi.org/10.1073/pnas.0710279105) · [Hilton et al. 2015, *ISME J* 9:1557](https://academic.oup.com/ismej/article/9/7/1557/7558109)
- [Yilmaz et al. 2011, MIxS](https://doi.org/10.1038/nbt.1823) · [Pioneers of plankton research: Victor Hensen](https://academic.oup.com/plankt/article/43/4/507/6318684)

## Citations

1. https://gold.jgi.doe.gov/ecosystem_classification
2. https://academic.oup.com/nar/article/51/D1/D957/6786204
3. https://doi.org/10.1038/nbt.1823
4. https://doi.org/10.1186/s13326-016-0097-6
5. https://www.nature.com/articles/ismej2011135
6. https://doi.org/10.1371/journal.pone.0140578
7. https://doi.org/10.1073/pnas.0710279105
8. https://doi.org/10.3389/fmicb.2013.00120
9. https://pubmed.ncbi.nlm.nih.gov/10388719/
10. https://doi.org/10.1038/nmicrobiol.2017.65
11. https://www.int-res.com/abstracts/ame/v38/ame038031
12. https://pubmed.ncbi.nlm.nih.gov/2383016/
13. https://academic.oup.com/ismej/article/9/7/1557/7558109
14. https://doi.org/10.3354/ame028175
15. https://doi.org/10.1016/0079-6611%2888%2990053-5
16. https://doi.org/10.4319/lo.1978.23.6.1256
17. https://academic.oup.com/plankt/article/43/4/507/6318684
18. https://doi.org/10.1038/ismej.2013.79
19. https://www.ebi.ac.uk/ols4/ontologies/envo
20. https://id.nlm.nih.gov/mesh/D010933.json
21. https://id.nlm.nih.gov/mesh/D059001.json