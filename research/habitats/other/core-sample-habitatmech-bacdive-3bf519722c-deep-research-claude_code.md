---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T22:06:12.734695'
end_time: '2026-08-17T22:16:52.173544'
duration_seconds: 639.44
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Core-sample
  habitat_identifier: habitatmech:BACDIVE.3bf519722c
  habitat_category: OTHER
  grounding_status: UNGROUNDED
  attestations: 'BACDIVE: Core-sample'
  assertions: '60'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Cohort
    review: the screen''s known blind spot, caught by reading the corpus rather than
    the ranking. NCIT:C180316 "Nucleotide Sequence Sample Name" is a metadata field
    name, not a place; it shares the word "sample" with the subject, so it lands in
    the low-risk overlap bucket. A sediment or ice core is a real habitat and no term
    in the slice names it. (source concept habitatmech:BACDIVE.3bf519722c)'
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
  web_search_requests: 16
  num_turns: 41
  total_cost_usd: 4.254887
  session_id: fd96af33-7f47-4f32-ac07-1ba3570edb1d
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 52
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Core-sample
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:BACDIVE.3bf519722c
- **Category:** OTHER
- **Grounding status:** UNGROUNDED
- **Source attestations:** BACDIVE: Core-sample
- **Upstream assertion volume:** 60
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Cohort review: the screen's known blind spot, caught by reading the corpus rather than the ranking. NCIT:C180316 "Nucleotide Sequence Sample Name" is a metadata field name, not a place; it shares the word "sample" with the subject, so it lands in the low-risk overlap bucket. A sediment or ice core is a real habitat and no term in the slice names it. (source concept habitatmech:BACDIVE.3bf519722c)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Core-sample** as a microbial habitat, with citations.

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

# Core-sample (`habitatmech:BACDIVE.3bf519722c`) — definition research

> **A mass of environmental material which has been recovered as a vertically continuous cylinder, preserving its depth stratification, by driving or drilling a hollow corer into sediment, rock, soil, or ice below a surface.**

**Read this first.** That sentence is a defensible definition of what "Core-sample" *names*, but it defines a **specimen form and its mode of recovery**, not a kind of place. The evidence below — most decisively the structure of BacDive's own vocabulary — indicates that `Core-sample` is a **sampling-method tag layered on top of place tags**, and that for every strain carrying it BacDive *also* records the actual habitat (`#Marine`, `#Sediment`, `#Glacier`, `#Geologic`). My recommendation is in §6; the existing `CONFIRM_UNGROUNDED` note ("A sediment or ice core is a real habitat and no term in the slice names it") is defensible but rests on a premise the source data does not support.

---

## 1. What the concept denotes

### 1.1 The literal sense

