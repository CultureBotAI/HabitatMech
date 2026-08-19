---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:09:09.058004'
end_time: '2026-08-17T16:17:57.652224'
duration_seconds: 528.59
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: 'Arthropoda: Insects'
  habitat_identifier: habitatmech:GOLD.dba2a83b95
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Arthropoda: Insects'
  assertions: '1833'
  parent_terms: ENVO:01001000, ENVO:01001002
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Nearest
    broader term ENVO:01001002 ''animal-associated environment'' attached as a parent.
    Insects as host. Parented to animal-associated environment; not grounded there
    because every host clade would merge onto one record. ENVO term request. (source
    concept habitatmech:GOLD.dba2a83b95)'
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
  num_turns: 30
  total_cost_usd: 3.2006769999999998
  session_id: dcc1f7b5-f6d1-47fb-8914-44aa3e8f31bd
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 24
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Arthropoda: Insects
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.dba2a83b95
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Arthropoda: Insects
- **Upstream assertion volume:** 1833
- **Nearest broader term already on the record:** ENVO:01001000, ENVO:01001002
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:01001002 'animal-associated environment' attached as a parent. Insects as host. Parented to animal-associated environment; not grounded there because every host clade would merge onto one record. ENVO term request. (source concept habitatmech:GOLD.dba2a83b95)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Arthropoda: Insects** as a microbial habitat, with citations.

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

# Definition research: `habitatmech:GOLD.dba2a83b95` — "Arthropoda: Insects"

> **Proposed definition:** An animal-associated environment which is determined by an insect (Insecta) or by a part of an insect.

Proposed label: **insect-associated environment**. Genus: `ENVO:01001002` *animal-associated environment*. Differentia: host clade = Insecta (`NCBITaxon:50557`). This mirrors ENVO's one existing clade-level precedent, `ENVO:01001179` *cnidarian-associated environment* ("An environmental system determined by a cnidarian or part of a cnidarian"), verbatim in form — which is the strongest argument for the request being accepted as-is.

---

## 1. What the concept denotes

**The thing sampled is an insect body, or a site/tissue/product within one.** In GOLD's five-level ecosystem classification, `Host-associated` is the top-level Ecosystem, `Arthropoda: Insects` is the Ecosystem Category, and everything below it is a body site or life stage of that host ([Mukherjee et al. 2023, *NAR* 51:D957, GOLD v.9](https://academic.oup.com/nar/article/51/D1/D957/6786204); [GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)). The label names the host clade because in GOLD the host *is* the environmental category.

The repo's own copy of the GOLD path table settles the scope empirically. `data/raw/gold_ecosystem_paths.tsv` holds **87 paths** rooted at `Host-associated > Arthropoda: Insects`, carrying **3,292 organism assertions** in total, of which **1,833 sit on the bare node itself** — i.e. isolates recorded as "from an insect" with no body site given. That 1,833 is not a rounding artefact of the hierarchy; it is the largest single count in the subtree and is what this record must be able to hold.

What the children show is inside the concept:

| Path below the node | Organisms |
|---|---|
| `Digestive system > Gut` | 742 |
| `Digestive system` | 203 |
| `Digestive system > Foregut > Regurgitated nectar` | 103 |
| `Larva` | 94 |
| `Digestive system > Hindgut > Fecal` | 87 |
| `Whole body` | 60 |
| `Digestive system > Midgut`; `Head` | 26 each |
| `Excretory system > Malpighian tubules` | 24 |
| `Larva > Gut`; `Digestive system > Hindgut` | 21, 20 |
| `Ootheca/Egg mass > Eggs` | 19 |
| `Circulatory system > Hemolymph` | 9 |
| `Digestive system > Midgut > Caeca: Bacteriome` | 5 |
| `Abdomen`, `Nymph/Instar`, `Fat body`, `Prepupa`, `Crop`, `Mouthparts`, `Rectum`, `Frass`, `Saliva`, `Cuticle`-adjacent segments… | ≤3 each |

