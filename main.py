"""
Assessment 3.3: Non-Linear Data Structure (Binary Tree and Graph, last name SAMSON)
Assessment 3.6: DFS Methods in Tree (Preorder, Inorder, Postorder)
Run:  python main.py
"""
from common import LINE
from part_a_binary_tree import binary_tree
from part_b_graph import graph
from part_c_dfs_tree import dfs_tree


def main():
    print(LINE)
    print(" ASSESSMENT 3.3 AND 3.6")
    print(" Last name: SAMSON")
    print(LINE)

    binary_tree.run()   # Part A
    print("\n" + LINE)
    graph.run()         # Part B
    print("\n" + LINE)
    dfs_tree.run()      # Part C (Assessment 3.6)
    print("\n" + LINE)


if __name__ == "__main__":
    main()
