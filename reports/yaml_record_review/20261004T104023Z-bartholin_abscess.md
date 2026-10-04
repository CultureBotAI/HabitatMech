# YAML Record Review: Bartholin abscess

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/bartholin_abscess.yaml`
- Started UTC: 2026-10-04T10:35:39Z
- Finished UTC: 2026-10-04T10:40:23Z
- Verdict: needs curation

## Target

The complete generated HabitatRecord was read:
`habitatmech:GOLD.cfa530990d`, Bartholin abscess, HOST_ASSOCIATED,
NOT_APPLICABLE, REVIEWED. It has one source-derived parent, one GOLD
attestation and two curation events. It has no definition, synonyms, xrefs,
taxa, parameters, evidence objects, graphs, datasets or discussions.

The actual `mint` of Host-associated > Mammals: Human > Reproductive system >
Vagina > Bartholin abscess reproduces the identifier. `PATHS.tsv:2818` pins
the stem. This target is not normal Bartholin gland, generic vaginal tissue,
a Bartholin cyst, or the separately modeled skin Abscess record.

## Validation

- `just validate data/habitats/host_associated/bartholin_abscess.yaml`: PASS,
  no issues.
- `just validate-strict data/habitats/host_associated/bartholin_abscess.yaml`:
  PASS, one file, zero errors.
- `just validate-products`: PASS in this unchanged-corpus session,
  1,179 canonical pairs, one synonym, five exceptions and 2,054 no-adapter
  skips. This minted excluded identity is outside the configured ontology
  surface; anatomy comparisons were separately checked against current OLS.
- `just worklist --status all --limit 5`: PASS, 953 ungrounded records and
  1,810 decisions. The limited preview is not the source of the exact-target
  decision or count checks below.
- `just qc` remains running at report completion. Lint, documentation and
  provenance passed; tests have passed the 93% progress marker but are not
  yet terminal. History, full corpus reproduction and site gates are not
  claimed complete. Log: `/private/tmp/habitatmech-bark-qc-20261004.log`.
  No invented focused check replaced these full-corpus gates.
- Read-only comparison using the actual `build_context` and `semantic_text`
  adapter confirms that removing the sole parent changes semantic input.
  No scientific input or generated record was changed.

## Identity and Grounding

`curation/decisions.tsv:1145` is ITEM NOT_APPLICABLE, dated 2026-08-12,
with the generic disease/intervention/sampling-artifact/filler rationale.
The generated NOT_APPLICABLE and REVIEWED states, decision event and August
16 seeding event faithfully reproduce that maintained input. REVIEWED is a
mechanical indication of ITEM coverage, not proof of the scientific decision.

The source label can denote a clinical condition, but an abscess can also be
a physical purulent microbial site. The primary source below directly samples
that material. This does not identify GOLD's ten historical organisms; it
does establish that the generic non-place rationale is insufficient without
a source-specific distinction between diagnosis, physical site and specimen.
The entire skin `abscess.yaml` comparison was read: it remains a minted
NARROW habitat. Its different treatment illustrates the existing family
question in #220, not an authorization to merge anatomical sites.

The complete `vagina__a4a4e1ad.yaml` parent is whole human Vagina,
`habitatmech:GOLD.1daee83236`, NARROW under UBERON:0000996. It has no
authored broader regional-environment definition. Current active
[UBERON:0000996](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUBERON_0000996)
denotes the fibromuscular vaginal tract. Neither an excluded condition nor a
localized purulent-site interpretation is a subtype of that whole organ.

Current BTO:0003115 and UBERON:0000460 are active major vestibular-gland
terms with Bartholin synonyms. Their definitions place the paired glands
adjacent to the vaginal opening; the inspected typed UBERON graph places
the gland under gland classes and relates it to external female genitalia.
This anatomical context does not make a gland or its abscess a kind of vagina.
The definitions/typed relations are comparison evidence, not proposed exact
abscess identities. UBERON:0000460 must not be silently adopted as the target.

`src/habitatmech/seed.py:898-907` adds the Vagina parent from GOLD nesting,
independently of the exclusion decision. The schema and curation guide require
strictly broader semantics for this contribution too. The retained source
breadcrumb does not justify an is-a edge.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:529` supplies the exact depth-five path,
one node 6356, ten organisms, zero direct studies/biosamples and total ten.
The generated source ID, full path and ORGANISM count match. These are not
ten species, ten clinical cases, or proof of any particular microbial taxon.
The parent's 475 ORGANISM assertions are not transferred to this target.

All 14 raw TSVs were parsed for the exact path, mint and Bartholin-abscess
label, including extra-column values. Only the exact GOLD tree row matched.
No exact-target bulk biosample, study crosswalk, triad, BacDive, PREGO, Madin,
parameter or isolation-mapping row was found. The original ten source
assignments therefore do not have recoverable specimen detail in these
retained tables. Current OLS returned 404 for path IRI 6356; this neither
invalidates the committed snapshot nor supplies a replacement interpretation.

