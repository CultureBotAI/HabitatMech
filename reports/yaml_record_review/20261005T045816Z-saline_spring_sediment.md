# YAML Record Review: Saline spring sediment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/saline_spring_sediment.yaml`
- Started UTC: 2026-10-05T04:52:36Z
- Finished UTC: 2026-10-05T04:58:16Z
- Verdict: needs curation; 0 blocker, 2 major, 0 minor findings.

## Target

The complete generated HabitatRecord was read. Minted identifier
habitatmech:GOLD.7dbe12a9d1 denotes sediment from a saline spring, not the
spring landform or its groundwater. The record is AQUATIC, UNGROUNDED and
SEEDED, with one parent, one GOLD attestation and two history events.
Definition/source, synonyms, xrefs, parameters, taxa, evidence, causal graphs,
discussions and datasets are absent. PATHS.tsv:2216 preserves its stem.
No scientific input, generated output or history was edited.

## Validation

- `just validate data/habitats/aquatic/saline_spring_sediment.yaml`: pass.
- `just validate-strict data/habitats/aquatic/saline_spring_sediment.yaml`:
  pass, one file and zero errors.
- Complete build_corpus/build_document dictionary equality: pass; one
  contributing source concept, zero ITEM-reviewed sources, zero taxa and
  two history events. Reproducibility does not establish scientific validity.
- `just validate-products`: pass on the permitted retry; 1179 canonical
  labels, one synonym, five exceptions and 2054 no-adapter skips. Minted
  identity and missing scientific definition are not certified by that gate.
- `just worklist --status all --limit 5`: pass; 953 ungrounded concepts and
  1810 decisions. Exact target resolution was separately inspected.
- Initial QC and label commands exited 2 because the sandbox denied uv's
  existing cache. They did not execute their gates. Authorized retries used
  that cache; fresh full QC is live during tests at review close. Lint,
  documentation and raw provenance passed. Remaining corpus-wide gates are
  not claimed complete here. Log:
  /private/tmp/habitatmech-saline-spring-water-qc-retry-20261005.log.
- The previous publication's separate main-push QC 37265052305 reached
  SUCCESS before this review; it is not the fresh run.
- Actual full-context semantic text changes when the groundwater parent is
  removed. No map, site or scientific record was regenerated.

## Identity and Grounding

Actual source minting reproduces habitatmech:GOLD.7dbe12a9d1. Automatic
gold_unmatched resolution and the CONFIRM_UNGROUNDED row at
curation/decisions.tsv:743 retain the minted identity. That 2026-08-12
decision is CLASS-level and explicitly says habitat identity was not assessed.
The 2026-08-16 seed event and SEEDED status therefore accurately represent
the available review depth; neither is an ITEM-review claim.

Ignored-inclusive searches of the vendored ontology inventory and the
inspected typed ENVO snapshot found no spring-sediment label or synonym.
Current official OLS exact queries for saline spring sediment and spring
sediment returned zero hits. This is a bounded candidate search, not proof
that no ontology anywhere has such a term.

Current active [ENVO:00002007 sediment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002007)
is a defensible material genus, not an exact identity for every spring-qualified
sediment. [ENVO:01001893 salt spring](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001893)
has the exact synonym saline spring, but denotes the spring rather than its
sediment. [ENVO:00000027 spring](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000027)
denotes a landform, and [ENVO:01001004 groundwater](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001004)
denotes water in underground pore spaces. None is an exact identity substitute.
Physical ontology_terms.tsv rows are 7170, 9383, 6623 and 8499 respectively.

The saline-sediment search also returned ENVO:01001050 saline sediment
environment and ENVO:01001049 non-saline sediment environment. Both were
inspected in current OLS and typed OWL; they denote environmental systems,
not this spring-qualified material. ENVO:01001036 sediment permeated by
saline water, inspected separately at ontology_terms.tsv:8531 and in current
[OLS](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001036),
is a potentially tighter material genus when the intended class explicitly
requires saltwater-filled pore space. The present source row supplies no such
measurement or definition, so do not silently strengthen all spring deposits
to that condition. It too is broader than the spring-qualified identity.

The entire parent record was read as context only. Its minted
habitatmech:GOLD.22a80cbd14 identity is the qualified GOLD groundwater bin,
automatically NARROW under ENVO:01001004. Its 249 ORGANISM assertions do not
belong to the reviewed child. Actual parent-path resolution has no item-level
override; src/habitatmech/seed.py:898-907 contributes that link mechanically.
Even with the deep-subsurface qualifier preserved, groundwater is not a
strict broader material class for deposited sediment. The source path remains
useful provenance, but provenance does not turn water into the material's genus.

## Evidence

Physical data/raw/gold_ecosystem_paths.tsv:925 contains the depth-five path
Environmental > Aquatic > Deep subsurface > Groundwater > Saline spring
sediment, one node 7985 and one ORGANISM assertion. No collapsed-node note is
needed. Tree study/biosample counts are zero. All 14 raw inventories were
scanned for this exact path/node: no matching bulk biosample, API triad,
study, parameter, BacDive, PREGO or Madin contribution was found in that
bounded scan. Current official GOLD lookups for 7985 and the contextual
parent's 5953 returned 404, not proof that either identifier is retired.
The underlying one organism/accession and original sample chain remain
unrecovered; do not infer taxon identity from the habitat label.

