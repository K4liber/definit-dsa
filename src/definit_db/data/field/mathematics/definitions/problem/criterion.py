from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER


class _Criterion(Definition):
    def _get_content(self) -> str:
        return f"""
A standard or principle by which something is judged or decided.

---

To decide whether a {NUMBER.key.get_reference(phrase="number")} is even, the criterion is whether it is 
divisible by 2: 4 satisfies this criterion, while 7 does not.
"""


CRITERION = _Criterion(
    key=DefinitionKey(
        name="criterion",
        field=FieldName.MATHEMATICS,
    )
)
