from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.dynamic_programming import DYNAMIC_PROGRAMMING
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.one_dimensional_dynamic_programming import (
    ONE_DIMENSIONAL_DYNAMIC_PROGRAMMING,
)
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX
from definit_db.data.field.mathematics.definitions.fundamental.matrix import MATRIX
from definit_db.data.field.mathematics.definitions.problem.subproblem import SUBPROBLEM


class _MultidimensionalDynamicProgramming(Definition):
    def _get_content(self) -> str:
        return f"""
Multidimensional Dynamic Programming is a form of 
{DYNAMIC_PROGRAMMING.key.get_reference(phrase="dynamic programming")} where each 
{SUBPROBLEM.key.get_reference(phrase="subproblem")} state is identified by multiple 
{INDEX.key.get_reference(phrase="indices")}. Unlike 
{ONE_DIMENSIONAL_DYNAMIC_PROGRAMMING.key.get_reference(phrase="1D dynamic programming")}, it stores states across a 
multi-axis structure such as a {MATRIX.key.get_reference()}.
"""


MULTIDIMENSIONAL_DYNAMIC_PROGRAMMING = _MultidimensionalDynamicProgramming(
    key=DefinitionKey(
        name="Multidimensional Dynamic Programming",
        field=FieldName.MATHEMATICS,
    )
)
