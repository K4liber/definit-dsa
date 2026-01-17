from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Union(Definition):
    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} of two {SET.key.get_reference("sets")} A and B is the set of elements that are in
A or in B (or in both).
"""


UNION = _Union(
    key=DefinitionKey(
        name="union",
        field=FieldName.MATHEMATICS,
    )
)
