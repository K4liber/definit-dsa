from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.dynamic_programming import DYNAMIC_PROGRAMMING
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.problem.subproblem import SUBPROBLEM


class _OneDimensionalDynamicProgramming(Definition):
    def _get_content(self) -> str:
        return f"""
1D Dynamic Programming is a form of {DYNAMIC_PROGRAMMING.key.get_reference(phrase="dynamic programming")} where each 
{SUBPROBLEM.key.get_reference(phrase="subproblem")} state can be represented by a single {INDEX.key.get_reference()} 
over a {SEQUENCE.key.get_reference()}. It is often used when the recurrence depends on earlier positions in one 
ordered dimension.
"""


ONE_DIMENSIONAL_DYNAMIC_PROGRAMMING = _OneDimensionalDynamicProgramming(
    key=DefinitionKey(
        name="1D Dynamic Programming",
        field=FieldName.MATHEMATICS,
    )
)