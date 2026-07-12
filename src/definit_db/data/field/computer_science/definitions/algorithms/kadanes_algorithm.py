from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.subarray import SUBARRAY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.dynamic_programming import DYNAMIC_PROGRAMMING
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.optimization import OPTIMIZATION
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _KadanesAlgorithm(Definition):
    def _get_content(self) -> str:
        return f"""
Kadane's algorithm is an {ALGORITHM.key.get_reference(phrase="algorithm")} for finding a contiguous 
{SUBARRAY.key.get_reference(phrase="subarray")} with maximum sum in a {NUMBER.key.get_reference(phrase="numeric")} 
{SEQUENCE.key.get_reference(phrase="sequence")}. It uses a 
{DYNAMIC_PROGRAMMING.key.get_reference(phrase="dynamic programming")} recurrence that tracks the best subarray ending 
at the current position and the best subarray seen so far, producing an 
{OPTIMIZATION.key.get_reference(phrase="optimized")} linear-time solution to the maximum subarray problem.

---

For the {SEQUENCE.key.get_reference(phrase="sequence")} `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`, Kadane's algorithm walks 
left to right, at each step choosing between extending the current subarray or starting fresh. At each position it 
keeps the best sum ending there (`current`) and the best sum seen so far (`best`):

  -2:  current = max(-2, 0 + -2) = -2,  best = -2   (start fresh)
   1:  current = max( 1, -2 +  1) =  1,  best =  1   (start fresh)
  -3:  current = max(-3,  1 + -3) = -2,  best =  1   (extend; best unchanged)
   4:  current = max( 4, -2 +  4) =  4,  best =  4   (start fresh)
  -1:  current = max(-1,  4 + -1) =  3,  best =  4   (extend)
   2:  current = max( 2,  3 +  2) =  5,  best =  5   (extend)
   1:  current = max( 1,  5 +  1) =  6,  best =  6   (extend)
  -5:  current = max(-5,  6 + -5) =  1,  best =  6   (extend; best unchanged)
   4:  current = max( 4,  1 +  4) =  5,  best =  6   (extend; best unchanged)

The best {SUBARRAY.key.get_reference(phrase="subarray")} ends where `best` reached 6, at the element `1`, tracing 
back to `[4, -1, 2, 1]` — whose sum is 6, larger than any other contiguous subarray in the sequence.
"""


KADANES_ALGORITHM = _KadanesAlgorithm(
    key=DefinitionKey(
        name="Kadane's algorithm",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
