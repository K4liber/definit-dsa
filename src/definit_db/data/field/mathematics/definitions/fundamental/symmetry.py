from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.relation import RELATION


class _Symmetry(Definition):
    def _get_content(self) -> str:
        return f"""
Symmetry is a {RELATION.key.get_reference(phrase="relation")} between an 
{OBJECT.key.get_reference(phrase="object")} and an {OPERATION.key.get_reference(phrase="operation")} where applying 
the operation leaves the object unchanged in the aspects being considered. A symmetric object therefore has a 
form or behavior that is preserved under some transformation, such as reflection, rotation, or exchange of parts.
"""


SYMMETRY = _Symmetry(
    key=DefinitionKey(
        name="symmetry",
        field=FieldName.MATHEMATICS,
    )
)
