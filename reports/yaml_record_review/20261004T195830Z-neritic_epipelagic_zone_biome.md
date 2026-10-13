# YAML Record Review: neritic epipelagic zone biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/neritic_epipelagic_zone_biome.yaml`
- Started UTC: 2026-10-04T19:54:44Z
- Finished UTC: 2026-10-04T19:58:30Z
- Verdict: pass

## Target

Entire 75-line generated HabitatRecord ENVO:01000042, neritic epipelagic
zone biome, AQUATIC, EXACT/SEEDED. It contains an ENVO definition, one
ontology parent, three related PREGO synonyms, one PREGO attestation, all
seven associated taxa and one seed event. Parameters, xrefs, record-level
evidence, causal graphs, discussions and datasets are absent.

`PATHS.tsv:766` pins the stem. Actual source-key minting gives
habitatmech:PREGO.4bfe6872e1 for PREGO's ENVO:01000042 concept.
This is the continental-shelf epipelagic biome, not generic marine photic
water or a specifically offshore oceanic biome. The pass is scoped to the
verified identity and source projection; original ecological evidence for
the seven associations remains unverified, as detailed below.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/neritic_epipelagic_zone_biome.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/neritic_epipelagic_zone_biome.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Fresh shared PASS: 1,179 canonical, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Terminal PASS: 457 tests passed, three skipped, two warnings in 522.71s; 90 history records, all 3,206 strict records, 32 graph curations, exact reproduction and all remaining gates passed. |
| Source/reference checks | Full target, actual PREGO ingester, extractor ranking logic, exact dictionary comparisons, all 14 raw tables, current typed ENVO/OLS, all seven current NCBI Taxonomy records and full page/semantic output. |

All seven taxon dictionaries, the complete attestation, pool size, label and
definition match maintained inputs. No graph/reference objects need a
separate causal validator. Identifier-label validation is not an ecological
or SSSOM/KGX semantics audit; none is claimed here.

## Identity and Grounding

Current [ENVO:01000042](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000042)
is active and matches the complete vendored definition at
`ontology_terms.tsv:7552`. It describes the shelf-associated upper water-
column biome with approximate depth and conditional seasonal-thermocline
wording. Preserve those qualifications, not universal measured depth limits.

Its sole typed named superclass is ENVO:01000032, neritic pelagic zone biome,
matching `ontology_subclass_edges.tsv:5682`. The broader term at
`ontology_terms.tsv:7542` and current OLS concerns the shelf water column.
Its definition starts with the epipelagic wording, but its canonical label
and explicit typed hierarchy distinguish the broader class; no local edge
contradiction was established. This is not a GOLD source-context parent.

Actual `ingest_prego` execution gives one prego_self_grounded route, one
source concept and zero reviewed sources. No applicable decision exists.
EXACT denotes direct ontology identity, not item-level ecological review;
SEEDED and the lone seed event are correct. The source and record share
the identifier, so omission of a mapping predicate is appropriate. This
does not reproduce #1398.

PREGO's singular, plural and unusual `neritic epipelagic zonous` strings
are preserved as RELATED_SYNONYM, attributed to PREGO. Current ENVO has
no synonyms for this term. The source variant is not presented as an ENVO
exact synonym or proof of a second identity. Any normalization should
preserve source provenance rather than silently invent a replacement.

## Evidence

`prego_habitats.tsv:364` gives seven taxa, seven direct assertions, maximum
score four and the environmental_samples channel. Generated assertion_count
uses the distinct taxon count, not an organism abundance or sample count.
The equal direct counter is a separate source statistic.

All seven rows at `prego_habitat_taxa.tsv:7484-7490` have score four,
direct_flag TRUE and the environmental_samples channel, without cross-source
corroboration. Full dictionary comparison verifies IDs, both supplied names,
five absent names, scores, ranks, source and candidate_pool seven. No top-25
truncation occurs for this target. The extractor sorts tied scores/direct
flags by taxon identifier; ranks one through seven do not establish seven
different strengths of evidence.

Current [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=163503,3068,463189,6669,777,84301,9541&retmode=xml)
resolved every requested ID directly, with no returned alias redirect:

