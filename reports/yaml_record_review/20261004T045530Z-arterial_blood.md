# YAML Record Review: arterial blood

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/arterial_blood.yaml`
- Started UTC: 2026-10-04T04:51:35Z
- Finished UTC: 2026-10-04T04:55:30Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord `BTO:0006188`: HOST_ASSOCIATED,
EXACT, REVIEWED, BTO definition, one source synonym, two parents, one
GOLD attestation and two events. `PATHS.tsv:424` pins the slug and
`RETIRED.tsv:25` preserves the former source URL. Actual `mint` reproduces
the former key `habitatmech:GOLD.b183820c16` from its mammal blood path.

## Validation

- `just validate data/habitats/host_associated/arterial_blood.yaml`: passed.
- `just validate-strict data/habitats/host_associated/arterial_blood.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed, 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Reused full CI QC 37177414332 on baseline commit
  `99d607932ced42eb6be1a3ef7527b2271baf85ef`: 457 passed, three skipped,
  two dependency warnings; corpus reproduced exactly and all gates passed.
  Post-push QC 37177807654 also passed. Scientific files remain unchanged;
  no new full local QC run is claimed.
- Official BTO JSON, NLM MeSH and primary PubMed/EFetch retrievals succeeded.
  Both citation pairs were checked in the primary PubmedData ArticleIdList,
  not inferred from cited references.

## Identity and Grounding

ITEM GROUND at `curation/decisions.tsv:1002` resolves the compound
`Blood > Arterial` to [BTO:0006188](https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms?obo_id=BTO%3A0006188).
The current non-obsolete label and complete definition exactly match
vendored row 6187 and the emitted YAML. The blood-in-arteries identity
is sound; the source synonym retains the path's adjective, not a claim
that every arterial structure is blood. Status, exactMatch and both
August 16 events faithfully reflect the ITEM decision. Historical #12
is the curation-backlog reference, not current corpus statistics.

The current typed graph and local edge 4327 make
[BTO:0000089](https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms?obo_id=BTO%3A0000089)
blood a valid superclass. Its current label/definition match local row 91.
The complete generated blood record was read as a reference; its PREGO
observations are not automatically arterial-blood observations.

The second parent is different: the complete `blood__c1b484fe.yaml`,
`habitatmech:GOLD.6c6aab19d3`, explicitly denotes mammalian Blood, remains
minted/NARROW, and has no authored definition broadening it to all hosts.
Generic arterial blood is not a subtype of this host-restricted class.
The source path is valid provenance but does not justify restricting the
scope of the adopted ontology identity through a false is-a edge.

## Evidence

Raw GOLD tree row 1995 is node 6820 and the exact five-level mammal path,
with zero organism/study/biosample/total assertions. Omitted count/unit is
correct. The immediate parent at raw row 141 aggregates nodes 3665/4114
and 160 organism assertions; those are not this target's counts. The
separate human Arterial record, node 6605, is NARROW/REVIEWED under the
generic term and human Blood; its context must not be silently merged.

Full structured scans covered 2,562 GOLD paths, 1,040 bulk rows, 4,587
studies and 1,587 triads. The arterial-name hits were only the two blood
tree rows and two arterial-ulcer tree rows; no target bulk/study/triad
observation was found. PREGO arterial-plaque synonyms do not describe
arterial blood. No nearby evidence or parent counts were transferred.

The inspected primary abstract [PMID:7479497](https://pubmed.ncbi.nlm.nih.gov/7479497/),
DOI:10.3382/ps.0741209, describes arterial and venous cannula sampling in
broiler chickens. This is a positive non-mammalian example satisfying the
BTO location definition, sufficient to refute the mammal-only superclass.
No physiological measurements, disease mechanisms or microbial observations
from that experiment are added to this GOLD source.

The definition's separate oxygenation sentence also needs qualification.
[NLM MeSH D014469](https://www.ncbi.nlm.nih.gov/mesh/68014469) identifies
umbilical arteries as arterial vessels carrying deoxygenated fetal blood.
The inspected primary abstract [PMID:10955430](https://pubmed.ncbi.nlm.nih.gov/10955430/),
DOI:10.1111/j.1471-0528.2000.tb10401.x, reports a prospective cohort of
vigorous newborns with low umbilical arterial oxygen saturation. It provides
a physiological counterexample to listing only the pulmonary exception.
The finding is about wording, not a clinical threshold, a universal oxygen
parameter or a reason to change the location-based identity. Only the
abstracts were inspected, not full study methods.

## Completeness

Ignored-inclusive current ID, former key, label and slug searches covered
curation, history, research, prior reviews, PATHS and RETIRED. No target
definition request, overlay, session, research report or previous exact-
target review was found. Prior generic-blood report mentions are not
completed review coverage for this record.

Complete scans additionally covered 162 BacDive sources, 3,081 BacDive
taxa, 358 mappings, 770 parameters, 58 Madin habitats, 1,378 Madin taxa,
719 PREGO habitats and 8,807 PREGO taxa. Apart from the excluded plaque
lead, no arterial-blood match appeared. This bounded negative does not
prove sterility. Optional taxa, parameters, mechanisms and datasets are
not quotas. iModulonDB is not applicable: no gene/regulator/module claim.

## Findings

1. **Major - HM-ARTERIAL-BLOOD-001:** a mammal-specific source Blood class
   is asserted as broader than generic arterial blood. Owner:
   `src/habitatmech/seed.py:898-907` or a governed source-parent exclusion.
   Filed as [#1348](https://github.com/CultureBotAI/HabitatMech/issues/1348).
2. **Minor - HM-ARTERIAL-BLOOD-002:** BTO-owned oxygenation wording omits
   the umbilical-artery exception. Owner: upstream `BTO:0006188`, then the
   ontology inventory produced by `_load_bto` in
   `src/habitatmech/extract.py:849-886`. Filed as
   [#1349](https://github.com/CultureBotAI/HabitatMech/issues/1349).

No blocker found. Identity, valid BTO parent, source fields, zero-count
handling and generated statuses are supported.

## Recommended Edits

Remove only the false mammal-specific source-parent contribution, retaining
the BTO identity/label, valid blood superclass, source path/node, mapping,
status and retired URL. Do not globally discard GOLD parents or combine
human and mammal observations. The separate human record's two direct
parents remain valid.

Correct or qualify the oxygenation sentence upstream in BTO and refresh
its governed inventory with matching provenance. Ontology-owned terms
cannot be redefined through `curation/term_requests.tsv`; the definition
validator explicitly rejects that route. Do not patch generated YAML or
an isolated raw row without its source update.

Read-only comparisons through the actual semantic adapter and full parent
context show that each proposed change independently alters map input.
Append required audit records, inspect guarded canaries and regenerate
corpus/map/site through supported tools; #1217 remains relevant. Do not
fake freshness, coordinates or checksums.

## Follow-up Checks

Regress the false edge and preserved valid parent/source fields. Verify
the corrected upstream definition after controlled re-extraction, with
provenance, strict/OAK/history/corpus, site/redirect and full QC checks.
Ensure an oxygen qualifier is never converted into a universal numeric
parameter. Confirm both historical source URL and human child survive.

## Additional Notes

All 499 existing issue bodies and returned comments were searched before
filing. #15 concerns grounding routes and #451 an old blood-report search
summary, not these findings. No external ontology issue was filed. No
scientific input, generated output, history or runtime pin changed, and
no paid research ran.
