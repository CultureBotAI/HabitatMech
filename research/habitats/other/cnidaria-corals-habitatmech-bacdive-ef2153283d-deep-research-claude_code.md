---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T21:17:47.335588'
end_time: '2026-08-17T21:25:32.748794'
duration_seconds: 465.41
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Cnidaria-Corals
  habitat_identifier: habitatmech:BACDIVE.ef2153283d
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Cnidaria-Corals'
  assertions: '75'
  parent_terms: (none)
  xrefs: mesh:D037421
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term mesh:D037421 'Anthozoa' attached as a parent. Host-taxon reversal\
    \ (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a\
    \ habitat'. That reasoning is wrong, and the corpus already contradicted it \u2014\
    \ the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia,\
    \ Mammals, Birds and Fish, which keep their own identity and a term request for\
    \ an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE\
    \ while its own child Porifera > Sponge was a term request.An organism acting\
    \ as a host IS a habitat: it is where the microbe lives, and ENVO models exactly\
    \ this at plant-associated, animal-associated and fungi-associated environment.\
    \ What is not a habitat is the TAXON TERM \u2014 a phylum is a class of organisms,\
    \ not a place \u2014 so the taxon stays an xref (#99) and the concept keeps its\
    \ own identity as a term-request candidate. NOT_APPLICABLE said the concept is\
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:BACDIVE.ef2153283d)"
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
  web_search_requests: 16
  num_turns: 33
  total_cost_usd: 3.3616735
  session_id: 8b116783-6e50-492e-8c23-1e301b726dda
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 31
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Cnidaria-Corals
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.ef2153283d
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Cnidaria-Corals
- **Upstream assertion volume:** 75
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** mesh:D037421

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term mesh:D037421 'Anthozoa' attached as a parent. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:BACDIVE.ef2153283d)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Cnidaria-Corals** as a microbial habitat, with citations.

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

# Cnidaria-Corals (`habitatmech:BACDIVE.ef2153283d`) — definition research

> **A cnidarian-associated environment which is determined by a coral or other anthozoan and is sampled as the animal's surface mucus layer, soft tissue, gastrovascular cavity, or aragonite skeleton.**

**But the primary finding of this research is that this record probably should not get a minted definition at all: ENVO already has the term.** `ENVO:01001179` *cnidarian-associated environment* — "An environmental system determined by a cnidarian or part of a cnidarian" — is live, non-obsolete, in the vendored slice (`data/raw/ontology_terms.tsv:8673`, `directly_referenced=TRUE`), and is already used elsewhere in this corpus. Details in §2 and §6.

---

## 1. What the concept denotes

