import pytest
from definit.db.md import DatabaseMd
from definit.definition.definition import Definition

from definit_db.serialize import serialize


@pytest.mark.skip(reason="Manual test: generates and displays the definition levels histogram.")
def test_generate_definition_levels_histogram() -> None:
    # Manual test: creates definition_levels_histogram.png and opens the plot window.
    db_path = serialize()
    db_md = DatabaseMd(data_md_path=db_path, load_cache=True)
    index = db_md.get_index()
    dag = db_md.get_dag(definition_keys=index)
    definition_levels = dag.get_definition_levels()

    level_to_definitions: dict[int, list[Definition]] = {}

    for definition, level in definition_levels:
        level_to_definitions.setdefault(level, []).append(definition)

    level_to_number_of_definitions = {level: len(definitions) for level, definitions in level_to_definitions.items()}

    import matplotlib.pyplot as plt  # noqa: PLC0415

    plt.bar(level_to_number_of_definitions.keys(), level_to_number_of_definitions.values())
    plt.xlabel("Level")
    plt.ylabel("Number of Definitions")
    plt.title("Number of Definitions per Level")
    plt.show()
    plt.savefig("definition_levels_histogram.png")
