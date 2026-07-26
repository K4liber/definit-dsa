from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.complexity import COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.np_class import NP_CLASS
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.p_class import P_CLASS
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
satisfied?" into classes such as {P_CLASS.key.get_reference(phrase="P")} 
(solvable {EFFICIENCY.key.get_reference(phrase="efficiently")}) and {NP_CLASS.key.get_reference(phrase="NP")} 
(verifiable efficiently). A central question is whether every problem whose 
answer can be checked quickly can also be solved quickly — the famous P vs NP question.
"""


COMPLEXITY_THEORY = _ComplexityTheory(
    key=DefinitionKey(
        name="complexity theory",
        field=FieldName.MATHEMATICS,
    )
)
