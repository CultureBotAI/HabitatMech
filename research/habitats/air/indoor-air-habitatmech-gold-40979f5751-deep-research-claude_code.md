---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T21:25:38.272915'
end_time: '2026-08-17T21:33:05.040524'
duration_seconds: 446.77
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Indoor Air
  habitat_identifier: habitatmech:GOLD.40979f5751
  habitat_category: AIR
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Environmental > Air > Indoor Air'
  assertions: '72'
  parent_terms: ENVO:00002005
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term ENVO:00002005 'air' attached as a parent. Indoor air. kg-microbe's\
    \ mapping table pointed this at ENVO:01000855, which it labels 'indoor air' and\
    \ ENVO labels 'area of mixed forest' \u2014 a different concept, now rejected\
    \ by the label check. No indoor-air term exists in the vendored slice, so this\
    \ is a genuine term request; parented to air. (source concept habitatmech:GOLD.40979f5751)"
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
  num_turns: 39
  total_cost_usd: 3.526729500000001
  session_id: d6b34a1e-5c30-4639-bfc2-ad7e85fa7865
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 24
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Indoor Air
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.40979f5751
- **Category:** AIR
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Environmental > Air > Indoor Air
- **Upstream assertion volume:** 72
- **Nearest broader term already on the record:** ENVO:00002005
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:00002005 'air' attached as a parent. Indoor air. kg-microbe's mapping table pointed this at ENVO:01000855, which it labels 'indoor air' and ENVO labels 'area of mixed forest' — a different concept, now rejected by the label check. No indoor-air term exists in the vendored slice, so this is a genuine term request; parented to air. (source concept habitatmech:GOLD.40979f5751)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Indoor Air** as a microbial habitat, with citations.

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

# Indoor Air — definition research for `habitatmech:GOLD.40979f5751`

> **Proposed definition:** An air which is contained within the interior space of a building or other roofed human construction, and which is thereby separated from the outdoor atmosphere by that structure's envelope.

