---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:35:43.945527'
end_time: '2026-08-17T16:44:44.208516'
duration_seconds: 540.26
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Invertebrates-Other
  habitat_identifier: habitatmech:BACDIVE.e864a16f03
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Invertebrates-Other'
  assertions: '596'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Cohort\
    \ review: NCIT:C17649 'Other' is a bucket with no meaning of its own, and it absorbs\
    \ 'Rodentia-Other' too \u2014 one record labelled 'Other' holding rodents and\
    \ invertebrates. The invertebrate-associated environment terms in the slice are\
    \ all aquatic-qualified. Real habitat, no term. (source concept habitatmech:BACDIVE.e864a16f03)"
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
  web_search_requests: 12
  num_turns: 32
  total_cost_usd: 3.2138725000000004
  session_id: a01e6ad7-f682-47ac-ae1d-e842a55b254d
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 17
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Invertebrates-Other
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.e864a16f03
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Invertebrates-Other
- **Upstream assertion volume:** 596
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Cohort review: NCIT:C17649 'Other' is a bucket with no meaning of its own, and it absorbs 'Rodentia-Other' too — one record labelled 'Other' holding rodents and invertebrates. The invertebrate-associated environment terms in the slice are all aquatic-qualified. Real habitat, no term. (source concept habitatmech:BACDIVE.e864a16f03)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Invertebrates-Other** as a microbial habitat, with citations.

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

# Invertebrates-Other — `habitatmech:BACDIVE.e864a16f03`

> **Proposed definition:** An animal-associated environment which is determined by an invertebrate animal — a metazoan lacking a vertebral column — acting as host, comprising that animal's tissues, body fluids, internal cavities and body surfaces.

The source label's `-Other` is a residual-bucket marker from BacDive's classification, not part of what the concept denotes. It belongs in a scope note, not in the definition (see §1 and §6).

Suggested scope note (separate field, not the definition sentence):
> Source-side residual category. In BacDive's isolation-source classification this tag collects invertebrate hosts that are not assigned to a separately enumerated invertebrate category; in this corpus the separately enumerated siblings are `Porifera-Sponges` (86 strains) and `Cnidaria-Corals` (75 strains). Membership is therefore determined partly by what the source vocabulary broke out, not only by the biology.

---

## 1. What the concept denotes

