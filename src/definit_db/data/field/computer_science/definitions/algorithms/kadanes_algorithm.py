from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.subarray import SUBARRAY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.dynamic_programming import DYNAMIC_PROGRAMMING
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.optimization import OPTIMIZATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.recurrence import RECURRENCE
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM


class _KadanesAlgorithm(Definition):
    def _get_content(self) -> str:
        return f"""
Kadane's algorithm is an {ALGORITHM.key.get_reference(phrase="algorithm")} for finding a contiguous 
{SUBARRAY.key.get_reference(phrase="subarray")} with maximum sum in a {NUMBER.key.get_reference(phrase="numeric")} 
{SEQUENCE.key.get_reference(phrase="sequence")}. It uses a 
{DYNAMIC_PROGRAMMING.key.get_reference(phrase="dynamic programming")} 
{RECURRENCE.key.get_reference(phrase="recurrence")} that tracks the best subarray ending 
at the current position and the best subarray seen so far, producing an 
{OPTIMIZATION.key.get_reference(phrase="optimized")} {TIME_COMPLEXITY.key.get_reference(phrase="linear-time")} 
({BIG_O_NOTATION.key.get_reference(phrase="O(n)")}) solution to the maximum subarray 
{PROBLEM.key.get_reference(phrase="problem")}.

---

For the {SEQUENCE.key.get_reference(phrase="sequence")} [-2, 1, -3, 4, -1, 2, 1, -5, 4], Kadane's algorithm walks 
left to right, at each step choosing between extending the current subarray or starting fresh. At each position it 
keeps the best sum ending there (`current = max(sum([subarray ending here]), element)`) and the best sum seen so far
(`best = max(best, current)`):


-2: current = max(sum([-2]), 0 + -2) = -2, best = sum([-2]) = -2 (initialize)


1: current = max(sum([1]), -2 + 1) = 1, best = max(sum([-2]), sum([1])) = 1 (start fresh)


-3: current = max(sum([-3]), 1 + -3) = -2, best = max(sum([1]), sum([-3])) = 1 (extend; best unchanged)


4: current = max(sum([4]), -2 + 4) = 4, best = max(sum([1]), sum([4])) = 4 (start fresh)


-1: current = max(sum([4, -1]), 4 + -1) = 3, best = max(sum([4]), sum([4, -1])) = 4 (extend; best unchanged)


2: current = max(sum([4, -1, 2]), 3 + 2) = 5, best = max(sum([4]), sum([4, -1, 2])) = 5 (extend)


1: current = max(sum([4, -1, 2, 1]), 5 + 1) = 6, best = max(sum([4, -1, 2]), sum([4, -1, 2, 1])) = 6 (extend)


-5: current = max(sum([4, -1, 2, 1, -5]), 6 + -5) = 1, best = max(sum([4, -1, 2, 1]), sum([4, -1, 2, 1, -5])) = 6 
(extend; best unchanged)


4: current = max(sum([4, -1, 2, 1, -5, 4]), 1 + 4) = 5, best = max(sum([4, -1, 2, 1]), sum([4, -1, 2, 1, -5, 4])) = 6 
(extend; best unchanged)


The best {SUBARRAY.key.get_reference(phrase="subarray")} ends where `best` reached 6, at the element `1`, tracing 
back to `[4, -1, 2, 1]` — whose sum is 6, larger than any other contiguous subarray in the sequence.
"""


KADANES_ALGORITHM = _KadanesAlgorithm(
    key=DefinitionKey(
        name="Kadane's algorithm",
        field=FieldName.COMPUTER_SCIENCE,
    ),
    aliases=["maximum subarray algorithm"],
)
