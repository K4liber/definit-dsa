from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _Square(Definition):
    def _get_content(self) -> str:
        return f"""
The square of a {NUMBER.key.get_reference(phrase="number")} is the result of multiplying that number by itself
(written n² = n × n).

---

3² = 3 × 3 = 9

5² = 5 × 5 = 25

7² = 7 × 7 = 49
"""


SQUARE = _Square(
    key=DefinitionKey(
        name="square",
        field=FieldName.MATHEMATICS,
    )
)
