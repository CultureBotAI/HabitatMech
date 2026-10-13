# YAML Record Review: Biotransformation

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/biotransformation.yaml`
- Started UTC: 2026-10-07T11:50:48Z
- Finished UTC: 2026-10-07T11:55:19Z
- Verdict: needs curation (0 blocker, 1 major, 0 minor)

## Target

Read the entire generated HabitatRecord `habitatmech:GOLD.7df92c13b7`,
Biotransformation, ENGINEERED, UNGROUNDED/SEEDED. Its path is
`Engineered > Biotransformation`, with 57 ORGANISM assertions and four
collapsed GOLD nodes. `data/habitats/PATHS.tsv:2220` pins the filename.
This is a process-named source category without an authored physical-habitat
definition, not an identified bioreactor, organism or specific conversion.

## Validation

- `just validate data/habitats/engineered/biotransformation.yaml`: pass.
- `just validate-strict data/habitats/engineered/biotransformation.yaml`:
  one file, zero errors.
- Read-only all-field `build_corpus`/`build_document` comparison passes:
  one source concept, zero reviewed sources, zero taxa, two history events.
- Shared unchanged-input checks in this session: all 3,207 records reproduce
  exactly and all 146 histories validate. Full QC/OAK/vendored results are
  reused from the identical scientific tree merged as
  `c54d9263c97873f825caf023896571c256c1deb6`, not new runs for this report.
- No ontology grounding, taxon, graph or citation is asserted in the target
  that needs a corresponding focused validator. Schema validity does not
  establish that a process-named source category denotes a habitat.
- Standard browsing and HTTP access to current IUPAC pages failed; a transient
  pypdf reader successfully inspected the historical original IUPAC text in a
  public university-hosted PDF without changing repository dependencies.

## Identity and Grounding

The canonical path reproduces the mint. The actual automatic resolution is
`gold_unmatched`, followed by the CLASS/CONFIRM_UNGROUNDED decision at
`curation/decisions.tsv:746`. Its notes explicitly leave habitat meaning
unassessed, so SEEDED is accurate and this is not an individually confirmed
novel habitat.

There is a conflicting local assessment:
`curation/samples/class_swept_unscreened-20260814.tsv:20` calls the concept
a process rather than a place. The sample result is not a maintained ITEM
decision and has not changed the generated interpretation. Preserve this
conflict rather than treating either the CLASS default or sample label as
sufficient evidence by itself.

Read the entire immediate parent,
`data/habitats/engineered/engineered__900b76ad.yaml`,
`habitatmech:GOLD.2acb39dd08`. It too is an undefined CLASS-swept source
(`curation/decisions.tsv:331`). The actual source-path edge is traceable, but
the parent cannot by itself turn a conversion process into a physical habitat.
A genuinely defined engineered setting may have a defensible broader relation;
that conditional interpretation has not been supplied here. No ontology or
authored definition adds an independent parent.

## Evidence

- `data/raw/gold_ecosystem_paths.tsv:288` records the depth-two path,
  nodes2895/3536/3876/4314 and 57 organisms, zero studies/biosamples, total57.
  First-node display, four-node note, count and ORGANISM unit all agree. These
  assertions are not 57 named characteristic taxa or experimental replicates.
- `gold_path_biosamples.tsv:946` separately links one biosample to node4314.
  `gold_studies.tsv:584` links Gs0110166 to both this category and
  `Engineered > Bioreactor > Anaerobic`. That membership does not equate
  biotransformation with an anaerobic reactor or support universal anaerobiosis.
  The live study page was inaccessible; exact-ID web search returned no results.
- All 14 raw TSVs were scanned with structured exact-field/pipe-member keys,
  including all four nodes derived from the actual collapsed row. Only the
  three GOLD inventories above matched. No target taxa, environmental parameters
  or triad assertion was found in the other eleven inventories.
- [IUPAC Gold Book, historical version 2.3.3, 2014-02-24](https://fenix.tecnico.ulisboa.pt/downloadFile/845043405473381/IUPAC_goldbook.pdf):
  inspected its title page and printed pages166-167 (PDF zero-based pages213-214).
  It distinguishes a bioreactor apparatus from biotransformation, a chemical
  conversion mediated by organisms or enzyme preparations. Both entries cite
  the 1992 biotechnology glossary, page148. This directly supports the
  process/apparatus distinction, not the meaning intended for every GOLD source.
  The live Gold Book HTML/plain/JSON/PDF and original IUPAC-hosted source were
  inaccessible or challenged, so no claim of checking the current 2025 wording
  is made. Search snippets were not used as substantive evidence.
- [Mukherjee et al., GOLD v.8](https://academic.oup.com/nar/article/49/D1/D723/5957166),
  PMID:33152092, PMCID:PMC7778979, DOI:10.1093/nar/gkaa983: inspected the
  publisher's abstract and Study/Organism/Biosample/controlled-vocabulary
  descriptions. They distinguish sampled entities from their organizing metadata;
  they do not define this source as a physical habitat or supply current counts.
  A later publisher refetch failed and Europe PMC full XML returned500. The
  [author-list correction](https://pmc.ncbi.nlm.nih.gov/articles/PMC11014354/),
  PMID:38416591, DOI:10.1093/nar/gkae163, was read through Europe PMC full XML;
  it adds omitted authors, not a habitat-modeling result. Both article identities
  were verified through NCBI efetch. Figure3 was not directly inspected and
  its search-result category counts are not used here.

## Completeness

Ignored-inclusive identifier, label and slug searches covered curation,
histories, configuration, research/manifest, PATHS, RETIRED and existing
review reports. They locate the CLASS decision, conflicting sample result and
a contextual mention in another target's environmental research, but no
target-owned ITEM decision, definition, causal overlay or research report in
those maintained surfaces. An older Engineered-root review mentions this child;
it is not a completed individual review of this record.

An ignored-inclusive filename search in the configured upstream kg-microbe
checkout found no matching GOLD node/edge or gold ecosystem/study files under
the queried filename patterns. Original individual assertions therefore were
not independently recounted; this is a bounded filename search, not global
source absence. Optional taxa, parameters, evidence, graphs, discussions and
datasets should remain empty without target-specific evidence. A count or
shared study is not a license to fill them.

## Findings

1. **Major: unresolved process-versus-habitat identity despite a recorded warning.**
   The record's only source meaning is a process-named category, its maintained
   CLASS decision explicitly did not assess habitat identity, and the earlier
   sample flagged exactly this concern. Inspected primary terminology supports
   the process distinction; source membership alone does not establish an
   associated physical setting. This needs an ITEM assessment, not automatic
   promotion to a novel habitat or a grounding to a process term. Owner:
   `curation/decisions.tsv`, with `curation/term_requests.tsv` only if a real
   source-supported habitat interpretation can be defined. The source's intended
   scope is still unresolved, so this review does not claim a proven wrong mint
   or mandate NOT_APPLICABLE solely from the label.

## Recommended Edits

1. Resolve what the GOLD category represents using source definitions and
   original associated records. Reconcile the sample warning in an ITEM
   decision with explicit evidence and without overwriting the old sample.
2. If the source itself denotes the conversion process, use NOT_APPLICABLE
   and do not give a process ontology identity to a habitat. If it consistently
   denotes a physical biotransformation setting, retain its mint and author a
   bounded evidence-backed habitat definition with a strictly broader genus.
   Do not equate the source with one study's anaerobic reactor or invent a matrix.
3. Preserve all four source nodes, full path, 57 ORGANISM assertions and
   separate bulk-study/biosample provenance; append curation history and
   regenerate only in a later authorized curation session.

## Follow-up Checks

Obtain original source scope before selecting either curation branch. Verify
any proposed ontology term and review all four possible parent-contribution
routes. Dry seed, inspect the target canary, add a differential regression for
the intended fields and unaffected records, validate history/strict schema and
exact reproduction, regenerate affected products and run full QC/OAK. Do not
promote review status merely because the sample or this report found the issue.

## Additional Notes

Only this new report was written; no scientific input, generated output,
status, history or GitHub item changed. Initial PDF page selection used
physical pages165-167, which were unrelated because of front matter; these
were discarded as evidence, and the correct printed pages were then read.
iModulonDB is not applicable to a bare process-named source with no specific
gene, regulator, organism/dataset or transcriptomic claim. No paid research.
