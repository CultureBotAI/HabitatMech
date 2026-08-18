---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:27:26.969100'
end_time: '2026-08-17T16:36:44.048941'
duration_seconds: 557.08
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Fungi
  habitat_identifier: habitatmech:GOLD.a8fc5001d1
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Fungi'
  assertions: '635'
  parent_terms: ENVO:01001000
  xrefs: FOODON:03411261
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term FOODON:03411261 'fungus' attached as a parent. Host-taxon reversal\
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
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.a8fc5001d1)"
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
  num_turns: 35
  total_cost_usd: 3.958212999999999
  session_id: eed40efc-13a9-4e2f-a0a4-b78c4b653222
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 24
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Fungi
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.a8fc5001d1
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Fungi
- **Upstream assertion volume:** 635
- **Nearest broader term already on the record:** ENVO:01001000
- **Cross-references upstream suggested:** FOODON:03411261

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term FOODON:03411261 'fungus' attached as a parent. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.a8fc5001d1)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Fungi** as a microbial habitat, with citations.

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

# Research report — `habitatmech:GOLD.a8fc5001d1` "Fungi" (GOLD `Host-associated > Fungi`)

> **A fungi-associated environment (`ENVO:01001041`) — i.e. an environmental system determined by an organism (`ENVO:01001000`) which is determined by a fungus — comprising the surfaces, internal tissues, intracellular compartments and adherent water films of a living or dead fungal thallus at any structure or life stage, sampled as the habitat of the microorganisms living in or on it.**

**Headline finding, stated up front: this concept is already named, and the term is already in HabitatMech's vendored slice.** The premise of the research brief — "HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO names the concept. This one is unnamed" — does not hold. `ENVO:01001041` **fungi-associated environment** exists, is an exact fit, and is *already the identifier of another record in this corpus* (`data/habitats/other/fungi_associated_environment.yaml`, `grounding_status: EXACT`, `mapping_status: REVIEWED`). The correct disposition is almost certainly **`GROUND` to `ENVO:01001041`**, which merges `GOLD.a8fc5001d1` into that existing record — not a term request and not `CONFIRM_UNGROUNDED`.

The rest of this report supports that conclusion, records the near-misses, and supplies the differentia material a curator would need either way.

---

## 1. What the concept denotes

### The reading the data means

`Host-associated > Fungi` is a GOLD **Ecosystem Category** — level 2 of GOLD's five-level path (Ecosystem → Ecosystem Category → Ecosystem Type → Ecosystem Subtype → Specific Ecosystem). Level 1 `Host-associated` means the sample was *collected from another organism*; for host-associated samples the Ecosystem Category slot holds the host — an individual host or a phylum-level host group ([JGI GOLD, Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)).

So the concept denotes **a fungus in its role as the place a microorganism was sampled from**. The sampled entity is the microbe; the fungus is the environment. This is the same construction as `Host-associated > Plants` or `Host-associated > Arthropoda`.

The 635 assertions on this node are `assertion_unit: ORGANISM` and sit on the **bare two-level path** — i.e. 635 GOLD organisms whose recorded ecosystem is "a fungal host, structure unspecified". They are not a roll-up of the children; the children carry their own counts (verified in `data/raw/gold_ecosystem_paths.tsv`, columns `organism_count` / `total_assertions`):

| GOLD path | depth | assertions |
|---|---|---|
| `Host-associated > Fungi` | 2 | **635** |
| `Host-associated > Fungi > Mycelium` | 3 | 260 |
| `Host-associated > Fungi > Fruiting body` | 3 | 140 |
| `Host-associated > Fungi > Spore` | 3 | 135 |
| `Host-associated > Fungi > Lichen` | 3 | 66 |
| `Host-associated > Fungi > Fruiting body > Inner tissue` | 4 | 63 |
| `… > Appressorium`, `> Germ tube`, `> Mycorrhiza`, `> Sclerotium`, `> Stroma` | 3 | 0 each |