Genus: `ENVO:00002005` *air*. Differentia: containment inside a built enclosure. This is the same differentia an open ENVO new-term request already proposes ("contained-in some building", [ENVO issue #1179](https://github.com/EnvironmentOntology/envo/issues/1179)), so adopting it keeps HabitatMech's minted term alignable if ENVO ever mints one.

---

## 1. What the concept denotes

**The sampled thing is the gas phase and its suspended particles inside an enclosure** — what a bioaerosol sampler draws through a filter or impactor when it is run in a room. It is not the room, not the building, and not the material that has settled out of it.

Boundary, explicitly:

| Inside the concept | Neighbouring concept |
|---|---|
| Air in dwellings, offices, hospitals, classrooms, barns, cleanrooms | The room / building itself (`ENVO:01000426` *room*, `ENVO:00000073` *building*) |
| Air that has been mechanically conditioned or filtered while remaining in the occupied space | The HVAC device (`ENVO:00002874` *air conditioning unit*, `ENVO:00003968` *air filter*) and its internal biofilm |
| Suspended particulate matter while airborne | Settled house dust — already a separate record, `habitatmech:GOLD.398aeb6c37` (`data/habitats/engineered/dust.yaml`) |
| — | Outdoor/ambient air, upper air (`ENVO:01001711`), free atmosphere (`ENVO:01001712`) |

**The label is not seriously ambiguous, but the source hierarchy is.** GOLD nests *Dust*, *Cattle barn*, *Poultry farm*, *Composting facility*, *Air scrubber* and *Air scrubber > Biofilm* under `Environmental > Air > Indoor Air` (`data/raw/gold_ecosystem_paths.tsv`). Two of those children — *Dust* and *Air scrubber > Biofilm* — are not air at all; GOLD's Air branch here records *where the sample came from*, not what the sample is. The existing Dust record already says exactly this in its curation note. **This matters for the definition:** do not widen the genus to accommodate GOLD's children. Define the parent as air, and let the non-air children stay as separately-identified records that happen to hang off it in GOLD's path tree.

One genuine scope decision for the curator: **vehicle cabins**. ISO 16000-1:2004 explicitly includes "cabins of vehicles and public transport" within the indoor environments it governs, alongside dwellings, workplaces, and public/commercial buildings ([ISO 16000-1:2004 scope](https://www.iso.org/standard/39844.html); restated in [ISO 16000-7:2007](https://www.csagroup.org/store/product/iso_034975/) and [ISO 16000-41:2023](https://www.iso.org/standard/76519.html)). ENVO's proposed differentia ("contained in some building") would exclude them. GOLD's 72 assertions give no direct evidence either way, but its subtypes (barn, poultry house, composting facility) are all buildings. Recommendation: write the definition around a **building or other roofed human construction** and note the ISO reading as a broader alternative rather than silently picking one.

## 2. Genus — the broader kind

**`ENVO:00002005` *air*** is the right genus and is already the record's `parent_habitats` value.

- Definition: "The mixture of gases (roughly 78% nitrogen, 20.95% oxygen, 0.93% argon, 0.038% carbon dioxide, trace amounts of other gases, and a variable amount of water vapor) that surrounds the planet Earth." (OLS4, retrieved 2026-08-17)
- Its own parent is `ENVO:01000797` *gaseous environmental material*.
- It has exactly **two** asserted children: `ENVO:01000676` *contaminated air* and `ENVO:01000828` *humid air*. Both are `air which ...` subclasses, so the genus works syntactically for a third sibling.

**ENVO has no indoor-air term, and no indoor-environment term either.** A full-text OLS4 search of ENVO for `indoor` returns six classes and none is about air: *indoor toilet* (`ENVO:01000425`), *indoor kitchen* (`ENVO:01000421`), *cupboard* (`ENVO:01000595`), *shower fixture* (`ENVO:00000992`… listed as `ENVO:01000992`), *shopping mall* (`ENVO:03501207`), *public toilet* (`ENVO:03501265`). A search for `built environment` in ENVO returns only *urban flooding*. This confirms the curator's note.

The mapping table's target is definitively wrong: **`ENVO:01000855` is "area of mixed forest"** — "An area of a planet's surface primarily covered by forest with a mixture of trees that both lose and retain foliage seasonally…" (OLS4, retrieved 2026-08-17). The parallel error on the sibling *Indoor* record (`ENVO:01000856` = *temperate marginal sea biome*, not *indoor environment*) shows this is a systematic off-by-one in kg-microbe's table, not a one-off.

### Near-misses and why each fails

| Candidate | Why it is not a match |
|---|---|
| `ENVO:00002005` *air* | Broader — this is the genus, not the concept. No containment claim. |
| `ENVO:01000676` *contaminated air* | Asserts contamination; a different axis. Most indoor air samples are not contaminated in ENVO's sense. |
| `ENVO:01000828` *humid air* / `ENVO:01000829` *water vapour saturated air* | Differentiated by water content, not location. Cross-cutting, not equivalent. |
| `ENVO:01001711` *upper air*, `ENVO:01001712` *free atmosphere*, `ENVO:01001682` *air mass* | Outdoor/atmospheric-science subdivisions of the same genus; disjoint from the concept. |
| `ENVO:01000426` *room*, `ENVO:00000073` *building*, `ENVO:01001480` *domestic building*, `ENVO:01000470` *building envelope* | The **container**, not the air. A sample of indoor air is not a sample of a room. These are what the differentia refers to, not the term itself. |
| `ENVO:03600000` *cleanroom* | Narrower **and** asserts engineered particulate control that the 72 GOLD assertions do not. |
| `ENVO:00002874` *air conditioning unit*, `ENVO:00003968` *air filter*, `ENVO:03501208` *air vent* | Devices/artifacts. |
| `mesh:D016902` *Air Pollution, Indoor* ("The contamination of indoor air") | A process/exposure, not a material. Do not adopt. |
| `MIXS:0000169` *room air exchange rate* ("the rate at which outside air replaces indoor air in a given space") | A measurement datum. Useful as the differentia's *measurable correlate*, not as a grounding target. |
| `DOID:2710` *sick building syndrome* | A disease. |

### The strongest external evidence that this is a real, unfilled gap

Two open ENVO issues ask for precisely this term, one of them for precisely this GOLD path:

- **[ENVO #1179, "NTRs: Indoor and outdoor air"](https://github.com/EnvironmentOntology/envo/issues/1179)** — open since 2021-06-15, labelled `GOLD/EBI-MGNIFY`: *"I propose an alternate way to subdivide air. We currently have: […] I can add two classes, indoor and outdoor air, using contained-in some building as differentia."*
- **[ENVO #858, "GOLD/EBI Air terms"](https://github.com/EnvironmentOntology/envo/issues/858)** — open since 2019-08-16, requesting terms for `root > Environmental > Air`, `> Indoor Air`, `> Indoor Air > Dust`, `> Outdoor Air`.

That an ENVO editor proposed this differentia and it has sat unmerged for five years is the best available warrant for both the gap and the wording. (Per your standing rule, I have not filed or commented on anything upstream — flagging these as an existing venue if you later decide to.)

*Caveat:* I could not confirm an active OBO relation CURIE for "contained in" — an OLS4 search of RO for it returned nothing current. If the definition's logical axiom is written out, check the vendored slice for the right property (`BFO:0000050` *part of* or a *located in* relation) rather than assuming `RO:0001018`.

## 3. Differentia — what distinguishes it

The containment clause is the definitional differentia. These are the observable consequences that justify it and would go in the term's comment/elucidation rather than the definition sentence:

**Physical setting and its measurable correlate.** The enclosure imposes a finite, ventilation-limited exchange with outdoor air, measured as air exchange rate — MIxS defines `room air exchange rate` as "the rate at which outside air replaces indoor air in a given space" (`MIXS:0000169`). Measured values in study spaces run around 5.5–6.2 h⁻¹ ([Qian et al. 2012](https://doi.org/10.1111/j.1600-0668.2012.00769.x), *Indoor Air* 22:339–351, PMID 22257156).

**Source mixture — the microbiologically meaningful differentia.** Indoor air's community is outdoor air *plus* an occupant- and building-derived overlay:
- Source apportionment attributes an average of **52% of observed indoor airborne bacteria to outdoor air** and 43% to unidentified sources ([Prussin & Marr 2015](https://doi.org/10.1186/s40168-015-0144-z), *Microbiome* 3:78).
- Eight source categories are recognised: humans, pets, plants, plumbing systems, HVAC systems, mould, dust resuspension, and outdoor air (ibid.).
- Human occupancy alone emits **37 × 10⁶ bacterial and 7.3 × 10⁶ fungal genome copies per person-hour**, ~18% of the bacterial emission from human-skin-associated taxa ([Qian et al. 2012](https://doi.org/10.1111/j.1600-0668.2012.00769.x)).
- Human-associated genera are **more than twice as abundant indoors as outdoors** ([Meadow et al. 2014](https://doi.org/10.1111/ina.12047), *Indoor Air* 24:41–48, PMID 23621155).
- In a controlled chamber, outdoor-derived particles dominated composition, with occupant number and activity a significant but smaller influence ([Adams et al. 2015](https://doi.org/10.1371/journal.pone.0128022), *PLoS ONE* 10(5):e0128022, PMID 26024222).

**Compositional distinctness from outdoor air.** Airborne phylogenetic diversity is **lower** indoors than outdoors; mechanically ventilated rooms are less diverse than window-ventilated ones; and indoor air contains taxa absent or rare outdoors, including relatives of human pathogens, at higher relative abundance under lower airflow and lower relative humidity ([Kembel et al. 2012](https://doi.org/10.1038/ismej.2011.211), *ISME J* 6:1469–1479). The DOE-JGI study behind GOLD's own Air branch concluded indoor air microbes are "not random transients from the surrounding outdoor environments" but include organisms from indoor niches ([Tringe et al. 2008](https://doi.org/10.1371/journal.pone.0001862), *PLoS ONE* 3(4):e1862).

**Characteristic loads.** ~10⁶ bacteria-like and ~10⁵ virus-like particles m⁻³; culturable fungi averaging ~80 CFU m⁻³ and reaching 10⁴ CFU m⁻³ ([Prussin & Marr 2015](https://doi.org/10.1186/s40168-015-0144-z)).

**Physicochemistry.** Ventilation air source, airflow rate, relative humidity and temperature all correlate with community structure ([Kembel et al. 2012](https://doi.org/10.1038/ismej.2011.211)); temperature and PM₂.₅/PM₁₀ are the strongest correlates in a four-season residential survey ([Chen et al. 2024](https://doi.org/10.1016/j.envint.2024.108857), *Environ Int* 190:108857, PMID 38954924).

**Why it is sampled at all** (motivation, not differentia): NHAPS respondents spent **87% of their time in enclosed buildings** and a further ~5.5% in enclosed vehicles ([Klepeis et al. 2001](https://doi.org/10.1038/sj.jea.7500165), *J Expo Anal Environ Epidemiol* 11:231–252, PMID 11477521).

## 4. Sources

Verified in this session unless marked.

**Ontology / vocabulary**
- ENVO via OLS4 API, retrieved 2026-08-17: `ENVO:00002005`, `ENVO:01000797`, `ENVO:01000676`, `ENVO:01000828`, `ENVO:01000855`, `ENVO:01000426`, `ENVO:00000073`, `ENVO:03600000`. Browse: https://www.ebi.ac.uk/ols4/ontologies/envo
- ENVO NTR: https://github.com/EnvironmentOntology/envo/issues/1179 (open, 2021-06-15)
- ENVO GOLD Air terms request: https://github.com/EnvironmentOntology/envo/issues/858 (open, 2019-08-16)
- ENVO definition conventions (genus–differentia, citation requirement): https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions
- MIxS `room air exchange rate` (`MIXS:0000169`) and the BuiltEnvironment package (`MIXS:0016001`): https://genomicsstandardsconsortium.github.io/mixs/
- Glass EM *et al.* (2013) MIxS-BE: a MIxS extension … built environment. *ISME J*. https://doi.org/10.1038/ismej.2013.176
- GOLD 5-level ecosystem classification (source of the path): https://gold.jgi.doe.gov/ecosystem_classification
- MeSH `D016902` *Air Pollution, Indoor*: https://meshb.nlm.nih.gov/record/ui?ui=D016902

**Standards / agencies**
- ISO 16000-1:2004, *Indoor air — Part 1*: https://www.iso.org/standard/39844.html — scope enumerates the indoor environments covered, including vehicle cabins.
- ISO 16000-41:2023: https://www.iso.org/standard/76519.html
- US EPA, *Introduction to Indoor Air Quality*: "the air quality within and around buildings and structures, especially as it relates to the health and comfort of building occupants." https://www.epa.gov/indoor-air-quality-iaq/introduction-indoor-air-quality

**Primary and review literature**
- Tringe SG *et al.* (2008) The airborne metagenome in an indoor urban environment. *PLoS ONE* 3(4):e1862. https://doi.org/10.1371/journal.pone.0001862
- Kembel SW *et al.* (2012) *ISME J* 6:1469–1479. https://doi.org/10.1038/ismej.2011.211
- Qian J *et al.* (2012) *Indoor Air* 22:339–351. https://doi.org/10.1111/j.1600-0668.2012.00769.x
- Meadow JF *et al.* (2014) *Indoor Air* 24:41–48. https://doi.org/10.1111/ina.12047
- Adams RI *et al.* (2015) *PLoS ONE* 10(5):e0128022. https://doi.org/10.1371/journal.pone.0128022 (correction: https://doi.org/10.1371/journal.pone.0133221)
- Prussin AJ II & Marr LC (2015) *Microbiome* 3:78. https://doi.org/10.1186/s40168-015-0144-z
- Gilbert JA & Stephens B (2018) *Nat Rev Microbiol* 16:661–670. https://doi.org/10.1038/s41579-018-0065-5 (PMID 30127345)
- Chen Y *et al.* (2024) *Environ Int* 190:108857. https://doi.org/10.1016/j.envint.2024.108857
- Height-resolved indoor airborne microbiome vs floor dust; shoe-sole dust contributes ~4% of airborne bacteria, ~14% of airborne fungi. *Environ Sci Technol* (2024). https://doi.org/10.1021/acs.est.4c06218
- Šunić *et al.* (2026) The indoor microbiome: sampling, analysis and emerging trends. *Environ Microbiol Rep*. https://doi.org/10.1111/1758-2229.70272 — most recent synthesis; notes persistent methodological non-comparability across studies.

**Explicitly my inference, not any source's statement:**
1. That the definition's genus should be `ENVO:00002005` rather than a room/building class. (ENVO #1179's author independently proposes air as the genus, which corroborates it, but no source states it as a rule.)
2. That GOLD's *Dust* and *Air scrubber > Biofilm* children should not widen this term's genus. This is a HabitatMech curation judgement, already recorded on the Dust record.
3. The building-vs-vehicle-cabin recommendation. ISO and ENVO #1179 disagree; I am recommending, not reporting.
4. The claim that ENVO contains no indoor-air term is from a lexical OLS4 search on labels and definitions — strong evidence, but not the same as an editor's statement. The two open NTRs make it near-certain.

## 5. Synonyms and what not to conflate

**Names in real use for this concept**
- indoor air *(ISO 16000 series title; EPA; GOLD)*
- indoor air microbiome / indoor airborne microbiome *(Chen et al. 2024; Šunić et al. 2026)*
- built environment air, indoor bioaerosol *(Prussin & Marr 2015; MIxS-BE)*
- room air *(as in MIxS `room air exchange rate`)*
- interior air, ambient indoor air *(common usage)*

**Wrongly treated as the same thing**
- **Indoor dust / house dust / settled dust** — a solid particulate material, not air. Already `habitatmech:GOLD.398aeb6c37`. Airborne and floor-dust communities differ significantly ([ES&T 2024](https://doi.org/10.1021/acs.est.4c06218)).
- **The built environment / indoor environment** — the whole enclosure including surfaces and materials ([Gilbert & Stephens 2018](https://doi.org/10.1038/s41579-018-0065-5)). Indoor air is one compartment of it. Note the sibling record `habitatmech:GOLD.b4e93f5d66` "Indoor" is a *different* GOLD concept entirely (`Engineered > Artificial ecosystem > Water channel system > Indoor`) — do not merge.
- **Indoor air quality (IAQ) / indoor air pollution** — a quality of, or process affecting, the material (`mesh:D016902`). Not the habitat.
- **HVAC / air-handling and air-scrubber interiors and their biofilms** — a source and a distinct habitat with its own aqueous/surface phase. GOLD nests *Air scrubber* here; the corpus already separates it (`data/habitats/engineered/air_scrubber.yaml`).
- **Cleanroom air** — narrower, and carries an engineered-control assertion (`ENVO:03600000`).
- **Sick building syndrome** (`DOID:2710`) — a disease.
- **Outdoor/ambient air** — the sibling, and the single largest *source* (~52%), which is exactly why the two are constantly conflated in source apportionment and must not be in the ontology.

## 6. Should it be a term at all?

**Yes.** It passes every test the corpus applies:

- It is a **place a sample is taken from**, and a material — not a process, quality, disease, taxon or procedure. It is a portion of environmental material with a boundary condition.
- It has a **genus already in ENVO** and a **differentia that is observable and enforceable** (containment by a built enclosure; measurable via air exchange rate).
- It is **distinguishable from its genus by evidence**, not just by name: lower diversity than outdoor air, an occupant-derived overlay >2× outdoor abundance, and taxa rare or absent outdoors ([Kembel 2012](https://doi.org/10.1038/ismej.2011.211); [Meadow 2014](https://doi.org/10.1111/ina.12047); [Tringe 2008](https://doi.org/10.1371/journal.pone.0001862)).
- It carries **72 GOLD assertions** plus a BacDive "Indoor-Air" isolation source that upstream left with an empty mapping (`data/raw/isolation_source_groundings.tsv`) — so the concept is attested twice over.
- **ENVO itself already agrees it is missing**, in two open issues, one of which names this exact GOLD path.

The only substantive open question is the vehicle-cabin boundary in §1. Everything else is settled enough to write the sentence.

## Citations

1. https://github.com/EnvironmentOntology/envo/issues/1179
2. https://www.iso.org/standard/39844.html
3. https://www.csagroup.org/store/product/iso_034975/
4. https://www.iso.org/standard/76519.html
5. https://github.com/EnvironmentOntology/envo/issues/858
6. https://doi.org/10.1111/j.1600-0668.2012.00769.x
7. https://doi.org/10.1186/s40168-015-0144-z
8. https://doi.org/10.1111/ina.12047
9. https://doi.org/10.1371/journal.pone.0128022
10. https://doi.org/10.1038/ismej.2011.211
11. https://doi.org/10.1371/journal.pone.0001862
12. https://doi.org/10.1016/j.envint.2024.108857
13. https://doi.org/10.1038/sj.jea.7500165
14. https://www.ebi.ac.uk/ols4/ontologies/envo
15. https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions
16. https://genomicsstandardsconsortium.github.io/mixs/
17. https://doi.org/10.1038/ismej.2013.176
18. https://gold.jgi.doe.gov/ecosystem_classification
19. https://meshb.nlm.nih.gov/record/ui?ui=D016902
20. https://www.epa.gov/indoor-air-quality-iaq/introduction-indoor-air-quality
21. https://doi.org/10.1371/journal.pone.0133221
22. https://doi.org/10.1038/s41579-018-0065-5
23. https://doi.org/10.1021/acs.est.4c06218
24. https://doi.org/10.1111/1758-2229.70272