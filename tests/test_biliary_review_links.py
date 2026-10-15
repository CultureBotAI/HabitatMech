"""Keep the reviewed cohort's issue links outside prose punctuation (#2179)."""

from jinja2 import Environment

from habitatmech import seed


def test_new_review_issue_links_have_exact_targets():
    rows = [
        *seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH).values(),
        *seed.load_definition_source_label_exclusions(
            seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
        ).values(),
        *seed.load_record_annotation_corrections(seed.RECORD_ANNOTATION_CORRECTIONS_PATH),
    ]
    template = Environment(autoescape=True).from_string("{{ changes|urlize }}")
    counts = {}
    for number, expected in [(2177, 14), (2173, 2), (2174, 2)]:
        url = f"https://github.com/CultureBotAI/HabitatMech/issues/{number}"
        notes = [row.notes for row in rows if url in row.notes]
        assert len(notes) == expected
        for note in notes:
            rendered = template.render(changes=note)
            assert f'href="{url}"' in rendered
            assert f'href="{url}:"' not in rendered
        counts[number] = len(notes)
    assert sum(counts.values()) == 18