That child list is the strongest available evidence of the intended extension: the concept ranges over **vegetative mycelium, reproductive structures (fruiting body, spore, sporocarp interior), infection structures (appressorium, germ tube), survival structures (sclerotium, stroma), symbiotic organs (mycorrhiza), and the lichen thallus** — vegetative and reproductive, living and senescent, surface and interior. It is the fungal *organism* as habitat, not any one fungal organ.

### Boundary — what is inside and what is a neighbour

**Inside:**
- The hyphal surface and its adherent water film, where bacteria attach and move (see §3).
- The internal tissue of fungal structures — GOLD's own `Fruiting body > Inner tissue` (63 assertions).
- The fungal cytoplasm, i.e. endohyphal/endofungal bacteria. HabitatMech's own record `habitatmech:GOLD.1ab59245f7` covers the *separate* GOLD path `Host-associated > Endosymbionts > Fungi` (0 assertions), so the corpus currently splits endosymbiont-of-fungus from fungus-as-host. That split is a GOLD path artefact, not a biological boundary — the literature treats endohyphal bacteria as one end of a continuum with surface colonists ([Deveau et al. 2018, FEMS Microbiol Rev 42:335–352, doi:10.1093/femsre/fuy008](https://doi.org/10.1093/femsre/fuy008)).
- The lichen thallus, which GOLD places here. Biologically defensible: the lichen is a fungus-structured composite, and its bacterial microbiome is thallus-associated ([Grube et al. 2015, ISME J 9:412–424, doi:10.1038/ismej.2014.138](https://doi.org/10.1038/ismej.2014.138)).

**Neighbouring concepts, outside:**
- **Mycosphere / hyphosphere soil** — the *soil* zone influenced by hyphae. GOLD's `Host-associated` root means "sampled from the organism"; soil around hyphae is `Environmental > Terrestrial > Soil`. *This boundary call is my inference from GOLD's level-1 definition, not something a source states about this path.* The distinction matters because much of the bacterial-fungal-interaction literature samples the mycosphere rather than the fungus.
- **Fungal culture medium** — `Engineered > Lab culture > Culture media > Fungi`, already a separate record (`habitatmech:GOLD.55a9660503`, `NARROW` onto `BTO:0000316`).
- **The mycobiome** — the fungal community *inside another host*. Directionally the reverse of this concept (see §5).
- **Fungi as a taxonomic group** — `FOODON:03411261` 'fungus' is "a member of the group of eukaryotic organisms in the kingdom Fungi…" (verified in the vendored slice). That is a class of organisms, not a place; it correctly sits in `xrefs` on the record.

### Is the label ambiguous?

The bare string "Fungi" is ambiguous across at least five readings — host-as-habitat; the sampled fungal community (mycobiome); the taxon; fungal culture medium; fungal food material. **The path disambiguates it completely**: `Host-associated > …` fixes reading 1. No silent choice is needed.

---

## 2. Genus — the broader kind

### The match (not a near-miss)

**`ENVO:01001041` — "fungi-associated environment"**
- Definition: *"An environmental system determined by a fungal structure."*
- Exact synonyms: `fungus environment`, `fungus-associated environment`
- Alternative label: **`Fungus`** — this is the EMPO (Earth Microbiome Project Ontology) host-taxon value, which is how a GOLD-style category label ended up on the term.
- Parents (from the vendored `ontology_subclass_edges.tsv`): `ENVO:01001000` *environmental system determined by an organism* (exact synonym: `host-associated environment`) and `ENVO:2100000` *anatomical entity environment*.
- **Present in `data/raw/ontology_terms.tsv` with exactly that label**, so a `GROUND` decision passes the seeder's term-exists-and-label-matches gate with no vendoring work.
- Sources: [OLS4 `ENVO:01001041`](https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001041); ENVO overall — [Buttigieg et al. 2013, J Biomed Semantics 4:43, doi:10.1186/2041-1480-4-43](https://doi.org/10.1186/2041-1480-4-43) and [Buttigieg et al. 2016, J Biomed Semantics 7:57, doi:10.1186/s13326-016-0097-6](https://doi.org/10.1186/s13326-016-0097-6). EMPO's host-taxon level (Animal / Plant / **Fungus**) — [EMP Ontology](https://earthmicrobiome.org/protocols-and-standards/empo/); [Thompson et al. 2017, *Nature* 551:457–463, doi:10.1038/nature24621](https://doi.org/10.1038/nature24621); [Shaffer et al. 2022, *Nat Microbiol* 7:2128–2150, doi:10.1038/s41564-022-01266-x](https://doi.org/10.1038/s41564-022-01266-x).

`ENVO:01001041` is the **exact structural analogue** of terms HabitatMech already uses for the sibling GOLD categories: `ENVO:01001001` *plant-associated environment* ("An environmental system determined by a green plant") and `ENVO:01001002` *animal-associated environment* ("An environmental system determined by an animal"). The curator's own note names all three — "ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment" — and then concludes UNGROUNDED anyway. That is the defect in the decision.

**One wrinkle worth recording:** ENVO's text for the fungal member says *"determined by a fungal **structure**"* where its plant and animal siblings say "determined by a green plant" / "determined by an animal". The `structure` wording is an ENVO editorial inconsistency, not a narrower scope — the term's alt-label `Fungus` and its placement as the fungal peer of the plant/animal terms both point at whole-organism scope. It does not block grounding; it is worth noting to ENVO if and when the project has reason to raise it.

### Genus if a curator instead writes a definition

If for some reason `ENVO:01001041` is rejected, the genus to start from is **`ENVO:01001000` *environmental system determined by an organism*** — already the record's `parent_habitats` value, and the direct parent of all three of ENVO's host-kingdom terms.

### Near-misses, and why each fails

Checked against the vendored slice (ENVO, BTO, FOODON, PO, UBERON):

| Term | Label / definition | Why it is not the match |
|---|---|---|
| `ENVO:01001058` | *environment associated with a fungal tissue* — "An environmental system determined by **part** of a living or dead fungus." Alt label `Fungus corpus` (EMPO). | **Narrower**: a part, not the organism. Note it is *not* a subclass of `ENVO:01001041` in the slice — both hang off `ENVO:2100000`, so ENVO's fungal branch is flat. This is the right target for `Fruiting body > Inner tissue`, not for the category. |
| `ENVO:01001035` | *environment determined by a biofilm on a fungal surface* | **Narrower** and asserts a biofilm the GOLD attestations do not claim. |
| `ENVO:01000929` | *mushroom environment* (no definition text) | **Narrower** — basidiocarps only; excludes mycelium, spores, lichen, which are the bulk of the children. |
| `ENVO:00003033` | *mushroom compost* | A different thing entirely — an engineered substrate for growing fungi, not a fungal host. |
| `ENVO:01000889`, `ENVO:01000949`, `ENVO:03600084` | *area of lichen-dominated vegetation*, *lichen woodland*, *lichen material* | Landscape/material terms, not host-as-habitat; and lichen-only. |
| `FOODON:03411261` | *fungus* — "A member of the group of eukaryotic organisms in the kingdom Fungi…" | **A taxon/organism class, not a place.** Grounding or parenting to it publishes the over-claim #99 warns about. Correctly kept as `xref` on the record. |
| `FOODON:00004336`, `FOODON:00001143` | *fungus material*, *fungus food product* | Assert a food/material framing the GOLD path never claims. |
| `BTO:0001494` | *fungus* | Same taxon problem as FoodOn; BTO is a tissue/cell-line source. |
| `BTO:0001436`, `BTO:0001290`, `BTO:0001366` etc. | *mycelium*, *sporocarp*, *thallus* | **Narrower** — these are the *parts*, and the corpus already grounds the GOLD children to them (`mycelium.yaml` → `BTO:0001436`, `appressorium.yaml` → `BTO:0000085`, `germ_tube.yaml` → `BTO:0004822`, `sclerotium.yaml` → `BTO:0001810`, `spore.yaml` → `BTO:0001171`). That is the parts-ground / whole-does-not rule working; the whole is what `ENVO:01001041` supplies. |

No UBERON or PO term is relevant — neither covers fungal anatomy. (The fungus-specific anatomy ontology, FAO, is not among HabitatMech's five source ontologies.)

---

## 3. Differentia — what distinguishes it from its siblings

Siblings under `ENVO:01001000` are the other host-kingdom environments: plant-associated (`ENVO:01001001`), animal-associated (`ENVO:01001002`). The distinguishing properties are observable and well-sourced:

**a) The host is a fungus — and the structural material is chitin/β-glucan, not cellulose (plant) or collagen/ECM (animal).** Fungal walls share an alkali-insoluble core of branched β-(1,3)-glucan, β-(1,6)-glucan and chitin, with species-specific outer layers (mannoproteins in *Candida albicans*, a fibril-free surface in *Aspergillus fumigatus*, a capsule in *Cryptococcus neoformans*) — [Gow, Latgé & Munro 2017, *Microbiol Spectr* 5(3):FUNK-0035-2016, doi:10.1128/microbiolspec.FUNK-0035-2016](https://doi.org/10.1128/microbiolspec.FUNK-0035-2016) (PMID 28513415).

**b) The habitat is a filamentous, extensible network rather than a bounded body.** Hyphae provide continuous water films along which motile bacteria disperse — the "fungal highway" — crossing air-filled soil pores that are impassable to bacteria alone. Demonstrated with *Fusarium oxysporum* and a *Rhexocercosporidium* sp. carrying PAH-degrading *Achromobacter*, *Mycobacterium frederiksbergense* and *Sphingomonas*; mobilisation depends on hyphal hydrophobicity and requires bacterial flagellar motility — [Kohlmeier et al. 2005, *Environ Sci Technol* 39:4640–4646, doi:10.1021/es047979z](https://doi.org/10.1021/es047979z) (PMID 16047804). Reviewed with the "highways vs subways" (surface vs intracellular) distinction in [Deveau et al. 2018, doi:10.1093/femsre/fuy008](https://doi.org/10.1093/femsre/fuy008).

**c) It has a genuine intracellular compartment occupied by obligate bacterial endosymbionts.** *Rhizopus microsporus* harbours *Burkholderia* (now *Mycetohabitans*) *rhizoxinica* / *B. endofungorum* in its cytosol; the endosymbiont, not the fungus, makes the rice-seedling-blight toxin rhizoxin, and curing the fungus abolishes sporulation — [Partida-Martínez & Hertweck 2005, *Nature* 437:884–888, doi:10.1038/nature03997](https://doi.org/10.1038/nature03997); [Partida-Martínez et al. 2007, *Int J Syst Evol Microbiol* 57:2583–2590, doi:10.1099/ijs.0.64660-0](https://doi.org/10.1099/ijs.0.64660-0); [Lackner et al. 2011, *J Bacteriol* 193:783–784, doi:10.1128/JB.01318-10](https://doi.org/10.1128/JB.01318-10). Arbuscular mycorrhizal fungi carry two independent endobacterial lineages — '*Candidatus* Glomeribacter gigasporarum' ([Bianciotto et al. 2003, *Int J Syst Evol Microbiol* 53:121–124, doi:10.1099/ijs.0.02382-0](https://doi.org/10.1099/ijs.0.02382-0)) and Mollicutes-related endobacteria, later '*Ca.* Moeniiplasma glomeromycotorum' ([Desirò et al. 2014, *ISME J* 8:257–270, doi:10.1038/ismej.2013.151](https://doi.org/10.1038/ismej.2013.151); [Naito et al. 2017, *Int J Syst Evol Microbiol* 67:1177–1184, doi:10.1099/ijsem.0.001785](https://doi.org/10.1099/ijsem.0.001785)).

**d) Fruiting bodies are discrete, nutrient-rich, chemically distinctive islands whose bacterial communities are filtered from the surrounding soil by fungal chemistry.** Endofungal bacterial community structure differs across fungal phylogenetic groups and, less strongly, across guilds (ectomycorrhizal vs saprotrophic), and is partly explained by fruitbody C:N ratio and pH — [Pent, Bahram & Põldmaa 2020, *ISME J* 14:2131–2141, doi:10.1038/s41396-020-0674-7](https://doi.org/10.1038/s41396-020-0674-7) (PMID 32409757); see also [Pent, Põldmaa & Bahram 2017, *Front Microbiol* 8:836, doi:10.3389/fmicb.2017.00836](https://doi.org/10.3389/fmicb.2017.00836) and [Gohar et al. 2022, *Environ Microbiol Rep* 14:254–264, doi:10.1111/1758-2229.13045](https://doi.org/10.1111/1758-2229.13045).

**e) Physicochemistry, per HabitatMech's own upstream parameter table.** The existing `ENVO:01001041` record already carries kg-microbe `host_fungus` bands: water availability **high**, water variability **permanently wet**, nutrients **high**, organic matter **high**, structural complexity **high**, gradients **high**, salinity **low** with **small** variability, pressure **low**, temperature variability **medium**. These are attributed to the environment-parameter table, not to a paper, and should be cited as such.

**f) The characteristic microbiota are recognisably fungus-specific.** The 25 MADIN taxa already on the `ENVO:01001041` record read as a roll-call of the bacterial–fungal-interaction literature: *Burkholderia endofungorum* (endofungal), *Collimonas fungivorans* (mycophagous), *Pseudomonas fluorescens* BBc6R8 (the canonical *Laccaria bicolor* mycorrhiza helper strain — *my identification of the strain, from the MHB literature, not stated in the record*), and *Pseudomonas tolaasii* and *Janthinobacterium agaricidamnosum* (mushroom-cultivation pathogens). Supporting concepts: mycophagy as a defined trophic strategy with necrotrophic, extracellular-biotrophic and endocellular-biotrophic modes — [Leveau & Preston 2008, *New Phytol* 177:859–876, doi:10.1111/j.1469-8137.2007.02325.x](https://doi.org/10.1111/j.1469-8137.2007.02325.x); mycorrhiza helper bacteria — [Frey-Klett, Garbaye & Tarkka 2007, *New Phytol* 176:22–36, doi:10.1111/j.1469-8137.2007.02191.x](https://doi.org/10.1111/j.1469-8137.2007.02191.x) (PMID 17803639). **This convergence is the best independent evidence that `ENVO:01001041` and GOLD `Host-associated > Fungi` denote the same thing**: two unrelated upstream sources populated the same concept with the same organisms.

**g) Lichen thalli extend the habitat into extreme, desiccation-prone settings.** *Lobaria pulmonaria* thalli host >800 bacterial species contributing N, P and S supply, pathogen defence and abiotic stress resistance — [Grube et al. 2015, doi:10.1038/ismej.2014.138](https://doi.org/10.1038/ismej.2014.138); species-specific community structure in [Grube et al. 2009, *ISME J* 3:1105–1115, doi:10.1038/ismej.2009.63](https://doi.org/10.1038/ismej.2009.63).

**General framing references** for the fungus-as-habitat concept: [Frey-Klett et al. 2011, *Microbiol Mol Biol Rev* 75:583–609, doi:10.1128/MMBR.00020-11](https://doi.org/10.1128/MMBR.00020-11) (PMID 22126995, PMC3232736) and [Deveau et al. 2018, doi:10.1093/femsre/fuy008](https://doi.org/10.1093/femsre/fuy008).

---

## 4. Sources

All cited inline above. Consolidated, with what each supports:

| Claim | Source |
|---|---|
| GOLD five-level path; `Host-associated` = sampled from another organism; Ecosystem Category = host taxon | [gold.jgi.doe.gov/ecosystem_classification](https://gold.jgi.doe.gov/ecosystem_classification) |
| GOLD sub-paths and assertion counts under `Host-associated > Fungi` | `data/raw/gold_ecosystem_paths.tsv` (repo, lines 57, 104, 158, 160, 263, 270, 1915, 1969–1973) |
| `ENVO:01001041` label, definition, synonyms, parents; near-miss inventory | [OLS4 / ENVO](https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001041); `data/raw/ontology_terms.tsv`, `data/raw/ontology_subclass_edges.tsv` (repo) |
| ENVO scope and design | Buttigieg et al. [2013 doi:10.1186/2041-1480-4-43](https://doi.org/10.1186/2041-1480-4-43); [2016 doi:10.1186/s13326-016-0097-6](https://doi.org/10.1186/s13326-016-0097-6) |
| EMPO host-taxon axis incl. `Fungus`; ENVO as EMPO's base | [earthmicrobiome.org/protocols-and-standards/empo](https://earthmicrobiome.org/protocols-and-standards/empo/); [Thompson et al. 2017 doi:10.1038/nature24621](https://doi.org/10.1038/nature24621); [Shaffer et al. 2022 doi:10.1038/s41564-022-01266-x](https://doi.org/10.1038/s41564-022-01266-x) |
| Bacterial–fungal interactions, general | [Frey-Klett et al. 2011 doi:10.1128/MMBR.00020-11](https://doi.org/10.1128/MMBR.00020-11); [Deveau et al. 2018 doi:10.1093/femsre/fuy008](https://doi.org/10.1093/femsre/fuy008) |
| Fungal wall composition | [Gow et al. 2017 doi:10.1128/microbiolspec.FUNK-0035-2016](https://doi.org/10.1128/microbiolspec.FUNK-0035-2016) |
| Hyphal water films as dispersal habitat | [Kohlmeier et al. 2005 doi:10.1021/es047979z](https://doi.org/10.1021/es047979z) |
| Endofungal bacteria | [Partida-Martínez & Hertweck 2005 doi:10.1038/nature03997](https://doi.org/10.1038/nature03997); [Partida-Martínez et al. 2007 doi:10.1099/ijs.0.64660-0](https://doi.org/10.1099/ijs.0.64660-0); [Lackner et al. 2011 doi:10.1128/JB.01318-10](https://doi.org/10.1128/JB.01318-10) |
| AMF endobacteria | [Bianciotto et al. 2003 doi:10.1099/ijs.0.02382-0](https://doi.org/10.1099/ijs.0.02382-0); [Desirò et al. 2014 doi:10.1038/ismej.2013.151](https://doi.org/10.1038/ismej.2013.151); [Naito et al. 2017 doi:10.1099/ijsem.0.001785](https://doi.org/10.1099/ijsem.0.001785) |
| Fruitbody chemistry structures endofungal communities | [Pent et al. 2020 doi:10.1038/s41396-020-0674-7](https://doi.org/10.1038/s41396-020-0674-7); [Pent et al. 2017 doi:10.3389/fmicb.2017.00836](https://doi.org/10.3389/fmicb.2017.00836); [Gohar et al. 2022 doi:10.1111/1758-2229.13045](https://doi.org/10.1111/1758-2229.13045) |
| Mycophagy; mycorrhiza helper bacteria | [Leveau & Preston 2008 doi:10.1111/j.1469-8137.2007.02325.x](https://doi.org/10.1111/j.1469-8137.2007.02325.x); [Frey-Klett et al. 2007 doi:10.1111/j.1469-8137.2007.02191.x](https://doi.org/10.1111/j.1469-8137.2007.02191.x) |
| Lichen thallus microbiome | [Grube et al. 2015 doi:10.1038/ismej.2014.138](https://doi.org/10.1038/ismej.2014.138); [Grube et al. 2009 doi:10.1038/ismej.2009.63](https://doi.org/10.1038/ismej.2009.63) |

**Explicitly flagged as my inference, not sourced:** (i) that mycosphere/hyphosphere *soil* falls outside this concept — derived from GOLD's definition of `Host-associated`, not stated about this path; (ii) that ENVO's "fungal structure" wording is an editorial inconsistency rather than a narrower scope — inferred from the parallel plant/animal definitions and the `Fungus` alt-label; (iii) the identification of *P. fluorescens* BBc6R8 as the *Laccaria bicolor* MHB strain; (iv) the reading that GOLD's separate `Endosymbionts > Fungi` path is a path artefact rather than a distinct habitat.

I could not retrieve the enumerated GOLD path list from `gold.jgi.doe.gov` directly (HTTP 403 to automated fetch); the path table above comes from this repo's own `data/raw/` extract, which is the authoritative copy for HabitatMech's purposes.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept:**
- fungi-associated environment; fungus-associated environment; fungus environment (ENVO exact synonyms)
- `Fungus` (EMPO host-taxon value; ENVO alt-label)
- host fungus (kg-microbe environment key `host_fungus`)
- fungal host; fungal holobiont / fungal microbiome (when "microbiome" means *of* the fungus)
- endofungal / endohyphal habitat (for the intracellular subregion)
- mycosphere, hyphosphere (adjacent — see below)

**Commonly but wrongly treated as the same thing:**

| Confusable | Why it is different |
|---|---|
| **Mycobiome** | The *fungal community within another host* (human gut mycobiome, plant mycobiome). Directionally the inverse: there the fungus is the sampled organism, here it is the habitat. This is the single most likely misreading of the bare label "Fungi". |
| **The taxon *Fungi*** (`FOODON:03411261`, `BTO:0001494`, `NCBITaxon:4751`) | A class of organisms, not a place. Belongs in `xrefs`, per #99. |
| **Mycosphere / hyphosphere** | The *soil* zone influenced by hyphae — a soil habitat modified by a fungus, not the fungus. Continuous with this concept in practice, distinct in ENVO and in GOLD's level-1 split. |
| **Mycorrhiza** | Ambiguous: as a *fungal organ* it is inside (GOLD lists it as a child); as the *plant root–fungus composite* it straddles plant-associated and fungi-associated. GOLD's placement fixes the fungal reading. |
| **Mushroom compost** (`ENVO:00003033`) | An engineered growth substrate *for* fungi. Not a fungal host. |
| **Fungal culture medium** | `Engineered` in GOLD; already a separate HabitatMech record. |
| **Fungal food products** (`FOODON:00001143`, `FOODON:00002434`) | Assert a food framing GOLD does not. |
| **Lichen** | Inside per GOLD, but it is a composite of mycobiont + photobiont; `FOODON:03412345` describes the composite organism, not the environment. HabitatMech's `lichen.yaml` keeps its own identity with the FoodOn term as `xref` — correct. |

---

## 6. Should this be a term at all?

**It is a habitat — but it should not be a *new* term.** It is a place (an organism acting as host), not a process, quality, disease or sampling artefact, so `NOT_APPLICABLE` is indeed the wrong disposition and the #114 reversal was right to undo it. But the reversal over-corrected: it moved the concept from `NOT_APPLICABLE` to `CONFIRM_UNGROUNDED` / term-request when the correct third option — `GROUND` to an existing ENVO term — was available all along.

**Recommended disposition: `GROUND` `habitatmech:GOLD.a8fc5001d1` → `ENVO:01001041` "fungi-associated environment".**

Four things a curator should check before or while making that change:

1. **This merges two records.** `ENVO:01001041` is already the identifier of `data/habitats/other/fungi_associated_environment.yaml` (attested by `ENVIRONMENTS_TABLE` `host_fungus` and `MADIN`, 38 taxa). Grounding adds GOLD's 635 organism-assertions as a third attestation on that record. Per the corpus rules this needs a `RETIRED.tsv` pass after commit (`seed-apply` → commit → `just redirects` → `just render` → commit), because `data/habitats/host_associated/fungi__136600ff.yaml` will disappear.

2. **Category conflict to resolve.** The existing `ENVO:01001041` record is `habitat_category: OTHER`; the GOLD concept is `HOST_ASSOCIATED`. The merged record should be `HOST_ASSOCIATED`. Worth checking whether the sibling plant/animal ENVO records have the same misfiling.

3. **The children re-parent cleanly.** `mycelium.yaml`, `spore.yaml`, `appressorium.yaml`, `germ_tube.yaml`, `sclerotium.yaml`, `fruiting_body.yaml` and `lichen.yaml` all list `habitatmech:GOLD.a8fc5001d1` in `parent_habitats`; those become `ENVO:01001041`, which is a real ENVO parent rather than a minted one — a net improvement. `Fruiting body > Inner tissue` gains an obvious target in `ENVO:01001058`.

4. **The existing note misdescribes its own record.** The `CONFIRM_UNGROUNDED` note says "Nearest broader term FOODON:03411261 'fungus' attached as a **parent**", but the record has `parent_habitats: [ENVO:01001000]` and `xrefs: [FOODON:03411261]`. The record is right and the note is wrong — the same boilerplate appears on the sibling `habitatmech:GOLD.1ab59245f7` record. Since `tests/test_decisions.py` exists specifically to catch notes making claims the repo contradicts, this is worth fixing in the decision text regardless of the grounding outcome.

**Knock-on:** `habitatmech:GOLD.1ab59245f7` (`Host-associated > Endosymbionts > Fungi`, 0 assertions) carries the same "no ontology term fits" note and is the same concept viewed from the endosymbiont side. It should be reviewed in the same pass — either grounded to `ENVO:01001041` as well, or explicitly justified as narrower.

**If, despite the above, a HabitatMech-minted term is still wanted**, the one defensible sentence is:

> An environmental system determined by an organism which is determined by a fungus, comprising the surfaces, internal tissues, intracellular compartments and adherent water films of a living or dead fungal thallus at any structure or life stage.

— which is `ENVO:01001041`'s definition with the "structure" wording corrected to match its plant and animal siblings. That it takes only a wording fix to reach is itself the argument for grounding instead of minting.

## Citations

1. https://gold.jgi.doe.gov/ecosystem_classification
2. https://doi.org/10.1093/femsre/fuy008
3. https://doi.org/10.1038/ismej.2014.138
4. https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001041
5. https://doi.org/10.1186/2041-1480-4-43
6. https://doi.org/10.1186/s13326-016-0097-6
7. https://earthmicrobiome.org/protocols-and-standards/empo/
8. https://doi.org/10.1038/nature24621
9. https://doi.org/10.1038/s41564-022-01266-x
10. https://doi.org/10.1128/microbiolspec.FUNK-0035-2016
11. https://doi.org/10.1021/es047979z
12. https://doi.org/10.1038/nature03997
13. https://doi.org/10.1099/ijs.0.64660-0
14. https://doi.org/10.1128/JB.01318-10
15. https://doi.org/10.1099/ijs.0.02382-0
16. https://doi.org/10.1038/ismej.2013.151
17. https://doi.org/10.1099/ijsem.0.001785
18. https://doi.org/10.1038/s41396-020-0674-7
19. https://doi.org/10.3389/fmicb.2017.00836
20. https://doi.org/10.1111/1758-2229.13045
21. https://doi.org/10.1111/j.1469-8137.2007.02325.x
22. https://doi.org/10.1111/j.1469-8137.2007.02191.x
23. https://doi.org/10.1038/ismej.2009.63
24. https://doi.org/10.1128/MMBR.00020-11