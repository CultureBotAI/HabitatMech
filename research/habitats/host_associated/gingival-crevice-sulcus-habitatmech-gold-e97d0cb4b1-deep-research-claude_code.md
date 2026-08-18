---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T00:51:53.895581'
end_time: '2026-08-18T00:59:40.973510'
duration_seconds: 467.08
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Gingival crevice/sulcus
  habitat_identifier: habitatmech:GOLD.e97d0cb4b1
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Mammals: Human > Digestive system > Oral
    cavity > Gingival crevice/sulcus'
  assertions: '15'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Variant-match\
    \ review (#12): the variant route reaches UBERON:0000093 'sulcus', defined as\
    \ any depression or fissure in the surface of an organ \u2014 a bucket that would\
    \ collect every groove in the body. UBERON has no gingival sulcus term. The gingival\
    \ crevice is a real and heavily sampled habitat. Path: Host-associated > Mammals:\
    \ Human > Digestive system > Oral cavity > Gingival crevice/sulcus (source concept\
    \ habitatmech:GOLD.e97d0cb4b1)"
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
  num_turns: 30
  total_cost_usd: 2.8243914999999995
  session_id: 310acad9-8413-431a-bff5-8b1542cb2cd0
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 18
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Gingival crevice/sulcus
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.e97d0cb4b1
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Mammals: Human > Digestive system > Oral cavity > Gingival crevice/sulcus
- **Upstream assertion volume:** 15
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Variant-match review (#12): the variant route reaches UBERON:0000093 'sulcus', defined as any depression or fissure in the surface of an organ — a bucket that would collect every groove in the body. UBERON has no gingival sulcus term. The gingival crevice is a real and heavily sampled habitat. Path: Host-associated > Mammals: Human > Digestive system > Oral cavity > Gingival crevice/sulcus (source concept habitatmech:GOLD.e97d0cb4b1)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Gingival crevice/sulcus** as a microbial habitat, with citations.

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

I'll research this now.

Key lead: UBERON may in fact have this term. Verifying directly.

# Novel-term research: *Gingival crevice/sulcus* (`habitatmech:GOLD.e97d0cb4b1`)

## ⚠️ Headline finding: this concept is **not** novel — UBERON already has it, and it is already in this repo's vendored slice

Before the definition: the premise of this research task is wrong, and the curator's note on the decision is factually incorrect.

The note says *"UBERON has no gingival sulcus term."* UBERON does have it:

- **`UBERON:0008805`**, label **`gingival groove`**, with **`gingival sulcus`** and **`sulcus gingivalis`** as **exact synonyms** and **`tooth-gingiva interface`** as a related synonym.
- Definition (verbatim): *"The gingival sulcus is an area of potential space between a tooth and the surrounding gingival tissue and is lined by sulcular epithelium. The depth of the sulcus (Latin for groove) is bounded by two entities: apically by the gingival fibers of the connective tissue attachment and coronally by the free gingival margin."*
- xrefs: `FMA:74580`, `NCIT:C114645` ("Gingival Sulcus"), `SCTID:245753001` ("Entire gingival sulcus"), Wikipedia `Gingival_sulcus`.
- Source: [OLS4 — UBERON:0008805](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON%3A0008805)

It is **already vendored**, at `data/raw/ontology_terms.tsv:13367`, with `rdfs:subClassOf UBERON:0000093` at `data/raw/ontology_subclass_edges.tsv:11651`.

And **this corpus already has a record for it**: `data/habitats/host_associated/gingival_groove.yaml` — `UBERON:0008805`, `grounding_status: CLOSE`, `mapping_status: REVIEWED`, seeded from the *sibling* GOLD node `gold.ecosystem:5097` "Gingival sulcus" (path `Host-associated > Mammals > Digestive system > Oral cavity > Gingival sulcus`, source concept `habitatmech:GOLD.2f044b8c11`).

So the corpus currently holds **two records for one anatomical concept**, differing only in whether the GOLD path says `Mammals` or `Mammals: Human`: one grounded `CLOSE` to `UBERON:0008805` and reviewed, the other (`habitatmech:GOLD.e97d0cb4b1`) `CONFIRM_UNGROUNDED` on the stated grounds that no such term exists. The variant-match route reaching only the generic `UBERON:0000093 'sulcus'` is a **lexical retrieval failure**, and the reason is diagnosable: UBERON's *primary label* is `gingival groove`, not `gingival sulcus` — the match is on a synonym, not the label.

**The correct disposition is `GROUND`, not `CONFIRM_UNGROUNDED`.** HabitatMech should not mint a definition here.

---

## Proposed definition sentence

If the curator nevertheless writes one (for a term-request or for the note), the defensible single sentence is:

> A **sulcus** (`UBERON:0000093`) which lies between the cervical surface of a tooth and the free gingiva surrounding it, bounded coronally by the free gingival margin and apically by the junctional epithelium, lined by non-keratinised sulcular epithelium, and continuously bathed by serum-derived gingival crevicular fluid — a low-oxygen, low-redox, proteolytic microenvironment whose microbiota is distinct from that of exposed supragingival tooth surfaces.

That is the genus and differentia that `UBERON:0008805` already encodes. **Recommendation: adopt UBERON's definition rather than restating it.**

---

## 1. What the concept denotes

**The place.** A shallow, sleeve-like **potential space** (a "V" in cross-section) that encircles each tooth, between the tooth surface on one wall and the inner (sulcular) face of the free gingiva on the other. Its floor is the coronal-most extent of the junctional epithelium; its opening is the free gingival margin ([UBERON:0008805 definition](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON%3A0008805); [NCIT:C114645](https://www.ebi.ac.uk/ols4/ontologies/ncit/classes?obo_id=NCIT%3AC114645) — *"Space between a tooth and surrounding gingival tissue lined by sulcular epithelium"*).

**Dimensions.** Histological depth in clinically normal human gingiva averages **0.69 mm** (Gargiulo, Wentz & Orban 1961, n = 287 teeth, cadaver specimens; [doi:10.1902/jop.1961.32.3.261](https://doi.org/10.1902/jop.1961.32.3.261)). Clinical *probing* depth in health is conventionally given as **0.5–3 mm**, and probing depth differs materially from histological depth because the probe tip penetrates the junctional epithelium — a distinction worth keeping out of the definition.

**As a microbial habitat**, this is the site a "subgingival" sample comes from: a paper point, curette or scaler is introduced into the space and the biofilm adherent to the subgingival tooth surface, plus the fluid and desquamated cells within, is recovered. Dewhirst et al. (2010) list the **gingival sulcus explicitly as one of the discrete habitats of the oral cavity**, alongside teeth, tongue, cheeks, palates and tonsils ([J Bacteriol 192:5002–5017, doi:10.1128/JB.00542-10](https://doi.org/10.1128/JB.00542-10), PMID 20656903).

**Boundary — what is inside and what is next door.**

| Inside the concept | Neighbouring concept |
|---|---|
| The space itself, from gingival margin to junctional epithelium | The **gingiva** (tissue) — `UBERON:0001828` |
| The subgingival tooth surface forming one wall | The **junctional epithelium / epithelial attachment** forming the floor — `UBERON:0035149`, `UBERON:8000014` |
| The fluid and biofilm occupying it | **Subgingival dental plaque** as a material — `UBERON:0016484` |
| The healthy, non-pathologically-deepened space | The **periodontal pocket** — the same space pathologically deepened with attachment loss (a disease state) |

**Ambiguity, stated rather than resolved silently.** The label admits two readings: (a) the anatomical space/site, and (b) the material recovered from it (subgingival plaque). **The GOLD path settles it as (a):** the node sits under `Oral cavity` as a *site*, and GOLD carries a **separate sibling node** for the material — `gold.ecosystem:3913` "Subgingival plaque", same parent path, 113 organism assertions (already in this corpus at `data/habitats/host_associated/subgingival_plaque.yaml`, grounded `NARROW` to `UBERON:0016484`). GOLD splits site from material; so should HabitatMech, and UBERON already does.

## 2. Genus — the broader kind

**Genus: `UBERON:0000093` 'sulcus'** — *"A depression or fissure in the surface of an organ."* This is already the asserted parent of `UBERON:0008805` in the vendored slice, and already sits in `parent_habitats` on both the target record and the `gingival_groove.yaml` record.

The curator's note is right that `UBERON:0000093` alone is far too broad to be a *grounding* target — but it is exactly the right *genus*, which is why UBERON placed the specific term under it. The note treated "the genus is too broad" as evidence that no term exists, when the specific term existed one level down.

**ENVO check — near-misses, all failures:**

| Candidate | Why it fails |
|---|---|
| `ENVO:01001002` **animal-associated environment** — *"An environmental system determined by an animal."* | Correct *ancestor*, far too broad to be a grounding target; it is the ENVO pattern CLAUDE.md cites for host-as-habitat, not a term for this site. |
| `ENVO:01001055` **environment associated with an animal part or small animal** | Same: the right ENVO *class of pattern*, no gingival specialisation. |
| `ENVO:03501185` **dental clinic** | A built environment; unrelated. |
| ENVO oral terms generally | ENVO has **no** oral-cavity, dental, subgingival or periodontal environmental-system term. An OLS4 query of ENVO for "oral" and for "subgingival" returns only imported UBERON anatomy (`mouth`, `saliva`, `oral epithelium`) and `dental clinic`. ENVO defers oral anatomy to UBERON entirely. |
| `UBERON:0000167` **oral cavity** | Broader; already the ground of the parent record `habitatmech:GOLD.92d1e65695`. |
| `UBERON:0016484` **subgingival dental plaque** | *Narrower and a different category*: the biofilm material occupying the space, not the space. A near-miss worth recording, not a match. |
| `BTO:0003364` **gingival fluid** (syn. crevicular fluid, sulcular fluid) | The fluid contents, not the space. |

**Conclusion: the genus is `sulcus`, and the species-level term already exists as `UBERON:0008805`.**

## 3. Differentia — what distinguishes it from its siblings

All four properties below are measurable and sourced; they are also what makes this a *habitat* term rather than a bare anatomy term.

**a) Anatomical bounding (the definitional differentia).** Located between tooth and free gingiva; coronal bound = free gingival margin, apical bound = junctional epithelium / connective-tissue attachment; lined by non-keratinised sulcular epithelium, which is *not* attached to the tooth ([UBERON:0008805](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON%3A0008805); Gargiulo et al. 1961).

**b) Low oxygen tension / low redox — the dominant ecological selector.** Direct pO₂ electrode measurement at the base of 36 untreated human periodontal pockets (5–10 mm) gave **5–27 mmHg, mean 13.3 mmHg**; sites at ≤15 mmHg carried significantly higher proportions of spirochaetes, while microaerophilic *Capnocytophaga* occurred where pO₂ > 15 mmHg (Loesche et al. 1983, *Infect Immun* 42:659–667, [doi:10.1128/iai.42.2.659-667.1983](https://doi.org/10.1128/iai.42.2.659-667.1983), PMID 6642647, [free full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC264480/)). *Caveat for the curator: these are pocket measurements, i.e. the pathologically deepened form; I found no equivalent direct pO₂ series for the healthy 0.5–3 mm sulcus, and it is reasonable to expect the healthy sulcus to be less anaerobic. Do not put a specific mmHg figure in a definition of the healthy sulcus.*

**c) Serum-fed, proteolytic nutrition — not saliva-and-sugar.** The space is bathed by **gingival crevicular fluid**, a serum transudate in health that becomes an inflammatory exudate with inflammation, reaching the sulcus by diffusion across the basement membrane and junctional epithelium and carrying serum proteins, peptides, amino acids, immunoglobulins, leukocytes and desquamated epithelial cells (review: Barros et al. / Gingival Crevicular Fluid overview, *J Pharm Bioallied Sci* 2019, [doi:10.4103/jpbs.jpbs_56_19](https://doi.org/10.4103/jpbs.jpbs_56_19), PMID 31198325; [MeSH D005883 "Gingival Crevicular Fluid"](https://meshb.nlm.nih.gov/record/ui?ui=D005883)). Consequently **protein/peptide fermentation, not saccharolysis, is the predominant metabolism**, yielding short-chain fatty acids, NH₃, volatile sulfur compounds and amines (Frontiers in Oral Health 2023 narrative review, [doi:10.3389/froh.2023.1210200](https://doi.org/10.3389/froh.2023.1210200), PMID 37388417). *Flow-rate figures in the literature vary widely with collection method (~0.2 µL/h/site is commonly quoted; recovered volumes of 0.43–1.56 µL are also reported) — I would not put a number in the definition.*

**d) A compositionally distinct community, discriminable from every other oral site.** This is the strongest habitat-hood evidence and the one to cite:
- Distinct oral sites host communities *"composed of entirely different microbes"* and most oral microbes are **site specialists**; subgingival plaque is one of the discriminated sites, with genus- and species-level specialisation (e.g. *Actinomyces* subgingivally vs *Schaalia* on the tongue; *R. dentocariosa* vs *R. mucilaginosa*) — Mark Welch, Dewhirst & Borisy 2019, *Annu Rev Microbiol* 73:335–358, [doi:10.1146/annurev-micro-090817-062503](https://doi.org/10.1146/annurev-micro-090817-062503), PMID 31180804.
- Recent authoritative synthesis: Baker, Mark Welch, Kauffman, McLean & He 2024, *"The oral microbiome: diversity, biogeography and human health"*, *Nat Rev Microbiol* 22:89–104, [doi:10.1038/s41579-023-00963-6](https://doi.org/10.1038/s41579-023-00963-6), PMID 37700024 — structured biogeography arising from the distinct microenvironments of the oral cavity.
- Characteristic taxa: the "red complex" (*Porphyromonas gingivalis*, *Tannerella forsythia*, *Treponema denticola*) and "orange complex" were defined **from subgingival plaque specifically**, across 13,261 samples from 185 subjects — Socransky et al. 1998, *J Clin Periodontol* 25:134–144, [doi:10.1111/j.1600-051X.1998.tb02419.x](https://doi.org/10.1111/j.1600-051X.1998.tb02419.x), PMID 9495612. A 2025 meta-taxonomic re-analysis (135 patients, V3–V4 16S) revises the complexes into 10 unambiguous-taxon-group clusters: [doi:10.1111/jcpe.14138](https://doi.org/10.1111/jcpe.14138).
- Health vs disease: subgingival communities in periodontitis show higher diversity *and* higher biomass than health; inflammation expands the community more than it replaces it — Abusleme et al. 2013, *ISME J* 7:1016–1025, [doi:10.1038/ismej.2012.174](https://doi.org/10.1038/ismej.2012.174), PMID 23303375.

**Contrast with the nearest sibling site (supragingival plaque / exposed tooth surface):** saliva-bathed rather than serum-bathed, higher redox, dietary-carbohydrate-driven and saccharolytic, dominated by facultative anaerobes; the subgingival environment's lower redox is what enriches obligate anaerobes such as *Fusobacterium*, *Prevotella* and *Treponema* ([Frontiers Oral Health 2023](https://doi.org/10.3389/froh.2023.1210200); Loesche et al. 1983).

## 4. Sources

Everything above is cited inline. Explicit statements of provenance:

**Sourced claims** — anatomical bounds and lining (UBERON/NCIT/SNOMED definitions); 0.69 mm mean histological depth (Gargiulo 1961); pocket pO₂ 5–27 mmHg (Loesche 1983); GCF as serum transudate/inflammatory exudate and its diffusion route (JPBS 2019 review; MeSH D005883); proteolytic metabolism and low-redox anaerobe enrichment (Frontiers Oral Health 2023); site-specialist community distinctness (Mark Welch 2019; Baker 2024); red/orange complexes (Socransky 1998); health-vs-periodontitis biomass and diversity (Abusleme 2013); gingival sulcus listed as a discrete oral habitat (Dewhirst 2010).

**My inference, not stated by a source** — (i) that the GOLD path's placement as a sibling of "Subgingival plaque" under "Oral cavity" resolves the site-vs-material ambiguity in favour of the site reading; (ii) that the healthy sulcus is likely less anaerobic than the measured periodontal pockets; (iii) the diagnosis that the variant-match route failed because `gingival sulcus` is a synonym rather than UBERON's primary label.

**Not verified** — I could not resolve `FMA:74580` through OLS4 to confirm its label independently; that xref is UBERON's assertion, taken on trust. The other three xrefs (`NCIT:C114645`, `SCTID:245753001`, Wikipedia) I did confirm resolve to gingival-sulcus concepts.

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- gingival sulcus *(UBERON exact synonym; the standard periodontal term)*
- gingival crevice *(equally standard; the adjectival form survives in "gingival crevicular fluid")*
- sulcus gingivalis *(Latin; UBERON exact synonym)*
- tooth–gingiva interface *(UBERON related synonym)*
- dentogingival sulcus / dentogingival crevice
- subgingival space, subgingival site, sulcular site *(sampling literature; loose)*
- SNOMED sub-site names: buccal / labial / lingual / mesial / distal gingival crevice (`SNOMED:245755008`, `245756009`, `245757000`, `245758005`, `245759002`) — per-surface partitions of this same space

**Commonly but wrongly treated as the same thing**

| Term | Why it is not this concept |
|---|---|
| **subgingival (dental) plaque** — `UBERON:0016484`, `BTO:0000338`/`UBERON:0016482` for dental plaque | The **biofilm material** occupying the space. Already a separate record here (`subgingival_dental_plaque.yaml`), and GOLD keeps a separate node for it. |
| **gingival crevicular fluid** — `BTO:0003364` "gingival fluid", `MeSH:D005883`, `OMIT:0007078` | The **fluid**, a sample matrix. The single most frequent conflation, because "GCF" is what most papers actually assay. |
| **periodontal pocket** | The pathologically **deepened** sulcus with attachment loss — a disease state, with different depth, pO₂ and community. Loesche's mmHg figures come from pockets, not sulci. |
| **junctional epithelium / epithelial attachment** — `MeSH:D004846`, `UBERON:0035149`, `UBERON:8000014` (dentogingival junction) | The **tissue forming the floor**, not the space. |
| **sulcular epithelium** | The tissue forming one **wall**. |
| **gingiva** — `UBERON:0001828`; **gingival epithelium** — `UBERON:0001949` | The surrounding tissue; broader/adjacent. |
| **free gingival groove** | A shallow groove on the **outer** gingival surface, an external landmark roughly corresponding to the sulcus floor. This is a genuine hazard given UBERON's chosen label `gingival groove`, which reads like this term but is defined as the sulcus. |
| **supragingival plaque** — `UBERON:0016485` | The sibling site above the gingival margin; different redox, nutrition and community. |
| **oral cavity** — `UBERON:0000167`; **saliva** — `UBERON:0001836` | Broader / adjacent compartments. |

## 6. Should it be a term at all?

**Yes — it is a real, heavily sampled, physicochemically distinct microbial habitat, and it already has a term.** It is a place, not a process, quality, disease state, taxon or sampling artefact: it is an anatomical *part* of the host (a space of the dentogingival junction), which under this repo's own rule — *"A host's PARTS ground to the anatomy term"* — grounds normally, exactly as `gut`, `skin` and `blood` do. There is nothing to mint.

## Recommended action for the curator

1. **Change the decision on `habitatmech:GOLD.e97d0cb4b1` from `CONFIRM_UNGROUNDED` to `GROUND`**, target **`UBERON:0008805`**. ⚠️ The `GROUND` row must name the expected label as **`gingival groove`** — *not* "gingival sulcus". The seeder's label check compares against the vendored slice (`data/raw/ontology_terms.tsv:13367`), where the label is `gingival groove` and `gingival sulcus` is only a synonym. Writing the synonym will fail the seed.
2. **Expect a merge, and check it.** `UBERON:0008805` already carries the mammalian GOLD sibling `GOLD.2f044b8c11` (`gold.ecosystem:5097`). Grounding this concept folds its 15 GOLD `ORGANISM` assertions into the same record, and `gingival_crevice_sulcus.yaml` should disappear. That is a record retirement — per CLAUDE.md, the second pass applies: `seed-apply` → commit → `just redirects` → `just render` → commit, or the published `gingival-crevice-sulcus` URL 404s.
3. **Predicate.** The existing `UBERON:0008805` record is `CLOSE` (from the `Mammals` path). This path is `Mammals: Human`, i.e. host-restricted relative to the taxon-neutral UBERON class — the same situation the corpus scored `NARROW` for `GOLD.506abc1148` "Subgingival plaque" (human path) against `UBERON:0016484`. Following that precedent, `NARROW` is the consistent choice for the human path; `CLOSE` on the merged record is also defensible. Worth a one-line rationale in the note either way.
4. **File two issues.**
   - *Review-method defect:* the variant-match route (#12) misses UBERON terms whose match is on a synonym rather than the primary label, and the reviewer inferred non-existence from the route's failure rather than checking the vendored slice. `UBERON:0008805` was **already in `data/raw/ontology_terms.tsv` and already used by another record in the same corpus** when the note was written. Other `CONFIRM_UNGROUNDED` decisions produced by the same pass are worth re-checking against the slice's synonym column.
   - *Upstream (obophenotype/uberon):* `UBERON:0008805`'s primary label `gingival groove` collides with the distinct anatomical structure "free gingival groove" and buries the standard term `gingival sulcus` in the synonym list. A label swap upstream would prevent exactly this failure recurring.

---

## Sources

- [OLS4 — UBERON:0008805 `gingival groove`](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON%3A0008805)
- [OLS4 — UBERON:0016484 `subgingival dental plaque`](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON%3A0016484)
- [OLS4 — UBERON:0000093 `sulcus`](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON%3A0000093)
- [NCIT:C114645 `Gingival Sulcus`](https://www.ebi.ac.uk/ols4/ontologies/ncit/classes?obo_id=NCIT%3AC114645)
- [MeSH D005883 — Gingival Crevicular Fluid](https://meshb.nlm.nih.gov/record/ui?ui=D005883)
- Gargiulo, Wentz & Orban (1961), *J Periodontol* 32:261–267 — [doi:10.1902/jop.1961.32.3.261](https://doi.org/10.1902/jop.1961.32.3.261)
- Loesche, Gusberti, Mettraux, Higgins & Syed (1983), *Infect Immun* 42:659–667 — [doi:10.1128/iai.42.2.659-667.1983](https://doi.org/10.1128/iai.42.2.659-667.1983) · [PMC264480](https://pmc.ncbi.nlm.nih.gov/articles/PMC264480/)
- Socransky, Haffajee, Cugini, Smith & Kent (1998), *J Clin Periodontol* 25:134–144 — [doi:10.1111/j.1600-051X.1998.tb02419.x](https://doi.org/10.1111/j.1600-051X.1998.tb02419.x)
- Dewhirst et al. (2010), *J Bacteriol* 192:5002–5017 — [doi:10.1128/JB.00542-10](https://doi.org/10.1128/JB.00542-10)
- Abusleme et al. (2013), *ISME J* 7:1016–1025 — [doi:10.1038/ismej.2012.174](https://doi.org/10.1038/ismej.2012.174) · [PMC3635234](https://pmc.ncbi.nlm.nih.gov/articles/PMC3635234/)
- Mark Welch, Dewhirst & Borisy (2019), *Annu Rev Microbiol* 73:335–358 — [doi:10.1146/annurev-micro-090817-062503](https://doi.org/10.1146/annurev-micro-090817-062503)
- Baker, Mark Welch, Kauffman, McLean & He (2024), *Nat Rev Microbiol* 22:89–104 — [doi:10.1038/s41579-023-00963-6](https://doi.org/10.1038/s41579-023-00963-6)
- Gingival Crevicular Fluid: An Overview (2019), *J Pharm Bioallied Sci* — [doi:10.4103/jpbs.jpbs_56_19](https://doi.org/10.4103/jpbs.jpbs_56_19)
- Microbial metabolites in the pathogenesis of periodontal diseases (2023), *Front Oral Health* — [doi:10.3389/froh.2023.1210200](https://doi.org/10.3389/froh.2023.1210200)
- Microbial Complexes in Subgingival Plaque: A Bacterial Meta-Taxonomic Study (2025), *J Clin Periodontol* — [doi:10.1111/jcpe.14138](https://doi.org/10.1111/jcpe.14138)
- The Subgingival Microbial Composition in Health and Periodontitis with Different Probing Depths (2025), *Microorganisms* — [mdpi.com/2076-2607/13/4/930](https://www.mdpi.com/2076-2607/13/4/930)

## Citations

1. https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON%3A0008805
2. https://www.ebi.ac.uk/ols4/ontologies/ncit/classes?obo_id=NCIT%3AC114645
3. https://doi.org/10.1902/jop.1961.32.3.261
4. https://doi.org/10.1128/JB.00542-10
5. https://doi.org/10.1128/iai.42.2.659-667.1983
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC264480/
7. https://doi.org/10.4103/jpbs.jpbs_56_19
8. https://meshb.nlm.nih.gov/record/ui?ui=D005883
9. https://doi.org/10.3389/froh.2023.1210200
10. https://doi.org/10.1146/annurev-micro-090817-062503
11. https://doi.org/10.1038/s41579-023-00963-6
12. https://doi.org/10.1111/j.1600-051X.1998.tb02419.x
13. https://doi.org/10.1111/jcpe.14138
14. https://doi.org/10.1038/ismej.2012.174
15. https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON%3A0016484
16. https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON%3A0000093
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC3635234/
18. https://www.mdpi.com/2076-2607/13/4/930