from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.problem.problem_space import PROBLEM_SPACE


class _LogarithmicComplexity(Definition):
    def _get_content(self) -> str:
        return f"""
A {TIME_COMPLEXITY.key.get_reference("time complexity")} classification where 
an {ALGORITHM.key.get_reference()} performs a number of {OPERATION.key.get_reference("operations")} that grows 
logarithmically with the size of the {INPUT_DATA.key.get_reference("input")}. Expressed in 
{BIG_O_NOTATION.key.get_reference("Big O notation")} as O(log n), logarithmic complexity means that each 
{OPERATION.key.get_reference()} reduces the {PROBLEM_SPACE.key.get_reference("problem space")} by a constant 
factor (typically by half). This is highly {EFFICIENCY.key.get_reference(phrase="efficient")} and commonly seen in 
algorithms that repeatedly divide the problem 
space. Logarithmic complexity is significantly faster than linear complexity, especially for large inputs, as doubling 
the {INPUT_DATA.key.get_reference("input")} size only adds one additional {OPERATION.key.get_reference()}.

---

Starting with a {PROBLEM_SPACE.key.get_reference()} of n = 1,024 and halving it at each {OPERATION.key.get_reference()}:

Step 0: 1,024 elements.

Step 1: 512 elements (divide by 2).

Step 2: 256 elements (divide by 2).

Step 3: 128 elements (divide by 2).

Step 4: 64 elements (divide by 2).

Step 5: 32 elements (divide by 2).

Step 6: 16 elements (divide by 2).

Step 7: 8 elements (divide by 2).

Step 8: 4 elements (divide by 2).

Step 9: 2 elements (divide by 2).

Step 10: 1 element, done.

{NUMBER.key.get_reference("10")} = log₂(1 024) {OPERATION.key.get_reference("operations")} to reduce the 
entire {PROBLEM_SPACE.key.get_reference()}.
Doubling the {INPUT_DATA.key.get_reference("input")} to n = 2 048 adds just one more step (log₂(2 048) = 11).
"""


LOGARITHMIC_COMPLEXITY = _LogarithmicComplexity(
    DefinitionKey(name="logarithmic complexity", field=FieldName.MATHEMATICS),
    aliases=["logarithmic time", "O(log n)"],
)
