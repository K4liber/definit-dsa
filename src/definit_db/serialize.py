import importlib
import os
import re
from heapq import heappop
from heapq import heappush
from pathlib import Path

from definit.db.md import DatabaseMd
from definit.definition.definition import Definition
from definit.definition.definition import DefinitionKey
from definit.definition.field import Field

from definit_db.data.field import FieldName

_REFERENCE_PATTERN = re.compile(r"\[(?:.*?)\]\((.*?)\)")

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

    all_definitions = topological_sort(definitions=all_definitions)

    DatabaseMd.serialize(
        definitions=all_definitions,
        db_path=_PATH_DATA_MD,
    )
    return _PATH_DATA_MD


def topological_sort(definitions: list[Definition]) -> list[Definition]:
    """Topologically sort definitions so that every referenced (lower-level) definition comes first.

    A definition that references another definition depends on it, so the referenced definition
    must appear earlier in the list. Ties are broken by the original input order to keep the
    output stable. Uses Kahn's algorithm.
    """
    uid_to_definition: dict[str, Definition] = {definition.key.uid: definition for definition in definitions}
    original_order: dict[str, int] = {definition.key.uid: index for index, definition in enumerate(definitions)}

    # dependencies[uid] = set of uids this definition references (must come before it)
    dependencies: dict[str, set[str]] = {}
    # dependents[uid] = set of uids that reference this definition
    dependents: dict[str, set[str]] = {uid: set() for uid in uid_to_definition}

    for definition in definitions:
        uid = definition.key.uid
        referenced_uids = {
            referenced_uid
            for referenced_uid in _REFERENCE_PATTERN.findall(definition.content)
            if referenced_uid in uid_to_definition and referenced_uid != uid
        }
        dependencies[uid] = referenced_uids

        for referenced_uid in referenced_uids:
            dependents[referenced_uid].add(uid)

    in_degree: dict[str, int] = {uid: len(deps) for uid, deps in dependencies.items()}
    # Min-heap keyed by original position so ties keep the original (stable) order.
    ready: list[tuple[int, str]] = []
    for definition in definitions:
        uid = definition.key.uid
        if in_degree[uid] == 0:
            heappush(ready, (original_order[uid], uid))

    ordered: list[Definition] = []

    while ready:
        _, uid = heappop(ready)
        ordered.append(uid_to_definition[uid])

        for dependent_uid in dependents[uid]:
            in_degree[dependent_uid] -= 1
            if in_degree[dependent_uid] == 0:
                heappush(ready, (original_order[dependent_uid], dependent_uid))

    if len(ordered) != len(definitions):
        remaining = [definition.key.uid for definition in definitions if in_degree[definition.key.uid] > 0]
        raise ValueError(f"Cycle detected in definition references; cannot topologically sort: {remaining}")

    return ordered


if __name__ == "__main__":
    serialize()
