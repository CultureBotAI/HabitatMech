---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T02:04:25.353268'
end_time: '2026-08-18T02:14:59.169856'
duration_seconds: 633.82
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Prepupa
  habitat_identifier: habitatmech:GOLD.ccdfcd10b9
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Arthropoda: Insects > Prepupa'
  assertions: '2'
  parent_terms: (none)
  xrefs: UBERON:0003142
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term UBERON:0003142 'prepupa' attached as a parent. Life-stage review\
    \ (#112), applying the rule #114 settled: the whole host ORGANISM gets its own\
    \ identity plus an <X>-associated environment term, while PARTS of a host ground\
    \ to the anatomy term as gut, skin and lung already do. A larva, pupa, prepupa\
    \ or embryo is the whole organism at a stage, not a part of one, so UBERON:0003142\
    \ 'prepupa' is the organism rather than the place \u2014 the same shape as Mollusca,\
    \ Porifera and the host clades. Kept as an xref (#99); the concept keeps its own\
    \ identity as a term-request candidate.This is the line that makes both calls\
    \ fall out of one rule, rather than an exception for terms that happen to live\
    \ in UBERON: a cocoon is a STRUCTURE an insect builds and stays grounded, because\
    \ it is not the organism. (source concept habitatmech:GOLD.ccdfcd10b9)"
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
  total_cost_usd: 3.061365499999999
  session_id: 5f896ba9-1ad9-4c5c-8cca-1c9f09ba30d8
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 28
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Prepupa
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.ccdfcd10b9
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Arthropoda: Insects > Prepupa
- **Upstream assertion volume:** 2
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** UBERON:0003142

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term UBERON:0003142 'prepupa' attached as a parent. Life-stage review (#112), applying the rule #114 settled: the whole host ORGANISM gets its own identity plus an <X>-associated environment term, while PARTS of a host ground to the anatomy term as gut, skin and lung already do. A larva, pupa, prepupa or embryo is the whole organism at a stage, not a part of one, so UBERON:0003142 'prepupa' is the organism rather than the place — the same shape as Mollusca, Porifera and the host clades. Kept as an xref (#99); the concept keeps its own identity as a term-request candidate.This is the line that makes both calls fall out of one rule, rather than an exception for terms that happen to live in UBERON: a cocoon is a STRUCTURE an insect builds and stays grounded, because it is not the organism. (source concept habitatmech:GOLD.ccdfcd10b9)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Prepupa** as a microbial habitat, with citations.

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

# Prepupa (`habitatmech:GOLD.ccdfcd10b9`) — definition research

## Proposed definition

> An insect-associated environment which is determined by a holometabolous insect in its prepupal phase — the non-feeding form, between the end of larval feeding and pupation, whose gut has been voided and which no longer takes in microbes from its growth substrate.

If the curator prefers to start from a term that already exists rather than from the record's own parent, the equivalent is: *An animal-associated environment (`ENVO:01001002`) which is determined by an insect in its prepupal phase …*. The first form is preferable for the same reason it was for `Larva`: the record's parent `habitatmech:GOLD.dba2a83b95` ("Arthropoda: Insects") already carries `ENVO:01001002`, so the insect restriction does not have to be repeated inside the differentia.

**One caveat the curator must decide before writing that sentence:** "prepupa" names three non-equivalent things across insect orders (§1), and GOLD's path gives no disambiguation beyond "Insects". The sentence above deliberately uses the *functional* reading (post-feeding, pre-pupal, gut voided), which is the only one that covers all three. If the curator instead adopts UBERON's strict reading ("start marked by pupariation"), the definition silently excludes the Hymenoptera and applied-entomology usages that most published "prepupa" microbiome sampling actually belongs to.

---

## 1. What the concept denotes

**The thing sampled is an insect host that is at the prepupal phase of development, treated as the place the microbes live** — not the phase as an interval of time, and not the cocoon, cell or substrate around it.

### The source path settles the modelling, not the biology

Verified against `data/raw/gold_ecosystem_paths.tsv`:

| Path | GOLD nodes | Assertions (ORGANISM) |
|---|---|---|
| `… > Insects > Prepupa` | 3 (`gold.ecosystem:7175`, `7370`, `7371`) | **2** |
| `… > Insects > Prepupa > Gut` | 2 | 0 |
| `… > Insects > Prepupa > Whole body` | 2 | 0 |

Siblings at the same level: `Larva` (94), `Nymph/Instar` (3), `Pupa` (0), `Whole body` (60), `Head` (26), `Fat body` (2), `Digestive system` (203 + children). GOLD therefore treats `Prepupa` exactly as it treats `Larva` and the organ systems: a partition of the host body that is then cut finer into `Gut` and `Whole body` ([GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)). The concept is the prepupal host as a habitat; its gut is *inside* the concept, expressed as a child node.

**Boundaries.**

- **Inside:** the prepupa's body as sampled — voided gut lumen and gut wall (including retained meconium before it is expelled), haemolymph/haemocoel, fat body and bacteriomes, and the cuticular surface.
- **Immediately outside, and each a separate GOLD node:** `Larva` (still feeding), `Pupa`, `Nymph/Instar`, and — importantly — `Pupa > Cocoon` and `Pupa > Cocoon > Meconium`. GOLD hangs the cocoon and the meconium off **`Pupa`**, not off `Prepupa`, even though in most Hymenoptera the cocoon is spun *by the prepupa* and the meconium is voided *at the prepupal transition*. A curator writing this definition should not fold the cocoon into it; it is a structure the insect builds (`UBERON:0013198` cocoon, present in the vendored slice), and under the rule the decision note cites, a structure grounds normally while the organism does not.
- **Also outside:** the rearing substrate, soil cell, nest cell or brood provision the prepupa sits in, and the frass it leaves behind (`… > Digestive system > Hindgut > Frass`).
- **The 2 assertions are anonymous here.** `data/raw/` records the count and the node ids but not which organisms; I could not resolve `gold.ecosystem:7175/7370/7371` to studies. Whether these are black soldier fly, a bee, or something else is **unknown**, not inferred.

### The label is genuinely ambiguous — four readings

1. **Strict dipteran / UBERON reading.** `UBERON:0003142` "prepupa": *"An organism at the prepupal stage. … The start of the pre-pupal stage is marked by pupariation, and the end is marked by pupation."* ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0003142)). This is the *Drosophila*-derived reading: the animal inside the newly formed puparium, from puparium formation (the "white prepupa", `BTO:0001459`, a ~15-minute window) through larval–pupal apolysis to head eversion ~12 h after puparium formation at 25 °C. WPP is the standard t = 0 staging landmark in fly work ([PMC6101747](https://pmc.ncbi.nlm.nih.gov/articles/PMC6101747/)).
2. **Applied / industry reading (the one most published "prepupa" microbiome sampling uses).** In *Hermetia illucens* the "prepupa" is the last (6th) larval instar after it has stopped feeding, emptied its gut, darkened and begun migrating — a phase *within* an instar, defined on pigmentation, sclerotisation and length reduction rather than on any moult. It is separated experimentally by exactly those criteria ([Bruno et al., *Insects*, PMC8879302](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8879302/)). Recent morphological work is blunt that this usage generates errors, because in Stratiomyidae the pupa forms inside the retained last-larval cuticle and authors routinely mislabel the last instar as a pupa ([*Transformations of Head Structures During the Larval Development of the Black Soldier Fly*, 2025, PMC11992506](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11992506/); [Barros et al., *J. Insect Sci.* 14:83, 2014](https://academic.oup.com/jinsectscience/article/14/1/83/2386555)). Note this reading is **incompatible with UBERON's**: no pupariation has occurred.
3. **Hymenopteran reading.** "Prepupa" = the post-defecating, non-feeding final-instar larva, usually inside a cocoon or earth cell; in Symphyta the same animal is called the **eonymph** (and, after a further transformation in Pamphiliidae, the pronymph), and it is the overwintering stage of most sawflies ([Sawfly glossary, sawflies.org.uk](https://www.sawflies.org.uk/wp-content/uploads/2021/01/Sawfly-Glossary.pdf); [Battisti, *Ent. Exp. Appl.* 1994, doi:10.1111/j.1570-7458.1994.tb00738.x](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1570-7458.1994.tb00738.x)). This is the reading behind the megachilid and *Anthophora* literature below, and it is where the stage can last **months** rather than hours.
4. **Thysanopteran reading — out of scope, but the label does not exclude it.** Thrips are neometabolous, not holometabolous; their "prepupa" (= "propupa") is a quiescent, mobile, wing-budded instar following two feeding larval instars ([UC IPM](https://ipm.ucanr.edu/natural-enemies/franklinothrips-predatory-thrips/); [E93 in neometabolous thrips, PMC8297894](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8297894/)). If the definition says "holometabolous", thrips are excluded — which is probably right but is a decision, not a given.

**My inference, flagged as such:** restricting the record to Holometabola. GOLD's sibling `Nymph/Instar` node absorbs hemimetabolous immatures, so the holometabolous reading of `Prepupa` follows structurally; GOLD itself states nothing. A curator who wants to avoid the inference can write "an insect in its prepupal phase — the non-feeding form between the last feeding larval instar and the pupa" and drop "holometabolous".

---

## 2. Genus — the broader kind

**Smallest well-established kind: an insect-associated environment. No ontology term expresses it.**

- **`habitatmech:GOLD.dba2a83b95` "Arthropoda: Insects"** — already this record's `parent_habitats` entry, itself UNGROUNDED. This is the right genus, and its being a HabitatMech mint is consistent: the whole family of insect-host habitat classes is absent from ENVO.
- **`ENVO:01001002` "animal-associated environment"** — *"An environmental system determined by an animal"* (verified in `data/raw/ontology_terms.tsv`). The nearest **existing** genus; correct but two steps too broad on the taxon axis and silent on stage.

**Near-misses, and why each fails:**

| Term | Status | Why it fails |
|---|---|---|
| `UBERON:0003142` **prepupa** (currently the record's `xref`) | organism class | *"An organism at the prepupal stage"*; in the vendored slice it is `rdfs:subClassOf UBERON:0000468` **multicellular organism** — the same parent as `UBERON:0002548` larva and `UBERON:0003143` pupa. An organism, not a place. Correctly held as `relation: xref` under #114. Also carries the pupariation commitment that reading 2 and reading 3 violate. |
| `BTO:0001110` **prepupa** | **in the vendored slice**, `subClassOf BTO:0001143` | *"1: An inactive stage just before the pupa in the development of certain insects. 2: The form of an insect in this stage."* — a term that is explicitly ambiguous between a stage and an organism. **This is the term the corpus has to explain itself about** (see §6): it is the exact structural analogue of `BTO:0000954` "nymph", which the corpus *does* ground. |
| `BTO:0001459` **white prepupa** | in the slice, `subClassOf BTO:0001110` | Narrower than the concept by a wide margin — a 15-minute *Drosophila* window. |
| `UBERON:0000069` **larval stage** / an analogous "prepupal stage" | stage class | A temporal occurrent, not a material entity. Worse than the organism reading, not better. No "prepupal stage" occurrent term is present in the vendored slice. |
| `ENVO:01001055` **environment associated with an animal part or small animal** — *"determined by part of a living or dead animal, or a whole small animal"* | genuinely broader | The most tempting near-miss, since a prepupa **is** a whole small animal. Two objections, both raised previously on `Larva`: it is a disjunctive class that also covers detached parts, and in the slice it sits under `ENVO:01001110` **ecosystem** (*"includes both living and non-living components"*), importing a commitment GOLD's node never makes. Defensible as an *additional* parent; not an identity. |
| `ENVO:01001176` **environment associated with an aquatic invertebrate** | narrower on an axis the concept lacks | Right for a chironomid, wrong for a sawfly eonymph in soil. Structurally useful, though: in the slice it is `subClassOf` **both** `ENVO:01001002` and `ENVO:01001055`, which is the multi-parent shape an "insect-associated environment" request should take. |
| `ENVO:01001001` plant-associated, `ENVO:01001041` fungi-associated, `ENVO:01001179` cnidarian-associated | sibling patterns | Wrong taxon. Their existence is the argument that ENVO accepts taxon-scoped `<X>-associated environment` classes and has simply never minted an arthropod one. |
| `UBERON:0013198` **cocoon** | in the slice | A structure the prepupa builds, not the prepupa. Grounds normally in its own right; GOLD in fact files `Cocoon` under `Pupa`. Do not use it here. |
| `ENVO:02000004` nesting material, `ENVO:2000006` nest of termite, `ENVO:00005804` nest of ant | habitations | Neighbouring habitats a prepupa may sit inside. Not the prepupa. |

Direct ENVO searches for `insect`- and `arthropod`-scoped **environment** classes return nothing usable: the only ENVO hits are `ENVO:01001636` "insect conservation process" (a process), `ENVO:03510022` resin varnish, and `NCBITaxon` cross-listings ([OLS4 ENVO search](https://www.ebi.ac.uk/ols4/ontologies/envo)).

---

## 3. Differentia — what distinguishes it from its siblings

Ranked by observability, and by how well each separates `Prepupa` from `Larva`, `Pupa` and `Nymph/Instar`. The three sibling life-stage nodes cannot be told apart by *which* microbes are present — they are told apart by the host's feeding state and gut contents, which is what a definition should use.

**(a) The host has stopped feeding and voided its gut — so the habitat is microbially depleted relative to the larva. This is the strongest and most measurable differentia.** In *H. illucens* reared on chicken feed, prepupae showed significantly lower total viable counts, *Enterobacteriaceae*, lactic acid bacteria and fungi than larvae (p ≤ 0.003), which the authors attribute directly to "cessation of feeding and starting to empty their digestive tract towards pupation"; *E. coli* declined steadily to the prepupal stage (< 1.1 ± 0.3 log cfu/g) and fell below detection from the end of the pupal stage on ([Van Looveren et al., *Animal Microbiome*, 2024, doi:10.1186/s42523-024-00317-4](https://pmc.ncbi.nlm.nih.gov/articles/PMC11129375/)). The same study found composition at the prepupal stage still closely tracking the larval community (*Enterococcus*, *Scrofimicrobium* predominant) before diversifying (*Proteus*, *Providencia*, *Sporosarcina*) — i.e. **prepupa is compositionally larva-like but quantitatively depleted**, which is exactly a differentia and not a separate community type.

**(b) The host is physically decoupled from its growth substrate.** Larval communities track the rearing medium; the prepupa leaves it. BSF prepupae migrate out of the wet substrate toward a dry pupation site — the behaviour industrial rearing exploits as "self-harvesting" ([Bruno et al., *Insects*, PMC8879302](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8879302/)); sawfly eonymphs burrow into soil or spin cocoons in litter ([sawflies.org.uk glossary](https://www.sawflies.org.uk/wp-content/uploads/2021/01/Sawfly-Glossary.pdf)); megachilid prepupae are sealed in a cocoon in a brood cell. Microbial input from diet stops at this boundary. **This is the property that makes `Prepupa` a different habitat from `Larva` rather than an older `Larva`.**

**(c) A host-imposed antimicrobial regime switches on at this transition.** Rapid induction of bactericidal activity at the onset of pupation is documented across Holometabola and is best characterised in Lepidoptera, under 20-hydroxyecdysone control; hemimetabolous crickets show no equivalent induction ([Johnston & Rolff, *PLoS Pathogens* 11:e1005246, 2015, doi:10.1371/journal.ppat.1005246](https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1005246); [*Phil. Trans. R. Soc. B* 374:20190073, 2019, doi:10.1098/rstb.2019.0073](https://royalsocietypublishing.org/doi/10.1098/rstb.2019.0073)). Hammer & Moran frame the whole transition as a habitat catastrophe for the resident microbes ([*Phil. Trans. R. Soc. B* 374:20190068, 2019, doi:10.1098/rstb.2019.0068](https://royalsocietypublishing.org/doi/10.1098/rstb.2019.0068)), and an 18-species comparison found significantly higher larva-to-adult community turnover in holometabolous than hemimetabolous hosts ([*Molecular Ecology*, 2022, doi:10.1111/mec.16673](https://onlinelibrary.wiley.com/doi/10.1111/mec.16673)).

**(d) Gut anatomy itself changes at this point in some clades.** In honey bees the larva has only a midgut, which connects to the hindgut at the pre-pupal stage — the event that permits defecation of the meconium ([Romero et al., *Insect Molecular Biology* 28:455–472, 2019, doi:10.1111/imb.12567](https://resjournals.onlinelibrary.wiley.com/doi/10.1111/imb.12567), a review). Adult *Apis* workers carry a large characteristic BFG microbiota concentrated in ileum and rectum, while larvae and newly emerged workers contain few or no bacteria ([Martinson, Moy & Moran, *Appl. Environ. Microbiol.* 78:2830–2840, 2012, doi:10.1128/AEM.07810-11](https://journals.asm.org/doi/10.1128/AEM.07810-11)); a within-hive comparison of 5th instar vs. black pupae reports Firmicutes dropping from ~70 % to ~40 % in favour of Gammaproteobacteria across larval defecation and pupation ([*BMC Microbiology* 2019, doi:10.1186/s12866-019-1490-y](https://link.springer.com/article/10.1186/s12866-019-1490-y)).

**(e) In the Hymenoptera reading, the prepupa is a long-duration, enclosed habitat in which microbes can proliferate rather than a brief transition — this is the case where "prepupa" is most clearly its own habitat.** In the solitary bee *Anthophora bomboides stanfordiana*, bacterial 16S copy number increased **33-fold** between early provisions and December diapausing prepupae, fungal abundance peaked at **52×** initial levels, and *Streptomyces* reached **48.5 %** relative abundance during overwintering (vs. 13.7 % in summer); *Streptomyces* isolates inhibited *Ascosphaera apis*, *Thelonectria* and *Aspergillus flavus* in vitro ([*ISME J* 18:wrae089, 20 May 2024, doi:10.1093/ismejo/wrae089](https://academic.oup.com/ismej/article/18/1/wrae089/7676633)). In *Megachile tosticauda*, *Acinetobacter* was abundant in feeding larvae and **largely absent from voided prepupae** ([*FEMS Microbiol. Ecol.* 101:fiaf023, 2025, doi:10.1093/femsec/fiaf023](https://academic.oup.com/femsec/article/101/4/fiaf023/8052006)) — an independent observation of the same gut-purge effect as (a).

**(f) It is the stage at which chalkbrood cadavers are formed** — i.e. the prepupa is the substrate for a well-described fungal habitat. *Ascosphaera* spp. germinate in the larval gut, replace the body contents with mycelium and produce a chalky mummy, typically in the late larval / cocooned prepupal phase; *A. aggregata* in *Megachile rotundata*, *A. torchioi* in *Osmia lignaria propinqua* ([*Environ. Entomol.* 21:1086, 1992](https://academic.oup.com/ee/article-abstract/21/5/1086/405520); [*BMC Ecol. Evol.* 15, 2015, doi:10.1186/s12862-015-0401-6](https://bmcecolevol.biomedcentral.com/articles/10.1186/s12862-015-0401-6)). Note the ontological wrinkle: a mummified prepupa is a **dead** small animal, which `ENVO:01001055` explicitly covers and `ENVO:01001002` arguably does not.

**Recommendation for the differentia clause:** use (a) + (b) — non-feeding, gut voided, separated from the growth substrate. Both are observable at sampling time, both hold under all three insect readings, and neither asserts a characteristic community. Leave (c)–(f) to `notes` and `causal_graphs`, where each edge carries its own evidence, as the schema requires.

**What must *not* go in the differentia:** any claim about which microbes a prepupa has. The BSF prepupa is a depleted larval community; the diapausing bee prepupa is a *Streptomyces*-dominated proliferating one; the honey bee prepupa is near-empty. There is no core prepupal microbiota to define the term by, and asserting one would be the unsupported sentence the brief warns against.

---

## 4. Sources

Ontology/vocabulary facts (each verified against `data/raw/ontology_terms.tsv` / `ontology_subclass_edges.tsv` in this repo, and against OLS4 where noted):

- `UBERON:0003142` prepupa, definition and `subClassOf UBERON:0000468` — [OLS4](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0003142)
- `BTO:0001110` prepupa; `BTO:0001459` white prepupa (`subClassOf BTO:0001110`); `BTO:0000954` nymph — vendored slice
- `ENVO:01001002`, `ENVO:01001055`, `ENVO:01001176`, `ENVO:01001001`, `ENVO:01001041`, `ENVO:01001179`, `ENVO:01001110` — vendored slice, confirmed via [OLS4 ENVO](https://www.ebi.ac.uk/ols4/ontologies/envo)
- `UBERON:0013198` cocoon; `UBERON:0002548` larva; `UBERON:0003143` pupa; `UBERON:0000069` larval stage — vendored slice
- `MIXS:0000251` "host life stage" (`host_life_stage`), *"Description of life stage of host"*, in the Agriculture / HostAssociated / PlantAssociated / SymbiontAssociated extensions; required in MIxS-SA — [GSC term page](https://genomicsstandardsconsortium.github.io/mixs/0000251/); [MIxS-SA, *ISME Communications* 2022, doi:10.1038/s43705-022-00092-w](https://www.nature.com/articles/s43705-022-00092-w)
- GOLD path structure and counts — `data/raw/gold_ecosystem_paths.tsv`; [GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)

Primary literature: Van Looveren et al. 2024 (doi:10.1186/s42523-024-00317-4); *ISME J* 18:wrae089 2024 (doi:10.1093/ismejo/wrae089); *FEMS Microbiol. Ecol.* 101:fiaf023 2025 (doi:10.1093/femsec/fiaf023); Brar et al., *Appl. Environ. Microbiol.* 2024 (doi:10.1128/aem.02076-23, [PMID 39136489](https://pubmed.ncbi.nlm.nih.gov/39136489/)) — sterile-pollen rearing produced no reduction in **prepupal weight**, i.e. the pollen microbiome is not required to reach the prepupal stage; Martinson et al. 2012 (doi:10.1128/AEM.07810-11); Johnston & Rolff 2015 (doi:10.1371/journal.ppat.1005246); Hammer & Moran 2019 (doi:10.1098/rstb.2019.0068); *Mol. Ecol.* 2022 (doi:10.1111/mec.16673); Barros et al. 2014 (*J. Insect Sci.* 14:83); Bruno et al. (PMC8879302); PMC11992506 (2025); Battisti 1994 (doi:10.1111/j.1570-7458.1994.tb00738.x).

**Explicitly marked as inference, not sourced:** (i) the Holometabola restriction (§1); (ii) the reading that GOLD's `Prepupa` is the union of the dipteran, hymenopteran and applied usages; (iii) the identity of the 2 organisms behind the assertions, which I could not resolve. **Sourced but secondary:** the claim that diapausing *M. rotundata* prepupae upregulate antimicrobial peptides and survive *E. coli* challenge better than non-diapausing ones appears in the [chromosome-level *M. rotundata* genome paper, PMC12199319](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12199319/) citing earlier work; I did not reach the primary study, so do not cite it as primary.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept:** prepupa; pre-pupa; prepupal larva; post-feeding larva; non-feeding last-instar larva; wandering-stage larva (Diptera); pharate pupa (strictly, reading 1 only); **eonymph** and **pronymph** (Hymenoptera: Symphyta — same animal, different vocabulary); "BSF prepupae" (industry, reading 2).

**Commonly but wrongly treated as the same thing:**

| Not the same | Why |
|---|---|
| **Pupa** (`UBERON:0003143`, GOLD `… > Insects > Pupa`) | The next stage and a separate GOLD node. Under UBERON's own definitions the boundary is larval–pupal apolysis / head eversion. Confounded constantly in Stratiomyidae, where the pupa sits inside the last-larval cuticle (PMC11992506). |
| **Last feeding instar / `Larva`** | The immediately preceding node (94 assertions). In the BSF literature the "prepupa" *is* the last instar, in a later phase — which means BSF papers using both words are cutting one GOLD node's worth of animal into two. Curator judgement call, worth a `notes` sentence. |
| **Puparium** | The hardened last-larval cuticle — a structure, not the animal. In Stratiomyidae it is calcium-carbonate impregnated. |
| **Cocoon** (`UBERON:0013198`) and **meconium** | Structures/materials the prepupa produces. GOLD files both under `Pupa`. Grounding a cocoon is right and routine; that is precisely the contrast the decision note draws. |
| **Thrips "prepupa"/"propupa"** | A quiescent, *mobile*, wing-budded instar of a **neometabolous** insect — not homologous, and excluded if the definition says "holometabolous" ([UC IPM](https://ipm.ucanr.edu/natural-enemies/franklinothrips-predatory-thrips/)). "Propupa" is essentially confined to thrips literature, "eonymph" to Symphyta. |
| **`UBERON:0000069` larval stage / "the prepupal stage"** | The interval of time, not the animal and not the place. |
| **The rearing substrate, brood provision, soil cell or frass** | Where the prepupa is, not what it is. Under GOLD these are separate nodes or `Environmental` paths entirely. |
| **"Prepupae" as feed/food** (`FOODON:00001177` insect food product) | Dried BSF prepupae as an aquafeed ingredient is a food-safety habitat, not the living host. Easy slip given the volume of that literature. |
| **`BTO:0001459` white prepupa** | A 15-minute *Drosophila* window, not the concept. |

---

## 6. Should this be a term at all?

**Yes — it is an organism acting as a place, which the corpus already treats as a habitat.** It is not a disease, quality, process or procedure, so `NOT_APPLICABLE` would be wrong. The existing disposition (UNGROUNDED, own identity, `UBERON:0003142` as `relation: xref`, term-request candidate) is consistent with #114/#112 and with the sibling `Larva`, `Pupa` and `Embryo` decisions. I would not change it.

Three things the curator should nonetheless record, because a reviewer will find them:

1. **The corpus is currently inconsistent across these four siblings, and `BTO:0001110` is the proof.** `habitatmech:GOLD.71e7bb35e2` "Nymph/Instar" is `GROUND`ed to `BTO:0000954` "nymph" — a term whose definition is *"Any of various immature insects…"*, i.e. an organism at a stage, exactly like `BTO:0001110` "prepupa" (*"…2: The form of an insect in this stage"*), which is in the vendored slice and is not used. So the same kind of concept is grounded at `Nymph/Instar` and confirmed-ungrounded at `Prepupa`, `Larva`, `Pupa` and `Embryo`. Under the #114 rule the *nymph* grounding is the outlier and should be re-opened; under any other reading, `Prepupa` should ground to `BTO:0001110`. Either way it should be one rule, and it is worth a separate issue rather than a note buried on this record.
2. **The stage axis may be the wrong axis for a habitat vocabulary at all.** MIxS records host life stage as sample metadata (`MIXS:0000251`), required in MIxS-SA, not as an environment class. An arguable alternative disposition is: request **one** ENVO term, "insect-associated environment", and let `larva` / `prepupa` / `pupa` be expressed as that environment plus a `host life stage` value. That would replace four minted identifiers with one term and a metadata field. I am not recommending it over the current path — GOLD's node exists and has attestations, so the record must — but the term request should say why the stage is being lifted into the class hierarchy rather than left as metadata, or an ENVO reviewer will ask.
3. **Priority is low and should be stated.** 2 assertions, with 0 on both child nodes, against 94 for `Larva`. If a term request is filed, file it for the parent (`insect-associated environment`) first; `prepupa` is only defensible as a child of a term that does not yet exist.

---

## Sources

- [UBERON:0003142 prepupa — OLS4](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0003142)
- [ENVO — OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo)
- [GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification)
- [MIXS:0000251 host life stage](https://genomicsstandardsconsortium.github.io/mixs/0000251/)
- [MIxS-SA, *ISME Communications* 2022](https://www.nature.com/articles/s43705-022-00092-w)
- [Van Looveren et al., *Animal Microbiome* 2024 — microbial dynamics across BSF life stages](https://pmc.ncbi.nlm.nih.gov/articles/PMC11129375/)
- [*ISME J* 18:wrae089 (2024) — symbiotic bacteria and fungi proliferate in diapause in a solitary bee](https://academic.oup.com/ismej/article/18/1/wrae089/7676633)
- [*FEMS Microbiol. Ecol.* 101:fiaf023 (2025) — *Megachile tosticauda* through its life cycle](https://academic.oup.com/femsec/article/101/4/fiaf023/8052006)
- [Brar et al., *Appl. Environ. Microbiol.* 2024 — gut bacteria not critical in *M. rotundata*](https://journals.asm.org/doi/10.1128/aem.02076-23)
- [Martinson, Moy & Moran, *AEM* 2012 — establishment of characteristic gut bacteria in the honeybee worker](https://journals.asm.org/doi/10.1128/AEM.07810-11)
- [Romero et al., *Insect Mol. Biol.* 2019 — honey bee gut microbiota review](https://resjournals.onlinelibrary.wiley.com/doi/10.1111/imb.12567)
- [*BMC Microbiology* 2019 — in-hive variation, larvae and pupae](https://link.springer.com/article/10.1186/s12866-019-1490-y)
- [Hammer & Moran, *Phil. Trans. R. Soc. B* 2019 — metamorphosis and symbiosis](https://royalsocietypublishing.org/doi/10.1098/rstb.2019.0068)
- [*Phil. Trans. R. Soc. B* 2019 — gut immune regulation, holo- vs hemimetabolous](https://royalsocietypublishing.org/doi/10.1098/rstb.2019.0073)
- [Johnston & Rolff, *PLoS Pathogens* 2015 — host and symbiont jointly control gut microbiota](https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1005246)
- [*Molecular Ecology* 2022 — complete metamorphosis and microbiota turnover](https://onlinelibrary.wiley.com/doi/10.1111/mec.16673)
- [Barros et al., *J. Insect Sci.* 14:83 (2014) — intra-puparial development of *H. illucens*](https://academic.oup.com/jinsectscience/article/14/1/83/2386555)
- [PMC11992506 (2025) — head structure transformations and last-instar misidentification in BSF](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11992506/)
- [Bruno et al., *Insects* — prepupal locomotion and self-harvesting in BSF](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8879302/)
- [Sawfly glossary — eonymph / prepupa (sawflies.org.uk)](https://www.sawflies.org.uk/wp-content/uploads/2021/01/Sawfly-Glossary.pdf)
- [Battisti 1994 — voltinism and diapause in *Cephalcia arvensis*](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1570-7458.1994.tb00738.x)
- [UC IPM — *Franklinothrips*, thrips "prepupa"/"propupa"](https://ipm.ucanr.edu/natural-enemies/franklinothrips-predatory-thrips/)
- [PMC8297894 — E93 in neometabolous thrips](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8297894/)
- [*Environ. Entomol.* 21:1086 (1992) — *Ascosphaera torchioi* in *Osmia lignaria propinqua*](https://academic.oup.com/ee/article-abstract/21/5/1086/405520)
- [*BMC Ecol. Evol.* 2015 — *Ascosphaera* adaptations to the bee habitat](https://bmcecolevol.biomedcentral.com/articles/10.1186/s12862-015-0401-6)
- [PMC12199319 — *M. rotundata* chromosome-level genome (secondary source for diapause AMP upregulation)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12199319/)
- [PMC6101747 — white prepupa as staging landmark in *Drosophila*](https://pmc.ncbi.nlm.nih.gov/articles/PMC6101747/)

## Citations

1. https://gold.jgi.doe.gov/ecosystem_classification
2. https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0003142
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC6101747/
4. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8879302/
5. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11992506/
6. https://academic.oup.com/jinsectscience/article/14/1/83/2386555
7. https://www.sawflies.org.uk/wp-content/uploads/2021/01/Sawfly-Glossary.pdf
8. https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1570-7458.1994.tb00738.x
9. https://ipm.ucanr.edu/natural-enemies/franklinothrips-predatory-thrips/
10. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8297894/
11. https://www.ebi.ac.uk/ols4/ontologies/envo
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC11129375/
13. https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1005246
14. https://royalsocietypublishing.org/doi/10.1098/rstb.2019.0073
15. https://royalsocietypublishing.org/doi/10.1098/rstb.2019.0068
16. https://onlinelibrary.wiley.com/doi/10.1111/mec.16673
17. https://resjournals.onlinelibrary.wiley.com/doi/10.1111/imb.12567
18. https://journals.asm.org/doi/10.1128/AEM.07810-11
19. https://link.springer.com/article/10.1186/s12866-019-1490-y
20. https://academic.oup.com/ismej/article/18/1/wrae089/7676633
21. https://academic.oup.com/femsec/article/101/4/fiaf023/8052006
22. https://academic.oup.com/ee/article-abstract/21/5/1086/405520
23. https://bmcecolevol.biomedcentral.com/articles/10.1186/s12862-015-0401-6
24. https://genomicsstandardsconsortium.github.io/mixs/0000251/
25. https://www.nature.com/articles/s43705-022-00092-w
26. https://pubmed.ncbi.nlm.nih.gov/39136489/
27. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12199319/
28. https://journals.asm.org/doi/10.1128/aem.02076-23