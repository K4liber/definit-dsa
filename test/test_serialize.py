from pathlib import Path

import pytest
from definit.db.md import DatabaseMd
from definit.definition.definition import Definition

from definit_db.data.field import FieldName
from definit_db.serialize import _FIELDS  # type: ignore
from definit_db.serialize import serialize
from definit_db.serialize import verify_definitions_package


def test_generate_and_load() -> None:
    # Given, When
    db_path = serialize()
    db_md = DatabaseMd(data_md_path=db_path, load_cache=True)
    index = db_md.get_index()
    dag = db_md.get_dag(definition_keys=index)
    definition_levels = dag.get_definition_levels()

    level_to_definitions: dict[int, list[Definition]] = {}

    for definition, level in definition_levels:
        level_to_definitions.setdefault(level, []).append(definition)

    level_to_number_of_definitions = {level: len(definitions) for level, definitions in level_to_definitions.items()}
    expected_level_to_number_of_definitions = {
        0: 5,
        1: 12,
        2: 30,
        3: 35,
        4: 39,
        5: 36,
        6: 30,
        7: 50,
        8: 29,
        9: 21,
        10: 11,
        11: 7,
        12: 6,
        13: 8,
        14: 2,
    }
    assert len(index) == 321
    assert level_to_number_of_definitions == expected_level_to_number_of_definitions


@pytest.mark.parametrize("field", _FIELDS)
def test_verify_definitions_package(repo_root_dir: Path, field: FieldName) -> None:
    # Given
    definitions_path = repo_root_dir / "src" / "definit_db" / "data" / "field" / field / "definitions"
    # When
    verify_definitions_package(definitions_path=definitions_path)
    # Then
    assert True
