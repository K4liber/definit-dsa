from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT


class _Node(Definition):
    def _get_content(self) -> str:
        return f"""
A node (also called vertex) is an abstract entity that can represent an {OBJECT.key.get_reference(phrase="object")} 
or position in a structure. It does not imply any connections or context on its own.

---

Consider three cities labeled "A", "B", and "C". Each city is an {OBJECT.key.get_reference(phrase="object")} 
that we place in a structure as a node.
"""


NODE = _Node(
    key=DefinitionKey(
        name="node",
        field=FieldName.MATHEMATICS,
    )
)
