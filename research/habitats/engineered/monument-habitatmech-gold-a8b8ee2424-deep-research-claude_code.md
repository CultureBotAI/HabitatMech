---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T02:15:48.672892'
end_time: '2026-08-18T02:24:39.822972'
duration_seconds: 531.15
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Monument
  habitat_identifier: habitatmech:GOLD.a8b8ee2424
  habitat_category: ENGINEERED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Engineered > Built environment > Monument'
  assertions: '2'
  parent_terms: mesh:D000076624
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Narrowed-grounding\
    \ review (#67): was ENVO:00000359 'natural monument', which is a protected-area\
    \ designation. GOLD's path is Engineered > Built environment > Monument, so this\
    \ is a built stone monument \u2014 close to the opposite. Stonework is a real\
    \ habitat and the slice has no term for it. (source concept habitatmech:GOLD.a8b8ee2424)"
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
  web_search_requests: 7
  num_turns: 31
  total_cost_usd: 2.860194
  session_id: 1b72ab54-5484-4a88-9352-a6701057ac30
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 22
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Monument
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.a8b8ee2424
- **Category:** ENGINEERED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Engineered > Built environment > Monument
- **Upstream assertion volume:** 2
- **Nearest broader term already on the record:** mesh:D000076624
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Narrowed-grounding review (#67): was ENVO:00000359 'natural monument', which is a protected-area designation. GOLD's path is Engineered > Built environment > Monument, so this is a built stone monument — close to the opposite. Stonework is a real habitat and the slice has no term for it. (source concept habitatmech:GOLD.a8b8ee2424)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Monument** as a microbial habitat, with citations.

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

# Monument — novel-term definition research

**Target:** `habitatmech:GOLD.a8b8ee2424` · label *Monument* · category ENGINEERED · GOLD path `Engineered > Built environment > Monument`

---

## Proposed definition

> A human construction which is conserved for its historical, artistic, religious or commemorative value and whose fabric of quarried stone, brick, mortar or plaster forms a subaerial mineral surface available for microbial colonisation.

Genus: `ENVO:00000070` *human construction* ("A construction that has been assembled by deliberate human effort.") — present and non-deprecated in the vendored slice, and already the asserted parent of the corpus's own `building` record (`ENVO:00000073`), so the genus is precedented in-corpus.

---

## ⚠️ First, a correction the curator needs before anything else

**The recorded note is factually wrong on its central claim.** It says "the slice has no term for it." The slice does have one:

```
data/raw/ontology_terms.tsv:9502
ENVO:02000132   ENVO   constructed monument   A human construction which serves as a memorial.   [syn] monument
```

Confirmed live in ENVO via OLS4: `ENVO:02000132` *constructed monument*, active (not obsolete), exact synonym **"monument"**, `rdfs:subClassOf ENVO:00000070` *human construction* — and that subclass edge is itself in `data/raw/ontology_subclass_edges.tsv:7887`. It has no children in ENVO.
<https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:02000132>

So the CONFIRM_UNGROUNDED reasoning as written does not hold. The note's *other* claim — that `ENVO:00000359` *natural monument* was the wrong target because it is a protected-area designation over a natural feature — remains correct. The question is therefore not "does a term exist" but **"is `ENVO:02000132` the same concept, and if not, in what direction does it differ."** My answer below is that it is a **near-miss by over-claim**, and that `relation: xref` is the right disposition — but this must be an explicit, argued decision, not a repeat of "nothing exists."

---

## 1. What the concept denotes

**The place a sample is taken from:** the mineral fabric — dimension stone, ashlar, carved relief, brick, lime mortar, plaster render — of a standing structure that is kept and maintained because of its cultural, historical, artistic or religious significance. The sampled material is almost always a **subaerial biofilm** scraped, swabbed or micro-cored from the stone surface, together with the outermost millimetres of the substratum where endolithic growth occurs (Gorbushina 2007, doi:[10.1111/j.1462-2920.2007.01301.x](https://doi.org/10.1111/j.1462-2920.2007.01301.x), PMID 17564597).

**The GOLD subtree settles the reading.** The full set of paths in `data/raw/gold_ecosystem_paths.tsv`:

| Path | assertions (ORGANISM) |
|---|---|
| `Engineered > Built environment > Monument` | 2 |
| `… > Monument > Stone` | 0 |
| `… > Monument > Stone > Sandstone` | 1 |
| `… > Monument > Interior wall` | 0 |

The children are **materials and parts of a structure**, not designations of a landscape. This is decisive: whatever "Monument" means here, it is the sort of thing made of stone and having interior walls. That is a built heritage structure, and confirms the #67 re-decision away from *natural monument*.

**Two boundary facts that constrain the definition:**

1. **`Interior wall` is inside the concept.** A definition restricted to *outdoor* or *open-air* surfaces would exclude a child GOLD explicitly places here — crypt walls, frescoed interiors, grotto and tomb interiors, cave-temple carvings. The literature body includes exactly these (Beishiku, Tiantishan and Maijishan Grottoes; Dazu Rock Carvings — Yang et al. 2025, doi:[10.1038/s43247-025-02993-9](https://doi.org/10.1038/s43247-025-02993-9)). Use "subaerial" (air-exposed) rather than "outdoor."
2. **The concept is the structure, not the biofilm.** The organisms sampled are the *inhabitants*; `subaerial biofilm` / `epilithic biofilm` is a community and a material, not a place. HabitatMech already models the site level this way for `building` (`ENVO:00000073`), and the corpus already has separate `biofilm__*` records.

**Is the label ambiguous?** Yes, and the ambiguity is the entire problem here — three live readings:

- **(a) Built heritage structure** — the cultural-heritage sense (temples, cathedrals, statues, stelae, rock carvings, tombstones, historic masonry). **This is what the GOLD data means.**
- **(b) Memorial** — a construction whose purpose is to commemorate. This is `ENVO:02000132`'s reading, and it is *narrower on function* than (a): Angkor Wat, Lingyin Temple pagoda and a cathedral façade are monuments in sense (a) and are not memorials.
- **(c) Natural monument** — a protected-area designation over a natural feature (`ENVO:00000359`, `ENVO:01001165`). Excluded by the `Engineered >` prefix; already rejected under #67.

The authoritative statement of reading (a) is the **1972 UNESCO World Heritage Convention, Article 1**, which defines "monuments" as *"architectural works, works of monumental sculpture and painting, elements or structures of an archaeological nature, inscriptions, cave dwellings and combinations of features, which are of outstanding universal value from the point of view of history, art or science."* <https://whc.unesco.org/en/conventiontext/> — note that *commemoration is nowhere in it*, and that cave dwellings are explicitly included, corroborating boundary fact (1).

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:00000070` *human construction*.** In the slice, non-deprecated, definition "A construction that has been assembled by deliberate human effort." It is unambiguously broader than the concept, it is the parent ENVO itself asserts for *constructed monument*, and the corpus already uses it as a parent on `building`. Nothing about it over-claims.

### Near-misses and why each fails

| Term | Label / definition | Why it is not the identity |
|---|---|---|
| **`ENVO:02000132`** | *constructed monument* — "A human construction which serves as a memorial." | **The closest thing in ENVO, and the one to record as `xref`.** It asserts a *commemorative function* that GOLD never claims and that most of the sampled corpus does not have. Temples (Bayon, Lingyin, Kaihua), grottoes, palace ruins and cathedral façades are not memorials. This is structurally the `anthropogenic contamination feature` situation from #99: grounding publishes an assertion the source did not make. It is also not a clean *parent* — memorial-hood and heritage-hood **overlap** rather than nest (a new war memorial is a memorial and not heritage; a Buddhist grotto is heritage and not a memorial), so `GROUND_AS_PARENT` is wrong for the same reason `GROUND` is. → `relation: xref`. |
| `ENVO:00000073` | *building* — "A permanent walled and roofed construction." | Asserts walls **and a roof**. Obelisks, stelae, statues, tombstones, bas-relief walls and rock carvings — the bulk of the sampled literature — have neither. Also a sibling in GOLD (`Built environment > Building`, 17 assertions), already grounded in the corpus; merging would collapse two distinct GOLD nodes. |
| `ENVO:00000359` | *natural monument* (syn. "monument") | The #67 error. A *natural* environment given a protective designation. Label-matches, denotes the opposite. |
| `ENVO:01001165` | *IUCN natural monument or feature* | An IUCN protected-area category over a primarily natural formation. Same failure. |
| `ENVO:00000375` | *world heritage site* | A **legal designation over an area**, and it can be a forest, lake or desert. Most sampled monuments are not WHS-listed; the property being sampled is the stonework, not the listing. Asserts far more than the data does. |
| `ENVO:03501280` | *mausoleum* | A genuine narrower child. Also a *building* by its own definition — inherits the walled-and-roofed problem. |
| `ENVO:03501337` | *temple* | Also a genuine narrower child, and covers a large share of the actual sampled sites — but is a proper subclass, not the concept. |
| `ENVO:01000457` / `ENVO:01000495` / `ENVO:01000465` | *masonry unit* / *stone exterior wall* / *building wall* | **Material and part terms, not the site.** These are the right targets for the *children* of this record (see §7), and are the reason the sibling `Stone` record's own note ("the slice has no term for it") also deserves re-checking. |
| `ENVO:00002055`, `ENVO:00002053`, `ENVO:01000356` | *sandstone*, *limestone*, *granite* | The lithotype, i.e. what the monument is made of. `Monument > Stone > Sandstone` should probably ground to `ENVO:00002055`; the parent should not. |
| `ENVO:00001995` / `ENVO:00002144` | *rock* / *cave wall* | Natural substrata. `cave wall` in particular is the correct term for painted caves (Lascaux, Altamira) — a genuinely neighbouring habitat that must **not** be merged in, since it is not a human construction. |

**Conclusion:** no ENVO term expresses reading (a) exactly. `ENVO:00000070` is the correct genus; `ENVO:02000132` is the correct `xref`.

---

## 3. Differentia — what distinguishes it

Ordered from most to least defensible, with the supporting source for each.

**(i) Deliberate human assembly from quarried/fired mineral material.** Separates it from natural rock outcrop, cliff, cave wall and rock shelter. The bioreceptivity literature treats freshly quarried rock as the explicit control against the same lithotype in a monument, precisely because the two differ in surface finishing, exposure history and secondary bioreceptivity (Guillitte 1995, doi:[10.1016/0048-9697(95)04582-L](https://doi.org/10.1016/0048-9697(95)04582-L); Miller et al. 2012, doi:[10.1016/j.scitotenv.2012.03.026](https://doi.org/10.1016/j.scitotenv.2012.03.026), PMID 22534363).

**(ii) Retained and maintained for cultural/historical/artistic/religious significance rather than for occupancy or utility.** This is what separates it from its GOLD siblings `Building`, `House`, `Cement wall`, `City` and `Hospital`. Source for the property itself: UNESCO 1972 Art. 1 (above); ICOMOS *Venice Charter* (1964) Art. 1 similarly frames the "historic monument" as embracing the architectural work together with its setting as evidence of a civilisation, a development, or a historic event <https://www.icomos.org/en/participer/179-articles-en-francais/ressources/charters-and-standards/157-thevenice-charter>. This is also the property that makes the habitat *scientifically distinct*: monuments are the substrata under active conservation intervention (biocides, consolidants, cleaning), which creates tertiary bioreceptivity — a state that ordinary building stone does not have (Guillitte 1995; Sanmartín et al. 2021, doi:[10.1016/j.scitotenv.2021.145314](https://doi.org/10.1016/j.scitotenv.2021.145314)).

**(iii) A subaerial mineral interface — oligotrophic, intermittently wetted, atmospherically supplied.** SABs are "ubiquitous, self-sufficient, miniature microbial ecosystems" on solid mineral surfaces exposed to the atmosphere; atmospheric aerosols, gases and propagules supply both nutrients and inoculum; metabolism centres on water retention and radiation protection (Gorbushina 2007, doi:[10.1111/j.1462-2920.2007.01301.x](https://doi.org/10.1111/j.1462-2920.2007.01301.x)). This is directly consistent with the corpus's own `built_environment_surfaces` parameter band already carried on `building`: NUTRIENTS low, ORGANIC_MATTER low, WATER_AVAILABILITY low, WATER_VARIABILITY "occasionally wet."

**(iv) The stone selects — the community is not simply deposited air or soil.** At the Monumental Cemetery of Milano, biofilm, surrounding air and soil were compared directly: only a few rare taxa were shared across the three compartments, and those had been selected by the stone environment (doi:[10.1016/j.ibiod.2021.105298](https://doi.org/10.1016/j.ibiod.2021.105298)). *This is the single strongest published argument that the concept is a real habitat and not a sampling artefact of urban air.*

**(v) Characteristic community structure and succession.** Phototrophs (cyanobacteria, Chlorophyta) as pioneers, followed by heterotrophic bacteria, microcolonial black fungi and lichens; epilithic *and* endolithic. At Bayon Temple, Angkor Thom, recovered sequences spanned 11 bacterial, 11 eukaryotic and 2 archaeal divisions (Lan et al. 2010, *Microb Ecol* 60:105–115, doi:[10.1007/s00248-010-9707-5](https://doi.org/10.1007/s00248-010-9707-5)). Across twelve stone specimens from four separated locations in China (limestone and marble Buddhist statuary and architecture), Cyanobacteria and Ascomycota were the predominant bacterial and fungal phyla, and 64% of isolated bacterial strains induced calcium carbonate precipitation (Zhang et al. 2018, *AEM*, doi:[10.1128/AEM.02680-17](https://doi.org/10.1128/AEM.02680-17)).

**(vi) Characteristic physicochemistry — pollutant-coupled N and S cycling.** On monument stone specifically, nitrifying bacteria and *Thiobacillus* correlated with ambient NO₂ and SO₂, while phototroph abundance correlated with light and humidity (Li et al. 2016, *PLoS ONE* 11:e0163287, doi:[10.1371/journal.pone.0163287](https://doi.org/10.1371/journal.pone.0163287), PMID 27658256). Deterioration proceeds by acid attack, salt mobilisation and mineral crystallisation, with >30 °C combined with >60% RH accelerating biodeteriogen activity (Liu et al. 2020, *Nat Sustain* 3:991–1004, doi:[10.1038/s41893-020-00602-5](https://doi.org/10.1038/s41893-020-00602-5)).

**(vii) Climate governs whether the community degrades or protects.** Across 91 sampling points at 10 World Heritage sites spanning temperate, subtropical and tropical Asia, biofilm role shifted from deterioration to protection along the temperate→tropical gradient; protection rate correlated with minimum temperature of the coldest month (R = 0.67, P < 0.001) and mean annual precipitation (R = 0.44, P < 0.001), mediated by dissimilatory nitrate reduction (*napAB*, *narGHI*, *nrfAH*, *nirBD*) and assimilatory sulfate reduction (*cysJI*, *sir*) gene abundance (Yang et al. 2025, *Commun Earth Environ* 6:1019, doi:[10.1038/s43247-025-02993-9](https://doi.org/10.1038/s43247-025-02993-9)).

**My inference, not a source claim:** that (i)+(ii) *jointly* are the minimal differentia — i.e. that "constructed" alone under-specifies (it would swallow `Building` and `Cement wall`) and "heritage-significant" alone under-specifies (it would swallow heritage canals, cultural landscapes and archaeological soils). No source states this pairing; it is my reading of what the GOLD sibling set requires.

---

## 4. Sources

| # | Citation | Identifier |
|---|---|---|
| 1 | Gorbushina AA. Life on the rocks. *Environ Microbiol* 9(7):1613–1631, 2007. | doi:[10.1111/j.1462-2920.2007.01301.x](https://doi.org/10.1111/j.1462-2920.2007.01301.x) · PMID [17564597](https://pubmed.ncbi.nlm.nih.gov/17564597/) |
| 2 | Liu X, Koestler RJ, Warscheid T, Katayama Y, Gu J-D. Microbial deterioration and sustainable conservation of stone monuments and buildings. *Nat Sustain* 3:991–1004, 2020. | doi:[10.1038/s41893-020-00602-5](https://doi.org/10.1038/s41893-020-00602-5) |
| 3 | Yang H, Li X, Chai L, Wang L, Qi C, et al. Climate-driven transition in microbial deterioration and protection of stone surfaces at cultural heritage sites. *Commun Earth Environ* 6:1019, 2025. | doi:[10.1038/s43247-025-02993-9](https://doi.org/10.1038/s43247-025-02993-9) |
| 4 | Zhang G, et al. Deterioration-associated microbiome of stone monuments: structure, variation, and assembly. *Appl Environ Microbiol* 84(7), 2018. | doi:[10.1128/AEM.02680-17](https://doi.org/10.1128/AEM.02680-17) |
| 5 | Lan W, Li H, Wang W-D, Katayama Y, Gu J-D. Microbial community analysis of fresh and old microbial biofilms on Bayon Temple sandstone of Angkor Thom, Cambodia. *Microb Ecol* 60(1):105–115, 2010. | doi:[10.1007/s00248-010-9707-5](https://doi.org/10.1007/s00248-010-9707-5) |
| 6 | Li Q, Zhang B, He Z, Yang X. Distribution and diversity of bacteria and fungi colonization in stone monuments analyzed by high-throughput sequencing. *PLoS ONE* 11(9):e0163287, 2016. | doi:[10.1371/journal.pone.0163287](https://doi.org/10.1371/journal.pone.0163287) · PMID [27658256](https://pubmed.ncbi.nlm.nih.gov/27658256/) |
| 7 | Guillitte O. Bioreceptivity: a new concept for building ecology studies. *Sci Total Environ* 167(1–3):215–220, 1995. | doi:[10.1016/0048-9697(95)04582-L](https://doi.org/10.1016/0048-9697(95)04582-L) |
| 8 | Miller AZ, et al. Bioreceptivity of building stones: a review. *Sci Total Environ* 426:1–12, 2012. | doi:[10.1016/j.scitotenv.2012.03.026](https://doi.org/10.1016/j.scitotenv.2012.03.026) · PMID [22534363](https://pubmed.ncbi.nlm.nih.gov/22534363/) |
| 9 | Sanmartín P, Miller AZ, Prieto B, Viles HA. Revisiting and reanalysing the concept of bioreceptivity 25 years on. *Sci Total Environ* 770:145314, 2021. | doi:[10.1016/j.scitotenv.2021.145314](https://doi.org/10.1016/j.scitotenv.2021.145314) |
| 10 | Villa F, Wu Y-L, et al. The tombstones at the Monumental Cemetery of Milano select for a specialized microbial community. *Int Biodeterior Biodegradation* 164:105298, 2021. | doi:[10.1016/j.ibiod.2021.105298](https://doi.org/10.1016/j.ibiod.2021.105298) |
| 11 | Biofilms on stone monuments: biodeterioration or bioprotection? *Trends Microbiol* 30(9), 2022. | doi:[10.1016/j.tim.2022.05.012](https://doi.org/10.1016/j.tim.2022.05.012) |
| 12 | Warscheid T, Braams J. Biodeterioration of stone: a review. *Int Biodeterior Biodegradation* 46(4):343–368, 2000. | doi:[10.1016/S0964-8305(00)00109-8](https://doi.org/10.1016/S0964-8305(00)00109-8) |
| 13 | Gaylarde CC, Gaylarde PM. A comparative study of the major microbial biomass of biofilms on exteriors of buildings in Europe and Latin America. *Int Biodeterior Biodegradation* 55(2):131–139, 2005. | doi:[10.1016/j.ibiod.2004.10.001](https://doi.org/10.1016/j.ibiod.2004.10.001) |
| 14 | Li H, Deng W, Gao J, Yen T-B, Katayama Y, Gu J-D. The active microbes and biochemical processes contributing to deterioration of Angkor sandstone monuments under the tropical climate in Cambodia — a review. *J Cult Herit* 47:218–226, 2021. | doi:[10.1016/j.culher.2020.10.010](https://doi.org/10.1016/j.culher.2020.10.010) |
| 15 | Biodeterioration of cultural heritage monuments: a review of their deterioration mechanisms and conservation. *Int Biodeterior Biodegradation*, 2025. | doi:[10.1016/j.ibiod.2025.106066](https://doi.org/10.1016/j.ibiod.2025.106066) |
| 16 | UNESCO. Convention Concerning the Protection of the World Cultural and Natural Heritage, Art. 1, 16 Nov 1972. | <https://whc.unesco.org/en/conventiontext/> |
| 17 | ICOMOS. International Charter for the Conservation and Restoration of Monuments and Sites (Venice Charter), Art. 1, 1964. | <https://www.icomos.org/en/participer/179-articles-en-francais/ressources/charters-and-standards/157-thevenice-charter> |
| 18 | ENVO `ENVO:02000132` *constructed monument* (OLS4, accessed 2026-08-18). | <https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:02000132> |
| 19 | ENVO `ENVO:00000070` *human construction* (OLS4, accessed 2026-08-18). | <https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00000070> |

**Claims that are mine, not a source's**, flagged explicitly: (a) that `ENVO:02000132` *overlaps* rather than subsumes the GOLD concept — this is my reading of ENVO's definition text against the sampled literature, not something either states; (b) the joint-differentia argument in §3; (c) the boundary judgement in §1 that `Interior wall` forces "subaerial" over "outdoor" — GOLD asserts the parentage, but no source discusses the terminological consequence; (d) the disposition recommendation in §7.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept** (all attested across sources 1–15):
`stone monument` · `stone-built cultural heritage` · `stone cultural heritage` · `built heritage` · `historic monument` · `historic stone building` · `heritage stonework` · `historic masonry` · `monumental stone` · `lithic cultural heritage` · `stone heritage surface`

**Commonly but wrongly treated as the same thing:**

- **`natural monument` (`ENVO:00000359`) and `IUCN natural monument or feature` (`ENVO:01001165`)** — protected-area designations over natural formations. `ENVO:00000359` carries the exact synonym "monument", which is precisely the lexical trap #67 caught. Do not restore.
- **`world heritage site` (`ENVO:00000375`)** — an administrative listing, applicable to forests and lakes. Overlaps with, but is neither identity nor genus.
- **`building` (`ENVO:00000073`)** — a distinct GOLD sibling with its own record and 17× the assertion volume; also asserts roof + walls.
- **`rock` (`ENVO:00001995`), `rock shelter` (`ENVO:00000440`), `cave wall` (`ENVO:00002144`)** — natural substrata. Painted/decorated caves are cultural heritage but are *not human constructions*; `ENVO:00002144` is the right term for those and should not be merged here.
- **`subaerial biofilm` / `epilithic biofilm`** — the *community and material* growing on the habitat, not the habitat. The corpus already holds separate `biofilm__*` records.
- **`quarry` / `quarried stone`** — the source material and its extraction site; used as the experimental control against monument stone, deliberately *not* the same habitat (source 8).
- **`stone` as a material** (`ENVO:01000457` *masonry unit*, `ENVO:00002055` *sandstone*) — the fabric, not the site. Note that GOLD's `Stone` node is a *child of Monument*, which reinforces that Monument is the site level.
- **`cemetery` / `tombstone`** — a real and heavily sampled instance (source 10), but a narrower case; do not let it drive the definition toward the memorial-only reading.

---

## 6. Should this be a term at all?

**Yes.** It passes every test the corpus applies:

- It is a **place**, not a process, quality, disease state, procedure or taxonomic grouping. `NOT_APPLICABLE` does not apply.
- It is **not a sampling artefact**: source 10 directly tested the artefact hypothesis (is this just deposited air and soil?) and rejected it — the stone selects a community distinguishable from both surrounding compartments.
- It has a **large, independent, decades-old literature** with its own methods (bioreceptivity assays), its own standards discourse (conservation charters), and its own biogeochemistry (sources 1–15).
- It has **structural load in this corpus already**: two records (`Stone`, `Interior wall`) list `habitatmech:GOLD.a8b8ee2424` as their parent. Retiring it would orphan them.

Assertion volume (2 ORGANISM) is low, but that measures GOLD deposition, not whether the concept is real; the sibling `Cement wall` has the same count and the literature behind *this* one is far deeper.

---

## 7. Recommended disposition

**`CONFIRM_UNGROUNDED`, but with a corrected and much narrower note** — the existing note must be rewritten because its stated reason ("the slice has no term") is false and `tests/test_decisions.py` checks note claims against the repo.

Suggested shape for the decision:

- **grounding:** stays UNGROUNDED, minted identity retained.
- **`ENVO:00000070` *human construction*** → `parent` (genus; broader; already precedented on `building`).
- **`ENVO:02000132` *constructed monument*** → **`relation: xref`**, with the reason stated: it asserts a commemorative function GOLD does not claim, and overlaps rather than subsumes, so it is neither identity nor parent (the #99 pattern).
- **`mesh:D000076624` *Built Environment*** → keep as-is.
- **Term-request candidate:** yes. Two routes, either acceptable — (a) an ENVO term request for a *heritage-significance* sibling of `constructed monument` under `human construction`; or (b) an ENVO issue asking whether `ENVO:02000132`'s "serves as a memorial" should be relaxed to the UNESCO Art. 1 sense, since its own exact synonym "monument" is already being used in the broader sense by data providers including GOLD. Route (b) is cheaper and fixes the mismatch at the source.

**Two adjacent findings, out of scope but worth filing:**

1. The sibling record `Stone` (`habitatmech:GOLD.8c6192908f`) carries the same "the slice has no term for it" claim. The slice does contain `ENVO:01000457` *masonry unit*, `ENVO:01000495` *stone exterior wall* and `ENVO:00002055` *sandstone*; whether any is right for `Built environment > Monument > Stone` was evidently not assessed. Same for `Interior wall` (`habitatmech:GOLD.6ade183144`) against `ENVO:01000465` *building wall*.
2. Both of those notes came from the same class-level sweep that produced this one, which suggests the sweep's "no term matched by any search route" claim may be systematically under-searching — `constructed monument` carries "monument" as an exact synonym and still was not found.

## Citations

1. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:02000132
2. https://doi.org/10.1111/j.1462-2920.2007.01301.x
3. https://doi.org/10.1038/s43247-025-02993-9
4. https://whc.unesco.org/en/conventiontext/
5. https://doi.org/10.1016/0048-9697(95
6. https://doi.org/10.1016/j.scitotenv.2012.03.026
7. https://www.icomos.org/en/participer/179-articles-en-francais/ressources/charters-and-standards/157-thevenice-charter
8. https://doi.org/10.1016/j.scitotenv.2021.145314
9. https://doi.org/10.1016/j.ibiod.2021.105298
10. https://doi.org/10.1007/s00248-010-9707-5
11. https://doi.org/10.1128/AEM.02680-17
12. https://doi.org/10.1371/journal.pone.0163287
13. https://doi.org/10.1038/s41893-020-00602-5
14. https://pubmed.ncbi.nlm.nih.gov/17564597/
15. https://pubmed.ncbi.nlm.nih.gov/27658256/
16. https://pubmed.ncbi.nlm.nih.gov/22534363/
17. https://doi.org/10.1016/j.tim.2022.05.012
18. https://doi.org/10.1016/S0964-8305(00
19. https://doi.org/10.1016/j.ibiod.2004.10.001
20. https://doi.org/10.1016/j.culher.2020.10.010
21. https://doi.org/10.1016/j.ibiod.2025.106066
22. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00000070