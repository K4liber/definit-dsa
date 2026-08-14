from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _Problem(Definition):
    def _get_content(self) -> str:
        return f"""
A question or a challenge defined in a formal way.

---

"Find a {NUMBER.key.get_reference(phrase="number")} that, when multiplied by itself, equals 9" is a problem.
"""


PROBLEM = _Problem(
    key=DefinitionKey(
        name="problem",
        field=FieldName.MATHEMATICS,
    )
)
