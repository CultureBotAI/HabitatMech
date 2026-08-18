---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T20:07:15.943473'
end_time: '2026-08-17T20:20:02.409757'
duration_seconds: 766.47
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: 'Arthropoda: Chelicerates'
  habitat_identifier: habitatmech:GOLD.44a2cbbd60
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Arthropoda: Chelicerates'
  assertions: '169'
  parent_terms: ENVO:01001000
  xrefs: NCBITaxon:6656
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term NCBITaxon:6656 'Arthropoda' attached as a parent. Host-taxon reversal\
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
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.44a2cbbd60)"
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
  web_search_requests: 24
  num_turns: 42
  total_cost_usd: 5.258923999999999
  session_id: 3a38f021-7d17-4ac3-b114-9801c2124444
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 53
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Arthropoda: Chelicerates
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.44a2cbbd60
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Arthropoda: Chelicerates
- **Upstream assertion volume:** 169
- **Nearest broader term already on the record:** ENVO:01001000
- **Cross-references upstream suggested:** NCBITaxon:6656

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term NCBITaxon:6656 'Arthropoda' attached as a parent. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.44a2cbbd60)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Arthropoda: Chelicerates** as a microbial habitat, with citations.

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

# Definition research: *Arthropoda: Chelicerates* (`habitatmech:GOLD.44a2cbbd60`)

> **Proposed definition:** An animal-associated environment [ENVO:01001002] which is determined by a living chelicerate — a mite, tick, spider, scorpion, harvestman, horseshoe crab, sea spider or relative — comprising that animal's body surfaces and internal compartments as sites of microbial colonisation.

