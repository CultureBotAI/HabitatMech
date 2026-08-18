---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T03:17:53.480179'
end_time: '2026-08-18T03:26:05.169836'
duration_seconds: 491.69
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Pupa
  habitat_identifier: habitatmech:GOLD.da1f99888c
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Arthropoda: Insects > Pupa'
  assertions: '0'
  parent_terms: (none)
  xrefs: UBERON:0003143
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term UBERON:0003143 'pupa' attached as a parent. Life-stage review (#112),\
    \ applying the rule #114 settled: the whole host ORGANISM gets its own identity\
    \ plus an <X>-associated environment term, while PARTS of a host ground to the\
    \ anatomy term as gut, skin and lung already do. A larva, pupa, prepupa or embryo\
    \ is the whole organism at a stage, not a part of one, so UBERON:0003143 'pupa'\
    \ is the organism rather than the place \u2014 the same shape as Mollusca, Porifera\
    \ and the host clades. Kept as an xref (#99); the concept keeps its own identity\
    \ as a term-request candidate.This is the line that makes both calls fall out\
    \ of one rule, rather than an exception for terms that happen to live in UBERON:\
    \ a cocoon is a STRUCTURE an insect builds and stays grounded, because it is not\
    \ the organism. (source concept habitatmech:GOLD.da1f99888c)"
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
  total_cost_usd: 3.2592175
  session_id: c03cfa2c-ccda-4319-9762-2a3a613853a4
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 33
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Pupa
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.da1f99888c
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Arthropoda: Insects > Pupa
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** UBERON:0003143

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term UBERON:0003143 'pupa' attached as a parent. Life-stage review (#112), applying the rule #114 settled: the whole host ORGANISM gets its own identity plus an <X>-associated environment term, while PARTS of a host ground to the anatomy term as gut, skin and lung already do. A larva, pupa, prepupa or embryo is the whole organism at a stage, not a part of one, so UBERON:0003143 'pupa' is the organism rather than the place — the same shape as Mollusca, Porifera and the host clades. Kept as an xref (#99); the concept keeps its own identity as a term-request candidate.This is the line that makes both calls fall out of one rule, rather than an exception for terms that happen to live in UBERON: a cocoon is a STRUCTURE an insect builds and stays grounded, because it is not the organism. (source concept habitatmech:GOLD.da1f99888c)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Pupa** as a microbial habitat, with citations.

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

# Pupa (`habitatmech:GOLD.da1f99888c`) — definition research

## Proposed definition

> An insect-associated environment which is determined by a holometabolous insect in its pupal stage — the non-feeding, largely immobile form between the last larval instar and the adult, whose larval gut epithelium and lumen contents have been shed and sequestered as meconium rather than replenished from food.

If the curator prefers to start from a term that already exists rather than from the record's own parent, the equivalent is: *An animal-associated environment (`ENVO:01001002`) which is determined by an insect in its pupal stage …*. The first form is preferable for the same reason it was for `Larva` and `Prepupa`: the record's parent `habitatmech:GOLD.dba2a83b95` ("Arthropoda: Insects") already carries `ENVO:01001002` (verified in `data/habitats/host_associated/arthropoda_insects.yaml`), so the insect restriction does not have to be repeated inside the differentia.

**One decision the curator must make before writing that sentence:** where the stage begins. GOLD carries a *separate* `Prepupa` node, so within this dataset `Pupa` excludes the prepupal phase; UBERON's `pupa` starts at larval–pupal apolysis, while UBERON's `prepupa` starts at *pupariation* — which in cyclorrhaphan flies means an animal already inside a hardened puparium can be labelled either way (§1). The differentia above is written on the functional criteria (non-feeding, gut shed) that hold under both readings; the clause "between the last larval instar and the adult" is deliberately vaguer than "from larval–pupal apolysis" for that reason.

---

## 1. What the concept denotes

**The thing sampled is an insect host at the pupal stage of development, treated as the place the microbes live** — not the stage as an interval of time, and not the cocoon, puparium, soil cell or rearing substrate around it.

### The source path settles the modelling

Verified against `data/raw/gold_ecosystem_paths.tsv` (lines 1833–1836):

| Path | GOLD nodes | Assertions (ORGANISM) |
|---|---|---|
| `… > Insects > Pupa` | 3 (`gold.ecosystem:7253`, `7368`, `7369`) | **0** |
| `… > Insects > Pupa > Cocoon` | 2 (`7254`, `7365`) | 0 |
| `… > Insects > Pupa > Cocoon > Meconium` | 1 (`7255`) | 0 |
| `… > Insects > Pupa > Whole body` | 2 (`7366`, `7367`) | 0 |

Siblings at the same level: `Larva` (94 assertions), `Prepupa` (2), `Nymph/Instar` (3), `Whole body` (60), `Head` (26), `Fat body` (2), `Digestive system` (203 plus children). `Pupa` sits at GOLD's **Ecosystem Type** level (level 3 of the five-level Ecosystem → Ecosystem Category → Ecosystem Type → Ecosystem Subtype → Specific Ecosystem scheme), in the same slot as those organ systems ([Mukherjee et al., *Nucleic Acids Res.* 47:D649–D659, 2019, doi:10.1093/nar/gky977](https://academic.oup.com/nar/article/47/D1/D649/5165343); [GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)). GOLD therefore treats `Pupa` exactly as it treats `Larva` and `Prepupa`: a partition of the host that is then cut finer.

**The whole subtree carries 0 assertions.** Nothing in GOLD has actually been classified to `Pupa` or any of its children. That is a real fact about the evidence base and belongs in the curator's disposition (§6), not a reason to distrust the concept — the sibling `Prepupa` has only 2.

**Boundaries.**

- **Inside:** the pupa's body as sampled — the remodelling midgut and its retained meconium, the haemocoel/haemolymph, fat body, bacteriomes and other symbiont refuges, and the pupal cuticular surface.
- **Immediately outside, each its own GOLD node:** `Larva` (still feeding), `Prepupa`, `Nymph/Instar`, and the adult body compartments.
- **A genuine oddity in GOLD's own tree:** `Cocoon` and `Cocoon > Meconium` hang *under* `Pupa`, although a cocoon is a casing the *larva or prepupa* spins around itself and is not part of the pupa in any mereological sense ([`UBERON:0013198` cocoon: "A casing spun of silk by many moth caterpillars, and numerous other holometabolous insect larvae as a protective covering for the pupa"](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0013198)). HabitatMech already grounds `Cocoon` to `UBERON:0013198` and parents it to this record (`data/habitats/host_associated/cocoon.yaml`), which is the right call under the rule the decision note cites — a structure an insect builds grounds normally — but the definition of *Pupa* must not absorb the cocoon, or the corpus will assert that a silk casing is part of an animal.
- **Also outside:** the pupation substrate (soil, vermiculite, leaf litter, nest cell, brood provision, water surface), the puparium/exuvia once shed, and the frass left behind.

### The label is ambiguous — five readings

1. **UBERON / strict developmental reading.** `UBERON:0003143` "pupa": *"An organism at the pupal stage. A life cycle stage of holometabolous insects in which the organism is a pupa and starts with the larval-pupal apolysis and ends with pupal-adult apolysis"* (synonyms: aurelia, chrysalides, chrysalis, pupae) ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0003143); the record already carries this as an xref). This is the reading I take to be intended.
2. **Colloquial cyclorrhaphan reading.** In higher flies the pupa is enclosed inside a hardened, tanned third-instar larval cuticle — the **puparium** — and lab shorthand calls the whole puparium-plus-contents "the pupa" from puparium formation onward. Under UBERON's boundaries the first ~12 h of that (at 25 °C in *Drosophila*) is the **prepupa**, not the pupa, because `UBERON:0003142` says the prepupal stage *starts* at pupariation. So for Cyclorrhapha the same specimen can be filed under either GOLD node depending on the depositor's convention. This is a real risk of cross-contamination between `Pupa` and `Prepupa` in the data, and it is my inference from the two UBERON definitions plus fly staging practice, not something a source states ([Tajiri et al., *iScience* 26:107361, 2023 — puparium is the tanned larval cuticle](https://www.sciencedirect.com/science/article/pii/S2589004223013561); [Drosophila life cycle, Vanderbilt](https://researchguides.library.vanderbilt.edu/c.php?g=156859&p=1161911)).
3. **Group-specific vernacular readings.** The pupa is called a **chrysalis** in butterflies and a **tumbler** in mosquitoes; these are the same rank of thing, not different things ([Amateur Entomologists' Society glossary, "Pupa"](https://www.amentsoc.org/insects/glossary/terms/pupa/)). Note that the mosquito pupa is *aquatic and actively mobile*, breathing through paired respiratory trumpets — so "immobile" cannot be part of the differentia without excluding Culicidae ([American Mosquito Control Association, Mosquito Biology](https://www.mosquito.org/mosquito-biology/); [Kim et al., *Sci. Rep.* 7:44490, 2017, doi:10.1038/srep44490](https://www.nature.com/articles/srep44490)).
4. **Commodity reading — out of scope.** "Pupae" also names a traded material: silkworm pupae and fly pupae as food and feed. That is a food product (`FOODON:00001177` insect food product), not a host-associated environment, and would be a different record in a different category.
5. **Stage-as-time reading — out of scope.** "Pupal stage" as a developmental interval is a life-cycle-stage term (UBERON/FBdv territory), not a place. The GOLD path forecloses this: nodes at Ecosystem Type are sample provenances.

**Restricting to Holometabola is my inference,** flagged as such. GOLD says only "Insects"; the sibling `Nymph/Instar` node absorbs hemimetabolous immatures, and a true pupa exists only in Holometabola (the thrips "pupa"/"propupa" of neometabolous Thysanoptera is the marginal case the label does not formally exclude).

---

## 2. Genus — the broader kind

**Smallest well-established kind: an insect-associated environment. No ontology term expresses it.**

ENVO's organism-determined branch is the right pattern — an environment "determined by a material entity that assumes the role of an environmental feature", e.g. a coral reef environment determined by a coral reef ([Buttigieg et al., *J. Biomed. Semantics* 4:43, 2013, doi:10.1186/2041-1480-4-43](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3904460/)) — but it stops well short of insects. What exists in the vendored slice (`data/raw/ontology_terms.tsv`):

| CURIE | Label |
|---|---|
| `ENVO:01001000` | environmental system determined by an organism |
| `ENVO:01001001` | plant-associated environment |
| `ENVO:01001002` | animal-associated environment |
| `ENVO:01001041` | fungi-associated environment |
| `ENVO:01001179` | cnidarian-associated environment |

An OLS4 search of ENVO for "insect" returns only *insect conservation process* (`ENVO:01001636`), *resin (gum) varnish*, and incidental mentions — **no insect-associated or arthropod-associated environment class, and nothing life-stage-qualified** ([OLS4 ENVO search](https://www.ebi.ac.uk/ols4/ontologies/envo)). ENVO's own issue tracker shows the host-associated branch was built out by request rather than systematically ([ENVO issue #1029, "EnvO terms for host-associated samples"](https://github.com/EnvironmentOntology/envo/issues/1029)), which is why `cnidarian-associated` exists and `insect-associated` does not.

### Near-misses, and why each fails

- **`UBERON:0003143` "pupa" — the record's xref.** Fails as identity because it denotes *an organism at a stage*, not a place. This is exactly the call the decision note records, and the same shape as Mollusca and Porifera. Keeping it as `relation: xref` preserves the link upstream saw without asserting that a habitat is an organism.
- **`BTO:0001143` "pupa"** — *"An intermediate usually quiescent stage of a metamorphic insect … enclosed in a cocoon or protective covering"*. Same failure, and its definition additionally over-claims: many pupae (butterfly chrysalides, mosquito pupae, most exposed obtect pupae) have no cocoon at all.
- **`UBERON:0013198` "cocoon"** — *narrower and a different entity*: the silk casing, which most pupae lack. It is already a grounded child record; folding it into `Pupa` would be a category error.
- **`ENVO:01001002` "animal-associated environment"** — correct but **too broad**: no insect restriction, no stage restriction. It is the right grandparent, reached through the existing `Arthropoda: Insects` record.
- **`ENVO:01001000` "environmental system determined by an organism"** — broader still; the pattern, not the genus.
- **NCBITaxon insect classes** — taxa, i.e. classes of organisms, not places; the corpus's standing rule.

**Conclusion for the curator:** the genus for the sentence is the record's own parent `habitatmech:GOLD.dba2a83b95` ("Arthropoda: Insects"), and the missing intermediate that would make this cleaner is an ENVO **`insect-associated environment`** — the same gap already recorded for `Larva`, `Prepupa` and `Embryo`. One term request covering all four is more useful than four.

---

## 3. Differentia — what distinguishes it

The pupa is not merely "an insect at an earlier age". The published evidence is that pupation imposes a *specific, measurable* change in the habitat, and these are the properties that separate it from `Larva`, `Prepupa` and the adult body compartments.

**a. It does not feed — the inoculum supply is cut off.** Pupae take no food; mosquito pupae, for instance, subsist on nutrients acquired as larvae ([AMCA](https://www.mosquito.org/mosquito-biology/)). The consequence, which is what matters for a habitat definition, is that the continuous environmental inoculation that dominates larval gut communities stops. In *Drosophila*, whose adult microbiome is maintained by ingestion, adults must re-acquire bacteria after eclosion: 9 of 10 flies had no detectable culturable bacteria 1 h after emergence, and 6 of 10 did within 24 h ([Blum et al., *mBio* 4:e00860-13, 2013, doi:10.1128/mBio.00860-13](https://journals.asm.org/doi/10.1128/mbio.00860-13)).

**b. The larval gut epithelium and its contents are shed and sequestered as meconium.** At the onset of metamorphosis the entire inner larval gut epithelium plus contents is shed and packaged, visible as a dark spot at the distal pole of the pupa and voided at adult emergence; residual microbes are exposed to lysozyme, antimicrobial peptides and pH shifts in the replacement gut ([Hammer & Moran, *Phil. Trans. R. Soc. B* 374:20190068, 2019, doi:10.1098/rstb.2019.0068](https://royalsocietypublishing.org/doi/10.1098/rstb.2019.0068)). In mosquitoes the material is enclosed in a dedicated meconial peritrophic membrane, which is why teneral adults are near-sterile ([Moll et al., *J. Med. Entomol.* 38:29–32, 2001, doi:10.1603/0022-2585-38.1.29](https://academic.oup.com/jme/article/38/1/29/889884)).

**c. Microbial load and diversity fall sharply, and the community turns over.** This is the most directly citable habitat property:

- *Galleria mellonella*: absolute microbiota abundance drops by several orders of magnitude across metamorphosis, and host immunity plus symbiont bacteriocin production jointly determine which lineage survives ([Johnston & Rolff, *PLoS Pathog.* 11:e1005246, 2015, doi:10.1371/journal.ppat.1005246](https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1005246)). *Enterococcus* spp., >90 % of the larval gut community, are replaced by *Enterobacter* spp. in the pupa ([Zhang et al., *Microbiol. Spectr.* 11:e02780-22, 2023, doi:10.1128/spectrum.02780-22](https://journals.asm.org/doi/10.1128/spectrum.02780-22)).
- *Spodoptera littoralis*: of the taxa abundant in larvae, only enterococci persist through metamorphosis ([Chen et al., *Sci. Rep.* 6:29505, 2016, PMID 27389097](https://pubmed.ncbi.nlm.nih.gov/27389097/)).
- *Hermetia illucens*: Shannon diversity is higher in larval and adult stages and **decreased in the pupal stage**; metabarcoding across eggs, larvae, pupae and adults found significant compositional and richness differences along development ([Ao et al., *Microb. Ecol.* 2022, doi:10.1007/s00248-022-02146-x](https://link.springer.com/article/10.1007/s00248-022-02146-x); [Klammsteiner et al., meta-analysis, *Front. Microbiol.* 2022, PMC9453823](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9453823/)).
- *Anopheles gambiae*: Cyanobacteria predominate in larval **and pupal** guts, while Proteobacteria and Bacteroidetes dominate adults ([Wang et al., *PLoS ONE* 6:e24767, 2011, doi:10.1371/journal.pone.0024767](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0024767)). *An. darlingi* larvae and pupae both largely mirror their breeding-site water, with a core independent of site ([Oliveira et al., *Sci. Rep.* 2023, PMC10150499](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10150499/)).
- Across 18 herbivorous species in eight orders, larva-to-adult microbiota turnover (beta diversity) is much higher in holometabolous than hemimetabolous insects ([Rothman/…, *Mol. Ecol.* 2022, doi:10.1111/mec.16673](https://onlinelibrary.wiley.com/doi/10.1111/mec.16673)).

**d. In at least one species the pupa is functionally aposymbiotic and is re-inoculated from outside.** In the burying beetle *Nicrophorus vespilloides*, pupae pass through an aposymbiotic stage and are then recolonised at eclosion with bacteria resembling those on the moulted larval cuticle and on the **wall of the pupal chamber** ([Wang & Rozen, *Appl. Environ. Microbiol.* 83:e03250-16, 2017, doi:10.1128/AEM.03250-16](https://journals.asm.org/doi/10.1128/aem.03250-16)). This is the sharpest available statement that the pupa and its chamber are two different habitats connected by a transmission step — and directly supports keeping the pupation substrate *outside* the concept.

**e. What survives does so in dedicated refuges, not in the lumen.** Sitophilus weevil bacteriocytes dissociate, migrate along the midgut and re-form adult bacteriomes ([Maire et al., *PNAS* 117:19347–19358, 2020, doi:10.1073/pnas.2007151117](https://www.pnas.org/doi/10.1073/pnas.2007151117)); in *Camponotus floridanus* the midgut effectively becomes a symbiotic organ during the pupal stages ([Stoll et al., *BMC Microbiol.* 10:308, 2010, doi:10.1186/1471-2180-10-308](https://link.springer.com/article/10.1186/1471-2180-10-308)); *Lagria* beetles bypass the internal reorganisation entirely by holding defensive symbionts in cuticular structures ([Rossi et al., *Front. Physiol.* 2022, PMC9468232](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9468232/)); see also [Moriyama & Fukatsu, *PNAS* 120:e2304879120, 2023](https://www.pnas.org/doi/10.1073/pnas.2304879120).

**f. The pupal integument is a sclerotised, melanised barrier.** Mature pupae resist entomopathogenic fungi that readily kill larvae and prepupae: in Queensland fruit fly, third-instar larvae were the most susceptible stage (51–98 % mortality by isolate) while older pupae showed no sign of fungal infection, attributed to melanisation and sclerotisation of the mature pupal cuticle ([Nguyen et al., *PLoS ONE* 19:e0297341, 2024, doi:10.1371/journal.pone.0297341](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0297341)).

**g. Practical consequence — low biomass.** Because of (a)–(c), pupal samples are low-biomass and vulnerable to reagent contamination: abundant control ASVs fall in *Acinetobacter*, *Chryseobacterium*, *Enterobacter* and *Pseudomonas*, the same genera reported as mosquito "core" taxa ([Chandler-style decontamination example, *Appl. Environ. Microbiol.* 2021, PMC8265668](https://pmc.ncbi.nlm.nih.gov/articles/PMC8265668/)). Worth a `notes` line on the record; not part of the definition.

**Properties that must NOT go in the differentia,** because they are not general: *encased in a cocoon* (most pupae are not), *immobile* (mosquito tumblers swim), *terrestrial* (mosquito pupae are aquatic), *inside a puparium* (Cyclorrhapha only), *lasting days* (many species overwinter as pupae).

---

## 4. Sources

Verified in the repository (not literature):

- `data/raw/gold_ecosystem_paths.tsv` lines 1833–1836 — node ids, path shape, 0 assertions.
- `data/habitats/host_associated/arthropoda_insects.yaml` — parent carries `ENVO:01001000`, `ENVO:01001002`; 1,833 ORGANISM assertions.
- `data/habitats/host_associated/cocoon.yaml`, `meconium__b08d4474.yaml`, `whole_body__86c6fa8b.yaml` — existing children.
- `data/raw/ontology_terms.tsv` — the five `*-associated environment` classes listed in §2, and the UBERON/BTO pupa definitions quoted.

Literature and vocabularies, with identifiers:

| Claim | Source |
|---|---|
| GOLD five-level classification | Mukherjee et al., *Nucleic Acids Res.* 47:D649, 2019, [doi:10.1093/nar/gky977](https://academic.oup.com/nar/article/47/D1/D649/5165343); [GOLD v.9, PMID 36318257](https://pubmed.ncbi.nlm.nih.gov/36318257/) |
| ENVO organism-determined-environment pattern | Buttigieg et al., *J. Biomed. Semantics* 4:43, 2013, [doi:10.1186/2041-1480-4-43](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3904460/); [ENVO issue #1029](https://github.com/EnvironmentOntology/envo/issues/1029) |
| `UBERON:0003143` pupa definition | [OLS4](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0003143) |
| Gut shed, meconium, immune challenge | Hammer & Moran, *Phil. Trans. R. Soc. B* 374:20190068, 2019, [doi:10.1098/rstb.2019.0068](https://royalsocietypublishing.org/doi/10.1098/rstb.2019.0068) |
| Meconial peritrophic membrane in mosquitoes | Moll et al., *J. Med. Entomol.* 38:29, 2001, [doi:10.1603/0022-2585-38.1.29](https://academic.oup.com/jme/article/38/1/29/889884) |
| Orders-of-magnitude load reduction; host+symbiont control | Johnston & Rolff, *PLoS Pathog.* 11:e1005246, 2015, [doi:10.1371/journal.ppat.1005246](https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1005246) |
| *Enterococcus* → *Enterobacter* turnover in pupae | *Microbiol. Spectr.* 11:e02780-22, 2023, [doi:10.1128/spectrum.02780-22](https://journals.asm.org/doi/10.1128/spectrum.02780-22) |
| Only enterococci persist (Lepidoptera) | Chen et al., *Sci. Rep.* 2016, [PMID 27389097](https://pubmed.ncbi.nlm.nih.gov/27389097/) |
| Pupal diversity minimum in BSF | *Microb. Ecol.* 2022, [doi:10.1007/s00248-022-02146-x](https://link.springer.com/article/10.1007/s00248-022-02146-x); meta-analysis [PMC9453823](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9453823/); vertical transmission across stages [PMC11129375](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11129375/) |
| Cyanobacteria in larval/pupal guts | Wang et al., *PLoS ONE* 6:e24767, 2011, [doi:10.1371/journal.pone.0024767](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0024767) |
| Immature mosquito microbiota mirrors breeding site | [*Sci. Rep.* 2023, PMC10150499](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10150499/) |
| Holometabolous > hemimetabolous turnover | *Mol. Ecol.* 2022, [doi:10.1111/mec.16673](https://onlinelibrary.wiley.com/doi/10.1111/mec.16673) |
| Aposymbiotic pupa, recolonised from pupal chamber | Wang & Rozen, *AEM* 83:e03250-16, 2017, [doi:10.1128/AEM.03250-16](https://journals.asm.org/doi/10.1128/aem.03250-16), [PMID 28213538](https://pubmed.ncbi.nlm.nih.gov/28213538/) |
| Bacteriocyte migration through metamorphosis | Maire et al., *PNAS* 117:19347, 2020, [doi:10.1073/pnas.2007151117](https://www.pnas.org/doi/10.1073/pnas.2007151117); Stoll et al., *BMC Microbiol.* 10:308, 2010, [doi:10.1186/1471-2180-10-308](https://link.springer.com/article/10.1186/1471-2180-10-308); Moriyama & Fukatsu, *PNAS* 2023, [doi:10.1073/pnas.2304879120](https://www.pnas.org/doi/10.1073/pnas.2304879120) |
| Ectosymbiont cuticular refuge (Lagria) | [*Front. Physiol.* 2022, PMC9468232](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9468232/) |
| Adults re-acquire microbes after eclosion | Blum et al., *mBio* 4:e00860-13, 2013, [doi:10.1128/mBio.00860-13](https://journals.asm.org/doi/10.1128/mbio.00860-13) |
| Melanised pupal cuticle resists fungal infection | [*PLoS ONE* 19:e0297341, 2024](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0297341) |
| Mosquito pupa aquatic, mobile, non-feeding, trumpets | [AMCA Mosquito Biology](https://www.mosquito.org/mosquito-biology/); [Kim et al., *Sci. Rep.* 7:44490, 2017](https://www.nature.com/articles/srep44490) |
| Puparium is tanned third-instar cuticle | [Tajiri et al., *iScience* 2023](https://www.sciencedirect.com/science/article/pii/S2589004223013561) |
| Pupa / chrysalis / cocoon / puparium usage | [AES Entomologists' Glossary](https://www.amentsoc.org/insects/glossary/terms/pupa/) |
| Low-biomass contamination caution | [*Appl. Environ. Microbiol.* 2021, PMC8265668](https://pmc.ncbi.nlm.nih.gov/articles/PMC8265668/) |

**Explicitly my inference, not sourced:** (i) that GOLD's `Pupa` means the holometabolous pupa; (ii) that the cyclorrhaphan "pupa"/"prepupa" convention clash puts specimens at risk of landing under either GOLD node; (iii) that the pupation substrate belongs outside the concept — supported by, but not stated as a boundary claim in, Wang & Rozen 2017.

---

## 5. Synonyms and what NOT to conflate

**Names in real use for this concept:** pupa, pupae, pupal stage, pupal-stage insect; **chrysalis** / chrysalides / aurelia (Lepidoptera, chiefly butterflies — all listed as UBERON synonyms); **tumbler** (Culicidae); obtect pupa, exarate pupa, coarctate pupa (morphological types, all still pupae); "pupal whole body" (GOLD's own child node, `gold.ecosystem:7366/7367`).

**Commonly but wrongly treated as the same thing:**

- **Prepupa** — a separate GOLD node with its own record (`habitatmech:GOLD.ccdfcd10b9`) and its own UBERON term; the non-feeding phase *before* pupation. In Cyclorrhapha the boundary is convention-dependent (§1); in Hymenoptera "prepupa" often means the post-defecating final-instar larva, which is not a pupa at all.
- **Cocoon** (`UBERON:0013198`) — the silk casing, spun by the larva/prepupa, absent in most pupae. Already its own grounded record; GOLD's nesting under `Pupa` should not be read as parthood.
- **Puparium / pupal case / exuvia** — the hardened third-instar larval cuticle in higher flies, and the shed skin after eclosion. It is *not* the pupa, has no UBERON term in the vendored slice, and if it is ever sampled it is a distinct surface habitat.
- **Insect meconium vs. mammalian meconium** — **a live problem in the corpus.** `habitatmech:GOLD.fb82b19ebb` ("Meconium", path `… > Pupa > Cocoon > Meconium`) is grounded `NARROW` to `UBERON:0007109`, whose definition is *"A dark greenish mass that accumulates in the bowel during fetal life and is discharged shortly after birth"* — the mammalian neonatal material. The insect meconium is the shed larval gut epithelium and contents voided at adult eclosion (Hammer & Moran 2019). These are homonyms, not a broader/narrower pair. Worth a GitHub issue against the seeded grounding independently of this definition.
- **Pupal chamber / pupal cell / pupation substrate / soil** — the surrounding environment, and demonstrably a *different* community that re-inoculates the emerging adult (Wang & Rozen 2017).
- **Nymph / instar** — hemimetabolous immatures; separate GOLD node, and no true pupa.
- **Silkworm or fly pupae as food or feed** — a food product (`FOODON:00001177` domain), not a host-associated environment.
- **"Pupal stage" as a life-cycle stage term** — a temporal interval; the modelling error this record's decision note exists to prevent.

---

## 6. Whether it should be a term at all

**Yes — keep it, and treat it as a term-request candidate,** on three grounds:

1. **It is a place, not a taxon, quality, process or disease.** It denotes a host organism acting as a habitat, which the corpus already settled (#114) is a habitat; the taxonomic/anatomical term `UBERON:0003143` correctly stays an xref. `NOT_APPLICABLE` would be the wrong disposition.
2. **The differentia is empirically real, not merely nominal.** Unlike a label that just subsets a host by convenience, the pupal interior is measurably a different habitat from the larval one — feeding stops, the gut epithelium and lumen are shed, load falls by orders of magnitude, diversity reaches a minimum, at least one species is functionally aposymbiotic, and the surviving symbionts occupy dedicated refuges (§3). That is the strongest case among the four life-stage records for the stage being a habitat class in its own right.
3. **Structurally it cannot be dropped.** `Cocoon` (a grounded record with a real ontology term) and `Whole body` hang off it. Removing `Pupa` orphans them.

**The honest caveat to record alongside the definition:** GOLD carries **zero** assertions on `Pupa` and all its children, so nothing in the upstream data has actually been sampled under this path. The concept is well-evidenced in the literature and structurally load-bearing in the corpus, but its *upstream* attestation is a bare node. If the term request to ENVO is prioritised by evidence volume, `Larva` (94 assertions) outranks it — and one request for an **`insect-associated environment`** intermediate, with `insect pupa-associated environment`, `insect larva-associated environment` and siblings beneath it, serves all four records at once and is the request I would file.

## Citations

1. https://academic.oup.com/nar/article/47/D1/D649/5165343
2. https://gold.jgi.doe.gov/ecosystem_classification
3. https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0013198
4. https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0003143
5. https://www.sciencedirect.com/science/article/pii/S2589004223013561
6. https://researchguides.library.vanderbilt.edu/c.php?g=156859&p=1161911
7. https://www.amentsoc.org/insects/glossary/terms/pupa/
8. https://www.mosquito.org/mosquito-biology/
9. https://www.nature.com/articles/srep44490
10. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3904460/
11. https://www.ebi.ac.uk/ols4/ontologies/envo
12. https://github.com/EnvironmentOntology/envo/issues/1029
13. https://journals.asm.org/doi/10.1128/mbio.00860-13
14. https://royalsocietypublishing.org/doi/10.1098/rstb.2019.0068
15. https://academic.oup.com/jme/article/38/1/29/889884
16. https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1005246
17. https://journals.asm.org/doi/10.1128/spectrum.02780-22
18. https://pubmed.ncbi.nlm.nih.gov/27389097/
19. https://link.springer.com/article/10.1007/s00248-022-02146-x
20. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9453823/
21. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0024767
22. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10150499/
23. https://onlinelibrary.wiley.com/doi/10.1111/mec.16673
24. https://journals.asm.org/doi/10.1128/aem.03250-16
25. https://www.pnas.org/doi/10.1073/pnas.2007151117
26. https://link.springer.com/article/10.1186/1471-2180-10-308
27. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9468232/
28. https://www.pnas.org/doi/10.1073/pnas.2304879120
29. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0297341
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC8265668/
31. https://pubmed.ncbi.nlm.nih.gov/36318257/
32. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11129375/
33. https://pubmed.ncbi.nlm.nih.gov/28213538/