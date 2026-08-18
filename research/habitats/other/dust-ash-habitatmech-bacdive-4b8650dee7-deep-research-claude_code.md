---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T00:28:26.408088'
end_time: '2026-08-18T00:42:12.197386'
duration_seconds: 825.79
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Dust-Ash
  habitat_identifier: habitatmech:BACDIVE.4b8650dee7
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Dust-Ash'
  assertions: '20'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Cohort
    review: dust and ash are different materials and the slice has both (ENVO:00002008,
    ENVO:02000090). Grounding to either half would assert an identity the source does
    not have. (source concept habitatmech:BACDIVE.4b8650dee7)'
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
  web_search_requests: 13
  num_turns: 40
  total_cost_usd: 4.490608999999999
  session_id: 2540d0dc-7a14-4ab8-9e20-4334384e3c6c
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 32
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Dust-Ash
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.4b8650dee7
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Dust-Ash
- **Upstream assertion volume:** 20
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Cohort review: dust and ash are different materials and the slice has both (ENVO:00002008, ENVO:02000090). Grounding to either half would assert an identity the source does not have. (source concept habitatmech:BACDIVE.4b8650dee7)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Dust-Ash** as a microbial habitat, with citations.

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

I'll research this concept. Let me load the web tools and check the repo's own evidence for what the source actually attests.

MISO's tag is `#Dust (Ash)` — that reframes the concept. Let me verify the tag string and gather the ENVO slice plus literature.

The tag's placement matters and the summarizer is giving inconsistent answers. Let me get the raw page myself.

# Definition research: `habitatmech:BACDIVE.4b8650dee7` — "Dust-Ash"

> **A solid environmental material which consists of fine, dry particles that have accumulated as a residue of human activity — either settled dust or the ash left by combustion — and that is sampled as a deposited bulk solid rather than as the air that carried it.**

Genus term: `ENVO:01000814` **solid environmental material** (verified: it is the nearest common superclass of `ENVO:00002008` dust and `ENVO:02000090` ash in live ENVO, and it is in the vendored slice).

**Read §6 before using this sentence.** The definition is only writable at this altitude because the source concept is a *disjunction* of two materials ENVO already names separately. My recommendation is to keep the record `UNGROUNDED` (as curation already decided), add **both** halves as `relation: xref`, and not raise an ENVO term request for the union. The existing curator note is right; the new evidence below strengthens it and corrects one part of its framing.

---

## 1. What the concept denotes

### The decisive evidence: the source path