A core sample is a cylindrical section of a naturally occurring substance obtained by driving or drilling a hollow tube (core barrel, core drill, push corer, gravity corer) into a substrate, so that the substrate enters the tube more or less intact and its vertical structure and stratification are preserved. In scientific ocean drilling this is formalised: a *core* is "a cylindrical section of recovered drilled sediments or rocks", subdivided into sections, split lengthwise, and indexed to a *cored interval* — a depth range in the drilled column ([IODP Expedition 374 methods](https://publications.iodp.org/proceedings/374/102/374_102.html); [IODP visual core description conventions](https://publications.iodp.org/proceedings/320_321/102/102_3.htm)). GENEPIO encodes the instrument with essentially this wording: *core sampling device* ([GENEPIO:0100943](https://www.ebi.ac.uk/ols4/ontologies/genepio/classes?obo_id=GENEPIO:0100943)) — "A grab sampler designed to extract a continuous, cylindrical section of material from a substrate preserving vertical structure and stratification."

So the intension of the label is: *cylinder of substrate + recovered by coring + stratification preserved*. Nothing in it fixes what the substrate is or where it was.

### 1.2 What the 60 BacDive strains actually mean by it

This is the decisive evidence, and it points two ways at once.

**(a) In BacDive's vocabulary, `Core sample` sits where places sit, but behaves like a method.** BacDive classifies isolation sources with the three-level Microbial Isolation Source Ontology (MISO): eight level-1 classes (`#Environmental`, `#Engineered`, `#Host`, `#Host body-site`, `#Host body-product`, `#Medical`, `#Condition`, `#Climate`), refined by level-2 and level-3 tags ([Reimer et al. 2019, *NAR* 47:D631–D636, doi:10.1093/nar/gky879](https://doi.org/10.1093/nar/gky879); [BacDive in 2022, *NAR* 50:D741, doi:10.1093/nar/gkab961](https://doi.org/10.1093/nar/gkab961)). `Core sample` is a **level-3 tag under `#Environmental` → `#Geologic`** ([BacDive isolation-source browser](https://bacdive.dsmz.de/isolation-sources)) — i.e. it occupies the same slot as `Marine`, `Sediment`, `Glacier`, `Permafrost`, `Volcanic`, all of which are places or materials.

**(b) Strains carry it *in addition to* a place tag, not instead of one.** I pulled the raw tag sets from two strains in this record's characteristic-taxa list:

| Strain | Free-text isolation source | MISO tags actually asserted |
|---|---|---|
| *Calderihabitans maritimus* KKC1 ([BacDive 24651](https://bacdive.dsmz.de/strain/24651)) | "marine sediment core of an undersea caldera" | `#Environmental` `#Aquatic` `#Marine` `#Terrestrial` `#Sediment` `#Volcanic` **`#Core sample`** |
| *Anaerosporomusa subterranea* FRC-RU4 ([BacDive 132639](https://bacdive.dsmz.de/strain/132639)) | "unconsolidated saprolite from a sediment core" | `#Environmental` `#Terrestrial` `#Geologic` `#Sediment` **`#Core sample`** |

The habitat is already named by a co-asserted tag in both cases. `#Core sample` adds *how the material was obtained*, not *where the organism lived*.

**(c) The substrates are heterogeneous and span at least four unrelated habitats.** Verified isolation records for taxa in this record:

| Taxon in the record | Actual substrate | Source |
|---|---|---|
| *Bacillus infernus* (2 strains) | shale core, 2.65–2.77 km below land surface, Taylorsville Triassic Basin, Virginia; DSMZ records the source verbatim as "core sample from 2.7 km depth" | [Boone et al. 1995, *IJSB* 45:441–448, doi:10.1099/00207713-45-3-441](https://doi.org/10.1099/00207713-45-3-441), PMID [8590670](https://pubmed.ncbi.nlm.nih.gov/8590670/); [DSM 10276](https://www.dsmz.de/catalogues/details/culture/DSM-10276.html) |
| *Anaeromyxobacter dehalogenans* (6 strains, rank 1) | soil/sediment cores from boreholes FW032/FW034, uranium-contaminated fractured saprolite, DOE Oak Ridge FRC | [Thomas et al. 2009, *AEM* 75:3679–3687, doi:10.1128/AEM.02473-08](https://doi.org/10.1128/AEM.02473-08) |
| *Anaerosporomusa subterranea* | unconsolidated saprolite core, Oak Ridge | [Choi et al. 2016, *IJSEM* 66:3848–3854, doi:10.1099/ijsem.0.001275](https://doi.org/10.1099/ijsem.0.001275), PMID [27381468](https://pubmed.ncbi.nlm.nih.gov/27381468/) |
| *Calderihabitans maritimus* | marine sediment core, Kikai caldera, Japan | [Yoneda et al. 2013, *IJSEM* 63:3602–3608, doi:10.1099/ijs.0.050468-0](https://doi.org/10.1099/ijs.0.050468-0), PMID [23606483](https://pubmed.ncbi.nlm.nih.gov/23606483/) |
| *Massilia glaciei* | ice core, Muztagh Glacier, Tibetan Plateau | [Shen et al. 2017, *IJSEM*, doi:10.1099/ijsem.0.002252](https://doi.org/10.1099/ijsem.0.002252), PMID [28901899](https://pubmed.ncbi.nlm.nih.gov/28901899/) |
| *Hymenobacter glacieicola* | ice core, Muztagh Glacier | [Su et al. 2016, *IJSEM*, doi:10.1099/ijsem.0.001266](https://doi.org/10.1099/ijsem.0.001266) |
| *Massilia eurypsychrophila*, *M. psychrophila*, *M. yuzhufengensis*, *Polaromonas eurypsychrophila*, *Sandarakinorhabdus glacialis*, *Hymenobacter frigidus* | Tibetan Plateau glacier ice cores (same programme) | as above; cf. [*Dyadobacter tibetensis* from 59 m ice-core depth](https://pmc.ncbi.nlm.nih.gov/articles/PMC6680632/) |
| *Thermosediminibacter litoriperuensis*, *Pseudothermotoga profunda*, *Rubrivirga profundi*, *Psychrobacter pacificensis*, *Roseivirga pacifica*, *Pseudooceanicola nanhaiensis* | deep-sea / subseafloor sediment and deep-water provenance | *not individually verified by me — inferred from epithets and genus provenance; treat as unconfirmed* |

So the cohort mixes **glacier ice**, **deep-sea and caldera marine sediment**, **weathered continental saprolite**, and **deep sedimentary bedrock (shale at 2.7 km)**. These have no shared ecological genus beyond "solid, subsurface, dark, energy-poor" — and glacier ice is not even subsurface in ENVO's sense of "not exposed to the atmosphere".

### 1.3 Boundary: in vs. out

**Inside the literal concept:** intact cylinders of sediment, rock, soil, ice, or peat recovered by piston/gravity/rotary/push coring, from land, seafloor, glacier, or permafrost.

**Neighbouring, and outside it:**
- **Drill cuttings, rock trimmings, mud returns** — comminuted material returned by the drilling fluid; explicitly a *different* `samp_type` from `core` in MIxS ([MIXS:0000998 `samp_type`](https://genomicsstandardsconsortium.github.io/mixs/0000998/)).
- **The borehole itself** — [ENVO:00002226 *borehole*](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002226) ("A channel which is constructed by removing materials from land or submerged beds") and [ENVO:00000026 *well*](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00000026) are the void left behind, not the recovered column.
- **Groundwater / formation fluid / produced water** — pumped, not cored; MIxS splits these into the sibling *hydrocarbon resources — fluids/swabs* package.
- **The core's outer surface** — routinely discarded as drilling-fluid-contaminated (see §3.3); only the interior is treated as the habitat sample.
- **Clinical core biopsies** — [SNOMED:430970004 *Core sample of tissue block*](https://www.ebi.ac.uk/ols4/ontologies/snomed/classes?obo_id=SNOMED:430970004), [NCIT:C159488 *Bone Marrow Core Biopsy Sample*](https://www.ebi.ac.uk/ols4/ontologies/ncit/classes?obo_id=NCIT:C159488). Same word, different domain; irrelevant to a BacDive `#Environmental` `#Geologic` tag.

**The ambiguity, stated plainly.** The label has two readings and the data supports the second:
1. **Habitat reading** — "the subsurface material that cores are cut from", i.e. deep sediment/rock/ice as a place microbes live.
2. **Specimen/method reading** — "material in the form of a core, obtained by coring", indifferent to which habitat.

Reading 2 is what BacDive means, because (a) the tag co-occurs with independent place tags on the same strain, and (b) its members are drawn from mutually exclusive habitats that BacDive tags separately. Reading 1 is what the current curation note assumes.

---

## 2. Genus — the broader kind

### 2.1 Under the literal (specimen) reading

The smallest well-established kind is **environmental specimen** — [GENEPIO:0001246](https://www.ebi.ac.uk/ols4/ontologies/genepio/classes?obo_id=GENEPIO:0001246), the class MIxS points `samp_type` at, and under which "core" is one of the enumerated values ([MIXS:0000998](https://genomicsstandardsconsortium.github.io/mixs/0000998/): "samples include types like **core**, rock trimmings, drill cuttings, piping section, coupon, pigging debris, solid deposit, produced fluid, produced water, injected water, and swabs"). This genus is *correct* and *fatal*: a specimen is not a habitat, and HabitatMech records habitats.

### 2.2 Under the habitat reading

The smallest genus is **environmental material** — [ENVO:00010483](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00010483) ("A material entity which other material entities in an environmental system are primarily or partially composed of"). This is very high in the tree; every candidate intermediate fails (below).

### 2.3 ENVO near-misses, and why each fails

I searched ENVO exhaustively via OLS4 for `core`, `core sample`, `sediment core`, `drill core`, `ice core`, `subsurface`, `saprolite`, and checked the vendored slice in `data/raw/ontology_terms.tsv`. Results:

| Candidate | Label / definition | Why it is not a match |
|---|---|---|
| **[ENVO:01001530](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001530)** *water ice core* | "An ice mass which has been drilled from an accumulation of snow and ice…"; synonyms *ice core*, *ice sample*; parent [ENVO:01000293](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01000293) *ice mass*. **Present in the vendored slice.** | **The only true "core" term in ENVO, and strictly narrower** — covers roughly the ~10 Tibetan-glacier strains, excludes every sediment, saprolite and shale core. Grounding here would misclassify ~50 of 60 strains. *This is the single most important near-miss and is worth recording: it establishes that ENVO is willing to mint recovery-defined terms of exactly this shape.* |
| [ENVO:00002007](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002007) *sediment* | "Particulate environmental material… transport and deposition of particles by flowing liquid" | Narrower (excludes ice, shale bedrock, saprolite) and asserts a depositional origin saprolite does not have. |
| [ENVO:03000033](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:03000033) *marine sediment*, [ENVO:00002113](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002113) *deep marine sediment* | | Narrower; covers only the marine subset. |
| [ENVO:03600016](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:03600016) *saprolite*, [ENVO:00002056](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002056) *shale*, [ENVO:00001998](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00001998) *soil* | | Each covers one substrate in the cohort; all narrower. |
| [ENVO:01001046](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001046) *planetary subsurface environment* / [ENVO:01000941](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01000941) *planetary subsurface zone* / [ENVO:01001776](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001776) *subsurface zone of an astronomical body* | "Regions… not exposed to the planet's atmosphere or space" | Closest **habitat-side** genus, but (i) it is an *environmental system / zone*, not a material — a core is a portion of material, not a region; (ii) it asserts subsurface-ness, which glacier ice cores from the upper tens of metres of an ice field sit awkwardly under; (iii) it is far broader (includes aquifers, caves, mines, oil reservoirs). Usable as a `parent_habitats` entry under the habitat reading, not as an identity. |
| [ENVO:00002226](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002226) *borehole*, [ENVO:00000026](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00000026) *well* | The channel/hole | The void, not the recovered column. Over-claims an engineered-feature identity. |
| [ENVO:00002184](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002184) *subsurface landform* | | A landform; a core is not a landform. |
| **[NCIT:C180316](https://www.ebi.ac.uk/ols4/ontologies/ncit/classes?obo_id=NCIT:C180316)** *Nucleotide Sequence Sample Name* | The upstream `skos:closeMatch` in `data/raw/isolation_source_groundings.tsv` (lexical match, `ols4_search_synonym`) | Already correctly rejected in the existing note: a metadata field name, not a place. Confirmed. |
| [GENEPIO:0100943](https://www.ebi.ac.uk/ols4/ontologies/genepio/classes?obo_id=GENEPIO:0100943) *core sampling device*, [GENEPIO:0100934](https://www.ebi.ac.uk/ols4/ontologies/genepio/classes?obo_id=GENEPIO:0100934) *soil coring* | device; "A specimen collection process…" | An instrument and a process. Correct targets for `relation: xref`; never for identity or `parent_habitats` (HabitatMech reserves `NOT_APPLICABLE`-style handling for processes and procedures). |
| [MIXS:0016015](https://genomicsstandardsconsortium.github.io/mixs/0016015/) *hydrocarbon resources — cores* | MIxS environmental package | A **checklist**, not a class of place. Evidence for the method reading, not a genus. |

**Conclusion on genus:** ENVO has no term for a core sample in general. It has exactly one recovery-defined core term (`water ice core`), which is narrower than this concept. Under the specimen reading the genus is *environmental specimen* (out of scope for HabitatMech); under the habitat reading the only honest genus is *environmental material*, one step below the root of ENVO's material branch.

---

## 3. Differentia — what would distinguish it

Take these as candidate differentiae if a curator proceeds with a term. Each is observable; the first two are the only ones that actually discriminate.

**3.1 Recovery geometry and stratigraphic integrity (discriminating).** A continuous cylinder whose axis is the depth axis, so that stratification, bedding, and age–depth ordering are preserved and each subsample is indexed to a depth below the surface ([GENEPIO:0100943](https://www.ebi.ac.uk/ols4/ontologies/genepio/classes?obo_id=GENEPIO:0100943); [IODP Exp. 374 methods](https://publications.iodp.org/proceedings/374/102/374_102.html)). This is precisely what separates a core from cuttings, grab samples, and swabs — MIxS lists all of these as distinct `samp_type` values ([MIXS:0000998](https://genomicsstandardsconsortium.github.io/mixs/0000998/)). It is also why recovery is quantified: elastic rebound and gas exsolution can yield >100% apparent recovery, an artefact reported per core ([IODP Exp. 374 methods](https://publications.iodp.org/proceedings/374/102/374_102.html)).

**3.2 Access restricted to drilling (discriminating for the habitat reading).** The material is not reachable by surface sampling; a drill string, piston corer, or ice auger is required. This is the property the cohort genuinely shares.

**3.3 A contaminated exterior and an indigenous interior (discriminating, and unique to this concept).** Because drilling fluid carries surface microbes into the recovered column, the *habitat* is operationally the core's **interior**, and the periphery is discarded. This is enforced with tracers: perfluorocarbon tracer (perfluoromethylcyclohexane) fed continuously into the drilling fluid and detected by GC, and 0.5 µm fluorescent microspheres sized to mimic cells (0.2–1.3 µm) applied in the fluid or dried onto the core barrel; subsamples are then taken from rim, intermediate, and centre positions with sterile cut-off syringes ([Yanagawa et al. 2013, IODP Exp. 331, *Sci. Drill.*, PMC3820981](https://pmc.ncbi.nlm.nih.gov/articles/PMC3820981/); [Juck et al. 2005, *AEM* 71:1035–1041, doi:10.1128/AEM.71.2.1035-1041.2005](https://doi.org/10.1128/AEM.71.2.1035-1041.2005) — the permafrost/ground-ice variant, which reports microsphere penetration of <1 cm from the exterior). *Note this cuts both ways: a differentia about how you clean a specimen is a property of the specimen-handling protocol, which is itself an argument that the concept is a specimen.*

**3.4 Physicochemistry of the sampled habitats (NOT discriminating).** The cohort's habitats share darkness, no photosynthesis, low energy flux, long residence times, and steep depth gradients, but the values diverge wildly: −5 to +2 °C in glacier ice and permafrost versus 55–68 °C for *Calderihabitans maritimus* and 61 °C for *Bacillus infernus*. Cell abundance in subseafloor sediment spans five orders of magnitude across sites and correlates with sedimentation rate and distance from land ([Kallmeyer et al. 2012, *PNAS* 109:16213–16216, doi:10.1073/pnas.1203849109](https://doi.org/10.1073/pnas.1203849109)); life persists to 120 °C at 1.2 km below the Nankai seafloor, with cells rare and endospore-dominated above 45 °C ([Heuer et al. 2020, *Science* 370:1230–1234, doi:10.1126/science.abd7934](https://doi.org/10.1126/science.abd7934)); the continental subsurface holds an estimated 2–6 × 10²⁹ cells with community composition correlating to **lithology** ([Magnabosco et al. 2018, *Nat. Geosci.* 11:707–717, doi:10.1038/s41561-018-0221-6](https://doi.org/10.1038/s41561-018-0221-6)); permafrost is treated as its own ecological niche ([Jansson & Taş 2014, *Nat. Rev. Microbiol.* 12:414–425, doi:10.1038/nrmicro3262](https://doi.org/10.1038/nrmicro3262)). **My inference, stated as such:** the fact that Magnabosco et al. find community composition tracks lithology is an argument *against* a lithology-agnostic habitat class — the ecologically meaningful grouping is the substrate, not the corer.

---

## 4. Sources

Consolidated; every claim above is anchored to one of these. Items marked ▲ are my inference from the cited material rather than a statement the source makes.

**Vocabularies and standards**
- ENVO via OLS4 — [ENVO:01001530 water ice core](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001530) (sole ENVO "core" term; parent [ENVO:01000293 ice mass](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01000293)); [ENVO:00010483](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00010483), [ENVO:01001046](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001046), [ENVO:00002226](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002226), [ENVO:03600016](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:03600016). Queried 2026-08-17; `numFound = 1` for `"core sample"` restricted to ENVO.
- GENEPIO — [core sampling device GENEPIO:0100943](https://www.ebi.ac.uk/ols4/ontologies/genepio/classes?obo_id=GENEPIO:0100943), [soil coring GENEPIO:0100934](https://www.ebi.ac.uk/ols4/ontologies/genepio/classes?obo_id=GENEPIO:0100934), [environmental specimen GENEPIO:0001246](https://www.ebi.ac.uk/ols4/ontologies/genepio/classes?obo_id=GENEPIO:0001246).
- MIxS — [`samp_type` MIXS:0000998](https://genomicsstandardsconsortium.github.io/mixs/0000998/); [hydrocarbon resources–cores package MIXS:0016015](https://genomicsstandardsconsortium.github.io/mixs/0016015/); Tsesmetzis et al. 2016, MIxS-HCR, *Standards in Genomic Sciences* [doi:10.1186/s40793-016-0203-5](https://doi.org/10.1186/s40793-016-0203-5) (93-field checklist; "some terms pertain to the HCR entity as a whole while others concern the samples acquired from it" — the entity/specimen split made explicit).
- Yilmaz et al. 2011, MIMARKS/MIxS, *Nat. Biotechnol.* 29:415–420 [doi:10.1038/nbt.1823](https://doi.org/10.1038/nbt.1823) — the environmental triad (`env_broad_scale` / `env_local_scale` / `env_medium`) is where habitat is recorded; collection device and material processing are separate slots. See also [Using ENVO with MIxS](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS).
- BacDive — [Reimer et al. 2019, *NAR* 47:D631, doi:10.1093/nar/gky879](https://doi.org/10.1093/nar/gky879) (MISO, three-level tags, eight level-1 classes); [Reimer et al. 2022, *NAR* 50:D741, doi:10.1093/nar/gkab961](https://doi.org/10.1093/nar/gkab961); [isolation-source browser](https://bacdive.dsmz.de/isolation-sources) (`Core sample` under `#Environmental` → `#Geologic`); strain records [24651](https://bacdive.dsmz.de/strain/24651) and [132639](https://bacdive.dsmz.de/strain/132639) (co-asserted tag sets, retrieved 2026-08-17).
- IODP core nomenclature — [Exp. 374 methods](https://publications.iodp.org/proceedings/374/102/374_102.html), [Exp. 320/321 visual core description](https://publications.iodp.org/proceedings/320_321/102/102_3.htm).

**Primary literature on the habitats and the isolates**
- Boone et al. 1995, *IJSB* 45:441–448 [doi:10.1099/00207713-45-3-441](https://doi.org/10.1099/00207713-45-3-441), PMID 8590670; DSMZ [DSM 10276](https://www.dsmz.de/catalogues/details/culture/DSM-10276.html) / [DSM 10277](https://www.dsmz.de/collection/catalogue/details/culture/DSM-10277) — "core sample from 2.7 km depth".
- Thomas et al. 2009, *AEM* 75:3679–3687 [doi:10.1128/AEM.02473-08](https://doi.org/10.1128/AEM.02473-08) — Oak Ridge FRC soil cores from boreholes FW032/FW034.
- Choi, Shah & Yee 2016, *IJSEM* 66:3848–3854 [doi:10.1099/ijsem.0.001275](https://doi.org/10.1099/ijsem.0.001275).
- Yoneda et al. 2013, *IJSEM* 63:3602–3608 [doi:10.1099/ijs.0.050468-0](https://doi.org/10.1099/ijs.0.050468-0).
- Shen et al. 2017, *Massilia glaciei* [doi:10.1099/ijsem.0.002252](https://doi.org/10.1099/ijsem.0.002252); Su et al. 2016, *Hymenobacter glacieicola* [doi:10.1099/ijsem.0.001266](https://doi.org/10.1099/ijsem.0.001266); [*Dyadobacter tibetensis* from 59 m ice-core depth](https://pmc.ncbi.nlm.nih.gov/articles/PMC6680632/).
- Kallmeyer et al. 2012 [doi:10.1073/pnas.1203849109](https://doi.org/10.1073/pnas.1203849109); Heuer et al. 2020 [doi:10.1126/science.abd7934](https://doi.org/10.1126/science.abd7934); Magnabosco et al. 2018 [doi:10.1038/s41561-018-0221-6](https://doi.org/10.1038/s41561-018-0221-6); Jansson & Taş 2014 [doi:10.1038/nrmicro3262](https://doi.org/10.1038/nrmicro3262).
- Contamination control: Yanagawa et al. 2013 [PMC3820981](https://pmc.ncbi.nlm.nih.gov/articles/PMC3820981/); Juck et al. 2005 [doi:10.1128/AEM.71.2.1035-1041.2005](https://doi.org/10.1128/AEM.71.2.1035-1041.2005).

**Explicitly my inference, not a source's claim (▲)**
- ▲ That `#Core sample` functions as a method tag rather than a place tag. *Basis:* the co-assertion pattern in the two BacDive strain records plus the heterogeneity of verified substrates. No publication states this about the MISO vocabulary.
- ▲ That the cohort has no shared physicochemistry (§3.4).
- ▲ The deep-sea provenance of *Thermosediminibacter litoriperuensis*, *Pseudothermotoga profunda*, *Rubrivirga profundi*, *Psychrobacter pacificensis*, *Roseivirga pacifica*, *Pseudooceanicola nanhaiensis* — not verified against their species descriptions.
- ▲ I audited isolation sources for ~12 of the 49 taxa (60 strains). The remainder are unaudited; the mix could be more or less heterogeneous than reported.

---

## 5. Synonyms, and what not to conflate

**Names in real use for the same thing**
- core, drill core, rock core, core sample, sediment core, soil core, ice core, peat core, core column, core section, whole-round core, core catcher sample, boring sample, core specimen. (DSMZ/BacDive free text uses "core sample", "sediment core", "ice core drilled from …".)

**Commonly but wrongly treated as the same thing**
| Conflated with | Why it is different |
|---|---|
| **Sediment** ([ENVO:00002007](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002007)) / marine sediment | Most cores are sediment cores, so the terms drift together — but shale, saprolite, ice and peat cores are not sediment, and sediment sampled by grab or push-tube is still sediment. |
| **Ice core** ([ENVO:01001530](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001530)) | A proper subtype only. |
| **Borehole / well** ([ENVO:00002226](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002226), [ENVO:00000026](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00000026)) | The hole vs. the material taken out of it. |
| **Drill cuttings / rock trimmings / drilling mud** | Distinct MIxS `samp_type` values; no stratigraphic integrity; heavily fluid-contaminated. |
| **Deep subsurface / deep biosphere** | The habitat vs. the specimen from it. Also mismatched in extension: glacier ice cores are not deep-subsurface; mine and cave sampling reaches the deep subsurface without coring. |
| **Core biopsy** (SNOMED:430970004, SNOMED:434479002, NCIT:C159488) | Clinical tissue, different domain entirely. |
| **NCIT:C180316 "Nucleotide Sequence Sample Name"** | A metadata field label; the upstream lexical `skos:closeMatch`. Already rejected. |
| **Coring, as a process** ([GENEPIO:0100934 soil coring](https://www.ebi.ac.uk/ols4/ontologies/genepio/classes?obo_id=GENEPIO:0100934)) | A process, not a material or a place. |

---

## 6. Should this be a term at all?

**My recommendation: no — this is a sampling artefact, and I would revisit the current `CONFIRM_UNGROUNDED`.**

The reasoning, in the terms this repo uses:

1. **It is not a place.** `Core sample` names a specimen form and its mode of recovery. The rule that decides it is the same one behind HabitatMech's `parent_habitats` discipline: a term goes in only if it is genuinely broader than the concept, and the concept has to be a habitat first. A cylinder of material defined by the tool that extracted it is what MIxS calls a `samp_type` value under *environmental specimen*, and MIxS deliberately records that in a different slot from the environmental triad ([Yilmaz et al. 2011](https://doi.org/10.1038/nbt.1823); [MIXS:0000998](https://genomicsstandardsconsortium.github.io/mixs/0000998/)).

2. **The upstream source already records the habitat separately.** Every `#Core sample` strain I checked also carries a place triple (`#Aquatic #Marine`, `#Terrestrial #Sediment`). Nothing is lost by declining to mint a habitat term here; the assertions are not orphaned, they are duplicated onto tags that already have records in this corpus (`Marine`, 2,040 strains; `Terrestrial`, 13,182; `Geologic`, 381).

3. **Minting a term would create a cross-cutting class that merges four unrelated habitats** — glacier ice, marine sediment, saprolite, and 2.7 km shale — which is exactly the failure mode the seeder's ambiguous-GOLD-leaf rule exists to prevent ("Grounding them all to the same term would merge marine, freshwater, and hot-spring sediment into one record with mixed attestations").

4. **The one honest counter-argument, stated fairly.** ENVO already carries [ENVO:01001530 *water ice core*](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001530), defined by recovery ("An ice mass which has been **drilled from** …") and classified as a material, not a specimen. So ENVO is not doctrinally opposed to recovery-defined material terms. If the curator finds that precedent binding, the definition at the top of this report is the one to use, with `relation: xref` to `ENVO:01001530` and `GENEPIO:0100943`, and no `parent_habitats` beyond `ENVO:00010483`. I think that is the weaker reading — `water ice core` succeeds because ice cores come from one substrate in one setting, which is precisely what this concept does not have.

**Disposition, concretely.** The repo's `NOT_APPLICABLE` is described as covering "diseases, qualities, processes and procedures"; a specimen form produced by a procedure is adjacent to but not squarely inside that list, and `tests/test_decisions.py` only blocks `NOT_APPLICABLE` whose target is an organism term, so either disposition passes the gate. I would either (a) extend the `NOT_APPLICABLE` rationale to cover specimen forms and record it as such, with `GENEPIO:0100943` / `GENEPIO:0100934` as xrefs — this is the claim the evidence actually supports; or (b) keep `CONFIRM_UNGROUNDED` but **rewrite the note**, since "A sediment or ice core is a real habitat" conflates the sediment (a habitat) with the core (a specimen of it), and the same 60 strains' habitats are already tagged elsewhere in BacDive. Failing both, (c) `REVIEW`, flagging that the disposition turns on a policy question — does HabitatMech admit specimen-form concepts — that is broader than this one record.

Whichever is chosen, the `NCIT:C180316` rejection in the existing note is correct and should be preserved.

## Citations

1. https://publications.iodp.org/proceedings/374/102/374_102.html
2. https://publications.iodp.org/proceedings/320_321/102/102_3.htm
3. https://www.ebi.ac.uk/ols4/ontologies/genepio/classes?obo_id=GENEPIO:0100943
4. https://doi.org/10.1093/nar/gky879
5. https://doi.org/10.1093/nar/gkab961
6. https://bacdive.dsmz.de/isolation-sources
7. https://bacdive.dsmz.de/strain/24651
8. https://bacdive.dsmz.de/strain/132639
9. https://doi.org/10.1099/00207713-45-3-441
10. https://pubmed.ncbi.nlm.nih.gov/8590670/
11. https://www.dsmz.de/catalogues/details/culture/DSM-10276.html
12. https://doi.org/10.1128/AEM.02473-08
13. https://doi.org/10.1099/ijsem.0.001275
14. https://pubmed.ncbi.nlm.nih.gov/27381468/
15. https://doi.org/10.1099/ijs.0.050468-0
16. https://pubmed.ncbi.nlm.nih.gov/23606483/
17. https://doi.org/10.1099/ijsem.0.002252
18. https://pubmed.ncbi.nlm.nih.gov/28901899/
19. https://doi.org/10.1099/ijsem.0.001266
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC6680632/
21. https://genomicsstandardsconsortium.github.io/mixs/0000998/
22. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002226
23. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00000026
24. https://www.ebi.ac.uk/ols4/ontologies/snomed/classes?obo_id=SNOMED:430970004
25. https://www.ebi.ac.uk/ols4/ontologies/ncit/classes?obo_id=NCIT:C159488
26. https://www.ebi.ac.uk/ols4/ontologies/genepio/classes?obo_id=GENEPIO:0001246
27. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00010483
28. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001530
29. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01000293
30. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002007
31. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:03000033
32. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002113
33. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:03600016
34. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002056
35. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00001998
36. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001046
37. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01000941
38. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001776
39. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:00002184
40. https://www.ebi.ac.uk/ols4/ontologies/ncit/classes?obo_id=NCIT:C180316
41. https://www.ebi.ac.uk/ols4/ontologies/genepio/classes?obo_id=GENEPIO:0100934
42. https://genomicsstandardsconsortium.github.io/mixs/0016015/
43. https://pmc.ncbi.nlm.nih.gov/articles/PMC3820981/
44. https://doi.org/10.1128/AEM.71.2.1035-1041.2005
45. https://doi.org/10.1073/pnas.1203849109
46. https://doi.org/10.1126/science.abd7934
47. https://doi.org/10.1038/s41561-018-0221-6
48. https://doi.org/10.1038/nrmicro3262
49. https://doi.org/10.1186/s40793-016-0203-5
50. https://doi.org/10.1038/nbt.1823
51. https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
52. https://www.dsmz.de/collection/catalogue/details/culture/DSM-10277