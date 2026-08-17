# ENVO and FoodOn term-request process, and mapping-set validation

Run 2026-08-16 with Claude Code's `/deep-research` workflow: five parallel search
angles, 24 sources fetched, 120 claims extracted, 25 verified by three-vote adversarial
verification, 106 agent calls. **11 claims survived; 11 were killed.**

This is committed because three merged PRs rest on it — #104, #105 and #115 — and
without it their reasoning is only a summary in a commit message. It is a snapshot:
ENVO's wiki and FoodOn's templates can change, and several findings below are already
flagged as time-sensitive.

**Superseded in part.** HabitatMech is now intended to supersede ENVO for microbial
habitats (#115), so the submission-process findings no longer describe anything the
project plans to do. They are kept because the OBO *conventions* they document —
definition form, provenance, ROBOT/DOSDP tooling — still govern how this repo writes its
own terms.

## Question asked

```
How should a LinkML knowledge base of microbial habitats (HabitatMech, grounded in
ENVO/FOODON/UBERON/BTO/PO) resolve two curation problems?
```

## Summary

On PROBLEM 1 the evidence is clear and almost entirely primary: there is no central OBO
submission portal, so HabitatMech's 863 ungrounded records must go to
EnvironmentOntology/envo and FoodOntology/foodon as issues on those trackers — but both
ontologies sanction batching rather than one issue per term. ENVO documents a ROBOT-
template batch route (one issue stating scope/motivation with literature references,
plus a filled copy of ENVO's template Google Sheet linked back in the issue, compiled by
ENVO editors with robot template/merge), while FoodOn's live NTR template explicitly
permits multiple closely-related terms per issue but offers no spreadsheet channel. The
per-term payload is fully enumerable and should be generated from data/raw/ rather than
hand-authored: label (lowercase), parent class, an Aristotelian genus-differentia
definition whose genus is the verbatim label of the asserted parent, four SKOS synonym
slots, URL/URI/IRI definition citations, ISO creation date, and pipe-delimited full
ORCID IRIs — which for composites like "Mangrove sediment" forces an explicit parent
choice (e.g. marine sediment ENVO:00002113) instead of an adjective-modified genus.
Formulaic families ("X sediment", "X soil", "environment associated with X") fit DOSDP —
ENVO maintains 18 live patterns including biome.yaml, ecosystem.yaml and
soil_by_property.yaml — while bespoke one-offs like "Spacecraft Assembly Cleanroom" fit
a ROBOT template; and ENVO's MIxS guidance means a host-associated gap may not be an
ENVO request at all, since PO and UBERON terms are sanctioned directly. PROBLEM 2 (the
sampling argument for 1,720 machine-generated mappings) is NOT addressed by any
surviving claim — zero of the 14 touch sampling statistics, published mapping error
rates, or SSSOM — so that half of the brief remains open.

## Confirmed findings (11)

### 1. There is no central OBO term-submission portal: requests go to each ontology's own GitHub issue tracker, so Ha

**Confidence:** high — vote 3-0

There is no central OBO term-submission portal: requests go to each ontology's own
GitHub issue tracker, so HabitatMech files at EnvironmentOntology/envo and
FoodOntology/foodon separately. FoodOn ships an NTR issue template; ENVO ships none (no
.github/ISSUE_TEMPLATE directory), so ENVO requests are free-form issues governed by its
wiki.

**Evidence.**

OBO Foundry's FAQ directs users to "the issue tracker of the [appropriate] ontology";
Principle 20 makes a public per-ontology tracker mandatory and requires its URL in
ontology metadata. ENVO's README: "Please use this GitHub repository's Issue tracker to
request new terms/classes." Verifier confirmed via the GitHub contents API that FoodOn
has exactly one issue template (new-term-request--ntr-.md, 830 bytes, no config.yml) and
that ENVO's .github contains only `workflows` — ENVO/.github/ISSUE_TEMPLATE returns 404.
The central OBOFoundry.github.io tracker is scoped to new-ontology and PURL/namespace
registration, not terms. Do not assert that an ENVO NTR issue template exists.

- <https://oboacademy.github.io/obook/lesson/contributing-to-obo-ontologies/>
- <https://obofoundry.org/faq/how-do-i-request-a-term.html>
- <https://obofoundry.org/principles/fp-020-responsiveness.html>
- <https://github.com/FoodOntology/foodon/blob/master/.github/ISSUE_TEMPLATE/new-term-request--ntr-.md>
- <https://github.com/EnvironmentOntology/envo>

### 2. ENVO sanctions BATCH new-term requests via a documented ROBOT-template workflow — one GitHub issue documenting

**Confidence:** medium — vote 2-1

ENVO sanctions BATCH new-term requests via a documented ROBOT-template workflow — one
GitHub issue documenting scope and motivation with literature references, then a copy of
ENVO's template Google Sheet filled in and linked back in the issue; ENVO engineers do
the robot template/merge/PR steps. This, not 863 separate issues, is the route for a
corpus-scale request.

**Evidence.**

Verbatim: "If you are interested in submitting a batch of term requests, create a new
ENVO github issue... thoroughly document the scope and motivation for the new terms
including references to appropriate literature", then copy the ENVO template sheet
(docs.google.com/spreadsheets/d/1K5GWxpSF2s397FMjdb9nGicC8xl10Xd1-M3-4fOnCts) and "add
the link to the new template google sheet in the github issue". Not vaporware: ENVO
issues #1063, #1070, #1089, #1091 exercise it (#1063 cites the wiki page by name). TWO
WEAKNESSES that drove the split vote: (1) the page was last edited 2022-08-11 and
observed usage clusters in 2020-21, with no post-2022 batch issue found; ENVO's
CONTRIBUTING.md never mentions batch requests, ROBOT templates, or the sheet, so a
newcomer would not discover this route. (2) The source gives NO batch-size guidance —
"hundreds at once" is extrapolation, and throughput is gated by ENVO engineer capacity
since editors perform the compile and merge. Confirm with ENVO editors in the opening
issue before assuming support at 863-term scale.

- <https://github.com/EnvironmentOntology/envo/wiki/ENVO-Robot-template-and-merge-workflow>
- <https://raw.githubusercontent.com/wiki/EnvironmentOntology/envo/ENVO-Robot-template-and-merge-workflow.md>
- <https://github.com/EnvironmentOntology/envo/issues/1070>
- <https://github.com/EnvironmentOntology/envo/issues/1063>

### 3. FoodOn's official NTR template explicitly permits multiple closely-related terms per issue, but there is no bu

**Confidence:** high — vote 3-0 (two merged claims)

FoodOn's official NTR template explicitly permits multiple closely-related terms per
issue, but there is no bulk/spreadsheet submission channel — and in practice the
template's fields are unenforced prompts rather than requirements.

**Evidence.**

The template's `about:` field (rendered on /issues/new/choose) reads: "You may request
more than one term per issue if the terms are closely related." Body sections: Parent
Term/Class {Label and Onto ID}; Definition "A {requested parent term} {which/during
which} is ..."; Definition Source; Exact/Narrow Synonym(s); Attribution (Name/ORCID).
Only Parent and Definition lack an "{If applicable}" hedge. Repo active (pushed
2026-08-10) though the template is unchanged since 2021-04-14; it is the only file in
.github/ISSUE_TEMPLATE and there is no config.yml, so no alternate bulk channel is
offered and blank issues remain enabled. Real precedent: issue #285 "NTRs: for 2023 USDA
Foundation Foods mapping" requested ~20 terms grouped by heading and closed in ~6 weeks.
Enforcement is nil — #285 gave parents by label only with no IDs or definitions, #297
was a two-word body, and #346 (2025) used an entirely different field set. Write "the
template prompts for", not "requires". Relevant to HabitatMech's "Fermented vegetables"
class of records.