The inspected original [clinical microbiology abstract](https://pubmed.ncbi.nlm.nih.gov/24084536/),
retrieved as official Europe PMC core metadata, verifies PMID:24084536 and
DOI:10.1097/AOG.0b013e3182a5f0de. Kessous and colleagues retrospectively
examined Bartholin gland abscess cases and explicitly report positive pus
cultures. That supports a physical microbial sampling-site alternative to a
diagnosis-only reading. It is not claimed as GOLD's source citation; its
patients, organisms, culture frequency and treatment conclusions are not
imported or generalized to the record.

The [official GOLD classification guide](https://gold.jgi.doe.gov/ecosystem_classification)
describes host-associated paths as collection surroundings. This supports
re-examining the precise sample/site interpretation, not automatically
reversing every abscess exclusion. Full source recovery remains necessary for
a defensible final disposition of this particular node.

## Completeness

Ignored-inclusive identifier, label, exact path and stem searches covered
curation, history, research, review reports, the research manifest, PATHS and
RETIRED. They found the exact ITEM decision but no target definition request,
causal overlay, separate history ledger, individual research/prior review or
retired URL. A missing later-style ledger for this legacy decision is not
independently a schema/history defect.

Empty taxa, parameters and graphs are appropriate until exact evidence and
maintained inputs support them. Do not import the clinical study's organisms
as GOLD taxa. No gene, locus, regulator or expression dataset is asserted;
iModulonDB is not applicable. Parent/reference reads do not count as reviews
of those other records.

## Findings

1. **Major: unresolved source-specific exclusion.** The generic ITEM
   NOT_APPLICABLE rationale does not address the supported physical abscess-
   site reading. Owner: `curation/decisions.tsv:1145`, informed by recovered
   original source assignments. Added as a new exact-target witness to existing
   [#220](https://github.com/CultureBotAI/HabitatMech/issues/220#issuecomment-5979105268).
2. **Major: unsupported whole-vagina superclass.** The source-parent pass
   asserts a strictly broader organ relation that neither plausible disposition
   supports. Owner: maintained source-parent handling in
   `src/habitatmech/seed.py` and a governed exact-source correction/exclusion.
   Filed as [#1371](https://github.com/CultureBotAI/HabitatMech/issues/1371).

Blockers: 0. Minors: 0. No copied count, status-generation or identifier
mismatch was found. Scientific input fidelity does not resolve these two
semantic findings.

## Recommended Edits

1. Recover the manifest-era organism/specimen assignments, then either retain
   exclusion with a source-specific diagnosis rationale or revise the ITEM
   decision to a supported physical-site interpretation. Preserve the mint
   and source specificity unless exact identity evidence warrants otherwise.
2. Correct or exclude this exact Vagina parent contribution independently of
   the final disposition. Do not hand-edit generated YAML, globally remove
   GOLD parents, replace location with an equivalence xref, or adopt whole
   Bartholin gland/whole vagina/generic Abscess as automatic identity.
3. Append new curation history for actual changes. Retain the original source
   path, node 6356 and ten-ORGANISM provenance; do not rewrite old history or
   use clinical-cohort counts as source totals.

## Follow-up Checks

Regress the exact source-parent edge and retained source/status behavior.
For a site-retaining decision, verify anatomy, specimen scope and any authored
genus separately; do not convert proximity or partonomy to is-a. Canary/reseed
and re-read the target; require strict schema, current ontology correspondence,
provenance, history, exact corpus reproduction and full QC.

The real full-context diagnostic drops `broader habitat: Vagina` after parent
removal, changing semantic text. A real map/site rebuild is therefore required
for that correction. #1217 remains OPEN and documents the supported-runtime
constraint. Protected draft #1218 remains OPEN/DRAFT at
`18c93452a789218f5c653d02723d11388d972055` and was not modified. Do not fake
hashes, change pins or weaken freshness gates to implement a scientific fix.

## Additional Notes

All 513 returned issue bodies were screened; #220, #1327 and #1333 plus
their returned comments were inspected. A GitHub title/body/comment search
for Bartholin returned zero existing issues before filing. #1333 concerns
anterior fornix and #1327 concerns large-intestine abscess parents; neither
already owned this exact edge. The disposition finding belongs in #220,
so no duplicate disposition issue was created.

The Japanese abscess paper PMC1233935 was only a search lead: official
full-text XML returned HTTP 500, and a restrictive title query returned zero.
Neither failure is biological evidence; its search excerpt was not used as
the support for the findings. The successfully inspected 2013 primary
abstract supplies the direct pus-culture evidence. Only this new review
report was added to the repo; scientific issues remain open and unimplemented.
