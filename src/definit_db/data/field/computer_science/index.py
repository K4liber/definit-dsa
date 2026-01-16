from definit.definition.definition import Definition

from definit_db.data.field.computer_science.definitions.algorithms.bit.bit_manipulation import BIT_MANIPULATION
from definit_db.data.field.computer_science.definitions.algorithms.problems.graph_labeling.graph_coloring import (
    GRAPH_COLORING,
)
from definit_db.data.field.computer_science.definitions.algorithms.problems.graph_labeling.graph_labeling import (
    GRAPH_LABELING,
)
from definit_db.data.field.computer_science.definitions.algorithms.problems.graph_labeling.vertex_coloring import (
    VERTEX_COLORING,
)
from definit_db.data.field.computer_science.definitions.algorithms.problems.hash.hash_collision import HASH_COLLISION
from definit_db.data.field.computer_science.definitions.algorithms.problems.hash.rolling_hash import ROLLING_HASH
from definit_db.data.field.computer_science.definitions.algorithms.searching.string.rabin_karp_algorithm import (
    RABIN_KARP_ALGORITHM,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.associative_array import (
    ASSOCIATIVE_ARRAY,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.bag import BAG
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.collection import (
    COLLECTION,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.hash_table import (
    HASH_TABLE,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.priority_queue import (
    PRIORITY_QUEUE,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.queue import QUEUE
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.set import SET
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.stack import STACK
from definit_db.data.field.computer_science.definitions.data_structure.collection.fundamental.trie import TRIE
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.array import ARRAY
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.linked_list import LINKED_LIST
from definit_db.data.field.computer_science.definitions.data_structure.collection.list.list import LIST
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.ascii import ASCII
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.character_encoding import (
    CHARACTER_ENCODING,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.extended_ascii import (
    EXTENDED_ASCII,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.regular_expression import (
    REGULAR_EXPRESSION,
)
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.string import STRING
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.substring import SUBSTRING
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.unicode import UNICODE
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.utf import UTF
from definit_db.data.field.computer_science.definitions.data_structure.collection.string.utf_8 import UTF_8
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.abstract_data_type import (
    ABSTRACT_DATA_TYPE,
)
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.bit_field import BIT_FIELD
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.map import MAP
from definit_db.data.field.computer_science.definitions.data_structure.fundamental.primitive_data_type import (
    PRIMITIVE_DATA_TYPE,
)
from definit_db.data.field.computer_science.definitions.data_structure.operation.string_concatenation import (
    STRING_CONCATENATION,
)
from definit_db.data.field.computer_science.definitions.data_structure.primitive.boolean import BOOLEAN
from definit_db.data.field.computer_science.definitions.data_structure.primitive.integer import INTEGER
from definit_db.data.field.computer_science.definitions.fundamental.arithmetic_right_shift import ARITHMETIC_RIGHT_SHIFT
from definit_db.data.field.computer_science.definitions.fundamental.assertion import ASSERTION
from definit_db.data.field.computer_science.definitions.fundamental.binary_fractions import BINARY_FRACTIONS
from definit_db.data.field.computer_science.definitions.fundamental.binary_representation import BINARY_REPRESENTATION
from definit_db.data.field.computer_science.definitions.fundamental.bit import BIT
from definit_db.data.field.computer_science.definitions.fundamental.bitwise_operation import BITWISE_OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.bottleneck import BOTTLENECK
from definit_db.data.field.computer_science.definitions.fundamental.branch import BRANCH
from definit_db.data.field.computer_science.definitions.fundamental.bug import BUG
from definit_db.data.field.computer_science.definitions.fundamental.cache import CACHE
from definit_db.data.field.computer_science.definitions.fundamental.call_stack import CALL_STACK
from definit_db.data.field.computer_science.definitions.fundamental.computer import COMPUTER
from definit_db.data.field.computer_science.definitions.fundamental.computer_memory import COMPUTER_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.conceptual_test import CONCEPTUAL_TEST
from definit_db.data.field.computer_science.definitions.fundamental.concurrency import CONCURRENCY
from definit_db.data.field.computer_science.definitions.fundamental.core import CORE
from definit_db.data.field.computer_science.definitions.fundamental.data import DATA
from definit_db.data.field.computer_science.definitions.fundamental.data_structure import DATA_STRUCTURE
from definit_db.data.field.computer_science.definitions.fundamental.data_type import DATA_TYPE
from definit_db.data.field.computer_science.definitions.fundamental.dataset import DATASET
from definit_db.data.field.computer_science.definitions.fundamental.edge_case import EDGE_CASE
from definit_db.data.field.computer_science.definitions.fundamental.hardware import HARDWARE
from definit_db.data.field.computer_science.definitions.fundamental.heap_memory import HEAP_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.heap_overflow import HEAP_OVERFLOW
from definit_db.data.field.computer_science.definitions.fundamental.hexadecimal_code import HEXADECIMAL_CODE
from definit_db.data.field.computer_science.definitions.fundamental.logical_right_shift import LOGICAL_RIGHT_SHIFT
from definit_db.data.field.computer_science.definitions.fundamental.memory_allocation import MEMORY_ALLOCATION
from definit_db.data.field.computer_science.definitions.fundamental.memory_management import MEMORY_MANAGEMENT
from definit_db.data.field.computer_science.definitions.fundamental.object import OBJECT
from definit_db.data.field.computer_science.definitions.fundamental.operation import OPERATION
from definit_db.data.field.computer_science.definitions.fundamental.over_optimization import OVER_OPTIMIZATION
from definit_db.data.field.computer_science.definitions.fundamental.parallelism import PARALLELISM
from definit_db.data.field.computer_science.definitions.fundamental.pointer import POINTER
from definit_db.data.field.computer_science.definitions.fundamental.processor import PROCESSOR
from definit_db.data.field.computer_science.definitions.fundamental.program import PROGRAM
from definit_db.data.field.computer_science.definitions.fundamental.pseudocode import PSEUDOCODE
from definit_db.data.field.computer_science.definitions.fundamental.random_access_memory import RANDOM_ACCESS_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.reverse_engineering import REVERSE_ENGINEERING
from definit_db.data.field.computer_science.definitions.fundamental.right_shift import RIGHT_SHIFT
from definit_db.data.field.computer_science.definitions.fundamental.special_case import SPECIAL_CASE
from definit_db.data.field.computer_science.definitions.fundamental.stack_memory import STACK_MEMORY
from definit_db.data.field.computer_science.definitions.fundamental.stack_overflow import STACK_OVERFLOW
from definit_db.data.field.computer_science.definitions.fundamental.test import TEST
from definit_db.data.field.computer_science.definitions.fundamental.test_case import TEST_CASE
from definit_db.data.field.computer_science.definitions.fundamental.twos_complement import TWOS_COMPLEMENT
from definit_db.data.field.computer_science.definitions.fundamental.variable import VARIABLE

field_index: list[Definition] = [
    OBJECT,
    DATA,
    DATASET,
    DATA_STRUCTURE,
    DATA_TYPE,
    OPERATION,
    BIT,
    BINARY_REPRESENTATION,
    HEXADECIMAL_CODE,
    BINARY_FRACTIONS,
    BITWISE_OPERATION,
    BOTTLENECK,
    BUG,
    ARITHMETIC_RIGHT_SHIFT,
    HARDWARE,
    COMPUTER,
    COMPUTER_MEMORY,
    POINTER,
    CONCURRENCY,
    CORE,
    PARALLELISM,
    PROCESSOR,
    PROGRAM,
    OVER_OPTIMIZATION,
    PSEUDOCODE,
    BRANCH,
    RANDOM_ACCESS_MEMORY,
    RIGHT_SHIFT,
    REVERSE_ENGINEERING,
    HEAP_MEMORY,
    HEAP_OVERFLOW,
    LOGICAL_RIGHT_SHIFT,
    STACK_MEMORY,
    CALL_STACK,
    CACHE,
    STACK_OVERFLOW,
    ASSERTION,
    TEST,
    CONCEPTUAL_TEST,
    TEST_CASE,
    EDGE_CASE,
    SPECIAL_CASE,
    MEMORY_ALLOCATION,
    MEMORY_MANAGEMENT,
    VARIABLE,
    TWOS_COMPLEMENT,
    ABSTRACT_DATA_TYPE,
    BIT_FIELD,
    COLLECTION,
    MAP,
    PRIMITIVE_DATA_TYPE,
    ASSOCIATIVE_ARRAY,
    HASH_TABLE,
    BAG,
    SET,
    ARRAY,
    LINKED_LIST,
    LIST,
    PRIORITY_QUEUE,
    QUEUE,
    STACK,
    BOOLEAN,
    INTEGER,
    CHARACTER_ENCODING,
    ASCII,
    EXTENDED_ASCII,
    UTF,
    UTF_8,
    UNICODE,
    REGULAR_EXPRESSION,
    STRING,
    STRING_CONCATENATION,
    SUBSTRING,
    TRIE,
    GRAPH_LABELING,
    GRAPH_COLORING,
    VERTEX_COLORING,
    HASH_COLLISION,
    ROLLING_HASH,
    RABIN_KARP_ALGORITHM,
    BIT_MANIPULATION,
]
