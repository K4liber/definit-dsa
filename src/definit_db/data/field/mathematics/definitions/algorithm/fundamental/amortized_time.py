from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.fundamental.bound import BOUND
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE


class _AmortizedTime(Definition):
    def __init__(self, key: DefinitionKey) -> None:
        super().__init__(key)

    def _get_content(self) -> str:
        return f"""
{self.key.get_reference()} is a method of analyzing the {TIME_COMPLEXITY.key.get_reference("time complexity")} 
of a {SEQUENCE.key.get_reference()} of {OPERATION.key.get_reference("operations")} by calculating the average 
cost per {OPERATION.key.get_reference()} over the entire sequence, rather than analyzing individual operations 
in isolation. This approach is particularly useful for {ALGORITHM.key.get_reference("algorithms")} 
where some operations are expensive but occur infrequently, while most operations are cheap. Amortized analysis 
guarantees that the average cost per operation over any sequence remains {BOUND.key.get_reference("bounded")}, 
even though individual operations may occasionally be costly.
"""


AMORTIZED_TIME = _AmortizedTime(DefinitionKey(name="amortized time", field=FieldName.MATHEMATICS))
