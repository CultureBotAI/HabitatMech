# Habitat curation rules

This document is the canonical domain guide for the curation inputs the seeder
reads: the decisions in `curation/decisions.tsv`, the authored definitions in
`curation/term_requests.tsv`, and the withdrawals in
`curation/redirects_retracted.tsv`. The seeder and tests enforce its
machine-checkable parts; this text explains the judgments that cannot be reduced
to a label match.

The domain rules come first, then the sections specific to one input file.

## Decision model

Every decision is keyed by the minted identifier of one source concept, as
printed by `just worklist`.

| Decision | Meaning |
|---|---|
| `GROUND` | Adopt a verified ontology term as the concept identity. |
| `GROUND_AS_PARENT` | Keep the minted identity and attach a strictly broader term, producing `NARROW` grounding. |
| `CONFIRM_UNGROUNDED` | Confirm that the concept is a real habitat for which no fitting identity term is available. |
| `NOT_APPLICABLE` | Confirm that the source concept itself is not a habitat, such as a disease, quality, process or procedure. |
| `REVIEW` | Endorse the answer the seeder already produced. |

A related term that is not broader can be retained with `relation: xref`.
`parent_habitats` is an is-a claim and must never be used merely to avoid losing
an upstream link.

A GOLD path can map exactly even when its bare leaf is broader than the
resolved habitat. When that leaf is the canonical label of a different strict
ontology ancestor, the seeder retains it as RELATED_SYNONYM, with a deterministic
scope event, rather than asserting exact lexical equivalence. Source attestations
remain verbatim. CLOSE- and BROAD-mapped GOLD and BacDive labels likewise receive
RELATED_SYNONYM, not exact scope, with a deterministic source-scope event
(#1459, #1769). Mapping direction alone does not establish a lexical broad or
narrow synonym relation. Independently supplied ontology synonyms are preserved. These guards
do not establish the scope of other source labels or repair untyped ontology
synonyms; those still need separate review (#1249).

An exact xref from an ontology that is not present in
`data/raw/ontology_terms.tsv` can be label-verified through
`curation/external_xrefs.tsv`. Those allow-listed terms are only valid beside a
`CONFIRM_UNGROUNDED` or `NOT_APPLICABLE` decision with `relation: xref`; they
must never be used as a `GROUND` identity or a `GROUND_AS_PARENT` parent.

Each decision has a `review_depth`. `ITEM` means the source path and candidate
terms were examined. `CLASS` records membership in a mechanically defined
screen and does not promote a record to `REVIEWED`. An equivalence grounding is
always an item-level judgment.

## Hosts, anatomy and taxa

An organism acting as a host is a microbial habitat. The taxon class or
whole-organism ontology term is not the identity of that associated environment.
For concepts such as Mammals, Mollusca, larva or embryo:

1. keep the source habitat concept under its minted identity;
2. retain the organism or taxon term as an xref;
3. attach an existing broader associated-environment term when defensible; and
4. request a more specific associated-environment term when none exists.

Anatomical parts such as gut, skin, lung and blood are different: they denote
the site where the microbe lives and can ground directly. A structure built by
an organism, such as a cocoon, is also not the whole organism and grounds by its
own meaning.

Do not use `NOT_APPLICABLE` merely because the available match is a taxon. That
decision says the source concept is not a habitat, which is stronger than saying
the proposed target is the wrong kind of entity.

## MIxS environmental triads

The ENVO guidance for MIxS distinguishes three roles:

- `env_broad_scale` describes the ecosystem or environmental system, not a
  process, material, single object or group of objects;
- `env_local_scale` describes the local feature and may use UBERON or PO for a
  host anatomical part;
- `env_medium` describes the material composing the sample.

Source: [Using ENVO with MIxS](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS).

A triad is strong contextual evidence, but the presence of a term does not
decide which slot, if any, is the habitat identity. For a host-associated
sample, broad scale may correctly describe the ecosystem around the host rather
than the host itself.

`just report` screens every GOLD triad slot before offering it to a curator. A
term is eligible only when it exists in the vendored ontology slice and is not
an organism or other taxon-valued concept. Terms from unsupported prefixes
remain out of scope unless other evidence justifies vendoring their ontology
data. The compatibility section reports excluded terms and cached GOLD labels
that disagree with the slice; ranked evidence always displays the authoritative
slice label required by a `GROUND` decision. Report obsolete source annotations
through the [GOLD feedback form](https://gold.jgi.doe.gov/help).

## Evidence and validation

Every curation session that changes a decision row, a term request or a
causal-graph curation also gets an append-only session record under
`history/`, scaffolded with `just new-history` and validated by `just qc`.
[history/README.md](../history/README.md) has the layout and the vocabulary.

Every `GROUND` records both the target CURIE and expected label. Seeding fails
unless that identifier exists in the vendored slice with the stated label. If a
valid target is absent, vendor the ontology data rather than weakening the
check.

Decision notes are also validated where possible: a `Path:` must match the
source concept, mentioned term identifiers must exist, and quoted labels must
match the slice. Notes should explain why the relationship holds, not merely
repeat the selected enum.

A merged record becomes `REVIEWED` only when every contributing source concept
has an item-level decision. Partial review intentionally leaves it `SEEDED`.

Every causal-graph edge requires cited evidence. Upstream habitat attestations
do not vouch for mechanism claims.

## Retracting a published redirect

`data/habitats/RETIRED.tsv` maps dead record URLs to live ones, and it is
append-only by design: a redirect the site has already published is state
someone may have linked to, so a later rebuild carries it forward rather than
letting it lapse. The builder reads the committed map, not the working copy,
which means deleting a row does not retract it — the row returns on the next
`just redirects`, and `--check` calls the hand-edited file stale in the
meantime.

Withdrawing one is therefore a curation decision, recorded in
`curation/redirects_retracted.tsv`:

| Column | Meaning |
|---|---|
| `retired_slug` | The page name to stop publishing, exactly as it appears in `RETIRED.tsv`. |
| `curator` | Who withdrew it. |
| `date` | When. |
| `why_retracted` | Why the redirect was wrong. |

The builder subtracts these slugs from the map and `just render` then prunes
their stubs, so the sequence is the ordinary one: add the row, run `just
redirects` and `just render`, commit both.

A retraction row is permanent — do not tidy one away because it looks spent.
The two kinds of row it can withdraw are not equally sticky. A carried-forward
redirect stays withdrawn once the retraction is committed, because the builder
reads the committed map and the row is no longer in it. A redirect derived from
a label change is rebuilt on every run from the live corpus and from every page
the branch has ever held, so the row in this file is the only thing suppressing
it; delete the row and the next `just redirects` republishes it.

Retract only a redirect that is *wrong* — one pointing at a habitat that never
absorbed the retired concept. A redirect whose target has itself since merged
is not wrong; the builder follows it onward through the stable upstream source
ids. Retracting returns the URL to a 404, which is the outcome the map exists
to prevent, so the reason has to say what the redirect claimed and why that
claim was false.

## Curated definitions and hierarchy

Definitions for minted terms belong in `curation/term_requests.tsv`; generated
records under `data/habitats/` are never edited directly. The optional
`parent_mode` column controls how the authored ontology genus interacts with
parents inferred from source hierarchy:

- `ADD` is the default. It retains source-derived parents and adds the authored
  ontology parent. Use it when both hierarchy claims are true, even when the
  ontology parent is more general or more stable.
- `REPLACE` removes every inherited parent before adding the authored ontology
  parent. Use it only after an item-level review establishes that every
  inherited parent is false for the concept, and record that evidence in the
  definition notes. It is not a way to express preference for a tighter genus.

When a definition renames a source label that equals its canonical strict-genus
label, the old label is retained as RELATED_SYNONYM with a deterministic
`SOURCE_SYNONYM_SCOPED` event, not promoted to exact equivalence. An authored
`exact_synonym` may not name that strict genus either. Both checks use the same
lexical key, including punctuation, whitespace and case folding. This bounded
guard does not assess other broader names, ancestor synonyms or definition scope;
those still require evidence-backed review. Verbatim source attestations and unrelated
authored exact aliases are preserved.

`curation/definition_source_label_exclusions.tsv` provides an explicit opt-out
from automatically retaining a renamed native term's old label as a synonym.
Use it for a reviewed ambiguous label, not to change the definition or source
attestation. Each required row pins the native identifier, exact pre-definition
`source_label`, exact `requested_label`, curator, ISO date and evidence-based
notes. Missing files, malformed or duplicate rows, unmatched definitions, stale
labels and contradictions with authored exact aliases stop regeneration. The
curation-floor check protects rows against accidental loss. Other source and
ontology synonyms are not removed; this is not a general synonym-scope repair.
The record receives a deterministic `SOURCE_SYNONYM_EXCLUDED` event, while its
old definition event and verbatim attestations remain intact. Append session
history targeting this table, inspect a canary and run the normal corpus/site
gates after editing it. Do not infer an opt-out from free-text definition notes.

For example, the diatom definition adds an organism-determined ENVO genus while
retaining GOLD's true alga-associated parent. The inland saline-or-alkaline
definition replaces GOLD's aquatic-biome edge because the source bin includes
engineered settings and therefore is not a kind of biome.

### Excluding a GOLD context parent

`curation/gold_parent_exclusions.tsv` suppresses only the immediate GOLD
source-path parent contribution for one minted source concept. Use it when
the source hierarchy denotes context rather than a strictly broader habitat,
including on ontology-grounded records; do not invent a term definition merely
to remove an unsupported edge. It does not remove independently supported
ontology, grounding-decision, other-source, or definition parents.

Each row names the GOLD source `identifier`, exact `source_path`, expected
resolved `parent_id`, `curator`, ISO `date`, and evidence-based `notes`.
Regeneration fails on duplicate, malformed, unmatched, or stale exclusions,
including when the immediate parent's resolution changes. Review the source
and update the row deliberately after an upstream change. The table is required
and protected by the curation-floor check against accidental row loss.

Exclusions preserve source paths, attestations, grounding, and review status;
they append a deterministic `SOURCE_PARENT_EXCLUDED` event to affected records.
They do not assert a replacement relation or settle an unresolved definition.
Run `just seed`, inspect `just seed-canary <IDENTIFIER> --force`, add session
history targeting this table, then regenerate and run the normal QC gates.
