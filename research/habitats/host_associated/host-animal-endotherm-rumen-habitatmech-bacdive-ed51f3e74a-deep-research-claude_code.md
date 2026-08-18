---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T20:20:08.525259'
end_time: '2026-08-17T20:27:09.347813'
duration_seconds: 420.82
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: host_animal_endotherm_rumen
  habitat_identifier: habitatmech:BACDIVE.ed51f3e74a
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'MADIN: host_animal_endotherm_rumen'
  assertions: '132'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Reviewed and endorsed the seeder's own resolution. Category override\
    \ (#57): a minted identifier gives infer_category nothing to read \u2014 no ontology\
    \ term, no GOLD path \u2014 so every Madin habitat named in the BacDive vocabulary\
    \ fell to OTHER. The rumen is an anatomical compartment of a warm-blooded host,\
    \ so HOST_ASSOCIATED rather than the FOOD its contents came from. (source concept\
    \ habitatmech:BACDIVE.ed51f3e74a)"
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
  web_search_requests: 6
  num_turns: 32
  total_cost_usd: 2.5436425000000003
  session_id: bbb6f736-1f10-4a1b-a646-89045ad7314e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 19
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** host_animal_endotherm_rumen
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.ed51f3e74a
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** MADIN: host_animal_endotherm_rumen
- **Upstream assertion volume:** 132
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Reviewed and endorsed the seeder's own resolution. Category override (#57): a minted identifier gives infer_category nothing to read — no ontology term, no GOLD path — so every Madin habitat named in the BacDive vocabulary fell to OTHER. The rumen is an anatomical compartment of a warm-blooded host, so HOST_ASSOCIATED rather than the FOOD its contents came from. (source concept habitatmech:BACDIVE.ed51f3e74a)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **host_animal_endotherm_rumen** as a microbial habitat, with citations.

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

# host_animal_endotherm_rumen — definition research

**Concept:** `habitatmech:BACDIVE.ed51f3e74a` · label `host_animal_endotherm_rumen` · HOST_ASSOCIATED · UNGROUNDED · 132 MADIN taxon assertions

---

> **A ruminant forestomach compartment which functions as a continuously-fed anaerobic fermentation chamber, held near 39 °C and near-neutral pH, in which a dense resident community of bacteria, methanogenic archaea, ciliate protozoa and anaerobic fungi hydrolyses and ferments ingested plant polysaccharides to volatile fatty acids, CO₂ and CH₄ before the digesta reaches the host's acid stomach.**

**But the more important finding first: this concept should almost certainly not get a minted term at all.** A term naming it exactly already exists, is already in this repo's vendored slice, and is already a REVIEWED record in this corpus. See §6 — the recommended disposition is `GROUND` to `UBERON:0007365` *rumen*, not a term request. The sentence above is offered as the habitat-framed gloss for the merged record; UBERON's own definition is what the record would carry.

---

## 1. What the concept denotes

**The physical place:** the rumen — the first and largest compartment of the four-chambered ruminant stomach, an anaerobic, muscular, keratinised-epithelium-lined sac that occupies most of the left side of the abdomen and holds the fermenting digesta mass. A sample "from the rumen" is rumen contents: the liquid (planktonic) fraction, the fibrous mat/solid fraction, or a scraping of the epimural (epithelium-attached) community.

