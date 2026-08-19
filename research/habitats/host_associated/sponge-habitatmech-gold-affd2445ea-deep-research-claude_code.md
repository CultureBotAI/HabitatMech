---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:58:05.294995'
end_time: '2026-08-17T17:05:59.976917'
duration_seconds: 474.68
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Sponge
  habitat_identifier: habitatmech:GOLD.affd2445ea
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Porifera > Sponge'
  assertions: '323'
  parent_terms: ENVO:01001002
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Nearest
    broader term ENVO:01001002 ''animal-associated environment'' attached as a parent.
    Sponges as host. ENVO:01000161 marine sponge reef is the reef environment, not
    the sponge as a host, so it is not a substitute. Parented to animal-associated
    environment. ENVO term request. (source concept habitatmech:GOLD.affd2445ea)'
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
  web_search_requests: 14
  num_turns: 27
  total_cost_usd: 2.9094155000000006
  session_id: df4fd1a5-01cf-4a22-b035-fd140b650f1c
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 52
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Sponge
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.affd2445ea
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Porifera > Sponge
- **Upstream assertion volume:** 323
- **Nearest broader term already on the record:** ENVO:01001002
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:01001002 'animal-associated environment' attached as a parent. Sponges as host. ENVO:01000161 marine sponge reef is the reef environment, not the sponge as a host, so it is not a substitute. Parented to animal-associated environment. ENVO term request. (source concept habitatmech:GOLD.affd2445ea)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Sponge** as a microbial habitat, with citations.

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

# Sponge — `habitatmech:GOLD.affd2445ea`

## Proposed definition

> An animal-associated environment which is determined by a living sponge (Porifera), in which microorganisms inhabit the collagenous mesohyl and the aquiferous canal system perfused by ambient water that the host pumps.

Minimal variant, matching ENVO's existing sibling phrasing for `ENVO:01001179` *cnidarian-associated environment* ("An environmental system determined by a cnidarian or part of a cnidarian"), if the term request is written to ENVO's house style rather than HabitatMech's:

> An environmental system determined by a sponge or part of a sponge.

**One structural finding first, because it changes what the curator should do with this record:** the concept is a legitimate habitat, but it is *coextensive with its own parent record* `habitatmech:GOLD.64acf9132c` **Porifera**. See §6 — the disposition is probably `SAME_AS`, not a second term request.

---

## 1. What the concept denotes

**The reading the data means.** GOLD's five-level path is `Ecosystem = Host-associated → Ecosystem Category = Porifera → Ecosystem Type = Sponge`. The Ecosystem Category level under `Host-associated` is the host clade; the Ecosystem Type level here is the vernacular restatement of that clade. So "Sponge" denotes **the body of a living poriferan animal, sampled as the place a microbial community lives** — a piece of sponge tissue excised from a specimen, from which DNA is extracted. It is not the water around the sponge, not the substratum it grows on, and not a geological feature built from sponges.

Physically, the sampled material is:

- the **mesohyl** — a gelatinous collagenous extracellular matrix between the outer pinacoderm and the inner choanoderm, which is where the great majority of symbionts sit, extracellularly, concentrated around the choanocyte chambers ([Hentschel et al. 2012, *Nat Rev Microbiol* 10:641–654](https://doi.org/10.1038/nrmicro2839); [Taylor et al. 2007, *Microbiol Mol Biol Rev* 71:295–347](https://doi.org/10.1128/MMBR.00040-06));
- the **aquiferous system** — ostia, incurrent and excurrent canals, choanocyte chambers, osculum — continuously perfused with filtered ambient water ([Leys et al. 2011, *PLoS ONE* 6:e27787](https://doi.org/10.1371/journal.pone.0027787));
- the **surface/pinacoderm** and, in some taxa, **intracellular symbionts** in bacteriocytes and in oocytes, embryos and larvae ([Carrier et al. 2022, *BMC Biol* 20:100](https://doi.org/10.1186/s12915-022-01291-6)).

**Salinity and depth are not part of the boundary.** The concept covers marine sponges (~8,500 valid extant species, 83% Demospongiae — [Van Soest et al. 2012, *PLoS ONE* 7:e35105](https://doi.org/10.1371/journal.pone.0035105)) *and* freshwater Spongillida (>240 described species in continental waters on every continent except Antarctica — [Manconi & Pronzato 2008, *Hydrobiologia* 595:27–33](https://doi.org/10.1007/s10750-007-9000-x)), which have their own well-characterised, taxonomically distinct but functionally convergent microbiomes ([Sugden et al. 2022, *ISME J* 16:2503–2512](https://doi.org/10.1038/s41396-022-01296-7); [Laport et al. 2019, *Front Microbiol* 10:2799](https://doi.org/10.3389/fmicb.2019.02799)). **Do not write "marine" into the definition** — it would exclude an attested and actively studied part of the concept. Depth range runs from the intertidal to >8,800 m ([PORO:0000001 definition](https://www.ebi.ac.uk/ols4/ontologies/poro/classes?obo_id=PORO:0000001)).

**Inside the concept:** sponge tissue, mesohyl, canal system, sponge surface, sponge larvae and gemmules as habitat, HMA and LMA species alike, marine and freshwater, shallow and deep-sea.

**Neighbouring concepts, outside it:**

| Neighbour | Why it is outside |
|---|---|
| `ENVO:01000161` **marine sponge reef** | A marine *reef* — a seafloor feature of rock, gravel and boulders framed by Hexactinosa sponges. The place is the reef structure, not the animal as host. |
| `ENVO:01000123` **marine sponge reef biome** | Same failure at biome scale. |
| deep-sea **sponge grounds** | Dense sponge aggregations as a benthic setting; a seafloor habitat containing sponges ([Rooks et al. 2020, *Biogeosciences* 17:1231–1245](https://doi.org/10.5194/bg-17-1231-2020)). |
| ambient/exhalent **sea water** | The reference environment routinely sampled alongside sponges precisely *because* it is a different habitat; sponge communities are consistently distinct from it ([Thomas et al. 2016](https://doi.org/10.1038/ncomms11870); [Moitinho-Silva et al. 2017](https://doi.org/10.1093/gigascience/gix077)). |
| `habitatmech:GOLD.…` **Sponge > Tissue** (GOLD, 7 organisms) | GOLD's only child of this node. A tissue-level narrowing of the same host, not a different host. |
| **bath sponge / cleaning sponge**, `FOODON:03540256` sponge cake, `FOODON:03000109` sponge gourd, `UBERON:0001337` spongiose part of urethra | Pure string collisions (§5). |

**Ambiguity:** the bare string "sponge" has four live readings in biological vocabularies — (i) the poriferan animal, (ii) a sponge reef/ground, (iii) porous artificial material (cleaning sponge, foam), (iv) sponge cake / sponge gourd. The GOLD path `Host-associated > Porifera > Sponge` settles it unambiguously on (i).

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001002` *animal-associated environment*** — "An environmental system determined by an animal" (verified verbatim from [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002); synonyms *Metazoan-associated environment*, *animal environment*). This is already the parent on the record, and it is correct.

The decisive precedent is **`ENVO:01001179` *cnidarian-associated environment*** — "An environmental system determined by a cnidarian or part of a cnidarian" — which I verified sits as a **direct** subclass of `ENVO:01001002`. ENVO therefore already models exactly this pattern (a phylum-level host clade as an environment class) and places it directly under *animal-associated environment*. A *sponge-associated environment* / *poriferan-associated environment* term would be its sibling, and the request essentially writes itself.

### Near-misses, and why each fails

| Term | Verified definition | Verdict |
|---|---|---|
| `ENVO:01001176` **environment associated with an aquatic invertebrate** | "An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system." | **Truthful but structurally awkward.** Sponges do satisfy it. But I verified it has *two* parents — `ENVO:01001002` **and** `ENVO:01001055` *environment associated with an animal part or small animal*. Adopting it as genus imports an "animal part or small animal" implication that a 1-m *Xestospongia muta* barrel sponge does not satisfy. ENVO itself did not route *cnidarian-associated environment* through this term. **Recommend against**, and record it as the near-miss it is. |
| `ENVO:01000161` **marine sponge reef** | "A marine sponge reef is marine reefs primarily built by marine sponges. The primary frame-building sponges are all members of the order Hexactinosa. They are found only in glacier-scoured troughs of low-angle continental shelf. The seafloor is stable and consists of rock, coarse gravel, and large boulders." | **Fails on four independent assertions** — marine-only, reef-hood, Hexactinosa framebuilders, glacier-scoured trough setting. None is claimed by the GOLD data, which is dominated by demosponges. The existing curator note is right. |
| `ENVO:01000123` **marine sponge reef biome** | Reef biome. | Same, at biome scale. Narrower *and* wrong-kind. |
| `NCBITaxon:6040` **Porifera** | Taxon. | A class of organisms, not a place. Per repo policy (#99, #114): `relation: xref`, never grounding, never `parent_habitats`. |
| `PORO:0000001` **sponge** (Porifera Ontology) | "Sponge bodies consist of jelly-like mesohyl sandwiched between two thin layers of cells…" | An organism/anatomical term for the *whole* organism. Per the repo's host rule, whole-host organism terms do not ground a habitat. Also **not in the vendored slice** (ENVO/UBERON/FOODON/BTO/PO), and PORO is a low-activity OBO ontology. At most an `xref`. |
| `PORO:0000002` **mesohyl** | Anatomical structure. | **Narrower** than this concept — it is the part, not the host. Would be the natural ground for a mesohyl-specific record; not for this one. Same slice/activity caveat. |
| UBERON, BTO, FOODON | — | I searched all three: every "sponge" hit is `UBERON:0001337` spongiose urethra / `UBERON:0002483` trabecular bone, `BTO:0005402` spongiotrophoblast, `FOODON:03540256` sponge cake, `FOODON:03000109` sponge gourd, `FOODON:03412226` sponge crab family. **Nothing relevant, and a real automated-grounding hazard.** |

**Conclusion: no existing term names this concept.** `CONFIRM_UNGROUNDED` with `ENVO:01001002` as parent is correct, and the ENVO term request is well-founded.

---

## 3. Differentia — what distinguishes it from its siblings

Ordered by how observable and how load-bearing each is. Any one or two of the first three is enough for the definition sentence; the rest belong in the term-request comment.

**(a) The host is a sponge — a sessile, organ-less metazoan whose entire body is a filter pump.** Sponges lack nervous, digestive and circulatory systems and depend wholly on water flow through the aquiferous system ([PORO:0000001](https://www.ebi.ac.uk/ols4/ontologies/poro/classes?obo_id=PORO:0000001); [Taylor et al. 2007](https://doi.org/10.1128/MMBR.00040-06)). This is the primary contrast with *cnidarian-associated*, *fish-associated* and every gut/skin-based animal habitat: there is no lumen and no epithelial organ system — the habitat *is* connective tissue.

**(b) The habitat compartment is an extracellular collagenous matrix (mesohyl), not a lumen or an epithelial surface.** Symbionts are predominantly extracellular in the mesohyl, densest around choanocyte chambers ([Hentschel et al. 2012](https://doi.org/10.1038/nrmicro2839)). This contrasts directly with cnidarian symbiosis, where the defining symbionts are *intracellular* in gastrodermal cells.

**(c) Symbiont density is extreme and bimodal — the HMA/LMA dichotomy.** High-microbial-abundance sponges carry ~10⁸–10¹⁰ microbial cells g⁻¹ tissue, low-microbial-abundance sponges ~10⁵–10⁶ — two to four orders of magnitude apart; in HMA species microbial biomass can reach roughly one third of total sponge biomass ([Hentschel et al. 2012](https://doi.org/10.1038/nrmicro2839); [Gloeckner et al. 2014, *Biol Bull* 227:78–88](https://doi.org/10.1086/BBLv227n1p78), PMID [25216505](https://pubmed.ncbi.nlm.nih.gov/25216505/), a TEM survey of 56 species assigning 28 to each class, with Agelasida and Verongida exclusively HMA and Poecilosclerida exclusively LMA). The two classes differ measurably in tissue density and pumping: HMA species pump 52–94% slower per unit volume ([Weisz et al. 2008](https://pubmed.ncbi.nlm.nih.gov/18030495/)). *This is the single most quantitative, measurable differentia available.*

**(d) The habitat is continuously perfused with the surrounding water column, yet its community is distinct from it.** Sponges process many times their body volume per hour, and filtration is strongly modulated by ambient current — at one studied site, current speeds >15 cm s⁻¹ occurred only ~20% of the time yet accounted for about two-thirds of total filtered volume ([Leys et al. 2011](https://doi.org/10.1371/journal.pone.0027787)). Despite this, sponge communities separate cleanly from ambient seawater, sediment and adjacent biofilms in both marine and freshwater systems ([Thomas et al. 2016](https://doi.org/10.1038/ncomms11870); [Sugden et al. 2022](https://doi.org/10.1038/s41396-022-01296-7)).

**(e) Steep, temporally shifting redox structure at millimetre scale.** Many sponges cease pumping for hours at irregular intervals; actively pumping specimens hold internal O₂ near ambient, while non-pumping specimens develop a thickened diffusive boundary layer and internal anoxia, with anoxic zones co-occurring with sulfate reduction in *Geodia barretti* ([Hoffmann et al. 2008, *Mar Biol* 153:1257–1264](https://doi.org/10.1007/s00227-008-0905-3); [Schläppy et al. 2010, *Limnol Oceanogr* 55:1289–1300](https://doi.org/10.4319/lo.2010.55.3.1289)). Nitrification and denitrification have been demonstrated in both HMA and LMA sponges ([Schläppy et al. 2010, *Mar Biol* 157:593–602](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3873014/)); denitrification is common in boreo-Arctic deep-sea sponges ([Rooks et al. 2020](https://doi.org/10.5194/bg-17-1231-2020)).

**(f) The community is host-structured and partly heritable, with sponge-enriched lineages found nowhere else in abundance.** "Sponge-enriched" 16S clusters span ~14 bacterial and archaeal phyla and are monophyletic, indicating divergence from free-living relatives — a pattern not described for any other animal-associated symbiosis ([Webster & Thomas 2016, *mBio* 7:e00135-16](https://doi.org/10.1128/mBio.00135-16)). The candidate phylum **Poribacteria** was described from sponges and was long thought sponge-exclusive ([Fieseler et al. 2004, *Appl Environ Microbiol* 70:3724–3732](https://doi.org/10.1128/AEM.70.6.3724-3732.2004)). Of 33 sponge-specific clusters, 48% occurred only in adults and larvae, implying vertical transmission ([Webster et al. 2010, *Environ Microbiol* 12:2070–2082](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2936111/)); transmission is now understood as widespread but neither universal nor faithful ([Björk et al. 2019, *Nat Ecol Evol* 3:1172–1183](https://doi.org/10.1038/s41559-019-0935-x); [Carrier et al. 2022](https://doi.org/10.1186/s12915-022-01291-6)). Host phylogeny affects the *complexity* rather than the composition of the community, and the phylum-wide pattern is one of independent assembly with convergent organisation ([Thomas et al. 2016](https://doi.org/10.1038/ncomms11870)).

**(g) Ecologically, the habitat is a DOM-processing node.** Coral-reef sponges recycle dissolved organic matter into cellular detritus via rapid choanocyte turnover — the "sponge loop" — at rates approaching whole-reef gross primary production ([de Goeij et al. 2013, *Science* 342:108–110](https://doi.org/10.1126/science.1241981)). HMA sponges rely more on DOM, LMA more on particulate organic matter.

**Scale of the evidence base**, for the term request's justification: the Sponge Microbiome Project standardised 3,569 sponge specimens plus 370 seawater and 65 sediment controls from ≥268 sponge species worldwide, yielding 1.1 billion raw sequences and 39,543 closed-reference OTUs ([Moitinho-Silva et al. 2017, *GigaScience* 6:gix077](https://doi.org/10.1093/gigascience/gix077), PMID 29020741). GOLD's own 323 organism-level assertions on this node are a small slice of a very large, standardised literature.

---

## 4. Sources and what is inference

Every numeric and definitional claim above carries a DOI/PMID/URL inline. Explicit separation of what is **stated by a source** from what is **my inference**:

**Stated by sources:** all density figures, HMA/LMA class assignments, pumping-rate differentials, anoxia/pumping coupling, species counts, Sponge Microbiome Project sample counts, sponge-enriched cluster monophyly, vertical-transmission percentages, sponge-loop rates, and every ENVO/PORO/UBERON/FOODON/BTO label and definition quoted (all fetched verbatim from OLS4, not recalled).

**My inference, not stated by any source:**
1. That `ENVO:01001179` *cnidarian-associated environment* is the correct structural template for a sponge term request. (Its existence, definition, and direct parentage under `ENVO:01001002` are verified facts; that it should be the template is my reading.)
2. That `ENVO:01001176`'s second parent, *environment associated with an animal part or small animal*, makes it a poor genus for large sponges. (The dual parentage is verified; the objection is mine.)
3. That "Sponge" and "Porifera" are coextensive in the GOLD tree (§6). This follows from the extracted path table, but GOLD publishes no statement to that effect.
4. The claim that FOODON/UBERON/BTO "sponge" hits are a grounding hazard — the hits are verified, the hazard framing is mine.

**Standards/vocabulary references:** [ENVO](http://obofoundry.org/ontology/envo.html) and its descriptions ([Buttigieg et al. 2013, *J Biomed Semantics* 4:43](https://doi.org/10.1186/2041-1480-4-43); [Buttigieg et al. 2016, *J Biomed Semantics* 7:57](https://doi.org/10.1186/s13326-016-0097-6)); [GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification), whose documentation states the paths are sample-driven rather than a comprehensive enumeration and are periodically revised — directly relevant to §6.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept:**
- sponge, sponges (the overwhelmingly dominant term in the literature)
- Porifera, poriferan (clade name used interchangeably for the host)
- sponge tissue, sponge sample, sponge specimen (sampling-level usage)
- sponge-associated environment / sponge-associated habitat (the proposed ENVO label; "sponge-associated" is the standard adjectival form — e.g. "sponge-associated microorganisms", "sponge-associated prokaryotes")
- bacteriosponge (historical, for HMA species specifically — [Vacelet & Donadey usage carried into Gloeckner et al. 2014](https://doi.org/10.1086/BBLv227n1p78))
- **narrower, not synonyms:** mesohyl, choanosome, sponge ectosome, sponge larva

**Commonly but wrongly treated as the same thing:**
- **sponge reef / sponge ground / glass sponge reef** — a benthic geological–biogenic feature (`ENVO:01000161`, `ENVO:01000123`). Sponges are *in* it; it is not *them*.
- **sponge holobiont** — the host-plus-microbiota evolutionary unit ([Webster & Thomas 2016](https://doi.org/10.1128/mBio.00135-16); [Pita et al. 2018, *Microbiome* 6:46](https://doi.org/10.1186/s40168-018-0428-1)). Related and frequently swapped in, but a holobiont is an organismal unit, not a place.
- **sponge microbiome** — the community. A community is not a habitat.
- **sponge-associated seawater / exhalent water** — the ambient and exhaled water, sampled *as a control against* this habitat.
- **the taxon term Porifera (`NCBITaxon:6040`) / `PORO:0000001` sponge** — organism terms, per repo policy an `xref` only.
- **bath sponge, cleaning sponge, foamed plastic** (`ENVO:06105016`), **sponge cake** (`FOODON:03540256`), **sponge gourd** (`FOODON:03000109`), **sponge crab family** (`FOODON:03412226`), **spongiose urethra** (`UBERON:0001337`), **trabecular ("spongy") bone** (`UBERON:0002483`). All string collisions; every one of these is what a naive lexical search on "sponge" actually returns.

---

## 6. Should it be a term at all?

**Yes as a habitat — but probably not as a *separate* record from its parent.** Two distinct answers:

**(a) Is it a habitat?** Yes, unambiguously. A living sponge is where the microbes live, and ENVO already models organisms-as-environments at *plant-*, *animal-*, *fungi-* and *cnidarian-associated environment*. This is not a disease, quality, process or procedure, so `NOT_APPLICABLE` would be wrong. The existing `CONFIRM_UNGROUNDED` + `ENVO:01001002` parent + ENVO term request is the right disposition for the *concept*, and it is consistent with the #114 host-taxon reversal already recorded on the Porifera record.

**(b) Is it a *distinct* concept from `habitatmech:GOLD.64acf9132c` "Porifera"?** **No — I can find no difference in denotation, and the GOLD table is fairly direct evidence of that.** The full extracted branch is:

```
Host-associated > Porifera                    depth 2   4 nodes    90 organisms
Host-associated > Porifera > Sponge           depth 3   3 nodes   323 organisms
Host-associated > Porifera > Sponge > Tissue  depth 4   2 nodes     7 organisms
```

"Sponge" is the **only** Ecosystem Type under Porifera, and "Porifera" is the phylum whose members are exactly the sponges. There is no sibling type it discriminates against, and no property "Sponge" has that "Porifera" lacks. The depth-2 node is best read as the unspecified-type bin, not a broader kind. GOLD's own documentation says the classification is driven by curated samples and periodically revised, which is how a vernacular restatement of a clade ends up occupying its own level. Both records currently exist, both are `UNGROUNDED`, both are term-request candidates, and both would generate the *same* ENVO request — a duplicate submission from one repo.

**Recommended disposition: a `SAME_AS` decision**, which the corpus supports (`src/habitatmech/curate/decisions.py`, #116/#117) and which is precisely the mechanism for "two novel concepts are the same". Direction is the curator's call; my recommendation is **`Porifera` → `SAME_AS` → `Sponge`**, on two grounds: the surviving concept then carries 323 + 90 assertions rather than splitting them, and "sponge" is the label ENVO's own conventions would use (compare *marine sponge reef*, and *cnidarian-associated environment* using the vernacular clade adjective). Two caveats to check before writing the row:

1. `SAME_AS` here points a **parent** at its **child** in the GOLD path tree. The validator only rejects self-reference and cycles, so it should pass, but the seeder's `parent_habitats` handling for the merged record and for the surviving `Sponge > Tissue` child is worth verifying on a canary before `seed-apply`.
2. The merged record should keep `NCBITaxon:6040` as `relation: xref` (already on the Porifera record; **absent from the Sponge record and worth adding either way**), and may add `PORO:0000001` as a second xref — though PORO is outside the vendored slice, so that is a term-request comment rather than a record field.

**If the curator prefers to leave both records standing**, the definition above still applies verbatim to both, and the ENVO term request should be filed **once**, for a single class — not twice.

**Note on external submission:** filing an ENVO term request is an outward-facing action. Per the standing rule in memory, that needs an explicit yes for this specific request; this report does not authorise it.

---

## Sources

- [Thomas et al. 2016, *Nat Commun* 7:11870 — Diversity, structure and convergent evolution of the global sponge microbiome](https://www.nature.com/articles/ncomms11870) ([PMC4912640](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4912640/))
- [Moitinho-Silva et al. 2017, *GigaScience* 6:gix077 — The sponge microbiome project](https://academic.oup.com/gigascience/article/6/10/gix077/4082886) ([erratum](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6283209/))
- [Hentschel et al. 2012, *Nat Rev Microbiol* 10:641–654 — Genomic insights into the marine sponge microbiome](https://doi.org/10.1038/nrmicro2839)
- [Webster & Thomas 2016, *mBio* 7:e00135-16 — The Sponge Hologenome](https://journals.asm.org/doi/10.1128/mbio.00135-16)
- [Taylor et al. 2007, *Microbiol Mol Biol Rev* 71:295–347](https://doi.org/10.1128/MMBR.00040-06)
- [Gloeckner et al. 2014, *Biol Bull* 227:78–88 — The HMA-LMA dichotomy revisited](https://www.journals.uchicago.edu/doi/full/10.1086/BBLv227n1p78) ([PMID 25216505](https://pubmed.ncbi.nlm.nih.gov/25216505/))
- [Weisz et al. 2008 — Do associated microbial abundances impact marine demosponge pumping rates and tissue densities? (PMID 18030495)](https://pubmed.ncbi.nlm.nih.gov/18030495/)
- [Leys et al. 2011, *PLoS ONE* 6:e27787 — The Sponge Pump](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0027787)
- [de Goeij et al. 2013, *Science* 342:108–110 — Surviving in a marine desert: the sponge loop](https://doi.org/10.1126/science.1241981)
- [Hoffmann et al. 2008, *Mar Biol* — Oxygen dynamics and transport in the Mediterranean sponge *Aplysina aerophoba*](https://pmc.ncbi.nlm.nih.gov/articles/PMC3873076/)
- [Schläppy et al. 2010, *Mar Biol* 157:593–602 — Nitrification and denitrification in HMA and LMA sponges](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3873014/)
- [Rooks et al. 2020, *Biogeosciences* 17:1231–1245 — Deep-sea sponge grounds as nutrient sinks](https://bg.copernicus.org/articles/17/1231/2020/)
- [Fieseler et al. 2004, *Appl Environ Microbiol* 70:3724–3732 — Discovery of Poribacteria](https://doi.org/10.1128/AEM.70.6.3724-3732.2004)
- [Webster et al. 2010 — Deep sequencing reveals exceptional diversity and modes of transmission for bacterial sponge symbionts](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2936111/)
- [Björk et al. 2019, *Nat Ecol Evol* — Vertical transmission of sponge microbiota is inconsistent and unfaithful](https://www.nature.com/articles/s41559-019-0935-x)
- [Carrier et al. 2022, *BMC Biol* 20:100 — Symbiont transmission in marine sponges](https://link.springer.com/article/10.1186/s12915-022-01291-6)
- [Sugden et al. 2022, *ISME J* 16:2503–2512 — Microbiome of the freshwater sponge *Ephydatia muelleri*](https://www.nature.com/articles/s41396-022-01296-7)
- [Laport et al. 2019, *Front Microbiol* 10:2799 — Freshwater sponge *Tubella variabilis*](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2019.02799/full)
- [Freshwater sponges of the southeastern U.S. harbor unique microbiomes (PMC11787800)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11787800/)
- [Van Soest et al. 2012, *PLoS ONE* 7:e35105 — Global Diversity of Sponges (Porifera)](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0035105)
- [Manconi & Pronzato 2008, *Hydrobiologia* — Global diversity of freshwater sponges (Spongillina)](https://link.springer.com/article/10.1007/s10750-007-9000-x)
- [Lurgi et al. 2019, *Nat Commun* 10:992 — Modularity of the global sponge-microbiome network](https://www.nature.com/articles/s41467-019-08925-4)
- [Sponge-associated microbes in the twilight zone of Curaçao, *Symbiosis* 2024](https://link.springer.com/article/10.1007/s13199-024-00992-6)
- [High microbiome and metabolome diversification in coexisting sponges, *Commun Biol* 2024](https://www.nature.com/articles/s42003-024-06109-5)
- [Dynamic microbiome diversity shaping sponge holobiont adaptation, *Microbiol Spectr* 2024](https://journals.asm.org/doi/10.1128/spectrum.01448-24)
- ENVO/PORO/UBERON/BTO/FOODON term records fetched from [OLS4](https://www.ebi.ac.uk/ols4/); [ENVO at OBO Foundry](http://obofoundry.org/ontology/envo.html); [Buttigieg et al. 2013](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3904460/); [Buttigieg et al. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/)
- [JGI GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)

## Citations

1. https://doi.org/10.1038/nrmicro2839
2. https://doi.org/10.1128/MMBR.00040-06
3. https://doi.org/10.1371/journal.pone.0027787
4. https://doi.org/10.1186/s12915-022-01291-6
5. https://doi.org/10.1371/journal.pone.0035105
6. https://doi.org/10.1007/s10750-007-9000-x
7. https://doi.org/10.1038/s41396-022-01296-7
8. https://doi.org/10.3389/fmicb.2019.02799
9. https://www.ebi.ac.uk/ols4/ontologies/poro/classes?obo_id=PORO:0000001
10. https://doi.org/10.5194/bg-17-1231-2020
11. https://doi.org/10.1038/ncomms11870
12. https://doi.org/10.1093/gigascience/gix077
13. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
14. https://doi.org/10.1086/BBLv227n1p78
15. https://pubmed.ncbi.nlm.nih.gov/25216505/
16. https://pubmed.ncbi.nlm.nih.gov/18030495/
17. https://doi.org/10.1007/s00227-008-0905-3
18. https://doi.org/10.4319/lo.2010.55.3.1289
19. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3873014/
20. https://doi.org/10.1128/mBio.00135-16
21. https://doi.org/10.1128/AEM.70.6.3724-3732.2004
22. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2936111/
23. https://doi.org/10.1038/s41559-019-0935-x
24. https://doi.org/10.1126/science.1241981
25. http://obofoundry.org/ontology/envo.html
26. https://doi.org/10.1186/2041-1480-4-43
27. https://doi.org/10.1186/s13326-016-0097-6
28. https://gold.jgi.doe.gov/ecosystem_classification
29. https://doi.org/10.1186/s40168-018-0428-1
30. https://www.nature.com/articles/ncomms11870
31. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4912640/
32. https://academic.oup.com/gigascience/article/6/10/gix077/4082886
33. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6283209/
34. https://journals.asm.org/doi/10.1128/mbio.00135-16
35. https://www.journals.uchicago.edu/doi/full/10.1086/BBLv227n1p78
36. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0027787
37. https://pmc.ncbi.nlm.nih.gov/articles/PMC3873076/
38. https://bg.copernicus.org/articles/17/1231/2020/
39. https://www.nature.com/articles/s41559-019-0935-x
40. https://link.springer.com/article/10.1186/s12915-022-01291-6
41. https://www.nature.com/articles/s41396-022-01296-7
42. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2019.02799/full
43. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11787800/
44. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0035105
45. https://link.springer.com/article/10.1007/s10750-007-9000-x
46. https://www.nature.com/articles/s41467-019-08925-4
47. https://link.springer.com/article/10.1007/s13199-024-00992-6
48. https://www.nature.com/articles/s42003-024-06109-5
49. https://journals.asm.org/doi/10.1128/spectrum.01448-24
50. https://www.ebi.ac.uk/ols4/
51. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3904460/
52. https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/