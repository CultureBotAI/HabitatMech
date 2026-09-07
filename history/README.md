# Curation history

Append-only provenance for curation sessions. One record per session per target,
written once and **never edited afterwards**. Corrections go in a new record that
references the old one in its `details`.

```
history/<kind-dir>/<slug>/<TIMESTAMP>-<actor>-<shortid>.yaml
```

This layer is distinct from the `curation_history` list inside each habitat
record. That list is the record's own audit trail of what changed in it; this
directory records the *session*: which model, using which tool, changed what,
why, under which issue, and what it checked. The two complement each other, and
records that are regenerated from `curation/decisions.tsv` still get a session
record here describing the decision.

## Why the layout looks like that

The directory-per-slug plus unguessable `shortid` is the whole design. Two agents
curating the same habitat concurrently cannot write the same file, so this layer
has **no merge-conflict surface**. A single shared changelog would conflict on
every parallel PR; this never does.

## Writing a record

Do not hand-write the filename or the timestamp. Scaffold it with claw's tool:

```bash
just new-history --kind record --slug fecal_environment \
  --target-root data/habitats/other \
  --event EDIT --outcome changed \
  --sections grounding,parent_habitats \
  --summary "Ground to ENVO:01001029 and add the ENVO parent" \
  --model claude-opus-5 --agent-tool claude-code \
  --issue https://github.com/CultureBotAI/HabitatMech/issues/<n> \
  --details "What was done, what evidence was used, how it was validated."
```

Habitat records live under `data/habitats/<category>/<slug>.yaml`, so `--slug` is
the record's filename stem and `--target-root data/habitats/<category>` resolves
the target path.

`just new-history` needs a claw checkout: it runs `kg_microbe_history` from
`CLAW_SRC`, which defaults to `../culturebotai-claw/src` and can point anywhere.
Omit `--details` and you get a TODO placeholder to edit before committing;
`just validate-history` **fails** while it is still there, so an unfilled record
cannot slip through. The command prints the record path as its final stdout
line, so scripts can capture it.

`--kind record` and `--kind schema` can derive the target path from `--slug` plus
`--target-root`. Every other kind needs an explicit `--path`.

Then validate and stage:

```bash
just validate-history history/records/fecal_environment/<file>.yaml
git add history/
```

## The vocabulary

`event`: `CREATE` · `EDIT` · `REVIEW` · `AUDIT` · `GENERAL`

`outcome`: `changed` · `no_change` · `needs_followup` · `blocked`

Outcome is orthogonal to event on purpose. A `REVIEW` that found nothing is
`no_change`, a real result worth recording because it says something was
checked. An `EDIT` that hit a wall is `blocked`, and `details` must say what the
wall was so the next session does not rediscover it.

`kind`: `record` · `schema` · `mapping` · `report` · `infrastructure` · `other`
(`other` requires an explicit `--path`).

## How strictly this is enforced

- **Validity is blocking.** `scripts/run_qc.py` runs `scripts/validate_history.py`
  on every push and pull request; a record that is structurally incomplete or
  fails the schema fails the build, like any other validation error.
- **Presence is advisory.** Nothing blocks a record change that arrives without a
  session record. A hard gate on provenance blocks legitimate work at
  inconvenient moments and trains people to route around it; the expectation is
  stated in `CLAUDE.md` instead.

## Where the schema lives

- **Canonical**: `culturebotai-claw/src/kg_microbe_governance/artifacts/schema/history.yaml`.
- **Vendored here**: `src/habitatmech/schema/history.yaml`, byte-identical and
  pinned through `scripts/.vendored_canon_ref`; `just check-vendored-sync` and the
  `vendored-sync` workflow verify it.

Validation uses the vendored copy, so it works with no claw checkout at all. Only
`just new-history` reaches claw, and anyone writing curation records has it.