| NCBITaxon ID | Current name | Generated label |
| --- | --- | --- |
| 163503 | Chaetoceros socialis | Matches. |
| 3068 | Volvox carteri f. nagariensis | Omitted, matching input. |
| 463189 | Centropages typicus | Omitted, matching input. |
| 6669 | Daphnia pulex | Omitted, matching input. |
| 777 | Coxiella burnetii | Matches. |
| 84301 | Calanus pacificus | Omitted, matching input. |
| 9541 | Macaca fascicularis | Omitted, matching input. |

These are identifier/name checks, not confirmation that each organism
inhabits this biome. In particular, unusual associations such as 9541 need
the original environmental record and taxon/habitat assignment inspected;
neither ecological correctness nor an automatic deletion follows from the
resolved name. No entry asserts is_characteristic, and no abundance,
mechanism or original sample measurement is supplied.

The complete 14-table exact-ID scan found no independent GOLD, BacDive,
MADIN or environmental-parameter row for this target. The configured
kg-microbe root is
`/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe`;
KG_MICROBE_ROOT is unset. A gitignore-independent filename search across
that checkout found no PREGO files. This is bounded to the configured
checkout, not all disks or upstream availability. The manifest names and
hashes historical transformed PREGO nodes/edges, but their current original
records were not recovered here.

The [PREGO portal](https://prego.hcmr.gr/) timed out in the web renderer;
a separate verified-TLS request failed because its certificate had expired.
Certificate verification was not bypassed. No current portal content,
sample-level provenance or underlying ecological experiment was inspected.

## Completeness

Ignored-inclusive identifier, minted source key, label and stem searches
covered curation, history, research, reports, conf, PATHS and RETIRED, with
filename inventory. They found the path lock and neighboring photic-zone
mentions, not a target decision, term request, overlay, dedicated research,
session history, retirement or previous individual review. No new habitat
term is needed for a supported active ENVO identity.

The ontology-only parent has no generated habitat record in the ignored-
inclusive corpus search; it is a verified external ontology reference, not
a broken minted link. The page resolves its label and displays all seven
taxa as source associations. Actual semantic text includes only the two
supplied taxon labels. Adding the other names in maintained taxonomy inputs
would change that text, but optional-name omission is not an invented
record defect. iModulonDB is inapplicable without expression/gene claims.

## Findings

None found within the inspected scope: zero blockers, zero major, zero minor.
The unrecovered original ecological evidence is an audit limitation, not
proof that source associations are false or a claim that they are verified.
The source-only odd synonym and optional blank labels are faithfully retained.

## Recommended Edits

No mandatory record correction is established. Preserve the active ontology
identity, supported parent, PREGO attribution and observational status.

Before endorsing or rejecting the unusual associations, recover their
original PREGO environmental records and inspect the exact source links.
Any supported correction belongs in versioned source/taxonomy inputs and
`src/habitatmech/extract.py`, not generated YAML. Optional name refreshes
must retain source IDs and follow normal provenance/regeneration rules.
Do not promote to REVIEWED or is_characteristic from this report alone.

## Follow-up Checks

Any future maintained-input change requires exact taxon/source regressions,
required new history, `just seed`, then
`just seed-canary ENVO:01000042 --force`. Inspect the entire canary before
`just seed-apply --force`; never prune partial runs. Preserve rank/pool/score
and evidence-channel meanings, related-synonym provenance and true ancestry.
Require ordinary/strict validation, current taxonomy and ontology checks,
exact reproduction and full QC.

No parent removal is recommended. Compare actual semantic inputs for any
selected taxonomy/synonym edit and perform genuine map/site refresh if they
change (#1217). Protect #1218/runtime pins. These are future checks, not
review mutations or an SSSOM/KGX compatibility certification.

## Additional Notes

All-state exact ontology-ID, minted-key and unusual-synonym issue searches
returned no matches. The broader neritic query found #1289; its full body
concerns unsupported offshore ancestry on generic marine photic zone,
not this correctly shelf-scoped biome. No defect issue is invented here.

An exploratory checker initially used `id` instead of the actual term_id
column, failed, and was corrected and rerun to terminal success. No corpus
file changed. Official typed ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated product, previous report/history or paid research changed.
