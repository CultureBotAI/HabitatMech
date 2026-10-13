"""Exact-scope microbial-mat, lake-layer and qualifier curation regressions."""

from dataclasses import replace

import pytest

from habitatmech import seed

CASES = {
    "ENVO:00000275": {
        "removed": ["ENVO:00001999"],
        "retained": ["ENVO:01000649"],
        "slug": "ocean_trench",
        "sources": [{"removed": "ENVO:00001999", "source": "habitatmech:GOLD.5c7c5ceae2"}],
    },
    "habitatmech:GOLD.086ba0a00d": {
        "removed": ["habitatmech:GOLD.c085f6141a"],
        "retained": ["ENVO:01000008"],
        "slug": "microbial_mats__8cd68d16",
        "sources": [{"removed": "habitatmech:GOLD.c085f6141a", "source": "habitatmech:GOLD.086ba0a00d"}],
    },
    "habitatmech:GOLD.0946b92f8f": {
        "decision": {
            "new": {
                "category": "",
                "curator": "codex-gpt-5",
                "date": "2026-10-12",
                "decision": "GROUND_AS_PARENT",
                "grounding_status": "NARROW",
                "identifier": "habitatmech:GOLD.0946b92f8f",
                "notes": "Exact-source ITEM assessment "
                "https://github.com/CultureBotAI/HabitatMech/issues/1409 "
                "(20261012T073340Z-mine_pit_pond). "
                "Mine pit pond: later asbestos-mine "
                "pond-water samples support a real "
                "pond. The CLASS-only decision "
                "omits a pond genus; the existing "
                "Alkaline parent is a non-habitat "
                "qualifier, not pond identity. Use "
                "the verified broader genus "
                "ENVO:00000033 pond; retain the "
                "source mint rather than "
                "exact-merge. Official ENVO labels "
                "and typed synonyms were inspected. "
                "Separate guarded exclusions remove "
                "false context ancestry. "
                "Mapping-endpoint issue #1398 "
                "remains open; this decision is not "
                "export certification.",
                "object_id": "ENVO:00000033",
                "object_label": "pond",
                "relation": "parent",
                "review_depth": "ITEM",
            },
            "old": {
                "category": "",
                "curator": "claude-opus-5",
                "date": "2026-08-12",
                "decision": "CONFIRM_UNGROUNDED",
                "grounding_status": "",
                "identifier": "habitatmech:GOLD.0946b92f8f",
                "notes": "Class-level sweep (see "
                "docs/HARMONIZATION.md#class-level-sweep): "
                "no term in the vendored slice "
                "matched this label by any search "
                "route. Whether the concept is a "
                "habitat at all was NOT assessed, "
                "so this is not yet a term-request "
                "candidate.",
                "object_id": "",
                "object_label": "",
                "relation": "",
                "review_depth": "CLASS",
            },
        },
        "removed": ["habitatmech:GOLD.94b8786010"],
        "retained": ["ENVO:00000033"],
        "slug": "mine_pit_pond",
        "sources": [{"removed": "habitatmech:GOLD.94b8786010", "source": "habitatmech:GOLD.0946b92f8f"}],
    },
    "habitatmech:GOLD.12b8a9a4c4": {
        "removed": ["habitatmech:GOLD.ce244e62cd"],
        "retained": [],
        "slug": "near_boiling_90c",
        "sources": [{"removed": "habitatmech:GOLD.ce244e62cd", "source": "habitatmech:GOLD.12b8a9a4c4"}],
    },
    "habitatmech:GOLD.17c67a52e1": {
        "removed": ["ENVO:01000263"],
        "retained": ["ENVO:01000008"],
        "slug": "microbial_mats__aba42aab",
        "sources": [{"removed": "ENVO:01000263", "source": "habitatmech:GOLD.17c67a52e1"}],
    },
    "habitatmech:GOLD.2a0de7e155": {
        "decision": {
            "new": {
                "category": "",
                "curator": "codex-gpt-5",
                "date": "2026-10-12",
                "decision": "GROUND_AS_PARENT",
                "grounding_status": "NARROW",
                "identifier": "habitatmech:GOLD.2a0de7e155",
                "notes": "Exact-source ITEM assessment "
                "https://github.com/CultureBotAI/HabitatMech/issues/1403 "
                "(20261012T073303Z-microbial_mats__a56a2e1b). "
                "Soda-lake mat: the ITEM rationale "
                "addresses the containing lake "
                "instead of the mat. Later "
                "Rhodobaca and Roseinatronobacter "
                "samples explicitly name bacterial "
                "mats; replace the saline-lake "
                "genus with microbial mat and "
                "independently remove the "
                "lake-context edge. Use the "
                "verified broader genus "
                "ENVO:01000008 microbial mat; "
                "retain the source mint rather than "
                "exact-merge. Official ENVO labels "
                "and typed synonyms were inspected. "
                "Separate guarded exclusions remove "
                "false context ancestry. "
                "Mapping-endpoint issue #1398 "
                "remains open; this decision is not "
                "export certification.",
                "object_id": "ENVO:01000008",
                "object_label": "microbial mat",
                "relation": "parent",
                "review_depth": "ITEM",
            },
            "old": {
                "category": "",
                "curator": "claude-opus-5",
                "date": "2026-08-13",
                "decision": "GROUND_AS_PARENT",
                "grounding_status": "NARROW",
                "identifier": "habitatmech:GOLD.2a0de7e155",
                "notes": "A soda lake is a specific alkaline "
                "saline lake; merging it into "
                "saline lake loses the distinction "
                "and ENVO has no soda-lake term. "
                "Path: Environmental > Aquatic > "
                "Non-marine Saline and Alkaline > "
                "Soda lake > Microbi",
                "object_id": "ENVO:00000019",
                "object_label": "saline lake",
                "relation": "",
                "review_depth": "ITEM",
            },
        },
        "removed": ["habitatmech:GOLD.b11bdfbd7c"],
        "retained": ["ENVO:01000008"],
        "slug": "microbial_mats__a56a2e1b",
        "sources": [{"removed": "habitatmech:GOLD.b11bdfbd7c", "source": "habitatmech:GOLD.2a0de7e155"}],
    },
    "habitatmech:GOLD.2c1e36b661": {
        "removed": ["habitatmech:GOLD.3098ee8fe8"],
        "retained": ["ENVO:01000008"],
        "slug": "microbial_mats__cfca43d0",
        "sources": [{"removed": "habitatmech:GOLD.3098ee8fe8", "source": "habitatmech:GOLD.2c1e36b661"}],
    },
    "habitatmech:GOLD.2d24faa338": {
        "removed": ["habitatmech:GOLD.3098ee8fe8"],
        "retained": ["ENVO:03600064"],
        "slug": "microbialites",
        "sources": [{"removed": "habitatmech:GOLD.3098ee8fe8", "source": "habitatmech:GOLD.2d24faa338"}],
    },
    "habitatmech:GOLD.38e159af25": {
        "removed": ["ENVO:00000195"],
        "retained": ["ENVO:01000008"],
        "slug": "microbial_mats__74823fe8",
        "sources": [{"removed": "ENVO:00000195", "source": "habitatmech:GOLD.38e159af25"}],
    },
    "habitatmech:GOLD.511058ef1e": {
        "removed": ["habitatmech:GOLD.c085f6141a"],
        "retained": [],
        "slug": "neutral",
        "sources": [{"removed": "habitatmech:GOLD.c085f6141a", "source": "habitatmech:GOLD.511058ef1e"}],
    },
    "habitatmech:GOLD.58a0fb1252": {
        "decision": {
            "new": {
                "category": "",
                "curator": "codex-gpt-5",
                "date": "2026-10-12",
                "decision": "GROUND_AS_PARENT",
                "grounding_status": "NARROW",
                "identifier": "habitatmech:GOLD.58a0fb1252",
                "notes": "Exact-source ITEM assessment "
                "https://github.com/CultureBotAI/HabitatMech/issues/1410 "
                "(20261012T073346Z-mixolimnion_top_layer). "
                "Mixolimnion: the circulating upper "
                "layer of a meromictic lake is part "
                "of, not a kind of, the entire "
                "lake. Lake layer is a supported "
                "genus; thermal epilimnion is not "
                "an automatic exact synonym. "
                "Literature from a brackish "
                "Norwegian lake is not evidence for "
                "freshwater-source taxa or measured "
                "conditions. Use the verified "
                "broader genus ENVO:01000283 lake "
                "layer; retain the source mint "
                "rather than exact-merge. Official "
                "ENVO labels and typed synonyms "
                "were inspected. Separate guarded "
                "exclusions remove false context "
                "ancestry. Mapping-endpoint issue "
                "#1398 remains open; this decision "
                "is not export certification.",
                "object_id": "ENVO:01000283",
                "object_label": "lake layer",
                "relation": "parent",
                "review_depth": "ITEM",
            },
            "old": {
                "category": "",
                "curator": "claude-opus-5",
                "date": "2026-08-12",
                "decision": "CONFIRM_UNGROUNDED",
                "grounding_status": "",
                "identifier": "habitatmech:GOLD.58a0fb1252",
                "notes": "Class-level sweep (see "
                "docs/HARMONIZATION.md#class-level-sweep): "
                "no term in the vendored slice "
                "matched this label by any search "
                "route. Whether the concept is a "
                "habitat at all was NOT assessed, "
                "so this is not yet a term-request "
                "candidate.",
                "object_id": "",
                "object_label": "",
                "relation": "",
                "review_depth": "CLASS",
            },
        },
        "removed": ["ENVO:00000199"],
        "retained": ["ENVO:01000283"],
        "slug": "mixolimnion_top_layer",
        "sources": [{"removed": "ENVO:00000199", "source": "habitatmech:GOLD.58a0fb1252"}],
    },
    "habitatmech:GOLD.5d5cab5f31": {
        "decision": {
            "new": {
                "category": "",
                "curator": "codex-gpt-5",
                "date": "2026-10-12",
                "decision": "GROUND_AS_PARENT",
                "grounding_status": "NARROW",
                "identifier": "habitatmech:GOLD.5d5cab5f31",
                "notes": "Exact-source ITEM assessment "
                "https://github.com/CultureBotAI/HabitatMech/issues/1409 "
                "(20261012T073336Z-mine_pit_lake). "
                "Mine pit lake: a real lake formed "
                "in a mine pit, not automatically a "
                "purpose-built reservoir. The "
                "CLASS-only unmatched decision "
                "omits a supported lake genus and "
                "ITEM assessment. Retain the "
                "separate Pit lake grouping and "
                "both source nodes. Use the "
                "verified broader genus "
                "ENVO:00000020 lake; retain the "
                "source mint rather than "
                "exact-merge. Official ENVO labels "
                "and typed synonyms were inspected. "
                "Separate guarded exclusions remove "
                "false context ancestry. "
                "Mapping-endpoint issue #1398 "
                "remains open; this decision is not "
                "export certification.",
                "object_id": "ENVO:00000020",
                "object_label": "lake",
                "relation": "parent",
                "review_depth": "ITEM",
            },
            "old": {
                "category": "",
                "curator": "claude-opus-5",
                "date": "2026-08-12",
                "decision": "CONFIRM_UNGROUNDED",
                "grounding_status": "",
                "identifier": "habitatmech:GOLD.5d5cab5f31",
                "notes": "Class-level sweep (see "
                "docs/HARMONIZATION.md#class-level-sweep): "
                "no term in the vendored slice "
                "matched this label by any search "
                "route. Whether the concept is a "
                "habitat at all was NOT assessed, "
                "so this is not yet a term-request "
                "candidate.",
                "object_id": "",
                "object_label": "",
                "relation": "",
                "review_depth": "CLASS",
            },
        },
        "removed": [],
        "retained": ["ENVO:00000020", "habitatmech:GOLD.5b56a06a4c"],
        "slug": "mine_pit_lake",
        "sources": [],
    },
    "habitatmech:GOLD.7614a6580e": {
        "removed": ["ENVO:01001319"],
        "retained": ["ENVO:01000008"],
        "slug": "microbial_mats__59ad9a00",
        "sources": [{"removed": "ENVO:01001319", "source": "habitatmech:GOLD.7614a6580e"}],
    },
    "habitatmech:GOLD.82ed8aa45e": {
        "removed": ["habitatmech:GOLD.486b52b120"],
        "retained": [],
        "slug": "neutral__819b9d53",
        "sources": [{"removed": "habitatmech:GOLD.486b52b120", "source": "habitatmech:GOLD.82ed8aa45e"}],
    },
    "habitatmech:GOLD.8b53067bc5": {
        "removed": ["ENVO:00000051"],
        "retained": [],
        "slug": "near_boiling_90c__f7b76591",
        "sources": [{"removed": "ENVO:00000051", "source": "habitatmech:GOLD.8b53067bc5"}],
    },
    "habitatmech:GOLD.9dbf296a4a": {
        "removed": ["ENVO:00001999"],
        "retained": ["ENVO:00000402"],
        "slug": "mud_volcano__980e0b1f",
        "sources": [{"removed": "ENVO:00001999", "source": "habitatmech:GOLD.9dbf296a4a"}],
    },
    "habitatmech:GOLD.9e03d49b70": {
        "removed": ["ENVO:00000019"],
        "retained": ["ENVO:01000008"],
        "slug": "microbial_mats__884c9c12",
        "sources": [{"removed": "ENVO:00000019", "source": "habitatmech:GOLD.9e03d49b70"}],
    },
    "habitatmech:GOLD.a00c47c576": {
        "decision": {
            "new": {
                "category": "",
                "curator": "codex-gpt-5",
                "date": "2026-10-12",
                "decision": "GROUND_AS_PARENT",
                "grounding_status": "NARROW",
                "identifier": "habitatmech:GOLD.a00c47c576",
                "notes": "Exact-source ITEM assessment "
                "https://github.com/CultureBotAI/HabitatMech/issues/1403 "
                "(20261012T073301Z-microbial_mats__a2a31086). "
                "Crystallizer-pond mat: the ITEM "
                "decision incorrectly uses a pond "
                "rationale and hypersaline-water "
                "genus. Later Guerrero Negro "
                "mat-depth samples support ENVO "
                "microbial mat, not liquid water or "
                "a whole pond. Use the verified "
                "broader genus ENVO:01000008 "
                "microbial mat; retain the source "
                "mint rather than exact-merge. "
                "Official ENVO labels and typed "
                "synonyms were inspected. Separate "
                "guarded exclusions remove false "
                "context ancestry. Mapping-endpoint "
                "issue #1398 remains open; this "
                "decision is not export "
                "certification.",
                "object_id": "ENVO:01000008",
                "object_label": "microbial mat",
                "relation": "parent",
                "review_depth": "ITEM",
            },
            "old": {
                "category": "",
                "curator": "claude-opus-5",
                "date": "2026-08-13",
                "decision": "GROUND_AS_PARENT",
                "grounding_status": "NARROW",
                "identifier": "habitatmech:GOLD.a00c47c576",
                "notes": "A salt crystallizer pond is a "
                "specific hypersaline evaporation "
                "pond, narrower than saline water "
                "generally. Path: Environmental > "
                "Aquatic > Non-marine Saline and "
                "Alkaline > Salt crystallizer p",
                "object_id": "ENVO:00002012",
                "object_label": "hypersaline water",
                "relation": "",
                "review_depth": "ITEM",
            },
        },
        "removed": ["habitatmech:GOLD.277843111f"],
        "retained": ["ENVO:01000008"],
        "slug": "microbial_mats__a2a31086",
        "sources": [{"removed": "habitatmech:GOLD.277843111f", "source": "habitatmech:GOLD.a00c47c576"}],
    },
    "habitatmech:GOLD.a0372e2d63": {
        "removed": ["ENVO:00000051"],
        "retained": ["ENVO:01000008"],
        "slug": "microbial_mats__522cc2c0",
        "sources": [{"removed": "ENVO:00000051", "source": "habitatmech:GOLD.a0372e2d63"}],
    },
    "habitatmech:GOLD.ae0db57f4a": {
        "removed": ["ENVO:00000207"],
        "retained": ["ENVO:01000008"],
        "slug": "microbial_mats__7a576572",
        "sources": [{"removed": "ENVO:00000207", "source": "habitatmech:GOLD.ae0db57f4a"}],
    },
    "habitatmech:GOLD.af1854714b": {
        "removed": ["habitatmech:GOLD.94b8786010"],
        "retained": ["ENVO:01000008"],
        "slug": "microbial_mats__66f27e00",
        "sources": [{"removed": "habitatmech:GOLD.94b8786010", "source": "habitatmech:GOLD.af1854714b"}],
    },
    "habitatmech:GOLD.b3e7b4ce80": {
        "removed": ["ENVO:00000215"],
        "retained": ["ENVO:01000008"],
        "slug": "microbial_mats__aaf3c430",
        "sources": [{"removed": "ENVO:00000215", "source": "habitatmech:GOLD.b3e7b4ce80"}],
    },
    "habitatmech:GOLD.b76e4c6e4a": {
        "removed": ["ENVO:00000199"],
        "retained": ["ENVO:01000008"],
        "slug": "microbial_mats__2265bbbd",
        "sources": [{"removed": "ENVO:00000199", "source": "habitatmech:GOLD.b76e4c6e4a"}],
    },
    "habitatmech:GOLD.bcbb2a8929": {
        "removed": ["habitatmech:GOLD.115edc36f8"],
        "retained": ["ENVO:03600064"],
        "slug": "microbialites__2dd0659e",
        "sources": [{"removed": "habitatmech:GOLD.115edc36f8", "source": "habitatmech:GOLD.bcbb2a8929"}],
    },
    "habitatmech:GOLD.bef53c8bcc": {
        "removed": ["habitatmech:GOLD.09350714a0"],
        "retained": ["ENVO:01000008"],
        "slug": "microbial_mats__42c901d2",
        "sources": [{"removed": "habitatmech:GOLD.09350714a0", "source": "habitatmech:GOLD.bef53c8bcc"}],
    },
    "habitatmech:GOLD.c0eea2809c": {
        "removed": ["habitatmech:GOLD.d250342fe1"],
        "retained": ["ENVO:01000008"],
        "slug": "microbial_mats__c3f0268a",
        "sources": [{"removed": "habitatmech:GOLD.d250342fe1", "source": "habitatmech:GOLD.c0eea2809c"}],
    },
    "habitatmech:GOLD.c8481605f8": {
        "removed": ["ENVO:01001020"],
        "retained": ["ENVO:01000008"],
        "slug": "microbial_mats__d16dafc1",
        "sources": [{"removed": "ENVO:01001020", "source": "habitatmech:GOLD.c8481605f8"}],
    },
    "habitatmech:GOLD.ce244e62cd": {
        "definition": {
            "new": {
                "curator": "codex-gpt-5",
                "date": "2026-10-12",
                "definition": "An aquatic environment "
                "which is determined by an "
                "inland water body whose "
                "water is substantially more "
                "saline than fresh water, "
                "substantially more alkaline "
                "than circumneutral water, "
                "or both.",
                "exact_synonym": "Non-marine Saline and Alkaline",
                "identifier": "habitatmech:GOLD.ce244e62cd",
                "notes": "Definition curated from the "
                "committed deep-research report "
                "for this record (#110, #185). "
                "The “or both” wording preserves "
                "GOLD's disjunctive hierarchy "
                "instead of claiming every child "
                "is simultaneously saline and "
                "alkaline. “Inland” is preferred "
                "to “non-marine” because "
                "marine-derived inland brines can "
                "remain geographically inland, "
                "while “athalassohaline” is not "
                "an exact synonym because it "
                "classifies water by ionic "
                "composition rather than "
                "location. Parent replacement is "
                "intentional: GOLD's inherited "
                "aquatic-biome edge is false for "
                "the node's operated-setting "
                "descendants, whereas ENVO's "
                "aquatic-environment genus covers "
                "both natural and engineered "
                "water-determined settings. "
                "Dropped the exact synonym "
                "'Non-marine-Saline-and-Alkaline' "
                "(#213): it is BacDive's label "
                "for the concept GOLD spells "
                "'Non-marine Saline and "
                "Alkaline', and the two differ "
                "only in punctuation. Both source "
                "labels survive on the record's "
                "source_attestations, where they "
                "identify which source said what; "
                "as a pair of EXACT synonyms they "
                "would read to an ENVO editor as "
                "the same string written twice. "
                "Found by the guard added for "
                "this issue, not by the review "
                "that filed it. Scope correction "
                "#1415: remove the three "
                "saline-only exact aliases "
                "because they omit the "
                "alkaline-only arm. Preserve the "
                "disjunctive definition, "
                "aquatic-environment REPLACE "
                "mode, reviewed source merge and "
                "separate assertion units.",
                "parent_class": "ENVO:01000317",
                "parent_label": "aquatic environment",
                "parent_mode": "REPLACE",
                "requested_label": "inland saline or alkaline aquatic environment",
            },
            "old": {
                "curator": "codex-gpt-5",
                "date": "2026-08-25",
                "definition": "An aquatic environment "
                "which is determined by an "
                "inland water body whose "
                "water is substantially more "
                "saline than fresh water, "
                "substantially more alkaline "
                "than circumneutral water, "
                "or both.",
                "exact_synonym": "Non-marine Saline and "
                "Alkaline|inland saline "
                "waters|saline inland "
                "waters|continental "
                "saline waters",
                "identifier": "habitatmech:GOLD.ce244e62cd",
                "notes": "Definition curated from the "
                "committed deep-research report "
                "for this record (#110, #185). "
                "The “or both” wording preserves "
                "GOLD's disjunctive hierarchy "
                "instead of claiming every child "
                "is simultaneously saline and "
                "alkaline. “Inland” is preferred "
                "to “non-marine” because "
                "marine-derived inland brines can "
                "remain geographically inland, "
                "while “athalassohaline” is not "
                "an exact synonym because it "
                "classifies water by ionic "
                "composition rather than "
                "location. Parent replacement is "
                "intentional: GOLD's inherited "
                "aquatic-biome edge is false for "
                "the node's operated-setting "
                "descendants, whereas ENVO's "
                "aquatic-environment genus covers "
                "both natural and engineered "
                "water-determined settings. "
                "Dropped the exact synonym "
                "'Non-marine-Saline-and-Alkaline' "
                "(#213): it is BacDive's label "
                "for the concept GOLD spells "
                "'Non-marine Saline and "
                "Alkaline', and the two differ "
                "only in punctuation. Both source "
                "labels survive on the record's "
                "source_attestations, where they "
                "identify which source said what; "
                "as a pair of EXACT synonyms they "
                "would read to an ENVO editor as "
                "the same string written twice. "
                "Found by the guard added for "
                "this issue, not by the review "
                "that filed it.",
                "parent_class": "ENVO:01000317",
                "parent_label": "aquatic environment",
                "parent_mode": "REPLACE",
                "requested_label": "inland saline or alkaline aquatic environment",
            },
        },
        "removed": [],
        "retained": ["ENVO:01000317"],
        "slug": "non_marine_saline_and_alkaline__0e812745",
        "sources": [],
    },
    "habitatmech:GOLD.e070d4c2be": {
        "decision": {
            "new": {
                "category": "",
                "curator": "codex-gpt-5",
                "date": "2026-10-12",
                "decision": "GROUND_AS_PARENT",
                "grounding_status": "NARROW",
                "identifier": "habitatmech:GOLD.e070d4c2be",
                "notes": "Exact-source ITEM assessment "
                "https://github.com/CultureBotAI/HabitatMech/issues/1410 "
                "(20261012T073348Z-monimolimnion_bottom_layer). "
                "Monimolimnion: the persistently "
                "unmixed deep layer is part of, not "
                "a kind of, a meromictic lake. Lake "
                "layer is a supported genus; "
                "thermal hypolimnion is not "
                "automatically exact. Preserve "
                "distinct source identity and "
                "absent organism counts. Use the "
                "verified broader genus "
                "ENVO:01000283 lake layer; retain "
                "the source mint rather than "
                "exact-merge. Official ENVO labels "
                "and typed synonyms were inspected. "
                "Separate guarded exclusions remove "
                "false context ancestry. "
                "Mapping-endpoint issue #1398 "
                "remains open; this decision is not "
                "export certification.",
                "object_id": "ENVO:01000283",
                "object_label": "lake layer",
                "relation": "parent",
                "review_depth": "ITEM",
            },
            "old": {
                "category": "",
                "curator": "claude-opus-5",
                "date": "2026-08-12",
                "decision": "CONFIRM_UNGROUNDED",
                "grounding_status": "",
                "identifier": "habitatmech:GOLD.e070d4c2be",
                "notes": "Class-level sweep (see "
                "docs/HARMONIZATION.md#class-level-sweep): "
                "no term in the vendored slice "
                "matched this label by any search "
                "route. Whether the concept is a "
                "habitat at all was NOT assessed, "
                "so this is not yet a term-request "
                "candidate.",
                "object_id": "",
                "object_label": "",
                "relation": "",
                "review_depth": "CLASS",
            },
        },
        "removed": ["ENVO:00000199"],
        "retained": ["ENVO:01000283"],
        "slug": "monimolimnion_bottom_layer",
        "sources": [{"removed": "ENVO:00000199", "source": "habitatmech:GOLD.e070d4c2be"}],
    },
    "habitatmech:GOLD.f46eba7b40": {
        "removed": ["ENVO:01001020"],
        "retained": ["ENVO:03600064"],
        "slug": "microbialites__b8560cfd",
        "sources": [{"removed": "ENVO:01001020", "source": "habitatmech:GOLD.f46eba7b40"}],
    },
    "habitatmech:GOLD.ffea544c70": {
        "removed": ["ENVO:00000021"],
        "retained": ["ENVO:01000008"],
        "slug": "microbial_mats__54849ba0",
        "sources": [{"removed": "ENVO:00000021", "source": "habitatmech:GOLD.ffea544c70"}],
    },
}


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_corrections_change_only_the_thirty_one_reviewed_records(documents, monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    sources = {s["source"] for case in CASES.values() for s in case["sources"]}
    assert len(CASES) == 31 and len(sources) == 29
    old_decisions = dict(decisions)
    old_definitions = dict(definitions)
    for identifier, case in CASES.items():
        if "decision" in case:
            old = dict(case["decision"]["old"])
            old["relation"] = old["relation"] or "parent"
            old_decisions[identifier] = seed.Decision(**old)
        if "definition" in case:
            old = case["definition"]["old"]
            old_definitions[identifier] = replace(
                definitions[identifier],
                exact_synonyms=tuple(old["exact_synonym"].split("|")),
                curator=old["curator"],
                date=old["date"],
                notes=old["notes"],
            )
    monkeypatch.setattr(
        seed,
        "load_gold_parent_exclusions",
        lambda _: {k: v for k, v in exclusions.items() if k not in sources},
    )
    monkeypatch.setattr(seed, "load_decisions", lambda _: old_decisions)
    monkeypatch.setattr(seed, "load_curated_definitions", lambda _: old_definitions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {key for key in before if before[key] != documents[key]} == CASES.keys()
    for identifier, case in CASES.items():
        old, new = before[identifier], documents[identifier]
        allowed = {"parent_habitats", "curation_history"}
        if "decision" in case:
            allowed |= {"grounding_status", "mapping_status", "source_attestations"}
            assert new["grounding_status"] == "NARROW"
            assert new["mapping_status"] == "REVIEWED"
            old_attestations = [
                {k: v for k, v in a.items() if k != "mapping_predicate"} for a in old["source_attestations"]
            ]
            new_attestations = [
                {k: v for k, v in a.items() if k != "mapping_predicate"} for a in new["source_attestations"]
            ]
            assert old_attestations == new_attestations
            assert all(a["mapping_predicate"] == "skos:narrowMatch" for a in new["source_attestations"])
        if "definition" in case:
            allowed.add("synonyms")
            removed = {"inland saline waters", "saline inland waters", "continental saline waters"}
            assert new["synonyms"] == [s for s in old["synonyms"] if s["synonym_text"] not in removed]
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        assert new.get("parent_habitats", []) == case["retained"]


@pytest.mark.parametrize("identifier", CASES)
def test_exact_sources_counts_and_parent_guards(identifier, documents):
    case = CASES[identifier]
    doc = documents[identifier]
    assert doc.get("parent_habitats", []) == case["retained"]
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    for source in case["sources"]:
        row = exclusions[source["source"]]
        assert seed.mint("GOLD", row.source_path) == source["source"]
        assert row.parent_id == source["removed"]
        raw = next(
            r for r in seed.read_tsv("gold_ecosystem_paths.tsv") if r["canonical_path"] == row.source_path
        )
        attestation = next(a for a in doc["source_attestations"] if a.get("source_path") == row.source_path)
        assert attestation["source_id"] == raw["gold_node_ids"].split("|")[0]
        if int(raw["organism_count"]):
            assert attestation["assertion_count"] == int(raw["organism_count"])
            assert attestation["assertion_unit"] == "ORGANISM"
        else:
            assert "assertion_count" not in attestation and "assertion_unit" not in attestation
        assert any(row.notes in e["changes"] for e in doc["curation_history"])


def test_corrected_mat_genera_and_unresolved_environment_scope(documents):
    for identifier, case in CASES.items():
        if case["slug"].startswith("microbial_mats"):
            assert documents[identifier]["parent_habitats"] == ["ENVO:01000008"]
    assert documents["habitatmech:GOLD.df20aa5a67"]["parent_habitats"] == ["ENVO:01000008", "ENVO:01001043"]
    assert documents["habitatmech:GOLD.51de99d734"]["parent_habitats"] == ["ENVO:01001043", "ENVO:03600064"]
    assert documents["habitatmech:GOLD.e53e2c6e8e"]["parent_habitats"] == ["ENVO:03600064"]


def test_pit_lake_and_layers_keep_distinct_identities(documents):
    assert documents["habitatmech:GOLD.5d5cab5f31"]["parent_habitats"] == [
        "ENVO:00000020",
        "habitatmech:GOLD.5b56a06a4c",
    ]
    assert documents["habitatmech:GOLD.0946b92f8f"]["parent_habitats"] == ["ENVO:00000033"]
    for identifier in ("habitatmech:GOLD.58a0fb1252", "habitatmech:GOLD.e070d4c2be"):
        assert documents[identifier]["identifier"] == identifier
        assert documents[identifier]["parent_habitats"] == ["ENVO:01000283"]


def test_saline_or_alkaline_scope_preserves_merge_and_taxon_pool(documents):
    doc = documents["habitatmech:GOLD.ce244e62cd"]
    assert "or both" in doc["definition"] and doc["parent_habitats"] == ["ENVO:01000317"]
    assert {(a["assertion_unit"], a["assertion_count"]) for a in doc["source_attestations"]} == {
        ("ORGANISM", 121),
        ("STRAIN", 37),
    }
    assert len(doc["characteristic_taxa"]) == 25
    assert not any("PATO:0001430" in str(x) for x in doc.get("ontology_xrefs", []))
