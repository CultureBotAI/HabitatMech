---
provider: claude_code
model: claude-opus-5[1m]
cached: false
start_time: '2026-08-18T03:39:22.205072'
end_time: '2026-08-18T03:48:06.795069'
duration_seconds: 524.59
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Larva
  habitat_identifier: habitatmech:GOLD.c4c779417d
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Arthropoda: Crustaceans > Larva'
  assertions: '0'
  parent_terms: (none)
  xrefs: UBERON:0002548
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term UBERON:0002548 'larva' attached as a parent. Life-stage review\
    \ (#112): carried UBERON:0002548 'larva' as a parent, reached by the ambiguous-leaf\
    \ rule rather than the path \u2014 several GOLD paths end in the same leaf, so\
    \ the ones that do not claim the term keep it as a parent. parent_habitats asserts\
    \ the parent is BROADER, and a larva or embryo is a whole organism rather than\
    \ a broader kind of place, so this is the same over-claim the identity cases had\
    \ one level up. Kept as an xref (#99). Per the rule #114 settled: the whole host\
    \ organism gets its own identity and an <X>-associated environment term; parts\
    \ of a host ground to the anatomy term. (source concept habitatmech:GOLD.c4c779417d)"
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
  web_search_requests: 8
  num_turns: 32
  total_cost_usd: 2.6197240000000006
  session_id: 513675c7-768f-4446-bc5b-21ac19e09e7a
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 29
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Larva
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.c4c779417d
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Arthropoda: Crustaceans > Larva
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** UBERON:0002548

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term UBERON:0002548 'larva' attached as a parent. Life-stage review (#112): carried UBERON:0002548 'larva' as a parent, reached by the ambiguous-leaf rule rather than the path — several GOLD paths end in the same leaf, so the ones that do not claim the term keep it as a parent. parent_habitats asserts the parent is BROADER, and a larva or embryo is a whole organism rather than a broader kind of place, so this is the same over-claim the identity cases had one level up. Kept as an xref (#99). Per the rule #114 settled: the whole host organism gets its own identity and an <X>-associated environment term; parts of a host ground to the anatomy term. (source concept habitatmech:GOLD.c4c779417d)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Larva** as a microbial habitat, with citations.

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

# Definition research: **Larva** (`habitatmech:GOLD.c4c779417d`)

> **Proposed definition:** An animal-associated environment which is determined by the body of a crustacean during a post-hatching, pre-juvenile larval stage of its life cycle.

Alternative wording if the curator prefers the aquatic genus (see §2 for why it is defensible here even though it was rejected one level up):

> An environment associated with an aquatic invertebrate which is determined by the body of a crustacean during a post-hatching, pre-juvenile larval stage of its life cycle.

---

## 1. What the concept denotes

**The sampled thing is a crustacean larva — the whole small animal, or a dissected part of it — treated as the place where microbes live.** The GOLD path is unambiguous about the host clade: `Host-associated > Arthropoda: Crustaceans > Larva`. The concept's own children in GOLD settle the sampling question:

| GOLD path | HabitatMech |
|---|---|
| `… > Crustaceans > Larva` | **this record** |
| `… > Crustaceans > Larva > Whole body` | `data/habitats/host_associated/whole_body__1542aa15.yaml` |
| `… > Crustaceans > Larva > Gut` | `data/habitats/host_associated/gut__0d32d8a8.yaml` |

(verified in `data/raw/gold_ecosystem_paths.tsv`)

So the concept is the larval organism as a host; the material actually extracted is either a whole-larva homogenate or, in larvae large enough to dissect, the larval gut. Whole-larva homogenate is the norm in this literature precisely because most crustacean larvae are too small to dissect — a whole-body sample therefore pools the chitinous cuticle surface, the gut lumen and its contents, and the haemocoel into one community ([Litopenaeus vannamei larval time series, *Microbiome* 8:106, 3 Jul 2020, doi:10.1186/s40168-020-00879-w](https://doi.org/10.1186/s40168-020-00879-w); [*Macrobrachium rosenbergii* 11-zoeal-stage series, *Microorganisms* 13:1881, 12 Aug 2025, doi:10.3390/microorganisms13081881](https://doi.org/10.3390/microorganisms13081881)).

**Physical boundaries of the concept.**

- **Starts at hatching.** The egg, the embryo and (for *Artemia*) the dormant cyst are outside: vibrios colonise and cross the cyst cuticle *before* hatching, and that is described as a distinct, pre-larval compartment ([*Aquaculture* 383:104–111, 2013, doi:10.1016/j.aquaculture.2012.11.030](https://doi.org/10.1016/j.aquaculture.2012.11.030)).
- **Ends at metamorphosis to the postlarva/juvenile.** GOLD keeps `Post-larva` as a separate node, already a separate HabitatMech record (`crustacean_post_larval_stage.yaml`, grounded `CLOSE` to `UBERON:0014858`).
- **Excludes the water the larva is suspended in.** Rearing water is a different GOLD branch entirely (`Engineered > Artificial ecosystem > Aquaculture > Crustaceans tank / pond / raceway`), and the microbiological literature treats larva and rearing water as two communities with distinct successional trajectories that only partly overlap ([doi:10.1186/s40168-020-00879-w](https://doi.org/10.1186/s40168-020-00879-w); [*Microbiol. Spectr.* 10:e04241-22, 21 Dec 2022, doi:10.1128/spectrum.04241-22](https://doi.org/10.1128/spectrum.04241-22)).

**Is the label ambiguous? Yes, in two ways, and only one is resolved by the path.**

1. *Which host?* "Larva" as a bare string is used across the GOLD tree for insects, amphibians and others. The path pins this record to Crustacea. Resolved.
2. *Which larval stage?* Unresolved, and deliberately so. GOLD carries `Larva: Nauplius`, `Larva: Zoea` and `Post-larva` as **siblings** of this node, not children (all three verified in `gold_ecosystem_paths.tsv`; the first two are `larva_nauplius.yaml` / `larva_zoea.yaml`, structured identically to this record — same parent, same `UBERON:0002548` xref). The generic `Larva` node is therefore the *stage-unspecified* reading: a submitter who recorded "larva" without naming nauplius, zoea, mysis, megalopa, phyllosoma or cypris. The definition should not name a stage.

> **Modelling flag for the curator, not a definition question:** logically, `Larva` is broader than `Larva: Nauplius` and `Larva: Zoea`, yet all three sit as siblings under `Arthropoda: Crustaceans`. If HabitatMech wants the hierarchy to reflect the biology rather than GOLD's flattening, `GOLD.c4c779417d` is the natural parent of the two named-stage records. That is a seeder/parentage change, not a definition change.

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001002` *animal-associated environment*** — "An environmental system determined by an animal." In the vendored slice (`data/raw/ontology_terms.tsv`), not deprecated. This is also the genus the parent record `habitatmech:GOLD.2959225799` ('Arthropoda: Crustaceans') already uses, so the two definitions nest without introducing a new intermediate.

**Near-misses, checked in ENVO via OLS4 and against the vendored slice:**

| Term | Why it is not an identity match |
|---|---|
| `ENVO:01001176` *environment associated with an aquatic invertebrate* — "An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system." | **Broader-but-true, and a legitimate parent here.** It names neither Crustacea nor the larval stage, so it cannot be the identity. Note that the objection recorded one level up — that it "excludes terrestrial crustaceans" — does **not** apply at this level: the terrestrial crustaceans that lack an aquatic phase (oniscidean woodlice, most amphipods) are direct developers with no free larva at all, and terrestrial decapods such as land and coconut crabs release their zoea larvae into the sea. *This is my inference from the developmental biology, supported by the standard references* ([Anger, *The Biology of Decapod Crustacean Larvae*, Crustacean Issues 14, Balkema 2001](https://www.taylorfrancis.com/books/mono/10.1201/9781003077461/biology-decapod-crustacean-larvae-klaus-anger); [Martin, Olesen & Høeg (eds), *Atlas of Crustacean Larvae*, Johns Hopkins UP 2014, doi:10.1353/book.31448](https://doi.org/10.1353/book.31448)) *— not a sentence any single source states about the ENVO term.* Verified via OLS4: this term is a child of both `ENVO:01001002` and `ENVO:01001055`. It **is** in the vendored slice. |
| `ENVO:01001055` *environment associated with an animal part or small animal* — "An environmental system determined by part of a living or dead animal, or a whole small animal." | Also broader-but-true, and interesting because "a whole small animal" describes a sub-millimetre crustacean larva exactly. Still names no host clade and no life stage. In the slice. Its only asserted parent in ENVO is `ENVO:01001110` *ecosystem*, so it does not chain under `animal-associated environment`; using it as the genus would place this record outside the branch its own parent record sits in. |
| `ENVO:01001000` *environmental system determined by an organism* | Two levels too broad; drops "animal". |
| `ENVO:01001179` *cnidarian-associated environment* | Wrong clade — cited only to show the naming pattern ENVO uses for a clade-specific host environment, which is the pattern a term request should follow. |
| `ENVO:01000905` *shrimp pond* | The engineered water body, not the animal. Neighbouring concept; maps to the `Engineered > Aquaculture` branch. |
| `UBERON:0002548` *larva* | The **organism**, not a place. Per the rule #114 settled and #112 applied, the whole host organism gets its own minted identity and carries the organism term as `relation: xref` — which is what the record already does. |
| `UBERON:0000069` *larval stage*; `UBERON:0018378` *crustacean larval stage*; `UBERON:0014858` *crustacean post-larval stage* | **Temporal stages**, not environments — a life-cycle interval cannot be sampled. `UBERON:0018378` would be the tightest available xref for "crustacean larva, stage unspecified", but **it is not in the vendored slice** (only `0000069`, `0002548` and `0014858` are), so a `GROUND`/xref against it would fail the slice check until ENVO/UBERON is re-vendored. |

**Conclusion on ENVO coverage:** I enumerated the descendants of `ENVO:01001002` via OLS4 — they are `ENVO:01001176`, `ENVO:01001179`, and (anomalously) the human-settlement subtree. There is **no** arthropod-, crustacean-, or insect-associated environment class in ENVO, and a wildcard search of ENVO for `larva*` returns only `UBERON:0000922` *embryo* by cross-reference. The `UNGROUNDED` disposition is correct.

---

## 3. Differentia — what distinguishes it

Ordered by how observable each property is.

**a. Host clade — Crustacea.** Fixed by the path. Distinguishes this from insect, amphibian, echinoderm and mollusc larva records under other GOLD host branches.

**b. Life stage — post-hatching and pre-juvenile.** This is the differentia that does real work, because the larval microbiome of a crustacean is *not* a small version of the adult's. Alpha-diversity across the *L. vannamei* developmental cycle is U-shaped, with zoea and mysis as the valley, and 89.1% of samples cluster by developmental stage into four groups (nauplius / zoea I–II / zoea III / mysis+postlarvae) ([doi:10.1186/s40168-020-00879-w](https://doi.org/10.1186/s40168-020-00879-w)). *Penaeus stylirostris* larvae likewise show stage-specific microbiotas and stage biomarkers over a shared core ([doi:10.3390/microorganisms12030608](https://doi.org/10.3390/microorganisms12030608)).

**c. Size and sampling unit — whole small animal.** Larvae are sampled whole; the community is a pooled cuticle + gut + haemocoel community. In an insect meta-analysis the same methodological point is made explicitly — gut-only samples have significantly lower diversity than whole larvae, the difference being cuticle- and body-associated taxa ([*Sci. Rep.* 12, 2022, PMC9453823](https://pmc.ncbi.nlm.nih.gov/articles/PMC9453823/)). *That the same holds for crustacean larvae is my inference from the shared sampling constraint, though it is consistent with the crustacean carapace-community literature in (e) below.*

**d. Gut ontogeny — a discontinuity adults do not have.** The larval digestive tract is not functional at hatching; the nauplius is lecithotrophic and the gut opens to the environment at the nauplius→zoea "mouth opening" transition. This is treated as *the* pivotal event in larval microbiome assembly: source-tracking shows rearing water dominating as a source at mouth opening, with internal succession taking over afterwards ([*Aquaculture*, 2025, doi:10.1016/j.aquaculture.2025.742659 — preprint at bioRxiv 2025.05.25.655974](https://doi.org/10.1101/2025.05.25.655974)); host selection for Rhodobacteraceae out of the rearing water begins at the zoea stage ([doi:10.1186/s40168-020-00879-w](https://doi.org/10.1186/s40168-020-00879-w)).

**e. Ecdysis — periodic loss of the surface habitat.** Crustaceans shed the exoskeleton, and with it a major part of the associated community, at every moult, which happens repeatedly across the larval phase. In *Portunus trituberculatus*, Rhodobacteraceae is significantly discarded with the shed shell and re-recruited over the 72 h postmoult, with early colonists (Pseudoalteromonadaceae, Oceanospirillaceae) assembling under homogeneous selection and late colonists (Flavobacteriaceae, Pseudomonadaceae) under drift and dispersal limitation ([*Aquaculture* 589:740863, Jun 2024, doi:10.1016/j.aquaculture.2024.740863](https://doi.org/10.1016/j.aquaculture.2024.740863)). Gut communities also restructure across the moult cycle in *Macrobrachium rosenbergii* ([*Aquaculture* 464:105–111, 2016, doi:10.1016/j.aquaculture.2016.06.021](https://doi.org/10.1016/j.aquaculture.2016.06.021)).

**f. Dominant material — chitin, immersed in water.** The larval surface is a chitinous cuticle in an aqueous medium, which is a nutritionally active substrate rather than an inert one: all pathogenic vibrios secrete extracellular chitinase and use chitin as a carbon and nitrogen source, and attachment to chitinous crustacean surfaces confers protection from environmental stress. This is the classic *Vibrio cholerae*–copepod relationship, and it is documented specifically for copepod eggs and **nauplii** as distinct from adults ([Huq et al., *Appl. Environ. Microbiol.* 45:275–283, Jan 1983, doi:10.1128/aem.45.1.275-283.1983](https://doi.org/10.1128/aem.45.1.275-283.1983); [*Front. Microbiol.* 4:375, 2013, doi:10.3389/fmicb.2013.00375](https://doi.org/10.3389/fmicb.2013.00375); [*Front. Microbiol.* 2:260, 2011, doi:10.3389/fmicb.2011.00260](https://doi.org/10.3389/fmicb.2011.00260)).

**g. Characteristic taxa.** Rhodobacteraceae (persistently dominant after mouth opening, and a probiotic-candidate source), Vibrionaceae, Flavobacteriaceae, Pseudoalteromonadaceae ([doi:10.1186/s40168-020-00879-w](https://doi.org/10.1186/s40168-020-00879-w); [doi:10.1016/j.aquaculture.2024.740863](https://doi.org/10.1016/j.aquaculture.2024.740863)). *Vibrio* is dual-role: `V. owensii` DY05 is the demonstrated aetiological agent of mass mortality in cultured *Panulirus ornatus* phyllosomas, proliferating in the larval hepatopancreas, and is vectored via *Artemia* live feed ([*Appl. Environ. Microbiol.* 78:2841–2849, 15 Apr 2012, doi:10.1128/aem.07274-11](https://doi.org/10.1128/aem.07274-11)), while vibrios are also routine commensals of healthy lobster guts with putative roles in chitin digestion ([*Fishes* 7:108, 2022, doi:10.3390/fishes7030108](https://doi.org/10.3390/fishes7030108)).

**h. Wild vs. cultured is a real axis, not noise.** Clone libraries from *wild* phyllosomas are dominated by alphaproteobacteria (*Sulfitobacter*) with *Vibrio* rarely detected, the inverse of hatchery-reared animals ([doi:10.3390/fishes7030108](https://doi.org/10.3390/fishes7030108) and refs therein). Relevant to the definition only in that it must **not** build "aquaculture" into the differentia — the concept covers wild plankton-caught larvae as well as larviculture.

**Recommended one-sentence differentia (matches the lead):** *…determined by the body of a crustacean during a post-hatching, pre-juvenile larval stage of its life cycle.* Everything in (c)–(h) is what a curator would put in a comment, not in the defining sentence — trying to fit ecdysis, mouth opening and chitin into one sentence is what a `crustacean larva-associated environment` ENVO term request should carry as its own annotations.

---

## 4. Synonyms, and what not to conflate

**Names in real use for this concept**

- crustacean larva / crustacean larvae; larval crustacean
- shrimp larvae, prawn larvae, crab larvae (species-level usages of the same concept)
- brine shrimp nauplii / *Artemia* nauplii — the single most-studied instance, both as a gnotobiotic model host and as live feed ([*Appl. Environ. Microbiol.* 71:4307–4317, Aug 2005, doi:10.1128/aem.71.8.4307-4317.2005](https://doi.org/10.1128/aem.71.8.4307-4317.2005))
- "larvae" as the sampling unit in **larviculture** / hatchery studies
- meroplankton, planktonic larvae (ecological framing; broader — includes non-crustacean larvae)

**Stage names that are narrower, not synonyms:** nauplius, metanauplius, zoea, mysis, megalopa, phyllosoma, cypris/cyprid, protozoea. Nauplius and zoea already have their own HabitatMech records; treating any of them as an exact synonym of the generic node would collapse three distinct records.

**Commonly but wrongly treated as the same thing**

| Not this concept | Why |
|---|---|
| **Rearing / hatchery water** | Separate GOLD branch (`Engineered > Aquaculture > Crustaceans tank`); the two communities are separately tracked and only partly overlapping ([doi:10.1128/spectrum.04241-22](https://doi.org/10.1128/spectrum.04241-22)). |
| **Egg, embryo, *Artemia* cyst** | Pre-hatching; the cyst has its own colonisation dynamics ([doi:10.1016/j.aquaculture.2012.11.030](https://doi.org/10.1016/j.aquaculture.2012.11.030)). Maternal/vertical transmission across that boundary is documented ([doi:10.3390/microorganisms12030608](https://doi.org/10.3390/microorganisms12030608)) but does not merge the concepts. |
| **Post-larva, juvenile, adult** | Separate GOLD nodes and separate HabitatMech records; stage-clustered communities (§3b). |
| **`UBERON:0002548` larva (the organism)** | Organism ≠ place. Already correctly held as `relation: xref`. |
| **`UBERON:0000069` / `UBERON:0018378` (stages)** | Temporal intervals; not samplable. |
| **Insect / amphibian / echinoderm larvae** | The ambiguous-leaf case that produced this record in the first place. Different host branches, different records. |
| **"*Artemia* as live feed"** | When *Artemia* nauplii are sampled as a **vector** into a shrimp or lobster hatchery, the sample is still a crustacean larva — but the study's habitat of interest is often the fed animal. Frozen *Artemia* has been identified as a major source of vibrios into larval tanks ([doi:10.1101/2025.05.25.655974](https://doi.org/10.1101/2025.05.25.655974)). Worth a comment; not a separate term. |
| **`host_life_stage` (MIxS)** | The MIxS host-associated package records life stage as a **host attribute** field, not as an environment ([GSC MIxS term `host_life_stage`, MIXS:0000251](https://genomicsstandardsconsortium.github.io/mixs/0000251/)). A sample annotated `host = Penaeus vannamei; host_life_stage = zoea` and one annotated with this HabitatMech term describe the same material by different means — do not treat the MIxS field as evidence that no environment term is needed. |

---

## 5. Should it be a term at all?

**Yes — keep it, keep it `UNGROUNDED` with its minted identifier, and file it as an ENVO term-request candidate.** Three checks:

1. **Is it a place?** Yes, under the rule #114 settled: an organism acting as host *is* a habitat, and ENVO models exactly this at plant-, animal- and fungi-associated environment. What is not a place is the *taxon term* or the *stage term* — hence `UBERON:0002548` stays as `relation: xref`. This is not a disease, quality, process, procedure or sampling artefact, so `NOT_APPLICABLE` would be the wrong disposition.
2. **Is it a whole organism rather than a part?** Yes — a larva is the entire animal at a life stage, so per #112 it keeps its own identity rather than grounding to an anatomy term. Its own children (`Gut`, `Whole body`) are where the part/whole distinction gets applied.
3. **Does it earn a term distinct from its parent?** Yes. Stage-clustered communities, the mouth-opening discontinuity, ecdysis-driven turnover and the fact that larvae are the operational sampling unit of an entire applied field (larviculture) all mean "crustacean larva" is not merely "crustacean, younger" (§3b, §3d, §3e).

**Recommended ENVO term request** — two terms, following the `cnidarian-associated environment` (`ENVO:01001179`) naming pattern:

- `crustacean-associated environment` — *An animal-associated environment which is determined by a crustacean or part of a crustacean* (this belongs to the parent record `habitatmech:GOLD.2959225799`);
- `crustacean larva-associated environment` — *A crustacean-associated environment which is determined by a crustacean at a post-hatching, pre-juvenile larval stage*, for this record.

**One inconsistency the curator should decide on before writing the definition.** The sibling `Post-larva` was grounded `CLOSE` to `UBERON:0014858` *crustacean post-larval stage* — a **stage** term — while `Larva`, `Larva: Nauplius` and `Larva: Zoea` were all confirmed `UNGROUNDED` with `UBERON:0002548` as an xref. Under the #112 rule those four are the same kind of concept and should have the same disposition. This does not change the definition proposed above, but writing this definition while `crustacean_post_larval_stage.yaml` claims a stage term as its identity leaves the crustacean life-stage family internally inconsistent. Worth a separate issue.

**Assertion volume caveat:** the brief records upstream assertion volume as 0 for this node, and the record notes that 3 GOLD ecosystem node ids share this path. So there is no GOLD organism annotated at this exact node — the case for the term rests on the child nodes (`Whole body`, `Gut`), the named-stage siblings, and the published literature below, not on upstream counts.

---

## 6. Sources

**Ontologies and standards** (all term facts verified against OLS4 or `data/raw/ontology_terms.tsv` on 18 Aug 2026)

- ENVO `ENVO:01001002` animal-associated environment — http://purl.obolibrary.org/obo/ENVO_01001002
- ENVO `ENVO:01001055` environment associated with an animal part or small animal — http://purl.obolibrary.org/obo/ENVO_01001055
- ENVO `ENVO:01001176` environment associated with an aquatic invertebrate — http://purl.obolibrary.org/obo/ENVO_01001176
- ENVO `ENVO:01001179` cnidarian-associated environment — http://purl.obolibrary.org/obo/ENVO_01001179
- UBERON `UBERON:0002548` larva; `UBERON:0000069` larval stage; `UBERON:0018378` crustacean larval stage; `UBERON:0014858` crustacean post-larval stage — http://purl.obolibrary.org/obo/UBERON_0018378
- Buttigieg et al., *The environment ontology: contextualising biological and biomedical entities*, J. Biomed. Semantics 4:43 (2013) — https://doi.org/10.1186/2041-1480-4-43
- Buttigieg et al., *The environment ontology in 2016*, J. Biomed. Semantics 7:57 (2016) — https://doi.org/10.1186/s13326-016-0097-6
- GSC MIxS term `host_life_stage` (MIXS:0000251) — https://genomicsstandardsconsortium.github.io/mixs/0000251/
- Yilmaz et al., *Minimum information about a marker gene sequence (MIMARKS) and MIxS specifications*, Nat. Biotechnol. 29:415–420 (2011) — https://doi.org/10.1038/nbt.1823

**Reference works on what a crustacean larva is**

- Martin, Olesen & Høeg (eds), *Atlas of Crustacean Larvae*, Johns Hopkins University Press (2014) — https://doi.org/10.1353/book.31448
- Anger, *The Biology of Decapod Crustacean Larvae*, Crustacean Issues 14, Balkema (2001) — https://www.taylorfrancis.com/books/mono/10.1201/9781003077461/biology-decapod-crustacean-larvae-klaus-anger

**Primary literature on the larva as a microbial habitat**

- Wang et al., *Fine-scale succession patterns and assembly mechanisms of bacterial community of Litopenaeus vannamei larvae across the developmental cycle*, Microbiome 8:106 (3 Jul 2020), PMID 32620132 — https://doi.org/10.1186/s40168-020-00879-w
- Zheng et al., *Succession, sources, and assembly of bacterial community in the developing crab larval microbiome*, Aquaculture 548:737600 (Feb 2022) — https://doi.org/10.1016/j.aquaculture.2021.737600
- *Dynamics and assembly mechanisms of bacterial communities during larval development of Macrobrachium rosenbergii*, Microorganisms 13:1881 (12 Aug 2025), PMID 40871385 — https://doi.org/10.3390/microorganisms13081881
- Callac et al., *Active microbiota of Penaeus stylirostris larvae: partially shaped via vertical and horizontal transmissions and larval ontogeny*, Microorganisms 12:608 (19 Mar 2024), PMID 38543660 — https://doi.org/10.3390/microorganisms12030608
- Callac et al., *Microbiota of the rearing water of Penaeus stylirostris larvae…*, Microbiol. Spectr. 10:e04241-22 (21 Dec 2022), PMID 36416556 — https://doi.org/10.1128/spectrum.04241-22
- *Source tracking of larval bacterial community of Pacific white shrimp across the developmental cycle*, Aquaculture (2025); preprint bioRxiv 2025.05.25.655974 — https://doi.org/10.1101/2025.05.25.655974
- *Reassembly and biotic sources of carapace bacterial community of Portunus trituberculatus after host molting*, Aquaculture 589:740863 (Jun 2024) — https://doi.org/10.1016/j.aquaculture.2024.740863
- Zhang et al., *Gut microbial communities associated with the molting stages of the giant freshwater prawn Macrobrachium rosenbergii*, Aquaculture 464:105–111 (2016) — https://doi.org/10.1016/j.aquaculture.2016.06.021
- Goulden et al., *Pathogenicity and infection cycle of Vibrio owensii in larviculture of the ornate spiny lobster (Panulirus ornatus)*, Appl. Environ. Microbiol. 78:2841–2849 (15 Apr 2012) — https://doi.org/10.1128/aem.07274-11
- Goulden et al., *Identification of an antagonistic probiotic combination protecting ornate spiny lobster larvae against Vibrio owensii infection*, PLoS ONE 7:e39667 (5 Jul 2012) — https://doi.org/10.1371/journal.pone.0039667
- Marques et al., *Effects of bacteria on Artemia franciscana cultured in different gnotobiotic environments*, Appl. Environ. Microbiol. 71:4307–4317 (Aug 2005) — https://doi.org/10.1128/aem.71.8.4307-4317.2005
- Defoirdt et al., *Poly-β-hydroxybutyrate-accumulating bacteria protect gnotobiotic Artemia franciscana from pathogenic Vibrio campbellii*, FEMS Microbiol. Ecol. 60:363–369 (2007), PMID 17391334 — https://doi.org/10.1111/j.1574-6941.2007.00305.x
- *Proliferation, colonization, and detrimental effects of Vibrio parahaemolyticus and Vibrio harveyi during brine shrimp hatching*, Aquaculture 383:104–111 (2013) — https://doi.org/10.1016/j.aquaculture.2012.11.030
- Huq et al., *Ecological relationships between Vibrio cholerae and planktonic crustacean copepods*, Appl. Environ. Microbiol. 45:275–283 (Jan 1983) — https://doi.org/10.1128/aem.45.1.275-283.1983
- Almagro-Moreno & Taylor, *Cholera: environmental reservoirs and impact on disease transmission* / *Environmental reservoirs and mechanisms of persistence of Vibrio cholerae*, Front. Microbiol. 4:375 (2013) — https://doi.org/10.3389/fmicb.2013.00375
- Nalin-tradition review: *Role of shrimp chitin in the ecology of toxigenic Vibrio cholerae and cholera transmission*, Front. Microbiol. 2:260 (2011) — https://doi.org/10.3389/fmicb.2011.00260
- Holt et al., *Understanding the role of the shrimp gut microbiome…* / *Gastrointestinal microbiota of spiny lobster: a review*, Fishes 7:108 (2022) — https://doi.org/10.3390/fishes7030108
- *Meta-analysis of larvae of the black soldier fly (Hermetia illucens) microbiota based on 16S rRNA gene amplicon sequencing*, FEMS Microbiol. Ecol. (2022), PMC9453823 — https://pmc.ncbi.nlm.nih.gov/articles/PMC9453823/ *(cited only for the whole-larva vs. gut-only sampling point; the organism is an insect, not a crustacean)*

**Explicitly marked as inference, not sourced claims**

- That essentially every free-living crustacean *larva* is aquatic, so `ENVO:01001176` is a safe parent at this level even though it was rejected as an identity for the crustacean parent record (§2). Grounded in the developmental-biology references, but no source states it about the ENVO term.
- That whole-larva homogenates in crustaceans pool cuticle + gut + haemocoel communities in the way the insect meta-analysis documents (§3c). Consistent with the *Portunus* carapace-community work, but not directly measured as a crustacean-larval sampling comparison in anything I found.
- The modelling observations in §1 and §5 (sibling-vs-child parentage of the named larval stages; the `Post-larva` grounding inconsistency) are my reading of the corpus, not claims from any source.

## Citations

1. https://doi.org/10.1186/s40168-020-00879-w
2. https://doi.org/10.3390/microorganisms13081881
3. https://doi.org/10.1016/j.aquaculture.2012.11.030
4. https://doi.org/10.1128/spectrum.04241-22
5. https://www.taylorfrancis.com/books/mono/10.1201/9781003077461/biology-decapod-crustacean-larvae-klaus-anger
6. https://doi.org/10.1353/book.31448
7. https://doi.org/10.3390/microorganisms12030608
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC9453823/
9. https://doi.org/10.1101/2025.05.25.655974
10. https://doi.org/10.1016/j.aquaculture.2024.740863
11. https://doi.org/10.1016/j.aquaculture.2016.06.021
12. https://doi.org/10.1128/aem.45.1.275-283.1983
13. https://doi.org/10.3389/fmicb.2013.00375
14. https://doi.org/10.3389/fmicb.2011.00260
15. https://doi.org/10.1128/aem.07274-11
16. https://doi.org/10.3390/fishes7030108
17. https://doi.org/10.1128/aem.71.8.4307-4317.2005
18. https://genomicsstandardsconsortium.github.io/mixs/0000251/
19. http://purl.obolibrary.org/obo/ENVO_01001002
20. http://purl.obolibrary.org/obo/ENVO_01001055
21. http://purl.obolibrary.org/obo/ENVO_01001176
22. http://purl.obolibrary.org/obo/ENVO_01001179
23. http://purl.obolibrary.org/obo/UBERON_0018378
24. https://doi.org/10.1186/2041-1480-4-43
25. https://doi.org/10.1186/s13326-016-0097-6
26. https://doi.org/10.1038/nbt.1823
27. https://doi.org/10.1016/j.aquaculture.2021.737600
28. https://doi.org/10.1371/journal.pone.0039667
29. https://doi.org/10.1111/j.1574-6941.2007.00305.x