Independent primary evidence supports this as a genuine microbial habitat.
The original [Perreault et al. study](https://doi.org/10.1128/AEM.00359-08),
PMID:18805995, PMC2583501, was inspected in its abstract and Site description
and sampling section. It separately sampled sediment and water from four
saline springs at Gypsum Hill and examined microbial communities. The
reported sediment sampling distinguished deposited material from the spring
water. PubMed EFetch confirmed the article title, PMID, PMCID and DOI.
That is evidence for the material/context distinction and microbial habitat
identity, not a link to the single GOLD organism or permission to generalize
one Arctic site's temperatures, salinity, taxa or metabolism to every saline
spring sediment.

The inspected primary [BioSample SAMN18613384](https://www.ncbi.nlm.nih.gov/biosample/SAMN18613384)
independently distinguishes local context saline spring from environmental
medium sediment and describes a single-cell sample from that material.
This is another bounded habitat example, not demonstrated membership in
GOLD node 7985, culture-isolation proof or an additional count to add to one.

The complete rendered page was inspected. Its unreviewed warning and
class-level curation wording are appropriate. It exposes the groundwater
link under broader habitats and has no definition, reflecting the same
scientific gaps rather than supplying independent evidence.

## Completeness

Ignored/hidden-inclusive searches covered the exact identifier, label and
stem across curation, conf, history, research, earlier individual reports,
raw inventories and PATHS/RETIRED. Only the class-level decision, source row
and stable-path entry were target-owned matches. No authored definition,
target causal overlay, separate history record or prior individual target
review was found in those surfaces. Other records' groundwater discussions
are context, not an individual review of this child.

An evidence-backed genus/differentia definition is consequential here: the
label remains the entire scientific description and the only parent is false.
In contrast, no exact evidence justifies filling optional chemistry, taxa,
datasets, discussions or causal graphs. iModulonDB is not applicable because
the target contains no gene/regulator/expression assertion; genes mentioned
in contextual literature were not imported as habitat mechanism evidence.

## Findings

| Severity | Finding | Maintained owner / scope |
| --- | --- | --- |
| Major | A real, source-qualified sediment habitat lacks an item-level identity ruling, defensible material genus and authored definition. CLASS-level confirmation did not assess these. | Exact row habitatmech:GOLD.7dbe12a9d1 in `curation/decisions.tsv` and a new keyed definition in `curation/term_requests.tsv`. |
| Major | The inherited groundwater parent is source context, not a strict broader class for spring sediment. | The same minted definition's explicit parent_mode=REPLACE; `src/habitatmech/seed.py` owns source-parent generation and definition application. |

No blocker or minor finding was established. The count reproduces correctly;
the unresolved original organism chain is not evidence that the count is false.

## Recommended Edits

1. Replace the CLASS-only ruling with an evidence-backed ITEM-level
   CONFIRM_UNGROUNDED decision, retaining this minted identity and attaching
   ENVO:00002007 sediment as a true broader class. Do not ground exactly to
   sediment, salt spring, groundwater or a saline environmental system.
2. Add a keyed authored definition, for example a sediment deposited in a
   saline spring, with source evidence and explicit scope in the notes. Use
   parent_mode=REPLACE only after recording that the sole inherited groundwater
   parent is false; add the true sediment genus. Retain AQUATIC category,
   full source path/node, one ORGANISM unit, stable stem and historical events.
3. Keep grounding UNGROUNDED when using this authored-definition path:
   src/habitatmech/curate/definitions.py rejects NARROW and ontology-owned
   terms. GROUND_AS_PARENT plus an authored term request would fail that
   guard. CONFIRM_UNGROUNDED with a verified parent and a definition is the
   supported route; do not weaken the guard or patch generated YAML.
4. Recover the original GOLD organism/sample chain separately if point-level
   ecology or a tighter pore-water genus is needed. Do not convert the two
   independent habitat examples into false provenance for node 7985.

## Follow-up Checks

For later authorized curation, add exact-source controls for retained minted
identity, ITEM review, accepted definition, true sediment genus, removed
groundwater parent, unchanged source count/unit and retained history. Append
required new history, dry-seed, then inspect a forced canary for
habitatmech:GOLD.7dbe12a9d1 before guarded wider regeneration. Never prune a
partial run. Run ordinary/strict schema, labels, provenance, history,
reproduction, site/redirect, term-request checks and full QC.

Parent removal changes actual full-context semantic input; a new definition
also needs comparison. Perform a genuine map/site refresh under #1217 and
preserve protected draft #1218/runtime pins. No SSSOM/KGX readiness claim
follows without inspecting actual products and current kg-microbe contracts.

## Additional Notes

Typed ENVO snapshot SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
Editorial OLS descriptions were distinguished from typed definitions.

All 570 open/closed GitHub issue titles and bodies were searched for the
exact source key, node and spring-sediment wording; no exact follow-up was
found. This is a bounded title/body search, not an assertion about every
comment. No GitHub mutation occurred during this individual review.
