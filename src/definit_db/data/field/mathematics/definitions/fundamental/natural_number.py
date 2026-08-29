from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _NaturalNumber(Definition):
    def _get_content(self) -> str:
        return f"""
A natural {NUMBER.key.get_reference("number")} is a non-negative {INTEGER.key.get_reference("integer")}.

---

Natural numbers: 0, 1, 2, 3, 4, 5, ...

-1 and -5 are not natural numbers — they are negative {INTEGER.key.get_reference("integers")}.
1.5 and π are not natural numbers — they are not {INTEGER.key.get_reference("integers")} at all.
"""


NATURAL_NUMBER = _NaturalNumber(
    key=DefinitionKey(
        name="natural number",
        field=FieldName.MATHEMATICS,
    ),
    aliases=["counting number"],
)
