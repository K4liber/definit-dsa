from definit.definition.definition import Definition
from definit.definition.definition_key import DefinitionKey

from definit_db.data.field import FieldName
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.map import MAP
from definit_db.data.field.computer_science.definitions.fundamental.dataset import DATASET
from definit_db.data.field.computer_science.definitions.fundamental.parallelism import PARALLELISM
from definit_db.data.field.computer_science.definitions.fundamental.programming_model import PROGRAMMING_MODEL
from definit_db.data.field.computer_science.definitions.fundamental.worker import WORKER


class _MapReduce(Definition):
    def _get_content(self) -> str:
        return f"""
A {PROGRAMMING_MODEL.key.get_reference(phrase="programming model")} for processing large 
{DATASET.key.get_reference(phrase="datasets")} by splitting work into two phases:

- map: transform input records into intermediate key/value pairs (conceptually a {MAP.key.get_reference(phrase="map")}).
- reduce: aggregate the intermediate values for each key.

MapReduce enables {PARALLELISM.key.get_reference()} by distributing the map and reduce work across many
{WORKER.key.get_reference(phrase="workers")}.

---

To count how often each word appears in a large {DATASET.key.get_reference(phrase="dataset")} of documents, the
{DATASET.key.get_reference(phrase="dataset")} is first split into chunks, and each chunk is assigned to a different
{WORKER.key.get_reference(phrase="worker")}. During the map phase, each worker reads the words in its chunk and
turns every word into a (word, 1) pair. All intermediate pairs are then grouped by word, so every pair that shares
the same word lands together regardless of which worker produced it. During the reduce phase, workers are each
assigned a group of words; each reduce worker adds the counts for its words, producing a single (word, total) result
per word. Because the map and reduce work is spread across many workers at once, the counting is done in
{PARALLELISM.key.get_reference(phrase="parallel")} and finishes much faster than reading the documents one by one.
"""


MAPREDUCE = _MapReduce(
    key=DefinitionKey(
        name="MapReduce",
        field=FieldName.COMPUTER_SCIENCE,
    )
)