**The physical place a sample comes from.** An individual invertebrate animal used as the sampling substrate — its gill tissue, gut lumen, haemolymph, mucus layer, body wall surface, specialised bacteriocytes, or whole macerated body. A microbiologist sampling this habitat homogenises or dissects an animal, not a volume of water or soil. This is the standard operational meaning of "host-associated" isolation in both BacDive and GOLD, where the host organism occupies the ecosystem-category slot that "mammals" or "plants" occupies ([GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification); [Reddy et al. 2015, *Nucleic Acids Res* 43:D1099, GOLD v.5](https://academic.oup.com/nar/article/43/D1/D1099/2439522)).

**The label is ambiguous and both readings need stating.**

- **Reading A — "invertebrates other than arthropods."** BacDive's own isolation-source browser lists `#Invertebrates (Other)` as a *category-2* tag sitting alongside a separate `#Arthropoda` category-2 tag under `#Host` ([BacDive isolation sources search](https://bacdive.dsmz.de/isolation-sources)). Under this reading the parenthetical "(Other)" contrasts invertebrates with arthropods.
- **Reading B — the residual category-3 bucket.** The concept is "invertebrate hosts not falling into an enumerated invertebrate subcategory."

**The data in this repo supports Reading B**, with a caveat. The BacDive inventory at `data/raw/bacdive_isolation_sources.tsv` is a flat list of 163 tag labels dominated by category-3 terms. `Invertebrates-Other` (596 strains) sits in that file next to `Porifera-Sponges` (86) and `Cnidaria-Corals` (75) as peers, and its exact structural analogue is `Rodentia-Other` (97), which sits next to `Muridae-Mouse/Rat` (325) — i.e. "rodents that are not murids." The `<Group>-Other` naming is a residual-sibling convention used at the same level in both branches. Note that BacDive assigns each isolation source *up to four category triplets* ([Reimer et al. 2019, *Nucleic Acids Res* 47:D631, doi:10.1093/nar/gky879](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/)), so a strain from a coral or sponge can legitimately carry both its specific tag and this one — the buckets are not disjoint.

**What is inside.** The record's characteristic taxa are the best available evidence of content, and they are coherent with an invertebrate-host reading:

| Taxon (strain count) | Host actually sampled |
|---|---|
| *Teredinibacter turnerae* (6) | gill bacteriocytes of wood-boring bivalves (Teredinidae) |
| *Xenorhabdus indica*, *X. khoisanae* (5, 4) | gut of *Steinernema* nematodes |
| *Photorhabdus thracensis*, *P. luminescens*, *P. laumondii*, *P. cinerea* (4, 4, 3, 3) | gut of *Heterorhabditis* nematodes |
| *Providencia vermicola* (3) | nematode |
| *Endozoicomonas ascidiicola* (2) | ascidian (tunicate) |
| *Lacinutrix venerupis* (2) | clam *Venerupis* |
| *Cobetia amphilecti* (2) | sponge *Amphilectus* |
| *Roseivivax isoporae* (2) | coral *Isopora* |
| *Vibrio parahaemolyticus*, *V. alginolyticus*, *V. lentus*, *V. alfacsensis* (5, 4, 3, 2) | shellfish and other marine invertebrates |
| *Pseudoalteromonas distincta*, *Thalassomonas viridans* (3, 2) | marine invertebrate surfaces/tissues |

Two clusters dominate: **marine invertebrate hosts** (molluscs, tunicates, echinoderms, plus sponge and coral spillover) and **terrestrial entomopathogenic nematodes** with their obligate enterobacterial symbionts.

**One anomaly the curator should not paper over.** Five of the top nineteen taxa are myxobacteria — *Sorangium cellulosum* (9), *Corallococcus coralloides* (7), *Archangium* sp. (6), *Nannocystis exedens* (5), *Myxococcus virescens* (3), together the single largest block in the list. Myxobacteria are canonically isolated from soil, rotting wood, compost and herbivore dung, not from invertebrates ([Dawid 2000, *FEMS Microbiol Rev* 24:403](https://academic.oup.com/femsre/article/24/4/403/510175); [Zhang et al. 2013, *PLOS ONE* 8:e70466](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0070466)). **This is my inference, not a sourced claim:** their presence here most likely reflects BacDive's multi-triplet tagging or residual assignment of free-text sources, rather than a genuine invertebrate-host signal. I could not retrieve the per-strain isolation-source text from BacDive to confirm. A curator should treat the 596 count as an upper bound on genuinely invertebrate-derived strains.

**Boundary — what is a neighbouring concept, not this one:**

- **Body parts of invertebrates** (gill, haemolymph, hypodermis, ocellus, nephridium, gastrodermis) — these have their own records and ground to BTO/UBERON anatomy terms. Per this repo's rule, a *part* grounds; the *whole organism* does not.
- **Enumerated invertebrate groups with their own records** — `Porifera-Sponges`, `Cnidaria-Corals`, and on the GOLD side `Mollusca`, `Nematoda`, `Echinodermata`, `Tunicata`, `Bryozoa`, `Ctenophora`, `Platyhelminthes`, `Arthropoda-Crustaceans`, `Arthropoda-Insects`. Whether these are *inside* or *outside* the residual bucket is exactly what Reading A vs B decides.
- **The environmental substrate the animal lives in** — sediment, seawater, soil. The animal, not its surroundings, determines this habitat.
- **`FOODON:00002452` invertebrate animal / invertebrate as food** — a class of organisms and a food commodity, not a place.

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001002` *animal-associated environment*** — "An environmental system determined by an animal." It is present in the vendored slice, its exact-synonym is "Metazoan-associated environment," and it is the direct superclass of every taxon-scoped animal-environment term ENVO has. Its own parent is `ENVO:01001000` *environmental system determined by an organism* (synonym: "host-associated environment").

This is also the genus the sibling GOLD record already uses — see §6.

**Near-misses in ENVO, and why each fails.** I queried the current ENVO release via OLS4 for every class mentioning "invertebrate," and separately enumerated all descendants of `ENVO:01001002`.

| Term | Why it is not a match |
|---|---|
| `ENVO:01001176` **environment associated with an aquatic invertebrate** — "An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system." | **Strictly narrower.** The aquatic qualifier is asserted in the definition and reinforced by a second parent, `ENVO:01001055` *environment associated with an animal part or small animal*. Grounding here would assert aquatic habitat for the entomopathogenic-nematode fraction (*Xenorhabdus*, *Photorhabdus*, *Providencia vermicola*), which is soil-dwelling. It cannot serve as the parent either — it would be a *child* of the concept, not broader than it. (xref `MEO_0000871`; subsets envoMeo, envoOmics.) |
| `ENVO:01001179` **cnidarian-associated environment** | Narrower, and already the home of the sibling `Cnidaria-Corals` concept. Useful as **precedent**: ENVO does mint taxon-scoped `<clade>-associated environment` classes under `ENVO:01001002`. |
| `ENVO:01001055` **environment associated with an animal part or small animal** | Asserts either *part-hood* or *smallness*. Neither holds generally: a giant squid or a *Xestospongia* barrel sponge is a whole large animal. Adopting it would over-claim. |
| `ENVO:01001000` **environmental system determined by an organism** | Correct but too broad — it also covers plants, fungi and protists. Fine as a grandparent, not as the genus. |
| `NCIT:C17649` **Other** (the upstream kg-microbe suggestion, recorded in `data/raw/isolation_source_groundings.tsv` as `skos:closeMatch`, `semapv:LexicalMatching`, confidence `medium`, method `ols4_search_synonym`) | A lexical match on the token "Other." It has no content and it collides — the same target absorbs `Rodentia-Other`. Correctly rejected. |
| `FOODON:00002452` **invertebrate animal**, `FOODON:00002581` aquatic invertebrate, `FOODON:00005522` invertebrate material | A taxonomic grouping and food commodities, not environments. Per this repo's rule, the taxon belongs in `relation: xref`, not `parent_habitats`. |
| `BTO:0001266` invertebrate muscular system, `BTO:0000572` hemolymph, `BTO:0000571` hemocyte, etc. | Anatomical parts of invertebrates — neighbouring concepts with their own records, not this one. |

**No general "invertebrate-associated environment" exists in ENVO.** The only two invertebrate-relevant classes are `ENVO:01001176` (aquatic-qualified) and `ENVO:01001179` (cnidarian-only). The curator's recorded note is accurate.

**There is no taxonomic anchor for the grouping either.** NCBI Taxonomy returns **zero** records for `Invertebrata` (E-utilities esearch, `db=taxonomy&term=Invertebrata`), because invertebrates are a paraphyletic grade rather than a clade — 31 of 32 animal phyla, defined by the *absence* of a vertebral column ([Eisenhauer et al. 2021, *Curr Biol* 31:R1214](https://www.sciencedirect.com/science/article/pii/S0960982221008873)). The only available taxon-side xref is `FOODON:00002452`.

---

## 3. Differentia — what distinguishes it

Under the genus *animal-associated environment*, the differentia that separate this from its siblings:

1. **Host phylogenetic scope — the absence of a vertebral column.** This distinguishes the concept from the vertebrate-host siblings in the same corpus (`Human`, `Mammal`, `Birds`, `Reptilia`, `Amphibia`, `Fishes`). It is a negative, grade-level criterion: invertebrates span ~31 of 32 animal phyla and roughly 95% of described animal species ([NPS, "Other Invertebrates"](https://www.nps.gov/shen/learn/nature/otherinvertebrates.htm); [Eisenhauer et al. 2021, *Curr Biol* 31:R1214](https://www.sciencedirect.com/science/article/pii/S0960982221008873)). Stating this openly is honest: the concept is broad and heterogeneous by construction.

2. **Anatomical compartmentation without vertebrate immune architecture.** Colonisable compartments are external epibiotic surfaces, mucus layers, tubes, gut lumen, haemocoel/haemolymph, and *specialised bacteriocytes and symbiont-housing organs* — the last a feature largely absent in the vertebrate hosts. Lo Giudice & Rizzo document site specificity across external surfaces, internal tissues, gill bacteriocytes, trophosome, appendages, tubes and mucus, and note active host selection rather than neutral colonisation ([Lo Giudice & Rizzo 2022, *Marine Drugs* 20:617, doi:10.3390/md20100617](https://pmc.ncbi.nlm.nih.gov/articles/PMC9605250/)).

3. **Dense, host-selected, often obligate symbioses with defined transmission modes.** Vertical (parent-to-offspring, e.g. *Calyptogena magnifica*) and horizontal acquisition at larval settlement (e.g. *Riftia pachyptila*) are both documented ([Lo Giudice & Rizzo 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9605250/)). Symbiont loads reach extremes not seen in vertebrate hosts: microbial cells constitute up to ~35% of sponge biomass ([Hentschel et al. 2012, *Nat Rev Microbiol* 10:641](https://www.nature.com/articles/nrmicro2839)).

4. **Nutritional symbioses supplying capabilities the host lacks.** The signature of this habitat in the isolate record. *Teredinibacter turnerae*, in bacteriocytes of the gland of Deshayes within shipworm gills, is cellulolytic and dinitrogen-fixing, enabling a wood diet ([Distel et al. 2002, *Int J Syst Evol Microbiol* 52:2261, PMID 12508896](https://pubmed.ncbi.nlm.nih.gov/12508896/)). *Endozoicomonas* spp. reside in aggregates within host tissues of corals, sponges, molluscs, worms and ascidians ([Neave et al. 2016, *Appl Microbiol Biotechnol* 100:8315, doi:10.1007/s00253-016-7777-0](https://pmc.ncbi.nlm.nih.gov/articles/PMC5018254/)).

5. **Vector/pathogen-delivery symbioses with no vertebrate-host analogue.** *Xenorhabdus* and *Photorhabdus* are carried in the intestine of non-feeding infective juveniles of *Steinernema* and *Heterorhabditis*, released into an insect haemocoel on invasion, killing the insect in 24–48 h, then re-acquired before the nematode leaves the cadaver ([Machado et al. 2024, *Zoological Letters* 10:13, doi:10.1186/s40851-024-00235-y](https://pmc.ncbi.nlm.nih.gov/articles/PMC11256433/)). The habitat here is a nematode gut receptacle — an invertebrate host that is itself a parasite of another invertebrate.

6. **Physicochemistry set by the host and its medium, not by an external biome.** For the marine fraction: seawater-matched ionic composition (elevated Ca²⁺ and Mg²⁺, ~0.3 M NaCl, pH ~8.5 optima for *T. turnerae*) ([Distel et al. 2002](https://pubmed.ncbi.nlm.nih.gov/12508896/)). For the nematode fraction: soil-temperature, microaerobic gut conditions. **The concept spans both marine and terrestrial settings — which is precisely why the aquatic-qualified `ENVO:01001176` cannot serve.**

7. **Phylosymbiosis — community composition tracks host phylogeny.** Reported for *Endozoicomonas* with Scleractinia and Demospongiae ([Eco-evolutionary processes shaping *Endozoicomonas* associations, 2025](https://www.sciencedirect.com/science/article/pii/S2667325825004546)) and for *Pseudoalteromonas* across marine invertebrate hosts ([*ISME J* 2026, wrag091](https://academic.oup.com/ismej/article/20/1/wrag091/8659212)). This supports treating "determined by the host animal" as a real differentia rather than a labelling convenience.

---

## 4. Sources

**Source vocabulary and classification**
- Reimer LC, Vetcininova A, Sardà Carbasse J, Söhngen C, Gleim D, Ebeling C, Overmann J (2019). BacDive in 2019: bacterial phenotypic data for high-throughput biodiversity analysis. *Nucleic Acids Research* 47:D631–D636. doi:10.1093/nar/gky879. https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/ — three-level tag hierarchy (category 1–3); eight top-level classes `#Environmental #Engineered #Host #Host body-site #Host body-product #Medical #Condition #Climate`; "Each isolation source is described with up to four triplets." *The paper does not mention residual or "other" categories* — the `-Other` convention is visible only in the live browser.
- BacDive isolation sources search. https://bacdive.dsmz.de/isolation-sources — `#Host` category-2 tags include `#Invertebrates (Other)` distinct from `#Arthropoda`.
- GOLD Ecosystem Classification. https://gold.jgi.doe.gov/ecosystem_classification ; Reddy TBK et al. (2015) *Nucleic Acids Res* 43:D1099. https://academic.oup.com/nar/article/43/D1/D1099/2439522 — five-level paths; `Host-associated > Invertebrates` occupies the ecosystem-category slot.

**Ontology**
- ENVO. Buttigieg PL et al. (2013) *J Biomed Semantics* 4:43, doi:10.1186/2041-1480-4-43, https://link.springer.com/article/10.1186/2041-1480-4-43 ; Buttigieg PL et al. (2016) *J Biomed Semantics* 7:57, https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/
- Term facts verified against the current ENVO release via EBI OLS4 (`/api/search`, `/api/ontologies/envo/terms/.../hierarchicalDescendants`) on 2026-08-17, and cross-checked against the vendored slice in `data/raw/ontology_terms.tsv` and `data/raw/ontology_subclass_edges.tsv`. Both agree: only `ENVO:01001176` and `ENVO:01001179` are invertebrate-relevant descendants of `ENVO:01001002`.
- NCBI Taxonomy E-utilities esearch, `db=taxonomy&term=Invertebrata` → 0 records (accessed 2026-08-17).

**Primary literature on the habitat**
- Lo Giudice A, Rizzo C (2022). Bacteria associated with benthic invertebrates from extreme marine environments. *Marine Drugs* 20:617. doi:10.3390/md20100617. https://pmc.ncbi.nlm.nih.gov/articles/PMC9605250/
- Distel DL, Morrill W, MacLaren-Toussaint N, Franks D, Waterbury J (2002). *Teredinibacter turnerae* gen. nov., sp. nov. *Int J Syst Evol Microbiol* 52:2261–2269. PMID 12508896. https://pubmed.ncbi.nlm.nih.gov/12508896/
- Machado RAR et al. (2024). Systematics and phylogeny of the entomopathogenic nematobacterial complexes *Steinernema*–*Xenorhabdus* and *Heterorhabditis*–*Photorhabdus*. *Zoological Letters* 10:13. doi:10.1186/s40851-024-00235-y. https://pmc.ncbi.nlm.nih.gov/articles/PMC11256433/
- Neave MJ, Apprill A, Ferrier-Pagès C, Voolstra CR (2016). Diversity and function of prevalent symbiotic marine bacteria in the genus *Endozoicomonas*. *Appl Microbiol Biotechnol* 100:8315–8324. doi:10.1007/s00253-016-7777-0. https://pmc.ncbi.nlm.nih.gov/articles/PMC5018254/
- Hentschel U, Piel J, Degnan SM, Taylor MW (2012). Genomic insights into the marine sponge microbiome. *Nat Rev Microbiol* 10:641–654. https://www.nature.com/articles/nrmicro2839
- Eisenhauer N, Bonn A, Guerra CA et al. (2021). Invertebrate biodiversity and conservation. *Curr Biol* 31:R1214. https://www.sciencedirect.com/science/article/pii/S0960982221008873
- Dawid W (2000). Biology and global distribution of myxobacteria in soils. *FEMS Microbiol Rev* 24:403–427. https://academic.oup.com/femsre/article/24/4/403/510175 — background for the myxobacteria anomaly.

**Explicitly flagged as my inference, not sourced:** (a) that the myxobacterial block in the characteristic taxa is a tagging artefact rather than genuine invertebrate-host isolation; (b) that Reading B (residual category-3 bucket) is what the HabitatMech inventory means — this rests on the structural parallel with `Rodentia-Other`/`Muridae-Mouse/Rat` in `data/raw/bacdive_isolation_sources.tsv`, not on a BacDive statement.

---

## 5. Synonyms and what NOT to conflate

**Names in real use for the positive concept**
- invertebrate-associated environment
- invertebrate host-associated environment
- invertebrate-associated habitat
- invertebrate holobiont environment
- invertebrate-derived isolation source
- (source-side, not for publication) `Invertebrates (Other)`, `Host > Invertebrates`

**Do not conflate with:**

| Not the same | Why |
|---|---|
| `ENVO:01001176` *environment associated with an aquatic invertebrate* | Aquatic-qualified; excludes the soil-dwelling nematode fraction. Narrower, not equivalent. |
| `FOODON:00002452` *invertebrate animal* / `FOODON:00002581` *aquatic invertebrate* | A grouping of organisms, and a food commodity class. Use as `relation: xref` only. |
| "Invertebrata" as a taxon | Not a clade and not an NCBI Taxonomy node; a paraphyletic grade defined by an absence. |
| `NCIT:C17649` *Other* | Contentless; collides with `Rodentia-Other`. |
| Invertebrate **body parts** (`BTO:0000572` hemolymph, `BTO:0000313` hypodermis, `BTO:0001758` ocellus, gill, gut) | Parts ground to anatomy terms and have their own records; the whole host organism does not. |
| Invertebrate **seafood** / shellfish products | A processed food material, a different habitat category (`Seafood`, 59 strains, is a separate row in the same inventory). |
| The **sediment, seawater or soil** an invertebrate inhabits | Environmental, not host-associated. |
| **Insect- and crustacean-associated** environments | BacDive places these under a separate `#Arthropoda` category-2 tag; GOLD has separate `Arthropoda > Insects` and `Arthropoda > Crustaceans` paths with their own records here. |
| The **insect cadaver** in an entomopathogenic-nematode cycle | A decomposing-animal environment colonised via a nematode vector; the nematode gut is the invertebrate habitat, the insect is a second, distinct one. |
| Invertebrate **disease states** (e.g. shellfish vibriosis) | A disease is not a habitat — the corpus disposition for those is `NOT_APPLICABLE`. |

---

## 6. Should this be a term at all?

**Yes for the concept; the `-Other` framing is the part that should not survive into the definition.**

Applying this repo's own tests:

- **Is it a habitat?** Yes. An organism acting as host is a place where microbes live, and ENVO models exactly this at `ENVO:01001002` with taxon-scoped children such as `ENVO:01001179`. This is not a disease, quality, process or procedure, so `NOT_APPLICABLE` would be the wrong disposition — and `tests/test_decisions.py` would reject it anyway, since the natural target is an organism grouping.
- **Is it a whole organism rather than a part?** Yes — invertebrates are whole host organisms, like `Mollusca` and `Porifera`. So the established handling applies: keep the minted identity, put the organism term (`FOODON:00002452`) in `relation: xref`, and treat this as an `<X>-associated environment` term-request candidate.
- **Is it a sampling artefact?** *Partly, and this is the real finding.* The `-Other` suffix is a residual bucket whose extension is fixed by what the source vocabulary happened to enumerate, not by biology. Two consequences: the definition must state the positive kind (invertebrate-determined animal-associated environment), and the residual scope belongs in a comment. A definition that reads "…which is not one of the other invertebrate categories" is unusable outside BacDive and should not be written.

**Recommended disposition**

| Field | Value | Rationale |
|---|---|---|
| grounding | `CONFIRM_UNGROUNDED` (unchanged) | No ENVO term fits. `ENVO:01001176` is narrower; `NCIT:C17649` is contentless. |
| `parent_habitats` | `ENVO:01001002` *animal-associated environment*, `relation: parent` | Genuinely broader. Matches what the sibling GOLD record already carries. |
| `parent_habitats` | `FOODON:00002452` *invertebrate animal*, `relation: xref` | Taxon grouping, not a place — xref per the repo rule. |
| `parent_habitats` | `ENVO:01001176`, `relation: xref` | Related but *narrower*; must not be a parent. Recording it as xref preserves the link without asserting aquatic-ness. |
| category | Consider `HOST_ASSOCIATED`, not `OTHER` | The concept is squarely host-associated; `OTHER` appears to be an artefact of the `Invertebrates-Other` label sorting into the `other/` directory. The sibling GOLD record is already `HOST_ASSOCIATED`. Curator's call. |
| term request | Candidate: `invertebrate-associated environment` under `ENVO:01001002` | Direct precedent: `ENVO:01001179` *cnidarian-associated environment*. **Do not submit without explicit per-request authorisation.** |

**Two things a curator should resolve before writing the record**

1. **Likely duplicate.** `habitatmech:GOLD.4d792ac724` "Invertebrates" (GOLD path `Host-associated > Invertebrates`, 621 organisms, UNGROUNDED, `HOST_ASSOCIATED`, parents `ENVO:01001000` + `ENVO:01001002`) is the same concept from the other source vocabulary, already reviewed with the same conclusion. If Reading A is taken, the two are identical; if Reading B is taken, the BacDive record is a residual subset of the GOLD one. The repo has a mechanism for declaring two novel concepts the same (PR #116/#117) and it looks applicable here.
2. **The 596 count is an upper bound.** Roughly a quarter of the top-ranked characteristic taxa are soil/dung myxobacteria with no known invertebrate association. If the definition or any downstream claim leans on the assertion volume, that caveat should travel with it.

## Citations

1. https://gold.jgi.doe.gov/ecosystem_classification
2. https://academic.oup.com/nar/article/43/D1/D1099/2439522
3. https://bacdive.dsmz.de/isolation-sources
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/
5. https://academic.oup.com/femsre/article/24/4/403/510175
6. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0070466
7. https://www.sciencedirect.com/science/article/pii/S0960982221008873
8. https://www.nps.gov/shen/learn/nature/otherinvertebrates.htm
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC9605250/
10. https://www.nature.com/articles/nrmicro2839
11. https://pubmed.ncbi.nlm.nih.gov/12508896/
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC5018254/
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC11256433/
14. https://www.sciencedirect.com/science/article/pii/S2667325825004546
15. https://academic.oup.com/ismej/article/20/1/wrag091/8659212
16. https://link.springer.com/article/10.1186/2041-1480-4-43
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/