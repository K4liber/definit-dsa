from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.subarray import SUBARRAY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.dynamic_programming import DYNAMIC_PROGRAMMING
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.optimization import OPTIMIZATION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _KadanesAlgorithm(Definition):
    def _get_content(self) -> str:
        return f"""
Kadane's algorithm is an {ALGORITHM.key.get_reference(phrase="algorithm")} for finding a contiguous 
{SUBARRAY.key.get_reference(phrase="subarray")} with maximum sum in a numeric 
{SEQUENCE.key.get_reference(phrase="sequence")}. It uses a {DYNAMIC_PROGRAMMING.key.get_reference(phrase="dynamic programming")} 
recurrence that tracks the best subarray ending at the current position and the best subarray seen so far, producing 
an {OPTIMIZATION.key.get_reference(phrase="optimized")} linear-time solution to the maximum subarray problem.
"""


KADANES_ALGORITHM = _KadanesAlgorithm(
    key=DefinitionKey(
        name="Kadane's algorithm",
        field=FieldName.COMPUTER_SCIENCE,
    )
)