---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:46:22.876451'
end_time: '2026-08-17T16:54:40.577479'
duration_seconds: 497.7
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Caprinae-Sheep/Goat
  habitat_identifier: habitatmech:BACDIVE.4d3086a839
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Caprinae-Sheep/Goat'
  assertions: '412'
  parent_terms: (none)
  xrefs: FOODON:03411328
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term FOODON:03411328 'goat' attached as a parent. Host-taxon reversal\
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
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:BACDIVE.4d3086a839)"
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
  web_search_requests: 18
  num_turns: 29
  total_cost_usd: 3.572918
  session_id: b3470c38-9f11-4850-b9aa-667d75a9b32a
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 33
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Caprinae-Sheep/Goat
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.4d3086a839
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Caprinae-Sheep/Goat
- **Upstream assertion volume:** 412
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** FOODON:03411328

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term FOODON:03411328 'goat' attached as a parent. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:BACDIVE.4d3086a839)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Caprinae-Sheep/Goat** as a microbial habitat, with citations.

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

# Caprinae-Sheep/Goat (`habitatmech:BACDIVE.4d3086a839`) — definition research

## Proposed definition

> An animal-associated environment which is determined by a member of the bovid subfamily Caprinae, chiefly the domestic sheep (*Ovis aries*) or the domestic goat (*Capra hircus*).

A second sentence would be needed to say *which parts* of the host are in scope (body sites, secretions, excreta). I recommend that go in a `comment`, not the definition — see §1, where I argue the missing intermediate class is a general **mammal-associated / livestock-associated environment** tier that ENVO does not currently have.

---

## 1. What the concept denotes

