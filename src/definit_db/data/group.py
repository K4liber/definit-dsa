from definit.definition.definition_group import DefinitionGroup

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science import computer_science_index
from definit_db.data.field.mathematics import mathematics_index

DATA_STRUCTURES_AND_ALGORITHMS = DefinitionGroup(
    name="Data Structures and Algorithms",
    definitions=[*mathematics_index, *computer_science_index],
)

_GROUPS = [DATA_STRUCTURES_AND_ALGORITHMS]

_FIELD_NAMES = [FieldName.MATHEMATICS, FieldName.COMPUTER_SCIENCE]
assert {field for field in _FIELD_NAMES} == {
    definition.key.field for definition in DATA_STRUCTURES_AND_ALGORITHMS.definitions
}


def get_groups() -> list[DefinitionGroup]:
    return _GROUPS
