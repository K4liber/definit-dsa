from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.square_root import SQUARE_ROOT


class _PerfectSquare(Definition):
    def _get_content(self) -> str:
        return f"""
A {self.key.get_reference()} is a non-negative {INTEGER.key.get_reference("integer")} that can be written as n² for
some integer n.

Equivalently, x is a perfect square if {SQUARE_ROOT.key.get_reference("the square root")} of x is an integer.

---

9 is a {self.key.get_reference()} because 9 = 3², and {SQUARE_ROOT.key.get_reference("the square root")} of 9
is 3 — an {INTEGER.key.get_reference("integer")}.

8 is not a {self.key.get_reference()} because {SQUARE_ROOT.key.get_reference("the square root")} of 8 ≈ 2.83,
which is not an {INTEGER.key.get_reference("integer")}.
"""


PERFECT_SQUARE = _PerfectSquare(
    key=DefinitionKey(
        name="perfect square",
        field=FieldName.MATHEMATICS,
    )
)
