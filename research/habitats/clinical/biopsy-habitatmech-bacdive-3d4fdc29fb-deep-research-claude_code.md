---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T20:44:04.803316'
end_time: '2026-08-17T20:50:42.780077'
duration_seconds: 397.98
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Biopsy
  habitat_identifier: habitatmech:BACDIVE.3d4fdc29fb
  habitat_category: CLINICAL
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Biopsy'
  assertions: '95'
  parent_terms: (none)
  xrefs: NCIT:C15189
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term NCIT:C15189 'Biopsy Procedure' attached as a parent. CLOSE-grounding\
    \ review (#12): the seeder made NCIT:C15189 'Biopsy Procedure' the identity of\
    \ BacDive's 'Biopsy' category, 95 strains. A procedure is not a habitat \u2014\
    \ it is the act of taking the sample, not the place the organism lived, the same\
    \ category error as grounding a record to an organism or a quality. The habitat\
    \ is whichever tissue was biopsied, which BacDive does not say, so no term fits.\
    \ The procedure term is kept as an xref (#99) to record what upstream matched\
    \ without this repo asserting the record is a procedure. The record was CLINICAL\
    \ while it carried the NCIT term and would fall to OTHER without one, because\
    \ the category is inferred from the grounding; a biopsy is a clinical source whether\
    \ or not a term fits, so the category is pinned rather than lost with the grounding.\
    \ (source concept habitatmech:BACDIVE.3d4fdc29fb)"
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
  num_turns: 28
  total_cost_usd: 2.529997
  session_id: 9b88d814-77d0-4370-a59b-59402f9859a2
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 19
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Biopsy
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.3d4fdc29fb
- **Category:** CLINICAL
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Biopsy
- **Upstream assertion volume:** 95
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** NCIT:C15189

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term NCIT:C15189 'Biopsy Procedure' attached as a parent. CLOSE-grounding review (#12): the seeder made NCIT:C15189 'Biopsy Procedure' the identity of BacDive's 'Biopsy' category, 95 strains. A procedure is not a habitat — it is the act of taking the sample, not the place the organism lived, the same category error as grounding a record to an organism or a quality. The habitat is whichever tissue was biopsied, which BacDive does not say, so no term fits. The procedure term is kept as an xref (#99) to record what upstream matched without this repo asserting the record is a procedure. The record was CLINICAL while it carried the NCIT term and would fall to OTHER without one, because the category is inferred from the grounding; a biopsy is a clinical source whether or not a term fits, so the category is pinned rather than lost with the grounding. (source concept habitatmech:BACDIVE.3d4fdc29fb)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Biopsy** as a microbial habitat, with citations.

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

I'll research this concept now.

# Research report — `habitatmech:BACDIVE.3d4fdc29fb` "Biopsy"

## Proposed definition

> An animal-associated environment which is the interior tissue of a living animal host at an anatomical site the source does not record.

**Caveat, stated up front:** that sentence is defensible but it is not a definition of *biopsy*. It is a definition of *unspecified host tissue*, and "biopsy" is the name of how the sample was obtained, not of the place. Nothing in the concept beyond "tissue interior of a living host" survives translation into habitat terms. My recommendation (§6) is that the existing `CONFIRM_UNGROUNDED` disposition is correct, that this concept should **not** become an ENVO/HabitatMech term request, and that the definition above should be recorded — if at all — as an explicitly underspecified placeholder, with the note saying so.

---

## 1. What the concept denotes

**As a habitat: the interior tissue of a living multicellular (in practice, human or other vertebrate) host, at whatever anatomical site the clinician sampled.** The label names the *procedure*; the place is the tissue.

The authoritative definitions all frame it as an act:

- **NCIT:C15189 "Biopsy Procedure"** — "The removal of tissue specimens or fluid from the living body for microscopic examination, performed to establish a diagnosis." ([NCI Thesaurus via OLS4](https://www.ebi.ac.uk/ols4/ontologies/ncit/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FNCIT_C15189))
- **OBI:0002650 "Biopsy"** — "A specimen collection that obtains a sample of tissue or cell from a living multicellular organism body for diagnostic purposes by means intended to be minimally invasive." ([OBI via OLS4](https://www.ebi.ac.uk/ols4/ontologies/obi/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0002650)) — OBI classifies it under *specimen collection*, i.e. a planned **process**, not a material entity.

Both are processes. Neither is a place. The curator's existing note is correct on this point and I found no source that contradicts it.

### What the BacDive data actually contains

The concept is not empty, though — the strain set has a clear centre of gravity. From this repo's own extraction (`data/raw/bacdive_source_taxa.tsv`, 95 strains / 73 taxa), the top attested taxa are:

| Rank | Taxon | Strains | Site a biopsy of this organism normally comes from |
|---|---|---|---|
| 1 | *Helicobacter pylori* (+ NCTC 11637) | 11 | gastric antral mucosa |
| 2 | *Eggerthella lenta* | 5 | gut / abscess tissue |
| 3 | *Granulicatella adiacens* | 4 | oral, endocardial |
| 4 | *Campylobacter concisus* | 3 | oral / intestinal mucosa |
| 5–8 | *Prevotella jejuni*, *Clostridium* sp., *Cutibacterium acnes*, *C. jejuni* subsp. *doylei* | 2 each | intestinal mucosa; skin/implant tissue |
| 11–25 | *Mycobacterium heckeshornense*, *M. arosiense*, *M. lentiflavum*, *M. decipiens*, *Nocardia kruczakiae/niwae/veterana*, *Kroppenstedtia pulmonis*, *Corynebacterium freneyi*, *Schaalia turicensis*, *Streptococcus gordonii*, *Limosilactobacillus gastricus*, *Lactobacillus kalixensis* | 1 each | lung, bone, skin, lymph node, gastric mucosa |

The dominant reading is **mucosal and deep-tissue sites of the human gastrointestinal, respiratory and integumentary systems**. Two entries are traceable to named biopsy studies:

- *H. pylori* was first cultured from antral **gastric biopsy specimens** taken at gastroscopy — 11 isolates from 100 consecutive patients (Marshall & Warren, *Lancet* 1984;323(8390):1311–15, [PMID 6145023](https://pubmed.ncbi.nlm.nih.gov/6145023/), [doi:10.1016/S0140-6736(84)91816-6](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(84)91816-6/fulltext)).
- *Limosilactobacillus gastricus* and *Lactobacillus kalixensis* were described from **human stomach mucosa biopsies** of healthy Swedish volunteers (Roos, Engstrand & Jonsson, *IJSEM* 2005;55:77–82, [doi:10.1099/ijs.0.63083-0](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.63083-0)).

### Boundary — what is inside and what is a neighbour

**Inside:** host tissue removed from a living body, of any organ, for diagnostic culture.

**Neighbouring concepts, outside:**
- **Body products** — blood, stool, sputum, urine, pus, synovial fluid. BacDive files these under `#Host body-product`; MIxS separates them as `host_body_product` (MIXS:0000888) from `host_body_site` (MIXS:0000867) ([GSC MIxS host-associated extension](https://genomicsstandardsconsortium.github.io/mixs/0016002/)).
- **Surface swabs** — a swab samples a surface film, not tissue. This is not a pedantic distinction: paired-sampling studies find tissue and swab cultures from the same joint give materially different results, and swabs are explicitly discouraged (Aggarwal et al., *Clin Orthop Relat Res* 2013, [PMID 23568679](https://pubmed.ncbi.nlm.nih.gov/23568679/)).
- **Post-mortem / surgical resection tissue** — same material, different procedure; BacDive tags these separately.
- **The named anatomical sites themselves** — `Lung`, `Bone`, `Liver`, `Lymph node` etc. are all separate BacDive category-3 tags. "Biopsy" is what is left when the site was *not* recorded, or was recorded only in the free text.

### Direct evidence that BacDive treats "Biopsy" as a facet, not a place

BacDive strain 154980 (*Mycobacterium setense* CCUG 55926), free text "human maxillary osseous biopsy", carries `Biopsy` **alongside** `Host Body-Site → Oral cavity and airways`, `Host Body-Site → Other (Bone)` and `Infection → Patient` ([BacDive strain 154980](https://bacdive.dsmz.de/strain/154980)). The site tag and the biopsy tag co-occur on one strain. That is one strain, not a survey — but it shows the tag is a collection-method facet layered over an independent site assertion, which is exactly why the category-level concept has no place of its own. BacDive's isolation-source vocabulary is hierarchical over three category levels under eight top-level classes (`#Environmental`, `#Engineered`, `#Host`, `#Host body-site`, `#Host body-product`, `#Medical`, `#Condition`, `#Climate`) — Reimer et al., *Nucleic Acids Res* 2019;47:D631–D636, [doi:10.1093/nar/gky879](https://academic.oup.com/nar/article/47/D1/D631/5106998); [BacDive isolation-source browser](https://bacdive.dsmz.de/isolation-sources).

---

## 2. Genus — the broader kind

**Smallest well-established kind: an environmental system determined by an animal — ENVO:01001002 "animal-associated environment"** ("An environmental system determined by an animal."), itself under **ENVO:01001000 "environmental system determined by an organism"** (related synonym: *host-associated environment*). ([ENVO via OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001002))

This is the genus I would build the definition from. It is broader than the concept, asserts only host-determination, and is the class ENVO already uses for host-as-habitat — consistent with this repo's rule that an organism acting as host is a habitat.

### Near-misses and why each fails

| Term | Why it is not a match |
|---|---|
| **NCIT:C15189 "Biopsy Procedure"** (current xref) | A process. Grounding to it asserts the record *is* the act of sampling. Correctly demoted to `xref`. ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/ncit/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FNCIT_C15189)) |
| **OBI:0002650 "Biopsy"** | Same failure, and explicit about it — OBI places it under *specimen collection*, a planned process. ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/obi/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0002650)) |
| **NCIT:C18202 "Biopsy Specimen"** — "A specimen obtained by biopsy, which is a process of removing tissue from living patients for diagnostic examination." | The *closest material-entity term that exists*, and still wrong for a habitat KB: a specimen is the excised sample in a tube, not the place the organism lived. Once tissue is a specimen the habitat has ended. Worth recording as a second xref if the repo wants the material-side link. ([NCIt](https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&code=C18202)) |
| **SNOMED CT 258415003 "Biopsy specimen"** | Same category as NCIT:C18202 — a specimen role, plus SNOMED is not in this repo's vendored slice. ([OLS4 search](https://www.ebi.ac.uk/ols4/search?q=biopsy%20specimen)) |
| **UBERON:0000479 "tissue"** — "Multicellular anatomical structure that consists of many cells of one or a few types, arranged in an extracellular matrix…" | *Broader* than the concept in one direction (any tissue of any multicellular organism, dead or alive, any sampling context) and it says nothing about a living host or a clinical setting. It is a legitimate **parent** candidate under the repo's parts-ground-normally rule, but not an identity: "Biopsy" ≠ "tissue". ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000479)) |
| **ENVO:01001055 "environment associated with an animal part or small animal"** | Reads as the right shape, but its asserted children are *environment associated with an aquatic invertebrate* (ENVO:01001176) and *human settlement* (ENVO:01001829) — the class is not being used for host-interior tissue environments, and "small animal" carries a size claim the sources do not make. Near-miss, not a match. |
| **ENVO clinical terms — ENVO:03501136 "clinical patient assessment facility", ENVO:03501183 "medical clinic", ENVO:03501158 "microbiology unit facility"** | All *built environments*: rooms and buildings. Grounding a tissue habitat to a facility asserts the microbe lived in a clinic. ENVO has **no** term for a clinical specimen or a biopsied tissue environment — a targeted OLS4 query for "biopsy" in ENVO returns **zero** hits. |

**No existing term expresses the concept.** The nearest ENVO class (ENVO:01001002) is several levels too broad; the terms that name "biopsy" are all processes or specimens.

---

## 3. Differentia — what distinguishes it from siblings

Under *animal-associated environment*, the properties that separate this concept from its siblings, ranked by how observable they are:

1. **Tissue interior rather than body product or surface.** The sample is solid host tissue with its extracellular matrix and epithelium intact, not a fluid, excretion, or surface film. This is the only differentia with real microbiological content, and it is measurable: mucosa-associated microbiota recovered from biopsies differ significantly in composition and function from luminal or faecal microbiota of the same gut — >30% of KEGG orthologues and >40% of pathways differ between biopsy and lavage samples, and mucosa-associated (but not luminal) composition discriminates IBS-D patients from controls (Vaga et al. review, *Biochem Soc Trans* 2022;50(5):1225–36, [doi:10.1042/BST20201201](https://portlandpress.com/biochemsoctrans/article/50/5/1225/231920/Relationship-between-mucosa-associated-gut); [Nature Sci Rep 2022 sampling comparison](https://www.nature.com/articles/s41598-022-05936-y)). A biopsy habitat is therefore genuinely not the same environment as a stool habitat, even from the same organ.
2. **Living host at the time of sampling.** Both NCIT:C15189 and OBI:0002650 stipulate a living body, which excludes post-mortem and food-animal carcass tissue.
3. **Normally low-biomass or sterile-presumed sites.** Deep tissue (bone, lung, lymph node, tumour) supports orders of magnitude less biomass than a mucosal surface, which is why tumour-tissue microbiome work needs dedicated contamination controls (Nejman et al., *Science* 2020;368(6494):973–80, [doi:10.1126/science.aay9189](https://www.science.org/doi/10.1126/science.aay9189)). Isolation from such a site is itself diagnostic — periprosthetic tissue culture is the reference method for prosthetic joint infection precisely because organisms should not be there ([Clin Microbiol Rev 2025 review](https://journals.asm.org/doi/10.1128/cmr.00054-25)).
4. **Clinical/diagnostic setting.** Human or veterinary patient, sampled during a medical encounter. This supports the pinned `CLINICAL` category and is attested in the strain metadata (e.g. strain 154980, Hôpital de la Timone, Marseille, 2007-07-30).
5. **Anatomical site unrecorded at the category level** — see §6. This is the differentia that makes the concept a residue rather than a kind.

**Inference, not sourced:** the ranking above, and the claim that these five together individuate the concept, is my synthesis. Each individual property is sourced; the claim that they constitute an adequate differentia is not something any source states.

---

## 4. Sources

| Claim | Source |
|---|---|
| Biopsy is a diagnostic procedure removing tissue from a living body | NCIT:C15189, [OLS4](https://www.ebi.ac.uk/ols4/ontologies/ncit/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FNCIT_C15189) |
| OBI models biopsy as a specimen-collection process, minimally invasive, living multicellular organism | OBI:0002650, [OLS4](https://www.ebi.ac.uk/ols4/ontologies/obi/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0002650) |
| A material "biopsy specimen" class exists but is a specimen, not a habitat | NCIT:C18202; SNOMED CT 258415003 |
| ENVO has no biopsy or clinical-specimen term; clinical terms are facilities | OLS4 ENVO queries (0 hits for "biopsy"; ENVO:03501136 / :03501183 / :03501158 for "clinical") |
| Genus candidate: animal-associated environment | ENVO:01001002; parent ENVO:01001000 (syn. *host-associated environment*) |
| Tissue as an anatomical kind | UBERON:0000479 |
| BacDive's isolation-source vocabulary is a 3-level hierarchy under 8 top classes | Reimer et al., *Nucleic Acids Res* 2019;47:D631–D636, [doi:10.1093/nar/gky879](https://academic.oup.com/nar/article/47/D1/D631/5106998); [isolation-source browser](https://bacdive.dsmz.de/isolation-sources) |
| BacDive 2025 scale and knowledge-graph/SPARQL access | Schober et al., *Nucleic Acids Res* 2025;53:D748–D756, [doi:10.1093/nar/gkae959](https://academic.oup.com/nar/article/53/D1/D748/7848838) |
| "Biopsy" co-occurs with independent body-site tags on a strain record | [BacDive strain 154980](https://bacdive.dsmz.de/strain/154980) — single strain, illustrative not systematic |
| Community standards record the *body site* (UBERON/FMA), not the collection procedure | MIXS:0000867 `host_body_site`, [GSC MIxS host-associated extension](https://genomicsstandardsconsortium.github.io/mixs/0016002/) |
| *H. pylori* first cultured from gastric antral biopsies | Marshall & Warren, *Lancet* 1984;323:1311–15, [PMID 6145023](https://pubmed.ncbi.nlm.nih.gov/6145023/) |
| Two attested taxa described from human stomach-mucosa biopsies | Roos, Engstrand & Jonsson, *IJSEM* 2005;55:77–82, [doi:10.1099/ijs.0.63083-0](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.63083-0) |
| Mucosa-associated ≠ luminal/faecal microbiota | Vaga et al., *Biochem Soc Trans* 2022;50:1225–36, [doi:10.1042/BST20201201](https://portlandpress.com/biochemsoctrans/article/50/5/1225/231920/Relationship-between-mucosa-associated-gut); [Sci Rep 2022;12:1758](https://www.nature.com/articles/s41598-022-05936-y) |
| Deep-tissue biopsy microbiomes are low-biomass and contamination-sensitive | Nejman et al., *Science* 2020;368:973–80, [doi:10.1126/science.aay9189](https://www.science.org/doi/10.1126/science.aay9189) |
| Tissue culture outperforms swabs; tissue is the PJI reference method | Aggarwal et al., *CORR* 2013, [PMID 23568679](https://pubmed.ncbi.nlm.nih.gov/23568679/); [Clin Microbiol Rev 2025](https://journals.asm.org/doi/10.1128/cmr.00054-25) |
| 95 strains / 73 taxa and the taxon ranking | This repo, `data/raw/bacdive_isolation_sources.tsv`, `data/raw/bacdive_source_taxa.tsv` (kg-microbe extraction of BacDive) — **not** an external citation |

**Explicitly my inference, not any source's claim:** (a) that the residual habitat content of "Biopsy" is "host tissue, site unrecorded"; (b) that ENVO:01001002 is the right genus for it; (c) the differentia ranking in §3; (d) that this concept should not be a term request.

---

## 5. Synonyms, and what not to conflate

**Names in real use for the same thing (candidate synonyms):**
- biopsy specimen / biopsy sample (material sense)
- tissue biopsy
- biopsy material, biopsied tissue
- German *Biopsie*, *Gewebeprobe* (BacDive is a DSMZ resource; older strain metadata is frequently German)

**Commonly but wrongly treated as the same:**

| Not the same as | Why |
|---|---|
| **Biopsy procedure** (NCIT:C15189, OBI:0002650) | The act, not the place. This is the error the current curation corrected. |
| **Biopsy specimen** (NCIT:C18202) | The excised material in a container. The habitat is the tissue *in situ*; the specimen begins where the habitat ends. |
| **Tissue** (UBERON:0000479) | Broader — any tissue of any multicellular organism, no living-host or clinical constraint. |
| **Autopsy / necropsy / resection tissue** | Same material, different procedure and often a dead host; BacDive tags separately. |
| **Swab** | Surface film, demonstrably different microbiology ([PMID 23568679](https://pubmed.ncbi.nlm.nih.gov/23568679/)). |
| **Body products** — blood, stool, sputum, pus, synovial fluid | A distinct MIxS field (`host_body_product`) and a distinct BacDive class; and biopsy-derived mucosal communities differ from luminal ones from the same organ ([doi:10.1042/BST20201201](https://portlandpress.com/biochemsoctrans/article/50/5/1225/231920/Relationship-between-mucosa-associated-gut)). |
| **The named organ records** — `Lung`, `Bone`, `Liver`, `Lymph node`, `Skin` | These are the *actual* habitats. "Biopsy" is the leftover when the organ was not tagged; it is not their parent and not their sibling in any principled sense. |
| **Infection / lesion / abscess** | Disease states, not places. `NOT_APPLICABLE` territory in this repo. |

---

## 6. Should it be a term at all?

**No — not as a new habitat term, and not as an ENVO term request.** The evidence points to a *sampling artefact*: a grouping individuated by how the sample was obtained rather than by any property of the place.

The argument, in four steps:

1. **Every authoritative definition of "biopsy" is a process definition** (NCIT:C15189, OBI:0002650). No source defines a biopsy as a place.
2. **The reference standards for reporting habitat record the site, not the method.** MIxS gives `host_body_site` (MIXS:0000867, expected value UBERON or FMA) for exactly this purpose ([GSC](https://genomicsstandardsconsortium.github.io/mixs/0016002/)). There is no MIxS field for "collected by biopsy" that plays a habitat role — because the collection method is provenance metadata, not environment.
3. **BacDive itself layers the tag over an independent site assertion.** Strain 154980 carries `Biopsy` *and* `Oral cavity and airways` *and* `Bone` ([BacDive 154980](https://bacdive.dsmz.de/strain/154980)). Where the site is known, the site tag carries it; the category-level "Biopsy" record is populated by the strains where it was not recorded at that level. The residue is heterogeneous by construction — the 73 taxa span gastric mucosa (*H. pylori*, *Limosilactobacillus gastricus*), oral cavity (*Granulicatella*, *S. gordonii*, *Schaalia turicensis*), lung (*Kroppenstedtia pulmonis*, *M. heckeshornense*), bone (*M. setense*) and skin/implant (*C. acnes*, *Corynebacterium freneyi*). These are not one habitat.
4. **Defining it would require asserting the union is a kind.** The only genuine common property — "interior tissue of a living animal host" — is already fully expressed by ENVO:01001002 plus UBERON:0000479, and adding "obtained by biopsy" narrows it by a *procedural* criterion that this repo has already ruled out as a grounding basis. A term whose differentia is a sampling method is exactly the "sampling artefact" case the objective anticipates.

**Recommended disposition — which is what the record already has:** keep `CONFIRM_UNGROUNDED`, keep `NCIT:C15189` as `relation: xref`, keep the `CLINICAL` category pinned. Two optional refinements a curator could take:

- Add **NCIT:C18202 "Biopsy Specimen"** as a second `xref` — it is the closest material-entity term and records the specimen link without asserting either identity or is-a.
- Add **ENVO:01001002 "animal-associated environment"** as a `parent`. Defensible: every strain here came from inside a living animal, so the parent claim is true of the whole set. But it says almost nothing, and given the concept is not really a habitat, leaving `parent_habitats` empty is equally defensible and I would slightly prefer it — an empty parent list correctly signals "we do not know where this is", which is the honest state of the data.

**Do not** attach `UBERON:0000479 "tissue"` as either grounding or parent: as grounding it asserts the record *is* tissue-in-general, which over-claims in the direction the repo's #99 note warns about; as a parent it is true but so weak it adds nothing a curator can use.

If the goal is to recover the 95 strains as usable habitat data, the productive route is not a definition — it is re-reading BacDive's free-text sampling site per strain (as in "human maxillary osseous biopsy") and re-attributing each strain to the organ record it belongs to. That is a data-extraction task upstream in `data/raw/`, not a term.

## Citations

1. https://www.ebi.ac.uk/ols4/ontologies/ncit/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FNCIT_C15189
2. https://www.ebi.ac.uk/ols4/ontologies/obi/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0002650
3. https://pubmed.ncbi.nlm.nih.gov/6145023/
4. https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(84
5. https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.63083-0
6. https://genomicsstandardsconsortium.github.io/mixs/0016002/
7. https://pubmed.ncbi.nlm.nih.gov/23568679/
8. https://bacdive.dsmz.de/strain/154980
9. https://academic.oup.com/nar/article/47/D1/D631/5106998
10. https://bacdive.dsmz.de/isolation-sources
11. https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001002
12. https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&code=C18202
13. https://www.ebi.ac.uk/ols4/search?q=biopsy%20specimen
14. https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000479
15. https://portlandpress.com/biochemsoctrans/article/50/5/1225/231920/Relationship-between-mucosa-associated-gut
16. https://www.nature.com/articles/s41598-022-05936-y
17. https://www.science.org/doi/10.1126/science.aay9189
18. https://journals.asm.org/doi/10.1128/cmr.00054-25
19. https://academic.oup.com/nar/article/53/D1/D748/7848838