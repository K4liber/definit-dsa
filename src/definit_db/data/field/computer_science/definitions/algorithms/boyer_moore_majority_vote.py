from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.algorithms.in_place_algorithm import IN_PLACE_ALGORITHM
from definit_db.data.field.computer_science.definitions.fundamental.variable import VARIABLE
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.space_complexity import SPACE_COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.loop import LOOP
from definit_db.data.field.mathematics.definitions.fundamental.majority_element import MAJORITY_ELEMENT
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _BoyerMooreMajorityVote(Definition):
    def _get_content(self) -> str:
        return f"""
An {ALGORITHM.key.get_reference(phrase="algorithm")} that finds the {MAJORITY_ELEMENT.key.get_reference(phrase="majority element")} 
in a {SEQUENCE.key.get_reference(phrase="sequence")} using a single pass through the data. It is an 
{IN_PLACE_ALGORITHM.key.get_reference(phrase="in-place algorithm")} that maintains two 
{VARIABLE.key.get_reference(phrase="variables")}: a candidate element and a counter. The algorithm 
{LOOP.key.get_reference(phrase="iterates")} through the sequence; when the counter is zero it sets the current 
element as the candidate, then increments the counter if the current element matches the candidate or decrements it 
otherwise. It has a {TIME_COMPLEXITY.key.get_reference(phrase="time complexity")} of 
{BIG_O_NOTATION.key.get_reference(phrase="O(n)")} and a {SPACE_COMPLEXITY.key.get_reference(phrase="space complexity")} 
of {BIG_O_NOTATION.key.get_reference(phrase="O(1)")}.
"""


BOYER_MOORE_MAJORITY_VOTE = _BoyerMooreMajorityVote(
    key=DefinitionKey(
        name="Boyer-Moore majority vote algorithm",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
