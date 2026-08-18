---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T21:06:41.914138'
end_time: '2026-08-17T21:15:09.272953'
duration_seconds: 507.36
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Porifera-Sponges
  habitat_identifier: habitatmech:BACDIVE.18f9382d8d
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Porifera-Sponges'
  assertions: '86'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Host-taxon\
    \ reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon\
    \ is not a habitat'. That reasoning is wrong, and the corpus already contradicted\
    \ it \u2014 the same kind of concept was treated as a habitat for Sponge, Nematoda,\
    \ Reptilia, Mammals, Birds and Fish, which keep their own identity and a term\
    \ request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE\
    \ while its own child Porifera > Sponge was a term request.An organism acting\
    \ as a host IS a habitat: it is where the microbe lives, and ENVO models exactly\
    \ this at plant-associated, animal-associated and fungi-associated environment.\
    \ What is not a habitat is the TAXON TERM \u2014 a phylum is a class of organisms,\
    \ not a place \u2014 so the taxon stays an xref (#99) and the concept keeps its\
    \ own identity as a term-request candidate. NOT_APPLICABLE said the concept is\
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:BACDIVE.18f9382d8d)"
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
  web_search_requests: 18
  num_turns: 26
  total_cost_usd: 3.360327
  session_id: f8729646-8c9c-4641-95b5-c79633be1d2a
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 35
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Porifera-Sponges
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.18f9382d8d
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Porifera-Sponges
- **Upstream assertion volume:** 86
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:BACDIVE.18f9382d8d)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Porifera-Sponges** as a microbial habitat, with citations.

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

# Definition research: *Porifera-Sponges* (`habitatmech:BACDIVE.18f9382d8d`)

> **Proposed definition:** An environment associated with an aquatic invertebrate which is determined by the body of a sponge (phylum Porifera) — its pinacoderm surface, water canal system, and mesohyl matrix — and which sustains a microbial community compositionally distinct from the surrounding water.

Genus is `ENVO:01001176` *environment associated with an aquatic invertebrate*, which already exists and is the tightest fit; the differentia is host identity (Porifera) plus the mesohyl-centred body plan the symbionts occupy. If the curator prefers to stay one level higher, `ENVO:01001002` *animal-associated environment* also works and is what the sibling GOLD `Sponge` record used — but it is looser than necessary (see §2).

---

## 1. What the concept denotes

**The reading the data means.** The label is a BacDive isolation-source category, not a free-text sample description. BacDive's isolation-source classification places it under Category 1 `#Host`, with `#Porifera (Sponges)` as the host-group level ([BacDive isolation sources browser](https://bacdive.dsmz.de/isolation-sources); [Reimer et al. 2019, *Nucleic Acids Res*, BacDive in 2019, PMC6323973](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/)). So the concept is **the sponge as a host — the place a strain was recovered from** — and the compound label is BacDive's convention of pairing the phylum name with its common name, not two concepts.

