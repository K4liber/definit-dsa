from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data_structure import DATA_STRUCTURE
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _Object(Definition):
    def _get_content(self) -> str:
        return f"""
A concrete realization of a {DATA_STRUCTURE.key.get_reference(phrase="data structure")}.

---

A {DATA_STRUCTURE.key.get_reference(phrase="data structure")} holding the particular
{NUMBER.key.get_reference(phrase="numbers")} 72, 85, and 90 is an object.
"""


OBJECT = _Object(
    key=DefinitionKey(
        name="object",
        field=FieldName.COMPUTER_SCIENCE,
    ),
    aliases=["instance"],
)
