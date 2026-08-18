---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:15:00.580791'
end_time: '2026-08-17T16:22:26.415811'
duration_seconds: 445.84
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Environmental
  habitat_identifier: habitatmech:GOLD.c3fa7fc4c2
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Environmental'
  assertions: '1285'
  parent_terms: (none)
  xrefs: ENVO:01000951
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Nearest
    broader term ENVO:01000951 ''natural environment'' attached as a parent. Term-request
    re-check (#12), after ENVO:01001000 showed these claims were never machine-rechecked:
    GOLD''s top-level Environmental bin, same near-miss as BacDive''s and for a sharper
    reason: GOLD files Terrestrial > Soil > Tree plantation under it, and a plantation
    is not an environment where ''minimal to no anthropisation has occurred''. Kept
    as an xref. Still a term request. (source concept habitatmech:GOLD.c3fa7fc4c2)'
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
  web_search_requests: 7
  num_turns: 28
  total_cost_usd: 2.615516
  session_id: 54a5efbf-8bca-4284-930a-c96ecd02ea54
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 34
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Environmental
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.c3fa7fc4c2
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Environmental
- **Upstream assertion volume:** 1285
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** ENVO:01000951

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:01000951 'natural environment' attached as a parent. Term-request re-check (#12), after ENVO:01001000 showed these claims were never machine-rechecked: GOLD's top-level Environmental bin, same near-miss as BacDive's and for a sharper reason: GOLD files Terrestrial > Soil > Tree plantation under it, and a plantation is not an environment where 'minimal to no anthropisation has occurred'. Kept as an xref. Still a term request. (source concept habitatmech:GOLD.c3fa7fc4c2)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Environmental** as a microbial habitat, with citations.

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

# Definition research — `habitatmech:GOLD.c3fa7fc4c2` "Environmental"

> **An** *environmental system* (`ENVO:01000254`) **which** is a portion of the air, water, or land surface and subsurface of an astronomical body, sampled in place, and which is neither bounded by a host organism nor constituted by a constructed or operated artefact.

The definition deliberately says nothing about human influence, because the GOLD bin it describes does not. That silence is the whole point and it will be misread unless it is stated in a comment, so:

> *Comment:* Anthropisation is orthogonal to this class. GOLD files managed and contaminated land, indoor air, and mine water under `Environmental`; what moves a sample out of the bin is being *inside a host* or *being an artefact*, not being human-affected.

**The missing intermediate class is the complement of `ENVO:01001000`** — a "free-living / non-host-determined environment" sibling that does not carry `natural environment`'s anthropisation restriction. ENVO has positive classes for the two things this bin excludes and no class for what it includes. Saying that to ENVO is more useful than a longer sentence.

---

## 0. Two things to fix on the record before writing anything

### 0.1 The note's evidence is correct but is the weakest instance available

The recorded note says GOLD files `Terrestrial > Soil > Tree plantation` under `Environmental`. **Verified** — that path exists in `data/raw/gold_ecosystem_paths.tsv` with 159 organism assertions. But it is the 6th-strongest example. The strongest, by an order of magnitude:

| GOLD path under `Environmental` | assertions |
|---|---|
| `Terrestrial > Soil > Garden` | **5,014** |
| `Terrestrial > Soil > Greenhouse` | **698** |
| `Terrestrial > Soil > Unclassified > Agricultural land` | 364 |
| `Terrestrial > Agricultural field` | 226 |
| `Terrestrial > Geologic > Mine` | 218 |
| `Terrestrial > Soil > Tree plantation` | 159 |
| `Terrestrial > Soil > Paddy field/soil` | 133 |
| `Terrestrial > Soil > Unclassified > Contaminated` | 129 |
| `Air > Indoor Air` (+ `> Dust` 65, `> Cattle barn` 5, `> Poultry farm` 3, `> Composting facility` 1) | 72 |
| `Terrestrial > Soil > Contaminated > Pesticide` / `> Uranium contaminated` | 9 / 3 |

If the note is ever rewritten, `Garden` (5,014) and `Greenhouse` (698) make the case that `Tree plantation` (159) only gestures at. All figures from `data/raw/gold_ecosystem_paths.tsv`, `total_assertions` column, `assertion_unit: ORGANISM`.

### 0.2 The near-miss is sharper than "narrower" — the bin *cross-cuts* ENVO's partition

The note calls `ENVO:01000951` a near-miss. It is worse than that, and the sharper statement is checkable in the vendored slice:

- `cultivated environment` (`ENVO:01000311`) is `rdfs:subClassOf` **`anthropogenic environment`** (`ENVO:01000313`) — verified in `data/raw/ontology_subclass_edges.tsv`, and `ENVO:01000311`'s definition is *"A cultivated environment is an environment that has been modified by humans by the preparation of the land, usually for the purposes of growing crops"* ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01000311), retrieved 2026-08-17), synonyms including *cropland*, *market garden*, *cultivated area*.
- `anthropogenic environment` and `natural environment` are **siblings**, both direct `rdfs:subClassOf ENVO:01000254` (verified in the same file).

So GOLD's `Agricultural field`, `Paddy field/soil`, `Garden` and `Orchard` sit inside `Environmental` *and* inside ENVO's `anthropogenic environment` branch. The bin is therefore **not narrower than `natural environment`; it properly overlaps both `natural environment` and its complement.** That is a stronger reason to reject the grounding, and it also rules out `anthropogenic environment` as a fallback.

**And it cross-cuts the third sibling too.** `Environmental` contains organism-built structures: `Terrestrial > Nest > Insects nest > Fungus garden/Fungus gallery` (77), `Terrestrial > Plant litter` (55), `Terrestrial > Nest > Chelicerates nest` (13), `> Spider web` (12), `Aquatic > Marine > Intertidal zone > Coral reef` (6), `Nest > Insects nest > Beehive: Honey` (2), `Nest > Alligator nest`, `Nest > Rodent burrow`. Each of these is arguably *determined by a living organism* in the sense of `ENVO:01001000`. **This last point is my reading of ENVO's definition applied to GOLD's paths, not a claim either source makes** — but the paths themselves are verbatim from the raw file.

The upshot: `Environmental` is not a subclass of any one of the three children of `environmental system`. It is a fourth, cross-cutting cut. That is exactly why nothing grounds it.

---

## 1. What the concept denotes

### 1.1 The reading the data means

`Environmental` is **the level-1 (`Ecosystem`) value of GOLD's five-level ecosystem classification**, one of exactly three:

> "At the top of this classification chain is Ecosystem, which consists of Environmental, Host-Associated and Engineered"
> — Mukherjee S, Stamatis D, Bertsch J, et al. *Genomes OnLine Database (GOLD) v.8: overview and updates.* **Nucleic Acids Research** 49(D1):D723–D733 (8 Jan 2021). doi:[10.1093/nar/gkaa983](https://doi.org/10.1093/nar/gkaa983) · [OUP full text](https://academic.oup.com/nar/article/49/D1/D723/5957166)

> "Environmental features of a Biosample or an Organism is described in a five-level ecosystem classification… Ecosystem, Ecosystem Category, Ecosystem Type, Ecosystem Subtype and Specific Ecosystem."
> — Mukherjee S, Stamatis D, Bertsch J, Ovchinnikova G, et al. *Genomes OnLine database (GOLD) v.7: updates and new features.* **NAR** 47(D1):D649–D659 (2019). doi:[10.1093/nar/gky977](https://doi.org/10.1093/nar/gky977) · [PMC6323969](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323969/)

It denotes, collectively, the settings a genome or biosample can come from that GOLD partitions into three **Ecosystem Categories: Air, Aquatic, Terrestrial**. Confirmed in `data/raw/gold_ecosystem_paths.tsv`: 707 distinct paths under `Environmental`, of which 412 Aquatic, 284 Terrestrial, 10 Air, plus the bare `Environmental` node itself. Current v.10 release: Mukherjee S, Stamatis D, Li CT, et al., *Genomes OnLine Database (GOLD) v.10: new features and updates*, **NAR** 53(D1):D989–D997 (6 Jan 2025), doi:[10.1093/nar/gkae1000](https://doi.org/10.1093/nar/gkae1000). Biosample split at v.8: "Host-associated (55%), Environmental (38%) and Engineered (7%)" (v.8 paper, above).

### 1.2 The boundary — inside and out

**Inside** (from the raw path table): all natural and managed waters (marine pelagic/oceanic/coastal/sediment, freshwater lake/river/pond/groundwater/aquifer, thermal springs, hydrothermal vents, hypersaline and soda lakes, acidic waters, deep subsurface groundwater, mine water, acid mine drainage); all land surface and subsurface (soil of every kind including garden, greenhouse, agricultural, paddy, pasture, orchard, plantation, contaminated; sediment; rock core; permafrost; caves; deserts; deep subsurface; geologic; mine); air (outdoor **and** indoor, including cattle barn, poultry farm, composting-facility air, and settled dust); and free-living microbial structures growing in those settings (microbial mats, biofilms, subaerial rock biofilms, plant litter).

**Outside — the neighbouring bins, from the same table:**

| Neighbour | GOLD `Ecosystem` | Its Ecosystem Categories |
|---|---|---|
| Constructed/operated systems and manufactured matrices | `Engineered` (528 paths) | Animal feed production, Artificial ecosystem, Bioreactor, Bioremediation, Biotransformation, **Built environment**, Drugs production, Food production, Industrial production, Lab culture, Lab enrichment, Lab synthesis, Laboratory developed, Modeled, Paper, Sewage treatment plant, Solid waste, Wastewater, WWTP |
| Anything in or on a host | `Host-associated` (1,324 paths) | Algae, Amoebozoa, Amphibia, Annelida, Arthropoda (×4), Birds, Bryozoa, Cephalochordata, Ciliophora, Cnidaria, Endosymbionts, Fish, Fungi, Invertebrates, Mammals, Mammals: Human, Microbial, Mollusca, Plants, Porifera, Protists, Protozoa, Reptilia, Tunicates |

**The one line GOLD draws inconsistently is indoor.** `Environmental > Air > Indoor Air` (72) is Environmental, but `Engineered > Built environment > Spacecraft Assembly Cleanrooms > Air` (5) and `Engineered > Built environment > House > Dust` (7) are Engineered — while `Environmental > Air > Indoor Air > Dust` (65) is not. So the same physical matrix lands in different bins depending on which subtree the curator entered from. **This is my observation from the path table, not a documented GOLD policy**, and it means the definition cannot use "outdoor" or "unsheltered" as a differentia (see §2.2, `ENVO:03501101`).

### 1.3 Ambiguity in the label

"Environmental" has at least four readings and only one is meant here:

1. **The GOLD provenance bin** — non-host, non-artefact sample origin. *This is what the data means*; the source path is literally the bare string `Environmental` at depth 1.
2. **"Environmental" as opposed to "clinical"** — the default reading in isolation-source free text and culture-collection catalogues, under which sewage and bioreactors *are* environmental. GOLD puts both in `Engineered`. This reading must be excluded explicitly.
3. **"The environment" as a mass concept** — ENVO's `environmental system` root.
4. **"Environmental" as a method qualifier** — environmental sequencing, environmental DNA. A process, not a place, and not a habitat.

### 1.4 One number worth correcting for

`assertion_count: 1285` on this record is **not** a subtree rollup. `scripts/extract_source_inventory.py` counts one `biolink:occurs_in` edge per (GOLD subject, ecosystem node) pair and sums only across nodes that collapse to the *same* filler-stripped path; there is no ancestor propagation. The 1,285 organisms are therefore those annotated at exactly `Environmental` with no Ecosystem Category filled in — genuinely unspecified provenance. The whole `Environmental` subtree carries 84,839 assertions by comparison. **This differs from the BacDive sibling record**, where the same label's 18,454 *is* a rollup because MISO tags a strain at all three levels. (Inference from the extractor code plus arithmetic; not a claim any source makes. It matters because `just report` ranks the backlog on this number, and here the number is honest.)

---

## 2. Genus

### 2.1 Recommended genus

**`ENVO:01000254` — *environmental system***
> "A system which has the disposition to environ one or more material entities." Exact synonym: *environment*.
> — [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01000254), retrieved 2026-08-17; identical text in the vendored `data/raw/ontology_terms.tsv`.

Correct because it is the immediate parent of all three of the cuts this concept cross-cuts — `natural environment`, `anthropogenic environment`, and `environmental system determined by an organism` are each a direct `rdfs:subClassOf ENVO:01000254` (verified in `data/raw/ontology_subclass_edges.tsv`). It asserts nothing the sources do not, and it is where GOLD's own level-1 sits.

**Caveat:** `ENVO:01000254`'s children are not a disjoint partition — the vendored slice alone shows `aquatic environment`, `cold environment`, `outdoor environment`, `ecosystem`, `endolithic environment`, `high pressure environment` and others as siblings of the three. So "fourth sibling" is a weaker structural claim than it sounds. *(Observation about ENVO's axiomatisation, not a sourced statement.)*

### 2.2 Near-misses — checked, and why each fails

| CURIE | Label | Why not |
|---|---|---|
| **`ENVO:01000951`** | **natural environment** | *"An environmental system in which minimal to no anthropisation has occurred and non-human agents are the primary determinants of the system's dynamics and composition."* Alt labels *non-anthropised environment*, *non-anthropized environment*; ENVO's own comment concedes most environments lie on a spectrum ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01000951)). GOLD's bin holds 5,014 `Garden`, 698 `Greenhouse`, 364+226+138 agricultural, 159 `Tree plantation`, 133 `Paddy`, 218 `Mine`, 72 `Indoor Air`, and explicitly `Contaminated > Pesticide`/`Uranium contaminated`. Also has **no air child** — its children are `terrestrial natural environment` (`ENVO:01001226`), `aquatic natural environment` (`ENVO:01001227`) and `natural monument` — so it cannot span GOLD's three Ecosystem Categories. **Verdict: keep as `relation: xref`, exactly as the record does.** |
| `ENVO:01000313` | anthropogenic environment | *"An anthropogenic environment is an environmental system which is the product of human activity."* This is GOLD's `Engineered`, not `Environmental`. Attaching it inverts the sense — even though, per §0.2, part of the GOLD bin falls under it. |
| `ENVO:01000311` | cultivated environment | Subclass of the above; covers GOLD's agricultural paths only, i.e. a *fragment* of the bin under the wrong branch. Already in the corpus as `data/habitats/other/cultivated_environment.yaml`. Worth an xref only if the curator wants the overlap recorded. |
| `ENVO:01001000` | environmental system determined by an organism (syn. *host-associated environment*) | GOLD's `Host-associated`. The complement on the axis the definition's second clause uses — cite it in the comment, never as parent. |
| `ENVO:03501101` | outdoor environment | *"An environmental system which is not sheltered."* The closest **positive** near-miss. Fails both ways: `Indoor Air`, `Cave`, `Deep subsurface`, `Groundwater`, `Rock core/Sediment` are inside GOLD's bin but sheltered; city streets and building exteriors are unsheltered but GOLD files them `Engineered > Built environment > City`. |
| `ENVO:01001110` | ecosystem | *"An environmental system which includes both living and non-living components."* True, but equally true of `Host-associated` and most of `Engineered`. Non-discriminating. Its child `anthropised ecosystem` (`ENVO:01001828`) is again the wrong branch. |
| `ENVO:01000739` | habitat | *"An environmental system which can sustain and allow the growth of an ecological population."* Every record in this corpus is a habitat; contributes no differentia. Also awkwardly placed in ENVO (parents `ENVO:01000813` and `ENVO:01001110`). |
| `ENVO:00010483` | environmental material | *"A material entity which other material entities in an environmental system are primarily or partially composed of."* A **material**, not a system — the MIxS `env_medium` slot. Grounding a place to a material is the category error the repo's `NOT_APPLICABLE` rule guards against for qualities. |
| `ENVO:00000428` | biome | The MIxS `env_broad_scale` vocabulary. GOLD's *children* ground here — `Environmental > Terrestrial` → `ENVO:00000446` *terrestrial biome*, `Environmental > Aquatic` → `ENVO:00002030` *aquatic biome* (both `EXACT` in this corpus) — but the parent bin is a provenance partition, not a climatically-defined region. |
| `ENVO:01000267` / `ENVO:00002005` | atmosphere / air | `Environmental > Air` already grounds to `ENVO:00002005` *air* in this corpus (an environmental *material*, note, not a biome). Covers one of three categories. |

**Nothing in UBERON, FOODON, BTO or PO is a candidate** — not an anatomical structure, food, tissue source, or plant structure.

**A telling detail:** the three children of this concept in this very corpus ground to two *biomes* and one *environmental material* (`terrestrial_biome.yaml`, `aquatic_biome.yaml`, `air.yaml`). GOLD's own Ecosystem Categories have no shared ENVO genus below `environmental system` either. That is independent evidence that the parent bin's genus really is that high.

**Non-OBO checked and rejected:** SNOMED CT's environment hierarchy is built around healthcare and occupational settings and has no place-kind term at this generality. AGROVOC `environment` (c_2600) is a topical subject descriptor, not a sampled place, and is not an appropriate grounding target for a habitat record.

---

## 3. Differentia

What separates this concept from its siblings under `environmental system`, in order of how checkable each is:

1. **The sampled matrix is a bulk environmental medium *in situ* — air, water, soil, sediment, rock, ice — not a tissue, body fluid, manufactured product, or process stream.** This is directly readable off any sampling record and is the single most operational differentia. It is also the MIxS `env_medium` framing: `env_medium` (MIXS:0000014/0000016) recommends subclasses of `environmental material` (`ENVO:00010483`), `env_broad_scale` (MIXS:0000012) recommends subclasses of `biome` (`ENVO:00000428`), and `env_local_scale` (MIXS:0000013) admits UBERON anatomical sites *specifically for host-associated samples*. [GSC MIxS](https://genomicsstandardsconsortium.github.io/mixs/) · [`env_broad_scale`](https://genomicsstandardsconsortium.github.io/mixs/0000012/) · [`env_local_scale`](https://genomicsstandardsconsortium.github.io/mixs/0000013/) · [ENVO–MIxS usage guide](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS). Original spec: Yilmaz P, Kottmann R, Field D, et al., *Minimum information about a marker gene sequence (MIMARKS) and minimum information about any (x) sequence (MIxS) specifications*, **Nature Biotechnology** 29:415–420 (2011), doi:[10.1038/nbt.1823](https://doi.org/10.1038/nbt.1823).

2. **No host organism bounds the system.** The microorganisms are free-living rather than resident in or on a plant, animal, fungus or protist. This separates the concept from `ENVO:01001000` and is the primary axis of every major microbial-habitat scheme (§4). *With the caveat of §0.2: GOLD does not apply it cleanly to organism-built structures.*

3. **The system is not itself a constructed or operated artefact.** No vessel, treatment train, culture, or fabricated product. This separates it from `ENVO:01000313` and from GOLD's `Engineered`. Note that this is narrower than "not human-affected": a greenhouse *soil* stays in, a bioreactor *does not*.

4. **It does *not* require the absence of human influence — this is the crux.** Managed land (`Garden` 5,014; `Greenhouse` 698; `Agricultural land` 502 across three paths; `Tree plantation` 159; `Paddy field/soil` 133; `Pasture`, `Orchard`, `Arable`, `Manure-fertilized`), contaminated land and water (`Contaminated > Pesticide`, `> Uranium contaminated`, `Oil-contaminated` in soil, sand, clay, marine oceanic and intertidal), extraction settings (`Geologic > Mine` 218, `Acid Mine Drainage` 18, `Surface mine > Reclaimed`), and indoor air all stay inside. This is the property that makes the concept broader-than-and-crossing `natural environment`.

5. **Physicochemistry and depth are subtypes, not differentiae.** Acidity, salinity, temperature and pressure appear *below* this level in GOLD (`Aquatic > Acidic`, `> Non-marine Saline and Alkaline`, `> Thermal springs > Hot (42–90C)`) rather than as a cross-cutting axis. Do not fold them in — cf. the repo's existing rule that "Acidic" maps to `PATO:0001429` and is `NOT_APPLICABLE`, and the environment-parameter skip rule for `sediment_marine_cold`.

**Not a differentia:** taxon composition. Nothing distinctive is claimed here; the concept is a provenance bin spanning marine pelagic to permafrost.

---

## 4. Sources

**The source vocabulary**

- Mukherjee S, Stamatis D, Bertsch J, Ovchinnikova G, Katta HY, Mojica A, Chen I-MA, Kyrpides NC, Reddy TBK. *Genomes OnLine database (GOLD) v.7: updates and new features.* **NAR** 47(D1):D649–D659 (24 Oct 2018). doi:[10.1093/nar/gky977](https://doi.org/10.1093/nar/gky977) · PMID [30357420](https://pubmed.ncbi.nlm.nih.gov/30357420/) · [PMC6323969](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323969/) — **the five-level classification quote in §1.1.**
- Mukherjee S, Stamatis D, Bertsch J, et al. *Genomes OnLine Database (GOLD) v.8: overview and updates.* **NAR** 49(D1):D723–D733 (8 Jan 2021). doi:[10.1093/nar/gkaa983](https://doi.org/10.1093/nar/gkaa983) · [full text](https://academic.oup.com/nar/article/49/D1/D723/5957166) — **the three-value Ecosystem quote and the 55/38/7% biosample split.**
- Mukherjee S, Stamatis D, Li CT, Ovchinnikova G, et al. *Twenty-five years of Genomes OnLine Database (GOLD): data updates and new features in v.9.* **NAR** 51(D1):D957–D963 (2023). doi:[10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974) · PMID [36318257](https://pubmed.ncbi.nlm.nih.gov/36318257/)
- Mukherjee S, Stamatis D, Li CT, Kandimalla M, Handke V, Reddy A, Ivanova N, Woyke T, Eloe-Fadrosh EA, Chen I-MA, Kyrpides NC, Reddy TBK. *Genomes OnLine Database (GOLD) v.10: new features and updates.* **NAR** 53(D1):D989–D997 (6 Jan 2025). doi:[10.1093/nar/gkae1000](https://doi.org/10.1093/nar/gkae1000) · [OSTI](https://www.osti.gov/pages/biblio/2482283) — current release.
- Reddy TBK, Thomas AD, Stamatis D, et al. *The Genomes OnLine Database (GOLD) v.5: a metadata management system based on a four level (meta)genome project classification.* **NAR** 43(D1):D1099–D1106 (2015). doi:[10.1093/nar/gku950](https://doi.org/10.1093/nar/gku950) — where isolate genomes began being classified with the same five-tier scheme; note the "four level" in the title is project organisation, not the ecosystem hierarchy.
- [GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification) and [Ecosystem Classification Paths browser](https://gold.jgi.doe.gov/ecosystemtree) — the live hierarchy. **Both return HTTP 403 to automated fetch** (as does `resources/project_help_doc.pdf`), so no verbatim quote from GOLD's own site is available here; the quotes above are from the NAR papers.
- All path counts in this report: `data/raw/gold_ecosystem_paths.tsv` (this repo, reconstructed from kg-microbe's `GOLD_nodes.tsv`/`GOLD_edges.tsv` by `scripts/extract_source_inventory.py`), read 2026-08-17.

**Independent corroboration that host/non-host is the primary axis**

- Thompson LR, Sanders JG, McDonald D, et al. (Earth Microbiome Project Consortium). *A communal catalogue reveals Earth's multiscale microbial diversity.* **Nature** 551:457–463 (1 Nov 2017). doi:[10.1038/nature24621](https://doi.org/10.1038/nature24621) · PMID [29088705](https://pubmed.ncbi.nlm.nih.gov/29088705/) — EMPO level 1 is **free-living vs host-associated**, level 2 saline vs non-saline. The strongest external evidence that this cut is a real, independently rediscovered partition rather than a GOLD idiosyncrasy.
- Shaffer JP, Nothias L-F, Thompson LR, et al. *Standardized multi-omics of Earth's microbiomes reveals microbial and metabolite diversity.* **Nature Microbiology** 7:2128–2150 (2022). doi:[10.1038/s41564-022-01266-x](https://doi.org/10.1038/s41564-022-01266-x) — EMPO v2 keeps host association at level 1.
- [EMPO documentation](https://earthmicrobiome.org/protocols-and-standards/empo/) — `empo_1` ∈ {Free-living, Host-associated, Control, Unknown}. **"Free-living" is the best positive-polarity name in the literature for what this bin means.**

**Standards and cross-walks**

- [NMDC Metadata Standards Documentation](https://microbiomedata.github.io/nmdc-schema/Metadata_Documentation_Overview/) — NMDC carries **both** the GOLD five-level path and the MIxS/EnvO triad per biosample, and states the triad assignment was done by **manual curation** from GOLD fields, with automated GOLD→EnvO mapping still an open problem. That is direct evidence that no mechanical GOLD-`Environmental`→ENVO mapping exists to borrow.
- MIxS term registry, as cited in §3.

**Ontology**

- Buttigieg PL, Morrison N, Smith B, Mungall CJ, Lewis SE, ENVO Consortium. *The environment ontology: contextualising biological and biomedical entities.* **J Biomed Semantics** 4:43 (2013). doi:[10.1186/2041-1480-4-43](https://doi.org/10.1186/2041-1480-4-43) · [PMC3904460](https://pmc.ncbi.nlm.nih.gov/articles/PMC3904460/)
- Buttigieg PL, Pafilis E, Lewis SE, Schildhauer MP, Walls RL, Mungall CJ. *The environment ontology in 2016: bridging domains with increased scope, semantic density, and interoperation.* **J Biomed Semantics** 7:57 (2016). doi:[10.1186/s13326-016-0097-6](https://doi.org/10.1186/s13326-016-0097-6)
- ENVO term text retrieved from [OLS4](https://www.ebi.ac.uk/ols4/api/) on 2026-08-17 for `ENVO:01000254`, `ENVO:01000951`, `ENVO:01000313`, `ENVO:01000311`, `ENVO:01001000`; hierarchy checked against the vendored `data/raw/ontology_subclass_edges.tsv`.
- [ENVO wiki: Creating good definitions](https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions) — ENVO's own guidance that most terms should be a kind of environmental material, environmental system, ecosystem, or astronomical body part. Relevant to §6: a negation-flavoured proposal is exactly what ENVO curators scrutinise.
- [ENVO issue #1029, "EnvO terms for host-associated samples"](https://github.com/EnvironmentOntology/envo/issues/1029) — the nearest existing thread. It requests *host-associated* biome terms; I found **no** open or closed ENVO request for the free-living complement. *(Absence-of-evidence from a web search, not an exhaustive tracker audit.)*

**Explicitly marked as inference, not sourced:** §0.2's reading of GOLD nests/reefs/litter as organism-determined; §1.2's indoor/outdoor inconsistency; §1.4's rollup analysis; §2.1's caveat on ENVO's non-partitioned children; §6's judgement.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**

| Name | Where |
|---|---|
| **free-living environment** / **free-living** | EMPO `empo_1` — the best positive-polarity name available |
| **non-host-associated environment** | comparative microbiome literature |
| **environmental ecosystem** / **Environmental** (as a GOLD Ecosystem value) | GOLD level 1; JGI/NCBI biosample submissions |
| **environmental sample source**, **environmental isolate source** | culture-collection catalogues |
| **natural and semi-natural environment** | where anthropogenic disturbance must be admitted without implying engineering |
| **air, water and soil compartments** | the three Ecosystem Categories, taken together |

**Do NOT conflate**

- **`ENVO:01000951` *natural environment*.** The likeliest error and the one the record already catches. Asserts minimal anthropisation; this bin holds 5,014 garden-soil organisms. Keep `relation: xref`.
- **`ENVO:01000313` *anthropogenic environment* / `ENVO:01000311` *cultivated environment*.** These cover *part* of the bin (§0.2), which makes them tempting and makes them wrong as identity or parent — they would exclude the marine, polar and deep-subsurface majority.
- **`ENVO:01001000` *environmental system determined by an organism*.** The complement on axis 2. Inverts the meaning.
- **`ENVO:03501101` *outdoor environment*.** Cross-cuts; excludes caves, subsurface and indoor air (all in), admits streets (out).
- **`ENVO:00010483` *environmental material*.** A material, the MIxS `env_medium` slot — not a system.
- **`ENVO:00000428` *biome*.** The MIxS `env_broad_scale` slot. The bin's *children* are biomes; the bin is not.
- **"Environmental" = "non-clinical."** Very widespread. Under that reading sewage, bioreactors and food are environmental; GOLD files all three as `Engineered`.
- **"Environmental sequencing" / "environmental DNA."** A method, not a place.
- **`ENVO:01000952` *anthropisation*.** A process — `NOT_APPLICABLE` territory by this repo's rule.
- **GOLD `Engineered > Built environment`.** Contains `Spacecraft Assembly Cleanrooms > Air` and `House > Dust` while `Environmental > Air > Indoor Air > Dust` is in-bin. Do not assume the two bins partition indoor space cleanly; they do not.

---

## 6. Should it be a term at all?

**Yes — as an explicitly-labelled grouping class, not as a sampleable habitat.** It is not a process, quality, disease state, taxon, or sampling artefact, so none of the corpus's existing disposals apply. Three independent vocabularies — GOLD, BacDive MISO, and EMPO — draw substantially the same top-level cut, which is about as strong an argument for term-hood as a high-level bin can have. Four qualifications:

1. **The differentia is two-thirds negative, and OBO practice discourages definition by negation** ([ENVO's own definition guidance](https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions)). The honest upstream framing is not "please add *Environmental*" but: *ENVO has positive classes for host-determined and anthropogenic environments and none for the free-living complement; `natural environment` is not that complement because it requires minimal anthropisation, and every large microbial-provenance vocabulary (GOLD, BacDive, EMPO) needs the complement class.* That is a specific, defensible ENVO request. **Per the standing rule, no ENVO submission without a separate explicit yes for that individual request.**

2. **The 1,285 is real annotation, not a rollup** (§1.4) — unlike the BacDive sibling's 18,454. These are organisms GOLD could place no more precisely than "Environmental". The backlog rank is honest here.

3. **Merge with the BacDive record first.** `data/habitats/other/environmental.yaml` (`habitatmech:BACDIVE.0f1e92a02c`, 18,454 strains) and `data/habitats/other/environmental__a27d7186.yaml` (this record) are both `label: Environmental`, `OTHER`, `UNGROUNDED`, xref `ENVO:01000951`, with near-identical notes. They are the level-1 bin of two vocabularies partitioning provenance the same way — the case #116/#117 added machinery for. **The one substantive disagreement is agriculture: BacDive files farmed land under `#Engineered / #Agriculture`, GOLD files it under `Environmental`.** That belongs in the merged record's notes as a source disagreement, not in the definition. A merged definition must not assert "no agricultural land."

4. **The definition proposed above is written to the GOLD bin.** If the merge happens, clause 3 ("not constituted by a constructed or operated artefact") is the one that has to absorb BacDive's stricter line, and the safest resolution is to keep the clause as written and record BacDive's narrower reading as a note.

**Suggested decision shape** (`curation/decisions.tsv`, keyed on `habitatmech:GOLD.c3fa7fc4c2`):

- Action: `CONFIRM_UNGROUNDED`, term-request candidate — **unchanged**.
- `parent_habitats`: `ENVO:01000254` *environmental system*, `relation: parent`. Genuinely broader, asserts nothing the sources do not. The record currently has no parent at all.
- `xrefs`: keep `ENVO:01000951` *natural environment*. Consider adding `ENVO:03501101` *outdoor environment* and `ENVO:01000311` *cultivated environment*, both `relation: xref`, so the next curator does not re-derive either near-miss.
- Note: the existing `Tree plantation` claim is **verified and safe to keep**. If it is rewritten, `Environmental > Terrestrial > Soil > Garden` (5,014 organisms) and `Environmental > Terrestrial > Soil > Greenhouse` (698) are stronger, and the `cultivated environment` ⊑ `anthropogenic environment` edge (§0.2) turns "narrower than" into the sharper and more accurate "cross-cuts". Any path quoted in a note must match `data/raw/gold_ecosystem_paths.tsv` verbatim — `tests/test_decisions.py` checks it.

## Citations

1. https://doi.org/10.1093/nar/gkaa983 · https://academic.oup.com/nar/article/49/D1/D723/5957166
2. https://doi.org/10.1093/nar/gky977 · https://pmc.ncbi.nlm.nih.gov/articles/PMC6323969/ · https://pubmed.ncbi.nlm.nih.gov/30357420/
3. https://doi.org/10.1093/nar/gkac974 · https://pubmed.ncbi.nlm.nih.gov/36318257/
4. https://doi.org/10.1093/nar/gkae1000 · https://academic.oup.com/nar/article/53/D1/D989/7875979 · https://www.osti.gov/pages/biblio/2482283
5. https://doi.org/10.1093/nar/gku950
6. https://gold.jgi.doe.gov/ecosystem_classification (HTTP 403 to automated fetch)
7. https://gold.jgi.doe.gov/ecosystemtree
8. https://doi.org/10.1038/nature24621 · https://pubmed.ncbi.nlm.nih.gov/29088705/
9. https://doi.org/10.1038/s41564-022-01266-x
10. https://earthmicrobiome.org/protocols-and-standards/empo/
11. https://doi.org/10.1038/nbt.1823
12. https://genomicsstandardsconsortium.github.io/mixs/ · /0000012/ · /0000013/
13. https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
14. https://microbiomedata.github.io/nmdc-schema/Metadata_Documentation_Overview/
15. https://doi.org/10.1186/2041-1480-4-43 · https://pmc.ncbi.nlm.nih.gov/articles/PMC3904460/
16. https://doi.org/10.1186/s13326-016-0097-6
17. https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01000254
18. https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01000951
19. https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01000311
20. https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001000
21. https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions
22. https://github.com/EnvironmentOntology/envo/issues/1029
23. http://obofoundry.org/ontology/envo.html

## Citations

1. https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01000311
2. https://doi.org/10.1093/nar/gkaa983
3. https://academic.oup.com/nar/article/49/D1/D723/5957166
4. https://doi.org/10.1093/nar/gky977
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC6323969/
6. https://doi.org/10.1093/nar/gkae1000
7. https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01000254
8. https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01000951
9. https://genomicsstandardsconsortium.github.io/mixs/
10. https://genomicsstandardsconsortium.github.io/mixs/0000012/
11. https://genomicsstandardsconsortium.github.io/mixs/0000013/
12. https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
13. https://doi.org/10.1038/nbt.1823
14. https://pubmed.ncbi.nlm.nih.gov/30357420/
15. https://doi.org/10.1093/nar/gkac974
16. https://pubmed.ncbi.nlm.nih.gov/36318257/
17. https://www.osti.gov/pages/biblio/2482283
18. https://doi.org/10.1093/nar/gku950
19. https://gold.jgi.doe.gov/ecosystem_classification
20. https://gold.jgi.doe.gov/ecosystemtree
21. https://doi.org/10.1038/nature24621
22. https://pubmed.ncbi.nlm.nih.gov/29088705/
23. https://doi.org/10.1038/s41564-022-01266-x
24. https://earthmicrobiome.org/protocols-and-standards/empo/
25. https://microbiomedata.github.io/nmdc-schema/Metadata_Documentation_Overview/
26. https://doi.org/10.1186/2041-1480-4-43
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC3904460/
28. https://doi.org/10.1186/s13326-016-0097-6
29. https://www.ebi.ac.uk/ols4/api/
30. https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions
31. https://github.com/EnvironmentOntology/envo/issues/1029
32. https://academic.oup.com/nar/article/53/D1/D989/7875979
33. https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001000
34. http://obofoundry.org/ontology/envo.html