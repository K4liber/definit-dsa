from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _MajorityElement(Definition):
    def _get_content(self) -> str:
        return f"""
An {ITEM.key.get_reference(phrase="element")} in a {SEQUENCE.key.get_reference(phrase="sequence")} that appears 
more than half the total number of times. Formally, given a sequence of n elements, a majority element is one that 
occurs more than n/2 times. A sequence may have at most one majority element.
"""


MAJORITY_ELEMENT = _MajorityElement(
    key=DefinitionKey(
        name="majority element",
        field=FieldName.MATHEMATICS,
    )
)
