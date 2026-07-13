from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Domain(Definition):
    def _get_content(self) -> str:
        return f"""
A domain is a {SET.key.get_reference(phrase="set")} of all values for which something is defined, specifying the
inputs or {ITEM.key.get_reference(phrase="elements")} over which it {OPERATION.key.get_reference(phrase="operates")}.

---

For a six-sided die, the domain is the set (1, 2, 3, 4, 5, 6): only those outcomes are possible.
"""


DOMAIN = _Domain(
    key=DefinitionKey(
        name="domain",
        field=FieldName.MATHEMATICS,
    )
)
