---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T02:15:05.316054'
end_time: '2026-08-18T02:22:39.425057'
duration_seconds: 454.11
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Plankton
  habitat_identifier: habitatmech:GOLD.23cd8889db
  habitat_category: AQUATIC
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Environmental > Aquatic > Freshwater > River > Plankton'
  assertions: '2'
  parent_terms: ENVO:01000297
  xrefs: mesh:D010933
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term mesh:D010933 'Plankton' attached as a parent. Host-taxon reversal\
    \ (#114): NOT_APPLICABLE on the reasoning that plankton is 'an assemblage of organisms\
    \ rather than a place'. Organisms can be habitats \u2014 plankton hosts epibiotic\
    \ and particle-attached microbial communities, which is a well-described habitat\
    \ distinct from the free-living water column. What is not a place is the TAXON\
    \ TERM, so mesh:D010933 stays an xref (#99) and the concept keeps its own identity.\
    \ NOT_APPLICABLE asserted the concept is not a habitat, which is stronger than\
    \ the evidence and stronger than what was meant. (source concept habitatmech:GOLD.23cd8889db)"
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
  total_cost_usd: 2.849147999999999
  session_id: 8db546c4-848f-4d15-a360-6500d21e175f
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 36
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Plankton
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.23cd8889db
- **Category:** AQUATIC
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Environmental > Aquatic > Freshwater > River > Plankton
- **Upstream assertion volume:** 2
- **Nearest broader term already on the record:** ENVO:01000297
- **Cross-references upstream suggested:** mesh:D010933

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term mesh:D010933 'Plankton' attached as a parent. Host-taxon reversal (#114): NOT_APPLICABLE on the reasoning that plankton is 'an assemblage of organisms rather than a place'. Organisms can be habitats — plankton hosts epibiotic and particle-attached microbial communities, which is a well-described habitat distinct from the free-living water column. What is not a place is the TAXON TERM, so mesh:D010933 stays an xref (#99) and the concept keeps its own identity. NOT_APPLICABLE asserted the concept is not a habitat, which is stronger than the evidence and stronger than what was meant. (source concept habitatmech:GOLD.23cd8889db)

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

# Plankton (`habitatmech:GOLD.23cd8889db`) — novel-term research

> **Proposed definition:** A portion of planktonic material which is suspended in and advected by the flowing fresh water of a river channel.

Optional expanded form if the corpus wants the sampling operation encoded: *"…, typically recovered as the net-tow or size-fractionated particulate fraction of river water."* I recommend keeping the one-sentence form above and putting the sampling detail in `comments`, because the operational cut (see §3) varies by study and is not part of what the concept **is**.

**Headline finding for the curator:** the note on this decision says "no ontology term fits this concept," but **ENVO:01000063 `planktonic material` exists, is in this repo's vendored slice, and is a genus-level fit** — it is broader than this concept (it covers marine and lacustrine plankton too), not equal to it. That makes this a `GROUND_AS_PARENT` / NARROW case, not a bare `CONFIRM_UNGROUNDED` anchored only on a MeSH organism-form term. Details in §2 and §6.

---

## 1. What the concept denotes

### The source path pins the reading

GOLD's classification is a five-level hierarchy — Ecosystem → Ecosystem Category → Ecosystem Type → Ecosystem Subtype → **Specific Ecosystem** — where "Specific Ecosystem at the bottom refers to a specific feature within that environment" ([Mukherjee et al., *NAR* 51:D957, 2023](https://academic.oup.com/nar/article/51/D1/D957/6786204); [GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)). So `Environmental > Aquatic > Freshwater > River > Plankton` names *the thing sampled from a freshwater river*, not a kind of river and not a taxon. The sample is a portion of the drifting biomass suspended in river water.

**Inside the concept:** the suspended assemblage of algae, cyanobacteria, protists, micro-metazoans and their associated organic aggregates recovered from the channel of a freshwater river — river phytoplankton (*potamoplankton*) plus riverine zooplankton — **together with the microorganisms attached to, or living inside, those particles and organisms**. That last clause is what makes it a habitat rather than a taxon list.

**Neighbouring concepts, outside it:**

| Neighbour | Why it is not this concept |
|---|---|
| **river water** (`ENVO:01000599`, in the slice; note: **no definition text in the slice**) | The medium. Bulk river water includes the free-living (0.2–3 µm) fraction, which is compositionally distinct from the particle/plankton-attached fraction — see §3. |
| **freshwater river** (`ENVO:01000297`) | The water body / geographic feature that contains the plankton. Currently this record's `parent_habitats` entry — see §6 for why that is a category error under the material reading. |
| **water column** (`ENVO:06105011`) | The container region ("a liquid astronomical body part which vertically spans a water body"), not the suspended matter. |
| **river sediment / biofilm (epilithon)** | Benthic. Rivers' benthic biofilms are a separate, better-studied microbial habitat; benthic taxa do contribute to river plankton, especially in headwaters ([Reynolds & Descy tradition, reviewed in Hydrobiologia 2020](https://link.springer.com/article/10.1007/s10750-020-04300-3)). |
| **marine plankton / river-plume plankton** | Sibling GOLD leaves (`gold.ecosystem:5378`, `gold.ecosystem:5367`) — see §6. |

### Ambiguity — three live readings, do not pick silently

1. **Material reading (recommended):** a portion of planktonic biomass, i.e. the net tow or filter concentrate. This is what ENVO already encodes (`ENVO:01000063` is an *environmental material*, subclass of `ENVO:01000155 organic material` → `ENVO:00010483 environmental material`). It is a place-like thing microbes inhabit and it dissolves the "assemblage of organisms, not a place" objection recorded on this decision, because a *portion of material* is not a taxon.
2. **Pelagic-environment reading:** "plankton" used loosely for the pelagic/water-column zone. **Avoid** — it collapses this record onto `ENVO:01000599 river water` and makes the record a duplicate.
3. **Host/epibiont reading:** the surfaces and interiors of individual plankters as microbial habitat (phycosphere, copepod gut and exoskeleton). Real and well-attested (§3), but as the *whole* denotation it re-imports the taxon problem. Best handled as part of the differentia under reading 1.

Reading 1 with reading 3 as its differentia is what I recommend. **This mapping of the three readings onto the GOLD path is my inference** from GOLD's documented level semantics plus ENVO's existing modelling; no source states it for this GOLD path.

---

## 2. Genus — the broader kind

**Smallest well-established kind: planktonic material.** An ENVO term expresses it exactly:

- **`ENVO:01000063` — *planktonic material***: "A portion of planktonic material is a portion of environmental material primarily composed of plankton." Parent: `ENVO:01000155 organic material`. Present in `data/raw/ontology_terms.tsv:7570`, so it passes the seeder's slice-and-label check. It has **no subclasses in ENVO** — there is no `marine planktonic material` or `freshwater planktonic material`.

Because `ENVO:01000063` is broader than *river* plankton, the correct disposition under this repo's own ambiguous-leaf convention is a minted identity with `ENVO:01000063` as parent at NARROW grounding — the same shape as the "several paths end in Sediment" case in `CLAUDE.md`. It is a genus, not a match.

### Near-misses and why each fails

| Term | Why it is not the genus |
|---|---|
| `ENVO:04000012` **particulate organic matter** | Broader still, and includes non-living particulates with no requirement that plankton dominate. `planktonic material` is the tighter genus. |
| `ENVO:01001103` **detritus** | "primarily composed of dead particulate matter" — asserts death. River plankton is a living assemblage; grounding here would publish a false claim. |
| `ENVO:01000158` **marine snow** | Marine, and specifically sinking detritus from productive surface layers. Wrong realm and wrong process. |
| `ENVO:01001189` **algal material** | **No definition text in the vendored slice**, and it covers only the phytoplankton part — excludes zooplankton, which is where much of the distinctive attached-microbe evidence sits (§3). |
| `ENVO:01000297` **freshwater river** | A water body, not a material. "River plankton *is a* freshwater river" is false as an is-a. Currently the record's only `parent_habitats` entry. |
| `ENVO:06105011` **water column** | A fiat body part of a water body — the container, not the contents. |
| `ENVO:2000004` **algal bloom** / `ENVO:01000057` **marine algal bloom** | A transient *feature* arising from population increase, not the standing assemblage. GOLD keeps `Phytoplankton bloom` as a separate leaf (`gold.ecosystem:5825`), confirming the sources treat these as different. |
| `BTO:0003281` **planktonic cell** | A cell type ("a plankton-like cell"), a single-organism concept, not an environmental portion. |
| `mesh:D010933` **Plankton** | MeSH tree number **B05.080.500 — under *Organism Forms***: "Community of tiny aquatic plants and animals, and photosynthetic bacteria, that are either free-floating or suspended in the water, with little or no power of locomotion." ([MeSH record](https://meshb.nlm.nih.gov/record/ui?ui=D010933)). This is an **organism grouping**, so under this repo's #99 rule it belongs in `relation: xref`, which is where the decision row already puts it — but the `curation_history` prose on the record says it was "attached as a parent," and `parent_habitats` in the YAML holds `ENVO:01000297`, not the MeSH term. The note contradicts itself and the record; worth cleaning up regardless of the grounding outcome. |

---

## 3. Differentia — what distinguishes it

Ordered from most to least defensible as definition material.

### 3a. Freshwater, flowing, short-residence-time setting (the primary differentia)

River plankton differs from lake and marine plankton by a physical regime, not a taxonomy. Algae suspended in river water are constrained by **advective losses** associated with downstream flow, and hydrological factors — discharge, water residence time — are of greater importance to planktonic development in rivers than in lakes (Reynolds & Descy 1996; Reynolds 2000; reviewed in [Hydrobiologia 2020, doi:10.1007/s10750-020-04300-3](https://link.springer.com/article/10.1007/s10750-020-04300-3)). Rivers are typically **turbid and light-limited rather than nutrient-limited** ([Reynolds' Founders' Lecture, 1996](https://www.tandfonline.com/doi/pdf/10.1080/09670269600651271); [Potamoplankton size structure, *L&O* 51:681, 2006](https://aslopubs.onlinelibrary.wiley.com/doi/epdf/10.4319/lo.2006.51.1_part_2.0681)). Persistence of an assemblage in an open, unidirectionally flowing system depends on **retention/"dead" zones and seeding from settled cells** — the mechanism Reynolds proposed to resolve why rivers have plankton at all.

These are observable and measurable (discharge, residence time, turbidity, light attenuation) and they cleanly separate this concept from lacustrine and marine siblings.

### 3b. A microbial habitat distinct from the surrounding water (why it is a habitat at all)

This is the load-bearing evidence that "plankton" names something more than "river water."

- **Columbia River, the canonical freshwater/river case:** particle-attached bacteria (>3 µm) were phylogenetically **distinct from the free-living assemblage (0.2–3 µm)** in the same water; in the estuary, 75% of particle-attached clones were rare or absent in river communities, while ~48% of free-living estuarine clones resembled river or coastal-ocean clones ([Crump, Armbrust & Baross, *AEM* 65:3192–3204, 1999](https://journals.asm.org/doi/abs/10.1128/aem.65.7.3192-3204.1999), PMID [10388721](https://pubmed.ncbi.nlm.nih.gov/10388721/)). Earlier: particle-attached communities were 10–100× more active than free-living and accounted for up to **90% of microbial secondary production** in the estuarine water column (Crump, Baross & Simenstad, *Aquat Microb Ecol* 14:7–18, 1998).
- **River reservoirs / river–reservoir continuum (freshwater, recent):** free-living and particle-attached communities differ in structure, diversity and gene functions, FL driven by dissolved nutrients and PA by particles ([Front. Microbiol. 2022, doi:10.3389/fmicb.2022.986637](https://www.frontiersin.org/articles/10.3389/fmicb.2022.986637/full), [PMC9470832](https://pmc.ncbi.nlm.nih.gov/articles/PMC9470832/)); PA communities show consistently higher α-diversity, "reflecting greater niche availability within organic aggregates," FL dominated by oligotrophs such as the hgcI clade ([*Hydrobiologia*, doi:10.1007/s10750-026-06109-y](https://link.springer.com/article/10.1007/s10750-026-06109-y)).
- **Conceptual statement:** aquatic bacteria "have expanded their living space by efficiently exploiting organic matter point sources such as particles/aggregates and higher organisms," and routine water sampling that targets only the free-living fraction misses this ([Grossart, *Environ Microbiol Rep* 2:706–714, 2010, doi:10.1111/j.1758-2229.2010.00179.x](https://enviromicro-journals.onlinelibrary.wiley.com/doi/10.1111/j.1758-2229.2010.00179.x), PMID [23766274](https://pubmed.ncbi.nlm.nih.gov/23766274/)). This is the single best citation for "plankton is a habitat, not just the organisms."
- **Phytoplankton cells as habitat:** the **phycosphere**, the microscale region immediately surrounding an individual phytoplankton cell, is "the planktonic analogue of the rhizosphere" and is explicitly described as a *unique microbial habitat* ([Seymour, Amin, Raina & Stocker, *Nature Microbiology* 2:17065, 2017, doi:10.1038/nmicrobiol.2017.65](https://www.nature.com/articles/nmicrobiol201765), PMID [28555622](https://pubmed.ncbi.nlm.nih.gov/28555622/)).
- **Zooplankton as habitat:** *Vibrio cholerae* attaches specifically to live copepods, with the **oral region and egg sac most heavily colonised**, and survives longer in their presence; *Pseudomonas* and *E. coli* did not adhere ([Huq et al., *AEM* 45:275–283, 1983, doi:10.1128/aem.45.1.275-283.1983](https://journals.asm.org/doi/10.1128/aem.45.1.275-283.1983), PMID [6337551](https://pubmed.ncbi.nlm.nih.gov/6337551/), [PMC242265](https://pmc.ncbi.nlm.nih.gov/articles/PMC242265)). Copepods and their faecal pellets are framed as "microbial hotspots" (Tang, *Aquat Microb Ecol* 38:31–40, 2005); zooplankton-associated microbiomes have significantly **lower α-diversity than free-living bacterioplankton**, consistent with host specialisation ([Datta et al., *ISME J*, doi:10.1038/s41396-018-0182-1](https://www.nature.com/articles/s41396-018-0182-1); [Carman & Dobbs, *Microsc Res Tech* 37:116–135, 1997](https://academic.oup.com/femsec/article/91/7/fiv064/603964) for epibionts).

**Honest caveat, and it belongs in the record's `comments`:** PA/FL divergence is *not* universal. It has been reported in the Columbia River estuary, Santa Barbara Channel, summer Chesapeake Bay, the northern Adriatic and Lake Constance, but San Francisco Bay and winter Chesapeake Bay found the two fractions similar. Seasonality, hydrology and residence time modulate it (see the [FEMS Victoria Harbor comparison](https://academic.oup.com/femsec/article/61/3/496/464948) for the literature survey). So "distinct from the surrounding water" is a well-supported *tendency*, not a definitional necessity — do not write it into the definition sentence as though it were criterial.

### 3c. Operational / measurable boundary

Plankton samples are defined in practice by a size cut, and the standards record it: **MIxS `size_frac` (MIXS:0000017)**, "the filtering pore size used in sample preparation," e.g. `0-0.22 micrometer` ([GSC MIxS term page](https://genomicsstandardsconsortium.github.io/mixs/0000017/); [Yilmaz et al., *Nat Biotechnol* 29:415–420, 2011, doi:10.1038/nbt.1823](https://www.nature.com/articles/nbt.1823), [PMC3367316](https://pmc.ncbi.nlm.nih.gov/articles/PMC3367316/)). Typical cuts: free-living 0.2–3 µm vs particle-attached >3 µm (Crump 1999); Tara Oceans used pico-nano 0.8–5, nano 5–20, micro 20–180, meso 180–2000 µm with pumps below 5 µm and nets above ([Pesant et al., *Sci Data* 2:150023, 2015, doi:10.1038/sdata.2015.23](https://www.nature.com/articles/sdata201523)). Filtered volume itself biases diversity estimates, which is why both `size_frac` and volume must be recorded ([*PLoS/PMC4451414*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4451414/)).

Useful precedent: Tara Oceans annotated its plankton sampling context with ENVO terms (`ENVO:00002042` surface water, `ENVO:01000326` DCM, `ENVO:00000213` mesopelagic zone), i.e. **ENVO is already the vocabulary of record for plankton sample context** — supporting a term request rather than treating this as un-ontologisable.

---

## 4. Sources

Consolidated, with identifiers. Every factual claim above traces to one of these; the items marked **[inference]** in §1 and §6 are mine.

**Ontology / standards**
- ENVO `ENVO:01000063` planktonic material — https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01000063 (also `data/raw/ontology_terms.tsv:7570`)
- ENVO `ENVO:01000297` freshwater river, `ENVO:01000599` river water, `ENVO:04000012` particulate organic matter, `ENVO:01001103` detritus, `ENVO:01000158` marine snow, `ENVO:06105011` water column — https://www.ebi.ac.uk/ols4/ontologies/envo
- Buttigieg et al., "The environment ontology: contextualising biological and biomedical entities," *J Biomed Semantics* 4:43 (2013) — https://link.springer.com/article/10.1186/2041-1480-4-43; and "The environment ontology in 2016," *J Biomed Semantics* 7:57 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/
- MeSH D010933 *Plankton*, tree B05.080.500 (Organism Forms) — https://meshb.nlm.nih.gov/record/ui?ui=D010933
- GSC MIxS `size_frac` (MIXS:0000017) — https://genomicsstandardsconsortium.github.io/mixs/0000017/ ; Yilmaz et al. 2011, doi:10.1038/nbt.1823 — https://www.nature.com/articles/nbt.1823
- GOLD five-level ecosystem classification: Mukherjee et al., *NAR* 51:D957 (2023), PMID 36318257 — https://academic.oup.com/nar/article/51/D1/D957/6786204 ; GOLD v.8, *NAR* 49:D723 — https://academic.oup.com/nar/article/49/D1/D723/5957166 ; https://gold.jgi.doe.gov/ecosystem_classification

**Primary literature — river/freshwater plankton ecology**
- Reynolds, "Potamoplankters do it on the side" (1996 Founders' Lecture) — https://www.tandfonline.com/doi/pdf/10.1080/09670269600651271
- Reynolds & Descy, "The production, biomass and structure of phytoplankton in large rivers," *Arch. Hydrobiol. Suppl.* (1996); retrospective: *Hydrobiologia* (2020), doi:10.1007/s10750-020-04300-3 — https://link.springer.com/article/10.1007/s10750-020-04300-3
- "Potamoplankton size structure and taxonomic composition," *Limnol. Oceanogr.* 51:681 (2006) — https://aslopubs.onlinelibrary.wiley.com/doi/epdf/10.4319/lo.2006.51.1_part_2.0681

**Primary literature — plankton as microbial habitat**
- Crump, Armbrust & Baross, *AEM* 65:3192–3204 (1999), doi:10.1128/AEM.65.7.3192-3204.1999, PMID 10388721 — https://journals.asm.org/doi/abs/10.1128/aem.65.7.3192-3204.1999
- Crump, Baross & Simenstad, *Aquat Microb Ecol* 14:7–18 (1998)
- Grossart, *Environ Microbiol Rep* 2:706–714 (2010), doi:10.1111/j.1758-2229.2010.00179.x, PMID 23766274 — https://enviromicro-journals.onlinelibrary.wiley.com/doi/10.1111/j.1758-2229.2010.00179.x
- Seymour, Amin, Raina & Stocker, *Nat Microbiol* 2:17065 (2017), doi:10.1038/nmicrobiol.2017.65, PMID 28555622 — https://www.nature.com/articles/nmicrobiol201765 (open PDF: https://stockerlab.ethz.ch/wp-content/uploads/2017/05/100._Seymour_atall.pdf)
- Huq et al., *AEM* 45:275–283 (1983), doi:10.1128/aem.45.1.275-283.1983, PMID 6337551, PMC242265 — https://journals.asm.org/doi/10.1128/aem.45.1.275-283.1983
- Tang, "Copepods as microbial hotspots in the ocean," *Aquat Microb Ecol* 38:31–40 (2005)
- Datta et al., *ISME J* (2018), doi:10.1038/s41396-018-0182-1 — https://www.nature.com/articles/s41396-018-0182-1
- Yungui Plateau canyon river reservoir, *Front. Microbiol.* (2022), doi:10.3389/fmicb.2022.986637 — https://www.frontiersin.org/articles/10.3389/fmicb.2022.986637/full ; PMC9470832 — https://pmc.ncbi.nlm.nih.gov/articles/PMC9470832/
- River–reservoir continuum FL/PA partitioning, *Hydrobiologia*, doi:10.1007/s10750-026-06109-y — https://link.springer.com/article/10.1007/s10750-026-06109-y
- Pearl River Estuary PA vs FL metabolic potential, *Sci Total Environ* — https://www.sciencedirect.com/science/article/abs/pii/S0048969720323731
- Contrasting result (no PA/FL difference in some systems), *FEMS Microbiol Ecol* 61:496 — https://academic.oup.com/femsec/article/61/3/496/464948
- Pesant et al., *Sci Data* 2:150023 (2015), doi:10.1038/sdata.2015.23 — https://www.nature.com/articles/sdata201523

**Reference / etymology**
- Hensen coined "plankton" (1887) from Greek *planktos*, "drifting"; the definition is ecological, not taxonomic — organisms that cannot swim against the current. Holoplankton (whole life cycle planktonic) vs meroplankton (planktonic larval stage only). — https://sciencenotes.org/what-is-plankton-definition-and-examples/ , https://en.wikipedia.org/wiki/Meroplankton , https://en.wikipedia.org/wiki/Holoplankton . *These are tertiary sources; if the etymology enters the definition or a note, replace with Hensen 1887 directly or a marine-biology textbook — `tests/test_decisions.py` will not catch a weak citation, but a reviewer should.*

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- *river plankton*, *riverine plankton*
- *potamoplankton* (strictly the phytoplankton component; the standard limnological term for river plankton)
- *freshwater plankton* (broader — includes lakes)
- *bacterioplankton, particle-attached fraction* (the microbial-ecology framing of the same sampled material)
- *seston* (near-synonym for suspended particulate matter, living + dead — broader; not in ENVO)
- *plankton net tow*, *plankton haul* (the sample, not the concept)

**Commonly but wrongly treated as the same**
- **Plankton ≠ the plankton taxa.** MeSH files *Plankton* under Organism Forms; the taxonomic grouping is not a place. Keep `mesh:D010933` as `relation: xref`.
- **Plankton ≠ river water.** Different operational fractions with demonstrably different communities (Crump 1999; Grossart 2010).
- **Plankton ≠ phytoplankton.** GOLD has a separate `Phytoplankton bloom` leaf; the zooplankton-attached microbiota evidence (Huq 1983; Tang 2005) sits outside the phytoplankton reading.
- **Plankton ≠ plankton bloom.** A bloom is a transient feature (`ENVO:2000004 algal bloom`), not the standing assemblage.
- **Plankton ≠ marine snow / detritus.** Those assert death and/or a marine sinking process.
- **Plankton ≠ periphyton / benthic biofilm.** Attached to substrata, not suspended — a different and much better-characterised river microbial habitat.
- **Plankton ≠ "planktonic" in the biofilm literature.** In `biofilm vs planktonic` usage, "planktonic" means *free-swimming, unattached single cells* — nearly the opposite of the particle-attached fraction that gives this habitat its identity. `BTO:0003281 planktonic cell` carries that sense. This is the most likely source of a wrong automated mapping.

---

## 6. Should it be a term at all? — yes, but the disposition on the record is probably wrong

**It should be a term.** Under the material reading it is a portion of environmental material that hosts a characterisable microbial community; it is not a disease, quality, process, procedure, or bare taxon. The current `CONFIRM_UNGROUNDED` reasoning — reversing an earlier `NOT_APPLICABLE` — reaches the right conclusion about habitat-hood. Three things about the record need the curator's attention:

**(a) `ENVO:01000063 planktonic material` was missed.** The note asserts "no ontology term fits this concept," but the term exists, is in the vendored slice, and is genus-level. The correct shape is `GROUND_AS_PARENT` → `ENVO:01000063` at **NARROW** grounding, with the record keeping its minted identity — exactly the pattern `CLAUDE.md` prescribes for ambiguous GOLD leaves. `CONFIRM_UNGROUNDED` leaves the record with no ontology anchor at all except a MeSH organism-form xref, which is weaker than the evidence supports.

**(b) The tie rule is why this is unclaimed, and it applies to three records, not one.** GOLD has **three** leaves labelled `Plankton`, all at depth 5:

| Record | GOLD path | Assertions |
|---|---|---|
| `habitatmech:GOLD.3fb6b22200` | Environmental > Aquatic > Marine > Oceanic > Plankton | 14 |
| `habitatmech:GOLD.23cd8889db` *(this one)* | Environmental > Aquatic > Freshwater > River > Plankton | 2 |
| `habitatmech:GOLD.aeb3ec93d9` | Environmental > Aquatic > Marine > River plume > Plankton | 0 |

Equal depth means no shallowest winner, so none of them claims a term outright — that part of the current state is the rule working correctly. But all three carry the **byte-identical curation note**, including the same self-contradiction, and whatever is decided here should be applied to all three in the same pass; the marine two take `ENVO:01000063` as parent equally well. **[Inference:** that the tie rule is what produced the UNGROUNDED status here — I read it from `CLAUDE.md` and the path table, not from a decision-log entry.**]**

**(c) `parent_habitats: ENVO:01000297` is an is-a error.** `parent_habitats` means *broader*. "River plankton **is a** freshwater river" is false — the river is where the plankton is, not a kind it belongs to. Under the material reading the parent should be `ENVO:01000063`, with `ENVO:01000297` demoted to `relation: xref` (or retained only as sampling context). The same applies to the sibling records' `ENVO:03600070` and `ENVO:00000207` parents.

**(d) The note contradicts itself and the YAML.** It says mesh:D010933 was "attached as a parent" and then that it "stays an xref"; the decisions row has `xref` and the YAML has it under `xrefs`. Only the prose is wrong, but `tests/test_decisions.py` checks note claims for exactly this class of drift — worth fixing while the record is open.

**Term-request case, if the curator wants one:** ENVO has no subclasses of `planktonic material`. A request for `freshwater planktonic material` (and, symmetrically, `marine planktonic material`) would be well-founded, low-controversy, and would let all three GOLD leaves ground properly rather than sit as minted narrows. Given the upstream volume here is only **2 assertions (unit: ORGANISM)**, the marine sibling at 14 is the better-motivated one to lead such a request with.

## Citations

1. https://academic.oup.com/nar/article/51/D1/D957/6786204
2. https://gold.jgi.doe.gov/ecosystem_classification
3. https://link.springer.com/article/10.1007/s10750-020-04300-3
4. https://meshb.nlm.nih.gov/record/ui?ui=D010933
5. https://www.tandfonline.com/doi/pdf/10.1080/09670269600651271
6. https://aslopubs.onlinelibrary.wiley.com/doi/epdf/10.4319/lo.2006.51.1_part_2.0681
7. https://journals.asm.org/doi/abs/10.1128/aem.65.7.3192-3204.1999
8. https://pubmed.ncbi.nlm.nih.gov/10388721/
9. https://www.frontiersin.org/articles/10.3389/fmicb.2022.986637/full
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC9470832/
11. https://link.springer.com/article/10.1007/s10750-026-06109-y
12. https://enviromicro-journals.onlinelibrary.wiley.com/doi/10.1111/j.1758-2229.2010.00179.x
13. https://pubmed.ncbi.nlm.nih.gov/23766274/
14. https://www.nature.com/articles/nmicrobiol201765
15. https://pubmed.ncbi.nlm.nih.gov/28555622/
16. https://journals.asm.org/doi/10.1128/aem.45.1.275-283.1983
17. https://pubmed.ncbi.nlm.nih.gov/6337551/
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC242265
19. https://www.nature.com/articles/s41396-018-0182-1
20. https://academic.oup.com/femsec/article/91/7/fiv064/603964
21. https://academic.oup.com/femsec/article/61/3/496/464948
22. https://genomicsstandardsconsortium.github.io/mixs/0000017/
23. https://www.nature.com/articles/nbt.1823
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC3367316/
25. https://www.nature.com/articles/sdata201523
26. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4451414/
27. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01000063
28. https://www.ebi.ac.uk/ols4/ontologies/envo
29. https://link.springer.com/article/10.1186/2041-1480-4-43
30. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/
31. https://academic.oup.com/nar/article/49/D1/D723/5957166
32. https://stockerlab.ethz.ch/wp-content/uploads/2017/05/100._Seymour_atall.pdf
33. https://www.sciencedirect.com/science/article/abs/pii/S0048969720323731
34. https://sciencenotes.org/what-is-plankton-definition-and-examples/
35. https://en.wikipedia.org/wiki/Meroplankton
36. https://en.wikipedia.org/wiki/Holoplankton