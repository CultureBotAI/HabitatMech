---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:50:03.349726'
end_time: '2026-08-17T16:57:56.385988'
duration_seconds: 473.04
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Mammals
  habitat_identifier: habitatmech:GOLD.e889967f4f
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Mammals'
  assertions: '6104'
  parent_terms: ENVO:01001000, ENVO:01001002
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Nearest
    broader term ENVO:01001002 ''animal-associated environment'' attached as a parent.
    Mammals as host. Parented to animal-associated environment; not grounded there
    because every host clade would merge onto one record. ENVO term request. (source
    concept habitatmech:GOLD.e889967f4f)'
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
  web_search_requests: 16
  num_turns: 32
  total_cost_usd: 3.478787499999999
  session_id: 57257e8c-035f-453c-bff9-9aeb62364ef8
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 23
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Mammals
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.e889967f4f
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Mammals
- **Upstream assertion volume:** 6104
- **Nearest broader term already on the record:** ENVO:01001000, ENVO:01001002
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:01001002 'animal-associated environment' attached as a parent. Mammals as host. Parented to animal-associated environment; not grounded there because every host clade would merge onto one record. ENVO term request. (source concept habitatmech:GOLD.e889967f4f)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Mammals** as a microbial habitat, with citations.

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

I'll research this concept now.

# Mammals as a microbial habitat — definition research

**Target:** `habitatmech:GOLD.e889967f4f` — "Mammals" (HOST_ASSOCIATED, UNGROUNDED, 6,104 GOLD organism assertions)
**Researched:** 2026-08-17

---

## Proposed definition

> An animal-associated environment which is determined by an organism that is a member of Mammalia.

Recommended supporting axioms and metadata (not part of the definition sentence):

- genus / `parent_habitats`: `ENVO:01001002` *animal-associated environment*
- `xrefs`: `NCBITaxon:40674` *Mammalia* (the determining organism, **not** the identity of the habitat)
- narrower concept already in the corpus: `habitatmech:GOLD.cd0b0940e5` *Mammals: Human*
- usage comment: *In GOLD, human hosts are routed to the sibling ecosystem category `Mammals: Human`, so records attested only by `Host-associated > Mammals` are in practice non-human mammals.*

I deliberately did **not** write "non-human mammal" into the definition. See §1.2 for the argument and the counter-argument, since this is the one judgement call a curator has to make before writing the sentence.

---

## 1. What the concept denotes

### 1.1 The habitat

The concept denotes **the environmental system constituted by an individual mammal acting as host** — the body surfaces, cavities, tracts, tissues, fluids and secretions of a living (or freshly dead) mammal, considered as the place in which a microbial community lives. The thing a sample is taken from is a body site of a mammal: rumen contents, faeces, milk, skin swab, nasopharyngeal swab, blood, lung tissue.

This reading is forced by the source. In GOLD's five-level classification (Ecosystem → Ecosystem Category → Ecosystem Type → Ecosystem Subtype → Specific Ecosystem), "Mammals" occupies the **Ecosystem Category** slot directly under Ecosystem = `Host-associated` ([GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification); [Mukherjee et al. 2025, *NAR* 53:D989–D997, doi:10.1093/nar/gkae1000](https://doi.org/10.1093/nar/gkae1000)). Everything below it in the path is host anatomy. In this repo's copy of the GOLD path inventory (`data/raw/gold_ecosystem_paths.tsv`), 258 distinct paths sit under `Host-associated > Mammals`, and the ecosystem-type level is populated exclusively by mammalian organ systems — Digestive, Respiratory, Integumentary, Circulatory, Lymphatic, Urinary, Reproductive, Nervous, Auditory/Hearing, Abdominal cavity, Connective tissue.

The largest leaves under `Host-associated > Mammals`, by GOLD organism count, are diagnostic of what the category is actually used for:

| GOLD path | organisms |
|---|---|
| `… > Digestive system > Foregut > Rumen` | 4,989 |
| `… > Digestive system > Large intestine > Fecal` | 4,785 |
| `… > Integumentary system > Mammary gland > Milk` | 650 |
| `… > Digestive system > Stomach > Rumen` | 450 |
| `… > Respiratory system > Lung` | 326 |
| `… > Lymphatic system > Tonsils` | 324 |

The 6,104 assertions on this record are the ones recorded at the bare `Host-associated > Mammals` node — i.e. samples whose curator identified a mammalian host but recorded no organ system.

### 1.2 Ambiguity: does "Mammals" include humans?

**It is ambiguous, and the two readings give different definitions.**

- **Reading A (clade).** "Mammals" = Mammalia, humans included. This is what the label says and what any reader outside GOLD would assume.
- **Reading B (GOLD convention: non-human).** GOLD carries `Mammals: Human` as a *separate ecosystem category* at the same level (476 paths, 40,432 organisms at the bare node). A GOLD curator with a human sample uses that category, not this one. Under GOLD's own usage, `Host-associated > Mammals` therefore denotes non-human mammals.

Corroborating evidence for Reading B from the path inventory: leaves under `Mammals` that would be nonsensical for humans include `Digestive system > Large intestine > Cecotropes/Night fecs` (lagomorph/rodent coprophagy), `Integumentary system > Skin > Digital dermatitis` (a cattle foot disease, 52 organisms), and `Cell Line > BHK | CHO | Mouse myeloma | Rat myeloma` (all non-human lines).

**Recommendation: define under Reading A and record Reading B as a usage comment.** Reasons:

1. ENVO definitions avoid negative differentiae; "a mammal that is not a human" is a definition by exclusion and would make `human-associated environment` disjoint from `mammal-associated environment`, which is biologically false and blocks the useful inference that a human gut sample is a mammalian gut sample.
2. The corpus already has a distinct record for the human concept (`habitatmech:GOLD.cd0b0940e5`, "Mammals: Human", also UNGROUNDED, also carrying `ENVO:01001002` as parent, merged `SAME_AS` with BacDive's "Human" under #116). Under Reading A that record is simply *narrower*, which is the correct relation, and the GOLD partition becomes a data-entry convention rather than an ontological claim.
3. Attributing GOLD's routing convention to the *concept* would publish an assertion GOLD does not make. GOLD states only that the classification is "primarily driven by the samples curated in GOLD" and is not a comprehensive enumeration ([GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)).

*This is my recommendation, not something a source states.* The counter-argument is real: if a downstream user aggregates the 6,104 assertions as "mammals" they will be aggregating a non-human-biased sample, so the usage comment is not optional garnish.

### 1.3 The boundary

**Inside the concept:** any body site, cavity, tract, tissue, surface, secretion or fluid of a mammal, sampled in the host — gut and rumen contents, faeces, skin, oral cavity and dental plaque, respiratory tract, milk in the mammary gland, blood, urine, lymphoid tissue, reproductive tract.

**Outside, and neighbouring:**

| Neighbouring concept | Why it is not this |
|---|---|
| Anatomical parts (`UBERON:0002416` integumental system, `UBERON:0000178` blood, rumen, skin) | These are the *parts*, and the corpus grounds part-level habitats directly to them. This concept is the whole host as an environment. Per this repo's rule, parts ground; the whole organism keeps its own identity. |
| `NCBITaxon:40674` Mammalia | A class of organisms, not a place. Belongs in `relation: xref`. |
| `habitatmech:GOLD.cd0b0940e5` "Mammals: Human" | Narrower, not equivalent (§1.2). |
| Mammal-derived materials in a food or product chain — `FOODON:00005501` *mammal material*, `FOODON:00001217` *mammalian milk beverage*, `FOODON:00001006` *mammalian meat food product* | These assert derivation and a food-chain role. Bulk-tank milk or retail meat is a food matrix, not the host environment; milk sampled from the mammary gland is. |
| Mammalian cell lines (GOLD: `Mammals > Cell Line > BHK / CHO / Mouse myeloma / Rat myeloma`) | *In vitro* engineered culture systems. GOLD nests them here, but they are not a host organism. **All four carry 0 assertions in this inventory**, so they do not affect this record — flag only, no action needed. |
| Livestock housing, manure lagoons, barn surfaces | Built/anthropogenic environments determined by human construction, not by a mammal's body. |
| Dung deposited on soil, carcasses in decomposition | Genuinely a boundary. Once separated from the living host the determining system arguably becomes the soil/decomposition system. No source I found adjudicates this; flag it, do not resolve it in the definition. |
| `habitatmech:BACDIVE.15180e7ff9` "Aquatic-mammal" (69 BacDive strains) | A narrower sibling *within* this concept, not a competitor to it. |

---

## 2. Genus — the broader kind

### 2.1 Recommended genus

**`ENVO:01001002` *animal-associated environment*** — "An environmental system determined by an animal." Exact synonyms: *Metazoan-associated environment*, *animal environment*. It is a subclass of `ENVO:01001000` *environmental system determined by an organism* (verified via OLS4 hierarchical ancestors, 2026-08-17), which itself sits under `ENVO:01001254`… more precisely under `ENVO:01000254` *environmental system*.

This is the smallest well-established kind that fits. ENVO already models exactly this genus and already has clade-scoped children (§2.3), so the genus is not a stretch.

**Minor record observation:** the record currently lists both `ENVO:01001000` and `ENVO:01001002` as `parent_habitats`. Since 01001002 *is_a* 01001000, the first is redundant. That is a seeder behaviour, not an error in the decision, and I raise it only so it is a conscious choice.

### 2.2 Confirmation that nothing grounds this concept

Searched OLS4 for ENVO (2026-08-17): the complete set of `*-associated environment` classes in ENVO is

`ENVO:01001000` environmental system determined by an organism (synonym: **host-associated environment**) · `ENVO:01001001` plant-associated environment · `ENVO:01001002` animal-associated environment · `ENVO:01001041` fungi-associated environment · `ENVO:01001055` environment associated with an animal part or small animal · `ENVO:01001057` environment associated with a plant part or small plant · `ENVO:01001058` environment associated with a fungal tissue · `ENVO:01001176` environment associated with an aquatic invertebrate · `ENVO:01001179` cnidarian-associated environment

Enumerating descendants of `ENVO:01001002` returns only `ENVO:01001055`, `ENVO:01001176`, `ENVO:01001179`, and the human-settlement branch (`ENVO:01001829`, `ENVO:00000856` city, `ENVO:01000246` village biome, etc.). **There is no *mammal-associated environment* and no *vertebrate-associated environment* in ENVO.** Text search for "mammal" and "vertebrate" scoped to ENVO returns only bodily-fluid materials (`ENVO:02000025` sweat material, `ENVO:02000028` ear wax material) and non-ENVO hits (NCBITaxon, FOODON, UBERON). **The UNGROUNDED status is correct.**

### 2.3 Near-misses worth recording

| Candidate | Verdict |
|---|---|
| `ENVO:01001002` animal-associated environment | **Genus, not identity.** Grounding here would merge Mammals with Birds, Fish, Reptilia, Amphibia, Mollusca, Invertebrates, Arthropoda and the rest of GOLD's 27 host-associated categories onto one record — the reason the existing curation note gives, and it is correct. |
| `ENVO:01001000` environmental system determined by an organism | Too broad (plants and fungi). Note its exact synonym is literally *host-associated environment*, i.e. it is the genus of GOLD's whole `Host-associated` ecosystem level, not of its Mammals category. |
| `ENVO:01001055` environment associated with an animal part or small animal | **Near-miss, fails twice.** It covers *parts* of animals and *whole small* animals. This concept is the whole host, and a cow, whale or elephant is not a small animal. Adopting it would misdescribe the majority of the attestations. |
| `ENVO:01001176` environment associated with an aquatic invertebrate; `ENVO:01001179` cnidarian-associated environment | Wrong clades — but **valuable precedent**: ENVO does mint clade-scoped `X-associated environment` classes under the animal branch. A *mammal-associated environment* request is a pattern-conformant addition, not a novel modelling proposal. |
| `NCBITaxon:40674` Mammalia | An organism class. Per this repo's rule it goes in `relation: xref`; it is neither the identity nor a broader *place*. Grounding here would repeat the #114/#112 error class. |
| UBERON anatomy (`UBERON:0002416` integumental system, `UBERON:0000160` intestine, `UBERON:0000178` blood) | Parts. These are the correct grounding target for the *child* records (`Mammals > Digestive system > …`), not for the host-level concept. |
| `FOODON:00005501` mammal material | Asserts derivation and a material/food framing rather than an environmental system. Legitimate xref for milk/meat-derived isolates only. |
| EMPO "Animal" | Maps to `ENVO:01001002` in the `envoEmpo` subset; EMPO has no mammal level either. |
| ENVO issue [#1029](https://github.com/EnvironmentOntology/envo/issues/1029) (opened 2020-10-20, closed, labelled "question") | Requested host-associated *biome* terms (host-, animal-, human-, plant-associated biome). Closed without adding them; the standing guidance is that host-associated samples use UBERON/PO terms for `env_broad_scale` and `env_medium`. Relevant background for an ENVO term request: **frame the request as an environmental-system class under `ENVO:01001002`, following the `cnidarian-associated environment` pattern, not as a biome.** |

---

## 3. Differentia — what distinguishes it

The differentia is **the determining organism is a mammal (Mammalia)**. What makes that more than a taxonomic bookkeeping label — the observable, measurable correlates a curator can cite — are the following. Siblings under the same genus in the source data are: Birds, Fish, Reptilia, Amphibia, Arthropoda (Insects / Crustaceans / Chelicerates / Myriapoda), Mollusca, Annelida, Porifera, Cnidaria, Tunicates, Cephalochordata, Bryozoa, Invertebrates, and (as protist/fungal/plant siblings under the wider genus) Protists, Protozoa, Amoebozoa, Ciliophora, Fungi, Plants, Algae.

**1. Endothermy and homeothermy at ~36–38 °C — a strong thermal filter on which microbes can colonise.** Robert & Casadevall analysed thermal tolerance of 4,802 fungal strains from 144 genera and found that each 1 °C increase across the 30–40 °C range excludes an additional ~6% of fungal isolates, concluding that mammalian endothermy and homeothermy constitute a potent non-specific defence against most fungi ([Robert & Casadevall 2009, *J Infect Dis* 200:1623–1626, doi:10.1086/644642](https://doi.org/10.1086/644642); PMID 19827944). Bergman & Casadevall modelled the fungal-protection/metabolic-cost trade-off and found an optimum at 36.7 °C, closely matching observed mammalian body temperatures ([*mBio* 1(5):e00212-10, doi:10.1128/mBio.00212-10](https://doi.org/10.1128/mBio.00212-10); PMID 21060737).
   *Discriminating power:* separates this concept sharply from the ectothermic host siblings (Fish, Reptilia, Amphibia, all invertebrate categories), where habitat temperature tracks ambient. **It does not separate it from Birds**, which are also endothermic — state this rather than over-claim.

**2. The mammary gland and milk — a mammal-restricted body site that is itself a sampled habitat.** Milk is described as an ancient, fundamental mammalian adaptation, and milk microbiomes have been detected in every species studied to date, with contributions from maternal gastrointestinal, oral, skin and mammary microbiomes and from the neonate's oral and skin microbiomes ([Reproduction and Fertility 5(2), 2024, doi:10.1530/RAF-23-0056](https://doi.org/10.1530/RAF-23-0056); PMC11046322).
   *Discriminating power:* **this one is exclusive.** No sibling clade has a mammary gland. It is directly visible in the data: `Host-associated > Mammals > Integumentary system > Mammary gland > Milk` carries 650 organisms and `… > Mammary gland` a further 400.

**3. The ruminant forestomach — the single largest sampled mammalian habitat in this dataset.** `Host-associated > Mammals > Digestive system > Foregut > Rumen` is the largest leaf under Mammals (4,989 organisms), plus 450 more at `… > Stomach > Rumen`. The rumen is among the best-characterised host-associated microbial habitats: 4,941 metagenome-assembled genomes were recovered from 283 cattle, raising rumen metagenomic read mapping from 15% to 50–70% ([Stewart et al. 2019, *Nat Biotechnol* 37:953–961, doi:10.1038/s41587-019-0202-3](https://doi.org/10.1038/s41587-019-0202-3); PMID 31375809).
   *Caution — do not over-claim.* Foregut fermentation is **not** unique to mammals: it evolved convergently in ruminants, camelids, colobine monkeys, sloths, some rodents and marsupials, and in the hoatzin, a bird ([Godoy-Vitorino et al. 2011, *ISME J*, foregut and hindgut communities in hoatzins and cows, doi:10.1038/ismej.2011.131](https://doi.org/10.1038/ismej.2011.131)). The defensible claim is the *anatomically distinct ruminant forestomach*, not foregut fermentation as such.

**4. Hair and glandular skin — a lipid-rich integument unlike feathers, scales or fish mucus.** The skin is the primary physical barrier between a vertebrate and its environment, and comparative work across vertebrate classes shows the mammalian skin microbiome is structurally distinct, with human skin distinct not only from other primates but from all ten mammalian orders sampled, and mammalian phylogenetic trees resembling microbial community relatedness trees ([Ross, Rodrigues Hoffmann & Neufeld 2019, *Microbiome* 7:79, doi:10.1186/s40168-019-0694-6](https://doi.org/10.1186/s40168-019-0694-6); PMID 31122279).

**5. Strong phylosymbiosis — gut community composition tracks host phylogeny, more so in mammals than in most vertebrate groups.** The founding result analysed 16S rRNA sequences from faecal microbiota of humans and 59 other mammalian species: diversity increases from carnivory through omnivory to herbivory, and bacterial communities codiversified with their hosts ([Ley et al. 2008, *Science* 320:1647–1651, doi:10.1126/science.1155725](https://doi.org/10.1126/science.1155725); PMID 18497261). Subsequent work refined the mechanism ([Groussin et al. 2017, *Nat Commun* 8:14319, doi:10.1038/ncomms14319](https://doi.org/10.1038/ncomms14319); [Youngblut et al. 2019, *Nat Commun* 10:2200, doi:10.1038/s41467-019-10191-3](https://doi.org/10.1038/s41467-019-10191-3); [Nishida & Ochman / Groussin follow-ups summarised in Youngblut]). A ~900-species vertebrate survey (315 mammals, 491 birds) found phylosymbiosis depends on factors convergently absent in birds *and bats*, likely tied to physiological adaptations for flight ([Song et al. 2020, *mBio* 11:e02901-19, doi:10.1128/mBio.02901-19](https://doi.org/10.1128/mBio.02901-19); PMID 31911491).
   *Honest caveat:* bats are mammals and break the pattern. The clade is not physiologically homogeneous, and the differentia should not claim it is. Scale dependence is also well documented — host phylogeny explains more variance than diet or geography at broad taxonomic scales, with ecology dominating among close relatives ([Youngblut et al. 2019](https://doi.org/10.1038/s41467-019-10191-3); [Nishida & Ochman-style assemblage studies, e.g. *Animal Microbiome* 3:33, 2021, doi:10.1186/s42523-021-00094-4](https://doi.org/10.1186/s42523-021-00094-4)).

**6. Scale of the class.** Mammalia comprises 6,791 extant species (6,774 wild, 17 domestic) out of 6,904 recognised including recently extinct taxa, per the Mammal Diversity Database v2.5 (released 2026-07-28); the peer-reviewed MDD2 release documented 6,759 total / 6,646 extant against a 2024-08-15 cutoff ([Mammal Diversity Database, American Society of Mammalogists, mammaldiversity.org](https://www.mammaldiversity.org/); [*J Mammal* 106(5):1082, 2025, PMID 41103548](https://academic.oup.com/jmammal/article/106/5/1082/8253815)). This is a clade of comparable granularity to the sibling categories GOLD uses — a defence against the charge that the concept is arbitrarily scoped.

### Sibling contrast, at a glance

| Sibling (GOLD ecosystem category) | Body temperature | Mammary gland | Integument | Phylosymbiosis signal |
|---|---|---|---|---|
| **Mammals** | endothermic, ~36–38 °C | **yes** | hair, sebaceous/sweat glands | strong (weaker in bats) |
| Birds | endothermic | no | feathers | weak |
| Reptilia / Amphibia / Fish | ectothermic | no | scales / permeable moist skin / mucus | variable, generally weaker |
| Arthropoda, Mollusca, Porifera, Cnidaria, Annelida | ectothermic | no | cuticle / shell / mesohyl / etc. | clade-specific |

---

## 4. Sources

**Ontologies and standards**

- ENVO term records, queried via EBI OLS4, 2026-08-17: `ENVO:01001002` animal-associated environment; `ENVO:01001000` environmental system determined by an organism; `ENVO:01001055`; `ENVO:01001176`; `ENVO:01001179`. https://www.ebi.ac.uk/ols4/ontologies/envo — PURL: http://purl.obolibrary.org/obo/ENVO_01001002
- Buttigieg P.L. et al. (2013) "The environment ontology: contextualising biological and biomedical entities." *J Biomed Semantics* 4:43. doi:10.1186/2041-1480-4-43 — https://doi.org/10.1186/2041-1480-4-43
- Buttigieg P.L. et al. (2016) "The environment ontology in 2016: bridging domains with increased scope, semantic density, and interoperation." *J Biomed Semantics* 7:57. doi:10.1186/s13326-016-0097-6 — https://doi.org/10.1186/s13326-016-0097-6
- ENVO issue #1029, "EnvO terms for host-associated samples," opened 2020-10-20, closed, labelled *question* — https://github.com/EnvironmentOntology/envo/issues/1029
- ENVO/MIxS usage guidance: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
- Yilmaz P. et al. (2011) "Minimum information about a marker gene sequence (MIMARKS) and minimum information about any (x) sequence (MIxS) specifications." *Nat Biotechnol* 29:415–420. doi:10.1038/nbt.1823 — source of the MIxS `host-associated` environmental package and the `host_taxid` field. https://doi.org/10.1038/nbt.1823
- Mukherjee S. et al. (2025) "Genomes OnLine Database (GOLD) v.10: new features and updates." *Nucleic Acids Research* 53(D1):D989–D997. doi:10.1093/nar/gkae1000 — https://doi.org/10.1093/nar/gkae1000
- JGI GOLD Ecosystem Classification — https://gold.jgi.doe.gov/ecosystem_classification and the path browser https://gold.jgi.doe.gov/ecosystemtree

**Primary and review literature on the habitat**

- Ley R.E. et al. (2008) *Science* 320:1647–1651. doi:10.1126/science.1155725 · PMID 18497261
- Groussin M. et al. (2017) *Nat Commun* 8:14319. doi:10.1038/ncomms14319
- Youngblut N.D. et al. (2019) *Nat Commun* 10:2200. doi:10.1038/s41467-019-10191-3
- Song S.J. et al. (2020) *mBio* 11(1):e02901-19. doi:10.1128/mBio.02901-19 · PMID 31911491 · PMC6946802
- Ross A.A., Rodrigues Hoffmann A., Neufeld J.D. (2019) *Microbiome* 7:79. doi:10.1186/s40168-019-0694-6 · PMID 31122279
- Stewart R.D. et al. (2019) *Nat Biotechnol* 37:953–961. doi:10.1038/s41587-019-0202-3 · PMID 31375809
- Robert V.A. & Casadevall A. (2009) *J Infect Dis* 200:1623–1626. doi:10.1086/644642 · PMID 19827944
- Bergman A. & Casadevall A. (2010) *mBio* 1(5):e00212-10. doi:10.1128/mBio.00212-10 · PMID 21060737
- "Microbiome: Mammalian milk microbiomes: sources of diversity, potential functions, and future research directions." (2024) *Reproduction and Fertility* 5(2). doi:10.1530/RAF-23-0056 · PMC11046322
- Godoy-Vitorino F. et al. (2011) "Comparative analyses of foregut and hindgut bacterial communities in hoatzins and cows." *ISME J*. doi:10.1038/ismej.2011.131
- Mammal Diversity Database, American Society of Mammalogists — https://www.mammaldiversity.org/ ; MDD2 analysis: *J Mammal* 106(5):1082 (2025), PMID 41103548

**Local, non-published evidence (repo data, cited as such)**

- `data/raw/gold_ecosystem_paths.tsv` — 258 paths under `Host-associated > Mammals`, 476 under `Host-associated > Mammals: Human`; per-leaf organism counts quoted in §1.1 and §3.
- `data/habitats/host_associated/mammals.yaml`, `data/habitats/host_associated/mammals_human.yaml`, `curation/decisions.tsv`.

**Statements that are my inference, not a source's claim:** the recommendation to define under Reading A rather than "non-human mammal" (§1.2); the reading of `ENVO:01001179` as *precedent* for a clade-scoped term request (§2.3); the boundary treatment of deposited dung and carcasses (§1.3); and the sibling contrast table (§3), which assembles well-known comparative anatomy rather than reporting a single study.

---

## 5. Synonyms, and what not to conflate

### Names in real use for this concept

- **mammal-associated environment** (the label I would request from ENVO; matches the `cnidarian-associated environment` / `plant-associated environment` pattern)
- **mammalian host-associated environment**, **mammal host environment**, **Mammalia-associated environment**
- **Mammals** (GOLD ecosystem category; the label as attested)
- In MIxS-conformant metadata the same concept is expressed compositionally, not by a single label: `env_package: host-associated` plus `host_taxid` within Mammalia ([Yilmaz et al. 2011](https://doi.org/10.1038/nbt.1823)).
- In EMPO, the nearest expression is "Animal" (mapped to `ENVO:01001002`) — no mammal level exists.

### Commonly but wrongly treated as the same thing

1. **`NCBITaxon:40674` Mammalia** — the taxon. A clade of organisms is not a place. Correct treatment: `relation: xref`. This is the exact conflation that #114 and #112 cost this repo.
2. **`ENVO:01001002` animal-associated environment** — the genus, one level too broad; using it as identity collapses 27 GOLD host categories into one record.
3. **The human concept** (`habitatmech:GOLD.cd0b0940e5` "Mammals: Human", merged `SAME_AS` BacDive "Human") — narrower, not equivalent. Note the arithmetic asymmetry: 40,432 human-node assertions against 6,104 here, so treating them as interchangeable would swamp any non-human signal.
4. **Mammalian anatomy terms** — UBERON gut, skin, blood, rumen. These are the parts; the corpus grounds part-level habitats to them and that is correct. This record is the whole host.
5. **Mammal-derived materials in a food chain** — `FOODON:00005501` mammal material, `FOODON:00001217` mammalian milk beverage, `FOODON:00001006` mammalian meat food product. Bulk-tank milk, cheese and retail meat are food matrices. Milk sampled in the mammary gland is the habitat.
6. **Mammalian cell lines** (BHK, CHO, mouse/rat myeloma) — GOLD nests these under `Mammals`, but they are engineered *in vitro* systems, not a host. Zero assertions here, so no action; flagged so a future re-seed does not silently import them.
7. **Livestock and companion-animal facilities** — barns, manure lagoons, veterinary clinics, zoo enclosures. Built/anthropogenic environments, `ENVO` anthropogenic branch.
8. **Disease states and processes** — `Skin > Digital dermatitis`, `Skin > Lesion`, zoonosis, mastitis. The habitat is the anatomical site; the disease is a process or a quality and, per this repo's convention, `NOT_APPLICABLE` territory if ever minted on its own.
9. **"Vertebrate-associated environment"** — a plausible intermediate, but no such ENVO term exists and no source I found treats Vertebrata as a microbiologically coherent habitat class; the comparative literature repeatedly finds vertebrate classes to be heterogeneous ([Song et al. 2020](https://doi.org/10.1128/mBio.02901-19)).

---

## 6. Should it be a term at all?

**Yes — keep it, as `CONFIRM_UNGROUNDED` with an ENVO term request.** The existing decision is right and this research supports it rather than overturning it.

The reasoning:

- **It is a place, not a taxon claim.** A mammal acting as host is where microbes live. ENVO already models exactly this at plant-, animal- and fungi-associated environment, and already carries clade-scoped children under the animal branch (`ENVO:01001179` cnidarian-associated environment; `ENVO:01001176` environment associated with an aquatic invertebrate). Requesting *mammal-associated environment* is filling in an established pattern, not proposing a new one.
- **It is not `NOT_APPLICABLE`.** That disposition is for diseases, qualities, processes and procedures. Nothing here is one of those, and `tests/test_decisions.py` would reject a NOT_APPLICABLE whose target is an organism term anyway.
- **The differentia is substantive, not merely nominal.** A curator could reasonably object that "the host is a mammal" is a taxonomic label dressed up as an environmental distinction. The answer is §3: endothermy at ~36–38 °C as a documented thermal filter, a mammal-exclusive body site (mammary gland/milk) that is itself sampled 1,050 times in this dataset, a distinct glandular integument, and the strongest phylosymbiosis signal among vertebrate groups. Those are observable and cited.
- **The volume justifies it.** 6,104 assertions at the bare node, and the category as a whole spans 258 paths including the 4,989-organism rumen leaf.

**Two things to state honestly in the term request:**

1. The clade is not physiologically homogeneous — bats break the phylosymbiosis pattern that otherwise characterises mammals ([Song et al. 2020](https://doi.org/10.1128/mBio.02901-19)). The definition should rest on "determined by a mammal," with the physiological correlates as supporting comment, not as necessary and sufficient conditions.
2. GOLD's routing of human samples to a sibling category means the attestations behind this record are in practice non-human. That is a usage fact about the evidence, and belongs in a comment on the record so downstream aggregation is not misled.

**No other action is needed on the record**, beyond optionally dropping the redundant `ENVO:01001000` parent (§2.1) and adding `NCBITaxon:40674` as an xref. Per the standing rule in this repo's memory, **do not file the ENVO term request without explicit per-request approval.**

## Citations

1. https://gold.jgi.doe.gov/ecosystem_classification
2. https://doi.org/10.1093/nar/gkae1000
3. https://github.com/EnvironmentOntology/envo/issues/1029
4. https://doi.org/10.1086/644642
5. https://doi.org/10.1128/mBio.00212-10
6. https://doi.org/10.1530/RAF-23-0056
7. https://doi.org/10.1038/s41587-019-0202-3
8. https://doi.org/10.1038/ismej.2011.131
9. https://doi.org/10.1186/s40168-019-0694-6
10. https://doi.org/10.1126/science.1155725
11. https://doi.org/10.1038/ncomms14319
12. https://doi.org/10.1038/s41467-019-10191-3
13. https://doi.org/10.1128/mBio.02901-19
14. https://doi.org/10.1186/s42523-021-00094-4
15. https://www.mammaldiversity.org/
16. https://academic.oup.com/jmammal/article/106/5/1082/8253815
17. https://www.ebi.ac.uk/ols4/ontologies/envo
18. http://purl.obolibrary.org/obo/ENVO_01001002
19. https://doi.org/10.1186/2041-1480-4-43
20. https://doi.org/10.1186/s13326-016-0097-6
21. https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
22. https://doi.org/10.1038/nbt.1823
23. https://gold.jgi.doe.gov/ecosystemtree