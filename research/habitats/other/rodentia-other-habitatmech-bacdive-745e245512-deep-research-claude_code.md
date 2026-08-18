---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T20:36:05.151093'
end_time: '2026-08-17T20:43:56.347683'
duration_seconds: 471.2
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Rodentia-Other
  habitat_identifier: habitatmech:BACDIVE.745e245512
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Rodentia-Other'
  assertions: '97'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Cohort\
    \ review: the other half of the NCIT:C17649 'Other' merge. Same reasoning as the\
    \ invertebrate source it was collapsing with \u2014 a bucket term is not an identity.\
    \ (source concept habitatmech:BACDIVE.745e245512)"
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
  num_turns: 37
  total_cost_usd: 3.251317
  session_id: c40f4bd3-7b46-434e-afa1-1ed9be86361c
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 31
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Rodentia-Other
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.745e245512
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Rodentia-Other
- **Upstream assertion volume:** 97
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Cohort review: the other half of the NCIT:C17649 'Other' merge. Same reasoning as the invertebrate source it was collapsing with — a bucket term is not an identity. (source concept habitatmech:BACDIVE.745e245512)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Rodentia-Other** as a microbial habitat, with citations.

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

# Definition research: `Rodentia-Other` (habitatmech:BACDIVE.745e245512)

> **Proposed definition:** An animal-associated environment which is determined by a rodent (order Rodentia, NCBITaxon:9989) belonging to a family other than Muridae.

**Read the next paragraph before using that sentence.** The differentia is partly negative ("other than Muridae"), which is an OBO anti-pattern, and it is negative because an intermediate class is genuinely missing. The positive class the corpus needs is **`rodent-associated environment`** — *An animal-associated environment which is determined by a rodent.* `Rodentia-Other` is the residual half of that class after BacDive splits off its mouse/rat bin (`Muridae-Mouse/Rat`, `habitatmech:BACDIVE.ab17ecb10f`, currently `REVIEW`). Requesting the positive parent and recording the murid exclusion as a **scope note** rather than as differentia is the more defensible disposition; see §6.

---

## 1. What the concept denotes

### 1.1 The label is a BacDive isolation-source tag, not free text

BacDive does not store isolation sources only as prose. Every source string is manually tagged against a controlled hierarchy:

> "The central parts of this tool are *Isolation source tags*, which are keywords that were manually assigned to each isolation source." … "The keywords are organized in a hierarchical ontology that comprises 387 terms on three levels." (Reimer et al., *BacDive in 2022*, Nucleic Acids Res 50:D741–D746, [doi:10.1093/nar/gkab961](https://doi.org/10.1093/nar/gkab961), [PMC8728306](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728306/))

> "This ontology is hierarchically ordered into three levels of tags (category 1–3). At the top level the eight major classes #Environmental, #Engineered, #Host, #Host body-site, #Host body-product, #Medical, #Condition and #Climate are listed." (Reimer et al., *BacDive in 2019*, Nucleic Acids Res 47:D631–D636, [doi:10.1093/nar/gky879](https://doi.org/10.1093/nar/gky879), [PMC6323973](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/))

The live BacDive isolation-source browser ([bacdive.dsmz.de/isolation-sources](https://bacdive.dsmz.de/isolation-sources)) shows, under `#Host`, the level-2 siblings **`#Rodentia (Other)`** and **`#Muridae (Mouse/Rat)`**. HabitatMech's label `Rodentia-Other` is that tag with its parenthesis flattened.

### 1.2 What it therefore denotes

**A non-murid rodent, considered as the living (or freshly dead) environment from which a strain was recovered.** The sample is taken *from an animal* — its tissue, its gut contents, its oral surfaces, a lesion — and the tag records *which kind of animal*, nothing else.

Two boundary facts follow directly from the MISO structure quoted above:

- **`#Host` is a separate top-level axis from `#Host body-site` and `#Host body-product`.** So `Rodentia-Other` does **not** denote a body site. "Guinea pig caecum" is `#Host` = Rodentia-Other **plus** `#Host body-site` = intestine. The concept is the whole host-as-environment, not an anatomical compartment. This is exactly the case CLAUDE.md's "an organism acting as a host IS a habitat; the taxon term is not" rule covers.
- **The boundary with its only sibling is `Muridae`, not "mouse/rat" in the vernacular sense.** Voles, lemmings and hamsters are Cricetidae (NCBITaxon:337677), not Muridae (NCBITaxon:10066), so they fall on the `Rodentia-Other` side even though a non-specialist would call *Microtus* a "field mouse". *Staphylococcus microti*, from the common vole *Microtus arvalis*, sits in this record and confirms the split is drawn at family rank, not at common name.

### 1.3 Ambiguity — two readings, and which the data supports

| Reading | Statement | Evidence |
|---|---|---|
| **A (supported)** | A *residual taxonomic partition*: rodent hosts of any family except Muridae. | The 25 top taxa on the record are overwhelmingly non-murid-host organisms — hamster (*Cricetus*, *Mesocricetus*), guinea pig (*Cavia*), chinchilla (*Chinchilla*), vole (*Microtus*), beaver (*Castor*), squirrel (*Sciurus*). This is the reading. |
| **B (not supported)** | A *catch-all for rodent isolates whose host species was not recorded* — i.e. "rodent, unspecified". | Nothing in the strain list suggests unspecified hosts; nearly every type strain has a named host species in its protologue. Reject. |

**Do not read the label as NCIT:C17649 "Other"** ("Different than the one(s) previously specified or mentioned"; [OLS4/NCIT](https://www.ebi.ac.uk/ols4/ontologies/ncit/classes?obo_id=NCIT:C17649)). That was the upstream lexical match on the trailing word, and it collapsed this concept with `Invertebrates-Other` into one record. The repo has already retired that merge (`data/habitats/RETIRED.tsv`: `other-ncit-c17649 → BACDIVE.745e245512 | BACDIVE.e864a16f03`, `source_concepts_split`). The semantically loaded word in the label is **Rodentia**, not *Other*.

### 1.4 Purity caveat — the bucket is not clean

Two of the 25 ranked taxa show the tag is assigned per deposited strain record, not per canonical host species, and that it leaks across its own boundaries:

- ***Citrobacter rodentium*** is the textbook *mouse* pathogen (transmissible murine colonic hyperplasia; Schauer et al., J Clin Microbiol 33:2064–2068, 1995, [PMID 7559949](https://pubmed.ncbi.nlm.nih.gov/7559949/)) — yet the DSMZ catalogue records the **host of type strain DSM 16636 as hamster** ([DSMZ catalogue DSM-16636](https://www.dsmz.de/collection/catalogue/details/culture/DSM-16636)). The strain, not the species, decides the bin. That is arguably correct behaviour for an isolation-source tag, but it means the record cannot be read as "microbes of non-murid rodents."
- ***Actinobacillus capsulatus*** was described from **rabbit** joint tissue (Arseculeratne, J Comp Pathol 72:33–39, 1962, [doi:10.1016/S0368-1742(62)80005-8](https://doi.org/10.1016/s0368-1742(62)80005-8)). Rabbits are Lagomorpha, **not** Rodentia. Either BacDive's tag on those specific strains reflects rodent-derived isolates not covered by the protologue, or this is a mis-binning. *I did not resolve which* — a curator writing a scope note should not cite this record as evidence that lagomorphs are in scope.

---

## 2. Genus — the broader kind

### 2.1 The match

**`ENVO:01001002` — *animal-associated environment*** — "An environmental system determined by an animal." (present in the vendored slice, `data/raw/ontology_terms.tsv`; [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002)). Its parent is `ENVO:01001000` *environmental system determined by an organism*.

This is the smallest well-established kind that fits, and it is the same genus ENVO uses for the plant and fungal cases (`ENVO:01001001`, `ENVO:01001041`). It matches the repo's own precedent for organism-as-host concepts.

### 2.2 There is no rodent- or mammal-level ENVO term

Checked directly against OLS4 (August 2026):

- `q=rodent, ontology=envo` → **zero results** (`numFound: 0`).
- `q="associated environment", ontology=envo` → the complete set of organism-associated environment classes is: `ENVO:01001001` plant-associated, `ENVO:01001002` animal-associated, `ENVO:01001041` fungi-associated, `ENVO:01001058` fungal tissue, `ENVO:01001176` aquatic invertebrate, `ENVO:01001055` animal part or small animal, `ENVO:01001057` plant part or small plant, `ENVO:01001179` cnidarian-associated. **No mammal, no vertebrate, no rodent.**

So the gap is real, and it is a two-level gap: ENVO jumps from *animal* straight to *cnidarian* / *aquatic invertebrate*. There is no `vertebrate-associated`, no `mammal-associated`, and no `rodent-associated environment`.

### 2.3 Near-misses and why each fails

| Candidate | Why it is not the genus |
|---|---|
| `ENVO:01001055` *environment associated with an animal part or small animal* | **Narrower and wrong-axis.** It covers a *part* of an animal, or a whole *small* animal. A guinea pig or beaver is neither a part nor a "small animal" in ENVO's sense, and the tag deliberately does not name a part (§1.2). |
| `ENVO:01001176` *environment associated with an aquatic invertebrate* | Sibling under the same parent, taxonomically disjoint. Recorded only because it is the pattern to imitate: ENVO *will* mint taxon-scoped associated-environment classes. |
| `NCBITaxon:9989` *Rodentia* | **Not a habitat.** A taxon term is a class of organisms, not a place. Per CLAUDE.md this belongs on the record as `relation: xref`, and must **not** be used as `parent_habitats` and must **not** trigger `NOT_APPLICABLE`. |
| `NCIT:C17649` *Other* | A generic residual placeholder with no habitat content. Already retired here as a merge target. |
| `UBERON` anatomy terms (gut, oral cavity, skin) | Wrong axis — those are the `#Host body-site` tags that co-occur with this one, not this one. Grounding here would silently pick one body site out of many. |
| `ENVO:00005803` *animal habitation* / `ENVO:03000038` etc. | Denotes a burrow or dwelling — the *place an animal lives*, not *the animal as a place*. Opposite direction. |

---

## 3. Differentia — what distinguishes it from its siblings

Under `animal-associated environment`, the siblings are the other host groups in BacDive's `#Host` level-2 list (Muridae-Mouse/Rat, Aves, Bovinae, Insecta, Pisces, Invertebrates-Other, …). What separates this one:

**Primary (definitional):** the determining animal is a member of **Rodentia** — a placental mammal with a single pair of continuously growing, self-sharpening incisors in each jaw and no canines. Rodentia is the largest mammalian order: **2,552 species, ~39% of all mammal species**, and the two largest mammalian families on Earth are rodent families — Muridae (834 spp.) and Cricetidae (792 spp.) (Burgin, Colella, Kahn & Upham, *How many species of mammals are there?*, J Mammal 99:1–14, 2018, [doi:10.1093/jmammal/gyx147](https://doi.org/10.1093/jmammal/gyx147)).

**Secondary (the residual restriction):** the rodent is **not** a murid mouse or rat — those are partitioned to the sibling concept. What is left is dominated by Cricetidae (hamsters, voles), Caviidae (guinea pigs, NCBITaxon:10139), Chinchillidae (chinchillas, NCBITaxon:10150), Castoridae (beavers, NCBITaxon:29132) and Sciuridae (squirrels).

**Observable / measurable properties that make this a distinct microbial habitat rather than a bookkeeping bin:**

1. **Digestive physiology differs sharply from the murid sibling.** The non-murid rodents dominating this record — guinea pig, chinchilla — are caecum-dominant hindgut fermenters and caecotrophs, clustering microbially with rabbits rather than with rats. In a fecal-microbiota comparison of ten domesticated species, Bray–Curtis dissimilarity put **rabbits and chinchillas in one cluster** of small hindgut fermenters, with Betaproteobacteria dominance the only host-specific signature identified (O'Donnell et al., MicrobiologyOpen 6:e509, 2017, [doi:10.1002/mbo3.509](https://doi.org/10.1002/mbo3.509)). Chinchilla GI microbiota are Firmicutes/Bacteroidota/Actinobacteriota/Proteobacteria-dominated with a notable duodenal Atopobiaceae signal (Vet Sci 11:58, 2024, [doi:10.3390/vetsci11020058](https://doi.org/10.3390/vetsci11020058)). Guinea pigs show the *lowest* hindgut VFA production and a distinct molar ratio among rabbit/guinea-pig/rat/hamster comparisons ([Asian-Australas J Anim Sci](https://www.animbiosci.org/journal/view.php?number=19756)).
2. **Host phylogeny, not diet, is the dominant structuring variable in rodent gut communities** — host phylogeny explained 34% of gut-microbiota variation vs 10% for dietary guild and 3% for geography across 12 rodent species in 3 families (PLOS ONE, 2025, [doi:10.1371/journal.pone.0316101](https://doi.org/10.1371/journal.pone.0316101)); phylosymbiosis in rodents persists through laboratory diet and temperature manipulation (Natl Sci Rev 10:nwad209, 2023, [doi:10.1093/nsr/nwad209](https://doi.org/10.1093/nsr/nwad209)). **This is the strongest available support for treating rodent host group as a habitat-defining variable at all** — it is a citable reason that a family-level rodent split is not arbitrary.
3. **Rodents are disproportionate zoonotic reservoirs**, which is why isolation from them is recorded as a distinct source class at all (Han, Schmidt, Bowden & Drake, *Rodent reservoirs of future zoonotic diseases*, PNAS 112:7039–7044, 2015, [doi:10.1073/pnas.1501598112](https://doi.org/10.1073/pnas.1501598112)). The record's *Yersinia enterocolitica* and *Y. pseudotuberculosis* attestations sit in that tradition.

**What samples from this habitat actually are, per the record's own 97 strain assertions across 80 taxa** — each host verified against LPSN/DSMZ protologues:

| Site type | Attesting taxa (verified isolation source) |
|---|---|
| Hamster oral cavity / dental plaque | *Bifidobacterium tsurumiense* — hamster dental plaque ([doi:10.1099/ijs.0.65296-0](https://doi.org/10.1099/ijs.0.65296-0)); *Alloscardovia criceti* — epithet "of hamster" ([doi:10.1099/ijs.0.051326-0](https://doi.org/10.1099/ijs.0.051326-0)); *Streptococcus criceti*, *Veillonella criceti*, *Actinomyces viscosus* |
| Guinea pig lesion / lymph node | *Caviibacter abscessus* — mandibular lymph node abscess of *Cavia porcellus* ([doi:10.1099/ijsem.0.000922](https://doi.org/10.1099/ijsem.0.000922), [PMID 26813893](https://pubmed.ncbi.nlm.nih.gov/26813893/)); *Nocardia otitidiscaviarum*; *Chlamydia caviae* |
| Rodent gut / faeces | *Bacteroides faecichinchillae* — *Chinchilla lanigera* faeces ([doi:10.1099/ijs.0.032706-0](https://doi.org/10.1099/ijs.0.032706-0)); *B. rodentium*, *B. stercorirosoris*; *Helicobacter aurati* — GI tissue of golden Syrian hamster *Mesocricetus auratus* ([doi:10.1128/jcm.38.10.3722-3728.2000](https://doi.org/10.1128/jcm.38.10.3722-3728.2000)) |
| Wild non-murid rodents | *Staphylococcus microti* — common vole *Microtus arvalis* ([doi:10.1099/ijs.0.011429-0](https://doi.org/10.1099/ijs.0.011429-0)); *Streptococcus castoreus* — beaver *Castor fiber* ([doi:10.1099/ijs.0.63433-0](https://doi.org/10.1099/ijs.0.63433-0)); *Mammaliicoccus sciuri* (squirrel, *Sciurus* — epithet-based, protologue not fetched) |
| Rodent necropsy generally | *Necropsobacter rosorum* — epithet *rosorum* "of rodents", from the "SP group" (*Sektionsprotocol*, necropsy) organisms ([doi:10.1099/ijs.0.024174-0](https://doi.org/10.1099/ijs.0.024174-0)) |

That table is the differentia in observable form: **oral/dental surfaces, caecal and faecal contents, and abscessed lymphoid tissue of captive and wild non-murid rodents**, dominated by laboratory and companion caviomorphs and cricetids.

---

## 4. Sources

Grouped by what they support. **Inferences of mine are marked.**

**BacDive tag structure and the boundary (§1)**
- Reimer LC, Sardà Carbasse J, Koblitz J, Ebeling C, Podstawka A, Overmann J. BacDive in 2022. *Nucleic Acids Res* 50:D741–D746 (2022). [doi:10.1093/nar/gkab961](https://doi.org/10.1093/nar/gkab961) · [PMC8728306](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728306/) — 387 tags, three levels.
- Reimer LC, Vetcininova A, Sardà Carbasse J, et al. BacDive in 2019. *Nucleic Acids Res* 47:D631–D636 (2019). [doi:10.1093/nar/gky879](https://doi.org/10.1093/nar/gky879) · [PMC6323973](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/) — the eight top-level classes verbatim, including the separation of `#Host` from `#Host body-site` and `#Host body-product`.
- [bacdive.dsmz.de/isolation-sources](https://bacdive.dsmz.de/isolation-sources) — live browser showing `#Rodentia (Other)` and `#Muridae (Mouse/Rat)` as level-2 siblings under Host. *(Retrieved 2026-08-17.)*

**ENVO gap (§2)** — OLS4 API queries against `ontology=envo`, retrieved 2026-08-17: `q=rodent` → 0 hits; `q="associated environment"` → the eight classes listed in §2.2. Cross-checked against this repo's vendored slice `data/raw/ontology_terms.tsv`. ENVO term-request tracker: [github.com/EnvironmentOntology/envo/issues](https://github.com/EnvironmentOntology/envo/issues).

**Rodent taxonomy and scale (§3)** — Burgin et al. 2018, [doi:10.1093/jmammal/gyx147](https://doi.org/10.1093/jmammal/gyx147) (correction: J Mammal 100:615, 2019). NCBI Taxonomy IDs verified live via the NCBI Datasets v2 taxonomy API on 2026-08-17: Rodentia **9989** (order), Muridae **10066**, Cricetidae **337677**, Caviidae **10139**, Chinchillidae **10150**, Castoridae **29132**.

**Rodent microbiome structure (§3)** — PLOS ONE 2025 [doi:10.1371/journal.pone.0316101](https://doi.org/10.1371/journal.pone.0316101); Natl Sci Rev 2023 [doi:10.1093/nsr/nwad209](https://doi.org/10.1093/nsr/nwad209) ([PMID 37928774](https://pubmed.ncbi.nlm.nih.gov/37928774/)); O'Donnell et al. 2017 [doi:10.1002/mbo3.509](https://doi.org/10.1002/mbo3.509); Vet Sci 2024 [doi:10.3390/vetsci11020058](https://doi.org/10.3390/vetsci11020058); Han et al. PNAS 2015 [doi:10.1073/pnas.1501598112](https://doi.org/10.1073/pnas.1501598112).

**Per-strain isolation sources (§3 table)** — LPSN species pages (lpsn.dsmz.de) and the protologue DOIs cited inline, each fetched individually on 2026-08-17. **Exception, unverified:** *Mammaliicoccus sciuri* (squirrel) and *Actinomyces viscosus* (hamster periodontal lesions) are asserted from etymology and general knowledge; I did not fetch their protologues. Do not cite them in a definition without checking.

**Standards (§6)** — GSC MIxS HostAssociated extension, [genomicsstandardsconsortium.github.io/mixs/0016002/](https://genomicsstandardsconsortium.github.io/mixs/0016002/); `host_taxid` = MIXS:0000250, mandatory in the host-associated package, [terms.tdwg.org/wiki/mixs:host_taxid](https://terms.tdwg.org/wiki/mixs:host_taxid). MIxS-SA symbiont extension: *Sci Data* 9:736 (2022), [PMC9723553](https://pmc.ncbi.nlm.nih.gov/articles/PMC9723553/).

**Explicitly my inference, not a source's claim:**
- That the concept's boundary is drawn at family rank rather than vernacular name. *(Inferred from the vole and hamster attestations falling on this side; BacDive publishes no scope note for the tag.)*
- That the residual "Other" naming is a data-management convention rather than a biological claim. *(Inferred from the tag's shape; no BacDive statement found.)*
- That §1.4's *Actinobacillus capsulatus* placement is a mis-binning. **Unresolved — flagged, not concluded.**

---

## 5. Synonyms, and what not to conflate

**Names in real use for approximately this concept**
- *Rodentia (Other)* — BacDive's own rendering; the only exact synonym.
- *non-murid rodent host* — descriptive, used in comparative rodent-microbiome work.
- *caviomorph / hystricomorph rodent host* — covers guinea pig and chinchilla but **not** hamster, vole, beaver or squirrel. **Narrower, not a synonym.**
- *"exotic companion mammal"* (guinea pig, chinchilla, hamster) — veterinary usage; overlaps heavily but wrongly includes rabbits and ferrets.

**Do not conflate with**
- **`Muridae-Mouse/Rat`** (`habitatmech:BACDIVE.ab17ecb10f`) — the disjoint sibling. Its 325 assertions are a separate concept, and its own record is already `REVIEW` for an over-narrow xref to *Rattus* alone.
- **Rodentia as a taxon** (NCBITaxon:9989) — a class of organisms, not a place. `relation: xref` only.
- **Lagomorpha (rabbits, hares)** — a *different order*. The vernacular grouping "small furry lab animals" merges them; the tag does not. Bears directly on the *A. capsulatus* question in §1.4.
- **Rodent burrows, nests, middens and animal litter** — those are `ENVO:00005803` *animal habitation* / `ENVO:00002191` *animal litter*, environments an animal *makes*, not the animal *as* an environment.
- **Murine gut / mouse model microbiome literature** — nearly all of it is the sibling concept. A definition written from "rodent microbiome" review articles will silently describe *Mus musculus*.
- **`NCIT:C17649` *Other*** — the retired lexical merge. Any future re-grounding attempt on the trailing word must be refused.

---

## 6. Should it be a term at all?

**Yes — this is a habitat, and it should keep a minted identity. But it should not be term-requested to ENVO in this shape.**

**Why it is a habitat.** A rodent acting as a host *is* where the microbe lives, which is exactly what ENVO models at `ENVO:01001002`. This is the CLAUDE.md rule that #114 and #112 paid for: the *taxon term* is not a place, but the *organism acting as host* is. `NOT_APPLICABLE` is the wrong disposition — it is reserved for diseases, qualities, processes and procedures, and `tests/test_decisions.py` fails on a NOT_APPLICABLE whose target is an organism term. 97 strain assertions across 80 taxa, each recovered from a physical rodent body site, is a real habitat with real sampling behind it.

**Why it should not be term-requested as-is.** Three problems, in order of severity:

1. **Residual classes do not take Aristotelian definitions.** A negative differentia ("of a family other than Muridae") makes the class's extension depend on where a *different* class draws its boundary. If BacDive later splits out `Cricetidae` as a third tag, this class silently shrinks and every prior annotation changes meaning. ENVO will not accept that, and it should not.
2. **The genus jump is two levels.** ENVO has no `vertebrate-associated` and no `mammal-associated environment` (§2.2). Requesting `rodent-associated environment` as a direct child of `animal-associated environment` is defensible — `cnidarian-associated environment` sets exactly that precedent — but it is worth saying in the request that the intermediate rungs are absent.
3. **MIxS already solves this with a slot, not a class.** `host_taxid` (MIXS:0000250) is a *mandatory* field of the host-associated package precisely so that host identity is carried as an NCBI taxid rather than as a proliferation of taxon-scoped environment classes. An ontology term per rodent family is a road ENVO has deliberately not gone down.

**Recommended disposition** (curator's call; this is my recommendation, not a source's):

- **Grounding:** keep `UNGROUNDED` — the existing `CONFIRM_UNGROUNDED` decision stands and is correct.
- **Parent:** the record currently has **no** parent, which is why it landed in `needs_a_parent_first.tsv`. Attach **`ENVO:01001002` *animal-associated environment*** as `parent_habitats` (`relation: parent`). It is genuinely broader, and it asserts nothing the sources do not — every attestation is from an animal.
- **Xref, not parent:** `NCBITaxon:9989` *Rodentia*, `relation: xref`. Optionally also `NCBITaxon:10066` *Muridae* as the excluded sibling — though an xref cannot express exclusion, so a note is better.
- **Category:** `OTHER` is arguably wrong now that the NCIT merge is retired; this is a host-associated concept. Worth checking whether the seeder's category assignment still derives from the retired grouping.
- **Term request, if one is made:** request **`rodent-associated environment`** — *An animal-associated environment which is determined by a rodent.* — as a child of `ENVO:01001002`, and let `Rodentia-Other` hang under it as a HabitatMech-local residual with the murid exclusion in a **scope note**, not in the definition. Do **not** request `Rodentia-Other` itself; a bucket boundary is not an ontological one. *(Per the standing rule in this repo's memory, any actual ENVO submission needs an explicit per-request yes.)*
- **Scope note to record verbatim on the record:** "Residual partition of BacDive's `#Host` level-2 tags: rodent hosts not assigned to `#Muridae (Mouse/Rat)`. The boundary is drawn at family rank, so hamsters and voles (Cricetidae) fall here despite vernacular names. Tag assignment follows the deposited strain's recorded host, not the species' canonical host — *Citrobacter rodentium* DSM 16636 is here because DSMZ records its host as hamster. At least one attesting taxon (*Actinobacillus capsulatus*) has a rabbit-derived type strain, i.e. Lagomorpha, outside the stated scope."

**If the definition sentence must stand alone without the intermediate class**, the least-bad single sentence is the one at the top of this report. It is honest about the negative differentia rather than hiding it, which is preferable to a positive-sounding sentence ("…determined by a hamster, guinea pig, chinchilla, vole, beaver or squirrel") that enumerates a list the source never closed.

## Citations

1. https://doi.org/10.1093/nar/gkab961
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC8728306/
3. https://doi.org/10.1093/nar/gky879
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC6323973/
5. https://bacdive.dsmz.de/isolation-sources
6. https://www.ebi.ac.uk/ols4/ontologies/ncit/classes?obo_id=NCIT:C17649
7. https://pubmed.ncbi.nlm.nih.gov/7559949/
8. https://www.dsmz.de/collection/catalogue/details/culture/DSM-16636
9. https://doi.org/10.1016/s0368-1742(62
10. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
11. https://doi.org/10.1093/jmammal/gyx147
12. https://doi.org/10.1002/mbo3.509
13. https://doi.org/10.3390/vetsci11020058
14. https://www.animbiosci.org/journal/view.php?number=19756
15. https://doi.org/10.1371/journal.pone.0316101
16. https://doi.org/10.1093/nsr/nwad209
17. https://doi.org/10.1073/pnas.1501598112
18. https://doi.org/10.1099/ijs.0.65296-0
19. https://doi.org/10.1099/ijs.0.051326-0
20. https://doi.org/10.1099/ijsem.0.000922
21. https://pubmed.ncbi.nlm.nih.gov/26813893/
22. https://doi.org/10.1099/ijs.0.032706-0
23. https://doi.org/10.1128/jcm.38.10.3722-3728.2000
24. https://doi.org/10.1099/ijs.0.011429-0
25. https://doi.org/10.1099/ijs.0.63433-0
26. https://doi.org/10.1099/ijs.0.024174-0
27. https://github.com/EnvironmentOntology/envo/issues
28. https://pubmed.ncbi.nlm.nih.gov/37928774/
29. https://genomicsstandardsconsortium.github.io/mixs/0016002/
30. https://terms.tdwg.org/wiki/mixs:host_taxid
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC9723553/