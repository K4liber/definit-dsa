from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.storage import STORAGE
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.real_world_performance import (
    REAL_WORLD_PERFORMANCE,
)
from definit_db.data.field.mathematics.definitions.computation.computation import COMPUTATION
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION
from definit_db.data.field.mathematics.definitions.fundamental.table import TABLE


class _Cache(Definition):
    def _get_content(self) -> str:
        return f"""
A high-speed {COMPUTER_MEMORY.key.get_reference()} {STORAGE.key.get_reference(phrase="storage")} layer that temporarily 
holds frequently accessed or recently used {DATA.key.get_reference()} to reduce access time and improve 
{REAL_WORLD_PERFORMANCE.key.get_reference(phrase="performance")}. 
When data is requested, the cache is checked first; if the data is found (a cache hit), it can be retrieved quickly 
without accessing slower storage. If not found (a cache miss), the data must be fetched from the original source 
and may be stored in the cache for future use.

---

A common {TABLE.key.get_reference(phrase="table")} of square roots can be kept in a cache so that a 
{INFORMATION.key.get_reference()} request for the
root of 2 is a hit on every call after the first. The first lookup computes the value and stores it (a miss); each
later lookup returns the cached value immediately instead of {COMPUTATION.key.get_reference(phrase="recomputing")} it.
"""


CACHE = _Cache(DefinitionKey(name="cache", field=FieldName.COMPUTER_SCIENCE))
