# Non-Linear Data Structure (Assessments 3.3 and 3.6)

Binary Tree and Graph built from the last name **SAMSON**, with BFS and DFS traversals.
Assessment 3.6 adds the DFS methods (preorder, inorder, postorder) on the tree from Assessment 3.5.

## Folder structure
```
SAMSON2F_CC204/
├── main.py                       # run this file
├── common.py                     # shared display helpers
├── part_a_binary_tree/
│   └── binary_tree.py            # Part A: binary tree, BFS, DFS
├── part_b_graph/
│   └── graph.py                  # Part B: graph, BFS, DFS
└── part_c_dfs_tree/
    └── dfs_tree.py               # Part C (3.6): preorder, inorder, postorder
```

## How to run
```
python main.py
```

## Results
| Part | BFS | DFS |
|------|-----|-----|
| A: Binary Tree | S - A - M - S - O - N | S - A - S - O - M - N |
| B: Graph | S - S - A - N - M - O | S - S - N - O - M - A |

### Part C (Assessment 3.6): DFS methods
| Method | Result |
|--------|--------|
| Preorder | C - H - R - S - A - L - M - S - A - E - O - N - S |
| Inorder | S - R - A - H - M - L - S - C - O - E - N - A - S |
| Postorder | S - A - R - M - S - L - H - O - N - E - S - A - C |
