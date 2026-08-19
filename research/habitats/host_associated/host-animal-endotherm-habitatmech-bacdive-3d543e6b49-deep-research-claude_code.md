---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:09:00.397421'
end_time: '2026-08-17T16:17:22.584599'
duration_seconds: 502.19
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: host_animal_endotherm
  habitat_identifier: habitatmech:BACDIVE.3d543e6b49
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'MADIN: host_animal_endotherm'
  assertions: '5130'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Reviewed and endorsed the seeder's own resolution. Category override\
    \ (#57): a minted identifier gives infer_category nothing to read \u2014 no ontology\
    \ term, no GOLD path \u2014 so every Madin habitat named in the BacDive vocabulary\
    \ fell to OTHER. This is the single largest Madin habitat at 5130 taxa; a warm-blooded\
    \ animal host is HOST_ASSOCIATED by the same reading as every other host source\
    \ here. (source concept habitatmech:BACDIVE.3d543e6b49)"
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
  web_search_requests: 10
  num_turns: 30
  total_cost_usd: 2.8358705
  session_id: fff56b4c-f035-4361-a630-fb6180f480db
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 35
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** host_animal_endotherm
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.3d543e6b49
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** MADIN: host_animal_endotherm
- **Upstream assertion volume:** 5130
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Reviewed and endorsed the seeder's own resolution. Category override (#57): a minted identifier gives infer_category nothing to read — no ontology term, no GOLD path — so every Madin habitat named in the BacDive vocabulary fell to OTHER. This is the single largest Madin habitat at 5130 taxa; a warm-blooded animal host is HOST_ASSOCIATED by the same reading as every other host source here. (source concept habitatmech:BACDIVE.3d543e6b49)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **host_animal_endotherm** as a microbial habitat, with citations.

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

# Definition research: `host_animal_endotherm` (`habitatmech:BACDIVE.3d543e6b49`)

## Proposed definition

> An **animal-associated environment** which is determined by an animal host that maintains an elevated, metabolically generated and regulated core temperature (endothermy), so that the environment is held near 37–41 °C with low temporal thermal variability irrespective of ambient conditions.

Genus: `ENVO:01001002` *animal-associated environment*. Differentia: the host's thermal physiology (endothermy), stated as an observable property of the environment (near-constant elevated temperature), not as a taxonomic claim about the host.

**Recommended disposition in this repo:** `GROUND_AS_PARENT` → `ENVO:01001002` *animal-associated environment*, keeping the minted identifier and flagging the concept as a term-request candidate (`endothermic animal-associated environment` / `warm-blooded animal-associated environment`). Reasons in §2 and §6. Do **not** `GROUND` to `ENVO:01001002` — that term is already the grounding for a *different* source concept in this corpus (see §2.3), and grounding here would merge the endotherm and non-specific-animal buckets.

---

## 1. What the concept denotes

### 1.1 Provenance of the label

`host_animal_endotherm` is not a BacDive string. It is a **level-3 label in the Madin et al. (2020) environment scheme**, a ~100-label controlled vocabulary built to normalise free-text isolation sources across 26 trait databases. The paper states the structure explicitly:

