# Semantic text map inputs

`just text-map-inputs` validates a preview of the **complete current corpus**.
It emits a summary; it does not run a model, generate coordinates or publish a map.
`just text-map-inputs --output build/text-map/inputs.jsonl` atomically exports
versioned semantic inputs for the shared fleet embedding pipeline.

For a canary, add `--limit 32` or repeat `--record data/habitats/<category>/<record>.yaml`.
The receipt explicitly says `subset`. A canary cannot stand in for full map
coverage. A temporary SQLite index keeps file/identifier bookkeeping bounded
in memory. Habitat resolves parent labels from its small complete corpus and vendored
ontology slice even for a canary, keeping each record's full/canary hash equal.

Each JSONL row has `identifier`, `label`, `category`, `page`, `source_path`,
`text`, `text_sha256` and `adapter_version`. The selected semantic fields
exclude citations, curation history, data-source counts and assembly/accession
identifiers. The source YAML is never edited. Duplicate identifiers and
symlink/outside-corpus paths are refused before output is published.

The habitat adapter includes names, definition/category, synonyms, resolved
broader-habitat labels, environmental parameters and explicitly distinguished
observed versus characteristic taxa. Page targets follow the existing site's
label-plus-identifier slug rule.

The installed CLAW runtime is `scripts/embedding_pipeline.py`; its separate
locked environment and exact build commands are in the [maintained runtime guide](../conf/embedding-runtime/README.md).
Normal rendering and verification do not install that model environment or run
inference. When record membership or selected semantic fields change, export
fresh full inputs, reuse the existing profile-bound vector cache to encode only
new or changed text, regenerate PaCMAP, and validate the complete bundle before
rendering. A stale bundle must be refreshed before publishing curated changes.

## Validated site publication

`conf/text_map.yaml` is enabled. The common BGE/PaCMAP bundle is stored at
`data/text_map/`, with its selected generation named in `current.json`. The
generation's `manifest.json` records the full input identity and coverage counts.
Its site files are committed at `pages/text-map/` and linked as the semantic
text map; rendering verifies freshness against the current corpus.

Rendering exports fresh **full-corpus** JSONL and validates the current pointer,
artifact checksums, complete input identity and pinned common BGE profile. The
runtime stages the selected `index.html`, `points.json` and `manifest.json` at
`pages/text-map/`; the site links to that view after successful staging. Missing
runtime or current pointer, stale inputs and invalid checksums fail an enabled
build. A failed preflight preserves the existing published pages.

`just render-check` uses the same validation and staging inside a temporary site.
These checks do not download weights, encode text or fit PaCMAP. A canary cannot
satisfy the full-corpus publication check.

Staging binds the exact immutable generation approved during preflight. A changed
current pointer or substituted generation fails validation before publication
(CLAW #429).
