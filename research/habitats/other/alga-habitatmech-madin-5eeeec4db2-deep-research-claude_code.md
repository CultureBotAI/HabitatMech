---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T20:58:31.114824'
end_time: '2026-08-17T21:08:39.606142'
duration_seconds: 608.49
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: alga
  habitat_identifier: habitatmech:MADIN.5eeeec4db2
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'MADIN: alga'
  assertions: '88'
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
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:MADIN.5eeeec4db2)"
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
  web_search_requests: 19
  num_turns: 43
  total_cost_usd: 4.115184000000001
  session_id: 526d84e3-4db0-4b90-b2c7-11a81eb97492
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 25
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** alga
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:MADIN.5eeeec4db2
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** MADIN: alga
- **Upstream assertion volume:** 88
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:MADIN.5eeeec4db2)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **alga** as a microbial habitat, with citations.

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

# Research report — `alga` (habitatmech:MADIN.5eeeec4db2)

## Proposed definition

> An environmental system determined by an organism which is determined by an alga — an oxygenic photosynthetic organism outside the land plants — and which comprises the algal thallus or cell surface, its internal tissues, and the exudate-enriched water layer immediately surrounding it.

If that reads as two claims rather than one, the reason is structural, not stylistic: there is no intermediate class between ENVO's *environmental system determined by an organism* (ENVO:01001000) and this concept, because ENVO has plant-, animal-, fungi- and cnidarian-associated siblings but no algal one (see §2). The honest alternative is to request **`alga-associated environment`** as a direct child of ENVO:01001000, defined exactly as above, and let the surface/interior/phycosphere distinctions become its children.

**Recommended dispositions for the curator, up front:**

1. This **is** a habitat; the confirm-ungrounded decision already on the record is right, and the ENVO term the upstream mapping points at is *obsolete* (§2).
2. The record's `habitat_category: OTHER` **contradicts its own upstream source**, which files this category under `Host_associated` (§1). It should be `HOST_ASSOCIATED`, matching the GOLD `Algae` sibling.
3. This is a strong **`SAME_AS` candidate** for `habitatmech:GOLD.02383c20a7` ("Host-associated > Algae", 394 assertions), which is already `CONFIRM_UNGROUNDED` with the same reasoning — the merge mechanism added in #116 exists and is already used once (`habitatmech:BACDIVE.c9b246fcbb SAME_AS habitatmech:GOLD.cd0b0940e5`). Caveat in §6.

---

## 1. What the concept denotes

### The decisive evidence: the upstream mapping table

`alga` here is not a free-text isolation source. It is one of ~58 condensed habitat categories in the Madin *et al.* trait synthesis, and the mapping is explicit in that project's own conversion table:

| Main group | Type | ENVO_terms | ENVO_ids |
|---|---|---|---|
| `Host_associated` | `host_algae` | `alga` | `ENVO:02500019` |