- <https://github.com/FoodOntology/foodon/blob/master/.github/ISSUE_TEMPLATE/new-term-request--ntr-.md>
- <https://github.com/FoodOntology/foodon/issues/285>
- <https://github.com/FoodOntology/foodon/issues/346>
- <https://oboacademy.github.io/obook/howto/term-request/>

### 4. Both ontologies expect an Aristotelian genus-differentia definition, and ENVO adds a constraint that makes com

**Confidence:** high — vote 3-0 (three merged claims)

Both ontologies expect an Aristotelian genus-differentia definition, and ENVO adds a
constraint that makes composite habitat labels non-trivial: the genus MUST be the exact
term label of the asserted superclass and SHOULD NOT be adjective-modified outside the
differentia. So "Mangrove sediment" cannot be defined as "A marine sediment which..."
unless marine sediment (ENVO:00002113) is literally the asserted parent.

**Evidence.**

ENVO wiki: "All definitions MUST be of one of the following forms: A `B` which `Cs` ...
A `B` during which `C`"; "`B` MUST be the exact term label of the superclass"; "`B`
SHOULD NOT be modified with an adjective... Bad form: `A green B which Cs`. Good form:
`A B which is 1) green and 2) Cs`". Multiple differentiae may be a numbered list, but
the page warns "if there are many such differentiae in one definition, it may be a sign
that you should create some intermediate classes" — directly relevant to "Tree
plantation soil" and "Mangrove sediment". The definition exercise determines the parent:
"Doing this exercise helps both to formulate a concise and simple definition as well as
determine the appropriate parent class." OBO FP-006 is looser (definitions MUST be
unique-within-ontology and in English; Aristotelian form only SHOULD, "where this is
practical"), so ENVO is stricter than the OBO baseline and FoodOn looser — do not
generalize ENVO's exact-label rule to FoodOn. Caveats: the ENVO definitions page carries
an UNDER CONSTRUCTION banner, was last revised 2021-03-01, and concedes "quite a lot of
legacy content... doesn't follow the guidance"; the exact-label rule is MUST while the
no-adjective rule is only SHOULD NOT; ENVO prescribes two forms, not one; and ENVO's
ROBOT sheet has no separate genus column — the constraint is on the genus position in
the definition string matching the parent-class column.

