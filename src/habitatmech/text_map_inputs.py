"""Export versioned semantic text for the fleet map; no model inference.

The temporary SQLite path/identity index bounds memory independently of corpus
size. Full exports are the default; selected subsets are reported as subsets.
Habitat parent labels are resolved from the small corpus even for a canary, so
selection cannot alter the semantic text/hash of a record.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys
import tempfile
from collections.abc import Iterator, Mapping
from contextlib import ExitStack
from pathlib import Path
from urllib.parse import quote

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
ADAPTER_VERSION = "habitatmech-semantic-v1"
CORPUS = "habitats"


def clean(value: object) -> str:
    if value is None:
        return ""
    return " ".join(str(value).split())


def _load(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        record = yaml.load(handle, Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))
    if not isinstance(record, dict):
        raise ValueError(f"record is not a mapping: {path}")
    for field in ("identifier", "label"):
        if not isinstance(record.get(field), str) or not clean(record[field]):
            raise ValueError(f"record has no nonempty {field}: {path}")
    return record


def _discover(directory: Path) -> Iterator[Path]:
    """Yield paths without a list of all YAML files or following symlinks."""
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_symlink():
                if entry.name.endswith(".yaml") or entry.is_dir():
                    raise ValueError(f"symlink in corpus: {entry.path}")
                continue
            if entry.is_dir(follow_symlinks=False):
                yield from _discover(Path(entry.path))
            elif entry.name.endswith(".yaml") and entry.is_file(follow_symlinks=False):
                yield Path(entry.path)


def _record_path(root: Path, relative: str) -> Path:
    if Path(relative).is_absolute() or ".." in Path(relative).parts:
        raise ValueError(f"record leaves the corpus: {relative}")
    path = root / relative
    corpus_root = root / "data" / CORPUS
    if path.suffix != ".yaml" or not path.is_file():
        raise ValueError(f"not a corpus YAML file: {relative}")
    try:
        path.resolve().relative_to(corpus_root.resolve())
        path.relative_to(corpus_root)
    except ValueError as exc:
        raise ValueError(f"record leaves the corpus: {relative}") from exc
    if any(parent.is_symlink() for parent in (path, *path.parents) if parent != root.parent):
        raise ValueError(f"symlink in record path: {relative}")
    return path


CATEGORY_FIELD = "habitat_category"


def build_context(root: Path) -> Mapping[str, str]:
    """Resolve parents consistently in full and canary exports, never from IDs."""
    import csv

    labels = {}
    terms = root / "data" / "raw" / "ontology_terms.tsv"
    if terms.exists():
        with terms.open(encoding="utf-8", newline="") as handle:
            labels.update((row["term_id"], row["label"]) for row in csv.DictReader(handle, delimiter="\t"))
    # Habitat's small corpus supplies labels for minted parent identifiers;
    # selection must not change a record's text hash by removing its parent.
    for path in _discover(root / "data" / CORPUS):
        record = _load(path)
        labels[record["identifier"]] = record["label"]
    return labels


def semantic_text(record: dict, context: Mapping[str, str] | None = None) -> str:
    context = context or {}
    lines = [
        f"name: {clean(record['label'])}",
        f"definition: {clean(record.get('definition'))}",
        f"habitat category: {clean(record.get(CATEGORY_FIELD)).lower().replace('_', ' ')}",
    ]
    synonyms = sorted({clean(item.get("synonym_text")) for item in record.get("synonyms") or []} - {""})
    if synonyms:
        lines.append("synonyms: " + "; ".join(synonyms))
    for label in sorted(
        {clean(context.get(identifier)) for identifier in record.get("parent_habitats") or []} - {""}
    ):
        lines.append("broader habitat: " + label)
    for item in record.get("environmental_parameters") or []:
        parameter = clean(item.get("parameter")).lower().replace("_", " ")
        values = []
        if clean(item.get("qualitative_value")):
            values.append(clean(item["qualitative_value"]))
        if item.get("minimum_value") is not None:
            values.append("minimum " + clean(item["minimum_value"]))
        if item.get("maximum_value") is not None:
            values.append("maximum " + clean(item["maximum_value"]))
        unit = clean(item.get("unit"))
        # Unit CURIEs remain paired with numeric bounds: stripping a unit
        # would change the meaning of a measurement. Other IDs stay excluded.
        if unit:
            values.append("unit " + unit)
        if parameter:
            lines.append(
                "environmental parameter: " + parameter + ("; " + "; ".join(values) if values else "")
            )
    for item in record.get("characteristic_taxa") or []:
        label = clean(item.get("taxon_label"))
        if label:
            relation = "characteristic taxon" if item.get("is_characteristic") is True else "observed taxon"
            lines.append(f"{relation}: {label}")
    return "\n".join(line for line in lines if not line.endswith(": ")) + "\n"


def page_target(record: dict) -> str:
    # Same identity-derived slug as scripts/render_pages.py, not the YAML stem.
    label_id = f"{record['label']}-{record['identifier']}".lower()
    slug = re.sub(r"[^a-z0-9]+", "-", label_id).strip("-") or "unnamed"
    return "habitats/" + quote(slug, safe="-") + ".html"


def iter_inputs(
    root: Path = REPO_ROOT, *, records: list[str] | None = None, limit: int | None = None
) -> Iterator[dict]:
    """Yield the exact fleet JSONL contract, with stable order and unique IDs."""
    root = root.resolve()
    corpus_root = root / "data" / CORPUS
    if not corpus_root.is_dir() or corpus_root.is_symlink() or (root / "data").is_symlink():
        raise ValueError(f"missing real corpus directory: {corpus_root}")
    if limit is not None and limit < 1:
        raise ValueError("limit must be a positive integer")
    context = build_context(root)
    with tempfile.TemporaryDirectory(prefix="habitatmech-map-inputs-") as directory:
        connection = sqlite3.connect(str(Path(directory) / "index.sqlite"))
        try:
            connection.execute("CREATE TABLE paths (path TEXT PRIMARY KEY)")
            connection.execute("CREATE TABLE ids (identifier TEXT PRIMARY KEY)")
            paths = (_record_path(root, path) for path in records) if records else _discover(corpus_root)
            for path in paths:
                relative = path.relative_to(root).as_posix()
                try:
                    connection.execute("INSERT INTO paths VALUES (?)", (relative,))
                except sqlite3.IntegrityError as exc:
                    raise ValueError(f"duplicate selected path: {relative}") from exc
            connection.commit()
            query = "SELECT path FROM paths ORDER BY path"
            if limit is not None:
                query += " LIMIT ?"
            for (relative,) in connection.execute(query, (limit,) if limit is not None else ()):
                record = _load(_record_path(root, relative))
                identifier = record["identifier"]
                try:
                    connection.execute("INSERT INTO ids VALUES (?)", (identifier,))
                except sqlite3.IntegrityError as exc:
                    raise ValueError(f"duplicate record identifier: {identifier}") from exc
                text = semantic_text(record, context)
                yield {
                    "identifier": identifier,
                    "label": clean(record["label"]),
                    "category": clean(record.get(CATEGORY_FIELD)) or "UNKNOWN",
                    "page": page_target(record),
                    "source_path": relative,
                    "text": text,
                    "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                    "adapter_version": ADAPTER_VERSION,
                }
        finally:
            connection.close()


def export_inputs(
    root: Path, output: Path | None, *, records: list[str] | None = None, limit: int | None = None
) -> dict:
    """Validate a preview or atomically publish JSONL after all rows pass."""
    destination = output.resolve() if output is not None else None
    if destination is not None and destination.suffix != ".jsonl":
        raise ValueError("output must have a .jsonl suffix")
    temporary = None
    handle = None
    digest = hashlib.sha256()
    count = 0
    try:
        with ExitStack() as stack:
            if destination is not None:
                destination.parent.mkdir(parents=True, exist_ok=True)
                handle = stack.enter_context(
                    tempfile.NamedTemporaryFile(
                        mode="wb",
                        prefix=".text-map-",
                        dir=destination.parent,
                        delete=False,
                    )
                )
                temporary = Path(handle.name)
            for record in iter_inputs(root, records=records, limit=limit):
                payload = (json.dumps(record, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")
                digest.update(payload)
                count += 1
                if handle is not None:
                    handle.write(payload)
            if not count:
                raise ValueError("selection contains no corpus records")
            if handle is not None:
                handle.close()
                temporary.replace(destination)
            return {
                "mode": "export" if destination is not None else "preview",
                "scope": "subset" if records or limit is not None else "full",
                "records": count,
                "adapter_version": ADAPTER_VERSION,
                "jsonl_sha256": digest.hexdigest(),
                "output": str(destination) if destination is not None else None,
            }
    finally:
        if handle is not None:
            handle.close()
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPO_ROOT, help="repository containing data/" + CORPUS)
    parser.add_argument("--output", type=Path, help="publish JSONL atomically; otherwise validate a preview")
    parser.add_argument(
        "--record", action="append", help="repo-relative YAML path; repeat for a canary subset"
    )
    parser.add_argument(
        "--limit", type=int, help="canary: select this many paths before parsing selected records"
    )
    args = parser.parse_args(argv)
    try:
        result = export_inputs(args.root, args.output, records=args.record, limit=args.limit)
    except (OSError, ValueError, yaml.YAMLError, sqlite3.Error) as exc:
        print(f"text-map inputs refused: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
