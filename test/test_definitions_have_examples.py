"""Every definition must include a worked example.

A definition is considered to have an example when its content contains a
standalone ``---`` separator (the convention used during the definition
review). This test guards against regressions: any definition that ships
without an example fails here.

It replaces the former ``scripts/generate_index_review.py`` utility, which
tracked review progress in ``data_md/index_review.md``. Now that every
definition has been reviewed, the example requirement is enforced by this
test instead.
"""

import pytest
from definit.definition.definition import Definition

from definit_db.data.field import FieldName
from definit_db.data.field.index import get_index

_FIELDS = [FieldName.MATHEMATICS, FieldName.COMPUTER_SCIENCE]


def _all_definitions() -> list[Definition]:
    definitions: list[Definition] = []
    for field in _FIELDS:
        definitions.extend(get_index(field).values())
    return definitions


@pytest.mark.parametrize(
    "definition",
    _all_definitions(),
    ids=lambda definition: definition.key.uid,
)
def test_definition_has_example(definition: Definition) -> None:
    has_example = any(line.strip() == "---" for line in definition.content.splitlines())
    assert has_example, (
        f"Definition {definition.key.uid!r} has no example. "
        "Add a worked example below the definition body, separated by a standalone '---' line."
    )