So the concept covers: **the gut lumen and its regions, the hemocoel and hemolymph, intracellular sites (bacteriome/mycetome), Malpighian tubules, fat body, the cuticular exterior, eggs, and the pre-adult life stages (larva, nymph/instar, prepupa) — of any member of Insecta.** This matches Douglas's canonical framing of the insect as a multi-compartment habitat: "All insects are colonized by microorganisms on the exoskeleton, in the gut and hemocoel, and within insect cells" ([Douglas 2015, *Annu Rev Entomol* 60:17–34, PMC4465791](https://pmc.ncbi.nlm.nih.gov/articles/PMC4465791/); PMID 25341109).

**Boundary — what is a neighbouring concept, not this one:**

- **Insect-built structures and stored products.** GOLD itself puts these elsewhere: `Environmental > Terrestrial > Nest > Insects nest > Beehive: Honey / Pollen / Brood combs / Cerumen / Royal jelly` is a *sibling of* `Host-associated`, not a descendant of this node. ENVO already covers this side with `ENVO:2000006` *nest of termite* ("An animal habitation constructed by termites") and `ENVO:01000576` *apiary*, and `ENVO:02000004` *nesting material*. A beehive is an animal habitation; the bee is the habitat. Do not merge them. (Note the one edge case: `Digestive system > Foregut > Regurgitated nectar`, 103 assertions, is honey-in-the-crop — GOLD deliberately files that inside the bee, and that placement is right.)
- **Other arthropods.** GOLD's sibling Ecosystem Categories are `Arthropoda: Chelicerates`, `Arthropoda: Crustaceans` and `Arthropoda: Myriapoda`. This label therefore means Insecta/Hexapoda specifically, not Arthropoda broadly — the "Arthropoda:" prefix is a grouping device in GOLD's category list, not part of the denotation. HabitatMech already has `habitatmech:GOLD.2959225799` for Crustaceans as a parallel UNGROUNDED record.
- **The taxon Insecta itself.** `NCBITaxon:50557` names a class of organisms, not a place. Per CLAUDE.md and #114, the taxon goes in `relation: xref`; the *environment determined by* an insect is the habitat.
- **Frass** (`Hindgut > Frass`) is genuinely ambiguous — excreted material is arguably an environmental material rather than a body site — but GOLD files it under the hindgut and there are 0 assertions on it, so it does not force a decision here.