**The BacDive category.** `bacdive.isolation_source:cnidaria-corals` is one of BacDive's controlled isolation-source categories (BacDive classifies each strain's origin in a three-level scheme; Reimer *et al.*, *Nucleic Acids Research* 50:D741–D746, 2022, [doi:10.1093/nar/gkab961](https://doi.org/10.1093/nar/gkab961), [PMC8728306](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728306/)). It carries **75 strains across 73 distinct taxa** — essentially one strain per taxon, which tells you this is a *type-strain-description* aggregate assembled from `sp. nov.` papers, not a deep sampling of any one reef.

**The physical thing sampled.** The place a microbiologist puts a swab, syringe, or airbrush is the body of a living cnidarian — overwhelmingly a coral. The coral holobiont is the cnidarian animal host plus its bacteria, archaea, viruses, fungi, and dinoflagellate (Symbiodiniaceae) partners (Voolstra *et al.*, *Nature Reviews Microbiology* 22:460–475, 4 March 2024, [doi:10.1038/s41579-024-01015-3](https://doi.org/10.1038/s41579-024-01015-3), [PMID 38438489](https://pubmed.ncbi.nlm.nih.gov/38438489/); Bourne, Morrow & Webster, *Annual Review of Microbiology* 70:317–340, 2016, [doi:10.1146/annurev-micro-102215-095440](https://doi.org/10.1146/annurev-micro-102215-095440), [PMID 27482741](https://pubmed.ncbi.nlm.nih.gov/27482741/)). It is anatomically a thin film of mucus and tissue over a voluminous, porous calcium carbonate skeleton, and each of those is a distinct microbial compartment with a distinct community (Ricci, Rossetto Marcelino, Blackall, Kühl, Medina & Verbruggen, *Microbiome* 7:159, 12 Dec 2019, [doi:10.1186/s40168-019-0762-y](https://doi.org/10.1186/s40168-019-0762-y), [PMID 31831078](https://pubmed.ncbi.nlm.nih.gov/31831078/); Li *et al.*, *Scientific Reports* 4:7320, 2014, [doi:10.1038/srep07320](https://doi.org/10.1038/srep07320)).

**The label is a two-part lexical compound, and this matters.** "Cnidaria-Corals" names *the phylum first and the dominant exemplar second*. The strain evidence confirms the wider reading is real, not nominal:

| Strain | Actual isolation source | Cnidarian class |
|---|---|---|
| *Endozoicomonas montiporae* CL-33ᵀ | encrusting pore coral *Montipora aequituberculata* | Anthozoa (Scleractinia) |
| *Corynebacterium maris* Coryn-1ᵀ (DSM 45190) | **mucus** of the coral *Fungia granulosa*, Gulf of Eilat | Anthozoa (Scleractinia) |
| *Endozoicomonas euniceicola*, *E. gorgoniicola* | octocorals *Eunicea fusca*, *Plexaura* sp. | Anthozoa (Octocorallia) |
| *Microbacterium aureliae* JF-6ᵀ | ***Aurelia aurita*, the moon jellyfish**, Bay of Bengal | **Scyphozoa — not a coral, not an anthozoan** |

Sources: Yang *et al.*, *IJSEM* 60:1158–1162, 2010 ([doi:10.1099/ijs.0.014357-0](https://doi.org/10.1099/ijs.0.014357-0), [PMID 19666790](https://pubmed.ncbi.nlm.nih.gov/19666790/)); Ben-Dov, Ben Yosef, Pavlov & Kushmaro, *IJSEM* 59:2458–2463, 2009 ([doi:10.1099/ijs.0.007468-0](https://doi.org/10.1099/ijs.0.007468-0)); Pike *et al.*, *IJSEM* 63:4294–4302, 2013 ([PMID 23832969](https://pubmed.ncbi.nlm.nih.gov/23832969/)); Kaur *et al.*, *IJSEM* 66:4665–4670, 2016 ([doi:10.1099/ijsem.0.001407](https://doi.org/10.1099/ijsem.0.001407), [PMID 27506590](https://pubmed.ncbi.nlm.nih.gov/27506590/)).

**Reading, stated explicitly.** The concept denotes **any cnidarian body as a microbial habitat, with corals as the dominant but not exclusive instance**. It is not "corals only". This is decisive for §2, because it means `mesh:D037421` *Anthozoa* — currently the record's sole xref and the note's proposed parent — is **narrower than the concept, not broader**: Anthozoa is one class *within* Cnidaria, and a moon-jellyfish isolate falsifies it.

**What is inside the boundary:** coral surface mucus layer, coral tissue, coral skeleton and its endolithic band, coral gastrovascular cavity, coral-associated microbial aggregates (CAMAs), coral larvae and mucus sheets; and the equivalent body compartments of octocorals/gorgonians, sea anemones, hydroids, and scyphozoan jellyfish.

**What is outside — neighbouring concepts:**
- **The reef as a place** — `ENVO:00000150` *coral reef*, already an EXACT-grounded record in this corpus (`data/habitats/aquatic/coral_reef.yaml`). The reef is a geographic/geomorphic feature built by corals; this concept is the animal's body.
- **Reef seawater, reef sediment, coral rubble, coral sand.** These are aquatic/sedimentary habitats that happen to sit on a reef.
- **`ENVO:01000852` *coral bleaching process*** — a process, not a place.

**Boundary noise in the source data (verified, and a caveat the curator should carry forward).** At least two of the 73 taxa are not from a cnidarian body:
- *Kosmotoga arenicorallina* S304ᵀ was isolated from **the Taketomi shallow submarine hydrothermal system occurring *within* a coral reef**, Yaeyama Archipelago, Japan — i.e. reef-hosted hot-spring sediment, not coral tissue (Nunoura *et al.*, *Archives of Microbiology* 192:811–819, 2010, [doi:10.1007/s00203-010-0611-7](https://doi.org/10.1007/s00203-010-0611-7), [PMID 20694719](https://pubmed.ncbi.nlm.nih.gov/20694719/)).
- *Nocardiopsis kunsanensis* HA-9ᵀ was isolated from **a saltern in Kunsan, Republic of Korea** (Chun *et al.*, *IJSEM* 50:1909–1913, 2000, [PMID 11034504](https://pubmed.ncbi.nlm.nih.gov/11034504/)). *Inference, not sourced:* the linkage to this category most likely comes from a non-type strain of the species deposited from a coral, since BacDive indexes strains rather than species; I could not verify which strain.

So roughly 3% of the attestations are reef-*locale* rather than host-*associated*. That is a lexical-aggregation artefact of the source category, not evidence that the concept means "the reef".

---

## 2. Genus — and the near-misses, one of which is a hit

### The match

**`ENVO:01001179` — *cnidarian-associated environment***
- Definition: *"An environmental system determined by a cnidarian or part of a cnidarian."*
- Direct parent: `ENVO:01001002` *animal-associated environment*; full chain `ENVO:01000254` *environmental system* → `ENVO:01001000` *environmental system determined by an organism* → `ENVO:01001002` → `ENVO:01001179`.
- `isObsolete: false`, `isDefiningOntology: true`, **no children** — so ENVO has no coral-specific subclass.
- Verified live at [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001179) and present in the vendored slice at `data/raw/ontology_terms.tsv:8673`, with the subclass edge at `data/raw/ontology_subclass_edges.tsv:6996`.

The wording — "a cnidarian **or part of a cnidarian**" — covers exactly the mucus/tissue/skeleton compartment structure that the sampling literature works in, and its extension is exactly the reading established in §1. **The label "Cnidaria-Corals" and the ENVO term "cnidarian-associated environment" pick out the same class.**

**The corpus already agrees.** `data/habitats/host_associated/coral.yaml` (`habitatmech:GOLD.a12eda25e9`, "Coral") is `grounding_status: NARROW` with `ENVO:01001179` attached as a parent, on a curation note that says so. That is the *narrower* GOLD concept. The present record — whose label names the phylum — has at least as good a claim to the term, arguably an EXACT one.

### The near-misses, and why each fails

| Candidate | Why it is a near-miss |
|---|---|
| `mesh:D037421` **Anthozoa** *(current xref / proposed parent)* | **Narrower than the concept, not broader.** Anthozoa is a class within Cnidaria; the concept demonstrably includes a scyphozoan (*M. aureliae* ex *Aurelia aurita*). Under the repo's rule that `parent_habitats` means *broader*, this cannot be a parent. Its provenance is a **lexical** match — `isolation_source_groundings.tsv:67` records `skos:closeMatch`, `medium` confidence, `semapv:LexicalMatching` via `ols4_search_synonym` — which matched the token "Corals" and silently dropped "Cnidaria". |
| `mesh:D003063` **Cnidaria** | Correct scope, present in the slice (`ontology_terms.tsv:13561`), and the right xref if the record keeps its own identity. But it is a **taxon term** — a class of organisms, not a place — so under CLAUDE.md's #99 rule it belongs in `relation: xref`, never as `parent`. It is also what the two sibling GOLD "Cnidaria" records already carry. |
| `ENVO:01001002` **animal-associated environment** | True but far too broad; it is the genus *one level above* the right answer. Correct fallback only if `ENVO:01001179` is rejected. |
| `ENVO:01001176` **environment associated with an aquatic invertebrate** | Broader, and structurally odd: it is a **sibling** of `ENVO:01001179` under `ENVO:01001002`, not its parent — so ENVO does not currently assert that cnidarian-associated environments are aquatic-invertebrate-associated environments. Using it would assert an is-a ENVO itself does not. |
| `ENVO:00000150` **coral reef** | A marine reef feature; the wrong kind of thing entirely (place built by corals vs. the coral's body). Already the identity of a separate AQUATIC record here. |
| `ENVO:01000049` / `ENVO:01000854` **marine (tropical) coral reef biome** | Biome-scale; asserts geography and climate the strain records do not claim. |
| `BTO:0006350` **polyp** / `BTO:0006151` **coral nubbin** | `polyp` is an anatomical form, `coral nubbin` an aquaculture artefact ("fragmented… attached to a substrate using Gorilla Glue"). Both far narrower and both assert things the sources do not. |
| `ENVO:01000852` **coral bleaching process** | A process. Not a habitat. |
| No **"coral-associated environment"** exists | Confirmed by OLS4 full-text search over ENVO for "coral" (16 hits, listed above; none is a host-associated class) and by `ENVO:01001179` having `hasDirectChildren: false`. |

---

## 3. Differentia — what distinguishes it from siblings under *animal-associated environment*

Should the curator proceed with a minted definition anyway, these are the defensible, observable differentiae. Each is sourced.

1. **Host clade — the only differentia ENVO itself uses at this level.** The determining organism is a cnidarian: a diploblastic metazoan with a single gastrovascular cavity and cnidocytes. This is what separates it from `ENVO:01001179`'s siblings (sponge-, fish-, human-associated).

2. **Compartmentalisation into mucus / tissue / skeleton.** Unlike most animal-associated environments, this one is routinely partitioned into three physically and microbiologically distinct compartments — surface mucus layer, soft tissue, and calcium carbonate skeleton — that harbour significantly different bacterial assemblages and respond differently to season (Li *et al.* 2014, [doi:10.1038/srep07320](https://doi.org/10.1038/srep07320); Ricci *et al.* 2019, [doi:10.1186/s40168-019-0762-y](https://doi.org/10.1186/s40168-019-0762-y)). Sampling method (mucus milking, tissue blasting, skeleton coring) determines which compartment you get, which is itself a documented comparability problem across studies (Ricci *et al.* 2019).

3. **A mineral endolithic compartment.** The aragonite skeleton is a porous, light-attenuated, redox-stratified habitat supporting endolithic algae (*Ostreobium*), fungi, and bacteria — a feature no soft-bodied animal host has (Ricci *et al.* 2019). Note this differentia applies to skeleton-forming anthozoans only, not to jellyfish or anemones; if the definition asserts it, the definition has silently narrowed to corals.

4. **Measurable enrichment over surrounding seawater.** Bacterial abundance in coral mucus ranged 5.3 × 10⁵ – 1.8 × 10⁶ cells ml⁻¹ versus 1.9 × 10⁵ – 4.2 × 10⁵ cells ml⁻¹ in surrounding seawater (Garren & Azam, *Applied and Environmental Microbiology* 76:6128–6133, 2010, [doi:10.1128/AEM.01100-10](https://doi.org/10.1128/AEM.01100-10), [PMC2937480](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2937480/)) — commonly cited as a 3–6× enrichment. Mucus-associated cells were also significantly *smaller* than seawater cells at every site (P < 0.0001). Compartment-level abundances are generally 10⁶–10⁷ cells ml⁻¹.

5. **Chemical distinctness.** Total organic carbon and nitrogen in coral mucus are 2–4× higher than in surrounding seawater (Tanaka *et al.*, cited in the mucus-production literature; see also Bourne *et al.* 2016).

6. **A characteristic, host-specific bacterial signature.** *Endozoicomonas* (Gammaproteobacteria, Endozoicomonadaceae) is a putative core coral taxon that forms dense intracellular/intratissue aggregates and can exceed 90% of total bacterial abundance in some corals (Neave *et al.*, *Applied Microbiology and Biotechnology* 100:8315–8324, 2016, [doi:10.1007/s00253-016-7777-0](https://doi.org/10.1007/s00253-016-7777-0), [PMC5018254](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5018254/); Pogoreutz & Ziegler, *Trends in Microbiology*, 2024, [doi:10.1016/j.tim.2023.11.008](https://doi.org/10.1016/j.tim.2023.11.008)). This is corroborated *within this record's own data*: three of the top-14 characteristic taxa are *Endozoicomonas* species, alongside a run of species epithets minted from the habitat itself — `coralii`, `coralli`, `coralicida`, `coralliicola`, `corallicola`, `isoporae`, `montiporae`, `gorgoniicola`, `euniceicola`, `madracius`.

7. **A mutualism–parasitism continuum, not a stable mutualism.** Recent genomic work reframes Endozoicomonadaceae associations as spanning beneficial and harmful functions rather than being fixed mutualists (Neave *et al.*, *Nature Communications* 14, 2023, [doi:10.1038/s41467-023-38502-9](https://doi.org/10.1038/s41467-023-38502-9); *Communications Biology*, 2025, [doi:10.1038/s42003-025-08828-9](https://doi.org/10.1038/s42003-025-08828-9)). A definition should therefore **not** assert that the resident microbiota are symbionts or beneficial — the category also contains named coral pathogens (*Aurantimonas coralicida*, the white-plague type II agent; several *Vibrio* spp.).

---

## 4. Sources

All cited inline above. Consolidated, with what each supports:

| Source | Supports |
|---|---|
| Voolstra, Raina, Dörr, Cárdenas, Pogoreutz, Silveira, Mohamed, Bourne, Luo, Amin & Peixoto. *Nat Rev Microbiol* 22:460–475 (2024). [doi:10.1038/s41579-024-01015-3](https://doi.org/10.1038/s41579-024-01015-3) · [PMID 38438489](https://pubmed.ncbi.nlm.nih.gov/38438489/) · [open copy](https://hal.science/hal-04495591v1) | Holobiont definition; current state of coral microbiome science |
| Bourne, Morrow & Webster. *Annu Rev Microbiol* 70:317–340 (2016). [doi:10.1146/annurev-micro-102215-095440](https://doi.org/10.1146/annurev-micro-102215-095440) | Holobiont/hologenome framing; corals as ecosystem engineers |
| Ricci, Rossetto Marcelino, Blackall, Kühl, Medina & Verbruggen. *Microbiome* 7:159 (2019). [doi:10.1186/s40168-019-0762-y](https://doi.org/10.1186/s40168-019-0762-y) · [PMID 31831078](https://pubmed.ncbi.nlm.nih.gov/31831078/) | Skeleton as a distinct endolithic habitat; compartment sampling artefacts |
| Li, Chen, Zhang, Huang, Wang, Cai, Luo, Curdt & Dong. *Sci Rep* 4:7320 (2014). [doi:10.1038/srep07320](https://doi.org/10.1038/srep07320) | Mucus/tissue/skeleton communities differ from each other and from seawater |
| Garren & Azam. *Appl Environ Microbiol* 76:6128–6133 (2010). [doi:10.1128/AEM.01100-10](https://doi.org/10.1128/AEM.01100-10) | Quantitative mucus vs. seawater cell abundances |
| Neave, Apprill, Ferrier-Pagès & Voolstra. *Appl Microbiol Biotechnol* 100:8315–8324 (2016). [doi:10.1007/s00253-016-7777-0](https://doi.org/10.1007/s00253-016-7777-0) | *Endozoicomonas* dominance, >90% of community |
| Neave *et al.* *Nat Commun* 14 (2023). [doi:10.1038/s41467-023-38502-9](https://doi.org/10.1038/s41467-023-38502-9) | Endozoicomonadaceae ecology across Pacific coral genera |
| Maire *et al.* *Sci Adv* 9 (2023). [doi:10.1126/sciadv.adg0773](https://doi.org/10.1126/sciadv.adg0773) | CAMAs — coral-associated microbial aggregates as a within-tissue microhabitat |
| Reimer, Sardà Carbasse, Koblitz, Ebeling, Podstawka & Overmann. *Nucleic Acids Res* 50:D741–D746 (2022). [doi:10.1093/nar/gkab961](https://doi.org/10.1093/nar/gkab961) | BacDive isolation-source classification (the source vocabulary) |
| Buttigieg, Morrison, Smith, Mungall & Lewis. *J Biomed Semantics* 4:43 (2013). [doi:10.1186/2041-1480-4-43](https://doi.org/10.1186/2041-1480-4-43) · [PMC3904460](https://pmc.ncbi.nlm.nih.gov/articles/PMC3904460/) | ENVO's environmental-system / feature modelling; the "single influential entity" pattern that `ENVO:01001179` instantiates |
| Buttigieg *et al.* *J Biomed Semantics* 7:57 (2016). [PMC5035502](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/) | ENVO's post-2013 host-associated expansion — relevant to `ENVO:01001179`'s bulk-generated provenance and thin axiomatisation |
| [OLS4: ENVO:01001179](https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001179) | Term exists, definition, parent, no children, not obsolete |
| Type-strain descriptions: Yang 2010 ([doi:10.1099/ijs.0.014357-0](https://doi.org/10.1099/ijs.0.014357-0)); Ben-Dov 2009 ([doi:10.1099/ijs.0.007468-0](https://doi.org/10.1099/ijs.0.007468-0)); Pike 2013 ([PMID 23832969](https://pubmed.ncbi.nlm.nih.gov/23832969/)); Kaur 2016 ([doi:10.1099/ijsem.0.001407](https://doi.org/10.1099/ijsem.0.001407)); Nunoura 2010 ([doi:10.1007/s00203-010-0611-7](https://doi.org/10.1007/s00203-010-0611-7)); Chun 2000 ([PMID 11034504](https://pubmed.ncbi.nlm.nih.gov/11034504/)) | The actual isolation sources behind the record's characteristic taxa, incl. the jellyfish isolate and the two boundary-noise strains |

**Marked as inference, not sourced by any of the above:**
- That "Cnidaria-Corals" as a *category label* is intended by BacDive to span the phylum with corals as exemplar. The label's word order and the *M. aureliae* membership support it; BacDive publishes no gloss for the category.
- That the *N. kunsanensis* linkage comes from a non-type strain.
- That ~3% boundary noise is "an aggregation artefact" — my characterisation of two verified mismatches.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- coral-associated environment; coral host environment
- coral holobiont *(strictly the host + microbiota as a unit, so a near-synonym that also names the biological entity)*
- cnidarian-associated environment *(the ENVO label)*
- coral microbiome *(names the community, commonly used metonymically for the habitat)*
- coral-associated habitat; coral tissue / coral mucus / coral skeleton *(compartment-level names, all narrower)*
- octocoral-, gorgonian-, scleractinian-, anemone-, jellyfish-associated environment *(host-clade-specific, all narrower)*

**Commonly but wrongly treated as the same thing**
- **Coral reef** (`ENVO:00000150`) and **marine coral reef biome** (`ENVO:01000049`). The single most frequent conflation in this domain. The reef is a mineral geographic feature and an ecosystem; this concept is an animal body. They coincide in space and differ in kind, and this corpus already keeps them apart as separate records.
- **Reef seawater / reef sediment / coral rubble / coral sand.** Adjacent, not identical — this is precisely where *Kosmotoga arenicorallina* actually came from.
- **Anthozoa** (`mesh:D037421`). Narrower than the concept (see §2), and in any case a taxon rather than a place.
- **Cnidaria** (`mesh:D003063`), **NCBITaxon:6073**. Right scope, wrong kind of entity — organism classes, not environments. Correct as `relation: xref`.
- **Symbiodiniaceae / zooxanthellae.** The dinoflagellate partner is a *member* of the holobiont, not the habitat.
- **Coral bleaching** (`ENVO:01000852`). A process affecting the habitat.
- **Coral nubbin** (`BTO:0006151`). An aquaculture preparation of a coral fragment — an experimental artefact, not this concept.
- **Aquarium / mesocosm coral.** Many strains in categories like this come from captive corals; the source data does not distinguish wild from aquarium origin, and neither should the definition claim wild provenance.

---

## 6. Should this be a term at all? — recommendation

**It is unambiguously a habitat.** An organism acting as a host is where microbes live; ENVO models exactly this, and the coral case is one of the best-characterised host-associated microbial habitats in marine microbiology. The record's `CONFIRM_UNGROUNDED` note is right on that point and the earlier `NOT_APPLICABLE` was wrong. Nothing here suggests a process, quality, disease, or sampling artefact.

**But the note's premise — "no ontology term fits this concept" — does not survive checking, and I'd flag two things for re-curation:**

**(a) `ENVO:01001179` fits, and it is already in the vendored slice.** Its definition is a paraphrase of what §1 establishes the concept denotes. My recommendation is `GROUND` to `ENVO:01001179` *cnidarian-associated environment*, at `EXACT` if the curator accepts the phylum-level reading of the label, or `NARROW` (term as parent, own identity retained) if they judge that "Corals" narrows it enough to matter. Grounding also has the useful side effect of moving the record out of `habitat_category: OTHER` — it is `HOST_ASSOCIATED`, which is where every sibling cnidarian record already sits.

**(b) Independently of (a), `mesh:D037421` *Anthozoa* should not become a `parent`.** It is narrower than the concept, its provenance is a medium-confidence lexical match that dropped half the label, and a jellyfish-derived type strain in the record's own `characteristic_taxa` contradicts it. If the record keeps a mesh xref, `mesh:D003063` *Cnidaria* (also in the slice) is the one that matches the label — and as `relation: xref`, per the #99 rule, since it is a taxon.

**Only if the curator rejects (a)** — e.g. on the ground that `ENVO:01001179` is an `envoMeo`-tagged, bulk-derived class with thin axiomatisation — does a minted definition apply. In that case use the sentence at the top of this report, with `ENVO:01001002` *animal-associated environment* as the ontology genus, and file an ENVO term request for *coral-associated environment* as a child of `ENVO:01001179` (which currently has none). **Per your standing rule, that request would need your explicit per-request yes before submission; I have not drafted or filed anything.**

One structural note worth an issue regardless of the decision: `ENVO:01001179` sits directly under `ENVO:01001002` *animal-associated environment* rather than under its sibling `ENVO:01001176` *environment associated with an aquatic invertebrate*. That is an ENVO classification gap, not a HabitatMech one, but it means a curator cannot rely on `ENVO:01001176` transitively covering cnidarians.

## Citations

1. https://doi.org/10.1093/nar/gkab961
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC8728306/
3. https://doi.org/10.1038/s41579-024-01015-3
4. https://pubmed.ncbi.nlm.nih.gov/38438489/
5. https://doi.org/10.1146/annurev-micro-102215-095440
6. https://pubmed.ncbi.nlm.nih.gov/27482741/
7. https://doi.org/10.1186/s40168-019-0762-y
8. https://pubmed.ncbi.nlm.nih.gov/31831078/
9. https://doi.org/10.1038/srep07320
10. https://doi.org/10.1099/ijs.0.014357-0
11. https://pubmed.ncbi.nlm.nih.gov/19666790/
12. https://doi.org/10.1099/ijs.0.007468-0
13. https://pubmed.ncbi.nlm.nih.gov/23832969/
14. https://doi.org/10.1099/ijsem.0.001407
15. https://pubmed.ncbi.nlm.nih.gov/27506590/
16. https://doi.org/10.1007/s00203-010-0611-7
17. https://pubmed.ncbi.nlm.nih.gov/20694719/
18. https://pubmed.ncbi.nlm.nih.gov/11034504/
19. https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001179
20. https://doi.org/10.1128/AEM.01100-10
21. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2937480/
22. https://doi.org/10.1007/s00253-016-7777-0
23. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5018254/
24. https://doi.org/10.1016/j.tim.2023.11.008
25. https://doi.org/10.1038/s41467-023-38502-9
26. https://doi.org/10.1038/s42003-025-08828-9
27. https://hal.science/hal-04495591v1
28. https://doi.org/10.1126/sciadv.adg0773
29. https://doi.org/10.1186/2041-1480-4-43
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC3904460/
31. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/