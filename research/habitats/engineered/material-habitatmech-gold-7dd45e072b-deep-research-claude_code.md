---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T03:26:46.475610'
end_time: '2026-08-18T03:39:16.818571'
duration_seconds: 750.34
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Material
  habitat_identifier: habitatmech:GOLD.7dd45e072b
  habitat_category: ENGINEERED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Engineered > Industrial production > Engineered product > Material'
  assertions: '0'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Stale-sweep\
    \ review (#12): NCIT:C48187 'Material' matches the label and carries none of the\
    \ meaning \u2014 a residual bucket like the NCIT 'Other' and 'Part' terms already\
    \ refused in #43. Path: Engineered > Industrial production > Engineered product\
    \ > Material (source concept habitatmech:GOLD.7dd45e072b)"
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
  web_search_requests: 9
  num_turns: 34
  total_cost_usd: 2.873715499999999
  session_id: 8d056956-eadb-40a8-b46a-79af2a716e19
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 38
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Material
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.7dd45e072b
- **Category:** ENGINEERED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Engineered > Industrial production > Engineered product > Material
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Stale-sweep review (#12): NCIT:C48187 'Material' matches the label and carries none of the meaning — a residual bucket like the NCIT 'Other' and 'Part' terms already refused in #43. Path: Engineered > Industrial production > Engineered product > Material (source concept habitatmech:GOLD.7dd45e072b)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Material** as a microbial habitat, with citations.

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

# Definition research: **Material** (`habitatmech:GOLD.7dd45e072b`)

> **Proposed definition:** A manufactured product which is a bulk fabricated substance — such as a plastic, a textile, or paper — supplied as stock for further use rather than as a functioning device, and whose surface and interior are colonised by microorganisms.

**Genus:** `ENVO:00003074` *manufactured product*.
**Caveat the curator should read before using this:** the concept is a **grouping node with zero direct attestations** (all upstream volume sits on its child *Plastic*). The definition above is defensible, but the honest alternative disposition — keep it as an unpopulated intermediate class and put curation effort on the three children — is discussed in §6.

---

## 1. What the concept denotes

### The source evidence

The GOLD path is `Engineered > Industrial production > Engineered product > Material`, at classification depth 4 (Ecosystem Subtype). Its own extraction row in this repo (`data/raw/gold_ecosystem_paths.tsv:1323`) records **2 GOLD node ids (8333, 8334), 0 organisms, 0 studies, 0 biosamples**. What fixes its meaning is its three children and its siblings:

| Children of *Material* | GOLD node | organisms |
|---|---|---|
| Plastic | 8335 | 30 |
| Fabric | 8336 | 0 |
| Paper | 8337 | 0 |

| Siblings under *Engineered product* | kind of thing |
|---|---|
| Aviation fuel | a fluid commodity |
| Bioanode, Biocathode (each with a *Biofilm* child) | functioning electrodes |
| Filter (child *Biofilter*) | a functioning device |
| Optical Instruments (child *Optical Lens*) | a functioning device |
| Tobacco product | a finished consumer good |
| Wetsalted hide | a part-processed animal product |

So *Material* is the node GOLD uses for **bulk fabricated substances characterised by what they are made of** (polymer, fibre, cellulose sheet), as opposed to its siblings, which are **artefacts characterised by what they do** (an electrode, a filter, a lens) or **finished goods/fluids**. A sample classified here is a piece of manufactured material — a plastic coupon or film, a swatch of cloth, a sheet of paper — from which DNA or isolates were taken. *(This reading is my inference from the tree structure, not a statement GOLD publishes; GOLD's own documentation describes only the five-level scheme, not per-node definitions — Mukherjee et al. 2023, [10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974).)*

### Readings the label admits, and which one the data means

1. **Bulk manufactured stock material** (plastic / textile / paper). *This is the reading the source path supports* — it is the only reading under which the three children are co-hyponyms.
2. **"Material" as any sample substance** (the mass-noun, environmental-material sense: soil is a material, blood is a material). This is the residual-bucket reading that `NCIT:C48187` "Material — the tangible substance that goes into the makeup of a physical object" encodes. It is excluded here by the position of the node *inside* `Engineered > Industrial production > Engineered product`.
3. **Materials-science reading including inorganics** — metal, concrete, glass, stone, ceramic. GOLD does not attest these under this node, but the standards vocabulary for exactly this idea does: MIxS `surf_material` (`MIXS:0000758`, "Surface materials at the point of sampling") enumerates *adobe, carpet, cinder blocks, concrete, glass, hay bales, metal, paint, plastic, stainless steel, stone, stucco, tile, vinyl, wood* ([MIxS term page](https://genomicsstandardsconsortium.github.io/mixs/0000758/), [SurfMaterialEnum](https://genomicsstandardsconsortium.github.io/mixs/SurfMaterialEnum/)). A definition that says "such as plastic, textile or paper" without closing the list keeps reading 3 open, which I recommend: GOLD subtypes are extended as projects arrive, and the corpus should not have to be re-curated when *Metal* appears under this node.

### Boundaries — what is *not* inside

- **The same material *in situ* in a building.** `Engineered > Built environment` covers building surfaces; MIxS records their composition with `surf_material` as an attribute of a built-environment sample, not as the sample's environment (Glass et al. 2013, MIxS-BE, [10.1038/ismej.2013.176](https://doi.org/10.1038/ismej.2013.176)). *Material* is the manufactured stuff sampled as itself.
- **Plastic litter in a natural setting.** The plastisphere literature samples plastic floating in seawater or lake water; that plastic is debris in an aquatic environment, not an engineered product on a production line (Zettler et al. 2013, [10.1021/es401288x](https://doi.org/10.1021/es401288x); Amaral-Zettler et al. 2020, [10.1038/s41579-019-0308-0](https://doi.org/10.1038/s41579-019-0308-0)). The GOLD child *Plastic* sits under an industrial-production branch and does not, by itself, license an environmental-debris reading.
- **`Engineered > Paper` (with child *Currency notes*).** GOLD carries a **second, unrelated "Paper" branch at Ecosystem Category level**, i.e. the paper industry / paper as an item in circulation. So "Paper" occurs twice in the GOLD tree with different parentage. Any definition of *Material* must not silently absorb that branch. (Source: `data/raw/gold_ecosystem_paths.tsv`, canonical paths `Engineered > Paper`, `Engineered > Paper > Currency notes`.)
- **`Engineered > Industrial production > Chemical products`** (artificial seawater, buffers, metalworking fluids, lab-grade water, reagent blanks) — the sibling *type* for formulated fluids and reagents. Liquids and formulated chemicals belong there, not under *Material*.
- **Devices made of these materials** — filter, lens, electrode. The line is function-vs-substance, and it is exactly the line GOLD drew when it put *Filter* and *Optical Instruments* beside *Material* rather than under it.

---

## 2. Genus — the broader kind

### Recommended: `ENVO:00003074` *manufactured product*

ENVO definition: *"A material entity that has been processed by humans or their technology in any way, including intermediate products as well as final products."* ([OLS](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00003074))

Why it fits:

- Two of the three children of GOLD *Material* are **already direct children of it in ENVO**: `ENVO:02000001` *textile* and `ENVO:00003895` *paper product* (verified via OLS4 parent queries, August 2026).
- The phrase "including intermediate products" is precisely the stock-material sense; a bolt of cloth is an intermediate product.
- HabitatMech already uses it as the parent of its own `textile` record (`data/habitats/engineered/textile.yaml`).

Why it is only a genus and not a match: `ENVO:00003074` has ~90 direct children spanning ATMs, televisions, oil tanks, umbrellas and conveyor belts. It is far broader than the concept; it is the *smallest well-established* ENVO kind above it, not a synonym. **There is no ENVO class between "manufactured product" and plastic/textile/paper for "bulk fabricated material".** That absence is the reason this term request exists.

### Near misses, and why each fails

| Candidate | Why it is a near miss and why it fails |
|---|---|
| `ENVO:0010001` *anthropogenic environmental material* — "Anthropogenic material in or on which organisms may live" | **Closest in intent** — it is explicitly framed as a habitat class. But it sits in the mass-noun `environmental material` branch, and its children are construction/handling substances: concrete, adobe, brick material, plaster, paint, latex, gypsum, refined asphalt, inks, sludge, mine tailing. It contains **no textile and no paper product**, so it cannot be the genus for a class whose attested children include *Fabric* and *Paper*. Worth recording: if HabitatMech later decides GOLD *Material* means the mass-noun sense, this is the right genus. |
| `ENVO:00010483` *environmental material* | Explicit ENVO note: *"Everything under this parent must be a mass noun (i.e. not countable)."* A sheet of paper and a garment are countable. Fails on ENVO's own stated constraint. |
| `ENVO:06105101` *plastic* | This is where the wrinkle bites: ENVO files *plastic* under `environmental material`, not under `manufactured product`. So GOLD's three children are split across **two disjoint ENVO branches**. This is real evidence that no single existing ENVO parent covers the GOLD node. (Verified via OLS4, August 2026.) |
| `ENVO:03501256` *sheet of paper* / `ENVO:02000001` *textile* | Narrower — these are the children, already used as such on `paper.yaml` and `textile.yaml`. |
| `NCIT:C48187` *Material* | Label match, no content; already refused in the stale-sweep review (#12) and consistent with the NCIT "Other"/"Part" refusals in #43. |
| `OBI:0000047` *processed material* | **Obsolete in OBI** (confirmed via OLS4, August 2026), and OBI is not in the vendored slice. Not usable. |
| FOODON `FOODON:00003368` *food contact material* | Asserts a food-contact context the GOLD path does not support — the same over-claim that got `FOODON:03500045` "food-grade textile surface" reverted in #62. |
| BTO | No relevant class; BTO's "material" hits are cell/tissue terms. |

*Checked and reported as of August 2026 against OLS4 for ENVO, FOODON, BTO, NCIT and OBI.*

---

## 3. Differentia — what distinguishes it

Properties that separate *Material* from its siblings under *manufactured product* / *Engineered product*, ordered by how observable they are:

1. **Substance-defined, not function-defined.** Membership is decided by composition (synthetic polymer, fibre network, cellulose sheet), not by an intended device function. Its siblings *Bioanode*, *Biocathode*, *Filter*, *Optical Instruments* are all defined by function. *(Inference from the source tree, plus ENVO's own contrast between `textile` — "comprised of a network of natural or artificial fibers" — and `air filter`/`medical instrument`, which are defined by use.)*
2. **Solid, and colonised as a surface.** These are substrata for biofilm rather than bulk media. Attachment, EPS secretion, microcolony formation and maturation is the canonical sequence on abiotic manufactured surfaces (Dang & Lovell 2016, *MMBR*, [10.1128/MMBR.00037-15](https://doi.org/10.1128/MMBR.00037-15); Flemming 1998, *Polym Degrad Stab*, [10.1016/S0141-3910(97)00189-4](https://doi.org/10.1016/S0141-3910(97)00189-4)).
3. **Surface physicochemistry selects the community — measurably.** Hydrophobicity, roughness, crystallinity and surface charge shape which taxa attach. Direct evidence: polyester (hydrophobic) adsorbs more bacteria and more sebum than cotton, while cotton's water retention sustains activity after drying (Møllebjerg et al. 2021, *Microbiol Spectr*, [10.1128/spectrum.01185-21](https://doi.org/10.1128/spectrum.01185-21)); polymer type shapes plastisphere assembly, though environmental conditions dominate (Amaral-Zettler et al. 2020, [10.1038/s41579-019-0308-0](https://doi.org/10.1038/s41579-019-0308-0)).
4. **The material is itself a carbon/nutrient source for at least part of the community.** Paper: cellulose plus sizing glues, animal/plant adhesives and ink binders are the nutrient base, degraded by cellulolytic fungi and by *Bacillus* spp. after fungal pre-degradation (Karakasidou et al. 2018, *MicrobiologyOpen*, [10.1002/mbo3.596](https://doi.org/10.1002/mbo3.596); Pinheiro et al. 2019, *Crit Rev Microbiol*, [10.1080/1040841X.2019.1690420](https://doi.org/10.1080/1040841X.2019.1690420)). Plastics: plastisphere members are directly implicated in polymer breakdown (Gu 2003, *Int Biodeterior Biodegrad*, [10.1016/S0964-8305(02)00177-4](https://doi.org/10.1016/S0964-8305(02)00177-4); Cappitelli et al. 2021, [10.1016/j.ibiod.2021.105282](https://doi.org/10.1016/j.ibiod.2021.105282)).
5. **The category is operationalised by standards as a testable substrate class.** ISO 846 ("Plastics — evaluation of the action of microorganisms") and ASTM G21 ("Standard Practice for Determining Resistance of Synthetic Polymeric Materials to Fungi") both treat *a material specimen* as the unit of exposure, inoculating with a defined fungal consortium (*Aspergillus niger*, *Penicillium* spp., *Chaetomium globosum*, *Gliocladium virens*, *Aureobasidium pullulans*) on carbon-free medium so that the material is the only carbon source, and scoring growth 0–4. This is the clearest external warrant that "material as microbial habitat" is a recognised, measurable category and not an ad-hoc GOLD bucket. ([ASTM G21](https://store.astm.org/g0021-21.html); [ISO 846:2019](https://www.iso.org/standard/74599.html))
6. **Human-shed inoculum dominates where the material contacts people.** T-shirt communities are individual-specific, dominated by skin taxa (*Staphylococcus*, *Enhydrobacter*, *Acinetobacter*), with subject identity outweighing fabric type; unworn polyester had no detectable microbiome while unworn cotton did (Callewaert et al. 2014, *AEM*, [10.1128/AEM.01422-14](https://doi.org/10.1128/AEM.01422-14); Sterndorff et al. 2020, *Environ Res*, [10.1016/j.envres.2020.109449](https://doi.org/10.1016/j.envres.2020.109449)).

**A one-sentence differentia should use (1) and (2)**; properties 3–6 vary across the children and belong in a comment or on the child records, not in the genus-differentia sentence.

---

## 4. Sources

**Vocabularies and standards**

- ENVO `manufactured product` (`ENVO:00003074`), `textile` (`ENVO:02000001`), `paper product` (`ENVO:00003895`), `sheet of paper` (`ENVO:03501256`), `plastic` (`ENVO:06105101`), `anthropogenic environmental material` (`ENVO:0010001`), `environmental material` (`ENVO:00010483`) — retrieved from [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo), August 2026. ENVO reference papers: Buttigieg et al. 2013, *J Biomed Semantics* [10.1186/2041-1480-4-43](https://doi.org/10.1186/2041-1480-4-43); Buttigieg et al. 2016, [10.1186/s13326-016-0097-6](https://doi.org/10.1186/s13326-016-0097-6).
- MIxS `surf_material` (`MIXS:0000758`) and `SurfMaterialEnum` — [genomicsstandardsconsortium.github.io/mixs/0000758](https://genomicsstandardsconsortium.github.io/mixs/0000758/).
- MIxS-BE: Glass, Schriml et al. 2013, *ISME J* [10.1038/ismej.2013.176](https://doi.org/10.1038/ismej.2013.176).
- GOLD five-level ecosystem classification: Mukherjee et al. 2023, *Nucleic Acids Research* 51:D957–D963, [10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974) (PMID [36318257](https://pubmed.ncbi.nlm.nih.gov/36318257/)); GOLD v.8, Mukherjee et al. 2021, [NAR 49:D723](https://academic.oup.com/nar/article/49/D1/D723/5957166).
- ISO 846:2019; ASTM G21-21.

**Primary and review literature**

- Zettler, Mincer & Amaral-Zettler 2013, "Life in the 'Plastisphere'", *Environ Sci Technol* 47:7137–7146, [10.1021/es401288x](https://doi.org/10.1021/es401288x).
- Amaral-Zettler, Zettler & Mincer 2020, "Ecology of the plastisphere", *Nat Rev Microbiol* 18:139–151, [10.1038/s41579-019-0308-0](https://doi.org/10.1038/s41579-019-0308-0).
- Zhang et al. 2023, "Microbial colonization and degradation of marine microplastics in the plastisphere: a review", *Front Microbiol* [10.3389/fmicb.2023.1127308](https://doi.org/10.3389/fmicb.2023.1127308).
- Freshwater plastisphere review 2024, *Front Microbiol* [10.3389/fmicb.2024.1395401](https://doi.org/10.3389/fmicb.2024.1395401).
- Gu 2003, *Int Biodeterior Biodegrad* 52:69–91, [10.1016/S0964-8305(02)00177-4](https://doi.org/10.1016/S0964-8305(02)00177-4).
- Flemming 1998, *Polym Degrad Stab* 59:309–315, [10.1016/S0141-3910(97)00189-4](https://doi.org/10.1016/S0141-3910(97)00189-4).
- Cappitelli, Villa & Sanmartín 2021, *Int Biodeterior Biodegrad* 163:105282, [10.1016/j.ibiod.2021.105282](https://doi.org/10.1016/j.ibiod.2021.105282); Cappitelli & Sorlini 2008, *Appl Environ Microbiol* 74:564–569, [10.1128/AEM.01768-07](https://doi.org/10.1128/AEM.01768-07).
- Pinheiro et al. 2019, "Fungi in archives, libraries, and museums", *Crit Rev Microbiol*, [10.1080/1040841X.2019.1690420](https://doi.org/10.1080/1040841X.2019.1690420).
- Karakasidou et al. 2018, *MicrobiologyOpen* 7:e00596, [10.1002/mbo3.596](https://doi.org/10.1002/mbo3.596).
- Callewaert et al. 2014, *Appl Environ Microbiol* 80:6611–6619, [10.1128/AEM.01422-14](https://doi.org/10.1128/AEM.01422-14).
- Sterndorff et al. 2020, *Environ Res* 185:109449, [10.1016/j.envres.2020.109449](https://doi.org/10.1016/j.envres.2020.109449).
- Møllebjerg et al. 2021, *Microbiol Spectr* 9:e01185-21, [10.1128/spectrum.01185-21](https://doi.org/10.1128/spectrum.01185-21) (erratum [10.1128/spectrum.02880-22](https://doi.org/10.1128/spectrum.02880-22)).
- Dang & Lovell 2016, *Microbiol Mol Biol Rev* 80:91–138, [10.1128/MMBR.00037-15](https://doi.org/10.1128/MMBR.00037-15).

**Explicitly my inference, not sourced:** (a) that GOLD's *Material* node means "bulk stock material as opposed to functioning artefact" — this is read off the sibling and child structure, since GOLD publishes no per-node definitions; (b) that the definition should leave the exemplar list open to metals/glass/concrete; (c) the boundary calls in §1, each of which is an argument from the shape of the GOLD tree rather than a claim any source makes.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**

- *material* (GOLD's own label; MIxS "surface material")
- *manufactured material*, *engineered material*, *fabricated material*
- *stock material*, *bulk material*
- *substratum* / *substrate* (in the biofilm-colonisation sense — but see the warning below)
- *material coupon* / *test specimen* (ISO 846, ASTM G21 usage for the sampled unit)

I would record at most *manufactured material* and *engineered material* as related synonyms. "Material" alone is too generic to serve as a synonym on any other record.

**Commonly conflated, and wrong**

| Do not conflate with | Why |
|---|---|
| `NCIT:C48187` *Material* | Label identity only; it is the generic substance-of-an-object sense and would let any soil, blood or rock sample fall under an engineered-product node. |
| ENVO *environmental material* / *anthropogenic environmental material* | Mass-noun branch; different commitment. Concrete and sludge are there; textiles and paper are not. |
| **"substrate" in the metabolic sense** | In microbiology "substrate" also means the compound being metabolised. The material-as-substratum sense is the intended one; the two collide constantly in the biodeterioration literature. |
| *Built environment surface* | Same materials, different sampled entity — the building surface *in situ*, where MIxS treats material as an attribute (`surf_material`) rather than the environment. |
| *Plastic marine debris / microplastic* (plastisphere) | Environmental setting, not industrial production. Same polymer, different habitat. |
| GOLD `Engineered > Paper` (and *Currency notes*) | A separate GOLD branch; "Paper" is duplicated in the GOLD tree. |
| *Biofilm* | The community on the material, not the material. GOLD models this separately (*Bioanode > Biofilm*, *Biocathode > Biofilm*), and ENVO has `ENVO:00002034` *biofilm*. |
| `FOODON:00003368` *food contact material* | Asserts a food-contact context the source path does not support. |

---

## 6. Should this be a term at all?

**It is a habitat, not a process, quality, disease or taxon.** A manufactured material is a physical place where microorganisms live and from which samples are taken; the biodeterioration literature and the ISO/ASTM test standards treat it as exactly that. So `NOT_APPLICABLE` would be the wrong disposition — it does not belong with the diseases, qualities and procedures the corpus reserves that for.

**But be honest about what kind of term it is.** Three facts argue it is a *grouping node* rather than a sampled habitat in its own right:

1. **Zero direct attestations** — 0 organisms, 0 studies, 0 biosamples on the node itself; the only volume in the subtree is 30 organisms on *Plastic*.
2. **Its children do not share one existing ENVO parent** — *plastic* is an environmental material, *textile* and *paper product* are manufactured products. A class whose members split across two disjoint upper branches is a convenience grouping, not a natural kind that ENVO has been missing.
3. **GOLD's own tree treats paper inconsistently**, giving it both an Ecosystem Category branch and a place under *Material*, which suggests the *Material* node was added pragmatically as projects arrived rather than designed.

**Recommendation.** Keep the concept (do not mark it `NOT_APPLICABLE`), keep it `UNGROUNDED`, and adopt `ENVO:00003074` *manufactured product* as `relation: parent` on the record so it stops being blocked in `needs_a_parent_first.tsv` — that parent is genuinely broader than the concept and asserts nothing the sources do not (every one of *plastic*, *fabric*, *paper* is human-processed). Then write the one-sentence definition at the top, and label it in the notes as a grouping class with no direct attestations.

If the project's policy is that a term request must be a habitat that something was actually sampled from, then the correct outcome is **no ENVO term request for *Material*** — instead request/ground the three children, of which two (`ENVO:02000001` textile, `ENVO:03501256` sheet of paper) are already grounded and one (`ENVO:06105101` plastic) is already parented. That would leave *Material* as a purely structural node inherited from GOLD, which is a defensible answer and cheaper than defending a definition for a class no sample was ever assigned to.

**Sources:**
- [GOLD v.9 (Mukherjee et al. 2023, NAR)](https://academic.oup.com/nar/article/51/D1/D957/6786204) · [GOLD v.8](https://academic.oup.com/nar/article/49/D1/D723/5957166)
- [ENVO in OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo) · [ENVO 2016 paper](https://doi.org/10.1186/s13326-016-0097-6)
- [MIxS surf_material](https://genomicsstandardsconsortium.github.io/mixs/0000758/) · [SurfMaterialEnum](https://genomicsstandardsconsortium.github.io/mixs/SurfMaterialEnum/) · [MIxS-BE](https://www.nature.com/articles/ismej2013176)
- [Zettler et al. 2013](https://doi.org/10.1021/es401288x) · [Amaral-Zettler et al. 2020](https://doi.org/10.1038/s41579-019-0308-0) · [Front Microbiol 2023 plastisphere review](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2023.1127308/full) · [Front Microbiol 2024 freshwater plastisphere](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2024.1395401/full)
- [Gu 2003](https://doi.org/10.1016/S0964-8305(02)00177-4) · [Flemming 1998](https://doi.org/10.1016/S0141-3910(97)00189-4) · [Cappitelli et al. 2021](https://doi.org/10.1016/j.ibiod.2021.105282) · [Cappitelli & Sorlini 2008](https://journals.asm.org/doi/full/10.1128/aem.01768-07)
- [Karakasidou et al. 2018](https://onlinelibrary.wiley.com/doi/full/10.1002/mbo3.596) · [Pinheiro et al. 2019](https://doi.org/10.1080/1040841X.2019.1690420)
- [Callewaert et al. 2014](https://journals.asm.org/doi/10.1128/aem.01422-14) · [Sterndorff et al. 2020](https://pubmed.ncbi.nlm.nih.gov/32278157/) · [Møllebjerg et al. 2021](https://journals.asm.org/doi/abs/10.1128/spectrum.01185-21) · [Dang & Lovell 2016](https://journals.asm.org/doi/10.1128/mmbr.00037-15)
- [ASTM G21](https://store.astm.org/g0021-21.html) · [ISO 846](https://www.iso.org/standard/74599.html) · [ISO 846 vs ASTM G21 comparison](https://microbe-investigations.com/blog/iso-846-vs-astm-g21-comparative-analysis-for-assessing-microbial-growth-in-plastics/)

## Citations

1. https://doi.org/10.1093/nar/gkac974
2. https://genomicsstandardsconsortium.github.io/mixs/0000758/
3. https://genomicsstandardsconsortium.github.io/mixs/SurfMaterialEnum/
4. https://doi.org/10.1038/ismej.2013.176
5. https://doi.org/10.1021/es401288x
6. https://doi.org/10.1038/s41579-019-0308-0
7. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00003074
8. https://doi.org/10.1128/MMBR.00037-15
9. https://doi.org/10.1016/S0141-3910(97
10. https://doi.org/10.1128/spectrum.01185-21
11. https://doi.org/10.1002/mbo3.596
12. https://doi.org/10.1080/1040841X.2019.1690420
13. https://doi.org/10.1016/S0964-8305(02
14. https://doi.org/10.1016/j.ibiod.2021.105282
15. https://store.astm.org/g0021-21.html
16. https://www.iso.org/standard/74599.html
17. https://doi.org/10.1128/AEM.01422-14
18. https://doi.org/10.1016/j.envres.2020.109449
19. https://www.ebi.ac.uk/ols4/ontologies/envo
20. https://doi.org/10.1186/2041-1480-4-43
21. https://doi.org/10.1186/s13326-016-0097-6
22. https://pubmed.ncbi.nlm.nih.gov/36318257/
23. https://academic.oup.com/nar/article/49/D1/D723/5957166
24. https://doi.org/10.3389/fmicb.2023.1127308
25. https://doi.org/10.3389/fmicb.2024.1395401
26. https://doi.org/10.1128/AEM.01768-07
27. https://doi.org/10.1128/spectrum.02880-22
28. https://academic.oup.com/nar/article/51/D1/D957/6786204
29. https://www.nature.com/articles/ismej2013176
30. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2023.1127308/full
31. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2024.1395401/full
32. https://journals.asm.org/doi/full/10.1128/aem.01768-07
33. https://onlinelibrary.wiley.com/doi/full/10.1002/mbo3.596
34. https://journals.asm.org/doi/10.1128/aem.01422-14
35. https://pubmed.ncbi.nlm.nih.gov/32278157/
36. https://journals.asm.org/doi/abs/10.1128/spectrum.01185-21
37. https://journals.asm.org/doi/10.1128/mmbr.00037-15
38. https://microbe-investigations.com/blog/iso-846-vs-astm-g21-comparative-analysis-for-assessing-microbial-growth-in-plastics/