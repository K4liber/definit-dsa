from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.factorial import FACTORIAL
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Combination(Definition):
    def _get_content(self) -> str:
        return f"""
A way of selecting {OBJECT.key.get_reference("objects")} from a 
{SET.key.get_reference("set")} where the order of selection does not matter.

The number of ways to choose k {OBJECT.key.get_reference("objects")} from a {SET.key.get_reference("set")}
of n objects, written C(n, k), equals n! / (k! · (n − k)!), using {FACTORIAL.key.get_reference("factorials")}.

---

Choosing 2 fruits from the {SET.key.get_reference("set")} {{apple, banana, cherry}} gives three 
combinations: {{apple, banana}}, {{apple, cherry}}, and {{banana, cherry}}. Picking 
banana then apple is the same combination as picking apple then banana, since order 
does not matter. This matches C(3, 2) = 3! / (2! · 1!) = 3.
"""


COMBINATION = _Combination(
    key=DefinitionKey(
        name="combination",
        field=FieldName.MATHEMATICS,
    )
)
