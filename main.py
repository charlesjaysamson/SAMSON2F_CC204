"""
Assessment 3.3: Non-Linear Data Structure
Binary Tree and Graph using the last name SAMSON
Run:  python main.py
"""
from common import LINE
from part_a_binary_tree import binary_tree
from part_b_graph import graph


def main():
    print(LINE)
    print(" ASSESSMENT 3.3: NON-LINEAR DATA STRUCTURE")
    print(" Last name: SAMSON")
    print(LINE)

    binary_tree.run()   # Part A
    print("\n" + LINE)
    graph.run()         # Part B
    print("\n" + LINE)


if __name__ == "__main__":
    main()
