# YAML Record Review: Crude Oil Sludge

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/crude_oil_sludge.yaml`
- Started UTC: 2026-10-08T06:29:38Z
- Finished UTC: 2026-10-08T06:33:38Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord `habitatmech:GOLD.808ed1c989` at
`6f0de147db0cfa1c186620880965d227bb20eafd`. Its exact GOLD path is
`Engineered > Built environment > Oil refinery > Crude oil sludge`.
It is ENGINEERED / UNGROUNDED / SEEDED, with one parent, one GOLD
attestation and two history events. Definition, synonyms, xrefs, parameters,
taxa, literature evidence, graphs, discussions and datasets are absent.
The petroleum-sludge child and same-named sibling are distinct records.

## Validation

Fresh commands used `UV_CACHE_DIR=build/uv-cache`:

- `just validate data/habitats/engineered/crude_oil_sludge.yaml`: no issues.
- `just validate-strict data/habitats/engineered/crude_oil_sludge.yaml`:
  one file, zero errors.
- `just verify-corpus`: all 3,207 records reproduce, with zero missing,
  extra or differing files.
- `just validate-history`: all 172 session histories valid.
- `just provenance-check`: 14 inventories and two GOLD sources current.
- `uv run pytest tests/test_corpus_integrity.py -q -k 'parent or
  reviewed_records or history or causal_edges_reference'`: six existing
  parent/status/reference tests passed, 33 deselected. This selection does
  not constitute an additional generated-history test.

Read-only `build_corpus` / `build_document` reproduced every target field;
the concept has one source and zero item-reviewed sources. Executed default
and curated GOLD resolution with complete ontology, normalized mapping,
leaf-claimant and composed-claimant indexes.

