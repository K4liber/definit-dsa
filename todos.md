# Definit-DB TODOs

As much as possible, the items should be prioritized in order of importance. We split the items into 4 categories:
- IN PROGRESS: Items that are currently being worked on.
- TODO: Items that are planned to be implemented in the future.
- DONE: Items that have been completed.
- ABANDONED: Items that are no longer being pursued, but are kept for historical purposes.

Each item should have a title, a description, and a list of tasks to be completed. The tasks should be checkboxes that can be checked off as they are completed. Each item should also have a category [FEATURE, BUG, DOCS, or OTHER] to indicate the type of work being done. If a task depends on another task, it should be indicated next to the category e.g. [FEATURE, depends on 1].

## IN PROGRESS

## TODO

### 12. [FEATURE] Add a new group

- [ ] "Data Structures and Algorithms" as a initial group with all the so far created definitions in it.

### 13. [FEATURE, depends on: 12] Simplify filtering

Filtering should have only 3 options:
- "Include descendants" (boolean, default: true)
- "Definitions" (list of definitions, default: "ready to learn" definitions)
- "Groups" (list of groups, default: none)

- [ ] Update the visualization package to use the new filtering options.
- [ ] Add a button "Reset filters" to reset the filters to the default values.

### 9. [FEATURE, depends on: 13] Introduce React Router

Apply filtering based on URL parameters and query strings. If no parameter is provided, use the default values. This will allow sharing links to specific filtered views. The filtering should be stored in the browser storage so that the user can return to the same filtered view after closing the browser. The "Reset filters" button should reset the filters to the default values, update the URL accordingly and clear the browser storage.

### 15. [FEATURE] Update "Progress" tab

For sure, we should display a progress bar. To be discussed how to improve it further.

### 14. [BUG] Definition content locked into previous scroll

When marking as learned, the scroll position of the definition content is locked into the previous scroll position. This is a bug and it cannot be scroll up, one need to switch a tab (e.g. to "Filters" and back) to reset the scroll position.

### 11. [FEATURE] Handling multiple definition sources/databases

### 10. [FEATURE] Limit number of nodes on visualization to 200

Add a pop-up window whenever filtering allows more than 200 nodes.

Figure out conditions for limiting the number of nodes displayed.

We could go for 200 most low-level (according to topological sorting) definitions after filters are applied. Then we could "cut-off" the already-learned definitions.

### 7. [FEATURE] Asking question instead of "Mark as learned"

### 8. [FEATURE] Create a json serializer compatible with the definit-visualization package

- [ ] Remove the JS-based serializer.
- [ ] Create a Python-based serializer that outputs a JSON file compatible with the definit-visualization package.

## DONE

### 2. [FEATURE] Add definition aliases

- [x] Create a aliases_index.md listing all definitions. Each line should be "- [ ] <definition name>" where checkbox indicates if we created aliases for that definition or not. The list should be sorted alphabetically.
- [x] Use the aliases_index.md to track the current progress of adding aliases. Take next 10 definitions from the list that are not checked and propose aliases for them. Propose aliases for definitions that have a common name (e.g. "DFS" for "Depth-First Search", "BFS" for "Breadth-First Search", "element" for "item", "grid" for "matrix", etc.) Ask [HUMAN] to review and approve the proposed aliases. Once approved, add the aliases to the definitions and mark them as done in the aliases_index.md. If there are no alias added for a defintion, mark it as well, not all definitions have aliases, but we should try to add them for as many as possible.
- [x] Add aliases in the UI. Under the Definition tab, under the definition name, we have a key (field/defintion_name) html element. Instead of this element, we should have an element displaying: "field: xxx, aliases: x, y, z ...".

### 5. [FEATURE] Remove categories from definitions

- [x] Update the definitions and python scripts
- [x] Update the visualization package to not use categories anymore

### 4. Review all definitions

- [x] Create a `review_definition.md` instruction file for how to review a definition
- [x] Check if they are accurate, complete and have all possible references to other definitions
- [x] Read them all for the final time on the app

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

## ABANDONED

### 3. [FEATURE] New definitions

- [ ] unix-style file system (does it belong here? It seems more related to file systems and OS concepts)
- [ ] simplified canonical path (does it belong here? It seems more related to file systems and OS concepts)

Abandoned because those will wait until a whole new module is created.
