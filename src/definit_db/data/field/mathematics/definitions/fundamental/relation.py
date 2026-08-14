from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName


class _Relation(Definition):
    def _get_content(self) -> str:
        return f"""
A relation (also called relationship) describes a connection or association between elements of a 
collection or set.

---

"is less than" is a relation. Applying it to the collection 
(1, 2, 3) it connects 1 to 2, 1 to 3, and 2 to 3.
"""


RELATION = _Relation(
    key=DefinitionKey(
        name="relation",
        field=FieldName.MATHEMATICS,
    )
)
