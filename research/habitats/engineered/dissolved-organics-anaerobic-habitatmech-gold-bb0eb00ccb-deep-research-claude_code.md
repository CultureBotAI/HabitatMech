---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T01:41:22.668056'
end_time: '2026-08-18T01:48:43.715268'
duration_seconds: 441.05
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Dissolved organics (anaerobic)
  habitat_identifier: habitatmech:GOLD.bb0eb00ccb
  habitat_category: ENGINEERED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Engineered > Wastewater > Nutrient removal > Dissolved organics
    (anaerobic)'
  assertions: '3'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Stale-sweep\
    \ review (#84): the variant search reaches PATO:0001456 'anaerobic' by taking\
    \ the parenthetical from 'Dissolved organics (anaerobic)'. A quality is not a\
    \ habitat \u2014 the call already recorded for Acidic, Humid, Arid and the climatic\
    \ zones \u2014 and the habitat here is the wastewater, not its oxygen state. The\
    \ sweep's answer stands; its stated reason no longer does. Path: Engineered >\
    \ Wastewater > Nutrient removal > Dissolved organics (anaerobic) (source concept\
    \ habitatmech:GOLD.bb0eb00ccb)"
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
  web_search_requests: 12
  num_turns: 27
  total_cost_usd: 2.8366964999999995
  session_id: 1e76a71c-38b9-4270-845d-204941211e2d
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 23
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Dissolved organics (anaerobic)
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.bb0eb00ccb
- **Category:** ENGINEERED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Engineered > Wastewater > Nutrient removal > Dissolved organics (anaerobic)
- **Upstream assertion volume:** 3
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Stale-sweep review (#84): the variant search reaches PATO:0001456 'anaerobic' by taking the parenthetical from 'Dissolved organics (anaerobic)'. A quality is not a habitat — the call already recorded for Acidic, Humid, Arid and the climatic zones — and the habitat here is the wastewater, not its oxygen state. The sweep's answer stands; its stated reason no longer does. Path: Engineered > Wastewater > Nutrient removal > Dissolved organics (anaerobic) (source concept habitatmech:GOLD.bb0eb00ccb)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Dissolved organics (anaerobic)** as a microbial habitat, with citations.

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

# Definition research: *Dissolved organics (anaerobic)* — `habitatmech:GOLD.bb0eb00ccb`

## Proposed definition

> **An anaerobic bioreactor which removes dissolved organic matter from a wastewater stream through a fermentative and methanogenic microbial consortium, under conditions lacking both dissolved oxygen and oxidised nitrogen.**

Genus: `ENVO:00002124` *anaerobic bioreactor* — present in the vendored slice (`data/raw/ontology_terms.tsv`, `directly_referenced: TRUE`), so a `GROUND_AS_PARENT` decision naming it will pass `tests/test_decisions.py`'s label check.

One word to consider softening: **"methanogenic."** High-rate anaerobic treatment is defined in the engineering literature by methane recovery, but sulfate-rich industrial streams run sulfidogenically rather than methanogenically, so the strictly defensible phrasing is "*through an anaerobic microbial consortium that mineralises them to biogas*." I recommend keeping "methanogenic" and recording the sulfidogenic exception in the note; that is a judgement call for the curator, and both variants are supported below.

---

## 1. What the concept denotes

**Reading supported by the data: the contents and interior environment of the anaerobic secondary-treatment stage of a wastewater treatment train — the unit in which *soluble* organic matter (soluble COD/BOD) is removed biologically without oxygen.** What a sample is taken from is the reactor's liquid and semi-solid contents: granular or flocculent anaerobic sludge, the sludge-blanket liquor, attached biofilm, or the anaerobically treated liquor itself.

Four pieces of evidence fix this reading, all internal to the source data (`data/raw/gold_ecosystem_paths.tsv`):

1. The node has a paired sibling, **`Engineered > Wastewater > Nutrient removal > Dissolved organics (aerobic)`** (`gold.ecosystem:3829`, HabitatMech `GOLD.17461837d0`). The parenthetical is a **process-condition contrast between two implementations of the same treatment duty**, not a description of a stand-alone chemical fraction.
2. The node carries a `specific_ecosystem` **child**, `… > Dissolved organics (anaerobic) > Activated sludge` (`gold.ecosystem:4259`). GOLD's leaves are the things sampled, and that leaf is a **biomass material** — so the parent is a treatment unit whose contents include sludge, not an analyte.
3. Its siblings under `Nutrient removal` are all named treatment configurations: `Nitrogen removal`, `Nitrogen removal > Anammox`, `Biological phosphorus removal > Activated sludge`, `Biological phosphorus removal > Bioreactor`.
4. GOLD's `Engineered` top-level ecosystem is explicitly for samples "collected from … engineered settings such as bioreactors" ([Mukherjee et al., *NAR* 2023, GOLD v.9, doi:10.1093/nar/gkac974](https://academic.oup.com/nar/article/51/D1/D957/6786204); [GOLD Ecosystem Classification browser](https://gold.jgi.doe.gov/ecosystem_classification)).

**The label is process-designated: it names what the unit removes, not the place.** That is normal for GOLD's Engineered branch and does not make the concept a process. The denotation is a place. This distinction matters because it is the difference between minting a term and recording `NOT_APPLICABLE` (§6).

### Residual ambiguity — state it, do not resolve it silently

- **System vs. material.** "The anaerobic reactor" and "the anaerobic sludge/liquor inside it" are two ENVO-shaped readings of the same GOLD node, and MIxS annotation routinely uses both at once (`env_local_scale` = the reactor, `env_medium` = the sludge). The proposed definition takes the **system** reading because it is the one an existing ENVO genus supports (`ENVO:00002124`) and because GOLD's own child node supplies the material separately. *This choice is my inference from the path structure, not something a source states.*
- **Sensu stricto vs. sensu lato "dissolved."** "Dissolved organics" is operationally defined by filtration, conventionally at 0.45 µm, and that boundary does not cleanly exclude colloids; "truly soluble" COD requires flocculation before filtration ([Mamais et al., *Water Res.* 1993, doi:10.1016/0043-1354(93)90211-Y](https://www.sciencedirect.com/science/article/abs/pii/004313549390211Y); [Wastewater COD characterization review, PMC7804026](https://pmc.ncbi.nlm.nih.gov/articles/PMC7804026/)). Real anaerobic reactors treat the whole influent, particulate fraction included. **Do not write a size threshold into the definition** — the source does not intend an analytical fraction, and a 0.45 µm claim would be an over-specification GOLD never made.

### Boundary

**Inside:** UASB, EGSB and internal-circulation reactors; anaerobic filters; anaerobic contact processes; anaerobic membrane bioreactors (AnMBR); anaerobic ponds/lagoons treating a wastewater stream; expanded-bed and fluidised-bed anaerobic reactors ([van Lier, Mahmoud & Zeeman, "Anaerobic Wastewater Treatment," ch. 16 in *Biological Wastewater Treatment: Principles, Modelling and Design*, IWA Publishing — [free 1st-ed. PDF](https://ocw.tudelft.nl/wp-content/uploads/Chapter_16_-_Anaerobic_Wastewater_Treatment.pdf); [2nd ed., 2020, ISBN 9781789060355](https://iwaponline.com/ebooks/book/791/chapter/1987475/Anaerobic-wastewater-treatment)).

**Outside (neighbouring concepts):**

| Neighbour | Why it is outside |
|---|---|
| `Dissolved organics (aerobic)` (`GOLD.17461837d0`) | Same duty, oxic; the sibling this concept is defined against |
| **Anaerobic sludge digester** / `ENVO:00003965` *anaerobic digester sludge* | Digests **particulate waste sludge** for solids stabilisation — a different feed and a different position in the plant. The single most common conflation (see §5) |
| Anoxic (denitrification) zone | No free O₂ but **nitrate present** — anoxic, not anaerobic, by engineering convention |
| EBPR anaerobic zone (`GOLD.…` *Biological phosphorus removal*) | Genuinely anaerobic, but its function is VFA uptake and P release, not carbon removal |
| `ENVO:00002043` *wastewater treatment plant* | The whole facility, of which this is one unit |
| The influent/effluent water itself (`ENVO:00002001`, `ENVO:06105268`) | The medium entering and leaving, not the treatment environment |

---

## 2. Genus — the broader kind

**Smallest well-established kind: an anaerobic bioreactor used for wastewater treatment.** ENVO expresses the first half of that (`ENVO:00002124`) but has **no class for the second half** — there is no intermediate *anaerobic wastewater treatment reactor* between `ENVO:00002124` and its only wastewater-specific descendant, `ENVO:00002213`.

I checked ENVO exhaustively via OLS4 (`q=anaerobic`, `q=anaerobic wastewater`, and the full hierarchical-descendant set of `ENVO:00002124`). `ENVO:00002124` has exactly three descendants: `ENVO:00002125`, `ENVO:00002211`, `ENVO:00002213`.

### Near-misses and why each fails

| CURIE | Label | Why it is not a match |
|---|---|---|
| **`ENVO:00002124`** | **anaerobic bioreactor** | **The genus.** "A bioreactor in which the contained material is not oxygenated (i.e. void of biologically consequential free oxygen)." Says nothing about wastewater or about removing dissolved organics — it also covers lab dechlorination reactors and solids digesters. Broader, correctly so |
| `ENVO:00002213` | anaerobic sludge blanket reactor | **Narrower** — one design (UASB) among several. Its definition ("treating wastewater through the action of methanogenic microbes") is the closest existing text to what this concept means, which is exactly why grounding here would over-claim a reactor geometry the GOLD node never asserts |
| `ENVO:00002211` | thermophilic anaerobic methanogenic reactor | **Narrower** — commits to thermophily; most anaerobic wastewater treatment is mesophilic or ambient |
| `ENVO:00002125` | anaerobic dechlorinating bioreactor | **Sibling, different duty** (reductive dechlorination of halogenated pollutants). Its definition text is a copied generic bioreactor definition and does not match its label — an upstream defect worth reporting to ENVO, not a reason to use it |
| `ENVO:00003965` | anaerobic digester sludge | Different feed (waste solids), and a **material** rather than a system; no definition in ENVO |
| `ENVO:00002129` | anaerobic sludge | **Material**, undefined in ENVO, silent on origin — could be pond sludge |
| `ENVO:00002046` | activated sludge | **Aerobic** by definition; a material |
| `ENVO:00002001` | waste water | The medium — already this record's grandparent via `nutrient_removal` |
| `ENVO:01000173` | anoxic water | Asserts only O₂ absence; no treatment function, no engineered origin. Its synonym "anaerobic water" makes it a tempting false match |
| `ENVO:03600076` | waste stabilization pond | Overlaps (the first cell of a WSP series is an anaerobic pond) but asserts an earthen impoundment the GOLD node does not |
| `ENVO:03600010` | membrane bioreactor | Orthogonal axis; AnMBR is the intersection, not a parent |
| `ENVO:06105300` | wastewater treatment process | **A process**, not a place |
| `ENVO:01001825` | active anaerobic enrichment culturing unit | Laboratory enrichment, not treatment |
| `PATO:0001456` | anaerobic | **A quality.** This is the false lead the stale sweep followed; the existing curation note is right to reject it |

UBERON, FOODON, PO and BTO have nothing relevant. BTO:0002471 *culture condition:anaerobically-grown cell* is a culture condition, not a habitat.

---

## 3. Differentia — what distinguishes it

Four properties separate this concept from its siblings under *anaerobic bioreactor*. All are observable or measurable, and each maps to a recorded MIxS field, which makes them checkable against real deposited samples ([Yilmaz et al., *Nat. Biotechnol.* 2011, doi:10.1038/nbt.1823](https://www.nature.com/articles/nbt.1823); [MIxS wastewater/sludge package, GSC](https://genomicsstandardsconsortium.github.io/mixs/0016013/)).

**(a) Function — removal of dissolved organic matter from a flowing wastewater stream.** This is the differentia that separates it from anaerobic digestion of solids and from anaerobic dechlorination. MIxS records it directly: `secondary_treatment` (`MIXS:0000351`) is defined as "the process for substantially degrading the biological content of the sewage," and `soluble_org_mat` (`MIXS:0000673`) records the concentration of soluble organics. The literature reports 70–84% *soluble* COD removal in a pilot AnMBR-type reactor on dairy wastewater at ambient temperature ([Dev et al./Trzcinski group, *Front./AEM*-indexed, PMC7082317](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7082317/)) and 86% COD removal in a UASB + anaerobic filter on domestic sewage at 13–28 °C (Chernicharo & Machado 1998, [*Water Sci. Technol.* 38(8–9), doi:10.1016/S0273-1223(98)00708-2](https://www.sciencedirect.com/science/article/abs/pii/S0273122398007082)).

**(b) Redox state — no dissolved O₂ *and* no oxidised nitrogen.** In wastewater engineering "anaerobic" and "anoxic" are distinct operating states: anoxic = no free O₂ but NO₃⁻/NO₂⁻ present as terminal acceptor; anaerobic = neither ([SSI Aeration technical note](https://www.ssiaeration.com/en/news/anoxic-vs-anaerobic-vs-aerobic-wastewater-treatment/); [ALMAWATECH glossary](https://www.almawatech.com/en/waste-water/anoxic/); the convention traces to operator-training texts such as CSU Sacramento's *Advanced Waste Treatment*). Note the genuine terminological clash: microbiologically, denitrification **is** anaerobic respiration, so ENVO's oxygen-only phrasing in `ENVO:00002124` is looser than the engineering sense. Writing "*lacking both dissolved oxygen and oxidised nitrogen*" into the differentia is what keeps this concept distinct from a denitrification basin. MIxS records the state as `oxy_stat_samp` (`MIXS:0000753`) and the nitrate concentration separately.

**(c) Terminal metabolism — a syntrophic consortium ending in methanogenesis, yielding biogas.** The canonical four-stage description (hydrolysis → acidogenesis → acetogenesis → methanogenesis) is codified in [ADM1: Batstone et al., *Water Sci. Technol.* 45(10):65–73, 2002, doi:10.2166/wst.2002.0292](https://iwaponline.com/wst/article/45/10/65/6034/The-IWA-Anaerobic-Digestion-Model-No-1-ADM1). This is what makes the environment a *habitat* with a characteristic community rather than an incidental container: methane recovery, not just COD destruction, is the defining feature of high-rate anaerobic treatment ([van Lier et al., ch. 16, above](https://ocw.tudelft.nl/wp-content/uploads/Chapter_16_-_Anaerobic_Wastewater_Treatment.pdf)).

**(d) Community structure — retained, often granular, slow-growing biomass.** The biomass is physically retained (granules, blanket, biofilm, membrane) because methanogens grow slowly and would otherwise wash out. Granules 1–3 mm across show layered spatial organisation, with *Syntrophobacter*-related cocci in the inner layers and filamentous *Chloroflexi* in the outermost layer of thermophilic granules ([Sekiguchi et al., *Appl. Environ. Microbiol.* 65:1280–1288, 1999, doi:10.1128/aem.65.3.1280-1288.1999](https://journals.asm.org/doi/10.1128/aem.65.3.1280-1288.1999); [Yamada et al., PMC1287668](https://pmc.ncbi.nlm.nih.gov/articles/PMC1287668/)). Communities in these reactors are dominated by *Bacteroidetes*, *Chloroflexi*, *Firmicutes* and candidate phylum KSB3, with organic loading rate a strong structuring variable ([Narihiro et al., soft-drink wastewater reactors, PMC4352018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4352018/)), and they harbour genomically distinctive uncultivated lineages — Atribacteria, Hydrogenedentes, Marinimicrobia — performing fermentative, syntrophic and acetogenic catabolism ([Nobu et al., *ISME J.* 9:1710–1722, 2015, doi:10.1038/ismej.2014.256](https://www.nature.com/articles/ismej2014256)). *This paragraph supports the habitat's distinctiveness; do not put taxon names in the definition* — community composition is loading- and feed-dependent, and a recent study finds no keystone taxon tied to COD removal ([PMC12116630](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12116630/)).

**Not usable as differentia:** temperature (mesophilic, thermophilic and ambient/psychrophilic all occur), reactor geometry (UASB, EGSB, filter, AnMBR, pond), and influent origin (municipal or industrial). Each would over-specify.

---

## 4. Sources

Reference vocabularies and standards
- GOLD ecosystem classification, five-level scheme and `Engineered` ecosystem — Mukherjee et al., *Nucleic Acids Res.* 51(D1):D957, 2023, [doi:10.1093/nar/gkac974](https://academic.oup.com/nar/article/51/D1/D957/6786204); browser at [gold.jgi.doe.gov/ecosystem_classification](https://gold.jgi.doe.gov/ecosystem_classification). Earlier: GOLD v.7, [doi:10.1093/nar/gky977](https://pubmed.ncbi.nlm.nih.gov/30357420/)
- MIxS wastewater/sludge environmental package (`secondary_treatment` MIXS:0000351, `reactor_type` MIXS:0000350, `soluble_org_mat` MIXS:0000673, `oxy_stat_samp` MIXS:0000753, `sewage_type` MIXS:0000215) — [GSC MIxS 0016013](https://genomicsstandardsconsortium.github.io/mixs/0016013/); Yilmaz et al., *Nat. Biotechnol.* 29:415–420, 2011, [doi:10.1038/nbt.1823](https://www.nature.com/articles/nbt.1823)
- ENVO term definitions and hierarchy — queried via OLS4 (`ebi.ac.uk/ols4/api`); Buttigieg et al., *J. Biomed. Semantics* 7:57, 2016, [doi:10.1186/s13326-016-0097-6](https://jbiomedsem.biomedcentral.com/articles/10.1186/s13326-016-0097-6)

Habitat and process
- van Lier, Mahmoud & Zeeman, "Anaerobic Wastewater Treatment," ch. 16 in Chen, Ekama, van Loosdrecht & Brdjanovic (eds.), *Biological Wastewater Treatment: Principles, Modelling and Design*, 2nd ed., IWA Publishing 2020, pp. 701–756, ISBN 9781789060355 — [IWA](https://iwaponline.com/ebooks/book/791/chapter/1987475/Anaerobic-wastewater-treatment); [free 1st-ed. PDF, TU Delft OCW](https://ocw.tudelft.nl/wp-content/uploads/Chapter_16_-_Anaerobic_Wastewater_Treatment.pdf)
- Batstone et al., ADM1, *Water Sci. Technol.* 45(10):65–73, 2002, [doi:10.2166/wst.2002.0292](https://iwaponline.com/wst/article/45/10/65/6034/The-IWA-Anaerobic-Digestion-Model-No-1-ADM1)
- Chernicharo & Machado, UASB + anaerobic filter on domestic sewage, *Water Sci. Technol.* 1998, [doi:10.1016/S0273-1223(98)00708-2](https://www.sciencedirect.com/science/article/abs/pii/S0273122398007082)
- Soluble/particulate COD fractionation and the 0.45 µm convention — Mamais et al., *Water Res.* 27(1):195–197, 1993, [doi:10.1016/0043-1354(93)90211-Y](https://www.sciencedirect.com/science/article/abs/pii/004313549390211Y); [COD characterization review, PMC7804026](https://pmc.ncbi.nlm.nih.gov/articles/PMC7804026/)

Microbial community
- Sekiguchi et al., *Appl. Environ. Microbiol.* 65:1280–1288, 1999, [doi:10.1128/aem.65.3.1280-1288.1999](https://journals.asm.org/doi/10.1128/aem.65.3.1280-1288.1999)
- Nobu et al., *ISME J.* 9:1710–1722, 2015, [doi:10.1038/ismej.2014.256](https://www.nature.com/articles/ismej2014256) — PMID 25615435
- Narihiro et al., anaerobic reactors on soft-drink wastewater, [PMC4352018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4352018/)
- Ambient-temperature dairy-wastewater reactor, 70–84% soluble COD removal, [PMC7082317](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7082317/)
- No keystone taxon for COD removal, [PMC12116630](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12116630/)
- AD MAG compendium (11,831 MAGs, 4,568 species, 314 metagenomes) — *Environmental Microbiome* 2023, [doi:10.1186/s40793-023-00545-2](https://environmentalmicrobiome.biomedcentral.com/articles/10.1186/s40793-023-00545-2); Campanaro et al., *Biotechnol. Biofuels* 2020, [doi:10.1186/s13068-020-01679-y](https://biotechnologyforbiofuels.biomedcentral.com/articles/10.1186/s13068-020-01679-y)
- MiDAS 5, global diversity in anaerobic digesters, [bioRxiv 2023.08.24.554448](https://www.biorxiv.org/content/10.1101/2023.08.24.554448v1.full.pdf)

**Explicitly flagged as my inference, not source-stated:** (i) that the GOLD node denotes the treatment unit/its contents rather than an analytical fraction — inferred from the sibling pair and the `Activated sludge` child; (ii) the choice of the system reading over the material reading; (iii) that ENVO lacks an intermediate *anaerobic wastewater treatment reactor* class — established by exhaustive OLS4 descendant query, but the absence is my reading of the result, not an ENVO statement.

---

## 5. Synonyms and what NOT to conflate

**Names in real use** (for the concept as defined)
- anaerobic secondary treatment; anaerobic biological treatment
- high-rate anaerobic wastewater treatment
- anaerobic COD removal / anaerobic carbon removal / soluble COD removal (anaerobic)
- methanogenic wastewater treatment reactor
- Implementations, not synonyms: UASB, EGSB, IC reactor, anaerobic filter, anaerobic contact process, AnMBR, anaerobic pond/lagoon, anaerobic fluidised bed

**Commonly but wrongly treated as the same thing**

1. **Anaerobic (sludge) digester / `ENVO:00003965` anaerobic digester sludge.** The most frequent conflation, and the one most likely to corrupt this record. A digester stabilises **particulate waste sludge** produced elsewhere in the plant; this concept treats the **dissolved fraction of the wastewater stream** as it flows through. Same biochemistry, different feed and different position in the train. Most of the AD-microbiome literature cited above is *digester* literature and should be cited for metabolism, not for habitat identity.
2. **Anoxic denitrification zone.** Frequently called "anaerobic" in loose usage. Nitrate present ⇒ anoxic; that is a *nitrogen-removal* environment and a different GOLD sibling.
3. **EBPR anaerobic zone.** Truly anaerobic, but its purpose is phosphorus release; GOLD gives it its own subtree (`Biological phosphorus removal`).
4. **`PATO:0001456` *anaerobic*.** A quality of the environment, not the environment. The existing curation note already rejects this, correctly.
5. **`ENVO:06105300` *wastewater treatment process*** and *anaerobic digestion* as a process — processes, not places.
6. **`ENVO:01000173` anoxic water** (synonym "anaerobic water") and **`ENVO:00002045` anaerobic sediment** — natural anoxic environments; no engineered origin, no treatment function.
7. **Septic tanks and anaerobic manure lagoons.** Related anaerobic environments; whether they fall inside depends on whether one counts them as treating "a wastewater stream." *This boundary is genuinely unsettled in the literature* — say so in the note rather than asserting a side.
8. **`BTO:0002471` culture condition: anaerobically-grown cell** — a laboratory culture condition.

---

## 6. Should it be a term at all?

**Yes — but as a `GROUND_AS_PARENT` decision, not a `GROUND`, and not `NOT_APPLICABLE`.**

It denotes a place where microorganisms live and from which samples are taken; it is not a disease, a quality, a process, or a taxon, so `NOT_APPLICABLE` would be wrong. No ENVO term names it, so `GROUND` has no target. Recommended disposition:

- **`GROUND_AS_PARENT` → `ENVO:00002124` *anaerobic bioreactor***, keeping the minted identity `habitatmech:GOLD.bb0eb00ccb`. The concept is genuinely narrower than the ENVO class (which also spans dechlorination reactors and solids digesters), and the parent relation is a true *broader* claim, so it satisfies the `parent_habitats` rule.
- Optionally add **`ENVO:00002213` *anaerobic sludge blanket reactor* as `relation: xref`** — related, but *narrower*, so not a parent.
- **Term-request candidate** for ENVO: *anaerobic wastewater treatment reactor*, the missing intermediate between `ENVO:00002124` and `ENVO:00002213`. Adding it would also give `ENVO:00002211` and the aerobic sibling somewhere coherent to sit.

Three caveats the curator should record in the note, all verifiable against `data/raw/gold_ecosystem_paths.tsv`:

1. **GOLD's placement under `Nutrient removal` is a misnomer.** Removing dissolved organic carbon is **carbon/BOD removal**, not nutrient (N/P) removal, which conventionally means nitrogen and phosphorus. GOLD is using "Nutrient removal" as a loose bucket for biological secondary treatment; the sibling `Nitrogen removal` and `Biological phosphorus removal` nodes are the actual nutrient-removal branches. Do not import the "nutrient" claim into the definition.
2. **The child node `… > Dissolved organics (anaerobic) > Activated sludge` (`gold.ecosystem:4259`) is internally inconsistent.** Activated sludge is by definition an aerated suspended-growth process (`ENVO:00002046`); it cannot be a specific ecosystem of an anaerobic subtype. This is upstream noise, not a signal about what the parent means.
3. **Evidence volume is thin.** 3 organism-level assertions across 2 GOLD node ids (`gold.ecosystem:3830`, `gold.ecosystem:4260`); the aerobic sibling has 0. Volume is a reason to keep the definition minimal and to resist adding taxonomic or performance detail, not a reason to withhold the term — the concept is well-attested in the engineering literature independent of GOLD's sample count.

**Sources:** see §4 for the full list.

## Citations

1. https://academic.oup.com/nar/article/51/D1/D957/6786204
2. https://gold.jgi.doe.gov/ecosystem_classification
3. https://www.sciencedirect.com/science/article/abs/pii/004313549390211Y
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC7804026/
5. https://ocw.tudelft.nl/wp-content/uploads/Chapter_16_-_Anaerobic_Wastewater_Treatment.pdf
6. https://iwaponline.com/ebooks/book/791/chapter/1987475/Anaerobic-wastewater-treatment
7. https://www.nature.com/articles/nbt.1823
8. https://genomicsstandardsconsortium.github.io/mixs/0016013/
9. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7082317/
10. https://www.sciencedirect.com/science/article/abs/pii/S0273122398007082
11. https://www.ssiaeration.com/en/news/anoxic-vs-anaerobic-vs-aerobic-wastewater-treatment/
12. https://www.almawatech.com/en/waste-water/anoxic/
13. https://iwaponline.com/wst/article/45/10/65/6034/The-IWA-Anaerobic-Digestion-Model-No-1-ADM1
14. https://journals.asm.org/doi/10.1128/aem.65.3.1280-1288.1999
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC1287668/
16. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4352018/
17. https://www.nature.com/articles/ismej2014256
18. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12116630/
19. https://pubmed.ncbi.nlm.nih.gov/30357420/
20. https://jbiomedsem.biomedcentral.com/articles/10.1186/s13326-016-0097-6
21. https://environmentalmicrobiome.biomedcentral.com/articles/10.1186/s40793-023-00545-2
22. https://biotechnologyforbiofuels.biomedcentral.com/articles/10.1186/s13068-020-01679-y
23. https://www.biorxiv.org/content/10.1101/2023.08.24.554448v1.full.pdf