from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION


class _Expression(Definition):
    def _get_content(self) -> str:
        return f"""
A combination of {OBJECT.key.get_reference(phrase="objects")} and
{OPERATION.key.get_reference(phrase="operations")} that represents a value. When evaluated, it produces a result.

---

2 + 3 is an expression: combining the {OBJECT.key.get_reference(phrase="objects")} 2 and 3 with the addition
operation produces the result 5.
"""


EXPRESSION = _Expression(
    key=DefinitionKey(
        name="expression",
        field=FieldName.MATHEMATICS,
    )
)
