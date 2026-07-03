from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.factorial import FACTORIAL
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.permutation import PERMUTATION
from definit_db.data.field.mathematics.definitions.fundamental.set import SET


class _Combination(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a way of selecting {OBJECT.key.get_reference("objects")} from a 
{SET.key.get_reference("set")} where the order of selection does not matter.

Combinations are related to {PERMUTATION.key.get_reference("permutations")} and are often computed using
{FACTORIAL.key.get_reference("factorials")}.

---

Choosing 2 fruits from the {SET.key.get_reference("set")} {{apple, banana, cherry}} gives three 
{self.key.get_reference("combinations")}: {{apple, banana}}, {{apple, cherry}}, and {{banana, cherry}}. Picking 
banana then apple is the same {self.key.get_reference("combination")} as picking apple then banana, since order 
does not matter.
"""


COMBINATION = _Combination(
    key=DefinitionKey(
        name="combination",
        field=FieldName.MATHEMATICS,
    )
)
