from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.data.field.mathematics.definitions.fundamental.uniqueness import UNIQUENESS


class _Bijection(Definition):
    def _get_content(self) -> str:
        return f"""
A bijection is a {FUNCTION.key.get_reference(phrase="function")} between two 
{SET.key.get_reference(phrase="sets")} that pairs every {ITEM.key.get_reference(phrase="element")} of the first set 
with exactly one element of the second set, and every element of the second set with exactly one element of the first 
set. In other words, it preserves {UNIQUENESS.key.get_reference(phrase="uniqueness")} in both directions.

---

The {FUNCTION.key.get_reference(phrase="function")} f(x) = x + 1 is a bijection from the 
{SET.key.get_reference(phrase="set")} of integers to itself: every integer n maps to a unique integer n+1, and every 
integer is reached by exactly one input.

The mapping {{A↔1, B↔2, C↔3}} is a bijection between the {SET.key.get_reference(phrase="sets")} {{A, B, C}}
and {{1, 2, 3}}: each element is paired with exactly one element on the other side.
"""


BIJECTION = _Bijection(
    key=DefinitionKey(
        name="bijection",
        field=FieldName.MATHEMATICS,
    ),
    aliases=("bijective function", "one-to-one correspondence"),
)
