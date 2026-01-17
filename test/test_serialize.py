from pathlib import Path

import pytest
from definit.db.md import DatabaseMd

from definit_db.data.field import FieldName
from definit_db.serialize import _FIELDS
from definit_db.serialize import serialize
from definit_db.serialize import verify_definitions_package


def test_generate_and_load() -> None:
    # Given, When
    db_path = serialize()
    db = DatabaseMd(data_md_path=db_path, load_cache=True)
    index = db.get_index()
    # Then
    assert len(index) == 275


@pytest.mark.parametrize("field", _FIELDS)
def test_verify_definitions_package(repo_root_dir: Path, field: FieldName) -> None:
    # Given
    definitions_path = repo_root_dir / "src" / "definit_db" / "data" / "field" / field / "definitions"
    # When
    verify_definitions_package(definitions_path=definitions_path)
    # Then
    assert True
