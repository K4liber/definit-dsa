import importlib
import os
from pathlib import Path

from definit.db.md import DatabaseMd
from definit.definition.definition import Definition
from definit.definition.definition import DefinitionKey
from definit.definition.field import Field

from definit_db.data.field import FieldName

_FIELDS = [FieldName.MATHEMATICS, FieldName.COMPUTER_SCIENCE]
_DEFINIT_DB_PACKAGE_ROOT = Path(os.path.dirname(__file__))
_PATH_DATA_MD = _DEFINIT_DB_PACKAGE_ROOT / "data_md"
_MODULE_FIELD = "definit_db.data.field"


def get_field_index(field: Field) -> list[Definition]:
    module = importlib.import_module(f"{_MODULE_FIELD}.{field}.index")
    return getattr(module, "field_index")


def _verify_definitions_subpackage(subpackage_dir: Path) -> None:
    init_file = subpackage_dir / "__init__.py"

    if not init_file.exists():
        raise FileNotFoundError(f"Package is missing __init__.py: {init_file}")

    for item in subpackage_dir.iterdir():
        if item.name in {"__pycache__"}:
            continue
        if item.is_dir():
            _verify_definitions_subpackage(subpackage_dir=item)
        elif item.suffix == ".py":
            continue
        else:
            raise ValueError(f"Invalid file in definitions package: {item}")


def verify_definitions_package(definitions_path: Path) -> None:
    """Verify the structure of a definitions package.

    It checks if the directory is a correct definitions package.
    Each subdirectory of a definitions package should have only python modules or sub-packages.
    If subdirectory contains both, it raises an error.
    """
    if not definitions_path.exists():
        raise FileNotFoundError(f"Package path does not exist: {definitions_path}")

    if not definitions_path.is_dir():
        raise NotADirectoryError(f"Package path is not a directory: {definitions_path}")

    _verify_definitions_subpackage(subpackage_dir=definitions_path)


def serialize() -> Path:
    # Write Markdown files for each definition in the specified fields
    all_definitions: list[Definition] = []

    for field in _FIELDS:
        field_index = get_field_index(field=field)

        for definition in field_index:
            # Extract sub_categories from module path
            sub_categories = tuple(
                definition.__module__.removeprefix("src.")
                .removeprefix(_MODULE_FIELD)
                .removeprefix(f".{field}.definitions.")
                .split(".")
            )[:-1]  # Exclude the last part which is the definition module itself
            fixed_definition = Definition(
                key=DefinitionKey(name=definition.key.name, field=definition.key.field, sub_categories=sub_categories),
                content=definition.content,
            )
            all_definitions.append(fixed_definition)

    DatabaseMd.serialize(
        definitions=all_definitions,
        db_path=_PATH_DATA_MD,
    )
    return _PATH_DATA_MD


if __name__ == "__main__":
    serialize()