Suggested label for the term request: **chelicerate-associated environment** (sibling of the existing `ENVO:01001179` *cnidarian-associated environment*, and of the parallel requests already researched for `habitatmech:GOLD.2959225799` *Arthropoda: Crustaceans* and `habitatmech:GOLD.dba2a83b95* *Arthropoda: Insects*).

Two things belong in a term comment rather than in the definition sentence: (a) the enumeration of compartments (cuticle surface, midgut and its diverticula, salivary glands, ovaries, Malpighian tubules, haemolymph), and (b) the fact that the great majority of real attestations are whole-animal samples of blood-feeding Acari. Both are corroborating evidence that the class carves at a real joint (§3), not part of its differentia.

**One correction the curator should make while editing this record:** the xref is `NCBITaxon:6656` *Arthropoda*, which is the **phylum** — three of its four subphyla (Crustacea, Hexapoda, Myriapoda) are *other* GOLD nodes with their own records. The taxon that matches this concept is `NCBITaxon:6843` *Chelicerata*, and it is **not** in `data/raw/ontology_terms.tsv` (the vendored NCBITaxon slice holds 31 terms, of which the only relevant ones are `NCBITaxon:6656` *Arthropoda* and `NCBITaxon:6935` *Ixodida*). So either vendor `NCBITaxon:6843` (see #10) or keep `6656` with a note that it is deliberately broader than the concept; do not silently let the phylum stand as if it were the match.

---

## 1. What the concept denotes

**The concept is a host organism acting as an environment — not a taxon, and not a body part.** The thing a sample is taken from is a living chelicerate: the animal's external surfaces and its interior, sampled whole in nearly every attested case.

### Evidence from the source path itself

GOLD's ecosystem classification is a five-level hierarchy (`Ecosystem > Ecosystem Category > Ecosystem Type > Ecosystem Subtype > Specific Ecosystem`) whose top level splits into **Host-associated**, **Environmental** and **Engineered**, with the second level naming the host group ([Mukherjee et al. 2023, *Nucleic Acids Res.* 51:D957–D963, doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974); correction [*NAR* 52:3483, doi:10.1093/nar/gkae162](https://doi.org/10.1093/nar/gkae162)). `Arthropoda: Chelicerates` sits at that second level, so it is structurally the same kind of node as `Mammals`, `Fish`, `Birds`, `Plants` — a host group, expanded downward by compartment.

The branch in `data/raw/gold_ecosystem_paths.tsv` is unusually thin, and its shape settles what the concept denotes:

| Path | GOLD node ids | Assertions (ORGANISM) |
|---|---|---|
| `Host-associated > Arthropoda: Chelicerates` (the clade node itself) | 4 | **169** |
| `… > Whole body` | 3 | **244** |
| `… > Cell Line` | 3 | 0 |
| `… > Cell Line > ISE6` | 2 | 0 |

That is the whole branch: **413 assertions, 100% of them at whole-animal resolution.** There is no digestive-system, respiratory-system or reproductive-system sub-branch here, unlike the crustacean node (47 paths) or the insect node. GOLD's only offered sub-resolution is a *cell line* — `ISE6`, an embryo-derived *Ixodes scapularis* line established by Munderloh and colleagues in 1994 and used to isolate and propagate *Rickettsia*, *Ehrlichia*, *Borrelia*, *Anaplasma* and tick-borne flaviviruses ([Alberdi et al. 2021, *Pathogens* 10:70, PMC7828734](https://pmc.ncbi.nlm.nih.gov/articles/PMC7828734/)). It carries zero assertions.

**Inference (mine, not any source's):** the dominant real-world usage of this concept is *microorganism isolated from a whole chelicerate*, host clade being the only environmental fact recorded — and the presence of a tick cell line as the sole named compartment is a fingerprint of which chelicerates the data is actually about. It is consistent with, but does not by itself prove, tick dominance.

**GOLD is the only attestor.** I checked `data/raw/bacdive_isolation_sources.tsv`, `prego_habitats.tsv` and `madin_habitats.tsv` for tick / mite / spider / scorpion / arachnid / chelicerate strings: none match. So no second vocabulary constrains the reading.

### Boundary — what is inside

- Living chelicerates of any lineage and habitat: terrestrial Arachnida (mites, ticks, spiders, scorpions, harvestmen, pseudoscorpions, whip spiders, camel spiders, ricinuleids), marine Xiphosura (horseshoe crabs) and marine Pycnogonida (sea spiders).
- All compartments of the individual animal when no compartment is separately named: cuticular surface and setae, book lungs and book gills, foregut and sucking pharynx, midgut and its diverticula, Malpighian tubules, salivary glands, venom gland/telson, gonads and ovaries, haemolymph and haemocoel.
- All post-embryonic life stages (larva, nymph/protonymph–tritonymph, adult). Per this repo's rule, a life stage is the whole organism, so tick larvae and nymphs are organism-as-habitat concepts nested inside this one, not anatomical parts.

### Boundary — what is a neighbouring concept

- **The animal's built structures.** GOLD puts these on the *Environmental* side, not here: `Environmental > Terrestrial > Nest > Chelicerates nest` (13 assertions; `habitatmech:GOLD.00a390bd33`, parented to `ENVO:00005803` *animal habitation*) and its child `… > Spider web` (12). Webs carry their own culturable bacteria — 22 strains isolated from orb-weaver webs, including *Microbacterium* sp. and *Novosphingobium* sp., which measurably increase host silk extensibility ([Sci. Rep. 2024, doi:10.1038/s41598-024-61723-x](https://doi.org/10.1038/s41598-024-61723-x); [PMC11093983](https://pmc.ncbi.nlm.nih.gov/articles/PMC11093983/)) — so this is a real and separate habitat, not a duplicate of the animal.
- **Body parts with their own anatomy terms.** Ground those to the anatomy term, not here. The vendored slice already holds `BTO:0001871` *synganglion* (whose definition is written explicitly about ticks), `BTO:0005777` *midgut diverticulum* ("The midgut of arachnids and crustaceans …"), `BTO:0001906` *cephalothorax*, `BTO:0002772` *chela*, `BTO:0002067` *stinger*, `BTO:0001250` *silk gland*.
- **The tick cell line.** `ISE6` (`habitatmech:GOLD.164a527d31`) is an in-vitro culture of tick cells, not a living animal and not an environment; see §6.
- **The vertebrate the ectoparasite was feeding on.** A tick removed from a dog is a chelicerate-associated sample; the dog's skin is `Host-associated > Mammals`. Both are true of the same collection event, and the distinction is the difference between two records.
- **The pathogen's other host.** *Borrelia burgdorferi* in a mouse is not this concept even though the same organism in an *Ixodes* midgut is.
- **Insects, crustaceans, myriapods.** The three sibling GOLD nodes. Note that Hexapoda and Crustacea are *mandibulate* arthropods; chelicerates are the other major branch, and the split is deep, not a matter of degree (§3a).

### Ambiguity — three readings, and which one the data means

1. **The chelicerate host as an environment** — the individual animal as the place microbes live. *This is the reading the GOLD path supports*: the node sits under `Host-associated`, takes assertions directly, and expands into `Whole body`.
2. **The taxon Chelicerata** — a class of organisms. Not a place. This is the reading that must not become the term's identity; the taxon belongs in `relation: xref` (#99, #114).
3. **Chelicerate-derived material** — silk, venom, *Limulus* amoebocyte lysate, chitin. Reachable from the bare word "chelicerate" but excluded by the `Host-associated` prefix; these are material entities.

I record reading 1 as intended and readings 2–3 as excluded. That mapping is my inference from the path structure plus the GOLD schema paper, not a claim any source makes about this label.

---

## 2. Genus — the broader kind

**Genus: `ENVO:01001002` *animal-associated environment***, defined in ENVO as "An environmental system determined by an animal", with synonyms *Metazoan-associated environment* and *animal environment*, itself a child of `ENVO:01001000` *environmental system determined by an organism* ([ENVO via OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002); [Buttigieg et al. 2013, *J. Biomed. Semantics* 4:43, PMC3904460](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3904460/); [Buttigieg et al. 2016, *J. Biomed. Semantics* 7:57, PMC5035502](https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/)). Both `ENVO:01001000` and `ENVO:01001002` are in the vendored slice with those exact labels, so a parent assertion on either will pass the label check.

The record currently parents to `ENVO:01001000` only. **`ENVO:01001002` is the tighter honest parent** — every chelicerate is an animal — and it is what the crustacean and insect records use.

**There is no chelicerate-, arachnid-, tick-, mite-, spider- or arthropod-associated class anywhere in ENVO.** Queried against the OLS4 API on 2026-08-17: `ENVO:01001002` has exactly three asserted children — `ENVO:01001176`, `ENVO:01001179` and `ENVO:01001829` *human settlement* — and full-text searches of ENVO for `tick`, `arachnid`, `chelicerate`, `spider` and `mite` return nothing relevant (only string collisions such as `ENVO:03501309` *booth*).

### Near-misses and why each fails

| Candidate | Why it is not the identity |
|---|---|
| **`ENVO:01001055` *environment associated with an animal part or small animal*** | The strongest near-miss, and the one most likely to tempt a curator, because most chelicerates *are* small animals: adult *Ixodes* nymphs are ~1–2 mm and most Acari are under 1 mm. It fails on two counts: (a) it disjoins "part" with "small animal", so adopting it asserts a disjunction the source never makes; (b) it is false for the large members — *Limulus polyphemus* reaches ~60 cm including telson, and theraphosid spiders have leg spans over 25 cm. A class that must exclude horseshoe crabs is not this class. |
| **`ENVO:01001176` *environment associated with an aquatic invertebrate*** | Defined as "An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system" (typo is ENVO's). Fails in **both** directions: it excludes the overwhelmingly terrestrial Arachnida (~112,000 of ~114,000 chelicerate species, §3a), and it includes molluscs, cnidarians, echinoderms and annelids. It is also asserted under `ENVO:01001055`, so parenting to it inherits the "part or small animal" over-claim. It has no children. |
| **`ENVO:01001179` *cnidarian-associated environment*** | Not a match, but the **precedent to copy**: "An environmental system determined by a cnidarian or part of a cnidarian" — a clade-level host-associated environment asserted directly under `ENVO:01001002`. It establishes that ENVO admits clade-level host environments and fixes the definitional pattern. |
| **`NCBITaxon:6843` Chelicerata / `NCBITaxon:6656` Arthropoda / `NCBITaxon:6935` Ixodida** | Classes of organisms, not places. Correct disposition is `relation: xref`. `6843` is the right one and is not vendored; `6656` (currently on the record) is the phylum and is broader than the concept; `6935` *Ixodida* is vendored and is *narrower* — it would name only the ticks. |
| **`BTO:0001489` *whole body*** | Already used, correctly, as the `NARROW` grounding of the child record `Whole body` (`habitatmech:GOLD.d438ab5070`, 244 assertions). It says "the whole animal was the sample", not "the animal is a chelicerate" — it is orthogonal to this concept, not broader than it. |
| **`ENVO:00005803` *animal habitation*** | Used, correctly, for the `Chelicerates nest` record. A built structure, not the builder. |
| **`ENVO:01001829` *human settlement*** | The third child of the genus; listed only to record that the genus's asserted children were enumerated exhaustively. |

**Where a request would go.** ENVO's tracker already carries [issue #1029, "EnvO terms for host-associated samples"](https://github.com/EnvironmentOntology/envo/issues/1029), opened 20 October 2020 by the GitHub user `jagadishcs` — a GOLD/JGI author — asking for host-associated, animal-associated, human-associated and plant-associated biome terms on exactly the argument used here ("for the microbial community the biome is the host organism"). The issue is closed without a recorded resolution, and no chelicerate or arthropod class exists today. The related GSC work is the symbiont-associated MIxS extension, [MIxS-SA (Parasite Microbiome Project, PMC9723553)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9723553/), which formalises nesting a symbiont-associated package inside a host-associated one. ENVO's own [Using ENVO with MIxS](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS) guidance still routes host-associated `env_local_scale` to UBERON/PO anatomy terms rather than to any host-clade environment class — which is precisely the gap this term would fill. *(No submission has been made and none should be made without explicit per-request permission for that specific request.)*

---

## 3. Differentia — what distinguishes it

**The differentia is the host clade: the environment is determined by a chelicerate rather than by some other animal.** That is the only property that is necessary and sufficient, and it is what separates this class from `cnidarian-associated environment`, from a crustacean- or insect-associated class, and from `Host-associated > Mammals`. Everything below is corroborating — it shows the class is biologically non-arbitrary — but none of it holds of *every* chelicerate, so none of it belongs in the sentence.

### 3a. Host clade, scope and internal heterogeneity

Chelicerata numbered **113,894 described species** in the standard global tally, of which **112,201 are Arachnida**, dominated by **Acari (54,617 mite and tick species)** and **Araneae (43,579 spiders)** ([Zhang 2011, *Zootaxa* 3148:7–12](https://www.mapress.com/zootaxa/2011/f/zt03148p012.pdf); revised in the 2013 addenda to Arachnida 114,275 / Acari 55,214 / Araneae 44,863, [*Zootaxa* 3703](https://www.biotaxa.org/Zootaxa/article/view/zootaxa.3703.1.6)). Spider description continues fast — the [World Spider Catalog](https://wsc.nmbe.ch/) records **53,680 species in 139 families** as of January 2026. Ticks, the microbiologically best-studied subgroup, comprise **1,033 valid species** in four families (Argasidae 221, Ixodidae 800, Khimairidae 1, Nuttalliellidae 11, including 21 fossil species) in the current world list ([*Parasites & Vectors* 2026, doi:10.1186/s13071-026-07493-z](https://link.springer.com/article/10.1186/s13071-026-07493-z)); the preceding hard-tick reference gave 762 Ixodidae species ([Guglielmone, Nava & Robbins 2023, *Zootaxa* 5251(1):1–274](https://www.mapress.com/zt/article/view/zootaxa.5251.1.1)).

The class is **not habitat-homogeneous**: Xiphosura (4 extant species) and Pycnogonida (~1,400 species) are marine while Arachnida are overwhelmingly terrestrial. *This is what kills `ENVO:01001176` as an identity from the terrestrial side, exactly as terrestrial isopods killed it for crustaceans from the other side.* (The 4 / ~1,400 figures are standard reference numbers that I saw only in tertiary sources in this search; treat them as approximate unless checked against a primary catalogue.)

The class is also **phylogenetically contested internally**: multiple phylogenomic analyses place Xiphosura *within* a paraphyletic Arachnida as sister to Ricinulei ([Ballesteros & Sharma 2019, *Syst. Biol.* 68:896–917, doi:10.1093/sysbio/syz011](https://doi.org/10.1093/sysbio/syz011); [Ballesteros et al. 2022, *Mol. Biol. Evol.* 39:msac021](https://academic.oup.com/mbe/article/39/2/msac021/6522129)), while other analyses recover sea spiders and horseshoe crabs as successive sister groups to a monophyletic terrestrial Arachnida ([Lozano-Fernandez et al. 2019, *Nat. Commun.* 10:2295, doi:10.1038/s41467-019-10244-7](https://www.nature.com/articles/s41467-019-10244-7); review: [Sharma 2021, *Diversity* 13:568, doi:10.3390/d13110568](https://doi.org/10.3390/d13110568)). **Chelicerata itself is not in dispute** — only the arrangement inside it — so a definition keyed on "a chelicerate" is safe where one keyed on "an arachnid" would not be.

### 3b. Body plan — a genuinely different animal from the other GOLD arthropod nodes

Chelicerates are the only major arthropod clade **lacking antennae**; the body is divided into prosoma and opisthosoma, the first appendage pair is the chelicerae (the only appendages anterior to the mouth), and mandibles are absent ([Britannica, *Chelicerata*](https://www.britannica.com/animal/Chelicerata); [Shultz, "Chelicerata (Arachnids, Including Spiders, Mites and Scorpions)", *Encyclopedia of Life Sciences*](https://jwshultz.weebly.com/uploads/4/6/2/2/46222147/chelicerata_encyclopedia.pdf); [*Current Biology* primer, doi:10.1016/j.cub.2018.05.036](https://www.sciencedirect.com/science/article/pii/S0960982218306729)). Marine forms respire with book gills; air-breathing forms with book lungs and/or tracheae. This is a different set of colonisable surfaces from the mineralised cuticle and branchial chamber of crustaceans or the tracheal system of insects.

### 3c. Preoral/extraoral digestion and midgut diverticula — why the chelicerate "gut" is not an insect gut

The chelicerate foregut opens into a preoral chamber with a muscular pharyngeal sucking pump, admitting only liquefied or filtered food; the midgut extends into the opisthosoma and ramifies as extensive blind diverticula/ceca ([Shultz, eLS, as above]; Ricinulei: [*J. Morphol.*, doi:10.1002/jmor.10897](https://onlinelibrary.wiley.com/doi/abs/10.1002/jmor.10897) — labral and pedipalpal setae forming a sieve-like preoral filter, pre- and postcerebral sucking pumps, four blind midgut diverticula; Pycnogonida: [microCT atlas, PMC8973786](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8973786/) — diverticula branching into chelifores and all legs; Opiliones: [*Sci. Rep.* 2025, s41598-025-18180-x](https://www.nature.com/articles/s41598-025-18180-x.pdf)). Extraoral digestion is the norm for predatory arachnids, and is a general predatory-arthropod strategy used by ~80% of predaceous arthropod species ([*Curr. Opin. Insect Sci.*, doi:10.1016/j.cois.2020.06.001](https://www.sciencedirect.com/science/article/abs/pii/S2214574520300924)).

**Inference (mine):** a filtered, liquid-fed, diverticulate gut offers little of the particulate retention that makes many insect and crustacean hindguts fermentation chambers. It is consistent with — and I think the likeliest mechanistic explanation for — the endosymbiont-dominated, low-diversity communities in §3d, but I found no source that states this causal link, so it must not enter a definition or a note as though it were established.

### 3d. Endosymbiont dominance — the clearest quantitative signal that this class is real

Chelicerates are **statistically distinct from mandibulate arthropods in heritable-symbiont incidence.** The reference meta-analysis estimates ~52% of arthropod species infected with *Wolbachia*, 24% with *Rickettsia* and 13% with *Cardinium*, and attributes the lower *Rickettsia*/*Cardinium* figures specifically to reduced incidence in most hexapod orders; *Cardinium* reaches ~60% of spider and mite species ([Weinert, Araujo-Jnr, Ahmed & Welch 2015, *Proc. R. Soc. B* 282:20150249, doi:10.1098/rspb.2015.0249](https://royalsocietypublishing.org/doi/10.1098/rspb.2015.0249)). Later comparative work analyses Chelicerata and Mandibulata *separately for this reason* ([Charlesworth et al. 2019, *Biol. Lett.*, doi:10.1098/rsbl.2019.0273](https://royalsocietypublishing.org/doi/10.1098/rsbl.2019.0273)). Earlier estimates ran the same way (~31.6% of mite species *Cardinium*-positive vs 6.1% of Hemiptera and 10.4% of Hymenoptera; [review in *Syst. Appl. Acarol.* 21:978](https://www.biotaxa.org/saa/article/view/saa.21.7.11)), and *Cardinium* is essentially fixed in some synanthropic Astigmata populations ([Kopecky et al. 2013, *J. Invertebr. Pathol.*, doi:10.1016/j.jip.2012.11.008](https://www.sciencedirect.com/science/article/abs/pii/S0022201112002698)).

In spiders the dominance is extreme enough to define the community: >99% of ~4.5 M reads from the dwarf spider *Oedothorax gibbosus* fell to five endosymbiont species — *Wolbachia*, *Rickettsia*, *Cardinium*, *Rhabdochlamydia* and *Acinetobacter* ([Vanthournout & Hendrickx 2015, *PLoS ONE* 10:e0117297, doi:10.1371/journal.pone.0117297](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0117297)); across eight spider species, *Wolbachia* reached 83.9 ± 6.3% in *Pirata subpiraticus* and *Rickettsiella* 87.6 ± 5.6% in *Agelena labyrinthica* ([Zhang et al. 2018, PMC5980269](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5980269/)); in *Argiope bruennichi* a single ASV accounted for 84.6% of filtered reads ([*Microorganisms* 8:8, doi:10.3390/microorganisms8010008](https://doi.org/10.3390/microorganisms8010008)).

### 3e. Haematophagy-driven obligate nutritional symbiosis

Blood is protein-rich and B-vitamin-poor, and obligate blood-feeding chelicerates depend on maternally inherited symbionts to close the gap. *Coxiella*-like and *Francisella*-like endosymbiont genomes converge on complete biosynthetic pathways for **biotin (B7), riboflavin (B2) and folate (B9)** ([review: *Ticks Tick Borne Dis.* / PMC10577665](https://pmc.ncbi.nlm.nih.gov/articles/PMC10577665/); [dual endosymbiosis in *Hyalomma marginatum*, *eLife* 2022, doi:10.7554/eLife.72747](https://elifesciences.org/articles/72747)); symbiont-derived B vitamins and L-proline are required for *Rhipicephalus sanguineus* feeding and reproductive fitness ([*mSphere* 2023, doi:10.1128/msphere.00693-23](https://journals.asm.org/doi/10.1128/msphere.00693-23)). *Ixodes* is the standing exception — it rarely carries CLE/FLE and instead relies on *Rickettsia buchneri* and *Candidatus* Midichloria mitochondrii ([*Trends Microbiol.* 2024, "Nutritional symbiosis in ticks: singularities of the genus *Ixodes*"](https://www.sciencedirect.com/science/article/abs/pii/S1471492224001648)); *R. buchneri* encodes complete biotin and folate pathways, resides principally in the ovaries, and can constitute close to 100% of the microbiome of adult females ([*PLoS ONE* 2015, doi:10.1371/journal.pone.0144552](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0144552); [Al-Khafaji et al. 2019, *Ticks Tick Borne Dis.*](https://www.sciencedirect.com/science/article/abs/pii/S1877959X19302602); [*Front. Vet. Sci.* 8:748427, PMC8770908](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8770908/)). The same pattern recurs in non-tick Acari: a *Rickettsiella* endosymbiont is a candidate B-vitamin source for the poultry red mite *Dermanyssus gallinae* ([PMC8446615](https://pmc.ncbi.nlm.nih.gov/articles/PMC8446615/)), and a novel **arachnid-specific Bartonella-like symbiont lineage spanning mites and scorpions** supplies pantothenate and lipoic acid to *Tyrophagus putrescentiae* ([*mSystems* 2023, doi:10.1128/msystems.00829-23](https://journals.asm.org/doi/10.1128/msystems.00829-23)).

### 3f. Compartments that are habitats in their own right

- **Midgut → haemolymph → salivary gland transit.** In unfed *Ixodes*, *Borrelia burgdorferi* is confined to the midgut expressing OspA; on feeding it downregulates OspA, upregulates OspC, crosses the midgut epithelium and reaches the salivary glands, with infection-competent spirochaetes not regularly arriving until ~60–72 h post-attachment ([*FEMS Microbiol. Rev.* 27:493](https://academic.oup.com/femsre/article/27/4/493/593332); [*J. Exp. Med.* 199:603](https://rupress.org/jem/article/199/5/603/40056/Borrelia-Outer-Membrane-Surface-Proteins-and)). Distinct compartments of one small animal function as distinct, sequentially occupied habitats.
- **Ovaries and Gené's-organ-mediated vertical transmission** as the route by which the symbiont community is inherited rather than acquired ([PMC10577665](https://pmc.ncbi.nlm.nih.gov/articles/PMC10577665/)).
- **Tissue-resolved surveys** show saliva and haemolymph harbouring more extracellular bacteria than salivary gland and midgut tissue in camel ticks ([*Sci. Rep.* 2024, doi:10.1038/s41598-024-81313-1](https://www.nature.com/articles/s41598-024-81313-1)).
- **Venom apparatus.** Scorpion telsons of *Hadrurus arizonensis* and *Smeringurus mesaensis* carry species-specific microbiota including Mollicutes ([*PLoS ONE* 2022, doi:10.1371/journal.pone.0277303](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0277303)) — a compartment with no counterpart in the crustacean or insect classes.
- **Body surface and haemolymph of horseshoe crabs.** Four body sites on wild *Limulus polyphemus* carried highly similar communities dominated by unclassified Gammaproteobacteria, Chitinophagales, Rhodobacteraceae, Saprospiraceae, Flavobacteriaceae, plus *Vibrio*, *Tenacibaculum*, *Thiothrix* and *Rubritalea*, with *Vibrio* and *Pseudoalteromonas* proposed as a core signature shared with Asian species ([*Front. Microbiol.* 11:1398, PMC7381184](https://pmc.ncbi.nlm.nih.gov/articles/PMC7381184/)). *Limulus* haemolymph — the source of LAL — is not sterile ([*Appl. Environ. Microbiol.* 49:718–720 (1985), doi:10.1128/aem.49.3.718-720.1985](https://journals.asm.org/doi/10.1128/aem.49.3.718-720.1985); method update: [*AEM* 2018, doi:10.1128/aem.02824-17](https://journals.asm.org/doi/10.1128/aem.02824-17)).

### 3g. What is *not* a discriminator

Moult-driven turnover of surface communities, maternal transmission through the egg, and reproductive manipulation by *Wolbachia* all occur across arthropods generally. They characterise this class; they do not distinguish it. Do not write them into the differentia.

---

## 4. Sources

Every substantive claim above carries an inline citation. Consolidated, the load-bearing ones are:

- **Source vocabulary structure:** Mukherjee et al. 2023, *NAR* 51:D957–D963, [doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974); correction [doi:10.1093/nar/gkae162](https://doi.org/10.1093/nar/gkae162).
- **Genus term:** ENVO `ENVO:01001002` via [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002), enumerated 2026-08-17; Buttigieg et al. [2013, PMC3904460](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3904460/) and [2016, PMC5035502](https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/).
- **Standards context:** [GSC MIxS](https://genomicsstandardsconsortium.github.io/mixs/); [MIxS-SA, PMC9723553](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9723553/); [ENVO wiki, Using ENVO with MIxS](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS); [ENVO issue #1029](https://github.com/EnvironmentOntology/envo/issues/1029).
- **Clade scope:** [Zhang 2011, *Zootaxa* 3148](https://www.mapress.com/zootaxa/2011/f/zt03148p012.pdf); [Zootaxa 3703 addenda](https://www.biotaxa.org/Zootaxa/article/view/zootaxa.3703.1.6); [World Spider Catalog](https://wsc.nmbe.ch/); [Guglielmone et al. 2023, *Zootaxa* 5251](https://www.mapress.com/zt/article/view/zootaxa.5251.1.1); [world tick list 2026, doi:10.1186/s13071-026-07493-z](https://link.springer.com/article/10.1186/s13071-026-07493-z).
- **Phylogeny:** [Ballesteros & Sharma 2019, doi:10.1093/sysbio/syz011](https://doi.org/10.1093/sysbio/syz011); [Ballesteros et al. 2022, MBE 39:msac021](https://academic.oup.com/mbe/article/39/2/msac021/6522129); [Lozano-Fernandez et al. 2019, doi:10.1038/s41467-019-10244-7](https://www.nature.com/articles/s41467-019-10244-7); [Sharma 2021, doi:10.3390/d13110568](https://doi.org/10.3390/d13110568).
- **Symbiont incidence:** [Weinert et al. 2015, doi:10.1098/rspb.2015.0249](https://royalsocietypublishing.org/doi/10.1098/rspb.2015.0249).
- **Chelicerate microbiomes:** spiders [doi:10.1371/journal.pone.0117297](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0117297), [PMC5980269](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5980269/), [doi:10.3390/microorganisms8010008](https://doi.org/10.3390/microorganisms8010008); ticks [PMC10577665](https://pmc.ncbi.nlm.nih.gov/articles/PMC10577665/), [doi:10.7554/eLife.72747](https://elifesciences.org/articles/72747), [doi:10.1128/msphere.00693-23](https://journals.asm.org/doi/10.1128/msphere.00693-23), [*Trends Microbiol.* 2024](https://www.sciencedirect.com/science/article/abs/pii/S1471492224001648), [*Microorganisms* 12:2451](https://www.mdpi.com/2076-2607/12/12/2451); mites [doi:10.1128/msystems.00829-23](https://journals.asm.org/doi/10.1128/msystems.00829-23), [PMC8446615](https://pmc.ncbi.nlm.nih.gov/articles/PMC8446615/); scorpions [doi:10.1371/journal.pone.0277303](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0277303); horseshoe crabs [PMC7381184](https://pmc.ncbi.nlm.nih.gov/articles/PMC7381184/), [doi:10.1128/aem.49.3.718-720.1985](https://journals.asm.org/doi/10.1128/aem.49.3.718-720.1985); webs [doi:10.1038/s41598-024-61723-x](https://doi.org/10.1038/s41598-024-61723-x).
- **Cell line:** [Alberdi et al. 2021, *Pathogens* 10:70, PMC7828734](https://pmc.ncbi.nlm.nih.gov/articles/PMC7828734/) (ISE6 established by Munderloh et al. 1994).

**Explicitly my inference, not any source's:** (a) that the GOLD path's `Host-associated` prefix plus its `Whole body` and `Cell Line` children fix reading 1 over readings 2–3; (b) that the ISE6 branch is a fingerprint of tick dominance in this node's real content; (c) that preoral/extraoral digestion plausibly explains the endosymbiont-dominated, low-diversity communities. None of these should be asserted in the definition or in a `notes` field as though sourced.

**Not found, and worth saying so:** no chelicerate-wide microbiome review exists. The literature is tick-heavy, spider-moderate, mite-moderate, and essentially absent for Opiliones, Solifugae, Amblypygi and Pycnogonida. Any claim about "the chelicerate microbiome" as a whole is currently an extrapolation from Acari and Araneae.

---

## 5. Synonyms and what NOT to conflate

**Names in real use for this concept**

- *Arthropoda: Chelicerates* (GOLD's own label — keep as the record label)
- chelicerate-associated environment / chelicerate host environment
- chelicerate holobiont *(usage note: "holobiont" names the host-plus-microbiota system, not the environment; near-synonymous in practice, not in ontology semantics)*
- Chelicerata (as a host qualifier, e.g. "host: Chelicerata")

**Narrower terms often used as if they were this concept**

- *arachnid-associated* — excludes Xiphosura and Pycnogonida, and Arachnida's monophyly is itself contested (§3a). Not a synonym.
- *tick microbiome*, *mite microbiome*, *spider microbiome*, *acarine host* — each names one subgroup. Ticks alone are ~1,033 of ~114,000 chelicerate species, yet they carry most of the literature; using "tick" as the class label would bake a sampling bias into an ontology term.

**Commonly but wrongly treated as the same thing**

| Not this concept | What it actually is |
|---|---|
| `NCBITaxon:6843` Chelicerata / `NCBITaxon:6656` Arthropoda | Taxa — classes of organisms, not places. `relation: xref` (#99). |
| Spider web, chelicerate nest | Built structures with their own microbiota; GOLD files them under `Environmental > Terrestrial > Nest`, parented to `ENVO:00005803` *animal habitation*. |
| ISE6 and other tick cell lines | In-vitro cultures of tick cells (§6). |
| The vertebrate host an ectoparasite fed on | `Host-associated > Mammals` / `> Birds` / `> Reptilia`. |
| Tick-borne disease in a human or animal patient | A disease state; `NOT_APPLICABLE` territory. |
| Spider silk, scorpion venom, LAL reagent, chitin | Material entities derived from the animal, not the animal as environment. Note that "antibiotic spider silk" is contested: seven species across the spider phylogeny showed no antimicrobial activity, and live bacteria were imaged on silk surfaces ([*iScience* 2021, "The myth of antibiotic spider silk"](https://www.sciencedirect.com/science/article/pii/S2589004221010932)). |
| Insects | A *mandibulate* arthropod lineage; the separation from Chelicerata is one of the deepest splits in the phylum, and unlike the insect-inside-Crustacea complication of the sibling record, there is no phylogenetic overlap to caveat here. |

---

## 6. Whether it should be a term at all

**Yes — this is a habitat, and it should be a term.** The concept is a living animal acting as the place microbes live, which is exactly what `ENVO:01001002` models and what `ENVO:01001179` instantiates at clade level. The host-taxon reversal recorded on this record (#114) is right, and the corroborating evidence here is unusually strong: multiple chelicerate lineages carry obligate, host-fitness-determining symbioses (§3e), and heritable-symbiont incidence differs *statistically between Chelicerata and Mandibulata* (§3d), so "chelicerate" is not an arbitrary slice of "animal".

Three qualifications the curator should carry into the note:

1. **The class is heterogeneous and the evidence is not evenly distributed.** Ticks and spiders supply nearly all of the microbiology; Pycnogonida, Opiliones, Solifugae and Amblypygi supply almost none. The definition survives this because it is keyed on the host clade, not on any microbial property — but a note that claims a shared community structure across Chelicerata would be an over-claim.
2. **`ISE6` (`habitatmech:GOLD.164a527d31`) deserves a different disposition from its parent, and this research does not settle it.** A continuously passaged embryo-derived cell line is a laboratory culture system, not a living animal and not an environment; it carries 0 assertions; and it is used precisely as a *substitute* for the animal when culturing obligate intracellular tick-borne bacteria ([PMC7828734](https://pmc.ncbi.nlm.nih.gov/articles/PMC7828734/)). Whether that is `NOT_APPLICABLE`, an engineered-environment concept, or a legitimate narrow habitat is a separate decision on a separate record; flagging it here so the whole branch is not swept in on this record's reasoning.
3. **Fix the xref while editing.** `NCBITaxon:6656` *Arthropoda* is the phylum and is shared with three sibling records that are not this concept. `NCBITaxon:6843` *Chelicerata* is the right target and is absent from the vendored slice — so this needs either a vendoring pass (#10) or an explicit note that the coarser taxon is being kept deliberately. Do not assert `NCBITaxon:6843` before it is vendored; the label check will fail, and that check is the thing standing between this pass and a plausible-looking wrong CURIE in the corpus.

## Citations

1. https://doi.org/10.1093/nar/gkac974
2. https://doi.org/10.1093/nar/gkae162
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC7828734/
4. https://doi.org/10.1038/s41598-024-61723-x
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC11093983/
6. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
7. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3904460/
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/
9. https://github.com/EnvironmentOntology/envo/issues/1029
10. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9723553/
11. https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
12. https://www.mapress.com/zootaxa/2011/f/zt03148p012.pdf
13. https://www.biotaxa.org/Zootaxa/article/view/zootaxa.3703.1.6
14. https://wsc.nmbe.ch/
15. https://link.springer.com/article/10.1186/s13071-026-07493-z
16. https://www.mapress.com/zt/article/view/zootaxa.5251.1.1
17. https://doi.org/10.1093/sysbio/syz011
18. https://academic.oup.com/mbe/article/39/2/msac021/6522129
19. https://www.nature.com/articles/s41467-019-10244-7
20. https://doi.org/10.3390/d13110568
21. https://www.britannica.com/animal/Chelicerata
22. https://jwshultz.weebly.com/uploads/4/6/2/2/46222147/chelicerata_encyclopedia.pdf
23. https://www.sciencedirect.com/science/article/pii/S0960982218306729
24. https://onlinelibrary.wiley.com/doi/abs/10.1002/jmor.10897
25. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8973786/
26. https://www.nature.com/articles/s41598-025-18180-x.pdf
27. https://www.sciencedirect.com/science/article/abs/pii/S2214574520300924
28. https://royalsocietypublishing.org/doi/10.1098/rspb.2015.0249
29. https://royalsocietypublishing.org/doi/10.1098/rsbl.2019.0273
30. https://www.biotaxa.org/saa/article/view/saa.21.7.11
31. https://www.sciencedirect.com/science/article/abs/pii/S0022201112002698
32. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0117297
33. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5980269/
34. https://doi.org/10.3390/microorganisms8010008
35. https://pmc.ncbi.nlm.nih.gov/articles/PMC10577665/
36. https://elifesciences.org/articles/72747
37. https://journals.asm.org/doi/10.1128/msphere.00693-23
38. https://www.sciencedirect.com/science/article/abs/pii/S1471492224001648
39. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0144552
40. https://www.sciencedirect.com/science/article/abs/pii/S1877959X19302602
41. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8770908/
42. https://pmc.ncbi.nlm.nih.gov/articles/PMC8446615/
43. https://journals.asm.org/doi/10.1128/msystems.00829-23
44. https://academic.oup.com/femsre/article/27/4/493/593332
45. https://rupress.org/jem/article/199/5/603/40056/Borrelia-Outer-Membrane-Surface-Proteins-and
46. https://www.nature.com/articles/s41598-024-81313-1
47. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0277303
48. https://pmc.ncbi.nlm.nih.gov/articles/PMC7381184/
49. https://journals.asm.org/doi/10.1128/aem.49.3.718-720.1985
50. https://journals.asm.org/doi/10.1128/aem.02824-17
51. https://genomicsstandardsconsortium.github.io/mixs/
52. https://www.mdpi.com/2076-2607/12/12/2451
53. https://www.sciencedirect.com/science/article/pii/S2589004221010932