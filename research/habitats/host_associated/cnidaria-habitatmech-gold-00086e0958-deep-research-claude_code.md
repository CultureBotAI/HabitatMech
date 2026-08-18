---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T20:30:40.089056'
end_time: '2026-08-17T20:38:12.755151'
duration_seconds: 452.67
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Cnidaria
  habitat_identifier: habitatmech:GOLD.00086e0958
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Invertebrates > Cnidaria'
  assertions: '102'
  parent_terms: (none)
  xrefs: mesh:D003063
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term mesh:D003063 'Cnidaria' attached as a parent. Host-taxon reversal\
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
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.00086e0958)"
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
  num_turns: 32
  total_cost_usd: 3.127758
  session_id: 63686faa-8679-464f-a787-8a87b502a311
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 18
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Cnidaria
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.00086e0958
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Invertebrates > Cnidaria
- **Upstream assertion volume:** 102
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** mesh:D003063

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term mesh:D003063 'Cnidaria' attached as a parent. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.00086e0958)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Cnidaria** as a microbial habitat, with citations.

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

I'll research this now.

Important — ENVO may already have this term. Verifying.

## Recommendation up front: this concept should not get a minted term — ENVO already names it

**`ENVO:01001179` "cnidarian-associated environment" — *"An environmental system determined by a cnidarian or part of a cnidarian."*** It is an active (non-obsolete) ENVO class in the `envoMeo` subset, a direct `rdfs:subClassOf` of `ENVO:01001002` animal-associated environment, and **it is already in this repo's vendored slice** (`data/raw/ontology_terms.tsv:8673`; edge at `data/raw/ontology_subclass_edges.tsv:6996`). The corpus already uses it: `data/habitats/host_associated/coral.yaml` carries it as a parent, and that record's own decision note (`curation/decisions.tsv:1557`) says in as many words:

> "Kept as a narrower kind of cnidarian-associated environment rather than grounded to it, **because Host-associated > Cnidaria is the shallower path entitled to that term**."

That entitled path is this concept. The `CONFIRM_UNGROUNDED` on `habitatmech:GOLD.00086e0958` ("no ontology term fits this concept") is therefore false, and its recorded parent `mesh:D003063` is a taxon term standing in for an environment term that exists.

Why the seeder missed it is mechanical, not conceptual: GOLD's leaf label is `Cnidaria`, ENVO's label is `cnidarian-associated environment`, and no lexical route (`gold_composed_label`, `gold_composed_synonym`, leaf label/synonym) matches across that gap. The same gap is why `ENVO:01001001` plant-associated and `ENVO:01001041` fungi-associated never auto-attached either.

So the proposed one-sentence definition below is offered **only** for the case where a curator decides HabitatMech must still carry prose; it is deliberately co-extensive with ENVO's:

> An animal-associated environment which is determined by a cnidarian — an aquatic, diploblastic, cnidocyte-bearing metazoan of the phylum Cnidaria — or by one of its parts, comprising the surface mucus layer, epidermal and gastrodermal tissue, gastrovascular cavity and, in calcifying forms, the skeleton.

---

## 1. What the concept denotes

The sample-able thing is **a cnidarian animal acting as host** — the whole organism, not a body part and not the reef structure. GOLD's path `Host-associated > Invertebrates > Cnidaria` (`gold.ecosystem:3564`, 102 ORGANISM assertions) sits directly above `… > Cnidaria > Coral` and, below that, `> Coral > Tissue`, `> Coral > Mucus`, `> Coral > Surface`. That hierarchy fixes the reading: this node is the **whole-phylum host level**, used when a metagenome/isolate came from a cnidarian but the source was not resolved to coral, and not to a compartment.

Boundaries:

