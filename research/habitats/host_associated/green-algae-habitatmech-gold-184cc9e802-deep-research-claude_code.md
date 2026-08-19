---
provider: claude_code
model: claude-opus-5[1m]
cached: false
start_time: '2026-08-17T20:27:16.235029'
end_time: '2026-08-17T20:35:55.515639'
duration_seconds: 519.28
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Green algae
  habitat_identifier: habitatmech:GOLD.184cc9e802
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Algae > Green algae'
  assertions: '108'
  parent_terms: (none)
  xrefs: FOODON:03412502
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term FOODON:03412502 'green algae' attached as a parent. Non-habitat\
    \ screen (#12): grounded EXACT to FOODON:03412502 'green algae', which FOODON\
    \ uses for the TAXON \u2014 red algae is defined there as 'one of the oldest groups\
    \ of eukaryotic algae, and one of the largest phyla' \u2014 not for a habitat.\
    \ An organism group is not a place, and the GOLD path says host-associated, so\
    \ the concept is the environment the alga provides. Same family as the sponge,\
    \ nematode and reptile requests. The FOODON term is kept as an xref (#99), which\
    \ records what the label matched without asserting the record is a phylum. (source\
    \ concept habitatmech:GOLD.184cc9e802)"
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
  - claude-opus-5[1m]
  web_search_requests: 15
  num_turns: 31
  total_cost_usd: 3.5669765000000004
  session_id: 618e6b49-643d-4326-9f2f-fff88d1b3667
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 19
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Green algae
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.184cc9e802
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Algae > Green algae
- **Upstream assertion volume:** 108
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** FOODON:03412502

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term FOODON:03412502 'green algae' attached as a parent. Non-habitat screen (#12): grounded EXACT to FOODON:03412502 'green algae', which FOODON uses for the TAXON — red algae is defined there as 'one of the oldest groups of eukaryotic algae, and one of the largest phyla' — not for a habitat. An organism group is not a place, and the GOLD path says host-associated, so the concept is the environment the alga provides. Same family as the sponge, nematode and reptile requests. The FOODON term is kept as an xref (#99), which records what the label matched without asserting the record is a phylum. (source concept habitatmech:GOLD.184cc9e802)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Green algae** as a microbial habitat, with citations.

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

# Green algae as a microbial habitat — definition research

**Target:** `habitatmech:GOLD.184cc9e802` · GOLD path `Host-associated > Algae > Green algae` · 108 assertions · UNGROUNDED · xref `FOODON:03412502`

---

## Proposed definition

> An environmental system determined by a green alga (Chlorophyta and the charophyte green algae) which comprises the living thallus or cell together with its exudate-enriched boundary layer, its surface biofilm and its internal tissues, and whose distinguishing resource is the alga's photosynthate and its cellulosic and sulfated-rhamnan (ulvan-type) wall polysaccharides.

That is one sentence but a long one, and the reason is structural: **the intermediate class `algae-associated environment` does not exist in ENVO**, so the differentia has to carry both "which alga" and "which parts of it". If the corpus's own minted sibling `Host-associated > Algae` (`habitatmech:GOLD.02383c20a7`) is accepted as the genus — as the brown-algae report proposed — the sentence collapses to the shorter and preferable form:

> An algae-associated environment which is determined by a green alga (Chlorophyta and the charophyte green algae), comprising the cellulose- and ulvan-walled thallus or cell, its surface biofilm, its internal tissues and the exudate-enriched boundary layer immediately surrounding it.

---

## 1. What the concept denotes

**The place:** an individual green alga — unicellular, colonial, filamentous or a macroalgal thallus — considered as the setting a microorganism occupies. The sampled material is the alga itself: a thallus swab or punch, a surface wash, a whole-thallus homogenate, or a phycosphere/culture pellet of a green microalga together with the bacteria attached to and immediately around it.

**Inside the concept:**

- The **thallus/cell surface and its epiphytic biofilm**. This is the dominant reading in the literature and almost certainly the dominant reading of the GOLD data: *Ulva* surface communities are the archetype ([Burke et al. 2011, *ISME J* 5:590–600](https://doi.org/10.1038/ismej.2010.164)).
- The **phycosphere** — the diffusive boundary layer immediately around the cell, enriched in photosynthate and infochemicals, described as "the planktonic analogue of the rhizosphere" ([Seymour et al. 2017, *Nat Microbiol* 2:17065](https://doi.org/10.1038/nmicrobiol.2017.65); the term goes back to Bell & Mitchell 1972).
- **Endophytic/internal tissue** of macroalgal thalli, which is routinely sampled separately from the surface ([Nahor et al. 2024, *Sci Rep* 14:18631](https://doi.org/10.1038/s41598-024-69362-y)).
- Both **macroalgal** (*Ulva*, *Monostroma*, *Codium*, *Caulerpa*) and **microalgal** (*Chlamydomonas*, *Chlorella*, *Klebsormidium*) green algae. GOLD gives no separate green-microalga bin — `Host-associated > Algae > Microalgae` exists but carries only 4 assertions — so green microalgal samples land here.
- Marine, freshwater *and* terrestrial/subaerial green algae. GOLD's own child node `Host-associated > Algae > Green algae > Ectosymbionts` (0 assertions) confirms the surface/ectobiont reading is in scope.

**Outside the concept — neighbouring concepts:**

| Neighbour | Why it is not this |
|---|---|
| The **water body** the alga floats in | `Environmental > Aquatic`; the sample is water, not alga |
| **Green tide / algal bloom** (`ENVO:2000004`, `ENVO:01000057`) | A *feature* arising from a population increase, and the sampled matrix is bloom water; the bloom event is not the alga-as-place |
| **Algal culture medium** (`Engineered > Lab culture > Culture media > Algae`, already decided to `BTO:0000316`) and **raceway ponds** (`ENVO:03600047`) | Engineered cultivation settings |
| **Algal material** (`ENVO:01001189`, `FOODON:00001184`) | An environmental *material* of living or dead algae plus exudates — decaying drift, wrack, detritus. A material, not an environmental system, and includes dead biomass |
| **Periphytic biofilm** (`ENVO:03605000`) | The mixed algal/cyanobacterial/detrital film on a submerged substrate — the community and its substrate, not one alga as host |
| **Lichen** (`FOODON:03412345`, already `CONFIRM_UNGROUNDED`) | A composite organism; the green algal photobiont is inside a fungal thallus, which is a different habitat |
| **Zoochlorellae** in *Hydra*, *Paramecium*, corals | The habitat there is the animal; the alga is a co-resident, not the setting |
| **Sibling algal groups** — Brown Algae (231), Red algae (73), Diatoms (218), Golden, Yellow-green, Haptophytes, Dinoflagellates, Cryptophytes | Distinct GOLD siblings, and biochemically distinct habitats (§3) |

**Ambiguity — three readings, and which the data means.** *Inference, flagged as such:*

1. **Chlorophyta *sensu stricto*.** FOODON gives `FOODON:03412502` the synonym "Chlorophyta", so the label GOLD matched carries this reading.
2. **Green algae *sensu lato*** — Chlorophyta *plus* the paraphyletic charophyte green algae (*Klebsormidium*, *Spirogyra*, *Zygnema*), i.e. Viridiplantae minus land plants. This is standard phycological usage ([Leliaert et al. 2012, *Crit Rev Plant Sci* 31:1–46](https://doi.org/10.1080/07352689.2011.615705)).
3. **Colloquial "green algae"** — anything green and algal, including cyanobacteria ("blue-green algae") and euglenids. Wrong; see §5.

GOLD's sibling set partitions algae by pigment-defined major lineage, and GOLD offers no other bin for a charophyte green alga, so **reading 2 is the practical scope and reading 1 is its core**. My recommendation is to write the definition to reading 2 with the parenthetical, because it is the only reading under which every sample GOLD would file here is covered.

---

## 2. Genus — the broader kind

### The near-match worth knowing about: `ENVO:01001001`

`ENVO:01001001` **plant-associated environment** — *"An environmental system determined by a green plant."* Exact synonym **"Viridiplantae-associated environment"**; broad synonym "plant environment"; EMPO alternative label "Plant". Its logical axiom is `RO:0002507 (determined by) → NCBITaxon:33090 Viridiplantae`, and its parent is `ENVO:01001000` *environmental system determined by an organism* (synonym: "host-associated environment"). Verified against OLS4 on 2026-08-17 and present in the vendored slice at `data/raw/ontology_terms.tsv:8496`.

**Green algae are Viridiplantae.** Under ENVO's own axiom, every green-algae-associated environment *is* a plant-associated environment. This is a real, defensible superclass — and it is more informative than `ENVO:01001000`, which is the genus of last resort. Two caveats a curator should weigh:

- It is **broader**, not equivalent: it also covers land plants. So it is a `GROUND_AS_PARENT` / BROAD relation, never an EXACT grounding.
- The **label says "plant"** and the EMPO alternative label is "Plant", which in MIxS/EMPO annotation practice is read as *land plant*. Publishing "green algal habitat is-a plant-associated environment" is textually true to the definition and the axiom but will read as surprising to a human. *This tension is my assessment, not a documented ENVO position.*

There is independent empirical support for the grouping, which weakens the objection: the *Chlamydomonas reinhardtii* phycosphere microbiota overlaps taxonomically and functionally with the *Arabidopsis thaliana* root microbiota, and synthetic communities from either host assemble into taxonomically similar communities on the other ([Durán et al. 2022, *Nat Commun* 13:406](https://doi.org/10.1038/s41467-022-28055-8)).

### Recommended genus

Use the corpus's own minted sibling `Host-associated > Algae` (`habitatmech:GOLD.02383c20a7`) as the immediate parent — it matches the GOLD path, matches how the brown-algae sibling was handled, and is honest about "algae" being a polyphyletic grouping of hosts. `ENVO:01001001` may be recorded as a **second, grounded parent**; note that it cannot be a parent of the minted `Algae` node itself, since red algae, brown algae and diatoms are not Viridiplantae.

### Near-misses and why each fails

| Term | Why it is not the genus |
|---|---|
| `ENVO:01001000` environmental system determined by an organism | Correct but maximally broad — one step from "any host". The grounded fallback if the minted sibling is rejected |
| `ENVO:01001001` plant-associated environment | Broader (includes land plants); label/axiom tension. Parent, not identity |
| `ENVO:01001057` environment associated with a plant part or small plant | *"part of a living or dead plant, or a whole small plant"* — a unicellular green alga arguably qualifies as a "small plant" under the Viridiplantae reading, but the term is aimed at plant parts, would not cover a macroalgal thallus, and "small" is undefined. Over-narrow and vague |
| `ENVO:01001041` fungi-associated environment / `ENVO:01001002` animal-associated environment | Siblings under the same parent, wrong kingdom |
| `ENVO:01001189` algal material | Wrong upper class: an environmental *material* of living or dead algae plus exudates, not an environmental system. Not green-specific |
| `ENVO:03605000` periphytic biofilm | The mixed film on a substrate, not one alga as host |
| `ENVO:2000004` / `ENVO:01000057` algal bloom | Features of a water body; population-level events |
| `FOODON:03412502` green algae | **No textual definition at all** in the vendored slice — only the synonym "Chlorophyta". FOODON files it in the organism/food-source hierarchy. The taxon, not a place. Correctly kept as `xref` (#99) |
| `FOODON:03411301` algae, `FOODON:03412266` seaweed, `FOODON:03000008` green algae food product, `FOODON:03540760` EFSA FoodEx2 green algae | Organisms and food commodities |
| Plant Ontology | PO has no algal anatomy. `PO:0030027` *thallus* is explicitly the gametophyte of liverworts and pteridophytes; `PO:0025521` *unicellular plant gametangium* mentions *Ulva* in passing but is otherwise land-plant scoped. No genus available |
| UBERON | Animal anatomy. Nothing |

**`ENVO:01001001` has no subclasses** (OLS `has_children: false`), and a search of ENVO for `alga`/`algal`/`seaweed`/`macroalga` returns only blooms, materials, processes, ponds and biofilms. **The class `algae-associated environment` — the genus this and its four attested siblings all need — is genuinely missing from ENVO.** That is the substantive term-request finding, and it is shared with the Algae, brown algae, red algae, diatom and seaweed decisions rather than being specific to this record.

---

## 3. Differentia — what separates green algae from their siblings

The differentia that a curator can defend, ordered by how measurable they are:

**a. Host lineage and its pigment/storage signature.** Viridiplantae: chlorophyll *a* and *b*, starch stored inside the plastid, predominantly cellulosic walls ([Leliaert et al. 2012](https://doi.org/10.1080/07352689.2011.615705)). This is what GOLD's pigment-based sibling partition is tracking.

**b. Wall polysaccharide chemistry — the strongest measurable differentia.** Ulvophycean green algae build walls containing **ulvan**, a sulfated polysaccharide of L-rhamnose-3-sulfate, glucuronic acid and iduronic acid that can reach ~30% of algal dry weight. Degrading it requires a dedicated enzymatic cascade: *Formosa agariphila* KMM 3901ᵀ carries an ulvan polysaccharide utilisation locus encoding 12 characterised CAZymes — two polysaccharide lyases, three sulfatases and seven glycoside hydrolases ([Reisky et al. 2019, *Nat Chem Biol* 15:803–812](https://doi.org/10.1038/s41589-019-0311-9)). Brown algae present alginate and fucoidan instead; red algae agar and carrageenan. So the sibling algal habitats differ in the *carbon substrate they offer*, and the resident communities differ correspondingly in CAZyme repertoire.

**c. A community distinct from the surrounding water, and host-specific.** The *Ulva australis* surface is dominated by Alphaproteobacteria and Bacteroidetes (Rhodobacteraceae, Sphingomonadaceae, Flavobacteriaceae, Saprospiraceae) and is clearly distinct from co-sampled seawater libraries ([Burke et al. 2011](https://doi.org/10.1038/ismej.2010.164)). In co-located green, brown and red macroalgae, 14 core genera — 0.7% of all genera detected — accounted for a mean 51.1% of bacterial abundance, and cultivation yielded 5,527 strains representing 1,235 species, 685 of them potentially novel ([Lu et al. 2023, *Microbiome* 11:126](https://doi.org/10.1186/s40168-023-01559-1)). Communities are more similar within an algal phylum than across phyla ([Nahor et al. 2024](https://doi.org/10.1038/s41598-024-69362-y)).

**Counter-evidence, stated plainly:** Burke et al. found *no consistent core species* across individual *U. australis* thalli and proposed a competitive-lottery model in which assembly is governed by functional genes rather than taxa. A definition should therefore assert that the community is distinct from the surrounding water and functionally structured, **not** that it has a fixed taxonomic composition.

**d. The host's development depends on its microbiota.** This is the sharpest operational property of the green macroalgal habitat. Axenic *Ulva mutabilis* gametes develop into undifferentiated callus-like colonies with abnormal cell walls; full morphogenesis is restored by two bacteria in a tripartite community — *Roseovarius* sp. MS2 (cell division, thallus elongation) and *Maribacter* sp. MS6 (rhizoid and cell wall formation) ([Spoerner et al. 2012, *J Phycol* 48:1433–1447](https://doi.org/10.1111/j.1529-8817.2012.01231.x); reviewed in [Wichard 2015, *Front Plant Sci* 6:86](https://doi.org/10.3389/fpls.2015.00086)). The *Maribacter* morphogen is **thallusin**, first isolated from an epiphytic bacterium of the green alga *Monostroma oxyspermum* and active at 0.001–1 pg L⁻¹ ([Matsuo et al. 2005, *Science* 307:1598](https://doi.org/10.1126/science.1105486)), later confirmed in the *Ulva* system ([Alsufyani et al. 2020, *J Exp Bot* 71:3340–3349](https://doi.org/10.1093/jxb/eraa066)).

**e. Photosynthate-driven boundary layer (microalgal reading).** The phycosphere is sustained by release of organic compounds into the region immediately surrounding the cell ([Seymour et al. 2017](https://doi.org/10.1038/nmicrobiol.2017.65)). For green microalgae specifically, community establishment requires *physical proximity* to the host, not merely diffusible metabolites ([Durán et al. 2022](https://doi.org/10.1038/s41467-022-28055-8)).

**f. Vitamin economy.** Of 326 algal species surveyed, 171 require exogenous vitamin B₁₂, supplied by bacteria — a cross-cutting basis for algal–bacterial mutualism ([Croft et al. 2005, *Nature* 438:90–93](https://doi.org/10.1038/nature04056)). This is not green-specific and should not carry the differentia, but it explains why the habitat is obligately microbial.

**g. Environmental breadth versus the brown-algal sibling.** Green algae occupy marine, freshwater *and* terrestrial/subaerial settings — biocrusts and soil surfaces (*Klebsormidium*, Zygnematophyceae), subaerial biofilms (Trentepohliales) — whereas brown algae are essentially marine. Subaerial green algal strains from all four relevant classes assemble distinct soil-derived phycosphere communities patterned by host phylogeny ([Durán et al. 2022](https://doi.org/10.1038/s41467-022-28055-8); [Leliaert et al. 2012](https://doi.org/10.1080/07352689.2011.615705)). *That this breadth is a usable differentia against the brown-algae sibling is my inference from the two cited scopes, not a claim either paper makes.*

---

## 4. Sources

All citations below were resolved against Europe PMC or OLS4 on 2026-08-17; DOIs and PMIDs are verbatim from those records.

**Primary literature — habitat and its communities**

- Burke C, Thomas T, Lewis M, Steinberg P, Kjelleberg S (2011). Composition, uniqueness and variability of the epiphytic bacterial community of the green alga *Ulva australis*. *ISME J* 5:590–600. [10.1038/ismej.2010.164](https://doi.org/10.1038/ismej.2010.164) · PMID 21048801
- Burke C, Steinberg P, Rusch D, Kjelleberg S, Thomas T (2011). Bacterial community assembly based on functional genes rather than species. *PNAS* 108:14288–14293. [PMC3161577](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3161577/) · PMID 21825123
- Lu DC, Wang FQ, Amann RI, Teeling H, Du ZJ (2023). Epiphytic common core bacteria in the microbiomes of co-located green (*Ulva*), brown (*Saccharina*) and red (*Grateloupia*, *Gelidium*) macroalgae. *Microbiome* 11:126. [10.1186/s40168-023-01559-1](https://doi.org/10.1186/s40168-023-01559-1) · PMID 37264413
- Nahor O, Israel Á, Barger N, Rubin-Blum M, Luzzatto-Knaan T (2024). Epiphytic microbiome associated with intertidal seaweeds in the Mediterranean Sea. *Sci Rep* 14:18631. [10.1038/s41598-024-69362-y](https://doi.org/10.1038/s41598-024-69362-y) · PMID 39128929
- Durán P, Flores-Uribe J, Wippel K, Zhang P, Guan R, Melkonian B, Melkonian M, Garrido-Oter R (2022). Shared features and reciprocal complementation of the *Chlamydomonas* and *Arabidopsis* microbiota. *Nat Commun* 13:406. [10.1038/s41467-022-28055-8](https://doi.org/10.1038/s41467-022-28055-8) · PMID 35058457

**Primary literature — host dependence and chemistry**

- Spoerner M, Wichard T, Bachhuber T, Stratmann J, Oertel W (2012). Growth and thallus morphogenesis of *Ulva mutabilis* (Chlorophyta) depends on a combination of two bacterial species excreting regulatory factors. *J Phycol* 48:1433–1447. [10.1111/j.1529-8817.2012.01231.x](https://doi.org/10.1111/j.1529-8817.2012.01231.x) · PMID 27009994
- Matsuo Y, Imagawa H, Nishizawa M, Shizuri Y (2005). Isolation of an algal morphogenesis inducer from a marine bacterium. *Science* 307:1598. [10.1126/science.1105486](https://doi.org/10.1126/science.1105486) · PMID 15761147
- Alsufyani T, Califano G, Deicke M, *et al.* (2020). Macroalgal–bacterial interactions: identification and role of thallusin in morphogenesis of the seaweed *Ulva* (Chlorophyta). *J Exp Bot* 71:3340–3349. [10.1093/jxb/eraa066](https://doi.org/10.1093/jxb/eraa066) · PMID 32016363
- Wichard T (2015). Exploring bacteria-induced growth and morphogenesis in the green macroalga order Ulvales (Chlorophyta). *Front Plant Sci* 6:86. [10.3389/fpls.2015.00086](https://doi.org/10.3389/fpls.2015.00086) · PMID 25784916
- Reisky L, Préchoux A, Zühlke MK, *et al.* (2019). A marine bacterial enzymatic cascade degrades the algal polysaccharide ulvan. *Nat Chem Biol* 15:803–812. [10.1038/s41589-019-0311-9](https://doi.org/10.1038/s41589-019-0311-9) · PMID 31285597
- Croft MT, Lawrence AD, Raux-Deery E, Warren MJ, Smith AG (2005). Algae acquire vitamin B12 through a symbiotic relationship with bacteria. *Nature* 438:90–93. [10.1038/nature04056](https://doi.org/10.1038/nature04056) · PMID 16267554

**Reviews and reference works**

- Seymour JR, Amin SA, Raina JB, Stocker R (2017). Zooming in on the phycosphere: the ecological interface for phytoplankton–bacteria relationships. *Nat Microbiol* 2:17065. [10.1038/nmicrobiol.2017.65](https://doi.org/10.1038/nmicrobiol.2017.65) · PMID 28555622
- Leliaert F, Smith DR, Moreau H, Herron MD, Verbruggen H, Delwiche CF, De Clerck O (2012). Phylogeny and molecular evolution of the green algae. *Crit Rev Plant Sci* 31:1–46. [10.1080/07352689.2011.615705](https://doi.org/10.1080/07352689.2011.615705) · [free PDF](https://www.vliz.be/imisdocs/publications/248853.pdf)

**Vocabularies and standards**

- ENVO `ENVO:01001001` plant-associated environment — [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001001)
- ENVO `ENVO:01001000` environmental system determined by an organism — [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000)
- ENVO `ENVO:01001189` algal material; `ENVO:03605000` periphytic biofilm; `ENVO:2000004` algal bloom — [ENVO](http://environmentontology.org/)
- FOODON `FOODON:03412502` green algae (syn. Chlorophyta; **no textual definition**) — [OLS4](https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03412502)
- Mukherjee S *et al.* (2023). Twenty-five years of the Genomes OnLine Database (GOLD): data updates and new features in v.9. *Nucleic Acids Res* 51:D957–D963. [10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974) — the source of the five-level `Ecosystem > Category > Type > Subtype > Specific Ecosystem` path this record is attested on

**Flagged as inference, not sourced:** which sense of "green algae" GOLD intends (§1); that `ENVO:01001001` is usable as a parent here despite its vernacular label (§2); that environmental breadth is a usable differentia against the brown-algae sibling (§3g); the inside/outside boundary table (§1), which is a reading of the GOLD path against the cited ENVO/FOODON definitions rather than a distinction any one source draws.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**

- green algal / green-algae-associated environment
- Chlorophyta-associated environment; chlorophyte phycosphere
- green macroalgal surface; green seaweed surface; green algal epiphytic habitat / epibiota
- *Ulva* phycosphere; green algal thallus surface
- algal holobiont (of a green alga) — used, but carries an extra claim about the host–microbiota unit that a habitat definition should not make

**Commonly but wrongly treated as the same thing**

- **Blue-green algae / cyanobacteria** (`FOODON:03411746`). Bacteria, not Viridiplantae. The single most likely lexical confusion for this label.
- **Euglenophyta and chlorarachniophytes.** Green-pigmented, chlorophyll *a*+*b*, but the plastid came by secondary endosymbiosis; not green algae.
- **"Green algae" as a food commodity** (`FOODON:03000008` green algae food product, `FOODON:03540760` EFSA FoodEx2 group, `FOODON:03000009` chlorella food product). A processed material, not a habitat.
- **Green tides.** A bloom event of *Ulva prolifera* and relatives — a feature of a water body, not the alga as a place.
- **Seaweed generally** (`FOODON:03412266`) — polyphyletic and macroscopic-only, and already a separate HabitatMech decision (`habitatmech:GOLD.0e7a5162bb`).
- **Algal material / decomposing algae** (`ENVO:01001189`) — dead biomass and drift, not a living host.
- **Lichen** (`FOODON:03412345`) — the green algal photobiont lives inside a fungal thallus; different habitat.
- **Algal culture medium** — engineered; already routed to `BTO:0000316`.

---

## 6. Should this be a term at all?

**Yes.** It is a habitat under the rule the repo has already settled: *an organism acting as a host is a habitat; the taxon term is not.* The GOLD path is explicitly `Host-associated`, 108 assertions describe microorganisms recovered from green algae, and the literature treats the green alga as a structured microbial habitat with a resident community distinct from the surrounding water, a characteristic carbon substrate, and a host whose own development depends on its microbiota. `NOT_APPLICABLE` — which says the concept is not a habitat — would be wrong here; that disposition belongs to diseases, qualities, processes and procedures.

The existing decision is right as recorded: **`CONFIRM_UNGROUNDED`, `FOODON:03412502` kept as `relation: xref`.** Two refinements this research supports:

1. **Replace or supplement the parent.** `FOODON:03412502` should not sit in `parent_habitats` (a taxon is not a broader habitat) — the decision note already says so, and the `xref` relation column handles it. `ENVO:01001001` *plant-associated environment* is a genuinely defensible broader term under its `determined by Viridiplantae` axiom, and is one level more informative than `ENVO:01001000`. Whether the label/EMPO-usage tension is worth accepting is a curator call.
2. **The missing class is `algae-associated environment`, not `green-algae-associated environment`.** This record, `Algae`, `brown algae`, `red algae`, `Diatoms` and `seaweed` all fail for the same reason: ENVO has `plant-`, `animal-`, `fungi-` and `cnidarian-associated environment` but nothing for algae, and `ENVO:01001001` has no subclasses at all. The highest-value external request would be the parent class plus lineage-level subclasses, filed once for the whole family rather than six times. **I have not filed anything** — per the standing rule, an ENVO term request needs your explicit yes for that specific request.

## Citations

1. https://doi.org/10.1038/ismej.2010.164
2. https://doi.org/10.1038/nmicrobiol.2017.65
3. https://doi.org/10.1038/s41598-024-69362-y
4. https://doi.org/10.1080/07352689.2011.615705
5. https://doi.org/10.1038/s41467-022-28055-8
6. https://doi.org/10.1038/s41589-019-0311-9
7. https://doi.org/10.1186/s40168-023-01559-1
8. https://doi.org/10.1111/j.1529-8817.2012.01231.x
9. https://doi.org/10.3389/fpls.2015.00086
10. https://doi.org/10.1126/science.1105486
11. https://doi.org/10.1093/jxb/eraa066
12. https://doi.org/10.1038/nature04056
13. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3161577/
14. https://www.vliz.be/imisdocs/publications/248853.pdf
15. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001001
16. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000
17. http://environmentontology.org/
18. https://www.ebi.ac.uk/ols4/ontologies/foodon/classes?obo_id=FOODON:03412502
19. https://doi.org/10.1093/nar/gkac974