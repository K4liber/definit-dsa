from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.data_type import DATA_TYPE
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _PrimitiveDataType(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a basic {DATA_TYPE.key.get_reference(phrase="data type")} whose values are atomic and 
cannot be decomposed into simpler parts. The {SET.key.get_reference(phrase="set")} of primitive data types forms the 
foundation from which all other data types are constructed.

---

For example, a primitive data type might represent truth values (with only two possible values), individual characters, 
or whole {NUMBER.key.get_reference(phrase="numbers")} within a fixed range. Each value of such a type is treated as an indivisible unit: unlike a composite 
type, it cannot be broken down into smaller named components.
"""


PRIMITIVE_DATA_TYPE = _PrimitiveDataType(
    key=DefinitionKey(
        name="primitive_data_type",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