- <https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions>
- <https://raw.githubusercontent.com/wiki/EnvironmentOntology/envo/Creating-good-definitions.md>
- <https://github.com/EnvironmentOntology/envo/wiki/ENVO-Robot-template-and-merge-workflow>
- <https://obofoundry.org/principles/fp-006-textual-definitions.html>
- <https://github.com/FoodOntology/foodon/blob/master/.github/ISSUE_TEMPLATE/new-term-request--ntr-.md>

### 5. The per-term fields ENVO's batch sheet expects are fully enumerable, so HabitatMech can generate them from dat

**Confidence:** high — vote 3-0

The per-term fields ENVO's batch sheet expects are fully enumerable, so HabitatMech can
generate them from data/raw/ rather than hand-authoring: Ontology ID (ENVO: + 8 digits,
may be blank), label, parent class, definition, definition cross reference, comment,
comment cross reference, editors note, exact/broad/narrow/related synonym, in subset,
cross reference, subclass axiom (explicitly NOT asked of collaborators), creation date
(ISO timestamp), created by (pipe-delimited full ORCID IRIs).

**Evidence.**

Verified against the wiki's raw markdown (27,239 bytes): the "Example robot template"
header row is exactly "Ontology ID | label | parent class | definition | definition
cross reference | comment | comment cross reference | editors note | exact synonym |
broad synonym | narrow synonym | related synonym | in subset | cross reference |
subclass axiom | creation date | created by". Each format rule has its own section: IDs
"must start with `ENVO:` and be followed by eight digits"; labels lowercase except
proper nouns ("Taylor column", "WMO blizzard"); citations are URLs "delimited by a `|`
character without spaces"; four synonym slots "follow SKOS style (broader or narrow)
conventions"; creation date is "the output from isotimestamp.com" (e.g.
2020-11-18T20:22:03.870Z); created by must "use the full IRI for the ORCIDs e.g.,
`https://orcid.org/0000-0003-4808-4736` not just the digits". Two softenings: the ID
column "can be left blank" absent an assigned range, and "we **do not** ask our
collaborators to provide" subclass axioms. Row 1 headers are cosmetic — ROBOT parses row
2's template strings (e.g. `AL oboInOwl:hasNarrowSynonym@en SPLIT=|`, `AI
oboInOwl:hasDbXref SPLIT=|`).

- <https://raw.githubusercontent.com/wiki/EnvironmentOntology/envo/ENVO-Robot-template-and-merge-workflow.md>
- <https://github.com/EnvironmentOntology/envo/wiki/ENVO-Robot-template-and-merge-workflow>

### 6. ENVO requires citable provenance on every definition — URLs/URIs/IRIs to the sources used, and for a term requ

**Confidence:** high — vote 3-0

ENVO requires citable provenance on every definition — URLs/URIs/IRIs to the sources
used, and for a term request those citations MUST be stated in the issue; paraphrased
definitions SHOULD carry dbxref annotations and verbatim ones MUST use the IAO
definition-source property. ORCIDs may substitute when expert knowledge is the source.

**Evidence.**

"All definitions MUST include URLs, URIs, or IRIs to references which were used to
generate the definition"; "If requesting a new term, definition citations MUST be stated
in the corresponding issue"; paraphrased refs "SHOULD be added as database cross-
reference annotation properties"; verbatim definitions "MUST be cited using the IAO
definition source annotation property"; "Citations can also be ORCIDs... if human expert
knowledge was used" (with written consent). Confirmed on an independent mirror, so not a
single-fetch artifact. Two softenings: the dbxref branch is SHOULD, not MUST, and
"machine-resolvable" overstates it — the annotations guide permits non-dereferenceable
literals such as ISBNs. Practical consequence for HabitatMech: each of the 863 records
needs at least one citable source URL, and the existing GOLD/BacDive/PREGO/Madin
provenance only partly supplies this — a source attesting that a concept is *used* is
not a source supporting the *definition*.

- <https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions>
- <https://github.com/EnvironmentOntology/envo/wiki/A-guide-to-annotations-on-ENVO-classes-and-relations>
- <https://github-wiki-see.page/m/EnvironmentOntology/envo/wiki/Creating-good-definitions>

### 7. Batch term generation splits on regularity: DOSDP auto-generates labels/definitions/synonyms from pattern rule

**Confidence:** high — vote 3-0 (two merged claims)

Batch term generation splits on regularity: DOSDP auto-generates
labels/definitions/synonyms from pattern rules and suits formulaic families, while ROBOT
templates carry manually curated per-row annotations and suit bespoke terms. HabitatMech
should therefore propose "X sediment"/"X soil"/"environment associated with X" families
as pattern+TSV and one-offs like "Spacecraft Assembly Cleanroom" as ROBOT-template rows.

**Evidence.**

OBO Academy (verified against raw markdown): "DOSDP templates are more about generating
annotations and axioms, while ROBOT templates are more about curating annotations and
axioms... the average DOSDP user will not write their own labels, definitions and
synonyms... the average ROBOT template user will not want automatically generated
definitions." Its Summary states the same rules of thumb. DOSDP is defined as "a
templating system for documenting and generating new OWL classes" (spec paper: Osumi-
Sutherland et al., J Biomed Semantics 2017;8:18) and is live in ENVO specifically:
src/envo/patterns holds 18 YAML patterns including biome.yaml, ecosystem.yaml,
soil_by_property.yaml, coastal_subtype_of_feature.yaml, entity_attribute_location.yaml,
mine.yaml, power_plant.yaml, driven by CSVs in src/envo/modules. Not deprecated — ODK PR
#1347 upgraded dosdp-tools to 0.20 in June 2026. Three qualifications: (a) the split is
a tendency, not a capability boundary ("While both ROBOT and DOSDP can be used for
'curation'..."); (b) a second axis may dominate — DOSDP's community-
consensus/shareability value versus "DOSDP templates are really hard to change"; (c)
DOSDP presupposes the differentia already exists as a term, so it fits "X sediment" far
better than "Spacecraft Assembly Cleanroom". SCOPE LIMIT: DOSDP is ENVO's internal build
mechanism, not an external submission channel — an outside requester still goes through
the issue flow; DOSDP is the shape a batch is proposed in.

- <https://oboacademy.github.io/obook/lesson/templates-for-obo/>
- <https://raw.githubusercontent.com/OBOAcademy/obook/master/docs/lesson/templates-for-obo.md>
- <https://oboacademy.github.io/obook/tutorial/dosdp-overview/>
- <https://github.com/EnvironmentOntology/envo/tree/master/src/envo/patterns>
- <https://doi.org/10.1186/s13326-017-0126-0>

### 8. A ROBOT template row can encode the entire OBO new-term payload (ID, LABEL, TYPE, definition/synonyms via A/AL

**Confidence:** high — vote 3-0 (two merged claims)

A ROBOT template row can encode the entire OBO new-term payload (ID, LABEL, TYPE,
definition/synonyms via A/AL/AT/AI/AP annotation templates, genus-differentia logic via
SC %/EC % Manchester class expressions) and can be machine-validated before submission,
so HabitatMech can generate and QC the request table in its own pipeline. ROBOT
templates are an explicit extension of the published Quick Term Templates method, giving
a citable precedent for many-terms-at-once submission.

**Evidence.**

ROBOT docs (raw master branch): "If the template string starts with `C`, `SC`, `EC`, or
`DC` followed by a space and template string (e.g. `SC %`) then it will be interpreted
as a class expression" in Manchester Syntax; `A <prop>` for string annotations
(definition = `A IAO:0000115`, synonyms = `A oboInOwl:hasExactSynonym SPLIT=|`), with
AL/AT/AI/AP variants and axiom-level provenance (>A/>AT/>AL/>AI) all confirmed present.
Validation is real: `robot template` "will fail on the first error encountered",
`--force true` logs all row parse errors, `--errors <path>` emits a table with
A1-notation cell locations and rule-ID CURIEs. Lineage is ROBOT's own wording: "The
approach extends the QTT method described in Overcoming the ontology enrichment
bottleneck with Quick Term Templates" (Rocca-Serra et al., Applied Ontology 6(1):13-22,
2011, doi:10.3233/AO-2011-0086). FoodOn independently generates thousands of terms this
way. Two limits: robot template does NOT mint IDs in the target namespace — requests use
placeholder IDs and editors assign real ENVO/FOODON IDs at merge; and "machine-
validated" means parse/OWL/QC level (template errors, robot report, unsatisfiability),
not that a definition is genuinely Aristotelian or in scope. DOSDP is a co-equal
precedent, so say "a" citable precedent, not "the".

- <http://robot.obolibrary.org/template.html>
- <https://raw.githubusercontent.com/ontodev/robot/master/docs/template.md>
- <http://dx.doi.org/10.3233/AO-2011-0086>
- <https://foodon.org/design/robot-managed-vocabularies/>

### 9. A host-associated gap is not automatically an ENVO term request: ENVO states it will not import terms availabl

**Confidence:** medium — vote 3-0, but with a significant counterweight

A host-associated gap is not automatically an ENVO term request: ENVO states it will not
import terms available from ontologies it already interoperates with, and explicitly
sanctions using PO and UBERON terms in MIxS env_broad_scale/env_local_scale/env_medium
provided they fit the same logic. For host-associated samples it prescribes the host's
ecosystem as env_broad_scale and a UBERON/PO anatomical part as env_local_scale.

**Evidence.**

Verbatim (page updated 2025-03-25, ENVO's own docs): "ENVO won't have every term that
you need, and we wouldn't import terms from other ontologies that we already
interoperate with. Thus, you can use terms from other OBO ontologies (such as PO and
UBERON) in MIxS env_broad_scale, env_local_scale, or env_medium fields, as long as they
fit the same logic." Same page: for host-associated samples env_local_scale "should use
terms from an ontology such as UBERON or PO" (e.g. UBERON:0001457 skin of eyelid,
PO:0025143 tepal apex). Limits noted by the verifier: env_broad_scale is still expected
to be a subclass of biome (ENVO:00000428), and NCBITaxon/NCIT ports are explicitly
discouraged. THE COUNTERWEIGHT, and why this is medium not high: ENVO DOES maintain a
pre-coordinated "environment associated with X" branch — ENVO:01001000 environmental
system determined by an organism, 01001001 plant-associated environment, 01001002
animal-associated environment, 01001041 fungi-associated, 01001057 environment
associated with a plant part, 01001055 animal-part equivalent, 01001176/01001179
aquatic-invertebrate and cnidarian variants (verified live via OLS4) — and issue #1029
shows active demand to extend it. So "Phyllosphere" and "Diatoms (host-associated)"
plausibly ARE legitimate ENVO NTRs under that branch; a UBERON/PO anatomy term is an
anatomical entity, not an environment class, and the MIxS sanction covers annotation
field values, not necessarily grounding a habitat class in a third-party KB. The claim
survives only because it says "not necessarily".

- <https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS>
- <https://github.com/EnvironmentOntology/envo/issues/1029>
- <https://www.ebi.ac.uk/ols4/ontologies/envo/classes?short_form=ENVO_01001000>

### 10. The pre-coordination vs post-coordination question (brief part d) is NOT resolved: every strong claim assertin

**Confidence:** low — vote 0-3 on three separate post-coordination claims; 1-2 on a fourth

The pre-coordination vs post-coordination question (brief part d) is NOT resolved: every
strong claim asserting that ENVO recommends post-composition over minting composite
classes was refuted on verification, and no surviving claim covers how
MIxS/GSC/NMDC/MGnify/GOLD/BacDive handled the same gap.

**Evidence.**

Refuted 0-3: that ENVO "explicitly recommends post-composition rather than minting pre-
coordinated composite classes", with the specific patterns `ecosystem [ENVO:01001110]
and determined by (RO:0002507) some X` and `'environmental material' [ENVO:00010483] and
composed primarily of (RO:0002473) some X`; and that ENVO's lead editor declined to mint
pre-coordinated host-associated biome terms for ~6K biosamples and directed the
requester to post-coordination. Voted 1-2: that ENVO prescribes a three-part host
decomposition rather than a single pre-coordinated host-associated term. Read alongside
the confirmed existence of the pre-coordinated ENVO:01001000 branch, the honest reading
is that ENVO does both and no sourced general policy preference was established.
HabitatMech should not build its argument on a claimed ENVO post-coordination policy.
The comparative-practice sub-question (how GOLD, BacDive, NMDC, MGnify handle this) went
entirely unanswered.

- <https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS>
- <https://github.com/EnvironmentOntology/envo/issues/1029>

### 11. PROBLEM 2 — the sampling argument for the 1,720 machine-generated mappings — received no verified findings at 

**Confidence:** high — vote n/a (absence of coverage, not evidence of absence)

PROBLEM 2 — the sampling argument for the 1,720 machine-generated mappings — received no
verified findings at all in this research pass.

**Evidence.**

All 14 surviving claims and all 11 refuted claims concern term requests, OBO definition
conventions, and ROBOT/DOSDP tooling. Nothing addresses: Wilson vs Clopper-Pearson
intervals, sample-size determination, stratified sampling, or LQAS/acceptance sampling;
published error rates for UMLS, OxO, BioPortal, Mondo, or ChEBI mapping sets; SSSOM's
mapping_justification / confidence / curation_status slots or any SSSOM validation-by-
sampling workflow; or precedent for publishing a set as "machine-generated, sampled at N
with X% estimated error". The 836 EXACT / 884 NARROW split in HabitatMech is a natural
stratified-sampling frame and the two strata almost certainly carry very different error
rates — but that is my inference, not a sourced finding. This half of the brief needs a
second research pass.

## Refuted on verification (11)

Kept deliberately. A claim that looked right and did not survive is the part of a
research pass most easily re-derived by the next person.

1. ENVO mandates a fixed Aristotelian genus-differentia syntax for every new term
definition, restricted to two templates: "A B which Cs" or "A B during which C" — so a
HabitatMech term request must supply a definition in exactly that shape.

2. Definitions must be attached with the annotation property 'definition' (IAO:0000115) and
their provenance supplied via 'definition source' (IAO:0000119) or as an axiom
annotation carrying oboInOwl:hasDbXref (e.g. a PMID) — i.e. every requested term needs a
citable source, not just prose.

3. OBO Foundry explicitly endorses Dead Simple Ontology Design Patterns (DOSDPs) — YAML
design specifications — to generate both textual and logical definitions for whole
groups of terms, and states they are widely used in OBO ontologies such as Mondo and
uPheno. This is the sanctioned mechanism for batch/templated term generation rather than
one-off issue submission.

4. A well-formed OBO new-term request must supply a specific minimum payload: the intended
parent term's ID and label, a definition in the proper format, sources/cross-references
for any synonyms, and the requester's ORCID — so HabitatMech cannot submit bare labels
like "Solar salterns" or "Phyllosphere" and must pre-compute a parent CURIE and a
definition for each of the 863 ungrounded records.

5. ROBOT's `template` command is the official OBO-tooling route for bulk term creation: it
converts a spreadsheet (CSV/TSV) of proposed terms into OWL, so a batch of hundreds of
new-term requests can be authored as one table rather than as individual GitHub issues.

6. DOSDP term generation is driven by TSV tables in which each row specifies one class, so
a batch of many new terms (e.g. HabitatMech's 863 ungrounded records) can be proposed as
a single pattern plus a spreadsheet rather than as hundreds of separate issues.

7. A DOSDP YAML pattern generates the label, an exact synonym, a textual definition and an
OWL equivalence axiom from a single supplied filler term, meaning a term request
submitted as pattern + TSV data rows yields uniform genus-differentia-style definitions
across the whole batch without per-term definition writing.

8. ENVO's official term-request process for MIxS users is to open an issue on the ENVO
GitHub tracker including a definition citing relevant sources, and it explicitly routes
bulk/large submissions to a separate 'Adding classes to ENVO' procedure rather than the
ordinary issue tracker.

9. ENVO explicitly recommends post-composition rather than minting pre-coordinated
composite classes for environments defined by a non-ENVO entity, giving the concrete
patterns 'ecosystem [ENVO:01001110] and determined by (RO:0002507) some X' and
"'environmental material' [ENVO:00010483] and composed primarily of (RO:0002473) some
X".

10. For host-associated microbial samples ENVO prescribes a three-part decomposition — host
taxonomy in the MIxS host fields, the host's ecosystem as env_broad_scale, and an UBERON
or PO anatomical part as env_local_scale — rather than a single pre-coordinated 'host-
associated X' habitat term.

11. ENVO's lead editor explicitly declined to mint pre-coordinated 'host-associated biome' /
'plant-associated biome' style terms requested for ~6K biosamples, directing the
requester to post-coordinated annotation (ENVO triad plus MIxS host/taxon metadata
fields) instead — i.e. ENVO's stated policy is post-coordination over composite term
minting.

## Open questions

- Is ENVO's ROBOT-template batch workflow still actively supported in 2026, and what batch
size will ENVO editors accept in one request? The wiki page and its observed usage both
predate 2023 and CONTRIBUTING.md is silent, so this needs a direct question to ENVO
editors before HabitatMech commits to the route.
- For host-associated and built-environment records ('Phyllosphere', 'Diatoms (host-
associated)', 'Spacecraft Assembly Cleanroom'), does ENVO want new subclasses under the
existing pre-coordinated ENVO:01001000 'environmental system determined by an organism'
branch, or post-coordinated MIxS-triad annotation? Evidence exists for both and every
claim of a stated ENVO policy preference was refuted.
- What state do the 863 records occupy while requests are pending? ROBOT templates do not
mint target-namespace IDs, real CURIEs are assigned at merge, and this repo's GROUND
check requires the CURIE to exist in the vendored slice with a matching label — so what
provisional grounding does the seeder emit, and how is a merged ENVO release reconciled
back into data/raw/?
- Problem 2 in full: what sample size and interval method (Wilson vs Clopper-Pearson),
stratified how across the 836 EXACT and 884 NARROW strata, and what published precedent
exists for releasing a mapping set as 'machine-generated, sampled at N, X% estimated
error' with SSSOM mapping_justification and curation_status recorded accordingly?

## Sources

- [https://github.com/EnvironmentOntology/envo/wiki/ENVO-Robot-template-and-merge-workflow](https://github.com/EnvironmentOntology/envo/wiki/ENVO-Robot-template-and-merge-workflow)
- [https://github.com/FoodOntology/foodon/blob/master/.github/ISSUE_TEMPLATE/new-term-request--ntr-.md](https://github.com/FoodOntology/foodon/blob/master/.github/ISSUE_TEMPLATE/new-term-request--ntr-.md)
- [https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions](https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions)
- [https://obofoundry.org/principles/fp-006-textual-definitions.html](https://obofoundry.org/principles/fp-006-textual-definitions.html)
- [https://oboacademy.github.io/obook/lesson/contributing-to-obo-ontologies/](https://oboacademy.github.io/obook/lesson/contributing-to-obo-ontologies/)
- [http://robot.obolibrary.org/template.html](http://robot.obolibrary.org/template.html)
- [https://oboacademy.github.io/obook/tutorial/dosdp-overview/](https://oboacademy.github.io/obook/tutorial/dosdp-overview/)
- [https://oboacademy.github.io/obook/lesson/templates-for-obo/](https://oboacademy.github.io/obook/lesson/templates-for-obo/)
- [https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS)
- [https://github.com/EnvironmentOntology/envo/issues/1029](https://github.com/EnvironmentOntology/envo/issues/1029)
- [https://github.com/EnvironmentOntology/envo/issues/792](https://github.com/EnvironmentOntology/envo/issues/792)
- [https://academic.oup.com/nar/article/50/D1/D828/6414581](https://academic.oup.com/nar/article/50/D1/D828/6414581)
- [https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/)
- [https://github.com/EnvironmentOntology/envo/wiki/Adding-classes-to-ENVO](https://github.com/EnvironmentOntology/envo/wiki/Adding-classes-to-ENVO)
- [https://arxiv.org/abs/2405.11919](https://arxiv.org/abs/2405.11919)
- [https://arxiv.org/abs/2209.04732](https://arxiv.org/abs/2209.04732)
- [https://arxiv.org/abs/2306.01198](https://arxiv.org/abs/2306.01198)
- [https://pmc.ncbi.nlm.nih.gov/articles/PMC9104662/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9104662/)
- [https://mapping-commons.github.io/sssom/mapping_justification/](https://mapping-commons.github.io/sssom/mapping_justification/)
- [https://arxiv.org/abs/2109.02516](https://arxiv.org/abs/2109.02516)
- [https://academic.oup.com/bioinformatics/article/39/4/btad130/7077133](https://academic.oup.com/bioinformatics/article/39/4/btad130/7077133)
- [https://academic.oup.com/database/article/doi/10.1093/database/baac035/6591806](https://academic.oup.com/database/article/doi/10.1093/database/baac035/6591806)
- [https://mapping-commons.github.io/sssom/tutorials/omop-mappings/](https://mapping-commons.github.io/sssom/tutorials/omop-mappings/)
- [https://mondo.readthedocs.io/en/stable/editors-guide/mappings/](https://mondo.readthedocs.io/en/stable/editors-guide/mappings/)
