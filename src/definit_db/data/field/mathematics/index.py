from definit.definition.definition import Definition

from definit_db.data.field.mathematics.definitions.algorithm.fundamental.algorithm import ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.amortized_time import AMORTIZED_TIME
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.asymptotic_efficiency import (
    ASYMPTOTIC_EFFICIENCY,
)
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.asymptotic_runtime import ASYMPTOTIC_RUNTIME
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.best_case import BEST_CASE
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.best_conceivable_runtime import (
    BEST_CONCEIVABLE_RUNTIME,
)
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.big_o_notation import BIG_O_NOTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.brute_force import BRUTE_FORCE
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.bud import BUD
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.co_np_class import CO_NP_CLASS
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.complexity import COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.divide_and_conquer import DIVIDE_AND_CONQUER
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.dynamic_programming import DYNAMIC_PROGRAMMING
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.efficiency import EFFICIENCY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.expected_case import EXPECTED_CASE
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.greedy_algorithm import GREEDY_ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.heuristic import HEURISTIC
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.logarithmic_complexity import (
    LOGARITHMIC_COMPLEXITY,
)
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.mathematical_programming import (
    MATHEMATICAL_PROGRAMMING,
)
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.memoization import MEMOIZATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.np_class import NP_CLASS
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.np_complete_class import NP_COMPLETE_CLASS
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.np_hard_class import NP_HARD_CLASS
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.objective_function import OBJECTIVE_FUNCTION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.off_by_one import OFF_BY_ONE
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.optimization import OPTIMIZATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.p_class import P_CLASS
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.precomputation import PRECOMPUTATION
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.real_life_efficiency import (
    REAL_LIFE_EFFICIENCY,
)
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.real_world_performance import (
    REAL_WORLD_PERFORMANCE,
)
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.space_complexity import SPACE_COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_complexity import TIME_COMPLEXITY
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.time_vs_space_tradeoff import (
    TIME_VS_SPACE_TRADE_OFF,
)
from definit_db.data.field.mathematics.definitions.algorithm.fundamental.worst_case import WORST_CASE
from definit_db.data.field.mathematics.definitions.algorithm.graph.a_star_algorithm import A_STAR_ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.graph.bellman_ford_algorithm import BELLMAN_FORD_ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.graph.cycle_detection import CYCLE_DETECTION
from definit_db.data.field.mathematics.definitions.algorithm.graph.dijkstras_algorithm import DIJKSTRAS_ALGORITHM
from definit_db.data.field.mathematics.definitions.algorithm.graph.floyd_warshall_algorithm import (
    FLOYD_WARSHALL_ALGORITHM,
)
from definit_db.data.field.mathematics.definitions.algorithm.searching.bidirectional_search import BIDIRECTIONAL_SEARCH
from definit_db.data.field.mathematics.definitions.algorithm.searching.binary_search import BINARY_SEARCH
from definit_db.data.field.mathematics.definitions.algorithm.searching.breadth_first_search import BREADTH_FIRST_SEARCH
from definit_db.data.field.mathematics.definitions.algorithm.searching.depth_first_search import DEPTH_FIRST_SEARCH
from definit_db.data.field.mathematics.definitions.algorithm.sorting.bubble_sort import BUBBLE_SORT
from definit_db.data.field.mathematics.definitions.algorithm.sorting.bucket_sort import BUCKET_SORT
from definit_db.data.field.mathematics.definitions.algorithm.sorting.heap_sort import HEAP_SORT
from definit_db.data.field.mathematics.definitions.algorithm.sorting.merge_sort import MERGE_SORT
from definit_db.data.field.mathematics.definitions.algorithm.sorting.quick_sort import QUICK_SORT
from definit_db.data.field.mathematics.definitions.algorithm.sorting.radix_sort import RADIX_SORT
from definit_db.data.field.mathematics.definitions.algorithm.sorting.selection_sort import SELECTION_SORT
from definit_db.data.field.mathematics.definitions.algorithm.sorting.sorting import SORTING
from definit_db.data.field.mathematics.definitions.algorithm.sorting.topological_sort import TOPOLOGICAL_SORT
from definit_db.data.field.mathematics.definitions.algorithm.strategy.bottom_up_approach import BOTTOM_UP_APPROACH
from definit_db.data.field.mathematics.definitions.algorithm.strategy.half_and_half_approach import (
    HALF_AND_HALF_APPROACH,
)
from definit_db.data.field.mathematics.definitions.algorithm.strategy.top_down_approach import TOP_DOWN_APPROACH
from definit_db.data.field.mathematics.definitions.analysis.asymptotic_behavior import ASYMPTOTIC_BEHAVIOR
from definit_db.data.field.mathematics.definitions.analysis.bound import BOUND
from definit_db.data.field.mathematics.definitions.analysis.upper_bound import UPPER_BOUND
from definit_db.data.field.mathematics.definitions.computation.deterministic_turing_machine import (
    DETERMINISTIC_TURING_MACHINE,
)
from definit_db.data.field.mathematics.definitions.computation.nondeterministic_turing_machine import (
    NONDETERMINISTIC_TURING_MACHINE,
)
from definit_db.data.field.mathematics.definitions.computation.turing_machine import TURING_MACHINE
from definit_db.data.field.mathematics.definitions.fundamental.binomial_coefficient import BINOMIAL_COEFFICIENT
from definit_db.data.field.mathematics.definitions.fundamental.boolean_expression import BOOLEAN_EXPRESSION
from definit_db.data.field.mathematics.definitions.fundamental.combination import COMBINATION
from definit_db.data.field.mathematics.definitions.fundamental.combinatorics import COMBINATORICS
from definit_db.data.field.mathematics.definitions.fundamental.distribution import DISTRIBUTION
from definit_db.data.field.mathematics.definitions.fundamental.expected_value import EXPECTED_VALUE
from definit_db.data.field.mathematics.definitions.fundamental.factorial import FACTORIAL
from definit_db.data.field.mathematics.definitions.fundamental.fibonacci import FIBONACCI
from definit_db.data.field.mathematics.definitions.fundamental.finite_sequence import FINITE_SEQUENCE
from definit_db.data.field.mathematics.definitions.fundamental.finite_set import FINITE_SET
from definit_db.data.field.mathematics.definitions.fundamental.function import FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.hash_function import HASH_FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.index import INDEX
from definit_db.data.field.mathematics.definitions.fundamental.information import INFORMATION
from definit_db.data.field.mathematics.definitions.fundamental.input_data import INPUT_DATA
from definit_db.data.field.mathematics.definitions.fundamental.instruction import INSTRUCTION
from definit_db.data.field.mathematics.definitions.fundamental.integer import INTEGER
from definit_db.data.field.mathematics.definitions.fundamental.intersection import INTERSECTION
from definit_db.data.field.mathematics.definitions.fundamental.item import ITEM
from definit_db.data.field.mathematics.definitions.fundamental.last_in_first_out import LAST_IN_FIRST_OUT
from definit_db.data.field.mathematics.definitions.fundamental.logical_operator import LOGICAL_OPERATOR
from definit_db.data.field.mathematics.definitions.fundamental.loop import LOOP
from definit_db.data.field.mathematics.definitions.fundamental.matrix import MATRIX
from definit_db.data.field.mathematics.definitions.fundamental.merge import MERGE
from definit_db.data.field.mathematics.definitions.fundamental.multiset import MULTISET
from definit_db.data.field.mathematics.definitions.fundamental.natural_number import NATURAL_NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.number import NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.numeral_system import NUMERAL_SYSTEM
from definit_db.data.field.mathematics.definitions.fundamental.object import OBJECT
from definit_db.data.field.mathematics.definitions.fundamental.operation import OPERATION
from definit_db.data.field.mathematics.definitions.fundamental.or_operator import OR_OPERATOR
from definit_db.data.field.mathematics.definitions.fundamental.perfect_square import PERFECT_SQUARE
from definit_db.data.field.mathematics.definitions.fundamental.permutation import PERMUTATION
from definit_db.data.field.mathematics.definitions.fundamental.polynomial import POLYNOMIAL
from definit_db.data.field.mathematics.definitions.fundamental.prime_factorization import PRIME_FACTORIZATION
from definit_db.data.field.mathematics.definitions.fundamental.prime_number import PRIME_NUMBER
from definit_db.data.field.mathematics.definitions.fundamental.probability import PROBABILITY
from definit_db.data.field.mathematics.definitions.fundamental.product import PRODUCT
from definit_db.data.field.mathematics.definitions.fundamental.pure_function import PURE_FUNCTION
from definit_db.data.field.mathematics.definitions.fundamental.radix import RADIX
from definit_db.data.field.mathematics.definitions.fundamental.relation import RELATION
from definit_db.data.field.mathematics.definitions.fundamental.reordering import REORDERING
from definit_db.data.field.mathematics.definitions.fundamental.sequence import SEQUENCE
from definit_db.data.field.mathematics.definitions.fundamental.set import SET
from definit_db.data.field.mathematics.definitions.fundamental.square_root import SQUARE_ROOT
from definit_db.data.field.mathematics.definitions.fundamental.uniform_distribution import UNIFORM_DISTRIBUTION
from definit_db.data.field.mathematics.definitions.fundamental.union import UNION
from definit_db.data.field.mathematics.definitions.fundamental.uniqueness import UNIQUENESS
from definit_db.data.field.mathematics.definitions.fundamental.vector import VECTOR
from definit_db.data.field.mathematics.definitions.fundamental.xor import XOR
from definit_db.data.field.mathematics.definitions.graph.acyclic_graph import ACYCLIC_GRAPH
from definit_db.data.field.mathematics.definitions.graph.adjacency_list import ADJACENCY_LIST
from definit_db.data.field.mathematics.definitions.graph.adjacency_matrix import ADJACENCY_MATRIX
from definit_db.data.field.mathematics.definitions.graph.bipartite_graph import BIPARTITE_GRAPH
from definit_db.data.field.mathematics.definitions.graph.connected_graph import CONNECTED_GRAPH
from definit_db.data.field.mathematics.definitions.graph.cycle import CYCLE
from definit_db.data.field.mathematics.definitions.graph.directed_acyclic_graph import DIRECTED_ACYCLIC_GRAPH
from definit_db.data.field.mathematics.definitions.graph.directed_graph import DIRECTED_GRAPH
from definit_db.data.field.mathematics.definitions.graph.edge import EDGE
from definit_db.data.field.mathematics.definitions.graph.graph import GRAPH
from definit_db.data.field.mathematics.definitions.graph.graph_distance import GRAPH_DISTANCE
from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.data.field.mathematics.definitions.graph.path import PATH
from definit_db.data.field.mathematics.definitions.graph.subgraph import SUBGRAPH
from definit_db.data.field.mathematics.definitions.graph.weighted_graph import WEIGHTED_GRAPH
from definit_db.data.field.mathematics.definitions.notations.label import LABEL
from definit_db.data.field.mathematics.definitions.problem.base_case import BASE_CASE
from definit_db.data.field.mathematics.definitions.problem.complement_problem import COMPLEMENT_PROBLEM
from definit_db.data.field.mathematics.definitions.problem.constraint import CONSTRAINT
from definit_db.data.field.mathematics.definitions.problem.criterion import CRITERION
from definit_db.data.field.mathematics.definitions.problem.feasible_solution import FEASIBLE_SOLUTION
from definit_db.data.field.mathematics.definitions.problem.mathematical_induction import MATHEMATICAL_INDUCTION
from definit_db.data.field.mathematics.definitions.problem.optimal_solution import OPTIMAL_SOLUTION
from definit_db.data.field.mathematics.definitions.problem.optimal_substructure import OPTIMAL_SUBSTRUCTURE
from definit_db.data.field.mathematics.definitions.problem.overlapping_subproblems import OVERLAPPING_SUBPROBLEMS
from definit_db.data.field.mathematics.definitions.problem.problem import PROBLEM
from definit_db.data.field.mathematics.definitions.problem.problem_space import PROBLEM_SPACE
from definit_db.data.field.mathematics.definitions.problem.recursion import RECURSION
from definit_db.data.field.mathematics.definitions.problem.reduction import REDUCTION
from definit_db.data.field.mathematics.definitions.problem.solution import SOLUTION
from definit_db.data.field.mathematics.definitions.problem.subproblem import SUBPROBLEM
from definit_db.data.field.mathematics.definitions.tree.avl_tree import AVL_TREE
from definit_db.data.field.mathematics.definitions.tree.b_tree import B_TREE
from definit_db.data.field.mathematics.definitions.tree.balanced_binary_tree import BALANCED_BINARY_TREE
from definit_db.data.field.mathematics.definitions.tree.binary_heap import BINARY_HEAP
from definit_db.data.field.mathematics.definitions.tree.binary_search_tree import BINARY_SEARCH_TREE
from definit_db.data.field.mathematics.definitions.tree.binary_tree import BINARY_TREE
from definit_db.data.field.mathematics.definitions.tree.binary_tree_traversal import BINARY_TREE_TRAVERSAL
from definit_db.data.field.mathematics.definitions.tree.complete_binary_tree import COMPLETE_BINARY_TREE
from definit_db.data.field.mathematics.definitions.tree.full_binary_tree import FULL_BINARY_TREE
from definit_db.data.field.mathematics.definitions.tree.heap_tree import HEAP_TREE
from definit_db.data.field.mathematics.definitions.tree.in_order_traversal import IN_ORDER_TRAVERSAL
from definit_db.data.field.mathematics.definitions.tree.interval_tree import INTERVAL_TREE
from definit_db.data.field.mathematics.definitions.tree.k_ary_tree import K_ARY_TREE
from definit_db.data.field.mathematics.definitions.tree.leaf import LEAF
from definit_db.data.field.mathematics.definitions.tree.max_heap import MAX_HEAP
from definit_db.data.field.mathematics.definitions.tree.min_heap import MIN_HEAP
from definit_db.data.field.mathematics.definitions.tree.minimum_spanning_tree import MINIMUM_SPANNING_TREE
from definit_db.data.field.mathematics.definitions.tree.n_ary_tree import N_ARY_TREE
from definit_db.data.field.mathematics.definitions.tree.perfect_binary_tree import PERFECT_BINARY_TREE
from definit_db.data.field.mathematics.definitions.tree.post_order_traversal import POST_ORDER_TRAVERSAL
from definit_db.data.field.mathematics.definitions.tree.pre_order_traversal import PRE_ORDER_TRAVERSAL
from definit_db.data.field.mathematics.definitions.tree.red_black_tree import RED_BLACK_TREE
from definit_db.data.field.mathematics.definitions.tree.root import ROOT
from definit_db.data.field.mathematics.definitions.tree.subtree import SUBTREE
from definit_db.data.field.mathematics.definitions.tree.tree import TREE
from definit_db.data.field.mathematics.definitions.tree.unbalanced_binary_tree import UNBALANCED_BINARY_TREE

