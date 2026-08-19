---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T22:42:57.535384'
end_time: '2026-08-17T22:53:39.909176'
duration_seconds: 642.37
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Root-Tooth
  habitat_identifier: habitatmech:BACDIVE.5bac6e6496
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Root-Tooth'
  assertions: '28'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Cohort
    review: NCIT:C33446 ''Root'' is unqualified and reads as a plant root, not the
    root of a tooth. The slice has no tooth-root term. Real habitat, no term. (source
    concept habitatmech:BACDIVE.5bac6e6496)'
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
  web_search_requests: 18
  num_turns: 36
  total_cost_usd: 4.0687630000000015
  session_id: 513283d5-df73-4fd0-b983-3723b017821c
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 27
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Root-Tooth
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.5bac6e6496
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Root-Tooth
- **Upstream assertion volume:** 28
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Cohort review: NCIT:C33446 'Root' is unqualified and reads as a plant root, not the root of a tooth. The slice has no tooth-root term. Real habitat, no term. (source concept habitatmech:BACDIVE.5bac6e6496)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Root-Tooth** as a microbial habitat, with citations.

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

# Root‑Tooth (`habitatmech:BACDIVE.5bac6e6496`) — definition research

> **Proposed definition:** *A part of a calcareous tooth which extends apically from the cementoenamel junction, is covered by cementum and seated in the alveolar socket, and encloses the root canal system — colonized by oral micro-organisms on its external cemental/radicular-dentine surface and, when the pulp is necrotic or removed, within its canal lumen.*

**Headline recommendation, before the supporting sections:** this concept is **not** a genuine novel term. `UBERON:0003677` *tooth root* names it exactly, with a definition that matches BacDive's usage; it is simply **absent from the vendored slice** (`data/raw/ontology_terms.tsv` carries 680 UBERON terms, including `UBERON:0001091` *calcareous tooth*, `UBERON:0001751` *dentine* and `UBERON:0001828` *gingiva*, but no tooth-root term). Per the repo's own rule that **a host's parts ground to the anatomy term**, the correct disposition is `GROUND` → `UBERON:0003677` *tooth root* once the slice is extended (issue #10), not a HabitatMech-minted term. The existing `CONFIRM_UNGROUNDED` note is accurate about the *slice* ("The slice has no tooth-root term") but its conclusion — "Real habitat, no term" — is wrong about the *ontology*: the term exists.

---

## 1. What the concept denotes

### 1.1 The source concept, resolved

The BacDive vocabulary string is not "Root-Tooth" as a compound; it is **`Root (Tooth)`**, a Category-3 (Cat3) term under Category-2 **`Oral cavity and airways`**, itself under Category-1 **`Host Body-Site`**. This was verified two ways:

