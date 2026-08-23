from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.sorting.quick_sort import QUICK_SORT
from definit_db.data.field.mathematics.definitions.fundamental.distribution import DISTRIBUTION
from definit_db.data.field.mathematics.definitions.fundamental.expected_value import EXPECTED_VALUE
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA


class _ExpectedCase(Definition):
    def _get_content(self) -> str:
        return f"""
The {EXPECTED_VALUE.key.get_reference("expected value")} of the
{TIME_COMPLEXITY.key.get_reference("time complexity")} of an {ALGORITHM.key.get_reference()} over a
{DISTRIBUTION.key.get_reference("probability distribution")} of {INPUT_DATA.key.get_reference("inputs")}.

It describes the algorithm's typical runtime under the assumed input distribution.

---

{QUICK_SORT.key.get_reference("QuickSort's")} expected case runtime is "O(n log n)" 
when the pivot splits the {INPUT_DATA.key.get_reference("input")} roughly in half on average across random 
inputs, even though a poor pivot choice on some inputs can degrade its {TIME_COMPLEXITY.key.get_reference()} to 
"O(n²)".
"""


EXPECTED_CASE = _ExpectedCase(
    key=DefinitionKey(
        name="expected case",
        field=FieldName.MATHEMATICS,
    ),
    aliases=("average case",),
)
