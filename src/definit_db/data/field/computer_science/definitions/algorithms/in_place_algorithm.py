from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.auxiliary_space import AUXILIARY_SPACE
from definit_db.data.field.computer_science.definitions.fundamental.data_structure import DATA_STRUCTURE
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.space_complexity import SPACE_COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA


class _InPlaceAlgorithm(Definition):
    def _get_content(self) -> str:
        return f"""
An {ALGORITHM.key.get_reference(phrase="algorithm")} that transforms a {DATA_STRUCTURE.key.get_reference(phrase="data structure")} 
using only a constant amount of {AUXILIARY_SPACE.key.get_reference(phrase="auxiliary space")}, meaning it 
{OPERATION.key.get_reference(phrase="operates")} directly on the {INPUT_DATA.key.get_reference(phrase="input data")} rather than creating a separate copy. 
An in-place algorithm typically has a {SPACE_COMPLEXITY.key.get_reference(phrase="space complexity")} of {BIG_O_NOTATION.key.get_reference(phrase="O(1)")}, 
not counting the space used by the input itself.
"""


IN_PLACE_ALGORITHM = _InPlaceAlgorithm(
    key=DefinitionKey(
        name="in-place algorithm",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
