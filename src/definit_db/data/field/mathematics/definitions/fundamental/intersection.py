from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Intersection(Definition):
    def _get_content(self) -> str:
        return f"""
The {self.key.get_reference()} of two {SET.key.get_reference("sets")} A and B is the set of elements that are in
both A and B.
"""


INTERSECTION = _Intersection(
    key=DefinitionKey(
        name="intersection",
        field=FieldName.MATHEMATICS,
    )
)
