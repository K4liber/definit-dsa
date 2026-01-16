import importlib
import pkgutil
from collections import deque

from definit.definition.definition import Definition

import definit_db
from definit_db.data.field import FieldName
from definit_db.data.field.index import get_index

_field_to_index_length = {
    FieldName.COMPUTER_SCIENCE: 81,
    FieldName.MATHEMATICS: 149,
}


def test_indexes_load_and_length() -> None:
    """By loading the index we check if there are no circular dependencies between definitions."""
    for field, index_length in _field_to_index_length.items():
        field_index = get_index(field)
        assert len(field_index) == index_length
        assert all(definition_key.field == field for definition_key in field_index), (
            f"All definitions in the index for {field} should have the correct field."
        )


def test_all_definitions_in_indexes() -> None:
    all_definitions_in_indexes: set[Definition] = set()

    for field in _field_to_index_length.keys():
        field_index = get_index(field)
        all_definitions_in_indexes.update({definition for definition in field_index.values()})

    all_definitions = _get_all_definitions()
    definitions_diff = all_definitions - all_definitions_in_indexes
    assert not definitions_diff, (
        f"The following definitions are missing in the indexes: "
        f"{', '.join(definition.key.name for definition in definitions_diff)}"
    )


def _get_all_definitions() -> set[Definition]:
    """Collect and return Definition subclasses recursively."""
    for _, name, _ in pkgutil.walk_packages(definit_db.__path__, definit_db.__name__ + "."):
        importlib.import_module(name)

    all_definitions: set[Definition] = set()
    q = deque([Definition])

    while q:
        cls = q.popleft()
        for definition_class in cls.__subclasses__():
            # search for all instances of the definition class
            definition_class_module_path = definition_class.__module__
            definition_class_module = __import__(definition_class_module_path, fromlist=[""])
            definitions = {
                definition_class_module.__dict__[name]
                for name in dir(definition_class_module)
                if isinstance(definition_class_module.__dict__[name], Definition)
                and definition_class_module.__dict__[name].__module__ == definition_class_module_path
            }
            assert len(definitions) == 1, (
                f"Expected exactly one instance of {definition_class.__name__}, found {len(definitions)}, "
                f"module: {definition_class_module_path}."
            )
            definition = definitions.pop()

            if definition not in all_definitions:
                all_definitions.add(definition)
                q.append(definition_class)

    return all_definitions