| Inside | Neighbouring concept |
|---|---|
| Corals (Scleractinia, Alcyonacea, Antipatharia), sea anemones (Actiniaria), *Hydra* and other hydrozoans, true/box/stalked jellyfish, hydroids | `… > Cnidaria > Coral` (`habitatmech:GOLD.a12eda25e9`) — a narrower host clade, already `GROUND_AS_PARENT`/`NARROW` |
| Whole-animal samples, homogenates, "coral-associated" isolates not resolved to compartment | Coral tissue / mucus / surface — cnidarian *parts*; ENVO's "or part of a cnidarian" covers them, GOLD splits them out |
| Cnidarian surfaces including the diffusive boundary layer chemically controlled by the host | `ENVO:00000150` coral reef / `ENVO:01000049` marine coral reef biome — geological/biome entities built largely of dead skeleton, not a host organism |
| The cnidarian's own dinoflagellate endosymbionts as part of the holobiont environment | Cultured Symbiodiniaceae (a distinct source; only 2.6 % of cultured-Symbiodiniaceae microbiota overlapped cnidarian samples, [McCauley et al. 2023](https://www.nature.com/articles/s41467-023-39876-6)) |

**One genuine ambiguity, and it is not in the label — it is in the corpus.** Two GOLD paths end in "Cnidaria":

- `Host-associated > Cnidaria` — depth 2, 95 assertions → `habitatmech:GOLD.e3fede2aea` (`cnidaria__e1ee42c6.yaml`)
- `Host-associated > Invertebrates > Cnidaria` — depth 3, 102 assertions → `habitatmech:GOLD.00086e0958` (this concept)

Both are `UNGROUNDED`, both carry the identical `CONFIRM_UNGROUNDED` note, and both denote the same thing: the two paths differ only by GOLD's inconsistent insertion of an "Invertebrates" rank, not by any property of the habitat. Under the seeder's ambiguous-leaf rule the *shallowest* path claims the term — which is `GOLD.e3fede2aea`, **not** this record. But the sediment rationale behind that rule (marine vs. freshwater vs. hot-spring sediment are different places) does not apply here, because nothing distinguishes the two paths. My recommendation is to ground **both** to `ENVO:01001179`, which merges them into one record carrying both attestations (197 ORGANISM assertions), rather than publishing one grounded record and one `NARROW` minted near-duplicate. If a curator prefers to preserve the shallowest-claims-it convention mechanically, the alternative is `SAME_AS` from `GOLD.00086e0958` onto `GOLD.e3fede2aea` — the mechanism added in #116/#117 and used once already for BacDive Human → GOLD Mammals: Human (`curation/decisions.tsv:77`). Either way the two should not stay as two.

## 2. Genus — the broader kind

**`ENVO:01001002` "animal-associated environment"** ("An environmental system determined by an animal") is the genus, and it is ENVO's own asserted parent of `ENVO:01001179`. It is in the slice. This is the term the corpus already uses as the ontology parent for the `Invertebrates` node (`invertebrates.yaml`).

Near-misses, and why each fails as *identity*:

- **`ENVO:01001176` "environment associated with an aquatic invertebrate"** — in the slice; ENVO's definition: *"An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system."* This is a plausible *intermediate* genus and is arguably a better parent than bare `ENVO:01001002`, since all cnidarians are aquatic. It fails as identity because it is far broader — it also covers sponges, molluscs, annelids, crustaceans. Note ENVO does **not** assert `01001179 subClassOf 01001176`; both hang directly off `01001002`. Attaching it here would be a curator's inference, not ENVO's assertion. (The crustaceans record rejected this term for the opposite reason — terrestrial crustaceans fall outside it; that objection does not apply to Cnidaria.)
- **`ENVO:01001055` "environment associated with an animal part or small animal"** — for parts and small whole animals; the coral *mucus*/*tissue* children live in this neighbourhood, not the whole-phylum host node.
- **`ENVO:00000150` coral reef, `ENVO:01000049`/`01000854` marine coral reef biome, `ENVO:01000024` marine benthic biome** — geographic features and biomes. A reef is a place *containing* corals plus water, algae, sediment and dead framework; grounding a host-associated concept here would assert a marine, shallow, reef setting that the GOLD node never claims (it also covers freshwater *Hydra* and aquarium/lab anemones).
- **`ENVO:01000852` coral bleaching process** — a process, not a habitat.
- **`NCBITaxon:6073` / `mesh:D003063` / `SNOMED:106900006` "Cnidaria"** — taxon terms; a phylum is a class of organisms, not a place (#99, #114). These belong in `xrefs` with `relation: xref`, which is what the current decision row does.

## 3. Differentia — what distinguishes it

If the ENVO grounding is taken, the differentia is ENVO's ("determined by a cnidarian"). The observable properties that back it, and would justify the term against sibling animal-associated environments:

- **Host body plan.** Cnidarians are diploblastic — two epithelial layers (epidermis, gastrodermis) separated by acellular mesoglea, with a single gastrovascular opening serving as mouth and anus. This gives microbes an unusually thin, directly seawater-exposed epithelium rather than a through-gut, and it is why *Hydra* became a model for epithelial microbiota control ([Fraune & Bosch 2007, *PNAS* 104:13146–13151](https://www.pnas.org/doi/full/10.1073/pnas.0703375104), doi:10.1073/pnas.0703375104).
- **A defined set of host-supplied microhabitats.** Surface mucus layer (a polysaccharide–protein–lipid interface with the water column), tissue, gastrovascular cavity, and — in calcifiers — an aragonite skeleton hosting an endolithic community ([Bourne, Morrow & Webster 2016, *Annu Rev Microbiol* 70:317–340](https://www.annualreviews.org/content/journals/10.1146/annurev-micro-102215-095440), doi:10.1146/annurev-micro-102215-095440, PMID 27482741; [Ricci et al. 2019, *Microbiome* 7:159](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-019-0762-y), PMID 31831078). Compartment is a first-order determinant of community composition: in the 12,010-sample synthesis, skeleton samples were the most colony-specific (68.7 % of their ASVs unique to a single colony) ([McCauley et al. 2023](https://www.nature.com/articles/s41467-023-39876-6)). The same compartment structure holds in medusozoans: exumbrella mucus and gastric cavity of *Aurelia aurita* carry significantly different communities ([Weiland-Bräuer et al. 2015, *Appl Environ Microbiol* 81:6038–6052](https://journals.asm.org/doi/10.1128/aem.01601-15), doi:10.1128/AEM.01601-15, PMID 26116680).
- **Photosymbiosis-driven physicochemistry.** In photosymbiotic cnidarians, Symbiodiniaceae photosynthesis and holobiont respiration drive extreme diel O₂ and pH swings across the diffusive boundary layer — hyperoxia in light, hypoxia to anoxia in darkness — over micrometre-to-millimetre distances ([Shashar, Cohen & Loya 1993, *Biol Bull* 185:455–461](https://www.journals.uchicago.edu/doi/10.2307/1542485); [Linsmayer et al. 2020, *Sci Rep* 10:19881](https://www.nature.com/articles/s41598-020-76828-2)). This is a measurable property of the habitat, not of the taxon, and it is the strongest differentia against, say, a mollusc- or fish-associated environment.
- **A distinctive and phylum-wide microbiota.** *Endozoicomonas* is the bacterial genus most ubiquitously associated with Cnidaria globally, residing in tissue aggregates and spanning stony corals, octocorals and sea anemones ([Neave et al. 2016, *Appl Microbiol Biotechnol* 100:8315–8324](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5018254/), doi:10.1007/s00253-016-7777-0; the mutualist framing is now contested — [Maire et al., *Trends Microbiol*, "Frenemies on the reef?"](https://www.cell.com/trends/microbiology/abstract/S0966-842X(23)00323-2)). Across 186 studies, 212 host species, 4 classes and 12 orders, McCauley et al. recovered 86 archaeal and bacterial phyla and identified *Endozoicomonas*, *Vibrio*, *Pseudoalteromonas*, *Alteromonas* and the cyanobacterial genus GpIIa as recurrent, plus ubiquitous non-bacterial members (ARL-V apicomplexans across seven orders; *Ostreobium* in scleractinians, octocorals and antipatharians).
- **Host dependence on the microbiome is demonstrated, not assumed.** Aposymbiotic *A. aurita* polyps fail to strobilate normally, a defect rescued by recolonisation with a native polyp microbiome ([Jensen et al. 2023, *Microbiol Spectr*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10433978/)) — the functional evidence that the animal is a structured habitat, not incidental substrate.
- **Aquatic, but not marine-only.** Cnidaria is recorded by WoRMS as marine, brackish and fresh; Hydrozoa contains all the freshwater forms ([WoRMS AphiaID 1267](https://www.marinespecies.org/aphia.php?p=taxdetails&id=1267)). Any definition that says "marine" over-claims — the *Hydra* literature above is freshwater.

*Inference flag:* the claim that these properties collectively make cnidarian-associated environments distinguishable from other animal-associated environments is **my synthesis**; no single source states it as a definitional criterion. Each individual property is sourced above.

## 4. Sources

Beyond those cited inline:

- ENVO:01001179 — [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179); ENVO modelling of organism-determined environments: [Buttigieg et al. 2016, *J Biomed Semantics* 7:57](https://jbiomedsem.biomedcentral.com/articles/10.1186/s13326-016-0097-6), doi:10.1186/s13326-016-0097-6, PMID 27664130.
- MeSH D003063 Cnidaria — *"A phylum of radially symmetrical invertebrates characterized by possession of stinging cells called nematocysts"*, tree number B01.050.500.308 ([MeSH Browser](https://meshb.nlm.nih.gov/record/ui?ui=D003063)). Note this is a taxon descriptor under Organisms, which is exactly why it is the wrong thing to hold as a habitat parent.
- Myxozoa (obligate endoparasites of fish and annelids) are cnidarians — [Chang et al. 2015, *PNAS* 112:14912–14917](https://www.pnas.org/doi/10.1073/pnas.1511468112), doi:10.1073/pnas.1511468112. This is a real edge of the concept: a myxozoan-associated microbial sample would be "cnidarian-associated" by phylogeny while physically sitting inside a fish. No GOLD path exercises it; flagged, not resolved.
- Chlamydiae across corals, jellyfish and anemones — [*ISME Communications* 4:ycae054 (2024)](https://academic.oup.com/ismecommun/article/4/1/ycae054/7645737).
- Molecular mechanisms of coral–microbiota interaction — [*FEMS Microbiol Rev* 47(2):fuad005 (2023)](https://academic.oup.com/femsre/article/47/2/fuad005/7071893).

## 5. Synonyms, and what not to conflate

**In real use for this concept:** cnidarian-associated environment; cnidarian host; cnidarian holobiont environment; coelenterate-associated environment (dated — "Coelenterata" also swept in ctenophores). GOLD writes it as the bare taxon name `Cnidaria`; BacDive writes a nearby but narrower category as `Cnidaria-Corals` (`bacdive.isolation_source:cnidaria-corals`, 75 strains, upstream-mapped to `mesh:D037421` Anthozoa).

**Do not conflate with:**

- **Coral reef** (`ENVO:00000150`) — a geographic feature; most of a reef is not living cnidarian.
- **The taxon Cnidaria** (`NCBITaxon:6073`, `mesh:D003063`, `SNOMED:106900006`) — a class of organisms.
- **Coral-associated** — narrower; corals are a subset of Cnidaria, and the corpus already models it that way.
- **Ctenophora** (comb jellies) — "jellyfish" colloquially covers both; they are a separate phylum, and the *Mnemiopsis leidyi* microbiome literature sits alongside, not inside, this concept.
- **Cultured Symbiodiniaceae** — the symbiont in isolation is not the host environment (2.6 % overlap, McCauley et al. 2023).
- **`ENVO:01000852` coral bleaching process** and cnidarian envenomation (`SNOMED:1251365008`) — a process and a disorder.

## 6. Should this be a term at all?

**It should be a *grounding*, not a term.** The concept is unambiguously a habitat — an organism acting as host, which is exactly what ENVO models at plant-/animal-/fungi-associated environment — and ENVO has already minted the class for it. Manufacturing a HabitatMech definition here would publish a permanent minted identifier duplicating `ENVO:01001179`, which is the failure mode the "no term names it" precondition exists to prevent.

Concretely, what I'd put in `curation/decisions.tsv`:

| identifier | decision | object_id | object_label | grounding_status | relation |
|---|---|---|---|---|---|
| `habitatmech:GOLD.e3fede2aea` | `GROUND` | `ENVO:01001179` | `cnidarian-associated environment` | `EXACT` | |
| `habitatmech:GOLD.00086e0958` | `GROUND` (or `SAME_AS habitatmech:GOLD.e3fede2aea`) | `ENVO:01001179` | `cnidarian-associated environment` | `EXACT` | |

Two things a curator should check before writing those rows, because I could not settle them from the data alone:

1. **The `mesh:D003063` xref.** Porifera carries `NCBITaxon:6040`; Cnidaria carries a MeSH descriptor, almost certainly because an OLS lexical search returned MeSH first. `NCBITaxon:6073` would be the consistent xref — **but it is not in the vendored slice** (only 31 NCBITaxon terms are, and 6073 is not among them), so proposing it would fail the term-existence check in `tests/test_decisions.py` until the taxon is vendored (#10). Leaving `mesh:D003063` as `relation: xref` is defensible in the meantime.
2. **Whether coral should be re-examined.** `GOLD.a12eda25e9` (coral) is `GROUND_AS_PARENT ENVO:01001179 / NARROW` — that decision was correct and stays correct once the parent is actually grounded rather than sitting under an UNGROUNDED minted record.

Sources: [ENVO:01001179 (OLS4)](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179) · [ENVO:01001176](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176) · [Buttigieg et al. 2016](https://jbiomedsem.biomedcentral.com/articles/10.1186/s13326-016-0097-6) · [McCauley et al. 2023, *Nat Commun* 14:4899](https://www.nature.com/articles/s41467-023-39876-6) · [Bourne, Morrow & Webster 2016](https://www.annualreviews.org/content/journals/10.1146/annurev-micro-102215-095440) · [Ricci et al. 2019](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-019-0762-y) · [Fraune & Bosch 2007](https://www.pnas.org/doi/full/10.1073/pnas.0703375104) · [Weiland-Bräuer et al. 2015](https://journals.asm.org/doi/10.1128/aem.01601-15) · [Jensen et al. 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10433978/) · [Neave et al. 2016](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5018254/) · [Maire et al., *Trends Microbiol*](https://www.cell.com/trends/microbiology/abstract/S0966-842X(23)00323-2) · [Shashar et al. 1993](https://www.journals.uchicago.edu/doi/10.2307/1542485) · [Linsmayer et al. 2020](https://www.nature.com/articles/s41598-020-76828-2) · [Chang et al. 2015](https://www.pnas.org/doi/10.1073/pnas.1511468112) · [ISME Commun 4:ycae054](https://academic.oup.com/ismecommun/article/4/1/ycae054/7645737) · [FEMS Microbiol Rev 47:fuad005](https://academic.oup.com/femsre/article/47/2/fuad005/7071893) · [WoRMS Cnidaria](https://www.marinespecies.org/aphia.php?p=taxdetails&id=1267) · [MeSH D003063](https://meshb.nlm.nih.gov/record/ui?ui=D003063)

## Citations

1. https://www.nature.com/articles/s41467-023-39876-6
2. https://www.pnas.org/doi/full/10.1073/pnas.0703375104
3. https://www.annualreviews.org/content/journals/10.1146/annurev-micro-102215-095440
4. https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-019-0762-y
5. https://journals.asm.org/doi/10.1128/aem.01601-15
6. https://www.journals.uchicago.edu/doi/10.2307/1542485
7. https://www.nature.com/articles/s41598-020-76828-2
8. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5018254/
9. https://www.cell.com/trends/microbiology/abstract/S0966-842X(23
10. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10433978/
11. https://www.marinespecies.org/aphia.php?p=taxdetails&id=1267
12. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179
13. https://jbiomedsem.biomedcentral.com/articles/10.1186/s13326-016-0097-6
14. https://meshb.nlm.nih.gov/record/ui?ui=D003063
15. https://www.pnas.org/doi/10.1073/pnas.1511468112
16. https://academic.oup.com/ismecommun/article/4/1/ycae054/7645737
17. https://academic.oup.com/femsre/article/47/2/fuad005/7071893
18. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176