- BacDive's isolation-source browser lists `Root (Tooth)` and `Root (Rhizome)` as two *separate* Cat3 terms, alongside `Tooth`, `Dental plaque`, `Subgingival plaque`, `Periodontal pocket`, `Gingiva`, `Mouth`, `Saliva`, `Throat` ([bacdive.dsmz.de/isolation-sources](https://bacdive.dsmz.de/isolation-sources), accessed 2026-08-17).
- A strain in the category: *Prevotella dentalis* ES2772<sup>T</sup> (DSM 3688), free-text isolation source **"human dental root canal"**, Helsinki, Finland; BacDive records Host = Human, Host Body-Site = **Oral cavity and airways / Root (Tooth)** ([BacDive 139763](https://bacdive.dsmz.de/strain/139763)). That strain is the type strain of *Mitsuokella dentalis* Haapasalo et al. 1986, described **"from dental root canals"** ([Int J Syst Bacteriol 36:566–568, 1986](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-36-4-566)), reclassified as *Prevotella dentalis* by [Willems & Collins 1995, IJSB 45:832–836](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-45-4-832).

The record's own `characteristic_taxa` corroborate the reading unambiguously — *Campylobacter rectus*, *C. curvus*, *C. showae*, *C. gracilis*, *Actinomyces israelii*, *A. viscosus*, *Aggregatibacter actinomycetemcomitans*, *A. aphrophilus*, *Prevotella dentalis*, *Capnocytophaga* sp., *Streptococcus infantis/peroris* — the canonical endodontic-plus-subgingival assemblage. Nothing in the taxon list is soil-, rhizosphere- or plant-associated.

### 1.2 The physical place, as sampled

The **root of a tooth**: the portion of the tooth apical to the cementoenamel junction (CEJ), covered by cementum rather than enamel, held in the alveolar socket by the periodontal ligament, and containing the root canal(s) that open at the apical foramen ([StatPearls, *Anatomy, Head and Neck, Teeth*, NBK557543](https://www.ncbi.nlm.nih.gov/books/NBK557543/); [StatPearls, *Histology, Periodontium*, NBK570604](https://www.ncbi.nlm.nih.gov/books/NBK570604/)).

As a **microbial habitat** the term covers two anatomically continuous but physicochemically opposite compartments — and BacDive's free text shows samples of both kinds:

| Compartment | What is sampled | Typical study context |
|---|---|---|
| **Internal — root canal system** (canal lumen, radicular dentine, dentinal tubules, apical ramifications) | necrotic pulp tissue, canal exudate, cryopulverized apical root segments from extracted teeth or root-end resections | endodontic infection, primary and post-treatment apical periodontitis ([Siqueira et al. 2024, *Int Endod J*](https://onlinelibrary.wiley.com/doi/10.1111/iej.14071), PMID [38634795](https://pubmed.ncbi.nlm.nih.gov/38634795/)) |
| **External — root surface** (cementum, exposed radicular dentine, subgingival root face) | biofilm/hard-tissue shavings from the root surface, root-caries lesions, root planing debris | root caries, periodontitis-associated root colonization ([Gondo et al. 2024, *BMC Oral Health* 24:869](https://link.springer.com/article/10.1186/s12903-024-04670-3)) |

### 1.3 The boundary — what is inside and what is next door

**Inside:** the root as a solid anatomical part and both of its colonizable surfaces (cemental/radicular-dentine exterior; canal lumen and tubule interior), in humans and in other mammals.

**Outside (neighbouring BacDive Cat3 concepts, kept separate upstream):**

- `Tooth` — the whole tooth, crown included. BacDive assigns strains here independently: *Actinomyces radicidentis* AO 96-06841 (free text "infected human tooth root") is recorded under body-site **Tooth**, not `Root (Tooth)` ([BacDive 176](https://bacdive.dsmz.de/strain/176)) — so the two categories are neither disjoint in practice nor interchangeable in principle.
- `Dental plaque` / `Subgingival plaque` — a biofilm *material* accumulated on a surface, not the surface itself.
- `Periodontal pocket` — the pathologically deepened gingival sulcus, i.e. a space bounded by soft tissue *and* the root; the type strain of *Campylobacter rectus* (DSM 3260) is recorded from a **human periodontal pocket**, a different category ([DSMZ DSM-3260](https://www.dsmz.de/collection/catalogue/details/culture/DSM-3260)).
- `Gingiva`, `Saliva`, `Mouth` — other oral sites.
- Periapical/periradicular tissue, alveolar bone, periodontal ligament — outside the tooth.
- `Root (Rhizome)`, `Rhizoplane`, `Rhizosphere`, `Root nodule` — the *plant* readings, held in the same vocabulary under different Cat3 terms.

### 1.4 Ambiguity, stated rather than resolved silently

The label **"Root"** alone is genuinely ambiguous (plant root vs. tooth root) — which is why the upstream lexical mapping to `NCIT:C33446` *Root* was rejected, correctly. Once disambiguated by BacDive's own parenthetical and Cat2 parent, **the tooth reading is the only one the data supports**. There is a residual, narrower ambiguity *within* the tooth reading — canal interior vs. root exterior — which the anatomical term subsumes and which BacDive does not distinguish.

**Two data caveats a curator should carry forward, stated as caveats not facts:**

1. **Host is not only human.** Five of the 28 strains are *Streptococcus devriesei*, described "from equine teeth" ([Collins et al. 2004, *Syst Appl Microbiol* 27:146–150](https://pubmed.ncbi.nlm.nih.gov/15046302/)); the Swedish source material is equine caries of the maxillary P2 ([Lundström et al. 2007, *Acta Vet Scand* 49:10](https://actavetscand.biomedcentral.com/articles/10.1186/1751-0147-49-10)). The *S. devriesei* type strain's own BacDive body-site reads **Oral cavity and airways / Tooth** ([BacDive 14834](https://bacdive.dsmz.de/strain/14834)), and equine *infundibular* caries is a crown lesion, not a root lesion. I could not check all 28 strain records individually (BacDive's per-category strain list needs the API/SPARQL endpoint), so **some category noise is likely** — the definition should describe the root, and the record should not be read as asserting that every one of the 28 strains came from a root. *This is my inference from three strain pages, not a statement any source makes.*
2. **Most strains come from diseased roots.** BacDive cross-classifies many of these under Cat1 `Infection` / Cat2 `Disease` (as it does for *A. radicidentis*). The habitat is the root; the infection is a state of it. Do not let the disease framing migrate into the definition — that would repeat the over-claim pattern of #99.

---

## 2. Genus — the broader kind

### 2.1 The match (not a near-miss)

**`UBERON:0003677` — *tooth root***
> "The part of a tooth that is implanted in the gum; the root is normally located below the neck of the tooth, covered by cementum rather than enamel, and attached by the periodontal ligament to the alveolar bone."
> Synonyms: *root of tooth*, *radix corona*. Parent: `UBERON:0000063` *organ subunit*. `part_of` `UBERON:0001091` *calcareous tooth*.
> Source: [OLS4 / UBERON](https://www.ebi.ac.uk/ols4/ontologies/uberon), retrieved 2026-08-17.

This is a multi-species anatomy term (it applies to the horse strains as well as the human ones), and it is the ontology MIxS names for `host_body_site` (MIXS:0000867, "expected value: FMA or UBERON") — [GSC MIxS host-associated extension](https://genomicsstandardsconsortium.github.io/mixs/0016002/). If HabitatMech grounds tooth-root samples anywhere, this is the term.

**Genus for the definition sentence:** *part of a calcareous tooth* (`UBERON:0001091`, already in the slice) — which is precisely `UBERON:0003677`'s own asserted parentage.

If instead the curator wants an ENVO-pattern environment term (`<X>-associated environment`), the sentence would be *"An animal-associated environment (`ENVO:01001002`) which is determined by the root of a tooth …"* — but that pattern is for **whole host organisms**, and the tooth root is a **part**, so the anatomy grounding is the one this repo's rule prescribes.

### 2.2 Near-misses, and why each fails

| Candidate | In slice? | Why it is not the match |
|---|---|---|
| `NCIT:C33446` *Root* (upstream `skos:closeMatch`, `ols4_auto`, medium confidence) | yes | Unqualified; no definition; reads as a plant root. Already rejected — correctly. |
| `UBERON:0001091` *calcareous tooth* | yes | **Broader.** Includes the crown; BacDive keeps `Tooth` as a separate Cat3 sibling with its own strains, so grounding here merges two upstream concepts. Fine as `parent_habitats`. |
| `BTO:0000397` *tooth* | yes | Same over-broadness, plus BTO is a tissue-source vocabulary with no multi-species commitment. |
| `BTO:0002525` *cementum* | yes | **Narrower.** One tissue on the root surface; excludes the canal lumen, radicular dentine and tubules — i.e. excludes exactly the compartment *P. dentalis* came from. |
| `BTO:0000339` *dental pulp* / `UBERON:0002487` *tooth cavity* | BTO yes, UBERON no | **Narrower and displaced.** Pulp is the soft tissue; *tooth cavity* is the whole pulp cavity including the coronal chamber. In endodontic infection the pulp is necrotic or absent — the habitat persists after the pulp does not. |
| `UBERON:0001751` *dentine* | yes | A tissue type spanning crown and root; not a site. |
| `BTO:0001021` *periodontium* / `BTO:0001020` *periodontal ligament* / `UBERON:0001828` *gingiva* | yes | Tissues **investing** the root, not the root. Grounding here asserts host-tissue provenance the sources do not claim. |
| `BTO:0000338` *dental plaque* | yes | A biofilm material; BacDive keeps `Dental plaque` and `Subgingival plaque` as separate Cat3 terms. |
| `mesh:D010514` *Periodontal Pocket* | yes | Sibling site, not this one. (Note `mesh:` **is** an accepted grounding prefix here — 9 decisions use it.) |
| `mesh:D014092` *Tooth Root* | **no** | Exists in MeSH ([id.nlm.nih.gov/mesh/D014092](https://id.nlm.nih.gov/mesh/D014092)) and would be a valid fallback grounding, but UBERON is the better target under MIxS. |
| **ENVO — anything oral** | — | ENVO has essentially no oral or dental site terms. An OLS4 search of ENVO for "oral" returns only `ENVO:03501185` *dental clinic*. `ENVO:01001002` *animal-associated environment* is the nearest ENVO ancestor and is many levels too broad. **ENVO does not cover this space at all.** |

---

## 3. Differentia — what distinguishes it from its siblings

Ordered from most to least directly observable; all four are measurable at the bench or chairside.

1. **Position and covering tissue.** The root lies **apical to the cementoenamel junction** and is covered by **cementum**, not enamel; the CEJ is the static anatomical landmark separating it from the crown, and the reference point from which probing depth and clinical attachment level are measured (StatPearls NBK557543; NBK573074).
2. **Normally not exposed to the oral cavity.** The root sits in the alveolar socket, ligament-attached, subgingival. It becomes a *surface* habitat only after gingival recession or periodontal attachment loss, and an *internal* habitat only when the pulp is necrotic or has been removed — "bacterial infection of the root canal system only occurs when the pulp is necrotic or was removed for previous treatment" ([Siqueira & Rôças 2022, *Int Endod J*, doi:10.1111/iej.13677](https://onlinelibrary.wiley.com/doi/10.1111/iej.13677)). This conditional accessibility is the single strongest differentia against `Tooth`, `Dental plaque` and `Gingiva`, all of which are continuously oral-exposed.
3. **Two contrasting physicochemical regimes within one structure.**
   - *Canal interior:* strongly reducing, low-Eh, anaerobic; nutrition dominated by peptides and amino acids from necrotic pulp tissue and periapical serum transudate rather than dietary carbohydrate, selecting asaccharolytic obligate anaerobes (*Porphyromonas*, *Prevotella*, *Fusobacterium*, *Peptostreptococcus*, *Actinomyces*) with facultative streptococci early in succession; the apical canal is the most nutrient-restricted, most anaerobic zone ([Siqueira & Rôças 2022](https://onlinelibrary.wiley.com/doi/10.1111/iej.13677); [Sundqvist & Figdor 2003, summarized in *Front Oral Health* 2021, doi:10.3389/froh.2021.672887](https://www.frontiersin.org/journals/oral-health/articles/10.3389/froh.2021.672887/full)).
   - *Root exterior:* a supra-/subgingival biofilm habitat on a **collagen-rich, ~50%-mineral substrate whose critical demineralization pH is ≈6.4, versus ≈5.5 for enamel** — so the root surface is lost to acid at pH values that leave enamel intact, and demineralized collagen then serves as a colonization scaffold ([*Microorganisms* 12(1):121, 2024, "The Evolving Microbiome of Dental Caries"](https://www.mdpi.com/2076-2607/12/1/121); [Gondo et al. 2024](https://link.springer.com/article/10.1186/s12903-024-04670-3)).
4. **A protected, instrument-inaccessible interior reservoir.** Radicular dentinal tubules and lacunar defects in cementum are invaded by a selected, Gram-positive-dominated subset of the oral flora (*Parvimonas micra*, *Streptococcus intermedius*, *Actinomyces naeslundii*, with fewer *P. gingivalis*, *P. intermedia*, *F. nucleatum*, *V. parvula*), shielded from scaling, irrigants and host defences, and act as reservoirs for recolonization after therapy ([Love & Jenkinson 2002, *Crit Rev Oral Biol Med* 13:171–183, doi:10.1177/154411130201300207](https://journals.sagepub.com/doi/10.1177/154411130201300207); [Adriaens et al. 1988, *J Periodontol* 59:493–503](https://pubmed.ncbi.nlm.nih.gov/3171862/)). No other oral BacDive site has this property.

**Why the site deserves its own identity at all:** oral microbes are largely **site specialists** — distinct oral sites host communities composed to a meaningful degree of different organisms, and at species-level resolution the specialization is the rule, not the exception ([Mark Welch, Dewhirst & Borisy 2019, *Annu Rev Microbiol* 73:335–358, doi:10.1146/annurev-micro-090817-062503](https://www.annualreviews.org/content/journals/10.1146/annurev-micro-090817-062503); PMID [31180804](https://pubmed.ncbi.nlm.nih.gov/31180804/)). Collapsing `Root (Tooth)` into `Tooth` would erase exactly the distinction that literature says is real.

---

## 4. Sources

**Anatomy / definitional**
- StatPearls, *Anatomy, Head and Neck, Teeth* (NBK557543) — https://www.ncbi.nlm.nih.gov/books/NBK557543/ (crown/root division, CEJ, cementum, apical foramen, root canal, alveolar process)
- StatPearls, *Anatomy, Head and Neck, Primary Dentition* (NBK573074) — https://www.ncbi.nlm.nih.gov/books/NBK573074/
- StatPearls, *Histology, Periodontium* (NBK570604) — https://www.ncbi.nlm.nih.gov/books/NBK570604/
- UBERON:0003677 *tooth root* — https://www.ebi.ac.uk/ols4/ontologies/uberon (retrieved 2026-08-17)
- MeSH D014092 *Tooth Root* — https://id.nlm.nih.gov/mesh/D014092

**Habitat / microbiology**
- Siqueira JF Jr & Rôças IN (2022) "Present status and future directions: Microbiology of endodontic infections." *Int Endod J* — doi:10.1111/iej.13677 — https://onlinelibrary.wiley.com/doi/10.1111/iej.13677
- Siqueira JF Jr, Silva WO, Romeiro K, Gominho LF, Alves FRF, Rôças IN (2024) "Apical root canal microbiome associated with primary and posttreatment apical periodontitis: A systematic review." *Int Endod J* — doi:10.1111/iej.14071 — PMID 38634795 — https://onlinelibrary.wiley.com/doi/10.1111/iej.14071 (literature searched to Aug 2023; 21 studies; apical root segments 2–7 mm from extracted teeth or root-end resection)
- Siqueira & Rôças group (2016) "Microbiome in the Apical Root Canal System of Teeth with Post-Treatment Apical Periodontitis." *PLOS ONE* — doi:10.1371/journal.pone.0162887 — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0162887 (11 phyla, 103 genera, 538 OTUs from cryopulverized apical root)
- *Front Oral Health* 2 (2021) "Microbiological Aspects of Root Canal Infections and Disinfection Strategies" — doi:10.3389/froh.2021.672887 — https://www.frontiersin.org/journals/oral-health/articles/10.3389/froh.2021.672887/full (open access; Eh, nutrition, succession)
- Love RM & Jenkinson HF (2002) "Invasion of Dentinal Tubules by Oral Bacteria." *Crit Rev Oral Biol Med* 13:171–183 — doi:10.1177/154411130201300207 — https://journals.sagepub.com/doi/10.1177/154411130201300207
- Adriaens PA, Edwards CA, De Boever JA, Loesche WJ (1988) "Ultrastructural observations on bacterial invasion in cementum and radicular dentin of periodontally diseased human teeth." *J Periodontol* 59:493–503 — PMID 3171862 — https://pubmed.ncbi.nlm.nih.gov/3171862/
- Gondo T et al. (2024) "Comparative analysis of microbiome in coronal and root caries." *BMC Oral Health* 24:869 — doi:10.1186/s12903-024-04670-3 — https://link.springer.com/article/10.1186/s12903-024-04670-3
- "The Evolving Microbiome of Dental Caries" (2024) *Microorganisms* 12(1):121 — https://www.mdpi.com/2076-2607/12/1/121 (root-caries microbiota; *Actinomyces* likely commensal rather than pathogen)
- Mark Welch JL, Dewhirst FE, Borisy GG (2019) "Biogeography of the Oral Microbiome: The Site-Specialist Hypothesis." *Annu Rev Microbiol* 73:335–358 — doi:10.1146/annurev-micro-090817-062503 — PMID 31180804
- *Dentiradicibacter hellwigii* gen. nov., sp. nov., isolated from a secondary infected root canal (2025) — PMC11881992 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11881992/ (evidence that the root canal remains an active source of novel cultured taxa)

**Strain-level provenance (BacDive / originating descriptions)**
- BacDive isolation-source browser — https://bacdive.dsmz.de/isolation-sources (Cat3 terms `Root (Tooth)`, `Root (Rhizome)`, `Tooth`, `Periodontal pocket`, `Subgingival plaque`)
- BacDive 139763, *Prevotella dentalis* ES2772<sup>T</sup> — https://bacdive.dsmz.de/strain/139763 ("human dental root canal"; body-site *Oral cavity and airways / Root (Tooth)*)
- Haapasalo M et al. (1986) "Mitsuokella dentalis sp. nov. from dental root canals." *Int J Syst Bacteriol* 36:566–568 — https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-36-4-566
- Willems A & Collins MD (1995) *Prevotella dentalis* comb. nov. *IJSB* 45:832–836 — https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-45-4-832
- BacDive 176, *Actinomyces radicidentis* AO 96-06841<sup>T</sup> — https://bacdive.dsmz.de/strain/176 ("infected human tooth root"; body-site *Tooth*)
- BacDive 14834 + Collins MD et al. (2004) "*Streptococcus devriesei* sp. nov., from equine teeth." *Syst Appl Microbiol* 27:146–150 — https://bacdive.dsmz.de/strain/14834 / https://pubmed.ncbi.nlm.nih.gov/15046302/
- Lundström T et al. (2007) "Caries in the infundibulum of the second upper premolar tooth in the horse." *Acta Vet Scand* 49:10 — https://actavetscand.biomedcentral.com/articles/10.1186/1751-0147-49-10
- DSMZ catalogue DSM 3260, *Campylobacter rectus* — https://www.dsmz.de/collection/catalogue/details/culture/DSM-3260 ("human periodontal pocket")

**Standards**
- GSC MIxS host-associated extension, `host_body_site` (MIXS:0000867), expected value FMA or UBERON — https://genomicsstandardsconsortium.github.io/mixs/0016002/

**Explicitly flagged as my inference, not sourced:** (a) that the 28 strains in `Root (Tooth)` include some equine crown-caries isolates and therefore carry category noise — based on three strain pages, not on a per-strain audit; (b) that the internal/external split is the salient habitat structure of this term — the literature describes both compartments separately, but I found no source that frames "the tooth root" as a single two-compartment habitat.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- *root of tooth*, *tooth root*, *dental root*, *radix dentis*, *radix corona* (UBERON synonym), *radicular* (adjectival: radicular dentine, radicular surface)
- Compartment-specific but within scope: *root canal*, *root canal system*, *intraradicular space*, *endodontium*, *apical root canal*, *root apex* / *apical segment* (as sampled in cryopulverization studies); *root surface*, *cemental surface*, *subgingival root surface*
- BacDive/UI form: `Root (Tooth)`, Cat2 `Oral cavity and airways`

**Commonly conflated but distinct**
| Not this | Why |
|---|---|
| **Plant root / rhizome / rhizoplane / rhizosphere / root nodule** | The other reading of "root"; BacDive's `Root (Rhizome)` is a separate Cat3 term. This is the failure mode `NCIT:C33446` walked into. |
| **Tooth (whole)** | Includes the enamel-covered crown; a separate BacDive category with its own strains. |
| **Dental plaque / subgingival plaque / dental calculus** | Biofilm or mineralized deposit *on* a surface, not the surface. |
| **Periodontal pocket, gingival crevice, gingival crevicular fluid** | Soft-tissue-bounded spaces adjacent to the root. |
| **Dental pulp** | The soft tissue occupying the canal; the root persists as a habitat once the pulp is necrotic or extirpated. |
| **Root caries, apical periodontitis, periapical abscess, endodontic infection** | Diseases and disease states of the site, not the site. Several source strains carry BacDive's `Infection / Disease` categories in parallel — do not import that into the definition. |
| **Root canal treatment / root planing / apicoectomy** | Clinical procedures. |
| **Periapical / periradicular tissue, alveolar bone, periodontal ligament, cementum** | Adjacent or constituent tissues; cementum is *part of* the root, not equivalent to it. |
| **"Root" in the sequence-analysis or hierarchy sense** | A namespace hazard when text-mining BacDive labels; unrelated. |

---

## 6. Should this be a term at all?

**Yes — it is a habitat, and specifically a body site.** It is a physical anatomical part with a definable boundary, from which samples are actually taken, hosting reproducible and site-characteristic microbial communities. It is not a disease, a process, a quality, or a taxon, so `NOT_APPLICABLE` would be wrong; and it is a **part** of a host, not a whole host organism, so the `<X>-associated environment` term-request pattern from #112/#114 does not apply here — the anatomy grounding does.

**But it should not be a HabitatMech-minted novel term.** Recommended disposition, in order of preference:

1. **Vendor `UBERON:0003677` *tooth root* into the slice and `GROUND` to it** (`GROUND | UBERON:0003677 | tooth root`). This is a slice-coverage gap of the kind issue #10 exists for, not an ontology gap. It also satisfies MIxS `host_body_site`, which expects UBERON/FMA.
2. If vendoring UBERON is blocked, `mesh:D014092` *Tooth Root* is a valid fallback — `mesh:` is already an accepted grounding prefix in this corpus (9 decisions) — though it is the weaker anatomy source.
3. Only if neither is available: keep the minted identifier with the definition proposed at the top, `parent_habitats: UBERON:0001091` *calcareous tooth* (`relation: parent` — the whole tooth is genuinely broader than its root, so this is a correct is-a-part-of-broader claim, not an over-claim), and record `UBERON:0003677` as an `xref` so the eventual grounding is one line away.

**Update the decision note either way.** The current note's premise ("The slice has no tooth-root term") is true; its conclusion ("Real habitat, no term") is not — the term exists in UBERON and in MeSH, and the record should say so.

## Citations

1. https://bacdive.dsmz.de/isolation-sources
2. https://bacdive.dsmz.de/strain/139763
3. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-36-4-566
4. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-45-4-832
5. https://www.ncbi.nlm.nih.gov/books/NBK557543/
6. https://www.ncbi.nlm.nih.gov/books/NBK570604/
7. https://onlinelibrary.wiley.com/doi/10.1111/iej.14071
8. https://pubmed.ncbi.nlm.nih.gov/38634795/
9. https://link.springer.com/article/10.1186/s12903-024-04670-3
10. https://bacdive.dsmz.de/strain/176
11. https://www.dsmz.de/collection/catalogue/details/culture/DSM-3260
12. https://pubmed.ncbi.nlm.nih.gov/15046302/
13. https://actavetscand.biomedcentral.com/articles/10.1186/1751-0147-49-10
14. https://bacdive.dsmz.de/strain/14834
15. https://www.ebi.ac.uk/ols4/ontologies/uberon
16. https://genomicsstandardsconsortium.github.io/mixs/0016002/
17. https://id.nlm.nih.gov/mesh/D014092
18. https://onlinelibrary.wiley.com/doi/10.1111/iej.13677
19. https://www.frontiersin.org/journals/oral-health/articles/10.3389/froh.2021.672887/full
20. https://www.mdpi.com/2076-2607/12/1/121
21. https://journals.sagepub.com/doi/10.1177/154411130201300207
22. https://pubmed.ncbi.nlm.nih.gov/3171862/
23. https://www.annualreviews.org/content/journals/10.1146/annurev-micro-090817-062503
24. https://pubmed.ncbi.nlm.nih.gov/31180804/
25. https://www.ncbi.nlm.nih.gov/books/NBK573074/
26. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0162887
27. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11881992/