— [`data/conversion_tables/environments.csv`](https://raw.githubusercontent.com/bacteria-archaea-traits/bacteria-archaea-traits/master/data/conversion_tables/environments.csv), bacteria-archaea-traits (Madin *et al.* 2020). This is the file HabitatMech's own `data/raw/MANIFEST.yaml` records as an input, and `data/raw/environment_parameters.tsv:326–333` carries its eight environmental axes for this exact category.

The companion file [`renaming_isolation_source.csv`](https://raw.githubusercontent.com/bacteria-archaea-traits/bacteria-archaea-traits/master/data/conversion_tables/renaming_isolation_source.csv) shows which raw strings were folded into `host_algae`. Verbatim, they include:

- **Macroalgae / seaweed:** `other, seaweed`, `other, isolated from seaweed`, `other, seaweed epiphyte`, `other, marine alga`, `other, marine algae`, `other, red alga`, `other, isolated from red alga`, `other, isolated from marine red alga`, `other, thalli of a marine red alga`, `other, red alga porphyra yezoensis`, `other, green alga`, `other, green algae`, `other, green alga from antarctic`, `other, brown alga`, `other, rhizosphere of brown alga`
- **Microalgae / phytoplankton / protists:** `other, marine phytoplankton`, `other, dinoflagellate`, `other, marine dinoflagellate`, `host-associated, microbial, dinoflagellates`, `other, marine alga phaeocystis globosa`, `other, lab culture of marine dinoflagellate`
- **Phycosphere proper:** `algal phycosphere`, `chrysochromulina tobin phycosphere`
- **Generic host-associated:** `host-associated, algae`, `host-associated, algae, free living`, `plant associated, algae`, `other, isolated from algae`
- **Boundary cases folded in (see below):** `other, algal mat`, `other, decomposing algal scum`, `other, lichen-colonized rock surface`

So the concept denotes: **the living body of an alga — of any lineage, macroscopic or unicellular, marine or freshwater, in the field or in laboratory culture — together with the thin layer of water and exudate around it, considered as the place a microorganism was sampled from.**

### What is inside the boundary

- The **thallus surface / epiphytic film** of a macroalga. This is the single most common reading in the data: *Epibacterium ulvae* U95ᵀ was isolated from the *surface* of *Ulva australis* ([IJSEM 2013, doi:10.1099/ijs.0.042838-0](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.042838-0), PMID 22904216) and *Polaribacter porphyrae* LNM-20ᵀ from *thalli* of the red alga *Porphyra yezoensis* ([IJSEM 2013, doi:10.1099/ijs.0.041434-0](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.041434-0), PMID 22904227).
- The **whole macroalgal body** where the description does not resolve a part — *Kiloniella laminariae* LD81ᵀ "from the marine macroalga *Laminaria saccharina*" ([IJSEM 2009, doi:10.1099/ijs.0.001651-0](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.001651-0)); *Phycisphaera mikurensis* FYK2301M01ᵀ "isolated from a marine alga" ([J Gen Appl Microbiol 2009; 55:267–275](https://pubmed.ncbi.nlm.nih.gov/19700920/)); *Algimonas porphyrae* from *P. yezoensis* ([PMID 22427444](https://pubmed.ncbi.nlm.nih.gov/22427444/)).
- The **holdfast/basal region** — the raw string `other, rhizosphere of brown alga` is explicitly in the category.
- The **phycosphere of a unicellular alga**, including in laboratory coculture. *Acidovorax* sp. RAC01, *Sinorhizobium* sp. RAC02, *Blastomonas* sp. RAC04 and *Agrobacterium* sp. RAC06 — four of the 25 exemplar taxa on this record — are from bacteria found in coculture with the **haptophyte** *Chrysochromulina tobin* ([Genome Announc. 2016, doi:10.1128/genomeA.01162-16](https://journals.asm.org/doi/10.1128/genomea.01162-16)).

### What is a neighbouring concept (and is nonetheless folded in upstream)

Three raw strings sit outside a strict reading and are worth naming in the record's note, because they are the reason a purist definition and the actual attestations do not perfectly coincide:

- `other, algal mat` — a **microbial mat** is a laminated community/feature (ENVO:01000008, "A multi-layered sheet of micro-organisms, mainly bacteria and archaea"), not an individual host organism.
- `other, decomposing algal scum` — decaying algal biomass is **algal material** (ENVO:01001189, "An organic material which is primarily composed of living or dead algae, along with their exudates"), an environmental *material*, not an organism-determined system.
- `other, lichen-colonized rock surface` — a lichen is a fungus–photobiont composite on rock; HabitatMech already treats lichen as its own concept (`habitatmech:GOLD.5e1a5d695c`, `CONFIRM_UNGROUNDED` against FOODON:03412345).

*This paragraph is my reading of the mapping table against the ENVO definitions quoted; no source states that Madin et al. mis-binned these.*

### Ambiguity: which readings the label carries

The label `alga` is genuinely ambiguous in three ways, and the source data does not resolve all three:

1. **Organism vs. environment.** As written, `alga` names an organism. As used — a `Host_associated / host_algae` isolation category — it names a place. The environment reading is the one the data means; that is exactly the distinction #114/#99 encode.
2. **Which organisms count as "algae".** "Alga" is not a clade. The attested strings span Rhodophyta (red), Phaeophyceae (brown), Chlorophyta (green), Bacillariophyta/other stramenopiles, Haptophyta (*Chrysochromulina*, *Phaeocystis*) and Dinophyceae. Whether **cyanobacteria** ("blue-green algae") are inside is unresolved: three of the 25 exemplar taxa are cyanobacteria (*Geitlerinema* sp. ATCC 29120, *Calothrix* sp. PCC 6303, *Geminocystis herdmanii* PCC 6308). *I could not determine from the sources why those three carry this category; the plausible routes are the historical "blue-green algae" usage or an `algal mat` isolation string. Treat this as unverified.*
3. **Field host vs. laboratory culture.** `other, lab culture of marine dinoflagellate` and the *C. tobin* phycosphere strains are xenic culture collections, not field samples. HabitatMech elsewhere routes "algal culture" GOLD paths to BTO:0000316 *culture medium* (`habitatmech:GOLD.5b8e5eddd2`). Both readings are inside this one MADIN category.

### One clear data-quality artefact

*Streptococcus pyogenes* (NCBITaxon:1314) appears among the 25 exemplars. There is no plausible sense in which the type material of *S. pyogenes* is algal. Flagging it as an upstream mis-assignment is safer than treating it as evidence about the habitat. *(My assessment; no source asserts this.)* Note also that the 25 `characteristic_taxa` are a sample of `candidate_pool: 88`; the 88 is the taxon count from `madin_habitats.tsv`.

---

## 2. Genus — the broader kind

### The genus to use

**ENVO:01001000 — *environmental system determined by an organism***
Definition: "An environmental system which is determined by a living organism." Exact synonym: *host-associated environment*. Parent: ENVO:01000254 *environmental system*.
Source: [OLS4 / ENVO](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000).

This is the right genus and it is already the genus the corpus used for the GOLD `Algae` sibling. Its existing children establish the pattern this concept should join:

| CURIE | Label | Definition |
|---|---|---|
| ENVO:01001001 | plant-associated environment | "An environmental system determined by a green plant." |
| ENVO:01001002 | animal-associated environment | "An environmental system determined by an animal." |
| ENVO:01001041 | fungi-associated environment | "An environmental system determined by a fungal structure." |
| ENVO:01001179 | cnidarian-associated environment | "An environmental system determined by a cnidarian or part of a cnidarian." |
| ENVO:01001176 | environment associated with an aquatic invertebrate | environmental system shaped by an aquatic invertebrate |

I enumerated all 30 descendants of ENVO:01001000 via OLS4: **there is no alga-, algal- or seaweed-related class among them.**

### Near-misses and why each fails

**ENVO:02500019 `alga` — the term upstream actually points at. It is obsolete.**
OLS4 returns label `obsolete alga`, `is_obsolete: true`, `term_replaced_by: null`. The trail is fully documented in ENVO's tracker:
- [Issue #1246, "obsolete: alga"](https://github.com/EnvironmentOntology/envo/issues/1246) (cmungall, 19 Nov 2021) — the class is confusing because one would expect subtypes and it has no subclasses; suggests either moving it to PCO or building "the correct union definition" kept in sync with NCBITaxon releases.
- [Issue #1448](https://github.com/EnvironmentOntology/envo/issues/1448) and [PR #1450](https://github.com/EnvironmentOntology/envo/pull/1450), "Proposal: obsolete 'alga'" (7 Sep 2023; PR merged 26 Sep 2023) — "obsolete ENVO:02500019".
- [Issue #1481](https://github.com/EnvironmentOntology/envo/issues/1481) (Jan 2024) — cleanup of references to `obsolete alga` from the algal-bloom axioms.

This matters twice over: it confirms the concept has no ENVO home, **and** it means the upstream `source_id` on this record is a deprecated IRI. It was also an *organism* class, so it would fail the corpus's organism-identity screen even if it were live. My recommendation is to record this in the note rather than attach it as an `xref` — xrefing an obsoleted-without-replacement term publishes a dead link. *(Judgment call; the repo has no stated policy on obsolete xref targets that I found.)*

**ENVO:01001001 `plant-associated environment` — the most seductive near-miss, and a partial overlap.**
Its equivalent-class axiom is `environmental system` **and** `determined by` some **NCBITaxon:33090 (Viridiplantae)**, with exact synonym "Viridiplantae-associated environment" (OLS4). Because Chlorophyta sit inside Viridiplantae, a *green*-alga-associated environment is logically already a `plant-associated environment`. But red algae, brown algae, diatoms, haptophytes and dinoflagellates are not Viridiplantae, so this term covers perhaps a quarter of the attested strings and misclassifies the rest. Grounding here would assert green-plant-hood of *Laminaria* and *Porphyra*. **Not a match; a genuine partial overlap worth recording in the note.**

**ENVO:01001189 `algal material` — right subject, wrong kind.** "An organic material which is primarily composed of living or dead algae, along with their exudates." This is an `organic material` (child of ENVO:01000155), not an environmental system. It fits drift wrack and `decomposing algal scum`; it does not fit "isolated from the surface of a living *Ulva*". Its editor note says it awaits further axiomatisation "with 'alga' once semantic ambiguities are resolved with PCO" — i.e. ENVO itself has parked the algal modelling problem. **Near-miss on kind.**

**ENVO:2000004 `algal bloom` / ENVO:01000057 `marine algal bloom` / ENVO:2000005 `freshwater algal bloom`** — features of a *water body* arising from algal proliferation. Narrower and different: a bloom is a population event in the water column, not the individual alga as host.

**ENVO:02500018 `algal bloom process`, ENVO:02500021 `algal bloom collapse`, ENVO:02500023 `algal production`** — processes, not places. Automatically `NOT_APPLICABLE`-shaped.

**ENVO:01000008 `microbial mat`** — a real habitat and already used 18× in `curation/decisions.tsv`, but it names a laminated multi-species community, not an alga acting as host. It would fit only the `algal mat` strings.

**FOODON:03411301 `algae`, FOODON:03412266 `seaweed`, FOODON:03412395 `brown algae`, FOODON:03412502 `green algae`, FOODON:03411743 `red algae`** — the corpus has already ruled on all five: they are organism/food-organism terms, and every one is recorded `CONFIRM_UNGROUNDED` with the FOODON term kept as an `xref`. The same reasoning applies unchanged here.

**NCBITaxon** — there is no `algae` node to xref; the group is polyphyletic. The only phycosphere-adjacent NCBITaxon class is **NCBITaxon:2011160 `phycosphere metagenome`**, which names a sequence-data category, not a place. **No OBO ontology defines a class `phycosphere`** (OLS4, all ontologies).

---

## 3. Differentia — what distinguishes it

Against its siblings under ENVO:01001000 (plant-, animal-, fungi-, cnidarian-associated), the differentiating properties are:

**a) The determining organism is an oxygenic photosynthetic non-embryophyte.** It is defined by function and grade, not by clade — algae are polyphyletic, which is precisely why ENVO could not give the class subclasses and obsoleted it (issue #1246). Any definition that names a taxon here will be wrong; the differentia must be "photosynthetic, thallus- or single-cell-bodied, outside the land plants."

**b) The habitat is a photosynthate-fuelled interface, not a digestive or immune interior.** This is the property that most sharply separates it from *animal-associated environment*. The classic statement is Bell & Mitchell's coinage of the **phycosphere**: "a region extending outward from an algal cell or colony for an undefined distance, in which bacterial growth is stimulated by extracellular products of the alga" ([Biol. Bull. 143:265–277, 1972, doi:10.2307/1540052](https://www.journals.uchicago.edu/doi/10.2307/1540052); full text at [BioStor](https://biostor.org/reference/9075)). Seymour *et al.* describe it as "the planktonic analogue of the plant rhizosphere," a microscale zone where metabolite and infochemical exchange governs mutualism through parasitism ([Nat. Microbiol. 2:17065, 30 May 2017, doi:10.1038/nmicrobiol.2017.65](https://www.nature.com/articles/nmicrobiol201765)).

**c) It is predominantly aquatic and permanently wet, in contrast to the plant-associated phyllosphere.** Supported by the upstream axis annotations for this exact category (`data/raw/environment_parameters.tsv:326–333`, derived from `environments.csv` and the habitat scheme of [Cobo-Simón & Tamames, *BMC Genomics* 18:499, 2017, doi:10.1186/s12864-017-3888-y](https://doi.org/10.1186/s12864-017-3888-y)):

| Parameter | Value |
|---|---|
| Water | high |
| water variability | permanently wet |
| Nutrients | high |
| Organic | high |
| Structural | high |
| Gradients | high |
| Pressure | low |
| temp variability | low |

These are curator-assigned axis labels in the upstream table, not measurements — cite them as such.

**d) Colonisation is dense, surface-attached and spatially structured.** Epibacterial densities on macroalgal surfaces run **10²–10⁷ cells cm⁻²**, varying with algal species, thallus section and season; on *Ulva australis* density rises an order of magnitude from tips (10⁶ cells cm⁻²) to base (10⁷ cells cm⁻²) ([Egan *et al.*, *FEMS Microbiol. Rev.* 37:462–476, 2013, doi:10.1111/1574-6976.12011](https://academic.oup.com/femsre/article/37/3/462/585525), PMID 23157386, citing Armstrong *et al.* 2000 and Bengtsson *et al.* 2010).

**e) The association is functionally obligate in both directions, i.e. a holobiont.** Egan *et al.* argue macroalgae and their epiphytic bacteria "interact as a unified functional entity, or holobiont, analogous to … corals" (2013, as above). Concretely, several macroalgae fail to develop normal morphology axenically; *Hyphomonas* strains restore normal morphogenesis in *Pyropia yezoensis* protoplasts ([*Microb. Ecol.* 2014, doi:10.1007/s00248-014-0423-4](https://link.springer.com/article/10.1007/s00248-014-0423-4)). The broader interaction spectrum, from mutualism to parasitism, is reviewed by [Ramanan *et al.*, *Biotechnol. Adv.* 34:14–29, 2016, doi:10.1016/j.biotechadv.2015.12.003](https://www.sciencedirect.com/science/article/pii/S0734975015300586) (PMID 26657897).

**f) Taxonomic signature of the residents.** The exemplar list is dominated by Flavobacteriia (*Polaribacter*, *Maribacter*, *Tenacibaculum*, *Aquimarina*, *Arenibacter*) and Roseobacter-group Alphaproteobacteria (*Epibacterium*, *Roseobacter*, *Erythrobacter*, *Algimonas*, *Kiloniella*), plus polysaccharide-degrading Gammaproteobacteria (*Microbulbifer*, *Pseudoalteromonas*, *Aquimarina agarilytica*) — consistent with a habitat whose dominant carbon source is sulfated and structural algal polysaccharide. *The pattern is directly observable in the record's `characteristic_taxa`; the causal reading of it is my inference, though the algae–Roseobacter association is described as "a classic case" by Ramanan et al. 2016.*

---

## 4. Sources

Ontology and vocabulary:
- ENVO:01001000, 01001001, 01001002, 01001041, 01001176, 01001179, 01001189, 01000008, 2000004, 01000057 — [EBI OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo), queried 17 Aug 2026.
- ENVO:02500019 obsoletion — [issue #1246](https://github.com/EnvironmentOntology/envo/issues/1246) (19 Nov 2021), [issue #1448](https://github.com/EnvironmentOntology/envo/issues/1448) + [PR #1450](https://github.com/EnvironmentOntology/envo/pull/1450) (Sep 2023), [issue #1481](https://github.com/EnvironmentOntology/envo/issues/1481) (Jan 2024).
- Buttigieg P.L. *et al.* "The environment ontology: contextualising biological and biomedical entities." *J. Biomed. Semantics* 4:43 (2013). [doi:10.1186/2041-1480-4-43](https://doi.org/10.1186/2041-1480-4-43), PMC3904460.

Upstream source (MADIN):
- Madin J.S. *et al.* "A synthesis of bacterial and archaeal phenotypic trait data." *Sci. Data* 7:170 (5 Jun 2020). [doi:10.1038/s41597-020-0497-4](https://www.nature.com/articles/s41597-020-0497-4), PMC7275036.
- `environments.csv` and `renaming_isolation_source.csv`, [bacteria-archaea-traits](https://github.com/bacteria-archaea-traits/bacteria-archaea-traits) v1.0.0.
- Cobo-Simón M. & Tamames J. *BMC Genomics* 18:499 (2017). [doi:10.1186/s12864-017-3888-y](https://doi.org/10.1186/s12864-017-3888-y), PMC5492924.

Habitat biology:
- Bell W. & Mitchell R. *Biol. Bull.* 143:265–277 (1972). [doi:10.2307/1540052](https://www.journals.uchicago.edu/doi/10.2307/1540052).
- Seymour J.R., Amin S.A., Raina J.-B., Stocker R. *Nat. Microbiol.* 2:17065 (2017). [doi:10.1038/nmicrobiol.2017.65](https://www.nature.com/articles/nmicrobiol201765).
- Egan S., Harder T., Burke C., Steinberg P., Kjelleberg S., Thomas T. *FEMS Microbiol. Rev.* 37:462–476 (2013). [doi:10.1111/1574-6976.12011](https://academic.oup.com/femsre/article/37/3/462/585525), PMID 23157386.
- Ramanan R. *et al.* *Biotechnol. Adv.* 34:14–29 (2016). [doi:10.1016/j.biotechadv.2015.12.003](https://www.sciencedirect.com/science/article/pii/S0734975015300586), PMID 26657897.
- Saha M. *et al.* "Progress and future directions for seaweed holobiont research." *New Phytol.* (2024). [doi:10.1111/nph.20018](https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.20018) — recent synthesis, useful if a 2024 anchor is wanted.

Type-strain isolation sources cited above:
- *Kiloniella laminariae*: Wiese J. *et al.* *IJSEM* 59:350–356 (2009). [doi:10.1099/ijs.0.001651-0](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.001651-0).
- *Epibacterium ulvae*: Penesyan A. *et al.* *IJSEM* (2013). [doi:10.1099/ijs.0.042838-0](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.042838-0), PMID 22904216.
- *Polaribacter porphyrae*: Fukui Y. *et al.* *IJSEM* 63:1665–1672 (2013). [doi:10.1099/ijs.0.041434-0](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.041434-0), PMID 22904227.
- *Algimonas porphyrae*: [PMID 22427444](https://pubmed.ncbi.nlm.nih.gov/22427444/).
- *Phycisphaera mikurensis*: Fukunaga Y. *et al.* *J. Gen. Appl. Microbiol.* 55:267–275 (2009). [PMID 19700920](https://pubmed.ncbi.nlm.nih.gov/19700920/). (Note: BacDive records the host as *Porphyra* sp.; the paper title says only "a marine alga" — do not quote a specific host genus without checking the paper.)
- RAC01/02/04/06: "Genome Sequences of Eight Bacterial Species Found in Coculture with the Haptophyte *Chrysochromulina tobin*." *Genome Announc.* (2016). [doi:10.1128/genomeA.01162-16](https://journals.asm.org/doi/10.1128/genomea.01162-16).

**Explicitly my inference, not sourced:** the boundary analysis in §1 (that `algal mat`, `decomposing algal scum` and `lichen-colonized rock surface` are neighbouring rather than inside concepts); the assessment that *S. pyogenes* is a mis-assignment; the polysaccharide-degradation reading of the resident taxa; and the recommendation not to xref an obsoleted term.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- *alga-associated environment* / *algae-associated environment* (constructed on ENVO's own naming pattern; **not currently an ENVO label**)
- *host_algae* (the upstream MADIN category name)
- *algal microbiome habitat*, *algal surface*, *algal epibiota / epiphytic habitat*
- *phycosphere* — in wide use, but **narrower**: strictly the exudate-enriched diffusive zone around a cell or colony (Bell & Mitchell 1972; Seymour *et al.* 2017), not the thallus interior or a whole seaweed
- *seaweed holobiont*, *macroalgal surface* — **narrower**: macroalgae only (Egan *et al.* 2013)
- *epiphytic bacterial community habitat* (used descriptively across the seaweed literature)

**Do not conflate with**
| Confusable | Why it is different |
|---|---|
| ENVO:02500019 `alga` | **Obsolete since Sept 2023**, no replacement; and it named the organism, not a place |
| FOODON:03411301 `algae`, FOODON:03412266 `seaweed`, and the colour-group FOODON terms | Organism/food terms. Already ruled on in `curation/decisions.tsv`; keep as `xref`, never as identity or `parent_habitats` |
| ENVO:01001189 `algal material` | An environmental *material* (living or dead algal biomass + exudates) — right subject, wrong kind |
| ENVO:2000004 / 01000057 / 2000005 `algal bloom` family | Features of a water body; a bloom is a population event, not the individual host |
| ENVO:02500018/21/23 bloom *processes* | Processes; `NOT_APPLICABLE`-shaped |
| ENVO:01000008 `microbial mat` | A laminated multi-species community, not an alga acting as host |
| ENVO:01001001 `plant-associated environment` | Axiomatised on NCBITaxon:33090 Viridiplantae — covers green algae only; asserts green-plant-hood of red/brown algae |
| Cyanobacteria / "blue-green algae" | Bacteria, not algae under modern usage; if a cyanobacterium is the host, that is a different host kind |
| Lichen | A fungal–photobiont composite; already its own HabitatMech concept |
| BTO:0000316 `culture medium` | The *medium* an alga is grown in; distinct from the alga as host, though MADIN folds some lab-culture strings into this category |
| NCBITaxon:2011160 `phycosphere metagenome` | A sequence-data category, not a place |
| Surrounding seawater / bacterioplankton | Compositionally distinct from the algal surface community (Egan *et al.* 2013) |

---

## 6. Should it be a term at all?

**Yes.** It is a place where microorganisms live — an organism acting as host — and it is exactly the case ENVO already models for plants, animals, fungi and cnidarians but has left unmodelled for algae. Three independent lines support keeping it and requesting a term:

1. **The upstream source itself classifies it as host-associated** (`Main group = Host_associated`, `Type = host_algae`). The record's `habitat_category: OTHER` is not what the source says.
2. **ENVO has no term and knows it.** The one candidate was obsoleted with no replacement, and ENVO's own issue #1246 identifies the union-definition-over-NCBITaxon approach as the fix — which is exactly the axiomatisation an `alga-associated environment` request should propose (union over Rhodophyta, Chlorophyta, Phaeophyceae, Bacillariophyta, Haptophyta, Cryptophyta, Dinophyceae, Euglenophyta).
3. **The habitat has a distinct, measurable microbiota**, 10²–10⁷ cells cm⁻², compositionally distinct from surrounding seawater, with documented functional dependence in both directions (Egan *et al.* 2013; Seymour *et al.* 2017).

**On the `SAME_AS` recommendation, with its caveat.** MADIN `alga` and GOLD `Host-associated > Algae` (`habitatmech:GOLD.02383c20a7`, 394 assertions) denote the same thing — an alga acting as host — and both are novel, so there is no ontology term to merge on: the #116 mechanism applies. The caveat is asymmetry of structure. GOLD's `Algae` is a *parent node* with curated children (green, red, brown, golden, yellow-green, microalgae, mixed algae turf, seaweed), each already a separate HabitatMech record; MADIN's `alga` is a single **flat** category that additionally sweeps in dinoflagellates, phytoplankton, algal mats and lab cocultures. Merging is still right — the GOLD parent node covers the same breadth, and its children remain children — but the merged record's note should say that MADIN's attestations are unresolved as to algal lineage and include laboratory-culture isolates, so they cannot be pushed down to any child.

**Also worth noting on the record:** eight environmental-parameter rows for `ENVO:02500019 / host_algae` exist in `data/raw/environment_parameters.tsv` (lines 326–333) but do not appear on `data/habitats/other/alga.yaml`. Whether that is the deliberate skip rule or a gap is a seeder question, not a definition question — but the values are the best available support for differentia (c) above, so it is worth resolving before writing the definition from them.

## Citations

1. https://raw.githubusercontent.com/bacteria-archaea-traits/bacteria-archaea-traits/master/data/conversion_tables/environments.csv
2. https://raw.githubusercontent.com/bacteria-archaea-traits/bacteria-archaea-traits/master/data/conversion_tables/renaming_isolation_source.csv
3. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.042838-0
4. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.041434-0
5. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.001651-0
6. https://pubmed.ncbi.nlm.nih.gov/19700920/
7. https://pubmed.ncbi.nlm.nih.gov/22427444/
8. https://journals.asm.org/doi/10.1128/genomea.01162-16
9. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000
10. https://github.com/EnvironmentOntology/envo/issues/1246
11. https://github.com/EnvironmentOntology/envo/issues/1448
12. https://github.com/EnvironmentOntology/envo/pull/1450
13. https://github.com/EnvironmentOntology/envo/issues/1481
14. https://www.journals.uchicago.edu/doi/10.2307/1540052
15. https://biostor.org/reference/9075
16. https://www.nature.com/articles/nmicrobiol201765
17. https://doi.org/10.1186/s12864-017-3888-y
18. https://academic.oup.com/femsre/article/37/3/462/585525
19. https://link.springer.com/article/10.1007/s00248-014-0423-4
20. https://www.sciencedirect.com/science/article/pii/S0734975015300586
21. https://www.ebi.ac.uk/ols4/ontologies/envo
22. https://doi.org/10.1186/2041-1480-4-43
23. https://www.nature.com/articles/s41597-020-0497-4
24. https://github.com/bacteria-archaea-traits/bacteria-archaea-traits
25. https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.20018