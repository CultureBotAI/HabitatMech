---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T01:07:25.562622'
end_time: '2026-08-18T01:16:31.299175'
duration_seconds: 545.74
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: tuberclar
  habitat_identifier: habitatmech:PREGO.c312b0d6fc
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'PREGO: tubercle'
  assertions: '11'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. EXACT-grounding
    sample (#69): BTO:0002173 ''tubercle'' matches the label exactly, but BTO defines
    it as the dorsal bosses on adult male Schistosoma. A tubercle as an isolation
    source is a tuberculous lesion; the two share a word and nothing else. The slice
    has no term for the lesion. (source concept habitatmech:PREGO.c312b0d6fc)'
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
  web_search_requests: 11
  num_turns: 30
  total_cost_usd: 2.984168
  session_id: fc70a709-d1ef-4abb-936c-32574614a322
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 20
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** tuberclar
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:PREGO.c312b0d6fc
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** PREGO: tubercle
- **Upstream assertion volume:** 11
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. EXACT-grounding sample (#69): BTO:0002173 'tubercle' matches the label exactly, but BTO defines it as the dorsal bosses on adult male Schistosoma. A tubercle as an isolation source is a tuberculous lesion; the two share a word and nothing else. The slice has no term for the lesion. (source concept habitatmech:PREGO.c312b0d6fc)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **tuberclar** as a microbial habitat, with citations.

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

# Novel-term research: `tuberclar` (habitatmech:PREGO.c312b0d6fc)

## Proposed definition

> A **granuloma** which walls off a focus of mycobacterial infection in host tissue, whose avascular, lipid-rich caseous core is hypoxic, and which is sampled directly as an isolation source for the infecting mycobacterium.

If the curator wants the definition to cover the non-caseating tuberculoid/leprosy sense as well, drop "caseous" and "hypoxic" — but see §5, that broadening is not what the attestation supports.

**Two things a curator should fix before writing anything, both independent of the definition:**

1. **The label `tuberclar` is a PREGO stemming artifact, not a name for anything.** The PREGO synonym string for `BTO:0002173` is `tuberclar|tubercle|tubercles` (`data/raw/prego_habitats.tsv:331`), and the same pattern appears in the neighbouring row for root nodule: `nodular|nodule|nodules|root nodular|root nodule|root tuberclar|root tubercle|root tubercles` (line 197) and for stem nodule: `stem nodular|stem nodule|stem nodules` (line 496). `-lar`/`-ar` there is the adjectival form the dictionary generates; it is the *first* token, so the seeder took it as the label. The root-nodule record hides this because it grounded and inherited BTO's label; this one is ungrounded, so the artifact surfaced. **The term should be labelled `tubercle`**, with `tuberclar` demoted to the source's string, not a synonym in real use.
2. **`assertion_count: 11` is weaker evidence than it looks** — see §6.2. All eleven taxa are "tubercle bacilli" by name.

---

## 1. What the concept denotes

**The reading the data means.** All eleven PREGO taxa on the record are members of the *Mycobacterium tuberculosis* complex or *M. leprae*: eight *M. canettii* CIPT strains, *M. tuberculosis* var. *bovis* AF2122/97, *M. leprae* TN, and *M. tuberculosis* H37Rv (`data/habitats/other/tuberclar.yaml:21-87`). That fixes the sense: **the tubercle of pathology — the nodular granulomatous lesion of tuberculosis** — and excludes every other reading of the word.

As a habitat, the thing a sample is taken from is a discrete, macroscopically visible nodule of host tissue, typically 1–20 mm, consisting of a rim of lymphocytes and fibroblasts around a cuff of epithelioid macrophages and Langhans giant cells, enclosing a core of **caseum**: soft, avascular, cheese-like necrotic debris derived from lysed lipid-laden macrophages. In tuberculosis "the granulomas formed are called tubercles" ([Britannica, *Tubercle (pathology)*](https://www.britannica.com/science/tubercle-pathology); [StatPearls, *Granuloma*, NBK554586](https://www.ncbi.nlm.nih.gov/books/NBK554586/)).

**This is genuinely sampled material, not an abstraction.** Two established sampling practices:

- **Veterinary.** Post-mortem inspection of cattle for tuberculosis-like lesions in cephalic, thoracic and mesenteric lymph nodes and lung, followed by **culture of *M. bovis* on primary isolation medium** from the excised lesion, is the WOAH/EU-mandated confirmatory step in bovine TB surveillance ([Merck Veterinary Manual, *Overview of Tuberculosis in Animals*](https://www.merckvetmanual.com/generalized-conditions/overview-of-tuberculosis-in-animals/overview-of-tuberculosis-in-animals); [Vet Res Commun 2025, PMID 40478354](https://pubmed.ncbi.nlm.nih.gov/40478354/); [Front Vet Sci qPCR-on-lymph-node validation, PMC8109245](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8109245/)).
- **Human.** Surgically resected lung tissue is dissected into *uninvolved lung, necrotic nodule, closed-nodule caseum, cavity caseum, cavity wall and fibrotic tissue*, each assayed separately for drug concentration and bacillary burden (trial NCT00816426, described in [Sarathy & Dartois, *Clin Microbiol Rev* 33:e00159-19, 2020, PMID 32238365](https://journals.asm.org/doi/full/10.1128/cmr.00159-19)).

**Boundary — inside the concept:** the whole walled-off lesion including its caseous core and cellular cuff; equally the tuberculous lymph-node lesion, the pulmonary nodule, and the Ghon focus.

**Boundary — neighbouring concepts, outside it:**

| Neighbour | Why it is outside |
|---|---|
| **Cavity / cavity wall** | A tubercle that has liquefied and drained into an airway. Physicochemically the opposite: oxygen-rich at the surface, bacillary load 10⁷–10⁹ vs 10²–10⁴ in closed caseous lesions (Canetti & Grosset 1965, as reported in [Sarathy & Dartois 2020](https://journals.asm.org/doi/full/10.1128/cmr.00159-19)). Arguably a sibling term, not this one. |
| **Caseum** | The *material* filling the core; a part of the tubercle, not the tubercle. If the corpus wants a material-entity habitat, that is a separate, narrower term. |
| **Abscess** (`habitatmech:GOLD.5d784b0218`, `mesh:D000038`) | Neutrophil-rich liquefactive pus, no epithelioid-macrophage architecture. A sibling under *lesion*, not under *granuloma*. |
| **Tuberculoma** | A conglomerate caseous mass, chiefly intracranial, formed by coalescence of deep-seated tubercles ([Wikipedia, *Tuberculoma*](https://en.wikipedia.org/wiki/Tuberculoma)). Narrower/derived. |
| **Tuberculosis** (`MONDO:0018076`) | The disease. Not a place. |

**Ambiguity, stated rather than resolved silently.** The bare word `tubercle` has at least five unrelated senses, four of which are already in the vendored slice or in UBERON. They are listed in §2 as near-misses. **The one that could plausibly have been meant and is not** — the legume root nodule, called a "tubercle" in older literature — is ruled out by the data itself: PREGO carries it as a *separate* concept, `BTO:0001190` with 91 taxa and the explicit synonyms `root tuberclar|root tubercle|root tubercles` (`data/raw/prego_habitats.tsv:197`), already a distinct HabitatMech record at `data/habitats/host_associated/root_nodule.yaml`.

---

## 2. Genus — the broader kind

**The genus is *granuloma***: an organized, delimited aggregation of epithelioid macrophages formed by the host in response to a persistent stimulus.

**No term in ENVO, UBERON, FOODON, BTO or PO expresses it.** Verified:

- **ENVO has nothing.** An OLS4 search of ENVO for `granuloma` returns zero results; for `lesion`, `numFound: 0`. ENVO's host-associated branch stops at organism-scale environments (`ENVO:01001002` animal-associated environment, `ENVO:01001000` environmental system determined by an organism) and does not model pathological structures at all.
- **BTO has only the *cells*.** `BTO:0005835` *granuloma cell* and `BTO:0005834` *infectious granuloma cell* ("One due to a specific microorganism, as tubercle bacilli") are cell types — a different kind of entity, and narrower. Neither can serve as the genus of a lesion.
- **Outside the five preferred vocabularies** there are two adequate terms, neither in the vendored slice: `MPATH:847` *granuloma* ("Collection of epithelioid macrophages into a nodule") and `NCIT:C3064` *Granuloma*. `NCIT:C113731` *Non-Necrotizing Granuloma* is an explicit sibling of what we want.

**Recommended practical resolution — the genus already exists in this corpus.** `curation/term_requests/needs_a_parent_first.tsv:37` blocks this term for having "no ontology parent on the record, so there is no genus to write a definition from". But HabitatMech already mints **`habitatmech:GOLD.dacfc87fde` "Granuloma"** (`data/habitats/host_associated/granuloma.yaml`, UNGROUNDED, from GOLD path `Host-associated > Mammals: Human > Benign tumor > Granuloma`). That is the genus, and pointing `parent_habitats` at it unblocks this term without inventing an intermediate class. Two caveats the curator should record: it is itself UNGROUNDED and its own definition is unwritten; and GOLD files it under *Benign tumor*, which is wrong — a granuloma is an inflammatory lesion, not a neoplasm — so the parent path should not be inherited as a claim.

**Near-misses, and why each fails.** Recording these matters because four of them match the label exactly.

| Term | Definition | Why it fails |
|---|---|---|
| `BTO:0002173` **tubercle** | Dorsal bosses on adult male *Schistosoma*, tegument lifted by parenchymal cell extensions, actin spines for gripping mesenteric vein walls | Homonym. Normal helminth surface anatomy. Already recorded on the decision (#69). |
| `UBERON:0005813` **tubercle** | "A round nodule, small eminence, or warty outgrowth on an anatomical surface" | Homonym, and the most dangerous one — it is the generic *normal* anatomical protuberance, asserting no disease, no infection, no necrosis. Parenting here would say a tuberculous lesion is a normal surface eminence. |
| `PO:0025352` **tubercle** | "An enlarged leaf base (PO:0020040) that is fused with adjacent shoot axis tissue" | Homonym. Plant morphology. |
| `BTO:0001869` **olfactory tubercle**; also `UBERON:0002235` tubercle of rib, `UBERON:0005876` genital tubercle, `UBERON:2002124` nuptial tubercle | Named anatomical structures | Homonyms; all normal anatomy. |
| `BTO:0001190` **root nodule** (`root tuberclar` synonym) | Legume symbiotic organ | The other live reading of the word — excluded by PREGO carrying it separately (§1). |
| `NCIT:C3824` **Lesion** *(in slice)* | — | Correct but far too broad; skips the granuloma level entirely, so abscess, ulcer and tubercle all collapse to one parent. Usable only as a fallback. |
| `ENVO:01001002` **animal-associated environment** *(in slice)* | "An environmental system determined by an animal" | True but an ancestor several levels up, not a genus. Correct as the eventual ENVO anchor for the host-associated branch. |
| `MONDO:0018076` tuberculosis | The disease | Grounding a place to a disease is the exact over-claim the repo's rules forbid. |

---

## 3. Differentia — what distinguishes it from its siblings

Ordered by how directly observable each is. Each is a candidate clause; the proposed one-sentence definition uses only the first three.

**a. Architecture and formation process (distinguishes it from abscess).** Formed by the host walling off persistent mycobacterial antigen: activated macrophages transform into epithelioid cells and fuse into Langhans giant cells, lymphocytes surround the lesion, fibroblasts lay down a fibrous rim, and the centre undergoes caseous necrosis ([StatPearls, *Granuloma*](https://www.ncbi.nlm.nih.gov/books/NBK554586/); [Front Immunol 2022, *In the Thick of It*, PMC8934850](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8934850/)).

**b. Caseation and dominant material — lipid-rich necrotic debris (distinguishes it from non-caseating granulomas: sarcoidosis, tuberculoid leprosy, foreign-body).** Direct biochemical analysis of the lipid species in human caseum identified **cholesterol, cholesteryl esters, triacylglycerols and lactosylceramide**, most likely LDL-derived; lipid-metabolism proteins (adipophilin, ACSL1, saposin C) are disproportionately abundant in the cells surrounding the caseum ([Kim MJ et al., *EMBO Mol Med* 2:258–274, 2010; doi:10.1002/emmm.201000079; PMID 20597103](https://link.springer.com/article/10.1002/emmm.201000079)). Caseum "largely derives from necrotized, lipid-droplet-laden macrophages" ([Sarathy & Dartois 2020](https://journals.asm.org/doi/full/10.1128/cmr.00159-19)).

**c. Avascular and hypoxic (distinguishes it from a cavity, and from the perfused tissue around it).** Pimonidazole adducts — formed only under hypoxia — accumulate in discrete zones surrounding the necrotic and caseous regions of pulmonary granulomas in **guinea pigs, rabbits and non-human primates**, and are substantially reduced by housing animals under 95% O₂; direct pO₂ measurement in rabbit granulomas by fibre-optic probe corroborates this. The mouse is the notable exception ([Via LE et al., *Infect Immun* 76:2333–2340, 2008; doi:10.1128/IAI.01515-07; PMID 18347040](https://journals.asm.org/doi/full/10.1128/iai.01515-07)).

**d. pH — report, but do not put in the definition.** The sources disagree and the authors say so. Sarathy & Dartois state caseum pH "varies across lesions but remains near neutral overall" and that acidic conditions "may be only transient"; rabbit caseum pH *rises* from 6.4 to 7.4 as the lesion matures. A 2025 review reports human TB lung tissue reaching pH ≤5.5 in glycolytic, lactate-accumulating zones, and argues for pH zonation *within* single granulomas ([Krueger, Faisal & Dorhoi, *Front Immunol* 2025, doi:10.3389/fimmu.2025.1575133, PMID 40196129](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1575133/full)). **A pH clause in the definition would be an over-claim.**

**e. Microbial load — heterogeneous, and not safe to assert.** Cavity caseum excised from rabbit lung: 6×10⁵ to 3×10⁸ CFU/g, constant over 28 days ex vivo, indicating non-replication. But 20–30% of rabbit granulomas had no detectable CFU at 15–20 weeks, and in macaques 0–75% of lesions were sterile even in *active* disease ([Lin PL et al., *Nat Med* 20:75–79, 2014, "Sterilization of granulomas is common in active and latent tuberculosis"](https://pubmed.ncbi.nlm.nih.gov/24336248/); reviewed in [Sarathy & Dartois 2020](https://journals.asm.org/doi/full/10.1128/cmr.00159-19)). A [2024 Frontiers review](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1427559/full) states the central necrotic area of an intact human tubercle is "usually sterile or of low bacterial burden". Hence the definition says *sampled as an isolation source*, not *harbours a high burden*.

**f. Community composition — dominated by MTBC but not always monomicrobial.** 16S amplicon and metagenomic sequencing of caseous necrosis from surgically excised human TB foci supports **two terminal states**: "true" TB necrosis containing 99.9% tubercle bacilli, and a **polymicrobial community in which anaerobic lipophilic bacteria predominate over MTB**, corroborated by isolation and genomic characterization of *Corynebacterium* and *Staphylococcus* species from caseum ([Ogarkov O, Orlova E, Suzdalnitsky A, Mokrousov I. *Int J Mycobacteriol* 14(3):209–218, 2025; doi:10.4103/ijmy.ijmy_126_25; PMID 40953197](https://doi.org/10.4103/ijmy.ijmy_126_25)). This is the single most on-point evidence that the tubercle is being treated in the literature as a *habitat with a microbiota*, not merely as a lesion.

**g. Host range and anatomical site.** Human, cattle (*M. bovis*), and experimental guinea pig, rabbit, macaque and zebrafish models; predominantly lung and draining lymph nodes, with mesenteric nodes and liver in ingestion-route bovine disease (48.8% of lesions in lung/associated nodes, 29.3% in mesenteric nodes and liver in a 2023 Ethiopian abattoir series, [PMC12475847](https://pmc.ncbi.nlm.nih.gov/articles/PMC12475847/)).

---

## 4. Sources

Primary literature and reference works, with what each supports.

| Claim supported | Citation |
|---|---|
| Caseum defined; niche characterization; oxygen/pH; Canetti & Grosset 1965 burden gradient; human resection sampling protocol (NCT00816426) | Sarathy JP, Dartois V. **Caseum: a Niche for *Mycobacterium tuberculosis* Drug-Tolerant Persisters.** *Clin Microbiol Rev* 33(3):e00159-19, 2020. [doi:10.1128/CMR.00159-19](https://journals.asm.org/doi/full/10.1128/cmr.00159-19) · PMID 32238365 |
| Granulomas are hypoxic in guinea pig, rabbit, NHP; mouse exception | Via LE, Lin PL, Ray SM, et al. *Infect Immun* 76(6):2333–2340, 2008. [doi:10.1128/IAI.01515-07](https://journals.asm.org/doi/full/10.1128/iai.01515-07) · PMID 18347040 |
| Caseum lipid composition (cholesterol, cholesteryl esters, TAG, lactosylceramide); lipid-metabolism protein localization | Kim MJ, Wainwright HC, Locketz M, et al. *EMBO Mol Med* 2(7):258–274, 2010. [doi:10.1002/emmm.201000079](https://link.springer.com/article/10.1002/emmm.201000079) · PMID 20597103 |
| Tubercle/caseum as a habitat with a resolvable microbiota; two terminal states; *Corynebacterium*/*Staphylococcus* isolation | Ogarkov O, Orlova E, Suzdalnitsky A, Mokrousov I. *Int J Mycobacteriol* 14(3):209–218, 2025. [doi:10.4103/ijmy.ijmy_126_25](https://doi.org/10.4103/ijmy.ijmy_126_25) · PMID 40953197 |
| Granuloma zonation; pH heterogeneity; glycolysis/lactate acidification | Krueger J, Faisal S, Dorhoi A. **Microenvironments of tuberculous granuloma.** *Front Immunol* 2025. [doi:10.3389/fimmu.2025.1575133](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1575133/full) · PMID 40196129 |
| Granuloma development across species; central necrotic area usually sterile/low burden | **Understanding the development of tuberculous granulomas.** *Front Immunol* 2024. [doi:10.3389/fimmu.2024.1427559](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1427559/full) |
| Sterile granulomas common in active and latent TB | Lin PL, Ford CB, Coleman MT, et al. *Nat Med* 20(1):75–79, 2014. [PMID 24336248](https://pubmed.ncbi.nlm.nih.gov/24336248/) |
| "In tuberculosis the granulomas formed are called tubercles" | [*Encyclopædia Britannica*, "Tubercle (pathology)"](https://www.britannica.com/science/tubercle-pathology) |
| Granuloma histology; caseating vs non-caseating; sarcoid and fungal differential | Shah KK, Pritt BS, Alexander MP. **Granuloma.** *StatPearls* / NCBI Bookshelf [NBK554586](https://www.ncbi.nlm.nih.gov/books/NBK554586/) |
| Granuloma formation, Ghon focus/complex, miliary and cavitary progression | Ehlers S, Schaible UE and successors; see [*In the Thick of It*, *Front Immunol* 13:820134, 2022, PMC8934850](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8934850/) |
| Tubercles as the sampled, cultured material in bovine TB surveillance | [Merck Veterinary Manual, *Overview of Tuberculosis in Animals*](https://www.merckvetmanual.com/generalized-conditions/overview-of-tuberculosis-in-animals/overview-of-tuberculosis-in-animals); [*Vet Res Commun* 2025, PMID 40478354](https://pubmed.ncbi.nlm.nih.gov/40478354/); [IS6110 qPCR on bovine lymph nodes, PMC8109245](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8109245/); [Ethiopian abattoir series 2023, PMC12475847](https://pmc.ncbi.nlm.nih.gov/articles/PMC12475847/) |
| *M. canettii* CIPT strains = "smooth tubercle bacilli", isolated from human TB patients | Supply P, Marceau M, Mangenot S, et al. **Genomic analysis of smooth tubercle bacilli.** *Nat Genet* 45:172–179, 2013. [PMID 23291586](https://pubmed.ncbi.nlm.nih.gov/23291586/) |
| "Tubercular leprosy" = nodular/lepromatous in older usage; "tuberculoid" = TB-like non-caseating granuloma | [MeSH *Leprosy, Lepromatous* (concept terms include "Leprosy, Nodular")](https://www.ncbi.nlm.nih.gov/mesh); [MSD Manual, *Leprosy*](https://www.msdmanuals.com/professional/infectious-diseases/mycobacteria/leprosy); [Wikipedia, *Tuberculoid leprosy*](https://en.wikipedia.org/wiki/Tuberculoid_leprosy) |
| PREGO methodology: text-mined co-mentions plus metadata co-occurrence, scored | Zafeiropoulos H, Paragkamian S, Ninidakis S, Pavlopoulos GA, Jensen LJ, Pafilis E. *Microorganisms* 10:293, 2022. [doi:10.3390/microorganisms10020293](https://www.mdpi.com/2076-2607/10/2/293) · PMID 35208748 |

**Explicitly my inference, not any source's statement:**

- That `tuberclar` is a PREGO dictionary stemming artifact. No source says this; it is inferred from the three PREGO rows quoted in the header of this report (`prego_habitats.tsv` lines 197, 331, 496), where `-lar`/`-ar` variants appear systematically alongside `nodule`/`nodules`. I consider this near-certain but it is a reading of the data file, not a citation.
- That the eleven-taxon attestation may be a lexical match on "tubercle bacill*" rather than eleven isolations from tubercles (§6.2). PREGO's published method makes it possible; nothing states it happened here.
- The mapping of near-miss terms to *why each fails* — the terms and their definitions are quoted from OLS4/the vendored slice, but the judgement of failure is mine.
- That `habitatmech:GOLD.dacfc87fde` "Granuloma" is the right parent. That is a curation recommendation, not a published fact.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept:**

- **tubercle** (the primary label to use)
- **tuberculous granuloma**
- **caseating granuloma** (near-synonymous in the TB context; strictly a slightly broader class — fungal granulomas also caseate)
- **tuberculous lesion**, **TB-like lesion**, **tuberculosis-like lesion** (veterinary post-mortem usage)
- **necrotic granuloma**, **closed nodule** (Dartois-lab lesion taxonomy)
- **Ghon focus** (the specific primary pulmonary tubercle)

**Commonly but wrongly treated as the same thing:**

| Confused with | Why it is different |
|---|---|
| **`UBERON:0005813` tubercle / rib, genital, olfactory, nuptial tubercles** | Normal anatomical protuberances. Pure homonymy. This is the highest-risk conflation because the label match is exact and the ontology is a preferred one. |
| **`BTO:0002173` tubercle** | *Schistosoma* dorsal boss. Pure homonymy. |
| **`PO:0025352` tubercle** | Enlarged, fused leaf base. Pure homonymy. |
| **Root nodule / "root tubercle"** (`BTO:0001190`) | A plant symbiotic organ housing rhizobia. Opposite sign — mutualism, not walled-off infection. PREGO keeps them separate; so must we. |
| **Tuberculosis** (`MONDO:0018076`) | The disease. A tubercle is where microbes live; tuberculosis is what happens to the host. |
| **Tuberculin / tubercle bacillus** | A reagent and an organism respectively. "Tubercle bacillus" is the source of the false-friend risk in §6.2. |
| **Abscess** (`mesh:D000038`) | Neutrophilic, liquefactive, pus-filled. Different formation process, different physicochemistry, sibling not synonym. |
| **Sarcoid granuloma, foreign-body granuloma** | Non-caseating and typically sterile — no microbial inhabitant, so not this habitat at all. StatPearls stresses that microbiological confirmation is required precisely because these look alike. |
| **Tuberculoid leprosy lesion** | Confusingly named: modern "tuberculoid" leprosy is the *paucibacillary*, non-caseating pole with *M. leprae* absent or scanty. Meanwhile pre-1960s "**tubercular leprosy**" (skin nodules literally called tubercles) corresponds to modern **lepromatous** leprosy. Given *M. leprae* TN is among the eleven attested taxa, the curator should decide explicitly whether leprosy nodules are in scope — my recommendation is **no**, and to say so in the notes, because the caseation and hypoxia differentiae do not hold for them. |
| **Cavity / cavity wall**, **caseum**, **tuberculoma** | Adjacent lesion types and a part; sibling or child terms, not synonyms (§1). |

---

## 6. Should it be a term at all?

**Yes — but with a scope and evidence caveat that belongs in the note.**

### 6.1 It is a habitat, not a disease, quality or process

A tubercle is a **physical, delimited, sampleable structure**: it is excised at abattoir inspection and cultured, it is dissected out of resected human lung and assayed, and its resident bacterial community has been characterized by 16S and metagenomic sequencing. That satisfies the repo's own line — a place a microbe lives — as squarely as `abscess` (already a NARROW-grounded record) or the existing `Granuloma` record. It is **not** in the class this corpus dispositions as `NOT_APPLICABLE`: it is not the disease (`tuberculosis` is), not a quality, not a process, not a taxon.

The `HOST_ASSOCIATED` category fits better than the current `OTHER`; the concept is defined by being inside animal tissue, and the existing sibling `Granuloma` record is already `HOST_ASSOCIATED`.

### 6.2 The evidence caveat a curator must not skip

**All eleven attested taxa are organisms whose common name contains the word "tubercle."** Eight are *M. canettii* CIPT strains — universally called the **"smooth tubercle bacilli"** in the literature that describes them ([Supply et al., *Nat Genet* 2013](https://pubmed.ncbi.nlm.nih.gov/23291586/)) — plus *M. tuberculosis* H37Rv, *M. bovis* AF2122/97 and *M. leprae* TN, all "tubercle bacilli". PREGO builds associations by *co-mention in text and co-occurrence in metadata*, scored for confidence ([Zafeiropoulos et al. 2022](https://www.mdpi.com/2076-2607/10/2/293)), and the evidence channel here is `annotated_genomes_isolates` with `score: 3.0`.

The *M. canettii* CIPT strains were in fact isolated from **lymph node aspirates and sputum** of TB patients, not from excised tubercles. So there is a live possibility that this concept's eleven "attestations" reflect a dictionary hit on **"tubercle bacillus"** in genome/isolate annotation rather than eleven records of a tubercle as isolation source.

This does not make the concept unreal — §1's veterinary and surgical sampling literature independently establishes that tubercles *are* an isolation source. It means:

- The **upstream assertion volume of 11 should not be cited in the note as evidence of sampling frequency.**
- The eleven taxa should **not** be written into the record as `characteristic_taxa` evidence of community composition without this caveat. The genuine community evidence is Ogarkov et al. 2025, not the PREGO taxon list.

### 6.3 Recommended disposition

1. **Relabel** to `tubercle`; retain `tuberculous granuloma` and `tuberculous lesion` as exact synonyms; drop `tuberclar` or mark it as a source string.
2. **Recategorize** `OTHER` → `HOST_ASSOCIATED`.
3. **Parent:** `habitatmech:GOLD.dacfc87fde` (Granuloma) as `relation: parent` — genuinely broader, so the `parent_habitats` bar is met. This clears line 37 of `needs_a_parent_first.tsv`.
4. **Xrefs, not parents:** `BTO:0002173` as `relation: xref` (the link upstream saw, without asserting the *Schistosoma* sense); optionally `MPATH:847` and `NCIT:C3064` as the nearest external granuloma terms, noting neither is in the vendored slice — if either is wanted as a grounding target, the ontology must be vendored first (#10), not the check weakened.
5. **Keep `CONFIRM_UNGROUNDED`** and promote to a **term request** — the existing decision and its reasoning stand; what changes is that a genus and a defensible definition now exist.
6. If the curator wants finer resolution later, `cavity caseum` and `closed-nodule caseum` are well-attested children with distinct physicochemistry (oxygen, bacillary load) and distinct sampling protocols.

## Citations

1. https://www.britannica.com/science/tubercle-pathology
2. https://www.ncbi.nlm.nih.gov/books/NBK554586/
3. https://www.merckvetmanual.com/generalized-conditions/overview-of-tuberculosis-in-animals/overview-of-tuberculosis-in-animals
4. https://pubmed.ncbi.nlm.nih.gov/40478354/
5. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8109245/
6. https://journals.asm.org/doi/full/10.1128/cmr.00159-19
7. https://en.wikipedia.org/wiki/Tuberculoma
8. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8934850/
9. https://link.springer.com/article/10.1002/emmm.201000079
10. https://journals.asm.org/doi/full/10.1128/iai.01515-07
11. https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1575133/full
12. https://pubmed.ncbi.nlm.nih.gov/24336248/
13. https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1427559/full
14. https://doi.org/10.4103/ijmy.ijmy_126_25
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC12475847/
16. https://pubmed.ncbi.nlm.nih.gov/23291586/
17. https://www.ncbi.nlm.nih.gov/mesh
18. https://www.msdmanuals.com/professional/infectious-diseases/mycobacteria/leprosy
19. https://en.wikipedia.org/wiki/Tuberculoid_leprosy
20. https://www.mdpi.com/2076-2607/10/2/293