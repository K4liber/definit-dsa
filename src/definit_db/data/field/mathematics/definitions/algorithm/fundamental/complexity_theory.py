from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.complexity import COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.fundamental.relation import RELATION
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM


class _ComplexityTheory(Definition):
    def _get_content(self) -> str:
        return f"""
The branch of study that analyzes the resources (such as time and space) required to 
solve {PROBLEM.key.get_reference(phrase="problems")} by {COMPLEXITY.key.get_reference(phrase="complexity")} classes.
It groups problems by their intrinsic difficulty and studies {RELATION.key.get_reference(phrase="relationships")} 
between those classes, such as which problems are tractable, which are equivalent in hardness, 
and which are harder than others.

---

Complexity theory classifies {PROBLEM.key.get_reference(phrase="problems")} like "can this Boolean formula be
satisfied?" according to whether they can be solved {EFFICIENCY.key.get_reference(phrase="efficiently")},
whether proposed answers can be checked efficiently, and how those classes are connected by
{RELATION.key.get_reference(phrase="relationships")} of difficulty. A central question in the area is whether
every problem whose answer can be checked quickly can also be solved quickly.
"""


COMPLEXITY_THEORY = _ComplexityTheory(
    key=DefinitionKey(
        name="complexity theory",
        field=FieldName.MATHEMATICS,
    )
)
