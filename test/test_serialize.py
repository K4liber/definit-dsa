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
        0: 6,
        1: 13,
        2: 36,
        3: 35,
        4: 33,
        5: 35,
        6: 45,
        7: 41,
        8: 19,
        9: 16,
        10: 7,
        11: 3,
        12: 6,
        13: 7,
        14: 2,
    }
    assert len(index) == 304
    assert level_to_number_of_definitions == expected_level_to_number_of_definitions
    # Plot a histogram of the number of definitions per level
    # TODO(K4liber): it should not be here -> move it to a separate script?
    return
    import matplotlib.pyplot as plt  # noqa: PLC0415

    plt.bar(level_to_number_of_definitions.keys(), level_to_number_of_definitions.values())
    plt.xlabel("Level")
    plt.ylabel("Number of Definitions")
    plt.title("Number of Definitions per Level")
    plt.show()
    plt.savefig("number_of_definitions_per_level.png")


@pytest.mark.parametrize("field", _FIELDS)
def test_verify_definitions_package(repo_root_dir: Path, field: FieldName) -> None:
    # Given
    definitions_path = repo_root_dir / "src" / "definit_db" / "data" / "field" / field / "definitions"
    # When
    verify_definitions_package(definitions_path=definitions_path)
    # Then
    assert True
