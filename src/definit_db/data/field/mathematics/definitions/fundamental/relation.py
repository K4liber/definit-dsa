from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Relation(Definition):
    def _get_content(self) -> str:
        return f"""
A relation (also called relationship) describes a connection or association between elements of a 
{SET.key.get_reference(phrase="set(s)")}.

---

"is less than" is a relation on the {SET.key.get_reference(phrase="set")} (1, 2, 3).
It connects 1 to 2, 1 to 3, and 2 to 3.
"""


RELATION = _Relation(
    key=DefinitionKey(
        name="relation",
        field=FieldName.MATHEMATICS,
    )
)
