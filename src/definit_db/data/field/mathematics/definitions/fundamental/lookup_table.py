from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.fundamental.table import TABLE


class _LookupTable(Definition):
    def _get_content(self) -> str:
        return f"""
A {TABLE.key.get_reference()} whose entries store results in advance so they can be retrieved directly instead of
being produced by repeating a {COMPUTATION.key.get_reference()}.

---

A lookup table for squares can store 0 → 0, 1 → 1, 2 → 4, and 3 → 9. Given 3, reading its entry returns 9 directly
instead of {COMPUTATION.key.get_reference("calculating")} 3 × 3 again.
"""


LOOKUP_TABLE = _LookupTable(
    key=DefinitionKey(
        name="lookup table",
        field=FieldName.MATHEMATICS,
    )
)