**The label is a BacDive isolation-source tag, and its path is the decisive evidence.** BacDive classifies isolation sources with a three-level controlled vocabulary (the Microbial Isolation Source Ontology, MISO), whose eight level-1 classes are `#Environmental`, `#Engineered`, `#Host`, `#Host body-site`, `#Host body-product`, `#Medical`, `#Condition` and `#Climate` ([Reimer et al. 2019, *NAR* 47:D631–D636](https://doi.org/10.1093/nar/gky879), PMID 30256983). Fetching the live browser at <https://bacdive.dsmz.de/isolation-sources> confirms the exact node: **`#Host` → `Mammals` → `Caprinae (Sheep/Goat)`**, sitting alongside sibling level-3 tags `Bovinae (Cow, Cattle)`, `Suidae (Pig, Swine)`, `Equidae (Horse)`, `Canidae (Dog)`, `Felidae (Cat)`, `Muridae (Mouse/Rat)`, `Leporidae (Rabbit/Hare)`, `Primates` and `Rodentia (Other)`.

So the concept denotes **the host organism as the environment a strain was recovered from** — a sheep or a goat, considered as the place where the microbe lived. It does *not* denote an anatomical site: BacDive carries site and product as **separate, co-annotated level-1 categories** (`#Host body-site`, `#Host body-product`). This is the sharpest boundary statement available and it is upstream's own design, not an inference: a strain from goat milk is tagged `Caprinae (Sheep/Goat)` **and** a body-product tag, and this record only inherits the former.

**What is inside the concept:** any sheep or goat (and, by the tag's name, any other caprine) from which a strain was isolated, whatever the body site — rumen and lower gut, nasal and conjunctival mucosa, skin, udder and milk, joint and synovial fluid, placenta and aborted fetal tissue, abscess material, and faeces/dung.

**What is a neighbouring concept, not this one:**
- `Bovinae (Cow, Cattle)` and `Suidae (Pig, Swine)` — sibling host tags at the same level.
- Any `#Host body-site` term (rumen, skin, nasal cavity) — these ground to UBERON anatomy and are *parts*, which per this repo's rule ground normally; the whole host does not.
- `#Host body-product` terms (milk, faeces) — likewise separate.
- Sheep- or goat-derived **foods** (raw ewe's-milk cheese, pecorino) — FOODON territory, a manufactured material, not the host.
- **Defibrinated sheep blood in culture media** — a laboratory reagent, not an isolation source (see §5).

**One genuine ambiguity, which the curator must resolve explicitly.** The tag name pairs a subfamily (*Caprinae*, [NCBITaxon:9963](https://www.ebi.ac.uk/ols4/ontologies/ncbitaxon/classes?obo_id=NCBITaxon:9963)) with two vernacular species names. Caprinae as a clade contains ~11 genera and ~31 species, including muskox (*Ovibos*), chamois (*Rupicapra*), serows, gorals, takin and the Tibetan antelope ([Wikipedia: Caprinae](https://en.wikipedia.org/wiki/Caprinae); [Ultimate Ungulate: Caprinae](https://www.ultimateungulate.com/Artiodactyla/Caprinae.html)). The two readings are:

1. **Broad (nomenclatural):** any caprine, wild or domestic. This is what the tag name literally says, and wild caprine isolates exist in the literature (e.g. *Mycoplasma conjunctivae* from wild Caprinae, [Fernández-Aguilar et al. 2013, *BMC Vet Res*](https://pmc.ncbi.nlm.nih.gov/articles/PMC3883482/)).
2. **Narrow (operational):** domestic sheep and goats, i.e. "small ruminants" in the veterinary sense. This is what the parenthetical says and almost certainly what the 412 strains are.

I could not enumerate the 412 strains to settle this empirically, so **I recommend the definition name the subfamily as the genus-level scope and name the two domestic species as the typical case** ("chiefly …"), which is true under both readings. That is the wording proposed above.

**A signal in this record worth reading before writing the definition.** The top characteristic taxa on the record are overwhelmingly myxobacteria — *Corallococcus coralloides* (40), *Myxococcus fulvus* (29), *Nannocystis exedens* (27), *Sorangium cellulosum* (24), *M. xanthus* (18), *M. virescens* (16), *Archangium disciforme* (10). **My inference** (upstream does not state it) is that these come from **dung-baited isolation**: partially embedding autoclaved herbivore dung pellets in soil or water agar is the standard myxobacterial isolation method, and rabbit, goat and other herbivore pellets are all used ([Zhang et al. 2003, *J Microbiol Methods* 54:21–29](https://doi.org/10.1016/S0167-7012(02)00257-9), PMID 12732418; [Sharma et al. 2022, *J Basic Microbiol* 62:162–173](https://doi.org/10.1002/jobm.202100518), which isolates myxobacteria from Himalayan animal dung pellets). The rest of the list is unambiguously caprine host biology: *Moraxella caprae* (7), *Mannheimia haemolytica* (6), *M. glucosida* (6), *Arcanobacterium pluranimalium* (6), *Corynebacterium pseudotuberculosis* (4), *Streptococcus ovis* (4), *Actinobacillus seminis* (4), plus rumen *Butyrivibrio* sp. (5) and *Campylobacter sputorum* (15).

The practical consequence: this tag mixes **strains that lived in the host** with **strains recovered from host-derived material that had already left the host and become an environmental substrate** (dung pellets on the ground, from which a soil myxobacterium was baited). A definition that says "environment determined by a caprine" covers both if "determined by" is read the way ENVO reads it; a definition that says "the interior of a sheep or goat" would exclude the largest single taxon block on the record. Prefer the former.

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001002` *animal-associated environment*** — "An environmental system determined by an animal", with synonyms *metazoan-associated environment* and *animal environment*; parent *environmental system determined by an organism*; mapped to EMPO "Animal" ([OLS4 / ENVO](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002); PURL <http://purl.obolibrary.org/obo/ENVO_01001002>).

This is exactly the modelling pattern the curator's note invokes, and ENVO adopted it precisely because host-derived microbiome samples have the host organism as their biome ([ENVO issue #1029, "EnvO terms for host-associated samples"](https://github.com/EnvironmentOntology/envo/issues/1029)). It is also in routine MIxS/BioSample practice as `env_broad_scale` / `env_local_scale` for host-associated samples ([Oregon State CQLS SRA submission guide](https://docs.hpc.oregonstate.edu/cqls/tips/submitting-sra-data/)).

**There is no existing term for this concept — near-misses, checked in ENVO via OLS4:**

| Candidate | Why it fails |
|---|---|
| `ENVO:01001002` animal-associated environment | **Match for the genus, too broad for the concept** — covers every metazoan host. Use as parent. |
| `ENVO:01001055` environment associated with an animal part or small animal | *Narrower and wrong-shaped*: "determined by part of a living or dead animal, or a whole small animal". A sheep is not a small animal, and the concept is the whole host, not a part. |
| `ENVO:01001176` environment associated with an aquatic invertebrate | Wrong clade; recorded only to show ENVO does mint taxon-shaped children of `ENVO:01001002`. |
| `ENVO:01001179` cnidarian-associated environment | **The precedent that matters.** ENVO already has a taxon-scoped `<clade>-associated environment` under animal-associated environment, so "Caprinae-associated environment" is a well-formed request, not a novel pattern. |
| Any mammal / vertebrate / ruminant / livestock tier | **Does not exist.** A full OLS4 sweep of ENVO labels containing "associated environment" returns exactly eight terms: plant- (`ENVO:01001001`), animal- (`ENVO:01001002`), fungi- (`ENVO:01001041`), environment associated with an animal part or small animal (`01001055`), with a plant part or small plant (`01001057`), with a fungal tissue (`01001058`), with an aquatic invertebrate (`01001176`), cnidarian- (`01001179`). There is nothing between "animal" and "cnidarian". |
| `ENVO:00000077` agricultural ecosystem, `ENVO:02000047` animal feed, `ENVO:00002869` hay | The only ENVO hits for "sheep". All are the *setting* or the *feed*, not the host. |
| `FOODON:03411328` goat (current xref) | **Half the concept and the wrong kind of thing.** Defined as "A whole goat" / "a goat which is dead or alive and has a relatively intact body" — a food-source organism class, not an environmental system, and it drops sheep entirely. The upstream mapping is a `skos:closeMatch` from lexical matching at *medium* confidence (`data/raw/isolation_source_groundings.tsv`), which is exactly the strength of evidence that should stay an xref. |
| `FOODON:03411183` sheep ("A whole sheep") | Same objection; worth adding as a **second xref** so the record does not silently privilege goat over sheep. |
| `NCBITaxon:9963` Caprinae | A class of organisms, not a place — `relation: xref` per the repo's #99/#114 rule. |

**Missing intermediate class (worth saying out loud rather than lengthening the definition):** the corpus is generating ten sibling host-taxon records from one BacDive level (`Bovinae`, `Suidae`, `Equidae`, `Muridae`, …) and ENVO offers them a single shared parent, `animal-associated environment`. If HabitatMech ever requests these upstream, the coherent request is a small stack — *mammal-associated environment* (or *livestock-associated environment*) between `ENVO:01001002` and the per-taxon leaves — rather than ten flat siblings.

## 3. Differentia — what distinguishes it

Ordered by how observable each property is.

**(a) Host identity — the primary differentia.** The host is a caprine bovid: subfamily Caprinae, family Bovidae, order Artiodactyla, suborder Ruminantia; wild progenitors *Ovis orientalis* and *Capra aegagrus*, both domesticated in the northern Zagros–southeastern Anatolia arc between roughly 11,000 and 10,500 BP, with caprine herd-management signals at ca. 10,500 BP ([Zeder 2008, *PNAS* 105:11597–11604](https://doi.org/10.1073/pnas.0801317105)). This alone separates the concept from every sibling host tag.

**(b) Foregut fermentation — shared with `Bovinae`, distinguishing from `Suidae`/`Equidae`.** The dominant microbial compartment is the rumen: an anaerobic, host-thermostatted fermentation chamber at ~39 °C (working ranges of 38–41 °C reported), diurnally varying pH 5.5–7.0, 12–18% w/v solids, osmolality ~250–400 mOsm/kg, VFA 7–12 g/L, with 70–85% of the bacterial community attached to feed particles and liquid/solid retention times of 8–12 h and ~48 h respectively ([Matthews et al. 2019, *Gut Microbes*; summarised with these parameters in the 2024 review, PMC11117383](https://pmc.ncbi.nlm.nih.gov/articles/PMC11117383/)). The record's *Butyrivibrio* sp. attestation is a direct rumen signal.

**(c) Sheep-vs-goat feeding ecology — the differentia *within* the concept, and the reason to keep the two together at this level.** Goats are browsers/opportunistic mixed feeders and sheep are grazers, with goats taking lower-fibre browse at varied heights and sheep taking high-fibre herbaceous swards; goats show a faster passage rate and greater tannin tolerance ([Merck Veterinary Manual, Nutritional Requirements of Goats](https://www.merckvetmanual.com/management-and-nutrition/nutrition-goats/nutritional-requirements-of-goats); [Mkhize et al. 2015, *Small Rumin Res*, Bonga sheep vs Kaffa goats tannin challenge, PMC4710639](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4710639/)). The microbiome consequence is genuinely contested and should **not** be asserted in a definition: co-grazed Tibetan goats and sheep differ in protein-degrading bacteria, fibre-degrading fungi/protozoa and VFA levels ([Wang et al. 2020, *Animals*, PMC7070549](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7070549/)); a 2024 tannin-forage study found greater compositional variability in sheep than goats ([*J Anim Sci* 2024, PMC11484804](https://pmc.ncbi.nlm.nih.gov/articles/PMC11484804/)); a 2025 overview reports no substantial sheep–goat difference ([*Animals* 15:758](https://www.mdpi.com/2076-2615/15/5/758)); and the largest cross-host survey attributes most variation to diet rather than host ([Henderson et al. 2015, *Sci Rep* 5:14567](https://doi.org/10.1038/srep14567)). **Defensible summary for a comment field:** sheep and goats overlap heavily and are frequently analysed jointly as "small ruminants", with reported differences smaller and less consistent than diet effects.

**(d) Characteristic caprine-restricted or caprine-associated taxa** — the most concrete observable differentia, and each is independently citable:
- *Moraxella caprae*, described from the nasal flora of healthy goats ([Kodjo et al. 1995, *IJSB* 45:467–471](https://doi.org/10.1099/00207713-45-3-467), PMID 8590674); *M. boevrei* likewise from goat nasal flora; *M. ovis* from sheep conjunctivitis.
- *Corynebacterium pseudotuberculosis* biovar *ovis*, agent of caseous lymphadenitis, a worldwide chronic disease of sheep and goats with external abscessation predominating in goats and internal forms in sheep ([Dorella et al. 2006, *Vet Res* 37:201–218](https://doi.org/10.1051/vetres:2005056), PMID 16472520; [Czech ovine/caprine strain comparison 2024, PMC11123211](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11123211/)).
- *Mycoplasma agalactiae*, *M. capricolum*, *M. mycoides* subsp. *capri*, *M. ovipneumoniae*, *M. conjunctivae* — the small-ruminant mycoplasma set ([Fernández-Aguilar et al. 2013, PMC3883482](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3883482/); [Besser et al. 2017, PMC5462392](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5462392/)).
- The zoonotic abortifacient triad shed in placenta, amniotic fluid, faeces and milk: *Brucella melitensis*, *Chlamydia abortus*, *Coxiella burnetii* ([Ahmed et al. 2023, *Front Vet Sci* / PMC10422025](https://pmc.ncbi.nlm.nih.gov/articles/PMC10422025/)).
- *Listeria ivanovii*, recovered from bulk-tank sheep and goat milk ([Papatsiros et al. 2022, PMC9220212](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9220212/)).

**(e) Anthropogenic setting.** Except for wild caprines, this environment is a managed farm animal, so the community is shaped by husbandry, diet formulation and antimicrobial use. This is well-supported generally but is *background*, not differentia — it is equally true of `Bovinae` and `Suidae`.

## 4. Sources

| Claim | Source |
|---|---|
| BacDive MISO three-level source vocabulary; eight level-1 classes incl. `#Host`, `#Host body-site`, `#Host body-product` | Reimer LC et al., *Nucleic Acids Res* 47:D631–D636 (2019). [doi:10.1093/nar/gky879](https://doi.org/10.1093/nar/gky879), PMID 30256983 |
| Current BacDive release / scale | Schober I, Koblitz J et al., *Nucleic Acids Res* 53:D748–D756 (2025). [doi:10.1093/nar/gkae959](https://doi.org/10.1093/nar/gkae959) |
| The exact tag `#Host → Mammals → Caprinae (Sheep/Goat)` and its siblings | <https://bacdive.dsmz.de/isolation-sources> (fetched 2026-08-17) |
| `ENVO:01001002` label, definition, parent, EMPO mapping | <http://purl.obolibrary.org/obo/ENVO_01001002> ; [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002) |
| ENVO has exactly eight `*-associated environment` terms; none for mammals/ruminants/sheep/goat | OLS4 ENVO label search, 2026-08-17 (`ENVO:01001001, 01001002, 01001041, 01001055, 01001057, 01001058, 01001176, 01001179`) |
| ENVO's rationale for host-as-environment terms | [EnvironmentOntology/envo issue #1029](https://github.com/EnvironmentOntology/envo/issues/1029) |
| `FOODON:03411328` "goat" = a whole goat, dead or alive; `FOODON:03411183` "sheep" | [OLS4 FOODON](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03411328) |
| `NCBITaxon:9963` = Caprinae | [OLS4 NCBITaxon](https://www.ebi.ac.uk/ols4/ontologies/ncbitaxon/classes?obo_id=NCBITaxon:9963) |
| Caprinae scope: subfamily of Bovidae, ~11 genera / ~31 species, incl. muskox, chamois, goral, takin, Tibetan antelope | [Wikipedia: Caprinae](https://en.wikipedia.org/wiki/Caprinae); [Ultimate Ungulate: Caprinae](https://www.ultimateungulate.com/Artiodactyla/Caprinae.html); [Encyclopedia.com, Bovids VI](https://www.encyclopedia.com/environment/encyclopedias-almanacs-transcripts-and-maps/bovids-vi-sheep-goats-and-relatives-caprinae) |
| Domestication ca. 11,000–10,500 BP; progenitors *Ovis orientalis*, *Capra aegagrus* | Zeder MA, *PNAS* 105:11597–11604 (2008). [doi:10.1073/pnas.0801317105](https://doi.org/10.1073/pnas.0801317105) |
| Rumen physicochemistry (39 °C, pH 5.5–7.0, solids, osmolality, VFA, particle attachment, retention times) | Review, *Microorganisms*/PMC11117383 (2024). <https://pmc.ncbi.nlm.nih.gov/articles/PMC11117383/> |
| Diet outweighs host across 742 samples / 32 ruminant species | Henderson G et al., *Sci Rep* 5:14567 (2015). [doi:10.1038/srep14567](https://doi.org/10.1038/srep14567) |
| Sheep–goat rumen community differences in co-grazed animals | *Animals* / PMC7070549 (2020). <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7070549/> |
| Sheep more variable than goats on tannin-rich forage | *J Anim Sci* skae198 (2024). [doi:10.1093/jas/skae198](https://doi.org/10.1093/jas/skae198), PMC11484804 |
| "No substantial differences between sheep and goats" | *Animals* 15:758 (2025). <https://www.mdpi.com/2076-2615/15/5/758> |
| Browser/grazer distinction, passage rate, tannin tolerance | [Merck Vet Manual: Nutritional Requirements of Goats](https://www.merckvetmanual.com/management-and-nutrition/nutrition-goats/nutritional-requirements-of-goats); PMC4710639 |
| *Moraxella caprae* from goat nasal flora | Kodjo A et al., *Int J Syst Bacteriol* 45:467–471 (1995). [doi:10.1099/00207713-45-3-467](https://doi.org/10.1099/00207713-45-3-467), PMID 8590674 |
| *C. pseudotuberculosis* / caseous lymphadenitis in sheep and goats | Dorella FA et al., *Vet Res* 37:201–218 (2006), PMID 16472520; PMC11123211 (2024) |
| Small-ruminant mycoplasmas; wild Caprinae involvement | PMC3883482 (2013); PMC5462392 (2017) |
| Zoonotic abortifacients (*Brucella*, *C. abortus*, *C. burnetii*) shed in placenta/milk/faeces | PMC10422025 (2023) |
| *Listeria ivanovii* from bulk-tank sheep/goat milk | PMC9220212 (2022) |
| Dung-pellet baiting as standard myxobacterial isolation; goat dung used | Zhang YQ et al., *J Microbiol Methods* 54:21–29 (2003), PMID 12732418; Sharma et al., *J Basic Microbiol* 62:162–173 (2022), [doi:10.1002/jobm.202100518](https://doi.org/10.1002/jobm.202100518) |

**Explicitly my inference, not sourced:** (i) that the myxobacterial block on this record reflects dung-baited isolation rather than in-host residence; (ii) that the operative reading of the tag is domestic sheep and goats; (iii) that the sibling host-taxon records collectively imply a missing mammal/livestock intermediate class. I could not verify a 2023 global FAOSTAT head-count for sheep or goats from an authoritative page, so **no population figure is asserted anywhere above** — FAO's own distribution pages give no total ([FAO Livestock Systems: goats](https://www.fao.org/livestock-systems/global-distributions/goats/en/), [sheep](https://www.fao.org/livestock-systems/global-distributions/sheep/en/)).

## 5. Synonyms and what NOT to conflate

**Names in real use for this concept**
- small ruminant (veterinary and FAO usage; the standard collective for sheep + goats)
- sheep and goats / ovine and caprine hosts
- caprine (goat-specific adjective), ovine (sheep-specific adjective)
- Caprinae; goat antelopes and relatives (broad-reading synonyms)
- sheep- and goat-associated environment (the ENVO-pattern name a term request would use)

**Commonly but wrongly treated as the same thing**
- **Defibrinated sheep blood / sheep blood agar.** A culture-medium reagent. A strain grown on sheep blood agar was not isolated from a sheep. This is the single most likely lexical trap in any text-mining pass over strain metadata.
- **Sheep- or goat-milk foods** — pecorino, sheep-milk cheese, goat cheese, kefir: FOODON classes for manufactured materials with their own microbiota, downstream of the host.
- **`FOODON:03411328` "goat" / `FOODON:03411183` "sheep"** — whole food-source organisms, dead or alive. Related, not identical; xref, not identity, and neither covers both species.
- **Rumen (UBERON/ENVO anatomy) and rumen fluid** — a *part* of the host, which grounds normally per this repo's rule; not the host.
- **Sheep/goat dung and manure as environmental material** — once excreted, the ENVO material terms apply; upstream tags this via `#Host body-product`, and the myxobacteria on this record probably straddle the line.
- **`Bovinae (Cow, Cattle)`** — sibling tag. "Ruminant" is not a synonym for "small ruminant".
- **Caseous lymphadenitis, enzootic abortion of ewes, contagious agalactia, Q fever** — disease states, not habitats. Correctly `NOT_APPLICABLE` if they appear as separate concepts.
- **Wild bighorn/Dall sheep and ibex** — inside the broad reading of Caprinae, outside "domestic livestock". Say which reading the definition takes rather than leaving it implicit.
- **"Sheep" in *Ovis aries* genome/host-genetics contexts** — the host organism as a study subject, not as a microbial habitat.

## 6. Should this be a term at all?

**Yes — and the current `CONFIRM_UNGROUNDED` + term-request disposition is right.** The concept names a place where microbes live (a host organism), which is exactly what ENVO models at `plant-associated environment` / `animal-associated environment` / `fungi-associated environment`, and ENVO has already minted at least one taxon-scoped child of it (`cnidarian-associated environment`). 412 strains is a large, real attestation volume, and no existing term in ENVO, UBERON, FOODON, BTO or PO names it. It is not a disease, a quality, a process, or a procedure, so `NOT_APPLICABLE` would be the wrong call — consistent with the #114 reversal recorded on the record.

Three things a curator should fix or decide while writing the definition:

1. **Add `FOODON:03411183` "sheep" as a second xref, and `NCBITaxon:9963` "Caprinae".** The record currently carries only `FOODON:03411328` "goat" — a medium-confidence lexical `skos:closeMatch` that names half the concept. Keeping only the goat xref makes the record look like it is *about* goats. All three are `relation: xref`, never `parent`, since a food-source-organism class and a taxon are not broader kinds of environment.
2. **`parent_habitats` should be `ENVO:01001002` *animal-associated environment*, not `FOODON:03411328`.** The curator note says the FOODON term was "attached as a parent" but the record has it under `xrefs` — the record is right and the note's wording is stale. "A whole goat" is not broader than "sheep-or-goat-associated environment"; `animal-associated environment` is.
3. **The record is `habitat_category: OTHER` and lives in `data/habitats/other/`, while its conceptual siblings (fish, mollusca, invertebrates, host-animal-endotherm) sit in `host_associated/`.** This is a seeder categorisation question, not a definition question, but it is the kind of split that made #114 possible in the first place — a host concept filed away from the other host concepts is one nobody compares against them. Worth a separate issue rather than a hand-edit.

**Suggested term-request label, if one is filed upstream:** *Caprinae-associated environment* (broad reading) or *sheep- or goat-associated environment* (narrow reading). Per the standing memory rule, any actual submission to ENVO needs explicit per-request permission first.

---

**Sources:**
[Reimer et al. 2019, BacDive, NAR](https://doi.org/10.1093/nar/gky879) · [BacDive isolation sources browser](https://bacdive.dsmz.de/isolation-sources) · [Schober et al. 2025, BacDive in 2025](https://doi.org/10.1093/nar/gkae959) · [ENVO:01001002 (OLS4)](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002) · [ENVO issue #1029](https://github.com/EnvironmentOntology/envo/issues/1029) · [FOODON:03411328 (OLS4)](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03411328) · [NCBITaxon:9963 (OLS4)](https://www.ebi.ac.uk/ols4/ontologies/ncbitaxon/classes?obo_id=NCBITaxon:9963) · [Wikipedia: Caprinae](https://en.wikipedia.org/wiki/Caprinae) · [Ultimate Ungulate: Caprinae](https://www.ultimateungulate.com/Artiodactyla/Caprinae.html) · [Encyclopedia.com: Bovids VI (Caprinae)](https://www.encyclopedia.com/environment/encyclopedias-almanacs-transcripts-and-maps/bovids-vi-sheep-goats-and-relatives-caprinae) · [Zeder 2008, PNAS](https://doi.org/10.1073/pnas.0801317105) · [Rumen microbiota review, PMC11117383](https://pmc.ncbi.nlm.nih.gov/articles/PMC11117383/) · [Henderson et al. 2015, Sci Rep](https://doi.org/10.1038/srep14567) · [Goats vs sheep rumen, PMC7070549](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7070549/) · [Tannin forage, J Anim Sci 2024](https://doi.org/10.1093/jas/skae198) · [Gut microbiota of ruminants, Animals 2025](https://www.mdpi.com/2076-2615/15/5/758) · [Merck Vet Manual: goat nutrition](https://www.merckvetmanual.com/management-and-nutrition/nutrition-goats/nutritional-requirements-of-goats) · [Bonga sheep vs Kaffa goats, PMC4710639](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4710639/) · [Kodjo et al. 1995, Moraxella caprae](https://doi.org/10.1099/00207713-45-3-467) · [Dorella et al. 2006, C. pseudotuberculosis](https://doi.org/10.1051/vetres:2005056) · [Ovine/caprine C. pseudotuberculosis, PMC11123211](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11123211/) · [Mycoplasma conjunctivae in small ruminants, PMC3883482](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3883482/) · [M. ovipneumoniae goat-to-bighorn, PMC5462392](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5462392/) · [Zoonotic abortifacients, PMC10422025](https://pmc.ncbi.nlm.nih.gov/articles/PMC10422025/) · [Listeria ivanovii in bulk-tank milk, PMC9220212](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9220212/) · [Zhang et al. 2003, myxobacteria isolation](https://doi.org/10.1016/S0167-7012(02)00257-9) · [Sharma et al. 2022, dung-pellet myxobacteria](https://doi.org/10.1002/jobm.202100518) · [FAO Livestock Systems: goats](https://www.fao.org/livestock-systems/global-distributions/goats/en/) · [FAO Livestock Systems: sheep](https://www.fao.org/livestock-systems/global-distributions/sheep/en/)

## Citations

1. https://doi.org/10.1093/nar/gky879
2. https://bacdive.dsmz.de/isolation-sources
3. https://www.ebi.ac.uk/ols4/ontologies/ncbitaxon/classes?obo_id=NCBITaxon:9963
4. https://en.wikipedia.org/wiki/Caprinae
5. https://www.ultimateungulate.com/Artiodactyla/Caprinae.html
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC3883482/
7. https://doi.org/10.1016/S0167-7012(02
8. https://doi.org/10.1002/jobm.202100518
9. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
10. http://purl.obolibrary.org/obo/ENVO_01001002
11. https://github.com/EnvironmentOntology/envo/issues/1029
12. https://docs.hpc.oregonstate.edu/cqls/tips/submitting-sra-data/
13. https://doi.org/10.1073/pnas.0801317105
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC11117383/
15. https://www.merckvetmanual.com/management-and-nutrition/nutrition-goats/nutritional-requirements-of-goats
16. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4710639/
17. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7070549/
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC11484804/
19. https://www.mdpi.com/2076-2615/15/5/758
20. https://doi.org/10.1038/srep14567
21. https://doi.org/10.1099/00207713-45-3-467
22. https://doi.org/10.1051/vetres:2005056
23. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11123211/
24. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3883482/
25. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5462392/
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC10422025/
27. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9220212/
28. https://doi.org/10.1093/nar/gkae959
29. https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03411328
30. https://www.encyclopedia.com/environment/encyclopedias-almanacs-transcripts-and-maps/bovids-vi-sheep-goats-and-relatives-caprinae
31. https://doi.org/10.1093/jas/skae198
32. https://www.fao.org/livestock-systems/global-distributions/goats/en/
33. https://www.fao.org/livestock-systems/global-distributions/sheep/en/