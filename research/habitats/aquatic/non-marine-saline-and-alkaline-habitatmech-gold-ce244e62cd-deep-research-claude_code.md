---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T20:21:47.893045'
end_time: '2026-08-17T20:30:34.998273'
duration_seconds: 527.11
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Non-marine Saline and Alkaline
  habitat_identifier: habitatmech:GOLD.ce244e62cd
  habitat_category: AQUATIC
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Environmental > Aquatic > Non-marine Saline and Alkaline'
  assertions: '121'
  parent_terms: ENVO:00002030
  xrefs: (none)
  decision_note: 'Reviewed and endorsed the seeder''s own resolution. xref-only review
    (#43): a quality is a property of a habitat rather than a habitat, the call already
    recorded for Acidic, Humid and Arid. The xref also drops the saline half of the
    source. (source concept habitatmech:GOLD.ce244e62cd)'
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
  num_turns: 28
  total_cost_usd: 3.0729685
  session_id: 0a71a20d-3990-4ddf-890a-750e9f9f73c4
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 21
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Non-marine Saline and Alkaline
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.ce244e62cd
- **Category:** AQUATIC
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Environmental > Aquatic > Non-marine Saline and Alkaline
- **Upstream assertion volume:** 121
- **Nearest broader term already on the record:** ENVO:00002030
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Reviewed and endorsed the seeder's own resolution. xref-only review (#43): a quality is a property of a habitat rather than a habitat, the call already recorded for Acidic, Humid and Arid. The xref also drops the saline half of the source. (source concept habitatmech:GOLD.ce244e62cd)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Non-marine Saline and Alkaline** as a microbial habitat, with citations.

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

# Non-marine Saline and Alkaline — definition research

**Concept:** `habitatmech:GOLD.ce244e62cd` · GOLD `Environmental > Aquatic > Non-marine Saline and Alkaline` · AQUATIC · UNGROUNDED · 121 organism assertions at the node

---

## Proposed definition

> **An aquatic environment which is determined by an inland water body whose water is substantially more saline than fresh water (conventionally > 3 g L⁻¹ total dissolved solids), substantially more alkaline than circumneutral water (pH ≳ 9), or both.**

A one-sentence definition is achievable here, but only for the *intended* reading of the label. Two caveats the curator has to decide on before writing it — both detailed in §1 and §6:

1. The concept is a **disjunction of two independent physicochemical axes** (salinity ∨ alkalinity). That is a legitimate grouping class but not a clean Aristotelian species, and it is the reason no ENVO term matches: ENVO models the two axes separately (`ENVO:01001040` saline environment, `ENVO:01000316` alkaline environment) and has no union of them.
2. GOLD's own children of this node **violate the "non-marine" qualifier** (salt marsh, solar salterns, an explicit `Thalassic` subtype). The definition above states what the label means; a scope note should record that the source bin is looser.

---

## 1. What the concept denotes

### The reading the data supports

GOLD's five-level ecosystem classification (Ecosystem → Ecosystem Category → Ecosystem Type → Ecosystem Subtype → Specific Ecosystem) places this concept at **level 3, Ecosystem Type**, as one of ten types under `Environmental > Aquatic` ([JGI GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification); [Mukherjee et al. 2019, GOLD v.7, *Nucleic Acids Res* 47:D649–D659, PMID 30357420](https://pubmed.ncbi.nlm.nih.gov/30357420/); [Mukherjee et al. 2021, GOLD v.8, PMID 33152092](https://pubmed.ncbi.nlm.nih.gov/33152092/)). Its siblings in `data/raw/gold_ecosystem_paths.tsv` are Freshwater (2,055), Marine (6,420), Thermal springs (744), Aquaculture, Deep subsurface, Acidic, Artesian spring, Floodplain, Pit lake.

So the node is **the third partition of aquatic environments by water chemistry**, sitting alongside Freshwater and Marine. Its own children (from `data/raw/gold_ecosystem_paths.tsv`, organism counts) show unambiguously what a sample filed here is taken from:

| Subtype | Organisms | Specific ecosystems below it |
|---|---:|---|
| Hypersaline | 219 | Sediment (159), Microbial mats (9), Salt flat/Salt pan (6), Salt flat sediment (4), Microbialites (0) |
| Saline | 150 | Sediment (37), Microbial mats (7), Epilimnion (2), Thalassic (1), Athalassic (0), Hypolimnion (0) |
| Hypersaline lake | 115 | Sediment (85), Sediment–water interface (1), Microbial mats, Microbialites, Salt crust (0) |
| Salt crystallizer ponds | 103 | Microbial mats (1), Saline water (0) |
| Lake | 75 | Brine (100), Sediment (30) |
| Saline lake | 58 | Sediment (43), Microbial mats, Ice core (0) |
| Soda lake | 52 | Sediment (91), Microbial mats (7) |
| Alkaline | 6 | Sediment (47), Carbonate (12), Microbial mats (1), Mine pit pond (0) |
| Hypersaline soda lake | 29 | Sediment (31), Microbial mats (2), Microbialites (0) |
| Solar solterns | 30 | Sediment (12) |
| Salt marsh | 16 | Sediment (0) |
| Sub-saline lake, Hypersaline spring, Fracking water, Biofouling, Near-boiling (>90C) | 0–2 each | — |

Summed over all paths in the subtree, ≈**1,660 organism assertions** (my arithmetic over the per-path counts; within GOLD the unit is uniform and each project carries one leaf path, so the sum is meaningful — it must not be added to BacDive or PREGO counts).

**What a sample from this concept is:** the water column, brine, bottom sediment, microbial mat, microbialite or evaporite/salt crust of an inland lake, pond, pan, spring or artificial evaporation basin whose water is saline, alkaline, or both. Note that the concept is *not* restricted to the water itself — over half the organism assertions in the subtree come from `Sediment`, `Microbial mats`, `Microbialites` and `Salt crust` specific-ecosystems. A definition scoped strictly to "a body of water" would exclude the majority of the data filed here; hence "an aquatic environment which is determined by an inland water body" rather than "a saline water body."

### Where the boundary falls

**Inside:** soda/alkaline lakes (Mono Lake, Lake Magadi, Kulunda Steppe lakes), hypersaline lakes (Great Salt Lake, Dead Sea, Lake Chaka, Lake Barkol), athalassic salt lakes and salt pans/playas, saline springs, salt-crystallizer ponds and solar salterns, alkaline flats, brines and salt crusts, and the sediments and mats of all of these.

**Neighbouring concepts, outside:**
- **Marine** (`Environmental > Aquatic > Marine`, `ENVO:00001999` marine water body) — sibling ecosystem type; the open sea and its coastal margin.
- **Freshwater** (sibling; `ENVO:00002011` fresh water) — the concept's complement on the salinity axis.
- **Thermal springs** (sibling) — though GOLD files `Near-boiling (>90C) > Alkaline` under *this* node, a scope leak.
- **Deep subsurface** (sibling) — deep saline aquifer brines are filed there, not here.
- **Saline soils** — GOLD files these under `Environmental > Terrestrial > Soil`; ENVO has `ENVO:00002255` solonetz for the alkaline sodic case.
- **Marine brine pools** (`ENVO:00000369`) — hypersaline but on the ocean floor; marine.

### Ambiguity — three readings, and they do not coincide

The label is genuinely ambiguous and the curator must not pick silently.

**(a) Geographic reading — "inland / continental, i.e. not the sea."** This is what the label's contrast with the Marine and Freshwater siblings implies, and it is what most of the children instantiate. This is the reading the proposed definition takes.

**(b) Chemical reading — "athalassohaline," i.e. ionic composition not derived from seawater.** This is the standard microbiological distinction: hypersaline environments divide into *thalassohaline* (marine-derived; Na⁺/Cl⁻-dominated, ionic ratios like seawater — solar salterns, Great Salt Lake) and *athalassohaline* (ionic proportions unlike seawater, reflecting the local geology — Dead Sea, dominated by Mg²⁺ and Ca²⁺; soda lakes, dominated by Na⁺ and CO₃²⁻/HCO₃⁻) ([Oren 2002, *J Ind Microbiol Biotechnol* 28:56–63, doi:10.1038/sj/jim/7000176, PMID 11938472](https://academic.oup.com/jimb/article/28/1/56/5989526); Hammer 1986, *Saline Lake Ecosystems of the World*, Junk, Dordrecht). GOLD encodes this distinction as two *specific ecosystems* under `Saline` — `Athalassic` and `Thalassic` — which is direct evidence that GOLD does **not** intend "non-marine" to mean "athalassohaline": if it did, `Thalassic` could not be a child.

The two readings are demonstrably not equivalent. Lake Meyghan (Iran), an inland lake, was found to have thalassohaline composition ([Naghoni et al. 2017, *Sci Rep* 7:11522, doi:10.1038/s41598-017-11585-3](https://www.nature.com/articles/s41598-017-11585-3)), and Dziani Dzaha (Mayotte) is a thalassohaline *alkaline crater lake* ([Hugoni et al. 2018, *Sci Rep*, PMID 30346079](https://pubmed.ncbi.nlm.nih.gov/30346079/); [Leboulanger et al. 2017, *PLOS ONE* 12(1):e0168879](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0168879)). **Do not write "athalassohaline" into the definition** — it would assert an ionic-composition claim about every sample filed under this node that neither GOLD nor the underlying studies support.

**(c) What the bin actually holds.** Beyond (a) and (b), GOLD files under this node several things that are neither inland nor athalassohaline: `Salt marsh` (coastal, tidal, seawater-fed), `Solar solterns` and `Salt crystallizer ponds` (seawater-fed evaporation ponds — the textbook thalassohaline system, per Oren 2002), `Fracking water` (anthropogenic brine, arguably ENGINEERED), and `Near-boiling (>90C)` (thermal, duplicating a sibling type). These are best recorded as a scope note plus per-child decisions, not folded into the definition. HabitatMech has already grounded `Salt marsh` to `ENVO:00000054` saline marsh (EXACT) and `Salt crystallizer ponds`-adjacent concepts independently, so the leaks are already handled at the child level.

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01000317` *aquatic environment*** — "An environment whose dynamics are strongly influenced by water." This is the smallest existing ENVO class that covers the whole node: water column, sediment, mat and crust alike, and both the saline and the alkaline halves.

If the curator prefers to keep the definition on the water-body axis and let the sediment/mat children hang off separately, the alternative genus is `ENVO:01001319` *saline water body* — but see the near-miss list; it is already the grounding target of this node's own child.

### Near-misses checked in ENVO (all rejected)

| CURIE | Label | Why it is not a match |
|---|---|---|
| `ENVO:00002030` | aquatic biome | **Current parent on the record.** A biome is defined by ecological climax communities; GOLD's node is a chemistry bin, not a biome, and its children include artificial crystallizer ponds and fracking water. Too broad *and* asserts biome-hood the source does not. Recommend replacing with `ENVO:01000317`. |
| `ENVO:01001040` | saline environment | Broader on one axis, narrower on the other: covers marine saline environments (does not carry "non-marine") and excludes non-saline alkaline waters. Also its parent `ENVO:01000314` high osmolarity environment brings in saline soils and aerosols. |
| `ENVO:01000307` | saline water environment | Same two failures as above, restricted to water. Includes all of Marine. |
| `ENVO:01001319` | saline water body | Same failures, **and already taken**: HabitatMech grounds `… > Saline` (this node's child, 150 organisms) to it as CLOSE. Grounding parent and child to the same term collapses them. |
| `ENVO:01001043` | hypersaline water environment | **Narrower** — hypersaline only; already the grounding for the child `… > Hypersaline` (219 organisms, CLOSE). Excludes soda lakes below seawater salinity and sub-saline lakes. |
| `ENVO:00000019` | saline lake | **Narrower** — lakes only, excluding springs, pans, salterns, marshes and flats; and not restricted to inland. Already the grounding for the child `… > Saline lake` (EXACT). |
| `ENVO:01001020` | hypersaline lake | Narrower still; already the natural target for `… > Hypersaline lake`. |
| `ENVO:00002121` | alkaline salt lake (syn. soda lake) | Narrower — one subtype (`… > Soda lake`), and conjoins saline ∧ alkaline where the node is saline ∨ alkaline. |
| `ENVO:01000316` | alkaline environment | Covers only the alkaline half, and is not aquatic-restricted (an alkaline environment can be a soil or a bioreactor). |
| `ENVO:01000357` | alkaline water | pH > 7 only — far too weak a threshold, and drops salinity entirely. |
| `ENVO:00000196` / `ENVO:00000279` | alkaline flat / saline pan | Narrower; these are dry lakebeds and would misdescribe the water-column children. |
| `ENVO:00000197` | endorheic lake | Captures the *formation process* most saline lakes share but is neither necessary (salterns, springs) nor sufficient (endorheic lakes can be fresh). Good candidate for a scope note or `relation: xref`, not the genus. |
| `ENVO:00000369` | brine pool | Marine (ocean-basin, salt-tectonic); asserts a setting the source contradicts. |

**Searched and absent from ENVO entirely** (OLS4 query against `envo`, 2026-08-17): *athalassohaline*, *athalassic*, *inland saline water*, *inland water body*, *saltern* (only `ENVO:00000055` saline evaporation pond, which asserts *man-made* and *from seawater*), *hypersaline environment* as such. There is no ENVO class for "inland water body" at all — `inland` returns only `inland cliff`, `inland sea`, `landlocked sea`. This is a real gap and supports minting.

**Reference vocabularies:** MIxS/GSC has no saline- or hypersaline-specific environmental package; the applicable packages are *water*, *sediment*, and *microbial mat/biofilm*, with habitat expressed through the ENVO triad rather than a package name ([Yilmaz et al. 2011, *Nat Biotechnol* 29:415–420, PMC3367316](https://pmc.ncbi.nlm.nih.gov/articles/PMC3367316/); [GSC extensions page](http://www.gensc.org//pages/standards/extensions.html)). So MIxS offers no competing term and no argument against minting.

---

## 3. Differentia

What separates this concept from Freshwater and Marine, its two siblings under the genus, in decreasing order of how well-supported each property is:

**(i) Salinity above the fresh/saline boundary — the primary, measurable differentia.** The conventional limnological threshold is **3 g L⁻¹ total dissolved solids** (Williams 1964, widely adopted by saline-inland-water limnologists; see [Britannica, *Inland water ecosystem — Saline lakes*](https://www.britannica.com/science/inland-water-ecosystem/Saline-lakes), which states that inland waters below 3 g L⁻¹ are conventionally regarded as fresh and that maxima reach ~350 g L⁻¹ where Na⁺/Cl⁻ dominate). A 1 g L⁻¹ threshold is also in use — [Boros & Kolpakova 2018, *PLOS ONE* 13(8):e0202205, doi:10.1371/journal.pone.0202205](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0202205) use 1.0 g L⁻¹ across 8 Eurasian countries. **State the threshold as "conventionally > 3 g L⁻¹" with the source, or omit the number and say "substantially elevated relative to fresh water"; do not present 3 g L⁻¹ as a fact without attribution.** GOLD's own `Sub-saline lake` subtype indicates the node's lower edge is deliberately soft.

**(ii) Carbonate alkalinity and elevated pH — the second, independent differentia.** Soda lakes are "natural sodium carbonate/bicarbonate-buffered systems with elevated pH values (9.5–11)", formed "in depressions where ground water rich in carbon dioxide, but poor in magnesium and calcium, leaches sodium from sodium-rich rocks", and are "found worldwide, predominantly in arid and semi-arid environments, such as the Rift Valley in East Africa, the rain-shadowed regions of California and Nevada, and the Kulunda Steppe in South Siberia" ([Sorokin et al. 2014, *Extremophiles* 18(5):791–809, doi:10.1007/s00792-014-0670-9, PMC4158274](https://pmc.ncbi.nlm.nih.gov/articles/PMC4158274/)). Boros & Kolpakova classify brines by ion dominance (>25 equivalent-%): *Soda* (Na⁺ and HCO₃⁻+CO₃²⁻ both dominant; mean pH 9.33, range 7.70–10.40), *Soda-Saline* (Na⁺ dominant, carbonate not; mean pH 9.33), *Saline* (carbonate < 25 e%; mean pH 8.40) — and warn that pH distributions overlap 49%, so **pH alone is not a reliable classifier**. Use "pH ≳ 9" as an indicative, not criterial, value, and cite Boros & Kolpakova for the caveat.

**(iii) Not part of the sea — the "non-marine" qualifier.** This is the differentia that distinguishes the concept from marine and coastal hypersaline systems, and it is the one the source's own children partly violate (§1c). It is defensible as the label's stated intent; it is *not* defensible as a claim about every sample filed there.

**(iv) Formation setting — supporting, not criterial.** Saline lakes occur mostly in hydrologically closed (endorheic) basins in semi-arid (200–500 mm yr⁻¹) or arid (25–200 mm yr⁻¹) zones, concentrated in belts between 20° and 40° latitude in both hemispheres, on all continents including Antarctica; roughly a tenth of Earth's land surface drains endorheically (Britannica, *Saline lakes*, as above; Williams, *Saline Inland Waters*). Evaporation exceeding inflow is the general mechanism. Do not put this in the definition — salterns and springs break it — but it belongs in a scope note.

**(v) Characteristic biota — corroborating context, not a differentia.** Salinity and alkalinity together impose a strong, well-documented selection: soda lakes are "the only natural environment suitable for stable development of obligately alkaliphilic, salt-tolerant microorganisms," which typically grow optimally near pH 10 and require ≥ 0.1 M Na⁺ ([Sorokin & Kuenen 2005, *FEMS Microbiol Rev* 29(4):685–702](https://academic.oup.com/femsre/article/29/4/685/492583)); above ~25% (w/v) NaCl, communities are dominated by the class *Halobacteria* (Oren 2002). Athalassohaline systems in particular behave as isolated islands with divergent communities and are a rich source of novel taxa ([Demergasso et al. 2004, *FEMS Microbiol Ecol* 48:57–69, PMID 19712431](https://academic.oup.com/femsec/article/48/1/57/559077)); e.g. Sambhar Lake salterns are dominated by uncultivated Woesearchaeota (90–94%) and Nanohaloarchaeota ([Mani et al. 2020, *Extremophiles* 24:875–885](https://link.springer.com/article/10.1007/s00792-020-01201-0)); see also [Lake Chaka, PMC1489620](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1489620/) and [Lake Barkol MAGs 2025, PMC12174138](https://pmc.ncbi.nlm.nih.gov/articles/PMC12174138/). **A definition should not name organisms** — ENVO's own convention — but this material justifies the concept's standing as a distinct habitat.

**Scale (context for the term's warrant, not part of the definition):** saline lakes account for roughly 23% of the surface area and ~44% of the volume of all lakes on Earth, with global saline lake volume estimated at ~85,000 km³ (Tweed et al. 2011) — comparable to the world's freshwater lakes. These figures are quoted from secondary syntheses ([ScienceDirect Topics, *Inland Saline Lakes*](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/inland-saline-lakes); [Boros et al., *The overlooked conservation value and ecosystem services of saline lakes*, preprint doi:10.21203/rs.3.rs-5835171/v1](https://www.researchsquare.com/article/rs-5835171/v1)); the underlying HydroLAKES paper ([Messager et al. 2016, *Nat Commun* 7:13603, PMC5171767](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5171767/)) reports global lake totals (2.67 × 10⁶ km², 181.9 × 10³ km³) without a saline breakdown, so **the 23%/44% split should be cited to the secondary source, not to Messager directly**. The volume figure is also heavily leveraged by the Caspian Sea alone; area is the better proxy for habitat extent.

---

## 4. Sources

Primary literature and reference works, ordered as used above.

| Claim | Source |
|---|---|
| GOLD five-level ecosystem classification; this node is an Ecosystem Type under Environmental > Aquatic | [gold.jgi.doe.gov/ecosystem_classification](https://gold.jgi.doe.gov/ecosystem_classification); [gold.jgi.doe.gov/ecosystemtree](https://gold.jgi.doe.gov/ecosystemtree); [Mukherjee et al. 2019 *NAR* 47:D649, PMID 30357420](https://pubmed.ncbi.nlm.nih.gov/30357420/); [Mukherjee et al. 2021 *NAR* 49:D723, PMID 33152092](https://pubmed.ncbi.nlm.nih.gov/33152092/); Mukherjee et al. 2024, GOLD v.10, *NAR* |
| Node's children, subtypes and counts | `data/raw/gold_ecosystem_paths.tsv` (this repo, from the kg-microbe extraction) |
| Thalassohaline vs athalassohaline distinction; ionic composition; *Halobacteria* above 25% NaCl | [Oren 2002, *J Ind Microbiol Biotechnol* 28:56–63, doi:10.1038/sj/jim/7000176, PMID 11938472](https://academic.oup.com/jimb/article/28/1/56/5989526); Oren 2002, *Halophilic Microorganisms and their Environments*, Kluwer |
| Athalassic vs thalassic ionic variability | Hammer 1986, *Saline Lake Ecosystems of the World*, Dr W. Junk, Dordrecht (ISBN 90-6193-535-0) |
| Soda lake chemistry, pH 9.5–11, formation, geography, salinity classes | [Sorokin et al. 2014, *Extremophiles* 18(5):791–809, doi:10.1007/s00792-014-0670-9, PMC4158274](https://pmc.ncbi.nlm.nih.gov/articles/PMC4158274/) |
| Obligate alkaliphiles require pH ~10 and ≥0.1 M Na⁺ | [Sorokin & Kuenen 2005, *FEMS Microbiol Rev* 29(4):685–702](https://academic.oup.com/femsre/article/29/4/685/492583) |
| Ion-dominance classification of soda/soda-saline/saline brines; pH unreliable alone; 1 g L⁻¹ threshold | [Boros & Kolpakova 2018, *PLOS ONE* 13(8):e0202205, doi:10.1371/journal.pone.0202205](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0202205) |
| 3 g L⁻¹ fresh/saline boundary; endorheic basins; 20–40° latitude belts | [Britannica, *Inland water ecosystem — Saline lakes*](https://www.britannica.com/science/inland-water-ecosystem/Saline-lakes); Williams 1964, and Williams, *Saline Inland Waters* (in *Encyclopedia of Inland Waters*) |
| Inland lake with thalassohaline chemistry (reading (b) fails) | [Naghoni et al. 2017, *Sci Rep* 7:11522, doi:10.1038/s41598-017-11585-3](https://www.nature.com/articles/s41598-017-11585-3) |
| Thalassohaline *alkaline* lake (Dziani Dzaha) | [Leboulanger et al. 2017, *PLOS ONE* 12(1):e0168879](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0168879); [Hugoni et al. 2018, PMID 30346079](https://pubmed.ncbi.nlm.nih.gov/30346079/) |
| Athalassohaline lakes as isolated, novel-taxon-rich systems | [Demergasso et al. 2004, *FEMS Microbiol Ecol* 48:57–69](https://academic.oup.com/femsec/article/48/1/57/559077); [Jiang et al., Lake Chaka, PMC1489620](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1489620/); [Mani et al. 2020, *Extremophiles* 24:875–885](https://link.springer.com/article/10.1007/s00792-020-01201-0); [Xamxidin et al. 2025, Lake Barkol, PMC12174138](https://pmc.ncbi.nlm.nih.gov/articles/PMC12174138/) |
| MIxS environmental packages; no saline/hypersaline package | [Yilmaz et al. 2011, *Nat Biotechnol* 29:415–420, PMC3367316](https://pmc.ncbi.nlm.nih.gov/articles/PMC3367316/); [GSC extensions](http://www.gensc.org//pages/standards/extensions.html) |
| Saline lakes ≈23% of lake area, ≈44% of lake volume; ~85,000 km³ | [ScienceDirect Topics, *Inland Saline Lakes*](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/inland-saline-lakes); [Boros et al. preprint, doi:10.21203/rs.3.rs-5835171/v1](https://www.researchsquare.com/article/rs-5835171/v1) — secondary; underlying lake totals in [Messager et al. 2016, *Nat Commun* 7:13603](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5171767/) |
| ENVO term labels, definitions, absence of *athalassohaline*/*inland saline* | EBI OLS4 API against `envo`, queried 2026-08-17; and `data/raw/ontology_terms.tsv` (vendored slice) |

**Explicitly my inference, not stated by any source:**
- That GOLD's "non-marine" qualifier means *geographic*, not *athalassohaline*. Inferred from GOLD's placement of `Thalassic` and `Athalassic` as coordinate specific-ecosystems beneath `Saline` within this node — strong evidence, but GOLD publishes no definition of the node.
- That the concept is a disjunction (saline ∨ alkaline) rather than a conjunction. Inferred from the coexistence of the `Saline` and `Alkaline` subtypes as siblings alongside the conjunctive `Hypersaline soda lake`.
- That `ENVO:01000317` is the smallest existing covering class. Inferred from the near-miss review; ENVO's hierarchy was inspected, not exhaustively proved minimal.
- The ≈1,660-assertion subtree total is my arithmetic over the repo's raw table, not an upstream figure.

---

## 5. Synonyms, and what not to conflate

### Names in real use for approximately this concept
- **inland saline waters** / **saline inland waters** — the standard limnological term (Williams; Boros & Kolpakova use "inland saline surface waters"). Closest natural-language equivalent; recommended as the primary exact synonym.
- **continental saline waters**
- **saline and alkaline lakes** / **saline–alkaline lakes** — common in the microbiology literature for the same grouping
- **athalassic saline waters** — Hammer's term; **related, not exact** (chemical criterion, see §1b). Safe as a *related* synonym only.
- **non-marine saline and alkaline** — the GOLD string itself; record as the source label.

### Commonly but wrongly treated as the same thing
- **athalassohaline environment** — a chemistry claim, not a geography claim; inland lakes can be thalassohaline (Lake Meyghan, Dziani Dzaha). Do not use as an exact synonym.
- **hypersaline environment** (`ENVO:01001043`) — overlaps but is neither broader nor narrower: excludes sub-saline and moderately saline lakes, includes marine brine pools and seawater-fed salterns.
- **saline lake** (`ENVO:00000019`) / **soda lake** (`ENVO:00002121`) / **hypersaline lake** (`ENVO:01001020`) — all strictly narrower; each is already a separate HabitatMech record grounded to its own ENVO term.
- **solar saltern / salt evaporation pond** (`ENVO:00000055`) — GOLD files these here, but they are seawater-fed and thalassohaline by definition; ENVO's term additionally asserts *man-made*.
- **salt marsh** (`ENVO:00000054`) — coastal and tidal; GOLD's placement here is a scope leak, already grounded EXACT on its own record.
- **marine brine pool** (`ENVO:00000369`) — marine.
- **saline/sodic soil**, **solonetz** (`ENVO:00002255`), **solonchak** — terrestrial; GOLD puts them under Terrestrial > Soil.
- **alkaline hot spring** (`ENVO:00002119`) — GOLD has a separate `Thermal springs` ecosystem type; the `Near-boiling (>90C)` child here duplicates it.
- **deep saline aquifer / formation brine / produced water** — GOLD's `Deep subsurface` sibling; the `Fracking water` child here is anthropogenic and arguably ENGINEERED.
- **alkaline as a quality** — `PATO:0001430` *alkaline*, and pH values generally. This is the trap the existing curation note fell into; see §6.

---

## 6. Should this be a term at all? — Yes, and I disagree with the recorded review

**Yes. This is a place, and it should be a term-request candidate, not `NOT_APPLICABLE` and not left UNGROUNDED under a biome.**

The recorded decision reads:

> xref-only review (#43): a quality is a property of a habitat rather than a habitat, the call already recorded for Acidic, Humid and Arid. The xref also drops the saline half of the source.

That reasoning is correct for the concept it was written about, but it has been applied one level too high. `Acidic`, `Humid`, `Arid` and this node's own child `Alkaline` (`habitatmech:GOLD.94b8786010`, `NOT_APPLICABLE`) are bare adjectives whose only content is a quality. **This node is not.** Its label is a compound noun phrase naming a partition of aquatic environments — coordinate with `Freshwater` (grounded EXACT to `ENVO:00002011`) and `Marine` (grounded EXACT to `ENVO:00001999`) — and it has 31 sub-paths that are unambiguously places: lakes, ponds, springs, marshes, flats, sediments, mats, crusts. A sample can be taken from it. `NOT_APPLICABLE` would be the same over-claim that #114 documented for host taxa, in the opposite direction: it says "this concept is not a habitat," which is false of a bin holding ≈1,660 organism assertions from Great Salt Lake, Mono Lake and Lake Magadi.

The note itself flags the problem — "the xref also drops the saline half of the source" — which is precisely the symptom of treating a two-axis grouping class as if it were the single quality named in half of its label.

**Concrete recommendations, in priority order:**

1. **Mint / request a term** for `inland saline or alkaline aquatic environment`, using the definition at the top. This is a real ENVO gap: OLS4 returns nothing for *athalassohaline*, *inland saline water* or *inland water body*, and the union of the salinity and alkalinity axes is unmodelled. Per this repo's standing rule, an ENVO term request needs explicit per-request permission before submission.
2. **Change `parent_habitats` from `ENVO:00002030` (aquatic biome) to `ENVO:01000317` (aquatic environment).** A biome asserts ecological climax communities; this node includes crystallizer ponds and fracking water. This is a small, well-supported correction independent of whether the term request goes ahead.
3. **Add `relation: xref` links, not parents**, to `ENVO:01001040` *saline environment* and `ENVO:01000316` *alkaline environment* — the two axes ENVO does model. Neither is broader than the concept (each covers only one axis and neither is inland-restricted), so neither belongs in `parent_habitats`; this is exactly the `xref` case #99 established.
4. **Record a scope note** that GOLD files `Salt marsh`, `Solar solterns`, `Salt crystallizer ponds`, `Near-boiling (>90C)` and `Fracking water` under this node in contradiction of the "non-marine" qualifier, and that these are decided independently at the child level.
5. **Consider whether the disjunction warrants splitting.** If a single ENVO class covering "saline ∨ alkaline ∧ inland" is judged unsatisfactory, the alternative is two requests — *inland saline water environment* and *inland alkaline water environment* — with this record retained as a HabitatMech grouping over both. Per the output instruction: the fact that one clean sentence requires a disjunction is itself the signal that ENVO is missing an intermediate class, and saying so is more useful than stretching the sentence.

## Citations

1. https://gold.jgi.doe.gov/ecosystem_classification
2. https://pubmed.ncbi.nlm.nih.gov/30357420/
3. https://pubmed.ncbi.nlm.nih.gov/33152092/
4. https://academic.oup.com/jimb/article/28/1/56/5989526
5. https://www.nature.com/articles/s41598-017-11585-3
6. https://pubmed.ncbi.nlm.nih.gov/30346079/
7. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0168879
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC3367316/
9. http://www.gensc.org//pages/standards/extensions.html
10. https://www.britannica.com/science/inland-water-ecosystem/Saline-lakes
11. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0202205
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC4158274/
13. https://academic.oup.com/femsre/article/29/4/685/492583
14. https://academic.oup.com/femsec/article/48/1/57/559077
15. https://link.springer.com/article/10.1007/s00792-020-01201-0
16. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1489620/
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC12174138/
18. https://www.sciencedirect.com/topics/earth-and-planetary-sciences/inland-saline-lakes
19. https://www.researchsquare.com/article/rs-5835171/v1
20. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5171767/
21. https://gold.jgi.doe.gov/ecosystemtree