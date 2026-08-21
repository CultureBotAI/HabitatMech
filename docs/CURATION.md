# Habitat curation rules

This document is the canonical domain guide for decisions in
`curation/decisions.tsv`. The seeder and tests enforce its machine-checkable
parts; this text explains the judgments that cannot be reduced to a label match.

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