**Is the label ambiguous?** Only mildly, in two ways, and the source path resolves both. (a) "Insects" could mean Insecta *sensu stricto* or Hexapoda (adding Collembola, Protura, Diplura); GOLD gives no finer partition and the distinction is immaterial at 3,292 assertions — recommend defining on Insecta and noting Hexapoda as an acceptable reading. (b) "Insect-associated" in the wider literature is sometimes used for *insect-visited* or *insect-vectored* material (flowers, dung, carrion). GOLD's `Host-associated` root excludes that reading.

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001002` *animal-associated environment*** — "An environmental system determined by an animal." (verified via [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002)). Insects are animals; the subsumption is unarguable, and it is the genus ENVO used for its own clade-level child.

Its own parent is `ENVO:01001000` *environmental system determined by an organism* — already on the record as a redundant second parent, harmless but implied.

**Near-misses checked in ENVO (OLS4 search over the current release), and why each fails:**

| CURIE | Label | Why it is not the term |
|---|---|---|
| `ENVO:01001176` | environment associated with an aquatic invertebrate | **Narrower on one axis, broader on another.** Its definition requires "a habitat that is found in an aquatic environmental system" — this admits aquatic insect larvae but excludes the overwhelmingly terrestrial bulk of Insecta, and simultaneously admits molluscs, annelids and crustaceans. Same failure as recorded for the Crustaceans sibling record. |
| `ENVO:01001055` | environment associated with an animal part or small animal | **A genuine broader term, worth considering as a second parent.** "An environmental system determined by part of a living or dead animal, or a whole small animal" covers both insect parts and whole insects. It fails as an *identity* because it merges every animal clade and every body part into one class. Flagging it as an additional `parent_habitats` entry is defensible; I'd note that ENVO's own use is loose (it also parents `ENVO:01001829` *human settlement*), so "small" is not a load-bearing criterion there. |
| `ENVO:01001179` | cnidarian-associated environment | Not a match (wrong clade) but the **template**: it establishes that ENVO accepts clade-level `X-associated environment` classes as direct children of animal-associated environment. |
| `ENVO:01001001` / `ENVO:01001041` | plant- / fungi-associated environment | Wrong kingdom; cited only as evidence that the pattern is ENVO's established shape at this level. |
| `ENVO:2000006`, `ENVO:01000576`, `ENVO:02000004` | nest of termite, apiary, nesting material | Insect-*built* structures. Asserts construction and an anthropogenic/architectural framing the GOLD host node does not claim. |
| `ENVO:01001187` | holothurian digestive tract | Structurally the nearest analogue for a *gut* child of this concept, not for the concept. |
| `NCBITaxon:50557` | Insecta | An organism class, not an environment. `relation: xref`. |
| `FOODON:00001177` | insect food product | Insects as food, not as habitat. Different concept entirely. |
| `ENVO:01001636` | insect conservation process | A process. Surfaces first on a naive `insect` search of ENVO — it is a distractor. |

**No ENVO class names this concept.** An OLS4 search of ENVO for `insect` returns no `*-associated environment` class; the confirmed UNGROUNDED status is correct. Two loosely-related ENVO GitHub issues exist ([#802 "Termite gut", 2019, labelled GOLD/EBI-MGNIFY](https://github.com/EnvironmentOntology/envo/issues/802); #981, 2020) but neither requests this class — note that #802 is itself GOLD-driven, which supports the request's provenance.

## 3. Differentia — what distinguishes it

**The formal differentia is the host clade** (Insecta, `NCBITaxon:50557`), because that is how ENVO differentiates every sibling under `ENVO:01001002` and because the host is the whole content of what GOLD is asserting. Everything below is *supporting evidence that the class carves a real habitat*, not additional differentiae to write into the sentence. Stating this distinction explicitly matters: a definition that tried to encode the physicochemistry would be false for some of Insecta.

Properties that make an insect a distinctive, non-arbitrary microbial habitat — each observable, each sourced:

- **Physicochemical extremes not found in the vertebrate siblings.** "The pH of the gut lumen is actively regulated and often diverges from that of the hemolymph… midguts of lepidopteran larvae show extreme alkalinity, with pH as high as 11–12" ([Engel & Moran 2013, *FEMS Microbiol Rev* 37:699–735](https://academic.oup.com/femsre/article/37/5/699/542120), doi:10.1111/1574-6976.12025). At the other pole, soil-feeding termite hindguts exceed pH 12 ([Brune & Kühl 1996, *J Insect Physiol* 42:1121–1127](https://doi.org/10.1016/S0022-1910(96)00036-4)), and microsensor work shows steep O₂ and H₂ gradients such that only the centre of dilated gut regions is anoxic ([Brune, Emerson & Breznak 1995, *AEM* 61:2681–2687](https://journals.asm.org/doi/10.1128/aem.61.7.2681-2687.1995); [Brune 2014, *Nat Rev Microbiol* 12:168–180](https://www.nature.com/articles/nrmicro3182)).
- **Colonization barriers imposed by arthropod anatomy.** Insects shed the cuticular lining of foregut and hindgut at each molt, disrupting attached populations, and repeatedly shed the peritrophic matrix from the midgut (Engel & Moran 2013, as above). This is a formation/turnover process unique to arthropod hosts and it is why insect gut communities are typically low-diversity relative to mammalian guts.
- **Intracellular compartments as distinct habitats.** Obligate endosymbionts occupy bacteriocytes — host cells specialized to house them — with the aphid–*Buchnera aphidicola* association dating to ~200 Mya and *Buchnera* genomes reduced to ~400–600 kb ([Chong et al. 2024, *Sci Data*, PMC11193766](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11193766/); review: [Kim, Weiss & Fukatsu 2024, "Insect Bacteriocytes: Adaptation, Development, and Evolution", *Annu Rev Entomol*](https://www.annualreviews.org/content/journals/10.1146/annurev-ento-010323-124159), doi:10.1146/annurev-ento-010323-124159). GOLD's `Midgut > Caeca: Bacteriome` node is exactly this.
- **Cuticle as a housed, not merely incidental, habitat.** Beewolf wasps hold *Streptomyces* in cuticle-lined antennal gland reservoirs across 5–6 antennal segments, detected in 38 Philanthini species ([Kaltenpoth et al. 2012, PMC3264120](https://pmc.ncbi.nlm.nih.gov/articles/PMC3264120/)); attine ants house *Pseudonocardia* in cuticular crypts ([Li et al. 2018, *PNAS* 115:10720–10725](https://www.pnas.org/doi/10.1073/pnas.1809332115)); *Lagria* beetles house defensive ectosymbionts in dorsal cuticular invaginations ([Flórez et al. 2022, *ISME J* 16:2691–2701](https://www.nature.com/articles/s41396-022-01311-x)).
- **Host-clade-specific community composition.** The honey bee gut carries a distinctive community of ~9 bee-specific bacterial species clusters, socially transmitted, with >99% of sequences in any one bee belonging to phylotypes shared across bees ([Kwong & Moran 2016, *Nat Rev Microbiol* 14:374–384](https://www.nature.com/articles/nrmicro.2016.43), doi:10.1038/nrmicro.2016.43). At the opposite extreme, caterpillars surveyed across 124 species in 15 families showed low-density, individually variable communities with a median 19.5% of the gut assemblage belonging to core phylotypes, and antibiotic suppression did not affect *Manduca sexta* growth or survival ([Hammer et al. 2017, *PNAS* 114:9641–9646](https://www.pnas.org/doi/10.1073/pnas.1707186114), PMID 28830993).
- **Scale.** ~1 million insect species are named, with a mean global estimate of ~5.5 million ([Stork 2018, *Annu Rev Entomol* 63:31–45](https://www.annualreviews.org/doi/10.1146/annurev-ento-020117-043348), doi:10.1146/annurev-ento-020117-043348, PMID 28938083). Endosymbiont incidence is correspondingly vast: after correcting for sampling bias, an estimated 52% (CI 48–57) of arthropod species carry *Wolbachia*, 24% *Rickettsia*, 13% *Cardinium* ([Weinert et al. 2015, *Proc R Soc B* 282:20150249](https://royalsocietypublishing.org/doi/10.1098/rspb.2015.0249)).

**My inference, not a source claim:** the last point is why a single ENVO class is the right granularity. The habitat is heterogeneous enough that one term cannot describe its physicochemistry, but the *host clade* is a stable, checkable, sample-level fact that every submitter can supply — the same reasoning that makes `host_taxid` a required-style slot in the MIxS host-associated extension ([GSC MIxS `HostAssociated` 0016002](https://genomicsstandardsconsortium.github.io/mixs/0016002/)).

## 4. Sources

Full citations for every claim above, gathered:

| Claim | Source |
|---|---|
| GOLD five-level classification; `Host-associated` root; host-associated package | Mukherjee et al. 2023, *Nucleic Acids Research* 51(D1):D957, doi:10.1093/nar/gkac974 — https://academic.oup.com/nar/article/51/D1/D957/6786204 ; https://gold.jgi.doe.gov/ecosystem_classification |
| Insect as multi-compartment habitat (exoskeleton, gut, hemocoel, cells) | Douglas 2015, *Annu Rev Entomol* 60:17–34, doi:10.1146/annurev-ento-010814-020822, PMID 25341109 — https://pmc.ncbi.nlm.nih.gov/articles/PMC4465791/ |
| Gut physicochemistry, pH 11–12, molting/peritrophic-matrix barriers, low diversity vs mammals | Engel & Moran 2013, *FEMS Microbiol Rev* 37(5):699–735, doi:10.1111/1574-6976.12025 — https://academic.oup.com/femsre/article/37/5/699/542120 |
| Termite gut O₂/pH gradients; alkaline soil-feeder hindgut | Brune, Emerson & Breznak 1995, *AEM* 61:2681–2687; Brune & Kühl 1996, *J Insect Physiol* 42:1121–1127; Brune 2014, *Nat Rev Microbiol* 12:168–180, doi:10.1038/nrmicro3182 — https://www.nature.com/articles/nrmicro3182 |
| Bacteriocytes; *Buchnera* genome reduction | Kim, Weiss & Fukatsu 2024, *Annu Rev Entomol*, doi:10.1146/annurev-ento-010323-124159 ; Chong et al. 2024, *Sci Data* — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11193766/ |
| Cuticular symbiont-housing organs | Kaltenpoth et al. 2012 — https://pmc.ncbi.nlm.nih.gov/articles/PMC3264120/ ; Li et al. 2018, *PNAS* 115:10720, doi:10.1073/pnas.1809332115 ; Flórez et al. 2022, *ISME J* 16:2691, doi:10.1038/s41396-022-01311-x |
| Honey bee ~9 core phylotypes | Kwong & Moran 2016, *Nat Rev Microbiol* 14(6):374–384, doi:10.1038/nrmicro.2016.43 |
| Caterpillars lack resident gut microbiome | Hammer et al. 2017, *PNAS* 114(36):9641–9646, doi:10.1073/pnas.1707186114, PMID 28830993 |
| Insect species counts | Stork 2018, *Annu Rev Entomol* 63:31–45, doi:10.1146/annurev-ento-020117-043348, PMID 28938083 |
| Endosymbiont incidence 52% / 24% / 13% | Weinert et al. 2015, *Proc R Soc B* 282(1807):20150249, doi:10.1098/rspb.2015.0249 |
| `host_taxid`, `host_body_site` slots; host-associated extension scope | GSC MIxS extension `HostAssociated` (0016002) — https://genomicsstandardsconsortium.github.io/mixs/0016002/ ; symbiont-associated extension: MIxS-SA, PMC9723553 |
| ENVO class definitions, parentage, absence of an insect class | EMBL-EBI OLS4 API against the current ENVO release (queried 2026-08-17): `ENVO:01001000`, `01001001`, `01001002`, `01001041`, `01001055`, `01001176`, `01001179`, `01001187`, `2000006`, `01000576`, `02000004`, `01001636` — https://www.ebi.ac.uk/ols4/ontologies/envo |
| GOLD path inventory, counts, sibling categories | `data/raw/gold_ecosystem_paths.tsv` in this repo (87 paths, 3,292 organism assertions, 1,833 on the bare node) |

**Explicitly my inference, not sourced:** (a) that the physicochemical heterogeneity argues for host-clade rather than physicochemistry as the differentia; (b) that GOLD's "Arthropoda:" prefix is a grouping device rather than part of the denotation — inferred from the sibling category list (`Chelicerates`, `Crustaceans`, `Myriapoda`), not from GOLD documentation; (c) that `ENVO:01001055` is a defensible second parent — the subsumption follows from its stated definition, but ENVO has not asserted it.

## 5. Synonyms, and what not to conflate

**Names in real use for this concept:**
- *insect-associated environment* (proposed primary; matches ENVO's `X-associated environment` pattern)
- *insect-associated habitat*
- *Insecta-associated environment* (exact-synonym candidate)
- *insect host environment*, *insect host-associated environment*
- *insect microbiome habitat* / *the insect microbiome* — used in the literature as the community's name, not the place's; acceptable as a related synonym at most
- GOLD's own string: *Arthropoda: Insects* (record as the source label, not as a synonym of the ENVO class)
- *hexapod-associated environment* (broader reading; see §1)

**Commonly but wrongly treated as the same thing — do not conflate:**
1. **Insecta the taxon** (`NCBITaxon:50557`) — a class of organisms, not a place. Belongs in `relation: xref`.
2. **Insect nests and hives** — `ENVO:2000006` *nest of termite*, `ENVO:01000576` *apiary*, `ENVO:02000004` *nesting material*. GOLD puts these under `Environmental > Terrestrial > Nest`, a different top-level Ecosystem.
3. **Hive products as food or commodity** — honey, royal jelly, pollen stores. GOLD files these under the nest; FoodOn files insect food products (`FOODON:00001177`) under food. Neither is a host-associated environment.
4. **`ENVO:01001176` environment associated with an aquatic invertebrate** — often reached for as "the invertebrate one". It is neither broader nor narrower cleanly; it cross-cuts.
5. **Insect-vectored or insect-visited material** — nectar in the flower, dung, carrion. "Insect-associated" in ecology sometimes covers these; here it does not.
6. **Insect cell lines** — GOLD keeps these under `Cell Line` nodes (e.g. `Arthropoda: Chelicerates > Cell Line > ISE6`); a cultured cell line is a laboratory system, not the host.
7. **The insect gut specifically** — the most frequent conflation, because 742+203+… of the assertions are gut. The gut is a child concept that grounds to anatomy (per the parts-vs-whole rule); the parent node's own 1,833 assertions are precisely the ones that have *no* body site and cannot live on a gut term.
8. **Arthropoda broadly** — Crustaceans, Chelicerates and Myriapoda are separate GOLD categories and separate HabitatMech records.

## 6. Should this be a term at all? — Yes

This is a habitat, and the corpus's own rules say so directly. Per CLAUDE.md: "An organism acting as a host IS a habitat; the taxon term is not," and ENVO already models exactly this at plant-, animal- and fungi-associated environment. `NOT_APPLICABLE` is reserved for diseases, qualities, processes and procedures — an insect host is none of those, and `tests/test_decisions.py` would reject a `NOT_APPLICABLE` pointing at an organism term anyway.

Four positive checks:

- **It is a place a sample is taken from.** 3,292 GOLD organism isolations across 87 paths, 1,833 of them recorded at exactly this level of resolution. A concept that 1,833 isolates are annotated to is not a sampling artefact.
- **It is not a process, quality or disease.** Contrast `ENVO:01001636` *insect conservation process*, which is the only ENVO class that surfaces on an "insect" search and is precisely the sort of thing that would warrant declining.
- **The pattern already exists in ENVO one level up and one clade over.** `ENVO:01001179` *cnidarian-associated environment* is a direct child of the proposed genus with the identical definitional shape. This request asks for nothing new structurally.
- **Grounding to the genus would be wrong.** The existing curation note is right: grounding to `ENVO:01001002` would collapse insects, crustaceans, chelicerates, molluscs, sponges, birds, mammals and every other GOLD host category onto one record, destroying the distinction the source data is making. The record must keep its minted identity until ENVO mints the class.

**Recommended record shape** (consistent with the existing `curation/term_requests.tsv` row for this identifier, which already proposes label *insect-associated environment* under `ENVO:01001002`):

- `grounding_status: UNGROUNDED`, minted identity retained
- `parent_habitats`: `ENVO:01001002` (keep). `ENVO:01001000` is implied by it and redundant. Consider adding `ENVO:01001055` *environment associated with an animal part or small animal* — the subsumption holds on its stated definition, though ENVO has not asserted it.
- `relation: xref` → `NCBITaxon:50557` *Insecta*
- ENVO NTR: label *insect-associated environment*; definition as proposed above; genus `ENVO:01001002`; differentia referencing `NCBITaxon:50557`; cite Douglas 2015 and Engel & Moran 2013 as definition sources.

**Two things a curator should decide, not inherit from me:**
1. **Insecta vs Hexapoda.** I recommend defining on Insecta and adding *hexapod-associated environment* as a related synonym; GOLD does not disambiguate and nothing in the data forces the choice.
2. **Whether to file a family of clade terms at once.** Crustaceans (`habitatmech:GOLD.2959225799`, 598 assertions), Chelicerates and Myriapoda have the identical shape and the identical near-miss (`ENVO:01001176`). ENVO reviewers may prefer one issue proposing an *arthropod-associated environment* intermediate with four children over four unrelated requests — and if they do, that intermediate is a missing class this repo should note rather than work around. Per the standing rule in memory, each external ENVO submission needs its own explicit go-ahead.

---

**Sources:**
[Mukherjee et al. 2023, GOLD v.9, *NAR*](https://academic.oup.com/nar/article/51/D1/D957/6786204) · [GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification) · [Douglas 2015, *Annu Rev Entomol*](https://pmc.ncbi.nlm.nih.gov/articles/PMC4465791/) · [Engel & Moran 2013, *FEMS Microbiol Rev*](https://academic.oup.com/femsre/article/37/5/699/542120) · [Brune 2014, *Nat Rev Microbiol*](https://www.nature.com/articles/nrmicro3182) · [Brune et al. 1995, *AEM*](https://journals.asm.org/doi/10.1128/aem.61.7.2681-2687.1995) · [Kim, Weiss & Fukatsu 2024, *Annu Rev Entomol*](https://www.annualreviews.org/content/journals/10.1146/annurev-ento-010323-124159) · [Chong et al. 2024, *Sci Data*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11193766/) · [Kaltenpoth et al. 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3264120/) · [Li et al. 2018, *PNAS*](https://www.pnas.org/doi/10.1073/pnas.1809332115) · [Flórez et al. 2022, *ISME J*](https://www.nature.com/articles/s41396-022-01311-x) · [Kwong & Moran 2016, *Nat Rev Microbiol*](https://www.nature.com/articles/nrmicro.2016.43) · [Hammer et al. 2017, *PNAS*](https://www.pnas.org/doi/10.1073/pnas.1707186114) · [Stork 2018, *Annu Rev Entomol*](https://www.annualreviews.org/doi/10.1146/annurev-ento-020117-043348) · [Weinert et al. 2015, *Proc R Soc B*](https://royalsocietypublishing.org/doi/10.1098/rspb.2015.0249) · [GSC MIxS host-associated extension](https://genomicsstandardsconsortium.github.io/mixs/0016002/) · [MIxS-SA, PMC9723553](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9723553/) · [EMBL-EBI OLS4 (ENVO)](https://www.ebi.ac.uk/ols4/ontologies/envo) · [ENVO issue #802 "Termite gut"](https://github.com/EnvironmentOntology/envo/issues/802) · [ENVO on OBO Foundry](http://obofoundry.org/ontology/envo.html) · [Buttigieg et al. 2016, ENVO in 2016](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/) · [Buttigieg et al. 2013, *J Biomed Semantics*](https://link.springer.com/article/10.1186/2041-1480-4-43)

## Citations

1. https://academic.oup.com/nar/article/51/D1/D957/6786204
2. https://gold.jgi.doe.gov/ecosystem_classification
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC4465791/
4. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
5. https://github.com/EnvironmentOntology/envo/issues/802
6. https://academic.oup.com/femsre/article/37/5/699/542120
7. https://doi.org/10.1016/S0022-1910(96
8. https://journals.asm.org/doi/10.1128/aem.61.7.2681-2687.1995
9. https://www.nature.com/articles/nrmicro3182
10. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11193766/
11. https://www.annualreviews.org/content/journals/10.1146/annurev-ento-010323-124159
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC3264120/
13. https://www.pnas.org/doi/10.1073/pnas.1809332115
14. https://www.nature.com/articles/s41396-022-01311-x
15. https://www.nature.com/articles/nrmicro.2016.43
16. https://www.pnas.org/doi/10.1073/pnas.1707186114
17. https://www.annualreviews.org/doi/10.1146/annurev-ento-020117-043348
18. https://royalsocietypublishing.org/doi/10.1098/rspb.2015.0249
19. https://genomicsstandardsconsortium.github.io/mixs/0016002/
20. https://www.ebi.ac.uk/ols4/ontologies/envo
21. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9723553/
22. http://obofoundry.org/ontology/envo.html
23. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035502/
24. https://link.springer.com/article/10.1186/2041-1480-4-43