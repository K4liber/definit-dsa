from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.combination import COMBINATION
from definit_db.data.field.mathematics.definitions.fundamental.factorial import FACTORIAL
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.permutation import PERMUTATION


class _Combinatorics(Definition):
    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a branch of mathematics concerned with counting, arranging, and selecting
{OBJECT.key.get_reference("objects")}. It studies concepts such as 
{PERMUTATION.key.get_reference("permutations")}, {COMBINATION.key.get_reference("combinations")} and 
{FACTORIAL.key.get_reference("factorials")}.
"""


COMBINATORICS = _Combinatorics(
    key=DefinitionKey(
        name="combinatorics",
        field=FieldName.MATHEMATICS,
    )
)