field_index: list[Definition] = [
    OBJECT,
    ITEM,
    INFORMATION,
    BOOLEAN_EXPRESSION,
    SEQUENCE,
    FINITE_SEQUENCE,
    FIBONACCI,
    VECTOR,
    MATRIX,
    INSTRUCTION,
    INDEX,
    LOOP,
    LAST_IN_FIRST_OUT,
    OPERATION,
    RELATION,
    SET,
    INTERSECTION,
    UNION,
    FINITE_SET,
    FUNCTION,
    HASH_FUNCTION,
    PURE_FUNCTION,
    POLYNOMIAL,
    MULTISET,
    LABEL,
    ASYMPTOTIC_BEHAVIOR,
    BOUND,
    UPPER_BOUND,
    BIG_O_NOTATION,
    ASYMPTOTIC_EFFICIENCY,
    TURING_MACHINE,
    DETERMINISTIC_TURING_MACHINE,
    NONDETERMINISTIC_TURING_MACHINE,
    PROBLEM,
    PROBLEM_SPACE,
    COMPLEMENT_PROBLEM,
    INPUT_DATA,
    CRITERION,
    OPTIMAL_SOLUTION,
    OPTIMAL_SUBSTRUCTURE,
    SOLUTION,
    SUBPROBLEM,
    OVERLAPPING_SUBPROBLEMS,
    ALGORITHM,
    HEURISTIC,
    COMPLEXITY,
    EFFICIENCY,
    AMORTIZED_TIME,
    ASYMPTOTIC_RUNTIME,
    TIME_COMPLEXITY,
    SPACE_COMPLEXITY,
    TIME_VS_SPACE_TRADE_OFF,
    LOGARITHMIC_COMPLEXITY,
    REAL_WORLD_PERFORMANCE,
    REAL_LIFE_EFFICIENCY,
    BEST_CONCEIVABLE_RUNTIME,
    BRUTE_FORCE,
    BUD,
    DYNAMIC_PROGRAMMING,
    MEMOIZATION,
    PRECOMPUTATION,
    CO_NP_CLASS,
    NP_CLASS,
    NP_COMPLETE_CLASS,
    NP_HARD_CLASS,
    OPTIMIZATION,
    P_CLASS,
    A_STAR_ALGORITHM,
    DIJKSTRAS_ALGORITHM,
    BELLMAN_FORD_ALGORITHM,
    FLOYD_WARSHALL_ALGORITHM,
    CYCLE_DETECTION,
    GRAPH,
    NODE,
    EDGE,
    ADJACENCY_LIST,
    ADJACENCY_MATRIX,
    ACYCLIC_GRAPH,
    BIPARTITE_GRAPH,
    CYCLE,
    DIRECTED_ACYCLIC_GRAPH,
    DIRECTED_GRAPH,
    GRAPH_DISTANCE,
    PATH,
    SUBGRAPH,
    CONNECTED_GRAPH,
    WEIGHTED_GRAPH,
    AVL_TREE,
    B_TREE,
    BALANCED_BINARY_TREE,
    FULL_BINARY_TREE,
    PERFECT_BINARY_TREE,
    BINARY_SEARCH_TREE,
    BINARY_TREE,
    BINARY_TREE_TRAVERSAL,
    IN_ORDER_TRAVERSAL,
    PRE_ORDER_TRAVERSAL,
    POST_ORDER_TRAVERSAL,
    COMPLETE_BINARY_TREE,
    BINARY_HEAP,
    MIN_HEAP,
    MAX_HEAP,
    INTERVAL_TREE,
    K_ARY_TREE,
    N_ARY_TREE,
    LEAF,
    ROOT,
    MINIMUM_SPANNING_TREE,
    RED_BLACK_TREE,
    SUBTREE,
    TREE,
    UNBALANCED_BINARY_TREE,
    HEAP_TREE,
    REDUCTION,
    BASE_CASE,
    MATHEMATICAL_INDUCTION,
    RECURSION,
    GREEDY_ALGORITHM,
    DIVIDE_AND_CONQUER,
    SORTING,
    QUICK_SORT,
    SELECTION_SORT,
    PROBABILITY,
    DISTRIBUTION,
    UNIFORM_DISTRIBUTION,
    MERGE,
    MERGE_SORT,
    BUCKET_SORT,
    NUMBER,
    SQUARE_ROOT,
    PERFECT_SQUARE,
    INTEGER,
    NATURAL_NUMBER,
    PRIME_NUMBER,
    PRIME_FACTORIZATION,
    FACTORIAL,
    COMBINATORICS,
    COMBINATION,
    BINOMIAL_COEFFICIENT,
    PRODUCT,
    REORDERING,
    UNIQUENESS,
    RADIX,
    NUMERAL_SYSTEM,
    RADIX_SORT,
    BUBBLE_SORT,
    HEAP_SORT,
    TOPOLOGICAL_SORT,
    BINARY_SEARCH,
    BIDIRECTIONAL_SEARCH,
    BREADTH_FIRST_SEARCH,
    DEPTH_FIRST_SEARCH,
    BOTTOM_UP_APPROACH,
    TOP_DOWN_APPROACH,
    HALF_AND_HALF_APPROACH,
    MATHEMATICAL_PROGRAMMING,
    CONSTRAINT,
    OBJECTIVE_FUNCTION,
    FEASIBLE_SOLUTION,
    OFF_BY_ONE,
    BEST_CASE,
    WORST_CASE,
    EXPECTED_CASE,
    EXPECTED_VALUE,
    PERMUTATION,
    LOGICAL_OPERATOR,
    OR_OPERATOR,
    XOR,
]