Full QC and label correspondence were not rerun for these report-only edits.
The exact baseline's native queue
[QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37736853501) and
[label gate](https://github.com/CultureBotAI/HabitatMech/actions/runs/37736853478)
passed. The immediately preceding publication also verified all 1,177 canonical
pairs, one synonym and five existing exceptions, with 2,057 no-adapter skips.
Neither gate establishes the meaning of a parent edge. No standalone
literature-reference check applies to this citation-free target; original
GOLD re-extraction was unavailable in the searched local source bounds.

## Identity and Grounding

Mint recomputation and `PATHS.tsv:2240` agree. Default resolution is
`gold_unmatched`, UNGROUNDED, without predicate or extra parents. The CLASS
`CONFIRM_UNGROUNDED` row at `curation/decisions.tsv:760` retains the same
identity through `curated_confirm_ungrounded_from_gold_unmatched` and does
not count as ITEM review. SEEDED and the two reproduced history events
therefore agree with the maintained inputs.

Omitting a mapping predicate is correct because the record retains its source
identity. The narrow-match endpoint defect in other records does not apply.
The ENVO:03600078 parent is supplied independently by the GOLD parent-path
pass, not by the grounding decision.

Current primary [ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl)
defines ENVO:03600078, oil refinery, as an industrial building and gives
ENVO:00003861 as its named superclass. This agrees with the local inventory
at `ontology_terms.tsv:10114`. Sludge material is not a subtype of the building
where it occurs. The full contextual `oil_refinery.yaml` was read; its 25
ORGANISM assertions and separate parents are not assertions about this material.

## Evidence

An exact-field/pipe-member scan of all 14 raw TSV inventories found only the
target's GOLD classification row at `gold_ecosystem_paths.tsv:1274`: depth four,
one node (`gold.ecosystem:4867`), and zero organism, study, biosample and total
counters. The single-node display, omitted node-collapse note and omitted
count/unit reproduce that row. Zero counters do not establish sterility or
absence of organisms. No exact target biosample, study, triad, taxon or
environmental-parameter row was found in those inventories.

The current [GOLD classification workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
contains the target path as the prefix of node 4868's petroleum-sludge child
at `site data` row 214. It separately places the direct oil-refinery
petroleum-sludge sibling at row 216, node 4519. This verifies the source
hierarchy context, not strict ontology subsumption or the original node 4867
payload/counts. Workbook: 84,174 bytes; SHA256
`f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.

Both contextual petroleum-sludge records were read in full. The child
`habitatmech:GOLD.2bc7edd546` has two ORGANISM assertions; the sibling
`habitatmech:GOLD.c98a35c438` has one ORGANISM assertion across two historical
nodes. The sibling's separate one-BIOSAMPLE row and multi-path study
Gs0127555 are not target evidence and were not adopted or separately verified
as target citations. Neither label similarity nor workbook placement justifies
merging these source concepts.

The primary OWL also confirms active ENVO:00002044, sludge, as a residual
semisolid material, a plausible broader material genus rather than exact
identity. ENVO:00002060, oil sludge, instead concerns motor oil gelling or
solidifying; its near-matching name is insufficient to ground this crude-oil
refinery category. The alternate ENVO:02000142 petroleum oil refinery term
also describes a facility, not an exact sludge identity.

OWL: 9,614,229 bytes; SHA256
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
The four inspected class elements contain no deprecation assertion.
No process conditions, composition, microbial taxa or degradation mechanism
are inferred from these category definitions.

## Completeness

Ignored-inclusive searches for the exact ID, label, stem, path and node covered
curation, raw inventories, path/retirement registries, configuration, docs,
tests, history, research, its manifest and prior individual reports. They
found the source/decision rows and contextual infrastructure references, but
no target-owned definition, parent exclusion, overlay, research entry, session
history, retirement or prior individual review. Contextual mentions and reads
are not new completed reviews of those other records.

An ignored-inclusive filename search of `build`, `data/raw` and the configured
kg-microbe `data` tree found no original GOLD node/edge dumps, goldData.xlsx
or biosample-sweep intermediate. These bounded misses do not establish global
absence. The public classification workbook is not the original bulk source.
Empty optional biology is not a defect. No named gene, strain, regulator,
pathway or expression claim makes iModulonDB applicable.

## Findings

Zero blockers, one major finding, zero minor findings.

1. **Major: sludge material inherits a refinery building as a strict parent.**
   `parent_habitats: ENVO:03600078` converts a GOLD location/context link into
   an is-a claim. The inspected source path and primary building definition
   support context, not a building subtype. Owner:
   `curation/gold_parent_exclusions.tsv` for the exact GOLD contribution.
   A later item-level definition/genus assessment belongs in
   `curation/decisions.tsv` and `curation/term_requests.tsv`.

## Recommended Edits

Suppress the exact source-path contribution to ENVO:03600078 through the
guarded exclusion table. Preserve the source mint, label, path, original node,
count omissions and lifecycle; removing a false parent does not itself make
the concept ITEM-reviewed or NOT_APPLICABLE. Do not edit generated YAML.

Assess and document a supported sludge-material genus and definition in a
separate item-level curation step. Do not adopt the motor-oil-gel class as an
exact match, equate the record to all sludge, or merge its petroleum-sludge
child/sibling without source-specific evidence. Do not invent a definition
merely to suppress the building edge.

## Follow-up Checks

Regress exact source-path/expected-parent matching, the independent parent
contribution, default/curated resolution, single-node zero-count omission,
lifecycle and both distinct petroleum-sludge neighbors. For an authorized
repair, add session history, dry-seed, inspect a canary, regenerate and run
strict, provenance, history, label, reproduction and full QC gates. Compare
full-context semantic-map inputs after any parent change and rebuild affected
map artifacts when the semantic input changes. This review does not certify
SSSOM/KGX readiness or current kg-microbe model compatibility.

## Additional Notes

Only this new target report was written. Scientific inputs, generated
records/pages, statuses, history and GitHub remained unchanged. No paid
research or delegation was used. The browser could not expose the ontology
API/workbook content; primary OWL and workbook bytes were retrieved and
parsed in memory, resetting the workbook's incorrect worksheet dimensions.