**The thing a sample is taken from.** In practice the sample is sponge body material: whole-animal homogenate, excised tissue, surface swab, or dissected mesohyl. The mesohyl is where the bulk of the symbiont load sits — PORO defines it as "an extracellular matrix enclosed by pinacoderm and choanoderm … The mesohyl contains cells (microbial and eukaryotic) and skeletal elements" ([PORO:0000002](https://www.ebi.ac.uk/ols4/ontologies/poro/classes?obo_id=PORO:0000002), citing Boury-Esnault & Rützler 1997; Müller 2003). Symbiotic consortia are located extracellularly in the mesohyl, concentrated around choanocyte chambers, with some species also hosting endosymbionts inside bacteriocytes and phototrophs beneath the pinacoderm ([Hentschel et al. 2012, *Nat Rev Microbiol* 10:641–654, doi:10.1038/nrmicro2839](https://www.nature.com/articles/nrmicro2839)).

**Inside the concept:** any sponge, any class (Demospongiae, Hexactinellida, Calcarea, Homoscleromorpha), marine *or* freshwater; any body compartment of that sponge (surface, canal lining, mesohyl, tissue, larvae/reproductive stages).

**Outside the concept (neighbouring):**
- The **seawater the sponge filters** — a distinct environment, and the microbiological literature's whole point is that the two differ by 2–4 orders of magnitude in cell density and by composition ([Hentschel, Usher & Taylor 2006, *FEMS Microbiol Ecol* 55:167–177, doi:10.1111/j.1574-6941.2005.00046.x](https://academic.oup.com/femsec/article/55/2/167/595128)).
- The **sponge reef** — a geomorphic/benthic feature built by hexactinellids, already `ENVO:01000161` *marine sponge reef* and `ENVO:01000123` *marine sponge reef biome*. That is the landscape a sponge builds, not the sponge body.
- The **taxon Porifera** as a class of organisms (`NCBITaxon:6040`). A phylum is not a place; this is exactly the distinction #99/#114 turn on.

**Ambiguity.** The bare English word "sponge" is heavily homonymous, and the upstream data is not ambiguous but a lexical matcher over it would be. Readings that are *not* meant here: manufactured absorbent pads (`NCIT:C42856` "Sponge" — "a soft flexible, absorbent pad usually made from natural material such as gauze or cotton, used to absorb blood and other fluids, as in surgery"; multiple SNOMED "Sponge" concepts including `SNOMED:714058007` surgical sponge-counting tray); "spongy" as a texture (`ENVO:06105016` *foamed plastic*, "a plastic which has a matrix- or sponge-like structure"); bath sponges as a commodity. Only the Porifera-host reading is supported by the source path.

---

## 2. Genus — the broader kind

**Recommended: `ENVO:01001176` *environment associated with an aquatic invertebrate*.**
ENVO definition: "An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system" ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176)) — *sic*, the typo is ENVO's. Every sponge is an aquatic invertebrate metazoan, including the freshwater Spongillida, so the genus covers the concept exactly with nothing left over. It is a direct child of `ENVO:01001002` *animal-associated environment* and currently has **no children in ENVO**, so a sponge-associated term would be the first — which is a point in favour, not against.

**Modelling precedent inside ENVO.** `ENVO:01001179` *cnidarian-associated environment* ("An environmental system determined by a cnidarian or part of a cnidarian") already exists as a sibling. ENVO has therefore already accepted the pattern "an `<invertebrate clade>`-associated environment" for exactly one clade; *sponge-associated environment* / *poriferan-associated environment* is the same pattern applied to Porifera. This is the strongest single argument that the term request is well-formed rather than novel modelling.

**Near-misses checked and why each fails** (OLS4 searches over ENVO, UBERON, FOODON, BTO, PO, and additionally PORO):

| Term | Why it is not a match |
|---|---|
| `ENVO:01001002` *animal-associated environment* | **Broader**, not wrong. Usable as a parent, but skips the aquatic-invertebrate level that already exists. |
| `ENVO:01001176` *environment associated with an aquatic invertebrate* | **Broader** — covers molluscs, cnidarians, annelids, echinoderms, sponges. Correct genus, not an identity. |
| `ENVO:01001161` *marine sponge reef* | **Different entity**: a reef built by Hexactinosa in "glacier-scoured troughs of low-angle continental shelf". Asserts geomorphology and geography the BacDive category never claims. Also excludes freshwater and non-reef-building sponges — i.e. nearly all of them. |
| `ENVO:01000123` *marine sponge reef biome* | Same problem, one level of granularity worse (biome). |
| `ENVO:01001055` *environment associated with an animal part or small animal* | Would apply to a sponge *part* (mesohyl, tissue), not to the sponge-as-host concept the BacDive category names. |
| `ENVO:01001179` *cnidarian-associated environment* | Wrong clade. Recorded here because "reef invertebrate" conflation is a real risk. |
| `NCBITaxon:6040` *Porifera* | A **taxon**, i.e. a class of organisms, not a place. This is the upstream mapping (see §4) and belongs in `relation: xref` per #99. |
| `PORO:0000001` *sponge* | An **organism** term ("All are sessile aquatic animals and, although there are freshwater species, the great majority are marine"). Whole-organism → xref, per the CLAUDE.md parts-vs-whole rule. Also PORO is not in HabitatMech's grounding ontology set. |
| `PORO:0000002` *mesohyl* | **Narrower** — one anatomical compartment of the host, and a legitimate grounding target for a future *sponge mesohyl* record, but not for the host-level concept. |
| BTO | No sponge/Porifera term. OLS returns only "spongy/spongiose" false positives (`BTO_0001700` cancellous bone, `BTO_0000053` albedo, etc.). |
| UBERON | No Porifera anatomy. `UBERON:0001337` *spongiose part of urethra* is a lexical false positive. |
| FOODON | `FOODON:00005683` *aquatic invertebrate material* is food-material framing, not a habitat. |

