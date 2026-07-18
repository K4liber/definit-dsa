from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.reordering import REORDERING
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _Permutation(Definition):
    def _get_content(self) -> str:
        return f"""
A {REORDERING.key.get_reference("reordering")} of the elements of a
{SEQUENCE.key.get_reference("sequence")}, i.e., the same elements arranged in a different order.

---

The {SEQUENCE.key.get_reference("sequence")} "1, 2, 3" has six permutations: 
"1, 2, 3", "1, 3, 2", "2, 1, 3", "2, 3, 1", "3, 1, 2", and "3, 2, 1", each a {REORDERING.key.get_reference()} of 
the same three elements.
"""


PERMUTATION = _Permutation(
    key=DefinitionKey(
        name="permutation",
        field=FieldName.MATHEMATICS,
    )
)
