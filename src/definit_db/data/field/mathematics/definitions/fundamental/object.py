from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName


class _Object(Definition):
    def _get_content(self) -> str:
        return """
An object is any entity that can be considered, named, or manipulated within a mathematical context.

---

"3" can be named, compared, and used in a statement. We can call it an object.
"""


OBJECT = _Object(
    key=DefinitionKey(
        name="object",
        field=FieldName.MATHEMATICS,
    )
)