The record's label is a slug-flattening of a BacDive/MISO tag. I parsed the tag tree out of the raw HTML of BacDive's isolation-source browser ([bacdive.dsmz.de/isolation-sources](https://bacdive.dsmz.de/isolation-sources), retrieved 2026-08-18) rather than trusting a page summary, because two summarisation passes disagreed. Ground truth from the markup:

| tag id | name | parent (cat2) | cat1 |
|---|---|---|---|
| **308** | **`#Dust (Ash)`** | **10 = `#Waste`** | **1 = `#Engineered`** |
| 315 | `#Dust` | 17 = `#Terrestrial` | 2 = `#Environmental` |

So the full path of *this* concept is:

> **`#Engineered` > `#Waste` > `#Dust (Ash)`**

Confirmed at strain level: BacDive strain 8468 (*Mycobacterium pulveris* 33505, sample type "house dust") carries the literal tag string `#Engineered #Waste #Dust (Ash)` ([bacdive.dsmz.de/strain/8468](https://bacdive.dsmz.de/strain/8468), retrieved 2026-08-18).

Three things follow, and they change the reading:

1. **This is not the label "Dust and Ash" as a compound of equals.** MISO uses parentheses throughout as a subsumed-example gloss — `#Animal habitation (Nest,Burrow)`, `#Plant exudate (Resin)`, `#Root (Rhizome)`, `#Mud (Sludge)`, `#Wetland (Swamp)`. `#Dust (Ash)` reads as *dust, ash included in the same bin*. Dust is the head; ash is folded in.
2. **MISO already has a separate, purely environmental dust tag** (`#Environmental > #Terrestrial > #Dust`, id 315). This record is *not* that one. The differentiating axis MISO chose is **anthropogenic residue vs. natural terrestrial material**, not composition.
3. **MISO also has a separate `#Air` cat2 tag** (id 13, under `#Environmental`, with `#Indoor air` / `#Outdoor air` beneath it). So the source vocabulary itself already draws the dust/air boundary; this concept is the deposited solid, not the gas.

Its cat3 siblings under `#Waste` are: activated sludge, coalbed water, domestic waste, industrial waste, industrial wastewater, landfill, sewage sludge, solid animal waste, solid plant waste, solid waste, waste gas, wastewater, water treatment plant. That sibling set is the clearest statement of intent available: **the bin is for particulate residues and by-products of human activity.**

### The extension, from the strains themselves

The 16 taxa on the record split cleanly across the two halves — I checked the original species descriptions:

| Half | Taxon on the record | Isolation source in the species description |
|---|---|---|
| **Ash** | *Sphingobium fuliginis* | fly-ash dumping site, Panki thermal power plant, Kanpur, India ([Prakash & Lal 2006, IJSEM 56:2147–2152, doi:10.1099/ijs.0.64080-0](https://doi.org/10.1099/ijs.0.64080-0); PMID [16957112](https://pubmed.ncbi.nlm.nih.gov/16957112/)) |
| **Ash** | *Pseudomonas delhiensis* | fly-ash dumping site of a thermal power plant, Delhi ([Prakash, Kumari & Lal 2007, IJSEM 57:527–531, doi:10.1099/ijs.0.64456-0](https://doi.org/10.1099/ijs.0.64456-0); PMID [17329778](https://pubmed.ncbi.nlm.nih.gov/17329778/)) |
| **Dust (indoor)** | *Mycolicibacterium pulveris* | house dust, Japan; epithet *pulveris* = "of dust" ([Tsukamura, Mizuno & Toyama 1983, IJSB 33:811–815, doi:10.1099/00207713-33-4-811](https://doi.org/10.1099/00207713-33-4-811)) |
| **Dust (airborne)** | *Sphingomonas aurantiaca*, *S. faeni* | described as "air- and dustborne … psychrotolerant bacteria"; *S. faeni* = "of hay" ([Busse et al. 2003, IJSEM 53:1253–1260, doi:10.1099/ijs.0.02461-0](https://doi.org/10.1099/ijs.0.02461-0); PMID [13130003](https://pubmed.ncbi.nlm.nih.gov/13130003/)) |
| **Dust (wood)** | *Aliirhizobium (Rhizobium) cellulosilyticum* | sawdust / pulverised decaying wood of *Populus alba* ([García-Fraile et al. 2007, IJSEM 57:844–848, doi:10.1099/ijs.0.64680-0](https://doi.org/10.1099/ijs.0.64680-0); PMID [17392217](https://pubmed.ncbi.nlm.nih.gov/17392217/)) |
| **Dust (organic/occupational)** | *Amycolatopsis sacchari* | "a moderately thermophilic actinomycete isolated from vegetable matter"; epithet *sacchari* points at sugarcane bagasse ([Goodfellow et al. 2001, IJSEM 51:187–193](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-51-1-187)) — *the bagasse-dust link is my inference from the epithet and the bagassosis literature, not a quotation from that paper* |

That is the concept's real extension: **settled indoor/house dust, occupational and organic process dust (hay, grain, bagasse, sawdust), and combustion ash including fly ash and ash-dump material.**

### The boundary

**Inside:** settled house/indoor dust; vacuum-bag and surface dust; hay, grain, bagasse, cotton, wood dust; industrial and mineral process dust; wood ash, coal ash, bottom ash, fly ash; ash-dump and ash-pond deposits.

**Neighbouring, outside:**
- **Air / bioaerosol** — MISO's own `#Air` tag with `#Indoor air` and `#Outdoor air` children; the medium, not the deposit.
- **Natural terrestrial dust** — MISO's separate `#Environmental > #Terrestrial > #Dust` (id 315): desert and aeolian dust.
- **Volcanic ash in situ** — MISO files volcanic material under `#Environmental > #Terrestrial > #Volcanic` (id 116), not here. Volcanic ash is a genuine microbial habitat (§3.4), but it is not what this tag collects.
- **Soil amended with ash, or post-fire soil** — the substrate is soil; the ash is a treatment.
- **Sludge, landfill, solid waste** — sibling tags, not this one.

### Ambiguity — stated, not silently resolved

The label admits two readings, and the source path resolves them only partly:

- **(a) Union reading** — "dust ∪ ash", one bin holding two distinct materials. This is what the strain evidence shows in practice: two disjoint clusters (house/organic dust; fly-ash dumps) with nothing in between.
- **(b) Head-plus-gloss reading** — "dust, ash included", i.e. *fine anthropogenic particulate residue* as a single kind, with ash as one variety. This is what MISO's parenthetical convention and the `#Waste` parent suggest was intended.

Reading (b) is the one that supports a definition at all; reading (a) is the one the data actually behaves like. **My judgement: the concept is genuinely a bin, and the definition above works only by abstracting to "fine dry particulate residue", which is broad enough to swallow both.** That is an honest description of the source, not a natural kind.

---

## 2. Genus — the broader kind

### The one term that fits

`ENVO:01000814` **solid environmental material** — *"An environmental material which is in a solid state."*

Verified live via OLS4 (retrieved 2026-08-18): `hierarchicalParents` of `ENVO:02000090` ash → `ENVO:01000814` only; of `ENVO:00002008` dust → `ENVO:01000060` particulate environmental material **and** `ENVO:01000814`. So **`ENVO:01000814` is the least common subsumer of the two halves.** It is present in the vendored slice (`data/raw/ontology_terms.tsv`) with that exact label, so it passes the seeder's label check.

It is also *very* broad — it admits soil, rock, sediment, ice. A curator may reasonably judge that asserting it adds little. It is nonetheless the only ENVO parent that is true of the whole concept.

### Near-misses and why each fails

| Candidate | Why it is not a match |
|---|---|
| `ENVO:00002008` **dust** — "Particulate environmental material with diameters less than 500 micrometers" | Covers roughly two-thirds of the strains and none of the fly-ash ones. Grounding here asserts a size bound and a non-combustion origin the ash half does not have. **Narrower than the concept.** |
| `ENVO:02000090` **ash** — "the non-aqueous, non-gaseous residues that remain after something is burned" | Covers the fly-ash strains only. Asserts combustion, which house dust and sawdust did not undergo. **Narrower than the concept.** This is the term `data/raw/isolation_source_groundings.tsv:96` proposes as a `skos:closeMatch` by lexical match — it is a half-match, and the existing decision to reject it is correct. |
| `ENVO:01000060` **particulate environmental material** | Tempting, and true of dust — but **ash is not asserted under it in ENVO** (verified above). Using it would silently retype the ash half. Also admits sand, silt, sediment. |
| `ENVO:00002264` **waste material** — "A material which is not the desired output of a process…" (in the slice) | Matches MISO's `#Waste` parent, and is the most *semantically* attractive genus. It fails on the dust half: house dust in situ is not the discarded output of a process, and neither is airborne hay dust. It also does not subsume `ash` or `dust` in ENVO. Asserting it publishes a waste-role claim BacDive's tag placement implies but the samples do not support. **Record as an xref if wanted; do not use as genus.** |
| `ENVO:00002267` **industrial waste material**, `ENVO:01000372` **household waste material**, `ENVO:03510070` **toxic waste** | Each true of a fraction only; each asserts a provenance the rest of the bin lacks. |
| `ENVO:00010505` **aerosol** — "Airborne solid particles … or liquid droplets" | Asserts suspension in a gas. This bin is deposited material, and MISO has a separate `#Air` tag. |
| `ENVO:00002005` **air** | A gas mixture; would type a solid as a gas. |
| `ENVO:01000701` **volcanic ash**, `ENVO:02000127` **coal ash**, `ENVO:02000128` **fly ash**, `ENVO:02000126` **wood ash** | All narrower children of `ash`; each names one fuel. |
| The 19 composition-differentiated dust children (`silica`, `coal`, `mineral`, `fibrous`, `metallic`, `cement`, `clay`, `asbestos`, `grain`, `cotton`, `wood`, `rock`, `kaolin`, `talc`, `slate`, `barium`, `aluminium`, `fibrous glass`, `dust from plant parts`) | Each asserts a dominant material. The bin cuts across all of them. |
| `ENVO:03000021` **soot** | A carbon-particle combustion product — a plausible member, not the genus. |
| `ENVO:00002007` **sediment** | Asserts deposition by flowing liquid. |
| `ENVO:01000595` **cupboard**, `ENVO:03600000` **cleanroom** | Lexical hits (their definitions mention dust). Not the concept. |

**Exhaustiveness check (verified this session):** a full OLS4 ENVO search returns 41 classes for `dust`, 25 for `ash`, 5 for `soot`. There is no ENVO class naming the union, no "particulate waste", and no "anthropogenic particulate residue". The curator note's conclusion — no term fits — is confirmed against live ENVO, not just the vendored slice. What the note gets slightly wrong is the implication that *nothing* attaches: `ENVO:01000814` is a legitimate, checkable parent for the whole bin.

---

## 3. Differentia — what distinguishes it

Ordered most to least observable.

**3.1 Physical state and grain size (primary).** Dry, unconsolidated, fine particulate; ENVO's dust bound is <500 µm and volcanic ash is defined at <2 mm ([`ENVO:00002008`](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002008), [`ENVO:01000701`](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01000701)). This is what separates it from sludge, wastewater and landfill among its `#Waste` siblings.

**3.2 Formation: air transport and settling, or combustion residue.** Two formation routes, and this duality is the concept's defining weakness as a class: *deposition of suspended particles* (dust) versus *what is left when something burns* (`ENVO:02000090`'s own definition). ENVO models the second route as a distinct process, `ENVO:01000839` combustion process, and the fall route as `ENVO:01000702` ash fall process.

**3.3 Anthropogenic setting.** The MISO cat1 is `#Engineered` and the cat2 is `#Waste`: houses, workplaces, processing plants, power-station ash dumps. This is the axis MISO used to split tag 308 from tag 315.

**3.4 Physicochemistry — and it differs sharply between the halves.** This is the strongest argument that the bin is not one habitat:
- *Dust*: low and fluctuating water activity, high organic and fibrous content, near-neutral, room temperature. Active microbial growth in floor dust requires elevated equilibrium relative humidity — fungal growth rates and community structure change profoundly above ~80 % ERH ([Dannemiller, Weschler & Peccia 2017, *Indoor Air* 27:354–363, doi:10.1111/ina.12313](https://doi.org/10.1111/ina.12313); PMID 27272645).
- *Ash*: strongly alkaline, salt- and oxide-rich, organic-carbon-poor, often metal-loaded. Coal-ash dumps at Apatity carry calcium and magnesium oxide roughly double the levels in regional natural soils ([Davydov et al. 2025, *Microorganisms* 13:1762, doi:10.3390/microorganisms13081762](https://doi.org/10.3390/microorganisms13081762); [PMC12388845](https://pmc.ncbi.nlm.nih.gov/articles/PMC12388845/)). Wildfire ash can raise soil pH by as much as 3 units ([ASM, *The Microbiology of Wildfires*, 2021](https://asm.org/articles/2021/april/the-microbiology-of-wildfires)). Fly-ash ponds are arsenic-leaching enough to matter for drinking-water limits ([*Bull Environ Contam Toxicol* 2018, doi:10.1007/s00128-018-2428-z](https://doi.org/10.1007/s00128-018-2428-z)).

**3.5 Community signature.** The record's own 16 taxa are dominated by desiccation- and oligotrophy-tolerant Actinomycetota (*Streptomyces griseus* subsp. *griseus* ×3 strains, *S. violaceoruber*, *S. antimycoticus*, *Amycolatopsis sacchari*, *Nocardiopsis dassonvillei*, *Agromyces ulmi*, *Mycolicibacterium pulveris*) plus pigmented, psychrotolerant, PAH-degrading Sphingomonadaceae (*Sphingomonas aurantiaca*, *S. faeni*, *Sphingobium fuliginis*). *Nocardiopsis* and thermophilic actinomycetes are the classic organic-dust taxa of hypersensitivity pneumonitis, farmer's lung and bagassosis ([*Bagassosis*, StatPearls NBK554444](https://www.ncbi.nlm.nih.gov/books/NBK554444/); [*Farmer's Lung*, StatPearls NBK557580](https://www.ncbi.nlm.nih.gov/books/NBK557580/)). The ash-derived isolates are instead aromatic-hydrocarbon degraders selected on ash as a carbon-poor, PAH-bearing substrate (Prakash & Lal 2006; Prakash et al. 2007, above). *That these two signatures are near-disjoint is my inference from the source list, not a claim any paper makes about this bin.*

**3.6 Ash supports genuine primary succession.** Ash is not merely a residue that microbes are deposited on: cyanobacterial colonisation of coal-ash dumps begins immediately after deposition, rising from 4 taxa in current-year slag to 12 species in a 30-year deposit, forming biocrusts that deposit C and N and initiate soil formation ([Davydov et al. 2025, doi:10.3390/microorganisms13081762](https://doi.org/10.3390/microorganisms13081762)). Fly-ash-exposed soils near Kolaghat were dominated by Actinobacteria (48.3 %) and Proteobacteria (40.8 %) ([*Environ Sci Pollut Res* 2025, doi:10.1007/s11356-025-36520-2](https://doi.org/10.1007/s11356-025-36520-2)). For volcanic ash, pioneer colonisation is driven by chemolithotrophy — N-fixing iron oxidisers on young Miyake-jima deposits, CO/H₂ oxidisers on Hawaiian and Pinatubo material ([*Sci Rep* 6:19687, doi:10.1038/srep19687](https://doi.org/10.1038/srep19687); [PMC4726209](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4726209/)) — and volcanic ash supported the most diverse bacterial community among five substrates in a marine mesocosm ([Witt et al. 2017, *Geobiology*, doi:10.1111/gbi.12231](https://doi.org/10.1111/gbi.12231); PMID [28256065](https://pubmed.ncbi.nlm.nih.gov/28256065/)).

**3.7 Operational definition.** Sampled as bulk solid — vacuum bag, surface wipe, sieved fraction, or a grab sample from an ash dump/pond — as opposed to filter or impinger sampling of air. *This distinction is drawn from the sampling literature generally and from MISO's separate `#Air` tag; I did not find a source stating it as a definitional criterion for this bin.*

---

## 4. Sources

**Verified by direct retrieval this session (raw fetch or OLS4 API, 2026-08-18):**
- MISO tag tree and the exact placement `#Engineered > #Waste > #Dust (Ash)` (tag id 308, parent 10, cat1 1), the separate `#Dust` (315, under `#Terrestrial`), `#Air` (cat2 id 13), and the 14 `#Waste` siblings — parsed from the HTML of <https://bacdive.dsmz.de/isolation-sources>
- Strain-level tag string `#Engineered #Waste #Dust (Ash)` with sample type "house dust" — <https://bacdive.dsmz.de/strain/8468>
- ENVO parents of `ENVO:02000090` (→ `ENVO:01000814` only) and `ENVO:00002008` (→ `ENVO:01000060`, `ENVO:01000814`); children of ash (`wood ash` 02000126, `coal ash` 02000127, `fly ash` 02000128, `bottom ash` 02000129, `volcanic ash` 01000701); full ENVO search counts for dust (41), ash (25), soot (5) — [OLS4 API](https://www.ebi.ac.uk/ols4/)
- Local corpus: `data/habitats/other/dust_ash.yaml`, `data/raw/bacdive_isolation_sources.tsv:115`, `data/raw/isolation_source_groundings.tsv:96`, `data/raw/bacdive_source_taxa.tsv:849-864`, `data/raw/ontology_terms.tsv`, `data/raw/ontology_subclass_edges.tsv`

**Species descriptions (abstract-level retrieval via search summaries; a curator quoting a specific figure should open the paper):**
- Tsukamura M, Mizuno S, Toyama H (1983). *Mycobacterium pulveris* sp. nov. *Int J Syst Bacteriol* 33:811–815. doi:[10.1099/00207713-33-4-811](https://doi.org/10.1099/00207713-33-4-811)
- Busse H-J et al. (2003). *Sphingomonas aurantiaca* sp. nov., *S. aerolata* sp. nov. and *S. faeni* sp. nov., air- and dustborne … *IJSEM* 53:1253–1260. doi:[10.1099/ijs.0.02461-0](https://doi.org/10.1099/ijs.0.02461-0); PMID 13130003
- Prakash O, Lal R (2006). *Sphingobium fuliginis* sp. nov., … from a fly ash dumping site. *IJSEM* 56:2147–2152. doi:[10.1099/ijs.0.64080-0](https://doi.org/10.1099/ijs.0.64080-0); PMID 16957112
- Prakash O, Kumari K, Lal R (2007). *Pseudomonas delhiensis* sp. nov., from a fly ash dumping site of a thermal power plant. *IJSEM* 57:527–531. doi:[10.1099/ijs.0.64456-0](https://doi.org/10.1099/ijs.0.64456-0); PMID 17329778
- García-Fraile P et al. (2007). *Rhizobium cellulosilyticum* sp. nov., isolated from sawdust of *Populus alba*. *IJSEM* 57:844–848. doi:[10.1099/ijs.0.64680-0](https://doi.org/10.1099/ijs.0.64680-0); PMID 17392217
- Goodfellow M et al. (2001). *Amycolatopsis sacchari* sp. nov., a moderately thermophilic actinomycete isolated from vegetable matter. *IJSEM* 51:187–193.

**Habitat literature (abstract-level unless noted):**
- Davydov D et al. (2025). Cyanobacterial assemblages inhabiting the Apatity thermal power plant fly ash dumps in the Russian Arctic. *Microorganisms* 13:1762. doi:[10.3390/microorganisms13081762](https://doi.org/10.3390/microorganisms13081762); [PMC12388845](https://pmc.ncbi.nlm.nih.gov/articles/PMC12388845/)
- Fly-ash contamination and soil microbial diversity near Kolaghat TPP (2025). *Environ Sci Pollut Res.* doi:[10.1007/s11356-025-36520-2](https://doi.org/10.1007/s11356-025-36520-2)
- Arsenic bioremediation by heavy-metal-resistant bacteria of a fly ash pond (2018). *Bull Environ Contam Toxicol.* doi:[10.1007/s00128-018-2428-z](https://doi.org/10.1007/s00128-018-2428-z)
- Unique pioneer microbial communities exposed to volcanic sulfur dioxide (2016). *Sci Rep* 6:19687. doi:[10.1038/srep19687](https://doi.org/10.1038/srep19687); [PMC4726209](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4726209/)
- Witt V et al. (2017). Volcanic ash supports a diverse bacterial community in a marine mesocosm. *Geobiology.* doi:[10.1111/gbi.12231](https://doi.org/10.1111/gbi.12231); PMID 28256065
- Dannemiller KC, Weschler CJ, Peccia J (2017). *Indoor Air* 27:354–363. doi:[10.1111/ina.12313](https://doi.org/10.1111/ina.12313); PMID 27272645
- *Bagassosis*, StatPearls: <https://www.ncbi.nlm.nih.gov/books/NBK554444/> · *Farmer's Lung*, StatPearls: <https://www.ncbi.nlm.nih.gov/books/NBK557580/>
- ASM (2021), *The Microbiology of Wildfires*: <https://asm.org/articles/2021/april/the-microbiology-of-wildfires>

**Vocabularies/standards:**
- ENVO — <http://environmentontology.org/>; Buttigieg PL et al. (2013) *J Biomed Semantics* 4:43, [PMC3904460](https://pmc.ncbi.nlm.nih.gov/articles/PMC3904460/)
- BacDive — Reimer LC et al. (2022) *Nucleic Acids Res* 50(D1):D741–D746, doi:[10.1093/nar/gkab961](https://doi.org/10.1093/nar/gkab961); current citation: BacDive in 2025, *NAR* 53(D1):D748, <https://academic.oup.com/nar/article/53/D1/D748/7848838>

**Explicitly my inference, not stated by any source:** the union-vs-head-plus-gloss ambiguity analysis and its resolution (§1); the reading of MISO parentheses as a subsumed-example gloss (inferred from the pattern across `#Root (Rhizome)`, `#Mud (Sludge)`, `#Animal habitation (Nest,Burrow)` etc.); the bagasse link for *A. sacchari*; the claim that the dust-taxon and ash-taxon signatures are near-disjoint; all recommendations in §6.

**Not checked this session:** SNOMED CT, AGROVOC, the MIxS built-environment package, and the indoor-dust microbiome primary literature beyond Dannemiller (Barberán et al. 2015, Adams et al. 2013, Amend et al. 2010 are cited in the sibling report `research/habitats/engineered/dust-habitatmech-gold-398aeb6c37-…md` and I did not re-verify them here). If the definition is to lean on indoor-dust ecology, take the citations from that report and check them.

---

## 5. Synonyms, and what not to conflate

**Names in real use for the whole bin:** there are none. This is worth stating plainly — "dust-ash" is not a term of art in any literature I found. It exists only as a BacDive/MISO tag string.

**Names in use for the halves:** *dust* — settled dust, house dust, indoor dust, floor dust, vacuum dust, reservoir dust, organic dust, occupational dust, grain/hay/bagasse/cotton/wood dust, sawdust, process dust. *ash* — ash, wood ash, coal ash, bottom ash, fly ash, pulverised-fuel ash (PFA), coal combustion residuals (an ENVO synonym on `ENVO:02000127`), ash pond/dump material, cenospheres.

**Commonly but wrongly treated as the same thing:**

| Not the same | Why |
|---|---|
| **`ENVO:02000090` ash alone** | The lexical mapping in `data/raw/isolation_source_groundings.tsv` proposes exactly this (`skos:closeMatch`, medium confidence, `semapv:LexicalMatching`). It covers 2 of 16 taxa. Adopting it would retype house dust and sawdust as combustion residue. |
| **`ENVO:00002008` dust alone** | The mirror-image error; drops the fly-ash strains. |
| **Air / indoor air / bioaerosol** | MISO has `#Air` with `#Indoor air`/`#Outdoor air` as separate tags. The medium, not the deposit. |
| **Natural terrestrial/desert dust** | MISO tag 315, a *different* tag under `#Environmental > #Terrestrial`. Same English word, different bin. |
| **Volcanic ash in situ / tephra** | MISO files this under `#Environmental > #Terrestrial > #Volcanic`. A real habitat with its own literature (§3.6), but not this concept. |
| **`habitatmech:GOLD.398aeb6c37` and `habitatmech:GOLD.b1230bf984` (both "Dust")** | GOLD's indoor-air and built-environment dust records. They are the *indoor dust* concept; this bin is broader on one axis (includes ash) and narrower on another (BacDive's own `#Built environment > #House` tag, which strain 8468 also carries, is where GOLD's concept lands). Do not merge. |
| **PM2.5 / PM10** | Regulatory size fractions of *suspended* matter. |
| **Soot (`ENVO:03000021`) / charcoal (`ENVO:01000560`) / biochar / slag (`ENVO:02000130`)** | Related combustion products; each a possible member, none the concept. |
| **Ash-amended or post-fire soil** | The habitat is soil. |
| **House dust mite (*Dermatophagoides*) and its allergens** | An arthropod found in dust; "house dust allergy" usually means mite allergy. |
| **`ENVO:00002264` waste material** | Matches the MISO parent, not the samples. See §2. |

---

## 6. Should it be a term at all?

**The two halves are unquestionably microbial habitats.** Settled dust hosts a characterised, sampled community (Dannemiller et al. 2017 and the indoor-microbiome literature); ash supports genuine primary succession, biocrust formation, and selection for metal-resistant and PAH-degrading taxa (Davydov et al. 2025; Prakash & Lal 2006). Neither is a process, quality, disease state, taxon, nor a sampling artefact. Twenty strains across 16 taxa were deposited from them.

**But the *bin* is not a habitat kind — it is a vocabulary bucket.** The proposed sentence at the top is defensible, and a curator can write and cite it. What it cannot do is name a natural kind: nothing about house dust and thermal-power-station fly ash co-varies except "fine, dry, and left over". Their pH, carbon content, water activity, formation process and community signatures are all different (§3.4, §3.5). An ontology should not mint "dust or ash" as a class, and ENVO has not — it names both halves and their children separately (verified, §2).

So the honest disposition, in priority order:

1. **Keep `CONFIRM_UNGROUNDED`.** The existing decision is right and the new path evidence strengthens it. One correction to the note's premise: it says "no ontology term fits this concept", which is true of an identity match but overstated as a whole — `ENVO:01000814` **solid environmental material** is genuinely broader than both halves and is in the slice. If the note is ever revised, that is the sentence to add.

2. **Do not raise an ENVO term request.** This is a disjunction, and a term request for it would be rejected — correctly. It is the one case where "no term exists" is not a gap in ENVO.

3. **Attach both halves as `relation: xref`, not `parent`.** `ENVO:00002008` dust and `ENVO:02000090` ash are each *narrower* than the bin, so neither belongs in `parent_habitats` under this repo's "broader" rule. Two xrefs record exactly what the source lumped, without asserting either identity. This is the same shape as the `anthropogenic contamination feature` case in #99.

4. **Optionally add `ENVO:01000814` as `parent_habitats` (relation: parent).** Defensible and checkable; also very weak, since it admits soil and rock. A curator who thinks that is not worth asserting should leave `parent_habitats` empty and say so — that is a judgement call, not an error either way.

5. **Two things to file as issues, not to fix in the definition:**
   - **`habitat_category: OTHER` contradicts the source.** MISO's cat1 for tag 308 is `#Engineered`, and its cat2 is `#Waste`; the record's siblings under that parent (`Industrial waste`, `Sewage-sludge`, `Waste-gas`, `Solid-waste`) are already `ENGINEERED` in this corpus. `ENGINEERED` looks like the category the source actually supports.
   - **Two MISO tags appear to be missing from `data/raw/bacdive_isolation_sources.tsv`:** `#Dust` (id 315, `#Environmental > #Terrestrial`) and `#Air` (cat2 id 13, with `#Indoor air`/`#Outdoor air`). I verified those tags exist in MISO; I did **not** verify they carry strains in kg-microbe's slice, so this may be legitimate rather than a gap. Worth one check of the extractor, because if it is a gap, the corpus is currently attributing all BacDive dust to the engineered-waste bin.

6. **The real fix is upstream, and worth recording:** BacDive holds free-text sample type per strain ("house dust", "fly ash dumping site"), which is exactly the information needed to split this bin into two well-grounded records — `ENVO:00002008` dust and `ENVO:02000090` ash, both already in the slice, both `EXACT`. If HabitatMech ever ingests strain-level isolation-source text rather than tag-level counts, this record dissolves into two grounded ones and the definition above becomes unnecessary. That is a better outcome than defining the bucket.

---

**Sources:** [BacDive isolation sources](https://bacdive.dsmz.de/isolation-sources) · [BacDive strain 8468](https://bacdive.dsmz.de/strain/8468) · [OLS4 / ENVO](https://www.ebi.ac.uk/ols4/ontologies/envo) · [Tsukamura et al. 1983](https://doi.org/10.1099/00207713-33-4-811) · [Busse et al. 2003](https://doi.org/10.1099/ijs.0.02461-0) · [Prakash & Lal 2006](https://doi.org/10.1099/ijs.0.64080-0) · [Prakash et al. 2007](https://doi.org/10.1099/ijs.0.64456-0) · [García-Fraile et al. 2007](https://doi.org/10.1099/ijs.0.64680-0) · [Goodfellow et al. 2001](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-51-1-187) · [Davydov et al. 2025](https://doi.org/10.3390/microorganisms13081762) · [Kolaghat metagenomics 2025](https://doi.org/10.1007/s11356-025-36520-2) · [Fly-ash arsenic bioremediation 2018](https://doi.org/10.1007/s00128-018-2428-z) · [Volcanic SO₂ pioneers 2016](https://doi.org/10.1038/srep19687) · [Witt et al. 2017](https://doi.org/10.1111/gbi.12231) · [Dannemiller et al. 2017](https://doi.org/10.1111/ina.12313) · [Bagassosis, StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK554444/) · [Farmer's Lung, StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK557580/) · [ASM: Microbiology of Wildfires](https://asm.org/articles/2021/april/the-microbiology-of-wildfires) · [BacDive 2022, NAR](https://doi.org/10.1093/nar/gkab961) · [BacDive 2025, NAR](https://academic.oup.com/nar/article/53/D1/D748/7848838)

## Citations

1. https://bacdive.dsmz.de/isolation-sources
2. https://bacdive.dsmz.de/strain/8468
3. https://doi.org/10.1099/ijs.0.64080-0
4. https://pubmed.ncbi.nlm.nih.gov/16957112/
5. https://doi.org/10.1099/ijs.0.64456-0
6. https://pubmed.ncbi.nlm.nih.gov/17329778/
7. https://doi.org/10.1099/00207713-33-4-811
8. https://doi.org/10.1099/ijs.0.02461-0
9. https://pubmed.ncbi.nlm.nih.gov/13130003/
10. https://doi.org/10.1099/ijs.0.64680-0
11. https://pubmed.ncbi.nlm.nih.gov/17392217/
12. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-51-1-187
13. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002008
14. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01000701
15. https://doi.org/10.1111/ina.12313
16. https://doi.org/10.3390/microorganisms13081762
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC12388845/
18. https://asm.org/articles/2021/april/the-microbiology-of-wildfires
19. https://doi.org/10.1007/s00128-018-2428-z
20. https://www.ncbi.nlm.nih.gov/books/NBK554444/
21. https://www.ncbi.nlm.nih.gov/books/NBK557580/
22. https://doi.org/10.1007/s11356-025-36520-2
23. https://doi.org/10.1038/srep19687
24. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4726209/
25. https://doi.org/10.1111/gbi.12231
26. https://pubmed.ncbi.nlm.nih.gov/28256065/
27. https://www.ebi.ac.uk/ols4/
28. http://environmentontology.org/
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC3904460/
30. https://doi.org/10.1093/nar/gkab961
31. https://academic.oup.com/nar/article/53/D1/D748/7848838
32. https://www.ebi.ac.uk/ols4/ontologies/envo