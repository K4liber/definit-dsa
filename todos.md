# TODOs

## IN PROGRESS

### 4. Review all definitions

- [x] Create a `review_definition.md` instruction file for how to review a definition
- [ ] Check if they are accurate, complete and have all possible references to other definitions

## TODO

### 6. Fix slow `get_dag` in the `definit` library (upstream)

`DatabaseMd.get_dag` / `_update_dag_in_place` (in `definit/db/md.py`) is the root cause of the
slow `test_generate_and_load` test (minutes instead of seconds). It is not a cycle.

Two compounding flaws make the cost proportional to the number of directed walks counted with
link multiplicity, instead of `O(V + E)`:

- It keeps **no visited set**, so a shared subtree is re-expanded every time it is reached.
- It iterates **every regex link match, including duplicate links** in the same definition, and
  recurses per occurrence. Duplicate references (e.g. examples re-linking `tree`/`node`/`leaf`)
  add no new edge but multiply the work up the dependency chain.

Measured impact: walk count grew from ~35.5k (unique edges) to ~2.56M with duplicate links
(72x), driven entirely by the example sections.

Proper fix (in the `definit` library):

- [ ] Add a `visited: set[DefinitionKey]` guard to `_update_dag_in_place` so each subtree is
      expanded once, and/or deduplicate the child links before recursing.
- [ ] Optionally cache the parsed child references per definition instead of re-running
      `re.findall` + `Definition` construction on every visit.
- [ ] This makes `get_dag` linear (`O(V + E)`) regardless of how many times a term is referenced.

### 5. Rethink the category concept

Maybe we should remove it and sort the index topologically. Then on the web app filters view we have a flat list of definitions sorted topologically.

### 2. What to do with something named twice with different names?

- [ ] hashmap (what to do with something named twice with different names?)
- [ ] grid (need a logic handling definitions named with multiple names? grid is the same as matrix, with exchangeable usage)

### 3. New definitions

- [ ] unix-style file system (does it belong here? It seems more related to file systems and OS concepts)
- [ ] simplified canonical path (does it belong here? It seems more related to file systems and OS concepts)

## DONE

### 1. Add DSA definitions found during doing LeetCode exercises

- [x] Two Pointers Technique
- [x] palindrome
- [x] subsequence
- [x] subarray
- [x] random/randomness
- [x] Sliding Window Technique
- [x] index
- [x] transposing (matrix)
- [x] hash set
- [x] infinity
- [x] isomorphic (string)
- [x] bijection
- [x] isomorphism
- [x] anagram
- [x] interval
- [x] merge
- [x] Reverse Polish notation
- [x] Floyd's Tortoise and Hare algorithm
- [x] in-place
- [x] Head-insertion (or pre-pending)
- [x] partition
- [x] LRU cache
- [x] symmetry
- [x] preorder/inorder/postorder traversal
- [x] lowest common ancestor
- [x] deep copy
- [x] Kahn's Algorithm (https://www.geeksforgeeks.org/dsa/topological-sorting-indegree-based-solution/)
- [x] bidirectional BFS
- [x] trie
- [x] Backtracking
- [x] bitmask
- [x] height-balanced binary search tree
- [x] quadtree
- [x] Kadane's algorithm
- [x] peak
- [x] median
- [x] Hamming weight
- [x] commutative operation
- [x] XOR swap algorithm
- [x] Patience sorting
- [x] bisect
- [x] Levenshtein distance
- [x] 1D DP
- [x] Multidimensional DP
