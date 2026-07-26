from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.complexity import COMPLEXITY
from definit_db.data.field.mathematics.definitions.analysis.asymptotic_behavior import ASYMPTOTIC_BEHAVIOR
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM


class _Performance(Definition):
    def _get_content(self) -> str:
        return f"""
How well an {ALGORITHM.key.get_reference()} uses resources (such as time and space) to produce its result.
Performance is gauged by the {COMPLEXITY.key.get_reference()} of the resource usage, either theoretically (as
{ASYMPTOTIC_BEHAVIOR.key.get_reference(phrase="asymptotic growth")}) or empirically (as observed behavior on actual
{INPUT_DATA.key.get_reference(phrase="data")}).

---

Two {ALGORITHM.key.get_reference(phrase="algorithms")} may both solve the same {PROBLEM.key.get_reference()}, 
yet one inspects every {ITEM.key.get_reference(phrase="element")} while the other skips ahead by halves; 
the second has better performance because its resource usage grows more slowly as the input grows.
"""


PERFORMANCE = _Performance(
    key=DefinitionKey(
        name="performance",
        field=FieldName.MATHEMATICS,
    )
)
