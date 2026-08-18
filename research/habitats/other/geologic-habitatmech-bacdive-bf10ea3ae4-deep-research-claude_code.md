---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:57:29.719963'
end_time: '2026-08-17T17:07:38.944121'
duration_seconds: 609.22
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Geologic
  habitat_identifier: habitatmech:BACDIVE.bf10ea3ae4
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Geologic'
  assertions: '381'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Generic
    "Geologic" bin spanning rock, sediment and subsurface. ENVO covers each specifically;
    nothing covers the bin without misattributing the rest. (source concept habitatmech:BACDIVE.bf10ea3ae4)'
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
  web_search_requests: 15
  num_turns: 40
  total_cost_usd: 4.144015999999999
  session_id: 209151d2-c170-4260-86d2-506b7f8b4f1d
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 26
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Geologic
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.bf10ea3ae4
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Geologic
- **Upstream assertion volume:** 381
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Generic "Geologic" bin spanning rock, sediment and subsurface. ENVO covers each specifically; nothing covers the bin without misattributing the rest. (source concept habitatmech:BACDIVE.bf10ea3ae4)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Geologic** as a microbial habitat, with citations.

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

# Definition research: **Geologic** — `habitatmech:BACDIVE.bf10ea3ae4`

> **A solid environmental material which is a naturally occurring rock, mineral or evaporite deposit, or an excavation or void within one, sampled directly as a lithic substrate rather than as overlying soil, sediment, or water.**

One caveat on that sentence up front: the concept as BacDive actually applies it straddles a **material** reading (calcarenite stone, limestone, rock salt, stalactite) and a **site** reading (cave, mine). A single Aristotelian sentence cannot carry both without a disjunctive genus. If the curator wants a clean definition, the honest structure is a material class (`rock/mineral substrate as microbial habitat`) plus a separate site class (`subterranean excavation or void`), with the BacDive tag mapped to the material class and the site cases carried as `xref`s. **The missing intermediate class is the material one** — ENVO has no "geological material" / "lithic environmental material" node (§2). Saying that is more useful than a two-clause definition.

---

## 1. What the concept denotes

**Reading the data actually supports.** `Geologic` is a **Category-3 tag in BacDive's Microbial Isolation Source Ontology (MISO)**, sitting under `#Environmental` (Cat 1) → `#Terrestrial` (Cat 2). MISO is a three-level controlled vocabulary whose eight Category-1 classes are `#Environmental, #Engineered, #Host, #Host body-site, #Host body-product, #Medical, #Condition, #Climate` ([Reimer et al. 2019, *Nucleic Acids Research* 47:D631, doi:10.1093/nar/gky879](https://academic.oup.com/nar/article/47/D1/D631/5106998), PMID [30256983](https://pubmed.ncbi.nlm.nih.gov/30256983/)). The path is therefore `#Environmental #Terrestrial #Geologic`, and I confirmed that exact three-tag path on four live BacDive strain records:

| BacDive ID | Strain | Free-text isolation source (verbatim) | Cat 1 / 2 / 3 |
|---|---|---|---|
| [130342](https://bacdive.dsmz.de/strain/130342) | *Geodermatophilus aquaeductus* DSM 46834 | "surface of an altered calcarinite stone", ruins of the Aqueduct of Hadrian, Zaghouan, Tunisia | Environmental / Terrestrial / **Geologic** |
| [132427](https://bacdive.dsmz.de/strain/132427) | *Lentzea guizhouensis* DSM 102208 | "limestone from a Karst area", Guizhou, China | Environmental / Terrestrial / **Geologic** |
| [141003](https://bacdive.dsmz.de/strain/141003) | *Angustibacter speluncae* YC2-20ᵀ | "pieces of stalactites collected at Yongcheon Cave", Jeju, Republic of Korea | Environmental / Terrestrial / **Geologic** (+ **Volcanic**) |
| [5924](https://bacdive.dsmz.de/strain/5924) | *Halococcus salifodinae* BIp (DSM 8989) | "rock salt" / "Salt mine near Bad Ischl", Austria | Environmental / Terrestrial / **Geologic** |

Two of these are corroborated by the primary species descriptions: *A. speluncae* was isolated from lava-cave stalactites ([Ko & Lee 2017, *IJSEM* 67:3283, doi:10.1099/ijsem.0.002108](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.002108), PMID [28857735](https://pubmed.ncbi.nlm.nih.gov/28857735/)); *H. salifodinae* from Permian rock salt in an Austrian salt mine ([Denner et al. 1994, *Int J Syst Bacteriol* 44:774, doi:10.1099/00207713-44-4-774](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-44-4-774)).

**So, inside the concept:** exposed and buried rock and stone (including built stone of geological material — the Roman aqueduct case), limestone/karst rock, cave interiors and speleothems, rock salt and other evaporite/mineral deposits, and mine workings and their rock faces. **The thing sampled is the lithic substrate itself.**

**Neighbouring concepts, outside it (all separate BacDive tags in this repo's own inventory, `data/raw/bacdive_isolation_sources.tsv`):** `Soil`, `Sandy` (607 strains), `Mud-Sludge` (540), `Tidal-flat` (246), `Cave-water` (2), `Freshwater`, `Marine`, `Saline`. BacDive keeps unconsolidated and aqueous sources out of `Geologic`; the cave *water* of a cave is a different tag from the cave *rock*.

**Ambiguity — and a correction to the note on the record.** The existing curation note says the bin spans "rock, sediment and subsurface." The *sediment* part is not BacDive's usage; it is **GOLD's**. GOLD's five-level ecosystem classification ([Mukherjee et al. 2023, *NAR* 51:D957, doi:10.1093/nar/gkac974](https://academic.oup.com/nar/article/51/D1/D957/6786204)) puts `Sediment`, `Sediment core`, `Oil-contaminated sediment`, `Pyrite containing`, `Mine` and `Mine pit pond` *under* `Environmental > Terrestrial > Geologic` — visible in this repo at `data/raw/gold_ecosystem_paths.tsv:117,139,817,1608–1612`. That GOLD concept is a **different record** (`habitatmech:GOLD.e00433021f`, `data/habitats/terrestrial/geologic__c55de755.yaml`). The two vocabularies use the same word with **different extensions**, and the BacDive record should be defined off BacDive's usage. This is worth recording explicitly so a later curator does not merge them.

**Second ambiguity:** MISO tags are **facets, not an exclusive partition** — *A. speluncae* carries both `#Geologic` and `#Volcanic`. Whatever definition is written should describe the substrate, not claim exclusivity against sibling tags.

**Taxon-profile check (this repo's own data, `characteristic_taxa`).** The 381 strains / 301 taxa include exactly the taxa the rock-habitat literature predicts: *Modestobacter* sp. (5), *Blastococcus* sp. (2) — stone-dwelling Geodermatophilaceae; *Angustibacter speluncae* (2) — cave; *Halococcus salifodinae* (3) — rock salt; *Alkalibacillus haloalkaliphilus*, *Thalassobacillus* sp. — halophiles. **But** the top of the list is myxobacteria — *Corallococcus coralloides* (9), *Nannocystis exedens* (8), *Sorangium cellulosum* (6), *Myxococcus fulvus* (5), *Herpetosiphon* sp. (3) — which are canonically soil, dung and bark organisms. *This is my inference, not a sourced claim:* that block most likely reflects a batch of strains whose free-text source was rock-associated soil or stone-surface material, and it is direct evidence that the bin's boundary against `#Soil` is not clean in practice. A curator should not over-claim substrate specificity in the differentia on the strength of the taxon list alone.

---

## 2. Genus — the broader kind

**Recommended genus: `solid environmental material` — `ENVO:01000814`** ("An environmental material which is in a solid state."). It is in the vendored slice (`data/raw/ontology_terms.tsv`), it is genuinely *broader* (so it is legitimate in `parent_habitats`), and it is the nearest ENVO node that subsumes both rock and evaporite. It is weak — it also subsumes soil and ice — so the differentia has to do all the work.

**There is no ENVO term for the concept.** I checked ENVO via OLS4 for `geological material`, `geologic`, and `geological formation`: the hits are processes (`ENVO:01000694` geological subsidence, `ENVO:04000017` geological carbon sequestration), fractures (`ENVO:01000667/8/72`), a quality (`ENVO:01001164` geodiversity), and landform classes — **no class named "geological material", "geological formation", or "geologic environment"** exists.

### Near-misses and why each fails

| CURIE | Label | Why it is not a match |
|---|---|---|
| `ENVO:01000256` | mineral material | Looks right, but **`rock` is not under it**. I verified via OLS4 that `ENVO:00001995` rock's direct parent is `ENVO:01000814` solid environmental material, not mineral material. Grounding here would fail to subsume the stone/limestone majority of the bin. |
| `ENVO:00001995` | rock | **Narrower.** Excludes rock salt as an isolation matrix framing, excludes the cave-void and mine-excavation cases, excludes loose mineral deposits. Correct as `relation: xref`. |
| `ENVO:00000191` | solid astronomical body part | Carries the synonym **"geological feature"**, which is why lexical search reaches for it — and it is the trap. It is a *feature/landform* class covering mountains, dunes, plains and every soil-bearing landform. Far broader than the concept, and it asserts feature-hood the BacDive tag never claims (the tag is applied to a piece of stone). Same over-claim pattern as the `Contamination` → *anthropogenic contamination feature* case (#99). |
| `ENVO:00000067` / `ENVO:00000076` | cave / mine | **Narrower**, and each covers only one slice of the bin. Attesting either as parent would misattribute the stone-monument and rock-salt strains. `xref` at most. |
| `ENVO:01000303` | endolithic environment | **Narrower** and asserts more: "an environment that exists *within* solid rock." *G. aquaeductus* was isolated from a stone **surface**, which is epilithic, not endolithic. |
| `ENVO:01000646` | lithosphere | **Far broader** — a planetary shell. Everything terrestrial is in the lithosphere. |
| `ENVO:01001776` | subsurface zone of an astronomical body | Covers the mine/cave/borehole cases but **excludes exposed rock surfaces**, which the exemplars show are in scope. |
| `ENVO:00002007` | sediment | Not in scope for the BacDive reading (§1); it is in scope for the *GOLD* `Geologic`. Grounding the BacDive record here would import GOLD's extension. |
| `ENVO:01000747` / `ENVO:01000751` | regolith / bedrock | Each **narrower**; a legitimate `xref` pair but neither is a genus. |
| `ENVO:00010483` | environmental material | Broader than `ENVO:01000814` and correspondingly weaker; use only if `solid` is judged too strong (it is not — every exemplar substrate is solid). |

**Standards check.** Neither MIxS nor GSC has a "geologic" environmental package: the package list is `Air, BuiltEnvironment, …, HydrocarbonResourcesCores, HydrocarbonResourcesFluidsSwabs, MicrobialMatBiofilm, MiscellaneousNaturalOrArtificialEnvironment, PlantAssociated, Sediment, Soil, Water, …` ([GSC MIxS schema](https://genomicsstandardsconsortium.github.io/mixs/); hydrocarbon packages from [Tsesmetzis et al. 2016, *Stand Genomic Sci*, PMC5059931](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5059931/)). Rock-hosted sampling in MIxS is handled by `Sediment`, `Soil`, or `HydrocarbonResourcesCores`, never by a geologic bin. **So the absence of an ontology term is not an oversight in ENVO alone — no reference standard carves this class.** That is a real argument that the concept is a source-vocabulary bin rather than a natural kind, and it should be weighed against §6.

**The literature does name the kind**, however, which is the counter-argument: "the rock-hosted biosphere" ([Templeton & Caro 2023, *Annu Rev Earth Planet Sci* 51:493–519, doi:10.1146/annurev-earth-031920-081957](https://www.annualreviews.org/content/journals/10.1146/annurev-earth-031920-081957), CC-BY) and "the endolithic environment … an interface between biology and geology" ([Walker & Pace 2007, *Annu Rev Microbiol* 61:331–347, doi:10.1146/annurev.micro.61.080706.093302](https://www.annualreviews.org/content/journals/10.1146/annurev.micro.61.080706.093302), PMID [17506683](https://pubmed.ncbi.nlm.nih.gov/17506683/)).

---

## 3. Differentia — what distinguishes it

Ordered by how observable each property is at sampling time. The first is the one that actually does the work.

1. **The sampled material is consolidated / lithified, not particulate-unconsolidated.** This is the operational line against `Soil` (`ENVO:00001998`, defined in the slice as "primarily composed of minerals, varying proportions of sand, silt, and clay, organic material such as humus…") and against `Sediment` (`ENVO:00002007`, "particulate environmental material … formed as a result of the transport and deposition of particles by flowing liquid"). Stone, limestone, bedrock, speleothems and rock salt are lithified; soil and sediment are not. *This differentia is my synthesis of the two ENVO definitions plus the exemplar sources; no single source states it as the boundary criterion.*
2. **Formation is geological, not pedogenic or depositional-aquatic.** Igneous, metamorphic, sedimentary-lithified, or evaporitic origin. Rock is "a naturally occurring solid aggregate of one or more minerals or mineraloids" (`ENVO:00001995`); *H. salifodinae*'s matrix is Permian evaporite ~250 Ma old (Denner et al. 1994, above).
3. **Organic carbon is minimal and the substrate itself supplies the mineral energy source.** Rock-hosted communities are characterised by mineral-associated growth under energy- and nutrient-limited conditions, with lithology, permeability and fluid mixing controlling community composition (Templeton & Caro 2023). Cave systems are explicitly "nutrient-limited environments containing a variety of redox interfaces," where sulfur-, iron- and manganese-oxidising bacteria dissolve host rock and speleothems ([Northup & Lavoie 2001, *Geomicrobiology Journal* 18:199–222, doi:10.1080/01490450152467750](https://www.tandfonline.com/doi/abs/10.1080/01490450152467750)). Mine settings run on sulfide-mineral oxidation: dissolution of pyrite, arsenopyrite, chalcopyrite, sphalerite and marcasite yields acidic, metal-rich solutions, with autotrophic Fe/S oxidation as the dominant metabolism ([Baker & Banfield 2003, *FEMS Microbiol Ecol* 44:139–152, doi:10.1016/S0168-6496(03)00028-X](https://academic.oup.com/femsec/article/44/2/139/546507)).
4. **Physical stress regime: desiccation, UV/ionising radiation, oligotrophy, freeze–thaw.** The rock substrate is repeatedly described as protecting inhabitants from UV and excessive solar radiation and freeze–thaw while providing physical stability and enhanced moisture availability (Walker & Pace 2007). The stone-dwelling Geodermatophilaceae quantify it: D₁₀ gamma-radiation doses of 900 Gy (*Blastococcus saxobsidens*), 6000 Gy (*Modestobacter multiseptatus*) and 9000 Gy (*Geodermatophilus obscurus*) ([Gtari et al. 2012, *FEMS Microbiol Ecol* 80:566–577](https://academic.oup.com/femsec/article/80/3/566/442285)); niche partitioning within a single stone is documented — *Blastococcus* in stone interiors, *Modestobacter* on stone surfaces ([Sghaier et al. 2016, *ISME J* 10:21–29, doi:10.1038/ismej.2015.108](https://pmc.ncbi.nlm.nih.gov/articles/PMC4681853/), PMID [26125681](https://pubmed.ncbi.nlm.nih.gov/26125681/)).
5. **Scale context (for the scope note, not the definition sentence):** the continental subsurface is estimated at 2–6 × 10²⁹ cells, ~23–31 Pg C, with community composition correlating with **sample lithology** ([Magnabosco et al. 2018, *Nature Geoscience* 11:707–717, doi:10.1038/s41561-018-0221-6](https://www.nature.com/articles/s41561-018-0221-6)). Lithology-as-predictor is the strongest published support for treating rock substrate as a habitat-defining variable.

---

## 4. Sources

Every substantive claim above is anchored to one of these. Where a statement is my synthesis rather than a source's assertion, it is marked inline.

**Source-vocabulary / standards**
- Reimer LC, Vetcininova A, Sardà Carbasse J, Söhngen C, Gleim D, Ebeling C, Overmann J. BacDive in 2019. *Nucleic Acids Research* 47:D631–D636 (2019). doi:[10.1093/nar/gky879](https://academic.oup.com/nar/article/47/D1/D631/5106998) · PMID [30256983](https://pubmed.ncbi.nlm.nih.gov/30256983/) — MISO, three levels, eight Category-1 classes.
- BacDive isolation-source browser: <https://bacdive.dsmz.de/isolation-sources>; strain records [130342](https://bacdive.dsmz.de/strain/130342), [132427](https://bacdive.dsmz.de/strain/132427), [141003](https://bacdive.dsmz.de/strain/141003), [5924](https://bacdive.dsmz.de/strain/5924) (fetched 2026-08-17).
- Mukherjee S et al. Twenty-five years of GOLD. *NAR* 51:D957 (2023). doi:[10.1093/nar/gkac974](https://academic.oup.com/nar/article/51/D1/D957/6786204) — five-level ecosystem classification (the differing GOLD extension of "Geologic").
- GSC MIxS schema, environmental package list: <https://genomicsstandardsconsortium.github.io/mixs/> · Tsesmetzis N et al. MIxS-HCR. [PMC5059931](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5059931/) (2016).
- Buttigieg PL, Pafilis E, Lewis SE, Schildhauer MP, Walls RL, Mungall CJ. The environment ontology in 2016. *J Biomed Semantics* 7:57 (2016). doi:[10.1186/s13326-016-0097-6](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/) · PMID [27664130](https://pubmed.ncbi.nlm.nih.gov/27664130/) — the biome / feature / material triad, i.e. why the material-vs-site split in §1 matters.
- ENVO term records via OLS4 (`ebi.ac.uk/ols4/api`, queried 2026-08-17) and the repo's vendored slice `data/raw/ontology_terms.tsv`.

**Primary literature on the habitat**
- Templeton AS, Caro TA. The Rock-Hosted Biosphere. *Annu Rev Earth Planet Sci* 51:493–519 (2023). doi:[10.1146/annurev-earth-031920-081957](https://www.annualreviews.org/content/journals/10.1146/annurev-earth-031920-081957).
- Walker JJ, Pace NR. Endolithic Microbial Ecosystems. *Annu Rev Microbiol* 61:331–347 (2007). doi:[10.1146/annurev.micro.61.080706.093302](https://www.annualreviews.org/content/journals/10.1146/annurev.micro.61.080706.093302).
- Magnabosco C et al. The biomass and biodiversity of the continental subsurface. *Nat Geosci* 11:707–717 (2018). doi:[10.1038/s41561-018-0221-6](https://www.nature.com/articles/s41561-018-0221-6).
- Northup DE, Lavoie KH. Geomicrobiology of Caves: A Review. *Geomicrobiol J* 18:199–222 (2001). doi:[10.1080/01490450152467750](https://www.tandfonline.com/doi/abs/10.1080/01490450152467750).
- Baker BJ, Banfield JF. Microbial communities in acid mine drainage. *FEMS Microbiol Ecol* 44:139–152 (2003). doi:[10.1016/S0168-6496(03)00028-X](https://academic.oup.com/femsec/article/44/2/139/546507).
- Sghaier H et al. Stone-dwelling actinobacteria … proteogenomes. *ISME J* 10:21–29 (2016). doi:[10.1038/ismej.2015.108](https://pmc.ncbi.nlm.nih.gov/articles/PMC4681853/).
- Gtari M et al. Contrasted resistance of stone-dwelling Geodermatophilaceae … *FEMS Microbiol Ecol* 80:566–577 (2012). [link](https://academic.oup.com/femsec/article/80/3/566/442285).
- Denner EBM, McGenity TJ, Busse H-J, Grant WD, Wanner G, Stan-Lotter H. *Halococcus salifodinae* sp. nov. *Int J Syst Bacteriol* 44:774–780 (1994). doi:[10.1099/00207713-44-4-774](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-44-4-774).
- Ko DH, Lee SD. *Angustibacter speluncae* sp. nov., isolated from a lava cave stalactite. *IJSEM* 67:3283–3288 (2017). doi:[10.1099/ijsem.0.002108](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.002108) · PMID [28857735](https://pubmed.ncbi.nlm.nih.gov/28857735/).
- Recent secondary review, for the endolithic scope: "Endolithic microbes of rocks, their community, function and survival strategies," *Int Biodeterior Biodegradation* (2022). [ScienceDirect S0964830522000154](https://www.sciencedirect.com/science/article/abs/pii/S0964830522000154). *I did not read the full text; cited for scope only.*

**Explicitly unverified.** A search result attributed a "376 terms" figure for MISO to third-party descriptions (Omnicrobe, *PLOS ONE* 2022, doi:10.1371/journal.pone.0272473). I did not confirm that number against either paper — **do not put it in a note.**

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- rock-hosted environment / rock-hosted biosphere (Templeton & Caro 2023) — the closest thing to a literature-standard name
- lithic habitat; lithobiontic habitat
- rock substrate; stone substrate; mineral substrate
- geological material (used descriptively in the literature; **not** an ENVO class)

**Commonly but wrongly treated as the same thing**
- **`soil`** (`ENVO:00001998`) — a separate BacDive tag and a separate MIxS package. Conflating them would absorb the largest terrestrial habitat in the corpus.
- **`sediment`** (`ENVO:00002007`) — inside *GOLD's* Geologic, outside *BacDive's*. The single most likely mis-merge for this record.
- **`endolithic environment`** (`ENVO:01000303`) — a proper subset (interior only); the exemplars include surface colonisation.
- **`mine`** (`ENVO:00000076`) and **`cave`** (`ENVO:00000067`) — settings partly covered by the tag, but each excludes most of it. Note also that `Cave-water` is a *separate* BacDive tag.
- **`acid mine drainage`** (`ENVO:00001997`) — an aqueous effluent, not the rock.
- **`solid astronomical body part`** (`ENVO:00000191`) — the synonym "geological feature" makes it a lexical magnet; it is a landform class and asserts feature-hood the tag does not.
- **`petroleum` / `formation fluid`** (`ENVO:00002984`, `ENVO:03600007`) — fluids in geologic formations; BacDive tags these under `Oil-Fuel` and related sources.
- **"US Geological Survey"** in strain provenance/history fields — a documented false-positive when text-searching BacDive for "Geologic" (e.g. *Geobacter metallireducens* GS-15, [BacDive 5791](https://bacdive.dsmz.de/strain/5791)). Worth a line in the note if the seeder ever does lexical matching on this label.

---

## 6. Should it be a term at all?

**Yes — it is a habitat, not a process, quality, disease or taxon.** Every exemplar names a physical place or material a sample was taken from. `NOT_APPLICABLE` would be wrong here; it is reserved for diseases, qualities, processes and procedures, and none of those readings apply. This is unlike the sibling BacDive Category-2/3 tags `Condition`, `Climate`, `Sulfuric`, `Humid` or `Xerophilic`, which are qualities of a habitat rather than habitats.

**But it is a bin, and the honest disposition depends on how much the corpus wants to assert.** The evidence cuts both ways:

- *Against a full term:* no ontology and no reference standard (ENVO, MIxS, GSC) carves this class; the boundary against `#Soil` is demonstrably leaky in the data (the myxobacteria block, §1); and the two source vocabularies that use the word disagree about its extension.
- *For a full term:* the literature does name the kind ("rock-hosted biosphere", "endolithic environment"), lithology is a published predictor of community composition (Magnabosco et al. 2018), and 381 strains / 301 taxa is a substantial attestation that would otherwise stay invisible.

**Recommended disposition:** keep the current `CONFIRM_UNGROUNDED` — it is correct — but **strengthen the record** rather than leaving it bare:

1. Add `parent_habitats: ENVO:01000814` (*solid environmental material*) with `relation: parent`. It is genuinely broader, it is in the vendored slice, and it gives the record the genus that `curation/term_requests/needs_a_parent_first.tsv:18` says it lacks. This alone moves the record off that blocker list.
2. Add `ENVO:00001995` (rock), `ENVO:01000256` (mineral material), `ENVO:00000067` (cave) and `ENVO:00000076` (mine) as `relation: xref` — the links BacDive's usage implies, without this repo asserting that any of them is the identity or a broader kind.
3. Update the note to correct the GOLD/BacDive extension conflict (§1) and to record that `ENVO:00000191`'s "geological feature" synonym is a near-miss to be rejected, not a candidate.
4. Treat it as a HabitatMech-minted term-request **candidate** for a `rock-hosted environmental material` class. Per the standing rule in memory, **any actual ENVO submission needs separate, explicit, per-request approval** — this report is not that request.

**One-sentence fallback if the material/site split is judged unacceptable in one class:** define only the material reading —

> *A solid environmental material which is a naturally occurring lithified rock, stone, or evaporite deposit, distinguished from soil and sediment by being consolidated and from aqueous habitats by being the sampled substrate itself.*

— and carry `cave` and `mine` purely as `xref`s. That is the version I would write.

## Citations

1. https://academic.oup.com/nar/article/47/D1/D631/5106998
2. https://pubmed.ncbi.nlm.nih.gov/30256983/
3. https://bacdive.dsmz.de/strain/130342
4. https://bacdive.dsmz.de/strain/132427
5. https://bacdive.dsmz.de/strain/141003
6. https://bacdive.dsmz.de/strain/5924
7. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.002108
8. https://pubmed.ncbi.nlm.nih.gov/28857735/
9. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-44-4-774
10. https://academic.oup.com/nar/article/51/D1/D957/6786204
11. https://genomicsstandardsconsortium.github.io/mixs/
12. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5059931/
13. https://www.annualreviews.org/content/journals/10.1146/annurev-earth-031920-081957
14. https://www.annualreviews.org/content/journals/10.1146/annurev.micro.61.080706.093302
15. https://pubmed.ncbi.nlm.nih.gov/17506683/
16. https://www.tandfonline.com/doi/abs/10.1080/01490450152467750
17. https://academic.oup.com/femsec/article/44/2/139/546507
18. https://academic.oup.com/femsec/article/80/3/566/442285
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC4681853/
20. https://pubmed.ncbi.nlm.nih.gov/26125681/
21. https://www.nature.com/articles/s41561-018-0221-6
22. https://bacdive.dsmz.de/isolation-sources
23. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/
24. https://pubmed.ncbi.nlm.nih.gov/27664130/
25. https://www.sciencedirect.com/science/article/abs/pii/S0964830522000154
26. https://bacdive.dsmz.de/strain/5791