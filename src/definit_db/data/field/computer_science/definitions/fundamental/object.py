from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data_structure import DATA_STRUCTURE
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _Object(Definition):
    def _get_content(self) -> str:
        return f"""
An instance of a {DATA_STRUCTURE.key.get_reference(phrase="data structure")}.

---

The array (72, 85, 90) is an object: it is one specific instance of the array data structure, holding these
particular {NUMBER.key.get_reference(phrase="numbers")}.
"""


OBJECT = _Object(
    key=DefinitionKey(
        name="object",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
