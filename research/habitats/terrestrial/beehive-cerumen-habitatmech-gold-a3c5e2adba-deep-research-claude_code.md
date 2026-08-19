---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T05:13:13.796884'
end_time: '2026-08-18T05:21:21.485603'
duration_seconds: 487.69
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: 'Beehive: Cerumen'
  habitat_identifier: habitatmech:GOLD.a3c5e2adba
  habitat_category: TERRESTRIAL
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Environmental > Terrestrial > Nest > Insects nest > Beehive:
    Cerumen'
  assertions: '0'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Sibling-path
    review (#12): grounding ''Cerumen/Earwax'' made this stale, but UBERON:0002297
    ''cerumen'' is defined as the secretion of apocrine sweat glands in the external
    auditory canal. Beehive cerumen is the wax-and-propolis mixture stingless bees
    build with; they share a word and nothing else. The slice has no term for it.
    Path: Environmental > Terrestrial > Nest > Insects nest > Beehive: Cerumen (source
    concept habitatmech:GOLD.a3c5e2adba)'
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
  web_search_requests: 9
  num_turns: 40
  total_cost_usd: 2.9220830000000007
  session_id: 0a88fc4c-e018-416b-ae9b-1174404d1981
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 17
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Beehive: Cerumen
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.a3c5e2adba
- **Category:** TERRESTRIAL
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Environmental > Terrestrial > Nest > Insects nest > Beehive: Cerumen
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Sibling-path review (#12): grounding 'Cerumen/Earwax' made this stale, but UBERON:0002297 'cerumen' is defined as the secretion of apocrine sweat glands in the external auditory canal. Beehive cerumen is the wax-and-propolis mixture stingless bees build with; they share a word and nothing else. The slice has no term for it. Path: Environmental > Terrestrial > Nest > Insects nest > Beehive: Cerumen (source concept habitatmech:GOLD.a3c5e2adba)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Beehive: Cerumen** as a microbial habitat, with citations.

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

# Beehive: Cerumen — definition research

**Concept:** `habitatmech:GOLD.a3c5e2adba` · GOLD path `Environmental > Terrestrial > Nest > Insects nest > Beehive: Cerumen` (gold.ecosystem:7299) · category TERRESTRIAL · UNGROUNDED · 0 upstream assertions.

## Proposed definition

> An organic material which stingless bees (Apidae: Meliponini) produce by kneading self-secreted beeswax together with plant resins they collect, and which they use to build the brood cells, involucrum, storage pots and internal nest linings of their nests.

Genus term: `ENVO:01000155` *organic material* (in the vendored slice). If the curator prefers the site reading over the material reading, see §2.3 — that is a *second* term, not a rewording of this one.

---

## 1. What the concept denotes

**The material.** Cerumen is the pliable wax–resin composite that stingless bees (tribe Meliponini) build with. The bees secrete beeswax from abdominal wax glands and knead it with plant resins they forage; the resulting mixture is the tribe's primary construction material and is used in essentially every nest structure — brood cells, the laminar sheaths around the brood (involucrum), the food-storage pots for honey and pollen, connecting pillars, and entrance tubes ([Amateur Entomologists' Society glossary](https://www.amentsoc.org/insects/glossary/terms/cerumen/); [Popova et al. 2021, *Foods* 10:997, doi:10.3390/foods10050997](https://pmc.ncbi.nlm.nih.gov/articles/PMC8147412/); [Chuttong et al. 2023, *Foods* 12:3909, doi:10.3390/foods12213909](https://pmc.ncbi.nlm.nih.gov/articles/PMC10648409/); [Jaramillo-Cevallos et al. 2025, *Insects* 16:1079, doi:10.3390/insects16111079](https://pmc.ncbi.nlm.nih.gov/articles/PMC12653277/) — "a malleable structural material that is used by stingless bees to build, repair, adapt and protect their nests").

**As a habitat / what a sample is.** A cerumen sample is a piece of, or a swab of, this material *in situ* in the nest. This is not hypothetical — it is exactly how the microbiology literature samples it:

- Brood-cell wall material was harvested aseptically and explicitly called cerumen in a 16S amplicon survey of *Austroplebeia australis*, *Tetragonula carbonaria* and *T. hockingsi* nest materials (62 samples, BioProject PRJNA896876) ([Kaluza et al./Leonhardt group, *Microbiol. Resour. Announc.* 2023, doi:10.1128/mra.01181-22](https://pmc.ncbi.nlm.nih.gov/articles/PMC10112253/)).
- Fungal symbionts of *Scaptotrigona depilis* were isolated by scraping cerumen from brood cells and plating it (*Monascus ruber* SDCP1, *Candida* sp. SDCP2), separate from the *Zygosaccharomyces* mass growing inside the cell ([Paludo et al. 2019, *PLOS ONE* 14:e0219696, doi:10.1371/journal.pone.0219696](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0219696)).
- Internal nest surfaces — which in Meliponini are cerumen — were swabbed across 12 colonies of four Brazilian species; 31,564 quality-filtered 16S sequences, Proteobacteria 78–96% of reads, with community composition tracking nest construction material (resin/wax builders *F. varia* and *T. angustula* dominated by *Pseudomonas syringae* and *Sphingomonas*; the mud-and-faeces builder *T. spinipes* by *Escherichia coli*, 72.73%) ([Leonhardt-style survey; Nogueira et al. 2021, *PLOS ONE* 16:e0252933, doi:10.1371/journal.pone.0252933](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0252933)).
- Cerumen is also sampled as a residue matrix: 41 samples from storage pots and involucrum across 10 Ecuadorian localities, assayed for glyphosate/AMPA and metals ([*Insects* 2025, doi:10.3390/insects16111079](https://pmc.ncbi.nlm.nih.gov/articles/PMC12653277/)).

**Boundary — inside the concept:** the wax+resin fabric itself, wherever it occurs in the nest (brood cell walls, involucrum, pot walls, pillars, entrance tube). The chemistry differs measurably between these locations but they are all cerumen ([Deyerling et al. 2024, *J. Chromatogr. Open* 5:100164, doi:10.1016/j.jcoa.2024.100164](https://www.sciencedirect.com/science/article/pii/S2772391724000513), which sampled batumen, involucrum and honey-pot cerumen from one *T. carbonaria* hive).

**Boundary — neighbouring concepts, outside:** the *contents* of the structures cerumen forms — honey (`BTO:0000605`, already grounded as `Beehive: Honey`), stored pollen/bee bread (`Beehive: Pollen`), larval food, royal jelly (`FOODON:03301033`) — and the resin-only or resin+soil deposits (propolis, geopropolis, batumen; see §5).

### Ambiguity you must not resolve silently

**(a) Meliponini vs *Apis*.** GOLD's label says "Beehive", whose default reading is *Apis mellifera*, but "cerumen" in this sense is a Meliponini term. Apini build combs of pure wax and deposit resin separately as propolis; Meliponini mix the two ([Popova et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8147412/); [Chuttong et al. 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10648409/)). A wax–propolis composite *does* occur in *A. mellifera*, at comb-cell rims — Raman mapping of *A. m. carnica* comb found a wax–propolis mixture at the rim topped by near-pure propolis, with the two phases chemically distinct rather than emulsified ([Nemec/Rehman et al., *Spectrochim. Acta A*, PMID [12833475](https://pubmed.ncbi.nlm.nih.gov/12833475/)) — but that layer is normally called propolis, not cerumen. **Recommendation:** take the Meliponini reading as the concept and do not assert *Apis* in the definition. GOLD gives no help here: the node carries 0 assertions, so no sample disambiguates it (*my inference from the source table*). Meliponiculture keeps colonies in boxes routinely called hives, so "Beehive: Cerumen" is coherent under the Meliponini reading.

**(b) Material vs site.** "Cerumen" names a substance; a sample taken from a nest is also a place. HabitatMech's category (TERRESTRIAL) and parent (`Insects nest`) push toward the site reading, but the sibling nodes (`Honey`, `Pollen`, `Royal jelly`) are materials. The material reading is the safer primary; see §2.3.

## 2. Genus

### 2.1 Recommended
**`ENVO:01000155` *organic material*** — "Environmental material derived from living organisms and composed primarily of one or more biomacromolecules." Present in the vendored slice. Cerumen is bee-secreted wax plus plant resin, i.e. organism-derived. *Caveat, my inference:* cerumen's constituents are long-chain lipid esters and di-/triterpenoids and phenolics, which are not biomacromolecules in the strict sense, so this genus is a good-enough superclass rather than a tight fit. If that bothers the curator, fall back to `ENVO:00010483` *environmental material* (also in the slice).

### 2.2 Near-misses in ENVO and why each fails

| Term | Why it is not the genus / not a match |
|---|---|
| `UBERON:0002297` *cerumen* | Homonym only. Defined as apocrine gland secretion of the external auditory canal ([UBERON via OLS](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0002297)). The curator note on the record is correct. |
| `ENVO:01000575` *wax* | Narrower on composition — "primarily composed of lipids or other organic compounds that consist of long alkyl chains". Cerumen's defining second component is terpenoid/phenolic plant resin. Using this genus would silently drop the differentia. |
| `ENVO:03510018` *resin* / `PO:0025603` *plant resin* | The foraged ingredient, not the mixture; asserts plant (or synthetic) origin and omits the bee-secreted wax. |
| `ENVO:02000004` *nesting material* | Closest ENVO concept by intent, but asserts a function cerumen only partly has — "materials used to cushion, insulate and protect the young". Cerumen also forms honey and pollen pots and the nest lining. It is also classified under *animal habitation*, i.e. ENVO already blurs material and site here. Over-claims and under-covers. |
| `ENVO:00005803` *animal habitation* | The record's existing grandparent via `Insects nest`. Correct but far too broad to serve as the genus of a specific material. |
| `ENVO:01001813` *construction* | "A material entity assembled through the intentional, instinctual, or deliberately programmed efforts of an organism or machine." Fits cerumen *structures* (pots, involucrum), not the substance. Candidate genus only under the site reading. |
| `ENVO:01000576` *apiary* | A managed site holding hives — two levels of granularity away, and asserts human beekeeping. |
| `FOODON:03302072` *beeswax*, `FOODON:03413010` *beeswax, white and yellow* | Food-additive framing of *Apis* wax; wrong producer framing and no resin. |
| `DRON:00012339` / FoodOn *propolis*, `MeSH:D011429`, `SNOMED:255970007`, AGROVOC `c_15919` | Propolis, not cerumen — see §5. FoodOn's definition is explicitly honey-bee saliva + beeswax + bud exudate. |
| `CHEBI:757496` *propolis wax* | A chemical fraction obtained from propolis, not a nest material. |
| `ENVO:00005804/00005805/2000006/03600069` *nest of ant / bird / termite / alligator* | ENVO's existing nest series — **note there is no bee nest or hive term in it.** An OLS search of ENVO for "hive" and "bee" returns only *apiary*, *beech forest soil* and *mycetome*. |

**Negative checks worth recording:** no ENVO term for a hive, a bee nest, or cerumen-the-material; no AGROVOC concept matching `cerumen*` (AGROVOC does have *propolis*, `c_15919`, so the endpoint was working); no open or closed ENVO GitHub issue mentioning cerumen. There is a real gap here, not a lookup failure.

### 2.3 If the curator wants the site reading instead
It needs its own sentence and its own term, e.g. *"A construction which stingless bees assemble from cerumen and which forms the brood cells, involucrum, storage pots and lining of their nest."* — genus `ENVO:01001813` *construction* or `ENVO:00005803` *animal habitation*. Stating that both a material term and a site term are missing is more useful than trying to make one sentence carry both; ENVO's own material/site split is exactly this distinction.

## 3. Differentia

Observable properties that separate cerumen from its siblings:

1. **Producer and formation process.** Made by Meliponini workers, who mix endogenously secreted wax with exogenously collected plant resin — a two-source composite, unlike pure beeswax comb (Apini) or pure resin deposits ([Popova et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8147412/); [Chuttong et al. 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10648409/)).
2. **Dominant material and chemistry.** Terpenoid-rich rather than flavonoid-rich. In *T. carbonaria* cerumen, GC-MS markers were isopimaric acid (12.23 ± 3.03% w/w), pimaric acid (6.31 ± 0.97%) and gallic acid (5.79 ± 0.81%), with the prenylated phenolics and flavonoids characteristic of *Apis* propolis **absent** ([Massaro et al. 2011, *Naturwissenschaften* 98:329–337, doi:10.1007/s00114-011-0770-7](https://pubmed.ncbi.nlm.nih.gov/21347735/)). *M. ferruginea* cerumen was dominated by carbohydrates and triterpenes, with the sugar alcohols arabitol and mannitol present ([Popova et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8147412/)). Indian *T. iridipennis* cerumen is a "gallic acid–naringin" type ([Layek et al. 2024, in *Stingless Bee Nest Cerumen and Propolis* Vol. 2, doi:10.1007/978-3-031-43887-5_9](https://link.springer.com/chapter/10.1007/978-3-031-43887-5_9)).
3. **Physical state.** Malleable/pliable at nest temperature and structurally load-bearing ([*Insects* 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12653277/)).
4. **Location and function within the nest.** Forms brood cells, involucrum, storage pots, pillars, entrance tubes — i.e. it is the fabric, not the contents.
5. **Antimicrobial/antioxidant character of the resin fraction.** Cerumen extracts inhibited 5-lipoxygenase at IC50 19.97 ± 2.67 µg/mL, comparable to Trolox (12.78 ± 1.82) but weaker than honeybee propolis (5.90 ± 0.62) ([Massaro et al. 2011](https://pubmed.ncbi.nlm.nih.gov/21347735/)). Antioxidant capacity varies by nest structure: FRAP 5.19–16.2 mmol Fe²⁺/kg and total phenolics 3.77–81.3 mg GAE/g across batumen, involucrum and honey-pot cerumen, with honey-pot cerumen lowest ([Deyerling et al. 2024](https://www.sciencedirect.com/science/article/pii/S2772391724000513)). The general claim that resin incorporation is an antimicrobial defence against microbes exploiting nest conditions is made in the review literature ([Menezes et al. 2020, *Curr. Opin. Insect Sci.*, doi:10.1016/j.cois.2020.09.001](https://www.sciencedirect.com/science/article/abs/pii/S2214574520301504)) — *note this is an adaptive interpretation, not a measured property of a given sample.*
6. **Distinguishing microbiota.** Cerumen/nest-surface communities differ from those of the honey, pollen and larval-food it encloses. Nest surfaces were *Pseudomonas*/*Sphingomonas*/*Escherichia*-dominated depending on building material ([*PLOS ONE* 2021](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0252933)), whereas food stores and larval diet in *Scaptotrigona* hives are Lactobacillaceae/Acetobacteraceae and Saccharomycetaceae-dominated ([Nature Communications 2025, doi:10.1038/s41467-025-66678-9](https://pmc.ncbi.nlm.nih.gov/articles/PMC12749006/)); *Tetragonula* nest materials were lactobacilli-dominated ([MRA 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10112253/)). Brood-cell cerumen specifically is the isolation source of *Monascus ruber* and *Candida* sp. that regulate the *Zygosaccharomyces* symbiont larvae must eat to pupate ([Paludo et al. 2019](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0219696); [Paludo et al. 2018, *Sci. Rep.* 8:1122, doi:10.1038/s41598-018-19583-9](https://www.nature.com/articles/s41598-018-19583-9)).

## 4. Sources

Primary literature
- Massaro FC, Brooks PR, Wallace HM, Russell FD (2011). Cerumen of Australian stingless bees (*Tetragonula carbonaria*): GC-MS fingerprints and potential anti-inflammatory properties. *Naturwissenschaften* 98(4):329–337. doi:10.1007/s00114-011-0770-7 · PMID [21347735](https://pubmed.ncbi.nlm.nih.gov/21347735/)
- Popova M, et al. (2021). A preliminary study of chemical profiles of honey, cerumen, and propolis of the African stingless bee *Meliponula ferruginea*. *Foods* 10(5):997. [doi:10.3390/foods10050997](https://pmc.ncbi.nlm.nih.gov/articles/PMC8147412/) (2 May 2021)
- Deyerling N, Achenbach J, dos Santos MM, Locher C (2024). Physicochemical properties, antioxidant activity and phytochemical profiling of Australian *Tetragonula carbonaria* cerumen. *J. Chromatogr. Open* 5:100164. [doi:10.1016/j.jcoa.2024.100164](https://www.sciencedirect.com/science/article/pii/S2772391724000513)
- Nogueira et al. (2021). Bacterial communities of indoor surface of stingless bee nests. *PLOS ONE* 16(7):e0252933. [doi:10.1371/journal.pone.0252933](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0252933) (9 Jul 2021)
- 16S amplicon metabarcoding of the nest materials of native Australian stingless bees. *Microbiol. Resour. Announc.* (13 Mar 2023). [doi:10.1128/mra.01181-22](https://pmc.ncbi.nlm.nih.gov/articles/PMC10112253/)
- Paludo CR, et al. (2019). Microbial community modulates growth of symbiotic fungus required for stingless bee metamorphosis. *PLOS ONE* 14(7):e0219696. [doi:10.1371/journal.pone.0219696](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0219696)
- Paludo CR, et al. (2018). Stingless bee larvae require fungal steroid to pupate. *Sci. Rep.* 8:1122. [doi:10.1038/s41598-018-19583-9](https://www.nature.com/articles/s41598-018-19583-9)
- Spatial segregation and cross-kingdom interactions drive stingless bee hive microbiome assembly. *Nat. Commun.* (25 Nov 2025). [doi:10.1038/s41467-025-66678-9](https://pmc.ncbi.nlm.nih.gov/articles/PMC12749006/)
- Chemical contaminants in cerumen samples from Ecuadorian stingless bees. *Insects* 16(11):1079 (22 Oct 2025). [doi:10.3390/insects16111079](https://pmc.ncbi.nlm.nih.gov/articles/PMC12653277/)
- Nemec/Rehman et al. Raman study of spatial distribution of propolis in comb of *Apis mellifera carnica*. PMID [12833475](https://pubmed.ncbi.nlm.nih.gov/12833475/) — for the *Apis* wax–propolis rim layer.

Reviews, reference works, vocabularies
- Chuttong B, et al. (2023). Exploring the functional properties of propolis, geopropolis, and cerumen, with special emphasis on antimicrobial effects. *Foods* 12(21):3909. [doi:10.3390/foods12213909](https://pmc.ncbi.nlm.nih.gov/articles/PMC10648409/) — explicitly notes cerumen research is sparse relative to propolis.
- Menezes C, et al. (2020). Stingless bees and microbial interactions. *Curr. Opin. Insect Sci.* [doi:10.1016/j.cois.2020.09.001](https://www.sciencedirect.com/science/article/abs/pii/S2214574520301504)
- Vit P, Bankova V, Popova M, Roubik DW (eds., 2023–2024). *Stingless Bee Nest Cerumen and Propolis*, Vols. 1–2, Springer. [doi:10.1007/978-3-031-43274-3](https://link.springer.com/book/10.1007/978-3-031-43274-3) · [doi:10.1007/978-3-031-43887-5](https://link.springer.com/content/pdf/10.1007/978-3-031-43887-5.pdf) — the standing reference work; Vol. 2 ch. 9 (Layek et al.) on *T. iridipennis* cerumen: [doi:10.1007/978-3-031-43887-5_9](https://link.springer.com/chapter/10.1007/978-3-031-43887-5_9)
- Amateur Entomologists' Society, *Entomologists' glossary*, "cerumen": [amentsoc.org](https://www.amentsoc.org/insects/glossary/terms/cerumen/)
- Ontology checks run 2026-08-18 against EBI OLS4 (`/api/search`) for `cerumen`, `propolis`, `beehive`, `hive`, `bee`, `beeswax`, `construction material`, `animal habitation`; AGROVOC REST `search?query=cerumen*`; GitHub issue search on `EnvironmentOntology/envo`.

**Explicitly my inference, not sourced:** that the GOLD node's 0 assertions leave the *Apis*/Meliponini reading undetermined by data; that `ENVO:01000155` is an imperfect but usable genus given cerumen's non-macromolecular chemistry; that ENVO's material/site split implies two terms rather than one.

## 5. Synonyms, and what not to conflate

**In real use for this concept:** cerumen; stingless bee cerumen; nest cerumen; bee cerumen; "cerumen (Meliponini)". Structure-qualified variants naming the same material: involucrum cerumen, batumen cerumen, honey-pot cerumen, brood-cell cerumen ([Deyerling et al. 2024](https://www.sciencedirect.com/science/article/pii/S2772391724000513)). Portuguese/Spanish literature: *cerume*/*cerumen*.

**Commonly but wrongly treated as the same thing:**

- **Earwax** (`UBERON:0002297`, `MeSH:D002571`, `SNOMED:41508009`, `NCIT:C32293`, `MA:0002506`, `EMAPA:36850`) — pure homonym. This is the trap the record's existing curator note already caught.
- **Propolis** (`DRON:00012339`/FoodOn, `MeSH:D011429`, `SNOMED:255970007`, AGROVOC `c_15919`) — resin-dominated bee glue, canonically *Apis*. Multiple reviews warn the two words are used interchangeably in the stingless-bee literature and should not be ([Popova et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8147412/); [Chuttong et al. 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10648409/)). Note the trap in reverse: the Australian nest-material study labelled its brood-cell-wall samples "propolis" while stating they are cerumen ([MRA 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10112253/)).
- **Geopropolis** — resin amalgamated with soil/clay; a different material by definition ([Popova et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8147412/)).
- **Batumen** — strictly a nest *structure* (the cavity-lining wall/sheath), which may be built of cerumen but may also incorporate mud, seeds, wood or vertebrate faeces. Overlapping, not identical.
- **Beeswax** (`FOODON:03302072`, `ENVO:01000575`) — one ingredient. *Austroplebeia* nests are built largely of wax while *Tetragonula* build mainly of cerumen, so the distinction is real within Meliponini ([Deyerling et al. 2024](https://www.sciencedirect.com/science/article/pii/S2772391724000513)).
- **Brood comb** (`Beehive: Brood combs`, `habitatmech:GOLD.230a05ae80`) — the *Apis* wax comb. In Meliponini the brood cells *are* cerumen, so the two GOLD nodes overlap under the Meliponini reading; they are distinct under the *Apis* reading. Worth a cross-reference on both records rather than a merge.
- **Honey / pollen / larval food** — the contents of cerumen containers, with demonstrably different microbiota ([Nat. Commun. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12749006/)).

## 6. Should it be a term at all?

**Yes.** It is a material and a physical location that is aseptically sampled, sequenced and cultured as a distinct nest compartment in at least four independent studies ([MRA 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10112253/); [PLOS ONE 2021](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0252933); [PLOS ONE 2019](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0219696); [Insects 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12653277/)), it supports resident microorganisms with a demonstrated functional role in the host's life cycle, and its community is distinguishable from those of the neighbouring concepts. It is not a process, quality, disease, taxon, or sampling artefact. It is a genuine ENVO gap: nothing in ENVO names a hive, a bee nest, or this material, and no ENVO term request for it exists.

Suggested disposition: keep `habitatmech:GOLD.a3c5e2adba` as a minted identity and treat it as an ENVO **term-request candidate**, ideally as a small package with the missing *nest of bee* / *nest of stingless bee* sibling to ENVO's existing *nest of ant / bird / termite / alligator*. Two caveats to carry into the request: the definition should say Meliponini rather than "beehive", and the curator should decide whether the material term or a companion site term (§2.3) is what the GOLD node needs.

## Citations

1. https://www.amentsoc.org/insects/glossary/terms/cerumen/
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC8147412/
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC10648409/
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC12653277/
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC10112253/
6. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0219696
7. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0252933
8. https://www.sciencedirect.com/science/article/pii/S2772391724000513
9. https://pubmed.ncbi.nlm.nih.gov/12833475/
10. https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0002297
11. https://pubmed.ncbi.nlm.nih.gov/21347735/
12. https://link.springer.com/chapter/10.1007/978-3-031-43887-5_9
13. https://www.sciencedirect.com/science/article/abs/pii/S2214574520301504
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC12749006/
15. https://www.nature.com/articles/s41598-018-19583-9
16. https://link.springer.com/book/10.1007/978-3-031-43274-3
17. https://link.springer.com/content/pdf/10.1007/978-3-031-43887-5.pdf