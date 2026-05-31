from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.algorithms.in_place_algorithm import IN_PLACE_ALGORITHM
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.array import ARRAY
from definit_db.data.field.computer_science.definitions.fundamental.pointer import POINTER
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.space_complexity import SPACE_COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX
from definit_db.data.field.mathematics.definitions.fundamental.loop import LOOP
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _TwoPointersTechnique(Definition):
    def _get_content(self) -> str:
        return f"""
A problem-solving {ALGORITHM.key.get_reference(phrase="algorithmic")} approach used on a 
{SEQUENCE.key.get_reference(phrase="sequence")} (typically an {ARRAY.key.get_reference(phrase="array")}) 
that maintains two {POINTER.key.get_reference(phrase="pointers")} (or 
{INDEX.key.get_reference(phrase="indices")}) which traverse the data simultaneously. The pointers 
commonly start at opposite ends and move toward each other, or move in the same direction at 
different speeds (a "fast" and "slow" pointer). Each iteration of the 
{LOOP.key.get_reference(phrase="loop")} advances one or both pointers based on a condition until they 
meet or the target configuration is found. It is an 
{IN_PLACE_ALGORITHM.key.get_reference(phrase="in-place algorithm")} that typically reduces a problem 
requiring nested iteration from a {TIME_COMPLEXITY.key.get_reference(phrase="time complexity")} of 
{BIG_O_NOTATION.key.get_reference(phrase="O(n^2)")} to {BIG_O_NOTATION.key.get_reference(phrase="O(n)")} 
while maintaining a {SPACE_COMPLEXITY.key.get_reference(phrase="space complexity")} of 
{BIG_O_NOTATION.key.get_reference(phrase="O(1)")}.
"""


TWO_POINTERS_TECHNIQUE = _TwoPointersTechnique(
    key=DefinitionKey(
        name="two pointers technique",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