**Conclusion: nothing in ENVO/UBERON/FOODON/BTO/PO names this concept. UNGROUNDED is correct, and a term request is warranted.**

---

## 3. Differentia — what distinguishes it from siblings

Ordered by how observable each property is.

**a) Host identity and body plan (the primary differentia).** Determined by a member of Porifera: a sessile aquatic metazoan whose body is a pinacoderm-bounded mesohyl traversed by an aquiferous canal system (ostia → choanocyte chambers → osculum) ([PORO:0000001](https://www.ebi.ac.uk/ols4/ontologies/poro/classes?obo_id=PORO:0000001); [Hentschel et al. 2012](https://www.nature.com/articles/nrmicro2839)). Microorganisms in the mesohyl are physically separated from ambient water by the pinacoderm — a real, microscopically observable boundary, which is what makes the sponge interior a *distinct* environment rather than a parcel of seawater.

**b) Symbiont load, two orders of magnitude apart (HMA/LMA).** The single most useful measurable property. High-microbial-abundance sponges carry ~10⁸–10¹⁰ microbial cells per gram of tissue; low-microbial-abundance sponges ~10⁵–10⁶ cells g⁻¹, i.e. within seawater range ([Hentschel, Usher & Taylor 2006, doi:10.1111/j.1574-6941.2005.00046.x](https://academic.oup.com/femsec/article/55/2/167/595128); dichotomy first described by [Vacelet & Donadey 1977, *J Exp Mar Biol Ecol* 30:301–314](https://doi.org/10.1016/0022-0981(77)90038-7)). In HMA sponges microbes can reach ~35–40% of host biomass ([Hentschel et al. 2012](https://www.nature.com/articles/nrmicro2839)); microscopy across four coexisting Mediterranean sponges puts symbionts at 40–50% of biomass in some species ([*Commun Biol* 2024, doi:10.1038/s42003-024-06109-5](https://www.nature.com/articles/s42003-024-06109-5)).

**c) Steep, host-behaviour-driven redox gradients.** Sponges intermittently cease pumping for hours; when they do, diffusion becomes the only oxygen supply and the tissue interior goes anoxic. Microsensor work on *Geodia barretti* found anoxia in weakly-pumping and non-pumping individuals, with active sulfate reduction in the mesohyl; nitrification (566 nmol N cm⁻³ d⁻¹), denitrification and anammox co-occur in the same animal ([Hoffmann et al. 2009, *Environ Microbiol* 11:2228–2243, PMID 19453700](https://pubmed.ncbi.nlm.nih.gov/19453700/); [Schläppy et al. 2010, *Mar Biol*, doi:10.1007/s00227-008-0905-3](https://link.springer.com/article/10.1007/s00227-008-0905-3)). A single sponge is therefore an oxic *and* anoxic habitat on a sub-millimetre scale — a differentia against most other aquatic-invertebrate-associated environments.

**d) Host-specific, water-distinct community assembly with vertical transmission.** The global Porifera microbiome survey (81 host species) found sponges to be a reservoir of exceptional microbial diversity, with communities structured by specialists and generalists rather than opportunists, and host phylogeny affecting complexity more than composition — supporting independent assembly and convergent organisation across the phylum ([Thomas et al. 2016, *Nat Commun* 7:11870, doi:10.1038/ncomms11870](https://www.nature.com/articles/ncomms11870)). Symbionts are transmitted vertically through oocytes, embryos and larvae as well as acquired horizontally ([Hentschel et al. 2012](https://www.nature.com/articles/nrmicro2839); [Björk et al./Carrier et al. review, *Front Ecol Evol* 2022, doi:10.3389/fevo.2022.1015592](https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.1015592/full)).

**e) Ecosystem role — the sponge loop.** Sponges take up dissolved organic matter and return it as cellular detritus consumed by reef fauna, at rates approaching whole-reef gross primary production ([de Goeij et al. 2013, *Science* 342:108–110, doi:10.1126/science.1241981](https://www.science.org/doi/10.1126/science.1241981)). Useful ecological context; **too process-y to belong in the definiens.**

### Two constraints the definition must respect

1. **Do not say "marine."** Porifera includes ~250 freshwater species (order Spongillida, derived from marine ancestors ~32 Mya), whose microbiomes are distinct from ambient water and from marine sponge microbiomes ([Costa et al. 2019, *Front Microbiol* 10:2799, doi:10.3389/fmicb.2019.02799](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2019.02799/full); [Kenny et al. 2022, *ISME J*, *Ephydatia muelleri*, doi:10.1038/s41396-022-01296-7](https://www.nature.com/articles/s41396-022-01296-7); [Gaikwad et al. 2023, *Microorganisms* 12:25, doi:10.3390/microorganisms12010025](https://doi.org/10.3390/microorganisms12010025); [southeastern-US freshwater sponges, 2025, PMC11787800](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11787800/)). The BacDive category is host-taxon-based and does not exclude them.
2. **Do not make the aquiferous system criterial without hedging.** Carnivorous sponges (Cladorhizidae, ~150 spp.) have lost the aquiferous system and choanocytes — the phylum's own diagnostic characters ([Vacelet & Boury-Esnault 1995, *Nature* 373:333–335, doi:10.1038/373333a0](https://www.nature.com/articles/373333a0)), and they do host microbiomes, including methane-oxidising symbionts ([Vacelet et al. 1996, *MEPS* 145:77–85](https://www.int-res.com/abstracts/meps/v145/p77-85/); [Dupont et al. 2013, *FEMS Microbiol Ecol* 86:520–531](https://academic.oup.com/femsec/article/86/3/520/637859)). The mesohyl, by contrast, is retained. The proposed sentence above lists the canal system as part of the host body rather than as a necessary condition; if the curator wants strictness, drop "water canal system" and keep "pinacoderm surface and mesohyl matrix."

---

## 4. Evidence that this record's 86 strains really are sponge-derived

Marked as **inference from the record**, not a claim any single source makes: 26 of the 25 ranked characteristic taxa carry sponge-derived epithets or genus names — `Lysobacter spongiicola`, `Streptomyces spongiicola`, `Maribacter spongiicola`, `Williamsia spongiae`, `Saccharopolyspora spongiae`, `Nocardia xestospongiae` (*Xestospongia*), `Planococcus plakortidis` (*Plakortis*), `Aquimarina amphilecti` and `Cobetia amphilecti` (*Amphilectus fucorum*), `Fulvitalea axinellae` (*Axinella*), `Maribacter vaceletii` (after sponge taxonomist Jean Vacelet). This is consistent with the well-documented pattern that cultivable sponge isolates are typically low-relative-abundance mesohyl members, while the numerically dominant symbionts remain uncultured ([Hentschel et al. 2012](https://www.nature.com/articles/nrmicro2839); [Steinert et al. 2021, "Bacteria cultivated from sponges and bacteria not yet cultivated from sponges", *Front Microbiol*, PMC8634882](https://pmc.ncbi.nlm.nih.gov/articles/PMC8634882/); [Selvin et al. 2022, *Appl Microbiol Biotechnol*, doi:10.1007/s00253-022-11791-8](https://link.springer.com/article/10.1007/s00253-022-11791-8)).

**Upstream corroboration of scale.** Independently of BacDive's 86 strains, GOLD carries `Host-associated > Porifera` (90 organisms), `> Sponge` (323), and `> Sponge > Tissue` (7) — from `data/raw/gold_ecosystem_paths.tsv`. Two vocabularies independently recognise the sponge-as-host category, and GOLD further subdivides it by body compartment, which is what one expects of a habitat rather than of a taxon label.

**On the upstream mapping.** `data/raw/isolation_source_groundings.tsv` maps this concept to `NCBITaxon:6040` *Porifera* via `skos:closeMatch`, `semapv:LexicalMatching`, confidence `medium`, method `ols4_auto`. That is a lexical match to a taxon, not a habitat grounding, and per #99 belongs in `relation: xref`. Note the record's `source_attestations.notes` currently reads "Upstream mapping targets a non-habitat ontology ()" with an empty parenthetical — a cosmetic seeder artefact worth a separate issue, unrelated to this definition.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- sponge-associated environment / poriferan-associated environment (the ENVO-pattern label to request)
- sponge-associated habitat; sponge host environment
- sponge microbiome habitat; sponge tissue (loose, common in strain metadata)
- marine sponge (**narrower** — excludes Spongillida; widely used as if it were the whole concept)
- sponge mesohyl (**narrower** — one compartment, `PORO:0000002`)
- HMA sponge / LMA sponge (**narrower** — two subtypes; would be children, not synonyms)
- BacDive `#Host > #Porifera (Sponges)`; GOLD `Host-associated > Porifera > Sponge`

**Commonly but wrongly treated as the same thing**
- **sponge holobiont** — the host *plus* its microbiota considered as one biological unit ([Pita et al. 2018, *Microbiome* 6:46, doi:10.1186/s40168-018-0428-1](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-018-0428-1)). A composite organism, not an environment. Do not use as a synonym; it names a different kind of entity.
- **`ENVO:01001161` marine sponge reef / `ENVO:01000123` marine sponge reef biome** — the reef, not the animal.
- **`NCBITaxon:6040` Porifera** — the taxon. Xref only.
- **`PORO:0000001` sponge** — the organism. Xref only.
- **surrounding seawater / reef water** — the very contrast the microbiology establishes.
- **coral or cnidarian-associated environment (`ENVO:01001179`)** — different clade, frequently lumped as "reef invertebrates."
- **surgical, cleaning or contraceptive sponges (`NCIT:C42856`, SNOMED "Sponge" concepts)** — manufactured objects; the highest-risk lexical false positive.
- **"sponge-specific" bacterial lineages as a proxy for the habitat** — Poribacteria were described as a sponge-specific candidate phylum ([Fieseler et al. 2004, *Appl Environ Microbiol* 70:3724–3732, doi:10.1128/AEM.70.6.3724-3732.2004](https://journals.asm.org/doi/10.1128/aem.70.6.3724-3732.2004)) but have since been recovered from free-living marine particles ([Podell et al. 2019, *ISME J*, doi:10.1038/s41396-018-0292-9](https://www.nature.com/articles/s41396-018-0292-9)). Do not define the habitat by a diagnostic taxon.

---

## 6. Should this be a term at all? — Yes

It is a habitat, not a taxon, a process, or a sampling artefact. Three independent lines support that:

1. **ENVO already models organisms-as-environments**, including one invertebrate clade specifically (`ENVO:01001179` cnidarian-associated environment) under the same genus this concept needs. The requested term is a sibling in an existing pattern, not new modelling.
2. **The physical boundary is real and observable.** The pinacoderm separates a mesohyl interior with 10⁸–10¹⁰ cells g⁻¹ and internal anoxia from ambient water at 10⁵–10⁶ cells mL⁻¹. That is a place with its own physicochemistry, which is exactly what a habitat term should denote.
3. **Two upstream vocabularies independently name it as a host category**, and one (GOLD) subdivides it by body compartment.

`NOT_APPLICABLE` would be wrong here for the reason the curation note states: it asserts the concept is not a habitat, a strictly stronger and false claim. `CONFIRM_UNGROUNDED` + term request is the right disposition.

### Curator recommendations

- **Genus / `parent_habitats`:** `ENVO:01001176` *environment associated with an aquatic invertebrate*, `relation: parent`. (`ENVO:01001002` if the curator prefers the coarser level already used on the GOLD `Sponge` sibling — but then the two records disagree on depth for one concept.)
- **`relation: xref`:** `NCBITaxon:6040` *Porifera* (the upstream lexical target); optionally `PORO:0000001` *sponge*.
- **Do not attach** `ENVO:01000161` or `ENVO:01000123` in any relation — a sponge sample is not from a sponge reef, and parenting there would publish a geomorphic and geographic over-claim of exactly the shape #99 documents.
- **Flag for the ENVO request:** requested label *sponge-associated environment*; parent `ENVO:01001176`; genus-differentia text as proposed above; supporting citations doi:10.1038/nrmicro2839, doi:10.1038/ncomms11870, doi:10.1111/j.1574-6941.2005.00046.x. ENVO requires definition citations in the NTR issue itself ([ENVO wiki, Creating good definitions](https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions)). **Per the standing rule, no term request is filed without a separate explicit go-ahead for this specific request.**
- **Possible duplicate, worth a separate look:** this concept is the same habitat as `habitatmech:GOLD.affd2445ea` (*Sponge*, 323 assertions) and `habitatmech:GOLD.64acf9132c` (*Porifera*, 90). Three records, three sources, one place. That is a merge decision (#116-style "two novel concepts are the same"), not a grounding decision, and it is out of scope for this report — but a term request should probably cover all three at once rather than being filed three times.
- **Do not sum** the 86 BacDive strains with the 323/90 GOLD organisms — different `assertion_unit`.

---

## Sources

- [Hentschel U, Piel J, Degnan SM, Taylor MW (2012) Genomic insights into the marine sponge microbiome. *Nat Rev Microbiol* 10:641–654. doi:10.1038/nrmicro2839](https://www.nature.com/articles/nrmicro2839)
- [Thomas T, Moitinho-Silva L, Lurgi M, et al. (2016) Diversity, structure and convergent evolution of the global sponge microbiome. *Nat Commun* 7:11870. doi:10.1038/ncomms11870](https://www.nature.com/articles/ncomms11870)
- [Hentschel U, Usher KM, Taylor MW (2006) Marine sponges as microbial fermenters. *FEMS Microbiol Ecol* 55:167–177. doi:10.1111/j.1574-6941.2005.00046.x](https://academic.oup.com/femsec/article/55/2/167/595128)
- [Hoffmann F, Radax R, Woebken D, et al. (2009) Complex nitrogen cycling in the sponge *Geodia barretti*. *Environ Microbiol* 11:2228–2243. PMID 19453700](https://pubmed.ncbi.nlm.nih.gov/19453700/)
- [Schläppy M-L, et al. (2008) Oxygen dynamics and transport in the Mediterranean sponge *Aplysina aerophoba*. *Mar Biol*. doi:10.1007/s00227-008-0905-3](https://link.springer.com/article/10.1007/s00227-008-0905-3)
- [de Goeij JM, van Oevelen D, Vermeij MJA, et al. (2013) Surviving in a marine desert: the sponge loop retains resources within coral reefs. *Science* 342:108–110. doi:10.1126/science.1241981](https://www.science.org/doi/10.1126/science.1241981)
- [Vacelet J, Boury-Esnault N (1995) Carnivorous sponges. *Nature* 373:333–335. doi:10.1038/373333a0](https://www.nature.com/articles/373333a0)
- [Vacelet J, Fiala-Médioni A, Fisher CR, Boury-Esnault N (1996) Symbiosis between methane-oxidizing bacteria and a deep-sea carnivorous cladorhizid sponge. *MEPS* 145:77–85](https://www.int-res.com/abstracts/meps/v145/p77-85/)
- [Dupont S, et al. (2013) First insights into the microbiome of a carnivorous sponge. *FEMS Microbiol Ecol* 86:520–531](https://academic.oup.com/femsec/article/86/3/520/637859)
- [Van Soest RWM, Boury-Esnault N, Vacelet J, et al. (2012) Global diversity of sponges (Porifera). *PLoS ONE* 7:e35105. doi:10.1371/journal.pone.0035105](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0035105)
- [Costa R, et al. (2019) Freshwater sponge *Tubella variabilis* presents richer microbiota than marine sponge species. *Front Microbiol* 10:2799. doi:10.3389/fmicb.2019.02799](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2019.02799/full)
- [Kenny NJ, et al. (2022) Microbiome of the freshwater sponge *Ephydatia muelleri* shares compositional and functional similarities with those of marine sponges. *ISME J*. doi:10.1038/s41396-022-01296-7](https://www.nature.com/articles/s41396-022-01296-7)
- [Gaikwad S, et al. (2023) Freshwater sponges as a neglected reservoir of bacterial biodiversity. *Microorganisms* 12:25. doi:10.3390/microorganisms12010025](https://doi.org/10.3390/microorganisms12010025)
- [Freshwater sponges in the southeastern U.S. harbor unique microbiomes (2025). PMC11787800](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11787800/)
- [Fieseler L, Horn M, Wagner M, Hentschel U (2004) Discovery of the novel candidate phylum "Poribacteria" in marine sponges. *Appl Environ Microbiol* 70:3724–3732. doi:10.1128/AEM.70.6.3724-3732.2004](https://journals.asm.org/doi/10.1128/aem.70.6.3724-3732.2004)
- [Podell S, et al. (2019) Pangenomic comparison of globally distributed Poribacteria associated with sponge hosts and marine particles. *ISME J*. doi:10.1038/s41396-018-0292-9](https://www.nature.com/articles/s41396-018-0292-9)
- [Pita L, Rix L, Slaby BM, Franke A, Hentschel U (2018) The sponge holobiont in a changing ocean. *Microbiome* 6:46. doi:10.1186/s40168-018-0428-1](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-018-0428-1)
- [Moitinho-Silva L, et al. (2017) The sponge microbiome project. *GigaScience* 6:gix077](https://academic.oup.com/gigascience/article/6/10/gix077/4082886)
- [Steinert G, et al. (2021) Bacteria cultivated from sponges and bacteria not yet cultivated from sponges — a review. *Front Microbiol*. PMC8634882](https://pmc.ncbi.nlm.nih.gov/articles/PMC8634882/)
- [Selvin J, et al. (2022) Factors affecting the isolation and diversity of marine sponge-associated bacteria. *Appl Microbiol Biotechnol*. doi:10.1007/s00253-022-11791-8](https://link.springer.com/article/10.1007/s00253-022-11791-8)
- [High microbiome and metabolome diversification in coexisting sponges (2024) *Commun Biol*. doi:10.1038/s42003-024-06109-5](https://www.nature.com/articles/s42003-024-06109-5)
- [Simple Porifera holobiont reveals complex interactions between host, archaeon, bacterium and phage (2024) *ISME J* 18:wrae197](https://academic.oup.com/ismej/article/18/1/wrae197/7815078)
- [Global patterns in symbiont selection and transmission strategies in sponges (2022) *Front Ecol Evol*. doi:10.3389/fevo.2022.1015592](https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.1015592/full)
- [Vogel S (1977) Current-induced flow through living sponges in nature. *PNAS* 74:2069–2071. doi:10.1073/pnas.74.5.2069](https://www.pnas.org/doi/10.1073/pnas.74.5.2069)
- [Reimer LC, et al. (2019) BacDive in 2019: bacterial phenotypic data for high-throughput biodiversity analysis. *Nucleic Acids Res*. PMC6323973](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/)
- [BacDive isolation source browser](https://bacdive.dsmz.de/isolation-sources)
- [ENVO:01001176 environment associated with an aquatic invertebrate (OLS4)](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176)
- [ENVO:01001179 cnidarian-associated environment (OLS4)](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179)
- [ENVO:01001002 animal-associated environment (OLS4)](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002)
- [ENVO:01000161 marine sponge reef (OLS4)](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01000161)
- [PORO:0000001 sponge / PORO:0000002 mesohyl (OLS4, Porifera Ontology)](https://www.ebi.ac.uk/ols4/ontologies/poro/classes?obo_id=PORO:0000002)
- [ENVO wiki — Creating good definitions](https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions)
- [Yilmaz P, et al. (2011) Minimum information about a marker gene sequence (MIMARKS) and minimum information about any (x) sequence (MIxS) specifications. *Nat Biotechnol* 29:415–420. doi:10.1038/nbt.1823](https://www.nature.com/articles/nbt.1823)

**Claims marked as inference, not sourced:** (a) that the 86 BacDive strains are sponge-derived, argued from species epithets in the record; (b) that this record duplicates the two GOLD sponge records; (c) the recommendation of `ENVO:01001176` over `ENVO:01001002` as genus — ENVO itself has not placed any sponge term. I did not find an existing ENVO GitHub issue requesting a sponge-associated environment term; absence of search hits is weaker evidence than a direct tracker check, so verify before filing.

## Citations

1. https://bacdive.dsmz.de/isolation-sources
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/
3. https://www.ebi.ac.uk/ols4/ontologies/poro/classes?obo_id=PORO:0000002
4. https://www.nature.com/articles/nrmicro2839
5. https://academic.oup.com/femsec/article/55/2/167/595128
6. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176
7. https://www.ebi.ac.uk/ols4/ontologies/poro/classes?obo_id=PORO:0000001
8. https://doi.org/10.1016/0022-0981(77
9. https://www.nature.com/articles/s42003-024-06109-5
10. https://pubmed.ncbi.nlm.nih.gov/19453700/
11. https://link.springer.com/article/10.1007/s00227-008-0905-3
12. https://www.nature.com/articles/ncomms11870
13. https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.1015592/full
14. https://www.science.org/doi/10.1126/science.1241981
15. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2019.02799/full
16. https://www.nature.com/articles/s41396-022-01296-7
17. https://doi.org/10.3390/microorganisms12010025
18. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11787800/
19. https://www.nature.com/articles/373333a0
20. https://www.int-res.com/abstracts/meps/v145/p77-85/
21. https://academic.oup.com/femsec/article/86/3/520/637859
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC8634882/
23. https://link.springer.com/article/10.1007/s00253-022-11791-8
24. https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-018-0428-1
25. https://journals.asm.org/doi/10.1128/aem.70.6.3724-3732.2004
26. https://www.nature.com/articles/s41396-018-0292-9
27. https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions
28. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0035105
29. https://academic.oup.com/gigascience/article/6/10/gix077/4082886
30. https://academic.oup.com/ismej/article/18/1/wrae197/7815078
31. https://www.pnas.org/doi/10.1073/pnas.74.5.2069
32. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179
33. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
34. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01000161
35. https://www.nature.com/articles/nbt.1823