**What the label's parts mean.** `host_animal_endotherm_rumen` is a node in the isolation-source hierarchy of Madin et al.'s condensed traits synthesis, sitting under `host_animal_endotherm` alongside `host_animal_endotherm_intratissue` ([Madin et al. 2020, *Sci Data* 7:170, doi:10.1038/s41597-020-0497-4](https://doi.org/10.1038/s41597-020-0497-4), PMID 32503990). The `endotherm` prefix is a facet of *Madin's own tree* — how it partitions animal hosts — not a differentia of the habitat. All extant ruminants are mammals and therefore endotherms, so the qualifier restricts nothing (*this last step is my inference from ruminant taxonomy, not a sourced claim*). **The differentia in the definition should not mention endothermy.**

**What the bin actually contains.** The mapping table that builds this category is decisive about the intended reading. `renaming_isolation_source.csv` in the [bacteria-archaea-traits repository](https://github.com/bacteria-archaea-traits/bacteria-archaea-traits) folds these raw strings into `host_animal_endotherm_rumen`:

- `host-associated, mammals, digestive system, foregut, rumen` (and `…, free living` / `…, symbiotic` / `…, symbiotic, commensal` variants)
- `host-associated, mammals, digestive system, stomach, rumen`
- `digesta samples from rumen`, `bovine rumen`, `bovine rumen fluid`, `rumen fluid`
- `rumen content of yak`, `rumen of yak`, `rumen of korean native cattle`

So the bin is *the rumen and its contents, from any ruminant host*, and it explicitly absorbs the GOLD paths `Host-associated > Mammals > Digestive system > Foregut > Rumen` and `… > Stomach > Rumen` — the same two GOLD leaves that already exist in this corpus as `rumen__e748f14c` (`gold.ecosystem:7512`, 4 989 organisms) and `rumen__a12a98cc` (`gold.ecosystem:4111`, 450 organisms), both parented to `UBERON:0007365`.

**Boundary — inside:** rumen fluid, rumen solid/fibre-adherent digesta, rumen epimural scrapings, whole "bovine rumen" isolations. **Boundary — outside:** the reticulum, omasum and abomasum (separate UBERON terms, all four in the slice); the intestines (`ENVO:2100002` *intestine environment*); faeces (`ENVO:00002003`); and the non-ruminant foregut fermentation chambers listed in §5.

**Ambiguity:** the label is not ambiguous in its source. It is only ambiguous in a way English is — "rumen" is used loosely for the reticulorumen as a functional unit, and the reticulum and rumen communicate freely across a shared wall and are usually sampled together. The source path pins the narrow reading (the rumen proper); the practical reading in the literature is the reticulorumen. `UBERON:0007364` *reticulorumen* exists in UBERON but is **not** in this repo's vendored slice (verified against `data/raw/ontology_terms.tsv`), so it is not an available target regardless.

## 2. Genus — the broader kind

**Recommended genus: `UBERON:0007359` *ruminant forestomach*** — "Any of the first three stomachs of a ruminant, i.e., the rumen, reticulum, or omasum." Present in the slice. This is also the shape the corpus already uses: `data/habitats/host_associated/rumen.yaml` (the PREGO-attested `BTO:0001194` record) carries `parent_habitats: [BTO:0000480]` — BTO's *forestomach*, the same kind.

**Near-misses, and why each fails:**

| Candidate | In slice? | Why it is not the genus |
|---|---|---|
| `ENVO` — any rumen/ruminal/forestomach term | — | **ENVO has none.** An OLS4 query for `rumen OR ruminal OR forestomach` restricted to ENVO returns zero documents ([OLS4 API](https://www.ebi.ac.uk/ols4/api/search?q=rumen&ontology=envo)). This is the answer to "check ENVO first": ENVO models the *environmental-system* layer here and stops well short of ruminant anatomy. |
| `ENVO:01001033` *digestive tract environment* | yes | Correct in kind but far too broad — it covers every gut of every animal. Usable as a broad parent; useless as the definitional genus. |
| `ENVO:01001002` *animal-associated environment* | yes | Broader still; the top of the host-associated branch. |
| `ENVO:2100002` *intestine environment* | yes | Wrong compartment — the rumen is a stomach chamber, not intestine. |
| `UBERON:0007364` *reticulorumen* | **no** | Arguably the *better* parent, since rumen and reticulum are one functional fermentation unit — but absent from the vendored slice, so unusable without vendoring more UBERON (cf. #10). |
| `UBERON:0007366` *ruminant stomach*, `UBERON:0010228` *ruminal fluid* | **no** | Both real UBERON terms, both absent from the slice. Worth noting because `ruminal fluid` is what the corpus's `rumen_fluid__18e64978` record would otherwise want. |
| `BTO:0000480` *forestomach* | yes | Fine, and already in use as the parent of the BTO rumen record. Redundant with `UBERON:0007359`. |
| `ENVO:02000026` *chyme material* | yes | Names the *contents*, not the compartment, and chyme is defined as post-stomach pre-duodenal material — a different stage of digestion. |

## 3. Differentia — what distinguishes it

Observable/measurable properties that separate the rumen from its siblings under "ruminant forestomach" and from other gut habitats:

- **Position and function:** first compartment of the ruminant stomach, upstream of the acid-secreting abomasum, so microbial fermentation precedes host digestion. It "lies on the left side of the body, occupying the whole of the left side of the abdomen… divided into an upper and a lower sac, each of which has a blind sac at its posterior extremity" ([UBERON:0007365](http://purl.obolibrary.org/obo/UBERON_0007365)). Anatomically demarcated by pillars, grooves and folds into five sacs — cranial, dorsal, ventral, caudodorsal blind and caudoventral blind ([Soltis et al. 2023, *Microorganisms* 11:747, doi:10.3390/microorganisms11030747](https://doi.org/10.3390/microorganisms11030747)) — a partition GOLD mirrors as five separate leaves, all already grounded here as NARROW under `UBERON:0007365`.
- **Volume:** large. Reticulorumen capacity is commonly given as ~35–100 L in cattle and ~3–5 L in sheep, ~62 % of total stomach capacity in mature cattle ([Mississippi State Extension, *Understanding the Ruminant Animal Digestive System*](https://extension.msstate.edu/publications/understanding-the-ruminant-animal-digestive-system); [Colorado State, *Rumen Physiology and Rumination*](https://vivo.colostate.edu/hbooks/pathphys/digestion/herbivores/rumination.html)). Ranges across sources are wide; cite a range, not a point value.
- **Strictly anaerobic and strongly reducing.** Redox potential in the rumen medium is reported at roughly −130 to −200 mV, with values across the ruminant digestive tract spanning −300 to +200 mV; all ruminal values are markedly negative, reflecting oxygen absence and strong reducing power. Eh correlates negatively with pH, total VFA and acetate proportion, positively with propionate ([Huang et al. 2018, *J Anim Physiol Anim Nutr*, doi:10.1111/jpn.12855](https://doi.org/10.1111/jpn.12855), PMID 29352497).
- **Near-neutral, diet-buffered pH:** mean ~6.5, varying by sac (cranial sac highest) and with diet ([Soltis et al. 2023](https://doi.org/10.3390/microorganisms11030747)).
- **Host body temperature, ~39 °C** — the standard in vitro incubation temperature precisely because it reproduces in vivo conditions ([Wang et al. 2017, *Front Microbiol* 8:1864, doi:10.3389/fmicb.2017.01864](https://doi.org/10.3389/fmicb.2017.01864)).
- **Exceptional microbial density and four-domain-spanning composition:** bacteria ~10¹⁰–10¹¹ mL⁻¹ of rumen fluid, archaea (all methanogens) 10⁸–10⁹ mL⁻¹, ciliate protozoa ~10⁶ mL⁻¹ (up to half the microbial biomass by volume), anaerobic fungi ~10⁶ mL⁻¹ ([Wang et al. 2017](https://doi.org/10.3389/fmicb.2017.01864)). The classic Hungate roll-tube figure of 10⁹–10¹⁰ bacteria mL⁻¹ ([Hungate, *The Rumen and Its Microbes*, Academic Press, 1966](https://doi.org/10.1016/B978-1-4832-3308-6.X5001-4)) is lower because it counts viable cells.
- **Fermentation output as the defining process:** plant cell-wall polysaccharides → volatile fatty acids + microbial protein + CO₂ + H₂, with H₂ removed by methanogens to CH₄ and eructated. Interspecies H₂ transfer keeps H₂ partial pressure low enough for fermentation to stay thermodynamically favourable ([Greening & Rushton-Green 2024 review, PMC10838669](https://pmc.ncbi.nlm.nih.gov/articles/PMC10838669/); [Ungerfeld 2012, PMID 22444607](https://pubmed.ncbi.nlm.nih.gov/22444607/)).
- **Short residence time** relative to other anaerobic habitats: digesta turns over once or twice per day, versus >14–20 days in anaerobic digesters and years in sediments — which is *why* fermentation is incomplete and yields VFA rather than full mineralisation. (Sourced to the comparative gut-anaerobe framing in [Greening et al., *Animal Microbiome* 2022, doi:10.1186/s42523-022-00174-z](https://doi.org/10.1186/s42523-022-00174-z).)
- **Internally structured, not a stirred tank.** Four distinct micro-habitats — planktonic/liquid, fibre-adherent solid, epimural, protozoa-associated — with the fibre-adherent fraction holding the greatest share of bacterial biomass and the epimural community markedly less diverse. VFA concentrations run ~38 % higher in dorsal than ventral regions ([Soltis et al. 2023](https://doi.org/10.3390/microorganisms11030747); [Jiang et al. 2022, PMC9161295](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9161295/)).
- **Globally conserved core community:** across 742 samples from 32 ruminant species in 35 countries, the same bacteria and archaea dominate nearly everywhere; diet explains community differences more than host species does ([Henderson et al. 2015, *Sci Rep* 5:14567, doi:10.1038/srep14567](https://doi.org/10.1038/srep14567), PMID 26449758, PMCID PMC4598811). The corresponding cultured reference set is Hungate1000 ([Seshadri et al. 2018, *Nat Biotechnol*, doi:10.1038/nbt.4110](https://doi.org/10.1038/nbt.4110)).

The record's own `characteristic_taxa` corroborate the reading independently: *Ruminococcus flavefaciens*, *Butyrivibrio fibrisolvens*, *Selenomonas ruminantium*, *Prevotella albensis*, *Succiniclasticum ruminis*, *Megasphaera elsdenii*, *Acetitomaculum ruminis* — the canonical rumen fibrolytic/fermentative guild.

## 4. Sources

Consolidated, all resolvable:

| Claim | Source |
|---|---|
| Isolation-source hierarchy and provenance of the label | [Madin et al. 2020, *Sci Data* 7:170, doi:10.1038/s41597-020-0497-4](https://doi.org/10.1038/s41597-020-0497-4) (PMID 32503990, PMCID PMC7275036); mapping table at [bacteria-archaea-traits/data/conversion_tables/renaming_isolation_source.csv](https://github.com/bacteria-archaea-traits/bacteria-archaea-traits) |
| Anatomy, sacs, per-region pH and VFA, micro-habitats | [Soltis et al. 2023, *Microorganisms* 11:747, doi:10.3390/microorganisms11030747](https://doi.org/10.3390/microorganisms11030747) (PMC10057925) |
| Redox potential as an intrinsic rumen parameter | [Huang et al. 2018, *J Anim Physiol Anim Nutr*, doi:10.1111/jpn.12855](https://doi.org/10.1111/jpn.12855) (PMID 29352497) |
| Microbial densities by domain; 39 °C | [Wang et al. 2017, *Front Microbiol* 8:1864, doi:10.3389/fmicb.2017.01864](https://doi.org/10.3389/fmicb.2017.01864) |
| Global core rumen microbiome | [Henderson et al. 2015, *Sci Rep* 5:14567, doi:10.1038/srep14567](https://doi.org/10.1038/srep14567) (PMCID PMC4598811) |
| Cultured reference genomes | [Seshadri et al. 2018, *Nat Biotechnol* 36:359, doi:10.1038/nbt.4110](https://doi.org/10.1038/nbt.4110) |
| Foundational monograph; classic density figures | Hungate RE, *The Rumen and Its Microbes*, Academic Press, 1966, [doi:10.1016/B978-1-4832-3308-6.X5001-4](https://doi.org/10.1016/B978-1-4832-3308-6.X5001-4) |
| Micro-environment community differences | [Jiang et al. 2022, *Front Microbiol*, PMC9161295](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9161295/) |
| H₂/formate flux, interspecies transfer, turnover-time contrast | [Greening et al. 2022, *Animal Microbiome* 4:22, doi:10.1186/s42523-022-00174-z](https://doi.org/10.1186/s42523-022-00174-z); [PMC10838669](https://pmc.ncbi.nlm.nih.gov/articles/PMC10838669/) |
| Convergent foregut fermentation outside Ruminantia | [Godoy-Vitorino et al. 2012, *ISME J* 6:531, doi:10.1038/ismej.2011.131](https://doi.org/10.1038/ismej.2011.131); [Grajal et al. 1989, *Science* 245:1236, doi:10.1126/science.245.4923.1236](https://doi.org/10.1126/science.245.4923.1236) |
| Capacity figures (range, low confidence — extension literature, wide variance) | [MSU Extension](https://extension.msstate.edu/publications/understanding-the-ruminant-animal-digestive-system); [Colorado State](https://vivo.colostate.edu/hbooks/pathphys/digestion/herbivores/rumination.html) |
| Term availability | [UBERON:0007365](http://purl.obolibrary.org/obo/UBERON_0007365); [BTO:0001194](http://purl.obolibrary.org/obo/BTO_0001194); [OLS4 ENVO query returning zero rumen terms](https://www.ebi.ac.uk/ols4/api/search?q=rumen&ontology=envo) |

**Explicitly my inference, not sourced:** (a) that `endotherm` is a Madin hierarchy artefact rather than a habitat property; (b) that Madin's bin is *slightly broader* than the UBERON organ because it absorbs rumen-fluid strings; (c) the slice-membership findings in §2, which are facts about this repo (`data/raw/ontology_terms.tsv`), not about the literature.

## 5. Synonyms, and what not to conflate

**Real synonyms / names in use:** *rumen*; *paunch* (UBERON exact synonym; also PREGO's `paunch`/`paunches`/`rumens`); *ruminal contents*, *rumen contents*, *rumen digesta*, *ruminal fluid*, *rumen liquor*, *strained rumen fluid* (all name the material, not the compartment); *first stomach*; *reticulorumen* and *fermentation vat* as the standard functional framing in the veterinary/extension literature.

**Do not conflate:**

1. **Termite hindgut "paunch" (P3 segment).** The word is shared and nothing else — the rumen is a mammalian *foregut* compartment; the termite paunch is an insect *hindgut* segment. ⚠️ **This conflation is live in the corpus right now:** `habitatmech:GOLD.86aef52360` grounds GOLD's `Host-associated > Arthropoda: Insects > Digestive system > Hindgut > Paunch/P3 segment` to `UBERON:0007365` as EXACT ("The paunch is the rumen"), and the resulting record `rumen__a47ac48b.yaml` now carries `Paunch/P3 segment` as a synonym of *rumen*. This is structurally the same error as the beehive-cerumen case (`GOLD.a3c5e2adba`), where the curator correctly refused the shared-word match. **Worth a separate issue.**
2. **Non-ruminant foregut fermenters.** Camelid C1–C3 compartments (pseudoruminant; three-chambered, no true rumen), macropod sacciform/tubiform forestomach, colobine sacculated stomach, hoatzin crop. Foregut fermentation arose independently in each lineage — molecular-clock analyses find no shared origin — and microbial community structure converges even though the organs are not homologous ([Godoy-Vitorino et al. 2012](https://doi.org/10.1038/ismej.2011.131); [Grajal et al. 1989](https://doi.org/10.1126/science.245.4923.1236)). These need `<X>-associated` or their own anatomy terms, never `UBERON:0007365`.
3. **`UBERON:0008827` murine forestomach.** Present in the slice, non-glandular, not a fermentation chamber, not homologous.
4. **Reticulum / omasum / abomasum** (`UBERON:0007361` / `:0007362` / `:0007358`), all in the slice as distinct terms. In particular the abomasum is the acid "true stomach" — physicochemically the opposite habitat.
5. **Rumen fluid vs the rumen.** The corpus already treats these as distinct and does so correctly: `GOLD.409867a634` and `BACDIVE.25af5eede6` are both `GROUND_AS_PARENT` / NARROW under `UBERON:0007365`. Madin's bin, by contrast, merges them.
6. **Ruminal acidosis / SARA.** A disease state of the host, not a habitat. If a source concept names it, that is `NOT_APPLICABLE` territory.
7. **Rumen-simulating bioreactors (RUSITEC, continuous culture).** Engineered systems; they diverge measurably from the animal — one study reported mean Eh of −251 and −243 mV, far more negative than in vivo, with Bacteroidetes:Firmicutes falling 3.2 → 1.2 over ten days (reported in the Eh literature surveyed by [Huang et al. 2018](https://doi.org/10.1111/jpn.12855)). These belong under an ENGINEERED framing.

## 6. Should this be a term at all? — **No. Ground it.**

This is a habitat, unambiguously: a physical anatomical compartment sampled directly for microbial isolation, with 132 taxon assertions behind it. Nothing about it suggests a process, quality, disease or taxon. The curator's HOST_ASSOCIATED category override (#57) is right.

But it does not need a *minted* term, and the premise that it has none does not hold up:

- **`UBERON:0007365` *rumen* is in the vendored slice** (`data/raw/ontology_terms.tsv`, `directly_referenced: TRUE`), with the full definition quoted above and synonym `paunch`.
- **It is already a record in this corpus** — `data/habitats/host_associated/rumen__a47ac48b.yaml`, `grounding_status: EXACT`, `mapping_status: REVIEWED`.
- **Eight existing decisions already point at it**, including five GOLD rumen-sac leaves and two rumen-fluid concepts.
- **The two GOLD paths Madin folds into this very bin are already parented to it.**

The label matches the slice label `rumen` exactly once the `host_animal_endotherm_` prefix — which is Madin's tree structure, not part of the concept name — is stripped. That prefix is why the seeder's exact-label matcher missed it, the same failure mode as the `Cerumen/Earwax` and `Ceruminous glands` variant-match cases recovered under #12.

**Recommended decision row** (key from `just worklist`; label check will pass — `UBERON:0007365` → `rumen` in the slice):

```
habitatmech:BACDIVE.ed51f3e74a	GROUND	UBERON:0007365	rumen	CLOSE	<curator>	<date>	…	ITEM	HOST_ASSOCIATED
```

**`CLOSE` rather than `EXACT`,** because Madin's bin is a sampling category that merges the compartment with its contents — `renaming_isolation_source.csv` folds `rumen fluid` and `bovine rumen fluid` into it alongside `bovine rumen` — whereas UBERON names the anatomical compartment. That is the same bin-versus-thing framing gap `BACDIVE.6add57f329` recorded as CLOSE. An `EXACT` is defensible if the curator prefers consistency with the GOLD `Rumen` leaves, which took EXACT; either way the target CURIE is the same and the two records merge. Note that the existing `HOST_ASSOCIATED` category override must be preserved on the row.

**Two follow-ups this research surfaced, neither of which belongs in the same decision:**

1. File an issue on `habitatmech:GOLD.86aef52360` — the termite hindgut paunch/P3 segment is grounded EXACT to `UBERON:0007365`, publishing "the termite hindgut is the ruminant rumen" and injecting `Paunch/P3 segment` as a synonym of *rumen*. UBERON has termite gut anatomy alternatives, or it is a `CONFIRM_UNGROUNDED` / term-request case like beehive cerumen.
2. The corpus carries two independent rumen identity records — `BTO:0001194` (PREGO, 231 taxa) and `UBERON:0007365` (GOLD/BacDive) — for one concept. Whether that is intended (source-vocabulary-keyed records) or a merge candidate is a separate question, but a curator grounding this concept will hit it and should be told the answer rather than picking.

## Citations

1. https://doi.org/10.1038/s41597-020-0497-4
2. https://github.com/bacteria-archaea-traits/bacteria-archaea-traits
3. https://www.ebi.ac.uk/ols4/api/search?q=rumen&ontology=envo
4. http://purl.obolibrary.org/obo/UBERON_0007365
5. https://doi.org/10.3390/microorganisms11030747
6. https://extension.msstate.edu/publications/understanding-the-ruminant-animal-digestive-system
7. https://vivo.colostate.edu/hbooks/pathphys/digestion/herbivores/rumination.html
8. https://doi.org/10.1111/jpn.12855
9. https://doi.org/10.3389/fmicb.2017.01864
10. https://doi.org/10.1016/B978-1-4832-3308-6.X5001-4
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC10838669/
12. https://pubmed.ncbi.nlm.nih.gov/22444607/
13. https://doi.org/10.1186/s42523-022-00174-z
14. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9161295/
15. https://doi.org/10.1038/srep14567
16. https://doi.org/10.1038/nbt.4110
17. https://doi.org/10.1038/ismej.2011.131
18. https://doi.org/10.1126/science.245.4923.1236
19. http://purl.obolibrary.org/obo/BTO_0001194