> "The scheme is hierarchical using up to four levels of specificity, for example a one-term label is 'host', a two-term is 'host_animal', a three-term is 'host_animal_endotherm', and a four-term is 'host_animal_endotherm_intestinal'."
> — Madin JS et al. (2020) *A synthesis of bacterial and archaeal phenotypic trait data*, **Scientific Data** 7:170. [doi:10.1038/s41597-020-0497-4](https://doi.org/10.1038/s41597-020-0497-4) · PMID 32503990 · [PMC7275036](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275036/)

The vocabulary and its mappings are in the project's conversion tables: [`data/conversion_tables/environments.csv`](https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/blob/master/data/conversion_tables/environments.csv) (92 labels, each with physicochemical annotations and an ENVO annotation column) and [`renaming_isolation_source.csv`](https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/blob/master/data/conversion_tables/renaming_isolation_source.csv) (3,153 manually translated source strings). Data release: [doi:10.6084/m9.figshare.c.4843290](https://doi.org/10.6084/m9.figshare.c.4843290).

The complete `Host_associated` block of that vocabulary — the concept's actual sibling and child set — is:

```
host, host_fungus, host_algae, host_animal,
host_animal_ectotherm,
host_animal_endotherm,
  …_oral   …_nasopharyngeal   …_vagina   …_blood   …_rumen
  …_intestinal   …_intracellullar [sic]   …_surface   …_intratissue   …_feces
host_plant, host_plant_root-associated, host_plant_leaf-associated,
host_plant_vasculature, host_plant_rootnodule
```

So the concept sits at a fixed position: **narrower than `host_animal`, contrasted with `host_animal_ectotherm`, and broader than ten body-site labels** — of which this corpus already carries `host_animal_endotherm_rumen`, `host_animal_endotherm_intratissue`, and (via their ENVO groundings) `mouth environment`, `intestine environment`, `skin environment`, `fecal environment`, `blood`, `vagina`, `nasopharynx`.

### 1.2 The label is ambiguous — two readings

**(a) Class reading (recommended).** The environment determined by any endothermic animal host, at any body site — the genuine superclass of the ten level-4 labels.

**(b) Residual reading (what the data actually contains).** "Isolated from a warm-blooded animal, body site not stated or not one of the ten enumerated sites." Madin's scheme is explicitly *applied* this way: the authors say the hierarchy "allowed us to be relatively specific or relatively vague depending on the information available."

The 168 source strings mapped to this exact label settle which reading the assertions represent. They are almost entirely (i) host taxon without a body site, or (ii) clinical specimen descriptions:

- Host-only: `host-associated, human`; `host-associated, mammals`; `host-associated, birds`; `bovine`; `hostassociated, pig`; `hostassociated, chicken`; `other, poultry`; `other, sheep and goats`; `other, marine mammals`; `other, whales`; `other, grey seals`; `other, flamingos`; `other, vultures`; `other, common vole`; `other, chinchilla`; `other, beaver`; `other, rabbit`; `homo sapiens`
- Clinical/specimen: `pus`; `abdominal abscess`; `human wound specimens`; `clinical isolates`; `human case of meningitis`; `tuberculosis patient`; `cystic fibrosis patient`; `unknown human clinical source`; `semen`; `human urine`; `skin lesion`; `hostassociated, human cerebrospinal fluid`

The 5,130-taxon count is therefore best read as **"warm-blooded host, site unresolved,"** and it is the single largest bucket in the whole Madin scheme precisely because it is the catch-all for a human- and livestock-dominated literature.

**Boundary — inside the concept:** any site on or in a mammal or bird treated as a microbial habitat, where the host's thermal regime is the salient environmental property.

**Boundary — outside the concept (neighbouring concepts):**

| Neighbour | Why it is not this |
|---|---|
| `host_animal_ectotherm` (`habitatmech:BACDIVE.e68bf42dcb`, 999 taxa) | Sibling; host temperature tracks ambient |
| `host_animal` (grounded upstream to `ENVO:01001002`, 144 taxa) | Parent; thermal type unstated |
| The ten `host_animal_endotherm_*` site labels | Children; each names a body site this one does not |
| `UBERON:0000468` *multicellular organism* (`host`, 1,249 taxa) | Grandparent in the source scheme, and an organism term, not a place |
| Clinical-specimen provenance | A *sampling* description, not a habitat — see §6.2 |

### 1.3 A recorded observation, not an inference

Madin's own curators **left the ENVO annotation column empty** for `host_animal_endotherm` (and for `host_animal_ectotherm`, `..._rumen`, `..._intracellullar`, `..._intratissue`). Every other level-3 host label carries one: `host_animal` → `ENVO:01001002`, `host_fungus` → `ENVO:01001041`, `host_algae` → `ENVO:02500019`. The paper explains the gaps: ENVO annotations were attempted but "most environmental terms required the union of multiple ENVO terms" and so were dropped from the released products. That empty cell is independent, upstream corroboration that **no single ENVO term names this concept** — the premise on which HabitatMech mints an identifier.

---

## 2. Genus — the broader kind

### 2.1 The match

**`ENVO:01001002` — *animal-associated environment*** · "An environmental system determined by an animal." Synonyms: *Metazoan-associated environment*, *animal environment*. [OLS](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002) — present and `directly_referenced` in this repo's vendored slice (`data/raw/ontology_terms.tsv`).

This is the smallest well-established kind the concept falls under. It is *strictly broader*: it subsumes the ectotherm sibling too. This is exactly the ENVO modelling pattern CLAUDE.md points at for host-as-habitat (`plant-associated environment` / `animal-associated environment` / `fungi-associated environment`).

### 2.2 Near-misses, and why each fails

| Term | Verdict |
|---|---|
| `ENVO:01001000` *environmental system determined by an organism* — "An environmental system which is determined by a living organism"; carries the exact synonym **"host-associated environment"** | **Too broad by two levels.** Subsumes plant-, fungus- and alga-associated. Useful as the grandparent, not the genus. |
| `ENVO:01001055` *environment associated with an animal part or small animal* — "…determined by part of a living or dead animal, or a whole small animal" | **Asserts what the sources do not.** "Part of" and "small" are claims absent from `host-associated, whales` and `host-associated, human`. |
| `ENVO:01001179` *cnidarian-associated environment* | Sibling at the wrong clade; cnidarians are ectotherms. Shows ENVO *does* subdivide `ENVO:01001002` by host kind — but by taxon, never by thermal physiology. |
| `UBERON:0000468` *multicellular organism* | An organism class, not a place. Per CLAUDE.md the taxon/organism term belongs in `relation: xref`, never as identity. |
| `ENVO:2100002`, `ENVO:08000002`, `ENVO:2100003`, `ENVO:01001029`, `UBERON:0000178`, `UBERON:0000996` (intestine / mouth / skin / fecal environment, blood, vagina) | **Narrower.** Each grounds one of this concept's *children* in this very corpus. Grounding here would collapse a superclass onto a subclass. |
| A taxon term for "endotherms" (NCBITaxon) | **Does not exist and cannot.** Endothermy is convergent — Mammalia and Aves independently, plus regional endothermy in lamnid sharks, tunas and opah, and thermogenesis in some insects and plants. No clade corresponds. |
| A quality term for endothermy (PATO) | **None found.** OLS4 searches for *endotherm*, *homeotherm*, *warm-blooded*, *poikilothermic* return no PATO class. The nearest anything is `NCIT:C14320` *Poikilotherms* ("Animals which have a body temperature which is largely controlled by external factors of the environment") — an organism grouping, wrong polarity, wrong ontology for this corpus. |

Exhaustive check of ENVO's `*-associated environment` family (OLS4, August 2026): only four exist — plant, animal, fungi, cnidarian. **There is no endotherm-, mammal-, bird- or vertebrate-associated environment term in ENVO.**

### 2.3 Why `GROUND` to the genus would be wrong here

`ENVO:01001002` is already the upstream grounding for the *sibling* source concept `host_animal` (144 taxa, present in `data/raw/madin_habitats.tsv` as its own habitat). Grounding `host_animal_endotherm` to the same term would merge 5,130 endotherm assertions into the 144-taxon unspecified-animal record and silently swallow the thermal distinction that `host_animal_ectotherm` (999 taxa, separately minted) depends on. This is the same failure mode as the ambiguous-GOLD-leaf rule in `scripts/seed_from_sources.py`: *"Grounding them all to the same term would merge marine, freshwater, and hot-spring sediment into one record."* `GROUND_AS_PARENT` records the true is-a without asserting identity.

---

## 3. Differentia — what distinguishes it

### 3.1 The primary differentia: a regulated, elevated, low-variance temperature

**Definition of endothermy (authoritative).** IUPS Thermal Commission, *Glossary of Terms for Thermal Physiology*, 3rd edn (2001, *Jpn J Physiol* 51:245–280; reprinted *J Therm Biol* 2003): endothermy is "the pattern of thermoregulation in which the body temperature depends on a high (tachymetabolic) and controlled rate of heat production," with ectothermy as its antonym — "the pattern of temperature regulation of animals in which body temperature depends mainly on the behaviourally controlled exchange of heat with the environment." [PDF](https://heathealth.info/assets/Glossary-of-terms-for-thermal-phys.pdf); 2nd edn: [PMID 3324054](https://pubmed.ncbi.nlm.nih.gov/3324054/).

**Quantitative range.** Prinzinger R, Preßmar A, Schleucher E (1991) *Body temperature in birds*, **Comp Biochem Physiol A** 99:499–506 ([doi:10.1016/0300-9629(91)90122-S](https://doi.org/10.1016/0300-9629(91)90122-S)) reports avian T_b as 38.54 ± 0.96 °C (rest, n=203), 41.02 ± 1.29 °C (active phase, n=724), 43.85 ± 0.94 °C (high activity, n=74), and states birds exceed mammals by 1.87 °C at rest and 2.43 °C in the active phase — placing mammals at ≈36.7 °C resting and ≈38.6 °C active. *(The mammalian figures are my arithmetic from Prinzinger's stated offsets, not values printed in that paper.)* Independently, Bergman A & Casadevall A (2010) model the fitness/metabolic-cost optimum of endothermy at **36.7 °C**, "closely matching actual mammalian body temperatures" — *Mammalian endothermy optimally restricts fungi and metabolic costs*, **mBio** 1:e00212-10 ([doi:10.1128/mBio.00212-10](https://doi.org/10.1128/mBio.00212-10), [PMID 21060737](https://pubmed.ncbi.nlm.nih.gov/21060737/)). Broader comparative dataset (596 mammals, 490 birds): Clarke A & Rothery P (2008) *Scaling of body temperature in mammals and birds*, **Funct Ecol** 22:58–67 ([doi:10.1111/j.1365-2435.2007.01341.x](https://doi.org/10.1111/j.1365-2435.2007.01341.x)). *I could not read Clarke & Rothery's full text; cite it for the comparative dataset, not for a specific mean.*

**Upstream's own parameterisation.** The `environments.csv` row for `host_animal_endotherm` records: Pressure `low`, Temperature `medium`, **temperature variability `low`**, salinity variability `small`, pH `medium`, and the Cobo-Simón adjusted habitat `host_internal`. Note the contrast in the same file: the sibling `host_animal_ectotherm` and the parent `host_animal` are *not* given `temp variability: low`. Thermal constancy is precisely what upstream used to separate this label from its sibling. (Per the repo's environment-parameter rules, these are qualitative band annotations on a single-term row — usable, unlike the skipped multi-term rows.)

### 3.2 Consequence 1: the habitat excludes most environmental fungi

Robert VA & Casadevall A (2009) *Vertebrate endothermy restricts most fungi as potential pathogens*, **J Infect Dis** 200:1623–1626 ([doi:10.1086/644642](https://doi.org/10.1086/644642), [PMID 19827944](https://pubmed.ncbi.nlm.nih.gov/19827944/)): thermal tolerance of **4,802 fungal strains from 144 genera** showed most cannot grow at mammalian body temperature; each 1 °C increase across the 30–40 °C range excluded roughly a further **6%** of isolates; fungi isolated from mammals and insects were more thermotolerant than soil and plant isolates. See also Casadevall A (2005) *Fungal virulence, vertebrate endothermy, and dinosaur extinction*, **Fungal Genet Biol** ([PMID 15670708](https://pubmed.ncbi.nlm.nih.gov/15670708/)) and *Fungi and the Rise of Mammals*, **PLoS Pathog** 8:e1002808 ([doi:10.1371/journal.ppat.1002808](https://doi.org/10.1371/journal.ppat.1002808)).

This is the strongest published statement that endothermy constitutes a *distinct habitat filter* rather than a host trait of incidental relevance — the crux of the differentia.

### 3.3 Consequence 2: genomic signatures of thermal stability in the residents

Fontaine SS & Kohl KD (2021) *Blowing Hot and Cold: Body Temperature and the Microbiome*, **mSystems** 6:e00707-21 ([doi:10.1128/mSystems.00707-21](https://doi.org/10.1128/msystems.00707-21)): classic endotherm intestinal commensals such as *Bifidobacterium* spp. show significant **loss of heat-shock-response genes** relative to their environmental relatives, consistent with adaptation to a thermostable niche; ectotherm-associated communities, exposed directly to ambient fluctuation, are not under the same relaxed selection. Relevant to this record's own `characteristic_taxa`, which lead with *Bifidobacterium longum* and *Megasphaera* spp.

### 3.4 Consequence 3: community-level distinctiveness among endotherm hosts

Song SJ et al. (2020) *Comparative analyses of vertebrate gut microbiomes reveal convergence between birds and bats*, **mBio** 11:e02901-19 ([doi:10.1128/mBio.02901-19](https://doi.org/10.1128/mbio.02901-19), [PMC6946802](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6946802/)) — 315 mammal, 491 bird and 86 other vertebrate species; phylosymbiosis holds in non-flying mammals but breaks down in birds and bats, whose microbiomes converge. Commentary: Hird SM (2020) **mBio** 11:e00153-20 ([doi:10.1128/mBio.00153-20](https://journals.asm.org/doi/10.1128/mbio.00153-20)).

### 3.5 Honest counter-evidence

A meta-analysis of experimental warming/cooling across host microbiomes found that **"microbiome changes under thermal treatments were determined by host habitat rather than host biological traits, and endotherms experienced a similar level of microbiome diversity decrease as ectotherms"** — *Experimental temperatures shape host microbiome diversity and composition*, **Glob Change Biol** (2022) ([doi:10.1111/gcb.16429](https://onlinelibrary.wiley.com/doi/full/10.1111/gcb.16429)), with the authors cautioning about low power for some host types. **The definition should therefore rest on the physical property of the habitat (a regulated, low-variance elevated temperature — directly measurable, and the property MIxS records) rather than on a claim that endotherm microbiomes respond differently to thermal perturbation.** That stronger claim is contested.

### 3.6 Measurability

The differentia is recordable in standard metadata: MIxS defines `host_body_temp` in the host-associated extension (`MIXS:0016002`, [spec](https://genomicsstandardsconsortium.github.io/mixs/0016002/)) alongside `host_taxid`, and `temp` (`MIXS:0000113`) as a general environment field. ENVO/MIxS guidance for `env_medium` (`MIXS:0000014`, [spec](https://genomicsstandardsconsortium.github.io/mixs/0000014/)) directs host-associated samples to UBERON/PO terms for the tissue — which is why the *site-unspecified* level of this concept has no natural MIxS home and needs an ENVO-style habitat term.

---

## 4. Sources

Consolidated, with dates:

1. Madin JS et al. (5 Jun 2020) *A synthesis of bacterial and archaeal phenotypic trait data*. **Sci Data** 7:170. [doi:10.1038/s41597-020-0497-4](https://doi.org/10.1038/s41597-020-0497-4) · PMID 32503990 · [PMC7275036](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275036/) — the scheme, the four-level hierarchy, the manual translation of >3,000 strings covering ~65% of species.
2. bacteria-archaea-traits [conversion tables](https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/tree/master/data/conversion_tables) (v1.0.0, 2020) — `environments.csv` (label set, physicochemical bands, empty ENVO cell for this label); `renaming_isolation_source.csv` (the 168 strings). Data: [doi:10.6084/m9.figshare.c.4843290](https://doi.org/10.6084/m9.figshare.c.4843290).
3. IUPS Thermal Commission (2001/2003) *Glossary of Terms for Thermal Physiology*, 3rd edn. *Jpn J Physiol* 51:245–280 / *J Therm Biol*. [PDF](https://heathealth.info/assets/Glossary-of-terms-for-thermal-phys.pdf) — definitions of endothermy/ectothermy/homeothermy.
4. Robert VA & Casadevall A (15 Nov 2009) **J Infect Dis** 200:1623–1626. [doi:10.1086/644642](https://doi.org/10.1086/644642) — thermal exclusion, 4,802 strains, ~6% per °C.
5. Bergman A & Casadevall A (2010) **mBio** 1:e00212-10. [doi:10.1128/mBio.00212-10](https://doi.org/10.1128/mbio.00212-10) — 36.7 °C optimum.
6. Casadevall A (2012) *Fungi and the Rise of Mammals*. **PLoS Pathog** 8:e1002808. [doi:10.1371/journal.ppat.1002808](https://doi.org/10.1371/journal.ppat.1002808)
7. Prinzinger R, Preßmar A, Schleucher E (1991) **Comp Biochem Physiol A** 99:499–506. [doi:10.1016/0300-9629(91)90122-S](https://doi.org/10.1016/0300-9629(91)90122-S) — avian T_b means and the bird–mammal offset.
8. Clarke A & Rothery P (2008) **Funct Ecol** 22:58–67. [doi:10.1111/j.1365-2435.2007.01341.x](https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2435.2007.01341.x) · [open record](https://nora.nerc.ac.uk/id/eprint/11428/) — 596 mammals + 490 birds.
9. Fontaine SS & Kohl KD (2021) **mSystems** 6:e00707-21. [doi:10.1128/mSystems.00707-21](https://journals.asm.org/doi/10.1128/msystems.00707-21)
10. Song SJ et al. (7 Jan 2020) **mBio** 11:e02901-19. [doi:10.1128/mBio.02901-19](https://journals.asm.org/doi/10.1128/mbio.02901-19) · Hird SM (2020) **mBio** 11:e00153-20. [doi:10.1128/mBio.00153-20](https://journals.asm.org/doi/10.1128/mbio.00153-20)
11. *Experimental temperatures shape host microbiome diversity and composition* (2022) **Glob Change Biol**. [doi:10.1111/gcb.16429](https://onlinelibrary.wiley.com/doi/full/10.1111/gcb.16429) — the counter-evidence.
12. ENVO classes via OLS4 (retrieved 17 Aug 2026): [ENVO:01001002](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002), [ENVO:01001000](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000), [ENVO:01001055](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001055), [ENVO:01001179](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179).
13. GSC MIxS: [host-associated extension `MIXS:0016002`](https://genomicsstandardsconsortium.github.io/mixs/0016002/), [`env_medium` `MIXS:0000014`](https://genomicsstandardsconsortium.github.io/mixs/0000014/), [Using ENVO with MIxS](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS).

**Explicitly flagged as my inference, not sourced:** (i) that the concept's *class* reading should be preferred over its residual reading; (ii) the ≈36.7 / ≈38.6 °C mammalian figures derived from Prinzinger's offsets; (iii) that `ENVO:01001002` is the correct genus (a modelling judgement, though it is the term upstream itself chose for the parent label); (iv) the recommended `GROUND_AS_PARENT` disposition. **No source states a definition of `host_animal_endotherm` — Madin et al. define the scheme's structure but never gloss the individual labels.** The definition has to be constructed, which is why the term exists.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- endotherm-associated environment; endothermic host environment
- warm-blooded animal host (colloquial; imprecise — see below)
- homeothermic vertebrate host (near-equivalent in practice, not in definition)
- mammal- and bird-associated environment (extensional gloss, correct for essentially all of the attested data)
- "host_internal" / "host" in the Cobo-Simón habitat coarsening carried in the same upstream row (a *coarser* grouping, not a synonym)

**Do NOT conflate**

| Confusable | Why it differs |
|---|---|
| **homeotherm** | Endothermy = *source* of heat (metabolic); homeothermy = *constancy* of temperature. Not coextensive: a tropical ectotherm can be near-homeothermic; a hibernating bat or torporing hummingbird is an endotherm that is not homeothermic. IUPS glossary treats them as distinct axes. |
| **"warm-blooded"** | Pre-theoretical and deprecated in thermal physiology; the endotherm/homeotherm pair was introduced (Bligh & Johnson 1973, formalised in the IUPS glossary) specifically to replace it. Fine as an exact synonym on the record; not fine in the definition text. |
| **Mammalia + Aves** | Practically the extension of the attested data, but not the definition. Regional endothermy occurs in tunas, lamnid sharks and opah; facultative endothermy in some insects (bumblebees) and thermogenic plants. Defining by clade would be wrong *and* would violate the repo's rule that a taxon term is not a habitat. |
| **`ENVO:01001002` animal-associated environment** | The genus, one level up; includes ectotherm hosts. |
| **human-associated / human gut / clinical** | Humans dominate the mapped strings but are a proper part; `host-associated, birds`, `bovine`, `whales`, `flamingos` are all in the same bucket. |
| **The ten `host_animal_endotherm_*` site labels** | Children, each already grounded or minted separately in this corpus. |
| **`host_animal_endotherm_intracellullar`** | A distinct upstream label (note the upstream typo) — an intracellular niche, not a synonym for the site-unspecified parent. |
| **"clinical specimen" / "isolation source"** | A provenance category, not a place. See §6.2. |
| **`ENVO:01001000`'s synonym "host-associated environment"** | Attaches to the *organism-determined* superclass and covers plants and fungi. |

---

## 6. Should it be a term at all?

### 6.1 Yes — it is a habitat, and it is the right kind of thing

It denotes a place where microbes live (the body of a warm-blooded animal), not a process, disease, quality, procedure, or taxon. It fits the repo's settled line exactly: *"An organism acting as a host IS a habitat; the taxon term is not."* Nothing here names a taxon — `endotherm` is a physiological predicate, not a clade — so the usual `NOT_APPLICABLE`-for-organism-terms trap does not apply, and `tests/test_decisions.py` would (correctly) reject `NOT_APPLICABLE` reasoning anyway. It is also the *largest* single habitat in the Madin scheme (5,130 taxa), and the point at which ENVO's `animal-associated environment` branch stops resolving. A term is warranted.

### 6.2 One real caveat the curator should record in `notes`

**About 30% of the attested strings are clinical-specimen descriptions** (`pus`, `abdominal abscess`, `human wound specimens`, `clinical isolates`, `human case of meningitis`, `unknown human clinical source`, `tuberculosis patient`). These describe *how a strain was obtained*, not a distinct habitat, and this repo has a separate `CLINICAL` category. The concept as attested is therefore partly a habitat class and partly an isolation-provenance bucket. This does not defeat the term — a wound and an abscess *are* sites in an endothermic host, so they fall under the class reading — but the note should say so plainly, because it is the honest account of why the 5,130 figure is so large and why the record can never be more precise than "site unresolved."

Two smaller upstream artefacts worth noting and not propagating: `host-associated, microbial, free living` and `Toxin-free strain for bacteriolytic tumor therapy` are both mapped to this label upstream and are plainly mismappings; `Originally discovered as a contaminant of a human cell culture` is a laboratory-contamination provenance.

### 6.3 Concrete recommendation for `curation/decisions.tsv`

| Field | Value |
|---|---|
| key | `habitatmech:BACDIVE.3d543e6b49` |
| decision | `GROUND_AS_PARENT` |
| target | `ENVO:01001002` |
| expected label | `animal-associated environment` |
| relation | `parent` (genuinely broader — an endotherm-associated environment *is* an animal-associated environment) |

Do **not** attach any of `UBERON:0000468`, `ENVO:2100002`, `ENVO:01001029` or a mammal/bird taxon as `parent`. If a link to the host kind is wanted at all, it belongs in `relation: xref`.

The concept remains a **term-request candidate** — proposed label *endothermic animal-associated environment*, exact synonym *warm-blooded animal-associated environment*, genus `ENVO:01001002`, with `host_animal_ectotherm` as the natural companion request. Per the standing rule in this project's memory, **nothing should be submitted to ENVO without your explicit per-request approval**; this report only records that the gap exists and what the request would say.

**Sources:** [Madin et al. 2020 Sci Data](https://doi.org/10.1038/s41597-020-0497-4) · [PMC7275036](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275036/) · [bacteria-archaea-traits conversion tables](https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/tree/master/data/conversion_tables) · [IUPS Thermal Glossary](https://heathealth.info/assets/Glossary-of-terms-for-thermal-phys.pdf) · [Robert & Casadevall 2009 JID](https://doi.org/10.1086/644642) · [Bergman & Casadevall 2010 mBio](https://journals.asm.org/doi/10.1128/mbio.00212-10) · [Casadevall 2012 PLoS Pathog](https://journals.plos.org/plospathogens/article?id=10.1371%2Fjournal.ppat.1002808) · [Prinzinger et al. 1991](https://doi.org/10.1016/0300-9629(91)90122-S) · [Clarke & Rothery 2008 Funct Ecol](https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2435.2007.01341.x) · [Fontaine & Kohl 2021 mSystems](https://journals.asm.org/doi/10.1128/msystems.00707-21) · [Song et al. 2020 mBio](https://journals.asm.org/doi/10.1128/mbio.02901-19) · [Hird 2020 mBio](https://journals.asm.org/doi/10.1128/mbio.00153-20) · [Glob Change Biol 2022](https://onlinelibrary.wiley.com/doi/full/10.1111/gcb.16429) · [ENVO:01001002 (OLS4)](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002) · [MIxS host-associated](https://genomicsstandardsconsortium.github.io/mixs/0016002/) · [MIxS env_medium](https://genomicsstandardsconsortium.github.io/mixs/0000014/) · [Using ENVO with MIxS](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS)

## Citations

1. https://doi.org/10.1038/s41597-020-0497-4
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC7275036/
3. https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/blob/master/data/conversion_tables/environments.csv
4. https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/blob/master/data/conversion_tables/renaming_isolation_source.csv
5. https://doi.org/10.6084/m9.figshare.c.4843290
6. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
7. https://heathealth.info/assets/Glossary-of-terms-for-thermal-phys.pdf
8. https://pubmed.ncbi.nlm.nih.gov/3324054/
9. https://doi.org/10.1016/0300-9629(91
10. https://doi.org/10.1128/mBio.00212-10
11. https://pubmed.ncbi.nlm.nih.gov/21060737/
12. https://doi.org/10.1111/j.1365-2435.2007.01341.x
13. https://doi.org/10.1086/644642
14. https://pubmed.ncbi.nlm.nih.gov/19827944/
15. https://pubmed.ncbi.nlm.nih.gov/15670708/
16. https://doi.org/10.1371/journal.ppat.1002808
17. https://doi.org/10.1128/msystems.00707-21
18. https://doi.org/10.1128/mbio.02901-19
19. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6946802/
20. https://journals.asm.org/doi/10.1128/mbio.00153-20
21. https://onlinelibrary.wiley.com/doi/full/10.1111/gcb.16429
22. https://genomicsstandardsconsortium.github.io/mixs/0016002/
23. https://genomicsstandardsconsortium.github.io/mixs/0000014/
24. https://github.com/bacteria-archaea-traits/bacteria-archaea-traits/tree/master/data/conversion_tables
25. https://doi.org/10.1128/mbio.00212-10
26. https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2435.2007.01341.x
27. https://nora.nerc.ac.uk/id/eprint/11428/
28. https://journals.asm.org/doi/10.1128/msystems.00707-21
29. https://journals.asm.org/doi/10.1128/mbio.02901-19
30. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001000
31. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001055
32. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001179
33. https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
34. https://journals.asm.org/doi/10.1128/mbio.00212-10
35. https://journals.plos.org/plospathogens/article?id=10.1371%2Fjournal.ppat.1002808